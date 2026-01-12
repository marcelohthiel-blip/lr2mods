# Activities is an abstraction for short activities players can have with girls.
# Primarily intended for dates, but not necessarily limited to them.
# They are generally available in the middle of a label, such as games played at the bar, or an item on the agenda at a work meeting.
# By default, they all have targetted overrides available, so that writers can modify each one for unique girls.
# This file is mostly a bunch of generic functions useful for all activities.
from __future__ import annotations
import renpy
from renpy import persistent
import builtins
from game.general_actions.interaction_actions.command_descriptions_definition_ren import demand_strip_naked_requirement, demand_strip_tits_requirement, demand_strip_underwear_requirement
from game.helper_functions.list_functions_ren import get_random_from_list
from game.business_policies.serum_policies_ren import mandatory_unpaid_serum_testing_policy, mandatory_paid_serum_testing_policy
from game.game_roles._role_definitions_ren import onlyfans_role
from game.game_roles.relationship_role_definition_ren import ask_girlfriend_requirement, evening_date_trigger, afternoon_date_trigger, morning_date_trigger, night_date_trigger
from game.major_game_classes.character_related.Person_ren import Person, mc, city_rep
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.Action_ren import Action

day = 0
time_of_day = 0
TIER_2_TIME_DELAY = 7
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""



# Use this for linking an activity shorthand for the name.
# Modded activities can use activity_names.append() to add
activity_names = {}
# activity_names["pong"] = "Beer Pong"
activity_names["salsa"] = "Salsa Dancing"
activity_names["arcade"] = "Super Street Kombat 2"
activity_names["billiards"] = "Billiards"
activity_names["darts"] = "Darts"
activity_names["karaoke"] = "Sing Karaoke"
activity_names["trivia"] = "Trivia Contest"

activity_response_list = ["salsa", "arcade", "billiards", "darts", "karaoke", "trivia"]

def get_activity_text(activity_name, person = None):
    entry_text = activity_names.get(activity_name, "Missing Activity Name")
    if person == None:
        return entry_text
    if activity_name in person.personality.activity_opinions:
        if person.personality.activity_opinions[activity_name] > 0:
            entry_text = "{color=#3DFF3D}" + entry_text + "{/color} (tooltip) She enjoys this activity"
        elif person.personality.activity_opinions[activity_name] < 0:
            entry_text = "{color=#FF0000}" + entry_text + "{/color} (tooltip) She does not enjoy this activity"
        else:
            entry_text = activity_names[activity_name]
    return entry_text

def get_group_activity_text(activity_name, group = None):
    entry_text = activity_names.get(activity_name, "Missing Activity Name")
    if group == None:
        return entry_text
    entry_text += "\n"
    for person in group:
        if person.personality.activity_opinions[activity_name] > 0:
            entry_text += "{color=#3DFF3D}" + person.name + " {/color}"
        elif person.personality.activity_opinions[activity_name] < 0:
            entry_text += "{color=#FF0000}" + person.name + " {/color}"
        else:
            entry_text += (person.name + " ")
    return entry_text

# Format an activity list for use in a menu displayable. Should return a list of tuples
def build_activity_list(activity_list, person = None):
    menu_list = []
    for activity in activity_list:
        menu_list.append(activity, get_activity_text(activity, person))
    return menu_list

def build_group_activity_list(activity_list, group = None):
    menu_list = []
    for activity in activity_list:
        menu_list.append(activity, get_group_activity_text(activity, group))
    return menu_list
