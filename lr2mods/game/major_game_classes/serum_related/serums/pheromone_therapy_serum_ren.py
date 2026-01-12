# Pheromone Therapy Serum by Starbuck

from __future__ import annotations
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def pheromone_therapy_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_slut(15, add_to_log = add_to_log)
    serum.effects_dict["pheromone_therapy_change"] = change_amount

def pheromone_therapy_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("pheromone_therapy_change", 15)
    person.change_slut(-(15 if change_amount is None else change_amount), add_to_log = add_to_log)

SerumTraitMod(name = "Pheromone Therapy",
    desc = "By mimicking pheromones found in closely related animals, this serum can recreate feelings of going into heat in women. No effect when girl at maximum sluttiness.",
    positive_slug = "+15 Sluttiness",
    negative_slug = "",
    research_added = 200,
    base_side_effect_chance = 20,
    on_apply = pheromone_therapy_on_apply,
    on_remove = pheromone_therapy_on_remove,
    tier = 2,
    start_researched = False,
    research_needed = 800,
    clarity_cost = 1500,
    hidden_tag = "Slut",
    mental_aspect = 5, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 2,
    start_enabled = False)
