from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, mc, iris, lily, mom
from game.major_game_classes.game_logic.Action_ren import Action


TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 12
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

def iris_schedule_backup_requirement():
    if lily.event_triggers_dict.get("oral_revisit_complete", False):
        if mom.event_triggers_dict.get("mom_office_slutty_level", 0) >= 2 or mom.is_employee:
            return True
    return False

def add_iris_schedule_backup_action():
    mc.business.add_mandatory_crisis(
        Action("Iris schedule backup", iris_schedule_backup_requirement, "iris_schedule_backup_label")
    )
