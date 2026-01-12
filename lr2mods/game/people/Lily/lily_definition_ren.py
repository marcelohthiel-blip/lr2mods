from __future__ import annotations
import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import ponytail
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Room_ren import university, lily_bedroom
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, lily, mom, ashley, erica
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.people.Lily.lily_role_definition_ren import had_family_threesome, init_sister_roles, lily_can_give_serum, lily_get_serums_tested, lily_mom_insta_started, lily_mom_topless_pics_complete, lily_started_insta_story, lily_will_strip, sister_role, sister_student_role
from game.people.Erica.erica_role_definition_ren import erica_get_is_doing_insta_sessions, erica_is_looking_for_work

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
list_of_instantiation_functions.append("create_lily_character")

def lily_titles(person: Person):
    valid_titles = [person.name]
    if person.love > 15:
        valid_titles.append("Sis")
    if person.love > 30:
        valid_titles.append("Li'l Sis")
    if person.love < -10:
        valid_titles.append("Bitch")
    if person.love < -30:
        valid_titles.append("Cunt")

    return valid_titles

def lily_possessive_titles(person: Person):
    valid_titles = ["your sister", person.title]

    if person.sluttiness > 60:
        valid_titles.append("your slutty sister")

    if person.sluttiness > 90:
        valid_titles.append("your cock hungry sister")
        valid_titles.append("the family cumdump")
    return valid_titles

def lily_player_titles(person: Person):
    valid_titles = [mc.name]
    valid_titles.append("Brother")
    if person.sluttiness > 30:
        valid_titles.append("Big Bro")
        valid_titles.append("Baby")
    return valid_titles

def sister_intro_crisis_requirements(person: Person, day_trigger):
    return mc.is_in_bed and day >= day_trigger

def sister_strip_intro_requirement(person: Person): #Note that this only ever triggers once, so we don't need to worry if it will retrigger at any point.
    if mc.is_in_bed:
        return person.sluttiness >= 30 and mc.business.event_triggers_dict.get("sister_serum_test_count", 0) >= 3
    return False

def instathot_intro_requirement(person: Person): #This action sits in her room
    if person.sluttiness < 20:
        return False
    if person.event_triggers_dict.get("insta_intro_finished", False):
        return False
    if not person.is_home or lily.bedroom.person_count > 1:
        return False
    return True

def create_lily_character():
    ### LILY ###
    lily_wardrobe = wardrobe_from_xml("Lily_Wardrobe")
    #height = 0.90
    init_sister_roles()

    global sister_student_job
    sister_student_job = JobDefinition("Student", sister_student_role, job_location = university, day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])

    global lily_personality
    lily_personality = Personality("lily", relaxed_personality.default_prefix,
        common_likes = ["skirts", "small talk", "the colour pink", "makeup"],
        common_sexy_likes = ["lingerie", "masturbating", "being submissive", "doggy style sex"],
        common_dislikes = ["working", "conservative outfits", "the colour brown"],
        common_sexy_dislikes = ["taking control", "anal sex", "creampies"],
        titles_function = lily_titles, possessive_titles_function = lily_possessive_titles, player_titles_function = lily_player_titles,
        insta_chance = 0, dikdok_chance = 0)

    global lily
    lily = make_person(name = "Lily", last_name = mc.last_name, age = 12, body_type = "thin_body", face_style = "Face_6", tits = "B", height = 0.94, hair_colour = ["saturated", [0.905, 0.898, 0.513, 0.95]], hair_style = ponytail, skin="white",
        eyes = "light blue", personality = lily_personality, name_color = "#FFB1F8", dial_color = "#FFB1F8", starting_wardrobe = lily_wardrobe, start_home = lily_bedroom,
        stat_array = [5, 2, 2], skill_array = [2, 2, 0, 1, 1], sex_skill_array = [2, 1, 0, 0], sluttiness = 8, obedience = 74, happiness = 122, love = 8, suggestibility_range = [4, 8],
        title = "Sis", possessive_title = "your sister", mc_title = mc.name, relationship = "Single", kids = 0,
        forced_opinions = [
            ["skirts", 1, False],
            ["the colour pink", 2, False],
            ["the colour black", 1, False],
            ["the colour brown", -1, False],
            ["conservative outfits", -1, False]],
        forced_sexy_opinions = [
            ["being submissive", 1, False],
            ["skimpy outfits", 2, False],
            ["showing her ass", 1, False],
            ["masturbating", 2, False]],
        serum_tolerance = 2, work_experience = 1, type="story")

    lily.add_role(sister_role)
    lily.set_schedule(lily.home, time_slots = [0, 3, 4])
    lily.change_job(sister_student_job)
    lily.home.add_person(lily)
    mc.phone.register_number(lily)
    lily.set_event_day("day_met")

    mc.business.add_mandatory_crisis(
        Action("sister_intro_crisis", sister_intro_crisis_requirements, "sister_intro_crisis_label", args=lily, requirement_args = [lily, renpy.random.randint(7, 14)])
    ) #Introduces Lily one to two weeks into the game. She will test serum for cash.
    mc.business.add_mandatory_crisis(
        Action("sister_strip_intro_crisis", sister_strip_intro_requirement, "sister_strip_intro_label", args=lily, requirement_args = lily)
    ) #Lily comes asking for more money. She will strip (to varying degrees) for cash)

    #Event to introduce Lily taking pictures on the internet for money.
    lily.add_unique_on_room_enter_event(
        Action("Instathot intro", instathot_intro_requirement, "sister_instathot_intro_label", priority = 30)
    )

##############
# Story Info #
##############

