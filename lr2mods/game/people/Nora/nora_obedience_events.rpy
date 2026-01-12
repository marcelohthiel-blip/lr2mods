# Nora's obedience events involve meeting with, and eventually controlling the University Dean
# Early on, you push Nora to contracting the company for producing serums
# Next, we push Nora to get the University to contract out some serum testing with MC's company
# Next, we push Nora to begin dosing the University Dean with the serums we are contracted to make for them
# Finally, MC and Nora bring the Dean under their control. Ends with MC controlling Nora, who controls the Dean.

#Single label to call and branch to the obedience storyline below.
label nora_obedience_branch_label():
    if nora.event_triggers_dict.get("nora_contracts_intro_complete", False) == False:
        call nora_obedience_intro_label() from _nora_obedience_step_1_01a
    elif nora.story_tracker.path_step("University Contracts") == 0 and nora.obedience >= 120 and nora.event_triggers_dict.get("contract_count", 0) >= 2:
        call nora_obedience_dean_intro_label() from _nora_obedience_step_2_02a
    elif nora.story_tracker.path_step("University Contracts") == 1 and nora.obedience >= 140 and nora.event_triggers_dict.get("contract_count", 0) >= 4:
        call nora_obedience_dean_update_label() from _nora_obedience_step_3_03a
    elif nora.story_tracker.path_step("University Contracts") == 2:
        call nora_obedience_dean_followup_label() from _nora_obedience_step_3_03b
    elif nora.story_tracker.path_step("University Contracts") == 3 and nora.obedience >= 160 and nora.event_triggers_dict.get("contract_count", 0) >= 6:
        call nora_obedience_dean_submission_label() from _nora_obedience_step_4_04a
    elif nora.story_tracker.path_complete("University Contracts"):
        call nora_obedience_epilogue_label() from _nora_obedience_step_6_06a
    elif nora.story_tracker.path_step("University Contracts") == 4:
        call nora_obedience_dean_submission_epilogue_label() from _nora_obedience_step_5_05a
    else:
        call nora_obedience_basic_update_label() from _nora_obedience_no_update_07a
    return

# Saturday meeting labels
# All related Saturday meeting labels have Nora solo in a scene manager for visual effects
label nora_obedience_intro_label():
    nora "Good evening, [nora.mc_title]. I've got good news for you."
    mc.name "Oh?"
    nora "You really owe me though. I talked to the university dean this week, and gave him some... sanitized information about your business."
    nora "He was extremely hesitant to commit to anything, but I was able to persuade him with a logical appeal."
    nora "He has agreed to put out a small, standing contract with your company for some of your serum."
    mc.name "Oh! That's great."
    nora "He was very sceptical about it, and I hid the true, shall we say, benefits of it."
    nora "You see, the university already has a fairly large contract with another company for research drugs with similar... specifications."
    mc.name "Wait... I have a competitor?"
    nora "Of course. You think you have something completely unique? There are always people, everywhere, pushing the boundaries of science."
    "It makes sense, but you hadn't really thought it through."
    nora "Anyway, I did some poking around with your competitor, and some of the things I've learned have been... troubling."
    nora "It seems that the university dean and a few other men have formed a sort of leadership group that has been pulling strings on things around the city."
    nora "You should be careful, the other company has their eyes out for similar drug designs as theirs. If a start up were to draw too much attention to themselves, it might lead to issues..."
    #Check here and see if we have already been visited by Penelope
    mc.name "Interesting. Yeah, I'll be careful."
    nora "Anyway, I'm going to keep doing some digging, but in the mean time, PLEASE, fulfill these contracts."
    nora "Don't make me look like an idiot by ignoring them, okay?"
    nora "I even made it easy. The contract is designed specifically to match your blue serum. Just make some and sell it us."
    mc.name "Will do, [nora.title]. And thank you for your hard work."
    $ nora.change_love(1, 40)
    $ nora.change_obedience(1, 140)
    nora "Of course."
    nora "Also, the dean is now aware that we are at least PARTIALLY working together."
    nora "I took the liberty of adding your name to the list of registered University business partners."
    mc.name "... and that means..."
    nora "Feel free to swing by and see me at the University sometime. You won't be turned away at security."
    mc.name "Oh! Right."
    "It has been a while since you stepped foot on University property. You aren't sure what you'll need there, but at least you have the ability to do so now."
    $ university.visible = True
    $ nora.event_triggers_dict["nora_contracts_intro_complete"] = True
    $ nora.story_tracker.start_path(nora, "University Contracts")
    return

# Use this label if we don't have any obedience changes.
label nora_obedience_basic_update_label():
    nora "Good evening, [nora.mc_title]."
    mc.name "Hello. Hows it going at the university? Learn anything new this week?"
    nora "Not much to report this week. Just keep fulfilling those serum contracts."
    mc.name "Alright."
    return


