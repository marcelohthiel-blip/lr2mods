

#Ashley Obedience Path
#Ashley taking command path

#These labels are for MC hitting specific personal serum requirements.
label ashley_demands_relief_label():    #at 30
    $ the_person = ashley
    $ the_person.arousal = 50   #She's horny
    $ the_person.add_situational_slut("Horny", 10, "I really need some relief!")
    $ first_time = the_person.event_triggers_dict.get("sub_titfuck_count", 0) == 0
    "It is the end of the day, so you swing by your office to pick up your daily serum dose."
    $ ceo_office.show_background()
    $ the_person.draw_person()
    "When you walk in, you see [the_person.possessive_title] standing next to your desk."
    mc.name "Ah, hello [the_person.title]."
    the_person "Oh hey. I was just dropping off your serums for you."
    mc.name "Thanks."
    "You walk over to your desk. As you reach down to pick them up, [the_person.title] puts her hand on yours."
    the_person "Hey, umm... I kinda need you to do something for me."
    mc.name "Oh?"
    the_person "Working on these serums, and around here in general, I'm really picking up a lot of tension, if you know what I mean."
    mc.name "I think I do."
    if ashley.progress.lust_step >= 1:
        the_person "I mean obviously we need to be quick... we don't want my sister to catch on or anything..."
    else:
        the_person "I need to be quick, I made a commitment with my sister this evening..."
    the_person "But I was thinking, you kinda owe me for making these serums for you anyway."
    the_person "I've heard you are pretty good with your hands, can you just get me off really quick?"
    mc.name "Hmmm... I don't know..."
    the_person "Seriously? It isn't often a girl asks you to stick your hands in her pants. Think carefully."
    "Something about her tone tells you she is being serious. You think about it for a moment."
    menu:
        "Finger Her\n{menu_red}Increases Sluttiness and Love{/menu_red}":
            mc.name "Alright, I can probably just get your sister to suck me off later anyway."
            the_person "Yes! And if you're trying to make me jealous, it isn't going to work."
            $ the_person.draw_person(position = "sitting")
            $ the_person.change_stats(love = 5, slut = 2)
            "[the_person.title] sits down on the edge of your desk. You walk over to her."
            "She puts her legs out and reach up, pulling off her bottoms."
            $ the_person.strip_to_vagina(position = "sitting")
            $ mc.change_locked_clarity(30)
            "Once exposed, she spreads her legs for you."
            $ the_person.draw_person(position = "missionary")
            the_person "Don't worry, you don't need to warm me up. I'm good to go."
            "You look down at her slit. Her inner labia are peeking out, and are glistening with arousal."
            mc.name "Damn. You really are turned on. Alright, time to get to work."
            "You put your middle and index finger together and stroke her slit a few times. Once they are good and wet, you easily slide them inside [the_person.possessive_title]."
            the_person "Mmm... fuck that's good..."
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(30)
            "[the_person.title] lays back and closes her eyes as you get to work. You push your two fingers deep inside her, giving her a few long, sensual strokes."
            the_person "That's good. I don't know why I didn't do this sooner..."
            "[the_person.possessive_title!c]'s body is responding to your touch rapidly. Her hips are moving in time with your strokes."
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(30)
            "With your other hand, you wet your thumb along her slit, then use it to move in circle around her clit."
            "[the_person.title] starts to writhe when you curl your two fingers inside her up, stroking her g-spot."
            $ the_person.change_arousal(30)
            $ mc.change_locked_clarity(30)
            the_person "Oh fuck! Right there, that's it!"
            "Her whole body tenses up and she shivers as she climaxes."
            "She quivers with pleasure for several seconds before her whole body relaxes."
            $ the_person.have_orgasm(half_arousal = False)
            the_person "Oh my god... I needed that so bad... you have no idea."
            "It was pretty hot, fingering [the_person.possessive_title] while she sits on your desk. You start to consider pulling out your dick and getting some service in return..."
            the_person "Don't worry, I'll see myself out after a bit. If you go now maybe you can still catch Steph before she leaves for the day."
            "Right, her sister. You consider for a moment just ignoring what she said and pulling your dick out anyway. But for some reason, it just seems like a bad idea."
            "You decide to give her time to recover. You reach over and grab the vials of serum for tomorrow. As you hold them in your hand, something feels a little off..."
            "Why are you doing what she told you to do? You want HER to get you off. But for some reason it just feels wrong."
            "As you turn and leave your office, you are deep in thought."
            the_person "That was great, [the_person.mc_title]. Next time I need another release like that, I'll be sure to swing by at closing time!"

        "Mutual Masturbation\n{menu_red}Increases Obedience{/menu_red} (disabled)":
            pass

    "You leave your office, leaving [the_person.possessive_title] behind."
    $ clear_scene()
    $ the_person.clear_situational_slut("Horny")
    $ add_ashley_demands_oral_action()
    return

label ashley_demands_oral_label():  #at 60
    $ the_person = ashley
    "In this scene, Ashley again approaches MC. This time she demands he eat her out."
    "We give players the opportunity to push back and ask for a favour in return for a small obedience boost."
    "If we submit, Ashley loses some obedience."
    $ add_ashley_arousal_serum_start_action()
    return

label ashley_arousal_serum_start_label():  #at 100
    $ the_person = ashley
    "In this scene, it starts with Stephanie texting MC asking if he has seen Ashley around."
    "He replies no, goes to his office to pickup his serums."
    "Once there, Ashley tries to handcuff him."
    "This is the scene that sets MCs non consent preferences. MC can submit, roleplay, or reject."
    "At the end, Stephanie walks in and gets angry. At the end, link to MC arousal serum quest."
    $ add_ashley_demands_sub_action()
    return

label ashley_demands_sub_label():   #at 150
    $ the_person = ashley
    "In this scene, Ashley approaches MC in private and gives him handcuffs, ordering him to put them on if he knows what's good for him"
    "Depending on non con preferences, MC will either submit, partially submit, or fake submission."
    "Choice provides a big swing in Ashley's obedience"
    $ add_ashley_final_submission_action()
    return

#Ashley's obedience levels
label ashley_submission_titfuck_label():  #at 20
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_titfuck_count", 0) == 0

    if mc.is_at(ceo_office):
        "At the end of the day, you are working in your office, when someone enters your door."
        $ the_person.draw_person(emotion = "happy")
        "As you look up, you see [the_person.possessive_title] walking in."
    else:
        "It is the end of the day, so you swing by your office to pick up your daily serum dose."
        $ mc.change_location(ceo_office)
        $ the_person.draw_person(emotion = "happy")
        "As you open the door, you see [the_person.possessive_title] standing next to your desk."
    mc.name "Ah, hello [the_person.title]."
    the_person "Oh hey. I was just dropping off your serums for you. Have a good evening."

    if first_time:
        if the_person.tits_visible:
            "[the_person.possessive_title!c]'s big tits are on full display for you. They heave a little with each breath and movement she makes."
        else:
            "You check her out. Her big tits seem to bounce enticingly with each movement she makes."
    "You've got a lot of pent-up energy from the day. You decide to see if you can get her to play with you for a bit."
    if first_time:
        mc.name "Hey, before you go, can I tell you something?"
        the_person "Sure?"
        mc.name "This might be a little bit forward, but... you have some really incredible tits."
        $ the_person.change_happiness(2)
        the_person "Wow. You're right. That is really forward."
        "She smiles a bit."
    else:
        mc.name "You know, you really DO have some incredible tits."
        the_person "Ah geez. This again?"
        $ the_person.change_happiness(2)
        "She questions you, but you notice a hint of a smile on her face."
        mc.name "I mean, can you blame me?"
        the_person "Yes. Yes I can."
    $ the_person.change_arousal(20)
    "You step closer to her. Now just an arms reach away."
    if not the_person.tits_visible:
        mc.name "Can I see them?"
        "She mutters under her breath for a moment. But then nods."
        $ the_person.strip_to_tits()
        $ the_person.break_taboo("bare_tits")
        "You help her take her top off, and her amazing tits spill free from their prior confines."
    "You notice a red tinge on her cheeks... her nipples are hard, ready to be sucked and pinched."
    mc.name "May I?"
    if first_time:
        the_person "You... you want to play with my tits?"
        mc.name "Yes."
        the_person "Umm, sure. That would be okay."
    else:
        "She mumbles under her breath, but nods."
        the_person "Yeah... but you can only touch them!"
        mc.name "Of course."
    "You reach forward with both hands and cup her big tits. They feel soft and hot to the touch."
    "You keep your touch light for now, but grasp both of them. She sighs as she enjoys you feeling her up."
    "She gives a little yelp when you pinch her nipples at the same time."
    if first_time:
        the_person "Ah! Easy..."
        mc.name "I don't know. I think you like it a little rough once in a while, don't you?"
        "She falls quiet. Her silence tells you what the answer is."
    else:
        the_person "Ah! You're always so rough..."
        mc.name "You like it rough though, don't you?"
        "She falls silent. She won't admit it, but you can tell you are turning her on."
    $ the_person.change_arousal(20)
    "[the_person.title]'s breathing is getting quicker. Groping her tits is getting you really turned on as well."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "After a bit longer, you decide it is time to make your move. You reach down and unzip your pants, pulling out your cock."
    if first_time:
        "She gasps when she sees what you are doing."
        the_person "What... what are you doing?"
    else:
        "She sighs when she sees what you are doing."
        the_person "Oh god... not again..."
    mc.name "[the_person.title], your tits are incredible. Get on your knees, I want to feel them wrapped around my cock."
    "You are careful to frame the statement as a command, not a question. She could say no, but you feel confident she will do it."
    if first_time:
        the_person "I... I guess... maybe just this once?"
        mc.name "Of course."
    else:
        the_person "We said... we weren't going to do this again..."
        mc.name "Are you saying you don't want to? You don't want to feel my hard cock between your big juicy tits?"
        the_person "I... I shouldn't..."
        mc.name "But you do. It's okay to want to."
    "She sighs, but obediently gets on her knees."
    $ the_person.draw_person(position = "blowjob")
    if first_time:
        "This is the first time you've gotten her to submit to you like this, and the sight of her on her knees for you gets you harder."
    else:
        "You got her on her knees again. Making her submit to you like this just gets you harder."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "She looks up at you, just a hint of defiance in her eyes. You step forward a bit until your cock is up against her cleavage."
    "The defiance dies when she feels your cock against her hot tit flesh."
    $ the_person.change_arousal(10)
    $ the_person.break_taboo("touching_penis")
    "[the_person.possessive_title!c] takes her tits in her hands and wraps them around your erection. At last her enticing melons are smothering your cock."
    mc.name "Mmm, your tits are amazing. This is going to feel so good."
    "She moves her tits up and down a couple times, but the friction feels a little rough. She looks down and spits a large glob of saliva that drips down into her cleavage."
    "She works her tits around your cock, spreading her saliva all over you. She repeats this a couple more times until your member glides easily back and forth between them."
    "[the_person.title] looks up at you and starts to move up and down a bit. Her heavenly titflesh massages your dick."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    mc.name "God you are so hot. That's it [the_person.title], fuck my cock with your big tits."
    "You let her do all the work for now. Her breasts wobble enticingly as they slide up and down your length."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "You like it too, don't you?"
    $ the_person.increase_opinion_score("giving tit fucks")
    if first_time:
        mc.name "Is this your first time, letting a guy fuck those massive sweater puppies?"
        the_person "No... I've had boyfriends in the past do this... but I've never liked it... before..."
        mc.name "Well, you hadn't met me before, had you? You just needed to find the right man to make getting on your knees feel this good."
        "[the_person.title] is quiet. She is clearly enjoying herself now, but is having trouble letting herself go."
        "She has stopped moving for now as she thinks about what you said."
    elif the_person.opinion.giving_tit_fucks >= 2:  #She orgasms.
        $ the_person.change_arousal(20)
        "[the_person.title] is looking up at you, but her eyes are glazing over. She's... going to orgasm?"
        mc.name "Oh my god, look at you. You are going to cum aren't you? Just from giving me a titty fuck!"
        $ the_person.call_dialogue("surprised_exclaim")
        $ the_person.change_arousal(20)
        mc.name "Look at me and tell me how much you love it and cum while you fuck me with those enormous titties you little slut!"
        the_person "Fuck! I love it! I love fucking your hot cock with my tits! Oh fuck [the_person.mc_title] I'm cumming!"
        "Her whole body starts to quake as she cums. Her tits tremble all around you as her body twitches in pleasure."
        $ the_person.have_orgasm(force_trance = True)
        "When she is finished she stops moving."
        $ mc.change_locked_clarity(100)
    else:
        the_person "That doesn't matter."
        mc.name "Of course it matters. Why are you doing this to yourself? Don't hold out on yourself. Just admit that you love it and move on."
        the_person "Love and like are two very different things."
        mc.name "Fine. Just admit that you like it. You like getting on your knees for me."
        "[the_person.possessive_title!c] stops moving and remains quiet. Sometimes she drives you nuts, remaining quiet when she should just be honest and submit."
    mc.name "Tired? That's okay, I can finish myself."
    "You reach down and grab her tits. You start to move yourself up down, fucking her tits in earnest."
    the_person "Ahhh, you don't need to..."
    mc.name "Nah, I can tell you are wearing out. Don't worry, I'm almost ready to cum. I can't wait to cover those tits of yours!"
    if mc_serum_cum_serum_is_active():
        "She suddenly looks up at you. She obviously knows you are on a serum now that changes your cum's properties."
        the_person "No... not on me!"
        mc.name "Of course on you. How do you think a tit fuck ends?"
    $ mc.change_arousal(40)
    $ mc.change_locked_clarity(50)
    "You speed up, hitting the point of no return. You pull out from between her tits at the last second and fire your load off all over her chest."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "blowjob")
    "You fire wave after wave onto her breasts. When you finish, you look down at your incredible artwork."
    $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_person)
    mc.name "Fuck, that was amazing."
    the_person "Yes... incredible..."
    if first_time:
        "Hah! You finally got her to admit it."
    else:
        "Hah! You got her to admit it again."
    $ the_person.draw_person(position = "stand2")
    "[the_person.possessive_title!c] slowly stands up. A small drip of cum slowly oozes off the edge of one her breasts and onto the floor."
    if first_time:
        the_person "I can't believe I just did that."
    else:
        the_person "I can't believe I just did that. Again."
    mc.name "It's okay. I'm sure it won't be that good EVERY time."
    the_person "I need to go..."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "You watch her disappearing down the hall."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    if first_time:
        "[the_person.possessive_title!c] has always been a little bit hard to predict."
        "You have a feeling you are going to hear about this event again from her."

    else:
        "You sigh. Maybe now she'll be able to accept that it is okay to be the submissive partner during sex once in a while?"
        "Either way, you are sure you'll hear about this soon."

    $ add_ashley_submission_titfuck_taboo_restore_action()
    $ ashley.event_triggers_dict["sub_titfuck_taboo_regen"] = True
    return

