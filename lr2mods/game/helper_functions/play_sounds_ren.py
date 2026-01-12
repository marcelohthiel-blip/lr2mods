from __future__ import annotations
import renpy
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""
import re

SOUND_FOLDER = "sounds"

def generate_sound_list(sound_name):
    return [x for x in renpy.list_files() if re.match(rf"{SOUND_FOLDER}\/.*({sound_name}).*", x, re.IGNORECASE)]

# We keep the list generation so the game doesn't crash if it checks for these lists elsewhere
moan_sounds = generate_sound_list("Moan")
orgasm_sounds = generate_sound_list("Orgasm")
slap_sounds = generate_sound_list("Slap")
breathing_sounds = generate_sound_list("Breathing")
gag_sounds = generate_sound_list("Gag")
swallow_sounds = generate_sound_list("Swallow")
mouthful_sounds = generate_sound_list("Mouthful")
blowjob_sounds = generate_sound_list("Blowjob")
notification_sounds = generate_sound_list("Notification")
message_sounds = generate_sound_list("Message")
ring_sounds = generate_sound_list("Ring")

# --- DISABLED SOUNDS (NSFW) ---
# Added 'pass' to allow the game to continue without playing audio

def play_moan_sound():
    pass
    # play_sound(moan_sounds)

def play_female_orgasm():
    pass
    # play_sound(orgasm_sounds)

def play_spank_sound():
    pass
    # play_sound(slap_sounds)

def play_breathing_sound():
    pass
    # play_sound(breathing_sounds)

def play_gag_sound():
    pass
    # play_sound(gag_sounds)

def play_swallow_sound():
    pass
    # play_sound(swallow_sounds)

def play_blowjob_sound():
    pass
    # play_sound(blowjob_sounds)

def play_mouthful_sound():
    pass
    # play_sound(mouthful_sounds)


# --- ACTIVE SOUNDS (UI/System) ---
# These remain active for gameplay notifications

def play_notification_sound():
    play_sound(notification_sounds)

def play_message_sound():
    play_sound(message_sounds, "effects")

def play_ring_sound():
    play_sound(ring_sounds, "effects")


# --- MAIN PLAY FUNCTION ---

def play_sound(sounds_list, channel = "sex"):
    if sounds_list:
        renpy.play(renpy.random.choice(sounds_list), channel)