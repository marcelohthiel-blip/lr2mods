from __future__ import annotations
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class StripClubOutfit():
    def __init__(self, outfit: Outfit, auto_enable = True):
        self.outfit = outfit.get_copy()

        if auto_enable:
            self.full_outfit_flag = self.can_toggle_full_outfit_state #True if this uniform should belong in the overwear set of the appropriate wardrobes
            self.overwear_flag = self.can_toggle_overwear_state
            self.underwear_flag = self.can_toggle_underwear_state
            enabled = self.full_outfit_flag or self.overwear_flag or self.underwear_flag
        else:
            self.full_outfit_flag = False
            self.overwear_flag = False
            self.underwear_flag = False
            enabled = False

        self.stripper_flag = enabled #True if this uniform should belong to this departments wardrobe.
        self.waitress_flag = enabled
        self.bdsm_flag = enabled
        self.manager_flag = enabled
        self.mistress_flag = enabled

    def __hash__(self):
        return self.outfit.__hash__()

    def __eq__(self, other: StripClubOutfit) -> bool:
        if not isinstance(other, StripClubOutfit):
            return NotImplemented
        return self.outfit.identifier == other.outfit.identifier

    def set_full_outfit_flag(self, state: bool):
        self.full_outfit_flag = state

    def set_overwear_flag(self, state: bool):
        self.overwear_flag = state

    def set_underwear_flag(self, state: bool):
        self.underwear_flag = state

    def set_stripper_flag(self, state: bool):
        self.stripper_flag = state

    def set_waitress_flag(self, state: bool):
        self.waitress_flag = state

    def set_bdsm_flag(self, state: bool):
        self.bdsm_flag = state

    def set_manager_flag(self, state: bool):
        self.manager_flag = state

    def set_mistress_flag(self, state: bool):
        self.mistress_flag = state

    @property
    def can_toggle_full_outfit_state(self) -> bool:
        return True

    @property
    def can_toggle_overwear_state(self) -> bool:
        return self.outfit.is_suitable_overwear_set

    @property
    def can_toggle_underwear_state(self) -> bool:
        return self.outfit.is_suitable_underwear_set
