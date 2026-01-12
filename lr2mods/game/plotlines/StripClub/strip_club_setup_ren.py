from __future__ import annotations
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, mc, cousin
from game.major_game_classes.clothing_related.Wardrobe_ren import Outfit
from game.major_game_classes.game_logic.Room_ren import strip_club
from game.plotlines.StripClub.stripclub_outfit_ren import StripClubOutfit
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("setup_stripclub_uniforms")

def setup_stripclub_uniforms():
    def parse_wardrobe_to_uniform(wardrobe, flag_func: str):
        outfit_sets = {"set_full_outfit_flag": wardrobe.outfit_sets, "set_overwear_flag": wardrobe.overwear_sets, "set_underwear_flag": wardrobe.underwear_sets}

        for outfit_flag_func, outfitset in outfit_sets.items():
            outfit: Outfit
            for outfit in outfitset:
                uniform = StripClubOutfit(outfit, False)
                getattr(uniform, outfit_flag_func)(True)
                getattr(uniform, flag_func)(True)
                mc.business.stripclub_uniforms.append(uniform)

    mc.business.stripper_wardrobe.clear_wardrobe()
    mc.business.waitress_wardrobe.clear_wardrobe()
    mc.business.bdsm_wardrobe.clear_wardrobe()
    mc.business.manager_wardrobe.clear_wardrobe()
    mc.business.mistress_wardrobe.clear_wardrobe()

    parse_wardrobe_to_uniform(wardrobe_from_xml("Stripper_Wardrobe"), "set_stripper_flag")
    parse_wardrobe_to_uniform(wardrobe_from_xml("Waitresses_Wardrobe"), "set_waitress_flag")
    parse_wardrobe_to_uniform(wardrobe_from_xml("BDSM_Wardrobe"), "set_bdsm_flag")
    parse_wardrobe_to_uniform(wardrobe_from_xml("Manager_Wardrobe"), "set_manager_flag")
    parse_wardrobe_to_uniform(wardrobe_from_xml("Mistress_Wardrobe"), "set_mistress_flag")
    mc.business.update_stripclub_wardrobes()

    # set stripclub owner name on Room as attribute
    strip_club.owner = Person.get_random_male_name()

def add_unlock_stripclub_alternative_route():
    # disable blackmail
    cousin.event_triggers_dict["blackmail_level"] = -1
    # the player only has to find out she's stripping to start foreclosed event
