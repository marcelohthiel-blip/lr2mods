from __future__ import annotations
import builtins
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import get_random_from_list
from game.fetish.fetish_action_ren import Fetish_Action
from game.fetish.fetish_serum_quests_ren import add_fetish_serum_anal_warning, add_fetish_serum_breeding_warning, add_fetish_serum_cum_warning
from game.bugfix_additions.SerumTraitMod_ren import SerumTraitMod, SerumTrait
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, lily, mom, aunt, starbuck, stephanie, erica, candace, sarah, myra
from game.major_game_classes.game_logic.Room_ren import lily_bedroom, aunt_apartment, gym
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.sex_positions._position_definitions_ren import missionary, doggy_anal
from game.people.Erica.erica_role_definition_ren import erica_get_progress, erica_has_given_morning_handjob
from game.people.Ellie.IT_Nanobot_Projects_ren import anal_fetish_increase_project, breeder_fetish_increase_project, cum_fetish_increase_project, exhibition_fetish_increase_project
from game.people.Myrabelle.myra_role_definition_ren import myra_lewd_game_fuck_avail
from game.people.Sarah.sarah_definition_ren import sarah_threesomes_unlocked
from game.people.Starbuck.starbuck_role_definition_ren import get_shop_investment_rate, sex_shop_stage
from game.trainables._trainables_ren import special_trainable_opinions

list_of_traits: list[SerumTrait] = []
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
FETISH_BASIC_OPINION_LIST = ["giving handjobs", "giving tit fucks", "being fingered", "kissing", "masturbating", "big dicks", "getting head", "lingerie"]
FETISH_ANAL_OPINION_LIST = ["anal sex", "doggy style sex", "anal creampies", "showing her ass"]
FETISH_CUM_OPINION_LIST = ["being covered in cum", "drinking cum", "cum facials", "giving blowjobs", "anal creampies", "creampies"]
FETISH_BREEDING_OPINION_LIST = ["bareback sex", "vaginal sex", "creampies", "missionary style sex"]
FETISH_EXHIBITION_OPINION_LIST = ["public sex", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "skimpy outfits", "skimpy uniforms", "high heels"]
FETISH_RESEARCH_ADDED = 300     #Research Difficulty
FETISH_PRODUCTION_COST = 100    #Production Difficulty
FETISH_SERUM_ATTENTION = 3      #Attention stat. Can be reduced via IT procedures
FETISH_SERUM_TRIGGER_VALUE = 20


def fetish_serum_unlock_count():
    return mc.business.event_triggers_dict.get("fetish_serum_count", 0)

def is_anal_fetish_unlocked():
    return mc.business.event_triggers_dict.get("anal_serum_warn", False)

def is_cum_fetish_unlocked():
    return mc.business.event_triggers_dict.get("cum_serum_warn", False)

def is_breeding_fetish_unlocked():
    return mc.business.event_triggers_dict.get("breeding_serum_warn", False)

def is_exhibition_fetish_unlocked():
    return mc.business.event_triggers_dict.get("exhibition_serum_warn", False)

def anal_fetish_employee_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office

def anal_fetish_family_intro_requirement(person: Person):
    return person.is_home and person.location.person_count == 1

def anal_fetish_generic_intro_requirement(person: Person):
    return not person.is_home and person.is_available

def anal_fetish_mom_intro_requirement():
    return mc.is_in_bed and mc.energy > 80 and mom.is_available

def anal_fetish_lily_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office and lily.is_available

def anal_fetish_rebecca_intro_requirement():
    return False

def anal_fetish_gabrielle_intro_requirement():
    return False

def anal_fetish_stephanie_intro_requirement():
    if mc.business.is_open_for_business and mc.is_at_office and renpy.random.randint(0, 100) < 20:
        return stephanie.is_available
    return False

def anal_fetish_alex_intro_requirement():
    return False

def anal_fetish_nora_intro_requirement():
    return False

def anal_fetish_emily_intro_requirement():
    return False

def anal_fetish_christina_intro_requirement():
    return False

def anal_fetish_starbuck_intro_requirement():
    return time_of_day == 3 and mc.is_at_office and starbuck.is_available

def anal_fetish_sarah_intro_requirement():
    return False

def anal_fetish_ophelia_intro_requirement():
    return False

def anal_fetish_candace_intro_requirement():
    return False

def anal_fetish_dawn_intro_requirement():
    return False

def anal_fetish_erica_intro_requirement():
    return day % 7 == 6 and erica.is_available

def anal_fetish_ashley_intro_requirement():
    return False

def anal_fetish_kaya_intro_requirement():
    return False

def anal_fetish_ellie_intro_requirement():
    return False

def anal_fetish_camila_intro_requirement():
    return False

def anal_fetish_sakari_intro_requirement():
    return False

def anal_fetish_myra_intro_requirement():
    return False

