from __future__ import annotations
import renpy
from game.sex_positions._position_definitions_ren import blowjob
from game.major_game_classes.game_logic.Room_ren import gym, university
from game.major_game_classes.character_related.Person_ren import Person, mc, erica, lily, nora
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def erica_get_to_know_requirement(person: Person):
    if not person.is_at(gym):
        return False
    if mc.max_energy < 110:
        return "Requires: 110 maximum energy"
    return mc.is_at(gym)

def erica_phase_one_requirement(person: Person):
    if erica_get_progress() < 1 or not erica_workout_is_unlocked() or not erica_protein_shake_is_unlocked():
        return False
    if time_of_day >= 4 or not person.is_at(gym):
        return False
    if mc.max_energy < 120:
        return "Requires: 120 maximum energy"
    if person.effective_sluttiness() < 40:
        return "Requires 40 Sluttiness"
    return mc.is_at(gym)

def erica_phase_two_requirement(person: Person):
    if erica_get_progress() < 2 or erica_get_progress() > 3:
        return False
    if time_of_day >= 4 or not person.is_at(gym):
        return False
    if mc.max_energy < 140:
        return "Requires: 140 maximum energy"
    if person.effective_sluttiness() < 60:
        return "Requires: 60 sluttiness"
    return True

def erica_buy_protein_shake_requirement(person: Person):
    if not erica_protein_shake_is_unlocked() or not person.is_at(gym):
        return False
    if erica.get_event_day("protein_day") == day:
        return "Once per Day"
    return True

def erica_house_call_requirement(person: Person):
    return erica_get_progress() == 4 and mc.is_at(person.home)

def erica_money_problems_update_requirement(person: Person):
    return time_of_day in (1, 2, 3) and erica_is_looking_for_work()

def erica_discuss_morning_wakeup_requirement(person: Person):
    return time_of_day in (1, 2, 3) and erica_has_given_morning_handjob()

def get_erica_role_actions():
    erica_get_to_know = Action("Get to know her {image=time_advance}", erica_get_to_know_requirement, "erica_get_to_know_label",
        menu_tooltip = "Make an observation about her.")
    erica_phase_one = Action("Workout Together {image=time_advance}", erica_phase_one_requirement, "erica_phase_one_label",
        menu_tooltip = "Work up a sweat.")
    erica_phase_two = Action("Challenge to Race {image=time_advance}", erica_phase_two_requirement, "erica_phase_two_label",
        menu_tooltip = "No risk, no reward.")
    erica_protein_shake = Action("Buy Protein Shake\n{menu_red}Costs: $5{/menu_red}", erica_buy_protein_shake_requirement, "erica_buy_protein_shake_label", menu_tooltip = "Slip some serum in.")
    erica_house_call = Action("Take Charge {image=time_advance}", erica_house_call_requirement, "erica_house_call_label",
        menu_tooltip = "Pick her up.")
    erica_money_problems_update = Action("Ask about finances", erica_money_problems_update_requirement, "erica_money_problems_update_label",
        menu_tooltip = "See if Erica has found work.")
    erica_discuss_morning_wakeup = Action("Discuss wakeup plans", erica_discuss_morning_wakeup_requirement, "erica_discuss_morning_wakeup_label",
        menu_tooltip = "Talk to Erica about whether she should wake you up in the morning after spending the night with Lily.")

    return [erica_get_to_know, erica_phase_one, erica_phase_two, erica_protein_shake, erica_house_call, erica_money_problems_update, erica_discuss_morning_wakeup]

def erica_intro_requirement(person: Person):
    return person.is_at(gym)

def initialise_erica_roaming():
    erica_role = Role(role_name ="College Athlete", actions = get_erica_role_actions(), hidden = True)

    college_athlete_job = JobDefinition("College Athlete", [erica_role], job_location = gym, day_slots = [0, 2, 4], time_slots = [1, 3])
    college_athlete_job.set_schedule(gym, day_slots = [1, 3], time_slots = [3])
    college_athlete_job.set_schedule(gym, day_slots = [5, 6], time_slots = [1, 2])
    erica.set_side_job(college_athlete_job, False)

    # unlock erica (free-roam)
    erica.set_override_schedule(None)
    erica.add_unique_on_room_enter_event(
        Action("Meet Erica", erica_intro_requirement, "erica_intro_label", priority = 30)
    )

def erica_race_crisis_requirement():
    return day % 7 == 5 and time_of_day == 1

def add_erica_race_crisis(person: Person):
    mc.business.add_mandatory_crisis(
        Action("Charity Race", erica_race_crisis_requirement, "erica_race_crisis_label", args = [person])
    )


def second_wind_func():
    mc.change_energy(mc.max_energy / 2)

def erica_get_wakeup_options():
    return erica.event_triggers_dict.get("wake_up_options", ["handjob"])

def add_erica_wakeup_option(option):
    if "wake_up_options" not in erica.event_triggers_dict:
        erica.event_triggers_dict["wake_up_options"] = erica_get_wakeup_options()
    if option not in erica_get_wakeup_options():
        erica.event_triggers_dict["wake_up_options"].append(option)

