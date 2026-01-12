
#Ashley Slut Path
label ashley_porn_video_discover_label():   #20 Sluttiness
    # make sure we are in the bedroom
    $ mc.change_location(bedroom)
    $ the_person = ashley
    "It's been a long day. You consider heading for bed, but you've got a lot of energy, and you'd rather not just lie awake in bed."
    "You decide to hop on your PC and watch some porn and jack off before you go to bed. That always helps you fall asleep."
    "You load up your porn accounts and start browsing through some videos."
    "'Desperate Slut Begs for Creampie'? Nah! 'Guy Fucks Step Sister Stuck In Bear Trap'? Hmm... maybe later."
    "As you browse, you notice a clip thumbnail with a girl riding a guy tied down and in restraints. She looks kinda familiar? Reminds you of someone from work maybe?"
    "'Naughty Nurse Ties Up Boyfriend. RUINED ORGASM'? Eh, it's worth a shot anyway. You click on it and wait for the generic porn intro to finish."
    "Your mouth falls open when the scene starts."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, the_person.get_random_appropriate_underwear(50, sluttiness_min = 20, guarantee_output = True), position = "stand4", emotion = "happy")
    $ mc.change_locked_clarity(10)
    "There's a guy and a girl, who you immediately recognise as [the_person.title]. This looks like one of those hidden camera type videos."
    "In the background is what appears to be some sort of medical office."
    "The guy is tied up, with his four limbs tied to the four corners of a medical bed. You watch as [the_person.title] gets up on the examination table and crawls on top of him."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "She turns and puts her ass right in his face. She starts to ride his face roughly."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] strokes the guy a little bit, but basically ignores his cock as she rides his face."
    "She does this for several minutes, until she starts to moan and really ride the guy roughly. Her moans get loud, it sounds like she is finishing."
    $ scene_manager.update_actor(the_person, position = "cowgirl")
    "She turns around and puts a condom on the guy. She starts to tease him."
    the_person "You want this in my pussy, bitch? Yeah right... like you deserve that."
    "Wow, she is definitely nailing the whole dominatrix role..."
    "She starts to dry hump the poor guy. With his limbs down at his sides, there's not much he can really do."
    "She keeps going, speeding up and slowing down multiple times."
    "Eventually, you can hear the guy starting to moan, it's clear he is getting ready to cum."
    "She quickly hops off. The guy fills up the condom while [the_person.title] basically ignores him."
    the_person "Pathetic... maybe someday I'll let you touch me... but not today, that's for sure!"
    $ scene_manager.clear_scene()
    "Wow... [the_person.title]..."
    "This seems pretty crazy. She seems to be some kind of closet dom? It's hard to believe."
    "And the background... was this done in a real hospital room?"
    "There's no way you can talk to her about it yet. Maybe you should bring it up with [stephanie.title] first?"
    $ add_ashley_ask_sister_about_porn_video_action()
    return

label ashley_ask_sister_about_porn_video_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_person.title]. I need to talk to you about something... sensitive. Could you please come with me to my office?"
    the_person "Of course."
    $ mc.change_location(ceo_office)
    "You enter your office and gesture for her to sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 50:
        "As she sits down, you notice [the_person.possessive_title]'s posture. She is sticking her chest out. She probably thinks you brought her to your office for some... personal time."
        $ mc.change_locked_clarity(20)
    mc.name "I wanted to talk to you again, about your sister, [ashley.fname]."
    the_person "Oh!... right..."
    if the_person.sluttiness > 50:
        "Her back slumps noticeably when you say that."
    mc.name "This is not going to be an easy or pleasant conversation, but uhh, I found a video of your sister..."
    the_person "UGH! I thought we got that deleted from everywhere."
    mc.name "Oh... deleted?"
    $ scene_manager.update_actor (the_person, emotion = "sad")
    the_person "Yeah, she had this boyfriend a while back. It came out after they broke up that he was secretly filming them having sex and posting it online..."
    the_person "Unfortunately, they were doing it while she was on break at her job..."
    the_person "We did everything we could to shut it down once we found out, but the internet is crazy. Once it's out there, it's out there!"
    mc.name "Wow, I feel awful, I had no idea."
    the_person "Someone at the hospital eventually found out about it, and that was the HR issue that wound up getting her fired."
    mc.name "Ahhh, that makes sense."
    "You both look at each other for a moment, considering the circumstances."
    the_person "As you probably saw... she is pretty... adventurous... with guys."
    the_person "I don't know why but... she has this thing, ever since we were little. Some kind of sibling rivalry."
    if the_person.is_girlfriend:
        the_person "It wouldn't surprise me if she makes a pass at you, especially since we are dating."
    else:
        the_person "I umm... I wouldn't be surprised if she makes a pass at you."
    "Interesting... but you wonder if getting busy with a dom like that is really what you want to do?"
    "Maybe with some serums, you could try taming her a bit... so she can see what the other side of it is like..."
    the_person "Look umm... just so I make myself clear here... be careful with her. She can be sneaky, and knows a lot more than she lets on."
    mc.name "I understand. Thank you [the_person.title]."
    $ scene_manager.clear_scene()
    $ add_ashley_ask_about_porn_action()
    return

