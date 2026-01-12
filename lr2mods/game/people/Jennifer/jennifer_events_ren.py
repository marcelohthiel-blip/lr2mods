from game.major_game_classes.character_related.Person_ren import Person, mc, mom
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import kitchen, mom_bedroom, mom_office_lobby
from game.sex_positions._position_definitions_ren import blowjob
from game.people.Jennifer.jennifer_definition_ren import mom_associate_job, mom_secretary_job
from game.people.Jennifer.mom_breakfast_progression_scene_definition_ren import mom_breakfast_prog_scene_action

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
def mother_love_lunch_date_requirement():
    return False

# Story progression actions
def add_mother_love_lunch_date_action():
    mother_love_lunch_date_action = Action("Lunch Date With Mom", mother_love_lunch_date_requirement, "mother_love_lunch_date_label")
    mc.business.add_mandatory_crisis(mother_love_lunch_date_action)
    return

###################
#   Lust Events   #
###################

### Jennifer Main Job Events
def mom_lust_story_bridge_requirement(person: Person):
    return (mc.business.is_work_day
        and person.story_event_ready("slut")
        and person.is_at(kitchen)
        and person.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_story_bridge_action():
    mom.add_unique_on_room_enter_event(
        Action("Jennifer's work sluttiness bridge", mom_lust_story_bridge_requirement, "mom_lust_story_bridge_label", priority = 30)
    )
    mom.story_event_log("slut")

def mom_lust_boss_prostitutes_intro_requirement(person: Person):
    return (person.sluttiness >= 60
        and mc.business.is_work_day
        and person.story_event_ready("slut")
        and person.is_at(kitchen)
        and person.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_boss_prostitutes_intro_action():
    mom.add_unique_on_room_enter_event(
        Action("Jennifer's Boss Hires Hookers Intro", mom_lust_boss_prostitutes_intro_requirement, "mom_lust_boss_prostitutes_intro_label", priority = 30)
    )
    mom.story_event_log("slut")

def mom_lust_boss_prostitute_followup_requirement(person: Person):
    return (mc.business.is_work_day
        and person.days_since_event("slut_event") >= TIER_1_TIME_DELAY
        and person.is_at(kitchen)
        and person.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_boss_prostitute_followup_action():
    mom.add_unique_on_room_enter_event(
        Action("Jennifer's Boss Hires Hookers Followup", mom_lust_boss_prostitute_followup_requirement, "mom_lust_boss_prostitute_followup_label", priority = 30)
    )
    mom.story_event_log("slut")

def mom_boss_phase_two_checkup_requirement():
    return (time_of_day == 1
        and mc.business.is_work_day
        and mom.story_event_ready("slut")
        and mom.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_boss_phase_two_checkup_action():
    mom_boss_phase_two_checkup_action = Action("Mom boss followup prompt", mom_boss_phase_two_checkup_requirement, "mom_boss_phase_two_checkup_label")
    mc.business.add_mandatory_crisis(mom_boss_phase_two_checkup_action)
    mom.story_event_log("slut")

def mom_lust_boss_bareback_intro_requirement():
    return (time_of_day in (1, 2, 3)
        and mc.business.is_work_day
        and mom.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_boss_bareback_intro_action():
    mom_office_lobby.add_unique_on_room_enter_event(
        Action("Jennifer's Boss wants bareback", mom_lust_boss_bareback_intro_requirement, "mom_lust_boss_bareback_intro_label", priority = 30)
    )

def mom_lust_boss_bareback_followup_requirement(person: Person):
    return (mc.business.is_work_day
        and person.sluttiness >= 70
        and person.opinion.bareback_sex >= 2
        and person.story_event_ready("slut")
        and person.is_at(kitchen)
        and person.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_boss_bareback_followup_action():
    mom.add_unique_on_room_enter_event(
        Action("Jennifer's Boss wants bareback", mom_lust_boss_bareback_followup_requirement, "mom_lust_boss_bareback_followup_label", priority = 30)
    )
    mom.story_event_log("slut")

def mom_boss_bareback_teamup_requirement():
    return (time_of_day in (1, 2, 3)
        and mc.business.is_work_day
        and mom.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_boss_bareback_teamup_action():
    mom_office_lobby.add_unique_on_room_enter_event(
        Action("Jennifer's Boss gets it bareback", mom_boss_bareback_teamup_requirement, "mom_boss_bareback_teamup_label", priority = 30)
    )

def mom_lust_boss_anal_intro_requirement(person: Person):
    return False
    return (person.sluttiness >= 80
        and person.story_event_ready("slut")
        and person.is_at(kitchen)
        and person.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_boss_anal_intro_action():
    mom.add_unique_on_room_enter_event(
        Action("Jennifer's Boss gets anal", mom_lust_boss_anal_intro_requirement, "mom_lust_boss_anal_intro_label", priority = 30)
    )
    mom.story_event_log("slut")

def mom_lust_boss_anal_followup_requirement(person: Person):
    return False

def add_mom_lust_boss_anal_followup_action():
    mom.add_unique_on_room_enter_event(
        Action("Blackmail the Boss", mom_lust_boss_anal_followup_requirement, "mom_lust_boss_anal_followup_label", priority = 30)
    )
    # mom.story_event_log("slut")

def mom_lust_boss_tied_up_requirement():
    return (time_of_day == 1
        and mc.business.is_work_day
        and mom.sluttiness >= 90
        and mom.story_event_ready("slut")
        and mom.has_job((mom_secretary_job, mom_associate_job)))

def add_mom_lust_boss_tied_up_action():
    mother_lust_tied_up_at_work_action = Action("Jennifer's Boss ties her up", mom_lust_boss_tied_up_requirement, "mom_lust_boss_tied_up_label")
    mc.business.add_mandatory_crisis(mother_lust_tied_up_at_work_action)
    mom.story_event_log("slut")

def mom_new_employee_first_day_requirement():
    return mc.business.is_work_day

def add_mom_new_employee_first_day_action():
    mc.business.add_mandatory_morning_crisis(
        Action("mom's first day", mom_new_employee_first_day_requirement, "mom_new_employee_first_day_label")
    )
    mom.story_event_log("slut")

########################
#   Obedience Events   #
########################

def mom_obedience_man_of_the_house_intro_requirement():
    return (day % 7 == 5  # saturday morning
        and mom.is_available)

def add_mom_obedience_man_of_the_house_intro_action():
    mc.business.add_mandatory_morning_crisis(
        Action("mom weekly pay intro", mom_obedience_man_of_the_house_intro_requirement, "mom_obedience_man_of_the_house_intro_label")
    )

def mom_obedience_weekly_bills_requirement():
    return (day % 7 == 5  # saturday morning
        and mom.is_available)

def add_mom_obedience_weekly_bills_action():
    mc.business.add_mandatory_morning_crisis(
        Action("Jennifer Weekly Bills", mom_obedience_weekly_bills_requirement, "mom_weekly_bills_label")
    )

def add_mom_obedience_breakfast_intro_action():
    mc.business.add_mandatory_morning_crisis(mom_breakfast_prog_scene_action)
    mom.story_event_log("obedience")

def mom_obedience_home_uniform_requirement():
    return (mom.obedience > 140
        and mom.story_event_ready("obedience")
        and mc.is_home
        and mom.is_at_mc_house
        and mom.outfit.has_shirt
        and (mom.outfit.has_skirt or mom.outfit.has_pants))

def add_mom_obedience_home_uniform_action():
    mc.business.add_mandatory_crisis(
        Action("mom home uniform intro", mom_obedience_home_uniform_requirement, "mom_obedience_home_uniform_label")
    )
    mom.story_event_log("obedience")

#############################
# Story progression actions #
#############################

# Weekly bill payment requirements and menus
def mom_weekly_kiss_requirement():
    return True

def mom_weekly_please_requirement():
    return True

def mom_weekly_see_tits_requirement():
    if mom.effective_sluttiness("bare_tits") >= 20 or ((mom.sluttiness + mom.obedience) - 100) > 30:    # slutty enough, or combined sluttiness and obedience of 20
        return True
    return "Not slutty or obedient enough"

def mom_weekly_touch_me_requirement():
    if mom.effective_sluttiness("touching_penis") >= 30 or ((mom.sluttiness + mom.obedience) - 100) > 50:    # slutty enough, or combined sluttiness and obedience of 30
        return True
    return "Not slutty or obedient enough"

def mom_weekly_see_ass_requirement():
    if mom.effective_sluttiness("bare_pussy") >= 40 or ((mom.sluttiness + mom.obedience) - 100) > 60:    # slutty enough, or combined sluttiness and obedience of 40
        return True
    return "Not slutty or obedient enough"

def mom_weekly_blowjob_requirement():
    return False

def mom_weekly_sex_requirement():
    return False

def mom_weekly_pay_give_blowjob_requirement_temp():
    if mom.is_willing(blowjob) and ((mom.sluttiness + mom.obedience) - 100) > 80:
        return True
    return False

def mom_weekly_glad_to_help_requirement():
    return True

def build_mom_weekly_bills_menu():
    actions_list = [
        Action("Ask for a kiss", mom_weekly_kiss_requirement, "mom_weekly_kiss_label"),
        Action("Just say please", mom_weekly_please_requirement, "mom_weekly_please_label"),
        Action("Show me your tits", mom_weekly_see_tits_requirement, "mom_weekly_see_tits_label"),
        Action("Handjob", mom_weekly_touch_me_requirement, "mom_weekly_touch_me_label"),
        Action("Show me your ass", mom_weekly_see_ass_requirement, "mom_weekly_see_ass_label"),
        Action("Give me a blowjob", mom_weekly_blowjob_requirement, "mom_weekly_blowjob_label"),
        Action("Fuck her", mom_weekly_sex_requirement, "mom_weekly_sex_label"),
        Action("Glad to help", mom_weekly_glad_to_help_requirement, "mom_weekly_glad_to_help_label")
        #Removed birth control weekly deal. Birth control to play a more integral part of her story with her boss fucking her bareback.
    ]
    actions_list.insert(0, "Choose Option")
    return actions_list


####################
#   Other Events   #
####################

def mother_anal_curiosity_intro_requirement():
    return (mom.sluttiness >= 60
        and mom.opinion.anal_sex >= 0
        and time_of_day == 4)
    
def add_mother_anal_curiosity_intro_action():
    mc.business.add_mandatory_crisis(
        Action("mom back massage", mother_anal_curiosity_intro_requirement, "mother_anal_curiosity_intro_label")
    )