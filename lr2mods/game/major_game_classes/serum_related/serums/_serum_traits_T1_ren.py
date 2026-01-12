## SERUM TRAIT GUIDELINES ##
# These are some guidelines for how serum traits are priced out.
# Each tier of serum trait should provide 2*(tier+1) aspect points.
# Add 1 extra aspect point per point of attention.

# Serum trait functions. Each serum trait can have up to four key functions: on_apply, on_remove, on_turn, and on_day. These are run at various points throughout the game.

from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import basic_med_app, primitive_serum_prod, suggestion_drugs_trait, caffeine_trait, birth_control_suppression, high_con_drugs, simple_aphrodisiac

list_of_traits: list[SerumTrait] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def get_blue_serum():
    blue_serum = SerumDesign("Blue Serum")
    blue_serum.add_trait(primitive_serum_prod)
    blue_serum.add_trait(high_con_drugs)
    blue_serum.add_trait(simple_aphrodisiac)
    return blue_serum

def get_red_serum():
    red_serum = SerumDesign("Red Serum")
    red_serum.add_trait(improved_serum_prod)
    red_serum.add_trait(aphrodisiac)
    red_serum.add_trait(off_label_drugs)
    red_serum.add_trait(large_obedience_enhancer)
    return red_serum

def get_purple_serum():
    purple_serum = SerumDesign("Purple Serum")
    purple_serum.add_trait(improved_serum_prod)
    purple_serum.add_trait(off_label_drugs)
    purple_serum.add_trait(improved_duration_trait)
    purple_serum.add_trait(love_potion)
    return purple_serum

def unlock_blue_serum():
    blue_serum = get_blue_serum()
    mc.business.add_serum_design(blue_serum)
    blue_serum.unlocked = True
    blue_serum.researched = True

def unlock_red_serum():
    red_serum = get_red_serum()
    mc.business.add_serum_design(red_serum)
    red_serum.unlocked = True
    red_serum.researched = True

def unlock_purple_serum():
    purple_serum = get_purple_serum()
    mc.business.add_serum_design(purple_serum)
    purple_serum.unlocked = True
    purple_serum.researched = True


## obedience_enhancer_functions ##
def obedience_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_obedience(10, add_to_log = add_to_log)
    serum.effects_dict["obedience_enhancer"] = change_amount

def obedience_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("obedience_enhancer", 10)
    person.change_obedience(-change_amount, add_to_log = add_to_log)

def obedience_enhancer_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_obedience(1, max_amount = 150 ,add_to_log = add_to_log)

## large_obedience_enhancer_functions ##
def large_obedience_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_obedience(20, add_to_log = add_to_log)
    serum.effects_dict["large_obedience_enhancer"] = change_amount

def large_obedience_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("large_obedience_enhancer", 20)
    person.change_obedience(-change_amount, add_to_log = add_to_log)

def large_obedience_enhancer_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_slut(-1, add_to_log = add_to_log)

## aphrodisiac_functions ##
def aphrodisiac_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_slut(15, add_to_log = add_to_log)
    serum.effects_dict["aphrodisiac"] = change_amount

def aphrodisiac_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("aphrodisiac", 15)
    person.change_slut(-change_amount, add_to_log = add_to_log)

def aphrodisiac_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_obedience(-1, add_to_log = add_to_log)

def aphrodisiac_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_slut(1, 20, add_to_log = add_to_log)

## refined_caffeine_trait functions ##
def refined_caffeine_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    serum.effects_dict["refined_max_energy"] = person.change_max_energy(20, add_to_log = add_to_log)
    person.change_energy(20, add_to_log = add_to_log)

def refined_caffeine_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-serum.effects_dict.get("refined_max_energy", 20), add_to_log = add_to_log)

## love_potion_functions ##
def love_potion_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_love(20, add_to_log = add_to_log)
    serum.effects_dict["love_potion_change"] = change_amount

def love_potion_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("love_potion_change", 20)
    person.change_love(-change_amount, add_to_log = add_to_log)

## off_label_drugs_functions ##
def off_label_drugs_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.add_suggest_effect(30, add_to_log = add_to_log)

def off_label_drugs_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.remove_suggest_effect(30)

## mood_enhancer_functions ##
def mood_enhancer_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(10, add_to_log = add_to_log)
    person.change_obedience(-1, add_to_log = add_to_log)