label ashley_ask_about_porn_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "You decide to broach the difficult topic of the porn video you discovered."
    mc.name "I was hoping to talk to you about something a little sensitive. Would you mind if we went to my office?"
    the_person "Oh... sure..."
    $ mc.change_location(ceo_office)
    "[the_person.possessive_title!c] follows you to your office. After you enter, you close the door behind you."
    mc.name "Go ahead and have a seat."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "You can tell she looks a little scared."
    mc.name "Are you okay?"
    the_person "I'm sorry sir... I'm working hard..."
    "What? She thinks you brought her here to discipline her?"
    #TODO Choice list
    mc.name "I didn't call you here to discipline you."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "happy")
    "She looks visibly relieved."
    the_person "Oh... you're not? Then... what did you want me here for?"
    "You clear your throat. You are going to have to phrase this very carefully."
    mc.name "Well, I had a great time at the concert the other night, and honestly I've gotten very fond of you..."
    "[the_person.title] smiles and blushes a bit. She is a little shy, but so cute when she does that."
    mc.name "So, before I move on, I just want you to know that I want to support you and help you in any way that I can."
    "Her face changes to a look of confusion."
    the_person "Help with what?"
    mc.name "I'm sorry, this is a difficult topic but... I was watching some pornography before I went to bed not long ago..."
    "The look on her face changes to pure horror."
    mc.name "I... was rather shocked to see a familiar face..."
    "She begins to stutter out a response."
    the_person "That... that wasn't... I'm sorry sir that..."
    mc.name "Sorry? [the_person.title] you don't need to apologise."
    the_person "I'm... huh? I don't?"
    mc.name "Of course not, it definitely looked like you were being filmed without your knowledge."
    the_person "Yeah... I had no idea... but what happened in the vid..."
    mc.name "It was between two consenting adults. Other than the recording anyway. It's okay."
    the_person "You aren't... grossed out by it?"
    mc.name "Grossed out? Why would I be grossed out?"
    the_person "I mean... the relationship I had with my last boyfriend was... not normal."
    mc.name "Hey, everyone has kinks. I'm not here to kink-shame you."
    the_person "And I mean... I was on break, but it was on company property... well my previous company anyway."
    mc.name "As far as I'm concerned, break time is yours to do what you want, as long as you can get some privacy anyway."
    "She looks down and thinks for a bit."
    the_person "The, umm... the video. Did you watch the whole thing?"
    mc.name "Yeah... yeah I did."
    "She looks a little sheepish, but continues."
    the_person "Did you... you know... like it?"
    "Wow, the conversation appears to be turning quickly."
    mc.name "I did. You're very sexy."
    "She gets a wide smile on her face."
    the_person "I'll admit it... I kind of like it... when guys let me take over a little bit..."
    $ mc.change_locked_clarity(10)
    $ the_person.discover_opinion("taking control")
    "Good to know for certain, but this was fairly obvious at this point."
    mc.name "A little bit?"
    "She chuckles."
    the_person "You've been so nice to me... Can I return the favour?"
    mc.name "You don't need to do that..."
    the_person "Oh, but I want to..."
    "She leans closer to you and whispers."
    the_person "I really want to... I want to make you feel good..."
    $ mc.change_locked_clarity(20)
    "DAMN. You feel your pants get a little tight after that. You remember from the video the way [the_person.title] took control and rode her ex..."
    mc.name "I mean, you don't have to do that..."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She gets up and walks around your desk. You stand up too."
    the_person "It's okay. I'm going to. You just enjoy."
    "With nothing else to say, [the_person.possessive_title] reaches down and begins to stroke your cock through your pants."
    the_person "Mmmm, I can tell you want it too!"
    "[the_person.title] has some skilled hands... You close your eyes and enjoy her stroking you for a moment."
    $ mc.change_locked_clarity(20)
    "You hear a zipper, some fabric rustles for a moment, then suddenly you feel her warm hand on your dick, skin to skin. You look down and see her pulling your dick out."
    if the_person.has_taboo("touching_penis"):
        the_person "Oh my god... it's so big... You've been hiding this from me, [the_person.mc_title]?"
        "She gives you a couple eager strokes. You can only moan in response. It feels good to finally feel her hands on you."
        $ the_person.break_taboo("touching_penis")
    else:
        the_person "God, it's so big. I love getting your cock out..."
        "She gives you a couple eager strokes. You can only moan in response."
    $ mc.change_locked_clarity(20)
    "She looks into your eyes as she continues to give you a handjob."
    the_person "Alright, don't hold back now."
    call get_fucked(the_person, start_position = handjob, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_ashley_first_handjob_01
    $ scene_manager.update_actor(the_person, position = "stand3")
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "You stand there with your eyes closed, slowly recovering. When you open them, you survey the mess you made."
    else:
        "You haven't finished, but [the_person.title] is still standing there with your dick in her hand."
    "Suddenly you hear your office door knob click and the door start to open. You forgot to lock it!"
    $ scene_manager.add_actor(stephanie, display_transform = character_left_flipped)
    stephanie "Hey [stephanie.mc_title] sorry to bug you but... oh fuck!"
    "It doesn't take [stephanie.title] long to survey the situation."
    stephanie "Holy shit, Ash! I didn't mean... I forgot to knock! Oh fuck!"
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "[stephanie.possessive_title!c] turns to flee the room."
    the_person "Oh my god... Steph this isn't what you think..."
    $ scene_manager.remove_actor(stephanie)
    "[stephanie.title] slams the door as she leaves the room."
    the_person "Oh no... oh god, how am I going to explain this?..."
    the_person "I'm sorry [the_person.mc_title]. I have to go!"
    "[the_person.title] quickly rushes to leave. You've barely had time to process everything that just happened."
    mc.name "[the_person.title]..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    the_person "Don't say anything... I just need to go..."
    $ scene_manager.remove_actor(the_person)
    "[the_person.possessive_title!c] quickly leaves the room."
    "Welp, you just got a handjob from [the_person.title]... and then her sister promptly walked in and witnessed the whole thing."
    "You'll have to consider how to approach both girls carefully before you talk to them next."
    $ scene_manager.clear_scene()
    $ add_ashley_post_handjob_convo_action()
    $ jump_game_loop() # she runs after her sister so end talk with Ashley
    return

label ashley_post_handjob_convo_label(the_person):
    "You decide not to give [the_person.title] too much time to overthink what happened in your office. You swing by her desk."
    $ the_person.draw_person()
    mc.name "Hey [the_person.title]..."
    the_person "Oh... haha, yeah, I figured something like this was coming... it's okay, I'll clean out my desk and be out before you know it..."
    mc.name "Clean out your desk? I'm not firing you. Come on, let's go get some coffee."
    if the_person.should_wear_uniform:
        the_person "Oh, coffee? Ok, I'm going to change and we can go."
        $ the_person.apply_outfit(the_person.planned_outfit)
        $ the_person.draw_person()
        the_person "I'm ready."
    else:
        the_person "Oh, coffee? I'm right behind you..."
    "[the_person.possessive_title!c] is blushing hard. It's kind of cute actually."
    $ downtown.show_background()
    "As you step out of the office building, [the_person.title] is following along behind you. You give her a second to catch up so you can walk side by side."
    "She's looking down at her feet, you can tell she is uncomfortable."
    menu:
        "Hold her hand" if the_person.love >= 20:
            mc.name "Don't worry, [the_person.title]. I just wanted to get out of the office to chat about things. Also to limit the possibility of an interruption..."
            "You reach your hand down and take her hand in yours. It startles her a little, but she quickly looks up at you."
            mc.name "I've really been enjoying spending time with you."
            the_person "Oh... that's... nice to hear. Thank you."
            $ the_person.change_stats(love = 5, happiness = 5, obedience = 5)
        "Hold her hand \n{menu_red}Requires 20 Love{/menu_red} (disabled)" if the_person.love < 20:
            pass
        "Reassure her":
            mc.name "Don't worry, [the_person.title]. I know we both need a chance to think about things, and I always find that coffee helps me think."
            the_person "Yeah... I suppose a coffee would be good for that..."
            $ the_person.change_stats(obedience = 5)
        "Tell her it was hot" if the_person.sluttiness >= 20:
            mc.name "Don't worry, [the_person.title]. I had a great time at the concert... and what happened in my office was fucking hot..."
            "[the_person.possessive_title!c] looks up at you, a bit surprised by your comment."
            the_person "Oh... I'm glad you think so..."
            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 40)
        "Tell her it was hot \n{menu_red}Requires 20 Sluttiness{/menu_red} (disabled)" if the_person.sluttiness < 20:
            pass
    "You get to the coffee shop. You order a couple coffees and sit down in a booth across from [the_person.possessive_title]."
    $ coffee_shop.show_background()
    #TODO if Alexia still works here
    $ the_person.draw_person(position = "sitting")
    "You take a few sips of your coffee. Finally you break the silence."
    mc.name "So... obviously working in an office with your sister, we should be careful about what we do... around the office..."
    "She takes a sip. She nods a bit, but doesn't yet chip in with her opinion."
    mc.name "I mean... I would like for things to continue... Is that what you are thinking?"
    "She takes a deep breath before speaking."
    if ashley_steph_relationship_status() == "stephanie":
        the_person "Well... I mean... we're sisters, so we talk about everything. Ever since you started the business up, she's been talking about you, almost non-stop..."
        the_person "She definitely has a thing for you... it would be wrong for me to let you pursue anything further with me..."
        mc.name "I understand that, but isn't what I want important too? I've known [stephanie.fname] for years, but I've only just recently met you."
        the_person "I... I guess..."
    elif ashley_steph_relationship_status() == "ashley":
        the_person "Yeah... I mean, I guess this whole thing has just happened really fast, but I would be lying if I said it wasn't exciting me."
        the_person "I'm just not sure what to tell Steph... she means the world to me, and I feel like she might've sort of had a thing for you, but I'm not sure."
        mc.name "Yeah, that is something to consider."
    else:
        the_person "Honestly... I'm just really confused right now. Steph and I... we're sisters! She means the world to me and we talk about everything!"
        the_person "Ever since you started this business thing up, she's been talking about you non-stop. I can tell she really likes you..."
        the_person "But... I know we only just met... but I... errm..."
        mc.name "Yes?"
        "She sighs."
        the_person "I guess... I kinda like you too..."
        the_person "I know this is kinda weird but... I guess you'll just have to like... decide? Who do you want to be with more?"
    "You consider your conversation carefully before deciding on how you want to proceed."
    menu:
        "Let's keep us secret":
            mc.name "I think I know what to do, where we can all be happy."
            the_person "Oh?"
            mc.name "Alright, let me explain the whole thing before you make up your mind. What if we keep things between us strictly physical, and don't tell [stephanie.fname]?"
            the_person "Errrm... you want to do what now?"
            $ the_person.change_stats(love = -5, happiness = -5, obedience = 5)
            mc.name "Look, [stephanie.fname] was the one in the first place that told me to ask you out. She wants you to be happy, and I think she knows you're going through a dry spell."
            mc.name "I'll help take care of your physical needs... then if you happen to find another guy or if things with your sister don't work out..."
            the_person "I don't know... I'm not sure I'll be able to lie to her about this..."
            mc.name "You don't have to lie about it, just don't talk about it. It'll be just like friends with benefits... but just between you and me."
            "She is struggling with the idea a bit, but finally makes up her mind."
            the_person "I guess we could try... but if it gets weird, I'm out, okay?"
            mc.name "Okay."
            the_person "And you have to go talk to her about what happened... you know... in your office..."
            mc.name "I'm sure I can handle that."
            "She bites her lip."
            the_person "Okay... let's give it a shot."
            $ the_person.event_triggers_dict["story_path"] = "secret"
            # $ assign_jealous_sister_role(the_person, stephanie)
        "I want to be friends with both of you" if ((ashley_steph_relationship_status() == "both" or mc.charisma > 4) and not stephanie.is_girlfriend):
            mc.name "There are a lot of feelings going on right now, but I think we all need to calm down a bit."
            mc.name "[stephanie.fname] and I go back a ways, but I just think of her as a friend."
            mc.name "I'm not going to lie, I really enjoy the way things are developing between us... but I have to be honest. I'm not looking to get tied down right now."
            the_person "Ahh... I see..."
            mc.name "I understand though, that everyone has needs. If you want some help relieving sexual tension, I'd be glad to help you out whenever you need it."
            "[the_person.title] looks confused for a moment."
            the_person "You mean... you want to be friends... with benefits?"
            mc.name "Exactly."
            the_person "Wow... I mean... I guess that would be okay..."
            $ the_person.event_triggers_dict["story_path"] = "fwb"
            the_person "I don't... I'm not sure how to talk to Steph about this though..."
            mc.name "Don't worry, I'll talk to her."
    "You drink your coffee with [the_person.title]. You are happy you were able to come up with a solution."
    the_person "This place is nice... maybe I should bring Steph here some time..."
    "Eventually you finish up. You decide to head back to the office."
    mc.name "I'm going to head back, feel free to take the rest of the day off if you need to."
    the_person "Ahh, thank you..."
    $ mc.location.show_background()
    $ add_ashley_stephanie_arrange_relationship_action()

    call advance_time() from _call_advance_ashley_post_hj_01
    return

