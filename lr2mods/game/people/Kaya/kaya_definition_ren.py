from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.clothing_lists_ren import heavy_eye_shadow, lipstick, colourful_bracelets, messy_hair
from game.major_game_classes.character_related.Person_ren import Person, mc, town_relationships, list_of_instantiation_functions, kaya, nora, stephanie, erica, sakari
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related._job_definitions_ren import unemployed_job
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Position_ren import Position
from game.personality_types._personality_definitions_ren import wild_personality
from game.people.Kaya.kaya_role_definition_ren import kaya_had_condom_talk

day = 0
time_of_day = 0
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_instantiation_functions.append("create_kaya_character")

def kaya_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)

    return valid_titles

def kaya_possessive_titles(person: Person):
    valid_possessive_titles = [person.title]
    valid_possessive_titles.append("your favourite barista")
    valid_possessive_titles.append("your native barista")
    return valid_possessive_titles

def kaya_player_titles(person: Person):
    return [mc.name]

def create_kaya_character() -> None:
    kaya_base_outfit = Outfit("kaya's base accessories")
    kaya_base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.26, .14, .21, 0.33])
    kaya_base_outfit.add_accessory(lipstick.get_copy(), [1.0, .21, .14, 0.33])
    kaya_base_outfit.add_accessory(colourful_bracelets.get_copy(), [.71, .4, .85, 0.95])

    kaya_personality = Personality("kaya", default_prefix = wild_personality.default_prefix,
        common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
        common_dislikes = ["pants", "working", "the colour yellow", "conservative outfits", "sports"],
        common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything", "polyamory"],
        titles_function = kaya_titles, possessive_titles_function = kaya_possessive_titles, player_titles_function = kaya_player_titles)

    global kaya
    kaya = make_person(
        name="Kaya",
        last_name="Greene",
        age=20,
        body_type="thin_body",
        face_style="Face_3",
        tits="B",
        height=0.94,
        hair_colour=["black", [0.09, 0.07, 0.09, 0.95]],
        hair_style=messy_hair,
        skin="tan",
        eyes="brown",
        personality=kaya_personality,
        name_color="#f0defd",
        job=unemployed_job,
        start_home=sakari.home,
        stat_array=[1, 4, 4],
        skill_array=[1, 1, 3, 5, 1],
        sex_skill_array=[2, 1, 0, 1],
        sluttiness=7,
        obedience_range=[70, 85],
        happiness=88,
        love=0,
        relationship="Single",
        kids=0,
        base_outfit=kaya_base_outfit,
        type="story",
        forced_opinions=[
            ["billiards", 2, False],
            ["work uniforms", -1, False],
            ["flirting", 1, False],
            ["working", 1, False],
            ["the colour green", 2, False],
            ["pants", 1, False],
            ["the colour yellow", 2, False],
            ["the colour red", 1, False],
        ],
        forced_sexy_opinions=[
            ["vaginal sex", 2, False],
            ["bareback sex", 2, False],
            ["drinking cum", -1, False],
            ["giving blowjobs", -1, False],
            ["missionary style sex", 2, False],
            ["creampies", 2, False],
        ],
    )

    kaya.home.add_person(kaya)
    kaya.set_override_schedule(kaya.home)
    kaya.on_birth_control = False   # explicitly disable

    # set relationships
    town_relationships.update_relationship(sakari, kaya, "Daughter", "Mother")


##############
# Story Info #
##############

def kaya_story_character_description() -> str:
    return "[kaya.fname] is a new barista at the local coffeeshop."

