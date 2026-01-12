from __future__ import annotations
from typing import Callable
from game.major_game_classes.character_related.Person_ren import Person

debug_log_enabled = True
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""

# This file is used for defining outfit_actions
# These are similar to game actions, but take a person and their outfit as arguments to make general changes
# Outfit Actions have unlock requirements as well as item availability requirements
# Outfit Actions are designed to automatically modify a girls outfit to meet requirements that MC sets out for them
# These actions can be attached to specific girls at specific places to provide an additional layer of outfit control and customization
# EG: Force head researcher to wear a lab coat

class Outfit_Action():
    def __init__(self, name: str, requirement: Callable, effect: Callable,
            menu_tooltip: str | None = None, tag: str | None = "pants", exclusive_tags: list | None = None):
        self.name = name

        # A requirement returns False if the action should be hidden, a string if the action should be disabled but visible (the string is the reason it is not enabled), and True if the action is enabled
        self.requirement = requirement #Requirement is a function that determines if the action is available.

        self.effect = effect #effect is a function that changes the outfit in some way
        self.menu_tooltip = menu_tooltip # A string added to any menu item where this action is displayed
        self.tag = tag #A string used for determining which category this action is in, EG "dress", "shoes", "bra"
        self.exclusive_tags = exclusive_tags #A list of tags that this tag is incompatible with. EG, a "dress" would not be compatible with "skirt"

    def __hash__(self) -> int:
        return hash(self.requirement, self.effect)

    def __eq__(self, other: Outfit_Action) -> bool:
        if not isinstance(other, Outfit_Action):
            return NotImplemented
        return self.requirement == other.requirement and self.effect == other.effect

    def check_requirement(self, person: Person): #Calls the requirement function associated with this action. Requires the person
        # Effectively private. Use "is_action_enabled" and "is_disabled_slug_shown" to figure out if there are important actions to display or take.
        if person is None:
            return False
        return self.requirement(person)


# def outfit_action_wear_lab_coat(person):
