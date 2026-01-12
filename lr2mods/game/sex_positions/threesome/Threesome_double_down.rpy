#Girl one cowgirl while girl two sits on MC's face

transform Threesome_double_down_girl_one_transform():
    yalign 0.40
    yanchor 0.5
    xalign 1.0
    xanchor 1.0
    zoom 0.8

transform Threesome_double_down_girl_two_transform():
    yalign 0.57
    yanchor 0.5
    xalign 1.07
    xanchor 1.0
    zoom 1.4 #Her ass is in your face!

label intro_threesome_double_down_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "You lay down on your back as the girls get into position."
    if not the_girl_1.vagina_visible:
        "[the_girl_1.title] quickly moves some clothing out of the way..."
        $ the_girl_1.strip_to_vagina(position = Threesome_double_down.position_one_tag, display_transform = Threesome_double_down.p1_transform, prefer_half_off = True)
    $ the_girl_1.break_taboo("vaginal_sex")
    $ the_girl_1.break_taboo("condomless_sex")
    "You briefly see [the_girl_1.title] sigh as she sinks down onto your cock, before [the_girl_2.possessive_title] swings a leg over your head."

    if not the_girl_2.vagina_visible:
        "[the_girl_2.title] quickly moves some clothing out of the way..."
        $ the_girl_2.strip_to_vagina(position = Threesome_double_down.position_two_tag, display_transform = Threesome_double_down.p2_transform, prefer_half_off = True)
    "With both girls on top of you, you waste no time diving into [the_girl_2.title]'s pussy."
    return

label scene_threesome_double_down_fuck_girl_one_1(the_girl_1, the_girl_2, the_location, the_object):
    #Scene: Make things rough. Spank her ass while she and the other girl play with each other.
    "You run your tongue up and down [the_girl_2.title]'s slit, lapping up her juices, before plunging your tongue inside her."
    "[the_girl_1.title]'s ass is making lewd smacking noises as she rides you roughly."
    the_girl_2 "Mmm, that's it [the_girl_2.mc_title]."
    "[the_girl_2.title] is pushing her pussy back against your face, smothering you with her pussy."
    "The girls are getting rough with you, so you decide it's time to get a little rough back!"
    menu:
        "Spank [the_girl_2.title]":
            "You reach your hand up to [the_girl_2.title]'s ass and grope it for a moment, then give it a hard spank."
            $ the_girl_2.slap_ass(update_stats = False)
            the_girl_2 "Oh! Am I being bad [the_girl_2.mc_title]?"
            $ the_girl_2.slap_ass(update_stats = False)
            if the_girl_2.is_submissive:
                the_girl_2 "OW! Oh [the_girl_2.mc_title] I'm sorry I've been a bad girl, I..."
                $ the_girl_2.slap_ass(update_stats = False)
                $ play_moan_sound()
                "She moans loudly when you spank her."
                the_girl_2 "I'm sorry, I'll be quiet, I just..."
                $ the_girl_2.slap_ass(update_stats = False)
                the_girl_2 "Oh fuck..."
                $ the_girl_2.change_arousal(5 * the_girl_2.opinion.being_submissive)
            else:
                the_girl_2 "Ow! Not so hard, I don't mind playing around a bit, but don't hurt me..."
                $ the_girl_2.slap_ass(update_stats = False)
                "This time you give her another spank, but a little lighter. More of a swat really."
                the_girl_2 "Mmmm, that's better..."
                $ the_girl_2.change_arousal(5)

        "Grab [the_girl_1.title]'s hips":
            "Even though you've got the other girl's pussy in your face, you reach down and grab [the_girl_1.possessive_title]'s hips."
            "With the extra leverage, you start to thrust up into her hard and fast."
            the_girl_1 "Oh! Fuck me good [the_girl_1.mc_title]!"
            $ the_girl_1.change_arousal(5)
            "You give it to her hard for a while, but eventually run out of steam and have to slow down."
    return

