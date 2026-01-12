
label Sarah_naomi_reconciliation_label(the_person):
    if not sarah.is_employee: # quick exit if she no longer works here
        return

    "As you are walking around, you suddenly hear a familiar voice calling you."
    the_person "Hey [the_person.mc_title], is that you?"
    $ the_person.draw_person()
    mc.name "Hello [the_person.title], long time no see. How are you these days?"
    $ the_person.draw_person(emotion = "sad")
    if the_person.relationship == "Married":
        the_person "To be honest, not so good. I recently divorced [the_person.SO_name]."
    else:
        the_person "To be honest, not so good. I recently broke up with my [the_person.so_title] [the_person.SO_name]."
    the_person "It seems we weren't as compatible as I thought."
    the_person "If you don't mind me asking, are you still seeing [sarah.fname]?"
    mc.name "Of course, she's one of my best employees."
    the_person "I would like to apologise to her, she's always been a good friend and we didn't part on the best terms last time..."
    mc.name "I remember, you were a real bitch the last time."
    the_person "I know and I'm really sorry about that. I shouldn't have said what I did, I guess I let [the_person.SO_name] influence me too much."
    mc.name "You know what, I will see what I can do for you, but first I need to talk this over with [sarah.fname]."
    $ the_person.draw_person(emotion = "happy")
    the_person "That would be awesome, I don't know how I could ever repay you."
    "You've got a few ideas for that and you doubt she is going to like them."
    if mc.phone.has_number(the_person):
        mc.name "Don't worry about it, I'll give you a call soon."
        the_person "Thanks again, talk to you soon."
    else:
        mc.name "Don't worry about it, just give me your phone number and I'll give you a call soon."
        $ mc.phone.register_number(the_person)
        the_person "Here you are, thanks again and talk to you soon."
    $ the_person.draw_person(position = "walking_away")
    "You should talk to [sarah.possessive_title] to give her a heads-up and discuss what just happened."

    python:
        the_person.SO_name = None
        the_person.relationship = "Single"
        # bring her back into the game
        the_person.set_override_schedule(None) # make Naomi free-roam
        clear_scene()
        add_talk_to_sarah_about_naomi_action()
    return

label Sarah_talk_about_naomi_label(the_person):
    $ the_person.draw_person()
    mc.name "Hey [the_person.title], can we have a talk in my office?"
    the_person "I'm not in trouble, am I?"
    mc.name "Don't worry, it's personal."
    the_person "Ok, let's go then."
    $ mc.change_location(ceo_office)
    "You gesture for [the_person.possessive_title] to sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "Guess who I bumped into the other day..."
    the_person "No clue, come on tell me..."
    mc.name "Your old friend [naomi.name]."
    "[sarah.fname] looks at you for a few seconds..."
    the_person "Okay, why should I care?"
    mc.name "Well, she wants to get back in touch with you, she's sorry about what happened last time."
    "She is still sceptical, what do you want to propose to her?"
    menu:
        "Get some revenge":
            mc.name "I think she deserves a little punishment for how she treated you last time."
            $ the_person.draw_person(position = "sitting", emotion = "happy")
            the_person "Yeah, I agree, she needs to be put in her place."
            mc.name "And since she's single again, we could make this a little more interesting for you."
            the_person "Oh, you little devil, what are you planning?"
            mc.name "Don't worry about that, do you trust me? I promise you will love it."
            the_person "Darn, now you made me really curious, but I will let you surprise me."
            mc.name "Perfect, now get back to work, you little slacker."
            $ the_person.draw_person(position = "back_peek")
            "With that she stands up and leaves your office, looking back to give you a wink."
            $ clear_scene()
            "Now let's invite [naomi.name] over to give her the 'good' news."
            $ mc.start_text_convo(naomi)
            mc.name "Good news, I talked it over with [the_person.fname]."
            mc.name "Can you come to my business next Wednesday afternoon?"
            naomi "That's just wonderful, I'll be there."
            $ mc.end_text_convo()
            $ add_naomi_visits_to_apologize_action()
            "The stage is set and you can execute your plan next Wednesday."
        "Be friends again\n{menu_red}Not written yet{/menu_red} (disabled)":
            pass
        "Nothing":
            mc.name "Looking at how she treated you, I would keep away from her."
            the_person "Yeah, I agree, I don't need her in my life. Things are just fine. Thanks for telling me though."
            mc.name "No problem, now back to work."
            $ the_person.draw_person(position = "walking_away")
            "With that she stands up and leaves your office."
            $ clear_scene()
    return

