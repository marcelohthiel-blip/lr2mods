from __future__ import annotations
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list
from game.game_roles._role_definitions_ren import hypno_orgasm_role, anal_fetish_role, cum_fetish_role
from game.sex_positions._position_definitions_ren import kissing, standing_finger, blowjob, missionary
from game.major_game_classes.serum_related.serums.fetish_serums_ren import is_anal_fetish_unlocked, is_cum_fetish_unlocked
from game.major_game_classes.character_related.Trainable_ren import Trainable
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import SerumTrait, foreplay_enhancer
from game.major_game_classes.serum_related.serums._serum_traits_T1_ren import oral_enhancer
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import vaginal_enhancer
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.personality_types._personality_definitions_ren import bimbo_personality

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

stat_trainables: list[Trainable] = []
skill_trainables: list[Trainable] = []
opinion_trainables: list[Trainable] = []
special_trainables: list[Trainable] = [] #Trainable put in this list are universal, and also displayed in the same list as Role specific trainables.

def train_intelligence_requirement(person: Person) -> bool:
    return person.personality != bimbo_personality

def train_focus_requirement(person: Person) -> bool:
    return person.personality != bimbo_personality

# Trainable definitions are defined here, the labels and requirements are separated off into their own file.
# STAT TRAINABLE #
sluttiness_trainable = Trainable("slut_train", "train_slut_label", "Increase Sluttiness", base_cost = 200)
stat_trainables.append(sluttiness_trainable)

obedience_trainable = Trainable("train_obedience", "train_obedience_label", "Increase Obedience", base_cost = 200)
stat_trainables.append(obedience_trainable)

love_trainable = Trainable("train_love", "train_love_label", "Increase Love", base_cost = 200)
stat_trainables.append(love_trainable)

suggest_trainable = Trainable("train_suggest", "train_suggest_label", "Increase Suggestibility", base_cost = 400)
stat_trainables.append(suggest_trainable)

charisma_trainable = Trainable("train_charisma", "train_charisma_label", "Increase Charisma", base_cost = 600)
stat_trainables.append(charisma_trainable)

intelligence_trainable = Trainable("train_intelligence", "train_intelligence_label", "Increase Intelligence", base_cost = 600, unlocked_function = train_intelligence_requirement)
stat_trainables.append(intelligence_trainable)

focus_trainable = Trainable("train_focus", "train_focus_label", "Increase Focus", base_cost = 600, unlocked_function = train_focus_requirement)
stat_trainables.append(focus_trainable)

# WORK SKILL TRAINABLE #
def train_work_requirement(person: Person):
    return person.is_employee

hr_trainable = Trainable("hr_train", "train_hr_label", "Increase HR Skill", unlocked_function = train_work_requirement)
skill_trainables.append(hr_trainable)

market_trainable = Trainable("market_train", "train_market_label", "Increase Marketing Skill", unlocked_function = train_work_requirement)
skill_trainables.append(market_trainable)

research_trainable = Trainable("research_train", "train_research_label", "Increase R&D Skill", unlocked_function = train_work_requirement)
skill_trainables.append(research_trainable)

production_trainable = Trainable("production_train", "train_production_label", "Increase Production Skill", unlocked_function = train_work_requirement)
skill_trainables.append(production_trainable)

supply_trainable = Trainable("supply_train", "train_supply_label", "Increase Supply Skill", unlocked_function = train_work_requirement)
skill_trainables.append(supply_trainable)

# SEX SKILL TRAINABLE #

def train_foreplay_requirement(person: Person):
    if person.has_taboo("touching_body"):
        return "Broken Touching Taboo"
    return True

def train_oral_requirement(person: Person):
    if person.has_taboo("sucking_cock"):
        return "Broken Blowjob Taboo"
    return True

def train_vaginal_requirement(person: Person):
    if person.has_taboo("vaginal_sex"):
        return "Broken Sex Taboo"
    return True

def train_anal_requirement(person: Person):
    if person.has_taboo("anal_sex"):
        return "Broken Anal Taboo"
    return True

foreplay_trainable = Trainable("foreplay_train", "train_foreplay_label", "Increase Foreplay Skill", unlocked_function = train_foreplay_requirement)
skill_trainables.append(foreplay_trainable)

oral_trainable = Trainable("oral_train", "train_oral_label", "Increase Oral Skill", base_cost = 200, unlocked_function = train_oral_requirement)
skill_trainables.append(oral_trainable)

vaginal_trainable = Trainable("vaginal_train", "train_vaginal_label", "Increase Vaginal Skill", base_cost = 300, unlocked_function = train_vaginal_requirement)
skill_trainables.append(vaginal_trainable)