label ashley_submission_titfuck_taboo_restore_label(the_person = ashley):
    $ outcome_convince = False
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_titfuck_count", 0) == 0
    $ ashley.event_triggers_dict["sub_titfuck_taboo_regen"] = False
    $ ashley.event_triggers_dict["sub_titfuck_count"] = ashley.event_triggers_dict.get("sub_titfuck_count", 0) + 1
    if not mc.is_at_office:
        "Your phone is ringing. It's [the_person.title]. You pick up."
        the_person "Hey. Can you meet me in your office? We need to talk."
        mc.name "I'll be right there."
        "You make your way back to work. She is waiting for you when you walk into the room."
        $ mc.change_location(ceo_office)
    $ the_person.draw_person(emotion = "angry")
    "[the_person.possessive_title!c] gives you a curt nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "Umm, no? Not at all?"
        the_person "Look, I know what kind of drugs we're making around here. {i}And{/i} the serums I've been making for you."
        the_person "It didn't take me long last night to put two and two together."
        the_person "I'm not just a pair of tits for you to fuck whenever you feel like it. Okay?"
    else:
        the_person "No? It isn't?"
        the_person "We already had this talk... but you seem to have forgotten."
        the_person "I'm not just a pair of big tits for you to fuck whenever you want to get off, okay?"

    mc.name "Are you saying you don't want to meet up now and then after closing anymore?"
    the_person "No... I'm not saying that. I'm just saying that I'm not going to stay late just to fulfil your crazy fantasies."
    if the_person.opinion.giving_tit_fucks == -1:
        mc.name "Admit it though. It wasn't as bad as you were expecting."
        the_person "I mean, I didn't HATE it. But that doesn't mean I like it!"
    elif the_person.opinion.giving_tit_fucks == 0:
        mc.name "Just admit it. Since we started doing this, you're coming around on giving tit fucks."
        the_person "I mean, I guess I'm just ambivalent about it. I don't really care one way or the other, it's more the idea of it."
    elif the_person.opinion.giving_tit_fucks == 1:
        mc.name "I saw the look in your eyes. You were really, truly, enjoying yourself."
        the_person "There are a LOT of sex acts that are enjoyable, but that doesn't mean I have to be down for all of them!"
    elif the_person.opinion.giving_tit_fucks == 2:
        mc.name "[the_person.title]... I saw the look in your eyes. You were loving every second of it."
        mc.name "I bet if I got you alone you'd do it again right now."
        "She stutters her rebuttal."
        the_person "I... yes, having your cock between my tits is amazing..."
        the_person "... but that doesn't mean I'm the kind of girl that just... drops to her knees to service her boss' big meaty cock anytime he wants!"
        mc.name "Who are you trying to convince? Exactly?"
    if the_person.opinion.giving_tit_fucks < 2:
        the_person "Besides, I'm not the type to just drop to her knees on demand."

    $ attempts = 3 - the_person.event_triggers_dict.get("sub_titfuck_count", 0)

    menu:
        "I thought you liked to make me feel good" if ashley.progress.love_step >= 3:
            mc.name "But remember what you told me the other night at my place, after the movie? You said you liked to make me feel good."
            mc.name "That I deserved to have someone do that for me once in a while."
            the_person "I... I know I did..."
            mc.name "Is this really any different? Your tits are amazing. They feel so good when my cock slides between them..."
            "She bites her lip, thinking. Eventually she relents."
            the_person "You're right... you deserve it... just once in a while! Okay?"
            mc.name "Of course."
            $ outcome_convince = True

        "I thought you liked to make me feel good\n{menu_red}Requires: Love Story Progress{/menu_red} (disabled)" if ashley.progress.love_step < 3:
            pass

        "You are that type of girl" if the_person.opinion.giving_tit_fucks == 2:
            mc.name "You keep saying that you just aren't that type of girl, but it is obvious every time it happens that you totally are."
            mc.name "It's okay, [the_person.title]. Boobs are sensitive. Cocks are warm. It's okay to enjoy the sensations of getting the two together."
            mc.name "You are only lying to yourself. You ARE the type of girl to drop to her knees and offer her tits for her boss' satisfaction."
            "[the_person.possessive_title!c] seems like she wants to argue, but even she can understand you're right."
            the_person "Fine. But don't kid yourself into thinking I'm going to take things any further."
            $ outcome_convince = True

        "You are that type of girl\n{menu_red}Requires: Ashley loves giving tit fucks{/menu_red} (disabled)"if the_person.opinion.giving_tit_fucks != 2:
            pass

        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_titfuck_count", 0) >= 3:
            mc.name "If it needs to stop, why does it keep happening [the_person.title]?"
            mc.name "Let's stop pretending. You enjoy it when you service my cock with your tits once in a while."
            mc.name "I'm not saying it needs to be this way every day, but once in a while, you need to take a turn being the submissive one."
            "[the_person.possessive_title!c] seems like she wants to argue, but even she can understand you're right."
            the_person "Fine. But don't kid yourself into thinking I'm going to take things any further."
            $ outcome_convince = True

        "But it keeps happening...\n{menu_red}Requires: [attempts] more submissive tit fucks{/menu_red} (disabled)" if ashley.event_triggers_dict.get("sub_titfuck_count", 0) < 3:
            pass

        "Understood" if the_person.opinion.giving_tit_fucks < 2:
            mc.name "I understand. You have boundaries and I won't cross them again without approval."
            "She looks at you suspiciously, but ultimately accepts your proposal."
            the_person "Alright. Let's just not have this talk again, okay?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks back to her desk."

    if outcome_convince:
        $ ashley_story_path_submission.next_step(ashley, step_index = 0)
        "[the_person.title] is now willing to stay after work once in a while for some discreet fun! Talk to her during the workday and she'll stay late for you."
        "For now, she's willing to let you fuck her tits, but if you can teach her to be more submissive, you're sure there's more she could do while she's on her knees for you..."
    else:
        "[the_person.title] isn't willing to make this a regular thing yet. You wonder if you can get her to be obedient if she would be willing to make this a more regular thing..."
    $ clear_scene()
    return

