## SERUM TRAIT GUIDELINES ##
# These are some guidelines for how serum traits are priced out.
# Each tier of serum trait should provide 2*(tier+1) aspect points.
# Add 1 extra aspect point per point of attention.

#Serum trait functions. Each serum trait can have up to four key functions: on_apply, on_remove, on_turn, and on_day. These are run at various points throughout the game.

from __future__ import annotations
import renpy
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import basic_med_app
from game.major_game_classes.serum_related.serums._serum_traits_T1_ren import improved_serum_prod, clinical_testing, improved_duration_trait, weight_loss, weight_gain, off_label_drugs, refined_caffeine_trait, aphrodisiac, mood_enhancer, fertility_enhancement_trait, fertility_suppression_trait

list_of_traits: list[SerumTrait] = []
day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

## slutty_caffeine_trait functions ##
def slutty_caffeine_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    serum.effects_dict["slutty_max_energy"] = person.change_max_energy(20, add_to_log = add_to_log)
    serum.effects_dict["slutty_caffeine"] = person.change_slut(15, add_to_log = add_to_log)
    person.change_energy(20, add_to_log = add_to_log)

def slutty_caffeine_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-serum.effects_dict.get("slutty_max_energy", 20), add_to_log = add_to_log)
    person.change_slut(-serum.effects_dict.get("slutty_caffeine", 15), add_to_log = add_to_log)

## blood_brain_pen_functions ##
def blood_brain_pen_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.add_suggest_effect(50, add_to_log = add_to_log)

def blood_brain_pen_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.remove_suggest_effect(50)

## breast_enhancement_functions ##
def breast_enhancement_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if renpy.random.randint(0, 100) < 25:
        person.increase_tit_size()

def breast_reduction_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if renpy.random.randint(0, 100) < 25:
        person.decrease_tit_size()

## focus_enhancement_functions ##
def focus_enhancement_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_focus(2, add_to_log = add_to_log)

def focus_enhancement_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_focus(-2, add_to_log = add_to_log)

## int_enhancement_functions ##
def int_enhancement_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_int(2, add_to_log = add_to_log)

def int_enhancement_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_int(-2, add_to_log = add_to_log)

## cha_enhancement_functions ##
def cha_enhancement_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_cha(2, add_to_log = add_to_log)

def cha_enhancement_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_cha(-2, add_to_log = add_to_log)

## happiness_tick_functions ##
def happiness_tick_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(5, add_to_log = add_to_log)

def climax_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_max_arousal(-int(person.max_arousal * .2), add_to_log = add_to_log)
    serum.effects_dict["climax_enhancer_amount"] = change_amount
    if person.arousal_perc < 50:
        change_amount = int((person.max_arousal / 2.0) - person.arousal)
        person.change_arousal(change_amount, add_to_log = add_to_log)

def climax_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_arousal(-(serum.effects_dict.get("climax_enhancer_amount", -20)), add_to_log = add_to_log)

def climax_enhancer_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_arousal(5, add_to_log = add_to_log)
    person.change_happiness(-2, add_to_log = add_to_log)

def rolling_orgasm_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-10, add_to_log = add_to_log)

def rolling_orgasm_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(10, add_to_log = add_to_log)

def rolling_orgasm_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.run_orgasm(show_dialogue = False, add_to_log = add_to_log)
    person.change_happiness(5, add_to_log = add_to_log)

def vaginal_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Vaginal", 2, add_to_log = add_to_log)

def vaginal_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Vaginal", -2, add_to_log = add_to_log)

def anal_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Anal", 2, add_to_log = add_to_log)

def anal_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Anal", -2, add_to_log = add_to_log)

