from __future__ import annotations
from typing import Any, Callable
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.main_character.MainCharacter_ren import mc, list_of_people

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
class Goal():
    def __init__(self, goal_name: str, goal_description: str, event_name: str, listener_type: str,
            valid_goal_function: Callable[[Goal, int], bool], on_trigger_function: Callable[[Goal, Any], bool], arg_dict = None,
            difficulty_scale_function: Callable[[Goal, int], None] | None = None,
            report_function: Callable[[Goal], str] | None = None,
            progress_fraction_function: Callable[[Goal], float] | None = None,
            available = True, avail_req = None, enabled = True) -> None:
        self.name = goal_name #Short form name to be displayed to the player, generally on a progress bar of some sort.
        self._description = goal_description #A long form fluff description of the goal purpose.
        self.event_name = event_name #The event (aka a string to give to a listener manager) that this goal listens to.
        self.listener_type = listener_type #Either "MC" or "Business", decides which object the goal will grab as their listener manager when you ask it to enrol.
        self.valid_goal_function = valid_goal_function #A function called to check to see if the goal is a valid/reasonable one to give to the player. Also is used to make sure goals aren't completed when they are assigned.
        self.on_trigger_function = on_trigger_function #A function called by an event listener that this goal is hooked up to.
        if arg_dict: #A dict to hold arguments you want to be used by the on_trigger function without having to get specific about what they are here.
            self.arg_dict = arg_dict
        else:
            self.arg_dict = {}

        self.completed = False #A flag set to true when the goal is finished, so the player can complete the objective and claim their bonus point.

        self.difficulty_scale_function = difficulty_scale_function #A function called when the goal is activated (aka when it is copied from the default goal) to scale the parameters to the current difficulty.
        self.report_function = report_function
        self.progress_fraction_function = progress_fraction_function
        self.available = available      #If this goal should show up when customizing goals with Camilla
        self.avail_req = avail_req      #REquirement function to switch this goal to available
        self.enabled = enabled
        self.identifier = generate_identifier(goal_name)

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Goal) -> bool:
        if not isinstance(other, Goal):
            return NotImplemented
        return self.name == other.name

    def check_valid(self, difficulty: int):
        if callable(self.valid_goal_function):
            return self.valid_goal_function(self, difficulty)
        return True #If a goal does not have a valid goal function it is always valid.

    def check_available(self):
        if callable(self.avail_req):
            self.available = self.avail_req()
        self.available = True
        return

    def activate_goal(self, difficulty: int):
        if self.listener_type == "MC": #Figure out what listener we should be listening to
            listener = mc.listener_system
        else: #== "Business"
            listener = mc.business.listener_system

        if self.difficulty_scale_function:
            self.difficulty_scale_function(self, difficulty) #If we have a function for changing difficulty hand it ourselves and the difficulty we were activated at.

        listener.enrol_goal(self.event_name, self) #Enrol us to the proper listener and hand it us so it will call our trigger when we need it to.

    @property
    def progress_string(self): #Returns a string corresponding to the current progress of the goal. Generally something like "5 of 10" or "3/20".
        if self.completed:
            return "Completed"
        if self.report_function:
            return self.report_function(self)
        return "In Progress"

    @property
    def progress_fraction(self) -> float:
        if self.progress_fraction_function:
            return self.progress_fraction_function(self)
        return 0.0

    @property
    def description(self) -> str:
        if "people" not in self.arg_dict:
            return self._description

        names = [f"{x.name} {x.last_name}" for x in list_of_people if x.identifier in self.arg_dict["people"]]
        if not names:
            return self._description

        return f"{self._description}\n(Counted: {', '.join(names)})"

    @description.setter
    def description(self, value):
        self._description = value

    def call_trigger(self, **kwargs):
        return self.on_trigger_function(self, **kwargs)

    def complete_goal(self):
        self.completed = True

    def toggle_enabled(self):
        self.enabled = not self.enabled