label ashley_work_titfuck_label(the_person):
    "You look at [the_person.possessive_title]. You feel the time is right to push her obedience boundary again."
    mc.name "Hey, can you come with me to my office? I have something I need to talk to you about in private."
    the_person "Sure."
    $ mc.change_location(ceo_office)
    "[the_person.possessive_title!c] follows you to your office. After you enter, you close the door behind you."
    the_person "So... what was it you needed?"
    "You decided to get straight to the point."
    mc.name "You know, you really DO have some incredible tits."
    the_person "Ah geez. This again?"
    $ the_person.change_happiness(2)
    "She questions you, but you notice a hint of a smile on her face."
    mc.name "I mean, can you blame me?"
    the_person "Yes. Yes I can."
    $ the_person.change_arousal(20)
    "You step closer to her. Now just an arms reach away."
    if not the_person.tits_visible:
        mc.name "Can I see them?"
        "She mutters under her breath for a moment. But then nods."
        $ the_person.strip_to_tits()
        $ the_person.break_taboo("bare_tits")
        "You help her take her top off, and her amazing tits spill free from their prior confines."
    "You notice a red tinge on her cheeks... her nipples are hard, ready to be sucked and pinched."
    mc.name "May I?"

    "She mumbles under her breath, but nods."
    the_person "Yeah... but you can only touch them!"
    mc.name "Of course."
    "You reach forward with both hands and cup her big tits. They feel soft and hot to the touch."
    "You keep your touch light for now, but grasp both of them. She sighs as she enjoys you feeling her up."
    "She gives a little yelp when you pinch her nipples at the same time."
    the_person "Ah! You're always so rough..."
    mc.name "You like it rough though, don't you?"
    "She falls silent. She won't admit it, but you can tell you are turning her on."
    $ the_person.change_arousal(20)
    "[the_person.title]'s breathing is getting quicker. Groping her tits is getting you really turned on as well."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "After a bit longer, you decide it is time to make your move. You reach down and unzip your pants, pulling out your cock."
    "She sighs when she sees what you are doing."
    the_person "Oh god... not again... in the middle of the workday? Really?"
    mc.name "[the_person.title], your tits are incredible. Get on your knees, I want to feel them wrapped around my cock."
    "You are careful to frame the statement as a command, not a question. She could say no, but you feel confident she will do it."
    the_person "We said... we weren't going to do this again..."
    mc.name "Are you saying you don't want to? You don't want to feel my hard cock between your big juicy tits?"
    the_person "I... I shouldn't..."
    mc.name "But you do. It's okay to want to."
    "She sighs, but obediently gets on her knees."
    $ the_person.draw_person(position = "blowjob")
    "You got her on her knees again. Making her submit to you like this just gets you harder."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "She looks up at you, just a hint of defiance in her eyes. You step forward a bit until your cock is up against her cleavage."
    "The defiance dies when she feels your cock against her hot tit flesh."
    $ the_person.change_arousal(10)
    $ the_person.break_taboo("touching_penis")
    "[the_person.possessive_title!c] takes her tits in her hands and wraps them around your erection. At last her enticing melons are smothering your cock."
    mc.name "Mmm, your tits are amazing. This is going to feel so good."
    "She moves her tits up and down a couple times, but the friction feels a little rough. She looks down and spits a large glob of saliva that drips down into her cleavage."
    "She works her tits around your cock, spreading her saliva all over you. She repeats this a couple more times until your member glides easily back and forth between them."
    "[the_person.title] looks up at you and starts to move up and down a bit. Her heavenly titflesh massages your dick."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    mc.name "God you are so hot. That's it [the_person.title], fuck my cock with your big tits."
    "You let her do all the work for now. Her breasts wobble enticingly as they slide up and down your length."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "You like it too, don't you?"
    $ the_person.increase_opinion_score("giving tit fucks")
    if the_person.opinion.giving_tit_fucks >= 2:  #She orgasms.
        $ the_person.change_arousal(20)
        "[the_person.title] is looking up at you, but her eyes are glazing over. She's... going to orgasm?"
        mc.name "Oh my god, look at you. You are going to cum aren't you? Just from giving me a titty fuck!"
        the_person "Oh shit... Oh fuck!"
        $ the_person.change_arousal(20)
        mc.name "Look at me and tell me how much you love it and cum while you fuck me with those enormous titties you little slut!"
        the_person "Fuck! I love it! I love fucking your hot cock with my tits! Oh fuck [the_person.mc_title] I'm cumming!"
        "Her whole body starts to quake as she cums. Her tits tremble all around you as her body twitches in pleasure."
        $ the_person.have_orgasm(force_trance = True)
        "When she is finished she stops moving."
        $ mc.change_locked_clarity(100)
    else:
        the_person "That doesn't matter."
        mc.name "Of course it matters. Why are you doing this to yourself? Don't hold out on yourself. Just admit that you love it and move on."
        the_person "Love and like are two very different things."
        mc.name "Fine. Just admit that you like it. You like getting on your knees for me."
        "[the_person.possessive_title!c] stops moving and remains quiet. Sometimes she drives you nuts, remaining quiet when she should just be honest and submit."
    mc.name "Tired? That's okay, I can finish myself."
    "You reach down and grab her tits. You start to move yourself up down, fucking her tits in earnest."
    the_person "Ahhh, you don't need to..."
    mc.name "Nah, I can tell you are wearing out. Don't worry, I'm almost ready to cum. I can't wait to cover those tits of yours!"
    if mc_serum_cum_serum_is_active():
        "She suddenly looks up at you. She obviously knows you are on a serum now that changes your cum's properties."
        the_person "No... not on me!"
        mc.name "Of course on you. How do you think a tit fuck ends?"
    $ mc.change_arousal(40)
    $ mc.change_locked_clarity(50)
    "You speed up, hitting the point of no return. You pull out from between her tits at the last second and fire your load off all over her chest."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "blowjob")
    "You fire wave after wave onto her breasts. When you finish, you look down at your incredible artwork."
    $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_person)
    mc.name "Fuck, that was amazing."
    the_person "Yes... incredible..."
    "Hah! You got her to admit it again."
    $ the_person.draw_person(position = "stand2")
    "[the_person.possessive_title!c] slowly stands up. A small drip of cum slowly oozes off the edge of one her breasts and onto the floor."
    the_person "I can't believe I just did that. Again."
    mc.name "It's okay. I'm sure it won't be that good EVERY time."
    the_person "I need to go..."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "You watch her disappearing down the hall."
    $ clear_scene()
    "You sigh. Maybe now she'll be able to accept that it is okay to be the submissive partner during sex once in a while?"
    "Either way, you are sure you'll hear about this soon."
    $ add_ashley_submission_titfuck_taboo_restore_action()
    # $ mc.schedule.new_event("ashley_submission_titfuck_taboo_restore_label", event_desc = "Ashley Submission Event", time_slot = mc.schedule.get_next_open_time_slot())
    $ ashley.event_triggers_dict["sub_titfuck_taboo_regen"] = True
    $ the_person.apply_planned_outfit()
    return

