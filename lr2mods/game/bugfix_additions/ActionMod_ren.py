from __future__ import annotations
from typing import Callable
import renpy
from game.major_game_classes.game_logic.ActionList_ren import ActionList
from game.major_game_classes.game_logic.Action_ren import Action
from game.main_character.MainCharacter_ren import mc

action_mod_list: list[ActionMod] = []
crisis_list: ActionList = []
morning_crisis_list: ActionList = []
limited_time_event_pool: ActionList = []

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def init_action_mod_disabled(action_mod):
    action_mod.enabled = False

class ActionMod(Action):
    @staticmethod
    def is_mod_enabled(action: ActionMod | str) -> bool:
        found = None
        if isinstance(action, ActionMod):
            found = next((x for x in action_mod_list if x == action), None)
        if isinstance(action, str):
            found = next((x for x in action_mod_list if x.effect == action), None)
        if found:
            return found.enabled
        return False

    _instances: set[ActionMod] = set()

    # store instances of mod
    def __init__(self, name: str, requirement: Callable[[], bool], effect: str, args = None, requirement_args = None, menu_tooltip: str | None = None, priority: int = 10, event_duration: int = 99999, is_fast: bool = True,
            initialization: Callable[['ActionMod'], None] = None, category: str = "Misc", allow_disable: bool = True, on_enabled_changed: Callable[[bool], None] = None, options_menu = None,
            is_crisis: bool = False, is_morning_crisis: bool = False, is_mandatory_crisis: bool = False):

        super().__init__(name, requirement, effect, args, requirement_args, menu_tooltip, priority, event_duration, is_fast)

        self.initialization = initialization
        self.category = category
        self.enabled = True                             # default to enabled (if not available at start use init_action_mod_disabled or any other initialize method that sets this to False)
        self.allow_disable = allow_disable
        self.on_enabled_changed = on_enabled_changed
        self.options_menu = options_menu
        self.is_crisis = is_crisis                      # chance to trigger during day
        self.is_morning_crisis = is_morning_crisis      # chance to trigger early morning
        self.is_mandatory_crisis = is_mandatory_crisis  # only triggered once when requirements are met

        ActionMod._instances.add(self)

    def initialize(self):
        if callable(self.initialization):
            self.initialization(self)

    def show_options(self):
        if self.options_menu and renpy.has_label(self.options_menu):
            renpy.call(self.options_menu)

    def toggle_enabled(self):
        self.enabled = not self.enabled
        # trigger event
        if callable(self.on_enabled_changed):
            self.on_enabled_changed(self.enabled)

        # update in game crisis lists ()
        if self.is_crisis:
            def _update_crisis(cl, action):
                found = next((x for x in cl if x == action), None)
                if found and not action.enabled:
                    cl.remove(found)
                if not found and action.enabled:
                    cl.append(action)

            if not self.is_morning_crisis:
                _update_crisis(crisis_list, self)

            if self.is_morning_crisis:
                _update_crisis(morning_crisis_list, self)

        if self.is_mandatory_crisis:
            def _update_mandatory_crisis(cl, action, add_func, remove_func):
                found = next((x for x in cl if x == action), None)
                if found and not action.enabled:
                    remove_func(action)
                if not found and action.enabled:
                    add_func(action)

            if "mc" in globals() and not self.is_morning_crisis:
                _update_mandatory_crisis(mc.business.mandatory_crises_list, self, mc.business.add_mandatory_crisis, mc.business.remove_mandatory_crisis)

            if "mc" in globals() and self.is_morning_crisis:
                _update_mandatory_crisis(mc.business.mandatory_morning_crises_list, self, mc.business.add_mandatory_morning_crisis, mc.business.remove_mandatory_crisis)
