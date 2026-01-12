from __future__ import annotations
import builtins
import renpy
from game.sex_positions.threesome.Threesome_Position_ren import willing_to_threesome
from game.people.Sarah.sarah_definition_ren import sarah_get_sex_unlocked
from game.people.Sarah.HR_supervisor_definition_ren import get_HR_director_tag
from game.people.Sarah.sarah_definition_ren import sarah_epic_tits_progress, sarah_get_special_titfuck_unlocked, sarah_threesomes_unlocked
from game.clothing_lists_ren import summer_dress, tiny_lace_panties, heels, thigh_highs, light_eye_shadow, lipstick, two_part_dress, fishnets, pumps, heavy_eye_shadow, tanktop, booty_shorts, short_socks, sneakers
from game.game_roles.stripclub._stripclub_role_definitions_ren import strip_club_is_closed
from game.business_policies.organisation_policies_ren import HR_director_creation_policy
from game.major_game_classes.game_logic.Room_ren import gym
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.character_related.Person_ren import Person, mc, sarah, lily, mom, starbuck, cousin, aunt, nora, ashley, ellie
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def alternative_hire_sarah_requirement(person: Person):
    return not mc.business.hr_director and HR_director_creation_policy.is_owned and person.event_triggers_dict.get("alt_hire", False)

def sarah_bar_date_ask_requirement(person: Person):
    if not sarah_get_sex_unlocked():
        return False
    if sarah.love < 30:
        return "Requires: 30 Love"
    if not mc.has_open_time_slot(3, day_restriction=(5,)):
        return "Already planned Saturday date!"
    return True

def get_sarah_role_actions():
    # give player one more chance to hire her as HR director
    alt_hire_action = Action("Hire her as HR Director", alternative_hire_sarah_requirement, "Sarah_alternative_hire_label")
    return [alt_hire_action]

def get_sarah_date_actions():
    sarah_bar_date_ask_action = Action("Ask her out to the bar", sarah_bar_date_ask_requirement, "sarah_bar_date_ask_label",
        menu_tooltip = "Plan a more serious date to the bar. Feed her a few drinks and see what happens!")
    return [sarah_bar_date_ask_action]

def init_sarah_roles():
    global sarah_role
    sarah_role = Role(role_name ="Childhood Friend", actions = get_sarah_role_actions(), role_dates = get_sarah_date_actions(), hidden = True)

def Sarah_remove_bra_from_wardrobe(wardrobe: Wardrobe):  #Test this function
    for outfit in wardrobe:
        outfit.remove_bra()

def Sarah_unlock_special_tit_fuck_requirement():  #Not an action, but make a requirement to make it easy to test anyway.
    return sarah.sex_record.get("Tit Fucks", 0) > 3 and not sarah_get_special_titfuck_unlocked()

def roll_dart_odds(target = 50, focus_score = 0):
    dart_roll = 0
    ran_num = renpy.random.randint(0, 100)
    if target == 50:
        if ran_num < (20 + (focus_score * 4)): #Bullseye!
            dart_roll = 50
        elif ran_num < (50 + (focus_score * 5)): #HIT
            dart_roll = 25
        else:
            dart_roll = renpy.random.randint(1, 20)
    elif target == 25:
        if ran_num < (40 + (focus_score * 4)): #HIT
            dart_roll = 25
        elif ran_num < (50 + (focus_score * 4)): #Bullseye!
            dart_roll = 50
        else:
            dart_roll = renpy.random.randint(1, 20)
    elif ran_num < (50 + (focus_score * 4)):
        dart_roll = target
    else:
        dart_roll = renpy.random.randint(1, 20)

    renpy.say(None, "The dart hits " + str(dart_roll) + "!")
    return dart_roll

def get_spend_the_night_threesome_possibility(person: Person):
    if sarah_threesomes_unlocked() and renpy.random.randint(0, 100) < 50:
        rnd = renpy.random.choice([0, 1])
        if rnd == 0:
            if willing_to_threesome(person, lily):
                return (True, lily)
            if willing_to_threesome(person, mom):
                return (True, mom)
        if rnd == 1:
            if willing_to_threesome(person, mom):
                return (True, mom)
            if willing_to_threesome(person, lily):
                return (True, lily)
    return (False, None)


