from __future__ import annotations
import renpy
from game.major_game_classes.game_logic.Room_ren import hall, strip_club, lily_bedroom
from game.major_game_classes.character_related.Person_ren import Person, mc, aunt, cousin
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.character_related._job_definitions_ren import stripper_job

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
cousin_strip_pose_list = ["walking_away", "back_peek", "standing_doggy", "stand2", "stand3", "stand4", "stand5"] #A list to let us randomly get some poses so each dance is a little different.

def cousin_blackmail_requirement(person: Person):
    if person.is_sleeping or person.event_triggers_dict.get("blackmail_level", -1) < 1:
        return False
    if person.days_since_event("last_blackmailed") < 5:
        return "Blackmailed too recently"
    if mc.location.person_count > 1:
        return "Must be in private"
    return True

def get_cousin_role_actions():
    #COUSIN ACTIONS#
    cousin_blackmail_action = Action("Blackmail her", cousin_blackmail_requirement, "cousin_blackmail_label",
        menu_tooltip = "Threaten to tell her mother about what she's been doing and see what you can get out of her.", priority = 10)
    return [cousin_blackmail_action]

def init_cousin_roles():
    global cousin_role
    cousin_role = Role("Cousin", get_cousin_role_actions(), hidden = True)

def blackmail_hint_requirement(person: Person, min_day: int):
    if day < min_day or time_of_day != 4:
        return False
    elif person.sluttiness < 25:
        return False
    elif person.event_triggers_dict.get("blackmail_level", -1) != 1:
        return False
    return True

def add_cousin_blackmail_hint_action(person: Person):
    person.set_schedule(hall, day_slots = [0, 1, 2, 3, 4], time_slots = [2])
    person.event_triggers_dict["blackmail_level"] = 1

    mc.business.add_mandatory_crisis(
        Action("Blackmail hint", blackmail_hint_requirement, "aunt_cousin_hint_label", args = [aunt, person], requirement_args = [person, day + renpy.random.randint(2, 4)])
    )


def cousin_serum_boobjob_check_requirement(the_day: int):
    return day >= the_day

def add_cousin_serum_boobjob_check_action(person: Person):
    person.event_triggers_dict["serum_boobjob"] = True #Reset the flag so you can ask her to get _another_ boobjob.
    mc.business.add_mandatory_crisis(
        Action("Cousin serum boobjob check", cousin_serum_boobjob_check_requirement, "cousin_serum_boobjob_label", args = [person, person.tits], requirement_args = [day + 3])
    )


def cousin_boobjob_get_requirement(start_day: int):
    return day >= start_day

def add_cousin_boobjob_get_action(person: Person):
    #Sets up an event that will trigger after a set number of days when she has gotten her boob job. This event, in turns, adds in an event when you talk to her.
    person.event_triggers_dict["getting boobjob"] = True #Reset the flag so you can ask her to get _another_ boobjob.
    mc.business.add_mandatory_crisis(
        Action("Cousin boob job get", cousin_boobjob_get_requirement, "cousin_boobjob_get_label", args = person, requirement_args = [day + renpy.random.randint(4, 6)])
    )


def cousin_tits_payback_requirement(the_day: int):
    return day >= the_day

def add_cousin_tits_payback_action(person: Person, amount):
    mc.business.add_mandatory_crisis(
        Action("cousin tits payback", cousin_tits_payback_requirement, "cousin_tits_payback_label", args = [person, amount], requirement_args = day + 7)
    ) #An event where she sends you some cash in a week, which if it has not finished then re-adds itself with the new amount


def blackmail_2_confront_requirement(person: Person):
    if person.event_triggers_dict.get("blackmail_level", -1) != 1 or person.is_sleeping:
        return False
    if mc.location.person_count > 1:
        return "Not with other people around"
    if person.get_destination() == strip_club:
        return "Not in the strip club"
    return True

def add_cousin_blackmail_2_confront_action():
    cousin.add_action(
        Action("Confront her about her stripping", blackmail_2_confront_requirement, "cousin_blackmail_level_2_confront_label",
            menu_tooltip = "Tell her that you know about her job as a stripper and use it as further leverage.")
    )
    cousin.event_triggers_dict["seen_cousin_stripping"] = True

def remove_cousin_blackmail_2_confront_action():
    cousin.remove_action("cousin_blackmail_level_2_confront_label")

def cousin_house_phase_two_requirement(person: Person):
    return person.is_at(hall)

