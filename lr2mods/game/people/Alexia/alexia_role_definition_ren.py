from __future__ import annotations
import renpy
from game.business_policies.organisation_policies_ren import public_advertising_license_policy
from game.major_game_classes.game_logic.Room_ren import downtown
from game.major_game_classes.character_related.Person_ren import Person, mc, alexia
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def alexia_ad_suggest_reintro_requirement(person: Person):
    if (not person.event_triggers_dict.get("camera_reintro_enabled", False)):
        return False
    if not mc.business.is_open_for_business \
            or not mc.is_at(mc.business.m_div) \
            or not person.is_at_office:
        return False
    if not mc.business.has_funds(500):
        return "Requires: $500"
    return True

def alexia_photography_intro_requirement(person: Person):
    if not mc.business.event_triggers_dict.get("has_expensive_camera", False):
        return False
    if not mc.is_at(mc.business.m_div) \
            or not mc.business.is_open_for_business \
            or not person.is_at_office:
        return False
    if time_of_day >= 4:
        return "Too late to shoot pictures"
    return True

def get_alexia_role_actions():
    #ALEXIA ACTIONS#
    alexia_ad_reintro = Action("Order photography equipment\n{menu_red}Costs: $500{/menu_red}", alexia_ad_suggest_reintro_requirement, "alexia_ad_suggest_reintro_label")
    alexia_ad_photo_intro = Action("Shoot pictures for business cards {image=time_advance}", alexia_photography_intro_requirement, "alexia_photography_intro_label")
    return [alexia_ad_reintro, alexia_ad_photo_intro]

def init_alexia_roles():
    global alexia_role
    alexia_role = Role("Alexia Model", get_alexia_role_actions(), hidden = True) #Hide her role because we don't want to display it.

def alexia_intro_phase_two_requirement(person: Person):
    return person.is_at_work

def alexia_hire_requirement(person: Person):
    if person.is_employee:
        return False
    if person.love < 10:
        return "Requires: 10 Love"
    if mc.business.at_employee_limit:
        return "At employee limit"
    return True

def camera_arrive_requirement(the_day: int):
    return day > the_day and mc.business.is_open_for_business

def alexia_ad_suggest_requirement(person: Person, the_day):
    if public_advertising_license_policy.is_owned or not day > the_day:
        return False
    if not mc.is_at_office or not mc.business.is_open_for_business or not person.is_at_office:
        return False
    return True

def ad_expire_requirement(the_day):
    return day > the_day

def create_add_space_and_expire_action(cost, multiplier):
    mc.business.change_funds(-cost, stat = "Marketing")
    mc.business.add_sales_multiplier("Ad Campaign", multiplier)
    mc.business.add_mandatory_morning_crisis(
        Action("Ad Expire", ad_expire_requirement, "ad_expire", args = multiplier, requirement_args = day + 7)
    ) #It'll expire in 7 days.
    mc.business.set_event_day("last_ad_campaign")

def add_alexia_phase_two_action(person: Person):
    alexia_intro_phase_two_action = Action("Have coffee together", alexia_intro_phase_two_requirement, "alexia_intro_phase_two_label")
    person.add_action(alexia_intro_phase_two_action)

def add_alexia_hire_action(person: Person):
    alexia.remove_action("alexia_intro_phase_two_label") #Clear the action from her actions list.
    alexia.set_schedule(downtown, day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3]) #She spends her time downtown "working".

    alexia_hire_action = Action(f"Hire {alexia.display_name} to work in sales", alexia_hire_requirement, "alexia_hire_label")
    person.add_action(alexia_hire_action) #NOTE: I think we can actually just modify the Role here, but we'll be double-sure.

def hire_alexia_and_add_to_company(person: Person):
    mc.business.add_employee_marketing(person)

    person.remove_action("alexia_hire_label") #Remove the hire action because this story event has played itself out.

    ad_suggest_event = Action("Ad Suggestion", alexia_ad_suggest_requirement, "alexia_ad_suggest_label", args = person, requirement_args = [person, day + renpy.random.randint(7, 12)])
    mc.business.add_mandatory_crisis(ad_suggest_event)

def add_camera_arrive_action(person: Person):
    camera_arrive_action = Action("Camera Arrive", camera_arrive_requirement, "alexia_ad_camera_label", args = person, requirement_args = day + renpy.random.randint(3, 7))
    mc.business.add_mandatory_crisis(camera_arrive_action)
    person.event_triggers_dict["camera_reintro_enabled"] = False
