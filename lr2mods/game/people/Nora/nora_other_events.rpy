##################################################
# Nora and Stephanie's Saturday Night Bar Events #
##################################################

#The next set of events define Saturday night bar events with Nora and Stephanie
#Early in the game, it is just some dialogue that turns into a bar date with Stephanie
#Nora may give MC updates on Serums and other things going on at the University
#Later on, Nora stays and has bar date with MC instead
#After a certain point in the storyline, it flows instead into Nora and Stephanie's teamup
#This event is split into sections for organization

# 1: Meet just Nora at the bar. Use this section to setup contracts with MC's business
# 2: Stephanie joins the group at the bar. Use this section to update Nora and MC quest lines, such as the new unstable serum testing
# 3: Who sticks around for a night of drinking.
# 4: If both, call the teamup scene intro.

#This event is Saturday[5] Night [4]

label nora_bar_meetup_intro_label(the_person = nora):    #Room entry with Nora event.
    $ the_person.set_event_day("nora_bar_meetup_intro_label")
    $ add_nora_bar_meetup_intro_action()
    "You step into the bar. After a quick look around, you spot [nora.possessive_title] near the back, at a table by herself."
    $ the_person.set_event_day("nora_weekly_meeting")
    $ scene_manager = Scene()
    $ scene_manager.add_actor(nora, position = "sitting", display_transform =character_right_flipped)
    if nora.event_triggers_dict.get("bar_intro_state", 0) == 0:
        $ add_nora_initial_closing_visit_action()   #Enable her lust story after this
        "You walk over to her and sit down. She nods at you as you sit. It has been three weeks since you last sat down with her."
        nora "Hello [nora.mc_title]. How was your first week in operations?"
        mc.name "It went as good as I could have hoped, I think. Starting a new business has been very challenging."
        nora "I imagine so. Any major challenges so far?"
        mc.name "Honestly, my biggest concern right now is just making enough money to pay bills. It turns out running a fledgling pharmaceutical company is expensive."
        nora "You... you don't have an outside source of funding?"
        mc.name "I do, but it is limited. And that money is just about gone."
        "[nora.title] sighs and shakes her head."
        nora "I may be able to use my leverage at the university to get you some favourable contracts for your existing serum. I'll see what I can do."
        mc.name "Contracts?"
        nora "Yes. Dear me... you know how contracts work... right?"
        mc.name "Umm yeah, totally..."
        "As you are talking, [stephanie.title] approaches the table."

    else:
        "You walk over to her and sit down. She nods at you as you sit."
        call nora_obedience_branch_label() from _nora_obedience_branch_update_01
    if nora_teamup_request_check():
        call nora_teamup_request_intro_label(the_person) from _nora_teamup_bar_request_01
    call nora_bar_meetup_stephanie_meeting_label([nora, stephanie]) from _nora_bar_meetup_step_01
    return


label nora_bar_meetup_stephanie_meeting_label(the_person):
    $ scene_manager.add_actor(stephanie, position = "sitting", display_transform = character_center_flipped)
    "[stephanie.possessive_title!c] joins you at the table."
    if nora.event_triggers_dict.get("bar_intro_state", 0) == 0:
        stephanie "Hey, sorry if I'm a little late."
        mc.name "I just got here as well."
        nora "Yes. You are right on time. [stephanie.fname], could you enlighten me about something?"
        stephanie "Sure. What is it?"
        nora "Has [nora.mc_title] shared with you any financial details of his business?"
        stephanie "Umm, no, not really."
        "She sighs."
        nora "I tell you what, I'll reach out to a few industry contacts and see if I can get you a few local contracts."
        nora "That should help you stay afloat for a little bit anyway. Although the contracts probably won't be very profitable until you prove yourself."
        "[stephanie.title] looks at you."
        stephanie "That would be helpful. I could push the details to your email and you could sort through them in your office."
        stephanie "I don't really have the time to manage them for you though. Maybe eventually you could hire someone for that?"
        nora "Alright, I'll see what I can dig up this weekend for you. I'll poke around at the university next week also and see what I can find out about a contract for them also."
        mc.name "Thank you again [nora.title] for your help."
        nora "Yes. I certainly hope this partnership can eventually yield benefits for *both* sides."
        mc.name "I'm sure it will."

    $ unstable_check = nora_unstable_serum_dialogue_check()
    if unstable_check:
        call nora_unstable_serum_label(the_person) from _unstable_dialogue_quest_line_01
    $ del unstable_check

    call nora_bar_meetup_plan_night_label(the_person) from _nora_bar_meetup_progression_01
    return



    # mc.name "Sorry, I have other commitments for tonight, but text me if you two need anything."
    # "[stephanie.title] seems pretty disappointed that you aren't staying, while [nora.possessive_title] just shakes her head."
    # nora "Better things to be doing? On a Saturday night? That seems unlikely, but I'm not here to babysit you."
    # "You take your leave of the table as the two girls return to their discussion."


