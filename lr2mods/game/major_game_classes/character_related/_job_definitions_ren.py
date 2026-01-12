# LIST OF GENERIC JOBS #
from __future__ import annotations
import builtins
from game.game_roles._role_definitions_ren import unemployed_role, employee_role, college_intern_role, generic_student_role, prostitute_role, unimportant_job_role, critical_job_role, head_researcher, prod_assistant_role
from game.game_roles.business_roles._duty_definitions_ren import general_duties_list, general_hr_duties, general_supply_duties, general_market_duties, general_rd_duties, general_production_duties, hr_work_duty, market_work_duty, research_work_duty, head_researcher_duty, production_work_duty, supply_work_duty, daily_serum_dosage_duty
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.character_related.ActiveJob_ren import ActiveJob
from game.major_game_classes.character_related.JobDefinition_ren import JobDefinition
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Room_ren import strip_club, university, bdsm_room, downtown, mom_office_lobby, coffee_shop, downtown_bar, downtown_hotel, clothing_store, sex_store, electronics_store, office_store, mall, mall_salon, home_store, gym, hospital, gaming_cafe, ceo_office
from game.business_policies.serum_policies_ren import mandatory_paid_serum_testing_policy, mandatory_unpaid_serum_testing_policy
from game.game_roles.stripclub._stripclub_role_definitions_ren import stripclub_bdsm_performer_role, stripper_role, stripclub_stripper_role, stripclub_manager_role, stripclub_waitress_role, stripclub_mistress_role
from game.people.Jennifer.personal_secretary_role_definition_ren import personal_secretary_role
from game.game_roles.business_roles._business_role_definitions_ren import IT_director_role

list_of_jobs: list[tuple[JobDefinition, int]] = []
full_job_list: list[JobDefinition] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
def employee_salary_function(job: ActiveJob) -> float: #returns the default value this person should be worth on a per day basis.
    stat_value = (job.person.int + job.person.focus + job.person.charisma) * 2 + (job.person.hr_skill + job.person.market_skill + job.person.research_skill + job.person.production_skill + job.person.supply_skill)
    if job.job_definition in mc.business.hr_jobs:
        stat_value = (3 * job.person.charisma) + job.person.int + (2 * job.person.hr_skill)
    elif job.job_definition in mc.business.market_jobs:
        stat_value = (3 * job.person.charisma) + job.person.focus + (2 * job.person.market_skill)
    elif job.job_definition in mc.business.research_jobs:
        stat_value = (3 * job.person.int) + job.person.focus + (2 * job.person.research_skill)
    elif job.job_definition in mc.business.supply_jobs:
        stat_value = (3 * job.person.focus) + job.person.charisma + (2 * job.person.supply_skill)
    elif job.job_definition in mc.business.production_jobs:
        stat_value = (3 * job.person.focus) + job.person.int + (2 * job.person.production_skill)

    base_salary = stat_value * job.person.salary_modifier * (0.5 + 0.25 * job.seniority_level)
    if mandatory_paid_serum_testing_policy.is_owned:
        base_salary *= 1.1
    if mandatory_unpaid_serum_testing_policy.is_owned:
        base_salary *= 1.2
    return builtins.round(base_salary * job.wage_adjustment, 2)

def stripper_salary_func(job: ActiveJob) -> float:
    tit_modifier = 10 - (builtins.abs(5 - Person.rank_tits(job.person.tits)))   # optimal size is DD-Cup
    age_modifier = 8 - (builtins.abs(25 - job.person.age) / 3.0)            # optimal age is 25
    slut_modifier = job.person.sluttiness / 20.0
    obed_modifier = 0
    if job.person.has_role(stripclub_bdsm_performer_role):
        obed_modifier = (job.person.obedience - 100) / 20.0

    return builtins.round((job.person.charisma + tit_modifier + age_modifier + slut_modifier + obed_modifier) * 2 * job.wage_adjustment, 2)

def intern_salary_function(job: ActiveJob) -> float:
    return employee_salary_function(job) * .1