label ashley_submission_blowjob_label():  #140 obedience
    $ the_person = ashley
    $ mc.reset_arousal()
    if mc.is_at(ceo_office):
        "At the end of the day, you are working in your office, when someone enters your door."
        $ the_person.draw_person(emotion = "happy")
        "As you look up, you see [the_person.possessive_title] walking in."
    else:
        "It is the end of the day, so you swing by your office to pick up your daily serum dose."
        $ mc.change_location(ceo_office)
        $ the_person.draw_person(emotion = "happy")
        "As you open the door, you see [the_person.possessive_title] standing next to your desk."

    mc.name "Ah, hello [the_person.title]."
    the_person "Oh hey. I was just dropping off your serums for you. Have a good evening."
    if the_person.tits_visible:
        "[the_person.possessive_title!c]'s big tits are on full display for you. They heave a little with each breath and movement she makes."
    else:
        "You check her out. Her big tits seem to bounce enticingly with each movement she makes."
    "You've been having fun with her tits lately, and she notices you checking her out."
    the_person "Oh boy... I know that look."
    "She reaches up and gives her chest a couple heaves."
    the_person "Thinking about getting that meaty cock of yours between the girls again?"
    mc.name "Well, if I wasn't before, I certainly am now!"
    the_person "I'm up for that."
    "You pull your cock out from your pants."
    mc.name "Good, because I wasn't going to bother asking."
    if not the_person.tits_visible:
        the_person "Give me one moment."
        $ the_person.strip_to_tits()
        $ the_person.break_taboo("bare_tits")
        "She quietly strips down until her big tits spring free."
        mc.name "Damn. That never gets old."
    "[the_person.possessive_title!c] steps toward you, then drops to her knees."
    $ the_person.draw_person(position = "blowjob")
    $ the_person.change_arousal(20)
    "She reaches out and gives your cock a couple strokes with her hand. She spits into her hand then gives you a couple more strokes."
    "She spends several seconds getting your cock lubed up, then lets some of her saliva drop from her mouth down between her tits."
    the_person "Mmm, okay. Here we go..."
    "[the_person.title] slides your erection in between her soft, pillowy tit flesh and starts to move them up and down on you."
    $ mc.change_arousal(20) #20
    "She bites her lip as she looks up at you. [the_person.possessive_title!c] is finally servicing you the way a good employee should."
    "You are getting so turned on, a bit of pre-cum starts to drip from the tip. You decide it is time to push her boundaries a little bit further."
    mc.name "Hang on a second."
    "She stops."
    the_person "Yeah?"
    mc.name "Look how much you are turning me on."
    "You reach down and give yourself a firm stroke, gripping hard to squeeze as much pre-cum from the shaft as you can, it gathers on the tip."
    the_person "Yeah..."
    mc.name "Taste it. Taste how much you are turning me on."
    the_person "I... what? Are you serious right now?"
    mc.name "Of course I am. Go on now, just stick out your tongue."
    the_person "I don't want to taste... that!"
    mc.name "Sure you do. Go on now."
    "You put your hand on the back of her head. You don't force her, but you give a gentle pull toward your crotch."
    the_person "I... I guess..."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "[the_person.possessive_title!c] licks the tip of your cock, then quickly pulls back and closes her mouth, grimacing."
    $ the_person.draw_person(position = "blowjob", special_modifier=None)
    mc.name "There, see? Damn, that was hot. You liked that, didn't you?"
    the_person "No, not at all. That's gross."
    mc.name "Aww don't talk like that. You liked it, tasting my arousal. That's what happens when you turn a man on with those big tits of yours."
    "She looks up at you, realising what you are planning."
    the_person "Look, I licked it, can we just go back to my tits?"
    mc.name "Sure."
    "For a little bit, anyway. You think to yourself. You decide to go back to using her tits for a bit, until you have another sample of pre-cum to give her."
    "She seems relieved, and after adding a bit more saliva as lubricant, she happily wraps her tits around you and resumes pumping up and down."
    "You reach down and grab [the_person.title]'s tits. You hold them in place for her as she works them up and down."
    $ mc.change_arousal(20) #40
    "Her bust feels great as she strokes you, but you are filled with desire to take it one step further. You look down and see a long dribble of pre-cum leaking out the tip now."
    $ the_person.change_arousal(15)
    mc.name "Look, you did it again. Be a good girl and lick that up too."
    "She stops and glares up at you."
    the_person "Again? I already did it once..."
    mc.name "I know, and it felt amazing. Why don't you suck on the tip a little and make sure you get it all out this time."
    the_person "No way! I'll just lick it off again..."
    "Your subtle mind game has successfully shifted the goal again, making it seem like licking your pre-cum is a compromise."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "[the_person.possessive_title!c] leans forward and licks the tip again. Her tongue lingers a little longer this time, and her breath on your skin makes you twitch."
    mc.name "Mmm, wait, hang on, you missed some..."
    "She circles the tip with her tongue a couple times, looking for the pre-cum she missed. Then she pulls back again."
    $ the_person.draw_person(position = "blowjob", special_modifier=None)
    mc.name "Perfect. Let's keep going."
    "You grab her tits and lean forward, pushing yourself between them. You make sure to start before she has a chance to spit on you again."
    "[the_person.title] just holds still while you use her breasts, on her knees looking up at you."
    "It doesn't take long until the friction starts to build up from the lack of saliva. You let go of her tits and then put your hand on the back of her head."
    mc.name "Mmm, it is getting kind of dry. Just stick your tongue out for a bit."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    $ the_person.increase_blowjobs()
    "Surprisingly, she obediently opens her mouth and sticks out her tongue. Without giving her a chance to rethink it, you pull her head toward you."
    "Her eyes close when her tongue makes contact with the shaft. Her wet, slick tongue feels heavenly as you start to slide it up and down your hardness."
    $ the_person.change_arousal(15)
    the_person "Mmmf..."
    "Was... was that a moan? This is progressing better than you expected. She starts to move her head a bit now, moving her tongue side to side as you move your hips up and down."
    $ mc.change_arousal(20) #60
    "Fuck it feels so good. At one point the tip of your cock rubs against her cheek and a long strand of pre-cum connects it to you as you keep stroking yourself with her tongue."
    "You pull back and she opens her eyes, looking up at you."
    $ the_person.draw_person(position = "blowjob", special_modifier=None)
    mc.name "It's leaking again. Now be a good girl and..."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "Before you can finish the sentence, she leans forward and sucks the tip of your cock into her mouth."
    "Her tongue swirls around the tip several times, cleaning the tip of your pre-cum, then pulls back, her lips smacking."
    $ the_person.draw_person(position = "blowjob", special_modifier=None)
    the_person "You aren't going to settle for anything less than a blowjob, are you?"
    mc.name "Nope! Those lips feel amazing."
    "You put your hand on the back of her head again. She sighs."
    the_person "Fine, just this once!"
    mc.name "Yeah, yeah, of course..."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "[the_person.possessive_title!c] opens her mouth obediently and leans forward, sliding the tip of your cock past her red, pouty lips."
    $ mc.change_arousal(20) #80
    "At long last, you finally have [the_person.title] on her knees, servicing your cock with her mouth."
    "As she begins, she is surprisingly good at it. For someone who doesn't enjoy blowjobs, she sure is well practised..."
    if ashley.progress.lust_step >= 2:
        "Of course, she did this for you once before, but her sister was sitting across your desk from you, so the situation is a little different."
        mc.name "Damn. This is just as good as I remembered."
    else:
        mc.name "Damn. For someone who doesn't like to give head, you sure are good at it."
    "[the_person.title] doesn't respond, but just keeps bobbing her head up and down on your shaft."
    $ mc.change_arousal(25)
    $ the_person.change_arousal(10)
    "You feel a vibration in [the_person.possessive_title]'s throat. Did she just moan? Looking down, it definitely appears that she is enjoying herself, despite her protests."
    "After the stimulation of her tits, you can't last as long as you want. You feel yourself getting ready to cum."
    "You make a split second decision to really drive home her submission and to cum in her mouth."
    "Your hand is already on the back of her head, but now you run your fingers through her hair and grab a handful, keeping her head in place."
    mc.name "That's it... I'm gonna cum! Now take it all like a good little slut."
    if mc_serum_cum_serum_is_active():
        "She suddenly looks up at you. She obviously knows you are on a serum now that changes your cum's properties."
        "When she tries to pull off, you firmly keep her head in place. She glares at you but quickly realises it is no use."
    else:
        "She suddenly looks up at you. She doesn't want your cum in her mouth."
        "When she tries to pull off, you firmly keep her head in place. She glares at you but quickly realises it is no use."
    "You start to cum and quickly fill up [the_person.possessive_title]'s mouth with your seed. She coughs and sputters a bit."
    $ the_person.cum_in_mouth()
    $ the_person.draw_person(position = "blowjob", special_modifier=None)
    "Even after you finish, you hold her head in place for a couple extra seconds, savouring it."
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
    "When you let go, [the_person.title] gasps. You quickly order her before she can get a word in."
    mc.name "That was amazing. Now swallow."
    "She looks up at you, and for a moment, you see a hint of defiance. However, it quickly melts away."
    $ play_swallow_sound()
    "She makes a show of it, tipping her chin up as she swallows your load. A bit of your cum is dribbling down her face, but you decide to leave that alone for now."
    the_person "Fuck, you don't have to be so rough!"
    mc.name "I know, but you were enjoying it too much. I needed to make sure you understood that you were on your knees to service me."
    the_person "I... I wasn't enjoying it!"
    "She tries to deny it, but she can't hold your gaze and looks away."
    mc.name "[the_person.title]. It's okay. You can admit that you liked giving me a blowjob."
    the_person "I didn't like it! I hate giving blowjobs!"
    mc.name "Do you though? Do you really?"
    the_person "I mean... I guess maybe hate is the wrong word."
    $ the_person.increase_opinion_score("giving blowjobs")
    $ the_person.draw_person()
    "[the_person.possessive_title!c] stands up as she grapples with what just happened."
    mc.name "It's okay. Next time we will take it a little slower, so you can savour it a bit more."
    the_person "Next time? Yeah right! I need to go."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "You watch her disappearing down the hall."
    $ clear_scene()
    "Despite your progress, [the_person.possessive_title] appears to be resisting your commanding influence again."
    "You have a feeling you are going to hear about this event again from her."
    $ add_ashley_submission_blowjob_taboo_restore_action()
    $ ashley.event_triggers_dict["sub_blowjob_taboo_regen"] = True
    return

label ashley_submission_blowjob_taboo_restore_label(the_person = ashley):
    $ outcome_convince = False
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_blowjob_count", 0) == 0
    $ ashley.event_triggers_dict["sub_blowjob_count"] = ashley.event_triggers_dict.get("sub_blowjob_count", 0) + 1
    $ the_person.draw_person(emotion = "angry")
    $ ashley.event_triggers_dict["sub_blowjob_taboo_regen"] = False

    "[the_person.possessive_title!c] gives you a curt nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "No. It's not."
        the_person "First with my tits... and now with my mouth!"
        the_person "I know what you're doing now, and I'm not going to fall for it."
        the_person "I'm not just another slut for you to keep around to suck your cock whenever you want!"
        if ashley.progress.lust_step >= 2:
            mc.name "You didn't seem to mind it the other day, when your sister was in my office."
            the_person "That was different! You know I was just trying to make it hell for you to talk to her."

    else:
        the_person "No? It isn't?"
        the_person "We already had this talk... but you seem to have forgotten."
        the_person "I'm not just a slut here to suck you off whenever you please, okay?"

    mc.name "Are you saying you don't like meeting up after work once in a while?"
    the_person "No... I'm not saying that. I'm just saying that I'm not going to stay late just to fulfil your crazy fantasies."
    if the_person.opinion.giving_blowjobs == 2:
        mc.name "[the_person.title], last time I got you on your knees to suck my cock, you were moaning practically non-stop."
        mc.name "When you started touching yourself, I wasn't sure who was going to finish first, me or you!"
        "She stutters her rebuttal."
        the_person "I didn't say I don't enjoy it, I just mean... blowjobs are great, if I'm getting some action too!"
        the_person "But I'm not here to just... drop to my knees and take your thick, meaty cock down my throat anytime it suits your fancy..."
        "She bites her lip as her voice trails off."
        if mc.is_at(ceo_office):
            mc.name "You would get down on your knees and do it again right now, wouldn't you?"
        else:
            mc.name "You would go with me to my office and do it again right now, wouldn't you?"
        "[the_person.title] looks away, her resistance melting."
    elif the_person.opinion.giving_blowjobs == 1:
        mc.name "I find that hard to believe. [the_person.title], last time you were really getting into it. I daresay you've come to enjoy it."
        "She gives a quick rebuttal."
        the_person "I'm not saying I don't enjoy giving a blowjob now and then!"
        the_person "What I'm saying is that I'm not just here for you to use my mouth whenever you please, okay?"
        mc.name "If you say so..."
    else:
        mc.name "That's fair, but I just want you to admit it. Giving me a blowjob wasn't as bad as you thought it was going to be. Was it?"
        the_person "It was... an experience."
        mc.name "A pleasant one."
        the_person "It was okay."
        "[the_person.title] retains a bit of her resistance."

    $ attempts = 3 - the_person.event_triggers_dict.get("sub_blowjob_count", 0)
    $ the_choice = "Get on your knees" if mc.is_at(ceo_office) else "Let's go to my office"

    menu:
        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_blowjob_count", 0) >= 3:
            mc.name "If it needs to stop, why does it keep happening [the_person.title]?"
            mc.name "Let's stop pretending. You love going down on me. Especially at the end when I fill your mouth with cum and you swallow every last drop."
            mc.name "Frankly, I don't understand what the problem is? Just admit that you like it. It's okay..."
            "[the_person.possessive_title!c] seems like she wants to argue, but even she can understand you're right."
            the_person "Fine. But just because I'm willing to suck you off once in a while, doesn't make me one of your air headed sluts, okay?"
            mc.name "I never said you were."
            $ outcome_convince = True
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title!c] turns and walks back to her desk."

        "But it keeps happening...\n{menu_red}Requires: [attempts] more submissive blowjobs{/menu_red} (disabled)" if ashley.event_triggers_dict.get("sub_blowjob_count", 0) < 3:
            pass

        "[the_choice]" if ashley.opinion.giving_blowjobs == 2:
            if not mc.is_at(ceo_office):
                mc.name "Come on. Let's go to my office and settle this."
                the_person "Umm... Okay..."
                $ mc.change_location(ceo_office)
                "You escort her to your office, then lock the door after you both enter."

            mc.name "Alright, so... what is it you said before? You aren't here to drop to your knees and take my thick, meaty cock anytime it suits my fancy?"
            the_person "Right... that is what I said."
            mc.name "Did you mean it though? I mean..."
            "You undo your zipper and pull out your dick."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(30)
            mc.name "You really DID seem to enjoy it. Maybe you should try it one more time. Just to make sure that is how you feel."
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title!c] is already getting down on her knees. Her resistance is crumbling."
            "Her eyes are fixed on your crotch. She bites her lip and moves closer, inch by inch."
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            $ the_person.increase_blowjobs()
            "Her tongue slithers out and swirls around your testicles, before she slides her mouth up the shaft, her tongue now swirling around the tip."
            "[the_person.title]'s eyes look up and meet yours in a fleeting moment of recognition, as she realises she is passing the point of no return."
            "She sighs and then envelops the tip of your penis between her lips, sliding them down the shaft in sweet victory."
            "Her skilful mouth is yours to use as your cocksleeve, whenever you please."
            "[the_person.possessive_title!c]'s head begins to bob up and down, accompanied by sweet sounds of slurps and sighs."
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(30)
            "She really is enjoying this! It has taken a while to get her to this point, but your obedient employee is now dedicated to making you cum."
            "You put your hand on her head, controlling the pace while she continues to slurp and moan happily sucking you off."
            "You feel yourself getting ready to cum, but you want to make a point, so you pull her back from your cock for a moment."
            $ the_person.draw_person(position = "blowjob", special_modifier=None)
            mc.name "So, [the_person.title]. Can I count on you to drop to your knees, and take my thick, meaty cock, anytime I want it?"
            "It takes her a moment, but she agrees."
            the_person "I... I will..."
            mc.name "And you'll take my cum, wherever I tell you to? Be it on your face, on your tits, or down your throat?"
            the_person "Yes [the_person.mc_title]."
            $ the_person.change_obedience(3)
            mc.name "Good. Today I want it down your throat. Here it comes!"
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "Before she can respond, you pull her face back down on your cock. You easily slide into her mouth and down into her throat."
            mc.name "Mmm, that's it. Here it comes!"
            $ play_gag_sound()
            "She gags a little as you start to cum, but obediently takes it down her throat and straight into her stomach."
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            $ mc.change_locked_clarity(30)
            $ play_gag_sound()
            "She gags again, and this time a little bit of cum escapes from the corners of her mouth."
            "After you finish, you hold her head in place for a couple extra seconds, savouring it."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            $ play_swallow_sound()
            "When you let go, [the_person.title] gasps for air, but doesn't complain."
            mc.name "Good. I'm glad we could come to an understanding. Now get yourself back to work."
            $ the_person.draw_person()
            the_person "Yes sir."
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title!c] stands up and leaves you alone in your office."
            $ outcome_convince = True
            $ the_person.increase_opinion_score("being submissive", max_value = -1) # remove hate from submissive only

        "[the_choice]\n{menu_red}Requires Ashley Loves Blowjobs{/menu_red} (disabled)" if ashley.opinion.giving_blowjobs != 2:
            pass


        "Understood":
            mc.name "I understand. You have boundaries and I won't cross them again without approval."
            "She looks at you suspiciously, but ultimately accepts your proposal."
            the_person "Alright. Let's just not have this talk again, okay?"
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title!c] turns and walks back to her desk."

    if outcome_convince:
        "[the_person.title] is willing to suck you off once in a while. You feel like you are finally tapping into her submissive side."
        "You can't wait. You know it is just a matter of time until she is willing to go even further..."
        "How far can you push her? You envision [the_person.possessive_title] bent over your desk, ass in the air, begging for your cum to fill up her quivering pussy."
        "You are certain it is just a matter of time."
        $ ashley_story_path_submission.next_step(ashley, step_index = 1)
    else:
        "[the_person.title] isn't willing to make this a regular thing yet. You wonder if you can get her to be obedient if you could give it another shot..."
    $ the_person.apply_planned_outfit()
    $ clear_scene()

    return

