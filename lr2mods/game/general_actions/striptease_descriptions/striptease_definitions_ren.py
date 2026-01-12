from __future__ import annotations
from game.major_game_classes.game_logic.StripteasePosition_ren import StripteasePosition

list_of_strip_positions: list[StripteasePosition] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

strip_awkward_stand = StripteasePosition(name = "Awkward_stand",
    girl_energy_cost = 4, guy_arousal_gain = 4,
    intro_label = "strip_awkward_stand_intro",
    transition_label = "strip_awkward_transition",
    turn_towards_label = "strip_awkward_stand_turn_towards",
    turn_away_label = "strip_awkward_stand_turn_away",
    towards_labels = ["strip_awkward_stand_towards_1", "strip_awkward_stand_towards_2"],
    away_labels = ["strip_awkward_stand_away_1"],
    climax_label = "strip_awkward_stand_climax")
list_of_strip_positions.append(strip_awkward_stand)


close_strip_dancing = StripteasePosition(name = "Close Strip Dancing",
    slut_requirement = 20,
    is_close = True,
    allows_touching = True, allows_jerking = True, allows_turning = True,
    position_towards_pose = "stand4", position_away_pose = "walking_away",
    girl_energy_cost = 6, guy_arousal_gain = 8,
    intro_label = "strip_close_dancing_intro",
    transition_label = "strip_close_dancing_transition",
    turn_towards_label = "strip_close_dancing_turn_towards",
    turn_away_label = "strip_close_dancing_turn_away",
    towards_labels = ["strip_close_dancing_towards_1", "strip_close_dancing_towards_2"],
    away_labels = ["strip_close_dancing_away_1"],
    climax_label = "strip_close_dancing_climax")
list_of_strip_positions.append(close_strip_dancing)


strip_dancing = StripteasePosition(name = "Strip_Dancing",
    slut_requirement = 10,
    position_towards_pose = "stand3", position_away_pose = "back_peek",
    girl_energy_cost = 6, guy_arousal_gain = 7,
    intro_label = "strip_dancing_intro",
    transition_label = "strip_dancing_transition",
    turn_towards_label = "strip_awkward_stand_turn_towards",
    turn_away_label = "strip_dancing_turn_away",
    towards_labels = ["strip_dancing_towards_1", "strip_dancing_towards_2"],
    away_labels = ["strip_dancing_away_1"],
    climax_label = "strip_dancing_climax")
list_of_strip_positions.append(strip_dancing)


strip_lap_dance = StripteasePosition(name = "Lap Dancing",
    slut_requirement = 30,
    is_close = True,
    allows_touching = True, allows_jerking = False, allows_turning = True,
    position_towards_pose = "cowgirl", position_away_pose = "sitting",
    girl_energy_cost = 6, guy_arousal_gain = 6,
    girl_arousal_gain = 2,
    intro_label = "strip_lap_dance_intro",
    transition_label = "strip_lap_dance_transition",
    turn_towards_label = "strip_lap_dance_turn_towards",
    turn_away_label = "strip_lap_dance_turn_away",
    towards_labels = ["strip_lap_dance_towards_1", "strip_lap_dance_towards_2"],
    away_labels = ["strip_lap_dance_away_1"],
    climax_label = "strip_lap_dance_climax")
list_of_strip_positions.append(strip_lap_dance)


close_strip_dancing.leads_to.append((strip_lap_dance, "Pull her on your lap"))
strip_awkward_stand.leads_to.append((strip_dancing, "Tell her to dance"))
strip_dancing.leads_to.append((close_strip_dancing, "Call her closer"))
