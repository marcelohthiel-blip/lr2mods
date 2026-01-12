#Use this file to test Story_Step and Story_Path commands for Nora's University Contract storyline.
#This story path is exclusive to Nora

from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, mc, nora
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

### University Contract Path ###
# This path details Nora's contracts with MC for serums on behalf of the university.
# As the path progresses, MC uses obedience to convince her to dose the University Dean
# MC can eventually use Nora to control the University Dean, one of the city council members.

####    EVENT_DICT_VARIABLES    ####
# nora
# "nora_contracts_intro_complete":   bool           Set this after the intro for dialogue purposes.
# "nora_contract_count":    int                     The number of contracts for Nora that MC has completed
# "dean_deal_proposed":   bool                      Has the Dean made a counteroffer
# "dean_contract_count":    int                     The number of contracts we have completed for the Dean
# "may_have_toys":  bool                            Set during the epilogue. Not currently used, but True allows Nora to have playthings

####    Step Discriptions       ####
#[0]        After the Intro, until we have 2 completed contracts.
#[1]        Increased requirement for contracto to require obedience trait. Reqs 2 completed contracts and 120 obedience
#[2]        Meet with the University Dean and receive counter offers. Reqs 4 completed contracts and 140 obedience
#[3]        Dean has been tamed. Reqs 6 contracts and 160 obedience
#[4]        Epilogue step. Dean is tamed, and Nora now has control of the council vote on your behalf.


# Step 0
# Intro until we have completed 2 contracts.
# Actions:
# None! These are all a part of Nora's weekly meetings.

# Step Functions

#normal INIT is when MC receives his first contrct, so intro must be complete.
def nora_university_contracts_story_0_init(person: Person):
    nora.event_triggers_dict["nora_contracts_intro_complete"] = True
    return True

def nora_university_contracts_story_0_finish(person: Person):
    return True

def nora_university_contracts_story_0_cheat_to(person: Person):
    nora.event_triggers_dict["nora_contracts_intro_complete"] = False
    nora.event_triggers_dict["nora_contract_count"] = 0
    nora.event_triggers_dict["dean_deal_proposed"] = False
    nora.event_triggers_dict["dean_contract_count"] = 0
    nora.event_triggers_dict["may_have_toys"] = False
    return

def nora_university_contracts_story_0_cheat_past(person: Person):
    nora.event_triggers_dict["nora_contracts_intro_complete"] = True
    nora.event_triggers_dict["nora_contract_count"] = 2
    return

def nora_university_contracts_story_0_remove(person: Person):
    return

def nora_university_contracts_story_0_progress(person: Person, complete: bool):
    nora.event_triggers_dict.get("contract_count", 0)
    return_string = "You have completed " + str(nora.event_triggers_dict.get("contract_count", 0)) + " University serum contracts.\n"
    return_string += "[person.name] is offering you official University serum contracts."
    if complete:
        return_string += "These contracts now require an obedience trait."
    else:
        return_string += "Complete at least two contracts and raise [person.name]'s obedience above 120."
    return return_string

nora_university_contracts_story_0_step = Story_Step(nora_university_contracts_story_0_init, nora_university_contracts_story_0_finish,
                                          nora_university_contracts_story_0_cheat_to, nora_university_contracts_story_0_cheat_past,
                                          nora_university_contracts_story_0_remove, nora_university_contracts_story_0_progress)

# Step 1
# Intro increase obedience req, finished we schedule a dean meeting.
# Actions:
# None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_university_contracts_story_1_init(person: Person):
    return True

def nora_university_contracts_story_1_finish(person: Person):
    return True

def nora_university_contracts_story_1_cheat_to(person: Person):
    nora.event_triggers_dict["dean_deal_proposed"] = False
    nora.event_triggers_dict["dean_contract_count"] = 0
    nora.event_triggers_dict["may_have_toys"] = False
    return

def nora_university_contracts_story_1_cheat_past(person: Person):
    nora.obedience = 140
    nora.event_triggers_dict["nora_contract_count"] = 4
    return

def nora_university_contracts_story_1_remove(person: Person):
    pass
    return

def nora_university_contracts_story_1_progress(person: Person, complete: bool):
    if complete:
        return "Her contracts have caught the University Dean's attention."
    else:
        return "Complete at least four contracts and raise [person.name]'s obedience above 140."
    return ""

nora_university_contracts_story_1_step = Story_Step(nora_university_contracts_story_1_init, nora_university_contracts_story_1_finish,
                                          nora_university_contracts_story_1_cheat_to, nora_university_contracts_story_1_cheat_past,
                                          nora_university_contracts_story_1_remove, nora_university_contracts_story_1_progress)

# Step 2
# intro we need to meet the dean. Mid- we met the dean and make serums for one or the other. Finish we tamed the dean.
# Actions:
# None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_university_contracts_story_2_init(person: Person):
    return True

def nora_university_contracts_story_2_finish(person: Person):
    return True

