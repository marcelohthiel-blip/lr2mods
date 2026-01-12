from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, ellie

time_of_day = 0
TIER_2_TIME_DELAY = 12
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

def IT_project_completed_requirement():
    return mc.business.it_director and mc.business.is_open_for_business and mc.is_at_office

def set_IT_director_tag(key, value):
    if mc.business.it_director:
        mc.business.it_director.IT_tags[key] = value

def get_IT_director_tag(key, default = None):
    if mc.business.it_director:
        return mc.business.it_director.IT_tags.get(key, default)
    return default

def IT_director_nanobot_intro_requirement(person: Person):
    return mc.is_at_office

def add_IT_director_nanobot_intro_action():
    if not mc.business.it_director:
        return  # make sure we have an it_director
    mc.business.it_director.add_unique_on_talk_event(
        Action("Nanobot Programs", IT_director_nanobot_intro_requirement, "IT_director_nanobot_intro_label", priority = 30)
    )
    mc.business.event_triggers_dict["fetish_to_IT"] = True

def IT_director_teamup_start_requirement():
    if mc.is_at_office and mc.business.it_director and mc.business.is_open_for_business:
        return mc.business.days_since_event("IT_dir_nanobot_takeover_day") >= TIER_2_TIME_DELAY
    return False

def add_IT_director_teamup_start_action():
    mc.business.set_event_day("IT_dir_nanobot_takeover_day")
    mc.business.add_mandatory_crisis(
        Action("IT and RnD Teamup Intro", IT_director_teamup_start_requirement, "IT_director_teamup_start_label")
    )

def add_IT_Project_completed_action(project):
    mc.business.add_mandatory_crisis(
        Action("IT Project Complete", IT_project_completed_requirement, "IT_project_complete_label", args = project)
    )

def nanobot_program_is_IT():
    return mc.business.event_triggers_dict.get("fetish_to_IT", False)

def it_director_alt_intro_requirement():
    return (mc.is_at_office and time_of_day > 1)

def add_it_director_alt_intro_action():
    mc.business.add_mandatory_crisis(
        Action("IT Director Alt Intro", it_director_alt_intro_requirement, "it_director_alt_intro_label")
    )
