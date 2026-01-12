from __future__ import annotations
from game.random_lists_ren import colour_white, colour_pink
from game.clothing_lists_ren import teddy, garter_with_fishnets, high_heels
from game.major_game_classes.game_logic.Room_ren import downtown_bar, mall
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, mc, camila
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def camila_get_a_drink_requirement(person: Person):
    if person.is_at(downtown_bar):
        if not mc.business.has_funds(20):
            return "Not enough money!"
        return True
    return False

def camila_go_dancing_requirement(person: Person):
    return False
    if person.is_at(downtown_bar) and person.event_triggers_dict.get("bathroom_sex", False):
        return True
    return False

def camila_take_pics_requirement(person: Person):
    return person.is_at(downtown_bar) and person.days_since_event("camila_blowjob_pic_day") > 0

def camila_home_sex_requirement(person: Person):
    if not person.event_triggers_dict.get("home_sex", False):
        return False
    if not person.is_home:
        return "Only at her house"
    if time_of_day != 4:
        return "Only at night when her husband is home"
    return person.is_home

def get_camila_role_action():
    camila_get_a_drink = Action("Get a drink {image=time_advance}", camila_get_a_drink_requirement, "camila_bar_date_wrapper_label", is_fast = False)
    camila_go_dancing = Action("Salsa Dancing", camila_go_dancing_requirement, "camila_go_dancing_label")
    camila_take_pics = Action("Take Sexy Pics {image=time_advance}", camila_take_pics_requirement, "camila_take_pics_label", is_fast = False)
    camila_home_sex = Action("Cuckold Visit {image=time_advance}", camila_home_sex_requirement, "camila_home_sex_label", is_fast = False)
    return [camila_get_a_drink, camila_go_dancing, camila_take_pics, camila_home_sex]

def init_camila_roles():
    global camila_role
    camila_role = Role(role_name ="Camila Bar", actions = get_camila_role_action(), hidden = True)
    global lifestyle_coach_role
    lifestyle_coach_role = Role(role_name ="Lifestyle Coach", actions = get_life_style_coach_actions(), hidden = True)

def lifestyle_coach_review_goals_requirement(person: Person):
    if not person.is_at(mall):
        return False
    if not mc.business.is_open_for_business:
        return "Only during business hours"
    return True

def lifestyle_coach_choose_sexy_goal_requirement(person: Person):
    return (
        person.sluttiness > 40
        and mc.energy > 80
        and person.energy > 80
        and person.is_at(mall)
    )

def get_life_style_coach_actions():
    lifestyle_coach_review_goals = Action("Review Goals", lifestyle_coach_review_goals_requirement, "lifestyle_coach_review_goals_label")
    return [lifestyle_coach_review_goals]

def camila_spot_at_bar_requirement(person: Person):
    return person.is_at(downtown_bar) and day > 5

def add_camila_spot_at_bar_action():
    camila.add_unique_on_room_enter_event(
        Action("Camila at the bar", camila_spot_at_bar_requirement, "camila_spot_at_bar_label", priority = 30)
    )

def get_camila_lingerie_set_white():
    outfit = Outfit("Lingerie Set Classic White")
    outfit.add_upper(teddy.get_copy(), colour_white)
    outfit.add_feet(garter_with_fishnets.get_copy(), colour_white)
    outfit.add_feet(high_heels.get_copy(), colour_white)
    return outfit

def get_camila_lingerie_set_pink():
    outfit = Outfit("Pink Lingerie")
    outfit.add_upper(teddy.get_copy(), colour_pink)
    outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
    outfit.add_feet(high_heels.get_copy(), colour_pink)
    return outfit
