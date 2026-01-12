#Aunt Role Action Requirements
###AUNT ACTION LABELS###
label aunt_intro_label():
    #NOTE: Doesn't technically contain the aunt, but introduces the concept of her when she appears the next day
    $ bedroom.show_background()
    mom "Hey [mom.mc_title], do you have a moment?"
    $ mom.draw_person()
    "[mom.possessive_title!c] cracks your door open and leans in."
    mc.name "Sure [mom.title], what's up?"
    mom "You remember your aunt [aunt.name], right? Well, she's been having a rough time with her husband lately and they're separating."
    "You nod and listen. [aunt.possessive_title!c] never spent much time visiting when you were a kid and it's been years since you've seen her at all."
    mom "It seems like he's going to be keeping the house, so she's going to be staying with us for a few days while she finds a new place to live."
    mom "She'll be bringing your cousin [cousin.name], too. You two haven't seen each other since you were kids, have you?"
    mc.name "No, it's been a long time."
    mom "I know it's going to be a little tight here while we sort this out, but she's family and I need to be there for her."
    mc.name "I understand [mom.title]. I'll help out however I can."
    $ mom.change_happiness(5)
    mom "That's so nice to hear [mom.mc_title], thank you. My [cousin.fname] will be sharing [lily.fname]'s room with her and aunt [aunt.name] will be on the couch in the living room."
    mom "They're going to be here in the morning. If you have a few minutes, could you help me pull out some sheets and get their beds made?"
    menu:
        "Help [mom.possessive_title] set up":
            mc.name "Sure, let's go get it done."
            $ mom.change_stats(happiness = 3, love = 2)
            "You and [mom.possessive_title] go to the laundry room and gather up extra pillows, sheets, and towels for your house guests."
            "You fold out the couch in the living room and dress it up as a temporary bed for your aunt."
            "Next, you drag an air mattress into [lily.title]'s room and start inflating it."
            $ lily.draw_person()
            lily "Mom, I don't even know [cousin.fname]. Can't she have [lily.mc_title]'s room and he can sleep somewhere else?"
            $ mom.draw_person()
            mom "Your brother has to worry about his work. It's just for a couple of days. I'm sure you and [cousin.fname] will get along just fine."
            "[lily.possessive_title!c] pouts but stops complaining. You and [mom.possessive_title] finish setting up the air mattress."
            mom "Alright, I think that's everything. Thank you so much for the help [mom.mc_title]. I know it's late and you probably want to get to bed."
            "[mom.possessive_title!c] gives you a hug and kiss on the forehead. You head off to your room and go to sleep."



        "Make [lily.possessive_title] do it":
            mc.name "Sorry [mom.title], I've got an early morning tomorrow and really need to get to bed. I think [lily.fname]'s free though."
            $ lily.change_stats(obedience = 2, love = -1)
            mom "Of course, [mom.mc_title]. I'm sure your sister won't mind helping. You get a good night's sleep."
            "[mom.possessive_title!c] gives you one last smile as she closes your door. You hear her talking to your sister outside while you get ready for bed."

    $ clear_scene()
    $ add_aunt_intro_phase_two_action()
    return

label aunt_intro_phase_two_label():
    #They show up at your house in the morning. Quick introductions with everyone.
    "In the morning [mom.possessive_title] wakes you up early with a knock on your door."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom)
    mom "[mom.mc_title], I just got a call, your aunt and cousin are on their way over. Get ready so you can help move their stuff inside."
    $ kitchen.show_background()
    "You get up, get dressed, and head to the kitchen to have some breakfast. [mom.possessive_title!c] paces around the house nervously, looking for things to tidy."
    $ her_hallway.show_background()
    $ scene_manager.add_actor(lily)
    "Finally the doorbell rings and she rushes to the door. You and [lily.title] join her in the front hall as she greets your guests."
    mom "[aunt.fname], I'm so glad you made it!"
    $ scene_manager.add_actor(aunt)
    $ scene_manager.add_actor(cousin, position = "sitting")
    aunt "[mom.fname]!"
    $ mc.change_locked_clarity(10)
    $ scene_manager.update_actor(aunt, position = "kissing")
    "[aunt.title] lets out an excited, high–pitched yell and rushes forward to hug [mom.possessive_title]."
    $ scene_manager.update_actor(mom, position = "kissing")
    aunt "Thank you so much for taking us in. It means the world to me and [cousin.fname]."
    $ scene_manager.update_actor(mom, position = "default")
    $ scene_manager.update_actor(aunt, position = "default")
    "[mom.possessive_title!c] breaks the hug. Your cousin, [cousin.title], sits outside the door on a suitcase, idly scrolling through her phone."
    mom "How are you doing [cousin.fname]? Holding up okay?"
    "She shrugs and doesn't take her eyes off her phone."
    cousin "Eh. Fine..."
    aunt "She's thrilled, really. Now who are these two little rascals I see?"
    $ scene_manager.update_actor(aunt, position = "kissing")
    "[aunt.possessive_title!c] steps into the house and throws her arms wide, pulling you and your sister in to a hug."
    aunt "I mean, it must be [mc.name] and [lily.fname], but you're both so much bigger than I remember!"
    $ mc.change_locked_clarity(10)
    $ scene_manager.update_actor(aunt, position = "default")
    "She hugs you both tight and then lets go. [aunt.title] looks at you in particular and laughs."
    aunt "I remember when you were just a little baby, and now you're a full–grown man. Oh no, I'm showing my age, aren't I. Hahaha."
    "She laughs and turns back to grab her things. [cousin.title] sighs loudly outside and rolls her eyes."
    aunt "Now [mom.fname], where should I bring my things?"
    $ scene_manager.update_actor(mom, position = "walking_away")
    mom "Just follow me, I'll show you around. We got everything set up as soon as we heard the news."
    $ scene_manager.remove_actor(mom)
    $ scene_manager.update_actor(aunt, position = "walking_away")
    "[mom.possessive_title!c] leads [aunt.possessive_title] into the house."
    $ scene_manager.hide_actor(aunt)
    "When they're gone [lily.possessive_title] takes a step towards [cousin.title]."
    lily "Hi [cousin.fname], it's nice to see you again. I don't think we've talked since we were little kids."
    cousin "Yep..."
    "There's a long period of awkward silence."
    lily "... Right. Well I'm sure we'll get along while you're staying with me."
    "[aunt.possessive_title!c] calls from farther inside the house."

    aunt "[cousin.fname], sweetheart, you should come see your room! I'm sure [lily.fname] and [mc.name] will help bring your stuff in."
    $ scene_manager.update_actor(cousin, position = "default")
    "[cousin.possessive_title!c] gets up from her suitcase seat, picks up her smallest bag, and walks inside."
    $ scene_manager.update_actor(cousin, position = "walking_away")
    cousin "Thanks for the help."
    $ scene_manager.remove_actor(cousin)
    "[lily.title] glances at you and rolls her eyes dramatically. The two of you grab more luggage and start hauling it inside."
    "After a few minutes all the suitcases have been moved to where they need to go."
    $ mc.change_location(hall)
    $ scene_manager.show_actor(aunt, position = "default")
    aunt "Thank you two so much, you're such sweethearts. Here's something for all your hard work."
    $ aunt.change_love(2)
    $ mc.business.change_funds(20)
    "[aunt.possessive_title!c] finds her purse, pulls out her wallet, and hands you and [lily.possessive_title] $20."
    aunt "Now I think your mother wanted to talk with me. I'm sure you both have busy days, so don't let me keep you!"
    #Their temporary homes are at your place. Later we will restore them to their normal homes.
    python:
        add_aunt_drunk_cuddle_action()
        add_aunt_phase_three_action()
        add_cousin_phase_one_action()
        scene_manager.clear_scene()
        scene_manager = None
        aunt.story_event_log("slut")    #Aunt can have drunken cuddles while still living with MC, so we set the timer for it here.
    return

label aunt_intro_phase_three_label():
    #Your aunt lets you know that she has an apartment lined up, and if you have free time would appreciate some help moving in.
    "There's a quick knock at your door."
    aunt "[aunt.mc_title], I hope you're decent because I'm coming in!"
    $ aunt.draw_person(emotion = "happy")
    "[aunt.possessive_title!c] throws your bedroom door open and steps in before you have a chance to answer."
    mc.name "Morning [aunt.title], uh... What's up?"
    aunt "Earlier today I got a call with some fantastic news. My realtor found this beautiful little apartment downtown for me and [cousin.fname]!"
    aunt "That means in a few days we'll be out of your hair and your house can go back to normal."
    mc.name "It was nice having you around [aunt.title], but I'm happy you're getting back on your feet. Things will be back to normal for you soon, too."
    aunt "I hope so. I actually had one {i}tiny{/i} little favour to ask while I was here..."
    mc.name "What is it?"
    aunt "Well now that it's just me and [cousin.fname], we don't have anyone to help us with the heavy lifting when we move in."
    aunt "We'll be moving our things starting tomorrow. If you have any free time to help us, it would mean the world to me."
    mc.name "I'll see if I have some spare time in my schedule and come to you if I do."
    $ aunt.draw_person(position = "sitting", emotion = "happy")
    $ aunt.change_happiness(8)
    $ mc.change_locked_clarity(5)
    "[aunt.possessive_title!c] sits on the side of your bed, puts a hand on your leg, and squeezes it gently."
    aunt "I'm so lucky to have such a wonderful nephew, you know that? If only I had married a man like you instead of..."
    aunt "Well, never mind that. Thank you."
    "She leans in, gives you a warm, familial hug, and then leaves you to get on with your day."
    $ clear_scene()

    $ add_aunt_moving_action()
    return

