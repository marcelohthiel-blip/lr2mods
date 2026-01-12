#This file contains code for a generic bar date.
#For now, start moving bar date related functions here. No generic bar date has been written yet but it is TODO


init -1 python:
    BAR_DATE_ROUNDS = 3     #Default how many rounds we go at the bar. Maybe make this changeable in game in some way?
    BAR_DATE_GAME_RANDOM_MARGIN = 10 # When comparing skills, each point gives an additional 1/(2X) chance to win the game.

    #NOTE: This is a copy of working weekend subjects. Make this a global and use it both places?
    relax_discussion_topics = {
        "general" : ["flirting", "sports", "hiking", "Mondays", "Fridays", "the weekend"],
        "work": ["working", "work uniforms", "research work", "marketing work", "HR work", "supply work", "production work"],
        "style": ["skirts", "pants", "dresses", "boots", "high heels", "makeup", "conservative outfits", "the colour blue", "the colour yellow", "the colour red", "the colour pink", "the colour green", "the colour purple", "the colour white", "the colour black"],
        "positions": ["missionary style sex", "doggy style sex", "sex standing up"],
        "sex_types": ["vaginal sex", "anal sex", "giving blowjobs", "getting head", "public sex"],
        "cum": ["creampies", "being covered in cum", "cum facials", "drinking cum", "bareback sex"],
        "sexy_clothing" : ["skimpy outfits", "skimpy uniforms", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "lingerie", "high heels", "dresses"],
        "kinks" : ["masturbating", "giving handjobs", "being fingered", "being submissive", "taking control", "threesomes", "incest"]
    }

    def bar_date_sex_booth_check(the_person):
        return the_person.effective_sluttiness() >= 60

    def bar_date_group_sex_booth_check(the_group):
        return False

    def bar_date_one_night_stand_check(the_person):
        if the_person.is_drunk:    #She's drunk, she invites MC home
            return "drunk"
        if the_person.arousal >= 80:
            return "arousal"
        if the_person.love >= 40:
            return "love"
        if the_person.effective_sluttiness() >= 40:
            return "slut"
        if the_person.obedience>= 140:
            return "obedience"
        return False

    def bar_date_fetish_interrupt_check(the_person):
        random_value = renpy.random.randint(0, 8)   #1 in 8 chance for each fetish she has, 4/8 chance for nothing even with max fetishes
        if random_value == 0 and the_person.has_breeding_fetish:
            return "breed"
        if random_value == 1 and the_person.has_cum_fetish:
            return "cum"
        if random_value == 2 and the_person.has_anal_fetish:
            return "anal"
        if random_value == 3 and the_person.has_exhibition_fetish:
            return "exhibition"
        return False

    def bar_group_date_fetish_interrupt_check(the_group):
        return False

    def build_bar_date_menu_items(the_person, previous_actions = []):
        option_list = []
        bar_opinions = the_person.personality.activity_opinions
        option_list.append("Start Choice")
        if "relax" not in previous_actions:
            option_list.append(["Relax at a Booth", "relax"])
        if "get to know" not in previous_actions and bar_date_person_has_get_to_know_label(the_person):
            option_list.append(["Get to Know Her Better", "get to know"])
        if "shots" not in previous_actions:
            option_list.append(["Order Shots", "shots"])
        for entry in mc.business.event_triggers_dict.get("bar_games_avail", {}):
            if entry not in previous_actions:
                option_list.append([get_activity_text(entry, the_person), entry])
        # if mc.business.event_triggers_dict.get("bar_booth_avail", False) and "booth" not in previous_actions and bar_date_sex_booth_check(the_person):
        #     option_list.append(["Sex Booth", "booth"])
            #This item commented out becuase it hasn't been written yet. To be accomplished with Camilla work.
        option_list.append(["Call it a Night", "leave"])
        return option_list

    def build_group_bar_date_menu_items(the_group, previous_actions = []):
        option_list = []
        option_list.append("Start Choice")
        if "relax" not in previous_actions:
            option_list.append(["Relax at a Booth", "relax"])
        if "shots" not in previous_actions:
            option_list.append(["Order Shots", "shots"])
        for entry in mc.business.event_triggers_dict.get("bar_games_avail", {}):    #Use unlocked generic bar date games as a baseline
            target_name = "bar_group_date_" + entry + "_label"
            if renpy.has_label((target_name)) and entry not in previous_actions:
                option_list.append([get_group_activity_text(entry, the_group), entry])

        if mc.business.event_triggers_dict.get("bar_booth_avail", False) and "booth" not in previous_actions and bar_date_group_sex_booth_check(the_group):
            option_list.append(["Sex Booth", "booth"])
        option_list.append(["Call it a Night", "leave"])
        return option_list

    def bar_date_add_available_game(the_game):
        if mc.business.event_triggers_dict.get("bar_games_avail", None) == None:
            mc.business.event_triggers_dict["bar_games_avail"] = []
        if the_game not in mc.business.event_triggers_dict.get("bar_games_avail", None):
            mc.business.event_triggers_dict["bar_games_avail"].append(the_game)
        return

    def bar_date_unlock_all():
        mc.business.event_triggers_dict["bar_games_avail"] = ["pong", "salsa", "arcade", "billiards", "darts", "karaoke", "trivia"]
        return


    list_of_girly_drinks = [    #Starts with a consanent so we don't have to adapt a(n) for drink orders#
        "floradora",
        "shirley temple",
        "strawberry daiquiri",
        "mojito",
        "sex on the beach",
        "tom collins",
        "mai tai",
        "screwdriver",
        "paloma",
        "Kahlua mudslide",
        "cosmopolitan",
        "white russian",
        "lemon drop",
        "sangria",
        "gin sour",
        "blue hawaiian",
        "appletini",
        "melon ball"
    ]

    list_of_shots = [
        "jager bombs",
        "slippery nipples",
        "vokda shots",
        "tequila shots",
        "cement mixers",
        "cactus coolers",
        "kamikazes",
        "cherry bombs",
        "green teas",
        "Irish car bombs",
        "lemon drops"
    ]

    def bar_date_favorite_drink(person):
        if person.event_triggers_dict.get("favorite_drink", None) == None:
            person.event_triggers_dict["favorite_drink"] = get_random_from_list(list_of_girly_drinks)
        return person.event_triggers_dict.get("favorite_drink", None)


    # Use this to determine if a girl attempts to distract MC
    # Distractions levels:
        # 0: Flirt
        # 1: Flash tits
        # 2: Flash Ass/pussy
        # 3: Grope/Lick/Suck MC
        # 4: Actual sex act? Probably never going to happen
    # Girls NEVER attempt anything illegal (yet)
    def bar_date_game_distraction_check(person, distraction_level):
        if distraction_level == 0:
            return ((person.effective_sluttiness() + person.drink_level + (3 * person.opinion.flirting)) >= 20)
        if distraction_level == 1:
            if mc.business.topless_is_legal:
                return ((person.effective_sluttiness("bare_tits") + person.drink_level + (3 * person.opinion.showing_her_tits)) >= 30)
            else:
                return False
        if distraction_level == 2:
            if mc.business.nudity_is_legal:
                return ((person.effective_sluttiness("bare_pussy") + person.drink_level + (3 * person.opinion.showing_her_tits)) >= 40)
            else:
                return False
        if distraction_level == 3:
            if mc.business.public_sex_act_is_legal:
                return ((person.effective_sluttiness() + person.drink_level + (3 * person.opinion.public_sex)) >= 60)
            else:
                return False
        if distraction_level == 4:
            if mc.business.public_sex_is_legal:
                return ((person.effective_sluttiness() + person.drink_level + (3 * person.opinion.public_sex)) >= 80)
            else:
                return False
        return False

    def bar_group_date_game_distraction_check(the_group, distraction_levels):
        #First, check and see if distraction is straight up illegal
        return False

    def bar_date_person_has_get_to_know_label(person):
        check_label = person.func_name + "_get_to_know_label"
        return renpy.has_label(check_label)

    def bar_date_get_to_know_label(person):
        check_label = person.func_name + "_get_to_know_label"
        if renpy.has_label(check_label):
            return check_label
        return None

    def test_group_date(group_size = 2):
        the_group = [stephanie]     #Our beautiful test subject
        x = 1
        test_people = [mom, lily, nora, alexia, cousin, aunt, camila, sarah, starbuck]
        while x < group_size:
            new_person = get_random_from_list(test_people)
            the_group.append(new_person)
            test_people.remove(new_person)
            x+= 1
        renpy.call("bar_date_group_main_label", the_group)
        return


