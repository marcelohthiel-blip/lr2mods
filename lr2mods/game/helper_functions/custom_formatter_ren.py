from __future__ import annotations
import renpy
from renpy import persistent
from game.helper_functions.convert_to_string_ren import cm_to_feet_and_inches
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.character_related.Person_ren import Person
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""

@renpy.pure
def get_energy_tag_info(percentage: float, color = "#FFFF00"):
    return [
        (renpy.TEXT_TAG, f"color={color}"),
        (renpy.TEXT_TEXT, f'{percentage:.0f}%'),
        (renpy.TEXT_TAG, "/color"),
        (renpy.TEXT_TEXT, " "),
        (renpy.TEXT_TAG, "image=energy_token_small")
    ]

def energy_tag(tag, argument):
    energy = float(argument)
    percentage = (energy / max(mc.max_energy, 1)) * 100
    return get_energy_tag_info(percentage)

renpy.config.self_closing_custom_text_tags["energy"] = energy_tag

def girl_energy_tag(tag, argument):
    max_energy = 100.0
    girl: Person = None
    global the_person
    # try to get current girl, if not use base energy value of 100
    if "the_person" in globals() and isinstance(the_person, Person):
        girl = the_person
    if girl:
        max_energy = float(girl.max_energy)

    energy = float(argument)
    percentage = (energy / max(max_energy, 1)) * 100

    return get_energy_tag_info(percentage, color="#43B197")

renpy.config.self_closing_custom_text_tags["girl_energy"] = girl_energy_tag


@renpy.pure
def color_menu_option_info(contents, size = 18, color = "#B14365"):
    return [
        (renpy.TEXT_TAG, f"color={color}"),
        (renpy.TEXT_TAG, f"size={size}"),
            ] + contents + [
        (renpy.TEXT_TAG, "/size"),
        (renpy.TEXT_TAG, "/color"),
    ]

def menu_option_red_tag(tag, argument, contents):
    return color_menu_option_info(contents, argument or 18, "#B14365")

renpy.config.custom_text_tags["menu_red"] = menu_option_red_tag

def menu_option_green_tag(tag, argument, contents):
    return color_menu_option_info(contents, argument or 18, "#43B197")

renpy.config.custom_text_tags["menu_green"] = menu_option_green_tag

def menu_option_yellow_tag(tag, argument, contents):
    return color_menu_option_info(contents, argument or 18, "#FFFF00")

renpy.config.custom_text_tags["menu_yellow"] = menu_option_yellow_tag


potential_colour_map = {
    "hr": [4, 7, 10],
    "market": [25, 42, 59],
    "research": [28, 40, 52],
    "production": [18, 30, 42],
    "supply": [40, 60, 80]
}

def get_potential_colour(stat_name: str, value: int) -> str:
    potential_range = potential_colour_map[stat_name]
    if value < potential_range[0]:
        return "#B14365"
    if value < potential_range[1]:
        return "#FF8C00"
    if value < potential_range[2]:
        return "#FFCC00"
    return "#43B197"

@renpy.pure
def potential_color_info(contents, stat_name = "hr", value = 0):
    color = get_potential_colour(stat_name, value)
    return [
        (renpy.TEXT_TAG, f"color={color}"),
            ] + contents + [
        (renpy.TEXT_TAG, "/color"),
    ]

def potential_colour_tag(tag, argument, contents):
    args = argument.split("|")
    stat_name = "hr"
    if len(args) > 0 and args[0] in potential_colour_map:
        stat_name = args[0]

    value = 0
    if len(args) > 1:
        try:
            value = int(args[1])
        except ValueError:
            pass

    return potential_color_info(contents, stat_name, value)

renpy.config.custom_text_tags["potential_colour"] = potential_colour_tag


def height_tag(tag, argument):
    if persistent.use_imperial_system:
        feet, inches = cm_to_feet_and_inches(float(argument))
        if feet == 0:
            return [(renpy.TEXT_TEXT, f"{inches:.0f}\"")]
        return [(renpy.TEXT_TEXT, f"{feet:.0f}' {inches:.0f}\"")]
    return [(renpy.TEXT_TEXT, f"{float(argument):.0f} cm")]

renpy.config.self_closing_custom_text_tags["height"] = height_tag

def weight_tag(tag, argument):
    if persistent.use_imperial_system:
        pounds = float(argument) * 2.205
        return [(renpy.TEXT_TEXT, f"{pounds:.1f} lbs")]
    return [(renpy.TEXT_TEXT, f"{float(argument):.1f} kg")]

renpy.config.self_closing_custom_text_tags["weight"] = weight_tag

def weight_system_tag(tag, argument):
    if persistent.use_imperial_system:
        return [(renpy.TEXT_TEXT, "pounds")]
    return [(renpy.TEXT_TEXT, "kilos")]

renpy.config.self_closing_custom_text_tags["weight_system"] = weight_system_tag

def height_system_tag(tag, argument):
    if persistent.use_imperial_system:
        return [(renpy.TEXT_TEXT, "inches")]
    return [(renpy.TEXT_TEXT, "centimetres")]

renpy.config.self_closing_custom_text_tags["height_system"] = height_system_tag

def long_height_system_tag(tag, argument):
    if persistent.use_imperial_system:
        return [(renpy.TEXT_TEXT, "feet")]
    return [(renpy.TEXT_TEXT, "metres")]

renpy.config.self_closing_custom_text_tags["long_height_system"] = long_height_system_tag