label aunt_intro_moving_apartment_label(the_person):
    #You help her move in, with different focuses each time you do it.
    $ aunt.draw_person()
    mc.name "[aunt.title], I've got a few free hours. Would you like some help moving your things?"
    aunt "Oh [aunt.mc_title], your help would be amazing. Here, let's go look at what we have to move."
    if aunt.event_triggers_dict.get("moving_apartment") == 0:
        #You help them and get a brief overview of what they're bringing in the future
        "You follow [aunt.possessive_title] to the stack of boxes, luggage, and furniture that are being stored in the garage."
        aunt "With your help I think we can manage this in four trips. Today we'll rent a truck and move all the big stuff in."
        aunt "Once that's done we can move all of my things into my room, then we move [cousin.fname]'s stuff."
        aunt "Last, we move in the kitchen things and get the place all tidied up. Sound good?"
        mc.name "Yeah, let's get started I guess."
        $ aunt.change_stats(happiness = 5, love = 2)
        aunt "Thank you so much! I'll go rent that truck, you just stay here and I'll be back in a little bit."
        $ clear_scene()
        "[aunt.title] gets in her car and drives off. You organize the boxes so they'll be easier to load when she gets back."
        cousin "What're you doing out here?"
        "You're startled by [cousin.possessive_title]'s voice. You spin around and find her leaning against the house door frame."
        $ cousin.draw_person()
        mc.name "Your mom's going to rent a truck. I'm helping you guys move your stuff over to your new place."
        cousin "Why?"
        menu:
            "Because it's a nice thing to do":
                mc.name "Because it's a nice thing to do, that's all."

            "Because I want to impress her":
                mc.name "Because I want to make a good impression. I want her to like me."

            "Because I'm hoping she'll pay me":
                mc.name "Because I'm hoping when we're done she'll pay me for the help."

        cousin "That's dumb, but whatever."
        mc.name "Yeah, whatever. [aunt.title] will be back soon. Do you want to give me a hand?"
        cousin "Not really. Be careful with my stuff."
        $ cousin.draw_person(position = "walking_away")
        "With that she turns around and goes back inside."
        $ clear_scene()
        mc.name "You're welcome..."
        "A few minutes later [aunt.title] pulls up in a rented pickup truck. You load up the back with furniture and boxes, then get in the passenger seat."
        $ aunt.draw_person(position = "sitting")
        $ mc.change_locked_clarity(5)
        aunt "Okay, let's get going! I don't know what I'd do without a big strong man like you to lift things for me. I'd be helpless!"
        $ aunt.change_love(1)
        $ downtown.show_background()
        "It doesn't take long to drive to [aunt.title]'s new apartment. She parks out front and you grab a box to bring up with you."
        $ aunt.draw_person()
        $ aunt_apartment.show_background()
        "The apartment is small but tidy, with two bedrooms and a combined living area and kitchen. [aunt.title] gestures to one of the bedrooms."
        aunt "My room will be in there, and the other one will be [cousin.fname]'s room. You can put that box down and go get another, I'll start unpacking."
        "The next couple of hours are spent unloading the truck and bringing everything up to [aunt.possessive_title]."
        "When you're done [aunt.title] returns the truck and drives you both home. When you get out of the car she gives you a tight hug."
        $ aunt.change_stats(happiness = 5, love = 3)
        $ aunt.draw_person(emotion = "happy")
        $ mc.change_locked_clarity(5)
        aunt "You're my hero [aunt.mc_title]. Come see me if you have any more spare time and we can move the rest of this over."
        "She breaks the hug and smiles."
        aunt "Now I'm going to go see if I can use your mother's shower!"
        $ clear_scene()



    elif aunt.event_triggers_dict.get("moving_apartment") == 1:
        #You help move your aunt's wardrobe and get a chance to dig through her underwear
        "You and [aunt.title] head to the garage and look over the stuff that still needs to be moved."
        aunt "I think we can move my things over today. If I need something I can always borrow it from your mother."
        aunt "She always hated when I borrowed her clothes when we were younger. She said I stretched out her tops."
        $ mc.change_locked_clarity(10)
        aunt "I think she was just jealous I got the nicer tits."
        "[aunt.possessive_title!c] laughs and blushes."
        $ aunt.change_slut(1, 20)
        aunt "Sorry, I shouldn't be talking about your mom's chest like that. It's different when you're sisters, you know?"
        mc.name "Oh yeah, I know what you mean."
        aunt "Anyway, we have work to get done. I think we can fit all of my clothes in the back of my car, so we don't need a truck today."
        aunt "Let's load it up and we can bring it all over."
        "You and [aunt.title] load up her hatchback with boxes filled with clothes. Once the car is loaded to capacity, you get in and drive to her new apartment."
        $ aunt_apartment.show_background()
        "When you arrive, you start to shuttle boxes up to [aunt.possessive_title]'s bedroom. [aunt.title] is kept busy unpacking the boxes and putting everything away."
        $ aunt.draw_person(position = "sitting")
        "After some hard work the car is empty and the last box is in [aunt.title]'s room."
        aunt "Thank you for all the help [aunt.mc_title]. It'll just take me a few minutes to get the rest of this put away."
        $ aunt.change_stats(happiness = 5, love = 1)
        menu:
            "Offer to help":
                mc.name "Here, let me help with that. Just tell me where to put things."
                $ aunt.change_love(1)
                aunt "My sister raised such a perfect gentleman! Here, this goes in the top drawer over there."
                "You clear out a couple of boxes, putting away shirts, skirts, and pants for [aunt.title]. [aunt.possessive_title!c] reaches for the last box, marked {b}Private{/b}, then hesitates."
                aunt "I can go through this one myself. It's all my underwear and that's probably the last thing you want to be digging through."
                mc.name "We're both adults, it's no big deal."
                "[aunt.possessive_title!c] shrugs, opens the box, and starts to sort through it. She hands you a pile of colourful panties."
                aunt "Okay, put these in that drawer on the left..."
                $ mc.change_locked_clarity(5)
                "You slide the garments into their drawer. Next [aunt.title] hands you a stack of lacey bras and small thongs."
                aunt "This goes to the side... and then... Oh my."
                "She closes the box and looks away, blushing."
                aunt "This is so embarrassing [aunt.mc_title]. I'll just finish this up myself later."
                mc.name "Come on, we're almost done."
                $ aunt.change_slut(1, 20)
                aunt "Don't tell my sister about this."
                $ mc.change_locked_clarity(10)
                "[aunt.title] pulls out the last few pieces of underwear from the box: a collection of g-strings and nippleless bras."
                mc.name "Is that all? I thought you had something to be embarrassed about."
                "You pick the tiniest g-string and hold it up against your waist. [aunt.title] laughs and snatches it from your hands."
                aunt "Stop that! I bought those for my husband, not that he ever cared what I wore. He was more interested in what his secretary {i}wasn't{/i} wearing."
                "She throws the underwear back at you."
                $ aunt.change_slut(1, 20)
                aunt "You know what, keep all this stuff near the front. Maybe I'll get a chance to wear it for someone who'll appreciate it."
                "You put away [aunt.title]'s sexy underwear and finish your work for the day."

            "Take a break":
                mc.name "Alright, I'm going to go get a glass of water and catch my breath."
                aunt "Go ahead, you've certainly earned it!"
                $ aunt.change_obedience(1)
                $ clear_scene()
                "You get a glass of water and sit down on the new sofa in the living room."
                "After half an hour [aunt.possessive_title] comes out and dusts off her hands."


        aunt "Alright, that's everything for today [aunt.mc_title]. Let's get you home."
        $ clear_scene()

    elif aunt.event_triggers_dict.get("moving_apartment") == 2:
        #You help move your cousin's wardrobe and get a chance to dig through her underwear. She catches you and taunts you "You little perv, you'll never get to see me wear something like that." kind of stuff.
        "You head to the garage and look at the dwindling pile of boxes that need to be moved."
        aunt "I think we can move [cousin.fname]'s things today. I'll go get her."
        $ clear_scene()
        $ scene_manager = Scene()
        $ scene_manager.add_actor(aunt)
        $ scene_manager.add_actor(cousin)
        "[aunt.possessive_title!c] is gone for a few minutes before coming back with [cousin.title] in tow."
        aunt "Let's get this show on the road! I know [cousin.fname] is excited to have a room to herself again, aren't you sweetheart."
        cousin "I'm not your sweetheart Mom. Let's just get this over with."
        $ mc.change_location(downtown)
        $ scene_manager.update_actor(cousin, position = "sitting")
        "She sulks over to [aunt.title]'s car and gets in the passenger seat."
        aunt "Sorry about that [aunt.mc_title]. She doesn't always play nice with others and this whole move has been tough on her. Could you help me load up the car?"
        mc.name "Sure. Just tell me where to put things."
        $ scene_manager.update_actor(aunt, position = "sitting")
        "You fill up [aunt.title]'s hatchback and get in the back seat with the last box sitting on your lap. [cousin.title] puts on headphones and ignores both of you."
        $ mc.change_location(cousin_bedroom)
        $ scene_manager.hide_actor(aunt)
        $ scene_manager.update_actor(cousin, position = "default")
        "When you arrive, you start to shuttle everything up to [cousin.possessive_title]'s room."
        $ scene_manager.update_actor(cousin, position = "sitting")
        "[cousin.title] sits down on her bed and gets her phone out. She looks up occasionally to tell you where to put boxes down."
        mc.name "You could help, you know."
        cousin "I could, but I don't want to. You're doing fine."
        $ scene_manager.show_actor(aunt, position = "default")
        "[aunt.possessive_title!c] pokes her head into the room."
        aunt "[cousin.fname], sweety, we should go downstairs and get an extra key for you."
        $ scene_manager.update_actor(cousin, position = "walking_away")
        $ scene_manager.hide_actor(aunt)
        "[cousin.title] rolls her eyes dramatically, then gets up and follows her mother. She stops just before leaving and looks back at you."
        cousin "Don't touch my stuff."
        $ scene_manager.hide_actor(cousin)
        menu:
            "Touch her stuff":
                "She's not the boss of you. You wait a couple of minutes then start snooping around."
                "Most of the boxes are clearly labelled, but you find one that just says \"Keep Out!\" on the side."
                "You open the box and find it filled with all of [cousin.title]'s underwear, all black, purple, or blue."
                $ mc.change_locked_clarity(10)
                "You dig deeper, past the large cupped bras she needs for her big tits. She has a handful of g-strings, fishnet stockings, and a garter belt near the bottom."
                "You think you feel something rigid at the bottom, but your search is interrupted by the front door lock clicking open."
                "You rush to get [cousin.possessive_title]'s underwear back in order. You slam the box shut and sit down on her bed, trying to look nonchalant."
                $ scene_manager.show_actor(cousin, position = "default")
                cousin "You didn't paw through my things, did you?"
                mc.name "Of course not, you told me not to."
                "She glares at you, then at her box of underwear, then at you again. She shakes her head."
                $ cousin.change_obedience(-3)
                cousin "Pervert."
                mc.name "Fine, I was curious. I didn't know what was in there."
                $ cousin.change_slut(2, 20)
                cousin "Whatever. It's not like you'll ever get to see me in it. I bet you'd like to though. I bet you're weird like that."
                "[cousin.title] gives you a strange, mischievous smile."
                $ mc.change_locked_clarity(10)
                cousin "Do you want to see me try some of it on? I won't tell anyone."
                menu:
                    "Yes":
                        "You nod your head. [cousin.title] laughs."
                        $ cousin.change_stats(happiness = 10, slut = 1, max_slut = 30)
                        cousin "Ha! You wish you pervert. Now get out of here before I tell my [aunt.fname]."

                    "No":
                        mc.name "What? No, you're being weird now."
                        "She shrugs."
                        cousin "Your loss. You'll just have to imagine it now. Now get out of here before I tell my mom you're digging through my things."

                "You get up off of [cousin.title]'s bed and leave."


            "Don't touch her stuff":
                "Not wanting to bring down [cousin.title]'s wrath, you focus on bringing up the rest of the boxes from the car."
                "Twenty minutes later, [aunt.title] and [cousin.title] come back just after you're done moving the last box."
                $ scene_manager.show_actor(cousin, position = "default")
                cousin "You didn't paw through my things, did you?"
                mc.name "Of course not, you told me not to."
                $ cousin.change_stats(happiness = 2, obedience = -3)
                cousin "Good."

        $ mc.change_location(downtown)
        $ scene_manager.show_actor(cousin, position = "sitting")
        $ scene_manager.show_actor(aunt, position = "sitting")
        "With your work done for the day, the three of you drive back home."
        $ mc.change_location(hall)
        $ scene_manager.hide_actor(cousin)
        $ scene_manager.update_actor(aunt, position = "kissing")
        "[aunt.title] gives you a big hug when you get out of the car."
        $ aunt.change_love(1)
        aunt "Thank you again for all the help."
        $ scene_manager.clear_scene()
        $ scene_manager = None


    elif aunt.event_triggers_dict.get("moving_apartment") == 3:
        #You help them move their kitchen stuff in. Your aunt gets dirty/sweaty and wants to chance now that her clothes are here. She asks you to wait around while she takes a shower, then
        #the landlord shows up and needs some documents from her, so you have to come into her bathroom and get a chance to see her naked/just in her underwear or something.

        "You head to the garage and look at the small pile of boxes left."
        aunt "I think it's just the kitchen stuff left. Let's get this packed in the car and we'll have everything moved over!"
        "You fill up [aunt.possessive_title]'s hatchback and head for her apartment."
        $ aunt_apartment.show_background()
        "You and [aunt.possessive_title] get to work shifting boxes upstairs."
        "After the first couple of boxes are upstairs, she starts to unpack them while you keep unloading the car."
        "It takes a couple of hours to get everything moved and unpacked. You and [aunt.title] are happy when the last box is emptied and you're finished with the move."
        $ aunt.change_happiness(5)
        aunt "[aunt.mc_title], I think that's everything! I think we should order a pizza and celebrate a little, what do you say?"
        mc.name "That sounds good to me. I'm starving."
        $ aunt.change_love(1)
        aunt "I'm sure you are, you've been doing all the heavy lifting for me! You're my big strong man, coming in to rescue me."
        $ mc.change_locked_clarity(5)
        "She gives you a hug, then grabs her phone and finds a local pizza place that delivers. She places your order."
        aunt "They said it may take a little while. All this hard work got me all sweaty. I'm going to go take a shower. Back in a bit!"
        $ clear_scene()
        "[aunt.possessive_title!c] heads off to the bathroom and you hear the shower start."
        "You're killing time on your phone when there's a knock on the door. It's the pizza guy."
        "Pizza Guy" "Hey, this is for you. One large."
        "He hands it over, then waits for you to pay."
        menu:
            "Pay for the pizza\n{menu_red}Costs: $25{/menu_red}" if mc.business.has_funds(25):
                mc.name "Thanks, here you go."
                $ mc.business.change_funds(-25, stat = "Food and Drinks")
                "Pizza Guy" "Thanks man, enjoy."
                "You take the pizza into the kitchen. A couple of minutes later [aunt.title] comes out of the bathroom."
                $ aunt.apply_planned_outfit()
                $ aunt.draw_person()
                aunt "Oh, is that here already? I'm sorry [aunt.mc_title], I was going to pay for that."
                mc.name "Don't worry about it, it's no big deal."
                $ aunt.change_love(1)
                aunt "Well thank you. Give me a slice of that, I'm starving now too!"

            "Pay for the pizza\n{menu_red}Not enough money{/menu_red} (disabled)" if not mc.business.has_funds(25):
                pass

            "Get the money from [aunt.title]":
                mc.name "Thanks, I just have to get the money. One sec."
                "The pizza guy nods and hangs out in the doorway while you head to the bathroom door and knock."
                aunt "Hmm? What is it?"
                mc.name "The pizza guy's here."
                aunt "Oh! I didn't think he would be here so soon! Just, uh... just come in and get it, it's in my purse."
                $ home_bathroom.show_background()
                "You open the door to the bathroom. [aunt.possessive_title!c]'s shower has a clear glass door that doesn't hide anything. She turns away as you come in."
                $ aunt.apply_outfit(Outfit("Nude"))
                #$ aunt.outfit = default_wardrobe.get_outfit_with_name("Nude 1") changed v0.24.1
                $ aunt.draw_person(position = "back_peek")
                $ aunt.change_slut(2, 40)
                $ mc.change_locked_clarity(10)
                aunt "It's right over there. Just grab it and go."
                "She nods her head towards her purse. You hurry inside, grab it, then retreat. You pull the cash out of her wallet and give it to the pizza guy."
                $ mc.location.show_background()
                $ clear_scene()
                "Pizza Guy" "Thanks man, enjoy."
                $ aunt.apply_planned_outfit()
                $ aunt.draw_person()
                "You take the pizza into the kitchen. A couple of minutes later [aunt.title] comes out of the bathroom."
                aunt "I'm so sorry about that. I know it must be embarrassing to see your aunt naked."
                mc.name "It's fine. We're family, right? We're supposed to be comfortable with each other."
                aunt "I guess you're right. Anyway, let me have some of that pizza. I'm starving now too!"

        "You grab a slice and start to have some lunch with [aunt.possessive_title]. You make some small talk to pass the time."
        mc.name "So, this place is going to be really nice. The alimony must be pretty good!"
        aunt "Oh, not as good as I would have liked. Your uncle... he has some good lawyers."
        aunt "But don't worry. I've got a good bit saved up. And I'm going to be taking some refresher courses online to get my license back up to date!"
        "You continue eating your pizza. You realise you have no idea what [aunt.title] used to do for work."
        mc.name "Refresher course for what?"
        aunt "Oh! I thought you knew. Before your uncle and I got married, I used to be an accountant for the same place he worked out."
        aunt "We got drinks one night after work, and the rest kind of snowballed from there... when I got pregnant with [cousin.fname], I just never came back after maternity leave."
        mc.name "Wow, I had no idea."
        aunt "Yeah... I've let my CPA license expire, but I'm going to be taking an online class to get it current again. They say it only takes a week for the renewal!"
        mc.name "That's great. Seems like accounting is something you could do just about anywhere."
        "You enjoy your lunch together then get in [aunt.title]'s car and head home. With all of their stuff moved, [aunt.title] and [cousin.title] should be ready to move out."

    $ aunt.event_triggers_dict["moving_apartment"] += 1
    $ aunt.event_triggers_dict["day_of_last_move"] = day
    call advance_time() from _call_advance_time_16
    return

label aunt_intro_phase_final_label():
    #You have finished moving all of their stuff over so your aunt and cousin can move out of your house.
    $ mc.change_location(kitchen)
    "When you get up for breakfast you find [aunt.title] and [mom.title] in the kitchen, both awake earlier than normal."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(aunt, position = "sitting")
    $ scene_manager.add_actor(mom, position = "sitting")
    aunt "Good morning [aunt.mc_title]."
    "She smiles at you warmly and sips coffee from a mug. [mom.possessive_title!c] is drinking a cup of tea across the table from her."
    mc.name "Morning. You two are up early."
    aunt "All the paperwork for my new apartment has been finished, so [cousin.fname] and I will be moving out today."
    mom "We're just finishing our drinks, then they'll be heading out."
    if aunt.event_triggers_dict.get("moving_apartment", 0) == 0:
        #Did nothing
        aunt "I was going to wake you up before I left, of course. You've been so busy, I barely got a chance to see you."
        mom "You're welcome to come over and visit any time [aunt.title]. I'll make sure [mom.mc_title] takes a break to come visit his family."

    elif aunt.event_triggers_dict.get("moving_apartment") in (1, 2, 3):
        #Did some stuff
        aunt "I was going to wake you up before I left, of course. I want to say thank you again for helping us move our things over."
        $ scene_manager.update_actor(mom, emotion = "happy")
        $ mom.change_stats(happiness = 5, love = 2)
        mom "I'm glad you were able to find some time to help them out [mom.mc_title]. I'm proud of you."

    else:
        #Did everything
        aunt "I was going to wake you up before I left, of course. I needed to say thank you again for the huge amount of help you gave us."
        $ scene_manager.update_actor(mom, emotion = "happy")
        $ mom.change_stats(happiness = 8, love = 3)
        mom "[aunt.fname] has been telling me all morning how helpful you've been. I'm so proud of you [mom.mc_title]."
        $ scene_manager.update_actor(aunt, emotion = "happy")
        aunt "He was a godsend, he really was."

    aunt "Come on [aunt.mc_title], sit down and join us for a few minutes."
    "You join [aunt.possessive_title] and [mom.possessive_title] while they finish their drinks and chat with each other."
    "[aunt.title] certainly seems happier now than she did a few weeks ago when she arrived."
    $ scene_manager.clear_scene()
    $ mc.change_location(hall)
    $ scene_manager.add_actor(mom)
    $ scene_manager.add_actor(lily)
    $ scene_manager.add_actor(aunt)
    $ scene_manager.add_actor(cousin)
    "When her drink is done [aunt.title] collects [cousin.possessive_title] and heads to the door. [lily.title] joins you as you say goodbye."
    $ scene_manager.update_actor(aunt, emotion = "happy")
    aunt "Thank you all for giving us a place to go. You're welcome to visit us any time. Just drop by."
    "[cousin.title] looks at you and shakes her head from behind her mother."
    $ scene_manager.update_actor(mom, emotion = "happy")
    mom "And you two are always welcome here. Call if you need anything."
    aunt "I will. Thanks sis."
    $ scene_manager.update_actor(aunt, position = "kissing")
    $ scene_manager.update_actor(mom, position = "kissing")
    "[mom.possessive_title!c] and [aunt.possessive_title] hug each other and don't let go for a long while."
    $ scene_manager.update_actor(aunt, position = "walking_away")
    $ scene_manager.update_actor(mom, position = "walking_away")
    $ scene_manager.update_actor(cousin, position = "walking_away")
    "When the moment has passed [mom.title] walks them out to the driveway."
    $ scene_manager.remove_actor(aunt)
    $ scene_manager.remove_actor(cousin)
    $ scene_manager.remove_actor(mom)
    "Leaving you alone with [lily.possessive_title]."
    lily "I'm going to miss them. I think [cousin.fname] and I were really getting along."
    mc.name "Really?"
    lily "Yeah! She may not talk much but she's a great listener. I hope she stays in touch."
    $ scene_manager.clear_scene()
    "You shrug and head back to your room to get ready for the day."

    python:
        aunt_move_to_new_apartment()
        scene_manager = None
        mc.change_location(bedroom)
        aunt.story_event_log("obedience")
        aunt.story_event_log("love")
    return

label aunt_share_drink_intro_label(the_person):
    # On talk trigger after she has moved out and you visit her
    # She invites you over to share some drinks. You can come by in the evening and share a drink with her.
    the_person "[the_person.mc_title], I'm so happy to see you! Come here, give me a hug."
    "[the_person.possessive_title!c] gives you a tight hug."
    mc.name "It's good to see you too [the_person.title]."
    the_person "We really should get together more often. I miss seeing my cute little nephew!"
    the_person "Come by in the evening some time, you can join me for a glass of wine and we can chat."
    $ mc.change_locked_clarity(5)
    "She gives you a kiss on the cheek and smiles at you."
    $ the_person.change_happiness(1)
    the_person "Anyway, I'm sure you have other stuff you wanted to talk about!"
    $ the_person.event_triggers_dict["invited_for_drinks"] = True
    call talk_person(the_person) from _call_talk_person_6
    return

