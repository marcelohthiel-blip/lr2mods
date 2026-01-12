# Multiple choice event where there are two major decisions
# First, WHO do you want to dose?
# Second, what nano serum to dose with?
# multiple choice progression is based on Ellie and Stephanie being willing to be your test subject.

transform character_researcher_1(xoffset = 0, yoffset = 0, zoom = 0.7):
    yalign (0.85 + yoffset)
    yanchor 1.0
    xalign (0.50 + xoffset)
    xanchor 1.0
    xzoom -.95
    zoom zoom

transform character_researcher_2(xoffset = 0, yoffset = 0, zoom = 0.8):
    yalign (0.9 + yoffset)
    yanchor 1.0
    xalign (0.4 + xoffset)
    xanchor 1.0
    xzoom .95
    zoom zoom


label ellie_stephanie_teamup_progression_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: ellie_stephanie_teamup_progression_scene_action_label():
    $ the_person.set_event_day("testing_teamup")
    call progression_scene_label(ellie_stephanie_teamup_progression_scene, [the_person, mc.business.head_researcher]) from _ellie_stephanie_teamup_progression_scene_call_test_01  #[the_person] parameter should be a list of people in the scene itself, IE [mom], [mom,lily], [sarah,erica,mom], etc
    return

label ellie_stephanie_teamup_progression_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ the_researcher = the_group[1]
    $ scene_manager = Scene()
    if mc.is_at(mc.business.r_div):
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! Can you meet me down in the lab?"
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You walk down to the lab."
        $ mc.change_location(mc.business.r_div)

    $ scene_manager.add_actor(the_person, the_person.outfit)
    the_person "Hey [the_person.mc_title]. I've run into a bit of a situation with the nanobots."
    mc.name "Oh? What's wrong?"
    the_person "I recently ran a tweak to some of the code... but the time it takes to get feedback on code revisions takes ages."
    $ scene_manager.add_actor(the_researcher, the_researcher.outfit, display_transform = character_center_flipped, position = "walking_away")
    "[the_researcher.possessive_title!c] walks by as you chat with [the_person.title]."
    the_person "I wish there was some way we could get more immediate test results... the waiting is really hampering my productivity."
    $ scene_manager.update_actor(the_researcher, position = "stand3")
    "[the_researcher.title] suddenly turns to you and [the_person.possessive_title]."
    the_researcher "Wait... did I hear you would like immediate test results?"
    the_person "Errr, I think so?"
    the_researcher "I've got a great idea! We recently put a serum testing clause in place. Let's draft someone and run it!"
    the_person "You want to give them to an employee? I mean, I guess that could work..."
    the_researcher "Of course it would work. Let me just pull up the list here..."
    "[the_researcher.possessive_title!c] turns and logs in to a nearby computer terminal."
    $ scene_manager.update_actor(the_researcher, display_transform = character_left, position = "standing_doggy")
    $ mc.change_locked_clarity(10)
    "Her ass sways a bit as she logs in and pulls up an employee list."
    the_researcher "Alright... here's my short list of employees to call in. Who do you think we should test [the_researcher.mc_title]?"
    $ scene_manager.update_actor(the_researcher, position = "stand3")
    "[the_researcher.title] stands up and to the side. You look at the computer terminal..."
    $ possible_picks = [x for x in mc.business.employees_availabe if x not in (the_person, the_researcher) and x.obedience >= 110]
    call screen employee_overview(white_list = possible_picks, person_select = True)
    $ pick_1 = _return
    if not isinstance(pick_1, Person):
        mc.name "Sorry, I don't think any of these girls will work..."
        the_researcher "Bullshit. Hang on, I'll pick one..."
        $ pick_1 = get_random_from_list(possible_picks)
        if not isinstance(pick_1, Person): # abort when no girl picked
            the_researcher "You are right, I can't find any suitable candidates."
            $ possible_picks  = None
            return
        the_researcher "Ah, here we go."
    $ possible_picks  = None
    the_researcher "I'll go get her."
    $ scene_manager.hide_actor(the_researcher)
    "[the_researcher.title] hurries off, leaving you with [the_person.possessive_title]."
    the_person "Stars, this is happening so fast... I'm not sure I even have any ready!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She quickly turns to one of the research stations. You see her quickly prepare a small tab of nanobots."
    $ scene_manager.update_actor(the_person, position = "default")
    the_person "There... that should do it. I made up a quick tab of basic bots to test."
    "You talk with [the_person.title] for a bit about her coding optimizations until [the_researcher.possessive_title] returns."
    $ scene_manager.show_actor(the_researcher, display_transform = character_left)
    $ scene_manager.update_actor(pick_1, display_transform = character_center_flipped)
    "She returns with [pick_1.possessive_title]."
    the_researcher "Yes, it is in the employee manual. Don't worry, we'll be observing you the entire time, okay?"
    pick_1 "Okay I guess... Oh, [pick_1.mc_title]? You didn't tell me he was going to be here too."
    mc.name "Yes, I will also be observing."
    pick_1 "I see. I guess that's okay then."
    the_researcher "Alright. Let's get started!"
    "In the corner of the research department, you have a small room designed for private testing. You walk into the room with the three girls."
    $ mc.change_location(testing_room)
    $ scene_manager.update_actor(the_person, display_transform = character_researcher_1)
    $ scene_manager.update_actor(the_researcher, display_transform = character_researcher_2)
    $ scene_manager.update_actor(pick_1, display_transform = character_right, position = "sitting")
    "The two researchers stand to one side, while your test subject sits on the exam table."
    "You take the tablet from [the_person.possessive_title]."
    mc.name "Alright, here you go [pick_1.title]. The effects should happen fairly quickly, so I want you to try and be mindful of what you are feeling."
    "You hand the tablet to [pick_1.possessive_title]. She swallows it with a glass of water."
    the_researcher "Alright, while we are waiting, let's go over a quick questionnaire. We can compare them between the before and after."
    pick_1 "Okay..."
    "You listen as [the_researcher.possessive_title] starts to ask some standard survey questions... It goes on for a while..."
    $ fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, 2, pick_1)
    $ pick_1.change_arousal(15)
    "However, as you watch [pick_1.title]..."
    $ fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, 2, pick_1)
    $ pick_1.change_arousal(15)
    "She seems to be getting aroused... some of her answers are starting to take longer than they should..."
    if pick_1.opinion.masturbating < 2:
        $ pick_1.max_opinion_score("masturbating", add_to_log = True)
    else:
        $ fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, 2, pick_1)
    $ pick_1.change_arousal(15)
    "[the_researcher.title] seems to be picking up on it also."
    the_researcher "Are you doing okay, [pick_1.name]?"
    pick_1 "I'm sorry... I'm just having a really hard time concentrating... I just... I'm feeling really hot..."
    the_researcher "Ah, can you describe what you are feeling?"
    pick_1 "To be honest, I really feel the need to... touch myself."
    "You hear a small gasp from [the_person.title], but you notice [the_researcher.possessive_title] give a slight smile."
    the_researcher "Would you say that you feel a strong urge to masturbate?"
    pick_1 "Uhhh... yeah... incredibly strong actually..."
    "You can see [the_researcher.title] and [the_person.possessive_title] chatting for a few moments, but can't really tell what they are saying..."
    "Then, you see [the_researcher.possessive_title] look over at you and give a quick wink."
    the_researcher "Alright, remember this is for science. Go ahead and masturbate, and let us know if anything feels different than usual."
    pick_1 "Ahh, umm... okay..."
    the_researcher "If it makes you feel uncomfortable we can have Mr. [mc.last_name] leave the room."
    "You shoot her a quick glare. Thankfully [pick_1.title] doesn't seem to notice."
    pick_1 "No, that's alright. I don't mind..."
    $ scene_manager.update_actor(pick_1, position = "kneeling1")
    if pick_1.vagina_available:
        "[pick_1.possessive_title!c] repositions herself and slowly runs a hand down between her legs."
        "You watch as she dips a finger into her exposed pussy while using her palm to press down on her clit."
        $ mc.change_locked_clarity(30)
    else:
        "[pick_1.possessive_title!c] repositions herself and slowly runs a hand down between her legs."
        "Her hand disappears under her clothes as she starts to touch herself."
        $ mc.change_locked_clarity(10)
    pick_1 "Ahh.... mmm..."
    $ pick_1.change_arousal(30)
    "[pick_1.possessive_title!c] doesn't waste any time. She moans as she touches herself."
    pick_1 "Oh god... it feels so good... I feel like my whole body is on fire..."
    "[pick_1.title] bites her lip and looks you straight in the eyes as she continues to touch herself."
    "Her eyes flicker down to your crotch a couple of times. You can tell she wants you to step in, but you stick to observing."
    $ pick_1.change_arousal(50)
    "You can see [pick_1.possessive_title] has really picked up the pace and her eyes are starting to glaze over a bit. She's almost finished."
    pick_1 "Oh fuck... oh!"
    $ pick_1.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(50)
    $ pick_1.change_stats(obedience = 3, slut = 2, max_slut = 50)
    "[pick_1.title]'s legs shake a bit as she starts to orgasm. Her moans echo through the small test room as you watch."
    "Eventually she finishes, slowly moving her hand away from her crotch."
    the_researcher "How do you feel now? Was that helpful?"
    "[pick_1.title] startles at the sudden question."
    $ scene_manager.update_actor(pick_1, position = "missionary")
    pick_1 "Oh! Uhhh... yeah... but I think I need to lay down for a bit..."
    the_researcher "That's fine. We will leave you the room to recover."
    $ mc.change_location(mc.business.r_div)
    $ scene_manager.remove_actor(pick_1)
    $ scene_manager.update_actor(the_researcher, display_transform = character_center_flipped)
    $ scene_manager.update_actor(the_person, display_transform = character_right)
    "You step out of the room with [the_researcher.title] and [the_person.possessive_title], leaving the test subject to recover."
    mc.name "Well that was insightful. Were you able to make any helpful observations?"
    the_researcher "Yeah, I think so."
    the_person "Yeah... hey umm... did you give her the entire tablet?"
    mc.name "I... yes?"
    the_person "I didn't think about it... that was the amount we usually put in a whole batch of serum..."
    the_researcher "Ahhh, that is why the effects were so immediate. That was actually incredibly insightful then!"
    the_person "Yeah... I think the tweaks I made for efficiency this past week worked..."
    "The two girls talk for a bit about the test. They seem to have learned quite a bit."
    $ get_fetish_basic_serum().add_mastery(2)
    $ mc.log_event(f"Mastery of {get_fetish_basic_serum().name} increased by 2.", "float_text_blue")
    the_researcher "So next time maybe we..."
    the_person "Next time?"
    the_researcher "Yeah? I mean, seems like it would be really helpful to optimize these if we study them more in depth in the future."
    the_person "Yeah, that's true... what do you think, [the_person.mc_title]?"
    mc.name "It makes sense. What kind of basis would be useful?"
    the_person "Well, sometimes I like to look at the code and make optimizations over the weekend... maybe once a week?"
    the_person "I'll finish up optimizations early in the week... maybe we could do this every Wednesday?"
    the_person "That would give me a chance to finalize changes, then have a couple days to analyse results."
    mc.name "Sounds good. [the_researcher.title], can you meet with her every Wednesday morning for these tests? I may not always be able to be here."
    the_researcher "Certainly. Especially if they all turn out as hot as this one!"
    the_person "Ahh, yeah considering the programs, they probably will..."
    mc.name "Perfect. Good work girls."
    "You say goodbye to the girls then step away. You can hear them chatting about the test."
    $ scene_manager.clear_scene()
    "You can now visit the research department every Wednesday morning to join [ellie.title] and [the_researcher.possessive_title] studying the nanobots."
    "As you return to your work, you try to adjust yourself. The scene has left you really turned on. Hopefully in the future you can take a more 'active' role in the research..."
    $ the_researcher = None
    $ mc.new_repeat_event("Research Meeting", 2, 1)
    return