label nora_obedience_dean_intro_label():
    nora "Good evening, [nora.mc_title]. I've got news for you."
    mc.name "Oh? Good news?"
    nora "I'm not sure yet."
    nora "The dean paid me a visit today. He appears to have taken a new interest in your business, and your product."
    nora "I managed to... convince him to expand your contract a bit."
    mc.name "Oh! Convinced? What do you mean? Did you... sleep with him?"
    nora "What!?! NO. Fuck no. No I managed to convince him using your tactics..."
    "Umm... so she DID sleep with him?"
    mc.name "I... I don't know what you mean..."
    nora "I was pretending to be a good subordinate and got him coffee. When he wasn't looking, I slipped one of your serums in his drink."
    nora "It truly does make convincing him much easier."
    mc.name "OH... right... that's exactly my tactics... you're right."
    nora "Right. Same tactics, different goals. While you use it to get in women's panties, I used it to further my position in the department."
    "Damn. She's out of line but she's right."
    nora "I've been given much more control over university drug contracts, so my first move was to update yours."
    nora "In addition, the dean wants to meet with me, *personally*, every week to update him on progress."
    mc.name "That's great..."
    "An idea begins to form in your head."
    mc.name "I think you should probably know something, if [stephanie.title] hasn't already told you."
    mc.name "We have an updated serum prototype, one that would be very useful for someone who wants to increase their influence on someone."
    mc.name "The first serum one is blue, but this one is red. I can forward you the design specs for it, if you want to change the contract details."
    "She thinks about it for a moment."
    nora "[nora.mc_title], are you suggesting I continue to drug the university dean to increase my influence over him?"
    mc.name "Ummm, I mean if you decided to do something like that you should probably have the proper tools to do it."
    mc.name "You said you are meeting with him weekly now."
    nora "Yes..."
    "There is a long pause."
    nora "Forward the details to me. I'll update your contract before they go out on Monday."
    "[nora.possessive_title!c] has updated your serum contract!"
    "By default, the red serum fulfills the specs, but any serum with the right modifiers and that improves obedience and suggestibility will work!"
    $ nora.story_tracker.advance_path(nora, "University Contracts")
    return

label nora_obedience_dean_update_label():
    nora "Good evening, [nora.mc_title]..."
    "Something about the way she greets you is troubling."
    mc.name "Good evening [nora.title]. How are things at the university this week?"
    nora "Well... we'll find out soon. I've had a bit of a development this week."
    mc.name "Oh?"
    nora "The dean... he wants to meet with you this week."
    mc.name "Meet... with me?"
    nora "Yes. Said he's been hearing about you and your exploits from his colleagues."
    nora "I think he wants to cooperate with you on some level..."
    "Hmm. Interesting."
    mc.name "I see. When does he want to meet?"
    nora "He said anytime during normal business hours this week, but he said *specifically* I am NOT to attend."
    mc.name "Interesting..."
    "She looks very nervous."
    mc.name "Have you been giving him the obedience serums you've been contracting out for?"
    nora "Yes, I have... do you think he is suspicious?"
    mc.name "Maybe. I'll see if I can find out when I meet with him."
    nora "Ah, so you'll do it?"
    mc.name "Of course. The more I can find out about his group the better."
    "[nora.possessive_title!c] is barely able to keep her voice down."
    nora "Look, I've helped you so much so far, but be careful with this man. I've been loyal to you since the start!"
    nora "If he offers you something... just pretend to accept."
    "You use your hands to hush her a bit."
    nora "I think he realizes something is going on, but he doesn't understand what."
    "For the first time, [nora.title] appears to be afraid. This is certainly an interesting development."
    mc.name "I'll go, and see what I can find out. But his offer would have to be pretty fucking good for me to consider it."
    "She seems a little relieved, but still nervous."
    nora "Okay, when can you meet him this week?"
    "You quickly consult your calender."
    $ time_slot = mc.schedule.get_next_open_time_slot(time_restriction = 1)    #Defaults to next business day
    if time_slot == None:
        mc.name "I'm actually all booked this week... can we talk about this again next week?"
        nora "I... I suppose."
        return
    $ time_text = day_and_time_string(time_slot[0], time_slot[1])
    mc.name "I can do it [time_text]."
    nora "I'll let him know. [time_text], at the University. Don't be late!"
    mc.name "Of course."
    $ mc.create_event("nora_obedience_dean_first_meeting_label", "Appointment with University Dean", time_slot = time_slot, person = nora)
    $ nora.story_tracker.advance_path(nora, "University Contracts")
    return

