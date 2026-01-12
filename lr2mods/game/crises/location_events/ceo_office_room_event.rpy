# Room events for MC working in his office.

label ceo_office_secretary_reminder():
    "You work in your office for a while."
    "After a few hours of quiet, you make a mental note that you should hire a new personal secretary."
    return

label ceo_office_secretary_fetch_event():
    if mc.business.personal_secretary is None:
        if renpy.random.randint(0, 10) > 9: #Don't fire this off EVERY time he sits down to work.
            call ceo_office_secretary_reminder() from _ceo_office_secretary_reminder_01
            return
    $ the_person = mc.business.personal_secretary
    $ the_person.draw_person()
    "As you sit down at your desk, your personal secretary appears in your door."
    if time_of_day == 1:    #Morning
        if the_person.obedience > 130:
            the_person "Good morning sir. Could I get you some coffee this morning?"
        else:
            the_person "Good morning [the_person.mc_title]. Anything I can get you this morning? Coffee maybe?"
        mc.name "That would be great, thank you."
        $ clear_scene()
        "You start your work. You are so in the zone, you don't even hear her walk in and she startles you as she sets the coffee cup on your desk."

    elif time_of_day == 2:    #Afternoon
        if the_person.obedience > 130:
            the_person "Good afternoon sir. Did you need me to order out some lunch for you today?"
        else:
            the_person "Good afternoon [the_person.mc_title]. I'm ordering some lunch, do you want anything?"
        "You quickly give her your order."
        $ clear_scene()
        "You start your work. You are so in the zone, you don't even hear her walk in and she startles you as she sets lunch down on your desk."

    elif time_of_day == 3:    #Evening
        if the_person.obedience > 130:
            the_person "Good afternoon sir. Did you want me to print out your post daily reports for you today?"
        else:
            the_person "Good afternoon [the_person.mc_title]. I see you are working hard, want me to print out your daily reports before I leave for the day?"

        $ clear_scene()
        "You are working hard, trying to finish up for the day. You are so in the zone, you don't even hear her walk in and she startles you as she sets the reports down on your desk."

    $ the_person.draw_person(position = "kneeling1")
    the_person "Here you are sir."
    if the_person.tits_visible:
        if the_person.has_large_tits:
            "She is leaning forward over your desk, and her big, exposed tits swing below her enticingly."
        else:
            "She is leaning forward over your desk, and perky, exposed tits are centre of your field of view."
        $ mc.change_locked_clarity(25)
    elif the_person.outfit.is_bra_visible:
        if the_person.has_large_tits:
            "She is leaning forward over your desk, and her big, bra clad tits swing below her enticingly."
        else:
            "She is leaning forward over your desk, and perky, tits are centre of your field of view."
        $ mc.change_locked_clarity(20)
    else:
        "She is leaning forward over your desk, with her chest mere inches from your face."
        $ mc.change_locked_clarity(15)
    $ the_person.draw_person(position = "walking_away")
    "You say thanks and she turns and leaves your office."
    $ clear_scene()
    return

label ceo_office_resupply_event():
    if mc.business.personal_secretary is None:
        if renpy.random.randint(0, 10) > 9: #Don't fire this off EVERY time he sits down to work.
            call ceo_office_secretary_reminder from _ceo_office_secretary_reminder_02
            return
    $ the_person = mc.business.personal_secretary
    $ resupply_obj_name = get_random_from_list["pens", "printer paper", "post it notes", "highlighters", "paperclips", "envelopes"]
    "You are just sitting down at your desk when [the_person.possessive_title] appears at your desk."
    $ the_person.draw_person()
    the_person "Hello sir. I noticed earlier when I was cleaning in here that you were running low on [resupply_obj_name], I got some more from the supply room."
    "You open up a drawer on the side of your desk."
    mc.name "Thanks, they go in here."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.vagina_visible:
        "As she bends over, her bare ass comes in to view."
        $ mc.change_locked_clarity(25)
    elif the_person.outfit.are_panties_visible:
        "As she bends over, her panties are exposed to your view."
        $ mc.change_locked_clarity(20)
    else:
        "As she bends over, her ass is mere inches away."
        $ mc.change_locked_clarity(15)
    if the_person.effective_sluttiness() < 20:
        "You restrain yourself from groping or spanking her backside... for now..."
    elif the_person.effective_sluttiness() < 40:
        "You reach over and give [the_person.title]'s ass a playful swat."
        the_person "Oh! Sorry I didn't realise how I was standing..."
        $ the_person.change_arousal(5)
        $ the_person.change_obedience(2)
    elif the_person.effective_sluttiness() < 60:
        "You reach over and give [the_person.title]'s ass a firm spank."
        the_person "Oh! Thank you sir!"
        $ the_person.change_arousal(10)
        $ the_person.change_obedience(2)
    else:
        "You reach over and spank [the_person.title]'s ass, then leave your hand there for several seconds, squeezing her butt."
        the_person "Ahhh... thank you sir!"
        $ the_person.change_arousal(15)
        $ the_person.change_obedience(2)
    $ the_person.draw_person(position = "walking_away")
    "She stands up then clears out of your office, leaving you to your work."
    $ clear_scene()
    return