label ellie_stephanie_teamup_progression_scene_intro_0(the_group):
    $ the_person = the_group[0]
    $ the_researcher = the_group[1]
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, the_person.outfit)
    $ scene_manager.add_actor(the_researcher, the_researcher.outfit, display_transform = character_center_flipped)
    "You walk into the research department. It is Wednesday morning, and [the_person.title] and [the_researcher.possessive_title] are setting up for their weekly nanobot test."
    the_researcher "These are some interesting optimizations. Do you think they will help?"
    the_person "Yeah, I do."
    the_researcher "Oh hey [the_researcher.mc_title]."
    mc.name "[the_person.fname], [the_researcher.fname]."
    the_person "Hello sir. Will you be joining us for the weekly nanotech test?"
    "You consider it. With the sexual nature of the bots, there will likely be something interesting to watch..."
    return

label ellie_stephanie_teamup_progression_scene_intro_1(the_group):
    $ the_person = the_group[0]
    "This is the second intro scene, played after you unlocked it."
    the_person "Hey, I had fun last time when you fucked my ass!"
    return

label ellie_stephanie_teamup_progression_multi_choice_scene(the_group):
    $ the_person = the_group[0]
    $ the_researcher = the_group[1]
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, the_person.outfit)
    $ scene_manager.add_actor(the_researcher, the_researcher.outfit, display_transform = character_center_flipped)
    $ nano_opinion_list = []
    $ bot_selection = ""
    $ mc.change_location(testing_room)
    "You step into the testing room and hand the two girls their coffees."
    the_researcher "Okay, now we just need to figure out who to test on..."
    menu:
        "Random Employee" if 0 in ellie_stephanie_teamup_progression_scene.scene_unlock_list:
            return 0
        "Pick an Employee" if 1 in ellie_stephanie_teamup_progression_scene.scene_unlock_list:
            return 1
        "[the_researcher.title]" if 2 in ellie_stephanie_teamup_progression_scene.scene_unlock_list:
            return 2
        "[the_person.title]" if 3 in ellie_stephanie_teamup_progression_scene.scene_unlock_list:
            return 3
        "[the_researcher.title] AND [the_person.title]" if 4 in ellie_stephanie_teamup_progression_scene.scene_unlock_list:
            return 4
    return 0


label ellie_stephanie_teamup_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label ellie_stephanie_teamup_trans_scene_1(the_group):
    $ the_person = the_group[0]
    "This is the transition to the second scene."
    the_person "I have another idea though... what if you fucked... my other hole?"
    mc.name "That's a good idea."
    return

