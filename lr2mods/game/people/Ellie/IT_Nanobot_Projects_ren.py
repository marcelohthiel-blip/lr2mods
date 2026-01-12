from __future__ import annotations
from game.major_game_classes.serum_related.serums.fetish_serums_ren import FETISH_ANAL_OPINION_LIST, FETISH_BREEDING_OPINION_LIST, FETISH_CUM_OPINION_LIST, FETISH_EXHIBITION_OPINION_LIST, FETISH_RESEARCH_ADDED, FETISH_SERUM_ATTENTION, fetish_unlock_anal_serum, fetish_unlock_breeding_serum, fetish_unlock_cum_serum, fetish_unlock_exhibition_serum, get_fetish_anal_serum, get_fetish_basic_serum, get_fetish_breeding_serum, get_fetish_cum_serum, get_fetish_exhibition_serum
from game.major_game_classes.character_related.Person_ren import mc
from game.people.Ellie.IT_Project_class_ren import IT_Project

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
## Nano IT Projects

### Project related functions ###

def basic_clarity_reduction_on_apply():
    get_fetish_basic_serum().research_added = 100

def basic_clarity_reduction_on_remove():
    get_fetish_basic_serum().research_added = FETISH_RESEARCH_ADDED

def basic_attention_reduction_on_apply():
    get_fetish_basic_serum().attention = 0

def basic_attention_reduction_on_remove():
    get_fetish_basic_serum().attention = FETISH_SERUM_ATTENTION

def anal_clarity_reduction_on_apply():
    get_fetish_anal_serum().research_added = 100

def anal_clarity_reduction_on_remove():
    get_fetish_anal_serum().research_added = FETISH_RESEARCH_ADDED

def anal_attention_reduction_on_apply():
    get_fetish_anal_serum().attention = 0

def anal_attention_reduction_on_remove():
    get_fetish_anal_serum().attention = FETISH_SERUM_ATTENTION

def breeder_clarity_reduction_on_apply():
    get_fetish_breeding_serum().research_added = 100

def breeder_clarity_reduction_on_remove():
    get_fetish_breeding_serum().research_added = FETISH_RESEARCH_ADDED

def breeder_attention_reduction_on_apply():
    get_fetish_breeding_serum().attention = 0

def breeder_attention_reduction_on_remove():
    get_fetish_breeding_serum().attention = FETISH_SERUM_ATTENTION

def cum_clarity_reduction_on_apply():
    get_fetish_cum_serum().research_added = 100

def cum_clarity_reduction_on_remove():
    get_fetish_cum_serum().research_added = FETISH_RESEARCH_ADDED

def cum_attention_reduction_on_apply():
    get_fetish_cum_serum().attention = 0

def cum_attention_reduction_on_remove():
    get_fetish_cum_serum().attention = FETISH_SERUM_ATTENTION

def exhibition_clarity_reduction_on_apply():
    get_fetish_exhibition_serum().research_added = 100

def exhibition_clarity_reduction_on_remove():
    get_fetish_exhibition_serum().research_added = FETISH_RESEARCH_ADDED

def exhibition_attention_reduction_on_apply():
    get_fetish_exhibition_serum().attention = 0

def exhibition_attention_reduction_on_remove():
    get_fetish_exhibition_serum().attention = FETISH_SERUM_ATTENTION

def anal_incest_project_on_apply():
    if "incest" not in FETISH_ANAL_OPINION_LIST:
        FETISH_ANAL_OPINION_LIST.append("incest")

def anal_incest_project_on_remove():
    if "incest" in FETISH_ANAL_OPINION_LIST:
        FETISH_ANAL_OPINION_LIST.remove("incest")

def breeder_submission_project_on_apply():
    if "being submissive" not in FETISH_BREEDING_OPINION_LIST:
        FETISH_BREEDING_OPINION_LIST.append("being submissive")

def breeder_submission_project_on_remove():
    if "being submissive" in FETISH_BREEDING_OPINION_LIST:
        FETISH_BREEDING_OPINION_LIST.remove("being submissive")

