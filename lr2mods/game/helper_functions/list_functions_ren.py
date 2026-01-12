from __future__ import annotations
import builtins
from itertools import chain
from typing import Callable, TypeVar
import renpy
from game.map.map_code_ren import MapHub, list_of_hubs
from game.people.Ellie.IT_Project_class_ren import IT_Project
from game.bugfix_additions.debug_info_ren import ttl_cache
from game.business_policies.clothing_policies_ren import uniform_policies_list
from game.business_policies.recruitment_policies_ren import recruitment_policies_list
from game.business_policies.organisation_policies_ren import organisation_policies_list, unmapped_policies_list
from game.business_policies.serum_policies_ren import serum_policies_list
from game.business_policies.special_policies_ren import special_policies_list
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, unemployed_job, full_job_list
from game.major_game_classes.character_related.Person_ren import Person, Room, home_hub, list_of_people, list_of_places, christina, emily, cousin, nora, alexia, ashley, candace, salon_manager, aunt, sarah, starbuck, camila, kaya, sakari, ellie, myra, erica, naomi
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits
from game.people.Ellie.IT_Business_Projects_ren import business_IT_project_list
from game.people.Ellie.IT_Nanobot_Projects_ren import nanobot_IT_project_list, nanobot_unlock_project_list
from game.people.Erica.erica_role_definition_ren import erica_get_progress

