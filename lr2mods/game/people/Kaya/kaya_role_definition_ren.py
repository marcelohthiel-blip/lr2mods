from __future__ import annotations
from renpy import persistent
from game.major_game_classes.character_related.Person_ren import Person, mc, kaya, erica
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, student_job, intern_salary_function
from game.major_game_classes.clothing_related.Wardrobe_ren import barista_uniforms
from game.major_game_classes.game_logic.Room_ren import university, coffee_shop
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.game_roles.business_roles._business_role_definitions_ren import college_intern_role
from game.game_roles.business_roles._duty_definitions_ren import general_duties_list, general_rd_duties, research_work_duty
from game.people.Nora.nora_role_definition_ren import add_nora_unlock_interns_program

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def kaya_get_drinks_requirement(person: Person):
    if not person.is_at(coffee_shop):
        return False
    if person.progress.love_step >= 2:
        return False
    if person.love < 20:
        return "Requires 20 love"
    if mc.has_open_time_slot(3, day_restriction = (day % 7,)):
        return "You already have plans tonight"
    if time_of_day != 3:
        return "Check in the evening"
    return True

def kaya_barista_fuck_requirement(person: Person):
    if not kaya_can_get_barista_quickie():
        return False
    if day > kaya.get_event_day("barista_fuck_last_day") + 3:
        if time_of_day != 2:
            return "Only in the afternoon"
        return True
    return "Wait a few days"

def get_kaya_role_actions():
    # kaya_get_drinks = Action("Ask to get drinks", kaya_get_drinks_requirement, "kaya_get_drinks_label")
    kaya_barista_fuck = Action("Fuck her on her break", kaya_barista_fuck_requirement, "kaya_barista_fuck_label")
    return [kaya_barista_fuck]

def kaya_intro_requirement(person: Person):
    return person.is_at_job("Barista")

def initialise_kaya_roaming():

    # she works as barista in the weekend, this is the side-job she will keep
    kaya.set_override_schedule(None)
    kaya_role = Role("Kaya Barista", get_kaya_role_actions(), hidden = True) #Hide her role because we don't want to display it.
    kaya_barista_job = JobDefinition("Barista", [kaya_role], coffee_shop, day_slots = [5, 6], time_slots = [1, 2, 3], wardrobe = barista_uniforms)
    kaya.set_side_job(kaya_barista_job, job_known = False)
    kaya.add_unique_on_room_enter_event(
        Action("Meet Kaya", kaya_intro_requirement, "kaya_intro_label", priority = 30)
    )

def kaya_begin_class_schedule():
    # just make her a normal student
    kaya.change_job(student_job)

def kaya_begin_work_program_schedule():
    # clear her student schedule for working days
    kaya.primary_job.set_schedule(None, day_slots = [0, 2, 4])
    kaya_intern_job = JobDefinition("Company Intern", [college_intern_role], job_location = mc.business.r_div,
        day_slots = [0, 2, 4], time_slots = [1, 2, 3], wardrobe = mc.business.r_uniform,
        mandatory_duties = [research_work_duty], available_duties = general_duties_list + general_rd_duties, base_salary_func = intern_salary_function, is_paid = True)
    kaya.change_job(kaya_intern_job, is_primary = False)
    mc.business.college_interns_unlocked = True
    add_nora_unlock_interns_program()

def kaya_ask_out_requirement(person: Person):
    if person.event_triggers_dict.get("drink_enabled", 1) != 1: # She is unable to go out for drinks for story reasons
        return False
    if time_of_day == 3 and person.love > 20 and person.is_at_job("Barista") and not kaya_can_get_drinks():
        return not mc.has_scheduled_appointment
    return False

def add_kaya_ask_out_action():
    kaya.add_unique_on_room_enter_event(
        Action("Ask to get drinks", kaya_ask_out_requirement, "kaya_ask_out_label", priority = 30)
    )
    kaya.event_triggers_dict["intro_complete"] = True

def kaya_meet_erica_at_uni_requirement(person: Person):
    return (person.sluttiness > 20
        and person.is_at(university)
        and erica.love >= 20
        and kaya_had_condom_talk()                  # things have gone further with kaya
        and not person.has_taboo("sucking_cock"))   # erica is more than a friend