label aunt_share_drinks_label(the_person):
    # An action that is only enabled in the evening (maybe only friday nights? Only ad)
    # Aunt shares drinks with you and chats. At higher sluttiness she does things like model for you, talk about her sexual preferences, etc.
    mc.name "Do you feel like having a glass of wine and chatting? I'm sure we have a lot to catch up on."
    "[the_person.title] claps her hands together excitedly!"
    the_person "Yes! You go sit on the couch and I'll pour us both a glass."
    "You sit down in [the_person.possessive_title]'s tiny living room and wait. She shuffles around in the kitchen, then comes out with two glasses of red wine."
    the_person "There you go. Now you have to make sure that I just have one glass of this. I love it, but wine goes straight to my head."
    $ the_person.draw_person(position = "sitting")
    "She hands you a glass, sits down, and tilts her glass toward you. You clink them together."
    mc.name "Cheers!"
    the_person "Cheers!"
    "[the_person.possessive_title!c] takes a sip, then leans back on the couch. She crosses her legs and turns to you."
    the_person "So what's been going on with your life? It's been so long!"
    menu:
        "Talk about work":
            mc.name "Well, work's been keeping me busy lately..."
            "You talk to [the_person.possessive_title] about your work. She nods politely but doesn't understand most of it."
            $ the_person.change_obedience(1)
            the_person "It sounds like you're a very important person, doing some very important work. I'm proud of you [the_person.mc_title]."

        "Talk about girls":
            mc.name "Well, I've been trying to meet someone lately..."
            "You talk to [the_person.possessive_title] about your love life. She listens intently."
            $ the_person.change_slut(1, 40)
            the_person "I've always thought it's important to be adventurous. You might connect with someone you wouldn't expect."

        "Talk about her":
            mc.name "Oh, it's been pretty quiet lately. What about you? I know you've been through a lot."
            "You get [the_person.possessive_title] talking about herself. She tells you about her failed marriage."
            $ the_person.change_love(1)
            the_person "... and when I told him I knew he was plowing his secretary every day, he kicked us out."
            "She takes another sip from her wine."
            the_person "Whew. That felt good to talk about actually."

    "[the_person.title] finishes off the last of her wine."
    the_person "Well that was a lovely chat [the_person.mc_title]. I won't keep you here any longer."
    if the_person.progress.lust_step == 3 and not aunt_fucking_round_two_requirement():
        "Before you have a chance to offer her another glass, she adds on quickly."
        the_person "Go on now. I have to get up very early tomorrow, and I don't have time to do umm... anything."
        mc.name "[the_person.title]..."
        the_person "No buts. Go on now, I'll see you soon."
        "[the_person.possessive_title!c] quickly shows you to the door."
        $ clear_scene()
        "As you step out of her apartment, you realise she probably needs more time to process what happened between you two the other day."
        "You should give her a few more days before you try your luck with her again."
        call advance_time() from _call_advance_time_too_soon_aunt_01 #Drinking advances time
        return
    menu:
        "Convince her to have another glass":
            mc.name "It's really no trouble. I can go pour you another glass, if you'd like."
            if the_person.love >= 20: #Can be convinced
                the_person "Oh, I really shouldn't. It's getting a little late, you probably have important places to be..."
                mc.name "It's not late, and I don't have anywhere important to be. Come on, just relax and give me your glass."
                the_person "Okay, okay, you've twisted my arm. I'm not to blame for any of my actions beyond this point though!"
                "She hands you her glass and you head to the kitchen to uncork her bottle of wine."
                menu:
                    "Add a dose of serum to her wine" if mc.inventory.has_serum:
                        call give_serum(the_person) from _call_give_serum_13

                    "Add a dose of serum to her wine\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                        pass

                    "Leave her drink alone":
                        pass
                "You top up your own drink while you're in the kitchen and head back to [the_person.title]. You hand over her new drink and sit down."
                the_person "Now, where were we..."
                "You and [the_person.possessive_title] keep talking. After her first glass she seems more relaxed, and the second one is already having its effect."
                $ the_person.add_situational_slut("Drunk", 5, "More than a little tipsy.")
                if aunt_fucking_round_two_requirement():
                    call aunt_fucking_round_two_label(the_person) from call_aunt_round_two_talk_01
                elif the_person.sluttiness <= 40:
                    call aunt_share_drinks_talk(the_person) from _call_aunt_share_drinks_talk

                elif the_person.sluttiness <= 50:
                    call aunt_share_drinks_sex_talk(the_person) from _call_aunt_share_drinks_sex_talk

                elif the_person.sluttiness <= 60:
                    call aunt_share_drinks_outfit_opinions(the_person) from _call_aunt_share_drinks_outfit_opinions

                elif the_person.sluttiness <= 70:
                    call aunt_share_drinks_underwear_opinions(the_person) from _call_aunt_share_drinks_underwear_opinions

                elif the_person.sluttiness <= 80:
                    call aunt_share_drinks_stripping(the_person) from _call_aunt_share_drinks_stripping

                else:
                    call aunt_share_drinks_fool_around(the_person) from _call_aunt_share_drinks_fool_around

                $ the_person.apply_planned_outfit()
                $ the_person.clear_situational_slut("Drunk")

            else:
                the_person "Oh, I really shouldn't. Too much wine makes me go silly."
                $ the_person.draw_person()
                "[the_person.title] waits until you've finished your glass of wine, then escorts you to the door."
                mc.name "See you soon [the_person.title]."
                the_person "I hope so! See you around."
        "Say goodbye":
            "[the_person.title] waits until you've finished your glass of wine, then escorts you to the door."
            mc.name "See you soon [the_person.title]."
            the_person "I hope so! See you around."

    "It's late and you decide to head home."
    $ mc.change_location(bedroom)
    call advance_time() from _call_advance_time_17 #Drinking advances time
    return

label aunt_share_drinks_mid_entry_label(the_person):    #Use this to enter having drinks mid sessions
    "She hands you her glass and you head to the kitchen to uncork her bottle of wine."
    menu:
        "Add a dose of serum to her wine" if mc.inventory.has_serum:
            call give_serum(the_person) from _call_give_serum_mid_entry_aunt_serums

        "Add a dose of serum to her wine\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
            pass

        "Leave her drink alone":
            pass
    "You top up your own drink while you're in the kitchen and head back to [the_person.title]. You hand over her new drink and sit down."
    the_person "Now, where were we..."
    "You and [the_person.possessive_title] keep talking. After her first glass she seems more relaxed, and the second one is already having its effect."
    $ the_person.add_situational_slut("Drunk", 5, "More than a little tipsy.")
    if aunt_fucking_round_two_requirement():
        call aunt_fucking_round_two_label(the_person) from call_aunt_round_two_talk_012

    if the_person.sluttiness <= 40:
        call aunt_share_drinks_talk(the_person) from _call_aunt_share_drinks_talk2

    elif the_person.sluttiness <= 50:
        call aunt_share_drinks_sex_talk(the_person) from _call_aunt_share_drinks_sex_talk2

    elif the_person.sluttiness <= 60:
        call aunt_share_drinks_outfit_opinions(the_person) from _call_aunt_share_drinks_outfit_opinions2

    elif the_person.sluttiness <= 70:
        call aunt_share_drinks_underwear_opinions(the_person) from _call_aunt_share_drinks_underwear_opinions2

    elif the_person.sluttiness <= 80:
        call aunt_share_drinks_stripping(the_person) from _call_aunt_share_drinks_stripping2

    else:
        call aunt_share_drinks_fool_around(the_person) from _call_aunt_share_drinks_fool_around2

    $ the_person.apply_planned_outfit()
    $ the_person.clear_situational_slut("Drunk")
    return


label aunt_share_drinks_talk(the_person):
    # She talks about her ex and then falls asleep.
    "As [the_person.title] gets deeper into her drink she starts to rant about her now ex-husband."
    the_person "I don't even know what he saw in that little skank... You've never seen her, but she was this flat chested little thing."
    "She scoffs and takes another drink while you listen patiently."
    $ the_person.change_slut(2, 40)
    the_person "And youth isn't everything it's cracked up to be. It takes practice to get good at some things. I hope he enjoys shitty blowjobs. HA!"
    "[the_person.possessive_title!c] puts her feet up on the couch and yawns."
    the_person "Oh, this wine really has just knocked me out. I'm just going to... rest my eyes while we talk, okay?"
    "She closes her eyes and leans her head back on the arm rest. She manages a few minutes of mumbled conversation before falling asleep completely."
    menu:
        "Get her a blanket":
            "You go to [the_person.title]'s room and take the blanket off her bed."
            "You lay the blanket over [the_person.possessive_title]. She grabs onto it and rolls over, mumbling something you can't understand."
            $ the_person.change_love(2)
            "You take your wine glasses to the kitchen and leave them in the sink, then see yourself out."

        "Grope her tits":
            $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
            "Seizing the opportunity, you kneel down in front of [the_person.possessive_title]."
            if the_person.tits_available:
                "Her nicely shaped breasts are already there for the taking. You move slowly and cup them in your hands."
                $ mc.change_locked_clarity(15)
            else:
                "You move slowly and cup her nicely shaped breasts, feeling them through her [the_person.outfit.get_upper_top_layer.display_name]."
                $ mc.change_locked_clarity(10)
            $ play_moan_sound()
            the_person "Mmm..."
            "[the_person.possessive_title!c] moans softly and tilts her head to the side."
            $ the_person.change_slut(2, 50)
            "You fondle her big tits until she seems like she's starting to wake up. You sit back down on the couch and pretend like nothing happened."
            the_person "... Hmm? Oh, did I nod off there? I'm sorry [the_person.mc_title], I think I need to have a little nap."
            mc.name "No problem, I'll clean up our glasses and head out."
            "She rolls over on the couch and is asleep again before you're out the door."

        "Grope her pussy":
            $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
            "Seizing the opportunity, you kneel down in front of [the_person.possessive_title]."
            if the_person.vagina_available:
                "Her pussy is out on display for you, there for the taking. You move slowly and slide your hand along her inner thigh, working upward."
                $ mc.change_locked_clarity(15)
            else:
                "You move slowly, sliding your hand along her inner thigh and working upward."
                "When you reach her waist, you slide your hand inside her [the_person.outfit.get_lower_top_layer.display_name]."
                $ mc.change_locked_clarity(10)

            if mc.foreplay_sex_skill >= 3:
                $ play_moan_sound()
                the_person "Mmm..."
                "She moans softly when your fingers make first contact with her pussy. Her hips press up gently against your hand."
                $ the_person.change_slut(2, 50)
                "You run your index finger gently over her clit, gently caressing it while you listen to her moan."
                "When it starts to seem like she's waking up, you retreat to your seat on the couch."

            else:
                $ play_moan_sound()
                "She moans softly when you make first contact with her pussy. You start to move your hand around, feeling for her clit."
                $ the_person.change_slut(1, 40)
                "You're inexperienced and perhaps a little overeager. [the_person.title] starts to wake up and you make a hasty retreat to your spot on the couch."

            the_person "... Hmm? Oh, did I nod off there? I'm sorry [the_person.mc_title], I think I need to have a little nap."
            mc.name "No problem, I'll clean up our glasses and head out."
            "She rolls over on the couch and is asleep again before you're out the door."
    return

label aunt_share_drinks_sex_talk(the_person):
    # She talks to you about stuff she finds sexy. Reveal a sex opinion
    "[the_person.title] talks more about herself, and it seems like being a little drunk seems to have removed any inhibitions she might have had."
    $ her_opinion = the_person.get_random_opinion(include_known = False, include_sexy = True, include_normal = False)
    if her_opinion:
        $ the_person.discover_opinion(her_opinion)
        $ opinion_string = opinion_score_to_string(the_person.opinion(her_opinion))
        "Through her surprisingly erotic ramblings you discover that she [opinion_string] [her_opinion]."
    else:
        #We know everything.
        "You don't learn anything new, but hearing [the_person.possessive_title] talk this way is certainly eye-opening."

    "She finally blushes and looks away from you."
    $ the_person.change_slut(2, 50)
    the_person "Oh my god, what have I even been saying? It's this wine [the_person.mc_title], I told you it makes me do crazy things."
    the_person "Just... don't tell my sister that I told you any of that. You can keep a secret, right?"
    mc.name "Of course, it's just between us."
    $ mc.change_locked_clarity(10)
    the_person "That's a good boy. Now I think I should stop drinking this wine while I still can. It was nice talking, come by any time and we can do it again."
    "She walks you to the door and you say goodbye."
    return

label aunt_share_drinks_outfit_opinions(the_person):
    # She wants your opinion on some outfits
    the_person "So [the_person.mc_title], now that I'm back on the market I think I need your help with something."
    mc.name "With what?"
    the_person "I need to update my wardrobe. You know, make it a little more modern. You're a hip young guy, I'm sure you can tell me what men like to see."
    the_person "Would you help me? It'll just take a few minutes."
    mc.name "Of course. Come on, show me what you've got."
    "She smiles, drinks the last of her wine, and leads you into her bedroom."
    $ the_person.draw_person()
    $ mc.change_location(aunt_bedroom)
    the_person "Okay, so here's what I have to work with. Tell me what you think."
    "She opens her wardrobe and stands back, giving you room to look around."
    call outfit_master_manager(start_mannequin = the_person) from _call_outfit_master_manager_10
    if isinstance(_return, Outfit):
        $ created_outfit = _return
        "You pull out a few pieces of clothing and lay them out on [the_person.possessive_title]'s bed."
        $ the_person.draw_person()
        "She looks at the outfit you've laid out for her and seems to think for a second."
        if the_person.judge_outfit(created_outfit): #She likes it enough to try it on.
            if created_outfit.vagina_visible:
                the_person "Oh, wow. My pussy would just be out there, for everyone to see..."
                "She sounds more excited than worried."
            elif created_outfit.tits_visible:
                the_person "Oh, wow. If I wore that my tits would just be out there, for everyone to see..."
                "She sounds more excited than worried."
            elif not created_outfit.wearing_panties:
                the_person "Oh wow, you don't think I should wear any panties with it? I guess that's what girls are doing these days..."
            elif not created_outfit.wearing_bra:
                the_person "You don't think I'd need a bra? I don't want my girls bouncing around all the time. Or do I?"
            else:
                the_person "Oh, that looks so cute!"
            $ the_person.update_outfit_taboos()

            the_person "If I try it on will you tell me what you think?"
            mc.name "Go for it. I want to see what it looks like on you."
            "[the_person.possessive_title!c] starts to get undressed in front of you. She pauses after a second."
            the_person "I'll just be naked for a second. You don't mind, right?"
            mc.name "Of course not."
            $ the_person.change_slut(2, 50)
            the_person "I didn't think so. Just don't tell my sister."
            $ the_person.strip_full_outfit(strip_feet = True, strip_accessories = True)
            $ mc.change_locked_clarity(10)
            "Once she's stripped out of her clothing, [the_person.possessive_title] puts on the outfit you've made for her."
            $ the_person.apply_outfit(created_outfit, update_taboo = True, show_dress_sequence = True)
            $ mc.change_locked_clarity(10)

            if created_outfit.outfit_slut_score <= the_person.sluttiness-20:
                #She would like it normally and doesn't find it slutty.
                the_person "Well, this is cute, but I don't know if I'm going to be wowing any men in it."
                $ the_person.draw_person(position = "back_peek")
                the_person "I think it needs to be a little... more. Or less, if you know what I mean."

            else:
                #She only likes it because she's drunk.
                the_person "Well, it's certainly a lot bolder than I would normally wear. Is this the sort of thing men like?"
                $ the_person.draw_person(position = "back_peek")
                $ the_person.change_slut(2, 60)
                the_person "What about my ass? Does it look good?"

            menu:
                "Add it to her wardrobe":
                    mc.name "It looks really good on you. You should wear it more often."
                    the_person "You really think so? Okay then, that's why I wanted your opinion in the first place!"
                    $ the_person.change_obedience(2)
                    $ the_person.draw_person()
                    $ the_person.wardrobe.add_outfit(created_outfit)
                "Don't add it to her wardrobe":
                    mc.name "Now that I'm seeing it, I don't think it really suits you."
                    the_person "That's a shame. Well, that's why I wanted your opinion in the first place!"
                    $ the_person.change_obedience(1)
                    "[the_person.title] starts to get naked again to put on her old outfit."

                    $ the_person.strip_full_outfit(strip_feet = True, strip_accessories = True)

                    $ strip_choice = None
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person()
            the_person "This was really fun [the_person.mc_title], but I think that extra glass of wine is starting to get to me."
            "She yawns dramatically and lies down on her bed."
            $ the_person.change_happiness(2)
            the_person "I'm going to have a little nap, but we should do this again some time. You're so nice to have around."
            mc.name "I'll make sure to come by again. I'll see myself out."



        else: #It's too slutty even for her drunk state. She's bashful but doesn't try it on.

            the_person "Oh my god [the_person.mc_title], do you really think I could wear that?"
            $ the_person.change_slut(1, 60)
            if created_outfit.vagina_visible:
                the_person "My... pussy would just be out there for everyone to see!"
            elif created_outfit.tits_visible:
                the_person "I would just have my tits out for everyone!"
            elif not created_outfit.wearing_panties:
                the_person "It doesn't even have any panties for me!"
            elif not created_outfit.wearing_bra:
                the_person "It doesn't even have a bra for me!"
            mc.name "I think it would be a good look for you. You should try it on."
            "[the_person.possessive_title!c] blushes and shakes her head."
            the_person "I don't think I can... Maybe that extra glass of wine wasn't such a good idea [the_person.mc_title], it's gone straight to my head."
            "She sits down on her bed and sighs."
            the_person "I think I just need to have a rest. You can help me out with this some other day, okay?"
            "[the_person.title] lies down and seems to be drifting off to sleep almost instantly. You say goodbye and head to the door."
        $ created_outfit = None

    else:
        mc.name "Sorry [the_person.title], I don't have any ideas right now."
        $ the_person.change_happiness(-2)
        $ the_person.draw_person(position = "missionary", emotion="sad")
        "[the_person.possessive_title!c] sighs dramatically and collapses onto her bed."
        the_person "Am I really that out of touch? I'll have to go shopping and update everything then."
        the_person "Maybe I just need to lie down, this wine is really getting to me."
        "[the_person.title] seems to be drifting off to sleep already. You say goodbye and head to the door."
    $ clear_scene()
    return