####################################
###### Primary Bar Date Label ######
####################################
label bar_date_main_label(the_person, drinks_only = False, selected_actions = []):
    #This is the main label we call for grabbing drinks at the bar.
    #Allow for a pre-existing drink label if we are coming from dinner, etc.
    #At the start of this label, we assume that the girl(s) have already accepted our offer for drinks and we are now deciding what to do.
    #Different intros can lead to this label, so we leave it to the calling label to establish the reason for grabbing drinks, we don't do that here.
    #EG Stephanie and Nora's team up leads us here.
    $ round_number = 0
    $ interrupt_complete = False
    $ round_choice = None

    #First, get her drink order and give a chance to dose her.
    $ drink_order = bar_date_favorite_drink(the_person)
    $ the_person.draw_person()
    "You approach the bar with [the_person.possessive_title], but it is pretty crowded."
    mc.name "I'll get us the drinks. What do you want?"
    the_person "Can you get me a [drink_order]?"
    mc.name "Absolutely. Give me a minute..."
    $ clear_scene()
    "It takes a bit, but you manage to find a spot at the bar and place your drink orders."
    "The bartender is busy, and after he drops off your drinks, he quickly moved on to the next person."
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    "If you are quick, you could sneak in a serum..."
    call give_serum(the_person) from _call_give_bar_date_sneaky_boi_01
    if _return:
        "You drop the serum in to the drink with no one noticing, then return to [the_person.title] and hand it to her."
    else:
        "You just grab the drinks and return to [the_person.title], handing it to her."
    $ the_person.draw_person()
    the_person "Thanks! This looks great..."
    $ the_person.change_happiness(2)
    "She takes a long sip, then flashes you a smile."
    the_person "So, what do you want to do now?"
    "You think about it for a moment."
    while round_number < BAR_DATE_ROUNDS:   #Right now this is a constant. Maybe link this to her serum resistance?
        if round_number > 0:    #Dialogue if we went through this loop atleast once already
            #First, check and see if she asks for a fetish fulfillment
            if not interrupt_complete:
                $ interrupt_type = bar_date_fetish_interrupt_check(the_person)
                if interrupt_type:
                    if interrupt_type == "breed":
                        call bar_date_breeding_fetish_interrupt_label(the_person) from _bar_date_breeding_interrupt
                    if interrupt_type == "cum":
                        call bar_date_cum_fetish_interrupt_label(the_person) from _bar_date_cum_interrupt
                    if interrupt_type == "anal":
                        call bar_date_anal_fetish_interrupt_label(the_person) from _bar_date_anal_interrupt
                    if interrupt_type == "exhibition":
                        call bar_date_exhibition_fetish_interrupt_label(the_person) from _bar_date_exhibition_interrupt
                $ interrupt_complete = True
            "You quickly head up to the bar and order another round for you and [the_person.title]."
            $ mc.business.change_funds(-20, stat = "Food and Drinks")
            "You return with her drink. She takes a sip."
            if the_person.is_drunk:
                the_person "Whew! This should prolly be my LAST one!"
                "Her slurred speech is getting more apparent. She must be getting pretty drunk."
            elif the_person.is_tipsy:
                the_person "Yum! Another drink, these are starting to feel good. What now?"
                "You can tell from her attitude that [the_person.title] is starting to get a little tipsy."
                pass
            else:
                the_person "Alright, what do you want to do now?"
        $ the_person.increase_drink_level(1)
        # $ bar_date_set_drunk_level(the_person, drink_level)
        #TODO Fancy code here to give a bunch of choices about what to do.
        call screen main_choice_display(build_menu_items([build_bar_date_menu_items(the_person, previous_actions = selected_actions)]))
        $ round_choice = _return
        $ selected_actions.append(round_choice)
        if round_choice == "leave":
            $ round_number = 99
        else:
            $ round_number += 1
            call bar_date_choice_label(the_person, round_choice) from _bar_date_round_choice_split_01
        if the_person.is_wasted:  #She is wasted, we need to back out of this loop
            $ round_number = BAR_DATE_ROUNDS
    if drinks_only: #If this label was called for the drink portion only, exit now
        return

    if the_person.is_wasted:
        $ the_person.draw_person()
        "As she stands before you, [the_person.possessive_title!c] struggles to form a complete sentence."
        "She appears to be completely wasted, incapable of coherent thought."
        "You sigh. You must have pushed her a bit to hard tonight. You'd probably better make sure she gets home okay."
        #TODO If it is a girlfriend, affair, or harem member, add the option to fuck her while she is passed out anyway.
        #Maybe make an automatic conversation for those roles where they give MC express permission to do so?
        mc.name "Hey, you seem really out of it, let's get you a cab home, okay?"
        the_person "Mmmm, how about a cab to YOUR home?"
        "Her slurred speech doesn't give you any confidence."
        if the_person.is_family:
            mc.name "[the_person.title], let's just get you home."
        else:
            mc.name "Next time, [the_person.title]."
        "She gives you a little pout but is no real position refuse you."
        if the_person == mom or the_person == lily:
            "You call a cab, and soon you are climbing into it with her."
            "You ride home together, making sure that she gets a glass of water and that she gets to bed okay."
        else:
            "You call a cab, and make sure the driver knows where to take her."
            "You walk home, stopping at the kitchen to chug a glass of water."
        $ clear_scene()
        "You go to your room, exhausted from a night of drinking, and quickly fall asleep."
        return
    if the_person.is_unique:    #For now, avoid one night stands with unique girls until I can figure out conditions for them.
        if get_named_label("date_take_home_her_place", the_person):
            $ run_named_label("date_take_home_her_place", the_person, date_type = "drinks")
            return
        $ the_person.draw_person()
        the_person "Hey thank you for the good time tonight... but I really need to get going."
        if the_person.is_family:
            mc.name "Yeah? Want to continue things at home?"
            the_person "Umm, maybe next time. But I really did have fun hanging out with you tonight [the_person.mc_title]."
            mc.name "Ah, okay. I'll see you later [the_person.title]."
        else:
            mc.name "Yeah? Want to go back to my place?"
            if bar_date_one_night_stand_check(the_person):
                "She clearly considers it for a few moments."
                the_person "Ugh, sounds like fun... but I really can't. I'm sorry!"
            else:
                the_person "I really can't. I'm sorry!"
            mc.name "No worries. Take care."
            the_person "I really did have fun hanging out with you tonight [the_person.mc_title]."
            mc.name "Ah, okay. I'll see you later [the_person.title]."
        $ the_person.change_love(5, 60)
        $ clear_scene()
        if time_of_day == 4:
            $ mc.change_location(kitchen)
            "You walk home, stopping at the kitchen to chug a glass of water."
            $ mc.change_location(bedroom)
            "You go to your room, exhausted from a night of drinking, and quickly fall asleep."
            return "Advance Time"
        else:
            "After saying goodbye, you turn back to the bar."
            return "Advance Time"
        return

    # Check and see if she requests MC to go to her place.
    $ bar_date_result = bar_date_one_night_stand_check(the_person)
    if bar_date_result:
        the_person "Hey, I had a great time tonight, and I don't want to say goodbye. Did you want to come back to my place for a bit?"
        if bar_date_result == "drunk":
            "Her slight slurring betrays the quantity of alcohol she's consumed tonight. It would be a good opportunity to take advantage of her drunken state."
        elif bar_date_result == "arousal":
            "Her pupils are slightly dilated and her cheeks are flushed. She is clearly aroused, and seems eager to get you along at her place to try and get off."
        elif bar_date_result == "love":
            the_person "I always have a great time with you, and it would be nice if I could show you how much I appreciate it in private..."
        elif bar_date_result == "slut":
            the_person "I've got some new underwear at home I could change in to that I picked out JUST for nights like this..."
        else:
            "She quietly waits for your response."
        menu:
            "Her Place":
                mc.name "That sounds like a great idea."
                "You quickly arrange for a taxi to her place."
                if not the_person.has_role(aunt_role) and not the_person.has_role(cousin_role):
                    if not the_person.mc_knows_address:
                        $ the_person.learn_home()
                $ the_person.change_location(the_person.home)
                "After a short ride you pull up in front her house. She leads you to the front door and invites you inside."
                $ run_named_label("date_take_home_her_place", the_person, date_type = "drinks")
                return
            "Call It a Night":
                mc.name "I'd like to call it an early night today, but maybe I'll take you up on the offer some other time."
                "You order her a taxi, and you step outside with her and wait."
                "Her taxi arrives. You give her a goodbye kiss and head home yourself."
    else:   #Date ends
        the_person "I had a great night [the_person.mc_title], you're a lot of fun to be around. We should do this again."
        mc.name "It would be my pleasure."
        "[the_person.title]'s taxi arrives and she gives you a kiss goodbye. You watch her drive away, then head home yourself."

    return "Advance Time"

