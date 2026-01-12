# Labels for the Starbuck Rebecca teamup
#This scene should roughly mimic actions Starbuck has taken to bring in more business, but with both girls.
# This scene is of the multiple choice type, but will generally progress from lower selections to higher.
#STAGES:
#0: Rebecca works on finances, but watches as you create an advertisement with Starbuck
#1: Rebecca and Starbuck work together to create a lingerie advertisement (Optional double tit fuck)
#2: Girls work together for makeup advertisement with dual blowjob scene
#3: Advertisement for "easy access" clothing line, bend them both over a desk
#4: Advertisement for products designed for anal play. Use strap on to fuck both girls in the ass.

#All stages should present opportunity to build sluttiness a bit.


label starbuck_rebecca_teamup_setup_one_label(the_person, skip_intro = False):
    # the_person == rebecca
    if skip_intro:
        mc.name "Actually [the_person.title], I already know of someone else who could really use your accounting services too."
        the_person "Oh? What is the situation?"
    else:
        the_person "Hey [the_person.mc_title], how are you doing today?"
        mc.name "Pretty good."
    mc.name "I've actually invested in a local business, but I recently discovered that the owner running the place is not good with finances."
    mc.name "She works hard, but she needs help from a financial professional."
    the_person "Do I know her?"
    mc.name "Her name is [starbuck.fname], and she runs a local... let's say it is an adult store."
    mc.name "She sells products made for sexual use."
    the_person "Oh! Oh wow. And you... invested in the store?"
    mc.name "I did. She is a great person, dealing with the loss of her late husband, and is a great business owner, other than her financial sense."
    mc.name "I recently set her up with a tax ID... she had been paying sales tax on her stock..."
    the_person "What... but why?"
    mc.name "She just didn't know any better."
    the_person "But... but... Is she getting wholesale pricing from distributors? What is her leasing agreement like? Are the utilities in her name or the business?"
    mc.name "I... have no idea to any of those."
    the_person "I think I could save your friend a lot of money. Would you talk to her? Set us up with a time for an initial consultation."
    the_person "Hell, I'll even do it gratis if I can't find a way to save her a significant amount of money."
    mc.name "Wow, okay. I'll talk to her and let you know!"
    $ add_starbuck_rebecca_teamup_setup_two_action()
    if not skip_intro:
        the_person "Was there anything else you needed?"
    return


label starbuck_rebecca_teamup_setup_two_label(the_person):
    # the_person == starbuck
    "You walk up to [the_person.title], working the counter at the sex shop."
    mc.name "Hello. I have some good news."
    the_person "Hey. What's that?"
    mc.name "I found someone willing to do some accounting work for you part time."
    the_person "Oh? Who is it?"
    mc.name "So, it is actually my Aunt. She is recently divorced, and has renewed her CPA license. She is looking for part time work."
    mc.name "When I told her about you, she rattled off four or five accounting questions that I had no idea about, but it seemed like she could probably save you some money."
    the_person "Hmm... your Aunt? And she was okay with helping out... at a sex shop?"
    mc.name "She was surprised that I had some business dealings here, but quickly agreed when we started talking about the details."
    the_person "And she is trustworthy?"
    mc.name "Definitely. I let her crash at my place while she looked for an apartment in the area after the divorce."
    mc.name "Just say the word, and I'll text her now with info. Her schedule is pretty open to coming out any time."
    the_person "Well... I don't know... how about Friday mornings?"
    the_person "I don't open until the afternoon, so that would give me a chance to set financial goals for the next week, without bringing her out at a weird time."
    mc.name "Sure. I'll set her up with the details. For the first time, I'll plan to come out with her."
    mc.name "We'll all meet here, Friday morning. And if it turns out she can't help much, no worries, she's just looking for some part time gigs anyway."
    the_person "Okay! Sounds great! I'll be here!"
    $ starbuck.set_schedule(sex_store, day_slots = [4], time_slots = [1])
    $ add_aunt_cpa_job_for_starbuck()
    "You pull out your phone and quickly text [aunt.possessive_title] the time and place to meet on Friday."
    "She quickly texts you back confirming it works."
    "Sounds like you've got an appointment on Friday with [the_person.fname] and [aunt.fname]!"
    "You'll have to look for opportunities for them to spend lots of quality time together. Who knows what you might be able to accomplish at the financial meetings."
    $ add_starbuck_rebecca_teamup_intro_action()
    $ mc.new_repeat_event(f"{starbuck.fname} and {aunt.fname} budget", 4, 1)
    return

label starbuck_rebecca_teamup_intro_action_label():
    $ mc.change_location(sex_store)
    call progression_scene_label(starbuck_rebecca_teamup, [starbuck, aunt]) from _starbuck_rebecca_teamup_scene_call_test_03
    return

label starbuck_rebecca_teamup_action_label(the_person):
    $ mc.change_location(sex_store)
    call progression_scene_label(starbuck_rebecca_teamup, [starbuck, aunt]) from _starbuck_rebecca_teamup_scene_call_test_02
    return

