label intro_against_wall(the_girl, the_location, the_object):
    "You put your arms around [the_girl.title] and spin her around, putting her face towards you and her back against the [the_object.name]."
    $ against_wall.redraw_scene(the_girl)
    if the_girl.effective_sluttiness() > 80:
        "[the_girl.possessive_title!c] plants her back against the [the_object.name] and watches you as you unzip your pants. She bites her lip and sighs under her breath when your cock springs out."
        the_girl "Mmm, what are you going to do to me?"
    else:
        "[the_girl.possessive_title!c] plants her back against the [the_object.name] and waits patiently while you unzip your pants."
    "You get your hard cock out and rub it against [the_girl.title]'s stomach a couple of times, then line up with her pussy. She gasps softly as you slide yourself inside her."
    return

label taboo_break_against_wall(the_girl, the_location, the_object):
    "You put your arms around [the_girl.title] and spin her around, putting her face towards you and her back against the [the_object.name]."
    $ against_wall.redraw_scene(the_girl)
    if the_girl.effective_sluttiness(against_wall.associated_taboo) > against_wall.slut_cap:
        "She reaches down and rubs your hard cock against her, teasing the tip against the slit of her pussy."
    else:
        "You step even closer, letting your hard cock rub against her stomach, a bare few {height_system} above her pussy."
    $ the_girl.call_dialogue(f"{against_wall.associated_taboo}_taboo_break")
    "You hold your shaft and line it up with [the_girl.possessive_title]'s warm cunt. She shivers in anticipation when your tip taps her clit."
    "You put one hand around her waist and pull her towards you as you push yourself forward."
    "After a moment of resistance your cock plunges into her warm, wet pussy."
    the_girl "Ah!"
    "You hold deep inside and let her adjust to your size for a few seconds, then start to glide in and out of her."
    return

