#Counter = KCF01

#Nothing technically wrong with this event, but if you uses kaden's mod, girls show up in their pyjamas, or, if Steph is slutty enough, buck naked, not that I mind, but public decency dammit. 

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["ellie_meet_ellie_intro_label"] = "meet_ellie_intro_label"
    config.label_overrides["Sarah_get_drinks_label"] = "Sarah_1st_official_label"

label meet_ellie_intro_label():
    $ the_person = mc.business.head_researcher
    "As night falls, you make your way downtown. Tonight you are meeting with your mysterious blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.lighting_conditions = dark_lighting
    "You text [the_person.possessive_title] to make sure she is still going to be there."
    $ mc.start_text_convo(the_person)
    mc.name "In the alley between 3rd and 5th. Did you manage to find a good vantage point?"
    the_person "Sure did. I don't see anyone yet, and I brought a taser, you know, just in case."
    $ mc.end_text_convo()
    "You have no idea how organized this person or group is, but you doubt that if things turn sour a taser will make much of a difference. You decide to keep that to yourself, though."
    "Hopefully she will go unnoticed if the blackmailer decides to have reinforcements of his own."
    "The blackmail note said to bring cash... But not how much. You pulled some strings at the bank and got $1000 in 20s, hopefully that will be enough."
    "Your business is just getting off the ground, so you really don't have the cash to handle a huge demand."
    "Eventually, the time comes, so you head down the alley. As you hit the halfway mark, a shadowy figure emerges from behind a dumpster."
    $ ellie.change_location(downtown)
    $ ellie.apply_planned_outfit() #KiNA Edit
    $ ellie.draw_person()
    ellie "That's far enough, stay right there."
    "The first thing you notice is the heavy southern twang in her accent. Secondly, it is heavily feminine. A southern woman is blackmailing you? It catches you completely off guard."
    ellie "You got cash?"
    mc.name "Yeah, although the note failed to mention exactly how much you were expecting."
    ellie "I'm figuring a million dollars in cold hard cash."
    "You pause. She can't be serious? If she knows anything about your business, she has to know you have no way of pulling that kind of liquidity."
    mc.name "I'm sorry, my business is just founded, and I don't have the ability to pull that much, especially on such short notice."
    ellie "Ah lordie help me. Hmm. How about this. You give me some cash now as a show of good faith, and we'll meet again next week and you kin give me the money then."
    ellie "As a fellow criminal, surely you can understand that I got bills to pay."
    "You doubt you will be able to find a million dollars between now and next week, but at least this will give you some time to try and figure things out."
    mc.name "Alright, that's a deal."
    ellie "Alright. For now, let me have a hundred dollars. That'd oughta get me thru until next week..."
    "This whole conversation is throwing up serious red flags. Is she really just asking a hundred for now? The whole thing reeks of amateurism."
    "You look up and around, trying to see if you see any motion or hint that she may have someone else watching, but don't see anything. You decide to play along for now."
    "You pull out a hundred dollars, being careful not to show the remaining bills you have with you, and extend your hand with them."
    $ mc.business.change_funds(-100)
    "She slowly walks forward and takes her money from you. The alley is dark, but is that red hair? She quickly pulls away."
    ellie "Same time next week."
    "The mysterious blackmailer turns and quickly leaves the alley. You stand there observing her until she turns the corner, when you turn around and leave the alley."
    $ clear_scene()
    "Once you are a safe distance away from the alley, you pull out your phone and text [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    mc.name "Hey, meet me at the bar. We have a lot to talk about."
    the_person "Okay, see you there."
    $ mc.end_text_convo()
    $ mc.location.lighting_conditions = standard_outdoor_lighting
    $ mc.change_location(downtown_bar)
    $ the_person.change_location(downtown_bar)
    "You grab a secluded table away from the crowd around the bar with [the_person.title]."
    $ the_person.apply_planned_outfit() #KiNA Edit
    $ the_person.draw_person(position = "sitting")
    the_person "So, how'd it go?"
    mc.name "Confusing, to be honest. You see anything from where you were at?"
    the_person "Not much, to be honest. I could tell it was a woman, but I didn't see anyone else and couldn't make out much about her."
    mc.name "Well, first thing, she had a heavy southern accent. She could have been faking it, but I doubt it. The whole thing felt... Like she was an amateur, to be honest."
    the_person "Why do you say that?"
    mc.name "Well, she really seemed to have no idea how much money to ask for, so she just said she needed a million dollars."
    the_person "Wow, there's no way you could make a ransom like that, at least as far as I know."
    mc.name "Right? And then when I said I didn't have that kind of money, she told me had she had bills to pay?"
    mc.name "So she just asked for a hundred dollars as a show of good faith, and to meet again next week..."
    the_person "Wow... That's so weird."
    mc.name "It was hard to see, the alley was so dark but... When she took the money from me... I think she's a redhead."
    the_person "Ahhh, a southern redhead? Of all the luck you have, your blackmailer happens to be a southern redhead? Did she have another obvious feature? Missing a leg perhaps?"
    "Your head researcher is joking with you, but you can't help but laugh. This has to be a setup... Right? How many southern redheads could possibly live in this town?"
    mc.name "Nothing else that I noticed. But the bills to pay thing bugs me."
    the_person "You think she's unemployed maybe?"
    mc.name "Maybe. I don't know. Up for helping me out with some research?"
    the_person "Oi. I guess I can do that. I'll do some searching on the internet this weekend and see if anything comes up."
    mc.name "Thanks. I appreciate it."
    "You decide you've had quite enough adventure for one night, so you decide to head home."
    mc.name "Thanks for your help [the_person.title]. I appreciate it."
    $ the_person.change_happiness(2)
    the_person "Well, I admit, I feel partially responsible since I was the one to bring in the nanobots in the first place."
    mc.name "I don't know why, but I feel a lot better about this whole thing. If we can figure out who she is, maybe we can come up with an alternative solution."
    the_person "Err... you don't mean like... 'taking care of her' do you?"
    mc.name "Of course not! But there may be other things we can do about this, I think."
    "With your business concluded, you and [the_person.possessive_title] part ways."
    $ mc.change_location(bedroom)
    $ clear_scene()
    $ add_ellie_head_researcher_halfway_intro_action()
    return

