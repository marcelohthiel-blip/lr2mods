from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.text_tags.southern_modifier_ren import southern_belle
from game.clothing_lists_ren import heavy_eye_shadow, big_glasses, lipstick, gold_chain_necklace, copper_bracelet, bobbed_hair
from game.game_roles._role_definitions_ren import critical_job_role
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, ellie
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.serum_related.serums.fetish_serums_ren import fetish_serum_unlock_count, get_fetish_basic_serum
from game.personality_types._personality_definitions_ren import introvert_personality
from game.sex_positions._position_definitions_ren import tit_fuck, standing_finger, standing_grope, drysex_cowgirl, standing_dildo, handjob, cowgirl_handjob
from game.people.Ellie.ellie_role_definition_ren import ellie_role, init_ellie_roles
from game.people.Ellie.IT_Nanobot_Projects_ren import nanobot_IT_project_list


day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_ellie_character")

def ellie_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)

    return valid_titles

def ellie_possessive_titles(person: Person):
    valid_possessive_titles = [person.name]
    if person.sluttiness > 30:
        valid_possessive_titles.append("your jezebel")
    if person.sluttiness > 60:
        valid_possessive_titles.append("your pious slut")
    return valid_possessive_titles

def ellie_player_titles(person: Person):
    return [mc.name]

def ellie_start_intro_note_requirement():
    if time_of_day != 2 or day % 7 != 2:
        return False
    return fetish_serum_unlock_count() >= 1 and get_fetish_basic_serum().mastery_level > 3.0 and mc.business.head_researcher

def create_ellie_character():
    ellie_wardrobe = wardrobe_from_xml("Ellie_Wardrobe")

    ellie_base_outfit = Outfit("ellie's base accessories")
    ellie_base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.71, .4, .85, 0.5])
    ellie_base_outfit.add_accessory(big_glasses.get_copy(), [.15, .15, .15, 0.95])
    ellie_base_outfit.add_accessory(lipstick.get_copy(), [.37, .02, .05, 0.75])
    ellie_base_outfit.add_accessory(gold_chain_necklace.get_copy(), [.95, .95, .78, 0.95])
    ellie_base_outfit.add_accessory(copper_bracelet.get_copy(), [.95, .95, .78, 0.95])

    init_ellie_roles()

    # init ellie job (make her hidden on start)
    ellie_job = JobDefinition("IT Specialist", [ellie_role, critical_job_role], None, time_slots = [1, 2, 3], wage_adjustment = 1.1)

    ellie_personality = Personality("ellie", default_prefix = introvert_personality.default_prefix,
        common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
        common_dislikes = ["pants", "working", "the colour yellow", "conservative outfits", "sports"],
        common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything", "polyamory"],
        titles_function = ellie_titles, possessive_titles_function = ellie_possessive_titles, player_titles_function = ellie_player_titles)

    global ellie
    ellie = make_person(name = "Ellie", last_name = "Sullivan", age = 24, body_type = "thin_body", face_style = "Face_13", tits="DDD", height = 0.92, hair_colour = ["dark auburn", [0.367, 0.031, 0.031, 0.95]], hair_style = bobbed_hair, skin="white",
        eyes = "light blue", personality = ellie_personality, name_color = "#FFA07A", starting_wardrobe = ellie_wardrobe, job = ellie_job,
        stat_array = [1, 4, 5], skill_array = [1, 1, 5, 3, 1], sex_skill_array = [1, 1, 0, 0], sluttiness = 0, obedience_range = [90, 100], happiness = 103, love = -3, suggestibility = 6,
        relationship = "Single", kids = 0, base_outfit = ellie_base_outfit,
        forced_opinions = [
            ["research work", 2, True],
            ["work uniforms", 1, False],
            ["flirting", 1, False],
            ["working", 1, False],
            ["the colour green", 2, False],
            ["pants", 1, False],
            ["cooking", 2, False]],
        serum_tolerance = 0, work_experience = 2, type = 'story')

    ellie.idle_pose = "stand2"
    ellie.generate_home()
    ellie.home.add_person(ellie)
    ellie.set_override_schedule(ellie.home)

    # ellie_mod_initialization():
    # ellie.event_triggers_dict["intro_complete"] = False    # True after first talk
    # ellie.event_triggers_dict["blackmail_stage"] = 0
    # ellie.event_triggers_dict["squirts"] = False
    # ellie.event_triggers_dict["been_fingered"] = False
    # ellie.event_triggers_dict["given_handjob"] = False
    # ellie.event_triggers_dict["given_blowjob"] = False
    # ellie.event_triggers_dict["given_virginity"] = False
    # ellie.event_triggers_dict["given_anal_virginity"] = False
    # ellie.event_triggers_dict["brought_lunch"] = False
    # ellie.event_triggers_dict["dinner_date"] = False
    # ellie.event_triggers_dict["work_turnon"] = False
    # ellie.event_triggers_dict["tit_fuck"] = False
    # ellie.event_triggers_dict["has_submit"] = False
    # ellie.event_triggers_dict["fetish_avail"] = False

    mc.business.add_mandatory_crisis(
        Action("Blackmail Note", ellie_start_intro_note_requirement, "ellie_start_intro_note_label")
    ) #Add the event here so that it pops when the requirements are met.

    #We usually set progress screen info here, but we wait until appropriate in the story to do it, since Ellie is initially a ?????

    # set relationships
    # Ellie is relatively new in town and has no mutual relationship with MC
    ellie.text_modifiers.append(southern_belle)

##############
# Story Info #
##############

def ellie_story_character_description():
    return "Fired from her previous job and desperate for work, you hired [ellie.fname] to be your IT lead."

