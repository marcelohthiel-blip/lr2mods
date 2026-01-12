from __future__ import annotations
from typing import Callable
import renpy
from game.bugfix_additions.ActionMod_ren import ActionMod, action_mod_list, init_action_mod_disabled
from game.general_actions.interaction_actions.chat_actions_definition_ren import build_specific_action_list
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder, one_piece_list, real_pants_list, real_dress_list, skirts_list, real_shirt_list, panties_list, real_bra_list, socks_list, shoes_list
from game.clothing_lists_ren import cute_panties, cute_lace_panties, bralette, lacy_one_piece_underwear, lace_bra, bodysuit_underwear, lace_panties, kitty_panties, lingerie_one_piece, teddy, tiny_g_string, strappy_bra, strappy_panties, long_skirt, pencil_skirt, skirt, lace_skirt, belted_skirt, mini_skirt, micro_skirt, camisole, tshirt, sweater, lace_sweater, business_vest, frilly_longsleeve_shirt, lace_crop_top, tanktop, tube_top, belted_top, capris, leggings, jean_hotpants, booty_shorts, daisy_dukes, evening_dress, frilly_dress, thin_dress, virgin_killer, two_part_dress, nightgown_dress, pinafore, wrapped_blouse, panties, thin_panties, thong, tiny_lace_panties, string_panties, crotchless_panties, strapless_bra, thin_bra, heart_pasties, quarter_cup_bustier, high_socks, thigh_highs, fishnets, garter_with_fishnets, sandal_heels, tall_boots, heels, boot_heels, pumps, high_heels, thigh_high_boots, tie_sweater

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def modify_wardrobe_requirement(person: Person):
    if not person.wardrobe.has_outfits:
        return False
    if person.obedience < 130:
        return "Requires: 130 Obedience"
    if person.effective_sluttiness() < 30 and person.love < 30:
        return "Requires: 30 Sluttiness or 30 Love"
    return True

modify_wardrobe_action = ActionMod("Modify entire wardrobe", requirement = modify_wardrobe_requirement, effect = "modify_wardrobe_label",
    menu_tooltip = "Ask girl to change her wardrobe.", priority = -5, category = "Wardrobe", initialization = init_action_mod_disabled)

def build_specific_action_list_alter_outfit_extended(org_func: Callable[[Person, bool], list]):
    def build_specific_action_list_wrapper(person: Person, keep_talking = True):
        # run original function
        result = org_func(person, keep_talking)
        # run extension code (append new action to base game menu)
        found = next((x for x in action_mod_list if x.effect == "modify_wardrobe_label"), None)
        if isinstance(found, ActionMod) and found.enabled:   # use enabled from action mod settings
            # use not stored action to append to action menu
            result.append((modify_wardrobe_action, person))
        return result

    return build_specific_action_list_wrapper

# wrap up the build_specific_action_list function
if "build_specific_action_list" in dir():
    build_specific_action_list = build_specific_action_list_alter_outfit_extended(build_specific_action_list)

def bra_removal(person: Person): # replace extensions with something
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.wearing_bra):
        old_bra = outfit.get_bra()
        new_panties = None
        if old_bra.has_extension and person.opinion.not_wearing_underwear < 0:
            new_panties = cute_panties.get_copy()
            new_panties.colour = old_bra.colour
        outfit.remove_clothing(old_bra)
        if new_panties:
            outfit.add_lower(new_panties)
        alterations += 1
    return alterations

def panty_removal(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.wearing_panties):
        old_panties = outfit.get_panties()
        if old_panties.is_extension:
            new_bra = None
            if person.opinion.not_wearing_underwear < 0:
                new_bra = bralette.get_copy()
                new_bra.colour = old_panties.colour
            if outfit.remove_bra():
                alterations += 1
            if new_bra:
                outfit.add_upper(new_bra)
                new_bra = None

        outfit.remove_clothing(old_panties)
        alterations += 1

    return alterations

def custom_clothing_comparer(clothing: Clothing, items: list[Clothing]):
    return any(x for x in items if clothing.is_similar(x))

