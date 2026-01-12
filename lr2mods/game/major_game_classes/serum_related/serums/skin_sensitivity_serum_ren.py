# Skin sensitivity serum original by Kaden
from __future__ import annotations
import renpy
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import clinical_testing

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("init_skin_sensitivity_serum_serum")

def skin_sensitivity_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    test_outfit = person.current_planned_outfit.get_copy()

    cloth = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
    if not cloth:
        return # nothing to strip
    test_outfit.remove_clothing(cloth)
    if not person.judge_outfit(test_outfit):
        return # too slutty
    if cloth in person.outfit.upper_body and test_outfit.tits_visible and person.has_taboo("bare_tits"):
        return # won't strip to tits
    if cloth in person.outfit.lower_body and test_outfit.vagina_visible and person.has_taboo("bare_pussy"):
        return # won't strip to vagina
    if test_outfit.underwear_visible and person.has_taboo("underwear_nudity"):
        return # won't strip to underwear

    person.current_planned_outfit = test_outfit

    if add_to_log:
        # she is wearing it and we can see her
        if mc.is_at(person.location):
            person.draw_animated_removal(cloth)
            renpy.say(None, f"It seems {person.possessive_title} is affected by the skin sensitivity serum.")
        mc.log_event(f"{person.display_name}: Removed her {cloth.display_name}", "float_text_grey")

def skin_sensitivity_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_stats(happiness = -2 if person.location.is_public else 0,
        arousal = 5 if person.arousal_perc < 50 else 0, add_to_log = add_to_log)

def init_skin_sensitivity_serum_serum():
    SerumTraitMod(name = "Skin Sensitivity",
        desc = "Heighten the subject's sense of touch. This can lead to increased arousal, but in public it might be frustrating if their clothes are too restrictive.",
        positive_slug = "+5 Arousal/turn, may cause stripping when administered",
        negative_slug = "-2 Happiness/turn in public",
        research_added = 20,
        base_side_effect_chance = 30,
        on_apply = skin_sensitivity_on_apply,
        on_turn = skin_sensitivity_on_turn,
        requires = [clinical_testing],
        tier = 1,
        research_needed = 800,
        clarity_cost = 1000,
        hidden_tag = "Slut",
        mental_aspect = 3, physical_aspect = 1, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 2)
