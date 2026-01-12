## A duty is similar to a Role, but it's mechanics are controlled by the business.
# -> Duties are given to employees of the MC's business, capped at that employees seniority level.
# -> Seniority levels are 1(intern, green employee), 2 (standard employee), 3(senior employee, department head).
# -> Duties are checked to add role actions/dates/interactions in the same way as roles.
from __future__ import annotations
from typing import Callable
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.Action_ren import Action

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
class Duty():
    def __init__(self, duty_name: str, duty_description: str, requirement_function: Callable[[Person], bool] | None = None,
            actions: list[Action] | None = None, internet_actions: list[Action] | None = None,
            on_turn_function: Callable[[Person], None] | None = None, on_move_function: Callable[[Person], None] | None = None, on_day_function: Callable[[Person], None] | None = None,
            on_apply_function: Callable[[Person], None] | None = None, on_remove_function: Callable[[Person], None] | None = None,
            duty_trainables = None, only_at_work = True):

        #TODO: Have a "smalltalk" label that can be called whenever you talk to a girl, she'll talk to you about her recent duties and what that entails.
        #TODO: Have an "on entrance" label that can be called instead of the generic greetings when you enter the room so it can tie into their active duties.

        self.duty_name = duty_name  #A short slug that can be shown in a menu, UI, etc.
        self.duty_description = duty_description # A paragraph to describe what this duty is, both flavour and effect
        self.actions = ActionList(actions)
        self.internet_actions = ActionList(internet_actions)

        self.requirement_function = requirement_function

        self.on_turn_function = on_turn_function
        self.on_move_function = on_move_function
        self.on_day_function = on_day_function

        self.on_apply_function = on_apply_function
        self.on_remove_function = on_remove_function

        self.only_at_work = only_at_work # Only run on_turn, on_move only when the employee is at work. Only run on_day when the employee went to work that day.

        if duty_trainables is None:
            self.duty_trainables = []
        elif isinstance(duty_trainables, list):
            self.duty_trainables = duty_trainables
        else:
            self.duty_trainables = [duty_trainables]
        self.identifier = generate_identifier((self.duty_name,
                self.requirement_function,
                self.on_turn_function,
                self.on_move_function,
                self.on_day_function,
                self.on_apply_function,
                self.on_remove_function,
                self.only_at_work))

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Duty) -> bool:
        if not isinstance(other, Duty):
            return NotImplemented
        return (self.duty_name, self.requirement_function, self.on_turn_function, self.on_move_function,
                self.on_day_function, self.on_apply_function, self.on_remove_function, self.only_at_work) == \
            (other.duty_name, other.requirement_function, other.on_turn_function, other.on_move_function,
             other.on_day_function, other.on_apply_function, other.on_remove_function, other.only_at_work)

    def check_requirement(self, person: Person):
        if callable(self.requirement_function):
            return self.requirement_function(person)
        return True

    def on_turn(self, person: Person):
        if callable(self.on_turn_function):
            self.on_turn_function(person)

    def on_move(self, person: Person):
        if callable(self.on_move_function):
            self.on_move_function(person)

    def on_day(self, person: Person):
        if callable(self.on_day_function):
            self.on_day_function(person)

    def on_apply(self, person: Person):
        if callable(self.on_apply_function):
            self.on_apply_function(person)

    def on_remove(self, person: Person):
        if callable(self.on_remove_function):
            self.on_remove_function(person)

    def add_action(self, action: Action):
        self.actions.add_action(action)

    def remove_action(self, action: Action | str):
        self.actions.remove_action(action)

    def add_internet_action(self, action: Action):
        self.internet_actions.add_action(action)

    def remove_internet_action(self, action: Action | str):
        self.internet_actions.remove_action(action)