def init_job_list():
    global unemployed_job
    unemployed_job = JobDefinition("Unemployed", unemployed_role, day_slots = [], time_slots = [])

    ## HR Jobs ##
    global hr_job
    hr_job = JobDefinition("Personnel Manager", employee_role, job_location = mc.business.h_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.h_uniform,
        mandatory_duties = [hr_work_duty], available_duties = general_duties_list + general_hr_duties,
        base_salary_func = employee_salary_function, wage_adjustment = 1.1, is_paid = True)
    #TODO: Personal secretary job

    global personal_secretary_job
    personal_secretary_job = JobDefinition("Personal Secretary", [employee_role, personal_secretary_role], job_location = ceo_office,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.h_uniform,
        mandatory_duties = [hr_work_duty], available_duties = general_duties_list + general_hr_duties,
        base_salary_func = employee_salary_function, wage_adjustment = 1.1, is_paid = True)

    ## Market Jobs ##
    global market_job
    market_job = JobDefinition("Sales Representative", employee_role, job_location = mc.business.m_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.m_uniform,
        mandatory_duties = [market_work_duty], available_duties = general_duties_list + general_market_duties,
        base_salary_func = employee_salary_function, is_paid = True)

    ## R&D Jobs ##
    global head_researcher_job
    head_researcher_job = JobDefinition("Head Researcher", [employee_role, head_researcher], job_location = mc.business.r_div, seniority_level = 2,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.r_uniform,
        mandatory_duties = [research_work_duty, head_researcher_duty], available_duties = general_duties_list + general_rd_duties,
        base_salary_func = employee_salary_function, wage_adjustment = 1.1, is_paid = True)

    global rd_job
    rd_job = JobDefinition("R&D Scientist", employee_role, job_location = mc.business.r_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.r_uniform,
        seniority_level = 2, mandatory_duties = [research_work_duty], available_duties = general_duties_list + general_rd_duties,
        base_salary_func = employee_salary_function, is_paid = True)

    global IT_director_job
    IT_director_job = JobDefinition("IT Director", [employee_role, IT_director_role], job_location = mc.business.r_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.r_uniform,
        seniority_level = 2, mandatory_duties = [research_work_duty], available_duties = general_duties_list + general_rd_duties,
        base_salary_func = employee_salary_function, wage_adjustment = 1.2, is_paid = True)

    ## Supply Jobs ##
    global supply_job
    supply_job = JobDefinition("Logistics Manager", employee_role, job_location = mc.business.s_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.s_uniform,
        mandatory_duties = [supply_work_duty], available_duties = general_duties_list + general_supply_duties,
        base_salary_func = employee_salary_function, is_paid = True)

    ## Production Jobs ##
    global production_job
    production_job = JobDefinition("Production Line Worker", employee_role, job_location = mc.business.p_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.p_uniform,
        mandatory_duties = [production_work_duty], available_duties = general_duties_list + general_production_duties,
        base_salary_func = employee_salary_function, wage_adjustment = 1.2, is_paid = True)

    global production_assistant_job
    production_assistant_job = JobDefinition("Production Assistant", [employee_role, prod_assistant_role], job_location = mc.business.p_div,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3], wardrobe = mc.business.p_uniform,
        mandatory_duties = [production_work_duty], available_duties = general_duties_list + general_production_duties,
        base_salary_func = employee_salary_function, is_paid = True)

    # intern jobs
    global student_intern_rd_job
    student_intern_rd_job = JobDefinition("Biology Intern", [college_intern_role], job_location = mc.business.r_div,
        day_slots = [5], time_slots = [1, 2], wardrobe = mc.business.r_uniform,
        mandatory_duties = [research_work_duty], available_duties = general_duties_list + general_rd_duties,
        age_range = [Person.get_age_floor(), 24], base_salary_func = intern_salary_function, is_paid = True)
    global student_intern_production_job
    student_intern_production_job = JobDefinition("Chemistry Intern", [college_intern_role], job_location = mc.business.p_div,
        day_slots = [5], time_slots = [1, 2], wardrobe = mc.business.p_uniform,
        mandatory_duties = [production_work_duty], available_duties = general_duties_list + general_production_duties,
        age_range = [Person.get_age_floor(), 24], base_salary_func = intern_salary_function, is_paid = True)
    global student_intern_market_job
    student_intern_market_job = JobDefinition("Graphic Design Intern", [college_intern_role], job_location = mc.business.m_div,
        day_slots = [5], time_slots = [1, 2], wardrobe = mc.business.m_uniform,
        mandatory_duties = [market_work_duty], available_duties = general_duties_list + general_market_duties,
        age_range = [Person.get_age_floor(), 24], base_salary_func = intern_salary_function, is_paid = True)
    global student_intern_hr_job
    student_intern_hr_job = JobDefinition("Psychology Intern", [college_intern_role], job_location = mc.business.h_div,
        day_slots = [5], time_slots = [1, 2], wardrobe = mc.business.h_uniform,
        mandatory_duties = [hr_work_duty], available_duties = general_duties_list + general_hr_duties,
        age_range = [Person.get_age_floor(), 24], base_salary_func = intern_salary_function, is_paid = True)
    global student_intern_supply_job
    student_intern_supply_job = JobDefinition("Economics Intern", [college_intern_role], job_location = mc.business.s_div,
        day_slots = [5], time_slots = [1, 2], wardrobe = mc.business.s_uniform,
        mandatory_duties = [supply_work_duty], available_duties = general_duties_list + general_supply_duties,
        age_range = [Person.get_age_floor(), 24], base_salary_func = intern_salary_function, is_paid = True)
    global student_job
    student_job = JobDefinition("Student", generic_student_role, job_location = university,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2], age_range = [Person.get_age_floor(), 24]) #Note that this is different from Emily's Student role, which is really a "tutee" role.

    global stripper_job
    stripper_job = JobDefinition("Stripper", stripper_role, job_location = strip_club,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4], wardrobe = mc.business.stripper_wardrobe, age_range= [21, 42])
    global stripclub_stripper_job
    stripclub_stripper_job = JobDefinition("Stripper", stripclub_stripper_role, job_location = strip_club,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4], wardrobe = mc.business.stripper_wardrobe,
        mandatory_duties = [daily_serum_dosage_duty], base_salary_func = stripper_salary_func, is_paid = True)
    global stripclub_waitress_job
    stripclub_waitress_job = JobDefinition("Waitress", stripclub_waitress_role, strip_club,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4], wardrobe = mc.business.waitress_wardrobe,
        mandatory_duties = [daily_serum_dosage_duty], base_salary_func = stripper_salary_func, wage_adjustment = 0.6, is_paid = True)
    global stripclub_bdsm_performer_job
    stripclub_bdsm_performer_job = JobDefinition("BDSM Performer", stripclub_bdsm_performer_role, bdsm_room,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4], wardrobe = mc.business.bdsm_wardrobe,
        mandatory_duties = [daily_serum_dosage_duty], base_salary_func = stripper_salary_func, is_paid = True)
    global stripclub_manager_job
    stripclub_manager_job = JobDefinition("Manager", stripclub_manager_role, strip_club,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [2, 3, 4], wardrobe = mc.business.manager_wardrobe,
        mandatory_duties = [daily_serum_dosage_duty], base_salary_func = stripper_salary_func, wage_adjustment = 1.1, is_paid = True)
    global stripclub_mistress_job
    stripclub_mistress_job = JobDefinition("Mistress", stripclub_mistress_role, bdsm_room,
        day_slots=[0, 1, 2, 3, 4, 5, 6], time_slots = [2, 3, 4], wardrobe = mc.business.mistress_wardrobe,
        mandatory_duties = [daily_serum_dosage_duty], base_salary_func = stripper_salary_func, wage_adjustment = 1.1, is_paid = True)

    global prostitute_job
    prostitute_job = JobDefinition("Prostitute", prostitute_role, job_location = downtown,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4])
    prostitute_job.schedule.set_schedule(downtown_bar, [4, 5], [4]) # Friday and Saturday nights in the bar
    prostitute_job.schedule.set_schedule(downtown_hotel, [6], [3]) # Sunday evening at the hotel

    # Random city roles, with no specific stuff related to them.
    global secretary_job
    secretary_job = JobDefinition("Secretary", unimportant_job_role, job_location = mom_office_lobby,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])

    global barista_uniforms
    barista_uniforms = wardrobe_from_xml("Barista_Wardrobe")
    global barista_job
    barista_job = JobDefinition("Barista", unimportant_job_role, job_location = coffee_shop,
        day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2], wardrobe = barista_uniforms)
    global bartender_job
    bartender_job = JobDefinition("Bartender", unimportant_job_role, job_location = downtown_bar,
        day_slots = [2, 3, 4, 5, 6], time_slots = [3, 4])
    global waitress_job
    waitress_job = JobDefinition("Waitress", unimportant_job_role, job_location = downtown_bar,
        day_slots = [2, 3, 4, 5, 6], time_slots = [3, 4])

    global maid_uniforms
    maid_uniforms = wardrobe_from_xml("Maid_Wardrobe")
    global hotel_receptionist_job
    hotel_receptionist_job = JobDefinition("Receptionist", unimportant_job_role, job_location = downtown_hotel,
        day_slots = [2, 3, 4, 5, 6], time_slots = [1, 2])
    global hotel_maid_job
    hotel_maid_job = JobDefinition("Maid", unimportant_job_role, job_location = downtown_hotel,
        day_slots = [0, 2, 4, 6], time_slots=[1, 2, 3], wardrobe = maid_uniforms)
    global hotel_maid_job2
    hotel_maid_job2 = JobDefinition("Maid", unimportant_job_role, job_location = downtown_hotel,
        day_slots = [1, 3, 5], time_slots=[2, 3, 4], wardrobe = maid_uniforms)
    global hotel_chef_job
    hotel_chef_job = JobDefinition("Chef", unimportant_job_role, job_location = downtown_hotel,
        day_slots = [0, 2, 3, 4, 5, 6], time_slots = [2, 3])

    global clothing_cashier_job
    clothing_cashier_job = JobDefinition("Cashier", unimportant_job_role, job_location = clothing_store,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global sex_cashier_job
    sex_cashier_job = JobDefinition("Cashier", unimportant_job_role, job_location = sex_store,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global electronics_cashier_job
    electronics_cashier_job = JobDefinition("Cashier", unimportant_job_role, job_location = electronics_store,
        day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2])
    global electronics_support_job
    electronics_support_job = JobDefinition("Customer Support", unimportant_job_role, job_location = electronics_store,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global supply_cashier_job
    supply_cashier_job = JobDefinition("Cashier", unimportant_job_role, job_location = office_store,
        day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2])
    global home_improvement_cashier_job
    home_improvement_cashier_job = JobDefinition("Cashier", unimportant_job_role, job_location = home_store,
        day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2])
    global home_improvement_support_job
    home_improvement_support_job = JobDefinition("Customer Support", unimportant_job_role, job_location = home_store,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global salon_hairdresser_job
    salon_hairdresser_job = JobDefinition("Hairdresser", unimportant_job_role, job_location = mall_salon,
        day_slots=[1, 2, 3, 4, 5], time_slots = [1, 2])
    global store_assistant_job
    store_assistant_job = JobDefinition("Store Assistant", unimportant_job_role, job_location = mall,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global store_clerk_job
    store_clerk_job = JobDefinition("Store Clerk", unimportant_job_role, job_location = office_store,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global gym_instructor_job
    gym_instructor_job = JobDefinition("Gym Instructor", unimportant_job_role, job_location = gym,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global yoga_teacher_job
    yoga_teacher_job = JobDefinition("Yoga Teacher", unimportant_job_role, job_location = gym,
        day_slots = [0, 1, 2, 3, 4], time_slots = [2, 3])

    global nurse_uniforms
    nurse_uniforms = wardrobe_from_xml("Nurse_Wardrobe")
    global doctor_job
    doctor_job = JobDefinition("Doctor", critical_job_role, job_location = hospital,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2], wardrobe = "Nurse_Wardrobe", age_range = [28, Person.get_age_ceiling()])
    global nurse_job
    nurse_job = JobDefinition("Nurse", unimportant_job_role, job_location = hospital,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [1, 2, 3], wardrobe = nurse_uniforms, age_range = [23, 35])
    global night_nurse_job
    night_nurse_job = JobDefinition("Night Nurse", unimportant_job_role, job_location = hospital,
        day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [0, 3, 4], wardrobe = nurse_uniforms, age_range = [23, 35])

    global office_worker_job
    office_worker_job = JobDefinition("Office Worker", unimportant_job_role, job_location = mom_office_lobby,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global lawyer_job
    lawyer_job = JobDefinition("Lawyer", critical_job_role, job_location = mom_office_lobby,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2], age_range = [28, Person.get_age_ceiling()])
    global architect_job
    architect_job = JobDefinition("Architect", critical_job_role, job_location = downtown,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2], age_range = [28, Person.get_age_ceiling()])
    global interior_decorator_job
    interior_decorator_job = JobDefinition("Interior Decorator", critical_job_role, job_location = downtown,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global fashion_designer_job
    fashion_designer_job = JobDefinition("Fashion Designer", critical_job_role, job_location = downtown,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])
    global pro_gamer_job
    pro_gamer_job = JobDefinition("Pro Gamer", critical_job_role, job_location = gaming_cafe,
        day_slots = [3, 4, 5, 6], time_slots = [2, 3])
    global university_professor_job
    university_professor_job = JobDefinition("Professor", critical_job_role, job_location = university,
        day_slots = [0, 1, 2, 3, 4, 5], time_slots = [1, 2], age_range = [33, Person.get_age_ceiling()])

    global list_of_jobs
    list_of_jobs = [
        [unemployed_job, 20],
        [secretary_job, 3],
        [barista_job, 3],
        [bartender_job, 3],
        [waitress_job, 3],
        [hotel_receptionist_job, 3],
        [hotel_maid_job, 3],
        [hotel_maid_job2, 3],
        [hotel_chef_job, 3],
        [clothing_cashier_job, 3],
        [sex_cashier_job, 3],
        [electronics_cashier_job, 3],
        [electronics_support_job, 3],
        [supply_cashier_job, 3],
        [home_improvement_cashier_job, 3],
        [home_improvement_support_job, 3],
        [salon_hairdresser_job, 3],
        [store_assistant_job, 3],
        [store_clerk_job, 3],
        [gym_instructor_job, 3],
        [yoga_teacher_job, 3],
        [doctor_job, 2],
        [nurse_job, 3],
        [night_nurse_job, 3],
        [office_worker_job, 3],
        [lawyer_job, 2],
        [architect_job, 2],
        [interior_decorator_job, 2],
        [fashion_designer_job, 2],
        [pro_gamer_job, 2],
        [university_professor_job, 2],
    ]
    init_full_job_list()

def init_full_job_list():
    # list of non-random selectable jobs
    global full_job_list
    full_job_list = [x[0] for x in list_of_jobs]
    full_job_list.extend([
        unemployed_job,
        rd_job,
        head_researcher_job,
        market_job,
        hr_job,
        supply_job,
        production_job,
        prostitute_job,
        student_job,
        student_intern_rd_job,
        student_intern_production_job,
        student_intern_market_job,
        student_intern_hr_job,
        student_intern_supply_job,
        stripper_job,
        stripclub_stripper_job,
        stripclub_waitress_job,
        stripclub_bdsm_performer_job,
        stripclub_manager_job,
        stripclub_mistress_job,
    ])
