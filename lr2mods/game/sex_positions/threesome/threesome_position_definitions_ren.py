from __future__ import annotations
from game.main_character.perks.Perks_ren import perk_system
from game.major_game_classes.character_related.Person_ren import Person, mc

from game.sex_positions.threesome.Threesome_MC_position_ren import Threesome_MC_position
from game.sex_positions.threesome.Threesome_Position_ren import Threesome_Position

list_of_threesomes: list[Threesome_Position] = []

Threesome_doggy_deluxe_girl_one_transform = None
Threesome_doggy_deluxe_girl_two_transform = None
threesome_double_blowjob_one_transform = None
threesome_double_blowjob_two_transform = None
Threesome_double_down_girl_one_transform = None
Threesome_double_down_girl_two_transform = None
character_69_bottom = None
character_69_on_top = None
Threesome_standing_embrace_girl_one_transform = None
Threesome_standing_embrace_girl_two_transform = None
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def requirement_always_true(the_person_one, the_person_two):
    return True

def requirement_disable_position(the_person_one, the_person_two):
    return False

def requirement_hard(the_person_one, the_person_two):
    return not mc.recently_orgasmed

def requirement_both_vagina_available(the_person_one: Person, the_person_two: Person):
    return the_person_one.vagina_available and the_person_two.vagina_available

def requirement_hard_both_vagina_available(the_person_one: Person, the_person_two: Person):
    if requirement_both_vagina_available(the_person_one, the_person_two):
        return requirement_hard(the_person_one, the_person_two)
    return False

def requirement_hard_both_vagina_male_strapon(the_person_one: Person, the_person_two: Person):
    if requirement_hard_both_vagina_available(the_person_one, the_person_two):
        return perk_system.has_item_perk("Male Strapon")
    return False

def requirement_hard_both_vagina_both_like_anal(the_person_one: Person, the_person_two: Person):
    if not requirement_hard_both_vagina_available(the_person_one, the_person_two):
        return False
    if (the_person_one.opinion.anal_sex < 0
            or the_person_two.opinion.anal_sex < 0):
        return False
    return True

Threesome_doggy_deluxe_fuck_girl_two = Threesome_MC_position(name = "fuck_girl_2",
    action_description = "Fuck [the_person_{0}.title]",
    default_action_person = "two",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Vaginal",
    girl_one_arousal = 18,
    girl_two_arousal = 22,
    girl_one_source = 2,
    girl_two_source = 0,
    girl_one_energy = 8,
    girl_two_energy = 13,
    guy_arousal = 20,
    guy_source = 2,
    guy_energy = 10,
    skill_tag_guy = "Vaginal",
    intro = "intro_threesome_doggy_deluxe_fuck_girl_two",
    scenes = ["scene_threesome_doggy_deluxe_fuck_girl_two_1", "scene_threesome_doggy_deluxe_fuck_girl_two_2"],
    outro = "outro_threesome_doggy_deluxe_fuck_girl_two",
    strip_description = "strip_threesome_doggy_deluxe_fuck_girl_two",
    strip_ask_description = "strip_ask_threesome_doggy_deluxe_fuck_girl_two",
    orgasm_description = "orgasm_threesome_doggy_deluxe_fuck_girl_two",
    swap_description = "swap_threesome_doggy_deluxe_fuck_girl_two",
    requirement = requirement_hard_both_vagina_available)

Threesome_doggy_deluxe_anal_girl_two = Threesome_MC_position(name = "anal_girl_2",
    action_description = "Fuck [the_person_{0}.title]'s ass",
    default_action_person = "two",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Anal",
    girl_one_arousal = 18,
    girl_two_arousal = 22,
    girl_one_source = 2,
    girl_two_source = 0,
    girl_one_energy = 8,
    girl_two_energy = 14,
    guy_arousal = 22,
    guy_source = 2,
    guy_energy = 10,
    skill_tag_guy = "Anal",
    intro = "intro_threesome_doggy_deluxe_anal_girl_two",
    scenes = ["scene_threesome_doggy_deluxe_anal_girl_two_1", "scene_threesome_doggy_deluxe_anal_girl_two_2"],
    outro = "outro_threesome_doggy_deluxe_anal_girl_two",
    strip_description = "strip_threesome_doggy_deluxe_anal_girl_two",
    strip_ask_description = "strip_ask_threesome_doggy_deluxe_anal_girl_two",
    orgasm_description = "orgasm_threesome_doggy_deluxe_anal_girl_two",
    swap_description = "swap_threesome_doggy_deluxe_anal_girl_two",
    requirement = requirement_disable_position) #WIP for now

