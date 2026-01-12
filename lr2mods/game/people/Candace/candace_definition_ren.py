from __future__ import annotations
from game.helper_functions.random_generation_functions_ren import make_person
from game.personality_types._personality_definitions_ren import bimbo_personality, relaxed_personality
from game.clothing_lists_ren import heavy_eye_shadow, light_eye_shadow, strappy_bra, lace_crop_top, strappy_panties, leggings, thigh_highs, high_heels, lipstick, curly_bun
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.game_logic.Room_ren import office_store
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.clothing_related.Wardrobe_ren import Wardrobe
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, candace, salon_manager, sarah, starbuck
from game.people.Candace.candace_role_definition_ren import candace_role, init_candace_roles, make_candace_free_roam_and_set_intro_event
from game.people.Ophelia.ophelia_role_definition_ren import ophelia_get_ex_name

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_instantiation_functions.append("create_candace_character")

def candace_titles(person: Person):
    return "Candi" # lock to this title

def candace_possessive_titles(person: Person):
    return "your office bimbo" # lock to this title

def candace_player_titles(person: Person):
    valid_mc_titles = []
    valid_mc_titles.append(mc.name)
    valid_mc_titles.append("Cutie")
    valid_mc_titles.append("Boss")
    return valid_mc_titles

def genius_titles(person: Person) -> list[str]:
    if person.love < 20:
        return ["Dr." + person.last_name] #If she doesn't like you she's much more formal.
    return [person.name]

def genius_possessive_titles(person: Person) -> list[str]:
    return genius_titles(person) #If we don't have a special possessive just use their normal title.

def genius_player_titles(person: Person) -> list[str]:
    return [mc.name]

def get_base_outfit() -> Outfit:
    outfit = Outfit("Candace's base accessories")
    outfit.add_accessory(light_eye_shadow.get_copy(), [.15, .15, .15, 0.5])
    outfit.add_accessory(lipstick.get_copy(), [.45, .31, .59, 0.4])
    outfit.add_accessory(heavy_eye_shadow.get_copy(), [.45, .31, .59, 0.5])
    return outfit

