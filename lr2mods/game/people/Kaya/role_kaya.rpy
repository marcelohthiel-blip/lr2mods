#Kaya reboot for Nov 2023 content patch
#Kaya starts working at the coffee shop on weekends, now independent of Alexia's schedule
#Native american heritage, she is just finishing up her undergrad online and is trying to get into the university for a pre-med masters program
#Her mother runs the clothing store, but lately the store has fallen on hard times. Starts working at the coffee shop for a little extra money
#When MC meets her, she is just starting her finals for her undergrad program, so she has a soft start timer
#After a couple weeks MC can slowly star to unlock more of her time. Starts with coffee shop, then the university, then a residency program at MC's business
#MC pairs up Kaya with Nora at the university to get her into the program. AFter she starts there, she can be recruited to work at MC's business as a work credit program
#Kaya starts the game living with her mother instead of moving in partway through the story

style kaya_lang:
    outlines [ (absolute(4), "#080", absolute(0), absolute(0)) ]

label kaya_intro_label(the_person):
    "It is a beautiful weekend, so you decide to swing by the coffee-shop for a pick me up."
    $ mc.change_location(coffee_shop)
    $ the_person.draw_person()
    $ the_person.side_job.job_known = True
    "When you step inside, there's a new girl working there you haven't seen before."
    "You listen as the person ahead of you orders."
    "???" "Yes I'd like a tall macchiato with whipped cream."
    the_person "Is that all?"
    "When she talks, there is a slight accent. It's subtle, and you have trouble placing it."
    "You quickly glance behind you. No one's in line yet... maybe you can chat with her for a bit?"
    "The person in front of you moves to wait for their drink."
    the_person "Hi, what can I get you?"
    "That accent... where is it from? It's starting to bother you..."
    the_person "{=kaya_lang}Kia ora? {/=kaya_lang}(?????)... Do you want to order?"
    "Ah! You zoned out for a second. What was that word?"
    mc.name "Yes, sorry. I was trying to place your accent, but I can't. I'll just take a large coffee, leave room for cream."
    the_person "Okay. Is that all?"
    mc.name "Yeah..."
    "You pay for your coffee, but stand still."
    mc.name "You know, I've been coming here for a while but haven't seen you before. You just get hired?"
    the_person "Yeah. I'm trying to make some extra money, and they hired me to work weekends here."
    $ kaya_begin_class_schedule()
    mc.name "I see. Why not work during the week?"
    the_person "Well, I'm taking some classes, and working during the week just wouldn't work for me."
    mc.name "At the local university?"
    the_person "No, I take my classes online, but I am hoping to... rmmm... I guess you could say transfer? To the local university."
    mc.name "Ah, good for you. Well, best of luck with your studies. If you are as smart as you are beautiful, I'm sure you will do well."
    the_person "Ah, thank you..."
    mc.name "I'm [mc.name]."
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("your favourite barista")
    $ the_person.set_mc_title(mc.name)
    $ the_person.set_event_day("day_met")
    the_person "[the_person.fname]."
    mc.name "It's a pleasure to meet you."
    "Right then another employee puts your coffee on the counter and calls your name."
    the_person "Right... sorry, there's someone behind you..."
    "You hear a throat clear behind you. You grab your coffee and move out of the way."
    "Well, the new barista is cute! Maybe you should try to get to know her more..."
    $ add_kaya_ask_out_action()
    return

