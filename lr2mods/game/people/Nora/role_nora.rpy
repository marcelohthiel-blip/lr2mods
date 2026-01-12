# All of the role specific actions for Nora
# Nora acts as an alternate way of unlocking serum research progress and allows the player to unlock special serum traits.

# Nora needs the player to help her cut through bureaucratic red tape and test serum traits that she can't.
# She gives the player (temporary) access to a serum trait with a very high side effect chance, strange/extreme effects, and minimal sale value.
# The player needs to raise the mastery value of the trait to a certain level, after which they can "turn in" the request for a reward.
# Initially this reward will be access to higher serum tech tiers or unlocks of other serum traits without having to research them.
# Later it may let you unlock unique serum traits.

label nora_intro_label(the_person):
    $ the_nora = nora
    $ mc.business.event_triggers_dict["intro_nora"] = False #We've already introduced her, so we don't have to do this again.
    $ the_nora.primary_job.job_known = True
    $ old_location = mc.location
    $ scene_manager = Scene()

    mc.name "[the_person.title], have you talked to [the_nora.title] yet?"
    "She nods."
    the_person "I did, she said we would be welcome by any time."
    mc.name "Excellent, I want to pay her a visit and want you to come along."
    the_person "Sure thing. It's going to be strange being back there, but I'm looking forward to it!"
    "The two of you head to the university. Being on campus again triggers a wave of nostalgia that you hadn't expected."

    $ mc.change_location(university)
    $ scene_manager.add_actor(the_person, the_person.planned_outfit, display_transform = character_right)

    "You navigate to the old lab and knock on the door. You hear the click of high heels approaching from the other side."
    "Your old lab director opens the door and smiles at you and [the_person.title]. Inside the room is bustling with activity."
    $ scene_manager.add_actor(the_nora, display_transform = character_center_flipped, emotion = "happy")
    the_nora "[the_nora.mc_title], [the_person.title], I'm glad you both stopped by."
    mc.name "It's nice to see you [the_nora.title]."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "Hey [the_nora.fname]. Good to be back."
    "[the_nora.possessive_title!c] steps out into the hallway and closes the lab door behind her."
    the_nora "I'm sorry I can't invite you in; the lab is a high security space now."
    the_nora "The university has gotten very protective of my work since you left."
    "She sounds frustrated with the situation."
    the_nora "Anyway, I know you aren't here for an earful about academic politics. You had a problem you needed help with?"
    mc.name "We did, but it might take a while to explain. How about I buy us a round of coffees and we talk about it upstairs."
    the_nora "The two of you have piqued my interest, lead the way."

    "The three of you return to ground level and go to a coffee shop near the campus."
    $ mc.change_location(coffee_shop)
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "default")
    $ scene_manager.update_actor(the_nora, position = "sitting", emotion = "default")
    "When you get there [the_person.title] pulls out a folder containing a synopsis of your research and slides it over to [the_nora.title]."
    "[the_nora.possessive_title!c] looks through the notes, sipping thoughtfully at her coffee."
    the_nora "Hmm... Yes... Ah, I see what's going on. I ran into this same roadblock."
    the_person "Excellent, so you know where to go from here?"
    "[the_nora.title] looks up from her notes."
    the_nora "Do I know? Of course! I haven't just been twiddling my thumbs since you two left!"
    the_nora "The problem is that all of my research is supposed to be kept within the university now. No sharing with outside organisations."
    the_nora "I wish I could help, but it's my job at risk."
    mc.name "Come on [the_nora.title], we're counting on you here."
    the_person "Think of the science, we shouldn't let bureaucrats get in the way of progress! That's what you always taught me, at least."
    "She leans forward in her chair, thinking intensely. You and [the_person.title] wait while she comes to a decision."
    the_nora "Okay, I'll help. But I'll need something in return."
    "You breathe a sigh of relief."
    mc.name "Name it, I'll do what I can."
    the_nora "I have some effects that might be achievable, but I'm running into nothing but red tape getting them approved for human testing."
    the_nora "I will provide you with some of my research. I need you to develop it into a complete package, test it, and return the results to me."
    the_nora "Once I have your results back I'll give you my old notes, which should be enough to keep you moving forward."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "That's perfect, that's all I need."
    mc.name "We'll make it happen [the_nora.title]. Send the plans for the trait you need researched and we'll get started right away."
    $ scene_manager.update_actor(the_nora, position = "default")
    "[the_nora.title] stands up and pushes her chair in."
    the_nora "I hope to hear from you soon. Good luck."
    $ scene_manager.update_actor(the_person, position = "kissing")
    $ scene_manager.update_actor(the_nora, position = "kissing")
    "She hugs [the_person.title] goodbye."
    $ scene_manager.update_actor(the_person, position = "default")
    $ scene_manager.update_actor(the_nora, position = "walking_away")
    mc.name "Right, let's get back to the office."

    $ scene_manager.remove_actor(the_nora)
    $ start_nora_trait_research()

    $ mc.change_location(old_location)
    $ scene_manager.draw_scene()
    "When you get back to the office [the_person.title] has a new file detailing an untested serum trait."
    the_person "Without [the_nora.fname]'s research notes all we'll be able to do is put this trait into a serum and manufacture it."
    the_person "You'll need to test a serum containing this trait on someone to raise its mastery level."
    the_person "We should bring up its mastery level to 2%% before we go back to [the_nora.fname]."

    mc.name "Understood. I'll be back once the testing is done."
    $ scene_manager.clear_scene()

    $ the_nora = None
    $ old_location = None
    $ add_nora_university_research_actions()
    return

