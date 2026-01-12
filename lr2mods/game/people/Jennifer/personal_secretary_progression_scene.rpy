#This file contains all labels associated with the personal secretary's progression scene.
#The personal secretary monitors the MC and if his lust gets above a certain value she initiates sex
#Sex acts begin with handjob and then steadily ramp up to MC banging her on his desk
#These scenes will also unlock the Personal Secretary's general willingness to do those acts, so she can be called on in other scenes
#Generally, a scene that might level MC sexually frustrated will be able to check and see if the personal secretary is willing to help out.
#This scene can be triggered once a day if MC's lust is above a specific amount

label personal_secretary_prog_scene_action_label():  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: personal_secretary_prog_scene_action_label():

    # "Test, is this working"
    $ mc.business.set_event_day("secretary_last_relief_day")
    $ personal_secretary_prog_scene.call_scene([mc.business.personal_secretary])
    return

label personal_secretary_prog_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ mc.arousal = 0
    if not mc.is_at(ceo_office):
        $ mc.change_location(ceo_office)
        "There are so many details to take care of, so you go to your office."

    #Use stages to the event to determine how many options we start with. Similar to the modelling action.
    "You sit down at your desk, ready to get some work done."
    "However, as you start to answer some emails, your mind starts to drift away from your tasks."
    "You've been letting yourself flirt and fantasize about your employees a lot lately."
    "You mind drifts into daydreaming about bending you employees over their desks or getting the down on their knees."
    $ mc.change_locked_clarity(30)
    "Your mind gets lost as you daydream about debauchery in the office."
    the_person "[the_person.mc_title]? [the_person.mc_title]???"
    "Mmm yeah [the_person.fname], take it you little slut..."
    the_person "[the_person.mc_title]? Are you okay?"
    $ the_person.draw_person()
    "Your mind suddenly snaps back. [the_person.title] is standing in front of you, looking at you expectantly."
    mc.name "Yes... I'm fine... I was just distracted..."
    the_person "Distracted? By what? Is there something I can help you with?"
    "You look at [the_person.possessive_title]. She recently started as your personal secretary."
    "What is the point of having a personal secretary if you can't have a little discretionary fun?"
    call perk_time_of_need_story_label() from _time_of_need_personal_secretary_prog_intro_01
    "You decide to see if you can get her to help relieve your distraction. You'll try and play it smooth at first though..."
    mc.name "Well... it is kind of a personal thing... it isn't business related..."
    "You act like you are trying to consider it for a moment."
    mc.name "I... maybe... no. I couldn't ask you to help. Sorry!"
    the_person "[the_person.mc_title], I'm your *personal* secretary. I assumed that you would need help now and then with your personal business too!"
    mc.name "Ah yes, but this goes a little beyond that I'm afraid..."
    "She sighs."
    the_person "Well, why don't you just tell me what you need, and if I can't help, then maybe I could find someone who can?"
    mc.name "Ah well, it isn't that simple... you see..."
    "You pretend to hesitate for a moment, as if you are still undecided if you are going to say it or not."
    mc.name "The truth is, I'm having trouble concentrating. I recently had an intimate encounter with someone that has left me feeling a bit... needy."
    if the_person == mom:
        the_person "Oh! I... I see what the issue is. I'm sorry, I didn't even think about that!"
    else:
        the_person "Ah, so it is THAT kind of problem..."
    if the_person.effective_sluttiness() >= 40 and the_person == mom:
        the_person "Well, I guess I'll have to help you with that then!"
        the_person "Isn't that what a secretary is for?"
    elif the_person.effective_sluttiness() >= 40: #No issues with helping out.
        the_person "Well that is an easy fix. I can take care of that for you!"
    else:
        the_person "Thank you for being honest with me. That certainly is an interesting problem."
        if the_person.has_taboo("touching_penis") and the_person == mom:
            the_person "I think I knew that being your secretary might involve problems like this."
            the_person "I know we've never really done this before but, I could help you... with that?"
        elif the_person.has_taboo("touching_penis"):  #Different dialogue for mommy here
            the_person "I know I've never really done this for you before but, if you were really having an issue, I could help you out?"
            the_person "I know you're my boss, but I really don't mind!"
    the_person "Would you be okay with a quick handjob? Would that help you concentrate and get back to work?"
    mc.name "That would be great. I would really appreciate it."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] starts to walk around your desk."
    the_person "Can you take it out for me?"
    mc.name "Sure..."
    $ the_person.break_taboo("touching_penis")
    # if the_person == mom:
    #     the_person "Well, it has been a change for sure. I don't miss my old boss one bit!"
    #     the_person "And being here and seeing all the things you are doing, it makes me so proud of you."
    # else:
    #     the_person "Well, it was different at first, being out of the cubicles. The office up here is much nicer!"
    #     the_person "I do kind of miss being down with the other girls in the general office space, but I take a break now and then and still have the chance to socialize."
    #     the_person "Overall, I think I like the change."
    # mc.name "Good, I'm glad to hear it."
    # mc.name "As you are aware, one of the reasons I asked you to move up here is to be my personal secretary."
    # mc.name "Once in a while I may have specific tasks that will require your... discretion."
    # if the_person.sluttiness >= 60:
    #     the_person "Ahh, I was hoping there would be some extra benefits to being up here."
    #     "[the_person.possessive_title!c] gives you a sly wink."
    # elif the_person.sluttiness >= 20:
    #     the_person "Ahh, I kinda knew something like this was coming."
    #     the_person "To be honest though... I don't think I mind it."
    # else:
    #     the_person "Oh? Like... what kind of tasks?"

    # "You stand up and walk around the desk. She looks up at your from her chair."
    # mc.name "Let's start with the basics. Use your hand for a bit."
    "You unzip your pants and pull out your cock."
    "She reaches out and gives your erection a few soft strokes."
    mc.name "Mmm, your hand feels great..."
    if the_person.sluttiness >= 60:
        "[the_person.possessive_title!c] licks her lips and looks at you."
        the_person "Just my hand? I can go along with that for now..."
    elif the_person.sluttiness >= 20:
        the_person "Ahh, a handjob? An innocent enough start I suppose."
    else:
        the_person "Oh my god... I... okay..."
        "She looks at you."
        the_person "I know you have... needs... I'll do what I have to do to help!"

    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] slips onto her knees. She starts to run her hand up and down your cock."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    the_person "Like this, [the_person.mc_title]? Is this what you need your secretary to do?"
    "Her soft hand is gliding up and down your erection. You sigh as you relax and just let her work."
    #Handjob defaults to being available, so we don't need to unlock anything here.
    #Next, check to see if she adds her tits without being asked.
    $ final_outcome_choice = "Handjob"
    if the_person.is_willing(tit_fuck) and the_person.has_large_tits and the_person.sluttiness > 20:
        if not the_person.tits_available:
            the_person "Mmm... maybe this will help..."
            "You watch as [the_person.title] pulls out her tits."
            $ the_person.strip_to_tits(position = "blowjob")
        the_person "Maybe [the_person.mc_title] would like to slide his cock between his secretary's tits for a bit too?"
        "She stretches her body up a little bit, until your cock is up against her cleavage, but she doesn't go so far as you slip your dick between them..."
        $ final_outcome_choice = "Titfuck"
    elif the_person.sluttiness > 20 or the_person.obedience > 120:  #She should be obedient enough.
        if not the_person.tits_available:
            mc.name "Why don't you get your tits out for me too."
            if the_person.sluttiness > 40:
                the_person "Oh, you want to see my big tits wobble around while I stroke it, do you? I guess that would be okay."
            else:
                the_person "Oh! I... I guess that would be okay..."
            "You watch as [the_person.title] pulls out her tits."
            $ the_person.strip_to_tits(position = "blowjob")
        if the_person.has_large_tits:
            "Her hand feels good, but you can't help but look down and think about sliding your cock between her big tits too..."
            menu:
                "Fuck her tits":
                    mc.name "Mmm, that feels good, but I'm ready to take it another step."
                    "You reach down and fondle her tits. They feel soft and hot in your hands."
                    "You give them several gropes and then give her nipples a little pinch. You pull her up gently by the nipples, and she shifts her weight up until her chest is leve with your groin."
                    $ final_outcome_choice = "Titfuck"
                "Enjoy her as is.":
                    pass
        elif the_person.is_willing(blowjob) and the_person.sluttiness >= 40:
            $ final_outcome_choice = "Blowjob"
        # Use this if a girl is slutty enough to give a so we don't want to assume a handjob.
    if final_outcome_choice == "Handjob":
        "You decide that for today, you will just let her stroke you with her hand."
        call fuck_person(the_person, start_position = handjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_sec_intro_handjob_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "Satisfied with your orgasm, you take a moment and put your cock away."
    if final_outcome_choice == "Titfuck":
        "You reach down and put your hands on her tits. You pull them apart a bit, then push your cock into her cleavage."
        "You put your hands on the sides, squishing her warm, soft breasts around your erection."
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(30)
        "[the_person.possessive_title!c] is just looking up at you as you start to fuck her tits."
        the_person "Does that feel good, [the_person.mc_title]? To have your secretary's tits bouncing up and down your cock?"
        mc.name "Mmm, damn right. It is going to be nice using these puppies anytime I want in here."
        $ the_person.change_arousal(15)
        $ the_person.change_slut(1, 60)
        "You let yourself enjoy it as she takes over, bouncing her chest up and down."
        $ personal_secretary_prog_scene.scene_unlock_list.append(1) #Unlock tit fucks anytime.
        if the_person.is_willing(blowjob) and the_person.sluttiness >= 60:  #Next, determine if she initiates a blowjob
            $ final_outcome_choice = "Blowjob"
            "She is starting to get out of breath, while she keeps looking up at you."
            the_person "Fuck it feels so hot..."
            "She pulls away for a moment."
            the_person "We both know where this is going... right? Is it time for me to taste it? Please?"
            "DAMN. You chose the right girl to be your secretary."
            "Instead of of answering, you put your hand on the back of her head, and gently urge her face down toward your crotch."
            the_person "Mmm... thank god..."
        elif the_person.is_willing(blowjob):
            "You run your hands through her hair, as she works you with her sweater puppies."
            "It feels good... but you think it might be time to move on to one of her warm, wet holes..."
            menu:
                "Move to a blowjob":
                    mc.name "Mmm, that is such a good warm up. I think it is time to move on to something a little... wetter..."
                    the_person "Oh? What do you have in mind?"
                    "You put your hand on the back of her head, and gently urge it down toward your crotch."
                    the_person "Ahhh... I get it now..."
                    $ final_outcome_choice = "Blowjob"
                "Enjoy her tits.":
                    pass
    if final_outcome_choice == "Titfuck":
        "You decide that for today, you will just enjoy her tits."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_sec_intro_titfuck_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "Satisfied with your orgasm, you take a moment and put your cock away."
            "Your cum is dripping down [the_person.possessive_title]."
    if final_outcome_choice == "Blowjob":
        "[the_person.possessive_title!c] lets you guide her face closer until your erection rests against her chin, lips, and nose."
        "She breathes in through her nose then lets out a sigh. She opens her mouth and begins to lick up and down the length."
        "Her mouth opens and then her wonderful lips close over the tip of your erection."
        "Her tongue glides in sensual circles, licking up your precum, before her head begins to bob up and down as she sucks on your cock."
        $ mc.change_arousal(20)
        $ mc.change_locked_clarity(40)
        "You let out a growling moan as [the_person.possessive_title] begins to work you over with her warm, wet mouth."
        "Her lips and tongue stimulate you in all kinds of exciting ways for several seconds."
        "She pulls back and looks up at you."
        the_person "So, [the_person.mc_title], are you going to have your slutty secretary in here often? On her knees, servicing her boss whenever he pleases?"
        mc.name "Of course. I think you'll fit nicely beneath my desk, servicing your boss while he accomplishes his meetings and work."
        $ the_person.change_arousal(15)
        $ the_person.change_slut(1, 70)
        the_person "Fuuuuck... that sounds hot..."
        $ personal_secretary_prog_scene.scene_unlock_list.append(2) #Unlock BJs anytime.
        "She opens her mouth and gets back to work with a renewed vigour. Her lips and tongue are working your erection with a renewed eagerness."
        if the_person.is_willing(standing_doggy) and the_person.sluttiness >= 70:   #We don't force her to do this, but if she is willing, leave the option to fuck her.
            "[the_person.possessive_title!c]'s mouth is warm and inviting, but you think you can push things one more step..."
            menu:
                "Bend her over your desk":
                    $ final_outcome_choice = "Fuck"
                    "You put your hand on her head again, but this time you pull her away from your groin."
                    "Your cock escapes her mouth with a loud smack, and she looks up at you a bit confused."
                    mc.name "Alright. Your boss is ready to finish this."
                    $ the_person.draw_person(position = "stand3")
                    "You pull her up to her feet."
                    the_person "I don't... what do you mean?"
                    "You turn her around..."
                    $ the_person.draw_person(position = "back_peek")
                    the_person "I'm... are... are you?"
                    "You bend her over your desk."
                    $ the_person.draw_person(position = "standing_doggy")
                    the_person "I... oh my god..."
                "Enjoy her mouth":
                    pass
    if final_outcome_choice == "Blowjob":
        "You just watch as [the_person.possessive_title] services you with her mouth."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_sec_intro_blowjob_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "Satisfied with your orgasm, you take a moment and put your cock away."
    if final_outcome_choice == "Fuck":
        if the_person.vagina_available:
            "You run your fingers up and down her slit. She understands now what is about to happen."
        else:
            "You quickly strip off her bottoms."
            $ the_person.strip_to_vagina(position = "standing_doggy")
            "Once she is fully exposed, you run your fingers up and down her slit. She understands now what is about to happen."
        if the_person.wants_condom():
            the_person "Oh god... wait! I... can you put on a condom please?"
            the_person "I'm not saying no... I just need you to wrap it up!"
            "You consider pushing the issue, but you decide with it being the first time you're taking her in your office that you should just comply for now."
            mc.name "Sure, good thing I keep some in here..."
            "You open up your desk and pull out a pack of condoms. You pull one out, open it, and roll it down your cock."
            $ mc.condom = True
            $ the_person.change_love(1)
            $ the_person.change_obedience(2)
        elif the_person.wants_creampie:
            the_person "Oh god, you can just put it in... you don't need a condom or anything... [the_person.mc_title]..."
            mc.name "I'm sorry, what was that? Were you making a request?"
            the_person "Oh fuck... [the_person.mc_title], can you fuck your slutty secretary raw? I want to feel everything!"
            the_person "You can cum wherever you want boss! My body is yours to use..."
            mc.name "You're damn right it is."
        else:
            the_person "Did... did you want to put on a condom?"
            the_person "I mean, you don't have to, but if you don't... you should probably pull out!"
            menu:
                "Fuck her Raw":
                    mc.name "Nah, if you're going to be my slutty little secretary, you're going to need to get used to taking my cock raw."
                    the_person "Oh... fuck... mmmm"
                "Put on Condom":
                    mc.name "I might pull out and cum all over your ass... but I haven't decided yet."
                    mc.name "I'll put one on... for now."
                    the_person "Okay!"
                    "You open up your desk and pull out a pack of condoms. You pull one out, open it, and roll it down your cock."
                    $ mc.condom = True
        "You put your hands on [the_person.possessive_title]'s hips. You slide your cock up and down her cunt a few times, getting the tip lubricated."
        "With gentle pressure, you press your hips forward. Your cock slides into her pussy easily."
        $ the_person.change_arousal(25)

        the_person "Oh my god... oh FUCK... it feels so good when it goes in...!"
        "A moment later, you are bottomed out. Your secretary's hips make an enticing view, exposed and pinned to your desk."
        "You give your hips a few tentative strokes. She moans with each stroke."
        the_person "Do you think I'll spend more time under your desk? Or bent over it?"
        $ personal_secretary_prog_scene.scene_unlock_list.append(3) #Fuck her anytime.
        mc.name "Well, between those two specifically, probably under my desk."
        mc.name "I might fuck you on the couch, or have you sit on my lap while I'm in my chair, or up against the window looking down on the employee lot."
        $ the_person.change_slut(1, 80)
        $ the_person.change_arousal(10)
        "[the_person.possessive_title!c] just moans and pushes back against you. You grab her hips and begin fucking her."
        call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_sec_intro_doggy_01
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.possessive_title!c] is left, still bent over your desk, out of breath from her orgasm."
        if the_report.get("guy orgasms", 0) > 0:
            "You quickly clean yourself up and put your cock away."

    "Eventually, she stands up and turns to you."
    $ the_person.draw_person(position = the_person.idle_pose)
    mc.name "Thank you [the_person.title]. That was just what I needed."
    the_person "Of course. I mean, as your secretary, I kind of assumed something like this would happen eventually."
    "She thinks about it for a moment."
    the_person "Would you like for me to do this again, when I notice that you are... distracted... again?"
    "You think about it for a moment."
    mc.name "That sounds excellent [the_person.title]. However only initiate when I'm..."
    menu:
        "... distracted. \n{menu_green}Lust > 25%%{/menu_green}":
            mc.name "I still need to have time to accomplish all of my regular work tasks."
            the_person "I understand sir."
            $ the_person.event_triggers_dict["ps_lust_tier"] = 2
        "... very distracted. \n{menu_green}Lust > 50%%{/menu_green}":
            mc.name "Just when you see that my work is starting to suffer."
            the_person "Of course sir."
            $ the_person.event_triggers_dict["ps_lust_tier"] = 3
        "... extremely distracted. \n{menu_green}Lust > 90%%{/menu_green}":
            mc.name "Only when you see it is almost impossible for me to get any work accomplished."
            the_person "Sounds good, sir."
            $ the_person.event_triggers_dict["ps_lust_tier"] = 4
    the_person "Is there anything else?"
    mc.name "Do me a favour, and make sure that your desk is stocked with supplies for when we get done with these sessions, like wipes and paper towels."
    the_person "Yes [the_person.mc_title]."
    mc.name "... and keep my desk stocked too, while you're at it."
    the_person "Of course [the_person.mc_title]."
    "She continues to stand there. You realise she is waiting for you to officially dismiss her."
    mc.name "Alright, that is all for now. Get back to work."
    the_person "Yes sir!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and leaves your office, closing the door on her way out."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "Your personal secretary will now offer to relieve your sexual urges at high lust scores when you work in your office."
    "To trigger the event, just work anywhere in your business with lust above your selected level and she will offer to help out."
    "You can change this threshold by talking to her again at work."
    $ del final_outcome_choice
    return