label nora_obedience_dean_first_meeting_label(the_person = nora):
    "In this label, we meet the dean of the university, face to face."
    $ university.show_background()
    "He talks about MC's serums he's heard rumours about from other council members, but doesn't seem to connect them with [nora.title]."
    "Instead, MC discovers that the dean has been using serums from your competitor to try and corrupt [nora.possessive_title], but they aren't working."
    "Players realize that the other serums are the reason she seems to have developed distaste for bareback sex, etc."
    "The dean asks for MC's help corrupting her with his serums, since the other ones clearly aren't working correctly."
    "He offers significant monetary rewards and future contracts to players if he fulfills a set of contracts for him, that he intends to use on [nora.title]."
    "He also offers his vote on the city council, and access to a prioritized university intern program."
    "Players understand the offer, and are presented internally with the choice of working with the Dean, or working with Nora."
    "However, savvy players may manage to partially corrupt [nora.title] before siding with her."
    $ nora.event_triggers_dict["dean_deal_proposed"] = True
    return

label nora_obedience_dean_followup_label():
    nora "Good evening, [nora.mc_title]. How did it go?"
    mc.name "The meeting with the dean?"
    nora "YES. How did it go?"
    mc.name "It went well I think."
    "Of course, you aren't going to share the details of EVERYTHING with her. Not yet anyway."
    nora "Does... does he suspect me?"
    mc.name "Actually, I don't think he does. Most of our discussion was about my serum formulas."
    mc.name "He has heard about it from outside sources, and wants to get his hands on a few specific samples."
    "[nora.possessive_title!c] seems relieved, but still a bit nervous."
    nora "Hmm, I wonder what he wants the samples for. He didn't say, did he?"
    mc.name "No, he didn't."
    "It hurts a bit to lie, but you haven't made up your mind yet which way you want to go."
    "You could continue to help [nora.title]. With the information you recorded and more dosages of your obedience serums, you could soon have the dean in your pocket."
    "Or... you could soon have a grateful dean working together with you, and a sluttified [nora.title] to play with..."
    "The next few weeks will be critical. You can continue to work with [nora.possessive_title], or work with the dean. But either way, you need to decide."
    "*NOTE* Working with dean has not yet been written. To continue what is written of this story, keep working with [nora.title] and fulfilling her contracts."
    "In addition, keep working on her obedience. You want HER to be under YOUR influence, whenever she breaks the dean!"
    $ nora.story_tracker.advance_path(nora, "University Contracts")
    return

label nora_obedience_dean_submission_label():
    nora "Good evening, [nora.mc_title]. I've got good news."
    mc.name "Yeah?"
    nora "Things are progressing with the dean. I've almost got him under my thumb."
    nora "I changed our meeting time this week, and it is time for me stage a little *incident*."
    mc.name "Ummm... what do you mean by incident?"
    nora "First of all, before I explain, I want you to understand that this is all just for show. Do you understand?"
    mc.name "What is?"
    nora "I have no attraction in the dean whatsoever. But you are going to walk in on us in a, shall we say, compromising situation."
    mc.name "Ah, a classic honeypot plan."
    nora "Umm, not exactly... When could you swing by? Some evening this week."
    "You quickly consult your calender."
    $ time_slot = mc.schedule.get_next_open_time_slot(time_restriction = 3)    #Defaults to next business day
    if time_slot == None:
        mc.name "I'm actually all booked this week... can we talk about this again next week?"
        nora "I... I suppose."
        return
    $ time_text = day_and_time_string(time_slot[0], time_slot[1])
    mc.name "I can do it [time_text]."

    nora "Okay. On [time_text], my office will be 'accidentally' unlocked, just let yourself in. I'll text you the exact time when I have the details worked out."
    mc.name "Alright. I'm not sure I understand the plan, but I'll be there."
    nora "Don't worry. You'll appreciate the situation when you get there."
    $ mc.create_event("nora_obedience_dean_final_submission_label", f"Appointment with {nora.fname}", time_slot = time_slot, person = nora)
    $ nora.story_tracker.advance_path(nora, "University Contracts")
    return