label aunt_share_drinks_underwear_opinions(the_person):
    # She wants your opinion about some underwear
    the_person "So [the_person.mc_title], since you're here I could use some help with something. It's a little... delicate."
    mc.name "What do you need?"
    the_person "Well, I want to put myself out there and meet someone, but I haven't done that since [cousin.fname] was born."
    the_person "I've got plenty of lingerie, but I need to know what looks good on me. Can I trust you to give me an honest opinion?"
    mc.name "Of course, I'll tell you exactly what I think."
    "She smiles, drinks the last of her wine, and leads you into her bedroom."
    $ the_person.draw_person()
    $ mc.change_location(aunt_bedroom)
    the_person "Okay, so I have a few things I want your opinion on. You just tell me what looks good and what I should keep around."
    "She starts to strip down, then pauses and looks at you."
    $ mc.change_locked_clarity(10)
    the_person "Don't tell my sister I'm doing this with you. We're both adults, but I don't think she'd understand."
    "She rolls her eyes and keeps going."
    $ the_person.change_slut(1, 60)

    # first time strip (fast - no dialogues)
    $ the_person.strip_outfit(exclude_feet = False)

    the_person "Okay, first one."
    "She slips on her new set of underwear."
    $ lingerie = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under", sluttiness_limit = the_person.sluttiness - 20)
    $ the_person.apply_outfit(lingerie, update_taboo = True, show_dress_sequence = True)
    $ mc.change_locked_clarity(10)
    the_person "Okay, what do you think? Keep or toss?"
    $ the_person.draw_person(position="back_peek")
    menu:
        "Add it to her wardrobe":
            mc.name "Keep, definitely."
            $ the_person.draw_person()
            the_person "Okay, keep it is! Let's see what's up next..."
            $ the_person.wardrobe.add_underwear_set(lingerie)
        "Don't add it to her wardrobe":
            mc.name "Toss, I think you can do better."
            $ the_person.draw_person()
            the_person "I think so too. Let's see what's up next..."

    $ the_person.change_slut(1, 60)
    $ the_person.strip_full_outfit(strip_feet = True, strip_accessories = True)

    "She slips on the next set of lingerie."
    $ lingerie = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under", sluttiness_limit = the_person.sluttiness - 10, allow_skimpy = True)
    $ the_person.apply_outfit(lingerie, update_taboo = True, show_dress_sequence = True)
    $ mc.change_locked_clarity(10)
    the_person "What about this one? Keep or toss?"
    $ the_person.draw_person(position="back_peek")
    menu:
        "Add it to her wardrobe":
            mc.name "Keep."
            $ the_person.draw_person()
            the_person "We've got a winner! Okay, one more..."
            $ the_person.wardrobe.add_underwear_set(lingerie)
        "Don't add it to her wardrobe":
            mc.name "Toss."
            $ the_person.draw_person()
            the_person "Tough customer. Okay, one more..."

    $ the_person.change_slut(1, 60)
    $ the_person.strip_full_outfit(strip_feet = True, strip_accessories = True)

    "She slips on the last set of underwear she has to show you."
    $ lingerie = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under", sluttiness_limit = the_person.sluttiness, swap_bottoms = True, allow_skimpy = True)
    $ the_person.apply_outfit(lingerie, update_taboo = True, show_dress_sequence = True)
    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position="back_peek")
    the_person "Well?"
    menu:
        "Add it to her wardrobe":
            mc.name "Keep it."
            $ the_person.draw_person()
            the_person "I thought you'd like this one. Okay, I'll hold onto it!"
            $ the_person.wardrobe.add_underwear_set(lingerie)
        "Don't add it to her wardrobe":
            mc.name "Toss it, you've got nicer stuff you could wear."
            $ the_person.draw_person()
            the_person "Yeah, I think you're right. Let's get this off then!"
            $ the_person.strip_full_outfit(strip_feet = True, strip_accessories = True)

    $ the_person.change_love(2)
    $ the_person.change_slut(2, 65)
    the_person "Thank you for helping me [the_person.mc_title]. Now I think I need to lie down, because that wine is going right to my head."
    "She yawns dramatically and falls back onto her bed, arms spread wide."
    the_person "Stop by again sometime soon though, we can do this again."
    mc.name "Sure thing [the_person.title], I'll be by again soon."

    $ clear_scene()
    $ lingerie = None
    return

label aunt_share_drinks_stripping(the_person):
    # She wants to strip for you.
    the_person "[the_person.mc_title], does it feel warm in here or is it just me?"
    "[the_person.title] takes a sip from her glass of wine and stands up."
    if the_person.outfit.remove_random_any(exclude_feet = True, do_not_remove = True):
        the_person "You don't mind if I get a little more comfortable, do you?"
        $ strip_choice = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
        if strip_choice:
            $ the_person.draw_animated_removal(strip_choice)
            $ mc.change_locked_clarity(10)
            "Before you can answer she peels off her [strip_choice.name] and drops it onto the couch."
            mc.name "No, go right ahead."
        if the_person.outfit.remove_random_lower(do_not_remove = True):
            $ strip_choice = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
            if not strip_choice is None:
                $ the_person.draw_animated_removal(strip_choice)
                $ mc.change_locked_clarity(5)
                "She takes off her [strip_choice.name] next and throws it onto the couch too."
    the_person "[the_person.mc_title], can I ask you a question? Do you think I'm still attractive?"
    $ the_person.draw_person(position = "back_peek")
    $ mc.change_locked_clarity(10)
    "She spins around in front of you, showing you her butt."
    the_person "I mean, would you be attracted to me if I wasn't your aunt?"
    menu:
        "Encourage her" if the_person.outfit.remove_random_any(exclude_feet = True, do_not_remove = True):
            mc.name "Keep taking your clothes off and maybe I'll tell you."
            $ the_person.change_stats(obedience = 1, slut = 2, max_slut = 70)
            the_person "Oh? Okay then, I'll play your game, you dirty boy."
            $ strip_choice = the_person.outfit.remove_random_any(exclude_feet = True, do_not_remove = True)
            $ the_person.draw_animated_removal(strip_choice, position = "back_peek")
            $ mc.change_locked_clarity(10)
            "She keeps her back to you and takes off her [strip_choice.name]."
            the_person "Do you like watching me strip down for you? Do you think I'm hot?"
            mc.name "Yeah, I think you're hot."
            the_person "Oh [the_person.mc_title], that's so nice to hear. I just want to be wanted. Even if it's only by you..."
            $ the_person.draw_person()
            the_person "We should keep this our little secret, okay?"

        "Compliment her":
            mc.name "Of course you're attractive [the_person.title], look at you! You've got a hot ass and a killer rack."
            the_person "Oh [the_person.mc_title], you know just what I wanted to hear..."
            $ mc.change_locked_clarity(5)
            "She wiggles her ass just for you."
            the_person "You don't think I'm too old? I feel like I'm past my prime."
            mc.name "You're beautiful, you have an amazing body, and you have the experience to know what to do with it."
            $ the_person.change_stats(happiness = 5, love = 1, slut = 2, max_slut = 70)
            $ the_person.draw_person()
            if the_person.tits_available:
                $ mc.change_locked_clarity(10)
                "She turns back around and leans over to give you a hug on the couch. Her tits dangle down in front of you, tempting you."
            else:
                "She turns back around and leans over to give you a hug on the couch."
            the_person "It's been so long since I felt wanted... I think I just needed to feel like I was, even if it's only by you..."

        "Insult her":
            mc.name "Attractive? Sure, but you've got to accept you're past your prime."
            $ the_person.change_happiness(-5)
            the_person "What?"
            mc.name "You're getting older [the_person.title], you just can't compete with all the younger women out there."
            $ the_person.draw_person(emotion="angry")
            "She turns back and crosses her arms."
            the_person "You're telling me these aren't some nice tits?"
            mc.name "Maybe, but you have to do more than just tease. If you want to impress someone get them wrapped around their cock."
            mc.name "You've got experience, but you need to put it to work."
            $ the_person.change_stats(obedience = 2, slut = 2, max_slut = 80)
            $ mc.change_locked_clarity(10)
            "She seems to think long and hard about this for a few seconds."
            the_person "I guess I understand. Thank you for being honest with me."

    $ strip_choice = None
    $ the_person.draw_person(position="sitting")
    "She sits down on the couch again and sighs."
    the_person "I'm sorry but that extra glass of wine is just knocking me out. I think I'm going to lie down for a bit."
    the_person "Do you want to come by another day and do this again?"
    mc.name "I'd love to."
    "You take your wine glasses to the kitchen for [the_person.title] and say goodbye."
    return

label aunt_share_drinks_fool_around(the_person):
    "[the_person.possessive_title!c] slides closer to you on the couch and places her hand on your thigh while you chat."
    $ mc.change_locked_clarity(10)
    "Inch by inch it moves up your leg until it brushes against the tip of your soft cock. She rubs it gently through your pants, coaxing it to life."
    the_person "I... I know we shouldn't, but nobody needs to know. Right?"
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        the_person "We won't take it too far, I just really need this..."
    menu:
        "Fool around":
            call fuck_person(the_person) from _call_fuck_person_22
            $ the_report = _return
            $ the_person.draw_person(position = "missionary")
            "[the_person.possessive_title!c] lies down on the couch when you're finished."
            if the_report.get("girl orgasms",0) > 0 and the_report.get("guy orgasms", 0) > 0:
                the_person "That was great [the_person.mc_title], I feel like I'm floating."
                "She looks up at you and giggles."
                $ the_person.change_happiness(5)
                the_person "And making you cum felt so good, I've still got it! I'm not too old yet! Haha..."
                "She puts her head down and sighs happily."

            elif the_report.get("girl orgasms",0) > 0:
                the_person "Oh wow, you really know what you're doing [the_person.mc_title], I feel like I'm floating."
                "She looks up at you and giggles."
                the_person "Next time I'm going to make you cum too, I want to show you that I've still got it!"
                mc.name "So there's going to be a next time?"
                the_person "I hope so! That was everything I needed."
                "She puts her head down and sighs happily."

            elif the_report.get("guy orgasms", 0) > 0:
                $ the_person.change_happiness(5)
                the_person "Ah... It's good to know I can still make a young man cum his brains out."
                "She looks up at you and giggles."
                the_person "Maybe next time I can give you some pointers on what girls like. Teach you something to impress a girlfriend."
                mc.name "So there's going to be a next time?"
                the_person "If you want there to be. I have years of experience I need to pass on to the next generation."
                "She puts her head down and sighs happily."

            else:
                the_person "We should, uh... It's probably a good idea we stop. I think I've had too much wine, I'm not thinking straight."
                "She looks up at you and smiles."
                the_person "But that was all very flattering. I'm sorry if I made you uncomfortable..."
                mc.name "No, I was having a good time too."
                the_person "It's kind of nice, still being wanted like that... Even if we shouldn't be doing this..."
                "She puts her head back down and sighs."
            "You move to the bathroom to get yourself cleaned up, and when you come back [the_person.title] is fast asleep."
        "Turn her down":
            mc.name "I don't think that's a good idea right now [the_person.title]. You're in no state to make that kind of decision."
            "You gently take her hand off you. She seems to snap to her senses and looks away."
            the_person "Right, of course. I didn't mean... I didn't mean anything, okay?"
            $ the_person.change_stats(obedience = 1, love = 1)
            the_person "Maybe you should go, I'm clearly not thinking straight with all this wine."
            mc.name "That may be for the best. Maybe we can do this again some other time though."
            "You take the glasses of wine to the kitchen for [the_person.possessive_title] and say goodbye."
    return

label family_games_night_intro(the_person): # Triggered as an on-talk event in her apartment.
    #Aunt introduces the family games night. she's already talked to your mother and it's planned for [some evening].
    # you're not required to go, but you're always welcome!
    $ the_person.draw_person()
    "You knock on the door of [the_person.possessive_title]'s apartment. After a brief pause she opens the door while talking to someone on her cell phone."
    the_person "... Well speak of the devil, he's just come by for a visit."
    "She gives you a smile and waves you into the living room, closing the door behind you."
    the_person "Oh no, he's no trouble... No, I don't mind at all... Don't worry, he's a wonderful kid."
    "You sit down on the couch and relax while she finishes her phone call."
    the_person "Yeah... I'll tell him. Talk to you soon. Love you sis."
    "[the_person.title] makes a dramatic kissing noise before hanging up and turning her attention to you."
    the_person "Hi [the_person.mc_title], I'm glad you've stopped by."
    $ the_person.draw_person(position = "sitting")
    "She gives you a kiss on the forehead and sits down on the couch next to you."
    mc.name "It's good to see you [the_person.fname]. Did you need to tell me something?"
    the_person "That was your mom. We want to spend more time together as a family, so she invited me to spend Wednesday evenings with her."
    the_person "We'll probably have some drinks, chat about what we've been doing, maybe play some cards."
    the_person "If you don't have anything better to do than hang out with a couple of old women you're welcome to join us."
    menu:
        "Promise to join":
            mc.name "I'd love to spend time with both of you. I'll do my best to make it."
            the_person "I'm looking forward to it even more now!"

        "You'll think about it":
            mc.name "It sounds like fun, but I'm not sure if I'll be free."
            the_person "I understand, you're a busy boy."

    $ init_family_games_night()
    $ clear_scene()
    return

label family_games_night_setup(): # Triggered as a mandatory crisis right before the games night
    $ setup_family_game_night()
    return