label ashley_stephanie_arrange_relationship_label(the_person):
    "It's time to talk to [the_person.title]. You approach her in the lab."
    mc.name "Hey, we need to chat. Can you come with me to my office?"
    the_person "Sounds good."
    "You walk to your office. She enters first, and you close the door behind your back as you both take a seat."
    $ mc.change_location(ceo_office)
    $ the_person.draw_person(position = "sitting")
    mc.name "So, I want to talk to you about me and [ashley.fname]..."
    the_person "Yeah, I figured. Look, I know, I encouraged the whole thing, so I shouldn't be surprised when you two were messing around..."
    if ashley_is_secret_path():
        mc.name "It's not like that, [the_person.title]. Me and [ashley.fname] got caught up in the moment, yes, but we've talked it over and decided to be just friends."
        "You feel a little bit bad about trying to keep your relationship with [ashley.possessive_title] a secret, but you're sure if you play your cards right it'll be worth it long term."
        if the_person.is_girlfriend:
            the_person "I have to admit... I'm a little bit relieved to hear that. I thought I was losing my boyfriend! And to my sister!.. we haven't always gotten along, but I was really hoping it hadn't come to that."
            mc.name "I'm sorry for what happened. It won't happen again."
        else:
            the_person "I... I don't understand... Why aren't you interested in [ashley.fname]?"
            mc.name "It isn't that I'm not interested, as much as that I'm currently interested in someone else..."
            "You give [the_person.title] a wink. When she realises what you mean, she blushes."
            the_person "Oh wow, I didn't realise that you felt the same way... Oh [the_person.mc_title]... Can we just make it official? I want everyone to know that I'm your girlfriend!"
            "Realising that your plan to keep things secret with [ashley.title] isn't going to work unless you take things further with [the_person.title], you agree."
            mc.name "Here, let me do this, officially. [the_person.title], will you be my girlfriend?"
            the_person "Yes! Oh yay! I thought for sure you were gonna get with [ashley.fname]... I was so jealous... When I saw..."
            $ the_person.add_role(girlfriend_role)
            mc.name "I'm sorry, it won't happen again."
        the_person "... I guess I should warn you about this. This isn't the first time this has happened..."
        mc.name "Oh?"
        the_person "When we were in high school, she was too shy to get any boyfriends... sometimes when I would bring a guy home, she would try to seduce him."
        the_person "It caused a lot of friction between us. She kept claiming she was just trying to 'protect me' by weeding out the bad ones."
        the_person "Sometimes though, they would fuck for weeks before I found out about it..."
        mc.name "I see."
        the_person "Anyway, I just wanted to give you a warning that this could come up again in the future."
        mc.name "Thank you for letting me know."
        "[the_person.title] jumps up, you stand up also as she walks around the desk."
        $ the_person.draw_person(position = "kissing")
        "You put your arms around her and you pull her close. You bring your face to hers and you kiss for a few moments. She slowly steps back."
        $ the_person.draw_person(position = "stand2")
        the_person "Alright... I'm going to get back to work. I'm so glad we got to talk!"
        $ the_person.draw_person(position = "walking_away")
        "As [the_person.possessive_title] leaves the room, you wonder if you are being smart. Keeping your relationship with her sister secret, even if it's only physical, might be difficult."
    elif ashley_is_fwb_path():
        mc.name "I know it seems like things between [ashley.fname] and I are moving really fast, but I want you to know it probably isn't what you are thinking."
        the_person "Oh? I mean... You went on a date and then she was giving you a handjob in your office..."
        mc.name "[ashley.fname] is an interesting girl, for sure, but I'm not interested in a relationship with her. We both have some physical needs, so we've decided to be friends... With benefits..."
        if the_person.love > 50:
            the_person "Wow... Okay... I did not see that coming."
        if the_person.has_taboo("vaginal_sex"):
            mc.name "We're all adults here. She knows that if she finds someone else there's no commitment. And she knows it's the same for me, if I were to happen to start dating someone."
        else:
            mc.name "It's nothing different than what has been going on between us. Don't worry, I know you have needs too."
        the_person "That's understandable. I mean, I get it, what is going on, it just surprises me."
        the_person "It might be a little weird... you know? Getting physical with a guy who is doing the same with my sister... but you're right. We're all adults here, getting what we want from each other, consensually."
        $ the_person.draw_person(position = "stand2")
        the_person "Alright. I'm glad we got to talk about it. It makes me feel better, knowing what is going on between you two. I think I'll get back to work."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title!c] turns and walks out of your office. Both girls are sexy, and you feel like your prospects are better if you can keep them from competing with each other for your attention."
    else:
        mc.name "I honestly was not expecting this to happen so quickly either. We went on that date, and had a great time."
        mc.name "We started with just chatting, but it was like we couldn't keep our hands off each other... And then you walked in..."
        if the_person.love > 50:
            "[the_person.title] is looking down, not making eye contact. You know she has feelings for you also, and is struggling with your newfound affection for her sister."
            the_person "That's... I mean, I guess I'm a good matchmaker, eh? I encouraged the whole thing, I shouldn't be surprised by it..."
            mc.name "And thank you for that. If it weren't for you, I never would have met [ashley.fname]."
            the_person "Yeah... Just being honest here... It's hard not to be a little jealous?"
            mc.name "I'm sorry... I'll try not to make things awkward..."
            the_person "I guess that means we probably shouldn't fuck anymore..."
            mc.name "I guess not..."
        else:
            the_person "Honestly, I'm really happy for you two. I was just caught off guard when I walked in on you two..."
            if the_person.sluttiness > 40:
                the_person "It's going to be hard for me to keep my hands off of you from now on, but my sister deserves it. We may not have always gotten along, but I'm glad she's found someone like you."
            else:
                the_person "Ash is a special girl, okay? You better take good care of her. We may not have always gotten along, but I'm glad she's found someone to make her happy."
        mc.name "Thank you. It means a lot to get your approval of this."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title!c] stands up and smiles. It looks a little forced, but she's trying to be genuine."
        the_person "Thank you for this chat. I feel better knowing what is going on with you two. Now... I think I'll get back to work?"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] turns and leaves your office. Things got a little sticky there, but you feel like you are now in the clear to pursue things with [ashley.title] from now on."
    $ clear_scene()
    $ add_ashley_blows_during_meeting_action()
    call advance_time() from _call_advance_ashley_arrangement_01
    return

