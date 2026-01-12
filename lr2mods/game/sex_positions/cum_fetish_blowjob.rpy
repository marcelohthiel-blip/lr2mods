label intro_cum_fetish_blowjob(the_girl, the_location, the_object):
    "[the_girl.possessive_title!c] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    if mc.condom:
        the_girl "Why are you wearing this thing? Let's take this off so I can take care of you better..."
        "[the_girl.possessive_title!c] pulls off your condom."
        $ mc.condom = False
    the_girl "How about I take care of this for you?"
    "[the_girl.possessive_title!c] looks up at your from her knees. She looks you right in the eyes as she leans forward and slides her lips over the tip of your dick."
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    return

label scene_cum_fetish_blowjob_1(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title!c] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    $ play_moan_sound()
    "She moans slightly as she strokes you with her soft, velvet lips."
    menu:
        "Talk dirty to her":
            mc.name "You are such a good cum slut. You are so eager to suck that cum straight out of me, aren't you?"
            "[the_girl.possessive_title!c] strokes you a few more times with her skilled mouth. She twirls her tongue around the tip a few times before taking a second to respond."
            the_girl "Mmm, it's been too long since you fed me... I can't wait to feel your cum sliding down my throat..."
            the_girl "... or maybe I'll pull off and stroke you while you cover my face in your hot cum..."
            "She slips you back into her mouth and resumes blowing you."
        "Stay quiet":
            "You rest your hand on her head, guiding her as she sucks you off."
            "With a little encouragement, you pull [the_girl.possessive_title]'s head down a little farther with each stroke."
            if the_girl.opinion.masturbating > 0:
                if the_girl.vagina_available:
                    "[the_girl.possessive_title!c] puts a hand between her legs and starts to touch herself while she blows you."
                    $ the_girl.change_arousal(the_girl.opinion.masturbating)
                    $ the_girl.discover_opinion("masturbating")
                    if the_girl.arousal_perc > 60:
                        $ play_moan_sound()
                        "Her moans are muffled by your cock when she slides a finger into her [the_girl.pubes_description] pussy and starts to finger herself."
                    else:
                        "She rubs her clit with her middle finger, making little circles around the sensitive nub."
                else:
                    if the_girl.arousal_perc > 60:
                        "[the_girl.possessive_title!c] puts a hand between her legs and eagerly rubs at her crotch through her clothing."
                    else:
                        "[the_girl.possessive_title!c] puts a hand between her legs and rubs at her crotch absentmindedly."
            else:
                "[the_girl.possessive_title!c] keeps up a steady pace, bobbing her head back and forth and running your cock in and out of her soft mouth."

    return

