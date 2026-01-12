from __future__ import annotations
from game.game_roles._role_definitions_ren import offer_to_hire_requirement
from game.business_policies.organisation_policies_ren import attention_floor_increase_2_policy, attention_bleed_increase_2_policy
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Trainable_ren import Trainable
from game.major_game_classes.character_related.Person_ren import Person, mc, city_rep
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.people.Sarah.HR_supervisor_definition_ren import HR_director_monday_meeting_requirement

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def city_rep_negotiate_requirement(person: Person):
    if not person.event_triggers_dict.get("currently_interrogating", False) or attention_floor_increase_2_policy.is_owned:
        return False
    return True

def city_rep_bribe_requirement(person: Person):
    if not person.event_triggers_dict.get("currently_interrogating", False):
        return False
    return not has_bribe_attempt("cash_bribe")

def city_rep_seduce_requirement(person: Person):
    if not person.event_triggers_dict.get("currently_interrogating", False):
        return False
    return not has_bribe_attempt("seduction_attempted")

def city_rep_order_requirement(person: Person):
    if not person.event_triggers_dict.get("currently_interrogating", False):
        return False
    return not has_bribe_attempt("order_attempted")


def get_city_rep_role_actions():
    city_rep_negotiate_action = Action("Negotiate Deal", city_rep_negotiate_requirement, "city_rep_negotiate", priority = 30)
    city_rep_bribe_action = Action("Offer a Bribe", city_rep_bribe_requirement, "city_rep_bribe", priority = 30)
    city_rep_order_action = Action("Order her to leave", city_rep_order_requirement, "city_rep_order", priority = 30)
    city_rep_seduce_action = Action("Try to seduce her", city_rep_seduce_requirement, "city_rep_seduce", priority = 40)
    city_rep_hire_action = Action("Offer to hire her at [mc.business.name]", offer_to_hire_requirement, "city_rep_offer_hire", priority = 30)
    return [city_rep_negotiate_action, city_rep_bribe_action, city_rep_order_action, city_rep_seduce_action, city_rep_hire_action]

def city_rep_dressup_training_requirement(person: Person):
    if not person.is_at_work:
        return False
    if person.known_opinion.skimpy_uniforms > 0:
        return True
    return "Likes Skimpy Uniforms"

def city_rep_penalty_reduction_training_requirement(person: Person):
    if not person.is_at_work:
        return False
    if person.event_triggers_dict.get("city_rep_reduced_penalties_trained", False):
        return False
    if person.known_opinion.being_submissive < 1:
        return "Likes being submissive"
    return True

def city_rep_internal_sabotage_training_requirement(person: Person):
    if not person.is_at_work:
        return False
    if attention_bleed_increase_2_policy.is_owned:
        return False
    if person.known_opinion.being_submissive < 2 or person.obedience < 120:
        return "Loves being submissive, 120+ Obedience"
    return True

def get_city_rep_role_trainables():
    city_rep_dressup_training = Trainable("City_Rep_Dressup", "city_rep_dressup_training", "Slutty Work Uniform.", unlocked_function = city_rep_dressup_training_requirement, doubling_amount = 4)
    city_rep_penalty_reduction_training = Trainable("City_Rep_Pen_Reduct", "city_rep_penalty_reduction_training", "Reduce Penalty Severity", 200, city_rep_penalty_reduction_training_requirement)
    city_rep_internal_sabotage_training = Trainable("City_Rep_Sabot", "city_rep_internal_sabotage_training", "Sabotage Investigations", 400, city_rep_internal_sabotage_training_requirement)
    return [city_rep_dressup_training, city_rep_penalty_reduction_training, city_rep_internal_sabotage_training]

def add_bribe_attempt(attempt):
    if "bribe_attempts" not in city_rep.event_triggers_dict:
        city_rep.event_triggers_dict["bribe_attempts"] = [attempt]
        return
    city_rep.event_triggers_dict["bribe_attempts"].append(attempt)

def has_bribe_attempt(attempt):
    if "bribe_attempts" not in city_rep.event_triggers_dict:
        return False
    return attempt in city_rep.event_triggers_dict["bribe_attempts"]

