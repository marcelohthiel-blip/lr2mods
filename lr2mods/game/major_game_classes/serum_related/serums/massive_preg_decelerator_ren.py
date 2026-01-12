# Massive Pregnancy Decelerator (Original by Kaden)
from __future__ import annotations
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import pregnancy_decelerator_trait

day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
list_of_instantiation_functions.append("init_massive_pregnancy_decelerator_serum")

def massive_pregnancy_decelerator_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.is_pregnant:
        return

    if person.event_triggers_dict.get("preg_announce_day", day) > day:
        person.event_triggers_dict["preg_announce_day"] = person.event_triggers_dict.get("preg_announce_day", day) + 1
    if person.event_triggers_dict.get("preg_tits_date", day) > day:
        person.event_triggers_dict["preg_tits_date"] = person.event_triggers_dict.get("preg_tits_date", day) + 1
    if person.event_triggers_dict.get("preg_transform_day", day) > day:
        person.event_triggers_dict["preg_transform_day"] = person.event_triggers_dict.get("preg_transform_day", day) + 1
    if person.event_triggers_dict.get("preg_finish_announce_day", day) > day:
        person.event_triggers_dict["preg_finish_announce_day"] = person.event_triggers_dict.get("preg_finish_announce_day", day) + 1
    return

def init_massive_pregnancy_decelerator_serum():
    SerumTraitMod(name = "Pregnancy Hormone Inhibitors",
        desc = "Clamps down on natural pregnancy hormone production. Massively decreases the pace at which a pregnancy will progress.",
        positive_slug = "-1 Pregnancy Progress per Turn",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 80,
        on_turn = massive_pregnancy_decelerator_on_turn,
        requires = [pregnancy_decelerator_trait],
        tier = 3,
        research_needed = 1400,
        exclude_tags = "Pregnancy",
        clarity_cost = 1800,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 9, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 4)