label nora_research_up_label(the_person):
    $ the_person.set_override_schedule(None)
    $ scene_manager = Scene()

    "You knock on the door to [the_person.title]'s lab and wait until the door is opened."
    $ scene_manager.add_actor(the_person)
    the_person "[the_person.mc_title], it's good to see you again."
    "She steps out of the office and closes the door behind her."
    mc.name "You too. I've got something for you."
    "You hold out the folder containing the details of your testing."
    the_person "Good, wait here."
    $ scene_manager.hide_actor(the_person)
    "She slips back into the room and is gone for a couple of minutes."
    $ scene_manager.show_actor(the_person)
    "When she comes back out she has two large binders tucked under her arm."
    the_person "Let's go get a coffee and chat."

    $ mc.change_location(coffee_shop)
    $ scene_manager.update_actor(the_person, position = "sitting")

    "A short walk later and you're sitting in a small coffee shop you visited last time. You slide your folder to [the_person.title] and she opens it eagerly."
    the_person "Hmmm. Interesting... Ah..."
    the_person "This is exactly the kind of information I wanted. Well done [the_person.mc_title]."
    "She slides her binders of notes over to you."
    $ the_person.change_love(3)
    the_person "I always thought you were destined for great things."
    the_person "I may have more testing for you to do soon. I'll get in touch when I do."
    "You finish your coffees and say goodbye."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "The notes [the_person.title] has given you provide all the details you need to pursue a number of new serum traits."

    python:
        scene_manager.clear_scene()
        complete_nora_initial_research()
        add_nora_research_intro_action(the_person, True)

    "You should check at your R&D department on what to research next."
    return


