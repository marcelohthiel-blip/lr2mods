from __future__ import annotations
from game.people.Myrabelle.myra_role_definition_ren import myra_at_cafe, myra_can_train_focus
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import gaming_cafe
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, myra
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes
from game.map.map_code_ren import gaming_cafe_is_open

day = 0
time_of_day = 4
TIER_1_TIME_DELAY = 1
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("myra_focus_progression_scene_init")

def myra_train_focus_intro_requirement(person: Person):
    return (
        person.days_since_event("myra_fails_tournament") > TIER_1_TIME_DELAY
        and gaming_cafe_is_open()
        and person.is_at(gaming_cafe)
    )

def add_myra_train_focus_intro_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra needs help",
            myra_train_focus_intro_requirement,
            "myra_train_focus_intro_label",
            priority = 30)
    )
    myra.event_triggers_dict["has_failed_tournament"] = True
    myra.set_event_day("myra_fails_tournament")

def myra_train_focus_requirement(person: Person):
    if not (myra_can_train_focus() and person.is_at(gaming_cafe)):
        return False
    if person.days_since_event("focus_train_day") == 0:
        return "Trained focus too recently"
    return True

def add_myra_train_focus_action():
    myra.add_action(
        Action("Help Myra Train Focus {image=time_advance}", myra_train_focus_requirement, "myra_train_focus_label")
    )
    myra.event_triggers_dict["can_train_focus"] = True
    myra.set_event_day("focus_train_day", day - 1)    # unlock directly

def myra_focus_progression_scene_0_req():    #Requirements for the basic scene. Should almost always be true.
    return True

def myra_focus_progression_scene_1_req():    #Requirements for grope scene
    return myra.sluttiness > 20 and myra.focus >= 3

def myra_focus_progression_scene_2_req():    #Requirements for fingering
    return myra.sluttiness > 40 and myra.focus >= 4

def myra_focus_progression_scene_3_req():    #Requirements for assjob scene
    return myra.sluttiness > 60

def myra_focus_progression_scene_4_req():    #Requirements for anal
    return False
    # if myra.sluttiness > 80 and myra_lewd_cafe_open():
    #     return True
    # return False

def myra_focus_progression_scene_action_req(person: Person):  #Use this function to determine the requirement for when to actually run the scene itself.
    return myra.days_since_event("focus_train_day") > 0 and myra.is_at(gaming_cafe)

def myra_focus_unit_test_func(the_group):
    for person in the_group:
        person.change_slut(10)
        person.change_energy(200)
    mc.change_energy(200)

def myra_focus_progression_scene_compile_scenes(the_progression_scene):
    #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
    the_progression_scene.start_scene_list = ["myra_focus_progression_scene_intro_0", "myra_focus_progression_scene_intro_1", "myra_focus_progression_scene_intro_2", "myra_focus_progression_scene_intro_3", "myra_focus_progression_scene_intro_4"]
    the_progression_scene.req_list = [myra_focus_progression_scene_0_req, myra_focus_progression_scene_1_req, myra_focus_progression_scene_2_req, myra_focus_progression_scene_3_req, myra_focus_progression_scene_4_req]
    the_progression_scene.trans_list = ["myra_focus_trans_scene_0", "myra_focus_trans_scene_1", "myra_focus_trans_scene_2", "myra_focus_trans_scene_3", "myra_focus_trans_scene_4"]
    the_progression_scene.final_scene_list = ["myra_focus_progression_scene_0", "myra_focus_progression_scene_1", "myra_focus_progression_scene_2", "myra_focus_progression_scene_3", "myra_focus_progression_scene_4"]
    # the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

myra_focus_progression_scene_action = Action("Train her Focus", myra_focus_progression_scene_action_req, "myra_focus_progression_scene_action_label")

def myra_focus_progression_scene_init():  #Run this during init only
    global myra_focus_progression_scene
    myra_focus_progression_scene = Progression_Scene(
        compile_scenes = myra_focus_progression_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "myra_focus_progression_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "myra_focus_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = myra_focus_progression_scene_action,      #The action used to call for this progression scene
        choice_scene = "myra_focus_progression_scene_choice",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = False,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = myra_focus_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
        is_multiple_choice = False, #If MC can choose what final scene he wants
        multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    myra_focus_progression_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(myra_focus_progression_scene)
