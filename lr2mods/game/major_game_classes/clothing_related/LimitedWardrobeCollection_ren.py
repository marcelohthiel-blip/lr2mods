from __future__ import annotations
from collections.abc import Iterator
from typing import Iterable
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.LimitedWardrobe_ren import LimitedWardrobe
from game.major_game_classes.clothing_related.Outfit_ren import Outfit

limited_wardrobes: LimitedWardrobeCollection
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -3 python:
"""
from collections import UserList

class LimitedWardrobeCollection(UserList):
    def __init__(self, iterable = None):
        if iterable is None:
            iterable = []
        super().__init__(item for item in iterable if type(item) in [LimitedWardrobe])

    def __setitem__(self, index, item):
        if type(item) in [LimitedWardrobe]:
            self.data[index] = item
        else:
            msg = 'Item must be a limited wardrobe.'
            raise TypeError(msg)

    def _update_sorted_list(self):
        self._sorted = sorted(self.data, key=lambda x: x.priority, reverse=True)

    def append(self, item: LimitedWardrobe):
        if type(item) in [LimitedWardrobe]:
            self.data.append(item)
            self._update_sorted_list()
        else:
            msg = 'Item must be a limited wardrobe.'
            raise TypeError(msg)

    def extend(self, items: Iterable[LimitedWardrobe]) -> None:
        self.data.extend(items)
        self._update_sorted_list()

    def __iter__(self) -> Iterator[LimitedWardrobe]:
        return iter(self._sorted)

    def should_use_limited_wardrobe(self, person: Person) -> bool:
        return any(x for x in self if x.has_outfits and x.is_valid(person))

    def decide_on_outfit(self, person: Person, sluttiness_modifier: float = 0, slut_limit: int = 999, allow_personal_wardrobe = True) -> Outfit:
        limited_wardobe = next((x for x in self if x.has_outfits and x.is_valid(person)), None)
        return limited_wardobe.decide_on_outfit(person, sluttiness_modifier, slut_limit, allow_personal_wardrobe)

    def update_outfit(self, person: Person, outfit: Outfit):
        limited_wardobe = next((x for x in self if x.has_outfits and x.is_valid(person)), None)
        limited_wardobe.set_outfit(person, outfit)
