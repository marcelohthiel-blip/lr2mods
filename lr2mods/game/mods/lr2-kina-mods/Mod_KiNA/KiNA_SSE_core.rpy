# SERUM SIDE EFFECT MOD CORE TWEAK by KiNA (OC by Trist)
# It's used for adding new Side Effect SerumTraits to the game
# Create a SideEffectTraitMod class, it has the same parameters as the VREN Action class.
# SerumTraitMod is added to save games when not present, the matching is based on the name property, so make sure it's unique.

### TEMPLATE ###
# init -1 python:
#     def anorexia_serum_on_turn(person, add_to_log):
#         return person.change_weight(amount = -.2, chance = 20)

# # any label that starts with serum_mod is added to the serum mod list
# label serum_mod_anorexia_serum_trait(stack):
#     python:
#         anorexia_serum_trait = SerumTraitMod(name = "Anorexia Serum",
#             desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centers to inhibit hunger and calorie intake.",
#             positive_slug = "-$15 Value, 20% Chance/Turn to reduce body mass by 200 grams",
#             negative_slug = "",
#             value_added = -15,
#             research_added = 125,
#             on_turn = anorexia_serum_on_turn,
#             is_side_effect = True,
#             
#         # continue on the hijack stack if needed
#         execute_hijack_call(stack)
#     return

init 30 python:
    add_label_hijack("normal_start", "activate_side_effect_core")
    add_label_hijack("after_load", "update_side_effect_core")

init python:
    def kina_init_side_effect_traits():
        global list_of_side_effects

        # check if SideEffectTraitMod class is already in the game append if needed and update serum_mod_list / list_of_side_effects list
        for serum_mod in SideEffectTraitMod._instances:
            if not serum_mod in list_of_side_effects:
                write_log(f"Add side effect trait mod: {serum_mod.name}")
                list_of_side_effects.append(serum_mod)
                serum_mod.update_serum_trait()


    # find all side effect trait mods, and append the creation to the stack
    def append_side_effect_mods_to_stack(stack):
        for game_label in renpy.get_all_labels():
            if game_label.startswith("side_effect_mod_"):
                stack.append(game_label)
        return stack


label activate_side_effect_core(stack):
    #$ list_of_side_effects = set()
    python:
        list_of_side_effects = []

        init_side_effect_traits()
        
        stack = append_side_effect_mods_to_stack(stack)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    # execute after stack has run
    $ kina_init_side_effect_traits()
    return

label update_side_effect_core(stack):
    python:
        stack = append_side_effect_mods_to_stack(stack)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)

    # execute after stack has run
    $ kina_init_side_effect_traits()
    return
