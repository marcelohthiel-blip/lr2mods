from __future__ import annotations
from typing import Callable
import renpy
from game.bugfix_additions.debug_info_ren import add_to_debug_log
from game.helper_functions.convert_to_string_ren import remove_display_tags

debug_log_enabled = True
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
import time

class Action(): #Contains the information about actions that can be taken in a room. Displayed when you are asked what you want to do somewhere.
    # Also used for crises, those are not related to any particular room and are not displayed in a list. They are forced upon the player when their requirement is met.
    def __init__(self, name: str, requirement: Callable, effect, args = None, requirement_args = None,
            menu_tooltip: str | None = None, priority: int = 0, event_duration: int = 99999,
            is_fast: bool = True, trigger: str | None = None, silent = False):
        self.name = name

        # A requirement returns False if the action should be hidden, a string if the action should be disabled but visible (the string is the reason it is not enabled), and True if the action is enabled
        self.requirement = requirement #Requirement is a function that is called when the action is checked.

        self.effect = effect #effect is a string for a renpy label that is called when the action is taken.
        if args is None:
            self.args = [] #stores any arguments that we want passed to the action or requirement when the action is created. Should be a list of variables.
        elif not isinstance(args, list):
            self.args = [args] #Make sure our list of arguments is a list.
        else:
            self.args = args

        if requirement_args is None:
            self.requirement_args = [] #A list of arguments handed to the requirement but not the actual event.
        elif not isinstance(requirement_args, list):
            self.requirement_args = [requirement_args]
        else:
            self.requirement_args = requirement_args

        self.enabled = True
        self.menu_tooltip = menu_tooltip # A string added to any menu item where this action is displayed
        self.priority = priority #Used to order actions when displayed in a list. Higher priority actions are displayed before lower ones, and disabled actions are shown after enabled actions.

        self.event_duration = event_duration # Used for actions turned into limited time actions as the starting duration.

        self.is_fast = is_fast #A "fast" event is one that can never result in a time change. A "slow" event that has the potential to cause a time jump, and might not be allowed in some time sensitive situations.
        self.trigger = trigger #For limited time actions either 'on_talk' or 'on_enter' use priority for weighted chance
        self.silent = silent # A silent event has no user interaction (just executes some changes) or must now show up on map

    def __hash__(self) -> int:
        return hash(tuple([self.requirement, self.effect] + self.args))

    def __eq__(self, other: Action) -> bool:
        if not isinstance(other, Action):
            return NotImplemented
        return (self.requirement, self.effect, self.args, self.name) == (other.requirement, other.effect, other.args, other.name)

    def check_requirement(self, extra_args = None): #Calls the requirement function associated with this action.
        # Effectively private. Use "is_action_enabled" and "is_disabled_slug_shown" to figure out if there are important actions to display or take.
        if extra_args is None: #We need to make sure we package all potential extra args as a list and hand them over.
            extra_args = []
        elif isinstance(extra_args, (tuple, set)):
            extra_args = list(extra_args)
        elif not isinstance(extra_args, list):
            extra_args = [extra_args]
        extra_args = extra_args + self.requirement_args
        return self.requirement(*extra_args)

    def is_action_enabled(self, extra_args = None) -> bool:
        if not self.enabled:
            return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, str):
            # Any string returned means the action is not enabled
            return False
        # If it's not a string it must be a bool
        return requirement_return

    def is_disabled_slug_shown(self, extra_args = None) -> bool: # Returns true if this action is not enabled but should show something when it is disabled.
        if not self.enabled:
            return False

        requirement_return = self.check_requirement(extra_args)
        if isinstance(requirement_return, str):
            return True
        return False

    def get_disabled_slug_name(self, extra_args = None) -> str: #Returns a formatted name for when the
        requirement_return = self.check_requirement(extra_args)
        return f"{self.name}\n{{menu_red=16}}{requirement_return}{{/menu_red}} (disabled)"

    def call_action(self, extra_args = None): #Can only use global variables. args is a list of elements you want to include as arguments. None is default
        if extra_args is None:
            extra_args = []
        elif not isinstance(extra_args, list):
            extra_args = [extra_args]

        # run extension code
        if debug_log_enabled:
            add_to_debug_log(f"Action: {remove_display_tags(self.name)} ({{total_time:.3f}})", time.time())

        renpy.exports.call(self.effect, *(self.args + extra_args))

    def update(self, action):
        if isinstance(action, Action):
            self.name = action.name
            self.requirement = action.requirement
            self.effect = action.effect
            self.args = action.args
            self.requirement_args = action.requirement_args
            self.menu_tooltip = action.menu_tooltip
            self.priority = action.priority
            self.event_duration = action.event_duration
            self.is_fast = action.is_fast

class Limited_Time_Action(Action):
    def __init__(self, action: Action):
        super().__init__(
            action.name,
            action.requirement,
            action.effect,
            action.args,
            action.requirement_args,
            action.menu_tooltip,
            action.priority,
            action.event_duration,
            action.is_fast,
            action.trigger,
            action.silent)

        self.turns_valid = action.event_duration
