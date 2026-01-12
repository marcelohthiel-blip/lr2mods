from __future__ import annotations
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import clinical_testing

day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
list_of_instantiation_functions.append("init_pigment_alteration_serum")

def pigment_serum_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    skin_styles = [x[0] for x in Person._list_of_skins if x[0] != person.skin]
    new_skin = get_random_from_list(skin_styles)
    return person.match_skin(new_skin)

def init_pigment_alteration_serum():
    SerumTraitMod(name = "Pigment Trait",
        desc = "Causes instantaneous alterations in the subject's pigment distribution causing noticeable changes in skin colour",
        positive_slug = "Changes the subject's skin colour",
        negative_slug = "",
        research_added = 125,
        base_side_effect_chance = 20,
        on_apply = pigment_serum_on_apply,
        requires = clinical_testing,
        tier = 3,
        research_needed = 500,
        clarity_cost = 2500,
        hidden_tag = "Physical",
        mental_aspect = 3, physical_aspect = 6, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 3)
