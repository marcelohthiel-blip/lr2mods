from __future__ import annotations
from game.major_game_classes.business_related.Infraction_ren import Infraction
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.business_related._punishments_ren import list_of_punishments
from game.game_roles.business_roles._business_role_definitions_ren import employee_freeuse_role

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

def employee_busywork_on_turn(person: Person):
    if mc.business.is_open_for_business:
        mc.business.change_team_effectiveness(-1) #She's slightly worse for efficiency because she's not focusing

def employee_busywork_on_day(person: Person):
    if mc.business.is_open_for_business:
        person.change_obedience(1)

def employee_busywork_report_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office

def add_busywork_report_action(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Busywork report crisis", employee_busywork_report_requirement, "employee_busywork_report_label", args = person, requirement_args = person)
    )

def employee_freeuse_report_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office

def remove_employee_freeuse_role(person: Person):
    person.remove_role(employee_freeuse_role, remove_linked = False)
    if person.is_employee:
        mc.business.add_mandatory_crisis(
            Action("Freeuse report crisis", employee_freeuse_report_requirement, "employee_freeuse_report_label", args = person, requirement_args = person)
        )

def employee_humiliating_work_on_turn(person: Person):
    if mc.business.is_open_for_business:
        mc.business.change_team_effectiveness(-2) #Worse for team efficiency

def employee_humiliating_work_on_day(person: Person):
    if mc.business.is_open_for_business:
        person.change_stats(happiness = -5, obedience = 2)

def employee_humiliating_work_report_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office

def add_humiliating_work_report_action(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Humiliating work report crisis", employee_busywork_report_requirement, "employee_humiliating_work_report_label", args = person, requirement_args = person)
    )

def get_infraction_list_menu(person: Person):
    infraction_list = []
    for infraction in person.infractions:
        infraction_list.append((f"{infraction.name}\n{{size=16}}Severity {infraction.severity}, Valid for {infraction.days_valid - infraction.days_existed} days{{/size}} (tooltip){infraction.desc}", infraction))
    infraction_list.append(("Return", "Return"))
    return infraction_list

def build_employee_infraction_choice_menu(person: Person, selected_infraction: Infraction):
    valid_punishments = ["Available Punishments"]
    invalid_punishments = ["Locked Punishments"]
    other_actions = ["Other Actions"]

    for punishment in list_of_punishments:
        if punishment.is_action_enabled([person, selected_infraction]):
            valid_punishments.append((punishment, (person, selected_infraction))) # This list is broken down by the menu function, the nested list are extra arguments so it can check which buttons are enabled.
        else:
            invalid_punishments.append((punishment, (person, selected_infraction)))

    other_actions.append(("Back", "Back"))

    return [valid_punishments, invalid_punishments, other_actions]

def employee_increase_job_experience(person: Person):
    if not person.is_at_work:
        return

    job = person.current_job
    if job.seniority_level >= 8:
        return  # max seniority reached (prevent cheating without affecting story)

    if job.job_definition in mc.business.research_jobs:
        job.seniority_level += 1
        if person.research_skill < job.seniority_level + 2:
            person.change_research_skill(1)
    elif job.job_definition in mc.business.market_jobs:
        job.seniority_level += 1
        if person.market_skill < job.seniority_level + 2:
            person.change_market_skill(1)
    elif job.job_definition in mc.business.supply_jobs:
        job.seniority_level += 1
        if person.supply_skill < job.seniority_level + 2:
            person.change_supply_skill(1)
    elif job.job_definition in mc.business.production_jobs:
        job.seniority_level += 1
        if person.production_skill < job.seniority_level + 2:
            person.change_production_skill(1)
    elif job.job_definition in mc.business.hr_jobs:
        job.seniority_level += 1
        if person.hr_skill < job.seniority_level + 2:
            person.change_hr_skill(1)
    else:
        return  # we are not performing a business related job

    mc.log_event(f"{person.display_name} work experience for {job.job_title}, now: {job.seniority_level}", "float_text_grey")
