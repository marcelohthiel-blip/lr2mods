from __future__ import annotations
from game.people.Ophelia.ophelia_role_definition_ren import ophelia_get_ex_name, ophelia_get_will_help_candace
from game.business_policies.clothing_policies_ren import reduced_coverage_uniform_policy
from game.personality_types._personality_definitions_ren import bimbo_personality
from game.major_game_classes.character_related.Person_ren import Person, mc, candace, police_chief
from game.major_game_classes.game_logic.Room_ren import office_store
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.people.Ellie.IT_Business_Projects_ren import supply_storage_project

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def candace_convince_to_quit_requirement(person: Person):
    if candace_get_can_convince_to_quit() and ophelia_get_will_help_candace():
        if mc.business.at_employee_limit:
            return "At employee limit"
        if not candace_get_has_quit_job():
            return True
    return False

def candace_get_to_know_requirement(person: Person):
    if candace_get_has_quit_job():
        return False
    if not candace_can_talk():
        return "Already talked today"
    return True

def get_candace_role_actions():
    candace_get_to_know = Action("Get to know her {image=time_advance}", candace_get_to_know_requirement, "candace_get_to_know_label", menu_tooltip = "Find out more about Candi")
    candace_convince_to_quit = Action("Convince her to quit", candace_convince_to_quit_requirement, "candace_convince_to_quit_label", menu_tooltip = "Quit her current job and join your company.")

    return [candace_get_to_know, candace_convince_to_quit]

def init_candace_roles():
    global candace_role
    candace_role = Role(role_name ="It\'s Complicated", actions = get_candace_role_actions(), hidden = True)

def candace_meet_at_office_store_requirement(person: Person):
    return mc.business.is_work_day and person.is_at(office_store)

def make_candace_free_roam_and_set_intro_event():
    candace.SO_name = ophelia_get_ex_name()
    # Buying office supplies for her employer, so clear override and set job schedule
    candace.set_override_schedule(None, day_slots = [0, 1, 2, 3, 4], time_slots = [3])
    candace.primary_job.set_schedule(office_store, day_slots = [0, 1, 2, 3, 4], time_slots = [3])
    candace.add_unique_on_room_enter_event(
        Action("Meet Candi", candace_meet_at_office_store_requirement, "candace_meet_at_office_store_label", priority = 30)
    )

def candace_check_police_chief_met():
    if police_chief.is_stranger:  # haven't met, set title
        police_chief.set_possessive_title("the police chief")
        police_chief.set_mc_title("Mr. " + mc.last_name)
        police_chief.set_title("Officer " + police_chief.last_name)
        police_chief.set_event_day("day_met")

def candace_increase_doubt():
    score = candace.event_triggers_dict.get("relationship_doubt_score", 0)
    candace.event_triggers_dict["relationship_doubt_score"] = score + 1

def candace_get_has_gone_clothes_shopping() -> bool:
    return candace.event_triggers_dict.get("clothes_shopping", 0) != 0

def candace_is_giving_supply_discount() -> bool:
    if candace.is_employee:
        return candace.event_triggers_dict.get("supply_discount", False)
    return False

def candace_calculate_discount():
    disc_mult = 1.0
    if candace_is_giving_supply_discount():
        if candace.personality == bimbo_personality:
            disc_mult = 0.90
        else:
            disc_mult = 0.80
    if mc.business.IT_project_is_active(supply_storage_project):
        disc_mult -= 0.05
    return disc_mult

def unlock_anti_bimbo_serum(): # unlock the serum by setting the tier to 3 (instead of 99)
    if found := next((x for x in list_of_traits if x.name == "Bimbo Reversal"), None):
        found.tier = 3

def candace_get_ready_to_quit():
    return candace.event_triggers_dict.get("relationship_doubt_score", 0) >= 5

def candace_get_learned_about_unhappy():
    return candace.event_triggers_dict.get("learned_about_unhappy", 0)

def candace_get_learned_about_bf_control():
    return candace.event_triggers_dict.get("learned_about_bf_control", 0)

def candace_get_learned_about_previous_work():
    return candace.event_triggers_dict.get("learned_about_previous_work", 0)

def candace_get_learned_about_uniform():
    return candace.event_triggers_dict.get("learned_about_uniform", 0)

def candace_get_learned_about_pay():
    return candace.event_triggers_dict.get("learned_about_pay", 0)

def candace_get_employees_have_lax_uniforms():
    return reduced_coverage_uniform_policy.is_active

def candace_get_mc_is_sexually_skilled():
    #Average of 4 or better across sex skills.
    return sum(value for key, value in mc.sex_skills.items()) > 16

def candace_get_can_convince_to_quit():
    if candace_get_ready_to_quit():
        if candace_get_learned_about_pay() and candace_get_learned_about_previous_work() and candace_get_learned_about_uniform() and candace_get_learned_about_bf_control():
            if candace_get_employees_have_lax_uniforms() or candace_get_mc_is_sexually_skilled():
                return True
    return False

def candace_get_has_quit_job():
    return candace.event_triggers_dict.get("quit_job", 0) != 0

def candace_can_talk():
    return candace.event_triggers_dict.get("last_talk_day", 0) < day
