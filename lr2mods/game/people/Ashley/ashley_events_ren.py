from __future__ import annotations
from game.sex_positions._position_definitions_ren import blowjob, against_wall
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, ashley, lily, stephanie
from game.major_game_classes.game_logic.Action_ren import Action
from game.people.Ashley.ashley_role_definition_ren import ashley_get_mc_obedience, ashley_submission_role

TIER_1_TIME_DELAY = 3
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

#### Love Events ####

def ashley_after_hours_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.love > 20
        and ashley.story_event_ready("love")
        and mc.is_at_office
    )

def add_ashley_afterhours_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley approach you", ashley_after_hours_requirement, "ashley_after_hours_label", priority = 10)
    )
    ashley.story_event_log("love")

def ashley_asks_about_lily_requirement(min_day: int):
    return (
        day > min_day
        and mc.business.is_open_for_business
        and mc.is_at_office
    )

def add_ashley_asks_about_lily_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley asks about Lily", ashley_asks_about_lily_requirement, "ashley_asks_about_lily_label", requirement_args = day + 3)
    )
    ashley.progress.love_step = 2

def ashley_lily_hangout_requirement():
    return time_of_day == 4

def add_ashley_lily_hangout_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley and Lily makeup", ashley_lily_hangout_requirement, "ashley_lily_hangout_label")
    )

def ashley_lily_shopping_selfies_requirement():
    return False
    return (
        time_of_day != 0
        and day % 7 == 5 #Saturday
        and ashley.love >= 60
        and ashley.story_event_ready("love")
    )

def add_ashley_lily_shopping_selfies_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley sends you pics", ashley_lily_shopping_selfies_requirement, "ashley_lily_shopping_selfies_label")
    )
    town_relationships.update_relationship(lily, ashley, "Friend")
    ashley.progress.love_step = 3
    ashley.story_event_log("love")

def ashley_lily_shopping_aftermath_requirement():
    return time_of_day == 4

def add_ashley_lily_shopping_aftermath_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley sneaks into your room", ashley_lily_shopping_aftermath_requirement, "ashley_lily_shopping_aftermath_label")
    )

def ashley_lily_truth_or_dare_requirement():
    return (
        time_of_day == 4
        and day % 7 not in (5, 6) #not weekend
        and ashley.love >= 80
        and ashley.story_event_ready("love")
    )

def add_ashley_lily_truth_or_dare_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley and Lily Truth or Dare", ashley_lily_truth_or_dare_requirement, "ashley_lily_truth_or_dare_label")
    )
    ashley.story_event_log("love")

def ashley_steph_harem_entry_requirement():
    return False

def add_ashley_steph_harem_entry_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley and Steph join your harem", ashley_steph_harem_entry_requirement, "ashley_steph_harem_entry_label")
    )
    town_relationships.update_relationship(lily, ashley, "Best Friend")
    ashley.story_event_log("love")

##### Lust Events #####

def ashley_porn_video_discover_requirement():
    return mc.is_in_bed and ashley.sluttiness >= 20 and ashley.story_event_ready("slut")

def add_ashley_porn_video_discover_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley emails you", ashley_porn_video_discover_requirement, "ashley_porn_video_discover_label")
    )
    ashley.story_event_log("slut")

def ashley_ask_sister_about_porn_video_requirement(person: Person):
    return person.is_at_work and person.is_available

def add_ashley_ask_sister_about_porn_video_action():
    stephanie.add_unique_on_talk_event(
        Action("Ask Steph about porn video", ashley_ask_sister_about_porn_video_requirement, "ashley_ask_sister_about_porn_video_label", priority = 30)
    )
    ashley.event_triggers_dict["porn_discovered"] = True

def ashley_ask_about_porn_requirement(person: Person):
    return time_of_day < 3 and person.is_at_office

def add_ashley_ask_about_porn_action():
    ashley.add_unique_on_room_enter_event(
        Action("Ask Ashley about porn", ashley_ask_about_porn_requirement, "ashley_ask_about_porn_label", priority = 30)
    )
    ashley.event_triggers_dict["porn_discussed"] = True
    ashley.story_event_log("slut")

def ashley_post_handjob_convo_requirement(person: Person):
    return person.is_at_work and person.is_available

