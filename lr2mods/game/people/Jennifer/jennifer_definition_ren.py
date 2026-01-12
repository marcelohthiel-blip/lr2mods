from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import diamond_ring, bobbed_hair
from game.game_roles._role_definitions_ren import onlyfans_role, instapic_role
from game.major_game_classes.game_logic.Room_ren import kitchen, mom_offices, mom_bedroom
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, unemployed_job
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, list_of_instantiation_functions, mom, lily, aunt, sarah
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.personality_types._personality_definitions_ren import reserved_personality
from game.people.Jennifer.jennifer_role_definition_ren import init_mother_roles, mother_role, get_mother_associate_role, get_mother_secretary_role
from game.people.Jennifer.jennifer_events_ren import add_mom_obedience_man_of_the_house_intro_action
from game.major_game_classes.business_related.Contract_ren import Contract


day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_instantiation_functions.append("create_jennifer_character")

def mom_titles(person: Person):
    valid_titles = ["Mother"]
    if person.love > 10:
        valid_titles.append("Mom")
    return valid_titles

def mom_possessive_titles(person: Person):
    valid_titles = ["your mother"]
    if person.love > 10:
        valid_titles.append("your mom")

    if person.sluttiness > 60 and person.love > 60:
        valid_titles.append("your literal MILF")

    if person.sluttiness > 90:
        valid_titles.append("your cock hungry mom")
        valid_titles.append("the family cumdump")
    return valid_titles

def mom_player_titles(person: Person):
    valid_titles = [mc.name]
    if person.happiness < 70:
        valid_titles.append(mc.name + " " + mc.last_name)

    if person.love > 20:
        valid_titles.append("Sweetheart")
        valid_titles.append("Sweety")
        valid_titles.append("Son")

    if person.sluttiness > 20:
        valid_titles.append("Darling")
        valid_titles.append("Baby")
        if person.can_be_spanked:
            valid_titles.append("Daddy")
    return valid_titles


def mom_work_promotion_one_requirement(person: Person):
    if mc.business.is_weekend or time_of_day == 0:
        return False
    if person.sluttiness < 30:
        return False
    if not person.is_home or person.is_sleeping:
        return False
    if not person.has_job(mom_associate_job):
        return False
    return True

def mom_found_serums_requirement(start_day):
    return day >= start_day

