from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.people.Jennifer.personal_secretary_progression_scene_definition_ren import personal_secretary_prog_scene
from game.main_character.perks.Perks_ren import perk_system

day = 0
time_of_day = 0
crisis_list = []
"""renpy
init -1 python:
"""

def personal_secretary_test_requirement(person: Person):
    return False

def personal_secretary_set_lust_tier_requirement(person: Person):
    return (
        0 in personal_secretary_prog_scene.scene_unlock_list
        and person.is_at_office
    )

def get_personal_secretary_role_actions():
    # personal_secretary_test_action = Action("Secretary Test Action {image=time_advance}", personal_secretary_test_requirement, "personal_secretary_test_label",
    #     menu_tooltip = "A test label for making a personal secretary")
    personal_secretary_set_lust_tier_action = Action("Change sexual relief instructions",
        personal_secretary_set_lust_tier_requirement,
        "personal_secretary_set_lust_tier_label",
        menu_tooltip = "Change the trigger for how much lust is required before she approaches you for sex in your office.",
        priority = 20)
    return [personal_secretary_set_lust_tier_action]

personal_secretary_role = Role("Personal Secretary", get_personal_secretary_role_actions(), hidden = True) #Actions go in block

# Some easy to use functions to determine if your personal secretary will put out at specific levels to make it easy to call in to various situations.
# EG if she is willing to suck, maybe add to a crisis that she is already under MC's desk servicing him when a crisis starts.
def personal_secretary_will_suck():
    return (isinstance(mc.business.personal_secretary, Person)
        and 2 in personal_secretary_prog_scene.scene_unlock_list
        and mc.business.personal_secretary.is_at_work)

def personal_secretary_will_ride():
    return (isinstance(mc.business.personal_secretary, Person)
        and 3 in personal_secretary_prog_scene.scene_unlock_list
        and mc.business.personal_secretary.is_at_work)

def personal_secretary_will_fuck():
    return (isinstance(mc.business.personal_secretary, Person)
        and 4 in personal_secretary_prog_scene.scene_unlock_list
        and mc.business.personal_secretary.is_at_work)

##########################
#  Popup text functions  #
##########################

def personal_secretary_quick_service_fuck_popup_text():
    if mc.sex_skills["Vaginal"] >= 6 and (mc.max_energy >= 160 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control")) and mc.business.personal_secretary.effective_sluttiness() >= 80:
        return "Full Scene"
    popup_text = ["Partial Scene:"]
    if mc.sex_skills["Vaginal"] < 6:
        popup_text.append("Vaginal Skill 6+")
    if mc.max_energy < 160:
        popup_text.append("Max Energy 160+")
    if mc.business.personal_secretary.effective_sluttiness() < 80:
        popup_text.append("Secretary Sluttiness +80")
    return "\n  ".join(popup_text)

def personal_secretary_quick_service_suck_popup_text():
    if mc.business.personal_secretary.sex_skills["Oral"] >= 4 and (mc.max_energy >= 160 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control")) and mc.business.personal_secretary.effective_sluttiness() >= 60:
        return "Full Scene"
    popup_text = ["Partial Scene:"]
    if mc.business.personal_secretary.sex_skills["Oral"] < 4:
        popup_text.append("Secretary Oral Skill 4+")
    if mc.max_energy < 160:
        popup_text.append("Max Energy 160+")
    if mc.business.personal_secretary.effective_sluttiness() < 60:
        popup_text.append("Secretary Sluttiness +60")
    return "\n  ".join(popup_text)
