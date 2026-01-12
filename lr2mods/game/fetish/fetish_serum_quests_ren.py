
from __future__ import annotations
import builtins
from game.clothing_lists_ren import lace_bra, garter_with_fishnets, high_heels, light_eye_shadow, heavy_eye_shadow, lipstick, thong, thin_bra, mini_skirt, tube_top, fishnets, slips
from game.random_lists_ren import colour_sky_blue, colour_black, colour_red, colour_pink, modify_transparency
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits
from game.major_game_classes.serum_related.serums.fetish_serums_ren import fetish_serum_unlock_count, get_body_monitor_serum, get_fetish_anal_serum, get_fetish_breeding_serum, get_fetish_cum_serum, get_fetish_exhibition_serum

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 12
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
def fetish_serum_quest_intro_requirement():
    return (time_of_day == 2
        and day > TIER_3_TIME_DELAY + TIER_2_TIME_DELAY
        and mc.business.research_tier >= 1
        and mc.is_at_office
        and mc.business.is_open_for_business
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_quest_intro():
    mc.business.add_mandatory_crisis(
        Action("Nanobot Discovery", fetish_serum_quest_intro_requirement, "fetish_serum_quest_intro_label")
    )

def body_monitoring_serum_phase_2_requirement():
    if day % 7 != 0 and mc.is_at_office and mc.business.is_open_for_business and mc.business.head_researcher and mc.business.head_researcher.is_at_office:
        fetish_serum = get_body_monitor_serum()
        return fetish_serum and fetish_serum.mastery_level > 3.0
    return False

def add_body_monitoring_serum_phase_2_action():
    mc.business.add_mandatory_crisis(
        Action("Body Monitor Upgrade", body_monitoring_serum_phase_2_requirement, "body_monitor_serum_upgrade_label")
    )

def body_monitoring_serum_upgrade_completed_action_requirement():
    return (time_of_day == 4
        and day % 7 == 6
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_body_monitor_upgrade_completed_action():
    mc.business.add_mandatory_crisis(
        Action("Body Monitor Upgrade Completed", body_monitoring_serum_upgrade_completed_action_requirement, "body_monitor_serum_upgrade_completed_label")
    )

def commission_next_nanobot_serum_requirement():
    return (
        # only when player has not started next step
        fetish_serum_unlock_count() == 0
        and not fetish_serum_research_in_progress()
        and not fetish_serum_coding_in_progress()
        and mc.business.is_open_for_business
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_at_office
    )

def add_commission_next_nanobot_serum():
    mc.business.add_mandatory_crisis(
        Action("Commission Next Nanobot Serum", commission_next_nanobot_serum_requirement, "commission_next_nanobot_serum_label")
    )

def fetish_serum_anal_requirement(min_day: int):
    return (day % 7 == 0
        and day > min_day
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_anal(min_day: int):
    mc.business.add_mandatory_crisis(
        Action("Anal Program", fetish_serum_anal_requirement, "fetish_serum_anal_label", requirement_args = min_day)
    )

def fetish_serum_anal_warning_requirement():
    if day % 7 != 0 and mc.is_at_office and mc.business.is_open_for_business:
        fetish_serum = get_fetish_anal_serum()
        if fetish_serum and fetish_serum.mastery_level > 3.0 and mc.business.head_researcher:
            return mc.business.head_researcher.is_available
    return False

def add_fetish_serum_anal_warning():
    mc.business.add_mandatory_crisis(
        Action("Anal Fetish Warning", fetish_serum_anal_warning_requirement, "fetish_serum_anal_warning_label")
    )

def fetish_serum_cum_requirement(min_day: int):
    return (day % 7 == 0
        and day > min_day
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_cum(min_day: int):
    mc.business.add_mandatory_crisis(
        Action("Cum Program", fetish_serum_cum_requirement, "fetish_serum_cum_label", requirement_args = min_day)
    )

def fetish_serum_cum_warning_requirement():
    if day % 7 != 0 and mc.is_at_office and mc.business.is_open_for_business:
        fetish_serum = get_fetish_cum_serum()
        if fetish_serum and fetish_serum.mastery_level > 3.0 and mc.business.head_researcher:
            return mc.business.head_researcher.is_available
    return False

def add_fetish_serum_cum_warning():
    mc.business.add_mandatory_crisis(
        Action("Cum Fetish Warning", fetish_serum_cum_warning_requirement, "fetish_serum_cum_warning_label")
    )

def fetish_serum_breeding_requirement(min_day: int):
    return (day % 7 == 0
        and day > min_day
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_breeding(min_day: int):
    mc.business.add_mandatory_crisis(
        Action("Reproduction Program", fetish_serum_breeding_requirement, "fetish_serum_breeding_label", requirement_args = min_day)
    )

def fetish_serum_breeding_warning_requirement():
    if day % 7 != 0 and mc.is_at_office and mc.business.is_open_for_business:
        fetish_serum = get_fetish_breeding_serum()
        if fetish_serum and fetish_serum.mastery_level > 3.0 and mc.business.head_researcher:
            return mc.business.head_researcher.is_available
    return False

def add_fetish_serum_breeding_warning():
    mc.business.add_mandatory_crisis(
        Action("Breeding Fetish Warning", fetish_serum_breeding_warning_requirement, "fetish_serum_breeding_warning_label")
    )

def fetish_serum_sexual_proclivity_requirement(min_day: int):
    return (day % 7 == 0
        and day > min_day
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_sexual_proclivity(min_day: int):
    mc.business.add_mandatory_crisis(
        Action("Sexual Proclivity Program", fetish_serum_sexual_proclivity_requirement, "fetish_sexual_proclivity_label", requirement_args = min_day)
    )

def fetish_serum_exhibition_requirement(min_day: int):
    return (day % 7 == 0
        and day > min_day
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_exhibition(min_day: int):
    mc.business.add_mandatory_crisis(
        Action("Exhibition Program", fetish_serum_exhibition_requirement, "fetish_serum_exhibition_label", requirement_args=min_day)
    )

def fetish_serum_exhibition_warning_requirement():
    if day % 7 != 0 and mc.is_at_office and mc.business.is_open_for_business:
        fetish_serum = get_fetish_exhibition_serum()
        if fetish_serum and fetish_serum.mastery_level > 3.0 and mc.business.head_researcher:
            return mc.business.head_researcher.is_available
    return False

def add_fetish_serum_exhibition_warning():
    mc.business.add_mandatory_crisis(
        Action("Exhibition Fetish Warning", fetish_serum_exhibition_warning_requirement, "fetish_serum_exhibition_warning_label")
    )

def fetish_serum_coding_activity_requirement():
    if mc.is_at_office and mc.business.head_researcher and fetish_serum_coding_in_progress():
        if mc.business.head_researcher.is_at(mc.location):
            return True
        return "Head Researcher must be present"
    return False

def add_fetish_serum_coding_activity():
    mc.business.r_div.add_action(
        Action("Design Nanobot Program {image=time_advance}", fetish_serum_coding_activity_requirement, "fetish_serum_coding_activity_label",
            menu_tooltip = "Spend some time coding the new Nanobot Program", priority = 10)
    )

def fetish_serum_quest_intro_followup_requirement(the_day):
    return (day > the_day
        and mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available)

def add_fetish_serum_quest_intro_followup():
    mc.business.add_mandatory_crisis(
        Action("Nanobot Discovery Followup", fetish_serum_quest_intro_followup_requirement, "fetish_serum_quest_intro_followup_label", requirement_args = day + 6 - day % 7)
    )

def get_fetish_serum_contact():
    return mc.business.event_triggers_dict.get("fetish_serum_contact", None)

def fetish_serum_research_in_progress():
    return mc.business.event_triggers_dict.get("fetish_serum_research_active", False)

def fetish_serum_coding_in_progress():
    return mc.business.event_triggers_dict.get("fetish_serum_coding_active", False)

def fetish_serum_get_coding_progress():
    return mc.business.event_triggers_dict.get("fetish_serum_code_progress", 0)

def set_fetish_serum_coding_target(trait: SerumTrait):
    mc.business.event_triggers_dict["fetish_serum_coding_active"] = True
    mc.business.event_triggers_dict["fetish_serum_code_progress"] = 0
    mc.business.event_triggers_dict["fetish_serum_coding_target"] = trait.name

def fetish_serum_get_coding_target():
    coding_target_name = mc.business.event_triggers_dict.get("fetish_serum_coding_target", None)
    if coding_target_name:
        return next((x for x in list_of_traits if x.name == coding_target_name), None)
    return None

def fetish_serum_has_previously_coded():
    return mc.business.event_triggers_dict.get("fetish_serum_prior_coding", False)

def fetish_serum_get_estimated_coding_progress():
    return builtins.int((mc.int + mc.focus + mc.research_skill) / 2)

def fetish_serum_coding_percent_done():
    work_required = fetish_serum_coding_work_required()
    if work_required == 0:
        return 100
    return (fetish_serum_get_coding_progress() * 100) / work_required

def fetish_serum_coding_work_required():
    target = fetish_serum_get_coding_target()
    if target:
        return target.research_needed // 10    # coding is harder based on research needed
    return 0

def fetish_serum_update_coding_progress(progress):
    mc.business.event_triggers_dict["fetish_serum_code_progress"] = builtins.int(fetish_serum_get_coding_progress() + progress)

def fetish_add_collar(person: Person, collar: Clothing):
    new_collar = collar.get_copy()
    new_collar.colour = [.1, .1, .1, .9]
    new_collar.pattern = "Pattern_1"
    new_collar.colour_pattern = [.95, .95, .95, .9]
    person.base_outfit.add_accessory(new_collar)

def set_special_fetish_outfit(person: Person, opinion_color = None):
    outfit = Outfit("A Special Night")
    outfit.add_upper(lace_bra.get_copy(), colour_pink)
    outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
    outfit.add_feet(high_heels.get_copy(), colour_pink)
    outfit.add_accessory(light_eye_shadow.get_copy(), modify_transparency(colour_black, 0.5))
    outfit.add_accessory(heavy_eye_shadow.get_copy(), modify_transparency(colour_sky_blue, 0.5))
    outfit.add_accessory(lipstick.get_copy(), modify_transparency(colour_red, 0.4))
    person.apply_outfit(person.personalize_outfit(outfit, opinion_color = opinion_color))

#colour_sky_blue
def set_special_fetish_blue_outfit(person: Person, opinion_color = None):
    outfit = Outfit("A Special Night")
    outfit.add_lower(thong.get_copy(), colour_sky_blue)
    outfit.add_upper(thin_bra.get_copy(), colour_sky_blue)
    outfit.add_lower(mini_skirt.get_copy(), colour_black)
    outfit.add_upper(tube_top.get_copy(), colour_sky_blue)
    outfit.add_feet(fishnets.get_copy(), colour_black)
    outfit.add_feet(slips.get_copy(), colour_black)
    outfit.add_accessory(light_eye_shadow.get_copy(), modify_transparency(colour_black, 0.5))
    outfit.add_accessory(heavy_eye_shadow.get_copy(), modify_transparency(colour_sky_blue, 0.5))
    outfit.add_accessory(lipstick.get_copy(), modify_transparency(colour_red, 0.4))
    person.apply_outfit(person.personalize_outfit(outfit, opinion_color = opinion_color))
