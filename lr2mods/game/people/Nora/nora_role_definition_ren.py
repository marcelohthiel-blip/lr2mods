from __future__ import annotations
import builtins
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.game_logic.Room_ren import university
from game.game_roles._role_definitions_ren import very_heavy_trance_role
from game.major_game_classes.character_related.Person_ren import Person, mc, nora, mom, lily, aunt, cousin
from game.major_game_classes.serum_related.serums._nora_serum_traits_ren import nora_reward_aunt_trait, nora_reward_cousin_trait, nora_reward_genius_trait, nora_reward_high_love_trait, nora_reward_high_slut_trait, nora_reward_hucow_trait, nora_reward_instant_trance, nora_reward_low_love_trait, nora_reward_mother_trait, nora_reward_sister_trait, nora_reward_nora_trait, nora_reward_high_obedience_trait
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits, list_of_nora_traits
from game.major_game_classes.game_logic.Action_ren import Action
from game.people.Nora.nora_place_progression_scene_definition_ren import nora_place_prog_scene_action_req

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

def nora_student_exam_rewrite_request_requirement(person: Person):
    if not person.event_triggers_dict.get("student_exam_ready", False):
        return False
    if not person.is_at(university):
        return "Better wait until she's working."
    return True

def add_student_rewrite_exam_action():
    nora.add_action(
        Action("Ask her about the exam rewrite",
            nora_student_exam_rewrite_request_requirement,
            "nora_student_exam_rewrite_request",
            menu_tooltip = "Ask if she can set up a new exam for your student.")
    )
    nora.event_triggers_dict["student_exam_ready"] = True #unlock flag

def remove_student_rewrite_exam_action():
    nora.remove_action("nora_student_exam_rewrite_request")

def start_nora_trait_research():
    trait = get_random_from_list(list_of_nora_traits)
    trait.researched = True
    mc.business.event_triggers_dict["nora_trait_researched"] = trait
    list_of_traits.append(trait)

def complete_nora_initial_research():
    mc.business.research_tier = 2
    mc.business.set_event_day("T2_unlock_day")
    mc.log_event("Tier 2 Research Unlocked", "float_text_grey")

    university.remove_action("nora_research_up_label")
    trait = mc.business.event_triggers_dict.get("nora_trait_researched")
    mc.business.event_triggers_dict["nora_trait_researched"] = None
    mc.business.event_triggers_dict["nora_cash_reintro_needed"] = False
    list_of_traits.remove(trait)
    list_of_nora_traits.remove(trait)


def nora_clear_current_cash_trait():
    trait = mc.business.event_triggers_dict.get("nora_cash_research_trait") #We know won't be None from our initial event check.
    mc.business.event_triggers_dict["nora_cash_research_trait"] = None

    list_of_traits.remove(trait)
    list_of_nora_traits.remove(trait) #Clear it from Nora's list as well so it cannot be randomly obtained again.

def add_new_nora_cash_trait_for_research():
    trait = get_random_from_list(list_of_nora_traits)
    if trait:
        trait.researched = True
        mc.business.event_triggers_dict["nora_cash_research_trait"] = trait
        list_of_traits.append(trait)

def get_nora_research_subject():
    subject = mc.business.event_triggers_dict.get("nora_research_subject", None)
    return Person.get_person_by_identifier(subject)