def add_cousin_at_house_phase_two_action(person: Person):
    #Changes her schedule to be at your house
    if not person.has_queued_event("cousin_house_phase_two_label"):
        person.set_schedule(hall, day_slots = [0, 1, 2, 3, 4], time_slots = [2])
        person.add_unique_on_room_enter_event(
            Action("Cousin visits house", cousin_house_phase_two_requirement, "cousin_house_phase_two_label", priority = 30)
        ) #When you see her next in your house this event triggers and she explains why she's there.


def cousin_house_phase_three_requirement(day_trigger: int):
    return day >= day_trigger

def add_cousin_at_house_phase_three_action():
    mc.business.add_mandatory_crisis(
        Action("Cousin changes schedule", cousin_house_phase_three_requirement, "cousin_house_phase_three_label", args = cousin, requirement_args = day + renpy.random.randint(2, 5))
    ) #In a couple of days change her schedule so she starts stealing from Lily.


def cousin_blackmail_intro_requirement(person: Person):
    #Only triggers when she's in there alone (and after the event has been added to the trigger list)
    return person.event_triggers_dict.get("blackmail_level", -1) < 0 and person.is_at(lily_bedroom) and lily_bedroom.person_count == 1

def add_cousin_blackmail_intro_action(person: Person):
    if not person.has_queued_event("cousin_blackmail_intro_label"):
        person.set_schedule(lily_bedroom, day_slots = [0, 1, 2, 3, 4], time_slots = [2])
        person.add_unique_on_room_enter_event(
            Action("Cousin caught stealing", cousin_blackmail_intro_requirement, "cousin_blackmail_intro_label", priority = 30)
        )

def cousin_room_search_requirement(person: Person):
    if person.event_triggers_dict.get("blackmail_level", -1) != 1:
        return False
    elif person.event_triggers_dict.get("found_stripping_clue", False):
        return False
    elif time_of_day == 4:
        return "Too late to search room"
    elif person.is_at(mc.location):
        return person.title + " is in the room"
    return True

def add_cousin_stripping_and_setup_search_room_action(the_aunt: Person, the_cousin: Person):
    the_cousin.change_job(stripper_job, is_primary = False, job_known = False)
    cousin.bedroom.add_action(
        Action("Search her room {image=time_advance}", cousin_room_search_requirement, "cousin_search_room_label", requirement_args = [the_cousin], args = [the_cousin, the_aunt])
    ) #Lets you search her room for a clue about where to go to find her.

def cousin_unlock_stripclub(person: Person):
    strip_club.visible = True
    person.event_triggers_dict["seen_cousin_stripping"] = True
    person.event_triggers_dict["blackmail_level"] = 2

def cousin_boobjob_ask_requirement(person: Person, start_day: int):
    if day < start_day or person.sluttiness < 40 or not person.is_strip_club_employee:
        return False
    if person.event_triggers_dict.get("getting boobjob", False):
        return False
    if Person.rank_tits(person.tits) >= Person.rank_tits("F"):
        return False #She already has F sized tits, which she thinks is good enough.
    if aunt.is_at(mc.location) or person.is_sleeping:
        return False
    return True

def add_cousin_boobjob_ask_action(person: Person):
    person.on_talk_event_list.add_action(
        Action("Cousin Boobjob Ask", cousin_boobjob_ask_requirement, "cousin_boobjob_ask_label", requirement_args = day + renpy.random.randint(3, 6))
    )


def cousin_new_boobs_brag_requirement(person: Person):
    return person.location.person_count <= 1

def add_cousin_boobjob_brag_action(person: Person):
    person.on_talk_event_list.add_action(
        Action("Cousin new boobs brag", cousin_new_boobs_brag_requirement, "cousin_new_boobs_brag_label")
    ) #Next time you talk to her she brags about her new boobs, offers to show them to you, and tells you that she'll pay you back eventually.


def cousin_talk_boobjob_again_requirement(person: Person):
    if person.sluttiness < 40 or person.event_triggers_dict.get("getting boobjob", False) or not person.is_strip_club_employee:
        return False
    if aunt.is_at(mc.location):
        return "Not while [aunt.title] is around"
    return True

def add_cousin_talk_boobjob_again_action():
    cousin.add_action(
        Action("Talk about getting a boobjob\n{menu_red}Costs: $5000{/menu_red}", cousin_talk_boobjob_again_requirement, "cousin_talk_boobjob_again_label")
    )

def remove_cousin_talk_boobjob_again_action():
    cousin.remove_action("cousin_talk_boobjob_again_label")
