# any label that starts with serum_mod is added to the serum mod list
label serum_mod_fetish_serum_trait(stack):
    python:
        add_fetish_serum_traits()
        execute_hijack_call(stack)
return

label fetish_serum_quest_intro_label():
    $ the_person = mc.business.head_researcher
    $ mc.business.event_triggers_dict["fetish_serum_contact"] = the_person.identifier

    if the_person.is_at(mc.location):
        $ the_person.draw_person()
        the_person "Hey, I just got a lead on some new technology that I think would be beneficial. Can we talk in your office?"
        mc.name "Sure, let's go."
        $ mc.change_location(ceo_office)
        "A few minutes later, you and [the_person.title] enter your office and sit down."
    else:
        "As you are going about your daily business..."
        $ mc.start_text_convo(the_person)
        the_person "Hey, I just got a lead on some new technology that I think would be beneficial. Can we meet up?"
        mc.name "Sure, meet me in my office."
        $ mc.end_text_convo()
        $ mc.change_location(ceo_office)
        "A few minutes later, [the_person.title] is standing at your door."
        $ the_person.draw_person()
        the_person "Hey [the_person.mc_title]. Mind if I sit down?"
        mc.name "Go ahead."

    $ the_person.draw_person(position = "sitting")
    the_person "Well, I just got off the phone with an old friend. Nerdy guy named Alan I kinda had a thing with at the university before I met you."
    the_person "He has been posting a bunch of stuff on Facebook about his work in robotics, and something he posted caught my eye."
    mc.name "Oh?"
    the_person "Yeah, basically, they've managed to make small robot nanobots that are designed to gather information from specific places in the body."
    mc.name "How could this technology help us?"
    the_person "If we program the nanobots to evaluate the doses, we could improve the effectiveness of our serums."
    "You consider briefly the implications of how this technology could help your business. This would help in creating more stable serums."
    mc.name "Is this something you would be able to program?"
    "[the_person.possessive_title!c] shakes her head."
    the_person "No... but ummm, this friend of mine kind of owes me a favour. I was thinking about paying him a visit this weekend. He still lives locally."
    mc.name "Hmm, maybe you could make some kind of deal with him... supply us with these bots? Then maybe set up a basic program we can use for our initial batches."
    mc.name "Eventually we could design new programs, but for initial testing, we should keep it basic."
    the_person "That sounds like a good idea. I'll talk to him, maybe he would be willing to write us the first round of code."
    mc.name "Just make sure they collect the data we need without disturbing the effects of our serums."
    if the_person.sluttiness < 20:
        the_person "Though I suppose it {i}does{/i} make sense that it goes along with our other research goals."
    elif the_person.sluttiness < 60:
        the_person "That's a good idea. perhaps in the future we could align it with our other research goals."
    else:
        the_person "Oh! Yeah we could start small, but if this works we could improve them and help with other things too!"
    mc.name "Exactly what I am thinking."
    "You spend some time going over the details with [the_person.title]. Eventually you have a plan in place."
    $ the_person.draw_person()
    the_person "Alright, I'll check back with you next week!"

    $ add_fetish_serum_quest_intro_followup()
    $ clear_scene()
    return

label fetish_serum_quest_intro_followup_label():
    $ the_person = mc.business.head_researcher
    if the_person.identifier != get_fetish_serum_contact():
        "You wonder how it is going with the nanobot program, when you remember, you changed your head researcher."
        "Unfortunately, you doubt your previous head researcher will be interested in following up. You may have lost your chance to acquire the machines."
        return

    $ unlock_body_monitor_serum()
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! Meet me down in the lab!"
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "Guess what! I got the first set of those nanobots. He did me a favour and spent all weekend coding the program for our first batch!"
    "You look at her desk. There is a small container filled with what appears to be a silver liquid."
    the_person "All we have to do is add a little bit to a serum, set the program, and it should be good to go!"
    the_person "However, he did give me a warning. He said this tech is still technically top secret, so we absolutely {b}cannot{/b} advertise what's in it or how they work."
    mc.name "Can we still sell the completed serum?"
    the_person "Yes, but we aren't allowed to tell anyone that they are in it. Kinda shady, but I understand where he is coming from."
    the_person "We'll need to design new serums with the bots, but it shouldn't be particularly difficult. They are basic to add."
    mc.name "Sounds great. We should make sure we observe the effects of these bots as well, to make sure they are effective."
    the_person "Okay! This is exciting stuff!"
    "You have unlocked Body Monitoring Nanobots. These can be added to any serum design, and do not take up a trait slot. However, they do increase the production cost."
    "These bots gather information about the body and any chemical substances in the blood stream, including more information about the serum you gave to your subject."
    "New versions of the nanobots can be unlocked after observing the results of these bots. To advance, raise their mastery level to at least 3%%."
    python:
        add_body_monitoring_serum_phase_2_action()
    return

