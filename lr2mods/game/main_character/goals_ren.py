# This file holds all of the goal objects that the player might be given over the course of the game.

## LIST OF CURRENT EVENTS ##

## STAT GOALS ##
# "general_work"
# "new_hire", the_person
# "new_serum", the_serum
# "serums_sold_value", amount
# "time_advance"
# "daily_profit", amount

## WORK GOALS ##
# "player_research",amount
# "player_serums_sold_count", amount
# "player_efficiency_restore", amount
# "player_production", amount
# "player_supply_purchase", amount
# "add_uniform", the_outfit
# "HR_opinion_improvement", the_person
# "give_random_serum", the_person

## SEX GOALS ##
# "player_flirt", the_person
# "sex_event", the_person, the_position, the_object
# "sex_cum_mouth", the_person
# "sex_cum_vagina", the_person
# "girl_climax", the_person
# "girl_pregnant", the_person
# "girl_trance", the_person
# "sex_cum_on_face", the_person
# "sex_cum_on_tits", the_person
# "sex_cum_ass", the_person
# "threesome", persone_one, person_two

#GOALS TO MAKE#
# "Dress up" - Assign an outfit with X sluttiness to a person.
# Reach research tier X.
from __future__ import annotations
import builtins
import copy

import renpy
from renpy import persistent

from game.major_game_classes.game_logic.Goal_ren import Goal
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.sex_positions._position_definitions_ren import kissing
from game.helper_functions.list_functions_ren import get_random_from_list
from game.main_character.perks.Perks_ren import perk_system
from game.major_game_classes.character_related.Person_ren import Person, camila, aunt, cousin, lily, mc, mom

day = 0
time_of_day = 0
stat_goals: list[Goal] = []
work_goals: list[Goal] = []
sex_goals: list[Goal] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

def create_new_stat_goal(goal_difficulty: int):
    potential_goal: Goal = get_random_from_list(
        tuple(x for x in stat_goals if x.enabled and x.check_valid(goal_difficulty) and not x == mc.stat_goal)
    )
    if not potential_goal:
        potential_goal: Goal = get_random_from_list(
            tuple(x for x in stat_goals if x.enabled)
        )
    return create_and_activate_goal(potential_goal, goal_difficulty)

def create_new_work_goal(goal_difficulty: int) -> Goal:
    potential_goal: Goal = get_random_from_list(
        tuple(x for x in work_goals if x.enabled and x.check_valid(goal_difficulty) and not x == mc.work_goal)
    )
    if not potential_goal:
        potential_goal: Goal = get_random_from_list(
            tuple(x for x in work_goals if x.enabled)
        )
    return create_and_activate_goal(potential_goal, goal_difficulty)

def create_new_sex_goal(goal_difficulty: int):
    potential_goal: Goal = get_random_from_list(
        tuple(x for x in sex_goals if x.enabled and x.check_valid(goal_difficulty) and not x == mc.sex_goal)
    )
    if not potential_goal:
        potential_goal: Goal = get_random_from_list(
            tuple(x for x in sex_goals if x.enabled)
        )

    return create_and_activate_goal(potential_goal, goal_difficulty)

def create_initial_stat_goal(goal_difficulty: int):
    first_stat_goal = next((x for x in stat_goals if x.name == "Work-A-Day"), None)
    return create_and_activate_goal(first_stat_goal, goal_difficulty)

def create_initial_work_goal(goal_difficulty: int):
    first_work_goal = next((x for x in work_goals if x.name == "Master of Logistics"), None)
    return create_and_activate_goal(first_work_goal, goal_difficulty)

def create_initial_sex_goal(goal_difficulty: int):
    first_sex_goal = next((x for x in sex_goals if x.name == "Plenty of Fish"), None)
    return create_and_activate_goal(first_sex_goal, goal_difficulty)

def create_and_activate_goal(goal: Goal, goal_difficulty: int):
    goal_template = copy.deepcopy(goal)
    goal_template.activate_goal(goal_difficulty)
    return goal_template