def add_ashley_post_handjob_convo_action():
    ashley.add_unique_on_talk_event(
        Action("Confront Ashley", ashley_post_handjob_convo_requirement, "ashley_post_handjob_convo_label", priority = 30)
    )
    ashley.event_triggers_dict["porn_convo_avail"] = True
    ashley.progress.lust_step = 1

def ashley_stephanie_arrange_relationship_requirement(person: Person):
    return person.is_at_work

def add_ashley_stephanie_arrange_relationship_action():
    stephanie.add_unique_on_talk_event(
        Action("Arrange things with Stephanie", ashley_stephanie_arrange_relationship_requirement, "ashley_stephanie_arrange_relationship_label", priority = 30)
    )

def ashley_blows_during_meeting_requirement():
    return (
        mc.business.is_open_for_business
        and ashley.sluttiness >= 40
        and ashley.story_event_ready("slut")
        and mc.is_at_office
        and ashley.is_willing(blowjob)
    )

def add_ashley_blows_during_meeting_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley blows you", ashley_blows_during_meeting_requirement, "ashley_blows_during_meeting_label")
    )
    ashley.story_event_log("slut")

def ashley_supply_closet_at_work_requirement():
    return False # not yet written
    return (
        mc.business.is_open_for_business
        and ashley.sluttiness >= 60
        and ashley.story_event_ready("slut")
        and mc.is_at_office
        and ashley.is_willing(against_wall)
    )

def add_ashley_supply_closet_at_work_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley is needy", ashley_supply_closet_at_work_requirement, "ashley_supply_closet_at_work_label")
    )
    ashley.progress.lust_step = 2
    ashley.story_event_log("slut")

def ashley_asks_for_anal_requirement():
    return (
        mc.business.is_open_for_business
        and ashley.sluttiness >= 80
        and ashley.story_event_ready("slut")
        and mc.is_at_office
    )

def add_ashley_asks_for_anal_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley one ups her sister", ashley_asks_for_anal_requirement, "ashley_asks_for_anal_label")
    )
    ashley.story_event_log("slut")

def ashley_tests_serum_on_sister_requirement():
    return False

def add_ashley_tests_serum_on_sister_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley gives you a present", ashley_tests_serum_on_sister_requirement, "ashley_tests_serum_on_sister_label")
    )
    ashley.story_event_log("slut")


#### Obedience Events ####


def ashley_demands_relief_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley_get_mc_obedience() > 30
        and ashley.story_event_ready("obedience")
        and mc.is_at_office
    )

def add_ashley_demands_relief_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley needs relief", ashley_demands_relief_requirement, "ashley_demands_relief_label", priority = 10)
    )
    ashley.story_event_log("obedience")

def ashley_demands_oral_requirement():
    return False    #Current writing place
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.story_event_ready("obedience")
        and ashley_get_mc_obedience() > 60
        and mc.is_at_office
    )

def add_ashley_demands_oral_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley needs oral relief", ashley_demands_oral_requirement, "ashley_demands_oral_label", priority = 10)
    )
    ashley.story_event_log("obedience")
    ashley.event_triggers_dict["dom_fingers"] = True

def ashley_arousal_serum_start_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.story_event_ready("obedience")
        and ashley_get_mc_obedience() > 100
        and mc.is_at_office
    )

def add_ashley_arousal_serum_start_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley takes arousal drug", ashley_arousal_serum_start_requirement, "ashley_arousal_serum_start_label", priority = 10)
    )
    ashley.story_event_log("obedience")
    ashley.event_triggers_dict["dom_oral"] = True

def ashley_demands_sub_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.story_event_ready("obedience")
        and ashley_get_mc_obedience() > 150
        and mc.is_at_office
    )

def add_ashley_demands_sub_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley takes charge", ashley_demands_sub_requirement, "ashley_demands_sub_label", priority = 10)
    )
    ashley.story_event_log("obedience")

def ashley_submission_titfuck_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.obedience > 120
        and ashley.story_event_ready("obedience")
        and mc.is_at_office
    )

