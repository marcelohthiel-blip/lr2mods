from __future__ import annotations
import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import short_hair
from game.game_roles._role_definitions_ren import critical_job_role
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.people.Alexia.alexia_role_definition_ren import alexia_role, init_alexia_roles
from game.major_game_classes.game_logic.Room_ren import coffee_shop, downtown
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, alexia, myra, kaya, camila
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.clothing_related.Outfit_ren import Outfit, big_glasses
from game.major_game_classes.clothing_related.Wardrobe_ren import barista_uniforms
from game.major_game_classes.game_logic.Action_ren import Action
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_alexia_character")

def alexia_intro_phase_zero_requirement(day_trigger):
    return day >= day_trigger

def alexia_intro_phase_one_requirement(person: Person):
    return alexia in downtown.people

def alexia_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    valid_titles.append("Alex")
    return valid_titles

def alexia_possessive_titles(person: Person):
    valid_titles = []
    valid_titles.append("your old classmate")
    return valid_titles

def alexia_player_titles(person: Person):
    valid_titles = [mc.name]
    if person.love > 10:
        valid_titles.append("Teacher's pet")
    return valid_titles

def create_alexia_character():
    ### ALEXIA ###
    alexia_wardrobe = wardrobe_from_xml("Alexia_Wardrobe")

    alexia_base = Outfit("Alexia's accessories")
    alexia_glasses = big_glasses.get_copy()
    big_glasses.colour = [0.1, 0.1, 0.1, 1.0]
    alexia_base.add_accessory(alexia_glasses)

    init_alexia_roles()

    alexia_personality = Personality("alexia", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["sports", "pop music"],
        common_sexy_likes = ["doggy style sex", "bareback sex", "not wearing anything", "skimpy outfits"],
        common_dislikes = ["conservative outfits", "hiking", "the colour brown", "the colour orange"],
        common_sexy_dislikes = ["anal sex", "being fingered", "taking control"],
        titles_function = alexia_titles, possessive_titles_function = alexia_possessive_titles, player_titles_function = alexia_player_titles,
        insta_chance = 40, dikdok_chance = 20)

    global alexia
    alexia = make_person(name = "Alexia", age_range = [21, 23], body_type = "thin_body", face_style = "Face_2", tits = "C", height = 0.93, hair_colour = ["golden blonde", [0.898, 0.784, 0.659, 0.95]], hair_style = short_hair, skin = "white",
        eyes = "brown", personality = alexia_personality, name_color = "#ffff6e", dial_color = "#ffff6e", starting_wardrobe = alexia_wardrobe,
        stat_array = [5, 3, 3], skill_array = [1, 6, 2, 1, 1], sex_skill_array = [2, 2, 1, 0], sluttiness = 3, obedience = 100, happiness = 102, love = 3,
        title = "Alexia", possessive_title = "your old classmate", mc_title = mc.name, relationship = "Girlfriend", SO_name = Person.get_random_male_name(), kids = 0, base_outfit = alexia_base,
        forced_opinions = [
            ["marketing work", 2, False],
            ["flirting", 1, False],
            ["pants", -1, False],
            ["the colour yellow", 2, False],
            ["the colour black", 1, False],
            ["the colour green", -2, False]],
        forced_sexy_opinions = [
            ["kissing", 1, False],
            ["cheating on men", -2, False]],
        work_experience = 2, type="story")

    alexia.generate_home()
    alexia.home.add_person(alexia)
    alexia.add_role(alexia_role)

    alexia_barista_job = JobDefinition("Barista", critical_job_role, job_location = coffee_shop, day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2], wardrobe = barista_uniforms)
    alexia.change_job(alexia_barista_job, job_known = False)

    alexia.set_override_schedule(alexia.home) #Hide them in their bedroom off the map until they're ready / #Stay at hom until we clear this.

    mc.business.add_mandatory_crisis(
        Action("Alexia Set Schedule", alexia_intro_phase_zero_requirement, "alexia_phase_zero_label", requirement_args = renpy.random.randint(14, 21))
    )
    alexia.add_unique_on_room_enter_event(
        Action("Alexia Intro Phase One", alexia_intro_phase_one_requirement, "alexia_intro_phase_one_label", priority = 50)
    )

##############
# Story Info #
##############

