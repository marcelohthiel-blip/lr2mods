# Original idea by divas72

from __future__ import annotations
import copy
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod
from game.helper_functions.list_functions_ren import find_serum_trait_by_name
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.serums._serum_traits_T3_ren import mind_control_agent

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
list_of_instantiation_functions.append("init_amnesia_serum")

def amnesia_trait_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    # check if multiple selective amnesia traits are active
    active_amnesia_traits = sum(1 for s in person.serum_effects for t in s.traits if t.name == "Selective Amnesia")

    if active_amnesia_traits > 1 and mc.business.event_triggers_dict.get("enhanced_selective_amnesia", False):
        oldest_serum = min([s for s in person.serum_effects if "amnesia_count" in s.effects_dict], key = lambda x: f"{x.effects_dict.get('start_day', 9999)}-{x.effects_dict.get('start_turn', 9)}")
        serum.effects_dict = oldest_serum.effects_dict.copy()
    else:
        serum.effects_dict["start_day"] = day
        serum.effects_dict["start_turn"] = time_of_day
        serum.effects_dict["amnesia_count"] = active_amnesia_traits
        serum.effects_dict["love"] = person.love
        serum.effects_dict["obedience"] = person._obedience
        serum.effects_dict["happiness"] = person.happiness
        serum.effects_dict["sluttiness"] = person._sluttiness
        serum.effects_dict["pregnant"] = person.is_pregnant
        serum.effects_dict["broken_taboos"] = person.broken_taboos.copy()
        serum.effects_dict["opinions"] = copy.deepcopy(person.opinions)
        serum.effects_dict["sexy_opinions"] = copy.deepcopy(person.sexy_opinions)
        serum.effects_dict["sex_record"] = person.sex_record.copy()

    if active_amnesia_traits > 1 and not mc.business.event_triggers_dict.get("enhanced_selective_amnesia", False):
        mc.business.event_triggers_dict["trigger_amnesia_event"] = True

    if add_to_log:
        mc.log_event(f"{person.display_name}: now has selective amnesia", "float_text_red")

def amnesia_trait_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if mc.business.event_triggers_dict.get("trigger_amnesia_event", False) and not mc.business.event_triggers_dict.get("enhanced_selective_amnesia", True):
        active_amnesia_traits = sum(1 for s in person.serum_effects for t in s.traits if t.name == "Selective Amnesia")
        if active_amnesia_traits == 0 and not mc.business.mandatory_crises_list.has_action("amnesia_girl_crisis_label"):
            mc.business.add_mandatory_crisis(
                Action("Amnesia Trait Overload", amnesia_girl_crisis_requirement, "amnesia_girl_crisis_label",
                       args = person, requirement_args = [person]))

    person.love = serum.effects_dict["love"]
    person._obedience = serum.effects_dict["obedience"]
    person.happiness = serum.effects_dict["happiness"]
    person._sluttiness = serum.effects_dict["sluttiness"]
    person.broken_taboos = serum.effects_dict["broken_taboos"]
    person.opinions = serum.effects_dict["opinions"]
    person.sexy_opinions = serum.effects_dict["sexy_opinions"]
    person.sex_record = serum.effects_dict["sex_record"]
    if not serum.effects_dict.get("pregnant", True) and person.is_pregnant:
        person.event_triggers_dict["preg_mc_father"] = False
        if person.is_single:    # confused about getting pregnant (she uses condom with strangers)
            person.event_triggers_dict["immaculate_conception"] = True

    if add_to_log:
        if serum.effects_dict.get("amnesia_count", 0) == 0:
            mc.log_event(f"{person.display_name}: selective amnesia has faded", "float_text_red")
        else:
            mc.log_event(f"{person.display_name}: selective amnesia has partially faded", "float_text_red")

def amnesia_girl_crisis_requirement(person: Person):
    if person.is_family:
        return mc.is_home and person.is_at_mc_house
    if person.is_employee:
        return mc.is_at_office and person.is_at_office
    if person.is_strip_club_employee:
        return mc.is_at_stripclub and person.is_at_stripclub
    return not (mc.is_at_office or mc.is_home)

def amnesia_trait_crisis_requirement():
    trait = find_serum_trait_by_name("Selective Amnesia")
    return mc.is_at_office and time_of_day < 4 and trait and trait.mastery_level > 5.0

def init_amnesia_serum():
    SerumTraitMod(name = "Selective Amnesia",
        desc = "This trait blocks the person's ability to store experience from the short-term memory into the long-term memory, when the serum expires all primary stats and opinions will be restored to the values prior to taking the serum, including sex acts and how she got pregnant.",
        positive_slug = "Blocks memories",
        negative_slug = "Restores all major stats and opinions to the value before taking serum",
        research_added = 1000,
        base_side_effect_chance = 100,
        on_apply = amnesia_trait_on_apply,
        on_remove = amnesia_trait_on_remove,
        tier = 3,
        start_researched = False,
        requires = [mind_control_agent],
        research_needed = 2000,
        clarity_cost = 1500,
        hidden_tag = "Unique",
        mental_aspect = 7, physical_aspect = 1, sexual_aspect = 3, medical_aspect = 2, flaws_aspect = 0, attention = 5,
        start_enabled = True)

    mc.business.add_mandatory_crisis(
        Action("Enhance Amnesia Trait Crisis", amnesia_trait_crisis_requirement, "amnesia_trait_crisis_label"))
