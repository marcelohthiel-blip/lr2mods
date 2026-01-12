from __future__ import annotations
from typing import Literal
from game.major_game_classes.character_related.Appointment_ren import Appointment
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.bugfix_additions.debug_info_ren import add_to_debug_log
from game.helper_functions.convert_to_string_ren import day_names, time_names, day_and_time_string

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

#TODO List
#An interactable screen for selecting an appointment time
#Cheat functions for cheating thru days and time slots, so that a proper schedule is preserved

def generic_appt_requirement(time_slot: tuple[int, int]) -> bool:
    return day % 7 == time_slot[0] and time_of_day == time_slot[1]

class AppointmentScheduler():
    def __init__(self):
        #Initialize both dicts as empty
        #Repeat events are for optional events that recur every week. Useful for displaying on a calander
        self.repeat_events: dict[tuple[int, int], list[str]] = {
            (0, 0): [],
            (0, 1): [],
            (0, 2): [],
            (0, 3): [],
            (0, 4): [],
            (1, 0): [],
            (1, 1): [],
            (1, 2): [],
            (1, 3): [],
            (1, 4): [],
            (2, 0): [],
            (2, 1): [],
            (2, 2): [],
            (2, 3): [],
            (2, 4): [],
            (3, 0): [],
            (3, 1): [],
            (3, 2): [],
            (3, 3): [],
            (3, 4): [],
            (4, 0): [],
            (4, 1): [],
            (4, 2): [],
            (4, 3): [],
            (4, 4): [],
            (5, 0): [],
            (5, 1): [],
            (5, 2): [],
            (5, 3): [],
            (5, 4): [],
            (6, 0): [],
            (6, 1): [],
            (6, 2): [],
            (6, 3): [],
            (6, 4): []
        }

        #Appointment List tracks mandatory events for MC, and attempts to keep his schedule clear
        self.appointment_list: dict[tuple[int, int], Appointment] = {
            (0, 0): None,
            (0, 1): None,
            (0, 2): None,
            (0, 3): None,
            (0, 4): None,
            (1, 0): None,
            (1, 1): None,
            (1, 2): None,
            (1, 3): None,
            (1, 4): None,
            (2, 0): None,
            (2, 1): None,
            (2, 2): None,
            (2, 3): None,
            (2, 4): None,
            (3, 0): None,
            (3, 1): None,
            (3, 2): None,
            (3, 3): None,
            (3, 4): None,
            (4, 0): None,
            (4, 1): None,
            (4, 2): None,
            (4, 3): None,
            (4, 4): None,
            (5, 0): None,
            (5, 1): None,
            (5, 2): None,
            (5, 3): None,
            (5, 4): None,
            (6, 0): None,
            (6, 1): None,
            (6, 2): None,
            (6, 3): None,
            (6, 4): None
        }

        #Use this for appointments that we were not able to schedule.
        #Check this list at the start of each day to see if we can make appointments for them
        #If not, leave it on the schedule list
        self.appointment_schedule_list: list[Appointment] = []

    def create_appointment(self, label: str, description: str, day_restriction: tuple[int] | int = (0, 1, 2, 3, 4, 5, 6), time_restriction: tuple[int] | int = (0, 1, 2, 3, 4), time_slot: tuple[int, int] | None = None, person: Person = None, appointment_type: Literal["Event", "Date"] = "Event") -> Appointment:
        '''
        Creates a new appointment.
        When a time_slot is passed, and it's not available, nothing will be scheduled.
        When passing restrictions and current week has no slot available, it will be scheduled to be added next week.
        '''
        if time_slot is None:
            time_slot = self.get_next_open_time_slot(day_restriction, time_restriction)

        if time_slot is not None and not self.get_appointment(time_slot = time_slot) is None:
            print(f"Already Booked: Unable to create appointment {description} at {time_slot}.")

        appointment = Appointment(label, description, day_restriction, time_restriction, time_slot, appointment_type, person)
        if appointment.is_scheduled:
            self.create_mandatory_event(appointment)
        else:
            self.schedule_event(appointment)
        return appointment

    #Returns None if time slot is open, otherwise returns event description
    def get_appointment(self, day_slot = None, time_of_day_slot = None, time_slot: tuple[int, int] = None) -> Appointment | None:
        if day_slot is None:
            day_slot = day % 7
        if time_of_day_slot is None:
            time_of_day_slot = time_of_day

        if time_slot is None:
            time_slot = (day_slot, time_of_day_slot)
        return self.appointment_list.get(time_slot, None)

    #For mandatory events#
    #At most use only for events that require a time slot and a person, no further requirements
    #Most useful if we already know an open time slot. Returns False if the time slot is not open.
    def create_mandatory_event(self, appointment: Appointment):
        if not appointment.is_scheduled:
            return False

        action = Action(appointment.description,
                generic_appt_requirement,
                appointment.label,
                args = appointment.person,
                requirement_args = appointment.time_slot,
                menu_tooltip= None,
                priority = -20, # low priority so it is scheduled after other mandatory events
                is_fast = False)

        if appointment.time_slot[1] == 0:
            mc.business.add_mandatory_morning_crisis(action)
        else:
            mc.business.add_mandatory_crisis(action)
        self.appointment_list[appointment.time_slot] = appointment
        return True

    def new_repeat_event(self, event_desc: str, day_slot: int, time_of_day_slot: int):
        '''
        Schedules an optional event for a specific day and time (make visible in scheduler).
        '''
        time_slot = (day_slot % 7, time_of_day_slot)
        if event_desc not in self.repeat_events[time_slot]:
            self.repeat_events[time_slot].append(event_desc)

    # Use this when we can't reserve a time slot properly
    # Adds the event to the scheduler that runs daily, to try and schedule the new event when possible.
    def schedule_event(self, appointment: Appointment):
        self.appointment_schedule_list.append(appointment)

    # Attempt to make a new appointment for a scheduled event. Returns True if scheduled, False if unable.
    def attempt_to_schedule_event(self, scheduled_appointment: Appointment) -> bool:
        time_slot = self.get_next_open_time_slot(scheduled_appointment.day_restriction, scheduled_appointment.time_restriction)
        if time_slot is None:
            return False

        scheduled_appointment.time_slot = time_slot
        self.create_mandatory_event(scheduled_appointment)
        return True

    def get_all_open_time_slots(self) -> list[tuple[int, int]]:
        '''
        Returns all time slots without any scheduled events in upcoming chronological order.
        This starts from the current day and time + 1 giving a slots for a full week.
        :return: A list of tuples (day, time)
        '''
        open_list = []
        start_day = day % 7
        # Make a list of all open slots
        for day_slot in range(7):  # [0,1,2,3,4,5,6]
            current_day_slot = (start_day + day_slot) % 7
            for time_slot in range(5): #[0,1,2,3,4]
                if day_slot == start_day and time_slot < time_of_day:
                    continue
                if not self.get_appointment(time_slot = (current_day_slot, time_slot)):
                    open_list.append((current_day_slot, time_slot))
        return open_list

    def get_open_time_slots(self, day_restriction = (0, 1, 2, 3, 4, 5, 6), time_restriction = (0, 1, 2, 3, 4)) -> list[tuple[int, int]]:
        '''
        Returns a list of free time slots. Can give a day and/or a time restriction.
        :param day_restriction : tuple[int] | int: Tuple of int indicating day(s) of the week to consider (0-6)
        :param time_restriction : tuple[int] | int: Tuple of int indicating time(s) of the day to consider (0-4)
        :return: List of free time slots in form tuple(day, time), can be an empty array
        '''
        if isinstance(day_restriction, int):
            day_restriction = (day_restriction, )
        if isinstance(time_restriction, int):
            time_restriction = (time_restriction, )

        return [slot for slot in self.get_all_open_time_slots() if slot[0] in day_restriction and slot[1] in time_restriction]

    def get_next_open_time_slot(self, day_restriction: tuple[int] | int = (0, 1, 2, 3, 4), time_restriction: tuple[int] | int = (1, 2, 3)) -> tuple[int, int] | None:
        '''
        Returns the next available time slot. If day or time restricted, only those time slots are considered.
        :param day_restriction: A tuple or int indicating which days of the week to search
        :param time_restriction: A tuple or int indicating which time slots to search
        :return: Tuple of (day_slot, time_slot) or None if no slots are available
        '''
        if isinstance(day_restriction, int):
            day_restriction = (day_restriction, )
        if isinstance(time_restriction, int):
            time_restriction = (time_restriction, )
        start_day = day % 7
        for day_slot in range(7):
            current_day_slot = (start_day + day_slot) % 7
            for time_slot in range(5):
                if day_slot == start_day and time_slot <= time_of_day:
                    continue
                if time_slot in time_restriction and current_day_slot in day_restriction and not self.get_appointment(time_slot = (current_day_slot, time_slot)):
                    return (current_day_slot, time_slot)
        return None

    #Clears out today's schedule
    def run_day(self):
        for time_slot in range(5): #[0,1,2,3,4]
            self.appointment_list[(day % 7, time_slot)] = None

    def run_morning(self):
        removed_appt_list = []
        for scheduled_appt in self.appointment_schedule_list:
            if self.attempt_to_schedule_event(scheduled_appt):
                removed_appt_list.append(scheduled_appt)
        for x in removed_appt_list:
            self.appointment_schedule_list.remove(x)