def cum_thirst_project_on_apply():
    if "taking control" not in FETISH_CUM_OPINION_LIST:
        FETISH_CUM_OPINION_LIST.append("taking control")

def cum_thirst_project_on_remove():
    if "taking control" in FETISH_CUM_OPINION_LIST:
        FETISH_CUM_OPINION_LIST.remove("taking control")

def exhibition_cheating_project_on_apply():
    if "cheating on men" not in FETISH_EXHIBITION_OPINION_LIST:
        FETISH_EXHIBITION_OPINION_LIST.append("cheating on men")

def exhibition_cheating_project_on_remove():
    if "cheating on men" in FETISH_EXHIBITION_OPINION_LIST:
        FETISH_EXHIBITION_OPINION_LIST.remove("cheating on men")

def anal_program_unlock_project_on_apply():
    fetish_unlock_anal_serum()

def breeder_program_unlock_project_on_apply():
    fetish_unlock_breeding_serum()

def cum_program_unlock_project_on_apply():
    fetish_unlock_cum_serum()

def exhibition_program_unlock_project_on_apply():
    fetish_unlock_exhibition_serum()


def basic_attention_reduction_project_requirement():
    if not get_fetish_basic_serum():
        return "???"
    if get_fetish_basic_serum().mastery_level >= 5.0:
        return True
    return "Low Trait Mastery (> 5)"

def anal_incest_project_requirement():
    if not get_fetish_anal_serum():
        return "???"
    if get_fetish_anal_serum().mastery_level >= 3.0:
        return True
    return "Low Trait Mastery (> 3)"

def anal_attention_reduction_project_requirement():
    if not get_fetish_anal_serum():
        return "???"
    if get_fetish_anal_serum().mastery_level >= 5.0:
        return True
    return "Low Trait Mastery (> 5)"

def anal_fetish_increase_project_requirement():
    if not get_fetish_anal_serum():
        return "???"
    if mc.business.it_director and mc.business.it_director.has_anal_fetish:
        return True
    return "IT Girl Anal Fetish"

def breeder_submission_project_requirement():
    if not get_fetish_breeding_serum():
        return "???"
    if get_fetish_breeding_serum().mastery_level >= 3.0:
        return True
    return "Low Trait Mastery (> 3)"

def breeder_attention_reduction_project_requirement():
    if not get_fetish_breeding_serum():
        return "???"
    if get_fetish_breeding_serum().mastery_level >= 5.0:
        return True
    return "Low Trait Mastery (> 5)"

def breeder_fetish_increase_project_requirement():
    if not get_fetish_breeding_serum():
        return "???"
    if mc.business.it_director and mc.business.it_director.has_breeding_fetish:
        return True
    return "IT Girl Breeding Fetish"

def cum_thirst_project_requirement():
    if not get_fetish_cum_serum():
        return "???"
    if get_fetish_cum_serum().mastery_level >= 3.0:
        return True
    return "Low Trait Mastery (> 3)"

def cum_attention_reduction_project_requirement():
    if not get_fetish_cum_serum():
        return "???"
    if get_fetish_cum_serum().mastery_level >= 5.0:
        return True
    return "Low Trait Master (> 5)"

def cum_fetish_increase_project_requirement():
    if not get_fetish_cum_serum():
        return "???"
    if mc.business.it_director and mc.business.it_director.has_cum_fetish:
        return True
    return "IT Girl Cum Fetish"

def exhibition_cheating_project_requirement():
    if not get_fetish_exhibition_serum():
        return "???"
    if get_fetish_exhibition_serum().mastery_level >= 3.0:
        return True
    return "Low Trait Mastery (> 3)"

def exhibition_attention_reduction_project_requirement():
    if not get_fetish_exhibition_serum():
        return "???"
    if get_fetish_exhibition_serum().mastery_level >= 5.0:
        return True
    return "Low Trait Mastery (> 5)"

def exhibition_fetish_increase_project_requirement():
    if not get_fetish_exhibition_serum():
        return "???"
    if mc.business.it_director and mc.business.it_director.has_exhibition_fetish:
        return True
    return "IT Girl Exhibition Fetish"