label nora_bar_meetup_plan_night_label(the_person):
    mc.name "Alright, that is enough business for tonight."
    nora "Indeed."
    if nora.event_triggers_dict.get("bar_meetup_both_stay", False):
        stephanie "I've been looking forward to this all week. Are you going to stay and have a few drinks with us, [stephanie.mc_title]?"
        "[nora.title] looks at you, awaiting your answer."
        menu:
            "Stay for drinks":
                mc.name "Of course I'm staying. Let's drink some alcohol and have some fun tonight."
                stephanie "Yay! That sounds like fun."
                nora "We'll go and save us a table if you could go get the first round."
                mc.name "Alright, I'll be right back."
                call bar_date_group_main_label([nora, stephanie], drinks_only = True) from _steph_nora_teamup_group_date_02
                # TODO call a cab, etc
                call stephanie_nora_teamup_repeat_intro_label() from _stephanie_nora_teamup_training_intro_label_01
                pass
            "Call it a night instead":
                mc.name "Sorry, but alcohol is not on my agenda for the night. Good night to you both, I need to be off."
                "The girls both seem a little disappointed, but they hide it."
                stephanie "Alright, be boring. Goodnight!"
                nora "Until next time."
                "You say goodnight to the women and depart the table."
                $ scene_manager.clear_scene()
                return

    elif nora_teamup_request_check():
        if nora.event_triggers_dict.get("steph_teamup_stage", 0) == 0:
            nora "[stephanie.fname], do you want to stay and have a few drinks with me?"
            stephanie "With... with you? Sure! That sounds like so much fun!"
            stephanie "But what about [stephanie.mc_title]?"
            nora "Oh, I suppose we could let him join us."
            stephanie "I don't know... what do you think?"
            "She turns to you."
            mc.name "I'd love to get drinks with both of you. We could have a fantastic night together!"
            stephanie "Oh! Okay! Let's do it!"
            mc.name "Let me grab the first round right now, stay here!"
            "[nora.title] gives you a quick wink when you get up. You quickly head over to the bartender with the girls drink orders."
            "You quickly pay for the drinks. You take a look at [stephanie.possessive_title]'s drink."
            "You need to add a serum to enhance her suggestibility to it."
            $ serum = get_random_from_list(mc.inventory.get_serums_with_hidden_tag("Suggest"))
            if serum:
                $ stephanie.give_serum(serum, add_to_log = True)
                "You grab a random one from your bag and drop it in, quietly."
            else:
                "Somehow, you don't have one. This is actually an error, post about this on the discord and chew out Starbuck."
                return
            "You return to the table with the drinks, making sure not to mix them up."
        elif nora.event_triggers_dict.get("steph_teamup_stage", 0) == 2:
            mc.name "[stephanie.title], think you are up for another night of fun with me and [nora.title]?"
            stephanie "Yeah! I had so much fun last time, although after that last drink it was a bit of a blur..."
            stephanie "What do you say, [nora.fname]? Are we drinking together again tonight?"
            nora "Oh, I suppose we could do that."
            nora "[nora.mc_title], could you grab the first round for us?"
            mc.name "Of course."
            "You stand up. Both girls are giving you knowing looks, although only one of them knows what the real outcome of the night is about to be..."
            "You head to the bar and order the first round."
            "You quickly pay for the drinks. You take a look at [nora.possessive_title]'s drink."
            "You need to add a serum to enhance her suggestibility to it."
            $ serum = get_random_from_list(mc.inventory.get_serums_with_hidden_tag("Suggest"))
            if serum:
                $ stephanie.give_serum(serum, add_to_log = True)
                "You grab a random one from your bag and drop it in, quietly."
            else:
                "Somehow, you don't have one. This is actually an error, post about this on the discord and chew out Starbuck."
                return
            "You return to the table with the drinks, making sure not to mix them up."
        "You watch as both women take sips from their drinks. One is drugged, and one is not."
        "It is time to get the night started."
        # PAss in shots because we don't want the girls to get actually wasted, it would break the group.
        call bar_date_group_main_label([nora, stephanie], drinks_only = True) from _steph_nora_teamup_group_date_01
        if nora.is_wasted:
            $ nora.increase_drink_level(-2)
        if stephanie.is_wasted:
            $ stephanie.increase_drink_level(-2)
        "After you finish your drinks, [nora.title] puts her arm around [stephanie.possessive_title]."
        nora "You two, this has been so much fun. Why don't we go back to my place? The three of us?"
        stephanie "Whoa... really!?! I've never been to your place before..."
        nora "[nora.mc_title], would call us a taxi?"
        mc.name "Of course. I'm on it."
        "One quick call and a few minutes later, the three of you are piling into the back of a taxi cab."
        if nora.event_triggers_dict.get("steph_teamup_stage", 0) == 0:
            call stephanie_nora_teamup_intro_label() from stephanie_nora_teamup_first_intro_01
        if nora.event_triggers_dict.get("steph_teamup_stage", 0) == 2:
            call stephanie_nora_teamup_revenge_label() from stephanie_nora_teamup_revenge_intro_02
        return


    elif nora.event_triggers_dict.get("bar_meetup_nora_stay", False):
        "You could ask either girl to stay and have a few drinks with you. Who do you choose?"
        menu:
            "[nora.title]":
                mc.name "I'm gonna stay and have a few drinks with [nora.title]."
                mc.name "[stephanie.title], I'll see you on Monday?"
                stephanie "Ah, of course. See you then."
                $ scene_manager.remove_actor(stephanie)
                "She quickly gets up and departs. She is a little disappointed, but you know you'll see her soon."
                nora "I'll stay here, while you get the first round."
                mc.name "Sure thing."
                $ scene_manager.hide_actor(nora)
                call bar_date_main_label(nora, drinks_only = False) from _nora_steph_drinks_nora_only_02
                # TODO back to nora's place
            "[stephanie.title]":
                mc.name "Thanks for meeting us [nora.title], I'm going to stay and have a few drinks with [stephanie.title]."
                nora "Alright, [nora.mc_title]. I'll see you next week [stephanie.fname]."
                stephanie "See ya!"
                $ scene_manager.remove_actor(nora)
                "She gets up and leaves, leaving you with [stephanie.possessive_title]."
                stephanie "I'm gonna hit up the restroom and fresh up a bit."
                mc.name "I'll get us the first round and meet you back here."
                stephanie "Okay!"
                $ scene_manager.hide_actor(stephanie)
                call bar_date_main_label(stephanie, drinks_only = False) from _nora_steph_drinks_steph_only_02
                # TODO back to stephanie's place
            "Call it a night instead":
                mc.name "Sorry, but alcohol is not on my agenda for the night. Good night to you both, I need to be off."
                "The girls both seem a little disappointed, but they hide it."
                stephanie "Alright, be boring. Goodnight!"
                nora "Until next time."
                "You say goodnight to the women and depart the table."
                $ scene_manager.clear_scene()

    elif nora.event_triggers_dict.get("nora_stay_for_drinks_intro", False):
        "Before [nora.title] can excuse herself, [stephanie.possessive_title] suddenly stands up."
        $ scene_manager.update_actor(stephanie, position = nora.idle_pose)
        stephanie "Welp, I need to be off. I started a new tennis workout and I have to be at the gym early tomorrow."
        stephanie "You two will just have to have a few drinks without me. See you next week [nora.fname]!"
        nora "What? You're leaving already...?"
        $ scene_manager.update_actor(stephanie, position = "walking_away")
        "Without waiting for her to finish her sentence, [stephanie.title] walks away, leaving you with [nora.possessive_title]."
        $ scene_manager.hide_actor(stephanie)
        "[nora.possessive_title!c] looks at you, eyes wide with surprise."
        mc.name "Her tennis program is really great. Anyway, want to have a couple drinks? My treat. For all the help you've given me so far."
        "[nora.title] gives you a questioning look, but relents."
        nora "Fine. Let's have a few drinks. Go get me a Manhattan, I need to use the restroom anyway, and we'll see how things go."
        $ nora.event_triggers_dict["favorite_drink"] = "Manhattan"
        mc.name "Alright, one Manhattan coming right up."
        call nora_first_bar_date_label() from _first_bar_date_with_nora_01

    else:
        "[nora.possessive_title!c] stands up."
        $ scene_manager.update_actor(nora, position = nora.idle_pose)
        nora "Well, this has been productive, but I must be off. You two have fun tonight."
        stephanie "Aww, you're no fun! Why don't you stay and have a couple drinks with us?"
        nora "I'm afraid I'm much too busy to be out drinking tonight. Goodnight."
        $ scene_manager.update_actor(nora, position = "walking_away")
        "She turns and leaves you at the table with [stephanie.title]."
        $ scene_manager.remove_actor(nora)
        stephanie "Alright, I'm going to use the restroom and freshen up a bit. I'll meet you at the bar in a minute. Can you get me a Piña Colada?"
        $ stephanie.event_triggers_dict["favorite_drink"] = "piña colada"
        mc.name "Sure, I'll meet you over there."
        $ scene_manager.hide_actor(stephanie)
        if nora.event_triggers_dict.get("bar_intro_state", 0) == 0: #First run through. Do the beer pong intro series.
            $ nora.event_triggers_dict["bar_intro_state"] = 1
            "This should be fun. [stephanie.title] has always been a bit of a party girl."
            "You bet if you can get a few drinks in her, you might be able to make your way back to her place tonight..."
            call stephanie_first_bar_date_label() from _first_bar_date_with_steph_01
        else:
            "[stephanie.title] gets up and leaves you at the table. You think about things for a bit before getting up."
            "You really wish you get [nora.title] to stay and have drinks with you sometime. Maybe if you managed to make an impression on her?"
            "Get her to like you a little bit, or even if she was just a little bit more obedient..."
            "You stand up and head towards the bar."
            $ add_nora_stephanie_bar_setup_action()
            call bar_date_main_label(stephanie, drinks_only = False) from _nora_steph_drinks_steph_only_01
            return

    return