label ashley_work_blowjob_label(the_person):
    "You look at [the_person.possessive_title]. You feel the time is right to push her obedience boundary again."
    mc.name "Hey, can you come with me to my office? I have something I need to talk to you about in private."
    the_person "Sure..."
    $ mc.change_location(ceo_office)
    "[the_person.possessive_title!c] follows you to your office. After you enter, you close and lock the door behind you."
    the_person "So... what was it you needed?"
    "You decide to get straight to the point."
    mc.name "I need some relief. In a way that only you can provide."
    the_person "Ah, I wondered if you were going to make it all the way through the workday today..."
    $ the_person.draw_person(position = "kneeling1")
    "[the_person.title] gets down on her knees as she teases you."
    the_person "I guess not!"
    if not the_person.tits_visible:
        "She smiles up at you as she pulls her top off."
        $ the_person.strip_to_tits(position = "kneeling1")
        $ the_person.break_taboo("bare_tits")
        "Her amazing tits spill free from their prior confines."
    "You step over to her while pulling your cock free from your trousers."
    if the_person.opinion.giving_blowjobs < 1:
        the_person "You remember the deal right? Just my tits..."
        mc.name "Yeah, of course."
        "You kind of feel bad. You remember that is the deal, but of course you have no intention of honouring it."
        the_person "It just needs a bit of lubrication..."
        "She gathers a bunch of saliva, then lets it drop out of her mouth and down between her tits."
        "She does it again, this time letting it fall on your cock. She uses her hand to spread it up and down your shaft."
    else:
        "She looks at your cock and bites her lip."
        the_person "No... no blowjobs... remember?"
        mc.name "Yeah, of course."
        the_person "It just... needs some lubrication..."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "She leans forward and starts to run her lips and tongue up and down your shaft, coating it with saliva."
        "You just watch as [the_person.possessive_title] gets your shaft lubed up... and then keeps going, licking your cock all over."
        "At one point she even licks to the base of your shaft and down to your testicles."
        $ the_person.change_arousal(10) #10
        "Her eyes are closed and she gives a little moan. You decide to say something."
        mc.name "I think you got it."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        "[the_person.title] suddenly snaps her eyes open."
        the_person "Ah! Umm... right..."
    "[the_person.possessive_title!c] leans forward and slides your well lubricated cock between her tits."
    "She is well practised, and starts to bounce her tits up and down, eager to please you."
    $ mc.change_arousal(20) #20
    "It isn't long until the first drops of pre-cum start to form at the tip of your cock. It is time to begin the mind games."
    "You put your hand on her shoulder and stop her eager bouncing for a moment."
    mc.name "Look at how much you are turning me on again."
    "[the_person.title] looks down and sees the pre-cum dribbling out the tip of your erection."
    $ the_person.increase_blowjobs()
    if the_person.opinion.giving_blowjobs < 1:
        mc.name "Go ahead, taste it."
        "[the_person.possessive_title!c] sighs. She clearly knows what you are angling for again, but decides to play along."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "She opens her mouth and sucks in the tip of your cock. She swirls her tongue around the head, tasting your pre-cum."
        "She does this for several seconds, then pulls off with a slight grimace."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        mc.name "You are getting used to the taste, aren't you?"
        the_person "I guess... although I really shouldn't {i}have{/i} to!"
        $ the_person.increase_opinion_score("giving blowjobs")
        mc.name "I mean sure, you don't {i}have{/i} to. But you {i}want{/i} to, don't you?"
        the_person "I... I mean... there are worse things in the world."
        "You put your hand on the back of her head."
        mc.name "Here, I think you missed some. Open up."
        "Her resistance fades, and she obediently opens her mouth again, allowing you to pull her head back to your crotch."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    else:
        mc.name "Go ahead, ta..."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "Before you can even finish the command, [the_person.possessive_title] leans forward and opens her mouth, taking your cock."
        $ play_swallow_sound()
        "She eagerly bobs her head up and down several times. She even gives a little moan as she dutifully sucks and swallows your pre-cum."
        $ play_moan_sound()
        "She gives another moan. A bit louder this time. You look down... is she touching herself?"
        $ the_person.change_arousal(20) #30
        "She definitely has a hand between her legs now. She's lost all pretense of resistance and is now eagerly sucking you off."
        mc.name "Damn, you're really getting into this. You've really grown to love sucking me off, haven't you?"
        $ the_person.increase_opinion_score("giving blowjobs")
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        the_person "It is so hot... it just turns me on so much... I can't help it!"
        "You lift her chin with your finger, looking her in the eyes."
        mc.name "Just say it. Just tell me you love sucking me off."
        the_person "I do! I love sucking your cock, [the_person.mc_title]!"
        mc.name "Good. Now ask me if you can give me a blowjob."
        the_person "[the_person.mc_title]... can I please suck your cock?"
        mc.name "Like you mean it."
        the_person "[the_person.mc_title]! Please! Please let me suck your amazing cock and swallow all your cum!"
        mc.name "Do it."
        "[the_person.possessive_title!c] immediately dives in. She opens her mouth and eagerly starts slurping up and down your manhood."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    $ mc.change_arousal(20) #40
    "[the_person.title]'s head bobs up and down on your dick, the blowjob beginning in earnest now."
    "You savour the sensations of the busty girl, servicing you obediently with her mouth."
    "Her soft lips give you shivers as they stroke your length repeatedly."
    mc.name "Fuck, your mouth is incredible."
    "You reach forward with both hands and cup her big tits. They feel soft and hot to the touch."
    "You keep your touch light for now, but grasp both of them. She sighs as you enjoy feeling her up."
    $ the_person.change_arousal(20) #50
    "She gives a little yelp when you pinch her nipples at the same time."
    $ the_person.draw_person(position = "blowjob", special_modifier=None)
    the_person "Ah! You're always so rough..."
    mc.name "You like it rough though, don't you?"
    "She falls silent. She won't admit it, but you can tell you are turning her on."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    $ mc.change_arousal(20) #60
    if the_person.opinion.giving_blowjobs < 2:
        "[the_person.possessive_title!c]'s talented mouth is really working you over. You just stand there and let her work you over."
        "You decide to talk dirty to her for a bit."
        mc.name "Damn, you really DO know how to give good head. You're gonna have me cumming in no time."
        mc.name "Can't wait to watch you swallow all your boss' cum, like a good employee."
        "She rolls her eyes for a moment, but doesn't stop sucking or licking you with her nimble tongue and mouth."
        $ mc.change_arousal(20) #80
        "[the_person.title]'s hot mouth is making your toes curl. Stroke after stroke of pleasure is building pressure towards your release."
        "You decide not to take any chances and put your hand on the back of her head."
        "She looks up at you, recognising how close you are getting to orgasm."
        "[the_person.possessive_title!c] closes her eyes and speeds up, eager to finish you off."
        if mc_serum_cum_serum_is_active():
            "If she remembers that you have a serum actively influencing your cum, she doesn't make it apparent."
        $ mc.change_arousal(30) #110
        mc.name "Fuck, I'm about to cum!"
        "You keep a hand on the back of [the_person.title]'s head to make it clear you want her to keep sucking. She keeps blowing you until you tense up and start to pump your load out into her mouth."
        "[the_person.possessive_title!c] stops when she feels the first wave of your cum erupt into her mouth."
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "blowjob")
        $ play_gag_sound()
        "[the_person.title] gags once, but otherwise dutifully takes your load in her mouth. When you finish, she pulls back, her lips leaving your skin with a smack."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
        mc.name "Fuck, that was amazing."
        $ play_swallow_sound()
        "[the_person.title] just moans her approval as she swallows your cum."
        if mc_serum_cum_serum_is_active():
            "As she swallows, her eyes suddenly open."
            the_person "Oh fuck... I forgot... Oh not again..."
        else:
            "As she swallows, her eyes suddenly open and look up at you."
            the_person "Oh fuck... not again...."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title!c] slowly stands up. A small drip of cum slowly oozes off the edge of her chin and onto the floor."
        the_person "I can't believe I just did that. Again."
        mc.name "It's okay. I'm sure it won't be that good EVERY time."
    else:
        "You watch in awe as the stubborn employee moans and gasps as she sucks you off with gusto."
        "Her hand is between her legs as she stimulates herself, getting herself off as she works you over."
        mc.name "Damn, look at you go. Who is going to cum first, I wonder?"
        "She pulls off for a moment, looking up at you."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        the_person "You are."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "Without breaking eye contact, [the_person.title] takes the head of your dick in her mouth and slowly slides down it..."
        "You just watch as the shaft slowly disappears into her gullet, inch by inch, until her nose pushes against your pubic bone."
        $ mc.change_arousal(25) #85
        mc.name "Oh FUCK. You've been practising, haven't you?"
        "[the_person.possessive_title!c] gives you a sly wink, your cock completely engulfed by her throat."
        "She closes her eyes and starts to give you long, slow strokes, each time taking your entire length into her throat."
        $ the_person.change_arousal(20) #70
        "You can see between each thrust, her hand is working hard between her legs. Her moans rumble all around your dick."
        "Instinctually you put your hand on the back of her head."
        mc.name "Fuck, when I cum, it's going to go straight down your throat."
        $ the_person.change_arousal(20) #90
        $ play_moan_sound()
        "She moans loudly. She is definitely going to get off, but time is up. You are going to finish first."
        $ mc.change_arousal(35) #120
        "[the_person.possessive_title!c]'s throat wrapped around your cock is pushing you past the point of no return. You get ready to cum."
        mc.name "Oh fuck! Get ready!"
        "You use your hand on the back of [the_person.title]'s head to pull her close, pushing your cock as deep down her throat as you can manage."
        "You grunt and twitch as you start to empty your balls right into her stomach."
        $ play_gag_sound()
        "[the_person.possessive_title!c] closes her eyes and holds still as you climax. You feel her throat spasm a few times as she struggles to keep your cock in place."
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "As you finish, her moaning crescendos. You watch as her legs start to twitch as she finishes masturbating."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
        mc.name "That's it, cum for me you little slut!"
        $ the_person.have_orgasm(force_trance = True)
        "Even though you are finished, [the_person.title] keeps herself in place with your cock down her throat as she cums."
        "After several more seconds, she slowly pulls off you, gasping for air."
        mc.name "[the_person.title]... holy shit."
        the_person "Ahh!... Gahh... I... I told you... you first!"
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title!c] slowly stands up, her legs a bit wobbly. A small drip of cum slowly oozes off the edge of her chin and onto the floor."
        "She looks at you and frowns."
        mc.name "Don't tell me you don't want to do that again. You CAN'T tell me that. That was amazing."
        the_person "I... it was... I..."
        "She looks conflicted. She knows she is falling more and more under your command, but she also loves it."
    the_person "I need to go..."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "You watch her disappearing down the hall."
    $ clear_scene()
    "You sigh. Maybe now she'll be able to accept that it is okay to be the submissive partner during sex once in a while?"
    "Either way, you are sure you'll hear about this soon."
    $ add_ashley_submission_blowjob_taboo_restore_action()
    $ the_person.apply_planned_outfit()
    $ ashley.event_triggers_dict["sub_blowjob_taboo_regen"] = True
    return