def Sarah_watch_yoga_at_gym_requirement(person: Person):
    return person.sluttiness > 20 and person.is_at(gym)

def add_sarah_watch_yoga_at_gym_action():
    sarah.add_unique_on_room_enter_event(
        Action("Sarah does yoga",
            Sarah_watch_yoga_at_gym_requirement,
            "Sarah_watch_yoga_at_gym_label",
            priority = 30)
    )

def Sarah_get_drinks_requirement():
    if sarah_epic_tits_progress() == 1: #Don't run this if epic tits is in progress
        return False
    if time_of_day > 2 and day % 7 == 5 and sarah.sluttiness > 40 and sarah.love > 40:
        return sarah.is_available and mc.is_at_office and get_HR_director_tag("business_HR_sexy_meeting", False)
    return False

def add_sarah_get_drinks_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah get drinks", Sarah_get_drinks_requirement, "Sarah_get_drinks_label")
    )

def Sarah_stripclub_story_requirement():
    if sarah_epic_tits_progress() < 2 and sarah_epic_tits_progress() != -1:  #Don't run until after she has bigger tits of you convinced her not to do it
        return False
    if strip_club_is_closed(): # Don't run while strip club is closed
        return False
    #Only in the evening when the strippers are at the club
    if time_of_day > 2 and day % 7 == 5 and sarah.sluttiness > 50 and sarah.love >= 60:  #Saturday
        return sarah.is_available and mc.is_at_office
    return False

def add_sarah_stripclub_story_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah Strip Club", Sarah_stripclub_story_requirement, "Sarah_stripclub_story_label")
    )

def Sarah_hire_requirement(day_trigger):
    return day > day_trigger and HR_director_creation_policy.is_owned

def add_sarah_hire_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah hire", Sarah_hire_requirement, "Sarah_hire_label", requirement_args = day)
    )

def Sarah_new_tits_requirement():
    return time_of_day == 0 and day % 7 == 0

def add_sarah_new_tits_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah new tits", Sarah_new_tits_requirement, "Sarah_new_tits_label")
    )

def add_sarah_epic_tits_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah Epic Tits Action", Sarah_new_tits_requirement, "Sarah_epic_tits_label")
    )

def Sarah_workout_in_tshirt_requirement(person: Person):
    return person.sluttiness > 60 and person.is_at(gym)

def add_sarah_workout_in_tshirt_action():
    sarah.add_unique_on_room_enter_event(
        Action("Sarah works out",
            Sarah_workout_in_tshirt_requirement,
            "Sarah_workout_in_tshirt_label",
            priority = 30)
    )

def get_Sarah_willing_threesome_list():
    target_list = []
    if willing_to_threesome(sarah, mom):
        target_list.append(mom)
    if willing_to_threesome(sarah, lily):
        target_list.append(lily)
    if willing_to_threesome(sarah, starbuck):
        target_list.append(starbuck)
    if willing_to_threesome(sarah, cousin):
        target_list.append(cousin)
    if willing_to_threesome(sarah, aunt):
        target_list.append(aunt)
    if willing_to_threesome(sarah, nora):
        target_list.append(nora)
    for person in [x for x in mc.business.employees_availabe if x not in (sarah, ashley, ellie) and willing_to_threesome(sarah, x)]:
        if person not in target_list:
            target_list.append(person)

    return target_list

def Sarah_threesome_request_requirement():
    if time_of_day > 2 and day % 7 == 5 and sarah.sluttiness >= 80 and sarah.is_available and mc.is_at_office:
        # at least three choices for who to hook up with
        return builtins.len(get_Sarah_willing_threesome_list()) >= 3
    return False

def add_sarah_threesome_request_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah Threesome Request", Sarah_threesome_request_requirement, "Sarah_threesome_request_label")
    )