label nora_research_cash_intro(the_person, did_research = False):
    # Nora calls you and enables the rest of the quest line. Doesn't give you the first trait yet, for that you need to visit her.
    $ the_person.set_override_schedule(None) #Let her out into the wild
    $ play_ring_sound()

    "You get a call from [the_person.title]."
    the_person "Hello [the_person.mc_title]. This is [the_person.name], I'm calling from the university on a recorded line."
    "It is obvious from her greeting that she wants you to be careful what you say."
    mc.name "[the_person.title], good to hear from you. How can I help you?"
    the_person "I have some good news for you."
    the_person "I presented the research findings from your field tests to my section head."
    the_person "They were very impressed with my findings and have given my lab a grant to accelerate our work."
    the_person "Obviously, I won't be able to keep up with the pace they expect without some help from you."
    mc.name "So you're saying you have some work for me?"
    the_person "I do. Come by the lab when you have the time and I can give you the details and discuss payment."
    mc.name "I'll see when I have time in my schedule. Talk to you soon [the_person.title]."
    $ mc.business.event_triggers_dict["nora_trait_researched"] = None
    $ add_visit_nora_lab_action(the_person)

    $ mc.business.event_triggers_dict["nora_cash_research_trigger"] = True
    return

label nora_research_cash_first_time(the_person):
    # The event for your first visit to see her to talk about being paid for your research. Can also trigger if you have research level 2 but nora_trait_researched is present (ie. you started her quest but never finished).
    "You knock on the door to the lab. [the_person.title] answers and steps out into the hallway to talk to you."
    $ the_person.draw_person()
    the_person "[the_person.mc_title], I'm glad you were able to come by. Let's walk and talk."
    $ university.show_background()
    "You walk upstairs together to make sure none of [the_person.possessive_title]'s co-workers are around."
    if mc.business.event_triggers_dict.get("nora_trait_researched", None) is None: #You don't have her first trait hanging around, so you've finished that quest line
        mc.name "So you have a serum trait for me to test?"
        the_person "I do. I have the details prepared for you to manufacture, and a section of the grant money set aside to pay for your work."
        the_person "Once your research findings are returned I can pay you a bounty of $2000 and provide you another trait to study."
        the_person "Do you find this acceptable?"
        "You think the offer over. It's a good amount of money for the amount of work, as long as you have someone to test these serums on."
        mc.name "I can make that work."
        the_person "Good. I'll send you the manufacturing details that we have prepared right away. Come and see me when your report is complete."
        $ add_new_nora_cash_trait_for_research()

    else:
        the_person "Do you have your finished research for me?"
        mc.name "I don't. My lab went in another direction and we found the breakthrough we were looking for."
        the_person "I see. I'm proud of you [the_person.mc_title], you seem very capable of turning theoretical science into practical results."
        the_person "I suppose this means we need to come to some sort of new arrangement then. If I cannot buy your services with research material I hope cash payment will do."
        the_person "If you finish your field research on the trait I provided you I can pay a bounty of $2000. I may also be able to provide another trait for you to study."
        the_person "Do you find this acceptable?"
        "You think the offer over. It's a good amount of money for the amount of work, as long as you have someone to test these serums on."
        mc.name "I can make that work."
        the_person "Glad to hear it. Come see me again when your research is complete."

        $ mc.business.event_triggers_dict["nora_cash_research_trait"] = mc.business.event_triggers_dict.get("nora_trait_researched") #The old research trait is now the cash goal trait
        $ mc.business.event_triggers_dict["nora_trait_researched"] = None #Clear this so we can use it as a flag to not show future events related to the research up quest.


    $ add_nora_research_cash_action(the_person)
    $ clear_scene()
    return

