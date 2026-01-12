init 3 python:
    def downtown_bar_drink_requirement():
        return mc.is_at(downtown_bar)

    # actions available from entry point action
    downtown_bar_drink_action = Action("Order a drink for... {image=time_advance}", downtown_bar_drink_requirement, "downtown_bar_drink_label", menu_tooltip = "Treat someone with a drink...")

    def downtown_bar_drink_date_transition_check(person: Person):
        skill_dif = (mc.charisma + mc.market_skill + person.drink_level) - (person.charisma + person.market_skill)
        rand_roll = renpy.random.randint(-5, 5)
        return ((skill_dif + rand_roll) > 0)


    def downtown_bar_topless_requirement():
        return downtown_bar_is_open()

    def add_downtown_bar_topless_action():
        downtown_bar.add_unique_on_room_enter_event(
            Action("Topless Bar", downtown_bar_topless_requirement, "downtown_bar_topless_label", priority = 30)
        )

    def downtown_bar_nudity_requirement():
        return downtown_bar_is_open()

    def add_downtown_bar_nudity_action():
        downtown_bar.add_unique_on_room_enter_event(
            Action("Nude Bar", downtown_bar_nudity_requirement, "downtown_bar_nudity_label", priority = 30)
        )

    def downtown_bar_sex_booth_unlock_requirement():
        return downtown_bar_is_open()

    def add_downtown_bar_sex_booth_unlock_action():
        downtown_bar.add_unique_on_room_enter_event(
            Action("Sex Booth at the Bar", downtown_bar_sex_booth_unlock_requirement, "downtown_bar_sex_booth_unlock_label", priority = 30)
        )

label downtown_bar_drink_label():
    $ new_person = make_person()

    if not mc.location.people: # No one is in the bar so we create a person.
        "The [downtown_bar.formal_name] is a desolate place to be..."

        $ new_person.draw_person()
        "Having seated yourself by the counter with no bartender in sight you hear the entry door open up as a woman walks in."

        $ new_person.draw_person(position = "sitting")
        "She seats herself in the lounge area, seemingly puzzled by the lack of attendance at the only bar in town."
        "She sits quietly minding her own business..."

        "Do you wish to introduce yourself, perhaps grace her with a free–of–charge drink?"

    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_at_location(mc.location) + unknown_people_at_location(mc.location) + (new_person, ), "Drink with", "Back")]
        ))

    if not isinstance(_return, Person):
        if new_person.is_stranger: # If the player had no interest in interacting with the character we remove it from the game. Assuming a proper "Back" button gets added during first time introduction we can do more with this.
            "Not seeing any reason to stick around she promptly leaves, never to be seen again."

        python: # release variables
            new_person.remove_person_from_game()
            clear_scene()
            del new_person

        return # Where to go if you hit "Back".
    else:
        $ the_person = _return
        $ del new_person

    # add person to game
    python:
        if not the_person in mc.location.people:
            the_person.generate_home()
            mc.location.add_person(the_person)
        the_person.draw_person()

    if the_person.is_stranger: # First time introduction that does not return to talk_person
        call person_introduction(the_person) from _call_person_introduction_downtown_bar_drink

    mc.name "Would you like a drink?"
    the_person "I don't know, anything you would recommend?"
    mc.name "Would you trust me and let me surprise you?"
    the_person "Very well, surprise me."
    if mc.location.people == 1:
        "You move behind the bar a mix a tequila sunrise."
    else:
        "You move to the bar and order a tequila sunrise from the bartender."
    menu:
        "Add serum to her drink" if mc.inventory.has_serum:
            call give_serum(the_person) from _call_give_serum_downtown_bar_drink
            if _return is None:
                "You reconsider, and don't add a serum to [the_person.title]'s drink."
            else:
                "You pour a dose of serum into [the_person.title]'s drink and swirl it in."

        "Add serum to her drink\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
            pass
        "Leave her drink alone":
            pass

    mc.name "One house special for the lady."
    $ the_person.change_stats(happiness = 5, love = 1)
    $ the_person.increase_drink_level(1)
    the_person "Thank you... hmmm... surprisingly tasty, thank you [the_person.mc_title]."
    "You chat for a while with [the_person.possessive_title]."
    if downtown_bar_drink_date_transition_check(the_person):
        the_person "You know, you are a really interesting person. Do you want to get to know each other a little better?"
        "You consider. Feeding her a few drinks might be an opportunity for some fun later..."
        menu:
            "Have some drinks":
                mc.name "Sure, I don't have anywhere to be."
                the_person "Great!"
                call bar_date_main_label(the_person) from _bar_date_from_bar_drink_trans_01
                return
            "Not tonight":
                mc.name "Not tonight, it is time for me to move on."
                the_person "Alright, maybe another time then."
                "You say goodbye and move on."
    else:
        "Eventually it's time to move on."

    if time_of_day == 4:
        "After a night of drinks you decide to head back home to bed."
        $ mc.change_location(bedroom)

    call advance_time() from downtown_bar_drink_1

    $ clear_scene()
    return

