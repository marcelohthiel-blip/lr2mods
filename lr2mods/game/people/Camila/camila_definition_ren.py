from __future__ import annotations
import builtins
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import blush, colourful_bracelets, lipstick, braided_bun
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions, mc, alexia, nora, camila
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import downtown_bar, mall
from game.personality_types._personality_definitions_ren import wild_personality
from game.people.Camila.camila_role_definition_ren import camila_role, init_camila_roles, lifestyle_coach_role

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_camila_character")

def camila_intro_requirement(person: Person):
    return person.is_at(mall)

def mc_dancing_skill(): #Wrapper for measuring MC's progress learning to salsa dance.
    return mc.charisma + builtins.int((mc.max_energy - 100) / 20)

def camila_titles(person: Person):
    valid_titles = []
    valid_titles.append(person.name)
    if person.effective_sluttiness() > 40:
        valid_titles.append("Slutwife")
        valid_titles.append("Cuckold Wife")
    return valid_titles

def camila_possessive_titles(person: Person):
    valid_possessive_titles = [person.title]

    if person.effective_sluttiness() > 60:
        valid_possessive_titles.append("the slut wife")
        valid_possessive_titles.append("your swinging slut")

    if person.effective_sluttiness() > 90:
        valid_possessive_titles.append("the bar cumdump")
    return valid_possessive_titles

def camila_player_titles(person: Person):
    valid_titles = ["Mr. " + mc.last_name]
    if person.love > 20:
        valid_titles.append(mc.name)
    if person.has_breeding_fetish:
        valid_titles.append("Bull")
    return valid_titles


def create_camila_character():
    camila_wardrobe = wardrobe_from_xml("Camila_Wardrobe")

    camila_base_outfit = Outfit("camila's base accessories")
    camila_base_outfit.add_accessory(blush.get_copy(), [.65, .23, .17, 0.2])
    camila_base_outfit.add_accessory(lipstick.get_copy(), [.26, .21, .14, 0.33])
    camila_base_outfit.add_accessory(colourful_bracelets.get_copy(), [.95, .95, .78, 0.95])

    init_camila_roles()

    camila_job = JobDefinition("Lifestyle Coach", lifestyle_coach_role, mall, day_slots = [0, 1, 2, 3, 4], time_slots = [1, 2])

    camila_personality = Personality("camila", default_prefix = wild_personality.default_prefix,
        common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
        common_dislikes = ["pants", "working", "the colour yellow", "conservative outfits", "sports"],
        common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything", "polyamory"],
        titles_function = camila_titles, possessive_titles_function = camila_possessive_titles, player_titles_function = camila_player_titles)

    global camila
    camila = make_person(name = "Camila", last_name = "Rojas", body_type = "thin_body", age = 34, face_style = "Face_2", tits="D", height = 0.98, hair_colour = ["golden blonde", [0.895, 0.781, 0.656, 0.95]], hair_style = braided_bun, skin="tan",
        personality = camila_personality, name_color = "#DAA520", starting_wardrobe = camila_wardrobe, job = camila_job,
        stat_array = [1, 4, 6], skill_array = [1, 1, 3, 5, 1], sex_skill_array = [4, 2, 2, 2], sluttiness = 7, obedience_range = [70, 85], happiness = 119, love = 0,
        relationship = "Married", kids = 0, base_outfit = camila_base_outfit, type = 'story',
        forced_opinions = [
            ["dancing", 2, True],
            ["fashion", 2, False],
            ["flirting", 1, False],
            ["working", 1, False],
            ["the colour purple", 2, False],
            ["dresses", 2, False],
            ["the colour blue", -2, False],
            ["skirts", 1, False]],
        forced_sexy_opinions = [
            ["being submissive", 2, False],
            ["getting head", 2, False],
            ["drinking cum", 1, False],
            ["giving blowjobs", 2, False],
            ["public sex", 1, False],
            ["showing her ass", 2, False],
            ["anal sex", -2, False],
            ["bareback sex", 2, False],
            ["doggy style sex", 1, False],
            ["vaginal sex", 1, False]],
        serum_tolerance = 1, work_experience = 2)

    camila.market_skill = 6
    camila.add_role(camila_role)
    camila.generate_home()
    camila.home.add_person(camila)
    camila.set_schedule(downtown_bar, time_slots = [3])

    # she introduces herself
    camila.set_title(camila.name)
    camila.set_possessive_title("your lifestyle coach")

    # camila_mod_initialization():
    # camila.event_triggers_dict["intro_complete"] = False    # True after first talk
    # camila.event_triggers_dict["get_drinks"] = False
    # camila.event_triggers_dict["go_dancing"] = False
    # camila.event_triggers_dict["take_pics"] = False
    # camila.event_triggers_dict["will_fuck"] = False
    # camila.event_triggers_dict["her_place"] = False
    # camila.event_triggers_dict["outfit_help"] = False
    # camila.event_triggers_dict["lingerie_help"] = False
    # camila.event_triggers_dict["formal_date"] = False
    # camila.event_triggers_dict["lost_anal_virginity"] = False
    # camila.event_triggers_dict["boudoir_stage"] = 0
    camila.fertility_percent = -1000.0  #She's infertile
    camila.on_birth_control = False     # No BC -> she's infertile

    camila.add_unique_on_room_enter_event(
        Action("camila_intro", camila_intro_requirement, "camila_intro_label", priority = 30)
    )