label kaya_ask_out_label(the_person): #Requires 20 love, substitute for first date.
    if kaya.progress.love_step == 0:
        call kaya_ask_out_reject_label(the_person) from _kaya_first_date_turn_down_01
        return
    if kaya.progress.love_step == 1:
        the_person "I'm sorry... I told you I have finals this week. I really do want to go though!"
        the_person "Come back next week!"
        return
    if not kaya_can_get_drinks():
        $ kaya.event_triggers_dict["can_get_drinks"] = True
        "You step into the coffee shop. You wonder if [the_person.title] is working. It is almost closing time."
        $ the_person.draw_person()
        "Sure enough, as you step inside, there she is. You've been getting to know her more lately, and you feel ready to ask her out."
        "When you step up to the counter, she smiles at you."
        $ the_person.draw_person( emotion = "happy")
        the_person "Good evening [the_person.mc_title]. What can I get you?"
        mc.name "I'll take a small coffee with room for cream... and I was hoping to ask you something."
        the_person "Okay, I can do that... and what is the question?"
    mc.name "I was ahhh, wondering if you were doing anything after you got off work today?"
    the_person "No, I don't have any plans. You umm... have any particular reason for asking?"
    mc.name "I know a good bar around the corner... I thought maybe we could get a drink?"
    the_person "Oh! I... you seem pretty nice... yeah I guess I could do that!"
    mc.name "Great! Tell you what, I'll take my coffee out to the patio... whenever you get off, I'll walk you over there?"
    the_person "Okay... don't worry I get off soon!"
    $ clear_scene()
    $ mc.change_location(downtown)
    "You step outside and sit down, sipping your coffee."
    "You spend some time on your phone, and follow up on a couple of work emails while you wait. It's a pretty pleasant evening."
    "Pretty soon you hear [the_person.possessive_title] clear her throat nearby. You look up from your phone."
    # change out of uniform
    $ the_person.apply_outfit(the_person.decide_on_outfit())
    $ the_person.draw_person()
    mc.name "Ah, you're right, that was quick!"
    the_person "Yes... hey... I need to be honest about something..."
    mc.name "Oh? Did you change your mind? It's quite alright..."
    the_person "No, I'd still like to go and hang out, but I won't be able to have any drinks."
    mc.name "Ah, you don't drink?"
    the_person "No, it's not that, I'm just... with school and some other stuff going on... money is just really tight right now..."
    mc.name "Oh! Why don't you let me pick up the tab tonight?"
    the_person "I couldn't let you..."
    mc.name "Just pretend like I left a 20 in your tip jar, and you wanted to treat yourself."
    the_person "I suppose... just a couple, okay?"
    mc.name "Great! Let's go."
    "You stand up, making sure to throw your coffee cup away and leave the table clean. You start to walk with [the_person.title] a couple blocks to the bar."
    the_person "So... sorry if I'm like... misreading this... but... is this like... a date?"
    "She seems to be in tune with your intentions."
    mc.name "Well [the_person.title], I'm certainly interested in getting to know you better! And I have to say I like what little I know about you so far..."
    mc.name "I can hardly think of a better way to learn more about you than a date!"
    $ the_person.change_love(2, 40)
    the_person "Ahhh... I'm glad to know I wasn't mistaken."
    $ mc.change_location(downtown_bar)
    "Soon, you arrive at the bar. You point her to a high top you spot that looks open."
    mc.name "Hey, if you want to go grab that table, what is your drink of choice?"
    the_person "Oh, umm, let me walk up with you instead, I want to see if they have any specials."
    mc.name "Okay. With company as pretty as you we'll probably get served faster anyway!"
    $ the_person.change_happiness(3)
    "She smiles and accepts your compliment. You walk up to the bar with her. Soon the bartender comes over."
    "???" "Hey there. Never seen you around here before, what can I get you?"
    the_person "Hi! Are you running any specials tonight?"
    "???" "Well, we got domestic beers for $2, some imports for $3, and rail drinks for $4."
    the_person "Ah, can I get a rum and coke please?"
    "You wonder if she's just trying to be considerate? You would hardly expect a girl like her to order that as a first choice..."
    "You must have given her a funny look."
    the_person "What? You seem like a nice guy, I just want to be a cheap date!"
    "Ah, so she must be very budget conscious. You suppose there are certainly worse personality traits to have!"
    "You order yourself an Old Fashioned, something to sip on while you chat."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    "Once you have your drinks, you glance around. The table you had your eye on is taken... looks like everything is full..."
    the_person "Ah! Look! An open pool table! Let's play!"
    $ the_person.discover_opinion("billiards")
    "[the_person.possessive_title!c] gets really excited. She must really enjoy billiards?"
    "She takes a sip of her drink, then sets it down on the side of the pool table. You do the same."
    mc.name "So tell me, cheap date, what happens to be your actual favourite cocktail?"
    the_person "Why so interested? Trying to get me drunk?"
    mc.name "Honestly, I feel like a person's favourite drink says a lot about them."
    the_person "Is that so?"
    mc.name "Absolutely. I know I'm dealing with immature college girls when the answer I get is some ridiculous drink like 'sex on the beach'."
    the_person "Ha! Yeah I suppose."
    "[the_person.title] pulls some quarters out of her purse and puts them in the table. She pays the cost of a game and you hear the billiard balls fall into the gully."
    mc.name "But you... you seem much too practical for something like that. You seem like the type that would enjoy finer spirits."
    "[the_person.possessive_title!c] is pulling the balls from the gully and setting them on the table. She looks at you and smirks."
    the_person "Ah, is that so?"
    mc.name "Indeed. And the fact that you don't deny it tells me I'm right."
    the_person "You sure seem pretty confident in yourself there, mister! Tell you what. Let's play a round, and if you win, I'll tell you my favourite drink. Okay?"
    mc.name "Ah, who's confident now? Placing a wager on a billiards game!"
    "She chuckles and rolls her eyes mockingly."
    the_person "Disclosing my favourite drink hardly seems like a major wager. Maybe I intend to lose, so you can learn my secret? You're the one buying the drinks, remember?"
    the_person "Tell you what, if I win, I'll even allow you a guess, and I'll tell you if you're right or not."
    mc.name "That seems more than fair. If I can't get it right, I think I can get close."
    "She picks up her drink and takes a long sip. Then grabs her pole."
    the_person "Here, rack these up, will you?"
    "In here goes a brief billiards game Starbuck hasn't made yet. It uses MC's intelligence to determine if he wins or loses. Today you win!"
    $ _return = True
    # call play_billiards(the_person) from _kaya_first_billiards_01
    if _return: #You won
        the_person "Wow, I'm impressed! Do you play much?"
        mc.name "Not particularly. But It's a game of angles, and math has always been a strong subject for me."
        the_person "I see."
        mc.name "Now, about our wager?"
        the_person "Okay, okay. If you really want to know..."
        the_person "My favourite cocktail is a Manhattan with an orange twist."
    else:
        mc.name "Wow, you are very good at pool! That was very impressive."
        the_person "Thank you. I love to play. It is a good exercise for your dexterity and your brain."
        mc.name "I agree. Now, about the wager..."
        the_person "Yes, this should be interesting. Go ahead, think about it and guess my favourite drink."
        "It is clear to you so far that [the_person.possessive_title] is intelligent and practical. However, even though she is strapped for money right now, you get the feeling things haven't always been this way for her."
        "Rum is too simple a spirit for her to favour. She probably favours gin or whiskey."
        "Something about her dark skin has you guessing it might be a darker spirit too, so you decide to guess a classic whiskey cocktail."
        menu:
            "Whiskey sour":
                pass
            "Highball":
                pass
            "John Collins":
                pass
        the_person "Wow. I admit, I was thinking that you were pretty full of shit, but that's actually really close! Close enough for me anyway!"
        mc.name "Oh?"
        the_person "My favourite cocktail is definitely a Manhattan with an orange twist."
    mc.name "Ah, a bold drink indeed. I was definitely thinking something whiskey inspired, but I would not have guessed that."
    the_person "Yeah. Sometimes I'll have one, but to make a good one it requires good whiskey. The ones you get with more affordable varieties just aren't as good."
    mc.name "Yes, a quality of many whiskey-heavy drinks, I think. Well, we seem to be ready for another round?"
    the_person "I umm... I'm kind of out of quarters..."
    mc.name "Here, let me go get us a couple more drinks and some quarters. I'm not quite ready to say goodbye for the evening yet."
    $ the_person.change_love(2)
    the_person "I suppose I could stay out for a bit longer."
    # $ mc.business.add_mandatory_crisis(kaya_get_drinks)
    $ kaya.event_triggers_dict["bar_date"] = True
    $ clear_scene()
    "You walk back up to the bartender. You order yourself another Old Fashioned and a top shelf Manhattan with an orange twist for [the_person.title]."
    $ mc.business.change_funds(-40, stat = "Food and Drinks")
    "When he brings you the drinks, you ask for change for a dollar to play another round of pool. When he goes to make change for you, you look down at the drinks..."
    if mc.inventory.has_serum:
        "You could probably slip a serum into her drink if you do it quickly..."
        call give_serum(the_person) from _call_give_kaya_serum_bar_01
    "You walk back to the pool table. She smirks when she sees your drink for her."
    $ the_person.draw_person()
    the_person "Ah, so you ARE trying to get me drunk then? Ahhh, {=kaya_lang}koretake {/=kaya_lang}(?????)."
    mc.name "As... what now?"
    the_person "Ah... sorry... as you might have guessed, English isn't my first language."
    "She takes a sip from her drink."
    the_person "[sakari.fname!c] thought it was important for me to learn my native tongue first, even though no one really speaks it anymore."
    the_person "Sometimes I still find myself using words from it by accident."
    mc.name "Ah, I see. So what language is your first language?"
    the_person "Well, my family and I are natives... from before white colonization here."
    mc.name "That's very interesting! I'm not sure I've ever met a native."
    the_person "Well, to be honest, there aren't many of us left, and even fewer off of reservations."
    "You take a moment to think about it. You take the coins from the bartender and walk around the pool table, starting up another game."
    the_person "We playing for anything this time? It's kinda fun when there are stakes..."
    mc.name "Sounds good to me. I set the stakes last match, how about you set them for this one?"
    the_person "Hmmm... okay. How about, if I win, you have to walk me home?"
    mc.name "You know I was planning to offer to do that anyway, right?"
    the_person "Probably, but now you'll {i}have{/i} to!"
    mc.name "Ah. Well, in that case, if I win, you have to let me take you out for drinks again another time."
    the_person "Free drinks? Deal. I might have to lose on purpose!"
    "Another billiards game Starbuck hasn't made yet! What luck you get to skip it!"
    $ _return = True
    #call play_billiards(the_person) from _kaya_first_billiards_02
    if _return: #You won
        the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
        mc.name "The horror!"
        the_person "Guess I'll just have to walk myself home now, dreading the day the mysterious stranger shows up at the coffee-shop and demands my presence again!"

    else:
        the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
        mc.name "Too bad you didn't make that your wager then."
        "At first she looks at you, a bit startled, thinking you mean you don't want to, but then realises you are teasing her."
        the_person "Guess you'll just have to walk me home and we'll go our separate ways then."
    "The teasing between you two has definitely become playful. You are really enjoying her company."
    the_person "But uh... we're doing both... right?"
    mc.name "Of course."
    "You both finish off what is left of your drinks, then leave the bar together."
    $ mc.change_location(downtown)
    "You step out on to the sidewalk and start to walk [the_person.possessive_title] home. Sensing a connection with her, you hold out your hand and she takes it."
    mc.name "So, you're taking online college classes, right?"
    the_person "That's right."
    mc.name "What are you studying?"
    the_person "I'm majoring in biology, but I'm hoping once I graduate to get into med school..."
    mc.name "Wow. So you want to be a doctor?"
    the_person "Yeah... something like that..."
    "She is quiet for a little bit, before she resumes."
    the_person "I know this might sound silly, but my mother is really the last family I have left. She's always had some recurring health issues, but lately they've been getting worse I think."
    the_person "It sucks... I know I'll never finish school in time to do anything for her... but I think I want to get into research. You know? Learn how to help other people. People like her."
    mc.name "She must be a great woman for you to look up to her like that."
    the_person "Yeah. She really is. She inspires me every day."
    mc.name "I can understand that. Did I tell you I run a pharmaceutical company? We do our own research and development, although not for any major medical illnesses."
    the_person "Really? That's pretty interesting. You're a very interesting man [the_person.mc_title]."
    "You walk in silence a bit longer with [the_person.title]."
    $ the_person.learn_home()
    "Soon you walk up to the steps of a run-down apartment building. This must be where she is living."
    the_person "Hey, I just want to say, it's been a long time since I had a night like this to just relax and have fun. I had a great time... please come back and see me at the coffee shop, okay?"
    mc.name "Your charm is difficult to resist. And the coffee is good too."
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] holds her arms out for a hug, and you draw her close. She is looking up at you, and feeling right, you kiss her."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
    "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when your hand wanders down to her ass, but reaches back and moves your hand back up."
    $ the_person.change_arousal(15)
    $ the_person.break_taboo("kissing")
    "You keep making out for several more seconds until [the_person.title] breaks it off and then steps back."
    $ the_person.draw_person()
    the_person "God you are hot..."
    mc.name "Can I umm... come up?"
    the_person "Oh... I'm sorry... this was just a first date! I couldn't possibly after just once..."
    mc.name "That's okay. I'm sorry I didn't mean to make you uncomfortable."
    the_person "It didn't at all. We umm... we just need to get to know each other better. Okay?"
    mc.name "Sounds great. I'll see you around?"
    the_person "Bye!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and starts to walk up the stairs of her apartment building."
    $ clear_scene()
    "Wow, what a busy night! You feel like you have a connection with [the_person.title]. She definitely seems eager too..."
    $ add_kaya_meet_erica_at_uni_action()
    call advance_time() from _call_advance_time_kaya_ask_out
    return

