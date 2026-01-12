label intro_cowgirl(the_girl, the_location, the_object):
    the_girl "Lie down for me, I want to be on top."
    "You lie down on the [the_object.name] and undo your pants. [the_girl.title] swings a leg over your body and straddles you."
    $ cowgirl.redraw_scene(the_girl)
    if the_girl.vagina_visible:
        "She leans back and grinds herself against you. The shaft of your cock rubs against the lips of her pussy."
    else:
        "She leans back and grinds herself against you. Underneath her [the_girl.outfit.get_lower_top_layer.display_name] you can feel the lips of her pussy sliding along the length of your shaft."
    the_girl "Ready?"
    if not the_girl.vagina_visible:
        "She quickly moves her clothing out of the way..."
        $ the_girl.strip_to_vagina(position = cowgirl.position_tag, prefer_half_off = True)

    if the_girl.vaginal_sex_skill > 3:
        "You nod. She grinds forward one last time, then lifts herself up and lets your tip fall into place. With one smooth movement she slides you deep into her tight cunt."
    else:
        "You nod and she lifts herself up. She reaches down with one hand and holds onto your cock to hold it steady."
        "When she has you in place she lowers herself down slowly, sliding you inch by inch into her tight cunt."
    the_girl "Ah..."
    "After pausing for a second to adjust [the_girl.possessive_title] starts to ride your dick."
    return

label taboo_break_cowgirl(the_girl, the_location, the_object):
    "[the_girl.possessive_title!c] leads you to the [the_object.name]."
    the_girl "Lie down for me [the_girl.mc_title]..."
    $ cowgirl.redraw_scene(the_girl)
    "You nod and follow her instructions. She steps over you and kneels down, straddling your hips."
    if the_girl.effective_sluttiness(cowgirl.associated_taboo) > cowgirl.slut_cap:
        "She reaches between her legs and grabs your cock, bringing it towards her and running the tip against her clit."
        "You feel her thighs tremble with pleasure."
    else:
        "She reaches between her legs and grabs your cock, rubbing it against her stomach and stroking it gently."
    $ the_girl.call_dialogue(f"{cowgirl.associated_taboo}_taboo_break")
    "[the_girl.title] lifts herself up, puts your hard cock in line with her pussy, and starts to lower herself down."
    "You feel a moment of resistance as your cock spreads her open, then her body weight carries her all the way down your shaft."
    $ play_moan_sound()
    "She closes her eyes and moans, holding your entire length inside her for a few seconds."
    "When she's ready she leans forward and starts to move her hips up and down, sliding your cock in and out of her wet pussy."
    return

label scene_cowgirl_1(the_girl, the_location, the_object):
    if the_girl.arousal_perc > 50:
        "[the_girl.title] leans back, putting her hands in line with your feet."
        "In her reclined position you have a perfect view of her pussy wrapped around your dick. She pumps her hips up and down while you enjoy the show."
        the_girl "Does that feel good? You feel so big inside me..."

    else:
        "[the_girl.title] leans back, putting her hands in line with your feet, and slows down her rhythm."
        the_girl "I need to take it a little slow until I get wet."
        "You have a perfect view of her pussy wrapped around your dick. She moves herself up and down it at a leisurely pace and each stroke feels like warm satin."
        mc.name "Take all the time you need."
    return

label scene_cowgirl_2(the_girl, the_location, the_object):
    "[the_girl.title] speeds up, working her thighs to pump herself up and down your cock."
    if the_girl.has_large_tits:
        if the_girl.tits_visible:
            "Her large, unconstrained tits bounce up and down with each stroke."
            the_girl "Fuck, hold onto these!"
            "[the_girl.possessive_title!c] reaches down and grabs your hands. She brings them up to her tits and plants them there."
            $ play_moan_sound()
            "She moans and grinds your hands into her breasts, then puts her hands on your chest and focuses on fucking you."
        else:
            "Her large tits are barely contained by her [the_girl.outfit.get_upper_top_layer.display_name]. You watch them bounce around as she fucks you vigorously."
    else:
        if the_girl.tits_visible:
            "She reaches up and grabs onto one of her own [the_girl.tits_description], squeezing it while she rides you."
            the_girl "Ah!"
        else:
            "She reaches up and grabs onto one of her [the_girl.tits_description] through her [the_girl.outfit.get_upper_top_layer.display_name]. She kneads it through the fabric and moans loudly while she rides you."
            the_girl "Ah!"
    return

