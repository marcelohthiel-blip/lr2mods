from __future__ import annotations
import copy
from game.map.map_code_ren import gaming_cafe_is_open
from game.major_game_classes.serum_related.serums.energy_drink_serum_ren import energy_drink_serum_trait
from game.major_game_classes.game_logic.Room_ren import gaming_cafe, mall, rd_division
from game.major_game_classes.character_related.Person_ren import Person, mc, myra, alexia
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.people.Myrabelle.myra_focus_training_definition_ren import myra_focus_progression_scene

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def gaming_cafe_owner_on_turn(person: Person):
    if gaming_cafe_is_open() and myra.is_at(gaming_cafe) and myra_has_exclusive_energy_drink():
        gaming_cafe_dose_customers()

def gaming_cafe_owner_on_day(person: Person):
    return

def init_myra_roles():
    global myra_role
    myra_role = Role(role_name ="Gaming Cafe Owner", hidden = True, on_turn = gaming_cafe_owner_on_turn, on_move = None, on_day = gaming_cafe_owner_on_day)

def myra_gaming_cafe_opening_requirement():
    # opening event triggers in weekend
    return day % 7 in (5, 6) and time_of_day in (2, 3) and myra.days_since_event("myra_rude_intro") >= TIER_2_TIME_DELAY and alexia.days_since_event("day_met") > TIER_1_TIME_DELAY

def add_myra_gaming_cafe_opening_action():
    mall.add_unique_on_room_enter_event(
        Action("Gaming Café Grand Opening", myra_gaming_cafe_opening_requirement, "myra_gaming_cafe_opening_label", priority = 30)
    )
    myra.set_event_day("myra_rude_intro")

def myra_develop_energy_drink_intro_requirement(person: Person):
    if person.sluttiness > 20 and gaming_cafe_is_open() and person.is_at(gaming_cafe) and myra_focus_progression_scene.get_stage() >= 1:    #Must have started focus training
        if myra.days_since_event("myra_sponsor_day") > TIER_2_TIME_DELAY:
            return mc.business.head_researcher is not None  # we need a head researcher for this quest line
    return False

def myra_energy_drink_research_intro_requirement(person: Person):
    return person == mc.business.head_researcher and person.is_at(rd_division)

def myra_energy_drink_research_final_requirement():
    if mc.business.head_researcher is not None and mc.business.head_researcher.is_at(rd_division):
        return mc.business.days_since_event("energy_drink_start_research") > TIER_2_TIME_DELAY
    return False

def myra_energy_drink_test_requirement(person: Person): # pylint: disable=unused-argument
    return gaming_cafe_is_open() and person.is_at(gaming_cafe) and myra_mc_has_acceptable_energy_serum()

def myra_energy_drink_distribution_intro_requirement(person: Person):
    return person.is_at_work

def myra_energy_drink_weekly_distribution_requirement():
    return time_of_day == 1 and day % 7 == 2 and myra_can_distribute_serum()

def add_myra_develop_energy_drink_intro_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Loves Energy Drinks", myra_develop_energy_drink_intro_requirement, "myra_develop_energy_drink_intro_label", priority = 30)
    )

def add_myra_energy_drink_research_intro_action():
    mc.business.head_researcher.add_unique_on_talk_event(
        Action("Develop an Energy Drink", myra_energy_drink_research_intro_requirement, "myra_energy_drink_research_intro_label", priority = 30)
    )

def add_myra_energy_drink_research_final_action():
    mc.business.add_mandatory_crisis(
        Action("New Serum Trait", myra_energy_drink_research_final_requirement, "myra_energy_drink_research_final_label", priority = 30)
    )
    mc.business.set_event_day("energy_drink_start_research")

def add_myra_energy_drink_test_action():
    myra.add_unique_on_talk_event(
        Action("Test Your Energy Drink", myra_energy_drink_test_requirement, "myra_energy_drink_test_label", priority = 30)
    )
    myra_unlock_energy_drink_serum()

def add_myra_energy_drink_distribution_intro(person: Person):
    myra.event_triggers_dict["energy_drink_supplier"] = person.identifier
    person.add_unique_on_room_enter_event(
        Action("Setup Distribution", myra_energy_drink_distribution_intro_requirement, "myra_energy_drink_distribution_intro_label", priority = 30)
    )

