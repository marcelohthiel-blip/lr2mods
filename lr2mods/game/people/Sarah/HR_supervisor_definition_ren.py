from __future__ import annotations
import renpy
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Action_ren import Action

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

def set_HR_director_tag(key: str, value):
    if mc.business.hr_director:
        mc.business.hr_director.HR_tags[key] = value

def get_HR_director_tag(key: str, default = None):
    if mc.business.hr_director:
        return mc.business.hr_director.HR_tags.get(key, default)
    return default

# used for unlocked sex positions
def set_HR_director_unlock(key: str, value: bool):
    if mc.business.hr_director:
        mc.business.hr_director.HR_unlocks[key] = value

# used for unlocked sex positions
def get_HR_director_unlock(key: str, default = False):
    if mc.business.hr_director:
        return mc.business.hr_director.HR_unlocks.get(key, default)
    return default

# get random unlocked sex position
def get_HR_director_random_unlock_key() -> str:
    if mc.business.hr_director:
        return get_random_from_list(mc.business.hr_director.HR_unlocks.keys(), "")
    return ""

# show menu choice for unlocked positions
def HR_director_choose_position():
    # HRUnlocks is dictionary of str, bool where the string is the unlocked hr position
    tuple_list = [(position.title(), position) for position, active in mc.business.hr_director.HR_unlocks.items() if active == True]
    tuple_list.append(("Surprise me", "any"))

    return renpy.display_menu(tuple_list, True, "Choice")

def HR_director_first_monday_requirement() -> bool:
    return day % 7 == 0 and time_of_day == 1 #Monday

def HR_director_monday_meeting_requirement() -> bool:
    if not mc.business.hr_director or not mc.business.hr_director.is_available:
        return False
    if mc.business.hr_director.days_since_event("hr_weekly_meeting") < 2:   #Prevent it from firing off multiple times on monday morning.
        return False
    return day % 7 == 0 and time_of_day == 1 #Monday

def HR_director_headhunt_interview_requirement() -> bool:
    if day < get_HR_director_tag("recruit_day"):
        return False
    if not mc.business.is_open_for_business:
        return False
    if time_of_day == 2:    # she talks with you at the end of the day instead of right after your meeting with her
        return True
    return False

def add_hr_director_first_monday_action(person: Person):
    HR_director_first_monday_action = Action("First Monday", HR_director_first_monday_requirement, "HR_director_first_monday_label", args = person)
    mc.business.add_mandatory_crisis(HR_director_first_monday_action)

def add_hr_director_monday_meeting_action(person: Person):
    HR_director_monday_meeting_action = Action("Monday HR Lunch", HR_director_monday_meeting_requirement, "HR_director_monday_meeting_label", args = person)
    mc.business.add_mandatory_crisis(HR_director_monday_meeting_action)

def add_hr_director_headhunt_interview_action(person: Person):
    HR_director_headhunt_interview_action = Action("Prospect Interview", HR_director_headhunt_interview_requirement, "HR_director_headhunt_interview_label", args = person)
    mc.business.add_mandatory_crisis(HR_director_headhunt_interview_action)