label scene_against_wall_1(the_girl, the_location, the_object):
    #CHOICE CONCEPT: Fondle her tits // Kiss her
    if the_girl.arousal_perc > 50:
        "[the_girl.title]'s cunt is nice and wet. You're able to speed up and fuck her a little faster."
    else:
        "[the_girl.title]'s cunt is tight and warm. She's still getting wet, so you take it easy on her."
    menu:
        "Fondle her tits":
            if the_girl.has_large_tits:
                if the_girl.tits_available:
                    "You grab one of [the_girl.possessive_title]'s tits while you fuck her. Her [the_girl.tits]'s more than fill up your hand."
                    "You squeeze her breast and rub your thumb over her nipple a few time. It starts to harden in response."
                else:
                    "You cup one of [the_girl.possessive_title]'s [the_girl.tits]-sized tits and fondle it through her [the_girl.outfit.get_upper_top_layer.display_name]. It's pleasantly soft and heavy in your hand."

                if the_girl.arousal_perc < 50:
                    the_girl "Rub them just like that... Do you like my breasts [the_girl.mc_title]? Do you like my nice, big tits?"
                    mc.name "I love them, you have the most amazing tits."
                else:
                    the_girl "Ah! Go easy on them, they get really sensitive when I'm horny!"

            else:
                if the_girl.tits_available:
                    "You grab one of [the_girl.title]'s tits while you fuck her against the [the_object.name]. Her small [the_girl.tits] cups don't give much to work with, but you enjoy them all the same."
                    "You rub your thumb over her nipple a few times and watch as it starts to harden in response."
                else:
                    "[the_girl.title]'s small [the_girl.tits] cup tits don't give you much to work with, especially not with her [the_girl.outfit.get_upper_top_layer.display_name] in the way, but you run your hand over them anyways."

                if the_girl.arousal_perc < 50:
                    the_girl "Ah... Do you like my breasts [the_girl.mc_title]? I know they're not big, but they're all yours."

                else:
                    the_girl "Oh god, your hands... your cock... it feels so good!"

        "Uncover her tits" if not the_girl.tits_visible:
            "You start to pull off the clothing covering her tits."
            $ the_girl.strip_to_tits(prefer_half_off = True, position = against_wall.position_tag)
            $ the_girl.break_taboo("bare_tits")
            if the_girl.has_large_tits:
                "You grab one of [the_girl.possessive_title]'s tits while you fuck her. Her [the_girl.tits_description] more than fill up your hand."
            else:
                "You grab one of [the_girl.possessive_title]'s tits while you fuck her against the [the_object.name]. Her small [the_girl.tits_description] don't give much to work with, but you enjoy them all the same."
            the_girl "Oh god, [the_girl.mc_title], yes, squeeze my slutty tits."

        "Kiss her":
            "You pin [the_girl.title] against the [the_object.name] with your body and press your lips against hers."
            if the_girl.foreplay_sex_skill > 3: #Experienced kisser
                if the_girl.opinion.kissing > 0:
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.opinion.kissing * 2)
                    "[the_girl.possessive_title!c] shivers with pleasure when your tongues meet. She bucks her hips against yours, suddenly desperate to have you deeper inside her."
                    "You keep pumping your hips, fucking her while you make out."
                elif the_girl.opinion.kissing < -1: #Hates Kissing
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.opinion.kissing * 2)
                    "[the_girl.possessive_title!c] immediately turns her head to the side."
                    the_girl "Ah no kissing... that's kind of a rule for me..."
                else:
                    "[the_girl.possessive_title!c] returns your kiss, darting her tongue out to meet yours."
                    if the_girl.tits_available:
                        "She wraps her arms around you and pulls you against her while you make out. You feel her tits pressed tight against your skin while you fuck her."
                    else:
                        "She wraps her arms around you and pulls you close while you make out. Her body rocks in time with your thrusts."

            else: #Unsure about kissing
                if the_girl.opinion.kissing > 0:
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.opinion.kissing)
                    "[the_girl.possessive_title!c] shivers when your tongue brushes against her lips. She opens her mouth and lets you inside."
                    "[the_girl.title] seems unsure of what to do with her tongue, but she trembles with every touch of yours. She rocks her hips against yours in time with your thrusts."
                    "After a while you break the kiss, leaving her breathing hard."
                    the_girl "Oh my god, my whole body... I didn't know that would feel so good! Don't stop!"
                    "She grabs the back of your head and pulls you back into a long kiss. You divide your attention between making out with [the_girl.title] and pounding her wet pussy."

                elif the_girl.opinion.kissing < 0:
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.opinion.kissing)
                    "[the_girl.possessive_title!c] pulls away and after a brief kiss."
                    the_girl "No kissing. I never know what to do and I like being able to moan."
                    "True to her word she lets out a long, happy sigh while you fuck her against the [the_object.name]."

                else:
                    "[the_girl.title] awkwardly returns your kiss. Her lips barely part when you press your tongue against them."
                    "After a few attempts you give up on making out and focus your attention on pounding her wet pussy."
    return