label personal_secretary_prog_scene_choice_label(the_group):
    $ the_person = the_group[0]
    if not mc.is_at(ceo_office):
        $ mc.change_location(ceo_office)
        "There is a lot to do, so you go to your office to get some work done."
    "There is a knock on your office door."
    mc.name "Come in."
    $ the_person.draw_person(position = "stand4")
    "It is your personal secretary. She closes the door and locks it behind her."
    if mc.lust_tier == 2:
        the_person "Hello [the_person.mc_title]. I noticed when you walked past my desk into your office you seemed a little distracted..."
    elif mc.lust_tier == 3:
        the_person "Hello [the_person.mc_title]. When you walked by my desk to your office, I umm... couldn't help but notice that you seemed a little excited..."
    else:
        the_person "Hello [the_person.mc_title]. I couldn't help but noticing when you walked by my desk that you had a raging hard on."
    "Perfect timing. You gave [the_person.possessive_title] permission to stop in when she notices you distracted like this."
    if personal_secretary_prog_scene.progression_available:
        the_person "I wouldn't mind at all. Maybe we could even mix things up a little bit today..."
    "Do you want to have some fun with her?"
    menu:
        "Get relief {image=progress_token_small}" if personal_secretary_prog_scene.progression_available:
            "Something about the look in her eyes tells you it is a good day to accept."
            mc.name "I could definitely use some relief today."
            return True
        "Get relief" if not personal_secretary_prog_scene.progression_available:
            mc.name "I could definitely use some relief today."
            return True
        "Not Now":
            mc.name "I'm sorry, I have a lot on my plate to get done right now. I'll manage."
            the_person "Ahh, okay. I'll see myself out then."
            return False
    return False

