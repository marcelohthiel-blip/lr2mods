#GLOBAL TODO before releasing this mechanic into the wild
#Need at least three positions that qualify for each sex goal for variety.
#Add new personality dialogue.
#Add dialogue based on sex goals
#Control where MC finishes based on sex goals to have a better chance of meeting the goal.

label get_fucked(the_person, the_goal = None, sex_path = None, private= True, start_position = None, start_object = None, skip_intro = False, report_log = None, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = True, condition = Condition_Type.default_condition()):
    python:
        apply_sex_modifiers(the_person, private) #Apply sex modifiers before choosing goals and positions to avoid choosing positions girl shouldn't accept
        finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
        ask_for_threesome = False
        object_choice = start_object
        start_mc_orgasm = 0
        start_girl_orgasm = 0
        used_mc_energy_serum = False
        the_watcher = None
        girl_in_charge = True
        watch_list = []
        current_node = None
        if report_log:  #We set orgasms in the report to zero for now so that requirement functions can check for them easier.
            is_continuation = True
            start_mc_orgasm = report_log.get("guy orgasms", 0)
            start_girl_orgasm = report_log.get("girl orgasms", 0)
            report_log["guy orgasms"] = 0
            report_log["girl orgasms"] = 0
        else:
            is_continuation = True
            report_log = create_report_log({ "was_public": not private and the_person.location.person_count > 1 })

    if skip_intro:  #If we are already having sex, using whatever condom status presently is
        $ using_condom = mc.condom
    else:
        $ using_condom = requires_condom(the_person)

    # generate a sex path for locked requests
    if not sex_path and not allow_continue and (not the_goal or the_goal == "get mc off"):
        if start_position == blowjob:
            $ sex_path = build_blowjob_path(the_person)
            # $ write_log("Build blowjob path: {}".format(len(sex_path)))
        if start_position == tit_fuck:
            $ sex_path = build_titfuck_path(the_person)
            # $ write_log("Build titfuck path: {}".format(len(sex_path)))

    # break taboos automatically, so the caller doesn't need to remember to do it
    if not ignore_taboo and isinstance(start_position, Position):
        # since we skip intro, it's assumed we are already in the position and use the loop to continue
        if skip_intro:
            $ the_person.break_taboo(start_position.associated_taboo)
        # we don't ask for condom and the mc is not wearing it and we are having intercourse
        if not mc.condom and start_position.skill_tag in ("Vaginal", "Anal"):
            $ the_person.break_taboo("condomless_sex")

    if start_position and not sex_path:
        if not the_goal:    # pick goal based on start position (female centred or male centred)
            $ the_goal = get_goal_based_on_position(start_position)
        $ sex_path = [dom_sex_path_node(start_position, get_goal_completion_requirement(the_goal))]  #If we have a start position only, we set the path to be the start position with MC getting off as the goal

    if not the_goal:
        $ the_goal = create_sex_goal(the_person, report_log)
        if unit_test: #unit_test is for debug dialogue
            "The goal for this session is [the_goal]."

    if the_goal and not sex_path:
        $ sex_path = create_sex_path(the_person, the_goal, prohibit_tags)
        if unit_test:
            "The first position for this session is [sex_path[0].position.name]."

    if not sex_path:  #We couldn't find a sex path, so abort the session, or possibly rerun it relaxing conditions? #TODO
        "[the_person.title] can't think of anything more to do with you."
        $ finished = True
        if unit_test: #unit_test is for debug dialogue
            "No viable path."

    if not object_choice and sex_path:
        $ object_choice = girl_choose_object(the_person, sex_path[0].position)
    if not object_choice:
        "[the_person.title] can't find a good place to have fun with you."
        $ finished = True
        if unit_test:
            "No suitable object"

    if sex_path:
        $ current_node = sex_path.pop(0)  #Pop the first node in the list of sex path nodes.
    #Next we mimic fuck_person() but only with applicable girl in charge parameters.
    #Privacy modifiers
    if mc.location.person_count == 1 and not private and not mc.location.is_public:
        $ private = True #If we're alone in the space we're always Private, even if we had left the possibility for people being around.
    #Next, check for generic conditions that keep us from continuing

    if not finished:
        if current_node.position is None: #There's no position we can take
            "[the_person.title] can't think of anything more to do with you."
            $ finished = True
        elif object_choice is None:
            "[the_person.title] looks around, but can't see anywhere to have fun with you."
            $ finished = True
        elif the_person.energy < 15 :
            the_person "I'm tired. Maybe we will continue this another time."
            $ finished = True

    if sex_path and len(sex_path) > 1 and not finished:
        the_person "Let's get warmed up a little bit first..."
    #TODO determine condom usage. Can probably just call a method from the sex bugfix file

    if the_goal:
        $ set_sex_goal(the_person, the_goal)
    #We should be able to initiate sex. If we need to, call initial intros and taboo breaks.
    if not skip_intro and not finished:
        if (current_node.position.skill_tag == "Vaginal" or current_node.position.skill_tag == "Anal") and using_condom:
            the_person "Hang on a second. I need to wrap this thing up first."
            "[the_person.title] gets a condom out of their own bag and opens it."
            "She holds it at the top of your cock with one hand as she strokes farther and farther with the other hand, rolling the condom down onto it."
            $ mc.condom = True
        if not ignore_taboo and the_person.has_taboo(current_node.position.associated_taboo):
            # call mod taboo break
            $ current_node.position.call_transition_taboo_break(None, the_person, mc.location, object_choice)
            $ the_person.break_taboo(current_node.position.associated_taboo)
        else:
            $ current_node.position.call_intro(the_person, mc.location, object_choice)
    elif not finished and start_position is None:
        # show dialogue since there is probably no intro for the position
        $ current_node.position.call_transition(start_position, the_person, mc.location, object_choice)

    #Now begin the sex loop
    while not finished:
        if mc.condom and go_raw_mid_sex(the_person):
            call remove_condom_go_raw(the_person, current_node.position) from _go_raw__girl_in_charge_01
            $ mc.condom = False
            $ using_condom = False
        if mc.recently_orgasmed and not used_mc_energy_serum and allow_continue and current_node.position.skill_tag in ("Anal", "Vaginal"):
            if perk_system.has_ability_perk("Serum: Energy Regeneration") and mc_serum_energy_regen.trait_tier >= 2 and mc.energy > 30:
                $ mc.recently_orgasmed = False
                $ used_mc_energy_serum = True   # prevent too long looping if she has a lot of energy
                "Your personal Energy Serum allows [the_person.possessive_title] to continue."
        if current_node.position.requires_hard and mc.recently_orgasmed:
            "Your post-orgasm cock softens, stopping [the_person.possessive_title] for now."
            #TODO if this keeps us from accomplishing sex goal, consider rerunning this method from the beginning, or just ending the scene. Or creating a new path?
            $ finished = True
        else:
            $ condition.call_pre_label(the_person, current_node.position, object_choice, report_log)
            $ scene_private = private
            if not private and mc.location.person_count == 1:
                $ scene_private = False #Only pass private to sex desc. if there is actually a witness

            call sex_description(the_person, current_node.position, object_choice, private = scene_private, report_log = report_log) from _call_sex_description_girl_in_charge_override_1

            $ condition.call_post_label(the_person, current_node.position, object_choice, report_log)

            $ report_log["last_position"] = current_node.position
            if not private and not mc.recently_orgasmed:
                call public_sex_post_round(the_person, current_node.position, report_log) from _public_sex_post_round_02
                if not _return:
                    $ finished = True
        if mc.condom and mc.recently_orgasmed: # you orgasmed so you used your condom.
            $ mc.condom = False

        #TODO figure out what to do in the following three cases


        if current_node.position.calculate_energy_cost(mc) > mc.energy - 5:
            "You're too exhausted to let [the_person.possessive_title] keep [current_node.position.verbing] you."
            $ finished = True

        elif current_node.position.calculate_energy_cost(the_person) > the_person.energy - 5:
            the_person "I'm exhausted [the_person.mc_title], I can't keep this up..."
            $ finished = True

        #Determine if the current node has completed it's finished requirement.
        if not finished:
            if current_node.completion_requirement(the_person, report_log):
                if len(sex_path) > 0:
                    $ new_node = sex_path.pop(0)
                    $ object_choice = girl_choose_object(the_person, new_node.position)
                    if object_choice is None:
                        if new_node.position.requires_location == "kneel" or new_node.position.requires_location == "lay":
                            $ object_choice = make_floor()
                        elif new_node.position.requires_location == "lean":
                            $ object_choice = make_wall()
                        else:
                            $ object_choice = make_chair()

                    if mc.recently_orgasmed:
                        # Prevent premature ending of sex-loop due to 'limp dick' while sex loop not finished
                        "She takes a few minutes to get your cock ready for another round."
                        $ mc.recently_orgasmed = False
                    if (new_node.position.skill_tag == "Vaginal" or new_node.position.skill_tag == "Anal") and using_condom and not mc.condom:
                        the_person "Hang on a second. I need to wrap this thing up first."
                        "[the_person.title] gets a condom out of their own bag and opens it."
                        "She holds it at the top of your cock with one hand as she strokes farther and farther with the other hand, rolling the condom down onto it."
                        $ mc.condom = True
                    if not ignore_taboo and the_person.has_taboo(new_node.position.associated_taboo):
                        # call mod taboo break
                        $ current_node.position.call_transition_taboo_break(new_node.position, the_person, mc.location, object_choice)
                        $ the_person.break_taboo(new_node.position.associated_taboo)
                    else:
                        $ current_node.position.call_transition(new_node.position, the_person, mc.location, object_choice)

                    $ current_node = new_node
                    $ new_node = None
                else:
                    $ finished = True    #Sex goal has been accomplished
                    $ the_person.call_dialogue("GIC_finish_response", the_goal = the_goal)
            elif len(sex_path) > 0:
                if not sex_path[0].position.check_clothing(the_person): #We don't meet the clothing requirements for the next position, so we strip some
                    $ the_clothing = choose_strip_sex_position_item(the_person, position = sex_path[0].position)
                    if the_clothing:
                        $ current_node.position.call_strip(the_person, the_clothing, mc.location, object_choice)
                else:
                    call girl_strip_event(the_person, sex_path[0].position, object_choice) from _call_girl_strip_event_girl_in_charge_01

    #TODO create positive feedback here for accomplishing sex goal
    #First condition, she is obedient. offers to keep going or to let MC take over.

    if unit_test:
        $ renpy.say(None, f"Main loop finished: continue is {allow_continue} -> continue function result is {sex_can_continue(the_person, the_node = current_node)}")

    if allow_continue: #Allows sex to keep going after girl finishes objectives
        if sex_can_continue(the_person, the_node = current_node) and the_person.obedience > 140 and mc.arousal_perc > 50:
            "As she finishes up, [the_person.title] gives your erection a couple strokes."
            the_person "Actually, do you want me to keep going? Or maybe you should take over..."
            menu:
                "Keep going":
                    mc.name 'Keep going, this is hot.'
                    the_person "Yes sir!"
                    call get_fucked(the_person, private= private, start_position = current_node.position, start_object = object_choice, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition) from GIC_keeps_going_01
                "Take over":
                    mc.name "Come here, I'm not done with you yet."
                    call fuck_person(the_person, private = private, ignore_taboo = ignore_taboo, report_log = report_log, prohibit_tags = prohibit_tags, condition = condition) from GIC_guy_takes_over_01
                "Finish":
                    mc.name "Let's be done for now."
                    the_person "Okay."
        #Second condition, she isn't obedient but at least likes MC a little bit. She offers to continue
        elif sex_can_continue(the_person, the_node = current_node) and the_person.love > 20 and mc.arousal_perc > 50:
            "As she finishes up, [the_person.title] gives your erection a couple strokes."
            the_person "Wow, you are still rock hard. Do you want me to keep going?"
            menu:
                "Keep going":
                    mc.name 'Yes, please keep going.'
                    the_person "Okay, I can do that!"
                    call get_fucked(the_person, private= private, start_position = current_node.position, start_object = object_choice, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition) from GIC_keeps_going_02
                "Finish":
                    mc.name "Let's be done for now."
                    the_person "Okay."

        #Third condition, she doesn't care for MC. She forces him to beg. She may or may not comply (think Gabrielle)
        elif sex_can_continue(the_person, the_node = current_node) and mc.arousal_perc > 70:
            "As she finishes up, [the_person.title] looks at your rock hard cock."
            the_person "Still hard? I bet you want me to keep going, don't you..."
            "She takes a pause before she continues."
            the_person "If you want me to keep going, you're going to have to beg for it. Want me to?"
            menu:
                "Beg her to continue":
                    mc.name "Oh god, please keep going. I'm so close, just a little bit further!"
                    "She laughs at your plight while she considers what to do."
                    if renpy.random.randint(-150,0) < the_person.love:  #Even at -100 love, she has a 1/3 chance of continuing
                        the_person "Hmm, I guess it's only fair. Maybe I'll even finish again!"
                        $ the_person.change_stats(obedience = -5)
                        call get_fucked(the_person, private= private, start_position = current_node.position, start_object = object_choice, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition) from GIC_keeps_going_03
                    else:
                        the_person "Ha! It was worth letting you defile me just to hear you beg. Not a chance!"
                        "[the_person.possessive_title!c] gets up, leaving you hanging."
                        $ the_person.change_stats(obedience = -5, slut = -1)
                "Finish":
                    mc.name "There's nothing special about you. Let's be done, I can always get a more willing cunt."
                    the_person "Whatever [the_person.mc_title], your loss!"
                    $ the_person.change_stats(obedience = 2, love = -5)
        elif sex_can_continue(the_person) and the_person.love > 50: #She loves you, so she leaves it up to you if you want to keep going.
            $ the_person.draw_person(position = "kissing")
            "As she finishes up, [the_person.title] cuddles up beside you."
            the_person "Mmm, thank you. I needed that really bad."
            "She pauses for a moment."
            the_person "Are you good? Or do you want to keep going?"
            menu:
                "Take over":
                    mc.name "Come here, I'm not done with you yet."
                    call fuck_person(the_person, private = private, ignore_taboo = ignore_taboo, report_log = report_log, prohibit_tags = prohibit_tags, condition = condition) from GIC_guy_takes_over_03
                "Finish":
                    mc.name "Let's be done for now."
                    the_person "Okay."
        elif the_person.is_willing(doggy) and the_person.energy < 50 and mc.arousal_perc > 70 and the_person.energy > 20 and mc.energy > 50: #She's exhausted and can't defend herself briefly from your advances.
            "You get up, but notice that [the_person.title] is a bit slower. She is breathing heavily and appears to be really worn out."
            the_person "Oh god... just give me a minute, okay?"
            $ the_person.draw_person(position = "doggy")
            "She gets on her hands and knees and is obviously worn out. Her current position leaves her ass obviously exposed. You give your rock hard cock a couple strokes and consider taking advantage."
            "She doesn't have the energy to stop you, but if she doesn't like you she might get pretty upset..."
            menu:
                "Fuck her":
                    "You get behind her. You line yourself up with her cunt."
                    the_person "Hey... [the_person.mc_title]... what are you doing?"
                    mc.name "Shhh, quiet."
                    "With one smooth motion you push yourself inside her."
                    if the_person.effective_sluttiness() > 90:
                        the_person "Ohhh god. Go ahead and take what you want, I'll just be along for the ride."
                    elif the_person.effective_sluttiness() > 60:
                        the_person "Ohhhhhh. I'm not sure how long I can do this but if you need to finish that bad go ahead..."
                    else:
                        the_person "What the fuck? Are you kidding me?"
                        "You give her ass a sharp spank."
                        mc.name "Quiet. I'm close to cumming, this will only take a minute."
                        $ the_person.add_situational_obedience("finish_him", 10, "Whatever, just hurry up and finish.")
                        $ the_person.change_stats(happiness = -5, love = -5)
                    call fuck_person(the_person,start_position = doggy, private = private, ignore_taboo = ignore_taboo, report_log = report_log, prohibit_tags = prohibit_tags, condition = condition) from GIC_guy_takes_over_05
                    $ the_person.clear_situational_obedience("finish_him")
                "Finish":
                    "You decide to leave her be."
        elif report_log.get("girl orgasms", 0) - start_girl_orgasm == 0 and the_person.energy > 50 and the_person.arousal_perc > 60:
            the_person "Ah, shit, I'm so horny, I need to get off."
            call get_fucked(the_person, the_goal = "get off", private = private, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition, allow_continue = False) from GIC_keeps_going_04

    python:
        condition.run_rewards(the_person, report_log)
        clear_sex_modifiers(the_person)

        if not is_continuation:
            # sex is a good workout and increases max_energy
            the_person.change_max_energy(report_log.get("girl orgasms",0), add_to_log = False)
            mc.change_max_energy(report_log.get("guy orgasms", 0), add_to_log = False)
            mc.recently_orgasmed = False

        # if we have a watcher make her leave
        if mc.location.allow_walk_in and the_watcher is not None and not is_fixed_watcher:
            the_watcher.draw_person(position = "walking_away", display_transform = character_left_flipped)
            if the_watcher.is_stranger:
                renpy.say(None, "As you finish up with [the_person.possessive_title], you see the stranger quietly slipping of out the door.")
            else:
                renpy.say(None, "As you finish up with [the_person.possessive_title], you see [the_watcher.fname] quietly slipping of out the door.")
            the_watcher.change_location(the_watcher.get_destination() or the_watcher.home)
            the_person.draw_person()

        report_log["end arousal"] = the_person.arousal
        report_log["girl orgasms"] = report_log.get("girl orgasms", 0) + start_girl_orgasm

        the_person.change_arousal(-builtins.max((the_person.arousal / (report_log.get("girl orgasms", 0) + 2)) + 20, the_person.arousal - the_person.max_arousal - 1))

        report_log["guy orgasms"] = report_log.get("guy orgasms", 0) + start_mc_orgasm
        mc.condom = False

        the_person.update_person_sex_record(report_log)
        the_goal = None
        sex_path = None
        current_node = None
        new_node = None
        the_watcher = None
        watch_list = None
        reset_sex_goal(the_person)
    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

