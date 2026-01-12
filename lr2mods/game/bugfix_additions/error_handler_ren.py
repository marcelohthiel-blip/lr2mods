from __future__ import annotations
import renpy
from game.bugfix_additions.debug_info_ren import write_log
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""

class LabelNotFountErrorHandler():
    """
    Handles error in game when return label not found.
    Mostly caused by loading a save game that was taken during an crisis event
    """

    def __init__(self):
        self.target_depth = renpy.call_stack_depth()

    def __call__(self, short, full, traceback_fn):
        write_log(short)
        if "Could not find return label" in short:

            renpy.jump("game_loop")

renpy.config.exception_handler = LabelNotFountErrorHandler()
