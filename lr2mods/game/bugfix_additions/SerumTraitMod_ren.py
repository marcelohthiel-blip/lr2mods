from __future__ import annotations
from typing import Callable
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
class SerumTraitMod(SerumTrait):
    # store instances of mod
    _instances: list[SerumTrait] = []

    def __init__(self, name: str, desc: str, positive_slug = "", negative_slug = "",
            research_added = 0, slots_added = 0, production_added = 0, duration_added = 0, base_side_effect_chance = 0, clarity_added = 0,
            on_apply: Callable[[Person, SerumDesign, bool], None] | None = None,
            on_remove: Callable[[Person, SerumDesign, bool], None] | None = None,
            on_turn: Callable[[Person, SerumDesign, bool], None] | None = None,
            on_day: Callable[[Person, SerumDesign, bool], None] | None = None,
            requires: list[SerumTrait] | SerumTrait | None = None,
            tier = 0, start_researched = False, research_needed=50, exclude_tags=None, is_side_effect = False,
            clarity_cost = 50, start_unlocked = False, start_enabled = True, hidden_tag = "Production",
            mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0,
            allow_toggle: bool = True):

        super().__init__(name, desc, positive_slug, negative_slug,
            research_added, slots_added, production_added, duration_added, base_side_effect_chance, clarity_added,
            on_apply, on_remove, on_turn, on_day,
            requires, tier, start_researched, research_needed, exclude_tags, is_side_effect,
            clarity_cost, start_unlocked,
            mental_aspect, physical_aspect, sexual_aspect, medical_aspect, flaws_aspect, attention, hidden_tag = hidden_tag)

        self.enabled = start_enabled
        self.allow_toggle = allow_toggle

        # store the instance in class static
        SerumTraitMod._instances.append(self)

    def toggle_enabled(self):
        if self.allow_toggle:
            self.enabled = not self.enabled
            self.update_serum_trait()

    def update_serum_trait(self):
        found = next((x for x in list_of_traits if x == self), None)

        new_requires = []
        for req in self.requires:
            requirement = next((x for x in list_of_traits if x == req), None)
            if requirement:
                new_requires.append(requirement)
        self.requires = new_requires

        if self.enabled:
            if not found:
                list_of_traits.append(self)
        elif found:
            list_of_traits.remove(found)