#Right now only run group dates with 2 girls, but leave options open for expanding later!
label bar_date_group_main_label(the_group, drinks_only = False, selected_actions = []):
    #We take a list as input so we can have bar dates with atleast 2 girls at the same time
    #This input allows us to write bigger dates in the future if we wish, but for now 2 works.
    #Otherwise mostly identical to the main label.
    $ group_size = len(the_group)   #Use group size for some decision paths
    $ round_number = 0
    $ interrupt_complete = False
    $ round_choice = None

    #First, get drink orders
    if group_size == 2:
        $ drink_order_1 = bar_date_favorite_drink(the_group[0])
        $ drink_order_2 = bar_date_favorite_drink(the_group[1])
        $ scene_manager = Scene()
        $ scene_manager.add_actor(the_group[0])
        $ scene_manager.add_actor(the_group[1])

        "You approach the bar with [the_group[0].possessive_title] and [the_group[1].title], but it is pretty crowded."
        mc.name "I'll get us the drinks. What do you two want?"
        the_group[0] "Can you get me a [drink_order_1]?"
        the_group[1] "And a [drink_order_2] for me!"
        mc.name "Absolutely. Give me a minute..."
        $ scene_manager.clear_scene()
        "It takes a bit, but you manage to find a spot at the bar and place your drink orders."
        "The bartender is busy, and after he drops off your drinks, he quickly moved on to the next person."
        $ mc.business.change_funds(-30, stat = "Food and Drinks")
        "If you are quick, you could sneak in a serum..."
        call give_serum(the_group[0]) from _call_give_bar_date_sneaky_boi_02
        call give_serum(the_group[1]) from _call_give_bar_date_sneaky_boi_03
        "You just grab the drinks and find the table where the girls are sitting, handing them out."
    $ scene_manager.add_actor(the_group[0], display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_group[1], position = "sitting", display_transform = character_right)
    "You sit down at the end of the table."
    the_group[0] "Thanks! This looks great..."
    $ the_group[0].change_happiness(2)
    the_group[1] "Yeah! Thanks [the_group[1].mc_title]!"
    "The girls take long sips from their drinks, then look at you, expectantly."
    the_group[0] "So, what do you want to do now?"
    "You think about it for a moment."
    while round_number < BAR_DATE_ROUNDS:
        if round_number > 0:    #Dialogue if we went through this loop atleast once already
            #First, check and see if she asks for a fetish fulfillment
            if not interrupt_complete:
                $ interrupt_type = bar_group_date_fetish_interrupt_check(the_group) #Check and see if the girls share a fetish type
                if interrupt_type:
                    if interrupt_type == "breed":
                        call bar_date_group_breeding_fetish_interrupt_label(the_person) from _bar_group_date_breeding_interrupt
                    if interrupt_type == "cum":
                        call bar_date_group_cum_fetish_interrupt_label(the_person) from _bar_group_date_cum_interrupt
                    if interrupt_type == "anal":
                        call bar_date_group_anal_fetish_interrupt_label(the_person) from _bar_group_date_anal_interrupt
                    if interrupt_type == "exhibition":
                        call bar_date_group_exhibition_fetish_interrupt_label(the_person) from _bar_group_date_exhibition_interrupt
                $ interrupt_complete = True
            "You quickly head up to the bar and order another round for you and the girls."
            $ mc.business.change_funds(-30, stat = "Food and Drinks")
            "You return with the drinks."
            if the_group[0].is_drunk:
                the_group[0] "Whew! This should prolly be my LAST one!"
                if the_group[1].is_drunk:
                    the_group[1] "Me too, I'm having such a great time though..."
                    "The girl's slurred speech is getting more apparent. They must be getting pretty drunk."
                elif the_group[1].is_tipsy:
                    the_group[1] "Yeah, I'm feeling pretty good too, but maybe one more?"
                    "[the_group[0].title]'s slurred speech is getting more apparent. It might be about time to be done, for her sake."
                else:
                    the_group[1] "Oh come on [the_group[0].fname], don't be such a lightweight!"
                    "She gives her a hard time, but you can tell that [the_group[1].title] is just joking."
                    "[the_group[0].title]'s slurred speech is getting more apparent. It might be about time to be done, for her sake."
            elif the_group[0].is_tipsy:
                the_group[0] "Yum! Another drink, these are starting to feel good. What now?"
                if the_group[1].is_drunk:
                    the_group[1] "Whew, I might have to be about done after this one..."
                    "One girl tipsy, and one girl drunk. You should probably call it a night soon."
                elif the_group[1].is_tipsy:
                    the_group[1] "Yeah! What a fun night!"
                    "The two girls are getting a bit tipsy. This could turn into a very fun night for you with another drink or two..."
                else:
                    "You can tell from her attitude that [the_group[0].title] is starting to get a little tipsy."
            elif the_group[1].is_drunk:
                the_group[0] "You okay there, [the_group[1].fname]?"
                the_group[1] "Sorry, I might need to be done soon..."
                "[the_group[0].title] shows some concern for [the_group[1].possessive_title], who is obviously drunk."
                "You might need to call it a night soon, for her sake."
            elif the_group[1].is_tipsy:
                the_group[1] "Yum! Another drink, these are starting to feel good. What now?"
                "You can tell from her attitude that [the_group[1].title] is starting to get a little tipsy."
            else:
                "The girls gratefully take their drinks. After a few sips, they turn to you again."
                the_group[1] "This is turning into a fun night. What now?"


        $ the_group[0].increase_drink_level(1)
        $ the_group[1].increase_drink_level(1)

        call screen main_choice_display(build_menu_items([build_group_bar_date_menu_items(the_group, previous_actions = selected_actions)]))
        $ round_choice = _return
        $ selected_actions.append(round_choice)
        if round_choice == "leave":
            $ round_number = 99
        else:
            $ round_number += 1
            call bar_group_date_choice_label(the_group, round_choice) from _bar_group_date_round_choice_split_01
        if the_group[0].is_wasted or the_group[1].is_wasted:  #too many
            $ round_number = BAR_DATE_ROUNDS
    if drinks_only: #If this label was called for the drink portion only, exit now
        return

    #Next, figure out if we are going home with one or both girls.

    return