label ashley_submission_fuck_label(): #160 obedience
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_fuck_count", 0) == 0
    if mc.is_at(ceo_office):
        "At the end of the day, you are working in your office, when someone enters your door."
        $ the_person.draw_person(emotion = "happy")
        "As you look up, you see [the_person.possessive_title] walking in."
    else:
        "It is the end of the day, so you swing by your office to pick up your daily serum dose."
        $ mc.change_location(ceo_office)
        $ the_person.draw_person(emotion = "happy")
        "As you open the door, you see [the_person.possessive_title] standing next to your desk."
    mc.name "Ah, hello [the_person.title]."
    the_person "Oh hey. I was just dropping off your serums for you."
    if the_person.tits_visible:
        "[the_person.possessive_title!c]'s big tits are on full display for you. They heave a little with each breath and movement she makes."
    else:
        "You check her out. Her big tits seem to bounce enticingly with each movement she makes."
    $ mc.change_locked_clarity(30)
    "She chuckles as you check her out. She looks down at your crotch and licks her lips."
    the_person "In need of anything else... while I'm here?"
    "Something about the way she smiles at you, within the context of being alone with her in your office yet again sparks your arousal."
    mc.name "You know, I think I COULD use something else. Care to lock the door?"
    the_person "On it!"
    $ the_person.draw_person(position = "walking_away")
    "When she turns away from you to go lock the door, your eyes are immediately drawn to her backside."
    $ mc.change_locked_clarity(30)
    "The way it wiggles back and forth with each step has you enchanted."
    "You stand up and start to walk around your desk when she finishes locking your door and turns around, walking back to you."
    $ the_person.draw_person(emotion = "happy")
    the_person "Mmm, I've been thinking about swallowing your meaty cock all day..."
    "She starts to get down on her knees, but you stop her."
    mc.name "I'm sure you have been, slut, but I want to have some different fun with you for now."
    the_person "Oh? Okay, what can I.... AH!"
    $ the_person.draw_person(position = "standing_doggy")
    "You quickly turn her around and bend her over your desk, sticking her ass out towards you."
    the_person "Hey... what... what are you doing?"
    if the_person.vagina_available and the_person.vagina_visible:
        "Her bare ass sticking out is practically begging for your attention."
    else:
        "You quickly pull away the clothes between you and her ass."
        $ the_person.strip_to_vagina(prefer_half_off = False, position = "standing_doggy")
        "Once her ass is bare, it is practically begging for your attention."
    "You run your hand along her ass cheek, down the back of her thigh, then between her legs you move it back up, sliding a finger along her slit."
    the_person "Ahhh, mmm..."
    $ the_person.change_arousal(10)
    "She moans as you push a finger inside of her. Her pussy moistens with each stroke as you gently thrust in and out of her with your finger."
    "You give her a few moments, then push in another finger."
    $ the_person.change_arousal(15)
    the_person "Aaaahhhh, that's nice. If you want a taste, let me lay back on your desk..."
    "As tempting as it is to bury your face in her sweet cunt, you have other plans."
    mc.name "That won't be necessary, I've almost got you warmed up."
    the_person "Wa... warmed up?"
    "She shifts her weight a bit, but you grab her hip with your free hand."
    the_person "I... could ride you, you could sit on your chair... AH!"
    "*SPANK*"
    "You give her ass a solid spank, eliciting a startled cry from her. Her ass shakes pleasingly."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(-5)
    mc.name "[the_person.title], you worked so hard today, no need to do that. I can take care of things, no need for you to work for it."
    "You reach down and start to take off your pants."
    the_person "Oh, don't be silly, I don't mind..."
    "Your cock springs free. You take it in one hand and use to give her ass a couple playful spanks."
    "She tries to move again but you grab her hips with both hands, holding her in place."
    the_person "[the_person.mc_title], I'm not some kind of animal for you just bend over your desk and..."
    "You move up closer behind her. You slide your cock between her legs, rubbing up against her pussy but not inside it."
    the_person "Ohhhh my god..."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20)
    "With your hands firmly on her hips, you thrust yourself against her. You can feel her heat and arousal as you slide yourself along her cunt."
    mc.name "Let's be honest with each other here, [the_person.title]. Sometimes, you really are a bitch. It is only fair that once in a while, someone treats you like one."
    "She refuses to respond to your statement, but she begins pushing her ass back against you, rubbing herself harder against your cock."
    mc.name "I can tell you want it. Don't you?"
    "She looks back at you, but refuses to say a word. Her body, however, is beginning to quiver a bit as she gets more and more aroused."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(10)
    mc.name "I'll tell you what, I'll even make this easy for you. You don't even have to say a word."
    mc.name "Just reach down between your legs, take my cock in your hand, and point it where you want it to go."
    mc.name "We both know you want this, the sooner you give in, the sooner you can feel my cock, filling you up."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20)
    "Her entire body shudders at your words. She looks back at you again, this time her eyes betray her arousal, she lets out a gasp of pleasure."
    "She pushes herself against you harder, but you both know that she is just teasing herself."
    "After several more seconds, she finally stops. You feel her body slowly shift upward as she pushes up onto her toes, and she reaches down with one hand between her legs."
    "You pull away a couple inches from her, giving her space as she wraps a hand around your cock."
    "She gives it a couple strokes with her hand, then carefully points it down at her vagina."
    "Your hands still on her hips, you slowly push yourself forward, your bare cock sliding inside of [the_person.possessive_title]'s eager cunt."
    the_person "Ohhhh fuuuuck..."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    "She is so turned on, you slide inside of her easily. One steady stroke is all it takes to bury yourself."
    mc.name "Like a bitch in heat? With pleasure."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    "With your hands planted firmly on her hips, you don't waste any time."
    "The sounds of your hips clapping against her ass soon fills the room as you start to fuck her."
    "Her moans of pleasure aren't far behind."
    $ play_moan_sound()
    mc.name "Damn, you are REALLY enjoying this. I'm pretty sure you are gonna cum first this time."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    the_person "Shut up and just... have your fun!"
    mc.name "I think you mean OUR fun?"
    mc.name "Sex doesn't have to be one sided. We can fuck and BOTH enjoy it, you know?"
    $ play_spank_sound()
    "You give her ass a spank, illiciting another moan from [the_person.possessive_title]."
    $ play_moan_sound()
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    mc.name "See? You can't tell me you aren't enjoying this also."
    "[the_person.title] doesn't respond but her moans are getting desperately urgent."
    "You can feel her getting close to orgasm, so you give her one last thrust, pushing yourself deep inside of her, then stop."
    the_person "That's so good... Wait... What? Why did you stop? Nooooo!"
    "She tries to thrust herself back against you, but you grab her hips forcefully and pin her to your desk."
    mc.name "What was that? Was there something you wanted?"
    the_person "You! You know..."
    mc.name "I know what? I think I know what you want, but you'd probably better tell me."
    "She looks back at you, but instead of anger in her eyes, it is only pleasure and need."
    the_person "PLEASE. Don't stop like that..."
    mc.name "Don't stop what?"
    the_person "FUCK ME! FUCK ME PLEASE! I want you to fuck me and don't stop until... AHH!"
    $ play_moan_sound()
    "You suddenly resume pounding [the_person.possessive_title]'s pussy, causing her words to die out in her throat."
    "Moments later, she is crying out in orgasm."
    $ the_person.have_orgasm()
    the_person "YES! OH YES [the_person.mc_title]! FUCK ME!"
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(20)
    "Watching [the_person.title] cum all over your cock sends you over the edge as well."
    "Since she is still in the throes of her own orgasm, you don't bother to warn her that you are getting close also."
    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside her":
        "Taking [the_person.title]'s pussy, bent over your desk like this at long last is incredible."
        "You decide to mark your territory, claiming her pussy with your seed."
        "With one final thrust, you push yourself deep inside of her and start to cum."
        $ the_person.cum_in_vagina()
        $ climax_controller.do_clarity_release(the_person)
        $ the_person.draw_person(position = "standing_doggy")
        "Her pussy is quivering from her own orgasm when you start to cum inside of her."
        "You pin her to the desk and fill her with your seed, marking [the_person.possessive_title] as your personal cum slut."
        "When finish, you slowly pull out and look down. Your seed is dripping down the inside of her legs."
        the_person "Oh god..."
        "[the_person.title] starts to try to stand up, but with her weak legs, you easily keep her pinned to the desk."
        the_person "Ohh... [the_person.mc_title]?"
        mc.name "Just one second..."
        "You quickly grab your phone and snap a picture. Your seed is clearly dripping from her cunt and you can see her surprised face in frame."
        the_person "Oh shit..."

    if the_choice == "Cum on her ass":
        "Taking [the_person.title]'s pussy, bent over your desk like this at long last is incredible."
        "You decide to mark your territory, pulling out of her at the last moment."
        $ the_person.cum_on_ass()
        $ climax_controller.do_clarity_release(the_person)
        $ the_person.draw_person(position = "standing_doggy")
        "You stroke yourself as you start to cum all over [the_person.possessive_title]'s ass. She barely notices, in the final stages of her own orgasm."
        "You spurt several waves of cum all over her, marking her as your personal cum slut."
        "When finish, you look down at her, marveling at your artwork."
        the_person "Oh god..."
        "[the_person.title] starts to try to stand up, but with her weak legs, you easily keep her pinned to the desk."
        the_person "Ohh... [the_person.mc_title]?"
        mc.name "Just one second..."
        "You quickly grab your phone and snap a picture. Her ass is covered with your seed and you can see her surprised face in frame."
        the_person "Oh shit..."


    mc.name "See? We can both get what we want. There's nothing wrong with bending over and letting me do what I want with you."
    the_person "I'm not an animal, I'm..."
    mc.name "You're a woman. Just because it is called 'doggy style' doesn't mean you have to be an animal to do it."
    mc.name "Any position can be amazing if you go into it with the right person."
    $ the_person.increase_opinion_score("doggy style sex")
    $ the_person.increase_opinion_score("showing her ass")
    the_person "I guess..."
    mc.name "Anyway, thanks for the relief. I really needed that! There are some wipes in my desk if you need them to cleanup."
    "You quickly get dressed. [the_person.title] slowly gets up."
    $ the_person.draw_person(position = the_person.idle_pose)
    mc.name "I bet next time I could make you cum more than once."
    the_person "Next time? Yeah right! I need to go."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "She disappears out of your door."
    $ clear_scene()
    "Finally, you've claimed [the_person.possessive_title] in your office, but you can tell she isn't going to do it again without some work."
    "You imagine you are going to have a chat about this soon."
    # Restore these lines when continue story
    $ add_ashley_submission_fuck_taboo_restore_action()
    $ ashley.event_triggers_dict["sub_fuck_taboo_regen"] = True

    return

