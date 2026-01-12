# Dopamine Therapy Serum by Starbuck
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

def dopamine_therapy_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if renpy.random.randint(0, 100) < (person.suggestibility - (person.happiness - 100)) * 5:
        person.change_happiness(1, add_to_log = add_to_log)

SerumTraitMod(name = "Dopamine Therapy",
        desc = "Slowly increases happiness. Increases effect based on suggestibility.",
        positive_slug = "Slowly increases happiness based on suggestibility",
        negative_slug = "",
        research_added = 100,
        base_side_effect_chance = 20,
        on_turn = dopamine_therapy_on_turn,
        tier = 1,
        start_researched = False,
        research_needed = 500,
        clarity_cost = 500,
        hidden_tag = "Medical",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 1)
