from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import lipstick, bead_bracelet, modern_glasses, wide_choker, light_eye_shadow, shaved_side_hair
from game.game_roles._role_definitions_ren import critical_job_role
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, list_of_instantiation_functions, myra, alexia
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import gaming_cafe, downtown
from game.major_game_classes.game_logic.Position_ren import Position
from game.sex_positions._position_definitions_ren import blowjob, deepthroat, skull_fuck, cowgirl_blowjob
from game.personality_types._personality_definitions_ren import Personality, wild_personality
from game.people.Myrabelle.myra_focus_training_definition_ren import myra_focus_progression_scene
from game.people.Myrabelle.myra_role_definition_ren import init_myra_roles, myra_role, myra_can_distribute_serum, myra_can_sponsor, myra_caught_masturbating, myra_distracts_gamers, myra_has_been_sponsored, myra_has_failed_tournament, myra_is_expanding_business, myra_lewd_cafe_open, myra_lewd_game_fuck_avail, myra_plays_esports, myra_deepthroat_avail, myra_finish_blowjob_training, myra_started_blowjob_training, myra_wants_bigger_tits, myra_will_grind_with_mc
from game.people.Teamups.alexia_myra_teamup_definition_ren import myra_alexia_teamup_scene


TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_myra_character")

def myrabelle_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    if person.has_breeding_fetish:
        valid_titles.append("Cow")
    if person.is_submissive:
        valid_titles.append("Dungeon slut")
    return valid_titles

def myrabelle_possessive_titles(person: Person):
    valid_possessive_titles = [person.title]
    if person.sluttiness > 40:
        valid_possessive_titles.append("your gaming slut")
    return valid_possessive_titles

def myrabelle_player_titles(person: Person):
    return [mc.name]

def myra_rude_intro_requirement():
    return time_of_day == 1 and day > 7


