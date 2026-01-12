from __future__ import annotations
import renpy
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import aunt_apartment, aunt_bedroom, cousin_bedroom, hall, lily_bedroom
from game.major_game_classes.character_related.Person_ren import Person, mc, aunt, cousin, mom
from game.major_game_classes.character_related.scene_manager_ren import Scene
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.people.Rebecca.aunt_events_ren import add_aunt_accounting_intro_action, add_aunt_first_date_tips_action
from game.people.Rebecca.aunt_definition_ren import aunt_unemployed_job

TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def aunt_intro_moving_apartment_requirement(person: Person):
    if person.event_triggers_dict.get("moving_apartment", -1) >= 0:
        if person.event_triggers_dict.get("moving_apartment", 0) >= 4:
            return "Everything has already been moved"
        if time_of_day == 0:
            return "Too early to start moving"
        if time_of_day == 4:
            return "Too late to start moving"
        if person.event_triggers_dict.get("day_of_last_move", -1) == day:
            return "Already moved today"
        return True
    return False

def aunt_share_drinks_requirement(person: Person):
    if not person.event_triggers_dict.get("invited_for_drinks", False):
        return False
    if not person.is_at(aunt_apartment):
        return False
    if time_of_day < 3:
        return "Too early for drinks"
    if time_of_day > 3:
        return "Too late for drinks"
    return True

def aunt_offer_hire_requirement(person: Person):
    if not person.has_job(aunt_unemployed_job):
        return False
    if not person.has_event_day("moved_out"):
        return False
    if person.love < 10 or person.is_sleeping:
        return False
    if person.love < 20:
        return "Requires: 20 Love"
    if mc.business.at_employee_limit:
        return "At employee limit"
    return True

def get_aunt_role_actions():
    #AUNT ACTIONS#
    aunt_help_move = Action("Help her move into her apartment {image=time_advance}", aunt_intro_moving_apartment_requirement, "aunt_intro_moving_apartment_label",
        menu_tooltip = "Help your aunt and your cousin move their stuff from your house to their new apartment. They're sure to be grateful, and it would give you a chance to snoop around.", priority = 5)

    aunt_share_drinks_action = Action("Share a glass of wine {image=time_advance}", aunt_share_drinks_requirement, "aunt_share_drinks_label",
        menu_tooltip = "Sit down with your aunt and share a glass or two of wine. Maybe a little bit of alcohol will loosen her up a bit.", priority = 10)

    #aunt_offer_hire_action = Action("Offer to hire her at [mc.business.name]", aunt_offer_hire_requirement, "aunt_offer_hire", priority = -5)
    return [aunt_help_move, aunt_share_drinks_action]

def init_aunt_roles():
    global aunt_role
    aunt_role = Role("Aunt", get_aunt_role_actions(), hidden = True)

def aunt_move_to_new_apartment():
    aunt.event_triggers_dict["moving_apartment"] = -1 #Disables the event in their action list so you can't help them move out once they're already moved out.

    aunt.set_event_day("moved_out")
    cousin.set_event_day("moved_out")

    aunt_bedroom.visible = True
    aunt_apartment.visible = True
    cousin_bedroom.visible = True

    #Your aunt is a homebody, but your cousin goes wandering during the day (Eventually to be replaced with going to class sometimes.)
    aunt.set_schedule(aunt.home, time_slots = [0, 1, 4])
    aunt.set_schedule(aunt_apartment, time_slots = [2, 3])

    cousin.set_schedule(cousin.home, time_slots = [0, 4])
    cousin.set_schedule(None, time_slots = [1, 2, 3])

    add_cousin_at_house_phase_one_action()
    add_aunt_share_drink_intro()

    add_aunt_accounting_intro_action()
    add_aunt_first_date_tips_action()

    aunt.change_location(aunt.home)
    cousin.change_location(cousin.home)


def family_games_night_setup_requirement():
    return day % 7 == 2 and time_of_day == 3

def family_games_night_requirement(the_mom: Person, the_aunt: Person):
    return (day % 7 == 2
        and time_of_day == 4
        and the_mom.is_at(hall)
        and the_aunt.is_at(hall))

def init_family_games_night():
    mc.business.add_mandatory_crisis(
        Action("Family games night setup", family_games_night_setup_requirement, "family_games_night_setup")
    )

    mom.add_unique_on_room_enter_event(
        Limited_Time_Action(
            Action("Family games night", family_games_night_requirement, "family_games_night_start",
                args = [aunt], requirement_args = [aunt], event_duration = 2))
    )