def kaya_moving_in_with_mother_intro_requirement(person: Person):
    return person.sluttiness > 40 and person.is_at_job("Barista") and kaya_studies_with_erica()

def add_kaya_meet_erica_at_uni_action():
    kaya.add_unique_on_room_enter_event(
        Action("Kaya can't drink", kaya_moving_in_with_mother_intro_requirement, "kaya_moving_in_with_mother_intro_label", priority = 30)
    )
    kaya.add_unique_on_room_enter_event(
        Action("Kaya and Erica Meet", kaya_meet_erica_at_uni_requirement, "kaya_meet_erica_at_uni_label", priority = 30)
    )
    kaya.event_triggers_dict["drink_date_complete"] = True

# def kaya_lily_study_night_intro_requirement():
#     if not lily.has_job(sister_student_job):
#         return False
#     if day%7 == 1 and time_of_day == 4:
#         return True
#     return False

# def add_kaya_lily_study_night_intro_action():
#     mc.business.add_mandatory_crisis(
#         Action("Kaya and Lily Study",kaya_lily_study_night_intro_requirement,"kaya_lily_study_night_intro_label")
#     )
#     kaya.event_triggers_dict["has_started_internship"] = False
#     town_relationships.update_relationship(lily, kaya, "Friend")

# def kaya_lily_study_night_apology_requirement(person: Person):
#     if not lily.has_job(sister_student_job):
#         return False
#     if person.is_at(coffee_shop):
#         return True
#     return False

# kaya_lily_study_night_apology = Action("Apologise to Kaya",kaya_lily_study_night_apology_requirement,"kaya_lily_study_night_apology_label")

# def kaya_lily_study_night_recurring_requirement(person: Person):
#     if day%7 != 1 or time_of_day != 4 or not lily.has_job(sister_student_job):
#         return False
#     if person.event_triggers_dict.get("last_lily_study_night", 0) >= day:
#         return False
#     return person.is_at(lily.home)

# kaya_lily_study_night_recurring = Action("Kaya and Lily Study",kaya_lily_study_night_recurring_requirement,"kaya_lily_study_night_recurring_label")


def kaya_uni_scholarship_intro_requirement(person: Person):
    # don't start internship before she moved out (changes her job and will lock out the move out / sakari intro)
    if day % 7 >= 4 or not person.event_triggers_dict.get("has_moved", False):
        return False
    return person.love > 40 and mc.business.has_funds(18000) and person.is_at(university)

def add_kaya_uni_scholarship_intro_action():
    kaya.add_unique_on_room_enter_event(
        Action("Start scholarship program", kaya_uni_scholarship_intro_requirement, "kaya_uni_scholarship_intro_label", priority = 30)
    )
    kaya.event_triggers_dict["studies_with_erica"] = True

# def kaya_first_day_of_internship_requirement():
#     return day % 7 == 5 and time_of_day <= 1

# def add_kaya_first_day_of_internship_action():
#     mc.business.add_mandatory_crisis(
#         Action("Kaya's first day as intern", kaya_first_day_of_internship_requirement, "kaya_first_day_of_internship_label")
#     )

# def kaya_asks_for_help_moving_requirement():
#     return time_of_day == 3 and day % 7 in (0, 2, 4, 5) and day >= kaya.event_triggers_dict.get("move_help_day", 9999)

# def add_kaya_asks_for_help_moving_action():
#     mc.business.add_mandatory_crisis(
#         Action("Kaya Needs Help", kaya_asks_for_help_moving_requirement, "kaya_asks_for_help_moving_label")
#     )
#     kaya.event_triggers_dict["move_help_day"] = day + 7
#     kaya.event_triggers_dict["can_get_drinks"] = False
#     #$ kaya.event_triggers_dict["studies_with_lily"] = False

# def kaya_moving_day_requirement():
#     return time_of_day == 1

# def add_kaya_moving_day_action():
#     mc.business.add_mandatory_crisis(
#         Action("Kaya Moves", kaya_moving_day_requirement, "kaya_moving_day_label")
#     )

