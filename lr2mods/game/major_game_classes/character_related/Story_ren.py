# Python file for Story_Path and Story_Step class
# Implementation of Path and Step allows us to define entire storylines in python only, allowing them to be loaded at runtime instead of saved to characters.
# Story_Step and Story_Path should only be modified by code, never in game via labels so that they can be modified and expanded easily.
# Characters keep track of what Story_Paths are available and applicable to them, and what step they are on.

from __future__ import annotations
from typing import Callable
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.character_related.Person_ren import mc

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 10
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

class Story_Step():

    def __init__(self, init_func: Callable, finish_func: Callable, cheat_to_func: Callable, cheat_past_func: Callable, remove_func: Callable,
            progress_desc: Callable):

        self.init_func = init_func                  #This function runs when this step is initiated. Used to add appropriate events
        self.finish_func = finish_func              #Use this function to finish a story step. Used to cleanup any remaining events.
        self.cheat_to_func = cheat_to_func          #Use this function in the cheat menu. Should be followed by init_func, use to set stats and variables appropriately.
        self.cheat_past_func = cheat_past_func      #Use thus function if we are cheating thru this step. Use to set stats and variables.
        self.remove_func = remove_func              #Use this to straight up remove a step without completing it. Useful for things like quitting jobs, etc.
        self.progress_desc = progress_desc          #Returns a string used by the progress screen. Pass in Person and Whether or not the step is complete.

        return

    def init_step(self, person: Person):
        if callable(self.init_func):
            return self.init_func(person)
        return False

    def finish_step(self, person: Person):
        if callable(self.finish_func):
            return self.finish_func(person)
        return False

    def cheat_past(self, person: Person):
        if callable(self.cheat_past_func):
            return self.cheat_past_func(person)

    def cheat_to(self, person: Person):
        if callable(self.cheat_to_func):
            return self.cheat_to_func(person)

    def remove_step(self, person: Person):
        if callable(self.remove_func):
            return self.remove_func(person)
        return False

    def step_progress(self, person: Person, complete: bool):
        if callable(self.progress_desc):
            return self.progress_desc(person, complete)
        return "Story Progress Error"


class Story_Path():
    def __init__(self, name: str, step_list: list[Story_Step], start_active = True, path_requirement = None, path_req_desc = "", path_prog_prefix = None):

        self.name = name                    #Used to display the name of the story arc in the progress screen
        self.step_list = step_list          #A list of all the Class Steps in this story
        # Action list? Use for story specific actions that we add to the general interaction list?
        self.start_active = start_active    #True means this story is active right at load. If we want it to start deactive, set to False.
                                            #Examples of starting deactive would be things like a Job change, EG Jennifer as a personal secretary.
        self.path_requirement = path_requirement    #A requirement function that must be true in order for this path to continue or to be started.
        self.path_req_desc = path_req_desc      #A description of the requirement function, if it returns false.
        self.path_prog_prefix = path_prog_prefix    #A callable that returns a string that can be listed at the beginnign of any progress screen dicts.
        return

    ### Information Functions ###
    def get_name(self):
        return self.name

    def story_length(self):
        return len(self.step_list)

    #Begins the story path from the beginning.
    def start_path(self, person: Person):
        self.step_list[0].init_step(person)
        return

    ### Functions for moving between steps ###
    #NOTE: step_index in these functions will ALWAYS refer to the current story step BEFORE the function started.
    def next_step(self, person: Person, step_index: int):
        self.step_list[step_index].finish_step(person)  #Finish the current step
        if 0 <= step_index + 1 < self.story_length():   #Make sure the next step exists
            return self.step_list[step_index + 1].init_step(person)       #Init the next step
        return False        #Return False if we can't move on to the next step. person can mark the storyline as finished, or attempt to add the step again at a later point.

    # Used to explicitly set a starting step for a story arc.
    def set_step(self, person: Person, step_index: int):
        #First, remove all current events
        for story_step in self.step_list:
            story_step.remove_step(person)
        #Next, cheat past prior steps to set appropriate variables
        tracking_index = 0
        while tracking_index < step_index:  #Less than because these are only steps we are cheating PAST
            self.step_list[tracking_index].cheat_past(person)
            tracking_index += 1
        self.step_list[step_index].cheat_to(person)     #To our new index
        self.step_list[step_index].init_step(person)    #Init the new index
        return True

    def pause_path(self, person: Person, step_index: int):
        return self.step_list[step_index].remove_step(person)

    def resume_path(self, person: Person, step_index: int):
        return self.step_list[step_index].init_step(person)

    ### Progress Functions ###
    def progress_description(self, person: Person, step_index: int):
        if callable(self.path_requirement):
            if not self.path_requirement():
                return {0: self.path_req_desc}
        progress_dict = {}
        tracking_index = 0
        while tracking_index < step_index:  #Completed steps first
            progress_dict[tracking_index] = (self.step_list[tracking_index].step_progress(person, True) + "\n")
            tracking_index += 1
        progress_dict[step_index] = self.step_list[step_index].step_progress(person, False)
        #NOTE: This currently doesn't have a condition for a completed storyline?
        #TODO figure out a way to add the prefix callable to the beginning of the returned dict while keeping the indices intact
        return progress_dict

    ### Cleanup Functions ###
    def remove_path(self, person: Person):
        for story_step in self.step_list:
            story_step.remove_step(person)
        return True


