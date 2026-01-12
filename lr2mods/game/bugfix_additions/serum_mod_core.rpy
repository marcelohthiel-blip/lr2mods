# SERUM MOD CORE by Tristimdorion
# It's used for adding new SerumTraits to the game
# Create a SerumTraitMod class, it has the same parameters as the VREN Action class.
# SerumTraitMod is added to save games when not present, the matching is based on the name property, so make sure it's unique.

### TEMPLATE ###
# init -1 python:
#     def anorexia_serum_on_turn(person, add_to_log):
#         return person.change_weight(amount = -.2, chance = 20)

# # any label that starts with serum_mod is added to the serum mod list
# label serum_mod_anorexia_serum_trait(stack):
#     python:
#         anorexia_serum_trait = SerumTraitMod(name = "Anorexia Serum",
#             desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centres to inhibit hunger and calorie intake.",
#             positive_slug = "-$15 Value, 20% Chance/Turn to reduce body mass by 200 grams",
#             negative_slug = "",
#             value_added = -15,
#             research_added = 125,
#             base_side_effect_chance = 20,
#             on_turn = anorexia_serum_on_turn,
#             requires = basic_med_app,
#             tier = 1,
#             research_needed = 500)

#         # continue on the hijack stack if needed
#         execute_hijack_call(stack)
#     return

init 20 python:
    add_label_hijack("normal_start", "activate_serum_mod_core")
    add_label_hijack("after_load", "update_serum_mod_core")

init 2 python:
    def initialize_serum_mod_traits():
        global serum_mod_list

        # check if SerumMod class is already in the game append if needed and update serum_mod_list / list_of_traits list
        for serum_mod in SerumTraitMod._instances:
            if not serum_mod in serum_mod_list:
                write_log(f"Add serum mod: {serum_mod.name}")
                serum_mod_list.add(serum_mod)
                serum_mod.update_serum_trait()


    # find all serum mods, and append the creation to the stack
    def append_serum_mods_to_stack(stack):
        for game_label in renpy.get_all_labels():
            if game_label.startswith("serum_mod_"):
                stack.append(game_label)
        return stack


label activate_serum_mod_core(stack):
    $ serum_mod_list = set()
    python:
        stack = append_serum_mods_to_stack(stack)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    # execute after stack has run
    $ initialize_serum_mod_traits()
    return

label update_serum_mod_core(stack):
    python:
        stack = append_serum_mods_to_stack(stack)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    # execute after stack has run
    $ initialize_serum_mod_traits()
    return
