label ophelia_takes_over_hair_salon_label():
    python:
        # make her free-roam and start working the salon
        salon_manager.set_override_schedule(None)
    return

label salon_manager_greetings(the_person):
    $ the_person.draw_person(emotion = "happy")

    if not the_person.has_event_day("day_met"):
        "You enter the hair salon. A beautiful young woman walks up to you and introduces herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        the_person "Hello there sir! Welcome to the Sweet Pixie Salon!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.is_stranger:
            mc.name "Hey, there."
            $ the_person.set_title()
            $ the_person.set_possessive_title()
            $ the_person.primary_job.job_known = True
            the_person "I am [the_person.title], top stylist and owner."
            "She holds her hand out to shake yours."
            the_person "And how may I call you?"
            $ title_choice = build_salon_manger_title_choice_menu(the_person)
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)

        the_person "I've just taken over the salon, so what can I do for you today? A wash or a trim? A shave perhaps?"
        mc.name "Nothing like that today, I own a company downtown."
        mc.name "My employees need to look perfect and I want to pay for their expenses, is that possible?"
        the_person "No problem, just give me your credit card details and I will charge it whenever you send someone by."
        "You smile at [the_person.fname] and hand over your company credit card."
        the_person "Perfect! All done."
        $ add_ophelia_gets_dumped_action()
    else:
        if the_person.love < 0:
            the_person "Hi, what can I do for you?"
        elif the_person.happiness < 90:
            the_person "Hey. I hope you're having a better day than I am."
        else:
            the_person "Hey there, [the_person.mc_title]! It's good to see you!"
            if the_person.sluttiness > 60:
                "[the_person.possessive_title!c] smiles playfully."
                the_person "I was just thinking about you. Anything I can do for you today?"
            else:
                the_person "Is there anything I can help you with?"

    $ clear_scene()
    return
