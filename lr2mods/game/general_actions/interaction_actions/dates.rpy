# Contains all of the descriptions for different date results, and shared things such as a girl taking you home after a successful date.

#Note: This only contains generic dates, if a date is specific to a role (ie. the special fuck date available to paramours) it's in their role file.
#Note: These are only the dates themselves. How they are added (ie. what specific thing triggered them) is in whatever file is appropriate (usually chat_action.rpy, since you ask her out)
init -2 python:

    small_talk_discussion_topics = {
        "general" : ["flirting", "sports", "hiking", "Mondays", "Fridays", "the weekend"],
        "work": ["working", "work uniforms", "research work", "marketing work", "HR work", "supply work", "production work"],
        "style": ["skirts", "pants", "dresses", "boots", "high heels", "makeup", "conservative outfits", "the colour blue", "the colour yellow", "the colour red", "the colour pink", "the colour green", "the colour purple", "the colour white", "the colour black"],
        "positions": ["missionary style sex", "doggy style sex", "sex standing up"],
        "sex_types": ["vaginal sex", "anal sex", "giving blowjobs", "getting head", "public sex"],
        "cum": ["creampies", "being covered in cum", "cum facials", "drinking cum", "bareback sex"],
        "sexy_clothing" : ["skimpy outfits", "skimpy uniforms", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "lingerie", "high heels", "dresses"],
        "kinks" : ["masturbating", "giving handjobs", "being fingered", "being submissive", "taking control", "threesomes", "incest"]
    }

    def lunch_date_create_topics_menu(the_person):
        opinion_question_list = []

        #Generates a list with a few (usually 4, unless there's some opinion collision, but it's not important enough to filter things out more intelligently) opinions, one of which she likes
        for x in builtins.range(3):
            possible_opinion = the_person.get_random_opinion()
            if possible_opinion not in opinion_question_list:
                opinion_question_list.append(possible_opinion)

        key_opinion = the_person.get_random_opinion(only_positive = True, include_sexy = the_person.effective_sluttiness() > 50)
        if key_opinion is not None and key_opinion not in opinion_question_list:
            opinion_question_list.append(key_opinion)

        neutral_opinion = get_random_from_list([x for x in the_person.get_normal_opinions_list() if x not in opinion_question_list and the_person.opinion(x) == 0])
        if neutral_opinion:
            opinion_question_list.append(neutral_opinion)

        if len(opinion_question_list) == 0:
            opinion_question_list.append("small talk")

        renpy.random.shuffle(opinion_question_list)

        formatted_opinion_list = []
        for item in opinion_question_list:
            score = the_person.known_opinion(item)    # only colorize when opinion is known
            color = "#fff"
            if score > 0:
                color = "#00e000"
            elif score < 0:
                color = "#e00000"

            formatted_opinion_list.append((f"Chat about {{color={color}}}{item}{{/color}}", item))
        return formatted_opinion_list

    def her_place_door_fuck_check(person):
        if renpy.random.randint(0, 100) + (person.opinion.public_sex * 20) + (person.arousal / 2) > 100:
            return person.is_willing(against_wall)
        return False

    def her_place_spend_the_night_check(person, report_log):    #Determines if girl offers to let MC stay over
        if mc.has_event_tomorrow_morning:
            return False
        if person.love >= 60:
            return True
        if person.effective_sluttiness() >= 60 and (report_log is not None and report_log.get("girl orgasms", 0) > 2):
            return True
        return False

    def her_place_get_finish_type(person):
        # Returns a string based on how the one night stand should finish.
        # First, check and see if we are on a serum type. Easiest scenario
        finish_list = []
        if person.active_serum_with_hidden_tag("Love"):
            finish_list.append("Love")
        if person.active_serum_with_hidden_tag("Obedience"):
            finish_list.append("Obedience")
        if person.active_serum_with_hidden_tag("Slut"):
            finish_list.append("Slut")
        if len(finish_list) > 0:
            return get_random_from_list(finish_list)

        #If not, make a weighted list to pull from
        finish_list.append(["TV", 40])
        if person.love > 40:
            finish_list.append(["Love", person.love - 40])
        if person.obedience > 140:
            finish_list.append(["Obedience", person.obedience - 140])
        if person.effective_sluttiness() > 40:
            finish_list.append(["Slut", person.effective_sluttiness() - 40])
        return get_random_from_weighted_list(finish_list)

    def date_take_home_her_place_tv_finish_popup_text(person):
        if (the_person.is_willing(standing_grope) or the_person.is_willing(standing_finger)) and mc.sex_skills["Foreplay"] >= 6 and mc.max_energy >= 180 and mc.sex_skills["Oral"] >= 4 and mc.sex_skills["Vaginal"] >= 6:
            return "Full Scene"
        popup_text = "Partial Scene:"
        if not (the_person.is_willing(standing_grope) or the_person.is_willing(standing_finger)):
            popup_text += ("\n  Date Unwilling to be Groped")
        if mc.max_energy < 180:
            popup_text += ("\n  Max Energy 180+")
        if mc.sex_skills["Foreplay"] < 6:
            popup_text += ("\n  Foreplay Skill 6+")
        if mc.sex_skills["Oral"] < 4:
            popup_text += ("\n  Oral Skill 6+")
        if mc.sex_skills["Vaginal"] < 6:
            popup_text += ("\n  Vaginal Skill 6+")
        return popup_text



    def get_random_opinion_from_list(opinion_list, person):
        return_list = []
        for op in opinion_list:
            if person.has_opinion(op):
                return_list.append(op)
        if len(return_list) == 0:
            return None
        return get_random_from_list(return_list)

    def small_talk_positions_avail(person):
        return (person.anal_sex_count + person.vaginal_sex_count) > 3

    def small_talk_sex_types_avail(person):
        return person.sex_record.get("Orgasms", 0) > 3

    def small_talk_cum_avail(person):
        return person.cum_exposure_count > 3

    def small_talk_sexual_clothing_avail(person):
        if person.has_taboo(["bare_tits", "bare_pussy"]):
            return False
        return True

    def small_talk_kinks_avail(person):
        return person.anal_sex_count > 1

label date_conversation(the_person):
    $ conversation_choice = renpy.display_menu(lunch_date_create_topics_menu(the_person),True,"Choice")
    $ the_person.discover_opinion(conversation_choice)
    $ score = the_person.opinion(conversation_choice)
    $ kiss_after = False
    if score > 0:
        "You steer the conversation towards [conversation_choice] and [the_person.title] seems more interested and engaged."
        $ kiss_after = True
        $ the_person.change_stats(happiness = 5, love = 5, max_love = 40)
    elif score == 0:
        "You steer the conversation towards [conversation_choice]. [the_person.title] chats pleasantly with you, but she doesn't seem terribly interested in the topic."
        $ the_person.change_love(2, 40)
    else: #Negative score
        "You steer the conversation towards [conversation_choice]. It becomes quickly apparent that [the_person.title] is not interested in talking about that at all."
        $ the_person.change_love(1, 35)
    $ del conversation_choice
    return kiss_after

label date_small_talk_label(the_person):
    # A more open ended small talk label
    # This should be talking only, no position changes
    $ discussion_opinion = None
    $ sexy_topic = False
    "As you make small talk with [the_person.title], you decide to try and find out something more specific about her."
    menu:
        "Get to know her" if the_person.has_gtk_avail:
            "You decide to try and get to know [the_person.possessive_title]'s history a bit better."
            call screen main_choice_display(build_menu_items([the_person.build_gtk_list()]))

            if isinstance(_return, Action):
                $ _return.call_action(the_person)
            #Call the gtk menu and appropriate action here
            $ del discussion_opinion
            $ del sexy_topic
            return
        "Ask about general opinions":
            "You spend some time getting to know her general opinions."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["general"], the_person)
        "Ask about work opinions":
            "You spend some time asking her about her work life and preferences."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["work"], the_person)
        "Ask about style opinions":
            "You spend some time asking about her sense of style and preferences."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["style"], the_person)
        "Ask about Sexual Positions" if small_talk_positions_avail(the_person):
            "You spend some time asking about what sexual positions she prefers."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["positions"], the_person)
            $ sexy_topic = True
        "Sex types" if small_talk_sex_types_avail(the_person):
            "You spend some time asking about what types of sex she prefers."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["sex_types"], the_person)
            $ sexy_topic = True
        "Cum" if small_talk_cum_avail(the_person):
            "You spend some time asking about her thoughts on semen during sex."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["cum"], the_person)
            $ sexy_topic = True
        "Sexy Clothing" if small_talk_sexual_clothing_avail(the_person):
            "You spend some time asking about her thoughts on sexually provacative clothing."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["sexy_clothing"], the_person)
            $ sexy_topic = True
        "Other Kinks" if small_talk_kinks_avail(the_person):
            "You spend some time asking about sexual kinks."
            $ discussion_opinion = get_random_opinion_from_list(small_talk_discussion_topics["kinks"], the_person)
            $ sexy_topic = True

    if discussion_opinion == None:
        the_person "Well, I'll be honest. I don't really have any strong feelings about that."
        mc.name "Ah, I see."
    else:
        $ the_person.discover_opinion(discussion_opinion)
        $ text_one = person_opinion_to_string(the_person, discussion_opinion)[1]
        $ text_two = get_topic_text(discussion_opinion)
        if sexy_topic:
            "[the_person.possessive_title!c] gives you a sultry smile, excited to talk about something naughty with you."
            $ the_person.change_arousal(5)
            the_person "Keep this between us, but I [text_one] [text_two]."
            mc.name "Nice. That is good to know."
        else:
            "[the_person.possessive_title!c] smiles, happy to talk about her opinions as you get to know her."
            $ the_person.change_happiness(1)
            the_person "You might already know this, but I [text_one] [text_two]."
            mc.name "Huh. That is good to know."
    $ del discussion_opinion
    $ del sexy_topic
    return

label lunch_date_label(the_person): #Could technically be included in the planning phase, but broken out to fit the structure of the other events.
    "You get ready and text [the_person.title] confirming the time and place. A little while later you meet her outside the restaurant."

    python:
        mc.phone.add_non_convo_message(the_person, "On my way there. See you soon?")
        mc.phone.add_non_convo_message(the_person, "Almost there, I'll meet you inside.", as_mc = True)
        the_person.apply_outfit(the_person.planned_outfit)
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
    "You order food for yourself and [the_person.possessive_title]."
    $ mc.business.change_funds(-30, stat = "Food and Drinks")
    $ the_person.draw_person(position = "sitting")
    "You sit down again with [the_person.title]. You have some time for small talk before the food is ready."
    call date_small_talk_label(the_person) from _lunch_date_small_talk_test_01
    "Soon, an employee brings out your food and sets it on the table."
    the_person "Mmm, it looks delicious. I'm just going to wash my hands, I'll be back in a moment."
    $ clear_scene()
    "[the_person.possessive_title!c] stands up heads for the washroom."
    menu:
        "Add some serum to her food" if mc.inventory.has_serum:
            call give_serum(the_person) from _call_give_serum_20
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
    "You dig into your food, chatting between bites about this and that. What do you talk about?"

    call date_conversation(the_person) from _call_date_conversation_1

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

        if not the_person.has_family_taboo and (not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0) and kiss_after:
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "She steps in close and kisses you. Her lips are soft and warm against yours."
        else:
            $ the_person.draw_person(position = "kissing")
            "She steps close and gives you a warm hug."

        $ the_person.draw_person()
        "After a brief second she steps back and smiles."

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
            "With one last smile the two of you enter the house."
        elif mc.is_at(office_hub):
            mc.name "Yeah, we should. It's always nice to get out of the office for lunch."
            if the_person.love > 50 and (the_person.is_girlfriend or not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0):
                "You wrap your arm around [the_person.title]'s shoulder as the two of you make your way back to work."
                "As you approach the building, you pause at the entrance and share a quick glance."
                the_person "Thanks for lunch, [mc.name]. I really needed that."
                mc.name "Me too. Let's not wait too long for the next one."
                "She smiles warmly, and you both head inside, the hum of office life welcoming you back."
            elif the_person.love > 30 and (the_person.is_girlfriend or not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0):
                "You walk back to the office, hand in hand, enjoying the comfortable silence that has settled between you."
                "As you approach the entrance, you exchange a knowing smile."
                the_person "Back to the grind, huh?"
                mc.name "Yep, but it was a nice break. Thanks for joining me."
                the_person "Anytime, [mc.name]."
                "You part ways at the door, both heading to your respective tasks."
                $ mc.location.show_background()
                "As you settle back at your desk, you find yourself smiling at the memory of the lunch."
            else:
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
    call advance_time() from _call_advance_time_29
    return