label scene_cum_fetish_blowjob_2(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = None
    $ cum_fetish_blowjob.redraw_scene(the_girl)

    "[the_girl.possessive_title!c] pulls your cock out of her mouth and leans in even closer. She runs her tongue along the bottom of your shaft, pausing at the top to kiss the tip a few times."
    the_girl "Mmm, I can't wait until your cock throbs and your sweet, sticky cum is shooting out..."
    mc.name "Of course you can't wait. You are my perfect little cum slut."
    "When [the_girl.possessive_title] opens her mouth and resumes blowing you, you put your hand on the back of her head, intending to push yourself down her throat."
    if the_girl.is_submissive:
        "[the_girl.possessive_title!c] looks up at you. You can see her pupils dilate as you slowly pull her head towards you, until your cock is buried in her throat."
        $ play_gag_sound()
        "[the_girl.possessive_title!c]'s knees quiver while her throat spasms around your shaft. You hold her deep while her body twitches with pleasure."
        "You let go of her head and she slowly comes up for air."
        the_girl "Oh god you taste so good. You can fuck my throat if you want to, just promise me you'll warn me before you cum..."
        the_girl "... I want to wear your cum all over my face, like a good slut!"
        the_girl "I want to walk around the rest of the day with it obvious to everyone who sees me that you've blown your load all over me..."
        $ the_girl.discover_opinion("cum facials")
        "Turned on by her filthy words, you grab the back of her head with both hands and force your dick right back down her throat."
        "You fuck her face roughly. Her throat makes vulgar suction noises with each thrust, and you can see her throat bulging slightly."
        $ the_girl.change_arousal(the_girl.opinion.being_submissive * 2)
    elif the_girl.is_dominant:
        "[the_girl.possessive_title!c] grabs your hands in hers. She holds your hands as she looks up at you, making eye contact."
        "With her hands holding yours, she opens her mouth wide and descends on your cock."
        "She bottoms out and her nose is touching your pubic hair. You are balls deep down her throat."
        mc.name "Mmmm, that's it bitch. Take it deep!"
        "Still making eye contact, [the_girl.possessive_title] begins to bob her head up and down, completely deep throating you with every stroke."
        "Every few strokes you can feel the soft rumble of a moan, being stifled by your length she keeps impaling her throat on."
        $ the_girl.discover_opinion("taking control")
        $ the_girl.change_arousal(the_girl.opinion.taking_control * 2)
    else:
        $ play_gag_sound()
        "[the_girl.possessive_title!c] turns her eyes up and meets your gaze. She eagerly swallows as you push yourself down her throat, her tongue eagerly licking at the bottom of your shaft."
        mc.name "Fuck that feels good [the_girl.title]."
        "In response she bottoms out on your dick. She rocks her head left and right, grinding her face into your crotch to take as much of your length as possible."
        "She tenses and relaxes her throat rhythmically, gently massaging your shaft with it."
        "You moan at the intense sensations.You let go of her head and she slowly comes up for air."
        the_girl "Oh god you taste so good. Just promise me you'll warn me before you cum..."
        the_girl "... I want to wear your cum all over my face, like a good slut!"
        the_girl "I want to walk around the rest of the day with it obvious to everyone who sees me that you've blown your load all over me..."
        $ the_girl.discover_opinion("cum facials")
        "Your cock twitches in response to her filthy words. She notices and quickly opens her mouth and take you deep again."
    return

label outro_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    "Little by little the soft, warm mouth of [the_girl.possessive_title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
    mc.name "Fuck, here I come!"

    # if the_girl.has_cum_fetish or the_girl.opinion.drinking_cum > the_girl.opinion.cum_facials:
    #     "[the_girl.possessive_title!c] moans and looks you in the eyes. She pulls off until just the tip of your cock is in her mouth and she begins to stroke out off eagerly."
    #     "You erupt in orgasm into her greedy mouth. Her pupils dilate as her cum-addicted brain registers the presence of your cum in her mouth."
    #     "[the_girl.possessive_title!c] is moaning uncontrollably around your twitching cock."
    #     $ the_girl.cum_in_mouth()
    #     $ cum_fetish_blowjob.redraw_scene(the_girl)
    #     if the_girl.arousal_perc > 100:
    #         "[the_girl.possessive_title!c]'s legs quiver as she convulses. She is so addicted to your cum, blowing in her mouth has set off another orgasm for her."
    #         $ the_girl.change_obedience(5*the_girl.opinion.drinking_cum)
    #     "Once you've had a second to recover, [the_girl.possessive_title] closes her mouth and swallows loudly. It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
    #     $ cum_fetish_blowjob.current_modifier = None
    #     $ cum_fetish_blowjob.redraw_scene(the_girl)
    #     $ the_girl.call_dialogue("cum_mouth")
    $ cum_fetish_blowjob.current_modifier = None
    $ the_girl.draw_person(position = "kneeling1")
    $ play_moan_sound()
    "[the_girl.possessive_title!c] moans and looks you in the eyes. She pulls off your cock and strokes you eagerly, waiting for the first splash across her face."
    "You erupt in orgasm and shoot your load across her glowing face. Her pupils dilate as her cum-addicted brain registers the presence of your cum on her skin."
    $ play_moan_sound()
    "[the_girl.possessive_title!c] moans uncontrollably with every spurt."
    $ the_girl.cum_on_face()
    $ the_girl.draw_person(position = "kneeling1")
    $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_girl)
    "Slowly recovering, you look at [the_girl.possessive_title]'s cum-covered face. Her eyes are closed and she is absentmindedly playing with some of the cum that is starting to run down her neck."
    the_girl "Yes... it's so hot... It feels so good on my skin..."
    return

