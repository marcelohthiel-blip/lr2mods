from __future__ import annotations
import builtins
from game.major_game_classes.character_related.JobDefinition_ren import JobDefinition
from game.major_game_classes.character_related.Person_ren import Person, mc, aunt
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import Room, ceo_office, sex_store

day = 0

TIER_2_TIME_DELAY = 12
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

def add_aunt_cpa_side_job():
    if not aunt.has_job("CPA Consultant"):
        cpa_role = Role("CPA Consultant", get_CPA_role_actions(), on_turn = CPA_on_turn, on_day = CPA_on_day, hidden = True)
        cpa_job = JobDefinition("CPA Consultant", cpa_role, seniority_level = 3)
        aunt.set_side_job(cpa_job)

def add_aunt_cpa_job_for_business(location: Room):
    add_aunt_cpa_side_job()
    aunt.side_job.schedule.set_schedule(location, day_slots = [1], time_slots = [1, 2, 3])

def add_aunt_cpa_job_for_starbuck():
    add_aunt_cpa_side_job()
    aunt.side_job.schedule.set_schedule(sex_store, day_slots = [4], time_slots = [1])

def CPA_on_turn(the_person: Person):
    return True

def CPA_on_day(the_person: Person):
    if day % 7 == 1 and aunt.side_job.schedule.get_destination(1, 1) in (mc.business.m_div, ceo_office):
        mc.business.change_funds(-100, stat = "Consulting")
        discount = builtins.min((the_person.int + the_person.focus) * 15 * mc.business.research_tier, 200 * mc.business.research_tier)   #max 200 * mc.business.research_tier ($600)
        if mc.business.event_triggers_dict.get("CPA_upkeep_discount", 0) != discount:
            mc.business.operating_costs += mc.business.event_triggers_dict.get("CPA_upkeep_discount", 0)
            mc.business.operating_costs -= discount
            mc.business.event_triggers_dict["CPA_upkeep_discount"] = discount

        efficiency = builtins.min(the_person.charisma, 10)    #max 10%
        mc.business.event_triggers_dict["CPA_eff_bonus"] = efficiency

        mc.business.add_normal_message(f"Your CPA, {the_person.fname} worked today. You paid her $100 in consulting fees.")
        mc.business.add_normal_message(f"CPA Bonus, lowering daily operating costs by $ {discount:.0f} and increasing maximum business efficiency by {efficiency:.0f}%.")
    return True

def get_CPA_role_actions():
    return []
