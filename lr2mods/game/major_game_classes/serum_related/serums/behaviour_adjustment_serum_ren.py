# Behaviour Adjustment Serum by Starbuck
from __future__ import annotations
import renpy
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def behaviour_adjustment_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.obedience_tier >= 5:
        return # caps at 180 obedience

    suggestion_bonus = (1 + person.suggest_tier - person.obedience_tier) * 5
    if renpy.random.randint(0, 100) < 10 + suggestion_bonus + (person.opinion.being_submissive * 5) - (person.opinion.taking_control * 5):
        person.change_obedience(1, add_to_log = add_to_log)

SerumTraitMod(name = "Behaviour Adjustment",
    desc = "Slowly increases obedience. Strong wills can resist it, but it increases effect based on suggestibility.",
    positive_slug = "Slowly increases obedience based on suggestibility",
    negative_slug = "",
    research_added = 100,
    base_side_effect_chance = 50,
    on_turn = behaviour_adjustment_on_turn,
    tier = 1,
    start_researched = False,
    research_needed = 500,
    clarity_cost = 500,
    mental_aspect = 3, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 2, flaws_aspect = 0, attention = 2,
    hidden_tag = ["Obedience"],
    start_enabled = True)