label Sarah_1st_official_label():
    $ mc.stats.change_tracked_stat("Girl", "Dates", 1)
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ the_person = sarah

    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person "[the_person.mc_title]! I figured I'd find you around here on a Saturday again!"
    "You look up to see the now familiar face of [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, get_sarah_date_outfit_one(), emotion = "happy")
    "It's crazy to think that just a short time ago, she was out of your life completely, but after your chance encounter, you feel like you've been friends forever."
    mc.name "Hey [the_person.title]. You look great! Are you going out tonight?"
    the_person "Actually, I'm not sure yet. I hope so! But I'm not sure if the guy I want to go out with is going to be able to go yet or not..."
    mc.name "Is that so? I hope he can make it and that he treats you well!"
    the_person "Hahaha, yeah me too. And don't worry, he's always treated me right."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] looks down at the floor for a minute and mumbles something. It's obvious she is trying to work up the courage to ask you out, but it is cute watching her fumble a bit."
    the_person "So... you uhh, have any big plans for the evening, [the_person.mc_title]?"
    mc.name "Oh, well, certainly nothing as big as what you have planned! I'm just trying to get a little ahead of work for next week."
    the_person "Ah! That's good. It is pretty amazing how much work you put into this place. It's something I admire a lot..."
    the_person "Anyway, I've seen how hard you work and I was thinking that, maybe we could go out and get a few drinks?"
    "You decide to tease her a bit."
    mc.name "Ahh, I see. You meeting another friend tonight? I'm not sure I want..."
    "She quickly interrupts you."
    the_person "No! God no, that was awful. I thought we could just go out, you know? Me and you?"
    mc.name "You mean like a date?"
    "She stutters a moment before she replies."
    the_person "Well, ermm, I mean, uhh..."
    the_person "Yeah. Pretty much that is exactly what I'm trying to ask..."
    $ mc.change_locked_clarity(10)
    "You admire her courage. She must be really interested in you to have the guts to ask you out like this! If you accept, she might assume you are interested in a relationship..."
    menu:
        "Sounds great!": #Begin the dating path with Sarah
            mc.name "A date sounds great! I'd love to spend some more time with you, catching up and learning about what you've been up to."
            "Her face shows visible signs of relief."
            the_person "Okay! This will be fun! Do you want to get out of here now, or do you need some time to finish up?"
            $ sarah.event_triggers_dict["dating_path"] = True
            $ the_person.add_situational_slut("Date", 10, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness since she really likes you.

            $ the_person.change_stats(happiness = 10, love = 5)
        "Just as friends":
            mc.name "I wouldn't mind going out for a few drinks, with a friend of course."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            "Her face shows visible signs of disappointment."
            the_person "Oh, right. Friends! That's us! I don't want to interrupt you, there, buddy. Need a few minutes to finish up?"
            $ the_person.change_stats(happiness = -10, love = -5, obedience = 5)
            $ sarah.event_triggers_dict["dating_path"] = False
            $ the_person.add_situational_slut("Date", 5, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness not so high since we go as friends.

    mc.name "I'm actually at a great stopping point now. Let's go!"
    the_person "Great! Do you want to walk again tonight? It was kind of nice when we walked together last time."
    mc.name "Sounds good to me, it's good to get out and stretch the legs once in a while."
    "You lock up on your way out and head toward downtown."

    $ mc.change_location(downtown)


    "You enjoy pleasant conversation with [the_person.possessive_title] as you walk downtown."
    if the_person.event_triggers_dict.get("dating_path", False):
        "As you walk along, you feel her hand slip into yours. You twiddle your thumb with hers as you walk downtown."
        $ mc.change_locked_clarity(10)
    #TODO the convo

    $ mc.change_location(downtown_bar)

    "You walk into the bar. [the_person.title] spots an empty booth."
    the_person "Hey, there's an empty table over there!"
    mc.name "Go grab it. Appletini?"
    the_person "Sounds great!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She walks off to the booth while you head up to the bar."
    "You order your drinks with the bartender. If you wanted to, now would be a good time to slip a serum into her drink..."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    menu:
        "Slip in a serum" if mc.inventory.has_serum:
            "After you get the drinks, you carefully add a serum to it."
            call give_serum(the_person) from _call_give_sarah_serum_KCF001

        "Slip in a serum\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
            pass

        "Leave alone":
            "You decide to leave her drink alone."
    "You grab your drinks and then head to the table. You sit down across from [the_person.title]."
    $ scene_manager.update_actor(the_person, position = "sitting")
    the_person "Thanks! I love these things..."
    "She takes a long sip from her glass. You take a sip of yours. [the_person.possessive_title!c] sets down her glass and looks at you."
    the_person "I have to say, I feel like I'm settling in pretty well. The girls at the office have been really nice to me so far."
    mc.name "That's good to hear. I'm very selective about who I hire."
    the_person "Yeah. Your choice is very, shall we say, interesting? Hiring only women to work for you. Not that I'm complaining or anything!"
    mc.name "I know it may seem a bit odd, but so far it has been advantageous to keep the staff all female. Perhaps in the future that could change, but for now it is working."
    the_person "It's quite alright with me. To be honest, I umm, enjoy the surroundings..."
    "She takes a long sip of her drink."
    mc.name "Sorry, I feel like you've hinted at this a few times before but, I just want to clarify. Are you a lesbian? I'm totally fine with that, I'm just curious."
    "[the_person.title] laughs and puts her hand on yours."
    the_person "Oh, I'm not dedicated to it or anything, but I've always been curious about what it would be like to be with another woman."
    "She sighs."
    the_person "Don't get me wrong, I don't think I could ever date another woman, I prefer men, but I've always wanted to try a Ménage à Trois..."
    $ the_person.increase_opinion_score("threesomes")
    "You have discovered that [the_person.title] is bi-curious and into threesomes!"
    $ mc.change_locked_clarity(20)
    mc.name "That's very open–minded of you. I can certainly respect that!"
    "[the_person.title] tips her glass back and finishes her first drink. You make it a point to do the same."
    mc.name "Let me grab the next round."
    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "That sounds great. Say, want to play some darts? I'll grab us a board while you grab the drinks!"
        mc.name "That sounds great, I'll meet you over there."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title!c] gets up and walks over to the dart boards while you grab a couple more drinks."
        $ mc.business.change_funds(-20, stat = "Food and Drinks")
        "You feel like, so far at least, this date is going pretty well!"
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You walk over to [the_person.title], drinks in hand. You hand her a drink."
        mc.name "How about a toast? To tonight! May we love as long as we live, and live as long as we love."
        $ the_person.change_stats(happiness = 5, love = 2)
        "You surprise yourself with your sappy toast. It seems to have the desired effect though, as she smiles wide with your toast."
    else:
        the_person "Hey, let me grab the next round. I want to play a game though! Can you go get us a dart game set up?"
        mc.name "Yeah, that actually sounds pretty fun. I'll do that."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title!c] gets up and walks over to the bar while you head over to reserve a dart board."
        "You are having a lot of fun hanging out with [the_person.title]. Even though you rejected her earlier, you are wondering how she might feel about a friends-with-benefits setup..."
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.title] joins you and hands you another whiskey."
        the_person "How about a toast? To he who has seen me at my best and has seen me at my worst and can't tell the difference!"
        "You grin at her cheesy toast, she smiles wide at you."
    "You clink your glasses together and take a deep sip."
    menu:
        "Play":
                the_person "Alright! I'm going first."
                $ scene_manager.hide_actor(the_person)
                call play_darts_301(the_person, focus_mod = 2) from play_darts_301_call_KCF2
                if _return:
                    $ scene_manager.show_actor(the_person, emotion = "sad")
                    "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
                else:
                    $ scene_manager.show_actor(the_person, emotion = "happy")
                    "[the_person.title] gives you a huge smile after winning your game of darts!"
        "Skip (no story impact)":
                #skipping dart game
                "After a few rounds..."
                if renpy.random.randint(0,1) == 0:
                    $ scene_manager.show_actor(the_person, emotion = "sad")
                    "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
                else:
                    $ scene_manager.show_actor(the_person, emotion = "happy")
                    "[the_person.title] gives you a huge smile after winning your game of darts!"

    "You notice the drinks are empty."
    mc.name "That was a good game. Want another round and another game?"
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    the_person "Oh! That sounds great! I'll get it set up!"
    "You walk over to the bartender and order another round. You walk back to the dart board and give [the_person.possessive_title] her drink."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    the_person "Thanksh! I love these things..."
    "You notice her speech is starting to get a little slurred... You bet as you feed her drinks, she may have trouble focusing on the game."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] starts to line herself up on the line to throw. You decide to see if you can distract her a little further."
    "You walk up behind her and put your hand on her back."
    mc.name "Hang on, I just noticed something about the way you are throwing the darts."
    "You get in close behind her until you are right behind her, your body up against hers."
    $ mc.change_locked_clarity(20)
    the_person "Oh? I thought I did okay, but if you have some... tips... for me that would be nice!"
    "The feminine smell of her perfume enters your nostrils and you take a deep breath, enjoying your proximity with [the_person.title]."
    "You run your fingertips along her arm, until you are holding her hand as she holds her dart."
    mc.name "That's right, there was something about your posture that caught my eye."
    "You are now pushing yourself lightly up against [the_person.title]. She catches her breath when she feels your erection beginning to grow against her backside."
    $ the_person.change_slut(2, 60)
    the_person "Ah, something caught your eye then?"
    "You quickly release her and then walk back to the table."
    mc.name "Yeah, something like that. I'm not sure what it was, but I'll let you know if I can put my finger on it..."
    # "[the_person.title] is trying to focus on the dart board, but she keeps stealing glances back at you. Your flirting is having the desired effect on her!"
    # "She readies herself for the next round of darts."
    # $ scene_manager.hide_actor(the_person)
    # call play_darts_301(the_person, focus_mod = -2) from play_darts_301_call_2
    # if _return:
    #     $ scene_manager.show_actor(the_person, emotion = "sad")
    #     "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
    # else:
    #     $ scene_manager.show_actor(the_person, emotion = "happy")
    #     "[the_person.title] gives you a huge smile after winning your game of darts!"
    "Drinks are empty again. You look at [the_person.title]. She is definitely tipsy, but you think she should be able to handle one more round."
    mc.name "How about one more game? I'll grab us another round."
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    the_person "Another drink! I loooooveeeee going out with you, [the_person.mc_title]! You know how to keep the drinksh flowing!"
    mc.name "Haha, okay, let me go grab us another round."
    "You walk over to the bartender and order another round. You walk back to the dart board and give [the_person.possessive_title] her drink."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    the_person "Okay, so, I've had a great warm up now, but I think for this next round, we should make it a littler more... intereshting."
    mc.name "Oh? What did you have in mind?"
    the_person "I think, whoever loses... hah, that's a funny word... anyway, whoever is the loser, should hafta walk the winner home!"
    "You raise an eyebrow involuntarily. For some reason you expected something a little... crazier than that."
    mc.name "Hah, okay, we can do that. You're up first!"
    "[the_person.possessive_title!c] turns and looks at the table where she set the darts earlier. She bends over and slowly starts picking them up, one by one."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She's completely bent over the table, and is obviously wiggling her hips at you. You realise when she talked earlier about the loser walking the winner home, she was probably proposing your place or hers..."
    $ mc.change_locked_clarity(25)
    "You step behind her and get close to her again. You push your hips against hers, and pretend to reach past her towards your darts that are also on the table."
    mc.name "Excuse me... just grabbing my darts here real quick..."
    "You slowly grab your darts, one by one. She pushes herself back against you."
    the_person "Of course, be careful though! The tipsh are sharp."
    mc.name "Of course, you needn't worry, I'll handle them gently..."
    $ the_person.change_slut(2, 60)
    "As you finish your sentence, you run your free hand down along her back. You slowly stand up and move away from her. You don't want to be too lewd in a public setting like this... not yet anyway..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title!c] walks over to the line and looks at the dart board, then back at you. She is so distracted, she can barely focus on the board."
    "You should be able to win this game handily, unless you decide to throw the game on purpose!"
    $ scene_manager.hide_actor(the_person)
    $ sarah.event_triggers_dict["drinks_out_progress"] = 2
    menu:
        "Play":
            call play_darts_301(the_person, focus_mod = -6) from play_darts_301_call_KCF3
            if _return:
                $ scene_manager.show_actor(the_person, emotion = "happy")
                "[the_person.title!c] can't even pretend to be sad when you win the game."
                the_person "You won!"
            else:
                $ scene_manager.show_actor(the_person, emotion = "happy")
                "[the_person.title!c] gives you a huge smile after winning your game of darts!"
                the_person "You are such a gentleman. I'm pretty sure you were just letting me win! That totally doesn't count!"
        "Skip":
            #skipping dart game
            "After a few more rounds..."
            if renpy.random.randint(0,1) == 0:
                $ scene_manager.show_actor(the_person, emotion = "happy")
                "[the_person.title!c] can't even pretend to be sad when you win the game."
                the_person "You won!"
            else:
                $ scene_manager.show_actor(the_person, emotion = "happy")
                "[the_person.title!c] gives you a huge smile after winning your game of darts!"
                the_person "You are such a gentleman. I'm pretty sure you were just letting me win! That totally doesn't count!"

    "She takes the last sip of her drink before setting it down."
    the_person "I'll walk you home! Besides, it's only fair, you walked me home last time."
    "You start to protest, but she quickly silences you."
    the_person "Don't be silly! I can see myself home whenever we get done... err... when you say goodbye I mean..."
    "Her intentions are pretty clear at this point. You take the last sip of your whiskey and set it down."
    mc.name "I can see there's no talking you out of it. And to be honest, I would appreciate the company."
    "She smiles at you. You leave the bar with her and start walking home."
    $ mc.change_location(downtown)
    #TODO set to nighttime
    $ time_of_day = 3 #Hopefully this works

    "You enjoy the fresh air as you begin your walk. Thinking about your time with [the_person.title] tonight, you decide now it would probably be a good idea to talk about things."
    if the_person.event_triggers_dict.get("dating_path", False):
        "You take the initiative and take [the_person.title]'s hand. You can see her smile out of the corner of your eye."
        mc.name "So, I had a lot of fun on our date tonight."
        the_person "Me too!"
        mc.name "I think it is great that you are so open in your sexuality, and wanting to try new things."
        "You can feel her grip tighten on your hand for a second."
        mc.name "I know it is kind of weird to talk about, but I want you to know that if you want to mess around with another girl... let's just say I'm not the jealous type."
        "She laughs at you before replying."
        the_person "That's good to know. Honestly, I wasn't sure how you would feel about it, but I figure most guys like the idea of being with two women..."
        if had_family_threesome() or nora.event_triggers_dict.get("steph_teamup_stage", 0) == 2:
            mc.name "Yeah, I suppose that much is obvious. That said, I feel confident that I could help get something started..."
        else:
            mc.name "Which guy wouldn't. I'll help you if I can find a candidate, but I want to be that lucky guy."
        
    else:
        mc.name "So, I had a lot of fun tonight."
        the_person "Me too!"
        mc.name "I think it is great that you are open in your sexuality, and wanting to try new things."
        "You see a brief frown on her face start to form."
        if had_family_threesome() or nora.event_triggers_dict.get("steph_teamup_stage", 0) == 2:
            mc.name "I know it is kind of weird to talk about, but I want you to know that, even though I'm not looking for anything serious right now, I'd love to help you explore that side of things... sexually."
        else:
            mc.name "You know what? I'll help you if I can find a candidate, but I want to be that lucky guy."
        
    "She stops and turns to you."
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person "You mean... you would be willing to try and set something up?"
    mc.name "Well... yeah! I'm pretty sure that is something I could pull off."
    "[the_person.title] looks bewildered."
    the_person "That would be something. Huh! I'll have to think about it... okay?"
    "As you are standing there looking at each other, you feel a cold breeze begin, followed quickly by rain drops beginning to fall."
    the_person "Ah! I didn't know it was going to rain!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title!c] turns and starts to walk quickly. You hurry to catch up to her."
    "You are only a few blocks from your house, but by the time you get there, the rain is pouring down in sheets."
    "You quickly open the door and let [the_person.title] in."

    $ mc.change_location(hall)
    $ the_person.change_location(hall)
    # make sure we don't alter the outfit in her wardrobe
    python:
        test_outfit = the_person.outfit.get_copy()
        if test_outfit.get_upper_top_layer:
            test_outfit.get_upper_top_layer.colour[3] *= .75 #make top transparent
        if test_outfit.get_lower_top_layer:
            test_outfit.get_lower_top_layer.colour[3] *= .75 #make bottom transparent
        scene_manager.update_actor(the_person, test_outfit, position = "stand4")
        del test_outfit

    if the_person.outfit.get_upper_top_layer or the_person.outfit.get_lower_top_layer:
        "You look at [the_person.title]. Her clothing is soaked and you can practically see through it. She looks cold."
    else:  #She's... naked?
        "Barely clothed, [the_person.title] is shivering from the cold."
    $ mc.change_locked_clarity(30)
    mc.name "I'm sorry, I didn't realise it was going to rain like that!"
    "You made quite a bit of noise when you came in the door, and [mom.title] pokes her head out from the kitchen to see what is going on."
    $ scene_manager.add_actor(mom, position = "stand2", display_transform = character_left_flipped)
    mom "Oh! You two look absolutely soaked! Are you okay?"
    if mom.is_employee:
        mc.name "Thanks, Mom! We got caught out in the rain walking back. Do you think you could grab us a few towels, and maybe have some dry clothes for her to wear for a bit?"
    else:
        mc.name "Thanks, Mom! This is [the_person.title]! We got caught out in the rain walking back. Do you think you could grab us a few towels, and maybe have some dry clothes for her to wear for a bit?"
    if sarah_epic_tits_progress() == 0: #Small tits
        mom "Yes of course! She looks about [lily.fname]'s size, I'm sure I can find something..."
    elif sarah_epic_tits_progress() == 2: #Big tits
        "[mom.title] looks her over for a moment, checking out her curves."
        mom "Yes! I'm not sure [lily.fname]'s clothes would work... I bet I have something I could give her, just give me a minute."
    elif sarah_epic_tits_progress() == 3: #Huge tits
        "[mom.possessive_title!c]'s eyes travel all over [the_person.title]'s body. Her eyes go wide when she sees how big her tits are."
        mom "I'm not sure I have... actually, I think [cousin.fname] might have left something that would fit her..."
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.title] leaves to go find something. [the_person.title] is shivering cold."
    $ scene_manager.hide_actor(mom)
    mc.name "I'm sorry, you look so cold. Why don't you come here for a minute..."
    "You step toward her. You put your hands around her back and draw her close to you. She wraps her arms around your neck."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "Her body feels cold, but it feels great running your hands along her body. After a minute, she stops shivering."
    $ mc.change_locked_clarity(20)
    the_person "Thank you... that feels... much better."
    "Her face is nearing yours, and you are just getting ready to kiss her."
    $ scene_manager.show_actor(mom, position = "stand2")
    mom "Here we go! I got you some... OH!"
    "ABORT! You quickly let go of [the_person.title] when your mother interrupts you."
    mom "Sorry! I didn't... here you go!"
    "She quickly hands [the_person.title] a large towel and a set of clothes."
    mom "There you are dear. I'm sorry, but [lily.fname] is in the bathroom right now, taking one of her ridiculously long showers..."
    mc.name "That's okay, she can change in my room! I can wait out here."
    the_person "Thank you! I'll be quick!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] takes the clothes and the towel. You quickly point her to your room."
    "She disappears behind your bedroom door with the clothes. You mother turns to you."
    $ scene_manager.hide_actor(the_person)
    mom "She seems nice!"
    if mom.is_employee:
        mc.name "Yeah! She used to be so scrawny back then, right? Never thought I'd see her again."
    else:
        mc.name "Yeah! Believe it or not, she is the daughter of one of dad's old friends. We used to play together as kids!"
    if mom.sluttiness < 40:
        if sarah_epic_tits_progress() == 0: #Small tits
            mom "Aww! That's cute! And she is so cute too. You be nice to her, okay?"
        elif sarah_epic_tits_progress() == 2: #Big tits
            mom "Aww! That's great! She certainly has blossomed into a beautiful young lady. You be nice to her, okay?"
        elif sarah_epic_tits_progress() == 3: #Huge tits
            mom "Wow! That's great! And she has... I mean... her figure is incredible! You be nice to her, okay?"
        mc.name "Don't worry, [mom.title]."
    elif mom.sluttiness < 70:
        if sarah_epic_tits_progress() == 0: #Small tits
            mom "That's cute... but... what about me? The woman who brought you into this world needs your attention too..."
        elif sarah_epic_tits_progress() == 2: #Big tits
            mom "That's nice dear... but don't forget about me, okay? I have needs too!"
        elif sarah_epic_tits_progress() == 3: #Huge tits
            mom "That's nice I guess..."
            mom "But... look I know she is absolutely stacked, but don't forget about me, okay? I have needs too!"
        $ mc.change_locked_clarity(20)
        mc.name "Don't worry, [mom.title]. No one could ever replace you."
    else:
        mom "And she is so pretty."
        if mom.opinion.threesomes >= 0:
            mom "So... when do I get a chance to get my hands on her?"
            $ mc.change_locked_clarity(30)
            mc.name "Don't worry, it'll be soon [mom.title]."
            mom "Okay! I'll umm, just be in my room for the night..."
        elif mom.opinion.polyamory >= 0:
            "[mom.fname] gave you a knowing look."
            if home_harem():
                mom "Two isn't enough for you?"
                "You hold your hands up."
                mom "We are going to have a long talk later, Romeo."
            else:
                mom "Explain yourself, young man."
                "You hold your hands up."
                mom "We are going to have a long talk later."
        elif mom_taboo_completed(): #We fucked her enough at least..
            "[mom.fname] gave you a conflicting look."
            mom "This is how it supposed to be..."
            mom "This is who you should be with..."
            "You can see she is shaking a bit."
            mom "But why..."
            "You gave her a reassuring hug."
            mc.name "Don't worry, [mom.title]. No one could ever replace you."
        else: #For non-incest path who don't touch Jennifer
            mom "Is she your girlfriend?"
            mom "Have fun!"
    $ scene_manager.remove_actor(mom, reset_actor = False)
    "[mom.possessive_title!c] quickly steps into her room and closes the door. You look at the door to your own bedroom, imagining the woman inside it slowly peeling off her soaking wet garments..."
    "As you look at your door, you realise that it isn't closed all the way. [the_person.title] left it open a crack!"
    "You creep slowly up to your door and listen. You don't hear much coming from within, so you slowly inch the door open and then peek inside."

    $ mc.change_location(bedroom)

    $ scene_manager.show_actor(the_person, position = "walking_away")
    "You see that [the_person.title] is just starting to peel off her clothes."
    $ scene_manager.strip_full_outfit(person = the_person)
    $ mc.change_locked_clarity(50)
    "She stands there, looking at herself in the mirror for a moment, when she spots you looking at her from the door. Busted!"
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person "Hey! You gonna come in and close the door or just stand there?"
    "Nice! She must have left the door cracked on purpose, hoping you would peek."
    "You quickly step into your room, close your door and lock it behind you. [the_person.title] giggles."
    "You walk over to her and embrace her again."
    $ scene_manager.update_actor(the_person, position = "kissing")
    the_person "I was hoping you would come..."
    "Her mouth opens, her eyes close, and your faces move together as you begin to kiss. Her mouth immediately opens and you begin to twirl your tongues around each other."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(10)
    the_person "That feels good... but I'm freezing!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You quickly pick her up. You carry her over to your bed and then throw her down on it."
    mc.name "Don't worry, I'll get you warmed up in a hurry!"
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You start to climb on top of [the_person.possessive_title]. She opens her legs and the wraps them around you."
    "You are still wearing your wet clothes, but you don't care. You slowly start to grind your hardness into her groin through your pants."
    $ the_person.change_arousal(10)
    the_person "Mmmm, that feels good, but you're cold too! Let's get these off..."
    "[the_person.title] is pulling at your shirt. You quickly help her take it off, then reach down, unbutton your pants, and take them and your underwear off in one smooth motion."
    "Your cock springs free. [the_person.title] gasps as she takes it in her hand."
    the_person "Ohhhh. It's so warm! This is exactly what I need to warm me up!"
    "You look down at [the_person.title]. She is stroking your cock now, and you can feel her legs start to wrap around your back again, urging you to push yourself into her."
    "For a moment you consider grabbing a condom, but that thought evaporates when she runs the nails of her free hand roughly down your back."
    "You let go of yourself, and move your hips into position just above hers. Her hand stops stroking you and guides your cock to her pussy as it gets close."
    "You can feel the moist heat coming from between [the_person.title]'s legs as you get close. You feel the head begin to poke against her slit."
    "Her legs wrap tighter behind you, begging you to push into her. You happily give in, parting her labia and sinking slowly into her cunt."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "OH god... that's so good!"
    call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_sex_description_sarah_grabbing_drinks_KCF1

    call check_date_trance(the_person) from _call_check_date_trance_sarah_get_drinks_KCF

    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "Oh my god... ever since you came back into my life, I'd been hoping... maybe this was all happening for a reason."
        $ scene_manager.draw_scene()
        "You lay down on your side next to her. She scoots next to you and lays her head on your arm."
        the_person "Can we... can I just be close to you for a while? I'm not ready for this day to end!"
        $ the_person.change_stats(happiness = 5, love = 2)
        mc.name "Of course! Your skin feels so good."
        "You cuddle up with [the_person.possessive_title] for a while, just enjoying the afterglow of your lovemaking."
        "She is starting to doze off, when suddenly she wakes up and gets up."
    else:
        the_person "Mmm, that was nice. It's been a while since I was able to do that."
        $ scene_manager.draw_scene()
        "She rolls on her side and looks at you."
        the_person "So... friends with benefits then? I think that is an arrangement that I could live with."
        mc.name "Great! Yeah if you get the urge, I'm up for a hookup now and then."
        the_person "Okay. You'd better satisfy me though!"
        "You give her a wink and a nod."
        $ the_person.change_stats(happiness = 5, slut = 1, max_slut = 60)
        the_person "Alright... I'm just gonna lay here for a moment. It's been a long day, I need to take a few minutes before I get up."
        "She rolls over, facing away from you and relaxes for a bit, enjoying coming down from the high of fucking."
        "She is starting to doze off, when suddenly she wakes up and gets up."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Sorry... I just realised how late it is getting. I'd better get home!"

    $ scene_manager.update_actor(the_person, get_sarah_date_outfit_one())
    "You watch her intently from your bed. Her body looks amazing, as she begins to hide it behind her clothes that have dried up by now."
    $ mc.change_locked_clarity(10)
    the_person "Don't worry, I can see myself out. I had a great time tonight! I'll see you on Monday, okay?"
    mc.name "Goodbye!"
    $ scene_manager.remove_actor(the_person)
    $ the_person.clear_situational_slut("Date")

    "[the_person.possessive_title!c] lets herself out of your room and leaves. Wow, what an evening!"

    $ add_sarah_stripclub_story_action()
    $ scene_manager.clear_scene()
    call advance_time() from _call_advance_time_sarah_get_drinks_KCF
    return
