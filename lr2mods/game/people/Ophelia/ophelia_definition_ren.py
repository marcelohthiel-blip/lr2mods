from __future__ import annotations
import builtins
import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import light_eye_shadow, modern_glasses, lipstick, messy_hair
from game.personality_types._personality_definitions_ren import wild_personality, wild_titles, wild_player_titles
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, salon_manager
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import mall_salon
from game.major_game_classes.game_logic.Position_ren import Position
from game.people.Ophelia.ophelia_role_definition_ren import add_ophelia_takes_over_hair_salon, get_salon_manager_role_actions, ophelia_get_chocolate_gift_unlock, ophelia_get_coworker_overheard, ophelia_get_first_date_finished, ophelia_get_first_date_planned, ophelia_get_special_bj_unlocked, ophelia_is_over_her_ex_day
from game.sex_positions._position_definitions_ren import blowjob, deepthroat, skull_fuck, ophelia_blowjob

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_salon_manager_character")
salon_style_cost = builtins.int(60)
salon_dye_cost = builtins.int(30)

salon_total_cost = salon_style_cost + salon_dye_cost

def salon_manager_titles(person: Person) -> list[str]:
    return wild_titles(person)

def salon_manager_possessive_titles(person: Person) -> list[str]:
    valid_possessive_titles = []
    valid_possessive_titles.append(person.name)
    valid_possessive_titles.append("your stylist")
    if person.sluttiness > 40:
        valid_possessive_titles.append("the salon slut")
    if person.sluttiness > 50:
        valid_possessive_titles.append("your intimate stylist")
    if ophelia_get_special_bj_unlocked():
        valid_possessive_titles.append("your blowjob prodigy")
    return valid_possessive_titles

def salon_manager_player_titles(person: Person):
    return wild_player_titles(person)

def create_salon_manager_character():
    salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")
    # Place the stylist character so it is in a room in the world.
    ophelia_base_outfit = Outfit("Ophelia's base accessories")
    ophelia_base_outfit.add_accessory(light_eye_shadow.get_copy(), [.15, .15, .15, 0.5])
    ophelia_base_outfit.add_accessory(modern_glasses.get_copy(), [.15, .15, .15, 0.95])
    ophelia_base_outfit.add_accessory(lipstick.get_copy(), [.5, .28, .37, 0.4])

    salon_manager_role = Role("Salon Manager", get_salon_manager_role_actions(), hidden = True)

    salon_job = JobDefinition("Hair Stylist", salon_manager_role, mall_salon, day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2, 3])
    salon_job.set_schedule(mall_salon, day_slots = 5, time_slots = [1, 2])

    salon_manager_personality = Personality("salon_manager", default_prefix = wild_personality.default_prefix, #Based on relaxed style personality
        common_likes = ["skirts", "small talk", "the weekend", "the colour purple", "makeup", "hiking", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "anal creampies", "showing her tits", "showing her ass", "being submissive", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour yellow", "supply work", "conservative outfits", "work uniforms", "pants", "boots"],
        common_sexy_dislikes = ["taking control", "bareback sex"],
        titles_function = salon_manager_titles, possessive_titles_function = salon_manager_possessive_titles, player_titles_function = salon_manager_player_titles)

    global salon_manager
    salon_manager = make_person(name = "Ophelia", last_name = "von Friseur", age = renpy.random.randint(26, 35), body_type = "thin_body", skin="tan", face_style = "Face_11", hair_colour = ["barn red", [.486, .039, .007, 1]], hair_style = messy_hair,
        personality = salon_manager_personality, starting_wardrobe = salon_wardrobe, eyes="green", sex_skill_array = [1, 5, 3, 1], sluttiness = 10, job = salon_job,
        possessive_title = "your stylist", relationship = "Single", base_outfit = ophelia_base_outfit,
        forced_opinions = [
            ["dark chocolate", 2, False],
            ["hiking", 2, False],
            ["the colour red", 2, False],
            ["the colour yellow", 1, False]],
        forced_sexy_opinions = [
            ["cum facials", 2, False], # it's good for the skin
            ["giving blowjobs", 2, False],
            ["skimpy outfits", 1, False], # Fashion forward
            ["vaginal sex", 0, False]],
        serum_tolerance = 3, type = 'story')   # when she hates vaginal it causes issues in story-line (so set to neutral)

    # create home for salon manager
    salon_manager.generate_home()
    salon_manager.home.add_person(salon_manager)
    # hide her until we need her
    salon_manager.set_override_schedule(salon_manager.home)
    salon_manager.event_triggers_dict["ex_name"] = Person.get_random_male_name()
    add_ophelia_takes_over_hair_salon()

def build_salon_manger_title_choice_menu(person: Person):
    title_tuple = []
    for title in person.get_player_titles():
        title_tuple.append((title, title))
    return renpy.display_menu(title_tuple, True, "Choice")


##############
# Story Info #
##############
def ophelia_story_character_description():
    return "A troubled young woman who took over the hair salon and is trying to make a name for herself."

# def ophelia_story_teamup_list() -> dict[int, tuple[Person, str]]:
#     return {
#     }

def ophelia_story_other_list():
    other_story_list = {}

    if not ophelia_get_coworker_overheard():
        other_story_list[0] = "Get to know her by visiting the salon."
        return other_story_list
    if not ophelia_get_chocolate_gift_unlock():
        other_story_list[0] = "Try talking with her to see what she likes."
        return other_story_list

    other_story_list[0] = "You discovered she likes dark chocolate."

    if not ophelia_get_first_date_planned():
        other_story_list[1] = "Try corrupting her and figure out what is going in her life."
        return other_story_list
    if not ophelia_get_first_date_finished():
        other_story_list[1] = "You are going on a date, let's see how it goes."
        return other_story_list
    if not ophelia_is_over_her_ex_day():
        other_story_list[1] = "You had an awkward date with her. She is still not over her ex, wait until she's ready to talk."
        return other_story_list

    other_story_list[1] = "She is finally over her ex and ready to move on with her life."

    other_story_list[2] = "Other possibilities will open up when you get to know [candace.fname] better."
    return other_story_list


####################
# Position Filters #
####################

def ophelia_foreplay_position_filter(foreplay_position: Position):
    return True

def ophelia_oral_position_filter(oral_position: Position):
    if ophelia_get_special_bj_unlocked():
        filter_out = [blowjob, deepthroat, skull_fuck]
        return oral_position not in filter_out
    return False

def ophelia_vaginal_position_filter(vaginal_position: Position):
    return ophelia_get_first_date_finished()

def ophelia_anal_position_filter(anal_position: Position):
    return ophelia_is_over_her_ex_day() > 0

def ophelia_oral_position_info():
    return "Complete the make ex jealous event"

def ophelia_vaginal_position_info():
    return "Complete the first date event"

def ophelia_anal_position_info():
    return "Wait until she is over her ex"

def ophelia_unique_sex_positions(person: Person, prohibit_tags = None) -> list[tuple[Position, int]]:
    if prohibit_tags is None:
        prohibit_tags = []

    positions = []
    if ophelia_get_special_bj_unlocked() and "Oral" not in prohibit_tags:
        positions.append((ophelia_blowjob, 1))
    return positions
