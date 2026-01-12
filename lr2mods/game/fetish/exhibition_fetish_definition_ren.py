from __future__ import annotations
from game.game_roles._role_definitions_ren import exhibition_fetish_role
from game.major_game_classes.character_related.Person_ren import Person

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def debug_set_stats_for_exhibition_fetish_mins(person: Person):
    person.arousal = 0
    person.energy = person.max_energy
    person.max_opinion_score("anal sex")
    person._sluttiness = 70
    person._obedience = 100
    person.happiness = 100
    person.love = 0

def abort_exhibition_fetish_intro(person: Person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
    person.event_triggers_dict["exhibition_fetish_start"] = False
    person.remove_role(exhibition_fetish_role)


# sb_free_strip_pose_list = [("Turn around","walking_away"), ("Turn around and look back", "back_peek"), ("Hands down, ass up","standing_doggy"), ("Be flirty","stand2"), ("Be casual","stand3"), ("Strike a pose", "stand4"), ("Move your hands out of the way", "stand5")]

# def sb_free_strip_build_strip_menu(person: Person, must_be_naked: bool):
#     option_list = []
#     option_list.append("Choose Strip Action")
#     for item in person.outfit.get_unanchored():
#         if not item.is_extension:
#             test_outfit = person.outfit.get_copy()
#             test_outfit.remove_clothing(item)

#             display_string = "Strip " + item.name
#             option_list.append((display_string, [item, 0]))

#     option_list.append(("Just watch", "Watch"))
#     option_list.append(("Tell her to pose", "Pose"))
#     if not must_be_naked or person.outfit.has_full_access:
#         option_list.append(("Finish the show", "Finish"))
#     return option_list

# def sb_free_strip_build_pose_menu(current_pose):
#     option_list = []
#     option_list.append("Choose Pose")
#     for pose in sb_free_strip_pose_list:
#         if not pose[1] == current_pose:
#             option_list.append(pose)
#     option_list.append(("Never mind", None))
#     return option_list


def add_exhibition_fetish(person: Person):
    person.add_role(exhibition_fetish_role)
    person.set_opinion("public sex", 2, True)
    person.set_event_day("LastExhibitionFetish")
