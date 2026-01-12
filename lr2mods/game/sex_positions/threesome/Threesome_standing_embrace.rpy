transform Threesome_standing_embrace_girl_one_transform():
    yalign 0.5
    yanchor 0.5
    xalign 1.0
    xanchor 1.0
    zoom 1.0


transform Threesome_standing_embrace_girl_two_transform():
    yalign 0.5
    yanchor 0.5
    xalign 1.0
    xanchor 1.0
    zoom 1.0

label intro_threesome_standing_embrace_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    "You stand back for a moment as the girls grab each other and start to make out. Their hands begin to roam all over each other's bodies."
    "You give yourself a couple strokes as you watch."
    the_girl_1 "Mmm, come on [the_girl_1.mc_title]."
    the_girl_2 "I'm ready for you!"
    if not the_girl_2.vagina_visible:
        "[the_girl_2.title] quickly moves some clothing out of the way..."
        $ the_girl_2.strip_to_vagina(position = Threesome_standing_embrace.position_two_tag, display_transform = Threesome_standing_embrace.p2_transform, prefer_half_off = True)

    "You step up behind [the_girl_2.possessive_title]. She arches her back a bit to give you easier access."
    $ the_girl_2.break_taboo("vaginal_sex")
    $ the_girl_2.break_taboo("condomless_sex")
    "With one smooth stroke you push yourself inside her, she moans as you begin to fuck her."
    return

label scene_threesome_standing_embrace_fuck_girl_two_1(the_girl_1, the_girl_2, the_location, the_object):
    "Your hips are slapping up against [the_girl_2.title]'s rear as you fuck her."
    "Around her you can see [the_girl_1.possessive_title] kissing her neck as she closes her eyes and enjoys the sensations."
    the_girl_2 "Mmm, your bodies feel so good."
    "You thrust deep inside her and keep it there. You start to kiss the opposite side of [the_girl_2.possessive_title]'s neck."
    "[the_girl_1.title] is pinching and pulling at her nipples. You use one hand to grope her ass cheeks as you grind deep inside her."
    "[the_girl_2.possessive_title!c] is arching her back hard as the sensations overwhelm her. She reaches back with one hand and runs it through your hair, while sensually touching [the_girl_1.title]'s lips with her other hand."
    return

label scene_threesome_standing_embrace_fuck_girl_two_2(the_girl_1, the_girl_2, the_location, the_object):
    "You grab [the_girl_2.possessive_title]'s leg and lift it a bit, allowing for deeper penetration."
    "The change of angle feels great and you enjoy the steamy wet grip of her cunt."
    "[the_girl_1.possessive_title!c] and [the_girl_2.title] both have their hands between each other's legs. You can feel [the_girl_1.title]'s hand moving circles around the hole you are fucking."
    "Her hand drops a little lower and is now cupping your balls. You push yourself deep into [the_girl_2.title] and grind your hips a bit, enjoying the sensation."
    the_girl_1 "Mmm, your balls are so full, [the_girl_1.mc_title]. I bet you're gonna fill her up, aren't you?"
    "[the_girl_2.title] just moans at all the intense sensations she is feeling."
    return

