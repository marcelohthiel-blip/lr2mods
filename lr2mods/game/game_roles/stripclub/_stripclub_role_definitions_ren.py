from __future__ import annotations
import renpy
from game.game_roles._role_definitions_ren import offer_to_hire_requirement, caged_role
from game.helper_functions.heart_formatting_functions_ren import get_gold_heart
from game.helper_functions.list_functions_ren import people_in_role
from game.major_game_classes.character_related.Person_ren import Person, mc, stripclub_stripper_job, stripclub_waitress_job, stripclub_bdsm_performer_job, stripclub_manager_job, aunt, cousin
from game.sex_positions._position_definitions_ren import blowjob, doggy, doggy_anal
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import strip_club, bdsm_room

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0
THREESOME_BASE_SLUT_REQ = 80
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def strip_club_get_manager() -> Person | None:
    managers = people_in_role(stripclub_manager_role)
    if managers:
        return managers[0]
    return None

def strip_club_get_mistress() -> Person | None:
    mistresses = people_in_role(stripclub_mistress_role)
    if mistresses:
        return mistresses[0]
    return None

def strip_club_has_manager_or_mistress() -> bool:
    return len(people_in_role([stripclub_manager_role, stripclub_mistress_role])) > 0

def bdsm_room_available() -> bool:
    return mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False)

def get_strip_club_foreclosed_stage():
    return mc.business.event_triggers_dict.get("foreclosed_stage", 0)

def set_strip_club_foreclosed_stage(value: int):
    mc.business.event_triggers_dict["foreclosed_last_action_day"] = day
    mc.business.event_triggers_dict["foreclosed_stage"] = value

def strip_club_is_closed():
    return strip_club.formal_name == "Foreclosed" or get_strip_club_foreclosed_stage() in (1, 2, 3, 4)

def stripclub_employee_on_turn(person: Person):
    return

def stripclub_employee_on_move(person: Person):
    if person.current_job and person.current_job.job_definition == stripclub_waitress_job and bdsm_room_available(): # waitresses sometimes work in bdsm_room
        if renpy.random.randint(0, 2) == 1:
            person.change_location(bdsm_room)
        else:
            person.change_location(strip_club)
    return

def stripclub_employee_on_day(person: Person):
    return

def stripper_private_dance_requirement(person: Person):
    if strip_club_is_closed() or not person.is_at(strip_club):
        return False
    if not mc.business.has_funds(100):
        return "Not enough cash."
    return True

def get_stripper_role_actions():
    stripper_dance_action = Action("Ask for a private dance\n{menu_red}Costs: $100{/menu_red}", stripper_private_dance_requirement, "stripper_private_dance_label",
        menu_tooltip = "Ask her to a back room for a private dance.")
    stripper_hire_action = Action("Offer to hire her at [mc.business.name]", offer_to_hire_requirement, "stripper_offer_hire")

    return [stripper_dance_action, stripper_hire_action]

def allow_promote_to_manager_requirement(person: Person):
    if not mc.owns_strip_club:
        return False
    if not person.is_at_work:
        return False
    if person in (aunt, cousin):
        return False # (aunt / cousin have own story line here)
    if strip_club_get_manager():
        return False # we already have a manager

    # detailed feedback
    if not person.is_primary_job((stripclub_stripper_job, stripclub_waitress_job, stripclub_bdsm_performer_job)):   # it's their secondary job
        return "Not her main job"
    if person.age < 25: # Restored age requirement, hire Gabrielle is handled by special event after hiring Rebecca
        return "Requires: age >= 25"
    if person.int < 4 or person.charisma < 5:
        return "Requires: intelligence >= 4 and charisma >= 5"
    if not mc.is_at_stripclub:
        return "Only in [strip_club.formal_name]"
    if day - person.event_triggers_dict.get("stripclub_hire_day", -7) < 7:
        return "Too recently hired"
    return True