label scene_cowgirl_3(the_girl, the_location, the_object):
    "You put your hands on [the_girl.title]'s hips and guide her up and down at a steady pace."
    if the_girl.arousal_perc > 75:
        "Your cock glides effortlessly in and out of her dripping wet pussy. The warm, tight sensation feels incredible."
    else:
        "Her pussy is warm, tight, and getting wetter by the second."
    "With [the_girl.possessive_title] in control you're able to relax and focus entirely on enjoying the feeling."
    return

label outro_cowgirl(the_girl, the_location, the_object):
    "With each stroke of her hips [the_girl.title] brings you closer and closer to cumming. You're finally driven past the point of no return."
    mc.name "Fuck, I'm going to cum!"

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_girl.wants_creampie or mc.condom: #She drops down on you as you cum.
        the_girl "Yes! Ah!"
        "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
        "Her breath catches in her throat when you pulse out your hot load of cum deep inside her."
        $ climax_controller = ClimaxController(["Cum inside her", "pussy"])
        $ climax_controller.show_climax_menu()
        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
            "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."

            call post_orgasm_condom_routine(the_girl, cowgirl) from _call_post_orgasm_condom_routine_cowgirl

        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ cowgirl.redraw_scene(the_girl)
            "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
            "[the_girl.possessive_title!c] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."

        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."

    elif the_girl.effective_sluttiness("creampie") < 60:
        #She always pull off and you cum on her stomach.
        #There is no condom branch here because 100% of the condom branches go to the first version.
        the_girl "Oh shit, you can't cum inside me!"
        "[the_girl.possessive_title!c] jerks up, pulls off your cock, and lowers herself back down."
        "She leans back and uses one hand to push your shaft against the lips of her pussy, grinding against it until you climax."
        the_girl "Cum for me [the_girl.mc_title], I want you to cum on me!"
        $ climax_controller = ClimaxController(["Cum on her", "body"])
        $ climax_controller.show_climax_menu()
        the_girl "Cum for me [the_girl.mc_title], I want you to cum on me!"
        "You tense up and cum, shooting your thick load up and onto [the_girl.title]'s stomach. She keeps grinding against you're completely spent."
        $ climax_controller.do_clarity_release(the_girl)
        $ the_girl.cum_on_stomach()
        $ cowgirl.redraw_scene(the_girl)

    else:
        #She hesitates and you can decide to pull her down or not.
        #There is no condom branch here because 100% of the condom branches go to the first version.
        "[the_girl.title] starts to pull up and off of you. She hesitates with the tip of your cock just inside her pussy."
        the_girl "I... I really shouldn't let you..."
        "She bites her lip and moans, unsure of what to do."
        $ climax_controller = ClimaxController(["Pull her down and cum inside her", "pussy"],["Let her pull off and cum on her stomach", "body"])
        $ the_choice = climax_controller.show_climax_menu()
        if the_choice == "Pull her down and cum inside her":
            "You reach up and grab [the_girl.possessive_title] by the hips. With one confident pull she plunges back onto your cock, gasping with pleasure."
            "The feeling of her warm, wet pussy sliding down and engulfing your cock again pushes you over the edge. You pull [the_girl.title] tight against you and unload inside her."
            the_girl "Ah! Just... Just this once!"
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.change_obedience(3)
            "You give a few half-hearted pumps when you're done, then tap [the_girl.title] on the ass. She slides off of your dick and collapses beside you."

        elif the_choice == "Let her pull off and cum on her stomach":
            "You stay silent. [the_girl.possessive_title!c] waits another second, as if waiting to be convinced, then pulls off of your cock."
            "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
            $ the_girl.cum_on_stomach()
            $ climax_controller.do_clarity_release(the_girl)
            $ cowgirl.redraw_scene(the_girl)
            the_girl "Whew, that was close..."
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
    return

label transition_default_cowgirl(the_girl, the_location, the_object):
    $ cowgirl.redraw_scene(the_girl)
    "You lie down on the [the_object.name]. [the_girl.title] swings a leg over your waist and straddles you."
    if not the_girl.vagina_visible:
        "She quickly moves her clothing out of the way..."
        $ the_girl.strip_to_vagina(position = cowgirl.position_tag, prefer_half_off = True)

    if the_girl.vaginal_sex_skill > 3:
        "She grinds her pussy against your shaft, then lifts herself up and lets your tip fall into place. With one smooth movement she slides you deep into her tight cunt."
    else:
        "She lifts herself up and reaches down with one hand. She holds onto your cock to hold it steady while she lines it up with herself."
        "When she has you in place she lowers herself down slowly, sliding you inch by inch into her tight cunt."
    return

label strip_cowgirl(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = cowgirl.position_tag)
    "[the_girl.title] struggles out of her [the_clothing.name] and throws it to the side."
    return