# This is the label that is activated from Kaya's role. Used as an intro at first, then becomes repeatable.
# This label has been disabled, pending movement of unique stuff from here to named labels.
label kaya_get_drinks_label(the_person):  #Repeatable date night with Kaya
    if the_person.progress.love_step < 2:
        call kaya_ask_out_label(the_person) from _call_kaya_ask_out_label
        return
    if the_person.event_triggers_dict.get("drink_date_count", 0) < 1:
        $ the_person.event_triggers_dict["drink_date_count"] = 1
    else:
        $ the_person.event_triggers_dict["drink_date_count"] = +1

    mc.name "How about a couple drinks tonight?"
    the_person "Sounds great! It's almost closing time, and I'm solo tonight. If you want to just grab a seat while I close up, we can walk over together."

    # "This will eventually be a full date that you can go on with [the_person.title], but it hasn't been written yet."
    # "You will have the chance to give her a serum though, so for now this is just a placeholder option to give her a serum."
    # Because pregnancy is core to Kaya's story, make sure we have pregnant dialogue for drinks, etc.

    $ clear_scene()
    $ mc.change_location(downtown)
    "You step outside and sit down, sipping your coffee."
    "You spend some time on your phone, and follow up on a couple of work emails while you wait. It's a pretty pleasant evening."
    "Pretty soon you hear [the_person.possessive_title] clear her throat nearby. You look up from your phone."
    # change out of uniform
    $ the_person.apply_outfit(the_person.decide_on_outfit())
    $ the_person.draw_person()
    mc.name "Ah, you're right, that was quick!"
    "You stand up, making sure to throw your coffee cup away and leave the table clean. You start to walk with [the_person.title] a couple blocks to the bar."
    $ mc.change_location(downtown_bar)
    "Soon, you arrive at the bar. You point her towards an empty pool table."
    mc.name "Hey, if you want to go grab that table, I'll get us some drinks."
    "You order yourself an Old Fashioned and a Manhattan with an orange twist for [the_person.title]."
    "The bartender finishes them up quickly and you hand over some cash."
    "He thanks you and turn to walk down the bar to another customer. You are fairly alone at this corner of the bar, behind a support post."
    if mc.inventory.has_serum:
        "You could probably slip a serum into her drink if you do it quickly..."
        call give_serum(the_person) from _call_give_kaya_serum_bar_02
    "By the time you get back [the_person.title] has the balls ready for you and trades you a stick for her drink."
    the_person "We playing for anything this time? It's kinda fun when there are stakes..."
    mc.name "Sounds good to me. Same stakes as last time?"
    the_person "What do you mean? Last time you won then you walked me home anyway and here we are having drinks again."
    mc.name "Seemed like a perfect outcome to me."
    $ the_person.change_stats(love = 2, happiness = 2)
    the_person "Yeah, I guess it's not too bad."
    "Another billiards game Starbuck hasn't made yet! What luck you get to skip it!"
    $ _return = True
    #call play_billiards(the_person) from _kaya_first_billiards_02
    if _return: #You won
        the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
        mc.name "The horror!"
    else:
        the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
        mc.name "I suppose that could be arranged."
    the_person "But uh... we're doing both... right?"
    mc.name "Of course."
    "You both finish off what is left of your drinks, then leave the bar together."
    $ mc.change_location(downtown)
    "You step out on to the sidewalk and start to walk [the_person.possessive_title] home. She reaches out for your hand before you have time to offer it."
    # put something here
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] leans close and goes up on her toes, obviously hoping for something, and feeling right, you kiss her."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
    "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when your hand wanders down to her ass, but reaches back and moves your hand back up."
    $ the_person.change_arousal(15)
    $ the_person.change_slut(2, 30)
    "You keep making out for several more seconds until [the_person.title] breaks it off and then steps back."
    $ the_person.draw_person()
    the_person "God you are hot..."
    mc.name "Can I umm... come up?"
    the_person "Oh... I'm sorry... not yet..."
    mc.name "That's okay. I'm sorry I didn't mean to make you uncomfortable."
    the_person "It didn't at all. We umm... we just need to get to know each other better. Okay?"
    mc.name "Sounds great. I'll see you around?"
    the_person "Bye!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and starts to walk up the stairs of her apartment building."
    $ clear_scene()
    "Wow, what a busy night! You feel like you have a connection with [the_person.title]."
    "Something is holding her back, you should probably see if you can make her more promiscuous before your next date."
    if kaya_studies_with_erica():
        "Maybe her Tuesday night study sessions with [erica.fname] could help you make progress."
    call advance_time() from _call_advance_time_kaya_drink
    return