def is_strip_club_stripper_requirement(person: Person):
    if not person.is_strip_club_employee or person.has_role(caged_role):
        return False
    if mc.owns_strip_club:
        if not person.is_at_work:
            return False
        if not mc.is_at_stripclub:
            return "Only in [strip_club.formal_name]"
        if person.has_role([stripper_role, stripclub_bdsm_performer_role, stripclub_waitress_role]):
            return True
    return False

def strip_club_review_requirement(person: Person):
    if not person.is_strip_club_employee or person.has_role(caged_role):
        return False
    if mc.owns_strip_club:
        if not person.is_at_work:
            return False
        if not mc.is_at_stripclub:
            return "Only in [strip_club.formal_name]"
        if person.current_job.days_employed < 7:
            return "Too recently hired"
        if person.has_event_day("stripclub_last_promotion_day") and person.days_since_event("stripclub_last_promotion_day") < 7:
            return "Too recently promoted"
        if person.has_event_day("day_last_performance_review") and person.days_since_event("day_last_performance_review") < 7:
            return "Too recently reviewed"
        return True
    return False

def strip_club_move_role_requirement(person: Person):
    if (len(mc.business.stripclub_strippers) >= 7
            and (not strip_club_has_manager_or_mistress() or len(mc.business.stripclub_waitresses) >= 4)
            and (not bdsm_room_available() or len(mc.business.stripclub_bdsm_performers) >= 5)):
        return "All positions filled"
    return strip_club_review_requirement(person)

def get_stripclub_base_actions() -> list[Action]:
    promote_to_manager_action = Action("Appoint as Manager", allow_promote_to_manager_requirement, "promote_to_manager_label", menu_tooltip = "Appoint [the_person.title] as strip club manager.")
    strip_club_stripper_fire_action = Action("Fire her", is_strip_club_stripper_requirement, "strip_club_fire_employee_label", menu_tooltip = "Fire [the_person.title] from her stripper job in your strip club.")
    strip_club_stripper_move_action = Action("Move to new role", strip_club_move_role_requirement, "strip_club_move_employee_label", menu_tooltip = "Move [the_person.title] to a different role within the strip club.")
    strip_club_stripper_performance_review_action = Action("Review her performance", strip_club_review_requirement, "stripper_performance_review_label", menu_tooltip = "Review [the_person.title]'s performances on stage.")

    return [promote_to_manager_action, strip_club_stripper_move_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action]

def strip_club_bdsm_dildochair_MC_requirements(person: Person) -> bool:
    return (
        not person.has_role(caged_role)
        and person.has_role(stripclub_bdsm_performer_role)
        and mc.is_at(bdsm_room)
    )

def strip_club_bdsm_dildochair_Mistress_requirements(person: Person) -> bool:
    return (
        strip_club_get_mistress() in mc.location.people
        and strip_club_bdsm_dildochair_MC_requirements(person)
    )

def get_stripclub_bdsm_performer_role_actions() -> list[Action]:
    strip_club_dildochair_MC_action = Action("Use the dildo chair {image=time_advance}", strip_club_bdsm_dildochair_MC_requirements, "strip_club_bdsm_dildochair_MC_label", menu_tooltip = "Use the dildo chair with your BDSM performer.")
    strip_club_dildochair_Mistress_action = Action("Mistress use the chair {image=time_advance}", strip_club_bdsm_dildochair_Mistress_requirements, "strip_club_bdsm_dildochair_Mistress_label", menu_tooltip = "Have the Mistress use the dildo chair with your BDSM performer.")

    return [strip_club_dildochair_MC_action, strip_club_dildochair_Mistress_action]

def has_manager_role_requirement(person: Person) -> bool | str:
    if not person.has_role(stripclub_manager_role) or not person.is_at_work:
        return False
    if not mc.is_at_stripclub:
        return "Only in [strip_club.formal_name]"
    return True

