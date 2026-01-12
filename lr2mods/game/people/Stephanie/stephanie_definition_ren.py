from __future__ import annotations
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.helper_functions.random_generation_functions_ren import make_person
from game.game_roles._role_definitions_ren import critical_job_role
from game.clothing_lists_ren import messy_short_hair
from game.personality_types._personality_definitions_ren import wild_personality
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.Room_ren import university, downtown_bar
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, stephanie, nora, ashley, ellie

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
list_of_instantiation_functions.append("create_stephanie_character")


def stephanie_titles(person: Person):
    valid_titles = [person.name]
    if person.love > 10:
        valid_titles.append("Steph")
    return valid_titles

def stephanie_possessive_titles(person: Person):
    valid_titles = [person.name]
    if person.love > 10:
        valid_titles.append("your study buddy")
    return valid_titles

def stephanie_player_titles(person: Person):
    valid_titles = [mc.name]
    if person.love > 20:
        valid_titles.append("Teacher's pet")
    return valid_titles

def stephanie_tennis_intro_requirement():
    if day % 7 == 5 and time_of_day == 0 and mc.is_at_office:
        return stephanie.love >= 20 and stephanie.story_event_ready("love")
    return False

stephanie_activity_opinions = {}
stephanie_activity_opinions["pong"] = 2  #It's her trademark game
stephanie_activity_opinions["salsa"] = -1
stephanie_activity_opinions["karaoke"] = -1
stephanie_activity_opinions["trivia"] = 1

def stephanie_at_the_bar_intro_requirement(person: Person):
    return False
    return time_of_day == 4 and person.sluttiness > 20 and person.is_at(downtown_bar)


def create_stephanie_character():
    ### STEPHANIE ###
    stephanie_wardrobe = wardrobe_from_xml("Stephanie_Wardrobe")

    lab_assistant_job = JobDefinition("Lab Assistant", critical_job_role, job_location = university) #Job for Steph to technically have at the start of the game so her job title is set correctly.

    stephanie_personality = Personality("stephanie", wild_personality.default_prefix,
        common_likes = ["Fridays", "makeup", "high heels"],
        common_sexy_likes = ["giving blowjobs", "drinking cum", "cheating on men", "missionary style sex", "public sex"],
        common_dislikes = ["Mondays", "dresses", "the colour brown", "the colour purple"],
        common_sexy_dislikes = ["anal sex", "being submissive", "doggy style sex"],
        titles_function = stephanie_titles, possessive_titles_function = stephanie_possessive_titles, player_titles_function = stephanie_player_titles,
        insta_chance = 40, dikdok_chance = 20)

    global stephanie
    stephanie = make_person(name = "Stephanie", age_range = [26, 29], body_type = "standard_body", face_style = "Face_3", tits="C", height = 0.96,
        hair_colour = ["chocolate brown", [0.21, 0.118, 0.039, 0.95]], hair_style = messy_short_hair, skin="white",
        eyes = "brown", personality = stephanie_personality, name_color = "#CD5C5C", dial_color = "#CD5C5C", starting_wardrobe = stephanie_wardrobe,
        stat_array = [3, 6, 5], skill_array = [1, 1, 6, 2, 1], sex_skill_array = [3, 4, 2, 1], sluttiness = 14, obedience = 112, happiness = 119, love = 7,
        title = "Stephanie", possessive_title = "your friend", mc_title = mc.name, relationship = "Single", kids = 0, job = lab_assistant_job,
        forced_opinions = [
            ["research work", 2, True],
            ["small talk", 1, False],
            ["flirting", 1, False],
            ["pants", 2, False],
            ["skirts", -1, False],
            ["the colour black", 2, False],
            ["the colour blue", 2, False],
            ["the colour red", 1, False],
            ["sports", 1, False]],
        forced_sexy_opinions = [
            ["kissing", 1, False],
            ["vaginal sex", 2, False],
            ["creampies", 2, False],
            ["threesomes", 1, False]],
        serum_tolerance = 3, work_experience = 3, type="story")

    stephanie.generate_home().add_person(stephanie)

    #Setup Stephanie's storylines from the beginning, since she is a starting character.
    stephanie.set_schedule(downtown_bar, day_slots = [2, 4, 5], time_slots = [4])
    stephanie.set_event_day("day_met")
    stephanie.set_event_day("obedience_event")
    stephanie.set_event_day("love_event")
    stephanie.set_event_day("slut_event")
    stephanie.set_event_day("story_event")
    stephanie.on_birth_control = True   #For starting events atleast
    mc.phone.register_number(stephanie)
    stephanie_gtk_init()
    mc.business.add_mandatory_crisis(
        Action("Stephanie Still Plays Tennis", stephanie_tennis_intro_requirement, "stephanie_tennis_intro_label")
    )
    mc.business.add_mandatory_crisis(
        Action("Stephanie Like to Drink", stephanie_at_the_bar_intro_requirement, "stephanie_at_the_bar_intro_label", requirement_args = [stephanie])
    )