label kaya_meet_erica_at_uni_label(the_person):     #This label is a replacement for kaya and lily event.
    #This label needs to be basically redone. Kaya's intro stuff has drastically changed, and she is too smart for most of this.
    #Maybe make her some kind of mentor for Erica? And when doing the teamup, make sure Kaya's questions are harder than Erica's.
    #For now though, the teamup has good smut, so it stays in until it can be properly retconned.
    $ scene_manager = Scene()
    "You go for a stroll at the university. With no particular aim, you just walk around, checking out some of the girls, stretching your legs a bit."
    the_person "[the_person.mc_title]? Is that you?"
    $ scene_manager.add_actor(the_person)
    $ the_person.primary_job.job_known = True
    "You turn and see [the_person.possessive_title]. She goes to class here, but it is a big school, so you are surprised to see her."
    mc.name "Ah, hello there [the_person.title]."
    "She gives you a smile and chirps at you."
    if the_person.event_triggers_dict.get("drink_date_count", 0) > 1:
        the_person "We go out for drinks once in a while and now you are stalking me at class, mister?"
    else:
        the_person "We go out one night for drinks and you are stalking me at class, mister?"
    "[the_person.title] is very quick-witted. You can tell she is half-joking... but also seriously wanting to know what you are doing here."
    mc.name "Ah, sorry I wasn't looking for you, to be honest... I was... er..."
    "Just then, you are saved by another familiar voice."
    erica "Oh hey, [erica.mc_title]!"
    $ scene_manager.add_actor(erica, display_transform = character_center_flipped)
    "[erica.possessive_title!c] walks up."
    erica "You didn't tell me you were gonna be here! I'm just headed to the gym, want to go work out?"
    $ scene_manager.update_actor(the_person, emotion = "angry")
    the_person "Ahhh... I see... you aren't here to see me..."
    "[erica.title] suddenly realises you were talking with [the_person.possessive_title]. The edge of jealously is clear in [the_person.title]'s voice."
    erica "Oh! Sorry, I didn't realise you were talking to her..."
    mc.name "Ah, let me introduce you. [the_person.fname], this is [erica.fname]. She is taking classes here also, and we work out together once in a while."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    "You can tell [the_person.title] is still sceptical."
    the_person "Ah... so you are... workout buddies?"
    mc.name "Yeah, something like that."
    erica "Nice to meet you! You look kind of familiar... have I seen you somewhere before?"
    the_person "Maybe, I work over at the coffee shop..."
    erica "Ah, probably not there, coffee makes me anxious."
    "The girls start to chat, trying to figure out if they know each other from somewhere."
    "Suddenly, they make a breakthrough."
    erica "Ah! Yes I have that class too! It is so hard!"
    the_person "Yeah it is definitely challenging."
    erica "Hey... do you want to get together to study sometime? They have study rooms here at the university."
    the_person "That would be really helpful."
    "As you watch the two girls interact, you can't help but start to get turned on."
    "Two hot college coeds. You've already started messing around with [erica.possessive_title], the other is right on the brink."
    "You can't help but imagine the two girls making out... getting on their knees in front of you, one of them taking the tip of your cock in her mouth while the other licks the shaft..."
    $ mc.change_locked_clarity(20)
    the_person "[the_person.mc_title]?"
    erica "Earth to [mc.name]?"
    mc.name "I'm sorry... I spaced out for a second."
    the_person "[erica.fname] just asked if you ever took molecular biology when you were here..."
    mc.name "Oh! Yes, actually that is one of my specialties. I use it every day at my pharmaceutical company."
    erica "Ah! You should join us sometime. I bet you could help us out if we get stuck."
    the_person "If it isn't too much of a bother."
    mc.name "No, I'll try to swing by sometime."
    "[the_person.possessive_title!c] and [erica.title] trade phone numbers. Sounds like you have a study party to crash on Tuesday!"
    $ town_relationships.update_relationship(erica, kaya, "Friend")
    $ kaya.add_unique_on_room_enter_event(kaya_erica_teamup_action)
    $ kaya.event_triggers_dict["has_started_internship"] = False
    $ kaya.set_override_schedule(university, day_slots = [1], time_slots = [3])
    $ erica.set_override_schedule(university, day_slots = [1], time_slots = [3])
    return

