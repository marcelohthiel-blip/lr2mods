from __future__ import annotations
from game.major_game_classes.game_logic.Position_ren import Position, list_of_positions, list_of_girl_positions
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

against_wall = Position(name = "Against the Wall", slut_requirement = 60, slut_cap = 80, requires_hard = True, requires_large_tits = False,
    position_tag = "against_wall", requires_location = "Lean", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 20, girl_energy = 16,
    guy_arousal = 18, guy_energy = 16,
    connections = [],
    intro = "intro_against_wall",
    scenes = ["scene_against_wall_1", "scene_against_wall_2", "scene_against_wall_3", "scene_against_wall_4"],
    outro = "outro_against_wall",
    transition_default = "transition_default_against_wall",
    strip_description = "strip_against_wall", strip_ask_description = "strip_ask_against_wall",
    orgasm_description = "orgasm_against_wall",
    taboo_break_description = "taboo_break_against_wall",
    opinion_tags = ["sex standing up", "vaginal sex"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "against_wall_double_orgasm")

list_of_positions.append(against_wall)

anal_on_lap = Position(name = "Sit on Lap", slut_requirement = 75, slut_cap = 95, requires_hard = True, requires_large_tits = False,
    position_tag = "sitting", requires_location = "Sit", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 22, girl_energy = 20,
    guy_arousal = 16, guy_energy = 14,
    connections = [],
    intro = "intro_anal_on_lap",
    scenes = ["scene_anal_on_lap_1", "scene_anal_on_lap_2"],
    outro = "outro_anal_on_lap",
    transition_default = "transition_default_anal_on_lap",
    strip_description = "strip_anal_on_lap", strip_ask_description = "strip_ask_anal_on_lap",
    taboo_break_description = "taboo_break_anal_on_lap",
    orgasm_description = "orgasm_anal_on_lap",
    verb = "ass fuck",
    opinion_tags = ["anal sex", "taking control"], record_class = "Anal Sex",
    gic_tags = ["get mc off", "get off", "hate fuck", "anal creampie"],
    associated_taboo = "anal_sex",
    girl_outro = "GIC_outro_anal_on_lap")

list_of_positions.append(anal_on_lap)
list_of_girl_positions.append(anal_on_lap)

anal_standing = Position(name = "Standing Anal", slut_requirement = 70, slut_cap = 95, requires_hard = True, requires_large_tits = False,
    position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 20, girl_energy = 16,
    guy_arousal = 18, guy_energy = 16,
    connections = [],
    intro = "intro_anal_standing",
    scenes = ["scene_anal_standing_1", "scene_anal_standing_2"],
    outro = "outro_anal_standing",
    transition_default = "transition_default_anal_standing",
    strip_description = "strip_anal_standing", strip_ask_description = "strip_ask_anal_standing",
    taboo_break_description = "taboo_break_anal_standing",
    orgasm_description = "orgasm_anal_standing",
    verb = "ass fuck",
    opinion_tags = ["doggy style sex", "anal sex", "sex standing up"], record_class = "Anal Sex",
    associated_taboo = "anal_sex",
    double_orgasm = "anal_standing_double_orgasm")

list_of_positions.append(anal_standing)

anal_swing = Position(name = "Swinging Anal", slut_requirement = 80, slut_cap = 100, requires_hard = True, requires_large_tits = False,
    position_tag = "sitting", requires_location = "Swing", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 20, girl_energy = 12,
    guy_arousal = 22, guy_energy = 16,
    connections = [],
    intro = "intro_anal_swing",
    scenes = ["scene_anal_swing_1", "scene_anal_swing_2"],
    outro = "outro_anal_swing",
    transition_default = "transition_default_anal_swing",
    strip_description = "strip_anal_swing", strip_ask_description = "strip_ask_anal_swing",
    taboo_break_description = "taboo_break_anal_swing",
    orgasm_description = "orgasm_anal_swing",
    verb = "ass fuck",
    opinion_tags = ["doggy style sex", "anal sex"], record_class = "Anal Sex",
    associated_taboo = "anal_sex")

list_of_positions.append(anal_swing)

blowjob = Position(name = "Blowjob", slut_requirement = 40, slut_cap = 60, requires_hard = False, requires_large_tits = False,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
    girl_arousal = 3, girl_energy = 13,
    guy_arousal = 16, guy_energy = 5,
    connections = [],
    intro = "intro_blowjob",
    scenes = ["scene_blowjob_1", "scene_blowjob_2", "scene_blowjob_3"],
    outro = "outro_blowjob",
    transition_default = "transition_default_blowjob",
    strip_description = "strip_blowjob", strip_ask_description = "strip_ask_blowjob",
    orgasm_description = "orgasm_blowjob",
    taboo_break_description = "taboo_break_blowjob",
    verb = "mouth fuck",
    opinion_tags = ["giving blowjobs"], record_class = "Blowjobs",
    gic_tags = ["get mc off", "oral creampie", "facial", "body shot"],
    associated_taboo = "sucking_cock")

list_of_positions.append(blowjob)

cunnilingus = Position(name = "Cunnilingus", slut_requirement = 40, slut_cap = 60, requires_hard = False, requires_large_tits = False,
    position_tag = "missionary", requires_location = "Sit", requires_clothing = "Vagina", skill_tag = "Oral",
    girl_arousal = 15, girl_energy = 3,
    guy_arousal = 3, guy_energy = 15,
    connections = [],
    intro = "intro_cunnilingus",
    scenes = ["scene_cunnilingus_1", "scene_cunnilingus_2", "scene_SB_Oral_Laying_1", "scene_SB_Oral_Laying_2"],
    outro = "outro_cunnilingus",
    transition_default = "transition_default_cunnilingus",
    strip_description = "strip_cunnilingus", strip_ask_description = "strip_ask_cunnilingus",
    orgasm_description = "orgasm_cunnilingus",
    taboo_break_description = "taboo_break_cunnilingus",
    verb = "lick",
    opinion_tags = ["getting head"], record_class = "Cunnilingus",
    gic_tags = ["get off"],
    associated_taboo = "licking_pussy")

list_of_girl_positions.append(cunnilingus)
list_of_positions.append(cunnilingus)

deepthroat = Position(name = "Deepthroat", slut_requirement = 55, slut_cap = 80, requires_hard = True, requires_large_tits = False,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
    girl_arousal = 3, girl_energy = 20,
    guy_arousal = 23, guy_energy = 5,
    connections = [],
    intro = "intro_deepthroat",
    scenes = ["scene_deepthroat_1", "scene_deepthroat_2", "scene_deepthroat_3"],
    outro = "outro_deepthroat",
    transition_default = "transition_default_deepthroat",
    strip_description = "strip_deepthroat", strip_ask_description = "strip_ask_deepthroat",
    orgasm_description = "orgasm_deepthroat",
    taboo_break_description = "taboo_break_deepthroat",
    verb = "throat fuck",
    opinion_tags = ["giving blowjobs", "being submissive"], record_class = "Blowjobs",
    gic_tags = ["get mc off", "oral creampie"],
    associated_taboo = "sucking_cock",
    double_orgasm = "deepthroat_double_orgasm")

list_of_positions.append(deepthroat)

doggy_anal_dildo_dp = Position(name = "Doggy Anal DP", slut_requirement = 80, slut_cap = 100, requires_hard = True, requires_large_tits = False,
    position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 26, girl_energy = 14,
    guy_arousal = 22, guy_energy = 20,
    connections = [],
    intro = "intro_doggy_anal_dildo_dp",
    scenes = ["scene_doggy_anal_dildo_dp_1", "scene_doggy_anal_dildo_dp_2"],
    outro = "outro_doggy_anal_dildo_dp",
    transition_default = "transition_default_doggy_anal_dildo_dp",
    strip_description = "strip_doggy_anal_dildo_dp", strip_ask_description = "strip_ask_doggy_anal_dildo_dp",
    taboo_break_description = "taboo_break_doggy_anal_dildo_dp",
    orgasm_description = "orgasm_doggy_anal_dildo_dp",
    verb = "dp", verbing = "dp-ing",
    opinion_tags = ["doggy style sex", "anal sex", "vaginal sex"], record_class = "Anal Sex",
    associated_taboo = "anal_sex")

doggy_anal = Position(name = "Anal Doggy", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
    position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 16, girl_energy = 14,
    guy_arousal = 22, guy_energy = 20,
    connections = [],
    intro = "intro_doggy_anal",
    scenes = ["scene_doggy_anal_1", "scene_doggy_anal_2", "scene_SB_doggy_anal_1", "scene_SB_doggy_anal_2"],
    outro = "outro_doggy_anal",
    transition_default = "transition_default_doggy_anal",
    strip_description = "strip_doggy_anal", strip_ask_description = "strip_ask_doggy_anal",
    orgasm_description = "orgasm_doggy_anal",
    taboo_break_description = "taboo_break_doggy_anal",
    verb = "ass fuck",
    opinion_tags = ["doggy style sex", "anal sex"], record_class = "Anal Sex",
    associated_taboo = "anal_sex",
    double_orgasm = "doggy_anal_double_orgasm")

list_of_positions.append(doggy_anal)

doggy = Position(name = "Doggy", slut_requirement = 60, slut_cap = 80, requires_hard = True, requires_large_tits = False,
    position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 16, girl_energy = 14,
    guy_arousal = 22, guy_energy = 20,
    connections = [],
    intro = "intro_doggy",
    scenes = ["scene_doggy_1", "scene_doggy_2", "doggy_stealth_attempt"],
    outro = "outro_doggy",
    transition_default = "transition_default_doggy",
    strip_description = "strip_doggy", strip_ask_description = "strip_ask_doggy",
    orgasm_description = "orgasm_doggy",
    taboo_break_description = "taboo_break_doggy",
    opinion_tags = ["doggy style sex", "vaginal sex"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "doggy_double_orgasm")

list_of_positions.append(doggy)

facing_wall = Position(name = "Facing Wall", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
    position_tag = "back_peek", requires_location = "Lean", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 20, girl_energy = 16,
    guy_arousal = 18, guy_energy = 16,
    connections = [],
    intro = "intro_facing_wall",
    scenes = ["scene_facing_wall_1", "scene_facing_wall_2"],
    outro = "outro_facing_wall",
    transition_default = "transition_default_facing_wall",
    strip_description = "strip_facing_wall", strip_ask_description = "strip_ask_facing_wall",
    orgasm_description = "orgasm_facing_wall",
    taboo_break_description = "taboo_break_facing_wall",
    verb = "fuck",
    opinion_tags = ["sex standing up", "vaginal sex"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "facing_wall_double_orgasm")

kissing = Position(name = "Kissing", slut_requirement = 10, slut_cap = 40, requires_hard = False, requires_large_tits = False,
    position_tag = "kissing", requires_location = "Stand", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 5, girl_energy = 10,
    guy_arousal = 5, guy_energy = 10,
    connections = [],
    intro = "intro_kissing",
    scenes = ["scene_kissing_1", "scene_kissing_2"],
    outro = "outro_kissing",
    transition_default = "transition_default_kissing",
    strip_description = "strip_kissing", strip_ask_description = "strip_ask_kissing",
    orgasm_description = "orgasm_kissing",
    taboo_break_description = "taboo_break_kissing",
    verb = "kiss",
    opinion_tags = ["kissing"], record_class = "Kissing",
    associated_taboo = "kissing")

list_of_positions.append(kissing)

missionary = Position(name = "Missionary", slut_requirement = 50, slut_cap = 70, requires_hard = True, requires_large_tits = False,
    position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 16, girl_energy = 12,
    guy_arousal = 15, guy_energy = 14,
    connections = [],
    intro = "intro_missionary",
    scenes = ["scene_missionary_1", "scene_missionary_2", "scene_missionary_3"],
    outro = "outro_missionary",
    transition_default = "transition_default_missionary",
    strip_description = "strip_missionary", strip_ask_description = "strip_ask_missionary",
    orgasm_description = "orgasm_missionary",
    taboo_break_description = "taboo_break_missionary",
    opinion_tags = ["missionary style sex", "vaginal sex"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "missionary_double_orgasm")

list_of_positions.append(missionary)

piledriver_anal = Position(name = "Anal Piledriver", slut_requirement = 80, slut_cap = 95, requires_hard = True, requires_large_tits = False,
    position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 18, girl_energy = 12,
    guy_arousal = 24, guy_energy = 20,
    connections = [],
    intro = "intro_piledriver_anal",
    scenes = ["scene_piledriver_anal_1", "scene_piledriver_anal_2"],
    outro = "outro_piledriver_anal",
    transition_default = "transition_default_piledriver_anal",
    strip_description = "strip_piledriver_anal", strip_ask_description = "strip_ask_piledriver_anal",
    orgasm_description = "orgasm_piledriver_anal",
    taboo_break_description = "taboo_break_piledriver_anal",
    verb = "ass fuck",
    opinion_tags = ["missionary style sex", "anal sex", "being submissive"], record_class = "Anal Sex",
    associated_taboo = "anal_sex",
    double_orgasm = "piledriver_anal_double_orgasm")

list_of_positions.append(piledriver_anal)

piledriver_dp = Position(name = "Piledriver DP", slut_requirement = 90, slut_cap = 100, requires_hard = True, requires_large_tits = False,
    position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 18, girl_energy = 14,
    guy_arousal = 24, guy_energy = 22,
    connections = [],
    intro = "intro_piledriver_dp",
    scenes = ["scene_piledriver_dp_1", "scene_piledriver_dp_2"],
    outro ="outro_piledriver_dp",
    transition_default = "transition_default_piledriver_dp",
    strip_description = "strip_piledriver_dp", strip_ask_description = "strip_ask_piledriver_dp",
    orgasm_description = "orgasm_piledriver_dp",
    taboo_break_description = "taboo_break_piledriver_dp",
    verb = "piledrive", verbing = "piledriving",
    opinion_tags = ["missionary style sex", "vaginal sex", "being submissive", "anal sex"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex")

piledriver = Position(name = "Piledriver", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
    position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 14, girl_energy = 12,
    guy_arousal = 26, guy_energy = 20,
    connections = [],
    intro = "intro_piledriver",
    scenes = ["scene_piledriver_1", "scene_piledriver_2"],
    outro ="outro_piledriver",
    transition_default = "transition_default_piledriver",
    strip_description = "strip_piledriver", strip_ask_description = "strip_ask_piledriver",
    orgasm_description = "orgasm_piledriver",
    taboo_break_description = "taboo_break_piledriver",
    verb = "piledrive", verbing = "piledriving",
    opinion_tags = ["missionary style sex", "vaginal sex", "being submissive"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "piledriver_double_orgasm")

list_of_positions.append(piledriver)

prone_anal = Position(name = "Prone Anal", slut_requirement = 75, slut_cap = 95, requires_hard = True, requires_large_tits = False,
    position_tag = "back_peek", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 14, girl_energy = 0,
    guy_arousal = 16, guy_energy = 14,
    connections = [],
    intro = "intro_prone_anal",
    scenes = ["scene_prone_anal_1", "scene_prone_anal_2", "scene_prone_anal_3"],
    outro = "outro_prone_anal",
    transition_default = "transition_default_prone_anal",
    strip_description = "strip_prone_anal", strip_ask_description = "strip_ask_prone_anal",
    orgasm_description = "orgasm_prone_anal",
    taboo_break_description = "taboo_break_prone_anal",
    verb = "ass fuck",
    opinion_tags = ["doggy style sex", "anal sex", "being submissive"], record_class = "Anal Sex",
    associated_taboo = "anal_sex",
    double_orgasm = "prone_anal_double_orgasm")

prone_bone = Position(name = "Prone", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
    position_tag = "back_peek", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 18, girl_energy = 0,
    guy_arousal = 16, guy_energy = 14,
    connections = [],
    intro = "intro_prone_bone",
    scenes = ["scene_prone_bone_1", "scene_prone_bone_2", "scene_prone_bone_3"],
    outro = "outro_prone_bone",
    transition_default = "transition_default_prone_bone",
    strip_description = "strip_prone_bone", strip_ask_description = "strip_ask_prone_bone",
    orgasm_description = "orgasm_prone_bone",
    taboo_break_description = "taboo_break_prone_bone",
    opinion_tags = ["doggy style sex", "vaginal sex", "being submissive"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "prone_bone_double_orgasm")

sixty_nine = Position(name = "Sixty-Nine", slut_requirement = 45, slut_cap = 65, requires_hard = False, requires_large_tits = False,
    position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Oral",
    girl_arousal = 15, girl_energy = 13,
    guy_arousal = 16, guy_energy = 15,
    connections = [],
    intro = "intro_sixty_nine",
    scenes = ["scene_sixty_nine_1", "scene_sixty_nine_2"],
    outro = "outro_sixty_nine",
    transition_default = "transition_default_sixty_nine",
    strip_description = "strip_sixty_nine", strip_ask_description = "strip_ask_sixty_nine",
    orgasm_description = "orgasm_sixty_nine",
    taboo_break_description = "taboo_break_sixty_nine",
    verb = "sixty-nine",
    verbing = "sixty-nining",
    opinion_tags = ["giving blowjobs", "getting head", "oral creampie"], record_class = "Cunnilingus",
    gic_tags = ["get mc off", "get off"],
    associated_taboo = "sucking_cock",
    girl_outro = "GIC_outro_sixty_nine",
    double_orgasm = "sixty_nine_double_orgasm")

list_of_positions.append(sixty_nine)
list_of_girl_positions.append(sixty_nine)

skull_fuck = Position(name = "Skull Fuck", slut_requirement = 65, slut_cap = 100, requires_hard = True, requires_large_tits = False,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
    girl_arousal = 5, girl_energy = 10,
    guy_arousal = 25, guy_energy = 12,
    connections = [],
    intro = "intro_skull_fuck",
    scenes = ["scene_skull_fuck_1", "scene_skull_fuck_2", "scene_skull_fuck_3", "scene_skull_fuck_4"],
    outro = "outro_skull_fuck",
    transition_default = "transition_default_skull_fuck",
    strip_description = "strip_skull_fuck", strip_ask_description = "strip_ask_skull_fuck",
    orgasm_description = "orgasm_skull_fuck",
    taboo_break_description = "taboo_break_skull_fuck",
    verb = "throat fuck",
    opinion_tags = ["giving blowjobs", "being submissive"], record_class = "Blowjobs",
    gic_tags = ["get mc off", "oral creampie"],
    associated_taboo = "sucking_cock")

spooning_sex = Position(name = "Spooning", slut_requirement = 60, slut_cap = 85, requires_hard = True, requires_large_tits = False,
    position_tag = "back_peek", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 12, girl_energy = 7,
    guy_arousal = 12, guy_energy = 10,  #A relaxed, low energy position
    connections = [],
    intro = "intro_spooning",
    scenes = ["scene_spooning_1", "scene_spooning_2"],
    outro = "outro_spooning",
    transition_default = "transition_default_spooning",
    strip_description = "strip_spooning", strip_ask_description = "strip_ask_spooning",
    orgasm_description = "orgasm_spooning",
    taboo_break_description = "taboo_break_spooning",
    opinion_tags = ["doggy style sex", "vaginal sex", "being submissive"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "spooning_double_orgasm")

standing_dildo = Position(name = "Dildo Fuck", slut_requirement = 40, slut_cap = 70, requires_hard = False, requires_large_tits = False,
    position_tag = "against_wall", requires_location = "Stand", requires_clothing = "Vagina", skill_tag = "Foreplay",
    girl_arousal = 15, girl_energy = 7,
    guy_arousal = 5, guy_energy = 20,
    connections = [],
    intro = "intro_standing_dildo",
    scenes = ["scene_standing_dildo_1", "scene_standing_dildo_2"],
    outro = "outro_standing_dildo",
    transition_default = "transition_default_standing_dildo",
    strip_description = "strip_standing_dildo", strip_ask_description = "strip_ask_standing_dildo",
    orgasm_description = "orgasm_standing_dildo",
    taboo_break_description = "taboo_break_standing_dildo",
    verb = "dildo",
    opinion_tags = ["being fingered", "sex standing up"], record_class = "Insertions",
    associated_taboo = "touching_vagina")

standing_doggy = Position(name = "Standing Doggy", slut_requirement = 60, slut_cap = 80, requires_hard = True, requires_large_tits = False,
    position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 18, girl_energy = 14,
    guy_arousal = 20, guy_energy = 16,
    connections = [],
    intro = "intro_standing_doggy",
    scenes = ["scene_standing_doggy_1", "scene_standing_doggy_2", "scene_standing_doggy_3", "standing_doggy_stealth_attempt"],
    outro = "outro_standing_doggy",
    transition_default = "transition_default_standing_doggy",
    strip_description = "strip_standing_doggy", strip_ask_description = "strip_ask_standing_doggy",
    orgasm_description = "orgasm_standing_doggy",
    taboo_break_description = "taboo_break_standing_doggy",
    verb = "fuck",
    opinion_tags = ["doggy style sex", "vaginal sex", "sex standing up"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "standing_doggy_double_orgasm")

list_of_positions.append(standing_doggy)

standing_finger = Position(name = "Fingering", slut_requirement = 25, slut_cap = 50, requires_hard = False, requires_large_tits = False,
    position_tag = "walking_away", requires_location = "Stand", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 15, girl_energy = 5,
    guy_arousal = 5, guy_energy = 20,
    connections = [],
    intro = "intro_standing_finger",
    scenes = ["scene_standing_finger_1", "scene_standing_finger_2"],
    outro = "outro_standing_finger",
    transition_default = "transition_default_standing_finger",
    strip_description = "strip_standing_finger", strip_ask_description = "strip_ask_standing_finger",
    orgasm_description = "orgasm_standing_finger",
    taboo_break_description = "taboo_break_standing_finger",
    verb = "finger",
    opinion_tags = ["being fingered", "sex standing up"], record_class = "Fingered",
    associated_taboo = "touching_vagina")

standing_dry_sex = Position(name = "Standing Dry Sex", slut_requirement = 20, slut_cap = 45, requires_hard = True, requires_large_tits = False,
    position_tag = "against_wall", requires_location = "Stand", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 15, girl_energy = 5,
    guy_arousal = 15, guy_energy = 15,
    connections = [],
    intro = "intro_standing_dry_sex",
    scenes = ["scene_standing_dry_sex_1", "scene_standing_dry_sex_2", "scene_standing_dry_sex_3"],
    outro = "outro_standing_dry_sex",
    transition_default = "transition_default_standing_dry_sex",
    strip_description = "strip_standing_dry_sex", strip_ask_description = "strip_ask_standing_dry_sex",
    orgasm_description = "orgasm_standing_dry_sex",
    taboo_break_description = "taboo_break_standing_dry_sex",
    verb = "hump",
    opinion_tags = ["kissing", "sex standing up"], record_class = "Kissing",
    associated_taboo = "kissing",
    double_orgasm = "standing_dry_sex_double_orgasm")

standing_grope = Position(name = "Groping", slut_requirement = 0, slut_cap = 30, requires_hard = False, requires_large_tits = False,
    position_tag = "walking_away", requires_location = "Stand", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 10, girl_energy = 5,
    guy_arousal = 5, guy_energy = 15,
    connections = [],
    intro = "intro_standing_grope",
    scenes = ["scene_standing_grope_1", "scene_standing_grope_2", "scene_standing_grope_3"],
    outro = "outro_standing_grope",
    transition_default = "transition_default_standing_grope",
    strip_description = "strip_standing_grope", strip_ask_description = "strip_ask_standing_grope",
    orgasm_description = "orgasm_standing_grope",
    taboo_break_description = "taboo_break_standing_grope",
    verb = "grope", verbing = "groping",
    opinion_tags = ["sex standing up"],
    associated_taboo = "touching_body")

list_of_positions.append(standing_grope)

standing_oral = Position(name = "Kneeling oral", slut_requirement = 40, slut_cap = 70, requires_hard = False, requires_large_tits = False,
    position_tag = "stand3", requires_location = "Stand", requires_clothing = "Vagina", skill_tag = "Oral",
    girl_arousal = 15, girl_energy = 3,
    guy_arousal = 3, guy_energy = 10,
    connections = [],
    intro = "intro_standing_oral",
    scenes = ["scene_standing_oral_1", "scene_standing_oral_2"],
    outro = "outro_standing_oral",
    transition_default = "transition_default_standing_oral",
    strip_description = "strip_standing_oral",
    strip_ask_description = "strip_ask_standing_oral",
    orgasm_description = "orgasm_standing_oral",
    taboo_break_description = "taboo_break_standing_oral",
    verb = "lick",
    opinion_tags = ["sex standing up", "getting head"],
    gic_tags = ["get off", "hate fuck"],
    record_class = "Cunnilingus",
    associated_taboo = "licking_pussy",
    girl_outro = "GIC_outro_standing_oral")

list_of_girl_positions.append(standing_oral)
list_of_positions.append(standing_oral)

tit_fuck = Position(name = "Tit Fuck", slut_requirement = 30, slut_cap = 55, requires_hard = True, requires_large_tits = True,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "Tits", skill_tag = "Foreplay",
    girl_arousal = 5, girl_energy = 12,
    guy_arousal = 15, guy_energy = 5,
    connections = [],
    intro = "intro_tit_fuck",
    scenes = ["scene_tit_fuck_1", "scene_tit_fuck_2", "scene_tit_fuck_3", "scene_SB_Titfuck_Kneeling_1", "scene_SB_Titfuck_Kneeling_2"],
    outro = "outro_tit_fuck",
    transition_default = "transition_default_tit_fuck",
    strip_description = "strip_tit_fuck", strip_ask_description = "strip_ask_tit_fuck",
    orgasm_description = "orgasm_tit_fuck",
    taboo_break_description = "taboo_break_tit_fuck",
    verb = "tit fuck",
    opinion_tags = ["giving tit fucks"], record_class = "Tit Fucks",
    gic_tags = ["get mc off", "body shot"],
    associated_taboo = "touching_penis",
    girl_outro = "GIC_outro_tit_fuck")

list_of_positions.append(tit_fuck)


#############################
# Girl In Control Positions #
#############################

anal_cowgirl = Position("Anal Cowgirl", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
    position_tag = "cowgirl", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
    girl_arousal = 22, girl_energy = 20,
    guy_arousal = 16, guy_energy = 14,
    connections = [],
    intro = "intro_anal_cowgirl",
    scenes = ["scene_anal_cowgirl_1", "scene_anal_cowgirl_2", "scene_anal_cowgirl_3", "scene_anal_cowgirl_4"],
    outro = "outro_anal_cowgirl",
    transition_default = "transition_default_anal_cowgirl",
    strip_description = "strip_anal_cowgirl", strip_ask_description = "strip_ask_anal_cowgirl",
    taboo_break_description = "taboo_break_anal_cowgirl",
    orgasm_description = "orgasm_anal_cowgirl",
    verb = "ass fuck",
    opinion_tags = ["taking control", "anal sex", "anal creampie"], record_class = "Anal Sex",
    gic_tags = ["get off", "get mc off", "anal creampie", "hate fuck"],
    associated_taboo = "anal_sex",
    double_orgasm = "anal_cowgirl_double_orgasm",
    girl_outro = "GIC_outro_anal_cowgirl")

list_of_girl_positions.append(anal_cowgirl)

cowgirl_blowjob = Position(name = "Cowgirl Blowjob", slut_requirement = 40, slut_cap = 60, requires_hard = True, requires_large_tits = False,
    position_tag = "blowjob", requires_location = "Lay", requires_clothing = "None", skill_tag = "Oral",
    girl_arousal = 3, girl_energy = 13,
    guy_arousal = 16, guy_energy = 5,
    connections = [],
    intro = "intro_cowgirl_blowjob",
    scenes = ["scene_cowgirl_blowjob_1", "scene_cowgirl_blowjob_2", "scene_cowgirl_blowjob_3"],
    outro = "outro_cowgirl_blowjob",
    transition_default = "transition_default_cowgirl_blowjob",
    strip_description = "strip_cowgirl_blowjob", strip_ask_description = "strip_ask_cowgirl_blowjob",
    orgasm_description = "orgasm_cowgirl_blowjob",
    taboo_break_description = "taboo_break_cowgirl_blowjob",
    verb = "mouth fuck",
    opinion_tags = ["giving blowjobs", "facial", "oral creampie"], record_class = "Blowjobs",
    gic_tags = ["get mc off"],
    associated_taboo = "sucking_cock",
    girl_outro = "GIC_outro_cowgirl_blowjob")

list_of_girl_positions.append(cowgirl_blowjob)

cowgirl_cunnilingus = Position(name = "Cowgirl Cunnilingus", slut_requirement = 40, slut_cap = 80, requires_hard = False, requires_large_tits = False,
    position_tag = "kneeling1", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Oral",
    girl_arousal = 15, girl_energy = 3,
    guy_arousal = 3, guy_energy = 15,
    connections = [],
    intro = "intro_cowgirl_cunnilingus",
    scenes = ["scene_cowgirl_cunnilingus_1", "scene_cowgirl_cunnilingus_2", "scene_cowgirl_cunnilingus_3"],
    outro = "outro_cowgirl_cunnilingus",
    transition_default = "transition_default_cowgirl_cunnilingus",
    strip_description = "strip_cowgirl_cunnilingus", strip_ask_description = "strip_ask_cowgirl_cunnilingus",
    orgasm_description = "orgasm_cowgirl_cunnilingus",
    taboo_break_description = "taboo_break_cowgirl_cunnilingus",
    verb = "lick",
    opinion_tags = ["getting head", "taking control"], record_class = "Cunnilingus",
    gic_tags = ["get off", "hate fuck"],
    associated_taboo = "licking_pussy",
    girl_outro = "GIC_outro_cowgirl_cunnilingus")

list_of_girl_positions.append(cowgirl_cunnilingus)

cowgirl_handjob = Position(name = "Cowgirl Handjob", slut_requirement = 20, slut_cap = 50, requires_hard = False, requires_large_tits = False,
    position_tag = "kneeling1", requires_location = "Lay", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 3, girl_energy = 10,
    guy_arousal = 14, guy_energy = 5,
    connections = [],
    intro = "intro_cowgirl_handjob",
    scenes = ["scene_cowgirl_handjob_1", "scene_cowgirl_handjob_2", "scene_cowgirl_handjob_3"],
    outro = "outro_cowgirl_handjob",
    transition_default = "transition_default_cowgirl_handjob",
    strip_description = "strip_cowgirl_handjob", strip_ask_description = "strip_ask_cowgirl_handjob",
    orgasm_description = "orgasm_cowgirl_handjob",
    taboo_break_description = "taboo_break_cowgirl_handjob",
    verb = "get stroked by", verbing = "getting stroked",
    opinion_tags = ["giving handjobs", "facial"], record_class = "Handjobs",
    gic_tags = ["get mc off", "waste cum", "body shot"],
    associated_taboo = "touching_penis",
    girl_outro = "GIC_outro_cowgirl_handjob")

list_of_girl_positions.append(cowgirl_handjob)

cowgirl = Position(name = "Cowgirl", slut_requirement = 60, slut_cap = 80, requires_hard = True, requires_large_tits = False,
    position_tag = "cowgirl", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 18, girl_energy = 14,
    guy_arousal = 14, guy_energy = 10,
    connections = [],
    intro = "intro_cowgirl",
    scenes = ["scene_cowgirl_1", "scene_cowgirl_2", "scene_cowgirl_3"],
    outro = "outro_cowgirl",
    transition_default = "transition_default_cowgirl",
    strip_description = "strip_cowgirl", strip_ask_description = "strip_ask_cowgirl",
    orgasm_description = "orgasm_cowgirl",
    taboo_break_description = "taboo_break_cowgirl",
    verb = "fuck",
    opinion_tags = ["vaginal sex", "taking control"], record_class = "Vaginal Sex",
    gic_tags = ["vaginal creampie", "get off", "hate fuck", "body shot"],
    associated_taboo = "vaginal_sex",
    double_orgasm = "cowgirl_double_orgasm",
    girl_outro= "GIC_outro_cowgirl")

list_of_girl_positions.append(cowgirl)

handjob = Position(name = "Handjob", slut_requirement = 15, slut_cap = 40, requires_hard = False, requires_large_tits = False,
    position_tag = "stand3", requires_location = "Stand", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 5, girl_energy = 10,
    guy_arousal = 14, guy_energy = 2,
    connections = [],
    intro = "intro_handjob",
    scenes = ["scene_handjob_1", "scene_handjob_2", "scene_handjob_3"],
    outro = "outro_handjob",
    transition_default = "transition_default_handjob",
    strip_description = "strip_handjob", strip_ask_description = "strip_ask_handjob",
    orgasm_description = "orgasm_handjob",
    taboo_break_description = "taboo_break_handjob",
    verb = "get stroked by", verbing = "getting stroked",
    opinion_tags = ["giving handjobs"], record_class = "Handjobs",
    gic_tags = ["get mc off", "waste cum", "body shot"],
    associated_taboo = "touching_penis",
    girl_outro = "GIC_outro_handjob")

list_of_girl_positions.append(handjob)

drysex_cowgirl = Position(name = "Dry Cowgirl", slut_requirement = 20, slut_cap = 40, requires_hard = False, requires_large_tits = False,
    position_tag = "cowgirl", requires_location = "Lay", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 12, girl_energy = 9,
    guy_arousal = 10, guy_energy = 11,
    connections = [],
    intro = "intro_drysex_cowgirl",
    scenes = ["scene_drysex_cowgirl_1", "scene_drysex_cowgirl_2"],
    outro = "outro_drysex_cowgirl",
    transition_default = "transition_default_drysex_cowgirl",
    strip_description = "strip_drysex_cowgirl", strip_ask_description = "strip_ask_drysex_cowgirl",
    orgasm_description = "orgasm_drysex_cowgirl",
    taboo_break_description = "taboo_break_drysex_cowgirl",
    verb = "fuck",
    opinion_tags = ["taking control"],
    gic_tags = ["get mc off", "get off", "waste cum"],
    associated_taboo = "touching_body",
    girl_outro = "GIC_outro_drysex_cowgirl")

list_of_girl_positions.append(drysex_cowgirl)

reverse_cowgirl = Position(name = "Reverse Cowgirl", slut_requirement = 60, slut_cap = 80, requires_hard = True, requires_large_tits = False,
    position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 18, girl_energy = 14,
    guy_arousal = 14, guy_energy = 10,
    connections = [],
    intro = "intro_reverse_cowgirl",
    scenes = ["scene_reverse_cowgirl_1", "scene_reverse_cowgirl_2"],
    outro = "outro_reverse_cowgirl",
    transition_default = "transition_default_reverse_cowgirl",
    strip_description = "strip_reverse_cowgirl", strip_ask_description = "strip_ask_reverse_cowgirl",
    orgasm_description = "orgasm_reverse_cowgirl",
    taboo_break_description = "taboo_break_reverse_cowgirl",
    verb = "fuck",
    opinion_tags = ["taking control", "vaginal sex", "vaginal creampie"], record_class = "Vaginal Sex",
    gic_tags = ["vaginal creampie", "get off", "hate fuck", "body shot"],
    associated_taboo = "vaginal_sex",
    double_orgasm = "reverse_cowgirl_double_orgasm",
    girl_outro = "GIC_outro_reverse_cowgirl")

list_of_girl_positions.append(reverse_cowgirl)

standing_cunnilingus = Position(name = "Standing Cunnilingus", slut_requirement = 40, slut_cap = 80, requires_hard = False, requires_large_tits = False,
    position_tag = "against_wall", requires_location = "Lean", requires_clothing = "Vagina", skill_tag = "Oral",
    girl_arousal = 15, girl_energy = 3,
    guy_arousal = 3, guy_energy = 12,
    connections = [],
    intro = "intro_standing_cunnilingus",
    scenes = ["scene_standing_cunnilingus_1", "scene_standing_cunnilingus_2"],
    outro = "outro_standing_cunnilingus",
    transition_default = "transition_default_standing_cunnilingus",
    strip_description = "strip_standing_cunnilingus", strip_ask_description = "strip_ask_standing_cunnilingus",
    orgasm_description = "orgasm_standing_cunnilingus",
    taboo_break_description = "taboo_break_standing_cunnilingus",
    verb = "lick",
    opinion_tags = ["getting head", "taking control"], record_class = "Cunnilingus",
    gic_tags = ["get off", "hate fuck"],
    associated_taboo = "licking_pussy",
    girl_outro = "GIC_outro_standing_cunnilingus")

list_of_girl_positions.append(standing_cunnilingus)


####################
# Fetish Positions #
####################
bent_over_breeding = Position(name = "Breeding Doggy", slut_requirement = 60, slut_cap = 100, requires_hard = True, requires_large_tits = False,
    position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 18, girl_energy = 14,
    guy_arousal = 20, guy_energy = 16,
    connections = [],
    intro = "intro_bent_over_breeding",
    scenes = ["scene_bent_over_breeding_1", "scene_bent_over_breeding_2", "scene_bent_over_breeding_3"],
    outro = "outro_bent_over_breeding",
    transition_default = "transition_default_bent_over_breeding",
    strip_description = "strip_bent_over_breeding", strip_ask_description = "strip_ask_bent_over_breeding",
    orgasm_description = "orgasm_bent_over_breeding",
    taboo_break_description = "taboo_break_bent_over_breeding",
    verb = "fuck",
    opinion_tags = ["doggy style sex", "vaginal sex", "sex standing up", "bareback sex"], record_class = "Vaginal Sex",
    associated_taboo = "condomless_sex",
    double_orgasm = "bent_over_breeding_double_orgasm")

breeding_missionary = Position(name = "Breeding Missionary", slut_requirement = 50, slut_cap = 100, requires_hard = True, requires_large_tits = False,
    position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
    girl_arousal = 16, girl_energy = 8,
    guy_arousal = 15, guy_energy = 10,
    connections = [],
    intro = "intro_breeding_missionary",
    scenes = ["scene_breeding_missionary_1", "scene_breeding_missionary_2"],
    outro = "outro_breeding_missionary",
    transition_default = "transition_default_breeding_missionary",
    strip_description = "strip_breeding_missionary", strip_ask_description = "strip_ask_breeding_missionary",
    orgasm_description = "orgasm_breeding_missionary",
    taboo_break_description = "taboo_break_breeding_missionary",
    opinion_tags = ["missionary style sex", "vaginal sex"], record_class = "Vaginal Sex",
    associated_taboo = "vaginal_sex",
    double_orgasm = "breeding_missionary_double_orgasm")

cum_fetish_blowjob = Position(name = "Cum Fetish Blowjob", slut_requirement = 40, slut_cap = 90, requires_hard = True, requires_large_tits = False,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
    girl_arousal = 13, girl_energy = 10,
    guy_arousal = 15, guy_energy = 3,
    connections = [],
    intro = "intro_cum_fetish_blowjob",
    scenes = ["scene_cum_fetish_blowjob_1", "scene_cum_fetish_blowjob_2"],
    outro = "outro_cum_fetish_blowjob",
    transition_default = "transition_default_cum_fetish_blowjob",
    strip_description = "strip_cum_fetish_blowjob", strip_ask_description = "strip_ask_cum_fetish_blowjob",
    orgasm_description = "orgasm_cum_fetish_blowjob",
    double_orgasm = "cum_fetish_blowjob_double_orgasm",
    taboo_break_description = "taboo_break_cum_fetish_blowjob",
    verb = "throat fuck",
    opinion_tags = ["giving blowjobs"], record_class = "Blowjobs",
    gic_tags = ["get mc off", "oral creampie", "facial"],
    associated_taboo = "sucking_cock")

spanking = Position(name = "Spanking", slut_requirement = 30, slut_cap = 50, requires_hard = False, requires_large_tits = False,
    position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "None", skill_tag = "Foreplay",
    girl_arousal = 0, girl_energy = 5,  #We use person specific variables to determine arousal
    guy_arousal = 0, guy_energy = 5,
    connections = [],
    intro = "intro_spanking",
    scenes = ["scene_spanking_1", "scene_spanking_2"],
    outro = "outro_spanking",
    transition_default = "transition_default_spanking",
    strip_description = "strip_spanking", strip_ask_description = "strip_ask_spanking",
    orgasm_description = "orgasm_spanking",
    taboo_break_description = "taboo_break_spanking",
    verb = "spank",
    opinion_tags = ["being submissive"], record_class = "Spankings",
    associated_taboo = "touching_body")

####################
# Unique Positions #
####################

sarah_tit_fuck = Position(name = "Special Tit Fuck", slut_requirement = 30, slut_cap = 55, requires_hard = True, requires_large_tits = True,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "Tits", skill_tag = "Foreplay",
    girl_arousal = 7, girl_energy = 20,
    guy_arousal = 15, guy_energy = 5,
    connections = [],
    intro = "intro_sarah_tit_fuck",
    scenes = ["scene_sarah_tit_fuck_1", "scene_sarah_tit_fuck_2", "scene_sarah_tit_fuck_3"],
    outro = "outro_sarah_tit_fuck",
    transition_default = "transition_default_sarah_tit_fuck",
    strip_description = "strip_sarah_tit_fuck", strip_ask_description = "strip_ask_sarah_tit_fuck",
    orgasm_description = "orgasm_sarah_tit_fuck",
    taboo_break_description = "taboo_break_sarah_tit_fuck",
    verb = "tit fuck",
    opinion_tags = ["giving tit fucks"], record_class = "Tit Fucks",
    gic_tags = ["get mc off", "body shot"],
    associated_taboo = "touching_body")

ophelia_blowjob = Position(name = "Special Blowjob", slut_requirement = 30, slut_cap = 60, requires_hard = True, requires_large_tits = False,
    position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
    girl_arousal = 3, girl_energy = 13,
    guy_arousal = 18, guy_energy = 5,
    connections = [],
    intro = "intro_ophelia_blowjob",
    scenes = ["scene_ophelia_blowjob_1", "scene_ophelia_blowjob_2"],
    outro = "outro_ophelia_blowjob",
    transition_default = "transition_default_ophelia_blowjob",
    strip_description = "strip_ophelia_blowjob", strip_ask_description = "strip_ask_ophelia_blowjob",
    orgasm_description = "orgasm_ophelia_blowjob",
    taboo_break_description = "taboo_break_ophelia_blowjob",
    verb = "throat fuck",
    opinion_tags = ["giving blowjobs"], record_class = "Blowjobs",
    gic_tags = ["get mc off", "oral creampie", "facial"],
    associated_taboo = "sucking_cock")


##################
# link positions #
##################

anal_standing.link_positions(standing_doggy, "transition_anal_standing_standing_doggy")
anal_standing.link_positions(doggy_anal, "transition_anal_standing_doggy_anal")

blowjob.link_positions(deepthroat, "transition_blowjob_deepthroat")

deepthroat.link_positions(blowjob, "transition_deepthroat_blowjob")
deepthroat.link_positions(skull_fuck, "transition_deepthroat_skull_fuck")

doggy.link_positions_two_way(doggy_anal, "transition_doggy_doggy_anal", "transition_stealth_doggy_anal_doggy")

facing_wall.link_positions_two_way(against_wall, "transition_facing_wall_against_wall", "transition_against_wall_facing_wall")

kissing.link_positions(blowjob, "transition_kissing_blowjob")
kissing.link_positions(handjob, "transition_kissing_handjob")
kissing.link_positions(standing_dry_sex, "transition_kissing_standing_dry_sex")

missionary.link_positions_two_way(piledriver, "transition_missionary_piledriver", "transition_piledriver_missionary")

piledriver.link_positions(piledriver_anal, "transition_piledriver_piledriver_anal")
piledriver_anal.link_positions(piledriver, "transition_piledriver_anal_to_piledriver")

prone_anal.link_positions_two_way(prone_bone, "transition_prone_anal_prone_bone", "transition_prone_bone_prone_anal")

missionary.link_positions(reverse_cowgirl, "transition_missionary_reverse_cowgirl")
reverse_cowgirl.link_positions(doggy, "transition_reverse_cowgirl_doggy")

skull_fuck.link_positions(deepthroat, "transition_skull_fuck_deepthroat_blowjob")

spanking.link_positions(standing_doggy, "transition_spanking_standing_doggy")

standing_doggy.link_positions(anal_standing, "transition_standing_doggy_anal_standing")
standing_doggy.link_positions(doggy, "transition_standing_doggy_doggy")

standing_grope.link_positions_two_way(standing_finger, "transition_standing_grope_standing_fingering", "transition_standing_fingering_standing_grope")
