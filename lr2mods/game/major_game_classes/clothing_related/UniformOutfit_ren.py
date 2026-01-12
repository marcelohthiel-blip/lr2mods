from __future__ import annotations
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class UniformOutfit():
    def __init__(self, outfit: Outfit):
        self.outfit = outfit.get_copy()

        self.full_outfit_flag = False
        self.overwear_flag = False
        self.underwear_flag = False

        self.full_outfit_flag = self.can_toggle_full_outfit_state #True if this uniform should belong in the overwear set of the appropriate wardrobes
        self.overwear_flag = self.can_toggle_overwear_state
        self.underwear_flag = self.can_toggle_underwear_state

        enabled = self.full_outfit_flag or self.overwear_flag or self.underwear_flag

        self.hr_flag = enabled #True if this uniform should belong to this departments wardrobe.
        self.research_flag = enabled
        self.production_flag = enabled
        self.supply_flag = enabled
        self.marketing_flag = enabled

    def __hash__(self) -> int:
        return self.outfit.__hash__()

    def __eq__(self, other: UniformOutfit) -> bool:
        if not isinstance(other, UniformOutfit):
            return NotImplemented
        return self.outfit.identifier == other.outfit.identifier

    def set_full_outfit_flag(self, state: bool):
        self.full_outfit_flag = state

    def set_overwear_flag(self, state: bool):
        self.overwear_flag = state

    def set_underwear_flag(self, state: bool):
        self.underwear_flag = state

    def set_research_flag(self, state: bool):
        self.research_flag = state

    def set_production_flag(self, state: bool):
        self.production_flag = state

    def set_supply_flag(self, state: bool):
        self.supply_flag = state

    def set_marketing_flag(self, state: bool):
        self.marketing_flag = state

    def set_hr_flag(self, state: bool):
        self.hr_flag = state

    @property
    def can_toggle_full_outfit_state(self) -> bool:
        if self.full_outfit_flag:
            return True # You can always remove uniforms.

        slut_limit, _, limited_to_top = mc.business.get_uniform_limits()
        if limited_to_top:
            return False

        if self.outfit.outfit_slut_score > slut_limit:
            return False

        return True

    @property
    def can_toggle_overwear_state(self) -> bool:
        if self.overwear_flag:
            return True

        slut_limit, _, _ = mc.business.get_uniform_limits()
        if self.outfit.overwear_slut_score > slut_limit:
            return False

        if not self.outfit.is_suitable_overwear_set:
            return False

        return True

    @property
    def can_toggle_underwear_state(self) -> bool:
        if self.underwear_flag:
            return True

        _, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
        if limited_to_top:
            return False

        if self.outfit.underwear_slut_score > underwear_limit:
            return False

        if not self.outfit.is_suitable_underwear_set:
            return False

        return True
