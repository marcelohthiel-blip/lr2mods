# Each punishment is an Action.
# The requirements should return the required severity if they would otherwise be unlocked, otherwise they are hidden.
# Note: Some punishments take place over a duration of time. We need to implement those in some way; maybe a Role.

#5 levels of punishment. Each one will have 3 different options: 1 always available, 1 made available with corporal punishment, and 1 made available with another policy.

# Level 1 (Trivial infraction; Arrived slightly late, minor work mistake)
# A) Verbal scolding
# B) Wrist Slap (hand)
# C) Free Serum Testing (Rec: Paid serum testing)

# Level 2 (Minor infraction; uniform non-compliance, under performing work)
# A) Office busy work (ie. coffee girl, personal secretary)
# B) Spanking (Clothed, maybe skirt up)
# C) Office underwear (Req: Some uniform policy)

# Level 3 (Moderate infraction; out of uniform, direct disobedience)
# A) Pay cut
# B) Strip and Spank
# C) Office nudity (Req: Some uniform policy)

# Level 4 (Major infraction; )
# A) Humiliating office work (ie. scrubbing floors, cleaning bathrooms)
# B) Orgasm denial
# C) Forced punishment outfit (Req: Some uniform policy)

# Level 5 (Tremendous infraction; corporate espionage, intentional sabotage)
# A) Unpaid intern
# B) Office Free Use

from __future__ import annotations
from game.game_roles.business_roles._business_role_definitions_ren import mc, employee_busywork_role, employee_humiliating_work_role, employee_freeuse_role
from game.business_policies.clothing_policies_ren import relaxed_uniform_policy, reduced_coverage_uniform_policy
from game.business_policies.organisation_policies_ren import corporal_punishment
from game.business_policies.serum_policies_ren import mandatory_paid_serum_testing_policy
from game.major_game_classes.business_related.Infraction_ren import Infraction
from game.major_game_classes.character_related.Person_ren import Person, Outfit, Role, ActiveJob
from game.major_game_classes.game_logic.ActionList_ren import ActionList, Action

day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_punishments = ActionList() #Establish a central holder for punishments. Mods can add additional punishments to this list.


# LEVEL 1 #

def punishment_verbal_scolding_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 1: #In theory not possible, but future events may reduce the effective severity of infractions and it keeps everyting looking similar
        return "Severity 1"
    return True

def punishment_wrist_slap_requirement(person: Person, the_infraction: Infraction):
    if not corporal_punishment.is_active:
        return "Requires Policy: Corporal Punishment"
    if the_infraction.severity < 1:
        return "Severity 1"
    return True

def punishment_serum_test_requirement(person: Person, the_infraction: Infraction):
    if not mandatory_paid_serum_testing_policy.is_active:
        return "Requires Policy: Mandatory Paid Serum Testing"
    if the_infraction.severity < 1:
        return "Severity 1"
    if not mc.inventory.has_serum:
        return "Requires: Serum in inventory"
    return True

punishment_verbal_scolding_action = Action("Verbal scolding", punishment_verbal_scolding_requirement, "punishment_verbal_scolding")
punishment_wrist_slap_action = Action("Wrist slaps", punishment_wrist_slap_requirement, "punishment_wrist_slap")
punishment_serum_test_action = Action("Test serum", punishment_serum_test_requirement, "punishment_serum_test")

list_of_punishments.append(punishment_verbal_scolding_action)
list_of_punishments.append(punishment_wrist_slap_action)
list_of_punishments.append(punishment_serum_test_action)


# LEVEL 2 #
def punishment_office_busywork_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 2:
        return "Severity 2"
    if person.has_role(employee_busywork_role):
        return "Already performing office busywork"
    if person.has_role(employee_humiliating_work_role):
        return "Already performing humiliating work"
    return True

def punishment_spank_requirement(person: Person, the_infraction: Infraction):
    if not corporal_punishment.is_active:
        return "Requires Policy: Corporal Punishment"
    if the_infraction.severity < 2:
        return "Severity 2"
    return True

def punishment_underwear_only_requirement(person: Person, the_infraction: Infraction):
    if not relaxed_uniform_policy.is_active:
        return "Requires: Relaxed Corporate Uniforms Policy"
    if the_infraction.severity < 2:
        return "Severity 2"
    if person.current_job and person.current_job.forced_uniform:
        return "Already has a forced uniform"
    if person.vagina_visible and person.tits_visible:
        return "Already naked"
    if person.are_panties_visible and person.is_bra_visible:
        return "Already in her underwear"
    return True

