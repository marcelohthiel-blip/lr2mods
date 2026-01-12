from __future__ import annotations

from game.bugfix_additions.ActionMod_ren import limited_time_event_pool
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.major_game_classes.character_related.Person_ren import Person, mc, mom
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def sleeping_walk_in_requirement(person: Person) -> bool:
    if not (time_of_day in (0, 4)): #ie. early morning (sleeping in) or late at night (early bed time)
        return False
    if person == mom and time_of_day == 0 and day % 7 == 5:
        return False #Don't want to trigger at the same time as the morning offer.
    if not person.is_home:
        return False
    if not person.is_family:
        return False
    if person.home.person_count > 1: #Nobody else in the room.
        return False
    return True

def reset_sleeping_walk_in_event(person: Person):
    if found := next((x for x in limited_time_event_pool if x.effect == "sleeping_walk_in_label"), None):
        person.add_unique_on_room_enter_event(Limited_Time_Action(found))

limited_time_event_pool.append(
    Action("Sleeping walk in", sleeping_walk_in_requirement, "sleeping_walk_in_label",
        event_duration = 1, priority = 8, trigger = "on_enter"))

# Menu Helper #

def build_sleep_climax_menu_options(person: Person, straddle = False, stomach_allowed = False, face_allowed = False, tits_allowed = False, throat_allowed = False, inside_allowed = False):
    climax_options = [("Cum in your hand", "air")]

    if stomach_allowed:
        climax_options.append(("Cum on her stomach", "body"))

    if tits_allowed:
        if person.effective_sluttiness() >= 30:
            climax_options.append(("Cum on her tits", "tits"))
        else:
            climax_options.append((f"Cum on her tits\n{{menu_red}}Requires: {get_gold_heart(30)}{{/menu_red}} (disabled)", "tits"))

    if face_allowed:
        if person.effective_sluttiness() >= 40:
            climax_options.append(("Cum on her face", "face"))
        else:
            climax_options.append((f"Cum on her face\n{{menu_red}}Requires: {get_gold_heart(40)}{{/menu_red}} (disabled)", "face"))

    if throat_allowed:
        if person.effective_sluttiness() >= 55:
            climax_options.append(("Cum down her throat", "throat"))
        else:
            climax_options.append((f"Cum down her throat\n{{menu_red}}Requires: {get_gold_heart(55)}{{/menu_red}} (disabled)", "throat"))

    if inside_allowed:
        if person.effective_sluttiness() >= 65 or mc.condom:
            climax_options.append(("Cum inside her", "pussy"))
        else:
            climax_options.append((f"Cum inside her\n{{menu_red}}Requires: {get_gold_heart(65)}{{/menu_red}} (disabled)", "pussy"))
    return climax_options
