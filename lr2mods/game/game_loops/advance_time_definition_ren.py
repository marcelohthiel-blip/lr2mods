from __future__ import annotations
import renpy
import builtins
from game.fetish.fetish_action_ren import Fetish_Action
from game.helper_functions.random_generation_functions_ren import create_party_schedule
from game.helper_functions.list_functions_ren import find_in_set, get_random_from_list, unique_characters
from game.random_lists_ren import get_random_from_weighted_list
from game.bugfix_additions.ActionMod_ren import ActionMod, ActionList, crisis_list, morning_crisis_list, limited_time_event_pool
from game.main_character.perks.Perks_ren import perk_system
from game.main_character.mc_serum_trait_ren import MC_Serum_Trait
from game.major_game_classes.character_related.Appointment_ren import Appointment
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene
from game.major_game_classes.clothing_related.LimitedWardrobeCollection_ren import LimitedWardrobeCollection
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action
from game.major_game_classes.game_logic.Room_ren import downtown
from game.crises.regular_crises.crises_definition_ren import invest_opportunity_crisis_requirement

crisis_tracker_dict = {}
action_mod_list: list[ActionMod] = []
excluded_crisis_tracker_events = []
list_of_people: list[Person] = []
list_of_mc_traits: list[MC_Serum_Trait] = []
limited_wardrobes: LimitedWardrobeCollection = LimitedWardrobeCollection()
list_of_progression_scenes: list[Progression_Scene] = []
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
global mandatory_event
global crisis_chance
global morning_crisis_chance

global crisis_base_chance
global morning_crisis_base_chance

# some crisis events have impact on game dynamic and should be allowed to trigger often
mandatory_event = False
crisis_base_chance = 30
morning_crisis_base_chance = 15

crisis_chance = crisis_base_chance
morning_crisis_chance = morning_crisis_base_chance

def advance_time_next_requirement():
    return True

def advance_time_end_of_day_requirement():
    return time_of_day == 0

def advance_time_random_crisis_requirement():
    if time_of_day == 0:    # slot 0 is for morning crisis events
        return False
    if mandatory_event:
        return False        # already had a mandatory event, so no random event
    return renpy.random.randint(0, 100) < crisis_chance

# only trigger mandatory crisis events in timeslot 4 when in bedroom (actually end of day after pressing sleep button, required for dialogue consistency)
def advance_time_mandatory_crisis_requirement():
    return True

def advance_time_bankrupt_check_requirement():
    return time_of_day == 4

def advance_time_mandatory_morning_crisis_requirement():
    return time_of_day == 0

def advance_time_random_morning_crisis_requirement():
    if time_of_day != 0:
        return False
    if mandatory_event:
        return False        # already had a mandatory event, so no random event
    return renpy.random.randint(0, 100) < morning_crisis_chance

def advance_time_people_run_day_requirement():
    return time_of_day == 4

def advance_time_people_run_turn_requirement():
    return True

def advance_time_update_progression_scenes_requirement():
    return True

def jump_game_loop():
    # make sure we empty the call stack before jumping to main loop
    while renpy.call_stack_depth() > 1:
        renpy.pop_call()
    renpy.jump("game_loop")

def get_active_excluded_events() -> list[Action]:
    return [x for x in crisis_list.enabled_actions() + morning_crisis_list.enabled_actions() if x.effect in excluded_crisis_tracker_events]

def has_scheduled_date_in_crisis_list() -> tuple[bool, Appointment]:
    appointment = mc.schedule.get_appointment(day_slot = day % 7, time_of_day_slot = time_of_day)
    if appointment and appointment.is_date:
        if any(x for x in mc.business.mandatory_crises_list if x.effect == appointment.label):
            return True, appointment
    return False, None

def update_advance_time_action_list():
    global advance_time_action_list
    for adv_time_action in advance_time_action_list:
        if found := find_in_set(adv_time_action, ActionMod._instances):
            try:
                idx = action_mod_list.index(found)
                found.enabled = action_mod_list[idx].enabled

                # replace the one in the action_mod_list with the current action implementation from the instance list
                action_mod_list[idx] = found
            except ValueError:
                pass

    # update the advance_time_action_list with the instances in the action_mod_list
    advance_time_action_list = [x for x in action_mod_list if x in advance_time_action_list]
    # sort list on execution priority
    advance_time_action_list.sort(key = lambda x: x.priority)