label downtown_bar_topless_label():
    $ new_person = make_person()
    $ new_person.strip_to_tits()
    "You step inside the local bar. The place is busy with several patrons crowded around it."
    $ new_person.draw_person(position = "sitting")
    $ mc.change_locked_clarity(20)
    "You notice a couple guys at the bar next to a woman. She appears to be topless."
    "Your influence with city officials recently allowed you legalize women going topless in public."
    "You hadn't thought much about it at the time, but it makes sense that it is something that would be popular at the local bar."
    python: # release variables
        clear_scene()
        new_person.remove_person_from_game()
        del new_person
    "You step away from the bar itself."
    return

label downtown_bar_nudity_label():
    $ new_person = make_person()
    $ new_person.strip_to_tits()
    $ new_person.strip_to_vagina()
    "You step inside the local bar. The place is busy with several patrons crowded around it."
    $ new_person.draw_person(position = "standing_doggy")
    "The first thing you notice, however, is a shapely ass, bent over a pool table, getting ready to take a shot."
    $ mc.change_locked_clarity(30)
    $ new_person.draw_person(position = new_person.idle_pose)
    "Your eyes linger on the woman after she takes her shot and stands up. You can't help but check her out."
    "Your influence with city officials recently allowed you legalize going completely naked in public."
    "You are glad to see that it has proven to be popular at the local bar."
    python: # release variables
        clear_scene()
        new_person.remove_person_from_game()
        del new_person
    "You walk past the pool table and continue into the bar."
    return

label downtown_bar_sex_booth_unlock_label():
    $ new_person = make_person()
    $ new_person.strip_to_tits()
    "You step inside the local bar. The place is incredibly busy with several patrons crowded around it."
    $ new_person.draw_person(position = "blowjob", display_transform = character_center_flipped(zoom = 0.7))
    "However, what catches your eye is a new set of booths setup along the side wall. They are small, but with curtains that can be pulled across for privacy."
    "In one of them, you notice a women underneath the table, giving a man a blowjob."
    $ mc.change_locked_clarity(40)
    "You notice at the end of the row of booths is a big guy with a security vest on."
    "You step up to the bar, and the bartender comes over."
    mc.name "Hey, what's with the booths?"
    "Bartender" "Yeah, I really need to get some signs made. Those are new."
    "Bartender" "With the city legalizing some public sexual acts, the owner saw a bunch of dollar signs and had those sex booths installed."
    "Bartender" "It's $100 to rent one, people can go in there and do their thing, and the bouncer down at the end makes sure nothing too crazy happens."
    "Bartender" "There's a curtain for some privacy, but with the law being what it is... it isn't required, as you can see."
    "He gestures over to the woman who is enthusiastically engaging in fellatio."
    mc.name "Wow, and people are using them?"
    "Bartender" "Yeah, they're quite popular actually. Turns out giving a man a blowjob here in the bar is often safer than trying to sneak into some back alley."
    "Bartender" "A lot of the girls who are regulars here love it, and they can get an idea of if a guy is worth taking home before they leave."
    "Bartender" "We clean them after each use, but most of that $100 is pure profit. It seems to be bringing in a lot more business also."
    mc.name "That's great. Thanks for the information."
    "You step away from the bar. You glance back at the booth, and watch as the man clearly begins to orgasm into the woman's mouth. She greedily swallows everything."
    $ mc.change_locked_clarity(30)
    $ new_person.draw_person(position = "sitting", display_transform = character_center_flipped(zoom = 0.7))
    "After a few more moments, she pops up from under the table and sits down next to the man."
    python: # release variables
        clear_scene()
        new_person.remove_person_from_game()
        del new_person
    "You turn back toward the bar itself."
    "You can now ask girls you are on dates with at the bar if they would like to spend some time with you in the sex booth!"
    "Due to legal limits, you can only engage in acts of foreplay. For now anyway..."
    $ mc.business.event_triggers_dict["bar_booth_avail"] = True
    return