# def kaya_share_the_news_requirement():
#     return time_of_day == 3 and kaya.is_at(coffee_shop) and day >= kaya.event_triggers_dict.get("share_news_day", 9999)

# def add_kaya_share_the_news_action():
#     mc.business.add_mandatory_crisis(
#         Action("Share the news with Kaya", kaya_share_the_news_requirement, "kaya_share_the_news_label")
#     )
#     kaya.event_triggers_dict["share_news_day"] = day + 7
#     kaya.event_triggers_dict["has_moved"] = True

# def kaya_jennifer_reveal_requirement(person: Person):
#     return False

# kaya_jennifer_reveal = Action("Talk to Jennifer about Kaya",kaya_jennifer_reveal_requirement,"kaya_jennifer_reveal_label")

# def kaya_lily_reveal_requirement(person: Person):
#     return False

# kaya_lily_reveal = Action("Talk to Lily about Kaya", kaya_lily_reveal_requirement,"kaya_lily_reveal_label")

# def kaya_barista_fuck_intro_requirement(person: Person):
#     return time_of_day == 2 and person.sluttiness >= 60 and person.is_at(coffee_shop)

# def sakari_intro_requirement(person: Person):
#     return person.is_at_work

# def add_kaya_barista_fuck_intro_action():
#     kaya.add_unique_on_talk_event(
#         Action("Kaya takes a break at work", kaya_barista_fuck_intro_requirement, "kaya_barista_fuck_intro_label")
#     )
#     sakari.add_unique_on_room_enter_event(
#         Action("See Sakari at Clothing Store", sakari_intro_requirement, "sakari_intro_label", priority = 30)
#     )
#     # set her sneaking to work during kaya's study hours
#     sakari.primary_job.set_schedule(clothing_store, day_slots = [0, 1, 2, 3, 4], time_slots = [1]) #

# def kaya_jennifer_confrontation_requirement():
#     if willing_to_threesome(kaya, mom):
#         return True
#     return False

def kaya_condom_talk_requirement():
    if time_of_day == 1 and kaya.is_at_job("Barista"):  #She is at the coffeeshop and it is the morning.
        if kaya.love >= 50 and kaya.progress.love_step >= 5:    #Her love story is ready
            return True
        if kaya.sluttiness >= 70:   #She is straight up slutty enough
            return True
        if kaya.sluttiness >= 50 and kaya.progress.lust_step >= 2:
            return True
    return False

def add_kaya_condom_talk_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya has an urgent message", kaya_condom_talk_requirement, "kaya_condom_talk_label")
    )


def kaya_has_finished_intro():
    return kaya.event_triggers_dict.get("intro_complete", False)   # True after first talk

def kaya_can_get_drinks():
    return kaya.event_triggers_dict.get("can_get_drinks", False)

def kaya_has_had_drink_date():
    return kaya.event_triggers_dict.get("drink_date_complete", False)

def kaya_can_get_barista_quickie():
    return kaya.event_triggers_dict.get("can_get_barista_quickie", False)

def kaya_has_started_internship():
    return kaya.event_triggers_dict.get("has_started_internship", False)

def kaya_is_virgin():
    return kaya.event_triggers_dict.get("is_virgin", True)

def kaya_has_moved():
    return kaya.event_triggers_dict.get("has_moved", False)

def kaya_had_condom_talk():
    return kaya.event_triggers_dict.get("no_condom_talk", False)

def kaya_condom_check():    #Generally, events with Kaya should skip condom scene, UNLESS pregnancy pref is set to 0. Use this to determine if skip_condom should be true
    return persistent.pregnancy_pref != 0

def kaya_studies_with_lily():
    return kaya.event_triggers_dict.get("studies_with_lily", False)

def kaya_studies_with_erica():
    return kaya.event_triggers_dict.get("studies_with_erica", False)

def kaya_mc_knows_relation():
    return kaya.event_triggers_dict.get("mc_knows_relation", False)

def kaya_can_get_work_quickie():
    return kaya.event_triggers_dict.get("can_get_work_quickie", False)