def allow_promote_to_mistress_requirement(person: Person) -> bool | str:
    if person.has_job(stripclub_manager_job) and bdsm_room_available() and not strip_club_get_mistress():
        if not person.is_at_work:
            return False
        if not mc.is_at_stripclub:
            return "Only in [strip_club.formal_name]"
        if person.has_event_day("stripclub_last_promotion_day") and person.days_since_event("stripclub_last_promotion_day") < 7:
            return "Too recently promoted"
        return True
    return False

def get_stripclub_manager_role_actions():
    manager_role_remove_action = Action("Remove as Manager", has_manager_role_requirement, "manager_role_remove_label", menu_tooltip = "Remove [the_person.title] as strip club manager.")
    promote_to_mistress_action = Action("Promote to Mistress", allow_promote_to_mistress_requirement, "promote_to_mistress_label", menu_tooltip = "Promote [the_person.title] as strip club mistress.")

    return [manager_role_remove_action, promote_to_mistress_action]

def has_mistress_role_requirement(person: Person):
    if person.has_role(stripclub_mistress_role):
        if not person.is_at_work:
            return False
        if not mc.is_at_stripclub:
            return "Only in [strip_club.formal_name]"
        return True
    return False

def mistress_hunt_for_me_requirement(person: Person) -> bool | str:
    if not person.has_role(stripclub_mistress_role) or not person.is_at_work:
        return False
    if not mc.is_at_stripclub:
        return "Only in [strip_club.formal_name]"
    if person.has_taboo("condomless_sex"):
        return f"Requires: unprotected sex with {person.name}"
    if person.has_taboo("sucking_cock"):
        return f"Requires: blowjob from {person.name}"
    if person.opinion.threesomes <= -2:
        return f"Requires: threesome experience {person.name}"
    minimum_sluttiness = THREESOME_BASE_SLUT_REQ + (person.opinion.threesomes * -5)
    if person.effective_sluttiness() < minimum_sluttiness:
        return f"Requires: {get_gold_heart(minimum_sluttiness)}"
    return True

def get_stripclub_mistress_role_actions() -> list[Action]:
    mistress_role_remove_action = Action("Remove as Mistress", has_mistress_role_requirement, "mistress_role_remove_label", menu_tooltip = "Remove [the_person.title] as strip club mistress.")
    mistress_hunt_for_me_action = Action("Hunt for me", mistress_hunt_for_me_requirement, "mistress_hunt_for_me_label", menu_tooltip = "Ask [the_person.title] to find you a girl for a threesome.")

    return [mistress_role_remove_action, mistress_hunt_for_me_action]

def get_bdsm_exhibitions(person: Person) -> int:
    return person.event_triggers_dict.get("exhibitions", 0)

def increase_bdsm_exhibitions(person: Person):
    person.event_triggers_dict["exhibitions"] = get_bdsm_exhibitions(person) + 1

def strip_club_get_caged():
    caged = people_in_role(caged_role)
    if caged:
        return caged[0]
    return None

def strip_club_cage_her_requirements(person: Person) -> bool:
    return (
        mc.is_at(bdsm_room)
        and not person.has_role(caged_role)
        and not people_in_role(caged_role)
    )

def strip_club_caged_strip_requirements(person: Person) -> bool:
    return (
        person.has_role(caged_role)
        and not (person.tits_visible and person.vagina_visible)
    )

def strip_club_caged_actions_milk_her_requirements(person: Person) -> bool | str:
    if not person.has_role(caged_role):
        return False
    if not person.is_lactating:
        return "Not lactating"
    if not person.tits_visible:
        return "Obstructed by Clothing"
    return True

def strip_club_caged_actions_blowjob_requirements(person: Person) -> bool | str:
    if not person.has_role(caged_role):
        return False
    if not person.is_willing(blowjob, False):
        return "Not willing to give blowjobs"
    return True

def strip_club_caged_actions_release_requirements(person: Person) -> bool:
    return person.has_role(caged_role)