Threesome_doggy_deluxe_watch_girls = Threesome_MC_position(name = "watch_girls",
    description = "Watch the Girls",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 15,
    girl_two_arousal = 15,
    girl_one_source = 2,
    girl_two_source = 1,
    girl_one_energy = 10,
    girl_two_energy = 10,
    guy_arousal = 6,
    guy_source = 0,
    guy_energy = 5,
    skill_tag_guy = "Foreplay",
    intro = "intro_threesome_doggy_deluxe_watch_girls",
    scenes = ["scene_threesome_doggy_deluxe_watch_girls"],
    outro = "outro_threesome_doggy_deluxe_watch_girls",
    strip_description = "strip_threesome_doggy_deluxe_watch_girls",
    strip_ask_description = "strip_ask_threesome_doggy_deluxe_watch_girls",
    orgasm_description = "orgasm_threesome_doggy_deluxe_watch_girls",
    swap_description = "swap_threesome_doggy_deluxe_watch_girls",
    requirement = requirement_disable_position) #WIP

Threesome_doggy_deluxe_dp_girl_two = Threesome_MC_position(name = "DP_girl_2",
    action_description = "Fuck [the_person_{0}.title]'s ass and pussy using strap-on",
    default_action_person = "two",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Anal",
    girl_one_arousal = 18,
    girl_two_arousal = 25,   #Intense sex for girl 2
    girl_one_source = 2,
    girl_two_source = 0,
    girl_one_energy = 8,
    girl_two_energy = 14,
    guy_arousal = 22,
    guy_source = 2,
    guy_energy = 10,
    skill_tag_guy = "Anal",
    intro = "intro_threesome_doggy_deluxe_dp_girl_two",
    scenes = ["scene_threesome_doggy_deluxe_dp_girl_two_1", "scene_threesome_doggy_deluxe_dp_girl_two_2"],
    outro = "outro_threesome_doggy_deluxe_dp_girl_two",
    strip_description = "strip_threesome_doggy_deluxe_dp_girl_two",
    strip_ask_description = "strip_ask_threesome_doggy_deluxe_dp_girl_two",
    orgasm_description = "orgasm_threesome_doggy_deluxe_dp_girl_two",
    swap_description = "swap_threesome_doggy_deluxe_dp_girl_two",
    requirement = requirement_hard_both_vagina_male_strapon) #WIP for now

Threesome_doggy_deluxe = Threesome_Position(name = "Doggy Deluxe",
    slut_requirement = 60,
    position_one_tag = "missionary",
    position_two_tag = "doggy",
    girl_one_final_description = "On your back and let her eat you out",
    girl_two_final_description = "Eat her out while on your hands and knees",
    requires_location = "Lay",
    requirements = requirement_hard_both_vagina_available,
    verb = "fuck",
    p1_transform = Threesome_doggy_deluxe_girl_one_transform,
    p2_transform = Threesome_doggy_deluxe_girl_two_transform,
    p1_z_order = 0,
    p2_z_order = 1,
    can_swap = True,
    mc_position = [Threesome_doggy_deluxe_fuck_girl_two, Threesome_doggy_deluxe_anal_girl_two, Threesome_doggy_deluxe_watch_girls, Threesome_doggy_deluxe_dp_girl_two])

list_of_threesomes.append(Threesome_doggy_deluxe)


threesome_double_blowjob_focus_oral = Threesome_MC_position(name = "focus_oral",
    description = "Focus on You",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 5,
    girl_two_arousal = 5,
    girl_one_source = 0,
    girl_two_source = 0,
    girl_one_energy = 15,
    girl_two_energy = 15,
    guy_arousal = 20,
    guy_source = 1,
    guy_energy = 5,
    skill_tag_guy = "Oral",
    intro = "intro_threesome_double_blowjob_focus_oral",
    scenes = ["scene_threesome_double_blowjob_focus_oral_1", "scene_threesome_double_blowjob_focus_oral_2"],
    outro = "outro_threesome_double_blowjob_focus_oral",
    strip_description = "strip_threesome_double_blowjob_focus_oral",
    strip_ask_description = "strip_ask_threesome_double_blowjob_focus_oral",
    orgasm_description = "orgasm_threesome_double_blowjob_focus_oral",
    swap_description = "swap_threesome_double_blowjob_focus_oral",
    requirement = requirement_hard)