label ellie_stephanie_teamup_progression_scene_scene_0(the_group, scene_transition = False):
    mc.name "Sorry, I don't know who to call in."
    the_researcher "Hang on, I'll just select someone at random."
    $ pick_1 = get_random_from_list([x for x in mc.business.employees_availabe if x not in (the_researcher, the_person)])
    if not isinstance(pick_1, Person):
        the_researcher "You are right, I can't find any suitable candidates."
        return

    the_researcher "Ah, here we go."
    "She shows you the personnel file for [pick_1.title] your [pick_1.current_job.job_title]."
    the_researcher "I'll go get her."
    $ scene_manager.update_actor(the_researcher, position = "walking_away")
    "As she goes to leave, [the_person.title] looks at you."
    $ scene_manager.hide_actor(the_researcher)
    the_person "So, what program do you want to test today?"
    menu:
        "Exhibitionist Program\n{menu_red}Not implemented (WIP){/menu_red} (disabled)" if fetish_exhibition_serum_is_unlocked():
            $ nano_opinion_list = FETISH_EXHIBITION_OPINION_LIST
            $ bot_selection = "exhibition"
        "Anal Program" if fetish_anal_serum_is_unlocked():
            $ nano_opinion_list = FETISH_ANAL_OPINION_LIST
            $ bot_selection = "anal"
        "Cum Program\n{menu_red}Not implemented (WIP){/menu_red} (disabled)" if fetish_cum_serum_is_unlocked():
            $ nano_opinion_list = FETISH_CUM_OPINION_LIST
            $ bot_selection = "cum"
        "Breeding Program" if fetish_breeding_serum_is_unlocked():
            $ nano_opinion_list = FETISH_BREEDING_OPINION_LIST
            $ bot_selection = "breeding"
        "Basic Program":
            $ nano_opinion_list = FETISH_BASIC_OPINION_LIST
            $ bot_selection = "basic"
    the_person "Alright, I'll get a tab of those loaded up..."
    $ scene_manager.add_actor(pick_1, pick_1.outfit, display_transform = character_left_flipped)
    $ scene_manager.show_actor(the_researcher, position = "default")
    "After a moment, [the_researcher.title] returns with your test subject."
    "[the_researcher.possessive_title!c] and [the_person.title] take their position while [pick_1.title] sits down on the exam bed."

    $ scene_manager.update_actor(the_person, display_transform = character_researcher_1)
    $ scene_manager.update_actor(the_researcher, display_transform = character_researcher_2)
    $ scene_manager.update_actor(pick_1, display_transform = character_right, position = "sitting")
    "The two researchers stand to one side, while your test subject sits on the exam table."
    "You take the tablet from [the_person.possessive_title]."
    mc.name "Alright, here you go [pick_1.title]. The effects should happen fairly quickly, so I want you to try and be mindful of what you are feeling."
    "You hand the tablet to [pick_1.possessive_title]. She swallows it with a glass of water."
    the_researcher "Alright, while we are waiting, let's go over a quick questionnaire. We can compare them between the before and after."
    pick_1 "Okay..."
    "You listen as [the_researcher.possessive_title] starts to ask some standard survey questions... It goes on for a while..."
    $ fetish_serum_increase_opinion(nano_opinion_list, 2, pick_1)
    $ pick_1.change_arousal(15)
    "However, as you watch [pick_1.title]..."
    $ fetish_serum_increase_opinion(nano_opinion_list, 2, pick_1)
    $ pick_1.change_arousal(15)
    "She seems to be getting aroused... some of her answers are starting to take longer than they should..."
    call ellie_stephanie_teamup_final_opinion_shift_label(pick_1, bot_selection, nano_opinion_list) from _call_ellie_stephanie_teamup_final_opinion_shift_label
    $ pick_1.change_arousal(35)
    "[the_researcher.title] seems to be picking up on it also."
    the_researcher "[pick_1.fname]... can you describe what you are feeling right now?"
    if bot_selection == "anal":
        call ellie_stephanie_tester_reaction_anal_label(pick_1, the_person, the_researcher) from _ellie_stephanie_teamup_anal_bot_test_01
    elif bot_selection == "cum":
        call ellie_stephanie_tester_reaction_cum_label(pick_1, the_person, the_researcher) from _ellie_stephanie_teamup_cum_bot_test_01
    elif bot_selection == "breeding":
        call ellie_stephanie_tester_reaction_breeding_label(pick_1, the_person, the_researcher) from _ellie_stephanie_teamup_breeding_bot_test_01
    elif bot_selection == "exhibition":
        call ellie_stephanie_tester_reaction_exhibition_label(pick_1, the_person, the_researcher) from _ellie_stephanie_teamup_exhibition_bot_test_01
    else:
        call ellie_stephanie_tester_reaction_basic_label(pick_1, the_person, the_researcher) from _ellie_stephanie_teamup_basic_bot_test_01
    $ pick_1 = None
    $ the_researcher = None
    return

label ellie_stephanie_teamup_progression_scene_scene_1(the_group, scene_transition = False):
    $ the_person = the_group[0]
    "This is the second scene. I'm not coding it, but you could code it that she gets naked and bends over, presenting her ass here."
    $ the_person.draw_person(position = "standing_doggy")
    the_person "Don't worry, my ass is always ready for you!"
    call fuck_person(the_person) from _call_sex_description_ellie_stephanie_teamup_scene_02

    the_person "Oh my god I hope I can walk tomorrow!"
    #You probably want to advance time after this
    #call advance_time() from _call_advance_ellie_stephanie_teamup_progression_scene_adv_03
    return


label ellie_stephanie_teamup_progression_scene_choice(the_group):
    $ the_person = the_group[0]
    $ the_researcher = the_group[1]
    "It will take up most of your morning though."
    menu:
        "Stay for the test {image=time_advance}":
            pass
        "Don't stay":
            return False
    mc.name "Yeah, I'd like to observe. Can I get you two coffee while you set up?"
    the_researcher "Yeah I'll take one."
    the_person "Me too."
    mc.name "Sounds good. I'll meet you in the testing room."
    $ scene_manager.clear_scene()
    $ mc.change_location(break_room)
    "You head to the break room and pour three coffees."
    if mc.inventory.has_serum:
        "No one is around, you look down at [the_person.possessive_title]'s coffee..."
        menu:
            "Dose coffee":
                "You look at [the_person.possessive_title]'s coffee."
                call give_serum(the_person) from _call_give_ellie_serum_teamup_05
                if mc.inventory.has_serum:
                    "You look at [the_researcher.possessive_title]'s coffee."
                    call give_serum(the_researcher) from _call_give_head_researcher_serum_teamup_06
            "Don't":
                pass
    "You pick up the coffees and head down to the testing room."
    return True

label ellie_stephanie_teamup_progression_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    $ the_researcher = the_group[1]
    mc.name "I'm afraid I have quite a bit of work to get done this morning, so you'll have to carry on without me today."
    the_researcher "Bummer."
    the_person "I understand. Maybe next week [the_person.mc_title]."
    mc.name "Maybe."
    $ clear_scene()
    $ mc.change_location(mc.business.r_div)
    $ the_researcher = None
    return