### Unstable Serum Quest Line ###
# This quest line takes place during Nora and Stephanie meetings
# Begins shortly after unlocking tier 1 serums
#

label nora_unstable_serum_label(the_person):
    # $ the_person = nora
    if nora.event_triggers_dict.get("unstable_serum_stage", 0) == 0:    #Intro
        $ nora.event_triggers_dict["unstable_serum_stage"] = 1
        nora "So, I heard from [stephanie.title] that you've made a pretty large advancement, but she wouldn't give me any details. Care to share?"
        mc.name "Wish I could, but those are company secrets."
        "[nora.title] just sighs and shakes her head."
        nora "Of course. But for the sake of satisfying my curiosity, maybe we could make a trade?"
        "She pulls a folder from her bag and sets it on the table in front of her."
        "[stephanie.possessive_title!c] shoots you a quick glance. She has definitely piqued her interest."
        nora "You may or may not realize it, but you have a competitor. Right now, the university is working with them, much to my annoyance."
        mc.name "You don't like the company?"
        nora "No. The man who runs it is a horrible man. I've heard some awful stories coming out of there."
        nora "In fact, the head researcher there recently departed the company in mysterious circumstances. She was widely recognized as one of the most knowledgeable experts in the field."
        mc.name "Is that why you want to know about our breakthrough? To help them?"
        "[nora.possessive_title!c] sighs again and shakes her head."
        nora "Fuck no. I hate the place, weren't you paying attention?"
        nora "I want to know so that if I see similarities in development there, I can better understand what is happening."
        nora "So far, they have taken a completely separate development process that is diverging rapidly from yours. But the more I know about both paths the better I can judge the similarities."
        nora "Call it a professional courtesy. Besides, you still owe me a lab technician."
        "You point toward the folder."
        mc.name "And what are you offering in exchange?"
        nora "It is a prototype formula that the other company is working on. They can't figure out why it isn't working the way they expected it to, but I suspect you may be able to make something of it with your divergent research patterns."
        "You look at [stephanie.title]. She gives you a nod."
        mc.name "What we discovered was a link to our serum effectiveness and… let's call it natural hormonal states."
        mc.name "Serums suddenly got much more effective if the test subject had an orgasm while under the effects. With multiple orgasms increasing the effects as well."
        "[nora.title] looks at you in disbelief. She looks back at [stephanie.title], who just nods her agreement."
        stephanie "The results are conclusive. With permission, I could forward you the data itself."
        nora "Huh. I can't say I saw that coming. I wouldn't mind a peek, an extra set of eyes could be helpful to verify the data…"
        mc.name "I suppose so. Go ahead and email her that first thing on Monday, [stephanie.title]."
        nora "Ahh, not email. I don't trust the school servers anyway. A USB stick or something similar would be better, I think."
        stephanie "I'll make one up for next week when we get together."
        "You look down at the folder in front of [nora.title]. She catches your gaze."
        nora "Right."
        "She pushes the folder across the table to you."
        nora "Inside the folder is a design spec for a serum that is *supposed* to make women more receptive to sexual advances. However, the company has had limited success in their trials."
        nora "My understanding is that they have stopped working on it, and that it only has an effect on the most frigid of women."
        nora "However, when I was running through the design specifications, something about it just didn't seem right. I thought maybe you could take a look at it. At your leisure, anyway."
        "You open the file and glance through it briefly. She's right, this design has similarities to your own traits, but formula is very… basic?"
        "It doesn't seem to have any realistic production tolerances. Nor does it seem to have any dosage guidelines."
        "You close the folder and push it over to [stephanie.title]."
        mc.name "At first glance, the production techniques and dosage seem to be… basic."
        nora "Ah, well let me know what you find, but be careful with this formula. It might draw a bit of unwanted attention to your business if your competitor were to discover you have it."
        mc.name "Understood."
        "[stephanie.possessive_title!c] takes the folder and puts it away into her bag."
        "[nora.title] is looking for you to research the trait. Reach 10%% mastery to learn more about it."
        mc.name "Now, who wants a drink?"
        $ nora.story_tracker.start_path(nora, "Unstable Serums")
        # $ nora.event_triggers_dict["unstable_serum_step"] = 0
        return

    elif nora.event_triggers_dict.get("unstable_serum_stage", 0) == 1 and nora_unstable_slut_trait.mastery_level >= 10:
        $ nora.event_triggers_dict["unstable_serum_stage"] = 2
        nora "How is going with that trait I sent you?"
        mc.name "The chemical composition is extremely volatile. After initial research, we have found that less than a percent makes it through the digestion process and into the bloodstream."
        stephanie "We've had some progress though. By continually refining our synthesization process we've been able to see significantly increased uptake."
        nora "So… does it do what they said it would do?"
        mc.name "It does, and we've been able to increase the effect considerably, and combinations with some of our suggestibility serums also seems to enhance it some."
        mc.name "However, I would say that the maximum effectiveness still has to be determined. It seems that every time we review the serum and its synthesization, we find new ways of improving it."
        "[nora.title] processes what you said for a few moments, then nods."
        nora "Fascinating. I wonder if the creators realized what they had on their hands… or if that was the reason their head researcher disappeared."
        "She seems troubled for a moment."
        nora "[nora.mc_title], you do realize that you have obligations, right? Not just to push the limits of science, but to use what you learn carefully?"
        mc.name "Of course. You mentioned the other company's former head researcher before… did he really just disappear?"
        nora "She. And yes. I did a bit of my own research, and as far as I can tell, one day she just stopped showing up at the other company and dropped off the face of the Earth."
        nora "Her apartment was foreclosed on and all her stuff was still there, and when I checked with the police station, no missing persons reports had been filled out."
        nora "By all indications, she was a brilliant researcher. I've been trying to locate her, but so far I've been unsuccessful."
        mc.name "Interesting. If we could find her, she might be able to provide insights on what is going on there."
        nora "Yes. But for now, I have something else for you."
        "[nora.possessive_title!c] pulls out another folder."
        mc.name "You have another stolen serum trait?"
        nora "I do. And from initial research, it appears to have the exact same issues as the other one I gave you."
        nora "However, instead of reducing sexual inhibitions, this one appears to be made to increase loyalty and obedience."
        nora "Initial research is promising, but once again, the CEO of the other company abandoned this formula since it only had marginal results."
        "She slides the folder across the table to you. You take a quick glance."
        "You see from the limited testing data that it softened the independence of only the wildest of subjects, but notice the chemical compound has a very similar structure to the last one."
        "You slide the folder over to [stephanie.title] who takes it and looks through it, then puts it in her bag."
        "Another trait to research for [nora.title]. Reach 10%% mastery to learn more about it."
        mc.name "I'll see what we can do. Now, who wants a drink?"
        $ nora.story_tracker.advance_path(nora, "Unstable Serums")
        $ nora.event_triggers_dict["unstable_serum_step"] = 1
        return


    elif nora.event_triggers_dict.get("unstable_serum_stage", 0) == 2 and nora_unstable_obedience_trait.mastery_level >= 10:
        $ nora.event_triggers_dict["unstable_serum_stage"] = 3
        nora "How is going with that trait I sent you?"
        mc.name "We've made considerable progress with it. It indeed has all the same hallmarks as the last one you gave us."
        mc.name "The composition is extremely volatile, and specialized production methods are needed for it to be used effectively."
        stephanie "Most of the methods are unique as well, so we can't combine the two designs you gave us into a single dose. The two designs just aren't compatible."
        mc.name "We've been able to refine it to the point that it has a definite effect on all but the most loyal of women, but again, it seems we've barely scratched the surface of how effective this trait can be."
        nora "Interesting. Once again, the CEO is overlooking the possibilities of subtle designs while focusing on only the flashiest ones."
        mc.name "Who is this guy, and what is going on with them?"
        nora "Well, I've actually got a lead I'm working on. I've learned that the former head researcher was actually fired after an accident in the lab, but the details of the accident are sparse."
        nora "Allegedly the accident really messed with her, and was no longer fit for her position."
        nora "I managed to get a hold of an informant in the company and learned that she was actually moved from one council member to another for purposes of employment."
        mc.name "Wait, the CEO is a city council member?"
        nora "Yes. Of the five council members, he is the one who represents the health sector."
        mc.name "Interesting. I wonder which other member he may have moved her to."
        nora "I'm looking into it. But, in the meantime, I have another formula for you to look at."
        "[nora.possessive_title!c] pulls out yet another folder and sets it on the table."
        nora "When I learned about this formula, I hesitated to bring it here, but after careful consideration, I think it is important for you to look into it."
        "She slides you the folder and you open it and begin to look over the design."
        nora "This is another unstable trait, but this one appears to increase emotional attachment."
        mc.name "A… love potion?"
        "She sighs and rolls her eyes."
        nora "Yeah, it sounds ridiculous, and if I ever find out you're dropping this thing in my drinks I'll have you strung up in the city square."
        "You slide the folder over to [stephanie.title] who takes it and looks through it, then puts it in her bag."
        "Another trait to research for [nora.title]. Reach 10%% mastery to learn more about it."
        mc.name "I'll see what we can do. Now, speaking of drink, who wants one?"
        $ nora.story_tracker.advance_path(nora, "Unstable Serums")
        $ nora.event_triggers_dict["unstable_serum_step"] = 2
        return


    elif nora.event_triggers_dict.get("unstable_serum_stage", 0) == 3 and nora_unstable_love_trait.mastery_level >= 10:
        $ nora.event_triggers_dict["unstable_serum_stage"] = 4
        #Outline
        "In this label, [nora.title] reveals that she has tracked down the former head researcher."
        "This will eventually lead to an alternate path for unlocking Candace, but it hasn't been written yet."
        "At the end, she also gives you access to the final two unstable serum traits!"
        "Hooray drugs!"
        $ nora.story_tracker.advance_path(nora, "Unstable Serums")
        $ nora.event_triggers_dict["unstable_serum_step"] = 3
        return

    elif nora.event_triggers_dict.get("unstable_serum_stage", 0) == 4:
        "In this label, we discuss progression of the unstable serum doses that have been shared with the business."
    else:   #Needs to work on mastery
        nora "How is going with that trait I sent you?"
        mc.name "Research is just beginning. The chemical itself is very volatile."
        stephanie "I think we need more research before we can draw any conclusions about it."
        nora "I see. Well let me know when you've made progress."


    return

