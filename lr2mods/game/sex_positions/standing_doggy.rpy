label intro_standing_doggy(the_girl, the_location, the_object):
    "You turn [the_girl.possessive_title] around, and she leans over the [the_object.name], presenting her ass to you."
    $ the_girl.draw_person(position = standing_doggy.position_tag)
    mc.name "Good girl, [the_girl.title], I'm going to fuck you hard."
    if the_girl.opinion.doggy_style > 2 :
        the_girl "Oh thank god, I've been daydreaming about you bending me over all day long."
    elif the_girl.opinion.sex_standing_up > 2 :
        the_girl "Oh thank god, I've been daydreaming about this all day long."
    elif the_girl.opinion.doggy_style > 0 :
        the_girl "I can't wait! It's so good when you bend me over."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 60:
        the_girl "Mmmm, this is gonna be fun."
    else:
        the_girl "Okay [the_girl.mc_title], I'll play along this time."

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = standing_doggy.position_tag, prefer_half_off = True)

    if the_girl.arousal_perc > 60:
        $ play_moan_sound()
        "You rub the tip of your cock against [the_girl.possessive_title]'s cunt, feeling how nice and wet she is already. She moans, anticipating your penetration."
        "You continue to rub your dick against her [the_girl.pubes_description] pussy and gather more of her juices. She is already so wet you are soon slick with her secretions."
    else:
        "You rub the tip of your cock against [the_girl.possessive_title]'s cunt."
    "When you're ready you push forward. Her pussy feels amazing wrapped around your erection."
    if the_girl.opinion.doggy_style > 0 :
        the_girl "Oh my god..."
        $ the_girl.discover_opinion("doggy style sex")
    if the_girl.opinion.sex_standing_up > 0 :
        "Her legs shake a bit as she gets used to the depth of your penetration."
        $ the_girl.change_arousal(the_girl.opinion.sex_standing_up)
        $ the_girl.discover_opinion("sex standing up")
    return

label scene_standing_doggy_1(the_girl, the_location, the_object):
    "Your hips slap against [the_girl.possessive_title]'s ass as you fuck her vigorously."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    if the_girl.vaginal_sex_skill < 3: #Inexperienced
        "After a particularly hard thrust, [the_girl.possessive_title] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl "I'm sorry [the_girl.mc_title], that's a little too rough. Can you go a little slower?"
        "You pull her hips back toward you slowly. She sighs, still trying to get accustomed to your girth, penetrating her at such a deep angle."
        "The next time you push yourself in you push a little faster. She seems to be adapting to your fucking."
    elif the_girl.has_breeding_fetish:          #breeding fetish
        $ play_moan_sound()
        "After a particularly hard thrust, [the_girl.possessive_title] moans lewdly."
        the_girl "That's it, fuck me harder! God, I can't imagine going a single day without your cock inside me..."
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand."
        "[the_girl.possessive_title!c] rocks her hips side to side each time you slam into her. Each time you pull back you can see her labia clinging to you."
        "You use both hands to grab her hips and slam yourself into her as deep as you can go."
        $ play_spank_sound()
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    else:
        $ play_moan_sound()
        "Fucking her hard, [the_girl.possessive_title] moans, matching each hip movement of yours with a movement of her own."
        the_girl "Oh god, you fuck me so good, I can barely keep up!"
        "[the_girl.possessive_title!c] reaches back with one hand and pulls her ass cheek back, giving you a great view of her pussy stretched wide to accommodate you."
        $ play_spank_sound()
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    menu:
        "Spank her" if the_girl.spank_level <= 8:
            "You look down at [the_girl.possessive_title]'s ass. It is [the_girl.ass_spank_description]"
            $ the_girl.slap_ass()
            "With your erection buried deep inside her, you give her ass a firm spank. Her sexy cheeks quake in response."
            mc.name "[the_girl.title], your ass looks amazing when I spank it. You are such a slut. I bet you love it, don't you?"
            if the_girl.is_submissive:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans at your words."
                $ play_spank_sound()
                "You pull her ass cheeks apart. You give her a hard spank with your other hand and enjoy the feeling of her silky cunt."
                mc.name "Do you let any guy with a hard cock fuck you and spank you like this? Or just me?"
                "[the_girl.possessive_title!c] responds quietly."
                if the_girl.is_submissive and not the_girl.can_be_spanked:
                    the_girl "Just you! I love it when you get rough with me, and spank me when I've been naughty!"
                    "She really seems to enjoy her spanking. Maybe you should work it into your normal foreplay..."
                    $ the_girl.unlock_spanking()
                else:
                    the_girl "Just you, [the_girl.mc_title]. I don't know why but it just feels so good... so right when you dominate me..."
                if the_girl.is_family:
                    the_girl "It makes me so happy to serve you like this... To be [the_girl.relation_possessive_title]!"
                "You give her pussy a few rough thrusts before bottoming out again."
                mc.name "That's right bitch, you're my little fuckhole. I'll bend you over and fuck you anytime I please."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.opinion.being_submissive * 2)
            else:
                the_girl "Mmm, it feels good but kinda hurts... could you hit a little more softly?"
                $ the_girl.slap_ass(update_stats = False)
                "You give her plaint ass another swat, this time not quite as hard."
                $ the_girl.slap_ass(update_stats = False)
                "Her ass quivers slightly as you spank her. Her pussy clenches around you each time you spank her."
            if mc.arousal_perc > 70:
                "[the_girl.possessive_title!c]'s tight pussy feels so good. You are getting close to cumming."
                mc.name "You feel amazing. You're gonna make me cum soon."
                if the_girl.wants_creampie:
                    "[the_girl.possessive_title!c] looks back at you and smiles."
                    the_girl "Oh [the_girl.mc_title], I can't wait to feel you fill me up. I hope you finish deep!"
                    "[the_girl.possessive_title!c]'s ass quivers a bit, as she imagines you cumming deep inside her."
                    $ the_girl.discover_opinion("creampies")
                    $ the_girl.discover_opinion("bareback sex")
                    $ the_girl.change_arousal(the_girl.opinion.creampies)
                    if the_girl.opinion.being_covered_in_cum > 0:
                        the_girl "You could always pull out too... your cum feels so good when it splashes all over my skin..."
                        $ the_girl.discover_opinion("being covered in cum")
                        $ the_girl.change_arousal(the_girl.opinion.being_covered_in_cum)
                        if the_girl.opinion.cum_facials > 0:
                            the_girl "Or my face! You haven't cum on my face in a while either..."
                            $ the_girl.discover_opinion("cum facials")
                            $ the_girl.change_arousal(the_girl.opinion.cum_facials)
                            "[the_girl.possessive_title!c] starts muttering to herself, fantasizing about all the different ways you could cum on, or in her."
            "You put your hands on her hips and continue fucking her."

        "Spank her\nToo bruised to continue (disabled)" if the_girl.spank_level > 8:
            pass

        "Play with her clit":
            "You lean forward a bit and reach down with one hand and begin to move it in circles around her clit."
            if the_girl.opinion.being_fingered > 0:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans loudly in response."
                the_girl "Oh [the_girl.mc_title], I love when you touch me there."
                "You slide your fingers around her slit a few times."
                "You give your hips a few long, slow strokes as your circle her clit with your fingers."
                $ the_girl.discover_opinion("being fingered")
                $ the_girl.change_arousal(the_girl.opinion.being_fingered + mc.foreplay_sex_skill)
                "She really enjoys the extra stimulation."
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            elif mc.foreplay_sex_skill > 4:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her."
                $ the_girl.change_arousal(mc.foreplay_sex_skill)
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."

            else:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her."
                $ the_girl.change_arousal(mc.foreplay_sex_skill)
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            if the_girl.arousal_perc > 90:
                the_girl "Oh fuck! Don't stop! Don't you dare stop!"
                $ play_moan_sound()
                "Her moans clearly indicate an impending orgasm. As best you can, you fuck her while you roughly rub her clit."
            else:
                "After a bit longer of touching her, you straighten your back and begin to rock your hips again, continuing to fuck her."
    return