label starbuck_rebecca_teamup_intro_scene(the_group):
    #For the first time through this scene, we establish that Rebecca can save Starbuck a lot of money. She agrees to come back every week.
    #Starbuck references some of her advertisement efforts. Asks Rebecca if she would be okay with her working on weekly adverts while she is there working on

    "You step into the Sex Shop. The sign says closed but the door was unlocked. After a quick look around you see [starbuck.possessive_title]."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(starbuck, display_transform = character_center_flipped)
    "She is in the back, and appears to be messing with her laptop. She hears you approach and looks over at you."
    starbuck "Good morning [starbuck.mc_title]."
    mc.name "Good morning. I see it is just us so far?"
    starbuck "Yeah, so far."
    mc.name "Don't worry, my aunt is usually pretty punctual. I'm sure she will be here soon."
    starbuck "Yeah. I'll admit it though, I'm a little bit nervous. I keep getting worried she is going to discover I have like... a bunch of unpaid taxes or something!"
    mc.name "Doubtful, but even if that were the case, wouldn't it be better to know about it now?"
    starbuck "Yeah... I suppose..."
    "You make some small talk with [starbuck.title] for a while. Soon, you hear the entry door open and close."
    $ scene_manager.add_actor(aunt)
    mc.name "Ah, hello [aunt.fname]."
    "[aunt.possessive_title!c] is looking around at the shop a bit wide eyed, as she walks over to where you are standing."
    aunt "Ah, hello there [aunt.mc_title]. And you must be [starbuck.fname]?"
    mc.name "Yes! [starbuck.fname], this is [aunt.fname] and likewise."
    starbuck "Hello! It is great to meet you!"
    aunt "Nice to meet you as well."
    starbuck "So... I'm just going to admit it... I'm really nervous about this."
    starbuck "I'm not very good at finances... my husband used to take care of all of that kind of thing for us..."
    aunt "Don't worry, just show me what you have and I'll see what I can do. I don't know if [aunt.mc_title] told you, but I'm happy to take a look and see what I can do."
    aunt "I think I'll be able to help you out with some things."
    starbuck "Alright... I keep all my records on this..."
    "[starbuck.title] points at the laptop. [aunt.possessive_title!c] walks over and sits down at the desk."
    $ scene_manager.update_actor(aunt, position = "sitting")
    "[starbuck.possessive_title!c] leans over and loads up the relevant financial software."
    $ scene_manager.update_actor(starbuck, position = "standing_doggy")
    starbuck "Alright, so, I normally use this for accounts... and this..."
    "She spends a minute going over her records..."
    aunt "Alright, I see. Now, do you have records of inventory orders?"
    starbuck "Ah, right, yeah, that is over here..."
    "You can't help but check out [starbuck.possessive_title]'s shapely backside as she bends over the desk..."
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(30)
    "[aunt.possessive_title!c] pulls out a small notepad and a pen from her purse."
    aunt "Alright, I think I have enough to get started. I'm going to go over some things and see what I can do."
    starbuck "Okay! I'll be around if you have any questions."
    aunt "Perfect."
    $ scene_manager.update_actor(starbuck, position = "default")
    "[starbuck.title] stands up and turns to you."
    starbuck "Wow. My stomach is full of butterflies."
    aunt "Don't worry, you've at least left me very very good records. I already see a couple ways to save you some money!"
    starbuck "Oh my... amazing!"
    $ starbuck.change_happiness(5)
    starbuck "Well... I'm going to work on getting the store ready for opening. Care to help me?"
    mc.name "Sure. I scheduled myself to be here for a few hours, so I might as well make myself useful."
    $ scene_manager.update_actor(aunt,display_transform = character_right(zoom = 0.4))
    "You and [starbuck.title] step out into the aisle of the store, leaving [aunt.possessive_title] at the desk."
    "You spend some time with [starbuck.possessive_title], down stocking and front facing product."
    "You turn one aisle and start down another, where she has some lingerie for sale."
    "You hear [aunt.possessive_title] call out from the front of the store."
    aunt "Hey! Do you have a log of your orders? I'm looking for a specific vendor and I can't find it!"
    starbuck "One sec!"
    $ scene_manager.update_actor(starbuck, display_transform = character_center_flipped(zoom = 0.4), position = "walking_away")
    "[starbuck.title] walks up to the front of the store."
    "You look over at the lingerie sets. You remember a recent advertisement you made with [starbuck.possessive_title] where you dressed her up in a few outfits..."
    "You would love to get her in an outfit like that again... maybe you could convince her to shoot another advertisement?"
    "The store is closed, and you don't think [aunt.possessive_title] would mind..."
    $ scene_manager.update_actor(starbuck, display_transform = character_center_flipped, position = "default")
    "She returns after helping [aunt.title]."
    mc.name "Hey. Remember that advertisement we did, where you dressed up in a few different sets of lingerie?"
    starbuck "Ahhh, yeah. How could I forget that?"
    mc.name "That advertisement... it helped out didn't it? You saw an increase in sales?"
    starbuck "It did! I got several compliments from customers as well."
    mc.name "Hey... the store is still closed for a bit... want to make another one really quick?"
    mc.name "You could dress up, and I'll just snap a few quick pictures."
    starbuck "What... with [aunt.fname] here?"
    mc.name "Sure. Why not? I'm sure she won't mind."
    starbuck "I don't know..."
    mc.name "Here, let me ask her."
    "You yell up to the front of the store."
    mc.name "Hey, [aunt.fname]!"
    aunt "Yeah?"
    mc.name "Me and [starbuck.fname] are going to work on a new lingerie advertisement. You're okay with that, right?"
    aunt "Umm, yeah? Whatever you two need to do."
    mc.name "Great! Thanks!"
    "You look back at [starbuck.possessive_title]. Her cheeks are a little blushed with embarrassment, but she goes along with it."
    starbuck "You know, I was kind of meaning to do something for a new set of pink lingerie I got in recently..."
    mc.name "Great! Why don't you put some on?"
    starbuck "Ahh... fuck it. I'll do it! Let me go see what I have!"
    $ scene_manager.update_actor(starbuck, position = "walking_away")
    "She walks back to the stock room in the back, where the changing rooms are."
    $ scene_manager.hide_actor(starbuck)
    $ scene_manager.update_actor(starbuck, starbuck.personalize_outfit(Wardrobe.generate_random_appropriate_outfit(starbuck, outfit_type = "under"), opinion_color = "the colour pink"))
    "You walk up to the front of the store, where [aunt.possessive_title] is working."
    $ scene_manager.update_actor(aunt, display_transform = character_right(zoom = 1.0))
    mc.name "Hey, how's it going?"
    "She glances over at you."
    aunt "Great! I've got a list of seven things so far that are going to save her a lot of money. Unfortunately I did see one place though where she isn't saving enough."
    aunt "Overall I still have her well in the black. And this should keep her from getting surprised by a big transaction fee later on this year."
    mc.name "That sounds great!"
    $ scene_manager.add_actor(starbuck, display_transform = character_center_flipped, position = "stand2")
    "[starbuck.possessive_title!c] emerges from the back room. Her outfit is impressive."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    mc.name "Wow [starbuck.title]! This advertisement is going to be great. [aunt.fname] was just telling me she is already making progress."
    aunt "Yes, I've already found several places where you can save..."
    $ scene_manager.update_actor(aunt, position = "default")
    "[aunt.possessive_title!c] stands up and turns to face [starbuck.title], then stops when she see what she is wearing."
    aunt "... that's... WOW. I didn't really process what you meant by a lingerie ad!"
    "[starbuck.title]'s face turns red and she starts stammering."
    starbuck "I... I didn't... I'm... I can do this later!"
    aunt "No! No, it is quite alright. I just had my nose down in the books so much I didn't really process what [aunt.mc_title] was saying."
    aunt "By all means, continue... I'll give you a breakdown of things when I finish up... wow."
    $ scene_manager.update_actor(aunt, position = "sitting")
    mc.name "Wow is right. You look amazing."
    "[aunt.title] sits back down at the laptop. She starts typing, but you notice her glancing over at you and [starbuck.title] once in a while."
    starbuck "Alright, we've only got a little bit longer until the store opens. Let's get this done!"
    "She hands you her phone. You start the photo app."
    mc.name "Let's do the pictures right here. There is plenty of room by the counter here."
    mc.name "Strike a quick pose."
    starbuck "Hmmm, okay!"
    $ scene_manager.update_actor(starbuck, position = "stand4")
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(30)
    $ starbuck.change_arousal(5)
    "You quickly snap a few pictures."
    mc.name "Great! Now, why don't you get down on your knees for a seductive one..."
    starbuck "Hmm, okay."
    $ scene_manager.update_actor(starbuck, position = "blowjob")
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(30)
    $ starbuck.change_arousal(5)
    starbuck "How is this?"
    mc.name "Perfect... Love it!"
    "You snap several more."
    mc.name "Now, why don't you bend over the counter, show us the backside?"
    $ scene_manager.update_actor(starbuck, position = "standing_doggy")
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ starbuck.change_arousal(5)
    mc.name "Wow, yeah, that's it!"
    "You snap several pictures. You notice that [aunt.title] is watching intently now as [starbuck.possessive_title] models her sexy underwear."
    $ aunt.change_arousal(15)
    mc.name "That's it... just a few more..."
    mc.name "Got it!"
    $ scene_manager.update_actor(starbuck, position = "stand2")
    mc.name "Wow, those were great!"
    aunt "Yeah... I bet those are going to work great!"
    $ starbuck.change_happiness(3)
    starbuck "Ah, thank you both."
    starbuck "I'm going to get changed."
    aunt "Good! I am just about finished up for today."
    $ scene_manager.update_actor(starbuck, position = "walking_away")
    "[starbuck.title] turns and starts walking to the back, then disappears behind the stock room door."
    $ scene_manager.hide_actor(starbuck)
    aunt "[aunt.mc_title]... You take pictures like that for her regularly?"
    mc.name "Just once, but I feel like if we took them more regularly it would really help drive business here."
    aunt "No doubt. She is stunning..."
    "There is a long silence between the two of you."
    aunt "Are you two umm... you know..."
    $ starbuck.apply_planned_outfit()
    $ scene_manager.add_actor(starbuck, starbuck.outfit, display_transform = character_center_flipped, position = "stand2")
    "Thankfully, [starbuck.title] emerges from the back room before you have to answer the question."
    starbuck "Alright... I have to know... how bad is it, [aunt.fname]?"
    aunt "Bad? No no, your record keeping helped make this incredibly easy."
    aunt "[starbuck.fname], I can save you a significant amount of money. Here's what I can do..."
    "[aunt.title] starts naming off several improvements she can make to the business' cash flow. You kind of zone out as they talk."
    "[aunt.possessive_title!c] and [starbuck.title] working together... this could make for some very exciting encounters in the future."
    "You got lost in a day dream for a moment, imaging the two sexy ladies dressing up in sexy underwear... then getting down on their knees..."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "The end of the conversation pulls you out of your day dream."
    aunt "So, I propose that I come back once a week to work on this stuff. The money you save would more than pay for my accounting fees!"
    aunt "And then I'll run your books for you, and you can just focus on running the place!"
    starbuck "Oh my god, [aunt.fname], you are amazing! Let's do it!"
    starbuck "How does same time next week sound? We could do it every Friday morning, before the shop opens."
    "This sounds perfect! You decide to make sure you insert yourself into the meetings also."
    mc.name "When I can, I'll make it out also. I can help you with shop opening, and we could even shoot additional advertisements while [aunt.title] is working!"
    aunt "That's a great idea!"
    starbuck "Yay! Alright, same time next week!"
    $ scene_manager.update_actor(aunt, position = "default")
    aunt "I'll be here."
    mc.name "I can't promise I'll be here every week, but I'll come as often as I can."
    starbuck "Alright."
    $ scene_manager.clear_scene()
    "You, [starbuck.possessive_title], and [aunt.title] go your separate ways for now."
    "This is going to be an excellent opportunity. Having [aunt.possessive_title] running the books is going to help the shop be more profitable, making you more money."
    "You are pretty sure that with some convincing, you can get her involved making some of the advertisements as well."
    "You can now join [starbuck.title] and [aunt.title] every Friday morning at the Sex Shop."
    $ starbuck.event_triggers_dict["shop_promo_market_rate"] += 0.5
    return

