from __future__ import annotations
from renpy import persistent
from game.clothing_lists_ren import apron
from game.bugfix_additions.ActionMod_ren import limited_time_event_pool
from game.game_roles._role_definitions_ren import mother_role, sister_role, cousin_role, aunt_role
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, mom, cousin
from game.major_game_classes.character_related._job_definitions_ren import mom_secretary_job
from game.major_game_classes.game_logic.Room_ren import aunt_bedroom, kitchen, mom_bedroom, aunt_apartment, cousin_bedroom

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def sister_walk_in_requirement(person: Person):
    return (
        person.energy > 40
        and person.arousal_perc > 25 - (person.opinion.masturbating * 5)
        and person.has_role(sister_role)
        and person in person.home.people
        and person.home.person_count < 2
    )

def nude_walk_in_requirement(person: Person):
    return (
        person in person.home.people
        and person.has_role((sister_role, mother_role))
        and person.home.person_count < 2
    )

def mom_house_work_nude_requirement(person: Person):
    return (
        person.event_triggers_dict.get("kissing_revisit_complete", False)
        and mc.business.is_work_day
        and person.has_role(mother_role)
        and person in kitchen.people
        and person.sluttiness > (40 - person.opinion.not_wearing_anything * 5)
    )

def mom_breeding_intro_requirement(person: Person):
    return (
        persistent.pregnancy_pref != 0
        and person.event_triggers_dict.get("vaginal_revisit_complete", False)
        and time_of_day > 0
        and not person.has_breeding_fetish
        and not person.on_birth_control
        and not person.knows_pregnant
        and not person.is_sleeping
        and not person.has_taboo("vaginal_sex")
        and person.opinion.creampies > 0
        and person.opinion.bareback_sex > 0
        and person.has_role(mother_role)
        and person in mom_bedroom.people
        and mom_bedroom.person_count < 2
    )

#TODO: We really need to be able to assign LTE's to roles instead of being general events

def mom_work_slutty_requirement(person: Person):
    return (
        time_of_day in (2, 3)
        and mc.business.is_work_day
        and person.event_triggers_dict.get("mom_office_slutty_level", 0) > 0
        and person.has_job(mom_secretary_job)
        and person.is_at_mc_house
    )

def aunt_home_lingerie_requirement(person: Person):
    return (
        person.has_role(aunt_role)
        and person.has_event_delay("home_lingerie", 7)
        and person.is_at(aunt_apartment)
        and not cousin.is_home
        and person.home == aunt_bedroom
    )

def cousin_home_panties_requirement(person: Person):
    return (
        person.has_role(cousin_role)
        and person.has_event_delay("home_panties", 7)
        and person.is_home
        and person.home == cousin_bedroom
    )

def add_mom_outfit_coloured_apron(person: Person):
    person.wear_apron([0.74, 0.33, 0.32, 0.95], "Pattern_1", [1.0, 0.83, 0.90, 0.95])

def sister_go_shopping_requirement(person: Person):
    return (
        time_of_day == 3
        and person.has_event_delay("last_shopping_day", 7)
        and person.is_at_mc_house
        and person.has_role(sister_role)
    )

def mom_go_shopping_requirement(person: Person):
    return (
        time_of_day == 3
        and person.has_event_delay("last_shopping_day", 7)
        and person.is_at_mc_house
        and person.has_role(mother_role)
    )

def mom_fuck_during_housework_requirement(person: Person):
    return (
        time_of_day == 3
        and person.has_role(mother_role)
        and person.sluttiness > 40
        and person.is_at_mc_house
    )

### ON TALK EVENTS ###
limited_time_event_pool.append(
    Action("Mom work slutty", mom_work_slutty_requirement, "mom_work_slutty_report",
        event_duration = 2, priority = 8, trigger = "on_talk"))

### ON ENTER EVENTS ###
limited_time_event_pool.append(
    Action("Sister walk in", sister_walk_in_requirement, "sister_walk_in_label",
        event_duration = 5, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Sister go shopping", sister_go_shopping_requirement, "sister_go_shopping_label",
        event_duration = 5, priority = 6, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Nude walk in", nude_walk_in_requirement, "nude_walk_in_label",
        event_duration = 5, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Mom nude house work", mom_house_work_nude_requirement, "mom_house_work_nude_label",
        event_duration = 5, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Mom breeding", mom_breeding_intro_requirement, "breeding_mom_intro_label",
        event_duration = 5, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Mom go shopping", mom_go_shopping_requirement, "mom_go_shopping_label",
        event_duration = 5, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Aunt home lingerie", aunt_home_lingerie_requirement, "aunt_home_lingerie_label",
        event_duration = 3, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Cousin home panties", cousin_home_panties_requirement, "cousin_home_panties_label",
        event_duration = 3, priority = 4, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Mom being naughty", mom_fuck_during_housework_requirement, "mom_fuck_during_housework_label",
        event_duration = 2, priority = 4, trigger = "on_enter"))
