label intro_standing_dry_sex(the_girl, the_location, the_object):
    $ standing_dry_sex.redraw_scene(the_girl)
    "[the_girl.title] puts her arms around your neck as you reach down and grab her ass, pulling her close to you."
    "She gasps when she feels your erection pressing up against her body."
    the_girl "Oh my god… you feel so hard… mmm…"
    if the_girl.vagina_available:
        "She lifts her leg up slightly. With two hands on her ass you start to grind your cock against her bare crotch."
    else:
        "She lifts her leg up slightly. With two hands on her ass you start to grind your cock against her crotch."
    "A soft moan escapes her lips as you begin to grind against her."
    return

label taboo_break_standing_dry_sex(the_girl, the_location, the_object):
    "She puts her arms around your neck as you reach down and grab her ass, pulling her close to you."
    "She gasps when she feels your erection pressing up against her body."
    $ the_girl.call_dialogue(f"{standing_dry_sex.associated_taboo}_taboo_break")
    $ standing_dry_sex.redraw_scene(the_girl)
    if the_girl.vagina_available:
        "She lifts her leg up slightly. With two hands on her ass you start to grind your cock against her bare crotch."
    else:
        "She lifts her leg up slightly. With two hands on her ass you start to grind your cock against her crotch."
    "A soft moan escapes her lips as you begin to grind against her."
    return

label scene_standing_dry_sex_1(the_girl, the_location, the_object):
    $ play_moan_sound()
    # Scene: Girl talks dirty in your ear a bit
    if the_girl.love >= 20:
        "[the_girl.possessive_title!c] moans in your ear, holding you tight as you grind up against her."
        "A shiver runs down your spine as she starts to kiss you on the back of your ear and down your neck."
        $ mc.change_locked_clarity(20)
    else:
        "[the_girl.possessive_title!c] moans in your ear as you grind up against her."
        $ the_girl.call_dialogue("sex_responses_foreplay")
    if the_girl.is_willing(against_wall, slut_bonus = 10): #With 10 bonus she would be eager to fuck
        the_girl "Mmmm, your cock feels so good."
        if the_girl.arousal_perc >= 60 and (the_girl.vagina_available or the_girl.can_remove_panties) and not the_girl.has_taboo("vaginal_sex"):
            "She whispers in your ear again."
            the_girl "You should just pull it out and slide it up inside me, just like this..."
            $ mc.change_locked_clarity(20)
            "Welp, [the_girl.possessive_title] is literally asking you to fuck her."
            menu:
                "Fuck her":
                    mc.name "I should have known a slut like you wouldn't need much of a warmup."
                    "You set her down for a moment while you pull your cock out. She licks her lips when she sees you pull it out."
                    if the_girl.can_remove_panties:
                        "[the_girl.possessive_title!c] pulls her panties to the side as you grab her ass again."
                        # Need code here for pulling panties to the side
                    else:
                        "You step into her and grab her ass again."
                    $ new_object = girl_choose_object(the_girl, against_wall)
                    "You pick her up and move over to the [new_object.name], pushing her up against it."
                    "[the_girl.title] plants her back against it with her legs wide open."
                    "You run the tip of your cock along her slit a few times, then slide yourself inside her tight cunt."
                    return (against_wall, new_object)
                "Stay like this":
                    mc.name "Enticing, but I want to take things a little slower right now."
                    the_girl "Mmm, okay. If that's what you want. It feels so hard, I'm getting so turned on..."
        else:
            mc.name "It'll feel even better when I slide it inside your slutty little cunt."
            the_girl "Mmm, I can't wait..."
    else:
        the_girl "It feels so hard, god it's turning me on..."
    "[the_girl.title]'s breath and moans tickle your ear as you thrust up against her."
    return

