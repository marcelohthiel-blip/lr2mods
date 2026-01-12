from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import twintail, shaved_pubes
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Room_ren import university
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, emily, christina
from game.major_game_classes.character_related._job_definitions_ren import student_job
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.sex_positions._position_definitions_ren import kissing, standing_grope
from game.people.Emily.emily_role_definition_ren import init_emily_roles

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
list_of_instantiation_functions.append("create_emily_character")

def create_emily_character():
    ### EMILY (18) ###
    emily_wardrobe = wardrobe_from_xml("Emily_Wardrobe")
    #original height = 0.91
    emily_base = Outfit("Emily's accessories") #TODO: Decide on what her wardrobe should look like. Also decide on name colour

    init_emily_roles()

    global emily
    emily = make_person(name = "Emily", last_name = "Vandenberg", age_range = [18, 20], body_type = "thin_body", face_style = "Face_8", tits = "C", height = 0.915, hair_colour = "chestnut", hair_style = twintail, pubes_style = shaved_pubes, skin = "white",
        eyes = "light blue", personality = relaxed_personality, starting_wardrobe = emily_wardrobe, stat_array = [3, 2, 1], skill_array = [2, 1, 1, 1, 2], sex_skill_array = [3, 1, 1, 0], job = student_job,
        sluttiness = 6, obedience = 100, happiness = 100, love = 0, relationship = "Single", kids = 0, base_outfit = emily_base,
        forced_opinions = [
            ["pants", 1, False],
            ["skirts", 1, False],
            ["the colour purple", 2, False],
            ["the colour black", 2, False]],
        forced_sexy_opinions= [
            ["kissing", 1, False],
            ["being submissive", 1, False]],
        work_experience = 1, type="story")

    #Remember base Focus/Int so you get credit for any academic enhancing things you do (or punished for reducing them)
    emily.event_triggers_dict["initial_int"] = emily.int
    emily.event_triggers_dict["initial_focus"] = emily.focus
    emily.generate_home().add_person(emily)
    emily.set_override_schedule(emily.home)

##############
# Story Info #
##############

def emily_story_character_description():
    return "A university student that asked you to help her with her studies."

def emily_story_love_list():
    love_story_list = {}

    if not emily.event_triggers_dict.get("tutor_enabled", False):
        love_story_list[0] = "You haven't offered to tutor her yet."
        return love_story_list

    love_story_list[0] = "You have accepted to tutor [emily.fname]."
    love_story_list[1] = "This next event is not yet written."

    return love_story_list

def emily_story_love_is_complete():
    return emily.event_triggers_dict.get("tutor_enabled", False)

def emily_story_lust_list():
    lust_story_list = {}

    if not emily.event_triggers_dict.get("tutor_enabled", False):
        lust_story_list[0] = "You haven't offered to tutor her yet."
        return lust_story_list

    lust_story_list[0] = "You have accepted to tutor [emily.fname]."
    lust_story_list[1] = "This next event is not yet written."

    return lust_story_list

def emily_story_lust_is_complete():
    return emily.event_triggers_dict.get("tutor_enabled", False)

# def emily_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

def emily_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (christina, "[emily.fname] and [christina.fname], a mother daughter pair that seems made for fucking."),
    }
    return teamups

def emily_story_other_list():
    other_story_list = {}
    #emily's other story index:
    # 0 - Her current tutor status
    # 1 - Her current involvement with training of Emily
    # 2 - Her council influence

    if not emily.event_triggers_dict.get("tutor_enabled", False):
        other_story_list[0] = "You haven't offered to tutor her yet."
    else:
        other_story_list[0] = "You are tutoring [emily.fname]."

    return other_story_list


####################
# Position Filters #
####################

def emily_foreplay_position_filter(foreplay_position: Position):
    # unlock after tutor enabled
    if not emily.event_triggers_dict.get("tutor_enabled", False):
        return False

    # first only unlock kissing and groping
    if emily.event_triggers_dict.get("student_masturbate", 0) < 3:
        return foreplay_position in (kissing, standing_grope)

    return True

def emily_oral_position_filter(oral_position: Position):
    # at least one blowjob punishment
    return emily.event_triggers_dict.get("study_blowjob_level", 0) != 0

def emily_vaginal_position_filter(vaginal_position: Position):
    # cum during punishment or at least 3 other blowjobs with swallow
    return emily.event_triggers_dict.get("study_blowjob_level", 0) > 1 \
        or emily.cum_mouth_count > 3

def emily_anal_position_filter(anal_position: Position):
    # for now unlock after a few creampies
    return emily.vaginal_creampie_count > 3

def emily_oral_position_info():
    return "Make her give you a blowjob during study event"

def emily_vaginal_position_info():
    count = 4 - emily.cum_mouth_count
    return f"Cum in her mouth {count} more times or make her swallow during blowjob study punishments"

def emily_anal_position_info():
    count = 4 - emily.vaginal_creampie_count
    return f"Give her {count} more creampies"