label nora_teamup_request_intro_label(the_person):
    if nora.event_triggers_dict.get("steph_teamup_stage", 0) == 0:
        nora "So... I've been thinking about something."
        nora "You said that when [stephanie.fname] took a serum and then had an orgasm, she entered into some sort of... trance?"
        mc.name "That's right. It made her very open to suggestion. Almost like a hypnosis effect."
        "She looks at you for several seconds."
        nora "I want to see it."
        mc.name "Huh?"
        nora "You heard me. You have some serum with you, don't you?"
        mc.name "I... err... yes?"
        nora "[stephanie.fname] is head over heels for you. You may not realize it, or care, but she would do anything you asked."
        nora "Tonight, suggest that we BOTH stay and have drinks with you. When you get her a drink, slip a serum into the drink."
        nora "We'll stay and get drunk, and then at my suggestion we'll go back to my place. Then we can put her in a trance."
        mc.name "[nora.title]... are you suggesting we drug your former lab assistant?"
        nora "Yes, that is exactly what I am proposing."
        "Holy shit. You remind yourself to watch out for [nora.title] and to keep an eye on her ambitions in the future. Crossing her would not be smart."
        nora "Just do it. We'll all have a little fun tonight. Okay?"
        mc.name "Okay..."
    if nora.event_triggers_dict.get("steph_teamup_stage", 0) == 2:
        nora "Do you have another serum for tonight?"
        mc.name "Yeah. Are you wanting to put [stephanie.fname] in a trance again?"
        nora "Yes, I have other things I want to explore. For science of course."
        mc.name "Of course. Yeah I have one. I'll drop it in her drink."
        "Of course, you won't be dropping one in [stephanie.possessive_title]'s drink tonight."
        "You and her made plans to turn the tables on [nora.title]. Make sure to give her a suggestibility serum instead!"
    return