label scene_standing_doggy_2(the_girl, the_location, the_object):
    "You take a breather, and then slowly start bringing the pace back up a bit."
    if the_girl.tits_available:
        "You reach around her body with one hand and grasp her tit. You pinch and pull at her nipple roughly as you fuck her saturated slit."
    else:
        $ play_spank_sound()
        "You run your hands along her hips. You grab her hips and smack her ass roughly as you fuck her saturated slit."

    if the_girl.arousal_perc > 100:
        the_girl "Ohhh my god, I already came... and you're still fucking me!"
        "[the_girl.possessive_title!c]'s legs are shaking. Her orifice clenches and spasms around you."
        "Her pussy convulsing around you feels spectacular."
        $ mc.change_arousal(5)
    elif the_girl.arousal_perc > 80:
        the_girl "Ohhh, [the_girl.mc_title]... You are gonna make me cum so hard..."
        "You can feel a slight quiver in [the_girl.possessive_title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.possessive_title!c] groans in response to one particularly deep thrust."
        the_girl "It's so big... it feels so good buried inside me."
    $ play_moan_sound()
    "You push yourself in as deep as you can go. [the_girl.possessive_title!c] moans as you fill her completely."
    menu:
        "Gentle Sex":
            "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
            mc.name "[the_girl.title], your pussy is so good. I love how eager you are to fuck me."
            if the_girl.sluttiness > 80:
                the_girl "Of course I'm eager. Your cock fills me just right. Fuck me good [the_girl.mc_title]!"
            else:
                the_girl "Mmm, I can't help it, you make me feel so good."
        "Rough Sex":
            if the_girl.is_bald:
                "You take one hand and start to knead the back of her scalp. Getting a good grip around her neck and pull."
            else:
                "You take one hand and start to knead the back of her scalp. You grab a fistful of hair and pull."
            "[the_girl.possessive_title!c] arches her back in response."
            mc.name "That's a good slut. Take it nice and deep."
            if the_girl.is_submissive:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans enthusiastically."
                the_girl "[the_girl.mc_title]! I love it deep. Fuck me good!"
                "[the_girl.possessive_title!c] begs you for more."
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.opinion.being_submissive)
            elif the_girl.is_dominant:
                "[the_girl.possessive_title!c] looks back at you with a scowl."
                the_girl "Don't get used to it, [the_girl.mc_title]... I'm not sure how I let you talk me into this..."
                $ the_girl.discover_opinion("being submissive")
                "You let go of her [the_girl.hair_description] and decide for now to keep your pace nice and slow."
            else:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans."
                the_girl "You are so deep... It feels good having you so deep inside me."
                "You stir the depths of her pussy with your erection by moving your hips side to side."

    return