label Sarah_naomi_visits_to_apologize_label():
    if not sarah.is_employee: # quick exit if she no longer works here
        return

    "It's Wednesday afternoon and Naomi is visiting, so you go down to the lobby to pick her up."
    python:
        the_person = naomi
        scene_manager = Scene()
        mc.change_location(lobby)
        scene_manager.add_actor(the_person)
    the_person "Hello [the_person.mc_title], thank you again for doing this for me."
    mc.name "Hi [the_person.fname], good to see you, let's go to my office."
    $ mc.change_location(ceo_office)
    $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_center_flipped)
    "You motion her to take a seat."
    mc.name "Would you like some coffee?"
    the_person "Yes, [the_person.coffee_style], please."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        "You pour some of your serum enhanced coffee, to make her a little more open to suggestion."
    else:
        "Your pour some coffee and place the cup before her on the desk."
    mc.name "Right, since we are all set, shall I call in [sarah.fname]?"
    the_person "Perfect, I have been thinking about what to say for a few days now."
    "You make a quick call to [sarah.possessive_title] and wait until she knocks on your door, all the while [the_person.fname] is sipping on her coffee."
    $ scene_manager.add_actor(sarah, display_transform = character_right)
    sarah "Good afternoon, [sarah.mc_title]."
    if sarah_epic_tits_progress() > 1:
        the_person "Oh my god, [sarah.fname] you look absolutely stunning, your breasts... they are... amazing."
        $ the_person.change_arousal(10)
        $ scene_manager.update_actor(sarah, emotion = "happy")
    else:
        the_person "Hello [sarah.fname], it's good to see you, you look great."
    "Before you have any chance to say anything, [the_person.fname], starts apologising to [sarah.possessive_title]."
    the_person "I'm so sorry, for the last time, you are my best friend, you were always there for me, I shouldn't have listened to that shit bag..."
    "During her rambling, [sarah.possessive_title] sits down, without saying a word."
    $ scene_manager.update_actor(sarah, position = "sitting", emotion = "default")
    mc.name "SILENCE !!"
    "[the_person.fname] stops rambling and both girls look at you."
    mc.name "We are not here to listen to you babbling, [sarah.fname] is here for an apology."
    mc.name "So it's time we get to it, I think [the_person.fname] deserves a good spanking, don't you agree [sarah.title]?"
    $ scene_manager.update_actor(sarah, emotion = "happy")
    "For a second [the_person.fname] looks dumbfounded, but [sarah.title] starts to smile and nods to you."
    mc.name "Good, I thought you both would agree, [the_person.fname] please stand and lean over my desk."
    the_person "I... but... well..."
    $ scene_manager.update_actor(the_person, position = "standing_doggy", display_transform = character_center)
    mc.name "Right, [sarah.title], I think it would be only fair if you did the spanking."
    "[sarah.possessive_title!c] finally seems to figure out where you are going and leans into the role."
    $ scene_manager.update_actor(sarah, position = "stand4", emotion = "default")
    if not the_person.vagina_visible:
        sarah "Right, this won't do at all [the_person.fname], a good spanking is done on a bare butt, show it to me."
        "[the_person.fname] looks at you and only sees you nodding, reluctantly she moves her clothes out of the way."
        $ scene_manager.strip_to_vagina(the_person)
    $ the_person.change_arousal(15)
    $ sarah.change_arousal(15)
    sarah "Good, I see you are committed to apologising."
    $ scene_manager.update_actor(sarah, position = "stand5")
    "And with that [sarah.possessive_title] starts slapping away at [the_person.fname]'s naked ass cheeks."
    $ the_person.slap_ass()
    the_person "Oh shit!... Fuck!... Aaarg!"
    sarah "Now you little bitch, tell me how sorry you are!"
    $ the_person.slap_ass(update_stats = False)
    the_person "Aaah... I'm... shit... really... Ouch... SORRY!!"
    $ the_person.slap_ass()
    mc.name "I don't think she's really sorry yet [sarah.fname]."
    sarah "I agree, [sarah.mc_title]."
    while the_person.spank_level < 6:
        $ the_person.slap_ass()
        $ ran_num = renpy.random.randint(0,2)
        if ran_num == 0:
            the_person "Oh... I'm sorry [sarah.fname]! Oh god..."
            "She keeps her ass still, taking [sarah.possessive_title]'s punishment with pride."
        elif ran_num == 1:
            the_person "Please... ah... fuck... [sarah.fname], please... ouch..."
        else:
            "[sarah.possessive_title!c] keeps slapping her old friend's ass like there is no tomorrow."

        if the_person.spank_level % 2 == 1:
            "You look down at [the_person.fname]'s ass. It is [the_person.ass_spank_description]"

        if the_person.spank_level < 6:
            mc.name "Just keep going, there is some room for improvement."
            if the_person.spank_level > 4:
                "As you are watching this scene you see [the_person.fname]'s [the_person.pubes_description] pussy seems to get wet also."
        else:
            mc.name "I think that should be enough."

    "How to continue?"
    menu:
        "Degrade [the_person.title]":
            mc.name "Hey [sarah.title], I think she is ready to make some further amends."
            sarah "What did you have in mind, Sir?"
            mc.name "Why don't you take a seat?"
            $ scene_manager.update_actor(sarah, position = "sitting")
            mc.name "Well [the_person.fname], did you know that [sarah.fname] had a girl crush on you since you met?"
            $ scene_manager.update_actor(the_person, position = "stand2")
            the_person "Oh... I didn't know that, is that why you were so angry with me after that night? Because my ex didn't let you join us?"
            $ the_person.change_arousal(10)
            "[sarah.possessive_title!c] looks at her and quietly nods."
            mc.name "[sarah.title], why don't you show her how wet your little snatch is..."
            $ scene_manager.update_actor(sarah, position = "missionary", display_transform = Threesome_doggy_deluxe_girl_one_transform, z_order = 0)
            if not sarah.vagina_visible:
                $ scene_manager.strip_to_vagina(sarah, prefer_half_off = True)
            $ sarah.change_arousal(10)
            "As [sarah.possessive_title] lays back in her chair she reveals her already slick snatch to her friend."
            mc.name "[the_person.fname], why don't you show her how much you value her friendship, by making her cum with your tongue."
            if not sarah.tits_visible and sarah_epic_tits_progress() > 1:
                the_person "Could I also see your magnificent breasts, they just look amazing as far as I can tell."
                "[sarah.possessive_title!c] smiles and reveals her new boobs."
                $ scene_manager.strip_to_tits(sarah, prefer_half_off = True)
                $ the_person.change_arousal(15)
                the_person "Oh my, they look truly amazing, you have to give me the number of your doctor."
                $ scene_manager.update_actor(sarah, emotion = "happy")
                "[sarah.possessive_title!c] looks up at you and gives you a big smile and a wink."
                mc.name "Well, get down to business [the_person.title]."
            $ scene_manager.update_actor(the_person, position = "doggy" , display_transform = Threesome_doggy_deluxe_girl_two_transform, z_order = 1)
            $ sarah.change_arousal(20)
            "[the_person.fname] moves between her friend's legs, and slowly starts licking her [sarah.pubes_description] fold."
            sarah "Oh yes, right there, sweety."
            "While [the_person.fname] is doing her best to satisfy [sarah.possessive_title], you position yourself right behind her."
            mc.name "I think she needs some extra motivation, don't you agree [sarah.title]?"
            "[sarah.possessive_title!c] is only able to nod while enjoying the tongue of her friend. And with that you continue the spanking of [the_person.fname]."
            $ play_spank_sound()
            the_person "*SLAP*... Aargh... *SLAP*... hmm... *SLAP*... MMM..."
            $ the_person.change_arousal(20)
            $ sarah.change_arousal(20)
            "Occasionally, you move your hands between her legs to check how wet she is, and she's getting wetter by the minute."
            $ the_person.change_arousal(20)
            $ sarah.change_arousal(20)
            $ play_moan_sound()
            "[sarah.possessive_title!c] is close to orgasm, judging by her groans getting louder and louder."
            $ the_person.change_arousal(30)
            $ sarah.change_arousal(30)
            $ play_spank_sound()
            sarah "Oh yes, right there [the_person.fname], make me cum... Oh God, YES, I'm CUMMING!!!"
            $ sarah.have_orgasm()
            "As [sarah.possessive_title!c] starts squirting, her friend starts to shudder indicating that she's having an orgasm as well."
            $ the_person.have_orgasm()
            the_person "MMMM!!!... Oh my, this is so good, I never thought you could taste this good."
            $ sarah.increase_opinion_score("getting head", 2)
            sarah "You really know you way around down there, I came like a freight train."
            "After [the_person.fname] gives [sarah.possessive_title] a few more licks along her dripping slit, she stands up."
            $ the_person.increase_opinion_score("being submissive", 1)
            $ scene_manager.update_actor(sarah, position = "sitting", display_transform = character_right)
            $ scene_manager.update_actor(the_person, position = "stand4", display_transform = character_center_flipped)
            the_person "I'm really happy I was able to do this for you [sarah.fname], friends?"

        "End the punishment":
            mc.name "Right, that will be enough for now."
            sarah "Ah, well, if you think so [sarah.mc_title]."
            $ the_person.increase_opinion_score("being submissive", 1)
            $ scene_manager.update_actor(sarah, position = "sitting")
            $ scene_manager.update_actor(the_person, position = "stand4")
            the_person "Do you think we could be friends again, [sarah.fname]?"

    "You look at [sarah.possessive_title], so she knows it's her decision."
    sarah "Very well, let's consider this a friendship on trial basis and see where it goes from here."
    the_person "That's all I ever wanted."
    if sarah.vagina_visible:
        "The girls rearrange their outfits."
    else:
        "[the_person.fname] puts her clothes in order."
    $ scene_manager.update_actor(sarah, position = "default")
    $ scene_manager.apply_outfits()
    the_person "Why don't you give me a tour of this place [sarah.fname]?"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She grabs [sarah.possessive_title] by the hand and drags her out of your office."
    $ scene_manager.update_actor(sarah, position = "walking_away")
    "It seems they are off to a good start, let's see where this relationship goes in the future."
    $ scene_manager.clear_scene()

    $ naomi.event_triggers_dict["naomi_sarah_speaking_again"] = True
    $ add_naomi_asks_for_a_job_action(day + 10)
    # TODO: add bar date with Sarah and Naomi, where you end up at Sarah's place for a night of fun
    return