label strip_ask_cowgirl(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name]. Would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = cowgirl.position_tag)
            "[the_girl.title] slows down her pace while she strips out of her [the_clothing.name]. When she's free of it she puts her hands on your chest and fucks you faster again."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 70:
                the_girl "Yeah? Do I look sexy in it?"
                "She sighs happily while she rides you."
            else:
                the_girl "Yeah? Do I look like a good little slut in it? Because that's what I feel like right now!"
                "She sighs happily while she rides your cock hard and fast."
            return False

label orgasm_cowgirl(the_girl, the_location, the_object):
    "[the_girl.title] works her hips faster and her breathing grows heavier."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "With one last gasp she collapses down against you. Her thighs quiver as she climaxes."
    "After a second [the_girl.title] regains control of herself. Her breath is warm against your ear as she whispers to you."
    the_girl "I can't stop now, I want you to make me cum again!"
    "She leans back and starts to ride you faster than ever."
    return

label cowgirl_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s is moaning non-stop, while she keeps riding your rock hard cock with loud slapping noises."
    the_girl "Oh god it's so good! Oh [the_girl.mc_title] I'm gonna cum!"
    "Hearing her call out your name and slamming your dick deep inside her is pushing you over the edge. You are about to cum too."
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her stomach", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside her":
        "[the_girl.possessive_title!c], using her full weight, pushes you deeper inside her as you climax."
        $ the_girl.have_orgasm()
        "She is moaning loudly as she cums together with you at the same time."
        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "After you finished cumming, she keeps you deep inside her for a few moments while she has a few aftershocks."
            "When your dick finally slips out of her leaking wet pussy, the condom is ballooned with your seed, hanging off your cock to one side."

            call post_orgasm_condom_routine(the_girl, missionary) from _call_post_orgasm_condom_routine_cowgirl_double_orgasm

        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ cowgirl.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                the_girl "Oh fuck oh yes!!!"
                "Her body convulses and she uses her full weight to push you deeper insider her as her orgasm hits."
            "After you finished cumming, [the_girl.title] keeps you deep inside her for a few moments while she has a few aftershocks, until your cock slowly slides out of her dripping wet pussy."

    elif the_choice == "Cum on her stomach":
        if mc.condom == False and (the_girl.has_breeding_fetish or the_girl.has_cum_fetish): #Leg Lock for internal creampie
            "While you try to push her up and take your rock hard cock out, [the_girl.title] locks her feet behind your legs and pushes down with her full weight."
            $ wordchoice = renpy.random.choice(["Oh God", "Oh yes", "Oh... OH! Yes"])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            "The sheer strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            if the_girl.vaginal_sex_skill > 3:
                "[the_girl.possessive_title!c] pulls your body close to hers, burying your cock as deep as she can and milks it with the muscles inside her dripping wet slit."
                "[the_girl.possessive_title!c]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few more times to make sure that you cum deep inside her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ cowgirl.redraw_scene(the_girl)
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
            if the_girl.has_cum_fetish or the_girl.has_breeding_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "She throws her head back in pleasure."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! Fill up your little slut!"
            $ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay", "Settle down"])
            $ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
            if the_girl.knows_pregnant:# The personality reactions but should it not be True instead of False?
                the_girl "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"
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
            $ cowgirl.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if mc.condom:
                "You pull out of [the_girl.possessive_title] at the last moment. You whip your condom off and blow your load over her stomach while she watches."
            else:
                "You pull out of [the_girl.possessive_title] at the last moment, while you blow your load over her stomach while she watches."
            if the_girl.wants_creampie:
                the_girl "What a waste, that would have felt so much better inside me..."
                "She reaches down and runs a finger through the puddles of cum you've put on her, then licks her finger clean and winks at you."
            else:
                the_girl "Oh wow, there's so much of it. It feels so warm..."
            "You sigh contentedly and relax for a moment, enjoying the sight of [the_girl.title] belly covered in your semen."

    $ post_double_orgasm(the_girl)
    return