def start_anal_fetish_quest(person: Person):
    if not is_anal_fetish_unlocked() \
            or person.has_started_anal_fetish \
            or person.has_taboo("anal_sex"):
        return False

    if person.opinion.anal_sex < 2 \
            or person.anal_sex_skill < 4 \
            or not person.is_willing(doggy_anal) \
            or person.sluttiness < 70:
        return False

    if person == mom and not mom.event_triggers_dict.get("anal_revisit_complete", False):
        return False
    if person == lily and not lily.event_triggers_dict.get("anal_revisit_complete", False):
        return False

    # chance to start the anal fetish quest
    if not mc.business.IT_project_is_active(anal_fetish_increase_project):
        if renpy.random.randint(0, 100) > fetish_serum_roll_fetish_chance(FETISH_ANAL_OPINION_LIST, person) and not person.is_in_very_heavy_trance:
            return False

    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("anal_fetish_locked"):
        return False

    person.set_event_day("anal_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == lily:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Lily Anal Fetish Intro", anal_fetish_lily_intro_requirement, "anal_fetish_lily_intro_label", fetish_type = "anal")
        )
        return True
    if person == mom:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Jennifer Anal Fetish Intro", anal_fetish_mom_intro_requirement, "anal_fetish_mom_intro_label", fetish_type = "anal")
        )
        return True
    if person == starbuck:
        if get_shop_investment_rate() >= 6.0:
            mc.business.add_mandatory_crisis(
                Fetish_Action("Starbuck Anal Fetish Intro", anal_fetish_starbuck_intro_requirement, "anal_fetish_starbuck_intro_label", fetish_type = "anal")
            )
            return True
        return False
    if person == stephanie:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Stephanie Anal Fetish Intro", anal_fetish_stephanie_intro_requirement, "anal_fetish_stephanie_intro_label", fetish_type = "anal")
        )
        return True
    # elif person == emily and False:
    #     pass
    # elif person == christina and False:
    #     pass
    # elif person == sarah and False:
    #     pass
    # elif person == salon_manager and False:
    #     pass
    if person == erica:
        if erica_has_given_morning_handjob():
            mc.business.add_mandatory_morning_crisis(
                Fetish_Action("Erica Anal Fetish Intro", anal_fetish_erica_intro_requirement, "anal_fetish_erica_intro_label", fetish_type = "anal")
            )
            return True
        return False
    # if person == candace and False:
    #     pass
    # elif person == ashley and False:
    #     pass
    # elif person == alexia and False:
    #     pass
    # elif person == kaya and False:
    #     pass
    # elif person == ellie and False:
    #     pass
    # elif person == camila and False:
    #     pass
    # elif person == sakari and False:
    #     pass
    # if person == myra:
    #     Fetish_Action("Myra Anal Fetish Intro", anal_fetish_myra_intro_requirement, "anal_fetish_myra_intro_label", fetish_type = "anal")
    if person.is_employee:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee Anal Fetish Intro", anal_fetish_employee_intro_requirement, "anal_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "anal")
        )
        return True
    if person.is_family:
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Anal Fetish Intro", anal_fetish_family_intro_requirement, "anal_fetish_family_intro_label", fetish_type = "anal", priority = 30)
        )
        return True

    person.add_unique_on_talk_event(
        Fetish_Action("Generic Anal Fetish Intro", anal_fetish_generic_intro_requirement, "anal_fetish_generic_intro_label", fetish_type = "anal")
    )
    return True

def breeding_fetish_employee_intro_requirement():
    return (
        time_of_day == 3
        and mc.business.is_open_for_business
        and mc.is_at_office
    )

def breeding_fetish_generic_intro_requirement(person: Person):
    return (
        person.is_available
        and not person.is_home
    )

def breeding_fetish_family_intro_requirement(person: Person):
    return (
        time_of_day >= 3
        and person.is_home
        and person.location.person_count == 1
    )
    if person.is_home and person.location.person_count == 1 and time_of_day >= 3: #She is alone in her bedroom
        return True
    return False

def breeding_fetish_mom_intro_requirement(): #TODO this should be a morning mandatory crisis event.
    return True #??? Is this right?

def breeding_fetish_lily_intro_requirement(person: Person):
    return lily.is_home and lily.location.person_count == 1

def breeding_fetish_rebecca_intro_requirement():
    return False

def breeding_fetish_gabrielle_intro_requirement():
    return False

def breeding_fetish_stephanie_intro_requirement():
    if mc.business.is_open_for_business and stephanie.is_at_work and renpy.random.randint(0, 100) < 25:
        return True
    return False

def breeding_fetish_emily_intro_requirement():
    return False

def breeding_fetish_christina_intro_requirement():
    return False

def breeding_fetish_starbuck_intro_requirement():
    return time_of_day == 3 and sex_shop_stage() > 0 and starbuck.is_available

def breeding_fetish_sarah_intro_requirement():
    return day % 7 != 5 and mc.is_in_bed and sarah_threesomes_unlocked() and sarah.is_available

def breeding_fetish_ophelia_intro_requirement():
    return False

def breeding_fetish_erica_intro_requirement():
    return mc.is_in_bed and day % 7 != 6 and erica.is_available and not erica.on_birth_control

def breeding_fetish_erica_unsuccessful_followup_requirement():
    return True

def breeding_fetish_candace_intro_requirement(person: Person):
    return candace.is_at_work and mc.is_at_office and candace.is_available

def breeding_fetish_ashley_intro_requirement():
    return False

def breeding_fetish_kaya_intro_requirement():
    return False

def breeding_fetish_ellie_intro_requirement():
    return False

def breeding_fetish_camila_intro_requirement():
    return False

def breeding_fetish_sakari_intro_requirement():
    return False

def breeding_fetish_myra_intro_requirement():
    return time_of_day == 4 and mc.energy > 80 and myra.energy > 80 and myra.is_available

