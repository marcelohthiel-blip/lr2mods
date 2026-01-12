from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.game_logic.Role_ren import Role
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.clothing_lists_ren import lipstick, landing_strip_pubes, messy_short_hair
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.game_logic.Room_ren import sex_store
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, starbuck, aunt
from game.people.Starbuck.starbuck_role_definition_ren import get_starbuck_role_actions, make_sex_shop_owner, get_shop_promo_stage, sex_shop_investment_average_return, sex_shop_stage
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
list_of_instantiation_functions.append("create_starbuck_character")

def starbuck_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.formal_address + " " + person.last_name)
    valid_titles.append("Cara")
    return valid_titles

def starbuck_possessive_titles(person: Person):
    valid_possessive_titles = []
    valid_possessive_titles.append(person.formal_address + " " + person.last_name)
    valid_possessive_titles.append("the sex shop owner")
    if sex_shop_stage() > 1:
        valid_possessive_titles.append("your business partner")
    if person.sluttiness > 60 and sex_shop_stage() > 1:
        valid_possessive_titles.append("your slutty business partner")
    return valid_possessive_titles

def starbuck_player_titles(person: Person):
    valid_player_titles = []
    valid_player_titles.append("Mr. " + mc.last_name)
    if sex_shop_stage() > 1:
        valid_player_titles.append("Business Partner")
    return valid_player_titles


def create_starbuck_character():
    starbuck_wardrobe = wardrobe_from_xml("Starbuck_Wardrobe")

    starbuck_personality = Personality("starbuck", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["skirts", "small talk", "the colour blue", "makeup"],
        common_sexy_likes = ["lingerie", "taking control", "doggy style sex", "creampies"],
        common_dislikes = ["working", "conservative outfits", "Mondays", "pants", "dresses"],
        common_sexy_dislikes = ["masturbating", "giving handjobs"],
        titles_function = starbuck_titles, possessive_titles_function = starbuck_possessive_titles, player_titles_function = starbuck_player_titles)

    # init starbuck role
    starbuck_role = Role(role_name ="Sex Shop Owner", actions = get_starbuck_role_actions(), hidden = True)

    starbuck_job = JobDefinition("Sex Shop Owner", starbuck_role, sex_store, day_slots = [0, 1, 2, 3, 4], time_slots = [2, 3])
    starbuck_job.set_schedule(sex_store, day_slots = [5], time_slots = [1, 2])

    global starbuck
    starbuck_base = Outfit("Starbuck's accessories")
    starbuck_lipstick = lipstick.get_copy()
    starbuck_lipstick.colour = [.80, .26, .04, .90]
    starbuck_base.add_accessory(starbuck_lipstick)

    starbuck = make_person(name = "Cara", last_name = "Thrace", age = 32, body_type = "curvy_body", face_style = "Face_4", tits="E", height = 0.89, hair_colour= ["golden blonde", [0.895, 0.781, 0.656, 0.95]], hair_style = messy_short_hair, skin = "white",
        eyes = ["green", [0.245, 0.734, 0.269, 0.9]], pubes_style = landing_strip_pubes, personality = starbuck_personality, name_color = "#cd5c5c", starting_wardrobe = starbuck_wardrobe, job = starbuck_job,
        stat_array = [3, 4, 3], skill_array = [1, 1, 4, 2, 1], sex_skill_array = [3, 4, 3, 4], sluttiness = 17, obedience_range = [70, 85], happiness = 119, love = 0,
        relationship = "Single", kids = 0, base_outfit = starbuck_base,
        forced_opinions = [
            ["conservative outfits", 2, True],
            ["Fridays", 1, False],
            ["working", 1, False],
            ["the colour black", 2, False],
            ["the colour red", 2, False],
            ["the colour purple", -2, False],
            ["skirts", 1, False],
            ["high heels", 1, False],
            ["pants", -2, False]],
        forced_sexy_opinions = [
            ["lingerie", 1, False],
            ["skimpy outfits", -1, False],
            ["giving blowjobs", 2, False],
            ["showing her tits", 1, False],
            ["drinking cum", 2, False],
            ["being submissive", 2, False]],
        serum_tolerance = 1, work_experience = 1, type = 'story')

    starbuck.generate_home()
    starbuck.home.add_person(starbuck)
    make_sex_shop_owner(starbuck)