def employee_busywork_remove_requirement(trigger_day: int) -> bool:
    return day >= trigger_day

def add_office_busywork_action(person: Person):
    person.add_role(employee_busywork_role)
    clear_action = Action("Clear employee busywork", employee_busywork_remove_requirement, "employee_busywork_remove_label", args = person, requirement_args = [day + 7])
    mc.business.add_mandatory_crisis(clear_action)


punishment_office_busywork_action = Action("Office Busywork", punishment_office_busywork_requirement, "punishment_office_busywork")
punishment_spank_action = Action("Spanking", punishment_spank_requirement, "punishment_spank")
punishment_underwear_only_action = Action("Underwear only", punishment_underwear_only_requirement, "punishment_underwear_only") #Note: Actually level 2, move it

list_of_punishments.append(punishment_office_busywork_action)
list_of_punishments.append(punishment_spank_action)
list_of_punishments.append(punishment_underwear_only_action)

# LEVEL 3 #
def punishment_pay_cut_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 3:
        return "Severity 3"
    if not person.current_job or person.current_job.salary <= 0:
        return "Requires: Paid Position"
    return True

def punishment_strip_and_spank_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 3:
        return "Severity 3"
    if not corporal_punishment.is_active:
        return "Requires Policy: Corporal Punishment"
    return True

def punishment_office_nudity_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 3:
        return "Severity 3"
    if not reduced_coverage_uniform_policy.is_active:
        return f"Requires Policy: {reduced_coverage_uniform_policy.name}"
    if person.current_job and person.current_job.forced_uniform:
        return "Already has a forced uniform"
    return True

punishment_pay_cut_action = Action("Pay cut", punishment_pay_cut_requirement, "punishment_pay_cut")
punishment_strip_and_spank_action = Action("Strip and Spank", punishment_strip_and_spank_requirement, "punishment_strip_and_spank")
punishment_office_nudity_action = Action("Mandatory Nudity", punishment_office_nudity_requirement, "punishment_office_nudity")

list_of_punishments.append(punishment_pay_cut_action)
list_of_punishments.append(punishment_strip_and_spank_action)
list_of_punishments.append(punishment_office_nudity_action)


# LEVEL 4 #
def punishment_office_humiliating_work_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 4:
        return "Severity 4"
    if person.has_role(employee_busywork_role):
        return "Already performing office busywork"
    if person.has_role(employee_humiliating_work_role):
        return "Already performing humiliating work"
    return True

def punishment_orgasm_denial_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 4:
        return "Severity 4"
    if not corporal_punishment.is_active:
        return "Requires Policy: Corporal Punishment"
    return True

def punishment_forced_punishment_outfit_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 4:
        return "Severity 4"
    if not reduced_coverage_uniform_policy.is_active:
        return f"Requires Policy: {reduced_coverage_uniform_policy.name}"
    if person.current_job and person.current_job.forced_uniform:
        return "Already has a forced uniform"
    return True

def employee_humiliating_work_remove_requirement(trigger_day: int) -> bool:
    return day >= trigger_day

def add_humiliating_work_action(person: Person):
    person.add_role(employee_humiliating_work_role)
    clear_action = Action("Clear employee humiliating work", employee_humiliating_work_remove_requirement, "employee_humiliating_work_remove_label", args = person, requirement_args = [day + 7])
    mc.business.add_mandatory_crisis(clear_action)

punishment_office_humiliating_work_action = Action("Humiliating Office Work", punishment_office_humiliating_work_requirement, "punishment_office_humiliating_work")
punishment_orgasm_denial_action = Action("Orgasm Denial", punishment_orgasm_denial_requirement, "punishment_orgasm_denial")
punishment_forced_punishment_outfit_action = Action("Punishment Outfit", punishment_forced_punishment_outfit_requirement, "punishment_forced_punishment_outfit")

list_of_punishments.append(punishment_office_humiliating_work_action)
list_of_punishments.append(punishment_orgasm_denial_action)
list_of_punishments.append(punishment_forced_punishment_outfit_action)


