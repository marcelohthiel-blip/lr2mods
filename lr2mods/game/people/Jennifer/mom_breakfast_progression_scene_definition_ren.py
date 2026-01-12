from __future__ import annotations
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import mc, list_of_instantiation_functions, mom
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("mom_breakfast_prog_scene_init")

def mom_breakfast_prog_scene_0_req():   #small talk
    return True

def mom_breakfast_prog_scene_1_req():   #striptease
    if mom.effective_sluttiness() >= 20:
        return True
    return False

def mom_breakfast_prog_scene_2_req():   #handjob
    if mom.event_triggers_dict.get("kissing_revisit_complete", False) and mom.effective_sluttiness() >= 30:
        return True
    return False

def mom_breakfast_prog_scene_3_req():   #blowjob
    if mom.effective_sluttiness() >= 50:
        return True
    return False

def mom_breakfast_prog_scene_4_req():   #reverse doggy
    if mom.event_triggers_dict.get("anal_revisit_complete", False) and mom.effective_sluttiness() >= 70:
        return True
    return False

def mom_breakfast_prog_scene_action_req():  #The intro event
    return (
        day % 7 != 5
        and mom.obedience > 120
        and mom.story_event_ready("obedience")
        and mom.is_available
        and mom.is_at_mc_house
    )

def mom_breakfast_prog_scene_mand_action_req(): #The morning mandatory action after requesting breakfast in bed
    return True

def add_mom_breakfast_prog_scene_mand_action():
    mc.business.add_mandatory_morning_crisis(
        Action("Breakfast in Bed", mom_breakfast_prog_scene_mand_action_req, "mom_breakfast_prog_scene_action_label")
    )

# def mom_breakfast_prog_scene_morning_crisis_req():  #The random morning crisis
#     if mom.days_since_event("breakfast_in_bed") >= (max(1, 10 - int((mom.obedience - 100)/10))):
#         if mom.progress.obedience_step >= 2:
#             return True
#         return False
#     return False

def mom_breakfast_prog_scene_compile_scenes(the_progression_scene):
    the_progression_scene.start_scene_list = ["mom_breakfast_prog_scene_intro_0"]
    the_progression_scene.req_list = [mom_breakfast_prog_scene_0_req, mom_breakfast_prog_scene_1_req, mom_breakfast_prog_scene_2_req, mom_breakfast_prog_scene_3_req, mom_breakfast_prog_scene_4_req]
    the_progression_scene.trans_list = ["mom_breakfast_prog_trans_scene_0", "mom_breakfast_prog_trans_scene_1", "mom_breakfast_prog_trans_scene_2", "mom_breakfast_prog_trans_scene_3", "mom_breakfast_prog_trans_scene_4"]
    the_progression_scene.final_scene_list = ["mom_breakfast_prog_scene_scene_0", "mom_breakfast_prog_scene_scene_1", "mom_breakfast_prog_scene_scene_2", "mom_breakfast_prog_scene_scene_3", "mom_breakfast_prog_scene_scene_4"]
    the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

mom_breakfast_prog_scene_action = Action("Breakfast in Bed", mom_breakfast_prog_scene_action_req, "mom_breakfast_prog_scene_action_label")  #Mandatory event
# mom_breakfast_prog_scene_crisis = Action("Breakfast in Bed", mom_breakfast_prog_scene_morning_crisis_req, "mom_breakfast_prog_scene_action_label")  #Random morning crisis

def mom_breakfast_prog_scene_init():
    global mom_breakfast_prog_scene
    mom_breakfast_prog_scene = Progression_Scene(
        compile_scenes = mom_breakfast_prog_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "mom_breakfast_prog_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "mom_breakfast_prog_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = mom_breakfast_prog_scene_action,      #The action used to call for this progression scene.
        choice_scene = "mom_breakfast_prog_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = False,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = True,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = None,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = False,    #Currently this is broke. Advance time in the scenes themselves for now...
        is_multiple_choice = False, #If MC can choose what final scene he wants
        multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    mom_breakfast_prog_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(mom_breakfast_prog_scene)
