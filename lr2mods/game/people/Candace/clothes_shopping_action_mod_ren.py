from __future__ import annotations
from game.people.Candace.candace_role_definition_ren import candace_get_has_gone_clothes_shopping
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.character_related.Person_ren import Person, mc
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

def invite_to_clothes_shopping_requirement():
    if not candace_get_has_gone_clothes_shopping():
        return False
    if not mc.business.has_funds(500):
        return "Requires $500"
    return True

def build_outfit_selection(person: Person):
    outfits = []
    for x in range(3):
        outfits.append(Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = person.sluttiness + (x * 5)))
    outfits.append(Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under"))
    return outfits

invite_to_clothes_shopping = ActionMod("Invite someone to shop {image=time_advance}", invite_to_clothes_shopping_requirement, "invite_to_clothes_shopping_label",
    menu_tooltip = "Invite a person to go clothes shopping.", category="Mall")
