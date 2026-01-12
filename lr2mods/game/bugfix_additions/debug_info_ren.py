from __future__ import annotations
import renpy
import builtins
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.major_game_classes.clothing_related.zip_manager_ren import zip_manager
from game.major_game_classes.clothing_related.outfit_selector_ren import outfit_queue
from game.major_game_classes.character_related.Person_ren import character_cache, portrait_cache

list_of_people = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
import collections
import threading
import time
import functools
import sys
from pylru import LRUCache # type: ignore


debug_log_enabled = False

class SystemInfo():
    def __init__(self):
        self.total_zip_size = 0
        self.total_zip_items = 0
        self.zip_utilization = 0
        self.texture_size = 0
        self.texture_count = 0
        self.cache_size = 0
        self.outfit_queue_size = 0

    def update(self):
        try:
            if "zip_manager" in globals():
                global zip_manager
                self.total_zip_size = zip_manager.byte_size
                self.total_zip_items = zip_manager.size
                self.zip_utilization = zip_manager.utilization()
                self.outfit_queue_size = outfit_queue.qsize()
            if "renpy" in globals():
                self.texture_size, self.texture_count = renpy.exports.get_texture_size()
                self.cache_size = renpy.display.im.cache.get_total_size()
        except Exception as e:
            write_log(e)
            pass

system_info = SystemInfo()

render_lock = threading.RLock()

# make sure we only call this on the main thread
def validate_texture_memory():
    # keep texture memory at configured image_cache_size_in_mb; game slows down when this gets too high
    # check for 90% of available memory cache slows down dramatically when under pressure
    if renpy.display.draw.get_texture_size()[0] > (renpy.display.im.cache.cache_limit * 4 * 1.1):
        clean_memory()

def clean_memory():
    global character_cache
    character_cache.clear()
    global portait_cache
    portrait_cache.clear()
    renpy.free_memory()

def update_texture_info():
    global debug_log_enabled
    while not hasattr(renpy.display.draw, "get_texture_size"):
        time.sleep(2)

    while True:
        try:
            if debug_log_enabled:
                system_info.update()
            time.sleep(.5)
        except Exception as e:
            write_log(e)
            break   # exit thread

debug_log = LRUCache(8)

# Background thread for updating debug info log information
texture_info_thread = threading.Thread(target=update_texture_info, name="texture_monitor")
texture_info_thread.daemon = True
texture_info_thread.start()

renpy.config.per_frame_screens.append("DebugInfo")

def show_debug_log():
    global debug_log_enabled
    debug_log_enabled = True
    renpy.show_screen("DebugInfo")

def hide_debug_log():
    global debug_log_enabled
    debug_log_enabled = False
    renpy.hide_screen("DebugInfo")

# write to log.txt in root folder
def write_log(s, *args):
    print(s, *args)

# add info to in-game debug window
def add_to_debug_log(message, start_time = time.time()):
    global debug_log_enabled
    if debug_log_enabled:
        debug_log[f"T{time.time()}"] = message.format(total_time = time.time() - start_time)
    write_log(message.format(total_time = time.time() - start_time))

def get_debug_log():
    return "\n".join(x[1] for x in sorted(debug_log.items(), key = lambda t: t[0], reverse = True))

def get_persons_size():
    return sum(bytesizeof(x) for x in list_of_people)

def bytesizeof(obj, seen=None):
    size = sys.getsizeof(obj)
    if not seen:
        seen = set()
    if id(obj) in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(id(obj))
    try:
        if isinstance(obj, collections.abc.Mapping):
            size += sum(bytesizeof(v, seen) for v in obj.values())
            size += sum(bytesizeof(k, seen) for k in obj)
        elif hasattr(obj, '__dict__'):  # sum all object attributes
            size += sum(bytesizeof(getattr(obj, name), seen) for name in obj.__dict__)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
            size += sum(bytesizeof(i, seen) for i in obj)
        elif isinstance(obj, (str, bytes, bytearray)):
            size += builtins.len(obj)
        else: # check if passed object has a nested object property
            for attr in (x for x in dir(obj) if isinstance(x, (list, dict, tuple, object))):
                size += bytesizeof(getattr(obj, attr), seen)
    except Exception:
        pass
    return size

'''
@ttl_cache(ttl=seconds) simple function decorator to cache result for ttl
'''
def ttl_cache(ttl = 10):
    def wrap(func):
        cache = {}

        @functools.wraps(func)
        def wrapped(*args, **kw):
            now = time.time()
            key = (generate_identifier(args), generate_identifier(kw.values()))
            if key not in cache or now - cache[key][0] > ttl:
                value = func(*args, **kw)
                cache[key] = (now, value)
            return cache[key][1]
        return wrapped
    return wrap
