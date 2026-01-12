label study_recordings_menu_label():
    $ temp_choice = None
    $ the_sister = lily
    $ the_person = get_lab_partner()
    if not mc.business.event_triggers_dict.get("study_recordings", []):
        return
    $ footage_list = mc.business.event_triggers_dict.get("study_recordings", [])
    while temp_choice != "Back":
        call screen main_choice_display(build_menu_items([["Select Footage"] + footage_list + ["Back"]]))
        $ temp_choice = _return
        if temp_choice == "1. Friend Recording":
            call friend_recording_1_label(the_sister, the_person) from _call_friend_recording_1_menu
        elif temp_choice == "2. Friend Recording":
            call friend_recording_2_label(the_sister, the_person) from _call_friend_recording_2_menu
        elif temp_choice == "[the_sister.title] Proposes":
            call lily_proposes_label(the_sister, the_person) from _call_lily_proposes_menu
        elif temp_choice == "Buddy Proposes":
            call buddy_proposes_label(the_sister, the_person) from _call_buddy_proposes_menu
        elif temp_choice == "[the_sister.title] Rejects":
            call lily_rejects_label(the_sister, the_person) from _call_lily_rejects_menu
        elif temp_choice == "Lily/Buddy Kissing":
            call lily_room_kiss(the_sister, the_person) from _call_lily_room_kiss_menu
        elif temp_choice == "Lily/Buddy Groping":
            call lily_room_grope(the_sister, the_person) from _call_lily_room_grope_menu
        elif temp_choice == "Lily/Buddy Stripping":
            menu:
                "[the_sister.name] Strips":
                    call lily_room_strip(the_sister, the_person) from _call_lily_room_strip_menu
                "[the_person.name] Strips":
                    call lily_room_strip(the_person, the_sister) from _call_lily_room_strip_menu2
        elif temp_choice == "Lily/Buddy Oral Sex":
            menu:
                "[the_sister.name] Licks":
                    call lily_room_oral(the_sister, the_person) from _call_lily_room_oral_menu
                "[the_person.name] Licks":
                    call lily_room_oral(the_person, the_sister) from _call_lily_room_oral_menu2
        elif temp_choice in ["Lesbian Failure 1", "Lesbian Failure 2", "Lesbian Failure 3"]:
            menu:
                "[the_sister.title] Orgasms":
                    $ person_one = the_sister
                    $ person_two = the_person
                "[the_person.title] Orgasms":
                    $ person_one = the_person
                    $ person_two = the_sister
            if temp_choice == "Lesbian Failure 1":
                call lesbian_fail_1(person_one, person_two) from _call_lesbian_fail_1_menu
            elif temp_choice == "Lesbian Failure 2":
                call lesbian_fail_2(person_one, person_two) from _call_lesbian_fail_2_menu
            elif temp_choice == "Lesbian Failure 3":
                call lesbian_fail_3(person_one, person_two) from _call_lesbian_fail_3_menu
        elif temp_choice == "Love Triangle Chat":
            call love_triangle_label(the_sister, the_person) from _call_love_triangle_label_bf
        elif temp_choice == "Threesome Chat":
            call threesome_chat_label(the_sister, the_person) from _call_threesome_chat_label_bf
    $ mc.location.show_background()
    return