advance_time_people_run_turn_action = ActionMod("Run people turn", advance_time_people_run_turn_requirement,
    "advance_time_people_run_turn_label", priority = 1, allow_disable = False)

advance_time_mandatory_crisis_action = ActionMod("Run mandatory crisis events", advance_time_mandatory_crisis_requirement,
    "advance_time_mandatory_crisis_label", priority = 2, category = "Gameplay", allow_disable = False)
advance_time_random_crisis_action = ActionMod("Run random crisis events", advance_time_random_crisis_requirement,
    "advance_time_random_crisis_label", priority = 3, category = "Gameplay")

advance_time_people_run_day_action = ActionMod("End of day run people", advance_time_people_run_day_requirement,
    "advance_time_people_run_day_label", priority = 4, allow_disable = False)

advance_time_next_action = ActionMod("Advances into the next time slot", advance_time_next_requirement,
    "advance_time_next_day_label", priority = 5, allow_disable = False)

advance_time_bankrupt_check_action = ActionMod("Bankruptcy check (Game Over)", advance_time_bankrupt_check_requirement,
    "advance_time_bankrupt_check_label", priority = 6, category = "Gameplay")

advance_time_end_of_day_action = ActionMod("End of day show summary", advance_time_end_of_day_requirement,
    "advance_time_end_of_day_label", priority = 7, allow_disable = False)

# People run move Actions
advance_time_people_run_move_action = ActionMod("Moves people to their destinations", advance_time_next_requirement,
    "advance_time_people_run_move_label", priority = 8, allow_disable = False)

advance_time_update_progression_scenes_action = ActionMod("Updates Progression Scenes", advance_time_update_progression_scenes_requirement,
    "advance_time_update_progression_scenes_label", priority = 9, allow_disable = False)

advance_time_mandatory_morning_crisis_action = ActionMod("Run mandatory morning crisis events", advance_time_mandatory_morning_crisis_requirement,
    "advance_time_mandatory_morning_crisis_label", priority = 10, category = "Gameplay", allow_disable = False)

advance_time_random_morning_crisis_action = ActionMod("Run random morning crisis events", advance_time_random_morning_crisis_requirement,
    "advance_time_random_morning_crisis_label", priority = 11, category = "Gameplay")

advance_time_action_list = [advance_time_people_run_turn_action, advance_time_people_run_day_action, advance_time_end_of_day_action, advance_time_next_action, advance_time_mandatory_crisis_action,
    advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action,
    advance_time_people_run_move_action, advance_time_bankrupt_check_action, advance_time_update_progression_scenes_action]

# sort list on execution priority
advance_time_action_list.sort(key = lambda x: x.priority)

# actions that trigger events
advance_time_event_action_list = [advance_time_mandatory_crisis_action, advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action]

def update_crisis_tracker(active_crisis_list) -> None:
    for crisis in (x for x in active_crisis_list if x.effect not in excluded_crisis_tracker_events and x.effect not in crisis_tracker_dict):
        crisis_tracker_dict[crisis.effect] = 0

def get_sorted_active_and_filtered_mandatory_crisis_list(crisis_list: ActionList):
    has_fetish = False
    active_crisis_list: list[Action] = []
    for crisis in sorted(crisis_list.enabled_actions(), key = lambda x: x.priority, reverse = True):
        if not has_fetish and isinstance(crisis, Fetish_Action):
            active_crisis_list.append(crisis)
            has_fetish = True
        else:
            active_crisis_list.append(crisis)
    return active_crisis_list

