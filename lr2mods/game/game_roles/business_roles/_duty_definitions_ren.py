#Contains all the stuff about instantiating duties.

# ie basic production/research/supply procurement/marketing/HR work.
# Rework some existing special roles into duties.
# -> Rule of thumb: if you can only have one thing it's a Job, if you can have this thing plus other things they're duties.
# -> Modelling should be a duty.
# -> Head researcher should be a Job (w/ a special duty?)
# Rework existing business policies into duties (Research -> Clarity, Serum policies)
# Add new duties (weekend/overtime work, some cross-department duties (reduce HR costs, expand market reach with R&D, make raw cash with marketers, etc.)
from __future__ import annotations
import builtins
import copy
from itertools import chain
import renpy
from game.helper_functions.list_functions_ren import get_random_from_list
from game.game_roles._role_definitions_ren import lactating_serum_role
from game.major_game_classes.business_related.Infraction_ren import Infraction
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Duty_ren import Duty
from game.major_game_classes.character_related._job_definitions_ren import stripclub_manager_job, stripclub_mistress_job
from game.major_game_classes.character_related.Person_ren import Person, mc, town_relationships
from game.major_game_classes.character_related.Relationship_ren import RelationshipArray
from game.business_policies.clothing_policies_ren import male_focused_marketing_policy
from game.business_policies.organisation_policies_ren import bureaucratic_nightmare, theoretical_research, research_journal_subscription, practical_experimentation, office_punishment
from game.business_policies.serum_policies_ren import breast_milking_space_policy, auto_pumping_stations_policy, high_suction_pumping_machinery_policy
from game.business_policies.serum_policies_ren import mandatory_unpaid_serum_testing_policy, daily_serum_dosage_policy, weekend_serum_dosage_policy
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait

