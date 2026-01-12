from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.business_policies.organisation_policies_ren import attention_bleed_increase_2_policy
from game.business_policies.special_policies_ren import topless_legal_policy
from game.clothing_lists_ren import ponytail, trimmed_pubes
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import city_hall
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, city_rep
from game.personality_types._personality_definitions_ren import introvert_personality
from game.people.Penelope.penelope_role_definition_ren import get_city_rep_role_actions, get_city_rep_role_trainables

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
list_of_instantiation_functions.append("create_penelope_character")

def penelope_titles(person: Person):
    return f"Ms. {person.last_name}" # lock title

def penelope_possessive_titles(person: Person):
    return "your annoyance" # lock title

def penelope_player_titles(person: Person):
    return f"Mr. {mc.last_name}" # lock title

def create_penelope_character():
    ### ??? ###
    city_rep_wardrobe = wardrobe_from_xml("City_Rep_Wardrobe")
    city_rep_base = city_rep_wardrobe.get_outfit_with_name("City_Rep_Accessories")
    #original height = 0.98
    city_rep_role = Role("City Representative", get_city_rep_role_actions(), role_trainables = get_city_rep_role_trainables(), hidden = True)
    city_rep_job = JobDefinition("City Administrator", city_rep_role, job_location = city_hall, day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3])
    city_rep_job.set_schedule(city_hall, day_slots = [5], time_slots = [1, 2])

    city_rep_personality = Personality("penelope", default_prefix = introvert_personality.default_prefix,
        common_likes = ["skirts", "makeup", "pop music", "work uniforms"],
        common_sexy_likes = ["taking control", "skimpy outfits", "showing her tits", "lingerie"],
        common_dislikes = ["conservative outfits", "the weekend", "pants"],
        common_sexy_dislikes = ["being submissive", "giving blowjobs"],
        titles_function = penelope_titles, possessive_titles_function = penelope_possessive_titles, player_titles_function = penelope_player_titles)

    global city_rep
    city_rep = make_person(name = "Penelope", age = 34, body_type = "thin_body", face_style = "Face_9", tits = "D", height = 1.02, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = ponytail, pubes_style = trimmed_pubes, skin = "white",
        starting_wardrobe = city_rep_wardrobe, base_outfit = city_rep_base, job = city_rep_job, kids = 0, relationship = "Single",
        personality = city_rep_personality, stat_array = [1, 4, 4], skill_array = [5, 0, 0, 0, 2], sex_skill_array = [1, 4, 3, 0],
        sluttiness = 0, obedience = 80, happiness = 100, love = -20,
        forced_opinions = [
            ["small talk", 2, False],
            ["flirting", 2, True],
            ["the colour white", 2, False],
            ["the colour red", 1, False],
            ["working", 2, True]],
        forced_sexy_opinions= [
            ["being fingered", 2, False],
            ["kissing", 1, False]],
        serum_tolerance = 1, work_experience = 4, type="story")

    # since small-talk and flirting are the only options to break open her story
    # line, make sure she is susceptible to that
    # after first meeting, the MC will have only 3 time-slots to interact with her outside her job (saturday evening, sunday afternoon/evening)

    # remove her base outfit (Accessories)
    city_rep.wardrobe.remove_outfit(city_rep_base)

    city_rep.generate_home().add_person(city_rep)
    city_rep.set_schedule(city_rep.home, day_slots = [6], time_slots = [1]) # she's home on sunday mornings
    city_rep.set_override_schedule(city_rep.home)   # initially she won't be visible

    city_rep.set_mc_title(f"Mr. {mc.last_name}")

#########################
# Character Information #
#########################

def penelope_story_character_description():
    return "City Employee that will enforce penalties when you attract too much attention."

def penelope_story_other_list():
    other_info_list = {}
    other_info_list[0] = f"[city_rep.fname] has visited your company {city_rep.event_triggers_dict.get('attention_times_visited', 0)} times."

    if city_rep.love < 15:
        other_info_list[1] = "Offer [city_rep.fname] a coffee when she visit's and try to increase her affection for you."

    if city_rep.event_triggers_dict.get("attention_times_visited", 0) > 0 and city_rep.love < 15:
        other_info_list[2] = "Meet with [city_rep.fname] on Saturday evening or Sundays to further increase her love."

    if city_rep.love > 20 and city_rep.sluttiness > 20:
        if city_rep.event_triggers_dict.get("city_rep_reduced_penalties_trained", False):
            other_info_list[3] = "[city_rep.fname] will reduce all penalties during her visits."
        else:
            other_info_list[3] = "Do a trance training during [city_rep.fname]'s visit to reduced the severity of your penalties."

        if not attention_bleed_increase_2_policy.is_owned:
            other_info_list[4] = "Do a trance training during [city_rep.fname]'s visit to increase the daily attention reduction."
        else:
            other_info_list[4] = "[city_rep.fname] will help you reduce your daily attention gain."

        if city_rep.event_triggers_dict.get('attention_times_visited', 0) > 0:
            if topless_legal_policy.requirement_met:
                other_info_list[5] = "You have unlocked the topless and public nudity policies."
            elif not city_rep.event_triggers_dict.get("discussed_topless_is_legal", False):
                other_info_list[5] = "Do a trance training during [city_rep.fname]'s visit to change her work outfit to something sluttier."
            else:
                other_info_list[5] = "Corrupt [city_rep.fname] and the police chief to unlock the topless and public nudity policies."

    return other_info_list


####################
# Position Filters #
####################

def penelope_foreplay_position_filter(foreplay_position: Position):
    return True

def penelope_oral_position_filter(oral_positions: Position):
    # for now unlock after she visited a few times
    return city_rep.event_triggers_dict.get("attention_times_visited", 0) > 3

def penelope_vaginal_position_filter(vaginal_position: Position):
    # for now unlock after few blowjobs with swallow
    return city_rep.cum_mouth_count > 3

def penelope_anal_position_filter(anal_position: Position):
    # for now unlock after few creampies
    return city_rep.vaginal_creampie_count > 3

def penelope_oral_position_info():
    count = 4 - city_rep.event_triggers_dict.get("attention_times_visited", 0)
    return f"She needs to inspect your business {count} more times"

def penelope_vaginal_position_info():
    count = 4 - city_rep.cum_mouth_count
    return f"Cum in her mouth {count} more times"

def penelope_anal_position_info():
    count = 4 - city_rep.vaginal_creampie_count
    return f"Give her {count} more creampies"
