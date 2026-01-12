from __future__ import annotations
from game.sex_positions.threesome.Threesome_Position_ren import willing_to_threesome
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import university
from game.major_game_classes.character_related.Person_ren import list_of_instantiation_functions, nora, stephanie, Person, mc

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("starbuck_rebecca_teamup_init")
list_of_lingerie_colors = ["the colour red", "the colour green", "the colour blue", "the colour black", "the colour white", "the colour pink", "the colour purple", "the colour orange", "the colour yellow", "the colour brown"]

def stephanie_nora_teamup_followup_requirement(the_person):
    if the_person.is_at_work:
        return True
    return False

def add_stephanie_nora_teamup_followup_action():
    stephanie.add_unique_on_room_enter_event(
        Action("Nora Training Followup", stephanie_nora_teamup_followup_requirement, "stephanie_nora_teamup_followup_label")
    )
    return

def stephanie_nora_teamup_revenge_followup_1_requirement():
    if time_of_day == 1 and day%7 < 5:
        return True
    return False

def add_stephanie_nora_teamup_revenge_followup_1_action():
    mc.business.add_mandatory_crisis(
        Action("Nora Training Agreement", stephanie_nora_teamup_revenge_followup_1_requirement, "stephanie_nora_teamup_revenge_followup_1_label")
    )
    return

