from __future__ import annotations
import renpy
from renpy import config
from renpy.character import HistoryEntry
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.helper_functions.list_functions_ren import all_people_in_the_game
from game.helper_functions.play_sounds_ren import play_message_sound
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""
def text_message_history_callback(history_entry):
    if "mc" not in globals():
        return
    if not mc.having_text_conversation or mc.text_conversation_paused:
        return
    if history_entry.who and history_entry.what:
        play_message_sound()
        mc.phone.__add_message(mc.having_text_conversation, history_entry)

config.history_current_dialogue = False
config.history_callbacks.append(text_message_history_callback) #Ensures conversations had via text are recorded properly

class TextMessageManager(): #Manages text conversations you've had with other girls. Also stores information for other phone related stuff
    def __init__(self):
        self.message_history: dict[int, list[HistoryEntry]] = {} # A dict that stores entries of Person:[HistoryEntry,HistoryEntry...] representing your recorded conversation with this girl.

    def register_number(self, person: Person): #Now just used to keep track of whose number we know
        if not self.has_number(person):
            self.message_history[person.identifier] = []
            self.add_system_message(person, f"Added {person.name} {person.last_name} to contacts.")

    def add_non_convo_message(self, person: Person, message: str, as_mc = False): #Allows you to add an entry to the log without it having to appear as dialogue.
        self.__add_message(person, self.__create_new_history_entry(mc.name if as_mc else person.fname, message))

    def add_system_message(self, person: Person, message: str): #Adds a history entry that does not have a "who" variable set. Use to add phone messages like "[SENT A PICTURE]".
        self.__add_message(person, self.__create_new_history_entry(None, message))

    def get_person_list(self, excluded_people = []):
        return sorted([x for x in all_people_in_the_game(excluded_people) if x.identifier in self.message_history], key = lambda x: x.name)

    def has_number(self, person: Person) -> bool:
        return person.identifier in self.message_history

    def get_message_list(self, person: Person):
        if self.has_number(person):
            return [(x.who, x.what) for x in self.message_history[person.identifier]]
        return []

    def __add_message(self, person: Person, history_entry: HistoryEntry):
        self.register_number(person)
        self.message_history[person.identifier].append(history_entry)
        # auto delete old messages
        self.message_history[person.identifier] = self.message_history[person.identifier][-15:]

    def __create_new_history_entry(self, who: str | None, what: str):
        entry = renpy.character.HistoryEntry()
        entry.kind = "adv"
        entry.who = who
        entry.what = what
        if renpy.game.context().rollback:
            entry.rollback_identifier = renpy.game.log.current.identifier
        return entry
