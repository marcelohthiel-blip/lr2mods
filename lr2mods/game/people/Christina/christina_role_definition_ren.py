from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.game_logic.Action_ren import Action

time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def student_mom_appologise_requirement(person: Person):
    if time_of_day != 3:
        return False
    return person in person.home.people

def add_student_mom_apologize_action(person: Person):
    person.add_unique_on_room_enter_event(
        Action("Student_mom_appologise", student_mom_appologise_requirement, "student_mom_appologise_label", priority = 30)
    )
    person.event_triggers_dict["student_mom_door_kiss"] = 1