def alexia_story_character_description():
    return "After no contact for over a year, you have a chance encounter with [alexia.fname], a former schoolmate from your time at the university."

def alexia_story_love_list():
    love_story_list = {}

    if alexia.progress.love_step == 0:
        love_story_list[0] = "Increase [alexia.fname]'s love to 10, then hire her to your marketing department."
    elif alexia.progress.love_step == 1:
        love_story_list[0] = "You've hired [alexia.fname] to be in your marketing department."

    if not myra.event_triggers_dict.get("gaming_cafe_open", False):
        love_story_list[1] = "[alexia.fname] seems interested in gaming. Wait for the gaming café to open up at the mall."
    else:
        love_story_list[1] = "[alexia.fname] can be found regularly at the gaming cafe, playing with her friend [myra.fname]."

    love_story_list[2] = "This story step has not yet been written."

    return love_story_list

def alexia_story_love_is_complete():
    return alexia.progress.love_step >= 2 and myra.event_triggers_dict.get("gaming_cafe_open", False)

def alexia_story_lust_list():
    lust_story_list = {}
    if alexia.progress.love_step == 0:
        lust_story_list[0] = "Hire [alexia.fname] to start this story."
        return lust_story_list

    if mc.business.event_triggers_dict.get("has_expensive_camera", False):
        lust_story_list[0] = "You can talk to [alexia.fname] to do a photoshoot for company advertising."
        lust_story_list[1] = "This story step has not yet been written."
    elif alexia.event_triggers_dict.get("camera_reintro_enabled", False):
        lust_story_list[0] = "Talk to [alexia.fname] to purchase the camera equipment."
    else:
        lust_story_list[0] = (
            "Wait for [alexia.fname] to talk to you about camera equipment, then purchase it."
        )

    return lust_story_list

def alexia_story_lust_is_complete():
    return alexia.progress.love_step != 0 and mc.business.event_triggers_dict.get("has_expensive_camera", False)

# def alexia_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

def alexia_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (myra, "[myra.fname] and [alexia.fname], a match made in gamer heaven?"),
        1: (camila, "[camila.fname] also has a significant other, maybe you could get them together?"),
        2: (kaya, "You wonder if [alexia.fname] and [kaya.fname] would be up for grabbing coffee together sometime.")    #this should have conditions on it
    }
    return teamups

def alexia_story_other_list():
    other_story_list = {}
    # Alexia's other story index:
    # 0 - Her current employment status
    # 1 - Her current girlfriend status
    # 2 - Is she the company model, if so, how far have photo shoots gone?
    if alexia.is_employee:
        other_story_list[0] = "You have hired [alexia.fname] to work for you."
    else:
        other_story_list[0] = "[alexia.fname] does not work for you."
    if alexia.has_significant_other:
        if alexia.is_affair:
            other_story_list[1] = "You are having an affair with her, although she is currently dating someone else!"
        else:
            other_story_list[1] = "She is currently dating someone else."
    elif alexia.is_girlfriend:
        other_story_list[1] = "She is your girlfriend."
    elif alexia.is_single:
        other_story_list[1] = "She is currently single."
    if alexia == mc.business.company_model:
        if alexia.event_triggers_dict.get("camera_fuck", False):
            other_story_list[2] = "[alexia.fname] is your company model, and even lets you fuck her for ad campaigns!"
        elif alexia.event_triggers_dict.get("camera_suck", False):
            other_story_list[2] = "[alexia.fname] is your company model, and even sucks your cock for ad campaigns."
        elif alexia.event_triggers_dict.get("camera_touch", False):
            other_story_list[2] = "[alexia.fname] is your company model and lets you touch her for ad campaigns."
        elif alexia.event_triggers_dict.get("camera_naked", False):
            other_story_list[2] = "[alexia.fname] is your company model and is willing to get naked for photo shoots."
        elif alexia.event_triggers_dict.get("camera_flash", False):
            other_story_list[2] = "[alexia.fname] is your company model and is willing to flash to camera for photo shoots."
        elif alexia.event_triggers_dict.get("camera_flirt", False):
            other_story_list[2] = "[alexia.fname] is your company model and flirts like a pro for photo shoots."
        else:
            other_story_list[2] = "[alexia.fname] is your company model, but the photo shoots are a bit boring."

    return other_story_list
