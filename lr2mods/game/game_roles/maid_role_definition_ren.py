from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, naomi
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0
THREESOME_BASE_SLUT_REQ = 80
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def maid_on_move(person: Person):
    return

def maid_on_turn(person: Person):
    return

def maid_on_day(person: Person):
    return

def maid_slap_ass_requirement(person: Person):
    if not person.is_at_work:
        return False
    if person == naomi:
        return naomi.corruption_level > 0
    if person.obedience < 120:
        return "Requires: 120 Obedience"
    if person.spank_level > 4:
        return "Too recently spanked"
    return True

def maid_grope_requirement(person: Person):
    if not person.is_at_work:
        return False
    if person == naomi:
        return naomi.corruption_level > 1
    if person.obedience < 140:
        return "Requires: 140 Obedience"
    if person.love < 20:
        return "Requires: 20 Love"
    return True

def maid_service_requirement(person: Person):
    if not person.is_at_work:
        return False
    return False    # DISABLED FOR NOW
    if person == naomi:
        return naomi.corruption_level > 2
    if person.obedience < 160:
        return "Requires: 160 Obedience"
    if person.sluttiness < 40:
        return "Requires: 40 Sluttiness"
    return False


def get_maid_role_actions():
    maid_slap_ass_action = Action("Spank Her", maid_slap_ass_requirement, "maid_slap_ass_label")
    maid_grope_action = Action("Grope Her", maid_grope_requirement, "maid_grope_label")
    maid_service_action = Action("Service Me", maid_service_requirement, "maid_service_label")

    return [maid_slap_ass_action, maid_grope_action, maid_service_action]

def init_maid_role():
    global maid_role
    maid_role = Role("Maid", actions = get_maid_role_actions(),
        hidden = True, on_turn = maid_on_turn, on_move = maid_on_move, on_day = maid_on_day)

# maid knows her work locations by using set_schedule / remove_location
# then set her schedule (preferably using maid_job) to be in one of these locations
# she will automatically wear a maid outfit when she moves to the location and unlock actions.

# assign new maid job to person (with empty work schedule)
# can also be used as 'cleaning lady' or whatever work you want to assign the maid role
def assign_maid_job(person: Person, job_title = "Maid", is_primary = True, daily_wage: float = 20.0, start_day: int = -1):
    job = person.change_job(new_job = JobDefinition(job_title, maid_role, day_slots = [], time_slots = [], wardrobe = "Maid_Wardrobe", is_paid = True), is_primary = is_primary, start_day = start_day)
    job.salary = daily_wage
    return job
