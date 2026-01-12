from __future__ import annotations
from typing import Callable
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -4 python:
"""

class LimitedWardrobe():
    def __init__(self, name: str, priority: int, func: Callable[[Person], bool], allow_edit = True, allow_personalisation = False, enforce_legal_status = True):
        '''
        name: name of wardrobe or XML file
        priority: higher priority will supply outfit first
        func: A function that determines if this wardrobe is valid at this point for that person
        '''
        self._wardrobe = wardrobe_from_xml(name)
        self._wardrobe._enforce_legal_status = enforce_legal_status
        self.priority = priority
        self.validation_func = func
        # cache for chosen outfit for person for this day
        self.daily_outfits: dict[int, Outfit] = {}
        self.allow_edit = allow_edit
        self.allow_personalisation = allow_personalisation

        self.identifier = generate_identifier(
            (name, priority, func)
        )

    def __hash__(self) -> int:
        return self.identifier

    @property
    def wardrobe(self) -> Wardrobe:
        return self._wardrobe

    @property
    def has_outfits(self) -> bool:
        return self.wardrobe.has_outfits

    @property
    def total_count(self) -> int:
        '''
        Total number of items in wardrobe
        Cumulation of outfit count, underwear count and overwear count
        '''
        return self.wardrobe.total_count

    @property
    def outfit_count(self) -> int:
        '''
        Total number of full outfits in wardrobe
        '''
        return self.wardrobe.outfit_count

    @property
    def overwear_count(self) -> int:
        '''
        Total number of overwear sets in wardrobe
        '''
        return self.wardrobe.overwear_count

    @property
    def underwear_count(self) -> int:
        '''
        Total number of underwear sets in wardrobe
        '''
        return self.wardrobe.underwear_count

    def clear(self):
        self.daily_outfits = {}

    def set_outfit(self, person: Person, outfit: Outfit):
        if isinstance(outfit, Outfit):
            self.daily_outfits[person.identifier] = outfit
        else:
            self.daily_outfits.pop(person.identifier, None)

    def is_valid(self, person: Person) -> bool:
        return self.validation_func(person)

    def decide_on_outfit(self, person: Person, sluttiness_modifier = 0.0, slut_limit = 999, allow_personal_wardrobe = False) -> Outfit:
        if person.identifier in self.daily_outfits:
            return self.daily_outfits[person.identifier]

        outfit = self.wardrobe.decide_on_outfit(person, sluttiness_modifier = sluttiness_modifier, slut_limit = slut_limit, allow_personal_wardrobe = allow_personal_wardrobe)
        if self.allow_personalisation:
            person.personalize_outfit(outfit, swap_bottoms = False, allow_skimpy= False)
        self.set_outfit(person, outfit)
        return outfit

    def pick_random_outfit(self) -> Outfit:
        return self.wardrobe.pick_random_outfit()

    ##############################
    # Wardrobe wrapper functions #
    ##############################

    def add_outfit(self, outfit: Outfit):
        self.wardrobe.add_outfit(outfit)

    def add_underwear_set(self, outfit: Outfit):
        self.wardrobe.add_underwear_set(outfit)

    def add_overwear_set(self, outfit: Outfit):
        self.wardrobe.add_overwear_set(outfit)

    def remove_outfit(self, outfit: Outfit | str):
        self.wardrobe.remove_outfit(outfit)
