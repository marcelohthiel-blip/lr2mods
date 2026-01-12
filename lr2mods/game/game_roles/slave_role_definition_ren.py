from __future__ import annotations
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Action_ren import Action
from game.game_roles._role_definitions_ren import slave_role
from game.clothing_lists_ren import breed_collar

day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

def wakeup_duty_crisis_requirement():
    return day % 7 != 5 # not on saturday mornings

def slave_assign_new_collar(person: Person, collar: Clothing | str):
    person.outfit.remove_all_collars()

    if collar == "Simple Collar":
        new_collar = breed_collar.get_copy()
        new_collar.colour = [.1, .1, .1, .8]
        new_collar.colour_pattern = [.1, .1, .1, .8]
    else:
        new_collar = collar.get_copy()
        new_collar.colour = [.1, .1, .1, .8]

        if "Two Tone" in new_collar.supported_patterns:
            new_collar.pattern = new_collar.supported_patterns["Two Tone"]
            new_collar.colour_pattern = [.95, .95, .95, .9]

    person.base_outfit.add_accessory(new_collar)

    person.slave_collar = True
    person.apply_planned_outfit()
    person.draw_person()

def slave_remove_collar(person: Person):
    person.slave_collar = False
    person.outfit.remove_all_collars()
    person.base_outfit.remove_all_collars()
    person.draw_person()

def slave_release_slave(person: Person):
    slave_remove_collar(person)
    person.remove_role(slave_role)
    person.stay_wet = False
    # she is not happy and will reset her obedience to 100
    person.change_stats(love = -20, happiness = -20, obedience = 100 - person.obedience)
    # she loses her submissive trait
    person.update_opinion_with_score("being submissive", 0)

def slave_add_wakeup_duty_action(person):
    mc.business.remove_mandatory_crisis("slave_alarm_clock_label")
    wakeup_duty_crisis.args = [person]
    mc.business.add_mandatory_morning_crisis(wakeup_duty_crisis)

wakeup_duty_crisis = Action("Slave Alarm Clock", wakeup_duty_crisis_requirement, "slave_alarm_clock_label")