label family_games_night_start(the_aunt, the_mom): # Triggered as an on enter event
    # Girls ask if you want to have some drinks, and then play cards some cards.
    # Ensure neither of them have shown up with outfits too slutty for the other to consider appropriate.
    $ lowest_slut = builtins.min(the_aunt.effective_sluttiness(), the_mom.effective_sluttiness())
    $ the_aunt.current_planned_outfit = the_aunt.get_random_appropriate_outfit(sluttiness_limit = lowest_slut, guarantee_output = True)
    $ the_mom.current_planned_outfit = the_mom.get_random_appropriate_outfit(sluttiness_limit = lowest_slut, guarantee_output = True)

    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_aunt, the_aunt.current_planned_outfit, position = "sitting")
    $ scene_manager.add_actor(the_mom, the_mom.current_planned_outfit, position = "sitting")

    "[the_mom.title] and [the_aunt.title] are sitting on the couch, chatting happily to each other when you enter the living room."
    if mc.business.event_triggers_dict.get("family_games_cards",0) == 0:
        the_mom "Welcome home [the_mom.mc_title]. [the_aunt.fname] is here to visit for the evening."
        $ scene_manager.update_actor(the_aunt, emotion = "happy")
        the_aunt "Hi [the_aunt.mc_title]. We were just about to have some drinks, do you want to join us?"
    else:
        the_mom "Welcome home [the_mom.mc_title]. [the_aunt.fname] is over to play some cards this evening."
        $ scene_manager.update_actor(the_aunt, emotion = "happy")
        the_aunt "Hi [the_aunt.mc_title]. We're having some drinks first, do you want to join us?"

    menu:
        "Join them":
            call family_games_night_drinks(the_mom, the_aunt) from _call_family_games_night_drinks
            $ mc.business.event_triggers_dict["family_games_drink"] += 1

        "Say you're busy":
            mc.name "Sorry, but I'll have to take a rain check tonight. Maybe next time."
            the_mom "Have a good evening sweetheart. We'll try not to make too much noise."
            the_aunt "No promises, my sister gets pretty rowdy once she has a couple of glasses of wine in her."
            the_mom "Hey!"
            "She slaps her sister playfully on the shoulder."
            the_mom "Just for that you're going to have to go pour the drinks! Go on, get!"
            "You leave the girls in the living room as they drink and gossip."



    # Otherwise they just ask you to go get your sister, it's becoming a routine.
    # Opportunity to drop out early here if all you wanted to do was dose them.
    $ scene_manager.clear_scene()
    $ scene_manager = None
    return

label family_games_night_drinks(the_mom, the_aunt): #Breakout function for the drink serving section to keep things organized.
    mc.name "I'd love to. What are you drinking?"
    the_aunt "I brought over a bottle of wine for us. It's in the kitchen, would you mind pouring us some?"
    the_mom "I can take care of that [the_aunt.fname], [mc.name] is probably tired and just wants to relax."
    the_aunt "He's getting free drinks. He should be pampering us like the refined wine moms we are."
    menu: #TODO: Have an option for Aunt at high obedience where you command her to do it for you.
        "Pour the drinks yourself":
            mc.name "Don't worry about it mom, I'll be back with drinks in a moment."
            the_mom "You're so sweet. Thank you."
            $ scene_manager.hide_actors()
            $ kitchen.show_background()
            "You find the bottle of wine easily in the kitchen and pour three glasses."
            menu:
                "Add a dose of serum to [the_mom.title]'s wine" if mc.inventory.has_serum:
                    call give_serum(the_mom) from _call_give_serum_29
                    if _return:
                        "You add a dose of serum into [the_mom.title]'s wine and swirl the glass, mixing it in thoroughly."
                    else:
                        "You reconsider, and decide not to add anything to [the_mom.title]'s drink."

                "Add a dose of serum to [the_mom.title]'s wine\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                    pass

                "Leave her drink alone":
                    pass

            menu:
                "Add a dose of serum to [the_aunt.title]'s wine" if mc.inventory.has_serum:
                    call give_serum(the_aunt) from _call_give_serum_30
                    if _return:
                        "You add a dose of serum into [the_aunt.title]'s wine and swirl the glass, mixing it in thoroughly."
                    else:
                        "You reconsider, and decide not to add anything to [the_aunt.title]'s drink."

                "Add a dose of serum to [the_aunt.title]'s wine\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                    pass

                "Leave her drink alone":
                    pass

            $ hall.show_background()
            $ scene_manager.show_all_actors()
            "You return to the living room and hand [the_mom.possessive_title] and [the_aunt.possessive_title] their drinks and sit back down beside them."

        "Let [mom.title] pour the drinks":
            mc.name "You're right mom, I could really use a break."
            $ scene_manager.update_actor(the_mom, position = "default", emotion = "happy")
            "[the_mom.possessive_title!c] stands up and motions to the couch as she walks towards the kitchen."
            the_mom "You sit down, I'll be back in a moment with drinks for everyone."
            $ the_mom.change_obedience(1)
            $ scene_manager.update_actor(the_mom, position = "walking_away")
            "As [the_mom.possessive_title] leaves her sister turns to you and shakes her head."
            $ scene_manager.hide_actor(the_mom)
            the_aunt "Are you this popular with all the ladies? You have my big sis falling over herself to serve you."
            mc.name "I try to be. I'm lucky to have such an amazing mother."
            the_aunt "You really are, and don't you forget it."
            $ scene_manager.show_actor(the_mom, position = "default")
            "[the_mom.possessive_title!c] comes back into the living room, three glasses of wine balanced between both hands."
            $ scene_manager.update_actor(the_mom, position = "sitting")
            "She hands out the drinks, then sits back down beside her sister."

    $ the_mom.change_happiness(5)
    the_mom "This is nice, you two. I'm glad we're able to get together like this."
    "[the_mom.possessive_title!c] and [the_aunt.possessive_title] chat about their week, happily trading stories and opinions."
    "You sip at your own glass of wine, content to just listen."
    "After half an hour of drinking and gossip [the_mom.possessive_title] puts her finished glass aside."
    if mc.business.event_triggers_dict.get("family_games_cards",0) == 0:
        the_mom "Would you two like to play something while we drink? I have a pack of cards in the kitchen."
        the_aunt "Oh my god, we used to play cards every night after school. Do you play cards often [the_aunt.mc_title]?"
        mc.name "Not very often."
        the_aunt "Well I'm sure you'll catch on quickly. Do you want to try?"

    else:
        the_mom "We should decide now if we want to play any cards tonight. If I have another glass of wine I'll be hopeless."
        the_aunt "Cards sound like a lot of fun. What do you think [mc.name]?"

    menu:
        "Play cards {image=time_advance}":
            if mc.business.event_triggers_dict.get("family_games_cards",0) == 0:
                mc.name "Cards sound like fun, but you'll have to teach me how to play."
                the_aunt "First we'll need a fourth player, so we can split up into teams."
                the_mom "[the_mom.mc_title], go see if your sister wants to come and play. We'll set up in the kitchen."

            else:
                mc.name "I'm up for some cards. I'll go see if Lily wants to join."
                the_aunt "Okay, we'll go and set up in the kitchen."

            $ scene_manager.hide_actors()
            if lily in lily_bedroom.people:
                "You knock on [lily.possessive_title]'s bedroom door."
                $ lily_bedroom.show_background()
                $ lily.current_planned_outfit = lily.get_random_appropriate_outfit(sluttiness_limit = lowest_slut, guarantee_output = True)
                lily "It's open!"
                $ scene_manager.add_actor(lily, lily.current_planned_outfit, position = "sitting")
                lily "What's up [lily.mc_title]?"
                if mc.business.event_triggers_dict.get("family_games_cards",0) == 0:
                    mc.name "[the_mom.fname] and [the_aunt.fname] want to play some cards, and we need a fourth player."
                    mc.name "Do you want to come and play?"
                    "She sighs and rolls her eyes."
                    lily "Cards? Like poker?"
                    mc.name "I don't think so. It's some game they played back when they were kids."
                    lily "We need to tell them that nobody plays with cards any more."
                    mc.name "They're having a good time together, let's just humour them, okay?"
                    lily "Fine, I wasn't doing anything tonight anyways."
                else:
                    mc.name "[the_mom.fname] and [the_aunt.fname] want to play cards again. Do you want to be our fourth player?"
                    lily "Sure, I guess I'm not doing anything else."
                    "She sighs."
                    lily "How sad is that? The most exciting thing I have to be doing is playing cards with my [the_mom.fname]?"
                    mc.name "I'm sure we can figure out how to make it more exciting."
                    #TODO: This is where you can ask her to take a dive for you.

                call family_games_night_cards(the_mom, the_aunt, lily) from _call_family_games_night_cards
                $ mc.business.event_triggers_dict["family_games_cards"] += 1
                call advance_time() from _call_advance_time_30

            else:
                "You knock on [lily.possessive_title]'s bedroom door. After you get no response you open it and peek inside."
                $ lily_bedroom.show_background()
                "The room is empty."
                $ kitchen.show_background()
                $ scene_manager.show_all_actors()
                "You head back to the kitchen, where [the_mom.possessive_title] and [the_aunt.possessive_title] are sorting a deck of cards."
                mc.name "Bad news. It looks like Lily is out for the night."
                the_mom "Oh, that's too bad."
                $ scene_manager.update_actor(the_aunt, position = "default")
                the_aunt "I think I'll just have another glass of wine then, if you don't mind [the_mom.fname]."
                the_aunt "We can play cards next time I'm over."
                $ scene_manager.update_actor(the_mom, position = "default")
                the_mom "Pour me one as well, I think I'm going to join you."

                $ scene_manager.hide_actors()
                "The sisters return to the living room and relax on the couch together."
                #TODO: Add a mom and aunt event specifically if Lily is busy (or she doesn't want to play/you don't invite her.)


        "Call it a night":
            mc.name "I'm going to have to pass this time, I have some business to attend to."
            the_aunt "Then the drinking will continue! Pour me another glass sis!"
            "You finish your own glass of wine and leave the girls in the living room to chat with each other."



    # Get Lily and bring her back, gather around the kitchen table to play.
    return

label family_games_night_cards(the_mom, the_aunt, the_sister): #Breakout function for the card game to keep things organized (and support adding new variants later)

    $ scene_manager.show_all_actors()
    $ scene_manager.update_actor(the_sister, position = "default")
    $ kitchen.show_background()
    "You bring [lily.title] back to the kitchen, where you find [the_mom.possessive_title] and [the_aunt.possessive_title] sorting a deck of cards."
    the_mom "And now the gang's all together! Pull up a chair, we've got the deck sorted out."
    $ scene_manager.update_actor(the_sister, position = "sitting")
    "You sit down around the table while [the_mom.possessive_title] shuffles the deck."
    $ partner = None

    if mc.business.event_triggers_dict.get("family_games_cards",0) == 0:
        the_mom "Alright, so have either of you two ever played euchre?"
        "[the_sister.title] shakes her head."
        the_mom "It's a card game that was popular back when me and my sister were in school."
        the_mom "You play it with a partner, and the goal is to win as many hands as possible."
        the_mom "The trick is that you don't know what cards your partner has, so..."
        "You listen as [the_mom.possessive_title] explains the rules of the game."
        if mc.int <= 2:
            "You do your best to follow along, but you don't think you've fully grasped the concept."
        else:
            "When she's finished you think you have a solid understanding of how to play."

        the_mom "Now normally we would pick our partners first, but it wouldn't be very fair to put the two new players on the same team."
        the_mom "So let's split up. [the_sister.fname], you can be my partner."
        the_aunt "And I'll team up with you, [the_aunt.mc_title]."
        $ partner = the_aunt

        the_mom "Well, is everyone ready?"
        the_aunt "Wait, what are we playing for?"
        the_mom "It's just supposed to be a friendly game. We don't need to play for anything."
        the_aunt "Come on, we used to play for cash all the time. Let's make it interesting."
        the_mom "[the_mom.mc_title], [the_sister.fname], what do you want to do?"
    else:
        the_mom "Okay then, we need to pick teams. [the_mom.mc_title], you can pick first."
        call screen main_choice_display(build_menu_items([["Play with", the_mom, the_aunt, the_sister]], draw_hearts_for_people = True))
        $ partner = _return
        "You pick [partner.title] and move seats so you are sitting across from each other."
        if partner == the_mom:
            partner "Good choice, we work so well together."
        elif partner == the_aunt:
            partner "Your son knows how to pick the winning team sis."
            "She gives you a friendly wink."
        else: # the_sister
            partner "Okay, let's give it our best shot I guess..."
            the_aunt "Age versus experience, let's see how well you two have learned!"
            the_mom "Don't worry you two, we'll go easy on you."

        the_aunt "So, what are we playing for tonight? Any suggestions?"



    menu:
        "Play for fun":
            # standard, always enabled
            if mc.business.event_triggers_dict.get("family_games_fun", 0) == 0:
                mc.name "Let's just play for fun. I could use some more practice before I put anything more on the line."
            else:
                mc.name "Let's just play for fun, I don't want to put anything more on the line."
            the_mom "That's a very responsible decision [the_mom.mc_title]."
            call family_games_night_fun(the_mom, the_aunt, the_sister, partner) from _call_family_games_night_fun
            $ mc.business.event_triggers_dict["family_games_fun"] += 1

        "Play for cash" if mc.business.event_triggers_dict.get("family_games_fun", 0) != 0 and the_mom.love >= 30 and the_aunt.love >= 30 and the_sister.love >= 30:
            if mc.business.event_triggers_dict.get("family_games_cash", 0) == 0:
                mc.name "Let's make it interesting and play for a little bit of cash."
                the_aunt "Sounds like fun!"
            else:
                mc.name "Let's play for some cash again. It made the game a lot more interesting."
                "[the_aunt.possessive_title!c] smiles happily."

            call family_games_night_cash(the_mom, the_aunt, the_sister, partner) from _call_family_games_night_cash
            $ mc.business.event_triggers_dict["family_games_cash"] += 1

        "Play for cash\n{menu_red}Requires: 30 Love, All{/menu_red} (disabled)" if mc.business.event_triggers_dict.get("family_games_fun", 0) != 0 and the_mom.love < 30 or the_aunt.love < 30 or the_sister.love < 30:
            pass


        "Play strip euchre" if mc.business.event_triggers_dict.get("family_games_cash", 0) != 0 and the_mom.sluttiness >= 30 and the_sister.sluttiness >= 30 and the_aunt.sluttiness >= 30:
            if mc.business.event_triggers_dict.get("family_games_strip", 0) == 0:
                mc.name "I know something that will make the game very interesting."
                mc.name "Mom, aunt, have you two ever played strip poker?"
                "[the_mom.possessive_title!c] gasps quietly and shakes her head."
                the_mom "[the_mom.mc_title], I would never..."
                "She's interrupted by her sister."
                $ mc.change_locked_clarity(5)
                the_aunt "Yeah, I have."
                "[the_mom.title] turns to [the_aunt.possessive_title], looking surprised."
                the_mom "You have? When?"
                "[the_aunt.title] giggles and shrugs."
                the_aunt "A bunch of times in university. It's a fun party game."
                the_mom "I... Really? I can't believe my own little sister was getting into so much mischief and I never knew!"
                "[the_aunt.title] shrugs again."
                the_aunt "Come on, it sounds like it could be fun. Let's give it a try."
                the_mom "No, I couldn't... I mean, I don't want to have to... strip in front of all of you."
                "You sit back, happy to let [the_aunt.possessive_title] do the convincing for you."
                the_aunt "That's why you try and win! Don't be such a stick in the mud, it'll be fun!"
                "[the_mom.possessive_title!c] considers it for a long moment, then sighs and shrugs."
                $ mc.change_locked_clarity(10)
                the_mom "Fine, but I don't want anyone taking this further than they're comfortable with. Okay?"
                the_aunt "Of course. Okay, let's play!"
            else:
                mc.name "Let's play strip euchre again, that was interesting last time."
                if mc.business.event_triggers_dict.get("family_games_dance", 0) > 0 and the_mom.sluttiness >= 40 and the_sister.sluttiness >= 40 and the_aunt.sluttiness >= 40:
                    mc.name "And winners get to watch while the losers dance for them."
                    $ mc.change_locked_clarity(15)
                    the_aunt "Alright, strip euchre with benefits it is. Let's play!"
                else:
                    $ mc.change_locked_clarity(5)
                    the_aunt "Alright, strip euchre it is. Let's play!"

            call family_games_night_strip(the_mom, the_aunt, the_sister, partner) from _call_family_games_night_strip
            $ mc.business.event_triggers_dict["family_games_strip"] += 1

        "Play strip euchre\n{menu_red}Requires: 30 Sluttiness, All{/menu_red} (disabled)" if mc.business.event_triggers_dict.get("family_games_cash", 0) != 0 and the_mom.sluttiness < 30 or the_sister.sluttiness < 30 or the_aunt.sluttiness < 30:
            pass

        #TODO: Figure out if we want an even higher tier (Maybe not yet, since we've avoided most inter-family stuff.
        # |-> Maybe if a girl strips completely you can add an extra requirement.


    if mc.business.event_triggers_dict.get("family_games_cards", 0) == 0:
        the_mom "This was a lot of fun [the_aunt.fname]. Should we do it again next week?"
        the_aunt "That sounds great. I'll bring the wine again."
    else:
        the_mom "Okay, I'll walk you to the door. This was a lot of fun, as always."
        the_aunt "Same time next week?"
        the_mom "As long as you bring the wine!"

    $ scene_manager.update_actor(the_mom, position = "walking_away")
    $ scene_manager.update_actor(the_aunt, position = "walking_away")
    $ scene_manager.update_actor(the_sister, position = "default")
    "[the_mom.possessive_title!c] walks [the_aunt.possessive_title] to the door while you and [the_sister.title] clean up the kitchen."
    $ scene_manager.hide_actors([the_mom, the_aunt])
    "It's already late, so when you're finished you go back to your room and go to bed."
    $ scene_manager.hide_actor(the_sister)
    python:
        partner = None
        mc.change_location(bedroom)

    if aunt_card_game_aftermath_requirement():
        call aunt_card_game_aftermath_label from _aunt_post_game_fun_intro_01
        #Do we want a recurring version of this for Rebecca only before we also bring Jennifer into these sessions?
    return