label personal_secretary_prog_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    "Alright [the_person.mc_title], I will leave you to your work."
    return

label personal_secretary_prog_scene_multiple_choice_scene(the_group):
    $ the_person = the_group[0]
    "[the_person.possessive_title!c] nods, her eyes never leaving yours. Her voice gets a little husky when she responds."
    if the_person == mom:
        the_person "I can give you what you need, [the_person.mc_title]. Just like I always do."
    else:
        the_person "Mmm... How can your secretary make you feel good today, sir?"
    menu:
        "Handjob" if 0 in personal_secretary_prog_scene.scene_unlock_list:
            return 0
        "Tit Fuck" if 1 in personal_secretary_prog_scene.scene_unlock_list and the_person.has_large_tits:
            mc.name "I want to feel those incredible tits of yours wrapped around my cock again."
            return 1
        "Blowjob" if 2 in personal_secretary_prog_scene.scene_unlock_list:
            mc.name "Come here and put that talented mouth of yours to work."
            return 2
        "Cowgirl" if 3 in personal_secretary_prog_scene.scene_unlock_list:
            mc.name "Come here and show me your horse riding skills."
            return 3
        "Bent Over Desk" if 4 in personal_secretary_prog_scene.scene_unlock_list:
            mc.name "I think I'll just take you here, on my desk."
            return 4
        "Anal Lapdance" if 5 in personal_secretary_prog_scene.scene_unlock_list:
            return 5
        "Anal Over Desk" if 6 in personal_secretary_prog_scene.scene_unlock_list:
            return 6
        "Breed Her" if 7 in personal_secretary_prog_scene.scene_unlock_list:
            return 7
        "Anal Fetish Scene" if 8 in personal_secretary_prog_scene.scene_unlock_list:
            return 8
        # "Surprise me" if len(personal_secretary_prog_scene.scene_unlock_list) > 1:
        #     the_person "Mmmm, okay"
        #     $ mc.change_arousal(5)
        #     $ the_person.change_stats(happiness = 5, obedience = 3)
        #     return renpy.random.choice(personal_secretary_prog_scene.scene_unlock_list)
    return

