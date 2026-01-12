from __future__ import annotations
import builtins
import renpy
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.business_policies.organisation_policies_ren import office_punishment
from game.business_policies.serum_policies_ren import mandatory_paid_serum_testing_policy, mandatory_unpaid_serum_testing_policy
from game.business_policies.special_policies_ren import testing_room_creation_policy
from game.game_roles._role_definitions_ren import Role, generic_student_role
from game.major_game_classes.serum_related.serums.fetish_serums_ren import body_monitor_serum_is_unlocked
from game.major_game_classes.character_related.Person_ren import Person, mc, ashley, stephanie
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import university, clone_facility
from game.people.Ellie.IT_director_role_definition_ren import nanobot_program_is_IT
from game.people.Ashley.production_assistant_role_definition_ren import get_production_assistant_role_actions

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def init_business_roles():
    global employee_role
    employee_role = Role("Employee", get_employee_role_actions(),
        on_turn = employee_on_turn, on_move = employee_on_move, on_day = employee_on_day, hidden = True)
    global employee_busywork_role
    employee_busywork_role = Role("Office Busywork", [], hidden = True)
    employee_role.link_role(employee_busywork_role) #Link this role to the employee_role, so they are removed at the same time.
    global employee_humiliating_work_role
    employee_humiliating_work_role = Role("Humiliating Office Work", [], hidden = True)
    employee_role.link_role(employee_humiliating_work_role)
    global employee_freeuse_role
    employee_freeuse_role = Role("Freeuse Slut", get_freeuse_actions(), hidden = True)
    employee_role.link_role(employee_freeuse_role)
    global head_researcher
    head_researcher = Role("Head Researcher", get_head_researcher_actions(), hidden = True)
    global company_model_role
    company_model_role = Role("Company Model", get_company_model_role_actions())
    global college_intern_role
    college_intern_role = Role("College Intern", actions = get_college_intern_actions(), hidden = True, on_turn = college_intern_on_turn, on_move = college_intern_on_move, on_day = college_intern_on_day, looks_like = generic_student_role)
    global IT_director_role
    IT_director_role = Role("IT Director", get_IT_director_role_actions(), on_turn = IT_director_on_turn, on_move = IT_director_on_move, hidden = True)
    global prod_assistant_role
    prod_assistant_role = Role("Production Assistant", get_production_assistant_role_actions(), hidden = True)
    global clone_role
    clone_role = Role("Clone", actions = get_clone_role_actions())

def employee_set_duties_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False

    if person.get_event_day("work_duties_last_set") == day:
        return "Duties already changed today"
    return True

def employee_complement_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.get_event_day("day_last_employee_interaction") == day:
        return "Already interacted today"
    return True

def employee_insult_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.get_event_day("day_last_employee_interaction") == day:
        return "Already interacted today"
    return True

def employee_pay_cash_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.get_event_day("day_last_employee_interaction") == day:
        return "Already interacted today"
    return True

def employee_performance_review_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.current_job.days_employed < 7:
        return "Too recently hired"
    if person.has_event_day("day_last_performance_review") and person.days_since_event("day_last_performance_review") < 7:
        return "Too recently reviewed"
    return True

def move_employee_requirement(person: Person):
    if person == ashley:
        return "Locked for production assistant"
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    return True

def employee_punishment_hub_requirement(person: Person):
    if not office_punishment.is_active:
        return False
    if not mc.is_at_office or not person.is_at_office:
        return False
    if len(person.infractions) <= 0:
        return "Requires: Rules Infraction"
    if person.get_event_day("last_punished") == day:
        return "Already punished today"
    return True