def create_myra_character():
    #Start with her wardrobe and base outfit
    myrabelle_wardrobe = wardrobe_from_xml("Myrabelle_Wardrobe")

    #Requires creation of a new wardrobe file. Alternatively, you can use one of the default ones, IE "myra_Wardrobe"
    myrabelle_base_outfit = Outfit("myrabelle's base accessories")
    myrabelle_base_outfit.add_accessory(lipstick.get_copy(), [.8, .26, .04, 0.33])
    myrabelle_base_outfit.add_accessory(bead_bracelet.get_copy(), [.4, .6, .93, 0.8])
    myrabelle_base_outfit.add_accessory(modern_glasses.get_copy(), [.15, .15, .15, 0.95])
    myrabelle_base_outfit.add_accessory(wide_choker.get_copy(), [.15, .15, .15, 0.9])
    myrabelle_base_outfit.add_accessory(light_eye_shadow.get_copy(), [.0, .28, .67, 0.33])

    myra_job = JobDefinition("Gaming Café Owner", critical_job_role, job_location = gaming_cafe, day_slots = [2, 3, 4, 5, 6], time_slots = [2, 3])
    myra_job.set_schedule(gaming_cafe, day_slots = [5, 6], time_slots = [1, 2, 3])    #Extended hours on weekends

    myrabelle_personality = Personality("myrabelle", wild_personality.default_prefix,
        common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
        common_dislikes = ["pants", "working", "the colour yellow", "conservative outfits", "sports"],
        common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything", "polyamory"],
        titles_function = myrabelle_titles, possessive_titles_function = myrabelle_possessive_titles, player_titles_function = myrabelle_player_titles)

    global myra
    myra = make_person(name = "Myrabelle", # First name
        last_name ="Cassidy",                   # Last Name
        age = 28,                               # Years Old
        body_type = "thin_body",                # Use "thin_body", "standard_body", or "curvy_body". For pregnant, suggest using become_pregnant() function after person is created.
        face_style = "Face_12",                 # 1-4 and 6-14 (5 is missing from vanilla files.)
        tits="B",                               # "AA" "A" "B" "C" "D" "DD" "DDD" "E" "F" "FF"... blame vren for weird sizing.
        height = 0.92,                          # Not sure the limits on this one
        hair_colour = ["sky blue", [0.529, 0.808, 0.922, 0.95]], # See list_of_hairs for options
        hair_style = shaved_side_hair,
        #pubes_style = diamond_pubes,
        skin="white",
        tan_style = None,
        eyes = "light blue",                    # "dark blue", "light blue", "green", "brown", "grey", or "emerald"
        job = myra_job,                         # Generic job title. Use for random town people or people with jobs OUTSIDE of MC's company
        personality = myrabelle_personality,    # Personality
        custom_font = None,                     #
        name_color = "#2a9df4",                 #
        starting_wardrobe = myrabelle_wardrobe, # Leave None to make basic wardrobe
        stat_array = [1, 3, 3],                 # [charisma, int, focus]
        skill_array = [1, 1, 5, 2, 1],          # [HR, market, research, production, supply]
        sex_skill_array = [4, 1, 2, 4],         # [foreplay, oral, vaginal, anal]
        sluttiness = 2,                         #
        obedience_range = [95, 110],            #
        happiness = 115,                        #
        love = 0,                               #
        start_home = None,                      # Use if this girl is living with someone else
        relationship = "Single",                # "Single", "Girlfriend", "Fiancée", "Married"
        kids = 0,                               #
        SO_name = None,                         # IF she isn't Single
        generate_insta = None,                  # True or False, random if None
        generate_dikdok = None,                 #
        generate_onlyfans = None,               #
        base_outfit = myrabelle_base_outfit,     #
        forced_opinions = [
            ["punk music", 2, True],
            ["work uniforms", -1, False],
            ["flirting", 1, False],
            ["working", -1, False],
            ["the colour blue", 2, False],
            ["pants", 1, False],
            ["gaming", 2, False]],
        forced_sexy_opinions = [
            ["giving handjobs", 2, False],
            ["showing her ass", 2, False],
            ["drinking cum", -1, False],
            ["giving blowjobs", -2, False],
            ["anal sex", 2, False],
            ["doggy style sex", 1, False],
            ["being submissive", 2, False],
            ["getting head", 2, False]],
        serum_tolerance = 1, type = 'story')

    # setup gaming cafe role
    init_myra_roles()
    myra.add_role(myra_role)

    myra.generate_home()                                        #Omit this if girl lives with someone else
    myra.set_schedule(myra.home, time_slots = [0, 1, 2, 3, 4])  #Hide myrabelle at home until we are ready to use her
    myra.home.add_person(myra)                                  #Need to add her to the world or MC will not encounter her.

    # Below is an example of how you could make a mandatory event that would start the myrabelle character's story. The label and the requirement functions are not included in this template.
    # myrabelle_intro = Action("myrabelle_intro",myrabelle_intro_requirement,"myrabelle_intro_label")
    # mc.business.add_mandatory_crisis(myrabelle_intro) #Add the event here so that it pops when the requirements are met.

    # set town relationships
    # town_relationships.update_relationship(myrabelle, kaya, "Daughter", "Mother")
    town_relationships.update_relationship(alexia, myra, "Friend")
    # town_relationships.update_relationship(lily, myrabelle, "Rival")

    downtown.add_unique_on_room_enter_event(
        Action("Meet Myra", myra_rude_intro_requirement, "myra_rude_intro_label", priority = 30)
    )

##############
# Story Info #
##############

def myrabelle_story_character_description():
    return "An aspiring professional gamer and owner of the Gaming Café at the mall."