def strip_club_caged_actions_sex_requirements(person: Person) -> bool | str:
    if not person.has_role(caged_role):
        return False
    if not person.is_willing(doggy, False):
        return "Not willing to have sex"
    if not person.vagina_available:
        return "Obstructed by Clothing"
    return True

def strip_club_caged_actions_anal_requirements(person: Person) -> bool | str:
    if not person.has_role(caged_role):
        return False
    if not person.is_willing(doggy_anal, False):
        return "Not willing to have anal sex"
    if not person.vagina_available:
        return "Obstructed by Clothing"
    return True

def add_strip_club_cage_her_action_to_mc_actions():
    strip_club_cage_her_action = Action("Cage her", strip_club_cage_her_requirements, "cage_her_label", menu_tooltip = "Put her in the cage.")
    mc.main_character_actions.add_action(strip_club_cage_her_action)

def strip_club_cage_role_on_turn(person: Person):
    return

def strip_club_cage_role_on_move(person: Person):
    person.change_location(bdsm_room)

def strip_club_cage_role_on_day(person: Person):
    person.clear_situational_slut("being_caged")
    person.clear_situational_obedience("being_caged")
    person.remove_role(caged_role)
    person.apply_planned_outfit()

def get_stripclub_caged_role_actions():
    caged_strip_action = Action(
        "Strip her",
        strip_club_caged_strip_requirements,
        "caged_strip_label",
        menu_tooltip="Strip the caged girl.",
    )
    caged_get_milked_action = Action(
        "Milk her",
        strip_club_caged_actions_milk_her_requirements,
        "caged_get_milked_label",
        menu_tooltip="Milk the caged girl.",
    )
    caged_BJ_action = Action(
        "Get a BJ from her",
        strip_club_caged_actions_blowjob_requirements,
        "caged_BJ_label",
        menu_tooltip="Get a BJ from the caged girl.",
    )
    caged_doggy_action = Action(
        "Fuck her Doggy style",
        strip_club_caged_actions_sex_requirements,
        "caged_doggy_label",
        menu_tooltip="Fuck the caged girl Doggy style.",
    )
    caged_anal_doggy_action = Action(
        "Fuck her anally",
        strip_club_caged_actions_anal_requirements,
        "caged_anal_doggy_label",
        menu_tooltip="Anal fuck the caged girl Doggy style.",
    )
    caged_release_action = Action(
        "Release her from the cage",
        strip_club_caged_actions_release_requirements,
        "caged_release_label",
        menu_tooltip="Release girl from the cage.",
    )
    return [
        caged_strip_action,
        #caged_get_milked_action,
        caged_BJ_action,
        caged_doggy_action,
        caged_anal_doggy_action,
        caged_release_action,
    ]


def init_strip_club_roles():
    global stripper_role
    stripper_role = Role("Stripper", get_stripper_role_actions(), hidden = True)

    global stripclub_stripper_role
    stripclub_stripper_role = Role("Stripper", get_stripper_role_actions() + get_stripclub_base_actions(),
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

    global stripclub_waitress_role
    stripclub_waitress_role = Role("Waitress", get_stripclub_base_actions(),
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

    global stripclub_bdsm_performer_role
    stripclub_bdsm_performer_role = Role("BDSM performer", get_stripclub_base_actions() + get_stripclub_bdsm_performer_role_actions(),
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

    global stripclub_manager_role
    stripclub_manager_role = Role("Manager", get_stripclub_manager_role_actions(),
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

    global stripclub_mistress_role
    stripclub_mistress_role = Role("Mistress", get_stripclub_mistress_role_actions(),
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

    global caged_role
    caged_role = Role("CAGED !", get_stripclub_caged_role_actions(),
        on_turn = strip_club_cage_role_on_turn, on_move = strip_club_cage_role_on_move, on_day = strip_club_cage_role_on_day, hidden = True)
