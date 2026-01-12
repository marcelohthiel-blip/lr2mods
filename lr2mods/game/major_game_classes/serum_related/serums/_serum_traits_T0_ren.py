## SERUM TRAIT GUIDELINES ##
# These are some guidelines for how serum traits are priced out.
# Each tier of serum trait should provide 2*(tier+1) aspect points.
# Add 1 extra aspect point per point of attention.

# Serum trait functions. Each serum trait can have up to four key functions: on_apply, on_remove, on_turn, and on_day. These are run at various points throughout the game.

from __future__ import annotations
from renpy.color import Color
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait

list_of_traits: list[SerumTrait] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
## suggestion_drugs_functions ##
def suggestion_drugs_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.add_suggest_effect(10, add_to_log = add_to_log)

def suggestion_drugs_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.remove_suggest_effect(10)

## high_concentration_drug_functions ##
def high_con_drugs_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.add_suggest_effect(25, add_to_log = add_to_log)

def high_con_drugs_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.remove_suggest_effect(25)

def high_con_drugs_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-2, add_to_log = add_to_log)

## sedatives_trait_functions ##
def sedatives_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_obedience(10, sedatives_trait.mastery_range(120, 140), add_to_log = add_to_log)
    serum.effects_dict["sedatives_trait"] = change_amount
    person.change_cha(-1, add_to_log = add_to_log)
    person.change_focus(-1, add_to_log = add_to_log)
    person.change_int(-1, add_to_log = add_to_log)

def sedatives_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("sedatives_trait", 10)
    person.change_obedience(-change_amount, add_to_log = add_to_log)
    person.change_cha(1, add_to_log = add_to_log)
    person.change_focus(1, add_to_log = add_to_log)
    person.change_int(1, add_to_log = add_to_log)

## caffeine_trait functions##
def caffeine_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    serum.effects_dict["caffeine_max_energy"] = person.change_max_energy(20, add_to_log = add_to_log)
    serum.effects_dict["caffeine_trait"] = person.change_obedience(-15, add_to_log = add_to_log)
    person.change_energy(20, add_to_log = add_to_log)

def caffeine_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-serum.effects_dict.get("caffeine_max_energy", 20), add_to_log = add_to_log)
    person.change_obedience(-serum.effects_dict.get("caffeine_trait", -15), add_to_log = add_to_log)

def birth_control_suppression_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.bc_penalty += 40
    person.change_baby_desire(1)
    if add_to_log:
        mc.log_event(f"{person.display_name}: Birth control effectiveness reduced by 40%", "float_text_grey")

def birth_control_suppression_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.bc_penalty -= 40

def simple_aphrodisiac_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = 10
    change_amount = person.change_slut(change_amount, simple_aphrodisiac.mastery_range(20, 50), add_to_log = add_to_log)
    serum.effects_dict["simple_aphrodisiac_amount"] = change_amount
    person.change_max_energy(-20, add_to_log = add_to_log)

def simple_aphrodisiac_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("simple_aphrodisiac_amount", 10)
    person.change_slut(-change_amount, add_to_log = add_to_log)
    person.change_max_energy(20, add_to_log = add_to_log)

def foreplay_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Foreplay", 2, add_to_log = add_to_log)

def foreplay_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Foreplay", -2, add_to_log = add_to_log)

## Body modification functions ##
def hair_lighten_dye_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    change_per_turn = 0.3 #At 1 it changes in a single turn, at 0 it never changes at all. At 0.5 it gets 50% closer each turn.
    person.lighten_hair_colour(change_per_turn)

def hair_darken_dye_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    change_per_turn = 0.3 #At 1 it changes in a single turn, at 0 it never changes at all. At 0.5 it gets 50% closer each turn.
    person.darken_hair_colour(change_per_turn)

def essential_oil_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_happiness(5, add_to_log = add_to_log)
    serum.effects_dict["essential_oil_amount"] = change_amount

def essential_oil_function_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("essential_oil_amount", 5)
    person.change_happiness(-change_amount, add_to_log = add_to_log)