label scene_against_wall_2(the_girl, the_location, the_object):
    #CHOICE CONCEPT: Fuck her harder // Talk dirty to her
    if the_girl.arousal_perc > 50:
        "You hold [the_girl.title]'s hands while you slide your cock in and out of her pussy. She's wet and obviously turned on."
    else:
        "You hold [the_girl.title]'s hands while you slide your cock in and out of her tight pussy."

    menu:
        "Fuck her harder":
            "You lift [the_girl.possessive_title]'s hands and pin them against the [the_object.name]. You lay into her, fucking her as hard as you can manage."
            if the_girl.is_submissive:
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.opinion.being_submissive)
                the_girl "Yes! Oh my god, yes! Use me however you want, I'll be whatever you want me to be!"
                $ play_moan_sound()
                "She bucks against you with pleasure. You respond by pushing her harder against the [the_object.name], which only makes her moan more loudly."
            else:
                if the_girl.opinion.vaginal_sex < 0:
                    $ the_girl.discover_opinion("vaginal sex")
                    $ the_girl.change_arousal(the_girl.opinion.vaginal_sex)
                    the_girl "Ow, slow down a little. You don't need to fuck me like you're trying to break me, you know."
                    "She pulls her hands out from under yours and uses them to guide your hips at a much more gentle pace."

                else:
                    if the_girl.vaginal_sex_skill > 3:
                        "[the_girl.title] rocks her hips in time with yours to let you get as deep as possible."
                        if the_girl.wants_creampie:
                            the_girl "That's it, fuck me hard you stud. Fuck me and pump that hot load inside me!"

                    else:
                        the_girl "Oh my god! [the_girl.mc_title], you feel so... Oh my god!"
                        "[the_girl.title] doesn't move much, but you're happy to just keep thrusting away at her warm cunt."




        "Talk dirty to her":
            mc.name "Do you like this, you dirty slut? Do you like getting fucked against the [the_object.name]?"
            if the_girl.is_dominant:
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.opinion.being_submissive)
                the_girl "Hey, don't talk like that. Just... Just keep going, okay?"
                "[the_girl.title] seems put off by your comments, but after a little while she's back to rocking her hips against you."

            else:
                if the_girl.sluttiness > 80 or the_girl.is_submissive:
                    the_girl "Mmm, I do... I love feeling your big cock inside me."
                    mc.name "Do you want me to keep fucking you?"

                    if the_girl.opinion.bareback_sex > 0:
                        the_girl "Uh huh! Fuck me until you cum in me! Fuck me like you want to get me pregnant!"

                    elif the_girl.wants_creampie:
                        the_girl "Uh huh! I want you to fuck me until you cum. Pin me against the [the_object.name] and pump your load into me! I want it so badly!"
                    else:
                        the_girl "Uh huh! Please keep fucking me! I want you to fuck me and use me until you cum!"
                else:
                    the_girl "It feels so good... Oh my god [the_girl.mc_title], keep doing that!"

                "You certainly aren't about to disappoint her. You keep thrusting your cock into her warm cunt."

    return

label scene_against_wall_3(the_girl, the_location, the_object):
    # CHOICE CONCEPT: Grab her ass // Let her take control

    "[the_girl.title] thrusts her hips forward to meet yours with each thrust. She closes her eyes and puts her head back against the [the_object.name]."
    menu:
        "Grab her ass":
            "You reach behind [the_girl.possessive_title] and grab her butt. You pull her against you and push yourself as deep as you can manage."
            if the_girl.vaginal_sex_skill > 2:
                the_girl "Oh my god, yes! Keep that cock deep inside me!"
                "[the_girl.title] grabs your head and pulls you into a kiss. She gasps a little with each thrust."

            else:
                the_girl "Oh fuck, go easy on me... it feels like you're tearing me in half when you do that!"
                "You slow down a little bit and let [the_girl.possessive_title] get used to having your cock so deep inside her."

            $ play_spank_sound()
            "You knead her ass cheeks while you fuck her. She lets out a happy yelp when you give them a slap."

        "Let her take control":
            "You stop pumping your cock into [the_girl.title] and let her hips do all the work."
            if the_girl.vaginal_sex_skill < 3 or not the_girl.is_dominant:
                "After a second she stops too and looks at you."
                the_girl "What's wrong?"
                mc.name "Nothing, keep going."
                "[the_girl.title] starts to move her hips. After a few strokes it's obvious that she's having trouble keeping up the rhythm."
                the_girl "Sorry, I'm just not very good at this I guess."
                "You take the lead back and start fucking [the_girl.possessive_title] against the [the_object.name] again."
            else:
                if the_girl.is_dominant:
                    $ the_girl.discover_opinion("taking control")
                    $ the_girl.change_arousal(the_girl.opinion.taking_control)
                    the_girl "Oh, you want me to take care of this all by myself?"
                    "She puts her hands on your waist and grinds herself deeper onto your dick."
                    the_girl "Mmm, it's nice to get you so deep inside me..."
                    if the_girl.wants_creampie:
                        the_girl "Do you think I'll be able to make you cum? I'd love to make you cum inside me."
                        "She pauses for a moment and trembles, then starts fucking you again."
                        the_girl "Oh yeah, I want your hot load deep inside me! I want to feel your dick twitch when I make you climax!"

                else:
                    "[the_girl.possessive_title!c] slows down for a second."
                    the_girl "Is something wrong?"
                    mc.name "No, I just like it when you take over."
                    "She bites her lip, puts her hands on your hips, and speeds up again."
                    the_girl "I'll see what I can do..."


                "[the_girl.possessive_title!c] clearly knows what she's doing. She uses the [the_object.name] behind her to push against you, and each stroke of her warm pussy pulls you closer and closer to climax."
                "You let yourself have a bit of a breather as she clings to you and moves her hips. When she starts to tremble you take back over and thrust again."
                $ mc.change_energy(2)
    return

