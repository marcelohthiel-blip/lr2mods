#GIRLFRIEND ACTIONS#
# Give her gifts (bonus happiness + Love)
# She tests serum for you for free.
# Go on dates (Remove this option from the normal chat menu?)
# If she has (of age) kids, meet them (and, amazingly, they're hot young women!)

#Other things to add#
# Enables new girlfriend specific crises.
# Adds more love to seduction attempts (reduce love from other sources)
# Fallout if your girlfriend catches you with someone else.


#Getting married is some kind of victory for the game?


#affair ACTIONS
# Sneaky versions of all of the normal girlfriend stuff
# Have her get money from her (b/f/h) and give it to you.
# Convince her to leave her (boyfriend/fiance/husband) for you. Changes to her being your girlfriend.
# Start to blackmail her for money or sex.

from __future__ import annotations
import renpy
from game.clothing_lists_ren import pube_styles
from game.helper_functions.list_functions_ren import get_random_from_list
from game.map.map_code_ren import mall_is_open
from game.game_roles._role_definitions_ren import sister_role, mother_role, dikdok_role
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import harem_mansion
from game.major_game_classes.character_related.Person_ren import Person, mc, kaya, sakari
from game.major_game_classes.clothing_related.Clothing_ren import Clothing

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
# special list for girlfriend morning actions
girlfriend_sleepover_interruption_list: list[Action] = []     #Ideas, daughter/mother walk in, phone call,
#girlfriend_roleplay_list : List[Action] = []                   #When a roleplay is created, add it here as an option. list of ACTIONS

def init_relationship_roles():
    global girlfriend_role
    girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates(), on_day = girlfriend_role_on_day) #Your girlfriend, and she's not in a relationship with anyone else
    global harem_role
    harem_role = Role("Girlfriend in Polyamory", get_harem_role_actions(), role_dates = get_harem_role_dates(), looks_like = girlfriend_role)
    global affair_role
    affair_role = Role("Paramour", get_paramour_role_actions(), role_dates = get_paramour_role_dates()) #A woman who is in a relationship but also wants to fuck you because of love (rather than pure sluttiness, where she thinks that's normal)

def ask_girlfriend_requirement(person: Person):
    if person.has_relation_with_mc:
        return False
    if person.has_role(sister_role) and person.event_triggers_dict.get("sister_girlfriend_waiting_for_blessing", False):
        return False
    if person.has_role(mother_role) and person.event_triggers_dict.get("mom_girlfriend_waiting_for_blessing", False):
        return False
    if person.love < 30:
        return False
    if person.love < 60:
        return "Requires: 60 Love"
    return True #But note that there are still failure conditions in the actual event, but those lead to hints about what to do to stop it.

def ask_break_up_requirement(person: Person):
    return True

def ask_get_boobjob_requirement(person: Person):
    if person.sluttiness < (40 - person.opinion.showing_her_tits * 5):
        return False
    if person.knows_pregnant:
        return "Not while pregnant"
    obedience_required = 130 - (person.opinion.showing_her_tits * 5)
    if person.obedience < obedience_required:
        return f"Requires: {obedience_required} Obedience"
    if person.event_triggers_dict.get("getting boobjob", False):
        return "Boobjob already scheduled"
    if person.tits == Person.get_larger_tit(person.tits):
        return "At maximum size"
    return True

def girlfriend_ask_trim_pubes_requirement(person: Person):
    obedience_required = 125 - (5 * person.opinion.being_submissive)
    if person.sluttiness < 30:
        return False
    if person.obedience < 110:
        return False
    if person.obedience < obedience_required:
        return f"Requires: {obedience_required} Obedience"
    return True

def girlfriend_myplace_yourplace_requirement(person: Person):
    if (person == kaya and person.home == sakari.home):  # exclude Kaya story wise
        return False
    if schedule_sleepover_available():
        if time_of_day < 4:
            return True
        return "Too Late"
    return "You already have a sleepover arranged"

def girlfriend_unplanned_sleepover_requirement(person: Person):
    # any GF can have a sleepover
    # exclude Kaya story wise
    return time_of_day == 4 and mc.is_at(person.home) and (person != kaya or person.home != sakari.home)

def girlfriend_underwear_shopping_requirement(person: Person):
    if person.love < 80 and person.sluttiness < 40:
        return False
    if not mall_is_open():
        return "Clothes store closed"
    if person.is_at_work:
        return "Ask her when she's not working"
    if not mc.business.has_funds(500):
        return "Requires: $500"
    return True

def girlfriend_quit_dikdok_requirement(person: Person):
    if not person.has_role(dikdok_role):
        return False
    if person.love < 40: # hide option will love is very low
        return False
    if person.love < 60:
        return "Requires: 60 Love"
    return True

