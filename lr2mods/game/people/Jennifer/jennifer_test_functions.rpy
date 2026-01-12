#Use this to test new jennifer related events.
#Note, every function in this file will break existing save games and states.


label test_family_game_night():
    $ loop_test = True
    $ mc.change_location(kitchen)
    $ lily.change_location(lily_bedroom)
    python:
        mc.business.event_triggers_dict["family_games_drink"] = 0
        mc.business.event_triggers_dict["family_games_cards"] = 0
        mc.business.event_triggers_dict["family_games_fun"] = 0
        mc.business.event_triggers_dict["family_games_cash"] = 1
        mc.business.event_triggers_dict["family_games_strip"] = 0
        mc.business.event_triggers_dict["family_games_setup_complete"] = True
    "This test loops family game night, incrementing sluttiness of each participant by 5 each time."
    while loop_test:
        $ aunt.change_energy(100)
        $ mom.change_energy(100)
        $ lily.change_energy(100)
        $ mc.change_energy(200)
        "Loop game night?"
        menu:
            "Yes":
                call family_games_night_start(aunt, mom) from _game_night_test_function_01
                $ aunt.change_slut(5, 100)
                $ mom.change_slut(5, 100)
                $ lily.change_slut(5, 100)
            "No":
                $ loop_test = False
            "Other":
                "What setting?"
                menu:
                    "Everyone loves drinking cum":
                        $ aunt.set_opinion("drinking cum", 2, True)
                        $ mom.set_opinion("drinking cum", 2, True)
                        $ lily.set_opinion("drinking cum", 2, True)
                    "Everyone loves showing tits":
                        $ aunt.set_opinion("showing her tits", 2, True)
                        $ mom.set_opinion("showing her tits", 2, True)
                        $ lily.set_opinion("showing her tits", 2, True)
    "Loop test Complete"
    return

label test_mom_underwear_crisis():
    $ loop_test = True
    "This test loops [mom.title] asking for assistance with her underwear on a loop."
    "By default it will run multiple times, each time increasing sluttiness by 10."
    $ end_mom_kissing_taboo_quests()
    while loop_test:
        $ mom.change_energy(100)
        $ lily.change_energy(100)
        $ mc.change_energy(200)
        "Loop outfit crisis?"
        menu:
            "Yes":
                call mom_outfit_help_crisis_label() from _test_function_mom_outfit_help_crisis_label_01
                $ mom.change_slut(10, 100)
            "No":
                $ loop_test = False
            "Other":
                call test_mom_modify() from _test_mom_modify_01

label test_mom_anal_taboo_revisit():
    $ mc.business.change_funds(25000)
    $ end_mom_kissing_taboo_quests()
    $ end_mom_oral_taboo_quest()
    $ mom.break_taboo("anal_sex")
    $ mom.change_slut(75, 75)
    call mom_anal_taboo_break_revisit(mom) from mom_anal_taboo_revisit
    return

label test_mom_modify():    #Ues this label to make generic changes to jennifer for testing purposes.
    $ loop_modify = True
    while loop_modify:
        menu:
            "Obedience":
                menu:
                    "Add 10 Obedience":
                        $ mom.change_obedience(10)
                    "Subtract 10 Obedience":
                        $ mom.change_obedience(-10)
                    "Max Obedience":
                        $ mom.obedience = 300
                    "Min Obedience":
                        $ mom.obedience = 50
                    "Moderate Obedience":
                        $ mom.obedience = 150
            "Love":
                menu:
                    "Add 10 love":
                        $ mom.change_love(10)
                    "Subtract 10 love":
                        $ mom.change_love(-10)
                    "Max love":
                        $ mom.love = 100
                    "Min love":
                        $ mom.love = -100
                    "Neutral love":
                        $ mom.love = 0
            "Sluttiness":
                menu:
                    "Add 10 slut":
                        $ mom.change_slut(10, 100)
                    "Subtract 10 slut":
                        $ mom.change_slut(-10, 100)
                    "Max slut":
                        $ mom.change_slut(100, 100)
                    "Min slut":
                        $ mom.change_slut(-100, 100)
                    "Neutral slut":
                        $ mom.change_slut(-200, 100)
                        $ mom.change_slut(200, 40)
            "Complete taboo quest":
                menu:
                    "Foreplay Taboo":
                        $ end_mom_kissing_taboo_quests()
                    "Oral Taboo":
                        $ end_mom_oral_taboo_quest()
                    "Anal Taboo":
                        $ end_mom_anal_taboo_quest()
                    "Vaginal Taboo":
                        $ end_mom_vaginal_taboo_quest()
            "Finished":
                $ loop_modify = False
    $ del loop_modify
    return