def pregnancy_accelerator_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.is_pregnant:
        return

    if person.event_triggers_dict.get("preg_announce_day", day) - 1 > day:
        person.event_triggers_dict["preg_announce_day"] = person.event_triggers_dict.get("preg_announce_day", day) - 1
    if person.event_triggers_dict.get("preg_tits_date", day) - 1 > day:
        if person.event_triggers_dict.get("preg_tits_date", day) - 1 > person.event_triggers_dict.get("preg_announce_day", 9999):
            person.event_triggers_dict["preg_tits_date"] = person.event_triggers_dict.get("preg_tits_date", day) - 1
    if person.event_triggers_dict.get("preg_transform_day", day) - 1 > day:
        if person.event_triggers_dict.get("preg_transform_day", day) - 1 > person.event_triggers_dict.get("preg_tits_date", 9999):
            person.event_triggers_dict["preg_transform_day"] = person.event_triggers_dict.get("preg_transform_day", day) - 1
    if person.event_triggers_dict.get("preg_finish_announce_day", day) - 1 > day:
        if person.event_triggers_dict.get("preg_finish_announce_day", day) - 1 > person.event_triggers_dict.get("preg_transform_day", 9999):
            person.event_triggers_dict["preg_finish_announce_day"] = person.event_triggers_dict.get("preg_finish_announce_day", day) - 1
    return

def pregnancy_decellerator_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.is_pregnant:
        return

    if person.event_triggers_dict.get("preg_announce_day", day) > day:
        person.event_triggers_dict["preg_announce_day"] = person.event_triggers_dict.get("preg_announce_day", day) + 1
    if person.event_triggers_dict.get("preg_tits_date", day) > day:
        person.event_triggers_dict["preg_tits_date"] = person.event_triggers_dict.get("preg_tits_date", day) + 1
    if person.event_triggers_dict.get("preg_transform_day", day) > day:
        person.event_triggers_dict["preg_transform_day"] = person.event_triggers_dict.get("preg_transform_day", day) + 1
    if person.event_triggers_dict.get("preg_finish_announce_day", day) > day:
        person.event_triggers_dict["preg_finish_announce_day"] = person.event_triggers_dict.get("preg_finish_announce_day", day) + 1

def height_increase_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if renpy.random.randint(0, 100) < 3: # 3% chance of breast size increase
        person.increase_tit_size()
    person.change_height(person.get_height_step(), 10)

def height_increase_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_height(person.get_height_step(), 100)
    if renpy.random.randint(0, 100) < 10:
        person.increase_tit_size()

def height_decrease_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if renpy.random.randint(0, 100) < 3: # 3% chance of breast size decrease
        person.decrease_tit_size()
    person.change_height(-person.get_height_step(), 10)

def height_decrease_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if renpy.random.randint(0, 100) < 10:
        person.decrease_tit_size()
    person.change_height(-person.get_height_step(), 100)

def skin_improvement_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(5, add_to_log = add_to_log)

# Tier 2 traits can produce moderate effects at a cost or minor effects without side effects.

