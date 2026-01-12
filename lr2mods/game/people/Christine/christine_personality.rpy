label police_chief_introduction(the_person):
    mc.name "Excuse me, officer?"
    "She looks up and measures you with a methodical glance."
    the_person "Yes citizen, how can I be of service?"
    mc.name "Ah yes, how may I address you?"
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    $ the_person.primary_job.job_known = True
    the_person "Well then, you can address me as [the_person.title]."
    "[the_person.possessive_title!c] looks you straight in the eyes."
    the_person "What's your name, citizen?"
    return

label police_chief_greetings(the_person):
    if the_person.love < 0:
        the_person "Yes, citizen, how can I help you?"
    elif the_person.happiness < 90:
        the_person "Hello citizen, what's your problem?"
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], how can I be of assistance?"
            else:
                the_person "Hello [the_person.mc_title], what can I do for you today?"
        else:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], is there something I can help you with?"
            else:
                the_person "Hello [the_person.mc_title], how can I help you today?"
    return

label police_chief_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        "[the_person.possessive_title!c] steps back and moves her hand to her weapon."
        the_person "Stand back, Sir. Or else I could charge you with assaulting an officer."
        mc.name "I'm sorry, my mistake."
        "She seems more guarded, but you both try and move past the awkward moment."
    else: #Fail point for touching waist
        "[the_person.possessive_title!c] suddenly shifts, steps back and moves her hand to her weapon."
        the_person "Stand back, Sir. You need to keep your hands away from my weapon."
        "You pull your hands back and lift them half up in the air apologetically."
        mc.name "Of course, I'm sorry."
        the_person "Thank you, you should know it's very dangerous to reach for an officer's weapon."
        "She seems unconvinced, but decides not to say anything else."
    return

label police_chief_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] speaks quietly as you start to move her [the_clothing.display_name]."
    if the_person.obedience > 180:
        the_person "I... I'm sorry, but I can't take that part of my uniform off [the_person.mc_title]..."
    else:
        the_person "I really can't take that part of my uniform off [the_person.mc_title]..."
    return

label police_chief_flirt_response_low(the_person):
    "[the_person.possessive_title!c] seems caught off guard by the compliment."
    if the_person.is_at_work:
        the_person "Oh, thank you! I'm just wearing my daily uniform."
    else:
        the_person "It's really nothing special."
    mc.name "Well, you make it look good."
    $ mc.change_locked_clarity(5)
    "She smiles and laughs self-consciously."
    the_person "Charmer!"
    return

label police_chief_flirt_response_mid(the_person):
    if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
        "[the_person.possessive_title!c] smiles, then glances around self-consciously."
        the_person "Keep your voice down [the_person.mc_title], there are other citizens around."
        mc.name "I'm sure they're all thinking the same thing."
        "She rolls her eyes and laughs softly."
        the_person "Maybe they are, but they are smart enough not to say it out loud."
        $ mc.change_locked_clarity(10)
        the_person "You'll have better luck if you save your flattery for when we're alone."
        mc.name "I'll keep that in mind."
    else:
        "[the_person.possessive_title!c] gives a subtle smile and nods her head."
        the_person "Thank you [the_person.mc_title]. I'm happy you like to see me in uniform."
        the_person "How does it look when I'm walking away?"
        $ the_person.draw_person(position = "walking_away")
        $ mc.change_locked_clarity(10)
        "She just keeps on walking, did you go too far?"
        mc.name "You have an amazing swag in your step, I wouldn't mind walking behind you."
        $ the_person.draw_person()
        "She turns around and smiles warmly."
    return

label police_chief_flirt_response_mid1(the_person):
    if mc.location.person_count > 1:
        "[the_person.possessive_title!c] smiles, then glances around."
        the_person "Not so loud, not everybody has to hear this."
    $ mc.change_locked_clarity(10)
    the_person "It does look good, doesn't it."
    "[the_person.possessive_title!c] gives you a smile."
    $ mc.change_locked_clarity(10)
    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other:
        the_person "I don't know [the_person.mc_title], I have a [the_person.so_title] you know."
        mc.name "Come on, it's just a coffee, we are not going on a date."
    the_person "Right, just let me know when."
    return

label police_chief_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "[the_person.mc_title], there are other citizens around."
        "She bites her lip and leans close to you, whispering in your ear."
        $ mc.change_locked_clarity(15)
        the_person "But if we were alone, I'm sure we could figure something out..."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Follow me."
                "[the_person.possessive_title!c] nods and follows a step behind you."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_police_chief_flirt_response_high_2
                "Once you're alone you put one hand around her waist, pulling her close against you. She looks into your eyes."
                the_person "Well? You better plan you next move carefully..."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She closes her eyes and leans her body against yours."
                else:
                    "You answer with a kiss. She closes her eyes and leans her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_police_chief_response_high
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_police_chief_flirt_response_high_2

            "Just flirt":
                mc.name "I'll just have to figure out how to get you alone then. Any thoughts?"
                the_person "You're a smart man, you'll figure something out."
                "She leans away from you again and smiles mischievously."

    else:
        if mc.location.person_count == 1: #She's shy but you're alone
            "[the_person.title] blushes and stammers out a response."
            the_person "I... I don't know what you mean [the_person.mc_title]."
            mc.name "It's just the two of us, you don't need to hide how you feel. I feel the same way."
            "She nods and takes a deep breath, steadying herself."
            the_person "Okay. You're right. What... do you want to do then?"

        else:  #You're not alone, but she doesn't care.
            the_person "Well I wouldn't want you to run amok. You'll just have to convince me to get me out of this uniform..."
            $ mc.change_locked_clarity(15)
            if the_person.has_large_tits: #Bounces her tits for you
                "[the_person.possessive_title!c] bites her lip sensually and grabs her [the_person.tits_description], jiggling them for you."

            else: #No big tits, so she can't bounce them (as much
                "[the_person.possessive_title!c] bites her lip sensually and looks you up and down, as if mentally undressing you."

            $ the_person.draw_person()
            the_person "Well? You better plan you next move carefully..."

        menu:
            "Kiss her":
                "You step close to [the_person.title] and put an arm around her waist."
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She presses her body up against yours."
                else:
                    "When you lean in and kiss her she responds by pressing her body tight against you."
                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_police_chief_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _call_fuck_person_police_chief_response_high2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_police_chief_flirt_response_high

            "Just flirt":
                mc.name "Not here, not right now, but I've got a few ideas I would like to run by you..."
                "If [the_person.title] has any feelings toward you, she does a good job hiding it, while staring in your eyes."
                the_person "Well maybe if you entertain me when I'm off-duty, you can enlighten me."
    return

label police_chief_public_sex_intervention(the_person):
    police_chief "Hey! What are you doing? You can't do that at the [mc.location.formal_name!i]!"
    $ police_chief.draw_person()
    "Suddenly, a police officer arrives. You stop what you are doing with [the_person.possessive_title]."
    police_chief "God, get decent. I'm taking you two downtown!"
    $ the_person.apply_planned_outfit()
    $ mc.change_location(police_station)
    $ scene_manager = Scene()
    $ scene_manager.add_actor(police_chief)
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_left_flipped)
    "You and [the_person.title] are escorted to the police station by the police officer. You spend a couple hours doing paperwork."
    call mc_arrested_penalties() from _arrested_public_sex_01
    "You and [the_person.possessive_title] go your separate ways for now. She doesn't seem eager to chat about getting arrested."
    call advance_time() from _call_advance_time_after_arrested_1
    jump game_loop
    return
