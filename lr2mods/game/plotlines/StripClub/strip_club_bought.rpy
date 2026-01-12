## Stripclub storyline Mod by Corrado
# You actually buy the stripclub and hire the strippers.

init 5 python:
    # for testing purposes, convert strip club to player owned.
    def test_strip_club():
        strip_club.old_owner = strip_club.owner
        strip_club.old_name = strip_club.formal_name
        mc.business.event_triggers_dict["foreclosed_day"] = day
        strip_club.owner = "Foreclosed"
        strip_club.formal_name = "Foreclosed"
        set_strip_club_foreclosed_stage(4)
        add_cousin_stripping_and_setup_search_room_action(aunt, cousin)
        cousin.secondary_job.job_known = True
        strip_club.formal_name = "Starlight Club"
        strip_club.visible = True
        add_strip_club_hire_employee_action_to_mc_actions()
        for stripper in mc.business.stripclub_strippers:
            print(f"Update stripper title {stripper.name}")
            stripper.set_title(get_random_from_list(stripper.get_titles()))
            stripper.set_mc_title("Boss")
            stripper.set_possessive_title("your stripper")
            stripper.change_stats(happiness = 10, obedience = 5, love = 5)
        mc.change_location(strip_club)
        renpy.call("strip_club_bought_strippers_selection_label", cousin)
        return

