from __future__ import annotations
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.major_game_classes.game_logic.Room_ren import mall_salon
from game.major_game_classes.character_related.Person_ren import Person, mc, salon_manager
from game.people.Ophelia.ophelia_definition_ren import salon_total_cost
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

def hair_salon_mod_initialization(self):
    # add haircut action to mall salon
    mall_salon.add_action(self)

# Note that the class Room have a bunch of useful variables already for restricting access, adding objects etc.
def salon_requirement():
    if not mc.business.has_funds(salon_total_cost): # $60 for hair cut, $30 for dye. You won't be spending your last money on haircuts.
        return "Requires $[salon_total_cost]"
    return True


salon_action = ActionMod("Schedule a haircut {image=time_advance}", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization,
    menu_tooltip = "Change a person's hair style and color.", category="Mall")
