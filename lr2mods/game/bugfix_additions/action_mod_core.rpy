# ACTION MOD CORE by Tristimdorion
# Create a ActionMod class, it has the same parameters as the VREN Action class.
# Attach the ActionMod object to any action list in the game.
# If you need some extra initialization after the game has started pass an initialization function (None is default)
# ActionMod is added to save games when not present, the matching is based on the name property, so make sure it's unique (and don't change it between releases)

# pre define variable for saving
define action_mod_list = None

init -1 python:
    # Initialize the randomizer
    renpy.random.seed()

    def action_mod_settings_requirement():
        return True

    def action_mod_configuration_requirement():
        return any(x for x in ActionMod._instances if x.options_menu)

    # check all ActionMod classes in the game and make sure we have one instance of each and update the action_mod_list
    def append_and_initialize_action_mods():
        # add action_mod instances to list
        if not ActionMod._instances is None:
            # renpy.say(None, "There are " + str(builtins.len(action_mod_list)) + " mods in save game.")
            for action_mod in sorted(ActionMod._instances, key = lambda x: x.priority):
                write_log("Load action mod: {}".format(action_mod.name))
                if action_mod not in action_mod_list:
                    action_mod_list.append(action_mod)
                    action_mod.initialize()

        # clean-up removed actions
        for action_mod in action_mod_list:
            if action_mod not in ActionMod._instances:
                action_mod_list.remove(action_mod)

        # the crisis_list is not stored in save game
        for action_mod in action_mod_list:
            if action_mod.is_crisis:
                if action_mod.is_morning_crisis:
                    if not action_mod in morning_crisis_list:
                        morning_crisis_list.append(action_mod)
                else:
                    if not action_mod in crisis_list:
                        crisis_list.append(action_mod)
            elif action_mod.is_mandatory_crisis:
                if action_mod.is_morning_crisis:
                    mc.business.add_mandatory_morning_crisis(action_mod)
                else:
                    mc.business.add_mandatory_crisis(action_mod)
        return

    def build_action_mod_configuration_menu():
        tuple_list = []
        for action_mod in action_mod_list:
            if action_mod.enabled and hasattr(action_mod, "options_menu") and not action_mod.options_menu is None:
                tuple_string = f"{action_mod.name} (tooltip){action_mod.menu_tooltip}"
                tuple_list.append((tuple_string, action_mod))

        tuple_list = sorted(tuple_list, key=lambda x: x[0])
        tuple_list.append(("Back","Back"))
        return renpy.display_menu(tuple_list, True, "Choice")

    # mod settings action
    action_mod_options_action = Action("MOD Settings", action_mod_settings_requirement, "show_action_mod_settings", menu_tooltip = "Enable or disable mods")
    action_mod_configuration_action = Action("MOD Configuration", action_mod_configuration_requirement, "show_action_mod_configuration", menu_tooltip = "Change configuration for individual MODS")

init 15 python: # NOTE: Having it at 5 was causing errors after I moved things around. Haven't seen any side effects of it.
    add_label_hijack("normal_start", "activate_action_mod_core")
    add_label_hijack("after_load", "update_action_mod_core")

# as long as VREN doesn't use this, we need to add a dummy label for hijacking purposes
# NOTE: this label gets called after the hijack labels have been triggered
label after_load():
    python:
        perk_system.save_load()
        update_fetish_unlock_list()
        show_ui()
    return

label activate_action_mod_core(stack):
    # define here using $ so it gets stored in save game
    python:
        append_and_initialize_action_mods()

        bedroom.add_action(action_mod_options_action)
        bedroom.add_action(action_mod_configuration_action)
        bedroom.add_action(character_poser_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

# called after loading a save game
label update_action_mod_core(stack):
    python:
        append_and_initialize_action_mods()

        bedroom.add_action(action_mod_options_action)
        bedroom.add_action(action_mod_configuration_action)
        bedroom.add_action(character_poser_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_action_mod_settings():
    $ hide_ui()
    call screen mod_configuration_ui()
    $ show_ui()
    return

label show_action_mod_configuration():
    python:
        action_mod_choice =  build_action_mod_configuration_menu()

        if action_mod_choice == "Back":
            renpy.return_statement()
        else:
            action_mod_choice.show_options()
    jump show_action_mod_configuration
