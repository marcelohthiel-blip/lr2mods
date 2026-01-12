label alexia_date_take_home_her_place(date_type = None):
    #intro
    $ the_person = alexia
    $ the_person.draw_person(position = the_person.idle_pose)

    #checks
    if the_person.has_role(affair_role) or not the_person.relationship == "Single":
        #We having an affair -or- she still in a relationship with somebody else
        the_person "Oh shit!"
        the_person "[the_person.SO_name] is home ..."
        "She grabs your hands tighter."
        the_person "Change of plan... Let's go to a hotel instead. I. WANT. YOU."
        menu:
            "Hotel":
                mc.name "That sounds like a great idea."
                "You both re-enter the taxi to a nearby hotel."
                call alexia_date_go_to_hotel(the_person) from _call_alexia_date_go_to_hotel
                return
            "Call It a Night":
                mc.name "Too late, I think he already heard us."
                $ the_person.change_happiness(-5)
                "She nods, but looks hurt."
                the_person "Right, well, have a good night."
                "You hopped back into the taxi and head home."
                return

    #She no longer involved with another guy
    the_person "My big bed missed a good tumbling."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    menu:
        "Her Place":
            "You snicker."
            mc.name "Your big bed... Really?"
            the_person "Oh shut up. Fine. I need a good dicking. Happy?"
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(5)
            mc.name "I can arrange that."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(5)
            call alexia_date_go_to_her_place(the_person) from _call_alexia_date_go_to_her_place
        "Call It a Night":
            mc.name "I'd like to call it an early night today, but maybe I'll take you up on the offer next time."
            $ the_person.change_happiness(-5)
            "She nods, but looks hurt."
            the_person "Right, well, have a good night."
            "You order her a taxi, and you step outside with her and wait."
            "Her taxi arrives. You give her a goodbye kiss and head home yourself."
    return

label alexia_date_go_to_hotel(the_person):
    $ mc.change_location(downtown_hotel)
    "You walk up to the reception and hire a hotel room for one night. You and [the_person.title] go up to your room."
    $ mc.business.change_funds(-80)
    $ mc.change_location(downtown_hotel_room)
    $ the_person.add_situational_slut("Romanced", 15, "I wanted this!")
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "As soon as the door closed she lunged into your embrace. Her lips met yours with a hunger that had been building for all night long."
    "It was messy, frantic, and utterly intoxicating. Her lips were soft and warm, and the taste of her drink earlier made your head spin."
    "As you pressed her back against the wall, your hands sliding down her sides to grip her hips. She moaned into the kiss, her body arching into yours as if she couldn’t get close enough."
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(5)
    "[the_person.possessive_title!c] hands reaches down and starts to stroke your cock through your pants."
    the_person "Let's get these pants off you..."
    "She reaches down and starts to pull of your pants. You let her pull them off while you take off your shirt."
    "She smiles when your cock springs free."
    the_person "Can't wait for this bad boy to be ravaging my inside..."
    "She fumbled with her zip and starts to get naked."
    the_person "Let's just get all these pesky clothes out of the way..."
    $ the_person.strip_to_vagina()
    "Once naked, she looks at you, waiting for you to make the next move."
    call fuck_person(the_person, private = True) from _call_fuck_person_alex_hotel_fuck
    $ the_person.call_dialogue("sex_review", the_report = _return)
    $ the_person.draw_person(position = "back_peek", emotion="happy")
    the_person "That was...amazing."
    "She whispered, her voice soft and sated. You kissed her forehead, your fingers intertwines each other."
    mc.name "It takes two to dance."
    "You both lay there in silence for a while, the hours slipping away as both basked in the warmth of your escapades."
    the_person "Stay with me?"
    $ sleep_outfit = the_person.outfit
    menu:
        "Stay":
            pass
        "Leave":
            $ the_person.apply_outfit(sleep_outfit)
            mc.name "I might need to leave early tomorrow."
            "You pull her closer to you as you both drifted off to sleep."
            "As morning light shone through, you started to get dressed."
            $ the_person.draw_person(position = "back_peek")
            the_person "You leaving?"
            mc.name "Sleep."
            if (day + 1) == mc.business.is_work_day and the_person.is_employee:
                mc.name "I'll see you at work tomorrow."
            else:
                mc.name "Enjoy your weekend."
            "You give her a kiss and step out of the room and head home."
            $ mc.change_location(bedroom)
            call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_alex_hotel_fuck
            return

    "You pull her closer to you as you both drifted off to sleep."
    "She gave you a loving smile and snuggles into your embrace."
    $ the_person.apply_outfit(sleep_outfit)
    $ the_person.draw_person(position = "walking_away")
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_alex_hotel_fuck_02
    $ the_person.draw_person(position = "back_peek")
    mc.name "Good morning~"
    $ the_person.draw_person(position = "missionary", emotion = "happy")
    the_person "Good morning!"
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    $ the_person.draw_person(position = "kissing")
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "stand3")
    "You both get ready for the day before checking out."
    $ mc.change_location(downtown_hotel)
    return

