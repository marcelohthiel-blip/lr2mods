init -1 python:
    def personality_change_on_apply(goal_personality, the_person, the_serum, add_to_log):
        the_person.change_personality(goal_personality)
        return

    def personality_menu():
        temp_list = []
        for x in list_of_personalities:
            if isinstance(x.personality_type_prefix, str):
                temp_string = str.capitalize(x.personality_type_prefix) + " Personality"
                temp_list.append([temp_string, x])
        return temp_list

init 1 python:
    personality_trait = SerumTraitBlueprint(
        unlock_label = "personality_unlock_label",
        name = "Personality Change",
        desc = "Instantly alters the core of the subject's personality.",
        positive_slug = "Changes Personality",
        negative_slug = "",
        research_added = 600,
        base_side_effect_chance = 100,
        tier = 3,
        research_needed = 3000,
        clarity_cost = 3300,
        mental_aspect = 10, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 3)

init 16 python:
    add_label_hijack("instantiate_serum_trait_blueprints", "instantiate_instant_personality_blueprint")
    add_label_hijack("after_load", "instantiate_instant_personality_blueprint")

label instantiate_instant_personality_blueprint(stack): # Called from instantiate_serum_traits.
    python:
        if not personality_trait in list_of_traits:
            list_of_traits.append(personality_trait)
        if not bimbo_personality in list_of_personalities:
            list_of_personalities.extend((
                bimbo_personality,
                alpha_personality,
                cougar_personality
            ))
        if 'daddy_girl_personality' in globals():
            list_of_personalities.extend((daddy_girl_personality))
        if 'breeding_stock' in globals():
            list_of_personalities.extend((breeding_stock))
        execute_hijack_call(stack)
    return

label personality_unlock_label(new_trait):
    python:
        return_personality = menu(personality_menu())
        temp_text = str.capitalize(return_personality.personality_type_prefix) + " Personality"
        new_trait.on_apply = partial(personality_change_on_apply, return_personality) #Generates a partially filled function
        new_trait.desc += " "+temp_text+" is the target personality."
        new_trait.name += ": "+temp_text
        del return_personality
        del temp_text
    return
