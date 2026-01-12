from __future__ import annotations
from game.sex_positions.threesome.Threesome_Position_ren import willing_to_threesome
from game.map.MapHub_ren import university_hub
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, kaya, nora, mc
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""
list_of_instantiation_functions.append("kaya_nora_teamup_init")


def kaya_nora_teamup_0_req():
    return True

def kaya_nora_teamup_1_req():
    return kaya.sluttiness > 20 and nora.sluttiness > 20

def kaya_nora_teamup_2_req():
    return kaya.sluttiness >= 40 and nora.sluttiness >= 40

def kaya_nora_teamup_3_req():
    return kaya.sluttiness >= 60 and nora.sluttiness >= 60

def kaya_nora_teamup_4_req():
    return willing_to_threesome(kaya, nora)

def kaya_nora_teamup_action_req(person: Person):
    return (day % 7 == 3
        and time_of_day == 3
        and person.is_at(university_hub))

def kaya_nora_teamup_intro_action_req():
    return (day % 7 == 3
        and time_of_day == 3
        and kaya.is_at(university_hub))

def kaya_nora_teamup_compile_scenes(the_teamup):
    the_teamup.start_scene_list = ["kaya_nora_teamup_intro_0", "kaya_nora_teamup_intro_1", "kaya_nora_teamup_intro_2", "kaya_nora_teamup_intro_3", "kaya_nora_teamup_intro_4"]
    the_teamup.req_list = [kaya_nora_teamup_0_req, kaya_nora_teamup_1_req, kaya_nora_teamup_2_req, kaya_nora_teamup_3_req, kaya_nora_teamup_4_req]
    the_teamup.trans_list = ["kaya_nora_trans_scene_0", "kaya_nora_trans_scene_1", "kaya_nora_trans_scene_2", "kaya_nora_trans_scene_3", "kaya_nora_trans_scene_4"]
    the_teamup.final_scene_list = ["kaya_nora_teamup_scene_0", "kaya_nora_teamup_scene_1", "kaya_nora_teamup_scene_2", "kaya_nora_teamup_scene_3", "kaya_nora_teamup_scene_4"]

kaya_nora_teamup_action = Action("Kaya and Nora Lab Work", kaya_nora_teamup_action_req, "kaya_nora_teamup_action_label")    #Recurring

def add_kaya_nora_teamup_intro_action():
    mc.business.add_mandatory_crisis(
        Action("Kaya and Nora Lab Work", kaya_nora_teamup_intro_action_req, "kaya_nora_teamup_intro_action_label")
    )
    return

def kaya_nora_teamup_init():
    global kaya_nora_teamup
    kaya_nora_teamup = Progression_Scene(
        compile_scenes = kaya_nora_teamup_compile_scenes,
        start_scene_list = [],
        req_list = [],
        trans_list = [],
        final_scene_list = [],
        intro_scene = "kaya_nora_teamup_intro_scene",
        exit_scene = "kaya_nora_teamup_exit_scene",
        progression_scene_action = kaya_nora_teamup_action,
        choice_scene = "kaya_nora_teamup_labwork_choice",
        person_action = True,
        stage = -1)

    kaya_nora_teamup.recompile_scenes()

    list_of_progression_scenes.append(kaya_nora_teamup)