# use as wrapper for get_fucked to satisfy mc requests, by building a custom sex path to fullfill request
# for now only supports 'blowjob' and 'titfuck'
label mc_sex_request(the_person, the_request = "blowjob", start_object = None, private = True):
    python:
        if the_request == "cowgirl":
            path = build_cowgirl_path(the_person, get_cowgirl_path_preferred_skill_tag(the_person))
            if not start_object:
                start_object = mc.location.get_object_with_trait("Lay")
            the_goal = "get mc off"
        elif the_request == "vaginal cowgirl":
            path = build_cowgirl_path(the_person, "Vaginal", use_warmup = False)
            if not start_object:
                start_object = mc.location.get_object_with_trait("Lay")
            the_goal = "get mc off"
        elif the_request == "anal cowgirl":
            path = build_cowgirl_path(the_person, "Anal", use_warmup = False)
            if not start_object:
                start_object = mc.location.get_object_with_trait("Lay")
            the_goal = "get mc off"
        elif the_request == "titfuck":
            path = build_titfuck_path(the_person)
            if not start_object:
                start_object = mc.location.get_object_with_trait("Kneel")
            the_goal = "get mc off"
        else:   # default blowjob
            path = build_blowjob_path(the_person)
            if not start_object:
                start_object = mc.location.get_object_with_trait("Kneel")
            the_goal = "oral creampie"

    call get_fucked(the_person, the_goal = the_goal, sex_path = path, private = private, start_object = start_object, skip_intro = True, ignore_taboo = True, allow_continue = False) from _call_get_fucked_mc_request
    $ the_report = _return
    python:
        path = None
        start_object = None
    return the_report

label remove_condom_go_raw(the_person, the_position):
    the_person "Hang on a second..."
    "[the_person.title] slowly pulls off your cock. You feel her give you a couple strokes with her hand."
    "She slowly pulls the condom off your cock."
    mc.name "[the_person.title]?"
    the_person "Sssshhh... I need to feel it... inside me..."
    "[the_person.possessive_title!c] slowly sinks back down onto your shaft, raw this time."
    $ the_person.change_arousal(5)
    $ mc.change_arousal(5)
    "The heat from her body translates perfectly now that you have that piece of latex between you removed. It feels wonderful."
    return

#############################################################
# Generic Outro GIC statement
# Copy past this into a new sex position outro to give easy access to all possible goals.

# if the_goal == "get off":
#     pass
# elif the_goal == "waste cum":
#     pass
# elif the_goal == "hate fuck":
#     pass
# elif the_goal == "vaginal creampie":
#     pass
# elif the_goal == "anal creampie":
#     pass
# elif the_goal == "facial":
#     pass
# elif the_goal == "body shot":
#     pass
# elif the_goal == "get mc off":
#     pass
# elif the_goal == "oral creampie":
#     pass
# else:
#     pass
############################################