label body_monitor_serum_upgrade_label():
    $ the_person = mc.business.head_researcher
    $ mc.change_location(break_room)
    "While taking a break from your work on your way to get a fresh cup of coffee, you see [the_person.possessive_title] approaching you."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "stand4")
    the_person "Sorry to bother you [the_person.mc_title], but do you have a moment?"
    mc.name "Sure. What can I do for you?"
    the_person "I wanted to talk to you about the Body Monitoring Nanobot Program."
    mc.name "The Program? Is there a problem with it?"
    the_person "No, not really a problem. Just something I noticed while going over the last batch of data we received."
    mc.name "Okay. Then let's go to my office."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You grab a cup of coffee for you and [the_person.possessive_title]."
    $ mc.change_location(ceo_office)
    $ scene_manager.update_actor(the_person, position = "sitting")
    "After sitting down behind your desk, you look at [the_person.possessive_title]."
    mc.name "Alright. What is the matter?"
    the_person "Like I mentioned before, there is no real problem with the program. The data the nanobots transmit is very valuable for our research. But something caught my attention. The amount of data we receive during daytimes is very high, while during the night, we hardly get any data."
    the_person "This isn't a big surprise, since most test subjects are asleep during the night. But while the subjects are sleeping, the nanobots are idle as well, which means there is a lot of wasted potential."
    "You nod in agreement."
    mc.name "I see. And I assume you would like to make use of that missed potential?"
    the_person "Exactly."
    mc.name "So, what do you have in mind?"
    the_person "I was thinking about using the nanobots to do something that would be beneficial for the subjects on the one side, but would also benefit your non–work–related activities."
    "[the_person.possessive_title!c] winks at you with a smirk on her face."
    "You nod, taking the hint."
    the_person "We could use the idle phase of the nanobots to stimulate the cell rejuvenation process. That would improve the general health of the subject and make them more energetic over the course of time. And a healthier body could also potentially increase the data we can collect."
    mc.name "That sounds interesting. How long would it take to reprogram the bots?"
    the_person"If I focus on rewriting the base program. Until next week would be my estimation."
    mc.name "Good. [the_person.title], I want this to be finished by Monday morning, if possible."
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person "Understood, [the_person.mc_title]. I will get to work right away."
    $ scene_manager.update_actor(the_person, position ="walking_away")
    "You watch your employee leave your office with a smile on your face."
    $ scene_manager.clear_scene()
    $ add_body_monitor_upgrade_completed_action()
    return

label body_monitor_serum_upgrade_completed_label():
    $ the_person = mc.business.head_researcher
    $ mc.start_text_convo(the_person)
    the_person "Just wanted to let you know that the improved nanobot program is uploaded to the database and ready to use."
    mc.name "That was quicker than I expected. Did you have any issues?"
    the_person "No, [the_person.mc_title]. Everything went smoothly. First tests showed a slight improvement of vital parameters. But it's too early to notice any permanent improvements."
    $ the_person.change_max_energy(1)
    mc.name "Good work anyway. Have a good rest."
    the_person "Good night, [the_person.mc_title]."
    $ mc.end_text_convo()
    "The Body Monitoring Nanobot Trait got enhanced with an additional effect."
    $ enhance_body_monitor_serum()
    $ add_commission_next_nanobot_serum()
    return

label commission_next_nanobot_serum_label():
    $ the_person = mc.business.head_researcher
    $ the_person.draw_person()
    the_person "Hey, [the_person.mc_title]. I think it's time we commission our next nanobot program."
    menu:
        "Agree":
            mc.name "Sounds good. Let's do it."
            call fetish_serum_choose_next_step_label(the_person) from _call_fetish_serum_choose_next_step_commission_next
        "Maybe later":
            mc.name "I'm not sure I want to do that yet."

    the_person "Okay, that it, talk to you later."
    $ clear_scene()
    return

label fetish_serum_discuss_label(the_person):
    if mc.business.it_director != None:
        the_person "Unfortunately, my contact has completely ghosted me, and to be honest, I feel completely out of my league with this stuff."
        the_person "Didn't you hire [mc.business.it_director.name]? That IT girl? Maybe you should talk to her about the nanobots."
        mc.name "That's a good idea. I think I'll do that."
        "From now on, all nanobot progression will be made through your IT director!"
        $ add_IT_director_nanobot_intro_action()
        return
    if get_body_monitor_serum().mastery_level < 5.0:
        the_person "Unfortunately, I feel like we still don't know enough about the nanobots to consider messing with their programming."
        mc.name "I understand. I'll make it a priority to observe their results more closely."
        "To unlock new nanobots, you need to raise the mastery level of Body Monitoring Nanobots to at least 5%%."
    elif fetish_serum_coding_in_progress():
        the_person "Do you want to work on it some right now? I have the time."
    elif the_person.identifier != get_fetish_serum_contact():
        if fetish_serum_has_previously_coded():
            the_person "Do you want to make another program?"
        else:
            the_person "I'm sorry... I don't have the contact information for the person who made the original program."
            mc.name "Maybe we could create our own code?"
            the_person "That... might be possible. We don't have any programmers on staff that I am aware of though."
        call fetish_serum_self_code_menu(the_person) from _fetish_discussion_coding_menu_01
    elif fetish_serum_research_in_progress():
        the_person "I already reached out to my contact. He is going to make a new program based on your specifications this weekend."
        mc.name "Excellent."
    else:
        call fetish_serum_choose_next_step_label(the_person) from _call_fetish_serum_choose_next_step_serum_discuss
    return

