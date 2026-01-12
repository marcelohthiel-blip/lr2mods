from __future__ import annotations
from game.sex_positions._position_definitions_ren import doggy_anal_dildo_dp, doggy, doggy_anal, piledriver_dp, standing_finger, standing_dildo, piledriver
from game.main_character.perks.Perks_ren import Item_Perk, perk_system
from game.major_game_classes.game_logic.Position_ren import list_of_positions

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def male_strapon_on_unlock():
    male_strapon_save_load()

def male_strapon_save_load():
    if doggy_anal_dildo_dp not in list_of_positions:
        #print("Add position")
        list_of_positions.append(doggy_anal_dildo_dp)
    if doggy_anal_dildo_dp not in doggy.connections:
        #print("Add doggy link")
        doggy.link_positions(doggy_anal_dildo_dp, "transition_doggy_doggy_anal_dildo_dp")
    if doggy_anal_dildo_dp not in doggy_anal.connections:
        #print("Add doggy-anal link")
        doggy_anal.link_positions(doggy_anal_dildo_dp, "transition_doggy_anal_doggy_anal_dildo_dp")
    if piledriver_dp not in piledriver.connections:
        #print("Add piledriver link")
        piledriver.link_positions(piledriver_dp, "transition_piledriver_piledriver_dp")

def male_strapon_unlock(): #This function is wrapper to unlock the male strap-on. This is in testing
    if perk_system.has_item_perk("Male Strapon"):
        return False

    item_perk_male_strapon = Item_Perk("A strap-on designed to be worn by men. Useful for double penetration!",
        on_unlock = male_strapon_on_unlock,
        save_load = male_strapon_save_load)

    perk_system.add_item_perk(item_perk_male_strapon, "Male Strapon")
    return True

def dildo_on_unlock():
    dildo_save_load()

def dildo_save_load():
    if standing_dildo not in standing_finger.connections:
        #print("Add standing finger link")
        standing_finger.link_positions(standing_dildo, "transition_standing_finger_standing_dildo")

def dildo_unlock():
    if perk_system.has_item_perk("Dildo"):
        return False

    item_perk_dildo = Item_Perk("A dildo, useful for penetrating any consenting orifice.",
        on_unlock = dildo_on_unlock,
        save_load = dildo_save_load)

    perk_system.add_item_perk(item_perk_dildo, "Dildo")
    return True