## Pregnancy related serum trait functions ##
def fertility_enhancement_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.fertility_percent += 20
    person.change_baby_desire(1)
    if add_to_log:
        mc.log_event(f"{person.display_name}: +20 Fertility", "float_text_grey")

def fertility_enhancement_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.fertility_percent -= 20

def fertility_suppression_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.fertility_percent -= 20
    person.change_baby_desire(-1)
    if add_to_log:
        mc.log_event(f"{person.display_name}: -20 Fertility", "float_text_grey")

def fertility_suppression_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.fertility_percent += 20

def climax_limiter_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_arousal(40, add_to_log = add_to_log)

def climax_limiter_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_arousal(-40, add_to_log = add_to_log)

def oral_enhancer_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Oral", 2, add_to_log = add_to_log)

def oral_enhancer_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_sex_skill("Oral", -2, add_to_log = add_to_log)

def lactation_hormones_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.lactation_sources += 1
    person.change_baby_desire(1)
    if add_to_log:
        if person.lactation_sources == 1:
            mc.log_event(f"{person.display_name}: Started lactating", "float_text_grey")
        else:
            mc.log_event(f"{person.display_name}: Lactation increases", "float_text_grey")

def lactation_hormones_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.lactation_sources -= 1

def weight_gain_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-20, add_to_log = add_to_log)

def weight_gain_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(20, add_to_log = add_to_log)
    person.change_weight(amount = 0.4536, chance = 100)

def weight_gain_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_weight(amount = 0.4536, chance = 30)

def weight_loss_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-20, add_to_log = add_to_log)

def weight_loss_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(20, add_to_log = add_to_log)
    person.change_weight(amount = -0.4536, chance = 100)

def weight_loss_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_weight(amount = -0.4536, chance = 30)

def anti_biotics_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(2, add_to_log = add_to_log)

def antidote_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    # handled by Person.serum_trait property
    return

def antidote_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    # handled by Person.serum_trait property
    return

# Tier 1 traits produce minor effects, often at the cost of unpleasant mandatory side effects (lower happiness, obedience, stats)