label ashley_blows_during_meeting_label():      #40 Sluttiness
    $ scene_manager = Scene()
    $ mc.reset_arousal()
    "You get a text from [stephanie.possessive_title]."
    $ mc.start_text_convo(stephanie)
    stephanie "Hey, can you meet me in your office? I just found something I wanted to talk to you about."
    if mc.is_at(ceo_office):
        mc.name "Sure, come on over."
        "Soon, you hear a knock on the door."
    else:
        mc.name "Sure, I'll be right there."
        $ mc.change_location(ceo_office)
        "You head to your office and sit down. Soon, you hear a knock on the door."
    $ mc.end_text_convo()
    mc.name "Come in."
    $ scene_manager.add_actor(ashley)
    mc.name "[ashley.title]?"
    ashley "Shh, Steph is coming! Don't say a word, or she'll know what I'm doing!"
    mc.name "And what exactly are you doing?"
    $ scene_manager.update_actor(ashley, position = "blowjob", display_transform = character_left_flipped(yoffset = .35, zoom = 1.45))
    "[ashley.possessive_title!c] quickly slides under your desk and unzips your pants, pulling your cock out."
    mc.name "Are you serious? Is this really the right time for..."
    $ scene_manager.update_actor(ashley, position = "blowjob", special_modifier = "blowjob")
    $ ashley.increase_blowjobs()
    "[ashley.title] engulfs the entirety of your rapidly hardening cock in her mouth, stopping your words in your throat."
    $ mc.change_locked_clarity(30)
    "It only takes a few moments to reach full hardness as she starts to work your cock over with her soft lips."
    "Of course, there is another knock at the door. You look up."
    $ scene_manager.add_actor(stephanie)
    stephanie "Hey, it's me."
    mc.name "Come in and have a seat."
    stephanie "Thanks."
    $ scene_manager.update_actor(stephanie, position = "sitting")
    "[ashley.title] continues to bob her head up and down your cock while her sister sits down across from you. Somehow she is completely silent?"
    $ mc.change_locked_clarity(30)
    mc.name "What can I do for you?"
    stephanie "Ah, well, I'm having some trouble with the synthesis on one of the latest serum designs, I was wondering if you could look at it."
    "Fuck, you aren't sure you can handle science talk right now..."
    "Those pouty lips are working wonders sliding up and down your cock... you just wanna grab her by her [ashley.hair_description]..."
    $ mc.change_locked_clarity(40)
    mc.name "What issues are you having?"
    "[stephanie.possessive_title!c] grabs a folder from her bag and hands it to you."
    stephanie "Well, some of the new components are separating out. We tried a basic emulsifier, but they seem to be immune to normal protein binding..."
    "With your right hand, you take the folder. With your left hand, you grab [ashley.possessive_title] by the back of her [ashley.hair_description]."
    mc.name "I see. Have you tried homogenizing it?"
    stephanie "We have, actually..."
    if ashley.is_bald:
        "[stephanie.title] starts to talk about some of the other methods they've been using. You use your hand at the back of [ashley.title]'s neck and force your cock down her throat."
    else:
        "[stephanie.title] starts to talk about some of the other methods they've been using. You use your hand in [ashley.title]'s hair and force your cock down her throat."
    "She manages to throat you for several seconds, but eventually sputters and gags. When you let go she quickly pulls off and gasps. You pretend to cough to cover up the noise."
    $ mc.change_locked_clarity(40)
    stephanie "Ah, you okay?"
    mc.name "Yes, sorry, please continue."
    "[ashley.possessive_title!c] takes you in her mouth again as her sister continues to talk about the serum issue."
    "[ashley.title]'s soft mouth is working your shaft hard. There is no way you don't cum soon."
    stephanie "Actually, maybe if I homogenized the base before we mixed in the catalyst, that would help..."
    mc.name "Yes I think that sounds... good..."
    $ mc.change_locked_clarity(40)
    "You put your hand on [ashley.possessive_title]'s head and force her down again as you start to cum, right down her throat."
    $ ashley.cum_in_mouth()
    $ scene_manager.update_actor(ashley)
    "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her [ashley.hair_description]."
    $ play_swallow_sound()
    "You do your best to remain absolutely silent, but you see [stephanie.title] looking at you confused."
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = ashley)
    stephanie "Are you okay? You seem a little... flushed."
    mc.name "Sorry, it has been a long day and I'm a bit tired."
    stephanie "Okay... well, I'll leave you alone for now then, and I think I have some new ideas for how to deal with the issue."
    stephanie "Thanks!"
    mc.name "Anytime."
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "You watch as [stephanie.possessive_title] walks out of your office and closes the door on her way out."
    $ scene_manager.remove_actor(stephanie)
    mc.name "Holy fuck, you couldn't pick a different time to do that?"
    "[ashley.title] looks up at you from below your desk, a bit of cum she didn't manage to swallow dribbling down her chin."
    ashley "Sure, but it wouldn't have been as fun otherwise."
    $ scene_manager.update_actor(ashley, position = "stand3", display_transform = character_center_flipped(yoffset = 0, zoom = 1.0))
    $ scene_manager.apply_outfit(ashley)
    "[ashley.possessive_title!c] gets up and straightens her outfit."
    ashley "Until next time..."
    $ scene_manager.clear_scene()
    "Your office now empty, you can't help but shake your head. Are you in over your head with those two sisters?"
    $ add_ashley_supply_closet_at_work_action()
    return

