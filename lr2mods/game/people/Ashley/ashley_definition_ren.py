from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import heavy_eye_shadow, copper_ring_set, ponytail
from game.sex_positions._position_definitions_ren import blowjob, tit_fuck, reverse_cowgirl
from game.major_game_classes.character_related._job_definitions_ren import unemployed_job
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, list_of_instantiation_functions, ashley, stephanie, nora, lily
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Room_ren import purgatory
from game.personality_types._personality_definitions_ren import wild_personality
from game.people.Ashley.ashley_role_definition_ren import ashley_mc_submission_story_complete, init_ashley_roles

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
list_of_instantiation_functions.append("create_ashley_character")

def ashley_intro_requirement():   #After discovering an obedience serum trait and there is a position available. Must be at work.
    if day > TIER_3_TIME_DELAY and mc.is_at_office and mc.business.is_open_for_business:
        if not mc.business.at_employee_limit:
            return mc.business.research_tier > 0
    return False

def create_ashley_character():
    ashley_base_outfit = Outfit("ashley's base accessories")
    ashley_base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.18, .54, .34, 0.5])
    ashley_base_outfit.add_accessory(copper_ring_set.get_copy(), [.1, .36, .19, 0.95])

    ashley_wardrobe = wardrobe_from_xml("Ashley_Wardrobe")

    init_ashley_roles()

    global ashley
    ashley = make_person(name = "Ashley", last_name = stephanie.last_name, age_range = [22, 25], body_type = "standard_body", face_style = "Face_3", tits="DDD", height = 0.89, hair_colour = ["strawberry blonde", [0.644, 0.418, 0.273, 0.95]], hair_style = ponytail, skin="white",
        eyes = "brown", personality = wild_personality, name_color = "#228b22", starting_wardrobe = ashley_wardrobe, job = unemployed_job,
        stat_array = [1, 4, 4], skill_array = [1, 1, 3, 5, 1], sex_skill_array = [4, 2, 2, 2], sluttiness = 7, obedience_range = [70, 85], happiness = 119, love = 0,
        relationship = "Single", kids = 0, base_outfit = ashley_base_outfit, type = 'story', start_home = stephanie.home,
        forced_opinions = [
            ["production work", 2, True],
            ["work uniforms", -1, False],
            ["flirting", 1, False],
            ["working", 1, False],
            ["the colour green", 2, False],
            ["pants", 1, False],
            ["the colour blue", -1, False],
            ["classical music", 2, False]],
        forced_sexy_opinions = [
            ["taking control", 2, False],
            ["getting head", 2, False],
            ["drinking cum", -1, False],
            ["giving blowjobs", -2, False],
            ["public sex", -1, False],
            ["giving tit fucks", -2, False],
            ["doggy style sex", -2, False],
            ["bareback sex", 2, False],
            ["creampies", 1, False],
            ["being submissive", -2, False]],
        serum_tolerance = 1, work_experience = 1)

    ashley.home.add_person(ashley)
    ashley.set_override_schedule(purgatory)    # lock in purgatory until used

    ashley.set_title(ashley.name)
    ashley.set_possessive_title("your production assistant")
    ashley.set_mc_title(mc.name)
    ashley.on_birth_control = True

    mc.business.event_triggers_dict["mc_serum_duration"] = 3
    mc.business.event_triggers_dict["mc_serum_aura_tier"] = 0
    mc.business.event_triggers_dict["mc_serum_cum_tier"] = 0
    mc.business.event_triggers_dict["mc_serum_energy_tier"] = 0
    mc.business.event_triggers_dict["mc_serum_physical_tier"] = 0
    mc.business.event_triggers_dict["mc_serum_aura_unlocked"] = False
    mc.business.event_triggers_dict["mc_serum_cum_unlocked"] = False
    mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = False
    mc.business.event_triggers_dict["mc_serum_physical_unlocked"] = False
    mc.business.event_triggers_dict["mc_serum_max_quant"] = 1

    # set relationships
    town_relationships.update_relationship(ashley, stephanie, "Sister")
    town_relationships.update_relationship(nora, ashley, "Friend")
    town_relationships.update_relationship(lily, ashley, "Rival")

    mc.business.add_mandatory_crisis(
        Action("ashley_intro", ashley_intro_requirement, "ashley_intro_label")
    )

##############
# Story Info #
##############


def ashley_story_character_description():
    return "[ashley.name] is [stephanie.name]'s sister and you gave her job in your production department to help her out."

