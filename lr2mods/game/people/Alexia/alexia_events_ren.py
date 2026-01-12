from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, mc, alexia
from game.major_game_classes.game_logic.Action_ren import Action

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

def init_alexia_events():
    alexia.progress.lust_step = 1
    alexia.progress.obedience_step = 1
    alexia.story_event_log("obedience")
    alexia.story_event_log("slut")
    add_alexia_viral_marketing_action()
    add_alexia_company_propaganda_intro_action()


#### Love Events ####
def alexia_first_stream_requirement(person: Person):
    return False

def add_alexia_first_stream_action():
    alexia.add_unique_on_room_enter_event(
        Action("Alexia wants to stream", alexia_first_stream_requirement, "alexia_first_stream_label", priority = 30)
    )



#### Lust Events ####

def alexia_viral_marketing_requirement(person: Person):
    return False

# Story progression actions
def add_alexia_viral_marketing_action():
    alexia.add_unique_on_room_enter_event(
        Action("Alexia tries viral marketing", alexia_viral_marketing_requirement, "alexia_viral_marketing_label", priority = 30)
    )





#### Obedience Events ####

def alexia_company_propaganda_intro_requirement():
    return False

# Story progression actions
def add_alexia_company_propaganda_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Alexia tries viral marketing", alexia_company_propaganda_intro_requirement, "alexia_company_propaganda_intro_label")
    )
