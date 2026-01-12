from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import modern_glasses, gold_earings, short_hair
from game.game_roles._role_definitions_ren import critical_job_role
from game.major_game_classes.game_logic.Room_ren import university, downtown_bar
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, list_of_instantiation_functions, mc, nora, stephanie
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_nora_traits
from game.personality_types._personality_definitions_ren import reserved_personality
from game.people.Nora.nora_events_ren import add_nora_bar_meetup_initial_meeting_action
from game.people.Nora.nora_role_definition_ren import add_nora_research_intro_action
from game.major_game_classes.business_related.Contract_ren import Contract

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_nora_character")

def nora_titles(person: Person):
    valid_titles = [person.name]
    return valid_titles

def nora_possessive_titles(person: Person):
    valid_titles = [person.name]
    valid_titles.append("your old boss")
    if person.sluttiness > 60:
        valid_titles.append("lab slut")
    return valid_titles

def nora_player_titles(person: Person):
    valid_titles = [mc.name]
    return valid_titles

def nora_reintro_requirement():
    if time_of_day in (0, 4) or mc.business.research_tier < 2 or mc.business.is_weekend:
        return False
    return not mc.business.event_triggers_dict.get("nora_cash_reintro_needed", True)

def create_nora_character():
    ### NORA ##
    nora_wardrobe = wardrobe_from_xml("Nora_Wardrobe")
    #original height = 0.98
    nora_base = Outfit("Nora's accessories")
    nora_base.add_accessory(modern_glasses.get_copy(), [0.09, 0.07, 0.09, 0.95])
    nora_base.add_accessory(gold_earings.get_copy(), [1.0, 1.0, 0.93, 0.95])

    nora_personality = Personality("nora", default_prefix = reserved_personality.default_prefix,
        common_likes = ["working", "classical music"],
        common_sexy_likes = ["vaginal sex", "skimpy uniforms", "lingerie", "masturbating"],
        common_dislikes = ["heavy metal music", "sports", "the colour yellow"],
        common_sexy_dislikes = ["not wearing anything", "not wearing underwear", "creampies"],
        titles_function = nora_titles, possessive_titles_function = nora_possessive_titles, player_titles_function = nora_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global nora_professor_job
    nora_professor_job = JobDefinition("Lecturer", critical_job_role, job_location = university, day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2])

    global nora
    nora = make_person(name = "Nora", age_range = [43, 47], body_type = "standard_body", face_style = "Face_4", tits = "D", height = 1.05, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = short_hair, skin = "white",
        eyes = "grey", personality = nora_personality, name_color = "#dddddd", dial_color = "#dddddd", starting_wardrobe = nora_wardrobe, job = nora_professor_job,
        stat_array = [1, 6, 4], skill_array = [1, 1, 6, 3, 1], sex_skill_array = [2, 4, 3, 1], sluttiness = 4, obedience = 102, happiness = 103, love = 3, suggestibility_range = [2, 7],
        title = "Nora", possessive_title = "your old boss", mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = nora_base,
        forced_opinions = [
            ["research work", 2, True],
            ["pants", 2, False],
            ["skirts", 1, False],
            ["the colour black", 2, False],
            ["the colour blue", 2, False],
            ["the colour pink", -2, False]],
        forced_sexy_opinions = [
            ["taking control", 2, False],
            ["being submissive", -1, False],
            ["bareback sex", -2, False],
            ["creampies", -2, False],
            ["giving blowjobs", 1, False],
            ["swallowing cum", 2, False],
            ["lingerie", 1, False]],
        serum_tolerance = 3, work_experience = 4, type="story")

    nora.generate_home()
    nora.home.add_person(nora)
    nora.idle_pose = "stand3"
    #Add Job and Set override schedule so Nora doesn't become available until appropriate time
    nora.set_opinion("research work", 2, True) #Always loves research work
    nora.on_birth_control = False   #Story purposes
    nora.max_arousal = 75           #Orgasms easily
    nora.set_event_day("day_met")   #We meet her in the prologue now
    nora.set_event_day("obedience_event")
    nora.set_event_day("love_event")
    nora.set_event_day("slut_event")
    nora.set_event_day("story_event")

    town_relationships.update_relationship(nora, stephanie, "Friend")
    nora.set_schedule(university, day_slots = [0, 1, 2, 3, 4], time_slots =[1, 2, 3])
    # nora.set_schedule(university, day_slots = [5], time_slots =[1, 2])
    nora.set_schedule(downtown_bar, day_slots = [5], time_slots =[4])
    mc.phone.register_number(nora)

    add_nora_research_intro_action(nora, False)
    add_nora_bar_meetup_initial_meeting_action()
    # Re-intro her if you don't take the option to visit her. Provides access to her special traits eventually.

