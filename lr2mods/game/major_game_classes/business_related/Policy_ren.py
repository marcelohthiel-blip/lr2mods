from __future__ import annotations
from typing import Callable
from game.bugfix_additions.mapped_list_ren import MappedList, generate_identifier
from game.helper_functions.list_functions_ren import all_policies_in_the_game
from game.main_character.MainCharacter_ren import mc
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -20 python:
"""
class Policy(): # An upgrade that can be purchased by the character for their business.
    def __init__(self, name: str, desc: str, cost: int,
            requirement: Callable[[], bool] = None,
            own_requirement: list['Policy'] | 'Policy' | None = None,
            active_requirement: list['Policy'] | 'Policy' | None = None,
            toggleable = False, exclusive_tag: str = None,
            on_buy_function: Callable = None, extra_arguments = None,
            on_apply_function: Callable[[], None] = None,
            on_remove_function: Callable = None,
            on_turn_function: Callable = None,
            on_move_function: Callable = None,
            on_day_function: Callable = None,
            dependant_policies: list['Policy'] | 'Policy' | None = None,
            extra_data = None):

        self.name = name #A short name for the policy.
        self.desc = desc #A text description of the policy.
        self.requirement = requirement #a function that is run to see if the PC can purchase this policy.
        if own_requirement is None:
            self.own_requirement = [] #List of other policies that need to be owned for this policy to be available.
        elif isinstance(own_requirement, Policy):
            self.own_requirement = [own_requirement]
        else:
            self.own_requirement = own_requirement

        if active_requirement is None:
            self.active_requirement = [] #List of other policies that need to be active for this policy to be available.
        elif isinstance(active_requirement, Policy):
            self.active_requirement = [active_requirement]
        else:
            self.active_requirement = active_requirement

        self.cost = cost #Cost in dollars.

        self.toggleable = toggleable #If True this policy can be toggled on and off. Otherwise, it is set "active" when bought and can never be deactivated.

        if extra_arguments is None:
            self.extra_arguments = {}
        else:
            self.extra_arguments = extra_arguments #A dictionary of extra values that can be used by the various on_buy, on_apply, etc. functions

        if extra_data is None:
            self.extra_data = {}
        else:
            self.extra_data = extra_data #A dictionary of extra data to be accessed

        self.on_buy_function = on_buy_function #A function to be called when purchased
        self.on_apply_function = on_apply_function
        self.on_remove_function = on_remove_function
        self.on_turn_function = on_turn_function #These functions are applied to anyone with the Employee role. Policies that affect people with specific sub-roles
        self.on_move_function = on_move_function
        self.on_day_function = on_day_function
        self.exclusive_tag = exclusive_tag
        self.identifier = generate_identifier(name)

        if dependant_policies is None:
            self.dependant_policies = []
        elif isinstance(dependant_policies, Policy):
            self.dependant_policies = [dependant_policies] #If we hand a single item wrap it in a list for iteration purposes
        else:
            self.dependant_policies = dependant_policies # Otherwise we have a list already.

        self.depender_policies = MappedList(Policy, all_policies_in_the_game) #These policies depend _on_ us, and are declared when other policies are defined. If they are on, we cannot toggle off.
        for policy in self.dependant_policies:
            policy.depender_policies.append(self) #Essentially builds a two way linked list of policies while allowing us to only define the requirements from the base up. Also conveniently stops dependency cycles from forming.

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Policy) -> bool:
        if not isinstance(other, Policy):
            return NotImplemented
        return self.name == other.name

    @property
    def is_owned(self) -> bool:
        return self in mc.business.policy_list

    @property
    def is_active(self) -> bool:
        return self in mc.business.active_policy_list

    @property
    def is_toggleable(self) -> bool:
        return_toggle = True
        if self.is_owned and self.toggleable: #If a policy is supposed to be toggleable:
            if self in mc.business.active_policy_list: # We are currently active, so we are only disable-able if all of the dependers are off.
                for policy in self.depender_policies:
                    if policy.is_active: #If any of the policies that rely on this are active we cannot toggle off.
                        return_toggle = False

            else: # We are owned but not active. We can only be toggled if every policy in our dependant list is active
                for policy in self.dependant_policies:
                    if not policy.is_active:
                        return_toggle = False

        else:
            return_toggle = False

        return return_toggle

    @property
    def requirement_met(self) -> bool:
        for policy in self.own_requirement:
            if not policy.is_owned:
                return False

        for policy in self.active_requirement:
            if not policy.is_active:
                return False

        if not callable(self.requirement):
            return True

        requirement_return = self.requirement()
        if isinstance(requirement_return, str) or not requirement_return:
            return False
        return True

    def buy_policy(self, ignore_cost = False):
        mc.business.policy_list.append(self)
        if not ignore_cost:
            mc.business.change_funds(-self.cost, stat = "Policies")
        if self.on_buy_function is not None:
            self.on_buy_function(**self.extra_arguments)

    def apply_policy(self):
        mc.business.active_policy_list.append(self)
        if self.on_apply_function is not None:
            self.on_apply_function(**self.extra_arguments)

    def remove_policy(self):
        if self in mc.business.active_policy_list:
            mc.business.active_policy_list.remove(self)
            if self.on_remove_function is not None:
                self.on_remove_function(**self.extra_arguments)

    def on_turn(self):
        if self.on_turn_function is not None:
            self.on_turn_function(**self.extra_arguments)

    def on_move(self):
        if self.on_move_function is not None:
            self.on_move_function(**self.extra_arguments)

    def on_day(self):
        if self.on_day_function is not None:
            self.on_day_function(**self.extra_arguments)

    @property
    def requirement_string(self) -> str:
        if self.requirement_met:
            return ""

        purchase_req = []
        if self.own_requirement:
            for policy in self.own_requirement:
                if not policy.is_owned:
                    purchase_req.append(policy.name)

        if self.active_requirement:
            for policy in self.active_requirement:
                if not policy.is_active:
                    purchase_req.append(policy.name)

        if callable(self.requirement):
            requirement_return = self.requirement()
            if isinstance(requirement_return, str):
                purchase_req.append(requirement_return)

        if purchase_req:
            return f"Requires: {', '.join(purchase_req)}"

        return ""
