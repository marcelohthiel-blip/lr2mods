from __future__ import annotations
import builtins
from operator import attrgetter
import renpy
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits, list_of_side_effects
from game.major_game_classes.serum_related.serums._serum_traits_T1_ren import volatile_reaction
from game.random_lists_ren import get_random_from_weighted_list
from game.bugfix_additions.ActionMod_ren import ActionMod, crisis_list
from game.sex_positions._position_definitions_ren import blowjob, doggy
from game.major_game_classes.character_related.Person_ren import Person, mc, town_relationships
from game.major_game_classes.character_related.scene_manager_ren import scene_manager, character_left
from game.major_game_classes.game_logic.Action_ren import Action
from game.people.Sarah.HR_supervisor_definition_ren import get_HR_director_tag

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def in_research_with_other():
    return (mc.is_at_office
        and mc.business.r_div.person_count > 0)

def in_production_with_other():
    return (mc.is_at_office
        and mc.business.p_div.person_count > 0)

def anyone_else_in_office(): #Returns true if there is anyone else at work with the mc.
    return mc.is_at_office and mc.business.number_of_employees_at_office > 0

def broken_AC_crisis_requirement():
    return in_production_with_other()

crisis_list.append(
    Action("Crisis Test", broken_AC_crisis_requirement, "broken_AC_crisis_label"))

def get_drink_crisis_requirement():
    return anyone_else_in_office() and mc.location.person_count > 0

crisis_list.append(
    Action("Getting a Drink", get_drink_crisis_requirement, "get_drink_crisis_label"))

def office_flirt_requirement():
    return anyone_else_in_office() and mc.location.person_count > 0

crisis_list.append(
    Action("Office Flirt Crisis", office_flirt_requirement, "office_flirt_label"))


def special_training_requirement():
    # no training in the first two weeks (low on cash)
    return (day > 14
        and mc.business.is_open_for_business
        and mc.business.employee_count > 2
        and mc.business.has_event_delay("special_training_day", TIER_1_TIME_DELAY)
        and special_training_employee() is not None)

def special_training_employee():
    return get_random_from_list([x for x in mc.business.employees_at_office if x.obedience > 110 and x.int > 1 and (mc.max_work_skills > x.hr_skill or mc.max_work_skills > x.supply_skill or mc.max_work_skills > x.market_skill or mc.max_work_skills > x.research_skill or mc.max_work_skills > x.production_skill)])

crisis_list.append(Action("Special Training Crisis", special_training_requirement, "special_training_crisis_label"))


def lab_accident_requirement():
    return (in_research_with_other()
        and isinstance(mc.business.active_research_design, SerumDesign)
        and mc.business.active_research_design.researched)

crisis_list.append(
    Action("Lab Accident Crisis", lab_accident_requirement, "lab_accident_crisis_label"))

def production_accident_requirement():
    return in_production_with_other() and mc.business.used_line_weight > 0

crisis_list.append(Action("Production Accident Crisis", production_accident_requirement, "production_accident_crisis_label"))


def extra_mastery_crisis_requirement():
    return (mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_at_office
        and mc.business.active_research_design
        and isinstance(mc.business.active_research_design, SerumTrait)
        and mc.business.active_research_design.researched)

crisis_list.append(
    Action("Mastery Boost", extra_mastery_crisis_requirement, "extra_mastery_crisis_label"))


def trait_for_side_effect_requirement():
    return (mc.is_at_office
        and mc.business.head_researcher
        and mc.business.head_researcher.is_at_office
        and mc.business.active_research_design
        and isinstance(mc.business.active_research_design, SerumDesign)
        and not mc.business.active_research_design.researched
        and not mc.business.active_research_design.has_trait(volatile_reaction))

def trait_for_side_effect_get_trait_and_side_effect(design: SerumDesign):
    list_of_valid_traits = []
    exclude_tags = []
    for trait in design.traits:
        exclude_tags.extend(trait.exclude_tags)

    for trait in list_of_traits:
        if trait.researched and trait not in design.traits and not trait.slots > 0 and not any(x for x in trait.exclude_tags if x in exclude_tags):
            list_of_valid_traits.append((trait, builtins.int(trait.mastery_level)))

    return (get_random_from_weighted_list(list_of_valid_traits), get_random_from_list(list_of_side_effects))

