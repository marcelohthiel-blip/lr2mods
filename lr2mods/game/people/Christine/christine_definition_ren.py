from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import short_hair
from game.major_game_classes.game_logic.Position_ren import Position
from game.game_roles._role_definitions_ren import critical_job_role
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, police_chief, city_rep
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.game_logic.Room_ren import police_station, mall, downtown, downtown_bar, strip_club
from game.personality_types._personality_definitions_ren import reserved_personality, reserved_player_titles

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_christine_character")

def police_chief_titles(person: Person):
    valid_titles = ["Chief " + person.last_name]
    if person.love > 30:
        valid_titles.append(person.name)
        valid_titles.append("Chief " + person.name)
    if person.has_cum_fetish:
        valid_titles.append("Chief Cumslut")
    if person.sluttiness > 70 and person.opinion.anal_sex > 1:
        valid_titles.append("Chief Buttslut")
    if person.has_anal_fetish:
        valid_titles.append("Chief Cornhole")
    return valid_titles

def police_chief_possessive_titles(person: Person):
    valid_possessive_titles = ["the police chief"]
    if person.love > 30:
        valid_possessive_titles.append("your police chief")
    if person.sluttiness > 40:
        valid_possessive_titles.append("your police bitch")
    if person.sluttiness > 70 and person.opinion.anal_sex > 1:
        valid_possessive_titles.append("your anal cop")
    return valid_possessive_titles


def create_christine_character():
    police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")
    cop_outfit = police_chief_wardrobe.get_outfit_with_name("Cop")
    police_chief_uniform_wardrobe = Wardrobe("Cop Uniform")
    police_chief_uniform_wardrobe.add_outfit(cop_outfit)
    police_chief_wardrobe.remove_outfit(cop_outfit)

    police_chief_personality = Personality("police_chief", default_prefix = reserved_personality.default_prefix,
        common_likes = ["pants", "small talk", "working", "the colour blue", "the colour black", "boots", "sports", "working", "work uniforms"],
        common_sexy_likes = ["taking control", "anal sex", "sex standing up", "anal creampies", "getting head"],
        common_dislikes = ["Mondays", "the colour yellow", "the colour pink", "skirts", "dresses", "high heels", "flirting"],
        common_sexy_dislikes = ["being submissive", "bareback sex", "skimpy outfits", "showing her tits", "showing her ass", "not wearing underwear", "cum facials", "incest"],
        titles_function = police_chief_titles, possessive_titles_function = police_chief_possessive_titles, player_titles_function = reserved_player_titles)

    police_job = JobDefinition("Police Chief", critical_job_role, police_station, time_slots = [1, 2], wardrobe = police_chief_uniform_wardrobe)
    police_job.set_schedule(mall, day_slots = [0, 2, 4], time_slots = [1]) #patrol mall
    police_job.set_schedule(downtown, day_slots = [1, 3], time_slots=[2]) # patrol downtown
    police_job.set_schedule(downtown_bar, day_slots = [5, 6], time_slots=[3]) # patrol bar
    police_job.set_schedule(strip_club, day_slots = [5, 6], time_slots=[4]) # patrol strip club (Does she have a kinky side?)

    global police_chief
    police_chief = make_person(name = "Christine", last_name = "Lavardin", age = 34, body_type = "thin_body", face_style = "Face_4", tits = "C", height = 0.91,
        hair_colour = ["knight red", [.745, .117, .235, 1]], hair_style = short_hair, skin = "white", eyes = "emerald", name_color = "#fcf7de",
        stat_array = [4, 6, 2], skill_array = [2, 1, 4, 1, 2], sex_skill_array = [0, 1, 1, 4], sluttiness = -20, obedience_range = [50, 70], happiness = 89, love = 0,
        generate_insta = False, generate_dikdok = False, generate_onlyfans = False, relationship = "Single", job = police_job,
        kids = 0, starting_wardrobe = police_chief_wardrobe, personality = police_chief_personality,
        forced_opinions = [
            ["pants", 2, False],
            ["the colour blue", 2, True],
            ["the colour black", 1, False],
            ["boots", 2, False],
            ["sports", 1, True],
            ["working", 2, False],
            ["work uniforms", 2, True]],
        forced_sexy_opinions = [
            ["taking control", 2, False],
            ["anal sex", 2, False],
            ["sex standing up", 1, False],
            ["being submissive", -2, False],
            ["skimpy outfits", -2, False],
            ["showing her tits", -1, False],
            ["showing her ass", -1, False],
            ["not wearing underwear", -2, False]],
        serum_tolerance = 1, work_experience = 2, type = 'story')

    police_chief.idle_pose = "stand3"   # forced idle pose
    police_chief.generate_home()
    police_chief.home.add_person(police_chief)
    police_chief.event_triggers_dict["times_arrested"] = 0

def mc_times_arrested():
    return police_chief.event_triggers_dict.get("times_arrested", 0)

##############
# Story Info #
##############

def christine_story_character_description():
    return "Chief of Police that will monitor if people abide by the city laws."


def christine_story_other_list():
    other_info_list = {}

    other_info_list[0] = "When attracting too much attention in public places, she might arrest you."
    if city_rep.event_triggers_dict.get("discussed_topless_is_legal", False):
        other_info_list[1] = "Corrupt the police chief and [city_rep.fname] to unlock the topless and public nudity policies."
    return other_info_list

####################
# Position Filters #
####################

def christine_foreplay_position_filter(foreplay_position: Position):
    # no restrictions for now
    return True

def christine_oral_position_filter(oral_position: Position):
    # for now unlock after few times fingered to orgasm
    return police_chief.sex_record.get("Fingered", 0) > 3

def christine_vaginal_position_filter(vaginal_position: Position):
    # for now unlock after few blowjobs with swallow
    return police_chief.cum_mouth_count > 3

def christine_anal_position_filter(anal_positions: Position):
    # for now unlock after few creampies
    return police_chief.vaginal_creampie_count > 3

def christine_oral_position_info():
    count = 4 - police_chief.sex_record.get("Fingered", 0)
    return f"Finger her {count} more times"

def christine_vaginal_position_info():
    count = 4 - police_chief.cum_mouth_count
    return f"Cum in her mouth {count} more times"

def christine_anal_position_info():
    count = 4 - police_chief.vaginal_creampie_count
    return f"Give her {count} more creampies"
