from __future__ import annotations
import builtins
from typing import TypeVar
from collections import OrderedDict
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list, people_with_job
from game.major_game_classes.character_related.Person_ren import Person, list_of_personalities
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, list_of_jobs
from game.major_game_classes.clothing_related.Clothing_ren import Clothing

T = TypeVar('T')
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
import random

generic_preference = {}
generic_preference["Body Type"] = {
    "Thin Body": ["thin_body", 33, 0],
    "Normal Body": ["standard_body", 33, 1],
    "Curvy Body": ["curvy_body", 33, 2]
}
generic_preference["Cup Size"] = {
    "AA": ["AA", 4, 0],
    "A": ["A", 8, 1],
    "B": ["B", 15, 2],
    "C": ["C", 20, 3],
    "D": ["D", 20, 4],
    "DD": ["DD", 15, 5],
    "DDD": ["DDD", 10, 6],
    "E": ["E", 5, 7],
    "F": ["F", 2, 8],
    "FF": ["FF", 1, 9]
}
generic_preference["Skin Colour"] = {
    "White": ["white", 33, 0],
    "Tan": ["tan", 33, 1],
    "Dark": ["black", 33, 2]
}
generic_preference["Hair Style"] = {
    "Bobbed Hair": ["Bobbed Hair", 8, 0],
    "Braided Hair": ["Braided Hair", 8, 1],
    "Coco Hair": ["Coco Hair", 8, 2],
    "Curly Bun Hair": ["Curly Bun Hair", 8, 3],
    "Long Hair": ["Long Hair", 8, 4],
    "Messy Hair": ["Messy Hair", 8, 5],
    "Messy Ponytail": ["Messy Ponytail", 8, 6],
    "Messy Short Hair": ["Messy Short Hair", 8, 7],
    "Ponytail": ["Ponytail", 8, 8],
    "Shaved Side Hair": ["Shaved Side Hair", 8, 9],
    "Short Hair": ["Short Hair", 8, 10],
    "Twin Tails": ["Twintails", 8, 11],
    "Windswept Short Hair": ["Windswept Short Hair", 8, 12]
}
generic_preference["Pubes Style"] = {
    "Shaved Pubic Hair": ["Shaved Pubic Hair", 20, 0],
    "Landing Strip Pubic Hair": ["Landing Strip Pubic Hair", 20, 1],
    "Diamond Shaped Pubic Hair": ["Diamond Shaped Pubic Hair", 20, 2],
    "Neatly Trimmed Pubic Hair": ["Neatly Trimmed Pubic Hair", 20, 3],
    "Untrimmed Pubic Hair": ["Untrimmed Pubic Hair", 20, 4]
}

# update defaults when not exist
for pref in generic_preference.values():
    for setting in pref.values():
        if not (getattr(persistent, setting[0]) or isinstance(getattr(persistent, setting[0]), int)):
            setattr(persistent, setting[0], setting[1])

def get_random_from_weighted_list(weighted_list: list[tuple[T, int]]) -> T: #Passed a list of parameters which are ["Thing", weighted value, anything_else,...]
    if builtins.len(weighted_list) == 0:
        return None

    result = random.choices(population = [x[0] for x in weighted_list], weights=[x[1] for x in weighted_list], k=1)
    return result[0]

def build_generic_weighted_list(preference: str, start = None, end = None):
    weighted_list = []
    if start is None:
        start = 0
    if end is None:
        end = len(generic_preference[preference])

    pref_dict = OrderedDict(generic_preference[preference])
    for idx, x in enumerate(pref_dict):
        if idx < start or idx > end:
            continue
        if getattr(persistent, generic_preference[preference][x][0], generic_preference[preference][x][1]) > 0:
            weighted_list.append((generic_preference[preference][x][0], getattr(persistent, generic_preference[preference][x][0], generic_preference[preference][x][1])))
    return weighted_list

def get_random_copy_from_named_list(weighted_list, item_list):
    name = get_random_from_weighted_list(weighted_list)
    if found := next((x for x in item_list if x.name.lower() == name.lower()), None):
        return found.get_copy()
    return None

def is_in_weighted_list(test_item, weighted_list):
    return any(x for x in weighted_list if x[0] == test_item)

def index_in_weighted_list(test_item, weighted_list):
    for item in weighted_list:
        if test_item == item[0]:
            return weighted_list.index(item)
    msg = f"{test_item!r} is not in weighted list"
    raise ValueError(msg)

def get_random_job() -> JobDefinition:
    result = get_random_from_weighted_list([x for x in list_of_jobs if x[1] > 2 and len(people_with_job(x[0])) < 4])
    if result:
        return result
    return get_random_from_weighted_list(list_of_jobs)

def get_random_personality():
    return get_random_from_list(list_of_personalities)

