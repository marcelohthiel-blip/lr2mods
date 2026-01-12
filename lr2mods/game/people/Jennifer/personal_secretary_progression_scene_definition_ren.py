from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import mc, list_of_instantiation_functions
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes
from game.sex_positions._position_definitions_ren import handjob, tit_fuck, skull_fuck, blowjob, cowgirl, anal_cowgirl, standing_doggy, anal_standing

day = 0
time_of_day = 4
"""renpy
init 5 python:
"""
list_of_instantiation_functions.append("personal_secretary_prog_scene_init")

def personal_secretary_prog_scene_0_req():
    return True

def personal_secretary_prog_scene_1_req():  #Tit Fuck
    return (
        mc.business.personal_secretary.has_large_tits
        and mc.business.personal_secretary.is_willing(tit_fuck, slut_bonus = 5)
    )

def personal_secretary_prog_scene_2_req():  #Blowjob
    return (
        mc.business.personal_secretary.is_willing(blowjob, slut_bonus = 5)
    )

def personal_secretary_prog_scene_3_req():  #Cowgirl
    if mc.business.personal_secretary.is_willing(cowgirl, slut_bonus = 5):
        return True
    return False

def personal_secretary_prog_scene_4_req(): #Bent over Desk
    if mc.business.personal_secretary.is_willing(standing_doggy, slut_bonus = 5) and mc.business.personal_secretary.obedience >= 140 and 3 in personal_secretary_prog_scene.scene_unlock_list:
        return True
    return False

def personal_secretary_prog_scene_5_req():  #Anal Cowgirl
    return False
    if mc.business.personal_secretary.is_willing(anal_cowgirl, slut_bonus = 5):
        return True
    return False

def personal_secretary_prog_scene_6_req():  #Anal bent over desk
    return False
    if mc.business.personal_secretary.is_willing(anal_standing, slut_bonus = 5) and mc.business.personal_secretary.obedience >= 160 and 5 in personal_secretary_prog_scene.scene_unlock_list:
        return True
    return False

def personal_secretary_prog_scene_7_req():  #Throat fuck
    return False
    if mc.business.personal_secretary.is_willing(skull_fuck) and mc.business.personal_secretary.obedience >= 180 and 2 in personal_secretary_prog_scene.scene_unlock_list:
        return True
    return False

def personal_secretary_prog_scene_action_req():
    if mc.business.personal_secretary is None:
        return False
    return (
        mc.business.has_event_delay("secretary_last_relief_day", 0)
        and mc.lust_tier >= mc.business.personal_secretary.event_triggers_dict.get("ps_lust_tier", 1)
        and mc.business.personal_secretary.is_willing(handjob)
        and mc.business.personal_secretary.is_at_office
    )

def personal_secretary_prog_scene_compile_scenes(the_progression_scene):
    the_progression_scene.start_scene_list = ["personal_secretary_prog_scene_intro_0"]
    the_progression_scene.req_list = [personal_secretary_prog_scene_0_req, personal_secretary_prog_scene_1_req, personal_secretary_prog_scene_2_req, personal_secretary_prog_scene_3_req, personal_secretary_prog_scene_4_req, personal_secretary_prog_scene_5_req, personal_secretary_prog_scene_6_req, personal_secretary_prog_scene_7_req]
    the_progression_scene.trans_list = ["personal_secretary_prog_trans_scene_0", "personal_secretary_prog_trans_scene_1", "personal_secretary_prog_trans_scene_2", "personal_secretary_prog_trans_scene_3", "personal_secretary_prog_trans_scene_4", "personal_secretary_prog_trans_scene_5", "personal_secretary_prog_trans_scene_6", "personal_secretary_prog_trans_scene_7"]
    the_progression_scene.final_scene_list = ["personal_secretary_prog_scene_scene_0", "personal_secretary_prog_scene_scene_1", "personal_secretary_prog_scene_scene_2", "personal_secretary_prog_scene_scene_3", "personal_secretary_prog_scene_scene_4", "personal_secretary_prog_scene_scene_5", "personal_secretary_prog_scene_scene_6", "personal_secretary_prog_scene_scene_7"]
    the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

personal_secretary_prog_scene_action = Action("Fool around with your secretary", personal_secretary_prog_scene_action_req, "personal_secretary_prog_scene_action_label")

def personal_secretary_prog_scene_init():
    global personal_secretary_prog_scene
    personal_secretary_prog_scene = Progression_Scene(
        compile_scenes = personal_secretary_prog_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "personal_secretary_prog_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "personal_secretary_prog_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = personal_secretary_prog_scene_action,      #The action used to call for this progression scene.
        choice_scene = "personal_secretary_prog_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = False,   #If this progression scene should run when encountering a person
        business_action = True,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = None,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = False,    #Currently this is broke. Advance time in the scenes themselves for now...
        is_multiple_choice = True, #If MC can choose what final scene he wants
        role_action = False, #Let's try putting this in as a role action and see if it shows progressions correctly.
        multiple_choice_scene = "personal_secretary_prog_scene_multiple_choice_scene",   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    personal_secretary_prog_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(personal_secretary_prog_scene)