label naomi_asks_for_a_job_label():
    python:
        the_person = naomi
        scene_manager = Scene()

    if not mc.is_at_office:
        $ play_ring_sound()
        "While going about your business, you get a call from [sarah.fname]."
        sarah "Hi [sarah.mc_title], my 'old friend' [the_person.fname] is here and she wants to have a talk with you."
        mc.name "Right, show her to my office, I will be there shortly."
        "As you walk into your office, [the_person.fname] is sitting in front of your desk."
        $ mc.change_location(ceo_office)
        $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_center)
    else:
        $ scene_manager.add_actor(sarah)
        sarah "Hello [sarah.mc_title], remember [the_person.fname]?"
        mc.name "Of course."
        sarah "Well, she's in the lobby and wants to talk with you, I guess?"
        if mc.is_at(ceo_office):
            mc.name "Fine, I'll make some time."
            sarah "I will show her in then."
            $ scene_manager.update_actor(sarah, position = "walking_away")
            $ scene_manager.hide_actor(sarah)
            "You continue your work, until there is a knock on your door."
            mc.name "Yes, enter!"
            $ scene_manager.add_actor(the_person)
            mc.name "Hello [the_person.fname], come in and take a seat."
            $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_center)
        else:
            mc.name "Alright, show her to my office, I will be there shortly."
            $ scene_manager.update_actor(sarah, position = "walking_away")
            $ scene_manager.hide_actor(sarah)
            "You finish up your work and go back to your office."
            "As you walk into your office, [the_person.fname] is sitting in front of your desk."
            $ mc.change_location(ceo_office)
            $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_center)

    mc.name "Can I get you a coffee?"
    the_person "Yes, please."
    "You pick up the phone and ask [sarah.possessive_title] to bring in some coffee."
    $ scene_manager.add_actor(sarah, position = "stand3")

    mc.name "Now, [the_person.fname], tell me, what brings you here today?"
    the_person "Hello [the_person.mc_title], let me get straight to the point, I'm here to ask you for a job."
    mc.name "Ah, I see. Well, to be honest, I'm not looking for new employees at the moment."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    "This is not quite what she expected and she gets a desperate expression on her face."

    "[sarah.fname]'s eyes light up with an idea and she gets a smirk on her face."
    sarah "[sarah.mc_title]... perhaps you need someone to help you clean your house?"

    mc.name "Hmm, yes, thank you [sarah.fname], you can go."
    $ scene_manager.update_actor(sarah, position = "walking_away")
    "She gives you a smile and leaves your office."
    $ scene_manager.hide_actor(sarah)

    "You pause and consider [sarah.fname]'s suggestion for a while."

    menu:
        "Offer her the job":
            mc.name "You know, that's actually not a bad idea at all!  What would you say to that, [the_person.fname]?"
            $ scene_manager.update_actor(the_person, emotion = "happy")
            the_person "Really? That would be great."
            mc.name "I can pay you $35 per day and I expect to see you at my house every weekday for various tasks."
            the_person "That would be perfect, [the_person.mc_title]. I'll be there."
            mc.name "Good, you can start next week. One more thing, [the_person.fname]."
            the_person "Yes?"
            mc.name "I would like you to call me 'Sir' from now on."
            $ the_person.set_mc_title("Sir")
            $ the_person.set_possessive_title("your maid")
            the_person "Of course, [the_person.mc_title]!"
            $ scene_manager.update_actor(the_person, position = "walking_away")
            "After talking over the details, you shake hands as she stands up and walks out of your office."

            $ scene_manager.clear_scene()
            $ hire_naomi_as_maid(the_person)
            $ add_catch_naomi_slacking_off_action()
            "You send your mother and sister a text, letting them know you hired a maid for the house and she will start working next monday."

        "Decline\n{menu_yellow}Ends story line{/menu_yellow}":
            mc.name "No, I'm sorry, I can't offer you a job at the moment."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "I understand, sorry for wasting your time."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            "Slightly disappointed, she stands up and leaves."

    $ scene_manager.clear_scene()

    return

