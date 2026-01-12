from __future__ import annotations
from game.sex_positions.threesome.Threesome_Position_ren import willing_to_threesome
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, myra, alexia
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("myra_alexia_teamup_scene_init")

def myra_alexia_teamup_scene_0_req():    #Requirements for the basic scene. Should almost always be true.
    return True

def myra_alexia_teamup_scene_1_req():    #Requirements for the second stage if not met use scene 1.
    if myra.has_taboo("touching_vagina") or alexia.has_taboo("touching_vagina"):
        return False
    if myra.opinion.being_fingered > -2 and alexia.opinion.being_fingered > -2:
        return myra.sluttiness >= 40 and alexia.sluttiness >= 40
    return False

def myra_alexia_teamup_scene_2_req():   #Requirements for the third stage if not met use scene 2
    if myra.has_taboo("licking_pussy") or alexia.has_taboo("licking_pussy"):
        return False
    if myra.opinion.getting_head > -2 and alexia.opinion.getting_head > -2:
        return myra.sluttiness >= 60 and alexia.sluttiness >= 60
    return False

def myra_alexia_teamup_scene_3_req():   #Requirements for the fourth stage if not met use scene 3
    if myra.has_taboo("vaginal_sex") or alexia.has_taboo("vaginal_sex"):
        return False
    if myra.opinion.vaginal_sex > -2 and alexia.opinion.vaginal_sex > -2:
        return myra.sluttiness >= 80 and alexia.sluttiness >= 80 and willing_to_threesome(myra, alexia)
    return False

def myra_alexia_teamup_scene_4_req():   #Requirements for the last stage if not met use scene 4
    return myra.is_free_use and alexia.is_free_use

def myra_alexia_teamup_scene_action_req(person: Person):
    return (
        day % 7 == 4
        and time_of_day == 3
        and person.is_available
        and alexia.is_available
    )

def myra_alexia_teamup_unit_test_func(the_group):
    person: Person
    for person in the_group:
        person.change_slut(20)
        person.change_energy(200)
    mc.change_energy(200)

def myra_alexia_teamup_scene_compile_scenes(the_progression_scene):
    #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
    the_progression_scene.start_scene_list = ["myra_alexia_teamup_scene_intro_0", "myra_alexia_teamup_scene_intro_1", "myra_alexia_teamup_scene_intro_2", "myra_alexia_teamup_scene_intro_3", "myra_alexia_teamup_scene_intro_4"]
    the_progression_scene.req_list = [myra_alexia_teamup_scene_0_req, myra_alexia_teamup_scene_1_req, myra_alexia_teamup_scene_2_req, myra_alexia_teamup_scene_3_req, myra_alexia_teamup_scene_4_req]
    the_progression_scene.trans_list = ["myra_alexia_teamup_trans_scene_0", "myra_alexia_teamup_trans_scene_1", "myra_alexia_teamup_trans_scene_2", "myra_alexia_teamup_trans_scene_3", "myra_alexia_teamup_trans_scene_4"]
    the_progression_scene.final_scene_list = ["myra_alexia_teamup_scene_scene_0", "myra_alexia_teamup_scene_scene_1", "myra_alexia_teamup_scene_scene_2", "myra_alexia_teamup_scene_scene_3", "myra_alexia_teamup_scene_scene_4"]
    the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

myra_alexia_teamup_scene_action = Action("Myra and Alexia's Game Night", myra_alexia_teamup_scene_action_req, "myra_alexia_teamup_scene_action_label", priority = 30)

def myra_alexia_teamup_scene_init():  #Run this during init only
    global myra_alexia_teamup_scene
    myra_alexia_teamup_scene = Progression_Scene(
        compile_scenes = myra_alexia_teamup_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "myra_alexia_teamup_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "myra_alexia_teamup_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = myra_alexia_teamup_scene_action,      #The action used to call for this progression scene.
        choice_scene = "myra_alexia_teamup_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = True,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = myra_alexia_teamup_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
        is_multiple_choice = False, #If MC can choose what final scene he wants
        multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    myra_alexia_teamup_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(myra_alexia_teamup_scene)