label family_games_night_fun(the_mom, the_aunt, the_sister, partner):
    python:
        # Describes a game where you're playing for fun.
        still_playing = True
        round_count = 1
        max_rounds = 5

        opponent_a, opponent_b, win_chance = family_game_night_get_opponents_with_info([the_mom, the_aunt, the_sister], partner)

    while still_playing:
        call card_round_description(the_mom, the_aunt, the_sister, partner, round_count) from _call_card_round_description
        if _return:
            # if partner == the_mom:
            #     pass #TODO
            # elif partner == the_aunt:
            #     pass #TODO: Unique dialogue
            # else: the_sister
            #     pass #Dialogue
            $ scene_manager.update_actor(partner, emotion = "happy")
            $ partner.change_happiness(2)
            partner "Nice! Good play [partner.mc_title]."

            $ scene_manager.update_actor(opponent_a, emotion = "sad")
            opponent_a "Gah, I thought we had that one..."


        else:

            # if partner == the_mom:
            #     pass #TODO
            # elif partner == the_aunt:
            #     pass #TODO: Unique dialogue
            # else: the_sister
            #     pass #Dialogue
            $ scene_manager.update_actor(opponent_b, emotion = "happy")
            $ opponent_a.change_happiness(2)
            $ opponent_b.change_happiness(2)
            opponent_b "Ooh, tough break there."
            $ scene_manager.update_actor(opponent_a, emotion = "default")
            opponent_a "I'm sure you'll get us next time though."

        if round_count > max_rounds:
            $ still_playing = False
            "[the_aunt.possessive_title!c] pushes her cards towards the centre of the table."
            the_aunt "Well, this has been a lot of fun but I should be heading home. It's getting late and I need to get a cab home."

        $ round_count += 1 #The only thing that stops us is if we're over our round count.

    python:
        opponent_a = None
        opponent_b = None
    return

label family_games_night_cash(the_mom, the_aunt, the_sister, partner):
    python:
        # Describes a game where you're playing for cash.
        still_playing = True
        round_count = 1
        max_rounds = 5

        opponent_a, opponent_b, win_chance = family_game_night_get_opponents_with_info([the_mom, the_aunt, the_sister], partner)

    while still_playing:
        call card_round_description(the_mom, the_aunt, the_sister, partner, round_count) from _call_card_round_description_1
        if _return:
            $ partner.change_happiness(5)
            $ opponent_a.change_happiness(-1)
            $ opponent_b.change_happiness(-1)
            # if partner == the_mom:
            #     pass #TODO
            # elif partner == the_aunt:
            #     pass #TODO: Unique dialogue
            # else: the_sister
            #     pass #Dialogue
            $ scene_manager.update_actor(partner, emotion = "happy")
            $ scene_manager.update_actor(opponent_a, emotion = "sad")
            $ scene_manager.update_actor(opponent_b, emotion = "sad")
            partner "Yes!"
            mc.name "Ooh, tough break girls. Come on, pay up."
            "[opponent_a.possessive_title!c] and [opponent_b.possessive_title] sigh and pull out a twenty."
            "They slide the money over to you and [partner.possessive_title]."
            $ mc.business.change_funds(20)
        else:

            $ partner.change_happiness(-1)
            $ opponent_a.change_happiness(5)
            $ opponent_b.change_happiness(5)
            # if partner == the_mom:
            #     pass #TODO
            # elif partner == the_aunt:
            #     pass #TODO: Unique dialogue
            # else: the_sister
            #     pass #Dialogue
            # pass #TODO: Loss dialogue
            $ scene_manager.update_actor(opponent_a, emotion = "happy")
            opponent_a "So sorry about this, but it looks we won."
            $ scene_manager.update_actor(opponent_b, emotion = "happy")
            opponent_b "You know the rules."
            if mc.business.has_funds(20):
                $ mc.business.change_funds(-20)
            else:
                "You pull out your wallet and realise there's no more cash in it."
                mc.name "Uh... it looks like you've cleared me out."
                $ opponent_a.change_happiness(-2)
                $ opponent_b.change_happiness(-2)
                $ scene_manager.update_actor(opponent_b, emotion = "sad")
                "[opponent_b.possessive_title!c] looks disappointed, but [opponent_a.title] just smiles and shrugs."
                opponent_a "Looks like that's the end of the game then. We win!"
                the_aunt "It's getting late, so this is probably a good time for me to head out too."
                $ still_playing = False

        if round_count > max_rounds and still_playing:
            $ still_playing = False
            "[the_aunt.possessive_title!c] pushes her cards towards the centre of the table."
            the_aunt "Well, this has been a lot of fun but I should be heading home. It's getting late and I need to get a cab home."


        $ round_count += 1 #The only thing that stops us is if we're over our round count.

    python:
        opponent_a = None
        opponent_b = None
    return