threesome_double_blowjob_makeout = Threesome_MC_position(name = "Makeout",
    description = "Watch Girls Makeout",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 12,
    girl_two_arousal = 12,
    girl_one_source = 2,
    girl_two_source = 1,
    girl_one_energy = 15,
    girl_two_energy = 15,
    guy_arousal = 20,
    guy_source = 1,
    guy_energy = 5,
    skill_tag_guy = "Oral",
    intro = "intro_threesome_double_blowjob_makeout",
    scenes = ["scene_threesome_double_blowjob_makeout_1", "scene_threesome_double_blowjob_makeout_2"],
    outro = "outro_threesome_double_blowjob_makeout",
    strip_description = "strip_threesome_double_blowjob_makeout",
    strip_ask_description = "strip_ask_threesome_double_blowjob_makeout",
    orgasm_description = "orgasm_threesome_double_blowjob_makeout",
    swap_description = "swap_threesome_double_blowjob_makeout",
    requirement = requirement_always_true)

threesome_double_blowjob = Threesome_Position(name = "Double Blowjob",
    slut_requirement = 60,
    position_one_tag = "blowjob",
    position_two_tag = "blowjob",
    girl_one_final_description = "On your knees too",
    girl_two_final_description = "On your knees too",
    requires_location = "Kneel",
    requirements = requirement_always_true,
    verb = "throat fuck",
    p1_transform = threesome_double_blowjob_one_transform,
    p2_transform = threesome_double_blowjob_two_transform,
    can_swap = True,
    mc_position = [threesome_double_blowjob_focus_oral, threesome_double_blowjob_makeout])

list_of_threesomes.append(threesome_double_blowjob)


Threesome_double_down_fuck_girl_one = Threesome_MC_position(name = "fuck_girl_1",
    description = "Enjoy the Ride",
    skill_tag_p1 = "Vaginal",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 20,
    girl_two_arousal = 20,
    girl_one_source = 0,
    girl_two_source = 0,
    girl_one_energy = 11,
    girl_two_energy = 11,
    guy_arousal = 20,
    guy_source = 1,
    guy_energy = 8,
    skill_tag_guy = "Vaginal",
    intro = "intro_threesome_double_down_fuck_girl_one",
    scenes = ["scene_threesome_double_down_fuck_girl_one_1", "scene_threesome_double_down_fuck_girl_one_2"],
    outro = "outro_threesome_double_down_fuck_girl_one",
    strip_description = "strip_threesome_double_down_fuck_girl_one",
    strip_ask_description = "strip_ask_threesome_double_down_fuck_girl_one",
    orgasm_description = "orgasm_threesome_double_down_fuck_girl_one",
    swap_description = "swap_threesome_double_down_fuck_girl_one",
    requirement = requirement_hard_both_vagina_available)

Threesome_double_down_ass_play = Threesome_MC_position(name = "Ass Play",
    description = "Anal Play",
    skill_tag_p1 = "Anal",
    skill_tag_p2 = "Anal",
    girl_one_arousal = 20,
    girl_two_arousal = 20,
    girl_one_source = 0,
    girl_two_source = 0,
    girl_one_energy = 12,
    girl_two_energy = 10,
    guy_arousal = 20,
    guy_source = 1,
    guy_energy = 10,
    skill_tag_guy = "Anal",
    intro = "intro_threesome_double_down_ass_play",
    scenes = ["scene_threesome_double_down_ass_play_1", "scene_threesome_double_down_ass_play_2"],
    outro = "outro_threesome_double_down_ass_play",
    strip_description = "strip_threesome_double_down_ass_play",
    strip_ask_description = "strip_ask_threesome_double_down_ass_play",
    orgasm_description = "orgasm_threesome_double_down_ass_play",
    swap_description = "swap_threesome_double_down_ass_play",
    #requirement = requirement_hard_both_vagina_both_like_anal)
    requirement = requirement_disable_position)  #Disabled until it gets written