#Intro Scene
label personal_secretary_prog_scene_intro_0(the_group):
    $ the_person = the_group[0]
    if not mc.is_at(ceo_office):
        $ mc.change_location(ceo_office)
        "There are so many details to take care of, so you go to your office."

    # Because this is a multiple choice scene, we only need one intro.
    "You sit down at your desk, ready to accomplish some work tasks."
    "You log on to your computer. Your thoughts start to stray to some of your employees."
    "For a moment, you don't even realise your computer has finished logging on, lost in your thoughts."
    if mc.lust_tier == 2:
        "You sigh. You don't really feel like working right now, but you definitely need to get some things done."
    elif mc.lust_tier == 3:
        "Your brain struggles to engage with the computer. Your mind keeps going back to the female employees working in the building..."
    else:
        "Your brain refuses to engage with the computer in front of you. Maybe you should call someone in to your office for a little fun."
    return


#Transition scenes
# Last line before the transition:
# mc.name "I could definitely use some relief today."
label personal_secretary_prog_trans_scene_0(the_group):
    #This should never get called since HJs are opened from the start
    $ the_person = the_group[0]
    return

label personal_secretary_prog_trans_scene_1(the_group):
    $ the_person = the_group[0]
    "You stand up and walk around your desk."
    mc.name "I have an idea for how we can mix it up."
    $ the_person.draw_person(position = "back_peek")
    "You walk around behind [the_person.possessive_title]. You put your hands on her hips, then run them to her front, along her stomach, slowly working upwards."
    "She shudders at your touch."
    $ the_person.change_arousal(10)
    mc.name "May I?"
    the_person "Of course..."
    "You bring your hands up to [the_person.title]'s tits. She gasps and leans back against you a bit, grinding her ass against your erection as you begin to grope her."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(10)
    $ the_person.change_slut(1, 40)
    if the_person.tits_available and the_person.tits_visible:
        "The hot flesh of her exposed chest feels heavy in your hands."
    else:
        "After several seconds of groping, you start to strip off her top..."
        $ the_person.strip_to_tits(prefer_half_off = False, position = "back_peek")
        "She lets out an appreciative moan when your hands return to her naked chest."
    "Several seconds go by while you enjoy feeling up your secretary."
    "You lean forward and whisper into her ear."
    mc.name "I want to feel my cock between your fantastic tits."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(10)
    $ the_person.change_slut(2, 40)
    "You feel a shudder run through her."
    if the_person.effective_sluttiness() >= 40: #Eager
        the_person "Ohhh, me too..."
    elif the_person.obedience > 130:
        the_person "If you want me to, sir..."
    else:
        the_person "If... If that's what you want..."
    $ the_person.draw_person(position = "stand4")
    the_person "Go sit down... I'll take care of you there."
    "Damn, that's a good idea. You return to your side of the desk and sit in your chair. [the_person.title] follows you."
    "You swivel it to the side while [the_person.possessive_title] gets down on her knees."
    $ the_person.draw_person(position = "blowjob")
    return

label personal_secretary_prog_trans_scene_2(the_group):
    $ the_person = the_group[0]
    mc.name "Come here, I have an idea for how we can mix it up."
    "She obediently starts to walk around your desk."
    $ the_person.change_obedience(1)
    if the_person.tits_available and the_person.tits_visible:
        mc.name "Get on your knees."
        "She gives a little gasp as you swivel your office chair to the side, but obediently obeys."

    else:
        mc.name "Get on your knees, and get your tits out."
        "She gives a little gasp as you swivel your office chair to the side, but obediently obeys."
        $ the_person.strip_to_tits(prefer_half_off = False, position = "blowjob")
    $ the_person.draw_person(position = "blowjob")
    the_person "Okay... what now sir?"
    mc.name "Take my cock out."
    the_person "Yes sir..."
    "She reaches up and quickly unbuttons your pants and then pulls them and your underwear down."
    "Your cock springs free. She gasps, licks her lips then looks up at you."
    the_person "Okay... what now?"
    "Your run your hand through her hair."
    mc.name "[the_person.fname]... I think we both know what is about to happen."
    if 1 in personal_secretary_prog_scene.scene_unlock_list:
        mc.name "As much as I love hand jobs or fucking your tits, I need something more than that today."
    else:
        mc.name "As much as I love hand jobs, I need something more than that today."
    mc.name "Namely, I need one of your warm, wet holes to fill."
    $ the_person.change_slut(2, 60)
    if the_person == mom and not the_person.event_triggers_dict.get("oral_revisit_complete", False):
        the_person "You can't be serious [the_person.mc_title]... a blowjob?"
        the_person "I know we've been having some fun but..."
        mc.name "But here you are, on your knees next to you boss's desk. Now be a good secretary and put that mouth of yours to work."
        "She looks up at you, and then something in her mind clicks. She takes a second in her brain to shift your relationship from mother-son to boss-secretary."
    elif not the_person.is_willing(blowjob):
        the_person "I... I wouldn't normally do something like that..."
        mc.name "But here you are, on your knees next to you boss's desk. Now be a good secretary and put that mouth of yours to work."
    else:
        the_person "Mmm, you make me feel like such a slut. I love it!"
        mc.name "Good, now be my slutty secretary and put that mouth of yours to work."
    the_person "Yes sir... I'll take care of you!"
    "She leans forward. You can feel her breath on your crotch. She opens her mouth and sticks out her tongue and begins to lick along the length of your shaft."
    "After a few seconds of teasing, you use a hand on the back of her head to bring her mouth to the tip."
    $ the_person.change_obedience(2)
    "[the_person.possessive_title!c] looks up at you and obediently opens her mouth, allowing your pressure on the back of her head to slide your cock into her warm, wet mouth."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    $ the_person.change_arousal(4)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(15)
    $ the_person.change_slut(1, 60)
    mc.name "Mmmm, ohhh that's it."
    "Her tongue glides in sensual circles, licking up your precum, before her head begins to bob up and down as she sucks on your cock."
    $ the_person.break_taboo("sucking_cock")
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(40)
    "You let out of a growling moan as [the_person.possessive_title] begins to work you over with her eager mouth."
    "Her lips and tongue stimulate you in all kinds of exciting ways for several seconds."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    "She pulls back and looks up at you."
    the_person "So, [the_person.mc_title], are you going to have your slutty secretary in here often? On her knees, servicing her boss whenever he pleases?"
    mc.name "Of course. I think you'll fit nicely beneath my desk, servicing me while I accomplish all sorts of work tasks. Maybe even having meetings with employees.."
    $ the_person.change_arousal(15)
    $ the_person.change_slut(1, 70)
    the_person "Fuuuuck... that sounds hot..."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "She opens her mouth and gets back to work with a renewed vigour. Her lips and tongue are working your erection with a renewed eagerness."
    mc.name "And don't forget, a good office slut always swallows everything. There's less to clean up afterwards."
    "She mumbles something that sounds like agreement, but the words are lost as your girth fills her mouth."
    return