label movie_date_label(the_person):
    #The actual event produced when it's time to go on your date.
    "You have a movie date planned with [the_person.title] right now."

    menu:
        "Get ready for the date {image=time_advance}" if mc.business.has_funds(50):
            pass

        "Get ready for the date\n{menu_red}Requires: $50{/menu_red} (disabled)" if not mc.business.has_funds(50):
            pass

        "Cancel the date (tooltip)She won't be happy with you cancelling last minute.":
            $ mc.start_text_convo(the_person)
            mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
            $ the_person.change_stats(happiness = -5, love = -5)
            the_person "I hope everything is okay. Maybe we can do this some other time then."
            $ mc.end_text_convo()
            return

    if mom_date_intercept_requirement(mom, the_person) and renpy.random.randint(0,100) < (mom.love):
        call mom_date_intercept(mom, the_person) from _call_mom_date_intercept
        if _return:
            $ clear_scene()
            return "Advance Time"

    "You get ready and text [the_person.title] confirming the time and place. A little while later you meet her outside the theatre."

    python:
        mc.phone.add_non_convo_message(the_person, "On my way to the theatre. See you soon?")
        mc.phone.add_non_convo_message(the_person, "Almost there, I'll meet you outside.", as_mc = True)
        mc.stats.change_tracked_stat("Girl", "Dates", 1)
        mc.change_location(downtown)

        scene_manager = Scene()
        scene_manager.add_actor(the_person, the_person.decide_on_outfit(sluttiness_modifier = 0.2))
        scene_manager.add_actor(the_person)

    the_person "Hey, good to see you!"
    the_person "I'm ready to go in, what do you want to see?"
    $ renpy.show("Theatre", what = bg_manager.background("Theatre_Background"), layer = "master")
    $ movie_type = None
    $ likes_movie = False
    menu:
        "Watch an action movie":
            $ the_choice = get_random_from_list(["The Revengers", "Raiders of the Found Ark", "Die Difficult", "Mission: Improbable", "Wonderful Woman", "John Wicked: Part 3", "The Destructonator", "Waterman"])
            $ movie_type = "action"
            if the_person.personality.personality_type_prefix == wild_personality.personality_type_prefix or the_person.personality.default_prefix == wild_personality.personality_type_prefix: #If it's a wild or wild derived personality type
                $ likes_movie = True
            mc.name "Yeah, I've wanted to see [the_choice] for a while. I'll go get us tickets."

        "Watch a comedic movie":
            $ the_choice = get_random_from_list(["Spooky Movie", "Aaron Powers", "Dumber and Dumberest-er", "Ghostblasters", "Shaun of the Undead"])
            $ movie_type = "comedy"
            if the_person.personality.personality_type_prefix == relaxed_personality.personality_type_prefix or the_person.personality.default_prefix == relaxed_personality.personality_type_prefix:
                $ likes_movie = True
            mc.name "I thought we'd both enjoy [the_choice]. I'll go get us tickets."

        "Watch a romantic movie":
            $ the_choice = get_random_from_list(["Olympic", "Britannic","The Workbook", "East Side Tale", "Pottery Poltergeist"])
            $ movie_type = "romantic"
            if the_person.personality.personality_type_prefix == reserved_personality.personality_type_prefix or the_person.personality.default_prefix == reserved_personality.personality_type_prefix:
                $ likes_movie = True
            mc.name "I thought [the_choice] would be a good fit for us. You just wait here, I'll go get us tickets."

        "Watch a foreign film":
            $ the_choice = get_random_from_list(["that one in French", "that one in Italian", "that one in Russian", "that one in Japanese", "that one in Mandarin", "that one that's silent"])
            $ movie_type = "foreign"
            if the_person.personality.personality_type_prefix == introvert_personality.personality_type_prefix or the_person.personality.default_prefix == introvert_personality.personality_type_prefix:
                $ likes_movie = True
            mc.name "I haven't heard much about it, but I think we should watch [the_choice]. It should be a really unique one."
            mc.name "I'll go get us tickets; be back in a moment."

    if the_person.personality is bimbo_personality and movie_type != "foreign":
        $ likes_movie = True # Bimbos like anything other than weird art pieces.

    #TODO: Generate a girl and assign them a uniform.
    "You walk up to the ticket booth and get tickets for yourself and [the_person.possessive_title]."
    $ mc.business.change_funds(-50)

    "Tickets in hand, you rejoin [the_person.title] and set off to find your theatre."
    the_person "Did you want to get us some popcorn or anything like that?"
    menu:
        "Stop at the concession stand\n{menu_red}Costs: $20{/menu_red}" if mc.business.has_funds(20):
            mc.name "Sure, you run ahead and I'll go get us some snacks."
            $ scene_manager.hide_actor(the_person)
            $ mc.business.change_funds(-20, stat = "Food and Drinks")
            "You give [the_person.possessive_title] her ticket and split up. At the concession stand you get a pair of drinks and some popcorn to share."
            menu:
                "Put a dose of serum in her drink" if mc.inventory.has_serum:
                    call give_serum(the_person) from _call_give_serum_14

                "Put a dose of serum in her drink\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                    pass

                "Leave her drink alone":
                    pass

            $ scene_manager.show_actor(the_person, position = "sitting")
            "Snacks in hand you return to [the_person.title]. She takes a sip from her drink as you settle into your seat beside her."


        "Stop at the concession stand\n{menu_red}Requires: $20{/menu_red} (disabled)" if not mc.business.has_funds(20):
            pass

        "Just go to the movie":
            mc.name "That stuff is always so overpriced, I hate giving them the satisfaction."
            $ the_person.change_happiness(-2)
            the_person "Right. Sure."
            $ scene_manager.update_actor(the_person, position = "sitting")
            "You find your theatre, pick your seats, and settle down next to each other for the movie."


    "You chat for a few minutes while you wait for the movie to begin."

    call date_small_talk_label(the_person) from _movie_date_small_talk_test_01

    $ scene_manager.update_actor(the_person, lighting = dark_lighting[time_of_day])
    "The lights dim and the movie begins."

    if likes_movie: #She's enjoying the movie. Good for love gain, and you may be able to feel her up while she's enjoying the movie.
        "Halfway through the movie it's clear that [the_person.title] is having a great time. She's leaning forward in her seat, eyes fixed firmly on the screen."
        $ mc.change_locked_clarity(10)
        "As the movie approaches its climax she reaches her hand down and finds yours to hold."
        "When it's finished you leave the theatre together, still holding hands."
        $ scene_manager.update_actor(the_person, position = "default", emotion = "happy", lighting = standard_indoor_lighting[time_of_day])
        mc.name "So, did you like the movie?"
        the_person "It was amazing! Let's watch something like that next time."
        $ the_person.change_love(5, 60)

    else: #She's bored. Bad for love gain, but good for getting her to fool around. She may start to feel you up to distract herself.
        "Halfway through the movie it's becoming clear that [the_person.title] isn't enthralled by it."
        if (the_person.sluttiness + the_person.opinion.public_sex * 5) > 50 and (not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0) and not the_person.has_family_taboo:
            $ mc.change_locked_clarity(10)
            "While you're watching you feel her rest her hand on your thigh. She squeezes it gently and slides her hand up higher and higher while whispering into your ear."
            the_person "I'm bored. You don't mind if I make this a little more interesting, do you?"
            "You take a quick look around. The theatre you're in is mostly empty, and nobody is in the same row as you."
            menu:
                "Go ahead":
                    mc.name "I'm certainly not going to stop you."
                    $ mc.change_locked_clarity(10)
                    "Her hand slides up to your waist and undoes the button to your pants. You get a jolt of pleasure as her fingers slide onto your hardening cock."
                    "[the_person.title] stays sitting in her seat, eyes fixed on the movie screen as she begins to fondle your dick."
                    "As you get hard she starts to stroke you off. Her hand is warm and soft, and the risk of being caught only enhances the experience."
                    $ mc.change_locked_clarity(10)
                    "After a few minutes [the_person.possessive_title] brings her hand to her mouth, licks it, and then goes back go jerking you off with her slick hand."

                    if (the_person.sluttiness + the_person.opinion.public_sex * 5) > 65 and (not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0) and not the_person.has_family_taboo:
                        "You're enjoying the feeling of her wet hand sliding up and down your cock when she stops. You're about to say something when she slides off of her movie seat and kneels down in the isle."
                        $ scene_manager.update_actor(the_person, position = "blowjob", special_modifier = "blowjob")
                        $ mc.change_locked_clarity(20)
                        $ the_person.increase_blowjobs()
                        "Without a word she slides your hard dick into her mouth and starts to suck on it. You struggle to hold back your moans as she blows you."
                        "You rest a hand on the top of her head and keep a lookout in the theatre, but nobody seems to have noticed."
                        "She comes up for air slides up your body, whispering into your ear."
                        the_person "Do you want to go to the bathroom and fuck me, or do you want to finish in my mouth right here?"
                        menu:
                            "Fuck her":
                                $ scene_manager.update_actor(the_person, position = "walking_away")
                                "You zip up your pants and stand up. [the_person.title] takes your hand and you rush out of the theatre."
                                $ scene_manager.hide_actor(the_person)
                                $ mc.change_location(mall_bathroom)
                                $ the_person.change_arousal(20 + (the_person.opinion.public_sex * 10))
                                $ mc.change_arousal(40)
                                $ the_person.draw_person()
                                "You hurry into the women's bathroom and lock yourselves in an empty stall."
                                call fuck_person(the_person, private = True) from _call_fuck_person_28

                                $ renpy.show("Theatre", what = bg_manager.background("Theatre_Background"), layer = "master")
                                $ scene_manager.show_actor(the_person, the_person.planned_outfit, position = "sitting")

                                "You slip out of the bathroom as quickly as possible and return to your seats with some time pleasantly passed."

                            "Cum right here":
                                mc.name "I want you to finish me here."
                                $ mc.change_locked_clarity(20)
                                "She purrs in your ear and slides back down to her knees again. Her warm mouth wraps itself around your shaft and she starts to blow you again."
                                "It doesn't take long for her to bring you to the edge of your orgasm."
                                $ climax_controller = ClimaxController(["Cum in her mouth","mouth"],["Cum down her throat","throat"])
                                $ the_choice = climax_controller.show_climax_menu()
                                if the_choice == "Cum in her mouth":
                                    $ climax_controller.do_clarity_release()
                                    "You clutch at the movie seat arm rests and suppress a grunt as you climax, blowing your hot load into [the_person.title]'s mouth."
                                    $ the_person.cum_in_mouth()
                                    $ scene_manager.update_actor(the_person, position = "sitting")
                                    "She waits until you're finished, then pulls off your cock, wipes her lips on the back of her hand, and sits down next to you."
                                    the_person "Mmm, thank you. That was fun."
                                    "She takes your hand and holds it. You lean back, thoroughly spent, and zone out for the rest of the movie."
                                elif the_choice == "Cum down her throat":
                                    "You grab onto [the_person.title]'s head and pull her as deep as you can get her onto your cock."
                                    if the_person.is_submissive or the_person.opinion.drinking_cum > 0:
                                        "She gags and twitches, but shifts to let you bury yourself entirely in her throat."
                                        $ climax_controller.do_clarity_release()
                                        "You cum, pumping your load out in big, hot pulses right into her stomach. In the dim theatre light you can see her flutter with each new deposit."
                                        $ the_person.cum_in_mouth()
                                        "When you're entirely spent you let go of [the_person.possessive_title]'s head and sit back with a sigh."
                                        $ the_person.discover_opinion("being submissive")
                                        $ play_swallow_sound()
                                        "[the_person.title] doesn't move for another few long seconds. You feel her throat constrict a few times as she swallows the last of your cum first."
                                        $ scene_manager.update_actor(the_person, position = "sitting")
                                        "She finally slides off of your dick and sits back down in her seat. She takes your hand and holds it tight in hers."
                                        the_person "Thank you [the_person.mc_title]. That was fun."

                                    else:
                                        "She gags and tries to pull back, but you hold your dick deep down her throat as you cum."
                                        $ climax_controller.do_clarity_release()
                                        "You pump your load out in big hot pulses. She twitches with each new deposit of semen, barely keeping herself in control."
                                        $ the_person.cum_in_mouth()
                                        $ scene_manager.update_actor(the_person, position = "kneeling1", emotion = "angry")
                                        "When you're entirely spent you let go of [the_person.possessive_title]'s head and sit back with a sigh."
                                        $ the_person.change_stats(love = -2, obedience = 1)
                                        "She pulls off your dick and gasps for breath. When she's recovered she glares up at you."
                                        mc.name "Sorry, I got carried away."
                                        $ scene_manager.update_actor(the_person, position = "sitting")
                                        "[the_person.title] slides back into her chair beside you."
                                        the_person "Yeah. A little. At least it wasn't boring..."
                                        "You lean back and zone out for the rest of the movie, feeling thoroughly spent."

                "Tell her to knock it off":
                    mc.name "I just want to watch a movie together. Can you at least try and pay attention?"
                    $ the_person.change_stats(happiness = -5, love = -1, obedience = 2)
                    "She pulls her hand back and sighs."
                    the_person "Aw, you're no fun."

        else:
            # She just annoys you by asking random questions
            the_person "Who is that again?"
            mc.name "He's working for the bad guy."
            the_person "Wait, I thought he was just with the good guys though."
            mc.name "He was lying. It's hard to explain."

        "Eventually the movie is over and you leave the theatre together."
        $ mc.location.show_background()
        $ scene_manager.update_actor(the_person, position = "default", lighting = standard_indoor_lighting[time_of_day])
        mc.name "So, did you like the movie?"
        the_person "It was okay. Let's try something else next time though."
        $ the_person.change_love(2, 60)

    the_person "There will be a next time, right?"
    mc.name "I'd love for there to be."
    $ the_person.change_happiness(10)

    if the_person.has_role(sister_role) or the_person.has_role(mother_role): #You live at home with those two, so it would be weird to kiss them goodnight.
        $ mc.change_locked_clarity(5)
        "She leans towards you and gives you a quick kiss."
        the_person "Let's head home then."
    else:
        if the_person in (aunt, cousin) and aunt_living_with_mc():
            "She leans towards you and gives you a quick kiss on the cheek."
            the_person "Let's head home then."
        # exclude Kaya story wise
        elif (the_person != kaya or the_person.home != sakari.home) and renpy.random.randint(0,100) < the_person.effective_sluttiness() + the_person.love + (mc.charisma * 5):
            $ mc.change_locked_clarity(5)
            "She leans towards you and gives you a quick kiss."
            $ the_person.call_dialogue("date_seduction")
            menu:
                "Go to [the_person.title]'s place":
                    $ downtown.show_background()
                    mc.name "That sounds like a great idea. Let's get a cab."
                    $ the_person.learn_home()
                    $ the_person.change_location(the_person.home)
                    "You flag a taxi and get in with [the_person.possessive_title]."
                    "After a short ride you pull up in front of her house. She leads you to the front door and invites you inside."
                    $ run_named_label("date_take_home_her_place", the_person, date_type = "movie")
                    return

                "Call it a night":
                    mc.name "I'd like to call it an early night today, but maybe I'll take you up on the offer some other time."
                    "Her taxi arrives. You give her a goodbye kiss and head home yourself."
        else:
            "She leans towards you and gives you a quick kiss on the cheek before saying goodbye."

    $ scene_manager.clear_scene()
    #Put them back at home after the event
    $ the_person.change_location(the_person.home)
    $ mc.change_location(bedroom)
    return "Advance Time"