label fetish_serum_choose_next_step_label(the_person):
    if fetish_serum_has_previously_coded():
        the_person "Do you want me to reach out to my contact to commission it? Or do you want to try and make another one?"
        menu:
            "Create a new program yourself":
                call fetish_serum_self_code_menu(the_person) from _fetish_discussion_coding_menu_02
            "Reach out to Contact" if the_person.identifier == get_fetish_serum_contact():
                call fetish_serum_contact_dialogue(the_person) from _fetish_discussion_commission_01
            "Review current progress":
                call fetish_serum_discuss_progress_label(the_person) from _fetish_discuss_progress_01
            "Nothing for now":
                pass
    else:
        the_person "Do you want me to reach out to my contact to commission it?"
        menu:
            "Reach out to Contact" if the_person.identifier == get_fetish_serum_contact() and get_body_monitor_serum().mastery_level >= 3.0:
                call fetish_serum_contact_dialogue(the_person) from _fetish_discussion_commission_02
            "Review current progress":
                call fetish_serum_discuss_progress_label(the_person) from _fetish_discuss_progress_02
            "Nothing for now":
                pass
    return

label fetish_serum_contact_dialogue(the_person):
    if fetish_serum_unlock_count() == 0:
        mc.name "I've been thinking about these nanobots."
        the_person "Yes?"
        mc.name "What if they did something more than just monitor the effects of a serum."
        the_person "Oh, what did you have in mind?"
        mc.name "If we program the nanobots to deliver targeted doses of endorphins and combined them with our suggestibility serums, it could change someone's opinions, depending on how we program the bots."
        "She briefly considers the implications of how this technology could help your business. And gives you a smile."
        mc.name "Is this something you would be able to program?"
        the_person "Not yet, but I will ask my contact if he's willing to make the necessary changes to the nanobots."
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_00
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 1:
        the_person "The nanobots have been working flawlessly, as far as our initial research can tell."
        mc.name "That is excellent news."
        the_person "I actually reached out to my previous contact, about the possibility of writing a new program for us."
        the_person "He has agreed to do it for us, but he is a little strapped for cash right now and has asked for a small payment."
        mc.name "How much?"
        the_person "He is asking for $1000. He could have it done by the start of business on Monday."
        mc.name "Hmm..."
        if not mc.business.has_funds(1000):
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_01
        if _return:
            $ mc.business.change_funds(-1000, stat = "Investments")
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 2:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        the_person "Hmm. Okay. Unfortunately, my contact told me that their current employer has been getting suspicious."
        the_person "Apparently, some nanobots were discovered where they shouldn't have been, and they are cracking down on access to the source code."
        the_person "He told me he could write us a new program, but he needs to secure some new equipment to do it safely."
        mc.name "How much for the new equipment?"
        the_person "He said $5000 should cover it, including his usual $1000 fee."
        mc.name "Hmm..."
        if not mc.business.has_funds(6000):
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_02
        if _return:
            $ mc.business.change_funds(-6000, stat = "Investments")
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 3:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        "[the_person.possessive_title!c] grimaces."
        the_person "I figured you might. However, my contact is starting to get spooked."
        the_person "His employer has instituted new measures for source code control. He's scared of getting caught and has significantly increased his commission price."
        mc.name "How much is he asking for?"
        the_person "He won't do it for less than $10000."
        mc.name "Hmm..."
        if not mc.business.has_funds(10000):
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_03
        if _return:
            $ mc.business.change_funds(-10000, stat = "Investments")
        the_person "Anything else I can do for you today?"
    elif fetish_serum_unlock_count() == 4:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        "[the_person.possessive_title!c] grimaces."
        the_person "I figured you might. However, my contact has some troubling news."
        the_person "His employer has instituted a whitelist for people to get access to the new source code, and my contact isn't on the list."
        the_person "He says he could probably get access, but he needs a significant bribe for the security head."
        mc.name "How much is he asking for?"
        the_person "He won't do it for less than $25000."
        mc.name "Hmm..."
        if not mc.business.has_funds(25000):
            "Unfortunately, you don't have the funds to commission this program right now."
            return
        "Do you want to commission a new nanobot program?"
        call fetish_serum_unlock_choice_menu(the_person) from _fetish_serum_menu_call_04
        if _return:
            $ mc.business.change_funds(-25000, stat = "Investments")
        the_person "Anything else I can do for you today?"
    else:
        mc.name "I want to discuss commissioning a new program for the nanobots."
        "[the_person.possessive_title!c] grimaces."
        the_person "I'm sorry [the_person.mc_title]. My contact has made it clear that at this point they can't work on the program anymore, for any amount of money."
        mc.name "I see."
    return

