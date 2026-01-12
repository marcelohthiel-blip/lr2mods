from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import rebuild_wardrobe
from game.people.Candace.candace_role_definition_ren import unlock_anti_bimbo_serum
from game.people.Candace.clothes_shopping_action_mod_ren import invite_to_clothes_shopping
from game.major_game_classes.game_logic.Room_ren import clothing_store
from game.major_game_classes.character_related.Person_ren import Person, mc, candace
from game.major_game_classes.game_logic.Action_ren import Action
from game.map.MapHub_ren import mall_hub

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def init_candance_story_lines():
    candace.event_triggers_dict["quit_job"] = 1
    # she has quit her job, give her a new wardrobe
    rebuild_wardrobe(candace, force = True)
    candace.set_override_schedule(None)
    add_candace_browsing_tinder_at_work_action(candace)
    add_candace_overhead_supply_order_action(candace)
    add_candace_goes_clothes_shopping_action(candace)
    candace.set_event_day("obedience_event")
    candace.set_event_day("love_event")
    candace.set_event_day("slut_event")
    candace.set_event_day("story_event")


# Love Events

def candace_goes_clothes_shopping_requirement(person: Person) -> bool:
    if person.love < 20 or not candace.story_event_ready("love"):
        return False
    return person.is_at_work

def add_candace_goes_clothes_shopping_action(person: Person):
    person.add_unique_on_talk_event(
        Action("Candi's Shopping", candace_goes_clothes_shopping_requirement, "candace_goes_clothes_shopping_label", priority = 30)
    )

def candace_goes_to_salon_requirement():
    return False

def add_candace_goes_to_salon_action():
    candace.event_triggers_dict["clothes_shopping"] = 1
    clothing_store.add_action(invite_to_clothes_shopping)
    mc.business.add_mandatory_crisis(
        Action("Candi's Spa Day", candace_goes_to_salon_requirement, "candace_goes_to_salon_label")
    )

def candace_karaoke_date_invite_requirement(person: Person):
    return False

def add_candace_karaoke_date_invite_action():
    # TODO: Write story
    #candace_karaoke_date_invite = Action("Candi's Date Request", candace_karaoke_date_invite_requirement, "candace_karaoke_date_invite_label")
    return

def candace_karaoke_date_requirement():
    return False

def add_candace_karaoke_date_action():
    # TODO: Write story
    # candace_karaoke_date = Action("Candi's Karaoke Date", candace_karaoke_date_requirement, "candace_karaoke_date_label")
    return

def candace_booty_call_requirement():
    return False

def add_candace_booty_call_action():
    # TODO: Write Story
    # candace_booty_call = Action("Candi's Booty Call", candace_booty_call_requirement, "candace_booty_call_label")
    return

# Obedience

def candace_browsing_tinder_at_work_requirement(person: Person):
    #120
    return person.is_at_office and person.obedience > 120 and person.primary_job.days_employed > 10

def add_candace_browsing_tinder_at_work_action(person: Person):
    # TODO: Write Story
    person.add_unique_on_room_enter_event(
        Action("Candi Browses Tinder", candace_browsing_tinder_at_work_requirement, "candace_browsing_tinder_at_work_label", priority = 30)
    )

def candace_topless_at_mall_requirement(person: Person):
    #140
    return person.obedience > 140 and person.is_at(mall_hub)

def add_candace_topless_at_mall_action():
    # TODO: Write Story
    candace.add_unique_on_room_enter_event(
        Action("Candi's Goes Topless", candace_topless_at_mall_requirement, "candace_topless_at_mall_label", priority = 30)
    )

def candace_sex_toy_in_public_requirement(person: Person):
    #160
    return False

def add_candace_sex_toy_in_public_action():
    # TODO: Write Story
    #candace_sex_toy_in_public = Action("Candi's Sex Toy", candace_sex_toy_in_public_requirement, "candace_sex_toy_in_public_label")
    return

def candace_sex_with_vendor_requirement():
    #180
    return False

def add_candace_sex_with_vendor__action():
    # TODO: Write Story
    #candace_sex_with_vendor = Action("Candi's Vendor Meetup", candace_sex_with_vendor_requirement, "candace_sex_with_vendor_label")
    return

# Lust Events
def candace_overhear_supply_order_requirement(person: Person) -> bool:
    return (time_of_day > 1
        and person.sluttiness > 40
        and candace.story_event_ready("lust")
        and person.is_at_office)

def add_candace_overhead_supply_order_action(person: Person):
    person.add_unique_on_talk_event(
        Action("Candi's Supply Order", candace_overhear_supply_order_requirement, "candace_overhear_supply_order_label", priority = 30)
    )