def kaya_story_love_list():
    love_story_list = {}
    love_story_list[0] = "This story is a work in progress."
    if kaya.progress.love_step == 0:
        love_story_list[0] = "Get [kaya.fname]'s love to 20, then ask her out on any kind of date."
    if kaya.progress.love_step == 1:
        love_story_list[0] = "Ask [kaya.fname] out for drinks next weekend."
    if kaya.progress.love_step == 2:
        love_story_list[0] = "Talk to [nora.fname] about sponsoring [kaya.fname]. Then talk to her again."
    if kaya.progress.love_step >= 3:
        love_story_list[0] = "[kaya.fname] has started taking classes at the university! She is there every Tuesday and Thursday."
    if kaya.progress.love_step == 3:
        if kaya.story_event_ready("love"):
            love_story_list[1] = "Get her love to 40, then talk to her at the coffee shop on the weekend."
        else:
            love_story_list[1] = "Give her some time to settle in at the university."
    if kaya.progress.love_step == 4:
        love_story_list[1] = "Talk to [nora.fname] again about helping her get a residency."
    if kaya.progress.love_step == 5:
        love_story_list[1] = "[kaya.fname] will start at your business on Monday morning."
    if kaya.progress.love_step == 6:
        love_story_list[1] = "Check in with [kaya.fname] at the end of the day."
    if kaya.progress.love_step >= 7:
        love_story_list[1] = "You recruited [kaya.fname] as an intern. She works for you every Monday, Wednesday, and Friday in Research."
    if kaya.progress.love_step == 7:
        if kaya.story_event_ready("love"):
            love_story_list[2] = "Get her love to 60, then she may ask for your help with something at the end of the workday at your business..."
        else:
            love_story_list[2] = "Give her some time to settle into her intern work."
    if kaya.progress.love_step >= 8:
        love_story_list[2] = "You fucked [kaya.fname] at the office, and she seems interested in getting knocked up..."
        love_story_list[3] = "The rest of this story is in progress."
    return love_story_list

def kaya_story_love_is_complete():
    return kaya.progress.love_step >= 8

def kaya_story_lust_list():
    lust_story_list = {}
    if kaya.progress.lust_step == 0:
        if kaya.progress.love_step < 3:
            lust_story_list[0] = "Progress [kaya.fname]'s love story to unlock this arc."
        else:
            lust_story_list[0] = "Get [kaya.fname]'s sluttiness to 20, then check on her at the university."
    if kaya.progress.lust_step >= 1:
        lust_story_list[0] = "You helped [kaya.fname] get off so she could concentrate on her studies in a university study room."

    if kaya.progress.lust_step == 1:
        if kaya.story_event_ready("slut"):
            lust_story_list[1] = "Get [kaya.fname]'s sluttiness to 40, the she may contact you to hang out on the weekend."
        else:
            lust_story_list[1] = "[kaya.fname] needs some time before she is willing to continue."
    if kaya.progress.lust_step >= 2:
        lust_story_list[1] = "You took [kaya.fname] out for drinks on her 21st birthday, and she gave you a blowjob in the alley."
    if kaya.progress.lust_step == 2:
        if kaya.story_event_ready("slut"):
            lust_story_list[2] = "Get [kaya.fname]'s sluttiness to 60, then she may send you late night text..."
        else:
            lust_story_list[2] = "[kaya.fname] needs some time before she is willing to continue."
    if kaya.progress.lust_step >= 3:
        lust_story_list[2] = "You and [kaya.fname] banged all night after she sent you a booty call."
        lust_story_list[3] = "The rest of this story is in progress."
    return lust_story_list

def kaya_story_lust_is_complete():
    return kaya.progress.lust_step >= 3

# def kaya_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

def kaya_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (stephanie, "[kaya.fname] and [stephanie.fname] seem to get along well in the lab..."),
        1: (erica, "Two students in the same class at university?"),
        2: (nora, "Maybe someday you could join [nora.fname] and [kaya.fname] in the lab"),
    }
    return teamups


def kaya_story_other_list() -> dict[int, str]:
    other_story_dict: dict[int, str] = {}
    # kaya's other story index:
    # 0 - Current student status
    # 1 - Current Residency Status
    # 2 - Condom Talk Status
    # 3 - Current Pregnancy Status
    if kaya.progress.love_step >= 3:
        other_story_dict[0] = (
            "[kaya.fname] takes classes at the University on Tuesdays and Thursdays."
        )
    if kaya.progress.love_step >= 7:
        other_story_dict[1] = (
            "She also works for you in research as an intern on Monday, Wednesday, and Fridays."
        )
    if kaya_had_condom_talk():
        other_story_dict[2] = (
            "[kaya.fname] has made it clear she will not tolerate condom usage when you have sex."
        )
    elif kaya.sluttiness > 50:
        other_story_dict[2] = (
            "[kaya.fname] seems hesitant to have sex. You need to progress her stories or push her sluttiness to find out why."
        )
    if kaya.knows_pregnant:
        other_story_dict[3] = "[kaya.fname] is currently pregnant with your child!"

    return other_story_dict


####################
# Position Filters #
####################

def kaya_vaginal_position_filter(vaginal_position: Position):
    return kaya_had_condom_talk() and not kaya.has_taboo("vaginal_sex") # wait for unlock event that breaks vaginal taboo

def kaya_anal_position_filter(anal_position: Position):
    # for now unlock after a few creampies
    return kaya_had_condom_talk() and \
        kaya.vaginal_creampie_count > 3
