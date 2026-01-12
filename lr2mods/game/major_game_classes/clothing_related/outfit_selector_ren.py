from game.bugfix_additions.debug_info_ren import clean_memory, write_log
from game.major_game_classes.character_related.Person_ren import Person, list_of_people
import threading
"""renpy
init 5 python:
"""
import queue
import time

# Background thread for loading daily outfits while user is viewing EndOfDay overview

outfit_queue = queue.Queue()

def outfit_selector_queue():
    while True:
        try:
            person_id = outfit_queue.get()
            person = Person.get_person_by_identifier(person_id)
            if isinstance(person, Person):
                person.update_daily_outfit()
        except Exception as e:
            write_log(f"Outfit selector error: {person_id} -> {e}")

def fill_outfit_queue():
    time.sleep(.2)
    for x in list_of_people:
        outfit_queue.put_nowait(x.identifier)

def queue_outfit_changes():
    clean_memory()
    t = threading.Thread(target = fill_outfit_queue)
    t.daemon = True
    t.start()

# start background thread for pre-loading zip cache
outfit_thread = threading.Thread(target=outfit_selector_queue)
outfit_thread.daemon = True
outfit_thread.start()