label dinner_date_label(the_person):
    "You have a dinner date planned with [the_person.title]."
    menu:
        "Get ready for the date {image=time_advance}" if mc.business.has_funds(50):
            pass

        "Get ready for the date\n{menu_red}Requires: $30{/menu_red} (disabled)" if not mc.business.has_funds(50):
            pass

        "Cancel the date (tooltip)She won't be happy with you cancelling last minute.":
            "You get your phone out and text [the_person.title]."
            mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
            $ the_person.change_stats(happiness = -5, love = -5)
            the_person "I hope everything is okay. Maybe we can do this some other time then."
            return

    if mom_date_intercept_requirement(mom, the_person) and renpy.random.randint(0,100) < (mom.love):
        call mom_date_intercept(mom, the_person) from _call_mom_date_intercept_1
        if _return:
            $ clear_scene()
            return "Advance Time"

    $ clear_scene()
    "You get yourself looking as presentable as possible and head downtown."

    python:
        mc.stats.change_tracked_stat("Girl", "Dates", 1)
        mc.change_location(downtown)

        scene_manager = Scene()
        scene_manager.add_actor(the_person, the_person.decide_on_outfit(sluttiness_modifier = 0.2), emotion = "happy")

    "You meet up with [the_person.title] on time."
    the_person "So, where are we going tonight [the_person.mc_title]?"
    menu:
        "A cheap restaurant\n{menu_red}Costs: $50{/menu_red}":
            $ mc.business.change_funds(-50, stat = "Food and Drinks")
            the_person "It sounds cosy. Let's go, I'm starving!"
            $ renpy.show("restaurant", what = bg_manager.background("Restaurant_Background"), layer = "master")

        "A moderately priced restaurant\n{menu_red}Costs: $100{/menu_red}" if mc.business.has_funds(100):
            $ mc.business.change_funds(-100, stat = "Food and Drinks")
            $ the_person.change_stats(happiness = 5, love = 3, max_love = 70)
            the_person "It sounds nice. Come on, I'm starving and could use a drink."
            $ renpy.show("restaurant", what = bg_manager.background("Restaurant_Background"), layer = "master")

        "An expensive restaurant\n{menu_red}Costs: $300{/menu_red}" if mc.business.has_funds(300):
            $ mc.business.change_funds(-300, stat = "Food and Drinks")
            $ the_person.change_stats(happiness = 5, love = 5, max_love = 80)
            the_person "Oh, it sounds fancy! Well, I'm flattered [the_person.mc_title]."
            $ mc.change_location(fancy_restaurant)

        "A moderately priced restaurant\n{menu_red}Requires: $100{/menu_red} (disabled)" if not mc.business.has_funds(100):
            pass

        "An expensive restaurant\n{menu_red}Requires: $300{/menu_red} (disabled)" if not mc.business.has_funds(300):
            pass

    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.has_role(sister_role) or the_person.has_role(mother_role):
        if the_person.sluttiness >= 20:
            "You and [the_person.possessive_title] get to the restaurant and order your meals. She chats and flirts with you freely, as if forgetting you were related."
        else:
            "You and [the_person.possessive_title] get to the restaurant and order your meals."
            "She chats and laughs with you the whole night, but never seems to consider this more than a friendly family dinner."

    else:
        "You and [the_person.possessive_title] get to the restaurant and order your meals. You chat, flirt, and have a wonderful evening."

    call date_small_talk_label(the_person) from _dinner_date_small_talk_test_01

    "After dinner you decide to order dessert. [the_person.title] asks for a piece of cheesecake, then stands up from the table."
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person "I'm going to go find the little girls' room. I'll be back in a moment."
    $ scene_manager.hide_actor(the_person)
    "She heads off, leaving you alone at the table with her half-finished glass of wine."
    menu:
        "Add a dose of serum to her drink" if mc.inventory.has_serum:
            call give_serum(the_person) from _call_give_serum_21
            if _return:
                "You pour a dose of serum into her wine and give it a quick swirl, then sit back and relax."
                "[the_person.possessive_title!c] returns just as your dessert arrives."
            else:
                "You sit back and relax, content to just enjoy the evening. [the_person.possessive_title!c] returns just as your dessert arrives."

        "Add a dose of serum to her drink\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
            pass

        "Leave her drink alone":
            "You sit back and relax, content to just enjoy the evening. [the_person.possessive_title!c] returns just as your dessert arrives."

    $ scene_manager.show_actor(the_person)
    the_person "Ah, perfect timing!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "She sits down at the table and sips her wine, then takes an eager bite of her cheesecake. She closes her eyes and moans dramatically."
    $ play_moan_sound()
    the_person "Mmm, so good!"
    $ the_person.change_stats(happiness = mc.charisma, love = mc.charisma, max_love = 80)
    if the_person.has_role(sister_role) or the_person.has_role(mother_role):
        "At the end of the night you pay the bill and leave with [the_person.title]. The two of you travel home together."
        $ mc.change_location(hall)
        $ scene_manager.update_actor(the_person, position = "default")
        if renpy.random.randint(0,100) < the_person.sluttiness + the_person.love + (mc.charisma * 10): #She invites you back to her place.
            $ the_person.call_dialogue("date_seduction")
            menu:
                "Go to [the_person.title]'s room":
                    mc.name "I think I would. Lead the way."
                    $ mc.change_location(the_person.home)
                    "[the_person.possessive_title!c] leads you into her room and closes the door behind you."
                    #TODO: Mirror the real date stuff: ie she might get dressed up or start stripping down right away.
                    $ the_person.add_situational_slut("Romanced", 15, "What a wonderful date!")
                    call fuck_person(the_person, private = True) from _call_fuck_person_16
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.clear_situational_slut("Romanced")
                    call check_date_trance(the_person) from _call_check_date_trance_dinner_date

                    #TODO: add support for spending the night somewhere other than home.

                    "When you and [the_person.possessive_title] are finished you slip back to your own bedroom just down the hall."

                "Call it a night":
                    mc.name "I think we should just call it a night now. I've got to get up early tomorrow."
                    "She lets go of your hand and looks away."
                    the_person "Right, of course. I wasn't saying we should... I was just... Goodnight [the_person.mc_title]."
                    "She hurries off to her room."
        else:
            the_person "I had a great night [the_person.mc_title]. We should get out of the house and spend time together more often."
            mc.name "I think so too. Goodnight [the_person.title]."

    else:
        $ mc.change_location(downtown)
        $ scene_manager.update_actor(the_person, position = "default")
        "At the end of the night you pay the bill and leave with [the_person.title]. You wait with her while she calls for a taxi."
        if ((the_person == cousin and the_person.get_destination(time_slot = 4) == lily_bedroom)
            or (the_person == aunt and the_person.get_destination(time_slot = 4) == hall)):
            # aunt and cousin still live at your place
            the_person "I had a great night [the_person.mc_title], you're a lot of fun to be around. We should do this again."
            mc.name "It would be my pleasure."
            "You both get in the taxi and head home."
        # exclude Kaya story wise
        elif (the_person != kaya or the_person.home != sakari.home) and renpy.random.randint(0,100) < the_person.effective_sluttiness() + the_person.love + (mc.charisma * 5):
            $ the_person.call_dialogue("date_seduction") #She invites you back to her place to "spend some more time together". She's been seduced.
            menu:
                "Go to [the_person.title]'s place":
                    mc.name "That sounds like a great idea."
                    $ the_person.learn_home()
                    "You join [the_person.possessive_title] when her taxi arrives."
                    $ the_person.change_location(the_person.home)
                    "After a short ride you pull up in front of her house. She leads you to the front door and invites you inside."
                    $ run_named_label("date_take_home_her_place", the_person, date_type = "dinner")

                "Call it a night":
                    mc.name "I'd like to call it an early night today, but maybe I'll take you up on the offer some other time."
                    "Her taxi arrives. You give her a goodbye kiss and head home yourself."
        else: #She says goodnight to you here.
            the_person "I had a great night [the_person.mc_title], you're a lot of fun to be around. We should do this again."
            mc.name "It would be my pleasure."
            "[the_person.title]'s taxi arrives and she gives you a kiss goodbye. You watch her drive away, then head home yourself."

    $ scene_manager.clear_scene()
    $ the_person.change_location(the_person.home)
    $ mc.change_location(bedroom)
    return "Advance Time"

label bar_date_label(the_person):
    "You have a date at the bar planned with [the_person.title]."
    menu:
        "Get ready for the date {image=gui/heart/Time_Advance.png}" if mc.business.has_funds(50):
            pass

        "Get ready for the date\n{menu_red}Requires: $50{/menu_red} (disabled)" if not mc.business.has_funds(50):
            pass

        "Cancel the date (tooltip)She won't be happy with you cancelling last minute.":
            "You get your phone out and text [the_person.title]."
            mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
            $ the_person.change_stats(happiness = -5, love = -5)
            the_person "I hope everything is okay. Maybe we can do this some other time then."
            return

    $ clear_scene()
    "You get yourself looking as presentable as possible and head downtown."

    python:
        mc.stats.change_tracked_stat("Girl", "Dates", 1)
        mc.change_location(downtown)

        the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = 0.2))
        the_person.draw_person(emotion = "happy")
    "You meet her outside the bar. She walks up to you with a smile on her face."
    the_person "Alright, I love this place!"
    mc.name "Great! Let's head inside."
    $ mc.change_location(downtown_bar)
    call bar_date_main_label(the_person) from _bar_date_from_bar_invite_01
    return

label missed_date_label(the_appointment):
    $ the_person = appointment.person
    if the_person is None:
        return

    $ mc.start_text_convo(the_person)
    the_person "Hey [the_person.mc.name], we were supposed to have a date..."
    mc.name "I'm sorry [the_person.title], something important came up, I promise I will make it up to you."
    the_person "You better."
    $ the_person.change_stats(love = -2, happiness = -10)
    $ mc.end_text_convo()
    return

#TODO: Add a "date_take_home_your_place" where you take her to your house.

label date_take_home_her_place(the_person, date_type = None): #Your date went well and you go back to her place. This event starts off when you enter the door.
    $ the_person.learn_home()
    $ noisy_neighbor = False
    $ spend_the_night = False
    $ door_sex = False
    $ the_report = None

    # exclude her from any work duties
    $ the_person.change_location(the_person.home)
    $ mc.change_location(the_person.home)

    #date_type can be passed through to identify what type of date it was to trigger different dialogue
    if the_person.is_affair:
        $ mc.change_location(the_person.home)
        call fuck_date_event(the_person) from _call_fuck_date_event_1 #You're having an affair, leads to all of the normal affair stuff like being caught. #TODO: Make sure the date seduction dialogue leads into this properly.
        return "Advance Time"

    #First, check and see if we just fuck her as soon as we walk in the door
    elif her_place_door_fuck_check(the_person):
        $ mc.change_location(her_hallway)
        if the_person.arousal_perc >= 70:   #She comes after MC eagerly
            "You're barely in the door before [the_person.title] has her hands all over you."
            the_person "Fuck, I can't wait any longer [the_person.mc_title]! I've been thinking about this all night long!"
            $ mc.change_locked_clarity(20)
            $ the_person.draw_person(position = "kissing")
            "She puts her arms around you and kisses your neck, grinding her body against you."
            mc.name "Don't you want to go to your bedroom first?"
            the_person "I can't wait! I want you right here, right now!"
            menu:
                "Fuck her against her front door":
                    "You return the kiss. A moment later [the_person.possessive_title] has her hand down your pants, fondling your cock."
                    the_person "It's already hard! Oh my god... Come on, how do you want me?"
                    "You grab her ass and push her up against the wall, eliciting a moan from her as you begin to grind your body against hers."
                    call date_take_home_her_place_fuck_against_door_label(the_person) from _front_door_sex_01
                    $ the_report = _return
                    $ noisy_neighbor = the_report.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex)
                    $ door_sex = True

                "Insist on the bedroom":
                    pass

                "Turn her down and leave":
                    $ the_person.draw_person()
                    "You push her back firmly. She seems confused and tries to kiss you again, but you don't let her."
                    mc.name "Slow down, this is going way too fast for me. You need to get yourself under control."
                    the_person "What? But don't you want this too? Don't you want me?"
                    mc.name "I was thinking about it, but you're acting like the only thing you care about is getting at my cock!"
                    mc.name "Now I just want to head home. Maybe you can try this again some other night."
                    $ the_person.change_stats(happiness = -20, love = -(2 + the_person.opinion.taking_control))
                    if the_person.is_dominant:
                        the_person "If you felt like that why did you come home with me at all?"
                        the_person "Wasn't it obvious what was going to happen? Did I have to write it out for you?"
                        "She scoffs and backs away from you."
                        the_person "Whatever, if that's how you feel then there's no reason for you to stay here."
                        mc.name "Right. Have a good night [the_person.title]."
                        "She sighs unhappily and watches you leave."
                    else:
                        pass
                    "[the_person.possessive_title!c] deflates like a balloon. She steps back."
                    the_person "I... I'm sorry [the_person.mc_title], I didn't know you felt like that."
                    "An awkward silence hangs for a few moments before you speak again."
                    mc.name "I'm going to get going. Have a good night."
                    "[the_person.title] watches you leave, then sulks back inside her house."
                    return "Advance Time"
        else:
            "She pauses for a moment, looking at you. It is like she is waiting for you to do something."
            "Your libido spikes. You wonder how she would react if you just took her right here, up against her front door."
            menu:
                "Fuck right here":
                    "You step toward her. She lifts up her arms and puts them around your neck as you begin to make out."
                    $ mc.change_locked_clarity(20)
                    $ the_person.draw_person(position = "kissing")
                    "You push her body against the wall as you eagerly make out. She moans into your mouth as you grind your body into hers."
                    $ the_person.change_arousal(10)
                    call date_take_home_her_place_fuck_against_door_label(the_person) from _front_door_sex_02
                    $ the_report = _return
                    $ noisy_neighbor = the_report.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex)
                    $ door_sex = True
                "Wait for her to continue":
                    pass

    # Fuck in the hallway, or atleast present it as an option
    if door_sex:
        $ spend_the_night = her_place_spend_the_night_check(the_person, the_report)
        "You gather your clothes off the floor."
        the_person "That was good, but you really wore me out."
        if spend_the_night:
            the_person "Did you want to spend the night? I'm sure you're tired after that too..."
            menu:
                "Stay the night":
                    mc.name "Yeah that sounds good. I'm definitely worn out."
                    the_person "Ah, okay..."
                "Head out":
                    mc.name "Sorry, I can't stay."
                    the_person "Ah, that's okay..."
                    $ spend_the_night = False

        if not spend_the_night:
            the_person "You should probably get going then, I don't think I have the energy for anything else tonight!"
            mc.name "I understand. I'll see you around."
            "You quickly get dressed. You say goodnight to [the_person.possessive_title], then step out of her front door."
            return "Advance Time"

        #Next, determine if we interact with anyone else as we enter.
        if mc.location.person_count > 1 and noisy_neighbor: #There are other people in the apartment and you made a lot of noise.
            call date_take_home_her_place_noisy_roomate_door_fuck_label(the_person) from _noisy_sex_at_front_door_01

    # If we didn't fuck in the hallway, see if we interact with anyone first.
    elif mc.location.person_count > 1:
        call date_take_home_her_place_meet_roomate_label(the_person) from _one_night_stand_meet_flatmate_01
        return "Advance Time"

    # Next, decide what one night stand action we are going to take.
    # If the girl has lower scores, she may suggest a relatively innocent 'netflix and chill'
    # At higher obedience, she may offer to service MC
    # At higher love score, offer the chance to make out, then take things to the bedroom.
    # At high slut score, she changes into lingerie to seduce MC.
    $ finish_type = her_place_get_finish_type(the_person)

    #The next 4 sequences return True of if there is a possibility of spending the night, otherwise False
    if finish_type == "TV":
        call date_take_home_her_place_tv_finish_label(the_person) from _date_her_place_TV_finish_01
        $ spend_the_night = _return
    elif finish_type == "Slut":
        call date_take_home_her_place_lingerie_finish_label(the_person) from _date_her_place_lingerie_finish_01
        $ spend_the_night = _return
    elif finish_type == "Obedience":
        call date_take_home_her_place_service_offer_label(the_person) from _date_her_place_service_offer_finish_01
        $ spend_the_night = _return
    else:
        call date_take_home_her_place_romance_finish_label(the_person) from _date_her_place_romance_finish_01
        $ spend_the_night = _return


    if spend_the_night:
        $ run_named_label("date_her_place_spend_the_night_proposal", the_person)
        return

    "You get home and head for your bedroom."
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_her_place_01
    return

label date_take_home_her_place_fuck_against_door_label(the_person): #Use this label if you fuck her right inside her front door.
    mc.name "I'm going to pin you to your front door and fuck you there."
    if the_person.opinion.public_sex < 0:
        the_person "Oh... I don't know... I'm not sure I can stay quiet, what if the neighbors hear?"
        mc.name "That's the point!"
    elif the_person.opinion.public_sex < 2:
        the_person "Oh fuck... let's do it! I think I can stay quiet enough the neighbors won't hear..."
        "She doesn't seem particularly worried about it though."
    else:
        the_person "Oh fuck yes! Make me cum all over your big cock and make me scream for all my neighbors to hear!"
        "She seems more excited than ashamed at the idea of her neighbors hearing you have sex."
    if not the_person.vagina_available:
        $ the_person.strip_to_vagina(prefer_half_off = False, position = "kissing")
        "You quickly reach down and strip off anything between you and her cunt, making a small pile on the floor."
    "You take your pants and underwear off, kicking them off onto the floor. then you grab [the_person.possessive_title] and pick her up."
    $ the_person.draw_person(position = "against_wall")
    "You push her back against her front door, pinning her to it. She wraps her legs around you."
    "You move your hips back and forth a bit, your cock sliding along her slit."
    if the_person.has_taboo("vaginal_sex"):
        the_person "Oh my god... I can't believe we're about to have sex... let alone like this!"
        "Although her words are unsure, her legs pull your body into hers, making it clear she wants this as much as you do."
    elif the_person.has_taboo("condomless_sex"):
        the_person "Oh my god... I forgot to ask you to put a condom on..."
        if the_person.opinion.bareback_sex < 0:
            "She seems hesitant to let you continue bare, but doesn't make the jump to telling you to put one on."
        "Although her words are unsure, her legs pull your body into hers, making it clear she wants this as much as you do."
    "You push her slightly higher, then reach down and take your cock at the base, pointing it up."
    "Slowly, you let [the_person.title] slide down the side of her front door, your erection easily sliding inside of her pussy."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(20)
    $ play_moan_sound()
    "When you are fully inserted, she lets out a low moan. She holds on to your back with her arms and her legs urge you to go as deep as you can."
    if the_person.wants_creampie:
        the_person "Oh fuck that is so deep... Are you... are you going to cum inside me like this?"
    else:
        the_person "Oh fuck that is so deep... You aren't going to cum inside me like this, are you?"
    mc.name "Maybe. I haven't decided yet."
    "You give your hips a gentle thrust, getting a feel for the angle and penetration depth."
    the_person "MMMM... ahh... okay..."
    call fuck_person(the_person, private = True, condition = make_condition_apartment_door_sex(), start_position = against_wall, start_object = make_door(), skip_intro = True, girl_in_charge = False, position_locked = False, skip_condom = True) from _call_fuck_date_against_front_door_01
    $ the_report = _return
    return the_report

