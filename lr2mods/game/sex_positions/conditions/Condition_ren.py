#This is the class for the condition
#Condition is used for non standard sex.
#Pretty much all params are optional. If they exist, they get called during sex at the appropriate times.
from __future__ import annotations
from typing import Any, Callable
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.game_logic.Position_ren import Position
from game.major_game_classes.game_logic.RoomObject_ren import RoomObject
import renpy
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""
class Condition_Type():
    @staticmethod
    def default_condition():
        return Condition_Type("Default")

    def __init__(self, name: str, pre_label: str = None, post_label: str = None,
            position_whitelist: list[Position] = None, position_blacklist: list[Position] = None,
            reward_cond: Callable[[Person, dict[str, Any]], bool] = None,
            reward_label: str = None, fail_label: str = None):
        self.name = name #A descriptive name of the contract.
        self.pre_label = pre_label  #Run this label before each sex round
        self.post_label = post_label    #Run this label after each sex round
        self.position_whitelist = position_whitelist    #Only positions on this list will be available
        self.position_blacklist = position_blacklist    #Positions on this list will NOT be available
        self.reward_cond = reward_cond          #Conditions to check for a reward
        self.reward_label = reward_label        #label to call for rewarded sequence.
        self.fail_label = fail_label
        self.condition_vars = []

    def call_pre_label(self, person: Person, position: Position, room_object: RoomObject, report_log: dict[str, Any]):
        if self.pre_label and renpy.has_label(self.pre_label):
            renpy.call(self.pre_label, person, position, room_object, report_log, self)

    def call_post_label(self, person: Person, position: Position, room_object: RoomObject, report_log: dict[str, Any]):
        if self.post_label and renpy.has_label(self.post_label):
            renpy.call(self.post_label, person, position, room_object, report_log, self)

    def filter_condition_positions(self, position: Position) -> bool:
        if self.position_whitelist:
            return position in self.position_whitelist
        if self.position_blacklist:
            return position not in self.position_blacklist
        return True

    def run_rewards(self, person: Person, report_log: dict[str, Any]):
        if callable(self.reward_cond):
            if self.reward_cond(self, person, report_log):
                renpy.call(self.reward_label, person, report_log, self)
            elif renpy.has_label(self.fail_label):
                renpy.call(self.fail_label, person, report_log, self)