label alexia_date_go_to_her_place(the_person):
    $ the_person.add_situational_slut("Romanced", 15, "DICK DICK DICK!")
    "You quickly arrange for a taxi to her place."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    "Her hands roams all over you during the ride."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    "You almost tempted to fuck her right inside the taxi."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    if not the_person.mc_knows_address:
        $ the_person.learn_home()
    "Fortunately, after a short ride you pull up in front her apartment. The driver gave you a sly smile and a thumbs up."
    $ driver = Person.get_random_male_name()
    driver "You lucky bastard~ Fuck her good!"
    mc.name "Gotcha!"
    $ the_person.change_to_hallway()
    "She fumbles with her keys, quickly opening the door before dragging you inside eagerly."
    "The door slammed shut behind you."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    $ the_person.draw_person(position = "kissing")
    "She puts her arms around you and kisses your neck, grinding her body against you."
    the_person "Fuck, I can't wait any longer [the_person.mc_title]! I've been thinking about this all night long!"
    mc.name "I thought your big bed needs a good tumbling?"
    "[the_person.possessive_title!c] almost killed you with a glare."
    "Despite the death glare, [the_person.title] starts to strip down."
    $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list())
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    "Not wanting to gain any more ire from her, you follow suit and soon, both of you naked right at her hallway."
    "She get closer again, her body pressed flush against you. Her breath was warm against your neck, her lips brushing your skin."
    $ the_person.draw_person(position = "against_wall")
    "[the_person.possessive_title!c] wrapped her legs around your waist, her arms clinging to your shoulders. As you pinned her against the door, your body pressed tightly against hers. "
    "All you could focus on was [the_person.title], the way her body fit against you, the way her breath hitched as you positioned himself at her pussy."
    "You pushed into her slowly, savoring the feel of her tight warmth enveloping you. She gasped, her nails digging into your shoulders. "
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(20)
    "You could feel her walls clenching around you, pulling you deeper. You paused, letting her adjust to you, but she wasn’t having it. She rolled her hips, urging you on."
    $ play_moan_sound()
    "The sound of flesh meeting flesh filled the hallway, mingling with both ragged breaths."
    if the_person.wants_creampie:
        the_person "Oh fuck that is so deep... Are you... are you going to cum inside me like this?"
    else:
        the_person "Oh fuck that is so deep... You aren't going to cum inside me like this, are you?"
    mc.name "Maybe. I wanna mark your inside as mine."
    "You give your hips a gentle thrust, getting a feel for the angle and penetration depth."
    the_person "MMMM... ahh... okay..."
    call fuck_person(the_person, private = True, condition = make_condition_apartment_door_sex(), start_position = against_wall, start_object = make_door(), skip_intro = True, girl_in_charge = False, position_locked = False, skip_condom = True) from _call_fuck_alex_at_house
    $ the_person.call_dialogue("sex_review", the_report = _return)
    $ the_person.draw_person(position = the_person.idle_pose)
    "As you finish dressing back up..."
    the_person "You leaving?"
    if (day + 1) == mc.business.is_work_day and the_person.is_employee:
        mc.name "Yeah.I'll see you at work tomorrow."
    else:
        mc.name "Yeah. Enjoy your weekend."
    "You give her a kiss and step out of the room and head home."
    $ the_person.clear_situational_slut("Romanced")
    $ clear_scene()
    return