label scene_standing_doggy_3(the_girl, the_location, the_object):
    if the_girl.body_is_thin:
        "Your hips begin to slap up against [the_girl.possessive_title]'s gloriously fit ass."
        "Her cheeks are tight from the exercise and care she puts into her body."
    elif the_girl.body_is_average:
        "Your hips begin to slap up against [the_girl.possessive_title]'s delicious ass."
        "Her cheeks are round but firm with just a hint of quaking with each impact."
    elif the_girl.body_is_thick:
        "Your hips begin to slap up against [the_girl.possessive_title]'s thick ass."
        "Her cheeks are full and generous, and they quake back and forth enticingly as you pound her."
    elif the_girl.body_is_pregnant:
        "Your hips begin to slap up against [the_girl.possessive_title]'s wide ass."
        "Her cheeks make a pleasing heart shape since her body has been changing with the baby growing in her belly."
    else:
        "Your hips begin to slap up against [the_girl.possessive_title]'s ass."
        "Her cheeks respond delightfully with each thrust."
    "[the_girl.title] is thrusting back against you, using the [the_object.name] as leverage to push herself back. Her ass is mesmerising."
    menu:
        "Finger her ass":
            if report_log.get("ass fingered", 0) == 0:
                "You decide to give her ass a little extra attention. You work up some saliva in your mouth then pause fucking her for a second."
                the_girl "Hey... why did you stop?"
                "Instead of answering her, you let the saliva drop from your mouth onto her crack. She feels it and realises what you are about to do when you start to work it into her crack with your finger."
            else:
                "Her butthole is still glistening with your saliva, so you decide to give it some extra attention."

            if the_girl.opinion.anal_sex > 1:
                "[the_girl.possessive_title!c] bucks her hips slightly as you start to push your finger into her tight back passage. Her back arches in pleasure."
                the_girl "Mmm! [the_girl.mc_title] that feels so good."
                $ the_girl.change_arousal(the_girl.opinion.anal_sex + mc.anal_sex_skill)
                "You slowly give her a long, deliberate stroke, pushing your cock and finger into her at the same time."
                "With your shaft buried inside her, you start to stroke yourself with your finger in her ass. An odd but very pleasurable feeling."
                "[the_girl.title] starts to get impatient and begins to move her hips forward and back. It feels so good, soon you are matching her."
                $ play_moan_sound()
                "You speed up and start to really pound her, her moans increasing in pitch from the double penetration."
                "Soon though, you feel the urge to really give it to her, so you pull your finger out so you can grab both her hips and fuck her rough."

            elif the_girl.opinion.anal_sex < 0:
                $ the_girl.call_dialogue("surprised_exclaim")
                the_girl "Hey I'm not really into that..."
                "She starts to pull away from you."
                "It seems that [the_girl.possessive_title] doesn't like having her ass played with."
                $ the_girl.change_arousal(the_girl.opinion.anal_sex)
                "You quickly mumble an apology. Instead of fingering her, you grab her hips with both hands and start to pound her."
            else:
                "[the_girl.possessive_title!c] tenses slightly as you start to push your finger into her back passage, but otherwise doesn't resist."
                the_girl "Go slow... I don't let just anyone touch me like this..."
                "She forces herself to relax. You can feel her rectum physically unclench, and you begin to slowly move your finger in and out of her."
                the_girl "That feels good [the_girl.mc_title]... just be careful with me back there!"
                "As you finger her ass, her hips remain stationary. She wills herself to relax, and manages to enjoy the stimulation."
                $ the_girl.change_arousal(mc.anal_sex_skill)
                "Soon though, you feel the urge in your hips to start fucking her again, so you pull your finger out so you can grab both her hips."

            $ report_log["ass fingered"] = report_log.get("ass fingered", 0) + 1
            $ the_girl.discover_opinion("anal sex")
        "Grope her ass":
            "Your hands are drawn to her cheeks. With a soft touch you trace your finger down around their delicious curve."
            "You grab a handful, her ass flesh feels tight and full in your hand. She moans and you give her a couple vigorous thrusts."
            mc.name "Your ass is amazing. Maybe I'll fuck you back there next..."
            $ play_moan_sound()
            "She moans and pushes back against you as you fuck."
    return