label ashley_supply_closet_at_work_label():   #60 sluttiness
    $ the_person = ashley
    $ the_person.arousal = 50
    "Taking a break from your work, you are walking down the hall when you start to pass [the_person.title]."
    $ the_person.draw_person()
    "Instead of letting you walk by her, she quickly steps in front of you."
    the_person "Oh! [the_person.mc_title]! I need your help with something right away, follow me!"
    $ the_person.draw_person(position = "walking_away")
    "She doesn't wait for your response, but turns and starts to walk in front of you."
    "You are definitely a little suspicious of her motives, but for now, you follow her."
    the_person "It's just right in here..."
    "You step through a door with [the_person.title], quickly realizing it to be a supply closet."
    mc.name "[the_person.title]... what is this about..."
    $ the_person.draw_person(position = "kissing")
    "She quickly turns around and embraces you."
    the_person "I couldn't wait until this evening, Steph kept going on and on this morning at breakfast about sex with you."
    the_person "You're supposed to be keeping up with both of us... it isn't fair she's been getting all your attention!"
    mc.name "Are you getting a little jealous of her?"
    "You reach around her and grab her ass, pulling her into you."
    the_person "Duh? Isn't that obvious?"
    $ the_person.draw_person(position = "blowjob")
    "She drops to her knees and quickly pulls your cock out. She gives it a few strokes to make sure you are good and hard."
    the_person "Jesus... No wonder she won't shut up about it. I bet this thing feels so good..."
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "stand3")
    "She stands up again."
    the_person "I'm sick of messing around... let's fuck!"
    "You feel a pang of guilt, knowing that this will hurt [stephanie.possessive_title] when she finds out eventually."
    $ the_person.strip_to_vagina()
    "However, as [the_person.possessive_title] strips down, you decide to let yourself indulge."
    the_person "Come on, I'm ready for you... mmm!"
    $ the_person.draw_person(position = "against_wall")
    "You easily pick [the_person.title] up and pin her against the closet wall."
    "She reaches down and takes your cock in her hand, lining it up."
    "Her legs wrap around your back and she eagerly pulls you in. You let yourself get pulled into her and your bare cock slides into her waiting pussy."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(20)
    $ play_moan_sound()
    $ the_person.change_arousal(25)
    "She moans in your ear and she wraps her arms and legs around you as you begin to fuck her."
    "The closet fills with the sound of soft gasps and noises of sex."
    if stephanie.is_girlfriend:
        the_person "That's it, fuck your girlfriend's sister..."
    else:
        the_person "Fuck, getting your dick wet with two sisters. You must be so proud of yourself..."
    "Never stick your dick in crazy. Isn't that how the saying goes? Unfortunately, good sense has gotten to you too late."
    $ mc.change_arousal(30)
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "You don't respond with words, but instead you pick up the place, slamming your cock in and out of her."
    the_person "Jesus... fuck me [the_person.mc_title], you're gonna make me cum...!"
    "[the_person.title]'s feet lock behind you and urges you to fuck her faster as she starts to orgasm."
    $ the_person.have_orgasm()
    "Her entire body starts to spasm and you fuck her straight through it. She buries her face in your shoulder to stifle her moans from getting too loud."
    $ mc.change_arousal(30)
    $ mc.change_locked_clarity(50)
    "Feeling [stephanie.title]'s crazy sister cum all over your cock has you approaching your own orgasm. Suddenly you realise you need to figure out how to finish."
    mc.name "Oh fuck, I'm..."
    "The feet locked behind you don't let up, instead she whispers in your ear."
    the_person "Mmmm, does Steph ever let you cum inside her? She probably does, I think we're both kind of slutty like that..."
    if stephanie.is_girlfriend:
        the_person "But of course, she's your girlfriend. It only makes sense she'd be taking your cum every chance she gets..."
    else:
        the_person "But of course, she's always had a thing for you. I bet she takes your cum every chance she gets..."
    if the_person.on_birth_control:
        the_person "Don't worry, I'm on the pill. Just cum inside me!"
    else:
        if stephanie.is_girlfriend:
            the_person "I'm not on birth control though. Can you imagine? Knocking up your girlfriend's sister?"
        else:
            the_person "I'm not on birth control, but what are the odds you knock me up with just one little creampie?"
    "The legs locked around you don't really give you a choice. Even though you have her up against the wall, you feel like you aren't really in control of it."
    $ mc.change_arousal(30)
    $ mc.change_locked_clarity(50)
    "The pleasure builds too fast and you get ready to finish."
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "against_wall")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)







    "In this label, Ashley approaches MC, jealous about how much he's been banging her sister and not her."
    "Drags him into a supply closet. MC pins her to the wall."
    $ add_ashley_asks_for_anal_action()
    return

label ashley_asks_for_anal_label(): #80 sluttiness
    "In this label, Ashley approaches MC for anal."
    "If MC has had anal with Steph, Ashley talks about how hot it was she could barely walk when you got done with her."
    "If not, Ashley wants to one up her sister getting taken anally."
    $ add_ashley_tests_serum_on_sister()
    return

label ashley_tests_serum_on_sister_label(): #100 sluttiness, also requires drinks out and arousal serum quest complete.
    "In this label, Ashley calls MC to the testing room, where she has drugged Stephanie with the arousal serum."
    "Offers her sister as a 'gift' for MC's enjoyment."
    "Watches as you fuck her sister senseless. When you finish, she blows MC back to erection, then gets on top of her sister and asks for the same treatment."
    "At the end they both enter MC's harem properly."
    return