label family_games_night_strip(the_mom, the_aunt, the_sister, partner):
    # Describes a game where you're playing to strip each other down.
    python:
        still_playing = True
        round_count = 1
        max_rounds = 6

        player_wins = 0 #AKA girl losses
        player_losses = 0

        opponent_a, opponent_b, win_chance = family_game_night_get_opponents_with_info([the_mom, the_aunt, the_sister], partner)


    while still_playing:
        call card_round_description(the_mom, the_aunt, the_sister, partner, round_count) from _call_card_round_description_2
        if _return:
            $ player_wins += 1

            $ something_to_strip = False
            python:
                for person in (opponent_a, opponent_b):
                    the_item = person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                    if the_item:
                        something_to_strip = True
                person = None

            if something_to_strip:
                mc.name "Good try girls, but that round is ours."
                partner "You know what that means!"
                $ partner.change_happiness(2)
                opponent_b "Yeah, we know. Come on, let's get this over with."
                $ something_removed = False
                python:
                    for person in (opponent_a, opponent_b):
                        the_item = person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        if the_item:
                            family_game_night_strip_description(person, the_item, scene_manager)
                            something_removed = True
                            person.change_slut(1, 40)
            else:
                "[opponent_a.title] sighs, and [opponent_b.title] pushes her cards into the centre of the kitchen table."
                opponent_a "Okay, we're out of clothes. You two win."
                opponent_b "Well done. Can we get dressed now? It's a little chilly..."
                partner "What do you think [partner.mc_title]? Should we let them off easy?"
                menu:
                    "Let them get dressed":
                        mc.name "Good game everyone, now let's get dressed and get everything cleaned up."
                        $ opponent_a.apply_planned_outfit()
                        $ opponent_b.apply_planned_outfit()
                        $ partner.apply_planned_outfit()
                        $ scene_manager.draw_scene()


                    "Give us a dance"if opponent_a.sluttiness >= 40 and opponent_b.sluttiness >= 40:

                        $ happy_ending = False
                        mc.name "I don't think so [partner.fname]. I think we should get a little reward for winning."
                        opponent_a "What do you want?"
                        mc.name "You've been able to hide behind the table all night, so I want a little dance now."
                        if mc.business.event_triggers_dict.get("family_games_dance", 0) == 0:
                            $ mc.business.event_triggers_dict["family_games_dance"] = 1
                            "[opponent_a.possessive_title!c] and [opponent_b.possessive_title] glance at each other."
                            opponent_a "What do you think?"
                            opponent_b "I mean... It's just a silly game, right? It doesn't mean anything..."
                            opponent_a "Okay, fine. Then we're getting dressed."
                            mc.name "Sounds fair to me."
                            $ scene_manager.update_actor(opponent_a, position = "default")
                            $ scene_manager.update_actor(opponent_b, position = "default")
                            $ mc.change_locked_clarity(10)
                            "The girls slide their chairs back from the kitchen table and stand up next to each other."
                            opponent_a "Okay, so how do we do this?"
                            opponent_b "Just move around a little. Here, like this..."
                            $ scene_manager.update_actor(opponent_b, position = "kissing")
                            "[opponent_b.title] takes the lead, swaying her hips and holding her hands high and out of the way."
                            $ mc.change_locked_clarity(10)
                            $ scene_manager.update_actor(opponent_a, position = "kissing")
                            "After watching for a second [opponent_a.title] starts to follow along."
                            mc.name "Turn around ladies, let's get a full view of things."
                            opponent_a "Oh my god, this is so embarrassing..."
                            $ scene_manager.update_actor(opponent_a, position = "walking_away")
                            $ scene_manager.update_actor(opponent_b, position = "walking_away")
                            "Despite her complaints she spins around, and [opponent_b.possessive_title] does the same."
                            "You turn to [partner.possessive_title], who is still sitting at the table next to you."
                            mc.name "Enjoying the show [partner.fname]?"
                            partner "It could be better. I think we might need a better view..."
                            opponent_b "Like this?"
                            $ scene_manager.update_actor(opponent_b, position = "standing_doggy")
                            $ mc.change_locked_clarity(20)
                            "[opponent_b.possessive_title!c] puts her hand on the kitchen counter and bends forward. She spreads her legs and twerks her ass for you."
                            $ scene_manager.update_actor(opponent_a, position = "stand3")
                            opponent_a "Oh my god, where did you learn to do that?"
                            "[opponent_b.title] just laughs and wiggles her butt a few more times before standing up."
                            $ scene_manager.update_actor(opponent_b, position = "default")
                            opponent_b "Alright, I think they've seen enough."
                            opponent_a "Whew... Well I think we should get everything tidied up and then get dressed."
                            $ scene_manager.apply_outfit(opponent_a, opponent_a.current_planned_outfit)
                            "Your [opponent_a.title] quickly gets dressed, while you and [partner.possessive_title] watch."
                            $ scene_manager.apply_outfit(opponent_b, opponent_b.current_planned_outfit)
                            $ scene_manager.update_actor(partner, position = "default")
                            "After [opponent_b.title] finishes dressing, you and [partner.possessive_title] stand up."

                        else:
                            $ mc.business.event_triggers_dict["family_games_dance"] += 1

                            "[opponent_a.possessive_title!c] and [opponent_b.possessive_title] smile at each other."
                            opponent_a "What do you think?"
                            opponent_b "I mean, it isn't like this is the first time this has happened."
                            opponent_a "Okay! Let's give them a show!"
                            mc.name "Less talking, more dancing."
                            $ scene_manager.update_actor(opponent_a, position = "default")
                            $ scene_manager.update_actor(opponent_b, position = "default")
                            $ mc.change_locked_clarity(10)
                            $ partner.change_arousal(10)
                            "The girls slide their chairs back from the kitchen table and stand up next to each other."
                            opponent_a "Okay, let's do this!"
                            $ scene_manager.update_actor(opponent_b, position = "kissing")
                            "[opponent_b.title] takes the lead, swaying her hips and holding her hands high and out of the way."
                            $ mc.change_locked_clarity(10)
                            $ scene_manager.update_actor(opponent_a, position = "kissing")
                            "After watching for a second [opponent_a.title] starts to follow along."
                            mc.name "Turn around ladies, let's get a full view of things."
                            opponent_a "Of course, we were just getting to that..."
                            $ scene_manager.update_actor(opponent_a, position = "walking_away")
                            $ scene_manager.update_actor(opponent_b, position = "walking_away")
                            "She spins around, and [opponent_b.possessive_title] does the same."
                            "You turn to [partner.possessive_title], who is still sitting at the table next to you."
                            mc.name "Enjoying the show [partner.fname]?"
                            if partner.sluttiness >= 50:
                                partner "I am, but are you? I think you should show them how much you appreciate their dancing."
                                mc.name "What are you suggesting?"
                                partner "Take your cock out. Then they'll be able to see for themselves how much you are enjoying it!"
                                "You swear you notice her lick her lips for a moment after she says it."
                                "[opponent_a.title] and [opponent_b.possessive_title] seem unphased by the suggestion. You consider it..."
                                menu:
                                    "Pull your cock out":
                                        $ happy_ending = True
                                        "What the hell, let's make this a little more interesting."
                                        $ scene_manager.update_actor(opponent_a, position = "back_peek")
                                        $ scene_manager.update_actor(opponent_b, position = "back_peek")
                                        call cards_cock_out_remarks(the_mom, the_aunt, the_sister, partner) from _cards_cock_out_after_win_02
                                        "You look over at your partner, [partner.title]. Her eyes are fixed on your cock."
                                        $ partner.change_arousal(10)
                                        if partner.vagina_visible and partner.vagina_available:
                                            "She's already exposed from the game, and you definitely notice some arousal in her face and body."
                                        else:
                                            mc.name "Alright, now it is your turn, [partner.fname]."
                                            partner "What? Me?"
                                            mc.name "Yeah, how else can they know that you are enjoying the show?"
                                            partner "Yes, I suppose that would only be fair."
                                            $ scene_manager.strip_to_vagina(partner, prefer_half_off = False)
                                            $ scene_manager.update_actor(partner, position = "sitting")
                                            "Once exposed, you notice definite signs of arousal in her face and body."
                                        "You look back at [opponent_a.title] and [opponent_b.title]."
                                        "They are still standing there, with their backs to you. Your hard cock aches at the sight."
                                        "Involuntarily, you reach down and give it a couple strokes."
                                        if mc.business.event_triggers_dict.get("family_games_happy_ending", 0) == 0:
                                            $ mc.business.event_triggers_dict["family_games_happy_ending"] = 1
                                            "The girls notice. Family game night appears to be on the precipice of turning overtly sexual."
                                            "You know that if this continues, it will change the tone of things significantly."
                                            the_mom "Sweetheart... should you be touching yourself?"
                                            mc.name "Sorry mom, I couldn't help it. Should I stop?"
                                            the_mom "Honey, I think..."
                                            the_aunt "Oh [the_mom.fname], he won, let him have his fun."
                                            the_mom "What!?!"
                                            the_aunt "He is going to do it either way, now or later. Might as well let him do it now."
                                            the_mom "I... I know, but with [the_sister.fname] here..."
                                            the_sister "I'm not saying this isn't really weird, but honestly, I don't mind."
                                            the_sister "I mean... he won, right? It seems like just a little fun."
                                            the_mom "I suppose, if we all agree."
                                            mc.name "[partner.fname] won too. There's a lot of tension in the room, why don't you join me?"
                                            partner "There IS a lot of tension... okay!"
                                            "[partner.title]'s hand goes between her legs, and she starts to touch herself too."
                                            $ partner.change_arousal(20)
                                        else:
                                            $ mc.business.event_triggers_dict["family_games_happy_ending"] += 1
                                            "[partner.title] gasps when she sees what you are doing, but doesn't say anything."
                                            "Instead, she uses her hand and begins to touch herself also."
                                            $ partner.change_arousal(20)
                                        if partner.opinion.masturbating > 0:
                                            partner "Ahh, sweet victory. You two need to step things up a notch though!"
                                        elif partner.opinion.masturbating == 0:
                                            partner "Mmm, it's nice to get myself off like this sometimes. I'll need a better show than this though!"
                                        else:
                                            partner "I don't normally like doing this, but I guess I could. How about a better show now?"
                                        $ partner.discover_opinion("masturbating")

                                    "Just enjoy the dance":
                                        partner "Alright, but if you aren't going to do that, I think we need a better view!"
                            else:
                                partner "It could be better. I think we might need a better view..."
                            opponent_b "Like this?"
                            $ scene_manager.update_actor(opponent_b, position = "standing_doggy")
                            $ mc.change_locked_clarity(20)
                            "[opponent_b.possessive_title!c] puts her hand on the kitchen counter and bends forward. She spreads her legs and twerks her ass for you."
                            $ scene_manager.update_actor(opponent_a, position = "stand3")
                            if happy_ending:
                                $ cum_catcher = the_mom #Set this to a default for now.
                                "You stroke yourself as [opponent_b.possessive_title] shakes her ass for you."
                                $ mc.change_arousal(15)
                                $ partner.change_arousal(25)
                                opponent_a "Damn! Shake it girl!"
                                partner "[opponent_b.name] knows what to do! Get to it [opponent_a.name]!"
                                opponent_a "Okay!"
                                $ scene_manager.update_actor(opponent_a, position = "standing_doggy")
                                $ mc.change_locked_clarity(40)
                                "[opponent_a.title] and [opponent_b.possessive_title] are shaking their asses for you and [partner.title]."
                                "You stroke yourself as you imagine their asses bouncing up and down on your cock, moaning as they fuck you."
                                $ mc.change_arousal(15)
                                $ partner.change_arousal(50)
                                "You look over at [partner.possessive_title], she seems to be REALLY enjoying herself!"
                                $ scene_manager.update_actor(partner, position = "sitting", emotion = "orgasm")
                                partner "Oh my god...!"
                                $ partner.have_orgasm()
                                "[partner.possessive_title!c] cries out and starts to orgasm."
                                "You watch in awe as her whole body spasms and she cums."
                                $ mc.change_locked_clarity(50)
                                $ mc.change_arousal(25)
                                $ scene_manager.update_actor(partner, position = "sitting", emotion = "happy")
                                "When she finishes, she sits back with a smile."
                                partner "Oh god... [partner.mc_title]? You better finish too! It'll be weird if it is only me!"
                                "You can feel yourself getting close, but you want one final push to get you over the edge, so you say the first thing that comes to your mind."
                                $ ran_num = renpy.random.randint(0, 2)
                                if ran_num == 0:    #You blurt out to have your opponents kiss, your partner becomes the cum catcher.
                                    $ cum_catcher = partner
                                    mc.name "I'm so close. You two kiss! I want to watch!"
                                    if opponent_a.opinion.kissing > 0:
                                        opponent_a "Oh! Come here!"
                                    elif opponent_a.opinion.kissing == 0:
                                        opponent_a "Oh? I... okay, come here!"
                                    else:
                                        opponent_a "Oh my god... I can't believe I'm about to do this..."
                                    $ opponent_a.discover_opinion("kissing")
                                    if opponent_b.opinion.kissing > 0:
                                        opponent_b "Mmm! Let's do it!"
                                    elif opponent_b.opinion.kissing == 0:
                                        opponent_b "Wow... okay."
                                    else:
                                        opponent_b "Ugh, I hope you're about done."
                                    $ opponent_b.discover_opinion("kissing")
                                    $ scene_manager.update_actor(opponent_a, position = "kissing")
                                    $ scene_manager.update_actor(opponent_b, position = "walking_away") #Give them the same transforms?
                                    "The two losers embrace. They give each other a tentative kiss, then look back at you."
                                    mc.name "That's it, now go ahead."
                                    "They begin to kiss again, but this time they keep going and start to make out a bit."
                                    "You speed up, stroking yourself eagerly as you watch [opponent_b.title] and [opponent_a.possessive_title] make out."
                                elif ran_num == 1:  #You blurt out for opponent A to put her tits in your face. Opponent B becomes the cum catcher
                                    $ cum_catcher = opponent_b
                                    mc.name "I'm so close. [opponent_a.title], I need a better look at those tits!"
                                    $ scene_manager.update_actor(opponent_a, position = "stand4")
                                    $ scene_manager.update_actor(opponent_b, position = "stand4")
                                    if opponent_a.opinion.showing_her_tits > 0:
                                        opponent_a "Oh? You want a better look at *these*?"
                                    elif opponent_a.opinion.showing_her_tits == 0:
                                        opponent_a "You want a close up?"
                                    else:
                                        opponent_a "Ugh, I guess, if it'll get you off faster."
                                    $ opponent_a.discover_opinion("showing her tits")
                                    $ scene_manager.update_actor(opponent_a, position = "kneeling1")
                                    "[opponent_a.possessive_title!c] comes over and walks around the side of the table and leans over, putting her tits just inches from your face."
                                    if opponent_a.has_large_tits:
                                        "Her big tits shudder and sway pleasingly. She uses her hands to hold them up to you, shaking them around a little."
                                    else:
                                        "Her perky tits shudder slightly. She takes her hands and pinches her nipples, letting out an audible sigh."
                                    "You speed up, stroking yourself eagerly as you watch [opponent_a.title] play with her tits."
                                else:               #You blurt out asking to see how wet your partner's pussy is after she orgasmed. default cum catcher is mom, then aunt.
                                    if partner == the_mom:
                                        $ cum_catcher = the_aunt
                                    else:
                                        $ cum_catcher = the_mom
                                    mc.name "I'm so close. Show me how wet your pussy is, [partner.title]!"
                                    "She seems shocked."
                                    partner "What? Hey we won, why me?"
                                    mc.name "They aren't the ones that just finished. Come on, just let me see."
                                    if partner.opinion.showing_her_ass > 0:
                                        partner "Alright! You just caught me by surprise is all, of course you can look!"
                                    elif partner.opinion.showing_her_ass == 0:
                                        partner "That is a weird request, but alright, I'll show you."
                                    else:
                                        partner "I don't like to show off, but I'm still feeling good, so I guess I can show you..."
                                    $ partner.discover_opinion("showing her ass")
                                    $ scene_manager.update_actor(partner, position = "missionary")
                                    "[partner.possessive_title!c] jumps up on the edge of the kitchen counter and spreads her legs. The other two girls stop and watch too."
                                    $ scene_manager.update_actor(opponent_a, position = "stand3")
                                    $ scene_manager.update_actor(opponent_b, position = "stand4")
                                    "[partner.title] reaches down and gently pull her labia to the sides using two fingers."
                                    "Her pink pussy glistens with moisture from her previous orgasm."
                                    "You speed up, stroking yourself eagerly as you imagine how good it would feel to push your cock inside her soaking wet cunt."
                                $ mc.change_locked_clarity(50)
                                $ mc.change_arousal(50)
                                "This final show is enough to drive you over the edge. You feel your balls tingle as you get ready to finish."
                                mc.name "Oh god, I'm gonna cum!"
                                "[cum_catcher.possessive_title!c] looks around, as if waiting for someone to intervene."
                                "When no one moves, she seems surprised."
                                if cum_catcher.opinion.drinking_cum > 0:
                                    cum_catcher "Fuck, don't let it go to waste! Cum in my mouth!"
                                    $ scene_manager.update_actor(cum_catcher, position = "blowjob", special_modifier="blowjob")
                                    "[cum_catcher.title] suddenly drops to her knees in front of you. She slaps your hand away, grabs your cock and puts the tip in her mouth."
                                    $ climax_controller = ClimaxController(["Cum in her mouth","mouth"])
                                    $ climax_controller.show_climax_menu()
                                    $ cum_catcher.break_taboo("sucking_cock")
                                    "You put your hand on the back of her head as you start to unload. She moans as wave after wave of your hot cum spurts into her eager mouth."
                                    $ cum_catcher.cum_in_mouth()
                                    $ scene_manager.update_actor(cum_catcher, position = "blowjob", special_modifier="blowjob")
                                    "The waves of your orgasm start to grow farther apart, and then eventually stop."
                                    "[cum_catcher.possessive_title!c] opens her eyes and looks up at you. A bit of your cum is dribbling down her chin."
                                    $ scene_manager.update_actor(cum_catcher, position = "kneeling1", emotion = "happy")
                                    $ play_swallow_sound()
                                    "She slowly pulls off, then smiles as she loudly gulps down your semen."
                                    $ cum_catcher.change_slut(2 + cum_catcher.opinion.drinking_cum, 70)
                                    $ cum_catcher.discover_opinion("drinking cum")
                                    $ climax_controller.do_clarity_release(cum_catcher)
                                elif cum_catcher.opinion.cum_facials > 0 or cum_catcher.opinion.being_covered_in_cum > 0:
                                    cum_catcher "Really? Don't let it go to waste, cum on my face!"
                                    "[cum_catcher.possessive_title!c] jumps up and kneels down between your legs."
                                    $ scene_manager.update_actor(cum_catcher, position = "blowjob", emotion = "happy")
                                    cum_catcher "Do it! Cum all over me!"
                                    $ climax_controller = ClimaxController(["Cum on her face","face"])
                                    $ climax_controller.show_climax_menu()
                                    "You're right on the edge. She closes her eyes and tilts her head back."
                                    $ cum_catcher.cum_on_face()
                                    $ scene_manager.update_actor(cum_catcher, position = "blowjob", emotion = "happy")
                                    "You stroke your cock faster and push yourself over the edge, firing your cum onto [cum_catcher.title]'s waiting face. She stays still until you're completely finished."
                                    $ climax_controller.do_clarity_release(cum_catcher)
                                    $ cum_catcher.change_slut(2, 70)
                                    $ cum_catcher.discover_opinion("cum facials")
                                    $ cum_catcher.discover_opinion("being covered in cum")
                                    cum_catcher "Mmm, that feels nice..."
                                    "She sits on her knees for a few seconds, letting you see your handiwork."
                                else:
                                    "However, she doesn't intervene. She watches excitedly as you get ready to finish."
                                    cum_catcher "Do it, I want to watch you cum!"
                                    $ climax_controller = ClimaxController(["Cum!","air"])
                                    $ climax_controller.show_climax_menu()
                                    "You grunt and push yourself over the edge. You pump your cum out in spurts onto the floor."
                                    $ climax_controller.do_clarity_release()
                                    cum_catcher "Well done, I'll make sure to clean that up in a little bit for you."
                                    "You slump back in your chair and take a deep breath."
                                "A bit of an awkward silence settles on the room when you are finished."
                                the_mom "Well... that certainly made for an interesting game night!"
                                if mc.business.event_triggers_dict.get("family_games_happy_ending", 0) == 1:    #First time with a happy ending
                                    the_aunt "I'll say! That was the best game night yet!"
                                else:
                                    the_aunt "I'll say! Another fantastic evening!"
                                the_sister "You three are crazy..."
                                "Your family starts to clean up and get dressed. No one talks about what just happened, they all just accept it."

                                $ scene_manager.update_actor(opponent_a, position = "default")
                                $ scene_manager.update_actor(opponent_b, position = "default")
                                $ scene_manager.update_actor(partner, position = "default")
                                $ scene_manager.apply_outfit(opponent_a, opponent_a.current_planned_outfit)
                                $ scene_manager.apply_outfit(opponent_b, opponent_b.current_planned_outfit)
                                $ scene_manager.apply_outfit(partner, partner.current_planned_outfit)
                                $ partner.change_stats(slut = 2, max_slut = 75)
                                $ opponent_a.change_stats(obedience = 5, slut = 2, max_slut = 75)
                                $ opponent_b.change_stats(obedience = 5, slut = 2, max_slut = 75)
                                the_aunt "Well, I think I'll go get a cab home... goodnight!"
                                $ cum_catcher = None
                            else:
                                opponent_a "Oh my god, where did you learn to do that?"
                                "[opponent_b.title] just laughs and wiggles her butt a few more times before standing up."
                                $ scene_manager.update_actor(opponent_b, position = "default")
                                opponent_b "Alright, I think they've seen enough."
                                opponent_a "Whew... Well I think we should get everything tidied up and then get dressed."
                                $ scene_manager.apply_outfit(opponent_a, opponent_a.current_planned_outfit)
                                "Your [opponent_a.title] quickly gets dressed, while you and [partner.possessive_title] watch."
                                $ scene_manager.apply_outfit(opponent_b, opponent_b.current_planned_outfit)
                                $ scene_manager.update_actor(partner, position = "default")
                                "After [opponent_b.title] finishes dressing, you and [partner.possessive_title] stand up."
                                $ partner.apply_planned_outfit()
                                $ partner.change_slut(2, 45)
                                $ opponent_a.change_stats(obedience = 5, slut = 2, max_slut = 65)
                                $ opponent_b.change_stats(obedience = 5, slut = 2, max_slut = 65)
                        $ still_playing = False
                        $ del happy_ending

                    "Give us a dance\n{menu_red}Requires: 40 Sluttiness, Opponents{/menu_red} (disabled)" if opponent_a.sluttiness < 40 or opponent_b.sluttiness < 40:
                        pass
        else:
            $ player_losses += 1

            $ partner_item = partner.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
            if partner_item:
                #TODO: Add in a check to see if a girl wants to quit after stripping.
                opponent_b "[opponent_a.fname!c], I think we just won. What does that mean again?"
                opponent_a "I think it means [opponent_a.mc_title] and [partner.fname] need to start stripping!"
                partner "Come on, let's get this over with [partner.mc_title]."
                $ family_game_night_strip_description(partner, partner_item, scene_manager)

                "[partner.possessive_title!c] grabs her [partner_item.display_name] and pulls it off while [opponent_a.title] and [opponent_b.title] watch."
            else:
                if player_losses > 4:
                    # You're naked too, so you lose.
                    $ still_playing = False
                    "[opponent_a.title] and [opponent_b.title] cheer."
                    opponent_b "It looks like you two are out of things to take off, which means we've won!"
                    opponent_a "You gave it a good try though."
                    if mc.business.event_triggers_dict.get("family_games_dance", 0) > 0:
                        opponent_b "Does this mean we get a little dance from you two?"
                        opponent_a "Yes! It's only fair!"
                        "[partner.possessive_title!c] looks over at you."
                        partner "Well partner, I guess we owe them this one."
                        $ scene_manager.update_actor(partner, position = "stand4")
                        "You and [partner.title] stand up."
                        opponent_a "I want [opponent_a.mc_title] to dance for me first, then we can switch halfway through!"
                        opponent_b "Okay!"
                        "You step in from of [opponent_a.title]. She giggles a bit, but her cheeks are flushed and she can barely take her eyes off your cock."
                        partner "Damn, wish we had some music or something..."
                        "You awkwardly start to move your body to imaginary music. [partner.possessive_title!c] does the same."
                        opponent_a "Oh my god, this is too funny!"
                        $ opponent_a.change_stats(happiness = 5, obedience = -5)
                        $ scene_manager.update_actor(partner, position = "walking_away")
                        "You both burn around, showing your backsides to the game night winners."
                        opponent_a "Damn... you have a tight ass [opponent_a.mc_title]!"
                        opponent_b "That's right girl, shake it!"
                        $ opponent_a.change_arousal(15)
                        $ opponent_b.change_arousal(10)
                        $ scene_manager.update_actor(partner, position = "stand4")
                        "You turn back around, then switch with [partner.title]. You step over in front of [opponent_b.title]."
                        "You do another jig to the enjoyment of the winning pair."
                        $ opponent_b.change_stats(happiness = 5, obedience = -5)
                        "When they are satisfied, you return to your seats at the table."
                        $ scene_manager.update_actor(partner, position = "sitting")

                else:
                    # She's naked but you aren't, so you keep playing.
                    "[partner.title] looks at you."
                    partner "Come on [partner.mc_title], you're keeping us in the game right now."
            $ partner_item = None

            if still_playing: # Shirt, pants, socks, underwear
                if player_losses == 1: #Take off your shirt.
                    "You grab the bottom of your shirt and pull it over your head in a single movement."
                    the_aunt "Looking good [the_aunt.mc_title]. Have you been working out?"
                elif player_losses == 2: # Take off your pants
                    mc.name "I guess this is next..."
                    "You stand up and undo the zipper on your jeans."
                    if the_mom.effective_sluttiness() < 40:
                        the_mom "Oh lord, [the_mom.mc_title]..."
                        "[the_mom.title] blushes and looks away as you pull them down."
                    else:
                        the_mom "[the_mom.mc_title]..."
                        "[the_mom.title] blushes, but doesn't take her eyes off of you as you pull them down."
                    "You kick your pants clear of your ankles and sit back down, wearing nothing but your socks and a set of underwear that only highlights your bulge."

                elif player_losses == 3: #Take off your socks (totally cheating, but girls have more pieces of clothing on average!)
                    opponent_b "Now this is getting interesting. Come on [opponent_b.mc_title]."
                    "You shrug and reach down to your feet, quickly pulling off your socks and throwing them to the side."
                    opponent_b "Oh, come on. Is that all?"
                    mc.name "What? Were you hoping to see something else?"
                    opponent_b "I... Never mind."
                    mc.name "Win another round and maybe you'll get what you want."

                elif player_losses == 4:
                    "All eyes are fixed on you as you stand up once again, with nothing else to remove but your tight boxers."
                    call cards_cock_out_remarks(the_mom, the_aunt, the_sister, partner) from _card_game_night_cock_out_01
                    opponent_a "Alright well... let's continue the game."

                else: # You're already naked
                    mc.name "Good thing you dressed up today [partner.fname], you're the only reason we're still in the game."
                    #TODO: Extra stuff for being hard in front of them.
                    pass




        if round_count > max_rounds and still_playing:
            $ still_playing = False
            the_aunt "I hate to be a stick in the mud, but I'm going to have to get ready to head home."
            the_aunt "It's getting late, and I have to catch a cab."


        $ round_count += 1


    python:
        opponent_a = None
        opponent_b = None
    return

