
label stephanie_bar_date_pong_label():
    $ the_person = stephanie
    $ mc_distraction = False
    $ date_distraction = False
    $ game_check = bar_date_skills_pong(the_person) # returns [int(advantage), int(result)]
    $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
    "This is a test. [the_person.title]'s unique override is working!"
    "You and [the_person.possessive_title] step over to one of the beer pong tables."
    "After pouring in the drinks and racking the cups, you being taking turns throwing the ping pong ball."
    if game_check[0] >= 0:  #MC advantage
        "You jump out to an early, leaving [the_person.title] trying to catch up."
        if bar_date_game_distraction_check(the_person, distraction_level = 1):
            if the_person.tits_visible: #Already out, so she taunts MC with them.
                the_person "Hey [the_person.mc_title], check this out!"
                $ the_person.draw_person(position = "kneeling1", display_transform = character_center_flipped(zoom = 0.9))
                "[the_person.possessive_title!c] leans over the side of the table, and shakes her chest back and forth for a moment."
            else:
                the_person "Hey [the_person.mc_title], look at this!"
                $ the_person.strip_to_tits(prefer_half_off = True)
                $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
                "[the_person.possessive_title!c] flashes her tits at you, giving them a good shake before restoring her clothing."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
            $ date_distraction = True
            $ mc.change_locked_clarity(40)
            $ the_person.change_arousal(10)
            $ game_check[1] += (-4)
            "Her distraction causes you to miss your next shot."
        if game_check[1] >= 0:  #mc wins
            if date_distraction:
                "However, despite the distraction, your lead is insurmountable."
            else:
                "She manages to string together a few good shots, but your lead turns out to be insurmountable."
            $ the_person.call_dialogue("activity_pong_response", mc_won = True)
            $ the_person.increase_drink_level(1)
            "[the_person.title] quickly finishes her drink."
            return True
        else:
            if date_distraction:
                "The distraction proves to be enough to get her in the lead, and somehow she accomplishes an impossible comeback."
            else:
                "Despite your early lead, she manages to string together several in a row, winning her the game."
            $ the_person.call_dialogue("activity_pong_response", mc_won = False)
    else:
        "[the_person.possessive_title!c] jumps out to an early lead."
        "You give it your best shot, managing to string together a few good shots here and there."
        if game_check[1] >= 0:  #mc wins
            "Somehow, you manage to string together several in a row, winning you the game, despite your slow start."
            $ the_person.call_dialogue("activity_pong_response", mc_won = True)
            $ the_person.increase_drink_level(1)
            "[the_person.title] quickly finishes her drink."
            return 1
        else:
            "You never manage to catch up with her though, and soon she sinks her final shot in victory."
            $ the_person.call_dialogue("activity_pong_response", mc_won = False)
    return False

label stephanie_bar_group_date_trivia_label(the_group):
    #OUTLINE
    "This is a test. [stephanie.title]'s unique override is working!"
    "In this label we do trivia with the girls."
    return False

label stephanie_date_take_home_her_place(date_type = None):
    # Proof of concept
    python:
        the_person = stephanie
        if not the_person.mc_knows_address:
            the_person.learn_home()
        mc.change_location(the_person.home)
        the_person.change_location(the_person.home)
        the_person.add_situational_slut("Romanced", 15, "What a wonderful date!")
        # in this case Ashley (if not moved to Harem)
        the_other_person = get_random_from_list(the_person.living_with)

    if the_other_person:
        the_person "[the_other_person.name] will be there, but we could sneak in and be quiet."

        "You and [the_person.possessive_title] step inside quietly, being careful not to make too much noise going back to her room."
        $ the_person.change_to_bedroom()
    else:
        "You and [the_person.possessive_title] step inside."
        "She doesn't leave any pretenses, leading you straight to her bedroom."
        $ the_person.change_to_bedroom()
        "She closes her door and locks it."
    if the_person.is_willing(blowjob):
        the_person "Mmm, finally got you all to myself. Let's get these pants off you!"
        $ the_person.draw_person(position = "blowjob")
        "She gets down on her knees and tugs at your pants. You let her pull them off you while you take off your shirt."
        "She smiles when your cock springs free."
        the_person "Mmmm, the things this cock has done to me..."
        "She opens her mouth and slides your erection past her lips into her hot mouth."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(5)
        "[the_person.possessive_title!c] slowly bobs her head up and down your manhood a few times, then pulls off."
        the_person "Fuck you're so hard. Alright..."
        $ the_person.draw_person(position = the_person.idle_pose)
        "She stands up and gets naked."

    else:
        "[the_person.possessive_title!c] reaches down and starts to stroke your cock through your pants."
        the_person "Let's get these pants off you..."
        "She reaches down and starts to pull of your pants. You let her pull them off while you take off your shirt."
        "She smiles when your cock springs free."
        the_person "Fuck, it's so big..."
        "She gives your manhood a few gentle strokes."
        $ the_person.break_taboo("touching_penis")
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(5)
        the_person "And so hard too. Alright..."
        "She starts to get naked."
    $ the_person.strip_to_tits()
    the_person "Let's just get all these pesky clothes out of the way..."
    $ the_person.strip_to_vagina()
    "Once naked, she looks at you, waiting for you to make the next move."
    call fuck_person(the_person, private = True) from _call_fuck_person_steph_one_night_stand
    $ the_person.call_dialogue("sex_review", the_report = _return)
    "Finished, you look around and start collecting your clothes."
    $ the_person.draw_person(position = "missionary")
    "As you get dressed, [the_person.title] flops down on her bed, exhausted."
    call check_date_trance(the_person) from _call_check_date_trance_stephanie_date_take_home_her_place
    if the_other_person:
        the_person "Hey, can you let yourself out quietly? Remember [the_other_person.fname] is probably around..."
    else:
        the_person "I'm beat... can you let yourself out?"
    mc.name "Sure. Take care [the_person.title]."
    the_person "You too!"
    $ the_person.clear_situational_slut("Romanced")
    $ clear_scene()
    if the_other_person:
        if the_other_person.effective_sluttiness() >= 30:
            $ the_other_person.change_to_hallway()
            "You quietly exit [the_person.title]'s room and into the hallway, being as quiet as possible."
            "However, as you pass the bathroom, the door opens and out steps [the_other_person.possessive_title]."
            $ the_other_person.draw_person(emotion = "happy")
            the_other_person "Oh!"
            "She is surprised, but quickly gives you a smile and a thumbs up."
            "She is quiet, and whispers to you."
            the_other_person "[the_person.name] let you get your dick wet?"
            mc.name "Yeah... something like that..."
            the_other_person "Nice. Have a good night."
            $ clear_scene()
            "You pass by her and continue on your way out."

    "You step out of [the_person.possessive_title]'s place and head home."
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_steph_overnight_01
    return