label ashley_submission_fuck_taboo_restore_label(the_person = ashley):
    $ outcome_convince = False
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_fuck_count", 0) == 0
    $ ashley.event_triggers_dict["sub_fuck_count"] = ashley.event_triggers_dict.get("sub_fuck_count", 0) + 1
    $ the_person.draw_person(emotion = "angry")
    $ ashley.event_triggers_dict["sub_fuck_taboo_regen"] = False
    "[the_person.possessive_title!c] gives you a curt nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "Seriously? Is everything alright?"
        the_person "You don't have any limits do you? I'm not just some cum-hungry slut for you to bend over every time you get a hard on!"
    else:
        the_person "No? It isn't?"
        the_person "We already had this talk... but you seem to have forgotten."
        the_person "I'm not just a slut here to bend over and take your cock whenever you feel like it, okay?"

    mc.name "Are you saying you don't like it when I bend you over, pin you to my desk and make you cum all over my cock?"

    if ashley.opinion.doggy_style == 1:
        $ the_person.change_arousal(10)
        "You notice a twinge of blush appear in [the_person.possessive_title]'s cheeks as tries to stutter out her rebuttal."
        the_person "No... I'm not saying that. I'm just saying that I'm not going to stay late just to fulfil your crazy fantasies."
    elif ashley.opinion.doggy_style == 2:
        $ the_person.change_arousal(20)
        "You notice her blush and [the_person.possessive_title] tries to stutter out her rebuttal."
        the_person "No! I mean, it can be fun but... But it isn't right when..."
        "Her voice trails off, she can't even refuse it anymore."
    else:
        the_person "Exactly. I don't mind screwing around once in a while, but I'm not your little sub for you to do anything you want to!"
        mc.name "Could have fooled me when you seem so eager to get on your knees for me..."
        the_person "That's different. I have agency during blowjobs, but when you bend me over your desk it is so humiliating."
        "You roll your eyes for a moment. She is stubbornly holding on to her ego."

    $ attempts = 3 - the_person.event_triggers_dict.get("sub_fuck_count", 0)
    $ the_choice = "Bend Her Over Now" if mc.is_at(ceo_office) else "Let's go to my office"

    menu:
        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_fuck_count", 0) >= 3 and ashley.opinion.doggy_style != 2:
            mc.name "If it needs to stop why does it keep happening [the_person.title]? You aren't bending over my desk on accident."
            mc.name "Let's stop pretending. You love it when I bend you over and I have my way with you."
            mc.name "Frankly, I don't understand what the problem is? It is completely natural for a woman to enjoy submitting to a strong male figure in that way."
            "[the_person.possessive_title!c] pouts for a moment, but even she can understand you're right."
            the_person "Fine. Please just... maybe we can keep this between you and me, okay? I don't want Steph to find out."
            mc.name "Sure. This will be our little secret."
            $ outcome_convince = True

        "But it keeps happening...\n{menu_red}Requires: [attempts] more submissive fucks{/menu_red} (disabled)" if ashley.event_triggers_dict.get("sub_fuck_count", 0) < 3:
            pass

        "[the_choice]" if ashley.opinion.doggy_style == 2:
            if not mc.is_at(ceo_office):
                mc.name "Come on. Let's go to my office and settle this."
                the_person "Mmmmm... Okay..."
                $ mc.change_location(ceo_office)
                "You escort her to your office, then lock the door after you both enter."

            mc.name "Alright, so... what is it you said before? You aren't here to bend over my desk and take my cock any time I want?"
            the_person "Right... that is what I said."
            "You step behind her. With the gentlest of nudges, you push her up against your desk."
            "With your hands on her hips, you start to grind your cock against her ass."
            mc.name "But is that what you meant?"
            $ the_person.change_arousal(20)
            mc.name "Be honest. You want to do it right now, don't you?"
            mc.name "Having me bend you over gets you off, doesn't it? I bet if we were both naked, you'd be so wet I could just slide right in..."
            "You run your hands up and down her body, then grope her tits. Her body is grinding back against you."
            $ the_person.change_arousal(20)
            "The last of her will crumbles when you slide a hand down between her legs."
            $ the_person.draw_person(position = "standing_doggy")
            "Without even realizing it, she bends over your desk, desperate for a better angle to grind her pussy against your erection."
            mc.name "Fine. You don't have to answer. But I'm a man of science, so I'm going to do an experiment."
            if not (the_person.vagina_available and the_person.vagina_visible):
                mc.name "Let's just get this out of the way..."
                $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = False)
                "You strip her down, exposing her backside."
            "You quickly pull your cock out, then line it up with her cunt."
            "You can feel the heat and humidity of her arousal against your crotch before you even make contact."
            "With one push, you slide yourself inside of [the_person.possessive_title]'s eager pussy once again."
            $ play_moan_sound()
            $ mc.change_locked_clarity(50)
            $ the_person.change_arousal(20)
            $ mc.change_arousal(10)
            mc.name "Damn! You're practically dripping. Can we please just stop with the fake ego bullshit now?"
            the_person "Fine! Just... fuck me good... please?"
            mc.name "It's about time. Alright, let's do this."
            # NOTE: Do this in long form later, for now use the sex system.
            call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_ashley_sub_01
            $ the_person.draw_person(position = "standing_doggy")
            "When you are finished, you step back from [the_person.title]."
            mc.name "Are you done being difficult now? We both clearly enjoy it."
            the_person "Fine. Please just... maybe we can keep this between you and me, okay? I don't want Steph to find out."
            mc.name "Sure. This will be our little secret."
            $ outcome_convince = True
            mc.name "Take your time cleaning up, I'm going to get back to work now."
            $ clear_scene()
            "You step out of your office, leaving [the_person.possessive_title] to recover and clean up."


        "[the_choice]\n{menu_red}Requires Ashley Loves Doggy Style{/menu_red} (disabled)" if ashley.opinion.doggy_style != 2:
            pass


        "Understood" if ashley.opinion.doggy_style != 2:
            mc.name "I understand. But if you bend over my desk again, I can't promise I'll be able to resist having my way with you."
            "She bites her lip, but nods her agreement."
            the_person "Right. We'll just keep things from getting that serious again."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks back to her desk."

    if outcome_convince:
        # this will unlock her for now remove when continue story
        $ ashley.event_triggers_dict["sub_fuck_avail"] = True
        $ ashley.event_triggers_dict["sub_anal_avail"] = True
        $ ashley_story_path_submission.next_step(ashley, step_index = 0)
        "You've finally gotten [the_person.title]'s submissive side trained. She's willing to let you bend her over your desk after work is closed for the day once in a while."
        "You wonder to yourself... is this really the end of the road for her submission training? She still has one forbidden hole you haven't plundered yet..."
    else:
        "[the_person.title] isn't willing to make this a regular thing yet. You wonder if you can get her to be obedient if you could give it another shot..."
    return