label card_round_description(the_mom, the_aunt, the_sister, partner, round_count):
    # Describes a technical round of cards and picks a winner (returns True if player).
    python:
        opponent_a, opponent_b, win_chance = family_game_night_get_opponents_with_info([the_mom, the_aunt, the_sister], partner)

    "The cards are dealt. You look at your hand and take a moment to formulate a plan."

    $ win_roll = renpy.random.randint(0,100)
    if win_roll < win_chance: #Player wins
        $ player_win = True
        if win_chance - win_roll >= 50: #Blowout win
            "You see a smooth line of play, and do your best to signal your plans to [partner.title]."
            "Card by card you lay down your hand, and, with the timely help of [partner.possessive_title], win the round."
        elif win_chance - win_roll <= 20: #Fair match
            "You think you see a good line of play, and do your best to signal your plans to [partner.title]."
            "It's a tough round, but with help from [partner.possessive_title] you're able to sweep up enough points to win."
        else: #Barely won
            "You have a poor hand, but [partner.title] is giving you signs that her hand is strong."
            "It's a struggle, but [partner.possessive_title] manages to grab the very last point and win you the round."
    else:
        $ player_win = False
        if win_roll - win_chance >= 50: # Blowout loss
            "Your cards are terrible, and when you glance at [partner.title] she doesn't seem much more confident."
            "From the first card it's clear that you're doomed. [opponent_a.possessive_title!c] and [opponent_b.possessive_title] wipe the floor with you this round."
        elif win_roll - win_chance >= 20: # Fair loss
            "Your hand is weak, and as the cards start to fall it's clear that [partner.possessive_title]'s hand is even worse."
            "It doesn't take long for [opponent_a.possessive_title] and [opponent_b.possessive_title] to win the round."
        else:  #Barely lost
            "Your hand looks strong, but as the cards start to fall you see that [partner.possessive_title] has a much weaker set of cards."
            "It's a close round, but by working together [opponent_a.possessive_title] and [opponent_b.possessive_title] beat you and secure the win."

    return player_win

label cards_winner_reward(the_mom, the_aunt, the_sister, partner):
    #TODO: If you win the game of cards what is your final reward (TODO: Decide if this is a bit we want to have).
    pass
    return

label cards_cock_out_remarks(the_mom, the_aunt, the_sister, partner):
    #Use this label for remarks from the group about MC's dick, when it comes out.
    #Track how many times MC has pulled it out in this group setting. Remarks can vary from shock and surprise to lewd comments.
    "The game already has you excited, and your cock is straining against the fabric."
    if mc.business.event_triggers_dict.get("family_games_cock_out", 0) == 0:
        $ mc.business.event_triggers_dict["family_games_cock_out"] = 1
        if the_mom.effective_sluttiness() < 40:
            the_mom "I think we've all had enough fun, right? You can stop [the_mom.mc_title]."
            the_aunt "Oh come on, don't be such a prude. This is the whole point of the game!"
            "[the_mom.title] leans closer to her sister and half-whispers."
            the_mom "[the_aunt.fname], he's clearly... excited. Isn't this going a little too far?"
            the_aunt "You're worrying way too much. Go ahead [the_aunt.mc_title], take it off!"
        else:
            the_mom "No need to be embarrassed [the_mom.mc_title], we're all family here."
            the_mom "It's just some good–natured fun. Right [the_aunt.fname]?"
            the_aunt "Yeah. Go ahead, take it off!"

        "You slip a thumb under your underwear waistband and start to pull them down."
        "All of the girls watch with keen attention as your hard cock finally slips free of your boxers."
        #TODO: Maybe only have this dialogue trigger the first time.
        $ mc.change_locked_clarity(10)
        the_aunt "You have a nice looking cock [the_aunt.mc_title]." #TODO: Add a way to keep track of how much the various family members know about _each others_ taboos.
        the_mom "[the_aunt.fname]!"
        the_sister "Oh my god..."
        "[the_aunt.possessive_title!c] just shrugs."
        the_aunt "What? It's true, and men just don't get complimented enough these days."
        the_aunt "It's good for his mental health to hear stuff like this."
        the_mom "You shouldn't be commenting on my son's... penis. Especially not in front of me!"
        mc.name "What's wrong with my penis mom?"
        $ mc.change_locked_clarity(10)
        the_mom "Oh! Nothing is wrong with it sweetheart, it's very attractive."
        the_aunt "And a great size."
        the_mom "[the_aunt.fname], please... It is a very impressive size [the_mom.mc_title]."
        $ mc.change_locked_clarity(10)
        "Her gaze lingers on your cock for an extra second before she clears her throat and looks away."
        the_mom "Now... Can you please sit down so we can continue the game?"
        mc.name "Yeah, of course."

        $ partner.change_slut(2, 50)
        $ opponent_a.change_slut(2, 55)
        $ opponent_b.change_slut(2, 55)

        "You sit down, leaning back to give [opponent_a.title] and [opponent_b.title] a good look at you if they want it."
    elif mc.business.event_triggers_dict.get("family_games_cock_out", 0) < 3:
        $ mc.business.event_triggers_dict["family_games_cock_out"] += 1
        if the_mom.effective_sluttiness() < 40:
            the_mom "You don't have to do this again, You can stop [the_mom.mc_title]."
            the_aunt "Oh come on, don't be such a prude. This is the whole point of the game!"
            "[the_mom.title] sighs, but doesn't bother to put up any more resistance."

        "You slip a thumb under your underwear waistband and start to pull them down."
        "All of the girls watch with keen attention as your hard cock finally slips free of your boxers."
        $ mc.change_locked_clarity(10)
        the_aunt "You really do have a nice looking cock [the_aunt.mc_title]."
        the_mom "[the_aunt.fname]!"
        the_sister "Oh my god, not again..."
        "[the_aunt.possessive_title!c] just shrugs."
        the_aunt "What? It's true, and men just don't get complimented enough these days."
        the_aunt "It's good for his mental health to hear stuff like this."
        the_mom "You know, you're right. You really are gifted sweetheart."
        $ mc.change_locked_clarity(10)
        the_sister "I can't believe I'm hearing this..."
        the_mom "Oh, come on [lily.fname], you can't tell me it isn't attractive!"
        the_aunt "And it has a great size!"
        $ mc.change_locked_clarity(10)
        the_sister "I mean I guess..."
        "Her gaze lingers on your cock for an extra second before she clears her throat and looks away."

        $ partner.change_slut(2, 50)
        $ opponent_a.change_slut(2, 55)
        $ opponent_b.change_slut(2, 55)

        "You sit down, leaning back to give [opponent_a.title] and [opponent_b.title] a good look at you if they want it."
    else:   #This is normal now, girls each have their own reactions.
        $ mc.business.event_triggers_dict["family_games_cock_out"] += 1
        "You slip a thumb under your underwear waistband and start to pull them down."
        "All of the girls watch with keen attention as your hard cock finally slips free of your boxers."
        $ mc.change_locked_clarity(10)
        "They all murmur their appreciation as you expose yourself at family game night, yet again."
        if the_aunt.effective_sluttiness() > 80:
            $ the_aunt.change_arousal(15)
            the_aunt "Mmmm, what a magnificent cock..."
        elif the_aunt.effective_sluttiness() > 60:
            $ the_aunt.change_arousal(10)
            the_aunt "Wow, it always surprises me how big it is when you get it out, [the_aunt.mc_title]..."
        elif the_aunt.effective_sluttiness() > 40:
            $ the_aunt.change_arousal(5)
            the_aunt "Wow, as impressive as usual [the_aunt.mc_title]..."
        else:
            the_aunt "Such an impressive penis..."

        if the_mom.effective_sluttiness() > 80:
            $ the_mom.change_arousal(15)
            the_mom "A round or two with that would be a real prize, right [the_aunt.fname]?"
        elif the_mom.effective_sluttiness() > 60:
            $ the_mom.change_arousal(10)
            the_mom "I can't believe you are so well endowed sweetheart. It really is impressive."
        elif the_mom.effective_sluttiness() > 40:
            $ the_mom.change_arousal(5)
            the_mom "Yes [the_aunt.fname], it really is."
        else:
            the_mom "[the_aunt.fname]! Even if true, you don't have to say it out loud..."

        if the_sister.effective_sluttiness() > 80:
            $ the_sister.change_arousal(15)
            the_sister "Fuck bro, bringing out the monster once again?"
        elif the_sister.effective_sluttiness() > 60:
            $ the_sister.change_arousal(10)
            the_sister "Holy fuck, I still can't believe my brother is hung like that..."
        elif the_sister.effective_sluttiness() > 40:
            $ the_sister.change_arousal(5)
            the_sister "Shit, why, of all people, is my brother the one hung like that?"
        else:
            the_sister "Holy shit I can't believe my brother is packing such a big dick..."
        the_mom "Language, young lady."
        "[the_sister.title] rolls her eyes for a moment."
        $ partner.change_slut(2, 50)
        $ opponent_a.change_slut(2, 55)
        $ opponent_b.change_slut(2, 55)

        "You sit down, leaning back to give [opponent_a.title] and [opponent_b.title] a good look at you if they want it."
    return

label aunt_offer_hire(the_person):
    mc.name "Now that you're settled, have you thought about finding some work around the city [the_person.title]?"
    the_person "Oh, I don't know... I have enough money from the divorce that I can survive as long as I'm careful."
    the_person "Can I be honest with you?"
    mc.name "Of course."
    "She chuckles self-consciously before working up her courage to continue."
    the_person "I've never really worked a real job. When I was a teen I worked at a convenience store, and that's about all."
    the_person "I got married, had [cousin.fname], and that was my life."
    the_person "So I'm not even sure how I would get started!"
    mc.name "Well, you could come work for me."
    the_person "Oh, you don't want me hanging around. I'll only get in the way and slow everything down."
    menu:
        "I promise you'll enjoy it" if the_person.known_opinion.working >= 2:
            mc.name "I know you'll enjoy it. Don't you want to get out there and experience the world?"
            "She thinks about it for a moment."
            the_person "Maybe it would be nice to get out of the house now and then."
            mc.name "Exactly what I was thinking! Now, let's talk about your skills..."
            call stranger_hire_result(the_person) from _call_stranger_hire_result_aunt_offer_hire
            if _return:
                call aunt_hire_reaction_setup() from _call_aunt_hire_reaction_setup_aunt_offer_hire
                mc.name "Then it's settled! Welcome to the team [the_person.title]!"
                the_person "I'm almost in shock! I can't believe this is happening!"
            else:
                mc.name "I'm going to need some time to think this over. I'll get back to you, alright?"
                the_person "Right, of course. Take your time."

        "I promise you'll enjoy it\nRequires: Loves working (disabled)" if the_person.known_opinion.working < 2:
            pass

        "Don't you want to work with [cousin.title]?" if cousin.is_employee:
            mc.name "Don't you want to come work with [cousin.fname]? You two get so little time together..."
            "She thinks about it for a moment."
            the_person "It would be nice to spend more time with her. You would be fine with that?"
            mc.name "Of course, I'd love to spend more time around both of you!"
            "[the_person.possessive_title!c] smiles happily and claps her hands together."
            the_person "Alright, I'll do it!"
            mc.name "Good! Now, let's talk about your skills..."
            call stranger_hire_result(the_person) from _call_stranger_hire_result_aunt_offer_hire_2
            if _return:
                call aunt_hire_reaction_setup() from _call_aunt_hire_reaction_setup_aunt_offer_hire_2
                mc.name "Then it's settled! Welcome to the team [the_person.title]!"
                the_person "I'm almost in shock! I can't believe this is happening!"
            else:
                mc.name "I'm going to need some time to think this over. I'll get back to you, alright?"
                the_person "Right, of course. Take your time."

        "Don't you want to work with [cousin.title]?\nRequires: Hire [cousin.title] (disabled)" if not cousin.is_employee:
            pass

        "I understand":
            mc.name "I understand. If you change your mind come talk to me, alright?"
            the_person "Alright, I will."

    return

label aunt_hire_reaction_setup():
    mc.name "One more thing, [the_person.name]."
    call add_role_family_employee_and_set_titles(the_person) from _call_add_role_family_employee_and_set_titles_aunt_hire_reaction
    $ add_cousin_aunt_hire_reaction_action()
    return

label cousin_aunt_hire_reaction(the_person):
    if the_person.is_employee:
        $ the_person.change_happiness(-10)
        the_person "You fucking asshole!"
        "[the_person.possessive_title!c] looks pissed already. It seems to be her natural state."
        mc.name "What?"
        the_person "You hired my [aunt.fname]?!"
        mc.name "Oh, that? Yeah, what's the problem?"
        the_person "When I took this job I thought it would get me away from that bitch."
        the_person "Now I'm going to have to see her all fucking day?"
        $ play_moan_sound()
        "She rolls her eyes and moans dramatically."
        the_person "Why would you hire her in the first place? She's going to be fucking useless."

    else: #She's off doing something else
        the_person "Hey, what the fuck?"
        "[the_person.possessive_title!c] looks pissed already. It seems to be her natural state."
        mc.name "What?"
        the_person "What are you doing with my [aunt.fname]? She said she's working for you now?"
        mc.name "Oh, that? Yeah, what's the problem?"
        the_person "It's weird, that's all. What possible reason do you want that useless bitch around for?"

    menu:
        "She's a good worker":
            mc.name "She seemed like she'd be a good worker if someone gave her the chance."
            "[the_person.title] laughs and shakes her head."
            the_person "The only thing she was ever good at was sucking a dick."
            mc.name "Maybe that will come in handy too."
            the_person "Ew. You pervert."

        "I'm going to fuck her":
            mc.name "Isn't it obvious? I want her close so I can start fucking her around the clock."
            "[the_person.title] laughs and shakes her head."
            the_person "You fucking pervert. Fine, don't tell me why you're doing it."

        "I wanted to piss you off" if the_person.is_employee:
            mc.name "I was thinking about what would make your life as miserable as possible, and this seemed like a good first step."
            the_person "Oh my god, you're the fuuuuucking worst."
            $ play_moan_sound()
            "[the_person.title] moans dramatically."
            the_person "She's going to want to talk to me all the time! God damn it [the_person.mc_title]!"
            the_person "I swear to god I'm going to quit one of these days!"

        "I'm keeping her away from you" if not the_person.is_employee:
            mc.name "I thought you'd thank me. I'm getting her out of the house and away from you."
            "[the_person.title] laughs and shakes her head."
            the_person "Yeah, I'm sure you're doing this out the kindness of your heart."
            the_person "Whatever, I don't even care."

    call talk_person(the_person) from _call_talk_person_cousin_aunt_hire_reaction
    return


label unit_test_role_aunt():
    python:
        the_person = aunt
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person._sluttiness = 0
        the_person._obedience = 100
        the_person.happiness = 100
        the_person.love = 0
    "Unit test Aunt Cuddle scenario, sluttiness = 0"
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_01

    "Unit test Aunt Cuddle scenario, sluttiness = 10"
    python:
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person._sluttiness = 10
        the_person._obedience = 100
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_02

    "Unit test Aunt Cuddle scenario, sluttiness = 20"
    python:
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person._sluttiness = 20
        the_person._obedience = 100
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_03

    "Unit test Aunt Cuddle scenario, sluttiness = 30"
    python:
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person._sluttiness = 30
        the_person._obedience = 100
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_04

    "Unit test Aunt Cuddle scenario, sluttiness = 40"
    python:
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person._sluttiness = 40
        the_person._obedience = 100
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_05

    "Unit test Aunt Cuddle scenario, sluttiness = 50"
    python:
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person._sluttiness = 50
        the_person._obedience = 100
        the_person.happiness = 100
        the_person.love = 0
    call aunt_drunk_cuddle_label from _unit_test_role_aunt_06

    return