## STAT GOAL FUNCTIONS ##

def work_time_function(the_goal: Goal) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def work_time_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += (the_difficulty * 2)

def hire_someone_function(the_goal: Goal, the_person: Person) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def serum_design_function(the_goal: Goal, the_serum) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def make_money_function(the_goal: Goal, amount) -> bool:
    the_goal.arg_dict["count"] += amount
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def make_money_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += the_difficulty * 500

def make_money_report(the_goal: Goal) -> str:
    return f"${the_goal.arg_dict['count']:,.0f}/${the_goal.arg_dict['required']:,.0f}"

def business_size_valid_function(the_goal: Goal, the_difficulty: int) -> bool:
    # only pick this goal when we don't have the required number of employees for goal and we can hire them
    return (mc.business.max_employee_count >= builtins.int(the_difficulty / 2)
        and mc.business.employee_count < builtins.int(the_difficulty / 2))

def business_size_function(the_goal: Goal) -> bool:
    the_goal.arg_dict["count"] = mc.business.employee_count
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def business_size_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 2)

def business_size_report_function(the_goal: Goal) -> str:
    return f"{mc.business.employee_count:.0f}/{the_goal.arg_dict['required']:.0f}"

def business_size_fraction_function(the_goal: Goal) -> float:
    return min(.99, mc.business.employee_count / max(the_goal.arg_dict["required"], 1))

def bank_account_size_valid_function(the_goal: Goal, the_difficulty: int):
    # only pick goal when we don't have the required funds yet for this difficulty
    return not mc.business.has_funds(2000 + 500 * the_difficulty)

def bank_account_size_function(the_goal: Goal) -> bool:
    #Checks to see if the player has made enough money yet.
    return mc.business.funds >= the_goal.arg_dict["required"]

def bank_account_size_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += 500 * the_difficulty

def bank_account_size_report_function(the_goal: Goal) -> str:
    return f"${mc.business.funds:,.0f} / ${the_goal.arg_dict['required']:,.0f}"

def bank_account_size_fraction_function(the_goal: Goal) -> float:
    return min(0.99, mc.business.funds / max(the_goal.arg_dict["required"], 1))

def daily_profit_count_function(the_goal: Goal, profit) -> bool:
    the_goal.arg_dict["count"] = profit # To make "progress" show
    return profit >= the_goal.arg_dict["required"]

def daily_profit_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] = 100
    the_goal.arg_dict["required"] += 50 * the_difficulty
    if the_difficulty > 4:
        the_goal.arg_dict["required"] += 100 * the_difficulty
    if the_difficulty > 8:
        the_goal.arg_dict["required"] += 150 * the_difficulty
    if the_goal.arg_dict["required"] > 5000:
        the_goal.arg_dict["required"] = 5000

## WORK GOAL FUNCTIONS ##
def generate_research_function(the_goal: Goal, amount) -> bool:
    the_goal.arg_dict["count"] += amount
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def generate_research_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += (the_difficulty * 50)

def player_sell_serums_function(the_goal: Goal, amount) -> bool:
    the_goal.arg_dict["count"] += amount
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def player_sell_serums_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += 5 * the_difficulty

def player_hr_efficiency_function(the_goal: Goal, amount) -> bool:
    the_goal.arg_dict["count"] += amount
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def player_hr_efficiency_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += 2 * the_difficulty

def player_production_function(the_goal: Goal, amount) -> bool:
    the_goal.arg_dict["count"] += amount
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def player_production_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += (the_difficulty * 50)

def player_supply_function(the_goal: Goal, amount) -> bool:
    the_goal.arg_dict["count"] += amount
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def player_supply_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += (the_difficulty * 50)

def uniform_designer_function(the_goal: Goal, the_outfit: Outfit):
    if the_outfit.identifier not in the_goal.arg_dict["outfits"]:
        the_goal.arg_dict["count"] += 1
        the_goal.arg_dict["outfits"].append(the_outfit.identifier)
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
    return False