def clear_bribe_attempts():
    if "bribe_attempts" not in city_rep.event_triggers_dict:
        return
    del city_rep.event_triggers_dict["bribe_attempts"]

def city_rep_outfit_check(outfit: Outfit, outfit_type = "full"):
    return outfit.is_legal_in_public

def city_rep_advocates_topless_requirement(person: Person, min_day: int):
    return day > min_day

def add_city_rep_advocates_topless_is_legal():
    if mc.business.topless_is_legal:
        return False
    if city_rep.event_triggers_dict.get("discussed_topless_is_legal", False):
        return False
    if city_rep.has_queued_event("city_rep_discuss_topless_is_legal"):
        return False

    city_rep.add_unique_on_room_enter_event(
        Action("City Rep discuss topless status", city_rep_advocates_topless_requirement, "city_rep_discuss_topless_is_legal", requirement_args = day + 10, priority = 30)
    )

####################
# Attention Events #
####################

def attention_fine_requirement(person: Person):
    return True

def attention_seize_inventory_requirement(person: Person):
    return mc.business.inventory.total_serum_count >= 10

def attention_seize_supplies_requirement(person: Person):
    return mc.business.supply_count >= 200

def attention_seize_research_requirement(person: Person):
    return any(x for x in mc.business.serum_designs if x.researched)

def attention_illegal_serum_requirement(person: Person):
    return any(x for x in mc.business.serum_designs if x.researched)

def attention_pick_current_event():
    attention_fine_action = Action("attention_fine", attention_fine_requirement, "attention_pay_fine")
    attention_seize_inventory_action = Action("attention_seize_inventory", attention_seize_inventory_requirement, "attention_seize_inventory")
    attention_seize_supplies_action = Action("attention_seize_supplies", attention_seize_supplies_requirement, "attention_seize_supplies")
    attention_seize_research_action = Action("attention_seize_research", attention_seize_research_requirement, "attention_seize_research")
    attention_illegal_serum_action = Action("attention_illegal_serum", attention_illegal_serum_requirement, "attention_illegal_serum")

    attention_events = [attention_fine_action, attention_seize_inventory_action, attention_seize_supplies_action, attention_seize_research_action, attention_illegal_serum_action]

    return get_random_from_list([x for x in attention_events if x.is_action_enabled(city_rep)])

def attention_event_requirement():
    if HR_director_monday_meeting_requirement():
        return False
    return mc.business.is_work_day and time_of_day == 1

def add_attention_event():
    mc.business.add_mandatory_crisis(
        Action("attention_event", attention_event_requirement, "attention_event")
    )


def get_highest_attention_serum_design_from_inventory():
    inventories = [mc.business.inventory]
    for contract in mc.business.active_contracts:
        inventories.append(contract.inventory)

    selected_design = None
    for inventory in inventories:
        for design in inventory.get_serum_types:
            if selected_design is None \
                    or design.attention > selected_design.attention \
                    or design.trait_count > selected_design.trait_count:
                if inventory.get_serum_count(design) > 10:  # if less than 10 items they won't find it
                    selected_design = design
    return selected_design

def seize_doses_from_inventory(target_design):
    total_seized = 0
    inventories = [mc.business.inventory]
    for contract in mc.business.active_contracts:
        inventories.append(contract.inventory)

    for inventory in inventories:
        design_list = inventory.get_serum_types
        for design in design_list:
            if design.name == target_design.name:
                if city_rep.event_triggers_dict.get("city_rep_reduced_penalties_trained", False):
                    amount = inventory.get_serum_count(design) // 2
                else:
                    amount = inventory.get_serum_count(design)

                inventory.change_serum(design, -amount)
                total_seized += amount

    return total_seized

def city_rep_first_visit_unlock(person: Person):
    person.set_title(f"Ms. {person.last_name}")
    person.set_mc_title(f"Mr. {mc.last_name}")
    person.set_possessive_title("your annoyance")
    person.set_override_schedule(None) # free roam on non-working (saturday evening / sunday)

def get_highest_attention_serum_design():
    highest_attention_design = None
    for design in [x for x in mc.business.serum_designs if x.researched]:
        if highest_attention_design is None or design.attention > highest_attention_design.attention:
            highest_attention_design = design
    return highest_attention_design
