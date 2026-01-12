from __future__ import annotations
from game.clothing_lists_ren import creampie_cum, ass_cum
from game.major_game_classes.character_related.Person_ren import Person, mc, ellie
from game.major_game_classes.game_logic.Action_ren import Action
from game.people.Ellie.IT_director_role_definition_ren import nanobot_program_is_IT
from game.people.Ellie.ellie_definition_ren import ellie_has_given_blowjob, ellie_is_working_on_nanobots
from game.people.Ellie.ellie_role_definition_ren import ellie_lust_role

TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 12
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

def take_virginity(person: Person): #Use this to apply the appropriate "clothing" item
    def get_blood_item(clothing):
        item = clothing.get_copy()
        item.colour = [.71, .1, .1, 0.8]
        item.layer = 0
        return item

    person.outfit.add_accessory(get_blood_item(creampie_cum))
    person.outfit.add_accessory(get_blood_item(ass_cum))
    person.break_taboo("vaginal_sex")
    person.event_triggers_dict["given_virginity"] = True

def restore_virginity(person: Person):  #For testing purposes only.
    person.event_triggers_dict["given_virginity"] = False


####### Love Events #######

def ellie_never_given_handjob_requirement():
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False
    return ellie.love >= 20

def add_ellie_never_given_handjob_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie wants to touch", ellie_never_given_handjob_requirement, "ellie_never_given_handjob_label")
    )

def ellie_brings_lunch_requirement():
    if time_of_day != 1 or day % 7 == 0 or not (mc.business.is_open_for_business and mc.is_at_office):
        return False
    return ellie.love >= 40 and ellie.story_event_ready("love")

def add_ellie_brings_lunch_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie likes cooking", ellie_brings_lunch_requirement, "ellie_brings_lunch_label")
    )
    ellie.story_event_log("love")

def ellie_dinner_date_intro_requirement(person: Person):
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False
    return person.love >= 60 and person.story_event_ready("love")

def add_ellie_dinner_date_intro_action():
    ellie.add_unique_on_talk_event(
        Action("Ellie asks for a dinner date", ellie_dinner_date_intro_requirement, "ellie_dinner_date_intro_label", priority = 30)
    )
    ellie.story_event_log("love")

def ellie_dinner_date_requirement():
    return day % 7 == 6 and time_of_day == 3

def add_ellie_dinner_date_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie cooks for you", ellie_dinner_date_requirement, "ellie_dinner_date_label")
    )

def ellie_lingerie_shopping_requirement(person: Person):
    # TODO: finish story line -> current writing point
    return False
    return time_of_day in (2, 3) and person.love >= 80 and person.story_event_ready("love")

def add_ellie_lingerie_shopping_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie dresses up for you", ellie_lingerie_shopping_requirement, "ellie_lingerie_shopping_label", priority = 30)
    )
    ellie.story_event_log("love")

###### Lust Events ######

def ellie_oral_taboo_restore_requirement(min_day: int):
    return day > min_day and time_of_day == 3 and mc.is_at_office and ellie.is_at_work and ellie.has_broken_taboo(["sucking_cock"])

def add_ellie_oral_taboo_restore_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie Oral Taboo", ellie_oral_taboo_restore_requirement, "ellie_oral_taboo_restore_label", requirement_args = day)
    )

def ellie_turned_on_while_working_intro_requirement(person: Person):
    return False

def add_ellie_turned_on_while_working_intro_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie gets horny", ellie_turned_on_while_working_intro_requirement, "ellie_turned_on_while_working_intro_label", priority = 30)
    )

def ellie_never_been_fucked_requirement(person: Person):
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False
    return person.sluttiness >= 60 and ellie.story_event_ready("slut")

def add_ellie_never_been_fucked_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie wants to fuck", ellie_never_been_fucked_requirement, "ellie_never_been_fucked_label", priority = 30)
    )

def ellie_vaginal_taboo_restore_requirement(min_day: int):
    return day > min_day and time_of_day == 3 and mc.is_at_office and ellie.is_at_work and ellie.has_broken_taboo(["vaginal_sex"]) and ellie.progress.lust_step == 1

def add_ellie_vaginal_taboo_restore_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie vaginal taboo", ellie_vaginal_taboo_restore_requirement, "ellie_vaginal_taboo_restore_label", requirement_args = day)
    )

def ellie_never_tried_anal_requirement(person: Person):
    return False

def add_ellie_never_tried_anal_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie tries anal", ellie_never_tried_anal_requirement, "ellie_never_tried_anal_label", priority = 30)
    )

def ellie_anal_taboo_restore_requirement(min_day: int):
    return day > min_day and time_of_day == 3 and mc.is_at_office and ellie.is_at_work and ellie.has_broken_taboo(["anal_sex"])

def add_ellie_anal_taboo_restore_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie Anal Taboo", ellie_anal_taboo_restore_requirement, "ellie_anal_taboo_restore_label", requirement_args = day)
    )