# LEVEL 5 #
def punishment_unpaid_intern_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 5:
        return "Severity 5"
    if not person.current_job or person.current_job.salary <= 0:
        return "Requires: Paid Position"
    return True

def punishment_freeuse_slut_requirement(person: Person, the_infraction: Infraction):
    if the_infraction.severity < 5:
        return "Severity 5"
    if person.has_role(employee_freeuse_role):
        return "Already a free use slut"
    if person.is_free_use:
        return "She is a slut by nature"
    if not corporal_punishment.is_active:
        return "Requires Policy: Corporal Punishment"
    if person.has_taboo("vaginal_sex"):
        return "Requires: Had vaginal sex with MC"
    return True

def employee_freeuse_remove_requirement(trigger_day: int) -> bool:
    return day >= trigger_day

def add_freeuse_role_and_clear_punishment_action(person: Person, outfit: Outfit | None = None) -> None:
    person.add_role(employee_freeuse_role)

    # create a freeuse outfit
    if outfit is None:
        outfit = person.decide_on_outfit(.2)
        person.personalize_outfit(outfit, allow_skimpy = True)
        outfit.make_easier_access()
        outfit.remove_bra_and_panties()

    person.current_job.forced_uniform = outfit

    clear_action = Action("Clear employee freeuse", employee_freeuse_remove_requirement, "employee_freeuse_remove_label", args = person, requirement_args = [day + (5 - day % 7)])
    mc.business.add_mandatory_crisis(clear_action)

def employee_unpaid_intern_remove_requirement(trigger_day: int) -> bool:
    return day >= trigger_day

def add_unpaid_intern_clear_punishment_action(job: ActiveJob, restore_amount: float):
    clear_action = Action("Clear employee freeuse", employee_freeuse_remove_requirement, "employee_unpaid_remove_label", args = [job, restore_amount], requirement_args = [day + 7])
    mc.business.add_mandatory_crisis(clear_action)

punishment_unpaid_intern_action = Action("Unpaid Internship", punishment_unpaid_intern_requirement, "punishment_unpaid_intern")
punishment_orgasm_denial_action = Action("Freeuse Office Slut", punishment_freeuse_slut_requirement, "punishment_office_freeuse_slut")

list_of_punishments.append(punishment_unpaid_intern_action)
list_of_punishments.append(punishment_orgasm_denial_action)

# SPECIAL MC PUNISHMENTS

def punishment_service_mc_requirement(person: Person, the_infraction):
    if the_infraction.severity < 3:
        return "Severity 3"
    if not corporal_punishment.is_active:
        return "Requires Policy: Corporal Punishment"
    return True

def employee_cocksucking_practice_remove_requirement(trigger_day):
    return day >= trigger_day

def employee_cocksucking_practice_report_requirement():
    return mc.business.is_open_for_business and mc.is_at_office

employee_practice_cocksucking_work_role = Role("Practising Cocksucking", [], hidden = True)

# Practice adding a time gated work discipline.
def add_practice_cocksucking_work_action(person: Person):
    if person.has_role(employee_practice_cocksucking_work_role): # prevent adding it twice
        return
    person.add_role(employee_practice_cocksucking_work_role)
    clear_action = Action("Clear employee cocksucking practice", employee_cocksucking_practice_remove_requirement, "employee_cocksucking_practice_remove_label", args = person, requirement_args = [day + 7])
    mc.business.add_mandatory_crisis(clear_action)

def add_practice_cocksucking_report_action(person: Person):
    if person.has_role(employee_practice_cocksucking_work_role):
        person.remove_role(employee_practice_cocksucking_work_role, remove_linked = False)

    if person.is_employee: #She may have quit/been fired since then.
        person.sex_skills["Oral"] = min(4, person.oral_sex_skill + 1)

        if person.opinion.giving_blowjobs <= -2:
            person.update_opinion_with_score("giving blowjobs", -1, add_to_log = False)  #Set this to -1 if it was -2 so that she at least tries to give MC a blowjob.

        practice_cocksucking_report_action = Action("Cocksucking practice report crisis", employee_cocksucking_practice_report_requirement, "employee_cocksucking_practice_report_label", args = person)
        mc.business.add_mandatory_crisis(practice_cocksucking_report_action)

punishment_service_mc_action = Action("Service Me", punishment_service_mc_requirement, "punishment_service_mc_label")

list_of_punishments.append(punishment_service_mc_action)
