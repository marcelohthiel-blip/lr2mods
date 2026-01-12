from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.clothing_lists_ren import twintail, shaved_pubes, colourful_bracelets
from game.game_roles._role_definitions_ren import critical_job_role, instapic_role, dikdok_role, onlyfans_role
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, student_job
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, town_relationships, emily, christina, iris
from game.major_game_classes.game_logic.Room_ren import mall_salon, mom_office_lobby

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_instantiation_functions.append("create_iris_character")

def iris_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)

    if person.primary_job.job_known:
        valid_titles.append("Fashionista")

    if person.onlyfans_known:
        valid_titles.append("Camslut")
    if person.dikdok_known:
        valid_titles.append("Camwhore")
    return valid_titles

def iris_possessive_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)

    if person.primary_job.job_known:
        valid_titles.append("your Fashionista")

    if person.sluttiness > 60:
        valid_titles.append("your slutty model")

    if person.sluttiness > 80:
        valid_titles.append("your sinfluencer")

    if person.onlyfans_known:
        valid_titles.append("your camslut")

    if person.dikdok_known:
        valid_titles.append("your personal porn star")
        valid_titles.append("your camwhore")
    return valid_titles

def iris_player_titles(person: Person):
    valid_titles = []
    if person.sluttiness > 60:
        valid_titles.append("Sugar Daddy")
    return valid_titles

def create_iris_character():
    ### IRIS ###
    #iris_wardrobe = wardrobe_from_xml("Iris_Wardrobe")
    iris_base = Outfit("Iris's accessories") #TODO: Decide what accessories we want her to haven
    iris_base.add_accessory(colourful_bracelets.get_copy(), [1.0, 0.84, 0, 0.95])

    influencer_job = JobDefinition("Influencer", critical_job_role, day_slots = [], time_slots = [])

    iris_personality = Personality("iris", relaxed_personality.default_prefix,
        common_likes = ["dresses", "the weekend", "the colour white", "makeup", "flirting"],
        common_sexy_likes = ["missionary style sex", "vaginal sex", "public sex", "sports", "cheating on men"],
        common_dislikes = ["working", "the colour orange"],
        common_sexy_dislikes = ["taking control", "giving handjobs", "incest", "bareback sex"],
        titles_function = iris_titles, possessive_titles_function = iris_possessive_titles, player_titles_function = iris_player_titles)

    global iris
    iris = make_person(name = "Iris", last_name = "Vandenberg", age_range = [21, 23], body_type = "thin_body", face_style = "Face_7", tits = "DD", height = 0.9, hair_colour = ["strawberry blonde", [0.644, 0.418, 0.273, 0.95]], hair_style = twintail, pubes_style = shaved_pubes, skin = "white",
        eyes = "green", personality = iris_personality, stat_array = [6, 2, 1], skill_array = [1, 4, 0, 0, 1], sex_skill_array = [4, 4, 0, 0], base_outfit = iris_base, job = influencer_job,
        sluttiness = 5, obedience = 80, happiness = 120, love = 0, relationship = "Single", kids = 0, suggestibility_range = [6, 12], start_home = emily.home,
        forced_opinions = [
            ["skirts", 2, False],
            ["high heels", 2, False],
            ["pants", -2, False],
            ["conservative outfits", -2, False]],
        forced_sexy_opinions = [
            ["skimpy outfits", 2, False],
            ["lingerie", 1, False],
            ["showing her tits", 2, False],
            ["showing her ass", 1, False]],
        work_experience = 1, type="story")

    iris.add_role(instapic_role)
    iris.add_role(dikdok_role)
    # iris.generate_home()
    iris.home.add_person(iris)
    iris.set_override_schedule(iris.home) #Hides her at home so she doesn't wander the city by accident.

    town_relationships.update_relationship(iris, emily, "Sister")
    town_relationships.update_relationship(iris, christina, "Mother", "Daughter")

def iris_init_schedule():
    iris.set_override_schedule(None)
    iris.set_schedule(iris.home, time_slots = [4])
    iris.change_job(student_job, is_primary = False)
    iris.set_schedule(mall_salon, day_slots = [5], time_slots = [2])
    iris.set_schedule(mom_office_lobby, day_slots = [0, 1, 2, 3, 4], time_slots = [3])
    return