label transition_default_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    if mc.condom:
        the_girl "Why are you wearing this thing? Let's take this off so I can take care of you better..."
        "[the_girl.possessive_title!c] pulls off your condom."
        $ mc.condom = False
    "[the_girl.possessive_title!c] gets onto her knees in front of you and takes your hard cock in her hands. She strokes it tentatively a few times, then leans in and slides the tip into her mouth."
    mc.name "That's it, that's a good girl."
    return

label transition_blowjob_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    if mc.condom:
        the_girl "Why are you wearing this thing? Let's take this off so I can take care of you better..."
        "[the_girl.possessive_title!c] pulls off your condom."
        $ mc.condom = False
    the_girl "Mmm, I going to drain every drop of cum from your balls!"
    mc.name "That's it, that's a good girl."
    return

label strip_cum_fetish_blowjob(the_girl, the_clothing, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = None
    $ cum_fetish_blowjob.redraw_scene(the_girl)

    "[the_girl.possessive_title!c] pops off your cock and looks up at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = cum_fetish_blowjob.position_tag)
    "[the_girl.possessive_title!c] strips off her [the_clothing.name]. She drops it to the ground, then gets back on her knees and slides your cock inside her mouth."
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    return

label strip_ask_cum_fetish_blowjob(the_girl, the_clothing, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = None
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    $ return_value = True

    "[the_girl.possessive_title!c] pops off your cock and looks up at you from her knees."
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = cum_fetish_blowjob.position_tag)
            "[the_girl.possessive_title!c] strips out of her [the_clothing.name]. Then she gets back to work sliding your cock all the way to the back of her mouth."

        "Leave it on":
            mc.name "No, I like how you look with it on."
            the_girl "Is it sexy? Does it make you just want to blow your load, looking at me wearing this?"
            "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
            $ return_value = False

    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    return return_value

label orgasm_cum_fetish_blowjob(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title!c] pauses suddenly. You hear her whimper softly, the noise partly muffled by your cock."

    "[the_girl.possessive_title!c] starts to pull back off of your cock. You place a firm hand on the back of her head."
    mc.name "Did I tell you to stop sucking, you dirty little slut?"
    "You push her back down, hard. [the_girl.possessive_title!c] keeps her mouth open wide and fits you all the way in, quivering as she climaxes."
    mc.name "A cock sleeve like you deserves to have her throat stuffed when she cums."
    if the_girl.is_submissive:
        if the_girl.sluttiness < cum_fetish_blowjob.slut_cap:
            $ the_girl.change_slut(the_girl.opinion.being_submissive) #If she likes being submissive this makes her cum and become sluttier super hard.
        $ the_girl.change_obedience(2*the_girl.opinion.being_submissive)
        $ play_gag_sound()
        "[the_girl.possessive_title!c] closes her eyes tight. You can feel her throat spasm around your shaft in time with her orgasmic contractions."
        $ the_girl.have_orgasm()
        if the_girl.vagina_visible:
            "You can see that [the_girl.possessive_title]'s pussy is dripping wet as she cums."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer
            if the_item and the_item.underwear:
                "[the_girl.possessive_title!c]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [the_item.display_name]."
            else:
                "[the_girl.possessive_title!c] clenches her thighs together and rides out her orgasm."
            $ the_item = None
        $ cum_fetish_blowjob.current_modifier = None
        $ cum_fetish_blowjob.redraw_scene(the_girl)
        "When she's stopped twitching and moaning you let [the_girl.possessive_title] slide back. She pants loudly, then licks along the length of your cock."
        the_girl "That was... incredible... Okay, I came... now it's your turn!"
        "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
    else:
        $ the_girl.have_orgasm()
        "[the_girl.possessive_title!c] closes her eyes as her orgasm peaks. She holds almost perfectly still, your dick still sitting in her mouth, until she's finished."
        $ cum_fetish_blowjob.current_modifier = None
        $ cum_fetish_blowjob.redraw_scene(the_girl)
        "She pulls off and takes a long, deep breath."
        $ the_girl.change_stats(happiness = 2, obedience = 1)
        the_girl "Wow, that was amazing... Okay, I came... now it's your turn!"
        "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."

    return

label cum_fetish_blowjob_double_orgasm(the_girl, the_location, the_object):
    $ cum_fetish_blowjob.current_modifier = "blowjob"
    $ cum_fetish_blowjob.redraw_scene(the_girl)
    "[the_girl.title] pulls back on your cock, almost letting it fall out of her mouth. She closes her eyes and quivers slightly."
    "But the warm, tight feeling of [the_girl.title]'s throat sliding back from your shaft pulls you closer to orgasm. You feel yourself pass the point of no return and let out a soft moan."

    $ climax_controller = ClimaxController(["Cum on her face", "face"], ["Cum down her throat", "throat"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        $ cum_fetish_blowjob.current_modifier = None
        $ the_girl.draw_person("kneeling1")
        "You take a step back, pulling your cock out of [the_girl.possessive_title]'s throat with a satisfyingly wet pop, and take aim at her face."
        $ climax_controller.do_clarity_release(the_girl)
        "[the_girl.title] sticks out her tongue and rubs her [the_girl.pubes_description] pussy while waiting for your hot load."
        $ the_girl.cum_on_face()
        $ the_girl.draw_person(position = "kneeling1")
        "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.title]'s face and into her open mouth, all the while rubbing her wet clit."
        $ the_girl.have_orgasm()
        "You hear her whimper as her cum fetish is satisfied."
        "You take a deep breath to steady yourself once you've finished cumming."
        "[the_girl.possessive_title!c] looks up at you from her knees, rubbing your cum all over her face while licking her fingers when they reach her mouth."

    elif the_choice == "Cum down her throat":
        "You put your hands on the back of [the_girl.title]'s head and pull her back down onto your shaft, hard."
        mc.name "Keep that dick in your throat you dirty little cum slut!"
        "[the_girl.possessive_title!c] keeps her mouth wide open for you, moaning hard waiting for her cum desire being satisfied."

        "You grunt and twitch as you start to empty your balls down her oesophagus."
        $ the_girl.have_orgasm()
        if the_girl.vagina_visible:
            "You can see that [the_girl.title]'s pussy is dripping wet as she starts shaking and enjoying her own fetish fuelled orgasm."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer
            if the_item.underwear:
                "[the_girl.title]'s trembling wet pussy has soaked her [the_item.display_name], and it drips fluid as she cums."
            else:
                "[the_girl.title] clenches her thighs together and rides out her fetish fuelled orgasm."
                $ the_item = None

        $ cum_fetish_blowjob.current_modifier = None
        $ the_girl.cum_in_mouth()
        $ cum_fetish_blowjob.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        "You keep on sliding your dick down her tight throat, coating her entire mouth with your cum, until she finishes twitching."
        "When she's finished cumming you let [the_girl.title] pull back off your shaft. She gasps loudly for air."
        the_girl "Oh my god [the_girl.mc_title], I love it when you feed me your cum!"
        "All the while scooping up and tasting the the cum that escaped her mouth."

    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return


label taboo_break_cum_fetish_blowjob(the_girl, the_location, the_object):
    # TODO: Add custom taboo break
    return