def add_myra_energy_drink_weekly_distribution():
    mc.business.add_mandatory_crisis(
        Action("Weekly Energy Drink Distribution", myra_energy_drink_weekly_distribution_requirement, "myra_energy_drink_weekly_distribution_label")
    )
    myra.event_triggers_dict["can_distribute_serum"] = True

# not yet hooked up
def myra_breeding_on_stream_requirement():
    return time_of_day == 3 and myra.has_breeding_fetish and myra.has_exhibition_fetish and myra.is_highly_fertile

def myra_will_grind_with_mc():
    return myra.event_triggers_dict.get("will_grind_with_mc", False)

def myra_plays_esports():
    return myra.event_triggers_dict.get("knows_plays_esports", False)

def myra_has_exclusive_energy_drink():
    return isinstance(myra_get_exclusive_energy_drink(), SerumDesign)

def myra_get_exclusive_energy_drink() -> SerumDesign | None:
    return myra.event_triggers_dict.get("weekly_serum", None)

def myra_can_train_focus() -> bool:
    return myra.event_triggers_dict.get("can_train_focus", False)

def myra_has_failed_tournament() -> bool:
    return myra.event_triggers_dict.get("has_failed_tournament", False)

def myra_can_sponsor() -> bool:
    return myra.event_triggers_dict.get("can_sponsor", False)

def myra_has_been_sponsored() -> bool:
    return myra.event_triggers_dict.get("has_been_sponsored", False)

def myra_has_won_tournament() -> bool:
    return myra.event_triggers_dict.get("has_won_tournament", False)

def myra_is_expanding_business() -> bool:
    return myra.event_triggers_dict.get("is_expanding_business", False)

def myra_can_distribute_serum() -> bool:
    return myra.event_triggers_dict.get("can_distribute_serum", False)

def bar_date_arcade_avail() -> bool:
    return myra.event_triggers_dict.get("bar_arcade_avail", False)

def myra_suggested_bigger_tits() -> bool:
    return myra.has_event_day("myra_bigger_tits_suggestion_day")

def myra_wants_bigger_tits() -> bool:
    return myra.event_triggers_dict.get("wants_bigger_tits", False)

def myra_knows_alexia_single() -> bool:
    return myra.event_triggers_dict.get("knows_alexia_single", False)

def myra_mc_bought_character() -> bool:
    return myra.event_triggers_dict.get("character_bought", False)

def myra_distracts_gamers() -> bool:
    return myra.event_triggers_dict.get("distracts_gamers", False)

def myra_caught_masturbating() -> bool:
    return myra.event_triggers_dict.get("lewd_game_oral", False)

def myra_lewd_game_fuck_avail() -> bool:
    return myra.event_triggers_dict.get("lewd_game_fuck", False)

def myra_started_blowjob_training() -> bool:
    return myra.event_triggers_dict.get("blowjob_train_start", False)

def myra_finish_blowjob_training() -> bool:
    return myra.event_triggers_dict.get("blowjob_train_finish", False)

def myra_deepthroat_avail() -> bool:
    return myra.event_triggers_dict.get("deepthroat_avail", False)

def myra_lewd_cafe_open() -> bool:
    return myra.event_triggers_dict.get("lewd_cafe_open", False)

def myra_mc_has_acceptable_energy_serum() -> bool:
    return mc.inventory.has_serum_with_trait(energy_drink_serum_trait)

def myra_serum_is_acceptable_energy_drink(serum: SerumDesign) -> bool:   #Make this a function so that as things progress we can loosen energy drink requirements.
    return serum.attention <= 3 and serum.has_trait(energy_drink_serum_trait)

def myra_set_weekly_serum(the_serum: SerumDesign):
    myra.event_triggers_dict["weekly_serum"] = None
    if isinstance(the_serum, SerumDesign):
        myra.event_triggers_dict["weekly_serum"] = copy.copy(the_serum)

def myra_unlock_energy_drink_serum():
    serum = next((x for x in list_of_traits if x.name == "Energy Drink"), None)
    serum.tier = 0
    serum.researched = True

def gaming_cafe_dose_customers():
    serum = myra_get_exclusive_energy_drink()
    if not isinstance(serum, SerumDesign):
        return
    count = 0
    for person in (x for x in gaming_cafe.people if x.active_serum_count < x.serum_tolerance):
        if not person.is_affected_by_serum(serum):
            person.give_serum(serum, add_to_log = False)
            count += 1
    mc.log_event(f"Myra distributed {count} energy drinks", "float_text_blue")
