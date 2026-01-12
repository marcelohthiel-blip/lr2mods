from __future__ import annotations
import renpy
from game.helper_functions.list_functions_ren import get_random_from_list, unique_characters
from game.bugfix_additions.ActionMod_ren import crisis_list, limited_time_event_pool
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.character_related.Person_ren import Person, mc, town_relationships, list_of_people, mom, lily
from game.major_game_classes.game_logic.Action_ren import Action

TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

relationship_stats = {
    "Married": 90,
    "Fiancée": 65,
    "Girlfriend": 40,
    "Single": 25,
}

breakup_chance_relationship = {
    "Married": 5,
    "Fiancée": 15,
    "Girlfriend": 30,
}

def so_relationship_improve_requirement():
    return (
        time_of_day in (1, 2, 3)
        and not get_so_relationship_improve_person() is None
    )

def so_relationship_worsen_requirement():
    return (
        time_of_day in (1, 2, 3)
        and not get_so_relationship_worsen_person() is None
    )

def so_relationship_quarrel_requirement(person: Person):
    return (
        time_of_day in (1, 2, 3)
        and not (person.is_unique or person.is_affair)
        and person.has_event_delay("relationship_changed", TIER_3_TIME_DELAY)
        and person.has_significant_other
        and not person.is_stranger
    )

def get_so_relationship_improve_person():
    potential_people = []
    for person in (x for x in mc.phone.get_person_list(excluded_people = unique_characters())
            if not x.relationship == "Married"
                and x.has_event_delay("relationship_changed", TIER_3_TIME_DELAY)
                and not x.has_relation_with_mc):

        if person.relationship in relationship_stats and person.love <= relationship_stats[person.relationship] + (person.opinion.cheating_on_men * 5):
            potential_people.append(person)
    return get_random_from_list(potential_people)

def get_so_relationship_worsen_person():
    potential_people = []
    for person in (x for x in mc.phone.get_person_list(excluded_people = unique_characters())
            if x.has_significant_other
                and not x.is_affair
                and x.has_event_delay("relationship_changed", TIER_3_TIME_DELAY)):

        if person.relationship in relationship_stats and person.love > relationship_stats[person.relationship] - (person.opinion.cheating_on_men * 5):
            potential_people.append(person)
    return get_random_from_list(potential_people)

limited_time_event_pool.append(
    Action("Girl had a fight with her SO", so_relationship_quarrel_requirement, "so_relationship_quarrel_label",
        event_duration = 2, priority = 1, trigger = "on_talk", silent = True))

crisis_list.append(
    Action("Friend SO relationship improve", so_relationship_improve_requirement, "so_relationship_improve_label"))

crisis_list.append(
    Action("Friend SO relationship worsen", so_relationship_worsen_requirement, "so_relationship_worsen_label"))

def get_phone_sexting_requirement():
    return (
        time_of_day in (3, 4)
        and not get_phone_sexting_person() is None
    )

def get_phone_sexting_person():
    return get_random_from_list([
        x for x in list_of_people
        if x.has_relation_with_mc
        and x.has_event_delay("phone_sexting", TIER_2_TIME_DELAY)
        and not x.is_at(mc.location)
    ])

crisis_list.append(
    Action("Affair dic pic", get_phone_sexting_requirement, "affair_dick_pick_label"))

def camera_strip_tits_description(person: Person, strip_list: list[Clothing]):
    for item in strip_list:
        person.draw_animated_removal(item, position = "stand5")
        if person.tits_visible:
            renpy.say(None, f"She pulls her {item.name} off and lets her tits fall free.")
            renpy.say(None, "She looks at the camera and shakes them for you.")

crisis_list.append(
    Action("Girlfriend nudes", get_phone_sexting_requirement, "girlfriend_nudes_label"))


def friends_help_friends_be_sluts_requirement():
    if mc.is_at_office and mc.business.is_open_for_business:
        return any(x for x in town_relationships.get_business_relationships(["Friend", "Best Friend"])
            if not x.person_a.has_relation_with_mc and x.person_a.is_at_office
                and x.person_b.has_relation_with_mc and x.person_b.is_at_office)
    return False

def get_friends_relationship_with_actor_not_girlfriend_or_paramour():
    relationship = get_random_from_list([x for x in town_relationships.get_business_relationships(["Friend", "Best Friend"])
        if not x.person_a.has_relation_with_mc and x.person_a.is_at_office
            and x.person_b.has_relation_with_mc and x.person_b.is_at_office])

    if relationship is None:
        return (None, None)

    if relationship.person_a.has_relation_with_mc \
            or relationship.person_a.effective_sluttiness() > relationship.person_b.effective_sluttiness():
        person_one = relationship.person_a
        person_two = relationship.person_b
    else:
        person_one = relationship.person_b
        person_two = relationship.person_a

    return (person_one, person_two)

crisis_list.append(
    Action("Friends Help Friends Be Sluts", friends_help_friends_be_sluts_requirement, "friends_help_friends_be_sluts_label"))


def work_relationship_change_crisis_requirement():
    return any(x for x in town_relationships.get_business_relationships(["Acquaintance"])
        if x.person_a.is_at_office and x.person_b.is_at_office)

crisis_list.append(
    Action("Work Relationship Change Crisis", work_relationship_change_crisis_requirement, "work_relationship_change_label"))

def work_relationship_get_friend_chance(person_one: Person, person_two: Person):
    friend_chance = 50
    for an_opinion in person_one.opinions:
        if person_one.opinion(an_opinion) == person_two.opinion(an_opinion):
            friend_chance += 10
        elif (person_one.opinion(an_opinion) > 0 and person_two.opinion(an_opinion) < 0) or (person_two.opinion(an_opinion) > 0 and person_one.opinion(an_opinion) < 0):
            friend_chance -= 10

    friend_chance += (person_one.opinion.small_talk * 5) + (person_two.opinion.small_talk * 5)
    return friend_chance


def friend_sends_text_requirement():
    return not get_friend_sends_text_person() is None

def get_friend_sends_text_person():
    return get_random_from_list(
        [x for x in mc.phone.get_person_list(excluded_people = [mom, lily])
            if x.love > 10 and not x.is_at(mc.location)])

crisis_list.append(
    Action("Friend Sends Text Crisis", friend_sends_text_requirement, "friend_sends_text"))
