from __future__ import annotations
import copy
import renpy
from game.helper_functions.random_generation_functions_ren import create_random_person
from game.game_roles._role_definitions_ren import instapic_role, onlyfans_role
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import kitchen, lily_bedroom, mom_bedroom, bedroom, hall
from game.major_game_classes.character_related._job_definitions_ren import secretary_job
from game.major_game_classes.character_related.Person_ren import Person, mc, mom, lily, aunt, cousin
from game.major_game_classes.clothing_related.Wardrobe_ren import Outfit, mom_business_wardrobe
from game.map.map_code_ren import mom_office_is_open
from game.people.Jennifer.jennifer_definition_ren import mom_associate_job, mom_secretary_job
from game.people.Jennifer.jennifer_events_ren import add_mother_anal_curiosity_intro_action

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def mom_kissing_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def mom_oral_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def mom_anal_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def mom_vaginal_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def mom_on_day(person: Person):
    # Set up taboo break revisits if taboos have been broken.
    if person.has_broken_taboo(["touching_body", "kissing", "bare_pussy", "bare_tits", "touching_vagina"]) and not person.event_triggers_dict.get("kissing_revisit_complete", False): #Checks if they have all of these taboos or not.
        if person.is_girlfriend:
            person.event_triggers_dict["kissing_revisit_complete"] = True
        else:
            broken_taboos = person.event_triggers_dict.get("kissing_revisit_restore_taboos", []) #Note: this will result in duplicates sometimes.
            if person.has_broken_taboo("bare_tits"):
                broken_taboos.append("bare_tits")
            if person.has_broken_taboo("bare_pussy"):
                broken_taboos.append("bare_pussy")
            if person.has_broken_taboo("kissing"):
                broken_taboos.append("kissing")
            if person.has_broken_taboo("touching_body"):
                broken_taboos.append("touching_body")
            if person.has_broken_taboo("touching_vagina"):
                broken_taboos.append("touching_vagina")

            taboo_revisit_event = Action("mom kissing taboo revisit", mom_kissing_taboo_revisit_requirement, "mom_kissing_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                person.add_unique_on_room_enter_event(taboo_revisit_event)
                for a_taboo in broken_taboos:
                    person.restore_taboo(a_taboo, add_to_log = False)
            person.event_triggers_dict["kissing_revisit_restore_taboos"] = broken_taboos

    if person.has_broken_taboo(["sucking_cock", "licking_pussy"]) and not person.event_triggers_dict.get("oral_revisit_complete", False):
        if person.is_girlfriend:
            person.event_triggers_dict["oral_revisit_complete"] = True
        else:
            broken_taboos = person.event_triggers_dict.get("oral_revisit_restore_taboos", [])
            if person.has_broken_taboo("sucking_cock"):
                broken_taboos.append("sucking_cock")
            if person.has_broken_taboo("licking_pussy"):
                broken_taboos.append("licking_pussy")
            taboo_revisit_event = Action("mom oral taboo revisit", mom_oral_taboo_revisit_requirement, "mom_oral_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                for a_taboo in broken_taboos:
                    person.restore_taboo(a_taboo, add_to_log = False)
                person.add_unique_on_room_enter_event(taboo_revisit_event)
            person.event_triggers_dict["oral_revisit_restore_taboos"] = broken_taboos

    if person.has_broken_taboo("anal_sex") and not person.event_triggers_dict.get("anal_revisit_complete", False):
        if person.is_girlfriend:
            person.event_triggers_dict["anal_revisit_complete"] = True
        else:
            taboo_revisit_event = Action("mom anal taboo revisit", mom_anal_taboo_revisit_requirement, "mom_anal_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                person.restore_taboo("anal_sex", add_to_log = False)
                person.add_unique_on_room_enter_event(taboo_revisit_event)

    if person.has_broken_taboo("vaginal_sex") and not person.event_triggers_dict.get("vaginal_revisit_complete", False):
        if person.is_girlfriend:
            person.event_triggers_dict["vaginal_revisit_complete"] = True
        else:
            taboo_revisit_event = Action("mom vaginal taboo revisit", mom_vaginal_taboo_revisit_requirement, "mom_vaginal_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                person.restore_taboo("vaginal_sex", add_to_log = False)
                person.add_unique_on_room_enter_event(taboo_revisit_event)

def mom_offer_make_dinner_requirement(person: Person):
    return time_of_day == 3 and person.is_at(kitchen)

def mom_home_change_wardrobe_requirement(person: Person):
    return person.progress.obedience_step >= 3 and person.is_at_mc_house

def mom_test_serum_night_requirement(person: Person):
    return (person.progress.obedience_step >= 2 and time_of_day == 4)

def mom_work_promotion_two_prep_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_work_promotion_two_prep_enabled", False):
        return False #Not visible if not enabled
    if not person.has_job(mom_associate_job):
        return False
    if time_of_day < 3:
        return "Too early to prepare"
    return True

def mom_work_secretary_replacement_bigger_tits_reintro_requirement(person: Person):
    if mc.business.is_weekend or not person.has_job(mom_secretary_job):
        return False
    if not person.event_triggers_dict.get("mom_work_tit_options_reintro", False):
        return False
    if person.event_triggers_dict.get("mom_office_slutty_level", 0) != 1:
        return False
    if person.event_triggers_dict.get("mom_replacement_approach", "seduce") != "tits":
        return False
    if (person.event_triggers_dict.get("mom_replacement_approach_waiting_for_tits", False) and person.rank_tits(person.tits) <= person.rank_tits(person.event_triggers_dict.get("mom_replacement_approach_waiting_for_tits", False))):
        return False
    if Person.rank_tits(person.tits) >= 8:  # they are already big enough
        return False
    if mc.location.person_count > 1:
        return "Not with other people around"
    return True

def sister_girlfriend_ask_blessing_requirement(person: Person): #This is an action that Mom has
    return person.event_triggers_dict.get("sister_girlfriend_ask_blessing", False)

def mom_girlfriend_return_requirement(person: Person):
    if person.event_triggers_dict.get("mom_girlfriend_sister_blessing_given", None) is None:
        return False
    if person.event_triggers_dict.get("mom_girlfriend_waiting_for_blessing", False) and lily.event_triggers_dict.get("mom_girlfriend_ask_blessing", False):
        return "Talk to [lily.title] first."
    return True

def fetish_mom_kitchen_requirement(person: Person):
    if person.fetish_count == 0:
        return False
    if person == mom and mc.is_at(kitchen):
        if mc.energy > 30:
            return True
        return "You're too tired for sex"
    return False

def mom_breakfast_prog_scene_request_req(person):   #Conversation where MC asks for breakfast in bed the next day
    if person.progress.obedience_step < 2 or not person.is_at_mc_house:
        return False
    if day % 7 in (4, 5):
        return "Unavailable on weekends"
    if person.days_since_event("breakfast_in_bed") >= (max(1, 10 - int((person.obedience - 100) / 20))):
        return time_of_day in (3, 4)
    return "Increase obedience to request breakfast in bed more often"

def get_mother_role_actions():
    #MOTHER ACTIONS#
    mom_test_serum_night = Action("Test a Serum {image=time_advance}", mom_test_serum_night_requirement, "mom_test_serum_night_label",
        menu_tooltip = "Test a serum.", priority = 5)

    mother_offer_make_dinner = Action("Offer to make dinner {image=time_advance}", mom_offer_make_dinner_requirement, "mom_offer_make_dinner_label",
        menu_tooltip = "Earn some good will by making dinner for your mother and sister.", priority = 5)

    mom_work_promotion_two_prep_action = Action("Prepare for her interview", mom_work_promotion_two_prep_requirement, "mom_work_promotion_two_prep",
        menu_tooltip = "Help your mom prepare for her one–on–one interview.", priority = 10)

    mom_work_bigger_tits_reintro = Action("Talk about getting bigger tits", mom_work_secretary_replacement_bigger_tits_reintro_requirement, "mom_work_secretary_replacement_bigger_tits_reintro",
        menu_tooltip = "Talk to her about improving her natural assets, either with implants or by using some of your serum.", priority = 10)

    mom_sister_girlfriend_blessing_action = Action("Talk about Lily", sister_girlfriend_ask_blessing_requirement, "sister_girlfriend_mom_blessing",
        menu_tooltip = "Try and convince her to give you and Lily her blessing.", priority = 100)

    mom_girlfriend_return_action = Action("Give her the news", mom_girlfriend_return_requirement, "mom_girlfriend_return",
        menu_tooltip = "Tell her how your conversation with Lily went.", priority = 100)

    fetish_mom_kitchen_action = Action("Kitchen Sex (Fetish) {image=time_advance}", fetish_mom_kitchen_requirement, "fetish_mom_kitchen_label",
        menu_tooltip = "Indulge your mother's fantasies.")

    mom_home_change_wardrobe_action = Action("Change her home wardrobe", mom_home_change_wardrobe_requirement, "mom_home_change_wardrobe_label",
        menu_tooltip = "Modify the wardrobe that [mom.fname] wears around the house.")

    mom_breakfast_prog_scene_request_action = Action("Request Breakfast in Bed", mom_breakfast_prog_scene_request_req, "mom_breakfast_prog_scene_request_label")

    return [mom_test_serum_night, mother_offer_make_dinner, mom_work_promotion_two_prep_action, mom_work_bigger_tits_reintro, mom_sister_girlfriend_blessing_action, mom_girlfriend_return_action, fetish_mom_kitchen_action, mom_home_change_wardrobe_action, mom_breakfast_prog_scene_request_action]

def mom_convince_quit_requirement(person: Person):
    if person.love < 10:
        return False
    if person.love < 20:
        return "Requires: 20 Love" # hide it until you're reasonably close, then show that you need at least 20 to get her to talk about it.
    return True #Are there any requirements for starting this conversation we need to throw in?

def get_mother_associate_actions():
    mom_convince_quit_action = Action("Convince her to quit her job", mom_convince_quit_requirement, "mom_convince_quit_label", priority = -5)
    return [mom_convince_quit_action]

def get_mother_associate_role() -> Role:
    return Role("Business Associate", get_mother_associate_actions(), hidden = True)

def get_mother_secretary_role() -> Role:
    return Role("Personal Associate", get_mother_associate_actions(), hidden = True)

def init_mother_roles():
    global mother_role
    mother_role = Role("Mother", get_mother_role_actions(), on_day = mom_on_day, hidden = True)

def mom_date_intercept_requirement(person: Person, the_date: Person):
    return (
        person.energy > 80
        and person.love > 10
        and person.is_at_mc_house
        and mc.is_home
        and person != the_date
    )

def sister_instapic_discover_requirement(person: Person):
    return (
        mc.is_in_bed
        and not person.event_triggers_dict.get("sister_instathot_mom_enabled", False)
        and person.is_home
        and mc.location.person_count == 0
    )

def add_sister_instapic_discover_crisis():
    mc.business.add_mandatory_crisis(
        Action("sister insta mom reveal",
            sister_instapic_discover_requirement,
            "sister_instathot_mom_discover",
            args = lily, requirement_args = lily)
    )

def mom_instapic_setup_intro_requirement(person: Person, start_day: int):
    return (
        day > start_day
        and not person.has_role(instapic_role)
        and person.is_home
    )

def add_mom_instapic_setup_intro_action():
    if mom.has_role(instapic_role):
        return
    mom.add_unique_on_room_enter_event(
        Action("mom start instapic",
            mom_instapic_setup_intro_requirement,
            "mom_instapic_setup_intro",
            requirement_args = day + renpy.random.randint(3, 5),
            priority = 30)
    )

def mom_instapic_alt_intro_requirement(person: Person, start_day: int):
    if person.event_triggers_dict.get("mom_instapic_help_enabled", False):
        return True #NOTE: When triggered this automatically returns, clearing the event from the internal list.

    if day < start_day or not person.has_role(instapic_role):
        return False
    return person.event_triggers_dict.get("mom_instapic_intro_done", False)

def add_mom_instapic_alt_intro_action():
    mom.add_unique_on_room_enter_event(
        Action("mom alt start instapic",
            mom_instapic_alt_intro_requirement,
            "mom_instapic_alt_intro",
            requirement_args = day + renpy.random.randint(3, 5),
            priority = 30)
    )

def mom_instapic_setup_help_requirement(person: Person):
    if person.has_role(instapic_role) or person.event_triggers_dict.get("mom_instapic_intro_done", False):
        return False
    if time_of_day >= 4:
        return "Not enough time."
    return True

def add_mom_instapic_setup_event():
    mom.add_action(
        Action("Set up her InstaPic account {image=time_advance}",
            mom_instapic_setup_help_requirement,
            "mom_instapic_setup",
            is_fast = False)
    )

def finish_mom_instapic_setup():
    mom.remove_action("mom_instapic_setup")
    mom.learn_instapic()
    mom.event_triggers_dict["mom_instapic_help_enabled"] = True
    mom.remove_on_room_enter_event("mom_instapic_alt_intro")    # remove alt intro
    add_mom_instapic_ban_action()

def mom_instapic_ban_requirement(person: Person, start_day: int):
    return (
        day > start_day
        and person.has_role(instapic_role)
        and person.location.person_count <= 1
    )

def add_mom_instapic_ban_action():
    mom.add_unique_on_room_enter_event(
        Action("Mom InstaPic Ban",
            mom_instapic_ban_requirement,
            "mom_instapic_ban",
            requirement_args = day + renpy.random.randint(3, 5),
            priority = 30)
    )

def mom_onlyfans_help_requirement(person: Person):
    if not person.has_role(onlyfans_role) or not person.is_home:
        return False
    if mom_bedroom.person_count > 1:
        return "Not with people around..."
    if person.event_triggers_dict.get("onlyfans_help_today", False):
        return "Already helped today."
    if time_of_day >= 4:
        return "Not enough time."
    return True

def add_mom_onlyfans_help_action():
    mom.add_action(
        Action("Help her with OnlyFanatics {image=time_advance}",
            mom_onlyfans_help_requirement,
            "mom_onlyfans_help",
            is_fast = False)
    )

def sister_instapic_jealous_requirement(person: Person, start_day):
    return (
        day > start_day
        and person.is_at_mc_house
        and not mom.is_at(person.location)
    )

def add_mom_sister_instapic_jealous_action():
    mom.event_triggers_dict["onlyfans_sister_jealous"] = True
    lily.on_talk_event_list.add_action(
        Action("Lily instapic jealous",
            sister_instapic_jealous_requirement,
            "sister_instapic_jealous",
            requirement_args = day + renpy.random.randint(3, 5))
    )

########
# MISC #
########

def aunt_living_with_mc():
    return aunt.has_event_day("arrival") and not aunt.has_event_day("moved_out")

def dose_dinner_with_serum(serum):
    people = [mom, lily]
    if aunt_living_with_mc():
        people.extend((aunt, cousin))
    for person in people:
        mc.inventory.change_serum(serum, -1)
        person.give_serum(copy.copy(serum))
    return

########
# Work #
########

def pick_interview_outfit(person: Person):
    interview_outfit = person.event_triggers_dict.get("mom_work_promotion_outfit", None)
    if interview_outfit is None:
        if person.event_triggers_dict.get("mom_work_promotion_outfit_slutty", False):
            interview_outfit = "business_slutty"
        else:
            interview_outfit = "business_conservative"
    return interview_outfit

def wear_promotion_outfit(person: Person, is_planned = False):
    interview_outfit = mom_business_wardrobe.get_outfit_with_name(pick_interview_outfit(person)).get_copy()
    if not interview_outfit:
        interview_outfit = mom_business_wardrobe.decide_on_outfit(person, sluttiness_modifier = 0.2 if person.event_triggers_dict.get("mom_work_promotion_outfit_slutty", False) else -0.1)
    if interview_outfit:
        if is_planned:
            person.planned_outfit = interview_outfit
        person.apply_outfit(interview_outfit, show_dress_sequence = not is_planned)

def mom_work_promotion_one_before_requirement(person: Person, start_day):
    if mc.business.is_weekend or day < start_day or not person.has_job(mom_associate_job):
        return False
    if person.is_sleeping:
        return False #she is sleeping in
    return True

def add_mom_work_promotion_one_before_crisis(person: Person):
    mc.business.add_mandatory_morning_crisis(
        Action("mom work promotion one before", mom_work_promotion_one_before_requirement, "mom_work_promotion_one_before", args = person, requirement_args = [person, (day + renpy.random.randint(3, 8))])
    )

def mom_work_promotion_two_intro_requirement(person: Person, start_day):
    if day < start_day or time_of_day != 4 or mc.business.is_weekend:
        return False
    return person.has_job(mom_associate_job)

def add_mom_work_promotion_two_intro_crisis(person: Person):
    mc.business.add_mandatory_crisis(
        Action("mom work promotion two intro crisis", mom_work_promotion_two_intro_requirement, "mom_work_promotion_two_intro", args = person, requirement_args = [person, (day + renpy.random.randint(2, 4))])
    )

def mom_work_promotion_two_report_requirement(person: Person):
    if time_of_day < 2: # only at end of day
        return False
    if not person.has_job(mom_associate_job):
        return False
    if not person.is_at_mc_house: #Only talk about this at home
        return False
    return True

def add_mom_work_promotion_two_report_crisis(person: Person):
    person.add_unique_on_room_enter_event(
        Action("mom work promotion two report", mom_work_promotion_two_report_requirement, "mom_work_promotion_two_report", priority = 30)
    )

def mom_work_promotion_two_requirement(person: Person, start_day):
    if day < start_day or mc.business.is_weekend:
        return False
    if person.is_sleeping:
        return False #she is sleeping in
    return person.has_job(mom_associate_job)

def add_mom_work_promotion_two_crisis(person: Person):
    mc.business.add_mandatory_morning_crisis(
        Action("mom_work_promotion_two_crisis", mom_work_promotion_two_requirement, "mom_work_promotion_two", args = person, requirement_args = [person, (day + renpy.random.randint(6, 9))])
    )

def mom_work_promotion_one_report_requirement(person: Person, start_day):
    if day <= start_day and time_of_day <= 2:   # same day too early for interview to have happened
        return False
    if not person.has_job(mom_associate_job):
        return False
    if not person.is_at_mc_house: # only talk at home
        return False
    return True

def add_mom_work_promotion_one_report_crisis(person: Person):
    person.add_unique_on_room_enter_event(
        Action("mom work promotion one report", mom_work_promotion_one_report_requirement, "mom_work_promotion_one_report", requirement_args = day, priority = 30)
    )

def mom_work_secretary_replacement_intro_requirement(person: Person, the_day: int):
    if day < the_day or mc.business.is_weekend:
        return False
    if not person.has_job(mom_secretary_job):
        return False
    if mc.location.person_count > 1:
        return False
    if person.effective_sluttiness() < 40:    #This is now a 40 sluttiness event for Jennifer
        return False
    return True

def add_mom_work_secretary_replacement_action(person: Person):
    person.event_triggers_dict["mom_office_slutty_level"] = 1

    person.add_unique_on_talk_event(
        Action("Mom work secretary replacement", mom_work_secretary_replacement_intro_requirement, "mom_work_secretary_replacement_intro", requirement_args = [day + 7], priority = 30)
    )


def mom_work_secretary_replacement_report_requirement(person: Person, the_day: int):
    if day < the_day or time_of_day < 2 or mc.business.is_weekend:
        return False
    if not person.has_job(mom_secretary_job):
        return False
    if (person.event_triggers_dict.get("mom_replacement_approach_waiting_for_tits", False) and Person.rank_tits(person.tits) <= Person.rank_tits(person.event_triggers_dict.get("mom_replacement_approach_waiting_for_tits", False))):
        return False
    if not mc.business.is_open_for_business:
        return False
    if mc.location.person_count > 1:
        return False # She doesn't want to talk about it
    return True

def add_mom_work_seduce_action(person: Person, approach = "tits"):
    person.event_triggers_dict["mom_replacement_approach"] = approach
    if approach == "tits":
        person.event_triggers_dict["mom_replacement_approach_waiting_for_tits"] = person.tits

    person.add_unique_on_talk_event(
        Action("mom_work_secretary_replacement_seduction_report", mom_work_secretary_replacement_report_requirement, "mom_work_secretary_replacement_report", requirement_args = [day + 1], priority = 30)
    )

def mom_got_boobjob_requirement(start_day):
    return day >= start_day

def add_mom_got_boobjob_action(person: Person):
    person.event_triggers_dict["getting boobjob"] = True #Reset the flag so you can ask her to get _another_ boobjob.
    mc.business.add_mandatory_crisis(
        Action("Mom Got Boobjob", mom_got_boobjob_requirement, "mom_got_boobjob_label", args = person, requirement_args = day + renpy.random.randint(3, 6))
    )

def create_mom_office_secretary():
    secretary = create_random_person(job = secretary_job)
    secretary.generate_home()
    secretary.home.add_person(secretary)
    mc.business.event_triggers_dict["mom_office_secretary"] = secretary.identifier
    secretary.primary_job.job_known = True
    return secretary

def get_mom_secretary():
    identifier = mc.business.event_triggers_dict.get("mom_office_secretary", None)
    if not identifier:
        return create_mom_office_secretary()
    secretary = Person.get_person_by_identifier(identifier)
    if not isinstance(secretary, Person):   # maybe got removed from game
        return create_mom_office_secretary()
    return secretary

def get_mom_office_actions():
    ask_for_actions = ["Ask for someone"]
    other_actions = ["Other", "Leave"]

    ask_for_actions.append(mom)
    if mom.event_triggers_dict.get("mom_promotion_boss_phase_one", False) and mom.event_triggers_dict.get("mom_replacement_approach", None) is None:
        ask_for_actions.append((mom.title + "'s Boss", "Boss"))
    return [ask_for_actions, other_actions]


################
# Taboo Quests #
################

def mom_kissing_quest_1_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_kissing_quest_active", False):
        return False
    if person.event_triggers_dict.get("mom_kissing_quest_1_complete", False):
        return False
    if time_of_day >= 4:
        return "Not enough time"
    if mc.energy < 20:
        return "Not enough energy"
    return True

def mom_kissing_quest_2_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_kissing_quest_active", False):
        return False
    if person.event_triggers_dict.get("mom_kissing_quest_2_complete", False):
        return False
    if time_of_day >= 4:
        return "Not enough time"
    if mc.energy < 20:
        return "Not enough energy"
    return True

def mom_kissing_quest_3_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_kissing_quest_active", False):
        return False
    if person.event_triggers_dict.get("mom_kissing_quest_3_complete", False):
        return False
    if time_of_day >= 4:
        return "Not enough time"
    if mc.energy < 20:
        return "Not enough energy"
    return True

def mom_kissing_quest_4_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_kissing_quest_active", False):
        return False
    if person.event_triggers_dict.get("mom_kissing_quest_4_complete", False):
        return False
    if time_of_day >= 4:
        return "Not enough time"
    if mc.energy < 20:
        return "Not enough energy"
    return True

def mom_kissing_taboo_break_revisit_complete_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_kissing_quest_active", False):
        return False
    if person.event_triggers_dict.get("kissing_taboo_revisit_quest_progress", 0) < 4:
        return str(person.event_triggers_dict.get("kissing_taboo_revisit_quest_progress", 0)) + "/4 chores complete."
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_mom_kissing_taboo_quests():
    mom.change_slut(-10)
    mom.event_triggers_dict["mom_kissing_quest_active"] = True

    bedroom.add_action(
        Action("Clean your room {image=time_advance}\n{menu_red}Costs: {energy=20}", mom_kissing_quest_1_requirement, "mom_kissing_taboo_break_revisit_quest_1", args = mom, requirement_args = mom, priority = 20)
    )
    hall.add_action(
        Action("Clean the bathroom {image=time_advance}\n{menu_red}Costs: {energy=20}{/menu_red}", mom_kissing_quest_2_requirement, "mom_kissing_taboo_break_revisit_quest_2", args = mom, requirement_args = mom, priority = 20)
    )
    hall.add_action(
        Action("Clean the living room {image=time_advance}\n{menu_red}Costs: {energy=20}{/menu_red}", mom_kissing_quest_3_requirement, "mom_kissing_taboo_break_revisit_quest_3", args = mom, requirement_args = mom, priority = 20)
    )
    kitchen.add_action(
        Action("Clean the fridge {image=time_advance}\n{menu_red}Costs: {energy=20}{/menu_red}", mom_kissing_quest_4_requirement, "mom_kissing_taboo_break_revisit_quest_4", args = mom, requirement_args = mom, priority = 20)
    )
    mom.add_action(
        Action("Check back in...", mom_kissing_taboo_break_revisit_complete_requirement, "mom_kissing_taboo_break_revisit_complete")
    )

def finish_mom_kissing_taboo_quest1():
    mom.event_triggers_dict["kissing_taboo_revisit_quest_progress"] = mom.event_triggers_dict.get("kissing_taboo_revisit_quest_progress", 0) + 1
    mom.event_triggers_dict["mom_kissing_quest_1_complete"] = True
    bedroom.remove_action("mom_kissing_taboo_break_revisit_quest_1")

def finish_mom_kissing_taboo_quest2():
    mom.event_triggers_dict["kissing_taboo_revisit_quest_progress"] = mom.event_triggers_dict.get("kissing_taboo_revisit_quest_progress", 0) + 1
    mom.event_triggers_dict["mom_kissing_quest_2_complete"] = True
    hall.remove_action("mom_kissing_taboo_break_revisit_quest_2")

def finish_mom_kissing_taboo_quest3():
    mom.event_triggers_dict["kissing_taboo_revisit_quest_progress"] = mom.event_triggers_dict.get("kissing_taboo_revisit_quest_progress", 0) + 1
    mom.event_triggers_dict["mom_kissing_quest_3_complete"] = True
    hall.remove_action("mom_kissing_taboo_break_revisit_quest_3")

def finish_mom_kissing_taboo_quest4():
    mom.event_triggers_dict["kissing_taboo_revisit_quest_progress"] = mom.event_triggers_dict.get("kissing_taboo_revisit_quest_progress", 0) + 1
    mom.event_triggers_dict["mom_kissing_quest_4_complete"] = True
    kitchen.remove_action("mom_kissing_taboo_break_revisit_quest_4")

def finish_mom_kissing_taboo_quests():
    mom.change_slut(10, 40)
    end_mom_kissing_taboo_quests()

def end_mom_kissing_taboo_quests():
    mom.event_triggers_dict["mom_kissing_quest_active"] = False
    mom.event_triggers_dict["kissing_revisit_complete"] = True
    mom.remove_action("mom_kissing_taboo_break_revisit_complete")
    mom.remove_queued_event("mom_kissing_taboo_break_revisit")
    bedroom.remove_action("mom_kissing_taboo_break_revisit_quest_1")
    hall.remove_action("mom_kissing_taboo_break_revisit_quest_2")
    hall.remove_action("mom_kissing_taboo_break_revisit_quest_3")
    kitchen.remove_action("mom_kissing_taboo_break_revisit_quest_4")

    for taboo in mom.event_triggers_dict.get("kissing_revisit_restore_taboos", []):
        mom.break_taboo(taboo, add_to_log = False, fire_event = False)

def mom_oral_quest_complete_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_oral_quest_active", False):
        return False
    if aunt.love < 40:
        return f"Requires: {aunt.fname} >= 40 Love"
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_mom_oral_taboo_quest():
    mom.change_slut(-10)
    mom.event_triggers_dict["mom_oral_quest_active"] = True
    mom.add_action(
        Action("Check back in...", mom_oral_quest_complete_requirement, "mom_oral_taboo_break_revisit_complete")
    )

def finish_mom_oral_taboo_quest():
    mom.change_slut(10, 50)
    end_mom_oral_taboo_quest()

def end_mom_oral_taboo_quest():
    mom.event_triggers_dict["mom_oral_quest_active"] = False
    mom.event_triggers_dict["oral_revisit_complete"] = True
    mom.remove_action("mom_oral_taboo_break_revisit_complete")
    mom.remove_queued_event("mom_oral_taboo_break_revisit")
    add_mother_anal_curiosity_intro_action()
    for taboo in mom.event_triggers_dict.get("oral_revisit_restore_taboos", []):
        mom.break_taboo(taboo, add_to_log = False, fire_event = False)

def mom_anal_quest_complete_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_anal_quest_active", False):
        return False
    if not mc.business.has_funds(20000):
        return "Insufficient funds"
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_mom_anal_taboo_quest():
    mom.change_slut(-10)
    mom.event_triggers_dict["mom_anal_quest_active"] = True
    mom.add_action(
        Action("Pay off her debt\n{menu_red}Costs: $20,000{/menu_red}",
            mom_anal_quest_complete_requirement,
            "mom_anal_taboo_break_revisit_complete")
    )

def finish_mom_anal_taboo_quest():
    mc.business.change_funds(-20000, stat = "Family Support")
    mom.change_slut(10, 65)
    end_mom_anal_taboo_quest()

def end_mom_anal_taboo_quest():
    mom.event_triggers_dict["mom_anal_quest_active"] = False
    mom.event_triggers_dict["anal_revisit_complete"] = True
    mom.break_taboo("anal_sex")
    mom.remove_action("mom_anal_taboo_break_revisit_complete")
    mom.remove_queued_event("mom_anal_taboo_break_revisit")
    mom.break_taboo("anal_sex", add_to_log = False, fire_event = False)


def mom_vaginal_quest_2_requirement(person: Person):
    if not person.event_triggers_dict.get("mom_vaginal_quest_active", False):
        return False
    if person.event_triggers_dict.get("mom_vaginal_quest_progress", 0) != 1:
        return False
    if person.is_at_mc_house:
        return f"Not with {mom.fname} around"
    if time_of_day >= 4:
        return "Not enough time"
    return True

def mom_vaginal_quest_3_requirement(person: Person, trigger_day):
    if day < trigger_day:
        return False
    if time_of_day != 3: #Prevents the event from triggering in the morning instead of the evening.
        return False
    return True

def mom_vaginal_quest_complete_requirement(person: Person):
    return person.is_home

def activate_mom_vaginal_taboo_quest2():
    mom.event_triggers_dict["mom_vaginal_quest_progress"] = 1
    mom_bedroom.add_action(
        Action("Check mom's advice post {image=time_advance}", mom_vaginal_quest_2_requirement, "mom_vaginal_taboo_break_revisit_quest_2", args = mom, requirement_args = mom, priority = 20, is_fast = False)
    )

def activate_mom_vaginal_taboo_quest3():
    mom.event_triggers_dict["mom_vaginal_quest_progress"] = 2
    mc.business.add_mandatory_crisis(
        Action("Mom makes a decision", mom_vaginal_quest_3_requirement, "mom_vaginal_quest_3", args = mom, requirement_args = [mom, day + renpy.random.randint(1, 3)])
    )

def activate_mom_vaginal_taboo_final_part():
    mom.add_unique_on_room_enter_event(
        Action("Seduce my son", mom_vaginal_quest_complete_requirement, "mom_vaginal_taboo_break_revisit_complete", priority = 30)
    )

def finish_mom_vaginal_taboo_quest():
    mom.change_slut(10, 85)
    end_mom_vaginal_taboo_quest()

def end_mom_vaginal_taboo_quest():
    mom.event_triggers_dict["mom_vaginal_quest_active"] = False
    mom.event_triggers_dict["vaginal_revisit_complete"] = True
    mc.business.remove_mandatory_crisis("mom_vaginal_quest_3")
    mom_bedroom.remove_action("mom_vaginal_taboo_break_revisit_quest_2")
    mom.remove_queued_event("mom_vaginal_taboo_break_revisit")
    mom.break_taboo("vaginal_sex", add_to_log = False, fire_event = False)

def mom_home_outfit_check(outfit: Outfit, outfit_type = "full"):
    if not isinstance(outfit, Outfit) or not outfit.has_shoes:
        return False
    if mom.sluttiness < 70:
        return not (outfit.vagina_visible or outfit.tits_visible or not outfit.has_apron or not (outfit.has_pants or outfit.has_skirt))
    elif mom.event_triggers_dict.get("vaginal_revisit_complete", False):
        return not (not outfit.has_apron)
    elif mom.event_triggers_dict.get("anal_revisit_complete", False):
        return not (not outfit.has_apron and outfit.wearing_panties)
    elif mom.event_triggers_dict.get("oral_revisit_complete", False):
        return not (outfit.vagina_visible or not outfit.has_apron or not (outfit.has_pants or outfit.has_skirt))
    return False