label standing_doggy_stealth_attempt(the_girl, the_location, the_object):  #Write the new scene here
    "[the_girl.possessive_title!c] moans, clearly enjoying herself as your cock hits all the right places."
    $ play_moan_sound()
    "She lowers her body to the [the_object.name] and arches her back. Her ass jiggles pleasantly with each stroke."
    if mc.condom:
        if not mc.has_removed_condom:
            "You look down and watch as her pussy takes your condom covered cock over and over. You wonder how good it would feel have her pussy stroke you raw."
            "[the_girl.title] is face down, if you are quick you could probably remove the condom without her even noticing."
            "If you take it off you should probably pull out when you finish though... or should you?"
            menu:
                "Attempt to remove condom":
                    "You bring one hand down to your cock and get it ready. With one out stroke, you pretend to accidentally pull back too far, pulling out of her."
                    "You quickly strip off the condom as quietly as possible, then line yourself up and plunge back into [the_girl.title]'s dripping wet cunt."
                    $ mc.remove_condom_stealth()
                    #TODO add a check against focus where she realises what you are doing
                    "You grab her hips and start pounding her with renewed vigour, enjoying the amazing sensation of her raw pussy."
                    the_girl "Oh god it feels so good. I can feel you so deep!"
                    "You smirk and shove yourself in deeper. It feels like her cunt is swallowing you whole. You enjoy the sensation for a few moments then resume fucking."
                    return
                "Leave condom on":
                    pass
        else:
            "You look down and watch your uncovered cock slide deep into [the_girl.title]'s dripping wet snatch."

    "You grab her her hips and start fucking her faster and deeper. [the_girl.possessive_title!c] responds by bracing herself against the [the_object.name]... her legs trembling from the effort."
    return


