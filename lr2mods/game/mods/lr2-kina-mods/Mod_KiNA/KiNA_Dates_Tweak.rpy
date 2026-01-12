#Counter = KDT00
init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["lunch_date_label"] = "improved_lunch_date_label"

label improved_lunch_date_label(the_person): #KiNA's Edit : Base game's kissing time is weird
    if the_person.is_at(mc.location):
        #$ the_person.event_triggers_dict["date_scheduled"] = False
        $ mc.stats.change_tracked_stat("Girl", "Dates", 1)
        the_person "So, where do you want to go?"
        $ the_type = get_random_from_list(["Chinese food","Thai food","Italian food","sushi","Korean barbecue","pizza","sandwiches"])
        mc.name "I know a nice place nearby. How do you like [the_type]?"
        the_person "No complaints, as long as it's good!"
        mc.name "Alright, let's go then!"
        # change out of uniform (or punishment uniform when going to lunch)
        $ the_person.apply_outfit(the_person.planned_outfit)
        $ the_person.draw_person()
        "You and [the_person.title] walk together to a little lunch place nearby. You chat comfortably with each other as you walk."
        $ renpy.show("restaurant", what = bg_manager.background("Restaurant_Background"), layer = "master")
        "A bell on the door jingles as you walk in."
        $ the_person.draw_person(position = "sitting")
        $ the_type = get_random_from_list(["Chinese food","Thai food","Italian food","sushi","Korean barbecue","pizza","sandwiches"])
        mc.name "My current favourite spot for lunch. Do you like [the_type]?"
        the_person "Is it? Let's see if it lives up to standard. I've heard good things about this place too."
        # change out of uniform (or punishment uniform when going to lunch)
        "You look at the menu with [the_person.possessive_title]. When she decides, she tells you her order."
        mc.name "Alright, I'll go order."
    else:
        "You get ready and text [the_person.title] confirming the time and place. A little while later you meet her outside the restaurant."

        python:
            mc.phone.add_non_convo_message(the_person, "On my way there. See you soon?")
            mc.phone.add_non_convo_message(the_person, "Almost there, I'll meet you inside.", as_mc = True)
            the_person.apply_outfit(the_person.planned_outfit)
            #the_person.event_triggers_dict["date_scheduled"] = False
            mc.stats.change_tracked_stat("Girl", "Dates", 1)
        
        "You get there first, so you grab a table."
        $ renpy.show("restaurant", what = bg_manager.background("Restaurant_Background"), layer = "master")
        "A short time later, [the_person.possessive_title] walks in. She spots you and walks over to sit down."
        $ the_person.draw_person(position = "sitting")
        $ the_type = get_random_from_list(["Chinese food","Thai food","Italian food","sushi","Korean barbecue","pizza","sandwiches"])
        mc.name "Thanks for coming [the_person.title]. Do you like [the_type]?"
        the_person "Yeah! And I've heard good things about this place."
        # change out of uniform (or punishment uniform when going to lunch)
        "You look at the menu with [the_person.possessive_title]. When she decides, she tells you her order."
        mc.name "Alright, I'll go order."
    $ clear_scene()
    "You order food for yourself and [the_person.possessive_title] and wait until it's ready."
    $ mc.business.change_funds(-30, stat = "Food and Drinks")
    $ the_person.draw_person(position = "sitting")
    "You sit down again with [the_person.title]. You have some time for small talk before the food is ready."
    call date_small_talk_label(the_person) from _lunch_date_small_talk_test_KDT01
    "Soon, an employee brings out your food and sets it on the table."
    if renpy.random.randint(0,100) < 40:
        the_person "Mmm, it looks delicious. I'm just going to wash my hands, I'll be back in a moment."
        $ clear_scene()
        "[the_person.possessive_title!c] stands up heads for the washroom."
        menu:
            "Add some serum to her food" if mc.inventory.has_serum:
                call give_serum(the_person) from _call_give_serum_KDT020
                if _return:
                    "Once you're sure nobody else is watching you add a dose of serum to [the_person.title]'s food."
                    "With that done you lean back and relax, waiting until she returns to start eating your own food."
                else:
                    "You think about adding a dose of serum to [the_person.title]'s food, but decide against it."
                    "Instead you lean back and relax, waiting until she returns to start eating your own food."

            "Add some serum to her food\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                pass

            "Leave her food alone":
                "You lean back and relax, waiting until [the_person.title] returns to start eating."

        $ the_person.draw_person(position = "sitting")
        the_person "Thanks for waiting, now let's eat!"
    else:
        the_person "Mmm, it looks delicious. Or maybe I'm just really hungry. Either way, let's eat!"
    "You dig into your food, chatting between bites about this and that. What do you talk about?"

    call date_conversation(the_person) from _call_date_conversation_KDT01

    $ kiss_after = _return
    if the_person.get_destination(time_slot = (time_of_day + 1)) == mc.location:
        "Before you know it you've both finished your lunch and it's time to leave. You walk [the_person.title] outside."
        $ downtown.show_background()
        $ the_person.draw_person()
        if the_person.love > 30 and not mc.phone.has_number(the_person):
            the_person "Can I give you my number, so you can call me sometime?"
            mc.name "Of course you can."
            "You hand her your phone. She types in her contact information, then hands it back with a smile."
            $ mc.phone.register_number(the_person)

        the_person "This was fun [the_person.mc_title], we should do it again."
        if mc.is_at(home_hub):
            mc.name "Yeah, we should. We don't get to spend as much time together as we used to."
            if the_person.love > 50:
                "You wrap your arm around [the_person.title]'s shoulder as the two of you make your way back home."
            elif the_person.love > 30:
                "You take [the_person.title]'s hand as the two of you make your way back home."
            else:
                "You talk a little as the two of you make your way back home."
            "The conversation mellows into comfortable silence, punctuated by occasional shared glances."
            "Upon reaching your doorstep, you pause, the gravity of the moment hanging in the air."
            the_person "I had a really great time today. Thanks for inviting me out."
            mc.name "I'm glad you enjoyed it. I had a great time too. Maybe we can do something like this again soon."
            the_person "Yeah, I'd like that."
            if not the_person.has_family_taboo and (not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0) and kiss_after:
                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "She steps in close and kisses you. Her lips are soft and warm against yours."
            else:
                $ the_person.draw_person(position = "kissing")
                "She steps close and gives you a warm hug."
            $ the_person.draw_person()
            "After a brief second she steps back and smiles."
            "With one last smile the two of you enter the house."
        elif mc.is_at(office_hub):
            mc.name "Yeah, we should. It's always nice to get out of the office for lunch."
            if the_person.love > 60 and (the_person.is_girlfriend or not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0):
                #highish love
                "You wrap your arm around [the_person.title]'s shoulder as the two of you make your way back to work."
                "As you approach the building, you pause at the entrance and share a quick glance."
                the_person "Thanks for lunch, [mc.name]. I really needed that."
                mc.name "Me too. Let's not wait too long for the next one."
                if not the_person.has_family_taboo and kiss_after:
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "She steps in close and kisses you. Her lips are soft and warm against yours."
                else:
                    $ the_person.draw_person(position = "kissing")
                    "She steps close and gives you a warm hug."
                $ the_person.draw_person()
                "After a brief second she steps back and smiles."
                "She smiles warmly, and you both head inside, the hum of office life welcoming you back."
            elif the_person.love > 40 and not the_person.has_significant_other:
                #midlish love and not in a relationship
                "You walk back to the office, hand in hand, enjoying the comfortable silence that has settled between you."
                "As you approach the entrance, you exchange a knowing smile."
                the_person "Back to the grind, huh?"
                mc.name "Yep, but it was a nice break. Thanks for joining me."
                the_person "Anytime, [mc.name]."
                if not the_person.has_family_taboo and kiss_after:
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "She steps in close and kisses you. Her lips are soft and warm against yours."
                else:
                    $ the_person.draw_person(position = "kissing")
                    "She steps close and gives you a warm hug."
                $ the_person.draw_person()
                "After a brief second she steps back and smiles."
                "You part ways at the door, both heading to your respective tasks."
                $ mc.location.show_background()
                "As you settle back at your desk, you find yourself smiling at the memory of the lunch."
            else:
                #strictly business
                "You walk back to the office together, the conversation tapering off into comfortable silence. The warm sunlight and the buzz of the city fill the gaps between your words."
                "When you reach the entrance, [the_person.title] smiles at you."
                the_person "Thanks again for lunch, [the_person.mc_title]. Let's plan another one soon."
                mc.name "Definitely. Have a good afternoon."
                $ mc.location.show_background()
                "With a final nod, you both head to your respective desks, the brief break giving you a renewed sense of energy for the rest of the day."
        else:
            mc.name "Anytime, [the_person.title]."
            if the_person.love > 50 and (not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0):
                "You wrap your arm around [the_person.title]'s shoulder as the two of you make your way back to the [mc.location.formal_name]."
                if not the_person.has_family_taboo and kiss_after:
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "She steps in close and kisses you. Her lips are soft and warm against yours."
                else:
                    $ the_person.draw_person(position = "kissing")
                    "She steps close and gives you a warm hug."
                $ the_person.draw_person()
                "After a brief second she steps back and smiles."
                
            elif the_person.love > 30 and (not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0):
                "You take [the_person.title]'s hand as the two of you make your way back to the [mc.location.formal_name]."
            else:
                "It is a bit awkward as the two of you walk back towards the [mc.location.formal_name] together."
    else:
        "Before you know it you've both finished your lunch and it's time to leave. You walk [the_person.title] outside and get ready to say goodbye."
        $ downtown.show_background()
        $ the_person.draw_person()
        if the_person.love > 30 and not mc.phone.has_number(the_person):
            the_person "Can I give you my number, so you can call me sometime?"
            mc.name "Of course you can."
            "You hand her your phone. She types in her contact information, then hands it back with a smile."
            $ mc.phone.register_number(the_person)

        if not the_person.has_family_taboo and (the_person.is_girlfriend or not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0) and kiss_after:
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "She steps in close and kisses you. Her lips are soft and warm against yours."
        else:
            $ the_person.draw_person(position = "kissing")
            "She steps close and gives you a warm hug."

        $ the_person.draw_person()
        "After a brief second she steps back and smiles."

        the_person "This was fun [the_person.mc_title], we should do it again."
        mc.name "Yeah, we should. I'll see you around."

    $ clear_scene()
    $ the_person.apply_planned_outfit() # change back to uniform if needed
    $ mc.location.show_background() # leave restaurant and move back to original location
    call advance_time() from _call_advance_time_KDT29
    return