def nora_university_contracts_story_2_cheat_to(person: Person):
    mc.create_event("nora_obedience_dean_first_meeting_label", "Appointment with University Dean", day_restriction = (0, 1, 2, 3, 4), time_restriction = 1, person = person)
    nora.event_triggers_dict["dean_deal_proposed"] = False
    nora.event_triggers_dict["dean_contract_count"] = 0
    nora.event_triggers_dict["may_have_toys"] = False
    return

def nora_university_contracts_story_2_cheat_past(person: Person):
    nora.obedience = 160
    nora.event_triggers_dict["nora_contract_count"] = 6
    nora.event_triggers_dict["dean_deal_proposed"] = True
    nora.event_triggers_dict["dean_contract_count"] = 0
    return

def nora_university_contracts_story_2_remove(person: Person):
    mc.schedule.cancel_event(event_desc = "Appointment with University Dean")
    mc.business.remove_mandatory_crisis("nora_obedience_dean_first_meeting_label")
    return

def nora_university_contracts_story_2_progress(person: Person, complete: bool):
    if complete:
        return "You refused the Dean's counteroffer."
    return_string = ""
    if nora.event_triggers_dict.get("dean_deal_proposed", False):
        return_string = "The Dean has made a counter offer for your serum contracts.\n"
        return_string += "Complete at least six contracts and raise [person.name]'s obedience above 160 to reject his offer."
    else:
        return_string = "Meet with the Dean when you can."
    return return_string

nora_university_contracts_story_2_step = Story_Step(nora_university_contracts_story_2_init, nora_university_contracts_story_2_finish,
                                          nora_university_contracts_story_2_cheat_to, nora_university_contracts_story_2_cheat_past,
                                          nora_university_contracts_story_2_remove, nora_university_contracts_story_2_progress)

# Step 3
# Intro we meet with Nora and the dean.
# Actions:
# None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_university_contracts_story_3_init(person: Person):
    return True

def nora_university_contracts_story_3_finish(person: Person):
    return True

def nora_university_contracts_story_3_cheat_to(person: Person):
    mc.create_event("nora_obedience_dean_final_submission_label", f"Appointment with {nora.fname}", day_restriction = (0, 1, 2, 3, 4), time_restriction = 3, person = person)
    return

def nora_university_contracts_story_3_cheat_past(person: Person):
    pass
    return

def nora_university_contracts_story_3_remove(person: Person):
    mc.schedule.cancel_event(event_desc = "Appointment with Nora")
    mc.business.remove_mandatory_crisis("nora_obedience_dean_final_submission_label")
    return

def nora_university_contracts_story_3_progress(person: Person, complete: bool):
    if complete:
        return "[nora.title] has taken over the University Dean's council vote."
    return "Meet with [nora.title] at her office."


nora_university_contracts_story_3_step = Story_Step(nora_university_contracts_story_3_init, nora_university_contracts_story_3_finish,
                                          nora_university_contracts_story_3_cheat_to, nora_university_contracts_story_3_cheat_past,
                                          nora_university_contracts_story_3_remove, nora_university_contracts_story_3_progress)


# Step 4
# Epiloge. We let Nora have toys... or not...
# Actions:
# None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_university_contracts_story_4_init(person: Person):
    return True

def nora_university_contracts_story_4_finish(person: Person):
    return True

def nora_university_contracts_story_4_cheat_to(person: Person):
    nora.event_triggers_dict["nora_contracts_intro_complete"] = True
    nora.event_triggers_dict["nora_contract_count"] = 8
    nora.event_triggers_dict["dean_deal_proposed"] = True
    nora.event_triggers_dict["dean_contract_count"] = 0
    nora.event_triggers_dict["may_have_toys"] = True
    return

def nora_university_contracts_story_4_cheat_past(person: Person):
    pass
    return

def nora_university_contracts_story_4_remove(person: Person):
    pass
    return

def nora_university_contracts_story_4_progress(person: Person, complete: bool):
    if nora.event_triggers_dict.get("may_have_toys", False):
        return "You allowed [nora.title] to have toys of her own."
    return "You forbid [nora.title] from messing around with other men."

nora_university_contracts_story_4_step = Story_Step(
    nora_university_contracts_story_4_init,
    nora_university_contracts_story_4_finish,
    nora_university_contracts_story_4_cheat_to,
    nora_university_contracts_story_4_cheat_past,
    nora_university_contracts_story_4_remove,
    nora_university_contracts_story_4_progress)

def nora_university_contracts_path_req():
    return nora.event_triggers_dict.get("nora_contracts_intro_complete", False)

nora_story_path_university_contracts = Story_Path("University Contracts",
    [
        nora_university_contracts_story_0_step,
        nora_university_contracts_story_1_step,
        nora_university_contracts_story_2_step,
        nora_university_contracts_story_3_step,
        nora_university_contracts_story_4_step
    ],
    False,
    nora_university_contracts_path_req,
    "Attend Saturday night meetings with Nora until you have unlocked University serum contracts.")
