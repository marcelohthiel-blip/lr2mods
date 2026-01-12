from __future__ import annotations
from game.map.map_code_ren import gaming_cafe_is_open
from game.sex_positions._position_definitions_ren import standing_doggy, reverse_cowgirl, prone_bone, cowgirl, against_wall, missionary, doggy
from game.major_game_classes.game_logic.Room_ren import gaming_cafe
from game.major_game_classes.game_logic.RoomObject_factories_ren import make_couch, make_wall
from game.major_game_classes.character_related.Person_ren import Person, mc, myra
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.serum_related.serums._serum_traits_T2_ren import breast_enhancement
from game.people.Myrabelle.myra_role_definition_ren import myra_at_cafe, myra_lewd_game_fuck_avail, myra_wants_bigger_tits
from game.people.Myrabelle.myra_focus_training_definition_ren import myra_focus_progression_scene

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

myra_random_positions = [standing_doggy, reverse_cowgirl, prone_bone, cowgirl, against_wall, missionary, doggy]
myra_random_positions_desc = {
    standing_doggy.name: "The computer screen shows the male sim bend the female over the bed and penetrate her from behind.",
    reverse_cowgirl.name: "On screen, the male sim lays down and the female gets on top of him, riding him reverse cowgirl.",
    prone_bone.name: "The male sim aggressively pushes the female face down on the bed.",
    cowgirl.name: "After the male sim lays down, the female gets on top and mounts him cowgirl style.",
    against_wall.name: "The male sim picks up the female and pushes her up against the wall.",
    missionary.name: "The female sim lays down and spreads her legs, and the male sim gets on top of her.",
    doggy.name: "The female sim gets on her hands and knees on the bed, and the male gets behind her."
}

myra_random_positions_intro = {
    standing_doggy.name: "She turns and you quickly bend her over the couch. You grab her hips and line yourself up, pushing inside her.",
    reverse_cowgirl.name: "You lay down on the couch. She climbs on top of you, and you admire the amazing view as she reaches between her legs, grabs your cock, lines it up, and sinks down onto you.",
    prone_bone.name: "You grab her and shove her down on the couch. You pin her down with your weight, and it takes a couple seconds of poking around until your cock finds her wet cunt and pushes in.",
    cowgirl.name: "You lay down and she gets on top of you. She grabs your cock and lines it up, then moans as she lets herself sink down onto your cock.",
    against_wall.name: "She yelps as you pick her up and push her against the wall. Her legs wrap around you as you push into her.",
    missionary.name: "She lays down and spreads her legs. You quickly slide up between them, kissing her on the neck as you easily slide inside her.",
    doggy.name: "She gets on the couch on all fours and shakes her ass as you get behind her. With one hand on her hips and one hand on your cock, you quickly slide inside her."
}

myra_random_positions_cum_inside_desc = {
    standing_doggy.name: "You grab her hips with both hands and fuck her as fast as you can. Her ass quivers with every thrust.",
    reverse_cowgirl.name: "Her quivering hole feels too good. You reach up and grab her hips with both hands, forcing her down on your cock so you can cum deep inside her.",
    prone_bone.name: "She whimpers, your weight pinning her to the couch. You thrust deep as you start to cum inside her.",
    cowgirl.name: "She leans forward, working her hips rapidly as you start to cum inside her.",
    against_wall.name: "As you get ready to cum, her legs wrap around you, pulling you deep as you cum inside her.",
    missionary.name: "Her fingernails scrape your back as you moan and push yourself deep, cumming inside her.",
    doggy.name: "You grab her hips with both hands and fuck her as fast as you can. Her ass quivers with every thrust."
}

myra_random_positions_obj = {
    standing_doggy.name: make_couch(),
    reverse_cowgirl.name: make_couch(),
    prone_bone.name: make_couch(),
    cowgirl.name: make_couch(),
    against_wall.name: make_wall(),
    missionary.name: make_couch(),
    doggy.name: make_couch()
}

#### Love Events ####

def myra_esports_practice_requirement(person: Person):
    return (
        day % 7 < 5
        and person.love >= 20
        and gaming_cafe_is_open()
        and myra.days_since_event("gaming_cafe_open_day") > TIER_2_TIME_DELAY
    )

def add_myra_esports_practice_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra's Esports Aspirations",
            myra_esports_practice_requirement,
            "myra_esports_practice_label",
            priority = 30)
    )
    mc.event_triggers_dict["guild_quest_level"] = 6
    mc.set_event_day("gaming_cafe_grind_day")
    myra.set_event_day("gaming_cafe_open_day")

def myra_esports_first_tournament_requirement():
    return (
        day % 7 == 6
        and myra.love >= 40
        and myra.story_event_ready("love")
        and gaming_cafe_is_open()
    )

def add_myra_esports_first_tournament_action():
    gaming_cafe.add_unique_on_room_enter_event(
        Action("Esports Tournament",
            myra_esports_first_tournament_requirement,
            "myra_esports_first_tournament_label",
            priority = 30)
    )
    myra.event_triggers_dict["knows_plays_esports"] = True
    myra.story_event_log("love")
    add_myra_distracted_gaming_action()