basic_clarity_reduction_project = IT_Project(name = "Chemical Adaptation",
    desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = basic_clarity_reduction_on_apply,   #Heckin typos. too lazy to fix, this is research_added, not clarity
    on_remove_function = basic_clarity_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "basic",
    tier = 10)

basic_attention_reduction_project = IT_Project(name = "Deceptive Programming",
    desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
    cost = 0,
    requirement = basic_attention_reduction_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = basic_attention_reduction_on_apply,
    on_remove_function = basic_attention_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "basic",
    tier = 30)

anal_clarity_reduction_project = IT_Project(name = "Anal Chemical Adaptation",
    desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = anal_clarity_reduction_on_apply,
    on_remove_function = anal_clarity_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "anal",
    tier = 10)

anal_incest_project = IT_Project(name = "Familial Anal Adaptation",
    desc = "Members of family may be more willing to accept acts of anal sex. Adds Incest to opinions increased by the Anal Proclivity Nanobots.",
    cost = 0,
    requirement = anal_incest_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = anal_incest_project_on_apply,
    on_remove_function = anal_incest_project_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "anal",
    tier = 20)

anal_attention_reduction_project = IT_Project(name = "Evasive Programming",
    desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
    cost = 0,
    requirement = anal_attention_reduction_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = anal_attention_reduction_on_apply,
    on_remove_function = anal_attention_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "anal",
    tier = 30)

anal_fetish_increase_project = IT_Project(name = "Anal Fetish Prioritization",
    desc = "Greatly increases the chances of causing an anal fetish after exposure.",
    cost = 0,
    requirement = anal_fetish_increase_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 250,
    category = "anal",
    tier = 40)

breeder_clarity_reduction_project = IT_Project(name = "Breeding Chemical Adaptation",
    desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = breeder_clarity_reduction_on_apply,
    on_remove_function = breeder_clarity_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "breeder",
    tier = 10)

breeder_submission_project = IT_Project(name = "Submissive Breeder Adaptation",
    desc = "Encourages breeding as an active form of submission. Adds being submissive to the list of opinions increased by Reproduction Proclivity Nanobots.",
    cost = 0,
    requirement = breeder_submission_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = breeder_submission_project_on_apply,
    on_remove_function = breeder_submission_project_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "breeder",
    tier = 20)

breeder_attention_reduction_project = IT_Project(name = "Evasive Programming",
    desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
    cost = 0,
    requirement = breeder_attention_reduction_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = breeder_attention_reduction_on_apply,
    on_remove_function = breeder_attention_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "breeder",
    tier = 30)

breeder_fetish_increase_project = IT_Project(name = "Breeding Fetish Prioritization",
    desc = "Greatly increases the chances of causing a breeding fetish after exposure.",
    cost = 0,
    requirement = breeder_fetish_increase_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 250,
    category = "breeder",
    tier = 40)

cum_clarity_reduction_project = IT_Project(name = "Cum Chemical Adaptation",
    desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = cum_clarity_reduction_on_apply,
    on_remove_function = cum_clarity_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "cum",
    tier = 10)

cum_thirst_project = IT_Project(name = "Cum Thirst Adaptation",
    desc = "Sexual fixation on cum can inspire a powerful thirst, motivating girls to take a more active role in getting their fix. Adds taking control to the list of opinions increased by Semen Proclivity Nanobots.",
    cost = 0,
    requirement = cum_thirst_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = cum_thirst_project_on_apply,
    on_remove_function = cum_thirst_project_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "cum",
    tier = 20)

cum_attention_reduction_project = IT_Project(name = "Evasive Programming",
    desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
    cost = 0,
    requirement = cum_attention_reduction_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = cum_attention_reduction_on_apply,
    on_remove_function = cum_attention_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "cum",
    tier = 30)

cum_fetish_increase_project = IT_Project(name = "Cum Fetish Prioritization",
    desc = "Greatly increases the chances of causing a cum fetish after exposure.",
    cost = 0,
    requirement = cum_fetish_increase_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 250,
    category = "cum",
    tier = 40)

