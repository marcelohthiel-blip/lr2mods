from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import diamond_ring, braided_bun, diamond_pubes
from game.sex_positions._position_definitions_ren import standing_grope, kissing
from game.game_roles._role_definitions_ren import critical_job_role
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, list_of_instantiation_functions, christina, emily, city_rep
from game.major_game_classes.game_logic.Position_ren import Position
from game.personality_types._personality_definitions_ren import reserved_personality
TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_christina_character")


def create_christina_character():
    ### CHRISTINA (EMILY'S MOM) ###
    christina_wardrobe = wardrobe_from_xml("Christina_Wardrobe")
    #original height = 0.94
    christina_base = Outfit("Christina's accessories")
    christina_base.add_accessory(diamond_ring.get_copy(), [1.0, 0.84, 0, 0.95])

    global christina
    christina = make_person(name = "Christina", last_name = "Vandenberg", age_range = [44, 47], body_type = "curvy_body", face_style = "Face_8", tits = "DD", height = 0.96,
        hair_colour = ["chestnut", [0.59, 0.31, 0.18, 0.95]], hair_style = braided_bun, pubes_style = diamond_pubes, skin = "white",
        eyes = "light blue", personality = reserved_personality, starting_wardrobe = christina_wardrobe, stat_array = [4, 2, 3], skill_array = [2, 1, 1, 1, 5], sex_skill_array = [2, 3, 3, 2],
        sluttiness = 10, obedience = 105, happiness = 85, love = 0, start_home = emily.home, relationship = "Married", kids = 2, base_outfit = christina_base,
        job = JobDefinition("Trophy Wife", critical_job_role),
        forced_opinions = [
            ["dresses", 2, False],
            ["skirts", 1, False],
            ["high heels", 1, False],
            ["the colour black", 2, False],
            ["the colour red", 1, False],
            ["the colour yellow", 1, False],
            ["the colour pink", -2, False]],
        forced_sexy_opinions = [
            ["being submissive", 1, False],
            ["kissing", 1, False],
            ["cheating on men", 1, False],
            ["anal sex", -1, False]
            ],
        work_experience = 3, type="story")

    christina.set_schedule(christina.home) #She's a stay-at-home Mom.
    christina.home.add_person(christina)
    christina.home.background_name = "Luxury_Apartment_Background"
    christina.home.darken = False

    town_relationships.update_relationship(christina, emily, "Daughter", "Mother")
    #Note: She plays an important role to Emily's story, but she is just given the normal affair role during the game.

##############
# Story Info #
##############

def christina_story_character_description():
    return "Neglected wife and mother of [emily.fname], a student who you are helping with her lessons."

def christina_story_lust_list():
    lust_story_list = {}

    if not christina.is_willing(kissing):
        lust_story_list[0] = "Keep tutoring her daughter [emily.fname] to unlock the home dinner (Marks >= 60%)."
    else:
        lust_story_list[0] = "After a tutoring session she can invite you to dinner, giving you the option to corrupt her further."

        lust_story_list[1] = "This story step has not yet been written."

    return lust_story_list

def christina_story_lust_is_complete():
    return christina.is_willing(kissing)

def christina_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (emily, "[emily.fname] and [christina.fname], a mother daughter pair that seems made for fucking."),
        1: (city_rep, "You wonder if she runs in the same social circles as [city_rep.fname]..."),
    }
    return teamups

def christina_story_other_list():
    other_story_list = {}
    #christinas other story index:
    # 0 - Her current affair status
    # 1 - Her current involvement with training of Emily
    # 2 - Her council influence

    if christina.is_affair:
        other_story_list[0] = "You are currently in an affair with [christina.title]."
    elif christina.is_girlfriend:
        other_story_list[0] = "You broke up her marriage and you are now dating [christina.fname]."
    elif christina.is_single:
        other_story_list[0] = "You broke up her marriage and [christina.fname] is now single."
    else:
        other_story_list[0] = "[christina.fname] is married to a powerful business owner."

    other_story_list[1] = "[christina.fname] is paying the bills for you to tutor her daughter."

    other_story_list[2] = "[christina.fname] has no influence over her husband and his company."

    return other_story_list

####################
# Position Filters #
####################

def christina_foreplay_position_filter(foreplay_position: Position):
    # only allow groping until kissed
    if christina.event_triggers_dict.get("student_mom_door_kiss", 0) == 0:
        return foreplay_position == standing_grope
    return True

def christina_oral_position_filter(oral_position: Position):
    # for now unlock after kiss
    return christina.event_triggers_dict.get("student_mom_door_kiss", 0) != 0

def christina_vaginal_position_filter(vaginal_position: Position):
    # for now unlock after few blowjobs with swallow
    return christina.cum_mouth_count > 3

def christina_anal_position_filter(anal_position: Position):
    # for now unlock after few creampies
    return christina.vaginal_creampie_count > 3

def christina_oral_position_info():
    return "Complete the invite to dinner event"

def christina_vaginal_position_info():
    count = 4 - christina.cum_mouth_count
    return f"Cum in her mouth {count} more times"

def christina_anal_position_info():
    count = 4 - christina.vaginal_creampie_count
    return f"Give her {count} more creampies"
