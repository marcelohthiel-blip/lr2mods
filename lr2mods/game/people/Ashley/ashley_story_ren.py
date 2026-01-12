#This is currently a test file only
#Use this file to test Story_Step and Story_Path commands, slowly converting Ashley to the updated system.
#Currently testing only her Obedience story steps.
#This story path is exclusive to Ashley

from __future__ import annotations
import builtins
import renpy
from renpy.display import im
from game.business_policies.serum_policies_ren import testing_room_creation_policy
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.BackGroundManager_ren import bg_manager
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import darken_matrix
from game.main_character.mc_serums._mc_serum_definitions_ren import mc_serum_energy_regen
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.major_game_classes.character_related.Person_ren import Person, mc, ashley, stephanie
from game.major_game_classes.character_related.Story_ren import Story_Step, Story_Path

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
clothing_fade = None
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""


#### Submission Story Path ####
#This story requires Ashley to be our Production Assistant#
# Step 0

# Actions
def ashley_submission_titfuck_requirement():
    return( ashley.obedience >= 120 and ashley.sluttiness >= 20 and mc.business.is_open_for_business
    and ashley.story_event_ready("submission")
    and mc.is_at_office)

def ashley_work_titfuck_requirement(person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.event_triggers_dict.get("sub_titfuck_taboo_regen", False) or person.event_triggers_dict.get("sub_titfuck_count", 0) == 0:
        return False
    if (person.obedience >= 120 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 120 obedience"

#Step Functions
def ashley_submission_story_0_init(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Fuck ashley's tits", ashley_submission_titfuck_requirement, "ashley_submission_titfuck_label")
    )
    
    #TODO add taboo regen if applicable

    ashley.story_event_log("submission")
    ashley.add_action(Action("Submission: Fuck Her Tits", ashley_work_titfuck_requirement, "ashley_work_titfuck_label", priority = 20))
    ashley.event_triggers_dict["submission_path_index"] = 0
    return True

def ashley_submission_story_0_finish(person: Person):
    person.remove_action("ashley_work_titfuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_titfuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_titfuck_taboo_restore_label")
    person.event_triggers_dict["sub_titfuck_avail"] = True
    person.event_triggers_dict["sub_titfuck_taboo_regen"] = False
    return True

def ashley_submission_story_0_cheat_to(person: Person):
    person.event_triggers_dict["sub_titfuck_count"] = 0
    return

def ashley_submission_story_0_cheat_past(person: Person):
    person.event_triggers_dict["sub_titfuck_avail"] = True
    person.event_triggers_dict["sub_titfuck_count"] = 3
    return
    
def ashley_submission_story_0_remove(person: Person):
    person.remove_action("ashley_work_titfuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_titfuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_titfuck_taboo_restore_label")
    return

def ashley_submission_story_0_progress(person: Person, complete: bool):
    if complete:
        return "You've convinced [person.fname] to let you fuck her tits after work whenever you want."
    if person.event_triggers_dict.get("sub_titfuck_taboo_regen", False):
        return "You fucked [person.fname]'s tits, but she didn't seem happy about it. She'll probably contact you soon."
    elif person.event_triggers_dict.get("sub_titfuck_count", 0) > 0:
        return "Talk to [person.fname] when she has at least 120 obedience to fuck her tits again."
    elif person.obedience < 120:
        return "Raise [person.fname]'s obedience to at least 120."
    elif person.sluttiness < 20:
        return "Raise [person.fname]'s sluttiness to at least 20."
    else:
        return "An event will occur with [person.fname] in the evening on a workday soon..."
    return "Error"

ashley_submission_story_0_step = Story_Step(ashley_submission_story_0_init, ashley_submission_story_0_finish,
                                          ashley_submission_story_0_cheat_to, ashley_submission_story_0_cheat_past,
                                          ashley_submission_story_0_remove, ashley_submission_story_0_progress)

#Step 1

#Actions
def ashley_submission_blowjob_requirement():
    return ( ashley.obedience >= 140 and ashley.sluttiness >= 40 and mc.business.is_open_for_business
    and ashley.story_event_ready("submission")
    and mc.is_at_office)

def ashley_work_blowjob_requirement(person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.event_triggers_dict.get("sub_blowjob_taboo_regen", False) or person.event_triggers_dict.get("sub_blowjob_count", 0) == 0:
        return False
    if (person.obedience >= 140 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 140 obedience"

#Step Functions

def ashley_submission_story_1_init(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Fuck Ashley", ashley_submission_blowjob_requirement, "ashley_submission_blowjob_label")
    )

    ashley.story_event_log("submission")
    ashley.add_action(Action("Submission: Blowjob", ashley_work_blowjob_requirement, "ashley_work_blowjob_label", priority = 20))
    ashley.event_triggers_dict["submission_path_index"] = 1
    return True

def ashley_submission_story_1_finish(person: Person):
    person.remove_action("ashley_work_blowjob_label")
    mc.business.remove_mandatory_crisis("ashley_submission_blowjob_label")
    mc.business.remove_mandatory_crisis("ashley_submission_blowjob_taboo_restore_label")
    person.event_triggers_dict["sub_blowjob_avail"] = True
    person.event_triggers_dict["sub_blowjob_taboo_regen"] = False
    return True

def ashley_submission_story_1_cheat_to(person: Person):
    person.event_triggers_dict["sub_blowjob_count"] = 0
    return

def ashley_submission_story_1_cheat_past(person: Person):
    person.event_triggers_dict["sub_blowjob_avail"] = True
    person.event_triggers_dict["sub_blowjob_count"] = 3
    return
    
def ashley_submission_story_1_remove(person: Person):
    person.remove_action("ashley_work_blowjob_label")
    mc.business.remove_mandatory_crisis("ashley_submission_blowjob_label")
    mc.business.remove_mandatory_crisis("ashley_submission_blowjob_taboo_restore_label")
    return

def ashley_submission_story_1_progress(person: Person, complete: bool):
    if complete:
        return "She'll even get on her knees and suck you off."
    if person.event_triggers_dict.get("sub_blowjob_taboo_regen", False):
        return "You fucked [person.fname]'s mouth, but she didn't seem happy about it. She'll probably contact you soon."
    elif person.event_triggers_dict.get("sub_blowjob_count", 0) > 0:
        return "Talk to [person.fname] when she has at least 140 obedience to fuck her mouth again."
    elif person.obedience < 140:
        return "Raise [person.fname]'s obedience to at least 140."
    elif person.sluttiness < 40:
        return "Raise [person.fname]'s sluttiness to at least 40."
    else:
        return "An event will occur with [person.fname] in the evening on a workday soon..."
    return "Error"

ashley_submission_story_1_step = Story_Step(ashley_submission_story_1_init, ashley_submission_story_1_finish,
                                          ashley_submission_story_1_cheat_to, ashley_submission_story_1_cheat_past,
                                          ashley_submission_story_1_remove, ashley_submission_story_1_progress)

#Step 2

#Actions
def ashley_submission_fuck_requirement():
    return ( ashley.obedience >= 160 and ashley.sluttiness >= 60 and mc.business.is_open_for_business
    and ashley.story_event_ready("submission")
    and mc.is_at_office)

def ashley_work_fuck_requirement(person):
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if person.event_triggers_dict.get("sub_fuck_taboo_regen", False) or person.event_triggers_dict.get("sub_fuck_count", 0) == 0:
        return False
    if (person.obedience >= 160 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 160 obedience"

#Step Functions

def ashley_submission_story_2_init(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Fuck Ashley", ashley_submission_fuck_requirement, "ashley_submission_fuck_label")
    )

    ashley.story_event_log("submission")
    ashley.add_action(Action("Submission: Fuck", ashley_work_fuck_requirement, "ashley_work_fuck_label", priority = 20))
    ashley.event_triggers_dict["submission_path_index"] = 2
    return

def ashley_submission_story_2_finish(person: Person):
    person.remove_action("ashley_work_fuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_fuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_fuck_taboo_restore_label")
    person.event_triggers_dict["sub_fuck_avail"] = True
    person.event_triggers_dict["sub_fuck_taboo_regen"] = False
    return

def ashley_submission_story_2_cheat_to(person: Person):
    person.event_triggers_dict["sub_fuck_count"] = 0
    return

def ashley_submission_story_2_cheat_past(person: Person):
    person.event_triggers_dict["sub_fuck_avail"] = True
    person.event_triggers_dict["sub_fuck_count"] = 3
    return
    
def ashley_submission_story_2_remove(person: Person):
    person.remove_action("ashley_work_fuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_fuck_label")
    mc.business.remove_mandatory_crisis("ashley_submission_fuck_taboo_restore_label")
    return

def ashley_submission_story_2_progress(person: Person, complete: bool):
    if complete:
        return "You've even trained [ashley.fname] to bend over your desk."
    if person.event_triggers_dict.get("sub_fuck_taboo_regen", False):
        return "You fucked [person.fname] bent over your desk, but she didn't seem happy about it. She'll probably contact you soon."
    elif person.event_triggers_dict.get("sub_fuck_count", 0) > 0:
        return "Talk to [person.fname] when she has at least 160 obedience to fuck her again."
    elif person.obedience < 160:
        return "Raise [person.fname]'s obedience to at least 160."
    elif person.sluttiness < 60:
        return "Raise [person.fname]'s sluttiness to at least 60."
    else:
        return "An event will occur with [person.fname] in the evening on a workday soon..."
    return "Error"

ashley_submission_story_2_step = Story_Step(ashley_submission_story_2_init, ashley_submission_story_2_finish,
                                          ashley_submission_story_2_cheat_to, ashley_submission_story_2_cheat_past,
                                          ashley_submission_story_2_remove, ashley_submission_story_2_progress)

def ashley_submission_path_req():
    if mc.business.prod_assistant == ashley:
        return True
    return False

ashley_story_path_submission = Story_Path("Submission",
        [ashley_submission_story_0_step, ashley_submission_story_1_step, ashley_submission_story_2_step],
        False,
        ashley_submission_path_req,
        "Ashley must be your Production Assistant to begin this story path.")
