init 2 python:
    # Follow Me Requirements
    def mc_start_follow_requirement(person):
        return not person.follow_mc and person.love > 20 and person.obedience >= 120

    def mc_stop_follow_requirement(person):
        return person.follow_mc

    def mc_action_lasik_surgery_person_requirement(person):
        if person.love < 20: # you need have some connection with her to offer this
            return False
        if person.has_event_day("lasik_surgery"):
            return False

        if isinstance(person.base_outfit, Outfit) and person.base_outfit.has_glasses:
            if person.love < 30:
                return "Requires: 30 Love"
            if not mc.business.has_funds(5000):
                return "Not enough money"
            return True
        return False

    def perform_lasik_surgery_requirement(start_day):
        return day > start_day

    def after_lasik_surgery_requirement(person):
        return True

    #REMOVED: Feature would mess-up dynamic function binding
    def mc_action_rename_person_requirement(person):
        return False

    # Spend the Night Requirements
    def mc_action_spend_the_night_requirement(person):
        if time_of_day == 4 and person.love > 50 and mc.is_at(person.home): #Has to be night, need to have some love and be in the_person's home location
            return True
        return False

    def mc_remove_person_requirement(person):
        return person in known_people_in_the_game(unique_characters())

    def do_a_favour_requirement(person):
        if not ActionMod.is_mod_enabled(do_a_favour_action):
            return False

        if mc.energy < 15:
            return "Requires: {energy=15}"
        if person.has_event_delay("obedience_favour", 1): #once per day
            return True
        return "Asked for a favour too recently"