def has_nora_trait_info(person: Person):
    if person == mom and person.sluttiness > 75 and person.love > 75 and nora_reward_mother_trait not in list_of_traits:
        return True
    if person == lily and person.sluttiness > 75 and person.obedience > 150 and nora_reward_sister_trait not in list_of_traits:
        return True
    if person == cousin and person.sluttiness > 75 and person.love < -25 and nora_reward_cousin_trait not in list_of_traits:
        return True
    if person == aunt and person.sluttiness > 75 and nora_reward_aunt_trait not in list_of_traits:
        return True
    if person == nora and person.sluttiness > 75 and nora_reward_nora_trait not in list_of_traits:
        return True
    if person.is_pregnant and person.pregnancy_is_visible and person.sluttiness > 75 and nora_reward_hucow_trait not in list_of_traits:
        return True
    if person.love > 85 and nora_reward_high_love_trait not in list_of_traits:
        return True
    if person.love < -50 and nora_reward_low_love_trait not in list_of_traits:
        return True
    if person.obedience > 180 and nora_reward_high_obedience_trait not in list_of_traits:
        return True
    if person.sluttiness > 95 and nora_reward_high_slut_trait not in list_of_traits:
        return True
    if person.int >= 7 and person.charisma >= 7 and person.focus >= 7 and nora_reward_genius_trait not in list_of_traits:
        return True
    if person.has_exact_role(very_heavy_trance_role) and nora_reward_instant_trance not in list_of_traits:
        return True
    return False

def nora_traits_left():
    nora_traits = [nora_reward_mother_trait, nora_reward_sister_trait, nora_reward_cousin_trait, nora_reward_aunt_trait, nora_reward_nora_trait, nora_reward_high_love_trait, nora_reward_low_love_trait, nora_reward_high_obedience_trait, nora_reward_high_slut_trait, nora_reward_genius_trait, nora_reward_instant_trance]
    if persistent.pregnancy_pref != 0:
        nora_traits.append(nora_reward_hucow_trait)

    return len(list(set(nora_traits) - set(list_of_traits)))


def nora_research_up_requirement():
    if mc.business.research_tier != 1 or mc.business.event_triggers_dict.get("nora_trait_researched", None) is None:
        return False
    if time_of_day == 0:
        return "Too early to visit [nora.title]"
    if time_of_day == 4:
        return "Too late to visit [nora.title]"
    if not nora.is_at(university):
        return "[nora.title] does not work now"
    if builtins.round(mc.business.event_triggers_dict.get("nora_trait_researched").mastery_level, 1) < 2:
        trait_name = mc.business.event_triggers_dict.get("nora_trait_researched").name
        return "Requires: " + trait_name + " Mastery >= 2"
    return True

def add_nora_university_research_actions():
    university.add_action(
        Action("Present your research to [nora.title]", nora_research_up_requirement, "nora_research_up_label", args = nora,
        menu_tooltip = "Deliver your field research to [nora.title] in exchange for her theoretical research notes.")
    )
    add_visit_nora_lab_action(nora)


def study_person_requirement(person: Person):
    if nora_traits_left() == 0:
        return False
    if not has_nora_trait_info(person):
        return "No interesting properties"
    if time_of_day == 4:
        return "Not enough time"
    return True

def special_research_requirement(person: Person):
    if get_nora_research_subject() is None and nora_traits_left() == 0:
        return False
    if get_nora_research_subject() is None:
        return "No new research to turn in"
    if time_of_day == 0:
        return "Too early to visit [nora.title]"
    if time_of_day == 4:
        return "Too late to visit [nora.title]"
    if not nora.get_destination() is university:
        return "[nora.title] does not work now"
    return True

def add_study_person_for_nora_actions(the_person):
    mc.main_character_actions.add_action(
        Action("Study her for Nora {image=time_advance}", study_person_requirement, "nora_profile_person", is_fast = False,
        menu_tooltip = "Work through the research questionnaire provided to you by Nora. After you can give it to Nora to see if she notices any interesting properties.")
    )
    university.add_action(
        Action("Turn in a research questionnaire", special_research_requirement, "nora_special_research", args = the_person, requirement_args = the_person,
        menu_tooltip = "Turn in the research questionnaire you had filled out. If the person is particularly unique or extreme she may be able to discover unique serum traits for you to research.")
    )


def nora_research_cash_intro_requirement(person: Person, min_day):
    return time_of_day in (2, 3) and day > min_day and mc.business.is_open_for_business and mc.business.research_tier >= 2

