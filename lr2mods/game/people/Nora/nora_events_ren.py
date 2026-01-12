from game.major_game_classes.character_related.Person_ren import Person, mc, nora, stephanie
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import downtown_bar
from game.sex_positions._position_definitions_ren import blowjob

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 12
day = 0
time_of_day = 0
"""renpy
init 5 python:
"""

###################
#   Love Events   #
###################

###################
#   Lust Events   #
###################
def nora_initial_closing_visit_requirement():
    return time_of_day == 3 and nora.sluttiness >= 20 and mc.business.is_open_for_business and nora.story_event_ready("slut")

def add_nora_initial_closing_visit_action():
    mc.new_repeat_event(f"Drinks with {nora.fname}+", 5, 4)
    mc.business.add_mandatory_crisis(
        Action("Nora Demands Attention", nora_initial_closing_visit_requirement, "nora_initial_closing_visit_label")
    )
    nora.story_event_log("slut")
    return

def nora_house_call_intro_requirement():
    return time_of_day == 4 and nora.sluttiness >= 40 and nora.story_event_ready("slut")

def add_nora_house_call_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Nora House Call", nora_house_call_intro_requirement, "nora_house_call_intro_label")
    )
    nora.story_event_log("slut")

def nora_university_booty_call_requirement():
    return time_of_day == 1 and mc.business.is_open_for_business and nora.sluttiness >= 60 and nora.story_event_ready("slut")

def add_nora_university_booty_call_action():
    mc.business.add_mandatory_crisis(
        Action("University Booty Call", nora_university_booty_call_requirement, "nora_university_booty_call_label")
    )
    nora.story_event_log("slut")

def nora_house_call_followsup_requirement():
    return False

def add_nora_house_call_followsup_action():
    mc.business.add_mandatory_crisis(
        Action("Nora is Needy", nora_house_call_followsup_requirement, "nora_house_call_followsup_label")
    )
    return

###################
# Obedience Events#
###################

###################
#   Other Events  #
###################

def nora_bar_meetup_initial_meeting_requirement():
    return time_of_day == 4 and day % 7 == 5

def add_nora_bar_meetup_initial_meeting_action():
    mc.create_event("nora_bar_meetup_initial_meeting_label", f"Meet with {nora.name}", day_restriction = 5, time_restriction = 4, person = nora)
    # mc.business.add_mandatory_crisis(
    #     Action("First bar meeting", nora_bar_meetup_initial_meeting_requirement, "nora_bar_meetup_initial_meeting_label")
    # )
    return

def nora_bar_meetup_intro_requirement(person: Person):
    return time_of_day == 4 and day % 7 == 5 and person.location == downtown_bar and person.has_event_delay("nora_bar_meetup_intro_label", 2)

def add_nora_bar_meetup_intro_action():
    nora.add_unique_on_room_enter_event(
        Action("Weekly bar meetup", nora_bar_meetup_intro_requirement, "nora_bar_meetup_intro_label")
    )

def nora_unstable_serum_dialogue_check():
    if nora.event_triggers_dict.get("unstable_serum_stage", 0) < 4:
        if mc.business.research_tier >= 1:
            return True
    if nora.event_triggers_dict.get("unstable_serum_stage", 0) == 4:
        return False
    return False

def nora_teamup_request_check():
    if mc.inventory.has_serum_with_hidden_tag("Suggest") and mc.business.research_tier >= 1:
        stage = nora.event_triggers_dict.get("steph_teamup_stage", 0)
        if stage in (0, 2) and nora.progress.lust_step >= 2 and stephanie.is_willing(blowjob):
            return True
    return False

def nora_stephanie_bar_setup_requirement():
    return day % 7 > 1 and mc.business.is_open_for_business and mc.is_at_office

def add_nora_stephanie_bar_setup_action():
    mc.business.add_mandatory_crisis(
        Action("Nora Bar Setup", nora_stephanie_bar_setup_requirement, "nora_stephanie_bar_setup_label")
    )
