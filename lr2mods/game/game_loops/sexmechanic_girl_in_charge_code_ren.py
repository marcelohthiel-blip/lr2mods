from __future__ import annotations
from typing import Any
import renpy
from renpy import persistent
from game.helper_functions.list_functions_ren import known_people_in_the_game
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Room_ren import bedroom
from game.major_game_classes.game_logic.Position_ren import Position
from game.sex_positions._position_definitions_ren import list_of_girl_positions, spanking, cunnilingus, cowgirl_cunnilingus, standing_dildo, standing_finger, standing_grope, standing_oral, standing_cunnilingus, kissing, handjob, cowgirl, anal_cowgirl, drysex_cowgirl, blowjob, deepthroat, skull_fuck, tit_fuck, cum_fetish_blowjob, ophelia_blowjob, sarah_tit_fuck
from game.random_lists_ren import get_random_from_weighted_list
from game.people.Kaya.kaya_definition_ren import kaya
from game.people.Ophelia.ophelia_definition_ren import salon_manager
from game.people.Sarah.sarah_definition_ren import sarah
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
list_of_selfish_dom_sex_goals = [
    "get off",
    "waste cum", #Unrealistic until we can control where MC finishes. Through new sex options?
    # "hate fuck" #We can't yet reliably path to this. Not enough path options
]

list_of_unselfish_dom_sex_goals = [
    "vaginal creampie",
    "anal creampie",
    "facial",
    "body shot",
    "get mc off", #Generally this will be foreplay tags
    "oral creampie"
]

list_of_all_dom_sex_goals = list_of_selfish_dom_sex_goals + list_of_unselfish_dom_sex_goals

class dom_sex_path_node():
    def __init__(self, position: Position, completion_requirement: bool = True):
        self.position = position
        self.completion_requirement = completion_requirement

def get_goal_based_on_position(position: Position):
    return ("get off" if position in (spanking, cunnilingus,
        cowgirl_cunnilingus, standing_dildo, standing_finger,
        standing_grope, standing_oral, standing_cunnilingus)
        else "get mc off")

def dom_requirement_creampie(person: Person, the_report: dict[str, Any]):
    return the_report["guy orgasms"] >= 1 and person.has_creampie_cum

def dom_requirement_anal_creampie(person: Person, the_report: dict[str, Any]):
    return the_report["guy orgasms"] >= 1 and person.has_creampie_cum

def dom_requirement_oral_creampie(person: Person, the_report: dict[str, Any]):
    return the_report["guy orgasms"] >= 1 and person.has_mouth_cum

def dom_requirement_facial(person: Person, the_report: dict[str, Any]):
    return the_report["guy orgasms"] >= 1 and person.has_face_cum

def dom_requirement_body_shot(person: Person, the_report: dict[str, Any]):
    return (the_report["guy orgasms"] >= 1
        and (person.has_ass_cum
            or person.has_tits_cum
            or person.has_stomach_cum
            or person.has_face_cum))

def dom_requirement_get_mc_off(person: Person, the_report: dict[str, Any]):
    return the_report["guy orgasms"] >= 1

def dom_requirement_get_off(person: Person, the_report: dict[str, Any]):
    return the_report["girl orgasms"] >= 1

def dom_requirement_hate_fuck(person: Person, the_report: dict[str, Any]):
    return the_report["girl orgasms"] >= 2

def dom_requirement_waste_cum(person: Person, the_report: dict[str, Any]):
    return the_report["guy orgasms"] >= 1

def dom_requirement_mc_hard(person: Person, the_report: dict[str, Any]):
    return mc.arousal_perc > 20

def dom_requirement_mc_aroused(person: Person, the_report: dict[str, Any]):
    return mc.arousal_perc > 40

def dom_requirement_mc_highly_aroused(person: Person, the_report: dict[str, Any]):
    return mc.arousal_perc > 70

def dom_requirement_girl_aroused(person: Person, the_report: dict[str, Any]):
    return person.arousal_perc > 40

def dom_requirement_girl_highly_aroused(person: Person, the_report: dict[str, Any]):
    return person.arousal_perc > 70

def dom_requirement_girl_vagina_avail(person: Person, the_report: dict[str, Any]):
    return person.vagina_available

def dom_requirement_tits_avail(person: Person, the_report: dict[str, Any]):
    return person.tits_available