label nora_research_cash(the_person):
    # The event where you turn in a completed research report.
    if not mc.business.is_weekend and not emily.event_triggers_dict.get("tutor_introduced", False):
        $ emily.event_triggers_dict["tutor_introduced"] = True
        call student_intro_one(the_person, emily) from _call_student_intro_one

    else:
        "You knock on the door to the lab. [the_person.title] answers and steps out into the hallway to talk to you."
        $ the_person.draw_person()
        the_person "[the_person.mc_title], I'm glad you were able to come by. Let's walk and talk."
        $ university.show_background()
        "You walk upstairs together to make sure none of [the_person.possessive_title]'s co-workers are around."

    # TODO: The first intro bit returns here
    $ nora_clear_current_cash_trait()

    mc.name "I have your research report prepared. The effects of the trait you designed were... {i}interesting{/i}."
    "You hand her a folder you've put together containing the information you collected from your test subjects. She takes it and tucks it under her arm."
    the_person "Thank you, I'll look through this later and send your payment if everything is in order."

    if list_of_nora_traits:
        #There are still items in the list, get one, give it to the player to study.
        the_person "I have another trait I would like studied, if you are still interested. I will send you the production details." #I'll mark the location of the settlement on your mp
        $ add_new_nora_cash_trait_for_research()
        mc.name "Okay, I'll see what I can do. Thank you for your business, [the_person.title]."
        "You say goodbye to [the_person.possessive_title] and split up. Your payment is sent soon after."

    else:
        #Unlock the boss trait phase
        the_person "I also have some good news. Thanks in part to your assistance I have been given a long term grant to continue my research."
        mc.name "Congratulations [the_person.title], after all your hard work you deserve it."
        the_person "Thank you. My boss was an issue but I was able to... Well, I was able to convince him, let's leave it at that."
        the_person "This money relieves the pressure on me to produce results quickly, and means I will not need you to perform any more field tests."
        the_person "But I have an idea we may both benefit from."
        mc.name "Go on, you always have interesting ideas for me."
        the_person "In my studies I have found that people with extreme personalities, mindsets, backgrounds, or beliefs can offer insights into new serum traits."
        the_person "I will provide you with a detailed questionnaire. Have an interesting person fill it out, or interview them and fill it out yourself, and bring it back to me."
        the_person "If I find any hints pointing towards a trait I will share the research with you. I expand the forefront of science, and you discover useful applications for your business."
        mc.name "That sounds like a good deal for both of us."
        the_person "My thoughts exactly, I'm glad you agree."
        "You say goodbye to [the_person.possessive_title] and split up. She sends your final payment and her research questionnaire soon after."

        $ add_study_person_for_nora_actions(the_person)
    $ mc.business.change_funds(2000)
    $ clear_scene()
    return

