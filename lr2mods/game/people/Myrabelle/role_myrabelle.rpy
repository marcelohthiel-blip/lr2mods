# Myrabelle is our generic gamer girl archetype. Blue hair, attitude, etc.
# Friends with Alexia from the start, she is opening a gaming café and is trying to make money in esports
# Her love story will be her primary story, revolves around her trying to establish an esports brand and make a name for herself
# Timeline involves working to get better, her first tournament (and failure), MC offering to sponsor her, 2nd attempt (success), finally business expansion
# Sluttiness story is a corruption of each step as we go along. When helping her to get better, train her focus while she is playing by fondling her.
# After sponsoring her, MC can add his own serum formula to the drink machines at the gaming café, allowing for corruption of the general public.
# When she reveals she didn't get a sponsorship the first time, can tell her she should get bigger tits.
# Myra's bar date opens up the option to play arcade game
#
# Team-up option is Alexia. On friday nights, they start to have all night gaming sessions. At first, MC just plays games with them, but it transitions to massages...
# ... topless massages, fingering, eventually at full corruption start the night with them naked and MC has total free-use while they play video games.
# initial release

label myra_rude_intro_label():
    $ the_person = myra
    "As you are walking around downtown, you stop at a crosswalk."
    $ the_person.draw_person()
    "As you stand there, a woman walks up and stands next to you, also waiting at the crosswalk."
    "You are struck by the woman's brightly coloured hair. You decide to say hello."
    mc.name "Hi there."
    "She looks at your briefly, then looks away. Did she not hear you?"
    mc.name "I like your hair, it looks great!"
    the_person "Err, thanks."
    mc.name "I'm [mc.name]."
    the_person "Fuck off, I don't talk with creepy randos on the street."
    $ the_person.draw_person(position = "walking_away")
    "As she says that, the crosswalk light turns to walk. She turns away from you and quickly starts walking."
    "You stop and watch her as she walks away. Despite your recent luck with women, you suppose it isn't surprising that not everyone is going to be receptive."
    $ clear_scene()
    "You continue walking, parting ways with the blue-haired lady."
    $ add_myra_gaming_cafe_opening_action()
    return

