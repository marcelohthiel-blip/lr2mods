from __future__ import annotations
import renpy
import builtins
from game.helper_functions.convert_to_string_ren import opinion_score_to_string
from game.helper_functions.random_generation_functions_ren import make_person
from game.major_game_classes.serum_related.serums._serum_traits_T3_ren import mind_control_agent
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.people.Erica.erica_role_definition_ren import erica_get_is_doing_yoga_sessions
from game.people.Sarah.HR_supervisor_definition_ren import get_HR_director_tag, set_HR_director_tag

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def HR_director_meeting_on_demand_requirement(person: Person):
    if not get_HR_director_tag("business_HR_meeting_on_demand", False):
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if get_HR_director_tag("business_HR_meeting_last_day", 0) >= day:
        return "One meeting per day"
    return True

def HR_director_coffee_tier_1_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if get_HR_director_tag("business_HR_coffee_tier", 0) != 0:
        return False
    if get_HR_director_tag("business_HR_serum_tier", 0) == 0:
        return False
    if not mc.business.has_funds(500):
        return "Requires: $500"
    return True

def HR_director_coffee_tier_2_requirement(person: Person):
    if get_HR_director_tag("business_HR_coffee_tier", 0) != 1:
        return False
    if get_HR_director_tag("business_HR_serum_tier", 0) <= 1:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if not mc.business.has_funds(1500):
        return "Requires: $1,500"
    return True

def HR_director_gym_membership_tier_1_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if mc.business.employee_count > 6 and get_HR_director_tag("business_HR_gym_tier", 0) == 0:
        return True
    return False

def HR_director_gym_membership_tier_2_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if mc.business.employee_count > 14 and get_HR_director_tag("business_HR_gym_tier", 0) == 1:
        return True
    return False

def HR_director_mind_control_requirement(person: Person):
    if get_HR_director_tag("business_HR_serum_tier", 0) != 3:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if not mc.business.has_funds(5000):
        return "Requires: $5,000"
    return True

def HR_director_mind_control_attempt_requirement(person: Person):
    if get_HR_director_tag("business_HR_serum_tier", 0) < 4:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if get_HR_director_tag("business_HR_meeting_last_day", 0) >= day:
        return "One meeting per day"
    return True

def HR_director_change_relative_recruitment_requirement(person: Person):
    if get_HR_director_tag("business_HR_relative_recruitment", 0) == 0:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    return True

def HR_director_headhunt_initiate_requirement(person: Person):
    if not get_HR_director_tag("business_HR_headhunter_initial", False):
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if get_HR_director_tag("business_HR_headhunter_progress", 0) != 0:
        return "Running a search"
    if mc.business.at_employee_limit:
        return "At employee limit"
    return True

def get_HR_director_role_actions():
    HR_director_meeting_on_demand_action = Action("Meet with employee {image=time_advance}", HR_director_meeting_on_demand_requirement, "HR_director_meeting_on_demand_label",
        menu_tooltip = "Arrange a meeting with an employee")
    HR_director_coffee_tier_1_action = Action("Add serum to coffee\n{menu_red}Costs: $500{/menu_red}", HR_director_coffee_tier_1_requirement, "HR_director_coffee_tier_1_label",
        menu_tooltip = "Costs $500 but makes Monday HR meetings more impactful.")
    HR_director_coffee_tier_2_action = Action("Add stronger serum to coffee\n{menu_red}Costs: $1,500{/menu_red}", HR_director_coffee_tier_2_requirement, "HR_director_coffee_tier_2_label",
        menu_tooltip = "Costs $1500 but makes Monday HR meetings impactful.")
    HR_director_gym_membership_tier_1_action = Action("Sponsor company gym membership\n{menu_red}Costs: $5 per employee/per week{/menu_red}", HR_director_gym_membership_tier_1_requirement, "HR_director_gym_membership_tier_1_label",
        menu_tooltip = "Costs money each week, but increases girls energy over time.")
    HR_director_gym_membership_tier_2_action = Action("Sponsor company health program\n{menu_red}Costs: $15 per employee/per week{/menu_red}", HR_director_gym_membership_tier_2_requirement, "HR_director_gym_membership_tier_2_label",
        menu_tooltip = "Costs money each week, but increases girls energy over time.")
    HR_director_mind_control_action = Action("Produce mind control serum\n{menu_red}Costs: $5,000{/menu_red}", HR_director_mind_control_requirement, "HR_director_mind_control_label",
        menu_tooltip = "Costs $5000. Allows you to attempt mind control of employee.")
    HR_director_mind_control_attempt = Action("Attempt Mind Control {image=time_advance}", HR_director_mind_control_attempt_requirement, "HR_director_mind_control_attempt_label",
        menu_tooltip = "WARNING: May have side effects!")
    HR_director_change_relative_recruitment_action = Action("Change recruitment signage", HR_director_change_relative_recruitment_requirement, "HR_director_change_relative_recruitment_label",
        menu_tooltip = "Changes how often employees ask for employment for their daughters")
    HR_director_headhunt_initiate_action = Action("Initiate employee search", HR_director_headhunt_initiate_requirement, "HR_director_headhunt_initiate_label",
        menu_tooltip = "Try and find a new employee for a specific job")

    return [HR_director_meeting_on_demand_action, HR_director_coffee_tier_1_action, HR_director_coffee_tier_2_action, HR_director_gym_membership_tier_1_action, HR_director_gym_membership_tier_2_action, HR_director_mind_control_action, HR_director_mind_control_attempt, HR_director_change_relative_recruitment_action, HR_director_headhunt_initiate_action]

