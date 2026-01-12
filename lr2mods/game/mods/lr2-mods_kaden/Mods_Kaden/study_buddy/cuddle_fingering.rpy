# game/sex_positions/_position_definitions_ren.py
init 1 python:
    cuddle_finger = Position(name = "Cuddle Fingering", slut_requirement = 25, slut_cap = 50, requires_hard = False, requires_large_tits = False,
        position_tag = "missionary", requires_location = "Lay", requires_clothing = "None", skill_tag = "Foreplay",
        girl_arousal = 15, girl_energy = 5,
        guy_arousal = 5, guy_energy = 20,
        connections = [],
        intro = "intro_cuddle_finger",
        scenes = ["scene_cuddle_finger_1", "scene_cuddle_finger_2", "scene_cuddle_finger_3", "scene_cuddle_finger_4"],
        outro = "outro_cuddle_finger",
        transition_default = "transition_default_cuddle_finger",
        strip_description = "strip_cuddle_finger", strip_ask_description = "strip_ask_cuddle_finger",
        orgasm_description = "orgasm_cuddle_finger",
        taboo_break_description = "taboo_break_cuddle_finger",
        verb = "finger",
        opinion_tags = ["being fingered", "missionary style sex"], record_class = "Fingered",
        associated_taboo = "touching_vagina")
        
    # list_of_positions.append(cuddle_finger)

# game/sex_positions/cuddle_fingering.rpy
label intro_cuddle_finger(the_girl, the_location, the_object):
    $ cuddle_finger.redraw_scene(the_girl)
    $ the_item = the_girl.outfit.get_lower_top_layer
    "You lay down next to [the_girl.title] propping yourself up with one arm while the other slides up her thigh."
    if the_item and not the_girl.vagina_available:
        "You don't waste any time pushing your hand between her legs, sliding it under her [the_item.display_name] to reach her pussy."
        "You run a finger over it, teasing it first."
    else:
        "You don't waste any time pushing your hand between her legs, teasing her cute, exposed pussy with your fingers."
    $ play_moan_sound()
    "She moans quietly as you slide two fingers inside her wet hole, savoring the warmth that envelops them."
    "The soft velvety texture of her inner walls send tingles up your arm as you being to pump your digits in and out."
    $ the_item = None
    return

label taboo_break_cuddle_finger(the_girl, the_location, the_object):
    $ cuddle_finger.redraw_scene(the_girl)
    $ the_item = the_girl.outfit.get_lower_top_layer
    "You lean down to kiss [the_girl.title]'s should and neck, distracting her from your hand sliding along her inner thigh and towards her crotch."
    if the_girl.effective_sluttiness(cuddle_finger.associated_taboo) > cuddle_finger.slut_cap:
        if the_item and not the_girl.vagina_available:
            "You slide your hand under her [the_item.display_name] and make her gasp as you brush her sensitive pussy."
            "She spreads her legs and leans back against you, giving you easy access."
        else:
            "She gasps as you brush her sensitive pussy. She spreads her legs for you, giving you easy access."
        $ the_girl.call_dialogue(f"{cuddle_finger.associated_taboo}_taboo_break")
        "You move your hand over her clit and feel her shiver in response to your touch."
    else:
        if the_item and not the_girl.vagina_available:
            "She starts as you slide your hand under her [the_item.display_name]. She grabs your wrist and stops you from moving any farther."
        else:
            "She starts as you brush her sensitive pussy. She grabs your wrist and stops you from moving any farther."
        $ the_girl.call_dialogue(f"{cuddle_finger.associated_taboo}_taboo_break")
        $ play_moan_sound()
        "She lets go of your hand, and you slide it down to your prize. She moans softly as you touch her, and shivers when you first touch her clit."
    "After teasing her for a moment you press two fingers between her slit, sliding them into the wet passage beyond her pussy lips."
    $ the_item = None
    return

