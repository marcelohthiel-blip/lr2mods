from __future__ import annotations
from renpy.display.im import Image
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.sex_positions._position_definitions_ren import blowjob, cowgirl_handjob, against_wall
from game.personality_types._personality_definitions_ren import reserved_personality
from game.clothing_lists_ren import heavy_eye_shadow, copper_ring_set, braided_bun
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related._job_definitions_ren import student_job
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, list_of_instantiation_functions, sarah, erica, lily, nora, kaya
from game.people.Erica.erica_role_definition_ren import erica_fetish_is_kicked_off_team, erica_fetish_rejoin_team, erica_get_is_doing_insta_sessions, erica_get_is_doing_yoga_sessions, erica_get_progress, erica_get_yoga_class_list, erica_has_given_morning_handjob, erica_is_looking_for_work, erica_post_yoga_fuck_complete, erica_pre_insta_blowjob_complete, erica_role
from game.people.Kaya.kaya_role_definition_ren import kaya_has_finished_intro, kaya_studies_with_erica
from game.people.Teamups.erica_kaya_teamup_definition_ren import kaya_erica_teamup

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 4 python:
"""

list_of_instantiation_functions.append("create_erica_character")

erica_activity_opinions = {}
erica_activity_opinions["pong"] = 2


def erica_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    if person.effective_sluttiness() > 40:
        valid_titles.append("College Athlete")
        valid_titles.append("Cardio Bunny")
    if person.effective_sluttiness() > 60:
        valid_titles.append("Slutty Athlete")
    if person.has_breeding_fetish:
        valid_titles.append("Breeding Gym Bunny")
    if person.has_anal_fetish:
        valid_titles.append("Anal Gym Bunny")
    return valid_titles

def erica_possessive_titles(person: Person):
    valid_possessive_titles = ["your gym girl", person.title]

    if person.effective_sluttiness() > 60:
        valid_possessive_titles.append("your gym slut")

    if person.effective_sluttiness() > 80:
        valid_possessive_titles.append("the gym cumdump")
        valid_possessive_titles.append("the gym bicycle")
    if person.has_breeding_fetish:
        valid_possessive_titles.append("your breeder gym bunny")
    if person.has_anal_fetish:
        valid_possessive_titles.append("your anal gym bunny")
    return valid_possessive_titles

def erica_player_titles(person: Person):
    valid_mc_titles = [mc.name]
    valid_mc_titles.append("Workout Partner")
    if person.has_breeding_fetish:
        valid_mc_titles.append("Bull")
    return valid_mc_titles

def create_erica_character():
    erica_wardrobe = wardrobe_from_xml("Erica_Wardrobe") # default wardrobe when not in gym (no xml file, no wardrobe)
    erica_base_outfit = Outfit("Erica's base accessories")
    erica_base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.20, .20, .37, 0.50])
    erica_base_outfit.add_accessory(copper_ring_set.get_copy(), [.1, .36, .19, 0.95])

    erica_personality = Personality("erica", default_prefix = reserved_personality.default_prefix,
        common_likes = ["small talk", "the colour blue", "sports"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "showing her ass", "drinking cum", "taking control"],
        common_dislikes = ["relationships", "conservative outfits", "makeup", "the colour pink", "dresses", "high heels", "the colour purple"],
        common_sexy_dislikes = ["lingerie", "being submissive", "skimpy outfits"],
        titles_function = erica_titles, possessive_titles_function = erica_possessive_titles, player_titles_function = erica_player_titles)

    global erica
    erica = make_person(name = "Erica", last_name = "Davenport", age = 19, body_type = "thin_body", face_style = "Face_4", tits="B", height = 0.89, hair_colour = ["ginger red", [0.72, 0.40, 0.00, 0.95]], hair_style = braided_bun, skin="white",
        eyes = "light blue", personality = erica_personality, name_color = "#89CFF0", starting_wardrobe = erica_wardrobe, job = student_job,
        stat_array = [2, 4, 4], skill_array = [4, 1, 3, 3, 1], sex_skill_array = [3, 2, 3, 2], sluttiness = 3, obedience_range = [70, 85], happiness = 119, love = 0,
        relationship = "Single", kids = 0, base_outfit = erica_base_outfit,
        forced_opinions = [
            ["production work", 2, True],
            ["work uniforms", -1, False],
            ["flirting", 1, False],
            ["pants", 1, False],
            ["the colour blue", 2, False],
            ["yoga", 2, False],
            ["sports", 2, False]],
        forced_sexy_opinions = [
            ["doggy style sex", 2, False],
            ["missionary style sex", -2, False],
            ["giving blowjobs", 1, False],
            ["getting head", 1, False],
            ["being submissive", 1, False],
            ["creampies", -2, False],
            ["public sex", 1, False]],
        serum_tolerance = 0, work_experience = 1, type = 'story')

    erica.max_energy = 120
    erica.generate_home()
    erica.home.background_name = "student_apartment_background"
    erica.home.add_person(erica)

    erica.set_override_schedule(erica.home) # hide until unlocked

    erica.fertility_percent = -400.0 #Erica refuses to get pregnant for MC, getting pregnant would cause her to be kicked from track team. Enabled with breeding fetish.

    town_relationships.update_relationship(nora, erica, "Friend")


##############
# Story Info #
##############

def erica_story_character_description():
    return "A collegiate track and field athlete."

def erica_story_love_list():
    love_story_list = {}
    if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
        love_story_list[0] = "You helped [erica.fname] earn some extra money doing InstaPic and Yoga."
    elif erica_get_is_doing_yoga_sessions():
        love_story_list[0] = "You helped [erica.fname] earn some extra money doing Yoga."
        love_story_list[1] = "Try working with [lily.fname] to help [erica.fname] earn some extra money."
        return love_story_list
    elif erica_get_is_doing_insta_sessions():
        love_story_list[0] = "You helped [erica.fname] earn some extra money doing InstaPic with [lily.fname]."
        love_story_list[1] = "Try working with your HR Director to help [erica.fname] earn some extra money."
        return love_story_list
    elif erica_is_looking_for_work():
        love_story_list[0] = "[erica.fname] is looking for some part-time work."
        love_story_list[1] = "Try working with your HR director or [lily.fname] to help her find some extra work!"
        return love_story_list
    elif erica.love < 20:
        love_story_list[0] = "Try increasing [erica.fname]'s love score."
        return love_story_list
    else:
        love_story_list[0] = "Try getting to know [erica.fname] better."
        return love_story_list

    if erica_pre_insta_blowjob_complete():
        love_story_list[1] = "[erica.fname] showed her appreciation by giving you a blowjob before an InstaPic session!"
    elif erica.love <= 40:
        love_story_list[1] = "Try increasing her love to continue this story."
        return love_story_list
    elif not erica.is_willing(blowjob):
        love_story_list[1] = "[erica.fname] needs to be willing to give you a blowjob. Make sure her sluttiness is high enough and she doesn't hate that act!"
        return love_story_list
    else:
        love_story_list[1] = "Make sure to be there to take pics for [erica.fname] and [lily.fname]'s next InstaPic session."
        return love_story_list

    if erica_post_yoga_fuck_complete():
        love_story_list[2] = "You couldn't stop watching [erica.fname] during your company yoga. She loved it and you fucked her after against your office wall."
    elif erica.love <= 60:
        love_story_list[2] = "Try increasing her love to continue this story."
        return love_story_list
    elif not erica.is_willing(against_wall):
        love_story_list[2] = "[erica.fname] needs to be willing to fuck you against the wall. Make sure her sluttiness is high enough and she doesn't hate that act!"
        return love_story_list
    else:
        love_story_list[2] = "Make sure to attend company yoga on Tuesday morning to continue this story."
        return love_story_list

    love_story_list[3] = "There is nothing more in this story line at this time."
    return love_story_list

def erica_story_love_is_complete():
    return erica_post_yoga_fuck_complete()

def erica_story_lust_list():
    lust_story_list = {}

    if erica_has_given_morning_handjob():
        lust_story_list[0] = "[erica.fname] woke you up with a handjob after spending the night with [lily.fname]."
        lust_story_list[1] = "Talk to her if you want her to wake you up more or less often."
    elif not erica.is_willing(cowgirl_handjob):
        lust_story_list[0] = "[erica.fname] needs to be willing to give a handjob to continue this story. Try raising her sluttiness and check her opinions."
        return lust_story_list
    elif not erica_get_is_doing_insta_sessions():
        lust_story_list[0] = "Try advancing [erica.fname]'s love story to unlock this."
        return lust_story_list
    else:
        lust_story_list[0] = "[erica.fname] may try sneaking into your room some morning..."
        return lust_story_list

    if erica_get_progress() > 1:
        lust_story_list[1] = "You worked out with [erica.fname] and had some fun in the gym locker room afterwords."
    elif erica_get_progress() == 1:
        lust_story_list[1] = "Try working out with [erica.fname] sometime."
        return lust_story_list
    elif mc.max_energy < 120:
        lust_story_list[1] = "[erica.fname] prefers athletic guys. Try raising your maximum energy."
        return lust_story_list
    elif erica.sluttiness < 40:
        lust_story_list[1] = "Try raising [erica.fname]'s sluttiness to continue this story."
        return lust_story_list

    if erica_get_progress() >= 4:
        lust_story_list[2] = "You won a bet with [erica.fname] in a race, then fucked her at her place."
    elif erica_get_progress() == 3:
        lust_story_list[2] = "You've challenged [erica.fname] to a race. To the victor go the spoils!"
        return lust_story_list
    elif erica.sluttiness < 60:
        lust_story_list[2] = "Try raising [erica.fname]'s sluttiness to continue this story."
        return lust_story_list
    elif mc.max_energy < 140:
        lust_story_list[2] = "[erica.fname] prefers athletic guys. Try raising your maximum energy."
        return lust_story_list
    else:
        lust_story_list[2] = "Try challenging [erica.fname] to a race."
        return lust_story_list

    lust_story_list[3] = "There is nothing more in this story line at this time."

    return lust_story_list

def erica_story_lust_is_complete():
    return erica_get_progress() >= 4

# def erica_story_obedience_list():
#     obedience_story_list = {}
#     obedience_story_list[0] = "This story step has not yet been written."
#     return obedience_story_list

def erica_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamup_story_list = {}
    #Yoga
    if erica_get_is_doing_yoga_sessions():
        teamup_story_list[0] = (sarah, "Watch [erica.fname] do yoga with [sarah.fname] every Tuesday morning at the office!")
    elif not erica.event_triggers_dict.get("yoga_quest_started", False):
        teamup_story_list[0] = (sarah, "Try progressing [erica.fname]'s story.")
    elif len(erica_get_yoga_class_list()) < 4:
        teamup_story_list[0] = (sarah, "Help [sarah.fname] convince employees to like or love yoga.")
    else:
        teamup_story_list[0] = (sarah, "Talk to [erica.fname] about hosting a company yoga class.")

    #Insta
    if erica_get_is_doing_insta_sessions():
        teamup_story_list[1] = (lily, "Help [erica.fname] take InstaPics with [lily.fname] every Saturday night in [lily.fname]'s bedroom!")
    elif not erica_is_looking_for_work():
        teamup_story_list[1] = (lily, "Try progressing [erica.fname]'s story.")
    elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
        teamup_story_list[1] = (lily, "Try advancing [lily.fname]'s storyline.")
    else:
        teamup_story_list[1] = (lily, "Try talking to [lily.fname] and [erica.fname] about money issues.")

    #Study
    if kaya_studies_with_erica():
        if kaya_erica_teamup.get_stage() == 0:
            teamup_story_list[2] = (kaya, "[erica.fname] and [kaya.fname] study together on Tuesday nights.")
        elif kaya_erica_teamup.get_stage() == 1:
            teamup_story_list[2] = (kaya, "[erica.fname] and [kaya.fname] study together on Tuesday nights, sometimes getting naked for you.")
        elif kaya_erica_teamup.get_stage() == 2:
            teamup_story_list[2] = (kaya, "[erica.fname] and [kaya.fname] study together on Tuesday nights, sometimes letting you spank them.")
        elif kaya_erica_teamup.get_stage() == 3:
            teamup_story_list[2] = (kaya, "[erica.fname] and [kaya.fname] study together on Tuesday nights, sometimes sucking you off.")
        elif kaya_erica_teamup.get_stage() == 4:
            teamup_story_list[2] = (kaya, "[erica.fname] and [kaya.fname] study together on Tuesday nights, and are down for a threesome after!")
    elif kaya_has_finished_intro():
        teamup_story_list[2] = (kaya, "[erica.fname] and [kaya.fname] are both college students...")
    return teamup_story_list

def erica_story_other_list():
    other_info_list = {}
    if erica_get_progress() > 1:
        other_info_list[0] = "[erica.fname] likes to workout with you at the gym, especially what happens after..."
    if erica_get_progress() >= 4:
        other_info_list[1] = "You are always welcome at [erica.fname]'s house at night."
    if erica_fetish_is_kicked_off_team() and not erica_fetish_rejoin_team():
        other_info_list[2] = "[erica.fname] got kicked off the track team for getting pregnant! Try talking to [nora.fname]."
    if erica_fetish_rejoin_team():
        other_info_list[3] = "You helped [erica.fname] rejoin the track team after knocking her up."

    return other_info_list