label nora_stephanie_bar_setup_label():
    $ the_person = stephanie
    "You think about the previous weekend when you met up with [nora.title] and [stephanie.possessive_title]."
    "It would be useful if you could convince [nora.title] to stay after the meeting with you for drinks."
    "It would give you a much easier time to pass her a serum or two, and getting more friendly with her could be good for you, in multiple ways."
    "You swing by the research division to talk to [stephanie.title] about it. Maybe you could get her to help you out."
    $ mc.change_location(rd_division)
    $ the_person.draw_person(position = "sitting")
    "You walk over to her desk. She is working, but looks up when you approach and nods."
    mc.name "Hey [stephanie.title], I was hoping I could ask you for a favour."
    stephanie "Sure. What do you need?"
    mc.name "I was wondering, next time we meet with [nora.fname] on Saturday night, if you could pretend you can't stay and have drinks."
    stephanie "What? But I love going out on Saturday nights..."
    mc.name "I know, but I need to find an opportunity to get more friendly with her. If you had to leave, I could pressure her into staying for drinks."
    "She crinkles her nose as she thinks about it."
    stephanie "Are you asking me to be your... wing man?"
    mc.name "Look, I'm not even sure it will work, but if I can convince her to stay, getting her to be more friendly could really help our business."
    "[stephanie.title] rolls her eyes."
    stephanie "Are you going to sleep with her?"
    mc.name "What? I... I mean, I don't know. Maybe? But I really doubt that is going to be on the table."
    mc.name "Seriously though. She is being so standoffish, I need an excuse to spend some time alone with her."
    stephanie "Ugh, fine. Next time I'll make up some excuse about having to leave. But you'll make it up to me, okay?"
    mc.name "Of course."
    "[stephanie.title] turns back to her computer and resumes her work."
    "Next time you meet with [nora.possessive_title] at the bar, you will have an opportunity to convince her to stay and have some drinks with you!"
    $ nora.event_triggers_dict["nora_stay_for_drinks_intro"] = True
    return

# First time dates