label myra_gaming_cafe_opening_label():
    $ scene_manager = Scene()
    $ the_person = myra
    $ gaming_cafe.visible = True        #Café is now open for business and you can go there anytime.
    $ myra.event_triggers_dict["gaming_cafe_open"] = True
    "As you walk around the mall, you notice a large sign."
    "GRAND OPENING: Predator LAN Gaming Café! Play for free during our grand opening!"
    "A gaming café? That seems interesting. You decide to head over to it."
    $ mc.change_location(gaming_cafe)
    "As you walk in, the place looks amazing. There are dozens of gaming PCs set up all over the place."
    "The place is pretty crowded, but you still see several open PCs. At the front counter, you spot someone familiar talking to someone behind the counter."
    $ scene_manager.add_actor(the_person, display_transform = character_right)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.possessive_title!c] appears to be talking to someone... isn't that the rude girl the other day you tried to talk to downtown?"
    alexia "This is awesome, I can't believe you actually did it."
    the_person "Yeah! It has been a crazy amount of work, but I finally did it!"
    "As you step up, [alexia.title] notices you."
    alexia "Oh hey [alexia.mc_title]! Here to check out the new gaming café?"
    mc.name "Indeed I am."
    "The girl behind the counter notices you. You think she remembers you, you notice her scrunch her nose a bit as she looks at you."
    the_person "You know this guy, [alexia.fname]?"
    alexia "Yeah! We went to the university around the same time, so we have known each other for a while."
    "The blue-haired girl behind the counter appears to be sizing you up."
    mc.name "I'm [mc.name]."
    "She's quiet for a moment longer."
    $ the_person.set_title("Myra")
    $ the_person.set_possessive_title("your gamer girl")
    $ the_person.set_mc_title(mc.name)
    $ the_person.primary_job.job_known = True
    $ the_person.set_event_day("day_met")
    the_person "I'm [the_person.fname], but you can call me Myra."
    "There is a bit of an odd silence for a few seconds."
    alexia "... well this is awkward... have you two met?"
    "Before you can say anything, [the_person.title] answers."
    the_person "He tried hitting on me the other day downtown."
    alexia "Ha! That sounds like him! I take it you shut him down?"
    mc.name "Now wait just a..."
    the_person "Of course."
    mc.name "I was just trying to tell you I thought your hair was very pretty."
    "[the_person.title] rolls her eyes."
    the_person "Right."
    alexia "Don't worry, he probably would have followed it up with a pick-up line. But let's be serious here, your hair DOES look great!"
    the_person "Thanks! I got it done in preparation for the grand opening, but I really like it! I think I might keep it like this."
    alexia "You should!"
    mc.name "So I take it you two are friends?"
    alexia "Yep! I've been playing this game called Guild Quest 2, and she is the guild leader."
    mc.name "So you met... playing a game?"
    alexia "No, we go back further than that, but lately it is mainly when playing that game."
    the_person "Yep! Cupcake and I go way back."
    alexia "Oh my gosh don't tell..."
    mc.name "Cupcake?"
    the_person "Well that's her character name, 'Blonde Cupcake'."
    "You laugh out loud."
    mc.name "Ha! Oh my, that is perfect for her!"
    "[alexia.possessive_title!c] just sighs."
    $ the_person.change_love(1)
    if alexia.is_employee:
        alexia "Anyway, [alexia.mc_title] here is actually a decent guy. He is the one who bailed me out of my coffee shop job."
        the_person "Ahh, that new marketing job you were telling me about?"
    else:
        alexia "Anyway, [alexia.mc_title] here is actually a decent guy. He helped me study and we often shared a cup of coffee or a bus ride."
        the_person "Ah, so he's more than just a pretty face?"
    alexia "Yeah! So, do you have Guild Quest on any of the PCs here already?"
    the_person "You better believe it! Let me show you. How about you [the_person.mc_title]? Want to play for a bit?"
    alexia "Oh! You should! Sit next to me, and I can help you get started!"
    "You've never played this game before, but you figure it couldn't hurt to give it a shot."
    mc.name "Sure, why not."
    the_person "The game has a free trial, but if you wind up liking it, you should probably buy it. Anyway, the PCs over here have the game set up and ready..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You and [alexia.title] follow [the_person.title] to a row of computers."
    "You follow [the_person.title] to one and [alexia.possessive_title] sits next to it."
    $ scene_manager.update_actor(alexia, position = "sitting")
    $ scene_manager.update_actor(myra, position = "standing_doggy")
    "[the_person.title] leans over the computer and starts the game up, and brings up a registration screen. You take a moment to check out her ass."
    "She is skinny but has some very nice curves, especially her back side..."
    $ mc.change_locked_clarity(10)
    $ scene_manager.update_actor(myra, position = "stand3")
    "When she stands back up, she looks at you with a smirk. Did she notice you checking her out? You were trying to be discreet..."
    $ the_person.change_slut(1)
    the_person "Alright, I've got it all set up for you! Have fun you two!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns and starts to walk away. You check her out one last time then sit down at the computer."
    alexia "This game is great! You're going to love it!"
    $ scene_manager.hide_actor(the_person)
    "You turn to the computer. You make an account, and soon you have a brand new level 1 ranger who you decide to name..."
    $ the_name = renpy.input("Pick your character name. (Default: 'BudLightyear')", default='BudLightyear', length = 20, exclude="[]{ }")
    $ mc.event_triggers_dict["guild_quest_name"] = the_name.strip()
    $ guild_quest_name = mc.event_triggers_dict.get("guild_quest_name", "BudLightyear")
    alexia "Alright, this is the tutorial area..."
    "You play the game for a while with [alexia.possessive_title]. After a couple hours, you are level 6."
    "You finish up an event where a giant undead monster rises up out of the swamp. With the help of Cupcake, you manage to kill it."
    alexia "Alright! Even though I'm max level, when you help noobs in this game, you can still get decent rewards."
    mc.name "That's good, I don't want to be a drag."
    alexia "Don't worry. Well, that is it for the free trial. What did you think?"
    mc.name "Well, I'm not much of a gamer, but it was neat that I can just pop in anytime I want to and make progress on my ranger."
    alexia "You should buy it!"
    $ scene_manager.show_actor(the_person, display_transform = character_right, position = "default")
    "As she is urging you, [the_person.title] walks up, checking on you and [alexia.title]."
    the_person "Hey, everything working good here?"
    alexia "Yeah this is great! And [alexia.mc_title] just finished up with the trial. I'm trying to convince him to buy it!"
    the_person "It is a great game, for hardcore and casual gamers alike, the way it is set up."
    "You think about it. It's only $20, and even though you don't play that many games anymore, it might be a good way to get closer with [alexia.title] and [the_person.title]."
    mc.name "Okay, why not. I'm not sure I'll be able to play much but it's only $20."
    $ alexia.change_happiness(5)
    alexia "Yay! We'll have to get you up to max level so you can help with end game stuff..."
    "[alexia.title] looks at [the_person.title]."
    alexia "Hey, can you add him to the guild?"
    the_person "Ah, that's a good idea! What's the username?"
    "[the_person.title] looks closely at your screen and laughs."
    $ the_person.change_love(1)
    the_person "[guild_quest_name] huh? That's pretty funny. I'll send out the invite later when I get the chance."
    $ mc.business.change_funds(-20)
    "You spend a few minutes and buy the game. You've been playing for a while now though and you decide to be done for now."
    "The two girls are talking as you close the game down."
    alexia "This is going to be great. I think I'll start coming here to play on the weekends. The computers are way better than mine, and being around other people is great!"
    the_person "It'll be fun having you around Cupcake! We'll be closed on Mondays and Tuesdays, but we have extended hours on the weekends!"
    $ alexia.set_schedule(gaming_cafe, day_slots = [5, 6], time_slots = [2, 3]) #Alexia plays at the café on weekends.
    mc.name "I need to get going, but this has been fun."
    alexia "See ya [alexia.mc_title]."
    the_person "I'll get that guild invite sent out later. Nice to meet you [the_person.mc_title]."
    mc.name "Thanks, you too."
    $ scene_manager.clear_scene()
    "You step away from the computer. This has certainly been an interesting development."
    "Any additional business here at the mall is good, and a gaming café should hopefully draw customers."
    "[the_person.title], the woman who is running it, is intriguing. You wonder if you might be able to get to know her better?"
    "She should be here at the café while it is open. Maybe you could impress her if you got good at the game she plays?"
    "You might have a chance to play with [alexia.title] sometimes too."
    $ add_myra_esports_practice_action()
    $ add_alexia_first_stream_action()
    $ alexia.progress.love_step = 2
    $ alexia.story_event_log("love")
    $ del guild_quest_name
    call advance_time(no_events = True) from _call_advance_time_myra_gaming_cafe_opening
    return