def start_breeding_fetish_quest(person: Person):
    #Determine who it is, then add the appropriate quest.
    if persistent.pregnancy_pref == 0 \
            or not is_breeding_fetish_unlocked() \
            or person.has_started_breeding_fetish \
            or person.has_taboo(["condomless_sex", "vaginal_sex"]):
        return False

    if person.opinion.bareback_sex < 2 \
            or person.vaginal_sex_skill < 4 \
            or not person.is_willing(missionary) \
            or person.sluttiness < 70:
        return False

    if person == mom and not mom.event_triggers_dict.get("vaginal_revisit_complete", False):
        return False
    if person == lily and not lily.event_triggers_dict.get("vaginal_revisit_complete", False):
        return False

    # chance to start the breeding fetish quest
    if not mc.business.IT_project_is_active(breeder_fetish_increase_project):
        if renpy.random.randint(0, 100) > fetish_serum_roll_fetish_chance(FETISH_BREEDING_OPINION_LIST, person) and not person.is_in_very_heavy_trance:
            return False

    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("breeding_fetish_locked"):
        return False

    if person.on_birth_control and person.has_event_day("changed_bc") and not person.has_event_delay("changed_bc", 7):
        return False  # lock her out of breeding fetish for first 7 days after starting BC

    person.set_event_day("breeding_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == mom:
        mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Mom breeding fetish intro", breeding_fetish_mom_intro_requirement, "breeding_fetish_mom_intro_label", fetish_type = "breeding")
        )
        return True
    if person == lily:
        lily.add_unique_on_room_enter_event(
            Fetish_Action("Lily breeding fetish intro", breeding_fetish_lily_intro_requirement, "breeding_fetish_lily_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    # if person == aunt:
    #     Fetish_Action("Rebecca breeding fetish intro", breeding_fetish_rebecca_intro_requirement, "breeding_fetish_rebecca_intro_label", fetish_type = "breeding")
    # elif person == cousin:
    #     Fetish_Action("Gabrielle breeding fetish intro", breeding_fetish_gabrielle_intro_requirement, "breeding_fetish_gabrielle_intro_label", fetish_type = "breeding")
    if person == stephanie:
        mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Stephanie breeding fetish intro", breeding_fetish_stephanie_intro_requirement, "breeding_fetish_stephanie_intro_label", fetish_type = "breeding")
        )
        return True
    # elif person == emily:
    #     Fetish_Action("Emily breeding fetish intro", breeding_fetish_emily_intro_requirement, "breeding_fetish_emily_intro_label", fetish_type = "breeding")
    # elif person == christina:
    #     Fetish_Action("Christina breeding fetish intro", breeding_fetish_christina_intro_requirement, "breeding_fetish_christina_intro_label", fetish_type = "breeding")
    if person == starbuck:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Starbuck breeding fetish intro", breeding_fetish_starbuck_intro_requirement, "breeding_fetish_starbuck_intro_label", fetish_type = "breeding")
        )
        return True
    if person == sarah:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Sarah breeding fetish intro", breeding_fetish_sarah_intro_requirement, "breeding_fetish_sarah_intro_label", fetish_type = "breeding")
        )
        return True
    # elif person is salon_manager and False:
    #     Fetish_Action("Ophelia breeding fetish intro", breeding_fetish_ophelia_intro_requirement, "breeding_fetish_ophelia_intro_label", fetish_type = "breeding")
    if person == erica:
        if erica_get_progress() >= 4:
            mc.business.add_mandatory_crisis(
                Fetish_Action("Erica breeding fetish intro", breeding_fetish_erica_intro_requirement, "breeding_fetish_erica_intro_label", fetish_type = "breeding")
            )
            return True
        return False
    if person == candace:
        candace.add_unique_on_room_enter_event(
            Fetish_Action("Candace breeding fetish intro", breeding_fetish_candace_intro_requirement, "breeding_fetish_candace_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    # elif person == ashley:
    #     Fetish_Action("Ashley breeding fetish intro", breeding_fetish_ashley_intro_requirement, "breeding_fetish_ashley_intro_label", fetish_type = "breeding")
    # elif person == alexia:
    #     pass
    # elif person == kaya:
    #     pass
    # elif person == ellie:
    #     pass
    # elif person == camila:
    #     pass
    # elif person == sakari:
    #     pass
    if person == myra:
        if myra_lewd_game_fuck_avail():
            mc.business.add_mandatory_crisis(
                Fetish_Action("Myra Breeding Fetish Intro", breeding_fetish_myra_intro_requirement, "breeding_fetish_myra_intro_label", fetish_type = "breeding")
            )
            return True
        return False
    if person.is_employee:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee breeding fetish intro", breeding_fetish_employee_intro_requirement, "breeding_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "breeding")
        )
        return True
    if person.is_family:
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Member breeding fetish intro", breeding_fetish_family_intro_requirement, "breeding_fetish_family_intro_label", fetish_type = "breeding", priority = 30)
        )
        return True
    person.add_unique_on_talk_event(
        Fetish_Action("Non Employee breeding fetish intro", breeding_fetish_generic_intro_requirement, "breeding_fetish_generic_intro_label", fetish_type = "breeding")
    )
    return True

def cum_fetish_employee_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office

def cum_fetish_family_intro_requirement(person: Person):
    return person.is_home and person.location.person_count == 1

def cum_fetish_generic_intro_requirement():
    return mc.is_in_bed and mc.energy > 70

def cum_fetish_mom_intro_requirement():
    return mc.is_in_bed and mc.energy > 70 and mom.is_available

def cum_fetish_lily_intro_requirement():
    return day % 7 != 5 and mc.is_home and lily.is_available

def cum_fetish_rebecca_intro_requirement(person: Person):
    return time_of_day == 3 and mc.energy > 70 and person in aunt_apartment.people

def cum_fetish_gabrielle_intro_requirement():
    return False

def cum_fetish_stephanie_intro_requirement():
    return False

def cum_fetish_alex_intro_requirement():
    return False

def cum_fetish_nora_intro_requirement():
    return False