def init_T2_traits():
    global advanced_serum_prod
    advanced_serum_prod = SerumTrait(name = "Advanced Serum Production",
        desc = "Advanced improvements to the basic serum design. Adds five serum trait slots, but requires even more production points.",
        positive_slug = "+5 Trait Slots\n+3 Turn Duration",
        negative_slug = "",
        research_added = 200,
        slots_added = 5,
        production_added = 80,
        duration_added = 3,
        base_side_effect_chance = 40,
        clarity_added = 750,
        requires = [improved_serum_prod, basic_med_app],
        tier = 2,
        research_needed = 800,
        exclude_tags = "Production",
        clarity_cost = 1500,
        hidden_tag = "Production",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 1)
    global blood_brain_pen
    blood_brain_pen = SerumTrait(name = "Blood Brain Penetration",
        desc = "A carefully designed delivery unit can bypass the blood-brain barrier. This will provide a large increase to the Suggestibility of the recipient.",
        positive_slug = "+50 Suggestibility",
        negative_slug = "",
        research_added = 25,
        base_side_effect_chance = 40,
        on_apply = blood_brain_pen_on_apply,
        on_remove = blood_brain_pen_on_remove,
        requires = [off_label_drugs, clinical_testing],
        tier = 2,
        research_needed = 500,
        exclude_tags = "Suggest",
        clarity_cost = 800,
        hidden_tag = "Suggest",
        mental_aspect = 6, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 1, flaws_aspect = 0, attention = 3)
    global low_volatility_reagents
    low_volatility_reagents = SerumTrait(name = "Low Volatility Reagents",
        desc = "Carefully sourced and stored reagents will greatly prolong the effects of a serum.",
        positive_slug = "+5 Turn Duration",
        negative_slug = "",
        research_added = 150,
        duration_added = 5,
        base_side_effect_chance = 15,
        requires = improved_duration_trait,
        tier = 2,
        research_needed = 600,
        clarity_cost = 1000,
        hidden_tag = "Duration",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 7, flaws_aspect = 0, attention = 1)
    global breast_enhancement
    breast_enhancement = SerumTrait(name = "Breast Enhancement",
        desc = "Grows breasts overnight. Has a 25% chance of increasing a girl's breast size by one step with each time unit.",
        positive_slug = "25% Chance/Turn Breast Growth",
        negative_slug = "",
        research_added = 125,
        base_side_effect_chance = 20,
        on_turn = breast_enhancement_on_turn,
        requires = [weight_gain],
        tier = 2,
        research_needed = 500,
        clarity_cost = 1000,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 6, sexual_aspect = 2, medical_aspect = 1, flaws_aspect = 0, attention = 3)
    global breast_reduction
    breast_reduction = SerumTrait(name = "Breast Reduction",
        desc = "Shrinks breasts overnight. Has a 25% chance of decreasing a girl's breast size by one step with each time unit.",
        positive_slug = "25% Chance/Turn Breast Reduction",
        negative_slug = "",
        research_added = 125,
        base_side_effect_chance = 20,
        on_turn = breast_reduction_on_turn,
        requires = [weight_loss],
        tier = 2,
        research_needed = 500,
        clarity_cost = 750,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 6, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global focus_enhancement
    focus_enhancement = SerumTrait(name = "Medical Amphetamines",
        desc = "The inclusion of low doses of amphetamines help the user focus intently for long periods of time.",
        positive_slug = "+2 Focus",
        negative_slug = "",
        research_added = 150,
        base_side_effect_chance = 30,
        on_apply = focus_enhancement_on_apply,
        on_remove = focus_enhancement_on_remove,
        requires = [basic_med_app, clinical_testing],
        tier = 2,
        research_needed = 800,
        clarity_cost = 800,
        hidden_tag = "Skill",
        mental_aspect = 4, physical_aspect = 1, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 2)
    global int_enhancement
    int_enhancement = SerumTrait(name = "Quick Release Nootropics",
        desc = "Nootropics enhance cognition and learning. These fast acting nootropics produce results almost instantly, but for a limited period of time.",
        positive_slug = "+2 Intelligence",
        negative_slug = "",
        research_added = 150,
        base_side_effect_chance = 30,
        on_apply = int_enhancement_on_apply,
        on_remove = int_enhancement_on_remove,
        requires = [basic_med_app, clinical_testing],
        tier = 2,
        research_needed = 800,
        clarity_cost = 800,
        hidden_tag = "Skill",
        mental_aspect = 5, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 2)
    global cha_enhancement
    cha_enhancement = SerumTrait(name = "Stress Inhibitors",
        desc = "By reducing the users natural stress response to social interactions they are able to express themselves more freely and effectively. Takes effect immediately, but lasts only for a limited time",
        positive_slug = "+2 Charisma",
        negative_slug = "",
        research_added = 150,
        base_side_effect_chance = 30,
        on_apply = cha_enhancement_on_apply,
        on_remove = cha_enhancement_on_remove,
        requires = [basic_med_app, clinical_testing],
        tier = 2,
        research_needed = 800,
        clarity_cost = 800,
        hidden_tag = "Skill",
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 3, flaws_aspect = 0, attention = 2)
    global happiness_tick
    happiness_tick = SerumTrait(name = "Slow Release Dopamine",
        desc = "By slowly flooding the users dopamine receptors they can be put into a long-lasting sense of optimism",
        positive_slug = "+5 Happiness/Turn",
        negative_slug = "",
        research_added = 100,
        base_side_effect_chance = 20,
        on_turn = happiness_tick_on_turn,
        requires = [basic_med_app, clinical_testing],
        tier = 2,
        research_needed = 800,
        clarity_cost = 1000,
        hidden_tag = "Medical",
        mental_aspect = 6, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 2)
    global slutty_caffeine_trait
    slutty_caffeine_trait = SerumTrait(name = "Libido Stimulants",
        desc = "Careful engineering allows for the traditional side effects of stimulants to be redirected to the parasympathetic nervous system, causing an immediate spike in arousal as well as general energy levels.",
        positive_slug = " +20 Max Energy\n+15 Sluttiness",
        negative_slug = "",
        research_added = 150,
        base_side_effect_chance = 60,
        on_apply = slutty_caffeine_trait_on_apply,
        on_remove = slutty_caffeine_trait_on_remove,
        requires = [refined_caffeine_trait, aphrodisiac],
        tier = 2,
        research_needed = 800,
        hidden_tag = ["Energy", "Slut"],
        mental_aspect = 2, physical_aspect = 2, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 2,
        exclude_tags = "Energy",
        clarity_cost = 1200)
    global pregnancy_accelerator_trait
    pregnancy_accelerator_trait = SerumTrait(name = "Pregnancy Acceleration Hormones",
        desc = "Encourages and supports the ongoing development of a fetus, increasing the effective speed at which a pregnancy develops.",
        positive_slug = "+1 Pregnancy Progress/Day",
        negative_slug = "",
        research_added = 250,
        base_side_effect_chance = 60,
        on_day = pregnancy_accelerator_on_day,
        requires = [fertility_enhancement_trait],
        tier = 2,
        research_needed = 800,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 6, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 3,
        exclude_tags = "Pregnancy",
        clarity_cost = 1200)
    global pregnancy_decelerator_trait
    pregnancy_decelerator_trait = SerumTrait(name = "Pregnancy Deceleration Hormones",
        desc = "Slows the ongoing development of a fetus, increasing the total amount of time needed to bring a pregnancy to term. If properly applied a pregnancy could be maintained indefinitely.",
        positive_slug = "-1 Pregnancy Progress/Day",
        negative_slug = "",
        research_added = 250,
        base_side_effect_chance = 60,
        on_day = pregnancy_decellerator_on_day,
        requires = [fertility_suppression_trait],
        tier = 2,
        research_needed = 800,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 6, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 3,
        exclude_tags = "Pregnancy",
        clarity_cost = 800)
    global vaginal_enhancer
    vaginal_enhancer = SerumTrait(name = "Natural Lubrication Stimulation",
        desc = "Kicks the subject's natural lubrication production into overdrive. Improved lubrication allows for more vigorous activities without discomfort.",
        positive_slug = "+2 Vaginal Skill",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 60,
        on_apply = vaginal_enhancer_on_apply,
        on_remove = vaginal_enhancer_on_remove,
        requires = [basic_med_app],
        tier = 2,
        research_needed = 700,
        clarity_cost = 1000,
        hidden_tag = "Sex_Skill",
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global anal_enhancer
    anal_enhancer = SerumTrait(name = "Sphincter Elasticity Promoter",
        desc = "Triggers a release of chemicals in the subject that increase muscle elasticity dramatically.",
        positive_slug = "+2 Anal Skill",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 60,
        on_apply = anal_enhancer_on_apply,
        on_remove = anal_enhancer_on_remove,
        requires = [basic_med_app],
        tier = 2,
        research_needed = 700,
        clarity_cost = 1000,
        hidden_tag = "Sex_Skill",
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global climax_enhancer
    climax_enhancer = SerumTrait(name = "Pleasure Center Stimulator",
        desc = "Changes the baseline of pleasure chemicals in the subject's brain. This has the effect of making it much easier for physical stimulation to trigger an orgasm in the subject. Comes with a large risk of side effects, and disturbs the subject's natural sense of enjoyment.",
        positive_slug = "+5 Arousal/Turn\n-20% Max Arousal\nArousal to 50% on apply",
        negative_slug = "-2 Happiness/Turn",
        research_added = 350,
        base_side_effect_chance = 100,
        on_apply = climax_enhancer_on_apply,
        on_remove = climax_enhancer_on_remove,
        on_turn = climax_enhancer_on_turn,
        requires = [mood_enhancer, aphrodisiac],
        tier = 2,
        research_needed = 1000,
        clarity_cost = 1600,
        hidden_tag = "Slut",
        mental_aspect = 2, physical_aspect = 0, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global rolling_orgasm
    rolling_orgasm = SerumTrait(name = "Climax Cycler",
        desc = "Linking the pleasure centre of the brain to the subject's natural circadian rhythm causes periodic, low grade orgasms spaced several hours apart. In addition to being pleasant and slightly tiring, this can trigger other orgasm related effects if they exist.",
        positive_slug = "+5 Happiness/Turn\n1 Forced Orgasm/Turn",
        negative_slug = "-10 Max Energy",
        research_added = 400,
        base_side_effect_chance = 50,
        on_apply = rolling_orgasm_on_apply,
        on_remove = rolling_orgasm_on_remove,
        on_turn = rolling_orgasm_on_turn,
        requires = [climax_enhancer],
        tier = 2,
        research_needed = 1000,
        clarity_cost = 2000,
        hidden_tag = "Slut",
        mental_aspect = 0, physical_aspect = 2, sexual_aspect = 7, medical_aspect = 0, flaws_aspect = 0, attention = 3)
    global height_increase
    height_increase = SerumTrait(name = "Human Growth Rebooter",
        desc = "Provides the required hormonal signals to promote growth that would otherwise stop after puberty, allowing the subject to grow taller. Causes a height increase of roughly 1 inch per day. There is a minor chance that the subject's breasts will grow along with her frame.",
        positive_slug = '+{height=2.54} Height/On Remove\n+10% Chance/Turn',
        negative_slug = "10% Chance/On Remove Breast Enhancement\n3% Chance/Turn",
        research_added = 200,
        base_side_effect_chance = 80,
        on_turn = height_increase_on_turn,
        on_remove = height_increase_on_remove,
        requires = [weight_gain],
        tier = 2,
        research_needed = 600,
        exclude_tags = ["Height Modification"],
        clarity_cost = 1400,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 7, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 3)
    global height_decrease
    height_decrease = SerumTrait(name = "Human Growth Rewinder",
        desc = "Carefully engineered hormones produce an inverted growth effect, effectively causing the subject to grow shorter. The subject's height will decrease by roughly 1 inch per day. There is a minor chance that the subject's breasts will be shrink along with her frame",
        positive_slug = '-{height=2.54} Height/On Remove\n+10% Chance/Turn',
        negative_slug = "10% Chance/On Remove Breast Reduction\n+3% Chance/Turn",
        research_added = 200,
        base_side_effect_chance = 80,
        on_turn = height_decrease_on_turn,
        on_remove = height_decrease_on_remove,
        requires = [weight_loss],
        tier = 2,
        research_needed = 600,
        exclude_tags = ["Height Modification"],
        clarity_cost = 1400,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 7, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 3)
    global skin_improvement_trait
    skin_improvement_trait = SerumTrait(name = "Skin Improvement",
        desc = "Normal medical serum that improves skin condition (prevent acne / reduces pigment spots).",
        positive_slug = "Permanent +5 Happiness",
        negative_slug = "",
        research_added = 50,
        base_side_effect_chance = 5,
        on_apply = skin_improvement_trait_on_apply,
        requires = [clinical_testing],
        tier = 2,
        start_researched = False,
        research_needed = 250,
        clarity_cost = 250,
        hidden_tag = "Physical",
        mental_aspect = 1, physical_aspect = 4, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 0)

    global list_of_traits
    list_of_traits.extend((
        advanced_serum_prod,
        blood_brain_pen,
        breast_enhancement,
        breast_reduction,
        focus_enhancement,
        int_enhancement,
        cha_enhancement,
        low_volatility_reagents,
        happiness_tick,
        slutty_caffeine_trait,
        pregnancy_accelerator_trait,
        pregnancy_decelerator_trait,
        vaginal_enhancer,
        anal_enhancer,
        climax_enhancer,
        rolling_orgasm,
        height_increase,
        height_decrease,
        skin_improvement_trait,
    ))