def employee_find_out_home_location_requirement(person: Person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.is_unique:
        return False
    if person.obedience > 120 and person.effective_sluttiness() > 30:
        return not person.mc_knows_address
    return False

def employee_paid_serum_test_requirement(person: Person):
    if not person.is_at_office: # only active while at work
        return False
    if not mandatory_paid_serum_testing_policy.is_active or mandatory_unpaid_serum_testing_policy.is_active:
        return False
    if not mc.business.has_funds(100):
        return "Requires: $100"
    return True

def employee_unpaid_serum_test_requirement(person: Person):
    return person.is_at_office and mandatory_unpaid_serum_testing_policy.is_active

def get_employee_role_actions():
    #EMPLOYEE ACTIONS#
    employee_duty_set_action = Action("Set her work duties", employee_set_duties_requirement, "employee_set_duties_label",
        menu_tooltip = "Review and set her work duties.")
    move_employee_action = Action("Move her to a new division", move_employee_requirement, "move_employee_label",
        menu_tooltip = "Move her to a new division, where her skills might be put to better use.")
    employee_paid_serum_test = Action("Test serum\n{menu_red}Costs: $100{/menu_red}", employee_paid_serum_test_requirement, "employee_paid_serum_test_label",
        menu_tooltip = "Pay her to willingly take a dose of serum, per company policy.")
    employee_unpaid_serum_test = Action("Test serum\n{menu_green}No Costs{/menu_green}", employee_unpaid_serum_test_requirement, "employee_unpaid_serum_test_label",
        menu_tooltip = "Give her a dose of serum to test on herself, per company policy.")
    employee_complement_action = Action("Compliment her work", employee_complement_requirement, "employee_complement_work",
        menu_tooltip = "Offer a few kind words about her performance at work. Increases happiness and love, dependant on your charisma.")
    employee_insult_action = Action("Insult her work", employee_insult_requirement, "insult_recent_work",
        menu_tooltip = "Offer a few choice words about her performance at work. Lowers love and happiness, but is good for instilling obedience.")
    employee_pay_cash_action = Action("Pay her a cash bonus", employee_pay_cash_requirement, "employee_pay_cash_bonus",
        menu_tooltip = "A bonus in cold hard cash is good for obedience and happiness. The larger the reward the greater the effect.")
    employee_performance_review = Action("Start a performance review {image=time_advance}", employee_performance_review_requirement, "employee_performance_review",
        menu_tooltip = "Bring her to your office for a performance review. Get her opinion about her job, reward, punish, or fire her as you see fit. Can only be done once every seven days.")
    employee_punishment = Action("Punish her", employee_punishment_hub_requirement, "employee_punishment_hub",
        menu_tooltip = "Punish her for any violations of company policy.", priority = 5)
    employee_find_out_home_location_action = Action("{image=home_marker} Have a personal chat", employee_find_out_home_location_requirement, "employee_find_out_home_location_label",
        menu_tooltip = "Have a chat with an employee and find our more about her, including her home address.")

    return [employee_duty_set_action, employee_paid_serum_test, employee_unpaid_serum_test, employee_complement_action, employee_insult_action, employee_pay_cash_action, employee_performance_review, move_employee_action, employee_punishment, employee_find_out_home_location_action]

def quitting_crisis_requirement(person: Person): #We are only going to look at quitting actions if it is in the middle of the day when people are at work.
    return (time_of_day == 3
        and mc.business.is_work_day
        and mc.is_at_office
        and person.is_at_office)

def promotion_crisis_requirement(person: Person):
    return (time_of_day == 3
        and mc.business.is_work_day
        and mc.is_at_office
        and person.is_at_office
        and (
            not person.has_event_day("last_promotion_day")
            or person.days_since_event("last_promotion_day") >= 7
        ))

def employee_on_turn(person: Person):
    if not (mc.business.is_work_day and person.is_at_office and person.current_job): #Only thinks about quitting/asking for a promotion when she's at work
        return

    happy_points = person.current_job.job_happiness_score
    if (person.obedience < 220 and happy_points < 0
            and person.has_event_delay("last_quit_crisis_day", 7)
            and person.current_job.days_employed > 6):

        if not mc.business.has_queued_crisis("quitting_crisis_label") and renpy.random.randint(0, 100) < happy_points * -2: #She is quitting
            mc.business.add_mandatory_crisis(
                Action(f"{person.name} {person.last_name} is quitting",
                    quitting_crisis_requirement,
                    "quitting_crisis_label",
                    args = person, requirement_args = person)
            )

        else: #She's not quitting, but we'll let the player know she's unhappy
            warning_message = f"{person.name} {person.last_name} ({person.current_job.job_title}) is unhappy with her job and is considering quitting."
            if warning_message not in mc.business.message_list:
                mc.business.add_normal_message(warning_message)

    if (not mc.business.has_queued_crisis("request_promotion_crisis_label")
            and person.current_job.seniority_level < builtins.max(5, builtins.min(8, person.int))
            and person.current_job.days_employed >= (person.current_job.seniority_level * person.current_job.seniority_level * 4) + renpy.random.randint(8, 12)):
        #14 days, 26, 46, 74 days on average
        if renpy.random.randint(0, 100) < 5 - person.current_job.seniority_level: #ie. longer mean time between promotion requests by higher experience people
            mc.business.add_mandatory_crisis(
                Action(f"{person.name} {person.last_name} requests promotion",
                    promotion_crisis_requirement,
                    "request_promotion_crisis_label",
                    args = person, requirement_args = person)
            )

def employee_on_move(person: Person):
    return

def employee_on_day(person: Person):
    return

def freeuse_fuck_requirement(person: Person):
    return mc.business.is_open_for_business and mc.is_at_office and person.is_at_office

def get_freeuse_actions():
    #EMPLOYEE FREEUSE ACTIONS#
    freeuse_fuck = Action("Fuck her", freeuse_fuck_requirement, "employee_freeuse_fuck", menu_tooltip = "Grab your free use slut and have some fun with her.", priority = 10)
    return [freeuse_fuck]

def improved_serum_unlock_requirement(person: Person): #If the person is with their R&D head in the research division during work hours and they meet the sluttiness requirements you can
    if mc.business.research_tier != 0 or not mc.business.is_open_for_business:
        return False
    if not mc.is_at(mc.business.r_div):
        return False
    if person.obedience < 110 or person.int < 3:
        return "Requires: 110 Obedience, 3 Intelligence"
    if sum(1 for x in list_of_traits if x.tier == 0 and x.researched) < 5:
        return "Requires: 5 or more researched T0 traits"
    return True

def advanced_serum_stage_1_requirement(person: Person):
    if mc.business.research_tier != 1 or not mc.business.is_open_for_business:
        return False
    if mc.business.event_triggers_dict.get("advanced_serum_stage_1", False):
        return False
    if not mc.is_at(mc.business.r_div):
        return False
    if person.obedience < 120 or person.sluttiness < 25 or person.int < 4:
        return f"Requires: 120 Obedience, 4 Intelligence, {get_gold_heart(25)}"
    if sum(1 for x in list_of_traits if x.tier == 1 and x.researched) < 8:
        return "Requires: 8 or more researched T1 traits"
    return True

def advanced_serum_stage_3_requirement(person: Person):
    if mc.business.research_tier != 1 or not mc.business.is_open_for_business:
        return False
    if not mc.business.event_triggers_dict.get("advanced_serum_stage_3", False):
        return False
    if not mc.is_at(mc.business.r_div):
        return False
    if person.obedience < 120 or person.int < 4:
        return "Requires: 120 Obedience, 4 Intelligence"
    return True

def futuristic_serum_stage_1_requirement(person: Person):
    if mc.business.research_tier != 2 or not mc.business.is_open_for_business:
        return False
    if mc.business.event_triggers_dict.get("futuristic_serum_stage_1", False):
        return False
    if not mc.is_at(mc.business.r_div):
        return False
    if person.obedience < 140 or person.sluttiness < 50 or person.int < 5:
        return f"Requires: 140 obedience, 5 Intelligence, {get_gold_heart(50)}"
    if sum(1 for x in list_of_traits if x.tier == 2 and x.researched) < 6:
        return "Requires: 6 or more researched T2 traits"
    return True

def futuristic_serum_stage_2_requirement(person: Person):
    if mc.business.research_tier != 2 or not mc.business.is_open_for_business:
        return False
    if not mc.business.event_triggers_dict.get("futuristic_serum_stage_1", False):
        return False
    if not mc.is_at(mc.business.r_div):
        return False
    if person.obedience < 140 or person.sluttiness < 50 or person.int < 5:
        return f"Requires: 140 obedience, 5 Intelligence, {get_gold_heart(50)}"
    return True

def fire_head_researcher_requirement(person: Person): #Remove the person as your head researcher.
    return (mc.business.is_open_for_business
        and person.is_at_office
        and not mc.business.event_triggers_dict.get("Tutorial_Section", False)) #Block firing Steph during the Tutorial

def visit_nora_intro_requirement(person: Person):
    if mc.business.research_tier != 1 or not mc.business.is_open_for_business:
        return False
    if person != stephanie: #Only Stephanie gets to have this event trigger while she is head researcher.
        return False
    if not mc.business.event_triggers_dict.get("intro_nora", False):
        return False
    if not mc.is_at(mc.business.r_div) or university.visible: #This event is used to get to tier 2, so if you're already past that it doesn't matter.
        return False
    if mc.business.days_since_event("nora_contacted") <= 1:
        return "Wait for her to contact Nora"
    if person.love < 15:
        return "Requires: 15 Love"
    return True

def head_researcher_serum_trait_test_requirement(person: Person):
    if testing_room_creation_policy.is_active:
        if not (mc.is_at_office and mc.business.is_open_for_business):
            return False
        if mc.business.days_since_event("serum_trait_test") > TIER_1_TIME_DELAY:
            return True
        wait_time = TIER_1_TIME_DELAY - mc.business.days_since_event('serum_trait_test')
        if wait_time > 0:
            return f"Tested serum too recently [[{wait_time} {'day' if wait_time == 1 else 'days'} left]"
        return "Testing will be available tomorrow"
    return False

def fetish_serum_discuss_requirement(person: Person):
    if nanobot_program_is_IT():
        return False
    return mc.is_at_office and mc.business.is_open_for_business and body_monitor_serum_is_unlocked()


def get_head_researcher_actions():
    #HEAD RESEARCHER ACTIONS#
    improved_serum_unlock = Action("Ask about advancing your research", improved_serum_unlock_requirement, "improved_serum_unlock_label",
        menu_tooltip = "Your basic initial research can only take you so far. You will need a breakthrough to discover new serum traits.", priority = 40)

    visit_nora_intro = Action("Visit Nora to try and advance your research", visit_nora_intro_requirement, "nora_intro_label",
        menu_tooltip = "Have your head researcher reach out to your old mentor to see if she can help advance your research.", priority = 40)

    advanced_serum_unlock_stage_1 = Action("Ask about advancing your research", advanced_serum_stage_1_requirement, "advanced_serum_stage_1_label",
        menu_tooltip = "Another breakthrough will unlock new serum traits.", priority = 40)

    advanced_serum_unlock_stage_3 = Action("Present with recording of prototype serum test", advanced_serum_stage_3_requirement, "advanced_serum_stage_3_label",
        menu_tooltip = "Your new head researcher will have to take over now, and this recording should help them.", priority = 40)

    futuristic_serum_unlock_stage_1 = Action("Ask about advancing your research", futuristic_serum_stage_1_requirement, "futuristic_serum_stage_1_label",
        menu_tooltip = "You will need another breakthrough to unlock new serum traits.", priority = 40) #First time you ask about it

    futuristic_serum_unlock_stage_2 = Action("Talk about the test subjects", futuristic_serum_stage_2_requirement, "futuristic_serum_stage_2_label",
        menu_tooltip = "Your head researcher needs willing, dedicated test subjects to advance your research any further.", priority = 40) #Talk to her to either select test subjects or get a refresher on what you need.

    fire_head_researcher_action = Action("Remove her as head researcher", fire_head_researcher_requirement, "fire_head_researcher",
        menu_tooltip = "Remove her as your head researcher so you can select another. Without a head researcher your R&D department will be less efficient.")

    head_researcher_serum_trait_test_action = Action("Test a Serum Trait {image=time_advance}", head_researcher_serum_trait_test_requirement, "head_researcher_serum_trait_test_label",
        menu_tooltip = "Perform intensive serum trait test with the help of your head researcher on an employee.", priority = 5)

    fetish_serum_discuss_action = Action("Discuss Nanobot Program", fetish_serum_discuss_requirement, "fetish_serum_discuss_label",
        menu_tooltip = "Discuss creation / status of the Nanobot program.", priority = 5)

    return [fire_head_researcher_action, improved_serum_unlock, advanced_serum_unlock_stage_1, visit_nora_intro, advanced_serum_unlock_stage_3, futuristic_serum_unlock_stage_1, futuristic_serum_unlock_stage_2, head_researcher_serum_trait_test_action, fetish_serum_discuss_action]

def model_photography_list_requirement(person: Person):
    if not mc.business.is_open_for_business:
        return False
    if not person.is_at_office:
        return False
    if mc.business.has_sales_multiplier("Ad Campaign"):
        return "Advertisement is still running"
    if time_of_day >= 4:
        return "Too late to shoot pictures"
    if person.energy < 30:
        return "She's too tired to shoot pictures"
    if mc.energy < 30:
        return "Requires: 30 Energy"
    return True

def fire_model_requirement(person: Person):
    return person.is_at_office

def get_company_model_role_actions():
    #MODEL ACTIONS#
    model_ad_photo_list = Action("Shoot pictures for an advertisement {image=time_advance}", model_photography_list_requirement, "model_photography_list_label", priority = 5)

    fire_model_action = Action("Remove her as your company model", fire_model_requirement, "fire_model_label",
        menu_tooltip = "Remove her as your company model so you can give the position to someone else. Effects from existing ad campaigns will continue until they expire.")

    return [model_ad_photo_list, fire_model_action]

def college_intern_training_requirement(person: Person):
    return False # disabled until written
    #return person.is_at_office and not person.is_at(university)

def college_intern_set_duties_requirement(person: Person):
    if not person.is_at_office or person.is_at(university):
        return "Only in the office"

    if person.get_event_day("work_duties_last_set") == day:
        return "Duties already changed today"
    return True

def get_college_intern_actions():
    college_intern_training = Action("Train your intern", college_intern_training_requirement,
        "college_intern_training_label")
    college_intern_duty_set_action = Action("Set her work duties", college_intern_set_duties_requirement,
        "intern_set_duties_label", menu_tooltip = "Review and set her work duties.")
    college_intern_punishment = Action("Punish her", employee_punishment_hub_requirement,
        "employee_punishment_hub", menu_tooltip = "Punish her for any violations of company policy.", priority = 5)

    return [college_intern_training, college_intern_duty_set_action, college_intern_punishment]

def college_intern_on_turn(person: Person):
    return

def college_intern_on_day(person: Person):  #Use this to figure out when to end the internship
    return

def college_intern_on_move(person: Person):
    return


####################
# IT Director Role #
####################

def update_IT_projects_requirement(person: Person):
    return mc.business.it_director and mc.business.is_open_for_business

def IT_director_on_turn(person: Person):
    if person.is_at(mc.business.r_div):
        mc.business.IT_increase_project_progress(amount = (person.int * 2) + (person.focus))

def IT_director_on_move(person: Person):
    #     if mc.business.is_open_for_business and mc.business.current_IT_project:
    return

def get_IT_director_role_actions():
    update_IT_projects_action = Action("Review IT Projects", update_IT_projects_requirement, "update_IT_projects_label",
        menu_tooltip = "Start, change, activate, or deactivate IT projects.", priority = 5)

    return [update_IT_projects_action]

##############
# Clone Role #
##############
def clone_recall_requirement(person: Person):
    return person not in clone_facility.people

def clone_rent_apartment_requirement(person: Person):
    if person.home != clone_facility or person.location != clone_facility:
        return False
    if not mc.business.has_funds(25000):
        return "Requires: $25,000"
    return True

def get_clone_role_actions():
    clone_recall_action = Action("Recall clone", clone_recall_requirement, "clone_recall_label", menu_tooltip = "Bring the clone back to the facility for modifications")
    clone_rent_apartment_action = Action("Rent Apartment\n{menu_red}Costs: $25000{/menu_red}", clone_rent_apartment_requirement, "clone_rent_apartment_label", menu_tooltip = "Rent a apartment for your clone.")

    return [clone_recall_action, clone_rent_apartment_action]

clone_role = Role("Clone", actions = get_clone_role_actions())


########################
# Family Employee Role #
########################

def family_employee_on_turn(person: Person):
    return

def family_employee_on_day(person: Person):
    return

def family_employee_set_work_title(person: Person):
    if not person.event_triggers_dict.get("work_title_active", True):
        family_employee_store_current_home_title(person)
        person.set_title(person.event_triggers_dict.get("work_title", "mom"))
        person.set_mc_title(person.event_triggers_dict.get("work_mc_title", "Boss"))
        person.event_triggers_dict["work_title_active"] = True

def family_employee_set_default_title(person: Person):
    if person.event_triggers_dict.get("work_title_active", False):
        family_employee_store_current_work_title(person)
        person.set_title(person.event_triggers_dict.get("home_title", "mom"))
        person.set_mc_title(person.event_triggers_dict.get("home_mc_title", "Boss"))
        person.event_triggers_dict["work_title_active"] = False

def family_employee_store_current_home_title(person: Person):
    person.event_triggers_dict["home_title"] = person.title
    person.event_triggers_dict["home_mc_title"] = person.mc_title

def family_employee_store_current_work_title(person: Person):
    person.event_triggers_dict["work_title"] = person.title
    person.event_triggers_dict["work_mc_title"] = person.mc_title

def family_employee_on_move(person: Person):
    if not person.event_triggers_dict.get("use_work_titles", False):
        return
    if person.is_at_office:
        family_employee_set_work_title(person)
    else:
        family_employee_set_default_title(person)

family_employee_role = Role("Family Employee", [],
    on_turn = family_employee_on_turn,
    on_move = family_employee_on_move,
    on_day = family_employee_on_day, hidden = True)

def add_family_employee_role(person: Person, work_title: str, work_mc_title: str):
    family_employee_store_current_home_title(person)
    person.event_triggers_dict["use_work_titles"] = True
    person.event_triggers_dict["work_title_active"] = False
    person.event_triggers_dict["work_title"] = work_title
    person.event_triggers_dict["work_mc_title"] = work_mc_title
    person.add_role(family_employee_role)
    family_employee_set_work_title(person)