label scene_standing_dry_sex_2(the_girl, the_location, the_object):
    # Scene: Grind and squeeze her ass instead of thrusting for a bit.
    "You stop thrusting for a moment and grope her ass."
    "Instead of thrusting, you move her hips in a circular motion, grinding her pussy up against you."
    $ play_moan_sound()
    if the_girl.vagina_available:
        "You can feel that heat and moisture from [the_girl.possessive_title!c]'s exposed pussy growing."

    else:   #Make a comment about wishing she had less clothes on. Then check and see if she would be into it.
        the_girl "So good..."
        mc.name "It would feel even better if you took something off."
        if the_girl.effective_sluttiness() >= 50:   #She immediately agrees
            the_girl "You're right... why am I even wearing anything right now, anyway? Give me a second..."
            $ the_girl.strip_to_vagina(prefer_half_off = False)
            "She quickly strips out of her bottoms."
            $ standing_dry_sex.redraw_scene(the_girl)
            $ the_girl.change_arousal(the_girl.opinion.showing_her_ass * 3)
            $ the_girl.discover_opinion("showing her ass")
            $ the_girl.break_taboo("bare_pussy")
        elif the_girl.effective_sluttiness() >= 30: #She's hesitant but agrees, with lower sluttiness than normally require to strip her down due to the foreplay
            the_girl "Ohh... Yeah... it probably would..."
            "She bites her lip for a moment, considering your statement."
            the_girl "Okay... give me a moment!"
            "You set her down for a second and strips out of her bottoms."
            $ the_girl.strip_to_vagina(prefer_half_off = False)
            "She quickly strips out of her bottoms."
            $ standing_dry_sex.redraw_scene(the_girl)
            $ the_girl.change_arousal(the_girl.opinion.showing_her_ass * 3)
            $ the_girl.discover_opinion("showing her ass")
            $ the_girl.break_taboo("bare_pussy")
        else:   #She thinks about it but declines
            the_girl "Ahh... you're probably right..."
            "She seems to consider it for a moment."
            if the_girl.has_taboo("bare_pussy"):
                the_girl "I don't want you to see me naked, that would just be too much."
            else:
                mc.name "It's nothing I haven't seen before."
                the_girl "I know, I'm just not ready to do that while we are embracing like this."
            $ the_person.change_slut(1, 30)
            "You can tell the idea excites her a bit, but she isn't ready to take anything off right now."
            "Instead, you grope her ass through her clothes a bit, enjoying her curves, then go back to thrusting up against her."
            return
        # Someday, have a marker for whether or not MC is exposed. For now, we assume his cock is in his pants.
        "With her pussy now exposed, you resume grinding up against her, with only your trousers between you."

    return

label scene_standing_dry_sex_3(the_girl, the_location, the_object):
    # Scene: Take a moment to play with her tits
    if the_girl.tits_available:
        "You stop thrusting for a moment and use a free hand to play with [the_girl.possessive_title]'s tits."
        if the_girl.has_large_tits:
            "[the_girl.title]'s big tits are a pleasure to grope. Wonderful handfuls for you to knead and tease."
        else:
            "You run a hand over [the_girl.possessive_title]'s cute little tits, pausing to pinch one of her nipples."
        "[the_girl.title] arches her back, pushing her tits up for you to enjoy."
    else:
        "You stop thrusting for a moment and use a free hand to play with [the_girl.possessive_title]'s tits through her clothes."
        mc.name "Your tits are great... may I?"
        "You put your hand on her clothing, indicating you want to strip her top."
        if the_girl.effective_sluttiness() >= 40:   #She immediately agrees
            the_girl "Of course! Let's get this off..."
            "[the_girl.title] cooperates eagerly as you strip her out of her top."
            $ the_girl.strip_to_tits(prefer_half_off = False)
            if the_girl.has_large_tits:
                "When the last piece of clothing is removed, her big tits drop free, jiggling for a few enticing moments."
                # Maybe add an option to fuck her tits here, as a conditional transition?
            else:
                "Her perky tits drop free as you take her top off."
            $ standing_dry_sex.redraw_scene(the_girl)
            $ the_girl.change_arousal(the_girl.opinion.showing_her_tits * 3)
            $ the_girl.discover_opinion("showing her tits")
            $ the_girl.break_taboo("bare_tits")
        elif the_girl.effective_sluttiness() >= 20: #She's hesitant but agrees, with lower sluttiness than normally require to strip her down due to the foreplay
            the_girl "Ohh geeze. I don't know..."
            "She bites her lip for a moment, considering your statement."
            the_girl "Okay... but only becuase you asked so politely!"
            "[the_girl.title] cooperates as you help strip her out of her top."
            $ the_girl.strip_to_tits(prefer_half_off = False)
            if the_girl.has_large_tits:
                "When the last piece of clothing is removed, her big tits drop free, jiggling for a few enticing moments."
            else:
                "Her perky tits drop free as you take her top off."
            $ standing_dry_sex.redraw_scene(the_girl)
            $ the_girl.change_arousal(the_girl.opinion.showing_her_tits * 3)
            $ the_girl.discover_opinion("showing her tits")
            $ the_girl.break_taboo("bare_tits")
        else:   #She thinks about it but declines
            the_girl "Oh! Ummm, I don't think that would be appropriate..."
            "You give her tits another squeeze."
            if the_girl.has_taboo("bare_tits"):
                the_girl "I don't want you to see my tits, that would just be too much."
            else:
                mc.name "It's nothing I haven't seen before."
                the_girl "I know, I'm just not ready to do that while we are embracing like this."
            $ the_person.change_slut(1, 30)
            "You can tell the idea excites her a bit, but she isn't ready to take anything off right now."
            "Instead, you grope her tits through her clothes a bit, enjoying her curves, then go back to thrusting up against her."
            return
        $ play_moan_sound()
        "With her tits exposed, you spend several seconds groping her, even lowering your face and sucking on a nipple for a few moments."
        "Satisfied for now, you put your hands back on her ass and start to thrust up against her again."
    return