def add_ashley_submission_titfuck_action():
    mc.business.add_mandatory_crisis(
        Action("Fuck ashley's tits", ashley_submission_titfuck_requirement, "ashley_submission_titfuck_label", priority = 10)
    )
    ashley.story_event_log("obedience")

def ashley_submission_taboo_restore_requirement(min_day: int):    #For all the taboo restoration events.
    return (
        time_of_day == 1
        and day > min_day
        and mc.is_at_office
        and mc.business.is_open_for_business
    )

def add_ashley_submission_titfuck_taboo_restore_action():
    mc.create_event("ashley_submission_titfuck_taboo_restore_label", f"Conversation with {ashley.fname}", day_restriction = (0, 1, 2, 3, 4), time_restriction = (1, 2, 3), person = ashley)
    # mc.business.add_mandatory_crisis(
    #     Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_titfuck_taboo_restore_label", requirement_args = day)
    # )
    # ashley.add_role(ashley_submission_role)
    ashley.change_obedience(-20)
    ashley.story_event_log("obedience")

def ashley_submission_blowjob_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.obedience > 150
        and ashley.story_event_ready("obedience")
        and mc.is_at_office
    )

def add_ashley_submission_blowjob_action():
    mc.business.add_mandatory_crisis(
        Action("Fuck ashley's mouth", ashley_submission_blowjob_requirement, "ashley_submission_blowjob_label", priority = 10)
    )
    ashley.event_triggers_dict["sub_titfuck_avail"] = True
    ashley.remove_role(ashley_submission_role)
    ashley.progress.obedience_step = 1
    ashley.story_event_log("obedience")

def add_ashley_submission_blowjob_taboo_restore_action():
    mc.create_event("ashley_submission_blowjob_taboo_restore_label", f"Conversation with {ashley.fname}", (0, 1, 2, 3, 4), (1, 2, 3), person = ashley)
    # mc.business.add_mandatory_crisis(
    #     Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_blowjob_taboo_restore_label", requirement_args = day)
    # )
    # ashley.add_role(ashley_submission_role)
    ashley.change_obedience(-20)
    ashley.story_event_log("obedience")

def ashley_submission_fuck_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley.obedience > 180
        and ashley.story_event_ready("obedience")
        and mc.is_at_office
    )

def add_ashley_submission_fuck_action():
    mc.business.add_mandatory_crisis(
        Action("Fuck Ashley over your desk", ashley_submission_fuck_requirement, "ashley_submission_fuck_label", priority = 10)
    )
    ashley.event_triggers_dict["sub_blowjob_avail"] = True
    ashley.remove_role(ashley_submission_role)
    ashley.progress.obedience_step = 2
    ashley.story_event_log("obedience")

def add_ashley_submission_fuck_taboo_restore_action():
    mc.business.add_mandatory_crisis(
        Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_fuck_taboo_restore_label", requirement_args = day)
    )
    ashley.add_role(ashley_submission_role)
    ashley.change_obedience(-20)
    ashley.story_event_log("obedience")

def ashley_submission_anal_requirement():
    return False    #Current writing spot is submission fuck

    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and ashley_get_mc_obedience() > 220
        and ashley.story_event_ready("obedience")
        and mc.is_at_office
    )

def add_ashley_submission_anal_action():
    mc.business.add_mandatory_crisis(
        Action("Fuck ashley's ass", ashley_submission_anal_requirement, "ashley_submission_anal_label", priority = 10)
    )
    ashley.event_triggers_dict["sub_fuck_avail"] = True
    ashley.remove_role(ashley_submission_role)
    ashley.progress.obedience_step = 2
    ashley.story_event_log("obedience")

def add_ashley_submission_anal_taboo_restore_action():
    mc.business.add_mandatory_crisis(
        Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_anal_taboo_restore_label", requirement_args = day)
    )
    ashley.add_role(ashley_submission_role)
    ashley.change_obedience(-20)
    ashley.story_event_log("obedience")

def ashley_final_submission_requirement():
    return False

def add_ashley_final_submission_action():
    mc.business.add_mandatory_crisis(
        Action("Ashley's serum plot", ashley_final_submission_requirement, "ashley_final_submission_label")
    )
    ashley.story_event_log("obedience")
    ashley.event_triggers_dict["dom_fuck"] = True
    ashley.story_event_log("obedience")
