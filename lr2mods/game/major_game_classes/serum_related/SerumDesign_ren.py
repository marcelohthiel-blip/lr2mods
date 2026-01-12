from __future__ import annotations
from itertools import chain
import builtins
import renpy
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.bugfix_additions.debug_info_ren import write_log
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import clinical_testing
from game.major_game_classes.serum_related.serums._serum_traits_T3_ren import self_generating_serum
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_side_effects
from game.main_character.MainCharacter_ren import mc

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class SerumDesign(): #A class that represents a design for a serum built up from serum traits.
    @staticmethod
    def build_test_serum(serumtraits, duration = 1):
        serum = SerumDesign.clone_serum("Test Serum", serumtraits)
        serum.duration = duration
        return serum

    @staticmethod
    def clone_serum(name, serumtraits):
        serum = SerumDesign(name)
        if isinstance(serumtraits, SerumTrait):
            serumtraits = [serumtraits]

        for trait in (x for x in serumtraits if isinstance(x, SerumTrait)):
            serum.add_trait(trait)
        return serum

    def __init__(self, name = ""):
        self.name = name
        self.traits: list[SerumTrait] = []
        self.side_effects: list[SerumTrait] = []

        self.researched = False
        self.unlocked = False
        self.obsolete = False
        self.current_research = 0.0

        self.research_needed = 0
        self.clarity_needed = 0
        self.slots = 0
        self.production_cost = 0

        self.duration = 0
        self.duration_counter = 0

        self.expires = True #If set to false the serum does not tick up the duration_counter, meaning it will never expire.

        self.effects_dict = {} # A dict that can be used to store information about this serum when applied to people. For example, tracking how much Sluttiness was added so the same amount can be removed at the end of the duration.

        self.mental_aspect = 0
        self.physical_aspect = 0
        self.sexual_aspect = 0
        self.medical_aspect = 0
        self._flaws_aspect = 0
        self._market_demand = 1.0   # 1.0 means 100%, sale price per unit is adjusted by this factor
        self.attention_modifier = 0  # is modified by change_attention

    @property
    def identifier(self) -> int:    # name is empty on object creation and can be changed by user
        return self.__hash__()

    def __hash__(self) -> int:
        return generate_identifier(tuple(self.name) + tuple(self))

    def __eq__(self, other: SerumDesign) -> bool:
        if not isinstance(other, SerumDesign):
            return NotImplemented
        return self.identifier == other.identifier

    def __sort_key__(self, trait: SerumTrait) -> tuple[int, int, int, str]:
        return (trait.tier, trait.base_side_effect_chance, trait.research_needed, trait.name)

    def __iter__(self):
        '''
        Default sort returns highest tier traits first
        '''
        return iter(
            sorted(
                chain(self.traits, self.side_effects),
                key = self.__sort_key__,
                reverse = True
            )
        )

    def __iter_reverse__(self):
        return iter(
            sorted(
                chain(self.traits, self.side_effects),
                key = self.__sort_key__,
            )
        )

    def is_same_design(self, other: SerumDesign) -> bool: #Checks if two serums are the same design (but not necessarily the same _dose_ of that design).
        if not isinstance(other, SerumDesign):
            write_log("Warning: passed parameter to SerumDesign.is_same_design() is no SerumDesign")
            return False

        if len(self.traits) != len(other.traits):
            return False
        if len(self.side_effects) != len(other.side_effects):
            return False

        return all(x.is_similar(y) for x, y in zip(self, other))

    def reset(self): #Resets the serum to the default serum values.
        self.__init__(self.name)

    @property
    def trait_count(self) -> int:
        return builtins.len(self.traits)

    @property
    def slots_used(self) -> int:
        return len([x for x in self.traits if not x.has_tag("Production")])

    @property
    def tier(self) -> int:
        return max([x.tier for x in self] or [0])

    @property
    def attention(self) -> int:
        # base attention from traits
        attention = max([x.attention for x in self] or [0])
        if clinical_testing in self.traits:
            attention -= 1
        attention += self.attention_modifier
        if attention < 0:
            return 0
        return attention

    @property
    def flaws_aspect(self) -> int:
        if self._flaws_aspect < 0:
            return 0
        return self._flaws_aspect

    @flaws_aspect.setter
    def flaws_aspect(self, value: int):
        self._flaws_aspect = value

    @property
    def is_expired(self) -> bool:
        return self.duration_counter >= self.duration

    @property
    def positive_slug(self) -> str:
        return "\n".join([x.positive_slug for x in self if x.positive_slug])

    @property
    def negative_slug(self) -> str:
        return "\n".join([x.negative_slug for x in self if x.negative_slug])

    @property
    def has_production_trait(self) -> bool:
        return any(x for x in self.traits if x.has_tag("Production"))

    @property
    def market_demand(self) -> float:
        return self._market_demand

    @market_demand.setter
    def market_demand(self, value: float):
        # between 30% and 105%
        self._market_demand = min(1.05, value)
        self._market_demand = max(0.3, self._market_demand)

    @property
    def total_duration(self) -> int:
        duration = self.duration
        if self_generating_serum in self.traits:
            duration = (duration * (duration + 1) / 2)
        return builtins.int(duration)

    def can_add_trait(self, trait: SerumTrait):
        if trait in self.traits:
            return False
        return not self.__is_tag_excluded(trait)

    def add_trait(self, trait: SerumTrait):
        if self.can_add_trait(trait):
            self.traits.append(trait)
            self.__apply_trait_side_effects(trait)

    def can_add_side_effect(self, side_effect: SerumTrait):
        if side_effect in self.side_effects:
            return False

        return not self.__is_tag_excluded(side_effect)

    def add_side_effect(self, side_effect: SerumTrait):
        if self.can_add_side_effect(side_effect):
            self.side_effects.append(side_effect)
            self.__apply_trait_side_effects(side_effect)

    def remove_trait(self, trait: SerumTrait):
        if trait in self.traits:
            self.traits.remove(trait)
            self.__remove_trait_side_effects(trait)

        if trait in self.side_effects:
            self.side_effects.remove(trait)
            self.__remove_trait_side_effects(trait)

    def has_trait(self, trait: SerumTrait) -> bool:
        return any(x for x in chain(self.traits, self.side_effects) if x == trait)

    def has_tag(self, the_tag: list[str] | str) -> bool: #Returns true if at least one of the traits has the tag "the_tag". Used to confirm a production trait is included.
        return any(x for x in chain(self.traits, self.side_effects) if x.has_tag(the_tag))

    def has_hidden_tag(self, the_tag: list[str] | str) -> bool: #Returns true if at least one of the traits has the tag "the_tag". Used to confirm a production trait is included.
        return any(x for x in chain(self.traits, self.side_effects) if x.has_hidden_tag(the_tag))

    def change_attention(self, amount: int): # can be used to increase or decrease attention of design
        self.attention_modifier += amount

    def run_on_turn(self, person: Person, add_to_log = False): #Increases the counter, applies serum effect if there is still some duration left
        if self.duration_counter < self.duration:
            for trait in (x for x in self if x.on_turn):
                trait.run_on_turn(person, self, add_to_log)
        if self.expires:
            self.duration_counter += 1

    def run_on_apply(self, person: Person, add_to_log = True):
        self.effects_dict = {} #Ensure this is clear and it isn't a reference to the main dict.
        for trait in (x for x in self if x.on_apply):
            trait.run_on_apply(person, self, add_to_log)

    def run_on_remove(self, person: Person, add_to_log = False):
        # remove strongest traits last by using reversed iterator
        for trait in (x for x in self.__iter_reverse__() if x.on_remove):
            trait.run_on_remove(person, self, add_to_log)

    def run_on_day(self, person: Person, add_to_log = False):
        for trait in (x for x in self if x.on_day):
            trait.run_on_day(person, self, add_to_log)

    def add_research(self, amount: float): #Returns true if "amount" research completes the research
        self.current_research += amount
        if self.current_research >= self.research_needed:
            self.researched = True
            return True
        return False

    def unlock_design(self, pay_clarity = True):
        if pay_clarity:
            mc.spend_clarity(self.clarity_needed)
        self.unlocked = True

    def calculate_side_effect_chance(self, trait: SerumTrait):
        if trait.has_tag("Production"):
            return trait.side_effect_chance

        base_tier = next((x.tier for x in self.traits if x.has_tag("Production")), 0)
        effect_change_modifier = max(trait.tier - base_tier, 0) * 15    # add 15% side effect chance for high tier traits in simple production serum
        return trait.side_effect_chance + effect_change_modifier

    def restore_market_demand(self, value: float):
        self.market_demand += value

    def update_market_demand(self, units_sold: int):
        self.market_demand -= (units_sold / max(300 - (self.tier * self.slots_used * (2 + self.attention)), 2))

    # Called when a serum is finished development.
    # Tests all traits against their side effect chance and adds an effect for any that fail.
    def generate_side_effects(self, add_to_log = True) -> list[SerumTrait]:
        side_effects = []
        for trait in self.traits:
            if renpy.random.randint(0, 100) < self.calculate_side_effect_chance(trait):
                side_effect = self.__create_side_effect(trait.name, add_to_log)
                if side_effect:
                    side_effects.append(side_effect)
        return side_effects

    # Add random side effect to a serum
    def __create_side_effect(self, cause, add_to_log = True) -> SerumTrait | None:
        side_effect = get_random_from_list([x for x in list_of_side_effects if self.can_add_side_effect(x)])
        if side_effect:
            self.add_side_effect(side_effect)
            if add_to_log:
                mc.log_event(f"{self.name} developed side effect {side_effect.name} due to {cause}", "float_text_blue")
        return side_effect

    def __is_tag_excluded(self, trait: SerumTrait) -> bool:
        disallowed_tags = []
        for x in (x.exclude_tags for x in chain(self.traits, self.side_effects)):
            disallowed_tags.extend(x)
        return any(x for x in trait.exclude_tags if x in disallowed_tags)

    def __apply_trait_side_effects(self, trait: SerumTrait):
        self.research_needed += trait.research_added
        self.clarity_needed += trait.clarity_added
        self.slots += trait.slots
        self.production_cost += trait.production_cost
        self.duration += trait.duration

        self.mental_aspect += trait.mental_aspect
        self.physical_aspect += trait.physical_aspect
        self.sexual_aspect += trait.sexual_aspect
        self.medical_aspect += trait.medical_aspect
        self._flaws_aspect += trait.flaws_aspect

    def __remove_trait_side_effects(self, trait: SerumTrait):
        self.research_needed -= trait.research_added
        self.clarity_needed -= trait.clarity_added
        self.slots -= trait.slots
        self.production_cost -= trait.production_cost
        self.duration -= trait.duration

        self.mental_aspect -= trait.mental_aspect
        self.physical_aspect -= trait.physical_aspect
        self.sexual_aspect -= trait.sexual_aspect
        self.medical_aspect -= trait.medical_aspect
        self._flaws_aspect -= trait.flaws_aspect
