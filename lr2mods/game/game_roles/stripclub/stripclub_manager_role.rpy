## Strip club storyline Mod by Corrado
# You have some strippers but the business could improve: you need a manager.
# When the strip club has a BDSM room, the role will be improved as Mistress.
# The role is incompatible with: low Charisma, slave_role, having collar.

init 5 python:

    def manager_role_status_acquisition(person):
        if person.is_slave:
            slave_release_slave(person)
            # restore partial stat loss from removing slave
            person.change_stats(happiness = 10, love = 10, obedience = 20, add_to_log = False)

        person.update_opinion_with_score("taking control", 2, add_to_log = False)
        if not person.is_unique and not person.personality == alpha_personality:
            person.change_personality(alpha_personality)

        person.set_possessive_title("your manager")
        return

    def mistress_hunt_for_me_prey(person):
        # first find a non-employee target
        target = get_random_from_list([x for x in known_people_at_location(mc.location, [person]) if not x.is_strip_club_employee and not x.is_employee and willing_to_threesome(person, x)])
        if target:
            return target

        target = get_random_from_list([x for x in known_people_at_location(mc.location, [person]) if not x.is_strip_club_employee and willing_to_threesome(person, x)])
        if target:
            return target

        # alternative find an employee target
        return get_random_from_list([x for x in known_people_at_location(mc.location, [person]) if willing_to_threesome(person, x)])

    def promote_strip_club_stripper_to_manager(person):
        if person.love <= 0:
            person.love = 5
        person.change_stats(happiness = 10, obedience = 5, love = 5)
        person.change_job_assignment(person.current_job.job_definition, stripclub_manager_job, strip_club)
        person.salary_modifier = 1.1

        manager_role_status_acquisition(person)

        add_strip_club_manager_hire_more_stripper_reminder_action()
        add_strip_club_manager_waitresses_suggestion_action()
        add_strip_club_manager_bdsm_room_suggestion_action()
        return

    def promote_strip_club_manager_to_mistress(person):
        person.change_job_assignment(stripclub_manager_job, stripclub_mistress_job, bdsm_room)
        person.salary_modifier = 1.1
        person.set_possessive_title("your mistress")
        return



label promote_to_manager_label(the_person):
    $ the_person.set_event_day("stripclub_last_promotion_day")
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "Maybe. Since I bought this place, I've been turning a profit, but I think business could be better."
    mc.name "Managing the girls' shifts, dealing with suppliers, and keeping an eye on everything here is going to take time, and I'm already pretty busy with other things."
    mc.name "So I wanna ask you, do you think you can manage this place? Are you the girl I'm looking for?"
    the_person "[mc.name], with the previous owner this place was a real mess, and I've seen the changes and the improvement you made."
    the_person "The place is clean, the girls are happy, and I don't see those shady figures hanging around here anymore."
    the_person "I get what you're doing here, and I think I see what you are trying to do."
    mc.name "Okay, [the_person.title], I will let you run the place. Prove to me that I made the right choice."
    "She looks intensely into your eyes. You see in her own eyes the glimmer of excitement for being chosen."
    the_person "I will."
    $ promote_strip_club_stripper_to_manager(the_person)
    return

label manager_role_remove_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I checked your management results and I can't say I'm happy, so I have decided to remove you from your management position."
    $ the_person.draw_person(emotion = "sad")
    the_person "I understand [the_person.mc_title], I can assure you I did my best..."
    mc.name "I know, that's why I'm still keeping you with me here, just as a stripper."
    $ the_person.change_stats(happiness = -10, obedience = 2)
    # this might increase the number of active strippers to 6
    $ the_person.change_job_assignment(stripclub_manager_job, stripclub_stripper_job, strip_club)
    $ the_person.salary_modifier = 1.0
    return

label promote_to_mistress_label(the_person):
    $ the_person.set_event_day("stripclub_last_promotion_day")
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I think someone should manage the BDSM room..."
    the_person "Wow, it would be a kinky job that one! Wait, are you planning to get some other man instead of you to do it?"
    $ the_person.draw_person(emotion = "sad")
    the_person "Because I don't know if I can accept someone else instead of you giving me orders, even if it is you asking me that..."
    the_person "You have been my 'first'... Well, not in the physical way, but you know what I mean, and I think you're the only one I can accept."
    mc.name "Actually, I was planning to have a woman doing the job."
    $ the_person.draw_person(emotion = "angry")
    the_person "What? No way! I will never agree to allow another woman to command me. If you do that, I will be forced to resign!"
    mc.name "And what if that commanding woman is you?"
    $ the_person.draw_person(emotion = "happy")
    the_person "Really? Are you asking me to be, after you, the ultimate authority here?"
    mc.name "I know it's a dirty job, but someone needs to do it."
    "A malicious smile creeps over her face, while she glances over to the other girls."
    the_person "I will do my best... or worst, depending on my mood."
    $ promote_strip_club_manager_to_mistress(the_person)
    return