def find_next_crisis(active_crisis_list):
    update_crisis_tracker(active_crisis_list)

    # special handling for when low on funds, investment opportunity triggers
    if not mc.business.has_funds(300) and invest_opportunity_crisis_requirement():
        crisis = next((x for x in active_crisis_list if x.effect == "invest_opportunity_crisis_label"), None)
        if crisis:
            return crisis

    # special handling for unlocking the unisex bathroom quest line faster (last stage should unlock around day 140)
    unisex_level = mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0)
    if unisex_level > 0 and unisex_level < 6 and day > 20 + unisex_level * 10:
        crisis = next((x for x in active_crisis_list if x.effect == "unisex_restroom_action_label"), None)
        if crisis:
            return crisis

    # special handling for mall introductions during weekends (prioritize while we have unknown people in the mall)
    if mc.business.is_weekend:
        crisis = next((x for x in active_crisis_list if x.effect == "mall_introduction_action_label"), None)
        if crisis:
            return crisis

    # append excluded events to list
    active_excluded_events = get_active_excluded_events()

    # get active events from crisis_tracker_dict (only those with lowest counter)
    tracker_info = {key: value for (key, value) in crisis_tracker_dict.items() if key in (x.effect for x in active_crisis_list)}
    key_list = [] # sometimes tracker_info is empty, to prevent error only choose from active_excluded_events
    if tracker_info.items():
        min_value = builtins.min(tracker_info.items(), key=lambda x: x[1])[1]
        average = builtins.int(builtins.sum(x[1] for x in tracker_info.items()) / len(tracker_info.items()))
        key_list = [key for (key, value) in tracker_info.items() if value == min_value]

    # add active events from exclusion list to possible events list
    if builtins.len(key_list) == 0 or builtins.len(key_list) > builtins.len(active_excluded_events):
        # when the key_list is getting smaller we are exhausting the possible crisis events
        # if we keep adding the excluded items, they will start to occur more and more frequent (>50%)
        # so we don't add them anymore, until we are back to a more comprehensive list of events
        key_list.extend((x.effect for x in active_excluded_events))

    random_crisis = get_random_from_list(key_list)
    # renpy.say(None, "Run Crisis [" + str(builtins.len(key_list)) +"]: " + random_crisis)
    if random_crisis in crisis_tracker_dict:
        crisis_tracker_dict[random_crisis] = average + 1     # set to min_value +1 to prevent the event from triggering a lot (its count maybe low due to being disabled)
    return next((x for x in active_crisis_list + active_excluded_events if x.effect == random_crisis), None)

def get_crisis_from_crisis_list() -> Action:
    return find_next_crisis(crisis_list.enabled_actions())

def get_limited_time_action_for_person(person) -> Action:
    return get_random_from_weighted_list([(x, x.priority) for x in limited_time_event_pool.enabled_actions(person)])

def get_morning_crisis_from_crisis_list() -> Action:
    return find_next_crisis(morning_crisis_list.enabled_actions())

def update_party_schedules():
    # exclude unique characters as to not to interfere with story lines
    for person in (x for x in list_of_people if x not in unique_characters()):
        create_party_schedule(person)
    return

def clear_follow_mc_flag():
    for person in (x for x in list_of_people if x.follow_mc):
        person.follow_mc = False

def apply_mc_serum_traits():
    for trait in list_of_mc_traits:
        if trait.is_active:   #Re apply traits Daily
            trait.remove_trait()
        if trait.is_selected:
            trait.apply_trait()

def advance_time_run_turn():
    for person in list_of_people: #Run the results of list_of_people spending their turn in their current location.
        person.run_turn()

    mc.business.run_turn()
    for project in mc.business.active_IT_projects:
        project.on_turn()
    mc.run_turn()
    perk_system.update()

def advance_time_run_day():
    mc.run_day()
    mc.business.run_day()

    for person in list_of_people:
        person.run_day()

    for project in mc.business.active_IT_projects:
        project.on_day()

    apply_mc_serum_traits()

    for wardrobe in limited_wardrobes:
        wardrobe.clear()

def advance_time_run_move():
    mc.business.run_move()
    for project in mc.business.active_IT_projects:
        project.on_move()

    for person in list_of_people: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
        person.run_move()

def advance_time_assign_limited_time_events():
    for person in (x for x in list_of_people if not x.is_stranger):
        if renpy.random.randint(0, 100) < 10: #Only assign one to 10% of people, to cut down on the number of people we're checking.
            crisis = get_limited_time_action_for_person(person)
            if crisis:
                if crisis.trigger == "on_talk" and crisis not in person.on_talk_event_list:
                    person.add_unique_on_talk_event(Limited_Time_Action(crisis))
                elif crisis.trigger == "on_enter" and crisis not in person.on_room_enter_event_list:
                    person.add_unique_on_room_enter_event(Limited_Time_Action(crisis))

def advance_time_check_location_accessibility():
    hub = mc.current_location_hub
    if not mc.location.is_accessible or not hub.is_accessible:
        if not mc.location.is_accessible:
            location_name = mc.location.formal_name
        else:
            location_name = hub.formal_name
        renpy.say(None, f"The {location_name} is closing, so you decide to take a walk downtown.")
        mc.change_location(downtown)

def advance_time_update_progression_scenes():
    for x in list_of_progression_scenes:
        x.update()
