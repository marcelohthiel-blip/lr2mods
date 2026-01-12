## SERUM TRAIT GUIDELINES ##
# These are some guidelines for how serum traits are priced out.
# Each tier of serum trait should provide 2*(tier+1) aspect points.
# Add 1 extra aspect point per point of attention.

#Serum trait functions. Each serum trait can have up to four key functions: on_apply, on_remove, on_turn, and on_day. These are run at various points throughout the game.

from __future__ import annotations
import copy
from game.bugfix_additions.debug_info_ren import add_to_debug_log
import renpy
from game.personality_types._personality_definitions_ren import bimbo_personality
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import advanced_serum_prod, blood_brain_pen, pregnancy_accelerator_trait, low_volatility_reagents

list_of_traits: list[SerumTrait] = []
day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

## mind_control_agent_functions ##
def mind_control_agent_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.add_suggest_effect(70, add_to_log = add_to_log)

def mind_control_agent_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.remove_suggest_effect(70)

## permanent_bimbo_functions ##
def permanent_bimbo_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_personality(bimbo_personality)
    person.change_slut(10, add_to_log = add_to_log)
    person.change_obedience(10, add_to_log = add_to_log)

    if person.int > 1:
        person.change_int(1 - person.int, add_to_log = add_to_log)
    if person.focus > 1:
        person.change_focus(1 - person.focus, add_to_log = add_to_log)
    person.change_personality(bimbo_personality)
    if add_to_log:
        mc.log_event(f"{person.display_name}: Personality changed. Now: Bimbo", "float_text_pink")

def anti_bimbo_serum_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.personality != bimbo_personality: #WE only run if we have the bimbo personality
        return

    person.restore_original_personality()
    if person.int < 3: # only change int when less than 3
        person.change_int(renpy.random.randint(3, 6), True)
    if person.focus < 3:
        person.change_focus(renpy.random.randint(3, 6), True)
    if add_to_log:
        mc.log_event(f"{person.display_name}: Personality changed.", "float_text_pink")

def massive_pregnancy_accelerator_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
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

def self_generating_serum_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    generated_serum = copy.copy(serum)
    generated_serum.duration -= 1
    generated_serum.duration_counter = 0

    if generated_serum.duration > 0: # when duration is up, the serum fizzles out
        person.give_serum(generated_serum, add_to_log = False)

def immediate_ovulation_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.ideal_fertile_day = ((day + 1) % 30)
    person.change_baby_desire(5)
    if add_to_log:
        mc.log_event(f"{person.display_name}: ovum is maturing", "float_text_red")