def init_HR_directore_roles():
    global HR_director_role
    HR_director_role = Role("HR Director", get_HR_director_role_actions()) #Actions go in block

def calculate_backfire_odds():
    serum_trait = next((x for x in list_of_traits if x == mind_control_agent), None)
    if serum_trait:
        return builtins.int(serum_trait.base_side_effect_chance / serum_trait.mastery_level)
    return 100

def create_HR_review_topic_list(person: Person):
    topic_list = ["working"]
    if person in mc.business.production_team:
        topic_list.append("production work")
    if person in mc.business.hr_team:
        topic_list.append("HR work")
    if person in mc.business.research_team:
        topic_list.append("research work")
    if person in mc.business.market_team:
        topic_list.append("marketing work")
    if person in mc.business.supply_team:
        topic_list.append("supply work")
    if get_HR_director_tag("business_HR_uniform", False):
        topic_list.append("work uniforms")
    if get_HR_director_tag("business_HR_skimpy_uniform", False):
        topic_list.append("skimpy uniforms")
    if get_HR_director_tag("business_HR_gym_tier", 0) > 1: # unlocks after health program
        topic_list.append("sports")
    if erica_get_is_doing_yoga_sessions():
        topic_list.append("yoga")
    return topic_list

def hr_director_mind_control_update_opinions(person: Person):
    topic_list = create_HR_review_topic_list(person)
    for topic in topic_list:
        person.increase_opinion_score(topic)

def build_HR_interview_discussion_topic_menu(person: Person, max_opinion = 0):
    opinion_list = create_HR_review_topic_list(person)
    opinion_chat_list = []
    for opinion in opinion_list:
        if person.opinion(opinion) < max_opinion:
            title_desc = opinion.title() + "\n{size=14}" + "She " + opinion_score_to_string(person.opinion(opinion)) + " it{/size}"
            opinion_chat_list.append((title_desc, opinion))

    opinion_chat_list.insert(0, "Discuss Topic")
    return opinion_chat_list

def get_HR_review_list(excluded_person: Person, max_opinion = 0):   #Pass in the HR director so we don't try to counsel her
    people_list = []
    for person in [x for x in mc.business.employees_at_office if x is not excluded_person]:
        topic_list = create_HR_review_topic_list(person)
        if any(x for x in topic_list if person.opinion(x) < max_opinion):
            people_list.append(person)
    return people_list

def build_HR_review_list(person: Person, max_opinion = 0):
    HR_tier_talk = -1 # init at -1 so we do the first collect with 0
    HR_employee_list = []
    # build list of girls that qualify for specified tier and max_tier score
    while builtins.len(HR_employee_list) == 0 and HR_tier_talk < get_HR_director_tag("business_HR_coffee_tier", 0) and HR_tier_talk < max_opinion:
        HR_tier_talk += 1
        HR_employee_list = get_HR_review_list(person, HR_tier_talk)
    return (HR_employee_list, HR_tier_talk)

def build_HR_mc_list(person: Person):
    HR_employee_list = []
    HR_employee_list = get_HR_review_list(person, max_opinion = 2)
    return HR_employee_list

def HR_director_initial_hire_requirement(hire_day):
    if time_of_day != 1 or day <= hire_day:
        return False
    return mc.business.is_open_for_business

def add_hr_director_initial_hire_action(person: Person):
    HR_director_initial_hire_action = Action("Hire HR Director", HR_director_initial_hire_requirement, "HR_director_initial_hire_label", args = person, requirement_args = day)
    mc.business.add_mandatory_crisis(HR_director_initial_hire_action)