label starbuck_rebecca_teamup_intro_0(the_group):
    $ aunt_chatter = get_random_from_list(["So if we wait to file until the end of the month...",
        "But the problem is that the interest actually accrues daily, so...",
        "Yeah, but there isn't any benefit to paying it off early, since there isn't any interest on...",
        "So unfortunately that could wind up actually decreasing margins on...",
        "We could wait and see if the prices dip a bit and then buy up some stock on..."])
    "You step into the Sex Shop. You walk over to the counter and see [starbuck.possessive_title] and [aunt.title] discussing something."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(starbuck, display_transform = character_center_flipped)
    $ scene_manager.add_actor(aunt)
    aunt "[aunt_chatter]"
    starbuck "Oh! Hey [starbuck.mc_title]!"
    "[aunt.possessive_title!c] stops in the middle of her sentence when she notices you."
    aunt "Ah, [aunt.mc_title], glad you could come. We weren't sure if you were going to make it or not."
    mc.name "Yeah, I was in the area and decided to swing by, since I knew you two were here."
    $ del aunt_chatter
    return




label starbuck_rebecca_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label starbuck_rebecca_trans_scene_1(the_group):
    starbuck "I've been really enjoying the lingerie ads. Can we do another one?"
    mc.name "Of course. And I'm not just saying that because I get to see you in sexy underwear."
    starbuck "Uh huh..."
    mc.name "It is definitely a part of, but not JUST because I want to."
    "[aunt.possessive_title!c] speaks up from the desk."
    aunt "Can't say I blame you. I wish I had a body like that to show off in such sexy clothes!"
    starbuck "Oh come on now, your body is fantastic."
    mc.name "Yeah, you are smoking hot. Why don't you join in? I bet [starbuck.title] could find a great outfit for you."
    aunt "Nonsense. Besides, I need to work on this, anyway."
    mc.name "I'm not joking. Having the two of you team up for a lingerie photo shoot would be a huge advertisement."
    "Sensing that her friend is on the edge of giving in, [starbuck.possessive_title] agrees."
    starbuck "Yeah! I can do some of it, but having an extra would be a large boon to the ad!"
    "She sighs and looks up from the computer."
    aunt "Well... I AM almost done with this..."
    starbuck "Ah! You just finish up, and I'll go pick out some outfits! This will be great!"
    "[starbuck.possessive_title!c] looks at you, but then suddenly stops."
    call starbuck_rebecca_strip_incest_label(the_group) from _starbuck_rebecca_teamup_incest_first_warning_01
    aunt "Alright, fine. Pick out the outfits, I'll finish up here shortly."
    $ mc.change_locked_clarity(20)
    starbuck "Alright! This is gonna be great!"
    $ scene_manager.update_actor(starbuck, position = "walking_away")
    "Awesome! You get to take pictures of [starbuck.possessive_title] and [aunt.title] in lingerie for an ad!"
    "This is certainly a big step in the right direction for what you have planned for these two..."
    $ scene_manager.hide_actor(starbuck)
    "After several minutes, [aunt.title] stands up."
    $ scene_manager.update_actor(aunt, position = "stand2")
    aunt "Well, that is enough accounting for today."
    aunt "Did... did you really mean it? You like my body?"
    mc.name "Of course I do. I'm going crazy waiting to see what outfits [starbuck.fname] picks out."
    aunt "Ah... I suppose I'd probably better go check on her."
    $ scene_manager.update_actor(aunt, position = "walking_away")
    "[aunt.possessive_title!c] disappears into the back of the store, looking for [starbuck.title]."
    return

