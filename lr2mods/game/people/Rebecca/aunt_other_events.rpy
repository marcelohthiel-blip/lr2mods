
label aunt_working_at_stripclub_label():
    if not mc.is_at(strip_club):
        $ mc.start_text_convo(cousin)
        cousin "Hey [cousin.mc_title], I need you at the club, right now!!"
        mc.name "Okay, relax, I'm on my way."
        $ mc.end_text_convo()
        "It sounded serious, so you make your way down to club."
        $ mc.change_location(strip_club)

    "As soon as you walk into the club, your cousin pulls you aside into one of the bar areas."

    $ scene_manager = Scene()
    $ scene_manager.add_actor(cousin)

    cousin "Finally, you're here!"
    cousin "We have a problem, my mother came in a while ago and asked for the dressing rooms."
    cousin "You haven't told her anything, right?! She's gonna kill me, if she finds me here!"

    mc.name "For fuck sake, calm down. I've hired her as a [aunt.current_job.job_title!l]."
    cousin "You did what?! You fucking asshole! I'm gonna kill you!"
    mc.name "Jesus, [cousin.name], for fuck sake, calm down?"
    cousin "What?"
    mc.name "Think of the positive side here."
    cousin "Huh? I don't get it..."
    mc.name "Simple, she's working here now, so she can't be mad at you for working here too."
    cousin "Right..."
    if cousin.event_triggers_dict.get("blackmail_level", -1) != -1:
        mc.name "Secondly, I don't have anything left to blackmail you with."
        cousin "Yeah, that's right."
    mc.name "Now let me go talk with her and sort this out for you, okay?"
    cousin "Alright, but if you get me in trouble, I'll swear..."
    mc.name "Now shut up, [cousin.name]. And let me go talk with her."
    cousin "Okay..."

    $ scene_manager.hide_actor(cousin)
    "You leave the bar area and make your way to the dressing rooms."

    $ mc.change_location(strip_club_dressing_room)
    $ scene_manager.add_actor(aunt, position = "sitting", emotion = "happy", display_transform = character_center)

    mc.name "Hey [aunt.title], how are you? Getting settled in for your first shift?"
    aunt "Hi [aunt.mc_title], yes, I'm a little excited, I hope they won't mind an older lady running around here."
    mc.name "Don't worry, you'll fit right in, I promise."

    mc.name "There is something I haven't told you yet."
    aunt "I knew it, you want me to get naughty with the customers."
    mc.name "No, that's not it, that's totally up to you."
    aunt "Oh, right, what is it then?"
    mc.name "Remember when you asked me to find out what's going on with [cousin.fname] and where she goes at night?"
    aunt "Right, yeah, I remember."
    mc.name "Well, I have some news for you."
    aunt "What?"
    mc.name "She's working for me now..."
    aunt "Oh, what a nice thing for you to do for her!"
    mc.name "... as a [cousin.secondary_job.job_title!l]."
    aunt "I'm sorry, you hired her as a what?!"

    if cousin.event_triggers_dict.get("blackmail_level", -1) > 0:
        "You figure it would be better to hide the fact that you have been blackmailing her daughter for a while..."
    else:
        "You figure it would be better not to let her know you knew about her daughter for a while..."

    mc.name "Hold on, let me explain. She was already stripping here when the old place went under; I just didn't tell her to stop is all."
    mc.name "Besides, isn't it better that she's working for me, instead of someone less professional?"
    mc.name "Plus, with you working side by side, you can be certain that she's safe and not being exploited - it's a win-win-win!"

    "She mulls this bombshell over."
    aunt "I hate to admit it, but you do have a point."

    mc.name "Relax [aunt.title]! She's happy working here, and she could work anywhere else if she wanted but I bet no one else in the city pays as well as I do."
    mc.name "Besides, you're not exactly in a position to throw stones, are you?"

    aunt "What do you mean?"

    mc.name "You work here too, [aunt.title]. Like mother, like daughter - right?"

    "She stares at you for while, trying to come to term with the idea..."

    mc.name "Tell you what, I'll have her come meet you back here and you two can hash it out."
    aunt "Alright, but this still doesn't mean I'm thrilled about it."
    aunt "I guess I do appreciate you looking out for us, even if it's a little unconventional."

    "You walk out and call in [cousin.possessive_title], so she can talk with her mother."

    $ scene_manager.show_actor(cousin)

    "She gives you a wary look as she walks in, but you just smile and look towards her mom."

    cousin "Hey, mom... how are you?"
    aunt "Hi [cousin.fname], come sit with me."

    $ scene_manager.update_actor(cousin, position = "sitting")

    aunt "At first I was really upset when [mc.name] told me you we working here..."

    $ scene_manager.clear_scene()
    $ cousin.event_triggers_dict["blackmail_level"] = -1  # disable blackmail cousin
    $ aunt.event_triggers_dict["knows_about_stripping"] = True
    $ add_aunt_working_at_stripclub_follow_up()

    "This is your cue to leave the girls to talk among themselves and go home."
    $ mc.change_location(bedroom)   # just move to bedroom to prevent any strange dialogues
    return