label personal_secretary_prog_trans_scene_3(the_group):
    # Cowgirl
    $ the_person = the_group[0]
    mc.name "Sometimes I need something more than just your mouth. I need to feel a tight wet pussy on my dick."
    the_person "Oh... Yes, you do [the_person.mc_title]."
    if not the_person.vagina_visible:
        $ the_item = the_person.outfit.get_lower_top_layer
        if the_item:
            if the_item.is_skirt or the_item.is_dress:
                mc.name "Why don't you pull up your [the_item.display_name]?"
            elif the_item.is_pants:
                mc.name "Why don't you pull down you [the_item.display_name]?"
            else:
                mc.name "Why don't you move those [the_item.display_name]'s out of the way?"

            $ the_person.draw_animated_removal(the_item, half_off_instead = True)
            the_person "Like this?"

            if not the_person.vagina_visible:
                mc.name "Keep going..."
                $ the_person.strip_to_vagina(prefer_half_off = True)
                mc.name "Nice."
            else:
                mc.name "Perfect."
        else:
            mc.name "Why don't you make your sweet little pussy available?"
            "She gives you a smile and starts moving her clothes out of the way."
            $ the_person.strip_to_vagina(prefer_half_off = True)
    else:
        mc.name "I see you came prepared."

    the_person "Okay... shall I bend over your desk?"
    mc.name "No, I'm to tired to pound your slutty cunt, I need you to ride me, so I can relax."
    the_person "Oh, silly me..."
    mc.name "Now be a good little secretary and ride your boss's dick until he fills you up."
    return

label personal_secretary_prog_trans_scene_4(the_group):
    $ the_person = the_group[0]
    # Bend her over your desk
    mc.name "You know what, I could definitely use some relief. And I know exactly how I want it."
    the_person "Oh? What can I do for you sir?"
    "You get up and start to walk around your desk."
    mc.name "Nothing. Just let me do what I want and enjoy yourself in the process."
    the_person "Oh my... okay..."
    $ the_person.draw_person(position = "back_peek")
    "You get behind her. Her body is trembling as you run your hands across her shoulders and down he sides."
    if not the_person.vagina_visible:
        $ the_item = the_person.outfit.get_lower_top_layer
        if the_item:
            if the_item.is_skirt or the_item.is_dress:
                mc.name "Why don't we just you pull up this [the_item.display_name]..."
            elif the_item.is_pants:
                mc.name "Why don't we just pull down this [the_item.display_name]..."
            else:
                mc.name "Why don't we just move this [the_item.display_name] out of the way..."

            $ the_person.draw_animated_removal(the_item, half_off_instead = True, position = "back_peek")


            if not the_person.vagina_visible:
                mc.name "Hmm, almost there..."
                $ the_person.strip_to_vagina(prefer_half_off = True, position = "back_peek")
                mc.name "There we go."
            else:
                mc.name "Perfect."
        else:
            mc.name "Why don't we get a good look at that sweet little pussy of yours..."
            "She sighs when you start moving her clothes out of the way."
            $ the_person.strip_to_vagina(prefer_half_off = True)
    else:
        mc.name "I see you came prepared."
    "[the_person.possessive_title!c] gasps when she feels you run a finger between her legs, along her slit."
    the_person "Ahh, sir? I..."
    mc.name "Shhh, just enjoy it."
    $ the_person.change_arousal(15)
    "You spend a few seconds, stroking her between the legs, making sure she is wet and ready for you."
    "With your other hand, you apply some pressure between her shoulders, slowly bending her over your desk."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person == mom:
        "You can't believe you are about to use [the_person.possessive_title] as your personal cock sleeve, right here in your office."
    else:
        "You look down. You finally have your secretary obediently bent over your desk, ready to get fucked."
    "You unzip your pants and take out your cock, then take it in your hand and use it to deliver a few lights spanks to her ass cheeks."
    $ the_person.change_arousal(15)
    return

label personal_secretary_prog_trans_scene_5(the_group):
    $ the_person = the_group[0]
    # Anal sitting on lap
    return

label personal_secretary_prog_trans_scene_6(the_group):
    $ the_person = the_group[0]
    # Bend her over your desk anal
    return



#Final Scenes
label personal_secretary_prog_scene_scene_0(the_group, scene_transition = False):
    $ the_person = the_group[0]
    the_person "Certainly sir!"
    "She walks around the side of your desk and stops next to you. You swivel your chair to the side to face her."
    if the_person.tits_available and the_person.tits_visible:
        "Her chest is directly at face height. Before she gets started, you reach out and hungrily grope her tits."
    else:
        mc.name "Can you get your tits out? I want something nice to look at."
        the_person "Sure."
        "She gets disrobed right in front of you."
        $ the_person.strip_to_tits(prefer_half_off = False, position = "stand4")
        "When her tits drop out of her top, you hungrily reach out and grope them."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(10)
    the_person "Mmm... feels amazing when you play with them..."
    "After several seconds of groping, she reaches down. She fumbles with your trousers for a few moments, but eventually unzips them and pulls out your cock."
    "She sits down on your lap, facing you."
    $ the_person.draw_person(position = "kneeling1")
    $ the_person.change_slut(2, 40)
    the_person "Oh my god, you are so hard! Don't worry I'll take care of this, boss!"
    "[the_person.possessive_title!c]'s soft hand starts to stroke you. It feels great."
    "You continue to grope her tits while she strokes your cock."
    the_person "Mmm, that feels nice too."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(15)
    "Her soft hand feels good, but you need to get some lubrication involved if you want to be able to finish."
    "You open a desk drawer and pull out a bottle of lotion that [the_person.title] keeps stocked in there and hand it to her."
    "She squirts a liberal amount on your cock and resumes stroking it with her hand. The sensations get much more pleasurable."
    mc.name "Mmm, that's it."
    the_person "Just enjoy yourself and let your secretary take care of you..."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(20)
    "[the_person.possessive_title!c]'s tits begin to shake right in front of you as her handjob speeds up. You lean forward and bury your face into one."
    "You open your mouth and suck vigorously on one of her nipples. She gasps."
    $ play_moan_sound()
    the_person "Ahhhh, that's it... That feels so good. Does it feel good for you, sir?"
    "You moan your approval through your mouth, into her breast. After a few more seconds, you switch sides, attacking her other breast with your mouth."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(20)
    "You are getting lost in the pleasure. Your arousal was so built up, you are getting ready to cum. You pull back for a second."
    mc.name "Keep going, I'm going to cum."
    the_person "Do it boss! Give me your hot cum!"
    "As you get ready to cum, she speeds up, finishing you off."
    $ climax_controller = ClimaxController(["Cum on her", "body"])
    $ the_choice = climax_controller.show_climax_menu()
    $ climax_controller.do_clarity_release(the_person)
    $ the_person.cum_on_stomach()
    $ the_person.draw_person(position = "kneeling1")
    "You bury your face in your secretary's tits as you start to cum."
    "It explodes up and out of her hand on onto her stomach."
    the_person "That's it! Cum for me!"
    "When you finish with the last spurt, you sit back in your chair. You look down and smile at the mess you've made of your secretary."
    if scene_transition:
        the_person "Wow... that was certainly one way to mix it up..."
        $ the_person.change_slut(1, 40)
    if the_person.opinion.being_covered_in_cum > 0:
        "[the_person.title] starts to rub your cum into her stomach, enjoying being covered in your hot cum."
        the_person "Mmm, thank you for your cum, boss!"
    else:
        the_person "That was fun, but now the worst part. The cleanup."
        mc.name "Ahh, don't think of it like that. Think of it as proof of how sexy you are."
        mc.name "Besides, is it really that bad?"
        $ ran_num = renpy.random.randint(0, 100)
        if (mc.charisma * 10 + the_person.suggestibility) > ran_num:    #Success
            $ mc.log_event(f"Charisma Check Passed", "float_text_green")
            "She looks up at you, then back down at the mess on her stomach."
            the_person "You know, you're right. It's actually kind of nice, if you just let yourself enjoy it a little."
            $ the_person.set_opinion("being covered in cum", 1)
        else:
            $ mc.log_event(f"Charisma Check Failed", "float_text_red")
            "She looks up at you and frowns."
            the_person "Yeah right. As much as I love to hear you moan and feel you spurt, it is such a pain to clean this stuff up."
        $ ran_num = None
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title!c] stands up."
    if scene_transition:
        the_person "Well... I suppose next time you are too horny to get any work done we could do that again, if you wanted."
        mc.name "Excellent. I was just thinking the same thing."
    $ del climax_controller
    $ del the_choice



    call personal_secretary_post_scene(the_group) from _person_secretary_handjob_cleanup_time_00a
    return