def create_jennifer_character():
    ### MOM ###
    mom_wardrobe = wardrobe_from_xml("Mom_Wardrobe")
    #original height = 0.94
    #adjusted height = 0.96
    mom_base = Outfit("Jennifer's accessories")
    mom_base.add_accessory(diamond_ring.get_copy(), [1.0, 0.84, 0, 0.95])

    global mom_business_wardrobe
    mom_business_wardrobe = wardrobe_from_xml("Business_Wardrobe") #Used in some of Mom's events when we need a business-ish outfit

    init_mother_roles()

    global mom_associate_job
    mom_associate_job = JobDefinition("Business Associate", get_mother_associate_role(), job_location = mom_offices,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2], wardrobe = mom_business_wardrobe, seniority_level = 2)

    global mom_secretary_job
    mom_secretary_job = JobDefinition("Office Secretary", get_mother_secretary_role(), job_location = mom_offices,
        day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2], wardrobe = mom_business_wardrobe, seniority_level = 1)

    mom_personality = Personality("mom", reserved_personality.default_prefix,
        common_likes = ["conservative outfits", "work uniforms", "makeup", "the colour pink", "the colour yellow"],
        common_sexy_likes = ["being submissive", "bareback sex", "creampies"],
        common_dislikes = ["production work", "sports", "the colour brown", "the colour green"],
        common_sexy_dislikes = ["anal sex", "drinking cum", "sex standing up"],
        titles_function = mom_titles, possessive_titles_function = mom_possessive_titles, player_titles_function = mom_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global mom
    mom = make_person(name = "Jennifer", last_name = mc.last_name, age_range = [41, 44], body_type = "thin_body", face_style = "Face_1", tits = "DD", height = 0.92, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = bobbed_hair, skin="white",
        eyes = "brown", personality = mom_personality, name_color = "#8fff66", dial_color = "#8fff66", starting_wardrobe = mom_wardrobe, start_home = mom_bedroom,
        stat_array = [3, 2, 4], skill_array = [5, 2, 0, 0, 2], sex_skill_array = [2, 1, 3, 0], sluttiness = 7, obedience = 92, happiness = 108, love = 8, job = mom_associate_job,
        title = "Mom", possessive_title = "your mother", mc_title = "Sweetheart", relationship = "Single", kids = 2, base_outfit = mom_base,
        forced_opinions = [
            ["pants", 2, False],
            ["skirts", 1, False],
            ["flirting", -1, False],
            ["the colour black", 2, False],
            ["the colour red", 1, False]],
        forced_sexy_opinions= [
            ["taking control", 2, False]],
        serum_tolerance = 2, work_experience = 3, type="story")

    mom.add_role(mother_role)
    mom.set_schedule(kitchen, time_slots = 3)
    mom.primary_job.job_known = True
    mom.set_event_day("day_met")

    add_mom_obedience_man_of_the_house_intro_action()

    mom.add_unique_on_talk_event(
        Action("mom promotion one crisis", mom_work_promotion_one_requirement, "mom_work_promotion_one", priority = 30)
    )

    mc.create_event("mom_found_serums", "Mom wants to talk", day_restriction = (3, 4, 5, 6), time_restriction = 0, person = mom)
    # mc.business.add_mandatory_morning_crisis(
    #     Action("mom find serum", mom_found_serums_requirement, "mom_found_serums", requirement_args = 3)
    # )

    mom.home.add_person(mom)
    mc.phone.register_number(mom)

    town_relationships.update_relationship(mom, lily, "Daughter", "Mother")

##############
# Story Info #
##############

def jennifer_story_character_description():
    return "[mom.name] is your mother, and you live together with her and your sister, [lily.name]. Your father is out of the picture."

def jennifer_story_love_list():
    love_story_list = {}

    if mom.is_girlfriend:
        love_story_list[1] = "[mom.name] has agreed to be your girlfriend!"
    elif mom.love < 60:
        love_story_list[1] = "Increase [mom.name]'s love and try to make her your girlfriend."
        return love_story_list
    elif not lily.event_triggers_dict.get("mom_girlfriend_ask_blessing", False):
        love_story_list[1] = "Work on getting [lily.name] to accept your relationship."
        return love_story_list
    else:
        love_story_list[1] = "You might be able to convince [mom.name] to be your girlfriend if you try."
        return love_story_list

    love_story_list[2] = "There is nothing more in this story line at this time."
    return love_story_list

def jennifer_story_love_is_complete():
    return mom.is_girlfriend

def jennifer_story_lust_list():
    lust_story_list = {}
    if mom.is_employee: #First, check and see if we have hired her.
        #If we have hired Jennifer, we drop all the entries for her previous job, and pick up new entries for being MC's employee
        lust_story_list[0] = "[mom.title] works for you now! The next set of events has not yet been written."
        return lust_story_list

    if mom.has_job(unemployed_job):
        lust_story_list[0] = "[mom.title] is currently unemployed. Maybe you could hire her?"
        return lust_story_list

    if mom.progress.lust_step == 0:
        if mom.sluttiness < 30:
            lust_story_list[0] = "Increase [mom.title]'s sluttiness to trigger this event"
        else:
            lust_story_list[0] = "[mom.title] will approach you soon."
    elif mom.progress.lust_step == 1:
        if mom.event_triggers_dict.get("mom_work_promotion_outfit_slutty", False):
            lust_story_list[0] = "[mom.title] is up for a promotion at her job, and you suggested she use her womanly charms to get it."
        else:
            lust_story_list[0] = "[mom.title] is up for a promotion at her job, and you suggested she use her professionalism to get it."
    elif mom.progress.lust_step == 2:
        if mom.event_triggers_dict.get("mom_work_promotion_two_prep_enabled", False):
            lust_story_list[0] = "[mom.title] needs help preparing for a round two interview for her promotion. You should help her prepare for it."
        elif mom.event_triggers_dict.get("mom_work_promotion_two_tactic", "professional") == "slutty":
            lust_story_list[0] = "You helped [mom.title] prepare for her next interview by suggesting she act slutty."
        elif mom.event_triggers_dict.get("mom_work_promotion_two_tactic", "professional") == "friendly":
            lust_story_list[0] = "You helped [mom.title] prepare for her next interview by suggesting she be extra friendly."
        elif mom.event_triggers_dict.get("mom_work_promotion_two_tactic", "professional") == "professional":
            lust_story_list[0] = "You helped [mom.title] prepare for her next interview by suggesting she be strictly professional."
    elif mom.progress.lust_step >= 3:
        if mom.has_job(mom_secretary_job):
            lust_story_list[0] = "You helped [mom.title] get promoted to being a personal secretary."
            if mom.sluttiness < 40:
                lust_story_list[1] = "Increase [mom.title]'s sluttiness to trigger her next event"
            else:
                lust_story_list[1] = "[mom.title] will approach you soon for her next event."
        else:
            lust_story_list[0] = "Your help wasn't enough, and [mom.title] didn't get a promotion."
            lust_story_list[1] = "To continue this arc, you should convince her to quit and to come work for you."
    if mom.progress.lust_step == 4:
        if mom.event_triggers_dict.get("mom_promotion_boss_phase_one", False):
            lust_story_list[1] = "[mom.fname] is worried about being replaced at her work. You should talk to her boss about the situation, then report back to her."
        elif mom.event_triggers_dict.get("mom_replacement_approach", "tits") == "seduce":
            lust_story_list[1] = "[mom.fname] is worried about being replaced at her work. You suggested that she perform sexual favours for her boss."
        elif mom.event_triggers_dict.get("mom_replacement_approach", "tits") == "tits":
            lust_story_list[1] = "[mom.fname] is worried about being replaced at her work. You suggested that she get bigger tits."
    elif mom.progress.lust_step >= 5:
        if mom.event_triggers_dict.get("mom_replacement_approach", "seduce") == "seduce":
            lust_story_list[1] = "[mom.fname] kept her boss from hiring a replacement by performing sexual favours for him."
        else:
            lust_story_list[1] = "[mom.fname] kept her boss from hiring a replacement by getting bigger tits."
        if mom.progress.lust_step == 5:
            lust_story_list[2] = "Give [mom.title] some time to settle in to her new work duties."
    if mom.progress.lust_step >= 6:
        lust_story_list[2] = "[mom.fname] is regularly giving her boss sexual favours."
    if mom.progress.lust_step == 6:
        if mom.sluttiness < 60:
            lust_story_list[3] = "Increase [mom.title]'s sluttiness to trigger her next event."
        else:
            lust_story_list[1] = "Check on [mom.title] in the evening in the kitchen once in a while."
    elif mom.progress.lust_step == 7:
        lust_story_list[3] = "Wait a few days, then check on [mom.title] in the kitchen in the evening."
    elif mom.progress.lust_step >= 8:
        lust_story_list[3] = "She has started letting him fuck her."
    if mom.progress.lust_step == 8:
        lust_story_list[4] = "Give [mom.title] a few days to settle in at her job."
    elif mom.progress.lust_step == 9:
        lust_story_list[4] = "Check in with [mom.title]'s boss to see how he is enjoying her."
    elif mom.progress.lust_step == 10:
        if mom.event_triggers_dict.get("boss_teamup", False):
            lust_story_list[4] = "Her boss wants [mom.title] to learn to love bareback sex."
        else:
            lust_story_list[4] = "This storyline has no further content in this version."
    if mom.progress.lust_step == 11:
        lust_story_list[3] = "She has started letting him fuck her bareback."
        lust_story_list[4] = "This storyline has no further content in this version."

    return lust_story_list

def jennifer_story_lust_is_complete():
    return (
        mom.is_employee
        or mom.progress.lust_step == 10 and not mom.event_triggers_dict.get("boss_teamup", False)
        or mom.progress.lust_step == 11
    )

def jennifer_story_obedience_list():
    obedience_story_list = {}
    if mom.progress.obedience_step == 0:
        obedience_story_list[0] = "Wait until the weekend."
    elif mom.progress.obedience_step >= 1:
        obedience_story_list[0] = "[mom.title] pays bills every Saturday morning. Use this opportunity to support her and gain her obedience."
    if mom.progress.obedience_step == 1:
        if mom.obedience < 120:
            obedience_story_list[1] = "Increase [mom.possessive_title]'s obedience to trigger her next event."
        else:
            obedience_story_list[1] = "[mom.possessive_title!c] may surprise you soon in the morning."
    elif mom.progress.obedience_step >= 2:
        obedience_story_list[1] = "[mom.possessive_title!c] is willing to make you breakfast in bed once in a while."
    if mom.progress.obedience_step == 2:
        if mom.obedience < 140:
            obedience_story_list[2] = "Increase [mom.possessive_title]'s obedience to trigger her next event."
        else:
            obedience_story_list[2] = "Talk to [mom.title] in the evening or night and she may be doing housework."
    elif mom.progress.obedience_step > 2:
        obedience_story_list[2] = "You can give [mom.title] outfits to wear around the house with an apron instead of a top."
        obedience_story_list[3] = "This storyline has no further content in this version."
    return obedience_story_list

def jennifer_story_obedience_is_complete() -> bool:
    return mom.progress.obedience_step > 2

def jennifer_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamups = {
        0: (lily, "[mom.fname] and your sister... The ultimate fantasy? There is probably no way this could ever happen."),
        1: (sarah, "Maybe someday you could get [mom.fname] together with [sarah.fname]..."),    #this should have conditions on it
        2: (aunt, "[aunt.fname] and your mom... Two hot MILFs, could something like this be possible?"),
    }
    return teamups

def jennifer_story_other_list():
    other_story_list = {}
    #Jennifers other story index:
    # 0 - Her current employment status
    # 1 - Her current taboo status
    # 2 - Her current Insta status
    # 3 - Her current girlfriend status
    if mom.has_job(mom_secretary_job):
        other_story_list[0] = "[mom.fname] is a personal assistant at the company she works for."
    elif mom.has_job(mom_associate_job):
        other_story_list[0] = "[mom.fname] is a business associate at the company she works for."
    elif mom.has_job(unemployed_job):
        other_story_list[0] = "[mom.fname] is currently unemployed."
    elif mom.is_employee:
        other_story_list[0] = "[mom.fname] works for you."
    else:
        other_story_list[0] = "[mom.fname] has some other job? Please report this error on Discord."

    if mom.event_triggers_dict.get("vaginal_revisit_complete", False):
        other_story_list[1] = "[mom.possessive_title!c] is completely open to your sexual requests."
    elif mom.event_triggers_dict.get("anal_revisit_complete", False):
        other_story_list[1] = "[mom.possessive_title!c] is willing to let you take her anally, but is refusing to go all the way."
    elif mom.event_triggers_dict.get("oral_revisit_complete", False):
        other_story_list[1] = "[mom.possessive_title!c] is willing to exchange oral favours, but refuses to go any further."
    elif mom.event_triggers_dict.get("kissing_revisit_complete", False):
        other_story_list[1] = "[mom.possessive_title!c] is willing to exchange minor sexual favours, but refuses to go any further."
    else:
        other_story_list[1] = "[mom.possessive_title!c] is unwilling to let you touch her sexually."

    if mom.has_role(onlyfans_role):
        other_story_list[2] = "[mom.title] has an OnlyFanatics that she regularly posts nudes to."
    elif mom.has_role(instapic_role):
        other_story_list[2] = "[mom.title] has an InstaPic account that she regularly posts pics to."
    else:
        other_story_list[2] = "[mom.title] doesn't post pictures online anywhere that you are aware of."

    other_story_list[3] = "[mom.fname] isn't dating anyone seriously that you know of."

    return other_story_list

####################
# Position Filters #
####################

def jennifer_oral_position_filter(oral_position: Position) -> bool:
    return mom.event_triggers_dict.get("kissing_revisit_complete", False)

def jennifer_vaginal_position_filter(vaginal_position: Position)-> bool:
    return mom.event_triggers_dict.get("anal_revisit_complete", False)

def jennifer_anal_position_filter(anal_position: Position)-> bool:
    return mom.event_triggers_dict.get("oral_revisit_complete", False)

def jennifer_oral_position_info() -> str:
    return "Break oral taboo"

def jennifer_vaginal_position_info() -> str:
    return "Break anal taboo"

########################
#  Vandalay Contracts  #
########################
def vandalay_serum_count_up():
    mc.business.event_triggers_dict["vandalay_contract_count"] = mc.business.event_triggers_dict.get("vandalay_contract_count", 0) + 1

def vandalay_serum_req(serum: SerumDesign):
    return serum.has_hidden_tag("Suggest") and serum.has_hidden_tag("Slut")

def get_vandalay_contract() -> Contract:
    if mc.business.event_triggers_dict.get("vandalay_contracts", False):
        vandalay_contract = None
        vandalay_contract = Contract("Vandalay Bank Intern Initiation Contract",
                                "Vandalay Bank has just hired a new batch of interns. Serums are requested to help them 'find their place' in the company hierarchy.\nMust have a sluttiness and suggestibility trait included", 5,
            mental_requirement = 4, physical_requirement = 0,
            sexual_requirement = 10, medical_requirement = 0,
            flaw_tolerance = 1, attention_tolerance = 3, amount_desired = 30,
            other_requirement = vandalay_serum_req, other_payout = vandalay_serum_count_up)
        return vandalay_contract
    return None