# Tier 3 traits produce large effects at a cost or moderate ones for free.
def init_T3_traits():
    global futuristic_serum_prod
    futuristic_serum_prod = SerumTrait(name = "Futuristic Serum Production",
        desc = "Space age technology makes the serum incredibly versatile. Adds seven serum trait slots at an increased production cost.",
        positive_slug = "7 Trait Slots\n3 Turn Duration",
        negative_slug = "",
        research_added = 500,
        slots_added = 7,
        production_added = 120,
        duration_added = 3,
        base_side_effect_chance = 60,
        clarity_added = 1250,
        requires = advanced_serum_prod,
        tier = 3,
        research_needed = 3000,
        exclude_tags = "Production",
        clarity_cost = 2500,
        hidden_tag = "Production",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 5, flaws_aspect = 0, attention = 2)

    global mind_control_agent
    mind_control_agent = SerumTrait(name = "Mind Control Agent",
        desc = "This low grade mind control agent will massively increase the suggestibility of the recipient, resulting in rapid changes in personality based on external stimuli.",
        positive_slug = "+70 Suggestibility",
        negative_slug = "",
        research_added = 200,
        base_side_effect_chance = 50,
        on_apply = mind_control_agent_on_apply,
        on_remove = mind_control_agent_on_remove,
        requires = blood_brain_pen,
        tier = 3,
        research_needed = 1500,
        exclude_tags = "Suggest",
        clarity_cost = 2000,
        hidden_tag = "Suggest",
        mental_aspect = 7, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 5, flaws_aspect = 0, attention = 4)
    global permanent_bimbo
    permanent_bimbo = SerumTrait(name = "Permanent Bimbofication",
        desc = "This delicate chemical cocktail was reverse engineered from an experimental serum sample in the lab and will turn the recipient into a complete bimbo. Intelligence, Focus and obedience will suffer, but she will be happy and slutty. This change is permanent.",
        positive_slug = "New Personality: Bimbo, +10 Permanent Sluttiness, +10 Permanent Obedience",
        negative_slug = "Permanent Int / Focus to 1",
        research_added = 400,
        base_side_effect_chance = 80,
        on_apply = permanent_bimbo_on_apply,
        requires = mind_control_agent,
        tier = 3,
        research_needed = 2000,
        exclude_tags = "Personality",
        clarity_cost = 2200,
        hidden_tag = "Unique",
        mental_aspect = 9, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 5)
    global anti_bimbo_serum_trait
    anti_bimbo_serum_trait = SerumTrait(name = "Bimbo Reversal",
        desc = "This serum doesn't completely counter the bimbo serum, but it returns her original personality, intelligence and focus are restored partially.",
        positive_slug = "Restores partial Intelligence / Focus, Restores Personality",
        negative_slug = "",
        research_added = 400,
        base_side_effect_chance = 50,
        on_apply = anti_bimbo_serum_function_on_apply,
        requires = permanent_bimbo,
        tier = 99,
        research_needed = 3000,
        exclude_tags = ["Personality"],
        clarity_cost = 2200,
        hidden_tag = "Unique",
        mental_aspect = 9, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 5, flaws_aspect = 0, attention = 5)
    global massive_pregnancy_accelerator
    massive_pregnancy_accelerator = SerumTrait(name = "Extreme Pregnancy Hormones",
        desc = "Overloads the body with natural pregnancy hormones alongside nutrient supplements. Massively increases the pace at which a pregnancy will progress.",
        positive_slug = "+1 Pregnancy Progress/Turn",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 80,
        on_turn = massive_pregnancy_accelerator_on_turn,
        requires = [pregnancy_accelerator_trait],
        tier = 3,
        research_needed = 1400,
        mental_aspect = 0, physical_aspect = 9, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 4,
        exclude_tags = "Pregnancy",
        hidden_tag = "Reproduction",
        clarity_cost = 1800)
    global self_generating_serum
    self_generating_serum = SerumTrait(name = "Self Replicating Serum",
        desc = "Inserts instructions for the creation of this serum into the subject's cells, allowing them to create a copy of the serum in the body, each copy will decrease its duration by 1, until it fades away.",
        positive_slug = "+3 Turn Duration, Long-Lasting Duration",
        negative_slug = "",
        duration_added = 3,
        research_added = 800,
        base_side_effect_chance = 200,
        on_remove = self_generating_serum_on_remove,
        requires = [low_volatility_reagents, futuristic_serum_prod],
        tier = 3,
        research_needed = 2400,
        clarity_cost = 3000,
        hidden_tag = "Duration",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 7, attention = 3)
    #based on original by JoZEr from f95
    global immediate_ovulation
    immediate_ovulation = SerumTrait(name = "Immediate Ovulation",
        desc = "Causes rapid maturation of a fertile ovum and alters the recipients natural fertility cycle.",
        positive_slug = "Ovum will mature next day",
        negative_slug = "Alter fertility cycle",
        research_added = 500,
        base_side_effect_chance = 80,
        on_apply = immediate_ovulation_on_apply,
        requires = [pregnancy_accelerator_trait],
        tier = 3,
        research_needed = 1600,
        hidden_tag = "Reproduction",
        mental_aspect = 2, physical_aspect = 7, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 4,
        clarity_cost = 2000)

    global list_of_traits
    list_of_traits.extend((
        futuristic_serum_prod,
        mind_control_agent,
        permanent_bimbo,
        massive_pregnancy_accelerator,
        self_generating_serum,
        immediate_ovulation
    ))