def myra_loses_sponsor_requirement(person: Person):
    return (
        time_of_day == 3
        and person.love >= 60
        and gaming_cafe_is_open()
        and person.days_since_event("myra_fails_tournament") > TIER_3_TIME_DELAY
        and person.is_at(gaming_cafe)
    )

def add_myra_loses_sponsor_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Loses a Sponsor",
            myra_loses_sponsor_requirement,
            "myra_loses_sponsor_label",
            priority = 30)
    )

def myra_gains_sponsor_requirement(person: Person):
    return time_of_day < 3 and mc.business.has_funds(25000) and person.is_at(gaming_cafe)

def add_myra_gains_sponsor_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Gains a Sponsor",
            myra_gains_sponsor_requirement,
            "myra_gains_sponsor_label",
            priority = 30)
    )
    myra.event_triggers_dict["bar_arcade_avail"] = True
    myra.event_triggers_dict["can_sponsor"] = True

def myra_esports_second_tournament_intro_requirement(person: Person):
    return (
        day % 7 < 4
        and person.love >= 80
        and myra.days_since_event("energy_drink_start_research") > TIER_2_TIME_DELAY
        and gaming_cafe_is_open()
        and myra_focus_progression_scene.get_stage() >= 2
        and person.is_at(gaming_cafe)
    )

def add_myra_esports_second_tournament_intro_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Sets Up New Tournament",
            myra_esports_second_tournament_intro_requirement,
            "myra_esports_second_tournament_intro_label",
            priority = 30)
    )
    myra.event_triggers_dict["has_been_sponsored"] = True
    myra.set_event_day("myra_sponsor_day")

def myra_esports_second_tournament_requirement():
    return day % 7 == 6 and gaming_cafe_is_open()

def add_myra_esports_second_tournament_action():
    mc.business.add_mandatory_crisis(
        Action("Myra's Redemption",
            myra_esports_second_tournament_requirement,
            "myra_esports_second_tournament_label",
            priority = 30)
    )

def myra_gaming_cafe_expansion_intro_requirement(person: Person):
    return (
        day % 7 != 6
        and person.love >= 95
        and person.days_since_event("myra_tournament_win_day") > TIER_2_TIME_DELAY
        and gaming_cafe_is_open()
        and person.is_at(gaming_cafe)
    )

def add_myra_gaming_cafe_expansion_intro():
    myra.add_unique_on_room_enter_event(
        Action("Myra Wants to Expand",
            myra_gaming_cafe_expansion_intro_requirement,
            "myra_gaming_cafe_expansion_intro_label",
            priority = 30)
    )
    myra.event_triggers_dict["has_won_tournament"] = True
    myra.set_event_day("myra_tournament_win_day")


#### Lust Events ####


def myra_distracted_gaming_requirement(person: Person):
    return (
        person.sluttiness >= 20
        and person.story_event_ready("slut")
        and person.is_at(gaming_cafe)
    )

def add_myra_distracted_gaming_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Distracts Her Opponents",
            myra_distracted_gaming_requirement,
            "myra_distracted_gaming_label",
            priority = 30)
    )
    myra.story_event_log("slut")

def myra_lewd_gaming_requirement(person: Person):
    return (
        time_of_day == 3
        and person.sluttiness >= 40
        and person.story_event_ready("slut")
        and person.is_at(gaming_cafe)
    )

def add_myra_lewd_gaming_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Plays Lewd Games",
            myra_lewd_gaming_requirement,
            "myra_lewd_gaming_label",
            priority = 30)
    )
    myra.story_event_log("slut")
    myra.event_triggers_dict["distracts_gamers"] = True

def myra_lewd_game_fuck_intro_requirement(person: Person):
    return (
        time_of_day == 3
        and person.sluttiness >= 60
        and person.energy > 70
        and not person.has_taboo("vaginal_sex")
        and person.story_event_ready("slut")
        and person.is_at(gaming_cafe)
    )

def add_myra_lewd_game_fuck_intro_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Game Re-enactment",
            myra_lewd_game_fuck_intro_requirement,
            "myra_lewd_game_fuck_intro_label",
            priority = 30)
    )
    myra.story_event_log("slut")

def myra_lewd_game_fuck_requirement(person: Person):
    if not (myra_lewd_game_fuck_avail() or person.is_at(gaming_cafe)):
        return False
    if time_of_day != 3:
        return "Only in the evening"
    if mc.energy < 50:
        return "You are too tired"
    if person.energy < 50:
        return "She looks too tired"
    return True

def add_myra_lewd_game_fuck_action():
    myra.add_action(
        Action("Lewd Game Re-enactment",
            myra_lewd_game_fuck_requirement,
            "myra_lewd_game_fuck_label",
            priority = 30)
    )
    myra.event_triggers_dict["lewd_game_fuck"] = True
    myra.story_event_log("slut")

