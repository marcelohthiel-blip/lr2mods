from __future__ import annotations
from game.map.MapHub_ren import MapHub
from game.map.map_code_ren import list_of_hubs
from game.bugfix_additions.debug_info_ren import write_log
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Duty_ren import Duty
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import Room
from game.major_game_classes.clothing_related.LimitedWardrobeCollection_ren import limited_wardrobes

day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

class ActiveJob():
    def __init__(self, person: Person, job_definition: JobDefinition, job_known = False, seniority_level: int = None, start_day: int = -1):
        '''
        Creates an active job for a person based on passed job_definition, the seniority_level denotes the workexperience for this job
        Passing a start_day will effectively make them start the job on that day (activate the job schedule) when not passed will use today
        '''
        self.person = person
        self.job_definition = job_definition
        if seniority_level:
            self.seniority_level = seniority_level
        else:
            self.seniority_level = job_definition.seniority_level
        self.wage_adjustment = job_definition.wage_adjustment
        self.productivity_adjustment = job_definition.productivity_adjustment

        self.schedule = job_definition.schedule.get_copy()
        self.schedule.start_day = start_day
        self.job_known = job_known
        self.employed_since = day if start_day == -1 else start_day
        self.shifts = 0
        self.current_uniform: Outfit = None #The uniform the person was planning on wearing for today
        self.forced_uniform: Outfit = None #Forced uniform for current week
        self.dress_code_outfit: Outfit = None #When no uniform, but dresscode is in effect use this outfit

        self.duties: list[Duty] = []
        for duty in self.job_definition.mandatory_duties:
            self.add_duty(duty)
        self.recalculate_salary()

    def __eq__(self, other: ActiveJob) -> bool:
        if not isinstance(other, ActiveJob):
            return NotImplemented
        return self.job_definition == other.job_definition

    def __hash__(self) -> int:
        return self.identifier

    def reset(self):
        '''
        Resets daily tracked stats for job
        '''
        self.shifts = 0
        self.current_uniform = None
        self.dress_code_outfit = None
        if day % 7 == 6:
            self.forced_uniform = None

    @property
    def identifier(self) -> int:
        self.job_definition.identifier

    @property
    def job_title(self) -> str:
        return self.job_definition.job_title

    @property
    def job_roles(self) -> tuple[Role]:
        '''
        Tuple of Roles associated with this Job
        '''
        return self.job_definition.job_roles

    @property
    def wardrobe(self) -> Wardrobe:
        '''
        Return Wardrobe for this Job
        '''
        return self.job_definition.wardrobe

    @property
    def planned_uniform(self) -> Outfit:
        '''
        Return planned uniform for this job
        '''
        if self.forced_uniform:
            return self.forced_uniform

        if self.person.should_wear_uniform and not self.current_uniform and self.person.is_at_job(self.job_definition):
            self.current_uniform = self.wardrobe.decide_on_uniform(self.person)
        if self.current_uniform:
            return self.current_uniform

        if self.person.should_wear_dress_code and not self.dress_code_outfit and self.person.is_at_job(self.job_definition):
            self.dress_code_outfit = self.person.wardrobe.decide_on_uniform(self.person)

        if not self.dress_code_outfit and limited_wardrobes.should_use_limited_wardrobe(self.person):
            self.dress_code_outfit = limited_wardrobes.decide_on_outfit(self.person)

        if self.dress_code_outfit:
            return self.dress_code_outfit

        return None

    @planned_uniform.setter
    def planned_uniform(self, outfit: Outfit):
        if self.person.should_wear_uniform:
            self.current_uniform = outfit.get_copy() if outfit else None
        else:
            self.dress_code_outfit = outfit.get_copy() if outfit else None

    @property
    def is_paid(self):
        '''
        Return True when job is paid for by MC
        '''
        return self.job_definition.is_paid

    @property
    def daily_wage(self) -> float:
        '''
        Salary to be paid based on worked timeslots for day
        '''
        if self.shifts == 0:
            return 0
        return round(self._base_salary * (self.schedule.scheduled_time_slots() / max(self.shifts, 1) * 1.0), 2)

    @property
    def salary(self):
        '''
        Salary for a full day of work for job
        '''
        return self._base_salary

    @salary.setter
    def salary(self, value):
        amount = value - self._base_salary
        if value < 0:
            amount = -self._base_salary

        self._base_salary += amount
        if amount != 0 and self.person in mc.business.on_payroll:
            if amount > 0:
                self.person.set_event_day("last_raise")
            mc.log_event(f"{self.person.display_name}: {self.job_title} Salary ${amount:+.2f}/day", "float_text_green" if amount > 0 else "float_text_red")

    @property
    def base_salary(self) -> float:
        '''
        Return the base salary of the job based on salary function and wage adjustment for job
        '''
        return self.job_definition.base_salary_func(self) * self.wage_adjustment

    def recalculate_salary(self, factor = 1):
        '''
        Reset salary for job to base salary multiplied by factor
        '''
        self._base_salary = self.base_salary * factor

    @property
    def scheduled_location(self) -> Room | None:
        '''
        Get current work location based on day and time
        '''
        return self.schedule.get_destination()

    @property
    def scheduled_location_hub(self) -> MapHub | None:
        '''
        returns the location hub of the current job where she should be working
        '''
        return next((x for x in list_of_hubs if self.scheduled_location in x), None)

    def set_schedule(self, location: Room, day_slots: list[int] | None = None, time_slots: list[int] | None = None):
        '''
        Sets the scheduled location for this job
        When day_slots is None, all days of the week are scheduled
        When time_slots is None, all timeslots of the day are scheduled
        '''
        self.schedule.set_schedule(location, day_slots, time_slots)

    def remove_location(self, location: Room):
        '''
        Remove passed location from workschedule for any day or timeslot
        '''
        self.schedule.remove_location(location)

    def is_work_day(self, work_day: int | None = None) -> bool:
        '''
        Return True when scheduled to work on the current / passed day
        '''
        return self.schedule.scheduled_time_slots(work_day) > 0

    def is_work_shift(self, work_day: int | None = None, time_slot: int | None = None) -> bool:
        '''
        Return True when passed work_day / timeslot has assigned job location
        '''
        return self.schedule.has_time_schedule(work_day, time_slot)

    @property
    def available_duties(self) -> tuple[Duty, ...]:
        '''
        List of availabe duties for this job
        '''
        return self.job_definition.available_duties

    def add_duty(self, duty: Duty):
        '''
        Adds passed duty as active duty for job
        '''
        if not isinstance(duty, Duty):
            write_log(f"Object passed to ActiveJob.add_duty() is not a Duty object but a {type(duty).__name__}")
            return
        if duty not in self.job_definition.available_duties + self.job_definition.mandatory_duties:
            write_log(f"Passed duty {duty.duty_name} is not part of available duties for this job.")
            return
        if len(self.duties) >= self.seniority_level:
            write_log(f"{self.job_title} maximum duties for experience reached. Duty {duty.duty_name} not added.")
            return
        if duty not in self.duties: #Isn't possible to have the same duty twice.
            if callable(duty.on_apply):
                duty.on_apply(self.person)
            self.duties.append(duty)

    def remove_duty(self, duty: Duty):
        '''
        Removes passed duty from active duty list for this Job
        '''
        if duty in self.duties:
            if callable(duty.on_remove):
                duty.on_remove(self.person)
            self.duties.remove(duty)

    def has_duty(self, duty: Duty) -> bool:
        '''
        Returns True when passed duty in active duty list for job
        '''
        return any(x for x in self.duties if x == duty)

    @property
    def duty_actions(self) -> tuple[Action, ...]:
        '''
        List of actions associated with current active duties
        '''
        actions = set()
        for duty in self.duties:
            if not duty.only_at_work or (self.person.is_at_work and self.person.current_job.has_duty(duty)):
                actions.update(duty.actions)
        return tuple(actions)

    @property
    def duty_internet_actions(self) -> tuple[Action, ...]:
        '''
        List of internet actions associated with current active duties
        '''
        actions = set()
        for duty in self.duties:
            if not duty.only_at_work or (self.person.is_at_work and self.person.current_job.has_duty(duty)):
                actions.update(duty.internet_actions)
        return tuple(actions)

    @property
    def job_happiness_score(self) -> int:
        '''
        How happy is the person with this Job, this is a generic function for now
        Score > 0 happy, < 0 unhappy
        '''
        happy_points = int(10 * (min(self.person.happiness - 120, 100) / 100.0)) #Happiness over 120 gives a bonus to job score, happiness less than 110 gives a penalty
        happy_points += int(10 * (min(self.person.obedience - 130, 100) / 100.0)) #Obedience over 130 gives a bonus to job score, obedience less than 120 gives a penalty
        happy_points += int(100 * (-1.0 + (self.salary / (max(self.base_salary or self.salary, 1))))) #Salary is a major component in happiness every 10% salary equals about 10 points of happiness score
        happy_points += self.person.opinion.working * 5 # Does she like working? It affects her happiness score. (max 10 points bonus/deficit)
        if self.job_definition in mc.business.research_jobs:
            happy_points += self.person.research_skill + (self.person.opinion.research_work * 5)
        elif self.job_definition in mc.business.market_jobs:
            happy_points += self.person.market_skill + (self.person.opinion.marketing_work * 5)
        elif self.job_definition in mc.business.supply_jobs:
            happy_points += self.person.supply_skill + (self.person.opinion.supply_work * 5)
        elif self.job_definition in mc.business.production_jobs:
            happy_points += self.person.production_skill + (self.person.opinion.production_work * 5)
        elif self.job_definition in mc.business.hr_jobs:
            happy_points += self.person.hr_skill + (self.person.opinion.hr_work * 5)

        if self.days_employed < 14:
            happy_points += 14 - self.days_employed #Employees are much less likely to quit over the first two weeks.
        return happy_points

    @property
    def days_employed(self) -> int:
        '''
        Number of days the person has had this job
        '''
        return day - self.employed_since

    ##############################
    # Wardrobe wrapper functions #
    ##############################

    def add_outfit(self, outfit: Outfit):
        self.wardrobe.add_outfit(outfit)

    def add_underwear_set(self, outfit: Outfit):
        self.wardrobe.add_underwear_set(outfit)

    def add_overwear_set(self, outfit: Outfit):
        self.wardrobe.add_overwear_set(outfit)

    def remove_outfit(self, outfit: Outfit | str):
        self.wardrobe.remove_outfit(outfit)