def ashley_story_love_list():
    love_story_list = {}
    if mc.business.p_div.person_count <= 1:
        love_story_list[0] = "Hire more production staff."
    elif ashley.is_employee and ashley.primary_job.days_employed < TIER_2_TIME_DELAY:
        love_story_list[0] = "Give [ashley.fname] time to settle into her new job."
    else:
        love_story_list[0] = "Talk to her about going to the classical concert."

    if ashley.progress.love_step == 0:
        if ashley.event_triggers_dict.get("concert_date", 0) == 0:
            return love_story_list
        if ashley.event_triggers_dict.get("concert_date", 0) == 1:
            love_story_list[0] = "Go with [ashley.fname] to the concert on Thursday night."
            return love_story_list

    love_story_list[0] = "You went with [ashley.fname] to a classical music concert."

    if ashley.progress.love_step == 1:
        if ashley.love < 20:
            love_story_list[1] = "Increase your love score with her to progress."
        elif not ashley.story_event_ready("love"):
            love_story_list[1] = "[ashley.fname] needs time before she is ready to progress this story."
        else:
            love_story_list[1] = "[ashley.fname] may approach you at work soon."
        return love_story_list

    love_story_list[1] = "She walked you home, and it seems she already knows your sister."

    if ashley.progress.love_step == 2:
        if ashley.love < 40:
            love_story_list[2] = "Increase [ashley.fname]'s love to at least 40."
        elif not ashley.story_event_ready("love"):
            love_story_list[2] = "[ashley.fname] needs some time to progress this story."
        else:
            love_story_list[2] = "[ashley.fname] will come over this evening."
        return love_story_list

    love_story_list[2] = "[ashley.fname] patched things up with your sister during movie night and they exchanged phone numbers."

    if ashley.progress.love_step == 3:
        if ashley.love < 60:
            love_story_list[3] = "Increase [ashley.fname]'s love to at least 60."
        elif not ashley.story_event_ready("love"):
            love_story_list[3] = "[ashley.fname] needs some time to progress this story."
        else:
            love_story_list[3] = "The next scene has not been written yet."
            #love_story_list[3] = "[ashley.fname] will come over this evening."

        return love_story_list

    love_story_list[3] = "The next scene has not been written yet."
    return love_story_list

def ashley_story_love_is_complete():
    return ashley.progress.love_step == 3 and ashley.love >= 60 and ashley.story_event_ready("love")

def ashley_story_lust_list():
    lust_story_list = {}

    if ashley.progress.lust_step == 0:
        if ashley.sluttiness < 20:
            lust_story_list[0] = "Increase [ashley.fname]'s sluttiness to progress"
        elif not ashley.story_event_ready("slut"):
            lust_story_list[0] = "[ashley.fname] needs a few days to adjust before progressing."
        else:
            lust_story_list[0] = "You think there will be progress with [ashley.fname] soon."
        return lust_story_list

    if not ashley.event_triggers_dict.get("porn_discovered", False):
        return lust_story_list

    lust_story_list[0] = "You should talk to [ashley.fname]'s sister about the video you found."

    if not ashley.event_triggers_dict.get("porn_discussed", False):
        return lust_story_list

    lust_story_list[0] = "You should talk to [ashley.fname] about the video you found."
    if not ashley.event_triggers_dict.get("porn_convo_avail", False):
        return lust_story_list

    lust_story_list[0] = "[ashley.fname] gave you a handjob after asking her about her porn video."

    if ashley.progress.lust_step == 1:
        if ashley.sluttiness < 40:
            lust_story_list[1] = "Increase [ashley.fname]'s sluttiness to progress"
        elif not ashley.story_event_ready("slut"):
            lust_story_list[1] = "[ashley.fname] needs a few days to adjust before progressing."
        elif not ashley.is_willing(blowjob):
            lust_story_list[1] = "[ashley.fname] needs to be willing to give blowjobs to progress."
        else:
            lust_story_list[1] = "You think there will be progress with [ashley.fname] soon."
        return lust_story_list

    lust_story_list[1] = "She gave you a blowjob while her sister was asking for advice!"

    if ashley.progress.lust_step == 2:
        lust_story_list[2] = "The rest of the story has not yet been written."

    #lust_story_list[1] = "You should talk to [ashley.fname] ASAP about the handjob."
    #lust_story_list[1] = "You should talk to [ashley.fname]'s sister about your relationships."

    return lust_story_list

def ashley_story_lust_is_complete():
    return ashley.progress.lust_step == 2

