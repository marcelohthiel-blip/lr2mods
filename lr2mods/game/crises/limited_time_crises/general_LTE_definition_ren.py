from __future__ import annotations
import builtins
from game.bugfix_additions.ActionMod_ren import limited_time_event_pool
from game.game_roles._role_definitions_ren import mother_role, sister_role, instapic_role, onlyfans_role, dikdok_role
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Action_ren import Action

day = 0
TIER_2_TIME_DELAY = 7
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def work_spank_opportunity_requirement(person: Person):
    return (
        person.arousal_perc > 30    # she needs to be a little aroused (reduce number of events)
        and (
            ((person.is_employee or person.is_intern) and person.is_at_office)
            or (mc.owns_strip_club and person.is_strip_club_employee and person.is_at_stripclub)
        )
    )

def ask_new_title_requirement(person: Person):
    return (
        day > 7
        and person.obedience < 180   #If she has higher obedience she ONLY lets you change her title.
        and person.has_event_delay("day_met", TIER_2_TIME_DELAY) # after first meet delay title change
        and person.has_event_delay("ask_new_title", TIER_2_TIME_DELAY) #delay for just change titles
        and not (person.is_employee and person.is_family and person.is_at_office) # Family employees have their own title mechanic
        and (builtins.len(person.get_titles()) > 1 or builtins.len(person.get_player_titles()) > 1)
    )

def work_walk_in_requirement(person: Person): #AKA she has to work for you, be at work, and be turned on
    return (
        person.energy > 40
        and person.arousal_perc > 40
        and person.sluttiness > 50 - (5 * person.opinion.masturbating)
        and person.has_event_delay("work_walk_in", TIER_2_TIME_DELAY)
        and person.is_employee
        and person.is_at_office
    )

def new_insta_account_requirement(person: Person):
    return (
        person.love > 15    #Girls who don't like you won't tell you they've made a profile
        and not person.has_role((instapic_role, mother_role, sister_role))
        and person.effective_sluttiness() > (100 - person.personality.insta_chance) - 5 * person.opinion.showing_her_tits - 5 * person.opinion.showing_her_ass
    )

def new_dikdok_account_requirement(person: Person):
    return (
        person.love > 30
        and not person.event_triggers_dict.get("block_dikdok", False)
        and not person.has_relation_with_mc
        and not person.has_role((dikdok_role, mother_role, sister_role))
        and person.effective_sluttiness() > (100 - person.personality.dikdok_chance) - 5 * person.opinion.showing_her_tits - 5 * person.opinion.showing_her_ass
    )

def new_onlyfans_account_requirement(person: Person):
    return (
        person.love > 40
        and not person.event_triggers_dict.get("block_onlyfans", False)
        and not person.has_role((onlyfans_role, mother_role, sister_role))
        and person.effective_sluttiness() > 90 - 5 * person.opinion.showing_her_tits - 5 * person.opinion.showing_her_ass - 5 * person.opinion.public_sex
    )

### ON TALK EVENTS ###
limited_time_event_pool.append(
    Action("Ask new title", ask_new_title_requirement, "ask_new_title_label",
        event_duration = 2, priority = 8, trigger = "on_talk", silent = True))

limited_time_event_pool.append(
    Action("Employee walk in", work_walk_in_requirement, "work_walk_in_label",
        event_duration = 4, priority = 4, trigger = "on_talk"))

limited_time_event_pool.append(
    Action("Employee spank opportunity", work_spank_opportunity_requirement, "work_spank_opportunity",
        event_duration = 2, priority = 2, trigger = "on_enter", silent = True))

limited_time_event_pool.append(
    Action("Make New Insta", new_insta_account_requirement, "new_insta_account",
        event_duration = 4, priority = 4, trigger = "on_talk"))

limited_time_event_pool.append(
    Action("Make New Dikdok", new_dikdok_account_requirement, "new_dikdok_account",
        event_duration = 4, priority = 2, trigger = "on_talk"))

limited_time_event_pool.append(
    Action("Make New Onlyfans", new_onlyfans_account_requirement, "new_onlyfans_account",
        event_duration = 4, priority = 1, trigger = "on_talk"))