def get_initial_wardrobe() -> Wardrobe:
    # her boyfriend only allows her to wear this 'company wardrobe'
    candace_wardrobe = Wardrobe("Candace's Wardrobe")
    outfit = Outfit("Pink Lace Top And Leggings")
    outfit.add_upper(strappy_bra.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_upper(lace_crop_top.get_copy(), [.87, .44, .63, .95])
    outfit.add_lower(strappy_panties.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_lower(leggings.get_copy(), [.87, .44, .63, .95])
    outfit.add_feet(thigh_highs.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_feet(high_heels.get_copy(), [.87, .44, .63, .95])
    candace_wardrobe.add_outfit(outfit)
    return candace_wardrobe

def init_candace_genius_personality():
    global genius_personality
    genius_personality = Personality("genius", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["pants", "the weekend", "small talk", "the colour pink", "flirting", "punk music", "pop music"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour yellow", "work uniforms"],
        common_sexy_dislikes = ["taking control", "doggy style sex", "showing her tits", "showing her ass", "bareback sex", "creampies"],
        titles_function = genius_titles, possessive_titles_function = genius_possessive_titles, player_titles_function = genius_player_titles)

def convert_candace_to_genius():
    init_candace_genius_personality()
    candace.change_personality(genius_personality)
    candace.set_event_day("cure_day")
    candace.int = 9       #Scary smart

def create_candace_character():
    candace_base_outfit = get_base_outfit()
    candace_wardrobe = get_initial_wardrobe()

    init_candace_roles()

    candace_job = JobDefinition("Assistant", candace_role, None, time_slots = [1, 2])

    candace_personality = Personality("candace", default_prefix = bimbo_personality.default_prefix,
        common_likes = ["small talk", "makeup", "pop music"],
        common_sexy_likes = ["missionary style sex", "being submissive", "showing her ass", "not wearing anything", "lingerie", "cum facials"],
        common_dislikes = ["working", "work uniforms", "conservative outfits", "Mondays", "pants"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = candace_titles, possessive_titles_function = candace_possessive_titles, player_titles_function = candace_player_titles)

    global candace
    candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "standard_body", face_style = "Face_12", tits = "F", height = 0.94, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = curly_bun, skin="black",
        eyes = "light blue", personality = candace_personality, name_color = "#D2691E", starting_wardrobe = candace_wardrobe, job = candace_job,
        stat_array = [3, 1, 5], skill_array = [2, 1, 2, 1, 5], sex_skill_array = [2, 3, 4, 1], sluttiness = 30, obedience_range = [50, 70], happiness = 76, love = 0,
        title = "Candi", possessive_title = "your acquaintance", mc_title = mc.name, relationship = "Girlfriend", kids = 0, base_outfit = candace_base_outfit,
        forced_opinions = [
            ["supply work", 2, True],        # she loves HR work
            ["skirts", 1, False],        #And Skirts
            ["the colour pink", 2, False], #She loves pink
            ["the colour yellow", 1, False],
            ["the colour purple", -2, False],
            ["the colour green", -2, False],
            ["pants", -2, False],        #She hates pants!
            ["high heels", 2, False]],
        forced_sexy_opinions = [
            ["being submissive", 1, False], # likes when others have their way with her
            ["giving handjobs", -2, False], # prefers to use other body parts...
            ["giving blowjobs", 1, False],  # like her mouth :)
            ["skimpy outfits", 1, False],
            ["showing her tits", 2, False],
            ["not wearing underwear", 2, False],
            ["cheating on men", 1, False]],
        serum_tolerance= 2, work_experience = 2, type = 'story')

    candace.generate_home()
    candace.home.add_person(candace)
    candace.set_override_schedule(candace.home)

def create_debug_candace(): #Use this function to make a version of Candace for debug purposes.
    candace_base_outfit = get_base_outfit()
    candace_wardrobe = get_initial_wardrobe()

    # init candace role
    candace_job = JobDefinition("Assistant", candace_role, None, time_slots = [1, 2])

    global candace
    candace.remove_person_from_game()

    candace_personality = Personality("candace", default_prefix = bimbo_personality.default_prefix,
        common_likes = ["skirts", "small talk", "the colour pink", "makeup", "pop music"],
        common_sexy_likes = ["giving blowjobs", "missionary style sex", "being submissive", "skimpy outfits", "showing her tits", "showing her ass", "not wearing anything", "not wearing underwear", "lingerie", "cum facials"],
        common_dislikes = ["working", "work uniforms", "conservative outfits", "Mondays", "pants"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = candace_titles, possessive_titles_function = candace_possessive_titles, player_titles_function = candace_player_titles)

    candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "F", height = 0.94, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = curly_bun, skin="black",
        eyes = "light blue", personality = candace_personality, name_color = "#D2691E", starting_wardrobe = candace_wardrobe, job = candace_job,
        stat_array = [3, 1, 5], skill_array = [2, 1, 2, 1, 5], sex_skill_array = [2, 3, 4, 1], sluttiness = 35, obedience_range = [50, 70], happiness = 76, love = 0,
        title = "Candi", possessive_title = "your acquaintance", mc_title = mc.name, relationship = "Girlfriend", SO_name = ophelia_get_ex_name(), kids = 0, base_outfit = candace_base_outfit, type = 'story',
        forced_opinions = [
            ["supply work", 2, True],        # she loves supply work
            ["skirts", 1, False],        #And Skirts
            ["the colour pink", 2, False], #She loves pink
            ["the colour yellow", 1, False],
            ["the colour purple", -2, False],
            ["the colour green", -2, False],
            ["pants", -2, False],        #She hates pants!
            ["high heels", 2, False]],
        forced_sexy_opinions = [
            ["being submissive", 1, False], # likes when others have their way with her
            ["giving handjobs", -2, False], # prefers to use other body parts...
            ["skimpy outfits", 1, False],
            ["showing her tits", 2, False],
            ["not wearing underwear", 2, False],
            ["cheating on men", 1, False]])

    candace.generate_home()
    candace.set_schedule(office_store, day_slots = [0, 1, 2, 3, 4], time_slots = [3]) #Buying office supplies for her employer.
    candace.home.add_person(candace)
    make_candace_free_roam_and_set_intro_event()
    mc.business.add_employee_supply(candace, False)

def create_debug_genius_candace():  #Use this function to make a version of genius Candace for debug purposes.
    candace_base_outfit = get_base_outfit()
    candace_wardrobe = get_initial_wardrobe()

    # init candace role
    candace_job = JobDefinition("Assistant", candace_role, None, time_slots = [1, 2])
    init_candace_genius_personality()

    global candace
    candace.remove_person_from_game()
    candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "F", height = 0.94, hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = curly_bun, skin="black",
        eyes = "light blue", personality = genius_personality, name_color = "#D2691E", starting_wardrobe = candace_wardrobe, job = candace_job,
        stat_array = [3, 1, 5], skill_array = [2, 1, 2, 1, 5], sex_skill_array = [2, 3, 4, 1], sluttiness = 35, obedience_range = [50, 70], happiness = 76, love = 0,
        title = "Candi", possessive_title = "your acquaintance", mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = candace_base_outfit, type = 'story',
        forced_opinions = [
            ["supply work", 2, True],        # she loves supply work
            ["skirts", 1, False],        #And Skirts
            ["the colour pink", 2, False], #She loves pink
            ["the colour yellow", 1, False],
            ["the colour purple", -2, False],
            ["the colour green", -2, False],
            ["pants", -2, False],        #She hates pants!
            ["high heels", 2, False]],
        forced_sexy_opinions = [
            ["being submissive", 1, False], # likes when others have their way with her
            ["giving handjobs", -2, False], # prefers to use other body parts...
            ["skimpy outfits", 1, False],
            ["showing her tits", 2, False],
            ["not wearing underwear", 2, False],
            ["cheating on men", 1, False]])

    candace.generate_home()
    candace.set_schedule(office_store, day_slots = [0, 1, 2, 3, 4], time_slots = [3]) #Buying office supplies for her employer.
    candace.home.add_person(candace)
    make_candace_free_roam_and_set_intro_event()
    mc.business.add_employee_supply(candace, False)


##############
# Story Info #
##############

def candace_story_love_list():
    love_story_list = {}

    if candace.event_triggers_dict.get("quit_job", 0) != 0:
        love_story_list[0] = "Keep working on [candace.fname] to quit her current job."
        return love_story_list

    love_story_list[0] = "You managed to hire [candace.fname] and convinced her to dump her boyfriend"

    if candace.love < 20:
        love_story_list[1] = "Increase [candace.fname]'s love to 20"
    if not candace.story_event_ready("love"):
        love_story_list[1] = "[candace.fname] needs time before she is ready to progress this story"
    if not candace.is_at_work:
        love_story_list[1] = "Talk to [candace.fname] at when she is working."

    if not candace.event_triggers_dict.get("clothes_shopping", 0) != 0:
        return love_story_list

    love_story_list[1] = "You went clothes shopping with [candace.fname]. You can invite other girls to go with you from the store anytime."
    love_story_list[2] = "This event is not yet written."
    return love_story_list

def candace_story_lust_list():
    lust_story_list = {}

    if candace.sluttiness < 40:
        lust_story_list[0] = "Increase [candace.fname]'s sluttiness to 40"
    if not candace.story_event_ready("lust"):
        lust_story_list[0] = "[candace.fname] needs time before she is ready to progress this story"
    else:
        lust_story_list[0] = "Check up on [candace.fname] at work in the afternoon or evening"

    if not candace.event_triggers_dict.get("supply_discount", False):
        lust_story_list[0] = "Check up with [candace.fname] and see how it went with the supplier."
        return lust_story_list

    lust_story_list[0] = "You convinced [candace.fname] to accept discounts from supply vendors!"
    lust_story_list[1] = "The next step has not yet been written"

    return lust_story_list

# def candace_story_obedience_list():
#     obedience_story_list = {
#         0: "This event is not yet written."

#     }
#     return obedience_story_list

def candace_story_teamup_list() -> dict[int, tuple[Person, str]]:
    return {
        0: (salon_manager, "This teamup is not yet written"),
        1: (sarah, "This teamup is not yet written"),
        2: (starbuck, "This teamup is not yet written")
    }

def candace_story_other_list():
    #candace's other story indices:
    # 0 - Her relationship with her boyfriend
    # 1 - Your karaoke skill level
    # 2 - Her bimbo status

    other_story_list = {}
    other_story_list[0] = "She is currently in a relationship"

    if candace.event_triggers_dict.get("quit_job", 0) != 0:
        other_story_list[0] = "You managed to break up [candace.fname]'s relationship with her abusive ex"

    # candace.other_messages[1] = "Your skill level at karaoke is "+ karaoke_skill + " / 20"
    return other_story_list
