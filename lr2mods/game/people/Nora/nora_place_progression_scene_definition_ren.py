import renpy
from renpy import persistent
from game.major_game_classes.game_logic.Action_ren import Action
from game.main_character.perks.Perks_ren import perk_system
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, nora
from game.major_game_classes.character_related.Progression_Scene_ren import Progression_Scene, list_of_progression_scenes

day = 0
time_of_day = 4
"""renpy
init 5 python:
"""
list_of_instantiation_functions.append("nora_place_prog_scene_init")

def nora_place_prog_scene_0_req():
    return True

def nora_place_prog_scene_1_req():  #Endurance Test
    return (
        nora.love >= 40
        and nora.effective_sluttiness() >= 40
    )

def nora_place_prog_scene_2_req():  #Cowgirl
    return (
        nora.progress.lust_step >= 3
        and nora.effective_sluttiness() >= 60
    )

def nora_place_prog_scene_3_req():  #Breeding fetish
    return False
    if nora.has_breeding_fetish:
        return True
    return False

def nora_place_prog_scene_4_req(): #anal fetish
    return False
    if nora.has_anal_fetish:
        return True
    return False

def nora_place_prog_scene_5_req():  #Cum fetish
    return False
    if nora.has_cum_fetish:
        return True
    return False

def nora_place_prog_scene_6_req():  #exhibitionist?
    return False
    if nora.has_exhibition_fetish:
        return True
    return False

def nora_place_prog_scene_action_req(person: Person):
    if nora.progress.lust_step < 2:
        return False
    return (
        time_of_day == 4
        and nora.is_home
        and nora.energy > 50
        and persistent.mc_noncon_pref >= 1  #For now only have events if MC is willing to get dominated
    )

def nora_place_prog_scene_compile_scenes(the_progression_scene: Progression_Scene):
    the_progression_scene.start_scene_list = ["nora_place_prog_scene_intro_0"]
    the_progression_scene.req_list = [nora_place_prog_scene_0_req, nora_place_prog_scene_1_req, nora_place_prog_scene_2_req, nora_place_prog_scene_3_req, nora_place_prog_scene_4_req, nora_place_prog_scene_5_req, nora_place_prog_scene_6_req]
    the_progression_scene.trans_list = ["nora_place_prog_trans_scene_0", "nora_place_prog_trans_scene_1", "nora_place_prog_trans_scene_2", "nora_place_prog_trans_scene_3", "nora_place_prog_trans_scene_4", "nora_place_prog_trans_scene_5", "nora_place_prog_trans_scene_6"]
    the_progression_scene.final_scene_list = ["nora_place_prog_scene_scene_0", "nora_place_prog_scene_scene_1", "nora_place_prog_scene_scene_2", "nora_place_prog_scene_scene_3", "nora_place_prog_scene_scene_4", "nora_place_prog_scene_scene_5", "nora_place_prog_scene_scene_6"]
    the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.

nora_place_prog_scene_action = Action("Have some fun", nora_place_prog_scene_action_req, "nora_place_prog_scene_action_label")

def nora_place_prog_scene_init():
    global nora_place_prog_scene
    nora_place_prog_scene = Progression_Scene(
        compile_scenes = nora_place_prog_scene_compile_scenes,
        start_scene_list = [],  #Set via the compile action
        req_list = [],  #Set via the compile action
        trans_list = [],    #Set via the compile action
        final_scene_list = [],  #Set via the compile action
        intro_scene = "nora_place_prog_scene_intro_scene", #Scene that plays the first time this scene is run
        exit_scene = "nora_place_prog_scene_exit_scene",   #Scene for if the player chooses to exit the scene
        progression_scene_action = nora_place_prog_scene_action,      #The action used to call for this progression scene.
        choice_scene = "nora_place_prog_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
        stage = -1,     #-1 will play the intro
        person_action = False,   #If this progression scene should run when encountering a person
        business_action = False,    #If this progression scene is a mandatory business event
        is_random = False,  #If this progression scene is a randomly occurring crisis event
        unit_test_func = None,  #Set a custom unit test function to test this progression event. Runs between every cycle
        advance_time = False,
        is_multiple_choice = True, #If MC can choose what final scene he wants
        role_action = True, #Let's try putting this in as a role action and see if it shows progressions correctly.
        multiple_choice_scene = "nora_place_prog_scene_multiple_choice_scene",   #The scene that lets MC choose which final scene he wants.
        regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.

    nora_place_prog_scene.recompile_scenes()   #This will populate the scenes that are blank above.

    list_of_progression_scenes.append(nora_place_prog_scene)

#Use this if nora is the one choosing the action. Uses a bunch of random rolls and condition checks.
def nora_place_prog_scene_choose_action():
    #First, check and see if we have any of the fetish scenes available. 15% chance to run any individual fetish we already have unlocked.
    rnd = renpy.random.randint(0, 100)
    if 3 in nora_place_prog_scene.scene_unlock_list and rnd <= 15:
        return 3
    if 4 in nora_place_prog_scene.scene_unlock_list and rnd > 15 and rnd <= 30:
        return 4
    if 5 in nora_place_prog_scene.scene_unlock_list and rnd > 30 and rnd <= 45:
        return 5
    if 6 in nora_place_prog_scene.scene_unlock_list and rnd > 45 and rnd <= 60:
        return 6

    #Roll another dice to choose between the final three scenes
    rnd = renpy.random.randint(0, 100)
    if 2 in nora_place_prog_scene.scene_unlock_list and rnd <= 40:  #40% chance of cowgirl if we have that unlocked
        return 2
    if 1 in nora_place_prog_scene.scene_unlock_list and rnd >= 70 and nora.sex_record.get("Last Sex Day", 0) >= day - 7:  #30% chance of endurance test IF MC has been keeping her satisfied.
        return 1
    return 0


#Popup text functions. Use these to display scene completion criteria at the beginning of each scene.
def nora_place_prog_scene_0_popup_text():
    if mc.sex_skills["Oral"] >= 6 and (mc.max_energy >= 160 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control")) and nora.effective_sluttiness() >= 60:
        return "Full Scene"
    popup_text = "Partial Scene:"
    if mc.sex_skills["Oral"] < 6:
        popup_text.append("\n  Oral Skill 6+")
    if mc.max_energy < 160:
        popup_text.append("\n  Max Energy 160+")
    if nora.effective_sluttiness() < 60:
        popup_text.append("\n  Nora Sluttiness +60")
    return popup_text

def nora_place_prog_scene_1_popup_text():
    if mc.sex_skills["Oral"] >= 6 and (mc.max_energy >= 170 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control")) and mc.sex_skills["Foreplay"] >= 6 and mc.sex_skills["Vaginal"] >= 6:
        return "Full Scene"
    popup_text = "Partial Scene:"
    if mc.sex_skills["Foreplay"] < 6:
        popup_text.append("\n  Foreplay Skill 6+")
    if mc.sex_skills["Oral"] < 6:
        popup_text.append("\n  Oral Skill 6+")
    if mc.sex_skills["Vaginal"] < 6:
        popup_text.append("\n  Vaginal Skill 6+")
    if mc.max_energy < 170:
        popup_text.append("\n  Max Energy 170+")
    return popup_text

def nora_place_prog_scene_2_popup_text():
    if mc.sex_skills["Vaginal"] >= 6 and (mc.max_energy >= 180 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control")):
        return "Full Scene"
    popup_text = "Partial Scene:"
    if mc.sex_skills["Vaginal"] < 6:
        popup_text.append("\n  Vaginal Skill 6+")
    if mc.max_energy < 170:
        popup_text.append("\n  Max Energy 180+")
    return popup_text