Threesome_double_down = Threesome_Position(name = "Double Down",
    slut_requirement = 60,
    position_one_tag = "cowgirl",
    position_two_tag = "doggy",
    girl_one_final_description = "Ride my cock",
    girl_two_final_description = "Ride my face",
    requires_location = "Lay",
    requirements = requirement_hard_both_vagina_available,
    verb = "fuck",
    p1_transform = Threesome_double_down_girl_one_transform,
    p2_transform = Threesome_double_down_girl_two_transform,
    p1_z_order = 0,
    p2_z_order = 1,
    can_swap = True,
    mc_position = [Threesome_double_down_fuck_girl_one, Threesome_double_down_ass_play])

list_of_threesomes.append(Threesome_double_down)


Threesome_sixty_nine_fuck_girl_one = Threesome_MC_position(name = "fuck_girl_1",
    action_description = "Fuck [the_person_{0}.title]",
    default_action_person = "one",
    skill_tag_p1 = "Vaginal",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 22,
    girl_two_arousal = 20,
    girl_one_source = 0,
    girl_two_source = 1,
    girl_one_energy = 12,
    girl_two_energy = 10,
    guy_arousal = 20,
    guy_source = 1,
    guy_energy = 10,
    skill_tag_guy = "Vaginal",
    intro = "intro_threesome_sixty_nine_fuck_girl_one",
    scenes = ["scene_threesome_sixty_nine_fuck_girl_one_1", "scene_threesome_sixty_nine_fuck_girl_one_2"],
    outro = "outro_threesome_sixty_nine_fuck_girl_one",
    strip_description = "strip_threesome_sixty_nine_fuck_girl_one",
    strip_ask_description = "strip_ask_threesome_sixty_nine_fuck_girl_one",
    orgasm_description = "orgasm_threesome_sixty_nine_fuck_girl_one",
    swap_description = "swap_threesome_sixty_nine_fuck_girl_one",
    requirement = requirement_hard_both_vagina_available)

Threesome_sixty_nine_oral_girl_two = Threesome_MC_position(name = "oral_girl_2",
    action_description = "Get Blowjob from [the_person_{0}.title]",
    default_action_person = "two",
    skill_tag_p1 = "Foreplay",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 16,
    girl_two_arousal = 20,
    girl_one_source = 0,
    girl_two_source = 1,
    girl_one_energy = 9,
    girl_two_energy = 13,
    guy_arousal = 18,
    guy_source = 2,
    guy_energy = 10,
    skill_tag_guy = "Oral",
    intro = "intro_threesome_sixty_nine_oral_girl_two",
    scenes = ["scene_threesome_sixty_nine_oral_girl_two_1", "scene_threesome_sixty_nine_oral_girl_two_2"],
    outro = "outro_threesome_sixty_nine_oral_girl_two",
    strip_description = "strip_threesome_sixty_nine_oral_girl_two",
    strip_ask_description = "strip_ask_threesome_sixty_nine_oral_girl_two",
    orgasm_description = "orgasm_threesome_sixty_nine_oral_girl_two",
    swap_description = "swap_threesome_sixty_nine_oral_girl_two",
    requirement = requirement_hard_both_vagina_available)

Threesome_sixty_nine_watch_girls = Threesome_MC_position(name = "watch_girls",
    description = "Watch the Girls",
    skill_tag_p1 = "Oral",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 15,
    girl_two_arousal = 15,
    girl_one_source = 2,
    girl_two_source = 1,
    girl_one_energy = 10,
    girl_two_energy = 10,
    guy_arousal = 6,
    guy_source = 0,
    guy_energy = 5,
    skill_tag_guy = "Foreplay",
    intro = "intro_threesome_sixty_nine_watch_girls",
    scenes = ["scene_threesome_sixty_nine_watch_girls"],
    outro = "outro_threesome_sixty_nine_watch_girls",
    strip_description = "strip_threesome_sixty_nine_watch_girls",
    strip_ask_description = "strip_ask_threesome_sixty_nine_watch_girls",
    orgasm_description = "orgasm_threesome_sixty_nine_watch_girls",
    swap_description = "swap_threesome_sixty_nine_watch_girls",
    requirement = requirement_always_true)

