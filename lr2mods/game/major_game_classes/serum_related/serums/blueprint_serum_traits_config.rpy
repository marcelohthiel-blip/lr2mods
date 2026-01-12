#Holds all of the info for SerumTraitBlueprints, which generate new unique traits when unlocked (to allow a single trait to do variations of the same action.)
label name_blueprint_trait(new_trait, effect_label): #This is called first to ensure all new traits are properly given a new name.
    $ renpy.call(effect_label, new_trait)
    if new_trait in mc.business.blueprinted_traits: #If the effect_label has removed the trait from the blueprinted list it means something failed and the design has not actually been made.
        $ new_trait.name = renpy.input("Give this trait a name.", default = new_trait.name, exclude="[]{}")
        while len(new_trait.name) < 3:
            $ new_trait.name = renpy.input("Give this trait a name.", default = new_trait.name, exclude="[]{}")
    return

label basic_hair_dye_unlock_label(new_trait):
    $ goal_colour = None
    $ hair_list = []
    python:
        for base_hair_colour in Person.get_list_of_hairs():
            hair_colour = Person.generate_hair_colour(base_hair_colour[0]) # Generate a variant hair colour so we don't apply the exact same thing every time.
            hair_descriptor = hair_colour[0]
            hair_colour = Color(rgb=(hair_colour[1][0], hair_colour[1][1], hair_colour[1][2]))
            hair_list.append(("{color=" + hair_colour.hexcode + "}" + hair_descriptor.capitalize()+"{/color}", hair_colour))

    $ renpy.say(None,"Select target hair colour.", interact = False)
    $ chosen_colour = renpy.display_menu(hair_list, screen = "choice")

    $ new_trait.on_turn = partial(hair_colour_change_on_turn, chosen_colour)
    $ new_trait.desc += "\n{color=" + chosen_colour.hexcode + "}" + " This is the target colour." + "{/color}"
    $ chosen_colour = None
    return

label hair_colour_change_unlock_label(new_trait):
    call screen colour_selector(title = "Pick the target hair colour.")
    python:
        return_colour = Color(rgb = _return.rgb, alpha = .95)
        new_trait.on_turn = partial(hair_colour_change_on_turn, return_colour) #Generates a partially filled function
        new_trait.desc += "\n{color=" + return_colour.hexcode + "}" + " This is the target colour." + "{/color}"
        del return_colour
    return

label eye_colour_change_unlock_label(new_trait):
    call screen colour_selector(title = "Pick the target eye colour.")
    python:
        return_colour = Color(rgb = _return.rgb, alpha = .95)
        new_trait.on_turn = partial(eye_colour_change_on_turn, return_colour) #Generates a partially filled function
        new_trait.desc += "\n{color=" + return_colour.hexcode + "}" + " This is the target colour." + "{/color}"
        del return_colour
    return

label breast_milk_serum_production_unlock_label(new_trait):
    call screen review_designs_screen(show_traits = False, select_instead_of_delete = True)
    $ return_design = _return
    if isinstance(return_design, SerumDesign):

        $ new_trait.on_apply = partial(breast_milk_serum_production_on_apply, return_design)
        $ new_trait.on_remove = partial(breast_milk_serum_production_on_remove, return_design)
        $ new_trait.desc += "\nProduces: " + return_design.name

    else:
        $ mc.add_clarity(new_trait.clarity_cost)
        $ mc.business.remove_trait(new_trait)
        $ mc.business.active_research_design = None
    return
