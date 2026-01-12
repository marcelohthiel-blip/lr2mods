from __future__ import annotations
import builtins
import renpy
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Room_ren import Room, RoomObject

girl_swap_pos = True
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

class Threesome_MC_position():
    def __init__(self, name, skill_tag_p1, skill_tag_p2, girl_one_arousal, girl_two_arousal, girl_one_source, girl_two_source, girl_one_energy, girl_two_energy,
            guy_arousal, skill_tag_guy, guy_source, guy_energy, intro, scenes, outro, strip_description, strip_ask_description, orgasm_description, swap_description, requirement,
            description = None, action_description = None, default_action_person = None):
        self.name = name
        self.description = description #Describes the position the MC is in
        self.action_description = action_description # Template for action {0} will be replaced with the action person number (one/two -> used for swap girls - description update)
        self.default_action_person = default_action_person
        self.skill_tag_p1 = skill_tag_p1 #The skill that will provide a bonus to this for girl 1
        self.skill_tag_p2 = skill_tag_p2 #The skill that will provide a bonus to this for girl 2
        self.girl_one_arousal = girl_one_arousal # The base arousal the girl receives from this position.
        self.girl_two_arousal = girl_two_arousal # The base arousal the girl receives from this position.
        self.girl_one_source = girl_one_source  #Who is giving girl 1 pleasure. 0 = MC, 1 = herself, 2 = girl 2
        self.girl_two_source = girl_two_source  #Who is giving girl 2 pleasure. 0 = MC, 1 = girl 1, 2 = herself
        self.girl_one_energy = girl_one_energy  #energy cost for girl 1
        self.girl_two_energy = girl_two_energy  #energy cost for girl 2
        self.guy_arousal = guy_arousal # The base arousal the guy receives from this position.
        self.skill_tag_guy = skill_tag_guy #The skill that will decide how much arousal MC receives.
        self.guy_source = guy_source # Who is giving MC pleasure. 0 = MC, 1 = girl 1, 2 = girl 2
        self.guy_energy = guy_energy #Energy burn for guy
        self.intro = intro
        self.scenes = scenes
        self.outro = outro
        self.strip_description = strip_description
        self.strip_ask_description = strip_ask_description
        self.orgasm_description = orgasm_description
        self.swap_description = swap_description
        self.requirement = requirement

    def call_intro(self, person_one: Person, person_two: Person, the_location: Room, the_object: RoomObject):
        if girl_swap_pos:
            renpy.call(self.intro, person_two, person_one, the_location, the_object)
        else:
            renpy.call(self.intro, person_one, person_two, the_location, the_object)

    def call_scene(self, person_one: Person, person_two: Person, the_location: Room, the_object: RoomObject):
        random_scene = renpy.random.randint(0, builtins.len(self.scenes) - 1)
        if girl_swap_pos:
            renpy.call(self.scenes[random_scene], person_two, person_one, the_location, the_object)
        else:
            renpy.call(self.scenes[random_scene], person_one, person_two, the_location, the_object)

    def call_orgasm(self, person_one: Person, person_two: Person, the_location: Room, the_object: RoomObject):
        if girl_swap_pos:
            renpy.call(self.orgasm_description, person_two, person_one, the_location, the_object)
        else:
            renpy.call(self.orgasm_description, person_one, person_two, the_location, the_object)

    def call_outro(self, person_one: Person, person_two: Person, the_location: Room, the_object: RoomObject):
        if girl_swap_pos:
            renpy.call(self.outro, person_two, person_one, the_location, the_object)
        else:
            renpy.call(self.outro, person_one, person_two, the_location, the_object)

    def call_transition(self, person_one: Person, person_two: Person, the_location: Room, the_object: RoomObject):
        if girl_swap_pos:
            renpy.call(self.swap_description, person_two, person_one, the_location, the_object)
        else:
            renpy.call(self.swap_description, person_one, person_two, the_location, the_object)

    def check_girl_one_energy(self, person_one: Person) -> bool:
        if girl_swap_pos:
            if self.girl_two_energy > person_one.energy:
                return False
        elif self.girl_one_energy > person_one.energy:
            return False
        return True

    def check_girl_two_energy(self, person_two: Person) -> bool:
        if girl_swap_pos:
            if self.girl_one_energy > person_two.energy:
                return False
        elif self.girl_two_energy > person_two.energy:
            return False
        return True

    def calc_arousal_changes(self, person_one: Person, person_two: Person):
        #Calculate arousal gains
        if girl_swap_pos:
            girl_one_arousal_change = self.girl_two_arousal + ((person_one.opinion.threesomes / 5) * self.girl_two_arousal)   #20% arousal bonus for each level of threesome like/dislike
            if self.girl_two_source == 0:  #MC is source#
                girl_one_arousal_change += girl_one_arousal_change * mc.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
            elif self.girl_two_source == 1:
                girl_one_arousal_change += girl_one_arousal_change * person_one.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
            else:  #Assume girl 2 is source
                girl_one_arousal_change += girl_one_arousal_change * person_two.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
        else:
            girl_one_arousal_change = self.girl_one_arousal + ((person_one.opinion.threesomes / 5) * self.girl_one_arousal)   #20% arousal bonus for each level of threesome like/dislike
            if self.girl_one_source == 0:  #MC is source#
                girl_one_arousal_change += girl_one_arousal_change * mc.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
            elif self.girl_one_source == 1: #Girl one is her own source? Maybe masturbating?
                girl_one_arousal_change += girl_one_arousal_change * person_one.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
            else:  #Assume girl 2 is source
                girl_one_arousal_change += girl_one_arousal_change * person_two.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level

        person_one.change_arousal(girl_one_arousal_change)  #Make the change

        #Repeat for girl two
        if girl_swap_pos:
            girl_two_arousal_change = self.girl_one_arousal + ((person_two.opinion.threesomes / 5) * self.girl_one_arousal)   #20% arousal bonus for each level of threesome like/dislike
            if self.girl_one_source == 0:  #MC is source#
                girl_two_arousal_change += girl_two_arousal_change * mc.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
            elif self.girl_one_source == 1: #Girl 1 is source
                girl_two_arousal_change += girl_two_arousal_change * person_one.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
            else:  #Assume girl 2 is source
                girl_two_arousal_change += girl_two_arousal_change * person_two.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
        else:
            girl_two_arousal_change = self.girl_two_arousal + ((person_two.opinion.threesomes / 5) * self.girl_two_arousal)   #20% arousal bonus for each level of threesome like/dislike
            if self.girl_two_source == 0:  #MC is source#
                girl_two_arousal_change += girl_two_arousal_change * mc.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
            elif self.girl_two_source == 1: #Girl 1 is source
                girl_two_arousal_change += girl_two_arousal_change * person_one.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
            else:  #Assume girl 2 is source
                girl_two_arousal_change += girl_two_arousal_change * person_two.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level

        person_two.change_arousal(girl_two_arousal_change)  #Make the change

        #MC arousal change
        his_arousal_change = self.guy_arousal
        if self.guy_source == 0:
            his_arousal_change += 0.1 * mc.sex_skills[self.skill_tag_guy]
        elif girl_swap_pos:
            if self.guy_source == 1:
                his_arousal_change += 0.1 * person_two.sex_skills[self.skill_tag_guy]
            else:
                his_arousal_change += 0.1 * person_one.sex_skills[self.skill_tag_guy]
        elif self.guy_source == 1:
            his_arousal_change += 0.1 * person_one.sex_skills[self.skill_tag_guy]
        else:
            his_arousal_change += 0.1 * person_two.sex_skills[self.skill_tag_guy]

        mc.change_arousal(his_arousal_change)

    def get_mc_pleasure_source(self, person_one: Person, person_two: Person) -> Person:
        if self.guy_source == 0:
            return None #Masturbating
        if girl_swap_pos:
            if self.guy_source == 1:
                return person_two
            return person_one
        if self.guy_source == 1:
            return person_one
        return person_two