label personal_secretary_prog_scene_scene_1(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        pass    #First time through this, we have already groped her and she is on her knees next to MC's chair.
    else:
        the_person "Certainly sir!"
        "She walks around the side of your desk and stops next to you. You swivel your chair to the side to face her."
        if the_person.tits_available and the_person.tits_visible:
            "Her chest is directly at face height. Before she gets started, you reach out and hungrily grope her tits."

        else:
            "She gets disrobed right in front of you."
            $ the_person.strip_to_tits(prefer_half_off = False, position = "stand4")
            "When her tits drop out of her top, you hungrily reach out and grope them."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(10)
        the_person "Mmm... feels amazing when you play with them..."
        "After several seconds of groping, you stop, and she gets down on her knees."
        $ the_person.draw_person(position = "blowjob")
    "She reaches forward and pulls at the button and zipper on your pants. She grabs your waistband and pulls down your pants and underwear until your cock springs free."
    $ the_person.change_slut(2, 50)
    the_person "Oh my god... it's so hard! The veins are popping out! My poor boss! Let me take care of this!"
    "You open a desk drawer and pull out a bottle of lotion that [the_person.title] keeps stocked in there and hand it to her."
    "She squirts a liberal amount on your cock and more into her cleavage."
    $ the_person.draw_person(position = "kneeling1")
    "[the_person.possessive_title!c] leans forward, holding her tits together with one hand."
    "With your cock against her stomach, she slides down, engulfing your erection in her lotioned up cleavage."
    mc.name "Oh fuck!.. [the_person.title] that feels so good..."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(10)
    the_person "Mmm your cock is so warm. Aren't you glad you chose me to be your sexy secretary? I know I am!"
    mc.name "Yes. You are certainly well endowed."
    the_person "Likewise..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title!c] rubs her tits up and down your shaft, making sure to get the lotion spread evenly."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(15)
    mc.name "Oh fuck... you're right. I really AM worked up. I'm not sure I'm going to last very long."
    the_person "Just sit back and enjoy. I'm happy to service you, boss!"
    "Knowing you are already excited, she sets a moderate pace to start, as she begins to move her whole upper body up and down."
    "With each down stroke, you can only get a peak at the tip of your cock as it briefly emerges from her quaking tit flesh."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(15)
    "You reach down with one hand and give one of her udders a squeeze, then pinch her nipple."
    $ play_moan_sound()
    "[the_person.title] lets out a moan, then looks up at you, biting her lip."
    the_person "Does it feel good for you sir?"
    mc.name "Mmmhmm, it feels incredible. Keep going my sexy little secretary."
    $ the_person.change_slut(1, 50)
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(15)
    "She blushes a bit but clearly enjoys servicing you."
    $ play_moan_sound()
    "[the_person.possessive_title!c] lets out a moan. She pinches her nipples while she bounces up and down."
    "She grabs your cock with her hand and then pulls her chest back from around you. She takes the tip of your cock and uses it to tease her nipples."
    the_person "Mmm, my nipples are so sensitive."
    "[the_person.title] taps her chest a few times now with your cock, sending ripples out from the point of impact."
    "Satisfied with her teasing, she takes her funbags in her hands and then wraps them around your cock again and resumes stroking you."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(25)
    mc.name "OH... Fuck... I'm gonna cum soon...! I wanna coat those incredible tits of yours!"
    the_person "Do it boss! Cover me with your hot cum!"
    "As you get ready to cum, she speeds up, finishing you off with her mammaries."
    $ climax_controller = ClimaxController(["Cum on her tits", "tits"])
    $ the_choice = climax_controller.show_climax_menu()
    $ climax_controller.do_clarity_release(the_person)
    "Your orgasm builds to a peak and you grunt, blasting your load up between [the_person.title]'s tits and out the top of her cleavage."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "kneeling1")
    "Your cum splatters down over the top of [the_person.title]'s tits. She gasps as the warm liquid covers her and drips back down between her tits."
    "When you finish with the last spurt, you sit back in your chair. You look down and smile at the mess you've made of your secretary."
    if scene_transition:
        the_person "Wow... that was certainly one way to mix it up..."
        $ the_person.change_slut(1, 40)
    if the_person.opinion.being_covered_in_cum > 0:
        "[the_person.title] starts to rub your cum into her chest, enjoying being covered in your hot cum."
        $ the_person.change_arousal(15)
        if the_person.arousal_perc >= 100:   #She orgasms
            the_person "Fuck that was hot... I... oh my god!"
            $ the_person.draw_person(position = "kneeling1", emotion = "orgasm")
            "Suddenly her words cut off with her mouth open and she roughly pinches her cum coated nipples. She's cumming!?!"
            $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 60)
            "She gasps and moans multiple times. She finished after just breast stimulation, dirty talk, and being covered in cum!"
            $ the_person.draw_person(position = "kneeling1")
            "Once she is finished, [the_person.title] just looks up at you."
            the_person "Oh my god... that was so good..."
            "She appears to have entered a trance after her surprise orgasm."
        else:
            the_person "Mmm, thank you for your cum, boss!"
    else:
        the_person "That was fun, but now the worst part. The cleanup."
        mc.name "Ahh, don't think of it like that. Think of it as proof of how sexy you are."
        mc.name "Besides, is it really that bad?"
        $ ran_num = renpy.random.randint(0, 100)
        if (mc.charisma * 10 + the_person.suggestibility) > ran_num:    #Success
            $ mc.log_event(f"Charisma Check Passed", "float_text_green")
            "She looks up at you, then back down at the mess on her chest."
            the_person "You know, you're right. It's actually kind of nice, if you just let yourself enjoy it a little."
            $ the_person.set_opinion("being covered in cum", 1)
        else:
            $ mc.log_event(f"Charisma Check Failed", "float_text_red")
            "She looks up at you and frowns."
            the_person "Yeah right. As much as I love to hear you moan and feel you spurt, it is such a pain to clean this stuff up."
        $ ran_num = None
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title!c] stands up."
    if scene_transition:
        the_person "Well... I suppose next time you are too horny to get any work done we could do that again, if you wanted."
        mc.name "Excellent. I was just thinking the same thing."
    $ del climax_controller
    $ del the_choice
    call personal_secretary_post_scene(the_group) from _person_secretary_titfuck_cleanup_time_01a
    return

