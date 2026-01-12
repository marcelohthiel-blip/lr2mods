## Hijack Original Label by Tristimdorion
# If you want run your MOD label before an in game label you just need to call
# the add_label_hijack method, since we store all hijacked labels, you can attach
# your code to any base game code, without changing the original game code.

# Make sure you append following lines, so you don't break the hijack functionality
#         # continue on the hijack stack if needed
#         execute_hijack_call(stack)
from __future__ import annotations
import builtins
import renpy
from renpy import config

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

hijack_list = {}

# Hijack the config label callback function
def hijack_label_callback(original_label, abnormal: bool):
    # create call stack of hijacked labels (allows for multiple hijacks of same label)
    if original_label in hijack_list:
        call_stack = []
        for hijack in hijack_list[original_label]:
            if not renpy.has_label(hijack):
                renpy.say(None, f"Unknown label {hijack}")
            else:
                call_stack.append(hijack)

        # print("Original label: {0} -> stack size {1}".format(original_label, len(call_stack)))

        # call first label on the stack
        execute_hijack_call(call_stack)

config.label_callbacks.append(hijack_label_callback)

def execute_hijack_call(stack):
    if builtins.len(stack) == 0:
        return

    # remove first label from stack
    target_label = stack.pop(0)
    # call the label
    renpy.call(target_label, stack)

def add_label_hijack(original_label_name, hijack_label_name):
    if original_label_name in hijack_list:
        hijack_list[original_label_name].append(hijack_label_name)
    else:
        hijack_list[original_label_name] = [hijack_label_name]

def remove_label_hijack(hijack_label_name):
    for original, hijacks in hijack_list:
        if hijack_label_name in hijacks:
            hijack_list[original].remove(hijack_label_name)


#label advance_time_extra:
#    "Testing hijack"
#    return

#init 200:
#    $ add_label_hijack("advance_time", "advance_time_extra")