def Sarah_arrange_threesome_requirement(person: Person, the_day: int):
    return day > the_day

def add_sarah_arrange_threesome_action(person: Person):
    person.add_unique_on_talk_event(
        Action("Sarah_threesome_arrange",
            Sarah_arrange_threesome_requirement,
            "Sarah_arrange_threesome_label",
            requirement_args = day + 1,
            priority = 30)
    )

def Sarah_initial_threesome_requirement():
    return time_of_day > 2 and day % 7 == 5 and sarah.is_available

def add_sarah_initial_threesome_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah initial threesome", Sarah_initial_threesome_requirement, "Sarah_initial_threesome_label")
    )

def Sarah_fertile_period_start_requirement():  #When this returns true, start the fertile period
    if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
        return sarah.is_highly_fertile
    return False

def add_sarah_fertile_period_start_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah starts a fertile period", Sarah_fertile_period_start_requirement, "Sarah_fertile_period_start_label")
    )

def Sarah_fertile_period_end_requirement():     #When this returns true, end the fertile period
    if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
        return not sarah.is_highly_fertile
    return False

def add_sarah_fertile_period_end_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah ends a fertile period", Sarah_fertile_period_end_requirement, "Sarah_fertile_period_end_label")
    )

def Sarah_catch_stealing_requirement():
    if strip_club_is_closed(): #Don't run while the strip club is closed
        return False
    return day % 7 == 4 and time_of_day == 3 and sarah.is_available and not sarah.knows_pregnant and mc.is_at_office

def Sarah_third_wheel_requirement():
    if sarah_epic_tits_progress() == 1: #Don't run this if epic tits is in progress
        return False
    if day % 7 == 5 and time_of_day > 2 and sarah.sluttiness >= 20 and sarah.love >= 20:
        return sarah.is_available and mc.is_at_office
    return False

def add_sarah_catch_stealing_action():
    mc.business.add_mandatory_crisis(
        Action("Catch Sarah Stealing", Sarah_catch_stealing_requirement, "Sarah_catch_stealing_label")
    )

def add_sarah_third_wheel_action():
    mc.business.add_mandatory_crisis(
        Action("Sarah's third wheel event", Sarah_third_wheel_requirement, "Sarah_third_wheel_label")
    )


def get_sarah_date_outfit_one():
    outfit = Outfit("Sarah Date Outfit One")
    outfit.add_upper(summer_dress.get_copy(), [.95, .7, .87, .95])
    outfit.add_lower(tiny_lace_panties.get_copy(), [.95, .7, .87, .95])
    outfit.add_feet(heels.get_copy(), [.95, .7, .87, .95])
    outfit.add_feet(thigh_highs.get_copy(), [.95, .7, .87, .95])
    outfit.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .5])
    outfit.add_accessory(lipstick.get_copy(), [.745, .117, .235, .4])
    return outfit

def get_sarah_date_outfit_two():
    outfit = Outfit("Sarah Date Outfit Two")
    outfit.add_upper(two_part_dress.get_copy(), [.95, .7, .87, .95])
    outfit.add_feet(fishnets.get_copy(), [.95, .7, .87, .95])
    outfit.add_feet(pumps.get_copy(), [.95, .7, .87, .95])
    outfit.add_accessory(heavy_eye_shadow.get_copy(), [.1, .1, .12, .5])
    outfit.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .5])
    outfit.add_accessory(lipstick.get_copy(), [.745, .117, .235, .4])
    return outfit

def get_sarah_workout_event_outfit():
    outfit = Outfit("Sarah Workout Outfit")
    outfit.add_upper(tanktop.get_copy(), [1.0, 1.0, 1.0, 1.0])
    outfit.add_lower(booty_shorts.get_copy(), [.15, .15, .15, .95])
    outfit.add_feet(short_socks.get_copy(), [1.0, 1.0, 1.0, 1.0])
    outfit.add_feet(sneakers.get_copy(), [.71, .4, .85, 1.0], "Pattern_1", [1.0, 1.0, 1.0, 1.0])
    return outfit