label ellie_stephanie_teamup_final_opinion_shift_label(the_tester, program_name, program_opinion_list):
    if program_name == "basic":
        if the_tester.opinion.masturbating < 2:
            $ the_tester.max_opinion_score("masturbating", add_to_log = True)
        else:
            $ fetish_serum_increase_opinion(program_opinion_list, 2, the_tester)
    elif program_name == "anal":
        if the_tester.opinion.anal_sex < 2:
            $ the_tester.max_opinion_score("anal sex", add_to_log = True)
        else:
            $ fetish_serum_increase_opinion(program_opinion_list, 2, the_tester)
    elif program_name == "cum":
        if the_tester.opinion.being_covered_in_cum < 2:
            $ the_tester.max_opinion_score("being covered in cum", add_to_log = True)
        else:
            $ fetish_serum_increase_opinion(program_opinion_list, 2, the_tester)
    elif program_name == "breeding":
        if the_tester.opinion.bareback_sex < 2:
            $ the_tester.max_opinion_score("bareback sex", add_to_log = True)
        else:
            $ fetish_serum_increase_opinion(program_opinion_list, 2, the_tester)
    elif program_name == "exhibition":
        if the_tester.opinion.public_sex < 2:
            $ the_tester.max_opinion_score("public sex", add_to_log = True)
        else:
            $ fetish_serum_increase_opinion(program_opinion_list, 2, the_tester)
    return

label ellie_stephanie_tester_reaction_basic_label(the_tester, the_person, the_researcher):
    the_tester "I'm sorry... I'm just having a really hard time concentrating... I just... I'm feeling really hot..."
    the_researcher "Hot how? Like sweaty hot?"
    the_tester "No, more like I really feel the need to... touch myself."
    "So, a similar reaction to the last time you tested this program."
    the_researcher "Would you say that you feel a strong urge to masturbate?"
    the_tester "Uhhh... yeah... incredibly strong actually..."
    "You can see [the_researcher.title] and [the_person.possessive_title] chatting for a few moments, but can't really tell what they are saying..."
    "Then, you see [the_researcher.possessive_title] look over at you and give a quick wink."
    the_researcher "Alright, remember this is for science. Go ahead and masturbate, and let us know if anything feels different than usual."
    the_tester "Ahh, umm... okay..."
    "Thankfully this time [the_researcher.possessive_title] doesn't offer to make you leave the room."
    $ scene_manager.update_actor(the_tester, position = "kneeling1")
    if the_tester.vagina_available:
        "[the_tester.possessive_title!c] repositions herself and slowly runs a hand down between her legs."
        "You watch as she dips a finger into her exposed pussy while using her palm to press down on her clit."
        $ mc.change_locked_clarity(30)
    else:
        "[the_tester.possessive_title!c] repositions herself and slowly runs a hand down between her legs."
        "Her hand disappears under her clothes as she starts to touch herself."
        $ mc.change_locked_clarity(10)
    the_tester "Ahh.... mmm..."
    $ the_tester.change_arousal(30)
    "[the_tester.possessive_title!c] doesn't waste any time. She moans as she touches herself."
    the_tester "Oh god... it feels so good... I feel like my whole body is on fire..."
    "[the_tester.title] bites her lip and looks you straight in the eyes as she continues to touch herself."
    "Her eyes flicker down to your crotch a couple of times. You can tell she wants you to step in, but you stick to observing."
    $ the_tester.change_arousal(50)
    "You can see [the_tester.possessive_title] has really picked up the pace and her eyes are starting to glaze over a bit. She's almost finished."
    the_tester "Oh fuck... oh!"
    $ the_tester.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(50)
    $ the_tester.change_stats(obedience = 3, slut = 2, max_slut = 50)
    "[the_tester.title]'s legs shake a bit as she starts to orgasm. Her moans echo through the small test room as you watch."
    "Eventually she finishes, slowly moving her hand away from her crotch."
    the_researcher "How do you feel now? Was that helpful?"
    "[the_tester.title] startles at the sudden question."
    $ scene_manager.update_actor(the_tester, position = "missionary")
    the_tester "Oh! Uhhh... yeah... but I think I need to lay down for a bit..."
    the_researcher "That's fine. We will leave you the room to recover."
    $ mc.change_location(mc.business.r_div)
    $ scene_manager.remove_actor(the_tester)
    $ scene_manager.update_actor(the_researcher, display_transform = character_center_flipped)
    $ scene_manager.update_actor(the_person, display_transform = character_right)
    "You step out of the room with [the_researcher.title] and [the_person.possessive_title], leaving the test subject to recover."
    return

label ellie_stephanie_tester_reaction_anal_label(the_tester, the_person, the_researcher):
    the_tester "I'm sorry... I'm just having a really hard time concentrating... I just... I'm feeling really strange!"
    the_researcher "Strange how?"
    if the_tester.sluttiness < 20:  #
        the_tester "Like I'm just... I don't know... empty."
        the_researcher "Like you need to eat?"
        the_tester "No... I feel like... this is going to sound crazy!"
        the_tester "I have this really weird urge to put something like... up my bottom..."
        "She barely manages to choke out the last few words."
    elif the_tester.sluttiness < 60:
        the_tester "I feel like my ass feels empty I guess?"
        the_tester "This is so weird. I feel like I want to stick something in my ass!"
        "[the_tester.title] looks around the room, stopping when she looks at you. Her eyes flicked down to your crotch and linger for a moment."
        the_tester "[the_tester.mc_title] I..."
        "She starts to say something but stops. You can tell the nanobots are having quite the effect on her."
    else:
        the_tester "No, like my ass is so empty! I... I need someone to fuck my ass!"
        "You hear a small gasp from the testing booth, but you aren't sure if it is from [the_researcher.title] or [the_person.possessive_title]."
        the_tester "[the_tester.mc_title]... will you? I need it! Please!?!"
        "[the_tester.title] has started begging. You glance at [the_researcher.possessive_title] and [the_person.title]."
        the_researcher "I mean, I think we have the data that we need..."
        the_person "It would be kinda mean to get her all worked up like this and leave her hanging..."
    "[the_researcher.title] and [the_person.possessive_title] talk quietly with each other for a few moments."
    "[the_researcher.possessive_title!c] looks up at you."
    the_researcher "We have the data we need so, we're going to leave now. Whatever happens after we leave is up to you..."
    $ scene_manager.remove_actor(the_researcher)
    $ scene_manager.remove_actor(the_person)
    "The two girls exit, leaving you alone with [the_tester.possessive_title]."
    the_tester "[the_tester.mc_title], it's getting hard to think..."
    $ the_tester.add_situational_slut("Test", 10, "I can't think anymore!")
    "It seems the nanobots are having a profound impact on her."
    "You could help her out, or leave her here to try and masturbate her way through the effects."
    menu:
        "Finger her ass":
            mc.name "Don't worry, I can help you."
            if the_tester.sluttiness < 60:
                "[the_tester.title] looks at you nervously as you start to walk over to her."
            else:
                "[the_tester.title] watches you eagerly as you start to walk over to her."
            mc.name "I know it is hard to reach your asshole yourself, so I'll finger it for you until the urges pass."
            $ the_tester.change_arousal(10)
            the_tester "Mmm, that sounds amazing right now..."
            call ellie_stephanie_tester_anal_finger_label(the_tester) from _anal_bot_anal_finger_01
        "Fuck her ass" if the_tester.is_willing(prone_anal):
            mc.name "Don't worry, I can help you."
            if the_tester.sluttiness < 60:
                "[the_tester.title] looks at you nervously as you start to walk over to her."
            else:
                "[the_tester.title] watches you eagerly as you start to walk over to her."
            "She gasps when you take off your pants, revealing your erection."
            mc.name "You and I both know that the cravings you are having right now can only be satisfied by one thing."
            if the_tester.sluttiness < 60:
                "[the_tester.title] looks concerned, but not afraid."
                the_tester "I don't know... are you sure that... monster... is going to fit?"
                mc.name "Definitely. But don't worry, we can take it slow if we need to."
                the_tester "Mmm... okay..."
            else:
                the_tester "Mmm, I was thinking the same thing. I can't wait to have that monster inside me!"
            call ellie_stephanie_tester_anal_sex_label(the_tester) from _anal_bot_test_anal_sex_01
        "Leave her":
            call ellie_stephanie_tester_left_alone_label(the_tester) from _anal_bot_testing_left_alone_01
            return

    $ scene_manager.remove_actor(the_tester)
    $ mc.change_location(mc.business.r_div)
    "You step out of the testing room, leaving [the_tester.possessive_title] to recover."
    $ get_fetish_anal_serum().add_mastery(1)
    "You are pretty sure that [the_researcher.title] and [the_person.possessive_title] got some useful research data from this experiment."
    $ the_tester.clear_situational_slut("Test")
    return