##############
# Story Info #
##############

def camila_story_character_description():
    return "A married lifestyle coach who frequents the bar in the evening."

def camila_story_love_list():
    love_story_list = {}

    if not camila.event_triggers_dict.get("met", False):
        love_story_list[0] = "Look for [camila.fname] at the bar in the evening"
        return love_story_list

    if camila.love < 20:
        love_story_list[0] = "Increase [camila.fname]'s love to 20"
    if not camila.story_event_ready("love"):
        love_story_list[0] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(mall):
        love_story_list[0] = "Meet [camila.fname] when she is working at the mall"

    if not camila.event_triggers_dict.get("help_with_outfit", False):
        return love_story_list

    love_story_list[0] = "[camila.fname] asked your opinion on date night outfits."

    if camila.love < 40:
        love_story_list[1] = "Increase [camila.fname]'s love to 40"
    if not camila.story_event_ready("love"):
        love_story_list[1] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(mall):
        love_story_list[1] = "Meet [camila.fname] when she is working at the mall"

    if not camila.event_triggers_dict.get("help_with_lingerie", False):
        return love_story_list

    love_story_list[1] = "[camila.fname] tried on lingerie for you and you had fun in the dressing room with her."

    if camila.love < 60:
        love_story_list[2] = "Increase [camila.fname]'s love to 60"
    else:
        love_story_list[2] = "[camila.fname] will contact you and continue this story when the time is right"

    if not camila.event_triggers_dict.get("formal_date", False):
        return love_story_list

    love_story_list[2] = "You went on a formal date with [camila.fname] and had a one-night stand."

    love_story_list[3] = "This next story step is not yet written"

    # camila.love_messages[3] = "As an act of retribution to her husband, [camila.fname] gave you her anal virginity."

    return love_story_list

def camila_story_love_is_complete():
    return camila.event_triggers_dict.get("formal_date", False)

def camila_story_lust_list():
    lust_story_list = {}

    if camila.sluttiness < 20:
        lust_story_list[0] = "Raise her sluttiness to 20"

    if not camila.event_triggers_dict.get("go_dancing", False):
        lust_story_list[0] = "Go dancing with [camila.fname] on Wednesday"
        return lust_story_list

    lust_story_list[0] = "You can now go salsa dancing with [camila.fname] at the bar"

    if camila.sluttiness < 40:
        lust_story_list[1] = "Raise her sluttiness to 40"
    if not camila.story_event_ready("slut"):
        lust_story_list[1] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(downtown_bar):
        lust_story_list[1] = "Talk to [camila.fname] at the bar in the evening"

    if camila.days_since_event("camila_blowjob_pic_day") == 0:
        return lust_story_list

    lust_story_list[1] = "[camila.fname] sucked you off in the bar restroom while you took pictures for her husband"

    if camila.sluttiness < 60:
        lust_story_list[2] = "Raise her sluttiness to 60"
    if mc_dancing_skill() <= 6:
        lust_story_list[2] = "Increase you dancing skill to continue this story"
    if not camila.story_event_ready("slut"):
        lust_story_list[2] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(downtown_bar):
        lust_story_list[2] = "Talk to [camila.fname] at the bar in the evening"

    if not camila.event_triggers_dict.get("bathroom_sex", False):
        return lust_story_list

    lust_story_list[2] = "You fucked [camila.fname] after a night of dancing"

    if camila.sluttiness < 80:
        lust_story_list[3] = "Raise her sluttiness to 80"
    if not camila.story_event_ready("slut"):
        lust_story_list[3] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(downtown_bar):
        lust_story_list[3] = "Talk to [camila.fname] at the bar in the evening"

    if not camila.event_triggers_dict.get("home_sex", False):
        return lust_story_list

    lust_story_list[3] = "You fucked [camila.fname] in her own bedroom while her husband watched"
    lust_story_list[4] = "This story step is not yet written"

    return lust_story_list

