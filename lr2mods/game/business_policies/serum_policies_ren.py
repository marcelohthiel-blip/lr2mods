from __future__ import annotations
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.business_related.ProductionLine_ren import ProductionLine
from game.major_game_classes.character_related.Person_ren import mc

serum_policies_list = list[Policy] = []
testing_room_creation_policy: Policy
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
#### SERUM TESTING POLICY SECTION ####

def unlock_serum_policy(factor: float):
    for employee in mc.business.employee_list:
        employee.primary_job.salary *= (1.0 + factor)

def batch_size_increase(increase_amount = 0, operating_cost_increase = 50):
    mc.business.batch_size += increase_amount
    mc.business.operating_costs += operating_cost_increase

def serum_production_improvement(increase_amount = 1, operating_cost_increase = 0):
    mc.business.max_serum_tier += increase_amount
    mc.business.operating_costs += operating_cost_increase

def production_line_addition_1_requirement():
    return True

def add_production_lines(amount, operating_cost_increase = 500):
    for _ in range(0, amount):
        mc.business.production_lines.append(ProductionLine(mc.business.inventory))
        mc.business.operating_costs += operating_cost_increase

def generic_operating_cost_increase(operating_cost_increase = 0):
    mc.business.operating_costs += operating_cost_increase

def init_serum_policies():
    global mandatory_paid_serum_testing_policy
    mandatory_paid_serum_testing_policy = Policy(name = "Mandatory Paid Serum Testing",
        desc = "Unlocks employee serum testing, as well as one market specific duty.\nEmployees will be required to test any doses of serum provided, in exchange for a monetary compensation.\nInstituting this policy will increase base wage for existing employee by 10% and pays out a 10% daily wage bonus while active.",
        cost = 500,
        on_buy_function = unlock_serum_policy,
        extra_arguments = {"factor": .1},
        toggleable = True)
    global mandatory_unpaid_serum_testing_policy
    mandatory_unpaid_serum_testing_policy = Policy(name = "Mandatory Unpaid Serum Testing",
        desc = "Updates your employee contracts and will remove the requirement for compensation when they are asked to test serums.\nInstituting this policy will increase base wage for existing employees by 20% and pays out a 20% daily wage bonus while active.",
        cost = 2000,
        toggleable = True,
        on_buy_function = unlock_serum_policy,
        extra_arguments = {"factor": .2},
        own_requirement = mandatory_paid_serum_testing_policy,
        dependant_policies = mandatory_paid_serum_testing_policy)
    global daily_serum_dosage_policy
    daily_serum_dosage_policy = Policy(name = "Daily Serum Dosage",
        desc = "Mandatory serum testing is expanded into a full scale daily dosage program. Unlocks a new duty for all employees, which can be used to have serum automatically consumed at the start of each work day. Requires sufficient serum dosages in serum stock.\n\n{color=#ffff00}Note: Employees need the daily serum duty, when this policy is disabled, the duty will have no effect.{/color}",
        cost = 5000,
        toggleable = True,
        own_requirement = mandatory_unpaid_serum_testing_policy,
        dependant_policies = mandatory_unpaid_serum_testing_policy)
    global weekend_serum_dosage_policy
    weekend_serum_dosage_policy = Policy(name = "Weekend Serum Dosage",
        desc = "Mandatory serum testing is expanded into the weekend. Each employee will receive two doses of the selected serum for their department to take over the weekend. Requires sufficient serum dosages in serum stock.\n\n{color=#ffff00}Note: Employees need the weekend serum duty, when this policy is disabled, the duty will have no effect.{/color}",
        cost = 10000,
        toggleable = True,
        own_requirement = daily_serum_dosage_policy,
        dependant_policies = daily_serum_dosage_policy)
    global serum_size_1_policy
    serum_size_1_policy = Policy(name = "Batch Size Improvement 1",
        desc = "Updating the equipment throughout the lab allows for increased batch sizes of serum as well as improved supply efficiency. Increases serum batch size by 1. Specialized equipment increases daily operating costs by $50 per workday.",
        cost = 500,
        toggleable = False,
        on_buy_function = batch_size_increase,
        extra_arguments = {"increase_amount": 1, "operating_cost_increase": 50})
    global serum_size_2_policy
    serum_size_2_policy = Policy(name = "Batch Size Improvement 2",
        desc = "Improved recycling of waste materials allows for a boost in production efficiency. Increases serum batch size by 2. Specialized equipment increases daily operating costs by $250 per workday.",
        cost = 2500,
        toggleable = False,
        own_requirement = serum_size_1_policy,
        on_buy_function = batch_size_increase,
        extra_arguments = {"increase_amount": 2, "operating_cost_increase": 250},
        dependant_policies = serum_size_1_policy)
    global serum_size_3_policy
    serum_size_3_policy = Policy(name = "Batch Size Improvement 3",
        desc = "Another improvement to the lab equipment allows for even more impressive boosts in production efficiency and speed. Increases serum batch size by 2. Specialized equipment increases daily operating costs by $500 per workday.",
        cost = 10000,
        toggleable = False,
        own_requirement = serum_size_2_policy,
        on_buy_function = batch_size_increase,
        extra_arguments = {"increase_amount": 2, "operating_cost_increase": 500},
        dependant_policies = serum_size_2_policy)
    global serum_production_1_policy
    serum_production_1_policy = Policy(name = "Tier 1 Serum Production",
        desc = "You will need more complex machinery to produce advanced serum designs, but those machines aren't cheap, and they add significant overhead to your business. Allows you to produce tier 1 serum designs, but costs an additional $50 per day in operating costs.",
        cost = 750,
        toggleable = False,
        on_buy_function = serum_production_improvement,
        extra_arguments = {"operating_cost_increase": 50})
    global serum_production_2_policy
    serum_production_2_policy = Policy(name = "Tier 2 Serum Production",
        desc = "Equipping your production lines with state-of-the-art machinery is necessary to produce tier 2 serum designs. Maintenance and licensing fees will cost an additional $200 per work day.",
        cost = 5000,
        toggleable = False,
        own_requirement = serum_production_1_policy,
        on_buy_function = serum_production_improvement,
        extra_arguments = {"operating_cost_increase": 200})
    global serum_production_3_policy
    serum_production_3_policy = Policy(name = "Tier 3 Serum Production",
        desc = "Installing prototype machinery in your production lines will allow you to produce tier 3 serum designs. Maintenance and licensing fees will cost an additional $500 per work day.",
        cost = 10000,
        toggleable = False,
        own_requirement = serum_production_2_policy,
        on_buy_function = serum_production_improvement,
        extra_arguments = {"operating_cost_increase": 500})
    global production_line_addition_1_policy
    production_line_addition_1_policy = Policy(name = "Production Line Expansion 1",
        desc = "Adding a new serum processing area will allow for the production of three serums at once. Maintenance fees will increase by $500 per work day.",
        cost = 800,
        on_buy_function = add_production_lines,
        extra_arguments = {"amount": 1, "operating_cost_increase": 500})
    global production_line_addition_2_policy
    production_line_addition_2_policy = Policy(name = "Production Line Expansion 2",
        desc = "Another serum assembly line will allow for the simultaneous production of four different serum designs at once. Maintenance fees will increase by $1000 per work day.",
        cost = 3000,
        own_requirement = production_line_addition_1_policy,
        on_buy_function = add_production_lines,
        extra_arguments = {"amount": 1, "operating_cost_increase": 1000},
        dependant_policies = production_line_addition_1_policy)
    global breast_milking_space_policy
    breast_milking_space_policy = Policy(name = "Breast Milking Equipment",
        desc = "Stock the break room with hand-powered breast pumps and make them available to your staff. Unlocks a new duty for all lactating staff to have them turn over a sample of any breast milk produced.",
        cost = 1500,
        toggleable = False)
    global auto_pumping_stations_policy
    auto_pumping_stations_policy = Policy(name = "Automatic Breast Pumping Stations",
        desc = "Cutting edge breast pump machinery will be installed in the break room. Unlocks a new duty for lactating staff to provide a larger amount of breast milk at once, if they have enough to give. Maintenance fees will increase by $100 per work day.",
        cost = 5000,
        on_buy_function = generic_operating_cost_increase,
        extra_arguments = {"operating_cost_increase": 100},
        toggleable = False)
    global high_suction_pumping_machinery_policy
    high_suction_pumping_machinery_policy = Policy(name = "High Suction Breast Pumping Machinery",
        desc = "Repurposed industrial dairy farming equipment will be installed in the break room. A new duty for large breasted lactating staff will produce an uncapped amount of breast milk, plus a small flat added amount. . Maintenance fees will increase by $250 per work day.",
        cost = 12000,
        on_buy_function = generic_operating_cost_increase,
        extra_arguments = {"operating_cost_increase": 250},
        toggleable = False)

    global serum_policies_list
    serum_policies_list.extend((
        mandatory_paid_serum_testing_policy,
        mandatory_unpaid_serum_testing_policy,
        daily_serum_dosage_policy,
        weekend_serum_dosage_policy,
        serum_size_1_policy,
        serum_size_2_policy,
        serum_size_3_policy,
        serum_production_1_policy,
        serum_production_2_policy,
        serum_production_3_policy,
        production_line_addition_1_policy,
        production_line_addition_2_policy,
        breast_milking_space_policy,
        auto_pumping_stations_policy,
        high_suction_pumping_machinery_policy,
    ))