def construct_mc_turn_on_weighted_list(person: Person, prohibit_tags = []):
    position_option_list = []
    position_option_list.append((kissing, 30 + person.opinion.kissing))
    position_option_list.append((handjob, 30 + person.opinion.giving_handjobs))
    position_option_list.append((drysex_cowgirl, 30 + person.opinion.taking_control))
    return get_random_from_weighted_list(position_option_list)

def set_sex_goal(person: Person, the_goal):
    person.event_triggers_dict["sex_goal"] = the_goal

def reset_sex_goal(person: Person):
    person.event_triggers_dict["sex_goal"] = None

#Use this function to make a "random" sex goal. Weights outcome based on the person and how far things have already gone.
#weight is scale 0-100
def create_sex_goal(person: Person, report_log: dict[str, Any] = None):
    if "report_log" in globals() and isinstance(report_log, dict): #First, check if we are here
        if report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) == 0:   #We are here because Mc finished too fast.
            pass #TODO do this here or in the original call?

    dom_sex_goal_weighted_list = []

    if person.fetish_count > 0: #She has fetishes, so use those to set a goal.
        if person.has_anal_fetish:
            dom_sex_goal_weighted_list.append(("anal creampie", 100))
        if person.has_cum_fetish:
            dom_sex_goal_weighted_list.append(("oral creampie", 50))
            dom_sex_goal_weighted_list.append(("body shot", 50))
            dom_sex_goal_weighted_list.append(("facial", 50))
        if person.has_breeding_fetish:
            dom_sex_goal_weighted_list.append(("vaginal creampie", 100))
        return get_random_from_weighted_list(dom_sex_goal_weighted_list)  #Hopefully this works if list only has one entry

    # If love is less than 0, we consider selfish sex goals
    if person.love < 0:
        for goal in list_of_selfish_dom_sex_goals:
            dom_sex_goal_weighted_list.append((goal, -person.love))
    else: #Always have at least one option in the list
        dom_sex_goal_weighted_list.append(("get mc off", 30))

    #Next, we add individual goals based on her sluttiness. #TODO consider a list of constants declared at the top that can be changed for setting sluttiness threshholds for these.
    #body shot
    if person.sluttiness > 30:
        body_shot_weight = 40 + (person.opinion.being_covered_in_cum * 10)
        dom_sex_goal_weighted_list.append(("body shot", body_shot_weight))

    #Facial
    if person.sluttiness > 40:
        facial_weight = 40 + (person.opinion.being_covered_in_cum * 10) + (person.opinion.cum_facials * 10)
        dom_sex_goal_weighted_list.append(("facial", facial_weight))

    #oral creampie
    if person.sluttiness > 50 and not person.has_taboo("oral_sex"):
        oral_creampie_weight = 40 + (person.opinion.drinking_cum * 20)
        dom_sex_goal_weighted_list.append(("oral creampie", oral_creampie_weight))

    #vaginal creampie
    if person.sluttiness > 60 and not person.has_taboo("vaginal_sex"):
        vaginal_creampie_weight = 40 + (person.opinion.creampies * 20)
        dom_sex_goal_weighted_list.append(("vaginal creampie", vaginal_creampie_weight))

    #anal creampie
    if person.sluttiness > 70 and not person.has_taboo("anal_sex"):
        anal_creampie_weight = 40 + (person.opinion.anal_creampies * 20)
        dom_sex_goal_weighted_list.append(("anal creampie", anal_creampie_weight))

    return get_random_from_weighted_list(dom_sex_goal_weighted_list)

def build_blowjob_path(person: Person):
    path = [] # start off with normal blowjob
    path.append(dom_sex_path_node(blowjob, dom_requirement_mc_aroused))

    transition = deepthroat
    if person.oral_sex_skill >= 5 and person.opinion.giving_blowjobs > 1 and person.is_submissive:
        transition = skull_fuck
    if person.has_cum_fetish:
        transition = cum_fetish_blowjob
    if person == salon_manager:
        transition = ophelia_blowjob

    path.append(dom_sex_path_node(transition, dom_requirement_get_mc_off))
    return path

def build_titfuck_path(person: Person):
    path = [] # use handjob as intro
    path.append(dom_sex_path_node(handjob, dom_requirement_mc_hard))

    transition = tit_fuck
    if person == sarah:
        transition = sarah_tit_fuck

    if person.has_cum_fetish: # when she has a cum fetish she will finish you off with her mouth
        path.append(dom_sex_path_node(transition, dom_requirement_mc_highly_aroused))
        path.append(dom_sex_path_node(cum_fetish_blowjob, dom_requirement_get_mc_off))
    else: # complete titfuck
        path.append(dom_sex_path_node(transition, dom_requirement_get_mc_off))
    return path

