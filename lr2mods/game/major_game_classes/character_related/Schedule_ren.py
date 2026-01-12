from __future__ import annotations
import copy
from game.helper_functions.convert_to_string_ren import day_names
from game.major_game_classes.game_logic.Room_ren import Room, list_of_places

list_of_places: list[Room]
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class DailySchedule():
    def __init__(self, early_morning_location: Room | None = None,
                 morning_location: Room | None = None,
                 afternoon_location: Room | None = None,
                 evening_location: Room | None = None,
                 night_location: Room | None = None):

        self.day_plan: dict[int, int | None] = {
            0: (early_morning_location.identifier if early_morning_location else None),
            1: (morning_location.identifier if morning_location else None),
            2: (afternoon_location.identifier if afternoon_location else None),
            3: (evening_location.identifier if evening_location else None),
            4: (night_location.identifier if night_location else None),
        }

    def __call__(self, time_slot: int | None = None) -> Room | None:
        if not time_slot:
            time_slot = time_of_day
        return self.get_destination(time_slot)

    def __str__(self) -> str:
        result = []
        for x in range(5):
            location = self.get_destination(x)
            result.append(f"{x}: {(location.formal_name if location else 'free')}")
        return " - ".join(result)

    def update_scheduled_location(self, location: Room):
        '''
        Switch all scheduled locations to a new location
        '''
        for time_slot in range(5):
            if self.day_plan[time_slot]:
                self.day_plan[time_slot] = location.identifier

    def get_destination(self, time_slot: int | None = None) -> Room | None:
        '''
        Destination for current or passed timeslot of day
        '''
        if time_slot is None:
            time_slot = time_of_day
        return next((x for x in list_of_places if x.identifier == self.day_plan[time_slot]), None)

    def get_copy(self) -> "DailySchedule": #Returns a new DailySchedule
        return copy.deepcopy(self)

    def set_schedule(self, location: Room | None, time_slots: list[int] | int):
        if isinstance(time_slots, list):
            for a_time in time_slots: #If it's a list distribute out a bunch of single time calls.
                self.set_schedule(location, a_time)
            return

        if location:
            self.day_plan[time_slots] = location.identifier
        else:
            self.day_plan[time_slots] = None

    @property
    def scheduled_time_slots(self) -> int:
        return sum(1 for x in self.day_plan.values() if x is not None)

    def has_time_schedule(self, time_slot: int | None = None):
        if time_slot is None:
            time_slot = time_of_day
        return self.day_plan[time_slot] is not None

    def has_location(self, location: Room) -> bool:
        return any(x for x in self.day_plan.values() if x == location.identifier)

class Schedule():
    @staticmethod
    def next_monday() -> int:
        return day + (7 - (day % 7))

    def __init__(self,
            monday_schedule: DailySchedule | None = None,
            tuesday_schedule: DailySchedule | None = None,
            wednesday_schedule: DailySchedule | None = None,
            thursday_schedule: DailySchedule | None = None,
            friday_schedule: DailySchedule | None = None,
            saturday_schedule: DailySchedule | None = None,
            sunday_schedule: DailySchedule | None = None,
            start_day: int = -1):

        self.start_day = start_day
        self.schedule: dict[int, DailySchedule | None] = {
            0: (monday_schedule if monday_schedule else DailySchedule()),
            1: (tuesday_schedule if tuesday_schedule else DailySchedule()),
            2: (wednesday_schedule if wednesday_schedule else DailySchedule()),
            3: (thursday_schedule if thursday_schedule else DailySchedule()),
            4: (friday_schedule if friday_schedule else DailySchedule()),
            5: (saturday_schedule if saturday_schedule else DailySchedule()),
            6: (sunday_schedule if sunday_schedule else DailySchedule()),
        }

    def __call__(self, day_slot: int | None = None, time_slot: int | None = None) -> Room | None:
        return self.get_destination(day_slot, time_slot)

    def __str__(self) -> str:
        result = []
        for day_slot in range(7):
            result.append(f"{day_names[day_slot]} -> {self.schedule[day_slot]!s}")
        return "\n".join(result)

    def update_scheduled_location(self, location: Room):
        '''
        Switch all scheduled locations to a new location
        '''
        for day_slot in range(7):
            self.schedule[day_slot].update_scheduled_location(location)

    def get_destination(self, day_slot: int | None = None, time_slot: int | None = None) -> Room | None:
        '''
        Destination for current day / time or passed day / time
        '''
        if day < self.start_day:
            return None
        if day_slot is None:
            day_slot = day % 7
        else:
            day_slot = day_slot % 7

        if time_slot is None:
            time_slot = time_of_day

        return self.schedule[day_slot].get_destination(time_slot)

    def get_next_destination(self) -> Room | None:
        '''
        Destination for next time_slot (can be early morning next day)
        Currently not used by any code but left in place for future usage
        '''
        check_time = time_of_day + 1
        check_day = day
        if check_time > 4:
            check_day = day + 1
            check_time = 0

        if check_day < self.start_day:
            return None

        return self.get_destination(check_day, check_time)

    def get_copy(self) -> "Schedule": #Returns a proper copy of the schedule that has unique DailySchedule references (but referenced Locations)
        return copy.deepcopy(self)

    def set_schedule(self, location: Room | None, day_slots: list[int] | int | None = None, time_slots: list[int] | None = None):
        '''
        Sets the scheduled location
        When day_slots is None, all days of the week are scheduled
        When time_slots is None, all timeslots of the day are scheduled
        '''
        if day_slots is None:
            day_slots = [0, 1, 2, 3, 4, 5, 6]
        if time_slots is None:
            time_slots = [0, 1, 2, 3, 4]
        if isinstance(day_slots, list):
            for a_day in day_slots:
                self.set_schedule(location, a_day, time_slots)
            return
        self.schedule[day_slots].set_schedule(location, time_slots)

    def remove_location(self, location: Room):
        for day_number in range(0, 7):
            for time_number in range(0, 5):
                if self.get_destination(day_slot = day_number, time_slot = time_number) == location:
                    self.set_schedule(None, day_slots = [day_number], time_slots = [time_number])

    def scheduled_time_slots(self, day_slot: int | None = None) -> int:
        '''
        Number of scheduled timeslots for current or specified day
        '''
        if day < self.start_day:
            return 0
        if day_slot is None:
            day_slot = day % 7
        return self.schedule[day_slot].scheduled_time_slots

    def has_time_schedule(self, day_slot: int | None = None, time_slot: int | None = None) -> bool:
        '''
        Has a scheduled location for the current day / time or passed day / time
        '''
        if day < self.start_day:
            return False
        if day_slot is None:
            day_slot = day % 7
        if time_slot is None:
            time_slot = time_of_day
        return self.schedule[day_slot].has_time_schedule(time_slot)

    def has_location(self, location: Room) -> bool:
        return any(x for x in self.schedule.values() if x.has_location(location))