label fetish_serum_unlock_choice_menu(the_person):
    menu:
        "Social Proclivity Program" if not fetish_basic_serum_is_unlocked():
            mc.name "I'd like to create a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to perform basic sexual acts."
            "In addition it would increase their Foreplay skill and will affect their underwear choices."
            the_person "Alright, I'll make up a specification sheet and pass it along to him. But you owe me for this."
            mc.name "Anything you want [the_person.title]."
            $ add_fetish_serum_sexual_proclivity(day)
        "Exhibitionist Program" if fetish_serum_unlock_count() > 0 and not fetish_exhibition_serum_is_unlocked():
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to have sexual activity in front of others."
            "In addition, it would make them more willing to show their body, even out in public."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ add_fetish_serum_exhibition(day)
        "Anal Program" if fetish_serum_unlock_count() > 1 and not fetish_anal_serum_is_unlocked():
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to have anal sexual activity and be submissive to their partner."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ add_fetish_serum_anal(day)
        "Semen Program" if fetish_serum_unlock_count() > 1 and not fetish_cum_serum_is_unlocked():
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person enjoy semen exposure."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ add_fetish_serum_cum(day)
        "Reproduction Program" if fetish_serum_unlock_count() > 1 and not fetish_breeding_serum_is_unlocked():
            mc.name "I'd like to commission a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to engage in reproduction and acts associated with it."
            the_person "Alright, I'll make up a specification sheet and pass it along to him, along with the payment."
            $ add_fetish_serum_breeding(day)
        "Not right now":
            mc.name "Not right now, but I'll keep this option in mind."
            return False
        "Attempt to code your own" if fetish_serum_unlock_count() >= 1 and not fetish_serum_has_previously_coded():
            mc.name "What if, instead of paying this guy, we make our own?"
            the_person "That... might be possible. We don't have any programmers on staff that I am aware of though."
            call fetish_serum_self_code_menu(the_person) from _fetish_discussion_coding_menu_03
            return False
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = True
    return True

label fetish_serum_self_code_menu(the_person):
    if fetish_serum_has_previously_coded():
        the_person "You've done that before, right? What kind of program are you thinking? Maybe I could help you organize it."
        mc.name "I anticipate I'll need your help with the code again, like last time."
    else:
        mc.name "Let's take a look at what we have. Do you have a copy of the code?"
        the_person "I do, let me pull it up."
        $ the_person.draw_person(position = "sitting")
        "[the_person.possessive_title!c] sits down at her computer terminal. In a minute or so, she pulls up the program."
        "You start to look at it together."
        if (mc.int + mc.focus + mc.research_skill) < 15:
            "Attribute check failed! Requires higher Intelligence, Focus, and Research Skill."
            "You look through it for several minutes, but unfortunately you can't make sense of the code."
            mc.name "This is too complicated, I think."
            the_person "Sorry, I'm not sure what to suggest."
            mc.name "Maybe we will have an opportunity to create new programs in the future."
            #TODO create a HINT here that tells players to get at least 15 total stats to proceed
            return False
        else:
            "You look through the code for several minutes, and you start to catch on to how it works."
            mc.name "There's that reference again. That must be how the program determines when to trigger."
            the_person "Ah! And the reference here must be to skin nerves and endorphin receptors."
            "The code itself is complicated, but you think it might be possible to modify it into a new program yourself, with the help of [the_person.possessive_title]."
            mc.name "I think we might actually be able to pull this off."
            $ add_fetish_serum_coding_activity()
    the_person "Okay, what kind of program do you think we should make?"
    menu:
        "Social Proclivity Program" if not fetish_basic_serum_is_unlocked():
            mc.name "I'd like to create a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to perform basic sexual acts."
            "In addition it would increase their Foreplay skill and will affect their underwear choices."
            the_person "Alright, let's see what we can do."
            "You spend some time setting up a new working directory while [the_person.title] starts making a list of possible dopamine triggers."
            "Everything is now set up. You can now spend time working on the new program in the lab. Your head researcher must be present to help."
            $ set_fetish_serum_coding_target(get_fetish_basic_serum())

        "Exhibitionist Program" if fetish_serum_unlock_count() > 0 and not fetish_exhibition_serum_is_unlocked():
            mc.name "I'd like to create a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to have sexual activity in front of others."
            "In addition, it would make them more willing to show their body, even out in public."
            the_person "Alright, let's see what we can do."
            "You spend some time setting up a new working directory while [the_person.title] starts making a list of possible dopamine triggers."
            "Everything is now set up. You can now spend time working on the new program in the lab. Your head researcher must be present to help."
            $ set_fetish_serum_coding_target(get_fetish_exhibition_serum())
            # $ add_fetish_serum_exhibition_warning() #TODO uncomment this one exhibitionist fetish is created

        "Anal Program" if fetish_serum_unlock_count() > 1 and not fetish_anal_serum_is_unlocked():
            mc.name "I'd like to create a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to have anal sexual activity and be submissive to their partner."
            the_person "Alright, let's see what we can do."
            "You spend some time setting up a new working directory while [the_person.title] starts making a list of possible dopamine triggers."
            "Everything is now set up. You can now spend time working on the new program in the lab. Your head researcher must be present to help."
            $ set_fetish_serum_coding_target(get_fetish_anal_serum())
            $ add_fetish_serum_anal_warning()
        "Semen Program" if fetish_serum_unlock_count() > 1 and not fetish_cum_serum_is_unlocked():
            mc.name "I'd like to create a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person enjoy semen exposure."
            the_person "Alright, let's see what we can do."
            "You spend some time setting up a new working directory while [the_person.title] starts making a list of possible dopamine triggers."
            "Everything is now set up. You can now spend time working on the new program in the lab. Your head researcher must be present to help."
            $ set_fetish_serum_coding_target(get_fetish_cum_serum())
            $ add_fetish_serum_cum_warning()
        "Reproduction Program" if fetish_serum_unlock_count() > 1 and not fetish_breeding_serum_is_unlocked():
            mc.name "I'd like to create a new program, based on these specifications."
            "You give [the_person.title] specifications that would make a person more willing to engage in reproduction and acts associated with it."
            the_person "Alright, let's see what we can do."
            "You spend some time setting up a new working directory while [the_person.title] starts making a list of possible dopamine triggers."
            "Everything is now set up. You can now spend time working on the new program in the lab. Your head researcher must be present to help."
            $ set_fetish_serum_coding_target(get_fetish_breeding_serum())
            $ add_fetish_serum_breeding_warning()
        "Not right now":
            mc.name "Not right now, but I'll keep this option in mind."
            return False
    return True