def ashley_story_obedience_list():
    obedience_story_list = {}

    obedience_story_list = ashley_story_path_submission.progress_description(ashley, ashley.event_triggers_dict.get("submission_path_index", 0))

    # if ashley.progress.obedience_step == 0:
    #     if ashley.obedience < 120:
    #         return {
    #             0: "Increase [ashley.fname]'s obedience to progress."
    #         }
    #     if ashley.days_since_event("obedience_event") < TIER_1_TIME_DELAY:
    #         return {
    #             0: "Wait a few days to progress."
    #         }

    #     obedience_story_list[0] = "Use obedience to convince [ashley.fname] to let you use her tits again."
    #     return obedience_story_list

    # obedience_story_list[0] = "You've convinced [ashley.fname] to let you fuck her tits anytime you want."

    # if ashley.progress.obedience_step == 1:
    #     if ashley.obedience < 150:
    #         obedience_story_list[1] = "Increase [ashley.fname]'s obedience to progress."
    #         return obedience_story_list
    #     if ashley.days_since_event("obedience_event") < TIER_1_TIME_DELAY:
    #         obedience_story_list[1] = "Wait a few days to progress."
    #         return obedience_story_list

    #     obedience_story_list[1] = "Use obedience to convince [ashley.fname] to blow you again."
    #     return obedience_story_list

    # obedience_story_list[1] = "[ashley.fname]'s mouth is available for your use whenever you want."

    # if ashley.progress.obedience_step == 2:
    #     if ashley.obedience < 180:
    #         obedience_story_list[2] = "Increase [ashley.fname]'s obedience to progress."
    #         return obedience_story_list
    #     if ashley.days_since_event("obedience_event") < TIER_1_TIME_DELAY:
    #         obedience_story_list[2] = "Wait a few days to progress."
    #         return obedience_story_list

    #     obedience_story_list[2] = "The next scene has not been written yet!"
    #     return obedience_story_list

    return obedience_story_list

def ashley_story_obedience_is_complete():
    return ashley.progress.obedience_step == 2

def ashley_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamup_story_list = {}

    teamup_story_list[0] = (stephanie, "[ashley.fname] and her sister would make an interesting pair to get together, but right now that seems impossible.")
    if ashley.progress.love_step >= 2:
        teamup_story_list[1] = (lily, "[ashley.fname] and your sister already seem to know each other. What might happen if you work on repairing their relationship?")

    return teamup_story_list

def ashley_story_other_list():
    other_story_list = {}
    if ashley.is_employee:
        other_story_list[0] = "You hired her as your production assistant."
    else:
        other_story_list[0] = "You did not hire her, locking you out of her stories."

    if ashley.event_triggers_dict.get("story_path", None) == "secret":
        other_story_list[1] = "You are keeping your relationship with [ashley.fname] a secret for now."
    elif ashley.event_triggers_dict.get("story_path", None) == "fwb":
        other_story_list[1] = "You are keeping your relationship with [ashley.fname] casual for now."

    if ashley_mc_submission_story_complete():
        other_story_list[2] = "[ashley.fname] had a plan to dominate you, but abandoned it."
    else:
        if ashley.event_triggers_dict.get("dom_fingers", False):
            other_story_list[2] = "[ashley.fname] sometimes requires you to finger her after work."

        if ashley.event_triggers_dict.get("dom_oral", False):
            other_story_list[3] = "[ashley.fname] sometimes requires you to go down on her after work."

        if ashley.event_triggers_dict.get("dom_fuck", False):
            other_story_list[4] = "[ashley.fname] fucks you after work whenever she wants."

    # if False: # need to set flags for this
    #     other_story_list[5] = "[ashley.fname] has given you a serum for personal use."
    #     other_story_list[5] = "[ashley.fname] can give you serums for personal use."

    # if False: # not yet written
    #     other_story_list[5] = "She has found a serum candidate that causes intense female libido that may be worth studying."

    #Ashley's other story indices:
    # 0 - Her attempting to get MC obedient
    # 1 - Your arrangement with Stephanie
    # 2 - arousal serum quest
    return other_story_list


####################
# Position Filters #
####################


def ashley_dom_finger_avail():
    return ashley.event_triggers_dict.get("dom_fingers", False)

def ashley_dom_oral_avail():
    return ashley.event_triggers_dict.get("dom_oral", False)

def ashley_dom_fuck_avail():
    return ashley.event_triggers_dict.get("dom_fuck", False)

def ashley_sub_titfuck_avail():
    return ashley.event_triggers_dict.get("sub_titfuck_avail", False)

def ashley_sub_oral_avail():
    return ashley.event_triggers_dict.get("sub_blowjob_avail", False)

def ashley_sub_fuck_avail():
    return ashley.event_triggers_dict.get("sub_fuck_avail", False)

def ashley_sub_anal_avail():
    return ashley.event_triggers_dict.get("sub_anal_avail", False)

def ashley_foreplay_position_filter(foreplay_position: Position):
    if not ashley_sub_titfuck_avail():
        return foreplay_position not in (tit_fuck, )
    return True

def ashley_oral_position_filter(oral_position: Position):
    return ashley_sub_oral_avail() \
        or ashley_dom_oral_avail()

def ashley_vaginal_position_filter(vaginal_position: Position):
    return ashley_sub_fuck_avail() \
        or ashley_dom_fuck_avail()

def ashley_anal_position_filter(anal_position: Position):
    return ashley_sub_anal_avail()

def ashley_oral_position_info():
    return "Complete the boobjob and subsequent blowjob training events"

def ashley_vaginal_position_info():
    return "Complete the bend over desk event"

def ashley_unique_sex_positions(person, prohibit_tags) -> list[tuple[Position, int]]:
    positions = []
    if ashley_dom_fuck_avail() and "Vaginal" not in prohibit_tags:
        positions.append((reverse_cowgirl, 1))
    return positions