def cum_fetish_emily_intro_requirement():
    return False

def cum_fetish_christina_intro_requirement():
    return False

def cum_fetish_starbuck_intro_requirement():
    return False

def cum_fetish_sarah_intro_requirement():
    if time_of_day == 2 and day % 7 != 0:
        return mc.is_at_office and mc.business.is_open_for_business and sarah.is_at_work and sarah.is_available
    return False

def cum_fetish_ophelia_intro_requirement():
    return False

def cum_fetish_candace_intro_requirement():
    return False

def cum_fetish_dawn_intro_requirement():
    return False

def cum_fetish_erica_intro_requirement(person: Person):
    return person.is_at(gym) and person.energy >= 80 and mc.energy >= 80 and person.is_available

def cum_fetish_ashley_intro_requirement():
    return False

def cum_fetish_kaya_intro_requirement():
    return False

def cum_fetish_ellie_intro_requirement():
    return False

def cum_fetish_camila_intro_requirement():
    return False

def cum_fetish_sakari_intro_requirement():
    return False

def cum_fetish_myra_intro_requirement(person: Person):
    return False


def start_cum_fetish_quest(person: Person):
    if not is_cum_fetish_unlocked() \
            or person.has_started_cum_fetish \
            or person.has_taboo(["sucking_cock", "condomless_sex"]):
        return False

    if person.opinion.being_covered_in_cum < 2 \
            or person.oral_sex_skill < 4 \
            or person.sluttiness < 70:
        return False

    # chance to start the cum fetish quest
    if not mc.business.IT_project_is_active(cum_fetish_increase_project):
        if renpy.random.randint(0, 100) > fetish_serum_roll_fetish_chance(FETISH_CUM_OPINION_LIST, person) and not person.is_in_very_heavy_trance:
            return False

    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("cum_fetish_locked"):
        return False

    person.set_event_day("cum_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    if person == lily:
        mc.business.add_mandatory_morning_crisis(
            Fetish_Action("Lily Cum Fetish Intro", cum_fetish_lily_intro_requirement, "cum_fetish_lily_intro_label", fetish_type = "cum")
        )
        return True
    if person == mom:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Jennifer Cum Fetish Intro", cum_fetish_mom_intro_requirement, "cum_fetish_mom_intro_label", fetish_type = "cum")
        )
        return True
    if person == aunt:
        person.add_unique_on_room_enter_event(
            Fetish_Action("Rebecca Cum Fetish Intro", cum_fetish_rebecca_intro_requirement, "cum_fetish_rebecca_intro_label", fetish_type = "cum", priority = 30)
        )
        return True
    # elif person is stephanie and person.has_role(head_researcher) and person.personality != bimbo_personality and False:
    #     pass
    if person == sarah:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Sarah Cum Fetish Intro", cum_fetish_sarah_intro_requirement, "cum_fetish_sarah_intro_label", fetish_type = "cum")
        )
        return True
    if person == erica:
        if erica_get_progress() >= 4:
            erica.add_unique_on_room_enter_event(
                Fetish_Action("Erica Cum Fetish Intro", cum_fetish_erica_intro_requirement, "cum_fetish_erica_intro_label", fetish_type = "cum", priority = 30)
            )
            return True
        return False
    # if person == myra:
    #     myra.add_unique_on_room_enter_event(
    #         cum_fetish_myra_intro = Fetish_Action("Myra Cum Fetish Intro", cum_fetish_myra_intro_requirement, "cum_fetish_myra_intro_label", fetish_type = "cum")
    #     )
    #     return True
    # elif person is kaya and False:
    #     pass
    # elif person is ellie and False:
    #     pass
    # elif person is camila and False:
    #     pass
    # elif person is sakari and False:
    #     pass
    if person.is_employee:
        mc.business.add_mandatory_crisis(
            Fetish_Action("Employee cum fetish intro", cum_fetish_employee_intro_requirement, "cum_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "cum")
        )
        return True
    if person.is_family:
        person.add_unique_on_room_enter_event(
            Fetish_Action("Family Cum Fetish Intro", cum_fetish_family_intro_requirement, "cum_fetish_family_intro_label", fetish_type = "cum", priority = 30)
        )
        return True

    mc.business.add_mandatory_crisis(
        Fetish_Action("Someone needs cum", cum_fetish_generic_intro_requirement, "cum_fetish_generic_intro_label", args = person, priority = 10, fetish_type = "cum")
    )
    return True


def exhibition_fetish_employee_intro_requirement():
    return time_of_day == 3 and mc.business.is_open_for_business and mc.is_at_office

def exhibition_fetish_family_intro_requirement(person: Person):
    return person.is_home and person.location.person_count == 1 #She is alone in her bedroom

def exhibition_fetish_generic_intro_requirement(person: Person):
    return not person.is_home

def exhibition_fetish_mom_intro_requirement():
    return False

def exhibition_fetish_lily_intro_requirement():
    return False

def exhibition_fetish_rebecca_intro_requirement():
    return False

def exhibition_fetish_gabrielle_intro_requirement():
    return False

def exhibition_fetish_stephanie_intro_requirement():
    return False

def exhibition_fetish_alex_intro_requirement():
    return False

def exhibition_fetish_nora_intro_requirement():
    return False

def exhibition_fetish_emily_intro_requirement():
    return False

def exhibition_fetish_christina_intro_requirement():
    return False

def exhibition_fetish_starbuck_intro_requirement():
    return False

def exhibition_fetish_sarah_intro_requirement():
    return False

def exhibition_fetish_ophelia_intro_requirement():
    return False

def exhibition_fetish_candace_intro_requirement():
    return False

def exhibition_fetish_dawn_intro_requirement():
    return False

def exhibition_fetish_erica_intro_requirement():
    return False

def exhibition_fetish_ashley_intro_requirement():
    return False

def exhibition_fetish_myra_intro_requirement():
    return False

def start_exhibition_fetish_quest(person: Person):
    if not is_exhibition_fetish_unlocked():
        return False
    if person.has_started_exhibition_fetish:
        return False
    if person.has_taboo(["sucking_cock", "vaginal_sex"]):
        return False

    if person.opinion.public_sex < 2 \
            or person.oral_sex_skill < 4 \
            or person.vaginal_sex_skill < 4 \
            or person.anal_sex_skill < 4 \
            or person.sluttiness < 70:
        return False

    # when blocking the fetish gain, prevent repeat triggering for a while
    if day < person.get_event_day("exhibition_fetish_locked"):
        return False

    person.set_event_day("exhibition_fetish_locked", day + renpy.random.randint(5, 7) + person.opinion.being_submissive - person.opinion.taking_control)

    # if person == myra:
    #     Fetish_Action("Myra Exhibitionism Fetish Intro", exhibition_fetish_myra_intro_requirement, "exhibition_fetish_myra_intro_label", fetish_type = "exhibition")

    if not mc.business.IT_project_is_active(exhibition_fetish_increase_project):
        if renpy.random.randint(0, 100) > fetish_serum_roll_fetish_chance(FETISH_EXHIBITION_OPINION_LIST, person) and not person.is_in_very_heavy_trance():
            return False

    return False #None of them are written yet

def fetish_serum_increase_opinion(opinion_list: list[str], max_value: int, person: Person): #WE purposefully increase a score EVERY time this function is used instead of RNG
    avail_opinions = [x for x in opinion_list if person.opinion(x) < max_value]
    if avail_opinions:
        for x in range(-2, max_value):
            lowest_opinions = [y for y in avail_opinions if person.opinion(y) == x]
            if x == -2: # exclude these opinions from auto increase from hate -> force ease hated opinion training
                lowest_opinions = [x for x in lowest_opinions if x not in special_trainable_opinions]
            if lowest_opinions:
                person.increase_opinion_score(get_random_from_list(lowest_opinions), max_value, True)
                break
        return True #Return true if we increased an opinion
    return False

def fetish_serum_increase_obedience(person: Person, add_to_log: bool = False):
    # slowly increase obedience (max 180)
    if person.obedience_tier >= 5:
        return
    if (renpy.random.randint(0, 100) <
            10 + (1 + person.suggest_tier - person.obedience_tier) * 5
            + (person.opinion.being_submissive * 5)
            - (person.opinion.taking_control * 5)):
        person.change_obedience(1, add_to_log = add_to_log)

def fetish_serum_increase_sluttiness(person: Person, add_to_log: bool = False):
    # slowly increase slut (up to max 90)
    if person.sluttiness > 90:
        return
    if renpy.random.randint(0, 100) < person.suggestibility - person.sluttiness:
        person.change_slut(1, add_to_log = add_to_log)

def fetish_serum_calculate_completion(person: Person, serum_tag: str):
    counter = person.event_triggers_dict.get(serum_tag, 0)
    return builtins.round((counter / float(FETISH_SERUM_TRIGGER_VALUE)) * 100, 1)

def fetish_serum_increase_counter(person: Person, serum_tag: str):
    person.event_triggers_dict[serum_tag] = person.event_triggers_dict.get(serum_tag, 0) + person.suggest_tier + 1

def fetish_serum_roll_fetish_chance(opinion_list, person: Person):
    fetish_odds = person.suggest_tier * 15 #Up to 60 points based on suggestibility
    opinion_modifier = (person.opinion(opinion_list) * 10) / builtins.len(opinion_list)
    return fetish_odds + builtins.int(opinion_modifier)

def body_monitor_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    updated_traits = [trait.add_mastery(.1) for serum in person.serum_effects for trait in serum.traits]
    if any(updated_traits) and add_to_log:
        mc.log_event(f"Remotely monitored {person.display_name}", "float_text_blue")

def body_monitor_on_day(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.max_energy < 160:
        person.change_max_energy(1, add_to_log = add_to_log)

def fetish_basic_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.event_triggers_dict["nano_bots_f"] = False

def fetish_basic_function_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.event_triggers_dict.get("nano_bots_f", False): # no trigger, report progress
        mc.log_event(f"{person.display_name} sexual proclivity bots: {fetish_serum_calculate_completion(person, 'nano_bots_fc')}%", "float_text_blue")

def fetish_basic_function_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.event_triggers_dict.get("nano_bots_f", False):
        return # this fetish already triggered (prevents stacking multiple basic fetish serums)

    fetish_serum_increase_counter(person, "nano_bots_fc")

    # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
    if person.event_triggers_dict.get("nano_bots_fc", 0) < FETISH_SERUM_TRIGGER_VALUE:
        return

    person.event_triggers_dict["nano_bots_fc"] = 0 # reset counter
    person.event_triggers_dict["nano_bots_f"] = True # block any effect for this dose

    tier = person.suggest_tier
    if renpy.random.randint(0, 100) < 10 + (tier * 5): # only chance to increase skill
        person.increase_sex_skill("Foreplay", 2 + tier, add_to_log = True)

    if not fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, tier - 1, person):
        mc.log_event(f"{person.display_name} sexual proclivity bots no longer effective at {person.suggestibility}% suggestibility.", "float_text_blue")

def fetish_anal_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.event_triggers_dict["nano_bots_a"] = False

def fetish_anal_function_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.event_triggers_dict.get("nano_bots_a", False): # no trigger, report progress
        mc.log_event(f"{person.display_name} anal proclivity Bots: {fetish_serum_calculate_completion(person, 'nano_bots_ac')}%", "float_text_blue")

def fetish_anal_function_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.event_triggers_dict.get("nano_bots_a", False):
        return # this fetish already triggered (prevents stacking multiple basic fetish serums)

    fetish_serum_increase_counter(person, "nano_bots_ac")

    # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
    if person.event_triggers_dict.get("nano_bots_ac", 0) < FETISH_SERUM_TRIGGER_VALUE:
        return

    person.event_triggers_dict["nano_bots_ac"] = 0 # reset counter
    person.event_triggers_dict["nano_bots_a"] = True # block any effect for this dose

    fetish_serum_increase_obedience(person, add_to_log = add_to_log)

    tier = person.suggest_tier
    if renpy.random.randint(0, 100) < 10 + (tier * 5): # only chance to increase skill
        person.increase_sex_skill("Anal", 2 + tier, add_to_log = True)

    if not fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, tier - 1, person):
        if person.anal_sex_skill < 2 + tier:
            person.increase_sex_skill("Anal", 2 + tier, add_to_log = True)
        else:
            mc.log_event(f"{person.display_name} anal proclivity bots reduced effectiveness at {person.suggestibility}% suggestibility.", "float_text_blue")

    if start_anal_fetish_quest(person):
        person.event_triggers_dict["anal_fetish_start"] = True
        #TODO some kind of test here to indicate to the player that their anal quest has started