label bar_date_choice_label(the_person, the_choice):    # I split this into it's own label to keep the code above cleaner.
    #Only use this label to call the correct label.
    if the_choice == "leave":
        return
    if the_choice == "get to know": # special option only visible for unique chars that have appropriate label
        $ label_name = bar_date_get_to_know_label(the_person)
        $ renpy.call(label_name)
        return

    if the_choice == "relax":
        call bar_date_relax_label(the_person) from _bar_date_choice_labels_001
    elif the_choice == "shots":
        call bar_date_do_shots_label(the_person) from _bar_date_choice_labels_002
    else:
        $ label_name = "bar_date_" + the_choice + "_label"
        $ run_named_label(label_name, the_person)
    return

label bar_group_date_choice_label(the_group, the_choice):
    #Only use this label to call the correct label.
    if the_choice == "leave":
        return

    if the_choice == "relax":
        call bar_group_date_relax_label(the_group) from _bar_group_date_choice_labels_001
    elif the_choice == "shots":
        call bar_group_date_do_shots_label(the_group) from _bar_group_date_choice_labels_002
    else:
        $ label_name = "bar_group_date_" + the_choice + "_label"
        $ run_group_named_label(label_name, the_group)
    return

#### Generic bar date actions ####
# Date small talk equivalent
label bar_date_relax_label(the_person):
    "You and [the_person.possessive_title] step over to one of the open tables to just relax and chat while you drink."
    $ the_person.draw_person(position = "sitting")
    $ sex_opinion_options = False
    $ SB_discover_opinion_count = 0
    if the_person.effective_sluttiness() >= 50:
        "She seems pretty open about her sexuality, so you feel like you could ask her about anything."
        $ sex_opinion_options = True
    elif the_person.is_drunk:
        "She's had a few drinks, so you feel like you could probably push her limits some and ask about just about anything..."
        $ sex_opinion_options = True
    else:
        "You use the opportunity to ask her about some of her opinions."
    menu:
        "Ask about general opinions":
            "You spend some time getting to know her general opinions."
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["general"])
        "Ask about work opinions":
            "You spend some time asking her about her work life and preferences."
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["work"])
        "Ask about style opinions":
            "You spend some time asking about her sense of style and preferences."
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["style"])
        "Positions" if sex_opinion_options:
            mc.name "So, how do you feel about different sexual positions, [the_person.title]?"
            if the_person.effective_sluttiness() < 50:
                "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
                $ the_person.change_slut(1, 40)
            else:
                "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
                $ the_person.change_happiness(2)
            the_person "Well..."
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["positions"])
        "Sex types" if sex_opinion_options:
            mc.name "So, how do you feel about different types of sex, [the_person.title]?"
            if the_person.effective_sluttiness() < 50:
                "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
                $ the_person.change_slut(1, 40)
            else:
                "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
                $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["sex_types"])
        "Cum" if sex_opinion_options:
            mc.name "So, how do you feel about cum, [the_person.title]?"
            if the_person.effective_sluttiness() < 50:
                "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
                $ the_person.change_slut(1, 40)
            else:
                "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
                $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["cum"])
        "Sexy Clothing" if sex_opinion_options:
            mc.name "So, how do you feel about sexy clothing and outfits, [the_person.title]?"
            if the_person.effective_sluttiness() < 50:
                "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
                $ the_person.change_slut(1, 40)
            else:
                "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
                $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["sexy_clothing"])
        "Other Kinks" if sex_opinion_options:
            mc.name "So, do you have any kinks, [the_person.title]? Something that might be more fun for me to know about?"
            if the_person.effective_sluttiness() < 50:
                "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
                $ the_person.change_slut(1, 40)
            else:
                "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
                $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_person, relax_discussion_topics["kinks"])
    if SB_discover_opinion_count == 0:
        "Unfortunately you don't feel like you learn much about her."
    "You chat with [the_person.possessive_title] for a bit longer, but eventually you finish your drinks."
    return False