label date_take_home_her_place_noisy_roomate_door_fuck_label(the_person):
    pass
    # "In this label, as we walk with [the_person.title] to her bedroom, her flatmate complains about you having noisy sex in the hall."
    # "At the end of it, you go to her bedroom."
    return True

label date_take_home_her_place_meet_roomate_label(the_person):
    pass
    # "In this label, as we walk into [the_person.title]'s apartment, her flatmate is there and we meet her."
    # "At the end of this interaction, return True if we continue on the normal date path."
    # "Use False if we aren't, EG we decided to have a threesome, or the flatmate got pissed and chased us out."
    return True

label date_take_home_her_place_tv_finish_label(the_person):
    the_person "I hope you aren't too tired, I was thinking about watching a movie."
    mc.name "Sounds good to me."
    the_person "Okay!"
    $ popup_text = date_take_home_her_place_tv_finish_popup_text(the_person)
    $ show_popup_hint(popup_text)
    "You and [the_person.possessive_title] walk into her living room and sit down on her couch."
    $ the_person.draw_person(position = "sitting")
    "She grabs her remote and fires up a streaming service. Soon a movie is playing but you couldn't care less what is happening with it."
    $ the_person.draw_person(position = "sitting", display_transform = character_center_focus)
    "After the intro, [the_person.title] scoots over, her body now up against yours. She lays her head on your shoulder and softly sighs."
    the_person "Mmm, this is nice..."
    "You put your arm around her. You try to pay attention to the movie but it is impossible with her body up against yours."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(20)
    "Slowly, you let your hand slide down her shoulder, across her collarbone, and down to her breast..."
    #TODO go through and do all the  taboo breaks for this scene
    if the_person.is_willing(standing_grope) or the_person.is_willing(standing_finger):
        "She sighs when she feels you start to feel her up. She turns her head towards you."
        the_person "Mmm, that feels nice..."
        "She nuzzles up against you and starts to kiss your neck. You take it as a sign that she is eager for you to continue."
        $ mc.change_locked_clarity(20)
        $ the_person.change_arousal(5)
    else:
        "When you give her a little grope, she jumps, surprised at your forwardness."
        "She pushes your hand back up onto her shoulder."
        the_person "Ahhh, sorry, can we just watch the movie?"
        mc.name "Yes, of course..."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably see you out..."

        $ the_person.change_to_hallway()
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    if mc.sex_skills["Foreplay"] < 2:
        "You clumsily grope her tit for a few minutes while she gives occasional kisses on your neck."
        "You start to move your head down to meet her lips with yours, but she pulls back."
        the_person "Ahh, I don't want this to get too serious..."
        mc.name "Ah, of course..."
        "She puts her hand on yours. She lets you leave your hand on her chest, but she stops you from actively groping her and goes back to watching the movie."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably see you out..."
        $ the_person.change_to_hallway()
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    else:
        "You softly grope her, mixing it up, sometimes rubbing softly, sometimes teasing her nipple, and sometimes groping forcefully."
        "She moans into you as she begins to eagerly lick, suck, and kiss the side of your neck."
        "After several seconds, she stops."
        the_person "Oh god, that feels so good..."
        "You look down at her and see her looking at your lips. You lean forward and she pushes up, your lips meeting together."
        "She opens her mouth and you begin to make out with [the_person.possessive_title] while your hand keeps groping her."
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(10)
    if mc.sex_skills["Foreplay"] < 4:
        "You make out with [the_person.possessive_title] for several minutes."
        "Your tongues lash against each other, and you eagerly grope her chest."
        "However, things eventually start to slow down, and she eventually pulls back."
        the_person "Ahh, you make me feel good, but I don't want things to get too serious tonight..."
        "Your cock aches a bit in disappointment, but you don't want to push her into anything she doesn't want to do."
        mc.name "I understand."
        "She leans back against you, putting her head on your chest."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably see you out..."
        $ the_person.change_to_hallway()
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    else:
        "You make out passionately with [the_person.possessive_title] for several minutes."
        "You can feel the heat building between you two when you finally feel her hand on your body."
        "[the_person.title]'s hand has started to stroke your cock in your pants as you make out. You make sure to moan your approval into her mouth."
        "Thankfully, it appears that you are going to get far enough with [the_person.title] tonight to at least cum, from the way things are going."
        "She stops making out with you and looks down at your lap. She uses both hands and starts to fumble with your pants."
        "You lift up your hips as she pulls them down and off, your cock springing free."
        the_person "Oh fuck, you're so big!..."
        "She begins to stroke you with her hand again, this time skin on skin. She looks you in the eyes."
        if the_person.is_willing(blowjob):
            the_person "I want to taste it. I want to feel this monster in my mouth!"
        else:
            the_person "Fuck, I never do this but... I want to taste it! Can I taste it?"
        mc.name "Of course."
        "She gets up for a moment and turns, laying down on her stomach with her head on your lap."
        $ the_person.draw_person(position = "walking_away", display_transform = character_center_focus_flipped_test)
        "You put your hand on the back of [the_person.possessive_title]'s head as she slides her tongue up and down your cock a few times."
        if the_person.vagina_available:
            "You reach over with your other hand up between her legs."
        else:
            "You reach over with your other hand and slide it down her bottoms, along her backside and between her legs."
        "The angle is a little awkward but you manage to slide your middle finger along her pussy, feeling how wet she has gotten."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "After several seconds of teasing each other, [the_person.title] moves her mouth up to the tip of your cock, then opens her mouth and slides it inside."
        "At the same time, you slide your middle finger into her, causing a moan to reverberate around her now full mouth."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
    # if mc.max_energy < 140 or mc.sex_skills["Oral"] < 4: #Cum in her mouth
        "You can feel her ass pushing up, eagerly accepting your finger inside her."
        "[the_person.title]'s mouth working your cock is really turning you on, combined with her moans you can barely concentrate on fingering her."
        $ mc.change_arousal(15)
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "The angle of your hand around her back side makes it difficult for you to finger her properly, but you work it as best as you can."
        "Her mouth is really getting you turned on, you make sure to voice how good it feels."
        mc.name "Mmm, damn, that feels amazing [the_person.title]. I'm not going to last long if you keep going like that."
        the_person "Mmmmm, mmmhmmm..."
        "She doesn't stop sucking you, just murmurs her approval with a throaty moan."
        $ mc.change_arousal(25)
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "You do your best to make her feel good too, but after another minute of her oral attention, you feel yourself getting ready to orgasm."
        mc.name "Oh fuck, [the_person.title], that's it, I'm gonna cum!"
        $ mc.change_arousal(25)
        $ mc.change_locked_clarity(50)
        if the_person.facial_or_swallow() == "swallow":
            the_person "Mmmm..."
            "Her mouth keeps going, and you feel yourself peak and begin to cum into her mouth."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            "You fill her mouth with wave after wave of cum. She lets out a couple gasps and when you finish, you hear as she gulps it down."
            $ play_swallow_sound()
            "For a few blissful moments, you revel in your post orgasm haze."
        else:
            "Suddenly, her mouth pops off your cock with a pop, and she starts stroking you with her hand."
            the_person "Mmm, that's it, cum for me!"
            $ the_person.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            "You begin to orgasm. Her head is blocking your view, but she is letting you cover her face with your seed."
            "After several waves, your orgasm winds down, and for a few blissful moments, you revel in your post orgasm haze."
        $ the_person.draw_person(position = "missionary", display_transform = character_center_focus_flipped_test)
        "She turns over onto her back. When she does so, your pull you hand back from between her legs."
        the_person "Mmm, that was nice, but I'm almost there!"
        "She takes your hand puts it back between her legs. You easily slide two fingers inside of her."
        the_person "Mmmmmm, yessss!"
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "This position makes it much easier for you to finger her and to stimulate her g-spot. She closes her eyes and moans."
        the_person "Ohhhh, that's it [the_person.mc_title]... right there..."
        "Suddenly, you feel her whole body tense up and she has her own orgasm."
        $ the_person.change_arousal(35)
        $ the_person.have_orgasm()
        the_person "Yes!!! Oh!"
        "She body quivers as she orgasms. You eagerly finger her through the spasms until she starts to come down."
        "She lays there for several seconds with her head on your lap as she recovers."
        the_person "Wow... that was nice..."
        $ the_person.apply_planned_outfit()
        "She quickly hops up and cleans up her face and then comes back."
        $ the_person.draw_person(position = "missionary", display_transform = character_center_focus_flipped_test)
        "You watch the rest of the movie together with [the_person.possessive_title] while she lays her head in your lap."
        the_person "I should probably see you out..."
        $ the_person.change_to_hallway()
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False

    # else:   #Make her cum first
    #     "As you start to finger her, you realize the angle is a bit awkward, but you are determined to get her off."
    #     "[the_person.possessive_title!c]'c warm, wet mouth feels good, but you focus on her first."
    #     $ mc.change_arousal(15)
    #     $ mc.change_locked_clarity(50)
    #     $ the_person.change_arousal(15)
    #     "You realize there is a pillow on the side of the couch, so you quickly grab it. You have her stop for a second and slide it under her."
    #     "The pillow forces her hips up a little higher, giving you a better angle for penetrating her with your fingers, and so you continue."
    #     $ play_moan_sound()
    #     the_person "Mmmmmm.... slllck... mmmm.... slllp sllp"
    #     "She begins to moan around your cock along with the occasional slurping noises as she sucks you off."
    #     $ mc.change_arousal(15)
    #     $ mc.change_locked_clarity(50)
    #     $ the_person.change_arousal(25)
    #     the_person "Mmmmm!... OH fuck!"
    #     "After a particularly urgent moan, she pulls away from your cock and strokes it a couple times with her hand."
    #     the_person "Fuck, I'm... I'm gonna cum...!"
    #     $ the_person.change_arousal(25)
    #     $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus_flipped_test, emotion = "orgasm")
    #     "She looks up at you with her mouth open as she moans and begins to orgasm."
    #     $ the_person.have_orgasm(half_arousal = True)
    #     "Her eager moans are music to your ears as she cums from your touch."
    #     "After several seconds, her moans begin to slow down."
    #     the_person "Wow! That felt so good... I want to make you feel good too...!"
    #     $ the_person.draw_person(position = "walking_away", display_transform = character_center_focus_flipped_test)
    #     "She turns her face back to your cock. You feel her mouth lick up and down the sides a few times, then you feel her mouth engulf your erection."
    # if mc.sex_skills["Foreplay"] < 6 or mc.max_energy < 160:   #Cum in her mouth while she has a second orgasm
    #     "[the_person.title]'s orgasm has caused her to redouble her efforts to suck you off."
    #     "You keep fingering her as well. You aren't sure if you'll be able to get her off again, but you figure it is worth trying."
    #     $ mc.change_arousal(15)
    #     $ mc.change_locked_clarity(50)
    #     $ the_person.change_arousal(25)





    # else:   #She orgasms again and sets up to ride cowgirl




    # if mc.sex_skills["Vaginal"] < 6 or mc.max_energy < 180:    #Cowgirl orgasm





    # else:   #She orgasms a third time and is exhausted, MC rides her prone bone


    return False