# Tier 0 traits produce almost no effect on the person taking them, or produce an effect with a significant downside. They are available for research from the start of the game.
def init_T0_traits():
    global primitive_serum_prod
    primitive_serum_prod = SerumTrait(name = "Primitive Serum Production",
        desc = "The fundamental serum creation technique. The special carrier molecule can deliver two serum traits with pinpoint accuracy.",
        positive_slug = "+2 Trait Slot\n+3 Turn Duration",
        negative_slug = "",
        research_added = 50,
        slots_added = 2,
        production_added = 40,
        duration_added = 3,
        base_side_effect_chance = 8,
        clarity_added = 25,
        start_researched = True,
        research_needed = 75,
        exclude_tags = "Production",
        clarity_cost = 50,
        hidden_tag = "Production",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 0)
    global high_capacity_design
    high_capacity_design = SerumTrait(name = "High Capacity Design",
        desc = "Removing the standard stabilizing agents allow an additional serum trait to be added to the design. This change shortens the duration of the serum and is almost certain to introduce unpleasant side effects.",
        positive_slug = "+1 Trait Slot",
        negative_slug = "-1 Turn Duration",
        research_added = 75,
        slots_added = 2,
        duration_added = -1,
        base_side_effect_chance = 200,
        requires = primitive_serum_prod,
        research_needed = 150,
        clarity_cost = 20,
        hidden_tag = "Capacity",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 0)
    global basic_med_app
    basic_med_app = SerumTrait(name = "Basic Medical Application",
        desc = "A spread of minor medical benefits ensures this will always have value for off label treatments. The required research may suggest other effects that can be included in a serum.",
        positive_slug = "",
        negative_slug = "",
        research_added = 50,
        base_side_effect_chance = 5,
        research_needed = 200,
        clarity_cost = 25,
        hidden_tag = "Medical",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 0)
    global suggestion_drugs_trait
    suggestion_drugs_trait = SerumTrait(name = "Suggestion Drugs",
        desc = "Carefully selected mind–altering agents amplify the pre-existing effects of the serum, making the recipient more vulnerable to behavioural changes.",
        positive_slug = "+10 Suggestibility",
        negative_slug = "",
        research_added = 50,
        on_apply = suggestion_drugs_on_apply,
        on_remove = suggestion_drugs_on_remove,
        base_side_effect_chance = 10,
        research_needed = 100,
        exclude_tags = "Suggest",
        clarity_cost = 15,
        hidden_tag = "Suggest",
        mental_aspect = 2, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 1)
    global high_con_drugs
    high_con_drugs = SerumTrait(name = "High Concentration Drugs",
        desc = "By increasing the dose of mind–altering agents a larger change to suggestibility can be achieved. The increased dosage has a tendency to leave the recipient depressed.",
        positive_slug = "+25 Suggestibility",
        negative_slug = "-2 Happiness/Turn",
        research_added = 50,
        base_side_effect_chance = 15,
        on_apply = high_con_drugs_on_apply,
        on_remove = high_con_drugs_on_remove,
        on_turn = high_con_drugs_on_turn,
        requires = [basic_med_app, suggestion_drugs_trait],
        research_needed = 150,
        exclude_tags = "Suggest",
        clarity_cost = 40,
        hidden_tag = "Suggest",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global sedatives_trait
    sedatives_trait = SerumTrait(name = "Low Concentration Sedatives",
        desc = "A low dose of slow release sedatives makes the recipient more obedient, but have a negative effect on productivity.",
        positive_slug = "+10 Obedience\nMax:(120-140)",
        negative_slug = "-1 To All Stats",
        research_added = 50,
        base_side_effect_chance = 10,
        on_apply = sedatives_trait_on_apply,
        on_remove = sedatives_trait_on_remove,
        requires = basic_med_app,
        research_needed = 100,
        clarity_cost = 20,
        hidden_tag = "Obedience",
        mental_aspect = 2, physical_aspect = 1, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global caffeine_trait
    caffeine_trait = SerumTrait(name = "Caffeine Infusion",
        desc = "Adding simple, well understood caffeine to the serum increases the energy levels of the recipient. Unfortunately, the stimulating effect tends to reduce obedience for the duration.",
        positive_slug = "+20 Max Energy",
        negative_slug = "-15 Obedience",
        research_added = 50,
        base_side_effect_chance = 20,
        on_apply = caffeine_trait_on_apply,
        on_remove = caffeine_trait_on_remove,
        research_needed = 150,
        mental_aspect = 1, physical_aspect = 1, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0,
        exclude_tags = "Energy",
        hidden_tag = "Energy",
        clarity_cost = 10)
    global birth_control_suppression
    birth_control_suppression = SerumTrait(name = "Birth Control Suppression",
        desc = "Designed to interfere with the most common forms of oral birth control, reducing their effectiveness.",
        positive_slug = "-40% BC Effectiveness",
        negative_slug = "",
        research_added = 50,
        base_side_effect_chance = 30,
        on_apply = birth_control_suppression_on_apply,
        on_remove = birth_control_suppression_on_remove,
        research_needed = 100,
        clarity_cost = 30,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 1, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global simple_aphrodisiac
    simple_aphrodisiac = SerumTrait(name = "Inhibition Suppression",
        desc = "Directly delivers alcoholic metabolites directly to the blood stream causing notably reduced inhibitions. Side effects are common, but always include drowsiness.",
        positive_slug = "+10 Sluttiness\nMax (20 - 50)",
        negative_slug = "-20 Energy",
        research_added = 50,
        base_side_effect_chance = 50,
        on_apply = simple_aphrodisiac_on_apply,
        on_remove = simple_aphrodisiac_on_remove,
        research_needed = 75,
        clarity_cost = 25,
        hidden_tag = "Slut",
        mental_aspect = 1, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global foreplay_enhancer
    foreplay_enhancer = SerumTrait(name = "Tactile Stimulator",
        desc = "Tunes the subject's nerves, especially those in the extremities, to higher levels of precision. Increases a girl's Foreplay skill for the duration.",
        positive_slug = "+2 Foreplay Skill",
        negative_slug = "",
        research_added = 50,
        base_side_effect_chance = 20,
        on_apply = foreplay_enhancer_on_apply,
        on_remove = foreplay_enhancer_on_remove,
        requires = [basic_med_app],
        tier = 0,
        research_needed = 100,
        clarity_cost = 50,
        hidden_tag = "Sex_Skill",
        mental_aspect = 0, physical_aspect = 1, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global hair_lighten_dye
    hair_lighten_dye = SerumTrait(name = "Synthetic Hair Bleach",
        desc = "Slow release chemicals lighten the hair colour of the subject. Application over several hours or days is needed for the best results.",
        positive_slug = "Lightens the Subject's Hair Colour.",
        negative_slug = "",
        research_added = 40,
        base_side_effect_chance = 40,
        on_turn = hair_lighten_dye_on_turn,
        tier = 0,
        research_needed = 75,
        exclude_tags = "Dye",
        clarity_cost = 20,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0)
    global hair_darken_dye
    hair_darken_dye = SerumTrait(name = "Synthetic Hair Darkening Agent",
        desc = "Slow release chemicals darken the hair colour of the subject. Application over several hours or days is needed for the best results.",
        positive_slug = "Darkens the Subject's Hair Colour.",
        negative_slug = "",
        research_added = 40,
        base_side_effect_chance = 40,
        on_turn = hair_darken_dye_on_turn,
        tier = 0,
        research_needed = 75,
        exclude_tags = "Dye",
        clarity_cost = 20,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0)
    global essential_oil_trait
    essential_oil_trait = SerumTrait(name = "Essential Oils",
        desc = "Pleasant smell and texture adds greatly to the value of the serum. High chance of negative side effect.",
        positive_slug = "+5 Happiness",
        negative_slug = "",
        research_added = 20,
        base_side_effect_chance = 150,
        on_apply = essential_oil_function_on_apply,
        on_remove = essential_oil_function_on_remove,
        tier = 0,
        start_researched = True,
        research_needed = 1500,
        clarity_cost = 1000,
        hidden_tag = "Medical",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 3, medical_aspect = 2, flaws_aspect = 0, attention = 0)

    global list_of_traits
    list_of_traits.extend((
        primitive_serum_prod,
        high_capacity_design,
        basic_med_app,
        suggestion_drugs_trait,
        high_con_drugs,
        sedatives_trait,
        caffeine_trait,
        simple_aphrodisiac,
        foreplay_enhancer,
        hair_lighten_dye,
        hair_darken_dye,
    ))