label bar_group_date_relax_label(the_group):
    "You step over to a table with girls to just relax and chat while you drink."
    $ scene_manager.update_actor(the_group[0], display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.update_actor(the_group[1], position = "sitting")
    $ sex_opinion_options = False
    "Small talk commences for a while."
    "You glance at [the_group[0].title]."
    if the_group[0].effective_sluttiness() >= 50:
        "She seems pretty open about her sexuality, so you feel like you could ask her about anything."
        if the_group[1].effective_sluttiness() >= 50:
            "Looking over at [the_group[1].possessive_title], she is the same way. Maybe you should spice up the conversation a bit."
        elif the_group[1].is_drunk:
            "Looking over at [the_group[1].possessive_title], she seems drunk enough to push her limits a bit. Maybe you should spice up the conversation a bit."
        else:
            "Looking over at [the_group[1].possessive_title] though, you quickly decide to keep discussion topics tame."
    elif the_group[0].is_drunk:
        "You glance at [the_group[0].title]."
        "She's had a few drinks, so you feel like you could probably push her limits some and ask about just about anything..."
        if the_group[1].effective_sluttiness() >= 50:
            "Looking over at [the_group[1].possessive_title], she is pretty open about her sexuality. Maybe you should spice up the conversation a bit."
        elif the_group[1].is_drunk:
            "Looking over at [the_group[1].possessive_title], she seems drunk too. Maybe you should spice up the conversation a bit."
        else:
            "Looking over at [the_group[1].possessive_title] though, you quickly decide to keep discussion topics tame."
    else:
        "She probably wouldn't appreciate you asking about anything intimate. You should probably keep discussion topics tame."
    "You decide to change the direction of conversation for a bit."
    menu:
        "Ask about general opinions":
            "You spend some time getting to know their general opinions."
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["general"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["general"])
        "Ask about work opinions":
            "You spend some time asking them about their work life and preferences."
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["work"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["work"])
        "Ask about style opinions":
            "You spend some time asking about their sense of style and preferences."
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["style"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["style"])
        "Positions" if sex_opinion_options:
            "You spend some time asking the girls about their favorite sexual positions."
            # mc.name "So, how do you feel about different sexual positions, [the_person.title]?"
            # if the_person.effective_sluttiness() < 50:
            #     "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
            #     $ the_person.change_slut(1, 40)
            # else:
            #     "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
            #     $ the_person.change_happiness(2)
            # the_person "Well..."
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["positions"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["positions"])
        "Sex types" if sex_opinion_options:
            "You spend some time asking the girls about different types of sex."
            # mc.name "So, how do you feel about different types of sex, [the_person.title]?"
            # if the_person.effective_sluttiness() < 50:
            #     "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
            #     $ the_person.change_slut(1, 40)
            # else:
            #     "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
            #     $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["sex_types"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["sex_types"])
        "Cum" if sex_opinion_options:
            "You spend some time asking the girls how, and where, men cum when they have sex."
            # mc.name "So, how do you feel about cum, [the_person.title]?"
            # if the_person.effective_sluttiness() < 50:
            #     "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
            #     $ the_person.change_slut(1, 40)
            # else:
            #     "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
            #     $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["cum"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["cum"])
        "Sexy Clothing" if sex_opinion_options:
            "You spend some time asking the girls how they feel about wearing revealing outfits and lingerie."
            # mc.name "So, how do you feel about sexy clothing and outfits, [the_person.title]?"
            # if the_person.effective_sluttiness() < 50:
            #     "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
            #     $ the_person.change_slut(1, 40)
            # else:
            #     "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
            #     $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["sexy_clothing"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["sexy_clothing"])
        "Other Kinks" if sex_opinion_options:
            "You spend some time asking the girls about various kinks and desires."
            # mc.name "So, do you have any kinks, [the_person.title]? Something that might be more fun for me to know about?"
            # if the_person.effective_sluttiness() < 50:
            #     "She pauses for a moment, but her alcohol addled brain loosens her inhibitions enough to answer."
            #     $ the_person.change_slut(1, 40)
            # else:
            #     "[the_person.possessive_title!c] smiles when she realises you are going to keep the topic interesting."
            #     $ the_person.change_happiness(2)
            $ SB_discover_opinion_count = display_topic_opinions(the_group[0], relax_discussion_topics["kinks"])
            $ SB_discover_opinion_count = display_topic_opinions(the_group[1], relax_discussion_topics["kinks"])
    if SB_discover_opinion_count == 0:
        "Unfortunately you don't feel like you learn much about them."
    "You finish up your drinks as the conversation dies down."
    return

# Do a few shots to jump start drunk stuff
label bar_date_do_shots_label(the_person):
    $ shot_count = 1
    $ shot_name = get_random_from_list(list_of_shots)
    mc.name "Let's go to the bar and do some shots!"
    if the_person.is_drunk:
        the_person "Umm, I've already had a lot... just one, okay?"
    elif the_person.is_tipsy:
        the_person "Okay, I think I'm down for a couple."
        $ shot_count = 2
    else:
        the_person "Oh, let's get things started fast? Okay!"
        $ shot_count = 3
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title] and get the bartender's attention."
    mc.name "Can we get some [shot_name] here?"
    "A minute later, the shots are in front of you and [the_person.title]."
    mc.name "Bottom's up!"
    if the_person.effective_sluttiness() >= 60:
        the_person "Not yet, but I'm sure my bottom will be up later."
        $ the_person.change_arousal(5)
        "She gives you a not so subtle wink, then takes her shot."
        $ mc.change_locked_clarity(10)
    elif the_person.effective_sluttiness() >= 40 or the_person.opinion.giving_blowjobs > 1:
        "Instead of reaching for the shot glass, [the_person.title] leans forward and takes the shot glass in her mouth, then leans back, tipping the shot into her mouth and drinking it."
        "She leans forward and sets the shot glass on the bar, then turns and gives you a not so subtle wink."
    else:
        the_person "Cheers!"
        "You clink your shot glasses together, then she takes her shot and sets it on the bar."
    "You take your shot as well."
    $ the_person.increase_drink_level(1)
    if shot_count >= 2:
        "You take a moment, then move on to the next shot."
        "You pick yours up and she does the same. You offer a toast."
        menu:
            "To Work" if the_person.is_employee:
                mc.name "To my employee, whose hard work helped fund the business that paid for this outing tonight!"
                "She rolls her eyes but smiles."
            "To Lovers" if not the_person.has_taboo("vaginal_sex"):
                mc.name "To lovers, who find comfort and joy in each other's company."
                "She smiles."
            "To Family" if the_person.is_family:
                mc.name "To family, for the love of a family is life's greatest blessing."
                "She seems surprised by your toast, but smiles."
            "To Spouses" if the_person.is_affair:
                mc.name "To husbands, fiancees, and boyfriends. I hope I will never meet."
                "She rolls her eyes but smiles."
            "To Alcohol":
                mc.name "To alcohol, and may the best of the past be the worst of the future."
                "She rolls her eyes but smiles."
            "To Sluts" if the_person.effective_sluttiness() >= 60:
                mc.name "To sluts and country roads. May they always take me home!"
                "She laughs and nods."
        the_person "Hear hear!"
        $ the_person.increase_drink_level(1)
        "You take your shots together."
    if shot_count >= 3:
        "Two down, one to go."
        if the_person.effective_sluttiness("bare_tits") > 40:   #Body shot
            "You look at your shots, then get a fun idea."
            mc.name "Hey [the_person.title], can I do a body shot for the last one?"
            the_person "Ah, I guess since you're buying I could go along with that!"
            #Split based on what is legal.
            if mc.business.public_sex_act_is_legal:   #She goes topless, allows MC to lick salt off her nipples and take the shot.
                if the_person.tits_visible and the_person.tits_available:
                    "She scoots a little closer to you."
                else:
                    "She quickly takes her top off."
                    $ the_person.strip_to_tits(prefer_half_off = False, position = "sitting")
                    "Then she scoots a little closer to you."
                $ the_person.draw_person(position = "sitting", display_transform = character_right(zoom = 1.3))
                the_person "Let's make this a fun one."
                "She reaches over and grabs a slice of lime and a salt shaker off the counter."
                "She squeezes out some lime juice onto each of her nipples, one at a time, then sprinkles some salt on the just the left."
                "Then she takes the shot of alcohol can carefully holds it in place in her cleavage. You notice several guys around the bar have taken notice, including the bartender."
                $ the_person.draw_person(position = "kneeling1", display_transform = character_right(zoom = 1.3))
                the_person "Alright, ready!"
                "You lean forward and lick her salted nipple. You take your time, opening your mouth wide and sucking on her nipple for several seconds."
                $ the_person.change_arousal(5)
                $ mc.change_locked_clarity(15)
                if the_person.is_lactating:
                    "A little bit of milk starts to leak from her nipple."
                    the_person "Hey, don't make me let down! That isn't part of the shot..."
                "You move your face over to her cleavage, taking the shot glass with your mouth, quickly tipping it back and swallowing it."
                "Then you move to her other breast, eagerly licking the sour lime juice and suckling her nipple for several more seconds."
                $ the_person.change_arousal(15)
                $ mc.change_locked_clarity(25)
                the_person "MMMmmm...."
                "She lets out a moan as you finish, sitting back. You can hear a few guys around the bar murmuring their jealousy..."
                the_person "Wow, now THAT was nice..."
                $ the_person.draw_person(position = "sitting")
                "She turns back to her shot, and quickly takes it."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person(position = "sitting")
            if mc.business.topless_is_legal:  #She goes topless, but doesn't take things beyond that.
                if the_person.tits_visible and the_person.tits_available:
                    "She scoots a little closer to you."
                else:
                    "She quickly takes her top off."
                    $ the_person.strip_to_tits(prefer_half_off = False, position = "sitting")
                    "Then she scoots a little closer to you."
                "She reaches over and grabs the shot, holding it carefully in her cleavage. You grab a slice of lime and the salt shaker."
                $ the_person.draw_person(position = "kneeling1", display_transform = character_right(zoom = 1.3))
                "You sprinkle a bit of salt onto you tongue, then lean forward, putting your face into her cleavage."
                "You hold it there a few moments longer then necessary, enjoying her soft tit flesh, slowly picking up the shot glass with your mouth, then tipping it back and swallowing it."
                $ the_person.change_arousal(5)
                $ mc.change_locked_clarity(15)
                "Then you take the slice of lime and suck on the end of it."
                the_person "Mmm, that was nice..."
                $ the_person.draw_person(position = "sitting")
                "She turns back to her shot, and quickly takes it."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person(position = "sitting")
            elif the_person.wearing_bra:
                if the_person.tits_visible and the_person.tits_available:
                    "She scoots a little closer to you."
                else:
                    "She quickly takes her top off, exposing her bra."
                    $ the_person.strip_top_to_underwear(prefer_half_off = False, position = "sitting")
                    "Then she scoots a little closer to you."
                "She reaches over and grabs the shot, holding it carefully in her cleavage. You grab a slice of lime and the salt shaker."
                $ the_person.draw_person(position = "kneeling1", display_transform = character_right(zoom = 1.3))
                "You sprinkle a bit of salt onto you tongue, then lean forward, putting your face into her cleavage."
                "You hold it there a few moments longer then necessary, enjoying her soft tit flesh, slowly picking up the shot glass with your mouth, then tipping it back and swallowing it."
                $ the_person.change_arousal(5)
                $ mc.change_locked_clarity(15)
                "Then you take the slice of lime and suck on the end of it."
                the_person "Mmm, that was nice..."
                $ the_person.draw_person(position = "sitting")
                "She turns back to her shot, and quickly takes it."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person(position = "sitting")
            else:
                "She looks around for a moment, then leans in and whispers in your ear."
                the_person "You'll have to go fast, I'm not wearing a bra!"
                mc.name "Deal."
                "She scoots closer to you while you grab the salt and a lime wedge."
                "You give her a little nod as you sprinkle a little salt on your tongue."
                "She quickly pulls up her shirt, exposing her tits."
                $ the_person.strip_to_tits(prefer_half_off = True, position = "kneeling1", display_transform = character_right(zoom = 1.3))
                "She grabs the shot and holds it in her cleavage while you quickly lean forward and grab the shot glass with your mouth."
                "You tip it up and swallow it, then suck on the lime wedge while she straightens out her clothes."
                $ the_person.restore_all_clothing()
                $ the_person.draw_person(position = "sitting")
                "She turns back to her shot, and quickly takes it."
                "You hear a couple hoots from around the bar from people who noticed. The bartender comes over."
                "Bartender" "Hey now, that's enough of that. Do that again and I'll have to kick you out, understand?"
                mc.name "Yes Sir."
            "[the_person.possessive_title!c] straightens her clothing out."

        else:
            "You take the last shot glass in your hand and turn to [the_person.title]."
            mc.name "Sorry, I don't have anything witty for this one. Cheers?"
            the_person "Cheers!"
            "You clink your shot glasses together and then take them at the same time."
            "She grimaces a bit after."
        $ the_person.increase_drink_level(1)
        the_person "Alright, no more shots for tonight!"
        mc.name "Agreed."
    "You use your regular drinks to help chase down your shots, making small talk as you sit at the bar, but eventually they run dry."
    return

