from __future__ import annotations
import builtins
from typing import Literal
import renpy
from renpy.color import Color
from renpy.rollback import NoRollback
from game.clothing_lists_ren import black_skin, shoes_list, rings_list, bracelet_list, apron, breed_collar, cum_slut_collar, fuck_doll_collar, nightgown_dress, long_skirt, pencil_skirt, skirt, lace_skirt, belted_skirt, mini_skirt, micro_skirt, jeans, suitpants, capris, leggings, jean_hotpants, booty_shorts, daisy_dukes, lab_coat, suit_jacket, vest, panties_list, dress_list, skirts_list, light_eye_shadow, heavy_eye_shadow, lipstick, blush, bra_list, cincher, heart_pasties, pants_list, cop_pants, shirts_list, cop_blouse, bath_robe, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, socks_list, tights_list, chandelier_earings, gold_earings, modern_glasses, neckwear_list, two_part_dress, thin_dress, leotard, lace_sweater, belted_top, lace_crop_top, frilly_dress, frilly_longsleeve_shirt, tanktop, tube_top, tshirt, business_vest, teddy, kitty_babydoll, tights, high_socks, thigh_highs, fishnets, garter_with_fishnets, pumps, heels, high_heels, thigh_high_boots, lace_choker, wide_choker, spiked_choker, long_sweater, sleeveless_top, long_tshirt, camisole, long_sleeve_blouse, short_sleeve_blouse, tie_sweater, dress_shirt, sweater_dress, bra, bralette, sports_bra, panties, plain_panties, cotton_panties, boy_shorts, kitty_panties, sandles, shoes, slips, sneakers, short_socks, medium_socks, wool_scarf, strapless_bra, lace_bra, strappy_bra, quarter_cup_bustier, summer_dress, virgin_killer, cute_panties, lace_panties, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string, string_panties, strappy_panties, crotchless_panties, sweater, sandal_heels, boot_heels, tall_boots, thin_panties, thin_bra, pinafore, corset
from game.random_lists_ren import get_random_from_weighted_list, modify_transparency
from game.helper_functions.random_generation_functions_ren import create_random_person, colour_yellow
from game.helper_functions.list_functions_ren import get_random_from_list
from game.helper_functions.webcolors_usage_ren import closest_preference_color
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.clothing_related.Facial_Accessories_ren import Facial_Accessory

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
import colorsys
from collections import OrderedDict

real_bra_list: list[Clothing] = [x for x in bra_list if x not in (cincher, heart_pasties, kitty_babydoll, teddy)]
real_pants_list: list[Clothing] = [x for x in pants_list if x != cop_pants]
real_shirt_list: list[Clothing] = [x for x in shirts_list if x not in (cop_blouse, lab_coat, camisole, suit_jacket, vest)]
real_dress_list: list[Clothing] = [x for x in dress_list if not x.is_extension and x not in (bath_robe, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, apron, nightgown_dress)]
nightgown_list: list[Clothing] = [nightgown_dress, camisole, kitty_babydoll, teddy]
one_piece_list: list[Clothing] = [lingerie_one_piece, lacy_one_piece_underwear, bodysuit_underwear, leotard]
low_socks_list: list[Clothing] = [short_socks, medium_socks]
outerwear_list: list[Clothing] = [apron, lab_coat, suit_jacket, vest, bath_robe]
thigh_high_sock_list: list[Clothing] = [high_socks, thigh_highs, fishnets, garter_with_fishnets]
boots_list: list[Clothing] = [boot_heels, tall_boots, thigh_high_boots]
high_heels_list: list[Clothing] = [pumps, heels, high_heels, boot_heels, thigh_high_boots]
earings_only_list: list[Clothing] = [chandelier_earings, gold_earings, modern_glasses]
neckwear_without_collars: list[Clothing] = [x for x in neckwear_list if x.proper_name not in ("Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Wool_Scarf", "Spiked Choker")]
makeup_list: list[Facial_Accessory] = [lipstick, light_eye_shadow, heavy_eye_shadow, blush]
always_uses_pattern: tuple[Clothing] = (apron, breed_collar, cum_slut_collar, fuck_doll_collar)