def uniform_designer_difficulty_function(the_goal: Goal, the_difficulty):
    the_goal.arg_dict["required"] += renpy.random.randint(0, 2) #Difficulty doesn't matter, but we want them to have to add a random number of outfits.

def HR_interview_count_function(the_goal: Goal, the_person: Person) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def HR_interview_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] = builtins.min(builtins.int(1 + (the_difficulty / 5)), 5)

def star_contractor_count_function(the_goal: Goal, the_person: Person) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def star_contractor_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] = builtins.min(builtins.int(1 + (the_difficulty / 5)), 5)

def give_serum_count_function(the_goal: Goal, the_person) -> bool:
    if the_person in mc.business.employee_list + [mom, lily, aunt, cousin]:
        return False

    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def give_serum_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 3)


## SEX GOAL FUNCTIONS ##
def flirt_count_function(the_goal: Goal, the_person: Person) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def flirt_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += the_difficulty

def makeout_count_function(the_goal: Goal, the_person: Person, the_position, **kwargs) -> bool:
    if the_position == kissing and the_person.identifier not in the_goal.arg_dict["people"]:
        the_goal.arg_dict["people"].append(the_person.identifier)
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
    return False

def makeout_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / (2 * 1.0))


def mouth_cum_count_function(the_goal: Goal, the_person) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def mouth_cum_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += the_difficulty


def orgasm_count_function(the_goal: Goal, **kwargs) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def knockup_count_function(the_goal: Goal, **kwargs) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def trance_count_function(the_goal: Goal, **kwargs) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def trance_goal_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += 1

def orgasm_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += the_difficulty

def vagina_cum_count_function(the_goal: Goal, the_person: Person) -> bool:
    if the_person.identifier not in the_goal.arg_dict["people"]:
        the_goal.arg_dict["people"].append(the_person.identifier)
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
    return False

def vagina_cum_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 3.0)

def chain_orgasm_count_function(the_goal: Goal, the_person: Person, **kwargs) -> bool:
    if the_goal.arg_dict["day"] == day and the_goal.arg_dict["time"] == time_of_day and the_goal.arg_dict.get("last person", 0) == the_person.identifier:
        the_goal.arg_dict["count"] += 1

    else:
        the_goal.arg_dict["day"] = day
        the_goal.arg_dict["time"] = time_of_day
        the_goal.arg_dict["last person"] = the_person.identifier
        the_goal.arg_dict["count"] = 1 #We've made her orgasm at this point.

    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def chain_orgasm_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 5.0)

def taboo_break_function(the_goal: Goal, **kwargs) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def taboo_break_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 3.0)

def standard_count_report(the_goal: Goal) -> str:
    return f"{the_goal.arg_dict['count']:.0f}/{the_goal.arg_dict['required']:.0f}"

def standard_progress_fraction(the_goal: Goal) -> float: #Returns a float from 0.0 to 1.0 used to display progress bars. Default assumes float and required exist
    return builtins.min(0.99, (the_goal.arg_dict["count"] * 1.0) / max(the_goal.arg_dict["required"], 1))

def always_valid_goal_function(the_goal: Goal, the_difficulty: int) -> bool:
    #Always a valid goal to give to the player. TODO: Implement support for non-valid goals.
    return True

def pregnancy_valid_goal_function(the_goal: Goal, the_difficulty: int) -> bool:
    return persistent.pregnancy_pref > 0 and the_difficulty >= 5

def flat_difficulty_function(the_goal: Goal, the_difficulty: int):
    #Does not become more difficult with time.
    return

def face_cum_count_function(the_goal: Goal, the_person: Person) -> bool:
    if the_person.identifier not in the_goal.arg_dict["people"]:
        the_goal.arg_dict["people"].append(the_person.identifier)
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
    return False

def face_cum_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 4.0)

