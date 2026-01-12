import renpy
import threading
import time
from game.bugfix_additions.debug_info_ren import write_log

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""

class floating_notification():
    def __init__(self, text: str, text_style: str = "float_text_grey", duration: int = 2):
        self.text = text
        self.text_style = text_style
        self.duration = duration
        self.start = time.time()

active_notifications: list[floating_notification] = []

def add_notification(text: str, text_style = "float_text_grey", duration = 2):
    active_notifications.append(floating_notification(text, text_style, duration))

def update_floating_notifications():
    while not hasattr(renpy.display.draw, "get_texture_size"):
        time.sleep(2)

    while True:
        try:
            for idx, notification in enumerate(active_notifications):
                if time.time() - notification.start > notification.duration:
                    active_notifications.remove(notification)

            time.sleep(.2)
        except Exception as e:
            write_log(f"Floating notification error: {repr(e)}")

notification_thread = threading.Thread(target=update_floating_notifications, name="texture_monitor")
notification_thread.daemon = True
notification_thread.start()

renpy.config.per_frame_screens.append("floating_notifications")