label ellie_stephanie_tester_reaction_cum_label(the_tester, the_person, the_researcher):
    pass
    return

label ellie_stephanie_tester_reaction_breeding_label(the_tester, the_person, the_researcher):
    the_tester "I'm sorry... I'm just having a really hard time concentrating... I just... I'm feeling really strange!"
    the_researcher "Strange how?"
    if the_tester.is_pregnant:
        the_tester "I feel so happy... but also... empty?"
        the_researcher "Like you need to eat?"
        the_tester "No, not like that."
        the_tester "I feel like I need a man to... fill me up again..."
        "She rubs her belly for a few moments."
    if the_tester.sluttiness < 20:  #
        the_tester "Like I'm just... I don't know... empty."
        the_researcher "Like you need to eat?"
        the_tester "No... I feel like... this is going to sound crazy!"
        if the_tester.is_single:
            the_tester "I am getting this really strong urge to mess around with someone have sex that is... risky..."

        else:
            the_tester "I really wish [the_tester.SO_name], my [the_tester.so_title] was here!"
            the_tester "I'm having urges to mess around with him and sex that would be kind of... risky..."
        "She seems a bit embarrassed with the last part."
    elif the_tester.sluttiness < 60:
        the_tester "I'm getting the itch, you know?"
        the_tester "Like that feeling when your body decides it is time to make a baby but... the urge is WAY stronger than usual!"
        "[the_tester.title] looks around the room, stopping when she looks at you. Her eyes flicked down to your crotch and linger for a moment."
        the_tester "[the_tester.mc_title] I..."
        "She starts to say something but stops. You can tell the nanobots are having quite the effect on her."
    else:
        the_tester "No, like my poor cunt is empty! It should be full, dripping virile cum into my panties all day long!"
        "You hear a small gasp from the testing booth, but you aren't sure if it is from [the_researcher.title] or [the_person.possessive_title]."
        the_tester "[the_tester.mc_title]... will you? I need it! Please!?!"
        "[the_tester.title] has started begging. You glance at [the_researcher.possessive_title] and [the_person.title]."
        the_researcher "I mean, I think we have the data that we need..."
        the_person "It would be kinda mean to get her all worked up like this and leave her hanging..."
    "[the_researcher.title] and [the_person.possessive_title] talk quietly with each other for a few moments."
    "[the_researcher.possessive_title!c] looks up at you."
    the_researcher "We have the data we need so, we're going to leave now. Whatever happens after we leave is up to you..."
    $ scene_manager.remove_actor(the_researcher)
    $ scene_manager.remove_actor(the_person)
    "The two girls exit, leaving you alone with [the_tester.possessive_title]."
    the_tester "[the_tester.mc_title], it's getting hard to think..."
    $ the_tester.add_situational_slut("Test", 10, "I can't think anymore!")
    "It seems the nanobots are having a profound impact on her."
    "You could help her out, or leave her here to try and masturbate her way through the effects."
    menu:
        "Fuck her" if the_tester.is_willing(missionary):
            mc.name "Don't worry, I can help you."
            if the_tester.sluttiness < 60:
                "[the_tester.title] looks at you nervously as you start to walk over to her."
            else:
                "[the_tester.title] watches you eagerly as you start to walk over to her."
            "She gasps when you take off your pants, revealing your erection."
            mc.name "You and I both know that the cravings you are having right now can only be satisfied by one thing."
            if the_tester.sluttiness < 60:
                "[the_tester.title] looks concerned, but not afraid."
                the_tester "I wouldn't usually do this, but I think that the test..."
                mc.name "Don't worry, I'll help you with those urges. We can go slow."
                the_tester "Mmm... okay..."
            else:
                the_tester "I know! Put that monster inside me and cum as deep as you can! Fill me up with your hot, virile cum!"
            call ellie_stephanie_tester_breeding_sex_label(the_tester) from _breeder_bot_test_breeding_sex_01
        "Finger her":
            mc.name "I'm sorry, I can't give you EXACTLY what your body is craving, but I can at least take the edge off."
            call serum_tester_finger_aid_label(the_tester) from _breeding_bot_test_finger_bang_01
        "Leave her":
            call ellie_stephanie_tester_left_alone_label(the_tester) from _anal_bot_testing_left_alone_02
            return

    $ scene_manager.remove_actor(the_tester)
    $ mc.change_location(mc.business.r_div)
    "You step out of the testing room, leaving [the_tester.possessive_title] to recover."
    $ get_fetish_breeding_serum().add_mastery(1)
    "You are pretty sure that [the_researcher.title] and [the_person.possessive_title] got some useful research data from this experiment."
    $ the_tester.clear_situational_slut("Test")
    return

label ellie_stephanie_tester_reaction_exhibition_label(the_tester, the_person, the_researcher):
    pass
    return

label ellie_stephanie_tester_left_alone_label(the_tester):
    "You decide to leave her in the testing room to deal with her urges herself."
    mc.name "I'm sorry [the_tester.title], but I have other work to accomplish."
    mc.name "You can stay in here as long as you need though. I'll lock the door on my way out to make sure you aren't disturbed."
    if the_tester.sluttiness < 40:
        the_tester "Ah, okay. Thank you, I appreciate it."
    elif the_tester.sluttiness >= 80:
        the_tester "Wow, you are leaving me alone? Okay..."
    else:
        the_tester "I wish you would stay... but I understand [the_tester.mc_title]."
    $ the_tester.change_stats(happiness = -3, obedience = 3)
    $ the_tester.clear_situational_slut("Test")
    return