label scene_cuddle_finger_1(the_girl, the_location, the_object):
    "As you explore [the_girl.title]'s intimate depths with your probing digits, she arches into your touch, her back bowing off the mattress."
    "Her breathy whimpers fill the room, punctuated by the soft squelching sounds of your fingers gliding through her slick folds."
    if the_girl.tits_available:
        "You bring your mouth down to her [the_girl.tits_description] lavisihing attention on each peak in turn."
        "Your tongue swirls around the sensitive buds, coaxing them to stiffen further under your ministrations. "
        "[the_girl.title] threads her fingers through your hair, holding you close as you lavish attention on her sensitive flesh."
    else:
        $ the_item = the_girl.outfit.get_upper_top_layer
        if the_item:
            "Her back arches, causing her [the_girl.tits_description] to jiggle enticingly. Making you wish she wasn't wearing her [the_item.display_name]."
            $ the_item = None
        else:
            "Her back arches, causing her [the_girl.tits_description] to jiggle enticingly."
    return

label scene_cuddle_finger_2(the_girl, the_location, the_object):
    "You slide your fingers in and out of her pussy, stroking the inside of that soft tunnel."
    $ play_moan_sound()
    "Each movement draws moans of pleasure from [the_girl.possessive_title], who rocks up her hips, pressing against your hand."
    if the_girl.arousal_perc > 60:
        if the_girl.vagina_available:
            "Her pussy is dripping wet now, juices running down her ass and pooling on the [the_object.name]."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer
            if the_item:
                "Her pussy is dripping wet now, her juices leaving a faint wet spot on her [the_item.display_name]."
                $ the_item = None
    else:
        if the_girl.vagina_available:
            "She places one of her own hands over yours, encouraging you to speed up."
            the_girl "Just like that... Ah..."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer
            if the_item:
                $ play_moan_sound()
                "You look down her body and watch as your fingers move under her [the_item.display_name], timed to her soft moans of pleasure."
                $ the_item = None
    return

label scene_cuddle_finger_3(the_girl, the_location, the_object):
    $ body_description = get_body_description(the_girl)
    "Your thumb finds her sensitive nub, circling it with just the right pressure to send shockwaves of pleasure through her [body_description]."
    $ play_moan_sound()
    "She lets out a soft moan as her inner walls clench and release rhythmically around your fingers."
    "Your free hand cradles the back of her head, guiding her face towards yours. Her lips part, inviting your kiss."
    "You hesitate for a moment, savoring the intimacy of the moment before your mouth claims hers."
    $ the_girl.break_taboo("kissing")
    return

label scene_cuddle_finger_4(the_girl, the_location, the_object):
    "You set a slow, steady rhythm, savoring the feel of her silky heat enveloping your fingers."
    $ play_moan_sound()
    "Every few strokes, you brush against her G-spot, making her shudder and whimper with need."
    "Her body tenses, and her breath catches in her throat. You hold the pressure there for a moment, feeling the tension build before releasing it slowly."
    return

label outro_cuddle_finger(the_girl, the_location, the_object):
    "[the_girl.title] can tell you are getting close. She rubs her hand into your crotch."
    "Feeling [the_girl.title]'s fingers on your crotch and as her hot, tight pussy squeezes yours is enough to push you that little bit farther, past the point of no return."
    "You clench your ass, thrusting up slightly as you cum, shoving your fingers deep into her cunt and making her gasp in surprise."
    $ ClimaxController.manual_clarity_release(climax_type = "air", person = the_girl)
    the_girl "Did you just... Cum?"
    mc.name "Yeah."
    if report_log.get("girl orgasms", 0) > 0:
        the_girl "That's only fair I suppose."
    else:
        the_girl "Aww, I thought I was going to get there first. Oh well."
    if the_girl.wants_creampie or the_girl.has_cum_fetish:
        the_girl "Maybe next time we'll find somewhere else for you to do that."
        if the_girl.opinion.drinking_cum > 0:
            "[the_girl.title] winks at you as she licks her lips."
        elif the_girl.opinion.cum_facials > 0:
            "[the_girl.title] strokes her cheek and pouts at you."
        elif the_girl.opinion.being_covered_in_cum > 0:
            if the_girl.tits_available:
                "[the_girl.title] strokes her bare chest with her hand."
            else:
                "[the_girl.title] strokes her neck."
        else:
            "[the_girl.title] winks at you and pouts slightly."
    if the_girl.opinion.being_fingered < 0:
        the_girl "Now, you've cum, can we do something else?"
        "[the_girl.title] gently pulls your hand up from her [the_girl.pubes_description] pussy."
        if the_girl.sluttiness >= 60:
            "She brings your hand up to her mouth. She slides your fingers, fresh from her cunt, into her mouth."
            "Her tongue wraps around them as she sucks gently on your fingers. She works her hips, wiggling closer to press up against your spent cock."
        else:
            $ play_moan_sound()
            "She moans and works her hips, wiggling to the side until she is pressed up against you."
    elif the_girl.opinion.being_fingered > 0 or report_log.get("girl orgasms", 0) > 0:
        the_girl "Now, what is it that you were doing?"
        "[the_girl.title] gently holds your arm in place with your hand at her pussy."
        the_girl "You are so good at this."
    else:
        the_girl "Don't forget what you were doing."
    return

