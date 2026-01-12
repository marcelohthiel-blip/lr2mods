from __future__ import annotations
import renpy
from game.map.MapHub_ren import mall_hub
from game.game_roles.maid_role_definition_ren import assign_maid_job
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, sarah, naomi
from game.major_game_classes.character_related.Schedule_ren import Schedule
from game.major_game_classes.game_logic.Room_ren import kitchen, bedroom, mom_bedroom, lily_bedroom, hall

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def naomi_reconciliation_requirement(person: Person):
    return time_of_day in (1, 2, 3) and person.location.is_public

def add_naomi_reconciliation_action():
    naomi.set_override_schedule(None)
    naomi_reconciliation_action = Action("Naomi reconciliation", naomi_reconciliation_requirement, "Sarah_naomi_reconciliation_label", priority = 30)
    naomi.add_unique_on_room_enter_event(naomi_reconciliation_action)

def talk_to_sarah_about_naomi_requirement(person: Person):
    return mc.is_at_office and mc.business.is_open_for_business

def add_talk_to_sarah_about_naomi_action():
    talk_to_sarah_about_naomi_action = Action("Sarah talk about Naomi", talk_to_sarah_about_naomi_requirement, "Sarah_talk_about_naomi_label", priority = 30)
    sarah.add_unique_on_talk_event(talk_to_sarah_about_naomi_action)

def naomi_visits_to_apologize_requirement(the_day: int):
    if day <= the_day or day % 7 != 2 or time_of_day != 2:
        return False
    return True

def add_naomi_visits_to_apologize_action():
    naomi_visits_to_apologize_action = Action("Naomi visits to apologise", naomi_visits_to_apologize_requirement, "Sarah_naomi_visits_to_apologize_label", requirement_args = day)
    mc.business.add_mandatory_crisis(naomi_visits_to_apologize_action)

def naomi_asks_for_a_job_requirement(the_day: int):
    if day <= the_day or day % 7 != 2 or time_of_day != 2:
        return False
    return True

def add_naomi_asks_for_a_job_action(target_day: int):
    naomi_asks_for_a_job_action = Action("Naomi asks for a job", naomi_asks_for_a_job_requirement, "naomi_asks_for_a_job_label", requirement_args = target_day)
    mc.business.add_mandatory_crisis(naomi_asks_for_a_job_action)

def hire_naomi_as_maid(person: Person):
    mc.phone.register_number(person)
    job = assign_maid_job(person, daily_wage = 35, start_day = Schedule.next_monday())
    job.set_schedule(kitchen, day_slots = [0, 2, 4], time_slots = [1])
    job.set_schedule(mom_bedroom, day_slots = [1, 3], time_slots = [1])
    job.set_schedule(hall, day_slots = [0, 2, 4], time_slots = [2])
    job.set_schedule(lily_bedroom, day_slots = [1, 3], time_slots = [2])
    job.set_schedule(bedroom, day_slots = [0, 1, 2, 3], time_slots = [3])

def catch_naomi_slacking_off_requirement(person: Person, target_day: int):
    return day > target_day and naomi.is_at_work and person.is_at(kitchen) and person.location.person_count == 1

def add_catch_naomi_slacking_off_action():
    naomi.add_unique_on_room_enter_event(
        Action("Naomi Slacking Off", catch_naomi_slacking_off_requirement, "catch_naomi_slacking_off_label", requirement_args = day + renpy.random.randint(6, 8), priority = 30)
    )

def catch_naomi_masturbating_requirement(person: Person, target_day: int):
    return day > target_day and naomi.is_at_work and person.is_at(bedroom) and person.location.person_count == 1

def add_catch_naomi_masturbating_action():
    naomi.add_unique_on_room_enter_event(
        Action("Naomi Masturbating", catch_naomi_masturbating_requirement, "catch_naomi_masturbating_label", requirement_args = day + renpy.random.randint(6, 8), priority = 30)
    )