def erica_wakeup_choose_position():
    tuple_list = []
    for position in erica_get_wakeup_options():
        tuple_list.append((position.title(), position))
    tuple_list.append(("Surprise me", "Surprise me"))

    return renpy.display_menu(tuple_list, True, "Choice")

def erica_get_morning_wakeup_pref():
    return erica.event_triggers_dict.get("morning_wakeup_pref", 0)

def erica_pre_insta_blowjob_complete():
    return erica.event_triggers_dict.get("pre_insta_blowjob", False)


def erica_watch_race_intro_requirement(person: Person):
    return False

def erica_watch_race_requirement():
    return day % 7 == 5 and time_of_day == 1

def erica_breeding_fetish_followup_requirement(person: Person):
    return (
        person.is_pregnant
        and person.is_at(gym)
        and day > person.get_event_day("preg_tits_date") + 3
    )

def erica_breeding_fetish_team_crisis_requirement():
    return (
        day % 7 != 5
        and time_of_day == 4
        and erica.is_pregnant
        and day >= erica.pregnancy_show_day + 7
    )

def add_erica_breeding_fetish_team_crisis_action():
    mc.business.add_mandatory_crisis(
        Action("Erica gets kicked off the track team", erica_breeding_fetish_team_crisis_requirement, "erica_breeding_fetish_team_crisis_label")
    )

def erica_breeding_fetish_nora_followup_requirement(person: Person):
    return person.is_at(university)

def add_erica_breeding_fetish_nora_followup_action():
    nora.add_unique_on_talk_event(
        Action("Talk to Nora about Erica", erica_breeding_fetish_nora_followup_requirement, "erica_breeding_fetish_nora_followup_label", priority = 30)
    )
    erica.event_triggers_dict["kicked_off_team"] = True

def erica_breeding_nora_news_part_one_requirement(min_day: int):
    return (time_of_day == 2 and day > min_day)

def add_erica_breeding_nora_news_part_one_action():
    mc.business.add_mandatory_crisis(
        Action("Nora follow up text", erica_breeding_nora_news_part_one_requirement, "erica_breeding_nora_news_part_one_label", requirement_args = day + 6)
    )

def erica_breeding_nora_news_part_two_requirement(min_day: int):
    return (time_of_day == 2 and day > min_day)

def add_erica_breeding_nora_news_part_two_action():
    mc.business.add_mandatory_crisis(
        Action("Nora good news", erica_breeding_nora_news_part_two_requirement, "erica_breeding_nora_news_part_two_label", requirement_args = day + 6)
    )

def erica_breeding_fetish_team_rejoin_requirement(person: Person):
    return True

def add_erica_breeding_fetish_team_rejoin_action():
    erica.set_event_day("team_reinstate_day")
    erica.add_unique_on_talk_event(
        Action("Erica gets good news", erica_breeding_fetish_team_rejoin_requirement, "erica_breeding_fetish_team_rejoin_label", priority = 30)
    )

def erica_pre_insta_love_requirement(person: Person):
    return (
        time_of_day == 4
        and day % 7 == 5
        and person.love > 40
        and person.is_at(lily.home)
        and person.is_willing(blowjob)
    )

def erica_get_is_yoga_nude():
    return erica.event_triggers_dict.get("nude_yoga", False)

def erica_post_yoga_fuck_complete():
    return erica.event_triggers_dict.get("post_yoga_fuck", False)

def erica_on_love_path():
    return erica.event_triggers_dict.get("love_path", False)

def erica_on_fwb_path():
    return erica.event_triggers_dict.get("fwb_path", False)

def erica_on_hate_path():
    return erica.event_triggers_dict.get("hate_path", False)

def erica_protein_shake_is_unlocked():
    return erica.event_triggers_dict.get("erica_protein", 0) != 0

def erica_workout_is_unlocked():
    return erica.event_triggers_dict.get("erica_workout", 0) != 0

def erica_get_is_doing_insta_sessions():
    return erica.event_triggers_dict.get("insta_pic_intro_complete", False)

def erica_is_looking_for_work():
    return erica.event_triggers_dict.get("looking_for_work", False)

def erica_has_given_morning_handjob():
    return erica.event_triggers_dict.get("post_insta_handy", False)

def erica_get_progress():
    return erica.event_triggers_dict.get("erica_progress", 0)

def erica_fetish_is_kicked_off_team():
    return erica.event_triggers_dict.get("kicked_off_team", False)

def erica_fetish_rejoin_team():
    return erica.event_triggers_dict.get("rejoin_team", False)


def erica_get_is_doing_yoga_sessions():
    return erica.event_triggers_dict.get("yoga_sessions_started", False)


def erica_get_yoga_class_list():
    yoga_list = []
    for person in [x for x in mc.business.employees_availabe if x.opinion.yoga > 0 and x != mc.business.hr_director]:
        yoga_list.append(person)
    return yoga_list