label ellie_stephanie_tester_anal_finger_label(the_person):
    if the_person.vagina_available and the_person.vagina_visible:
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] strips off her bottoms as you walk over to her."
        $ scene_manager.strip_to_vagina(the_person)
        "She scoots to the edge of the medical table and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "Both her eager holes are on display for you."
    $ mc.change_locked_clarity(20)
    "You stand next to her and start to your hands up and down her thighs. She bites her lip and looks you in the eyes."
    mc.name "Alright, here we go."
    "You spit onto your fingers to lube them up, then lean forward and spit onto her puckered hole."
    "Carefully, you start to push a finger into her back door."
    if the_person.arousal_perc < 25:
        "You go nice and slow, working your finger in and out. She gasps as she tries to get used to the sensations."
        mc.name "Force yourself to relax your muscles. Just receive, and this will feel incredible."
        the_person "Ah, I think I can do that..."
        "With a bit more pressure, you are able to push your finger all the way inside her asshole."
        $ mc.change_locked_clarity(20)
    elif the_person.arousal_perc < 50:
        "Another round of spit, and you are able to push your finger all the way inside her puckered asshole."
        "She moans when you get it all the way, willing herself to relax under your touch."
        "A bit of her arousal is starting to leak from her cunt."
        $ mc.change_locked_clarity(20)
    else:
        "Your finger slides in with some effort. Her pussy lips are swollen with arousal, and some of her juices are running down between her legs."
        "When you pull your finger out, you can easily rub your finger in some and then slide your finger back inside her asshole easily."
        $ mc.change_locked_clarity(20)
    if the_person.arousal_perc >= 40:
        "You can tell her body is ready for another finger, so you quickly spit on your middle finger and then on your next stroke, you start to push them both inside her."
        "Her back arches when she feels the larger intrusion into her forbidden hole."
    if the_person.arousal_perc >= 80:
        the_person "Oh fuck, that feels so good! I can't believe it!"
        "[the_person.title] is really worked up. Without thinking, you reach with your other hand and stroke her clit with your thumb."
        the_person "Oh! Oh fuck..."
        $ mc.change_locked_clarity(20)
    if the_person.arousal_perc >= 100:
        the_person "[the_person.mc_title]! Oh my god I'm... I'm gonna cum!"
        "Wow, she must have been really pent-up! She is getting ready to orgasm already!"
        $ mc.change_locked_clarity(30)

    if the_person.arousal_perc < 20:
        the_person "Ah... go slow please... I need to warm up a bit."
        "You follow her request. You take it nice and slow, exploring her insides with one finger."
        the_person "Mmm yeah... that's it..."
        "She closes her eyes and concentrates on her feelings as her body gets aroused."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal_perc < 40:
        the_person "That's starting to feel so good... keep going..."
        "Her body is definitely responding to your intimate touches. Her cheeks are getting red and her breathing is getting deeper."
        "Your finger is sliding in and out of her puckered hole easily now. You decide it is time for another finger."
        "You pull out for a moment, spitting onto your fingers, then push two fingers inside her."
        the_person "Ahhh! Oh!"
        "Her back arches when she feels the larger intrusion into her forbidden hole."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal_perc < 60:
        the_person "Ahhh... Mmmm..."
        "[the_person.possessive_title!c] is trying to stifle her moans as they begin to grow more eager."
        "She looks up at you, and when your eyes meet, she can't stifle them anymore."
        the_person "Ahh! Oh [the_person.mc_title], that feels really good!"
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
    if the_person.arousal_perc < 80:
        the_person "Yes! Oh yes! It feels so good!"
        "[the_person.title] isn't trying to stifle her moans any more. She is actively encouraging you to keep going."
        "You reach down with your free hand and run your thumb over her exposed clit. Her hips twitch when you make contact."
        the_person "Ohhh fuck... that is so good..."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
    if the_person.arousal_perc < 100:
        $ play_moan_sound()
        "[the_person.possessive_title!c] moans and writhes beneath your skilled hands. She is moaning non-stop now."
        the_person "Yes! Oh fuck yes... I'm so close..."
        "Her words and her breathing show you just how close she is. You can tell she is in the final stretch."
        "You eagerly fingerbang her tight, puckered asshole, while you tease her clit with your thumb."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(30)
    the_person "Yes! Oh YES!"
    $ the_person.have_orgasm(force_trance = True)
    "[the_person.title]'s breathing stops as her hips start to twitch. Her whole body trembles as she begins to orgasm."
    the_person "Ah! Ahhhhh! Oh..."
    "Waves of orgasm rock her body, then begin to get smaller and smaller."
    the_person "Mmm... Ahh..."
    "She seems finished, but you give her puckered hole one last stroke and feel her whole body twitch in response."
    $ mc.change_locked_clarity(50)
    "She lays there, enjoying her post orgasm glow."
    "You remove your fingers from her and clean yourself up a bit while she recovers."
    return