def fetish_breeding_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.event_triggers_dict["nano_bots_b"] = False

def fetish_breeding_function_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.event_triggers_dict.get("nano_bots_b", False): # no trigger, report progress
        mc.log_event(f"{person.display_name} reproduction proclivity bots: {fetish_serum_calculate_completion(person, 'nano_bots_bc')}%", "float_text_blue")

def fetish_breeding_function_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.event_triggers_dict.get("nano_bots_b", False):
        return # this fetish already triggered (prevents stacking multiple basic fetish serums)

    fetish_serum_increase_counter(person, "nano_bots_bc")
    person.change_baby_desire(1)

    # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
    if person.event_triggers_dict.get("nano_bots_bc", 0) < FETISH_SERUM_TRIGGER_VALUE:
        return

    person.event_triggers_dict["nano_bots_bc"] = 0 # reset counter
    person.event_triggers_dict["nano_bots_b"] = True # block any effect for this dose

    tier = person.suggest_tier
    if renpy.random.randint(0, 100) < 10 + (tier * 5):
        person.increase_sex_skill("Vaginal", 2 + tier, add_to_log = True)
    if renpy.random.randint(0, 100) < (person.suggestibility - (person.happiness - 100)) * 3:
        person.change_happiness(1, add_to_log = True)

    if not fetish_serum_increase_opinion(FETISH_BREEDING_OPINION_LIST, tier - 1, person):
        if person.vaginal_sex_skill < 2 + tier:
            person.increase_sex_skill("Vaginal", 2 + tier, add_to_log = True)
        else:
            mc.log_event(f"{person.display_name} reproduction proclivity bots reduced effectiveness at {person.suggestibility}% suggestibility.", "float_text_blue")

    if persistent.pregnancy_pref == 0:  # pregnancy is disabled, so don't run rest of function
        return

    # going off birth-control
    if fetish_serum_roll_fetish_chance(FETISH_BREEDING_OPINION_LIST, person) >= 50:
        add_breeding_fetish_going_off_BC_action(person)

    if start_breeding_fetish_quest(person):
        person.event_triggers_dict["breeding_fetish_start"] = True
        person.on_birth_control = False
        #TODO some kind of test here to indicate to the player that their breeding quest has started

