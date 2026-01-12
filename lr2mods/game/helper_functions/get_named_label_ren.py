from __future__ import annotations
import renpy
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Person_ren import Person


"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

# Use get_named_label(str, person) to look and see if there is a named label for the person being passed in.
# Uses person.name and appends it to the front of the string name and searches to see if the specified label exists.
# returns False if no label is found
# returns True if found
# EG:
# if get_named_label("BC_TALK", mom):
#     return
#
# This would allow for an override of BC_TALK label

def get_named_label(label_name: str, person: Person) -> bool:
    label_name = person.func_name + '_' + label_name
    return renpy.has_label(label_name)

# Use run_named_label(str, person) to look and see if there is a named label for the person being passed in.
# If so, it runs the named version. If not, it runs the label name passed in.

def run_named_label(label_name: str, person: Person, *args, **kwargs):
    named_label = person.func_name + '_' + label_name
    if renpy.has_label(named_label):
        renpy.call(named_label, *args, **kwargs)
    else:
        renpy.call(label_name, person, *args, **kwargs)

def run_group_named_label(label_name: str, group: list[Person], *args, **kwargs):
    named_label_group = []
    for person in group:
        if get_named_label(label_name, person): #Check and see if there is a unique version of this
            named_label_group.append(person)
    if len(named_label_group) > 0:
        run_named_label(label_name, get_random_from_list(named_label_group), group, *args, **kwargs)
    else:
        renpy.call(label_name, group, *args, **kwargs)

# Below is a list of labels that use this format, allowing for custom labels for specific people
# "date_take_home_her_place"      Used for one night stands after a date.
# "date_her_place_spend_the_night_proposal"     When at a one night stand and she asks if MC wants to spend the night
# "date_her_place_morning_after_wakeup_label"       When waking up next to a one night stand
# "bc_talk_label"                 Used for discussing birth control status.
# "bc_demand_label"               Command version of birth control status

# Feb 1, 2025, added all date arrangement labels.
# lunch_date_plan_label             #In person
# movie_date_plan_label
# dinner_date_plan_label
# plan_fuck_date_label
# bar_date_plan_label
# lunch_date_text_plan_label        #From the phone
# movie_date_text_plan_label
# dinner_date_text_plan_label
# bar_date_text_plan_label

#ALL Bar games now use this option! The following are the label names that can be overridden:
# bar_date_arcade_label
# bar_date_billiards_label
# bar_date_salsa_label
# bar_date_darts_label
# bar_date_karaoke_label
# bar_date_trivia_label
# bar_date_pong_label
# bar_date_booth_label            Sex at the public booth. Probably the most interesting override possibility
# Modded bar games should automatically have this function as well.

#GROUP Bar games are ALSO included. If multiple girls in the group have an override, the code chooses one of them at random.
# bar_group_date_darts_label
# bar_group_date_karaoke_label
# bar_group_date_trivia_label
# bar_group_date_booth_label