label personal_secretary_prog_scene_scene_2(the_group, scene_transition = False):
    $ the_person = the_group[0]
    $ finish_type = the_person.facial_or_swallow()  # "swallow" "facial"
    if scene_transition:
        pass    #First time through this, She is already on her knees sucking off MC.
    else:
        "[the_person.possessive_title!c] starts to walk around your desk."
        if the_person.tits_available and the_person.tits_visible:
            mc.name "You know what to do. Get on your knees."
            "She obediently gets down on her knees, ready to service you."

        else:
            mc.name "You know what to do. Get on your knees, and get your tits out."
            "She obediently gets down on her knees, taking her tits out so she can be ready to service you."
            $ the_person.strip_to_tits(prefer_half_off = False, position = "blowjob")
        $ the_person.draw_person(position = "blowjob")
        $ the_person.change_obedience(2)
        the_person "Is it okay if I take it out now sir?"
        mc.name "Yes. Go ahead and take my cock out and get to work."
        the_person "Yes sir!"
        "She reaches over and unbuttons and unzips your pants, then pulls at the waistline, pulling down your pants and underwear until your cock springs free."
        the_person "Oh god it's so big..."
        "She leans forward and begins to lick up and down the shaft."
        if finish_type == "swallow":
            the_person "Mmm, I can't wait to swallow all of your hot cum..."
        else:
            the_person "Mmm, I can't wait for you to cover my face in your hot cum..."
        $ mc.change_locked_clarity(40)
        $ mc.change_arousal(15)
        "It feels good, but soon you are ready for more. You put your hand on the back of [the_person.possessive_title]'s head and urge her up, until the tip rests on her lips."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "She looks up at you and makes eye contact as she opens her mouth and allows you to guide her head down with your cock sliding into her wet mouth."
        "Your secretary runs her tongue around the tip, licking up her first bit of precum, then begins bobbing her head up and down on your erection."
        $ the_person.change_arousal(4)
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(15)
        mc.name "Ohhh fuck. That is just what I needed. What a good secretary, sucking your boss's cock to help him keep his focus on work."
        "[the_person.title] closes her eyes and gets to work, slobbering up and down your length."
        "She is happy and eager to please the man who signs her paychecks."
    "You sit back in your office chair, your legs spread, your slutty secretary in between them."
    "Lewd sucking noises and muffled moans drive your pleasure as you watch her work."
    $ the_person.change_arousal(4)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(15)
    "Soft slurps and tongue movement across your length relax away the stresses of work. You run your hands through [the_person.possessive_title]'s hair, appreciatively."
    "[the_person.title] pops off your cock and her lips make a loud smacking noise."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    if the_person == mom:
        the_person "Am I doing okay, [the_person.mc_title]?"
        "The way [the_person.possessive_title] emphasizes your title makes your cock twitch."
    else:
        the_person "Is this helping, [the_person.mc_title]?"
    "You put your hand on the back of her head."
    mc.name "It feels amazing, now keep going."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "A brief smile appears on [the_person.title]'s face before her mouth opens and she resumes servicing your manhood orally."
    $ the_person.change_arousal(4)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(25)
    "More slurping and more muffled moaning. It's good to be the boss."
    if the_person.oral_sex_skill <= 3:   #Average blowjob
        the_person "Mmmmmff... *slurp*...... nnnnhh..."
        "You leave your hand on the back of her head, content to let her pleasure you at her own pace and skill."
        $ the_person.change_arousal(4)
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(25)
        "[the_person.title]'s swirling tongue and persistent head bobbing are paying off. It feels amazing."
    else:
        mc.name "Mmm, fuck [the_person.title], you are so good at this."
        "She looks up at you and gives you a little wink."
        "Without breaking eye contact, her mouth descends past the tip, her lips devouring your entire length as she takes you down her throat."
        $ the_person.change_arousal(4)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(25)
        mc.name "Mmm, that's it..."
        "You entire length is enguled in the wet heat of her mouth and throat. You move your hips a bit, thrusting gently down her throat."
        "She throats you for several seconds, returning to the tip only for a moment to get some fresh air, then goes back down your length again."
        "The sensations are incredible."
    "Your cock sucking secretary is doing a great job, and you can feel your excitement starting to build to its conclusion."
    mc.name "I'm gonna cum, [the_person.title]."
    if finish_type == "swallow":
        if the_person.oral_sex_skill <= 3 or the_person.opinion.drinking_cum < 0:  #Generic finish
            "[the_person.title] leaves the tip in her mouth and uses her hand to keep stroking you."
            "The gentle suction of her mouth on your glans sends you over the edge, and you begin to dump your load in your secretary's hot mouth."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "Your cock spasms in her mouth as you fill it up with semen. Once you've finished she slides off, looks up at you and opens her mouth to shows it full of sperm."
            $ play_swallow_sound()
            if the_person.opinion.drinking_cum < 0:
                "She swallows and drinks it all down, with only a slight grimace on her face from the taste."
                $ the_person.increase_opinion_score("drinking_cum", max_value = 1)
            else:
                "She swallows it all and then looks up at you with a smile."
        else:
            the_person "Mmmmfff.. yssss!"
            "[the_person.possessive_title!c] voices her muffled excitement as she takes your cock down her throat again."
            "The sensations nearly overwhelm you. You put your hand on the back of her and pin her face in place as you start to spasm and cum down her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "throat", person = the_person)
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "[the_person.title]'s fingers dig into your thighs as she takes your load, but doesn't attempt to pull back until your are completely satisfied."
            "When you let go, your cock slips from her mouth with a wet pop."
            "[the_person.title] is licking her lips, then uses her fingers to see if any cum leaked out during your finish."
    else:
        $ the_person.draw_person(position = "blowjob", emotion = "happy")
        if the_person.opinion.cum_facials < 0:
            the_person "Why don't you cum on my face?"
            "[the_person.possessive_title!c] backs off and starts stroking you with her hand, pointing it at her face."
            $ mc.change_locked_clarity(30)
            "She closes her eyes as you begin to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
            "She gives a slight smile as you paint her face with spurt after spurt of hot cum."
            "[the_person.title] keeps stroking you until your orgasmic pulses stop, then carefully opens her eyes."
            $ the_person.increase_opinion_score("cum_facials", max_value = 1)
            the_person "That... was actually kind of fun!"
        else:
            "Suddenly, [the_person.possessive_title] backs off and starts stroking you eagerly with her hand."
            if the_person == mom:
                the_person "That's it! Cum all over mommy's face!"
            else:
                the_person "That's it [the_person.mc_title]! Cum all over your slutty secretary's face!"
            $ mc.change_locked_clarity(50)
            "Her eyes are locked to yours as she points your cock directly at her face as you start to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
            "She smiles as you paint her face with spurt after spurt of hot cum. One of them makes her jump when in hits her eyes, which she promptly closes."
            "[the_person.title] keeps stroking you until your orgasmic pulses stop."
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
    if the_person == mom:
        "[the_person.possessive_title!c]'s voice is soft and soothing."
        the_person "Mmm, good boy. Now you can get back to work."
    else:
        "From between your legs, [the_person.possessive_title]'s voice is soft and soothing."
        the_person "That should help you get back to work now, sir..."
    "Before she stands up, [the_person.title] leans forward and licks your softening cock up and down a few times, cleaning any cum remnants off."
    $ the_person.draw_person(position = the_person.idle_pose)
    if scene_transition:
        the_person "Well... I suppose next time you are too horny to get any work done we could do that again, if you wanted."
        mc.name "Excellent. I was just thinking the same thing."
    $ del finish_type

    call personal_secretary_post_scene(the_group) from _person_secretary_blowjob_cleanup_time_00a
    return