label starbuck_rebecca_trans_scene_2(the_group):
    starbuck "I've just gotten in a great new product that I can't wait to showoff for the store, if you are up for it!"
    mc.name "Oh yeah? I'm always interested in helping you with new product demos."
    aunt "Yeah, if there is something new that you're are excited about, I'm interested to see it too."
    starbuck "Ah, well, I got in a new brand of lip stick!"
    aunt "Oh?"
    starbuck "And get this, it is made specifically so it only comes off with these special lipstick removal wipes..."
    starbuck "It was originally made for working girls for going down on johns without their lipstick coming off!"
    aunt "Oh! That would be handy to not have to mess with lipstick after a blowjob!"
    starbuck "They come in lots of colors too! I have several colors that match lingerie sets..."
    mc.name "Sounds hot, we're you thinking about doing some kind of... demonstration?"
    aunt "Oh! Good idea! A demo to show a before and after shot, showing how it still looks great after a strenuous round of slurping and sucking..."
    starbuck "Yeah, I DO have good advertising following of both men and women."
    "[starbuck.possessive_title!c] looks at you excitedly."
    starbuck "Would you be okay with that? If we used you for the demo?"
    mc.name "Umm, yes? Damn I'm getting hard just thinking about you two and your lips on my cock."
    "[starbuck.title] looks over at [aunt.fname], then stops for a moment."
    call starbuck_rebecca_strip_oral_label(the_group) from _starbuck_rebecca_teamup_oral_warning_02


    return

