#This class is designed to hold all the variables and labels required to create a corruption progression scene.
#Class contains labels for all parts of the scene in a list, which progresses automatically in corruption based on specified conditions
#Class should track what stage the progression is at so it can be referenced easily and should save the progress in save file
#Class should compile at startup the list of stages of the progression_scene so that it can be modified and added to as necessary
#Class may have to reference another class in the event of a branching storyline
#Use a character's init file to call their progression scene recompiles.

from __future__ import annotations
from ctypes import ArgumentError
from typing import Callable
import renpy
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.game_logic.Action_ren import Action

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
list_of_progression_scenes: list[Progression_Scene] = []

class Progression_Scene():
    def _parseGroup(self, the_group: list[Person] | Person):
        if isinstance(the_group, (list, tuple, set)):
            return list(the_group)
        if isinstance(the_group, Person):
            return [the_group]
        raise ArgumentError(f"the_group must be a list, tuple, set, or Person. Got {type(the_group)} instead.")

    def __init__(self, compile_scenes: Callable[['Progression_Scene'], None], start_scene_list: list[str], req_list: list[Callable], trans_list: list[str], final_scene_list: list[str],
            intro_scene: str, exit_scene: str, progression_scene_action: Action, choice_scene,
            stage = -1, advance_time = True, business_action = False, person_action = False, is_random = False,
            role_action = False, unit_test_func = None,
            is_multiple_choice = False, multiple_choice_scene = None, regress_scene_list = None):

        self.stage = stage  #The corruption level of the progression_scene event
        self.compile_scenes = compile_scenes #Use this function to recompile the lists. Should be run on game load and initial game start.
        self.intro_scene = intro_scene  #Scene to play the first time this progression_scene is called
        self.exit_scene = exit_scene    #If MC decides not to participate.
        self.choice_scene = choice_scene    #Use this to determine if MC wants to stay or leave the event.
        self.progression_scene_action = progression_scene_action  #Use this as a generic action that can be added to any girl to proc the event.
        self.name = self.progression_scene_action.name
        self.start_scene_list: list[str] = start_scene_list    #Scene to play at the beginning of the progression_scene. Mostly to build lust and set the stage.
        self.req_list = req_list    #Requirements used to determine if we are advancing corruption levels
        self.trans_list = trans_list    #A transition between corruption levels.
        self.final_scene_list = final_scene_list    #The act of the progression_scene itself
        self.advance_time = advance_time    #IF the event should advance time. Probably yes?
        self.business_action = business_action  #If the action should be a business (mandatory) crisis
        self.person_action = person_action      #if the action should be a person (on room enter) crisis
        self.is_random = is_random              #If this action only pops up randomly.
        self.role_action = role_action          #if this a selectable action and is part of a role.
        if unit_test_func is None:              #Set a unit test function
            self.unit_test_func = progression_scene_test_func_default
        else:
            self.unit_test_func = unit_test_func
        self.is_multiple_choice = is_multiple_choice    #Set to true if we want MC to decide which final scene to play.
        self.multiple_choice_scene = multiple_choice_scene  #Use this scene to setup the choice. IE how do you fuck her, etc.
        self.regress_scene_list = regress_scene_list        #Fill this list if we want progress here to be capable of regressing.
        if regress_scene_list is None:
            self.regress_scene_list = []
        self.scene_unlock_list = []                         #Hold a list of scene refences. Should be numbers only, EG: [0,1,2,5]

    def get_stage(self) -> int:
        return self.stage

    def set_stage(self, stage):
        self.stage = stage

    def call_intro(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        renpy.call(self.intro_scene, the_group)

    def call_start_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        if len(self.start_scene_list) < self.stage + 1: #If the list is shorter than the index, assume the last on the list is the function we want to call.
            renpy.call(self.start_scene_list[-1], the_group)
        else:
            renpy.call(self.start_scene_list[self.stage], the_group)

    def call_trans_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        renpy.call(self.trans_list[self.stage], the_group)

    def call_multi_trans_scene(self, the_group: list[Person], the_stage):
        the_group = self._parseGroup(the_group)
        renpy.call(self.trans_list[the_stage], the_group)

    def call_regress_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        renpy.call(self.regress_scene_list[self.stage], the_group)

    def call_final_scene(self, the_group: list[Person], scene_transition):
        the_group = self._parseGroup(the_group)
        renpy.call(self.final_scene_list[self.stage], the_group, scene_transition)

    def call_multi_final_scene(self, the_group: list[Person], scene_transition, the_stage):
        the_group = self._parseGroup(the_group)
        renpy.call(self.final_scene_list[the_stage], the_group, scene_transition)

    def call_exit_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        renpy.call(self.exit_scene, the_group)

    def call_choice_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        return renpy.call(self.choice_scene, the_group)

    def call_multiple_choice_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        return renpy.call(self.multiple_choice_scene, the_group)

    def is_progress_only(self):
        return len(self.regress_scene_list) == 0

    def recompile_scenes(self):
        if callable(self.compile_scenes):
            self.compile_scenes(self)

    def call_scene(self, the_group: list[Person]):
        the_group = self._parseGroup(the_group)
        renpy.call("progression_scene_label", self, the_group)

    def run_unit_test(self, the_group: list[Person], cycles = 10):
        scene_count = 0
        while scene_count < cycles:
            self.call_scene(the_group)
            self.unit_test_func(the_group)

    def run_stage_test(self, the_group: list[Person]):
        renpy.call("progression_scene_stage_test_label", self, the_group)

    def reset_scene(self):
        self.recompile_scenes()
        self.scene_unlock_list = []
        self.stage = -1

    @property
    def progression_available(self) -> bool:
        if self.is_multiple_choice:
            counter = 0
            while counter < len(self.trans_list):
                if counter not in self.scene_unlock_list and self.req_list[counter]():
                    return True
                counter += 1
            return False
            #Check all choices for possible progression.
        elif len(self.req_list) > self.stage + 1: #Only try if there is another scene
            return self.req_list[self.stage + 1]()
        return False

    def update(self):   #I don't think this function actually works?
        if self.role_action:
            if self.progression_available:
                self.progression_scene_action.name = self.name + " {image=progress_token_small}"
            else:
                self.progression_scene_action.name = self.name


#Default function to run between cycles if we do a default unit test.
def progression_scene_test_func_default(the_group: list[Person] = None):
    if the_group is None:
        the_group = []
    for person in the_group:
        person.change_slut(10, 100)
        person.change_energy(200)
