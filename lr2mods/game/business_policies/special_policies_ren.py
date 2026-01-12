from __future__ import annotations
from renpy.display.im import Image
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.character_related.Person_ren import mc, sarah, city_rep, police_chief
from game.major_game_classes.game_logic.Room_ren import clone_facility, rd_division, ceo_office
from game.business_policies.organisation_policies_ren import increase_max_employee_size
from game.general_actions.downtown_bar_actions import add_downtown_bar_topless_action, add_downtown_bar_nudity_action, add_downtown_bar_sex_booth_unlock_action

special_policies_list: list[Policy] = []
biotech_build_cloning_facility = Action("", None, "")
biotech_modify_person = Action("", None, "")
biotech_clone_person = Action("", None, "")
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""

def HR_director_creation_requirement():
    if sarah.has_event_day("day_met"):
        return True
    return "Meeting Sarah and hire her as HR Director"

HR_director_creation_policy = Policy(name = "Create HR Director Position",
    desc = "Create a new position for an HR Director. Increases maximum employee count by one.",
    cost = 500,
    requirement = HR_director_creation_requirement,
    on_buy_function = increase_max_employee_size,
    extra_arguments = {"amount": 1})

def personal_secretary_creation_requirement():
    if mc.business.event_triggers_dict.get("personal_secretary_policy_avail", False) or len(mc.business.hr_team) >= 2:
        return True
    return "Story Progression with Jennifer"

# personal_secretary_creation_policy = Policy(name = "Create Personal Secretary Position",
#     desc = "Create a new position for a Personal Secretary. Increases maximum employee count by one.",
#     cost = 1500,
#     requirement = personal_secretary_creation_requirement,
#     on_buy_function = increase_max_employee_size,
#     extra_arguments = {"amount": 1})

def production_assistant_creation_requirement():
    if mc.business.event_triggers_dict.get("production_assistant_policy_avail", False):
        return True
    return "Story Progression with Stephanie, or Hire Ashley"

production_assistant_creation_policy = Policy(name = "Create Production Assistant Position",
    desc = "Create a new position for a Production Assistant to create personal use serums.",
    cost = 1500,
    requirement = production_assistant_creation_requirement)

def it_director_creation_requirement():
    if mc.business.event_triggers_dict.get("it_director_policy_avail", False):
        return True
    return "Story Progression with Stephanie and Nanobots, or Hire Ellie"

it_director_creation_policy = Policy(name = "Create IR Director Position",
    desc = "Create a new position for an IT Director to enhance nanobots and enhance your company workflows.",
    cost = 3500,
    requirement = it_director_creation_requirement)

def testing_room_creation_requirement():
    if mc.business.event_triggers_dict.get("testing_room_policy_avail", False):
        return True
    return "Story Progression"

def testing_room_policy_unlock(unlock):
    mc.business.event_triggers_dict["testing_room_policy_unlock"] = unlock

def unisex_bathroom_policy_requirement():
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_avail", 0) == 1:
        return True
    return "The unlock event where girls complain about the bathrooms"

def unlock_unisex_bathroom_policy(unlock):
    mc.business.unisex_restroom_unlocks["unisex_policy_unlock"] = unlock

def genetic_modification_policy_requirement():
    if mc.business.research_tier >= 2:
        return True
    return "Tier 2 Research"

def unlock_genetic_modification():
    rd_division.background_name = "Biotech_Background"
    ceo_office.add_action(biotech_build_cloning_facility)
    rd_division.add_action(biotech_modify_person)
    mc.log_event("You can now buy the cloning facility from the CEO office", "float_text_yellow")

def genetic_manipulation_policy_requirement():
    if mc.business.research_tier >= 3:
        if not clone_facility.visible:
            return "Build cloning facility"
        return True
    return "Tier 3 Research"

def unlock_genetic_manipulation():
    clone_facility.add_action(biotech_clone_person)

def topless_legal_requirement():
    if mc.business.council_members_influenced > 0:  #Bypass city admin by going directly to other officials.
        return True
    if not city_rep.event_triggers_dict.get("discussed_topless_is_legal", False):
        return "Convince the City Administrator to wear a slutty outfit to work."
    if ((city_rep.sluttiness > 50 or city_rep.obedience > 180)
            and (police_chief.sluttiness > 50 or police_chief.obedience > 180)):
        return True
    return "Corrupt city officials - City Administrator and Policy Chief (sluttiness > 50 or obedience > 180)"

def public_sex_act_legal_requirement():
    if mc.business.council_members_influenced > 0:
        return True
    return "Gain influence over more city officials"

def public_sex_legal_requirement():
    if mc.business.council_members_influenced > 1:
        return True
    return "Gain influence over more city officials"

def topless_legal_unlock(unlock: bool):
    mc.business.event_triggers_dict["topless_is_legal"] = unlock
    add_downtown_bar_topless_action()

def nudity_legal_unlock(unlock: bool):
    mc.business.event_triggers_dict["nudity_is_legal"] = unlock
    add_downtown_bar_nudity_action()