general_duties_list: list[Duty]
general_rd_duties: list[Duty]
general_market_duties: list[Duty]
general_supply_duties: list[Duty]
general_production_duties: list[Duty]
general_hr_duties: list[Duty]

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 0 python:
"""
#Basic work duty functions#
## Supply ##
def get_duty_supply_cost_modifier(person: Person):
    cost_modifier = 1.0
    if person.has_duty(greymarket_deals_duty):
        cost_modifier = 0.75
    if person.has_duty(alternative_payment_duty):
        if person.effective_sluttiness() >= 25:
            cost_modifier += -0.05 * person.foreplay_sex_skill
        if person.effective_sluttiness() >= 50:
            cost_modifier += -0.05 * person.oral_sex_skill
    return cost_modifier

def supply_work_duty_on_turn(person: Person):
    cost_modifier = get_duty_supply_cost_modifier(person)

    mc.business.supply_purchase(person.focus, person.charisma, person.supply_skill, person.calculate_job_efficiency(), cost_modifier)

def heavy_supply_work_duty_on_turn(person: Person):
    cost_modifier = get_duty_supply_cost_modifier(person)

    mc.business.supply_purchase(person.focus, person.charisma, person.supply_skill, person.calculate_job_efficiency() * 0.2, cost_modifier)
    person.change_happiness(-2, add_to_log = False)

def greymarket_deals_duty_on_turn(person: Person):
    mc.business.attention += 1

def alternative_payment_duty_requirement(person: Person):
    if not male_focused_marketing_policy.is_active:
        return False
    if person.effective_sluttiness() < 25:
        return "Requires 25 Sluttiness"
    return True

## Research ##
def research_clarity_production_check(person: Person, research_amount): #Helper function to check a researcher and generate the correct amount of associated Clarity.
    clarity_produced = 0
    if person.has_duty(theoretical_research_duty):
        clarity_produced += research_amount * 0.2

    if person.has_duty(research_journal_subscription_duty):
        clarity_produced += research_amount * 0.2

    if person.has_duty(practical_experimentation_duty) and mc.business.supply_count >= 5:
        mc.business.supply_count -= 5
        clarity_produced += research_amount * 0.2

    mc.business.partial_clarity += clarity_produced
    if mc.business.partial_clarity >= 1.0:
        int_clarity = builtins.int(mc.business.partial_clarity)
        mc.add_clarity(int_clarity, add_to_log = False)
        mc.business.partial_clarity -= int_clarity
        mc.business.add_counted_message("Idle R&D team produced Clarity", int_clarity)


def research_work_duty_on_turn(person: Person):
    research_amount = mc.business.research_progress(person.int, person.focus, person.research_skill, person.calculate_job_efficiency())
    research_clarity_production_check(person, research_amount)

def heavy_research_work_duty_on_turn(person: Person):
    research_amount = mc.business.research_progress(person.int, person.focus, person.research_skill, person.calculate_job_efficiency() * 0.2)
    research_clarity_production_check(person, research_amount)
    person.change_happiness(-2, add_to_log = False)

def research_journal_on_apply(person: Person):
    mc.business.operating_costs += 10

def research_journal_on_remove(person: Person):
    mc.business.operating_costs -= 10

## Production
def production_work_duty_on_turn(person: Person):
    mc.business.production_progress(person.focus, person.int, person.production_skill, person.calculate_job_efficiency())

def heavy_production_work_duty_on_turn(person: Person):
    mc.business.production_progress(person.focus, person.int, person.production_skill, person.calculate_job_efficiency() * 0.2)
    person.change_happiness(-2, add_to_log = False)

def bend_safety_rules_on_turn(person: Person):
    mc.business.production_progress(person.focus, person.int, person.production_skill, person.calculate_job_efficiency() * 0.1)

    dose_chance = 50 - (person.production_skill * 2) - (person.focus * 3) - person.int
    if renpy.random.randint(1, 100) < dose_chance:
        apply_accidental_serum_dosage(person)

def production_quality_control_on_day(person: Person):
    person.change_happiness(2, add_to_log = False) # pride in her work makes her happier

    dose_chance = 50 - (person.production_skill * 2) - (person.focus * 3) - person.int
    if renpy.random.randint(1, 100) < dose_chance:
        apply_accidental_serum_dosage(person)

def apply_accidental_serum_dosage(person: Person):
    if (person.active_serum_count >= person.serum_tolerance):
        return # we are at limit don't apply

    serum = mc.business.get_random_weighed_production_serum()
    if not person.is_affected_by_serum(serum):
        person.give_serum(serum)
        person.change_happiness(-2, add_to_log = False)


## Marketing ##
def market_work_duty_on_turn(person: Person):
    work_skill = person.market_skill + person.extra_market_skill
    mc.business.sale_progress(person.charisma, person.focus, work_skill, person.calculate_job_efficiency())

def heavy_market_work_duty_on_turn(person: Person):
    work_skill = person.market_skill + person.extra_market_skill
    mc.business.sale_progress(person.charisma, person.focus, work_skill, person.calculate_job_efficiency() * 0.2)
    person.change_happiness(-2, add_to_log = False)

def client_demonstration_duty_requirement(person: Person):
    return mandatory_unpaid_serum_testing_policy.is_active

def client_demonstration_duty_on_turn(person: Person):
    mc.business.sale_progress(0, 0, person.foreplay_sex_skill, person.calculate_job_efficiency())
    if renpy.random.randint(0, 100) < 5:
        person.give_serum(mc.business.get_random_weighed_production_serum())
        person.change_happiness(-2, add_to_log = False)

def work_for_tips_duty_requirement(person: Person):
    if not male_focused_marketing_policy.is_active:
        return False
    if person.sluttiness < 25:
        return "Requires 25 Sluttiness"
    return True

## HR ##
def hr_work_duty_on_turn(person: Person):
    mc.business.hr_progress(person.charisma, person.int, person.hr_skill, person.calculate_job_efficiency())

def heavy_hr_work_duty_on_turn(person: Person):
    mc.business.hr_progress(person.charisma, person.int, person.hr_skill, person.calculate_job_efficiency() * 0.2)
    person.change_happiness(-2, add_to_log = False)

def encourage_loyalty_duty_on_turn(person: Person):
    coworker = get_random_from_list([x for x in mc.business.employees_at_office if x != person and x.obedience < person.obedience - 1])
    if isinstance(coworker, Person):
        coworker.change_obedience(1, add_to_log = False)

def internal_propaganda_duty_on_turn(person: Person):
    coworker = get_random_from_list([x for x in mc.business.employees_at_office if x != person and x.love < person.love - 1])
    if isinstance(coworker, Person):
        coworker.change_love(1, add_to_log = False)

def corrupt_work_chat_duty_on_turn(person: Person):
    coworker = get_random_from_list([x for x in mc.business.employees_at_office if x != person and x.sluttiness < person.sluttiness - 1])
    if isinstance(coworker, Person):
        coworker.change_slut(1, add_to_log = False)

## GENERAL DUTY FUNCTIONS ##

def mandatory_breaks_duty_on_turn(person: Person):
    person.change_happiness(1, add_to_log = False)

def daily_serum_dosage_duty_requirement(person: Person):
    return daily_serum_dosage_policy.is_owned

def weekend_serum_dosage_duty_requirement(person: Person):
    return weekend_serum_dosage_policy.is_owned

def daily_serum_dosage_duty_on_move(person: Person):
    if not daily_serum_dosage_policy.is_active:
        return # only execute when policy is active

    if person.event_triggers_dict.get("daily_serum_distributed", False):
        return #Give it to them first thing in the morning, but only once

    if not person.is_at_work:
        return #Don't give it to them if they aren't at work.

    give_daily_serum_dosage(person)

def give_daily_serum_dosage(person: Person):
    serum = None
    if person in chain(mc.business.research_team, mc.business.college_interns_research):
        serum = mc.business.r_serum
    elif person in chain(mc.business.market_team, mc.business.college_interns_market):
        serum = mc.business.m_serum
    elif person in chain(mc.business.production_team, mc.business.college_interns_production):
        serum = mc.business.p_serum
    elif person in chain(mc.business.supply_team, mc.business.college_interns_supply):
        serum = mc.business.s_serum
    elif person in chain(mc.business.hr_team, mc.business.college_interns_HR):
        serum = mc.business.h_serum
    elif mc.owns_strip_club:
        if person in mc.business.stripclub_strippers:
            serum = mc.business.strippers_serum
        elif person in mc.business.stripclub_waitresses:
            serum = mc.business.waitresses_serum
        elif person in mc.business.stripclub_bdsm_performers:
            serum = mc.business.bdsm_performers_serum
        elif person.has_job((stripclub_manager_job, stripclub_mistress_job)):
            serum = mc.business.manager_serum

    if serum is not None:
        person.event_triggers_dict["daily_serum_distributed"] = True
        should_give_serum = True
        for active_serum in person.serum_effects:
            if serum.is_same_design(active_serum):
                if active_serum.total_duration - active_serum.duration_counter >= 3:
                    should_give_serum = False #Don't double-dose girls if they have the serum running and it will last the work day already
                    break

        if should_give_serum:
            if mc.business.inventory.get_serum_count(serum) > 0:
                mc.business.inventory.change_serum(serum, -1)
                person.give_serum(serum, add_to_log = False)
            else:
                mc.business.add_counted_message(f"Stockpile out of {serum.name} to give to staff.")

def daily_serum_dosage_duty_on_day(person: Person):
    person.event_triggers_dict["daily_serum_distributed"] = False

def weekend_serum_dosage_duty_on_move(person: Person):
    if not weekend_serum_dosage_policy.is_active:
        return # only execute when policy is active

    if person.event_triggers_dict.get("daily_serum_distributed", False):
        return #Give it to them first thing in the morning, but only once

    if not mc.business.is_weekend:
        return #Don't give it to them on work days.

    give_daily_serum_dosage(person)

def bureaucratic_nightmare_duty_requirement(person: Person):
    return bureaucratic_nightmare.is_active

def employee_generate_infraction_requirement(person: Person):
    return True

def social_media_advertising_duty_requirement(person: Person):
    if person.instapic_known or person.dikdok_known or person.onlyfans_known:
        return True
    return "No Known Social Media Account"

def social_media_advertising_duty_on_turn(person: Person):
    effect = 0
    work_skill = person.market_skill
    if person.effective_sluttiness() >= 25:
        work_skill += person.foreplay_sex_skill
    if person.instapic_known:
        effect += 0.1
    if person.dikdok_known:
        effect += 0.1
    if person.onlyfans_known:
        effect += 0.1
    mc.business.sale_progress(person.charisma, person.focus, work_skill, person.calculate_job_efficiency() * effect)

def get_girl_milky_serum(person: Person) -> SerumDesign | None:
    serum_produced: SerumDesign = get_random_from_list(person.event_triggers_dict.get("lactating_serum_types", [])) #If there are multiple traits we only use a random one
    if serum_produced:
        milk_serum = copy.deepcopy(serum_produced)
        milk_serum.name = f"Milky {serum_produced.name}"
        milk_serum.add_trait(get_milk_trait())
        return milk_serum
    return None

def get_milk_trait() -> SerumTrait: # Generates a milk trait that can be used any time you harvest lactating milk.
    return SerumTrait("Breast Milk",
        "Fresh breast milk. Valuable to the right sort of person.",
        physical_aspect = 2, medical_aspect = 2, mental_aspect = 1)

def auto_milk_tits(person: Person, max_doses: int, extra_doses = 0):
    available_doses = min(max_doses, int(person.breast_milk))
    if person.has_role(lactating_serum_role) and available_doses > 0:
        available_doses = min(max_doses, builtins.int(person.breast_milk))
        milk_serum = get_girl_milky_serum(person)
        if milk_serum:
            mc.business.inventory.change_serum(milk_serum, available_doses + extra_doses)
            person.breast_milk = 0

    elif person.lactation_sources > 0 and available_doses > 0:
        person.breast_milk -= available_doses
        milk_serum = SerumDesign("Breast Milk")
        milk_serum.add_trait(get_milk_trait())
        mc.business.inventory.change_serum(milk_serum, int(available_doses) + extra_doses)
        person.breast_milk = 0

def breast_milking_space_duty_requirement(person: Person):
    if not breast_milking_space_policy.is_active:
        return False
    return True

def breast_milking_space_on_turn(person: Person):
    auto_milk_tits(person, 1)

def breast_pump_2_duty_requirement(person: Person):
    if not auto_pumping_stations_policy.is_active:
        return False
    return True

def breast_pump_2_duty_on_turn(person: Person):
    auto_milk_tits(person, 3)

def breast_pump_3_duty_requirement(person: Person):
    if not high_suction_pumping_machinery_policy.is_active:
        return False
    if not person.has_large_tits:
        return "Breasts too small for machine"
    return True

def breast_pump_3_duty_on_turn(person: Person):
    auto_milk_tits(person, 99, 1)


## R&D DUTY FUNCTIONS ##
def theoretical_research_duty_requirement(person: Person):
    return theoretical_research.is_active

def research_journal_subscription_duty_requirement(person: Person):
    return research_journal_subscription.is_active

def practical_experimentation_duty_requirement(person: Person):
    return practical_experimentation.is_active

def IT_work_duty_requirement(person: Person):
    if mc.business.it_director and person != mc.business.it_director:   #Don't let the IT director double dip
        return True
    return False

def IT_work_duty_on_turn(person: Person):
    if mc.business.current_IT_project:
        mc.business.IT_increase_project_progress(amount = builtins.int((person.int * 2) + (person.focus)) / 3) #Not as much research as the IT director

## HR DUTY FUNCTIONS ##
def find_infractions_duty_requirement(person: Person):
    return office_punishment.is_active

def random_infraction_generation(the_target):
    potential_infractions = []
    potential_infractions.append(Infraction.bureaucratic_mistake_factory())
    potential_infractions.append(Infraction.careless_accident_factory())
    potential_infractions.append(Infraction.underperformance_factory())
    potential_infractions.append(Infraction.office_disturbance_factory())
    if the_target.is_wearing_uniform:
        potential_infractions.append(Infraction.out_of_uniform_factory())
    if the_target.obedience < 100:
        potential_infractions.append(Infraction.disobedience_factory())
    if the_target.effective_sluttiness() > 25:
        potential_infractions.append(Infraction.inappropriate_behaviour_factory())
    return get_random_from_list(potential_infractions)


def find_infractions_duty_on_turn(person: Person):
    if renpy.random.randint(0, 100) < 10: #NOTE: This is different from 5% so we can have low obedience/rival employees show up more often.
        # There's a chance we've discovered an infraction
        target = get_random_from_list(mc.business.employees_at_office)
        if target is None:
            return #Nobody to generate infractions for.

        if person == target:
            # NOTE: Doesn't have any probability correction, because you always 100% know when you've committed an infraction
            # when she's submissive enough, she will give herself an infraction
            if person.is_submissive:
                target.add_infraction(random_infraction_generation(target), add_to_log = False)

        else:
            infraction_chance = 150 - target.obedience
            if town_relationships.get_relationship_type(person, target) == "Rival":
                infraction_chance += 20
            elif town_relationships.get_relationship_type(person, target) == "Nemesis":
                infraction_chance += 40
            elif town_relationships.get_relationship_type(person, target) == "Friend":
                infraction_chance -= 20
            elif town_relationships.get_relationship_type(person, target) in chain(("Best Friend", ), RelationshipArray.RELATIONSHIP_FAMILY):
                infraction_chance -= 40
            if renpy.random.randint(0, 100) < infraction_chance:
                target.add_infraction(random_infraction_generation(target))

def init_duty_lists():
    ## BASIC WORK DUTIES ##
    global supply_work_duty
    supply_work_duty = Duty("Order Supplies",
        "Contact bulk chemical providers, place orders, arrange for deliveries, and ensure the production team has all the materials they need. Orders 3xFocus + 2xSupply Skill + 1xCharisma Supply, at a cost of $1 per Supply.",
        on_turn_function = supply_work_duty_on_turn)
    global heavy_supply_work_duty
    heavy_supply_work_duty = Duty("Heavy Workload",
        "Enough work to fill up the day, and then some. Produces an extra 20% of normal production, but lowers Happiness by -2 per turn.",
        on_turn_function = heavy_supply_work_duty_on_turn)

    global research_work_duty
    research_work_duty = Duty("Research and Development",
        "Experiment with chemical formulations, refine synthesis techniques, and prepare models for stability and long term effectiveness of new serum traits and designs. Produces 3xIntelligence + 2xResearch Skill + 1xFocus Research Points per turn.",
        on_turn_function = research_work_duty_on_turn)
    global heavy_research_work_duty
    heavy_research_work_duty = Duty("Heavy Workload",
        "Enough work to fill up the day, and then some. Produces an extra 20% of normal production, but lowers Happiness by -2 per turn.",
        on_turn_function = heavy_research_work_duty_on_turn)

    global production_work_duty
    production_work_duty = Duty("Production Line Work",
        "Operate the machinery necessary to turn chemical precursors into serum doses at an industrial scale and at economical costs. Produces (3xFocus + 2xProduction Skill + 1xIntelligence) Production Points per turn, at a cost of 1 unit of Supply.",
        on_turn_function = production_work_duty_on_turn)
    global heavy_production_work_duty
    heavy_production_work_duty = Duty("Heavy Workload",
        "Enough work to fill up the day, and then some. Produces an extra 20% of normal production, but lowers Happiness by -2 per turn.",
        on_turn_function = heavy_production_work_duty_on_turn)

    global market_work_duty
    market_work_duty = Duty("Find Clients",
        "Cold-call potential clients and inform them about new products, respond to business inquiries, and increase general awareness about your product. Increases Market Reach by 15xCharisma + 10xMarket Skill + 5xFocus per turn. Producing 1 Market Reach per 1 of each Serum Aspect sold is enough to keep price at 100%. Higher Market Reach increases Aspect value, while lower Market Reach decreases it.",
        on_turn_function = market_work_duty_on_turn)
    global heavy_market_work_duty
    heavy_market_work_duty = Duty("Heavy Workload",
        "Enough work to fill up the day, and then some. Produces an extra 20% of normal production, but lowers Happiness by -2 per turn.",
        on_turn_function = heavy_market_work_duty_on_turn)

    global hr_work_duty
    hr_work_duty = Duty("Office Paperwork",
        "Manage payroll, distribute internal reports, receive official complaints, and otherwise handle administrative work as it arises. Raises Business Efficiency by 3xFocus + 2xHR Skill + 1xCharisma per turn. Efficiency directly affects the production of all other duties.",
        on_turn_function = hr_work_duty_on_turn) #We could do this on_move?
    global heavy_hr_work_duty
    heavy_hr_work_duty = Duty("Heavy Workload",
        "Enough work to fill up the day, and then some. Produces an extra 20% of normal production, but lowers Happiness by -2 per turn.",
        on_turn_function = heavy_hr_work_duty_on_turn)

    ## GENERAL DUTIES ## - Duties that should be available to everyone at the company.
    global mandatory_breaks_duty
    mandatory_breaks_duty = Duty("Mandatory Breaks",
        "Ample time throughout the day to take a break, get some coffee, and stretch your legs. Doesn't achieve anything, but makes the work slightly more pleasant. Increases Happiness by 1/turn.",
        on_turn_function = mandatory_breaks_duty_on_turn)
    global extra_paperwork_duty
    extra_paperwork_duty = Duty("Extra Paperwork", #NOTE: Effect is calculated by Business so it can ignore extra effectiveness costs from other things
        "Complete all of your own paperwork, reducing the amount of administrative work that needs to be done. This employee will not lower Business Efficiency every turn.")
    global daily_serum_dosage_duty
    daily_serum_dosage_duty = Duty("Daily Serum Dose",
        "Receive a dose of serum from management at the start of every work day, unless a previous dose will last the work day. Serum type can be varied by department and set from the CEO office.",
        requirement_function = daily_serum_dosage_duty_requirement,
        on_move_function = daily_serum_dosage_duty_on_move, #NOTE: A flag makes sure this is only triggered once per day.
        on_day_function = daily_serum_dosage_duty_on_day)
    global weekend_serum_dosage_duty
    weekend_serum_dosage_duty = Duty("Weekend Serum Dose",
        "Receive a dose of serum from management at the start of every weekend, unless a previous dose will last the weekend. Serum type can be varied by department and set from the CEO office (daily serum dose).",
        requirement_function = weekend_serum_dosage_duty_requirement,
        on_move_function = weekend_serum_dosage_duty_on_move, #NOTE: A flag makes sure this is only triggered once per day.
        on_day_function = daily_serum_dosage_duty_on_day,
        only_at_work = False)

    employee_generate_infraction = Action("Invent an infraction\n{menu_red}Costs: -5 Efficiency{/menu_red}", employee_generate_infraction_requirement, "employee_generate_infraction_label",
        menu_tooltip = "Company policy is so complicated it's nearly impossible to go a day without violating some minor rule. If you were paranoid, you might think it was written that way on purpose...")
    global bureaucratic_nightmare_duty
    bureaucratic_nightmare_duty = Duty("Bureaucratic nightmare",
        "Forms, records, reports, and even more forms, all in triplicate. So many rules that it's impossible not to make a mistake somewhere! Management can generate an infraction at will, at the cost of 5% business efficiency.",
        requirement_function = bureaucratic_nightmare_duty_requirement,
        actions = [employee_generate_infraction])
    global social_media_advertising_duty
    social_media_advertising_duty = Duty("Social Media Advertising",
        "Post company approved ads on your personal social media accounts. Produces 10% of normal Marketing production for each InstaPic, DikDok, and OnlyFanatics account the employee has. If Sluttiness is 25 or higher, also adds Foreplay to Marketing Skill for this bonus production .",
        requirement_function = social_media_advertising_duty_requirement,
        on_turn_function = social_media_advertising_duty_on_turn)

    global breast_milk_pump_1_duty
    breast_milk_pump_1_duty = Duty("Provide Breast Milk Samples",
        "Make use of company provide milk pumping equipment to provide management with breast milk samples for health and safety purposes. Produces doses of breast milk serum, limited to a maximum 1 dose per turn. Smaller breasts or a low number of lactation sources may result in doses only being created every two or three turns.\n{menu_yellow}Please note: Duty has no effect when girl is not lactating.{/menu_yellow}",
        requirement_function = breast_milking_space_duty_requirement,
        on_turn_function = breast_milking_space_on_turn)

    global breast_milk_pump_2_duty
    breast_milk_pump_2_duty = Duty("Mandatory Breast Pumping",
        "Use electronic breast pump stations at regular intervals to prevent interruptions to normal business operations. Produces up to 3 doses of breast milk serum per turn. Large breasts and/or multiple lactation sources will be required to reach maximum output\n{menu_yellow}Please note: Duty has no effect when girl is not lactating.{/menu_yellow}",
        requirement_function = breast_pump_2_duty_requirement,
        on_turn_function = breast_pump_2_duty_on_turn)

    global breast_milk_pump_3_duty
    breast_milk_pump_3_duty = Duty("Industrial Breast Suction",
        "Spend part of the day with your breasts attached to repurposed dairy hardware. The high efficiency hardware will ensure every possible drop of breast milk is extracted in a timely manner. Breast milk production is limited only by breast size and number of lactation sources, and an additional dose is created whenever any milk is produced. Requires at least D-cup breast to properly interface with the machinery\n{menu_yellow}Please note: Duty has no effect when girl is not lactating.{/menu_yellow}",
        requirement_function = breast_pump_3_duty_requirement,
        on_turn_function = breast_pump_3_duty_on_turn)

    #TODO: Company Informant. Occasionally will generate an infraction for other girls, particularly ones she is friends with.
    #TODO: Turn the +Sluttiness effects into individual duties.
    #TODO: Milking duties, unlocked by having the milk serum production thing unlocked.

    #TODO: Figure out how to work this into our scheduling code. Probably not worth it.
    #TODO: Extra Hours. Employee will stay 1 time chunk later.
    #TODO: Work Weekends. Employee will show up on the weekend. (and needs to be paid for those days)
    #-> Adjust the pay code for that.

    ## Supply Specific Duties ##
    global greymarket_deals_duty
    greymarket_deals_duty = Duty("Arrange Greymarket Deals",
        "Contact various less–than–reputable suppliers and arrange deals. Lowers cost of all supplies by purchased by this character by 25%, but increases Attention by 1 per turn.",
        on_turn_function = greymarket_deals_duty_on_turn)
    global alternative_payment_duty
    alternative_payment_duty = Duty("Alternative Payment Methods",
        "Convince vendors to provide Serum Supplies, using methods other than money to convince them. Reduces supply cost by 5% per Foreplay skill level. If Sluttiness is higher than 50, also add Oral skill.",
        requirement_function = alternative_payment_duty_requirement)

    ## R&D Specific Duties ##
    global theoretical_research_duty
    theoretical_research_duty = Duty("Theoretical Research",
        "Read cutting edge research papers and propose novel ideas to management. Generate 1 Clarity for every 5 Research Points generated.",
        requirement_function = theoretical_research_duty_requirement)
    global research_journal_subscription_duty
    research_journal_subscription_duty = Duty("Journal Studies",
        "Read academic journals, a critical task to keep abreast of the most recent developments in the field. Generates 1 Clarity for every 5 Research Points generated. Costs $10 per day in journal subscription fees.",
        requirement_function = research_journal_subscription_duty_requirement,
        on_apply_function = research_journal_on_apply,
        on_remove_function = research_journal_on_remove)
    global practical_experimentation_duty
    practical_experimentation_duty = Duty("Practical Experimentation",
        "Formulate novel hypotheses, test them, and produce research reports. Generates 1 Clarity for every 5 Research Points generated, at the cost of 5 Serum Supply per turn.",
        requirement_function = practical_experimentation_duty_requirement)
    global IT_work_duty
    IT_work_duty = Duty("Assist IT",
        "While working in Research and Development, have the employee assist with developing new IT projects.",
        requirement_function = IT_work_duty_requirement,
        on_turn_function = IT_work_duty_on_turn,
        only_at_work = True)
    global head_researcher_duty
    head_researcher_duty = Duty("Provide Research Expertise",
        "Direct research efforts and provide high level assistance to all members of the R&D team. Provides a 5% bonus to Research Points produced per point of Int above 2. Int below 2 instead produces a penalty of 5% per missing point.")

    ## Production work duties ##
    global bend_safety_rules_duty
    bend_safety_rules_duty = Duty("Bend Safety Rules",
        "Safety equipment that gets in the way of productivity should be ignored. This employee will produce an additional 10% productivity, but may occasionally dose themselves with a serum being produced, when this happens, her happiness will decrease by 2 points.",
        on_turn_function = bend_safety_rules_on_turn)
    global quality_control_duty
    quality_control_duty = Duty("Production Quality Control",
        "Employee will check quality of produced serums to verify that quality standards are met, taking pride in her work will improve her happiness by 2 points each shift. There is a chance she will be accidentally dosed with the serum, when this happens, her happiness will decrease by 2 points.",
        on_day_function = production_quality_control_on_day)

    ## Market Specific Duties ##
    global client_demonstration_duty
    client_demonstration_duty = Duty("Client Demonstrations",
        "Provide practical demonstrations of serum effects to clients on demand. Increases Market reach by 2*Foreplay skill, with a small chance each turn to be given a dose of serum currently in production.",
        requirement_function = client_demonstration_duty_requirement,
        on_turn_function = client_demonstration_duty_on_turn)
    global work_for_tips_duty
    work_for_tips_duty = Duty("Arouse Potential Clients",
        "Take advantage of the male dominated market by teasing and arousing potential clients when possible. Adds Foreplay skill to Marketing skill. If Sluttiness is higher than 50, also adds Oral skill.",
        requirement_function = work_for_tips_duty_requirement)

    # TODO: Seductive Deal Making. Increases serum value based on Foreplay skill. Requires some level of Sluttiness
    # TODO: Management Eye Candy. Strip tease for management on demand. Requires some level of Sluttiness or Opinions
    # TODO: Secretive Marketing. Actively lowers attention by a small amount.
    # TODOx2: Some way of using your girls as a bribe to lower attention even more at high Sluttiness.

    ## HR Specific Duties##
    # TODO: Personal secretary specific duties.
    global find_infractions_duty
    find_infractions_duty = Duty("Find Infractions",
        "Verify reports, check uniforms, and apply company regulations wherever possible. Base 5% chance to discover an infraction every turn. Less likely to generate infractions for high Obedience employees and friends, more likely for lower Obedience and rival employees.",
        requirement_function = find_infractions_duty_requirement,
        on_turn_function = find_infractions_duty_on_turn)
    global encourage_loyalty_duty
    encourage_loyalty_duty = Duty("Encourage Staff Loyalty",
        "Talk to other staff, reminding them of the importance of loyalty and obedience around the office. Picks an employee with Obedience lower than this employee each turn and raises Obedience by 1.",
        on_turn_function = encourage_loyalty_duty_on_turn)
    global internal_propaganda_duty
    internal_propaganda_duty = Duty("Distribute Internal Propaganda",
        "Spread stories among the staff, highlighting the positive and likeable features of management. Picks an employee with Love lower than this employee each turn and raises Love by 1.",
        on_turn_function = internal_propaganda_duty_on_turn)
    global corrupt_work_chat_duty
    corrupt_work_chat_duty = Duty("Corrupt Work Chat Groups",
        "Share scandalous stories and links to porn while encouraging others within the company to do the same. Picks an employee with Sluttiness lower than this employee each turn and raises Sluttiness by 1.",
        on_turn_function = corrupt_work_chat_duty_on_turn)

    # V have these key off of the recruitment elements.
    # TODO: Add "Internal Propaganda" duty. Raises Love of someone within the company by 1 per day, up to this character's Love.
    # TODO: Add "Disciplinary Meetings" duty. Raises Obedience of someone within the company by 1 per day, up to this character's Obedience
    # TODO: Management Stress Relief. Requires some level of sluttiness, which determines what she'll do for you.

    # -> Stuff like "On Demand Stress Relief" to fuck them whenever, blowjobs at your desk, etc.
    # -> Also options to have them manage punishments (just consumes infractions and produces Obedience).

    global general_duties_list
    general_duties_list.extend((
        mandatory_breaks_duty,
        extra_paperwork_duty,
        daily_serum_dosage_duty,
        weekend_serum_dosage_duty,
        bureaucratic_nightmare_duty,
        social_media_advertising_duty,
        breast_milk_pump_1_duty,
        breast_milk_pump_2_duty,
        breast_milk_pump_3_duty))

    global general_rd_duties
    general_rd_duties.extend((
        heavy_research_work_duty,
        theoretical_research_duty,
        research_journal_subscription_duty,
        practical_experimentation_duty,
        IT_work_duty))

    global general_market_duties
    general_market_duties.extend((
        market_work_duty,
        heavy_market_work_duty,
        client_demonstration_duty,
        work_for_tips_duty))

    global general_supply_duties
    general_supply_duties.extend((
        supply_work_duty,
        heavy_supply_work_duty,
        greymarket_deals_duty,
        alternative_payment_duty))

    global general_production_duties
    general_production_duties.extend((
        production_work_duty,
        heavy_production_work_duty,
        bend_safety_rules_duty,
        quality_control_duty))

    global general_hr_duties
    general_hr_duties.extend((
        hr_work_duty,
        heavy_hr_work_duty,
        find_infractions_duty,
        encourage_loyalty_duty,
        internal_propaganda_duty,
        corrupt_work_chat_duty))
