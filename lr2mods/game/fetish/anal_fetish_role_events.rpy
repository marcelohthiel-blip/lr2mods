
label fetish_anal_staylate_label(the_person):
    mc.name "[the_person.title], I need you to stay after work today."
    the_person "Oh, of course sir. I'm not in trouble am I?"
    "You give [the_person.possessive_title] a reassuring smile."
    mc.name "No, of course not, you are a wonderful asset to the company..."
    "You lower your voice and whisper in her ear so others don't overhear."
    mc.name "... but I might have to spank your ass a bit anyway."
    "You look [the_person.possessive_title] in the eyes. Her pupils dilate a bit as she realises the reasoning behind asking her to stay late."
    $ mc.change_locked_clarity(20)
    the_person "Oh! Thank you sir! I'll look forward to it!"
    "You say goodbye to [the_person.possessive_title]."
    $ add_fetish_anal_staylate_event(the_person)
    return

#SBA2
label fetish_anal_staylate_event_label(the_person):
    if not mc.is_at_office:
        "Your phone rings. It's [the_person.possessive_title]. You answer it."
        the_person "Hey, are you at work? I can't find you."
        "You forgot! You asked [the_person.possessive_title] to stay after work today."
        mc.name "Sorry, I had something come up and had to leave early."
        "[the_person.possessive_title!c] tries to mask disappointment in her voice but it is still obvious."
        the_person "Oh... okay... well try to let me know next time before I stay late. I thought... anyway, maybe some other time. Bye!"
        $ the_person.change_stats(happiness = -5, love = -2)
        return
    $ mc.change_location(ceo_office)
    "You finish up with your work for the day and return to your office. You are organizing some papers when [the_person.possessive_title] enters the room."
    $ set_special_fetish_outfit(the_person)
    $ the_person.draw_person()
    $ mc.change_locked_clarity(30)
    "From the look of her attire, she seems to have guessed the purpose of your meeting correctly."
    the_person "Hey [the_person.mc_title]. You wanted to see me?"
    mc.name "That's right. While your job performance has been ideal, it has recently come to my attention that you may not be of sound moral character."
    "[the_person.possessive_title!c] smiles slightly. She can see where you are going with this conversation."
    mc.name "I asked you to stay late so I could punish you properly for your misconduct. Now, I want you to bend over my desk to prepare for your punishment."
    the_person "Yes Sir!"
    $ the_person.draw_person(position = "standing_doggy")
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    "You approach [the_person.possessive_title] and begin to inspect her shapely ass. Nestled between her cheeks, you can see the pink jewel of her butt plug."
    "Below her plug, you can see the soft wet lips of her cunt. They are already flushed, showing a slight glisten of moisture. She is getting aroused just from presenting her ass to you."
    "She begins to wiggle her hips slightly in response to your intense gaze."
    the_person "Is everything to your satisfaction, sir?"
    "Should you reward her with your cock in her ass? Or spank it first?"
    menu:
        "Spank Her":
            $ the_person.slap_ass(update_stats = False)
            "Your hand lands a firm blow on her supple ass. Her knees buckle a bit and she arches her back, surprised by the sudden blow."
            mc.name "Quiet slut! You will speak only when spoken to. Do you understand?"
            the_person "Yes sir!"
            "You murmur a soft approval. You give her ass another hard spank."
            $ the_person.slap_ass()
            "[the_person.possessive_title!c]'s accommodating ass ripples in shock waves out from where you hand spanks it."
            "You give her hind quarters a few more spanks, giving her few seconds in between."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(50)
            "[the_person.possessive_title!c] barely stifles a moan as you spank her again. Her cheeks are beginning to glow a rosy red. Her pussy lips are growing puffy with clear signs of arousal."
            "You decide it is time to move on."
        "Fuck Her Ass":
            "You firmly grasp one of her ass cheeks in one hand before responding."
            mc.name "Everything seems to be in order, but I'll still need to carry out your punishment."
            "With two fingers, you start to pull the jewelled plug from her. When only the tip remains, you push it back in."
            the_person "Oh! Whatever you think is best sir..."
            "You fuck her for a few moments with the jewelled plug. She loves the penetration and begins to push her hips back against you as you work the plug in and out of her."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(50)
            mc.name "Now, I think it is time for something a bit more substantial than the plug..."
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.opinion.anal_sex)
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title!c] tries to push back against you and begins to beg."
            the_person "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            $ the_person.break_taboo("anal_sex")
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_SBA20
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] lays over the desk for a while, recovering from her ass reaming."
                the_person "God... that felt so fucking good..."
                $ the_person.change_stats(happiness = 5, obedience = 5)
                call check_fetish_trance(the_person, "anal-fetish") from _call_check_fetish_trance_fetish_anal_staylate_event
            else:
                the_person "Okay... I guess we're done already?"
                "[the_person.possessive_title!c] seems disappointed she didn't finish."
                $ the_person.change_stats(happiness = -5, love = -2)
            $ the_person.draw_person()
            "[the_person.possessive_title!c] gets up and starts getting ready to go home."
            "You say goodbye to her as she walks out your office door."
            return
    menu:
        "Fuck Her Ass":
            "You firmly grasp one of her ass cheeks in one hand. It is hot to the touch."
            "With two fingers, you start to pull the jewelled plug from her. When only the tip remains, you push it back in."
            "You fuck her for a few moments with the jewelled plug. She loves the penetration and begins to push her hips back against you as you work the plug in and out of her."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(50)
            mc.name "Now, I think it is time for something a bit more substantial than the plug..."
            "You slowly pull out the pink jewelled butt plug from [the_person.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_person.change_arousal(the_person.opinion.anal_sex * 5)
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_person.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_person.possessive_title!c] tries to push back against you and begins to beg."
            the_person "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            $ the_person.break_taboo("anal_sex")
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_SBA21
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] lays over the desk for a while, recovering from her ass reaming and spanking."
                the_person "God... that felt so fucking good..."
                $ the_person.change_stats(happiness = 5, obedience = 5)
                $ the_person.draw_person()
                call check_fetish_trance(the_person, "anal-fetish") from _call_check_fetish_trance_fetish_anal_staylate_event_2
            else:
                the_person "Okay... I guess we're done already?"
                "[the_person.possessive_title!c] seems disappointed she didn't finish."
                $ the_person.change_stats(happiness = -5, love = -2)
            $ the_person.draw_person()
            "[the_person.possessive_title!c] gets up and starts getting ready to go home."
            "You say goodbye to her as she walks out your office door. She walks a bit funny, clearly uncomfortable after the spanking she received."
        "Send her home":
            mc.name "That's enough for today [the_person.title]."
            "[the_person.possessive_title!c] looks back at you, clearly surprised that you are sending her away already."
            the_person "What? I mean, already? Okay..."
            "She grabs her stuff and quickly makes an exit from your office."
            $ the_person.change_stats(happiness = -5, love = -2, obedience = 5)
    return