def get_girlfriend_role_actions():
    ask_break_up_action = Action("Break up with her", ask_break_up_requirement, "ask_break_up_label", menu_tooltip = "Breaking up may break her heart, but it'll be easier on her than catching you with another woman.")
    ask_get_boobjob_action = Action("Ask her to get a boob job\n{menu_red}Costs: $7000{/menu_red}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
    girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
    girlfriend_sleepover_action = Action("Arrange a sleepover", girlfriend_myplace_yourplace_requirement, "girlfriend_myplace_yourplace_label", menu_tooltip = "Ask your girlfriend if she wants to sleep together tonight.")
    girlfriend_unplanned_sleepover_action = Action("Spend the night", girlfriend_unplanned_sleepover_requirement, "girlfriend_unplanned_sleepover_label", menu_tooltip = "Tell your girlfriend you want to spend the night with her.")
    girlfriend_underwear_shopping_action = Action("Shop for new lingerie {image=time_advance}", girlfriend_underwear_shopping_requirement, "girlfriend_underwear_shopping_label", menu_tooltip = "Take your girlfriend out to shop for some exciting underwear to wear for you.")
    girlfriend_quit_dikdok_action = Action("Quit DikDok", girlfriend_quit_dikdok_requirement, "girlfriend_quit_dikdok_label", menu_tooltip = "Ask your girlfriend to stop showing herself off on DikDok.")

    return [ask_break_up_action, ask_get_boobjob_action, girlfriend_ask_trim_pubes_action, girlfriend_sleepover_action, girlfriend_unplanned_sleepover_action, girlfriend_underwear_shopping_action, girlfriend_quit_dikdok_action]

def girlfriend_role_on_day(person: Person):
    if day % 4 == 0:
        person.change_baby_desire(1)
    return

def fuck_date_requirement(person: Person):
    if (person == kaya and person.home == sakari.home):  # exclude Kaya story wise
        return False
    if not mc.has_open_time_slot(time_slot = 4, day_restriction=(2, 3, 4)):
        return "Already planned dates!"
    if person.is_girlfriend and person.effective_sluttiness() < 60:
        return "Requires: 60 Sluttiness"
    return True

def shopping_date_requirement(person: Person):
    if time_of_day == 0:
        return "Too early to go shopping."
    if time_of_day >= 4:
        return "Too late to go shopping."
    if person.has_event_day("last_shopping_day") and person.days_since_event("last_shopping_day") < 5:
        return f"Wait another {6 - person.days_since_event('last_shopping_day')} days"
    return True

def get_girlfriend_role_dates():
    plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = 'Pick a night to go over there and spend nothing but "quality time" with each other.')
    girlfriend_shopping_date = Action("Go shopping together {image=time_advance}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
    return [plan_fuck_date_action, girlfriend_shopping_date]

def harem_move_to_mansion_requirement(person: Person):
    if person.home == harem_mansion:    # already in mansion
        return False
    if not mc.has_harem_mansion: # mansion not build
        return False
    if person.is_affair: # she needs to leave her SO
        return "Requires: Single"
    return True

def harem_break_up_requirement(person: Person):
    return True     # high consequence breakup

def harem_ask_get_boobjob_requirement(person: Person):
    if person.is_affair:
        return False
    return ask_get_boobjob_requirement(person)

def harem_ask_trim_pubes_requirement(person: Person):
    if person.is_affair:
        return False
    return girlfriend_ask_trim_pubes_requirement(person)

def harem_myplace_yourplace_requirement(person: Person):
    if person.home == harem_mansion:    # already in mansion
        return False
    if person.is_affair:
        return False
    return girlfriend_myplace_yourplace_requirement(person)

def harem_unplanned_sleepover_requirement(person: Person):
    if person.home == harem_mansion:    # already in mansion
        return False
    if person.is_affair:
        return False
    return girlfriend_unplanned_sleepover_requirement(person)

def harem_quit_dikdok_requirement(person: Person):
    if person.is_affair:
        return False
    return girlfriend_quit_dikdok_requirement(person)

def get_harem_role_actions():
    ask_harem_move_to_mansion_action = Action("Move into Harem Mansion", harem_move_to_mansion_requirement, "harem_move_to_mansion_label", menu_tooltip = "Ask her to leave her current residence and move into your Harem Mansion.", priority = 10)
    ask_harem_break_up_action = Action("Break up with her\n{menu_red}Will reset love / obedience / relationship{/menu_red}", harem_break_up_requirement, "leave_harem_label", menu_tooltip = "Rip out her heart and stomp on it, will remove her from the Polyamory.")
    ask_harem_get_boobjob_action = Action("Ask her to get a boob job\n{menu_red}Costs: $7000{/menu_red}", harem_ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
    ask_harem_trim_pubes_action = Action("Ask her to trim her pubes", harem_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
    ask_harem_sleepover_action = Action("Arrange a sleepover", harem_myplace_yourplace_requirement, "girlfriend_myplace_yourplace_label", menu_tooltip = "Ask your harem girl if she wants to sleep together tonight.")
    ask_harem_unplanned_sleepover_action = Action("Spend the night", harem_unplanned_sleepover_requirement, "girlfriend_unplanned_sleepover_label", menu_tooltip = "Tell your harem girl you want to spend the night with her.")
    ask_harem_quit_dikdok_action = Action("Quit DikDok", harem_quit_dikdok_requirement, "girlfriend_quit_dikdok_label", menu_tooltip = "Ask your harem girl to stop showing herself off on DikDok.")
    return [ask_harem_move_to_mansion_action, ask_harem_get_boobjob_action, ask_harem_trim_pubes_action, ask_harem_sleepover_action, ask_harem_unplanned_sleepover_action, ask_harem_quit_dikdok_action, ask_harem_break_up_action]

def harem_fuck_date_requirement(person: Person):
    if person.home == harem_mansion:    # already in mansion
        return False
    if person.is_affair:
        return False
    return fuck_date_requirement(person)

def get_harem_role_dates():
    plan_fuck_date_action = Action("Plan a fuck date at her place", harem_fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = 'Pick a night to go over there and spend nothing but "quality time" with each other.')
    girlfriend_shopping_date = Action("Go shopping together {image=time_advance}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
    return [plan_fuck_date_action, girlfriend_shopping_date]

def leave_SO_love_calculation(person: Person) -> int: #Standalone calculation so we can use these values in multiple different events
    love_required = 60 + (person.opinion.cheating_on_men * 10) #This should never be lower than the love requirement for her being your girlfriend.
    if person.relationship == "Fiancée":
        love_required += 10
    elif person.relationship == "Married":
        love_required += 20
    if person.kids > 2:
        love_required += 10
    if person.kids > 0:
        love_required += 5
    if person.age > 30:
        love_required += 5
    return love_required

def ask_leave_SO_requirement(person: Person) -> bool | str:
    love_required = leave_SO_love_calculation(person)
    if person.love < love_required:
        return f"Requires: {love_required} Love"
    return True

def get_paramour_role_actions() -> list[Action]:
    ask_paramour_get_boobjob_action = Action("Ask her to get a boob job\n{menu_red}Costs: $7000{/menu_red}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
    ask_paramour_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
    ask_paramour_underwear_shopping_action = Action("Shop for new lingerie {image=time_advance}", girlfriend_underwear_shopping_requirement, "girlfriend_underwear_shopping_label", menu_tooltip = "Take your paramour out to shop for some exciting underwear to wear for you.")
    ask_paramour_quit_dikdok_action = Action("Quit DikDok", girlfriend_quit_dikdok_requirement, "girlfriend_quit_dikdok_label", menu_tooltip = "Ask your paramour to stop showing herself off on DikDok.")
    ask_paramour_leave_SO_action = Action("Ask her to leave her significant other for you", ask_leave_SO_requirement, "ask_leave_SO_label", menu_tooltip = "This affair has been secret long enough! Ask her to leave her significant other and make your relationship official.")

    return [ask_paramour_get_boobjob_action, ask_paramour_trim_pubes_action, ask_paramour_underwear_shopping_action, ask_paramour_quit_dikdok_action, ask_paramour_leave_SO_action]

def get_paramour_role_dates():
    plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = 'Pick a night to go over there and spend nothing but "quality time" with each other.')
    return [plan_fuck_date_action]

def girlfriend_got_boobjob_requirement(start_day):
    return day >= start_day

def add_girlfriend_got_boobjob_action(person: Person):
    person.event_triggers_dict["getting boobjob"] = True #Reset the flag so you can ask her to get _another_ boobjob.
    mc.business.add_mandatory_crisis(
        Action("Girlfriend Got Boobjob", girlfriend_got_boobjob_requirement, "girlfriend_got_boobjob_label", args = person, requirement_args = day + renpy.random.randint(3, 6))
    )

def girlfriend_boob_brag_requirement(person: Person, start_day: int):
    return day > start_day

def add_girlfriend_brag_boobjob_action(person: Person):
    person.add_unique_on_talk_event(
        Action("Girlfriend Boobjob Brag", girlfriend_boob_brag_requirement, "girlfriend_boob_brag_label", requirement_args = day)
    )

def girlfriend_build_pubes_choice_menu(person: Person):
    valid_pubes_options = [(x.name, x) for x in pube_styles if x.name != person.pubes_style.name]
    valid_pubes_options.append(("Never mind", "Never mind"))
    return valid_pubes_options

def girlfriend_do_trim_pubes_requirement(start_day):
    return day >= start_day

def add_girlfriend_do_trim_pubes_action(person: Person, pubes_choice: Clothing, time_needed: int):
    mc.business.add_mandatory_crisis(
        Action("Girlfriend trim pubes", girlfriend_do_trim_pubes_requirement, "girlfriend_do_trim_pubes_label", args = [person, pubes_choice], requirement_args = [day + time_needed])
    )
    person.event_triggers_dict["trimming_pubes"] = "girlfriend_do_trim_pubes_label"

def girlfriend_trimmed_pubes_requirement(person: Person):
    return not person.location.is_public

def add_girlfriend_trimmed_pubes_notification_action(person: Person):
    person.add_unique_on_room_enter_event(
        Limited_Time_Action(
            Action("Trimmed pubes notification", girlfriend_trimmed_pubes_requirement, "girlfriend_pubes_comment", event_duration = 10)
        )
    )

def girlfriend_set_new_pubes(person: Person, the_style: Clothing):
    new_pubes = the_style.get_copy() #Copy the base style passed to us
    new_pubes.colour = person.pubes_style.colour #Modify the copy to match this person's details
    new_pubes.pattern = person.pubes_style.pattern #TODO: Make sure this makes sense for any future patterns we use.
    new_pubes.colour_pattern = person.pubes_style.colour_pattern
    person.pubes_style = new_pubes #And assign it to them.
    person.event_triggers_dict["trimming_pubes"] = None

def schedule_sleepover_available():
    return not mc.business.event_triggers_dict.get("girlfriend_sleepover_scheduled", False)

def girlfriend_sleepover_crisis_requirement():
    return time_of_day == 4

def schedule_sleepover_in_story(person: Person, your_place = True):
    mc.business.event_triggers_dict["girlfriend_person"] = person.identifier
    mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
    mc.business.event_triggers_dict["your_place"] = your_place
    mc.business.add_mandatory_crisis(
        Action("Have a sleepover", girlfriend_sleepover_crisis_requirement, "girlfriend_sleepover_crisis_label")
    )

def get_random_girlfriend_morning_action(person: Person):
    selected_action = get_random_from_list(
        [x for x in girlfriend_morning_action_list if x.is_action_enabled(person)]
    )
    if selected_action:
        selected_action.args = [person]
        return selected_action
    return None

def get_random_girlfriend_sleepover_interruption_action(person: Person):
    selected_action = get_random_from_list(
        [x for x in girlfriend_sleepover_interruption_list if x.is_action_enabled(person)]
    )
    if selected_action:
        selected_action.args = [person]
        return selected_action
    return None

def girlfriend_wakeup_spooning_requirement(person: Person):
    return True

def girlfriend_wakeup_cowgirl_requirement(person: Person):
    return person.wants_creampie  # since it ends with creampie

# morning action
girlfriend_morning_action_list: list[Action] = [
    Action("Spooning wakeup", girlfriend_wakeup_spooning_requirement, "girlfriend_wakeup_spooning_label"),
    Action("Cowgirl wakeup", girlfriend_wakeup_cowgirl_requirement, "girlfriend_wakeup_cowgirl_label")
]

def caught_cheating_requirement(person: Person):
    return True

def add_caught_cheating_action(person: Person, cheated_on: Person):
    cheated_on.add_unique_on_room_enter_event(
        Action("Caught cheating action", caught_cheating_requirement, "caught_cheating_label", args = person)
    )

def caught_affair_cheating_requirement(person: Person):
    return True

def add_caught_affair_cheating_action(person: Person, cheated_on: Person):
    cheated_on.add_unique_on_room_enter_event(
        Action("Caught affair cheating action", caught_affair_cheating_requirement, "caught_affair_cheating_label", args = person)
    )

def evening_date_trigger():
    if time_of_day == 3: # For now we just check for the correct time of day
        return True
    return False

def afternoon_date_trigger():
    if time_of_day == 2:
        return True
    return False

def night_date_trigger():
    if time_of_day == 4:
        return True
    return False

def morning_date_trigger():
    if time_of_day == 1:
        return True
    return False

def create_fuck_date_action(person: Person, time_slot: tuple[int, int]):
    mc.create_date("fuck_date_label", f"Fuck date with {person.fname}", time_slot = time_slot, person = person)

def so_morning_breakup_requirement(person: Person):
    return True #ALways valid for now.

def add_so_morning_breakup_crisis(person: Person):
    mc.business.add_mandatory_morning_crisis(
        Action("Morning SO breakup", so_morning_breakup_requirement, "so_morning_breakup", args = person, requirement_args = person)
    )