##############
# Story Info #
##############

def cara_story_character_description():
    return "[starbuck.fname] is the owner of a local sex shop."

def cara_story_love_list():
    love_story_list = {}
    if starbuck.event_triggers_dict.get("shop_progress_stage", 0) == 0:
        love_story_list[0] = "Invest in [starbuck.fname]'s shop to start this story."
        return love_story_list
    if starbuck.progress.love_step == 0:
        if starbuck.love < 20:
            love_story_list[0] = "Increase [starbuck.fname]'s love to progress this story."
        else:
            love_story_list[0] = "[starbuck.fname] will be contacting you soon."
    else:
        love_story_list[0] = "You had a great coffee date with [starbuck.fname]. She seemed surprised in your interest in her."
        love_story_list[1] = "The rest of this story is a work in progress."

    return love_story_list

def cara_story_love_is_complete():
    return starbuck.event_triggers_dict.get("shop_progress_stage", 0) > 0 and starbuck.progress.love_step > 0

def cara_story_lust_list():
    lust_story_list = {}

    if starbuck.event_triggers_dict.get("shop_progress_stage", 0) == 0:
        lust_story_list[0] = "Invest in [starbuck.fname]'s shop to start this story."
        return lust_story_list
    if starbuck.progress.lust_step == 0:
        if starbuck.sluttiness < 20:
            lust_story_list[0] = "Increase [starbuck.fname]'s sluttiness to start this story."
        else:
            lust_story_list[0] = "Check in with [starbuck.fname] at the sex shop once in a while to start this story."
        return lust_story_list
    lust_story_list[0] = "[starbuck.fname] tested a foreplay enhancing device with you, and is now available at her store."

    if starbuck.progress.lust_step == 1:
        if starbuck.sluttiness < 40:
            lust_story_list[1] = "Increase [starbuck.fname]'s sluttiness to continue this story."
        else:
            lust_story_list[1] = "Check in with [starbuck.fname] at the sex shop once in a while to continue this story."
        return lust_story_list
    lust_story_list[1] = "You tested an oral sex enhancing lip balm with her at the store which you can buy if you runout."

    if starbuck.progress.lust_step == 2:
        if starbuck.sluttiness < 60:
            lust_story_list[2] = "Increase [starbuck.fname]'s sluttiness to continue this story."
        elif sex_shop_stage() < 2:
            lust_story_list[2] = "Invest more money into [starbuck.fname]'s business to continue this story."
        else:
            lust_story_list[2] = "Check in with [starbuck.fname] at the sex shop once in a while to continue this story."
        return lust_story_list
    lust_story_list[2] = "You fucked [starbuck.fname] with a multifunction cock ring to help her test it."

    if starbuck.progress.lust_step == 3:
        if starbuck.sluttiness < 80:
            lust_story_list[3] = "Increase [starbuck.fname]'s sluttiness to continue this story."
        else:
            lust_story_list[3] = "Check in with [starbuck.fname] at the sex shop once in a while to continue this story."
        return lust_story_list
    lust_story_list[3] = "You fucked [starbuck.fname]'s ass using a new special lubricant and she loved it."
    lust_story_list[4] = "This story is a work in progress."

    return lust_story_list

def cara_story_lust_is_complete():
    return starbuck.progress.lust_step > 3

