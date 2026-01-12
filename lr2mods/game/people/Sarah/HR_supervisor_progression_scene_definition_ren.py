from __future__ import annotations
from game.people.Sarah.sarah_definition_ren import sarah_epic_tits_progress, sarah_get_sex_unlocked
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import mc, list_of_instantiation_functions, sarah
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("hr_director_prog_scene_init")


def hr_director_prog_scene_0_req():
    return True

def hr_director_prog_scene_1_req():
    if mc.business.hr_director != sarah:
        if mc.business.hr_director.has_large_tits and mc.business.hr_director.opinion.giving_tit_fucks > -2:
            return True
    else:
        return sarah_epic_tits_progress() > 1
    return False

def hr_director_prog_scene_2_req():
    if mc.business.hr_director.opinion.vaginal_sex == -2 or mc.business.hr_director.opinion.missionary_style == -2:
        return False
    if mc.business.hr_director.sluttiness >= 60 and (mc.business.hr_director != sarah or sarah_get_sex_unlocked()):
        return True
    return False

def hr_director_prog_scene_3_req():
    if mc.business.hr_director.opinion.vaginal_sex == -2 or mc.business.hr_director.opinion.doggy_style == -2:
        return False
    if mc.business.hr_director.sluttiness >= 70 and (mc.business.hr_director != sarah or sarah_get_sex_unlocked()):
        return mc.business.hr_director.obedience > 140
    return False

def hr_director_prog_scene_4_req(): #This is actually Sarah's 80 love event
    return (
        sarah.love >= 80
        and sarah.sluttiness >= 60
        and mc.business.hr_director == sarah
        and sarah.event_triggers_dict.get("stripclub_progress", 0) >= 1
    )

def hr_director_prog_scene_5_req():
    return False

def hr_director_prog_scene_6_req():
    return sarah.has_breeding_fetish and sarah.is_highly_fertile

def hr_director_prog_scene_7_req():
    return False

def hr_director_prog_scene_action_req():
    return True


def hr_director_prog_scene_compile_scenes(the_progression_scene):
    the_progression_scene.start_scene_list = ["hr_director_prog_scene_intro_0"]
    the_progression_scene.req_list = [hr_director_prog_scene_0_req, hr_director_prog_scene_1_req, hr_director_prog_scene_2_req, hr_director_prog_scene_3_req, hr_director_prog_scene_4_req, hr_director_prog_scene_5_req, hr_director_prog_scene_6_req, hr_director_prog_scene_7_req]
    the_progression_scene.trans_list = ["hr_director_prog_trans_scene_0", "hr_director_prog_trans_scene_1", "hr_director_prog_trans_scene_2", "hr_director_prog_trans_scene_3", "hr_director_prog_trans_scene_4", "hr_director_prog_trans_scene_5", "hr_director_prog_trans_scene_6", "hr_director_prog_trans_scene_7"]
    the_progression_scene.final_scene_list = ["hr_director_prog_scene_scene_0", "hr_director_prog_scene_scene_1", "hr_director_prog_scene_scene_2", "hr_director_prog_scene_scene_3", "hr_director_prog_scene_scene_4", "hr_director_prog_scene_scene_5", "hr_director_prog_scene_scene_6", "hr_director_prog_scene_scene_7"]
    the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

hr_director_prog_scene_action = Action("Hr Director Quality Time", hr_director_prog_scene_action_req, "hr_director_prog_scene_action_label")

def hr_director_prog_scene_init():
    global hr_director_prog_scene
    hr_director_prog_scene = Progression_Scene(
        compile_scenes = hr_director_prog_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "hr_director_prog_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "hr_director_prog_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = hr_director_prog_scene_action,      #The action used to call for this progression scene.
        choice_scene = "hr_director_prog_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = False,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = None,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = False,    #Currently this is broke. Advance time in the scenes themselves for now...
        is_multiple_choice = True, #If MC can choose what final scene he wants
        multiple_choice_scene = "hr_director_prog_scene_multiple_choice_scene",   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    hr_director_prog_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(hr_director_prog_scene)