label outro_threesome_standing_embrace_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_2.possessive_title!c]'s sweet cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl_2.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    menu:
        "Cum inside her":
            if mc.condom:
                "You pull back on [the_girl_2.possessive_title]'s hips and drive your cock deep inside her as you cum. She gasps when she feels you filling the condom deep inside her."
                "You wait until your orgasm has passed completely, then pull out and stand back. Your condom is bulged on the end where it is filled with your seed."
                "[the_girl_1.possessive_title!c] reaches down for your cock, removes the condom, and ties the end in a knot for you."
                the_girl_1 "Damn that was hot... is it my turn next?"
                return
            "You pull back on [the_girl_2.possessive_title]'s hips and drive your cock deep inside her as you cum. She gasps softly in time with each new shot of hot semen inside her."
            if the_girl_2.wants_creampie:
                the_girl_2 "Yes! Fill me up with your cum!"
            if the_girl_2.opinion.bareback_sex > 0:
                the_girl_2 "I love it when you shoot your seed so deep!"
            $ the_girl_2.cum_in_vagina()
            $ scene_manager.draw_scene()
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl_2)
            the_girl_1 "Damn that was hot... is it my turn next?"

        "Cum on her ass":
            if mc.condom:
                "You pull out of [the_girl_2.possessive_title] at the last moment, pulling your condom off as you blow your load all over her ass."
                "She holds still for you as you cover her with your sperm."
            else:
                "You pull out of [the_girl_2.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She wiggles her ass for you as you cover her with your sperm."
            if the_girl_2.opinion.being_covered_in_cum > 0:
                the_girl_2 "Yes! Paint me with your sticky cum!"
            $ the_girl_2.cum_on_ass()
            $ scene_manager.draw_scene()
            $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_girl_2)
            if the_girl_2.opinion.showing_her_ass > 0:
                "[the_girl_2.possessive_title!c] bends over and presents her cum-covered ass to you."
                "She gives her hips a few enticing wiggles as your cum starts to drip down the back of her legs."
            "[the_girl_1.title] spanks [the_girl_2.possessive_title], then gropes her and starts to rub your cum into her cheeks."
            "She brings her fingers up to her mouth and begins to lick them off."
            the_girl_1 "Damn that was hot... is it my turn next?"
    return

label strip_threesome_standing_embrace_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label strip_ask_threesome_standing_embrace_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    "This is just a test to see if this position is working."
    "This is the ask Strip Scene!"
    return

label orgasm_threesome_standing_embrace_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        $ play_moan_sound()
        "Both girls are moaning aggressively into each other's mouths as they make out. [the_girl_2.title] has her fingers vigorously working [the_girl_1.possessive_title]'s slit."
        $ the_girl_2.call_dialogue("climax_responses_vaginal")
        $ Threesome_standing_embrace.have_orgasm(the_girl_2)
        "You can feel [the_girl_2.possessive_title]'s legs buckle for a second as she starts to cum. You grab her hips and hold them firmly in place while you fuck her."
        $ Threesome_standing_embrace.have_orgasm(the_girl_1)
        "[the_girl_2.title]'s cunt squeezes your cock as she cums, while [the_girl_1.title] moans and closes her eyes as she cums at the same time."
        "As they start to wind down, you continue fucking [the_girl_2.title]'s now considerably more slick pussy."
        return

    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        $ play_moan_sound()
        "[the_girl_1.title] is moaning loudly as [the_girl_2.possessive_title]'s fingers work her cunt and she kisses and licks at her breasts."
        the_girl_1 "Oh fuck! Yes!!!"
        $ Threesome_standing_embrace.have_orgasm(the_girl_1)
        "She orgasms, her moans reaching a fevered pitch."
        "As [the_girl_1.title] comes down from her orgasm you continue your relentless fucking of [the_girl_2.possessive_title]."
        return

    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        $ play_moan_sound()
        "[the_girl_2.title] moans loud as you and [the_girl_1.possessive_title] pleasure her."
        "[the_girl_1.title] is holding [the_girl_2.possessive_title]'s leg up at an angle while she sucks eagerly on her nipples."
        $ the_girl_2.call_dialogue("climax_responses_vaginal")
        $ Threesome_standing_embrace.have_orgasm(the_girl_1)
        "The stimulation is overwhelming and she cums. Her legs start to buckle but you and [the_girl_1.title] hold her up as she orgasms."
        "As she starts to wind down, you continue fucking [the_girl_2.title]'s now considerably more slick pussy."
    return


label swap_threesome_standing_embrace_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "As the girls make out with each other, you step up behind [the_girl_2.possessive_title]. She arches her back a bit to give you easier access."
    $ the_girl_2.break_taboo("vaginal_sex")
    $ the_girl_2.break_taboo("condomless_sex")
    "With one smooth stroke you push yourself inside her, she moans as you begin to fuck her."
    return
