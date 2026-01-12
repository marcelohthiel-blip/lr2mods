from __future__ import annotations
from game.major_game_classes.game_logic.Room_ren import university
from game.major_game_classes.character_related.Person_ren import Person, mc, emily
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.map.MapHub_ren import university_hub

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def student_reintro_requirement(person: Person):
    return person.event_triggers_dict.get("student_reintro_required", False)

def student_study_propose_requirement(person: Person):
    if not person.event_triggers_dict.get("tutor_enabled", False):
        return False
    if not (person.is_at(university_hub)
            or (person.is_home and person.event_triggers_dict.get("home_tutor_enabled", False))):
        return False
    if person.get_event_day("last_tutor") == day:
        return "Already studied today"
    if time_of_day == 4:
        return "Too late to study"
    return True

def student_test_intro_requirement(person: Person):
    return person.event_triggers_dict.get("test_rewrite_intro_enabled", False)

def student_test_requirement(person: Person):
    if not person.event_triggers_dict.get("student_exam_rewrite_enabled", False):
        return False
    if day % 7 in (5, 6):
        return "Closed on the weekend"
    if time_of_day == 4:
        return "Too late to start the exam"
    if not person.is_at(university):
        return "Wait until she's on campus"
    return True

def student_offer_job_requirement(person: Person):
    if not person.event_triggers_dict.get("student_offer_job_enabled", False):
        return False
    if mc.business.at_employee_limit:
        return "At employee limit"
    return True

def get_student_role_actions():
    #STUDENT ACTIONS#
    student_reintro_action = Action("Ask about tutoring her", student_reintro_requirement, "student_reintro")
    student_study_propose_action = Action("Tutor her {image=time_advance}", student_study_propose_requirement, "student_study_propose")
    student_test_intro_action = Action("Tell her she can rewrite her exam", student_test_intro_requirement, "student_test_intro")
    student_test_action = Action("Time to rewrite her exam {image=time_advance}", student_test_requirement, "student_test")
    student_offer_job_reintro_action = Action("Offer her a job", student_offer_job_requirement, "student_offer_job_reintro")
    return [student_reintro_action, student_study_propose_action, student_test_intro_action, student_test_action, student_offer_job_reintro_action]

def init_emily_roles():
    global student_role
    student_role = Role("Tutee", get_student_role_actions())

def student_intro_two_requirement(person: Person):
    return (
        person in university.people
        and person.story_event_ready("love")
    )

def add_student_intro_two_action(person: Person):
    person.add_unique_on_room_enter_event(
        Action("Student_intro_two", student_intro_two_requirement, "student_intro_two", priority = 30)
    )
    person.event_triggers_dict["current_marks"] = 35 # Should be a value between 0 and 100%
    person.story_event_log("love")
    person.set_override_schedule(None) # make her free_roam

def unlock_emily_tutoring():
    emily.event_triggers_dict["tutor_enabled"] = True
    emily.event_triggers_dict["student_reintro_required"] = False
    emily.set_event_day("obedience_event")
    emily.set_event_day("love_event")
    emily.set_event_day("slut_event")
    emily.set_event_day("story_event")
    emily.set_schedule(emily.home, day_slots=[0, 1, 2, 3, 6], time_slots = [3]) # she's guaranteed home on certain days for tuturing
    emily.progress.love_step = 0
    emily.progress.obedience_step = 0
    emily.progress.lust_step = 0
    emily.add_role(student_role) # tutor actions
    # these currently do nothing but should be hooked up here and moved to _ren.py file
    add_emily_ask_about_serum_action()
    add_emily_university_lunch_action()


def student_mom_intro_requirement(person: Person):
    if not emily.event_triggers_dict.get("home_tutor_enabled", False):
        return False
    return person in person.home.people and time_of_day in (2, 3)

def add_student_mom_intro_action(person: Person):
    person.add_unique_on_room_enter_event(
        Action("Student_Mom_Intro", student_mom_intro_requirement, "student_mom_intro", priority = 30)
    ) #christina