def myra_adult_gaming_intro_requirement(person: Person):
    return False # current writing spot, event is disabled
    # return (
    #     person.sluttiness >= 80
    #     and person.energy > 50
    #     and person.story_event_ready("slut")
    #     and myra_is_expanding_business()
    #     and person.is_at(gaming_cafe)
    # )

def add_myra_adult_gaming_intro_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Wants Lewd Café",
            myra_adult_gaming_intro_requirement,
            "myra_adult_gaming_intro_label",
            priority = 30)
    )
    myra.story_event_log("slut")

def myra_adult_gaming_opening_requirement():
    return (
        myra.days_since_event("adult_cafe_opening_day") >= TIER_3_TIME_DELAY
        and myra.is_at(gaming_cafe)
    )

def add_myra_adult_gaming_opening_action():
    mc.business.add_mandatory_crisis(
        Action("Myra Opens Lewd Café",
        myra_adult_gaming_opening_requirement,
        "myra_adult_gaming_opening_label",
        priority = 30)
    )
    myra.set_event_day("adult_cafe_opening_day")

def myra_harem_entry_requirement(person: Person):
    return False

def add_myra_harem_entry_action():
    myra.add_unique_on_room_enter_event(
        Action("Harem: Myra",
            myra_harem_entry_requirement,
            "myra_harem_entry_label",
            priority = 30)
    )
    myra.event_triggers_dict["lewd_cafe_open"] = True

#### Obedience Events ####

def myra_bigger_tits_intro_requirement(person: Person):
    return (
        person.obedience >= 120
        and myra.days_since_event("myra_bigger_tits_suggestion_day") > 7
        and person.is_at(gaming_cafe)
    )

def add_myra_bigger_tits_intro_action():
    if myra.has_event_day("myra_bigger_tits_suggestion_day"):
        return

    myra.add_unique_on_room_enter_event(
        Action("Myra Wants Bigger Tits",
            myra_bigger_tits_intro_requirement,
            "myra_bigger_tits_intro_label",
            priority = 30)
    )
    myra.set_event_day("myra_bigger_tits_suggestion_day")

def myra_bigger_tits_serum_requirement(person: Person):
    if myra_wants_bigger_tits() and not person.has_large_tits and person.is_at(gaming_cafe):
        if mc.inventory.has_serum_with_trait(breast_enhancement):
            return True
        return "Requires serum with Breast Enhancement Trait"
    return False

def add_myra_bigger_tits_serum_action():
    myra.add_action(
        Action("Give Serum for Bigger Tits",
            myra_bigger_tits_serum_requirement,
            "myra_bigger_tits_serum_label")
    )

def remove_myra_bigger_tits_serum_action():
    myra.remove_action("myra_bigger_tits_serum_label")
    myra.increase_opinion_score("giving tit fucks")
    myra.event_triggers_dict["wants_bigger_tits"] = False

def myra_bigger_tits_final_requirement(person: Person):
    return person.has_large_tits and person.is_at(gaming_cafe)

def add_myra_bigger_tits_final_action():
    myra.add_unique_on_talk_event(
        Action("Myra Gets Large Tits",
            myra_bigger_tits_final_requirement,
            "myra_bigger_tits_final_label")
    )
    myra.event_triggers_dict["wants_bigger_tits"] = True  #This will open up the option on her role

def myra_blowjob_training_intro_requirement(person: Person):
    return (
        person.obedience >= 140
        and person.opinion.giving_blowjobs > -2
        and person.story_event_ready("obedience")
        and person.event_triggers_dict.get("can_train_focus", False)
        and person.is_at(gaming_cafe)
    )

def add_myra_blowjob_training_intro_action():
    myra.add_unique_on_room_enter_event(
        Action("Myra Needs Help",
            myra_blowjob_training_intro_requirement,
            "myra_blowjob_training_intro_label",
            priority = 30)
    )
    myra.event_triggers_dict["lewd_game_oral"] = True
    myra.story_event_log("obedience")

def myra_blowjob_training_progress_requirement(person: Person):
    return (
        person.obedience >= 160
        and person.story_event_ready("obedience")
        and person.is_at(gaming_cafe)
    )

def add_myra_blowjob_training_progress_action():
    myra.add_unique_on_room_enter_event(
        Action("Develop Myra Orally",
            myra_blowjob_training_progress_requirement,
            "myra_blowjob_training_progress_label",
            priority = 30)
    )
    myra.increase_opinion_score("giving blowjobs")
    myra.story_event_log("obedience")


def myra_blowjob_training_final_requirement(person: Person):
    return (
        person.obedience >= 180
        and person.story_event_ready("obedience")
        and person.is_at(gaming_cafe)
    )

def add_myra_blowjob_training_final_action():
    myra.add_unique_on_room_enter_event(
        Action("Develop Myra Orally",
            myra_blowjob_training_final_requirement,
            "myra_blowjob_training_final_label",
            priority = 30)
    )
    myra.story_event_log("obedience")

#### Other Events ####
