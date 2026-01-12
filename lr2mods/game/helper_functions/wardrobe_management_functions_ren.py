from __future__ import annotations
import os
import re
from game.major_game_classes.clothing_related.Outfit_ren import Outfit, Clothing
from renpy import config
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

def log_outfit(outfit: Outfit, outfit_class = "FullSets", wardrobe_name = "Exported_Wardrobe") -> None:
    def build_item_dict(cloth: Clothing):
        def add_colors(item_dict, colour: list[float], prefix = ""):
            for idx, col_name in enumerate(["red", "green", "blue", "alpha"]):
                item_dict[prefix + col_name] = f"{colour[idx]:0.5f}"

        if isinstance(cloth, Clothing):
            item_dict = {"name": cloth.proper_name}
            add_colors(item_dict, cloth.colour)
            if cloth.pattern is not None:
                item_dict["pattern"] = cloth.pattern
                add_colors(item_dict, cloth.colour_pattern, "p")
        return item_dict

    def removeEmptyLines(root: ET.Element):
        hasWords = re.compile("\\w")
        for element in root.iter():
            if not re.search(hasWords, str(element.tail)):
                element.tail = ""
            if not re.search(hasWords, str(element.text)):
                element.text = ""

    # make sure wardrobe_name is without .xml
    if wardrobe_name.endswith(".xml"):
        wardrobe_name = wardrobe_name[:-4]
    elif not wardrobe_name:
        wardrobe_name = "Exported_Wardrobe"

    # allow variantion of outfit_class passed
    if outfit_class == "full":
        outfit_class = "FullSets"
    elif outfit_class == "under":
        outfit_class = "UnderwearSets"
    elif outfit_class == "over":
        outfit_class = "OverwearSets"

    file_path = os.path.abspath(os.path.join(config.basedir, "game"))
    file_path = os.path.join(file_path, "wardrobes")
    file_name = os.path.join(file_path, wardrobe_name + ".xml")

    #print("Writing wardrobe {} to file {}".format(wardrobe_name, file_name))

    if not os.path.isfile(file_name): #We assume if the file exists that it is well formed. Otherwise we will create it and guarantee it is well formed.
        #Note: if the file is changed (by inserting extra outfits, for example) exporting outfits may crash due to malformed xml, but we do not overwrite the file.
        starting_element = ET.Element("Wardrobe", {"name": wardrobe_name})
        starting_tree = ET.ElementTree(starting_element)
        ET.SubElement(starting_element, "FullSets")
        ET.SubElement(starting_element, "UnderwearSets")
        ET.SubElement(starting_element, "OverwearSets")
        starting_tree.write(file_name, encoding="UTF-8")

    wardrobe_tree: ET.ElementTree = ET.parse(file_name)
    tree_root: ET.Element = wardrobe_tree.getroot()
    outfit_root: ET.Element = tree_root.find(outfit_class)

    #print("Write {} to root: {}".format(outfit.name, outfit_class))

    outfit_element = ET.SubElement(outfit_root, "Outfit", {"name": outfit.name})

    parse_set = {
        "UpperBody": "upper_body",
        "LowerBody": "lower_body",
        "Feet": "feet",
        "Accessories": "accessories"
    }

    for set_name, attr_name in parse_set.items():
        base_element = ET.SubElement(outfit_element, set_name)
        for cloth in getattr(outfit, attr_name):
            item_dict = build_item_dict(cloth)
            if not cloth.is_extension:
                ET.SubElement(base_element, "Item", item_dict)

    removeEmptyLines(wardrobe_tree.getroot())
    xmlstr = minidom.parseString(ET.tostring(wardrobe_tree.getroot(), 'utf-8')).toprettyxml()
    with open(file_name, "w", encoding='utf-8') as f:
        f.write(xmlstr)

def log_wardrobe(the_wardrobe, file_name):

    for outfit in the_wardrobe.outfit_sets:
        log_outfit(outfit, outfit_class = "FullSets", wardrobe_name = file_name)

    for outfit in the_wardrobe.underwear_sets:
        log_outfit(outfit, outfit_class = "UnderwearSets", wardrobe_name = file_name)

    for outfit in the_wardrobe.overwear_sets:
        log_outfit(outfit, outfit_class = "OverwearSets", wardrobe_name = file_name)
