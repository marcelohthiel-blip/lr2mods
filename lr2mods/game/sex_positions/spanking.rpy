#TODO transitions to standing anal

label intro_spanking(the_girl, the_location, the_object):
    "You stand behind [the_girl.title] and put your arms around her waist, pushing her so she is bending over the [the_object.name]."
    $ spanking.redraw_scene(the_girl)
    mc.name "Someone has been a bad girl. It's time for your punishment, [the_girl.title]."
    if the_girl.vagina_visible:
        "You don't waste any time and put your hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    else:
        mc.name "Let's get these out of the way first."
        $ the_girl.strip_to_vagina(position = spanking.position_tag, prefer_half_off = True)
        "You put both hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    return

label taboo_break_spanking(the_girl, the_location, the_object):
    mc.name "Someone has been a bad girl. It's time for your punishment, [the_girl.title]."
    the_girl "What... what are you gonna do to me?"
    mc.name "You need a spanking. It's only natural for a bad girl like you to get a spanking once in a while."
    the_girl "Oh god... I... Okay [the_girl.mc_title]..."
    $ spanking.redraw_scene(the_girl)
    "You stand behind [the_girl.title] and put your arms around her waist, pushing her so she is bending over the [the_object.name]."
    if the_girl.vagina_visible:
        "You don't waste any time and put your hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    else:
        mc.name "Let's get these out of the way first."
        $ the_girl.strip_to_vagina(position = spanking.position_tag, prefer_half_off = True)
        "You put both hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    return

label scene_spanking_1(the_girl, the_location, the_object):
    "You look down at [the_girl.possessive_title]'s ass. It is [the_girl.ass_spank_description]"
    $ the_girl.slap_ass()
    "You give her a solid spank. She lets out a little yelp."
    $ the_girl.slap_ass(update_stats = False)
    $ the_girl.slap_ass(update_stats = False)
    $ the_girl.slap_ass(update_stats = False)
    "You don't let up, giving her a solid spanking."
    if the_girl.spank_enjoyment_level > 5: #She loves it.
        the_girl "Oh god [the_girl.mc_title]! Give it to me good! Oh god!"
        "She is really getting into this. With each spank she wiggles her ass, giving you an enticing target."
    elif the_girl.spank_enjoyment_level > 0:
        the_girl "Oh... I'm sorry [the_girl.mc_title]! Oh god..."
        "She keeps her ass still, taking your blows. Her ass makes an enticing target."
    elif the_girl.spank_enjoyment_level > -5:
        the_girl "Ouch! I'm sorry [the_girl.mc_title]! That really hurts..."
        "With each spank, she flinches a bit."
    else:
        the_girl "Fuck! That hurts! Why are you doing this? Please stop!"
        "She's trembling. With each spank she flinches and quakes."
    if mc.arousal_perc < 20:
        $ mc.change_arousal(5)
    return

label scene_spanking_2(the_girl, the_location, the_object):
    $ play_spank_sound()
    "*{b}SMACK{/b}*"
    "You look at her bottom, deciding what to do next..."
    menu:
        "Continue spanking":
            call scene_spanking_1(the_girl, the_location, the_object) from _call_scene_spanking_1_from_scene_2
        "Rub her ass":
            "Instead of smacking her ass again, you start rubbing, it's [the_girl.ass_spank_description]"
            if the_girl.spank_enjoyment_level > 5:
                the_girl "Oh, that feels very nice, [the_girl.mc_title]."
                "She starts to move her ass, moving along with your rubbing motions."
            elif the_girl.spank_enjoyment_level > 0:
                the_girl "Oh... I didn't expect that [the_girl.mc_title]! Oh god..."
                "She keeps her ass motionless in order to minimize the discomfort."
            elif the_girl.spank_enjoyment_level > -5:
                the_girl "Ouch! I'm sorry [the_girl.mc_title]! I'm a little tender, could your rub a little softer..."
                "You soften your touch and softly rub her apple red buttocks."
            else:
                the_girl "Jesus! That hurts! Please stop, even a feather's touch would be too painful!"
                "She's trembling. With each touch of a finger her legs start shaking."

            $ the_girl.change_arousal(the_girl.spank_enjoyment_level * ((mc.foreplay_sex_skill / 10) + 1))

        "Finger her pussy" if the_girl.opinion.being_fingered > 0 and the_girl.vagina_available:
            "You slide your fingers in and out of her pussy, stroking the inside of that soft tunnel."
            $ play_moan_sound()
            "Each movement draws moans of pleasure from [the_girl.possessive_title], who presses herself against you."
            "She places one of her own hands over yours, encouraging you to speed up."
            the_girl "Just like that... Ah..."
            $ the_girl.change_arousal((the_girl.opinion.being_fingered + 1) * 5)

        "Finger Her pussy\n{menu_red}Must like being fingered{/menu_red} (disabled)" if the_girl.opinion.being_fingered <= 0 and the_girl.vagina_available:
            pass

        "Finger Her pussy\n{menu_red}Obstructed by clothing{/menu_red} (disabled)" if not the_girl.vagina_available:
            pass

        "Rub her pussy" if not the_girl.vagina_available and the_girl.are_panties_visible:
            "You slide your fingers over her underwear, feeling the damp spot of her arousal."
            $ play_moan_sound()
            "Each movement draws moans of pleasure from [the_girl.possessive_title], who presses herself against you."
            the_girl "Oh god... Ah..."
            $ the_girl.change_arousal(10)

        "Finger her ass" if the_girl.opinion.anal_sex > 0 and the_girl.vagina_available:
            "You slide your finger through her wet slit and move it up to her sphincter slightly lubricating it."
            the_girl "Oh god I love it when you do this..."
            "[the_girl.possessive_title!c] is pushing her ass against your finger, her breathing heavy, enticing you to keep going. You push your finger deep into her bowel."
            the_girl "Oh!!! [the_girl.mc_title] YES!"
            "You continue for a while. [the_girl.title] clearly enjoys the anal penetration. Eventually you pull your finger out and continue the punishment."
            $ the_girl.change_arousal(the_girl.opinion.anal_sex * 10)

        "Finger her ass\n{menu_red}Must like anal sex{/menu_red} (disabled)" if the_girl.opinion.anal_sex <= 0 and the_girl.vagina_available:
            pass

        "Finger her ass\n{menu_red}Obstructed by clothing{/menu_red} (disabled)" if not the_girl.vagina_available:
            pass

    if mc.arousal_perc < 20:
        $ mc.change_arousal(5)
    return


