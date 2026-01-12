from __future__ import annotations
import renpy
from renpy import config

draw_layers = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def clear_scene(specific_layers = None): # Clears the current scene of characters.
    if specific_layers and not isinstance(specific_layers, (list, tuple, set)):
        specific_layers = (specific_layers, ) #Allows for passing lists or single names.

    global draw_layers
    for a_layer in (x for x in draw_layers if not specific_layers or x in specific_layers):
        renpy.scene(a_layer)

def add_draw_layer(layer_name, above = "master"): #Sets up a character draw layer under the name of "layer name". This can be used to draw multiple characters on the screen at once.
    global draw_layers

    if layer_name not in draw_layers:
        draw_layers.append(layer_name)
        renpy.add_layer(layer_name, above = above)
        config.menu_clear_layers.append(layer_name)
        config.context_clear_layers.append(layer_name)
