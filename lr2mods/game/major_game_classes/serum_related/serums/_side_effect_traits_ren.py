#Serum trait functions. Each serum trait can have up to four key functions: on_apply, on_remove, on_turn, and on_day. These are run at various points throughout the game.

##Guidelines##
# Side effects generally give 1 flaw point, but may also add other aspects, in particular Attention.
from __future__ import annotations
import renpy
from renpy.color import Color
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait
from game.major_game_classes.serum_related.serums._blueprint_serum_traits_ren import hair_colour_change_on_turn

list_of_side_effects: list[SerumTrait] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
## depressant_side_effect_functions ##
def depressant_side_effect_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-20)

## libido_suppressant_functions ##
def libido_suppressant_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_slut(-20)
    serum.effects_dict["libido_suppressant"] = change_amount

def libido_suppressant_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("libido_suppressant", -20)
    person.change_slut(-(-20 if change_amount is None else change_amount), add_to_log = add_to_log)

## anxiety_provoking_functions ##
def anxiety_provoking_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-3, add_to_log = add_to_log)

## performance_inhibitor_functions ##
def performance_inhibitor_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_int(-1, add_to_log = add_to_log)
    person.change_focus(-1, add_to_log = add_to_log)
    person.change_cha(-1, add_to_log = add_to_log)

def performance_inhibitor_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_int(1, add_to_log = add_to_log)
    person.change_focus(1, add_to_log = add_to_log)
    person.change_cha(1, add_to_log = add_to_log)

## mood_swings_functions ##
def mood_swings_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    swing = renpy.random.randint(0, 1)
    if swing == 0:
        person.change_happiness(-10, add_to_log = add_to_log)
    else:
        person.change_happiness(10, add_to_log = add_to_log)

## Sedative functions ##
def sedative_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-20, add_to_log = add_to_log)

def sedative_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(20, add_to_log = add_to_log) #They don't get the normal energy back instantly, it has to come back on it's own

## Slow release sedative functions ##
def slow_release_sedative_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_energy(-10)

## Toxic functions ##
def toxic_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person._serum_tolerance -= 1

def toxic_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person._serum_tolerance += 1

## stimulation suppressant ##
def stimulation_suppressant_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_arousal(40, add_to_log = add_to_log)

def stimulation_suppressant_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_arousal(-40, add_to_log = add_to_log)

## hair colour changes ##
def hair_colour_wild_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    serum.effects_dict['random_colour'] = Color((renpy.random.randint(0, 255), renpy.random.randint(0, 255), renpy.random.randint(0, 255), 230))

def hair_colour_wild_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    random_colour = serum.effects_dict.get('random_colour', Color((renpy.random.randint(0, 255), renpy.random.randint(0, 255), renpy.random.randint(0, 255), 242)))
    hair_colour_change_on_turn(random_colour, person, serum, add_to_log)

def hair_colour_dull_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    # safeguard against invalid hair_colour variables
    if isinstance(person.hair_colour, list) and len(person.hair_colour) == 2:
        current_colour = Color(rgb=(person.hair_colour[1][0], person.hair_colour[1][1], person.hair_colour[1][2]), alpha = person.hair_colour[1][3])
        goal_colour = current_colour.replace_hsv_saturation(0.0)

        hair_colour_change_on_turn(goal_colour, person, serum, add_to_log)

## uncontrollable_arousal_side_effect_functions ##
def uncontrollable_arousal_side_effect_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_slut(20, add_to_log = add_to_log)
    serum.effects_dict["uncontrollable_arousal_effect"] = change_amount

def uncontrollable_arousal_side_effect_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("uncontrollable_arousal_effect", 20)
    person.change_slut(-(20 if change_amount is None else change_amount), add_to_log = add_to_log)

## tryptamine_side_effect_functions ##
def tryptamine_side_effect_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_obedience(10, add_to_log = add_to_log)
    serum.effects_dict["tryptamine_effect"] = change_amount

def tryptamine_side_effect_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("tryptamine_effect", 10)
    person.change_obedience(-(10 if change_amount is None else change_amount), add_to_log = add_to_log)

## oxytocin_side_effect_functions ##
def oxytocin_side_effect_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_love(1, 40, add_to_log = False)

def skin_sensitivity_side_effect_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_arousal(5, add_to_log = add_to_log)