def ellie_story_love_list():
    love_story_list = {}
    if not ellie_has_been_fingered():
        love_story_list[0] = "Advance her sluttiness story to continue this story."
        return love_story_list
    if not ellie_has_given_handjob():
        if ellie.love < 20:
            love_story_list[0] = "Increase [ellie.fname]'s love to continue this story."
        else:
            love_story_list[0] = "[ellie.fname] may surprise you at work soon."
        return love_story_list
    else:
        love_story_list[0] = "[ellie.fname] returned the sexual favour with her first handjob!"

    if not ellie_has_brought_lunch_date():
        if ellie.love < 40:
            love_story_list[1] = "Increase [ellie.fname]'s love to continue this story."
        else:
            love_story_list[1] = "Work in the morning and [ellie.fname] may surprise you with a meal."
        return love_story_list
    else:
        love_story_list[1] = "[ellie.fname] surprised you at work with a delicious home cooked meal."
        if ellie_has_given_blowjob():
            love_story_list[2] = "You made her cum while eating her out in your office."

    love_story_list[3] = "There is nothing more in this story line at this time."
    return love_story_list

def ellie_story_love_is_complete():
    return ellie_has_brought_lunch_date()

def ellie_story_lust_list():
    lust_story_list = {}
    if not ellie_has_been_fingered():
        if ellie.sluttiness < 20:
            lust_story_list[0] = "Trying increasing her sluttiness to continue this story."
        else:
            lust_story_list[0] = "Try working while she is working on a nanobot program to continue this story."
        return lust_story_list
    else:
        lust_story_list[0] = "Gave [ellie.fname] her first orgasm with your fingers in her office!"

    if not ellie_has_given_handjob():   #Requires love story progress
        lust_story_list[1] = "Try progressing [ellie.fname]'s love story to continue this story."
        return lust_story_list
    elif not ellie_has_given_blowjob(): #40 sluttiness event
        if ellie.sluttiness < 40:
            lust_story_list[1] = "Trying increasing her sluttiness to continue this story."
        elif not any(x for x in mc.business.employee_list if x != ellie and x.sluttiness > 50):
            lust_story_list[1] = "[ellie.fname] doesn't know anyone she can confide her desires in. Raise another employee's sluttiness to at least 50."
        else:
            lust_story_list[1] = "You may overhear a conversation [ellie.fname] is having at work soon..."
        return lust_story_list
    else:
        lust_story_list[1] = "[ellie.fname] gave you her first blowjob after you overheard her asking a coworker about oral sex!"

    lust_story_list[2] = "There is nothing more in this story line at this time."

    return lust_story_list

def ellie_story_lust_is_complete():
    return ellie_has_given_blowjob()

# def ellie_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

# def ellie_story_teamup_list() -> dict[int, tuple[Person, str]]:
#     return {}

def ellie_story_other_list():
    other_info_list = {}
    if ellie.is_employee and ellie.primary_job.days_employed > 0:
        other_info_list[0] = "[ellie.fname] is thankful you hired her, despite blackmailing you."
    if ellie_is_a_squirter():
        other_info_list[1] = "[ellie.fname] has extremely wet orgasms!"
    # other_info_list.append("[ellie.fname] is not yet willing to go all the way with you. Try advancing her story.")
    return other_info_list

####################
# Position Filters #
####################

def ellie_foreplay_position_filter(foreplay_position: Position):
    filter_out = []
    if not ellie_has_tit_fuck():
        filter_out.append(tit_fuck)
    if not ellie_has_been_fingered():
        filter_out.extend((standing_finger, standing_grope, drysex_cowgirl, standing_dildo))
    if not ellie_has_given_handjob():
        filter_out.extend((handjob, cowgirl_handjob))

    return foreplay_position not in filter_out

def ellie_oral_position_filter(oral_position: Position):
    return ellie_has_given_blowjob()

def ellie_vaginal_position_filter(vaginal_position: Position):
    return ellie_has_given_virginity()

def ellie_anal_position_filter(anal_position: Position):
    return ellie_has_given_anal_virginity()

def ellie_oral_position_info():
    return "Story progression will unlock oral"

def ellie_vaginal_position_info():
    return "Story progression will unlock vaginal"

def ellie_anal_position_info():
    return "Unlock is not yet written"
    # return "Story progression will unlock anal"

def ellie_is_working_on_nanobots(): #This should probably always return true now since she is in R&D
    if ellie.is_at(mc.business.r_div) and mc.business.current_IT_project is not None:
        return mc.business.current_IT_project in nanobot_IT_project_list

def ellie_is_working_on_project():
    return ellie.is_at(mc.business.r_div) and mc.business.current_IT_project is not None

def ellie_is_a_squirter():
    return ellie.event_triggers_dict.get("squirts", False)

def ellie_has_been_fingered():
    return ellie.event_triggers_dict.get("been_fingered", False)

def ellie_has_given_handjob():
    return ellie.event_triggers_dict.get("given_handjob", False)

def ellie_has_given_blowjob():
    return ellie.event_triggers_dict.get("given_blowjob", False)

def ellie_has_given_virginity():
    return ellie.event_triggers_dict.get("given_virginity", False)

def ellie_has_given_anal_virginity():
    return ellie.event_triggers_dict.get("given_anal_virginity", False)

def ellie_has_tit_fuck():
    return ellie.event_triggers_dict.get("tit_fuck", False)

def ellie_has_brought_lunch_date():
    return ellie.event_triggers_dict.get("brought_lunch", False)

def ellie_has_cooked_dinner_date():
    return ellie.event_triggers_dict.get("dinner_date", False)

def ellie_work_crisis_unlocked():
    return ellie.event_triggers_dict.get("work_turnon", False)
