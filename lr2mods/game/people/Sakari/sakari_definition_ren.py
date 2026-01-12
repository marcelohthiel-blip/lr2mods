from __future__ import annotations
from game.major_game_classes.game_logic.Role_ren import Role
from game.text_tags.maori_modifier_ren import maori_accent
from game.helper_functions.random_generation_functions_ren import make_person
from game.clothing_lists_ren import garnet_ring, lipstick, modern_glasses, bald_hair
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.game_roles._role_definitions_ren import critical_job_role
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, sakari, kaya
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.clothing_related.Outfit_ren import Outfit

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_sakari_character")

def sakari_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)

    return valid_titles

def sakari_possessive_titles(person: Person):
    valid_possessive_titles = [person.title]
    return valid_possessive_titles

def sakari_player_titles(person: Person):
    return [mc.name]

def create_sakari_character():
    sakari_base_outfit = Outfit("sakari's base accessories")
    sakari_base_outfit.add_accessory(lipstick.get_copy(), [.15, .15, .15, 0.5])
    sakari_base_outfit.add_accessory(garnet_ring.get_copy(), [.82, .15, .15, 0.95])
    sakari_base_outfit.add_accessory(modern_glasses.get_copy(), [.15, .15, .15, 0.95])

    sakari_personality = Personality("sakari", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
        common_dislikes = ["pants", "working", "the colour yellow", "conservative outfits", "sports"],
        common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything", "polyamory"],
        titles_function = sakari_titles, possessive_titles_function = sakari_possessive_titles, player_titles_function = sakari_player_titles)

    sakari_job = JobDefinition("Clothing Store Owner", critical_job_role, job_location = None) # not schedule to work, fill work schedule as needed

    global sakari
    sakari = make_person(name = "Sakari", last_name = "Greene", age = 42, body_type = "thin_body", face_style = "Face_14", tits="C", height = 0.92, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = bald_hair, skin="tan",
        eyes = "brown", personality = sakari_personality, name_color = "#FFA500", job = sakari_job,
        stat_array = [1, 4, 4], skill_array = [1, 1, 3, 5, 1], sex_skill_array = [4, 2, 2, 2], sluttiness = 7, obedience_range = [100, 120], happiness = 88, love = 0,
        relationship = "Single", kids = 1, base_outfit = sakari_base_outfit,
        forced_opinions = [
            ["production work", 2, True],
            ["work uniforms", -1, False],
            ["flirting", 1, False],
            ["working", 1, False],
            ["the colour green", 2, False],
            ["pants", 1, False],
            ["the colour blue", -2, False],
            ["classical music", 1, False]],
        forced_sexy_opinions = [
            ["being submissive", 2, False],
            ["getting head", 1, False],
            ["drinking cum", -2, False],
            ["giving blowjobs", -1, False],
            ["creampies", 2, False]],
        serum_tolerance = 1, work_experience = 3, type = 'story')

    sakari.generate_home()
    sakari.set_schedule(sakari.home, time_slots = [0, 1, 2, 3, 4])   #Hide Sakari at home until we are ready to use her
    sakari.home.add_person(sakari)

    sakari.on_birth_control = False   # explicitly disable
    sakari.text_modifiers.append(maori_accent)

    # set relationships
    # town_relationships.update_relationship(nora, sakari, "Friend")
    # town_relationships.update_relationship(lily, sakari, "Rival")

##############
# Story Info #
##############

def sakari_story_character_description():
    return "A native woman who is dealing with a dire health issue. Lives with her daughter, [kaya.name]."

# def sakari_story_love_list():
#     love_story_list = {
#         0: "This story step has not yet been written."
#     }
#     return love_story_list

# def sakari_story_lust_list():
#     lust_story_list = {
#         0: "This story step has not yet been written."
#     }
#     return lust_story_list

# def sakari_story_obedience_list():
#     obedience_story_list = {
#         0: "This story step has not yet been written."
#     }
#     return obedience_story_list

def sakari_story_teamup_list() -> dict[int, tuple[Person, str]]:
    return {
        0: (kaya, "Hmm, [kaya.fname] is [sakari.fname]'s daughter... surely nothing could happen there... right?'")
    }

def sakari_story_other_list():
    return {
        0: "[sakari.fname] has started working at the clothing store again. Look for her there in the morning."
    }

####################
# Position Filters #
####################