Threesome_sixty_nine = Threesome_Position(name = "Sixty Nine Plus One",
    slut_requirement = 60,
    position_one_tag = "missionary",
    position_two_tag = "cowgirl",
    girl_one_final_description = "On your back and eat her out",
    girl_two_final_description = "Face me and ride her face",
    requires_location = "Lay",
    requirements = requirement_always_true,
    verb = "fuck",
    p1_transform = character_69_bottom,
    p2_transform = character_69_on_top,
    p1_z_order = 0,
    p2_z_order = 1,
    can_swap = True,
    mc_position = [Threesome_sixty_nine_fuck_girl_one, Threesome_sixty_nine_oral_girl_two, Threesome_sixty_nine_watch_girls])

list_of_threesomes.append(Threesome_sixty_nine)


Threesome_standing_embrace_fuck_girl_two = Threesome_MC_position(name = "fuck_girl_2",
    action_description = "Fuck [the_person_{0}.title]",
    default_action_person = "two",
    skill_tag_p1 = "Foreplay",
    skill_tag_p2 = "Vaginal",
    girl_one_arousal = 10,
    girl_two_arousal = 20,
    girl_one_source = 2,
    girl_two_source = 0,
    girl_one_energy = 7,
    girl_two_energy = 12,
    guy_arousal = 18,
    guy_source = 2,
    guy_energy = 10,
    skill_tag_guy = "Vaginal",
    intro = "intro_threesome_standing_embrace_fuck_girl_two",
    scenes = ["scene_threesome_standing_embrace_fuck_girl_two_1", "scene_threesome_standing_embrace_fuck_girl_two_2"],
    outro = "outro_threesome_standing_embrace_fuck_girl_two",
    strip_description = "strip_threesome_standing_embrace_fuck_girl_two",
    strip_ask_description = "strip_ask_threesome_standing_embrace_fuck_girl_two",
    orgasm_description = "orgasm_threesome_standing_embrace_fuck_girl_two",
    swap_description = "swap_threesome_standing_embrace_fuck_girl_two",
    requirement = requirement_hard_both_vagina_available)

Threesome_standing_embrace_oral_girl_two = Threesome_MC_position(name = "Oral_girl_2",
    action_description = "Lick [the_person_{0}.title]",
    default_action_person = "two",
    skill_tag_p1 = "Foreplay",
    skill_tag_p2 = "Oral",
    girl_one_arousal = 15,
    girl_two_arousal = 18,
    girl_one_source = 0,
    girl_two_source = 0,
    girl_one_energy = 7,
    girl_two_energy = 7,
    guy_arousal = 2,
    guy_source = 2,
    guy_energy = 14,
    skill_tag_guy = "Oral",
    intro = "intro_Threesome_standing_embrace_oral_girl_2",
    scenes = ["scene_Threesome_standing_embrace_oral_girl_2_1", "scene_Threesome_standing_embrace_oral_girl_2_2"],
    outro = "outro_Threesome_standing_embrace_oral_girl_2",
    strip_description = "strip_Threesome_standing_embrace_oral_girl_2",
    strip_ask_description = "strip_ask_Threesome_standing_embrace_oral_girl_2",
    orgasm_description = "orgasm_Threesome_standing_embrace_oral_girl_2",
    swap_description = "swap_Threesome_standing_embrace_oral_girl_2",
    #requirement = requirement_both_vagina_available)
    requirement = requirement_disable_position)  #Disabled until it gets written

Threesome_standing_embrace = Threesome_Position(name = "Standing Embrace",
    slut_requirement = 60,
    position_one_tag = "kissing",
    position_two_tag = "back_peek",
    girl_one_final_description = "Embrace each other",
    girl_two_final_description = "Embrace each other",
    requires_location = "Stand",
    requirements = requirement_hard_both_vagina_available,
    verb = "fuck",
    p1_transform = Threesome_standing_embrace_girl_one_transform,
    p2_transform = Threesome_standing_embrace_girl_two_transform,
    p1_z_order = 0,
    p2_z_order = 1,
    can_swap = True,
    mc_position = [Threesome_standing_embrace_fuck_girl_two, Threesome_standing_embrace_oral_girl_two])

list_of_threesomes.append(Threesome_standing_embrace)
