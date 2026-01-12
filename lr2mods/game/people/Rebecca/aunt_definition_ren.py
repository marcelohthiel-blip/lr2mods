from __future__ import annotations
import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import bobbed_hair
from game.game_roles._role_definitions_ren import critical_job_role, aunt_role
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Room_ren import aunt_bedroom, aunt_apartment
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, list_of_instantiation_functions, mom, lily, starbuck, aunt
from game.personality_types._personality_definitions_ren import wild_personality
from game.people.Rebecca.aunt_role_definition_ren import init_aunt_roles
from game.people.Teamups.starbuck_rebecca_teamup_definition_ren import starbuck_rebecca_teamup

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_instantiation_functions.append("create_rebecca_character")

def aunt_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    valid_titles.append("Aunt " + person.name)
    if person.love > 20:
        valid_titles.append("Auntie")
        valid_titles.append("Becky")
        valid_titles.append("Becca")
        valid_titles.append("Aunt Becky")
        valid_titles.append("Aunt Becca")
    return valid_titles

def aunt_possessive_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    valid_titles.append("your aunt")

    if person.love > 20:
        valid_titles.append("your loving aunt")

    if person.love > 40 and person.sluttiness > 60:
        valid_titles.append("your personal MILF")
        valid_titles.append("your slutty aunt")

    if person.sluttiness > 90:
        valid_titles.append("your cock hungry aunt")
        valid_titles.append("your cumdump aunt")

    return valid_titles

def aunt_player_titles(person: Person):
    valid_titles = [mc.name]

    if person.love > 20:
        valid_titles.append("Sweetheart")
        valid_titles.append("Sweety")
        valid_titles.append("Nephew")

    if person.sluttiness > 40:
        valid_titles.append("Champ")
        valid_titles.append("Slugger")
    return valid_titles

def aunt_intro_requirement(day_trigger):
    return (
        day >= day_trigger
        and day % 7 != 4
        and time_of_day == 4
        and not mom.is_sleeping
    )

def family_games_night_intro_requirement(person: Person):
    if time_of_day != 3 or person.love < 20 or mom.love < 20:
        return False
    if not person.event_triggers_dict.get("invited_for_drinks", False):
        return False
    return person.is_at(aunt_apartment)