label GIC_outro_cowgirl(the_girl, the_location, the_object):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal is None or the_goal == "get mc off" or the_goal == "anal creampie":
        $ cowgirl.call_default_outro(the_girl, the_location, the_object)

    else:
        "With each stroke of her hips [the_girl.title] brings you closer and closer to cumming. You're finally driven past the point of no return."
        mc.name "Fuck, I'm going to cum!"
        if the_goal == "get off":
            the_girl "Seriously? I haven't finished yet..."
            if mc.condom:
                "She keeps riding you. With one final stroke you start to cum into the condom."
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
                "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."
            else:
                "You stay silent. [the_girl.possessive_title!c] waits another second, as if waiting for a response, then pulls off of your cock."
                "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
                $ the_girl.cum_on_stomach()
                $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_girl)
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "waste cum":
            the_girl "You wanna cum inside me? Do you?"
            "She starts to speed up. You moan as you get ready to fire your load up inside her."
            if mc.condom:
                "At the last second she pulls off and pulls your condom off. You groan as your start to cum, spraying all over your stomach."
            else:
                "At the last second she pulls off, you groan as your start to cum, spraying all over your stomach."
            the_girl "Ha! Not a chance."
            "She watches as your cock twitches and finishes."
            $ ClimaxController.manual_clarity_release(climax_type = "air", person = the_girl)
            the_girl "Look at all that wasted cum... Too bad, [the_girl.mc_title]!"
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "hate fuck":
            if not the_girl.is_infertile and (the_girl.on_birth_control or mc.condom):
                the_girl "Already? I guess I was just too much for you to handle."
                if mc.condom:
                    the_girl "Whatever, I'm sure the condom can handle your pathetic load."
                    "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
                    "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                    "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."
                else:
                    the_girl "I don't feel like getting off. Go ahead and cum inside me [the_girl.mc_title], I'm on birth control anyway."
                    $ the_girl.update_birth_control_knowledge()
                    "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                    $ the_girl.cum_in_vagina()
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
                    $ cowgirl.redraw_scene(the_girl)
                    "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                    "[the_girl.possessive_title!c] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
            else:
                the_girl "Already? Is my cunt to just too much for you to handle?"
                if the_girl.wants_creampie:
                    the_girl "Whatever. I want to feel you cum inside me. Not like your swimmers are strong enough to knock me up anyway."
                    "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                    $ the_girl.cum_in_vagina()
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
                    $ cowgirl.redraw_scene(the_girl)
                    "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                    "[the_girl.possessive_title!c] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
                else:
                    the_girl "Whatever. Hurry up and cum."
                    "She starts to speed up. You moan as you get ready to fire your load up inside her."
                    "At the last second she pulls off, you groan as your start to cum, spraying all over your stomach."
                    "She watches as your cock twitches and finishes."
                    $ ClimaxController.manual_clarity_release(climax_type = "air", person = the_girl)
                    the_girl "Look at all that wasted cum... Too bad, [the_girl.mc_title]!"
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "vaginal creampie":
            the_girl "Yes! Ah!"
            "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
            "Her breath catches in her throat when you pulse out your hot load of cum deep inside her."
            #the_girl "Oh my god... Give it all to me [the_girl.mc_title]... Fill me up..."
            if mc.condom:
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
                "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."

                call post_orgasm_condom_routine(the_girl, cowgirl) from _call_post_orgasm_condom_routine_GIC_cowgirl

            else:
                $ the_girl.call_dialogue("cum_vagina")
                $ the_girl.cum_in_vagina()
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_girl)
                $ cowgirl.redraw_scene(the_girl)
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                "[the_girl.possessive_title!c] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "facial":
            if mc.condom:
                "[the_girl.possessive_title!c] pulls off you, but quickly moves down your body. She pulls off the condom and begins stroking you while pointing it at her face."
            else:
                "[the_girl.possessive_title!c] pulls off you, but quickly moves down your body and begins stroking your cock. She points it at her face."
            $ the_girl.draw_person(position = "kneeling1")
            the_girl "That's it. I want it on my face!"
            "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            "[the_girl.title] looks up at you, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")
        elif the_goal == "body shot":
            the_girl "Ohhh, I can't wait to feel it on my skin."
            if mc.condom:
                "[the_girl.possessive_title!c] pulls off you, reaches down and pulls your condom off and begins stroking you."
            else:
                "[the_girl.possessive_title!c] pulls off you, reaches down and begins to stroke you."
            "She grinds the lips of her [the_girl.pubes_description] pussy against your shaft as you climax. You fire your hot load over her stomach."
            $ the_girl.cum_on_stomach()
            $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_girl)
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "oral creampie":
            the_girl "Wait! I want it in my mouth!"
            if mc.condom:
                "[the_girl.possessive_title!c] pulls off you, but quickly moves down your body. She pulls off the condom and takes you into her mouth."
            else:
                "[the_girl.possessive_title!c] pulls off you, but quickly moves down your body and takes you into her mouth."
            $ the_girl.draw_person(position = "kneeling1")
            $ play_moan_sound()
            "She moans as your cum begins to spill into her mouth."
            $ the_girl.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm into [the_girl.possessive_title]'s eager mouth. She makes sure to wait until you're completely finished."
            $ play_swallow_sound()
            "[the_girl.title] closes her mouth and swallows loudly."
            "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
        else:
            "DEBUG tell starbuck she fucked up you shouldn't be here"
    return