def add_nora_research_intro_action(person: Person, did_research: bool):
    mc.business.remove_mandatory_crisis("nora_research_cash_intro") # remove existing cash intro from character creation
    mc.business.add_mandatory_crisis(
        Action("Nora cash research intro", nora_research_cash_intro_requirement, "nora_research_cash_intro", args = [person, did_research], requirement_args = [person, day + renpy.random.randint(3, 6)])
    )

def nora_research_cash_requirement(person: Person):
    if mc.business.event_triggers_dict.get("nora_cash_research_trait", None) is None:
        return False
    if time_of_day == 0:
        return "Too early to visit [nora.title]"
    if time_of_day == 4:
        return "Too late to visit [nora.title]"
    if not nora.is_at(university):
        return "[nora.title] does not work now"
    if builtins.round(mc.business.event_triggers_dict.get("nora_cash_research_trait").mastery_level, 1) < 2:
        trait_name = mc.business.event_triggers_dict.get("nora_cash_research_trait").name
        return "Requires: " + trait_name + " Mastery >= 2"
    return True

def add_nora_research_cash_action(person: Person):
    mc.business.event_triggers_dict["nora_cash_research_trigger"] = False #Reset this trigger so the event is hidden properly again in the future (TODO: Just remove it from the list)
    university.add_action(
        Action("Turn in your finished research", nora_research_cash_requirement, "nora_research_cash", args = person, requirement_args = person,
        menu_tooltip = "Turn in your completed trait research to Nora, in exchange for payment.")
    )

def visit_lab_intro_requirement(person: Person):
    if mc.business.research_tier <= 1:
        return False
    if mc.business.event_triggers_dict.get("nora_trait_researched", None) is None and not mc.business.event_triggers_dict.get("nora_cash_research_trigger", False):
        return False
    if time_of_day == 0:
        return "Too early to talk to [nora.title] about business"
    if time_of_day == 4:
        return "Too late to talk to [nora.title] about business"
    if not nora.is_at(university):
        return "[nora.title] does not work now"
    return True

def add_visit_nora_lab_action(person: Person):
    # if university.visible:            University starts available now
    #     return
    university.add_action(
        Action("Visit Nora's lab", visit_lab_intro_requirement, "nora_research_cash_first_time", args = nora, requirement_args = nora,
            menu_tooltip = "Visit your old lab and talk to Nora about serum research.")
    ) #Prepare this so if we visit the university again under the proper conditions we can start studying traits for her for money.

    nora.set_override_schedule(None)
    nora.set_schedule(university, day_slots = [0, 1, 2, 3, 4], time_slots =[1, 2, 3])
    nora.set_schedule(university, day_slots = [5], time_slots =[1, 2])
    university.visible = True

def nora_unlock_interns_program_requirement(person: Person, start_day: int):
    return (day > start_day
        and mc.business.has_funds(25000)
        and person.is_at(university)
        and mc.business.hr_director)  # we need HR director for unlock

def add_nora_unlock_interns_program():
    nora.add_unique_on_room_enter_event(Action("Start Intern Program", nora_unlock_interns_program_requirement,
        "nora_unlock_interns_program_label", requirement_args = day + TIER_3_TIME_DELAY, priority = 30))

def hire_new_college_intern_requirement(person):
    if not person.is_at_work:
        return False
    if not mc.business.has_funds(15000):
        return "$15,000 scholarship fund"
    if len(mc.business.get_intern_depts_with_openings()) > 0:
        return True
    return "No internship openings"

def unlock_recruit_new_college_interns():
    nora.add_action(
        Action("Hire new intern {image=time_advance}",
            hire_new_college_intern_requirement,
            "hire_new_college_intern_label")
    )

def unlock_nora_place_prog_scene():
    nora.add_action(
        Action("Have fun with her {image=gui/heart/Time_Advance.png}",
               nora_place_prog_scene_action_req,
               "nora_have_fun_with_her_action_label")
    )