label kaya_condom_talk_label():
    $ the_person = kaya
    $ story_path = None
    $ kaya.change_baby_desire(40)    #She's okay with it.
    if the_person.sluttiness >= 50:
        $ story_path = "lust"
    elif the_person.love >= 50 and the_person.progress.love_step >= 5:
        $ story_path = "love"
    else:
        $ story_path = "lust"
    "You get a text message on your phone. It is from [the_person.possessive_title]."
    $ mc.start_text_convo(kaya)
    the_person "Hey, I really need to talk to you about something."
    the_person "Can you swing by the coffee shop? I'll be brief, I promise!"
    mc.name "For you? Sure. I'll be right there."
    $ mc.end_text_convo()
    "It sure sounds urgent, so you head over to the coffee shop right away to see her."
    $ mc.change_location(coffee_shop)
    #Use story_path to determine which path brought us to this conversation.
    #If left as none, assume it happened because we tried to have sex with her and she accepted somehow.
    $ the_person.draw_person()
    "When you walk in, she sees you. She looks over at a co-worker."
    the_person "Hey, I really need to a quick break, okay?"
    "Co-worker" "Sure thing."
    "As she comes out from around the counter, you sit down at a booth, away from other people."
    if persistent.pregnancy_pref != 0:
        $ the_person.on_birth_control = False
        the_person "So, there is something that I really... REALLY need to talk to you about."
        $ the_person.draw_person(position = "sitting")
        "She sits down across from you. She is looking away."
        mc.name "You seem nervous. Whatever it is, it's okay. Take a deep breath, and let it out."
        the_person "Ahhh... yes..."
        "She takes a breath, and then starts talking."
        the_person "I'm sorry I meant to have this conversation before this happened but... you're just so fucking hot and I was scared how this might go."
        the_person "I have this weird thing that I need to tell you about, and I'm just really worried how you are going to react."
        the_person "So please, just listen from start to finish, and whatever happens or however you feel, I'll understand."
        mc.name "Yes... what is it?"
        the_person "Okay... here goes."
        the_person "So obviously, you've noticed I am from one of the native tribes here, and, well, I'm really proud of where I'm from and my heritage."
        the_person "It has been really great. My mom and I get support from tribe leaders, and it has a lot of great things about it."
        the_person "But... some of the things involve centuries old beliefs and customs..."
        the_person "And well... in my culture... we... we don't believe in using birth control."
        mc.name "Like... the pill?"
        the_person "Like... anything. Babies are sacred, no pills, no condoms..."
        mc.name "So... what... but..."
        the_person "I know! In modern society it hasn't been easy to stick with it."
        the_person "I've had a couple boyfriends before, and we would fool around and stuff, but then this exact same conversation happened."
        the_person "One guy dumped me on the spot, another guy acted like it was okay, but I could tell he basically lost interest or got scared."
        the_person "I umm... I've never actually had the opportunity to like... go all the way with someone."
        mc.name "You're a virgin?"
        the_person "Yes. And I'm okay with that. I just hadn't met the right guy yet."
        mc.name "Okay. I think I understand. And you are telling me because..."
        if story_path == "love":
            the_person "Look... I've REALLY enjoyed the time we've been spending together."
            the_person "And I know things have been crazy with school and things at your business, and the coffee shop... and my mom..."
            the_person "I don't even know if we'll ever even have the chance but... I mean..."
            the_person "I want you to be fully prepared. If you want me, that's how it has to be, okay?"
            mc.name "I think I understand."
            the_person "And to be honest, I think I'm ready for it too. It, AND the consequences."

        elif story_path == "lust":
            the_person "Look... everytime you are around, my body feels like it is on fire."
            the_person "I'm 21... my hormones are going crazy!"
            the_person "What we've done so far has been amazing... but I want more."
            mc.name "Damn. Well when you put it like that..."
        mc.name "You want me to knock you up?"
        the_person "No, I mean... I'm not out here TRYING to or anything but... if it happened..."
        "She shrugs."
        mc.name "But like, with everything going on, adding a pregnancy and a baby on top of it?"
        the_person "Ah, well, I guess I didn't tell you."
        the_person "My tribe... they are actually getting smaller every year."
        the_person "A while back, some of the leaders got together and decided to offer to support women in the tribe who had babies, financially."
        the_person "And I know my mom would be willing to help. We talked about it already..."
        mc.name "Wow, that is definitely a lot to think about. Thank you for telling me."
        the_person "I mean, it isn't a sure thing either."
        the_person "It's okay too, if you want to just pull out. In my culture, if a man has a will strong enough to pull out, he is allowed to..."
        mc.name "... ... ... You know that makes no sense whatsoever."
        the_person "Yeah, I know."
        mc.name "This is certainly a lot to think about."
        mc.name "So umm... what are you doing tonight after work?"
        the_person "I'm going home! This was a major thing, and I don't want you to make a decision about how you want things to go right here, right now."
        the_person "Sleep on it, for a night or two... okay?"
        mc.name "I mean, sure, but I'm pretty sure I already know how I feel about it."
        menu:
            "Be supportive\n{menu_red}Increases love{/menu_red}":
                mc.name "That is pretty awesome that you are able to get help with finances from your tribe."
                mc.name "It can be pretty tough, to stick with your beliefs and your heritage even when society looks down on you."
                the_person "It has been sometimes..."
                mc.name "Respecting yourself and where you come from is one of the things I love about you."
                mc.name "I understand what you are saying. And should an opportunity happen soon... I'd be proud to be your first."
                $ the_person.change_love(3, 80)
                $ mc.change_locked_clarity(20)
                the_person "Oh my god... I'm really, REALLY glad to hear you say that..."
                "Her foot touches yours under the table, and for a moment, she looks you straight in the eyes."
            "Be lewd\n{menu_red}Increases sluttiness{/menu_red}":
                mc.name "So you're saying I might have an opportunity in the near future, not just to deflower a smoking hot native girl, but to do it raw?"
                mc.name "So what, next weekend? I'll wait out by the front door of the coffee shop for when it closes?"
                the_person "Oh my god, you're ridiculous!..."
                $ the_person.change_slut(3, 70)
                $ mc.change_locked_clarity(40)
                "She smiles at you. You feel her foot under the table rub up against yours, and then slide up your leg..."
                the_person "I hope you back those words up with actions..."
            "Be commanding\n{menu_red}Increases obedience{/menu_red} (disabled)":
                pass
        $ the_person.draw_person(position = the_person.idle_pose)
        the_person "Alright. I gotta get back to work!"
        the_person "Seriously though... think about it!"
        $ the_person.draw_person(position = "walking_away")
        "You watch as [the_person.possessive_title] turns and starts to walk away. Her ass swaying with each step."
        "Goddamn, you're on the verge of tapping that! And she wants it raw!"
        $ clear_scene()
        "Still, she was very clear about it. She wants you to think about it for a few days before going any further."
    else:
        "This is when [the_person.possessive_title] would normally tell you she hates condoms, but the pregnancy settings prevent this interaction."
    $ kaya.event_triggers_dict["no_condom_talk"] = True
    $ kaya.event_triggers_dict["no_condom_talk_day"] = day
    return

init 2 python:
    def calc_pool_ball_sink_chance(skill = 0, difficulty = 0):
        if renpy.random.randint(0,100) < min((50 + (skill * 5) ) - (difficulty * 10), 90):
            return True
        return False