label starbuck_rebecca_trans_scene_3(the_group):
    pass
    return

label starbuck_rebecca_trans_scene_4(the_group):
    pass
    return

label starbuck_rebecca_teamup_scene_0(the_group, scene_transition = False):
    #Scene starts, Rebecca is in the back working on finances, you just told Starbuck you want to do a lingerie ad with just her.
    $ scene_color = get_random_from_list(list_of_lingerie_colors)   #In the future let MC pick or take opinions into accounts
    starbuck "Another lingerie ad? That is a good idea!"
    starbuck "I've got something in mind, I've been wanting to run an ad with lingerie in [scene_color]!"
    $ scene_manager.update_actor(starbuck, position = "walking_away")
    "[starbuck.possessive_title!c] turns to head to the back room."
    $ scene_manager.hide_actor(starbuck)
    "While you are alone with her, you chat with [aunt.title]."
    mc.name "How's it looking this week?"
    aunt "It looks good. She is turning a good profit now, but there are a couple tasks that need to be done still."
    if 1 in starbuck_rebecca_teamup.scene_unlock_list:  #She's already agreed to pose in lingerie, and is a little offended she wasn't asked to
        "[aunt.possessive_title!c] gives a loud sigh, before looking over at you."
        aunt "I was kind of surprised you just wanted [starbuck.fname] to model for you this week."
        $ aunt.change_happiness(-2)
        "She is clearly upset you didn't ask her to be a part of the lingerie ad."
        menu:
            "I wasn't sure you wanted that\n{menu_red}Increases love{/menu_red}":
                mc.name "I'm sorry [aunt.title], I guess I didn't realise you wanted to do it again."
                mc.name "I didn't want to assume anything from such a close family member."
                $ aunt.change_love(2)
                aunt "Ah, well maybe next time just ask!"
            "I like to keep you for myself\n{menu_red}Increases Sluttiness{/menu_red}":
                mc.name "I love the way you look, [aunt.title], and I guess I enjoy those nights we just chill at your place."
                mc.name "There is something nice about having those times between just us, not on an advertisement."
                $ aunt.change_slut(2, 60)
                aunt "Ah, yeah, I understand..."
        "She goes back to typing on the computer, but you can tell from a blush on her cheeks that she appreciates the sentiment."
    else:
        aunt "Is [starbuck.fname] doing another... you know... underwear ad with you this week?"
        mc.name "Lingerie. And yeah, I think she is in the back getting changed now."
        aunt "Ah, I see..."
        $ aunt.change_slut(1, 40)
        "She goes back to typing on the computer, but you think you noticed a slight blush on her cheeks."
    $ scene_manager.add_actor(starbuck, starbuck.personalize_outfit(Wardrobe.generate_random_appropriate_outfit(starbuck, outfit_type = "under"), opinion_color = scene_color), display_transform = character_center_flipped, position = "stand2")
    "[starbuck.possessive_title!c] emerges from the back room. Her outfit is impressive."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    mc.name "Wow [starbuck.title]! Another great outfit for another fantastic ad!"
    mc.name "What do you think, [aunt.title]?"
    $ scene_manager.update_actor(aunt, position = "default")
    "[aunt.possessive_title!c] stands up and turns to face [starbuck.title]."
    aunt "Wow. You look incredible as always, [starbuck.fname]."
    "[starbuck.title]'s face turns red but she smiles."
    starbuck "Thank you [aunt.fname]."
    "After another moment, [aunt.possessive_title] returns to the computer."
    $ scene_manager.update_actor(aunt, position = "sitting")
    mc.name "She's right. You always look amazing."
    starbuck "Alright, we've only got a little bit longer until the store opens. Let's get this done!"
    "She hands you her phone. You start the photo app."
    mc.name "Let's do the pictures right here. There is plenty of room by the counter here."
    mc.name "Strike a quick pose."
    starbuck "Hmmm, okay!"
    $ scene_manager.update_actor(starbuck, position = "stand4")
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(30)
    $ starbuck.change_arousal(5)
    "You quickly snap a few pictures."
    mc.name "Great! Now, why don't you get down on your knees for a seductive one..."
    starbuck "Hmm, okay."
    $ scene_manager.update_actor(starbuck, position = "blowjob")
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(30)
    $ starbuck.change_arousal(5)
    starbuck "How is this?"
    mc.name "Perfect... Love it!"
    "You snap several more."
    mc.name "Now, why don't you bend over the counter, show us the backside?"
    $ scene_manager.update_actor(starbuck, position = "standing_doggy")
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ starbuck.change_arousal(5)
    mc.name "Wow, yeah, that's it!"
    "You snap several pictures. You notice that [aunt.title] is watching intently now as [starbuck.possessive_title] models her sexy underwear."
    $ aunt.change_arousal(15)
    mc.name "That's it... just a few more..."
    mc.name "Got it!"
    $ scene_manager.update_actor(starbuck, position = "stand2")
    mc.name "Wow, those were great!"
    aunt "Yeah... I bet those are going to work great!"
    $ starbuck.change_happiness(3)
    starbuck "Ah, thank you both."
    starbuck "I'm going to get changed."
    aunt "Good! I am just about finished up for today."
    $ scene_manager.update_actor(starbuck, position = "walking_away")
    "[starbuck.title] turns and starts walking to the back, then disappears behind the stock room door."
    $ scene_manager.hide_actor(starbuck)
    aunt "[aunt.mc_title]... She really is something."
    mc.name "Yeah."
    "There is a long silence between the two of you."
    $ starbuck.apply_planned_outfit()
    $ scene_manager.show_actor(starbuck, starbuck.outfit, display_transform = character_center_flipped, position = "stand2")
    starbuck "Alright, how are we looking this week, [aunt.fname]?"
    $ scene_manager.update_actor(aunt, position = "default")
    aunt "You are in great shape [starbuck.fname]. I've got you all set up with expenses paid for the next week."
    aunt "Honestly, I was done before you even started taking pictures."
    starbuck "Great! Thank you so much for your help. Both of you."
    starbuck "I wouldn't be able to run this place without your help!"
    starbuck "Alright, same time next week!"
    aunt "I'll be here."
    mc.name "I can't promise I'll be here every week, but I'll come as often as I can."
    starbuck "Alright."
    $ scene_manager.clear_scene()
    "You, [starbuck.possessive_title], and [aunt.title] go your separate ways for now."
    if 1 not in starbuck_rebecca_teamup.scene_unlock_list:
        "After today, you are pretty sure you could convince [aunt.title] to join in the lingerie ad sometime."
        "You just need to make sure both her and [starbuck.title] are slutty enough."
    return

