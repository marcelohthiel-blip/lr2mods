from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, stephanie, ashley
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("ashley_stephanie_progression_scene_init")


def ashley_stephanie_progression_scene_0_req():    #Requirements for the basic scene. Should almost always be true.
    return True

def ashley_stephanie_progression_scene_1_req():    #Requirements fo the second stage.
    return stephanie.sluttiness > 20

def ashley_stephanie_progression_scene_2_req():
    return stephanie.sluttiness > 40 and ashley.sluttiness > 20

def ashley_stephanie_progression_scene_action_req(person: Person):  #Use this function to determine the requirement for when to actually run the scene itself.
    return (
        day % 7 == 6
        and time_of_day == 1
        and person.is_available
        and person.is_at(stephanie.location)
    )

def ashley_stephanie_unit_test_func(the_group):
    for person in the_group:
        person.change_slut(30)
        person.change_energy(200)
    mc.change_energy(200)

def ashley_stephanie_progression_scene_compile_scenes(the_progression_scene):
    #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
    the_progression_scene.start_scene_list = ["ashley_stephanie_progression_scene_intro_0"]
    the_progression_scene.req_list = [ashley_stephanie_progression_scene_0_req, ashley_stephanie_progression_scene_1_req, ashley_stephanie_progression_scene_1_req]
    the_progression_scene.trans_list = ["ashley_stephanie_trans_scene_0", "ashley_stephanie_trans_scene_1", "ashley_stephanie_trans_scene_2"]
    the_progression_scene.final_scene_list = ["ashley_stephanie_progression_scene_0", "ashley_stephanie_progression_scene_1", "ashley_stephanie_progression_scene_2"]
    the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

ashley_stephanie_progression_scene_action = Action("Coffee with Ashley and Stephanie", ashley_stephanie_progression_scene_action_req, "ashley_stephanie_progression_scene_action_label", priority = 30)

def ashley_stephanie_progression_scene_init():  #Run this during init only
    global ashley_stephanie_progression_scene
    ashley_stephanie_progression_scene = Progression_Scene(
        compile_scenes = ashley_stephanie_progression_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "ashley_stephanie_progression_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "ashley_stephanie_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = ashley_stephanie_progression_scene_action,      #The action used to call for this progression scene.
        choice_scene = "ashley_stephanie_progression_scene_choice",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = True,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = ashley_stephanie_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
        is_multiple_choice = False, #If MC can choose what final scene he wants
        multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    ashley_stephanie_progression_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(ashley_stephanie_progression_scene)
