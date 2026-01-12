from __future__ import annotations
from renpy.color import Color
from game.game_roles._role_definitions_ren import lactating_serum_role
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumTraitBlueprint_ren import SerumTraitBlueprint
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import hair_lighten_dye, hair_darken_dye
from game.major_game_classes.serum_related.serums._serum_traits_T1_ren import lactation_hormones
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import advanced_serum_prod

list_of_traits: list[SerumTrait] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

def breast_milk_serum_production_on_apply(target_design, person: Person, serum: SerumDesign, add_to_log: bool):
    if person.add_role(lactating_serum_role):
        person.breast_milk = 0 # set to 0 -> already available milk needs to be converted to serum

    if "lactating_serum_types" in person.event_triggers_dict:
        person.event_triggers_dict["lactating_serum_types"].append(target_design)
    else:
        person.event_triggers_dict["lactating_serum_types"] = [target_design]

def breast_milk_serum_production_on_remove(target_design, person: Person, serum: SerumDesign, add_to_log: bool):
    if target_design in person.event_triggers_dict.get("lactating_serum_types", []):
        person.event_triggers_dict["lactating_serum_types"].remove(target_design)
    if not person.event_triggers_dict.get("lactating_serum_types", []):
        person.remove_role(lactating_serum_role) #If there are no serums to lactate recorded we can safely remove the role - needed in case you double dose her with this production serum.
        person.breast_milk = 0 # set to 0 -> already available serum needs to be converted to milk

## Blueprint Traits ###

# these have enhanced signatures that are partially filled on creation
def hair_colour_change_on_turn(goal_colour, person: Person, serum: SerumDesign, add_to_log: bool): #NOTE: This function must be partially filled and assigned when the blueprint is realised.
    change_per_turn = 1.0 / max(serum.duration - 1, 2)

    if isinstance(person.hair_colour, (list, tuple, set)):
        current_colour_raw = person.hair_colour[1] #NOTE: Hair colour also comes with a descriptor, but we need a way to override/replace that at some point in the future.
        if not isinstance(current_colour_raw, list):
            current_colour_raw = [0.15, 0.15, 0.15, .95]
    else:
        current_colour_raw = [0.15, 0.15, 0.15, .95]

    if len(current_colour_raw) == 3:    # append the alpha channel if needed
        current_colour_raw.append(.95)

    current_colour = Color(rgb=(current_colour_raw[0], current_colour_raw[1], current_colour_raw[2]), alpha = current_colour_raw[3]) #Generate a proper Colour object
    new_colour = current_colour.interpolate(goal_colour, change_per_turn) #Each turn it gets 30% closer to the goal (but never _quite_ gets there).
    person.set_hair_colour(new_colour, change_pubes = False)

def eye_colour_change_on_turn(goal_colour, person: Person, serum: SerumDesign, add_to_log: bool):
    change_per_turn = 1.0 / max(serum.duration - 1, 2)

    if isinstance(person.eyes, (list, tuple, set)):
        current_colour_raw = person.eyes[1]
        if not isinstance(current_colour_raw, list):
            current_colour_raw = [0.15, 0.15, 0.15, .95]
    else:
        current_colour_raw = [0.15, 0.15, 0.15, .95]

    if len(current_colour_raw) == 3:    # append the alpha channel if needed
        current_colour_raw.append(.9)

    current_colour = Color(rgb=(current_colour_raw[0], current_colour_raw[1], current_colour_raw[2]), alpha = current_colour_raw[3]) #Generate a proper Colour object
    new_colour = current_colour.interpolate(goal_colour, change_per_turn) #Each turn it gets 30% closer to the goal (but never _quite_ gets there).
    person.set_eye_colour(new_colour)

def init_blueprint_traits():
    # Tier 1
    global basic_hair_dye_trait
    basic_hair_dye_trait = SerumTraitBlueprint(
        unlock_label = "basic_hair_dye_unlock_label",
        name = "Encapsulated Hair Dyes",
        desc = "Precise delivery of commonly available hair dyes re-colours the targets hair over the course of hours. Only a limited ranges of hair colours are suitable for this procedure.",
        positive_slug = "Shifts Hair Colour Towards Selected Preset Colour",
        negative_slug = "",
        research_added = 40,
        base_side_effect_chance = 5,
        requires = [hair_lighten_dye, hair_darken_dye],
        tier = 1,
        research_needed = 100,
        exclude_tags = "Dye",
        clarity_cost = 50,
        mental_aspect = 0, physical_aspect = 4, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 1)

    # Tier 2
    global hair_dye_trait
    hair_dye_trait = SerumTraitBlueprint(
        unlock_label = "hair_colour_change_unlock_label",
        name = "Organic Hair Chemicals",
        desc = "Triggers the production of natural hair dyes, which quickly re-colours the subject's hair over the course of hours. Application for several days is suggested for perfect colour accuracy. Test on hidden patch first.",
        positive_slug = "Shifts Hair Colour Towards Set Target Colour",
        negative_slug = "",
        research_added = 80,
        base_side_effect_chance = 20,
        requires = [hair_lighten_dye, hair_darken_dye],
        tier = 2,
        research_needed = 400,
        exclude_tags = "Dye",
        clarity_cost = 300,
        mental_aspect = 0, physical_aspect = 7, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 2)

    global eye_dye_trait
    eye_dye_trait = SerumTraitBlueprint(
        unlock_label = "eye_colour_change_unlock_label",
        name = "Ocular Dyes",
        desc = "Modifies the cells of the subject's iris, causing them to change to the target colour over the course of hours. This method can achieve eye colours not normally seen.",
        positive_slug = "Shifts Eye Colour Towards Set Target Colour",
        negative_slug = "",
        research_added = 40,
        base_side_effect_chance = 40,
        requires = [hair_lighten_dye, hair_darken_dye],
        tier = 2,
        research_needed = 200,
        clarity_cost = 150,
        mental_aspect = 0, physical_aspect = 6, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 1)

    global breast_milk_serum_production
    breast_milk_serum_production = SerumTraitBlueprint(name = "Serum Lactation",
        unlock_label = "breast_milk_serum_production_unlock_label",
        desc = "Temporarily reprograms the mammary glands of the subject, causing them to produce the selected Serum Design along with their natural milk when they lactate. The number of doses that can be collected depends primarily on the subject's breast size and lactation intensity, although other factors are suspected to exist.",
        positive_slug = "0 Slots, 6 Turn Duration, Lactation Produces Serum Milk",
        negative_slug = "",
        research_added = 1200,
        slots_added = 0,
        production_added = 120,
        duration_added = 6,
        base_side_effect_chance = 100,
        clarity_added = 500,
        on_apply = breast_milk_serum_production_on_apply,
        on_remove = breast_milk_serum_production_on_remove,
        # on_turn = a_function, #TODO: Decide if we want some sort of on/turn or on/day effect for this.
        # on_day = a_function,
        requires = [lactation_hormones, advanced_serum_prod],
        tier = 2,
        research_needed = 1000,
        exclude_tags = "Production",
        clarity_cost = 1500,
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 2)

    global list_of_traits
    list_of_traits.extend((
        # TIER 1 #
        basic_hair_dye_trait,
        # TIER 2 #
        hair_dye_trait,
        eye_dye_trait,
        breast_milk_serum_production,
    ))