label strip_club_bought_strippers_selection_label(the_person): # Talk event
    $ clear_scene()
    $ the_person.draw_person()
    mc.name "Hey [the_person.title], good, you came."
    the_person "Yeah, I'm here, now tell me why I'm here."
    mc.name "Not yet, can you call all your old coworkers from the strip club and get them here as soon as possible?"
    the_person "You are a weird pervert, you know. But fine, I'll humour you."
    "She talks on the phone for a while."
    the_person "Right, I was able to contact them all, they will be here as soon as they can."
    mc.name "Good, come, let's go inside."
    the_person "You have keys for this place? You must have been a very good customer for that cheap fuck to give you some keys."
    $ strip_club.background_name = "Club_Background" # Set up the original background
    $ mc.location.show_background()
    "You just smile and take her inside. About 30 minutes later, they're all there, eager to get their jobs back."
    $ scene_manager = Scene()
    $ scene_manager.add_group(mc.business.stripclub_strippers, emotion = "default")
    the_person "Okay [mc.name], we're all here... Actually, what are we doing here? You wanted a private party?"
    mc.name "Calm your tits [the_person.title], I'm here because I bought this place and now it belongs to me."
    "The girls all stare at you in surprise."
    mc.name "If you all are still looking to get your old jobs back, I think we need to discuss it a bit, don't you agree?"
    $ scene_manager.update_actor(the_person, emotion = "angry")
    the_person "You bought this place, [mc.name]? Really? What does that mean for us? We can get our old jobs back? What about our back pay?"
    mc.name "For your back pay, I can't do anything about that. The money [strip_club.old_owner] owed you is gone."
    mc.name "I'm not stupid, so I recognise that hiring skilled and experienced workers has its advantages."
    mc.name "Here's my offer: you girls show me your skills on the stage, and I will decide if I'm going to give you your old job back..."
    mc.name "If my evaluation is positive, you sign the new contract, and I'll pay you a $500 signing bonus."
    $ scene_manager.update_actor(the_person, emotion = "default")
    the_person "And what will be our daily salary?"
    mc.name "I'll calculate it based on your skills on the stage. Sexy girls attract more customers; more customers, more profit, so you get a better salary."
    # one stripper does not apply
    $ the_person = get_random_from_list([x for x in mc.business.stripclub_strippers if x != cousin and x.personality != alpha_personality])
    $ scene_manager.update_actor(the_person, display_transform = character_right)
    the_person "[mc.name], I'm sorry to interrupt, but in the meantime I found another job, it doesn't pay as much as stripping, but it gives me enough to live, so..."
    mc.name "Well, I can't force anyone to stay, if one day you decide that you need more cash to get by, I'll give you your chance, but let me wish you the best with your new job."
    the_person "Now I'm a little sad, [mc.name]... Finally this could become a real 'Gentleman's Club', with you here..."
    the_person "I hope to see you again someday, thank you for your understanding."
    $ scene_manager.update_actor(the_person, position = "kissing", emotion = "happy")
    "She leans on you, placing a hand on your chest and giving you a soft kiss on your cheek."
    the_person "Goodbye, [mc.name]!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    if the_person.is_stranger:
        mc.name "Goodbye!"
    else:
        mc.name "Goodbye, [the_person.title]!"
    $ scene_manager.remove_actor(the_person)
    $ the_person.change_stats(happiness = 5, obedience = 3, love = 3)
    $ the_person.set_override_schedule(None, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4])
    $ the_person.change_job(get_random_from_list((home_improvement_cashier_job, electronics_cashier_job, store_assistant_job, hotel_maid_job, waitress_job)), start_day = day + 1)
    $ the_person.change_location(the_person.home)

    # resume dialogue with
    $ the_person = cousin
    $ scene_manager.add_actor(the_person, display_transform = character_right)
    the_person "I still don't know if I want my old job back... I mean, of course I want it, I just don't know if I will enjoy working for you."
    mc.name "Your choice, [the_person.title], but only after {b}my{/b} choice to hire you or not. Don't forget who's the boss here now."
    $ the_person.change_obedience(10)
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "I like the job, and most importantly, I like the money... I can manage a working relationship with you."
    mc.name "Okay girls, if we haven't met before, do a quick introduction and then start stripping. Let's get the music started, and show me your best! Who wants to go first?"

    # loop remaining strippers and hire
    $ scene_manager.hide_actors()
    $ strippers = mc.business.stripclub_strippers[:]
    while builtins.len(strippers) > 0:
        $ the_person = get_random_from_list(strippers)
        $ the_person.set_override_schedule(None, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4])
        call strip_club_evaluate_stripper(the_person) from _call_strip_club_evaluate_stripper_selection
        $ strippers.remove(the_person)

    $ strippers = None
    $ scene_manager.show_all_actors()

    if builtins.len(mc.business.stripclub_strippers) > 1:
        mc.name "Okay girls, the team is built. Enjoy the rest of your day, we will reopen the club tomorrow evening."
        "Excited to have got back their jobs and the unexpected pay raises, the girls get dressed while you watch them."
        $ scene_manager.apply_outfits(planned_outfits = True)
        mc.name "That's it for now, see you all at your next shift."
        $ scene_manager.update_group(position = "walking_away")
        "With that the girls walk out of the club."
        $ scene_manager.clear_scene()
        $ scene_manager = None
    elif builtins.len(mc.business.stripclub_strippers) > 0:
        mc.name "Okay [mc.business.stripclub_strippers[0].name], I will count on you. Enjoy the rest of the day, we will re-open the club tomorrow evening."
        $ scene_manager.apply_outfits(planned_outfits = True)
        "Excited to have got back her job and the unexpected pay raise, the girl puts her clothes back on and walks out."
        $ scene_manager.clear_scene()
        $ scene_manager = None
    else:
        mc.name "Damn, I bought a stripclub and now I don't have any strippers..."
        mc.name "I'd better hurry and find someone to work here fast, if I want to reopen this place."

    $ set_strip_club_foreclosed_stage(5)
    $ add_strip_club_hire_employee_action_to_mc_actions()

    "As the last one left in the club, you turn off the lights, close the doors, and return home eager for a good night's rest."
    $ mc.change_location(bedroom)
    $ add_strip_club_manager_reminder_action()
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_club_bought_strippers_selection
    # since we are in a talk event with Gabrielle, we need to exit using a jump.
    return

