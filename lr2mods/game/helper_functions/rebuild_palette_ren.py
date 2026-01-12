from __future__ import annotations
import renpy
from renpy import persistent
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def rebuild_colour_palette():
    matches = ["red", "green", "blue", "brown"]
    persistent.colour_palette = []
    for opinion in sorted(WardrobeBuilder.color_prefs, key = lambda x: x):
        count = 0
        for color_name in WardrobeBuilder.color_prefs[opinion]:
            if count < (5 if any(x in opinion for x in matches) else 4):
                persistent.colour_palette.append(WardrobeBuilder.color_prefs[opinion][color_name])
                count += 1

    while len(persistent.colour_palette) < 52:
        persistent.colour_palette.append([1, 1, 1, 1])

    renpy.save_persistent()

# generate a more useable default color palette
if len(persistent.colour_palette) < 52:
    rebuild_colour_palette()

if persistent.colour_palette[0] == [1, 1, 1, 1]:
    rebuild_colour_palette()
