# Constant Stimulation Serum by Starbuck
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

def constant_stimulation_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.sluttiness >= 80:
        return

    if renpy.random.randint(0, 100) < person.suggestibility - person.sluttiness:
        person.change_slut(1, add_to_log = add_to_log)   #No cap because the condition should cap it for us, gives reward for extremely high suggestibility values also.

SerumTraitMod(name = "Constant Stimulation",
    desc = "Slowly increases sluttiness. Strong wills can resist it, but it increases effect based on suggestibility.",
    positive_slug = "Slowly increases sluttiness based on suggestibility",
    negative_slug = "",
    research_added = 100,
    base_side_effect_chance = 50,
    on_turn = constant_stimulation_on_turn,
    tier = 1,
    start_researched = False,
    research_needed = 500,
    clarity_cost = 500,
    mental_aspect = 2, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 3,
    hidden_tag = ["Slut"],
    start_enabled = True)