label starbuck_rebecca_teamup_scene_1(the_group, scene_transition = False):
    #Scene starts, Rebecca is in the back working on finances, you just told Starbuck you want to do a lingerie ad with just her.
    $ pose_stances = erica_make_insta_pose_pairs(the_group = the_group)
    $ scene_color = get_random_from_list(list_of_lingerie_colors)   #In the future let MC pick or take opinions into accounts
    $ starbuck_lingerie = starbuck.personalize_outfit(Wardrobe.generate_random_appropriate_outfit(starbuck, outfit_type = "under"), opinion_color = scene_color)
    $ aunt_lingerie = aunt.personalize_outfit(Wardrobe.generate_random_appropriate_outfit(starbuck, outfit_type = "under"), opinion_color = scene_color)
    if scene_transition:
        $ scene_manager.hide_actor(aunt)
        "After a few minutes, [starbuck.title] emerges from the back room."
        $ scene_manager.add_actor(starbuck, starbuck_lingerie, display_transform = character_center_flipped, position = "stand2")
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(30)
        mc.name "Wow [starbuck.title]! You sure are good at picking out sexy outfits!"
        starbuck "Thanks. Alright, come on now [aunt.fname], come on out!"
        starbuck "She's feeling a little shy."
        "You call out to her."
        mc.name "Come on, [aunt.title]. I can't wait to see your outfit."
        aunt "Ahhh, fine. Here I come!"
        $ scene_manager.show_actor(aunt, aunt_lingerie, position = "default")
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(30)
        mc.name "Wow! You two... absolutely stunning."
        starbuck "I know, right??? Ahhh, look, he's really enjoying it [aunt.fname]!"
        "You don't bother to try and hide the erection you are sporting."
        aunt "Wow, is that just from seeing us?"
        mc.name "You better believe it."
        aunt "Awww, you're sweet."
        starbuck "That's not all. [aunt.fname], show him the back!"
        aunt "Oh, good idea!"
    else:
        aunt "Ah, you want me to join the ad again? Sounds fun! Let me just finish up with this task."
        starbuck "I've got something in mind! I'll get the outfits picked out while you finish up!"
        starbuck "I've been wanting to run an ad with lingerie in [scene_color]!"
        $ scene_manager.update_actor(starbuck, position = "walking_away")
        "[starbuck.possessive_title!c] turns to head to the back room."
        $ scene_manager.hide_actor(starbuck)
        "[aunt.title] seems to be working rapidly through her accounting software. You decide to leave her to concentrate on it so she can be done quicker."
        aunt "It looks good. She is turning a good profit now, but there are a couple tasks that need to be done still."
        "After several minutes, you hear [starbuck.possessive_title] emerge from the back room."
        $ scene_manager.add_actor(starbuck, starbuck_lingerie, display_transform = character_center_flipped, position = "stand2")
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(30)
        mc.name "Wow [starbuck.title]! You sure are good at picking out sexy outfits!"
        "[aunt.title] glances over."
        aunt "Wow, that really is something. Let me just finish up this last thing..."
        $ scene_manager.update_actor(aunt, position = "default")
        "[aunt.possessive_title!c] stands up and turns to face [starbuck.title]."
        aunt "You look incredible as always, [starbuck.fname]."
        "[starbuck.title] smiles."
        starbuck "Thank you [aunt.fname]. I left your outfit out in the back!"
        aunt "Alright, I'll be right back!"
        $ scene_manager.hide_actor(aunt)
        "You wait for a few minutes. While you wait you chat with [starbuck.possessive_title]."
        "Soon, she emerges."
        $ scene_manager.show_actor(aunt, aunt_lingerie)
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(30)
        aunt "Alright, what do you think?"
        starbuck "Damn girl, looking hot!"
        mc.name "Yeah [aunt.title], you look great! This ad is going to be a huge hit."
        starbuck "Turn around, how's the back?"
        "Thank goodness for [starbuck.title], saying exactly what you were thinking."
        aunt "Oh, right."
    $ scene_manager.update_actor(aunt, position = "back_peek")
    starbuck "Woo! That ass is to die for!"
    "[starbuck.title] cat calls [aunt.possessive_title], then they both laugh."
    aunt "Alright, let's get to it."
    "[starbuck.possessive_title!c] hands you her phone with the camera app pulled up."
    mc.name "Alright, here we go. The ad is supposed to have a playful tone to it, so just play around with each other for a bit and I'll snap some pictures."
    $ pose_one = get_random_from_list(pose_stances) #TODO instead of get random, have it pop a random pose from the list, so it doesn't get repeated later. Then we could do three poses instead of just 2 for a longer event.
    $ scene_manager.update_actor(starbuck, position = pose_one[0])
    $ scene_manager.update_actor(aunt, position = pose_one[1])
    "You start to take some pictures."
    "[pose_one[2]]"
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ aunt.change_arousal(20)
    $ starbuck.change_arousal(20)
    mc.name "That is great. How about one more pose?"
    aunt "Okay!"
    $ pose_one = get_random_from_list(pose_stances)
    $ scene_manager.update_actor(starbuck, position = pose_one[0])
    $ scene_manager.update_actor(aunt, position = pose_one[1])
    "You take several more pictures."
    "[pose_one[3]]"
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ aunt.change_arousal(10)
    $ starbuck.change_arousal(10)


    mc.name "Wow. This is perfect. And you two are just smoking hot."
    $ scene_manager.update_actor(starbuck, position = "stand2")
    $ scene_manager.update_actor(aunt, position = "default")
    $ starbuck.change_slut(2, 60)
    $ aunt.change_slut(2, 60)
    "The two women smile at you as they resume normal poses."

    if scene_transition:
        aunt "God, I haven't felt this young in years!"
        starbuck "What do you mean *feel* young? We're still in our primes [aunt.fname]."
        aunt "Hah, you're funny. I'm under no illusion I'm still some spring chicken."
        mc.name "Just because you're a hen doesn't make you less desirable."
        aunt "Ahh... I suppose you are right."
        starbuck "Alright, I have to open the shop soon. I'd better get ready for it."
        starbuck "Thanks again [aunt.fname]! Did you get your paycheck sorted out?"
        aunt "Yeah, I've got my accounting fees all set up."
        starbuck "Alright. [starbuck.mc_title] can you see yourself out? We're going to go to the back and get dressed."
        mc.name "Sure. I'll catch you both later."
        $ scene_manager.clear_scene()
        "The two women disappear to the back."
        "Getting [aunt.possessive_title] and [starbuck.title] together for a lingerie shoot was just as amazing as you had hoped."
        "You can't wait to see how far you can take things with the two smoking hot ladies."

    else:
        aunt "God, spending time with you two makes me feel so young again!"
        starbuck "What do you mean *feel* young? We're still in our primes [aunt.fname]."
        aunt "Hah! That's funny. But I suppose you are as young as you feel."
        mc.name "Exactly. Any man would be lucky to have you."
        starbuck "Alright, I have to open the shop soon. I'd better get ready for it."
        starbuck "Thanks again [aunt.fname]! Did you get your paycheck sorted out?"
        aunt "Yeah, I've got my accounting fees all set up."
        starbuck "Alright. [starbuck.mc_title] can you see yourself out? We're going to go to the back and get dressed."
        mc.name "Sure. I'll catch you both later."
        $ scene_manager.clear_scene()
        "The two women disappear to the back."
        "You are really pleased with how well these sessions are going."
    $ del starbuck_lingerie
    $ del aunt_lingerie
    $ del pose_stances
    $ del scene_color
    return