technobabble_list = (
    "optimize the electromagnetic pathways",
    "correct for the nanowave signature",
    "de-scramble the thermal injector",
    "crosslink the long chain polycarbons",
    "carbonate the ethyl groups",
    "oxidize the functional group",
    "resynchronize the autosequencers",
    "invert the final power spike",
    "kickstart the process a half second early",
    "stall the process by a half second",
    "apply a small machine learning algorithm",
    "hit the thing in just the right spot",
    "wait patiently for it to finish",
)

font_list = (
    "fonts/Avara.ttf",
    "fonts/GlacialIndifference-Regular.otf",
    "fonts/FantasqueSansMono-Regular.ttf",
    "fonts/TruenoRg.otf",
    "fonts/TruenoBd.otf",
    "fonts/Crimson-Roman.ttf",
    "fonts/Crimson-Bold.ttf",
    "fonts/HKVenetian-Regular.otf",
    "fonts/HKVenetian-Italic.otf",
    "fonts/AAntiCorona-L3Ax3.ttf",
)

def get_random_font():
    return renpy.store.gui.default_font
    # use one generic font
    #return get_random_from_list(font_list)

#https://snook.ca/technical/colour_contrast/colour.html A good site to generate colour contrast examples to make sure things are readable. Our text background is roughly #3459d2
readable_color_list = ( #Colours that are easily readable on our blue background.
    "#FFFFFF", # White
    "#C0C0C0", # Silver
    "#708090", # Slate Gray
    "#FFC0CB", # Pink
    "#FF69B4", # Hot Pink
    "#FF1493", # Deep Pink
    "#FA8072", # Salmon
    "#CD5C5C", # Indian Red
    "#ED2939", # Imperial
    "#DC143C", # Crimson
    "#FF6347", # Tomato
    "#FF8C00", # Dark Orange
    "#FFA500", # Orange
    "#FFFF66", # Laser Lemon
    "#FCE883", # Yellow (Crayola)
    "#FFD700", # Gold
    "#BC8F8F", # Rosy Brown
    "#F4A460", # Sandy Brown
    "#32CD32", # Lime Green
    "#00FF00", # Lime
    "#00FF7F", # Spring Green
    "#00FA9A", # Medium Spring Green
    "#98FB98", # Pale Green
    "#00FFFF", # Aqua
    "#AFEEEE", # Pale Turquoise
    "#48D1CC", # Medium Turquoise
    "#87CEFA", # Light Sky Blue
    "#00BFFF", # Deep Sky Blue
    "#DDA0DD", # Plum
    "#EE82EE", # Violet
    "#FF00FF", # Fuchsia
    "#7B68EE", # Medium Slate Blue
)
## COLOUR DEFINES ##
# Here we define colours as a 0 to 1 float for red, green, blue, and alpha. 0,0,0,1 would correspond to perfect black everywhere, 1,1,1,1 corresponds to no modification to the original greyscale.

colour_white = [1.0, 1.0, 1.0, 0.95]
colour_black = [0.1, 0.1, 0.1, 0.95]
colour_red = [0.6, 0.1, 0.1, 0.95]
colour_green = [0.2, 0.4, 0.2, 0.95]
colour_sky_blue = [0.4, 0.6, 0.9, 0.95]
colour_dark_blue = [0.15, 0.20, 0.80, 0.95]
colour_yellow = [0.9, 0.8, 0.05, 0.95]
colour_pink = [1.0, 0.8, 0.85, 0.95]

def get_random_readable_color():
    return get_random_from_list(readable_color_list)

def modify_transparency(color: list[float], transparency: float) -> list[float]:
    return [color[0], color[1], color[2], transparency]

def format_group_of_people(list_of_people: list[Person]): # Returns a string made up of people titles like "PersonA, PersonB, and PersonC." or just "PersonA and PersonB" if there are two people. (or PersonA if it's just one person)
    #Note: the list is formatted in the order it is handed over. renpy.random.scramble() it beforehand if you want it in a random order.
    return_string = ""
    if builtins.len(list_of_people) == 1:
        return_string += list_of_people[0].title
    elif builtins.len(list_of_people) == 2:
        return_string += f"{list_of_people[0].title} and {list_of_people[1].title}"
    else:
        for a_person in list_of_people:
            if a_person is not list_of_people[-1]: #If they're not the last person:
                return_string += a_person.title + ", "
            else:
                return_string += "and " + a_person.title

    return return_string

def format_list_of_clothing(clothing_list: list[Clothing]): # Takes a list of strings and formats them to the form "ThingA, thingB, and ThingC"
    return_string = ""
    if builtins.len(clothing_list) == 1:
        return_string = clothing_list[0].display_name
    elif builtins.len(clothing_list) == 2:
        return_string = f"{clothing_list[0].display_name} and {clothing_list[1].display_name}"
    else:
        for item in clothing_list:
            if item is clothing_list[-1]:
                return_string += "and " + item.display_name
            else:
                return_string += item.display_name + ", "
    return return_string