def create_rebecca_character():
    ### AUNT ###
    aunt_wardrobe = wardrobe_from_xml("Aunt_Wardrobe")
    #original height = 0.92

    init_aunt_roles()

    aunt_personality = Personality("aunt", wild_personality.default_prefix,
        common_likes = ["small talk", "makeup", "flirting"],
        common_sexy_likes = ["skimpy outfits"],
        common_dislikes = ["working", "hiking", "conservative outfits", "the colour blue", "the colour green"],
        common_sexy_dislikes = ["public sex", "masturbating", "being fingered", "cheating on men"],
        titles_function = aunt_titles, possessive_titles_function = aunt_possessive_titles, player_titles_function = aunt_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global aunt_unemployed_job
    aunt_unemployed_job = JobDefinition("Unemployed", critical_job_role, day_slots = [], time_slots = [])

    global aunt
    aunt = make_person(name = "Rebecca", last_name = Person.get_random_last_name(), age = 39, body_type = "thin_body", face_style = "Face_1", tits = "DD", height = 0.935, hair_colour = ["dirty blonde", [0.663, 0.549, 0.373, 0.95]], hair_style = bobbed_hair, skin="white",
        eyes = "brown", personality = aunt_personality, name_color = "#66FF8A", dial_color = "#66FF8A", starting_wardrobe = aunt_wardrobe, start_home = aunt_bedroom,
        stat_array = [5, 2, 1], skill_array = [1, 2, 0, 0, 0], sex_skill_array = [3, 5, 3, 2], sluttiness = 11, obedience = 100, happiness = 70, love = 5, job = aunt_unemployed_job,
        title = "Aunt Becky", possessive_title = "your aunt", mc_title = mc.name, relationship = "Single", kids = 1, suggestibility_range = [5, 15],
        forced_opinions = [
            ["pants", 2, True],
            ["high heels", 2, False],
            ["the colour pink", 2, False],
            ["the colour black", 2, False]],
        forced_sexy_opinions = [
            ["lingerie", 2, False],
            ["showing her tits", 2, False],
            ["showing her ass", 2, False],
            ["taking control", 2, False]],
        work_experience = 3, type="story")

    aunt.add_role(aunt_role) #Note that her "Hire" event is actually held by her aunt role, which just checks if she has the aunt_unemployed_job Job. Avoids needing a new Role just for her non-job.
    aunt.set_schedule(aunt_bedroom) #Hide them in their bedroom off the map until they're ready.
    aunt.home.add_person(aunt)

    mc.business.add_mandatory_crisis(
        Action("Aunt introduction", aunt_intro_requirement, "aunt_intro_label", requirement_args = renpy.random.randint(15, 20))
    ) #Aunt and cousin will be visiting tomorrow in the morning

    aunt.add_unique_on_room_enter_event(
        Action("Family games night intro", family_games_night_intro_requirement, "family_games_night_intro", priority = 30)
    )

    town_relationships.update_relationship(mom, aunt, "Sister")
    town_relationships.update_relationship(aunt, lily, "Niece", "Aunt")

##############
# Story Info #
##############

def rebecca_story_character_description():
    return "Your aunt on your mom's side. She is recently divorced, and has a daughter, your cousin [cousin.fname]."

# def rebecca_story_love_list():
#     love_story_list = {}
#     love_story_list[0] = "The next step in this story has not yet been written."

#     return love_story_list

def rebecca_story_lust_list():
    lust_story_list = {}
    if aunt.progress.lust_step == 0:
        if aunt.sluttiness < 20:
            lust_story_list[0] = "Increase [aunt.fname]'s sluttiness to progress this story."
        else:
            lust_story_list[0] = "[aunt.fname] likes to drink with your mother once in a while. Wait until the next time this happens."
        return lust_story_list
    else:
        lust_story_list[0] = "[aunt.fname] let you dry hump her ass after getting drunk one evening."
    if aunt.progress.lust_step == 1:
        if aunt.sluttiness < 40:
            lust_story_list[1] = "Increase [aunt.fname]'s sluttiness to progress this story."
        elif not aunt.has_event_day("moved_out"):
            lust_story_list[1] = "Wait for [aunt.fname] to move into her own apartment."
        else:
            lust_story_list[1] = "Visit [aunt.fname] at her apartment sometime."
        return lust_story_list
    if aunt.progress.lust_step > 1:
        lust_story_list[1] = "[aunt.fname] gave you a blowjob after you accidentally walked in on her in her underwear."
    if aunt.progress.lust_step == 2:
        if aunt.sluttiness < 60:
            lust_story_list[2] = "Increase [aunt.fname]'s sluttiness to progress this story."
        elif aunt.story_event_ready("slut"):
            lust_story_list[2] = "Play cards games with your family on Wednesday nights!"
        else:
            lust_story_list[2] = "[aunt.fname] needs some time before she is ready to advance this story."
        return lust_story_list
    if aunt.progress.lust_step >= 3:
        lust_story_list[2] = "You had sex with [aunt.fname] after a family game night!"
    if aunt.progress.lust_step == 3:
        lust_story_list[3] = "She seemed hesitant to allow it to happen again. Give her a few days then have wine with her at her place."
    else:
        lust_story_list[3] = "She's willing to fuck you anytime now."
    lust_story_list[4] = "The next step in this story has not yet been written."

    return lust_story_list

def rebecca_story_lust_is_complete():
    return aunt.progress.lust_step > 3

def rebecca_story_obedience_list():
    obedience_story_list = {}

    if aunt.progress.obedience_step == 0:
        obedience_story_list[0] = "After [aunt.fname] has moved into her own place, check up on her in the evenings to start this arc."
        return obedience_story_list
    if aunt.progress.obedience_step == 1:
        obedience_story_list[0] = "[aunt.fname] has started working on a CPA renewal. Give her some time to finish it and she will contact you."
        return obedience_story_list
    if aunt.progress.obedience_step >= 2:
        obedience_story_list[0] = "[aunt.fname] has finished her CPA renewal and is looking for work!"
        if aunt.progress.obedience_step == 2:
            if aunt.obedience < 120:
                obedience_story_list[1] = "Raise her obedience to advance this story."
            elif aunt.story_event_ready("obedience"):
                obedience_story_list[1] = "Check on her in the evenings to advance this story."
            else:
                obedience_story_list[1] = "She needs time to search for a new job before advancing this story."
            return obedience_story_list
    if aunt.progress.obedience_step == 3:
        obedience_story_list[1] = "She has agreed to audit your finances on a trial basis."
    if aunt.progress.obedience_step >= 4:
        obedience_story_list[1] = "You have hired [aunt.fname] to be your financial consultant. She comes to your company every Tuesday"
        obedience_story_list[2] = "The next step in this story has not yet been written."
    return obedience_story_list

def rebecca_story_obedience_is_complete():
    return aunt.progress.obedience_step >= 4

def rebecca_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {}
    if starbuck_rebecca_teamup.get_stage() == -1:
        teamups[0] = (starbuck, "Try advancing obedience stories for [aunt.fname] and [starbuck.fname]...")
    else:
        teamups[0] = (starbuck, "[aunt.fname] and [starbuck.fname] meet at the sex shop every Friday morning.")

    return teamups

    # if sakari.has_story:
    #     teamup_story_list[1] = (sakari, "[sakari.fname] and seemed to take a liking to your aunt when you took her shopping.")

    # if cousin.has_story:
    #     teamup_story_list[2] = (cousin, "Maybe someday you could get [aunt.fname] together with [cousin.fname], but right now that seems impossible.")

    # return teamup_story_list

def rebecca_story_other_list():
    story_other_list = {}

    # Rebecca's other stories
    # 0 - How far she takes wine night with MC
    # 1 - How far she goes with family card night
    # 2 - Her status with her Ex

    if not aunt.has_event_day("moved_out"):
        story_other_list[0] = "[aunt.fname] is still living with your family."
    elif not aunt.event_triggers_dict.get("invited_for_drinks", False):
        story_other_list[0] = "Visit [aunt.fname] in her new apartment."
    else:
        story_other_list[0] = "Have some drinks with [aunt.fname] in the evenings at her apartment."

    if mc.business.event_triggers_dict.get("family_games_strip", 0) > 0:
        story_other_list[1] = "[aunt.fname] and the rest of your family are willing to play strip euchre on Wednesday nights."
    elif mc.business.event_triggers_dict.get("family_games_cards", 0) > 0:
        story_other_list[1] = "You have a family game night on Wednesday nights."
    else:
        story_other_list[1] = "Progress things with [aunt.fname] to begin having family game nights."

    story_other_list[2] = "[aunt.fname] went through a messy divorce after discovering her ex husband was cheating on her."

    return story_other_list

####################
# Position Filters #
####################

def rebecca_vaginal_position_filter(vaginal_position: Position):
    return aunt.sluttiness > 80 - (aunt.opinion.incest * 5) - (aunt.opinion.vaginal_sex * 5) or aunt.progress.lust_step > 3

def rebecca_anal_position_filter(anal_positions: Position):
    return aunt.sluttiness > 60 - (aunt.opinion.incest * 5) - (aunt.opinion.anal_sex * 5) or aunt.progress.lust_step > 3

def rebecca_vaginal_position_info():
    return "Not slutty enough / vaginal and incest opinion too low"

def rebecca_anal_position_info():
    return "Not slutty enough / anal and incest opinion too low"