#Public serum distribution questline

label myra_develop_energy_drink_intro_label(the_person):  #20 sluttiness event. requires sponsorship. on room entry event. Why does this require sluttiness? Replace with something?
    $ the_person.draw_person(emotion = "angry")
    "You step into the gaming café. You notice [the_person.possessive_title] talking on her phone angrily."
    "You walk over to her and see what is going on."
    the_person "No! Come on, that's crazy! Those are like my favourite!"
    the_person "No... you know what? FINE! I'll just find a competitor!"
    "She clicks her phone off."
    mc.name "You okay?"
    the_person "NO! I'm fucking not!"
    mc.name "What's going on?"
    the_person "I just got off the phone. My beverage supplier said they can't supply the store here with my favourite energy drinks anymore!"
    the_person "How am I supposed to get my game on if I can't even concentrate!?!"
    "You think about it for a moment. What is even in energy drinks? They can't be that hard to make... maybe you could make some?"
    mc.name "I have a crazy idea."
    the_person "I'm listening..."
    mc.name "I run a pharmaceuticals company... it can't be that hard to come up with an energy drink formula."
    mc.name "What if I put something together and I can supply you with energy drinks for you to distribute?"
    mc.name "I mean, I'm already a sponsor. It would be good exposure for my company and you could have an exclusive deal on an energy drink."
    the_person "Hmm..."
    $ the_person.draw_person(emotion = "happy")
    the_person "That is actually a pretty damn good idea..."
    mc.name "I know right? What is your favourite flavour?"
    the_person "Me? Oh... well I've always loved blue raspberry flavoured stuff..."
    mc.name "Give me a few weeks to see what I can come up with. I'll come up with a formula and run some basic tests and if you like it, I'll supply it."
    "She thinks about your proposal for a moment."
    the_person "Alright... Let me know what you come up with!"
    "You have agreed to try and provide [the_person.title] with a new energy drink for her gaming café!"
    "The only problem is... you have no idea how to make energy drinks!"
    "You should talk to your head researcher. Maybe she can help you formulate a new serum trait to mimic an energy drink syrup?"
    $ add_myra_energy_drink_research_intro_action()
    return

