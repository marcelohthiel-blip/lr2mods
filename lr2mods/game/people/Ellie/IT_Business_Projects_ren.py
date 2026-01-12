from __future__ import annotations
import builtins
import renpy
from game.business_policies.clothing_policies_ren import male_focused_marketing_policy
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, mc
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait
from game.people.Ellie.IT_Project_class_ren import IT_Project

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
def hr_organized_chaos_project_requirement():
    if mc.business.hr_director:
        return True
    return "Requires HR Director"

def hr_task_manager_project_requirement():
    if len(mc.business.hr_team) >= 3:
        return True
    return "Requires 3 HR employees"

def serum_creation_crisis_requirement():
    # only when mc is at office or any researchers at office
    return (
        mc.is_at_office
        or mc.business.r_div.person_count > 0
    )

def hr_hack_cell_tower_requirement():
    return True

def supply_inventory_project_requirement():
    return True

def supply_storage_project_requirement():
    if len(mc.business.supply_team) >= 3:
        return True
    return "Requires 3 supply employees"

def market_photo_filter_project_requirement():
    if mc.business.company_model:
        return True
    return "Requires Company Model"

def market_targeted_advertising_project_requirement():
    if mc.business.company_model:
        return True
    return "Requires Company Model"

def research_peerless_review_project_requirement():
    return True

def research_group_discovery_project_requirement():
    return "!! Not Implemented !!"

def research_team_building_project_requirement():
    if len(mc.business.research_team) >= 3:
        return True
    return "Requires 3 research employees"

def production_assembly_line_project_requirement():
    return True

def production_equipment_selftest_project_requirement():
    if len(mc.business.production_team) >= 3:
        return True
    return "Requires 3 production employees"

def hr_organized_chaos_project_on_apply():
    mc.business.event_triggers_dict["HR_eff_bonus"] = mc.business.event_triggers_dict.get("HR_eff_bonus", 0) + 5

def hr_organized_chaos_project_on_remove():
    mc.business.event_triggers_dict["HR_eff_bonus"] = mc.business.event_triggers_dict.get("HR_eff_bonus", 0) - 5

def hr_hack_cell_tower_project_on_apply():
    mc.business.event_triggers_dict["gps_tracker_enabled"] = True

def market_photo_filter_project_on_apply():
    mc.business.add_sales_multiplier("Photo Filters", 1.05)

def market_photo_filter_project_on_remove():
    mc.business.remove_sales_multiplier("Photo Filters", 1.05)

def production_equipment_selftest_project_on_day():
    if not mc.business.is_weekend:
        for person in mc.business.production_team:
            person.change_happiness(1, add_to_log = False)

def market_targeted_advertising_project_on_turn():
    if not mc.business.is_open_for_business:
        return 0

    extra_amount = 0
    for person in (x for x in mc.business.market_team if x.is_at_office):
        if person.should_wear_uniform and male_focused_marketing_policy.is_active:
            amount_increased = builtins.int((3 * person.charisma) + (person.focus) + (2 * person.market_skill)) * (mc.business.team_effectiveness * 0.01) * (1.0 + (person.outfit.outfit_slut_score / 100.0)) * 5.0
        else:
            amount_increased = builtins.int((3 * person.charisma) + (person.focus) + (2 * person.market_skill)) * (mc.business.team_effectiveness * 0.01) * 5.0
        extra_amount += (amount_increased * .1)

    mc.business.market_reach += extra_amount
    return extra_amount

def research_peerless_review_project_on_turn():
    if not mc.business.is_open_for_business:
        return 0
    research_inc = 0
    for person in mc.business.research_team:
        research_inc += person.research_potential
    research_amount = builtins.round(research_inc * 0.05 * (mc.business.team_effectiveness / 100.0))

    if mc.business.active_research_design is not None:
        the_research = mc.business.active_research_design
        is_researched = the_research.researched # If it was researched before we added any research then we are increasing the mastery level of a trait (does nothing to serum designs)
        mc.business.research_produced += research_amount
        if the_research.add_research(research_amount): #Returns true if the research is completed by this amount'
            if isinstance(the_research, SerumDesign):
                side_effects = the_research.generate_side_effects() #The serum will generate any side effects that are needed.
                mc.business.add_mandatory_crisis(Action("Research Finished Crisis", serum_creation_crisis_requirement, "serum_creation_crisis_label", args = [the_research, side_effects], priority=100)) #Create a serum finished crisis, it will trigger at the end of the round
                mc.business.add_normal_message(f"New serum design researched: {the_research.name}")
                mc.business.active_research_design = None
            elif isinstance(the_research, SerumTrait):
                if is_researched: #We've researched it already, increase mastery level instead.
                    mc.business.add_normal_message(f"Serum trait mastery improved: {the_research.name} -> {the_research.mastery_level:.1f}%")
                else:
                    mc.business.add_normal_message(f"New serum trait researched: {the_research.name}")
                    mc.business.active_research_design = None #If it's a newly discovered trait clear it so we don't start mastering it without player input.
    return