class WardrobeBuilder(NoRollback):
    default_person = None

    preferences: dict[str, dict[str, list[Clothing]]] = {}
    preferences["skimpy outfits"] = {}
    preferences["skimpy outfits"]["upper_body"] = [two_part_dress, thin_dress, leotard, lace_sweater, belted_top, lace_crop_top, frilly_longsleeve_shirt, tshirt, tanktop, tube_top, business_vest]
    preferences["skimpy outfits"]["lower_body"] = [booty_shorts, jean_hotpants, daisy_dukes, belted_skirt, mini_skirt, micro_skirt]
    preferences['skimpy outfits']["feet"] = [thigh_highs, fishnets, garter_with_fishnets, pumps, heels, high_heels, thigh_high_boots]
    preferences["skimpy outfits"]["accessories"] = [lace_choker, wide_choker, spiked_choker]
    preferences["conservative outfits"] = {}
    preferences["conservative outfits"]["upper_body"] = [long_sweater, sleeveless_top, long_tshirt, camisole, long_sleeve_blouse, short_sleeve_blouse, tie_sweater, dress_shirt, sweater_dress, bra, bralette, sports_bra, lab_coat, vest, suit_jacket]
    preferences["conservative outfits"]["lower_body"] = [pencil_skirt, skirt, long_skirt, jeans, suitpants, panties, plain_panties, cotton_panties, boy_shorts, kitty_panties, tights]
    preferences["conservative outfits"]["feet"] = [sandles, shoes, slips, sneakers, short_socks]
    preferences["conservative outfits"]["accessories"] = [wool_scarf]
    preferences["dresses"] = {}
    preferences["dresses"]["upper_body"] = real_dress_list
    preferences["skirts"] = {}
    preferences["skirts"]["lower_body"] = skirts_list
    preferences["pants"] = {}
    preferences["pants"]["lower_body"] = real_pants_list
    preferences["showing her tits"] = {}
    preferences["showing her tits"]["upper_body"] = [strapless_bra, lace_bra, strappy_bra, quarter_cup_bustier, cincher, heart_pasties, thin_dress, two_part_dress, pinafore, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, lace_sweater, tshirt, sweater, belted_top, tube_top, business_vest, suit_jacket, vest]
    preferences["showing her ass"] = {}
    preferences["showing her ass"]["upper_body"] = [two_part_dress, thin_dress, summer_dress, virgin_killer, frilly_dress, leotard, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear]
    preferences["showing her ass"]["lower_body"] = [cute_panties, lace_panties, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string, string_panties, strappy_panties, crotchless_panties, leggings, booty_shorts, jean_hotpants, daisy_dukes, micro_skirt]
    preferences["high heels"] = {}
    preferences["high heels"]["feet"] = [sandal_heels, pumps, heels, high_heels, boot_heels, thigh_high_boots]
    preferences["boots"] = {}
    preferences["boots"]["feet"] = [boot_heels, tall_boots, thigh_high_boots]
    preferences["makeup"] = {}
    preferences["makeup"]["accessories"] = [light_eye_shadow, heavy_eye_shadow, blush, lipstick]
    preferences['lingerie'] = {}
    preferences['lingerie']["upper_body"] = [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, nightgown_dress, strapless_bra, lace_bra, thin_bra, strappy_bra, cincher, corset, heart_pasties]
    preferences['lingerie']["lower_body"] = [lace_panties, cute_lace_panties, tiny_lace_panties, thin_panties, thong, tiny_g_string, string_panties, strappy_panties, tights]
    preferences['lingerie']["feet"] = [high_socks, thigh_highs, fishnets, garter_with_fishnets]
    preferences['lingerie']['accessories'] = [lace_choker, wide_choker]

    matching_underwear: dict[str, list[Clothing]] = {}
    matching_underwear["Bralette"] = [boy_shorts, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string]
    matching_underwear["Sports_Bra"] = [cotton_panties, panties, lace_panties]
    matching_underwear["Lace_Bra"] = [cute_lace_panties, lace_panties, tiny_lace_panties, thong, tiny_g_string, crotchless_panties]
    matching_underwear["Strappy_Bra"] = [strappy_panties]
    matching_underwear["Corset"] = [panties, thin_panties, thong, tiny_lace_panties, tiny_g_string, string_panties, crotchless_panties]
    matching_underwear["Cincher"] = [panties, thin_panties, thong, tiny_lace_panties, tiny_g_string, string_panties, crotchless_panties]

    color_prefs: dict[str, OrderedDict[str, list[float]]] = {}
    color_prefs["the colour blue"] = OrderedDict([
        ("dark slate blue", [.282, .239, .545, .95]),
        ("dark denim", [0, .278, .671, .95]),
        ("denim", [.082, .376, .741, .95]),
        ("steel blue", [.0275, .51, .706, .95]),
        ("light denim", [.365, .678, .925, .95]),
        ("cornflower blue", [.392, .584, .929, .95]),
        ("sky blue", [.529, .808, .922, 0.95]),
    ])
    color_prefs["the colour yellow"] = OrderedDict([
        ("khaki", [.765, .69, .569, .95]),
        ("indian yellow", [.89, .659, .341, .95]),
        ("sand", [.8862, .79215, .4627, .95]),
        ("flax", [.9333, .8627, .5098, .95]),
        ("saffron", [.96, .77, .19, .95]),
        ("corn", [.98, .92, .36, .95]),
    ])
    color_prefs["the colour red"] = OrderedDict([
        ("bordeaux red", [.38, .118, .149, .95]),
        ("berry", [.478, .09, .071, .95]),
        ("venetian red", [.7843, .0313, .08235, .95]),
        ("sinopia", [.80, .26, .04, .95]),
        ("vermillion", [.890, .258, .203, .95]),
        ("debian red", [.843, .039, .325, .95]),
    ])
    color_prefs["the colour pink"] = OrderedDict([
        ("dark pink", [.906, .329, .502, .95]),
        ("french pink", [.9647, .2901, .54117, .95]),
        ("hot pink", [1, .412, .706, .95]),
        ("nadeshiko pink", [.9647, .6784, .7764, .95]),
        ("cotton candy", [1, .733, .851, .95]),
        ("pale pink", [.98, .885, .867, .95]),
    ])
    color_prefs["the colour black"] = OrderedDict([
        ("midnight black", [.15, .15, .15, .95]),
        ("charcoal", [.212, .271, .31, .95]),
        ("dark grey", [.365, .365, .365, .95]),
        ("warm black", [0, .26, .36, .95]),
    ])
    color_prefs["the colour green"] = OrderedDict([
        ("army green", [.294, .325, .125, .95]),
        ("sea green", [.18, .545, .341, .95]),
        ("jade", [0, .659, .43, .95]),
        ("caribbean green", [0, .8, .6, .95]),
        ("pistachio", [.576, .772, .447, .95]),
    ])
    color_prefs["the colour purple"] = OrderedDict([
        ("tyrian purple", [.4, .0078, .23529, .95]),
        ("palatinate purple", [.41, .16, .38, .95]),
        ("dark lavender", [.45, .31, .59, .95]),
        ("medium purple", [.5764, .4392, .8588, .95]),
        ("rich lilac", [.714, .4, .824, .95]),
        ("mauve", [.878, .690, 1, .95]),
    ])
    color_prefs["the colour orange"] = OrderedDict([
        ("clay", [0.6235, 0.3294, 0, .95]),
        ("burnt orange", [.8, .33, 0, .95]),
        ("tigers eye", [.878, .552, .235, .95]),
        ("honey orange", [.89, .6, .16, .95]),
        ("swiss coffee", [.859, .331, .321, .95]),
        ("vintage orange", [1, .6901, .3647, .95]),
    ])
    color_prefs["the colour white"] = OrderedDict([
        ("dark white", [.8823, .8509, .8196, .95]),
        ("cotton white", [.992, .953, .918, .95]),
        ("white smoke", [.95, .95, .95, .95]),
        ("ghost white", [.97, .97, 1, .95]),
        ("antique white", [.98, .922, .843, .95]),
    ])
    color_prefs["the colour brown"] = OrderedDict([
        ("chocolate noir", [.352, .239, .239, .95]),
        ("leather", [.384, .29, .18, .95]),
        ("coffee", [.435, .305, .215, .95]),
        ("saddle brown", [.451, .313, .235, .95]),
        ("mocha", [.514, .373, .345, .95]),
        ("khaki", [.765, .69, .569, .95]),
        ("light beige", [.94, .94, .78, .95]),
    ])
    #color_prefs[""][""] = [, , , ]

    neutral_palette: dict[str, list[float]] = {
        "dark denim": [0, .278, .671, .95],
        "denim": [.082, .376, .741, .95],
        "light denim": [.365, .678, .925, .95],
        "midnight black": [.15, .15, .15, .95],
        "khaki": [.765, .69, .569, .95],
        "dark grey": [.365, .365, .365, .95],
        "indian yellow": [.89, .659, .341, .95],
        "grey": [.502, .502, .502, .95],
        "light grey": [.827, .827, .827, .95],
        "sky blue": [.529, .808, .922, 0.95],
        "antique white": [.98, .922, .843, .95],
        "white smoke": [.95, .95, .95, .95],
        "light beige": [.94, .94, .78, .95],
        "sand": [.8862, .79215, .4627, .95],
        "venetian red": [.7843, .0313, .08235, .95],
        "vintage orange": [1, .6901, .3647, .95],
        "leather": [.384, .29, .18, .95],
        "mocha": [.514, .373, .345, .95],
        "charcoal": [.212, .271, .31, .95],
        "scarlet": [1, .141, .0, .95],    #Looks decent for some patterns, might have to delete
        "pale pink": [.98, .885, .867, .95],
        "berry": [.478, .09, .071, .95],
        "saffron": [.96, .77, .19, .95],
    }

    color_clothing_map: dict[str, tuple[str]] = {
        "Jean_Hotpants": ("the colour black", "the colour blue", "the colour brown", "the colour white"),
        "Daisy_Dukes": ("the colour black", "the colour blue", "the colour brown", "the colour white"),
        "Jeans": ("the colour black", "the colour blue", "the colour brown", "the colour white"),
        "Suit_Pants": ("the colour black", "the colour blue", "the colour brown", "the colour white", "the colour red", "the colour yellow", "the colour green"),
        "Capris": ("the colour black", "the colour blue", "the colour brown", "the colour white"),
        "Pencil_Skirt": ("the colour black", "the colour blue", "the colour brown", "the colour white", "the colour red", "the colour yellow", "the colour green"),
        "Short_Socks": ("the colour black", "the colour white", "the colour red"),
        "Long_Socks": ("the colour black", "the colour white", "the colour red"),
        "High_Socks": ("the colour black", "the colour white", "the colour red", "the colour pink", "the colour yellow"),
        "Slips": ("the colour black", "the colour white", "the colour brown"),
        "Shoes": ("the colour black", "the colour white", "the colour brown"),
        "Sneakers": ("the colour black", "the colour white", "the colour red"),
        "Sandal_Heels": ("the colour black", "the colour white", "the colour red", "the colour brown"),
        "Heels": ("the colour black", "the colour white", "the colour red", "the colour brown"),
        "High_Heels": ("the colour black", "the colour white", "the colour red", "the colour brown"),
        "Boot_Heels": ("the colour black", "the colour white", "the colour red", "the colour brown"),
        "High_Boots": ("the colour black", "the colour white", "the colour red", "the colour brown"),
        "Gold_Earings": ("the colour yellow",),
        "Copper_Bracelet": ("the colour yellow",),
        "Diamond_Ring": ("the colour yellow",),
        "Copper_Ring_Set": ("the colour yellow",),
        "Spiked_Bracelet": ("the colour white",),
        "Spiked_Choker": ("the colour white",),
    }

    clashing_colour_map: dict[str, tuple[str]] = {
        "the colour red": ("the colour pink", "the colour purple", "the colour brown"),
        "the colour pink": ("the colour red", "the colour purple", "the colour brown"),
        "the colour purple": ("the colour red", "the colour pink", "the colour blue"),
        "the colour blue": ("the colour purple",),
        "the colour orange": ("the colour yellow",),
        "the colour yellow": ("the colour orange",),
        "the colour brown": ("the colour black", "the colour pink", "the colour red"),
        "the colour black": ("the colour brown",),
    }

    neutral_color_map: dict[str, tuple[str]] = {
        "Jeans": ("dark denim", "denim", "light denim", "midnight black", "dark grey"),
        "Suit_Pants": ("midnight black", "leather", "khaki", "grey", "berry"),
        "Capris": ("dark denim", "denim", "dark grey"),
        "Leggings": ("midnight black", "dark grey", "leather", "berry", "indian yellow"),
        "Leggings_Pattern": ("pale pink", "light grey", "white smoke"),
        "Jean_Hotpants": ("dark denim", "denim", "light denim", "midnight black", "dark grey"),
        "Booty_Shorts": ("midnight black", "dark grey", "leather", "berry"),
        "Daisy_Dukes": ("light denim", "sky blue", "dark grey"),

        "Long_Skirt": ("midnight black", "leather"),
        "Pencil_Skirt": ("midnight black", "dark grey", "leather", "grey", "khaki", "white smoke", "berry", "indian yellow"),
        "Lace_Skirt": ("midnight black", "leather", "white smoke", "light grey"),
        "Skirt": ("khaki", "light grey", "leather", "light beige", "white smoke"),
        "Belted_Skirt": ("khaki", "grey", "leather", "light grey", "berry"),
        "Belted_Skirt_Pattern": ("leather", "dark grey"),
        "Mini_Skirt": ("khaki", "dark grey", "leather", "white smoke", "berry"),
        "Micro_Skirt": ("midnight black", "leather", "light grey", "white smoke"),

        "Lab_Coat": ("midnight black", "white smoke", "light grey"),
        "Suit_Jacket": ("midnight black", "white smoke", "dark denim", "dark grey"),
        "Vest": ("midnight black", "white smoke", "light grey", "leather"),

        "Short_Socks": ("white smoke", "light grey", "midnight black", "berry"),
        "Long_Socks": ("midnight black", "white smoke", "berry"),
        "High_Socks": ("midnight black", "white smoke", "light grey", "berry"),
        "Thigh_Highs": ("midnight black", "white smoke", "light grey", "mocha", "berry"),
        "Fishnets": ("midnight black", "white smoke", "dark grey", "berry"),
        "Garter_and_Fishnets": ("charcoal", "dark grey", "grey", "white smoke", "berry"),
        "Garter_and_Fishnets_Pattern": ("charcoal", "white smoke"),

        "Sandles": ("white smoke", "midnight black", "leather", "grey"),
        "Shoes": ("leather", "light grey"),
        "Slips": ("leather", "white smoke", "midnight black", "mocha", "dark grey"),
        "Sneakers": ("grey", "white smoke", "light beige"),
        "Sneakers_Pattern": ("white smoke",),
        "Sandal_Heels": ("midnight black", "grey", "white smoke", "light beige"),
        "Pumps": ("white smoke", "charcoal"),
        "Heels": ("midnight black", "charcoal", "white smoke"),
        "High_Heels": ("midnight black", "white smoke", "grey"),
        "Boot_Heels": ("leather", "grey"),
        "High_Boots": ("charcoal", "leather"),
        "Thigh_Boots": ("charcoal", "leather", "light grey"),

        "Tshirt": ("midnight black", "dark grey", "white smoke", "berry", "indian yellow"),
        "Tshirt_Pattern": ("grey", "light grey", "berry", "charcoal"),
        "Lace_Sweater": ("white smoke", "light grey", "midnight black", "berry", "indian yellow"),
        "Long_Sweater": ("midnight black", "light grey", "white smoke", "berry", "indian yellow"),
        "Sleveless_Top": ("midnight black", "dark grey", "white smoke", "berry", "indian yellow"),
        "Long_Tshirt": ("midnight black", "white smoke", "dark grey", "berry", "indian yellow"),
        "Long_Tshirt_Pattern": ("white smoke", "light grey", "light beige", "berry"),
        "Frilly_Longsleeve_Shirt": ("white smoke", "dark grey", "charcoal", "berry", "indian yellow"),
        "Sweater": ("leather", "white smoke", "charcoal", "khaki", "berry", "indian yellow"),
        "Belted_Top": ("leather", "khaki", "grey", "white smoke", "charcoal", "berry", "indian yellow"),
        "Lace_Crop_Top": ("charcoal", "light beige", "light grey", "white smoke", "berry", "indian yellow"),
        "Tanktop": ("leather", "white smoke", "grey", "midnight black", "berry", "indian yellow"),
        "Camisole": ("midnight black", "dark grey", "white smoke", "berry", "indian yellow"),
        "Long_Sleeve_Blouse": ("white smoke", "midnight black", "sky blue", "berry", "indian yellow"),
        "Short_Sleeve_Blouse": ("charcoal", "white smoke", "light beige", "light grey", "berry", "indian yellow"),
        "Wrapped_Blouse": ("charcoal", "light beige", "white smoke", "berry", "indian yellow"),
        "Tube_Top": ("white smoke", "midnight black", "dark grey", "charcoal", "berry", "indian yellow"),
        "Tie_Sweater": ("midnight black", "dark grey", "white smoke", "berry", "indian yellow"),
        "Tie_Sweater_Pattern": ("scarlet", "pale pink", "light grey", "light beige"),
        "Dress_Shirt": ("charcoal", "grey", "white smoke", "berry", "indian yellow"),
        "Tight_Vest": ("white smoke", "light beige", "dark grey", "charcoal", "berry", "indian yellow"),
        "Wool_Scarf": ("khaki", "charcoal", "grey", "white smoke", "berry", "indian yellow"),
        "Lace_Choker": ("charcoal", "white smoke", "dark grey", "berry", "pale pink", "indian yellow"),
        "Wide_Choker": ("charcoal", "white smoke", "dark grey", "berry", "pale pink", "indian yellow"),
        "Spiked_Choker": ("charcoal", "white smoke", "dark grey", "pale pink"),
        "Heart Pasties": ("charcoal", "venetian red", "scarlet", "berry"),
        "Cincher": ("charcoal", "dark grey", "venetian red", "pale pink", "leather"),
        "Cincher_Pattern": ("charcoal", "white smoke", "venetian red"),
        "Forearm_Gloves": ("charcoal", "light beige", "light grey", "white smoke", "berry"),
        "Forearm_Gloves_Pattern": ("charcoal", "pale pink", "white smoke"),

        "Copper_Bracelet": ("saffron",),
        "Gold_Bracelet": ("white smoke", "saffron"),
        "Spiked_Bracelet": ("white smoke",),
        "Colourful_Bracelets": ("grey", "venetian red", "scarlet", "berry"),
        "Diamond_Ring": ("saffron",),
        "Garnet_Ring": ("saffron",),
        "Copper_Ring_Set": ("saffron",),
        "Gold_Earings": ("saffron",),

        "Modern_Glasses": ("charcoal", "midnight black"),
        "Big_Glasses": ("charcoal", "midnight black"),
        "Sunglasses": ("charcoal", "midnight black"),
        "Head_Towel": ("white smoke",),
        # special version for underwear
        "Underwear": ("charcoal", "white smoke", "dark grey", "pale pink", "venetian red", "berry")
    }

    @staticmethod
    def clothing_in_preferences(topic: str, clothing: Clothing):
        return any(clothing.is_similar(item) for part in WardrobeBuilder.preferences[topic].values() for item in part)

    @staticmethod
    def get_color_from_opinion_color(opinion_color: str):
        return get_random_from_list([WardrobeBuilder.color_prefs[opinion_color][x][:] for x in WardrobeBuilder.color_prefs[opinion_color]])

    @staticmethod
    def get_item_color(item: Clothing, colour: list[float], exclude_list: list[str] = [], multiplier = 1.0):
        if item.proper_name in WardrobeBuilder.color_clothing_map:
            # exclude hate list
            available_list = [x for x in WardrobeBuilder.color_clothing_map[item.proper_name] if x not in exclude_list]
            if not available_list:
                # no color left revert to original list
                available_list = WardrobeBuilder.color_clothing_map[item.proper_name]

            # color not match list
            if WardrobeBuilder.get_color_opinion(colour) not in available_list:
                colour = get_random_from_list(list(WardrobeBuilder.color_prefs[get_random_from_list(available_list)].values()))[:]
                return [colour[0] * multiplier, colour[1] * multiplier, colour[2] * multiplier, colour[3]]
        return [colour[0] * multiplier, colour[1] * multiplier, colour[2] * multiplier, colour[3]]

    @staticmethod
    def get_color_opinion(colour: list[float]) -> str:
        if not isinstance(colour, list) or len(colour) not in (3, 4):
            return "the colour black"

        color_name = closest_preference_color(Color(rgb=(colour[0], colour[1], colour[2])))
        return next((topic for topic, colors in WardrobeBuilder.color_prefs.items() if color_name in colors), "the colour black")

    @staticmethod
    def get_color(person: Person, base_color: list[float] = None) -> list[float]:
        def get_excluded(base_color: list[float]) -> list[str]:
            if not base_color:
                return []
            opinion_color = WardrobeBuilder.get_color_opinion(base_color)
            if opinion_color in WardrobeBuilder.clashing_colour_map:
                return WardrobeBuilder.clashing_colour_map[opinion_color]
            return []

        color_list = []
        for cp in (x for x in WardrobeBuilder.color_prefs if x not in get_excluded(base_color)):
            score = person.opinion(cp)
            if score > -2: # don't append colors she hates
                color_list.extend(([WardrobeBuilder.color_prefs[cp][x][:], (score + 2) ** 2] for x in WardrobeBuilder.color_prefs[cp]))

        if not color_list:  # if she hates all colours
            for colors in WardrobeBuilder.color_prefs.values():
                color_list.extend(([colors[x][:], 5] for x in colors))

        return get_random_from_weighted_list(color_list)

    @staticmethod
    def apply_variation(color: list[float], max_variance = 10, fixed = False) -> list[float]:
        '''
        Applies a luminance shift to a color based on max_variance as percentage
        When fixed is true, apply variation of max_variance (pass negative for darker)
        '''
        hls = list(colorsys.rgb_to_hls(color[0], color[1], color[2]))
        variation = (max_variance if fixed else renpy.random.randint(-max_variance, max_variance)) / 100.0
        if variation == 0:  # quick exit if we don't change it
            return color
        if not fixed and renpy.random.randint(0, 1) == 0:
            variation *= -1 # make darker
        hls[1] = min(1, max(0, hls[1] + variation))
        rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
        # print(f"Received colour: {color}, applied {variation} variance, resulted in {rgb}")
        return list((*rgb, color[3]))

    @staticmethod
    def get_main_color_scheme(person: Person, match_percent = 60):
        primary_color = WardrobeBuilder.get_color(person)
        alternate_color = WardrobeBuilder.get_color(person, primary_color)

        col_choice = renpy.random.randint(0, 100)
        lower_percent = (100 - match_percent) // 2
        if col_choice < lower_percent:
            color_upper = primary_color
            color_lower = alternate_color
            color_feet = primary_color
        elif col_choice >= lower_percent and col_choice < match_percent:
            color_upper = primary_color
            color_lower = primary_color
            color_feet = alternate_color
        else:
            color_upper = primary_color
            color_lower = alternate_color
            color_feet = alternate_color

        # print("Upper: {}, Lower: {}, Feet: {}".format(
        #     closest_preference_color(Color(rgb=(color_upper[0], color_upper[1], color_upper[2]))),
        #     closest_preference_color(Color(rgb=(color_lower[0], color_lower[1], color_lower[2]))),
        #     closest_preference_color(Color(rgb=(color_feet[0], color_feet[1], color_feet[2])))))

        return (WardrobeBuilder.apply_variation(color_upper),
                WardrobeBuilder.apply_variation(color_lower),
                WardrobeBuilder.apply_variation(color_feet))

    @staticmethod
    def build_filter_list(item_list: list[Clothing], points: int, min_points: int = 0, filter_list: list[Clothing] = None, layers: list[int] = None) -> list[Clothing]:
        if filter_list is None:
            filter_list = []
        if layers is None:
            layers = [1, 2, 3, 4]

        if filter_list:
            work_list = [
                x for x in item_list
                if not any(x.is_similar(y) for y in filter_list)
            ]
        else:
            work_list = item_list

        if not work_list:   # no valid items
            return []

        min_actual = min(x.slut_value for x in work_list)
        max_actual = max(x.slut_value for x in work_list)

        points = max(points, min_actual)
        points = min(points, max_actual)
        min_points = min(min_points, points)

        return [x for x in work_list if x.slut_value >= min_points and x.slut_value <= points and x.layer in layers]

    @staticmethod
    def build_weighted_list(person: Person, item_group: str, filtered_list: list[Clothing]) -> list[Clothing, int]:
        '''
        Builds a weighted list of items from filtered list for specified item_group based on person preferences
        '''
        item_list = [[x, 0, True] for x in filtered_list]
        for (topic, clothing) in ((key, val[item_group]) for key, val in WardrobeBuilder.preferences.items() if item_group in val):
            score = person.opinion(topic)
            for item in (x for x in clothing if x in filtered_list):
                found = next((x for x in item_list if x[0] == item), None)
                if score == -2:
                    found[2] = False
                else:
                    found[1] += (score + 3) ** 2  # 4, 9, 16, 25

        # print(f"Build weighted list for {item_group} -> {len(item_list)}")
        for x in item_list: # skew towards person sluttiness
            if x[0].slut_score < person.sluttiness // 10:
                # print(f"Lowered {x[0].name} by {(8 - x[0].slut_value) * 2}")
                x[1] -= (8 - x[0].slut_value) * 2
            if x[1] < 0:
                x[1] = 0
            # print(f"{x[0].name}: {x[1]} - {x[2]}")

        # first return pref without hated, then without pref and hate, then with pref, then any item
        return [x for x in item_list if x[1] > 1 and x[2]] \
            or [x for x in item_list if x[1] > 0 and x[2]] \
            or [x for x in item_list if x[1] > 1] \
            or [x for x in item_list if x[1] > 0]

    @staticmethod
    def add_accessory_from_list(outfit: Outfit, filtered_list: list[Clothing], chance: int, item_color: list[float] = None):
        if item_color is None:
            item_color = [.8, .1, .1, .95]
        if renpy.random.randint(0, chance) == 0:
            if item := get_random_from_list(filtered_list):
                outfit.add_accessory(item.get_copy(), WardrobeBuilder.get_item_color(item, item_color))

    @staticmethod
    def get_item_from_list(person: Person, item_group: str, filtered_list: list[Clothing], no_pattern = False) -> Clothing | None:
        '''
        Returns a copy from a random clothing item from passed filtered_list based on person opinions and unlocked global policies (topless / nudity)
        '''
        if not filtered_list:
            return None

        if item_group == "special":
            item = get_random_from_list(filtered_list).get_copy()
        else:
            item: Clothing = get_random_from_weighted_list(WardrobeBuilder.build_weighted_list(person, item_group, filtered_list))
            if not item:    # make sure we have an item from the list
                item = get_random_from_list(filtered_list).get_copy()
            else:
                item = item.get_copy()

        if no_pattern or not item or len(item.supported_patterns) == 1:
            return item

        # force pattern for certain items, others random 50/50
        exclude = ["Default"] if item.always_use_pattern or item.underwear else []
        item.pattern = item.supported_patterns[get_random_from_list([x for x in item.supported_patterns.keys() if x not in exclude])]
        item.colour_pattern = WardrobeBuilder.get_color(person, item.colour)
        item.pattern_transparency = .80 + (renpy.random.randint(0, 15) / 100.0)    # random pattern transparency
        return item

    @staticmethod
    def get_clothing_min_max_slut_value(sluttiness: int) -> tuple[int, int]:
        base_sluttiness = builtins.max(sluttiness - 10, 0) # first 10 points of sluttiness don't impact outfit builder
        min_sluttiness = builtins.min(base_sluttiness // 20, 4) if sluttiness > 50 else 0 # prevent override of person preferences until she's slutty enough not to care
        return (min_sluttiness, builtins.min(base_sluttiness // 11, 8))

    @staticmethod
    def random_preference_color(color_list: list[str], exclude_list) -> list[float]:
        colors = [WardrobeBuilder.neutral_palette[x] for x in color_list]
        if not exclude_list:
            return WardrobeBuilder.apply_variation(get_random_from_list(colors))
        neutral_list = [x for x in colors if not WardrobeBuilder.get_color_opinion(x) in exclude_list]
        if not neutral_list:
            return WardrobeBuilder.apply_variation(get_random_from_list(colors))
        return WardrobeBuilder.apply_variation(get_random_from_list(neutral_list))

    @staticmethod
    def update_pattern_colour(item: Clothing, exclude_list: list[str] = None):
        color_key = item.proper_name + "_Pattern"
        if color_key in WardrobeBuilder.neutral_color_map:
            item.update_pattern_colour(WardrobeBuilder.random_preference_color(WardrobeBuilder.neutral_color_map[color_key], exclude_list))
        else:
            item.update_pattern_colour(WardrobeBuilder.random_preference_color(WardrobeBuilder.neutral_color_map["Underwear"], exclude_list))

    @staticmethod
    def neutralize_item_colour(item: Clothing, exclude_list: list[str] = []):
        '''
        Neutralizes the colour of the item based not using colors from the exclude list
        '''
        if not item:
            return None

        if (item.is_bra or item.is_one_piece):
            item.update_colour(WardrobeBuilder.random_preference_color(WardrobeBuilder.neutral_color_map["Underwear"], exclude_list))
            if item.pattern:
                item.update_pattern_colour(WardrobeBuilder.random_preference_color(WardrobeBuilder.neutral_color_map["Underwear"], exclude_list))
            return item

        if item.proper_name in WardrobeBuilder.neutral_color_map:
            item.update_colour(WardrobeBuilder.random_preference_color(WardrobeBuilder.neutral_color_map[item.proper_name], exclude_list))
            if item.proper_name == "Sneakers": #For sneakers we always set the pattern color to white (laces)
                item.pattern = item.supported_patterns[get_random_from_list(list(item.supported_patterns.keys()))]
                color_key = item.proper_name + "_Pattern"
                item.update_pattern_colour(WardrobeBuilder.random_preference_color(WardrobeBuilder.neutral_color_map[color_key], exclude_list))
            elif isinstance(item, Facial_Accessory):    #facial accessories don't have patterns
                pass
            elif item.pattern:
                WardrobeBuilder.update_pattern_colour(item, exclude_list)
        return item

    @staticmethod
    def update_item_colour(item: Clothing, colour: list[float], exclude_list: list[str] = None):
        item.update_colour(colour)
        if item.pattern:
            WardrobeBuilder.update_pattern_colour(item, exclude_list or [WardrobeBuilder.get_color_opinion(colour)])

    @staticmethod
    def add_make_up_to_outfit(person: Person, outfit: Outfit, make_up_score_boost = 0):
        # determine make-up colors based on skin-tone
        if person.skin == "black":
            eye_shadow_colours = [[.569, .349, .263, .9], [0, .2, .4, .9], [.47, .318, .663, .9]]
            lipstick_colours = [[.569, .318, .212, .8], [.451, .416, .526, .8], [.492, .419, .384, .8]]
            blush_colours = [[.435, .306, .216, .6], [.588, .251, 0, .6], [.451, .412, .576, .6]]
        else:
            eye_shadow_colours = [[.1, .1, .12, .9], [.4, .5, .9, .9], [.644, .418, .273, .9]]
            lipstick_colours = [[.745, .117, .235, .8], [1, .5, .8, .8], [.8, .26, .04, .8]]
            blush_colours = [[.34, .34, .32, .6], [1, .898, .706, .6], [.867, .627, .867, .6]]

        make_up_score = person.opinion.makeup + make_up_score_boost
        if make_up_score > 0 or (make_up_score <= 0 and renpy.random.randint(0, 4) == 0):
            make_up_score += renpy.random.randint(1, 2)
            if make_up_score > 0:
                outfit.add_accessory(light_eye_shadow.get_copy(), modify_transparency(get_random_from_list(eye_shadow_colours), 0.5))
            if make_up_score > 1:
                outfit.add_accessory(heavy_eye_shadow.get_copy(), modify_transparency(get_random_from_list(eye_shadow_colours), 0.5))
            if make_up_score > 2:
                outfit.add_accessory(lipstick.get_copy(), modify_transparency(get_random_from_list(lipstick_colours), 0.4))
            if make_up_score > 3:
                outfit.add_accessory(blush.get_copy(), modify_transparency(get_random_from_list(blush_colours), .2))

    def __init__(self, person: Person | None):
        if isinstance(person, Person):
            self.person = person
        else:
            if WardrobeBuilder.default_person is None:
                WardrobeBuilder.default_person = create_random_person(name ="Ema", last_name = "Hesire", age = 23, stat_array = [3, 3, 3], skill_array = [3, 3, 3, 3, 3], sex_skill_array = [3, 3, 3, 3], body_type = "thin_body", tits = "B")
                WardrobeBuilder.default_person.opinions.clear() # reset opinions so every item has an equal chance
                WardrobeBuilder.default_person.sexy_opinions.clear()

            self.person = WardrobeBuilder.default_person

        skirts_score = self.person.opinion.skirts
        pants_score = self.person.opinion.pants
        dress_score = self.person.opinion.dresses

        # person hates all main clothing items, make her like skirts.
        if skirts_score + pants_score + dress_score == -6:
            self.person.opinions["skirts"] = [1, True]

    def build_outfit(self, outfit_type: Literal['over', 'under', 'full'], points: int, min_points: int = 0) -> Outfit:
        if outfit_type == "over":
            return self.build_overwear(points, min_points)
        if outfit_type == "under":
            return self.build_underwear(points, min_points)

        underwear = self.build_underwear(points, min_points)
        overwear = self.build_overwear(points, min_points)

        outfit = Wardrobe.build_assembled_outfit(underwear, overwear)

        # make sure we are wearing panties on medium high sluttiness (no commando)
        if (points < 7 and not outfit.wearing_panties):
            self.person.set_sexier_panties(outfit, min_slut = min_points, max_slut = points)

        # make sure we are wearing a bra on lower than average sluttiness
        if (points < 5 and not outfit.wearing_bra):
            self.person.set_sexier_bra(outfit, min_slut = min_points, max_slut = points)

        if outfit.is_legal_in_public:
            return outfit

        if outfit.vagina_visible:   # make sure vagina is covered so it's a legal outfit
            self.person.set_sexier_panties(outfit, min_slut = min_points, max_slut = points)

        if outfit.is_legal_in_public:
            return outfit

        if outfit.tits_visible:     # make sure tits are covered so it's a legal outfit
            self.person.set_sexier_bra(outfit, allow_remove_bra = False, min_slut = min_points, max_slut = points)

        return outfit # should be legal now

    def build_overwear(self, points: int = 0, min_points: int = 0) -> Outfit:
        def make_upper_item_transparent(item: Clothing, points: int, colour: list[float]) -> tuple[Clothing, list[float]]:
            colour[3] = .95
            if item.layer == 3 and item.slut_value > 0 and points > 5 and (item.is_shirt or item.is_dress):
                colour[3] = .75 + (renpy.random.randint(0, 15) / 100.0)
            elif points > 1:
                colour[3] = .85 + (renpy.random.randint(0, 10) / 100.0)
            return item, colour

        def make_lower_item_transparent(item: Clothing, points: int, colour: list[float]) -> tuple[Clothing, list[float]]:
            colour[3] = .95
            if item.layer == 3 and item.slut_value > 0 and points > 5 and (item.is_shirt or item.is_pants):
                colour[3] = .75 + (renpy.random.randint(0, 15) / 100.0)
            elif points > 1:
                colour[3] = .85 + (renpy.random.randint(0, 10) / 100.0)
            return item, colour

        outfit = Outfit("Overwear")
        item = None

        color_upper, color_lower, color_feet = WardrobeBuilder.get_main_color_scheme(self.person)
        color_hate_list = self.person.hated_color_opinions

        # decide if person will wear overwear
        if not (mc.business.topless_is_legal and points >= 7
            and ((self.person.opinion.not_wearing_anything > -2
                and renpy.random.randint(0, 4 - self.person.opinion.not_wearing_anything) == 0)
                or self.person.has_exhibition_fetish)):

            upper_item_list = real_shirt_list + [suit_jacket, camisole, vest, kitty_babydoll] + (real_dress_list if points > 1 else [])
            # find upper body item
            if item := WardrobeBuilder.get_item_from_list(self.person, "upper_body", WardrobeBuilder.build_filter_list(upper_item_list, points, min_points)):
                outfit.add_upper(*make_upper_item_transparent(item, points, WardrobeBuilder.get_item_color(item, color_upper, color_hate_list)))

            # we added a overlay item, so find a real upper item this time
            if item and item.layer == 4 and not item.has_extension:
                if item := WardrobeBuilder.get_item_from_list(self.person, "upper_body", WardrobeBuilder.build_filter_list(upper_item_list, points, min_points, layers = [3])):
                    outfit.add_upper(*make_upper_item_transparent(item, points, WardrobeBuilder.get_item_color(item, color_lower, color_hate_list)))

        if not (mc.business.nudity_is_legal and points >= 7
            and (self.person.opinion.not_wearing_anything > -2
                and renpy.random.randint(0, 4 - self.person.opinion.not_wearing_anything) == 0)
                or self.person.has_exhibition_fetish):

            # find lowerbody item
            if not item or (not item.has_extension or item.has_extension.layer == 2):
                if item := WardrobeBuilder.get_item_from_list(self.person, "lower_body", WardrobeBuilder.build_filter_list(real_pants_list + skirts_list, points, min_points)):
                    outfit.add_lower(*make_lower_item_transparent(item, points, WardrobeBuilder.get_item_color(item, color_lower, color_hate_list, 0.9)))

        # find feet item
        if item := WardrobeBuilder.get_item_from_list(self.person, "feet", WardrobeBuilder.build_filter_list(shoes_list, points, min_points)):
            outfit.add_feet(item, WardrobeBuilder.get_item_color(item, color_feet, color_hate_list, 0.8))

        # special case where we randomly add tights to outerwear (when combining we check if underwear has socks / hose, and skip tights)
        if renpy.random.randint(0, 1) == 0:
            if item := WardrobeBuilder.get_item_from_list(self.person, "lower_body", WardrobeBuilder.build_filter_list(tights_list, points, min_points)):
                outfit.add_lower(*make_lower_item_transparent(item, points, WardrobeBuilder.get_item_color(item, color_lower, color_hate_list, 0.9)))

        # special case (leotard without skirt or pants)
        if outfit.has_clothing(leotard) and not (outfit.has_skirt or outfit.has_pants):
            if item := WardrobeBuilder.get_item_from_list(self.person, "lower_body", WardrobeBuilder.build_filter_list(real_pants_list + skirts_list, points, min_points)):
                outfit.add_lower(*make_lower_item_transparent(item, points, WardrobeBuilder.get_item_color(item, color_lower, color_hate_list, 0.9)))

        # random chance of adding outfit custom makeup (base on pref for make-up)
        if self.person.opinion.makeup > -2 and renpy.random.randint(0, 4 - self.person.opinion.makeup) == 0:
            # add makeup to outfit (overrides makeup in base_outfit)
            WardrobeBuilder.add_make_up_to_outfit(self.person, outfit)

        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(earings_only_list, points, min_points, self.person.base_outfit.accessories), 1, color_lower)
        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(rings_list, points, min_points, self.person.base_outfit.accessories), 1, colour_yellow)
        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(bracelet_list, points, min_points, self.person.base_outfit.accessories), 2, color_upper)
        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(neckwear_without_collars, points, min_points, self.person.base_outfit.accessories), 3, color_upper)

        outfit.update_name()
        return outfit

    def build_underwear(self, points: int = 0, min_points: int = 0) -> Outfit:
        def make_upper_item_transparent(item: Clothing, points: int, colour: list[float]) -> tuple[Clothing, list[float]]:
            colour[3] = .95
            if points >= 6 and item.slut_value > 0 and (item.is_one_piece or item.is_bra):
                colour[3] = .7 + (renpy.random.randint(0, 20) / 100.0)
            elif points > 1:
                colour[3] = .90 + (renpy.random.randint(0, 5) / 100.0)
            return item, colour

        def make_lower_item_transparent(item: Clothing, points: int, colour: list[float]) -> tuple[Clothing, list[float]]:
            colour[3] = .95
            if points >= 6 and item.slut_value > 0 and item.is_panties:
                colour[3] = .7 + (renpy.random.randint(0, 20) / 100.0)
            elif points > 1:
                colour[3] = .90 + (renpy.random.randint(0, 5) / 100.0)
            return item, colour

        outfit = Outfit("Underwear")
        item = None

        color_upper, color_lower, color_feet = WardrobeBuilder.get_main_color_scheme(self.person, match_percent = 80) # underwear mismatch is less likely

        # decide if person will wear underwear
        if not (points >= 7
            and ((self.person.opinion.not_wearing_anything > -2
                and renpy.random.randint(0, 4 - self.person.opinion.not_wearing_anything) == 0)
                or self.person.has_exhibition_fetish)):

            upper_list = real_bra_list

            # find upper body item
            if item := WardrobeBuilder.get_item_from_list(self.person, "upper_body", WardrobeBuilder.build_filter_list(upper_list + one_piece_list, points, min_points)):
                outfit.add_upper(*make_upper_item_transparent(item, points, color_upper))

        if not (points >= 7
            and (self.person.opinion.not_wearing_anything > -2
                and renpy.random.randint(0, 4 - self.person.opinion.not_wearing_anything) == 0)
                or self.person.has_exhibition_fetish):

            # find lower body item
            if not item or not item.has_extension:
                if item and item.proper_name in WardrobeBuilder.matching_underwear:
                    item = WardrobeBuilder.get_item_from_list(self.person, "lower_body", WardrobeBuilder.build_filter_list(WardrobeBuilder.matching_underwear[item.proper_name], points, min_points))
                else:
                    item = WardrobeBuilder.get_item_from_list(self.person, "lower_body", WardrobeBuilder.build_filter_list(panties_list, points, min_points))
                if item:
                    outfit.add_lower(*make_lower_item_transparent(item, points, color_upper))

        # random chance of adding sexy underwear part (heart pasties / cincher)
        if points >= 7 and renpy.random.randint(0, 3 - self.person.opinion.lingerie) == 0:
            item = WardrobeBuilder.get_item_from_list(self.person, "special", [cincher, heart_pasties])
            outfit.add_upper(*make_upper_item_transparent(item, points, color_lower), colour_pattern = color_upper)

        # random socks (with high points we definitely wear socks)
        if min_points > 2 or points >= 6 or renpy.random.randint(0, 1) == 0:
            if points >= 5:
                item = WardrobeBuilder.get_item_from_list(self.person, "feet", WardrobeBuilder.build_filter_list([x for x in socks_list if x not in (short_socks, medium_socks)], points, min_points))
            else:
                item = WardrobeBuilder.get_item_from_list(self.person, "feet", WardrobeBuilder.build_filter_list(socks_list, points, min_points))
            if item:
                outfit.add_feet(item.get_copy(), color_feet)

        # random shoes (with high points we definitely wear shoes)
        if min_points > 2 or points >= 6 or renpy.random.randint(0, 1) == 0:
            if item := WardrobeBuilder.get_item_from_list(self.person, "feet", WardrobeBuilder.build_filter_list(shoes_list, points, min_points)):
                outfit.add_feet(item, WardrobeBuilder.get_item_color(item, color_feet, self.person.hated_color_opinions, 0.8))

        # random chance of adding outfit custom makeup (base on pref for make-up)
        if self.person.opinion.makeup > -2 and renpy.random.randint(0, 4 - self.person.opinion.makeup) == 0:
            # add makeup to outfit (overrides makeup in base_outfit)
            WardrobeBuilder.add_make_up_to_outfit(self.person, outfit)

        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(rings_list, points, min_points, self.person.base_outfit.accessories), 1, colour_yellow)
        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(bracelet_list, points, min_points, self.person.base_outfit.accessories), 2, color_upper)
        WardrobeBuilder.add_accessory_from_list(outfit, WardrobeBuilder.build_filter_list(neckwear_without_collars, points, min_points, self.person.base_outfit.accessories), 3, color_upper)

        outfit.update_name()
        return outfit

    def personalize_outfit(self, outfit: Outfit, opinion_color: str | None = None, coloured_underwear = True, main_colour: list[float] | None = None, swap_bottoms = False, allow_skimpy = True) -> Outfit:
        outfit.remove_all_collars()
        outfit.remove_all_cum()
        outfit.restore_all_clothing()

        #First, get a theme color
        if opinion_color is None:
            if main_colour:
                opinion_color = WardrobeBuilder.get_color_opinion(main_colour)
            elif renpy.random.randint(0, 100) < 50:  #50% chance we go straight to a favourite color.
                main_colour = WardrobeBuilder.get_color(self.person)
                opinion_color = WardrobeBuilder.get_color_opinion(main_colour)
            else:
                opinion_color = self.person.favourite_colour

        color_list = [WardrobeBuilder.color_prefs[opinion_color][x][:] for x in WardrobeBuilder.color_prefs[opinion_color]]
        if main_colour is None:
            main_colour = get_random_from_list(color_list)

        main_colour = WardrobeBuilder.apply_variation(main_colour)
        color_hate_list = self.person.hated_color_opinions

        underwear_colour = None
        if coloured_underwear:
            if renpy.random.randint(0, 100) < 70: #70% chance to use similar color as outfit theme
                underwear_colour = get_random_from_list(color_list)
            else:
                underwear_colour = WardrobeBuilder.get_color(self.person, main_colour)

        if swap_bottoms:
            self.person.apply_outfit_bottom_preference(outfit)

        if allow_skimpy:
            if outfit.wearing_panties:
                self.person.set_sexier_panties(outfit, underwear_colour)
            if outfit.wearing_bra:
                self.person.set_sexier_bra(outfit, underwear_colour)

        #Next, determine what kind of outfit this is.
        if outfit.has_dress: #If it is a dress, let the dress be the focal point of the outfit.
            # print("Personalise outfit dress branch")
            for item in outfit.upper_body:
                if underwear_colour and (item.is_bra or item.is_one_piece):
                    WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                elif item.is_dress:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

            if not underwear_colour and outfit.wearing_bra:
                underwear_colour = outfit.get_bra().colour

            for item in (x for x in outfit.lower_body if not x.is_extension):
                if underwear_colour and item.is_panties:
                    WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            for item in outfit.feet:
                WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        elif outfit.has_pants: #This outfit has lower body pants covering.
            # print("Personalise outfit pants branch")
            #First determine if we want to switch to a skirt.
            #Next, figure out what kind of top we have. Regular, bra, or topless.
            if outfit.tits_visible:   #Tits are on display, but she may have a top still. Colour her top (if there) and pants
                for item in outfit.upper_body:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                for item in (x for x in outfit.lower_body if not x.is_extension):
                    if underwear_colour and item.is_panties:
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    elif item.is_pants:
                        WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            elif not outfit.bra_covered: #Bra is on display, use that for our colour theme. Bra is focal point of outfit, so neutralize pants
                for item in outfit.upper_body:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                for item in (x for x in outfit.lower_body if not x.is_extension):
                    if underwear_colour and item.is_panties:
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            else: #Assume a decent top is being worn. Top is the focal point of the outfit
                for item in outfit.upper_body:
                    if underwear_colour and (item.is_bra or item.is_one_piece):
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    elif item.is_shirt:
                        WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

                if not underwear_colour and outfit.wearing_bra:
                    underwear_colour = outfit.get_bra().colour

                for item in (x for x in outfit.lower_body if not x.is_extension):
                    if underwear_colour and item.is_panties:
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

            for item in outfit.feet:
                if item.proper_name == "Sneakers":
                    WardrobeBuilder.neutralize_item_colour(item)
                    item.update_pattern_colour(main_colour)
                elif renpy.random.randint(0, 100) < 30 and item.is_shoes: #Normally we neutralize feet, but have a chance at having a matching set of shoes
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        elif outfit.has_skirt: #This outfit has a skirt.
            # print("Personalise outfit skirt branch")
            #Similar logic to pants. First determine if we should switch to pants
            #Next, determine what kind of top is being worn.
            if outfit.tits_visible:   #Tits are on display, but she may have a top still. Colour her top (if there) and skirt
                for item in outfit.upper_body:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                for item in (x for x in outfit.lower_body if not x.is_extension):
                    if underwear_colour and item.is_panties:
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    elif item.is_skirt:
                        WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            elif not outfit.bra_covered: #Bra is on display, use that for our colour theme. Bra is focal point of outfit, so neutralize skirt
                for item in outfit.upper_body:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                for item in (x for x in outfit.lower_body if not x.is_extension):
                    if underwear_colour and item.is_panties:
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            else:   #She's wearing a full outfit. Probably top is focal point, but there is a CHANCE that she may decide to make the skirt the outfit focal point.
                skirt_focus = renpy.random.randint(0, 100) < 30  #30% chance for skirt focus
                for item in outfit.upper_body:
                    if underwear_colour and (item.is_bra or item.is_one_piece):
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    elif not skirt_focus and item.is_shirt:
                        WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

                if not underwear_colour and outfit.wearing_bra:
                    underwear_colour = outfit.get_bra().colour

                for item in (x for x in outfit.lower_body if not x.is_extension):
                    if underwear_colour and item.is_panties:
                        WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                    elif item.is_skirt:
                        if skirt_focus:
                            WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                        else:
                            WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
                    else:
                        WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

            for item in outfit.feet:
                if item.proper_name == "Sneakers":
                    WardrobeBuilder.neutralize_item_colour(item)
                    item.update_pattern_colour(main_colour)
                elif renpy.random.randint(0, 100) < 30 and item.is_shoes: #Normally we neutralize feet, but have a chance at having a matching set of shoes
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        #Next type of outfit: housewear. Girl comfy clothes general in game are some top with just panties or no panties. EG mom's apron, pyjamas, etc.
        #With this outfit, tits will be covered. Make top the focal point.
        elif outfit.has_shirt:
            # print("Personalise outfit shirt branch")
            for item in outfit.upper_body:
                if underwear_colour and (item.is_bra or item.is_one_piece):
                    WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                elif item.is_shirt:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

            if not underwear_colour and outfit.wearing_bra:
                underwear_colour = outfit.get_bra().colour

            for item in (x for x in outfit.lower_body if not x.is_extension):
                if underwear_colour and item.is_panties:
                    WardrobeBuilder.update_item_colour(item, underwear_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

            for item in outfit.feet:
                if item.proper_name == "Sneakers":
                    WardrobeBuilder.neutralize_item_colour(item)
                    item.update_pattern_colour(main_colour)
                elif renpy.random.randint(0, 100) < 30 and item.is_shoes: #Normally we neutralize feet, but have a chance at having a matching set of shoes
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        #This outfit does not have lower or upper body covering. Could be just underwear or lingerie.
        #First, check and see if this is just an underwear set. In that case, colour all underwear as main color.
        #To differentiate between underwear and lingerie, check and see if it is classic underwear set via layers.
        #If bottom layer only, check sluttiness rating and access and for pantyhose vs socks and determine if we treat as just underwear or as lingerie
        elif outfit.is_suitable_underwear_set and not (outfit.has_thigh_high_socks or outfit.underwear_slut_score > 25):
            # print("Personalise outfit non-sexy underwear branch")
            #Make underwear main color, neutralize everything else.
            for item in outfit.upper_body:
                if (item.is_bra or item.is_one_piece):
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            for item in (x for x in outfit.lower_body if not x.is_extension):
                if item.is_panties:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)
            for item in outfit.feet:
                if item.is_socks and renpy.random.randint(0, 100) < 70:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        else: #This is for exciting, lingerie style outfits. Lingerie is generally completely color matching, maybe with only one or two neutral pieces.
            # print("Personalise outfit sexy underwear branch")
            for item in outfit.upper_body:
                WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
            for item in (x for x in outfit.lower_body if not x.is_extension):
                WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
            for item in outfit.feet:
                if item.is_socks and renpy.random.randint(0, 100) < 70:
                    WardrobeBuilder.update_item_colour(item, main_colour, color_hate_list)
                else:
                    WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        for item in outfit.accessories:
            WardrobeBuilder.neutralize_item_colour(item, color_hate_list)

        # give high socks a high transparency
        for x in (x for x in outfit.feet if x.proper_name == "High_Socks"):
            x.transparency = .33
            if x.pattern:
                x.pattern_transparency = .5

        return outfit