label date_take_home_her_place_service_offer_label(the_person):
    $ mc.change_location(the_person.home)
    the_person "[the_person.mc_title], I just wanted to tell you I had a great time tonight."
    "She gives you a not so subtle wink."
    the_person "I was thinking we could go to my room, and I could show you just how much I appreciate it..."
    if the_person.is_willing(anal_standing) and the_person.is_willing(standing_doggy) and the_person.is_willing(blowjob):
        the_person "You can pick any hole you want and have your way with it. I wouldn't mind!"
    elif the_person.is_willing(anal_standing):
        the_person "I could bend over the side of the bed and let you pick a hole..."
        the_person "You could stick it in my butt if you want. I wouldn't mind!"
    elif the_person.is_willing(standing_doggy):
        the_person "I could bend over the side of the bed and let you fuck me as hard as you want. I wouldn't mind!"
    elif the_person.is_willing(blowjob):
        the_person "I could get on my knees and service you with a nice blowjob if you want. I don't mind!"
    else:
        the_person "I think we could figure out a way to make it feel good for you. I don't mind!"
    mc.name "That's a nice offer..."
    menu:
        "Get serviced":
            mc.name "I'd be an idiot to say no. Let's do it."
            the_person "Mmm, okay! My room is over here..."
            $ the_person.change_to_bedroom()
            mc.name "Alright, first things first. Get naked."
            the_person "Ah, yes sir..."
            $ the_person.strip_outfit(position = "stand3")
            $ mc.change_locked_clarity(20)
            "She stands in front of you, naked, waiting for your next order."
            $ the_person.add_situational_obedience("service_him", 20, "I want to make him feel good.")
            menu:
                "Fuck her Tits" if the_person.has_large_tits and the_person.is_willing(tit_fuck):
                    mc.name "Get on your knees. I want to have some fun with those amazing tits of yours."
                    "[the_person.possessive_title!c] quickly drops to her knees."
                    $ the_person.draw_person(position = "blowjob")
                    "She takes her considerable tits in her hands as you step over to her, looking up at you with a smile."
                    the_person "Go ahead. Use my tits to make yourself feel good!"
                    "You push your cock into the valley of her ample titflesh."
                    $ mc.change_locked_clarity(30)
                    "She begins to stroke your cock with her breasts, using her hands to control the tempo."
                    call fuck_person(the_person, private = True, start_position = tit_fuck) from _call_fuck_person_her_place_service_tit_fuck_01
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

                "Fuck her Mouth" if the_person.is_willing(blowjob):
                    mc.name "Get on your knees. I want to feel those pouty lips of yours around my cock."
                    "[the_person.possessive_title!c] quickly drops to her knees."
                    $ the_person.draw_person(position = "blowjob")
                    "She licks her lips, staring at your cock as you step over to her."
                    "[the_person.title] looks up at you and opens her mouth, silently waiting for you to use her."
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "You put your hand on the back of her head and gently guide her mouth onto your erection."
                    $ mc.change_locked_clarity(40)
                    "You feel a gently moan as your cock slides into her mouth. You let go of her head and she begins to suck you off."
                    call fuck_person(the_person, private = True, start_position = blowjob) from _call_fuck_person_her_place_service_blowjob_01
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

                "Fuck her Pussy" if the_person.is_willing(standing_doggy):
                    mc.name "Bend over your bed. Let me see what I'll be working with tonight."
                    "[the_person.possessive_title!c] quickly obeys, bending over her bed and preseting her ass to you."
                    $ the_person.draw_person(position = "standing_doggy")
                    "She looks back at you, hungrily, watching as you step over to her."
                    "You grab [the_person.title]'s hips and you push yourself up against her, grinding your dick against her ass."
                    $ the_person.change_arousal(10)
                    "She moans and grinds back against you a bit. Soon, you're ready for more."
                    "You use one hand to point your cock down and then push your hips forward, letting your cock slide inside her."
                    $ mc.change_locked_clarity(50)
                    "Once you are all the way in, you move your hand back to her hip and giver her a couple thrusts. Time to fuck this slut."
                    call fuck_person(the_person, private = True, start_position = standing_doggy, skip_condom = True) from _call_fuck_person_her_place_service_doggy_01
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

                "Fuck her Ass" if the_person.is_willing(anal_standing):
                    mc.name "Bend over your bed and show me these holes you mentioned."
                    "[the_person.possessive_title!c] quickly obeys, bending over her bed and preseting her ass to you."
                    $ the_person.draw_person(position = "standing_doggy")
                    "She looks back at you, hungrily, watching as you step over to her."
                    "You grab [the_person.title]'s hips and you push yourself up against her, grinding your dick against her ass."
                    $ the_person.change_arousal(10)
                    "She moans and grinds back against you a bit. Soon, you're ready for more."
                    mc.name "Do you have any lube?"
                    the_person "Oh, yeah! One second..."
                    "She reaches over to her bedside table and grabs some lubricant, quickly passing it to you."
                    "You quickly apply ample amounts. Your cock and her puckered hole now glisten from it."
                    "You use one hand to point your cock down and then push your hips forward."
                    "There are several moments of resistance as your erection slowly loosens and then pushes inside her sphincter."
                    $ mc.change_locked_clarity(70)
                    "When it finally gives way, you easily slide all the way in."
                    "You give [the_person.title] Time to fuck this slut."
                    call fuck_person(the_person, private = True, start_position = anal_standing, skip_condom = True) from _call_fuck_person_her_place_service_doggy_anal_01
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

                "Just fool around":
                    mc.name "Why don't we just fool around some? No need for anything specific."
                    the_person "Mmm, okay!"
                    $ the_person.change_to_bedroom()
                    call fuck_person(the_person, private = True) from _call_fuck_person_her_place_service_fool_around_01
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

            $ the_person.clear_situational_obedience("service_him")
        "Not tonight":
            mc.name "Sorry, I don't have time for that tonight, but I appreciate the offer."
            the_person "Huh? Really?"
            "She seems shocked at your answer, but is obedient enough to know not to second guess it."
            $ the_person.change_stats(happiness = -20, love = -2)
            the_person "Ok... well... maybe another time then..."
            mc.name "I should probably get going."
            the_person "Right..."
            "You say goodnight and leave, heading back to your place."
            return False

    $ spend_the_night = her_place_spend_the_night_check(the_person, the_report)

    call check_date_trance(the_person) from _call_check_date_trance_date_take_home_her_place_service_offer

    the_person "That was good, but you really wore me out."
    if spend_the_night:
        the_person "Did you want to spend the night? I'm sure you're tired after that too..."
        menu:
            "Stay the night" if not mc.has_event_tomorrow_morning:
                mc.name "Yeah that sounds good. I'm definitely worn out."
                the_person "Ah, okay..."
                return True
            "Stay the night\n{menu_red}Requires: Free Early Morning{/menu_red} (disabled)" if mc.has_event_tomorrow_morning:
                pass
            "Head out":
                mc.name "Sorry, I can't stay."
                the_person "Ah, that's okay..."

    the_person "I should probably see you out..."
    if the_person.tits_visible or the_person.vagina_visible:
        $ the_person.wear_bathrobe(show_dress_sequence = True)
    $ the_person.change_to_hallway()
    the_person "Thank you for a wonderful date [the_person.mc_title]."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "After giving you a long kiss, she steps back."
    $ the_person.draw_person(emotion = "happy")
    mc.name "You're welcome, [the_person.title]!"
    return False

label date_take_home_her_place_romance_finish_label(the_person):
    $ mc.change_location(the_person.home)
    #Normal date-turned-fuck session.
    the_person "Let me get you a drink and show you around."
    "She pours you a drink and leads you around her place. The tour ends with the two of you sitting on the couch in the living room."
    $ the_person.draw_person(position = "sitting")
    the_person "Well, what would you like to do now?"
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] leans closer to you and puts her hand on your thigh. It's obvious what she wants, but she's waiting for you to make the first move."
    menu:
        "Kiss her":
            "You put your drink aside, then put one hand on the back of [the_person.possessive_title]'s neck and pull her into a kiss."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            if not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0:
                "She returns the kiss eagerly."
            else:
                "She returns the kiss for a moment, then breaks away. Her lips hover, barely separated from yours."
                the_person "I shouldn't... My [the_person.so_title]..."
                "You kiss her again, and this time all resistance falls away."
            "After a long moment spent making out [the_person.title] pulls away."
            the_person "I think we'd be more comfortable in the bedroom, don't you?"
            $ the_person.draw_person(position = "walking_away")
            mc.name "I couldn't agree more."
            $ the_person.change_to_bedroom()
            $ the_person.add_situational_slut("Romanced", 10, "What a wonderful date!")
            $ the_person.add_situational_obedience("horny", 10, "Take me however you want...")
            "[the_person.possessive_title!c] leads you to her bedroom and starts to undress."
            $ the_person.strip_to_underwear()
            call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_104
            $ the_person.clear_situational_obedience("horny")
            $ the_person.clear_situational_slut("Romanced")
            $ the_person.call_dialogue("sex_review", the_report = _return)
            $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
            the_person "That was good, but you really wore me out."
            call check_date_trance(the_person) from _call_check_date_trance_date_take_home_her_place_romance_finish

            if spend_the_night:
                the_person "Did you want to spend the night? I'm sure you're tired after that too..."
                menu:
                    "Stay the night" if not mc.has_event_tomorrow_morning:
                        mc.name "Yeah that sounds good. I'm definitely worn out."
                        the_person "Ah, okay..."
                        return True
                    "Stay the night\n{menu_red}Requires: Free Early Morning{/menu_red} (disabled)" if mc.has_event_tomorrow_morning:
                        pass
                    "Head out":
                        mc.name "Sorry, I can't stay."
                        the_person "Ah, that's okay..."

            $ the_person.wear_bathrobe(show_dress_sequence = True)
            $ the_person.change_to_hallway()
            "When you and [the_person.title] are finished you get dressed and she walks you out."
            the_person "Thank you for a wonderful date [the_person.mc_title]."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "After giving you a long kiss, she steps back."
            $ the_person.draw_person(emotion = "happy")
            mc.name "You're welcome, [the_person.title]!"

        "Go home":
            mc.name "It's been a fun evening, but I need to be going soon. I hope we can do this again some time though."
            $ the_person.change_happiness(-5)
            "[the_person.possessive_title!c] seems a little disappointed, but she smiles politely."
            if not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0:
                the_person "Of course. It's getting late, I should probably be going to bed as well."
            else:
                the_person "Of course, that's fine. My [the_person.so_title] probably wouldn't like it that I have other men visiting anyways."

            the_person "I had a fun time, we should do this again."
            mc.name "I think I'd like that."
            "You finish your drink and say goodnight to [the_person.title]."
            return False
    return False

label date_take_home_her_place_lingerie_finish_label(the_person):
    $ mc.change_location(the_person.home)
    the_person "Let me get you a drink and show you around."
    "She pours you a drink and leads you around her place. The tour ends in the living room."
    the_person "Have a seat and enjoy your drink, I'll be back in a moment."
    $ clear_scene()
    if the_person.opinion.not_wearing_anything > the_person.opinion.lingerie:
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True) #She's wearing nothing at all. nothing at all. nothing at all...

    elif the_person.opinion.lingerie >= 0:
        $ the_person.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness + 20, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person)), update_taboo = True) #She's just wearing lingerie for the evening.

    else: #She doesn't like being nude or wearing lingerie, so just strip her to her underwear
        $ the_person.outfit.strip_to_underwear()
    "You sit down on the couch and relax while you wait for [the_person.possessive_title]. A few minutes later she calls out for you."
    the_person "[the_person.mc_title], could you come here?"
    "You down the rest of your drink and leave the empty glass behind, following the sound of her voice."
    mc.name "On my way. Is everything okay?"
    the_person "Everything's fine, just get in here!"
    "Her voice is coming from the other side of a partially opened door. You nudge it open and step inside."
    $ the_person.draw_person(position = "sitting")
    $ mc.change_locked_clarity(15)
    $ the_person.change_to_bedroom()
    "It's the master bedroom, and [the_person.possessive_title] is sitting at the foot of the bed."
    the_person "I thought we might be more comfortable in here. I got changed for you, too."
    $ the_person.draw_person()
    "She stands up and steps closer to you, leaning in for a kiss."
    menu:
        "Kiss her":
            if the_person.has_taboo("kissing"):
                $ the_person.call_dialogue("kissing_taboo_break")
                $ the_person.break_taboo("kissing")

            "You put your arm around her waist and pull her against your body. She kisses you passionately, and you return the gesture in full."
            $ the_person.add_situational_slut("horny", 10, "I really need this...")
            call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_17
            $ the_person.clear_situational_slut("horny")
            $ the_person.call_dialogue("sex_review", the_report = _return)
            $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
            the_person "That was good, but you really wore me out."
            call check_date_trance(the_person) from _call_check_date_trance_date_take_home_her_place_lingerie_finish
            if spend_the_night:
                the_person "Did you want to spend the night? I'm sure you're tired after that too..."
                menu:
                    "Stay the night":
                        mc.name "Yeah that sounds good. I'm definitely worn out."
                        the_person "Ah, okay..."
                        return True
                    "Head out":
                        mc.name "Sorry, I can't stay."
                        the_person "Ah, that's okay..."
            $ the_person.wear_bathrobe(show_dress_sequence = True)
            $ the_person.change_to_hallway()
            "When you and [the_person.title] are finished you get up and she walks you out."
            the_person "Thank you for a wonderful date [the_person.mc_title]."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "After giving you a long kiss, she steps back."
            $ the_person.draw_person(emotion = "happy")
            mc.name "Goodnight, [the_person.title]!"

        "Turn her down":
            mc.name "[the_person.title], we shouldn't do this..."
            the_person "What? You're not interested in me?"
            $ the_person.change_stats(happiness = -20, love = -2)
            "She steps back, hurt by your rejection."
            mc.name "No, I am, it's just that tonight isn't the right night for this. I'm sorry."
            the_person "Oh, I... I'm sorry, I shouldn't have been so eager."
            "An awkward silence fills the room."
            mc.name "I should, um... I should probably get going."
            the_person "Right, that's a good idea... Maybe some other time we can do this again?"
            mc.name "Yeah, I think I'd like that."
            "You say goodnight and leave, heading back to your place."
            return False
    return

label date_her_place_spend_the_night_proposal(the_person):
    # Use this label to propose the overnight, and the code to actually trigger it.
    # This scene assumes that we are in her room and ready to lay down and go to sleep.
    "[the_person.title] turns and lays down in her bed, and you climb in beside her."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title!c] turns her back to you. You cuddle up with her, wrapping your arm around her."
    mc.name "Goodnight..."
    the_person "Night..."
    $ the_person.next_day_outfit = the_person.outfit # she wakes up with these clothes -> wakeup event chooses next day outfit
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_one_night_stand_01
    $ run_named_label("date_her_place_morning_after_wakeup_label", the_person)
    return

label date_her_place_morning_after_wakeup_label(the_person):
    #This label does not start until the actual wakeup time
    $ the_person.draw_person(position = "walking_away")
    "You slowly start to wake up. However, you aren't in your own room."
    "When you stir, the woman next to you also awakens."
    "A flash of recollection hits you. You had a date with her last night and wound up back at her place. It must have gone well."
    # First, we wakeup. Initial reactions to waking up next to our one night stand.
    # Possible emotions: regret, infatuation, love, awkwardness, no emotion
    # Regret should be for a true one night stand where things went too far too fast.
    # Awkward for when she doesn't necessarily regret it but still doesn't really know MC
    # Infatuation if she had a great time and wants to do it again sometime
    # Love if she has maybe done this before? Or otherwise this wasn't out of nowhere, and this was good for her.
    # No emotion if she is just slutty and was doing slutty things.
    if the_person.love >= 60:   #She loves MC
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] stretches, then looks back at you."
        the_person "Ahhh, good morning [the_person.mc_title]."
        "She leans her body back against yours. You take the opportunity to hug her tightly from behind. She gives a sigh."
        $ the_person.change_love(2, 80)
        the_person "Waking up next to you is nice..."
        "After a few more moments, she starts to get up, so you get up also."

    elif the_person.effective_sluttiness() >= 40: #She is just a slut doing slut things
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] stretches, then looks back at you."
        the_person "Oh! Good morning [the_person.mc_title]. I thought I felt something extra nice this morning..."
        "She pushes her body back against you. Her ass grinds up against your crotch suggestively..."
        $ mc.change_locked_clarity(20)
        "She sighs."
        the_person "Well, I guess it is time to get up..."
        "After a few more moments, she starts to get up, so you get up also."

    elif the_person.love >= 30:   #Infatuation
        "[the_person.title] stretches, then startles when you start to move behind her."
        $ the_person.draw_person(position = "back_peek")
        the_person "OH! [the_person.mc_title]? That's... That's right... You came over last night..."
        "She looks back at you a bit sheepishly, but you notice a smile on the corners of her lips."
        the_person "I ummm... I... Good... Morning?"
        mc.name "Good morning, [the_person.title]."
        $ the_person.change_love(2, 60)

    elif (the_person.days_since_event("day_met") < 5 and the_person.love < 20) or the_person.love <= 0:   #Regret
        if the_person.days_since_event("day_met") < 3:
            "Damn, you can hardly even remember her name. What was it?"
            "It takes you several seconds... [the_person.title]... Right?"
        "She doesn't move, but lets out a sigh as you start to get up."
        the_person "Ah... Morning [the_person.mc_title]."
        $ the_person.draw_person(position = "missionary")
        "She rolls over on her back after you get up."
        the_person "I must have had way too much to drink last night."
        mc.name "You rather enjoyed last night, from what I remember [the_person.title]."
        $ the_person.change_love(-2)
        "She flinches when you say her name."
        the_person "Ugh, I won't make that mistake again."
        "She starts to get up as well."
    else:   #Just awkward wakeup.
        "[the_person.title] stretches, then startles when you start to move behind her."
        $ the_person.draw_person(position = "back_peek")
        the_person "WHOA! I... Wow I must have had a lot to drink last night..."
        "There's a long, awkward silence."
        $ the_person.change_happiness(-2)
        mc.name "I ummm... I should probably get going."
        the_person "Yeah..."
        "Silently, you both get up."

    $ mc.phone.register_number(the_person)
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "stand4")
    "Once you are both dressed, you head out."
    $ mc.change_location(downtown)
    $ clear_scene()
return


