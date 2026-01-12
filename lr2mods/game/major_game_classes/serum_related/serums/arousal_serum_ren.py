from __future__ import annotations
import builtins
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
# NOTE: This was part of a story line, but is currently not active

def arousal_serum_function_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.arousal < person.suggestibility:
        person.change_arousal(builtins.min(15, person.suggestibility - person.arousal), add_to_log = False)

arousal_serum_trait = SerumTrait(name = "Female Viagra",
    desc = "Reverse engineered from the pills you ordered. Increases arousal over time, maxing out based on suggestibility.",
    positive_slug = "+15 Arousal over time",
    negative_slug = "",
    research_added = 20,
    base_side_effect_chance = 30,
    on_turn = arousal_serum_function_on_turn,
    tier = 2,
    start_researched = True,
    research_needed = 800,
    clarity_cost = 1000,
    hidden_tag = "Slut",
    mental_aspect = 2, physical_aspect = 3, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 2)