label nora_special_research(the_person):
    if not mc.business.is_weekend and not emily.event_triggers_dict.get("tutor_introduced", False):
        $ emily.event_triggers_dict["tutor_introduced"] = True
        call student_intro_one(the_person, emily) from _call_student_intro_two

    # Bring a report about a special person to Nora and she generates a special serum trait for them.
    $ the_subject = get_nora_research_subject() #This is guaranteed to exist thanks to the pre action checks.

    $ the_person.draw_person()
    mc.name "I have a research profile for you to take a look at, [the_person.title]. Let me know if you can find out anything interesting."
    if the_subject == the_person:
        "You give [the_person.possessive_title] the report you have prepared on herself."
    else:
        "You give [the_person.possessive_title] the report you have prepared on [the_subject.title]."
    the_person "Excellent. This shouldn't take too long to process, I just need to head to the lab and input the data."
    $ clear_scene()
    "[the_person.title] leaves for her lab. True to her word, she's back in less than half an hour with her findings in hand."
    $ the_person.draw_person()
    if the_subject.has_role(trance_role) and nora_reward_instant_trance not in list_of_traits:
        the_person "A very interesting case [the_person.mc_title]. I have some leads for you."
        the_person "The subject's level of suggestibility is remarkable. With persistence I believe you could convince them of almost anything in this state."
        the_person "It reminded me of some of our old research work. I've dug out the notes on those early designs and identified the molecule responsible for this state."
        the_person "It won't achieve results as extreme as what the subject presented with, but it may prove much faster than whatever means you used to achieve this state naturally."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_instant_trance)

    elif the_subject == mom and the_subject.sluttiness > 75 and the_subject.love > 75 and nora_reward_mother_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "Your mother's responses indicate an intense level of devotion to you, to the point that she seems to derive almost sexual pleasure from your satisfaction."
        the_person "It may be possible to reverse the relationship in others, inspiring love in place of sexual attraction."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_mother_trait)

    elif the_subject == lily and the_subject.sluttiness > 75 and the_subject.obedience > 150 and nora_reward_sister_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "Your sister's responses seemed incredibly deferential, but she seemed to derive some sort of pleasure from the act."
        the_person "It may be possible to produce that association in others, with the effect increasing alongside their natural tendencies to obey."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_sister_trait)

    elif the_subject == cousin and the_subject.sluttiness > 75 and the_subject.love < -25 and nora_reward_cousin_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "This was your cousin, correct? I'm surprised to find such vitriol in such a close family member."
        the_person "Her hate of you brings her great pleasure, to the point that I believe she has a sexual link to it."
        the_person "I don't know how useful it would be, but I think this could be replicated in others with some research work."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_cousin_trait)

    elif the_subject == aunt and the_subject.sluttiness > 75 and nora_reward_aunt_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "Your aunt is a blank slate, ready for any sort of change. That would make her an ideal candidate to be affected by any number of other effects."
        the_person "If we could emulate that state of mind in others, you could safely add more serum traits to a single design."
        $ list_of_traits.append(nora_reward_aunt_trait)

    elif the_subject == nora and the_subject.sluttiness > 75 and nora_reward_nora_trait not in list_of_traits:
        the_person "Well I suppose your out-of-the-box thinking is why I appreciate your scientific input, [the_person.mc_title]."
        the_person "I ran your report on myself, and much to my surprise I think there may be something here for us both to study."
        the_person "My own sexual drive seems to be linked quite heavily to the intelligence of the person I am talking to."
        the_person "It may be possible to develop a serum that replicates this in another person, with the effect being more pronounced the larger the intelligence difference."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_nora_trait)

    elif the_subject.is_pregnant and the_subject.pregnancy_is_visible and the_subject.sluttiness > 75 and nora_reward_hucow_trait not in list_of_traits:
        # Change for mod to exclude girls who didn't get pregnant by MC
        if the_subject.event_triggers_dict.get("preg_mc_father", True):
            the_person "First off, congratulations [the_person.mc_title]. You're the father."
            the_person "Second, I have an interesting development and possible path forward."
        else:
            the_person "I have an interesting development and possible path forward."
        the_person "My testing has revealed a number of major differences between the test subject's hormonal balance and what is expected."
        the_person "I believe this is the body's natural response to her noticeably intense desire for sexual satisfaction."
        the_person "If most women have a biological clock ticking, this one has a church bell."
        the_person "It may be possible to induce and amplify this hormonal response in others pre-impregnation."
        the_person "I would expect the results to be increased fertility, breast swelling, and very likely immediate lactation."
        the_person "Traditional birth control is also unlikely to affect this new hormonal balance, so it will be rendered ineffective."
        $ list_of_traits.append(nora_reward_hucow_trait)

    elif the_subject.love > 85 and nora_reward_high_love_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "The subject reported an intense love for you, to the exclusion of all others."
        the_person "Moral objections aside, this effect would have obvious applications if you could find a way to apply it to others."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_high_love_trait)

    elif the_subject.love < -50 and nora_reward_low_love_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "I'm surprised you were able to convince the subject to produce any answers at all for you. She reported a burning, almost single-minded hatred of you."
        the_person "I don't know how useful it will be, but with some further research work you may be able to replicate that level of absolute disgust in whomever you want."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_low_love_trait)

    elif the_subject.obedience > 180 and nora_reward_high_obedience_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "I'm not surprised you were able to extract such detailed information from the subject, her obedience to you seems to be almost complete."
        the_person "She seems content with her lack of independence, which you might be able to replicate and harness with some further research work."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_high_obedience_trait)

    elif the_subject.sluttiness > 95 and nora_reward_high_slut_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "Your subject was obviously very forthcoming with her sexual desires, but what I found interesting was how central to her personality they were."
        the_person "It may be possible to instill this same sexual confidence in others, if they have a budding tendency for it to start with."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_high_slut_trait)

    elif the_subject.int >= 7 and the_subject.charisma >= 7 and the_subject.focus >= 7 and nora_reward_genius_trait not in list_of_traits:
        the_person "This was certainly an interesting case, and I have a development for you."
        the_person "Your subject was extremely competent, scoring near perfectly across the board on all intellectual tests."
        the_person "Replicating the capabilities of this amazing mind may be possible with modern science."
        "She hands you her research on the matter, unlocking a new serum trait for you to research."
        $ list_of_traits.append(nora_reward_genius_trait)

    else:
        the_person "There doesn't seem to be anything of particular interest about your subject, unfortunately."

    $ mc.business.event_triggers_dict["nora_research_subject"] = None
    $ the_subject = None

    return