def breeding_fetish_going_off_BC_requirement(person: Person):
    return (
        person.on_birth_control
        and not person.is_infertile
        and not person.event_triggers_dict.get("is_changing_birth_control", False)
    )

def add_breeding_fetish_going_off_BC_action(person: Person):
    if person.has_queued_event("breeding_fetish_going_off_BC_label"):
        return # don't add if already queued
    breeding_fetish_going_off_BC = Action("She goes off BC", breeding_fetish_going_off_BC_requirement, "breeding_fetish_going_off_BC_label")
    person.add_unique_on_talk_event(breeding_fetish_going_off_BC)

def fetish_cum_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.event_triggers_dict["nano_bots_c"] = False

def fetish_cum_function_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.event_triggers_dict.get("nano_bots_c", False): # no trigger, report progress
        mc.log_event(f"{person.display_name} semen proclivity bots: {fetish_serum_calculate_completion(person, 'nano_bots_cc')}%", "float_text_blue")

def fetish_cum_function_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.event_triggers_dict.get("nano_bots_c", False):
        return # this fetish already triggered (prevents stacking multiple basic fetish serums)

    fetish_serum_increase_counter(person, "nano_bots_cc")

    # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
    if person.event_triggers_dict.get("nano_bots_cc", 0) < FETISH_SERUM_TRIGGER_VALUE:
        return

    person.event_triggers_dict["nano_bots_cc"] = 0 # reset counter
    person.event_triggers_dict["nano_bots_c"] = True # block any effect for this dose

    fetish_serum_increase_sluttiness(person, add_to_log = add_to_log)

    tier = person.suggest_tier
    if renpy.random.randint(0, 100) < 10 + (tier * 5): # only chance to increase skill
        person.increase_sex_skill("Oral", 2 + tier, add_to_log = True)

    if not fetish_serum_increase_opinion(FETISH_CUM_OPINION_LIST, tier - 1, person):
        if person.oral_sex_skill < 2 + tier:
            person.increase_sex_skill("Oral", 2 + tier, add_to_log = True)
        else:
            mc.log_event(f"{person.display_name} semen proclivity bots reduced effectiveness at {person.suggestibility}% suggestibility.", "float_text_blue")

    if start_cum_fetish_quest(person):
        person.event_triggers_dict["cum_fetish_start"] = True
        #TODO some kind of test here to indicate to the player that their cum quest has started

