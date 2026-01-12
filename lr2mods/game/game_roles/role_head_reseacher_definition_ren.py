#HEAD RESEARCHER ACTION REQUIREMENTS#
from __future__ import annotations
import renpy
from game.business_policies.serum_policies_ren import testing_room_creation_policy
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
def advanced_serum_stage_2_requirement(person: Person, earliest_trigger_day: int):
    if mc.business.is_open_for_business:
        return day >= earliest_trigger_day
    return False

def add_advance_serum_unlock_stage_two(person: Person):
    mc.business.event_triggers_dict["advanced_serum_stage_1"] = True
    mc.business.add_mandatory_crisis(
        Action("Advanced serum unlock stage 2", advanced_serum_stage_2_requirement, "advanced_serum_stage_2_label", args = person, requirement_args = [person, day + renpy.random.randint(2, 4)])
    ) #Append it to the mandatory crisis list so that it will be run eventually. We will list the person and the random day that the event will finish.

def head_researcher_suggest_testing_room_requirement():
    if mc.business.research_tier >= 1 and mc.business.days_since_event("tier_1_serum_unlock_day") > TIER_2_TIME_DELAY:
        if mc.business.head_researcher and mc.business.head_researcher.is_available:
            return mc.is_at_office and mc.business.is_open_for_business
    return False

def add_suggest_testing_room():
    mc.business.set_event_day("tier_1_serum_unlock_day", day)
    mc.business.add_mandatory_crisis(
        Action("Testing room request", head_researcher_suggest_testing_room_requirement, "head_researcher_suggest_testing_room_label")
    )

def head_researcher_testing_room_intro_requirement(person: Person):
    if testing_room_creation_policy.is_active and mc.is_at_office:
        return (mc.business.is_open_for_business and mc.business.head_researcher and mc.business.head_researcher.is_available)
    return False

def add_head_researcher_testing_room_intro(person: Person):
    mc.business.event_triggers_dict["testing_room_policy_avail"] = True
    person.add_unique_on_room_enter_event(
        Action("Testing Room Intro", head_researcher_testing_room_intro_requirement, "head_researcher_testing_room_intro_label")
    )

def head_researcher_strip_tease_requirement(person: Person):
    if person.obedience >= 140 and person.days_since_event("obedience_event") >= TIER_2_TIME_DELAY:
        return mc.is_at_office and mc.business.is_open_for_business
    return False

def add_head_researcher_strip_tease_event(person: Person):
    mc.business.set_event_day("serum_trait_test")
    person.set_event_day("obedience_event")

    person.add_unique_on_room_enter_event(
        Action("Head Researcher Strip Tease", head_researcher_strip_tease_requirement, "head_researcher_strip_tease_label")
    )

def head_researcher_cure_discovery_intro_requirement():
    if mc.business.is_open_for_business and mc.business.head_researcher is not None and mc.business.head_researcher.is_available: #Only trigger if people are in the office.
        if mc.business.head_researcher.days_since_event("obedience_event") >= TIER_2_TIME_DELAY and mc.business.head_researcher.obedience >= 160:
            return len(mc.business.market_team) > 0
    return False

def add_head_researcher_cure_discovery_intro(person: Person):
    person.set_event_day("obedience_event")
    mc.business.add_mandatory_crisis(
        Action("Begin Cure Discovery Quest", head_researcher_cure_discovery_intro_requirement, "head_researcher_cure_discovery_intro_label")
    )

def head_researcher_cure_discovery_market_patent_requirement(person: Person):
    return mc.business.is_open_for_business and person.is_at_office

def add_head_researcher_cure_discovery_market_patent(person: Person):
    person.add_unique_on_talk_event(
        Action("Attempt to sell patent", head_researcher_cure_discovery_market_patent_requirement, "head_researcher_cure_discovery_market_patent_label")
    )

def head_researcher_cure_discovery_patent_sold_requirement(person: Person):
    if mc.business.is_open_for_business and mc.business.head_researcher is not None and mc.business.head_researcher.is_available:
        return mc.business.head_researcher.days_since_event("obedience_event") >= TIER_1_TIME_DELAY
    return False

def add_head_researcher_cure_discovery_patent_sold(person: Person):
    mc.business.head_researcher.set_event_day("obedience_event")
    person.add_unique_on_room_enter_event(
        Action("Patent Sold", head_researcher_cure_discovery_patent_sold_requirement, "head_researcher_cure_discovery_patent_sold_label")
    )

def head_researcher_cure_discovery_patent_kept_requirement():
    if mc.business.is_open_for_business and mc.business.head_researcher is not None and mc.business.head_researcher.is_available:
        return mc.business.head_researcher.days_since_event("obedience_event") >= TIER_1_TIME_DELAY
    return False

def add_head_researcher_cure_discovery_patent_kept(person: Person):
    person.set_event_day("obedience_event")
    mc.business.add_mandatory_crisis(
        Action("Patent Stolen", head_researcher_cure_discovery_patent_kept_requirement, "head_researcher_cure_discovery_patent_kept_label")
    )

def head_researcher_cure_finish_requirement(person: Person):
    return mc.business.is_open_for_business and mc.business.head_researcher is not None and mc.business.head_researcher.is_available

def add_head_researcher_cure_finish():
    mc.business.head_researcher.add_unique_on_talk_event(
        Action("Cure Reward", head_researcher_cure_finish_requirement, "head_researcher_cure_finish_label")
    )