label stephanie_first_bar_date_label():
    $ the_person = stephanie
    $ bar_date_add_available_game("pong")
    "You head over to the bar and order drinks for you and [the_person.title]."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    "If you are quick, you could sneak in a serum..."
    call give_serum(the_person) from _call_give_bar_date_sneaky_boi_steph_01
    if _return:
        "You drop the serum in to the drink with no one noticing, then return to [the_person.title] and hand it to her."
    else:
        "You just grab the drinks and return to [the_person.title], handing it to her."
    $ the_person.draw_person()
    stephanie "Thanks! Oh this looks perfect. They make them so good here."
    "[stephanie.title] gratefully accepts your drink and takes a large sip from it."
    $ the_person.increase_drink_level(1)
    stephanie "So, what do you want to do tonight? There's lots of games to play here, if you want!"
    "You look around the bar. There ARE a ton of games here. Darts, arcade, billiards. But you honestly don't really know how to play any of them..."
    mc.name "Ummm, to be honest, I don't come here very often. Any suggestions?"
    stephanie "Ah yes, I forget sometimes that you really are a nerd."
    stephanie "Well, if you want to play something just for fun, nothing beats a quick round of beer pong!"
    stephanie "There's a table open over there. Let me show you!"
    $ the_person.draw_person(position = "walking_away")
    "She takes your hand and drags you over to a table next to the bar. She quickly buys a couple of beers and begins pouring them into cups on both sides."
    $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
    "She steps around the far side of the table and holds up a ping pong ball."
    stephanie "Alright, don't worry! It's really simple. You just take the ball and try to bounce it into the cups on the other side of the table..."
    "She quickly explains to you the rules of the simple drinking game. It seems easy enough, so you start to play."
    "While the rules are simple, it takes a surprising amount of focus and dexterity to play well."
    "You can tell [stephanie.title] is taking it easy on you, but she still wins easily, hitting your last cup while she still has three on the table."
    stephanie "Yes! Normally, whoever lost has to do an extra shot for losing, but we're just playing for fun tonight, so I won't make you!"
    "She picks up her remaining cups and drinks them quickly while you finish your own."
    $ the_person.increase_drink_level(1)
    "It is clear she is having a good time, and she enjoys her alcohol."
    mc.name "Shots eh? Well, we could always do some together, anyway."
    stephanie "Oh! Feeling adventurous? I'd like that!"
    call bar_date_do_shots_label(the_person) from _scripted_bar_shots_stephanie_01
    stephanie "Ohhh, this has been such a fun night. I think I need to slow down a little bit though..."
    stephanie "Why don't we just go relax at a table for a little bit? I want one last drink."
    mc.name "Certainly."
    "You order a final round with the bartender."
    $ the_person.increase_drink_level(1)
    call bar_date_relax_label(the_person) from _scripted_bar_relax_stephanie_01
    stephanie "Mmm, thank you for the fun night, [stephanie.mc_title]. You're so much fun."
    stephanie "I really wish you had kept in touch better. I missed you, ya know?"
    mc.name "I'm sorry, I meant to, but things were very stressful for a while."
    stephanie "Yeah yeah, I understand. Hey... do you wanna get out of here?"
    stephanie "We could go back to my place, if you wanted to I mean..."
    "You brain is addled a bit from the alcohol, but you're pretty sure she's inviting you to her place for a little intimate fun."
    "You could say no, but doing so would probably really hurt her."
    menu:
        "Go to her place":
            pass
        "Order her a cab":
            mc.name "Sorry, I can't tonight, but let me get you a cab home."
            $ stephanie.change_love(-5)
            $ stephanie.change_happiness(-30)
            $ stephanie.change_obedience(10)
            stephanie "Ahh... of course..."
            "[stephanie.title] doesn't say much after that, but you make good on getting her cab. You walk her out."
            $ the_person.draw_person(position = the_person.idle_pose)
            $ mc.change_location(downtown)
            stephanie "Goodnight. I'll see you at work."
            mc.name "Goodbye."
            $ clear_scene()
            "You think you see a tear in her eye as she turns way and gets quietly into the cab."
            "You don't like hurting her like this, but you have to be careful. You don't want to get tied down to a girl right now, and maintaining a professional relationship is the key to that."
            "You head home for the night."
            $ mc.change_location(bedroom)
            call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_steph_intro_01
            return
    mc.name "Yes, I would love to go back to your place, [stephanie.title]."
    $ stephanie.change_love(5, 40)
    $ stephanie.change_happiness(30)
    $ stephanie.change_obedience(10, 140)
    "She flashes you a positively beaming smile. She stands up and you join her."
    stephanie "Great! It isn't far from here, let's go!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "You step out of the bar and walk the short distance to her apartment building."
    "She leads you to the front door and invites you inside."
    $ the_person.add_situational_slut("Romanced", 20, "What a wonderful date!")
    $ mc.change_location(the_person.home)
    "You and [the_person.possessive_title] step inside."
    "She doesn't leave any pretenses, leading you straight to her bedroom."
    $ the_person.change_to_bedroom()
    mc.name "Wow. After the craziness of last summer, I finally get to see the inside of [stephanie.title]'s bedroom."
    $ stephanie.change_happiness(2)
    "She giggles."
    the_person "Yep!"
    "She lets out a loud sigh."
    the_person "Last summer feels like SUCH a long time ago."
    "She looks over at you and smiles."
    the_person "Being your head researcher though, I think this is the change in my life I've been waiting for."
    the_person "The things we are going to accomplish together. I can't wait to see what happens!"
    the_person "I just wish you would have stayed in touch better. You know I could have helped you, right?"
    mc.name "I know. I don't know what I was thinking. I guess I thought you would be angry at me for not sharing more details about the serums."
    $ stephanie.change_love(2, 40)
    the_person "Awww, It's okay..."
    "She sighs and shakes her head."
    the_person "I just can't stay mad at you, can I?"
    the_person "Anyway, this is my room. Shall we pick up where we left off last summer?"
    "You watch in awe as she starts to strip down."
    $ the_person.strip_to_tits()
    the_person "Let's just get all these pesky clothes out of the way..."
    $ the_person.strip_to_vagina()
    $ the_person.break_taboo("bare_tits")
    $ the_person.break_taboo("bare_pussy")
    "Once naked, she looks at you, waiting for you to make the next move."
    $ mc.change_locked_clarity(30)
    mc.name "Wow, you look amazing [the_person.title]."
    "You quickly disrobe as well. She smiles at you approvingly when your erection is revealed."
    the_person "Ah, there's that amazing cock. I seem to remember a thing or two about that..."
    $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
    "She approaches and wraps her hands around you. Your hands immediately go to her hips and you pull her close."
    "You hands go to her ass and pull her body harder against yours. She leans forward and starts to kiss the side of your neck and nibbles on your ear."
    "A soft whisper sends goosebumps down your back."
    the_person "I'm yours tonight. Do what you want with me..."
    $ mc.change_locked_clarity(50)
    "Your body fills with lust, and she gasps when you pick her up."
    mc.name "Yes ma'am."
    "You take her over to her bed and then roughly throw her down on it, then quickly jump on top of her."
    $ the_person.draw_person(position = "missionary", display_transform = character_center_focus)
    $ the_person.change_arousal(15)
    the_person "Mmmm! Ah yes that feels good..."
    "You kiss your way down her neck to her tits. Your lips latch onto one of her nipples while you grope the other one."
    "[the_person.possessive_title!c]'s hands go to the back of your head and she moans as you warm her up."
    "You keep kissing, going down along the bottom of her breast to her rib cage. Your head keeps descending."
    the_person "Ahh, you don't need to do that, I'm..."
    mc.name "Shhh, I just want to get a quick taste."
    the_person "Ah, I guess I can't blame you..."
    "You kiss your way down her stomach. As you get lower, you bring your arms from around her waist to between her legs."
    "You use your hands to spread her legs wide open as you marvel at her wonderful little pussy."
    the_person "Ahhh, no staring..."
    "She seems a little embarrassed, but you enjoy the view for a few more moments."
    $ mc.change_locked_clarity(50)
    "You lean forward, kissing up the inside of her legs, making her laugh."
    the_person "Hey! That tickles! Take it eas.... aaaahhhhhh!"
    "You kiss up between her legs and then reach her pussy, causing her to moan out loud."
    $ the_person.change_arousal(20)
    $ the_person.break_taboo("licking_pussy")
    "Her hand goes to the back of your head again as you begin to lick up and down her delicious slit."
    "You push your tongue inside her and taste her arousal for a few moments, then begin licking up and down her again."
    the_person "Ohhh fuck [the_person.mc_title]..."
    "You use your tongue to explore your former lab partner. She moans her approval constantly."
    $ play_moan_sound()
    $ the_person.change_arousal(20)
    "Your tongue flicks across her clit a few times, causing her body to tense up."
    "Suddenly you feel her hand on your head, desperately pushing you away from her cunt."
    "You look up at her."
    the_person "STOP! Please... I want your cock..."
    $ mc.change_locked_clarity(50)
    "Hearing her request makes the aforementioned organ twitch."
    the_person "AH!"
    "You plant one last kiss on her slit, eliciting a surprised gasp from [the_person.title], then you move back up her body."
    "She reaches down and grabs your cock, pointing it directly at her dripping wet hole."
    the_person "Please! I need it so bad...!"
    "Not one to disappoint a lady, you gently slide your hips forward, letting her guide your erection into her needy vagina."
    $ play_moan_sound()
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(15)
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    "Your former lab partner's body accepts your bare manhood and you slide all the way in with one smooth stroke."
    the_person "YES!!! Oh baby..."
    "Her arms wrap around your back and she leans up. You lean down and your lips meet as you begin to makeout with her."
    "She doesn't seem to mind the taste of her own pussy as her mouth opens and her tongue darts inside your mouth."
    "You make out for several seconds, then you begin to move your hips. She pulls back and gasps."
    the_person "Ohhh fuck, oh fuck me baby!"
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(15)
    "You begin to thrust into her, and she is so worked up she is going to cum already."
    the_person "Oh my god... OHHH!"
    $ the_person.have_orgasm(half_arousal = True)
    "Gasps and moans are all she manages as you fuck her through her orgasm."
    "You only slow down after the most urgent of her moans begin to subside."
    the_person "Ohhhh... oh fuck so good... oh god [the_person.mc_title] I love you...rrrrr..."
    "Suddenly her eyes go wide as she realizes what she is saying."
    the_person "...youuurrrr cock, haha. I love your cock!"
    "She grimaces for a moment. Her orgasmic, drunken brain has caused her to slip up for a moment."
    mc.name "Good. And I love your pussy."
    "You slow down and stop thrusting for a moment, just enjoying the feeling of being inside of [the_person.possessive_title]."
    the_person "Yeah... ha... they go good together."
    $ mc.change_locked_clarity(50)
    "You spend a few moments laying on top of [the_person.title]. Her body under yours feels so good."
    "You feel your cock twitch a couple times. The evening has been so hot, you need to finish soon."
    mc.name "[the_person.title], I'm not sure I can last much longer..."
    the_person "Then don't. It's okay, I'm on the pill..."
    $ the_person.update_birth_control_knowledge()
    "Her words of encouragement are all you need to start fucking her again."
    mc.name "Are you sure? We've had some drinks... I don't want you to regret this in the morning."
    the_person "Ah, don't worry, I promise I won't regret it!"
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(25)
    mc.name "Ahhh, oh fuck... okay!"
    "You speed up, your body rapidly approaching orgasm. [the_person.possessive_title] has given you clearance to cum inside her!"
    mc.name "Oh fuck... here it comes!"
    the_person "Yes! Give it to me!"
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "missionary", display_transform = character_center_focus)
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
    if the_person.has_taboo("creampie"):
        # $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
    "Her words drive you over the edge and you start to orgasm, dumping your cum inside of her."
    the_person "Oh my god... yes!"
    $ the_person.change_arousal(20)
    "You give her wave after wave of cum, pinning her to her bed and filling her pussy with your seed."
    "Suddenly she gasps and starts to tremble."
    the_person "Ohhhh! YES!!!"
    $ the_person.have_orgasm(half_arousal = False)
    "Just as your orgasm is winding down, she begins to cum too."
    "Her entire body quivers and trembles as she orgasms again. Her moans are music to your ears."
    "When she finishes, you just lay on top of her. Your cock is slowly softening, but you leave it inside of her for now."
    the_person "[the_person.mc_title]... that was amazing..."
    mc.name "Yeah... that was fucking hot..."
    "She catches her breath for a few more moments."
    the_person "I know I should probably like... scramble for a towel or something... but I just have no energy..."
    "You slowly push yourself and begin to pull out of her. She gives a little gasp when your cock slides out."
    "Your cum is dripping down her pussy between her legs, and your combined cum has made a damp spot on the sheets."
    $ the_person.draw_person(position = "missionary")
    "You stand up and start to collect your clothes."
    "As you get dressed, [the_person.title] watches you from her bed, exhausted."
    the_person "I'm beat... can you let yourself out?"
    mc.name "Yeah. Take care [the_person.title]."
    the_person "You too!"
    $ the_person.clear_situational_slut("Romanced")
    $ clear_scene()
    "You step out of [the_person.possessive_title]'s place and start to head home."
    $ the_person.change_location(downtown)
    "As you walk, you think about the crazy events of the last week of your life."
    "Meeting back up with [nora.title] and [stephanie.possessive_title], starting the business, and now this."
    "It is happening so fast, you can barely believe it."
    "Your former lab partner DEFINITELY seems to have a thing for you still. You regret falling out of contact with her over the last year."
    "You make up your mind to make up for it now."
    "However, she was definitely a little... intoxicated..."
    "You should probably check back with her next week at work and try and get a feel for things, if she regrets your little one night stand or not."
    $ add_stephanie_first_bar_date_followup_action()
    "You get home and head for your bedroom."
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_steph_intro_02
    return