def cara_story_obedience_list():
    obedience_story_list = {}

    if starbuck.event_triggers_dict.get("shop_progress_stage", 0) == 0:
        obedience_story_list[0] = "Invest in [starbuck.fname]'s shop to start this story."
        return obedience_story_list

    if starbuck.progress.obedience_step == 0:
        if starbuck.obedience < 120:
            obedience_story_list[0] = "Increase [starbuck.fname]'s obedience to progress this story."
        elif starbuck.story_event_ready("obedience"):
            obedience_story_list[0] = "Visit [starbuck.fname]'s shop in the evening when it is open to progress this story."
        else:
            obedience_story_list[0] = "[starbuck.fname] needs some time before advancing this story."
        return obedience_story_list
    else:
        obedience_story_list[0] = "You convinced [starbuck.fname] to dress up for you in exchange for help with her finances."

    if starbuck.progress.obedience_step == 1:
        if starbuck.obedience < 140:
            obedience_story_list[1] = "Increase [starbuck.fname]'s obedience to progress this story."
        elif starbuck.story_event_ready("obedience"):
            obedience_story_list[1] = "Visit [starbuck.fname]'s shop in the evening when it is open to progress this story."
        else:
            obedience_story_list[1] = "[starbuck.fname] needs some time before advancing this story."
        return obedience_story_list

    if starbuck.progress.obedience_step == 2:
        obedience_story_list[1] = "[starbuck.fname] is receptive to wearing a uniform. Keep her obedience high and keep at it."
        return obedience_story_list
    if starbuck.progress.obedience_step >= 3:
        obedience_story_list[1] = "You've convinced [starbuck.fname] to wear a uniform to the shop. Talk to her to modify her uniform wardrobe."
    obedience_story_list[2] = "The rest of this story is a work in progress."
    return obedience_story_list

def cara_story_obedience_is_complete():
    return starbuck.progress.obedience_step >= 3

def cara_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {}
    if starbuck_rebecca_teamup.get_stage() == -1:
        teamups[0] = (aunt, "Try advancing obedience stories for [aunt.fname] and [starbuck.fname]...")
    else:
        teamups[0] = (aunt, "[aunt.fname] and [starbuck.fname] meet at the sex shop every Friday morning.")

    return teamups

def cara_story_other_list():
    other_story_list = {}
    #starbucks other story index:
    # 0 - MC's investment level
    # 1 - MC's expected daily returns
    # 2 - Sex Shop Promo Stage

    if starbuck.event_triggers_dict.get("shop_progress_stage", 0) > 0:
        other_story_list[0] = "You have invested a small amount into [starbuck.fname]'s sex shop."
        other_story_list[1] = f"Your average daily return on investment is ${sex_shop_investment_average_return():,.0f}"
    else:
        return other_story_list #If we haven't invested yet, make sure we return a blank list
    if starbuck.event_triggers_dict.get("shop_progress_stage", 0) > 1:
        other_story_list[0] = "You have invested a significant amount into [starbuck.fname]'s sex shop. She considers you a major investor."
    if starbuck.event_triggers_dict.get("shop_progress_stage", 0) > 2:
        other_story_list[0] = "You have invested a large amount into [starbuck.fname]'s sex shop. She considers you a business partner."

    if get_shop_promo_stage() == 1.0:
        other_story_list[2] = "You haven't run any additional promotion materials with [starbuck.fname]"
    elif get_shop_promo_stage() == 2.0:
        other_story_list[2] = "You ran a promotional with [starbuck.fname] dressed in lingerie, which slightly bumped profits."
    elif get_shop_promo_stage() == 3.0:
        other_story_list[2] = "You ran a promotional video with [starbuck.fname] testing a dildo, which slightly increased profits."
    elif get_shop_promo_stage() == 4.0:
        other_story_list[2] = "You ran a promotional video with [starbuck.fname] testing edible underwear, which increased profits."
    elif get_shop_promo_stage() == 5.0:
        other_story_list[2] = "You ran a promotional video with [starbuck.fname] where you spanked and fucked her ass, which greatly increased profits."
    elif get_shop_promo_stage() == 6.0:
        other_story_list[2] = "You ran a promotional video with [starbuck.fname] where you fucked her ass while she was in a swing, which gave a huge increase in profits."

    return other_story_list

####################
# Position Filters #
####################
