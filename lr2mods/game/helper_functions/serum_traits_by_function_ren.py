from __future__ import annotations
import builtins
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def serum_traits_by_function(function = "Medical", researched = True) -> list[SerumTrait]:
    return_trait_list: list[SerumTrait] = []
    if function == "Medical":
        return_trait_list = [x for x in list_of_traits
            if x.medical_aspect > builtins.max(x.mental_aspect, x.physical_aspect, x.sexual_aspect)
            and not any(tag for tag in x.exclude_tags if tag in ["Production", "Suggest", "Dye", "Nanobots"])
        ]
    elif function == "Mental":
        return_trait_list = [x for x in list_of_traits
            if x.mental_aspect > builtins.max(x.medical_aspect, x.physical_aspect, x.sexual_aspect)
            and not any(tag for tag in x.exclude_tags if tag in ["Production", "Suggest", "Dye", "Nanobots"])
        ]
    elif function == "Physical":
        return_trait_list = [x for x in list_of_traits
            if x.physical_aspect > builtins.max(x.medical_aspect, x.mental_aspect, x.sexual_aspect)
            and not any(tag for tag in x.exclude_tags if tag in ["Production", "Suggest", "Dye", "Nanobots"])
        ]
    elif function == "Sexual":
        return_trait_list = [x for x in list_of_traits
            if x.sexual_aspect > builtins.max(x.medical_aspect, x.mental_aspect, x.physical_aspect)
            and not any(tag for tag in x.exclude_tags if tag in ["Production", "Suggest", "Dye", "Nanobots"])
        ]
    elif function == "Duration":
        return_trait_list = [x for x in list_of_traits if x.duration_added > 0]
    elif function == "Production":
        return_trait_list = [x for x in list_of_traits if "Production" in x.exclude_tags]
    elif function == "Suggest":
        return_trait_list = [x for x in list_of_traits if "Suggest" in x.exclude_tags]
    elif function == "Nanobots":
        return_trait_list = [x for x in list_of_traits if "Nanobots" in x.exclude_tags]

    if researched:
        return [x for x in return_trait_list if x.researched and x.tier < 6]

    return return_trait_list
