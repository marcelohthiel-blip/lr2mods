from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import mc, mom, stripper_job, stripclub_stripper_job
from game.map.map_code_ren import mom_office_is_open
from game.game_roles.stripclub._stripclub_role_definitions_ren import get_strip_club_foreclosed_stage
from game.people.Jennifer.jennifer_definition_ren import mom_secretary_job, mom_associate_job

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def sleep_action_requirement():
    if time_of_day != 4:
        return "Too early to sleep"
    return True

def bedroom_masturbate_requirement():
    if time_of_day >= 4:
        return "Not enough time"
    elif mc.location.person_count > 0:
        return "Not with someone around"
    elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
        return "Finish tutorial first"
    return True

def mc_bedroom_actions():
    #PC Bedroom actions#
    sleep_action = Action("Sleep for the night {image=time_advance}{image=time_advance}", sleep_action_requirement, "sleep_action_description",
        menu_tooltip = "Go to sleep and advance time to the next day. Night time counts as three time chunks when calculating serum durations.", priority = 20)
    bedroom_masturbate_action = Action("Masturbate {image=time_advance}", bedroom_masturbate_requirement, "bedroom_masturbation",
        menu_tooltip = "Jerk off. A useful way to release Clarity, but you'll grow bored of this eventually.")

    return [sleep_action, bedroom_masturbate_action]


def mom_room_search_requirement():
    if mom.is_at_mc_house:
        return f"Not with {mom.fname} around"
    elif mc.energy < 15:
        return "Requires: {energy=15}"
    return True

def mom_bedroom_actions():
    ##Mom Bedroom Actions##
    mom_room_search_action = Action("Search [mom.title]'s room {energy=-15}", mom_room_search_requirement, "mom_room_search_description",
        menu_tooltip = "Take a look around and see what you can find.")
    return [mom_room_search_action]


def mom_office_person_request_requirement():
    return (
        mom_office_is_open()
        and mom.has_job((mom_secretary_job, mom_associate_job))
    )

def mom_office_actions():
    mom_office_person_request_action = Action("Approach the receptionist", mom_office_person_request_requirement, "mom_office_person_request",
        menu_tooltip = "The receptionist might be able to help you, if you're looking for someone.")

    return [mom_office_person_request_action]


def downtown_search_requirement():
    if time_of_day >= 4:
        return "Too late to explore"
    return True

def downtown_actions():
    downtown_search_action = Action("Wander the streets {image=time_advance}", downtown_search_requirement, "downtown_search_label",
        menu_tooltip = "Spend time exploring the city and seeing what interesting locations it has to offer.")

    return [downtown_search_action]


def stripclub_show_requirement():
    if get_strip_club_foreclosed_stage() in (1, 2, 3, 4):
        return False
    if not any(x for x in mc.location.people if x.has_job((stripper_job, stripclub_stripper_job))):
        return False
    if time_of_day in (0, 1, 2):
        return "Too early for performances"
    if not mc.owns_strip_club and not mc.business.has_funds(20):
        return "Not enough cash"
    return True

def strip_club_set_uniforms_requirement():
    return mc.owns_strip_club

def strip_club_actions():
    strip_club_show_action = Action("Watch a show", stripclub_show_requirement, "stripclub_dance",
        menu_tooltip = "Take a seat and wait for the next girl to come out on stage.")
    strip_club_set_uniforms_action = Action("Manage Stripclub Uniforms", strip_club_set_uniforms_requirement, "strip_club_set_uniforms_label",
        menu_tooltip = "Assign the uniforms your stripclub employees will wear.")

    return [strip_club_show_action, strip_club_set_uniforms_action]