T = TypeVar('T')
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -20 python:
"""
from _collections_abc import Iterable
import inspect

def all_people_in_the_game(excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in list_of_people if x not in excluded_people)

def all_locations_in_the_game() -> tuple[Room]:
    return tuple(list_of_places)

def all_policies_in_the_game(excluded_policies: Iterable[Policy] = ()) -> tuple[Policy]:
    return tuple(x for x in chain(uniform_policies_list, recruitment_policies_list, serum_policies_list, organisation_policies_list, special_policies_list, unmapped_policies_list) if x not in excluded_policies)

def all_IT_projects() -> tuple[IT_Project]:
    return tuple(chain(business_IT_project_list, nanobot_IT_project_list, nanobot_unlock_project_list))

def all_jobs(excluded_jobs: Iterable[JobDefinition] = ()) -> tuple[JobDefinition]:
    return [x for x in full_job_list if x not in excluded_jobs]

def all_hubs() -> tuple[MapHub]:
    return tuple(list_of_hubs)

@ttl_cache(ttl=1)
def unique_characters_not_known() -> tuple[Person]: # TODO The check should be standardized, but some people are vanilla, some are different modders or different 'style'.
    not_met_yet_list = []
    if not alexia.has_event_day("day_met"): # She'll be scheduled otherwise when met.
        not_met_yet_list.append(alexia)
    if ashley.has_job(unemployed_job):
        not_met_yet_list.append(ashley)
    if not candace.has_event_day("day_met"): # She exist but not met yet.
        not_met_yet_list.append(candace)
    if not christina.has_event_day("day_met"): #She'll call MC differently when met.
        not_met_yet_list.append(christina)
    if not emily.has_event_day("day_met"): #She'll call MC differently when met.
        not_met_yet_list.append(emily)
    if erica_get_progress() == 0:
        not_met_yet_list.append(erica)
    if nora.get_destination(time_slot = 1) == nora.home: # She'll be scheduled otherwise when met.
        not_met_yet_list.append(nora)
    if not salon_manager.has_event_day("day_met"):
        not_met_yet_list.append(salon_manager)
    if not aunt.has_event_day("arrival"):
        not_met_yet_list.append(aunt)
        not_met_yet_list.append(cousin)
    if not sarah.has_event_day("day_met"):
        not_met_yet_list.append(sarah)
    if not starbuck.has_event_day("day_met"):
        not_met_yet_list.append(starbuck)
    if not camila.has_event_day("day_met"):
        not_met_yet_list.append(camila)
    if not kaya.has_event_day("day_met"):
        not_met_yet_list.append(kaya)
    if not sakari.has_event_day("day_met"):
        not_met_yet_list.append(sakari)
    if not ellie.has_event_day("day_met"):
        not_met_yet_list.append(ellie)
    if not myra.has_event_day("day_met"):
        not_met_yet_list.append(myra)
    if not naomi.has_event_day("day_met"):
        not_met_yet_list.append(naomi)
    return tuple(not_met_yet_list)

def unique_characters() -> tuple[Person]:
    return tuple(x for x in list_of_people if x.is_unique)

def known_people_in_the_game(excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in list_of_people if x not in excluded_people and x not in unique_characters_not_known() and not x.is_stranger)

def people_at_location(location: Room, excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in list_of_people if x not in excluded_people and x.location.identifier == location.identifier)

def known_people_at_location(location: Room, excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in location.people if x.is_available and x not in excluded_people and x not in unique_characters_not_known() and not x.is_stranger)

def unknown_people_in_the_game(excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in list_of_people if x not in excluded_people and (x in unique_characters_not_known() or x.is_stranger))

def unknown_people_at_location(location: Room, excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in location.people if x.is_available and x not in excluded_people and (x in unique_characters_not_known() or x.is_stranger))

def people_in_mc_home(excluded_people: Iterable[Person] = ()) -> tuple[Person]:
    return tuple(x for x in list_of_people if x.is_available and x not in excluded_people and x.location in home_hub)

def people_in_role(role: str | Role | Iterable[Role]) -> tuple[Person]:
    return tuple(x for x in list_of_people if x.has_role(role))

def people_with_job(job: JobDefinition) -> tuple[Person]:
    return tuple(x for x in list_of_people if x.has_job(job))

# splits a item_array in even chunks of block_size
@renpy.pure
def split_list_in_blocks(split_list, block_size):
    for i in builtins.range(0, builtins.len(split_list), block_size):
        yield split_list[i:i + block_size]

# splits an item_array in a number of blocks about equal in size (remainders are added to last block)
@renpy.pure
def split_list_in_even_blocks(split_list, block_count):
    avg = builtins.len(split_list) / float(block_count)
    result = []
    last = 0.0

    while last < builtins.len(split_list):
        result.append(split_list[builtins.int(last):builtins.int(last + avg)])
        last += avg

    return result

# finds an item in a list, where search(item) == True
# search as lambda could be a lambda ==> x: x.name == 'searchname'
def find_serum_trait_by_name(name: str) -> SerumTrait | None:
    return next((x for x in list_of_traits if x.name == name), None)

@renpy.pure
def find_in_set(obj, in_set: set[T]) -> T:
    return next((x for x in in_set if x == obj), None)

@renpy.pure
def flatten_list(lst):
    def is_element(e) -> bool:
        return not (isinstance(e, Iterable) and not isinstance(e, str))

    for el in lst:
        if is_element(el):
            yield el
        else:
            yield from flatten_list(el)


# get a sorted list of people to use with main_choice_display
@renpy.pure
def get_sorted_people_list(people: list[Person], title: str, back_extension: None | str = None, reverse = False) -> list[Person]:
    result = sorted(people, key = lambda x: x.name, reverse = reverse) # create copy so we don't alter the original list
    result.insert(0, title)
    if back_extension is not None:
        result.extend([back_extension])
    return result

@renpy.pure
def get_random_from_list(choices: Iterable[T], default: T = None) -> T:
    if choices and isinstance(choices, (list, tuple, set)) and not isinstance(choices, str):
        return renpy.random.choice(choices)
    elif inspect.isgenerator(choices):
        return renpy.random.choice(list(choices))
    return default

@renpy.pure
def get_random_items_from_list(choices: Iterable[T], count: int, filter: Callable[[T], bool] = lambda x: True) -> tuple[T]:
    '''
    When count == 1 -> returns T or None
    When count > 1 -> returns tuple of (T or None) * count
    filter as lambda could be a lambda x: x.name == 'searchname'
    '''
    filtered = [x for x in choices if filter(x)]
    if len(filtered) < count:
        return tuple(filtered + [None for _ in range(count - len(filtered))])

    result = []
    for _ in builtins.range(count):
        item = get_random_from_list(filtered)
        if item:
            result.append(item)
            filtered.remove(item)

    if count == 1:
        return result[0]

    return tuple(result)