label ashley_work_fuck_label(the_person):
    "You look at [the_person.possessive_title]. You feel the time is right to push her obedience boundary again."
    mc.name "Hey, can you come with me to my office? I have something I need to talk to you about in private."
    the_person "Sure thing, [the_person.mc_title]"
    $ mc.change_location(ceo_office)
    "[the_person.possessive_title!c] follows you to your office. After you enter, you close and lock the door behind you."
    the_person "So... what was it you needed?"
    "You decide to get straight to the point."
    mc.name "I need some relief. In a way that only you can provide."
    the_person "Ah, I wondered if you were going to make it all the way through the workday today..."
    "She starts to get down on her knees, but you stop her."
    mc.name "Hang on, before you get on your knees, I want to see that amazing ass of yours."
    if the_person.opinion.showing_her_ass > 0:  #She eagerly bends over
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title!c] eagerly turns around and bends over your desk, wiggling her ass back at you."
        if not (the_person.vagina_available and the_person.vagina_visible):
            the_person "Let's just get this out of the way..."
            $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = False)
            "Once exposed, you enjoy the sight of [the_person.title]'s ass, pointed back at you."
        else:
            "You take a moment to appreciate the sight of [the_person.title]'s ass, pointed back at you."
    else:
        "She hesitates."
        the_person "I don't know... I'm not sure I want things to go in that direction..."
        mc.name "[the_person.title], I'm your boss. Now do as you're told."
        "For once, she remains silent and does as she is told, bending over your desk."
        $ the_person.draw_person(position = "standing_doggy")
        if not (the_person.vagina_available and the_person.vagina_visible):
            mc.name "Let's just get this out of the way..."
            $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = False)
            "Once exposed, you enjoy the sight of [the_person.title]'s ass, pointed back at you."
        else:
            "You take a moment to appreciate the sight of [the_person.title]'s ass, pointed back at you."
    $ mc.change_locked_clarity(50)
    mc.name "Damn, your ass is amazing."
    "You reach your hand out and run it along her hip, underneath her cheek, then up between her legs."
    $ the_person.change_arousal(10)
    $ play_moan_sound()
    the_person "Mmm..."
    "She gives a moan when you run your fingers across her exposed pussy."
    "You grope her ass with your other hand while you slide a finger inside of her."
    $ the_person.change_arousal(20)
    $ play_moan_sound()
    the_person "Ahhh... That feels really good. Do you want that blowjob now?"
    mc.name "Nah, I'm just getting you warmed up. You know what we said would happen if you bent over my desk like this again."
    if the_person.opinion.doggy_style >= 1:
        "She sighs but doesn't even pretend to put up a fight."
        the_person "Yeah, I know..."
    elif the_person.opinion.doggy_style == 0:
        "She sighs with a hint of annoyance in her voice."
        the_person "Ugh, really?"
        "She thinks about it for a moment."
        the_person "I guess this is easier than giving head though. Fine, do what you want."
    else:
        "She tenses up."
        the_person "What? I thought you were joking. You aren't really going to..."
        "You push a second finger inside of her, illiciting another moan."
        $ the_person.change_arousal(20)
        $ play_moan_sound()
        mc.name "Of course I'm going to. An ass like this deserves to be enjoyed to the fullest."
        mc.name "Besides, isn't this easier then getting down on your knees and giving head? You can just let me do my thing."
        the_person "Ugh. I should have seen this coming."
        the_person "Fine. Do what you want. I GUESS this is easier than giving head..."
    mc.name "Good. You definitely feel ready!"
    "Her pussy is slick with arousal from your fingering. You quickly drop your pants and get out your cock."
    $ mc.change_locked_clarity(50)
    "You smack her ass a couple times with your cock, then put your hands on her hips."
    if the_person.opinion.doggy_style >= 1:
        "Once you are lined up, she reaches back with one hand puts it on your leg, urging you forward."
        the_person "Mmm, put it in. I want to feel you slide inside of me!"
    else:
        "It takes a moment to get yourself lined up, but soon your cock is in position."
    "You hold her hips firmly as you push forward, sliding inside [the_person.possessive_title]'s slick cunt."
    $ play_moan_sound()
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    "You are once again fucking [the_person.title], bareback, bent over your desk."
    "Feels good to be the boss."
    "While you are using her for your pleasure, you want to make sure she has a good time too, to help break down those mental walls that keep this from happening more often."
    "You start slow, making sure to angle yourself down, rubbing along the front of her vagina, stimulating her g-spot."
    $ play_moan_sound()
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    the_person "Oooohhhh, that feels good..."
    "You pick up the pace a bit, and her body responds."
    if the_person.opinion.doggy_style >= 1:
        "She is trying to push herself back against you, but you have her pinned to the desk."
        the_person "Fuck me [the_person.mc_title], I'm so close!"
        "You can't believe she's getting ready to cum already, but you pick up the pace again, eager to make her cum all over your bare cock."
    else:
        "She lets out an extended moan. That actually sounded urgent?"
        mc.name "Are you gonna cum already, [the_person.title]?"
        "She looks back at you, breathless. From the look on her face, she must be!"
        "You speed up, eager to make her cum all voer your bare cock."
    $ play_moan_sound()
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    "The sounds of hips clapping together and feminine moans fills your office."
    "Suddenly her moans stop and her entire body begins to quiver."
    $ the_person.have_orgasm(half_arousal = False)
    "You continue to pound her pussy as she orgasms."
    "Watching your previously dominant employee cum all over your cock while pinned to your desk brings a smile to your face, and it feels amazing."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    the_person "Oh fuck, are... are you close?"
    mc.name "Getting there, but it is going to take a bit longer."
    the_person "Oohhhh.... Fuck...!"
    $ play_spank_sound()
    "You give her ass a spank, as if to make a point."
    "Her legs are shaking. If she were just standing, there's no way they would hold her weight."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    "Her moans are growing more desperate. She is going to cum again and you are going to cum too."
    "You don't bother letting her know, you quietly decide what you are going to do."
    $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside her":
        "You want to feel her pussy quivering all around you as you dump your load inside her."
        the_person "Oh fuck, I'm cumming!"
        $ the_person.have_orgasm()
        "With one final thrust, you push yourself deep inside of her and start to cum with her."
        $ the_person.cum_in_vagina()
        $ climax_controller.do_clarity_release(the_person)
        $ the_person.draw_person(position = "standing_doggy")
        "Her quivering pussy feels like it is sucking the cum from your body as you begin to unload inside of her."
        "You pin her to the desk and fill her with your seed, marking [the_person.possessive_title] as your personal cum slut."
        "When finish, you slowly pull out and look down. Your seed is dripping down the inside of her legs."
        the_person "Oh god..."
        "[the_person.title] doesn't even bother trying to stand up yet."

    if the_choice == "Cum on her ass":
        "[the_person.title] is distracted by her impending orgasm."
        the_person "Oh fuck, I'm cumming!"
        $ the_person.have_orgasm()
        "You decide to mark your territory, pulling out of her at the last moment."
        $ the_person.cum_on_ass()
        $ climax_controller.do_clarity_release(the_person)
        $ the_person.draw_person(position = "standing_doggy")
        "You stroke yourself as you start to cum all over [the_person.possessive_title]'s ass. She barely notices, in the final stages of her own orgasm."
        "You spurt several waves of cum all over her, marking her as your personal cum slut."
        "When finish, you look down at her, marveling at your artwork."
        the_person "Oh god..."
        "[the_person.title] doesn't even bother trying to stand up yet."
    "[the_person.possessive_title!c] seems dazed from her orgasms. You quickly clean yourself up."
    mc.name "Wow. Another good session. Would you mind closing the door behind you when you leave? I need to get going."
    the_person "Hey... That wasn't..."
    "You don't bother listening to what she has to say. Instead, you leave her behind in your office."
    $ clear_scene()
    "You made [the_person.possessive_title] cum all over your cock once again. You are sure her resistance is weakening, but you aren't sure if she is ready to give in to you fully."
    "Either way, you imagine you are going to have a chat about this soon."

    $ the_person.increase_opinion_score("doggy style sex")
    $ the_person.increase_opinion_score("showing her ass")
    $ add_ashley_submission_fuck_taboo_restore_action()
    $ ashley.event_triggers_dict["sub_fuck_taboo_regen"] = True
    return

label ashley_submission_anal_label():
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_anal_count", 0) == 0
    $ ashley.event_triggers_dict["sub_anal_count"] = ashley.event_triggers_dict.get("sub_anal_count", 0) + 1

    the_person "In this event, [the_person.title] bends over her desk and fucks her ass."
    "In this event, MC bends [the_person.title] over his desk again."
    "After sex begins, however, he sticks a finger in her ass. Then two."
    "Once she is warmed up, he pulls out of her pussy and fucks her ass."
    "At the end, MC chooses where to cum, and she gains a point towards liking anal sex."

    $ add_ashley_submission_anal_taboo_restore_action()
    return

label ashley_submission_anal_taboo_restore_label():
    $ outcome_convince = False
    $ the_person = ashley

    $ first_time = the_person.event_triggers_dict.get("sub_anal_count", 0) == 1
    $ the_person.draw_person(emotion = "sad")
    "[the_person.possessive_title!c] gives you a nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "Seriously? Is everything alright?"
        the_person "I can barely walk today... Was it really not enough to have my pussy anytime you want it? You have to put it in my ass too?"
    else:
        the_person "No? It isn't?"
        the_person "I thought that you were okay with it before. I don't want it in my ass like that."
        the_person "I can barely walk today!"

    mc.name "You didn't like having your ass fucked? It seemed like you came pretty hard..."
    the_person "I'm not saying it wasn't good. But it is just so weird to take it in the ass like that. Can we please stop?"

    $ attempts = 3 - the_person.event_triggers_dict.get("sub_anal_count", 0)

    menu:
        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_anal_count", 0) >= 3:
            mc.name "If it needs to stop, why does it keep happening [the_person.title]?"
            mc.name "You bent over my desk and you were practically BEGGING me for it."
            mc.name "Let's stop pretending. You love it when I fuck you. And you don't care what hole I choose. They are all mine to use anytime, any way I want."
            mc.name "You're a slut, [the_person.title]. Stop denying it."
            "[the_person.possessive_title!c] pouts for a moment, but even she can understand you're right."
            the_person "I know. But you're wrong about one thing."
            the_person "I'm not just {i}A{/i} slut, you idiot. I'm {i}YOUR{/i} slut. That's what makes this different."
            the_person "I'm not just a set of holes for any random man to please himself with."
            mc.name "Sure. This will be our little secret."
            $ outcome_convince = True

        "But it keeps happening...\n{menu_red}Requires: [attempts] more submissive anal fucks{/menu_red} (disabled)" if ashley.event_triggers_dict.get("sub_anal_count", 0) < 3:
            pass

        "Understood":
            mc.name "I don't agree that it is weird. But if you don't want to have sex like that again, I can settle for your sweet little pussy."
            "She bites her lip, but nods her agreement."
            the_person "Right. We'll just keep things from getting that serious again."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks back to her desk."

    if outcome_convince:
        $ ashley.event_triggers_dict["sub_anal_avail"] = True
        "[the_person.title] is willing to take your cock in any hole. Your mind wanders, thinking about how and when you can take advantage of her total submission to you again."
    else:
        $ add_ashley_submission_anal_taboo_restore_action()
        "[the_person.title] isn't willing to make anal sex a regular thing yet. You wonder if you can get her to be obedient if you could give it another shot..."
    return

label ashley_work_anal_label(the_person):
    pass

    return