#Group Story Path, AKA Harems
#Group Stories are similar to regular story paths, but are owned by MC and need to link to multiple other paths

class Group_Story_Path(Story_Path):
    def __init__(self, name: str, step_list: list[Story_Step],
                 linked_paths: list[Story_Path], path_index_requirement: list[tuple], start_active = True, path_requirement = None, path_req_desc = "",):
        super().__init__(name, step_list, start_active, path_requirement, path_req_desc)

        #Stores the per person paths for each member of this group story.
        #EG, A harem story will have a group_story_path, with links to each individual path
        #Home_Insta_Harem ------- > Lily_Insta_Story
        #                 \
        #                  ------ > Jennifer_Insta_Story
        #
        #Each per person story advances on it's own pace, with the Group story advancing when appropriate
        self.linked_paths = linked_paths

        #Hold required step of linked paths to progress the group story.
        # NOTE: linked_paths should be an ordered list, with the tuples matching the order of the linked paths.
        # EG, if the group path has two individuals, and their individual paths are required to be at step 4 and step 2 to advance, respectively...
        # The Tuple for thie step index need to be (4, 2), matching their order in linked_paths
        self.path_index_requirement = path_index_requirement

# Temporary class
# Should be added to Progression Class when it is ready, or possibly replace progression?
# Controls Story Paths
class Story_Tracker():
    def __init__(self, person: Person):
        # A dict with all the stories for the appropriate character.
        # dict key is the story_path.name
        # Each reference contains the path itself, the current step, whether the path is active or not, and whether the path is complete
        # [0] = the Path         (story_path)
        # [1] = Current Step     (int)
        # [2] = Path is Active   (bool)
        # [3] = Path is complete (bool)
        self.story_dict: dict[str, tuple[str, int, bool, bool]] = {}

        dict_string_prefix = (person.func_name + "_story_path")     #We load the story paths automatically for people on init based on the path name
        for x in globals():
            if dict_string_prefix in x:
                self.story_dict[globals()[x].name] = [globals()[x], 0, globals()[x].start_active, False]

    def has_path(self, path_name: str):
        return (path_name in self.story_dict)

    # To allow for partial string matches while looking for keywords, EG girlfriend, affair, lust, etc
    def has_path_with_partial_string(self, path_name: str):
        for x in self.story_dict:
            if path_name in x:
                return True
        return False
    #Note: How should we handle GETTING associated partial name match? Return a list with all possible entries? Could have multiple hits, the above method only finds the first

    # Getters for list information
    def get_path(self, path_name: str):
        if self.has_path(path_name):
            return self.story_dict[path_name][0]
        return None

    def path_step(self, path_name: str):
        if self.has_path(path_name):
            return self.story_dict[path_name][1]
        return False

    def path_active(self, path_name: str):
        if self.has_path(path_name):
            return self.story_dict[path_name][2]
        return False

    def path_complete(self, path_name: str):
        if self.has_path(path_name):
            return self.story_dict[path_name][3]
        return False

    # Allow input of either string name, or an actual path itself.
    def add_path(self, path_name):
        if isinstance(path_name, str):
            if self.has_path(path_name):
                return False
            for x in globals():
                if isinstance(globals()[x], Story_Path):
                    if globals()[x].name == path_name:
                        self.story_dict[globals()[x].name] = [globals()[x], 0, globals()[x].start_active, False]
                        return True
        elif isinstance(path_name, Story_Path):
            if self.has_path(path_name.name):
                return False
            self.story_dict[path_name.name] = [path_name, 0, path_name.start_active, False]
            return True
        return False

    # Allow input of either string name, or an actual path itself.
    def remove_path(self, path_name):
        if isinstance(path_name, Story_Path):
            path_name = path_name.name
        if self.has_path(path_name):
            del self.story_dict[path_name]
            return True
        return False

    ### Path Manipulation Functions ###
    # probably wrapper these in Person

    def start_path(self, person: Person, path_name: str):
        if not self.has_path(path_name):
            return False
        self.story_dict[path_name][0].start_path(person)
        self.story_dict[path_name][1] = 0
        self.story_dict[path_name][2] = True

    def advance_path(self, person: Person, path_name: str):
        if not self.has_path(path_name):
            return False
        if self.story_dict[path_name][0].next_step(person, self.story_dict[path_name][1]): #Returns True if successful step
            self.story_dict[path_name][1] += 1
            self.story_dict[path_name][3] = False
        else:                                                                           #It can't step if the story is complete
            self.story_dict[path_name][3] = True
        return True

    def pause_path(self, person: Person, path_name: str):
        if not self.has_path(path_name):
            return False
        return self.story_dict[path_name][0].pause_path(person, self.story_dict[path_name][1])

    def resume_path(self, person: Person, path_name: str):
        if not self.has_path(path_name):
            return False
        return self.story_dict[path_name][0].resume_path(person, self.story_dict[path_name][1])

    ### Progress screen functions ###
    # Gets progression screen info for a single path
    def get_path_progress(self, person: Person, path_name: str):
        progress_dict = {}
        if not self.has_path(path_name):
            progress_dict[0] = "Error, no Path"
            return progress_dict
        progress_dict = self.story_dict[path_name][0].progress_description(person, self.story_dict[path_name][1])
        if self.story_dict[path_name][3]:
            progress_dict[int(len(progress_dict))] = "This Story Path is Complete"
        return progress_dict

    # Gets all applicable story path progress, returns in the form a list
    def get_path_progress_list(self, person: Person):
        progress_list = []
        for _, v in sorted(self.story_dict.items()):
            progress_list.append((v[0].name, self.get_path_progress(person, v[0].name)))
        return progress_list

    # We have two goals on game load.
    # First, we want to refresh all character associated storylines, WITHOUT overwriting existing storylines.
    # Works similar as init, except we only set the actual story path, not the full list of trackers.
    # Second, we want to check and see if a completed story has a new story step to activate.
    # Go through the list of completed story lines and check and see if there is a new step available
    def on_load(self, person: Person):
        dict_string_prefix = (person.func_name + "_story_path", )
        for x in globals():
            if dict_string_prefix in x:
                if globals()[x].name in self.story_dict:    #We already have the story, only overwrite the story_path
                    self.story_dict[globals()[x].name][0] = globals()[x]
                else:                                       #We DON'T already have it. Yay new content!
                    self.story_dict[globals()[x].name] = [globals()[x], 0, globals()[x].start_active, False]
        for y in self.story_dict:
            if y[3]:    #IT is marked as complete
                if y[1] - 1 < len(y[0].step_list):  #A new step, yay!
                    self.advance_path(person, y[0].name)
        return


#Similar to Story Tracker, but for any business focuesed story. For example, Head Researcher events that progress the entire business.
#Does not require a person to be passed in
class Business_Story_Tracker(Story_Tracker):
    def __init__(self, person: Person):
        # A dict with all the stories for the appropriate character.
        # dict key is the story_path.name
        # Each reference contains the path itself, the current step, whether the path is active or not, and whether the path is complete
        # [0] = the Path         (story_path)
        # [1] = Current Step     (int)
        # [2] = Path is Active   (bool)
        # [3] = Path is complete (bool)
        # [4] = Any Person currently associated with the path  (person)

        self.story_dict: dict[str, tuple[str, int, bool, bool, Person]] = {}
        dict_string_prefix = ("business_story_path", )     #We load the story paths automatically for people on init based on the path name
        for x in globals():
            if dict_string_prefix in x:
                self.story_dict[globals()[x].name] = [globals()[x], 0, globals()[x].start_active, False]