label mistress_role_remove_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I checked your management results and I can't say I'm happy, so I have decided to remove you from your management position."
    $ the_person.draw_person(emotion = "sad")
    the_person "I understand [the_person.mc_title], I can assure you I did my best..."
    mc.name "I know, that's why I'll keep you with me here, just as a stripper."
    $ the_person.change_job_assignment(stripclub_mistress_job, stripclub_stripper_job, strip_club)
    $ the_person.salary_modifier = 1.0
    return

label mistress_hunt_for_me_label(the_person):
    $ scene_manager = Scene()
    mc.name "Do you think you can find a girl here to have some fun with?"
    the_person "Oh, 'that' kind of fun, [the_person.mc_title]? Sure, let me see..."
    $ scene_manager.add_actor(the_person, position = "walking_away")
    "She starts scanning the room, looking for a new victim."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person "I think I've found what we're looking for, let me work my magic."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She arranges her clothes and starts moving closer to her prey..."
    $ the_person_two = mistress_hunt_for_me_prey(the_person)
    $ scene_manager.hide_actor(the_person)
    if the_person_two is None:
        $ scene_manager.show_actor(the_person, position = "stand3", emotion = "sad")
        the_person "Amazing, she's not interested and I cannot find anyone else... Am I losing my touch?"
        return
    "After a couple of minutes the girls are back."
    $ scene_manager.show_actor(the_person, position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(the_person_two, display_transform = character_center_flipped, position = "stand2", emotion = "happy")
    the_person "I told her we have something nice planned for her, [the_person.mc_title]..."
    mc.name "Good choice [the_person.title]! So [the_person_two.title], would you like to join us?"
    the_person_two "It would be my pleasure [the_person_two.mc_title]!"
    mc.name "Ok, let's find a more appropriate place. Follow me, girls!"
    $ mc.change_location(downtown_hotel)
    $ scene_manager.clear_scene()
    "A couple of minutes later, you are in the hotel. You walk up to the reception desk to get a hotel room for one night."
    $ mc.business.change_funds(-80)
    $ mc.change_location(downtown_hotel_room)

    # readd them, now wearing street clothes, since we are moving to a hotel room
    $ scene_manager.add_actor(the_person, the_person.planned_outfit, position = "back_peek")
    $ scene_manager.add_actor(the_person_two, the_person_two.planned_outfit, position = "walking_away")
    "You open the door of the room and motion the girls to come in. You notice [the_person.title] already grabbing [the_person_two.title]'s ass."
    $ scene_manager.update_actor(the_person, position = "stand4")
    if not the_person.vagina_available:
        "[the_person_two.possessive_title!c] starts moving some of your mistress's clothing to get access to her [the_person.pubes_description] pussy."
        $ scene_manager.strip_to_vagina(the_person, prefer_half_off = True)
    $ scene_manager.update_actor(the_person_two, position = "default")
    if not the_person_two.vagina_available:
        "Your mistress is eager to get access to [the_person_two.possessive_title]'s pussy."
        $ scene_manager.strip_to_vagina(the_person_two, prefer_half_off = True)
    call start_threesome(the_person, the_person_two, girl_in_charge = the_person, start_object = make_bed(), affair_ask_after = False) from _call_start_threesome_mistress_hunt_for_me_label
    "Once you've all had your fun, the girls start getting dressed."
    $ scene_manager.update_actor(the_person, position = "default", display_transform = character_right)
    $ scene_manager.update_actor(the_person_two, position = "default", display_transform = character_center_flipped)
    $ scene_manager.apply_outfits()
    mc.name "This was a lot fun, but lets get back to the club."
    the_person "Yeah, lets go, [the_person_two.fname]."
    $ scene_manager.clear_scene()
    $ the_person.change_location(bdsm_room)
    $ the_person_two.change_location(bdsm_room)
    "After a while you and the girls are back at the club."
    $ mc.change_location(strip_club)
    return