label fetish_sexual_proclivity_label():
    $ the_person = mc.business.head_researcher
    if ellie.is_employee:
        call fetish_serum_contact_ghost(the_person) from _fetish_serum_quest_reroute_00
        return
    $ fetish_unlock_basic_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! I have details on the new sexual program!"
        mc.name "I'll be in the lab shortly!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will be more experienced in basic sexual activities and change their opinion on sexier underwear."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Sexual Proclivity Nanobots."
    "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
    "You can learn more about it when mastery level is at 3%%."
    return

label fetish_serum_exhibition_label():
    $ the_person = mc.business.head_researcher
    if ellie.is_employee:
        call fetish_serum_contact_ghost(the_person) from _fetish_serum_quest_reroute_01
        return
    $ fetish_unlock_exhibition_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! I have details on the new social program!"
        mc.name "I'll be in the lab shortly!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will be more willing to show their bodies in public, or commit sexual acts in front of others."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Social Sexual Proclivity Nanobots."
    "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
    "You can learn more about it when mastery level is at 3%%."
    return

label fetish_serum_anal_label():
    $ the_person = mc.business.head_researcher
    if ellie.is_employee:
        call fetish_serum_contact_ghost(the_person) from _fetish_serum_quest_reroute_02
        return
    $ fetish_unlock_anal_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! I have details on the new anal program!"
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will be more willing to commit acts of sodomy in submission to their partner."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Anal Sexual Proclivity Nanobots."
    "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
    "You can learn more about it at mastery level 3%%."

    return

label fetish_serum_cum_label():
    $ the_person = mc.business.head_researcher
    if ellie.is_employee:
        call fetish_serum_contact_ghost(the_person) from _fetish_serum_quest_reroute_03
        return
    $ fetish_unlock_cum_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! I have details on the new semen program!"
        mc.name "Be there in a few!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will have positive reactions to exposure to semen."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Semen Proclivity Nanobots."
    "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
    "You can learn more about it when mastery level is at 3%%."

    return

label fetish_serum_breeding_label():
    $ the_person = mc.business.head_researcher
    if ellie.is_employee:
        call fetish_serum_contact_ghost(the_person) from _fetish_serum_quest_reroute_04
        return
    $ fetish_unlock_breeding_serum()
    $ mc.business.event_triggers_dict["fetish_serum_research_active"] = False
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! I have details on the new reproduction program!"
        mc.name "Be there soon!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "My contact emailed me the new program late last night. We should be able to program a new set of nanobots with it immediately."
    the_person "The new program should make it so that people will have positive reactions to reproducing and other associated bodily functions, such as lactation."
    mc.name "Excellent."
    the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
    "You have unlocked Reproduction Proclivity Nanobots."
    "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
    "You can learn more about it when mastery level is at 3%%."

    return

label fetish_serum_anal_warning_label():
    $ the_person = mc.business.head_researcher
    $ mc.business.event_triggers_dict["anal_serum_warn"] = True
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. When she sees you, she walks right up."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab ASAP."
        mc.name "Leaving now!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "So, I've been running some experiments with those Anal Proclivity Nanobots. The results have been... interesting."
    mc.name "Oh?"
    the_person "I ran some modified version of them on some rats. I obviously expected for there to be some interesting results, but this was beyond my expectations."
    the_person "A small subset of the group of rats actually stopped eating, and instead would sit on their food, attempting to absorb it... rectally."
    the_person "I also had trouble keeping them hydrated. I had to develop a hydrating enema... and once they experienced that, I was unable to get them to drink water normally."
    mc.name "Those are interesting results."
    the_person "So far, we haven't had any similar situations in our human trials, but be careful, okay?"
    the_person "It wouldn't surprise me if repeated doses could lead someone to develop an anal fixation or fetish."
    mc.name "I understand. Thank you for the update."
    "Hmm, repeat doses could lead to a fetish? This warrants further investigation."
    return