def tits_cum_count_function(the_goal: Goal, the_person) -> bool:
    if the_person.identifier not in the_goal.arg_dict["people"]:
        the_goal.arg_dict["people"].append(the_person.identifier)
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
    return False

def tits_cum_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 6.0)  #Unlocked goal, so we make it slightly easier than other similar ones.

def tits_cum_avail_function() -> bool:
    return perk_system.has_ability_perk("Tits Man")

def ass_cum_count_function(the_goal: Goal, the_person: Person) -> bool:
    if the_person.identifier not in the_goal.arg_dict["people"]:
        the_goal.arg_dict["people"].append(the_person.identifier)
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
    return False

def ass_cum_count_difficulty_function(the_goal: Goal, the_difficulty: int):
    the_goal.arg_dict["required"] += builtins.int(the_difficulty / 4.0)

def threesome_count_function(the_goal: Goal, the_person_one, the_person_two) -> bool:
    the_goal.arg_dict["count"] += 1
    return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

def threesome_difficulty_function(the_goal: Goal, the_difficulty):
    #For now this difficulty does not scale
    the_goal.arg_dict["required"] = 1

def camila_company_goals_avail_function() -> bool:
    return (camila.progress.obedience_step >= 1)

def camila_personal_goals_avail_function() -> bool:
    return (camila.progress.obedience_step >= 2)

def camila_sex_goals_avail_function() -> bool:
    return (camila.progress.obedience_step >= 3)

