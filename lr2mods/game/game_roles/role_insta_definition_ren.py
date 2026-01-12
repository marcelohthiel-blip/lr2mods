from __future__ import annotations
import renpy
from game.game_roles._role_definitions_ren import instapic_role
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Action_ren import Action

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
def insta_would_ban(outfit: Outfit): #Helper function for Insta related stuff. Returns True if an outfit would get you banned from InstaPic.
    return outfit.tits_visible or outfit.vagina_visible

def comment_action_requirement(person: Person):
    if person.get_event_day("insta_commented_day") == day:
        return "Already commented today"
    return True

def dm_action_requirement(person: Person):
    if person.event_triggers_dict.get("insta_special_request_pending", False):
        return "Waiting for her reply"
    return True

def dm_option_specific_outfit_requirement(person: Person):
    return True

def dm_option_underwear_requirement(person: Person):
    return True

def dm_option_topless_requirement(person: Person):
    return True

def dm_option_nude_requirement(person: Person):
    return True

def dm_response_requirement(person: Person):
    if renpy.random.randint(0, 100) < 60 and not person.event_triggers_dict.get("insta_special_request_asap", False): #Respond at a random time, not as soon as possible.
        return False
    elif person.is_at_work and person.obedience >= 160: #Obedient girls don't try and take pics at work.
        return False
    elif person.is_at(mc.location) and mc.location.is_public:
        return False #If she's in the same location as us and we are in public she doesn't take the picture.
    elif mc.is_at(person.home) and person.is_home: #Doesn't do it if she's at home and you're in the room with her (mainly for Lily/Mom)
        return False
    return True

def insta_dm_cleanup(person: Person): #Resets all the appropriate flags that should be reset after a response has been given.
    person.event_triggers_dict["insta_special_request_pending"] = False
    if person.event_triggers_dict.get("insta_special_request_sis", None):
        person.event_triggers_dict["insta_special_request_sis"] = None
    return

def build_insta_menu():
    insta_list = ["Accounts You Know"]
    insta_list.extend((x for x in mc.phone.get_person_list() if x.instapic_known))

    other_options_list = ["Other Options", "Back"]
    return [insta_list, other_options_list]

def build_instapic_comment_actions(person: Person, posted_today: bool):
    display_list = []

    if posted_today:
        nice_comment_action = Action("Leave a nice comment", comment_action_requirement, "comment_description", requirement_args = person, args = ["nice"])
        mean_comment_action = Action("Leave a mean comment", comment_action_requirement, "comment_description", requirement_args = person, args = ["mean"])
        sexy_comment_action = Action("Leave a sexual comment", comment_action_requirement, "comment_description", requirement_args = person, args = ["sexy"])

        comment_list = ["Comment", nice_comment_action, mean_comment_action, sexy_comment_action]
        display_list.append(comment_list)

    dm_request_action = Action("Ask for something special", dm_action_requirement, "dm_description", requirement_args = person)
    dm_list = ["Direct message her", dm_request_action]
    display_list.append(dm_list)

    other_list = ["Other Options"]
    other_list.append("Back")
    display_list.append(other_list)
    return display_list

def build_dm_description_actions(person: Person):
    dm_option_specific_outfit_action = Action("Wear a specific outfit\n{menu_red}Costs: $20{/menu_red}", dm_option_specific_outfit_requirement, "dm_option_specific_outfit", requirement_args = person)
    dm_option_underwear_action = Action("Show me your underwear\n{menu_red}Costs: $50{/menu_red}", dm_option_underwear_requirement, "dm_option_underwear", requirement_args = person)
    dm_option_topless_action = Action("Show me your tits\n{menu_red}Costs: $100{/menu_red}", dm_option_topless_requirement, "dm_option_topless", requirement_args = person)
    dm_option_nude_action = Action("Send me some nudes\n{menu_red}Costs: $200{/menu_red}", dm_option_nude_requirement, "dm_option_nude", requirement_args = person)
    dm_options = ["Make a request", dm_option_specific_outfit_action, dm_option_underwear_action, dm_option_topless_action, dm_option_nude_action]

    other_list = ["Other Options"]
    other_list.append("Back")
    return [dm_options, other_list]

def add_dm_outfit_response(person: Person, outfit: Outfit):
    mc.business.add_mandatory_crisis(
        Action("DM outfit response", dm_response_requirement, "dm_option_specific_outfit_response", args = [person, outfit], requirement_args = person)
    )

def add_dm_underwear_response(person: Person):
    mc.business.add_mandatory_crisis(
        Action("DM underwear response", dm_response_requirement, "dm_option_underwear_response", args = person, requirement_args = person)
    )

def add_dm_topless_response(person: Person):
    mc.business.add_mandatory_crisis(
        Action("DM topless response", dm_response_requirement, "dm_option_topless_response", args = person, requirement_args = person)
    )

def add_dm_nude_response(person: Person):
    mc.business.add_mandatory_crisis(
        Action("DM topless response", dm_response_requirement, "dm_option_nude_response", args = person, requirement_args = person)
    )
