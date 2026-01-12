from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import sex_store
from game.major_game_classes.character_related.Person_ren import Person, mc, starbuck
from game.people.Starbuck.starbuck_role_definition_ren import sex_shop_stage

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

#### Love Events ####

def starbuck_coffee_time_requirement():
    if time_of_day == 1 and starbuck.love > 20 and starbuck.event_triggers_dict.get("shop_progress_stage", 0) >= 1.0 and starbuck.story_event_ready("love"):
        return True
    return False

def add_starbuck_coffee_time_action():
    mc.business.add_mandatory_crisis(
        Action("Starbuck meets for Coffee", starbuck_coffee_time_requirement, "starbuck_coffee_time_label")
    )
    starbuck.story_event_log("love")

def starbuck_rebound_talk_requirement():
    if time_of_day == 1 and starbuck.love > 40 and starbuck.story_event_ready("love"):
        return True
    return False

def add_starbuck_rebound_talk_action():
    mc.business.add_mandatory_crisis(
        Action("Starbuck meets for Lunch", starbuck_rebound_talk_requirement, "starbuck_rebound_talk_label")
    )
    starbuck.story_event_log("love")

#### Lust Events ####

def starbuck_foreplay_enhancer_requirement(person: Person):
    return (time_of_day == 3
        and person.sluttiness > 20
        and person.is_at_work
        and person.story_event_ready("slut"))

def add_starbuck_foreplay_enhancer_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck foreplay enhancer", starbuck_foreplay_enhancer_requirement, "starbuck_foreplay_enhancer_label", priority = 30)
    )
    starbuck.story_event_log("slut")

def starbuck_oral_enhancer_requirement(person: Person):
    return (time_of_day == 3
        and person.sluttiness > 40
        and person.is_at_work
        and person.story_event_ready("slut"))

def add_starbuck_oral_enhancer_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck oral enhancer", starbuck_oral_enhancer_requirement, "starbuck_oral_enhancer_label", priority = 30)
    )
    starbuck.story_event_log("slut")

def starbuck_vaginal_enhancer_requirement(person: Person):
    return (time_of_day == 3
        and sex_shop_stage() >= 2.0
        and person.sluttiness > 60
        and person.is_at_work
        and person.story_event_ready("slut"))

def add_starbuck_vaginal_enhancer_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck vaginal enhancer", starbuck_vaginal_enhancer_requirement, "starbuck_vaginal_enhancer_label", priority = 30)
    )
    starbuck.story_event_log("slut")

def starbuck_anal_enhancer_requirement(person: Person):
    return (time_of_day == 3
        and person.sluttiness > 80
        and person.is_at_work
        and person.story_event_ready("slut"))

def add_starbuck_anal_enhancer_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck anal enhancer", starbuck_anal_enhancer_requirement, "starbuck_anal_enhancer_label", priority = 30)
    )
    starbuck.story_event_log("slut")

#### Obedience Events ####
def starbuck_no_profit_requirement(person: Person):
    return (time_of_day == 3
        and person.obedience >= 120
        and person.is_at_work
        and person.story_event_ready("obedience"))

def add_starbuck_no_profit_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck's Money Problems", starbuck_no_profit_requirement, "starbuck_no_profit_label", priority = 30)
    )
    starbuck.story_event_log("obedience")

#140 events
def starbuck_dressup_intro_requirement(person: Person):
    return (time_of_day == 3
        and person.obedience >= 80
        and person.is_at_work
        and person.story_event_ready("obedience"))

def add_starbuck_dressup_intro_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck Work Uniform", starbuck_dressup_intro_requirement, "starbuck_dressup_intro_label", priority = 30)
    )
    starbuck.story_event_log("obedience")

def starbuck_dressup_recap_requirement(person: Person):
    if day < starbuck.event_triggers_dict.get("recap_day", 0):
        return False
    return person.is_at_work

def add_starbuck_dressup_recap_action():
    starbuck.add_unique_on_talk_event(
        Action("Starbuck Uniform recap", starbuck_dressup_recap_requirement, "starbuck_dressup_recap_label", priority = 30)
    )
    starbuck.event_triggers_dict["recap_day"] = day + 2

def starbuck_dressup_retry_requirement(person: Person):
    return (time_of_day == 3
        and person.obedience >= 140
        and person.is_at_work
        and person.story_event_ready("obedience"))

def add_starbuck_dressup_retry_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck Uniform retry", starbuck_dressup_retry_requirement, "starbuck_dressup_retry_label", priority = 30)
    )

#160 events - Disabled for now, did not have time to complete
def starbuck_underwear_intro_requirement(person: Person):
    return False
    return (time_of_day == 3
        and person.obedience >= 160
        and person.is_at_work
        and person.story_event_ready("obedience"))

def add_starbuck_underwear_intro_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck Underwear Uniform", starbuck_underwear_intro_requirement, "starbuck_underwear_intro_label", priority = 30)
    )
    starbuck.story_event_log("obedience")

def starbuck_underwear_recap_requirement(person: Person):
    return False
    if day < starbuck.event_triggers_dict.get("recap_day", 0):
        return False
    return person.is_at(sex_store)

def add_starbuck_underwear_recap_action():
    starbuck.add_unique_on_talk_event(
        Action("Starbuck Underwear recap", starbuck_underwear_recap_requirement, "starbuck_underwear_recap_label", priority = 30)
    )
    starbuck.event_triggers_dict["recap_day"] = day + 2

def starbuck_underwear_retry_requirement(person: Person):
    return False
    if time_of_day == 3 and person.obedience >= 160 and person.is_at_work:
        return True
    return False

def add_starbuck_underwear_retry_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Starbuck Underwear retry", starbuck_underwear_retry_requirement, "starbuck_underwear_retry_label", priority = 30)
    )


#### Personal Lubricant Story Arc ####

def starbuck_lubricant_shortage_requirement(person: Person):
    return False

def add_starbuck_lubricant_shortage_action():
    starbuck.add_unique_on_room_enter_event(
        Action("Lube Shortage", starbuck_lubricant_shortage_requirement, "starbuck_lubricant_shortage_label", priority = 30)
    )