label shopping_date_intro(the_person, skip_intro = False, skip_outro = False):
    if not skip_intro: #Skip the intro if another event (like Lily's LTE) already provides the context. Assumes you're talking to your girlfriend/paramour
        mc.name "Want to hang out for a while? I was going to head the mall and wander around for a while."
        if the_person.is_employee and mc.business.is_open_for_business:
            the_person "Right now? I had some work to get done, but I could take a break if you want me to."
            menu:
                "Take some time off":
                    #TODO: Make sure her production isn't added for the turn
                    mc.name "You've been doing a great job, you deserve some time off."
                    $ the_person.change_obedience(-2)
                    the_person "Alright, you're the boss. Some time at the mall sounds fun!"

                "Stay at work":
                    mc.name "You're right, you've got more important things to do at the lab."
                    the_person "Come see me after work, I should be free then."
                    return
        else: #She's not your employee, or it's outside of work hours.
            the_person "A shopping trip sounds like fun, and I've always got time for you [the_person.mc_title]."
            the_person "Come on, let's go!"

        "You and [the_person.possessive_title] head to the mall together."

    $ mc.change_location(mall)
    $ should_advance_time = True
    $ the_person.set_event_day("last_shopping_day")

    call shopping_date_loop(the_person) from _call_shopping_date_loop_first_choice
    if _return == "leave_early":
        $ should_advance_time = False
    else:
        call shopping_date_loop(the_person, _return) from _call_shopping_date_loop_second_choice

    if not skip_outro:
        $ mc.change_location(mall)
        $ the_person.draw_person()
        "You walk with [the_person.possessive_title] to the mall entrance."
        the_person "This was fun [the_person.mc_title], maybe we can do it again some time."
        mc.name "Yeah, I hope so too."
        $ clear_scene()
        "She waves goodbye and you part ways outside of the mall."


    if should_advance_time:
        call advance_time() from _call_advance_time_shopping_date_intro
    return

label shopping_date_loop(the_person, previous_choice = None):
    if previous_choice is not None:
        the_person "So, what do you want to do now?"
    else:
        the_person "What should we do first?"

    menu:
        "Get some food" if previous_choice != "Food":
            call shopping_date_food(the_person) from _call_shopping_date_food
            return "Food"

        "Go clothes shopping" if previous_choice != "Overwear":
            call shopping_date_overwear(the_person) from _call_shopping_date_overwear
            return "Overwear"

        "Go lingerie shopping" if previous_choice != "Underwear":
            call shopping_date_underwear(the_person) from _call_shopping_date_underwear
            return "Underwear"

        "Get her hair done" if previous_choice != "Hair":
            call shopping_date_hair(the_person) from _call_shopping_date_hair
            return "Hair"
        #
        # "Look at electronics." if previous_choice != "Electronics": #TODO: Write these other options when we have time
        #     call shopping_date_electronics(the_person)
        #     return "Electronics"
        #
        # "Visit the sex store." if previous_choice != "Sex_Store":
        #     call shoppint_date_sex_store(the_person)
        #     return "Sex_Store"

        "Head home":
            if previous_choice is None:
                mc.name "I just remembered, I have an important appointment today!"
                the_person "You do? But we just got here!"
                mc.name "I'm really sorry, I'll make it up to you some other time."
                $ the_person.change_stats(love = -1, obedience = -2)
                "[the_person.possessive_title!c] seems disappointed, but nods her understanding."
            else:
                mc.name "That was fun [the_person.title], but I'm going to have to cut this trip a little short."
                mc.name "I've got some work to get back to."
                "She smiles and nods."
                the_person "Okay. Maybe we can do this again some time."
            return "leave_early"

    $ mc.stats.change_tracked_stat("Girl", "Shopping", 1)
    # TODO: Asks the player what they want to do at the mall, if they are in control. "previous_choice" cannot be picked."
    # TODO: Give the girl the chance to take control. Girls with Low obedience demand to do things, moderate obedience ask to do something specifically, and high obedience always give you complete control.
    # TODO: If she has control for one round it's less likely for her to have control for the next, and if you take control for the first she'll be more likely to take control and want to do something specifically.
    return

label shopping_date_food(the_person):
    mc.name "Let's head over to the food court, I could use a bite."
    the_person "Sounds like a plan."
    $ mc.change_location(mall)
    $ the_person.draw_person(position="walking_away")
    "You lead [the_person.possessive_title] to the crowded food court. She looks around and hums as she decides what to eat."
    #TODO: Have a list of random food places to arbitrarily chose from
    menu:
        "Pay for her [StringInfo.time_of_day_food_string]\n{menu_red}Costs: $40{/menu_red}" if mc.business.has_funds(40):
            $ the_person.draw_person()
            mc.name "[StringInfo.time_of_day_food_string] is on me, what do you want me to get you?"
            $ the_person.change_stats(happiness = 10, love = 1, max_love = 40)
            the_person "Aw, thanks [the_person.mc_title]..."
            "She thinks for a while, then points to a fast food place."
            the_person "Get me something that looks good from there."
            mc.name "Okay, you go find us a place to sit and I'll be over soon."
            "[the_person.title] nods and heads off into the crowd to find a free table."
            $ clear_scene()
            "You get in line and order food for yourself and [the_person.possessive_title]. It takes a few minutes until your order number is called."
            $ mc.business.change_funds(-40, stat = "Food and Drinks")
            "You collect your order and move over to the condiment station."
            menu:
                "Add serum to her drink" if mc.inventory.has_serum:
                    call give_serum(the_person) from _call_give_serum_22
                    if _return is None:
                        "You reconsider, and bring [the_person.title]'s food back to her without any additions."
                    else:
                        "You pour a dose of serum into [the_person.title]'s drink and swirl it in."

                "Add serum to her drink\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                    pass
                "Leave her food alone":
                    pass
            "You wander around the food court, until you spot [the_person.possessive_title]."
            $ the_person.draw_person(position = "sitting")
            "She waves you over to the table she's saved."
            the_person "Thank you [the_person.mc_title], this looks great!"
            $ the_person.change_love(1, max_amount = 40)
            "You eat [StringInfo.time_of_day_food_string] together, chatting idly about nothing important."

        "Pay for her [StringInfo.time_of_day_food_string]\n{menu_red}Costs: $40{/menu_red} (disabled)" if not mc.business.has_funds(40):
            pass

        "Just buy your own [StringInfo.time_of_day_food_string]\n{menu_red}Costs: $20{/menu_red}" if mc.business.has_funds(20):
            $ the_person.draw_person()
            mc.name "See anything you like?"
            the_person "Not right away... I'm going to wander around a bit, you go ahead and order something."
            $ clear_scene()
            "[the_person.possessive_title!c] moves off into the crowd. You pick a fast food place for yourself and order some food."
            $ mc.business.change_funds(-20, stat = "Food and Drinks")
            "When you get your order you find a table, and a couple of minutes later [the_person.title] shows up with her own [StringInfo.time_of_day_food_string]."
            $ the_person.draw_person(position = "sitting", emotion = "happy")
            the_person "Hope you weren't waiting long, it just all looked so good!"
            $ the_person.change_love(1, max_amount = 40)
            "You eat [StringInfo.time_of_day_food_string] together, chatting idly about nothing important."

        "Just buy your own [StringInfo.time_of_day_food_string]\n{menu_red}Costs: $20{/menu_red} (disabled)" if not mc.business.has_funds(20):
            pass

        "Don't buy anything":
            mc.name "Actually, I'm not as hungry as I thought I was."
            the_person "Oh, alright. Let's get shopping then!"

    $ the_person.draw_person()
    return

label shopping_date_overwear(the_person, skip_intro = False):
    if not skip_intro:
        mc.name "Let's do some window shopping. If you see any cute outfits you could try them on."
        the_person "That sounds fun, and I think I know the first place we should check out. Follow me!"
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] takes your hand and leads you through the mall."
        #TODO: List of random store names (and maybe have each place have a specific set of clothing they can sell in the future)
    the_person "Here, doesn't it have the cutest stuff? Let's go look around!"
    $ mc.change_location(clothing_store)
    "[the_person.possessive_title!c] brings you into one of the dozens of clothing stores in the mall."
    the_person "Oh, look at this! I should try this on... and this... Check if they have this one in my size!"
    $ the_person.change_happiness(10)
    menu:
        "Pick out an outfit for her" if the_person.obedience >= 110:
            call outfit_master_manager(show_outfits = False, show_underwear = False, start_mannequin = the_person) from _call_outfit_master_manager
            if isinstance(_return, Outfit):
                $ new_overwear = _return
                "You move between the racks and pick out a few pieces for [the_person.title]."
                $ the_person.draw_person()
                the_person "What have you got there?"
                mc.name "Something for you. I think it'll look good on you."
                "She takes the clothes from you and smiles."
                the_person "Well let's go see!"
                "She leads you to the changing rooms at the back of the store."

            else:
                "You can't find anything you like for [the_person.title], but she comes to you with plenty of clothing for her to hold."
                $ the_person.draw_person()
                "When she feels like she had collected enough she leads you to the changing rooms at the back of the store."
                $ new_overwear = default_wardrobe.get_random_appropriate_overwear(sluttiness_limit = the_person.sluttiness, sluttiness_min = the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person))

        "Pick out an outfit for her\n{menu_red}Requires: 110 Obedience{/menu_red} (disabled)" if the_person.obedience < 110:
            pass

        "Let her pick out an outfit":
            "She moves between the racks of clothes, picking out her favourites and handing them over to you to hold."
            $ the_person.draw_person()
            "When she feels like she had collected enough she leads you to the changing rooms at the back of the store."
            $ new_overwear = default_wardrobe.get_random_appropriate_overwear(sluttiness_limit = the_person.sluttiness, sluttiness_min = the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person))

    call shopping_date_changing_room(the_person, new_overwear, "overwear") from _call_shopping_date_changing_room
    $ (wants_outfit, new_overwear) = _return

    if wants_outfit and isinstance(new_overwear, Outfit):
        "You and [the_person.possessive_title] move to the cashier at the front of the store."
        $ cost = (10 * new_overwear.item_count) + (5 * new_overwear.overwear_slut_score)
        menu:
            "Pay for the outfit\n{menu_red}Costs: $[cost]{/menu_red}" if mc.business.has_funds(cost):
                mc.name "Let me get this for you [the_person.title]."
                "She smiles at you as you pull out your wallet."
                $ the_person.change_stats(love = 2, obedience = 1, max_love = 40)
                $ mc.business.change_funds(-cost, stat = "Shopping")
                the_person "That's so sweet of you [the_person.mc_title]. Thank you!"

            "Pay for the outfit\n{menu_red}Requires: $[cost]{/menu_red} (disabled)" if not mc.business.has_funds(cost):
                pass

            "Let [the_person.title] pay":
                "She waits for the outfit to be rung up by the cashier, then hands over a credit card and pays."

        $ the_person.wardrobe.add_overwear_set(new_overwear)
        "Purchase in hand, the two of you leave the store and head back into the mall."

    else:
        "[the_person.possessive_title!c] drops the outfit into a return bin nearby, and the two of you leave the store."

    $ the_person.change_love(1, max_amount = 40)
    $ new_overwear = None
    "[the_person.title] seems to have enjoyed your shopping trip together."
    return

label shopping_date_underwear(the_person):
    mc.name "There was a store I saw that might have something you'd like. Let's do a little shopping."
    the_person "That sounds fun! Which store did you want to visit?"
    "You take her hand and lead her through the mall to a small lingerie store."
    mc.name "Here it is. You can buy yourself something pretty to wear."
    if the_person.effective_sluttiness("underwear_nudity") < 15:
        "[the_person.possessive_title!c] seems unsure for a moment, then shakes her head."
        the_person "I don't want to shop for that kind of... stuff with you [the_person.mc_title]!"
        the_person "Come on, let's just go look for some normal clothes. There's a place right over there."
        "It doesn't seem like you can change her mind, so you follow her to the opposite side of the hall into a normal clothing store."
        call shopping_date_overwear(the_person, skip_intro = True) from _call_shopping_date_overwear_1
        return
    elif the_person.has_taboo("underwear_nudity") and the_person.is_family:
        "[the_person.possessive_title!c] seems unsure for a moment."
        the_person "Are you sure you want to go into a place like that with me?"
        the_person "Wouldn't it be embarrassing for you?"
        mc.name "Not at all. It's just clothing, right?"
        the_person "Yes... Just clothing... Okay, let's go in."
        "[the_person.title] seems unconvinced, but she finds her courage and leads the way."
    else:
        the_person "That's a good idea, let's go!"
        "She leads the way and hurries in."

    $ mc.change_location(clothing_store)

    menu:
        "Pick out some lingerie for her" if the_person.obedience >= 120:
            "You move between the racks of bras and display boxes of panties, picking out a cute little outfit for [the_person.possessive_title]."
            call outfit_master_manager(show_outfits = False, show_overwear = False, show_underwear = True, start_mannequin = the_person) from _call_outfit_master_manager_3
            if isinstance(_return, Outfit):
                $ new_underwear = _return
                mc.name "Here you go [the_person.title]. You should try this on."
                "You hand the collection of underwear to [the_person.possessive_title]."
                if new_underwear.underwear_slut_score > the_person.effective_sluttiness(): #TODO: Check to make sure it actually covers her
                    "She glances at it and scoffs."
                    the_person "I couldn't wear this, it's..."
                    mc.name "Just try it on. Maybe you'll like it more when you're wearing it."
                    "She sighs and shrugs."
                    the_person "Okay, I'll try it. No promises though..."
                else:
                    "She takes it and looks it over."
                    the_person "Hmm, this could be nice..."
                the_person "The changing rooms are at the back."

            else:
                if the_person.effective_sluttiness() > 50 or the_person.opinion.lingerie > 0:
                    $ new_underwear = lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person))
                else:
                    $ new_underwear = default_wardrobe.get_random_appropriate_underwear(the_person.sluttiness, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person))
                "[the_person.title] moves between the racks of bras and display boxes of panties, picking out a few choice pieces."
                the_person "I want to go try some of this on. The changing rooms are at the back."


        "Pick out some lingerie for her\n{menu_red}Requires: 120 Obedience{/menu_red} (disabled)" if the_person.obedience < 120:
            pass

        "Let her do her own shopping":
            if the_person.effective_sluttiness() > 50 or the_person.opinion.lingerie > 0:
                $ new_underwear = lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person))
            else:
                $ new_underwear = default_wardrobe.get_random_appropriate_underwear(the_person.sluttiness, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person))
            "[the_person.title] moves between the racks of bras and display boxes of panties, picking out a few choice pieces."
            the_person "I want to go try some of this on. The changing rooms are at the back."


    call shopping_date_changing_room(the_person, new_underwear, "underwear") from _call_shopping_date_changing_room_1
    $ (wants_outfit, new_underwear) = _return

    if wants_outfit and isinstance(new_underwear, Outfit):
        "You and [the_person.possessive_title] move to the cashier at the front of the store."
        $ cost = (5 * new_underwear.item_count) + (15 * new_underwear.overwear_slut_score)
        menu:
            "Pay for the lingerie\n{menu_red}Costs: $[cost]{/menu_red}" if mc.business.has_funds(cost):
                mc.name "Let me get this for you [the_person.title]."
                "She smiles at you as you pull out your wallet."
                $ the_person.change_stats(love = 2, obedience = 1, max_love = 40)
                $ mc.business.change_funds(-cost, stat ="Shopping")
                the_person "That's so sweet of you [the_person.mc_title]. Thank you!"

            "Pay for the lingerie\n{menu_red}Requires: $[cost]{/menu_red} (disabled)" if not mc.business.has_funds(cost):
                pass

            "Let [the_person.title] pay":
                "She waits for the lingerie to be rung up by the cashier, then hands over a credit card and pays."

        "Lingerie in hand, [the_person.possessive_title] leads you out of the store and back into the busy mall."
        $ the_person.wardrobe.add_underwear_set(new_underwear)

    else:
        "[the_person.possessive_title!c] drops the underwear into a return bin nearby, and the two of you leave the store."

    $ new_underwear = None
    $ the_person.change_stats(happiness = 5 + the_person.opinion.lingerie, love = 1, max_love = 40)
    "[the_person.title] seems to have enjoyed shopping for lingerie with you."
    return

