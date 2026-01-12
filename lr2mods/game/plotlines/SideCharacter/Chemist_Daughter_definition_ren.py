from __future__ import annotations
from game.helper_functions.list_functions_ren import get_random_from_list
from game.game_roles._role_definitions_ren import affair_role
from game.major_game_classes.character_related.Personality_ren import Personality
from game.map.HomeHub_ren import industrial_home_hub
from game.major_game_classes.character_related.Person_ren import Person, make_character_unique, mc, town_relationships, list_of_instantiation_functions, lily, mom, cousin, aunt
from game.major_game_classes.game_logic.Action_ren import Action

TIER_1_TIME_DELAY = 3
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
day_names: tuple[str]
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
list_of_instantiation_functions.append("init_chemist_daughter")
chemist_daughter_dad_name = "Gregory"


def chemist_daughter_init_requirement():
    if day < TIER_3_TIME_DELAY * 2:
        return False  # don't start too early
    if lily.cum_exposure_count + mom.cum_exposure_count + aunt.cum_exposure_count + cousin.cum_exposure_count < 5:
        return False  # check player incest desire
    if mc.business.employee_count < 10:
        return False  # wait until we have a sizeable business
    return not find_avail_princess_employee() is None

def init_chemist_daughter():
    mc.business.add_mandatory_crisis(
        Action("Initialize chemist daughter", chemist_daughter_init_requirement, "chemist_daughter_init_label")
    )

def add_chemist_daughter_coffee_meeting():
    return mc.create_event("chemist_daughter_coffee_label", "Get coffee with chemist", day_restriction = (0, 1, 2, 3, 4), time_restriction = 2)

def chemist_daughter_after_raise_consult_requirement():
    if time_of_day in (0, 4):
        return False
    person = get_chemist_daughter()
    if person is None:
        return True
    if person.primary_job.salary > person.event_triggers_dict.get("starting_pay", 0):
        return person.days_since_event("last_raise") > TIER_1_TIME_DELAY
    return False

def add_chemist_daughter_after_raise_consult_action(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Chemist Daughter Gets a Raise", chemist_daughter_after_raise_consult_requirement, "chemist_daughter_after_raise_consult_label")
    )
    person.event_triggers_dict["starting_pay"] = person.primary_job.salary


def chemist_daughter_help_move_requirement():
    if time_of_day != 3:
        return False

    person = get_chemist_daughter()
    if person is None:
        return True
    return person.days_since_event("moving_day") > 0

def add_chemist_daughter_help_move_action():
    mc.business.add_mandatory_crisis(
        Action("Help Baby Girl Move", chemist_daughter_help_move_requirement, "chemist_daughter_help_move_label")
    )

def chemist_daughter_daddy_title_requirement(person: Person):
    return person.sluttiness > 40 \
        and mc.is_at_office and mc.business.is_open_for_business

def add_chemist_daughter_daddy_title_action(person: Person):
    person.add_unique_on_room_enter_event(
        Action("Name Baby Girl", chemist_daughter_daddy_title_requirement, "chemist_daughter_daddy_title_label")
    )


def get_chemist_daughter():
    person = Person.get_person_by_identifier(mc.business.event_triggers_dict.get("chemist_daughter_ident", None))
    if person is None or not person.is_employee:
        return None
    return person

def find_avail_princess_employee():
    able_person_list = []
    for person in [x for x in mc.business.production_team if x.age < 25 and x.kids == 0 and x.primary_job.days_employed > 7 and x.is_single and not x.is_clone]:
        if len(town_relationships.get_existing_parents(person)) == 0 and len(town_relationships.get_existing_sisters(person)) == 0: # no mother / sisters in game
            able_person_list.append(person)
    return get_random_from_list(able_person_list)

def chemist_daughter_employee_finished():
    return mc.business.event_triggers_dict.get("chemist_daughter_employee_finish", False)

def chemist_daughter_intro_requirement(person: Person):
    return time_of_day >= 2 and mc.business.is_open_for_business and person.is_at_office

def setup_chemist_daughter():
    person = find_avail_princess_employee()
    if person is None:
        init_chemist_daughter() # reset event
        return

    # make sure 'selected person' is single and has no kids
    # although the player might have seen other information
    # it is more disturbing when this information does not
    # match the story line
    person.kids = 0
    person.relationship = "Single"
    person.SO_name = None
    person.remove_role(affair_role)   # make sure we don't have a affair
    person.update_opinion_with_score("incest", 2, add_to_log = False) # this method updates or adds the opinion
    person.update_opinion_with_score("being submissive", 2, add_to_log = False) # this method updates or adds the opinion
    make_character_unique(person, industrial_home_hub)
    mc.business.event_triggers_dict["chemist_daughter_ident"] = person.identifier

    person.add_unique_on_room_enter_event(
        Action("Chemist Daughter Intro", chemist_daughter_intro_requirement, "chemist_daughter_intro_label", priority = 30)
    )
    return

def daddy_girl_titles(the_person):
    return "Baby Girl" # locks to this title

def daddy_girl_possessive_titles(the_person):
    return "your baby girl" # locks to this title

def daddy_girl_player_titles(the_person):
    return "Daddy" # locks to this title

def update_to_daddy_girl_personality(person: Person): #Use a function to get this so we can keep the girls prefix so her personality doesn't change TOO much
    daddy_girl_personality = Personality("princess", default_prefix = person.personality.default_prefix,
        titles_function = daddy_girl_titles, possessive_titles_function = daddy_girl_possessive_titles, player_titles_function = daddy_girl_player_titles)
    person.change_personality(daddy_girl_personality)
