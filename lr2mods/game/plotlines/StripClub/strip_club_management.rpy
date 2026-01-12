## Stripclub storyline Mod by Corrado
# You have some strippers but the business could improve.
init 3 python:
    def strip_club_manager_bdsm_room_build_requirement():
        if not mc.business.has_funds(10000):
            return False
        if bdsm_room_available():
            return False
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        return not strip_club_get_manager() is None

    # extend the default build phone menu function with renovations
    def build_phone_menu_build_bdsm_room_extended(org_func):
        def phone_menu_wrapper():
            # run original function
            phone_menu = org_func()
            if mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", -1) == 0: # only show option when we haven't started construction
                strip_club_manager_bdsm_room_build_action = Action("Build a BDSM room\n{menu_red}Costs: $10,000{/menu_red}", strip_club_manager_bdsm_room_build_requirement, "strip_club_manager_bdsm_room_build_label")
                phone_menu[2].insert(1, strip_club_manager_bdsm_room_build_action)

            return phone_menu

        return phone_menu_wrapper

    build_phone_menu = build_phone_menu_build_bdsm_room_extended(build_phone_menu)


init 3 python:

    def strip_club_manager_reminder_requirement():
        # the event start to trigger after 7 days MC bought the club.
        if day % 5 == 0 and time_of_day == 2 and day >= (get_strip_club_foreclosed_last_action_day() + 7):
            return mc.owns_strip_club and strip_club_get_manager() is None
        return False

    def add_strip_club_manager_reminder_action():
        if strip_club_get_manager() is None:
            mc.business.add_mandatory_crisis(
                Action("A simple reminder to appoint someone as strip club manager", strip_club_manager_reminder_requirement, "strip_club_manager_reminder_label")
            )

    def strip_club_manager_hire_more_stripper_reminder_requirement():
        if day % 5 == 0 and time_of_day == 2 and builtins.len(mc.business.stripclub_strippers) < 7:
            return not strip_club_get_manager() is None
        return False

    def add_strip_club_manager_hire_more_stripper_reminder_action():
        if builtins.len(mc.business.stripclub_strippers) < 7:
            mc.business.add_mandatory_crisis(
                Action("A simple reminder from the strip club manager to hire more stripper", strip_club_manager_hire_more_stripper_reminder_requirement, "strip_club_manager_hire_more_stripper_reminder_label")
            )

    def strip_club_manager_waitresses_suggestion_requirement():
        if day % 5 == 2 and time_of_day == 2 and builtins.len(mc.business.stripclub_waitresses) < 1:
            return not strip_club_get_manager() is None
        return False

    def add_strip_club_manager_waitresses_suggestion_action():
        if builtins.len(mc.business.stripclub_waitresses) < 1:
            mc.business.add_mandatory_crisis(
                Action("Your strip club manager suggests you hire a couple of waitresses.", strip_club_manager_waitresses_suggestion_requirement, "strip_club_manager_waitresses_suggestion_label")
            )

    def strip_club_manager_hire_more_waitresses_reminder_requirement():
        if day % 5 == 4 and time_of_day == 2 and builtins.len(mc.business.stripclub_waitresses) < 4:
            return not strip_club_get_manager() is None
        return False

    def add_strip_club_manager_hire_more_waitresses_reminder_action():
        if builtins.len(mc.business.stripclub_waitresses) < 4: # the event only trigger if there's not the max nr. of waitresses (4)
            mc.business.add_mandatory_crisis(
                Action("A simple reminder from the strip club manager to hire more waitresses", strip_club_manager_hire_more_waitresses_reminder_requirement, "strip_club_manager_hire_more_waitresses_reminder_label")
            )

    def strip_club_manager_bdsm_room_suggestion_requirement():
        if not bdsm_room_available():
            if day >= (get_strip_club_foreclosed_last_action_day() + 15): # the event trigger after 15 days you have a manager
                if not mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", None): # Not suggested yet
                    if builtins.len(mc.business.stripclub_waitresses) > 0 and not strip_club_get_manager() is None:
                        if time_of_day == 3 and not mc.is_at(strip_club_hub):
                            return True
        return False

    def add_strip_club_manager_bdsm_room_suggestion_action():
        if not bdsm_room_available():
            mc.business.add_mandatory_crisis(
                Action("Your strip club manager suggests you build a new BDSM room.", strip_club_manager_bdsm_room_suggestion_requirement, "strip_club_manager_bdsm_room_suggestion_label")
            )

    def strip_club_manager_bdsm_room_reminder_requirement():
        if not bdsm_room_available() and day % 5 == 3 and time_of_day == 2 and mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", -1) == 0:
            return not strip_club_get_manager() is None
        return False

    def add_strip_club_manager_bdsm_room_reminder_action():
        if not bdsm_room_available():
            mc.business.add_mandatory_crisis(
                Action("A simple reminder from the strip club manager to build a BDSM room.", strip_club_manager_bdsm_room_reminder_requirement, "strip_club_manager_bdsm_room_reminder_label")
            )


    def strip_club_manager_bdsm_room_built_requirement():
        if day >= (mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", -1) + 5):
            return mc.business.is_open_for_business
        return False

    def add_strip_club_manager_bdsm_room_built_event():
        mc.business.add_mandatory_crisis(
            Action("Your new BDSM room has been built.", strip_club_manager_bdsm_room_built_requirement, "strip_club_manager_bdsm_room_built_label")
        )

    def strip_club_offer_drink_requirement():
        return mc.location.person_count > 0

    strip_club_offer_drink_action = Action("Offer a drink to ...", strip_club_offer_drink_requirement, "strip_club_offer_drink_label", menu_tooltip = "Offer a drink to the customer / employee.", priority = 10)

label strip_club_set_uniforms_label():
    call screen stripclub_uniform_manager()
    if _return == "Add":
        call outfit_master_manager() from _call_outfit_master_manager_strip_club_set_uniforms
        if isinstance(_return, Outfit):
            $ mc.business.stripclub_uniforms.append(StripClubOutfit(_return))
        jump strip_club_set_uniforms_label
    return

label strip_club_manager_reminder_label():
    "A few days have passed since you bought the strip club, and after running the numbers, you realise that business could be better."
    "But you can't spend all your time there micro-managing everything, you need to find someone to do it for you."
    "Someone obedient to you, but also strong enough to manage the other girls, the customers and the suppliers... Perhaps one of the strippers?"
    "Even better, why not get [aunt.possessive_title] to do it, it might be worth it to have mother and daughter working side by side."
    return

label strip_club_manager_hire_more_stripper_reminder_label(): # phone call
    if builtins.len(mc.business.stripclub_strippers) >= 7:
        return
    $ the_person = strip_club_get_manager()
    if the_person is None:
        return # somehow we no longer have a manager
    if mc.is_at(strip_club_hub) and the_person.is_at(strip_club_hub):
        $ the_person.draw_person()
    else:
        "Suddenly your phone rings, it's your strip club manager."
    the_person "Hello [the_person.mc_title], I just wanted to remind you that we can have seven girls here, performing on the stage."
    the_person "A full roster would make setting up the shifts easier and, of course, it would be more profitable for you."
    mc.name "Thank you [the_person.title]... I know, I'll find someone, I promise!"
    the_person "Okay [the_person.mc_title], thank you!"
    $ clear_scene()
    return

label strip_club_manager_hire_more_waitresses_reminder_label(): # phone call
    if builtins.len(mc.business.stripclub_waitresses) >= 4:
        return
    $ the_person = strip_club_get_manager()
    if the_person is None:
        return # somehow we no longer have a manager
    if mc.is_at(strip_club_hub) and the_person.is_at(strip_club_hub):
        $ the_person.draw_person()
    else:
        "Your phone rings. It's your strip club manager."
    the_person "Hello [the_person.mc_title], I just wanted to remind you that we need more waitresses, we can't have our strippers do that."
    mc.name "Thank you [the_person.title]... I know, I'll find someone, I promise!"
    the_person "Okay [the_person.mc_title], thank you!"
    $ clear_scene()
    return

label strip_club_manager_waitresses_suggestion_label(): # (personal contact)
    $ the_person = strip_club_get_manager()
    if the_person is None:
        return # somehow we no longer have a manager
    if not mc.is_at(strip_club_hub):
        "Your smartphone rings. It's your strip club manager."
        the_person "Hi [the_person.mc_title]! Can you join me here at the Club ? I need to talk with you."
        mc.name "Sure [the_person.title], I'm coming."
        $ mc.change_location(strip_club)

    $ the_person.draw_person(emotion = "happy", position = "stand3")
    mc.name "Here I am [the_person.title], how are things going here?"
    the_person "That's exactly what I wanna talk to you about: you spent a lot of money to buy this place, don't you wanna make it more profitable?"
    mc.name "Of course I do: what do you have in mind?"
    the_person "A lot of customers here get a drink at the bar, then sit by the stage to watch the girls stripping, right?"
    mc.name "Yes, that's how the business here works."
    the_person "Exactly! After they get their drink, most customers don't want to leave the stage. Only a few come back to the bar to get another drink."
    mc.name "I think I get where you're going with this..."
    the_person "Yeah! What if we had a couple of waitresses serving the drinks directly at the customer's seat, and maybe some peanuts or some chips..."
    the_person "With the salty snacks keeping them thirsty and the waitresses letting them stay in their seats, we'd sell a lot more drinks by the end of the day."
    mc.name "Thank you [the_person.title], that's really a good idea! I'll look into hiring some waitresses as soon as possible."
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    "[the_person.title] smiles back to you, proud to have proven herself worthy."
    $ add_strip_club_manager_hire_more_waitresses_reminder_action()
    return

label strip_club_manager_bdsm_room_suggestion_label(): # (personal contact)
    $ the_person = strip_club_get_manager()
    if the_person is None:
        return # somehow we no longer have a manager
    if not mc.is_at(strip_club_hub):
        "Your smartphone rings. It's your strip club manager."
        the_person "Hi [the_person.mc_title]! Can you join me here at the club? I need to talk with you."
        mc.name "Sure [the_person.title], I'll be right over."
        $ mc.change_location(strip_club)

    $ the_person.draw_person(emotion = "happy", position = "stand3")
    mc.name "Okay, here I am [the_person.title], what's up?"
    the_person "I have an idea to make the business here more profitable."
    mc.name "You have my attention, what do you have in mind?"
    the_person "This place has a lot of unused space around the back... What if we make another room there for a different kind of show?"
    mc.name "'Different show? You know that this is a strip club, right? Not a brothel?"
    the_person "No no no, [the_person.mc_title], nothing like that! I did some research, and I found that in other cities you can find places that offer BDSM shows."
    the_person "But here, in our city, there's nothing like it... yet!"
    mc.name "What do you mean by 'BDSM shows'?"
    the_person "Well, you know there are girls who like to submit themselves completely to their partners during sex, right?"
    "Your mind wanders off for a bit, of course you know, you know very well!"
    the_person "And you know that almost every girl, more or less, likes to show herself off, right?"
    "You don't even try to hide your smile, you know that too..."
    the_person "So, in a BDSM show girls submit themselves completely to their partners in a public place like this, showing off their obedience and devotion to their Master."
    mc.name "But you know [the_person.title], we can't have guys on the stage, fucking around with girls... we would get into some serious trouble!"
    the_person "Whoever said anything about men performing on stage?"
    "She winks mischievously at you, now it's clear what kind of picture is floating in her vicious mind..."
    mc.name "I get the picture. I admit it could be a very good idea, but I need to double-check with my lawyer to see if it is feasible."
    the_person "I made a business prospect for you with costs and revenues, I will send it to your phone."
    mc.name "Thank you, [the_person.title], I'll look at it."
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    "As you glance over the documents, you quickly realise that the $10,000 investment could be very, very profitable."

    $ add_strip_club_manager_bdsm_room_reminder_action()
    $ mc.business.event_triggers_dict["strip_club_bdsm_decision_day"] = 0
    return

label strip_club_manager_bdsm_room_build_label(): # (action button)
    "You pick up the phone and call your usual contractor."
    mc.name "Hello, this is [mc.name] [mc.last_name] from [strip_club.formal_name], I need some construction work done here at my club."
    "You go over the details and agree on a price of $10,000 for converting some unused space into a fully equipped and soundproofed BDSM room."
    $ mc.business.change_funds(-10000, stat = "Renovations")
    $ add_strip_club_manager_bdsm_room_built_event()
    $ mc.business.event_triggers_dict["strip_club_bdsm_decision_day"] = day
    return

label strip_club_manager_bdsm_room_reminder_label(): # phone call
    $ the_person = strip_club_get_manager()
    if the_person is None:
        return # somehow we no longer have a manager
    if mc.is_at(strip_club_hub):
        $ the_person.draw_person()
    else:
        "Your phone rings, it's your strip club manager."
    the_person "Hello [the_person.mc_title], did you check the business prospect I sent you for having a special room for BDSM shows?"
    the_person "I'm sure it would make the business here a lot more profitable, we would be the only club in the city having that kind of entertainment."
    mc.name "Thank you [the_person.title]... I know, I'll get back to you, I promise!"
    the_person "Ok [the_person.mc_title], thank you!"
    $ clear_scene()
    return

label strip_club_manager_bdsm_room_built_label(): # (time event)
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The BDSM room at the strip club is now ready for use."
    $ strip_club.add_action(strip_club_offer_drink_action)
    $ bdsm_room.add_action(strip_club_offer_drink_action)
    $ add_strip_club_cage_her_action_to_mc_actions()
    $ bdsm_room.visible = True
    $ mc.business.event_triggers_dict["strip_club_has_bdsm_room"] = True
    return

label strip_club_offer_drink_label():
    call screen main_choice_display(
        build_menu_items(
            [
                get_sorted_people_list(
                    [x for x in known_people_at_location(mc.location) + unknown_people_at_location(mc.location)
                        if not x.has_role(caged_role) and x.has_event_delay("free_club_drink_day", 0)],
                    "Offer drink to",
                    "Back")
            ]
        ))

    if not isinstance(_return, Person):
        return
    else:
        $ the_person = _return

    $ the_person.draw_person()

    if the_person.is_stranger: # First time introduction that does not return to talk_person
        call person_introduction(the_person) from _call_person_introduction_strip_club_offer_drink

    mc.name "Can I offer you a drink? It's on the house."
    the_person "That's very kind, what can you recommend?"
    mc.name "Why don't you let me surprise you?"
    the_person "That sounds wonderful, [the_person.mc_title], please do."
    mc.name "Just a minute, [the_person.title], I will be right back."

    if mc.inventory.has_serum:
        "This gives you an opportunity to spike her drink with a serum."
        call give_serum(the_person) from _call_give_serum_strip_club_offer_drink

    mc.name "One house special for the lady."
    $ the_person.draw_person(emotion = "happy")
    $ the_person.set_event_day("free_club_drink_day")
    the_person "Hmm, very nice, thank you, [the_person.mc_title]."
    return