def fetish_exhibition_function_on_apply(person: Person, serum: SerumDesign, add_to_log: bool):
    person.event_triggers_dict["nano_bots_e"] = False

def fetish_exhibition_function_on_remove(person: Person, serum: SerumDesign, add_to_log: bool):
    if not person.event_triggers_dict.get("nano_bots_e", False):   # no trigger, report progress
        mc.log_event(f"{person.display_name} social sexual proclivity bots: {fetish_serum_calculate_completion(person, 'nano_bots_ec')}%", "float_text_blue")

def fetish_exhibition_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
    if person.event_triggers_dict.get("nano_bots_e", False):
        return # this fetish already triggered (prevents stacking multiple basic fetish serums)

    fetish_serum_increase_counter(person, "nano_bots_ec")

    # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
    if person.event_triggers_dict.get("nano_bots_ec", 0) < FETISH_SERUM_TRIGGER_VALUE:
        return

    person.event_triggers_dict["nano_bots_ec"] = 0 # reset counter
    person.event_triggers_dict["nano_bots_e"] = True # block any effect for this dose

    fetish_serum_increase_sluttiness(person, add_to_log = add_to_log)
    fetish_serum_increase_obedience(person, add_to_log = add_to_log)

    tier = person.suggest_tier
    if not fetish_serum_increase_opinion(FETISH_EXHIBITION_OPINION_LIST, tier - 1, person):
        if person.foreplay_sex_skill < 2 + tier:
            person.increase_sex_skill("Foreplay", 2 + tier, add_to_log = True)
        else:
            mc.log_event(f"{person.display_name} social sexual proclivity bots reduced effectiveness at {person.suggestibility}% suggestibility.", "float_text_blue")

    if start_exhibition_fetish_quest(person):
        person.event_triggers_dict["exhibition_fetish_start"] = True
        #TODO some kind of test here to indicate to the player that their exhibitionism quest has started

def unlock_fetish_serum(serum: SerumTrait):
    if not serum or serum.researched: # prevent duplicate unlock calls
        return
    serum.tier = 1
    serum.researched = True
    mc.business.event_triggers_dict["fetish_serum_count"] = fetish_serum_unlock_count() + 1

def unlock_body_monitor_serum():
    serum = get_body_monitor_serum()
    if not serum or serum.researched:
        return
    serum.tier = 1
    serum.researched = True

def enhance_body_monitor_serum():
    serum = get_body_monitor_serum()
    if serum:
        serum.add_mastery(2)
        serum.on_day = body_monitor_on_day
        serum.desc = "Monitors body functions and vital parameters and slowly improves body condition overnight. Remotely transfers data for further analysis to your R&D Division."
        serum._positive_slug = "Remote Mastery Improvement, +1 Max Energy/day (Max 160)"

def get_body_monitor_serum() -> SerumTrait:
    return next((x for x in list_of_traits if x.name == "Body Monitoring Nanobots"), None)

def fetish_unlock_basic_serum():
    unlock_fetish_serum(get_fetish_basic_serum())

def get_fetish_basic_serum() -> SerumTrait:
    return next((x for x in list_of_traits if x.name == "Sexual Proclivity Nanobots"), None)

def fetish_unlock_anal_serum():
    unlock_fetish_serum(get_fetish_anal_serum())
    add_fetish_serum_anal_warning()

def get_fetish_anal_serum() -> SerumTrait:
    return next((x for x in list_of_traits if x.name == "Anal Proclivity Nanobots"), None)

def fetish_unlock_exhibition_serum():
    unlock_fetish_serum(get_fetish_exhibition_serum())

def get_fetish_exhibition_serum() -> SerumTrait:
    return next((x for x in list_of_traits if x.name == "Social Sexual Proclivity Nanobots"), None)

def fetish_unlock_cum_serum():
    unlock_fetish_serum(get_fetish_cum_serum())
    add_fetish_serum_cum_warning()

def get_fetish_cum_serum() -> SerumTrait:
    return next((x for x in list_of_traits if x.name == "Semen Proclivity Nanobots"), None)

def fetish_unlock_breeding_serum():
    unlock_fetish_serum(get_fetish_breeding_serum())
    add_fetish_serum_breeding_warning()

def get_fetish_breeding_serum() -> SerumTrait:
    return next((x for x in list_of_traits if x.name == "Reproduction Proclivity Nanobots"), None)