def camila_story_lust_is_complete():
    return camila.event_triggers_dict.get("home_sex", False)

def camila_story_obedience_list():
    obedience_story_list = {}

    if camila.obedience < 120:
        obedience_story_list[0] = "Increase [camila.fname]'s obedience to 120"
    if not camila.story_event_ready("obedience"):
        obedience_story_list[0] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(mall):
        obedience_story_list[0] = "Talk to [camila.fname] when she is at the mall"

    if not camila.event_triggers_dict.get("goal_coach", False):
        return obedience_story_list

    obedience_story_list[0] = "You got [camila.fname] to help you make new business goals"

    if camila.obedience < 140:
        obedience_story_list[1] = "Increase [camila.fname]'s obedience to 140"
    if not camila.story_event_ready("obedience"):
        obedience_story_list[1] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(mall):
        obedience_story_list[1] = "Talk to [camila.fname] when she is at the mall"

    if not camila.event_triggers_dict.get("sex_goal_coach", False):
        return obedience_story_list

    obedience_story_list[1] = "You got [camila.fname] to help you make new sexual goals"

    if camila.obedience < 160:
        obedience_story_list[2] = "Increase [camila.fname]'s obedience to 160"
    if not camila.story_event_ready("obedience"):
        obedience_story_list[2] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(mall):
        obedience_story_list[2] = "Talk to [camila.fname] when she is at the mall"

    if not camila.event_triggers_dict.get("obedience_titfuck", False):
        return obedience_story_list

    obedience_story_list[2] = "[camila.fname] helped you realise your love for tits, when you finished all over hers."

    if camila.obedience < 180:
        obedience_story_list[3] = "Increase [camila.fname]'s obedience to 180"
    if not camila.story_event_ready("obedience"):
        obedience_story_list[3] = "[camila.fname] needs time before she is ready to progress this story"
    if not camila.is_at(mall):
        obedience_story_list[3] = "Talk to [camila.fname] when she is at the mall"

    obedience_story_list[4] = "The next story step has not yet been written."

    return obedience_story_list

def camila_story_obedience_is_complete():
    return camila.event_triggers_dict.get("obedience_titfuck", False)

def camila_story_teamup_list() -> dict[int, tuple[Person, str]]:
    return {
        0: (alexia, "This teamup is not yet written"),
        1: (nora, "This teamup is not yet written")
    }

def camila_story_other_list():
    #camila's other story indices:
    # 0 - Her relationship with her husband
    # 1 - Your salsa dancing skill level
    # 2 - Her fertility progress (if any)
    other_story_list = {}

    if camila.event_triggers_dict.get("bar_met", False):
        other_story_list[0] = "[camila.fname] is happily married but in an open marriage"
        other_story_list[1] = "[camila.fname] doesn't have any children"

    dancing_skill = str(mc_dancing_skill())
    other_story_list[2] = "Your skill level at salsa dancing is " + dancing_skill + " / 20"
    if camila.event_triggers_dict.get("bathroom_sex", False):
        other_story_list[3] = "[camila.fname] is infertile"

    return other_story_list

####################
# Position Filters #
####################

def camila_oral_position_filter(oral_position: Position):
    return camila.days_since_event("camila_blowjob_pic_day") > 0

def camila_oral_position_info():
    return "Complete the take dirty pictures event"

def camila_vaginal_position_filter(vaginal_position: Position):
    return camila.event_triggers_dict.get("booty_call", False)

def camila_vaginal_position_info():
    return "Complete the salsa dancing event"

def camila_anal_position_filter(anal_position: Position):
    return camila.event_triggers_dict.get("home_sex", False)

def camila_anal_position_info():
    return "Complete the home sex event"
