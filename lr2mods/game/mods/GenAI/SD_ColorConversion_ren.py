import builtins
from collections import OrderedDict
from game.helper_functions.webcolors_ren import closest_color_name, normalize_hex, rgb_fraction_to_rgb, rgb_to_hex
from renpy.color import Color

"""renpy
init -1 python:
"""

color_prefs: dict[str, OrderedDict[str, list[list[float]]]] = {}
color_prefs["the colour blue"] = OrderedDict([
    ("purple", [[.282, .239, .545, .95]]),
    ("navy blue", [[0, .278, .671, .95]]),
    ("blue", [[.082, .376, .741, .95], [.529, .808, .922, 0.95]]),
    ("light blue", [[.0275, .51, .706, .95], [.365, .678, .925, .95], [.392, .584, .929, .95]]),
])
color_prefs["the colour yellow"] = OrderedDict([
    ("brown", [[.765, .69, .569, .95]]),
    ("orange", [[.89, .659, .341, .95]]),
    ("yellow", [
        [.8862, .79215, .4627, .95],
        [.9333, .8627, .5098, .95],
        [.96, .77, .19, .95],
        [.98, .92, .36, .95],
    ]),
])
color_prefs["the colour red"] = OrderedDict([
    ("dark red", [[.38, .118, .149, .95], [.478, .09, .071, .95]]),
    ("red", [
        [.7843, .0313, .08235, .95],
        [.890, .258, .203, .95],
        [.843, .039, .325, .95],
    ]),
    ("purple", [[.80, .26, .04, .95]]),
])
color_prefs["the colour pink"] = OrderedDict([
    ("light pink", [[.906, .329, .502, .95], [.9647, .2901, .54117, .95]]),
    ("hot pink", [[1, .412, .706, .95]]),
    ("faded pink", [[.9647, .6784, .7764, .95]]),
    ("pink", [[.98, .885, .867, .95], [1, .733, .851, .95]]),
])
color_prefs["the colour black"] = OrderedDict([
    ("black", [[.15, .15, .15, .95]]),
    ("dark teal", [[.212, .271, .31, .95], [0, .26, .36, .95]]),
    ("dark grey", [[.365, .365, .365, .95]]),
])
color_prefs["the colour green"] = OrderedDict([
    ("army green", [[.294, .325, .125, .95]]),
    ("sea green", [[.18, .545, .341, .95]]),
    ("green", [[0, .659, .43, .95], [0, .8, .6, .95]]),
    ("light green", [[.576, .772, .447, .95]]),
])
color_prefs["the colour purple"] = OrderedDict([
    ("dark purple", [[.4, .0078, .23529, .95], [.41, .16, .38, .95]]),
    ("purple", [[.45, .31, .59, .95], [.5764, .4392, .8588, .95]]),
    ("light purple", [[.714, .4, .824, .95], [.878, .690, 1, .95]]),
])
color_prefs["the colour orange"] = OrderedDict([
    ("dark orange", [[0.6235, 0.3294, 0, .95], [.8, .33, 0, .95]]),
    ("orange", [
        [.878, .552, .235, .95],
        [.89, .6, .16, .95],
        [1, .6901, .3647, .95],
    ]),
    ("red", [[.859, .331, .321, .95]]),
])
color_prefs["the colour white"] = OrderedDict([
    ("dark white", [[.8823, .8509, .8196, .95]]),
    ("white", [
        [.992, .953, .918, .95],
        [.95, .95, .95, .95],
        [.97, .97, 1, .95],
        [.98, .922, .843, .95],
    ]),
])
color_prefs["the colour brown"] = OrderedDict([
    ("dark brown", [
        [.352, .239, .239, .95],
        [.384, .29, .18, .95],
        [.435, .305, .215, .95],
    ]),
    ("brown", [[.451, .313, .235, .95], [.514, .373, .345, .95]]),
    ("light brown", [[.765, .69, .569, .95]]),
    ("light beige", [[.94, .94, .78, .95]]),
])

def SD_get_color_opinion(colour: list[float], colour_overrides: {}) -> str:
    hex_codes_to_names = {}
    if colour_overrides:
        for colour_name, value in colour_overrides.items():
            if isinstance(value, builtins.list):
                hex_values = value
            else:
                hex_values = [value]
            for hex_value in hex_values:
                hex_codes_to_names[normalize_hex(hex_value)] = colour_name
    else:
        for g_prefs in color_prefs.values():
            for g_name, g_colors_list in g_prefs.items():
                for g_color in g_colors_list:
                    if len(g_color) >= 3:
                        try:
                            rgb_tuple = rgb_fraction_to_rgb((g_color[0], g_color[1], g_color[2]))
                            hex_code = normalize_hex(rgb_to_hex(rgb_tuple))
                            hex_codes_to_names[hex_code] = g_name
                        except ValueError:
                            pass

    if not hex_codes_to_names:
        return "black"

    try:
        input_color_obj = Color(rgb=(colour[0], colour[1], colour[2]))
    except (IndexError, TypeError):
        return "black"

    try:
        return closest_color_name(input_color_obj, hex_codes_to_names)
    except ValueError:
        return "black"