label fetish_serum_cum_warning_label():
    $ the_person = mc.business.head_researcher
    $ mc.business.event_triggers_dict["cum_serum_warn"] = True
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. When she sees you, she walks right up."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab ASAP."
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "So, I've been running some experiments with those Semen Proclivity Nanobots. The results have been... interesting."
    mc.name "Oh?"
    the_person "I ran some modified version of them on some rats. I obviously expected for there to be some interesting results, but this was beyond my expectations."
    the_person "In my experimental group, I offered two different nutrition sources, a normal one and another modified to copy the taste, consistency, and chemical properties of semen."
    the_person "Obviously, the control group preferred the former, while the second group preferred the latter. However, we had one interesting development."
    the_person "I had one rat from the experimental group who actually managed to escape the cage. She found her way to the place I was storing the semen equivalent..."
    the_person "I found her the next day in the vat, drowned."
    mc.name "So she fell in it?"
    the_person "Well, no. Upon further testing, rats in the control group would swim out without being harmed. The experimental group would actually let themselves sink into the vat..."
    mc.name "That is very interesting."
    the_person "So far, we haven't had any similar situations in our human trials, but be careful, okay?"
    the_person "It wouldn't surprise me if repeated doses could lead someone to develop a semen fixation or fetish."
    mc.name "I understand. Thank you for the update."
    "Hmm, repeat doses could lead to a fetish? This warrants further investigation."
    return

label fetish_serum_breeding_warning_label():
    $ the_person = mc.business.head_researcher
    $ mc.business.event_triggers_dict["breeding_serum_warn"] = True
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. When she sees you, she walks right up."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab ASAP."
        mc.name "Be there soon!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "So, I've been running some experiments with those Reproduction Proclivity Nanobots. The results have been... interesting."
    mc.name "Oh?"
    the_person "I ran some modified version of them on some rats. I obviously expected for there to be some interesting results, but this was beyond my expectations."
    the_person "Obviously, we expected the rats in the experimental group to produce more offspring, but the numbers were actually staggering."
    the_person "Normal rats produce about 80-120 offspring a year. The ones in our experimental group? On pace to produce over 500."
    the_person "Gestation period for rats is fairly short in comparison to humans, but if we saw a similar effect, it would be like if a woman produced 20-25 children..."
    mc.name "That is very interesting."
    the_person "It wouldn't surprise me if repeated doses could lead someone to develop a breeding fixation or fetish."
    mc.name "I understand. Thank you for the update."
    "Hmm, repeat doses could lead to a fetish? This warrants further investigation."
    return

label fetish_serum_exhibition_warning_label():
    $ the_person = mc.business.head_researcher
    $ mc.business.event_triggers_dict["exhibition_serum_warn"] = True
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. When she sees you, she walks right up."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab ASAP."
        mc.name "Coming to the lab now!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "So, I've been running some experiments with those Public Sexual Proclivity Nanobots. The results have been... interesting."
    mc.name "Oh?"
    the_person "I ran some modified version of them on some rats. I obviously expected for there to be some interesting results, but this was beyond my expectations."
    the_person "Normal rats usually are night active and retreat during the daytime into a protected shelter."
    the_person "But they no longer seemed to care, foraging and running around all day long and copulating wherever they find a mate."
    mc.name "That is very interesting."
    the_person "It wouldn't surprise me if repeated doses could lead someone to develop an exhibitionist fixation or fetish."
    mc.name "I understand. Thank you for the update."
    "Hmm, repeat doses could lead to a fetish? This warrants further investigation."
    return

