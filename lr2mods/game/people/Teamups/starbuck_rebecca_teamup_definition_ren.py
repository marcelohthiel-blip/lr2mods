from __future__ import annotations
from game.sex_positions.threesome.Threesome_Position_ren import willing_to_threesome
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import sex_store, aunt_apartment
from game.major_game_classes.character_related.Person_ren import list_of_instantiation_functions, starbuck, aunt, Person, mc
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("starbuck_rebecca_teamup_init")
list_of_lingerie_colors = ["the colour red", "the colour green", "the colour blue", "the colour black", "the colour white", "the colour pink", "the colour purple", "the colour orange", "the colour yellow", "the colour brown"]


def starbuck_rebecca_teamup_setup_one_requirement(person: Person):
    return person.is_at(aunt_apartment)

def add_starbuck_rebecca_teamup_setup_one_action():
    aunt.add_unique_on_talk_event(
        Action("Starbuck rebecca teamup setup one", starbuck_rebecca_teamup_setup_one_requirement, "starbuck_rebecca_teamup_setup_one_label", priority = 30)
    )


def starbuck_rebecca_teamup_setup_two_requirement(person: Person):
    return person.is_at(sex_store)

def add_starbuck_rebecca_teamup_setup_two_action():
    starbuck.add_unique_on_talk_event(
        Action("Starbuck rebecca teamup setup two", starbuck_rebecca_teamup_setup_two_requirement, "starbuck_rebecca_teamup_setup_two_label", priority = 30)
    )

def starbuck_rebecca_teamup_intro_requirement():
    return day % 7 == 4 and time_of_day == 1

def add_starbuck_rebecca_teamup_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Starbuck rebecca teamup intro", starbuck_rebecca_teamup_intro_requirement, "starbuck_rebecca_teamup_intro_action_label")
    )


def starbuck_rebecca_teamup_0_req():
    return True

def starbuck_rebecca_teamup_1_req():
    return (
        starbuck.sluttiness > 40
        and aunt.sluttiness > 40
    )

def starbuck_rebecca_teamup_2_req():
    return False
    return (
        starbuck.sluttiness > 60
        and aunt.sluttiness > 60
    )

def starbuck_rebecca_teamup_3_req():
    return False
    return (
        starbuck.sluttiness > 80
        and aunt.sluttiness > 80
    )

def starbuck_rebecca_teamup_4_req():
    return False
    return willing_to_threesome(starbuck, aunt)

def starbuck_rebecca_teamup_action_req(person: Person):
    return (
        day % 7 == 4
        and time_of_day == 1
        and person.is_at(sex_store)
        and aunt.is_at(sex_store)
    )

def starbuck_rebecca_teamup_compile_scenes(the_teamup):
    the_teamup.start_scene_list = ["starbuck_rebecca_teamup_intro_0"]
    the_teamup.req_list = [starbuck_rebecca_teamup_0_req, starbuck_rebecca_teamup_1_req, starbuck_rebecca_teamup_2_req, starbuck_rebecca_teamup_3_req, starbuck_rebecca_teamup_4_req]
    the_teamup.trans_list = ["starbuck_rebecca_trans_scene_0", "starbuck_rebecca_trans_scene_1", "starbuck_rebecca_trans_scene_2", "starbuck_rebecca_trans_scene_3", "starbuck_rebecca_trans_scene_4"]
    the_teamup.final_scene_list = ["starbuck_rebecca_teamup_scene_0", "starbuck_rebecca_teamup_scene_1", "starbuck_rebecca_teamup_scene_2", "starbuck_rebecca_teamup_scene_3", "starbuck_rebecca_teamup_scene_4"]

starbuck_rebecca_teamup_action = Action("Starbuck and Rebecca Teamup", starbuck_rebecca_teamup_action_req, "starbuck_rebecca_teamup_action_label", priority = 30)

def starbuck_rebecca_teamup_init():
    global starbuck_rebecca_teamup
    starbuck_rebecca_teamup = Progression_Scene(
        compile_scenes = starbuck_rebecca_teamup_compile_scenes,
        start_scene_list = [],
        req_list = [],
        trans_list = [],
        final_scene_list = [],
        intro_scene = "starbuck_rebecca_teamup_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "starbuck_rebecca_teamup_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = starbuck_rebecca_teamup_action,      #The action used to call for this progression scene.
        choice_scene = "starbuck_rebecca_teamup_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = True,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = None,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = True,
        is_multiple_choice = True, #If MC can choose what final scene he wants
        multiple_choice_scene = "starbuck_rebecca_teamup_multiple_choice_scene",   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])

    starbuck_rebecca_teamup.recompile_scenes()

    list_of_progression_scenes.append(starbuck_rebecca_teamup)