label scene_against_wall_4(the_girl, the_location, the_object):
    #She begs for mercy / to be fucked harder, based on her vaginal skill.
    if the_girl.arousal_perc > 50:
        "[the_girl.title]'s warm, wet cunt allows you to fuck her hard and fast. It feels so good you feel your hips speeding up all on their own."
    else:
        "[the_girl.title]'s cunt is tight and warm. She's still getting wet, but it feels so good you feel your hips speeding up all on their own."

    if the_girl.vaginal_sex_skill > 2:
        "[the_girl.possessive_title!c]'s leg wraps around your back as you fuck her, urging you deeper and deeper."
        the_girl "Oh fuck, it feels so good! Give it to me harder, [the_girl.mc_title]!"
        menu:
            "Fuck her hard":
                "You aren't about to let an invitation like that go unanswered. You forcefully pin her to the wall then pull all the way out."
                "With one smooth motion, you thrust back into her, her body making a lewd smacking noise."
                "You take your time. You don't go fast, but you {i}do{/i} give it to her hard! Pulling out completely, then shoving it all the way in deep, making her squeal."
                the_girl "That's it! It... OH! It feels so good when... OH!"
                "She can barely get out a full sentence as you fuck her hard."
                $ the_girl.change_arousal(5)
            "Pin her to the [the_object.name]":
                "You lean forward, using your body weight to pin her helplessly to the [the_object.name]."
                mc.name "I'll fuck you how I like, [the_girl.title]."
                "You give her a solid stroke."
                mc.name "It might be hard. It might be slow. But it'll be exactly how I choose."
                if the_girl.is_submissive:
                    "With each sentence, you slam your cock into her."
                    the_girl "Yes... Of course! Use me however you want..."
                    "[the_girl.possessive_title!c] clings to you submissively as you give her several slow, deep thrusts."
                    $ the_girl.change_arousal(5)
                else:
                    "[the_girl.possessive_title!c] bites her lip. She wants to respond, but her vulnerable position forces her to comply."
                    the_girl "Yes... if that is what you want..."
                    $ the_girl.change_obedience(3)
                    "[the_girl.title] seems to be a bit more submissive as you fuck her."


    else:
        "[the_girl.possessive_title!c]'s arm pushes against you slightly as you speed up."
        the_girl "Easy... I can't take it much harder than that..."
        "You are tempted to fuck her harder, just to prove a point, but her voice wavered a bit at the end of her request."
        "You force yourself to slow your hips a bit, just savouring the feeling of being balls deep inside [the_girl.title]."
        "She seems to appreciate it."
        $ the_girl.change_obedience(1)
    return

