'''
Contains the implementation of webcolors in conjunction with game classes
'''
from __future__ import annotations
from game.helper_functions.webcolors_ren import _reversedict, closest_color_name, normalize_hex, rgb_fraction_to_rgb, rgb_to_hex
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder
from renpy.color import Color
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
from functools import lru_cache

hair_color_names_to_hex = {}
for color in Person._list_of_hairs:
    hair_color_names_to_hex[color[0]] = normalize_hex(rgb_to_hex(rgb_fraction_to_rgb(color[1][:3])))
hair_color_hex_to_names = _reversedict(hair_color_names_to_hex)

@lru_cache(500)
def closest_hair_colour(requested_colour: Color) -> str:
    return closest_color_name(requested_colour, hair_color_hex_to_names)

eye_color_names_to_hex = {}
for color in Person._list_of_eyes:
    eye_color_names_to_hex[color[0]] = normalize_hex(rgb_to_hex(rgb_fraction_to_rgb(color[1][:3])))
eye_color_hex_to_names = _reversedict(eye_color_names_to_hex)

@lru_cache(500)
def closest_eye_color(requested_colour: Color) -> str:
    return closest_color_name(requested_colour, eye_color_hex_to_names)

opinion_color_names_to_hex = {}
for g_prefs in WardrobeBuilder.color_prefs.values():
    for g_name, g_color in g_prefs.items():
        opinion_color_names_to_hex[g_name] = normalize_hex(rgb_to_hex(rgb_fraction_to_rgb(g_color[:3])))
opinion_color_names_to_hex = _reversedict(opinion_color_names_to_hex)

@lru_cache(1000)
def closest_preference_color(requested_colour: Color) -> str:
    return closest_color_name(requested_colour, opinion_color_names_to_hex)