label nora_obedience_dean_final_submission_label(the_person = nora):
    "You get a text on your phone. It's from [nora.possessive_title]."
    nora "Walk into my office at 6:30 pm tonight. Sharp."
    "You text her back with a thumbs up emoji."
    "She has been working on the dean for several weeks now, slowly corrupting him and feeding him obedience serums."
    "Her proposal to have you walk in on them in a compromising situation is interesting. You wonder what exactly you are walking in to."
    $ university.show_background()
    "You don't have much time to consider it. You head to the university, and soon you are standing outside of her office."
    "You check the time. 6:27. You put your ear to the door and listen."
    nora "That's right. Good boy. Now come show your mistress how good you've been."
    "Umm... damn... something fun is going on in there..."
    "You hear a few gasps and moans coming from the room."
    "After what feels like forever, you look at your watch again. 6:29."
    "Fuck it. Close enough, right?"
    "You make a show of knocking on the door and then open it without waiting for a response. You swing it wide open and walk inside, pretending to already be speaking."
    mc.name "Hey [nora.title], sorry to bug you, but I wanted to look at the details..."
    if the_person.wardrobe.get_outfit_with_name("Nora Lingerie"):
        $ the_person.apply_outfit(the_person.wardrobe.get_outfit_with_name("Nora Lingerie"))
    else:
        $ the_person.apply_outfit(lingerie_wardrobe.pick_random_outfit(), update_taboo = True)
    $ the_person.draw_person(position = "against_wall")
    "You don't have to pretend to be surprised at what you see when you step inside the office."
    "[nora.possessive_title] is sitting on her desk in black lingerie, her legs splayed wide open, and the university dean is on all fours, with a collar on, his face buried between her legs."
    "Hearing you enter, he suddenly pulls away from her and looks at you in shock and surprise."
    nora "Hey! Who said you could stop?"
    "A leash that you didn't see before suddenly goes taught, and [nora.title] pulls his face back up between her legs."
    nora "Ah, [mc.name]. What a pleasant surprise. The dean and I were just discussing your future contract arrangements."
    mc.name "Ahh... favourable terms, I hope?"
    nora "Of course."
    mc.name "And what about his influence and vote for council meetings?"
    nora "Ah, let me ask him. Boy, pause for a moment."
    "The university dean sheepishly pulls away from her."
    nora "You don't mind voting the way I ask you to for council meetings, do you?"
    "Dean" "Ahh, if my mistress has an opinion, of course I'll voice it and vote accordingly..."
    nora "Excellent. Now, where were you?"
    "The leash goes taught and the university dean resumes eating out [nora.possessive_title]."
    nora "Well [nora.mc_title], it would seem that you've gained a vote on the city council from here on out."
    nora "Now... was there something I can do for you?"
    "She licks her lips. Watching her getting eaten out by another man is something you were certainly not expecting, and you take a moment to think about how it makes you feel."
    "Note: Regardless of what you choose, you will follow up with [nora.title] about how you feel about her having sex with other men at another time."
    menu:
        "Use HER mouth (disabled)" if not the_person.is_willing(blowjob):
            pass
        "Use HER mouth (disabled)" if the_person.is_willing(blowjob):   #I haven't written this yet
            pass
        "Excuse yourself":
            mc.name "I'm afraid I must be off. But it was good to see you again, Dean."
            "You hear a vaguely mumbled response."
            "You back out of the office, leaving [nora.title] to her fun."
    "You have now gained influence over the Dean of the University!"
    "Controlling his vote on the city council enhances your plans for your business and the city!"
    if mc.business.event_triggers_dict.get("council_influence", None):
        $ mc.business.event_triggers_dict.get("council_influence", None).append(("University", "submission"))
    else:
        $ mc.business.event_triggers_dict["council_influence"] = [("University", "submission")]
    $ nora.progress.obedience_step = 5
    return

label nora_obedience_dean_submission_epilogue_label():
    nora "Good evening, [nora.mc_title]..."
    mc.name "Hey"
    "She looks a bit embarrassed. It is clear she wants to talk about what happened this week."
    nora "Look... about the dean..."
    mc.name "Yeah?"
    nora "What are your feelings about what happened?"
    mc.name "About you making him submit to you?"
    nora "Yeah? I mean, kind of..."
    "She clears her throat."
    nora "Look, I want to make sure we are on the same page here."
    nora "The dean is fun little toy, but he's just that."
    nora "I want to make sure you aren't upset that I was... playing with him."
    "Ah, looks she is trying to figure out if you are jealous."
    "You suppose that is a normal thing to be concerned about. You make sure to give her a clear answer."
    "Note: At this point, no content has been made that uses this decision."
    menu:
        "Having toys is fine":
            mc.name "I don't mind if you entertain yourself once in a while."
            mc.name "After all, I'm doing the same thing, aren't I?"
            nora "Ah, okay. I just wanted to make sure you didn't mind."
            mc.name "Not at all, just don't forget who YOUR daddy is."
            nora "Yes of course."
            $ nora.event_triggers_dict["may_have_toys"] = True
        "Don't do it again, you are mine.":
            mc.name "We did what we had to, but don't do that again."
            mc.name "You are mine. And Mine alone. Understand?"
            nora "Ah, yes sir."
            $ nora.event_triggers_dict["may_have_toys"] = False
    "With that settled, you wait for [stephanie.title] to arrive."
    $ nora.story_tracker.advance_path(nora, "University Contracts")
    return

label nora_obedience_epilogue_label():
    nora "Good evening, [nora.mc_title]."
    mc.name "Hello [nora.title]. Have a good week?"
    nora "Yes, you?"
    mc.name "Same."
    return
