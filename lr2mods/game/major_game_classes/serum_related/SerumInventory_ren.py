from __future__ import annotations
from typing import Callable
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait
from game.business_policies.organisation_policies_ren import attention_floor_increase_1_policy, attention_floor_increase_2_policy
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class SerumInventory(): #A bag class that lets businesses and people hold onto different types of serums, and move them around.
    def __init__(self, starting_list: list[tuple[SerumDesign, int]] | None = None):
        # TODO: Refactor serums held to dictionary with SerumDesign as key
        if starting_list is None:
            self.serums_held: list[tuple[SerumDesign, int]] = []
        else:
            self.serums_held: list[tuple[SerumDesign, int]] = starting_list ##Starting list is a list of tuples, going [SerumDesign,count]. Count should be possitive.

    @property
    def has_serum(self) -> bool:
        return len(self.serums_held) > 0

    @property
    def total_serum_count(self) -> int:
        return sum(dose_count for _, dose_count in self.serums_held)

    def get_serum_count(self, serum_design: SerumDesign) -> int:
        return sum(dose_count for design, dose_count in self.serums_held if design == serum_design)

    def get_matching_serum_count(self, check_function: Callable[[SerumDesign], bool] = lambda x: True) -> int: #Hand a function to the inventory and get a count of the number of serums that match that requirement.
        return sum(self.get_serum_count(x) for x in self.get_serum_types if check_function(x))

    @property
    def get_serum_types(self) -> list[SerumDesign]: ## returns a list of all the serum types that are in the inventory, without their counts.
        return [design for design, _ in self.serums_held]

    @property
    def total_attention(self) -> int:
        attention_modifier = 0
        if attention_floor_increase_1_policy.is_active:
            attention_modifier += 1
        if attention_floor_increase_2_policy.is_active:
            attention_modifier += 1

        return sum((max(design.attention - attention_modifier, 0) * dose_count) for design, dose_count in self.serums_held)

    @property
    def get_max_serum_count(self) -> int: #Returns the count of the highest group of serums you have available.
        if not self.get_serum_types:
            return 0
        return max(self.get_serum_count(x) for x in self.get_serum_types)

    def change_serum(self, serum_design: SerumDesign, change_amount: int): ##Serum count must be greater than 0. Adds to stockpile of serum_design if it is already there, creates it otherwise.
        if found := next((x for x in self.serums_held if x[0].is_same_design(serum_design)), None):
            if found[1] + change_amount > 0:
                found[1] += change_amount
            else:
                self.serums_held.remove(found)
        elif change_amount > 0:
            self.serums_held.append([serum_design, change_amount])

    def has_serum_with_trait(self, trait: SerumTrait) -> bool:
        return any(x for x in self.get_serum_types if x.has_trait(trait))
    
    def has_serum_with_hidden_tag(self, tag_name: str) -> bool:
        return any(x for x in self.get_serum_types if x.has_hidden_tag(tag_name))

    def get_serums_with_trait(self, trait: SerumTrait) -> list[SerumDesign]:
        return [x for x in self.get_serum_types if x.has_trait(trait)]
    
    def get_serums_with_hidden_tag(self, tag_name: str) -> list[SerumDesign]:
        return [x for x in self.get_serum_types if x.has_hidden_tag(tag_name)]
