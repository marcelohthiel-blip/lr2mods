from __future__ import annotations
import builtins
from game.bugfix_additions.ActionMod_ren import crisis_list, morning_crisis_list
from game.clothing_lists_ren import towel
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import bedroom
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, mc, erica, mom, lily, cousin
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe, mom_business_wardrobe
from game.people.Jennifer.jennifer_definition_ren import mom_secretary_job, mom_associate_job

TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def mom_outfit_help_requirement():
    return (time_of_day == 4
        and day % 7 in (0, 1, 2, 3, 6)      #It has to be a day before a weekday, so she has work in the morning.
        and not mom.is_sleeping
        and mc.is_home
        and mom.is_available
        and mom.has_job((mom_secretary_job, mom_associate_job))
        and mom_business_wardrobe.total_count < 12     # event stops occurring after she has 12 outfits in her business wardrobe
        and max(x.outfit_slut_score for x in mom_business_wardrobe) + 5 < mom.sluttiness)    # we don't have an outfit that matches her current slut level

def sister_helps_mom_with_next_day_outfit(mom, sister):
    mom.change_stats(slut = 1, max_slut = builtins.min(sister.effective_sluttiness(), 30))

    thinks_appropriate = False
    count = 0
    while not thinks_appropriate and count < 3:
        outfit = Wardrobe.generate_random_appropriate_outfit(sister, outfit_type = "full", opinion_color = sister.favourite_colour, allow_skimpy = sister.effective_sluttiness() > 30)
        thinks_appropriate = mom.judge_outfit(outfit)
        count += 1
    if thinks_appropriate and outfit:
        mom_business_wardrobe.add_outfit(outfit.get_copy())
        return outfit
    return None

crisis_list.append(
    Action("Mom Outfit Help Crisis ", mom_outfit_help_requirement, "mom_outfit_help_crisis_label"))


def mom_lingerie_surprise_requirement():
    return (time_of_day == 4
        and mom.energy > 50
        and mom.love > 40
        and mom.effective_sluttiness("underwear_nudity") > 40
        and mom.arousal_perc > 50
        and mc.is_at(bedroom))

crisis_list.append(
    Action("Mom Lingerie Surprise Crisis", mom_lingerie_surprise_requirement, "mom_lingerie_surprise_label"))


def mom_selfie_requirement():
    return (time_of_day in (1, 2, 3)
        and mom.love >= 15
        and mom.has_event_delay("last_phone_message", 5)
        and not mom.is_at_office    # she works for you
        and not mc.is_home
        and mom.is_available
        and mom not in mc.location.people)

crisis_list.append(
    Action("Mom Selfie Crisis", mom_selfie_requirement, "mom_selfie_label"))

def mom_morning_surprise_requirement():
    return (time_of_day == 0
        and mc.business.is_work_day
        and mom.love >= 45
        and mom.is_available
        and mc.is_at(bedroom)
        and not mom.is_sleeping)

morning_crisis_list.append(
    Action("Mom Morning Surprise", mom_morning_surprise_requirement, "mom_morning_surprise_label"))


def lily_new_underwear_requirement():
    return (lily.love >= 30
        and mc.is_in_bed
        and (not erica.event_triggers_dict.get("insta_pic_intro_complete", False) or day % 7 != 5)  # Erica visits on saturday nights (no new underwear event)
        and (not lily.has_taboo("underwear_nudity") or lily.effective_sluttiness("underwear_nudity") >= 20)
        and lily.wardrobe.underwear_sets     # we don't have underwear that matches her sluttiness level
        and max(x.underwear_slut_score for x in lily.wardrobe.underwear_sets) + 3 < (lily.sluttiness // 2))

def lily_new_underwear_get_underwear(person: Person):
    return Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under")

crisis_list.append(
    Action("Lily New Underwear Crisis", lily_new_underwear_requirement, "lily_new_underwear_crisis_label"))


def lily_morning_encounter_requirement():
    return (time_of_day == 0
        and day % 7 != 5        # not on saturday mornings
        and not lily.is_sleeping
        and lily.has_event_delay("morning_encounter", TIER_2_TIME_DELAY)
        and lily.is_available
        and mc.is_home)

morning_crisis_list.append(Action("Lily Morning Encounter", lily_morning_encounter_requirement, "lily_morning_encounter_label"))


def family_weekend_breakfast_requirement():
    return (time_of_day == 0
        and day % 7 == 6    # only on sunday
        and mom.love > 20
        and mc.is_home)

morning_crisis_list.append(
    Action("Family Morning Breakfast", family_weekend_breakfast_requirement, "family_morning_breakfast_label"))


def morning_shower_requirement():
    return (time_of_day == 0
        and day % 7 != 5    # not on saturdays
        and mc.is_home)

def apply_towel_outfit(person: Person, show_dress_sequence = False):
    towel_outfit = Outfit("Towel")
    towel_outfit.add_dress(towel.get_copy(), [.95, .95, .95, .95])
    person.apply_outfit(towel_outfit, show_dress_sequence = show_dress_sequence)

morning_crisis_list.append(
    Action("Morning Shower", morning_shower_requirement, "morning_shower_label"))


def cousin_tease_crisis_requirement():
    return (cousin.love < 30
        and cousin.obedience < 150
        and cousin.sluttiness > 20
        and mc.phone.has_number(cousin)
        and cousin.has_event_delay("cousin_text_tease", TIER_2_TIME_DELAY)
        and (not cousin.is_strip_club_employee or time_of_day < 3)
        and cousin not in mc.location.people)

crisis_list.append(
    Action("Cousin text tease", cousin_tease_crisis_requirement, "cousin_tease_crisis_label"))