crisis_list.append(
    Action("Trait for Side Effect Crisis", trait_for_side_effect_requirement, "trait_for_side_effect_label"))

def water_spill_crisis_requirement():
    return anyone_else_in_office()

crisis_list.append(
    Action("Water Spill Crisis", water_spill_crisis_requirement, "water_spill_crisis_label"))


# reduced occurrence of this event and first trigger after first 2 weeks of gameplay
def home_fuck_crisis_requirement():
    return (day > 14
        and mc.is_in_bed
        and mc.business.has_event_delay("home_fuck_crisis", TIER_1_TIME_DELAY)
        and home_fuck_crisis_get_person() is not None)

def home_fuck_crisis_get_person():
    return get_random_from_list([x for x in mc.business.employee_list + mc.business.intern_list
        if x.is_available
            and x.sluttiness > 20
            and not x.is_family
            and (x.is_single or x.opinion.cheating_on_men > 0)])

crisis_list.append(
    Action("Home Fuck Crisis", home_fuck_crisis_requirement, "home_fuck_crisis_label"))


def invest_opportunity_crisis_requirement():
    return (mc.business.research_tier > 0
        and day % 7 > 1
        and mc.business.is_open_for_business
        and mc.is_at_office
        and mc.business.has_queued_crisis("invest_rep_visit_label"))

crisis_list.append(
    Action("Investment Opportunity", invest_opportunity_crisis_requirement, "invest_opportunity_crisis_label"))


def work_chat_crisis_requirement():
    return (mc.is_at_office
        and work_chat_crisis_get_person() is not None)

def work_chat_crisis_get_person():
    return get_random_from_list([x for x in mc.location.people if (x.is_employee or x.is_intern) and x.opinion.small_talk >= 0])

crisis_list.append(
    Action("Work Chat Crisis", work_chat_crisis_requirement, "work_chat_crisis_label"))


def cat_fight_crisis_requirement():
    #Be at work during work hours with at least two other people who have a poor relationship
    return (mc.is_at_office
        and any([x for x in town_relationships.get_business_relationships(["Rival", "Nemesis"])
            if x.person_a.is_at_office and x.person_b.is_at_office]))

def cat_fight_crisis_get_girls():
    the_relationship = get_random_from_list(
        [x for x in town_relationships.get_business_relationships(["Rival", "Nemesis"])
            if x.person_a.is_at_office and x.person_b.is_at_office])

    if the_relationship is None:
        return (None, None)

    if renpy.random.randint(0, 1) == 1: #Randomize the order so that repeated events with the same people alternate who is person_one and two.
        person_one = the_relationship.person_a
        person_two = the_relationship.person_b
    else:
        person_one = the_relationship.person_b
        person_two = the_relationship.person_a
    return (person_one, person_two)

crisis_list.append(
    Action("Cat Fight Crisis", cat_fight_crisis_requirement, "cat_fight_crisis_label"))


def research_reminder_crisis_requirement():
    return (mc.business.head_researcher
        and mc.business.head_researcher.is_at_office
        and not mc.business.active_research_design
        and mc.business.event_triggers_dict.get("no_research", 0) > 9
        and mc.business.has_event_delay("no_research_reminder", 10)  # max once every 10 days
        and any(x for x in list_of_traits if not x.researched))

research_reminder_action = ActionMod("Research Reminder Crisis", research_reminder_crisis_requirement, "research_reminder_crisis_label",
    menu_tooltip = "Your head researcher will inform you when no research is running (after a few days).", category = "Business", is_mandatory_crisis = True)

def add_research_reminder_crisis():
    mc.business.add_mandatory_crisis(
        Action("Research Reminder Crisis", research_reminder_crisis_requirement, "research_reminder_crisis_label")
    )

