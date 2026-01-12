import renpy
from game.game_roles.relationship_role_definition_ren import get_girlfriend_role_actions, get_girlfriend_role_dates
from game.game_roles._role_definitions_ren import girlfriend_role, sister_role, mother_role
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import kitchen, lily_bedroom, mom_bedroom, bedroom, hall
from game.major_game_classes.character_related.Person_ren import Person, mc, mom, lily, aunt
from game.major_game_classes.character_related.Job_ren import mom_associate_job, mom_secretary_job
from game.major_game_classes.clothing_related.Wardrobe_ren import business_wardrobe
from game.people.Lily.lily_role_definition_ren import had_family_threesome

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def lily_knows_about_mom():
    return had_family_threesome() or lily.event_triggers_dict.get("mom_girlfriend_sister_knows", False)

def mom_taboo_completed():
    return mom.event_triggers_dict.get("vaginal_revisit_complete", False) 

def lily_taboo_completed():
    return lily.event_triggers_dict.get("vaginal_revisit_complete", False)

def mom_virgin_before():
    return mom.event_triggers_dict.get("virgin_mom", False) 
    #if vt_enabled() and mom.vaginal_virgin == 0:

def mom_our_secretary():
    return mom.is_employee and mom.event_triggers_dict.get("personal_sec", False)

def home_harem():
    return mc.business.event_triggers_dict.get("exclusive_home_harem", False)

def mom_want_baby():
    return mom.event_triggers_dict.get("preg_wanted", False)

def lily_want_baby():
    return lily.event_triggers_dict.get("preg_wanted", False)

def family_prefer_incest():
    return (mom.known_opinion.incest == 2 and lily.known_opinion.incest == 2)