def pleasant_taste_side_effect_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(5)

def init_side_effect_traits():
    global depressant_side_effect
    depressant_side_effect = SerumTrait(name = "Depressant",
        desc = "An unintended interaction produces a sudden and noticeable drop in the recipients mood without any corresponding improvement when the serum expires.",
        positive_slug = "",
        negative_slug = "-20 Happiness When Applied, -$5 Value",
        on_apply = depressant_side_effect_on_apply,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global unpleasant_taste_side_effect
    unpleasant_taste_side_effect = SerumTrait(name = "Unpleasant Taste",
        desc = "This serum has a prominent and decidedly unpleasant taste. While it does not decrease the effectiveness of the serum it has a large impact on its value when sold.",
        positive_slug = "",
        negative_slug = "",
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 2, attention = 1)
    global pleasant_taste_side_effect
    pleasant_taste_side_effect = SerumTrait(name = "Liquorice Taste",
        desc = "This serum has a prominent and pleasant liquorice taste. It adds a slight happiness boost to the serum.",
        positive_slug = "+5 Happiness when applied",
        negative_slug = "",
        is_side_effect = True,
        on_apply = pleasant_taste_side_effect_on_apply,
        mental_aspect = 1, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0)
    global bad_reputation
    bad_reputation = SerumTrait(name = "Bad Reputation",
        desc = "This serum design has developed a particularly bad reputation. Regardless of it being based on facts or not, it has a significant effect on the price customers are willing to pay.",
        positive_slug = "",
        negative_slug = "",
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 2, attention = 2)
    global unstable_reaction
    unstable_reaction = SerumTrait(name = "Unstable Reaction",
        desc = "The reaction used to create this serum was less stable than initially hypothesised. Reduces serum duration by two turns.",
        positive_slug = "",
        negative_slug = "-2 Turn Duration",
        duration_added = -2,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global stable_solution_side_effect
    stable_solution_side_effect = SerumTrait(name = "Stable Solution",
        desc = "The solution is more stable than initially hypothesized. Increases duration of the serum by two turns.",
        positive_slug = "+2 Turn Duration",
        negative_slug = "",
        duration_added = 2,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 1)
    global manual_synthesis_required
    manual_synthesis_required = SerumTrait(name = "Manual Synthesis Required",
        desc = "A step in this serums manufacturing process requires manual intervention, preventing the use of time saving automation. This has no impact on effectiveness or value, but increases the amount of production effort required.",
        positive_slug = "",
        negative_slug = "",
        production_added = 20,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 0)
    global libido_suppressant
    libido_suppressant = SerumTrait(name = "Libido Suppressant",
        desc = "An unintended interaction results in a major decrease in the recipients sex drive for the duration of this serum.",
        positive_slug = "",
        negative_slug = "-20 Sluttiness",
        on_apply = libido_suppressant_on_apply,
        on_remove = libido_suppressant_on_remove,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global anxiety_provoking
    anxiety_provoking = SerumTrait(name = "Anxiety Provoking",
        desc = "An unintended interaction creates a subtle but pervasive sense of anxiety in the recipient. This has a direct effect on their happiness.",
        positive_slug = "",
        negative_slug = "-3 Happiness/Turn",
        on_turn = anxiety_provoking_on_turn,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global performance_inhibitor
    performance_inhibitor = SerumTrait(name = "Performance Inhibitor",
        desc = "For reasons not understood by your R&D team this serum causes a general decrease in the recipients ability to do work for the duration of the serum.",
        positive_slug = "",
        negative_slug = "-1 Intelligence, Focus, and Charisma",
        on_apply = performance_inhibitor_on_apply,
        on_remove = performance_inhibitor_on_remove,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global mood_swings
    mood_swings = SerumTrait(name = "Mood Swings",
        desc = "The recipient suffers large, sudden, and unpleasant mood swings.",
        positive_slug = "",
        negative_slug = "Random +10 or -10 Happiness/Turn",
        on_day = mood_swings_on_turn,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global sedative
    sedative = SerumTrait(name = "Accidental Sedative",
        desc = "This serum has the unintended side effect of slightly sedating the recipient. Their maximum energy is reduced for the duration.",
        positive_slug = "",
        negative_slug = "-20 Maximum Energy",
        on_apply = sedative_on_apply,
        on_remove = sedative_on_remove,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global slow_release_sedative
    slow_release_sedative = SerumTrait(name = "Slow Acting Sedative",
        desc = "This serum produces slow acting sedative effects, reducing how quickly the recipient bounces back from tiring tasks. Reduces energy gain for the duration.",
        positive_slug = "",
        negative_slug = "-10 Energy per Turn",
        on_turn = slow_release_sedative_on_turn,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global toxic_side_effect
    toxic_side_effect = SerumTrait(name = "Toxic",
        desc = "Mildly toxic interactions make this serum dangerous to mix with other medications at any dose. Reduces serum tolerance for the duration.",
        positive_slug = "",
        negative_slug = "-1 Serum Tolerance",
        on_apply = toxic_on_apply,
        on_remove = toxic_on_remove,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global stimulation_suppressant_effect
    stimulation_suppressant_effect = SerumTrait(name = "Stimulation Suppressant",
        desc = "Interactions with the body's nervous system makes it very difficult for the subject to orgasm. A common side effect for many medications.",
        positive_slug = "",
        negative_slug = "+40 Max Arousal",
        on_apply = stimulation_suppressant_on_apply,
        on_remove = stimulation_suppressant_on_remove,
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 1)
    global hair_colour_wild_effect
    hair_colour_wild_effect = SerumTrait(name = "Hair Colour Shifts",
        desc = "Complex interactions produce visible changes in hair colour. Produces random and sometimes striking changes in hair colour over time.",
        positive_slug = "",
        negative_slug = "Random Hair Colour Changes",
        on_apply = hair_colour_wild_on_apply,
        on_turn = hair_colour_wild_on_turn,
        exclude_tags = "Dye",
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 2)
    global hair_colour_dull_effect
    hair_colour_dull_effect = SerumTrait(name = "Dull Hair",
        desc = "Complex interactions produce visible changes in hair colour. Has the effect of dulling down the hair colour of the subject.",
        positive_slug = "",
        negative_slug = "Reduces Hair Saturation",
        on_turn = hair_colour_dull_on_turn,
        exclude_tags = "Dye",
        is_side_effect = True,
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 2)
    global uncontrollable_arousal_side_effect
    uncontrollable_arousal_side_effect = SerumTrait(name = "Uncontrollable Arousal",
        desc = "An unintended interaction produces a sudden and noticeable spike in the recipient's promiscuity, making them more agreeable to lewd interactions.",
        positive_slug = "+20 Sluttiness for duration",
        negative_slug = "",
        on_apply = uncontrollable_arousal_side_effect_on_apply,
        on_remove = uncontrollable_arousal_side_effect_on_remove,
        is_side_effect = True,
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 2)
    global tryptamine_side_effect
    tryptamine_side_effect = SerumTrait(name = "Tryptamine Induction",
        desc = "An unintended interaction produces a sudden and noticeable degradation of the subject's free will, making them susceptible to suggestion for the duration.",
        positive_slug = "+10 Obedience for duration",
        negative_slug = "",
        on_apply = tryptamine_side_effect_on_apply,
        on_remove = tryptamine_side_effect_on_remove,
        is_side_effect = True,
        mental_aspect = 2, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 1)
    global oxytocin_side_effect
    oxytocin_side_effect = SerumTrait(name = "Oxytocin Increment",
        desc = "An unintended interaction produces a sudden and lasting emotional connection to a person, but only when they have no deep connection already.",
        positive_slug = "Permanent +1 Love/Turn when Love < 40",
        negative_slug = "",
        on_turn = oxytocin_side_effect_on_turn,
        is_side_effect = True,
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)

    global list_of_side_effects
    list_of_side_effects.extend((
        depressant_side_effect,
        bad_reputation,
        unpleasant_taste_side_effect,
        pleasant_taste_side_effect,
        unstable_reaction,
        stable_solution_side_effect,
        manual_synthesis_required,
        libido_suppressant,
        anxiety_provoking,
        performance_inhibitor,
        mood_swings,
        sedative,
        slow_release_sedative,
        toxic_side_effect,
        stimulation_suppressant_effect,
        hair_colour_wild_effect,
        hair_colour_dull_effect,
        uncontrollable_arousal_side_effect,
        tryptamine_side_effect,
        oxytocin_side_effect,
    ))