def add_fetish_serum_traits():
    SerumTraitMod(name = "Body Monitoring Nanobots",
        desc = "Monitors body functions and vital parameters. Remotely transfers data for further analysis to your R&D Division.",
        positive_slug = "Remote Mastery Improvement",
        negative_slug = "",
        research_added = 1000,
        slots_added = 1,
        production_added = 50,
        base_side_effect_chance = 10,
        on_turn = body_monitor_on_turn,
        on_day = body_monitor_on_day,
        tier = 99,
        start_researched = False,
        research_needed = 1000,
        exclude_tags = ["Nanobots"],
        clarity_cost = 1000,
        hidden_tag = "Nanobots",
        mental_aspect = 0, physical_aspect = 3, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 1,
        allow_toggle = False)

    SerumTraitMod(name = "Sexual Proclivity Nanobots",
        desc = "Targeted endorphin emitters increase general positive sexual responses based on suggestibility.",
        positive_slug = "Increases sexual opinions, slowly increases foreplay skill",
        negative_slug = "",
        research_added = FETISH_RESEARCH_ADDED,
        slots_added = 1,
        production_added = FETISH_PRODUCTION_COST,
        base_side_effect_chance = 20,
        on_apply = fetish_basic_function_on_apply,
        on_remove = fetish_basic_function_on_remove,
        on_turn = fetish_basic_function_on_turn,
        tier = 99,
        start_researched = False,
        research_needed = 1000,
        exclude_tags = ["Nanobots"],
        clarity_cost = 1000,
        hidden_tag = "Nanobots",
        mental_aspect = 3, physical_aspect = 3, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
        allow_toggle = False)

    SerumTraitMod(name = "Social Sexual Proclivity Nanobots",
        desc = "Targeted endorphin emitters increase general positive opinions of public sexual encounters based on suggestibility.",
        positive_slug = "Increases exhibitionistic behaviour, slowly increases sluttiness / obedience",
        negative_slug = "",
        research_added = FETISH_RESEARCH_ADDED,
        slots_added = 1,
        production_added = FETISH_PRODUCTION_COST,
        base_side_effect_chance = 20,
        on_apply = fetish_exhibition_function_on_apply,
        on_remove = fetish_exhibition_function_on_remove,
        on_turn = fetish_exhibition_on_turn,
        tier = 99,
        start_researched = False,
        research_needed = 1200,
        exclude_tags = ["Nanobots"],
        clarity_cost = 1000,
        hidden_tag = "Nanobots",
        mental_aspect = 5, physical_aspect = 2, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
        allow_toggle = False)

    SerumTraitMod(name = "Anal Proclivity Nanobots",
        desc = "Targeted endorphin emitters increase pleasure received from anal stimulation based on suggestibility.",
        positive_slug = "Increases Anal sexual opinions, slowly increases anal skill / obedience",
        negative_slug = "",
        research_added = FETISH_RESEARCH_ADDED,
        slots_added = 1,
        production_added = FETISH_PRODUCTION_COST,
        base_side_effect_chance = 20,
        on_apply = fetish_anal_function_on_apply,
        on_remove = fetish_anal_function_on_remove,
        on_turn = fetish_anal_function_on_turn,
        tier = 99,
        start_researched = False,
        research_needed = 2000,
        exclude_tags = ["Nanobots"],
        clarity_cost = 1500,
        hidden_tag = "Nanobots",
        mental_aspect = 4, physical_aspect = 6, sexual_aspect = 6, medical_aspect = 1, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
        allow_toggle = False)

    SerumTraitMod(name = "Semen Proclivity Nanobots",
        desc = "Targeted endorphin emitters increase pleasure received when in contact with semen based on suggestibility.",
        positive_slug = "Increases Cum related sexual opinions, slowly increases oral skill / sluttiness",
        negative_slug = "",
        research_added = FETISH_RESEARCH_ADDED,
        slots_added = 1,
        production_added = FETISH_PRODUCTION_COST,
        base_side_effect_chance = 20,
        on_apply = fetish_cum_function_on_apply,
        on_remove = fetish_cum_function_on_remove,
        on_turn = fetish_cum_function_on_turn,
        tier = 99,
        start_researched = False,
        research_needed = 2000,
        exclude_tags = ["Nanobots"],
        clarity_cost = 1500,
        hidden_tag = "Nanobots",
        mental_aspect = 5, physical_aspect = 3, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
        allow_toggle = False)

    SerumTraitMod(name = "Reproduction Proclivity Nanobots",
        desc = "Targeted endorphin emitters increase reproduction drive and associated opinions based on suggestibility.",
        positive_slug = "Increases reproduction sexual opinions, slowly increases vaginal skill",
        negative_slug = "",
        research_added = FETISH_RESEARCH_ADDED,
        slots_added = 1,
        production_added = FETISH_PRODUCTION_COST,
        base_side_effect_chance = 20,
        on_apply = fetish_breeding_function_on_apply,
        on_remove = fetish_breeding_function_on_remove,
        on_turn = fetish_breeding_function_on_turn,
        tier = 99,
        start_researched = False,
        research_needed = 2000,
        exclude_tags = ["Nanobots"],
        clarity_cost = 1500,
        hidden_tag = "Nanobots",
        mental_aspect = 5, physical_aspect = 5, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
        allow_toggle = False)

def body_monitor_serum_is_unlocked():
    if not get_body_monitor_serum():
        return False
    return get_body_monitor_serum().researched

def fetish_anal_serum_is_unlocked():
    if not get_fetish_anal_serum():
        return False
    return get_fetish_anal_serum().researched

def fetish_breeding_serum_is_unlocked():
    if not get_fetish_breeding_serum():
        return False
    return get_fetish_breeding_serum().researched

def fetish_cum_serum_is_unlocked():
    if not get_fetish_cum_serum():
        return False
    return get_fetish_cum_serum().researched

def fetish_exhibition_serum_is_unlocked():
    if not get_fetish_exhibition_serum():
        return False
    return get_fetish_exhibition_serum().researched

def fetish_basic_serum_is_unlocked():
    if not get_fetish_basic_serum():
        return False
    return get_fetish_basic_serum().researched
