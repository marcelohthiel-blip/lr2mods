from __future__ import annotations
from game.business_policies.clothing_policies_ren import strict_uniform_policy
from game.business_policies.organisation_policies_ren import public_advertising_license_policy
from game.business_policies.serum_policies_ren import daily_serum_dosage_policy
from game.business_policies.special_policies_ren import personal_secretary_creation_policy, production_assistant_creation_policy, it_director_creation_policy
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
def manage_contracts_requirement():
    if len(mc.business.active_contracts) == 0 and len(mc.business.offered_contracts) == 0:
        return "No contracts available"
    return True

def interview_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.at_employee_limit:
        return "At employee limit"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def policy_purchase_requirement():
    return True

def set_uniform_requirement():
    return strict_uniform_policy.is_active

def set_serum_requirement():
    if daily_serum_dosage_policy.is_owned and not daily_serum_dosage_policy.is_active:
        return "Policy not active"
    return daily_serum_dosage_policy.is_active

def head_researcher_select_requirement():
    if isinstance(mc.business.head_researcher, Person):
        return False
    if len(mc.business.research_team) == 0:
        return "Nobody to pick"
    return True

def pick_personal_secretary_requirement():
    if mc.business.personal_secretary is not None:
        return False
    if not personal_secretary_creation_policy.is_active:
        return False
    if len(mc.business.hr_team) == 0 or (mc.business.hr_director and len(mc.business.hr_team) == 1):
        return "Nobody to pick"
    return True

def pick_production_assistant_requirement():
    if mc.business.prod_assistant is not None:
        return False
    if not production_assistant_creation_policy.is_active:
        return False
    if len(mc.business.production_team) == 0:
        return "Nobody to pick"
    return True

def pick_it_director_requirement():
    if mc.business.it_director is not None:
        return False
    if not it_director_creation_policy.is_active:
        return False
    if len(mc.business.research_team) == 0 or (mc.business.head_researcher is not None and len(mc.business.research_team) == 1):
        return "Nobody to pick"
    return True

def ceo_office_actions() -> list[Action]:
    manage_contracts = Action("Manage Contracts", manage_contracts_requirement, "manage_contracts_action_description",
        menu_tooltip = "Accept and complete contracts, and check the current market prices.")

    interview_action = Action("Hire someone new {image=time_advance}", interview_action_requirement, "interview_action_description",
        menu_tooltip = "Look through the resumes of several candidates. More information about a candidate can be revealed by purchasing new business policies.")

    policy_purchase_action = Action("Manage business policies", policy_purchase_requirement, "policy_purchase_description",
        menu_tooltip = "New business policies changes the way your company runs and expands your control over it. Once purchased business policies are always active.")

    set_head_researcher_action = Action("Pick a Head Researcher", head_researcher_select_requirement, "head_researcher_select_description",
        menu_tooltip = "Pick a member of your R&D staff to be your head researcher. A head researcher with a high intelligence score will increase the amount of research produced by the entire division.")

    set_personal_secretary_action = Action("Pick a personal secretary", pick_personal_secretary_requirement, "personal_secretary_select_description",
        menu_tooltip = "Pick one your employees to be your personal secretary. She will contribute to HR but be stationed at the entry to your office.")

    set_it_director_action = Action("Pick an IT Director", pick_it_director_requirement, "it_director_select_description",
        menu_tooltip = "Pick one your employees to be your IT Director. She will contribute to Research while also accomplishing IT work.")

    set_production_assistant_action = Action("Pick a production assistant", pick_production_assistant_requirement, "production_assistant_select_description",
        menu_tooltip = "Pick one your employees to be your production assistant. She will contribute to production but will also produce serums for your personal use.")

    ##Actions unlocked by policies##
    set_serum_action = Action("Set Daily Serum Doses", set_serum_requirement, "set_serum_description")
    set_uniform_action = Action("Manage Employee Uniforms", set_uniform_requirement, "uniform_manager_loop")

    return [manage_contracts, interview_action, policy_purchase_action, set_uniform_action, set_serum_action, set_head_researcher_action, set_personal_secretary_action, set_it_director_action, set_production_assistant_action]


def sell_serum_action_requirement():
    return True

def market_work_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def pick_company_model_requirement():
    if isinstance(mc.business.company_model, Person):
        return False
    if not public_advertising_license_policy.is_active:
        return False
    if len(mc.business.market_team) == 0:
        return "Nobody to pick"
    return True

def market_division_actions() -> list[Action]:
    sell_serum_action = Action("Sell Serum", sell_serum_action_requirement, "sell_serum_action_description",
        menu_tooltip = "Review your current stock of serum and check the current market prices.")

    market_work_action = Action("Find new clients {image=time_advance}", market_work_action_requirement, "market_work_action_description",
        menu_tooltip = "Find new clients who may be interested in buying serum from you, increasing your Market reach. Important for maintaining good Aspect prices.\n+(3*Charisma + 2*Skill + 1*Focus + 20) Market Reach.")

    set_company_model_action = Action("Pick a company model", pick_company_model_requirement, "pick_company_model_description",
        menu_tooltip = "Pick one your employees to be your company model. You can run ad campaigns with your model, increasing the value of every dose of serum sold.")

    return [sell_serum_action, market_work_action, set_company_model_action]


def hr_work_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def supplies_work_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def pick_supply_goal_action_requirement():
    return True

