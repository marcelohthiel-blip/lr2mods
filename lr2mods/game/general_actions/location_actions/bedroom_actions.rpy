label bedroom_masturbation(location_description = "home", edging_available = True, should_advance_time = True): #Baseline efficiency for masturbating. Advances time, consumes energy, and releases Clarity inefficiently.
    if location_description == "home":
        "You sit down in front of your computer and start to look around for some porn to jerk off to."

    if mc.masturbation_novelty >= 95:
        "You have the entire internet's worth of porn at your fingertips, so it's not long before you're stroking your cock to some new porn."
    elif mc.masturbation_novelty >= 75:
        "You browse the internet for something hot to watch. After a few minutes you've found enough to entertain you and start to stroke your cock."
    elif mc.masturbation_novelty >= 60:
        "You browse the internet, but it's getting hard to find good porn you haven't seen before."
        "Soon you're searching one-handed as you bounce from side to side, stroking yourself to keep hard until you find that perfect video to finish to."
    else:
        "You browse the internet, but it feels as if you've seen it all before."
        "Nothing new interests you, so you pull up some old favourites and jerk off to those instead."

    menu:
        "Jerk off and cum":
            "You enjoy stroking yourself off for a long while."
            $ mc.change_locked_clarity(10)
            "Eventually you can feel the edge of your orgasm and push yourself towards it."
            $ climax_controller = ClimaxController(["Cum!", "masturbation"])
            $ climax_controller.show_climax_menu()
            $ climax_controller.do_clarity_release()
            "You grab desperately at some tissue as you start to cum, smothering your tip to avoid making a mess."

            "You take a few deep breaths as your climax passes, then wad up the spent tissues and chuck them into the trash."

        "Try and edge yourself" if edging_available:
            "You enjoy stroking yourself off for a long while."
            $ mc.change_locked_clarity(10)
            if renpy.random.randint(0,100) < 15*mc.focus + 10:
                # You manage to avoid climaxing
                "For a long while you edge yourself, pushing yourself to the edge of your orgasm and then slowing down."
                $ mc.change_locked_clarity(10)
                "It takes focus and willpower, but you're able to avoid making yourself cum. You feel like a dam ready to burst now."
                "You put your cock away, excited about the release you'll experience next time you climax."
            else:
                "For a long while you edge yourself, pushing yourself right to the edge of your climax before slowing down."
                "It only takes a momentary lapse of willpower for it all to fall apart. An unexpected jiggle set of internet tits and you're suddenly past the point of no return."
                $ climax_controller = ClimaxController(["Cum!", "masturbation"])
                $ climax_controller.show_climax_menu()
                "You grab desperately at some tissue as you start to cum, smothering your tip to avoid making a mess."
                $ climax_controller.do_clarity_release()
                "You take a few deep breaths as your climax passes, then wad up the spent tissues and chuck them into the trash."

    if should_advance_time:
        call advance_time() from _call_advance_time_bedroom_masturbation
    return