def production_assembly_line_project_on_turn():
    if not mc.business.is_open_for_business:
        return

    # calculate bonus production (25% for each employee)
    for person in (x for x in mc.business.production_team if x.is_at_office):
        mc.business.production_progress(person.focus, person.int, person.production_skill, production_modifier = 0.25)

def research_team_building_project_on_day():
    if not mc.business.is_weekend:
        for person in mc.business.research_team:
            person.change_obedience(1, add_to_log = False)

## Business IT Projects

hr_organized_chaos_project = IT_Project(name = "Organized Chaos",
    desc = "Increases the maximum efficiency of the company by 5%.",
    requirement = hr_organized_chaos_project_requirement,
    cost = 0,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = hr_organized_chaos_project_on_apply,
    on_remove_function = hr_organized_chaos_project_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "HR",
    tier = 10)

hr_task_manager_project = IT_Project(name = "Task Manager",
    desc = "Requires an HR Director. All HR employees give a maximum efficiency bonus at half the rate of the HR Director.",
    requirement = hr_task_manager_project_requirement,
    cost = 0,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "HR",
    tier = 20)

hr_hack_cell_tower_project = IT_Project(name = "Hack Cell Towers",
    desc = "Hack the city cell towers to track the location of people's phones, will add location information to the phone menu.",
    requirement = hr_hack_cell_tower_requirement,
    cost = 0,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = hr_hack_cell_tower_project_on_apply,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "HR",
    tier = 30)

supply_inventory_project = IT_Project(name = "JiT Inventory",
    desc = "Just in Time inventory practices help increase efficiency. Increased supply procurement when the company is low on supplies.",
    cost = 0,
    requirement = supply_inventory_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "supply",
    tier = 10)

supply_storage_project = IT_Project(name = "Storage Automation",
    desc = "Chemical storage and retrieval automation. Reduces the cost associated with purchasing and storing supplies by 5%.",
    cost = 0,
    requirement = supply_storage_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "supply",
    tier = 20)

market_photo_filter_project = IT_Project(name = "Photo Filters",
    desc = "Automated photo filters. Increases the desirability of the subjects used in promotions, increasing product demand. 5% product price increase.",
    cost = 0,
    requirement = market_photo_filter_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = market_photo_filter_project_on_apply,
    on_remove_function = market_photo_filter_project_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "market",
    tier = 10)

market_targeted_advertising_project = IT_Project(name = "Targeted Adverts",
    desc = "Know your audience. Refining advertising filters automatically based on the demographics of previous sales. Increases market reach by 10%.",
    cost = 0,
    requirement = market_targeted_advertising_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = market_targeted_advertising_project_on_turn,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "market",
    tier = 20)

research_peerless_review_project = IT_Project(name = "Peerless Review",
    desc = "The sensitive nature of the research hinders peer review. Automatic detection and replacement of sensitive terms allows for increased rate of research. Increases research by 5%",
    cost = 0,
    requirement = research_peerless_review_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = research_peerless_review_project_on_turn,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "research",
    tier = 10)

research_group_discovery_project = IT_Project(name = "Group Discovery",
    desc = "Automates sharing of research among team members who work in similar fields. Allows research to be more evenly distributed. Reduces Clarity costs of serum traits by 5%",
    cost = 0,
    requirement = research_group_discovery_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "research",
    tier = 30)

research_team_building_project = IT_Project(name = "Distributed Research",
    desc = "Distributing research evenly among team members eases workloads, making employees more loyal. Increases researcher obedience.",
    cost = 0,
    requirement = research_team_building_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = research_team_building_project_on_day,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "research",
    tier = 20)

production_assembly_line_project = IT_Project(name = "Assembly Line",
    desc = "Serums now created via assembly line instead of in small batches. Production increased by 25%, but also uses 25% more supply. Can be toggled.",
    cost = 0,
    requirement = production_assembly_line_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = production_assembly_line_project_on_turn,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "production",
    tier = 10)

production_equipment_selftest_project = IT_Project(name = "Equipment Selftest",
    desc = "Production equipment now runs an end of the day self test. Reduces production staff workload, slightly increasing happiness.",
    cost = 0,
    requirement = production_equipment_selftest_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = production_equipment_selftest_project_on_day,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "production",
    tier = 20)

business_IT_project_list: list[IT_Project] = [
    hr_organized_chaos_project,
    hr_task_manager_project,
    hr_hack_cell_tower_project,
    supply_inventory_project,
    supply_storage_project,
    market_photo_filter_project,
    market_targeted_advertising_project,
    research_peerless_review_project,
    research_group_discovery_project,
    research_team_building_project,
    production_assembly_line_project,
    production_equipment_selftest_project
]

def IT_get_business_projects(category: str) -> list[IT_Project]:
    return sorted([x for x in business_IT_project_list if x.category == category], key=lambda x: (x.tier, x.name))
