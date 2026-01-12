from __future__ import annotations
import builtins
import renpy
from game.game_roles._role_definitions_ren import trance_role
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign, SerumTrait, list_of_traits
from game.personality_types._personality_definitions_ren import bimbo_personality

list_of_nora_traits: list[SerumTrait] = []
day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

## nora_serum_up_trait ##
def nora_suggest_up_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.add_suggest_effect(40, add_to_log = add_to_log)

def nora_suggest_up_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.remove_suggest_effect(40)

def nora_nightmares_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(-15, add_to_log = add_to_log)

def nora_obedience_swing_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = renpy.random.randint(-15, 15)
    person.change_obedience(change_amount)

def nora_sluttiness_boost_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_slut(20, add_to_log = add_to_log)
    serum.effects_dict["nora_sluttiness"] = change_amount

def nora_sluttiness_boost_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("nora_sluttiness", 20)
    person.change_slut(-change_amount, add_to_log = add_to_log)

## nora_special_unlock_traits
def nora_reward_mother_trait_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    amount_change = builtins.int((person.sluttiness - person.love) / 10.0)
    if amount_change > 0:
        person.change_love(amount_change, add_to_log = add_to_log)


def nora_reward_sister_trait_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    amount_change = min(max(int((person.obedience - 120) // 20.0), 1), 5)  # 140 = 1, 160 = 2 etc with max 5
    if amount_change > 0:
        person.change_slut(amount_change, add_to_log = add_to_log)

def nora_reward_cousin_trait_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.love > 0:
        return
    amount_change = min(max(int(-person.love // 20.0), 1), 3) # max 3 sluttiness per day based on hate
    if amount_change > 0:
        person.change_slut(amount_change, add_to_log = add_to_log)

def nora_reward_nora_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    amount = 5 * mc.int
    change_slut = person.change_slut(amount, add_to_log = add_to_log)
    serum.effects_dict["nora_reward_nora_slut"] = change_slut
    change_obed = person.change_obedience(amount, add_to_log = add_to_log)
    serum.effects_dict["nora_reward_nora_obed"] = change_obed

def nora_reward_nora_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_slut = serum.effects_dict.get("nora_reward_nora_slut", 5 * mc.int)
    person.change_slut(-change_slut, add_to_log = add_to_log)
    change_obed = serum.effects_dict.get("nora_reward_nora_obed", 5 * mc.int)
    person.change_obedience(-change_obed, add_to_log = add_to_log)

def nora_reward_high_love_trait_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.sluttiness > person.love and person.love < 100:
        person.change_slut(-1, add_to_log = add_to_log)
        person.change_love(1, add_to_log = add_to_log)

def nora_reward_low_love_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = person.change_love(-50, add_to_log = add_to_log)
    serum.effects_dict["nora_low_love"] = change_amount

def nora_reward_low_love_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    change_amount = serum.effects_dict.get("nora_low_love", -50)
    person.change_love(-change_amount, add_to_log = add_to_log)

def nora_reward_high_obedience_trait_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    amount = builtins.round((person.obedience - 100) / 5)
    person.change_happiness(amount, add_to_log = add_to_log)

def nora_reward_high_slut_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_slut(5, add_to_log = add_to_log)

def nora_reward_genius_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.personality == bimbo_personality:
        mc.log_event(f"{person.display_name}: bimbo personality blocks the Nora Natural Talent trait", "float_text_pink")
        return

    stats: list[str] = []
    if person.charisma < 7:
        change = person.change_cha(7 - person.charisma, add_to_log = False)
        stats.append(f"{change:+.0f} charisma")
    if person.int < 7:
        change = person.change_int(7 - person.int, add_to_log = False)
        stats.append(f"{change:+.0f} intelligence")
    if person.focus < 7:
        change = person.change_focus(7 - person.focus, add_to_log = False)
        stats.append(f"{change:+.0f} focus")

    if add_to_log and stats:
        mc.log_event(f"{person.display_name}: {', '.join(stats)}", "float_text_blue")

def nora_reward_hucow_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.event_triggers_dict.get("nora_hucow_trait", False):
        return

    person.event_triggers_dict["nora_hucow_trait"] = True # set stack flag
    person.bc_penalty += 75
    person.fertility_percent += 70
    person.lactation_sources += 3

    max_tit_changes = 2
    max_tit_rank = Person.rank_tits(Person.get_maximum_tit())
    tit_changes = builtins.min(max_tit_rank - Person.rank_tits(person.tits), max_tit_changes)

    for _ in range(tit_changes):
        person.increase_tit_size()

    serum.effects_dict["nora_hucow_tit_changes"] = tit_changes

    if add_to_log:
        mc.log_event(f"{person.display_name}: Human Breeding started", "float_text_grey")
        if person in mc.location.people: #If you're here applying this trait in person it causes her to exclaim.
            renpy.say(f"{person.display_name}", "Oh my god my tits feel... bigger!")

def nora_reward_hucow_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.event_triggers_dict.get("nora_hucow_trait", False):
        return

    person.bc_penalty -= 75
    person.fertility_percent -= 70
    person.lactation_sources -= 3

    # restores original tit-size
    tit_changes = serum.effects_dict.get("nora_hucow_tit_changes", 2)
    for _ in range(tit_changes):
        person.decrease_tit_size()

    if add_to_log:
        mc.log_event(f"{person.display_name}: Human Breeding ended", "float_text_grey")

    person.event_triggers_dict["nora_hucow_trait"] = False # remove stack flag

def nora_reward_instant_trance_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.is_in_trance:
        person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = add_to_log)


## Nora unstable traits

def nora_unstable_slut_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_stats(
        slut = nora_unstable_slut_trait.mastery_range(1, 3),
        max_slut = nora_unstable_slut_trait.mastery_range(20, 100),
        obedience = -nora_unstable_obedience_trait.mastery_range_inverted(1, 3)
    )

def nora_unstable_obedience_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_obedience(nora_unstable_obedience_trait.mastery_range(1, 3), nora_unstable_obedience_trait.mastery_range(120, 200), add_to_log = add_to_log)

def nora_unstable_love_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_love(nora_unstable_love_trait.mastery_range(1, 3), nora_unstable_love_trait.mastery_range(20, 100), add_to_log = add_to_log)

def nora_unstable_happiness_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_happiness(nora_unstable_happiness_trait.mastery_range(1, 5), nora_unstable_happiness_trait.mastery_range(120, 200), add_to_log = add_to_log)

def nora_unstable_energy_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_energy(nora_unstable_energy_trait.mastery_range(1, 3), add_to_log = add_to_log)

def nora_unstable_energy_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    serum.effects_dict["unstable_max_energy"] = person.change_max_energy(nora_unstable_energy_trait.mastery_range(20, 60), add_to_log = add_to_log)

def nora_unstable_energy_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    person.change_max_energy(-serum.effects_dict.get("unstable_max_energy", 20), add_to_log = add_to_log)

def init_nora_special_traits():
    ### Nora research traits ###
    global nora_suggest_up
    nora_suggest_up = SerumTrait(name = "Nora's Research Trait XRC",
        desc = "The manufacturing details for a serum trait developed by Nora. Raises suggestibility significantly, but is guaranteed to generate a side effect and negatively effects value.",
        positive_slug = "+40 Suggestibility",
        negative_slug = "",
        research_added = 75,
        base_side_effect_chance = 1000000,
        on_apply = nora_suggest_up_on_apply,
        on_remove = nora_suggest_up_on_remove,
        tier = 1,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        exclude_tags = "Suggest",
        hidden_tag = "Suggest",
        mental_aspect = 8, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 2, attention = 2,
        nora_trait = True)
    global nora_nightmares
    nora_nightmares = SerumTrait(name = "Nora's Research Trait CBX",
        desc = "The manufacturing details for a serum trait developed by Nora. Negatively affects the recipient's sleep, as well as generating a side effect and negatively effecting value.",
        negative_slug = "-15 Happiness/Night",
        research_added = 75,
        base_side_effect_chance = 1000000,
        on_day = nora_nightmares_on_day,
        tier = 1,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Medical",
        mental_aspect = 4, physical_aspect = 4, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 2, attention = 2,
        nora_trait = True)
    global nora_obedience_swing
    nora_obedience_swing = SerumTrait(name = "Nora's Research Trait XBR",
        desc = "The manufacturing details for a serum trait developed by Nora. Causes wild fluctuations in the recipient's willingness to follow orders, as well as generating a side effect and negatively effecting value.",
        negative_slug = "Random Obedience Changes",
        research_added = 75,
        base_side_effect_chance = 1000000,
        on_turn = nora_obedience_swing_on_turn,
        tier = 1,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Obedience",
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 2, attention = 2,
        nora_trait = True)
    global nora_sluttiness_boost
    nora_sluttiness_boost = SerumTrait(name = "Nora's Research Trait RXC",
        desc = "The manufacturing details for a serum trait developed by Nora. Causes a sudden spike in the recipient's sluttiness, as well as generating a side effect and negatively effecting value.",
        positive_slug = "+20 Temporary Sluttiness",
        negative_slug = "",
        research_added = 75,
        base_side_effect_chance = 1000000,
        on_apply = nora_sluttiness_boost_on_apply,
        on_remove = nora_sluttiness_boost_on_remove,
        tier = 1,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Slut",
        mental_aspect = 2, physical_aspect = 0, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 2, attention = 2,
        nora_trait = True)

    # Nora initial research traits for unlocking her special traits
    list_of_nora_traits.extend((
        nora_suggest_up,
        nora_nightmares,
        nora_obedience_swing,
        nora_sluttiness_boost,
    ))

    ### Nora boss unlock traits ###
    global nora_reward_mother_trait
    nora_reward_mother_trait = SerumTrait(name = "Motherly Devotion",
        desc = "A special serum trait developed by Nora after studying your mother. Permanently increases the recipient's Love by 1 per turn for every 10 points that their Sluttiness is higher than Love.",
        positive_slug = "+1 Love/Turn per 10 Sluttiness greater than Love",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 50,
        on_turn = nora_reward_mother_trait_on_turn,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Love",
        mental_aspect = 6, physical_aspect = 0, sexual_aspect = 3, medical_aspect = 0, flaws_aspect = 0, attention = 1,
        nora_trait = True)
    global nora_reward_sister_trait
    nora_reward_sister_trait = SerumTrait(name = "Sisterly Obedience",
        desc = "A special serum trait developed by Nora after studying your sister. Permanently increases the recipient's Sluttiness by 1-5 per day based on their Obedience.",
        positive_slug = "1-5 sluttiness/day based on obedience",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 75,
        on_day = nora_reward_sister_trait_on_day,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Slut",
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 7, medical_aspect = 0, flaws_aspect = 0, attention = 2,
        nora_trait = True)
    global nora_reward_cousin_trait
    nora_reward_cousin_trait = SerumTrait(name = "Cousinly Hate",
        desc = "A special serum trait developed by Nora after studying your cousin. Permanently increases the recipient's Sluttiness by 1-3 per day based on negative love value.",
        positive_slug = "+1-3 Sluttiness/Day based on hate",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 50,
        on_day = nora_reward_cousin_trait_on_day,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Slut",
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 7, medical_aspect = 0, flaws_aspect = 0, attention = 3,
        nora_trait = True)
    global nora_reward_aunt_trait
    nora_reward_aunt_trait = SerumTrait(name = "Aunty Potential",
        desc = "A special serum trait developed by Nora after studying your aunt. Increases the number of traits a serum design may contain by 2.",
        positive_slug = "+2 Extra Trait Slots",
        negative_slug = "",
        research_added = 300,
        slots_added = 3,
        base_side_effect_chance = 100,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Capacity",
        mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 1,
        nora_trait = True)
    global nora_reward_nora_trait
    nora_reward_nora_trait = SerumTrait(name = "Meritocratic Attraction",
        desc = "A special serum trait developed by Nora after studying herself. Increases the recipient's Obedience and Sluttiness for the duration by 5 for every point of Intelligence you have.",
        positive_slug = "+5 Temporary Obedience and Sluttiness per Intelligence",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 50,
        on_apply = nora_reward_nora_trait_on_apply,
        on_remove = nora_reward_nora_trait_on_remove,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = ["Obedience", "Slut"],
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 0, attention = 2,
        nora_trait = True)
    global nora_reward_high_love_trait
    nora_reward_high_love_trait = SerumTrait(name = "Lovers Attraction",
        desc = "A special serum trait developed by Nora after studying someone who adores you. Each turn permanently converts one point of Sluttiness into Love until they are equal.",
        positive_slug = "Converts 1 Sluttiness to Love per turn until equal",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 75,
        on_turn = nora_reward_high_love_trait_on_turn,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Love",
        mental_aspect = 6, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 2,
        nora_trait = True)
    global nora_reward_low_love_trait
    nora_reward_low_love_trait = SerumTrait(name = "Distilled Disgust",
        desc = "A special serum trait developed by Nora after studying someone who absolutely hates you. Gives a massive penalty to love for the duration of the serum.",
        positive_slug = "",
        negative_slug = "-50 Love",
        research_added = 300,
        base_side_effect_chance = 10,
        on_apply = nora_reward_low_love_trait_on_apply,
        on_remove = nora_reward_low_love_trait_on_remove,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Love",
        mental_aspect = 9, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 1,
        nora_trait = True)
    global nora_reward_high_obedience_trait
    nora_reward_high_obedience_trait = SerumTrait(name = "Pleasurable Obedience",
        desc = "A special serum trait developed by Nora after studying someone who was completely subservient to you. Increases happiness by 1 for every 5 points of Obedience over 100 per turn.",
        positive_slug = "+1 Happiness/Turn per 5 Obedience over 100",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 50,
        on_turn = nora_reward_high_obedience_trait_on_turn,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Medical",
        mental_aspect = 7, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 1,
        nora_trait = True)
    global nora_reward_high_slut_trait
    nora_reward_high_slut_trait = SerumTrait(name = "Rapid Corruption",
        desc = "A special serum trait developed by Nora after studying someone who was a complete slut. Instantly and permanently increases their Sluttiness by 5.",
        positive_slug = "+5 Permanent Sluttiness",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 50,
        on_apply = nora_reward_high_slut_trait_on_apply,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Slut",
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 7, medical_aspect = 0, flaws_aspect = 0, attention = 3,
        nora_trait = True)
    global nora_reward_genius_trait
    nora_reward_genius_trait = SerumTrait(name = "Natural Talent",
        desc = "A special serum trait developed by Nora after studying someone who was a genius. Instantly and permanently raises the recipient's Intelligence, Charisma, and Focus to 7 if lower.",
        positive_slug = "Raises Charisma, Intelligence, Focus to 7",
        negative_slug = "",
        research_added = 1000,
        base_side_effect_chance = 300,
        on_apply = nora_reward_genius_trait_on_apply,
        tier = 2,
        start_researched = False,
        research_needed = 4000,
        clarity_cost = 8000,
        hidden_tag = "Skill",
        mental_aspect = 8, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 3,
        nora_trait = True)
    global nora_reward_hucow_trait
    nora_reward_hucow_trait = SerumTrait(name = "Human Breeding Hormones",
        desc = "A special serum trait developed by Nora after studying someone who was in the later stages of pregnancy. Massively decreases birth control effectiveness, increases fertility, and triggers breast swelling and lactation.",
        positive_slug = "+70% Fertility\n-75% BC Effectiveness\nIncreased Breast Size\nMassive Lactation",
        negative_slug = "Effect does not stack and will only be applied when not already in bloodstream",
        research_added = 300,
        base_side_effect_chance = 80,
        on_apply = nora_reward_hucow_trait_on_apply,
        on_remove = nora_reward_hucow_trait_on_remove,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Reproduction",
        mental_aspect = 0, physical_aspect = 8, sexual_aspect = 3, medical_aspect = 0, flaws_aspect = 0, attention = 3,
        nora_trait = True)
    global nora_reward_instant_trance
    nora_reward_instant_trance = SerumTrait(name = "Trance Inducer",
        desc = "A special serum trait developed by Nora after studying someone who was deep in a trance at the time. Instantly puts the subject in a Trance if they are not already in one. Does not deepen existing Trances.",
        positive_slug = "Induces Trance State",
        negative_slug = "",
        research_added = 300,
        base_side_effect_chance = 75,
        on_apply = nora_reward_instant_trance_on_apply,
        tier = 2,
        start_researched = False,
        research_needed = 1000,
        clarity_cost = 1000,
        hidden_tag = "Unique",
        mental_aspect = 8, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 3,
        nora_trait = True)

    ### Nora Unstable unlock traits ###
    global nora_unstable_slut_trait
    nora_unstable_slut_trait = SerumTrait(name = "Unstable Libido Enhancer",
        desc = "Careful distillation can concentrate the active ingredient from common aphrodisiacs, producing a sudden spike in sluttiness when consumed. The sexual frustration linked to this effect tends to make the recipient less obedient over time as well.",
        positive_slug = "+(1-3) Sluttiness/Turn\nMax:(20-100)",
        negative_slug = "-(1-3) Obedience/Turn\nHigh Attention",
        research_added = 75,
        base_side_effect_chance = 100,
        on_turn = nora_unstable_slut_on_turn,
        tier = 1,
        research_needed = 500,
        clarity_cost = 300,
        hidden_tag = "Slut",
        exclude_tags = "Unstable",
        start_researched = True,
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 3)
    global nora_unstable_obedience_trait
    nora_unstable_obedience_trait = SerumTrait(name = "Unstable Obedience Enhancer",
        desc = "An unstable obedience enhancement drug originally from another serum design company. Gets better with high mastery",
        positive_slug = "+(1-3) Obedience/Turn\nMax:(120-200)",
        negative_slug = "High Attention",
        research_added = 75,
        base_side_effect_chance = 100,
        on_turn = nora_unstable_obedience_on_turn,
        tier = 1,
        research_needed = 500,
        clarity_cost = 300,
        hidden_tag = "Obedience",
        exclude_tags = "Unstable",
        start_researched = True,
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 3)
    global nora_unstable_love_trait
    nora_unstable_love_trait = SerumTrait(name = "Unstable Love Enhancer",
        desc = "An unstable love enhancement drug originally from another serum design company. Gets better with high mastery",
        positive_slug = "+(1-3) Love/Turn\nMax:(20-100)",
        negative_slug = "High Attention",
        research_added = 75,
        base_side_effect_chance = 100,
        on_turn = nora_unstable_love_on_turn,
        tier = 1,
        research_needed = 500,
        clarity_cost = 300,
        hidden_tag = "Love",
        exclude_tags = "Unstable",
        start_researched = True,
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 3)
    global nora_unstable_happiness_trait
    nora_unstable_happiness_trait = SerumTrait(name = "Unstable Mood Enhancer",
        desc = "An unstable mood enhancement drug originally from another serum design company. Gets better with high mastery",
        positive_slug = "+(1-5) Happiness/Turn\nMax:(120-200)",
        negative_slug = "High Attention",
        research_added = 75,
        base_side_effect_chance = 100,
        on_turn = nora_unstable_happiness_on_turn,
        tier = 1,
        research_needed = 500,
        clarity_cost = 300,
        hidden_tag = "Medical",
        exclude_tags = "Unstable",
        start_researched = True,
        mental_aspect = 4, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 3)
    global nora_unstable_energy_trait
    nora_unstable_energy_trait = SerumTrait(name = "Unstable Energy Enhancer",
        desc = "A more carefully refined stimulant produces the same boost to baseline energy levels as ordinary caffeine, but with none of the unpleasant side effects.",
        positive_slug = "+(20-60) Max Energy\n+(1-3)Energy/Turn",
        negative_slug = "High Attention",
        research_added = 75,
        base_side_effect_chance = 100,
        on_turn = nora_unstable_energy_on_turn,
        on_apply = nora_unstable_energy_on_apply,
        on_remove = nora_unstable_energy_on_remove,
        tier = 1,
        research_needed = 500,
        clarity_cost = 300,
        exclude_tags = "Unstable",
        hidden_tag = "Energy",
        start_researched = True,
        mental_aspect = 4, physical_aspect = 4, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 3)
    # global nora_unstable_duration_trait       #This trait won't work with the way duration is currently calculated.
    # nora_unstable_duration_trait = SerumTrait(name = "Unstable Duration Enhancer",
    #     desc = "An unstable drug duration enhancer originally from another serum design company. Gets better with high mastery",
    #     positive_slug = "+(2-10) Turn Duration",
    #     negative_slug = "High Attention",
    #     research_added = 75,
    #     on_apply =
    #     base_side_effect_chance = 10,
    #     tier = 1,
    #     research_needed = 350,
    #     clarity_cost = 300,
    #     hidden_tag = "Duration",
    #     exclude_tags = "Unstable",
    #     start_researched = True,
    #     mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 0)

    # Unstable fertility enhancer?

def nora_unstable_serum_test():
    list_of_traits.append(nora_unstable_energy_trait)
    list_of_traits.append(nora_unstable_happiness_trait)
    list_of_traits.append(nora_unstable_love_trait)
    list_of_traits.append(nora_unstable_obedience_trait)
    list_of_traits.append(nora_unstable_slut_trait)
    return