label myra_energy_drink_research_intro_label(the_person):     #On talk event. Propose to research lead energy drink creation
    "You step into the research and development wing and step over to your head researcher's desk."
    $ the_person.draw_person(position = "sitting")
    "You set down an energy drink and blue raspberry flavoured hard candy on her desk."
    the_person "Ah, hello [the_person.mc_title]. Is this supposed to help me get more research done? I'm not really into energy drinks..."
    mc.name "No, but a lot of people DO like energy drinks. I was hoping you could do some research for me on how they work..."
    mc.name "...And make it blue raspberry flavoured, so we can market serums with this as an energy drink."
    the_person "Aha. I think I understand what you are trying to do. I'm pretty sure these things are just some B vitamins and caffeine..."
    "She looks at the items for a moment."
    the_person "Give me a few days and I'll let you know what I can come up with, okay?"
    mc.name "Thank you [the_person.title]. I appreciate it."
    "You step away from [the_person.possessive_title]'s desk. She will contact you when she comes up with a solution."
    $ add_myra_energy_drink_research_final_action()
    return

label myra_energy_drink_research_final_label():     #On talk event. Test energy drink with head researcher
    $ the_person = mc.business.head_researcher
    if mc.is_at(mc.business.r_div):
        the_person "[the_person.mc_title], I have some good news."

    else:
        $ mc.start_text_convo(the_person)
        the_person "I have something for you to see. Can you come to the lab?"
        mc.name "I'm on my way."
        $ mc.end_text_convo()
        "You make your way to the research division."
        $ mc.business.r_div.show_background()
    $ the_person.draw_person()
    the_person "I have a serum trait that I think meets your specifications."
    "[the_person.possessive_title!c] holds out a small blue vial."
    the_person "Several B, C, and D vitamins, zinc, and caffeine."
    the_person "Hit it hard with raspberry flavouring, blue dye, and some high fructose corn syrup, and voila!"
    the_person "Add this to any serum, along with 8 ounces of carbonated water, and the flavour is strong enough to cover up any chemical tastes from the other serum traits we include."
    mc.name "That's great. Any downsides?"
    the_person "Well, watering down serums reduces the length of time that the serum is effective for. And it will take up a trait slot in the research phase from something more useful."
    mc.name "That is great. Thank you [the_person.title]"
    the_person "No problem."
    $ add_myra_energy_drink_test_action()
    "You have unlocked the energy drink serum trait!"
    "Create a new serum using the trait and take it to [myra.possessive_title], and if she likes it you can start distributing it there to the public!"
    "For now, you should probably not do anything too controversial. Keep the attention of the serum at 2 or less, and don't distribute any nanobots!"
    return