#Cancellation functions

    # Pass in a person.
    # Hopefully this clears the schedule, AND removes the appropriate mandatory event
    def cancel_date_with_person(self, person):
        date = next((x for x in self.appointment_list.values() if x.person == person and x.is_date), None)
        if date:
            mc.business.remove_mandatory_crisis(date.label)

    # Cancel an event by either name, or time slot
    # Does NOT remove it from the mandatory crisis list!
    def cancel_event(self, event_desc = None, time_slot: tuple[int, int] = None):
        if event_desc:
            event = next((x for x in self.appointment_list.values() if x.description == event_desc), None)
        elif time_slot:
            event = next((x for x in self.appointment_list.values() if x.time_slot == time_slot), None)

        if event:
            mc.business.remove_mandatory_crisis(event.label)
            self.appointment_list[time_slot] = None

    def debug_print_appointments(self):
        for day_slot in range(7): #[0,1,2,3,4,5,6]:    #For some reason debug screen cuts out Wednesday? Unsure why
            for time_slot in range(5): #[0,1,2,3,4]:
                appointment = self.get_appointment(time_slot = (day_slot, time_slot))
                if appointment is None:
                    add_to_debug_log(f"No events on {day_names[day_slot]} {time_names[time_slot]}.")
                else:
                    add_to_debug_log(f"{appointment}")

    @property
    def has_event_now(self) -> bool:
        appointment = self.get_appointment(day_slot = day % 7, time_of_day_slot = time_of_day)
        return appointment is not None and appointment.is_event

    #Returns true if MC has a date in the current time slot.
    @property
    def has_date_now(self) -> bool:
        appointment = self.get_appointment(day_slot = day % 7, time_of_day_slot = time_of_day)
        return appointment is not None and appointment.is_date

    @property
    def has_scheduled_appointment(self) -> bool:
        return self.get_appointment(time_slot = (day % 7, time_of_day)) is not None

    @property
    def current_appointment_description(self) -> str:
        appointment = self.get_appointment(time_slot = (day % 7, time_of_day))
        return "" if appointment is None else appointment.description

    def has_date_with_person(self, person: Person) -> bool:
        return any(x for x in self.appointment_list.values() if x and x.person == person and x.is_date)

    #Checks to see if the next early morning slot is free.
    #Useful if we want to check if there is a mandatory event the next morning.
    #Check this when we see if we can stay the night somewhere.
    #If not, then MC should refuse, or block off the event from happening.
    @property
    def is_tomorrow_early_open(self) -> bool:
        return self.get_appointment(day_slot = (day + 1) % 7, time_of_day_slot = 0) is None

    #Pass in a list of time slots to build a new list of menu items.
    #If no list is passed it, it grabs ALL available time slots
    def build_appt_menu_items(self, slot_list = None) -> list:
        if slot_list is None:
            slot_list = self.get_all_open_time_slots()
        option_list = []
        option_list.append("Choose a Time")
        for time_slot in slot_list:
            slot_text = day_and_time_string(time_slot[0], time_slot[1])
            option_list.append([slot_text, time_slot])
        option_list.append(["Nevermind", False])
        return option_list

    #Use to grab a list of all the appointments in a day, formatted for use in
    def get_formatted_day_appt_schedule(self, day_index = 0) -> list:
        day_schedule = []
        if day_index >= 7:
            day_index = day_index % 7
        day_schedule.append(day_names[day_index])
        for time_slot in range(5): #[0,1,2,3,4]:
            if self.get_appointment(time_slot = (day_index, time_slot)) is None:
                if self.repeat_events.get((day_index, time_slot), None) is None:
                    day_schedule.append("----------")
                else:
                    day_schedule.append("")
                    for event_desc in self.repeat_events.get((day_index, time_slot), None):
                        day_schedule[time_slot + 1] += "{i}" + event_desc + "{/i}\n"
            else:
                day_schedule.append("{b}" + self.get_appointment(time_slot = (day_index, time_slot)).description + "{/b}")
        return day_schedule

    #Used for the new schedule button on the top left GUI
    def get_hud_text(self) -> str:
        day_index = day % 7
        hud_text = "No Events"
        appointment = self.get_appointment(day_slot = day_index, time_of_day_slot = time_of_day)
        if appointment is None:
            if self.repeat_events.get((day_index, time_of_day), None):
                if len(self.repeat_events.get((day_index, time_of_day), None)) == 1:
                    hud_text = self.repeat_events.get((day_index, time_of_day), None)[0]
                else:
                    hud_text = str(len(self.repeat_events.get((day_index, time_of_day), None))) + " Optional Events"
        else:
            hud_text = appointment.description
        return hud_text

    #Tooltip for the GUI
    def get_hud_tooltip(self) -> str:
        day_index = day % 7
        if self.get_hud_text() == "No Events":
            return "No events scheduled right now.\nClick to view your full calender for the next week."

        if self.get_appointment(time_slot = (day_index, time_of_day)):
            return "You have a mandatory event next.\nClick to view your full calender for the next week."
        if len(self.repeat_events.get((day_index, time_of_day), [])) == 1:
            return "You have an optional event next.\nClick to view your full calender for the next week."

        hud_tooltip_text = ""
        for event_desc in self.repeat_events.get((day_index, time_of_day), []):
            hud_tooltip_text += (event_desc + "\n")
        hud_tooltip_text += "Click to view your full calender for the next week."
        return hud_tooltip_text
