from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import messy_short_hair
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Room_ren import cousin_bedroom
from game.major_game_classes.character_related._job_definitions_ren import unemployed_job
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, town_relationships, mc, aunt, mom, lily, cousin
from game.personality_types._personality_definitions_ren import introvert_personality
from game.people.Gabrielle.cousin_role_definition_ren import cousin_role, init_cousin_roles

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

list_of_instantiation_functions.append("create_gabrielle_character")

def cousin_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(person.name)
    if person.love > 20:
        valid_titles.append("Cuz")

    if person.love < -30:
        valid_titles.append("Hellspawn")
    return valid_titles

def cousin_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(person.name)
    valid_titles.append("your cousin")
    if person.love > 20:
        valid_titles.append("your cuz")

    if person.love < -30:
        valid_titles.append("your bitchy cousin")

    if person.love < -50 and person.sluttiness > 50:
        valid_titles.append("your hell-whore")

    if person.sluttiness > 40:
        valid_titles.append("your cock-goth cousin")

    return valid_titles

def cousin_player_titles(person: Person) -> list[str]:
    valid_titles = [mc.name]
    if person.love < -20:
        valid_titles.append("Asshat")
        valid_titles.append("Dickwad")
        valid_titles.append("Dick-for-brains")

    if person.love > 20:
        valid_titles.append("Cuz")
        valid_titles.append("Cousin")

    if person.love < 0 and person.sluttiness > 40:
        valid_titles.append("Meathead")

        if person.obedience < 20:
            valid_titles.append("Cock slave")
            valid_titles.append("Slave")
    return valid_titles


def create_gabrielle_character():
    ### COUSIN ###
    cousin_wardrobe = wardrobe_from_xml("Cousin_Wardrobe")

    init_cousin_roles()

    cousin_personality = Personality("cousin", default_prefix = introvert_personality.default_prefix,
        common_likes = ["the colour black", "heavy metal music", "punk music", "makeup", "the colour purple", "high heels"],
        common_sexy_likes = ["lingerie", "masturbating", "taking control", "getting head", "skimpy outfits", "showing her tits", "showing her ass"],
        common_dislikes = ["small talk", "flirting", "working", "conservative outfits"],
        common_sexy_dislikes = ["kissing", "giving blowjobs", "bareback sex"],
        titles_function = cousin_titles, possessive_titles_function = cousin_possessive_titles, player_titles_function = cousin_player_titles,
        insta_chance = 30, dikdok_chance = 15)

    global cousin
    cousin = make_person(name = "Gabrielle", last_name = aunt.last_name, age = 18, body_type = "curvy_body", face_style = "Face_3", tits = "DDD", height = 0.98, hair_colour = ["off black", [0.173, 0.133, 0.169, 0.95]], hair_style = messy_short_hair, skin="white",
        eyes = "brown", personality = cousin_personality, name_color = "#9c4dea", dial_color = "#9c4dea", starting_wardrobe = cousin_wardrobe, start_home = cousin_bedroom,
        stat_array = [0, 4, 2], skill_array = [0, 0, 2, 1, 0], sex_skill_array = [3, 0, 0, 0], sluttiness = 8, obedience = 70, happiness = 70, love = -20, job = unemployed_job,
        title = "Gabrielle", possessive_title = "your cousin", mc_title = mc.name, relationship = "Single", kids = 0,
        forced_opinions = [
            ["the colour black", 2, True]],
        forced_sexy_opinions = [
            ["kissing", 1, False],
            ["being fingered", 2, False]],
        serum_tolerance = 2, work_experience = 1, type="story")

    cousin.add_role(cousin_role)
    cousin.set_schedule(cousin_bedroom) #Hide them in their bedroom off the map until they're ready
    cousin.home.add_person(cousin)

    town_relationships.update_relationship(mom, cousin, "Niece", "Aunt")
    town_relationships.update_relationship(aunt, cousin, "Daughter", "Mother")
    town_relationships.update_relationship(lily, cousin, "Cousin")

def gabrielle_story_character_description():
    return "Your cousin and [aunt.fname]'s daughter. She is quite obnoxious and doesn't like being around people."

def gabrielle_story_other_list():
    story_other_list = {}

    if not cousin.has_event_day("moved_out"):
        story_other_list[0] = "[cousin.fname] is still living with your family."
        return story_other_list
    else:
        story_other_list[0] = "[cousin.fname] has moved of your house."

    if cousin.has_queued_event('cousin_house_phase_two_label'):
        story_other_list[1] = "Seems she's hanging around your house in the afternoon."
        return story_other_list

    if cousin.event_triggers_dict.get("blackmail_level", 0) == 0:
        story_other_list[1] = "What's [cousin.fname] up to in your house? You should find out."
        return story_other_list

    if cousin.event_triggers_dict.get("blackmail_level", 0) == 1:
        story_other_list[1] = "You have blackmailed [cousin.fname] and can keep on doing so."
        return story_other_list
    else:
        story_other_list[1] = "You can not blackmail [cousin.fname]."

    if not cousin.event_triggers_dict.get("seen_cousin_stripping", False):
        story_other_list[2] = "Try to find out what [cousin.fname] does at night."
        return story_other_list

    story_other_list[2] = "You have seen [cousin.fname] stripping at the local strip club."

    if cousin.has_queued_event("cousin_boobjob_ask_label"):
        story_other_list[3] = "[cousin.fname] will ask you for your help soon."
        return story_other_list
    elif cousin.event_triggers_dict.get("getting boobjob", False):
        story_other_list[3] = "You have helped [cousin.fname] with her boobjob."
    elif cousin.event_triggers_dict.get("serum_boobjob", False):
        story_other_list[3] = "You have given [cousin.fname] a serum to increase her cup size."
    else:
        story_other_list[3] = "You can help [cousin.fname] getting larger boobs."

    return story_other_list


####################
# Position Filters #
####################

def gabrielle_vaginal_position_filter(vaginal_position: Position):
    return cousin.sluttiness > 80 - (cousin.opinion.incest * 5) - (cousin.opinion.vaginal_sex * 5)

def gabrielle_anal_position_filter(anal_position: Position):
    return cousin.sluttiness > 60 - (cousin.opinion.incest * 5) - (cousin.opinion.anal_sex * 5)

def gabrielle_vaginal_position_info():
    return "Not slutty enough / vaginal and incest opinion too low"

def gabrielle_anal_position_info():
    return "Not slutty enough / anal and incest opinion too low"
