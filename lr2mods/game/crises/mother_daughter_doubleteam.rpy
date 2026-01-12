## Mother Daughter Double Team
init 10 python:
    def mother_daughter_doubleteam_requirement():
        if mc.business.is_open_for_business and mc.is_at_office:
            return any(
                rel for rel in town_relationships.get_business_relationships(["Mother"])
                    if rel.person_a.is_at_office and rel.person_b.is_at_office
                        and willing_to_threesome(rel.person_a, rel.person_b)
            )
        return False

    def get_mother_with_daughter_for_doubleteam():
        mother_daughter = get_random_from_list(
            [
                (rel.person_b, rel.person_a) for rel in town_relationships.get_business_relationships(["Mother"])
                    if rel.person_a.is_at_office and rel.person_b.is_at_office
                        and willing_to_threesome(rel.person_a, rel.person_b)
            ]
        )

        if mother_daughter:
            return mother_daughter
        return (None, None)

    mother_daughter_doubleteam_action = ActionMod("Mother Daughter Blowjob", mother_daughter_doubleteam_requirement, "mother_daughter_doubleteam_action_label",
        menu_tooltip = "A mother and daughter compete to give a better blowjob.", category = "Business", is_crisis = True)

label mother_daughter_doubleteam_action_label():
    python:
        (the_mother, the_daughter) = get_mother_with_daughter_for_doubleteam()
        if not the_mother or not the_daughter:
            renpy.return_statement()
        # check if mom and daughter got swapped
        if town_relationships.get_existing_mother(the_mother) == the_daughter:
            the_mother, the_daughter = the_daughter, the_mother

        mc.change_location(break_room)

        scene_manager = Scene() # make sure we have a clean scene manager

    "As you are walking around the office, you hear some arguing coming from the break room."
    "When you look inside, you see [the_mother.possessive_title] having a discussion with her daughter."
    $ scene_manager.add_actor(the_mother)
    $ scene_manager.add_actor(the_daughter, display_transform = character_center_flipped)
    the_daughter "I know, I know, dad always said you were good in bed. I'm not disputing that! I'm just saying I'm pretty good at giving blowjobs and I might even be better than you..."
    the_mother "Honey, blowjobs are an art that takes {i}years{/i} to master. I understand that you have enthusiasm, but that doesn't make up for practised technique."
    the_daughter "What makes you think I don't have practice? Oh! Hey [the_daughter.mc_title]."
    $ mc.change_locked_clarity(10)
    "They both look at you as you walk into the break room."
    the_mother "Hey [the_mother.mc_title], maybe you could help us settle something. In your experience, who gives better blowjobs, enthusiastic, younger girls or experienced older women?"
    "Oh boy, you walked into a hornet's nest."
    mc.name "Well, to be honest I've had both that were amazing, it really just depends on the situation."
    the_daughter "See [the_mother.fname]? It's totally plausible I'm just as good, if not better than you."
    the_mother "I suppose, but, I really feel like you are underestimating your mother here dear."
    mc.name "Why don't you two just find some hapless guy at the bar tonight? You can both blow him and then find out who he thinks is better?"
    the_daughter "That's a good idea! Except... I mean some random guy? He may not be experienced or have a clue."
    the_mother "That {i}is{/i} a good idea [the_daughter.mc_title], except we need someone with a bit more experience... like say... you!"
    $ mc.change_locked_clarity(20)
    the_daughter "Hey! There we go! [the_daughter.mc_title], you should let us blow you and decide who is better!"
    "Hmmm, you wonder. Maybe you could talk them into doing it at the same time? It would be easier to judge technique if they were both on their knees in front of you..."
    menu:
        "Let's settle this right now":
            mc.name "I have one condition though. Why don't you both go at the same time, that way I can go back and forth and make up my mind easier."
            $ mc.change_locked_clarity(20)
            the_daughter "Yes! Let's do it [the_mother.fname]! Loser has to cook dinner tonight!"
            the_mother "Okay, let's do it!"
            mc.name "Let's go to my office for some privacy."
            $ mc.change_location(ceo_office)
            "As soon as mother and daughter get to your office, they drop to their knees, giving you a burst of anticipation energy. A competitive blowjob. This should be fun!"
            python:
                mc.change_energy(50)
                the_mother.change_energy(50)
                the_daughter.change_energy(50)
            call start_threesome(the_mother, the_daughter, start_position = threesome_double_blowjob, private = True, position_locked = True, affair_ask_after = False) from mother_daughter_teamup_call1
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0:
                "You sigh happily after you finish receiving your double blowjob from the girls. For a moment, you forgot that it was a competition."
            else:
                "You decide who you think is the better oral giver, so you pull back to deliver the news."

            "As the both stand up, they look at you expectantly."
            $ scene_manager.update_actor(the_mother, position = "default", display_transform = character_right)
            $ scene_manager.update_actor(the_daughter, position = "default", display_transform = character_center_flipped)
            the_daughter "So? How'd I do? Who do you think is better at giving blowjobs?"
            menu:
                "[the_mother.fname]":
                    "[the_daughter.fname] is disappointed, but she quickly smiles."
                    the_daughter "I see. Well, I guess I'm making dinner tonight mom. But we should revisit this in the future, I bet with a bit more practice, this might go differently."
                "[the_daughter.fname]":
                    "[the_mother.fname] is stunned by your verdict."
                    the_mother "That... I can't believe it. Have I let myself get comfortable after all these years? Maybe I should practice more."
                    the_mother "Alright, I'll make dinner tonight, but this isn't over girl! We'll revisit this another time!"
            $ scene_manager.update_actor(the_mother, position = "walking_away", display_transform = character_right)
            $ scene_manager.update_actor(the_daughter, position = "walking_away", display_transform = character_center_flipped)
            "The two girls walk out of your office, the competition settled... for now..."
        "Too busy":
            mc.name "I'm sorry, I have a lot on my to-do list right now. Perhaps another time."
            the_daughter "Oof. Okay, maybe we're both bad if [the_daughter.mc_title] won't even accept a free blowjob from us [the_mother.fname]?"
            the_mother "That's... no, I'm sure he's just busy honey."
            $ scene_manager.update_actor(the_mother, position = "walking_away")
            $ scene_manager.update_actor(the_daughter, position = "walking_away")
            "The two girls walk out of the break room, still discussing their issue."
            $ mc.change_location(lobby)

    python:
        scene_manager.clear_scene()
        # Release variables
        del the_mother
        del the_daughter
    return