def lingerie_removal(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_one_piece):
        cloth = next((x for x in outfit.upper_body if custom_clothing_comparer(x, one_piece_list)), None)
        if cloth and cloth.has_extension:
            if cloth.is_similar(lacy_one_piece_underwear):
                new_bra = lace_bra.get_copy()
                new_panties = lace_panties.get_copy()
            elif cloth.is_similar(bodysuit_underwear):
                new_bra = lace_bra.get_copy()
                new_panties = thong.get_copy()
            elif cloth.is_similar(lingerie_one_piece):
                new_bra = teddy.get_copy()
                new_panties = tiny_g_string.get_copy()
            else:
                new_bra = strappy_bra.get_copy()
                new_panties = strappy_panties.get_copy()

            outfit.remove_clothing(cloth)

            if new_bra:
                new_bra.colour = cloth.colour
                outfit.add_upper(new_bra)
            if new_panties:
                new_panties.colour = cloth.colour
                outfit.add_lower(new_panties)
            outfit.update_name()
            alterations += 1
    return alterations

def no_pants(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_pants):
        for clothing in (x for x in outfit.lower_body if custom_clothing_comparer(x, real_pants_list)):
            new_clothing = None
            if clothing.slut_value <= 0:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = long_skirt.get_copy()
                else:
                    new_clothing = pencil_skirt.get_copy()
            elif clothing.slut_value <= 1:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = skirt.get_copy()
                else:
                    new_clothing = lace_skirt.get_copy()
            elif clothing.slut_value <= 4:
                new_clothing = belted_skirt.get_copy()
            elif clothing.slut_value <= 6:
                new_clothing = mini_skirt.get_copy()
            else:
                new_clothing = micro_skirt.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_lower(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations

def no_dresses(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_dress):
        for clothing in (x for x in outfit.upper_body if custom_clothing_comparer(x, real_dress_list)):
            if clothing.slut_value <= 1:
                if renpy.random.randint(0, 1) == 1:
                    new_top = camisole.get_copy()
                elif renpy.random.randint(0, 1) == 1:
                    new_top = tshirt.get_copy()
                else:
                    new_top = sweater.get_copy()
                if renpy.random.randint(0, 1) == 1:
                    new_bottom = long_skirt.get_copy()
                else:
                    new_bottom = pencil_skirt.get_copy()
            elif clothing.slut_value <= 3:
                if renpy.random.randint(0, 1) == 1:
                    new_top = lace_sweater.get_copy()
                elif renpy.random.randint(0, 1) == 1:
                    new_top = business_vest.get_copy()
                else:
                    new_top = frilly_longsleeve_shirt.get_copy()
                if renpy.random.randint(0, 1) == 1:
                    new_bottom = skirt.get_copy()
                else:
                    new_bottom = lace_skirt.get_copy()
            elif clothing.slut_value <= 5:
                new_top = lace_crop_top.get_copy()
                new_bottom = belted_skirt.get_copy()
            elif clothing.slut_value <= 6:
                if renpy.random.randint(0, 1) == 1:
                    new_top = tanktop.get_copy()
                else:
                    new_top = tube_top.get_copy()
                new_bottom = mini_skirt.get_copy()
            else:
                new_top = belted_top.get_copy()
                new_bottom = micro_skirt.get_copy()

            outfit.remove_clothing(clothing)
            if new_top:
                new_top.colour = clothing.colour
                outfit.add_upper(new_top)
            if new_bottom:
                new_bottom.colour = clothing.colour
                outfit.add_lower(new_bottom)
            outfit.update_name()
            alterations += 1
    return alterations

def shorter_pants(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_pants):
        for clothing in (x for x in outfit.lower_body if custom_clothing_comparer(x, real_pants_list)):
            new_clothing = None
            if clothing.slut_value <= 1:
                new_clothing = capris.get_copy()
            elif clothing.slut_value <= 2 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 20:
                new_clothing = leggings.get_copy()
            elif clothing.slut_value <= 3 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 40:
                new_clothing = jean_hotpants.get_copy()
            elif clothing.slut_value <= 4 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = booty_shorts.get_copy()
            elif (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = daisy_dukes.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_lower(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations

def shorter_skirts(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_skirt):
        for clothing in (x for x in outfit.lower_body if custom_clothing_comparer(x, skirts_list)):
            new_clothing = None
            if clothing.slut_value <= 1:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = skirt.get_copy()
                else:
                    new_clothing = lace_skirt.get_copy()
            elif clothing.slut_value <= 2 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 40:
                new_clothing = belted_skirt.get_copy()
            elif clothing.slut_value <= 3 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = mini_skirt.get_copy()
            elif (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if person.opinion.skimpy_outfits * 5 + person.sluttiness > 80:
                    new_clothing = micro_skirt.get_copy()
                else:
                    new_clothing = mini_skirt.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_lower(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations

def smaller_dresses(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_dress):
        for clothing in (x for x in outfit.upper_body if custom_clothing_comparer(x, real_dress_list)):
            new_clothing = None
            if clothing.slut_value <= 1:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = evening_dress.get_copy()
                else:
                    new_clothing = frilly_dress.get_copy()
            elif clothing.slut_value <= 2 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 40:
                new_clothing = thin_dress.get_copy()
            elif clothing.slut_value <= 4 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = virgin_killer.get_copy()
            elif (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 80:
                    new_clothing = two_part_dress.get_copy()
                else:
                    new_clothing = nightgown_dress.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                if clothing == pinafore:    # when pinafore also remove shirt
                    top = next((x for x in outfit.upper_body if x.layer == 2), None)
                    if top:
                        outfit.remove_clothing(top)
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_upper(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations

def smaller_shirts(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_shirt):
        for clothing in (x for x in outfit.upper_body if custom_clothing_comparer(x, real_shirt_list) and x.layer == 2):
            new_clothing = None
            if clothing.slut_value <= 0:
                new_clothing = wrapped_blouse.get_copy()
            if clothing.slut_value <= 0 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 20:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = tie_sweater.get_copy()
                elif renpy.random.randint(0, 1) == 1:
                    new_clothing = tshirt.get_copy()
                else:
                    new_clothing = sweater.get_copy()
            elif clothing.slut_value <= 1 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 40:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = lace_sweater.get_copy()
                elif renpy.random.randint(0, 1) == 1:
                    new_clothing = business_vest.get_copy()
                else:
                    new_clothing = frilly_longsleeve_shirt.get_copy()
            elif clothing.slut_value <= 2 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = lace_crop_top.get_copy()
            elif clothing.slut_value <= 3 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = tanktop.get_copy()
            elif (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 80:
                    new_clothing = belted_top.get_copy()
                else:
                    new_clothing = tube_top.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_upper(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations

def sexier_panties(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.wearing_panties):
        for clothing in (x for x in outfit.lower_body if custom_clothing_comparer(x, panties_list)):
            new_clothing = None
            if clothing.slut_value <= 0:
                new_clothing = panties.get_copy()
            if clothing.slut_value <= 0 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 20:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = thin_panties.get_copy()
                elif renpy.random.randint(0, 1) == 1:
                    new_clothing = kitty_panties.get_copy()
                else:
                    new_clothing = cute_panties.get_copy()
            elif clothing.slut_value <= 1 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 40:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = cute_lace_panties.get_copy()
                else:
                    new_clothing = lace_panties.get_copy()
            elif clothing.slut_value <= 2 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = thong.get_copy()
                else:
                    new_clothing = tiny_lace_panties.get_copy()
            elif clothing.slut_value <= 3 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = string_panties.get_copy()
                else:
                    new_clothing = tiny_g_string.get_copy()
            elif (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 80:
                    new_clothing = crotchless_panties.get_copy()
                else:
                    new_clothing = strappy_panties.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_lower(new_clothing)
                if outfit in person.wardrobe.underwear_sets:
                    outfit.update_name()
                alterations += 1
    return alterations

def sexier_bras(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.wearing_bra):
        for clothing in (x for x in outfit.upper_body if custom_clothing_comparer(x, real_bra_list)):
            new_clothing = None
            if clothing.slut_value <= 0:
                new_clothing = bralette.get_copy()
            if clothing.slut_value <= 1 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 20:
                new_clothing = strapless_bra.get_copy()
            elif clothing.slut_value <= 2 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 40:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = lace_bra.get_copy()
                else:
                    new_clothing = thin_bra.get_copy()
            elif clothing.slut_value <= 3 and (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                new_clothing = strappy_bra.get_copy()
            elif (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 60:
                if (person.opinion.skimpy_outfits * 5 + person.sluttiness) > 80:
                    new_clothing = heart_pasties.get_copy()
                else:
                    new_clothing = quarter_cup_bustier.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_upper(new_clothing)
                if outfit in person.wardrobe.underwear_sets:
                    outfit.update_name()
                alterations += 1
    return alterations

def sexier_socks(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_socks):
        for clothing in (x for x in outfit.feet if custom_clothing_comparer(x, socks_list)):
            new_clothing = None
            if clothing.slut_value <= 0 and (person.opinion.lingerie * 5 + person.sluttiness) > 20:
                new_clothing = high_socks.get_copy()
                clothing.colour[3] = .33
            elif clothing.slut_value <= 2 and (person.opinion.lingerie * 5 + person.sluttiness) > 40:
                new_clothing = thigh_highs.get_copy()
            elif clothing.slut_value <= 5 and (person.opinion.lingerie * 5 + person.sluttiness) > 60:
                new_clothing = fishnets.get_copy()
            elif (person.opinion.lingerie * 5 + person.sluttiness) > 60:
                new_clothing = garter_with_fishnets.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_feet(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations

def sexier_shoes(person: Person):
    alterations = 0
    for outfit in (x for x in person.wardrobe if x.has_shoes):
        for clothing in (x for x in outfit.feet if custom_clothing_comparer(x, shoes_list)):
            new_clothing = None
            if clothing.slut_value <= 0 and person.sluttiness > 20:
                if renpy.random.randint(0, 1) == 1:
                    new_clothing = sandal_heels.get_copy()
                else:
                    new_clothing = tall_boots.get_copy()
            elif clothing.slut_value <= 1 and person.sluttiness > 30:
                new_clothing = heels.get_copy()
            elif clothing.slut_value <= 2 and person.sluttiness > 40:
                new_clothing = boot_heels.get_copy()
            elif clothing.slut_value <= 3 and person.sluttiness > 50:
                new_clothing = pumps.get_copy()
            elif clothing.slut_value <= 4 and person.sluttiness > 60:
                new_clothing = high_heels.get_copy()
            elif person.sluttiness > 60:
                if person.opinion.boots >= 0:
                    new_clothing = thigh_high_boots.get_copy()
                else:
                    new_clothing = high_heels.get_copy()

            if new_clothing and not clothing.is_similar(new_clothing):
                new_clothing.colour = clothing.colour
                outfit.remove_clothing(clothing)
                outfit.add_feet(new_clothing)
                outfit.update_name()
                alterations += 1
    return alterations


def translucent(person: Person, fade_number = .98, fade_over = False, fade_under = False):
    alterations = 0
    for outfit in person.wardrobe:
        for clothing in (x for x in outfit.upper_body + outfit.lower_body):
            if (not clothing.transparency == fade_number
                and ((fade_over and clothing not in real_bra_list + panties_list)
                    or (fade_under and clothing in real_bra_list + panties_list))):

                clothing.transparency = fade_number
                alterations += 1
    return alterations

def add_makeup(person: Person, make_up_score_boost = 0):
    alterations = 0
    for outfit in person.wardrobe:
        WardrobeBuilder.add_make_up_to_outfit(person, outfit, make_up_score_boost = make_up_score_boost)
        alterations += person.opinion.makeup + make_up_score_boost
    return alterations

def build_modify_wardrobe_menu():
    modify_outfit = ["Outfit", ["Change Base Outfit", "base"], ["Add Make Up", "add_makeup"], ["More Translucency", "translucent"],
        ["Sexier Clothes (all options)", "sexier_clothes"], ["Back", "back"]
    ]
    modify_overwear = ["Overwear", ["Stop wearing pants", "no_pants"], ["Stop wearing dresses", "no_dresses"],
        ["Shorter Skirts", "shorter_skirts"], ["Shorter Pants", "shorter_pants"],
        ["Sexier Shirts", "sexier_shirts"], ["Sexier Dresses", "sexier_dresses"],
        ["Sexier Shoes", "sexier_shoes"]
    ]
    modify_underwear = ["Underwear", ["Stop wearing one piece underwear", "lingerie_removal"],
        ["Stop wearing bras", "no_bras"], ["Stop wearing panties", "no_panties"],
        ["Sexier Bras", "sexier_bras"], ["Sexier Panties", "sexier_panties"],
        ["Sexier Socks", "sexier_socks"]
    ]
    return [modify_outfit, modify_overwear, modify_underwear]
