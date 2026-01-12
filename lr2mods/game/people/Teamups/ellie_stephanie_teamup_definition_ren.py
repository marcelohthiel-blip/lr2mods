from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("ellie_stephanie_teamup_progression_scene_init")

def ellie_stephanie_teamup_progression_scene_0_req():    #Requirements for the basic scene. Should almost always be true.
    return True

def ellie_stephanie_teamup_progression_scene_1_req():    #Requirements for the second stage.
    #return the_group[0].sluttiness > 20
    return

def ellie_stephanie_teamup_progression_scene_action_req(person: Person):
    return (
        time_of_day == 1
        and day % 7 == 2
        and mc.business.head_researcher
        and mc.business.head_researcher.is_available
        and person.is_available
        and person.has_event_delay("testing_teamup", 1)
    )

def ellie_stephanie_teamup_unit_test_func(the_group):
    for person in the_group:
        person.change_slut(30)
        person.change_energy(200)
    mc.change_energy(200)

def ellie_stephanie_teamup_progression_scene_compile_scenes(the_progression_scene):
    #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
    the_progression_scene.start_scene_list = ["ellie_stephanie_teamup_progression_scene_intro_0", "ellie_stephanie_teamup_progression_scene_intro_1"]
    the_progression_scene.req_list = [ellie_stephanie_teamup_progression_scene_0_req, ellie_stephanie_teamup_progression_scene_1_req]
    the_progression_scene.trans_list = ["ellie_stephanie_teamup_trans_scene_0", "ellie_stephanie_teamup_trans_scene_1"]
    the_progression_scene.final_scene_list = ["ellie_stephanie_teamup_progression_scene_scene_0", "ellie_stephanie_teamup_progression_scene_scene_1"]

ellie_stephanie_teamup_progression_scene_action = Action("Ellie Stephanie Testing Teamup", ellie_stephanie_teamup_progression_scene_action_req, "ellie_stephanie_teamup_progression_scene_action_label", priority = 30)

def ellie_stephanie_teamup_progression_scene_init():  #Run this during init only
    global ellie_stephanie_teamup_progression_scene
    ellie_stephanie_teamup_progression_scene = Progression_Scene(
        compile_scenes = ellie_stephanie_teamup_progression_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "ellie_stephanie_teamup_progression_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "ellie_stephanie_teamup_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = ellie_stephanie_teamup_progression_scene_action,      #The action used to call for this progression scene.
        choice_scene = "ellie_stephanie_teamup_progression_scene_choice",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = True,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = ellie_stephanie_teamup_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = True,    # Advance time in the scenes themselves for now...
        is_multiple_choice = True, #If MC can choose what final scene he wants
        multiple_choice_scene = "ellie_stephanie_teamup_progression_multi_choice_scene",   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    ellie_stephanie_teamup_progression_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(ellie_stephanie_teamup_progression_scene)