def main_office_actions() -> list[Action]:
    hr_work_action = Action("Organize your business {image=time_advance}", hr_work_action_requirement, "hr_work_action_description",
        menu_tooltip = "Raise business efficiency, which drops over time based on how many employees the business has.\n+(3*Charisma + 2*Skill + Intelligence + 15) divided by 5 is Efficiency % Increase.")

    supplies_work_action = Action("Order Supplies {image=time_advance}", supplies_work_action_requirement, "supplies_work_action_description",
        menu_tooltip = "Purchase serum supply at the cost of $1 per unit of supplies. When producing serum every production point requires one unit of serum.\n+(5*Focus + 3*Skill + 3*Charisma + 20) Serum Supply.")

    pick_supply_goal_action = Action("Set the amount of supplies you would like to maintain", pick_supply_goal_action_requirement, "pick_supply_goal_action_description",
        menu_tooltip = "Set the maximum amount of supplies you and your staff will attempt to purchase.")

    return [hr_work_action, supplies_work_action, pick_supply_goal_action]


def research_work_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.active_research_design is None:
        return "No research project set"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def serum_design_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def research_select_action_requirement():
    return True

def review_designs_action_requirement():
    return True


def research_division_actions() -> list[Action]:
    research_work_action = Action("Research in the lab {image=time_advance}", research_work_action_requirement, "research_work_action_description",
        menu_tooltip = "Contribute research points towards the currently selected project.\n+(3*Intelligence + 2*Skill + 1*Focus + 10) Research Points.")

    design_serum_action = Action("Design new serum {image=time_advance}", serum_design_action_requirement, "serum_design_action_description",
        menu_tooltip = "Combine serum traits to create a new design. Once a design has been created it must be researched before it can be put into production.")

    pick_research_action = Action("Assign Research Project", research_select_action_requirement, "research_select_action_description",
        menu_tooltip = "Pick the next research topic for your R&D division. Serum designs must be researched before they can be put into production.")

    review_designs_action = Action("Review serum designs", review_designs_action_requirement, "review_designs_action_description",
        menu_tooltip = "Shows all existing serum designs and allows you to delete any you no longer desire.")

    return [research_work_action, design_serum_action, pick_research_action, review_designs_action]


def production_work_action_requirement():
    if time_of_day >= 4:
        return "Too late to work"
    elif mc.business.used_line_weight == 0:
        return "No serum design set"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    elif mc.has_date_now:
        return "You have other things on your schedule"
    return True

def production_select_action_requirement():
    return True

def trade_serum_action_requirement():
    return True

def production_division_actions() -> list[Action]:
    production_work_action = Action("Produce serum {image=time_advance}", production_work_action_requirement, "production_work_action_description",
        menu_tooltip = "Produce serum from raw materials. Each production point of serum requires one unit if supply, which can be purchased from your office.\n+(3*Focus + 2*Skill + 1*Intelligence + 10) Production Points.")

    pick_production_action = Action("Set production settings", production_select_action_requirement, "production_select_action_description",
        menu_tooltip = "Decide what serum designs are being produced. Production is divided between multiple factory lines, and automatic sell thresholds can be set to automatically flag serum for sale.")

    trade_serum_action = Action("Access production stockpile", trade_serum_action_requirement, "trade_serum_action_description",
        menu_tooltip = "Move serum to and from your personal inventory. You can only use serum you are carrying with you.")

    return [production_work_action, pick_production_action, trade_serum_action]

# These actions have been removed so storylines are followed

# def mc_breakthrough_requirement(new_level, clarity_cost):
#     if mc.business.research_tier+1 != new_level:
#         return False
#     if sum(1 for x in list_of_traits if x.tier == mc.business.research_tier and x.researched) < 5:
#         return f"Research 4 traits on Tier {mc.business.research_tier}"
#     elif clarity_cost > mc.free_clarity:
#         return "Not enough Clarity"
#     elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
#         return "Finish tutorial first"
#     elif time_of_day >= 4:
#         return "Too late to work"
#     return True

# def unassigned_actions() -> list[Action]:
#     ##Breakthrough Actions##
#     mc_breakthrough_1 = Action("Have a Breakthrough {image=time_advance}\n{menu_red}Requires: 500 Clarity{/menu_red}", mc_breakthrough_requirement, "mc_research_breakthrough", args = [1, 500], requirement_args = [1, 500],
#         menu_tooltip = "Put your intellect to work and unlock a new tier of research! There may be other ways to achieve this breakthrough as well", priority = 100)
#     mc_breakthrough_2 = Action("Have a Breakthrough {image=time_advance}\n{menu_red}Requires: 5000 Clarity{/menu_red}", mc_breakthrough_requirement, "mc_research_breakthrough", args = [2, 5000], requirement_args = [2, 5000],
#         menu_tooltip = "Put your intellect to work and unlock a new tier of research! There may be other ways to achieve this breakthrough as well", priority = 100)
#     mc_breakthrough_3 = Action("Have a Breakthrough {image=time_advance}\n{menu_red}Requires: 25000 Clarity{/menu_red}", mc_breakthrough_requirement, "mc_research_breakthrough", args = [3, 25000], requirement_args = [3, 25000],
#         menu_tooltip = "Put your intellect to work and unlock a new tier of research! There may be other ways to achieve this breakthrough as well", priority = 100)
#     return