label outro_standing_doggy(the_girl, the_location, the_object):
    "[the_girl.possessive_title!c]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her ass", "body"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside her":
        "[the_girl.possessive_title!c]'s drenched cunt is just too good. You decide to cum inside it."
        if mc.has_removed_condom:  #You sly dog
            "You know you should probably pull out after pulling the condom off, but you can't. You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum."
            the_girl "Oh god, you are cumming so hard, I swear I can almost feel it splashing inside me!"
            $ the_girl.cum_in_vagina()
            $ standing_doggy.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "After you finish, you leave your cock deep inside her. A few drops of your cum start to drip out of her."
            "[the_girl.title] reaches between her legs and feels it, realising you just finished inside her."
            if the_girl.has_job(prostitute_job):
                if the_girl.on_birth_control or the_girl.is_infertile:
                    the_girl "What the FUCK? You took the condom off? And then came inside me!?! I know I'm just a working girl, but you can't treat me like this."
                else:
                    the_girl "What? You took the condom off? And then came inside me!?! Fuck, I could get pregnant, not all working girls take birth control, you asshole!"
                    $ the_girl.update_birth_control_knowledge()
                $ the_girl.change_stats(happiness = -5, obedience = 3, love = -5) #She loses trust
            elif the_girl.wants_creampie:         #She likes creampies...
                the_girl "Wait... that's... you took the condom off, didn't you? Oh fuck that's why it felt so good!"
                $ the_girl.discover_opinion("creampies")
                if the_girl.is_infertile or (the_girl.on_birth_control and not the_girl.is_pregnant):
                    the_girl "Oh god, that's so hot! I love feeling cum deep inside me."
                elif the_girl.knows_pregnant:
                    the_girl "So fucking hot! Bathe my pregnant womb with your hot cum!"
                else:
                    the_girl "Oh god that's so hot. You could knock me up you know? Next time be more careful!"
                    "Her voice drops to a whisper."
                    the_girl "or don't..."
                $ the_girl.change_stats(happiness = 2, obedience = 3)
                # she liked it, so skip condom in next loops
                $ use_condom = False
            elif the_girl.sluttiness > 80:                          #She is slutty enough she doesn't mind the cream filling
                the_girl "Oh my god you took the condom off? You know you can cum inside me anytime you want, no need to take it off like that!"
                menu:
                    "Agree":
                        mc.name "I like the sound of that."
                        $ use_condom = False
                    "Don't":
                        mc.name "I was just checking how far you were willing to go."
                $ the_girl.change_obedience(3)
            else:                                                   #She gets pissed
                if the_girl.on_birth_control or the_girl.is_infertile:
                    the_girl "What the FUCK? You took the condom off? And then came inside me!?! You asshole!"
                else:
                    the_girl "What the FUCK? You took the condom off? And then came inside me!?! I could get pregnant, asshole!"
                    $ the_girl.update_birth_control_knowledge()
                $ the_girl.change_stats(happiness = -5, obedience = 3, love = -5) #She loses trust
                "You planted your seed inside [the_girl.possessive_title], but it is clear she isn't happy about it."
            "You slowly pull out of [the_girl.title]. Your cum is dripping down her leg as you sit back."
        elif mc.condom:
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum. She gasps when she feels you filling the condom deep inside her."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You wait until your orgasm has passed completely, then pull out and sit back. Your condom is bulged on the end where it is filled with your seed."
            $ the_girl.draw_person(position = the_girl.idle_pose)
            if the_girl.opinion.drinking_cum > 1 and the_girl.sluttiness > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title!c] turns around and reaches for your cock. With delicate fingers she slides the condom off of you."
                the_girl "It would be a shame to waste all of this, right?"
                "She winks and brings the condom to her mouth. Squeezing all your cum right into her mouth."
                $ the_girl.change_slut(the_girl.opinion.drinking_cum, 70)
            else:
                "[the_girl.possessive_title!c] turns around and reaches for your cock. She removes the condom and ties the end in a knot, before throwing it away."
            "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
        else:
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum. She gasps softly in time with each new shot of hot semen inside her."

            if the_girl.wants_creampie:
                the_girl  "Yes! Fill me with your cum!"
            if the_girl.arousal_perc > 100:
                "You feel her pussy convulsing around your dick as she also starts to orgasm."
                $ the_girl.change_happiness(5)
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ standing_doggy.redraw_scene(the_girl)
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title!c]'s body goes rigid as your cum pours into her [the_girl.pubes_description] pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"

            if the_girl.knows_pregnant:
                the_girl "I just love it when you fill me up, I can take a load like that anytime..."
            elif the_girl.opinion.bareback_sex > 0:
                the_girl "Oh god... I can feel it so deep. I mean... it could... hopefully..."
                "[the_girl.possessive_title!c]'s voice starts to trail off."
            elif the_girl.sluttiness > 90 or the_girl.is_infertile:
                the_girl "Oh god, it's so deep."
            elif the_girl.on_birth_control:
                the_girl "Oh fuck... Good thing I'm on the pill..."
                $ the_girl.update_birth_control_knowledge()
            else:
                the_girl "Oh fuck... I could get pregnant you know..."

            "You wait until your orgasm has passed completely, then pull out and stand back."

            if the_girl.opinion.bareback_sex > 0:
                "As your cum starts to leak out, [the_girl.possessive_title] reaches back and tries to keep it inside with her hand."
            else:
                "Your cum leaks out of her dripping wet pussy."

    if the_choice == "Cum on her ass":
        if mc.condom and not mc.has_removed_condom:
            "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as you blow your load all over her ass."
            "She holds still for you as you cover her with your sperm."
        else:
            "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        if the_girl.opinion.being_covered_in_cum > 0:
            the_girl "Yes! Paint me with your sticky cum!"
        $ the_girl.cum_on_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ standing_doggy.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title!c]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            $ play_moan_sound()
            "[the_girl.possessive_title!c] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            "She truly is addicted to your cum."
        if the_girl.sluttiness > 90:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
    if the_choice == "Cum on her face":
        mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
        if mc.condom and not mc.has_removed_condom:
            "You pull your cock out of [the_girl.possessive_title] with a satisfying pop. You pull your condom off as she turns around and gets on her knees in front of you."
        else:
            "You pull your cock out of [the_girl.possessive_title]. She immediately turns around and gets on her knees in front of you."
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.opinion.being_covered_in_cum > 0 or the_girl.opinion.cum_facials > 0:
            "[the_girl.possessive_title!c] reaches up and strokes you off for your final few seconds."
            "Your orgasm hits hard. Your first jet sprays across her face."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            if the_girl.has_cum_fetish:
                "You can see [the_girl.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                $ play_moan_sound()
                "[the_girl.possessive_title!c] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                "She truly is addicted to your cum."
            else:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as your dick sprays jet after jet of seed across her face."
        elif the_girl.sluttiness > 80:
            "[the_girl.possessive_title!c] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            the_girl "Oh god... it feels so good on my skin..."
        elif the_girl.sluttiness > 60:
            "[the_girl.possessive_title!c] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.possessive_title!c] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        $ climax_controller.do_clarity_release(the_girl)
        "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title!c] looks up at you from her knees, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")
    return

label transition_standing_doggy_doggy(the_girl, the_location, the_object):
    mc.name "Get down on your knees [the_girl.title], I'm going to fuck you like the little bitch you are."
    the_girl "Oh yes, [the_girl.mc_title], make me your little bitch."
    return

label transition_standing_doggy_anal_standing(the_girl, the_location, the_object):
    "You pull out of [the_girl.title]'s wet pussy, leaving it dripping fluids on the [the_object.name]."
    "You line your cock up with her asshole, the tip just barely pressing against it."
    call transition_default_anal_penetration_dialog(the_girl, the_location, the_object) from _call_transition_default_anal_penetration_dialog_2
    return

