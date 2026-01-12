from __future__ import annotations
import builtins
from game.game_roles._role_definitions_ren import heavy_trance_role, very_heavy_trance_role
from game.main_character.mc_serums._mc_serum_definitions_ren import mc, Person, mc_serum_feat_hypnotist

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class Trainable():
    def __init__(self, short_name: str, on_train_label, display_name = None, base_cost = 100, unlocked_function = None, extra_args = None, doubling_amount = 2.0, training_tag = None):
        self.short_name = short_name #A short word to be used for lists and logs, but not necessarily for display. Should be unique.
        self.on_train_label = on_train_label #A Ren'py label that is called with the person as an argument (as well as any extra args) when this is bought.
        #on_train_effect should encapsulate all effects except for paying the Clarity cost.

        if display_name is None: #display_name is a long form name used for buttons.
            self.display_name = self.short_name
        else:
            self.display_name = display_name

        self.base_cost = base_cost #Starting clarity cost before she has been trained in this before.

        self.unlocked_function = unlocked_function #A python function called to check if this trainable should be displayed. It will be passed the person and any extra args.

        if extra_args is None: #Extra arguments passed through to the train label and the unlocked function to make it easier to reuse the same base functionality.
            self.extra_args = []
        elif isinstance(extra_args, list):
            self.extra_args = extra_args
        else:
            self.extra_args = [extra_args]

        self.doubling_amount = doubling_amount * 1.0 #The cost of training this thing doubles every time it has been trained doubling_amount already.

        if training_tag is None: #Training tag is used to record how often a similar thing has been trained and increase all of their costs together.
            self.training_tag = self.short_name
        else:
            self.training_tag = training_tag

    def __hash__(self) -> int:
        return hash((self.short_name, self.on_train_label))

    def __eq__(self, other: Trainable) -> bool:
        if not isinstance(other, Trainable):
            return NotImplemented
        return (self.short_name, self.on_train_label) == (other.short_name, other.on_train_label)

    def get_cost(self, person: Person) -> int:
        base_modified_cost = self.base_cost * (2**(person.training_log[self.training_tag] / self.doubling_amount))
        base_modified_cost = min((self.base_cost * 4), base_modified_cost)
        trance_modifier = 2.0
        if person.has_exact_role(heavy_trance_role):
            trance_modifier = 1.0
        elif person.has_exact_role(very_heavy_trance_role):
            trance_modifier = 0.5

        if mc_serum_feat_hypnotist.is_active:
            if mc_serum_feat_hypnotist.trait_tier == 2:
                trance_modifier = trance_modifier * 0.8
            elif mc_serum_feat_hypnotist.trait_tier >= 3:
                trance_modifier = trance_modifier * 0.6

        return builtins.int(base_modified_cost * trance_modifier)

    def can_be_trained(self, person: Person) -> bool:
        if not callable(self.unlocked_function):
            return True
        return self.unlocked_function(person, *self.extra_args)

    def is_valid_trainnee(self, person: Person):
        if callable(self.unlocked_function):    # not unlocked
            value = self.unlocked_function(person, *self.extra_args)
            if value is False or isinstance(value, str):
                return False

        # can we use it?
        return mc.free_clarity >= self.get_cost(person)