#TODO create cuddle_grope
label transition_cuddle_fingering_cuddle_grope(the_girl, the_location, the_object):
    "You give her a few wet pussy a few more strokes, then pull your fingers out and drag them along her stomach."
    $ play_moan_sound()
    if the_girl.sluttiness >= 60:
        "She moans and takes hold of your hand, bringing it up to her mouth. She slides your fingers, fresh from her cunt, into her mouth."
        "Her tongue wraps around them as she sucks gently on your fingers. She looks into your eyes, making sure you enjoy the show."
    else:
        "She moans and looks deeply into your eyes as she rubs your crotch."
    return

#TODO create cuddle_dildo
label transition_cuddle_fingering_cuddle_dildo(the_girl, the_location, the_object):
    "You give her a few wet pussy a few more strokes, then pull your fingers out and drag them along her stomach."
    $ play_moan_sound()
    if the_girl.sluttiness >= 60:
        "She moans and takes hold of your hand, bringing it up to her mouth. She slides your fingers, fresh from her cunt, into her mouth."
        "Her tongue wraps around them as she sucks gently on your fingers. She works her hips, grinding your erection against her ass."
    else:
        "She moans and works her hips back against you, grinding your erection against her ass."
    return

#TODO
label transition_default_cuddle_finger(the_girl, the_location, the_object):
    $ cuddle_finger.redraw_scene(the_girl)
    "Laying down next to [the_girl.title], rest a hand on her stomach,  and start sliding it down towards her [the_girl.pubes_description] mound."
    "You don't waste any time sliding two fingers into her warm, wet pussy."
    return

label strip_cuddle_finger(the_girl, the_clothing, the_location, the_object):
    the_girl "Your hands feel amazing... Oh my god..."
    $ the_girl.draw_animated_removal(the_clothing, position = cuddle_finger.position_tag)
    $ play_moan_sound()
    "She strips off her [the_clothing.name] while you're fingering her, moaning the whole time."
    return

label strip_ask_cuddle_finger(the_girl, the_clothing, the_location, the_object):
    the_girl "Everything feels so tight, I want to take it all off... Do you mind?"
    "[the_girl.possessive_title!c] grabs onto her [the_clothing.name], waiting for you to tell her what to do."
    menu:
        "Let her strip":
            mc.name "Take it off. Strip for me."
            $ the_girl.draw_animated_removal(the_clothing, position = cuddle_finger.position_tag)
            "[the_girl.possessive_title!c] takes off her [the_clothing.name] and drops it to the side while you pump your fingers in and out of her cunt."
            return True
        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl "Do you think I look sexy in it?"
            else:
                the_girl "Don't you think I would look better wearing your cum? That would be so fitting for your dirty little slut, wouldn't it?"
            return False

label orgasm_cuddle_finger(the_girl, the_location, the_object):
    the_girl "Oh god... Right there! Right there! Ahhhhh!"
    "Her whole body tenses up and she arches off the [the_object.name]. A shiver runs through her body as she climaxes."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She quivers with pleasure for a few seconds before her whole body relaxes."
    the_girl "Ah... Keep going..."
    return
