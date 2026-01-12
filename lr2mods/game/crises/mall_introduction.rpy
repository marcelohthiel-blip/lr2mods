## Mall Introduction Crisis Mod by Tristimdorion
label mall_introduction_action_label():
    $ (known_person, stranger, name) = mall_introduction_get_actors()

    if known_person is None or stranger is None:
        $ known_person = None
        $ stranger = None
        return

    python:
        scene_manager = Scene()
        scene_manager.add_actor(known_person, position = "stand4", emotion = "happy", display_transform = character_center_flipped)
        scene_manager.add_actor(stranger, position = "stand3")

    known_person "Oh, hello [known_person.mc_title], how nice to see you here."
    mc.name "Hello [known_person.title], nice to see you too."

    # set titles for unknown person
    python:
        formatted_title = stranger.create_formatted_title(f"{stranger.name} {stranger.last_name}")
        stranger.set_title(renpy.random.choice([stranger.name, f"{stranger.formal_address} {stranger.last_name}"]))
        stranger.set_possessive_title()
        stranger.set_mc_title()
        stranger.set_event_day("day_met")
        title_choice = f"{mc.name} {mc.last_name}"

    known_person "Let me introduce my [name!l] [formatted_title]."
    "[formatted_title] holds her hand out to shake yours."

    if known_person.is_employee:
        known_person "And this is my boss, [title_choice]."
    elif known_person.is_intern:
        known_person "And this is my benefactor, [title_choice]."
    elif known_person == lily:
        known_person "And this is my brother, [title_choice]."
    elif known_person == mom:
        known_person "And this is my son, [title_choice]."
    elif known_person == aunt:
        known_person "And this is my nephew, [title_choice]."
    elif known_person == cousin:
        known_person "And this is my cousin, [title_choice]."
    else:
        known_person "And this is my friend, [title_choice]."

    mc.name "It's a pleasure to meet you, [formatted_title]."
    $ scene_manager.update_actor(stranger, emotion = "happy")
    $ stranger.change_love(5)
    stranger "The pleasure is all mine, [stranger.mc_title]."
    if formatted_title != stranger.title:
        stranger "But please, call me [stranger.title]."

    # bonus stats when the person knows you more intimately
    if known_person.sluttiness > 20 or known_person.love > 20:
        if known_person.is_employee:
            if known_person.sluttiness > 40:
                known_person "You should get to know him more intimately [stranger.fname], you should apply for a position in the company."
            else:
                known_person "I promise you [stranger.fname], he is a great boss. You should go out with him sometime."
        else:
            if known_person.sluttiness > 40:
                known_person "He can show you a really good time [stranger.fname], if you know what I mean."
            else:
                known_person "I have to tell you [stranger.fname], he is a great person to hang out with."

        $ stranger.change_stats(happiness = 10, love = 5)

        if stranger.sluttiness > 30:
            stranger "Well, he's very handsome [known_person.fname], I wouldn't mind going on a date with him."
        elif stranger.sluttiness > 10:
            stranger "He is very cute [known_person.fname], I might just do that."
        else:
            stranger "I trust your judgement [known_person.fname], perhaps we could go out sometime."

    mc.name "It was great meeting you both here. I'll see you around [stranger.title]."
    if stranger.has_job(prostitute_job):
        stranger "If you ever want some company, give me a call, I'm sure we can come to some kind of arrangement."
        "She hands you a business card with her phone number."
        $ mc.phone.register_number(stranger)
        $ stranger.learn_job(prostitute_job)

    $ scene_manager.update_actor(stranger, position = "back_peek")
    $ scene_manager.update_actor(known_person, position = "walking_away")

    "While walking away [stranger.title] looks back at you with a smile."

    python:
        scene_manager.clear_scene()
        # make sure they have a relationship
        mall_introduction_update_relationship(known_person, stranger)
        # lock event for time delay
        mc.business.set_event_day("mall_introduction")
        # Release variables
        title_choice = None
        formatted_title = None
        known_person = None
        stranger = None
        name = None
    return