def daughter_work_crisis_requirement():
    # Requires you to have an employee over a certain age, with at least one kid, who hasn't been introduced to the game yet.
    # Requires you and her to be at work.
    # Requires you to have a free slot in the company
    return (mc.is_at_office
        and not mc.business.at_employee_limit
        and get_HR_director_tag("business_HR_relative_recruitment", 0) == 2
        and get_random_mother_from_company_with_children())

def get_random_mother_from_company_with_children():
    return get_random_from_list([x for x in mc.business.employees_at_office
        if x.age >= 34
            and not x.is_unique
            and not x.is_clone
            and x.kids - x.number_of_children_with_mc > 0
            and x.kids - x.number_of_children_with_mc > town_relationships.get_existing_child_count(x)])

crisis_list.append(
    Action("Daughter Work Crisis", daughter_work_crisis_requirement, "daughter_work_crisis_label"))


def horny_at_work_crisis_requirement():
    return (mc.is_at_office
        and mc.energy >= mc.max_energy // 2
        and mc.arousal_perc >= 50
        and mc.location.person_count > 0)

crisis_list.append(
    Action("Horny at work crisis", horny_at_work_crisis_requirement, "horny_at_work_crisis_label"))


#########################
# Crisis Helper Methods #
#########################

def broken_AC_crisis_get_watch_list_menu(person: Person):
    people_list = [x for x in mc.business.p_div.people if x is not person]
    people_list.insert(0, "Watch")
    return people_list

def broken_AC_crisis_get_sluttiest_person():
    if not mc.business.p_div.people:
        return None
    return max(mc.business.p_div.people, key=attrgetter('sluttiness'))

def broken_AC_crisis_update_stats(happiness, obedience):
    for person in mc.business.p_div.people:
        person.change_stats(happiness = happiness, obedience = obedience)

def broken_AC_crisis_update_sluttiness():
    clarity_change = 0
    for person in mc.business.p_div.people:
        person.change_slut(1 + person.opinion.not_wearing_anything, 30, add_to_log = False)
        if person.vagina_visible:
            clarity_change += 10
        elif person.tits_visible:
            clarity_change += 5
        elif person.underwear_visible:
            clarity_change += 3
    mc.change_locked_clarity(clarity_change)
    mc.log_event("All Production Staff: Sluttiness Affected", "float_text_pink")

def broken_ac_crisis_strip_other_girls(person: Person, girl: Person):
    for other_girl in (x for x in mc.business.p_div.people if x not in (person, girl)):
        scene_manager.add_actor(other_girl, display_transform = character_left)
        # only remove clothing, don't show it on screen
        removed_something = scene_manager.strip_actor_outfit_to_max_sluttiness(other_girl, temp_sluttiness_boost = 20)
        if removed_something:
            if other_girl.tits_visible:
                other_girl.break_taboo("bare_tits")
            if other_girl.vagina_visible:
                other_girl.break_taboo("bare_pussy")
            if (other_girl.are_panties_visible) or (other_girl.is_bra_visible):
                other_girl.break_taboo("underwear_nudity")
            other_girl.current_planned_outfit = other_girl.outfit
        else:
            scene_manager.update_actor(other_girl, emotion = "sad")
            renpy.say(None, f"{other_girl.display_name} glances at the other girls, but decides against taking off some clothes.")
        scene_manager.remove_actor(other_girl)


dict_work_skills = {
    "hr_skill": ["Human Resources", "hr_skill"],
    "market_skill": ["Marketing", "market_skill"],
    "research_skill": ["Research & Development", "research_skill"],
    "production_skill": ["Production", "production_skill"],
    "supply_skill": ["Supply Procurement", "supply_skill"]}

def build_seminar_improvement_menu(person: Person):
    work_seminar = [] # NOTE: We can allow seminars for both main and sex skills, e.g through introducing a company hosted seminar type.
    for skill in dict_work_skills.values():
        if getattr(person, skill[1]) < mc.max_work_skills:
            work_seminar.append((f"{skill[0]}\nCurrent: {getattr(person, skill[1])}", skill[1]))
    work_seminar.insert(0, "Work Skills")
    work_seminar.append(("Cancel", None))
    return [work_seminar]

