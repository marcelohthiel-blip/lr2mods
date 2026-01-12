from __future__ import annotations
import builtins
from game.main_character.perks.Perks_ren import Ability_Perk, perk_system
from game.major_game_classes.game_logic.ClimaxController_ren import ClimaxController
from game.major_game_classes.character_related.Person_ren import mc
from renpy import persistent

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def tits_man_perk_unlock():
    if not perk_system.has_ability_perk("Tits Man"):
        perk_system.add_ability_perk(Ability_Perk(description = "Gain increased clarity when cumming on tits.", active = True, save_load = tits_man_perk_save_load, usable = False), "Tits Man")
        tits_man_perk_unlock()
        return True
    return False

def tits_man_perk_save_load():
    ClimaxController.climax_type_dict["tits"] = 2.0

def ass_man_perk_unlock():
    if not perk_system.has_ability_perk("Ass Man"):
        perk_system.add_ability_perk(Ability_Perk(description = "Gain increased clarity when cumming on ass.", active = True, save_load = ass_man_perk_save_load, usable = False), "Ass Man")
        ass_man_perk_save_load()
        return True
    return False

def ass_man_perk_save_load():
    ClimaxController.climax_type_dict["body"] = 2.0

def lustful_vigour_perk_update_func():
    lust_factor = builtins.abs(mc.lust_tier - 4)
    mc.change_locked_clarity(lust_factor * 20, add_to_log = False)

def lustful_vigour_perk_unlock():
    if not perk_system.has_ability_perk("Lustful Vigour"):
        perk_system.add_ability_perk(Ability_Perk(description = "Gain lust quickly when it is low.", active = True, togglable = True, usable = False, update_func = lustful_vigour_perk_update_func), "Lustful Vigour")
        return True
    return False

def lustful_youth_perk_update_func():
    mc.change_energy((mc.lust_tier * 20), add_to_log = False)

def lustful_youth_perk_unlock():
    if not perk_system.has_ability_perk("Lustful Youth"):
        perk_system.add_ability_perk(Ability_Perk(description = "Gain energy back more rapidly with high lust.", active = True, togglable = True, usable = False, update_func = lustful_youth_perk_update_func), "Lustful Youth")
        return True
    return False

def situational_awareness_perk_update_func():
    if mc.location.person_count == 0:
        return

    amount = int(mc.location.room_outfit_eye_candy_score)
    mc.change_locked_clarity(amount, add_to_log = False)
    if persistent.clarity_messages:
        mc.log_event(f"You gain {amount} Lust from eye candy in this room.", "float_text_blue")

def situational_awareness_perk_unlock():
    if not perk_system.has_ability_perk("Situational Awareness"):
        perk_system.add_ability_perk(Ability_Perk(description = "Gain lust based on sluttiness of girl's outfits in the area.", active = True, togglable = True, usable = False, update_func = situational_awareness_perk_update_func), "Situational Awareness")
        return True
    return False

def personality_perception_perk_unlock():
    if not perk_system.has_ability_perk("Personality Perception") and mc.stats.opinions_discovered > 40:
        perk_system.add_ability_perk(Ability_Perk(description = "When interacting with a girl, you gain some insights into her personal opinions.", active = True, togglable = False, usable = False), "Personality Perception")
        return True
    return False

def sexual_preference_perception_perk_unlock():
    if not perk_system.has_ability_perk("Extra Sexual Perception") and mc.stats.sexy_opinions_discovered > 40:
        perk_system.add_ability_perk(Ability_Perk(description = "When interacting with a girl, you gain some insights into her sexual preferences.", active = True, togglable = False, usable = False), "Extra Sexual Perception")
        return True
    return False

def ovulation_cycle_perception_perk_unlock():
    if not perk_system.has_ability_perk("Ovulation Cycle Perception") and mc.offspring_count + len(mc.girls_knocked_up) > 3:
        perk_system.add_ability_perk(Ability_Perk(description = "When you know her BC status and see or interact with a girl, you gain the ability to predict if she's ovulating.", active = True, togglable = False, usable = False), "Ovulation Cycle Perception")
        return True
    return False
