from __future__ import annotations
from game.clothing_lists_ren import sports_bra, tanktop, cotton_panties, skirt, sneakers, short_socks
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Role_ren import Role
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""



def stephanie_get_tennis_outfit():
    outfit = Outfit("Stephanie Tennis Outfit")
    outfit.add_upper(sports_bra.get_copy(), [.56, .1, .06, 0.95])
    outfit.add_upper(tanktop.get_copy(), [1.0, 1.0, 1.0, .85])
    outfit.add_lower(cotton_panties.get_copy(), [.56, .1, .06, 0.95])
    outfit.add_lower(skirt.get_copy(), [.94, .94, 1.0, .95])
    outfit.add_feet(sneakers.get_copy(), [1.0, .81, 1.0, 0.95], "Pattern_1", [1.0, 1.0, 1.0, 0.95])
    outfit.add_feet(short_socks.get_copy(), [1.0, 1.0, 1.0, 0.95])
    return outfit