label stephanie_first_bar_date_followup_label(the_person):
    $ the_person.draw_person(emotion = "happy", position = "sitting")
    "As you enter the lab, you see [the_person.possessive_title]."
    "She is humming happily to herself as she works. You need to have a chat with her about last weekend."
    "She seems to be in a good mood, so you figure now is as good of a time as any to approach her."
    "As you walk up, she hears you approach and looks up. When she sees you, her smile goes wide."
    the_person "Oh hey [the_person.mc_title]! It's good to see you!"
    "So far so good."
    mc.name "Hey [the_person.title]. How's work going?"
    the_person "Great. SO glad to be here and out of the bureaucracy of the university labs."
    mc.name "Yeah, I bet..."
    the_person "Hey, so I was texting [nora.name] a bit ago, and she is still planning to meet with us on Saturday night."
    the_person "Do you think you'll be able to go? Last weekend I had SUCH a good time."
    "She looks up at you hopefully. This is going better than you expected."
    mc.name "Oh, I'm planning on it, unless something comes up, of course."
    the_person "Good! Hopefully I'll see you there then. Maybe we could even have a few drinks after, again?"
    mc.name "Yeah, pretty sure that will be fine."
    $ the_person.change_love(2, 40)
    $ the_person.change_happiness(5)
    the_person "Alright. See ya!"
    $ clear_scene()
    "You step away from [the_person.possessive_title]'s desk."
    "It definitely seems like she is just fine with what happened last weekend at her place, and even seems eager for a repeat performance."
    return


