from __future__ import annotations
import builtins
from typing import Callable
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.business_policies.organisation_policies_ren import attention_floor_increase_1_policy, attention_floor_increase_2_policy
from game.helper_functions.misc_helpers_ren import round_to_nearest
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumInventory_ren import SerumInventory
from game.major_game_classes.character_related.Person_ren import mc
import renpy
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class Contract():
    def __init__(self, name: str, description: str, contract_length: int,
            mental_requirement: int, physical_requirement: int, sexual_requirement: int,
            medical_requirement: int, flaw_tolerance: int, attention_tolerance: int,
            amount_desired: int,
            other_requirement: Callable[[SerumDesign], bool] = None,
            other_payout: Callable[[], None] = None):

        self.name = name #A descriptive name of the contract.
        self.description = description #A sentence or two describing the contract/vendor, ect. "So-and-so is looking for a product to ensure greater obedience within their company.")
        self.contract_length = contract_length
        self.mental_aspect = mental_requirement
        self.physical_aspect = physical_requirement
        self.sexual_aspect = sexual_requirement
        self.medical_aspect = medical_requirement
        self.flaws_aspect = flaw_tolerance
        self.attention = attention_tolerance
        self.amount_desired = amount_desired
        self.other_requirement = other_requirement  #Allows for additional serum requirements, such as specific traits.
        self.other_payout = other_payout            #Allows for tracking or other rewards from finishing the contract in addition to money

        self.contract_started = False

        self.time_elapsed = 0

        self.inventory = SerumInventory()

        self.price_per_aspect = 12 + (10 * (renpy.random.random() - 0.5))
        self.price_per_dose = builtins.round(self.price_per_aspect * (self.mental_aspect + self.physical_aspect + self.sexual_aspect + self.medical_aspect), 2)
        self.identifier = generate_identifier(
            (self.name, self.contract_length, self.mental_aspect, self.physical_aspect, self.sexual_aspect,
             self.medical_aspect, self.flaws_aspect, self.amount_desired, self.price_per_aspect, self.price_per_dose)

        )

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Contract) -> bool:
        if not isinstance(other, Contract):
            return NotImplemented
        return (self.name, self.contract_length, self.mental_aspect, self.physical_aspect, self.sexual_aspect,
                self.medical_aspect, self.flaws_aspect, self.amount_desired, self.price_per_aspect, self.price_per_dose) == \
            (other.name, other.contract_length, other.mental_aspect, other.physical_aspect, other.sexual_aspect,
             other.medical_aspect, other.flaws_aspect, other.amount_desired, other.price_per_aspect, other.price_per_dose)

    def run_day(self) -> bool:
        if self.contract_started:
            self.time_elapsed += 1
        if self.time_elapsed > self.contract_length:
            return True
        return False

    def check_serum(self, serum: SerumDesign) -> bool:
        effective_attention = serum.attention
        if attention_floor_increase_1_policy.is_active:
            effective_attention -= 1
        if attention_floor_increase_2_policy.is_active:
            effective_attention -= 1

        if callable(self.other_requirement) and not self.other_requirement(serum):
            return False

        if serum.mental_aspect < self.mental_aspect \
                or serum.physical_aspect < self.physical_aspect \
                or serum.sexual_aspect < self.sexual_aspect \
                or serum.medical_aspect < self.medical_aspect \
                or serum.flaws_aspect > self.flaws_aspect \
                or serum.attention > self.attention:
            return False
        return True

    @property
    def serum_count(self) -> int:
        count = 0
        for design, dose_count in self.inventory.serums_held:
            if self.check_serum(design):
                count += dose_count
        return count

    @property
    def can_finish_contract(self) -> bool:
        return self.inventory.get_matching_serum_count(self.check_serum) >= self.amount_desired

    @property
    def pay_out(self) -> int:
        return round_to_nearest(self.price_per_dose * self.amount_desired, 100)

    def start_contract(self):
        self.contract_started = True

    def finish_contract(self):
        self.inventory = SerumInventory()
        if callable(self.other_payout):
            self.other_payout()
        mc.listener_system.fire_event("contract_complete")

    def abandon_contract(self):
        for design, dose_count in self.inventory.serums_held:
            mc.business.inventory.change_serum(design, dose_count)

        self.inventory = SerumInventory()
        self.contract_started = False

    @property
    def reference_design(self) -> SerumDesign:
        return self._reference_design

    @reference_design.setter
    def reference_design(self, value: SerumDesign):
        self._reference_design = value
