from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
# sub class for fetish actions
# this is a type we can check to add extra restrictions / functionality in other parts of the game
# for instance limit the mandatory event trigger to one fetish event per time-slot
class Fetish_Action(Action):
    def __init__(self, name, requirement, effect, args = None, requirement_args = None,
                 menu_tooltip = None, priority = 0, event_duration = 99999, fetish_type = None):

        super().__init__(name, requirement, effect, args, requirement_args, menu_tooltip, priority, event_duration)

        self.fetish_type = fetish_type
