from __future__ import annotations
from game.major_game_classes.game_logic.Room_ren import aunt_apartment, cousin_bedroom
from game.major_game_classes.character_related.Person_ren import Person, mc, aunt, cousin
from game.major_game_classes.game_logic.Action_ren import Action
from game.game_roles.stripclub._stripclub_role_definitions_ren import strip_club_get_manager

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 3
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

#### Love Events ####

def aunt_first_date_tips_requirement(person: Person):
    if not person.is_at(aunt_apartment):
        return False
    return False    #Never got completed :(
    if person.story_event_ready("love") and person.love >= 20:
        return True

def add_aunt_first_date_tips_action():
    aunt.add_unique_on_room_enter_event(
        Action("Rebecca's dating problems", aunt_first_date_tips_requirement, "aunt_first_date_tips_label", priority = 30)
    )
    aunt.story_event_log("love")

##### Lust Events #####

def aunt_drunk_cuddle_requirement():
    return time_of_day == 4 and aunt.story_event_ready("slut") and aunt.sluttiness > 20 and not mc.has_scheduled_appointment

def add_aunt_drunk_cuddle_action():
    mc.business.add_mandatory_crisis(
        Action("Aunt Drunken Cuddle", aunt_drunk_cuddle_requirement, "aunt_drunk_cuddle_label")
    )
    aunt.story_event_log("slut")

def aunt_surprise_walk_in_requirement(person: Person):
    return (
        person.sluttiness > 40
        and person.story_event_ready("slut")
        and person.is_at(aunt_apartment)
        and not cousin.is_home
    )

def add_aunt_surprise_walk_in_action():
    aunt.add_unique_on_room_enter_event(
        Action("Aunt Surprise Show", aunt_surprise_walk_in_requirement, "aunt_surprise_walk_in_label", priority = 30)
    )
    aunt.story_event_log("slut")

def aunt_card_game_aftermath_requirement():
    return aunt.story_event_ready("slut") and aunt.progress.lust_step == 2 and aunt.sluttiness > 60

#No action to add card game aftermath because it is automatically called in the card game label.

def aunt_fucking_round_two_requirement():
    return aunt.progress.lust_step == 3 and aunt.days_since_event("story_event") >= TIER_1_TIME_DELAY and mc.energy > 80 and aunt.energy > 80


#### Obedience Events ####

def aunt_accounting_intro_requirement(person: Person):
    return (
        time_of_day in (2, 3)
        and person.story_event_ready("obedience")
        and person.is_at(aunt_apartment)
    )

def add_aunt_accounting_intro_action():
    aunt.add_unique_on_room_enter_event(
        Action("Rebecca's Accounting Intro", aunt_accounting_intro_requirement, "aunt_accounting_intro_label", priority = 30)
    )
    aunt.story_event_log("obedience")

def aunt_accounting_cpa_renewal_requirement():
    return aunt.story_event_ready("obedience") and time_of_day == 3 and aunt.has_event_day("moved_out")

def add_aunt_accounting_cpa_renewal_action():
    mc.business.add_mandatory_crisis(
        Action("Rebecca's CPA License", aunt_accounting_cpa_renewal_requirement, "aunt_accounting_cpa_renewal_label", priority = 30)
    )
    aunt.story_event_log("obedience")

def aunt_employment_problems_requirement(the_person):
    return aunt.story_event_ready("obedience") and time_of_day == 3 and aunt.obedience >= 120 and aunt.has_event_day("moved_out")

def add_aunt_employment_problems_action():
    aunt.add_unique_on_room_enter_event(
        Action("Rebecca's Employment Problems", aunt_employment_problems_requirement, "aunt_employment_problems_label", priority = 30)
    )
    aunt.story_event_log("obedience")


def aunt_cpa_first_day_requirement():
    return time_of_day == 1 and day % 7 == 1

def add_aunt_cpa_first_day_action():
    mc.business.add_mandatory_crisis(
        Action("Rebecca's CPA First Day", aunt_cpa_first_day_requirement, "aunt_cpa_first_day_label")
    )

def aunt_cpa_first_day_finish_requirement():
    return time_of_day == 3

def add_aunt_cpa_first_day_finish_action():
    mc.business.add_mandatory_crisis(
        Action("Rebecca's CPA First Day Finished", aunt_cpa_first_day_finish_requirement, "aunt_cpa_first_day_finish_label")
    )


def aunt_money_launder_offer_requirement() -> bool:
    return False
    if aunt.story_event_ready("obedience") and aunt.obedience >= 140 and time_of_day == 1 and day % 7 == 1:
        return True
    return False

def add_aunt_money_launder_offer_action():
    mc.business.add_mandatory_crisis(
        Action("Rebecca's Money Launder", aunt_money_launder_offer_requirement, "aunt_money_launder_offer_label")
    )
    aunt.story_event_log("obedience")


# Other events

def aunt_working_at_stripclub_requirement():
    return aunt.is_strip_club_employee and cousin.is_strip_club_employee and aunt.is_at_work and cousin.is_at_work and aunt.is_at_stripclub and cousin.is_at_stripclub

def add_aunt_starts_working_at_stripclub_action():
    if not aunt.event_triggers_dict.get("knows_about_stripping", False):
        mc.business.add_mandatory_crisis(
            Action("Rebecca starts working at stripclub", aunt_working_at_stripclub_requirement, "aunt_working_at_stripclub_label")
        )

def aunt_or_cousin_promotion_requirement(person: Person, start_day):
    return (
        day >= start_day
        and person.is_strip_club_employee
        and person.is_available
        and person.is_at_stripclub
        and cousin.is_strip_club_employee
        and cousin.is_available
        and not strip_club_get_manager()
    )

def add_aunt_working_at_stripclub_follow_up():
    aunt.add_unique_on_talk_event(
        Action("Promote Rebecca or Gabrielle", aunt_or_cousin_promotion_requirement, "aunt_or_cousin_promotion_label", requirement_args = [day + 7], priority = 30)
    )
