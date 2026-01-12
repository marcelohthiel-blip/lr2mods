from __future__ import annotations
from typing import Iterator
from itertools import chain
from game.bugfix_additions.debug_info_ren import ttl_cache
from game.bugfix_additions.mapped_list_ren import MappedList
from game.helper_functions.list_functions_ren import all_jobs, all_people_in_the_game
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_people
from game.map.MapHub_ren import MapHub, Point, Room

residential_home_hub: HomeHub
industrial_home_hub: HomeHub
downtown_home_hub: HomeHub
university_home_hub: HomeHub

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
class HomeHub(MapHub):
    def __init__(self, name, formal_name, locations: list[Room] | None = None,
            position: Point | None = None, icon = None, accessible_func = None,
            people: list[Person] | None = None, jobs: list[JobDefinition] | None = None):
        super().__init__(name, formal_name, locations, position, icon, accessible_func)

        self.people = MappedList(Person, all_people_in_the_game)
        self.jobs = MappedList(JobDefinition, all_jobs)

        self.people.extend(people)
        self.jobs.extend(jobs)

    @ttl_cache(5)
    def _locations(self) -> set[Room]:
        def get_full_name(person: Person):
            return f"{person.name} {person.last_name}"

        return set(chain(
            self.locations,
            (x.home for x in self.people),
            (x.home for x in list_of_people
                if not x.is_unique
                and x.primary_job.job_definition in self.jobs
                and get_full_name(x) in x.home.name)
        ))

    def __iter__(self) -> Iterator[Room]:
        return iter(self._locations())

    @property
    def residents(self) -> list[Person]:
        return [x for x in list_of_people if x.home in self]

    @property
    def visible_locations(self) -> list[Room]:
        return [x for x in self if not x.hide_in_known_house_map and x in mc.known_home_locations]
