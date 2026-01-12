from __future__ import annotations
import builtins
from game.business_policies.organisation_policies_ren import HR_director_creation_policy
from game.helper_functions.random_generation_functions_ren import make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import modern_glasses, light_eye_shadow, windswept_hair
from game.game_roles._role_definitions_ren import critical_job_role
from game.game_roles.stripclub._stripclub_role_definitions_ren import strip_club_is_closed
from game.sex_positions._position_definitions_ren import tit_fuck, sarah_tit_fuck
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.Room_ren import ceo_office
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import breast_enhancement
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition
from game.major_game_classes.character_related.Personality_ren import Personality
from game.major_game_classes.character_related.Person_ren import Person, mc, list_of_instantiation_functions, sarah, erica
from game.personality_types._personality_definitions_ren import relaxed_personality
from game.people.Erica.erica_definition_ren import erica_get_is_doing_yoga_sessions, erica_get_yoga_class_list
from game.people.Sarah.HR_supervisor_definition_ren import get_HR_director_tag, get_HR_director_unlock
from game.people.Sarah.HR_supervisor_role_definition_ren import init_HR_directore_roles
from game.people.Sarah.sarah_role_definition_ren import get_Sarah_willing_threesome_list, init_sarah_roles, sarah_role


TIER_1_TIME_DELAY = 3
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
list_of_instantiation_functions.append("create_sarah_character")
sarah_strip_pose_list = ["walking_away", "back_peek", "standing_doggy",
                         "stand2", "stand3", "stand4", "stand5", "doggy", "kneeling1"]

def Sarah_intro_requirement():
    return day >= TIER_1_TIME_DELAY and mc.is_home

def can_appoint_HR_director_requirement():
    if not mc.business.hr_director:
        return HR_director_creation_policy.is_owned \
            and mc.business.event_triggers_dict.get("HR_unlocked", False)
    return False

def Sarah_titles(the_person: Person):
    return [the_person.name]

def Sarah_possessive_titles(the_person: Person):
    valid_possessive_titles = Sarah_titles(the_person)
    valid_possessive_titles.append("your childhood friend")
    if the_person.event_triggers_dict.get("try_for_baby", 0) >= 1:
        valid_possessive_titles.append("your breeding mare")
    return valid_possessive_titles

def Sarah_player_titles(the_person):
    return [mc.name]

