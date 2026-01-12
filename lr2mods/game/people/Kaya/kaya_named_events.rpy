#Named events are for unique character specific overrides to generic labels.

label kaya_bc_talk_label():
    $ the_person = kaya
    if the_person.event_triggers_dict.get("no_condom_talk", False):
        the_person "Oh... did you forget?"
        the_person "I'm not on birth control, and I'm never going to be."
        the_person "It is against my culture, please don't ask me to go on it!"
        mc.name "I'm not, I had just forgotten."
        $ the_person.update_birth_control_knowledge()
    else:
        the_person "Oh umm, I'm sorry I don't really feel comfortable talking about that right now..."
        "She grimaces for a moment. You wonder what that means."
    return

label kaya_lunch_date_plan_label():
    $ the_person = kaya
    mc.name "I was wondering if you would want to get some lunch out sometime."
    if kaya.progress.love_step == 0:
        the_person "Sorry, I can't!"
        call kaya_ask_out_reject_label(the_person) from _kaya_first_date_turn_down_01_lunch
        return
    if kaya.progress.love_step == 1:
        the_person "I'm sorry... I told you I have finals this week. I really want to do something though!"
        the_person "Come back next week!"
        return
    if the_person.love < 40:
        the_person "Oh! I'm pretty busy, but I guess I could try and work that out."
        the_person "You seem nice enough... but I can't do it on the weekends."
        the_person "I work a short shift and they don't give me a lunch break at the coffee shop."
        
    else:
        the_person "Sounds great!"
        the_person "You know the deal though, no lunch breaks at the coffee shop, so it'll have to be a weekday."
    mc.name "Okay, let me see if I have a day available for that..."
    call date_schedule_selection(the_person, 2, day_restriction = [0,1,2,3,4]) from _date_schedule_afternoon_lunch_with_kaya_01
    if _return:
        $ create_lunch_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_lunch_date_text_plan_label():
    $ the_person = kaya
    if kaya.progress.love_step == 0:
        "You start to text her to ask her out for lunch, but it feels awkward via text."
        "Maybe you should try talking to her about it in person intead."
        return
    if kaya.progress.love_step == 1:
        "You start to text her about a lunch date, but remember she said she had finals this week."
        return
    mc.name "Would you like to go get a coffee, maybe a little lunch, and just chat for a while? I feel like I want to get to know you better."
    if the_person.love < 40:
        the_person "Oh! I'm pretty busy, but I guess I could try and work that out."
        the_person "You seem nice enough... but I can't do it on the weekends."
        the_person "I work a short shift and they don't give me a lunch break at the coffee shop."
    else:
        the_person "Sounds great!"
        the_person "You know the deal though, no lunch breaks at the coffee shop, so it'll have to be a weekday."
    mc.name "Okay, let me see if I have a day available for that..."
    call date_schedule_selection(the_person, 2, day_restriction = [0,1,2,3,4]) from _date_schedule_afternoon_lunch_with_kaya_02
    if _return:
        $ create_lunch_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_movie_date_plan_label():
    $ the_person = kaya
    mc.name "I was wondering if you would want to go out for a movie this week."
    if kaya.progress.love_step == 0:
        the_person "Sorry, I can't!"
        call kaya_ask_out_reject_label(the_person) from _kaya_first_date_turn_down_01_movies
        return
    if kaya.progress.love_step == 1:
        the_person "I'm sorry... I told you I have finals this week. I really want to do something though!"
        the_person "Come back next week!"
        return

    mc.name "It would give us a chance to spend some time together and get to know each other better."
    the_person "That could be fun I guess... when were you thinking?"
    

    call date_schedule_selection(the_person, 3) from _date_schedule_evening_movie_in_person_with_kaya_01
    if _return:
        $ create_movie_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_movie_date_text_plan_label():
    $ the_person = kaya
    if kaya.progress.love_step == 0:
        "You start to text her to ask her out to a movie, but it feels awkward via text."
        "Maybe you should try talking to her about it in person intead."
        return
    if kaya.progress.love_step == 1:
        "You start to text her about a movie date, but remember she said she had finals this week."
        return

    mc.name "So [the_person.title], I was wondering if you'd like to come see a movie with me some time this week."
    mc.name "It would give us a chance to spend some time together and get to know each other better."
    the_person "Oh, a movie sounds fun! Let's do it!"

    call date_schedule_selection(the_person, 3) from _date_schedule_evening_movie_in_person_with_kaya_02
    if _return:
        $ create_movie_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_dinner_date_plan_label():
    $ the_person = kaya
    mc.name "I was wondering if you would want to go out for dinner this week."
    if kaya.progress.love_step == 0:
        the_person "Sorry, I can't!"
        call kaya_ask_out_reject_label(the_person) from _kaya_first_date_turn_down_01_dinner
        return
    if kaya.progress.love_step == 1:
        the_person "I'm sorry... I told you I have finals this week. I really want to do something though!"
        the_person "Come back next week!"
        return

    mc.name "I'd really like to treat such a hard working young woman to a nice night out."
    the_person "Aww, you're so sweet. When were you thinking?"

    call date_schedule_selection(the_person, 3) from _date_schedule_evening_dinner_in_person_with_kaya_01
    if _return:
        $ create_dinner_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_dinner_date_text_plan_label():
    $ the_person = kaya
    if kaya.progress.love_step == 0:
        "You start to text her to ask her out to a movie, but it feels awkward via text."
        "Maybe you should try talking to her about it in person intead."
        return
    if kaya.progress.love_step == 1:
        "You start to text her about a movie date, but remember she said she had finals this week."
        return
    mc.name "I was wondering if you would want to go out for dinner soon."
    mc.name "I'd really like to treat such a hard working young woman to a nice night out."
    the_person "Aww, you're so sweet. When were you thinking?"

    call date_schedule_selection(the_person, 3) from _date_schedule_evening_dinner_in_person_with_kaya_02
    if _return:
        $ create_dinner_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_bar_date_plan_label():
    $ the_person = kaya
    mc.name "I was wondering if you would want to go out for a few drinks some night soon."
    if kaya.progress.love_step == 0:
        the_person "Sorry, I can't!"
        call kaya_ask_out_reject_label(the_person) from _kaya_first_date_turn_down_01_drinks
        return
    if kaya.progress.love_step == 1:
        the_person "I'm sorry... I told you I have finals this week. I really want to do something though!"
        the_person "Come back next week!"
        return
    if kaya.progress.lust_step < 2:
        the_person "Oh, I appreciate the thought, but maybe we could do something else instead?"
        the_person "Being under 21 in a bar can be kind of weird sometimes."
        return
    the_person "Oh! I'm always up for a little liquid refreshment. When were you thinking?"
    call date_schedule_selection(the_person, 4) from _date_schedule_night_bar_in_person_with_kaya_01
    if _return:
        $ create_bar_date_action(the_person, _return)
        "You give her the location of the bar downtown, and you agree to meet there at the specified time."
        the_person "Sounds great! They have a pool table, right?"
        mc.name "Of course."
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label kaya_bar_date_text_plan_label():
    $ the_person = kaya
    if kaya.progress.love_step == 0:
        "You start to text her to ask her out to a movie, but it feels awkward via text."
        "Maybe you should try talking to her about it in person intead."
        return
    if kaya.progress.love_step == 1:
        "You start to text her about a movie date, but remember she said she had finals this week."
        return
    mc.name "I was wondering if you would want to go out for a few drinks some night soon."
    if kaya.progress.lust_step < 2:
        the_person "Oh, I appreciate the thought, but maybe we could do something else instead?"
        the_person "Being under 21 in a bar can be kind of weird sometimes."
        return
    the_person "Oh! I'm always up for a little liquid refreshment. When were you thinking?"
    call date_schedule_selection(the_person, 4) from _date_schedule_night_bar_in_person_with_kaya_02
    if _return:
        $ create_bar_date_action(the_person, _return)
        "You give her the location of the bar downtown, and you agree to meet there at the specified time."
        the_person "Sounds great! They have a pool table, right?"
        mc.name "Of course."
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return