def return_from_seminar_action_requirement():
    return mc.business.is_open_for_business and mc.is_at_office

def add_return_from_seminar_action(person: Person):
    return_from_seminar_action = Action("Return From Seminar Thank You", return_from_seminar_action_requirement, "return_from_seminar_action_label", args = person)
    mc.business.add_mandatory_crisis(return_from_seminar_action)


def invest_rep_visit_requirement(trigger_day):
    return (day == trigger_day
        and time_of_day in (1, 2, 3)
        and mc.is_at_office)

def add_invest_rep_visit_action(rep_name):
    mc.business.add_mandatory_crisis(
        Action("Investment Representative Visit", invest_rep_visit_requirement, "invest_rep_visit_label", args = rep_name, requirement_args = [day + 7 - (day % 7) + 1])
    )

def update_investor_payment():
    investor_modifier = next((x for x in mc.business.sales_multipliers if x[0] == "Investor Payment"), None)
    if not investor_modifier:
        mc.business.add_sales_multiplier("Investor Payment", 0.99)
    else:
        mc.business.update_sales_multiplier("Investor Payment", investor_modifier[1] - .01)

def horny_at_work_get_person_and_cause():
    potential_cause = []
    for person in mc.location.people:
        if person.outfit.outfit_slut_score >= 20:
            potential_cause.append((person, "slutty_outfit"))
        if person.has_large_tits:
            potential_cause.append((person, "large_tits"))
        if person.vagina_visible:
            potential_cause.append((person, "vagina_visible"))
        if person.tits_visible:
            potential_cause.append((person, "tits_visible"))

    if potential_cause:
        the_cause = get_random_from_list(potential_cause)
        return the_cause

    return (None, "nothing")

def horny_at_work_get_follower():
    potential_follower = []
    for person in mc.location.people:
        if person.sluttiness >= 30 and renpy.random.randint(0, 10) < person.focus:
            potential_follower.append(person)
    return get_random_from_list(potential_follower)

def horny_at_work_get_licker(helpful_people: list[Person]):
    licker = None
    for person in helpful_people:
        person.change_stats(obedience = 3, slut = 1)
        if person.has_cum_fetish and licker is None:
            licker = person
        if person.is_submissive and person.opinion.drinking_cum > 0 and licker is None:
            licker = person #The list was randomized, so even if you have multiple people who meet this criteria this should still end up random.
    return licker

def horny_at_work_strip_down(person: Person):
    for clothing in person.outfit.get_half_off_to_vagina_list():
        scene_manager.draw_animated_removal(person, clothing, half_off_instead = True)
        if person.vagina_available:
            renpy.say(None, f"You pull her {clothing.display_name} out of the way so you can get to her pussy.")
        else:
            renpy.say(None, f"You pull her {clothing.display_name} out of the way.")

def horny_at_work_get_people_sets():
    clarity_change = 0
    unhappy_people = [] #They're surprised/shocked/disgusted that you're doing this.
    neutral_people = [] #They're neither surprised that you're doing this, nor willing to come help out.
    masturbating_people = []
    helpful_people = [] #They're happy to come over and help you take care of your "needs"
    for person in mc.location.people:
        person.discover_opinion("public sex")
        if person.sluttiness < (30 - person.opinion.public_sex * 10) and (not person.has_story or not person.is_willing(blowjob, private = False)):
            unhappy_people.append(person)

        elif person.obedience > (130 - (person.opinion.being_submissive * 10)) and (not person.has_story or person.is_willing(doggy, private = False)):
            helpful_people.append(person)
            clarity_change += 10

        else:
            neutral_people.append(person)

    for person in neutral_people:
        if person.opinion.masturbating > 0 and person.sluttiness >= 40:
            masturbating_people.append(person)
            clarity_change += 10
        else:
            clarity_change += 5

    mc.change_locked_clarity(clarity_change)
    renpy.random.shuffle(unhappy_people)
    renpy.random.shuffle(neutral_people)
    renpy.random.shuffle(masturbating_people)
    renpy.random.shuffle(helpful_people)
    return (unhappy_people, neutral_people, masturbating_people, helpful_people)
