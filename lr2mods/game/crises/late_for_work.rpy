## Late for Work Crisis Mod by Tristimdorion
init 10 python:
    def late_for_work_requirement():
        return (time_of_day < 3
            and mc.is_at_office
            and mc.business.number_of_employees_at_office > 2)

    late_for_work_action = ActionMod("Late for Work", late_for_work_requirement, "late_for_work_action_label",
        menu_tooltip = "An employee is late for work.", category = "Business", is_crisis = True)

label late_for_work_action_label():
    #Lets get the girl of interest (exclude Sarah on mondays).
    $ exclude_list = [] if day%7 != 0 else [sarah]
    $ the_person = get_random_from_list([x for x in mc.business.employees_at_office if x not in exclude_list])
    if the_person is None:
        return

    $ mc.change_location(lobby)
    $ the_person.apply_outfit(the_person.planned_outfit)    # she was outside -> not wearing uniform
    "As you are walking through the main corridor you spot [the_person.possessive_title] rushing through the entrance doors."
    if the_person.sluttiness < 40:
        $ the_person.draw_person(position="stand3", emotion="default")
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                if time_of_day != 1:
                    mc.name "What's going on [the_person.title]?"
                    the_person "Sorry [the_person.mc_title], I was reading during my lunch break and totally lost track of time."
                else:
                    mc.name "Do you know what time we start here [the_person.title]?"
                    the_person "Sorry [the_person.mc_title], I missed my bus."
                mc.name "I don't care what you have to do, but I need you to be here on time. Now get going..."
                $ the_person.change_stats(obedience = 3, happiness = -2)

            "Punish her for being late" if office_punishment.is_active and mc.business.is_work_day:
                if time_of_day != 1:
                    mc.name "What's going on [the_person.title]?"
                    the_person "Sorry [the_person.mc_title], I was reading during my lunch break and totally lost track of time."
                else:
                    mc.name "Do you know what time we start here [the_person.title]?"
                    the_person "Sorry [the_person.mc_title], I missed my bus."

                mc.name "That's not my problem [the_person.title]. I'm going to have to write you up for this."
                the_person "Oh, I... I'm sorry [the_person.mc_title]..."
                $ the_person.add_infraction(Infraction.disobedience_factory())
                mc.name "I'm sure you'll learn your lesson in the future."

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                mc.name "Well okay now, run along quickly, [the_person.title]."
                $ the_person.change_stats(obedience = -2, happiness = 2)

        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title!c] quietly rushes to her desk."
    elif the_person.has_significant_other:   # high sluttiness non single girls
        $ the_person.cum_on_tits(add_to_record = False)
        $ the_person.draw_person(position="stand3", emotion="default")
        if time_of_day != 1:
            the_person "I'm sorry [the_person.mc_title], [the_person.SO_name] needed some personal attention after our lunch date."
        else:
            the_person "I'm sorry [the_person.mc_title], [the_person.SO_name] needed some personal attention when he dropped me off at the office."

        mc.name "I see, it's all over your outfit."
        "She blushes as she looks down at her cum covered chest."

        $ the_clothing = the_person.outfit.get_upper_top_layer
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person "I am really sorry [the_person.mc_title]."
                if the_clothing:
                    mc.name "I don't care, next time be on time and clean up your [the_clothing.display_name]."
                else:
                    mc.name "I don't care, next time be on time and make your tits presentable."
                $ the_person.change_stats(obedience = 3, happiness = -2)

            "Punish her for being late" if office_punishment.is_active and mc.business.is_work_day:
                mc.name "Do you know what time we start here [the_person.title]?"
                the_person "I am really sorry [the_person.mc_title]."
                mc.name "I don't care [the_person.title]. I'm going to have to write you up for this."
                $ the_person.add_infraction(Infraction.disobedience_factory())
                mc.name "I'm sure you'll learn your lesson in the future."

            "Spank her right here":
                call late_for_work_spanking(the_person) from _call_late_for_work_spanking_1

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                if the_clothing:
                    mc.name "Well at least clean up your [the_clothing.display_name], before you start."
                else:
                    mc.name "At least get that cum off your tits, before you go to work."
                the_person "Thank you, [the_person.mc_title]!"
                $ the_person.change_stats(obedience = -2, happiness = 2)

            "What a coincidence..." if the_person.is_affair:
                mc.name "I'm feeling the need for a little personal attention myself."
                the_person "Oh, is that so?"
                if the_clothing:
                    mc.name "That's right. Get on your knees, I want your practised mouth on my cock now."
                else:
                    mc.name "That's right. Get on your knees, I won't be content with just your tits."
                if the_person.is_submissive:
                    $ the_person.change_stats(arousal = 30, obedience = 5, happiness = 5, slut = 1, max_slut = 50)
                    the_person "Oh god, I love it when you take charge like this..."
                else:
                    $ the_person.change_stats(arousal = 20, obedience = 2, happiness = 2)
                    the_person "Mmm, sounds fun..."

                $ the_person.draw_person(position = "kneeling1")
                if the_person.has_taboo(["touching_penis"]):
                    "She slowly gets down on her knees and opens the zipper on your pants."
                    the_person "Oh my, that's a nice specimen, if only I had known sooner..."
                    "She pulls your cock out and starts pumping until it's fully erect."
                    $ the_person.break_taboo("touching_penis")
                else:
                    "She quickly gets down on her knees. She pulls your cock out of your pants and gives it a couple strokes."
                $ mc.change_locked_clarity(10)

                if the_person.has_taboo(["sucking_cock"]):
                    mc.name "Ok, now get to work, I have a busy day today."
                    the_person "Yes [the_person.mc_title], I was just wondering if I can fit that into my mouth."
                    $ the_person.draw_person(position = "blowjob")
                    "She bends forward, slowly sliding your cock into her mouth."
                    $ the_person.break_taboo("sucking_cock")
                else:
                    if the_person.opinion.giving_blowjobs > 0:
                        the_person "Mmm, can't believe I get to suck my two favourite cocks in the same morning..."
                    $ the_person.draw_person(position = "blowjob")
                    "Her mouth opens and envelops your cock. She begins to suck you off eagerly."

                call mc_sex_request(the_person) from _call_mc_sex_request_late_for_work_bj_1
                $ the_report = _return
                if the_report.get("girl orgasms",0) > 0:
                    "It takes [the_person.title] a minute before she finally stands up, recovering from her orgasm."
                $ the_person.draw_person(position="stand3", emotion="default")
                if the_report.get("guy orgasms",0) > 0:
                    "Satisfied with her work, you enjoy the afterglow of your orgasm."
                else:
                    "You decide not to cum for her at this time."
                mc.name "That's enough for now. Try to be on time from now on, or at least be ready to service me again if you {i}are{/i} going to be late."
                the_person "Anything for you, [the_person.mc_title]!"
                $ the_person.change_stats(obedience = 2)

        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title!c] rushes to the ladies' room to clean up."
        $ the_clothing = None
    elif persistent.show_ntr and the_person.sluttiness > 80 and not the_person.is_girlfriend and mc.business.is_work_day: # NTR Enabled very slutty single girls
        $ the_person.cum_on_face(add_to_record = False)
        $ the_person.cum_on_tits(add_to_record = False)
        $ the_person.draw_person(position="stand3", emotion="default")
        if time_of_day != 1:
            the_person "Sorry [the_person.mc_title], a business lunch with a client took a little longer than expected. You can let marketing know I made the sale."
        else:
            the_person "Sorry [the_person.mc_title], a client caught me in the parking lot and wanted to have a business meeting in his car. You can let marketing know I made the sale."

        mc.name "I can see that, you are literally covered in your efforts."
        "She smiles proudly while you check out her cum covered face and chest."

        menu:
            "Send her to work":
                mc.name "Well, it sure does look like it was a productive meeting. Go clean yourself up before you get back to work. I don't want you dripping that all over the building."
                if the_person.opinion.cum_facials > 0:
                    the_person "Aww. But I like the way it feels."
                elif the_person.opinion.cum_facials < 0:
                    the_person "Definitely, I hate feeling all sticky."
                else:
                    the_person "Of course [the_person.mc_title]."

            "Punish her for inappropriate behaviour" if office_punishment.is_active and mc.business.is_work_day:
                mc.name "That's not how we do business around here [the_person.title]."
                the_person "Really, I thought..."
                mc.name "I don't care [the_person.title]. I'm going to have to write you up for this."
                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())
                mc.name "I'm sure you'll learn your lesson in the future."

            "Spank her right here":
                call late_for_work_spanking(the_person) from _call_late_for_work_spanking_2

            "Request her service":
                mc.name "Very good, now I require the same level of dedication, make your boss happy and get on your knees."
                if the_person.is_submissive:
                    $ the_person.change_stats(arousal = 50, obedience = 5, happiness = 5, slut = 1, max_slut = 50)
                    the_person "Yes boss, I love it when you command me..."
                else:
                    $ the_person.change_stats(arousal = 30, obedience = 2, happiness = 2)
                    the_person "If you insist, [the_person.mc_title]!"

                $ the_person.draw_person(position = "kneeling1")
                if the_person.has_taboo(["touching_penis"]):
                    "She slowly gets down on her knees and opens the zipper on your pants."
                    the_person "Oh my, that's a nice specimen, if only I had known sooner..."
                    "She pulls your cock out and starts pumping until it's fully erect."
                    $ the_person.break_taboo("touching_penis")
                else:
                    "She quickly gets down on her knees. She pulls your cock out of your pants and gives it a couple strokes."
                $ mc.change_locked_clarity(10)

                if the_person.has_taboo(["sucking_cock"]):
                    mc.name "Ok, now get to work, I have a busy day today."
                    the_person "Yes [the_person.mc_title], I was just wondering if I can fit that into my mouth."
                    $ the_person.draw_person(position = "blowjob")
                    "She bends forward, slowly sliding your cock into her mouth."
                    $ the_person.break_taboo("sucking_cock")
                else:
                    if the_person.opinion.giving_blowjobs > 0:
                        the_person "Mmm, I just love to suck your cock. This really makes my day, two blowjobs..."
                    $ the_person.draw_person(position = "blowjob")
                    "Her mouth opens and envelops your cock. She begins to suck you off eagerly."

                call mc_sex_request(the_person) from _call_mc_sex_request_late_for_work_bj_3
                $ the_report = _return
                if the_report.get("girl orgasms",0) > 0:
                    "It takes [the_person.title] a minute before she finally stands up, recovering from her orgasm."
                $ the_person.draw_person(position="stand3", emotion="default")
                if the_report.get("guy orgasms",0) > 0:
                    $ the_person.slap_ass()
                    "Satisfied with her work, you give her a smack on her bottom."
                else:
                    "You decide to deny her your cum this time."
                mc.name "Now get back to work, my little cocksucker."
                if the_person.is_submissive:
                    the_person "Yes boss, as you wish."
                else:
                    the_person "Alright [the_person.mc_title], right away."
                if not the_person.is_wearing_planned_outfit:
                    $ the_person.apply_planned_outfit(show_dress_sequence = True)

        $ the_person.draw_person(position = "walking_away")
        "The client wires the money to your company account, but must have forgotten to actually place an order."
        $ mc.business.change_funds(250, "Sales")

    else: #high sluttiness single girls
        $ the_person.draw_person(position="stand3", emotion="default")
        if time_of_day != 1:
            the_person "[the_person.mc_title]! I know this looks bad. I went for a walk during lunch and I took a wrong turn somewhere."
            "You feel yourself roll your eyes for a moment involuntarily."
            the_person "I had to retrace my steps, but... ummm... I made a wrong turn somewhere."
        else:
            the_person "[the_person.mc_title]! I know this looks bad. I have a great excuse for being late, I swear!"
            "You feel yourself roll your eyes for a moment involuntarily."
            the_person "I just had to... ummm... my car had a... a thing wrong with it!"
            mc.name "Oh? What was it doing?"
            if mc.business.is_work_day:
                the_person "It was... Look I'm sorry I'm late, it won't happen again. Please don't write me up!"
            else:
                the_person "It was... Look I'm sorry I'm late, it won't happen again."
        $ the_person.draw_person(position="stand4", emotion="happy")
        "She gives you a big fake smile and strikes a pose."
        the_person "I could do something... you know... to make it up to you!"
        "She puts her hand on your crotch. She looks you in the eye and licks her lips."
        menu:
            "Lecture Her On Being Late":
                $ the_person.draw_person(emotion = 'sad')
                if time_of_day == 1:
                    mc.name "You know how long your break lasts, [the_person.title]."
                else:
                    mc.name "Do you know what time we start here, [the_person.title]?"
                the_person "I am really sorry, [the_person.mc_title]."
                mc.name "I don't care, next time be on time and make your tits presentable."
                $ the_person.change_stats(obedience = 3, happiness = -2)

            "Let it slide":
                $ the_person.draw_person(emotion = 'happy')
                mc.name "Well okay now, run along quickly, [the_person.title]."
                $ the_person.change_stats(obedience = -2, happiness = 2)

            "Punish her for trying to seduce you" if office_punishment.is_active and mc.business.is_work_day:
                if time_of_day != 1:
                    mc.name "You know how long your break lasts, [the_person.title]."
                else:
                    mc.name "Do you know what time we start here, [the_person.title]?"
                the_person "I am really sorry, [the_person.mc_title]."
                mc.name "I don't care, [the_person.title]. I'm going to have to write you up for this."
                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())
                mc.name "I'm sure you'll learn your lesson in the future."

            "Spank her right here":
                call late_for_work_spanking(the_person) from _call_late_for_work_spanking_3

            "Make it up to me" if the_person.is_willing(blowjob):
                mc.name "If you want to make it up to me, get on your knees."
                if the_person.is_submissive:
                    $ the_person.change_stats(arousal = 35, obedience = 5, happiness = 5, slut = 1, max_slut = 50)
                    the_person "Oh god, I love it when you take charge like this..."
                else:
                    $ the_person.change_stats(arousal = 25, obedience = 2, happiness = 2)
                    the_person "If you insist, [the_person.mc_title]!"

                $ the_person.draw_person(position = "kneeling1")
                if the_person.has_taboo(["touching_penis"]):
                    "She slowly gets down on her knees and opens the zipper on your pants."
                    the_person "Oh my, that's a nice specimen, if only I had known sooner..."
                    "She pulls your cock out and starts pumping until it's fully erect."
                    $ the_person.break_taboo("touching_penis")
                else:
                    "She quickly gets down on her knees. She pulls your cock out of your pants and gives it a couple strokes."
                $ mc.change_locked_clarity(10)

                if the_person.has_taboo(["sucking_cock"]):
                    mc.name "Ok, now get to work, I have a busy day today."
                    the_person "Yes [the_person.mc_title], I was just wondering if I can fit that into my mouth."
                    $ the_person.draw_person(position = "blowjob")
                    "She bends forward, slowly sliding your cock into her mouth."
                    $ the_person.break_taboo("sucking_cock")
                else:
                    if the_person.opinion.giving_blowjobs > 0:
                        the_person "Mmm, can't believe I get to suck your cock. This is how to start the day off right..."
                    $ the_person.draw_person(position = "blowjob")
                    "Her mouth opens and envelops your cock. She begins to suck you off eagerly."

                call mc_sex_request(the_person) from _call_mc_sex_request_late_for_work_bj_2
                $ the_report = _return
                if the_report.get("girl orgasms",0) > 0:
                    "It takes [the_person.title] a minute before she finally stands up, recovering from her orgasm."
                $ the_person.draw_person(position="stand3", emotion="default")
                if the_report.get("guy orgasms",0) > 0:
                    "Satisfied with her work, you enjoy the afterglow of your orgasm."
                else:
                    "You decide not to cum for her at this time."
                mc.name "That's enough for now. Try to be on time from now on, or at least be ready to service me again if you {i}are{/i} going to be late."
                the_person "It will be my pleasure, [the_person.mc_title]!"
                $ the_person.change_stats(obedience = 2)

        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title!c] rushes away."

    $ clear_scene()
    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    return

