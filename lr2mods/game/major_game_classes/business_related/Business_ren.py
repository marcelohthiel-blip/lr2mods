from __future__ import annotations
import builtins
from functools import cached_property
import renpy
from game.bugfix_additions.mapped_list_ren import MappedList
from game.helper_functions.list_functions_ren import all_IT_projects, all_people_in_the_game, all_policies_in_the_game, people_with_job
from game.business_policies.clothing_policies_ren import maximal_arousal_uniform_policy, corporate_enforced_nudity_policy, minimal_coverage_uniform_policy, reduced_coverage_uniform_policy, casual_uniform_policy, relaxed_uniform_policy, strict_uniform_policy
from game.business_policies.recruitment_policies_ren import recruitment_policies_list
from game.business_policies.organisation_policies_ren import attention_floor_increase_1_policy, attention_floor_increase_2_policy
from game.game_roles.business_roles._duty_definitions_ren import extra_paperwork_duty, work_for_tips_duty, heavy_market_work_duty
from game.game_roles.business_roles._business_role_definitions_ren import company_model_role, IT_director_role, family_employee_role, college_intern_role
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.ListenerManagementSystem_ren import ListenerManagementSystem
from game.major_game_classes.game_logic.Room_ren import Room, list_of_places
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, head_researcher_job, market_job, rd_job, production_job, supply_job, hr_job, student_intern_rd_job, student_intern_market_job, student_intern_production_job, student_intern_supply_job, student_intern_hr_job, stripper_job, stripclub_stripper_job, stripclub_waitress_job, stripclub_bdsm_performer_job, personal_secretary_job, IT_director_job, production_assistant_job
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_people, town_relationships, kaya
from game.major_game_classes.clothing_related.UniformOutfit_ren import UniformOutfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits
from game.major_game_classes.business_related._contracts_ren import generate_contract, generate_story_contracts
from game.major_game_classes.business_related.ProductionLine_ren import ProductionLine
from game.major_game_classes.business_related.Contract_ren import Contract
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.serum_related.SerumInventory_ren import SerumInventory
from game.plotlines.StripClub.stripclub_outfit_ren import StripClubOutfit
from game.people.Ashley.production_assistant_role_definition_ren import prod_assistant_role, cleanup_prod_assistant_meetings
from game.people.Ellie.IT_Business_Projects_ren import serum_creation_crisis_requirement, supply_inventory_project
from game.people.Ellie.IT_director_role_definition_ren import add_IT_Project_completed_action
from game.people.Ellie.IT_Project_class_ren import IT_Project
from game.people.Candace.candace_role_definition_ren import candace_calculate_discount
from game.people.Penelope.penelope_role_definition_ren import add_attention_event
from game.people.Sarah.HR_supervisor_role_definition_ren import HR_director_role
from game.people.Jennifer.personal_secretary_progression_scene_definition_ren import personal_secretary_prog_scene_action, personal_secretary_prog_scene

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class Business():
    # main jobs to start with:
    # 1) buying raw supplies.
    # 2) researching new serums.
    # 2a) The player (only) designs new serums to be researched.
    # 3) working in the lab to produce serums.
    # 4) Working in marketing. Increases volume you can sell, and max price you can sell for.
    # 5) Packaging and selling serums that have been produced.
    # 6) General secretary work. Starts at none needed, grows as your company does (requires an "HR", eventually). Maybe a general % effectiveness rating.
    def __init__(self, name, m_div, p_div, r_div, s_div, h_div):
        self.name = name
        self.funds = 2000 #Your starting wealth.

        self.bankrupt_days = 0 #How many days you've been bankrupt. If it hits the max value you lose.
        self.max_bankrupt_days = 3 #How many days you can be negative without loosing the game. Can be increased through research.

        self._m_div = m_div.identifier #The physical locations of all of the teams, so you can move to different offices in the future.
        self._p_div = p_div.identifier
        self._r_div = r_div.identifier
        self._s_div = s_div.identifier
        self._h_div = h_div.identifier

        # These wardrobes handle the department specific uniform stuff. A list of UniformOutfits is used to populate the uniform manager screen.
        self.m_uniform = Wardrobe(self.name + " Marketing Wardrobe")
        self.p_uniform = Wardrobe(self.name + " Production Wardrobe")
        self.r_uniform = Wardrobe(self.name + " Research Wardrobe")
        self.s_uniform = Wardrobe(self.name + " Supply Wardrobe")
        self.h_uniform = Wardrobe(self.name + " HR Wardrobe")

        self.business_uniforms: list[UniformOutfit] = [] #A list of UniformOutfits

        self.stripper_wardrobe = Wardrobe("Stripper Wardrobe")
        self.waitress_wardrobe = Wardrobe("Waitress Wardrobe")
        self.bdsm_wardrobe = Wardrobe("BDSM Performer Wardrobe")
        self.manager_wardrobe = Wardrobe("Manager Wardrobe")
        self.mistress_wardrobe = Wardrobe("Mistress Wardrobe")

        self.stripclub_uniforms: list[StripClubOutfit] = [] #A list of StripClubOutfits

        # special wardrobe that contains designed outfits for punishments
        self.punishment_wardrobe = Wardrobe("Punishment Wardrobe")

        #These are the serums given to the different departments if the daily serum dosage policy is researched.
        self.m_serum = None
        self.p_serum = None
        self.r_serum = None
        self.s_serum = None
        self.h_serum = None

        self.strippers_serum = None
        self.waitresses_serum = None
        self.bdsm_performers_serum = None
        self.manager_serum = None

        self.max_employee_count = 8

        self.supply_count = 50
        self.supply_goal = 250
        self.auto_sell_threshold = None
        self.marketability = 0
        #self.production_points = 0 Use to be used to store partial progress on serum. is now stored in the assembly line array
        self.team_effectiveness_temp = 0 #Used as a temporary store to track non-instant team effectiveness changes.
        self.team_effectiveness = 100 #Ranges from 50 (Chaotic, everyone functions at 50% speed) to 200 (masterfully organized). Normal levels are 100, special traits needed to raise it higher.
        self.base_effectiveness_cap = 100 #Max cap, can be raised.

        self.research_tier = 0 #The tier of research the main character has unlocked with storyline events. 0 is starting, 3 is max.
        self.max_serum_tier = 0 #The tier of serum you can produce in your lab. Mirrors research tiers.

        self.blueprinted_traits = [] #List of traits that we have built from trait blueprints.

        self.serum_designs: list[SerumDesign] = [] #Holds serum designs that you have researched.
        self.active_research_design = None #The current research (serum design or serum trait) the business is working on

        self.batch_size = 5 #How many serums are produced in each production batch

        self.recruitment_cost = 50

        self.inventory = SerumInventory()
        # Production lines now have their own class.
        self.production_lines: list[ProductionLine] = [] #Holds instances of Production Line. Default is 2, buying more production lines lets you produce serum designs in parallel (but no more than your default amount).
        self.production_lines.append(ProductionLine(self.inventory))
        self.production_lines.append(ProductionLine(self.inventory))

        self.max_active_contracts = 2
        self.active_contracts: list[Contract] = []

        self.max_offered_contracts = 2
        self.offered_contracts: list[Contract] = []

        # self.policy_list = [] #This is a list of Policy objects.
        # self.active_policy_list = [] #This is a list of currently active policies (vs just owned ones)

        self.message_list = [] #This list of strings is shown at the end of each day on the business update screen. Cleared each day.
        self.counted_message_list = {} #This is a dict holding the count of each message stored in it. Used when you want to have a message that is counted and the total shown at the end of the day.
        self.production_potential = 0 #How many production points the team was capable of
        self.supplies_purchased = 0
        self.production_used = 0 #How many production points were actually used to make something.
        self.research_produced = 0 #How much research the team produced today.
        self.sales_made = 0
        self.serums_sold = 0

        self.partial_clarity = 0.0 #Float used to store partial clarity produced by research until it can be given out as a full integer.

        self.sales_multipliers: list[tuple[str, float]] = [] #This list holds ["Source_type",multiplier_as_float]. The multiplier is applied to the value of serums when they are sold.
        # Only the most positive modifier of any source type is used. (This means a 1.0 modifier can be used to replace a negative modifier).

        self.mandatory_crises_list = ActionList() #A list of crises to be resolved at the end of the turn, generally generated by events that have taken place.
        self.mandatory_morning_crises_list = ActionList() #A list of specifically morning crises that need to be resolved.

        self.event_triggers_dict = {} #This dictionary will be used to hold flags for story events and triggers. In general a string is the key and a bool is the value stored.
        self.event_triggers_dict["policy_tutorial"] = 1 #We have a policy tutorial.
        self.event_triggers_dict["research_tutorial"] = 1 #We have a research tutorial.
        self.event_triggers_dict["design_tutorial"] = 1 #We have a serum design tutorial.
        self.event_triggers_dict["production_tutorial"] = 1 #We have a production tutorial.
        self.event_triggers_dict["outfit_tutorial"] = 1 #We have an outfit design tutorial.
        self.event_triggers_dict["hiring_tutorial"] = 1 #We have an outfit design tutorial.

        self.market_reach = 100 #"market_reach" can be thought of as your total customer base.
        self.mental_aspect_sold = 0 #Customers only have so much need for serum, so as you sell aspects the price per aspect goes down. You need to increase your market reach to get that price back up.
        self.physical_aspect_sold = 0
        self.sexual_aspect_sold = 0
        self.medical_aspect_sold = 0

        self.default_aspect_price = 10 # THis is the starting price that most aspects are "worth".
        self.aspect_price_max_variance = 8 # This is the total amount each aspect can be worth (ie no aspect is ever worth base more than 18 or less than 2).
        self.aspect_price_daily_variance = 2 #This is the +- amount the price of each aspect can fluctuate.

        self.mental_aspect_price = self.default_aspect_price #These are the actual current values of each aspect, which will vary from day-to-day
        self.physical_aspect_price = self.default_aspect_price
        self.sexual_aspect_price = self.default_aspect_price
        self.medical_aspect_price = self.default_aspect_price

        self.flaws_aspect_cost = -10 #NOTE: Flaws are a flat -10 each, _not_ reduced by amount sold.

        self.attention = 0 #Current attention.
        self.max_attention = 100 #If you end the day over this much attention you trigger a high attention event.
        self.attention_bleed = 10 #How much attention is burned each day,

        self.operating_costs = 0 #How much money is spent every work day just owning your lab.
        self.paid_salaries = 0 #Store for daily salaries paid
        self.standard_efficiency_drop = 1 #How much efficiency drops per employee per turn at work.

        self.listener_system = ListenerManagementSystem()

        self._active_policy_list = MappedList(Policy, all_policies_in_the_game)
        self._policy_list = MappedList(Policy, all_policies_in_the_game)
        self._active_IT_project_map = MappedList(IT_Project, all_IT_projects)
        self._IT_project_map = MappedList(IT_Project, all_IT_projects)
        self._partial_IT_projects: dict[int, int] = {}
        self._current_IT_project: int = None
        self.current_IT_project_progress = 0
        self._head_researcher = None
        self._hr_director = None
        self._it_director = None
        self._prod_assistant = None
        self._company_model = None
        self._personal_secretary = None
        self._research_team = MappedList(Person, all_people_in_the_game)
        self._market_team = MappedList(Person, all_people_in_the_game)
        self._supply_team = MappedList(Person, all_people_in_the_game)
        self._production_team = MappedList(Person, all_people_in_the_game)
        self._hr_team = MappedList(Person, all_people_in_the_game)
        self._funds_yesterday = self.funds
        self._unisex_restroom_unlocks = {}
        self.college_interns_unlocked = False
        self.max_interns_by_division = 3

        # init dict
        self.event_triggers_dict["coffee_shop_buy_coffee_day"] = -1

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: Business) -> bool:
        if not isinstance(other, Business):
            return NotImplemented
        return self.name == other.name

    def __getstate__(self): # excludes decorators from serialization
        state = self.__dict__.copy()
        for x in Business._clear_employee_cache_keys:
            state.pop(x, None)
        return state

    @property
    def active_policy_list(self) -> list[Policy]:
        return self._active_policy_list

    @property
    def policy_list(self) -> list[Policy]:
        return self._policy_list

    @property
    def active_IT_projects(self) -> list[IT_Project]:
        return self._active_IT_project_map

    @property
    def IT_projects(self) -> list[IT_Project]:
        return self._IT_project_map

    @property
    def IT_partial_projects(self) -> tuple[int, int]:
        return self._partial_IT_projects

    @property
    def current_IT_project(self) -> IT_Project:
        return IT_Project.get_by_identifier(self._current_IT_project)

    @current_IT_project.setter
    def current_IT_project(self, value: IT_Project | None):
        self._current_IT_project = None
        if isinstance(value, IT_Project):
            self._current_IT_project = value.identifier

    def IT_increase_project_progress(self, amount = 0, add_to_log = False):
        if not self.current_IT_project:
            return

        self.current_IT_project_progress += amount
        if add_to_log:
            mc.log_event(f"+{amount:.0f} IT Project Progress", "float_text_green")
        if self.current_IT_project_progress >= self.current_IT_project.project_cost:
            self.IT_unlock_project(self.current_IT_project)
            add_IT_Project_completed_action(self.current_IT_project)
            self.current_IT_project = None
            self.current_IT_project_progress = 0
        return

    def IT_unlock_project(self, project: IT_Project = None, add_to_log = True):
        if project and project not in self.IT_projects:
            self.IT_projects.append(project)
            project.apply_policy()  # enable project at completion

            if add_to_log:
                mc.log_event(project.name + " IT Project Complete!", "float_text_green")

    def IT_project_is_active(self, project: IT_Project | str) -> bool:
        if isinstance(project, str):
            return any(x for x in self.active_IT_projects if x.name == project)
        return project in self.active_IT_projects

    @cached_property
    def m_div(self) -> Room:
        return next((x for x in list_of_places if x.identifier == self._m_div), None)

    @cached_property
    def p_div(self) -> Room:
        return next((x for x in list_of_places if x.identifier == self._p_div), None)

    @cached_property
    def r_div(self) -> Room:
        return next((x for x in list_of_places if x.identifier == self._r_div), None)

    @cached_property
    def s_div(self) -> Room:
        return next((x for x in list_of_places if x.identifier == self._s_div), None)

    @cached_property
    def h_div(self) -> Room:
        return next((x for x in list_of_places if x.identifier == self._h_div), None)

    @cached_property
    def head_researcher(self) -> Person:
        return Person.get_person_by_identifier(self._head_researcher)

    def _set_head_researcher(self, value):
        self._head_researcher = None
        self.__dict__.pop("head_researcher", None)
        if isinstance(value, Person):
            self._head_researcher = value.identifier

    @cached_property
    def hr_director(self) -> Person:
        return Person.get_person_by_identifier(self._hr_director)

    def _set_hr_director(self, value):
        self._hr_director = None
        self.__dict__.pop("hr_director", None)
        if isinstance(value, Person):
            self._hr_director = value.identifier

    @cached_property
    def personal_secretary(self) -> Person:
        return Person.get_person_by_identifier(self._personal_secretary)

    def _set_personal_secretary(self, value):
        self._personal_secretary = None
        self.__dict__.pop("personal_secretary", None)
        if isinstance(value, Person):
            self._personal_secretary = value.identifier

    @cached_property
    def it_director(self) -> Person:
        return Person.get_person_by_identifier(self._it_director)

    def _set_it_director(self, value):
        self._it_director = None
        self.__dict__.pop("it_director", None)
        if isinstance(value, Person):
            self._it_director = value.identifier

    @cached_property
    def prod_assistant(self) -> Person:
        return Person.get_person_by_identifier(self._prod_assistant)

    def _set_prod_assistant(self, value):
        self._prod_assistant = None
        self.__dict__.pop("prod_assistant", None)
        if isinstance(value, Person):
            self._prod_assistant = value.identifier

    @cached_property
    def company_model(self) -> Person:
        return Person.get_person_by_identifier(self._company_model)

    def _set_company_model(self, value):
        self._company_model = None
        self.__dict__.pop("company_model", None)
        if isinstance(value, Person):
            self._company_model = value.identifier

    _clear_employee_cache_keys = ("employee_list", "research_team", "market_team", "supply_team", "production_team", "hr_team",
        "intern_list", "college_interns_research", "college_interns_production", "college_interns_market", "college_interns_supply", "college_interns_HR",
        "stripclub_strippers", "stripclub_bdsm_performers", "stripclub_waitresses", "stripclub_employees")

    def _clear_employee_cache(self):
        '''
        Primarily called from Person class when changing job assignments (could impact cached properties)
        '''
        for key in self._clear_employee_cache_keys:
            self.__dict__.pop(key, None)

    @cached_property
    def research_team(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(self.research_jobs)]

    @cached_property
    def research_jobs(self) -> tuple[JobDefinition]:
        return (rd_job, head_researcher_job, IT_director_job)

    @cached_property
    def market_team(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(self.market_jobs)]

    @cached_property
    def market_jobs(self) -> tuple[JobDefinition]:
        return (market_job,)

    @cached_property
    def supply_team(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(self.supply_jobs)]

    @cached_property
    def supply_jobs(self) -> tuple[JobDefinition]:
        return (supply_job,)

    @cached_property
    def production_team(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(self.production_jobs)]

    @cached_property
    def production_jobs(self) -> tuple[JobDefinition]:
        return (production_job, production_assistant_job)

    @cached_property
    def hr_team(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(self.hr_jobs)]

    @cached_property
    def hr_jobs(self) -> tuple[JobDefinition]:
        return (hr_job, personal_secretary_job)

    @property
    def funds_yesterday(self) -> int:
        return self._funds_yesterday

    @funds_yesterday.setter
    def funds_yesterday(self, value: int):
        self._funds_yesterday = value

    @property
    def unisex_restroom_unlocks(self):
        return self._unisex_restroom_unlocks

    def run_turn(self): #Run each time the time segment changes. Most changes are done here.
        # efficiency drop for each employee without extra paperwork duty
        self.change_team_effectiveness(sum(-self.standard_efficiency_drop for x in self.employees_at_office if not x.has_duty(extra_paperwork_duty)))
        self.update_team_effectiveness()

        if self.active_research_design:
            self.event_triggers_dict["no_research"] = 0
        elif self.is_open_for_business:
            self.event_triggers_dict["no_research"] = self.event_triggers_dict.get("no_research", 0) + 1

        self.do_autosale() #Mark extra serums to be sold by marketing.

        for policy in self.active_policy_list:
            policy.on_turn()

    def run_move(self):
        for policy in self.active_policy_list:
            policy.on_move()

    def run_day(self): #Run at the end of the day.
        self.attention += -self.attention_bleed
        self.attention = max(self.attention, 0)

        #Pay everyone for the day
        if self.is_work_day:
            self.paid_salaries = self.calculate_salary_cost()
            self.change_funds(-self.paid_salaries, stat = "Salaries")
            self.change_funds(-self.operating_costs, stat = "Operational Costs")

            if self.attention >= self.max_attention and not self.event_triggers_dict.get("attention_event_pending", False):
                self.event_triggers_dict["attention_event_pending"] = True
                add_attention_event()

            for policy in self.active_policy_list:
                policy.on_day()

            for contract in self.active_contracts[:]:   # iterate over copy to allow for removal by complete/abandon
                if contract.run_day():
                    if contract.can_finish_contract:
                        self.complete_contract(contract)
                        self.add_normal_message(f"Contract {contract.name} was going to expire with product in inventory, completed automatically.")
                    else:
                        self.abandon_contract(contract)
                        self.add_normal_message(f"Contract {contract.name} has expired unfilled.")

            # baseline market skill value 8 restores 1% market demand
            restore_value = sum((x.market_skill + x.extra_market_skill) for x in self.market_team if x.is_available) / 800.0
            for design in self.serum_designs:
                design.restore_market_demand(restore_value)

        strip_club_income = self.calculate_strip_club_income()
        if strip_club_income != 0:
            self.change_funds(strip_club_income, stat = "Strip Club Income", add_to_log = False)
            self.add_normal_message(f"The [strip_club.formal_name] has made a net profit of ${strip_club_income:,.0f} today!")

        # reset some events
        self.event_triggers_dict["coffee_shop_buy_coffee_day"] = 0
        self.event_triggers_dict["glory_hole_wait"] = 0

        if day % 7 == 6: #ie is Monday
            self.renew_contracts()

    @property
    def is_open_for_business(self) -> bool:
        '''
        Returns True when business is open (employees are present)
        For now monday-friday -> timeslots 1, 2, 3
        '''
        if not self.is_work_day: #It is the weekend, people have the day off.
            return False
        return time_of_day in (1, 2, 3)

    @property
    def is_work_day(self) -> bool:
        '''
        Returns True for monday to friday
        '''
        return not self.is_weekend

    @property
    def is_weekend(self) -> bool:
        '''
        Returns True for saturday and sunday
        '''
        return day % 7 in (5, 6)

    def update_stripclub_wardrobes(self):
        def update_stripclub_uniform(wardrobe: Wardrobe, uniform: StripClubOutfit):
            if uniform.full_outfit_flag:
                wardrobe.add_outfit(uniform.outfit.get_copy())
            if uniform.overwear_flag:
                wardrobe.add_overwear_set(uniform.outfit.get_copy())
            if uniform.underwear_flag:
                wardrobe.add_underwear_set(uniform.outfit.get_copy())

        self.stripper_wardrobe.clear_wardrobe()
        self.waitress_wardrobe.clear_wardrobe()
        self.bdsm_wardrobe.clear_wardrobe()
        self.manager_wardrobe.clear_wardrobe()
        self.mistress_wardrobe.clear_wardrobe()

        for uniform in self.stripclub_uniforms:
            if uniform.stripper_flag:
                update_stripclub_uniform(self.stripper_wardrobe, uniform)
            if uniform.waitress_flag:
                update_stripclub_uniform(self.waitress_wardrobe, uniform)
            if uniform.bdsm_flag:
                update_stripclub_uniform(self.bdsm_wardrobe, uniform)
            if uniform.manager_flag:
                update_stripclub_uniform(self.manager_wardrobe, uniform)
            if uniform.mistress_flag:
                update_stripclub_uniform(self.mistress_wardrobe, uniform)

    def get_uniform_limits(self): #Returns three values: the max sluttiness of a full outfit, max sluttiness of an underwear set, and if only overwear sets are allowed or notself.
        slut_limit = 0
        underwear_limit = 0
        limited_to_top = True
        if maximal_arousal_uniform_policy.is_active:
            slut_limit = 999 #ie. no limit at all.
            underwear_limit = 999
            limited_to_top = False
        elif corporate_enforced_nudity_policy.is_active:
            slut_limit = 80
            underwear_limit = 999
            limited_to_top = False
        elif minimal_coverage_uniform_policy.is_active:
            slut_limit = 60
            underwear_limit = 30
            limited_to_top = False
        elif reduced_coverage_uniform_policy.is_active:
            slut_limit = 40
            underwear_limit = 15
            limited_to_top = False
        elif casual_uniform_policy.is_active:
            slut_limit = 30
            underwear_limit = 0
            limited_to_top = True
        elif relaxed_uniform_policy.is_active:
            slut_limit = 20
            underwear_limit = 0
            limited_to_top = True
        elif strict_uniform_policy.is_active:
            slut_limit = 10
            underwear_limit = 0
            limited_to_top = True
        return slut_limit, underwear_limit, limited_to_top

    def add_uniform_to_company(self, outfit, full_outfit_flag = False, overwear_flag = False, underwear_flag = False, research = True, production = True, supply = True, marketing = True, hr = True):
        uniform = UniformOutfit(outfit)
        if uniform.can_toggle_full_outfit_state:
            uniform.set_full_outfit_flag(full_outfit_flag)
        if uniform.can_toggle_overwear_state:
            uniform.set_overwear_flag(overwear_flag)
        if uniform.can_toggle_underwear_state:
            uniform.set_underwear_flag(underwear_flag)

        uniform.set_research_flag(research)
        uniform.set_production_flag(production)
        uniform.set_supply_flag(supply)
        uniform.set_marketing_flag(marketing)
        uniform.set_hr_flag(hr)

        self.business_uniforms.append(uniform)
        self.update_uniform_wardrobes()

    def update_uniform_wardrobes(self): #Rebuilds all uniforms in the wardrobe based on current uniform settings.
        def update_department_uniform(wardrobe: Wardrobe, uniform: UniformOutfit):
            if uniform.full_outfit_flag:
                wardrobe.add_outfit(uniform.outfit.get_copy())
            if uniform.overwear_flag:
                wardrobe.add_overwear_set(uniform.outfit.get_copy())
            if uniform.underwear_flag:
                wardrobe.add_underwear_set(uniform.outfit.get_copy())

        self.m_uniform.clear_wardrobe()
        self.p_uniform.clear_wardrobe()
        self.r_uniform.clear_wardrobe()
        self.s_uniform.clear_wardrobe()
        self.h_uniform.clear_wardrobe()

        for uniform in self.business_uniforms:
            if uniform.hr_flag:
                update_department_uniform(self.h_uniform, uniform)
            if uniform.research_flag:
                update_department_uniform(self.r_uniform, uniform)
            if uniform.production_flag:
                update_department_uniform(self.p_uniform, uniform)
            if uniform.supply_flag:
                update_department_uniform(self.s_uniform, uniform)
            if uniform.marketing_flag:
                update_department_uniform(self.m_uniform, uniform)

    def clear_messages(self): #clear all messages for the day.
        self.message_list = []
        self.counted_message_list = {}
        self.production_potential = 0
        self.supplies_purchased = 0
        self.production_used = 0
        self.research_produced = 0
        self.sales_made = 0
        self.serums_sold = 0

    def add_counted_message(self, message, new_count = 1):
        if message in self.counted_message_list:
            self.counted_message_list[message] += new_count
        else:
            self.counted_message_list[message] = new_count

    def add_normal_message(self, message): #Adds an uncounted message, only ever listed once per day
        if message not in self.message_list:
            self.message_list.append(message)

    @property
    def on_payroll(self) -> list[Person]:
        return [x for x in list_of_people if any(x for x in x.jobs if x.is_paid)]

    def calculate_salary_cost(self) -> float:
        salaries = sum(y.daily_wage for x in self.on_payroll for y in x.jobs if y.is_paid)
        return builtins.round(salaries, 2)

    def calculate_base_salaries(self) -> float:
        base_salaries = sum(y.salary for x in self.on_payroll for y in x.jobs if y.is_paid)
        return builtins.round(base_salaries, 2)

    def calculate_strip_club_income(self) -> int:
        income = 0
        if mc.owns_strip_club:
            for person in self.stripclub_employees:
                income += person.stripclub_profit
                income -= person.stripclub_salary

        income *= 1 + (len(self.stripclub_waitresses) / 10.0) # each waitress boost profits by 10%

        return builtins.int(income)  # round to whole dollars

    def add_serum_design(self, the_serum: SerumDesign):
        self.serum_designs.append(the_serum)
        mc.stats.change_tracked_stat("Business", "Serum Designs", 1)

    def remove_serum_design(self, the_serum: SerumDesign):
        self.serum_designs.remove(the_serum)
        if the_serum is self.active_research_design:
            self.active_research_design = None

        for line in self.production_lines:
            if line.selected_design == the_serum:
                line.clear_product()

    def remove_trait(self, trait: SerumTrait):
        self.blueprinted_traits.remove(trait)
        if trait is self.active_research_design:
            self.active_research_design = None

    def is_trait_researched(self, trait: SerumTrait | str):
        if isinstance(trait, str):
            research_trait = next((x for x in list_of_traits if x.name.startswith(trait)), None)
        else:
            research_trait = next((x for x in list_of_traits if x.name == trait.name), None)
        if research_trait:
            return research_trait.researched
        return False

    def set_serum_research(self, new_research):
        if callable(new_research):
            new_research = new_research() #Used by serumtrait.unlock_function's, particularly SerumTraitBlueprints to properly set the new trait.
        self.active_research_design = new_research

    def research_progress(self, intel: int, focus: int, skill: int, production_modifier = 1.0) -> float:
        research_amount = ((3 * intel) + focus + (2 * skill) + 10) * (self.team_effectiveness / 100.0) * production_modifier

        if self.head_researcher and self.head_researcher.is_at_work:
            bonus_percent = (self.head_researcher.int - 2) * 0.05
            research_amount *= (1.0 + bonus_percent) #Every point above int 2 gives a 5% bonus.
            self.add_normal_message(f"Head researcher {self.head_researcher.display_name}'s intelligence resulted in a {bonus_percent * 100:+.0f}% change in research produced.")
        elif not self.head_researcher:
            research_amount *= 0.9  # No head researcher is treated like int 0.
            self.add_normal_message("No head researcher resulted in a 10% reduction in research produced! Assign a head researcher at R&D!")

        if self.active_research_design is not None:
            the_research = self.active_research_design
            is_researched = the_research.researched # If it was researched before we added any research then we are increasing the mastery level of a trait (does nothing to serum designs)
            self.research_produced += research_amount
            if the_research.add_research(research_amount): #Returns true if the research is completed by this amount'
                if isinstance(the_research, SerumDesign):
                    side_effects = the_research.generate_side_effects() #The serum will generate any side effects that are needed.
                    self.mandatory_crises_list.append(Action("Research Finished Crisis", serum_creation_crisis_requirement, "serum_creation_crisis_label", args = [the_research, side_effects], priority=100)) #Create a serum finished crisis, it will trigger at the end of the round
                    self.add_normal_message(f"New serum design researched: {the_research.name}")
                    self.active_research_design = None
                elif isinstance(the_research, SerumTrait):
                    if is_researched: #We've researched it already, increase mastery level instead.
                        self.add_normal_message(f"Serum trait mastery improved: {the_research.name} -> {the_research.mastery_level:.1f}%")
                    else:
                        self.add_normal_message(f"New serum trait researched: {the_research.name}")
                        self.active_research_design = None #If it's a newly discovered trait clear it so we don't start mastering it without player input.

            mc.stats.change_tracked_stat("Business", "Research Amount", research_amount)

        return research_amount  # return for clarity duty calculations

    def supply_purchase(self, focus: int, cha: int, skill: int, production_modifier = 1.0, cost_modifier = 1.0) -> int:
        max_supply = ((5 * focus) + (3 * cha) + (3 * skill) + 20) * production_modifier * (self.team_effectiveness / 100.0)
        if (self.supply_count / (self.supply_goal or 1)) < 20 and self.supply_count < 250 and self.IT_project_is_active(supply_inventory_project):
            max_supply *= 1.25
        if max_supply + self.supply_count > self.supply_goal:
            max_supply = self.supply_goal - self.supply_count
            if max_supply <= 0:
                return 0

        max_supply = builtins.int(max_supply)

        self.change_funds(-(max_supply * cost_modifier * candace_calculate_discount()), stat = "Supplies", add_to_log = False)

        mc.stats.change_tracked_stat("Business", "Supplies Bought", max_supply)

        self.supply_count += max_supply
        self.supplies_purchased += max_supply #Used for end of day reporting
        return max_supply

    def sale_progress(self, cha: int, focus: int, skill: int, production_modifier = 1.0) -> int:
        amount_increased = builtins.int(((3 * cha) + focus + (2 * skill) + 20) * (self.team_effectiveness * 0.01) * production_modifier)
        self.market_reach += amount_increased

        mc.stats.change_tracked_stat("Business", "Market Reach", amount_increased)
        return amount_increased

    def production_progress(self, focus: int, intel: int, skill: int, production_modifier = 1.0) -> int:
        #First, figure out how many production points we can produce total. Subtract that much supply and mark that much production down for the end of day report.
        production_amount = builtins.int(((3 * focus) + intel + (2 * skill) + 10) * (self.team_effectiveness / 100.0) * production_modifier)
        self.production_potential += production_amount

        if production_amount > self.supply_count:
            production_amount = self.supply_count #Figure out our total available production, before we split it up between tasks (which might not have 100% usage!)

        for line in self.production_lines:
            supply_used = line.add_production(production_amount) #NOTE: this is modified by the weighted use of the Line in particular. This allows for greater than 100% efficiency.
            self.supply_count -= supply_used
            self.production_used += supply_used
            mc.stats.change_tracked_stat("Business", "Production Amount", supply_used)

        return production_amount

    def hr_progress(self, cha: int, intel: int, skill: int, production_modifier = 1.0, instant_effect = False) -> int: #Don't compute efficiency cap here so that player HR effort will be applied against any efficiency drop even though it's run before the rest of the end of the turn.
        restore_amount = builtins.int((((3 * cha) + (intel) + (2 * skill) + 15) * production_modifier) / 5)
        self.change_team_effectiveness(restore_amount, instant = instant_effect)
        return restore_amount

    def player_research(self) -> float:
        amount_researched = self.research_progress(mc.int, mc.focus, mc.research_skill)
        self.listener_system.fire_event("general_work")
        self.listener_system.fire_event("player_research", amount = amount_researched)
        renpy.say(None, f"You spend time in the lab, experimenting with different chemicals and techniques and producing {amount_researched:.1f} research points.")
        return amount_researched

    def player_buy_supplies(self) -> int:
        if self.supply_count >= self.supply_goal:
            renpy.say(None, "You spend time going over the supply inventory and concluded that you already met the set supply goal.")
            return 0

        amount_bought = self.supply_purchase(mc.focus, mc.charisma, mc.supply_skill)
        self.listener_system.fire_event("general_work")
        self.listener_system.fire_event("player_supply_purchase", amount = amount_bought)
        renpy.say(None, f"You spend time securing new supplies for the lab, purchasing {amount_bought:.0f} units of serum supplies.")
        return amount_bought

    def player_market(self) -> int:
        amount_sold = self.sale_progress(mc.charisma, mc.focus, mc.market_skill)
        self.listener_system.fire_event("general_work")
        renpy.say(None, f"You spend time making phone calls to acquire new potential clients and advertising your business. You expand your market reach by {amount_sold:.0f} people.")
        return amount_sold

    def player_production(self) -> int:
        production_amount = self.production_progress(mc.focus, mc.int, mc.production_skill)
        self.listener_system.fire_event("player_production", amount = production_amount)
        self.listener_system.fire_event("general_work")
        renpy.say(None, f"You spend time in the lab synthesizing serum from the raw chemical precursors. You generate {production_amount} production points.")
        return production_amount

    def player_hr(self) -> int:
        eff_amount = self.hr_progress(mc.charisma, mc.int, mc.hr_skill, instant_effect = True) #Player effect is instant so that it can be reflected on the UI right away.
        self.listener_system.fire_event("player_efficiency_restore", amount = eff_amount)
        self.listener_system.fire_event("general_work")
        renpy.say(None, f"You settle in and spend a few hours filling out paperwork, raising company efficiency by {eff_amount}%%.")
        return eff_amount

    def accept_contract(self, contract: Contract):
        self.active_contracts.append(contract)
        if contract in self.offered_contracts:
            self.offered_contracts.remove(contract)

        contract.start_contract()

    def abandon_contract(self, contract: Contract):
        if contract in self.active_contracts:
            self.active_contracts.remove(contract)

        contract.abandon_contract()
        mc.stats.change_tracked_stat("Business", "Contracts Abandoned", 1)

    def complete_contract(self, contract: Contract):
        if contract in self.active_contracts:
            self.active_contracts.remove(contract)

        self.change_funds(contract.pay_out, stat = "Business Contracts")
        self.sales_made += contract.pay_out
        self.attention += contract.inventory.total_attention
        self.listener_system.fire_event("player_serums_sold_count", amount = contract.amount_desired)
        self.listener_system.fire_event("serums_sold_value", amount = contract.pay_out)

        contract.finish_contract()
        mc.stats.change_tracked_stat("Business", "Contracts Fullfilled", 1)

    def renew_contracts(self):
        self.offered_contracts = generate_story_contracts() #Puts story contracts at top of list
        for _ in range(0, self.max_offered_contracts):
            self.offered_contracts.append(generate_contract(self.max_serum_tier))

    def sell_serum(self, the_serum: SerumDesign, serum_count = 1):
        #NOTE: Each serum immediately decreases the value of the one sold after it. (ie selling one serum at a time is no more or less efficient than bulk selling to the open market.
        sales_value = 0

        if self.inventory.get_serum_count(the_serum) < serum_count:
            serum_count = self.inventory.get_serum_count(the_serum)

        for _ in range(0, serum_count):
            serum_value = self.get_serum_sales_value(the_serum)

            sales_value += serum_value

            self.mental_aspect_sold += the_serum.mental_aspect
            self.physical_aspect_sold += the_serum.physical_aspect
            self.sexual_aspect_sold += the_serum.sexual_aspect
            self.medical_aspect_sold += the_serum.medical_aspect

            attention_gain = the_serum.attention
            if attention_floor_increase_1_policy.is_active:
                attention_gain -= 1
            if attention_floor_increase_2_policy.is_active:
                attention_gain -= 1
            attention_gain = max(attention_gain, 0)
            self.attention += attention_gain

        the_serum.update_market_demand(serum_count)
        sales_value = builtins.int(sales_value)
        self.inventory.change_serum(the_serum, -serum_count)
        self.change_funds(sales_value, stat = "Serum Sales")
        self.sales_made += sales_value
        self.listener_system.fire_event("player_serums_sold_count", amount = serum_count)
        self.listener_system.fire_event("serums_sold_value", amount = sales_value)
        mc.stats.change_tracked_stat("Business", "Serums Sold", serum_count)

    def get_serum_base_value(self, the_serum: SerumDesign):
        serum_value = 0
        serum_value += the_serum.mental_aspect * self.get_aspect_price("mental")
        serum_value += the_serum.physical_aspect * self.get_aspect_price("physical")
        serum_value += the_serum.sexual_aspect * self.get_aspect_price("sexual")
        serum_value += the_serum.medical_aspect * self.get_aspect_price("medical")
        serum_value += the_serum.flaws_aspect * self.get_aspect_price("flaw")
        return serum_value

    def get_serum_sales_value(self, the_serum: SerumDesign):
        serum_value = self.get_serum_base_value(the_serum)
        for modifier_tuple in self.sales_multipliers:
            serum_value = serum_value * modifier_tuple[1]

        # apply demand factor
        serum_value = serum_value * the_serum.market_demand
        return serum_value

    def get_aspect_price(self, the_aspect: str) -> float: #If we want to be really proper we could have this check _per aspect_, but I think that's excessive.
        the_aspect = the_aspect.lower()
        if the_aspect == "mental":
            return self.mental_aspect_price * self.get_aspect_percent("mental")

        if the_aspect == "physical":
            return self.physical_aspect_price * self.get_aspect_percent("physical")

        if the_aspect == "sexual":
            return self.sexual_aspect_price * self.get_aspect_percent("sexual")

        if the_aspect == "medical":
            return self.medical_aspect_price * self.get_aspect_percent("medical")

        if the_aspect == "flaw":
            return self.flaws_aspect_cost * self.get_aspect_percent("flaw")
        return 0

    def get_aspect_percent(self, the_aspect) -> float:
        the_aspect = the_aspect.lower()
        if the_aspect == "mental":
            return 1.0 / (1 + ((self.mental_aspect_sold * 1.0) / ((self.market_reach or 1) * 1.0)))

        if the_aspect == "physical":
            return 1.0 / (1 + ((self.physical_aspect_sold * 1.0) / ((self.market_reach or 1) * 1.0)))

        if the_aspect == "sexual":
            return 1.0 / (1 + ((self.sexual_aspect_sold * 1.0) / ((self.market_reach or 1) * 1.0)))

        if the_aspect == "medical":
            return 1.0 / (1 + ((self.medical_aspect_sold * 1.0) / ((self.market_reach or 1) * 1.0)))

        return 1.0

    def has_funds(self, amount: int) -> bool:
        return self.funds >= amount

    def change_funds(self, amount: int | float, stat: str = None, add_to_log = True):
        amount = builtins.int(amount)
        self.funds += amount

        if stat is None:
            stat = "Misc. Profit" if amount > 0 else "Misc. Expenses"

        mc.stats.change_tracked_stat("Money", stat, int(amount))

        if amount != 0 and add_to_log:
            mc.log_event(f"{self.name} {'received' if amount > 0 else 'paid'}: ${builtins.abs(amount):,.0f}", "float_text_green")

    # Use to be def clear_production(self)
    def clear_all_production(self): #Clears all current production lines.
        for line in self.production_lines:
            line.clear_product()

    @property
    def used_line_weight(self) -> int:
        return sum(x.production_weight for x in self.production_lines)

    def has_sales_multiplier(self, multiplier_class: str) -> bool:
        return multiplier_class in (x[0] for x in self.sales_multipliers)

    def add_sales_multiplier(self, multiplier_class: str, multiplier: float):
        mc.log_event(f"Serum sale value increased by {(multiplier - 1) * 100:.0f}% due to {multiplier_class}.", "float_text_grey")
        self.sales_multipliers.append((multiplier_class, multiplier))

    def update_sales_multiplier(self, multiplier_class: str, multiplier: float):
        if found := next((x for x in self.sales_multipliers if x[0] == multiplier_class), None):
            found[1] = multiplier
            mc.log_event(f"Serum sale value increased by {(multiplier - 1) * 100:.0f}% due to {multiplier_class}.", "float_text_grey")

    def remove_sales_multiplier(self, multiplier_class: str, multiplier: float):
        if found := next((x for x in self.sales_multipliers if x[0] == multiplier_class), None):
            multiplier = found[1]
            mc.log_event(f"No longer receiving {(multiplier - 1) * 100:.0f}% serum value increase from {multiplier_class}.", "float_text_grey")
            self.sales_multipliers.remove(found)

    def do_autosale(self):
        autosale_potential = 0
        for employee in (x for x in people_with_job(market_job) if x.is_at_job(market_job)):
            work_skill = employee.market_skill
            if employee.has_duty(work_for_tips_duty):
                work_skill += employee.oral_sex_skill / 2.0
                if employee.sluttiness > 50:
                    work_skill += employee.foreplay_sex_skill / 2.0
            autosale_potential += builtins.int(work_skill * 3 * employee.calculate_job_efficiency())
            if employee.has_duty(heavy_market_work_duty):
                autosale_potential = builtins.int(autosale_potential * 1.2)

        extra_doses = 0
        for line in (x for x in self.production_lines if x.autosell and x.selected_design):
            if autosale_potential <= 0:
                break
            available_doses = self.inventory.get_serum_count(line.selected_design) - line.autosell_amount
            extra_doses += available_doses # track all doses
            if available_doses > autosale_potential:
                available_doses = autosale_potential
            if available_doses > 0:
                self.sell_serum(line.selected_design, available_doses)
                extra_doses -= available_doses # remove sold doses
                autosale_potential -= available_doses

        if autosale_potential == 0 and extra_doses > 0: # autosell is exhausted before available doses == 0
            mc.log_event("Insufficient people in marketing to auto-sell all serum doses", "float_text_yellow")

    def get_random_weighed_production_serum(self): #Return the serum design of one of our actively produced serums, relative probability by weight.
        used_production = self.used_line_weight
        random_serum_number = renpy.random.randint(0, used_production)

        for line in self.production_lines:
            if random_serum_number < line.production_weight and line.selected_design:
                return line.selected_design
            random_serum_number -= line.production_weight #Subtract the probability of this one from our number to make progress in our search.
        return None

    def change_team_effectiveness(self, amount, instant = False):
        if instant:
            self.team_effectiveness += amount
            if self.team_effectiveness > self.effectiveness_cap:
                self.team_effectiveness = self.effectiveness_cap
            elif self.team_effectiveness < 50:
                self.team_effectiveness = 50
        else:
            self.team_effectiveness_temp += amount #temp_effectiveness is changed to team_effectiveness on_turn so that all HR effects are frozen.

    @property
    def effectiveness_cap(self):
        # save compatibility (can be removed from future versions)
        if not hasattr(self, "base_effectiveness_cap"):
            self.base_effectiveness_cap = 100

        factor = 0
        # sum event_trigger_dict_bonusses
        for bonus in ("HR_eff_bonus", "CPA_eff_bonus"):
            factor += self.event_triggers_dict.get(bonus, 0)

        # calculate HR team bonusses
        if self.hr_director:
            factor += (self.hr_director.charisma * 2) + self.hr_director.hr_skill   #Charisma + HR skill
            if self.IT_project_is_active("Task Manager"):
                for hr_person in [x for x in self.hr_team if x != self.hr_director]:
                    factor += builtins.round(((hr_person.charisma * 2) + hr_person.hr_skill) / 2)
        return self.base_effectiveness_cap + factor

    def update_team_effectiveness(self):
        self.change_team_effectiveness(self.team_effectiveness_temp, instant = True)
        self.team_effectiveness_temp = 0

    def remove_employee_assignment(self, person: Person):
        '''
        Removes any special employee assignments
        '''
        if person == self.head_researcher:
            self.fire_head_researcher()

        if person == self.company_model:
            self.fire_company_model()

        if person == self.hr_director:
            self.fire_HR_director()

        if person == self.personal_secretary:
            self.fire_personal_secretary()

        if person == self.it_director:
            self.fire_IT_director()

        if person == self.prod_assistant:
            self.fire_production_assistant()

    def _setup_employee_stats(self, person: Person):
        '''
        Centralized function for setting up employee stats when you hire them
        NOTE: needs to be called prior to hiring
        '''
        # set names when hiring (if not set)
        if person.is_stranger:
            person.set_title()
            person.set_possessive_title()
            person.set_mc_title()

        if not person.has_event_day("day_met"):
            person.set_event_day("day_met")

        # introduce her to other employees
        for other_employee in self.employee_list + self.intern_list:
            town_relationships.begin_relationship(person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"

        # register phone and trigger listeners (when not already employee)
        if not (person.is_employee or person.is_intern):
            mc.phone.register_number(person)        # you know the phone numbers of your employees
            self.listener_system.fire_event("new_hire", the_person = person)
            self.listener_system.fire_event("general_work")

        # make sure she is dressed appropriately
        person.apply_planned_outfit()

    def add_employee_research(self, person: Person, start_day: int = -1):
        '''
        Hire passed person in research job, when no start_day is set, the next day is used
        When start_day = -1, the next day is used
        '''
        self.remove_employee_assignment(person)
        self._setup_employee_stats(person)
        person.change_job(rd_job, job_known = True, start_day = day + 1 if start_day == -1 else start_day)

    def add_employee_production(self, person: Person, start_day: int = -1):
        '''
        Hire passed person in production job, when no start_day is set, the next day is used
        When start_day = -1, the next day is used
        '''
        self.remove_employee_assignment(person)
        self._setup_employee_stats(person)
        person.change_job(production_job, job_known = True, start_day = day + 1 if start_day == -1 else start_day)

    def add_employee_supply(self, person: Person, start_day: int = -1):
        '''
        Hire passed person in supply job, when no start_day is set, the next day is used
        When start_day = -1, the next day is used
        '''
        self.remove_employee_assignment(person)
        self._setup_employee_stats(person)
        person.change_job(supply_job, job_known = True, start_day = day + 1 if start_day == -1 else start_day)

    def add_employee_marketing(self, person: Person, start_day: int = -1):
        '''
        Hire passed person in marketing job, when no start_day is set, the next day is used
        When start_day = -1, the next day is used
        '''
        self.remove_employee_assignment(person)
        self._setup_employee_stats(person)
        person.change_job(market_job, job_known = True, start_day = day + 1 if start_day == -1 else start_day)

    def add_employee_hr(self, person: Person, start_day: int = -1):
        '''
        Hire passed person in HR job, when no start_day is set, the next day is used
        When start_day = -1, the next day is used
        '''
        self.remove_employee_assignment(person)
        self._setup_employee_stats(person)
        person.change_job(hr_job, job_known = True, start_day = day + 1 if start_day == -1 else start_day)

    def remove_employee(self, person: Person):
        self.remove_employee_assignment(person)
        person.quit_job(person.primary_job) # let person class handle it
        person.change_location(person.home) # remove from premisis
        mc.stats.change_tracked_stat("Employee", "Fired / Quit Job", 1)
        person.remove_role(family_employee_role) # special role for family

    def get_employee_count(self, division: str) -> int:
        if division in ("r", "r_div", "research"):
            return len(self.research_team)
        elif division in ("p", "p_div", "production"):
            return len(self.production_team)
        elif division in ("s", "s_div", "supply"):
            return len(self.supply_team)
        elif division in ("m", "m_div", "market"):
            return len(self.market_team)
        elif division in ("h", "h_div", "hr"):
            return len(self.hr_team)
        raise ValueError(f"Division {division} not known")

    def get_intern_count(self, division: str) -> int:
        if division in ("r", "r_div", "research"):
            return len(self.college_interns_research)
        elif division in ("p", "p_div", "production"):
            return len(self.college_interns_production)
        elif division in ("s", "s_div", "supply"):
            return len(self.college_interns_supply)
        elif division in ("m", "m_div", "market"):
            return len(self.college_interns_market)
        elif division in ("h", "h_div", "hr"):
            return len(self.college_interns_HR)
        raise ValueError(f"Division {division} not known")

    @cached_property
    def employee_list(self) -> list[Person]:
        return self.research_team + self.production_team + self.supply_team + self.market_team + self.hr_team

    @property
    def employee_count(self) -> int:
        return len(self.employee_list)

    @property
    def employees_at_office(self) -> list[Person]:
        return [x for x in self.employee_list + self.intern_list if x.is_at_office]

    @property
    def employees_availabe(self) -> list[Person]:
        return [x for x in self.employee_list + self.intern_list if x.is_available]

    @property
    def at_employee_limit(self) -> bool:
        return self.employee_count >= self.max_employee_count

    @property
    def number_of_employees_at_office(self) -> int:
        return builtins.len(self.employees_at_office)

    def advance_tutorial(self, tutorial_name):
        self.event_triggers_dict[tutorial_name] += 1 #advance our tutorial slot.

    def reset_tutorial(self, tutorial_name):
        self.event_triggers_dict[tutorial_name] = 1 #Reset it when the reset tutorial button is used.

    def generate_candidate_requirements(self): #Checks current business policies and generates a dict of keywords for create_random_person to set the correct values to company requirements.
        # In cases where a range is allowed it generates a random value in that range, so call this one per person being created.
        candidate_dict = {} # This will hold keywords and arguments for create_random_person to create a person with specific modifies

        candidate_dict["age_range"] = [Person.get_age_floor(), Person.get_age_ceiling()]
        candidate_dict["height_range"] = [Person.get_height_floor(), Person.get_height_ceiling()]
        candidate_dict["stat_range_array"] = [[Person.get_stat_floor(), Person.get_stat_ceiling()] for x in range(0, 3)]
        candidate_dict["skill_range_array"] = [[Person.get_skill_floor(), Person.get_skill_ceiling()] for x in range(0, 5)]
        candidate_dict["sex_skill_range_array"] = [[Person.get_sex_skill_floor(), Person.get_sex_skill_ceiling()] for x in range(0, 4)]

        candidate_dict["happiness_range"] = [Person.get_happiness_floor(), Person.get_happiness_ceiling()]
        candidate_dict["suggestibility_range"] = [Person.get_suggestibility_floor(), Person.get_suggestibility_ceiling()]
        candidate_dict["sluttiness_range"] = [Person.get_sluttiness_floor(), Person.get_sluttiness_ceiling()]
        candidate_dict["love_range"] = [Person.get_love_floor(), Person.get_love_ceiling()]
        candidate_dict["obedience_range"] = [Person.get_obedience_floor(), Person.get_obedience_ceiling()]

        candidate_dict["tits_range"] = Person.get_tit_weighted_list()

        candidate_dict["relationship_list"] = Person.get_potential_relationships_list()

        #First Pass / Independent & Relative Policies
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                candidate_dict["age_range"][0] += recruitment_policy.extra_data.get("age_floor_adjust", 0)
                candidate_dict["age_range"][1] += recruitment_policy.extra_data.get("age_ceiling_adjust", 0)

                for stat_range in candidate_dict["stat_range_array"]:
                    stat_range[0] += recruitment_policy.extra_data.get("stat_floor_adjust", 0)
                    stat_range[1] += recruitment_policy.extra_data.get("stat_ceiling_adjust", 0)

                for skill_range in candidate_dict["skill_range_array"]:
                    skill_range[0] += recruitment_policy.extra_data.get("skill_floor_adjust", 0)
                    skill_range[1] += recruitment_policy.extra_data.get("skill_ceiling_adjust", 0)

                for sex_skill_range in candidate_dict["sex_skill_range_array"]:
                    sex_skill_range[0] += recruitment_policy.extra_data.get("sex_skill_floor_adjust", 0)
                    sex_skill_range[1] += recruitment_policy.extra_data.get("sex_skill_ceiling_adjust", 0)

                candidate_dict["happiness_range"][0] += recruitment_policy.extra_data.get("happiness_floor_adjust", 0)
                candidate_dict["happiness_range"][1] += recruitment_policy.extra_data.get("happiness_ceiling_adjust", 0)

                candidate_dict["suggestibility_range"][0] += recruitment_policy.extra_data.get("suggestibility_floor_adjust", 0)
                candidate_dict["suggestibility_range"][1] += recruitment_policy.extra_data.get("suggestibility_ceiling_adjust", 0)

                candidate_dict["sluttiness_range"][0] += recruitment_policy.extra_data.get("sluttiness_floor_adjust", 0)
                candidate_dict["sluttiness_range"][1] += recruitment_policy.extra_data.get("sluttiness_ceiling_adjust", 0)

                candidate_dict["love_range"][0] += recruitment_policy.extra_data.get("love_floor_adjust", 0)
                candidate_dict["love_range"][1] += recruitment_policy.extra_data.get("love_ceiling_adjust", 0)

                candidate_dict["obedience_range"][0] += recruitment_policy.extra_data.get("obedience_floor_adjust", 0)
                candidate_dict["obedience_range"][1] += recruitment_policy.extra_data.get("obedience_ceiling_adjust", 0)

                relationships_allowed = recruitment_policy.extra_data.get("relationships_allowed")
                if relationships_allowed:
                    candidate_dict["relationship_list"] = [relationship for relationship in candidate_dict["relationship_list"] if relationship[0] in relationships_allowed]

        #Make sure ranges are not reversed (only done for ranges where that is currently possible)
        if candidate_dict["age_range"][0] > candidate_dict["age_range"][1]:
            candidate_dict["age_range"].reverse()

        #2nd Pass / Absolute Policies
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                candidate_dict["tits_range"] = recruitment_policy.extra_data.get("tits_range", candidate_dict["tits_range"])

                #Because these are absolute they should also ensure that the range is valid (so an absolute floor also needs to raise the ceiling if it's below the floor)
                candidate_dict["height_range"][0] = builtins.max(candidate_dict["height_range"][0], recruitment_policy.extra_data.get("height_floor", candidate_dict["height_range"][0]))
                candidate_dict["height_range"][1] = builtins.max(candidate_dict["height_range"][1], recruitment_policy.extra_data.get("height_floor", candidate_dict["height_range"][1]))

                candidate_dict["height_range"][1] = builtins.min(candidate_dict["height_range"][1], recruitment_policy.extra_data.get("height_ceiling", candidate_dict["height_range"][1]))
                candidate_dict["height_range"][0] = builtins.min(candidate_dict["height_range"][0], recruitment_policy.extra_data.get("height_ceiling", candidate_dict["height_range"][0]))

                candidate_dict["age_range"][0] = builtins.max(candidate_dict["age_range"][0], recruitment_policy.extra_data.get("age_floor", candidate_dict["age_range"][0]))
                candidate_dict["age_range"][1] = builtins.max(candidate_dict["age_range"][1], recruitment_policy.extra_data.get("age_floor", candidate_dict["age_range"][1]))

                candidate_dict["age_range"][1] = builtins.min(candidate_dict["age_range"][1], recruitment_policy.extra_data.get("age_ceiling", candidate_dict["age_range"][1]))
                candidate_dict["age_range"][0] = builtins.min(candidate_dict["age_range"][0], recruitment_policy.extra_data.get("age_ceiling", candidate_dict["age_range"][0]))

        #Enforce limits (only done where it's currently possible for it to be violated)
        candidate_dict["age_range"][0] = builtins.max(candidate_dict["age_range"][0], Person.get_age_floor(initial=False))
        candidate_dict["age_range"][1] = builtins.min(candidate_dict["age_range"][1], Person.get_age_ceiling(initial=False))

        #3rd Pass / Dependent limits
        candidate_dict["kids_range"] = Person.get_initial_kids_range(candidate_dict["age_range"], candidate_dict["relationship_list"])

        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                #These are special restrictions that should be enforced *after* final age / relationships adjustments (which can only be done when the age and relationships are known) so they can't be calculated in at this point
                candidate_dict["kids_floor"] = recruitment_policy.extra_data.get("kids_floor")
                candidate_dict["kids_ceiling"] = recruitment_policy.extra_data.get("kids_ceiling")

        return candidate_dict

    def hire_company_model(self, person: Person):
        if self.company_model:
            self.fire_company_model()
        self._set_company_model(person)
        person.add_role(company_model_role)

    def fire_company_model(self):
        if self.company_model:
            self.company_model.remove_role(company_model_role)
            self._set_company_model(None)

    def hire_head_researcher(self, person: Person):
        if self.head_researcher:
            self.fire_head_researcher()
        self._set_head_researcher(person)
        person.change_job(head_researcher_job)

    def fire_head_researcher(self):
        if self.head_researcher:
            self.head_researcher.change_job(rd_job)
            self._set_head_researcher(None)

    def hire_HR_director(self, person: Person):
        if self.hr_director:
            self.fire_HR_director()
        self._set_hr_director(person)
        self.hr_director.HR_tags = {}
        self.hr_director.HR_unlocks = {}
        self.hr_director.add_role(HR_director_role)
        self.event_triggers_dict["HR_unlocked"] = True

    def fire_HR_director(self):
        def cleanup_HR_director_meetings():
            self.remove_mandatory_crisis("Sarah_intro_label")
            self.remove_mandatory_crisis("Sarah_hire_label")
            self.remove_mandatory_crisis("Sarah_get_drinks_label")
            self.remove_mandatory_crisis("Sarah_stripclub_story_label")
            self.remove_mandatory_crisis("Sarah_epic_tits_label")
            self.remove_mandatory_crisis("Sarah_new_tits_label")
            self.remove_mandatory_crisis("Sarah_third_wheel_label")
            self.remove_mandatory_crisis("Sarah_catch_stealing_label")
            self.remove_mandatory_crisis("Sarah_threesome_request_label")
            self.remove_mandatory_crisis("Sarah_initial_threesome_label")
            self.remove_mandatory_crisis("HR_director_initial_hire_label")
            self.remove_mandatory_crisis("HR_director_first_monday_label")
            self.remove_mandatory_crisis("HR_director_monday_meeting_label")
            self.remove_mandatory_crisis("HR_director_headhunt_interview_label")

        if self.hr_director:
            self.hr_director.remove_role(HR_director_role)
            self._set_hr_director(None)
            cleanup_HR_director_meetings()

    def hire_personal_secretary(self, person: Person):
        if self.personal_secretary:
            self.fire_personal_secretary()
        self._set_personal_secretary(person)
        personal_secretary_prog_scene.stage = -1
        personal_secretary_prog_scene.scene_unlock_list = []
        person.change_job(personal_secretary_job)
        self.add_mandatory_crisis(personal_secretary_prog_scene_action)

    def fire_personal_secretary(self):
        if self.personal_secretary:
            self.personal_secretary.change_job(hr_job)
            self._set_personal_secretary(None)
            self.remove_mandatory_crisis(personal_secretary_prog_scene_action)

    def hire_IT_director(self, person: Person):
        if self.it_director:
            self.fire_IT_director()
        self._set_it_director(person)
        self.it_director.IT_tags = {}   #What is this even for?
        person.change_job(IT_director_job)

    def fire_IT_director(self):
        if self.it_director:
            self.it_director.change_job(rd_job)
            self.it_director.remove_role(IT_director_role)
            self._set_it_director(None)

    def hire_production_assistant(self, person: Person):
        if self.prod_assistant:
            self.fire_production_assistant()
        self._set_prod_assistant(person)
        person.change_job(production_assistant_job)

    def fire_production_assistant(self):
        if self.prod_assistant:
            cleanup_prod_assistant_meetings(self.prod_assistant)
            self.prod_assistant.change_job(production_job)
            self.prod_assistant.remove_role(prod_assistant_role)
            self._set_prod_assistant(None)

    def add_mandatory_crisis(self, crisis_event: Action):
        self.mandatory_crises_list.append(crisis_event)

    def add_mandatory_morning_crisis(self, crisis_event: Action):
        self.mandatory_morning_crises_list.append(crisis_event)

    def remove_mandatory_crisis(self, crisis_event: Action | str):
        self.mandatory_crises_list.remove_action(crisis_event)
        self.mandatory_morning_crises_list.remove_action(crisis_event)

    def has_queued_crisis(self, action: Action | str) -> bool:
        '''
        Returns True when action / label name is an event in the room_enter or talk_event lists
        '''
        return self.mandatory_crises_list.has_action(action) \
            or self.mandatory_morning_crises_list.has_action(action)

    @property
    def active_mandatory_crisis_count(self) -> int:
        return sum(1 for x in self.mandatory_crises_list if x.is_action_enabled())

    @property
    def active_mandatory_morning_crisis_count(self) -> int:
        return sum(1 for x in self.mandatory_morning_crises_list if x.is_action_enabled())

    @property
    def mc_offspring_count(self) -> int:
        return sum(x.number_of_children_with_mc for x in self.employee_list + self.intern_list)

    @property
    def employees_with_children_with_mc(self) -> list[Person]:
        return [x for x in self.employee_list + self.intern_list if x.has_child_with_mc]

    @property
    def employees_knocked_up_by_mc(self) -> list[Person]:
        return [x for x in self.employee_list + self.intern_list if (x.knows_pregnant and x.is_mc_father)]

    def set_event_day(self, dict_key: str, set_day = None):
        '''
        Set event day with passed key, when no set_day is passed, current day is set
        '''
        self.event_triggers_dict[dict_key] = day if set_day is None else set_day

    def get_event_day(self, dict_key: str) -> int:
        '''
        Returns the day value set for key
        When key doesn't exist returns 0
        '''
        return self.event_triggers_dict.get(dict_key, 0)

    def days_since_event(self, dict_key: str) -> int:
        '''
        Number of days passed since value set for key
        When key does not exist returns 0
        '''
        return day - self.event_triggers_dict.get(dict_key, day)

    def has_event_day(self, dict_key: str) -> bool:
        '''
        Return True when event day is set
        '''
        return dict_key in self.event_triggers_dict

    def has_event_delay(self, dict_key: str, delay: int = 7) -> bool:
        '''
        Retruns True when dict_key is not set or delay for dict_key has passed
        delay: number of days passed since dict_key was set
        '''
        return not self.has_event_day(dict_key) or self.days_since_event(dict_key) > delay

    def string_since_event(self, dict_key: str) -> str: #Returns a string describing how long it has been since an event
        since = self.days_since_event(dict_key)

        if since < 1:
            return "earlier"
        if since == 1:
            return "yesterday"
        if since <= 4:
            return "a few days ago"
        if since <= 10:
            return "a week ago"
        if since <= 19:
            return "a couple weeks ago"
        if since <= 28:
            return "a few weeks ago"
        if since <= 45:
            return "a month ago"
        if since <= 75:
            return "a couple months ago"
        if since <= 145:
            return "a few months ago"
        return "quite some time ago"

    @cached_property
    def stripclub_strippers(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job((stripper_job, stripclub_stripper_job))]

    @cached_property
    def stripclub_bdsm_performers(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(stripclub_bdsm_performer_job)]

    @cached_property
    def stripclub_waitresses(self) -> list[Person]:
        return [x for x in list_of_people if x.has_job(stripclub_waitress_job)]

    @cached_property
    def stripclub_employees(self) -> list[Person]:
        return [x for x in list_of_people if x.is_strip_club_employee]

    # College intern related functions
    @cached_property
    def intern_list(self) -> list[Person]:
        return [x for x in list_of_people if x.is_intern]

    @cached_property
    def college_interns_research(self) -> list[Person]:
        return [x for x in self.intern_list if x.has_job(student_intern_rd_job) or x == kaya]

    @cached_property
    def college_interns_production(self) -> list[Person]:
        return [x for x in self.intern_list if x.has_job(student_intern_production_job)]

    @cached_property
    def college_interns_market(self) -> list[Person]:
        return [x for x in self.intern_list if x.has_job(student_intern_market_job)]

    @cached_property
    def college_interns_supply(self) -> list[Person]:
        return [x for x in self.intern_list if x.has_job(student_intern_supply_job)]

    @cached_property
    def college_interns_HR(self) -> list[Person]:
        return [x for x in self.intern_list if x.has_job(student_intern_hr_job)]

    @property
    def college_supply_interns_unlocked(self) -> bool:
        return self.event_triggers_dict.get("supply_interns_unlocked", False)

    @college_supply_interns_unlocked.setter
    def college_supply_interns_unlocked(self, value):
        self.event_triggers_dict["supply_interns_unlocked"] = value

    @property
    def college_market_interns_unlocked(self) -> bool:
        return self.event_triggers_dict.get("market_interns_unlocked", False)

    @college_market_interns_unlocked.setter
    def college_market_interns_unlocked(self, value):
        self.event_triggers_dict["market_interns_unlocked"] = value

    @property
    def college_hr_interns_unlocked(self) -> bool:
        return self.event_triggers_dict.get("hr_interns_unlocked", False)

    @college_hr_interns_unlocked.setter
    def college_hr_interns_unlocked(self, value):
        self.event_triggers_dict["hr_interns_unlocked"] = value

    def hire_college_intern(self, person: Person, job: JobDefinition):
        self._setup_employee_stats(person)

        if len(self.intern_list) % 2 == 0: # alternating work-days for students (limit daily overcrowding of department)
            work_days = [1, 3] # tue / thu
        else:
            work_days = [2, 4] # wed / fri

        # change student schedule for workdays
        person.primary_job.set_schedule(None, day_slots = work_days, time_slots = [2, 3])

        # setup work schedule
        person.change_job(job, is_primary = False, start_day = day + 1)
        location = job.schedule.get_destination(5, 1) # get job destination for saturday (is working department)
        person.secondary_job.set_schedule(location, day_slots = work_days, time_slots = [2, 3])

        self.listener_system.fire_event("new_intern", the_person = person)

    def remove_college_intern(self, person: Person):
        person.quit_job(person.secondary_job)

    def get_intern_depts_with_openings(self) -> list[str]:
        dept_list = []
        if len(self.college_interns_research) < self.max_interns_by_division:
            dept_list.append("Research")
        if len(self.college_interns_production) < self.max_interns_by_division:
            dept_list.append("Production")
        if len(self.college_interns_market) < self.max_interns_by_division and self.college_market_interns_unlocked:
            dept_list.append("Marketing")
        if len(self.college_interns_supply) < self.max_interns_by_division and self.college_supply_interns_unlocked:
            dept_list.append("Supply")
        if len(self.college_interns_HR) < self.max_interns_by_division and self.college_hr_interns_unlocked:
            dept_list.append("HR")
        return dept_list

    @property
    def topless_is_legal(self) -> bool:
        return self.event_triggers_dict.get("topless_is_legal", False)

    @property
    def nudity_is_legal(self) -> bool:
        return self.event_triggers_dict.get("nudity_is_legal", False)

    @property
    def public_sex_act_is_legal(self) -> bool:  #If minor sexual acts are legal
        return self.event_triggers_dict.get("public_sex_act_is_legal", False)

    # Unused
    @property
    def public_sex_is_legal(self) -> bool:  #If full sex in public is legal
        return self.event_triggers_dict.get("public_sex_is_legal", False)

    # Unused
    @property
    def incestuous_sex_is_legal(self) -> bool:  #If incest is legal
        return self.event_triggers_dict.get("incestuous_sex_is_legal", False)

    # Unused
    @property
    def prostitution_is_legal(self) -> bool:  #If prostitution is legal
        return self.event_triggers_dict.get("prostitution_is_legal", False)

    @property
    def council_members_influenced(self) -> int:
        return len(self.event_triggers_dict.get("council_influence", []))
