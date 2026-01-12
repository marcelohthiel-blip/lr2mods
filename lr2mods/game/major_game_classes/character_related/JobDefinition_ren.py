from __future__ import annotations
import builtins
from typing import Callable, Iterable
from renpy.rollback import NoRollback
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.character_related.ActiveJob_ren import ActiveJob
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.game_roles._role_definitions_ren import unimportant_job_role
from game.major_game_classes.character_related.Schedule_ren import Schedule
from game.major_game_classes.game_logic.Duty_ren import Duty
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import Room

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
def base_salary_calculation(person: Person) -> float:
    base_salary = ((person.int + person.focus + person.charisma) * 2 + (person.hr_skill + person.market_skill + person.research_skill + person.production_skill + person.supply_skill)) * person.salary_modifier * (0.5 + 0.25 * person.work_experience)
    return builtins.round(base_salary, 2)

def salary_function(job: ActiveJob) -> float:
    return base_salary_calculation(job.person)

class JobDefinition(NoRollback): # A job is just a title displayed on the screen and a name that is displayed. A person can only have one job at a time (if it's not a full time job it's just a Role).
    def __init__(self, job_title: str, job_roles: Iterable[Role] | Role | None = None, job_location: Room | None = None,
            day_slots: list[int] = None, time_slots: list[int] = None, wardrobe: Wardrobe | str | None = None,
            seniority_level = 1, wage_adjustment = 1.0, productivity_adjustment = 1.0,
            mandatory_duties: Iterable[Duty] | Duty | None = None, available_duties: Iterable[Duty] | Duty | None = None,
            base_salary_func: Callable[[ActiveJob], float] = salary_function, is_paid = False,
            age_range: list[int] = None):

        self.job_title = job_title # The string that is displayed on the hud
        if job_roles is None:
            self.job_roles = (unimportant_job_role,)
        elif isinstance(job_roles, (list, tuple, set)):
            self.job_roles = tuple(job_roles)
        else:
            self.job_roles = (job_roles, )

        if day_slots is None:
            day_slots = [0, 1, 2, 3, 4]
        if time_slots is None:
            time_slots = [1, 2, 3]

        # build default schedule for Job
        self.schedule = Schedule()
        self.set_schedule(job_location, day_slots, time_slots)

        self.wardrobe = None
        if isinstance(wardrobe, str):
            self.wardrobe = wardrobe_from_xml(wardrobe)
            self.wardrobe.name = f"{self.job_title} Wardrobe"
        if isinstance(wardrobe, Wardrobe):
            self.wardrobe = wardrobe
        if self.wardrobe is None:
            self.wardrobe = Wardrobe(f"{self.job_title} Wardrobe")

        self.seniority_level = seniority_level # How experienced or far up the career ladder this job is. Girls will be unhappy or unwilling to take jobs with lower seniority levels.
        self.wage_adjustment = wage_adjustment #How much more or less than basic income this job demands.
        self.productivity_adjustment = productivity_adjustment #How much more or less this job produces compared to normal.
        self.base_salary_func = base_salary_func
        self.is_paid = is_paid # When True, salary is paid by player
        self.age_range = age_range

        if mandatory_duties is None:
            self.mandatory_duties = ()
        elif isinstance(mandatory_duties, (list, tuple, set)):
            self.mandatory_duties = tuple(mandatory_duties)
        else:
            self.mandatory_duties = (mandatory_duties,)

        if available_duties is None:
            self.available_duties = ()
        elif isinstance(available_duties, (list, tuple, set)):
            self.available_duties = tuple(available_duties)
        else:
            self.available_duties = (available_duties,)

        self.identifier = generate_identifier((tuple(self.job_title) + tuple(x.identifier for x in self.job_roles)))

    def __eq__(self, other: JobDefinition) -> bool:
        if not isinstance(other, JobDefinition):
            return NotImplemented
        return self.identifier == other.identifier

    def __hash__(self) -> int:
        return self.identifier

    def set_schedule(self, location: Room, day_slots: list[int] | None = None, time_slots: list[int] | None = None):
        '''
        Sets the scheduled location for this job definition
        When day_slots is None, all days of the week are scheduled
        When time_slots is None, all timeslots of the day are scheduled
        '''
        self.schedule.set_schedule(location, day_slots, time_slots)