def create_sarah_character():
    sarah_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")

    sarah_base_outfit = Outfit("Sarah's base accessories")
    sarah_base_outfit.add_accessory(modern_glasses.get_copy(), [.15, .15, .15, 0.95])
    sarah_base_outfit.add_accessory(light_eye_shadow.get_copy(), [.45, .31, .59, 0.5])

    init_sarah_roles()
    init_HR_directore_roles()

    # initial representative job
    sarah_initial_job = JobDefinition("Representative", critical_job_role, day_slots = [], time_slots = [])

    Sarah_personality = Personality("Sarah", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["skirts", "small talk", "Fridays", "the weekend", "makeup", "flirting", "heavy metal music", "punk music"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her ass", "threesomes", "not wearing underwear", "creampies", "bareback sex"],
        common_dislikes = ["the colour pink", "supply work", "conservative outfits", "work uniforms"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex"],
        titles_function = Sarah_titles, possessive_titles_function = Sarah_possessive_titles, player_titles_function = Sarah_player_titles)

    global sarah
    sarah = make_person(name = "Sarah", last_name ="Cooper", age = 21, body_type = "thin_body", face_style = "Face_3", tits = "A", height = 0.90, hair_colour = ["chocolate", [.247, .0, .058, 1]], hair_style = windswept_hair, skin="white",
        eyes = "dark blue", personality = Sarah_personality, name_color = "#dda0dd", starting_wardrobe = sarah_wardrobe,
        stat_array = [5, 3, 3], skill_array = [5, 3, 2, 1, 1], sex_skill_array = [1, 2, 3, 1], sluttiness = 3, happiness = 102, love = 3, job = sarah_initial_job,
        title = "Sarah", possessive_title = "your childhood friend", mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = sarah_base_outfit,
        forced_opinions = [
            ["HR work", 2, True],        # she loves HR work
            ["work uniforms", 1, False], # she likes uniforms
            ["Mondays", 1, False],       # she likes mondays, and monday meetings!
            ["working", 1, False],       # a bit of a workaholic
            ["the colour black", 1, False],  #She likes black!
            ["the colour purple", 2, False], #She loves purple!
            ["skirts", 1, False],        #And Skirts
            ["the colour red", -2, False], #She hates red
            ["yoga", 2, False]],        # she sets up yoga classes
        forced_sexy_opinions = [
            ["threesomes", 1, False],   # she's interested in threesomes
            ["taking control", 1, False], # she likes taking control, type A
            ["giving handjobs", 2, False], # Not afraid to get her hands dirty ;)
            ["giving blowjobs", 1, False], # make sure she likes blowjobs (HR meeting)
            ["showing her tits", -2, False]],
        work_experience = 2, serum_tolerance = 2, type = 'story')

    sarah.generate_home()
    sarah.add_role(sarah_role)
    sarah.set_override_schedule(sarah.home)
    sarah.home.add_person(sarah)

    # Sarah_mod_initialization(): #Add actionmod as argument#
    # sarah.event_triggers_dict["yoga_voyeur"] = False
    # sarah.event_triggers_dict["gym_tshirt"] = False
    # sarah.event_triggers_dict["epic_tits_progress"] = 0    # 0 = not started, 1 = mandatory event triggered, 2 = tits epic, -1 = convinced her not to do it
    # sarah.event_triggers_dict["drinks_out_progress"] = 0   # 0 = not started, 1 = third wheel event complete, 2 = grab drinks complete
    # sarah.event_triggers_dict["dating_path"] = False       # False = not started, or doing FWB during story, True = dating her.
    # sarah.event_triggers_dict["stripclub_progress"] = 0    # 0 = not complete, 1 = strip club even complete
    # sarah.event_triggers_dict["initial_threesome_target"] = None    #this will hold who sarah decides she wants to have a threesome with.
    # sarah.event_triggers_dict["threesome_unlock"] = False     #\\
    # sarah.event_triggers_dict["try_for_baby"] = 0         # 0 = not trying, 1 = trying for baby, 2 = knocked up
    # sarah.event_triggers_dict["fertile_start_day"] = -1    #-1 means not fertile, otherwise is the day that she tells MC she is fertile. Using math we can determine if she is fertile in the future.
    # sarah.event_triggers_dict["fertile_start_creampie_count"] = -1  #Set this to the total number of creampies she has had at the beginning of her fertile period.
    # sarah.event_triggers_dict["special_tit_fuck"] = False

    # add appointment action
    HR_director_appointment_action = Action("Appoint HR Director", can_appoint_HR_director_requirement, "HR_director_appointment_action_label",
            menu_tooltip = "Pick a member of your HR staff to be your HR director. The HR director will help you manage your employees well-being and motivation.")
    ceo_office.add_action(HR_director_appointment_action)

    mc.create_event("Sarah_intro_label", "Meet someone new", day_restriction = (3, 4, 5, 6), time_restriction = 0, person = sarah)
    # mc.business.add_mandatory_morning_crisis(
    #     Action("Sarah_intro", Sarah_intro_requirement, "Sarah_intro_label")
    # )

def sarah_epic_tits_progress():
    return sarah.event_triggers_dict.get("epic_tits_progress", 0)

def sarah_get_special_titfuck_unlocked():
    return sarah.event_triggers_dict.get("special_tit_fuck", False)

def sarah_get_sex_unlocked():
    return sarah.event_triggers_dict.get("drinks_out_progress", 0) >= 2

def sarah_threesomes_unlocked():
    return sarah.event_triggers_dict.get("threesome_unlock", False)

def Sarah_has_bigger_tits():
    return sarah_epic_tits_progress() > 1 or sarah.has_large_tits

##############
# Story Info #
##############

def sarah_story_character_description():
    return "A long lost childhood friend. Maybe you can spark a flame with her."

#First, setup the love storyline hints and functions.
def sarah_story_20_love_hint():
    if sarah.love < 20:
        return "Try increasing [sarah.fname]'s Love score."
    if sarah.sluttiness < 20:
        return "Try increasing [sarah.fname]'s sluttiness."
    return "[sarah.fname] may ask you out if you are working on a Saturday."

def sarah_story_20_love_complete_func():
    return sarah.event_triggers_dict.get("drinks_out_progress", 0) > 0

def sarah_story_40_love_hint():
    if sarah_epic_tits_progress() == 1:
        return "Wait and see how her tits look on Monday."
    if sarah.love < 40:
        return "Try increasing [sarah.fname]'s Love score."
    if sarah.sluttiness < 40:
        return "Try increasing [sarah.fname]'s sluttiness."
    if not get_HR_director_tag("business_HR_sexy_meeting", False):
        return "Progress [sarah.fname]'s lust story."
    return "[sarah.fname] may ask you out again if you are working on a Saturday."

def sarah_story_40_love_complete_func():
    return sarah.event_triggers_dict.get("drinks_out_progress", 0) > 1

def sarah_story_60_love_hint():
    if sarah_epic_tits_progress() < 2 and not sarah_epic_tits_progress() == -1:
        return "Progress [sarah.fname]'s lust story."
    if strip_club_is_closed():
        return "Progress buying the strip club storyline."
    if sarah.love < 60:
        return "Try increasing [sarah.fname]'s Love score."
    if sarah.sluttiness < 50:
        return "Try increasing [sarah.fname]'s sluttiness."
    return "[sarah.fname] may ask you out again if you are working on a Saturday."

def sarah_story_60_love_complete_func():
    return sarah.event_triggers_dict.get("stripclub_progress", 0) > 0

def sarah_story_80_love_hint():
    if sarah.love < 80:
        return "Try increasing [sarah.fname]'s Love score."
    if sarah.sluttiness < 60:
        return "Try increasing [sarah.fname]'s sluttiness."
    if sarah != mc.business.hr_director:
        return "[sarah.fname] must be your HR Director to progress this story."
    return "[sarah.fname] will give you a special service during your Monday morning meeting soon."

def sarah_story_80_love_complete_func():
    return get_HR_director_unlock("anal lapdance")

def sarah_story_100_love_hint():
    return "This story is complete for now..."

def sarah_story_100_love_complete_func():
    return False

#### Copy and paste these for the other 4 love story events.

def sarah_story_20_lust_hint():
    if sarah.sluttiness < 20:
        return "Try increasing [sarah.fname]'s sluttiness."
    return "Look for [sarah.fname] at the gym on the weekend."

def sarah_story_20_lust_complete_func():
    return sarah.event_triggers_dict.get("yoga_voyeur", False)

def sarah_story_40_lust_hint():
    if sarah != mc.business.hr_director:
        return "[sarah.fname] must be your HR Director to progress this story."
    if sarah.sluttiness < 40:
        return "Try increasing [sarah.fname]'s sluttiness."
    return "[sarah.fname] has a surprise for you during your Monday HR meeting."

def sarah_story_40_lust_complete_func():
    return get_HR_director_unlock("blowjob")

def sarah_story_tit_serum_hint():
    if not mc.business.is_trait_researched(breast_enhancement):
        return "Try researching breast enhancement serums to progress this story."
    return "[sarah.fname] seemed very interested in the breast enhancement serums. Wait for her to steal some."

def sarah_story_tit_serum_complete_func():
    if sarah_epic_tits_progress() < 2 and not sarah_epic_tits_progress() == -1:
        return False
    return True

def sarah_story_60_lust_hint():
    if sarah.sluttiness < 20:
        return "Try increasing [sarah.fname]'s sluttiness."
    return "Look for [sarah.fname] at the gym on the weekend."

def sarah_story_60_lust_complete_func():
    return sarah.event_triggers_dict.get("gym_tshirt", False)

def sarah_story_80_lust_hint():
    if sarah.event_triggers_dict.get("initial_threesome_target", None) is not None:
        return "Arrange the threesome with the person you chose."
    if sarah.sluttiness < 80:
        return "Try increasing [sarah.fname]'s sluttiness."
    if builtins.len(get_Sarah_willing_threesome_list()) <= 3:
        return "Not enough possible threesome partners. Try increasing more girl's sluttiness to at least 80."
    else:
        return "Look for [sarah.fname] at work on Saturdays."

def sarah_story_80_lust_complete_func():
    return sarah_threesomes_unlocked()

def sarah_story_100_lust_complete_func():
    return False

def sarah_story_100_lust_hint():
    return "This story is complete for now..."

#### Copy and paste these for the 4 other lust events.

def sarah_story_teamup_1_hint():
    if not erica.event_triggers_dict.get("yoga_quest_started", False):
        return "Try progressing [erica.fname]'s story."
    if len(erica_get_yoga_class_list()) < 4:
        return "Help [sarah.fname] convince employees to like or love yoga."
    return "Talk to [erica.fname] about hosting a company yoga class."

def sarah_story_teamup_1_complete_func():
    return erica_get_is_doing_yoga_sessions()

#### Repeat this for all different teamups.

def sarah_story_love_list():
    love_story_list = {}
    if sarah_story_20_love_complete_func():
        love_story_list[0] = "[sarah.fname] enjoyed your first date at the bar."
        if sarah_story_40_love_complete_func():
            love_story_list[1] = "[sarah.fname] enjoyed your second date at the bar."
            if sarah_story_60_love_complete_func():
                love_story_list[2] = "[sarah.fname] took you to the strip club."
                if sarah_story_80_love_complete_func():
                    love_story_list[3] = "[sarah.fname] gave you her ass during a Monday meeting!"
                    if sarah_story_100_love_complete_func():
                        pass
                    else:
                        love_story_list[4] = sarah_story_100_love_hint()
                else:
                    love_story_list[3] = sarah_story_80_love_hint()
            else:
                love_story_list[2] = sarah_story_60_love_hint()
        else:
            love_story_list[1] = sarah_story_40_love_hint()
    else:
        love_story_list[0] = sarah_story_20_love_hint()
    return love_story_list

def sarah_story_love_is_complete():
    return sarah_story_80_love_complete_func()

def sarah_story_lust_list():
    lust_story_list = {}
    if sarah_story_20_lust_complete_func():
        lust_story_list[0] = "[sarah.fname] enjoyed when you watched her do yoga at the gym."
        if sarah_story_40_lust_complete_func():
            lust_story_list[1] = "[sarah.fname] gave you a blowjob in your office!"
            if sarah_story_tit_serum_complete_func():
                lust_story_list[2] = "[sarah.fname] stole breast enhancing serums and used them!"
                if sarah_story_60_lust_complete_func():
                    lust_story_list[3] = "[sarah.fname] turned a gym session into a lewd show!"
                    if sarah_story_80_lust_complete_func():
                        lust_story_list[4] = "[sarah.fname] finally had her first threesome."
                        if sarah_story_100_lust_complete_func():
                            pass
                        else:
                            lust_story_list[5] = sarah_story_100_lust_hint()
                    else:
                        lust_story_list[4] = sarah_story_80_lust_hint()
                else:
                    lust_story_list[3] = sarah_story_60_lust_hint()
            else:
                lust_story_list[2] = sarah_story_tit_serum_hint()
        else:
            lust_story_list[1] = sarah_story_40_lust_hint()
    else:
        lust_story_list[0] = sarah_story_20_lust_hint()

    return lust_story_list

def sarah_story_lust_is_complete():
    return sarah_story_80_lust_complete_func()


# def sarah_story_obedience_list():
#     obedience_story_list = {
#         0: "This story step has not yet been written."
#     }
#     return obedience_story_list

def sarah_story_teamup_list() -> dict[int, tuple[Person, str]]:
    teamup_story_list = {}
    if sarah_story_teamup_1_complete_func():
        teamup_story_list[0] = (erica, "Watch [sarah.fname] do yoga with [erica.fname] every Tuesday morning at the office!")
    else:
        teamup_story_list[0] = (erica, sarah_story_teamup_1_hint())
    return teamup_story_list

def sarah_story_other_list():
    other_info_list = {}
    if sarah is mc.business.hr_director:
        other_info_list[0] = "[sarah.fname] is your HR Director"
    else:
        other_info_list[0] = "[sarah.fname] needs to be your HR director to progress most story options."

    if Sarah_has_bigger_tits():
        other_info_list[1] = "[sarah.fname] took serums to make her breasts bigger."
    if sarah_get_special_titfuck_unlocked():
        other_info_list[2] = "[sarah.fname] gives amazing tit fucks!"
    return other_info_list


####################
# Position Filters #
####################

def sarah_foreplay_position_filter(foreplay_position: Position):
    if sarah_get_special_titfuck_unlocked():
        return foreplay_position not in (tit_fuck, )
    return True

def sarah_oral_position_filter(oral_position: Position):
    return True

def sarah_vaginal_position_filter(vaginal_position: Position):
    return sarah_get_sex_unlocked()

def sarah_anal_position_filter(anal_position: Position):
    return sarah_get_sex_unlocked() \
        and sarah.vaginal_creampie_count > 3

def sarah_vaginal_position_info():
    return "You need to complete both weekend date events"

def sarah_anal_position_info():
    count = 4 - sarah.vaginal_creampie_count
    return f"Give her {count} more creampies"

def sarah_unique_sex_positions(person, prohibit_tags) -> list[tuple[Position, int]]:
    positions = []
    if sarah_get_special_titfuck_unlocked() and "Foreplay" not in prohibit_tags:
        positions.append((sarah_tit_fuck, 1))
    return positions