def lily_story_character_description():
    return "Your younger sister. Attends classes at the local university and often hard up for cash."

def lily_story_love_list():
    love_story_list = {}
    if not lily_can_give_serum():
        love_story_list[0] = "[lily.name] may talk to you about earning some money soon!"
        return love_story_list
    else:
        love_story_list[0] = "[lily.name] agreed to help you test your serums."

    if lily.is_girlfriend:
        love_story_list[1] = "[lily.name] has agreed to be your girlfriend!"
    elif lily.love < 60:
        love_story_list[1] = "Increase [lily.name]'s love and try to make her your girlfriend."
        return love_story_list
    elif not mom.event_triggers_dict.get("sister_girlfriend_ask_blessing", False):
        love_story_list[1] = "Work on getting [mom.name] to accept your relationship."
        return love_story_list
    else:
        love_story_list[1] = "You might be able to convince [lily.name] to be your girlfriend if you try."
        return love_story_list

    love_story_list[2] = "There is nothing more in this story line at this time."
    return love_story_list

def lily_story_love_is_complete():
    return lily.is_girlfriend

def lily_story_lust_list():
    if not lily_can_give_serum():
        return {
            0: "Work on [lily.name]'s love story first."
        }

    #Insta start
    lust_story_list = {}
    if lily.sluttiness < 20:
        return {
            0: "Get [lily.name] to 20 sluttiness."
        }
    if lily_started_insta_story():
        lust_story_list[0] = "You helped [lily.name] take pictures for InstaPic."
    else:
        return {
            0: "Try entering [lily.name]'s room when she is alone there."
        }

    #Stripping
    if lily_will_strip():
        lust_story_list[1] = "[lily.name] offered to strip for you for extra cash!"
    elif lily.sluttiness < 30:
        lust_story_list[1] = "Raise [lily.name]'s sluttiness to at least 30 to continue this story."
        return lust_story_list
    elif lily_get_serums_tested() < 4:
        lust_story_list[1] = "Have [lily.name] test " + str(4 - lily_get_serums_tested()) + " more serums."
        return lust_story_list

    lust_story_list[2] = "There is nothing more in this story line at this time."

    return lust_story_list

def lily_story_lust_is_complete():
    return lily_will_strip()

# def lily_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

def lily_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamup_story_list = {}
    if had_family_threesome():
        teamup_story_list[0] = (mom, "You've slept with [lily.name] and [mom.name] at the same time!")
    elif lily_mom_topless_pics_complete():
        teamup_story_list[0] = (mom, "You've convinced [lily.name] and [mom.name] to take topless InstaPics!")
    elif lily_mom_insta_started():
        teamup_story_list[0] = (mom, "You've convinced [lily.name] and [mom.name] to take InstaPics together.")
    else:
        teamup_story_list[0] = (mom, "Getting [lily.name] and [mom.name] together seems impossible... but is it?")

    if erica_get_is_doing_insta_sessions():
        teamup_story_list[1] = (erica, "Help [erica.name] take InstaPics with [lily.name] every Saturday night in [lily.name]'s room!")
    elif not erica_is_looking_for_work():
        teamup_story_list[1] = (erica, "Try progressing [erica.name]'s story.")
    elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
        teamup_story_list[1] = (erica, "Try advancing [lily.name]'s storyline.")
    else:
        teamup_story_list[1] = (erica, "Try talking to [lily.name] and [erica.name] about money issues.")

    if ashley.progress.love_step >= 2:
        teamup_story_list[2] = (ashley, "Your sister and [ashley.fname] already seem to know each other. What might happen if you work on repairing their relationship?")

    # This is currently not available
    #if kaya_has_finished_intro():
    #    teamup_story_list[3] = [kaya,"The [lily.name] and [kaya.name] teamup is in progress but not yet written."]

    return teamup_story_list

def lily_story_other_list():
    story_other_list = {}
    if lily_can_give_serum():
        story_other_list[0] = "[lily.fname] will test your serums for $50"
    if lily_will_strip():
        story_other_list[1] = "[lily.fname] will strip for you for $100"
    if lily_started_insta_story():
        story_other_list[2] = "You can help [lily.name] take pictures for her InstaPic account."

    if lily.event_triggers_dict.get("vaginal_revisit_complete", False):
        story_other_list[3] = "[lily.possessive_title!c] is completely open to your sexual requests."
    elif lily.event_triggers_dict.get("anal_revisit_complete", False):
        story_other_list[3] = "[lily.possessive_title!c] is willing to let you take her anally, but is refusing to go all the way."
    elif lily.event_triggers_dict.get("oral_revisit_complete", False):
        story_other_list[3] = "[lily.possessive_title!c] is willing to exchange oral favours, but refuses to go any further. Perhaps she would try anal."
    elif lily.event_triggers_dict.get("kissing_revisit_complete", False):
        story_other_list[3] = "[lily.possessive_title!c] is willing to exchange minor sexual favours, but refuses to go any further."
    else:
        story_other_list[3] = "[lily.possessive_title!c] is unwilling to let you touch her sexually."

    return story_other_list

####################
# Position Filters #
####################

def lily_oral_position_filter(oral_position: Position):
    return lily.event_triggers_dict.get("kissing_revisit_complete", False)

def lily_vaginal_position_filter(vaginal_position: Position):
    return lily.event_triggers_dict.get("anal_revisit_complete", False)

def lily_anal_position_filter(anal_position: Position):
    return lily.event_triggers_dict.get("oral_revisit_complete", False)

def lily_oral_position_info():
    return "Break oral taboo"

def lily_vaginal_position_info():
    return "Break anal taboo"