label nora_profile_person(the_person):
    if get_nora_research_subject() is not None:
        $ the_other_person = get_nora_research_subject()
        "Studying [the_person.title] will replace your information about [the_other_person.title]."
        menu:
            "Discard the report and continue":
                pass

            "Keep the report on [the_other_person.title]":
                return
        $ del the_other_person

    if the_person.love < 0:
        "[the_person.title]'s obvious dislike of you makes it difficult to fill out the survey [nora.title] gave to you, but with a little guess work and some clever questions you fill it all in."
        "All that is left is to take it back to [nora.title] and to see if she finds anything interesting."

    else:
        mc.name "Do you have a few minutes, [the_person.title]? I have a few questions I was hoping you could answer for me."
        "You fill in all the information you already know about [the_person.possessive_title], then have her answer a few questions you were unsure about."
        if the_person == nora:
            "It takes some time, but soon you have completed her research survey."
            "All that is left now is to give it to her and see if she finds anything interesting about herself."
        else:
            "It takes some time, but soon you have completed [nora.title]'s research survey."
            "All that is left now is to take it back to her and see if she finds anything interesting."

    $ mc.business.event_triggers_dict["nora_research_subject"] = the_person.identifier
    $ clear_scene()
    call advance_time() from _call_advance_time_24
    return

label nora_student_exam_rewrite_request(the_person):
    mc.name "I want to talk to you about [emily.fname]. I've been tutoring her and she has really improved."
    the_person "You're tutoring her? That would explain why she stopped showing up to my office every other day."
    mc.name "Her marks on assignments have been improving lately, and she said there's an important exam you were going to let her rewrite."
    the_person "Oh, that."
    "[the_person.possessive_title!c] sighs and shakes her head."
    the_person "I confess, I only told her that so she would stop bothering me about regrading every failing assignment she handed in."
    the_person "I thought she would realise she wasn't cut out for this and give up."
    mc.name "[the_person.title], this girl has worked hard and deserves a second shot. You need to let her rewrite this exam."
    the_person "When would I have the time for that? The lab is so busy right now, it's a circus in there."
    the_person "I don't have time to sit around while a single student rewrites an exam, and I certainly don't have time to grade it after."
    menu:
        "I'll run and grade the exam":
            mc.name "What if I run the exam? I'll sit with her while she takes it, and I'll grade it for you."
            mc.name "All you need to do is record the results after."
            the_person "I am confident in your own knowledge. And I did promise her..."
            "[the_person.possessive_title!c] thinks about this for a long moment."
            the_person "Okay, bring her to the lab and I'll give her an exam."
            $ the_person.event_triggers_dict["student_exam_ready"] = False
            $ emily.event_triggers_dict["test_rewrite_intro_enabled"] = True
            $ remove_student_rewrite_exam_action()
            # TODO: Set up the exam event (You need to wait until she's on campus??)


        "Maybe some other time":
            mc.name "Maybe you'll be able to run it some time in the future?"
            the_person "I wouldn't get her hopes up [the_person.mc_title]."
            # Nothing changes, the player still has the option of pursuing this storyline
    return