label outro_against_wall(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. You speed up as you pass the point of no return, pushing her up against the [the_object.name] and laying into her."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Fuck, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her stomach", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside her":
        if mc.condom:
            "You push forward as you climax, thrusting your cock as deep inside [the_girl.possessive_title] as you can manage. She pants quietly as you pulse your hot cum into the condom you're wearing."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "Once your climax has passed you step back and pull your cock out from [the_girl.title]. Your condom is ballooned out, filled with your seed."

            call post_orgasm_condom_routine(the_girl, against_wall) from _call_post_orgasm_condom_routine_against_wall

        else:
            if the_girl.has_cum_fetish or the_girl.has_breeding_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
            else:
                "You push forward as you finally climax, thrusting your cock as deep inside [the_girl.possessive_title] as you can manage. She gasps softly each time your dick pulses and shoots hot cum into her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ against_wall.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "You wait until your orgasm has passed, then step back and sigh happily. [the_girl.title] stays leaning against the [the_object.name] for a few seconds as your semen drips down her leg."

    elif the_choice == "Cum on her stomach":
        if mc.condom == False and (the_girl.has_breeding_fetish or the_girl.wants_creampie): #Leg Lock for internal creampie
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God", "Oh yes", "Oh... OH! Yes"])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            "The strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            if the_girl.vaginal_sex_skill > 3:
                "[the_girl.possessive_title!c] pulls your body close to hers, burying your cock as deep as she can and milks it with the muscles inside her pussy."
                "[the_girl.possessive_title!c]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ against_wall.redraw_scene(the_girl)
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
            if the_girl.has_cum_fetish or the_girl.has_breeding_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "She throws her head back in pleasure."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
            $ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay", "Settle down"])
            $ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
            if the_girl.knows_pregnant:# The personality reactions but should it not be True instead of False?
                the_girl "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"
            elif the_girl.is_infertile:
                the_girl "[wordchoice], [the_girl.mc_title]. I can't get pregnant."
            elif the_girl.on_birth_control:
                the_girl "[wordchoice], [the_girl.mc_title]. I'm on [wordchoice2]."
            elif the_girl.has_significant_other:
                the_girl "[wordchoice], [the_girl.mc_title]. If anything happens I'll tell my [the_girl.so_title] it's his."
            else:
                if the_girl.love > 80:
                    the_girl "I love you, [the_girl.mc_title]. We should make a baby together."
                elif the_girl.love > 0:
                    the_girl "It was too good, [the_girl.mc_title], I just couldn't let you pull out!"
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."
        else:
            $ the_girl.cum_on_stomach()
            $ against_wall.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if mc.condom:
                "You pull out of [the_girl.possessive_title] at the last moment and step back. You whip your condom off and blow your load over her stomach while she watches."
            else:
                "You pull out of [the_girl.possessive_title] at the last moment and step back. You stroke yourself off and blow your load over her stomach while she watches."
            if the_girl.wants_creampie:
                the_girl "What a waste, that would have felt so much better inside me..."
                "She reaches down and runs a finger through the puddles of cum you've put on her, then licks her finger clean and winks at you."
            else:
                the_girl "Oh wow, there's so much of it. It feels so warm..."
            "You sigh contentedly and relax for a moment, enjoying the sight of [the_girl.title] covered in your semen."
    return

label transition_default_against_wall(the_girl, the_location, the_object):
    $ against_wall.redraw_scene(the_girl)
    "You press [the_girl.possessive_title] against the [the_object.name]. She plants her back against it and opens her legs, letting you step between them."
    "You run the tip of your cock along her slit a few times, then slide yourself inside her tight cunt."
    return

label strip_against_wall(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = against_wall.position_tag)
    "[the_girl.possessive_title!c] struggles out of her [the_clothing.name] and drops it beside her."
    return

label strip_ask_against_wall(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = against_wall.position_tag)
            "You slow the pace of your thrusts down while [the_girl.possessive_title] strips out of her [the_clothing.name]. When she drops it beside her you settle back into your rhythm."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 70:
                the_girl "Yeah? Do I look sexy in it?"
                $ play_moan_sound()
                "You fuck her a little faster in response and she moans loudly."
            else:
                the_girl "Yeah? Do I look like a good little slut in it? Because that's what I feel like right now!"
                $ play_moan_sound()
                "You fuck her a little faster and she moans loudly."
            return False

label orgasm_against_wall(the_girl, the_location, the_object):
    "[the_girl.possessive_title!c] closes her eyes and gasps suddenly. Her hands wrap around you, pulling hard, with her nails clawing into your back."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "You push her up against the [the_object.name] and keep fucking her through her orgasm."
    "After a couple of seconds [the_girl.title] opens her eyes again and takes a couple of deep breaths. You slow down your pace and give her a chance to recover."
    the_girl "Keep... keep going and see if you can make me cum again!"
    return

label against_wall_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. Her breathing is getting ragged as she nears her orgasm also."
    the_girl "[the_girl.mc_title], your cock is so good! Pin me to the [the_object.name] and make me cum all over it!"
    "You speed up with her words of encouragement, passing the point of no return. You push her up against the [the_object.name] and lay into her."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Fuck, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her stomach", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside her":
        if the_girl.wants_creampie:
            the_girl "Oh god yes, cum with me [the_girl.mc_title]!"
        if mc.condom:
            $ the_girl.have_orgasm()
            "You push forward as you climax, thrusting your cock as deep inside [the_girl.possessive_title] as you can manage. She wraps her legs around you as she cums in unison."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "Once your climax has passed you keep [the_girl.title] pinned to the [the_object.name] for a little longer. When her aftershocks wind down, she slowly unwraps her legs."
            "You step back and pull out of [the_girl.possessive_title]. Your condom is ballooned out, filled with your seed."

            call post_orgasm_condom_routine(the_girl, against_wall) from _call_post_orgasm_condom_routine_against_wall_double_orgasm

        else:
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans in ecstasy as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                $ the_girl.have_orgasm()
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "Having your cum inside her heightens her orgasm as her fetish for your cum is fulfilled."
            else:
                "You push forward as you finally climax, thrusting your cock as deep inside [the_girl.possessive_title] as you can manage."
                $ the_girl.have_orgasm()
                "She clings to you helplessly as she cums with you in unison."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ against_wall.redraw_scene(the_girl)
            "You wait until your orgasm has passed, then step back and sigh happily. [the_girl.title] stays leaning against the [the_object.name] for a few seconds as your semen drips down her leg."

    elif the_choice == "Cum on her stomach":
        if mc.condom == False and the_girl.wants_creampie and the_girl.obedience <200 :
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God", "Oh yes", "Oh... OH! Yes"])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            "The strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            $ the_girl.have_orgasm()
            if the_girl.vaginal_sex_skill > 3:
                "[the_girl.possessive_title!c] pulls your body close to hers. She cries out as she orgasms, her slick cunt rippling all around you."
                "[the_girl.possessive_title!c]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her. She cries out as she orgasms, her slick cunt rippling all around you."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ against_wall.redraw_scene(the_girl)
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans in ecstasy as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "Having your cum inside her heightens her orgasm as her fetish for you cum is fulfilled."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
            "When you finish, [the_girl.title] leaves her legs wrapped around you as she has a couple aftershocks. Her pussy twitches with each one."
            "She slowly opens her eyes and looks at you."
            $ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay"])
            $ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
            if the_girl.knows_pregnant:# The personality reactions but should it not be True instead of False?
                the_girl "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"
            elif the_girl.is_infertile:
                the_girl "[wordchoice], [the_girl.mc_title]. I can't get pregnant."
            elif the_girl.on_birth_control:
                the_girl "[wordchoice], [the_girl.mc_title]. I'm on [wordchoice2]."
            elif the_girl.has_significant_other:
                the_girl "[wordchoice], [the_girl.mc_title]. If anything happens I'll tell my [the_girl.so_title] it's his."
            else:
                if the_girl.love >59:
                    the_girl "I love you, [the_girl.mc_title]. We should make a baby together."
                elif the_girl.love >0:
                    the_girl "I'm sorry... I don't know what came over me... I just couldn't let you pull out!"
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."

            $ del wordchoice
            $ del wordchoice2
        else:
            $ the_girl.cum_on_stomach()
            $ climax_controller.do_clarity_release(the_girl)
            $ against_wall.redraw_scene(the_girl)
            if mc.condom:
                "You pull out of [the_girl.possessive_title] at the last moment and step back. You whip your condom off and blow your load over her stomach while she watches."
            else:
                "You pull out of [the_girl.possessive_title] at the last moment and step back. You stroke yourself off and blow your load over her stomach while she watches."
            "As your cum erupts, she reaches down with her hand and rapidly strokes her clit. She throws her head back and begins to orgasm together with you."
            $ the_girl.have_orgasm()
            the_girl "Ohhhh yes! Shower me with your hot cum!"
            "You sigh contentedly and relax for a moment, enjoying the sight of [the_girl.title] covered in your semen."
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title!c]'s body goes rigid and goosebumps erupt all over her body as her brain registers your cum on her."
                "[the_girl.possessive_title!c] revels in bliss as she mindlessly rubs in your cum and licks of her fingers to heighten her orgasm."
                "She truly is addicted to your cum."
            elif the_girl.wants_creampie:
                the_girl "What a waste, that would have felt so much better inside me..."
                "She reaches down and runs a finger through the puddles of cum you've put on her, then licks her finger clean and winks at you."
            else:
                the_girl "Oh wow, there's so much of it. It feels so warm..."

    $ post_double_orgasm(the_girl)
    return
