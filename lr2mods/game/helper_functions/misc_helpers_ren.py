from __future__ import annotations
from typing import Any
from renpy.color import Color
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, report_log
import math
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
from functools import lru_cache

def get_coloured_arrow(direction):
    if direction < 0:
        return "{image=gui/heart/Red_Down.png}"
    if direction > 0:
        return "{image=gui/heart/Green_Up.png}"
    return "{image=gui/heart/Grey_Steady.png}"

def last_position_used():
    if "report_log" in globals() and isinstance(report_log, dict):
        return report_log.get("last_position", None)
    return None

def round_to_nearest(value, nearest: int = 1000) -> int:
    '''
     round to 1000 is default, use 100 or 10 for different rounding
    '''
    if nearest == 0:
        nearest = 10
    return int(round(value / (nearest * 1.0))) * nearest

def lighten_colour(current_colour_raw: list[float], factor: float = .07) -> Color | None:
    '''
    Creates a tint of passed color by mixing it with white. `factor` is
    the factor of this color that is in the new color. If `factor` is
    0.0, the color is unchanged, if 1.0, white is returned.

    The alpha channel is unchanged.
    '''
    if isinstance(current_colour_raw, list) and len(current_colour_raw) >= 4:
        current_colour = Color(rgb=(current_colour_raw[0], current_colour_raw[1], current_colour_raw[2]), alpha = current_colour_raw[3])
        return current_colour.tint(1.0 - factor)
    return None

def darken_colour(current_colour_raw: list[float], factor: float = .07) -> Color | None:
    '''
    Creates a shade of passed color by mixing it with black. `factor` is
    the factor of this color that is in the new color. If `factor` is
    0.0, the color is unchanged, if 1.0, black is returned.

    The alpha channel is unchanged.
    '''
    if isinstance(current_colour_raw, list) and len(current_colour_raw) >= 4:
        current_colour = Color(rgb=(current_colour_raw[0], current_colour_raw[1], current_colour_raw[2]), alpha = current_colour_raw[3])
        return current_colour.shade(1.0 - factor)
    return None


def build_transparency_factor_map() -> dict[float, float]:
    def decimal_range(start, stop, step):
        while start < stop:
            yield round(start, 2)
            start += step

    return {t: 0.9 + abs(math.log10(t - .20)) - min(1.0, max(0.0, (t - .33)) / (.95 - .33))
            for t in decimal_range(0.25, 1.01, .01)}

@lru_cache(500)
def has_global_func(func_name: str) -> bool:
    return func_name in globals()

def call_global_func(func_name: str, *args, **kwargs):
    if has_global_func(func_name):
        return globals()[func_name](*args, **kwargs)
    return None