label friend_recording_1_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister)
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    $ scene_manager.add_actor(the_sister, sister_outfit, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, position = "sitting", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "In the recording you see [the_sister.title]'s room, except the bed and desk are filled with books and studying materials"
    "[the_person.title] and [the_sister.title] sit side by side at the small desk, focused intently on their work."
    "[the_person.title] glances over at [the_sister.title], who seems to be struggling with something."
    the_person "Hey, do you need help with that math problem?"
    the_sister "No, no thanks. I think I've got it."
    "They both go back to their studies for a few minutes before [the_person.title] speaks again."
    the_person "So, what were you having trouble with earlier?"
    the_sister "Just some geometry problems. It's been awhile since we had to deal with that stuff."
    the_person "Yeah, I know what you mean. But hey, at least we have each other to help out."
    "They spend the next hour going over their homework together, occasionally laughing at inside jokes or helping each other understand tricky concepts."
    the_sister "Thanks for being such a great study buddy, [the_person.title]."
    the_person "Anytime, [the_sister.fname]."
    "As they finish up, they realise how much time has passed and decide to start packing things up before it gets too late."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label friend_recording_2_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister).get_copy()
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person).get_copy()
    $ scene_manager.add_actor(the_sister, sister_outfit, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, position = "sitting", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "The scene opens on [the_person.title] and [the_sister.title] in [the_sister.possessive_title]'s bedroom."
    "It is neat and tidy except for the scattered textbooks and papers on the desk."
    "The girls are engrossed in their studies, their focus unbroken."
    "[the_person.title] leans back in her chair, stretching her arms above her head."
    the_person "Wow, this is nice. We should do this more often."
    the_sister "Definitely. It helps to have someone to bounce ideas off of."
    $ scene_manager.add_actor(mom, emotion = "happy")
    "They continue working diligently until a knock on the door interrupts them. [mom.possessive_title] pokes her head in, looking concerned."
    mom "Girls, dinner's ready. Come and eat before it gets cold."
    the_person "Oh wow, we lost track of time. We're coming!"
    $ scene_manager.remove_actor(mom)
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "stand2", emotion = "happy")
    $ scene_manager.update_actor(the_person, person_outfit, position = "stand3", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "As they gather their things, [the_sister.title]'s phone buzzes with a message from a classmate. She quickly reads it and blushes before putting her phone away."
    the_person "What's wrong? Is everything okay?"
    the_sister "Yeah, it's nothing important. Just a silly message from a friend."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lily_proposes_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister).get_copy()
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person).get_copy()
    $ scene_manager.add_actor(the_sister, sister_outfit, emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "The scene opens on [the_person.title] and [the_sister.title] in [the_sister.possessive_title]'s bedroom."
    the_sister "So, [the_person.title], I wanted to talk to you about something."
    "There's a pause, filled only by the sound of breathing."
    the_sister "I've been... Thinking a lot about us, about how we spend time together, how comfortable we are around each other. And I realised... I like being around you."
    the_person "[the_sister.title]..."
    the_sister "Just hear me out, okay? I mean, I really like being around you. Like, more than a friend. More than just a friend."
    "Another long pause follows, filled with silence. Finally, [the_person.title] speaks."
    the_person "[the_sister.title], I... I feel the same way."
    "There's a collective sigh of relief from both girls."
    the_person "I've been so afraid to say it because... Well, you know."
    the_sister "I feel the same way, I never thought... I didn't think it was possible."
    the_person "Neither did I, but here we are."
    "They stare at each other, their eyes filled with unspoken emotions. Finally, [the_sister.title] takes a deep breath."
    the_sister "[the_person.title], I want to be more than friends with you. I want to date you."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "kissing" )
    $ scene_manager.update_actor(the_person, person_outfit, position = "kissing" , display_transform = character_left_flipped(xoffset = .3))
    "[the_person.title]'s eyes fill with tears, and she leans forward, pressing her lips against [the_sister.title]'s."
    "It starts slow, tentative, but quickly grows in intensity."
    "When they break apart, both girls are flushed and breathless."
    the_person "I want that too."
    "And with that, they lean in again, sealing their newfound relationship with another passionate kiss."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label buddy_proposes_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister).get_copy()
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person).get_copy()
    $ scene_manager.add_actor(the_sister, sister_outfit, emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, emotion = "sad", display_transform = character_left_flipped(xoffset = .3))
    "The scene opens on [the_person.title] and [the_sister.title] in [the_sister.possessive_title]'s bedroom."
    the_person "Okay, so, um, here goes nothing. [the_sister.title], I just wanted to say..."
    the_person "I mean, I know we've been friends for a while, and I never thought anything of it, but lately... I mean, I've been noticing things."
    "There's a long pause, and you can hear her breathing heavily."
    the_person "Like, how your laughter makes my stomach flip-flop, or how your eyes light up when we talk about our favorite movies."
    the_person "And then there's the way your body moves when you dance... God, I'm such a loser. Forget I ever said anything."
    $ scene_manager.update_actor(the_person, person_outfit, position = "walking_away", display_transform = character_left_flipped(xoffset = .3))
    "[the_person.title] turns her back, burying her face in her hands."
    the_sister "[the_person.title], I've felt it too."
    "[the_person.title]'s head jolts up, her mouth open in surprise."
    $ scene_manager.update_actor(the_person, person_outfit, position = "stand2", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    the_person "Really?!"
    "There's a long pause, and you can almost hear her biting her lip."
    the_sister "Yeah, I mean, I didn't want to say anything because... You know, we're lab partners, and it's weird, right?"
    the_sister "But... I've been thinking about you a lot lately, too."
    "[the_person.title] covers her mouth with her hand, trying hard not to cry." 
    the_person "Oh, [the_sister.title], I..."
    the_sister "So, uh, maybe we should go on a date sometime soon?"
    the_person "Yes! Yes, yes, yes, yes, yes!! That would be amazing!!! When? How? Where? What should I wear?"
    "She smiles widely, and you can see her blush deepen."
    the_sister "Well, if you're ready, why don't we meet tomorrow after school?"
    the_person "Tomorrow afternoon? After school? Here?"
    the_sister "Yup!"
    the_person "Alright, alright, fine. I'll come over after school."
    the_sister "Awesome! See you then!"
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lily_rejects_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister).get_copy()
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person).get_copy()
    $ scene_manager.add_actor(the_sister, sister_outfit, emotion = "sad")
    $ scene_manager.add_actor(the_person, person_outfit, emotion = "sad", display_transform = character_left_flipped(xoffset = .3))
    "The scene opens on [the_person.title] and [the_sister.title] in [the_sister.possessive_title]'s bedroom."
    the_person "So, um... I wanted to ask you something."
    "[the_person.title] continues, twirling a strand of her own hair around her finger nervously."
    the_person "Do you... Do you want to go out with me?"
    "You feel a knot forming in your throat as you watch the exchange between [the_sister.title] and [the_person.title] unfold on the screen."
    "It's clear that [the_person.title] has developed feelings for [the_sister.title], and she mustered the courage to confess them tonight."
    "But as [the_sister.title] listens to her lab partner speak, you can already guess the answer."
    "Her face falls, and she shakes her head slowly."
    the_sister "No, I don't think so, I mean, I care about you and all, but I don't think of you like that."
    "[the_person.title]'s shoulders slump, and she lets out a slow breath."
    the_person "Oh, well, I just thought maybe... Since we're such good friends and all..."
    "[the_sister.title] reaches out, placing a comforting hand on [the_person.title]'s shoulder."
    the_sister "I'm sorry, really I am, but I don't think it'll work out between us."
    "Your heart aches as you watch [the_person.title] struggle with the rejection."
    "You wish there was something you could do to make it better, to ease the pain you know she's feeling."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lily_room_kiss(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister)
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    $ scene_manager.add_actor(the_sister, sister_outfit, position = "stand3", emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, position = "stand3", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "You quickly skim through the start of the video as they chat, then you see [the_sister.possessive_title] move over and flip off the light."
    "The scene in [the_sister.title]'s room is darker now with only the soft glow of the moonlight illuminating their faces as she walks back to [the_person.possessive_title]."
    "[the_person.title] leans closer, her eyes filled with desire, and slowly, tentatively, she closes the distance between them."
    $ scene_manager.update_actor(the_person, person_outfit, position = "walking_away" , display_transform = character_left_flipped(xoffset = .4))
    "[the_sister.possessive_title!c] hesitates for a moment, but then her own desire overwhelms her reservations, and she responds in kind."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "kissing" )
    $ scene_manager.update_actor(the_person, person_outfit, position = "walking_away" , display_transform = character_left_flipped(xoffset = .5))
    "Their lips meet, tentatively at first, but soon they're kissing fervently, tongues exploring each other's mouths, hands tangled in their hair, pressing against each other's bodies."
    $ mc.change_arousal(5)
    "[the_sister.title] moans softly into the kiss, her body trembling and then going awkwardly stiff."
    $ scene_manager.update_actor(the_person, person_outfit, position = "walking_away" , display_transform = character_left_flipped(xoffset = .4))
    "[the_person.title] seems to sense her discomfort and pulls back slightly, gazing into [the_sister.title]'s eyes with love and adoration."
    the_person "Are you okay? Should we stop?"
    "[the_sister.title] shakes her head vigorously, her breath coming in short gasps, her eyes pleading with [the_person.title] to continue."
    $ scene_manager.update_actor(the_person, person_outfit, position = "walking_away" , display_transform = character_left_flipped(xoffset = .5))
    "And so they do, their passion ignited by the thrill of new sensations."
    "They explore each other's bodies, their touches becoming more daring slipping under clothes, but not taking them off."
    $ mc.change_arousal(10)
    "Their kisses turn deep and passionate, their breaths mingling together in sweet, ragged gasps."
    "[the_person.possessive_title!c]'s hand sneaks up [the_sister.title]'s shirt, caressing her skin, eliciting a soft moan from [the_sister.title]."
    "[the_sister.title] reciprocates, tracing delicate lines down [the_person.title]'s stomach, causing her to arch her back in pure pleasure."
    $ scene_manager.update_actor(the_person, person_outfit, position = "walking_away" , display_transform = character_left_flipped(xoffset = .4))
    "Finally, both girls, panting heavily, break apart, foreheads resting against each other's, chests heaving in sync."
    "They share a long, tender look before reluctantly pulling away, giggling nervously at what they've just done."
    "While they linger close to one another, it seems like they have gone as far as they will today."
    "You watch a bit longer, but nothing more intimate happens before [the_person.title] leaves for the night."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lily_room_grope(the_sister, the_person):
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister)
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    if not sister_outfit.get_panties():
        $ sister_outfit.add_lower(panties)
    $ sister_panties = sister_outfit.get_panties()
    if not person_outfit.get_panties():
        $ person_outfit.add_lower(panties)
    $ buddy_panties = person_outfit.get_panties()
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ scene_manager.add_actor(the_person, person_outfit, position = "missionary", emotion = "happy", display_transform = character_left_flipped(xoffset = .525))
    $ scene_manager.add_actor(the_sister, sister_outfit, position = "back_peek", emotion = "happy")
    "The lights are off in [the_sister.title]'s room, the moonlight bathing it in a soft glow."
    "[the_person.title] and [the_sister.title] are entwined on the bed, their hands roaming over each other's bodies, their breaths coming in quick, shallow gasps."
    "[the_sister.title]'s fingers trace delicate patterns on [the_person.possessive_title]'s abdomen, dipping lower to tease the hem of her [buddy_panties.display_name]."
    "[the_person.title] moans softly, her hips bucking against [the_sister.possessive_title]'s hand."
    if sister_outfit.get_lower_top_layer and sister_outfit.get_lower_top_layer.layer == 3:
        if sister_outfit.get_lower_top_layer.is_extension:
            "[the_person.title] returns the favor, her fingers deftly finding the hem of [the_sister.title]'s [sister_outfit.get_lower_top_layer.display_name] and sliding it up her legs."
        else:
            "[the_person.title] returns the favor, her fingers deftly finding the waistband of [the_sister.title]'s [sister_outfit.get_lower_top_layer.display_name] and sliding it down her legs."
        $ scene_manager.draw_animated_removal(the_sister, sister_outfit.get_lower_top_layer)
    else:
        "[the_person.title] returns the favor, her fingers deftly sliding up [the_sister.possessive_title]'s legs."
    "[the_sister.title] gasps as [the_person.title]'s fingers brush against her bare thighs, sending shivers down her spine."
    "As they continue their exploration, their touches become more insistent, more desperate."
    "Judging by the way their bodies treble with anticipation, they're both achingly close to climax."
    "[the_sister.title] searches between their bodies, her fingers finding [the_person.title]'s clit through her [buddy_panties.display_name]."
    $ mc.change_arousal(10)
    "She circles it gently, teasing it until [the_person.possessive_title] cries out, her hips bucking wildly."
    "[the_person.title] reciprocates, her fingers pushing against [the_sister.title]'s [sister_panties.display_name], seeking out her sensitive bud."
    $ play_female_orgasm()
    "[the_sister.title] moans loudly, her entire body convulsing as she comes hard, her muscles contracting violently."
    $ play_female_orgasm()
    $ mc.change_arousal(10)
    "[the_person.title] follows suit, her own orgasm hitting her like a tidal wave, her voice echoing [the_sister.possessive_title]'s moans as she too climaxes, her body shuddering uncontrollably."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "missionary", emotion = "happy", display_transform = character_left_flipped())
    "Both girls collapse onto the bed, gasping for air, their chests heaving in unison."
    "They share a long, tender look before pulling away, giggling nervously at what they've just done."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lily_room_strip(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister).get_copy()
    if not sister_outfit.get_bra():
        $ sister_outfit.add_upper(bra)
    if not sister_outfit.get_panties():
        if the_sister.opinion.showing_her_ass > 0:
            $ sister_outfit.add_lower(thong)
        else:
            $ sister_outfit.add_lower(panties)
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person).get_copy()
    $ scene_manager.add_actor(the_person, person_outfit, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(the_sister, sister_outfit, emotion = "happy", display_transform = character_left_flipped(xoffset = .2))
    $ body_word = get_body_word(the_sister)
    "When you pull up the footage it reveals a dimly lit room bathed in a soft glow."
    "[the_sister.title] stands in front of [the_person.title], her body illuminated by the moonlight streaming through the window."
    "[the_sister.possessive_title!c] begins to undress, removing her clothes piece by piece, revealing her [body_word] frame."
    while sister_outfit.get_upper_top_layer and sister_outfit.get_upper_top_layer.layer > 1:  
        $ the_item = sister_outfit.remove_random_upper(top_layer_first = True, do_not_remove = False)
        $ scene_manager.draw_animated_removal(the_sister, the_item)
    "[the_person.possessive_title!c] watches hungrily, her eyes devouring every inch of [the_sister.title]'s body."
    "Her fingers twitch with desire as she imagines how she would touch and taste every part of [the_sister.title]."
    $ scene_manager.strip_to_tits(the_sister, visible_enough = False)
    $ mc.change_arousal(5)
    "[the_sister.title] continues her striptease, removing her bra, revealing her pert nipples."
    while sister_outfit.get_lower_top_layer and sister_outfit.get_lower_top_layer.layer > 1:
        $ temp_lower = sister_outfit.remove_random_lower(top_layer_first = True, do_not_remove = False)
        $ scene_manager.draw_animated_removal(the_sister, temp_lower)
    $ temp_panties = sister_outfit.get_panties()
    if temp_lower:
        if clothing_plural(temp_lower):
            "Her [temp_lower.display_name] slide down her legs, and she steps out of them, leaving her standing in only her [temp_panties.display_name]."
        else:
            "Her [temp_lower.display_name] slides down her legs, and she steps out of it, leaving her standing in only her [temp_panties.display_name]."
    else:
        "She is now standing there in only her [temp_panties.display_name]."
    "[the_person.title]'s breath hitches as she takes in the sight of [the_sister.title]'s smooth, toned thighs and the scrap of fabric at the juncture of her legs."
    $ mc.change_arousal(5)
    "Her fingers twitch with the need to reach out and touch her, to feel the silken texture of her skin."
    "But instead, she remains seated on the bed, her eyes locked with [the_sister.title]'s as she encourages her to continue her striptease."
    the_person "Keep going, show me more of that sexy body."
    "[the_sister.title] responds to [the_person.title]'s dirty talk, her body trembling with excitement as she undresses completely, leaving her standing naked in front of [the_person.title]."
    $ scene_manager.strip_to_vagina(the_sister, visible_enough = False)
    $ mc.change_arousal(5)
    "[the_person.title]'s mouth waters as she takes in the sight of [the_sister.title]'s nude form, her [the_sister.tits_description] jutting proudly, her flat stomach, and her smooth thighs."
    "Her fingers twitch with the need to touch and taste every part of her."
    "[the_sister.title] stands confidently, her eyes locked with [the_person.title]'s as she encourages her to continue her dirty talk."
    "[the_person.title] obliges, her words becoming more explicit and lewd as she praises [the_sister.title]'s beauty and begs for more."
    "Their gazes remain locked, the sexual tension palpable even though they don't physically touch."
    $ scene_manager.update_actor(the_sister, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "[the_sister.title] steps closer to [the_person.title], her body mere inches from hers, teasing and taunting her with her nakedness."
    "Your eyes focus on [the_person.title], her eyes ravenous as she watches [the_sister.title]"
    the_person "Oh god, you're so fucking beautiful, [the_sister.fname]. Your body was made for sin."
    "[the_sister.title] smiles seductively, her eyes filled with mischief."
    the_sister "Is that right? And what do you want me to do about that, [the_person.title]?"
    "[the_person.title]'s breath hitches, her voice growing huskier."
    the_person "I want you to come closer, [the_sister.fname]. I want to feel your soft skin against mine."
    $ scene_manager.update_actor(the_sister, emotion = "happy", display_transform = character_left_flipped(xoffset = .4))
    "[the_sister.title] slowly starts to move towards [the_person.title], her hips swaying hypnotically."
    the_sister "Are you sure, [the_person.fname]? Once I touch you, there's no going back."
    "[the_person.title] nods frantically, her breathing becoming more labored."
    the_person "Yes, [the_sister.fname]. Please..."
    $ mc.change_arousal(5)
    $ scene_manager.update_actor(the_sister, emotion = "happy", display_transform = character_left_flipped(xoffset = .45))
    "[the_sister.title] finally stops inches away from [the_person.possessive_title], her [the_sister.tits_description] brushing against [the_person.title]'s chest"
    the_sister "Do you really want this, [the_person.fname]?"
    "[the_person.title] nods fervently, her breath catching in her throat."
    the_person "God, yes! Please, [the_sister.fname]..."
    "[the_sister.title] leans forward, her lips inches away from [the_person.title]'s, but then pulls away, her eyes sparkling with delightful cruelty."
    the_sister "Later, maybe. For now, you'll just have to imagine what could have been."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lily_room_oral(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = Outfit("Nude").get_copy()
    $ person_outfit = Outfit("Nude").get_copy()
    $ scene_manager.add_actor(the_person, person_outfit, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    $ scene_manager.add_actor(the_sister, sister_outfit, emotion = "happy")
    $ person_body = get_body_description(the_person)
    "You skip straight to the action."
    "[the_sister.title] and [the_person.title] are in the dimly lit room, their bodies glistening with sweat under the moonlight streaming through the window."
    "They are both naked, their eyes locked as they walk towards each other and embrace with intimate familiarity."
    $ scene_manager.update_actor(the_person, person_outfit, emotion = "happy", display_transform = character_left_flipped(xoffset = .4))
    "[the_person.title] runs her hands over [the_sister.title]'s [person_body], tracing her curves and exploring every inch of her skin."
    "[the_sister.title] moans softly, arching her back in response to [the_person.title]'s touch."
    $ mc.change_arousal(10)
    "In turn, [the_sister.title] uses her tongue to tease and explore [the_person.title]'s neck, you wouldn't be surprised to see a hickey on her tomorrow."
    "Their kisses become deeper and more passionate as they lose themselves in their desire for one another."
    $ scene_manager.update_actor(the_person, person_outfit, position = "missionary", display_transform = character_right(yoffset = -0.15))
    "Suddenly [the_person.title] takes a step back and lays on the bed, looking up at [the_sister.title] invitingly."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "doggy", display_transform = character_right(yoffset = -0.3, xoffset = -0.01, zoom = 1.2))
    "[the_sister.title] leans down to kiss her. As their tongues entwine, she lowers her body, sinking down to kneel over [the_person.title]."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "doggy", display_transform = character_right(yoffset = -0.18, xoffset = -0.01, zoom = 1.2))
    "A moment later, [the_sister.possessive_title] is sliding down her, trailing kisses along her torso."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "doggy", display_transform = character_right(yoffset = -0.075, xoffset = -0.01, zoom = 1.2))
    "Once she is far enough, [the_sister.title] lowers her head to nestle between [the_person.title]'s legs."
    "You are left with the incredible view of [the_sister.title]'s ass and [the_sister.pubes_description] pussy pointed right at the camera."
    "From [the_person.possessive_title]'s reaction it is pretty clear [the_sister.possessive_title] has found the right spot."
    $ mc.change_arousal(10)
    "Her moans and gasps fill the air as they lose themselves in the sensation of giving and receiving pleasure."
    "The camera captures every intimate moment, from the way [the_sister.title]'s fingers dig into [the_person.title]'s hips to the way [the_person.title]'s knot in [the_sister.title]'s hair."
    $ play_female_orgasm()
    "Her orgasm approaches rapidly, and soon enough, she cries out, her body shuddering with ecstasy as she climaxes."
    "[the_sister.title] lingers at [the_person.title]'s sex, planting gentle kisses along her thighs as her aftershocks die down."
    $ scene_manager.update_actor(the_sister, sister_outfit, position = "missionary", display_transform = character_left_flipped(xoffset = .3))
    $ scene_manager.update_actor(the_person, person_outfit, position = "missionary")
    "Eventually she stands up and then collapses on the bed, next to her sweaty and satisfied girlfriend."
    "They are both still breathing hard, their hearts no doubt racing from the intense experience they just shared."
    $ del person_body
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lesbian_fail_1(person_one, person_two):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ outfit_one = limited_university_wardrobe.decide_on_outfit(person_one).get_copy()
    $ outfit_two = limited_university_wardrobe.decide_on_outfit(person_two).get_copy()
    if outfit_two.wearing_bra:
        $ outfit_two.remove_clothing(outfit_two.get_bra())
    $ scene_manager.add_actor(person_one, outfit_one, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(person_two, outfit_two, position = "sitting", emotion = "happy", display_transform = character_left_flipped(xoffset = .5))
    "As you watch the footage from [lily.title]'s bedroom, you see [person_two.title] and [person_one.title] cuddled up on her bed."
    "They've been spending a lot of time together since their heartfelt conversation about their mutual attraction."
    "[person_two.title] leans in to kiss [person_one.title] softly on the lips, her hands roaming over [person_one.possessive_title]'s body."
    while outfit_two.get_upper_top_layer and outfit_two.get_upper_top_layer.layer > 3:
        $ the_item = outfit_two.remove_random_upper(top_layer_first = True, do_not_remove = False)
        $ scene_manager.draw_animated_removal(person_two, the_item)
    "[person_one.title] moans into the kiss, her fingers tangling in [person_two.title]'s hair."
    while outfit_one.get_upper_top_layer and outfit_one.get_upper_top_layer.layer > 2:
        $ the_item = outfit_one.remove_random_upper(top_layer_first = True, do_not_remove = False)
        $ scene_manager.draw_animated_removal(person_one, the_item)
    "It's clear that they both want to take things further tonight."
    "They break apart with heavy breathing, their faces flushed with desire."
    person_two "I want you so badly."
    "[person_one.title] nods, her eyes filled with lust."
    person_one "Me too!"
    $ top_two = outfit_two.get_upper_top_layer
    if top_two and top_two.layer > 1:
        "[person_one.title] reaches down to remove [person_two.title]'s [top_two.display_name]."
        $ scene_manager.draw_animated_removal(person_two, outfit_two.get_upper_top_layer)
        "As she pulls it off, revealing [person_two.title]'s [person_two.tits_description], she can't help but be amazed by how beautiful her friend is."
    $ top_one = outfit_one.get_upper_top_layer
    $ bra_one = outfit_one.get_bra()
    if top_one and bra_one and top_one != bra_one:
        $ scene_manager.strip_to_tits(person_one, visible_enough = False)
        "[person_two.title] returns the favor, slipping off [person_one.title]'s [top_one.display_name] and [bra_one.display_name]."
    $ scene_manager.strip_full_outfit(person_one)
    $ scene_manager.strip_full_outfit(person_two)
    "With trembling hands, they remove each other's skirts and underwear, revealing their naked forms to one another, and the camera."
    $ mc.change_arousal(10)
    "The sight takes your breath away, and you can feel your own arousal growing."
    "[person_two.title] positions her hand between [person_one.title]'s legs, her fingers slipping effortlessly into [person_one.possessive_title]'s wetness." 
    "[person_one.title] cries out in pleasure as [person_two.title] begins to stroke her, finding just the right rhythm to drive her wild."
    "You watch with bated breath as [person_two.title] leans down and takes one of [person_one.title]'s nipples into her mouth, sucking hard while she continues to finger her."
    "The noises they make together fill the room, a symphony of moans and gasps that only serve to heighten your arousal."
    "It doesn't take long before [person_one.title] is on the brink of orgasm. Her hips buck against [person_two.title]'s touch, begging for release."
    person_one "[person_two.fname], I need you to... I need you to..."
    "[person_two.title] knows exactly what [person_one.title] needs, and she's more than happy to oblige."
    "She moves her fingers faster, thrusting deep inside [person_one.possessive_title]'s body, feeling the tight muscles begin to contract around her."
    $ play_female_orgasm()
    "With one final push, [person_one.title] arches her back and lets out a long, shuddering moan as she comes undone beneath her."
    "Her body goes limp, every muscle relaxed in the aftermath of her orgasm."
    "[person_two.title] licks a trail up [person_one.title]'s stomach and kisses her passionately, their tongues dancing together as they share a moment of pure bliss."
    "But as the intensity of their lovemaking begins to build once again, you notice something strange happening."
    "Despite [person_one.title]'s best efforts, she can't seem to bring [person_two.title] to orgasm."
    "Every time she touches [person_two.possessive_title], it's like she hits a wall, unable to push her over the edge."
    "Maybe one or both of them are too tired or distracted, but for whatever reason nothing seems to work."
    "The more she fails, the more desperate she becomes. At one point [person_two.title] offers to help."
    person_two "Here, let me show you."
    person_one "No, I can do this... Just give me a moment."
    "She redoubles her efforts, but force alone obviously isn't working to get [person_two.title] there."
    "Finally, after a few more futile attempts, [person_one.title] collapses onto the bed next to [person_two.title]."
    "Her face is flushed with frustration and exhaustion, while [person_two.title] looks at her with concern etched on her features."
    person_one "I'm sorry, [person_two.title], I don't know why I couldn't make you cum."
    person_one "You made me feel so good, the least I can do is return the favor."
    "[person_two.title] reaches out and takes [person_one.title]'s hand, giving it a reassuring squeeze."
    person_two "It's okay, sometimes it just doesn't work. We'll figure this out together."
    $ del top_one
    $ del top_two
    $ del bra_one
    $ del outfit_one
    $ del outfit_two
    $ scene_manager.clear_scene()
    return

label lesbian_fail_2(person_two, person_one):
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(person_one).get_copy()
    $ person_outfit = Outfit("Nude").get_copy()
    $ lily_bedroom.show_background()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(person_two, person_outfit, emotion = "happy", position = "missionary")
    "The screen comes alive with the image of [person_two.title] lying on the bed, naked and ready for [person_one.title]."
    $ sister_outfit.strip_to_underwear()
    $ scene_manager.add_actor(person_one, sister_outfit, emotion = "happy", position = "kissing", display_transform = character_left_flipped(xoffset = .4))
    $ mc.change_arousal(10)
    "In no time, [person_one.title] joins her, her lips finding [person_two.title]'s neck and earlobe."
    "She kisses and nibbles her way down [person_two.title]'s body, stopping only to tease her [person_two.tits_description] with her tongue."
    "Her fingers dig into the soft flesh of [person_two.title]'s inner thighs, pulling them apart to grant access to her glistening lips."
    $ scene_manager.update_actor(person_one, position = "doggy", display_transform = character_left_flipped(zoom = 1.2, xoffset = 0.52, yoffset = 0.125))
    "[person_one.title] lowers herself between [person_two.title]'s legs, alternating kisses on each of her inner thighs."
    $ mc.change_arousal(10)
    "You watch as [person_one.title]'s mouth closes around [person_two.title]'s clit, suckling it gently before moving on to licking along her slit."
    "With each lap of her tongue, she draws out a chorus of sweet moans from her girlfriend."
    "[person_two.title]'s body begins to undulate, her hips lifting off the bed in response, her moans growing louder and more desperate."
    person_two "Yes, just like that, don't stop."
    $ mc.change_arousal(10)
    "While continuing her ministrations, [person_one.title] straddles [person_two.title]'s right leg, pinning it firmly under her hips as she grinds down with her sex."
    person_one "You're so responsive, I love how your body reacts to me."
    "[person_two.possessive_title!c]'s hand roam [person_one.title]'s back, nails digging into her shoulders as she clings to her partner."
    "While probing at [person_two.title]'s pussy with her tongue, [person_one.possessive_title] slides a hand down her leg to work her own clit."
    "It's pretty clear that [person_two.title] is close, but [person_one.title] doesn't seem ready to cum, and is desperately trying to catch up."
    $ mc.change_arousal(10)
    $ play_female_orgasm()
    "Unfortunately it is too late, [person_two.title] screams her orgasmic release, her entire body convulsing."
    "She dutifully licks and sucks, coaxing every aftershock out of [person_two.title] until she goes limp, her chest heaving with exertion."
    "[person_one.title] continues to grind herself against [person_two.title]'s leg throughout, but is clearly not getting the release she sought."
    "Looking down at [person_two.title] it is pretty clear that she is too spent to reciprocate tonight, so [person_one.title] slows and stops."
    "She presses a final kiss to [person_two.possessive_title]'s inner thigh before crawling up her body, claiming her mouth in a passionate kiss."
    person_one "You're incredible, always so beautiful when you cum."
    "[person_two.title] returns the kiss, her exhaustion evident in the languid press of her lips."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lesbian_fail_3(person_one, person_two):
    $ lily_bedroom.show_background()
    $ scene_manager = Scene()
    $ sister_outfit = Outfit("Nude").get_copy()
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(person_two).get_copy()
    "The scene opens to a dimly lit bedroom, the only light coming from a small lamp on the nightstand casting shadows on the walls."
    $ scene_manager.add_actor(person_one, sister_outfit, emotion = "happy", position = "missionary")
    "In the center of the frame, [person_one.title] lies naked on her back, legs spread wide, her breathing heavy with anticipation."
    $ person_outfit.strip_to_underwear()
    $ scene_manager.add_actor(person_two, person_outfit, emotion = "happy", position = "sitting", display_transform = character_left_flipped(zoom = 1.15, yoffset = 0.3, xoffset = 0.5))
    "She glances down, looking at [person_two.title] who kneels between her legs, kissing and nibbling her way along her body."
    $ mc.change_arousal(10)
    "[person_two.title]'s fingers trace circles around [person_one.title]'s clitoris, driving her wild with pleasure. [person_one.title] gasps loudly, arching her back off the mattress, moaning encouragement."
    $ scene_manager.add_actor(person_two, person_outfit, emotion = "happy", position = "sitting", display_transform = character_left_flipped(zoom = 1.15, xoffset = 0.5))
    "She grabs onto [person_two.title]'s hair, pulling her closer until their lips meet passionately."
    "Their tongues dance, exploring each other's mouths, as [person_two.title] continues to stimulate [person_one.title] with her fingers."
    $ mc.change_arousal(10)
    "Suddenly, [person_two.title] slides two fingers inside [person_one.title], pumping slowly at first before speeding up."
    "[person_one.title] cries out, her hips bucking off the bed, meeting [person_two.title]'s rhythm."
    "They move together, lost in the heat of the moment, their bodies glistening with sweat under the soft glow of the lamp."
    "You can't seem to look away as [person_two.title] brings [person_one.title] to the brink of orgasm, her moans growing louder and more desperate."
    $ mc.change_arousal(10)
    $ play_female_orgasm()
    "Finally, [person_one.title]'s climax crashes over her, her body trembling and contracting around [person_two.title]'s fingers."
    "[person_two.title] kisses her tenderly, wiping the sweat from her brow, it is clear they truly care for each other."
    "Unfortunately for [person_two.title] it doesn't look like [person_one.possessive_title] is going to be able to return the favor."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label lesbian_success_1(person_one, person_two): #grope / finger
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(person_one).get_copy()
    $ scene_manager.add_actor(person_one, visible = False)
    $ scene_manager.apply_outfit(person_one, temp_outfit)
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(person_two).get_copy()
    $ scene_manager.add_actor(person_two, visible = False)
    $ scene_manager.apply_outfit(person_two, temp_outfit)
    $ scene_manager.show_actor(person_one, emotion = "happy")
    $ scene_manager.show_actor(person_two, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "INCOMPLETE LABEL"
    "Inside the room, [person_one.title] and [person_two.title] collapse onto the bed."
    #strip
    "Slowly, they begin to undress each other, their fingers tracing sensitive spots on the other's body, eliciting soft moans and gasps of delight."
    #position
    "[person_one.title] lies back on the bed, spreading her legs wide open, inviting [person_two.title] to join her."
    #position
    "[person_two.title] hesitates for a moment before crawling between her lover's thighs, kissing her way up and down [person_one.title]'s quivering form."
    "Your breath catches as you watch them, savouring every single detail as it unfolds before your eyes."
    "As [person_two.title]'s tongue glides across [person_one.title]'s pussy, she lets out a cry of pleasure, her hips bucking off the bed."
    "Her fingers rake through [person_two.title]'s hair, urging her to continue."
    #TODO more
    person_one "Oh... Oh god... I... I'm cumming!"
    "[person_one.title] moans and screams as [person_two.title] drives her over the edge."
    # position
    "While she recovers, [person_two.title] moves, positioning herself above [person_one.title]'s face."
    "Her dripping pussy inches away from [person_one.title]'s waiting mouth."
    "[person_one.title] doesn't waste any time, lapping up every drop of [person_two.title]'s juice, her tongue exploring every nook and cranny of [person_two.title]'s wetness."
    "[person_two.title] groans loudly, her body trembling with satisfaction."
    person_two "Ohhh, [person_one.fname]... [person_one.fname], please..."
    "[person_one.title] doesn't need any more encouragement; she sucks harder, her hands gripping [person_two.title]'s ass tightly, pulling her closer."
    "[person_two.title]'s hips move rhythmically, her moans growing louder and more desperate."
    person_two "Ahh... Ahh... [person_one.fname], I'm close..."
    "And with that, she crumbles into an intense orgasm, her body shaking violently as waves of orgasmic bliss wash over her."
    "[person_one.title] devours every drop of her essence, her own cunt throbbing with need."
    # position
    "After a few moments, they lay side by side, sweaty and spent. [person_one.title] rests her head on [person_two.title]'s chest, their hearts beating in sync."
    person_one "That was amazing, [person_two.fname]. Thank you."
    person_two "No, thank you, [person_one.fname]. I needed that just as much as you did."
    "They giggle softly, content in knowing that they have each other to share this incredible journey with." 
    $ del temp_outfit
    $ scene_manager.clear_scene()
    return

label lesbian_success_2(person_one, person_two): #69
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(person_one).get_copy()
    $ scene_manager.add_actor(person_one, visible = False)
    $ scene_manager.apply_outfit(person_one, temp_outfit)
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(person_two).get_copy()
    $ scene_manager.add_actor(person_two, visible = False)
    $ scene_manager.apply_outfit(person_two, temp_outfit)
    $ scene_manager.show_actor(person_one, emotion = "happy")
    $ scene_manager.show_actor(person_two, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "INCOMPLETE LABEL"
    "As [person_one.title] and [person_two.title] lose themselves in their passionate embrace, their bodies entwined in a sensual dance of desire, they begin to explore each other intimately."
    "Their hands caress every inch of skin, reveling in the warmth and softness."
    person_one "Oh [person_two.fname]... I've needed so much."
    person_two "Mmmm, [person_one.fname]... Me too. Let's make this unforgettable."
    "With each touch and kiss, their breathing becomes more rapid. They move closer together, their hearts pounding with excitement."
    $ scene_manager.strip_to_underwear()
    "As they explore further, their clothes begin to disappear under the force of their passion."
    "Their fingers work quickly to remove any lingering barriers."
    $ scene_manager.strip_full_outfit()
    person_one "[person_two.fname]... I need you inside me now!"
    $ scene_manager.update_actor(person_one, emotion = "happy", position = "missionary")
    $ scene_manager.update_actor(person_two, emotion = "happy", position = "doggy")
    "With an intimate understanding of each other's desires, [person_one.title] and [person_two.title] begin to use their tongues and fingers to explore the depths of one another's pussies."
    person_one "Oh [person_two.fname]... Your tongue feels so amazing on my clit!"
    person_two "Mmmm, [person_one.fname]... I love the way your fingers feel inside me."
    "As they continue to lick and finger one another with increasing intensity, their breaths become more rapid, mirroring the building passion between them."
    #TODO more details
    "Their touches become more urgent as they both approach the peak of pleasure."
    person_one "[person_two.fname]... I'm so close! Please, don't stop!"
    person_two "Mmmm, [person_one.fname]... Me too. We're going to experience this together!"
    #TODO orgasm
    $ play_female_orgasm()
    #TODO cuddle
    $ del temp_outfit
    $ scene_manager.clear_scene()
    return

label lesbian_success_3(person_one, person_two): #finger / finger anal
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ scene_manager.add_actor(person_one, visible = False)
    $ scene_manager.strip_full_outfit(person_one)
    $ scene_manager.add_actor(person_two, visible = False)
    $ scene_manager.strip_full_outfit(person_two)
    $ scene_manager.show_actor(person_one)
    $ scene_manager.show_actor(person_two)
    "[person_one.title]'s fingers dance across [person_two.title]'s smooth skin as she trails her fingertips down the gentle slope of her lover's stomach."
    "You hear a soft exhalation of breath from [person_two.title] as [person_one.title] leans in, her lips seeking out the tender flesh of [person_two.title]'s neck."
    person_one "You're so beautiful, I could stare at you all day."
    "[person_two.title]'s eyes flutter closed, her head tilting to give [person_one.title] better access."
    "Her hands come up to cradle [person_one.title]'s face, her thumbs tracing the curve of [person_one.title]'s cheeks."
    person_two "I love how you touch me, it's like you can sense exactly what I need."
    "[person_one.title]'s lips brush against [person_two.title]'s ear, sending shivers coursing through her body."
    person_one "And I love how you react to me, you're so responsive... It drives me wild."
    "As she speaks, [person_one.title]'s hand drifts lower, her fingers delving into the warm, wet heat between [person_two.title]'s thighs."
    "She finds the swollen bud of [person_two.title]'s clitoris, her fingers circling it in slow, deliberate strokes."
    $ play_moan_sound()
    "[person_two.title] moans, her hips bucking upward in search of more friction."
    "[person_one.title] smiles, her tongue darting out to lick the shell of [person_two.title]'s ear."
    person_two "Yes... Yes, just like that."
    "Her breathing grows ragged, their bodies moving in tandem as they chase the peak of pleasure."
    "[person_one.title]'s fingers work their magic, her mouth leaving trails of kisses on [person_two.title]'s skin as she devoures her lover."
    person_two "Oh, [person_one.title]... I'm getting close... You make me feel so alive..."
    "[person_one.title]'s lips find [person_two.title]'s, capturing the words in a searing kiss that leave them both breathless."
    "As their tongues entwine, [person_one.title]'s fingers pick up pace, driving [person_two.title] relentlessly toward the precipice of climax."
    "[person_two.title]'s nails dig into [person_one.title]'s shoulders, her hips jerking erratically as she teeters on the brink."
    person_two "Please, [person_one.title]... I need you..."
    "With a final, decisive movement, [person_one.title] sends [person_two.title] hurtling over the edge."
    $ play_female_orgasm()
    "She cries out, her body convulsing in ecstasy as waves of pleasure crash over her."
    "[person_one.title] holds her close, riding out the aftershocks with gentle, soothing touches until [person_two.title] collapses back against the bed, spent but satisfied."
    "Panting heavily, [person_one.title] gazes down at [person_two.title] with a look of profound contentment."
    "For several long moments, they lay there, catching their breath and basking in the afterglow of their shared experience."
    $ scene_manager.update_actor(person_one, emotion = "happy", position = "sitting")
    "Then, with a soft chuckle, [person_one.title] rolls off [person_two.title], propping herself up on one elbow to study her lover's flushed face."
    person_one "Well, that was certainly... Eventful."
    person_two "Yeah, I guess it was, I love how we can be like this together."
    "They lapse into silence again, seemingly content to simply enjoy each other's company and the closeness they share."
    "Eventually, though, [person_one.title]'s curiosity gets the better of her."
    person_one "So, do you want to try something new tonight?"
    person_two "Like what?"
    person_one "Well, I've always wanted to try... Anal."
    "[person_two.title]'s eyes go wide with surprise, then narrow playfully."
    person_two "Is that so? And here I thought you were just a vanilla girl."
    $ scene_manager.update_actor(person_two, emotion = "happy", position = "sitting")
    "[person_two.title] chuckles, nipping at [person_one.title]'s earlobe, her hand sliding down to cup [person_one.title]'s rear possessively."
    person_one "Vanilla? Please, I have a whole spice rack hidden away..."
    "[person_one.title] arches her back, leaning into the pressure of [person_two.title]'s hand, a playful smirk dancing on her lips."
    person_two "Hmm, well, I think this could be a good night for some experimentation."
    $ scene_manager.update_actor(person_one, emotion = "happy", position = "back_peek")
    $ scene_manager.update_actor(person_two, emotion = "happy", position = "sitting")
    "[person_two.title] grins wickedly, her thumb tracing lazy circles around the taut muscle of [person_one.title]'s anus."
    person_two "Let's see if this little black cherry is ripe enough for picking."
    "Her fingers gently probe the entrance, testing the waters before venturing further."
    "[person_one.title] gasps softly, her muscles instinctively clenching around [person_two.title]'s probing touch."
    person_one "Careful now..."
    "[person_two.title] laughs, relishing the way [person_one.title]'s voice trembles with anticipation."
    person_two "Don't worry, [person_one.fname], I wouldn't dream of hurting you."
    "She reaches for the lube, spreading a good amount on her hand."
    "Returning to [person_one.title] slowly, deliberately, she widens the opening, pressing firmly as her finger sinks deeper and deeper."
    "The initial resistance gives way to a slow, deliberate slide, filling [person_one.title]'s channel with a steady pressure."
    "[person_two.title] cries out, her body tensing as the foreign object stretches her tightness."
    person_two "Breathe, sweetheart, breathe... It'll feel amazing once you're used to it."
    "[person_one.title] takes a shaky breath, her hands fisting the sheets as [person_two.title] begins to move, gliding in and out of [person_one.title]'s snug passage with a rhythmic cadence."
    "A whimper escapes [person_one.title]'s lips as [person_two.title]'s finger finally reaches the sweet spot within, sending shivers racing through her core."
    person_one "Mmm, yes... Like that... More..."
    person_two "Trust me, baby, I'll take care of you. I promise."
    "[person_two.title] obliges, her movements becoming increasingly confident as she explores the most intimate depths of [person_one.title]'s ass."
    "The room fills with the sound of slick, wet slapping as [person_two.title]'s fingers plunge deeper, stroking the sensitive tissue inside."
    "Moans and whimpers punctuate the air, mingling with the creaking of the bed frame and the heavy breathing of the lovers."
    $ play_female_orgasm()
    "Then, with a final, powerful thrust, [person_two.title] sends [person_one.title] soaring over the edge, collapsing against her lover in a tangle of limbs and contented sighs."
    "[person_two.title] keeps moving even after [person_one.title]'s orgasm subsides, savoring the lingering heat, the trembling remnants of pleasure."
    "Eventually, she slows down, withdrawing her hand."
    $ scene_manager.update_actor(person_one, emotion = "happy", position = "missionary")
    person_two "See? Told you it would be amazing."
    "[person_one.title] manages a weak smile, her chest heaving from exertion from the intensity of the experience."
    person_one "You weren't kidding... That was... Wow."
    "[person_two.title] leans down, pressing a soft kiss to [person_one.title]'s temple, her thumb stroking soothing circles on her cheekbone."
    $ scene_manager.clear_scene()
    return

label love_triangle_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister)
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    $ scene_manager.add_actor(the_sister, sister_outfit, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, position = "sitting", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "[the_sister.title] leans back in her chair, sipping her water thoughtfully."
    the_sister "Do we need to talk more about what happened with [mc.name] last time?"
    the_person "Maybe, I mean I think we are both on the same page... But we should be sure."
    the_sister "He's helped us find this amazing connection, and I wouldn't trade that for anything."
    "[the_person.title] nods her head in agreement, her [the_person.eyes[0]!l] eyes sparkling with excitement."
    the_person "I know! Being with you is everything I ever wanted... But..."
    the_sister "What if we could have even more?"
    the_person "Exactly!"
    the_sister "So you do want to keep seeing him too?"
    the_person "Only if it's okay with you, and of course you'd be able to see other people too."
    "[the_sister.title] pauses, taking a deep breath before diving in... Cautiously."
    if the_sister.is_girlfriend:
        the_sister "Well, you know we used to date, right? What if he was also the other person I wanted to see?"
    else:
        the_sister "What if he was also the other person I wanted to see?"
    "[the_person.title] raises an eyebrow curiously."
    the_person "Really?"
    "[the_sister.title] nods nervously."
    the_sister "This isn't the first time I've considered him as a potential partner."
    if not the_sister.has_taboo("kissing"):
        if not the_sister.has_taboo("sucking_cock"):
            the_sister "We experimented a little... There were some lines that got crossed."
            "[the_person.title]'s eyes widen in surprise and disbelief."
            the_person "You mean..."
            if not the_sister.has_taboo("anal_sex"):
                "She trails off, her voice hoarse with emotion.[the_sister.title] nods again."
                the_sister "Yeah, (sigh) It was wrong, but it happened."
                if the_sister.sluttiness > 60: # incest?
                    the_sister "Honestly, it was some of the best sex I've ever had."
                    $ the_person.increase_opinion_score("incest")
            else:
                the_sister "Not... Like all the way... I just kinda blew him a few times."
        else:
            the_sister "It was pretty chaste, nothing more than we did when he was teaching me."
    else:
        the_sister "We never did anything, I think I just kissed him on the cheek, but it didn't feel like hanging out with my brother."
    "There is a long pause as both girls process this revelation. Finally, [the_person.title] speaks up."
    the_person "Wow, so if he's up for it we can both be with him openly, not just our training sessions?" 
    "[the_sister.title] bites her lip anxiously, considering the proposal. After a few moments of hesitation, she nods slowly."
    the_sister "I think that's what I want... If you don't have a problem with me and my brother hooking up."
    $ the_person.increase_opinion_score("incest")
    "[the_person.title] grins widely and leans across the gap between their chairs, planting a simple kiss on [the_sister.title]'s cheek."
    the_person "Of course not, if that's what makes you happy. Honestly... I think it's kinda hot."
    the_person "When you licked his cum off my chin... I've never been so turned on."
    the_sister "That's a relief, I've been so concerned about freaking you out."
    the_person "I love you [the_sister.fname]. I don't think there is anything you could do that would freak me out."
    the_sister "I love you too [the_person.fname]."
    "There is a lull in the conversation, but it looks like [the_person.title] is trying to decide if she wants to ask a question."
    the_person "Actually... If you wanted to... Maybe next time I could... Watch you and him?"
    the_person "Only if your comfortable with it."
    the_sister "I think that would be okay as long as you won't be jealous."
    the_person "If I'm being honest... I might be a little envious, it's so hard not to touch your body."
    the_sister "We'll figure it out, but we can try right?"
    the_person "Yeah, we can definitely try."
    "With renewed vigor, the two girls go back to their studies, eager to reconnect with [mc.name] in a new way."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

label threesome_chat_label(the_sister, the_person):
    $ scene_manager = Scene()
    $ lily_bedroom.show_background()
    $ sister_outfit = limited_university_wardrobe.decide_on_outfit(the_sister)
    $ person_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    $ scene_manager.add_actor(the_sister, sister_outfit, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(the_person, person_outfit, position = "sitting", emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "[the_person.title] and [the_sister.title] lie together on [the_sister.title]'s bed, their fingers lazily tracing patterns across each other's skin."
    the_sister "You know, I was thinking... We should really find some way to thank [mc.name] for all his help."
    "[the_person.title] nods in agreement."
    the_person "He's done so much for us. It feels like he gave us our relationship."
    the_person "So, how do you think we should thank [mc.name]?"
    "[the_sister.title] lets out a contented sigh."
    the_sister "I don't know... I mean, he was really helpful. But what can we possibly give him that would be enough?"
    the_person "You know, he seemed to enjoy it when we were both involved..."
    "A mischievous smile crosses her face, as she continues in a low and suggestive voice."
    the_sister "Maybe we could invite him over for a little... Private party."
    "[the_sister.title] blushes deeply at the mention of this, but something inside her stirs at the thought."
    the_sister "You mean... Like a threesome?"
    "[the_person.title] smiles wickedly and rolls onto her side to face [the_sister.title]."
    the_person "Exactly, he was so into watching us together... I think it would mean a lot to him."
    "[the_sister.title] bites her lip, considering this idea. The memory of your reactions during their private sessions is enough to make her heart race."
    "She looks over at [the_person.title], who returns her gaze with equal parts curiosity and desire. Slowly, she nods."
    the_sister "Yeah, I think you're right, a threesome would be a great way to show him how much we appreciate everything he's done for us."
    "[the_person.title] smiles triumphantly and leans in to press their lips together in a passionate kiss."
    "As they continue to explore each other's mouths, their hands roam freely across the others' bodies, teasing and arousing with every touch."
    "Finally, they break apart, panting heavily."
    the_person "So... When do we invite your BIG brother to join the fun?"
    the_sister "I don't know... Maybe we should wait a few nights? Give us some time to prepare something special?"
    the_person "Sounds good, do you want to go shopping and pick out some special outfits for him too?"
    the_sister "Yeah, that would be great, really make the night all about him."
    "With that, they get back to work, and you can't wait to see what they have in store for you."
    $ del sister_outfit
    $ del person_outfit
    $ scene_manager.clear_scene()
    return