init 5 python:
    mc_start_follow_action = ActionMod("Follow me", mc_start_follow_requirement, "mc_start_follow_label", menu_tooltip = "Ask a girl to follow you around town.", category = "Generic People Actions")
    mc_stop_follow_action = ActionMod("Stop following me", mc_stop_follow_requirement, "mc_stop_follow_label", menu_tooltip = "Ask the girl stop following you.", allow_disable = False, category = "Generic People Actions")

    # Spend the Night | Allows you to sleep in the home of a person you have increased the love stat.
    mc_spend_the_night_action = ActionMod("Spend the night with girl", mc_action_spend_the_night_requirement, "mc_spend_the_night_label", menu_tooltip = "Allows you to sleep in this location.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    mc_lasik_surgery_action = ActionMod("Pay for LASIK surgery\n{menu_red}Costs: $5000{/menu_red}", mc_action_lasik_surgery_person_requirement, "mc_action_lasik_surgery_label", menu_tooltip = "You don't like a girl wearing glasses, offer to pay for LASIK surgery.", category = "Generic People Actions")

    mc_remove_person_action = ActionMod("Remove from game", mc_remove_person_requirement, "mc_remove_person_label", menu_tooltip = "You are not interested in a girl. This will remove her from the game.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    main_character_actions_list = [mc_start_follow_action, mc_stop_follow_action, mc_spend_the_night_action, mc_lasik_surgery_action, mc_remove_person_action]

    do_a_favour_action = ActionMod("Ask for a Favour   {energy=-15}", do_a_favour_requirement, "do_a_favour_label", category = "Generic People Actions", initialization = init_action_mod_disabled,
        menu_tooltip = "Ask for a favour. Successfully asking for a favour tends to build obedience in your relationship.")
    chat_actions.append(do_a_favour_action)

# NOTE: Not sure where to place these actions yet. Basically actions that could fit on any person regardless of role.
label mc_spend_the_night_label(person): # Consider adding the sleep_action to the_person's room, but stats jump all over the place so doesn't necessarily make sense.
    "You go to sleep in [person.home.formal_name]."
    $ the_person.change_stats(happiness = 5, love = 3)
    call advance_time() from _call_advance_time_spend_the_night
    return

# Follower Labels
label mc_start_follow_label(person):
    "You tell [person.title] to follow you around."

    $ the_person.follow_mc = True
    person "Ok, let's go."
    jump game_loop      # exit talk menu

label mc_stop_follow_label(person):
    python:
        if the_person.get_destination() is the_person.home:
            schedule_destination = "my room"
        elif the_person.get_destination():
            schedule_destination = f"the {the_person.get_destination().formal_name}"
        else:
            schedule_destination = "somewhere else"

    "You tell [person.title] to stop following you around."

    $ the_person.follow_mc = False

    $ the_person.draw_person(position = "walking_away")

    $ the_person.run_move() # This will trigger stat changes based on clothing, but shouldn't be problematic although it can be exploited.

    the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."


    return

label mc_action_lasik_surgery_label(the_person):
    mc.name "[the_person.title], you have beautiful eyes, but they are always hidden behind your glasses."
    the_person "Don't you like them? I can wear different glasses tomorrow."
    mc.name "I mean, that I really would like to see you without any glasses."
    if renpy.random.randint(1,2) == 1:
        the_person "I'm sorry, but I can't wear lenses."
        mc.name "That's fine."
    else:
        the_person "If you like, I can start wearing lenses."
        mc.name "I don't think that's the right solution."

    mc.name "Could you take them off for a minute?"
    the_person "Sure."
    $ the_person.outfit.remove_glasses()
    $ the_person.draw_person()
    mc.name "Absolutely lovely."
    "She blushes a little at your comment."
    menu:
        "Offer LASIK surgery\n{menu_red}Costs: $5000{/menu_red}":
            mc.name "I made an appointment for you in the clinic for a LASIK surgery where your eyesight will be corrected."
            "[the_person.title] gives you a spontaneous hug."
            $ the_person.draw_person(position = "kissing")
            the_person "You make me so happy [the_person.mc_title], thank you so much!"
            "She puts her glasses back on, but she will let you know when the surgery is completed."
            python:
                the_person.change_stats(happiness = 10, love = 5, max_love = 80)
                mc.business.change_funds(-5000, stat = "Cosmetic Surgery")
                the_person.apply_planned_outfit()
                the_person.set_event_day("lasik_surgery")
                mc.business.add_mandatory_crisis(
                    Action("Perform LASIK surgery",
                        perform_lasik_surgery_requirement,
                        "perform_lasik_surgery_label",
                        requirement_args = [day + 2],
                        args = [the_person])
                )
        "Don't":
            mc.name "Thank you, [the_person.title]."
            the_person "Anytime, [the_person.mc_title]."
            $ the_person.apply_planned_outfit()
    return

label perform_lasik_surgery_label(the_person):
    python:
        the_person.base_outfit.remove_glasses()
        the_person.add_unique_on_room_enter_event(
            Action("After LASIK surgery", after_lasik_surgery_requirement, "after_lasik_surgery_label"),
        )
    return

label after_lasik_surgery_label(the_person):
    $ the_person.draw_person()
    the_person "Hello [the_person.mc_title], what do you think? Do I look good without glasses?"
    mc.name "Absolutely, you look amazing without glasses."
    the_person "Thank you."
    $ clear_scene()
    return

label mc_remove_person_label(person):
    menu:
        "Are you sure?":
            $ person.remove_person_from_game()
            $ jump_game_loop()
        "Reconsider":
            pass
    return

#Obedience Actions
label do_a_favour_label(the_person):
    mc.name "Hey. I was wondering if you would be willing to do me a favour."
    if the_person.obedience < 70:
        "[the_person.possessive_title!c] scoffs and rolls her eyes."
        the_person "Probably not, but shoot your shot, [the_person.mc_title]."
    elif the_person.obedience < 100:
        the_person "Maybe, what do you need?"
    elif the_person.obedience < 130:
        "[the_person.possessive_title!c] smiles."
        the_person "If I have time. What do you need?"
    else:
        "[the_person.possessive_title!c] smiles wide."
        the_person "Anything for you, [the_person.mc_title]."
    menu:
        "Small Favour":
            $ mc.change_energy(-15)
            $ favour_success = True
            if mc.is_home:
                mc.name "Hey, I'm a little short. Any chance I can borrow $5 to grab some coffee?"
                if favour_success:
                    the_person "Uhh, yeah I guess that would be okay."
                    "[the_person.possessive_title!c] grabs her purse and hands you a $5 bill from it."
                    mc.name "Thanks!"
                    $ mc.business.change_funds(5)
                    if the_person.obedience < 130:
                        $ the_person.change_obedience(1)
                else:
                    the_person "I'm not your personal bank account, [the_person.mc_title]."
                    mc.name "Ah, sorry."
            elif mc.is_at_office:
                mc.name "I accidentally left my wallet at home. Can I borrow $5 to grab something from the vending machine?"
                if favour_success:
                    the_person "Oh, sure. I'm sure you're good for it, right?"
                    mc.name "Of course."
                    $ mc.business.change_funds(5)
                    if the_person.obedience < 130:
                        $ the_person.change_obedience(1)
                else:
                    the_person "Aren't you supposed to be paying me? Sorry, I don't carry cash, anyway..."
                    mc.name "Right, sorry."
            else:
                mc.name "Hey, I left my wallet at home. Can you spot me $5 for a coffee?"
                if favour_success:
                    the_person "Oh, sure. I'm sure you're good for it, right?"
                    mc.name "Of course."
                    $ mc.business.change_funds(5)
                    if the_person.obedience < 130:
                        $ the_person.change_obedience(1)
                else:
                    the_person "Sorry, I don't carry cash [the_person.mc_title]."
                    mc.name "Right, sorry."

        "Moderate Favour" if the_person.has_event_delay("obedience_med_favour", TIER_1_TIME_DELAY):
            $ mc.change_energy(-15)
            $ favour_success = True  #calculate this instead of assuming true
            if not mc.phone.has_number(the_person):
                mc.name "I was just wondering if I could get your number."
                if favour_success:
                    the_person "I suppose that would be okay. Just no drunk 3 am phone calls, okay?"
                    mc.name "Of course."
                    "You grab your phone and quickly put her number in as she lists it off for you."
                    $ mc.phone.register_number(the_person)
                    if the_person.obedience < 150:
                        $ the_person.change_obedience(2)
                else:
                    the_person "Yeah right, I don't think we're close enough for something like that."
                    "Ouch."
            else:
                mc.name "You look amazing in that outfit. Can I snap a picture to update your profile on my phone?"
                if favour_success:
                    the_person "Yeah, I can do that!"
                    $ the_person.draw_person(position = "stand3")
                    "You quickly snap a picture of [the_person.possessive_title]."
                    $ the_person.draw_person()
                    if the_person.obedience < 150:
                        $ the_person.change_obedience(2)
                else:
                    the_person "Sorry, I'm not here to play dress up for you."
                    "Ouch."
            $ the_person.set_event_day("obedience_med_favour")
        "Large Favour" if mc.phone.has_number(the_person) and the_person.has_event_delay("obedience_large_favour", TIER_2_TIME_DELAY):
            $ mc.change_energy(-15)
            $ favour_success = True  #calculate this instead of assuming true
            if the_person.is_family:
                if mc.is_home:
                    mc.name "Hey, can I ask for a huge favour?"
                    the_person "Umm, maybe. What do you need?"
                    if time_of_day < 2:
                        mc.name "I really need to get going, could you pack me a lunch? I don't think I have time today."
                    else:
                        mc.name "Can you get the trash and the dishes tonight? I know it's my turn, but I have work stuff I really need to get done."
                    if favour_success:
                        the_person "I... yeah I guess I can do that. Just this once?"
                        mc.name "Of course."

                        if the_person.obedience < 160:
                            $ the_person.change_obedience(3)
                    else:
                        the_person "Nope! The world doesn't revolve around you—find a way to get it done yourself!"
                else:
                    mc.name "Hey, can I ask for a favour?"
                    the_person "Umm, maybe?"
                    mc.name "I accidentally left my wallet at home, but I need to grab some food at the office today."
                    mc.name "Can you front me $20?"
                    if favour_success:
                        the_person "I... yeah I guess I can do that. Try not to make a habit out of this, okay?"
                        mc.name "Of course."
                        $ mc.business.change_funds(20)
                        if the_person.obedience < 160:
                            $ the_person.change_obedience(3)
                    else:
                        the_person "No way! If I give you money I'll never see it again!"
            elif not the_person.mc_knows_address:
                mc.name "Can I get your address? It would be handy to have."
                if favour_success:
                    the_person "I guess. Just no unannounced 3 am booty calls, okay?"
                    mc.name "Of course."
                    $ the_person.learn_home()
                    if the_person.obedience < 160:
                        $ the_person.change_obedience(3)
                else:
                    the_person "Yeah right! That is need to know information only, mister."
                    mc.name "Ah, okay..."
            elif the_person.has_role(instapic_role):
                mc.name "Your InstaPics have been so hot lately. Could you take a few more today? I like to check it when I go to bed."
                if favour_success:
                    the_person "Oh! I'm glad you like them. Yeah I could do that."
                    mc.name "Great! I appreciate it."
                    $ the_person.event_triggers_dict["insta_generate_pic"] = True
                    if the_person.obedience < 160:
                        $ the_person.change_obedience(3)
                else:
                    the_person "Ummm, I just post when I get the chance. Sorry I'm not sure if I'll get around to it today or not."
                    mc.name "Ah, okay."
            else:
                mc.name "You look amazing today. Have you ever thought about starting an InstaPic account?"
                mc.name "You really should. I know I would check it out!"
                if favour_success:
                    the_person "You know, I had been considering doing that. I think you've convinced me, I'll do it later!"
                    mc.name "Great! I can't wait to see you post!"
                    $ the_person.learn_instapic()
                    if the_person.obedience < 160:
                        $ the_person.change_obedience(3)
                else:
                    the_person "Sorry, I'm not really into social media."
                    mc.name "Okay, well if you ever change your mind, you would be great!"
            $ the_person.set_event_day("obedience_large_favour")
        "Nevermind":
            mc.name "Nevermind, it's okay."
            return
    $ the_person.set_event_day("obedience_favour")
    return

label mc_move_to_private_location(the_person):
    $ old_mc_location = None
    if mc.location.person_count < 2:
        return False

    "You look around and see some people watching you, what do you want to do?"
    menu:
        "Go somewhere more private\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
            mc.name "Let's find somewhere a little more private."
            call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_move_to_private_location
            return True
        "Keep going\n{menu_yellow}[mc.location.watcher_info_text]{/menu_yellow}":
            return False

label mc_change_to_private_location(the_person):
    $ old_mc_location = mc.location

    # TODO: Add more appropriate private locations for hubs when needed
    if the_person.is_at_mc_house:
        $ ran_num = renpy.random.randint(0, 3)
        if ran_num == 0 and the_person.is_at(the_person.bedroom) and the_person.bedroom.person_count > 1:
            # bedroom is not private choose other location
            $ ran_num += renpy.random.randint(1, 3)
        if ran_num == 3 and kitchen.person_count > 0:
            # we can't go into the kitchen
            $ ran_num -= renpy.random.randint(1, 2)
        if ran_num == 0:
            $ mc.change_location(the_person.bedroom)
            "You take [the_person.possessive_title] to her bedroom."
        elif ran_num == 1:
            $ mc.change_location(home_shower)
            "You take [the_person.possessive_title] by the hand and lead her into the bathroom."
        elif ran_num == 2:
            $ mc.change_location(laundry_room)
            "You pull [the_person.possessive_title] into the laundry room."
        else:
            $ mc.change_location(kitchen)
            "You take [the_person.possessive_title] by the hand and lead her into the kitchen."
    elif the_person.is_at_job(prostitute_job):
        $ mc.change_location(downtown_hotel_room)
        "[the_person.possessive_title!c] takes you to a motel that rents rooms by the hour."
    elif mc.is_at(the_person.home):
        $ mc.change_location(the_person.bedroom)
        "You take [the_person.possessive_title] to her bedroom."
    elif mc.is_at(downtown_bar):
        $ mc.change_location(downtown_bar_bathroom)
        "You take [the_person.possessive_title] to the bathroom."
    elif mc.is_at(downtown_hotel):
        $ mc.change_location(downtown_hotel_room)
        "You take [the_person.possessive_title] to an empty hotel room."
    elif mc.is_at(hospital):
        $ mc.change_location(hospital_room)
        "You take [the_person.possessive_title] to an empty patient room."
    elif mc.is_at(gaming_cafe):
        $ mc.change_location(gaming_cafe_store_room)
        "You take [the_person.possessive_title] to the storage room."
    elif mc.is_at((mom_office_lobby, mom_offices)):
        $ mc.change_location(office_photocopy_room)
        "You take [the_person.possessive_title] to the photocopy room."
    elif mc.is_at_office:
        $ ran_num = renpy.random.randint(0, 2)
        if ran_num == 0:
            $ mc.change_location(work_bathroom)
            "You pull [the_person.possessive_title] into one of the bathrooms at your office."
        elif ran_num == 1:
            $ mc.change_location(storage_room)
            "You take [the_person.possessive_title]'s hand and lead her to an empty storage room and lock the door behind you."
        else:
            $ mc.change_location(ceo_office)
            "You take [the_person.possessive_title] by the arm and lead her to your office."
    elif mc.is_at(mall_hub):
        if mc.is_at(clothing_store):
            $ mc.change_location(changing_room)
            "You pull [the_person.possessive_title] into the dressing room."
        else:
            $ mc.change_location(mall_bathroom)
            "You take [the_person.possessive_title] to the mall bathroom."
    elif mc.is_at(gym_hub):
        $ mc.change_location(gym_shower)
        "You take [the_person.possessive_title] to the gym's shower area."
    elif mc.is_at(downtown_hub):
        $ mc.change_location(mall_bathroom)
        "You take [the_person.possessive_title] into a public bathroom nearby."
    elif mc.is_at(strip_club_hub):
        $ mc.change_location(strip_club_dressing_room)
        "You take [the_person.possessive_title] into the dressing room."
    elif mc.is_at(sex_shop_hub):
        $ mc.change_location(sex_store_storage)
        "You take [the_person.possessive_title] to the storage room."
    elif mc.is_at(university_hub):
        $ ran_num = renpy.random.randint(0, (3 if kaya.progress.love_step >=3 and (day % 7 in  (5,6) or time_of_day not in (1, 2)) else 2))
        if ran_num == 0:
            $ mc.change_location(university_bathroom)
            "You take [the_person.possessive_title] to one of the university's bathrooms."
        elif ran_num == 1:
            $ mc.change_location(university_study_room)
            "You take [the_person.possessive_title] to one of the university's empty study rooms."
        elif ran_num == 2:
            $ mc.change_location(university_library)
            "You take [the_person.possessive_title] to one an empty part of the university library."
        else: # rare occasions
            $ mc.change_location(university_lab)
            "You take [the_person.possessive_title] to [nora.fname]'s lab at the university that should be deserted by now."
    else:
        "You take [the_person.possessive_title] to a more private spot."
        $ old_mc_location = None
    return

label mc_restore_original_location(the_person):
    if "old_mc_location" in globals() and isinstance(old_mc_location, Room):
        if not old_mc_location.is_private:
            # we are moving to a non private location, she needs to get dressed properly
            if (not the_person.outfit.matches(the_person.current_planned_outfit) or
                    the_person.outfit.has_half_off_clothing):
                $ the_person.call_dialogue("clothing_review")
        if old_mc_location.is_public:
            "Afterwards you and [the_person.possessive_title] go back to the [old_mc_location.formal_name]."
        else:
            "Afterwards you and [the_person.possessive_title] go back to [old_mc_location.formal_name]."

        $ mc.change_location(old_mc_location)
        $ old_mc_location = None
        return True
    elif not the_person.location.is_private:
        if (not the_person.outfit.matches(the_person.current_planned_outfit) or
                the_person.outfit.has_half_off_clothing):
            $ the_person.call_dialogue("clothing_review")
    $ old_mc_location = None
    return False
