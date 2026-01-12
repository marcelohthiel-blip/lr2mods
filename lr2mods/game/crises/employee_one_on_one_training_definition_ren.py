import renpy
from game.bugfix_additions.ActionMod_ren import ActionMod
from game.helper_functions.convert_to_string_ren import opinion_score_to_string
from game.helper_functions.list_functions_ren import get_random_from_list
from game.main_character.perks.Perks_ren import Ability_Perk, Stat_Perk, perk_system
from game.major_game_classes.character_related.Person_ren import Person, mc

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
def one_on_one_training_requirement():
    return (mc.is_at_office
        and mc.business.employee_count > 3
        and any(x for x in mc.business.employees_at_office if x.obedience > 110 and x.int > 1 and (mc.hr_skill > x.hr_skill or mc.supply_skill > x.supply_skill or mc.market_skill > x.market_skill or mc.research_skill > x.research_skill or mc.production_skill > x.production_skill)))

def get_training_employee():
    return get_random_from_list([x for x in mc.business.employees_at_office if x.obedience > 110 and x.int > 1 and (mc.hr_skill > x.hr_skill or mc.supply_skill > x.supply_skill or mc.market_skill > x.market_skill or mc.research_skill > x.research_skill or mc.production_skill > x.production_skill)])

def one_on_one_update_skill(person: Person, attribute_name: str, opinion: str):
    mc_skill = getattr(mc, attribute_name)
    person_skill = getattr(person, attribute_name)
    increase = renpy.random.randint(1, mc_skill - person_skill)
    setattr(person, attribute_name, person_skill + increase)
    display_name = opinion.replace("work", "skill").title()
    mc.log_event(f"{person.display_name}: +{increase} {display_name}", "float_text_grey")
    person.increase_opinion_score(opinion)
    if perk_system.has_ability_perk("Those Who Can't, Teach"):
        if mc_skill < mc.max_work_skills:
            setattr(mc, attribute_name, mc_skill + 1)
            mc.log_event(f"You gained +1 {display_name} from Perk", "float_text_yellow")

def one_on_one_training_check_perks(attribute_name: str):
    if not perk_system.has_ability_perk("Those Who Can't, Teach"):
        perk_system.add_ability_perk(Ability_Perk(description = "When you teach someone else a skill, you also gain a skill point in that area.", active = False, usable = False), "Those Who Can't, Teach")
        renpy.say(None, "Teaching someone else has given you new insights into your own skills. You realise by teaching others, you increase you own mastery in a given skill set.")
        return

    if perk_system.has_stat_perk("Those Who Can, Do"):
        return

    if (getattr(mc, attribute_name) == mc.max_work_skills):
        perk_system.add_stat_perk(Stat_Perk(description = "Teaching others has raised your skill ceiling to new levels. +1 work skills cap", skill_cap = 1), "Those Who Can, Do")
        renpy.say(None, "Sharing with someone a skill you thought you had wholly mastered reveals a few final deficient areas. You feel like you can take your skills even further now.")
        mc.log_event("You gained +1 maximum work skills from Perk", "float_text_yellow")

one_on_one_action = ActionMod("One-on-One Training", one_on_one_training_requirement, "SB_one_on_one_label",
    menu_tooltip = "You give an employee on the job training.", category = "Business", is_crisis = True)