def public_sex_act_legal_unlock(unlock: bool):
    mc.business.event_triggers_dict["public_sex_act_is_legal"] = unlock
    add_downtown_bar_sex_booth_unlock_action()

def public_sex_legal_unlock(unlock: bool):
    mc.business.event_triggers_dict["public_sex_is_legal"] = unlock

def init_special_policies():
    global HR_director_creation_policy
    HR_director_creation_policy = Policy(name = "Create HR Director Position",
        desc = "Create a new position for an HR Director. Increases maximum employee count by one.",
        cost = 500,
        requirement = HR_director_creation_requirement,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 1})

    global personal_secretary_creation_policy
    personal_secretary_creation_policy = Policy(name = "Create Personal Secretary Position",
        desc = "Create a new position for a Personal Secretary. Increases maximum employee count by one.",
        cost = 1500,
        requirement = personal_secretary_creation_requirement,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 1})

    global production_assistant_creation_policy
    production_assistant_creation_policy = Policy(name = "Create Production Assistant Position",
        desc = "Create a new position for a Production Assistant to create personal use serums.",
        cost = 1500,
        requirement = production_assistant_creation_requirement,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 1})
    
    global it_director_creation_policy
    it_director_creation_policy = Policy(name = "Create IT Director Position",
        desc = "Create a new position for an IT Director to enhance nanobots and enhance your company workflows.",
        cost = 3500,
        requirement = it_director_creation_requirement,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 1})

    global testing_room_creation_policy
    testing_room_creation_policy = Policy(name = "Serum Testing Room",
        desc = "Some medical equipment, a couple windows, and a privacy curtain creates an ideal place to test specific serum traits.",
        cost = 1000,
        requirement = testing_room_creation_requirement,
        on_buy_function = testing_room_policy_unlock,
        extra_arguments = {"unlock": True})
    global unisex_bathroom_creation_policy
    unisex_bathroom_creation_policy = Policy(name = "Make Restrooms Unisex",
        desc = "Some basic remodelling and a change of signs will make all company restrooms unisex.",
        cost = 1000,
        requirement = unisex_bathroom_policy_requirement,
        on_buy_function = unlock_unisex_bathroom_policy,
        extra_arguments = {"unlock": 1})
    global genetic_modification_policy
    genetic_modification_policy = Policy(
        name = "Genetic Modification License",
        cost = 50000,
        desc = "Allows genetic sequencing of human DNA for cosmetic changes.\nRequires research Tier 2 unlocked.",
        requirement = genetic_modification_policy_requirement,
        on_buy_function = unlock_genetic_modification,
    )
    global genetic_manipulation_policy
    genetic_manipulation_policy = Policy(
        name = "Genetic Experimentation License",
        cost = 100000,
        desc = "Unlock full genetic sequencing of human DNA for cloning purposes, the military is very interested in this technology.\nRequires research Tier 3 unlocked and a cloning facility.",
        requirement = genetic_manipulation_policy_requirement,
        on_buy_function = unlock_genetic_manipulation,
    )
    global topless_legal_policy
    topless_legal_policy = Policy(name = "City Laws: Legalize topless outfits",
        desc = "Use your connections with various city officials to lobby for toplessness to be made legal regardless of gender.",
        cost = 75000,
        requirement = topless_legal_requirement,
        on_buy_function = topless_legal_unlock,
        extra_arguments = {"unlock": True})
    # just a policy for now until we have a story to go with it
    global nudity_legal_policy
    nudity_legal_policy = Policy(name = "City Laws: Legalize public nudity",
        desc = "You connections with various city officials allow nudity to be legal.",
        cost = 75000,
        own_requirement = topless_legal_policy,
        requirement = topless_legal_requirement,
        on_buy_function = nudity_legal_unlock,
        extra_arguments = {"unlock": True})
    
    global public_sex_act_legal_policy
    public_sex_act_legal_policy = Policy(name = "City Laws: Legalize public sexual acts",
        desc = "You connections with various city officials allow you to legalize minor sexual acts in public.",
        cost = 75000,
        own_requirement = nudity_legal_policy,
        requirement = public_sex_act_legal_requirement,
        on_buy_function = public_sex_act_legal_unlock,
        extra_arguments = {"unlock": True})
    
    global public_sex_legal_policy
    public_sex_legal_policy = Policy(name = "City Laws: Legalize public sex",
        desc = "You connections with various city officials allow you to legalize hardcore sex acts in public.",
        cost = 75000,
        own_requirement = public_sex_act_legal_policy,
        requirement = public_sex_legal_requirement,
        on_buy_function = public_sex_legal_unlock,
        extra_arguments = {"unlock": True})

    global special_policies_list
    special_policies_list.extend((
        HR_director_creation_policy,
        personal_secretary_creation_policy,
        production_assistant_creation_policy,
        it_director_creation_policy,
        testing_room_creation_policy,
        unisex_bathroom_creation_policy,
        topless_legal_policy,
        nudity_legal_policy,
        public_sex_act_legal_policy,
        public_sex_legal_policy,
        genetic_modification_policy,
        genetic_manipulation_policy,
    ))
