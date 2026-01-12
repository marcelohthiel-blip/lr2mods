from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import kaya, sakari
from game.major_game_classes.game_logic.Role_ren import Role

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""


def sakari_is_sick():
    return sakari.event_triggers_dict.get("is_sick", False)

def sakari_intro_complete():
    return sakari.event_triggers_dict.get("intro_complete", False)

def sakari_mc_knows_sick():
    return sakari.event_triggers_dict.get("mc_knows_sick", False)

def sakari_offered_mc_partner():
    return sakari.event_triggers_dict.get("mc_offered_partner", False)

def sakari_mc_are_partners():
    return sakari.event_triggers_dict.get("mc_is_partner", False)

def sakari_mc_is_booty_call():
    return sakari.event_triggers_dict.get("mc_is_booty_call", False)

def sakari_is_mc_personal_milf():
    return sakari.event_triggers_dict.get("is_mc_personal_milf", False)

def sakari_is_jealous():
    return sakari.event_triggers_dict.get("is_jealous", True)

def sakari_has_skinny_dipped():
    return sakari.event_triggers_dict.get("has_skinny_dipped", False)

def sakari_has_given_movie_bj():
    return sakari.event_triggers_dict.get("has_given_movie_bj", False)

def sakari_has_fucked_at_store():
    return sakari.event_triggers_dict.get("has_fucked_at_store", False)

def sakari_has_stripped_at_club():
    return sakari.event_triggers_dict.get("has_stripped_at_club", False)

def sakari_has_had_kaya_threesome():
    return sakari.event_triggers_dict.get("had_kaya_threesome", False)

def sakari_has_died():
    return kaya.event_triggers_dict.get("sakari_has_died", False)
