init -1 python:
    def skin_change_on_apply(new_skin, the_person, the_serum, add_to_log):
        return the_person.match_skin(new_skin)

init 1 python:
    skin_change_trait = SerumTraitBlueprint(
        unlock_label = "skin_change_unlock_label",
        name = "Skin Pigmentation",
        desc = "Triggers instant changes in the way the body produces melanin causing skin tone to shift to the desired pigment.",
        positive_slug = "Alters skin tone",
        negative_slug = "",
        research_added = 80,
        base_side_effect_chance = 20,
        tier = 2,
        research_needed = 400,
        clarity_cost = 300,
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 3)

init 16 python:
    add_label_hijack("instantiate_serum_trait_blueprints", "instantiate_pigment_blueprint")
    add_label_hijack("after_load", "instantiate_pigment_blueprint")

label instantiate_pigment_blueprint(stack): # Called from instantiate_serum_traits.
    python:
        if not skin_change_trait in list_of_traits:
            list_of_traits.append(skin_change_trait)
        execute_hijack_call(stack)
    return

label skin_change_unlock_label(new_trait):
    menu:
        "White":
            $ return_pigment ='white'
            $ temp_text = "White"
        "Tan":
            $ return_pigment = 'tan'
            $ temp_text = "Tan"
        "Black":
            $ return_pigment = 'black'
            $ temp_text = "Black"
    python:
        new_trait.on_apply = partial(skin_change_on_apply, return_pigment) #Generates a partially filled function
        new_trait.desc += " "+temp_text+ " is the target pigment."
        new_trait.name += ": "+temp_text
        del return_pigment
        del temp_text
    return
