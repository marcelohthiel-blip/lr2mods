
label train_dealbreaker_kissing_label(the_person):
    $ the_person.draw_person() # make her stand up

    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    mc.name "I've noticed that you won't let me kiss you."
    the_person "Yeah, I'm not into that."
    mc.name "It can't be that bad?"
    the_person "Well, I never found it that arousing."
    if the_person.has_broken_taboo("touching_body"):
        mc.name "But you do like it when I touch you, right?"
        the_person "Yeah, I enjoy that."
        mc.name "Perhaps you could consider me kissing you as touching you with my lips and tongue."
        mc.name "Why don't we give it a try and see if I can change your mind."
    else:
        mc.name "You are so sexy, I could just eat you up."
        mc.name "Just think of kissing as me trying to devour you."
        the_person "I... I don't know. It is kind of hard to imagine..."
        "You wish you had a similar experience to pull a memory from to help convince her."
        mc.name "Come on, let's try."
    the_person "Well, okay, we can try..."

    mc.name "Good, now come closer and wrap your arms around me."
    $ the_person.draw_person(position = "kissing")
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(10)
    "You pull her closer and start moving your hands along her body."
    mc.name "Now, move you face closer to mine and let our lips touch."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "You keep caressing her, making sure she doesn't try to pull back."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "kissing")
    mc.name "See, that ain't so bad is it."
    if mc.foreplay_sex_skill > 7:
        $ the_person.update_opinion_with_score("kissing", 1, add_to_log = True)
        the_person "This was better than I remember, I think I actually liked it."
    elif mc.foreplay_sex_skill > 5:
        $ the_person.update_opinion_with_score("kissing", 0, add_to_log = True)
        the_person "It's not that bad, I might even enjoy it."
    else:
        $ the_person.update_opinion_with_score("kissing", -1, add_to_log = True)
        the_person "It's not as bad as I remember."

    mc.name "Alright, let's explore this further another time."
    the_person "That sound good."
    return True