label transition_standing_doggy_to_standing_anal_taboo_break_label(the_girl, the_location, the_object):
    "You hold onto [the_girl.title]'s ass cheeks with each hand. You spread them apart, giving you a clear view of her asshole as you continue to fuck her pussy."
    if the_girl.arousal_perc >= 70 or report_log.get("girl orgasms", 0) > 0:
        "You pull out of [the_girl.title]'s wet pussy, leaving it dripping fluids on the [the_object.name]. You hold her ass cheeks in place with one hand, while you guide your well lubed cock to her tight hole."
    else:
        "You hold her ass cheeks in place with one hand as you pull back and out of [the_girl.title]'s pussy. You hold your cock with the other hand, guiding it as you press the head against her tight hole."
    "You lean forward to whisper in her ear."
    mc.name "I think it's time we stretched you open."
    $ the_girl.call_dialogue(f"{anal_standing.associated_taboo}_taboo_break")
    if the_girl.opinion.anal_sex > 0:
        "[the_girl.title] shivers with anticipation."
    if the_girl.anal_sex_skill > 3:
        "She gasps as your tip starts to spread her open. She tilts her head back and pushes her hips against you, helping the process."
        the_girl "Oh god... Mfphhhh!"
    else:
        "She gasps as your tip tries to spread open her impossibly tight asshole. She tries to pull away, but you pull on her waist and bring her closer."
        mc.name "Come on, you'll get there."
        if the_girl.arousal_perc >= 70 or report_log.get("girl orgasms", 0) > 0:
            "Your cock is still wet from [the_girl.title]'s pussy. You push steadily as you slide the tip into [the_girl.title]'s ass."
        else:
            "You pull back slightly, spit onto your cock and try again. This time making better progress, sliding the tip of your dick into [the_girl.title]'s ass."
        the_girl "Oh god... Fuck!"
    "Inch by inch you slide your entire length into [the_girl.possessive_title]. She grunts and gasps the whole way down."
    "You stop when you've bottomed out, to give your cock time to properly stretch her out."
    the_girl "I think... I'm ready for you to move some more..."
    "You pull back a little bit and give her a few testing strokes. When she can handle those you speed up, until you're thrusting your entire length."
    return

label transition_default_standing_doggy(the_girl, the_location, the_object):
    mc.name "Stand here."
    $ standing_doggy.redraw_scene(the_girl)
    "[the_girl.possessive_title!c] obeys then leans forward and puts her hands on the [the_object.name]."
    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = standing_doggy.position_tag, prefer_half_off = True)
    "You bounce your hard shaft on her ass a couple of times before sliding your cock between her thighs."
    "You continue your back and forth motion, rubbing your cock along her pussy lips."
    if the_girl.opinion.vaginal_sex > 0:
        the_girl "Oh... Please..."
    "You continue to move your cock forwards and backwards teasing her [the_girl.pubes_description] pussy."
    if the_girl.has_taboo("vaginal_sex"):
        $ the_girl.call_dialogue(f"{doggy.associated_taboo}_taboo_break")
        "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
        "After a moment of resistance your cock spreads her pussy open and you slide smoothly inside her."
        the_girl "Oh god... Ah..."
        "You start with short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
        $ the_girl.break_taboo("vaginal_sex")
    else:
        "Once you're both ready you push yourself forward, slipping your hard shaft deep inside her. She lets out a gasp under her breath."
    return

label strip_standing_doggy(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title!c] leans forward a little farther and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  standing_doggy.position_tag)
    "[the_girl.possessive_title!c] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside her."
    return

label strip_ask_standing_doggy(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = standing_doggy.position_tag)
            "[the_girl.possessive_title!c] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She groans happily when you push back inside her."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her hips back into you and moans happily."
            else:
                the_girl "Does it make me look like the cum–hungry slut that I am? Or is it your cock inside me that makes me look that way?"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label orgasm_standing_doggy(the_girl, the_location, the_object):
    "[the_girl.possessive_title!c]'s legs start to quiver, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "You bury your cock deep in [the_girl.possessive_title]'s cunt while she cums. Her pussy spasms around you."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    if the_girl.opinion.doggy_style > 0:
        the_girl "Oh god, you've got me bent over and it feels so good I'm just cumming all over you..."
    the_girl "Don't stop... it still feels so good!"
    return