label fetish_serum_coding_activity_label():
    $ the_person = mc.business.head_researcher
    if fetish_serum_get_coding_progress() + fetish_serum_get_estimated_coding_progress() >= fetish_serum_coding_work_required():
        "You sit down at a computer terminal in the lab. You set your phone to do not disturb."
        "You are confident that you can finish this program in the next few hours, so you decide not to let any distractions through."
        $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress())
    else:
        "You sit down at a computer terminal in the lab to work on the nanobot program. Things seem to be progressing normally."
        $ ran_num = renpy.random.randint(0,6)
        if ran_num == 1:
            $ the_person.arousal = 40
            $ the_person.draw_person()
            "[the_person.possessive_title!c] walks up behind you, looking over your shoulder at your work."
            the_person "Hey, I was just looking at that program earlier..."
            "You feel her hands on your shoulders. She starts to rub your back. It feels nice and is very relaxing."
            if the_person.effective_sluttiness() > standing_doggy.slut_requirement + 5 and mc.energy > 50 and the_person.energy > 50:
                "Her hands slowly move down your chest, her fingertips feel soft as she moves them in little circles down your body."
                "When she reaches your crotch, she leans a little farther forward and kisses your neck."
                $ mc.change_arousal(10)
                the_person "Working on this program, thinking about what it does gets me so worked up sometimes..."
                if the_person.has_exhibition_fetish:
                    the_person "Can we take a break? I'm so turned on. You can bend me over the desk, right here."
                else:
                    the_person "Can we take a break? I'm so turned on."
                "She starts softly kissing your neck as she waits for your reply. Her hand is stroking your rapidly hardening cock."
                menu:
                    "Fuck [the_person.title]":
                        mc.name "I could use a break."
                        if the_person.has_exhibition_fetish or mc.location.person_count <= 1:  #She likes it public or there's no one else here.
                            "You stand up and turn to her."
                            mc.name "Bend over the desk. I'm taking you right here."
                            if mc.location.person_count > 1:
                                the_person "Oh god, right here in front of everyone? This is so hot..."
                            else:
                                the_person "Oh god, right here in the lab? This is so hot..."
                            $ the_person.change_arousal(5)
                            $ the_person.draw_person(position = "standing_doggy")
                            if the_person.vagina_available:
                                "You take your cock out and get behind her."
                            else:
                                "[the_person.possessive_title!c] bends over. You start to strip off her bottoms."
                                $ the_person.strip_outfit(exclude_upper = True, position = "standing_doggy")
                                "When you finish, you take your cock out and get behind her."
                            if mc.location.person_count <= 1:
                                "Some of the other employees in the room have noticed your actions and are watching to see what is about to happen."
                                the_person "Okay [the_person.mc_title]. Fuck me good! Don't hold back!"
                            "You run your cock along her slit a couple of times, then line yourself up and push forward."
                            $ the_person.break_taboo("condomless_sex")
                            $ the_person.break_taboo("vaginal_sex")
                            "[the_person.title]'s wet cunt feels so good wrapped around your penis. You start to fuck her."
                            call fuck_person(the_person,private = False, start_position = standing_doggy, skip_intro = True, skip_condom = True) from _call_fuck_person_serum_coding_event_01
                            $ the_report = _return
                            if the_report.get("girl orgasms", 0) > 0:
                                the_person "Ah... I think I'll actually be able to focus after that. Thanks, [the_person.mc_title]."
                            $ the_person.review_outfit()
                            $ the_person.draw_person(position = "sitting")
                            "Once [the_person.title] gets herself tidied up she sits down at her desk and goes back to work, as if nothing out of the ordinary happened."
                        else:
                            mc.name "Let's find somewhere private."
                            "You grab [the_person.possessive_title] and soon you find an empty storeroom."
                            call fuck_person(the_person,private = True) from _call_fuck_person_serum_coding_event_02
                            $ the_report = _return
                            if the_report.get("girl orgasms", 0) > 0:
                                the_person "Ah... I think I'll actually be able to focus after that. Thanks, [the_person.mc_title]."
                            "You get your clothes back on and head back to the lab, sitting down at the terminal. After a few minutes, [the_person.possessive_title] comes back in."
                            $ the_person.review_outfit()
                            $ the_person.draw_person(position = "sitting")
                            "Once [the_person.title] has gotten herself tidied up she sits down at her desk and goes back to work, as if nothing out of the ordinary happened."
                        "You start back to work on coding, but the distraction of fucking [the_person.title] makes it difficult to focus and make much progress."
                        $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress() / 4)

                    "Focus on the code" if mc.focus >= 6:
                        mc.name "I think I would like to work on this right now. Maybe another time."
                        $ the_person.change_stats(happiness = -3, obedience = 3)
                        the_person "Ah, okay."
                        "You spend a few hours working on the code. You feel like you are making good progress."
                        "You write some unit tests. There are a couple bugs, but you are able to work through them."
                        "You save your work. Your progress is coming along nicely."
                        $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress())
                    "Focus on the code\n{menu_red}Requires Focus: 6+{/menu_red} (disabled)" if mc.focus <6:
                        pass
            else:
                "Even though she means well and you do feel more relaxed, you can't seem to focus on the code."
                "You manage to accomplish some progress, but it is not much."
                $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress() / 4)
        elif ran_num == 2:
            "However, you hit a snag. This particular program requires specific nerve group activation and you are having trouble identifying them."
            "It takes a few hours of work, but you finally overcome this limitation."
            "You manage to accomplish some work on the program, but not as much as you would normally like to."
            $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress() / 2)
        elif ran_num == 3:
            "As you are looking through the variable names, however, you notice a pattern."
            "If you group together this particular group of nerve related variables, you could save a lot of time with this code."
            "You work a few hours on the grouping. Your progress has come along faster than you were expecting!"
            $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress() + mc.int + mc.focus)
        else:
            "You spend a few hours working on the code. You feel like you are making good progress."
            "You write some unit tests. There are a couple bugs, but you are able to work through them."
            "You save your work. Your progress is coming along nicely."
            $ fetish_serum_update_coding_progress(fetish_serum_get_estimated_coding_progress())

    if fetish_serum_get_coding_progress() >= fetish_serum_coding_work_required(): #Serum Finished
        "You run the final set of unit tests. Everything in the program checks out. It's finished!"
        "You call over to [the_person.possessive_title]."
        mc.name "Hey [the_person.title], come here."
        $ the_person.draw_person()
        "[the_person.title] quickly walks over."
        mc.name "The program is done. Let's load this on to a batch of those nanobots."
        the_person "That's great! I'll get it up and running."
        the_person "We'll have to make new formulas for it though, and due to production limitations, we can't combine more than one set of bots in a single serum dose."
        # fully unlock the newly researched serum
        $ unlock_fetish_serum(fetish_serum_get_coding_target())
        $ temp_string = fetish_serum_get_coding_target().name
        "You have now unlocked [temp_string]."
        "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
        "You can learn more about it when mastery level is at 3%%."
        $ mc.business.event_triggers_dict["fetish_serum_coding_active"] = False
        $ mc.business.event_triggers_dict["fetish_serum_code_progress"] = 0
        $ del temp_string
    else:
        $ ran_num = builtins.int(fetish_serum_coding_percent_done())
        "You quickly review your work. Progress is coming along, you estimate it is about [ran_num] percent complete."
    call advance_time() from _call_serum_progress_advance_time_01
    return

