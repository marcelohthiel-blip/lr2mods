from __future__ import annotations
from game.major_game_classes.game_logic.Goal_ren import Goal

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

class ListenerManagementSystem(): #Used to manage listeners in objects. Contains functions for enrolling and removing triggers as well as firing notices to those triggers.
    def __init__(self):
        self.event_dict = {} #THis dictionary uses strings as keys (the trigger that is called) and each key holds a list of goals. When an event is triggered each listener enrolled to the key receives a notice (the on_trigger_function is called)

    def enrol_goal(self, trigger_name: str, the_goal: Goal):
        if trigger_name in self.event_dict:
            self.event_dict[trigger_name].append(the_goal) #Add the goal to the list.

        else: #The trigger_name is not in our dict, we need to add it then add the goal to it.
            self.event_dict[trigger_name] = [the_goal]

    def fire_event(self, trigger_name: str, **kwargs):
        if trigger_name not in self.event_dict:
            return

        completed_goals = []
        for goal in self.event_dict[trigger_name]:
            #on_trigger returns true if the goal is finished and we can stop letting it know.
            if goal.call_trigger(**kwargs):
                completed_goals.append(goal)

        #Remove all completed goals, they are no longer important.
        for goal in completed_goals:
            goal.complete_goal()
            self.event_dict[trigger_name].remove(goal)