def init_T1_traits():
    global improved_serum_prod
    improved_serum_prod = SerumTrait(name = "Improved Serum Production",
        desc = "General improvements to the basic serum creation formula. Allows for three serum traits to be delivered, but requires slightly more production to produce.",
        positive_slug = "+3 Trait Slots\n+3 Turn Duration",
        negative_slug = "",
        research_added = 50,
        slots_added = 3,
        production_added = 60,
        duration_added = 3,
        base_side_effect_chance = 25,
        clarity_added = 250,
        requires = primitive_serum_prod,
        tier = 1,
        research_needed = 200,
        exclude_tags = "Production",
        clarity_cost = 500,
        hidden_tag = "Production",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 0)
    global obedience_enhancer
    obedience_enhancer = SerumTrait(name = "Obedience Enhancer",
        desc = "A blend of off the shelf pharmaceuticals will make the recipient more receptive to direct orders.",
        positive_slug = "+10 Obedience\n+1 Obedience Per turn (Max 150)",
        negative_slug = "",
        research_added = 75,
        base_side_effect_chance = 15,
        on_apply = obedience_enhancer_on_apply,
        on_remove = obedience_enhancer_on_remove,
        on_turn = obedience_enhancer_on_turn,
        requires = [basic_med_app],
        tier = 1,
        research_needed = 300,
        clarity_cost = 200,
        hidden_tag = "Obedience",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global large_obedience_enhancer
    large_obedience_enhancer = SerumTrait(name = "Experimental Obedience Treatment",
        desc = "The combination of several only recently released compounds should produce a larger increase in obedience. Unfortunately the effect leaves the recipient rather stuck up and stuffy.",
        positive_slug = "+20 Obedience",
        negative_slug = "-1 Sluttiness/Turn",
        research_added = 75,
        base_side_effect_chance = 20,
        on_apply = large_obedience_enhancer_on_apply,
        on_remove = large_obedience_enhancer_on_remove,
        on_turn = large_obedience_enhancer_on_turn,
        requires = obedience_enhancer,
        tier = 1,
        research_needed = 350,
        clarity_cost = 400,
        hidden_tag = "Obedience",
        mental_aspect = 5, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global improved_duration_trait
    improved_duration_trait = SerumTrait(name = "Improved Reagent Purification",
        desc = "By carefully purifying the starting materials you can extend the length of time a serum remains active.",
        positive_slug = "+2 Turn Duration",
        negative_slug = "",
        research_added = 75,
        duration_added = 2,
        base_side_effect_chance = 10,
        requires = basic_med_app,
        tier = 1,
        research_needed = 350,
        clarity_cost = 300,
        hidden_tag = "Duration",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 0)
    global aphrodisiac
    aphrodisiac = SerumTrait(name = "Distilled Aphrodisiac",
        desc = "Careful distillation can concentrate the active ingredient from common aphrodisiacs, producing a sudden spike in sluttiness when consumed. The sexual frustration linked to this effect tends to make the recipient less obedient over time as well.",
        positive_slug = "+10 Sluttiness\n+1 Sluttiness per Turn (Max 20)",
        negative_slug = "-1 Obedience/Day",
        research_added = 60,
        base_side_effect_chance = 20,
        on_apply = aphrodisiac_on_apply,
        on_remove = aphrodisiac_on_remove,
        on_day = aphrodisiac_on_day,
        on_turn = aphrodisiac_on_turn,
        requires = basic_med_app,
        tier = 1,
        research_needed = 250,
        clarity_cost = 300,
        hidden_tag = "Slut",
        mental_aspect = 2, physical_aspect = 0, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global love_potion
    love_potion = SerumTrait(name = "Love Potion",
        desc = "A carefully balanced combination of chemicals can replicate the brain's response to loved ones. Produces an immediate but temporary feeling of love. This trait is particularly prone to introducing side effects.",
        positive_slug = "+20 Love",
        negative_slug = "",
        research_added = 75,
        base_side_effect_chance = 75,
        on_apply = love_potion_on_apply,
        on_remove = love_potion_on_remove,
        requires = [aphrodisiac, basic_med_app],
        tier = 1,
        research_needed = 250,
        clarity_cost = 500,
        hidden_tag = "Love",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global off_label_drugs
    off_label_drugs = SerumTrait(name = "Off Label Pharmaceuticals",
        desc = "Several existing drugs can be repurposed to increase the mental pliability of the recipient.",
        positive_slug = "+30 Suggestibility",
        negative_slug = "",
        research_added = 80,
        base_side_effect_chance = 30,
        on_apply = off_label_drugs_on_apply,
        on_remove = off_label_drugs_on_remove,
        requires = suggestion_drugs_trait,
        tier = 1,
        research_needed = 300,
        exclude_tags = "Suggest",
        clarity_cost = 250,
        hidden_tag = "Suggest",
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 1, flaws_aspect = 0, attention = 2)
    global clinical_testing
    clinical_testing = SerumTrait(name = "Clinical Testing Procedures",
        desc = "A set of careful tests rather than any single ingredient or process. Serums may be put through formal clinical testing, significantly boosting their value to the general public. This also significantly raises the research cost of each serum design.",
        positive_slug = "Reduces attention of serum design by 1",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 0,
        requires = [basic_med_app, improved_serum_prod],
        tier = 1,
        research_needed = 400,
        clarity_cost = 500,
        hidden_tag = "Medical",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 0)
    global mood_enhancer
    mood_enhancer = SerumTrait(name = "Mood Enhancer",
        desc = "Standard antidepressants provide a general improvement in mood. The most common side effect is a lack of respect for authority figures, brought on by the chemical endorphin rush.",
        positive_slug = "+10 Happiness/Turn",
        negative_slug = "-1 Obedience/Turn",
        research_added = 75,
        base_side_effect_chance = 15,
        on_turn = mood_enhancer_on_turn,
        requires = basic_med_app,
        tier = 1,
        research_needed = 300,
        clarity_cost = 300,
        hidden_tag = "Medical",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 0, flaws_aspect = 0, attention = 0)
    global refined_caffeine_trait
    refined_caffeine_trait = SerumTrait(name = "Refined Stimulants",
        desc = "A more carefully refined stimulant produces the same boost to baseline energy levels as ordinary caffeine, but with none of the unpleasant side effects.",
        positive_slug = "+20 Max Energy",
        negative_slug = "",
        research_added = 50,
        base_side_effect_chance = 25,
        on_apply = refined_caffeine_trait_on_apply,
        on_remove = refined_caffeine_trait_on_remove,
        requires = [caffeine_trait],
        tier = 1,
        research_needed = 300,
        mental_aspect = 2, physical_aspect = 2, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0,
        exclude_tags = "Energy",
        hidden_tag = "Energy",
        clarity_cost = 250)
    global fertility_enhancement_trait
    fertility_enhancement_trait = SerumTrait(name = "Fertility Enhancement",
        desc = "Targets and enhances a woman's natural reproductive cycle, increasing the chance that she may become pregnant. Birth control will still prevent most pregnancies.",
        positive_slug = "+20% Fertility",
        negative_slug = "",
        research_added = 100,
        base_side_effect_chance = 40,
        on_apply = fertility_enhancement_on_apply,
        on_remove = fertility_enhancement_on_remove,
        requires = [birth_control_suppression, basic_med_app],
        tier = 1,
        research_needed = 250,
        clarity_cost = 500,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 1, sexual_aspect = 1, medical_aspect = 3, flaws_aspect = 0, attention = 1)
    global fertility_suppression_trait
    fertility_suppression_trait = SerumTrait(name = "Fertility Suppression",
        desc = "Targets and dampens a woman's natural reproductive cycle, decreasing the chance that she may become pregnant.",
        positive_slug = "-20% Fertility",
        negative_slug = "",
        research_added = 100,
        base_side_effect_chance = 40,
        on_apply = fertility_suppression_on_apply,
        on_remove = fertility_suppression_on_remove,
        requires = [birth_control_suppression, basic_med_app],
        tier = 1,
        research_needed = 250,
        clarity_cost = 200,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 1, sexual_aspect = 1, medical_aspect = 2, flaws_aspect = 0, attention = 0)
    global lactation_hormones
    lactation_hormones = SerumTrait(name = "Lactation Promotion Hormones",
        desc = "Contains massive quantities of hormones normally found naturally in the body during late stage pregnancy. Triggers immediate breast lactation",
        positive_slug = "Encourages Lactation",
        negative_slug = "",
        research_added = 150,
        base_side_effect_chance = 20,
        on_apply = lactation_hormones_on_apply,
        on_remove = lactation_hormones_on_remove,
        requires = [fertility_enhancement_trait],
        tier = 1,
        research_needed = 600,
        clarity_cost = 750,
        hidden_tag = "Physical",
        mental_aspect = 0, physical_aspect = 3, sexual_aspect = 2, medical_aspect = 1, flaws_aspect = 0, attention = 2)
    global oral_enhancer
    oral_enhancer = SerumTrait(name = "Gag Suppressant",
        desc = "Targets and suppresses the natural gag reflex of the subject. This has little practical benefit, other than making it significantly easier for the subject to perform oral sex.",
        positive_slug = "+2 Oral Skill",
        negative_slug = "",
        research_added = 150,
        base_side_effect_chance = 50,
        on_apply = oral_enhancer_on_apply,
        on_remove = oral_enhancer_on_remove,
        requires = [basic_med_app],
        tier = 1,
        research_needed = 300,
        clarity_cost = 750,
        hidden_tag = "Sex_Skill",
        mental_aspect = 0, physical_aspect = 1, sexual_aspect = 3, medical_aspect = 1, flaws_aspect = 0, attention = 1)
    global climax_limiter
    climax_limiter = SerumTrait(name = "Pleasure Center Depressant",
        desc = "Makes it much harder for a subject to orgasm, while still allowing them to feel the full effects of being highly aroused. Some subjects may take drastic steps to achieve orgasm.",
        positive_slug = "+40 Max Arousal",
        negative_slug = "",
        research_added = 100,
        base_side_effect_chance = 35,
        on_apply = climax_limiter_on_apply,
        on_remove = climax_limiter_on_remove,
        requires = [basic_med_app],
        tier = 1,
        research_needed = 200,
        clarity_cost = 500,
        hidden_tag = "Slut",
        mental_aspect = 0, physical_aspect = 1, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global weight_gain
    weight_gain = SerumTrait(name = "Weight Gain Promoter",
        desc = "Increase target subject body mass, by reducing hormones from the thyroid gland slowing down metabolism, thus causing weight gain.",
        positive_slug = "+{weight=0.453}/On Remove\n+30% Chance/Turn",
        negative_slug = "-20 Max Energy",
        research_added = 80,
        base_side_effect_chance = 40,
        on_apply = weight_gain_on_apply,
        on_remove = weight_gain_on_remove,
        on_turn = weight_gain_on_turn,
        requires = [basic_med_app],
        tier = 1,
        research_needed = 150,
        exclude_tags = ["Weight Modification"],
        clarity_cost = 200,
        hidden_tag = "Physical",
        mental_aspect = 1, physical_aspect = 3, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 1)
    global weight_loss
    weight_loss = SerumTrait(name = "Weight Loss Promoter",
        desc = "Decrease target subject body mass, using peptide YY3-36 as a serum component that acts on the hypothalamic feeding centres to inhibit hunger and calorie intake.",
        positive_slug = "-{weight=0.453}/On Remove\n+30% Chance/Turn",
        negative_slug = "-20 Max Energy",
        research_added = 160,
        base_side_effect_chance = 80,
        on_apply = weight_loss_on_apply,
        on_remove = weight_loss_on_remove,
        on_turn = weight_loss_on_turn,
        requires = [basic_med_app],
        tier = 1,
        research_needed = 500,
        exclude_tags = ["Weight Modification"],
        clarity_cost = 700,
        hidden_tag = "Physical",
        mental_aspect = 1, physical_aspect = 4, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 2)
    global volatile_reaction
    volatile_reaction = SerumTrait(name = "Volatile Reaction",
        desc = "In order to create a serum that will have unintentional side effects, this trait will apply an extra random trait and a side effect, while researching a design.",
        positive_slug = "1 Trait Slot\nAdds a random trait to the design on completion.",
        negative_slug = "Adds a random side effect to the design on completion.",
        slots_added = 1,
        research_added = 200,
        base_side_effect_chance = 0,
        requires = [clinical_testing],
        tier = 1,
        research_needed = 100,
        clarity_cost = 100,
        hidden_tag = "Capacity",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0)
    global anti_biotics_trait
    anti_biotics_trait = SerumTrait(name = "Anti-Biotics",
        desc = "Normal medical serum that combats bacterial infections.",
        positive_slug = "Permanent +2 Happiness",
        negative_slug = "",
        research_added = 20,
        base_side_effect_chance = 5,
        on_apply = anti_biotics_trait_on_apply,
        requires = [basic_med_app],
        tier = 1,
        start_researched = False,
        research_needed = 50,
        clarity_cost = 50,
        hidden_tag = "Medical",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 0)
    global exotic_components
    exotic_components = SerumTrait(name = "Exotic Ingredients",
        desc = "Exotic sounding ingredients from unlikely sources ranging from unheard of tree saps to rare flower products give the customers the idea that this serum must be very special indeed, and increase its sale value accordingly. There is no change to the effects of the serum.",
        positive_slug = "",
        negative_slug = "",
        research_added = 100,
        base_side_effect_chance = 1,
        requires = [basic_med_app, improved_serum_prod],
        tier = 1,
        research_needed = 300,
        clarity_cost = 300,
        hidden_tag = "Medical",
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = -1, attention = 0)
    global antidote_trait
    antidote_trait = SerumTrait("Antidote",
        desc = "The antidote counters the toxic effect of a serum on the body, this will temporarily increase the subject's serum tolerance by one.",
        positive_slug = "Base Serum Tolerance +1 (does not stack)",
        negative_slug="",
        research_added = 100,
        base_side_effect_chance = 0,
        on_apply = antidote_on_apply,
        on_remove = antidote_on_remove,
        requires = [basic_med_app],
        tier = 1,
        research_needed = 200,
        clarity_cost = 300,
        hidden_tag = "Medical",
        mental_aspect = 0, physical_aspect = 3, sexual_aspect = 0, medical_aspect = 1, flaws_aspect = 0, attention = 0)

    global list_of_traits
    list_of_traits.extend((
        # Tier 1
        improved_serum_prod,
        improved_duration_trait,
        off_label_drugs,
        aphrodisiac,
        love_potion,
        obedience_enhancer,
        large_obedience_enhancer,
        clinical_testing,
        mood_enhancer,
        refined_caffeine_trait,
        birth_control_suppression,
        fertility_enhancement_trait,
        fertility_suppression_trait,
        lactation_hormones,
        oral_enhancer,
        climax_limiter,
        weight_gain,
        weight_loss,
        volatile_reaction,
        anti_biotics_trait,
        exotic_components,
        antidote_trait,
    ))