label taboo_break_standing_doggy(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You grab [the_girl.possessive_title]'s ass and give it a squeeze, then a hard slap."
    if the_girl.effective_sluttiness(standing_doggy.associated_taboo) > standing_doggy.slut_cap or the_girl.opinion.showing_her_ass > 0:
        mc.name "Stand over here, let me have a good look from behind."
        $ the_girl.draw_person(position = "back_peek")
        "She turns around and jiggles her butt playfully for you."
        the_girl "This cute ass? You want to have a closer look?"
        mc.name "I said stand here, come on."
        $ the_girl.draw_person(position = "standing_doggy")
        "She leans into the [the_object.name] and points her butt in your direction. She lowers her shoulders and works her hips for you."
    else:
        mc.name "Stand over here."
        $ the_girl.draw_person(position = "stand2")
        "She slowly walks to the indicated position in front of you."
        mc.name "Good girl, now spin around and show me that ass."
        "She nods and turns around."
        $ the_girl.draw_person(position = "walking_away")
        mc.name "Nice. Now shake it for me."
        the_girl "Like... this?"
        $ the_girl.draw_person(position = "standing_doggy")
        "[the_girl.title] works her hips and jiggles her ass for you."
        mc.name "Getting there, a little faster now."
        "She speeds up."
    the_girl "Is that what you wanted?"
    "You move behind her and slide your cock between her thighs, brushing softly along her already wet snatch."
    mc.name "Not quite, you seem pretty excited, perhaps I should slide it in to see if you can take it."
    $ the_girl.call_dialogue(f"{standing_doggy.associated_taboo}_taboo_break")
    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you press it against her wet hole."
    if the_girl.vaginal_sex_skill > 3:
        "She gasps as your tip starts to spread her lips apart. She lowers her shoulders and pushes her hips against you, helping the process."
        the_girl "Oh god... Mfphhhh!"
    else:
        "She gasps as your tip slowly spreads her lips apart. She tries to pull away, but you pull on her waist and bring her closer."
        mc.name "Come on, you'll get there."
        "As you give it another try, you are making better progress, sliding the tip of your dick into [the_girl.title]'s wet tight cunt."
        the_girl "Oh god... Fuck!"
    "Inch by inch you slide your entire length into [the_girl.possessive_title]. She grunts and gasps the whole way down."
    "When you cannot go any deeper you give her some time to get used to your girth and length."
    the_girl "I think... I'm ready for you to move some more..."
    "You pull back a little bit and give her a few testing strokes. When she can handle those, you speed up, until you're thrusting your entire length."
    return

label standing_doggy_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s back is arched and she is moaning non-stop. Her ass quakes with every rapid thrust."
    the_girl "Oh god it's so good! Oh [the_girl.mc_title] I'm gonna cum!"
    "Hearing her call out your name is pushing you over the edge. You are about to cum too."
    mc.name "I'm cumming too!"
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her ass", "body"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside her":
        "[the_girl.possessive_title!c]'s drenched cunt is just too good. You decide to cum inside it."
        if mc.has_removed_condom:  #You sly dog
            "You know you should probably pull out after pulling the condom off, but you can't. You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum."
            the_girl "Oh god, you are cumming so hard, I swear I can feel you filling me up!"
            "You cum in unison with [the_girl.title]."
            $ the_girl.have_orgasm()
            $ the_girl.cum_in_vagina()
            $ standing_doggy.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock. A few drops of your cum start to drip out of her."
            "[the_girl.title] reaches between her legs and feels it, realising you just finished inside her."
            if the_girl.has_job(prostitute_job):
                if the_girl.on_birth_control or the_girl.is_infertile:
                    the_girl "What the FUCK? You took the condom off? And then came inside me!?! I know I'm just a working girl, but you can't treat me like this."
                else:
                    the_girl "What? You took the condom off? And then came inside me!?! Fuck, I could get pregnant, not all working girls take birth control, you asshole!"
                    $ the_girl.update_birth_control_knowledge()
                $ the_girl.change_stats(happiness = -5, love = -5, obedience = 3)
            elif the_girl.wants_creampie:         #She likes creampies...
                the_girl "Wait... that's... you took the condom off, didn't you? Oh fuck that's why it felt so good!"
                $ the_girl.discover_opinion("creampies")
                if the_girl.is_infertile or (the_girl.on_birth_control and not the_girl.is_pregnant):
                    the_girl "Oh god, that's so hot! I love feeling cum deep inside me."
                elif the_girl.knows_pregnant:
                    the_girl "So fucking hot! Bathe my pregnant womb with your hot cum!"
                else:
                    the_girl "Oh god that's so hot. You could knock me up you know? Next time be more careful!"
                $ the_girl.change_stats(happiness = 2, obedience = 3)
            elif the_girl.opinion.bareback_sex > 0:  #She is slutty enough she doesn't mind the cream filling
                the_girl "Oh my god you took the condom off? You know you can cum inside me anytime you want, no need to be sneaky about it!"
                $ the_girl.change_obedience(3)
            else:                                                   #She gets pissed
                if the_girl.on_birth_control or the_girl.is_infertile:
                    the_girl "What the FUCK? You took the condom off? And then came inside me!?! You asshole!"
                else:
                    the_girl "What the FUCK? You took the condom off? And then came inside me!?! I could get pregnant, asshole!"
                    $ the_girl.update_birth_control_knowledge()
                $ the_girl.change_stats(happiness = -5, love = -5, obedience = 3)
                "You planted your seed inside [the_girl.possessive_title], but it is clear she isn't happy about it."
            "You slowly pull out of [the_girl.title]. Your cum is dripping down her leg as you sit back."
        elif mc.condom:
            $ play_moan_sound()
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum. She moans when she feels you filling the condom deep inside her."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.have_orgasm()
            "Her cunt quivers as she joins you in orgasm. Her body goes rigid but you can feel the delicious pulsing as it feels like her body is trying to suck the condom off."
            "You wait until her orgasm has passed completely, then pull out and sit back. Your condom is bulged on the end where it is filled with your seed."
            $ the_girl.draw_person(position = the_girl.idle_pose)
            if (the_girl.opinion.drinking_cum > 1 and the_girl.sluttiness > 50) or the_girl.has_cum_fetish:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title!c] turns around and reaches for your cock. With delicate fingers she slides the condom off of you."
                the_girl "It would be a shame to waste all of this, right?"
                "She winks and brings the condom to her mouth. Squeezing all your cum right into her mouth."
                $ the_girl.change_slut(the_girl.opinion.drinking_cum, 70)
            else:
                "[the_girl.possessive_title!c] turns around and reaches for your cock. She removes the condom and ties the end in a knot, before throwing it away."
            "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
        else:
            $ play_moan_sound()
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum. She moans in time with each new shot of hot semen inside her."

            if the_girl.wants_creampie:
                the_girl "Yes! Fill me with your cum!"
            $ the_girl.have_orgasm()
            "You feel her [the_girl.pubes_description] pussy convulsing around your dick as she also starts to orgasm."
            $ the_girl.cum_in_vagina()
            $ standing_doggy.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish or the_girl.has_breeding_fetish:
                "[the_girl.possessive_title!c]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
            if the_girl.knows_pregnant:
                "[the_girl.possessive_title!c] groans deeply in pleasure, feeling your hot load spread inside her well-fucked pussy."
                the_girl "Oh, yeah, [the_girl.mc_title]... so hot... fill me with another hot load..."
                if the_girl.pregnancy_is_visible:
                    the_girl "That one made the baby kick!"
            elif the_girl.is_infertile:
                the_girl "Ah god... I just love your spunk deep inside me!"
            elif the_girl.opinion.bareback_sex > 0 and not the_girl.knows_pregnant:
                the_girl "Oh god... I can feel it so deep. I mean... it could... hopefully..."
                "[the_girl.possessive_title!c]'s voice starts to trail off."
            elif the_girl.wants_creampie:
                the_girl "Oh god, it's so deep."
            elif the_girl.on_birth_control:
                the_girl "Oh fuck... Good thing I'm on the pill..."
                $ the_girl.update_birth_control_knowledge()
            else:
                the_girl "Oh fuck... I could get pregnant you know..."
            "When you finish, you wait for a bit, revelling in the sensations as [the_girl.title]'s slick cunt has aftershocks."

            "You wait until her orgasm has passed completely, then pull out and stand back."

            if the_girl.has_breeding_fetish:
                "As your cum starts to leak out, [the_girl.possessive_title] reaches back and tries to keep it inside with her hand."
            else:
                "Your cum leaks out of her dripping wet pussy."

    elif the_choice == "Cum on her ass":
        if mc.condom and not mc.has_removed_condom:
            "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as you blow your load all over her ass."
            "She holds still for you as you cover her with your sperm."
        else:
            "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        $ the_girl.have_orgasm()
        "She reaches down and you see she is rapidly rubbing her clit as she begins to orgasm at the same time."
        if the_girl.opinion.being_covered_in_cum > 0:
                the_girl "Yes! Paint me with your sticky cum!"
        $ the_girl.cum_on_ass()
        $ standing_doggy.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title!c]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            $ play_moan_sound()
            "[the_girl.possessive_title!c] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly as her orgasm is enhanced by your bodyshot."
            "She truly is addicted to your cum."
        "After you finish, you watch as she slowly stops rubbing herself. Her body twitches once in a while from an aftershock."
        if the_girl.sluttiness > 90 or the_girl.opinion.being_covered_in_cum > 0:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."

    elif the_choice == "Cum on her face":
        mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
        if mc.condom and not mc.has_removed_condom:
            "You pull your cock out of [the_girl.possessive_title] with a satisfying pop. You pull your condom off as she turns around and gets on her knees in front of you."
        else:
            "You pull your cock out of [the_girl.possessive_title]. She immediately turns around and gets on her knees in front of you."
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.opinion.being_covered_in_cum > 0 or the_girl.opinion.cum_facials > 0:
            "[the_girl.possessive_title!c] reaches up with one hand, stroking you to finish. She reaches down with her other hand and begins to aggressively touch herself."
            $ the_girl.have_orgasm()
            "Your orgasm hits hard. Your first jet sprays across her face. Her expression is orgasmic bliss as she finishes at the same time."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish:
                "You can see [the_girl.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                $ play_moan_sound()
                "[the_girl.possessive_title!c] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                "She truly is addicted to your cum."
            else:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as your dick sprays jet after jet of seed across her face."
        elif the_girl.sluttiness > 80:
            "[the_girl.possessive_title!c] sticks out her tongue for you and holds still, eager to take your hot load."
            "She reaches down and begins to touch herself, bringing herself to orgasm at the same time as you."
            $ the_girl.have_orgasm()
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            $ climax_controller.do_clarity_release(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            the_girl "Oh god... it feels so good on my skin..."
        elif the_girl.sluttiness > 60:
            "[the_girl.possessive_title!c] closes her eyes and waits patiently for you to cum."
            "She reaches down and begins to touch herself, bringing herself to orgasm at the same time as you."
            $ the_girl.have_orgasm()
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            $ climax_controller.do_clarity_release(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.possessive_title!c] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            "She reaches down and begins to touch herself, bringing herself to orgasm at the same time as you."
            $ the_girl.have_orgasm()
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            $ climax_controller.do_clarity_release(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title!c] looks up at you from her knees, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")

    $ post_double_orgasm(the_girl)
    return
