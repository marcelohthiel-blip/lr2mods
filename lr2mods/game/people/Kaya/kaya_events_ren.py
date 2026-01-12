from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.map.MapHub_ren import university_hub
from game.major_game_classes.character_related.Person_ren import Person, mc, kaya, nora
from game.major_game_classes.character_related.Schedule_ren import Schedule

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


### Love Events ###

def kaya_first_date_requirement(person: Person):
    return (time_of_day == 3
        and person.is_at_job("Barista")
        and person.days_since_event("drink_reject_day") >= 2)

def add_kaya_first_date_action():
    kaya.add_unique_on_room_enter_event(
        Action("Kaya First Date", kaya_first_date_requirement, "kaya_first_date_label", priority = 30)
    )
    kaya.set_event_day("drink_reject_day")

def kaya_ask_nora_for_sponsorship_requirement(person: Person):
    return (person.is_at(university_hub))

def add_kaya_ask_nora_for_sponsorship_action():
    nora.add_unique_on_room_enter_event(
        Action("Nora Sponsor Kaya Intro Event", kaya_ask_nora_for_sponsorship_requirement, "kaya_ask_nora_for_sponsorship_label", priority = 30)
    )

def kaya_nora_sponsorship_requirement(person: Person):
    return person.is_at_job("Barista")

def add_kaya_nora_sponsorship_action():
    kaya.add_unique_on_room_enter_event(
        Action("Kaya Gets Sponsored", kaya_nora_sponsorship_requirement, "kaya_nora_sponsorship_label", priority = 30)
    )

def kaya_first_day_of_class_requirement():
    return day % 7 == 1 and time_of_day == 3

def add_kaya_first_day_of_class_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya Back to Class Event", kaya_first_day_of_class_requirement, "kaya_first_day_of_class_label")
    )

def kaya_needs_residency_requirement(person: Person):
    return (
        person.story_event_ready("love")
        and person.love >= 40
        and person.is_at_job("Barista")
        and time_of_day in [2, 3]
    )

def add_kaya_needs_residency_action():
    kaya.add_unique_on_room_enter_event(
        Action("Kaya Needs Work Program Intro", kaya_needs_residency_requirement, "kaya_needs_residency_label", priority = 30)
    )
    kaya.story_event_log("love")

def kaya_nora_residency_requirement(person: Person, start_day: int):
    return (
        day >= start_day
        and person.is_at(university_hub)
    )

def add_kaya_nora_residency_action():
    nora.add_unique_on_room_enter_event(
        Action("Nora Kaya Request Event", kaya_nora_residency_requirement, "kaya_nora_residency_label", requirement_args = Schedule.next_monday(), priority = 30)
    )

def kaya_residency_first_day_requirement(start_day: int):
    return (
        day > start_day
        and day % 7 == 0
        and time_of_day == 1
    )

def add_kaya_residency_first_day_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya's First Day At RnD", kaya_residency_first_day_requirement, "kaya_residency_first_day_label", requirement_args = day)
    )

def kaya_first_research_day_requirement():
    return time_of_day == 3

def add_kaya_first_research_day_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya's First Day At RnD Ended", kaya_first_research_day_requirement, "kaya_first_research_day_label")
    )

def kaya_working_late_requirement():
    if kaya.event_triggers_dict.get("no_condom_talk_day", 99999) + 2 > day:
        return False
    return (time_of_day == 3
        and kaya.love >= 60
        and kaya.story_event_ready("love")
        and kaya.is_at_office
        and mc.is_at_office)

def add_kaya_working_late_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya Working Late Event", kaya_working_late_requirement, "kaya_working_late_label")
    )
    kaya.story_event_log("love")

def kaya_sakari_cure_intro_requirement():
    return False

def add_kaya_sakari_cure_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya Wants to Find the Cure", kaya_sakari_cure_intro_requirement, "kaya_sakari_cure_intro_label")
    )
    kaya.story_event_log("love")

### Lust Events ###
def kaya_study_struggle_requirement(person: Person):
    return (person.sluttiness >= 20
        and person.story_event_ready("slut")
        and person.is_at(university_hub))

def add_kaya_study_struggle_action():
    kaya.add_unique_on_room_enter_event(
        Action("Kaya can't study", kaya_study_struggle_requirement, "kaya_study_struggle_label", priority = 30)
    )
    kaya.story_event_log("slut")

def kaya_birthday_night_out_requirement():
    return (day % 7 in [5, 6]
        and time_of_day == 3
        and kaya.sluttiness >= 40
        and kaya.story_event_ready("slut"))

def add_kaya_birthday_night_out_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya turns 21", kaya_birthday_night_out_requirement, "kaya_birthday_night_out_label")
    )
    kaya.story_event_log("slut")

def kaya_booty_call_requirement():
    if kaya.event_triggers_dict.get("no_condom_talk_day", 99999) + 2 > day: #It has been at least a couple days since the talk.
        return False
    return (day % 7 in [0, 1, 2, 3, 4]
        and time_of_day == 4
        and kaya.sluttiness >= 60
        and kaya.story_event_ready("slut"))

def add_kaya_booty_call_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya makes a booty call", kaya_booty_call_requirement, "kaya_booty_call_label")
    )
    kaya.story_event_log("slut")

def kaya_booty_call_followup_requirement():
    return time_of_day == 3

def add_kaya_booty_call_followup_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya makes a booty call follow-up", kaya_booty_call_followup_requirement, "kaya_booty_call_followup_label")
    )

def kaya_study_struggle_redux_requirement(person: Person):
    return (kaya.sluttiness >= 60
        and kaya.story_event_ready("love")
        and kaya.is_at_office)

def add_kaya_study_struggle_redux_action():
    kaya.add_unique_on_room_enter_event(
        Action("Kaya can't focus at work", kaya_study_struggle_redux_requirement, "kaya_study_struggle_redux_label", priority = 30)
    )
    kaya.story_event_log("slut")

### Obedience Events ###
def kaya_nora_research_pilfer_intro_requirement():
    return False    # disabled for now
    return (day % 7 == 2
        and kaya.obedience > 120
        and kaya.story_event_ready("obedience")
        and kaya.is_at_office)

def add_kaya_nora_research_pilfer_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya notices something", kaya_nora_research_pilfer_intro_requirement, "kaya_nora_research_pilfer_intro_label")
    )
    kaya.story_event_log("obedience")

### Pregnancy Events ###

### Other Events ###