##############
# Story Info #
##############

def nora_story_character_description():
    return "Your former lab instructor, [nora.fname] is now following closely your business progress while helping pull strings for you at the university."

def nora_story_love_list():
    love_story_list = {}
    love_story_list = nora.story_tracker.get_path_progress(nora, "Unstable Serums")

    return love_story_list

def nora_story_love_is_complete():
    return True

# def nora_story_lust_list():
#     lust_story_list = {}
#     lust_story_list[0] = "This story step has not yet been written."
#     return lust_story_list

def nora_story_obedience_list():
    obedience_story_list = {}
    obedience_story_list = nora.story_tracker.get_path_progress(nora, "University Contracts")

    return obedience_story_list

def nora_story_obedience_is_complete():
    return nora.progress.obedience_step > 2

def nora_story_story_lust_list():
    lust_story_list = {}
    lust_story_list[0] = "This branch is under construction."

    return lust_story_list

def nora_story_lust_is_complete():
    return nora.progress.lust_step > 2

def nora_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (stephanie, "[stephanie.fname] and [nora.fname]. Could you get your old lab mates together again?"),
    }
    return teamups

def nora_story_other_list():
    other_story_list = {}

    other_story_list[0] = "Meet with [nora.fname] at the bar on Saturday nights."

    return other_story_list

####################
# Position Filters #
####################

def nora_foreplay_position_filter(foreplay_position: Position):
    return True

def nora_oral_position_filter(oral_positions: Position):
    # for now unlock after completing paid research
    return True
    return len(list_of_nora_traits) == 0

def nora_vaginal_position_filter(vaginal_position: Position):
    # for now unlock after few blowjobs with swallow
    return True
    return nora.cum_mouth_count > 3

def nora_anal_position_filter(anal_position: Position):
    # for now unlock after few creampies
    return True
    return nora.vaginal_creampie_count > 3

def nora_oral_position_info():
    return "Complete the paid research event chain"

def nora_vaginal_position_info():
    count = 4 - nora.cum_mouth_count
    return f"Cum in her mouth {count} more times"

def nora_anal_position_info():
    count = 4 - nora.vaginal_creampie_count
    return f"Give her {count} more creampies"

####################
#  Nora Contracts  #
####################
def nora_obedience_serum_count_up():
    nora.event_triggers_dict["contract_count"] = nora.event_triggers_dict.get("contract_count", 0) + 1

def nora_obedience_stage_2_serum_req(serum: SerumDesign):
    return serum.has_hidden_tag("Suggest") and serum.has_hidden_tag("Obedience")

def get_nora_contract() -> Contract:
    if not nora.event_triggers_dict.get("nora_contracts_intro_complete", False):
        return None

    if nora.story_tracker.path_step("University Contracts") == 0:
        return Contract("University Research Program",
            "The local university has contracted out some of your serums for research purposes.", 5,
            mental_requirement = 4, physical_requirement = 0,
            sexual_requirement = 3, medical_requirement = 1,
            flaw_tolerance = 0, attention_tolerance = 2, amount_desired = 10,
            other_payout = nora_obedience_serum_count_up)

    return Contract("University Research Program",
        "The local university has contracted out for a more advanced obediene serum\nMust have an obedience and a suggestibility trait included.", 5,
        mental_requirement = 11, physical_requirement = 0,
        sexual_requirement = 6, medical_requirement = 3,
        flaw_tolerance = 0, attention_tolerance = 2,
        amount_desired = 20,
        other_requirement = nora_obedience_stage_2_serum_req,
        other_payout = nora_obedience_serum_count_up)