anal_trainable = Trainable("anal_train", "train_anal_label", "Increase Anal Skill", base_cost = 400, unlocked_function = train_anal_requirement)
skill_trainables.append(anal_trainable)

# OPINION SKILL TRAINABLE #

def train_learn_opinion_requirement(person: Person):
    if person.has_unknown_opinions:
        return True
    return "Unknown Opinions"

def train_strengthen_opinion_requirement(person: Person):
    if person.get_opinion_topics_list(include_unknown = False, include_hate = False, include_love = False):
        return True
    return "Known Moderate Opinion"

def train_weaken_opinion_requirement(person: Person):
    if person.get_opinion_topics_list(include_unknown = False):
        return True
    return "Known Opinion"

learn_opinion_trainable = Trainable("learn_opinion_train", "train_learn_opinion_label", "Reveal a New Opinion", unlocked_function = train_learn_opinion_requirement)
opinion_trainables.append(learn_opinion_trainable)

strengthen_opinion_trainable = Trainable("strengthen_opinion_train", "train_strengthen_opinion_label", "Strengthen an Opinion", base_cost = 200, unlocked_function = train_strengthen_opinion_requirement, training_tag = "change_opinion")
opinion_trainables.append(strengthen_opinion_trainable)

weaken_opinion_trainable = Trainable("weaken_opinion_train", "train_weaken_opinion_label", "Weaken an Opinion", unlocked_function = train_weaken_opinion_requirement, training_tag = "change_opinion")
opinion_trainables.append(weaken_opinion_trainable)

new_normal_opinion_trainable = Trainable("new_normal_opinion_train", "train_new_opinion_label", "Inspire a New Normal Opinion", training_tag = "new_opinion")
opinion_trainables.append(new_normal_opinion_trainable)

new_sexy_opinion_trainable = Trainable("new_sexy_opinion_train", "train_new_opinion_label", "Inspire a New Sex Opinion", base_cost = 200, extra_args = True, training_tag = "new_opinion")
opinion_trainables.append(new_sexy_opinion_trainable)

# SPECIAL TRAINABLE #

def train_breeder_requirement(person: Person):
    if persistent.pregnancy_pref == 0 or person.is_infertile:
        return False
    if person.has_breeding_fetish or person.knows_pregnant:
        return False
    if person.on_birth_control and person.has_event_day("changed_bc") and not person.has_event_delay("changed_bc", 7):
        return "She started birth control too recently"
    if person.known_opinion.creampies < 2 or person.known_opinion.bareback_sex < 2:
        return "Loves Creampies and Bareback Sex"
    return True

def train_hypnotic_orgasm_requirement(person: Person):
    if person.has_role(hypno_orgasm_role):
        return False
    if person.suggestibility <= 50:
        return ">50% Suggestibility"
    if not person.is_in_very_heavy_trance:
        return "Very Deep Trance"
    return True

def train_online_attention_whore_requirement(person: Person):
    if person.instapic_known and person.dikdok_known and person.onlyfans_known:
        return False #No point doing it if she already has all three and you know about them.
    if person.known_opinion.showing_her_tits < 1 or person.known_opinion.showing_her_ass < 1 or person.known_opinion.skimpy_outfits < 1:
        return "Likes Showing her Tits, Ass, and Skimpy Outfits"
    return True

def train_dealbreaker_kissing_requirement(person: Person):
    if not person.known_opinion.kissing <= -2 or person.is_position_filtered(kissing):
        return False
    if person.sluttiness <= 20:
        return ">20 sluttiness"
    if mc.inventory.has_serum_with_trait(foreplay_enhancer):
        return True
    if person.has_broken_taboo("touching_body") or mc.foreplay_sex_skill > 4:
        return True
    return "Break touching taboo or foreplay skill > 4 or foreplay increasing serum in inventory"

def train_dealbreaker_fingering_requirement(person: Person):
    if not person.known_opinion.being_fingered <= -2 or person.is_position_filtered(standing_finger):
        return False
    if person.sluttiness <= 30:
        return ">30 sluttiness"
    if mc.inventory.has_serum_with_trait(foreplay_enhancer):
        return True
    if person.has_broken_taboo(["touching_penis", "touching_body", "touching_vagina"]):
        return True
    return "Break similar taboo or have foreplay increasing serum in inventory"

def train_dealbreaker_blowjob_requirement(person: Person):
    if not person.known_opinion.giving_blowjobs <= -2 or person.is_position_filtered(blowjob):
        return False
    if person.sluttiness <= 40:
        return ">40 sluttiness"
    if mc.inventory.has_serum_with_trait(oral_enhancer):
        return True
    if person.has_broken_taboo(["touching_penis", "sucking_cock", "licking_pussy"]):
        return True
    return "Break similar taboo or have oral increasing serum in inventory"