label myra_energy_drink_test_label(the_person):
    $ the_serum = get_random_from_list(mc.inventory.get_serums_with_trait(energy_drink_serum_trait))
    "You walk into the gaming café. At the main desk, you spot [the_person.title] and approach her."
    $ the_person.draw_person()
    mc.name "Good day [the_person.title]."
    the_person "Hey [the_person.mc_title]."
    mc.name "I have something for you."
    "You set a can of your new energy drink on the table."
    mc.name "One proprietary, blue raspberry flavoured energy drink."
    the_person "Wow! This is neat... May I?"
    mc.name "Of course."
    "[the_person.possessive_title!c] takes the drink and opens it. She gives it a sniff, then takes a long sip."
    $ mc.inventory.change_serum(the_serum,-1)
    $ the_person.give_serum(copy.copy(the_serum), add_to_log = True)
    "She smiles."
    the_person "Hey... that is really good!"
    "She takes another long sip."
    the_person "What is in it?"
    mc.name "Well, I'll be honest, it was mostly done by my head researcher; but she said there are a lot of vitamins in it, some caffeine, and zinc."
    "[the_person.title] keeps drinking it."
    mc.name "After that, we had to balance the raspberry flavour, and added some sweetness with corn syrup."
    "You conveniently leave out the remaining serum traits that went into the production. [the_person.possessive_title!c] takes several large gulps."
    mc.name "We have nutritional facts we can publish, as well as an ingredient and allergen list."
    "She tips up her drink and finishes it off."
    the_person "This is incredible. I love it!"
    $ the_person.change_stats(obedience = 2, love = 2)
    the_person "I feel more energized already. Alright, if you can make delivery on Wednesday mornings, I'll set it up to sell!"
    mc.name "Sounds good. I'll arrange for delivery with one of my employees."
    the_person "This is fucking awesome. What do you call it?"
    mc.name "Well, we have an internal name for it, but it isn't really something we would call on-brand for you."
    mc.name "Since it is made to your specifications, why not call it something like Myra's Gaming Fuel."
    the_person "Ooh! I like it!"
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title!c] throws her arms around you and gives you a big hug."
    the_person "Thank you [the_person.mc_title]! This is going to be great!"
    mc.name "I agree."
    $ clear_scene()
    "You step away from the desk after saying goodbye. You should set up delivery of the serum with one of your employees."

    if alexia.is_employee:
        "Since [alexia.possessive_title] is working for you, it makes sense to have her do the deliveries. You should talk to her about it next chance you get."
        $ add_myra_energy_drink_distribution_intro(alexia)
    else:
        "No one really stands out to you as an obvious choice for who to have run the deliveries."
        "Who should you talk to about it?"
        call screen main_choice_display(build_menu_items([["Call in"] + mc.business.employees_availabe], draw_hearts_for_people = False))
        if isinstance(_return, Person):
            $ add_myra_energy_drink_distribution_intro(_return)
            "You decide to talk to [_return.title] about running the deliveries. You should talk to her about it as soon as practical."
    return

label myra_energy_drink_distribution_intro_label(the_person):     #On talk event. Work out details of distributing energy drink at gaming café with myra
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. I want to talk to you about something."
    the_person "Oh? Go ahead."
    if the_person == alexia:
        mc.name "The company has developed a new energy drink for [myra.fname] to sell over at the gaming café. I was hoping you could run the deliveries for me."
        the_person "Oh! That is really neat! I bet she is excited! When do you want me to run the deliveries out?"
    else:
        mc.name "The company has started sponsoring an esports team at the local gaming café. We have developed an exclusive energy drink to sell there."
        mc.name "I want you to be in charge of running the deliveries every week."
        the_person "Okay, I can do that. When do you want me to do the deliveries?"
    "You talk to [the_person.title] about taking some energy drink over to the gaming café every Wednesday."
    the_person "Okay, I'll talk to you on Wednesday morning then."
    $ add_myra_energy_drink_weekly_distribution()
    "[the_person.possessive_title!c] will be running your deliveries. Make sure you have at least 10 of the serum in the company's inventory to send to the gaming café."
    return