def build_cowgirl_path(person: Person, skill_tag = "Vaginal", use_warmup = True):
    path = []
    if use_warmup:
        path.append(dom_sex_path_node(drysex_cowgirl, dom_requirement_girl_aroused))
    if skill_tag == "Vaginal":
        path.append(dom_sex_path_node(cowgirl, dom_requirement_get_off))
        path.append(dom_sex_path_node(cowgirl, dom_requirement_get_mc_off))
    elif skill_tag == "Anal":
        path.append(dom_sex_path_node(anal_cowgirl, dom_requirement_get_off))
        path.append(dom_sex_path_node(anal_cowgirl, dom_requirement_get_mc_off))
    else:
        path.append(dom_sex_path_node(drysex_cowgirl, dom_requirement_get_mc_off))
    return path

def get_cowgirl_path_preferred_skill_tag(person: Person):
    possible_positions = [("Foreplay", 1)] # default "Foreplay" she will only dryhump
    if person.is_willing(cowgirl) and not person.is_position_filtered(cowgirl):
        possible_positions.append(("Vaginal", (person.opinion.vaginal_sex + (10 if person.has_breeding_fetish else 2)) * 5))
    if person.is_willing(anal_cowgirl) and not person.is_position_filtered(anal_cowgirl):
        possible_positions.append(("Anal", (person.opinion.anal_sex + (10 if person.has_anal_fetish else 2)) * 5))
    return get_random_from_weighted_list(possible_positions)

def get_goal_completion_requirement(the_goal: str):
    if the_goal == "get off":
        return dom_requirement_get_off
    if the_goal == "waste cum":
        return dom_requirement_waste_cum
    if the_goal == "hate fuck":
        return dom_requirement_hate_fuck
    if the_goal == "vaginal creampie":
        return dom_requirement_creampie
    if the_goal == "anal creampie":
        return dom_requirement_anal_creampie
    if the_goal == "facial":
        return dom_requirement_facial
    if the_goal == "body shot":
        return dom_requirement_body_shot
    if the_goal == "get mc off":
        return dom_requirement_get_mc_off
    if the_goal == "oral creampie":
        return dom_requirement_oral_creampie
    return dom_requirement_get_mc_off  # default 'get mc off'

