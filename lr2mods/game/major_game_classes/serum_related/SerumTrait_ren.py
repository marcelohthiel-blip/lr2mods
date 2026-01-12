from __future__ import annotations
import builtins
from functools import cached_property
from typing import Callable, Iterable
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.main_character.MainCharacter_ren import mc, Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign

list_of_traits: list[SerumTrait]
list_of_side_effects: list[SerumTrait]
list_of_nora_traits: list[SerumTrait]
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

class SerumTrait():
    def __init__(self, name: str, desc: str, positive_slug = "", negative_slug = "",
            research_added = 0, slots_added = 0, production_added = 0, duration_added = 0, base_side_effect_chance = 0, clarity_added = 0,
            on_apply: Callable[[Person, SerumDesign, bool], None] | None = None,
            on_remove: Callable[[Person, SerumDesign, bool], None] | None = None,
            on_turn: Callable[[Person, SerumDesign, bool], None] | None = None,
            on_day: Callable[[Person, SerumDesign, bool], None] | None = None,
            requires: list[SerumTrait] | SerumTrait | None = None,
            tier = 0, start_researched = False, research_needed=50, exclude_tags=None, is_side_effect = False,
            clarity_cost = 50, start_unlocked = False,
            mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0,
            nora_trait = False, hidden_tag = "Medical"):

        # Display info #
        self.name = name
        self.desc = desc #A fluff text description.
        self._positive_slug = positive_slug #A short numerical list of positive effects
        self._negative_slug = negative_slug #The negative costs

        # Serum trait values #
        self.research_added = research_added
        self.slots = slots_added
        self.production_cost = production_added
        self.duration = duration_added
        self.base_side_effect_chance = base_side_effect_chance #A percentage chance that this trait will introduce a side effect to the finished design.
        self.mastery_level = 1.0 #The amount of experience the MC has with this serum. Divide base side effect chance by mastery level to get effective side effect chance.
        self.clarity_added = clarity_added #Amount of Clarity added to the serum design when it will be made.

        # Serum trait effects #
        self.on_apply = on_apply #The function applied to the person when the serum is first applied.
        self.on_remove = on_remove #The function applied to the person when the serum is removed (it should generally undo the on_apply effects)
        self.on_turn = on_turn #The function applied to the person at the end of a turn under the effect of the serum. Effectively "End" of turn.
        self.on_day = on_day #The function applied to the person at the end of the day.

        # Research details #
        if requires is None: #A list of other traits that must be researched before this.
            self.requires = []
        elif isinstance(requires, list):
            self.requires = requires
        else:
            self.requires = [requires]

        self.tier = tier #The tier of research that the business must have unlocked to research this, in addition to the other prerequisites.
        self.researched = start_researched
        self.research_needed = research_needed
        self.current_research = 0.0

        self.clarity_cost = clarity_cost #How much clarity has to be spent to unlock this trait before it can be researched.
        self.unlocked = start_unlocked or start_researched #Only unlocked traits can be researched

        if exclude_tags is None:    #A list of tags (strings) that this trait cannot be paired with. If a trait has the same excluded tag this cannot be added to a trait.
            self.exclude_tags = []
        elif isinstance(exclude_tags, list):
            self.exclude_tags = exclude_tags
        else:
            self.exclude_tags = [exclude_tags]

        self.is_side_effect = is_side_effect #If true this trait is a side effect and not counted towards serum max traits and such. It also cannot be added to a serum on purpose.

        self.mental_aspect = mental_aspect
        self.physical_aspect = physical_aspect
        self.sexual_aspect = sexual_aspect
        self.medical_aspect = medical_aspect
        self.flaws_aspect = flaws_aspect
        self.attention = attention
        self.nora_trait = nora_trait
        self.hidden_tag = hidden_tag
        self.identifier = generate_identifier(name)

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: SerumTrait) -> bool:
        if not isinstance(other, SerumTrait):
            return NotImplemented
        return self.name == other.name

    def is_similar(self, other: SerumTrait) -> bool: #Returns True if these two traits are near-identical, even if they aren't the same object (primarily for dynamic traits like breast milk)
        if not isinstance(other, SerumTrait):
            return False

        return (self.desc == other.desc
            and self.on_apply == other.on_apply
            and self.on_remove == other.on_remove
            and self.on_turn == other.on_turn
            and self.researched == other.researched
            and self.is_side_effect == other.is_side_effect
            and self.mental_aspect == other.mental_aspect
            and self.physical_aspect == other.physical_aspect
            and self.sexual_aspect == other.sexual_aspect
            and self.medical_aspect == other.medical_aspect
            and self.flaws_aspect == other.flaws_aspect
            and self.attention == other.attention)

    def run_on_apply(self, person: Person, serum: SerumDesign, add_to_log = True):
        if self.on_apply:
            self.on_apply(person, serum, add_to_log)

    def run_on_remove(self, person: Person, serum: SerumDesign, add_to_log = False):
        if self.on_remove:
            self.on_remove(person, serum, add_to_log)

    def run_on_turn(self, person: Person, serum: SerumDesign, add_to_log = False):
        if self.on_turn:
            self.on_turn(person, serum, add_to_log)

    def run_on_day(self, person: Person, serum: SerumDesign, add_to_log = False):
        if self.on_day:
            self.on_day(person, serum, add_to_log)

    def add_research(self, amount: float) -> bool:
        self.current_research += amount
        if self.current_research >= self.research_needed:
            if self.researched:
                while self.current_research >= self.research_needed: #For large businesses when the research produced is much larger than the total research needed you can gain multiple levels.
                    self.add_mastery(0.5)
                    self.current_research -= self.research_needed
            else:
                self.current_research -= self.research_needed
            self.researched = True

            return True
        return False

    def unlock_trait(self, pay_clarity = True) -> SerumTrait:
        if pay_clarity:
            mc.spend_clarity(self.clarity_cost)
        self.unlocked = True
        return self #Return self so we can unlock and set as selected research as an atomic action in research UI.

    def add_mastery(self, amount: float) -> bool:
        if self.mastery_level < 100:
            self.mastery_level = min(100.0, self.mastery_level + amount)
            return True
        return False

    @property
    def side_effect_chance(self): #Generates the effective side effect chance percent as an integer.
        the_chance = self.base_side_effect_chance / max(self.mastery_level, 1)
        return builtins.int(the_chance)

    @cached_property
    def negative_slug(self) -> str:
        return_slug = []

        if self._negative_slug:
            return_slug.append(self._negative_slug)

        if self.production_cost > 0:
            return_slug.append(f"+{self.production_cost} Production/Batch")

        if self.research_added > 0:
            return_slug.append(f"+{self.research_added} Serum Research")

        if self.clarity_added > 0:
            return_slug.append(f"+{self.clarity_added} Clarity to Unlock")

        if self.is_side_effect and self.flaws_aspect != 0:
            return_slug.append(f"+{self.flaws_aspect} Flaws")

        return "\n".join(return_slug)

    @property
    def positive_slug(self) -> str:
        return_slug = []
        if self._positive_slug:
            return_slug.append(self._positive_slug)
        return "\n".join(return_slug)

    @property
    def is_unlocked(self) -> bool:
        if self.tier > mc.business.research_tier:
            return False
        if self.requires and any(x for x in self.requires if isinstance(x, SerumTrait) and not x.researched):
            return False
        return True

    def has_tag(self, tags: Iterable[str] | str) -> bool:
        if isinstance(tags, str):
            return tags in self.exclude_tags
        if isinstance(tags, (list, tuple, set)):
            return any(x for x in tags for x in self.exclude_tags)
        return False

    def has_hidden_tag(self, tags: Iterable[str] | str) -> bool:
        if isinstance(tags, str):
            return tags in self.hidden_tag
        if isinstance(tags, (list, tuple, set)):
            return any(x for x in tags for x in self.hidden_tag)
        return False

    def mastery_range(self, low_score: int, high_score: int) -> int:    #Returns an int with a score between the two scores based on serum mastery
        if low_score == high_score:
            return low_score
        if low_score > high_score:
            low_score, high_score = high_score, low_score
        score_range = high_score - low_score
        return int(round(
            ((score_range * self.mastery_level) / 100) + low_score
        ))

    def mastery_range_inverted(self, low_score: int, high_score: int) -> int:    #Returns an int with a score between the two scores based on serum mastery
        if low_score == high_score:
            return low_score
        if low_score > high_score:
            low_score, high_score = high_score, low_score
        score_range = high_score - low_score
        return int(round(
            high_score - ((score_range * self.mastery_level) / 100)
        ))
