from __future__ import annotations
from game.people.Camila.camila_definition_ren import mc_dancing_skill
from game.major_game_classes.game_logic.Room_ren import mall, downtown_bar
from game.major_game_classes.character_related.Person_ren import Person, mc, camila
from game.major_game_classes.game_logic.Action_ren import Action

TIER_1_TIME_DELAY = 3
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

def init_camila_story_line():
    camila.add_unique_on_room_enter_event(
        Action("Shopping Trip", camila_outfit_help_requirement, "camila_outfit_help_label", priority = 30)
    )
    camila.add_unique_on_room_enter_event(
        Action("Making New Goals", camila_obedience_new_goals_requirement, "camila_obedience_new_goals_label", priority = 30)
    )
    camila.set_event_day("obedience_event")
    camila.set_event_day("love_event")
    camila.set_event_day("slut_event")
    camila.set_event_day("story_event")
    camila.event_triggers_dict["bar_met"] = True

##### Love Events #####

def camila_outfit_help_requirement(person: Person):
    return (person.love > 20
        and person.story_event_ready("love")
        and person.has_event_delay("last_shopping_day", 6)
        and person.is_at(mall))

def camila_lingerie_help_requirement(person: Person):
    return (person.love > 40
        and person.story_event_ready("love")
        and person.has_event_delay("last_shopping_day", 6)
        and camila.days_since_event("camila_blowjob_pic_day") > 0
        and person.is_at(mall))

def add_camila_lingerie_help_action():
    camila.add_unique_on_room_enter_event(
        Action("Lingerie Shopping", camila_lingerie_help_requirement, "camila_lingerie_help_label", priority = 30)
    )
    camila.event_triggers_dict["help_with_outfit"] = True
    camila.story_event_log("love")

def camila_formal_date_requirement():
    return time_of_day == 3 and day % 7 < 4 and camila.love >= 60 and camila.story_event_ready("love") and camila.is_available

def add_camila_formal_date_action():
    mc.business.add_mandatory_crisis(
        Action("Camila Comes Over", camila_formal_date_requirement, "camila_formal_date_label")
    )
    camila.event_triggers_dict["help_with_lingerie"] = True
    camila.story_event_log("love")

def camila_gives_anal_virginity_requirement(person: Person):
    return False

def add_camila_gives_anal_virginity_action():
    camila.add_unique_on_room_enter_event(
        Action("Camila Tries Anal", camila_gives_anal_virginity_requirement, "camila_gives_anal_virginity_label", priority = 30)
    )
    camila.event_triggers_dict["formal_date"] = True


##### Lust Events #####


def camila_dance_lessons_requirement():
    return day % 7 == 2 and time_of_day == 3

def add_camila_dance_lessons_action():
    mc.business.add_mandatory_crisis(
        Action("Dancing Lessons", camila_dance_lessons_requirement, "camila_dance_lessons_label")
    )

def camila_bathroom_blowjob_requirement(person: Person):
    return person.sluttiness > 40 and person.story_event_ready("slut") and person.is_at(downtown_bar)

def add_camila_bathroom_blowjob_action():
    camila.add_unique_on_room_enter_event(
        Action("Bathroom Blowjob", camila_bathroom_blowjob_requirement, "camila_bathroom_blowjob_label", priority = 30)
    )
    camila.event_triggers_dict["go_dancing"] = True

def camila_blowjob_text_requirement(person: Person):
    return person.days_since_event("camila_blowjob_pic_day") > 0

def add_camila_blowjob_text_action():
    camila.add_unique_on_room_enter_event(
        Action("Blowjob Discussion", camila_blowjob_text_requirement, "camila_blowjob_text_label", priority = 30)
    )
    camila.set_event_day("camila_blowjob_pic_day")

def camila_dancing_sex_requirement(person: Person):
    return person.sluttiness > 60 and person.story_event_ready("slut") and person.is_at(downtown_bar) and mc_dancing_skill() >= 6

def add_camila_dancing_sex_action():
    camila.add_unique_on_room_enter_event(
        Action("First Sex", camila_dancing_sex_requirement, "camila_dancing_sex_label", priority = 30)
    )

def camila_sex_invite_requirement(person: Person):
    return time_of_day == 3 and person.sluttiness > 80 and person.story_event_ready("slut") and person.is_at(downtown_bar)

def add_camila_sex_invite_action():
    camila.add_unique_on_room_enter_event(
        Action("House Call", camila_sex_invite_requirement, "camila_sex_invite_label", priority = 30)
    )
    camila.event_triggers_dict["bathroom_sex"] = True

def camila_her_place_requirement():
    return time_of_day == 4

def add_camila_her_place_action():
    mc.business.add_mandatory_crisis(
        Action("Cuckold Visit", camila_her_place_requirement, "camila_her_place_label", priority = 30)
    )
    camila.learn_home()


##### Obedience Events #####

def camila_obedience_new_goals_requirement(person: Person):
    return person.obedience > 100 and person.story_event_ready("obedience") and person.is_at(mall)

def camila_obedience_new_personal_goals_requirement(person: Person):
    return person.obedience > 120 and person.story_event_ready("obedience") and person.is_at(mall)

def add_camila_obedience_new_personal_goals_action():
    camila.add_unique_on_room_enter_event(
        Action("Exploring Personal goals", camila_obedience_new_personal_goals_requirement, "camila_obedience_new_personal_goals_label", priority = 30)
    )
    camila.event_triggers_dict["goal_coach"] = True

def camila_obedience_sexual_goals_intro_requirement(person: Person):
    return person.obedience > 140 and person.story_event_ready("obedience") and person.is_at(mall)

def add_camila_obedience_sexual_goals_intro_action():
    camila.add_unique_on_room_enter_event(
        Action("Exploring Sexual Goals", camila_obedience_sexual_goals_intro_requirement, "camila_obedience_sexual_goals_intro_label", priority = 30)
    )
    camila.event_triggers_dict["goal_coach"] = True

def camila_obedience_tit_fuck_requirement(person: Person):
    return person.obedience > 160 and person.story_event_ready("obedience") and person.is_at(mall) and person.is_at_work

def add_camila_obedience_tit_fuck_action():
    camila.add_unique_on_room_enter_event(
        Action("MC Loves Tits", camila_obedience_tit_fuck_requirement, "camila_obedience_tit_fuck_label", priority = 30)
    )
    camila.story_event_log("obedience")
    camila.event_triggers_dict["sex_goal_coach"] = True

def camila_obedience_ass_man_requirement(person: Person):
    return False
    return person.obedience > 180 and person.story_event_ready("obedience") and person.is_at(mall) and person.is_at_work

def add_camila_obedience_ass_man_action():
    camila.add_unique_on_room_enter_event(
        Action("MC Loves Ass", camila_obedience_ass_man_requirement, "camila_obedience_ass_man_label", priority = 30)
    )
    camila.event_triggers_dict["obedience_titfuck"] = True