label bar_group_date_do_shots_label(the_group):
    $ shot_count = 1
    $ shot_name = get_random_from_list(list_of_shots)
    mc.name "Let's go to the bar and do some shots!"
    if the_group[0].is_drunk or the_group[1].is_drunk:
        "You decide given the state of the girls that you should probably kept it to just one shot."
    elif the_group[0].is_tipsy or the_group[1].is_tipsy:
        "The girls are feeling good, but you don't want to push things to far, so you decide to order two shots each."
        $ shot_count = 2
    else:
        "The girls seem excited about getting the night of drinking started. You order three shots each."
        $ shot_count = 3
    "You girls take seats at the bar and you sit between them. You get the bartender's attention."
    $ scene_manager.update_actor(the_group[0], display_transform = character_left_flipped, position = "sitting")
    $ scene_manager.update_actor(the_group[1], position = "sitting")
    mc.name "Can we get some [shot_name] here?"
    "A minute later, the shots are in front of you. You quickly pass them out."
    mc.name "Bottom's up!"
    if the_group[0].effective_sluttiness() >= 60:
        the_group[0] "Hopefully that's not the last time you tell me that tonight!"
        if the_group[1].effective_sluttiness() >= 60:
            "[the_group[1].title] snorts a moment laughing."
            the_group[1] "Don't worry [the_group[0].fname]. If he doesn't ask you to stick your bottom up tonight, I will!"
            "The girls laugh and take their shots."
        else:
            "[the_group[1].title] laughs to herself, then lifts her shot glass."
            "The girls take their shots."
    else:
        "The girls take their shots."
    $ the_group[0].increase_drink_level(1)
    $ the_group[1].increase_drink_level(1)
    if shot_count >= 2:
        "You take a moment between shots. [the_group[1].possessive_title] is the first to raise her second glass."
        the_group[1] "Alright, my turn for a toast."
        if the_group[1].effective_sluttiness() >= 60:
            the_group[1] "Here's to the storks that bring babies, and to the swallows that don't!"
            "You and [the_group[0].title] laugh at her toast and raise your glasses."
            if the_group[0].effective_sluttiness() >= 60:
                the_group[0] "Ah yes, to staying positive and testing negative!"
        else:
            the_group[1] "May the best of your past be the worst of your future!"
            "You and [the_group[0].title] laugh at her toast and raise your glasses."
        "You take your shots together."
        $ the_group[0].increase_drink_level(1)
        $ the_group[1].increase_drink_level(1)
    if shot_count >= 3:
        "You take a moment between shots. [the_group[0].possessive_title] takes the initiative for the final toast."
        the_group[0] "Alright, my turn for a toast, I'm not very good at these but let's see..."
        "You raise your glasses together."
        if the_group[0].effective_sluttiness() >= 60:
            the_group[0] "This one's for rattlesnakes and condoms... Two things I don't fuck with!"
        elif the_group[0].is_drunk:
            the_group[0] "As they say in the furniture business… CHAIRS!"
            "You shake your head and [the_group[1].title] laughs at her horrible, drunken toast."
        else:
            the_group[0] "Here's to twice-baked bread... Without which we would have no toast"
        "You clink your glasses together and you take your shots."
        $ the_group[0].increase_drink_level(1)
        $ the_group[1].increase_drink_level(1)
    "You sit at the bar a little longer with the girls, finishing off the last of your drinks, but eventually they run dry."
    return


# If we've unlocked the appropriate policies
label bar_date_booth_label(the_person):
    #OUTLINE
    "In this label we have sex with [the_person.title] in the sex booth."
    return False

label bar_group_date_booth_label(the_group):
    #OUTLINE
    "In this label we have sex with the girls in the sex booth."
    return False



#### Bar date games ####










#Fetish interrupt labels
label bar_date_cum_fetish_interrupt_label(the_person):
    pass
    return

label bar_date_anal_fetish_interrupt_label(the_person):
    pass
    return

label bar_date_breeding_fetish_interrupt_label(the_person):
    pass
    return

label bar_date_exhibition_fetish_interrupt_label(the_person):
    pass
    return


#Group fetish interrupts
label bar_date_group_cum_fetish_interrupt_label(the_person):
    pass
    return

label bar_date_group_anal_fetish_interrupt_label(the_person):
    pass
    return

label bar_date_group_breeding_fetish_interrupt_label(the_person):
    pass
    return

label bar_date_group_exhibition_fetish_interrupt_label(the_person):
    pass
    return



###NOTE One night stand actions got moved to dates.rpy###
