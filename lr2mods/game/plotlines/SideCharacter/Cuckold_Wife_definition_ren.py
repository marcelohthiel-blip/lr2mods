from __future__ import annotations
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Person_ren import Person, make_character_unique, mc, list_of_instantiation_functions
from game.major_game_classes.game_logic.Action_ren import Action
from game.map.HomeHub_ren import industrial_home_hub

TIER_1_TIME_DELAY = 3
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
list_of_instantiation_functions.append("init_cuckold_wife")


def cuckold_employee_init_requirement():
    if day < TIER_3_TIME_DELAY * 2:
        return False  # don't start too early
    if mc.business.mc_offspring_count + len(mc.business.employees_knocked_up_by_mc) <= 2: #kids or knocked up at least 3 employees so far
        return False
    if mc.business.employee_count < 10:
        return False  # wait until we have a sizeable business
    if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 0:
        return False  # disabled until glory hole unlocked

    # check if we have a married woman without kids who is slutty enough for breeding
    return not find_avail_cuckold_employee() is None

def init_cuckold_wife():
    mc.business.add_mandatory_crisis(
        Action("Initialize cuckold", cuckold_employee_init_requirement, "cuckold_employee_init_label")
    )

def cuckold_employee_intro_requirement():
    return mc.is_at_office and mc.business.is_open_for_business

def add_cuckold_employee_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Cuckold Intro", cuckold_employee_intro_requirement, "cuckold_employee_intro_label")
    )

def cuckold_employee_decision_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business):
        return False

    person = get_cuckold_wife()
    if person is None:
        return True #Return true so that the event clears and we clean up at the start of the label.
    return person.days_since_event("breeding_event") >= TIER_1_TIME_DELAY

def add_cuckold_employee_decision_action(person: Person):
    person.set_event_day("breeding_event")
    mc.business.add_mandatory_crisis(
        Action("Cuckold Reveal", cuckold_employee_decision_requirement, "cuckold_employee_decision_label")
    )

def cuckold_employee_rethink_decision_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business):
        return False

    person = get_cuckold_wife()
    if person is None:
        return True
    return person.days_since_event("breeding_event") >= TIER_1_TIME_DELAY

cuckold_employee_rethink_decision = Action("Cuckold Submits", cuckold_employee_rethink_decision_requirement, "cuckold_employee_rethink_decision_label")

def cuckold_employee_breeding_session_requirement(person: Person):
    return mc.is_at_office and person.is_at_office and not person.knows_pregnant

def add_cuckold_employee_breeding_session_action(person: Person):
    person.add_unique_on_talk_event(
        Action("Cuckold Breeding Session", cuckold_employee_breeding_session_requirement, "cuckold_employee_breeding_session_label")
    )

def cuckold_employee_gloryhole_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business):
        return False

    person = get_cuckold_wife()
    if person is None:
        return True

    return person.days_since_event("breeding_event") >= TIER_1_TIME_DELAY

def add_cuckold_employee_gloryhole_action():
    mc.business.add_mandatory_crisis(
        Action("Cuckold at Glory Hole", cuckold_employee_gloryhole_requirement, "cuckold_employee_gloryhole_label")
    )

def cuckold_employee_after_window_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business):
        return False

    person = get_cuckold_wife()
    if person is None:
        return True

    return person.days_since_event("breeding_event") >= 7

def add_cuckold_employee_after_window_action():
    mc.business.add_mandatory_crisis(
        Action("Cuckold Aftermath", cuckold_employee_after_window_requirement, "cuckold_employee_after_window_label")
    )

def cuckold_employee_reconsider_requirement(person: Person):
    return True

def add_cuckold_employee_reconsider_action(person: Person):
    person.remove_on_talk_event("cuckold_employee_breeding_session_label")
    person.add_unique_on_talk_event(
        Action("Cuckold Reluctance", cuckold_employee_reconsider_requirement, "cuckold_employee_reconsider_label")
    )

def cuckold_employee_knocked_up_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business):
        return False

    person = get_cuckold_wife()
    if person is None:
        return True

    return person.days_since_event("breeding_event") >= TIER_1_TIME_DELAY

def add_cuckold_employee_knocked_up_action():
    mc.business.add_mandatory_crisis(
        Action("Cuckold Success", cuckold_employee_knocked_up_requirement, "cuckold_employee_knocked_up_label")
    )

def cuckold_employee_fertile_return_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business):
        return False

    person = get_cuckold_wife()
    if person is None:
        return True

    return person.is_highly_fertile    #She has started a new fertile period

def add_cuckold_employee_fertile_return_action():
    mc.business.add_mandatory_crisis(
        Action("Cuckold Return", cuckold_employee_fertile_return_requirement, "cuckold_employee_fertile_return_label")
    )

def setup_cuckold_employee():
    if persistent.pregnancy_pref == 0:
        return  # pregnancy disable, so this event is disabled

    person = find_avail_cuckold_employee()
    if person is None:
        init_cuckold_wife() # reset event
        return

    mc.business.event_triggers_dict["cuckold_employee_ident"] = person.identifier
    person.event_triggers_dict["no_pregnancy"] = True   # enable pregnancy_lock
    person.set_opinion("creampies", 2, False)
    person.set_opinion("bareback sex", 2, False)
    person.set_opinion("vaginal sex", 2, False)
    person.on_birth_control = False
    person.change_baby_desire(200)
    make_character_unique(person, industrial_home_hub)
    add_cuckold_employee_intro_action()

def find_avail_cuckold_employee():
    able_person_list = []
    for person in [x for x in mc.business.employees_availabe if x.sluttiness >= 50 and x.kids == 0
            and not x.is_clone
            and x.relationship == "Married" and not x.is_pregnant]:
        able_person_list.append(person)
    return get_random_from_list(able_person_list)

def get_cuckold_wife():
    person = Person.get_person_by_identifier(mc.business.event_triggers_dict.get("cuckold_employee_ident", None))
    if person is None or not person.is_employee:
        return None
    return person