label nora_unlock_interns_program_label(the_person):
    "You go for a walk, eventually coming to the university grounds. You decide to walk about for a bit, admiring the architecture and the people."
    "After the four years you spent going here, you feel a connection to this place and to the students. It feels good to be on the grounds."
    if not mc.business.hr_director:
        $ add_nora_unlock_interns_program() # reschedule until we have new HR director
        return # abort we need the HR for unlock (storyline will not be unlocked)

    $ the_person.draw_person()
    the_person "Ah, hello [nora.mc_title], could I have a word?"
    mc.name "Hello [nora.title]. Sure, what's the matter?"
    the_person "The university board is threatening to scrap my Lecturer position."
    the_person "And I was wondering if you could help me out?"
    mc.name "Well, my cash flow is limited, but I can see what I can do."
    the_person "No no, it's nothing like that, they want me to contribute more to the university."
    mc.name "Oh... right... what did you have in mind?"
    the_person "Well, since you already offered [kaya.fname] a chance to combine her study with working experience."
    the_person "I was wondering if you would be willing to setup some kind of internship program."
    mc.name "Well, I'm sure I can help. What do you need?"
    the_person "I was thinking you could setup a scholarship for talented students, who you could fund and intern at your company."
    mc.name "That does sound like a nice idea. How much would this cost?"
    the_person "Last time I checked, other similar programs paid about $15,000 per intern. That covers the student's entire tuition, meal plan, and books."
    mc.name "I see, so we could start slow and gradually bring on more people as things move along?"
    the_person "Yes, if you want to I could work with you on identifying potential candidates. However, there are a few people who would be ineligible."
    mc.name "Who would be ineligible?"
    the_person "While not illegal, the university takes a strong stance against nepotism, so your family members would not be eligible."
    the_person "So [lily.fname], your sister, would not be eligible."
    mc.name "[lily.fname], right."
    mc.name "Are there any other limits to who can participate?"
    the_person "Not really, but you should be careful not to discriminate against protected classes with your scholarship."
    mc.name "What if I wanted to support a protected class?"
    the_person "Such as?"
    mc.name "What if I made it... a STEM internship program for girls only?"
    mc.name "That should give the board some extra promotional reasons for the university and since I'm one of your old students, I could tie the program to you as scholarship evaluator and trustee."
    the_person "Oh! [nora.mc_title], that would be a great idea. No such program currently exists that I'm aware of. I think the university would jump at the chance to offer a STEM internship for women."
    the_person "If you want to start this, I want to be your partner for it. To get some of these girls out into the world of research and getting some job experience before they graduate would be invaluable."
    the_person "I'll talk to the university CFO right away if you want to get it set up. I'm sure I can convince him to approve it."
    if the_person.sluttiness > 40:
        the_person "I can be VERY persuasive if I want to."
    "You think about it for a moment. This seems like a great opportunity to get impressionable young co-eds in your business..."
    "However, you should probably run the details by your HR director before you go full steam ahead."
    mc.name "Tell you what, I will run this by my HR supervisor and iron out the details, and then get this program going."
    the_person "Excellent. What programs are you looking to intern from?"
    mc.name "Well, for a STEM program... we currently do medical research and pharmaceutical manufacturing, so I suppose Chemistry and Biology?"
    the_person "I'll go corner the university CFO right away. So we can start working together."
    mc.name "Do it. I have the funds to start this ASAP."
    $ the_person.change_stats(happiness = 10, love = 3, obedience = 5)
    the_person "It's decided then. I'll go find him right now. You're doing a wonderful thing, supporting students, [nora.mc_title]."
    $ clear_scene()
    $ add_HR_start_internship_program_action()
    return

label nora_have_fun_with_her_action_label(the_person = None):
    call progression_scene_label(nora_place_prog_scene, [nora]) from _call_progression_scene_nora_have_fun_with_her
    return
