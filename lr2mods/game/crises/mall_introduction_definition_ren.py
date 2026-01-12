from game.bugfix_additions.ActionMod_ren import ActionMod
from game.helper_functions.list_functions_ren import get_random_from_list, known_people_at_location, unique_characters, unknown_people_at_location
from game.major_game_classes.character_related.Person_ren import Person, mc, town_relationships
from game.map.MapHub_ren import mall_hub, downtown_hub, gym_hub

TIER_1_TIME_DELAY = 3
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
def mall_introduction_requirement():
    return (
        (not mc.business.has_event_day("mall_introduction")
            or mc.business.days_since_event("mall_introduction") >= TIER_1_TIME_DELAY)
        and mc.is_at((mall_hub, downtown_hub, gym_hub))
        and any(unknown_people_at_location(loc, unique_characters()) for loc in mc.current_location_hub)
        and any(any(x for x in known_people_at_location(loc) if x.love > 20) for loc in mc.current_location_hub)
    )

def mall_introduction_update_relationship(known_person: Person, stranger: Person):
    if town_relationships.get_relationship(known_person, stranger) is None:
        town_relationships.update_relationship(known_person, stranger, "Friend")

def mall_introduction_get_people_with_status() -> tuple[list[Person], list[Person]]:
    strangers: list[Person] = []
    known_people: list[Person] = []
    for loc in mc.current_location_hub:
        strangers.extend(unknown_people_at_location(loc, unique_characters())) # don't introduce unique characters
        known_people.extend([x for x in known_people_at_location(loc) if x.love > 20])
    return (strangers, known_people)

def mall_introduction_get_actors() -> tuple[Person, Person, str]:
    '''
    return (known_person, stranger, relationship_type_name)
    '''
    strangers, known_people = mall_introduction_get_people_with_status()
    # prioritize family introduction
    family_relation = next(((x, y) for x in known_people for y in strangers if town_relationships.is_family(x, y)), None)
    if family_relation:
        return (*family_relation, town_relationships.get_relationship_type(*family_relation))

    # pick a person from each
    known_person = get_random_from_list(known_people)
    stranger = get_random_from_list(strangers)
    return (known_person, stranger, "Friend")

mall_introduction_action = ActionMod("Mall Introduction", mall_introduction_requirement, "mall_introduction_action_label",
    menu_tooltip = "You meet a stranger and a friend/family introduces you.", category = "Mall", is_crisis = True)
