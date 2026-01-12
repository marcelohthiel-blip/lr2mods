import renpy
from renpy.character import Character
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.business_policies.special_policies_ren import unlock_unisex_bathroom_policy
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action
from game.major_game_classes.game_logic.Room_ren import lobby
from game.major_game_classes.character_related.Person_ren import Person, mc

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def unisex_restroom_fantasy_actout_requirement(person: Person):
    return (person.is_employee or person.is_intern) and mc.is_at_office and person.is_at_office

def unisex_restroom_gloryhole_wait_requirement():
    if mc.business.number_of_employees_at_office == 0:
        return "Nobody in the office!"
    if mc.business.event_triggers_dict.get("glory_hole_wait", 0) == time_of_day:
        return "Try again later"
    if mc.business.number_of_employees_at_office > 2:
        return True
    return "You should hire more employees"

def add_unisex_restroom_fantasy_actout_action(person: Person):
    unisex_restroom_fantasy_actout = Action("Act out dream fantasy", unisex_restroom_fantasy_actout_requirement, "unisex_restroom_fantasy_actout_label", event_duration = 5)
    person.add_unique_on_talk_event(Limited_Time_Action(unisex_restroom_fantasy_actout))
    return

def unlock_unisex_restroom_gloryhole_wait():
    unisex_restroom_gloryhole_wait = Action("Wait by the glory hole", unisex_restroom_gloryhole_wait_requirement, "unisex_restroom_gloryhole_wait_label")
    lobby.add_action(unisex_restroom_gloryhole_wait)
    return

def unisex_restroom_crisis_requirement():
    return (time_of_day in (1, 2)
        and day % 7 not in (4, 5, 6)    # not on Fridays / weekends
        and mc.business.has_event_delay("unisex_restroom_day", TIER_1_TIME_DELAY)
        and mc.is_at_office
        and mc.business.number_of_employees_at_office > 2)

def unisex_restroom_use_requirement():
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) == 0:
        return False
    return mc.business.number_of_employees_at_office > 2

def add_unisex_restroom_use_action():
    if not lobby.has_action("unisex_restroom_use_action_label"):
        unisex_restroom_room_use_action = Action("Use Unisex Restroom {image=time_advance}",
            unisex_restroom_use_requirement,
            "unisex_restroom_use_action_label")

        lobby.add_action(unisex_restroom_room_use_action)

def unisex_restroom_update_unlock_level():
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) < 6:
        current_level = mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0)
        unlock_unisex_bathroom_policy(current_level + 1)
    else:
        current_level = renpy.random.randint(2, 5)
    return current_level

def gloryhole_get_response(person: Person):    #this function creates a weight list of possible outcomes for the glory hole responses.
    gloryhole_list = []
    if person.sluttiness < 20: #They get pissed and refuse to do anything
        gloryhole_list.append("Refuse")
    else:
        gloryhole_list.append("Handjob")
        # actions based on sluttiness
        if person.sluttiness > 35:
            gloryhole_list.append("Blowjob")
        if person.sluttiness > 60:
            gloryhole_list.append("Vaginal")
            gloryhole_list.append("JoinMe")
        if person.sluttiness > 85:
            gloryhole_list.append("Anal")
    # actions based on fetishes (will always be added regardless of sluttiness)
    if person.has_cum_fetish:
        gloryhole_list.append("Blowjob")
    if person.has_breeding_fetish:
        gloryhole_list.append("Vaginal")
    if person.has_anal_fetish:
        gloryhole_list.append("Anal")

    return get_random_from_list(gloryhole_list)

def get_anon_person(person: Person):
    '''
    This function returns an anonymous version of a person (using the same font and colours).
    '''
    return Character("???", #The name to be displayed above the dialogue.
            what_font = person.char.what_args['font'], #The font to be used for the character.
            who_font = person.char.who_args['font'],
            color = person.char.who_args['color'], #The colour of the character's NAME section
            what_color = person.char.what_args['color'], #The colour of the character's dialogue.
            what_style = "general_dialogue_style")

unisex_restroom_crisis_action = ActionMod("Unisex Restroom", unisex_restroom_crisis_requirement, "unisex_restroom_action_label",
    menu_tooltip = "Change company restrooms to unisex and enjoy the results.", category="Business", is_crisis = True)