def myrabelle_story_love_list():
    love_story_list = {}
    love_story_list[0] = "[myra.fname] has opened a gaming café at the mall. Play games there to restore energy."
    if not myra_will_grind_with_mc():
        love_story_list[1] = "Get your character to at least level 30 to play Guild Quest 2 with [myra.fname]."
    else:
        love_story_list[1] = "[myra.fname] enjoys playing Guild Quest 2 with you."

    if myra_plays_esports():
        love_story_list[2] = "You learned she is a part of an esports team."
    elif myra.love < 20:
        love_story_list[2] = "Increase [myra.fname]'s love to learn more about her."
        return love_story_list
    else:
        love_story_list[2] = "Swing by the gaming café to learn more about [myra.fname]."
        return love_story_list

    if myra_has_failed_tournament():
        love_story_list[3] = "However, [myra.fname] lost her first esports tournament, badly."
    elif myra.love < 40:
        love_story_list[3] = "Increase [myra.fname]'s love to learn more about her."
        return love_story_list
    else:
        love_story_list[3] = "[myra.fname]'s first tournament is on a Sunday."
        return love_story_list

    if myra_can_sponsor():
        love_story_list[4] = "She lost a major sponsor as a result."
    elif myra.love < 60:
        love_story_list[4] = "Increase [myra.fname]'s love to progress her story."
        return love_story_list
    else:
        love_story_list[4] = "Stop by the café in the evening to learn the repercussions of her loss."
        return love_story_list

    if not mc.business.has_funds(25000):
        love_story_list[5] = "You need more money to step up and sponsor her yourself."
        return love_story_list
    else:
        love_story_list[5] = "Talk to [myra.fname] about sponsoring her team yourself."

    if myra_has_been_sponsored():
        love_story_list[5] = "You stepped up and sponsored her esports team yourself."
        love_story_list[6] = "This is the end of content in this version."

    return love_story_list

    # love_story_list[6] = "This is the end of content in this version. Everything after this in her love story is just outlining."
    # if myra.love < 80:
    #     love_story_list[7] = "Increase [myra.fname]'s love to progress her story."
    #     return love_story_list
    # elif myra_focus_progression_scene.get_stage() < 2:
    #     love_story_list[7] = "Help [myra.fname] train her focus to advance her story."
    #     return love_story_list
    # elif not myra_has_won_tournament():
    #     love_story_list[7] = "Talk to [myra.fname] about setting up a new tournament. She is ready!"
    #     return love_story_list

    # if myra_has_won_tournament():
    #     love_story_list[8] = "[myra.fname] hosted her own tournament and placed third! A huge improvement!"
    # if myra_is_expanding_business():
    #     love_story_list[8] = "She has used her winnings to begin expanding her business!"
    # elif myra.love < 95:
    #     love_story_list[8] = "Increase [myra.fname]'s love to progress her story."
    #     return love_story_list
    # else:
    #     love_story_list[8] = "Talk to [myra.fname] about her winnings."
    #     return love_story_list

    # love_story_list[9] = "There is nothing more in this story line at this time."
    # return love_story_list

def myrabelle_story_love_is_complete():
    return myra_has_been_sponsored()

def myrabelle_story_lust_list():
    lust_story_list = {}
    if myra_distracts_gamers():
        lust_story_list[0] = "[myra.fname] likes to use dirty language and double entendres to distract gaming opponents."
    elif myra.sluttiness < 20:
        lust_story_list[0] = "Raise [myra.fname]'s sluttiness to advance this story."
        return lust_story_list
    else:
        lust_story_list[0] = "Swing by the gaming café during business hours to advance this story."
        return lust_story_list

    if myra_caught_masturbating():
        lust_story_list[1] = "[myra.fname] enjoys sexual video games. You caught her masturbating to one."
    elif myra.sluttiness < 40:
        lust_story_list[1] = "Raise [myra.fname]'s sluttiness to advance this story."
        return lust_story_list
    else:
        lust_story_list[1] = "Swing by the gaming café during the evening to advance this story."
        return lust_story_list

    if myra_lewd_game_fuck_avail():
        lust_story_list[2] = "[myra.fname] enjoys fucking you while acting out positions from a sexual PC game. She is willing every evening at the gaming café."
    elif myra.sluttiness < 60:
        lust_story_list[2] = "Raise [myra.fname]'s sluttiness to advance this story."
        return lust_story_list
    elif myra.has_taboo("vaginal_sex"):
        lust_story_list[2] = "Fuck [myra.fname] to advance this story."
        return lust_story_list
    else:
        lust_story_list[2] = "Swing by the gaming café during the evening to advance this story."
        return lust_story_list

    if myra_lewd_cafe_open():
        lust_story_list[3] = "She has opened an adults only VIP section at the gaming café for sexual PC games."
    elif myra.sluttiness < 80:
        lust_story_list[3] = "Raise [myra.fname]'s sluttiness to advance this story."
        return lust_story_list
    elif not myra_is_expanding_business():
        lust_story_list[3] = "Advance [myra.fname]'s love story before advancing this story."
        return lust_story_list

    lust_story_list[4] = "There is nothing more in this story line at this time."

    return lust_story_list

def myrabelle_story_lust_is_complete():
    return myra_has_been_sponsored()

# def myrabelle_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