label ellie_stephanie_tester_anal_sex_label(the_person):
    if the_person.vagina_available and the_person.vagina_visible:
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] strips off her bottoms as you walk over to her."
        $ scene_manager.strip_to_vagina(the_person)
        "She scoots to the edge of the medical table and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "Both her eager holes are on display for you."
    $ mc.change_locked_clarity(20)
    "You grab some lube from a shelf next to the bed, then start to apply it liberally to yourself and [the_person.title]'s puckered hole."
    "Once you are lubed up, you pull her hips to the edge of the examination bed. You put her legs over your shoulders and grab the base of your cock."
    "You move it up and down between her legs a few times, then seek out her forbidden back door."
    if the_person.has_taboo("anal_sex"):
        the_person "Oh fuck, I can't believe it... I'm about to get fucked in the ass... by my boss!"
        mc.name "Don't worry, this might be the first time, but it won't be the last time. You're going to learn to love it."
        the_person "I think I already do..."
        $ the_person.break_taboo("anal_sex")
    if the_person.arousal_perc < 25:
        "You push forward with a slow and steady pressure. Her body resists your penetration a bit as you start."
        "You hold onto her ankles and push yourself in. She gasps as the tip of your cock slips into her ass."
        "[the_person.title] grunts and gasps as you push deeper and deeper. When you finally bottom out, you hold still, giving her time to adjust to your size."
    elif the_person.arousal_perc < 50:
        "[the_person.possessive_title!c]'s ass takes a few seconds to penetrate, but you are able to slide in with minimal resistance."
        "You hold her ankles and just enjoy the sensation of having your cock sheathed in her smooth, tight back door."
    else:
        "[the_person.possessive_title!c] moans as you push your cock deep into her smooth back door. She moans when you bottom out."
        the_person "Fuck, you are so big... It feels amazing..."
        "You hold her ankles and just enjoy the sensation of having your cock sheathed in her smooth, tight back door."
        "You can feel her body twitch now and then as she adjusts to your size and gets ready to get her ass fucked raw."
    $ mc.change_locked_clarity(50)

    if the_person.arousal_perc >= 100:
        "As you start to move your hips, [the_person.title] gasps and immediately begins to cry out."
        the_person "Oh fuck! [the_person.mc_title] I'm sorry, I'm... I'm gonna cum!"
        "Wow, she must have been really pent-up! She is getting ready to orgasm already!"
        "You don't waste any time. You grab her hips with both hands and start to fuck her ass as hard as you can."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)

    if the_person.arousal_perc < 20:
        the_person "Oh god you did it... it's all the way in!"
        mc.name "It is. And doesn't it feel amazing?"
        the_person "It does... it feels so... OH!"
        "Her voice catches in her throat as you pull out and start to push back in."
        the_person "You're going to fuck me raw... aren't you?"
        mc.name "Yes. And you want me to, don't you?"
        the_person "Oh my god... yes!"
        "You start slow, but begin to fuck [the_person.possessive_title]'s incredible back door."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 40:
        the_person "It's so good... I can't believe how good this is!"
        "Her body is starting to tremble. The intense sensations of getting her puckered hole stuffed are driving her arousal higher."
        "You let go of her ankles and grab her hips. You go slow, but use the leverage to fuck her hard, with loud slaps as your hips come together."
        the_person "Fuck! Oh shit..."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 60:
        the_person "Ahhh... [the_person.mc_title]! Oh god!"
        "[the_person.possessive_title!c] is eagerly calling out to you as fuck her tight back door."
        "She looks up at you and your eyes meet, she can't stifle them anymore."
        the_person "Ahh! Oh [the_person.mc_title], fuck my ass, make me cum all over your incredible cock!"
        "You pick up the pace a little, and her moans indicate that she is loving it."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 80:
        the_person "Yes! Oh yes! It feels so good! Ohh!"
        "[the_person.title]'s moans are turning into whimpers as you sodomize her roughly."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
    if the_person.arousal_perc < 100:
        $ play_moan_sound()
        "[the_person.possessive_title!c] moans and writhes beneath you. She is moaning and whimpering non-stop now."
        the_person "Yes! My poor little ass... I'm... I'm so close!"
        "Her eyes are starting to glaze over. Her ass cheeks clap loudly as you butt fuck her with wild abandon."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(30)
    the_person "Yes! Oh YES!"
    $ the_person.have_orgasm(force_trance = True)
    "[the_person.title]'s breathing stops as her hips start to twitch. Her whole body trembles as she begins to orgasm."
    the_person "Ah! Ahhhhh! Oh..."
    "Waves of orgasm rock her body. Her raw backdoor is twitching and pulsing all around you."
    $ mc.change_arousal(20)
    menu:
        "Cum":
            $ mc.change_locked_clarity(50)
            "Feeling her cum as you sheath yourself in her bum feels too good. You let yourself go and get ready to finish."
            mc.name "Oh fuck... I'm gonna cum too!"
            "[the_person.title] reaches down and grabs your leg as you begin to cum in her bowel."
            "You can't tell if she is trying to push you off or pull you deeper. With her legs up in the air, she has zero leverage to do either."
            $ ClimaxController.manual_clarity_release(climax_type = "ass", person = the_person)
            $ the_person.cum_in_ass()
            $ scene_manager.update_actor(the_person, position = "missionary")
            "In the midst of her own orgasm, she just moans as you fill her ass up with your cum."
            if the_person.opinion.anal_creampies == -2:
                the_person "Oh my god... in my ass? I really just let you...???"
                "When you finally finish, you leave your cock anchored as deep inside her ass as it will go."
                mc.name "Fuck, that was incredible. Wasn't it amazing to get filled up like that?"
                the_person "I... I guess it was..."
                mc.name "This is just the start. You're going to learn to love it."
                the_person "I suppose we could try it again sometime..."
                $ the_person.increase_opinion_score("anal creampies")
                "You seem to have shifted her opinion on getting an anal creampie!"
            elif the_person.opinion.anal_creampies == 2:
                the_person "Yes! Oh fuck keep it deep!"
                "She is definitely pulling you deeper now."
                mc.name "Fuck, your needy asshole is so good. Take it you little butt slut!"
                the_person "I am! Oh [the_person.mc_title] give it to me!"
                "When you finally finish, you leave your cock stuffed as deep inside her ass as it will go."
                the_person "Oh fuck... that was amazing..."
            else:
                the_person "Oh my god! I can feel it! I can feel your cum splashing inside my ass!"
                "Her face is blissful as you fill her up. She is really loving it."
                "When you finally finish, you leave your cock deep inside her bowels."
                the_person "I didn't know it could feel so good like that! That was incredible!"
                mc.name "This is just the start. You're going to learn to love it."
                the_person "I already do! Maybe you should just cum inside my ass every time from now on..."
                $ the_person.increase_opinion_score("anal creampies")
                "You seem to have shifted her opinion on getting an anal creampie!"
            "When you are both finished, you slowly pull out of her. A little bit of cum is trickling down between her legs."
        "Keep yourself from cumming" if mc.arousal_perc < 100 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
            "Somehow, against all odds, you dig deep and keep yourself from cumming."
            "When she finishes, you slowly pull out of her."
        "Keep yourself from cumming\n{menu_red}Too aroused{/menu_red} (disabled)" if mc.arousal_perc >= 100 and not perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
            pass

    $ mc.change_locked_clarity(50)
    "She lays there, enjoying her post orgasm glow."
    "You clean yourself up a bit while she recovers."
    return