label personal_secretary_prog_scene_scene_3(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        pass    #First time through this, she is already naked in front of you.
    else:
        the_person "Of course, [the_person.mc_title]."
        mc.name "Now be a good little secretary and ride your boss's dick until he fills you up."
        if not the_person.vagina_visible:
            "She gives you a smile and starts moving her clothes out of the way."
            $ the_person.strip_to_vagina(prefer_half_off = True)

    "You push your chair back while she walks up to you."
    the_person "Let me get that for you, [the_person.mc_title]."
    "She unzips your pants and takes out your cock."

    $ ceo_office.lock() # prevent walk-ins
    call mc_sex_request(the_person, the_request = "vaginal cowgirl", start_object = make_chair()) from _call_mc_sex_request_personal_secretary_cowgirl
    $ ceo_office.unlock()

    call personal_secretary_post_scene(the_group) from _person_secretary_cowgirl_cleanup_time_00a
    return

label personal_secretary_prog_scene_scene_4(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        pass    #First time through this, you have her bent over your desk with your cock out, ready to penetrate her.
    else:
        "You get up and walk around your desk, getting behind [the_person.possessive_title]"
        $ the_person.draw_person(position = "back_peek")
        "She watches you, but doesn't object."
        if not the_person.vagina_visible:
            "Her arms stay are her sides as you start moving her clothes out of the way."
            $ the_person.strip_to_vagina(prefer_half_off = True)
        "With one hand, you reach down between her legs and run your middle finger between her labia, and with the other you pull your cock out."
        $ the_person.change_arousal(15)
        "You stroke the length of her slit a few times, her body already getting aroused."
        the_person "Mmm, I think I know where this is going..."
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title!c] bends over your desk, her ass up and ready for you to use."
        "You smack her ass with your cock a couple times, enjoying the way it wobbles when you do."

    call personal_secretary_special_condom_ask(the_group) from _call_condom_personal_secretary_condom_check_01
    "You put one hand on her hip and with the other you point your dick at her slit."
    "You push your hips forward and slide inside her with one slow, gentle thrust."

    $ ceo_office.lock()
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), condition = make_condition_secretary_sex(),skip_intro = True, skip_condom = True) from _call_sex_sec_standing_doggy_03
    $ ceo_office.unlock()




    # $ ceo_office.lock() # prevent walk-ins
    # call mc_sex_request(the_person, the_request = "vaginal cowgirl", start_object = make_chair()) from _call_mc_sex_request_personal_secretary_cowgirl
    # $ ceo_office.unlock()

    call personal_secretary_post_scene(the_group) from _person_secretary_bent_over_cleanup_time_00a
    return

label personal_secretary_prog_scene_scene_5(the_group, scene_transition = False):
    $ the_person = the_group[0]

    call personal_secretary_post_scene(the_group) from _person_secretary_anal_cowgirl_cleanup_time_00a
    return

label personal_secretary_prog_scene_scene_6(the_group, scene_transition = False):
    $ the_person = the_group[0]

    call personal_secretary_post_scene(the_group) from _person_secretary_anal_bent_over_cleanup_time_00a
    return

label personal_secretary_post_scene(the_group):
    $ the_person = the_group[0]
    if the_person.is_in_trance:
        "[the_person.title] is in a trance. Before you release her, you can take a moment to train her."
        call do_training(the_person) from _call_do_training_personal_sec_sex_time_01
    the_person "Well, should I go clean up and get back to my desk?"
    mc.name "I appreciate your hard work [the_person.title]. You can go now."
    $ the_person.change_obedience(2, 160)
    the_person "Thank you sir!"
    $ the_person.draw_person(position = "walking_away")
    $ the_person.slap_ass()
    "As she turns around, you give [the_person.possessive_title] a slap on the ass."
    "Your secretary turns and walks to your office door. She unlocks it, opens it, and leaves."
    $ clear_scene()
    "You clean up a bit yourself and then turn back to your computer. You find it much easier to concentrate on your work tasks now."
    $ the_person.apply_planned_outfit()
    return

label personal_secretary_special_condom_ask(the_group): #Use this as an alternative to the condom_ask routine, since that routine can return with not having sex at all.
    $ the_person = the_group[0]
    $ condom_threshold = the_person.get_no_condom_threshold()

    if the_person.effective_sluttiness() < condom_threshold:
        $ the_person.call_dialogue("condom_ask")
        menu:
            "Put on a condom":
                mc.name "Yeah, I'd probably better."
                "You pull a condom out of your desk and tear open the package."
                $ mc.condom = True
                "You quickly put it on."

            "Don't bother":
                mc.name "Yeah right, I didn't hire you to be my secretary so that I could cum into a latex sleeve."
                the_person "Ahh... okay..."
    elif the_person.has_cum_fetish or the_person.has_breeding_fetish:
        "[the_person.possessive_title!c] is ready to fuck, and doesn't seem remotely interested in protection, but if you wanted to you could put on a condom."
        menu:
            "Put on a condom":
                "You pull a condom out of your desk and tear open the package."
                "[the_person.title] takes a hold of your hand."
                the_person "Please don't use that! I want to feel your cum dripping out of me the rest of the day..."
                menu:
                    "Insist on condom":
                        mc.name "I think a condom is a good idea, so I'm going to put one on anyway."
                        "She scoffs, but knows better than to fight you on this."
                        the_person "Ugh, fine... you're the boss."
                        $ mc.condom = True
                        "She lets go and you quickly put the condom on."
                    "Fuck her raw":
                        mc.name "Since you feel so strongly about it, I guess I could give you my raw cock."
                        the_person "Mmm, I can't wait..."

            "Don't bother":
                pass
    else:
        "[the_person.possessive_title!c] is ready to fuck, but you stop for a moment. Maybe you should put on a condom?"
        menu:
            "Put on a condom":
                "You pull a condom out of your desk and tear open the package. [the_person.title] sees what you are doing."
                $ the_person.call_dialogue("condom_bareback_ask")
                menu:
                    "Insist on condom":
                        mc.name "I think a condom is a good idea, so I'm going to put one on anyway."
                        "She scoffs, but knows better than to fight you on this."
                        the_person "Ugh, fine... you're the boss."
                        $ mc.condom = True
                        "She lets go and you quickly put the condom on."
                    "Fuck her raw":
                        mc.name "Since you feel so strongly about it, I guess I could give you my raw cock."
                        the_person "Mmm, I can't wait..."
            "Don't bother":
                pass
    return