label fetish_serum_discuss_progress_label(the_person):
    if get_body_monitor_serum().mastery_level < 5.0:
        the_person "We need to work on researching the basic nanobot effects. Design some serums, use them, and observe the effects!"
        "To continue progressing with nanobots, you need to raise the mastery level of Body Monitoring Nanobots to at least 5%%."
        return
    elif fetish_serum_unlock_count() == 0:
        the_person "I think we should commission another nanobot program with our contact."
        return
    elif fetish_serum_unlock_count() == 1:
        the_person "We've learned a lot about how the nanobots work. I think we should try making a new program for them!"
        return
    elif fetish_serum_unlock_count() < 5:
        the_person "There are still some possibilities for new nanobot programs. You should consider trying to make new programs."
    else:
        the_person "I think we have exhausted all the possibilities for new nanobot programs, for now at least."
        return

    the_person "Here is the current status of our specialised nanobot programs."
    if fetish_exhibition_serum_is_unlocked():
        # if not is_exhibition_fetish_unlocked(): #TODO once we make an exhibitionist fetish, uncomment this
        #     the_person "I think there are more possibilities with the Social Sexual Proclivity Nanobots. You should observe the effects of them on test subjects more!"
        # else:
        the_person "I think we are at the limit of how far we can take the program on Social Sexual Proclivity Nanobots."
    if fetish_anal_serum_is_unlocked():
        if not is_anal_fetish_unlocked():
            the_person "I think there are more possibilities with the Anal Proclivity Nanobots. You should observe the effects of them on test subjects more!"
            "To unlock their potential, raise the mastery of Anal Proclivity Nanobots to at least 3%%."
        else:
            the_person "I think we are at the limit of how far we can take the program on Anal Proclivity Nanobots."
    if fetish_cum_serum_is_unlocked():
        if not is_cum_fetish_unlocked():
            the_person "I think there are more possibilities with the Semen Proclivity Nanobots. You should observe the effects of them on test subjects more!"
            "To unlock their potential, raise the mastery of Semen Proclivity Nanobots to at least 3%%."
        else:
            the_person "I think we are at the limit of how far we can take the program on Semen Proclivity Nanobots."
    if fetish_breeding_serum_is_unlocked():
        if not is_breeding_fetish_unlocked():
            the_person "I think there are more possibilities with the Reproduction Proclivity Nanobots. You should observe the effects of them on test subjects more!"
            "To unlock their potential, raise the mastery of Reproduction Proclivity Nanobots to at least 3%%."
        else:
            the_person "I think we are at the limit of how far we can take the program on Reproduction Proclivity Nanobots."
    return

label fetish_serum_contact_ghost(the_person):
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She seems upset."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey, I need to see you in the lab."
        mc.name "Be there in a few!"
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person()
    the_person "You're not going to believe it."
    mc.name "What?"
    the_person "Remember my contact? The one that we got the nanobots from?"
    mc.name "Yeah..."
    the_person "He ghosted. And not just me, it's like he doesn't exist anymore!"
    mc.name "What?"
    the_person "That's right. I can't find information about him anywhere."
    mc.name "And the money for the program?"
    the_person "Gone with him, I'm afraid."
    "Damn. You knew that was a risk taking back channels to contact this guy though, so you suppose you shouldn't be too surprised."
    "Still... you do have a new hire that is familiar with the technology..."
    the_person "I'm sorry [the_person.mc_title]... I..."
    mc.name "Don't worry. We'll be fine without him."
    the_person "I... okay... I'll get back to work."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns to get back to work. You should talk to [ellie.possessive_title] about the nanobots..."
    $ add_IT_director_nanobot_intro_action()
    return
