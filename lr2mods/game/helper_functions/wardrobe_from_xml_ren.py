from __future__ import annotations
import os
from typing import Callable
import xml.etree.ElementTree as ET
import renpy
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.UniformOutfit_ren import UniformOutfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe, Outfit, mc
from game.clothing_lists_ren import panties_list, bra_list, pants_list, skirts_list, dress_list, shirts_list, socks_list, tights_list, shoes_list, earings_list, bracelet_list, rings_list, neckwear_list
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -8 python:
"""

def wardrobe_from_xml(xml_filename):
    wardrobe = Wardrobe(xml_filename)
    wardrobe.load(xml_filename)
    return wardrobe

def import_wardrobe(wardrobe: Wardrobe, xml_filename: str): # This is a rewrite of the wardrobe_from_xml function written by Vren.
    file_name = Wardrobe.get_wardrobe_file(xml_filename)
    if file_name is None:
        return wardrobe # return the original wardrobe since we didn't find an xml to import into it.

    wardrobe.load(xml_filename, clean_wardrobe = False)
    return wardrobe

def import_uniform(xml_filename: str):
    file_name = Wardrobe.get_wardrobe_file(xml_filename)
    if file_name is None:
        return

    xml_root: ET.Element = ET.parse(file_name).getroot()
    for outfit_element in xml_root.find("FullSets"):
        mc.business.business_uniforms.append(UniformOutfit(Wardrobe.outfit_from_xml(outfit_element)))
    for outfit_element in xml_root.find("UnderwearSets"):
        mc.business.business_uniforms.append(UniformOutfit(Wardrobe.outfit_from_xml(outfit_element)))
    for outfit_element in xml_root.find("OverwearSets"):
        mc.business.business_uniforms.append(UniformOutfit(Wardrobe.outfit_from_xml(outfit_element)))
    return