def mind_control_backfire(person: Person):
    person.change_cha(-2)
    person.change_int(-2)
    person.change_focus(-2)
    # Use this function to create random backfire to person. Ideas: Bimbo, loss of stats, decrease all opinions.
    return "Backfire: Stat Loss"

def reset_headhunter_criteria():
    set_HR_director_tag("recruit_dept", None)
    set_HR_director_tag("recruit_obedience", None)
    set_HR_director_tag("recruit_focused", None)
    set_HR_director_tag("recruit_marital", None)
    set_HR_director_tag("recruit_slut", None)
    set_HR_director_tag("recruit_kids", None)
    set_HR_director_tag("recruit_age", None)
    set_HR_director_tag("recruit_bust", None)
    set_HR_director_tag("recruit_height", None)
    set_HR_director_tag("recruit_body", None)
    set_HR_director_tag("recruit_day", day)

def generate_HR_recruit():
    # department boosted stats
    main_stat = renpy.random.randint(Person.get_stat_floor() + 2, Person.get_stat_ceiling())
    main_skill = renpy.random.randint(Person.get_skill_floor() + 2, Person.get_skill_ceiling())

    main_stat += 1  # HR Boost
    main_skill += 1 # HR Boost
    other_stat = 0
    experience_stat = 0

    # extra boost / penalty for focused recruit
    if get_HR_director_tag("recruit_focused", False):
        main_stat += 2  # Focus Boost
        main_skill += 2 # Focus Boost
        other_stat = 2  # Focus Detractor
        experience_stat = 1  # Experience boost

    recruit = make_person(tits = get_HR_director_tag("recruit_bust", None),
        obedience = get_HR_director_tag("recruit_obedience", None),
        sluttiness = get_HR_director_tag("recruit_slut", None),
        relationship = get_HR_director_tag("recruit_marital", None),
        age = get_HR_director_tag("recruit_age", None),
        kids = get_HR_director_tag("recruit_kids", None),
        body_type = get_HR_director_tag("recruit_body", None),
        height = get_HR_director_tag("recruit_height", None),
        stat_range_array = [[Person.get_stat_floor() + 1, Person.get_stat_ceiling() + 1] for x in range(0, 3)],    # balanced stats
        skill_range_array = [[Person.get_skill_floor() + 1, Person.get_skill_ceiling() + 1] for x in range(0, 5)], # balanced skills
        sex_skill_range_array = [[Person.get_sex_skill_floor() + experience_stat, Person.get_sex_skill_ceiling() + experience_stat] for x in range(0, 4)],
        work_experience_range = [Person.get_work_experience_floor() + 1 + experience_stat, Person.get_work_experience_ceiling() + 1 + experience_stat])

    if get_HR_director_tag("recruit_dept") == "HR":
        recruit.charisma = main_stat
        recruit.hr_skill = main_skill
        recruit.focus -= other_stat
        recruit.focus = max(recruit.focus, 1)
        recruit.opinions["HR work"] = [2, True]
    elif get_HR_director_tag("recruit_dept") == "supply":
        recruit.focus = main_stat
        recruit.supply_skill = main_skill
        recruit.int -= other_stat
        recruit.int = max(recruit.int, 1)
        recruit.opinions["supply work"] = [2, True]
    elif get_HR_director_tag("recruit_dept") == "market":
        recruit.charisma = main_stat
        recruit.market_skill = main_skill
        recruit.int -= other_stat
        recruit.int = max(recruit.int, 1)
        recruit.opinions["marketing work"] = [2, True]
    elif get_HR_director_tag("recruit_dept") == "research":
        recruit.int = main_stat
        recruit.research_skill = main_skill
        recruit.charisma -= other_stat
        recruit.charisma = max(recruit.charisma, 1)
        recruit.opinions["research work"] = [2, True]
    elif get_HR_director_tag("recruit_dept") == "production":
        recruit.focus = main_stat
        recruit.production_skill = main_skill
        recruit.charisma -= other_stat
        recruit.charisma = max(recruit.charisma, 1)
        recruit.opinions["production work"] = [2, True]

    # discover some opinions
    for _x in builtins.range(0, 6):
        recruit.discover_opinion(recruit.get_random_opinion(include_known = False, include_sexy = True), add_to_log = False)

    return recruit

def HR_start_internship_program_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office and person.is_at_office

def add_HR_start_internship_program_action():
    mc.business.hr_director.add_unique_on_room_enter_event(Action("Discuss scholarship with HR",
        HR_start_internship_program_requirement, "HR_start_internship_program_label", priority = 30))