label outro_standing_dry_sex(the_girl, the_location, the_object):
    "Grinding your cock against [the_girl.title]'s body is enough to push you that little bit farther, past the point of no return."
    $ climax_controller = ClimaxController(["Cum in your pants.", "air"])
    $ the_choice = climax_controller.show_climax_menu()
    $ climax_controller.do_clarity_release(the_girl)
    "She looks surprised as your start to cum."
    the_girl "Are you cumming?"
    mc.name "Yes!"
    "She wraps her arms around you and grinds her body agaainst you as you cum, pumping your load out into your pants."
    the_girl "Wow, that was hot..."
    return

label transition_standing_dry_sex_standing_fingering(the_girl, the_location, the_object):
    if the_girl.vagina_available:
        "You pet [the_girl.title]'s pussy, then slide two fingers inside it. She gasps as they slip inside."
    else:
        $ the_item = the_girl.outfit.get_lower_top_layer
        if the_item:
            "You slide a hand under her [the_item.display_name], bringing your hand right to her pussy."
            "She gasps as you tease it with two fingers, then slip them inside the wet hole."
            $ the_item = None
        else:
            "You pet [the_girl.title]'s pussy, then slide two fingers inside it. She gasps as they slip inside."
    the_girl "Oh [the_girl.mc_title]... Ah..."
    return

label transition_default_standing_dry_sex(the_girl, the_location, the_object):
    $ standing_dry_sex.redraw_scene(the_girl)
    "[the_girl.title] puts her arms around your neck as you reach down and grab her ass, pulling her close to you."
    if the_girl.vagina_available:
        "She lifts her leg up slightly. With two hands on her ass you start to grind your cock against her bare crotch."
    else:
        "She lifts her leg up slightly. With two hands on her ass you start to grind your cock against her crotch."
    "A soft moan escapes her lips as you begin to grind against her."
    return

label strip_standing_dry_sex(the_girl, the_clothing, the_location, the_object):
    the_girl "Your body feel amazing... Oh my god..."
    the_girl "I need to feel more..."
    $ the_girl.draw_animated_removal(the_clothing, position = standing_dry_sex.position_tag)
    "You pause while she awkwardly strips off her [the_clothing.name], then continue humping her."
    return

label strip_ask_standing_dry_sex(the_girl, the_clothing, the_location, the_object):
    the_girl "I want to feel you touch me everywhere... Can I take off my [the_clothing.name] for you?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = standing_dry_sex.position_tag)
            "You watch while [the_girl.possessive_title] takes off her [the_clothing.name] and drops it to the side."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl "Do you think I look sexy in it?"
            else:
                the_girl "Don't you think I would look better wearing your cum? That would be so fitting for your dirty little slut, wouldn't it?"
            return False

label orgasm_standing_dry_sex(the_girl, the_location, the_object):
    "You feel [the_girl.possessive_title] tense up in your arms as you thrust up against her."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She quivers with pleasure for a few seconds before her whole body relaxes."
    the_girl "Ah... Keep going... I might be able to cum again!"
    return

label standing_dry_sex_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] is holding tightly to you. She is moaning with every thrust."
    the_girl "It's so good... I'm gonna cum!"
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. You are going to cum."
    mc.name "Me too!"

    $ climax_controller = ClimaxController(["Cum in your pants.", "air"])
    $ the_choice = climax_controller.show_climax_menu()
    $ climax_controller.do_clarity_release(the_girl)
    "She wraps her arms around you and grinds her body agaainst you as you cum, pumping your load out into your pants."
    "[the_girl.possessive_title!c]'s entire body starts to twitch and she cries out as she starts to cum with you."
    $ the_girl.have_orgasm()
    "After several seconds, you both stop grinding, your mutual orgasms leaving you in a post orgasmic bliss."
    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