label ellie_stephanie_tester_breeding_sex_label(the_person):
    if the_person.vagina_available and the_person.vagina_visible:
        "[the_person.title] scoots to the edge of the medical bed and spreads her legs for you as you walk over to her."
    else:
        "[the_person.title] strips off her bottoms as you walk over to her."
        $ scene_manager.strip_to_vagina(the_person)
        "She scoots to the edge of the medical bed and spreads her legs for you."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You look down at [the_person.title]. Her legs are wide open, beckoning you to enter her bare and fill her up with your seed."
    $ mc.change_locked_clarity(30)
    "You grab her hips with both hands and pull her ass to the edge of the bed, then take your cock in one hand."
    "You line it up with her pussy and you get ready to penetrate her."
    if the_person.has_taboo("vaginal_sex"):
        the_person "Oh God, I can't believe it... I'm about to get fucked by my boss!"
        mc.name "Don't worry, this might be the first time, but it won't be the last time. You're going to learn to love it."
        the_person "I think I already do..."
        $ the_person.break_taboo("vaginal_sex")
        $ mc.change_locked_clarity(50)
    if the_person.arousal_perc < 25:
        "You push forward with a slow and steady pressure. You slide inside her cunt with a bit of pressure."
        "You let go of the base of your cock and grab her ankles, spreading them wide apart as you push deeper inside of her."
        "[the_person.title] moans and gasps as you push deeper and deeper. When you finally bottom out, you hold her still, giving her time to adjust to your size."
    elif the_person.arousal_perc < 50:
        "You push forward and slide easily inside of [the_person.possessive_title]'s wet cunt."
        "You grab her ankles and spread them wide as you push all the way inside of her."
        the_person "Mmmmm!!! Ahhh..."
        "She moans and gasps when you bottom out."
    else:
        "[the_person.possessive_title!c] moans as you push your cock easily into her soaking wet cunt."
        the_person "Fuck, you are so big... It feels amazing..."
        "You grab her ankles and spread them wide as you push all the way inside of her."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(10)

    if the_person.arousal_perc >= 100:
        "As you start to move your hips, [the_person.title] gasps and immediately begins to cry out."
        the_person "Oh fuck! [the_person.mc_title] I'm sorry, I'm... I'm gonna cum!"
        "Wow, she must have been really pent-up! She is getting ready to orgasm already!"
        "You don't waste any time. You grab her hips with both hands and start to fuck her as hard as you can."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    elif the_person.arousal_perc >= 60:
        "As you start to move your hips, [the_person.title] moans loudly."
        the_person "Oh fuck... [the_person.mc_title], no need to be gentle, fuck me good!"
        mc.name "Don't worry, I intend to."
        "Sensing that she doesn't need any warmup time, you set a vigorous pace and begin to pump your hips."
        "Your cock is sliding rapidly in and out of her unprotected cunt."
        "She lets out a pleasured yelp when you pick her ass up off the exam table a couple inches, taking away any leverage she might have."

    if the_person.arousal_perc < 20:
        the_person "Oh god that's exactly what I needed..."
        "You looks down between her legs, watching as your bare cock pulls almost all the way, then moans as it pushes back in."
        the_person "I wasn't even paying attention... you're bare... right?"
        mc.name "Yes. There is nothing protecting you from what I'm about to do to you."
        the_person "Oh my god... yes!"
        "You start slow, but begin to fuck [the_person.possessive_title]."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 40:
        the_person "It's so good... It's like I can feel your manhood going deeper and deeper each thrust..."
        "Her body is starting to tremble. The intense sensations of getting fucked combine with the nano bots to drive irresistable urges."
        the_person "You going to cum inside me... right?"
        mc.name "There is nothing you can do to stop me from filling you with cum if I decide to."
        "To make the point, you suddenly lift her ass an inch or two off the exam table, taking away any leverage she might have been able to manage."
        the_person "Fuck! Oh shit..."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 60:
        the_person "Ahhh... [the_person.mc_title]! Oh god!"
        "[the_person.possessive_title!c] is eagerly calling out to you as fuck her."
        "She looks up at you and your eyes meet, she can't stifle her urges anymore."
        the_person "Ahh! Oh [the_person.mc_title], fuck me! Make me cum and then flood me with your cum too!"
        if the_person.knows_pregnant:
            the_person "Shower my baby with your virile cum!"
        else:
            the_person "Cum deep and knock me up!"
        "You pick up the pace a little, and her moans indicate that she is loving it."
        $ the_person.change_arousal (20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 80:
        the_person "Yes! Oh yes! It feels so good! Ohh!"
        "[the_person.title]'s moans are turning into whimpers as you fuck her roughly."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(20)
    if the_person.arousal_perc < 100:
        $ play_moan_sound()
        "[the_person.possessive_title!c] moans and writhes beneath you. She is moaning and whimpering non-stop now."
        the_person "Yes! I'm... I'm so close! Cum with me!"
        "Her eyes are starting to glaze over. Her ass cheeks clap loudly as you fuck her with wild abandon."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(20)

    "She is getting ready to cum."
    menu:
        "Cum":
            $ mc.change_locked_clarity(50)
            "You let yourself go and get ready to finish."
            mc.name "Oh fuck... I'm gonna cum too!"
            "Suddenly, with a strength you didn't know she had, her ankles pull from your grasp."
            "Her legs wrap around you and pull you forward, causing you to fall forward directly on top of her."
            mc.name "Wha! OH fuck..."
            "Her heels dig in to your ass as she clings to you with her arms."
            the_person "Don't you even think about pulling out! OH! OH FUCK!"
            "Her body begins to tremble in orgasm but her grip is too strong for you to overcome."
            $ the_person.have_orgasm(force_trance = True)
            "You weren't really considering pulling out anyway so you let yourself go, joining her in orgasm as you start to cum deep inside of her."
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
            $ the_person.cum_in_vagina()
            $ scene_manager.update_actor(the_person, position = "missionary")
            "In the midst of her own orgasm, she just moans as your orgasm begins."
            the_person "YES! Oh my God it's so warm.... YESSSS!"
            "[the_person.possessive_title!c]'s body is trembling beneath you as she accepts pulse after pulse of your cum."
            "Even after you finish, she clings to you for several more seconds before relaxing her embrace."
            "You push yourself up with your arms and look down at her."
            if the_person.opinion.creampies == -2:
                the_person "Wow so... that just happened... didn't it..."
                "You slowly pull out of her pussy. Once out, a short stream of your cum suddenly gushes out and slides down onto the exam table."
                the_person "Oh god... yeah... I felt that..."
                mc.name "Fuck, that was incredible. Wasn't it amazing to get filled up like that?"
                the_person "I... I guess it was pretty hot..."
                mc.name "This is just the start. You're going to learn to love it."
                the_person "I suppose I wouldn't necessarily hate it..."
                $ the_person.increase_opinion_score("creampies")
                "You seem to have shifted her opinion on getting a creampie!"
            elif the_person.opinion.creampies == 2:
                the_person "Yes! Oh fuck that was so deep!"
                "You slowly pull out of her pussy. Once out, a short stream of your cum suddenly gushes out and slides down onto the exam table."
                the_person "Mmmm... I wish it would all stay inside, but there's still so much, I can feel it..."
                mc.name "Fuck, that was incredible. You need to take it easy though, I was going to creampie you, no need to get so clingy."
                the_person "Oh! I'm sorry [the_person.mc_title], I had this sudden fear that you were about to pull out and waste it all cumming on my tits or something..."
                mc.name "It's okay, I understand."
                "She takes a deep breath."
                the_person "Thank you..."
                $ the_person.change_obedience(2, 180)
            else:
                the_person "Oh my god! I'm sorry, I don't know what came over me..."
                "You slowly pull out of her pussy. Once out, a short stream of your cum suddenly gushes out and slides down onto the exam table."
                the_person "Mmmfff... I can't believe I just did that..."
                mc.name "It was probably the serum, there are some known side effects."
                the_person "Mmm, well I think the side effects of this one are nice..."
                the_person "Maybe we could do that again sometime, without the test bed?"
                $ the_person.increase_opinion_score("creampies")
                "You seem to have shifted her opinion on getting a creampie!"
            "You get up and carefully step down from the exam table."
        "Keep yourself from cumming" if mc.arousal_perc < 100 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
            the_person "Yes! Oh YES!"
            $ the_person.have_orgasm(force_trance = True)
            "[the_person.title]'s breathing stops as her hips start to twitch. Her whole body trembles as she begins to orgasm."
            the_person "Ah! Ahhhhh! Oh..."
            "Waves of orgasm rock her body. Her pussy is twitching and pulsing all around you."
            $ mc.change_arousal(20)
            "Somehow, against all odds, you dig deep and keep yourself from cumming."
            "When her orgasm subsides, she looks up at you."
            the_person "Ahhh, that was nice, now it's your turn!"
            mc.name "I'm sorry, I hope I took the edge off, but I can't cum inside you."
            the_person "You... what!?! You can't be serious..."
            "Before she can react, you quickly set her ass on the table and pull back. She whimpers when your cock slides out of her."
            the_person "[the_person.mc_title], you don't have to... you can still..."
            mc.name "Shhh, it's okay [the_person.title]. This is for the better."
            $ the_person.change_obedience(5, 180)
            "She can't believe it, but quietly accepts your decision."
        "Keep yourself from cumming\n{menu_red}Too aroused{/menu_red} (disabled)" if mc.arousal_perc >= 100 and not perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
            pass

    $ mc.change_locked_clarity(50)
    "She lays there, enjoying her post orgasm glow."
    "You clean yourself up a bit while she recovers."
    return

label ellie_stephanie_tester_blowjob_cum_label(the_person):
    pass
    return

label ellie_stephanie_tester_public_sex_label(the_person, the_researcher, the_tester):
    pass
    return

init 5 python:
    def head_researcher_needy_tester_response(the_person, program_name):
        if the_person.sluttiness < 20:
            pass
            # the_person "[the_person.mc_title], this seems like a bad idea. Getting involved like that could invalidate our data!"
        elif the_person.sluttiness < 40:
            pass
        return