label shopping_date_changing_room(the_person, new_outfit, changing_type):
    python:
        # safeguard for no outfit
        if not isinstance(new_outfit, Outfit) or new_outfit.item_count < 2:
            if changing_type == "underwear":
                new_outfit = default_wardrobe.get_random_appropriate_underwear(sluttiness_limit = the_person.sluttiness, guarantee_output = True)
            else:
                new_outfit = default_wardrobe.get_random_appropriate_overwear(sluttiness_limit = the_person.sluttiness, guarantee_output = True)

        old_location = mc.location
        waiting_outside = True
        wants_outfit = False

    if the_person.effective_sluttiness("underwear_nudity") > 40:
        "[the_person.possessive_title!c] steps into one of the changing rooms, then pauses and looks back at you."
        the_person "Come on in, I want your opinion. Quick, before someone else shows up."
        menu:
            "Join her in the changing room":
                $ waiting_outside = False
                "You glance over your shoulder to make sure you're actually alone, then follow [the_person.title] into the changing room."
                $ mc.change_location(changing_room)
                "She pulls the curtain closed behind you."

            "Wait outside":
                mc.name "I don't want us to get kicked out. I'm sure you'll manage without me."
                $ clear_scene()
                "[the_person.title] shrugs and pulls the curtain closed."
                the_person "Your loss!"
    else:
        the_person "Wait here, I'm going to try some of this on."
        $ clear_scene()
        "[the_person.possessive_title!c] slips into one of the changing rooms and pulls the curtain closed behind her."
        "You can see her feet move as she manoeuvres around the small room."
        menu:
            "Step into the changing room": #Effectively this is the peek, and sometimes you get thrown out.
                $ mc.change_location(changing_room)
                if the_person.effective_sluttiness() > 20: #Great for taboo breaking.
                    $ waiting_outside = False
                    $ the_person.outfit.strip_to_underwear()
                    $ the_person.draw_person(position = "back_peek", emotion = "angry")
                    if changing_type == "overwear":
                        if the_person.has_taboo("underwear_nudity"):
                            the_person "Occupied! [the_person.mc_title]?!"
                            "She turns her back to you, trying to shield her body from your view."
                            mc.name "I thought this would be a little faster way for me to give some advice."
                            mc.name "We should be quiet though, or someone else might hear us."
                            "[the_person.possessive_title!c] is still for a moment, then sighs, lowers her hands, and turns around to face you."
                            $ the_person.draw_person()
                            the_person "Well, I guess it's fine as long as I keep my underwear on."
                            the_person "Just... look away, okay? You shouldn't be seeing me undressed like this..."
                            $ the_person.update_outfit_taboos()
                        else:
                            the_person "Occupied! I..."
                            "[the_person.possessive_title!c] sighs and lowers her hands to her side."
                            $ the_person.draw_person()
                            the_person "Oh, it's just you."
                            mc.name "I thought this would be a little faster way for me to give some advice."
                            the_person "Okay, but you need to be quiet. Have a seat over there."
                            the_person "And try not to stare, okay? You shouldn't be seeing me undressed like this..."

                    else:
                        if the_person.has_taboo(["bare_tits", "bare_pussy"]):
                            the_person "Occupied! [the_person.mc_title]?!"
                            "She turns her back to you, trying to shield her body from your view."
                            the_person "I'm getting changed [the_person.mc_title], can you wait outside?"
                            mc.name "I can't give you my opinion if I'm out there. We need to be quiet though, or someone will catch us."
                            "[the_person.possessive_title!c] is still for a moment, then sighs, lowers her hands, and turns around to face you."
                            $ the_person.draw_person()
                            the_person "Okay, you can stay. Just... try and look away while I get changed."
                            $ the_person.update_outfit_taboos() #NOTE: We also do proper nudity breaks as she strips.

                        else:
                            the_person "Occupied! I..."
                            "[the_person.possessive_title!c] sighs and lowers her hands to her side."
                            $ the_person.draw_person()
                            the_person "Oh, it's just you."
                            mc.name "I thought you might want my opinion. We'll need to be quiet though, or someone will catch us."
                            "[the_person.title] nods and motions to a narrow knee-high shelf."
                            the_person "Sit down, I'll be changed in a second. Just... try not to stare too much, okay?"
                            the_person "You really aren't supposed to see me naked."

                else:
                    $ the_person.draw_person(position = "back_peek", emotion = "angry")
                    the_person "Occupied! [the_person.mc_title]?!"
                    "She turns her back to you, trying to shield her body from your view."
                    mc.name "I thought this would be a little..."
                    $ the_person.draw_person(emotion = "angry")
                    $ the_person.change_love(-2)
                    "[the_person.title] glares at you and grabs the changing room curtain."
                    the_person "You're going to get us kicked out of the store! Go wait until I'm finished!"
                    "She hurries you out of the changing room and yanks the curtain closed again."
                    $ clear_scene()


            "Wait for her to get changed":
                pass

    if waiting_outside:
        "You find a seat and wait while [the_person.title] changes."
        if changing_type == "overwear":
            $ the_person.apply_outfit(new_outfit.get_copy().merge_outfit(the_person.outfit))
            "Soon enough the changing room curtain is pulled open and [the_person.possessive_title] steps out."
            $ the_person.draw_person()
            the_person "Thanks for waiting. Well, what do you think?"
            "She waits for a moment, then turns around to let you see her outfit from behind."
            $ mc.change_locked_clarity(5)
            $ the_person.draw_person(position = "back_peek")
            if new_outfit.overwear_slut_score > the_person.sluttiness + 5*(the_person.opinion.skimpy_outfits):
                the_person "I think it may be too revealing..."
            else:
                pass

            menu:
                "Get it":
                    mc.name "Buy it, it looks fantastic on you [the_person.title]."
                    $ wants_outfit = True


                "Leave it":
                    mc.name "Leave it, it's not your style."

            "[the_person.possessive_title!c] thinks for a moment, then nods in agreement."
            the_person "You're right, as always."
            $ clear_scene()
            $ the_person.apply_planned_outfit()
            the_person "I just need to change back, I'll be out in a moment!"
            "She steps back into the changing room and closes the curtain behind her."
            $ the_person.draw_person()
            "A short wait later and she steps back out, ready to leave the store."

        else:
            "After waiting for a little while [the_person.title] calls out from behind the curtain."
            if the_person.effective_sluttiness("underwear_nudity") < 20 or the_person.has_taboo("underwear_nudity"):
                if new_outfit.underwear_slut_score < the_person.sluttiness + 5*the_person.opinion.lingerie:
                    the_person "I think it's really cute [the_person.mc_title]!"
                    the_person "I'm going to buy it! I'll be out in a second!"
                    $ wants_outfit = True
                else:
                    the_person "Oh my... It doesn't leave much to the imagination!"
                    the_person "I don't think I'm going to be buying this. Wow, do women actually wear stuff like this?"
                    the_person "I'll be out in a second, thanks for waiting!"
                $ the_person.apply_planned_outfit() #Gets changed back into her normal outfit before coming out.
                $ the_person.draw_person()
                "A little more waiting, then the curtain slides open again."

            elif the_person.effective_sluttiness() > 60 - (10 * the_person.opinion(("skimpy outfits", "public sex"))) and not new_outfit.tits_visible and not new_outfit.vagina_visible:
                if new_outfit.underwear_slut_score <= 5:
                    if the_person.has_role(sister_role):
                        the_person "This is disappointing. It looks like something our grandmother would wear!"
                    else:
                        the_person "This is disappointing. It looks like something my grandmother would wear!"
                    the_person "I might as well put on a chastity belt and call it a day!"
                    the_person "I'll be out in a moment, just need to get dressed again."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person()
                    "Another short wait, then the changing room curtain slides open and [the_person.title] steps out."
                else:
                    $ the_person.apply_outfit(new_outfit)
                    the_person "Hmm, this is pretty cute. I think I need your opinion on it [the_person.mc_title]."
                    $ mc.change_locked_clarity(10)
                    $ the_person.draw_person()
                    "You're about to get up when [the_person.title] throws the changing room curtain open and strides out into the store."
                    the_person "What do you think? It's nice, right?"
                    $ the_person.draw_person(position = "back_peek")
                    $ mc.change_locked_clarity(10)
                    "She gives you a look from the front, then turns around to let you gawk at her ass."

                    $ store_clerk = get_random_from_list(people_with_job(store_assistant_job))
                    if isinstance(store_clerk, Person):
                        mc.name "You look good in it [the_person.title], I..."
                        store_clerk "Excuse me, Ma'am?"
                        $ clear_scene()
                        $ scene_manager = Scene()
                        $ scene_manager.add_actor(the_person, position = "back_peek")
                        "You're interrupted by a store employee, who hurries up to [the_person.possessive_title]."
                        $ scene_manager.add_actor(store_clerk)
                        store_clerk "I'm sorry, but you need to stay inside your changing room while you're trying outfits on."
                        the_person "I have everything covered, don't I? It's no worse than me wearing a bathing suit."
                        store_clerk "It's just store policy, now if you could just step back into the changing room..."
                        $ scene_manager.update_actor(the_person, position = "stand2")
                        the_person "Okay, I understand. Just quickly... [the_person.mc_title], what do you think? Should I buy it?"
                        menu:
                            "Get it":
                                mc.name "Buy it, it looks fantastic on you [the_person.title]."
                                $ wants_outfit = True

                            "Leave it":
                                mc.name "Leave it, it's not your style."

                        the_person "There, I told you I would just need a moment."
                        $ scene_manager.remove_actor(the_person)
                        "[the_person.possessive_title!c] smiles smugly at the store employee and steps back into the changing room."
                        $ scene_manager.update_actor(store_clerk, position = "walking_away")
                        "The employee sighs with relief and wanders back to the front of the store."
                        $ scene_manager.clear_scene()
                        $ scene_manager = None
                        $ store_clerk = None
                    else:
                        the_person "What do you think, [the_person.mc_title]? Should I buy it?"
                        menu:
                            "Get it":
                                mc.name "Buy it, it looks fantastic on you [the_person.title]."
                                $ wants_outfit = True

                            "Leave it":
                                mc.name "Leave it, it's not your style."

                        the_person "Perfect, then let's get out of here."
                        $ clear_scene()

                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person()
                    "After another short wait [the_person.title] steps out, dressed appropriately once again."

            else:
                the_person "It's cute, but... I think I'm going to need your opinion on it [the_person.mc_title]."
                "The curtain to the changing room shifts, and [the_person.title] sticks her head out to check if anyone else is around."
                the_person "Come in. Quick, before anyone notices."
                "You hurry up from your seat and slide into the small changing room with [the_person.possessive_title]."
                $ the_person.apply_outfit(new_outfit)
                $ the_person.draw_person()
                the_person "What do you think? Does it look good on me?"
                "She poses for you briefly, then turns around so you can see it from behind."
                $ the_person.draw_person(position = "back_peek")
                call shopping_date_inside_changing_room(the_person, new_outfit, changing_type, skip_get_changed = True) from _call_shopping_date_inside_changing_room
                $ wants_outfit = _return
    else:
        $ mc.change_location(changing_room)
        call shopping_date_inside_changing_room(the_person, new_outfit, changing_type) from _call_shopping_date_inside_changing_room_1
        $ wants_outfit = _return

    python:
        mc.change_location(old_location)
        old_location = None
    return (wants_outfit, new_outfit)