##############
# Story Info #
##############

def stephanie_story_character_description():
    return "After starting your new pharmaceutical company, you hired your friend [stephanie.fname], to run the research and development division."

def stephanie_story_love_list():
    love_story_list = {}
    if stephanie != mc.business.head_researcher:
        love_story_list[0] = "[stephanie.fname] is no longer your head researcher. You cannot progress this story arc any more."
        return love_story_list

    if stephanie.progress.love_step == 0:
        if stephanie.love < 20:
            love_story_list[0] = "Increase [stephanie.fname]'s love to 20."
        else:
            love_story_list[0] = "Get to work early on Saturday, and you might catch [stephanie.fname] as she comes and goes."
    elif stephanie.progress.love_step >= 1:
        love_story_list[0] = "[stephanie.fname] spends Saturday mornings playing tennis."
        love_story_list[1] = "This story step has not yet been written."

    return love_story_list

def stephanie_story_love_is_complete():
    return stephanie.progress.love_step >= 1

# def stephanie_story_lust_list():
#     lust_story_list = {}
#     lust_story_list[0] = "This story step has not yet been written."
#     return lust_story_list

def stephanie_story_obedience_list():
    obedience_story_list = {}
    if stephanie != mc.business.head_researcher:
        obedience_story_list[0] = "[stephanie.fname] is no longer your head researcher. You cannot progress this story arc any more."
        return obedience_story_list

    if stephanie.progress.obedience_step == 0:
        obedience_story_list[0] = "Advance your business serum trait R&D to tier 1, then [stephanie.fname] will approach you about serum testing."
    elif stephanie.progress.obedience_step == 1:
        obedience_story_list[0] = "[stephanie.fname] has asked you to create a special testing room for serum traits."
    else:
        obedience_story_list[0] = "You have created a room for special serum testing. Talk to [stephanie.fname] to run a test."
    if stephanie.progress.obedience_step == 2:
        if stephanie.obedience < 140:
            obedience_story_list[1] = "Increase her obedience to at least 140 to continue this story."
        else:
            obedience_story_list[1] = "Work in R&D with [stephanie.fname] to continue this story."
    elif stephanie.progress.obedience_step > 2:
        obedience_story_list[1] = "You ordered [stephanie.fname] to give you a special show. You can now command any employee with at least 140 obedience for a lap dance."
        obedience_story_list[2] = "The next story step is not yet written"
    return obedience_story_list

def stephanie_story_obedience_is_complete():
    return stephanie.progress.obedience_step > 2

def stephanie_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (nora, "[nora.fname] and [stephanie.fname]. Could you get your old lab mates together again?"),
        1: (ashley, "Her sister, [ashley.fname], would be awfully fun to get together with, but right now that seems impossible."),
        2: (ellie, "You wonder how [stephanie.fname] and [ellie.fname] enjoy working together.")
    }
    return teamups

def stephanie_story_other_list():
    other_story_list = {}
    #stephanie's other story index:
    # 0 - Her current head researcher status
    # 1 - Her tennis status
    # 2 - Sister storyline status
    if stephanie == mc.business.head_researcher:
        other_story_list[0] = "[stephanie.fname] is your head researcher. Talk to her to advance your business research capabilities."
    else:
        other_story_list[0] = "[stephanie.fname] is no longer your head researcher."
    if stephanie.progress.love_step >= 1:
        other_story_list[1] = "She plays tennis at the gym on Saturday mornings."
    if ashley.is_employee:
        other_story_list[2] = "You hired her sister, [ashley.fname], as a favour to her."

    return other_story_list

####################
# Position Filters #
####################

#None! Fuck Stephanie however you want!

###############
# Get To Know #
###############

def stephanie_gtk_init():
    steph_gtk_list = ActionList([
        Action("Ask about the lab after you left", requirement = stephanie_gtk_past_year_requirement, effect = "stephanie_gtk_past_year_label",
        menu_tooltip = "Find out what was going on at the lab between the time you left and hiring her to be your Head Researcher."),
        Action("Ask about her tennis league", requirement = stephaine_gtk_tennis_requirement, effect = "stephaine_gtk_tennis_label",
        menu_tooltip = "Show interest in her by asking her the details of her tennis league.")
    ])
    stephanie.set_gtk_list(steph_gtk_list)
    return

def stephanie_gtk_past_year_requirement(person = None):
    return stephanie.is_employee

def stephaine_gtk_tennis_requirement(person = None):
    return "Test disabled topic"