def ellie_grope_taboo_restore_requirement(min_day: int):
    return (
        day > min_day
        and ellie.days_since_event("last_grope") > 0
        and ellie.has_broken_taboo(["touching_body"])
        and mc.is_at_office
        and ellie.is_at_work
    )

def add_ellie_grope_taboo_restore_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie confronts you", ellie_grope_taboo_restore_requirement, "ellie_grope_taboo_restore_label", requirement_args = day)
    )
    ellie.add_role(ellie_lust_role)

def ellie_text_message_apology_requirement():
    return day % 7 == 6

def add_ellie_text_message_apology_action():
    mc.business.add_mandatory_morning_crisis(
        Action("Ellie texts you", ellie_text_message_apology_requirement, "ellie_text_message_apology_label")
    )
    ellie.remove_role(ellie_lust_role)
    ellie.progress.lust_step = 2

def ellie_never_been_kissed_requirement(person: Person):
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False

    if ellie_is_working_on_nanobots() or person.sluttiness >= 20:
        return mc.business.days_since_event("hired_ellie_IT") >= TIER_2_TIME_DELAY
    return False

def add_ellie_never_been_kissed_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie Gets Kissed", ellie_never_been_kissed_requirement, "ellie_never_been_kissed_label", priority = 30)
    )

def ellie_never_tasted_cock_requirement(person: Person):
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False

    if person.sluttiness >= 40 and ellie.story_event_ready("slut"):
        return any(x for x in mc.business.employees_at_office if x != person and x.sluttiness > 50)
    return False

def add_ellie_never_tasted_cock_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie wants to taste", ellie_never_tasted_cock_requirement, "ellie_never_tasted_cock_label", priority = 30)
    )
    ellie.story_event_log("slut")

###### Obedience Events ######

def ellie_tit_fuck_requirement():
    if not mc.business.is_open_for_business or not ellie.story_event_ready("obedience"):
        return False
    return mc.is_at(mc.business.r_div) and ellie.obedience >= 120

def add_ellie_tit_fuck_action():
    mc.business.add_mandatory_crisis(
        Action("Use Ellie's Tits", ellie_tit_fuck_requirement, "ellie_tit_fuck_label")
    )
    ellie.story_event_log("obedience")

def ellie_start_search_requirement():
    if not (mc.is_at_office and mc.business.is_open_for_business) or not mc.business.head_researcher:
        return False
    if ellie.days_since_event("obedience_event") <= TIER_2_TIME_DELAY:
        return False
    if mc.business.get_event_day("IT_dir_nanobot_takeover_day") < TIER_3_TIME_DELAY:
        return False
    #Need to make sure we know contact has ghosted head researcher.
    return ellie.obedience >= 140 and nanobot_program_is_IT()

def add_ellie_start_search_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie was framed", ellie_start_search_requirement, "ellie_start_search_label")
    )
    ellie.story_event_log("obedience")

def ellie_search_update_requirement(person: Person):
    if not (mc.is_at_office and mc.business.is_open_for_business) or not mc.business.head_researcher:
        return False
    return ellie_has_given_blowjob() and person.story_event_ready("obedience")

def add_ellie_search_update_action():
    ellie.add_unique_on_room_enter_event(Action("Finding the Culprit", ellie_search_update_requirement, "ellie_search_update_label", priority = 30))
    ellie.story_event_log("obedience")

def ellie_search_finish_requirement():
    if time_of_day != 3 or not (mc.is_at_office and mc.business.is_open_for_business) or not mc.business.head_researcher:
        return False
    return ellie.story_event_ready("obedience")

def add_ellie_search_finish_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie's Revenge", ellie_search_finish_requirement, "ellie_search_finish_label")
    )
    ellie.story_event_log("obedience")

def ellie_submission_requirement():
    if time_of_day != 3 or not (mc.is_at_office and mc.business.is_open_for_business):
        return False
    return ellie.obedience > 160 and ellie.story_event_ready("obedience")

def add_ellie_submission_action():
    mc.business.add_mandatory_crisis(
        Action("Ellie's submission", ellie_submission_requirement, "ellie_submission_label")
    )
    ellie.story_event_log("obedience")


def ellie_nanobot_fetish_testing_requirement(person: Person):
    return False

def add_ellie_nanobot_fetish_testing_action():
    ellie.add_unique_on_room_enter_event(
        Action("Ellie's first fetish", ellie_nanobot_fetish_testing_requirement, "ellie_nanobot_fetish_testing_label", priority = 30)
    )
    ellie.event_triggers_dict["has_submit"] = True
    ellie.story_event_log("obedience")


def ellie_nanobot_fetish_requirement(person: Person):
    return False

def add_ellie_nanobot_fetish_action():
    ellie.add_unique_on_room_enter_event(
        Action("Give Ellie another fetish",
               ellie_nanobot_fetish_requirement,
               "ellie_nanobot_fetish_label",
               priority = 30)
    )
    ellie.story_event_log("obedience")