def setup_family_game_night():
    if mom.get_destination(time_slot = 4) in (mom.home, None, hall) and aunt.get_destination(time_slot = 4) in (aunt.home, None, hall): #Change their schedule if they aren't explicitly suppose to be somewhere else.
        mom.set_schedule(hall, day_slots = 2, time_slots = 4) #She is in the hall on wednesdays in the evening.
        aunt.set_schedule(hall, day_slots = 2, time_slots = 4) #She is in the hall on wednesdays in the evening.

    elif mom.get_destination(time_slot = 4) == hall: #She's in the hall but her sister can't make it.
        mom.set_schedule(mom.home, day_slots = 2, time_slots = 4)

    elif aunt.get_destination(time_slot = 4) == hall: #She's in the hall but her sister can't make it.
        aunt.set_schedule(aunt.home, day_slots = 2, time_slots = 4)

    if not mc.business.event_triggers_dict.get("family_games_setup_complete", False):
        mc.business.event_triggers_dict["family_games_drink"] = 0
        mc.business.event_triggers_dict["family_games_cards"] = 0
        mc.business.event_triggers_dict["family_games_fun"] = 0
        mc.business.event_triggers_dict["family_games_cash"] = 0
        mc.business.event_triggers_dict["family_games_strip"] = 0
        mc.business.event_triggers_dict["family_games_setup_complete"] = True

    init_family_games_night() #Re-add the event for next week.

def family_game_night_get_opponents_with_info(opponents: list[Person], partner: Person):
    opponents.remove(partner)
    win_chance = 50 + mc.int + mc.focus + partner.int + partner.focus - sum(x.int for x in opponents) - sum(x.focus for x in opponents)
    return (opponents[0], opponents[1], win_chance)

def family_game_night_strip_description(person: Person, cloth: Clothing, scene_manager: Scene):
    test_outfit = person.outfit.get_copy()
    test_outfit.remove_clothing(cloth)
    if test_outfit.tits_visible and not person.tits_visible:
        if person.has_taboo("bare_tits"):
            renpy.say(None, f"{person.title} glances around the table nervously.")
            renpy.say(person.char, "Maybe we should call it here?")
            renpy.say(mc.name, f"Relax {person.fname}, it's just a game! Come on, get those tits out for us.")
            renpy.say(None, f"{person.possessive_title.capitalize()} hesitates, and the other girls start to cheer her on.")
            renpy.say(person.char, "Okay, okay...")

        scene_manager.update_actor(person, position = "stand3")
        scene_manager.draw_animated_removal(person, cloth)
        if person.has_large_tits:
            renpy.say(None, f"{person.title} pulls off her {cloth.display_name}. Her large breasts jiggle briefly as they're released.")
        else:
            renpy.say(None, f"{person.title} pulls off her {cloth.display_name}, setting her tits free.")

        if person.has_taboo("bare_tits"):
            renpy.say(None, f"{person.title} tries to keep her breasts covered with her hands, cheeks red.")
            person.break_taboo("bare_tits")

    elif test_outfit.vagina_visible and not person.vagina_visible:
        if person.has_taboo("bare_pussy"):
            renpy.say(None, f"{person.title} starts to move her {cloth.display_name}, but hesitates.")
            renpy.say(person.char, "Maybe we've taken this far enough...")
            renpy.say(mc.name, f"Come on {person.fname}, you can't quit now. We're all family here, nobody cares.")
            renpy.say(None, "The rest of the table cheers her on. She takes a deep breath and gathers her courage.")

        scene_manager.update_actor(person, position = "stand3")
        scene_manager.draw_animated_removal(person, cloth)
        renpy.say(None, f"{person.title} pulls her {cloth.display_name} down, peeling them away from her pussy.") # We should probably check if they're actually underwear, but I'm happy enough with this.

        if person.has_taboo("bare_pussy"):
            renpy.say(None, f"With her {cloth.display_name} off, {person.title} sits back down quickly, blushing a fierce red.")
            person.break_taboo("bare_pussy")

    elif person.has_taboo("underwear_nudity") and test_outfit.underwear_visible and not person.underwear_visible:
        renpy.say(None, f"{person.title} glances nervously around the table.")
        renpy.say(person.char, f"You don't really want me to take off my {cloth.display_name}, do you? I'll just have my underwear on...")
        renpy.say(mc.name, f"Come on {person.fname}, that's the whole point of the game! Nobody cares about you just wearing your underwear.")
        renpy.say(None, "She bites her lip as she considers it, then takes a deep breath.")

        scene_manager.update_actor(person, position = "stand3")
        scene_manager.draw_animated_removal(person, cloth)

        renpy.say(None, f"{person.title} pulls off her {cloth.display_name} and drops it beside her chair.")
        renpy.say(person.char, "There, I did it.")
        person.break_taboo("underwear_nudity")

    else: #She's just stripping, and it's not really important
        scene_manager.update_actor(person, position = "stand3")
        scene_manager.draw_animated_removal(person, cloth)

        renpy.say(None, f"{person.title} takes her {cloth.display_name} off, putting it down beside her chair.")

    #TODO: See about streamlining that by rolling it all into a single strip based description thing (we're doing a lot of strip dialogue lately)

    person.update_outfit_taboos() #Make sure we update all taboos, in case two were broken at once.
    mc.change_locked_clarity(10)
    scene_manager.update_actor(person, position = "sitting")

    return #TODO: Have this return something special so we can tell if any of the girls should comment.