label shopping_date_inside_changing_room(the_person, new_outfit, changing_type, skip_get_changed = False): #NOTE: skip_get_changed used when an event has already set her outfit properly.
    if not skip_get_changed:
        if changing_type == "overwear":
            $ strip_list = the_person.outfit.get_underwear_strip_list(strip_shoes = True)

        else: #Changing into underwear.
            $ strip_list = the_person.outfit.get_full_strip_list()
            if the_person.has_taboo(["bare_tits", "bare_pussy"]):
                the_person "I'm going to need to... get naked. You don't mind, do you?"
                "[the_person.possessive_title!c] thumbs nervously at her underwear."
                the_person "You could wait outside if you want..."
                mc.name "It's fine [the_person.title], I really don't mind. It's actually nice to watch you like this."
                if the_person.is_family:
                    the_person "You shouldn't be saying that about me [the_person.mc_title]. It's not right..."
                    "She takes a deep breath and nods."
                    the_person "Okay, here we go..."
                else:
                    the_person "You're cute, did you know that? Alright, here we go..."

        if len(strip_list) > 0:
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.remove_clothing(strip_list)
            $ the_person.update_outfit_taboos()
            $ mc.change_locked_clarity(15)

        $ strip_list = None

        the_person "Okay, let's see what this looks like..."
        $ her_opinion = "likes"
        if changing_type == "overwear":
            "She picks up the outfit and slides it on one piece at a time."
            $ the_person.apply_outfit(new_outfit.get_copy().merge_outfit(the_person.outfit), show_dress_sequence = True)
            if new_outfit.overwear_slut_score > the_person.sluttiness + 5*(the_person.opinion.skimpy_outfits):
                $ her_opinion = "slutty"

        else:
            "She picks up the underwear and slips it on."
            $ the_person.apply_outfit(new_outfit, show_dress_sequence = True)
            if new_outfit.underwear_slut_score > the_person.sluttiness + 5*(the_person.opinion.lingerie):
                $ her_opinion = "slutty"
            elif new_outfit.underwear_slut_score <= 5:
                $ her_opinion = "conservative"

        $ the_person.draw_person()
        "She turns to you when it's on, posing for you to get a good view."
        if her_opinion == "likes":
            the_person "What do you think? I think it's a cute look. I could definitely imagine myself wearing this."
        elif her_opinion == "slutty":
            the_person "What do you think? Is it too much? I think it's too much."
        elif her_opinion == "conservative":
            the_person "What do you think? I don't think it suits me very well."
            the_person "It covers up a little too much."

    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title!c] turns around to give you a look at her ass."

    $ wants_outfit = False
    menu:
        "Get it":
            mc.name "Buy it, it looks fantastic on you [the_person.title]."
            $ wants_outfit = True
            "She considers for a moment, then nods in agreement."
            the_person "You're right, of course! Alright, I'm getting it!"

        "Leave it":
            mc.name "Leave it, it's not your style."
            "She considers it for a moment, then nods in agreement."
            the_person "You're right. It looked a lot cuter on the rack."
            the_person "Oh well..."

    $ slut_token = get_gold_heart(30)

    menu:
        "Grope her butt":
            $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
            $ mc.change_locked_clarity(10)
            "You lean forward from your seat and plant a hand on [the_person.possessive_title]'s ass."
            if the_person.has_taboo("touching_body"):
                "She gasps and tries to take a step away from you, but there isn't enough room in the small changing room for her to escape."
                the_person "[the_person.mc_title]! What are you doing?"
                "She glances nervously at the curtain-door, worried her outburst had been too loud."
                $ mc.change_locked_clarity(10)
                if the_person.vagina_available or the_person.outfit.are_panties_visible:
                    "You continue to run your hand over her smooth butt as you respond."
                else:
                    "You continue to run your hand over her ass as you respond."
                mc.name "You were shoving it in my face, I thought this is what you wanted."
                the_person "I... Of course not!"
                mc.name "Quiet, [the_person.title], or someone's going to hear us. Imagine if they found us like this..."
                $ the_person.break_taboo("touching_body")
                "[the_person.possessive_title!c] shuffles uncomfortably, but seems more comfortable under your touch."
                "She plants her hands on the far side of the changing room and arches her back a little bit."

            else:
                "She gasps and shuffles away from you in surprise, but there isn't enough room in the small changing room to get away from your touch."
                the_person "[the_person.mc_title], stop it! You're going to get us in trouble!"
                "She glances nervously at the curtain-door, worried someone might have heard her yelp."
                $ mc.change_locked_clarity(10)
                if the_person.vagina_available or the_person.outfit.are_panties_visible:
                    "You continue to run your hand over her smooth butt as you respond."
                else:
                    "You continue to run your hand over her ass as you respond."
                mc.name "You were shoving this in my face, isn't this what you want?"
                the_person "Not here, obviously! I..."
                mc.name "Quiet, [the_person.title], or someone's going to hear us."
                "[the_person.title] sighs and relents, planting her hands on the far side of the changing room and arching her back a little."

            $ the_person.draw_person(position = "standing_doggy")
            if the_person.effective_sluttiness() + 10*the_person.opinion.public_sex >= 40:
                $ mc.change_locked_clarity(10)
                "She lets you caress her body from your seat, leaning herself against your hands happily."
                "You stand up and wrap your arms around her, kissing her neck sensually."
                the_person "As long as we're quiet..."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_124
                $ the_report = _return
                $ the_person.call_dialogue("sex_review", the_report = the_report)
            else:
                $ mc.change_locked_clarity(10)
                "She lets you caress her for a few moments, then stands up and starts to collect her clothing."
                $ the_person.draw_person()
                the_person "That was nice, but we can't be in here too long. You'll have to wait until later."



        "Pull out your cock" if the_person.effective_sluttiness() >= 30:
            "You slide your pants down and pull out your hard cock while [the_person.possessive_title] is checking herself out in the mirror."
            $ sex_valid = False
            if the_person.effective_sluttiness() + 10 * the_person.opinion.public_sex > 60:
                "When she glances back she smiles and nods."
                the_person "Right here [the_person.mc_title]? It's a little risky..."
                $ mc.change_locked_clarity(15)
                "You grab onto your hard cock and stroke it slowly while talking."
                mc.name "Watching you get dressed up for me got me excited. I need to take care of this before I go back out."
                if the_person.vagina_available and not the_person.has_taboo("vaginal_sex"): # She bends over and asks if you want to fuck her
                    $ sex_valid = True
                    $ the_person.draw_person()
                    "[the_person.title] turns around and plants her back against the changing room wall."
                    $ mc.change_locked_clarity(20)
                    "She reaches between her legs and pets her pussy."
                    the_person "I think I have just what you need."
                elif the_person.outfit.can_half_off_to_vagina() and not the_person.has_taboo("vaginal_sex"):
                    $ sex_valid = True #She pulls her clothing to the side and asks if you want to fuck her
                    $ the_person.draw_person()
                    "[the_person.title] turns around and plants her back against the changing room wall."
                    $ generalised_strip_description (the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
                    $ mc.change_locked_clarity(20)
                    "[the_person.title] reaches between her legs and pets her pussy as you watch."
                    the_person "I think I have just what you need."
                else:
                    the_person "You do, huh? Well then, what can I do to help?"
            else:
                "When she glances back and sees she gasps quietly."
                the_person "[the_person.mc_title]! What are you doing?"
                mc.name "Watching you get dressed up for me got me hard, I can't go outside like this."
                $ mc.change_locked_clarity(10)
                "You grab onto your hard cock with one hand and stroke it slowly while talking."
                mc.name "I won't be long, I just need to take care of this."


            $ blowjob_slut_requirement = 40 - (5 * the_person.opinion(("public sex", "giving blowjobs")))
            $ blowjob_slut_token = get_gold_heart(blowjob_slut_requirement)

            $ sex_slut_requirement = 60 - (5 * the_person.opinion(("public sex", "vaginal sex")))
            $ sex_slut_token = get_gold_heart(sex_slut_requirement)

            menu shopping_date_inside_changing_room_menu:
                "Jerk yourself off":
                    "You stroke your cock while looking at [the_person.title]."
                    "You know you might not have long before you are interrupted, so you focus on making yourself cum as quickly as possible."
                    if the_person.tits_available:
                        $ mc.change_locked_clarity(15)
                        "[the_person.title]'s tits give you something nice to focus on as you draw closer and closer to climax."
                    else:
                        $ mc.change_locked_clarity(5)
                        "[the_person.title]'s nice body gives you something to focus on as you draw closer and closer to climax."
                    the_person "[the_person.mc_title], are you almost done? We've been in here a really long time."
                    if the_person.outfit.can_half_off_to_tits():
                        the_person "Here..."
                        $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
                        "She jiggles her tits for you, giving you something to focus on."
                    $ climax_controller = ClimaxController(["Cum on the floor.","air"])
                    $ climax_controller.show_climax_menu()
                    "You push yourself past the point of no return and lean back, grunting softly as you cum."
                    $ climax_controller.do_clarity_release(the_person)
                    "You pulse your load in an arc onto the floor, getting some of it on [the_person.title]'s feet."
                    the_person "... Better?"
                    "You pant and nod, stuffing your cock back in your pants."
                    mc.name "Much better."

                "Ask for a handjob":
                    "You stroke your cock in front of [the_person.possessive_title] for a little bit."
                    mc.name "This would go faster if you would take care of it... Just come over here and put your hand on it."
                    if the_person.has_taboo("touching_penis"):
                        $ the_person.call_dialogue("touching_penis_taboo_break")
                        $ the_person.break_taboo("touching_penis")
                    $ mc.change_locked_clarity(10)
                    "[the_person.title] wraps her hand around your shaft and starts to stroke it for you."
                    call fuck_person(the_person, private = True, start_position = handjob, skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_125
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

                "Ask for a blowjob" if the_person.effective_sluttiness() >= blowjob_slut_requirement:
                    "You stroke your cock in front of [the_person.possessive_title] for a little bit."
                    mc.name "This would go faster if you would take care of it."
                    mc.name "Get on your knees and suck me off, before anyone notices what's going on in here."
                    if the_person.has_taboo("sucking_cock"):
                        $ the_person.call_dialogue("sucking_cock_taboo_break")
                        $ the_person.break_taboo("sucking_cock")
                    $ the_person.draw_person(position = "blowjob")
                    $ mc.change_locked_clarity(15)
                    "[the_person.title] kneels down in front of you. You let go of your shaft and let it flop onto her face."
                    the_person "Ah..."
                    "She leans back and brings the tip of your dick to her lips."
                    "After giving it a quick kiss she bobs forward, sliding you into her mouth."
                    "You have to stifle a moan as her slippery tongue begins to work it's magic up and down your shaft."
                    call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_126
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)

                "Ask for a blowjob\n{menu_red}Requires: [blowjob_slut_token]{/menu_red} (disabled)" if the_person.effective_sluttiness() < blowjob_slut_requirement:

                    pass

                "Fuck her" if sex_valid and the_person.effective_sluttiness() >= sex_slut_requirement:
                    mc.name "Yeah, that's exactly what I need right now."
                    call condom_ask(the_person) from _call_condom_ask_4
                    if _return:
                        call fuck_person(the_person, private = True, start_position = against_wall, skip_condom = True) from _call_fuck_person_127
                        $ the_report = _return
                        $ the_person.call_dialogue("sex_review", the_report = the_report)
                    else:
                        $ sex_valid = False
                        jump shopping_date_inside_changing_room_menu

                "Fuck her\n{menu_red}Requires: [sex_slut_token]{/menu_red} (disabled)" if sex_valid and the_person.effective_sluttiness() < sex_slut_requirement:
                    pass

        "Pull out your cock\n{menu_red}Requires: [slut_token]{/menu_red} (disabled)" if the_person.effective_sluttiness() < 30:
            pass

        "Let her get dressed":
            pass

    "[the_person.title] changes back into her own outfit."
    python:
        slut_token = None
        sex_slut_token = None
        blowjob_slut_token = None
        the_person.apply_planned_outfit(show_dress_sequence = True)

    "When she's done she slides open the changing room curtain."
    the_person "Come on, let's get going."
    return wants_outfit

label shopping_date_hair(the_person):
    mc.name "How about we get your hair done? I think there's a salon in here somewhere."
    if the_person.has_relation_with_mc:
        if the_person.is_bald:
            "She runs her hand over her bald scalp."
        else:
            "She runs her fingers through her [the_person.hair_description]."
        the_person "Do you think it's time for a change?"
        mc.name "Maybe. Let's take a look."
    elif the_person.has_role(sister_role):
        the_person "Why, don't you think my hair looks cute?"
        mc.name "Can't hurt to try a new style, right?"
        if the_person.is_bald:
            "She runs her hand over her bald scalp and thinks for a few seconds."
        else:
            "She runs her fingers through her [the_person.hair_description] and thinks for a few seconds."
        the_person "I guess... Alright, we can take a look."
    elif the_person.has_role(mother_role):
        the_person "Oh, I don't like to spend money on things like that. I'm happy with my [the_person.hair_description], nice and plain."
        mc.name "Come on, if it's money that's the issue I can pay for it. You should treat yourself once in a while."
        if the_person.is_bald:
            "She runs her hand over her bald scalp and thinks for a moment."
        else:
            "She runs her fingers through her [the_person.hair_description] and thinks for a moment."
        the_person "Well... I suppose it couldn't hurt to look."
    else: #In theory this shouldn't come up right now, but maybe it will in the future.
        the_person "Don't you like my [the_person.hair_description]?"
        mc.name "Sure, but a new style could be nice too, right?"
        if the_person.is_bald:
            "She runs her hand over her bald scalp, then shrugs and nods."
        else:
            "She runs her fingers through her [the_person.hair_description], then shrugs and nods."
        the_person "Alright, we can take a look."

    $ the_person.draw_person(position = "walking_away")
    "You and [the_person.possessive_title] walk to the salon."

    if day % 7 == 6: # closed on sundays
        "As you walk up to the salon, you notice that it is closed."
        mc.name "Seems we are out of luck."
        the_person "I guess you will have to take me another time."
        return

    $ mc.change_location(mall_salon)
    if ophelia_get_chocolate_gift_unlock():
        $ salon_manager.draw_person()
        salon_manager "Hello [salon_manager.mc_title], nice to see you again."
        mc.name "Hello [salon_manager.fname], this is [the_person.fname], she wants to change up her style."
        salon_manager "No problem, here is our catalog, don't worry [the_person.fname], I will make you look spectacular."
    else:
        "The receptionist smiles as you come in and offers you a style magazine to look through."

    python:
        clear_scene()
        hair_style_check = the_person.hair_style.get_copy()
        pubes_style_check = the_person.pubes_style.get_copy()
        the_person.draw_person(show_person_info = False)

    call screen hair_creator(the_person, hair_style_check, pubes_style_check)
    call salon_checkout() from _call_salon_checkout_shopping_date_hair

    $ the_person.draw_person()

    if hair_style_check != the_person.hair_style:
        the_person "Well, what do you think?"
        "She gives a little turn so you can get a good look."
        menu:
            "It's cute":
                mc.name "It's a cute look."
                $ the_person.change_love(1, max_amount = 40)

            "It's sexy":
                mc.name "You look pretty hot."
                $ the_person.change_slut(1, 30)

            "It's what I wanted":
                mc.name "It's just what I wanted."
                $ the_person.change_obedience(1, max_amount = 140)

        $ mc.change_location(mall)
        "You leave the salon together. [the_person.possessive_title!c] keeps looking at her new style in her phone camera."

    elif hair_style_check.colour != the_person.hair_style.colour:
        the_person "Well, what do you think?"
        "She gives a little turn so you can get a good look."
        menu:
            "It's cute":
                mc.name "It's a cute look."
                $ the_person.change_love(1, max_amount = 40)

            "It's sexy":
                mc.name "You look pretty hot."
                $ the_person.change_slut(1, 30)

            "It's what I wanted":
                mc.name "It's just what I wanted."
                $ the_person.change_obedience(1, max_amount = 140)

        $ mc.change_location(mall)
        "You leave the salon together. [the_person.possessive_title!c] keeps looking at her new dye in her phone camera."

    elif pubes_style_check != the_person.pubes_style or pubes_style_check.colour != the_person.pubes_style.colour:
        the_person "Will you be checking out my new styling later?"
        mc.name "At least I will have a reason to take off your panties."

        $ mc.change_location(mall)
        "While you leave the salon together, she grabs your arm and holds you tight."
    else:
        the_person "Pity we couldn't find anything nice."
        mc.name "Don't worry, I like you just the way you are."

        $ mc.change_location(mall)
        "You leave the salon together."

    python:
        clear_scene()
        del hair_style_check
        del pubes_style_check
    return

label do_haircut(the_person, new_style):
    $ clear_scene()
    "You take a seat as [the_person.possessive_title] is taken away by a stylist."

    $ old_colour = the_person.hair_style.colour
    $ the_person.hair_style = new_style.get_copy()
    $ the_person.hair_style.colour = old_colour
    "You pass the time on your phone until [the_person.title] comes back out."
    $ the_person.draw_person()
    return

label do_dye(the_person, new_colour):
    $ clear_scene()
    "You take a seat as [the_person.possessive_title] is taken away by a stylist."
    $ the_person.set_hair_colour(new_colour, change_pubes = False)
    "You pass the time on your phone until [the_person.title] comes back out."
    $ the_person.draw_person()
    return

label check_date_trance(the_person): #At the end of a date you have an opportunity to trance her as well.
    if the_person.trance_training_available:
        "You pause. [the_person.possessive_title!c] seems to be stunned by her recent climax."
        "This might be your chance to put some new thoughts in her head."
        menu:
            "Train her":
                call do_training(the_person) from _call_do_training_check_date_trance

            "Leave her alone":
                pass
    return

label date_schedule_selection(the_person, time_slot, day_restriction = (0, 1, 2, 3, 4, 5, 6)):
    $ available_date_list = mc.schedule.get_open_time_slots(day_restriction = day_restriction, time_restriction = time_slot)
    if len(available_date_list) > 0:
        "You check your calendar to see what day you have available."
        call screen main_choice_display(build_menu_items([mc.schedule.build_appt_menu_items(available_date_list)]))
        if isinstance(_return, tuple) and len(_return) == 2:
            $ day_name = day_and_time_string(_return[0], _return[1])
            "You mark your calendar for a date with [the_person.title] on [day_name]."
            return _return
        else:
            "You decide not to schedule something for now."
            return None
    else:
        "There isn't a free time slot for you date."
        return None

#TODO: Write all of the date options, which should include.
# A) Get some food (chat + serum chance)
# B) Go overwear shopping. (Tries on some different overwear sets for you, gives you the option to buy it for her)
# C) Go underwear shopping. (Suggest some underwear sets to her. At moderate slut you can sneak in and view it on her.)
# |-> Both of these should include options to peek in on her as she changes (and maybe get caught), or have her invite you in.
# |-> At high Sluttiness you can try and fuck her in the changing booth.
# E) Go electronics shopping. (Chance to spend major cash for Love boost)
# F) Go sex toy shopping. (Chance to increase Sluttiness, but needs high Sluttiness to begin with).
# Z) Go home/Go home early.
