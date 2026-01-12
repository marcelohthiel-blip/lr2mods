# internal class to  handle list of actions
from __future__ import annotations
from collections.abc import Iterator
from typing import Iterable
from game.bugfix_additions.debug_info_ren import write_log
from game.major_game_classes.game_logic.Action_ren import Action
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
class ActionList():
    def __init__(self, actions: Iterable[Action] | ActionList | Action | None = None) -> None:
        self._actions: list[Action] = []
        if isinstance(actions, ActionList):
            self._actions = actions._actions[:]
        if isinstance(actions, (list, tuple, set)):
            for x in actions:
                self.add_action(x)
        if isinstance(actions, Action):
            self.add_action(actions)

    def __getitem__(self, key):
        if isinstance(key, slice):
            #Get the start, stop, and step from the slice
            return [self[ii] for ii in range(*key.indices(len(self)))]
        if isinstance(key, int):
            if key < 0: #Handle negative indices
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError
            return self._actions[key]
        raise TypeError

    def __repr__(self) -> str:
        return repr(self._actions)

    def __call__(self):
        return self._actions

    def __iter__(self) -> Iterator[Action]:
        return iter(self._actions)

    def __len__(self) -> int:
        return len(self._actions)

    def __contains__(self, action: Action) -> bool:
        found = self.find(action)
        return found is not None

    def __add__(self, action: Action):
        if isinstance(action, ActionList):
            return self.__class__(self._actions + action._actions)
        if isinstance(action, list):
            return self.__class__(self._actions + action)
        if isinstance(action, Action):
            return self.__class__(self._actions + [action])
        return self

    def __radd__(self, action: Action):
        if isinstance(action, ActionList):
            return self.__class__(action._actions + self._actions)
        if isinstance(action, list):
            return self.__class__(action + self._actions)
        if isinstance(action, Action):
            return self.__class__([action] + self._actions)
        return self

    def __iadd__(self, action: Action):
        if isinstance(action, ActionList):
            self._actions += action._actions
        elif isinstance(action, (list, tuple, set)):
            for x in action:
                self.add_action(x)
        else:
            self.add_action(action)
        return self

    def __sub__(self, action: Action):
        self.remove_action(action)

    def __isub__(self, action: Action):
        self.remove_action(action)
        return self

    def append(self, action: Action):
        self.add_action(action)

    def remove(self, action: Action):
        self.remove_action(action)

    def clear(self):
        self._actions.clear()

    def copy(self):
        return self.__class__(self)

    def extend(self, other: Action | list[Action] | ActionList) -> None:
        if isinstance(other, ActionList):
            self._actions.extend(other._actions)
        elif isinstance(other, (list, tuple, set)):
            for x in other:
                self.add_action(x)
        elif isinstance(other, Action):
            self.add_action(other)

    def pop(self, index = -1):
        return self._actions.pop(index)

    def index(self, action: Action):
        if found := self.find(action):
            return self._actions.index(found)
        raise ValueError

    def find(self, action: Action):
        if isinstance(action, Action):
            return next((x for x in self._actions if x == action), None)
        return None

    def add_action(self, action: Action):
        '''
        Adds passed action to list if it not already exists in the list
        '''
        if not isinstance(action, Action):
            write_log(f"Passed object to ActionList.add_action is not an Action object, but a {type(action).__name__}")
            return

        found = self.find(action)
        if not found:
            self._actions.append(action)
        else:
            found.update(action)

    def remove_action(self, action: Action | str):
        '''
        Removes passed action (or label name) from action list
        '''
        found = None
        if isinstance(action, Action):
            found = self.find(action)
        if isinstance(action, str):
            found = next((x for x in self._actions if x.effect == action), None)
        if found:
            self._actions.remove(found)

    def enabled_actions(self, extra_args = None) -> list[Action]:
        '''
        List of actions that have their requirements met
        '''
        return [x for x in self._actions if x.is_action_enabled(extra_args)]

    def has_action(self, action: Action | str) -> bool:
        '''
        Returns True when action of label name exists in list
        '''
        found = None
        if isinstance(action, Action):
            found = self.find(action)
        if isinstance(action, str):
            found = next((x for x in self._actions if x.effect == action), None)
        return found is not None