exhibition_clarity_reduction_project = IT_Project(name = "Exhibition Chemical Adaptation",
    desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = exhibition_clarity_reduction_on_apply,
    on_remove_function = exhibition_clarity_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "exhibition",
    tier = 10)

exhibition_cheating_project = IT_Project(name = "Risky Behaviour Adaptation",
    desc = "Exhibitionism often encourages risky behaviour. Adds cheating on men to the list of opinions increased by Social Sexual Proclivity Nanobots.",
    cost = 0,
    requirement = exhibition_cheating_project_requirement,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = exhibition_cheating_project_on_apply,
    on_remove_function = exhibition_cheating_project_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 150,
    category = "exhibition",
    tier = 20)

exhibition_attention_reduction_project = IT_Project(name = "Evasive Programming",
    desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
    cost = 0,
    requirement = exhibition_attention_reduction_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = exhibition_attention_reduction_on_apply,
    on_remove_function = exhibition_attention_reduction_on_remove,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 200,
    category = "exhibition",
    tier = 30)

exhibition_fetish_increase_project = IT_Project(name = "Exhibitionism Fetish Prioritization",
    desc = "Greatly increases the chances of causing an exhibitionist fetish after exposure.",
    cost = 0,
    requirement = exhibition_fetish_increase_project_requirement,
    toggleable = True,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = None,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 250,
    category = "exhibition",
    tier = 40)

nanobot_IT_project_list: list[IT_Project] = [
    basic_clarity_reduction_project,
    basic_attention_reduction_project,
    anal_clarity_reduction_project,
    anal_incest_project,
    anal_attention_reduction_project,
    anal_fetish_increase_project,
    breeder_clarity_reduction_project,
    breeder_submission_project,
    breeder_attention_reduction_project,
    breeder_fetish_increase_project,
    cum_clarity_reduction_project,
    cum_thirst_project,
    cum_attention_reduction_project,
    cum_fetish_increase_project,
    exhibition_clarity_reduction_project,
    exhibition_cheating_project,
    exhibition_attention_reduction_project,
    exhibition_fetish_increase_project,
]

anal_unlock_project = IT_Project(name = "Anal Program",
    desc = "A new nanobot program that encourages anal stimulation.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = anal_program_unlock_project_on_apply,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "anal",
    tier = 0)

breeder_unlock_project = IT_Project(name = "Breeding Program",
    desc = "A new nanobot program that encourages breeding behaviours.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = breeder_program_unlock_project_on_apply,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "breeder",
    tier = 0)

cum_unlock_project = IT_Project(name = "Cum Program",
    desc = "A new nanobot program that encourages cum exposure.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = cum_program_unlock_project_on_apply,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "cum",
    tier = 0)

exhibition_unlock_project = IT_Project(name = "Exhibitionism Program",
    desc = "A new nanobot program that encourages exhibitionism.",
    cost = 0,
    requirement = None,
    toggleable = False,
    on_buy_function = None,
    extra_arguments = None,
    on_apply_function = exhibition_program_unlock_project_on_apply,
    on_remove_function = None,
    on_turn_function = None,
    on_move_function = None,
    on_day_function = None,
    dependant_policies = None,
    project_progress = 0,
    project_cost = 100,
    category = "exhibition",
    tier = 0)

nanobot_unlock_project_list = [
    anal_unlock_project,
    breeder_unlock_project,
    cum_unlock_project,
    exhibition_unlock_project
]

def IT_get_nanobot_projects(category: str) -> list[IT_Project]:
    return sorted([x for x in nanobot_IT_project_list if x.category == category], key = lambda x: (x.tier, x.name))

def update_fetish_unlock_list():
    def _get_project_by_name(name: str):
        return next((x for x in mc.business.IT_projects if x.name == name), None)

    projects = [anal_incest_project, breeder_submission_project, cum_thirst_project, exhibition_cheating_project]
    for proj in projects:
        active_proj = _get_project_by_name(proj.name)
        if active_proj:
            active_proj.on_apply_function()