def train_dealbreaker_vaginal_sex_requirement(person: Person):
    if not person.known_opinion.vaginal_sex <= -2 or person.is_position_filtered(missionary):
        return False
    if person.sluttiness <= 50:
        return ">50 sluttiness"
    if mc.inventory.has_serum_with_trait(vaginal_enhancer):
        return True
    if person.has_broken_taboo(["licking_pussy", "anal_sex"]):
        return True
    return "Break cunnilingus or anal taboo or have vaginal sex enhancing serum in inventory"

def dealbreaker_give_enhancing_serum(person: Person, trait: SerumTrait):
    if not mc.inventory.has_serum_with_trait(trait):
        return False

    serum = get_random_from_list(mc.inventory.get_serums_with_trait(trait))
    if serum:
        renpy.say(None, f"You grab a {serum.name} and give it to {person.possessive_title}.")
        renpy.say(mc.name, "Here, drink this really quick. It will help.")

        mc.inventory.change_serum(serum, -1)
        person.give_serum(serum, add_to_log = True)
        return True
    return False

breeder_trainable = Trainable("breeder_train", "train_breeder_label", "Breeding Fascination", base_cost = 1500, unlocked_function = train_breeder_requirement)
special_trainables.append(breeder_trainable)

hypno_orgasm_trainable = Trainable("hypno_orgasm_train", "train_hypnotic_orgasm", "Trigger Word Orgasms", base_cost = 1000, unlocked_function = train_hypnotic_orgasm_requirement)
special_trainables.append(hypno_orgasm_trainable)

online_attention_whore_trainable = Trainable("online_attention_whore", "train_online_attention_whore", "Online Attention Whore", base_cost = 800, unlocked_function = train_online_attention_whore_requirement)
special_trainables.append(online_attention_whore_trainable) #RIght now this ensures she has all possible social media accounts. TODO: In the future we should expand on this some more, make this the intro to a longer storyline.

dealbreaker_kissing_trainable = Trainable("dealbreaker_kissing_train", "train_dealbreaker_kissing_label", "Ease Hated Opinion: Kissing", base_cost = 200, unlocked_function = train_dealbreaker_kissing_requirement)
special_trainables.append(dealbreaker_kissing_trainable)

dealbreaker_fingering_trainable = Trainable("dealbreaker_fingering_train", "train_dealbreaker_fingering_label", "Ease Hated Opinion: Fingering", base_cost = 200, unlocked_function = train_dealbreaker_fingering_requirement)
special_trainables.append(dealbreaker_fingering_trainable)

dealbreaker_blowjob_trainable = Trainable("dealbreaker_blowjob_train", "train_dealbreaker_blowjob_label", "Ease Hated Opinion: Blowjob", base_cost = 400, unlocked_function = train_dealbreaker_blowjob_requirement)
special_trainables.append(dealbreaker_blowjob_trainable)

dealbreaker_vaginal_sex_trainable = Trainable("dealbreaker_vaginal_sex_train", "train_dealbreaker_vaginal_sex_label", "Ease Hated Opinion: Vaginal Sex", base_cost = 200, unlocked_function = train_dealbreaker_vaginal_sex_requirement)
special_trainables.append(dealbreaker_vaginal_sex_trainable)

# These will be removed from normal opinion training list, because we have a special training for that
special_trainable_opinions = ("kissing", "being fingered", "giving blowjobs", "vaginal sex")

# FETISH TRAINABLE #

def train_anal_fetish_requirement(person: Person):
    if not is_anal_fetish_unlocked():
        return False
    if person.has_role(anal_fetish_role):
        return False
    if person.has_started_anal_fetish:
        return "Not started"
    if person.sluttiness < 50:
        return ">50 sluttiness"
    if person.opinion.anal_sex < 1 or person.opinion.anal_creampies < 1:
        return "Likes Anal Sex and Creampies"
    return True

def train_cum_fetish_requirement(person: Person):
    if not is_cum_fetish_unlocked():
        return False
    if person.has_role(cum_fetish_role):
        return False
    if person.has_started_cum_fetish:
        return "Not started"
    if person.sluttiness < 50:
        return ">50 sluttiness"
    return True


anal_fetish_trainable = Trainable("anal_fetish_train", "train_anal_fetish_label", "Anal Fetish", base_cost = 2000, unlocked_function = train_anal_fetish_requirement)
special_trainables.append(anal_fetish_trainable)

cum_fetish_trainable = Trainable("cum_fetish_train", "train_cum_fetish_label", "Cum Fetish", base_cost = 2000, unlocked_function = train_cum_fetish_requirement)
special_trainables.append(cum_fetish_trainable)