def init_goal_lists():
    ## STAT GOALS ##
    work_time_goal = Goal("Work-A-Day", "It may not be groundbreaking, but you learn a little something every day. Personally perform any work task.", "general_work", "Business", always_valid_goal_function, work_time_function,
        {"count": 0, "required": 5},
        difficulty_scale_function = work_time_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    hire_someone_goal = Goal("Fresh Blood", "New talent is the lifeblood of your business. Comb through the resumes and see who catches your eye.", "new_hire", "Business", always_valid_goal_function, hire_someone_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    serum_design_goal = Goal("Research and Development", "Theoretical research is all well and good, but you need products to put to market. Create a new serum design.", "new_serum", "Business", always_valid_goal_function, serum_design_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    make_money_goal = Goal("Stable Income", "Any successful business needs income to match expenses. Have your business earn money.", "serums_sold_value", "Business", always_valid_goal_function, make_money_function,
        {"count": 0, "required": 500},
        difficulty_scale_function = make_money_difficulty_function, report_function = make_money_report, progress_fraction_function = standard_progress_fraction)

    business_size_goal = Goal("Sizeable Workforce", "Sometimes quantity is more important than quality. Ensure your business has the required number of employees.", "time_advance", "MC", business_size_valid_function, business_size_function,
        {"required": 1},
        difficulty_scale_function = business_size_difficulty_function, report_function = business_size_report_function, progress_fraction_function = business_size_fraction_function)

    bank_account_size_goal = Goal("Liquidity", "A depth of liquid cash gives you the ability to react quickly to the changing whims of the free market. Amass a small fortune (Checked at the end of the day).", "time_advance", "MC", bank_account_size_valid_function, bank_account_size_function,
        {"required": 2000},
        difficulty_scale_function = bank_account_size_difficulty_function, report_function = bank_account_size_report_function, progress_fraction_function = bank_account_size_fraction_function)

    daily_profit_goal = Goal("Daily Profit", "Profitability is always a concern when running a business. Have your business make at least a certain amount in one day.", "daily_profit", "Business", always_valid_goal_function, daily_profit_count_function,
        {"count": 0, "required": 50},
        difficulty_scale_function = daily_profit_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    ## WORK GOALS ##
    generate_research_goal = Goal("Brave New World", "The future is knocking, it's time to answer. Generate research points.", "player_research", "Business", always_valid_goal_function, generate_research_function,
        {"count": 0, "required": 100},
        difficulty_scale_function = generate_research_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    sell_serums_goal = Goal("Face of the Business", "Exercise your personal skills, pick up a phone, and make some sales! Sell some doses of serum.", "player_serums_sold_count", "Business", always_valid_goal_function, player_sell_serums_function,
        {"count": 0, "required": 5},
        difficulty_scale_function = player_sell_serums_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    hr_efficiency_goal = Goal("Paper Pusher", "Payroll, scheduling, tax structure, the internal demands of employment are always present. Perform HR work to improve efficiency", "player_efficiency_restore", "Business", always_valid_goal_function, player_hr_efficiency_function,
        {"count": 0, "required": 10},
        difficulty_scale_function = player_hr_efficiency_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    generate_production_goal = Goal("Practical Chemistry", "Get busy in the production lab and turn out some product. Produce production points.", "player_production", "Business", always_valid_goal_function, player_production_function,
        {"count": 0, "required": 100},
        difficulty_scale_function = player_production_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    generate_supply_goal = Goal("Master of Logistics", 'You need to handle the "supply" side of supply and demand. Get on the phone and secure basic supplies for your serum.', "player_supply_purchase", "Business", always_valid_goal_function, player_supply_function,
        {"count": 0, "required": 100},
        difficulty_scale_function = player_supply_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    set_uniform_goal = Goal("Corporate Dress", "Public appearance can be just as important as the product you are selling. Pay your corporate wardrobe a visit and assign a few new uniform pieces.", "add_uniform", "Business", always_valid_goal_function, uniform_designer_function,
        {"count": 0, "required": 1, "outfits": []},
        difficulty_scale_function = uniform_designer_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    HR_interview_goal = Goal("HR meetings", "Use the HR director to conduct meetings with employees.", "HR_opinion_improvement", "MC", always_valid_goal_function, HR_interview_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = HR_interview_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    give_serum_goal = Goal("Try This Serum", "Successfully give a serum to a person who is not an employee or family member.", "give_random_serum", "MC", always_valid_goal_function, give_serum_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = give_serum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    ## SEX GOALS ##
    flirt_count_goal = Goal("Plenty of Fish", "The first step is putting yourself out there. Flirt a few times.", "player_flirt", "MC", always_valid_goal_function, flirt_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = flirt_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    makeout_count_goal = Goal("Tongue Twister", "Practice makes perfect, and kissing is a good thing to be perfect at. Make out with different women.", "sex_event", "MC", always_valid_goal_function, makeout_count_function,
        {"count": 0, "required": 2, "people": []},
        difficulty_scale_function = makeout_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    mouth_cum_goal = Goal("Good Girls Swallow", "There's nothing better than seeing the look in a girl's eyes when you shoot your hot cum across her tongue. Do that a few times.", "sex_cum_mouth", "MC", always_valid_goal_function, mouth_cum_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = mouth_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    orgasm_count_goal = Goal("Shiver", "Send shivers down her spine with a kiss; make her spasm while you fuck her; do what you have to do to make her orgasm. Cause a few orgasms, all at once or split up.", "girl_climax", "MC", always_valid_goal_function, orgasm_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = orgasm_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    vagina_cum_goal = Goal("Spread your Seed", "They may be on the pill, they may be playing it risky, maybe they just aren't thinking straight. Regardless, when a girl asks for you to cum inside you should be happy to oblige. Cum inside a few different girls.", "sex_cum_vagina", "MC", always_valid_goal_function, vagina_cum_count_function,
        {"count": 0, "required": 1, "people": []},
        difficulty_scale_function = vagina_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    chain_orgasm_goal = Goal("Ahegao", "Sure she's orgasmed, but what about second orgasms? Melt a girl's brain by making her cum repeatedly in the same session.", "girl_climax", "MC", always_valid_goal_function, chain_orgasm_count_function,
        {"count": 0, "required": 2, "day": 0, "time": 0, "last person": None},
        difficulty_scale_function = chain_orgasm_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    taboo_break_goal = Goal("New Frontiers", "There's nothing like a new experience, so go give someone else one. Break some taboos and show her what she's missing!", "girl_taboo_break", "MC", always_valid_goal_function, taboo_break_function,
        {"count": 0, "required": 2},
        difficulty_scale_function = taboo_break_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    knockup_goal = Goal("Beautiful Burdening", "They might say they don't want kids, but in the heat of the moment simple biology can not be denied. Bang 'em and breed 'em!", "girl_pregnant", "MC", pregnancy_valid_goal_function, knockup_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    trance_goal = Goal("Mind Break", "Those soft-spoken words, her shallow breathing, that cum-clouded look in her eye - all of them mean she's ready to hear a few choice suggestions from you. Put a girl into a trance.", "girl_trance", "MC", always_valid_goal_function, trance_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = trance_goal_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    face_cum_goal = Goal("Paint the Town White", "Show the world that various girls belong to you, by cumming all over their faces.", "sex_cum_on_face", "MC", always_valid_goal_function, face_cum_count_function,
        {"count": 0, "required": 1, "people": []},
        difficulty_scale_function = face_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    ass_cum_goal = Goal("Anal Seeding", "There's nothing like dumping a load in a tight asshole. Cum inside a few different asses.", "sex_cum_ass", "MC", always_valid_goal_function, ass_cum_count_function,
        {"count": 0, "required": 1, "people": []},
        difficulty_scale_function = ass_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    threesome_goal = Goal("Have a Threesome", "You don't need a million dollars to do two girls at the same time.", "threesome", "MC", always_valid_goal_function, threesome_count_function,
        {"count": 0, "required": 1},
        difficulty_scale_function = threesome_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

### Camila goals ###
# The goals are added as a part of Camila's questline.
#Personal goals

#Work goals
    star_contractor_goal = Goal("Star Contractor", "Fulfill business contracts.", "contract_complete", "Business", always_valid_goal_function, generate_research_function,
        {"count": 0, "required": 100},
        difficulty_scale_function = star_contractor_difficulty_function, report_function = star_contractor_count_function, progress_fraction_function = standard_progress_fraction, enabled = False, available = False, avail_req = camila_company_goals_avail_function)

#Sexual Goals
    her_place_goal = Goal("Her Place", "Get invited back to a woman's place after a date.", "sex_cum_on_tits", "MC", always_valid_goal_function, tits_cum_count_function,
        {"count": 0, "required": 1, "people": []},
        difficulty_scale_function = tits_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False, available = False, avail_req = tits_cum_avail_function)

#Special Goals
    tits_cum_goal = Goal("Frosted Cupcakes", "Mark your territory. Cum on multiple girl's tits.", "sex_cum_on_tits", "MC", always_valid_goal_function, tits_cum_count_function,
        {"count": 0, "required": 1, "people": []},
        difficulty_scale_function = tits_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False, available = False, avail_req = tits_cum_avail_function)

    global stat_goals
    stat_goals.extend((
        work_time_goal,
        hire_someone_goal,
        serum_design_goal,
        make_money_goal,
        business_size_goal,
        bank_account_size_goal,
        daily_profit_goal,
    ))

    global work_goals
    work_goals.extend((
        generate_research_goal,
        sell_serums_goal,
        hr_efficiency_goal,
        generate_production_goal,
        generate_supply_goal,
        set_uniform_goal,
        give_serum_goal,
        HR_interview_goal,
    ))

    global sex_goals
    sex_goals.extend((
        flirt_count_goal,
        makeout_count_goal,
        mouth_cum_goal,
        orgasm_count_goal,
        vagina_cum_goal,
        chain_orgasm_goal,
        taboo_break_goal,
        knockup_goal,
        trance_goal,
        face_cum_goal,
        tits_cum_goal,
        ass_cum_goal,
        threesome_goal,
    ))

def update_available_goals():
    for goal in stat_goals:
        goal.check_available()

    for goal in work_goals:
        goal.check_available()

    for goal in sex_goals:
        goal.check_available()
    return
