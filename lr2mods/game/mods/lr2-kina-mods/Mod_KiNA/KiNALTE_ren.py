from __future__ import annotations
from renpy import persistent
import builtins
from game.bugfix_additions.ActionMod_ren import limited_time_event_pool
from game.game_roles._role_definitions_ren import girlfriend_role, mother_role, sister_role, instapic_role, onlyfans_role, dikdok_role
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.game_logic.Action_ren import Action

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def get_closer_requirement(person: Person):
    if time_of_day not in (0, 4) and person.love > 20: #dont chat early morning or late night and only if we know them enough...
        if person.effective_sluttiness() > 60: #Slutty enough, we just check everything
            return person.has_unknown_opinions
        else:
            return person.has_unknown_normal_opinions #Just normal opinion then
    else:
        return False

def family_degenerating_requirement(person: Person):
    if not (time_of_day == 0 or time_of_day == 4): #ie. early morning (sleeping in) or late at night (early bed time)
        return False
    if not person.has_role([sister_role, mother_role]):
        return False
    if person == mom and time_of_day == 0 and day % 7 == 5:
        return False #Don't want to trigger at the same time as the morning offer.
    if not person.is_home:
        return False
    if person.home.person_count > 1: #And nobody else.
        return False
    if ((person.sex_record.get("Orgasms", 0) > 20) and (person.known_opinion.incest == -2)):    #For starter, we just check her orgasm stat
        return True
    elif ((person.cum_exposure_count > 20) and (person.known_opinion.incest == -1)):    #Now we count our cum in or on her.. drinking, creampies(both holes) or spray paint all over her
        return True
    elif ((person.sex_record.get("Vaginal Creampies", 0) > 20) and (person.known_opinion.incest == 0)): #We now filled her pussy to the brim. No more condoms
        return True
    elif ((person.knows_pregnant and person.is_mc_father) and (person.known_opinion.incest == 1)): #You practically her hubby now. She loves you, she loves incest
        return True
    elif person.known_opinion.incest > 1: #Maxxed incest.. No longer needed
        return False
    return False

### ON ENTER EVENTS ###
limited_time_event_pool.append(
    Action("Get to know others", get_closer_requirement, "chat_break_label", event_duration = 1,
    priority = 1, trigger = "on_enter"))

limited_time_event_pool.append(
    Action("Family accepting incest", family_degenerating_requirement, "family_accept_incest_label",
        event_duration = 1, priority = 8, trigger = "on_enter"))