label outro_spanking(the_girl, the_location, the_object):
    pass #arousal is zero for MC. this shouldn't be possible
    return


label transition_default_spanking(the_girl, the_location, the_object):
    $ spanking.redraw_scene(the_girl)
    "You stand behind [the_girl.title] and put your arms around her waist, pushing her so she is bending over the [the_object.name]."
    mc.name "Someone has been a bad girl. It's time for your punishment, [the_girl.title]."
    if the_girl.vagina_visible:
        "You don't waste any time and put your hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    else:
        mc.name "Let's get these out of the way first."
        $ the_girl.strip_to_vagina(position = spanking.position_tag, prefer_half_off = True)
        "You put both hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    return

label strip_spanking(the_girl, the_clothing, the_location, the_object):
    the_girl "Oh my god... I'm so hot... I need to get this off!"
    $ the_girl.draw_animated_removal(the_clothing, position = spanking.position_tag)
    "She strips off her [the_clothing.name] while you're spanking her, moaning the whole time."
    return

label strip_ask_spanking(the_girl, the_clothing, the_location, the_object):
    the_girl "Everything feels so tight, I want to take it all off... Please can I?"
    "[the_girl.possessive_title!c] grabs onto her [the_clothing.name], waiting for you to tell her what to do."
    menu:
        "Let her strip":
            mc.name "Take it off."
            $ the_girl.draw_animated_removal(the_clothing, position = spanking.position_tag)
            "[the_girl.possessive_title!c] takes off her [the_clothing.name] and drops it to the side while you grope her ass."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl "Do you think I look sexy in it?"
            else:
                the_girl "Don't you think I would look better wearing your cum? That would be so fitting for your dirty little slut, wouldn't it?"
            return False

label orgasm_spanking(the_girl, the_location, the_object):
    the_girl "Oh god, oh god, oh... OH... OHHHH!"
    "Her whole body tenses up. You give her a few more spanks as she cums, just from the sensations of being spanked."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She quivers with pleasure for a few seconds before her whole body relaxes."
    the_girl "Ah... I'm sorry."
    mc.name "There you go, being bad again!"
    $ the_girl.slap_ass(update_stats = False)
    "You give her another hard spank."
    return

label transition_spanking_standing_doggy(the_girl, the_location, the_object):
    "You are done spanking her. You run your fingers along her slit a bit, getting a feel for how ready she is."
    mc.name "That's enough spanking [the_girl.title]. Now I'll make it feel all better."
    the_girl "Oh yes, [the_girl.mc_title], make me feel good."
    "You bounce your hard shaft on her ass a couple of times before sliding your cock between her thighs."
    "You continue your back and forth motion, rubbing your cock along her already wet pussy lips."
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

# when breaking the taboo we don't go into the default transition, so we use this custom label to trigger the transition dialogue
label transition_spanking_to_standing_doggy_taboo_break_label(the_girl, the_location, the_object):
    call transition_spanking_standing_doggy(the_girl, the_location, the_object) from _call_transition_spanking_to_standing_doggy_taboo_break_label
    return