def candace_supply_order_discount_requirement() -> bool:
    return time_of_day == 1 and mc.is_at_office and mc.business.is_open_for_business

def add_candace_supply_order_discount_action():
    mc.business.add_mandatory_crisis(
        Action("Candi's Supply Discount", candace_supply_order_discount_requirement, "candace_supply_order_discount_label", priority = 30)
    )

def candace_sex_shop_trip_requirement(person: Person):
    return False

def add_candace_sex_shop_trip_action():
    # TODO: Write Story
    #candace_sex_shop_trip = Action("Candi in a Sex Store", candace_sex_shop_trip_requirement, "candace_sex_shop_trip_label")
    return

def candace_supply_leader_team_huddle_requirement():
    return False

def add_candace_supply_leader_team_huddle_action():
    # TODO: Write Story
    #candace_supply_leader_team_huddle = Action("Candi Trains the Girls", candace_supply_leader_team_huddle_requirement, "candace_supply_leader_team_huddle_label")
    return

# Other Events

def candace_uniform_complaint_requirement():
    return False

def add_candace_uniform_complaint_action():
    candace.event_triggers_dict["supply_discount"] = True
    mc.business.add_mandatory_crisis(
        Action("Candi Hates the Uniforms", candace_uniform_complaint_requirement, "candace_uniform_complaint_label")
    )

def candace_midnight_wakeup_requirement():
    return False

def add_candace_midnight_wakeup_action():
    mc.business.add_mandatory_crisis(
        Action("Candi Gets Arrested", candace_midnight_wakeup_requirement, "candace_midnight_wakeup_label")
    )

def candace_begin_cure_research_requirement(person: Person):
    return False

def add_candace_begin_cure_research_requirement():
    mc.business.head_researcher.add_unique_on_talk_event(
        Action("Cure for Candi", candace_begin_cure_research_requirement, "candace_begin_cure_research_label", priority = 30)
    )

def candace_anti_bimbo_serum_requirement():
    return False

def add_candace_anti_bimbo_serum_action(person: Person):
    candace.set_event_day("living_with_stephanie")
    candace.set_schedule(the_location = person.home, time_slots = [0, 4])
    mc.business.add_mandatory_crisis(
        Action("Bimbo Cure Progress", candace_anti_bimbo_serum_requirement, "candace_anti_bimbo_serum_label")
    )

def candace_cure_bimbo_requirement():
    return False

def add_candace_cure_bimbo_action():
    unlock_anti_bimbo_serum()
    mc.business.add_mandatory_crisis(
        Action("Bimbo Cure Serum", candace_cure_bimbo_requirement, "candace_cure_bimbo_label")
    )

def candace_meet_doctor_candace_requirement():
    return False

def add_candace_meet_doctor_candace_action():
    candace.event_triggers_dict["sex_record_snapshot"] = candace.sex_record.copy() #This should take a snapshot of our sex record with candace so we can compare it later
    candace.set_schedule(the_location = candace.home, time_slots = [0, 4])
    mc.business.add_mandatory_crisis(
        Action("Meet Doctor Candace", candace_meet_doctor_candace_requirement, "candace_meet_doctor_candace_label")
    )

def candace_get_sex_record_difference_tier() -> int: #Use this to determine what dialogue to run after curing her bimboism. Made a function because messy
    old_dict = candace.event_triggers_dict.get("sex_record_snapshot", None)
    if old_dict is None:
        return 0
    if old_dict["Vaginal Sex"] < candace.vaginal_sex_count or old_dict["Anal Sex"] < candace.anal_sex_count: #You fucked her at least once
        if old_dict["Vaginal Sex"] + old_dict["Anal Sex"] + 2 <= candace.vaginal_sex_count + candace.anal_sex_count: #Sex at least twice
            if old_dict["Vaginal Creampies"] + old_dict["Anal Creampies"] + 2 <= candace.vaginal_creampie_count + candace.anal_creampie_count:
                return 4
            return 3
        return 2
    if old_dict["Handjobs"] < candace.sex_record["Handjobs"] or old_dict["Blowjobs"] < candace.blowjob_count or old_dict["Cunnilingus"] < candace.sex_record["Cunnilingus"] or old_dict["Fingered"] < candace.sex_record["Fingered"]:
        return 1
    return 0

def candace_cleanup_snapshot():
    if "sex_record_snapshot" in candace.event_triggers_dict:
        del candace.event_triggers_dict["sex_record_snapshot"]