label catch_naomi_slacking_off_label(the_person):
    $ the_person.draw_person(position = "sitting")
    "As you walk into the kitchen you see [the_person.possessive_title] sitting at the kitchen table."
    mc.name "Hello [the_person.title]!"
    the_person "Ah... hello [the_person.mc_title]."
    mc.name "Please remind me, why are you here today?"
    the_person "I'm here to clean the house, [the_person.mc_title]."
    mc.name "And what are you currently doing?"
    the_person "Uhm... I was tired, so I took a short break."
    mc.name "Do I pay you for taking breaks?"
    the_person "No, you don't."
    mc.name "No, you don't, who?"
    the_person "Ah...you don't, [the_person.mc_title]."
    mc.name "It seems to me you are slacking off and I can't tolerate it when employees slack off."
    the_person "But [the_person.mc_title]..."
    mc.name "Silence, don't interrupt me when I'm speaking."
    mc.name "And since I'm reasonably satisfied with your work, I'm willing to let you off after a small punishment."
    mc.name "What do you think, [the_person.title]? Should I let you off with a punishment?"
    the_person "Ah, well, I guess it's better than getting fired."
    mc.name "Good, please stand here."
    $ the_person.draw_person(position = "stand2")
    "She slowly gets up and stands at the indicated position."
    mc.name "I think a good spanking is in order, to remind you why you're here."
    the_person "But... [the_person.mc_title], you don't have to do that. I promise I will do better."
    mc.name "You can show me that you mean it, by letting me spank you."
    "She sees the determination in your eyes and only nods her agreement."
    mc.name "Good, now bend over and put your hands on the table."
    $ the_person.draw_person(position = "standing_doggy")
    "She slowly bends over and puts her hands on the table, pushing out her buttocks."

    call maid_spank_loop(the_person) from _call_maid_spank_loop_catch_naomi_slacking_off

    mc.name "Good, remember this lesson."
    mc.name "Bad girls get punished, good girls get a reward."
    the_person "As you wish, [the_person.mc_title]."
    mc.name "Now get dressed and get back to work."

    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    "She rearranges her uniform and gets back to work."

    $ the_person.corruption_level += 1
    $ the_person.unlock_spanking()
    $ add_catch_naomi_masturbating_action()

    call advance_time() from _call_advance_time_catch_naomi_slacking_off
    return

