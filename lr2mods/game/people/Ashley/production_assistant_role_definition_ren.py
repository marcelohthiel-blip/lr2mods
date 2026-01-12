from __future__ import annotations
from game.business_policies.serum_policies_ren import testing_room_creation_policy, serum_production_2_policy, serum_production_3_policy
from game.main_character.mc_serums._mc_serum_definitions_ren import mc_serum_energy_regen
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import mall
from game.major_game_classes.character_related.Person_ren import Person, mc, camila, ashley
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import essential_oil_trait

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def mc_serum_review_requirement(person: Person):
    return mc.business.event_triggers_dict.get("mc_serum_energy_unlocked", False) and mc.business.is_open_for_business

def get_production_assistant_role_actions():
    mc_serum_review = Action("Review Personal Serums", mc_serum_review_requirement, "mc_serum_review_label",
        menu_tooltip = "Review your personal serum options, research progress, and refresh your dose.", priority = 20)

    return [mc_serum_review]

def prod_assistant_essential_oils_intro_requirement(person: Person):
    return production_assistant_progress_check()

def add_prod_assistant_essential_oils_intro_action():
    prod_assistant_essential_oils_intro = Action("Essential Oils Intro", prod_assistant_essential_oils_intro_requirement, "prod_assistant_essential_oils_intro_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_essential_oils_intro)

def quest_essential_oils_research_start_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office and mc.business.head_researcher is not None

def add_quest_essential_oils_research_start_action():
    quest_essential_oils_research_start = Action("Essential Oil Research", quest_essential_oils_research_start_requirement, "quest_essential_oils_research_start_label", priority = 30)
    mc.business.head_researcher.add_unique_on_talk_event(quest_essential_oils_research_start)


def quest_essential_oils_research_end_requirement(person: Person):
    return production_assistant_progress_check()

def add_quest_essential_oils_research_end_action():
    quest_essential_oils_research_end = Action("Essential Oil Outcome", quest_essential_oils_research_end_requirement, "quest_essential_oils_research_end_label", priority = 30)
    mc.business.head_researcher.add_unique_on_talk_event(quest_essential_oils_research_end)
    mc.business.set_event_day("prod_assistant_advance")

def quest_essential_oils_discover_supplier_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office

def add_quest_essential_oils_discover_supplier_action():
    quest_essential_oils_discover_supplier = Action("Find a Supplier", quest_essential_oils_discover_supplier_requirement, "quest_essential_oils_discover_supplier_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_talk_event(quest_essential_oils_discover_supplier)


def quest_essential_oils_decision_requirement(person: Person):
    return (
        time_of_day in (0, 1, 2)
        and person.is_at(mall)  # the_person is camila
    )

def add_quest_essential_oils_decision_action():
    quest_essential_oils_decision = Action("Talk to Supplier", quest_essential_oils_decision_requirement, "quest_essential_oils_decision_label", priority = 30)
    camila.add_unique_on_talk_event(quest_essential_oils_decision)
    mc.business.set_event_day("prod_assistant_advance")

def prod_assistant_unlock_auras_requirement(person: Person):
    return production_assistant_progress_check()

def add_prod_assistant_unlock_auras_action():
    prod_assistant_unlock_auras = Action("Unlock Aura Personal Serums", prod_assistant_unlock_auras_requirement, "prod_assistant_unlock_auras_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_unlock_auras)
    list_of_traits.append(essential_oil_trait)


def prod_assistant_unlock_cum_requirement(person: Person):
    return (
        person.cum_exposure_count > 0
        and production_assistant_progress_check()
    )

def add_prod_assistant_unlock_cum_action():
    prod_assistant_unlock_cum = Action("Unlock Cum Personal Serums", prod_assistant_unlock_cum_requirement, "prod_assistant_unlock_cum_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_unlock_cum)
    mc.business.set_event_day("prod_assistant_advance")


def prod_assistant_unlock_physical_requirement(person: Person):
    return (
        person.obedience > 140
        and production_assistant_progress_check()
    )

def add_prod_assistant_unlock_physical_action():
    prod_assistant_unlock_physical = Action("Unlock Physical Personal Serums", prod_assistant_unlock_physical_requirement, "prod_assistant_unlock_physical_label", priority = 30)
    mc.business.set_event_day("prod_assistant_advance")
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_unlock_physical)


def prod_assistant_performance_upgrade_requirement(person: Person):
    return (
        serum_production_2_policy.is_active
        and production_assistant_progress_check()
    )

def add_prod_assistant_performance_upgrade_action():
    prod_assistant_performance_upgrade = Action("Upgrade Performance Serums", prod_assistant_performance_upgrade_requirement, "prod_assistant_performance_upgrade_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_performance_upgrade)
    mc.business.set_event_day("prod_assistant_advance")


def prod_assistant_aura_upgrade_requirement(person: Person):
    return (
        serum_production_3_policy.is_active
        and production_assistant_progress_check()
    )

def add_prod_assistant_aura_upgrade_action():
    prod_assistant_aura_upgrade = Action("Upgrade Aura Serums", prod_assistant_aura_upgrade_requirement, "prod_assistant_aura_upgrade_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_aura_upgrade)
    mc.business.event_triggers_dict["mc_serum_aura_unlocked"] = True


def prod_assistant_cum_upgrade_requirement(person: Person):
    return (
        mc.business.research_tier >= 3
        and person.cum_exposure_count >= 7
        and production_assistant_progress_check()
    )

def add_prod_assistant_cum_upgrade_action():
    prod_assistant_cum_upgrade = Action("Upgrade Cum Serums", prod_assistant_cum_upgrade_requirement, "prod_assistant_cum_upgrade_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_cum_upgrade)
    mc.business.event_triggers_dict["mc_serum_cum_unlocked"] = True


def prod_assistant_physical_upgrade_requirement(person: Person):
    return (
        mc.business.research_tier >= 3
        and production_assistant_progress_check()
    )

def add_prod_assistant_physical_upgrade_action():
    prod_assistant_physical_upgrade = Action("Upgrade Physical Serums", prod_assistant_physical_upgrade_requirement, "prod_assistant_physical_upgrade_label", priority = 30)
    mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_physical_upgrade)
    mc.business.event_triggers_dict["mc_serum_physical_unlocked"] = True
    mc.business.set_event_day("prod_assistant_advance")

def cleanup_prod_assistant_meetings(person: Person):
    mc.business.remove_mandatory_crisis("Discover MC Serums")
    mc.business.remove_mandatory_crisis("Serums runout")

    #on room
    person.remove_on_room_enter_event("Serum Setup")
    person.remove_on_room_enter_event("Essential Oils Intro")
    person.remove_on_room_enter_event("Unlock Aura Personal Serums")
    person.remove_on_room_enter_event("Unlock Cum Personal Serums")
    person.remove_on_room_enter_event("Unlock Physical Personal Serums")
    person.remove_on_room_enter_event("Upgrade Performance Serums")
    person.remove_on_room_enter_event("Upgrade Aura Serums")
    person.remove_on_room_enter_event("Upgrade Cum Serums")
    person.remove_on_room_enter_event("Upgrade Physical Serums")

    #on talk
    person.remove_on_talk_event("Find a Supplier")

    #HR
    if mc.business.head_researcher:
        mc.business.head_researcher.remove_on_talk_event("Essential Oil Research")
        mc.business.head_researcher.remove_on_talk_event("Essential Oil Outcome")

    #camila on talk
    camila.remove_on_talk_event("Talk to Supplier")
    return

def production_assistant_alt_intro_requirement():
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False

    if ashley.is_employee:
        return False
    if testing_room_creation_policy.is_active and mc.business.days_since_event("testing_room_unlocked") > TIER_1_TIME_DELAY:
        if found := next((x for x in list_of_traits if x.name == mc_serum_energy_regen.linked_trait), None):
            return found.researched
    return False

def add_production_assistant_alt_intro_action():
    production_assistant_alt_intro = Action("Alternate MC Serums route", production_assistant_alt_intro_requirement, "production_assistant_alt_intro_label", priority = 30)
    mc.business.add_mandatory_crisis(production_assistant_alt_intro)

def remove_production_assistant_alt_intro_action():
    mc.business.remove_mandatory_crisis("Alternate MC Serums route")

def production_assistant_progress_check():  #Use this method to check and make sure we are ready to progress the production assistant.
    return (
        mc.business.is_open_for_business
        and mc.business.head_researcher is not None
        and mc.business.days_since_event("prod_assistant_advance") >= TIER_1_TIME_DELAY
        and mc.is_at_office
    )