def aunt_intro_phase_two_requirement(): #Always triggers the day after the initial intro event
    return True

def add_aunt_intro_phase_two_action():
    aunt.set_event_day("obedience_event")
    aunt.set_event_day("love_event")
    aunt.set_event_day("slut_event")
    aunt.set_event_day("story_event")
    aunt.progress.love_step = 0
    aunt.progress.lust_step = 0
    aunt.progress.obedience_step = 0
    aunt.primary_job.job_known = True
    cousin.primary_job.job_known = True

    mc.business.add_mandatory_morning_crisis(
        Action("Aunt introduction phase two", aunt_intro_phase_two_requirement, "aunt_intro_phase_two_label")
    ) #Aunt and cousin will be visiting tomorrow in the morning

def cousin_aunt_hire_reaction_requirement(person: Person):
    #NOTE: This is an event sitting on the cousin, not the aunt
    return True

def add_cousin_aunt_hire_reaction_action():
    cousin.add_unique_on_talk_event(
        Action("hire_reaction", cousin_aunt_hire_reaction_requirement, "cousin_aunt_hire_reaction", priority = 30)
    )


def aunt_intro_phase_three_requirement(day_trigger):
    return day >= day_trigger

def add_aunt_phase_three_action():
    aunt.change_location(hall)
    aunt.set_schedule(hall, time_slots = [0, 1, 2, 3, 4])
    aunt.set_event_day("arrival")
    mc.business.add_mandatory_morning_crisis(
        Action("aunt_intro_phase_three", aunt_intro_phase_three_requirement, "aunt_intro_phase_three_label", requirement_args = day + renpy.random.randint(18, 24))
    )

def cousin_intro_phase_one_requirement(day_trigger):
    return day >= day_trigger and time_of_day == 4

def add_cousin_phase_one_action():
    cousin.change_location(lily_bedroom)
    cousin.set_schedule(lily_bedroom, time_slots = [0, 4])
    cousin.set_schedule(None, time_slots = [1, 2, 3])
    mc.business.add_mandatory_crisis(
        Action("cousin_intro_phase_one", cousin_intro_phase_one_requirement, "cousin_intro_phase_one_label", requirement_args = day + renpy.random.randint(2, 5))
    )

def aunt_intro_phase_five_requirement(day_trigger):
    return day >= day_trigger and day % 7 != 5

def add_aunt_moving_action():
    aunt.event_triggers_dict["moving_apartment"] = 0 #If it's a number it's the number of times you've helped her move. If it doesn't exist or is negative the event isn't enabled
    mc.business.add_mandatory_morning_crisis(
        Action("Moving finished", aunt_intro_phase_five_requirement, "aunt_intro_phase_final_label", requirement_args = day + 7)
    )

def cousin_house_phase_one_requirement(day_trigger):
    return day >= day_trigger

def add_cousin_at_house_phase_one_action():
    mc.business.add_mandatory_crisis(
        Action("Cousin changes schedule", cousin_house_phase_one_requirement, "cousin_house_phase_one_label", args = cousin, requirement_args = day + renpy.random.randint(2, 5))
    ) #This event changes the cousin's schedule so she shows up at your house.

def aunt_drink_intro_requirement(person: Person):
    return time_of_day == 3 and person.is_at(aunt_apartment)

def add_aunt_share_drink_intro():
    aunt.add_unique_on_talk_event(
        Action("Aunt drink intro", aunt_drink_intro_requirement, "aunt_share_drink_intro_label", priority = 30)
    )