def myrabelle_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamup_story_list = {}

    #Alexia
    if myra_alexia_teamup_scene.get_stage() == -1:
        teamup_story_list[0] = (alexia, "[alexia.fname] is her good friend. Maybe there will be an opportunity here someday")
    elif myra_alexia_teamup_scene.get_stage() == 0:
        teamup_story_list[0] = (alexia, "[alexia.fname] meets with her every Friday night. You can rub their backs if you join them.")
    elif myra_alexia_teamup_scene.get_stage() == 1:
        teamup_story_list[0] = (alexia, "[alexia.fname] and [myra.fname] compete for you to finger them on Friday nights.")
    elif myra_alexia_teamup_scene.get_stage() == 2:
        teamup_story_list[0] = (alexia, "[alexia.fname] and [myra.fname] compete for you to eat them out on Friday nights.")
    elif myra_alexia_teamup_scene.get_stage() == 3:
        teamup_story_list[0] = (alexia, "[alexia.fname] and [myra.fname] compete for you to fuck them on Friday nights.")
    elif myra_alexia_teamup_scene.get_stage() == 3:
        teamup_story_list[0] = (alexia, "[alexia.fname] and [myra.fname] have a friendly gaming night that always ends in a threesome on Friday nights.")
    return teamup_story_list

def myrabelle_story_other_list():
    other_info_list = {}
    if myra_focus_progression_scene.get_stage() >= 0:
        other_info_list[0] = "You can help [myra.fname] train her focus to get better at gaming in distracting situations."
        if myra_focus_progression_scene.get_stage() == 0:
            other_info_list[1] = "You distract her with back rubs during training. Raise her sluttiness to take distractions further."
        elif myra_focus_progression_scene.get_stage() == 1:
            other_info_list[1] = "You distract her by groping her tits during training. Raise her sluttiness to take distractions further."
        elif myra_focus_progression_scene.get_stage() == 2:
            other_info_list[1] = "You distract her by fingering her during training. Raise her sluttiness to take distractions further."
        elif myra_focus_progression_scene.get_stage() == 3:
            other_info_list[1] = "You distract her by getting a lap dance during training. Raise her sluttiness to take distractions further."
        elif myra_focus_progression_scene.get_stage() == 4:
            other_info_list[1] = "You distract her by fucking her ass during training."
    if myra_can_distribute_serum():
        other_info_list[2] = "Every Wednesday, you can send company energy drinks to [myra.fname] for distribution."
    if myra_wants_bigger_tits() and not myra.has_large_tits:
        other_info_list[3] = "[myra.fname] has asked for help growing bigger tits."
    elif myra.has_large_tits and myra_wants_bigger_tits():
        other_info_list[3] = "[myra.fname] is thankful you helped her grow her tits."
    if myra_finish_blowjob_training():
        other_info_list[4] = "You helped train [myra.fname] how to give amazing head."
    elif myra_started_blowjob_training():
        other_info_list[4] = "You are training [myra.fname] how to give better head. Check back with her weekly."
    else:
        other_info_list[4] = "[myra.fname] hates giving head. You should look for some way to show her oral skills are important."
    if myra_lewd_cafe_open():
        other_info_list[5] = "[myra.fname] has opened an adults only section to the gaming café!"

    return other_info_list


####################
# Position Filters #
####################


def myrabelle_foreplay_position_filter(foreplay_position: Position):
    return True

def myrabelle_oral_position_filter(oral_position: Position):
    if myra_finish_blowjob_training():
        return True
    if myra_started_blowjob_training() and myra_deepthroat_avail():
        return not oral_position == skull_fuck
    if myra_started_blowjob_training():
        return oral_position not in (skull_fuck, deepthroat)
    return oral_position not in (skull_fuck, deepthroat, blowjob, cowgirl_blowjob)

def myrabelle_vaginal_position_filter(vaginal_position: Position):
    # for now unlock after a few swallows
    return myra.cum_mouth_count > 3

def myrabelle_anal_position_filter(anal_position: Position):
    # for now unlock after a few creampies
    return myra.vaginal_creampie_count > 3

def myrabelle_oral_position_info():
    return "Finish her blowjob training"

def myrabelle_vaginal_position_info():
    count = 4 - myra.cum_mouth_count
    return f"Cum in her mouth {count} more times"

def myrabelle_anal_position_info():
    count = 4 - myra.vaginal_creampie_count
    return f"Give her {count} more creampies"