label aunt_or_cousin_promotion_label(the_person):

    $ the_person.draw_person()

    mc.name "Hello [the_person.title], do you enjoy working together with your daughter?"
    the_person "Well, it was a little awkward at first, but now I really like it."
    mc.name "I'm happy to hear that."
    mc.name "This place is doing great, but I think it would be better if someone else manages the daily operations."

    $ the_person.draw_person(emotion = "happy")
    the_person "Oh, that is a great idea, where you thinking about someone specific?"

    "She puts on an endearing smile, figuring that you would promote her to run the club for you."

    menu:
        "Promote [the_person.fname]":
            mc.name "I can't think of anyone more capable and qualified as you, [the_person.title]."
            the_person "I understand [the_person.mc_title], I can assure you I will do my best..."
            mc.name "That's all I need, [the_person.title], I will let you run the place. Prove to me that I made the right choice."
            "She looks intensely into your eyes. You see in her eyes the glimmer of excitement."
            the_person "I will. Let me go and get changed."
            python:
                the_person.change_stats(happiness = 10, obedience = 3)
                the_person.set_event_day("stripclub_last_promotion_day")
                promote_strip_club_stripper_to_manager(the_person)
                the_person.apply_planned_outfit()

        "Promote [cousin.fname]" if cousin.is_strip_club_employee:
            mc.name "I can't think of anyone better than [cousin.fname], she knows this place and the girls like the back of her hand."
            $ the_person.draw_person(emotion = "sad")
            mc.name "But since you're her mother, I thought I would talk to you about it first."
            the_person "Right, yes, of course, I'm happy that you will give her chance to become more than just a [cousin.current_job.job_title!l]."
            mc.name "Great, I'm happy that you agree, I will let her know right away."
            $ clear_scene()
            $ the_person.change_stats(happiness = -10, obedience = -3, love = -5)
            "As you leave your disappointed aunt, you walk over to your cousin to give her the news."
            $ cousin.draw_person()
            "Hey [cousin.title], can we have a little talk?"
            cousin "Sure, why not?"
            mc.name "I've decided to promote you to manager."
            cousin "What?! No way! You are fucking kidding me right?"
            mc.name "Nope, I've talked it over with your mom and she agrees that you are the best person for the job."
            cousin "Fuck me! I don't know what to say..."
            mc.name "Just say yes."
            cousin "Yes!!"
            $ cousin.draw_person(emotion = "happy")
            $ cousin.change_stats(happiness = 10, obedience = 5, love = 5)
            mc.name "Good, from now on you will be in charge of the daily operations. Prove to me that I made the right choice."
            cousin "I will make you proud, let me go and get changed."

            python:
                cousin.set_event_day("stripclub_last_promotion_day")
                promote_strip_club_stripper_to_manager(cousin)
                cousin.apply_planned_outfit()

        "Think it over":
            mc.name "I haven't found anyone yet, but I will let you know if I do."
            $ the_person.draw_person(emotion = "sad")
            "[the_person.possessive_title!c] is not happy, she was sure it would be her."
            mc.name "Thanks for listening and agreeing with me."

    $ clear_scene()
    return
