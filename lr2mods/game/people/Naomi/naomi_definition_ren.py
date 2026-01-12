from __future__ import annotations
import renpy
from game.helper_functions.random_generation_functions_ren import make_person
from game.clothing_lists_ren import braided_bun
from game.game_roles._role_definitions_ren import maid_role
from game.major_game_classes.character_related._job_definitions_ren import unemployed_job
from game.major_game_classes.character_related.Person_ren import Person, town_relationships, mc, list_of_instantiation_functions, sarah, naomi
from game.major_game_classes.game_logic.Position_ren import Position
from game.personality_types._personality_definitions_ren import Personality, wild_personality
from game.sex_positions._position_definitions_ren import tit_fuck, standing_grope, standing_finger, standing_dildo, spanking

TIER_1_TIME_DELAY = 3
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 3 python:
"""
list_of_instantiation_functions.append("create_naomi_character")

def naomi_titles(the_person: Person):
    valid_titles = [the_person.name]
    return valid_titles

def naomi_possessive_titles(the_person: Person):
    valid_titles = ["Sarah's slutty friend"]
    if the_person.has_role(maid_role):
        valid_titles.append("Your maid")
        if the_person.sluttiness > 40:
            valid_titles.append("Your slutty maid")
    return valid_titles

def naomi_player_titles(the_person: Person):
    valid_titles = [mc.name]
    if the_person.has_role(maid_role):
        valid_titles.append("Sir")
    return valid_titles

def create_naomi_character():     # initializes her and returns person
    global naomi

    naomi_personality = Personality("Naomi", default_prefix = wild_personality.default_prefix,
        common_likes = ["small talk", "Fridays", "the weekend", "makeup", "flirting", "punk music"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her ass", "threesomes", "not wearing underwear", "creampies", "bareback sex"],
        common_dislikes = ["the colour pink", "supply work", "conservative outfits", "work uniforms"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex"],
        titles_function = naomi_titles, possessive_titles_function = naomi_possessive_titles, player_titles_function = naomi_player_titles)

    naomi = make_person(name = "Naomi", last_name = "Walters", age = 23, body_type = "thin_body", face_style = "Face_3",
        height = 0.94, personality = naomi_personality, hair_colour = ["toasted wheat", [0.848, 0.75, 0.469, 0.95]], hair_style = braided_bun,
        skin="white", relationship = "Fiancée", kids = 0, tits = "DD", sluttiness = renpy.random.randint(25, 40), job = unemployed_job,
        forced_opinions = [
            ["skirts", 1, False],
            ["boots", 1, False],
            ["the colour yellow", 2, False],
            ["the colour blue", 2, False],
            ["the colour green", -2, False],
            ["pants", -2, False],
            ["high heels", 2, False]],
        forced_sexy_opinions = [
            ["taking control", 1, False],
            ["threesomes", 2, False],
            ["giving handjobs", -2, False],
            ["skimpy outfits", 1, False],
            ["showing her tits", 2, False],
            ["not wearing underwear", 2, False],
            ["anal sex", -2, False]],
        work_experience = 1, type = 'story')

    naomi.generate_home()
    naomi.home.add_person(naomi)
    naomi.set_title(naomi.name)
    naomi.set_mc_title(mc.name)
    naomi.set_possessive_title("Sarah's slutty friend")
    # hide her from player until she is reintroduced into the story
    naomi.set_override_schedule(naomi.home)
    town_relationships.update_relationship(sarah, naomi, "Best Friend")

#############################################
# Custom property on Person class for Naomi #
#############################################

def get_corruption_level(self):
    return self.event_triggers_dict.get("corruption_level", 0)

def set_corruption_level(self, value):
    self.event_triggers_dict["corruption_level"] = value

Person.corruption_level = property(get_corruption_level, set_corruption_level, None, "Corruption Level of the person")

#########################
# Character Information #
#########################

def naomi_story_character_description():
    return "A party girl, with an explicit taste in partners."

def naomi_story_other_list():
    other_info_list = {}
    if sarah.event_triggers_dict.get("threesome_unlock", False):
        other_info_list[0] = "Wait for [naomi.fname] to contact you."
        if naomi.event_triggers_dict.get("naomi_sarah_speaking_again", False):
            other_info_list[0] = "[naomi.fname] apologized to [sarah.fname] and they agreed give their friendship a chance."
    else:
        other_info_list[0] = "Continue [sarah.fname]'s story, until you have had your first threesome."

    if naomi.event_triggers_dict.get("naomi_sarah_speaking_again", False):
        other_info_list[1] = "[naomi.fname] will contact you soon, to discuss her financial issues."
    elif naomi.has_role(maid_role):
        other_info_list[1] = "You've hired [naomi.fname] as a maid to clean your home."
    else:
        return other_info_list

    if not naomi.has_role(maid_role):
        other_info_list[2] = "You did not hire [naomi.fname], ending her alternative story."
        return other_info_list

    if naomi.corruption_level < 2:
        other_info_list[2] = "You will have several opportunities to corrupt your maid [naomi.fname]."

    return other_info_list


####################
# Position Filters #
####################

def naomi_foreplay_position_filter(foreplay_position: Position):
    filter_out = [tit_fuck, standing_finger, standing_grope, standing_dildo, spanking]
    if naomi.corruption_level > 0:
        filter_out.remove(spanking)
    if naomi.corruption_level > 1:
        filter_out.extend((standing_grope, standing_finger))
    if naomi.corruption_level > 2:
        filter_out = []
    # only allow groping or kissing until story continues
    return foreplay_position not in filter_out

def naomi_oral_position_filter(oral_position: Position):
    if not naomi.has_role(maid_role):
        return False
    # naomi.event_triggers_dict.get("naomi_allow_oral", False)
    return naomi.sex_record.get("Fingered", 0) > 3

def naomi_vaginal_position_filter(vaginal_position: Position):
    if not naomi.has_role(maid_role):
        return False
    if naomi.corruption_level <= 2:
        return False
    # naomi.event_triggers_dict.get("naomi_allow_vaginal", False)
    return naomi.cum_mouth_count > 3

def naomi_anal_position_filter(anal_position: Position):
    if not naomi.has_role(maid_role):
        return False
    # return naomi.event_triggers_dict.get("naomi_allow_anal", False)
    return naomi.vaginal_creampie_count > 3

def naomi_oral_position_info():
    if not naomi.has_role(maid_role):
        return "Wait until you can hire her as maid"
    if naomi.corruption_level <= 2:
        return "You will need to corrupt your maid further"
    count = 4 - naomi.sex_record.get("Fingered", 0)
    return f"Finger her {count} more times"

def naomi_vaginal_position_info():
    if not naomi.has_role(maid_role):
        return "Wait until you can hire her as maid"
    if naomi.corruption_level <= 2:
        return "You will need to corrupt your maid further"
    count = 4 - naomi.cum_mouth_count
    return f"Cum in her mouth {count} more times"

def naomi_anal_position_info():
    if not naomi.has_role(maid_role):
        return "Wait until you can hire her as maid"
    if naomi.corruption_level <= 2:
        return "You will need to corrupt your maid further"
    count = 4 - naomi.vaginal_creampie_count
    return f"Give her {count} more creampies"