label late_for_work_spanking(the_person):
    mc.name "A naughty employee like you needs to be punished. But just lecturing you wouldn't do the trick, would it?"
    the_person "I'm not sure what you're saying..."
    mc.name "Turn around, [the_person.title]. I'm going to give you the spanking you deserve."
    if the_person.is_submissive:
        $ the_person.change_stats(arousal = 35, obedience = 5, happiness = 5, slut = 1, max_slut = 30)
        the_person "Oh god, yes sir anything you say!"
    else:
        $ the_person.change_stats(arousal = 25, obedience = 2, happiness = 2)
        the_person "If you insist, [the_person.mc_title]."
    call fuck_person(the_person, start_position = spanking, position_locked = True) from _call_fuck_person_late_for_work_spanking_01
    if the_person.is_submissive:
        if not the_person.can_be_spanked:
            $ the_person.unlock_spanking()
            the_person "Oh god, [the_person.mc_title]... that was hot... I'm sorry, I'll try not to be late again!"
            "She really seemed to enjoy her spanking. Maybe you should work it into your normal foreplay..."
    $ the_person.draw_person()
    mc.name "That's enough for now. Try to be on time from now on, or I'll have to spank you again."
    if not (the_person.has_taboo("vaginal_sex") and the_person.has_taboo("anal_sex")):
        the_person "Is there anything else you wanted to do with me?"
        "Her suggestive tone implies she wouldn't mind if you took her right here..."
        menu:
            "Fuck her" if not the_person.has_taboo("vaginal_sex"):
                mc.name "Perhaps I should teach you another lesson."
                call fuck_person(the_person, start_position = standing_doggy, position_locked = True) from _call_fuck_person_late_for_work_spanking_02
                mc.name "I think it's time you got back to work, [the_person.title]."
            "Fuck her ass" if not the_person.has_taboo("anal_sex"):
                mc.name "Perhaps I should teach you another lesson."
                call fuck_person(the_person, start_position = anal_standing, position_locked = True) from _call_fuck_person_late_for_work_spanking_03
                mc.name "I think it's time you got back to work, [the_person.title]."
            "Let her go":
                mc.name "I think it's time you got back to work, [the_person.title]."

    the_person "Yes sir!"
    "She quickly brings her clothing in order."
    $ the_person.apply_outfit(the_person.planned_outfit, show_dress_sequence = True)
    mc.name "Now back to work [the_person.fname]!"
    return