label catch_naomi_masturbating_label(the_person):
    "As you walk into your bedroom you see [the_person.possessive_title] laying on your bed."

    $ the_person.outfit.remove_random_lower(top_layer_first = True)
    $ the_person.draw_person(position = "missionary")
    if the_person.vagina_visible:
        $ play_moan_sound()
        $ the_person.change_arousal(20)
        "She is moaning, while rubbing her wet pussy."
    else:
        $ the_clothing = the_person.outfit.get_lower_top_layer
        $ play_moan_sound()
        $ the_person.change_arousal(10)
        "She is moaning, while rubbing her pussy through her [the_clothing.display_name]."

    $ mc.change_locked_clarity(20)
    "Since she hasn't noticed you, you continue to watch her pleasing herself for a while."
    "You decide it has been enough and announce your presence."

    mc.name "Hello [the_person.title]."
    "She immediately stops, looks up at you and scrambles to her feet."
    $ the_person.draw_person()
    the_person "Ah, hello [the_person.mc_title], I was just..."
    mc.name "Playing with yourself on my bed?"
    the_person "Well, ah, I was tired and decided to lie down for a while and started thinking about you lying here..."
    mc.name "I see, hmmm... I guess it's time for another lesson."

    the_person "Please Sir, don't punish me again."
    mc.name "We will see."

    call maid_grope_loop(the_person) from _call_maid_grope_loop_naomi_masturbating

    the_person "Thank you, Sir. I appreciate you taking the time to improve my skills."
    mc.name "You're welcome [the_person.title]. Now back to work."

    the_person "Yes, Sir."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "walking_away")
    "You watch as she rearranges her uniform and gets back to work."

    $ the_person.corruption_level += 1

    call advance_time() from _call_advance_time_catch_naomi_masturbating
    return