label starbuck_rebecca_teamup_scene_2(the_group, scene_transition = False):
    $ pose_stances = erica_make_insta_pose_pairs(the_group = the_group)
    $ scene_color = get_random_from_list(list_of_lingerie_colors)   #In the future let MC pick or take opinions into accounts
    $ starbuck_lingerie = starbuck.personalize_outfit(Wardrobe.generate_random_appropriate_outfit(starbuck, outfit_type = "under"), opinion_color = scene_color)
    $ aunt_lingerie = aunt.personalize_outfit(Wardrobe.generate_random_appropriate_outfit(starbuck, outfit_type = "under"), opinion_color = scene_color)
    if scene_transition:
        pass
    else:
        pass

    return

label starbuck_rebecca_teamup_scene_3(the_group, scene_transition = False):
    pass
    return

label starbuck_rebecca_teamup_scene_4(the_group, scene_transition = False):

    return


label starbuck_rebecca_teamup_scene_choice_label(the_group):
    starbuck "So, are you just stopping by, or are you hanging out with us today, [starbuck.mc_title]?"
    aunt "You should! It is always nice to have you around."
    if starbuck_rebecca_teamup.progression_available:
        "There is a pleasant tension in the air. You have a feeling something good is going to happen if you decide to stay."
    else:
        if 1 in starbuck_rebecca_teamup.scene_unlock_list:
            starbuck "We may be getting old, but I'm sure we could make sure you don't regret staying!"
        if 2 in starbuck_rebecca_teamup.scene_unlock_list:
            aunt "Mmm, definitely."
            "[aunt.possessive_title!c] looks you up and down... and did she just lick her lips?"
    menu:
        "Stick around {image=progress_token_small}" if starbuck_rebecca_teamup.progression_available:
            pass
        "Stick around {image=time_advance}" if not starbuck_rebecca_teamup.progression_available:
            pass
        "Leave":
            return False

    mc.name "Yeah I'll stick around. Can I get coffee going for you two ladies in the back while you get started?"
    starbuck "Sure!"
    aunt "I'll take mine with two creams please."
    starbuck "I'll take one cream and one sugar. Thanks [starbuck.mc_title]!"
    $ scene_manager.clear_scene(reset_actor = False)
    "You step into the back of the sex shop and start up a pot of coffee."
    "As it brews, you get out a couple of paper cups. You briefly consider adding some serum..."
    if mc.inventory.has_serum:
        "You look at [starbuck.possessive_title]'s cup."
        call give_serum(starbuck) from _call_give_starbuck_serum_teamup_05
    else:
        "Unfortunately, you don't have any serums to add right now."
    if mc.inventory.has_serum:
        "You look at [aunt.possessive_title]'s cup."
        call give_serum(aunt) from _call_give_aunt_serum_teamup_06
    "When the coffee is done, you fill up the two cups, being careful to add the correct amount of cream to each, and sugar to [starbuck.title]'s."
    "You step back into the main shop."
    $ scene_manager.add_actor(starbuck, starbuck.outfit, display_transform = character_center_flipped)
    $ scene_manager.add_actor(aunt, position = "sitting")
    "You see that [aunt.title] is already sitting down at the laptop and has started her accounting work."
    "You give the two girls their caffeine boost."
    starbuck "Thanks!"
    "She takes a long sip, then turns to you."
    return True

