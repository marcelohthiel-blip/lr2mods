from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, mc, ellie
from game.major_game_classes.character_related.Schedule_ren import Schedule
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def ellie_on_day(person: Person):
    #subtract sluttiness based on her story progress.
    return

def ellie_on_turn(person: Person):
    if person.is_employee and person.arousal_perc < 30 and person.is_at_office:
        person.change_arousal(3, add_to_log = False)

def ellie_work_grope_requirement(person: Person):
    #MC can tell that she is aroused from working on nanobots and sexual research.
    return person.arousal_perc >= 20 and mc.is_at_office and person.is_at_office and person.days_since_event("last_grope") > 0

def ellie_work_blowjob_requirement(person: Person):
    return False

def ellie_work_fuck_requirement(person: Person):
    return False

def ellie_work_anal_requirement(person: Person):
    return False

def get_ellie_lust_role_actions():
    ellie_work_grope = Action("Sluttiness: Grope Her", ellie_work_grope_requirement, "ellie_work_grope_label", priority = 20)
    ellie_work_blowjob = Action("Sluttiness: Blowjob", ellie_work_blowjob_requirement, "ellie_work_blowjob_label", priority = 20)
    ellie_work_fuck = Action("Sluttiness: Fuck Her", ellie_work_fuck_requirement, "ellie_work_fuck_label", priority = 20)
    ellie_work_anal = Action("Sluttiness: Fuck Her Ass", ellie_work_anal_requirement, "ellie_work_anal_label", priority = 20)
    return [ellie_work_grope, ellie_work_blowjob, ellie_work_fuck, ellie_work_anal]

def init_ellie_roles():
    global ellie_role
    ellie_role = Role("Ellie Pious", [], on_day = ellie_on_day, on_turn = ellie_on_turn)
    global ellie_lust_role
    ellie_lust_role = Role(role_name ="Ellie Slut", actions = get_ellie_lust_role_actions(), hidden = True)




def ellie_meet_ellie_intro_requirement():
    return time_of_day == 4 and day % 7 == 3

def add_ellie_meet_ellie_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Meet Your Blackmailer", ellie_meet_ellie_intro_requirement, "ellie_meet_ellie_intro_label")
    )

def ellie_head_researcher_halfway_intro_requirement():
    return time_of_day == 3 and day % 7 == 0

def add_ellie_head_researcher_halfway_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Blackmailer Identity", ellie_head_researcher_halfway_intro_requirement, "ellie_head_researcher_halfway_intro_label")
    )

def ellie_unnecessary_payment_requirement():
    return time_of_day == 4 and day % 7 == 3

def add_ellie_unnecessary_payment_action():
    mc.business.add_mandatory_crisis(
        Action("Pay Blackmailer", ellie_unnecessary_payment_requirement, "ellie_unnecessary_payment_label")
    )

def ellie_self_research_identity_requirement():
    return time_of_day == 3 and day % 7 == 0

def add_ellie_self_research_identity_action():
    mc.business.add_mandatory_crisis(
        Action("Blackmailer Identity", ellie_self_research_identity_requirement, "ellie_self_research_identity_label")
    )

def ellie_end_blackmail_requirement():
    return time_of_day == 4 and day % 7 == 3

def add_ellie_end_blackmail_action():
    mc.business.add_mandatory_crisis(
        Action("End Blackmail", ellie_end_blackmail_requirement, "ellie_end_blackmail_label")
    )

def ellie_work_welcome_requirement():
    return time_of_day == 1 and day % 7 == 4    # friday morning

def add_ellie_work_welcome_action():
    ellie.set_possessive_title("your IT girl")
    ellie.set_title(ellie.name)
    ellie.set_mc_title(mc.name)

    mc.business.set_event_day("hired_ellie_IT")
    mc.business.add_mandatory_crisis(
        Action("Hire Ellie", ellie_work_welcome_requirement, "ellie_work_welcome_label")
    )

def ellie_work_welcome_monday_requirement():
    return time_of_day == 1 and day % 7 == 0    # monday morning

def add_ellie_work_welcome_monday_action():
    mc.business.add_employee_research(ellie, start_day = Schedule.next_monday())
    ellie.set_override_schedule(None)   # make her free-roam
    mc.business.add_mandatory_crisis(
        Action("Review Ellie", ellie_work_welcome_monday_requirement, "ellie_work_welcome_monday_label")
    )