label myra_energy_drink_weekly_distribution_label():          #mandatory event. select which serum to distribute for the week.
    $ contact = myra.event_triggers_dict.get("energy_drink_supplier", None)
    $ new_delivery_person = False
    $ finished = False
    if contact is None:
        "Unfortunately, your delivery person is not available anymore. You decide to appoint someone new to do it."
        call screen main_choice_display(build_menu_items(
            [get_sorted_people_list(mc.business.employees_availabe, "Call in")],
            draw_hearts_for_people = False))

        $ the_person = _return
        $ myra.event_triggers_dict["energy_drink_supplier"] = the_person.identifier
        $ new_delivery_person = True
    else:
        $ the_person = Person.get_person_by_identifier(contact)
        if not the_person.is_employee or not the_person.is_available:
            "Unfortunately, your delivery person is not available anymore. You decide to appoint someone new to do it."
            call screen main_choice_display(build_menu_items(
                [get_sorted_people_list(mc.business.employees_availabe, "Call in")],
                draw_hearts_for_people = False))
            $ the_person = _return
            $ myra.event_triggers_dict["energy_drink_supplier"] = the_person.identifier
            $ new_delivery_person = True
    $ contact = None

    if new_delivery_person:
        "You head to your office, paging [the_person.title] to meet you there."
        $ mc.change_location(ceo_office)
        $ the_person.draw_person()
        the_person "Hello [the_person.mc_title]!"
        mc.name "Hi [the_person.title], I need you to do something for me."
        mc.name "The company has started sponsoring an esports team at the local gaming café. We have developed an exclusive energy drink to sell there."
        mc.name "I want you to be in charge of running the deliveries every week."
        the_person "Okay, I can do that. When do you want me to go?"
        mc.name "Now, let me just set up which serums I want you to deliver."
    elif mc.is_at_office:
        $ the_person.draw_person()
        $ the_serum = None

        the_person "Hey [the_person.mc_title]. I was just getting ready to take over the energy drinks for [myra.fname]."
        the_person "Which one did you want me to take over?"
    else:
        "You get a message from [the_person.title]. She wants to know which serums you want delivered to the gaming café this week."
    "You take a look at your business' inventory. Time to decide which serum to send over to the gaming café for the next week."
    "You quickly remind yourself, the serum must include the energy drink trait, attention should be less than 3, and you need at least 10."
    call screen serum_inventory_select_ui(mc.business.inventory, batch_size = 10, select_requirement = myra_serum_is_acceptable_energy_drink)
    if isinstance(_return, SerumDesign):
        $ the_serum = _return
        "You set it up for [the_person.title] to take 10 [the_serum.name]s to the gaming café."
        "It will be distributed there for the next week to anyone who stops by."
        $ myra_set_weekly_serum(the_serum)
        $ mc.business.inventory.change_serum(the_serum, -10)
    else:
        $ the_serum = None
        "You decide not to send over any energy drinks this week."
        $ myra_set_weekly_serum(None)
    if new_delivery_person or mc.is_at_office:
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] walks away."
    else:
        "You set up the delivery of the energy drink over the phone."
    $ add_myra_energy_drink_weekly_distribution()
    return

#End game sexual events

label myra_breeding_on_stream_label():    #Requires breeding and exhibition fetish
    $ the_person = myra
    $ the_person.arousal = 40
    "You feel your phone vibrate. It's a message from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey! Can you come to the café? I need your help with something."
    mc.name "What help do you need?"
    the_person "Some of my streaming fans have been requesting something. I need your help with it though."
    the_person "As a hint, I am super fertile right now ;)"
    mc.name "I'll be right there."
    $ mc.end_text_convo()
    "Sounds like [the_person.title] wants to get bred on stream... seems too good to pass up!"
    "You head over to the game café. Then make your way to the adults only section."
    $ mc.change_location(gaming_cafe)
    $ the_person.apply_outfit(Outfit("Nude"))
    "When you get there, you take a quick look around, then spot [the_person.possessive_title]. It appears she has already started her stream..."
    $ the_person.draw_person(position = "walking_away")
    "She is laying on a couch, facing a screen while she holds a controller. She is naked, and her ass is ripe and ready to be fucked."
    "To one side, you see a computer screen where she has her streaming setup. There is a side angle view of her, showing off her curves on the couch."
    the_person "Fuck yeah! Got you bitch!"
    "As you start walking towards her, she manages to score a kill in the shooter she is playing. You know exactly what part you play in this stream."
    "You have no doubt she really is fertile right now. You are about to knock her up live on stream."
    "You take your clothes off, then slowly approach her from behind."
    "You run your hand up her legs as you climb onto the couch. She peeks at the screen and sees that it's you, but otherwise doesn't let herself react at all."
    "Her legs part just the slightest as you run your hand up between them. You can feel the heat and humidity coming off her cunt when your hand gets to it."
    "[the_person.title] is turned on and ready to fuck. You give her ass a little spank then climb onto her."
    "The only indication she gives of what is about to happen, she says on the headset to her teammates." #I'm not sure how to fix this line but it sounds wrong
    if the_person.is_girlfriend:
        the_person "Hey, sorry if I seem distracted for a bit. My boyfriend is here and he is going to knock me up now. No no, I'm going to keep playing."
    else:
        the_person "Hey, sorry my sperm donor is here and he's about to knock me up, sorry if I seem a bit distracted. No no, I'm going to keep playing."



    return