label starbuck_rebecca_teamup_multiple_choice_scene(the_group):
    #Setting, Aunt it already working at the computer and Starbuck just took a big sip of her coffee.
    # Both girls possibly serumed at this point.
    $ the_person = the_group[0] #Starbuck
    the_person "Alright! What kind of advertisement should we make this week, [the_person.mc_title]?"
    if 1 in starbuck_rebecca_teamup.scene_unlock_list:
        "You notice [aunt.possessive_title] glance over at you, waiting to hear what you have to say."
    menu:
        "Solo Lingerie" if 0 in starbuck_rebecca_teamup.scene_unlock_list:
            return 0
        "Lingerie with [aunt.title]" if 1 in starbuck_rebecca_teamup.scene_unlock_list:
            return 1
        "Sexy Makeup with [aunt.title]" if 2 in starbuck_rebecca_teamup.scene_unlock_list:
            return 2
        "Easy Access Clothing with [aunt.title]" if 3 in starbuck_rebecca_teamup.scene_unlock_list:
            return 3
        "Anal Toys with [aunt.title]" if 4 in starbuck_rebecca_teamup.scene_unlock_list:
            return 4
        # "Cum Fetish Scene" if 5 in starbuck_rebecca_teamup.scene_unlock_list:
        #     return 5
        # "Breed Her" if 6 in starbuck_rebecca_teamup.scene_unlock_list:
        #     return 6
        # "Anal Fetish Scene" if 7 in starbuck_rebecca_teamup.scene_unlock_list:
        #     return 7
        # "Surprise me" if len(starbuck_rebecca_teamup.scene_unlock_list) > 1:
        #     the_person "Hmmm, okay."
        #     $ the_person.change_stats(happiness = 5, obedience = 3)
        #     return renpy.random.choice(starbuck_rebecca_teamup.scene_unlock_list)
    return

label starbuck_rebecca_teamup_exit_scene(the_group):
    "You decide not to stay."
    $ scene_manager.clear_scene()
    return


#Incest related labels
#Use these labels for Starbuck's reaction to MC sexual actions with aunt. Pulled out into labels to make it easier to modify.
label starbuck_rebecca_strip_incest_label(the_group):
    starbuck "Actually... I forgot for a moment that she is your aunt."
    starbuck "Maybe umm... maybe it isn't such a good idea for you to see her like that."
    mc.name "I'm not sure what you mean. Like what?"
    starbuck "What? You know what I mean, in a skimpy outfit."
    mc.name "[starbuck.title], why would that be a problem?"
    starbuck "Well, you're related, right? Doesn't that make it... bad?"
    "You make sure to dismiss her concerns forcefully."
    mc.name "Of course not. She is here to help, and while her primary skill set is her accounting know-how, if she wants to help with the ad, why not?"
    mc.name "It isn't like I'm going to suddenly be smitten and fall in love and marry her or something."
    mc.name "And just because she is family, doesn't mean I can't acknowledge that she has a great body."
    aunt "You know I'm hearing all of this, right?"
    mc.name "And do you disagree?"
    aunt "Well, you should probably get your eyes checked. I'm just an old..."
    starbuck "Oh you shush. Everyone here agrees that your body is perfect for the ad."
    return

label starbuck_rebecca_strip_oral_label(the_group):
    starbuck "Sorry, I just realized what I was saying. For someone reason I keep forgetting that you two are related."
    mc.name "Yeah, but what does that have to do with it?"
    starbuck "Errmm, we were just talking about giving you a blowjob..."
    mc.name "Yeah? [starbuck.title], what is wrong with that?"
    starbuck "I... I guess I just assumed that you two wouldn't be okay with it..."
    "You make sure to dismiss her concerns forcefully."
    mc.name "Hey, she and I are capable of making our own decisions about what is appropriate between two consenting adults."
    mc.name "Besides, it isn't like we're fucking or I'm gonna knock her up. We're just shooting an ad for your business that happens to have some oral fun..."
    mc.name "Do you have a problem with it?"
    aunt "[starbuck.fname], you've become a good friend of mine. I'm more than happy to suck [aunt.mc_title]'s cock if it would help your business."
    aunt "Besides... it'll be fun too!"
    starbuck "Okay!"
    return

label starbuck_rebecca_strip_vaginal_label(the_group):
    "Use this label for describing MC and Aunts relationship in the intro to sex"
    return

label starbuck_rebecca_strip_anal_label(the_group):
    "Use this label for describing MC and Aunts relationship in the intro to anal"
    return
