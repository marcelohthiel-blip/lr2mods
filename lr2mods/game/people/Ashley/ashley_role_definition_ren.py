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

TIER_1_TIME_DELAY = 5
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
clothing_fade = None
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def ashley_work_titfuck_requirement(person: Person):
    if person.progress.obedience_step != 0 or person.event_triggers_dict.get("sub_titfuck_count", 0) == 0:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if (person.obedience >= 120 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 120 obedience"

def ashley_work_blowjob_requirement(person: Person):
    if person.progress.obedience_step != 1 or person.event_triggers_dict.get("sub_blowjob_count", 0) == 0:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if (person.obedience >= 140 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 140 obedience"

def ashley_work_fuck_requirement(person: Person):
    if person.progress.obedience_step != 2 or person.event_triggers_dict.get("sub_fuck_count", 0) == 0:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if (person.obedience >= 160 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 160 obedience"

def ashley_work_anal_requirement(person: Person):
    if person.progress.obedience_step != 3 or person.event_triggers_dict.get("sub_anal_count", 0) == 0:
        return False
    if not (mc.business.is_open_for_business and person.is_at_office):
        return False
    if (person.obedience >= 180 or person.active_serum_with_hidden_tag("Obedience")):
        return True
    return "Requires 180 obedience"

def get_ashley_submission_role_actions():
    ashley_work_titfuck = Action("Obedience: Fuck Her Tits", ashley_work_titfuck_requirement, "ashley_work_titfuck_label", priority = 20)
    ashley_work_blowjob = Action("Obedience: Get Blowjob", ashley_work_blowjob_requirement, "ashley_work_blowjob_label", priority = 20)
    ashley_work_fuck = Action("Obedience: Fuck Her", ashley_work_fuck_requirement, "ashley_work_fuck_label", priority = 20)
    ashley_work_anal = Action("Obedience: Fuck Her Ass", ashley_work_anal_requirement, "ashley_work_anal_label", priority = 20)
    return [ashley_work_titfuck, ashley_work_blowjob, ashley_work_fuck, ashley_work_anal]

def init_ashley_roles():
    global ashley_submission_role
    ashley_submission_role = Role(role_name ="Ashley Submission", actions = get_ashley_submission_role_actions(), hidden = True)

def ashley_steph_relationship_status():  #This function should return limited options back, to summarize the current status of MC relationship with Steph and Ashley
    if (ashley.sluttiness > 70 or ashley.is_girlfriend) and (stephanie.sluttiness > 70 or stephanie.is_girlfriend):
        return "both"
    if ashley.is_girlfriend:
        return "ashley"
    if stephanie.is_girlfriend:
        return "stephanie"
    if builtins.abs(ashley.love - stephanie.love) < 20: # love difference < 20
        return "both"
    if ashley.love > stephanie.love:
        return "ashley"
    if ashley.love < stephanie.love:
        return "stephanie"
    return "both"

def ashley_hire_directed_requirement():
    if not mc.business.head_researcher == stephanie or not mc.business.is_open_for_business:
        return False
    if mc.business.at_employee_limit:
        return "At employee limit"
    if not mc.is_at_office:
        return "Talk to her at work"
    return True

def ashley_first_talk_requirement(person: Person):
    return person.is_at_office and mc.is_at_office

def ashley_room_overhear_classical_requirement(person: Person):
    if mc.business.p_div.person_count <= 1:
        return False
    if person.is_at_work and mc.business.p_div.person_count > 1:
        return person.current_job.days_employed > TIER_2_TIME_DELAY
    return False

def ashley_ask_date_classic_concert_requirement(person: Person):
    if ashley_get_concert_overheard() and not ashley_get_concert_date_stage() > 0:
        return person.is_at_work
    return False

def ashley_classical_concert_date_requirement():
    if time_of_day == 3 and day % 7 == 3:  #Thursday
        return ashley_get_concert_date_stage() == 1
    return False

def show_concert_hall_background(darken = False, fade = False):
    at_arguments = []
    if fade:
        at_arguments = [clothing_fade]
    if darken:
        renpy.show("concert_hall", what = im.MatrixColor(bg_manager.background("Concert_Hall_Background"), darken_matrix * im.matrix.brightness(-0.15)), layer = "master", tag = "dimmed")
        if fade:
            renpy.show("concert_hall", at_list = at_arguments, what = bg_manager.background("Concert_Hall_Background"), layer = "master", tag = "bright")
    else:
        renpy.show("concert_hall", what = bg_manager.background("Concert_Hall_Background"), layer = "master", tag = "bright")
        if fade:
            renpy.show("concert_hall", at_list = at_arguments, what = im.MatrixColor(bg_manager.background("Concert_Hall_Background"), darken_matrix * im.matrix.brightness(-0.15)), layer = "master", tag = "dimmed")

def set_ashley_hired():
    mc.business.add_employee_production(ashley)
    ashley.set_override_schedule(None)  # let her roam
    ashley.change_location(ashley.home) # move her to her home
    mc.business.set_event_day("prod_assistant_advance") #start production assistant chain
    add_mc_serum_intro_action()

def add_ashley_hire_later_action():
    ashley_hire_directed = Action("Reconsider hiring Stephanie's sister", ashley_hire_directed_requirement, "ashley_hire_directed_label",
        menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
    mc.business.r_div.add_action(ashley_hire_directed)

def remove_ashley_hire_later_action():
    mc.business.r_div.remove_action("ashley_hire_directed_label")

def add_ashley_first_talk_action():
    ashley_first_talk = Action("Introduce yourself to Ashley", ashley_first_talk_requirement, "ashley_first_talk_label", priority = 30)
    ashley.add_unique_on_room_enter_event(ashley_first_talk)

def add_ashley_room_overhear_classical_action():
    ashley_room_overhear_classical = Action("Ashley talks about concert", ashley_room_overhear_classical_requirement, "ashley_room_overhear_classical_label", priority = 30)
    ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
    ashley.event_triggers_dict["intro_complete"] = True
    ashley_ask_date_classic_concert = Action("Ask Ashley to the Concert", ashley_ask_date_classic_concert_requirement, "ashley_ask_date_classic_concert_label", priority = 30)
    ashley.add_action(ashley_ask_date_classic_concert)

def add_ashley_classical_concert_date_action():
    ashley_classical_concert_date = Action("Ashley Date Night", ashley_classical_concert_date_requirement, "ashley_classical_concert_date_label")
    mc.business.add_mandatory_crisis(ashley_classical_concert_date)
    ashley.event_triggers_dict["concert_date"] = 1
    ashley.remove_action("ashley_ask_date_classic_concert_label")

def mc_serum_intro_requirement(person: Person): #This event is exclusive to Ashley
    if not (mc.business.is_open_for_business and mc.is_at_office):
        return False

    if ashley.is_employee and mc.business.days_since_event("prod_assistant_advance") > TIER_2_TIME_DELAY:
        if testing_room_creation_policy.is_active and mc.business.days_since_event("testing_room_unlocked") > TIER_1_TIME_DELAY:
            if found := next((x for x in list_of_traits if x.name == mc_serum_energy_regen.linked_trait), None):
                return found.researched
    return False

def add_mc_serum_intro_action():
    mc_serum_intro = Action("Discover MC Serums", mc_serum_intro_requirement, "mc_serum_intro_label", priority = 30)
    ashley.add_unique_on_room_enter_event(mc_serum_intro)

def mc_serum_timeout_requirement():
    return mc.business.days_since_event("prod_assistant_advance") > TIER_1_TIME_DELAY

def add_mc_serum_timeout_action():
    mc_serum_timeout = Action("Serums runout", mc_serum_timeout_requirement, "mc_serum_timeout_label")
    mc.business.add_mandatory_crisis(mc_serum_timeout)
    mc.business.set_event_day("prod_assistant_advance")

def mc_serum_review_intro_requirement(person: Person):
    return mc.business.is_open_for_business

def add_mc_serum_review_intro_action():
    mc_serum_review_intro = Action("Serum Setup", mc_serum_review_intro_requirement, "mc_serum_review_intro_label", priority = 30)
    ashley.add_unique_on_room_enter_event(mc_serum_review_intro)
    mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = True

def ashley_mc_submission_story_complete():
    return ashley.event_triggers_dict.get("ashley_submission_complete", False)

def ashley_get_mc_obedience():
    return ashley.event_triggers_dict.get("mc_obedience", 0)

def ashley_get_intro_complete():
    return ashley.event_triggers_dict.get("intro_complete", False)

def ashley_get_if_excitement_overheard():
    return ashley.event_triggers_dict.get("excitement_overhear", False)

def ashley_get_attitude_discussed():
    return ashley.event_triggers_dict.get("attitude_discussed", False)

def ashley_get_porn_discovered():
    return ashley.event_triggers_dict.get("porn_discovered", False)

def ashley_get_porn_discussed():
    return ashley.event_triggers_dict.get("porn_discussed", False)

def ashley_get_concert_overheard():
    return ashley.event_triggers_dict.get("concert_overheard", False)

def ashley_get_concert_date_stage():
    return ashley.event_triggers_dict.get("concert_date", 0)

def ashley_get_porn_convo_day():
    return ashley.event_triggers_dict.get("porn_convo_day", 9999)

def ashley_get_porn_convo_avail():
    return ashley.event_triggers_dict.get("porn_convo_avail", False)

def ashley_get_story_path():
    return ashley.event_triggers_dict.get("story_path", None)

def ashley_is_secret_path():
    return ashley.event_triggers_dict.get("story_path", None) == "secret"

def ashley_on_default_path():
    return stephanie.is_girlfriend and not ashley.is_girlfriend and stephanie == mc.business.head_researcher

def ashley_is_fwb_path():
    return ashley.event_triggers_dict.get("story_path", None) == "fwb"

def ashley_is_normal_path():
    return ashley.event_triggers_dict.get("story_path", None) == "normal"

def ashley_get_coffee_partner():
    return Person.get_person_by_identifier(ashley.event_triggers_dict.get("coffee_partner", None))

def ashley_set_coffee_partner(person: Person):
    ashley.event_triggers_dict["coffee_partner"] = person.identifier

def ashley_reset_coffee_partner():
    ashley.event_triggers_dict["coffee_partner"] = None

def ashley_set_observed_outfit(the_outfit):
    ashley.event_triggers_dict["observed_outfit"] = the_outfit.get_copy()

def ashley_get_observed_outfit():
    return ashley.event_triggers_dict.get("observed_outfit", None)

def ashley_second_date_complete():
    return ashley.event_triggers_dict.get("second_date_complete", None)

def ashley_sneaks_over_complete():
    return ashley.event_triggers_dict.get("sneaks_over_complete", False)

def ashley_caught_cheating_on_sister():
    return ashley.event_triggers_dict.get("caught_cheating", False)

def ashley_non_con_enabled():
    return ashley.event_triggers_dict.get("non_con", False)

def ashley_mc_submission_score():
    return ashley_get_mc_obedience() - (ashley.obedience - 80)
