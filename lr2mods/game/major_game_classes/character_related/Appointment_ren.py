from typing import Literal
from game.major_game_classes.character_related.Person_ren import Person

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

class Appointment():
    def __init__(self, label: str, description: str, day_restriction: tuple[int] | int = (0, 1, 2, 3, 4, 5, 6), time_restriction: tuple[int] | int = (0, 1, 2, 3, 4), time_slot: tuple[int, int] = None, appointment_type: Literal["Date", "Event"] = "Event", person: Person = None):
        self.label = label
        self.description = description
        self.day_restriction = day_restriction
        self.time_restriction = time_restriction
        self.time_slot = time_slot
        self.appointment_type = appointment_type
        self.person = person

    @property
    def is_event(self) -> bool:
        return self.appointment_type == "Event"

    @property
    def is_date(self) -> bool:
        return self.appointment_type == "Date"

    @property
    def is_scheduled(self) -> bool:
        return self.time_slot is not None

    @property
    def in_restriction(self) -> bool:
        if self.is_scheduled:
            return self.day_restriction in self.time_slot[0] and self.time_restriction in self.time_slot[1]
        return False