def create_sex_path(person: Person, the_goal: str, prohibit_tags = []):
    position_option_list = []
    second_position_option_list = []
    extra_positions = []
    ### Create list of possible positions###
    # when she enjoys blow jobs, add one to her choices (to prevent always going to blowjob variant)
    if person.has_cum_fetish:
        extra_positions.append(cum_fetish_blowjob)
    elif person.oral_sex_skill >= 5 and person.opinion.giving_blowjobs > 1 and person.is_submissive:
        extra_positions.append(skull_fuck)
    elif person.oral_sex_skill > 3 and person.opinion.giving_blowjobs > 1:
        extra_positions.append(deepthroat)
    elif person.oral_sex_skill > 2 and person.opinion.giving_blowjobs > 0:
        extra_positions.append(blowjob)
    elif the_goal == "oral creampie" or the_goal == "facial":
        extra_positions.append(blowjob)

    # when she enjoys tit fucks, add it to her position choices
    if person.foreplay_sex_skill > 2 and person.opinion.giving_tit_fucks >= 1 and person.has_large_tits:
        extra_positions.append(tit_fuck)

    #TODO we also need to check and make sure an object exists for each possible sex position. Figure out how to do this
    #TODO Add in per character position filters so make sure ALL positions are included
    for position in list_of_girl_positions + extra_positions:
        if the_goal in position.gic_tags:
            if person.sluttiness >= position.slut_requirement:
                if position.skill_tag not in prohibit_tags:
                    position_option_list.append((position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))))  #every qualifying position has at least weight 20, with higher weights if actual sluttiness is close to requirement

    if len(position_option_list) == 0: #Somehow no positions available for this requirement.
        return None

    #Construct final node by choosing appropriately tagged final position
    final_node = dom_sex_path_node(get_random_from_weighted_list(position_option_list))
    final_node.completion_requirement = get_goal_completion_requirement(the_goal)

    ###Construct path to final node
    #First, we explore cases where we MUST have an earlier node
    req_func = None
    first_position = None

    #She isn't naked enough to go straight to final node
    if not final_node.position.check_clothing(person):  #She isn't naked enough to go straight to the end node
        for position in list_of_girl_positions + extra_positions:
            if person.allow_position(position) and mc.location.has_object_with_trait(position.requires_location):
                if position.check_clothing(person):
                    if final_node.position.skill_tag == "Vaginal" or final_node.position.skill_tag == "Anal":
                        if position.skill_tag == "Foreplay" or position.skill_tag == "Oral":
                            if position.skill_tag not in prohibit_tags:
                                second_position_option_list.append((position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))))
                    else:
                        if position.skill_tag == "Foreplay":
                            if position.skill_tag not in prohibit_tags:
                                second_position_option_list.append((position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))))
        if len(second_position_option_list) == 0: #No workable options.
            return None
        first_position = get_random_from_weighted_list(second_position_option_list)
        if final_node.position.requires_clothing == "Vagina":
            req_func = dom_requirement_girl_vagina_avail
        else:
            req_func = dom_requirement_tits_avail

    #MC isn't hard enough for final node
    elif mc.recently_orgasmed and final_node.position.requires_hard:
        first_position = construct_mc_turn_on_weighted_list(person, prohibit_tags)
        req_func = dom_requirement_mc_aroused

    #If we don't have a first node, 50/50 chance we create a first node, or sex begins with final node
    elif renpy.random.randint(0, 100) < 50:
        for position in list_of_girl_positions + extra_positions:
            if person.allow_position(position) and mc.location.has_object_with_trait(position.requires_location):
                if position.check_clothing(person):
                    if final_node.position.skill_tag == "Vaginal" or final_node.position.skill_tag == "Anal":
                        if position.skill_tag == "Foreplay" or position.skill_tag == "Oral":
                            if position.skill_tag not in prohibit_tags:
                                second_position_option_list.append((position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))))
                    else:
                        if position.skill_tag == "Foreplay":
                            if position.skill_tag not in prohibit_tags:
                                second_position_option_list.append((position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))))

        first_position = get_random_from_weighted_list(second_position_option_list)
        if first_position:
            if first_position.girl_arousal > first_position.guy_arousal: #Choose our exit function based on who the position arouses more
                req_func = dom_requirement_girl_aroused
            else:
                req_func = dom_requirement_mc_aroused

    ###Now we construct our path.
    sex_path = []
    if first_position is None:  #We are going straight to our final position
        sex_path.append(final_node)
        return sex_path
    else:
        first_node = dom_sex_path_node(first_position, completion_requirement = req_func)
        sex_path.append(first_node)
        sex_path.append(final_node)
        return sex_path

def sex_can_continue(person: Person, the_node: dom_sex_path_node = None): #Use this to check and see if girl would be up to continue the current position
    if not the_node:
        return False

    position = the_node.position
    if position is not None:
        if not position.check_clothing(person):
            return False
        if person.energy < 10 + position.girl_energy * 2:  #Enough for at least 2 more rounds
            return False
        if mc.energy < 10 + position.guy_energy * 2:
            return False
    elif person.energy < 30 or mc.energy < 30:
        return False
    return True

def requires_condom(person: Person):
    if person == kaya and persistent.pregnancy_pref != 0:
        return False
    if person.effective_sluttiness("condomless_sex") < person.get_no_condom_threshold(situational_modifier = 10):
        return True
    return False

def go_raw_mid_sex(person: Person):
    if person.effective_sluttiness("condomless_sex") > person.get_no_condom_threshold(situational_modifier = 25):
        return renpy.random.randint(0, 100) < 10  #10% chance per round over sluttiness threshold
    return False

def GIC_unit_test(count = 1): #Count is the number of times we repeat the unit test.
    unit_test_count = 0
    while unit_test_count < count:
        mc.change_location(bedroom)
        the_person = renpy.random.choice(known_people_in_the_game())
        the_person.love = renpy.random.randint(-50, 50)
        the_person._sluttiness = renpy.random.randint(60, 100)
        mc.energy = mc.max_energy
        the_person.energy = the_person.max_energy
        renpy.call("get_fucked", the_person, unit_test = True, the_goal = renpy.random.choice(list_of_all_dom_sex_goals))
        unit_test_count += 1

def GIC_unit_test_2(count = 1): #Count is the number of times we repeat the unit test.
    unit_test_count = 0
    while unit_test_count < count:
        mc.change_location(bedroom)
        the_person = renpy.random.choice(known_people_in_the_game())
        the_person.love = -50
        the_person._sluttiness = renpy.random.randint(60, 100)
        mc.energy = mc.max_energy
        the_person.energy = the_person.max_energy
        renpy.call("get_fucked", the_person, unit_test = True)
        unit_test_count += 1
