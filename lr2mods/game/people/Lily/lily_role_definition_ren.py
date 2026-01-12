from __future__ import annotations
import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.game_roles._role_definitions_ren import generic_student_role
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import lily_bedroom, electronics_store
from game.major_game_classes.character_related.Person_ren import Person, mc, mom, lily
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.character_related._job_definitions_ren import student_job

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

def sister_kissing_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def sister_oral_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def sister_anal_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def sister_vaginal_taboo_revisit_requirement(person: Person):
    return person.location.person_count <= 1 and not person.is_sleeping

def sister_on_day(person: Person):
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

            taboo_revisit_event = Action("sis kissing taboo revisit", sister_kissing_taboo_revisit_requirement, "sister_kissing_taboo_break_revisit", priority = 50)
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
            taboo_revisit_event = Action("sis oral taboo revisit", sister_oral_taboo_revisit_requirement, "sister_oral_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                for a_taboo in broken_taboos:
                    person.restore_taboo(a_taboo, add_to_log = False)
                person.add_unique_on_room_enter_event(taboo_revisit_event)
            person.event_triggers_dict["oral_revisit_restore_taboos"] = broken_taboos

    if person.has_broken_taboo("anal_sex") and not person.event_triggers_dict.get("anal_revisit_complete", False):
        if person.is_girlfriend:
            person.event_triggers_dict["anal_revisit_complete"] = True
        else:
            taboo_revisit_event = Action("sis anal taboo revisit", sister_anal_taboo_revisit_requirement, "sister_anal_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                person.restore_taboo("anal_sex", add_to_log = False)
                person.add_unique_on_room_enter_event(taboo_revisit_event)

    if person.has_broken_taboo("vaginal_sex") and not person.event_triggers_dict.get("vaginal_revisit_complete", False):
        if person.is_girlfriend:
            person.event_triggers_dict["vaginal_revisit_complete"] = True
        else:
            taboo_revisit_event = Action("sis vaginal taboo revisit", sister_vaginal_taboo_revisit_requirement, "sister_vaginal_taboo_break_revisit", priority = 50)
            if not person.has_queued_event(taboo_revisit_event):
                person.restore_taboo("vaginal_sex", add_to_log = False)
                person.add_unique_on_room_enter_event(taboo_revisit_event)

def sister_reintro_action_requirement(person: Person):
    return mc.business.event_triggers_dict.get("sister_needs_reintro", False)

def sister_serum_test_requirement(person: Person):
    if not mc.business.event_triggers_dict.get("sister_serum_test", False):
        return False
    if not person.is_home:
        return False
    if not mc.business.has_funds(50):
        return "Requires: $50"
    return True

def validate_sister_serum(serum: SerumDesign):
    slutty_serum = False #Set true if it raises Sluttiness OR Arousal.
    happy_serum = False #Set true if it raises Happiness
    test_person = make_person(job = student_job)
    start_happinesss = test_person.happiness
    start_sluttiness = test_person.effective_sluttiness()
    start_max_arousal = test_person.max_arousal
    start_arousal = test_person.arousal

    test_person.give_serum(serum, add_to_log = False)
    test_person.run_turn()

    if test_person.happiness > start_happinesss:
        happy_serum = True
    if test_person.effective_sluttiness() > start_sluttiness:
        slutty_serum = True
    if test_person.max_arousal < start_max_arousal or test_person.arousal > start_arousal + 20:
        slutty_serum = True
    return (slutty_serum, happy_serum)

def sister_strip_reintro_requirement(person: Person):
    if not mc.business.event_triggers_dict.get("sister_strip_reintro", False):
        return False
    if not mc.is_at(person.home):
        return False
    if len(person.home.people) > 1:
        return False
    if person.sluttiness < 30:
        return "Requires: " + get_gold_heart(30)
    return True

def sister_strip_requirement(person: Person): #She'll only strip if you're in her bedroom and alone.
    if not mc.business.event_triggers_dict.get("sister_strip", False):
        return False
    if not mc.is_at(lily_bedroom):
        return False
    if len(lily_bedroom.people) > 1:
        return False
    if person.sluttiness < 30 or not mc.business.has_funds(100):
        return "Requires: $100, " + get_gold_heart(30)
    return True

def sister_boobjob_give_serum_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_boobjob_serum_enabled", False):
        return False
    if person.event_triggers_dict.get("sister_boobjob_serum_count", 0) >= 3:
        return False
    if person.event_triggers_dict.get("sister_boobjob_serum_last_day", -1) >= day:
        return "Already taken a dose today."
    return True

def sister_get_boobjob_talk_requirement(person: Person):
    return person.event_triggers_dict.get("sister_boobjob_ask_enabled", False)

def mom_girlfriend_ask_blessing_requirement(person: Person):
    return person.event_triggers_dict.get("mom_girlfriend_ask_blessing", False)

def sister_girlfriend_return_requirement(person: Person): #This is an action Lily has, enabled when you've talked to Mom
    if person.event_triggers_dict.get("sister_girlfriend_mom_blessing_given", None) is None:
        return False
    if person.event_triggers_dict.get("sister_girlfriend_waiting_for_blessing", False) and person.event_triggers_dict.get("sister_girlfriend_ask_blessing", False):
        return "Talk to [mom.title] first."
    return True

def get_sister_role_actions():
    #SISTER ACTIONS#
    sister_reintro_action = Action("Ask if she needs extra work", sister_reintro_action_requirement, "sister_reintro_label",
        menu_tooltip = "She was eager to make some money before, maybe she still is.")

    sister_serum_test_action = Action("Ask her to test serum", sister_serum_test_requirement, "sister_serum_test_label",
        menu_tooltip = "Have your sister test serum for you. Over time she will become more comfortable following your orders and making deals with you.")

    sister_strip_reintro_action = Action("Ask if she would strip for pay", sister_strip_reintro_requirement, "sister_strip_reintro_label",
        menu_tooltip = "She was eager to make some money, maybe she will be willing to strip for you if you pay her.")

    sister_strip_action = Action("Ask her to strip for you", sister_strip_requirement, "sister_strip_label",
        menu_tooltip = "Have your sister strip for you, in exchange for some money.", priority = 5)

    sister_boobjob_give_serum_action = Action("Give her some breast enhancement serum", sister_boobjob_give_serum_requirement, "sister_give_boobjob_serum_label",
        menu_tooltip = "Give your sister some serum, which she thinks will grow her boobs.", priority = 10)

    sister_boobjob_ask_action = Action("Talk about getting implants", sister_get_boobjob_talk_requirement, "sister_get_boobjob",
        menu_tooltip = "Talk to your sister about the implants she wants to get.", priority = 10)

    sister_mom_girlfriend_blessing_action = Action("Talk about Mom", mom_girlfriend_ask_blessing_requirement, "mom_girlfriend_sister_blessing",
        menu_tooltip = "Try and convince her to give you and Mom her blessing.", priority = 100)

    sister_girlfriend_return_action = Action("Give her the news", sister_girlfriend_return_requirement, "sister_girlfriend_return",
        menu_tooltip = "Tell her how your conversation with Mom went.", priority = 100)

    return [sister_reintro_action, sister_serum_test_action, sister_strip_reintro_action, sister_strip_action, sister_boobjob_give_serum_action, sister_boobjob_ask_action, sister_mom_girlfriend_blessing_action, sister_girlfriend_return_action]

def init_sister_roles():
    global sister_role
    sister_role = Role("Sister", get_sister_role_actions(), on_day = sister_on_day, hidden = True)
    global sister_student_role
    sister_student_role = Role("Student", get_sister_student_role_actions(), hidden = True, looks_like = generic_student_role)

def sister_offer_to_hire_requirement(person: Person): #NOTE: This is attached to the sister student role.
    if person.event_triggers_dict.get("dropout_convince_progress", 0) > 2:
        return False
    if person.love < 10:
        return False
    if person.love < 20:
        return "Requires: 20 Love"
    if mc.business.at_employee_limit:
        return "At employee limit"
    return True

def get_sister_student_role_actions():
    sister_hire_offer_action = Action("Offer to hire her at [mc.business.name]", sister_offer_to_hire_requirement, "sister_offer_to_hire",
        menu_tooltip = "Offer her a job at your company. You'll have to convince her to drop out of school first...")
    return [sister_hire_offer_action]

def mother_sister_dropout_convince_requirement(person: Person):
    return lily.event_triggers_dict.get("dropout_convince_progress", 0) == 1

def add_sister_dropout_convince_action():
    lily.event_triggers_dict["dropout_convince_progress"] = 1
    mom.add_action(
        Action("Let " + lily.fname + " drop out", mother_sister_dropout_convince_requirement, "mother_sister_dropout_convince_label",
        menu_tooltip = "Convince " + mom.fname + " to let her daughter drop out of school and come work for you.")
    )

def finish_sister_drop_out_of_school():
    mom.remove_action("mother_sister_dropout_convince_label")
    lily.event_triggers_dict["dropout_convince_progress"] = 3

def instathot_requirement(person: Person):
    if not person.is_home or person.location.person_count > 1 or person.is_sleeping:
        return False
    if time_of_day == 4:
        return "Too late to take pictures"
    if time_of_day == 1:
        return "Too early to take pictures"
    return True

def add_sister_instahot_action():
    lily.add_action(
        Action("Help her take Insta-pics {image=time_advance}", instathot_requirement, "sister_instathot_label",
               menu_tooltip = "Help your sister grow her Insta-pic account by taking some pictures of her.")
    )

def sister_instathot_mom_report_requirement(person: Person, start_day: int):
    if day <= start_day:
        return False #Wait at least a day
    if mom in mc.location.people:
        return False #Don't talk to her in front of her face.
    return mc.is_home

def add_sister_instathot_mom_report_action(person: Person):
    person.add_unique_on_talk_event(
        Action("Sister instathot mom report crisis", sister_instathot_mom_report_requirement, "sister_instathot_mom_report", requirement_args = day, priority = 30)
    )

def sister_serum_new_boobs_check_requirement(person: Person, start_size: str, end_day: int):
    if person.rank_tits(person.tits) - person.rank_tits(start_size) >= 2:
        return True #Her boobs grew, she'll trigger her brag event
    if day >= end_day:
        return True #It's been too long, she'll trigger the fail/timeout event.
    return False #Don't trigger until one of those conditions is met.

def add_sister_boobjob_serum_check_action(person: Person):
    mc.business.add_mandatory_crisis(
        Action("sister_serum_boobjob_check", sister_serum_new_boobs_check_requirement, "sister_serum_new_boobs_check", args = [person, person.tits], requirement_args = [person, person.tits, day + 10])
    )

def sister_got_boobjob_requirement(start_day: int):
    return day >= start_day

def add_sister_got_boobjob_action():
    if lily.event_triggers_dict.get("getting boobjob", False):
        return # she already has one
    lily.event_triggers_dict["getting boobjob"] = True
    mc.business.add_mandatory_crisis(
        Action("Sister got boobjob", sister_got_boobjob_requirement, "sister_got_boobjob_label", args = lily, requirement_args = day + renpy.random.randint(3, 6))
    )

def sister_serum_boobjob_fail_requirement(person: Person):
    return True

def add_sister_boobjob_serum_result_action(person: Person, starting_tits: str):
    if Person.rank_tits(person.tits) - Person.rank_tits(starting_tits) >= 2:
        add_sister_boobjob_result_brag_action(person, True)
    else: #Handles all the possible ways the serum checks could fail.
        person.add_unique_on_room_enter_event(
            Action("Sister_serum_boobjob_fail", sister_serum_boobjob_fail_requirement, "sister_serum_partial_boobjob_label", args = starting_tits, priority = 30)
        )

def sister_boobjob_brag_requirement(person: Person):
    return True

def add_sister_boobjob_result_brag_action(person: Person, from_serum = False):
    person.add_unique_on_room_enter_event(
        Action("Sister_new_boobs_brag", sister_boobjob_brag_requirement, "sister_new_boobs_brag_label", args = from_serum, priority = 30)
    )


################
# Taboo Quests #
################

def sister_kissing_quest_complete_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_kissing_quest_active", False):
        return False
    if person.event_triggers_dict.get("sister_kissing_quest_progress", 0) < 3:
        return str(person.event_triggers_dict.get("sister_kissing_quest_progress", 0)) + "/3 InstaPic Sessions."
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_lily_kissing_taboo_quests():
    lily.event_triggers_dict["sister_kissing_quest_active"] = True
    lily.change_slut(-10)
    lily.add_action(
        Action("Check back in...",
            sister_kissing_quest_complete_requirement,
            "sister_kissing_taboo_break_revisit_complete")
    )

def finish_lily_kissing_taboo_quests():
    lily.change_slut(10, 40)
    end_lily_kissing_taboo_quests()

def end_lily_kissing_taboo_quests():
    lily.event_triggers_dict["sister_kissing_quest_active"] = False
    lily.event_triggers_dict["kissing_revisit_complete"] = True
    lily.remove_action("sister_kissing_taboo_break_revisit_complete")
    lily.remove_queued_event("sister_kissing_taboo_break_revisit")
    for taboo in lily.event_triggers_dict.get("kissing_revisit_restore_taboos", []):
        lily.break_taboo(taboo, add_to_log = False, fire_event = False)

def sister_oral_quest_1_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_oral_quest_active", False):
        return False
    if not person.event_triggers_dict.get("sister_oral_quest_progress", 0) == 0:
        return False
    return True

def sister_oral_quest_2_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_oral_quest_active", False):
        return False
    if not person.event_triggers_dict.get("sister_oral_quest_progress", 0) == 1:
        return False
    if not mc.business.has_funds(1200):
        return "Insufficient funds"
    return True

def sister_oral_revisit_quest_complete_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_oral_quest_active", False):
        return False
    if not person.event_triggers_dict.get("sister_oral_quest_progress", 0) == 2:
        return "Buy her a {size=+12}{font=fonts/Crimson-Bold.ttf}\u03C0{/font}{/size}phone"
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_lily_oral_taboo_quests():
    lily.event_triggers_dict["sister_oral_quest_active"] = True
    lily.event_triggers_dict["sister_oral_quest_progress"] = 0
    lily.change_slut(-10)

    electronics_store.add_unique_on_room_enter_event(
        Action("pi phone discover", sister_oral_quest_1_requirement, "sister_oral_taboo_break_revisit_quest_1", args = lily, requirement_args = lily, priority = 30)
    )
    electronics_store.add_action(
        Action("Buy a {size=+12}{font=fonts/Crimson-Bold.ttf}\u03C0{/font}{/size}phone\n{menu_red}Costs: $1200{/menu_red}",
            sister_oral_quest_2_requirement,
            "sister_oral_taboo_break_revisit_quest_2", args = lily, requirement_args = lily)
    )
    lily.add_action(
        Action("Check back in...",
            sister_oral_revisit_quest_complete_requirement,
            "sister_oral_taboo_break_revisit_complete")
    )

def complete_first_part_of_lily_oral_taboo_quests():
    lily.event_triggers_dict["sister_oral_quest_progress"] = 2
    electronics_store.remove_action("sister_oral_taboo_break_revisit_quest_2")

def finish_lily_oral_taboo_quests():
    lily.change_slut(10, 40)
    end_lily_oral_taboo_quests()

def end_lily_oral_taboo_quests():
    lily.event_triggers_dict["sister_oral_quest_active"] = False
    lily.event_triggers_dict["oral_revisit_complete"] = True
    lily.remove_action("sister_oral_taboo_break_revisit_complete")
    lily.remove_queued_event("sister_oral_taboo_break_revisit")
    for taboo in lily.event_triggers_dict.get("oral_revisit_restore_taboos", []):
        lily.break_taboo(taboo, add_to_log = False, fire_event = False)


def sister_anal_revisit_quest_complete_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_anal_quest_active", False):
        return False
    if person.event_triggers_dict.get("sister_instathot_mom_shirtless_covered_count", 0) == 0:
        return "Convince [mom.title] to take shirtless InstaPic shots."
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_lily_anal_taboo_quests():
    lily.change_slut(-10)
    lily.event_triggers_dict["sister_anal_quest_active"] = True
    lily.add_action(
        Action("Check back in...",
            sister_anal_revisit_quest_complete_requirement,
            "sister_anal_taboo_break_revisit_complete")
    )

def finish_lily_anal_taboo_quests():
    lily.change_slut(10, 65)
    end_lily_anal_taboo_quests()

def end_lily_anal_taboo_quests():
    lily.event_triggers_dict["sister_anal_quest_active"] = False
    lily.event_triggers_dict["anal_revisit_complete"] = True
    lily.remove_action("sister_anal_taboo_break_revisit_complete")
    lily.remove_queued_event("sister_anal_taboo_break_revisit")
    lily.break_taboo("anal_sex", add_to_log = False, fire_event = False)

def sister_vaginal_quest_revisit_requirement(person: Person):
    if not person.event_triggers_dict.get("sister_vaginal_quest_active", False):
        return False
    if mc.inventory.get_max_serum_count < 10:
        return "Requires: 10 identical serum doses"
    if person.location.person_count > 1:
        return "Not while other people are around"
    return True

def activate_lily_vaginal_taboo_quests():
    lily.event_triggers_dict["sister_vaginal_quest_active"] = True
    lily.change_slut(-10)
    lily.add_action(
        Action("Hand over the serum",
            sister_vaginal_quest_revisit_requirement,
            "sister_vaginal_taboo_break_revisit_quest_1")
    )

def finish_lily_vaginal_taboo_quests():
    lily.change_slut(10, 85)
    end_lily_vaginal_taboo_quests()

def end_lily_vaginal_taboo_quests():
    lily.event_triggers_dict["sister_vaginal_quest_active"] = False
    lily.event_triggers_dict["vaginal_revisit_complete"] = True
    lily.remove_action("sister_vaginal_taboo_break_revisit_quest_1")
    lily.remove_queued_event("sister_vaginal_taboo_break_revisit")
    lily.break_taboo("vaginal_sex")

def lily_can_give_serum():
    return mc.business.event_triggers_dict.get("sister_serum_test", False)

def lily_get_serums_tested():
    return mc.business.event_triggers_dict.get("sister_serum_test_count", 0)

def lily_will_strip():
    return mc.business.event_triggers_dict.get("sister_strip", False)   #Why vren uses mc.business for this?

def lily_started_insta_story():
    return lily.event_triggers_dict.get("insta_intro_finished", False)

def lily_mom_insta_started():
    return mom.event_triggers_dict.get("mom_instathot_pic_count", 0) > 0

def lily_mom_topless_pics_complete():
    return lily.event_triggers_dict.get("sister_instathot_mom_shirtless_covered_count", 0) > 0

def mom_knows_about_lily():
    return had_family_threesome() or mom.event_triggers_dict.get("sister_girlfriend_mom_knows", False)

def had_family_threesome():
    return mc.business.event_triggers_dict.get("family_threesome", False)