label scene_threesome_double_down_fuck_girl_one_2(the_girl_1, the_girl_2, the_location, the_object):
    "You put both hands on [the_girl_2.title]'s ass cheeks, pulling them apart to give you better access."
    "[the_girl_1.possessive_title!c] stops bouncing for a moment, and instead grinds her hips against you for a bit, changing the angle of penetration."
    "You can hear lips smacking coming from above you as the girls begin to make-out while they ride you."
    "You lay your head back for a second and just enjoy the view of [the_girl_2.title]'s ass hovering right above your face. Maybe you should put a finger in?"
    menu:
        "Finger her pussy":
            "You push two fingers into [the_girl_2.title]'s sopping wet pussy. From this angle, it's easy to angle your fingers down and find her G-spot."
            "The girls continue to make out as they ride you. You notice [the_girl_1.title] reach back and spank [the_girl_2.possessive_title]'s ass."
            the_girl_2 "Mmmm..."
            "[the_girl_2.title] begins to twist and pull at [the_girl_1.possessive_title]'s nipples. You can feel her pussy clamp down on you as she stimulates her breasts."
        "Finger her ass":
            "You lick your index finger quickly, getting it lubed up, then press it against [the_girl_2.title]'s ass. You slowly push it inside her."
            if the_girl_2.opinion.anal_sex < 0:
                "She immediately stops making out with [the_girl_1.title] and pulls away from you."
                the_girl_2 "Hey! No butt stuff, you know I hate that!"
                "Damn, guess you won't be exploring her rectum today!"
            else:
                "You hear [the_girl_2.title] moan into the other girl's mouth as they continue to make out. Encouraged by her reaction, you push a little harder until your finger is deep inside her rectum."
                "You lick at her clit as you start to move your finger in and out. Her back passage grips your finger greedily, trying to milk it like a cock."
                $ the_girl_2.change_arousal(5 + 5 * the_girl_2.opinion.anal_sex)
        "Finger both holes" if the_girl_2.opinion.being_fingered > 0:
            "You put your ring finger and pinky together and your index finger out. You put your index finger up to her sphincter and the other two fingers to her cunt and start to push them in."
            the_girl_2 "Oh! Wow that feels amazing..."
            "[the_girl_2.possessive_title!c] pushes her ass back as you push your fingers deep into her holes. Once you bottom out, you start to move them in and out."
            "[the_girl_2.title] moans loudly as she resumes making out with [the_girl_1.title]. She seems to be really responding to this!"
            "You fuck her with your fingers, eliciting all kinds of gasps and moans from her as you do, until you decide to go back to oral."
            $ the_girl_2.change_arousal(5 + 5 * the_girl_2.opinion.being_fingered)
    return

label outro_threesome_double_down_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "You feel yourself go past the point of no return, but there is nothing you can do. With [the_girl_2.title]'s pussy in your face, you can't really even get out a warning."
    $ play_spank_sound()
    "You give [the_girl_2.possessive_title]'s ass a hard spank and moan as you feel yourself begin to dump your cum inside [the_girl_1.title]."
    $ the_girl_1.cum_in_vagina()
    $ scene_manager.draw_scene()
    $ ClimaxController.manual_clarity_release(climax_type = "vagina", person = the_girl_1)
    the_girl_1 "Oh god! He's cumming inside me! I can feel it!"
    "She drops her hips down, taking you as deep as she can. She rotates her hips instead of thrusting, milking your cum as best she can."
    if the_girl_2.has_cum_fetish:
        the_girl_2 "Hey! No fair! I want some of that!"
        "You feel [the_girl_1.title] slowly pull off of you, your cock cold and aching to be back inside her."
        "[the_girl_2.title] leans forward and takes your cock in her mouth, sucking the remains of your cum off your shaft."
        $ the_girl_2.cum_in_mouth()
        $ scene_manager.draw_scene()
        "You feel a few more licks along your pelvic area, which you assume is her cleaning up any remaining drops of cum."
        the_girl_2 "Mmmm, I'm not letting a drop go to waste..."
    "You give a sigh, deeply contented with having dumped your load inside [the_girl_1.title]."
    return

label strip_threesome_double_down_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    pass
    "This scene in progress"
    return

label strip_ask_threesome_double_down_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    pass
    "This scene in progress"
    return

label orgasm_threesome_double_down_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        $ play_moan_sound()
        "You can feel the moaning and gasps from the girls on top of you coming to a crescendo."
        $ the_girl_1.call_dialogue("climax_responses_vaginal")
        $ Threesome_double_down.have_orgasm(the_girl_1)
        $ Threesome_double_down.have_orgasm(the_girl_2)
        the_girl_2 "Oh god I'm cumming too!"
        "[the_girl_2.title] is grinding your face when she cums, her juices running down the sides of her legs."
        "[the_girl_1.possessive_title!c] slams her body down on top of you as she begins to cum at the same time. Her pussy is convulsing all around you."
        "You just lay back and enjoy yourself as the two girls moan and writhe on top of you."
        return

    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        "[the_girl_1.title] is moaning loudly now. [the_girl_2.title] is pinching and twisting her nipples, driving her over the edge."
        $ the_girl_1.call_dialogue("climax_responses_vaginal")
        $ Threesome_double_down.have_orgasm(the_girl_1)
        "She orgasms, her pussy quivering around your cock. You enjoy the sensation of her pussy convulsing around you."
        "She takes a moment to recover, but soon [the_girl_1.title] begins to bounce up and down again on top of you."
        return

    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        "[the_girl_2.title] opens her mouth and moans as you assault her pussy with your skilled tongue."
        $ the_girl_2.call_dialogue("climax_responses_oral")
        $ Threesome_double_down.have_orgasm(the_girl_2)
        "[the_girl_2.title] grinds her pussy against you. [the_girl_1.title] pinches and pulls at her nipples, sending her over the edge."
        "[the_girl_2.title]'s juices are beginning to run down the inside of her legs, you do your best to lap them up and then continue licking her."
    return

label swap_threesome_double_down_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    $ the_girl_1.break_taboo("vaginal_sex")
    $ the_girl_1.break_taboo("condomless_sex")
    "[the_girl_1.title] slowly sinks down onto your cock, enjoying the sensations as you penetrate her pussy."
    "[the_girl_2.title] wiggles her hips back and forth, so you grab her ass cheeks with your hands and spread them apart."
    "You dive into her pussy with vigour, determined to get her off with your tongue."
    return