label nora_first_bar_date_label():
    $ the_person = nora
    "You head over to the bar and order drinks for you and [the_person.title]."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    "If you are quick, you could sneak in a serum..."
    call give_serum(the_person) from _call_give_bar_date_sneaky_boi_nora_01
    if _return:
        "You drop the serum in to the drink with no one noticing, then return to [the_person.title] and hand it to her."
    else:
        "You just grab the drinks and return to [the_person.title], handing it to her."
    $ the_person.draw_person()
    nora "Thank you."
    "[nora.title] gratefully accepts your drink and takes a small sip from it."
    $ the_person.increase_drink_level(1)
    mc.name "A Manhattan is a sophisticated drink, for a sophisticated lady."
    "[nora.title] rolls her eyes at you."
    nora "Spare me the flattery. You're lucky I was considering staying anyway."
    mc.name "Oh? You wanted to hang out with me and [stephanie.fname]?"
    nora "No, but they have started running a fun little diversion here. A trivia game."
    mc.name "Oh yeah? I didn't know you liked trivia, although now that you say it, it makes sense."
    nora "Yes. On my way back from the restroom, I signed us up."
    mc.name "Us?"
    nora "Yeah. It is supposed to be for couples to play against other couples."
    nora "Obviously we aren't a couple, but I thought it would be fun to play anyway."
    nora "Winner's get a free drink, and judging from what I've heard about the state of your business, I thought you could use it."
    mc.name "Ouch. But you know what, it sounds fun. Let's go."
    "You and [nora.possessive_title] step over to the area of the bar where they are getting ready to start trivia."
    "There are a few other couples there, and [nora.title] explains to you the rules as things get ready to start."
    "Thankfully, either person can answer the questions, so you get ready to try and impress [nora.possessive_title]."
    "The game starts, and before you know it, she has racked up several correct answers."
    nora "What is quantum entanglement."
    "Host" "Yes, that is correct again."
    "You can't believe how fast she answers all the questions. You manage to snag a couple right answers also, but she easily runs the board."
    nora "What is Ohio."
    "Host" "... Yes... that's correct..."
    "By the end of the trivia game, [nora.title] has thoroughly dominated the game. You have triple the score of the next closest couple."
    "Host" "Alright! That's the game. Here are our winners, by a landslide!"
    $ the_person.change_happiness(10)
    $ the_person.change_love(3, 40)
    $ the_person.draw_person(emotion = "happy")
    "[the_person.title] cracks a wide smile for the first time all night."
    nora "Alright! We won!"
    $ the_person.draw_person(position = "kissing")
    "She suddenly turns and gives you a big hug. She whispers into your ear."
    nora "We need to pretend to be a couple, or they won't let us play next time. Slap my ass or something."
    mc.name "Uhhh, with pleasure."
    "You grab her ass and pull her closer to you. She gasps when she feels your body pressing up against her."
    nora "Ahhh, that... that should do it..."
    "You hold on to her for several more seconds. Just as she starts to push you away you let her go."
    $ the_person.change_slut(2, 40)
    $ the_person.change_obedience(2, 140)
    $ the_person.change_arousal(15)
    $ the_person.draw_person(emotion = "happy", position = the_person.idle_pose)
    "Her smile remains. She doesn't seem to be angry, in fact you think you notice a bit of color in her cheeks."
    "Host" "Alright, well to the winners, see the bartender for your prize!"
    "You walk with [nora.possessive_title] to the bar. Soon, two drinks appears before you, gratis."
    $ the_person.increase_drink_level(1)
    mc.name "Well, what do you say we find a table and just relax with our rewards?"
    nora "Yes, that sounds good."
    call bar_date_relax_label(the_person) from _nora_drinks_intro_01
    nora "Well, this has been fun, but I must be getting home."
    mc.name "Shall I walk you home?"
    nora "No, I'll make it by myself, thank you. Though I appreciate the sentiment."
    "She looks you over before standing up."
    nora "You know, this *HAS* been fun. If you want to do this again next week, I'll stick around."
    "She gives you a stern look."
    nora "BUT. I'm not your arm candy. And I'm not here to hang out with [stephanie.fname]."
    nora "I'm not jealous of the girl or anything, but if you want to have some drinks with me, it'll be just us. Okay?"
    mc.name "I can live with that."
    nora "Right..."
    $ the_person.draw_person(position = the_person.idle_pose)
    nora "Until next time then. Goodbye [the_person.mc_title]."
    $ the_person.draw_person(position = "walking_away")
    "She walks away, leaving you by yourself at the table."
    $ clear_scene()
    "While you didn't wind up at her place like you had hoped, you definitely made some progress with her tonight."
    "She's willing to do this with you again, but you'll have to choose between her and [stephanie.title] to hang out with."
    "And, you learned to play trivia. Maybe you could play with other girls on dates? It takes intelligence, but it might be good to impress them."
    $ nora.event_triggers_dict["bar_meetup_nora_stay"] = True
    $ bar_date_add_available_game("trivia")
    "You get home and head for your bedroom."
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_nora_intro_01
    return

# Very first time mandatory event #
label nora_bar_meetup_initial_meeting_label(the_person = nora):
    "It is Saturday night, and your first week as a business owner is drawing to a close."
    "You promised to meet with [nora.title] again tonight, so you head over to the bar."
    $ mc.change_location(downtown_bar)
    call nora_bar_meetup_intro_label(nora) from _initial_bar_meetup_nora_001a
    return
