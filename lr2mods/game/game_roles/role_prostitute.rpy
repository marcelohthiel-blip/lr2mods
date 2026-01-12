label prostitute_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    the_person "Hello honey, what can I do for you?"
    mc.name "I know this is strange, but I saw you walking and I have to say, you look amazing."
    "She laughs and blushes."
    the_person "Really? Aren't you cute."
    $ title = renpy.random.choice(["Diamond", "Pearl", "Angel", "Rose", "Candy", "Scarlett", "Aurora", "Jasmine", "Skye", "Kendra"])
    $ the_person.set_title(title)
    $ the_person.set_possessive_title(title)
    the_person "You can call me [the_person.title], and this is my business card with my number."
    $ mc.phone.register_number(the_person)
    $ the_person.set_event_day("day_met")
    $ the_person.learn_job()
    "You give a quick glance at the card and realise she's a working girl."
    the_person "And what's your name honey?"
    return


label prostitute_label(the_person):
    mc.name "[the_person.title], I'm looking for a friend to spend some time with. Are you available?"

    if not the_person.is_at_work:
        if the_person.arousal_perc < 50:
            the_person "I'm sorry honey, but I'm not working at the moment, come find me later."
            return
        else:
            the_person "I'm not working at the moment, but to be honest, I'm feeling a little worked up. So if you are paying, I'm up for it."
    else:
        the_person "If you're paying I am."

    $ the_person.draw_person(position = "walking_away")
    "She takes you by the hand and you walk down the street together."
    $ the_person.draw_person()
    the_person "Down here we won't be disturbed."

    $ mc.business.change_funds(-200, stat = "Hookers")
    $ the_person.change_obedience(1)

    $ the_person.add_situational_obedience("prostitute", 20, "I'm being paid for this, I should do whatever he wants me to do.")
    call fuck_person(the_person, private = True, start_object = mc.location.get_object_with_name("Alley"), ignore_taboo = True) from _call_fuck_person_23 #She's a prostitute, she doesn't care about normal taboos
    $ the_report = _return

    $ the_person.draw_person()
    $ the_person.clear_situational_obedience("prostitute")
    if the_report.get("girl orgasms", 0) > 1:
        "It seems you gave [the_person.title] one of the better fucks in her life, she is still trembling and catching her breath."
        the_person "Holy shit, that was something, maybe I should be paying you... Whew!"
    elif the_report.get("girl orgasms", 0) > 0:
        "It takes [the_person.title] a few moments to catch her breath."
        the_person "Not bad [the_person.mc_title], I actually had fun."

    call sex_review_trance(the_person) from _call_sex_review_trance_prostitute

    if not the_person.is_wearing_planned_outfit:
        "While you rearrange your clothes, you watch her do the same."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)

    the_person "That was fun, I hope you had a good time [the_person.mc_title]."
    $ the_person.draw_person(position = "walking_away")
    "She gives you a quick peck on the cheek, turns around, and walks away."
    $ clear_scene()
    jump game_loop  # for her the encounter is finished, so end talk.

label prostitute_hire_offer(the_person):
    mc.name "Have you ever thought about a different career?"
    mc.name "My company could really use talented people like you."
    "She laughs and shakes her head."
    the_person "I don't think you really mean that."
    mc.name "I do, and you wouldn't have to be walking the streets just to make ends meet."
    if the_person.opinion(("vaginal sex", "anal sex", "public sex", "giving blowjobs", "skimpy outfits")) > 2 and the_person.sluttiness >= 60:
        # She enjoys fucking people too much to quit.
        the_person "That's sweet of you to say, but I don't just do it for the money."
        the_person "Truth is, I kind of like it. I get paid to get fucked, what's not to like?"
        "She shakes her head in a final refusal."
        the_person "So thanks, but no thanks."

    else:
        the_person "Really? Well... Okay, tell me about it."
        call stranger_hire_result(the_person) from _call_stranger_hire_result_prostitute_hire_offer
        if _return:
            mc.name "Then it's settled. I'll see you at work."
            the_person "I suppose I'm going to need a more professional wardrobe now."
            mc.name "That might surprise you, actually..."
            if the_person.sluttiness > 40:  # when she's slutty, she will keep walking the streets
                $ the_person.change_job(prostitute_job, is_primary = False, job_known = False)
        else:
            mc.name "I'm really sorry [the_person.title], but I just don't think we have any positions available that suit your skills right now."
            the_person "I knew it was too good to be true."
            mc.name "Hey, chin up. If we have an opening to fill you'll be my first thought."
    return