label strip_club_evaluate_stripper(the_person):
    python:
        scene_manager.apply_outfit(the_person, mc.business.stripper_wardrobe.pick_random_outfit())
        the_person.draw_person(emotion = "happy", position = "stand4")
        the_person.quit_job(stripper_job)   # every girls quits being a normal stripper

    "A new song starts playing over the speakers and a stripper moves elegantly up on the stage."

    if the_person.is_stranger:
        $ the_person.set_title()
        $ the_person.set_mc_title("Boss")
        $ the_person.set_possessive_title("the stripper")
        $ the_person.set_event_day("day_met")
        the_person "Hi [the_person.mc_title], my name is [the_person.title] and I'm [the_person.age] years old."

    "She shows off a few poses, then she starts to strut down the walkway and stops at the end of the stage."
    "[the_person.title] starts to dance to the music, swinging her hips and turning slowly to show herself off."
    $ the_person.draw_person(position = "back_peek")
    "She spins and poses for you, and you can easily imagine a crowd responding with whoops and cheers."
    if the_person.has_large_tits:
        if the_person.tits_available:
            "As the music builds, [the_person.title]'s dance becomes more energetic. Her [the_person.tits_description] bounce and jiggle in rhythm with her movements."
        else:
            "As the music builds, [the_person.title]'s dance becomes more energetic. Her big tits bounce and jiggle, looking almost desperate to escape her clothing."
    else:
        "As the music builds, [the_person.title]'s dance becomes more energetic. She runs her hands over her tight body, accentuating her curves."
    $ the_person.draw_person(position = get_random_from_list(cousin_strip_pose_list))
    "Her music hits its crescendo and her dancing does the same. [the_person.title] holds onto the pole in the middle of the stage and spins herself around it."
    $ the_person.draw_person(position = "doggy")
    if the_person.vagina_visible:
        "As the song comes to an end, the dancer lowers herself to all fours, showing off her ass and pussy."
    else:
        "As the song comes to an end, the dancer lowers herself to all fours. She spreads her legs and works her hips, jiggling her ass for your amusement."
    $ the_person.draw_person()
    "She stands up and gives you a coy smile, hoping for your final approval."
    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.title]'s body as she walks offstage to rejoin you and the other girls."
    $ the_person.draw_person(emotion = "happy")
    the_person "So [mc.name] what do you think, am I good enough to be one of your girls?"
    "She puts a hand on your shoulder pressing her bosom against your body..."
    menu:
        "Yes" if mc.business.has_funds(500):
            $ the_person.change_job(stripclub_stripper_job, is_primary = (the_person != cousin), job_known = True, start_day = day + 1)
            mc.name "Yes, you impressed me! Your salary will be $[the_person.primary_job.salary:.2f] per day excluding tips, if you agree?"
            $ ran_num = builtins.int(((the_person.primary_job.base_salary / 20) - 1) * 100)
            if ran_num < 5: # make sure we are >= 5%
                $ ran_num = 5
            the_person "If I agree? Of course, that's [ran_num]%% more than what [strip_club.old_owner] paid me before!"
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "Without any forewarning she pushes her tongue into your mouth showing you her happiness and gratitude."
            $ mc.business.change_funds(-500, stat = "Salaries")
            $ the_person.set_possessive_title("your stripper")
            $ the_person.draw_person(emotion = "happy")
            "After a few seconds, when she stops, you give her the promised signing bonus."
            $ the_person.change_stats(happiness = 5, obedience = 3, love = 3)
        "Yes\n{menu_red}Insufficient funds{/menu_red} (disabled)" if not mc.business.has_funds(500):
            pass
        "Maybe later": # Don't need to reschedule
            $ the_person.draw_person(emotion = "sad", position = "stand2")
            "[the_person.title] was so sure she would get back her job she can't utter a single word."
            "She can't believe your decision, and in a few seconds her face is striped by copious tears."
            $ the_person.apply_outfit(the_person.planned_outfit, show_dress_sequence = True)
            $ the_person.draw_person(emotion = "sad", position = "walking_away")
            if the_person == cousin:
                "Humiliated like never before, [the_person.title] quickly dresses back up and walks out of the club."
                $ the_person.change_stats(happiness = -10, obedience = 3, love = -5)
            else:
                "Unable to argue with you, [the_person.title] quickly dresses back up and leaves the club, still in tears."
                $ the_person.change_job(unemployed_job)
            $ the_person.change_location(the_person.home)
            $ scene_manager.remove_actor(the_person) # make sure we don't draw her after selection
    return
