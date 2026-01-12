# Fix for sex mechanic for people who don't have the bugfix branch installed
# Enhancement for pick object (don't show list when only one object can be selected (auto-select it))
# Added condom ask enhancements (Original by BadRabbit)
init -5:
    # when False ask for condom is skipped when girl sluttiness is high
    # when True, the condom ask function will always be called regardless of girl sluttiness
    default persistent.always_ask_condom = False
    default forcedNewPosition = None
    default forcedNewObject = None

label fuck_person(the_person, private= True, start_position = None, start_object = None, skip_intro = False, girl_in_charge = False, self_strip = True, hide_leave = False, position_locked = False, report_log = None, affair_ask_after = True, ignore_taboo = False, skip_condom = False, prohibit_tags = [], condition = Condition_Type.default_condition(), the_watcher = None):
    # When called fuck_person starts a sex scene with someone. Sets up the encounter, mainly with situational modifiers.
    python:
        if report_log is None:
            report_log = create_report_log()

        watch_list = []
        finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
        position_choice = start_position # initialize with start_position (in case girl is in charge or position is locked)
        object_choice = start_object # initialize with start_object (in case girl is in charge or position is locked)
        guy_orgasms_before_control = 0
        girl_orgasms_before_control = 0
        allow_transitions = not (skip_intro or start_position or start_object) # disable first time transitions if we continue a custom intro
        round_choice = "Continue" if skip_intro and start_position and start_object else "Change" # use "Continue" if just had a custom intro
        first_round = True
        has_taken_control = False
        ask_for_condom = skip_condom
        ask_for_threesome = False
        skip_taboo_break = False
        use_condom = mc.condom if skip_condom else False
        stop_stripping = False
        is_fixed_watcher = not the_watcher is None
        willing = 0

        # break taboos automatically, so the caller doesn't need to remember to do it
        if not ignore_taboo and isinstance(start_position, Position):
            # since we skip intro, it's assumed we are already in the position and use the loop to continue
            if skip_intro:
                the_person.break_taboo(start_position.associated_taboo)
            # we don't ask for condom and the mc is not wearing it and we are having intercourse
            if skip_condom and not mc.condom and start_position.skill_tag in ("Vaginal", "Anal"):
                the_person.break_taboo("condomless_sex")

        #Privacy modifiers
        if not private and mc.location.person_count <= 1:   # there is not one around so make it private
            private = True
        report_log["was_public"] = not private
        apply_sex_modifiers(the_person, private)

    # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    while not finished:
        if girl_in_charge:
            if not position_choice is None and position_choice.skill_tag == "Foreplay" and not mc.recently_orgasmed and not first_round and not position_locked:
                # girl has got you hard again, now let her pick an actual sex position (clear foreplay position)
                if not the_person.vagina_visible: # lets see if she is willing to go further
                    $ the_person.strip_outfit_to_max_sluttiness()
                $ position_choice = None

            # The girls decisions set round_choice here.
            if position_choice is None:
                $ position_choice = girl_choose_position(the_person, ignore_taboo = ignore_taboo) #Can be none, if no option was available for her to take.
                if position_choice is not None:
                    # We need to make sure we're using an appropriate object
                    $ object_choice = girl_choose_object(the_person, position_choice)
                    $ round_choice = "Change"

            # no initial object choice
            if first_round and position_choice and not object_choice:
                $ object_choice = girl_choose_object(the_person, position_choice)

            if position_choice is None: #There's no position we can take
                "[the_person.title] can't think of anything more to do with you."
                $ round_choice = "Girl Leave"
            elif object_choice is None:
                "[the_person.title] looks around, but can't see anywhere to have fun with you."
                $ round_choice = "Girl Leave"
            elif report_log.get("guy orgasms", 0) > guy_orgasms_before_control and report_log.get("girl orgasms", 0) > girl_orgasms_before_control: #Both parties have been satisfied
                mc.name "Whew, that was amazing, and I'm guessing you enjoyed it too."
                $ round_choice = "Girl Leave"
            elif report_log.get("guy orgasms", 0) > guy_orgasms_before_control and position_locked: # MC liked what we did
                mc.name "That felt great, we should do this again soon."
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) > girl_orgasms_before_control and not (the_person.love > 50 or the_person.obedience > 200): #She's cum and doesn't care about you finishing.
                the_person "Whew, that felt great. Thanks for the good time [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) > girl_orgasms_before_control + 1: # she's had her fill and doesn't care about you anymore
                the_person "Oh my god, I came so hard, thanks a lot [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) == 0 and the_person.energy < 15 :
                the_person "That was nice, but I'm tired. We will continue this another time."
                $ round_choice = "Girl Leave"
            else:
                if has_taken_control:
                    $ has_taken_control = False
                    $ the_person.call_dialogue("sex_take_control")
                    call get_fucked(the_person, private = private, the_goal = "get off", skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, condition = condition, allow_continue = not position_locked) from _call_get_fucked_fuck_person
                    $ round_choice = "Girl Leave"

                if round_choice == "Change" and position_choice and object_choice:
                    # show dialogue of girl changing position on her own
                    if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                        $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                        $ the_person.break_taboo(position_choice.associated_taboo)
                    elif not skip_intro:
                        $ position_choice.call_transition(position_choice, the_person, mc.location, object_choice)
                    $ round_choice = "Continue"
        else:
            # Forced actions (when the guy is in charge) go here and set round_choice.
            pass
            # if position_choice is None:
            #     $ round_choice = "Change" #Something has kicked our position out, so we need to ask the player what to do.

            # Note: There can be no chance based decisions in this section, because it loops on menu interactions, not on actual rounds of sex. Those go after the "change or continue" loop

        if round_choice is None: #If there is no set round_choice
            #TODO: Add a variant of this list when the girl is in control to ask if you want to resist or ask/beg for something.
            call screen main_choice_display(build_menu_items([build_round_choice_menu(the_person, position_choice, position_locked, object_choice, ignore_taboo = ignore_taboo, condition = condition, allow_transitions = allow_transitions, hide_leave = hide_leave)]))
            $ round_choice = _return #This gets the players choice for what to do this round.

        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue" or round_choice == "early_orgasm":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignore all of that
                $ current_position = position_choice
                if start_position is None: #The first time we get here,
                    call pick_position(the_person, current_position = current_position, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, condition = condition) from _call_pick_position_bugfix
                else:
                    $ position_choice = start_position

                $ object_choice = pick_object(the_person, position_choice, forced_object = start_object)

                if position_choice and object_choice and position_choice != current_position:
                    call check_position_willingness(the_person, position_choice, ignore_taboo = ignore_taboo, skip_condom_ask = True) from _call_check_position_willingness_fuck_person
                    if willing < 1: #If she wasn't willing for whatever reason (too slutty a position, not willing to wear a condom) we clear our settings and try again.
                        if willing == -1 or (willing == -2 and position_locked): # angry reject ends interactions
                            $ finished = True
                            $ report_log["is_angry"] = True
                            $ position_choice = None
                            $ object_choice = None
                        elif willing == -2:   #She hates that position, but suggests a different one.
                            $ position_choice = suggest_alternate_sex_position(the_person, position_choice, object_choice, ignore_taboo = ignore_taboo)
                            $ object_choice = None
                            if position_choice.verb:
                                the_person "I have another idea... what if we [position_choice.verb] like this?"
                            else:
                                the_person "I have another idea... what if we just did this?"
                            "[the_person.possessive_title!c] leans into your ear and whispers, describing [position_choice.name]."
                            menu:
                                "[position_choice.name]":
                                    mc.name "Let's do it."
                                    $ object_choice = pick_object(the_person, position_choice)
                                "Do something else":
                                    mc.name "I think I can come up with something else instead..."
                                    $ position_choice = None
                        else:
                            $ position_choice = None
                            $ object_choice = None

                        $ skip_intro = False

                if position_choice and object_choice and position_choice != current_position:
                    call should_ask_for_condom(the_person, position_choice) from _call_should_ask_for_condom_fuck_person
                    if skip_intro:
                        $ skip_intro = False  # turn off skip, for when we get here the second time.
                    elif first_round:
                        $ the_person.draw_person() #Draw her standing until we pick a new position
                        if not ignore_taboo and the_person.has_taboo(position_choice.associated_taboo):
                            # call mod taboo break
                            $ position_choice.call_transition_taboo_break(position_choice, the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            if _return == 0:    # if we don't put on condom
                                $ position_choice.call_intro(the_person, mc.location, object_choice)
                            else: # if we have a condom, penis is out, so don't call intro (that mostly has take penis out dialogue)
                                $ position_choice.call_transition(start_position, the_person, mc.location, object_choice)
                    else:
                        $ the_person.change_arousal(-5) #Changing position lowers your arousal slightly
                        $ mc.change_arousal(-5)
                        if not ignore_taboo and the_person.has_taboo(position_choice.associated_taboo):
                            $ the_person.draw_person() #Draw her during taboo break transition
                            $ position_choice.call_transition_taboo_break(position_choice, the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_transition(start_position, the_person, mc.location, object_choice)
                    # redraw after transition not before
                    $ position_choice.redraw_scene(the_person)

                $ the_person.current_position = position_choice

            if round_choice == "Continue" and not allow_transitions:
                call check_position_willingness(the_person, position_choice, ignore_taboo = ignore_taboo, skip_dialog = skip_intro) from _call_check_position_willingness_fuck_person_2

            $ allow_transitions = True
            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ current_position = None
            $ start_object = None
            # $ renpy.say(None, "Continue round => Position: " + position_choice.name + ", object: " + object_choice.name)
            if position_choice and object_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                $ report_log["last_position"] = position_choice
                if willing == 2:
                    $ happiness_change = (the_person.opinion.being_submissive - 1 + report_log.get("girl orgasms", 0)) * 2
                    if happiness_change > 0 and the_person.happiness > 200:
                        pass
                    else:
                        $ the_person.change_happiness(happiness_change)    #default -2 happiness per turn, being submissive negates or subverts happiness loss.
                    if the_person.is_dominant:
                        $ the_person.change_obedience(-2)   #If she hates being submissive, she slowly gets less submissive

                $ condition.call_pre_label(the_person, position_choice, object_choice, report_log)

                if not ignore_taboo and the_person.has_taboo(position_choice.associated_taboo):
                    $ the_person.draw_person() #Draw her standing during the transition taboo break
                    $ position_choice.call_transition_taboo_break(position_choice, the_person, mc.location, object_choice)
                    $ the_person.break_taboo(position_choice.associated_taboo)

                $ scene_private = private
                if not private and mc.location.person_count == 1:
                    $ scene_private = False #Only pass private to sex desc. if there is actually a witness
                if round_choice == "early_orgasm":
                    "You rapidly build arousal, using your orgasm control to force yourself to cum early."
                    $ mc.change_arousal(100)
                call sex_description(the_person, position_choice, object_choice, private = scene_private, report_log = report_log) from _call_sex_description_bugfix

                if isinstance(_return, tuple) and len(_return) == 2 and not mc.recently_orgasmed:
                    # received new position from this scene, continue with that
                    $ start_position = _return[0]
                    $ start_object = _return[1]
                else: # only when we don't have a new position
                    # If the girl has an orgasm due to MC coming, she gets a guaranteed trance upgrade
                    if the_person.arousal_perc >= 100:
                        if report_log.get("girl orgasms", 0) == 0:
                            the_person "Oh, [the_person.mc_title], I'm cumming..."
                        else:
                            the_person "Oh, [the_person.mc_title], I'm cumming again..."
                        $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = position_choice.slut_requirement, half_arousal = False, reset_arousal = False)
                        $ the_person.change_arousal((-builtins.max((the_person.arousal/(report_log.get("girl orgasms", 0)+2))+20, the_person.arousal - the_person.max_arousal - 1)))

                    $ condition.call_post_label(the_person, position_choice, object_choice, report_log)
                    if not private and not mc.recently_orgasmed:
                        call public_sex_post_round(the_person, position_choice, report_log) from _public_sex_post_round_01
                        if not _return:
                            $ finished = True

                    $ first_round = False
                    if not finished:    # when we switched to threesome finished is True
                        if mc.condom and mc.recently_orgasmed: # you orgasmed so you used your condom.
                            $ mc.condom = False
                        if mc.recently_orgasmed and not position_locked:
                            if perk_system.has_ability_perk("Serum: Energy Regeneration") and mc_serum_energy_regen.trait_tier >= 2 and mc.energy > 30:
                                $ mc.recently_orgasmed = False
                                $ allow_transitions = False
                                "Your personal Energy Serum allows you to continue [position_choice.verbing] [the_person.possessive_title]."
                        if position_choice.requires_hard and mc.recently_orgasmed:
                            "Your post-orgasm cock softens, stopping you from [position_choice.verbing] [the_person.possessive_title] for now."
                            $ position_choice = None
                            $ allow_transitions = False
                        elif position_choice.calculate_energy_cost(mc) > mc.energy:
                            if girl_in_charge:
                                "You're too exhausted to let [the_person.possessive_title] keep [position_choice.verbing] you."
                            else:
                                "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                            $ position_choice = None
                        elif position_choice.calculate_energy_cost(the_person) > the_person.energy:
                            #TODO: Add some differentiated dialogue depending on the position.
                            #TODO: Add "no energy" transitions where you keep fucking her anyways. (double TODO: Add a way of "breaking" her like this)
                            if not girl_in_charge:
                                the_person "I'm exhausted [the_person.mc_title], I can't keep this up..."
                            if position_choice.skill_tag == "Vaginal" and mc.energy > 50 and mc.location.has_object_with_trait(prone_bone.requires_location): # or position_choice.skill_tag == "Anal")
                                call prone_decision_label(the_girl = the_person, the_location = mc.location, the_object = object_choice, the_position = position_choice) from _prone_sex_takeover_01
                                if _return:
                                    $ the_object = _return
                                    $ position_choice = prone_bone
                                else:
                                    $ finished = True
                            elif position_choice.skill_tag == "Anal" and mc.energy > 50 and mc.location.has_object_with_trait(prone_anal.requires_location):
                                call prone_anal_decision_label(the_girl = the_person, the_location = mc.location, the_object = object_choice, the_position = position_choice) from _prone_anal_sex_takeover_01
                                if _return:
                                    $ the_object = _return
                                    $ position_choice = prone_anal
                                else:
                                    $ finished = True
                            else:
                                $ position_choice = None
                        elif not position_locked: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                            if self_strip and not stop_stripping:
                                call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event_bugfix

                            if girl_in_charge and position_choice is not None: # girls in charge and wants to spice things up
                                if the_person.effective_sluttiness() > position_choice.slut_cap and the_person.arousal_perc > position_choice.slut_cap:
                                    "[the_person.title] wants to spice things up."
                                    $ position_choice = None


        elif isinstance(round_choice, Position): #The only non-strings on the list are positions we are changing to
            call check_position_willingness(the_person, round_choice, ignore_taboo = ignore_taboo, skip_dialog = True) from _call_check_position_willingness_fuck_person_3
            $ allow_transitions = True
            if willing > 0:
                $ round_choice.redraw_scene(the_person)
                if not ignore_taboo and the_person.has_taboo(round_choice.associated_taboo):
                    # call mod taboo break
                    $ position_choice.call_transition_taboo_break(round_choice, the_person, mc.location, object_choice)
                    $ the_person.break_taboo(round_choice.associated_taboo)
                else:
                    $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                $ position_choice = round_choice
                $ the_person.current_position = position_choice

            else: #If she wasn't willing we keep going with what we were doing, so just loop around.
                if willing == -1: # angry reject ends interactions
                    $ finished = True
                    $ report_log["is_angry"] = True
                    $ position_choice = None
                    $ object_choice = None
                else:
                    the_person "Why don't we just continue what we were doing?"

        elif round_choice == "Strip":
            call strip_menu(the_person, position_choice, private, ignore_taboo) from _call_strip_menu_bugfix
            $ stop_stripping = False

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end

            # In 13% or 25% (if dominant) of the cases she takes control regardless of obedience, but only when she came less then 3 times
            # higher chance when she likes taking control lower when she doesn't
            if not position_locked and the_person.energy >= 30 and report_log.get("girl orgasms", 0) < 3 and ((renpy.random.randint(0, builtins.int(the_person.arousal)) + 50 + the_person.opinion.taking_control * 25 > the_person.obedience) or renpy.random.randint(0, (3 if the_person.is_dominant else 6)) == 3):
                $ the_person.change_obedience(-3)
                $ girl_in_charge = True
                $ finished = False
                $ stop_stripping = False    # allow her to strip again
                $ guy_orgasms_before_control = report_log.get("guy orgasms", 0)
                $ girl_orgasms_before_control = report_log.get("girl orgasms", 0)
                $ has_taken_control = True #After successful position and object choice she will let you know she wants to keep going.
                $ position_choice = None #She picks the position now, because she has her own list of possibilities

            elif not position_locked and the_person.energy >= 30 and (the_person.arousal_perc > 70) and (report_log.get("girl orgasms", 0) == 0) and report_log.get("beg finish", 0) == 0: #Within 30 of orgasming and she hasn't cum yet
                # They're close to their orgasm and beg you to help them finish.
                $ the_person.strip_outfit_to_max_sluttiness()
                $ the_person.call_dialogue("sex_beg_finish")
                menu:
                    "Give her what she wants":
                        $ the_person.change_obedience(2, 160)
                        $ report_log["beg finish"] = report_log.get("beg finish", 0) + 1
                        $ finished = False
                        $ position_locked = False

                    "Stop and leave":
                        $ the_person.call_dialogue("sex_end_early")

            elif report_log.get("beg finish", 0) > 0 and report_log.get("girl orgasms", 0) == 0: #You promised to make her cum but didn't
                $ the_person.change_stats(obedience = -5, happiness = -10, love = -3)
                the_person "But you promised..."
                #TODO: Add some personality specific dialogue for this

            else: # You end the encounter and nothing special happens.
                #TODO: Add some personality specific dialogue
                pass

        elif round_choice == "Girl Leave":
            $ finished = True

        elif round_choice == "Hypno_Orgasm":
            $ the_person.event_triggers_dict["hypno_orgasmed_recently"] = True
            $ the_word = the_person.event_triggers_dict.get("hypno_trigger_word","Cum").capitalize()
            mc.name "[the_word]."
            $ the_person.change_arousal(the_person.max_arousal)
            "[the_person.possessive_title!c] whimpers with pleasure as your training takes hold of her brain."
            call describe_girl_climax(the_person, position_choice, object_choice, private, report_log) from _call_describe_girl_fuck_person #Calls just the climax stuff without costing energy.

        elif round_choice == "hypnotize":
            call hypnotize_in_sex_label(the_person, position_choice) from _hypnosis_in_sex_01

        if start_position is None:
            $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the beginning of the loop we can set a mandatory choice for the first one.
        else:
            # we have received a new position from the old position
            $ round_choice = "Change"

    if mc.location.allow_walk_in and the_watcher is not None and not is_fixed_watcher:
        $ the_watcher.draw_person(position = "walking_away", display_transform = character_left_flipped)
        if the_watcher.is_stranger:
            "As you finish up with [the_person.possessive_title], you see the stranger quietly slipping of out the door."
        else:
            "As you finish up with [the_person.possessive_title], you see [the_watcher.fname] quietly slipping of out the door."
        $ the_watcher.change_location(the_watcher.get_destination() or the_watcher.home)
        $ the_person.draw_person()

    python:
        condition.run_rewards(the_person, report_log)

        clear_sex_modifiers(the_person)

        report_log["end arousal"] = the_person.arousal
        the_person.arousal = (the_person.arousal/(report_log.get("girl orgasms",0)+1)) # The more you make her cum the more satisfied she will be. At 0 orgasms her arousal does not move - you've just edged her!

        mc.condom = False
        mc.recently_orgasmed = False

    if affair_ask_after and private and not the_person.has_relation_with_mc and not the_person.has_job(prostitute_job) and the_person.has_significant_other and report_log.get("girl orgasms",0) >= 1:
        if not the_person.has_role([lifestyle_coach_role]): # don't exclude all unique characters (boss wife / emily mom -> affair should be possible)
            if the_person.relationship in relationship_stats and the_person.love >= relationship_stats[the_person.relationship] - 10 - (the_person.opinion.cheating_on_men * 5):
                if the_person.effective_sluttiness() >= 30 - (the_person.opinion.cheating_on_men * 5):
                    call affair_check(the_person, report_log) from _call_affair_check_fuck_person

    python:
        # Only activate sexting when we have her number
        if report_log.get("girl orgasms",0) >= 2 and time_of_day < 3 and the_person in mc.phone.get_person_list():
            attaboy_target = the_person.identifier
            attaboy_record = report_log.copy()
            attaboy_day = day

        # sex is a good workout and increases max_energy
        the_person.change_max_energy(report_log.get("girl orgasms",0), add_to_log = False)
        mc.change_max_energy(report_log.get("guy orgasms", 0), add_to_log = False)

        the_person.update_person_sex_record(report_log)
        the_person.position_choice = None
        mc.recently_orgasmed = False
        position_choice = None
        object_choice = None
        the_watcher = None
        watch_list = None

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label check_position_willingness(the_person, the_position, ignore_taboo = False, skip_dialog = False, skip_condom_ask = False): #Returns if hte person is willing to do this position or not, and charges the appropriate happiness hit if they needed obedience to be willing.
    $ willing = 1

    $ the_taboo = the_position.associated_taboo
    if ignore_taboo:
        $ the_taboo = None

    if the_person == kaya:  # she never asks for a condom
        $ skip_condom_ask = True

    $ final_slut_requirement, final_slut_cap = the_position.calculate_position_requirements(the_person, ignore_taboo)
    $ hates_position = len([the_person.discover_opinion(x) for x in the_position.opinion_tags if the_person.opinion(x) == -2]) != 0

    if ignore_taboo:
        # ignore taboo, also ignores willingness (we got here in a special way)
        # so we also go into the position (no escape because she hates is)
        pass
    elif not hates_position and the_person.effective_sluttiness(the_taboo) >= final_slut_requirement:
        if not (skip_dialog or the_person.has_taboo(the_taboo)):
            $ the_person.call_dialogue("sex_accept", the_position)

    elif not hates_position and the_person.effective_sluttiness(the_taboo) + (the_person.obedience-100) >= final_slut_requirement:
        "[the_person.possessive_title!c] doesn't seem enthusiastic, but a little forceful encouragement would probably convince her."
        menu:
            "Order her":
                mc.name "[the_person.title], this is going to happen."
                python:
                    happiness_drop = the_person.effective_sluttiness(the_taboo) - final_slut_requirement #Our initial conditions mean this is a negative number
                    the_person.change_arousal(the_person.opinion.being_submissive*2)
                    the_person.discover_opinion("being submissive")
                    if not the_person.is_submissive:
                        the_person.change_happiness(int(happiness_drop / (3 + the_person.opinion.being_submissive)))

                if not the_person.has_taboo(the_taboo):
                    $ the_person.call_dialogue("sex_obedience_accept")

                $ report_log["used_obedience"] = True
                $ willing = 2
            "Try something else":
                mc.name "Let's try something else that you might be more comfortable with."
                $ willing = 0

    elif not hates_position and the_person.effective_sluttiness(the_taboo) > final_slut_requirement * .6:
        # She's not willing to do it, but gives you a soft reject.
        $ the_person.call_dialogue("sex_gentle_reject")
        $ willing = 0

    elif hates_position and the_person.effective_sluttiness(the_taboo) > final_slut_requirement * .6:
        #She hates the position but isn't so mad she ends sex outright.
        $ willing = -2

    else:
        # You're nowhere close to the required sluttiness or hates position, lose some love for even trying and end interaction
        python:
            ran_num = the_person.effective_sluttiness(the_taboo) - final_slut_requirement
            ran_num = builtins.abs(builtins.int(ran_num/5.0))
            the_person.change_love(-ran_num)
            willing = -1

        $ the_person.call_dialogue("sex_angry_reject")

    if willing == 1 and not skip_condom_ask:
        call should_ask_for_condom(the_person, the_position) from _call_should_ask_for_condom_check_position_willingness

    if willing == 1 and (the_position.skill_tag == "Vaginal" or the_position.skill_tag == "Anal" or the_position.name == "Dildo Fuck") and not the_person.vagina_visible:
        # make sure we move skirts out of the way when rendering
        python:
            for the_clothing in (x for x in the_person.outfit.get_lower_ordered() if not (x.underwear or x.half_off)):
                renpy.say(None, f"You move her {the_clothing.display_name} out of the way.")
                the_person.outfit.half_off_clothing(the_clothing)
                the_person.draw_person()

    return willing

label should_ask_for_condom(the_person, the_position):
    if the_position.skill_tag in ("Vaginal", "Anal") and not mc.condom: #We might need a condom, which means she might say no. TODO: Add an option to pull _off_ a condom while having sex.
        if not ask_for_condom:
            $ ask_for_condom = True
            # if still has taboo, always ask
            if (persistent.always_ask_condom or the_person.effective_sluttiness("condomless_sex") < the_person.get_no_condom_threshold() + 50
                    or the_person.has_taboo("condomless_sex") or the_person.has_job(prostitute_job)):
                # she is not slutty enough and we have the condom dialog
                call condom_ask(the_person, the_position.skill_tag) from _call_condom_ask_check_position_willingness
                if not _return:
                    $ ask_for_condom = False # we don't have vag/anal sex so if player tries again, she will ask for condom again
                    $ willing = 0
                else:
                    $ use_condom = mc.condom
            else:
                # she is so slutty we are going to fuck her raw (we don't care anymore)
                if the_position.skill_tag == "Vaginal":
                    mc.name "I'm going to fuck your little pussy raw."
                else:
                    mc.name "I'm going to fuck your slutty asshole raw."
        elif use_condom:  # you already determined you are going to fuck her with condom
            call put_on_next_condom_routine(the_person, the_position) from _call_put_on_next_condom_routine_2
    return

label condom_ask(the_person, skill_tag = "Vaginal"):
    $ condom_threshold = the_person.get_no_condom_threshold()

    if the_person == kaya and persistent.pregnancy_pref != 0:
        "As you look at [the_person.possessive_title], you remember she doesn't want you to use condoms. Should you put one on anyway?"
        menu:
            "Put on a condom":
                mc.name "One sec, let me just get a condom on..."
                the_person "Really? You know I'm not okay with that."
                mc.name "I know but..."
                the_person "I'm sorry. We do it bare, or not at all."
                menu:
                    "Fuck her raw":
                        $ the_person.break_taboo("condomless_sex")
                        return True
                    "Refuse and do something else":
                        "[the_person.possessive_title!c] seems like she's made up her mind, and you doubt you would be able to change it."
                        mc.name "We can't risk it [the_person.title]. We'll have to do something else."
                        return False
            "Don't":
                $ the_person.break_taboo("condomless_sex")
                return True

    if the_person.has_cum_fetish or the_person.has_breeding_fetish:
        "[the_person.possessive_title!c] eyes your cock greedily. You could put a condom on if you wanted."
        menu:
            "Put on a condom":
                "You pull a condom out of your wallet and tear open the package."
                "[the_person.title] takes a hold of the condom in your hand."
                if skill_tag == "Vaginal":
                    if the_person.knows_pregnant:
                        the_person "I'm already pregnant. It's a bit late for that, isn't it?"
                    elif the_person.on_birth_control:
                        the_person "I'm on the pill so we really don't need one of those." # even if she is or not - she'll say it
                        $ the_person.update_birth_control_knowledge()
                    else:
                        the_person "You don't really need that thing, do you?"
                the_person "I want your cum inside me and this is going to stop that."
                menu:
                    "Insist on condom":
                        mc.name "I think a condom is a good idea."
                        if the_person.is_dominant:
                            the_person "OK. Let me put this another way."
                            "[the_person.title] grabs the condom and throws it off to the side."
                            if skill_tag == "Vaginal":
                                the_person "Either we fuck and you come inside me or we don't fuck at all."
                            else:
                                the_person "Either you fuck my ass raw or we don't fuck at all."
                            menu:
                                "Fuck her raw":
                                    mc.name "Fine."
                                    call fuck_without_condom_taboo_break_response(the_person, skill_tag) from _call_fuck_without_condom_taboo_break_response_1
                                "Don't":
                                    mc.name "If it's that important to you let's just do something else."
                                    return False
                        else:
                            the_person "OK."
                            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_8
                    "Fuck her raw":
                        call fuck_without_condom_taboo_break_response(the_person, skill_tag) from _call_fuck_without_condom_taboo_break_response_2

            "Don't":
                pass

    elif the_person.has_job(prostitute_job):
        $ ran_num = (the_person.opinion.cheating_on_men * -5) + (the_person.opinion.bareback_sex * -5)
        if the_person.love < 50 + ran_num and the_person.obedience < 180 + (ran_num * 2):
            the_person "Are you remembering that I'm a 'working girl'?"
            the_person "That means 'safety first'—always."
            the_person "We're going to have to use one of these."
            "She gets out a condom."
            if skill_tag == "Vaginal":
                if the_person.knows_pregnant:
                    the_person "Me being pregnant doesn't change that."
            the_person "But don't you worry."
            the_person "You're going to feel {i}every{/i} thing we do."
            menu:
                "Put on condom":
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_1

                "Refuse and do something else":
                    "[the_person.title] doesn't seem like she's going to change her mind."
                    mc.name "If it's that important to you let's just do something else."
                    return False

        elif the_person.vaginal_creampie_count < 7 - the_person.opinion.cheating_on_men - the_person.opinion.bareback_sex:
            the_person "Normally we would have to use one of these."
            "She gets out a condom."
            if skill_tag == "Vaginal":
                if the_person.knows_pregnant:
                    the_person "Would you like to fuck this pregnant whore without one?"
                else:
                    the_person "But maybe not. What do you think?"
            else:
                the_person "I know, I can't get pregnant, when you fuck my ass, should we use one?"
            menu:
                "Condom":
                    mc.name "Let's cover this bad boy up."
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_2

                "No condom":
                    mc.name "I like fucking you like nature intended."
                    call prostitute_agree_no_condom_taboo_break_response(the_person) from _call_prostitute_agree_no_condom_taboo_break_response_1

                "[the_person.title] smiles at you."

        else:
            the_person "I know you like to do me bare."
            if skill_tag == "Vaginal":
                if the_person.knows_pregnant:
                    the_person "Would you like to shower my baby with your cum?"
                else:
                    the_person "So maybe no condom today?"
            else:
                the_person "So, do you want to fuck my little asshole without one?"
            menu:
                "Agree no condom":
                    call prostitute_agree_no_condom_taboo_break_response(the_person) from _call_prostitute_agree_no_condom_taboo_break_response_2

                    "[the_person.title] smiles at you."
                "Use condom":
                    mc.name "I still think that it's a good idea."
                    the_person "Alright."

                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_3

    elif the_person.effective_sluttiness() < condom_threshold:
        # they demand you put on a condom.
        #TODO: Make this dialogue personality based
        if the_person.knows_pregnant and skill_tag == "Vaginal":
            if the_person.opinion.bareback_sex < 0:
                the_person "You can't get me {i}more{/i} pregnant, but I really don't like bare sex."
            else:
                the_person "Although I'm pregnant, I would like you to wear a condom anyway."
        elif skill_tag == "Anal":
            the_person "Although it's the backdoor, I still need you to wear a condom."
        else:
            $ the_person.call_dialogue("condom_demand")

        menu:
            "Put on a condom":
                call put_on_condom_routine(the_person) from _call_put_on_condom_routine_4
                if the_person.opinion.bareback_sex < 0 :
                    the_person "There we go, a nice big rubbery cock."

            "Refuse and do something else":
                "[the_person.title] doesn't seem like she's going to change her mind."
                mc.name "If it's that important to you let's just do something else."
                return False

            "Fuck her raw anyways" if the_person.obedience >= 150:
                if skill_tag == "Anal":
                    mc.name "No way, this ass is getting fucked raw."
                else:
                    mc.name "No way, this pussy is getting fucked raw."
                call fuck_without_condom_taboo_break_response(the_person, skill_tag) from _call_fuck_without_condom_taboo_break_response_7

            "Fuck her raw anyways\n{menu_red}Requires: 150 Obedience{/menu_red} (disabled)" if the_person.obedience < 150:
                pass

    elif the_person.opinion.bareback_sex < 0 or the_person.effective_sluttiness("condomless_sex") < condom_threshold + 20 or the_person.has_taboo("condomless_sex"):
        # They suggest you put on a condom.
        if the_person.knows_pregnant and skill_tag == "Vaginal":
            if the_person.opinion.bareback_sex < 0:
                the_person "You can't get me {i}more{/i} pregnant, but I don't like bare sex. I think that you should put on a condom."
            else:
                the_person "There's not much point in a condom now that I'm pregnant."
        elif skill_tag == "Anal":
            the_person "Could you put on a condom? I don't want to have a mess when you start pumping my ass."
        else:
            $ the_person.call_dialogue("condom_ask")
            $ skip_taboo_break = True

        menu:
            "Put on a condom":
                if not skip_taboo_break:
                    if the_person.knows_pregnant:
                        mc.name "Not this time slut, we are using a condom."
                    elif the_person.opinion.bareback_sex < 0 or the_person.effective_sluttiness("condomless_sex") < condom_threshold + 20 or the_person.has_taboo("condomless_sex"):
                        mc.name "That's okay, I'm happy to oblige."
                    elif the_person.on_birth_control:
                        mc.name "A condom might be a good idea."
                    else:
                        mc.name "I think you're right. One second."
                call put_on_condom_routine(the_person) from _call_put_on_condom_routine_5

            "Fuck her raw":
                if the_person.knows_pregnant:
                    if skill_tag == "Vaginal":
                        mc.name "I'm going to fuck that pregnant pussy raw."
                    else:
                        mc.name "I'm going to fuck that slutty ass raw."
                elif the_person.wants_creampie:
                    if skill_tag == "Vaginal":
                        mc.name "I'm going to fill up that little cunt of yours."
                    else:
                        mc.name "I'm going to fill up that cute ass of yours."
                else:
                    mc.name "No way. I want to feel you wrapped around me."
                call fuck_without_condom_taboo_break_response(the_person, skill_tag, skip_taboo_break = skip_taboo_break) from _call_fuck_without_condom_taboo_break_response_3

    else: #Slutty enough that she doesn't even care about a condom.
        if the_person.is_dominant and the_person.wants_creampie: # likes it bare and is not a pushover
            menu:
                "Put on a condom":
                    mc.name "One sec, let me just get a condom on..."
                    if skill_tag == "Anal":
                        the_person "No way, I want you to fuck my slutty ass raw!"
                    else:
                        $ the_person.call_dialogue("condom_bareback_demand") #TODO: Write this. Girl demands you fuck her bareback, or she'll force you to do something else. High Obedience will let you ignore her and wear one anyways.
                    menu:
                        "Fuck her raw":
                            mc.name "Alright, as long as you know what you're getting into..."
                            "You abandon your plans to put on a condom and get ready to take [the_person.possessive_title] raw."

                        "Refuse and do something else":
                            "[the_person.possessive_title!c] seems like she's made up her cock-hungry mind, and you doubt you would be able to change it."
                            mc.name "We can't risk it [the_person.title]. We'll have to do something else."
                            return False

                        "Put on a condom anyways\n{menu_red}Requires: 140 Obedience{/menu_red} (disabled)" if the_person.obedience < 140:
                            pass

                        "Put on a condom anyways" if the_person.obedience >= 140:
                            mc.name "I can't risk it [the_person.title], no matter how desperate you are for raw cock."
                            "You pull out a condom from your wallet, tear open the package, and start to unroll it down your dick."
                            mc.name "So you have a choice. You can have my cock inside you like this, or you can have no cock at all."
                            "She whimpers like a sad puppy, but you know there's only one choice she would ever make."
                            $ mc.condom = True

                "Fuck her raw":
                    call fuck_without_condom_taboo_break_response(the_person, skill_tag, condom_promise = False) from _call_fuck_without_condom_taboo_break_response_5

        else:
            if skill_tag == "Anal":
                the_person "Well... ah... could you fuck my little ass raw?"
            else:
                $ the_person.call_dialogue("condom_bareback_ask")
                $ skip_taboo_break = True
            menu:
                "Put on condom":
                    mc.name "I think a condom is a good idea."
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_7

                "Fuck her raw":
                    mc.name "No arguments here."
                    call fuck_without_condom_taboo_break_response(the_person, skill_tag, condom_promise = False, skip_taboo_break = skip_taboo_break) from _call_fuck_without_condom_taboo_break_response_6

    if not mc.condom:
        $ the_person.break_taboo("condomless_sex")

    return True

label condomless_promise(the_person):
    menu:
        "Promise to pull out":
            mc.name "I'll pull out, don't worry."
            "[the_person.possessive_title!c] seems reassured by your promise."
            #TODO: Add negative stats if you promise and cum inside her anyways

        "Don't promise anything":
            mc.name "I'll do my best. I'm not sure I'll be able to resist."
            if not the_person.on_birth_control:
                the_person "You're going to get me pregnant if you aren't careful!"
            #TODO: Middle ground between warning her it's happening and lying to her.

        "Promise to cum inside":
            mc.name "Oh I'm not pulling out. I'm planning on dumping my load inside your tight little pussy."
            if the_person.wants_creampie:
                the_person "Oh god..."
            elif not the_person.on_birth_control:
                the_person "Fuck [the_person.mc_title], you're going to get me pregnant like that!"
                "She squirms uncomfortably, but this doesn't seem to be a deal-breaker for her."
            else:
                the_person "Oh god, of course you are..."
            #TODO: Moderate stat penalties, but less than lying
    return

label prostitute_agree_no_condom_taboo_break_response(the_person):
    if the_person.has_taboo("condomless_sex"):
        $ the_person.call_dialogue("condomless_sex_taboo_break")
    else:
        if the_person.opinion.bareback_sex > 0:
            the_person "Good choice. I hate those things but I usually have to use them."
        else:
            the_person "Normally I wouldn't do this, I don't like it, but for you, I will make an exception."

        if the_person.opinion.creampies < 0 or the_person.opinion.anal_creampies < 0 or not the_person.on_birth_control:
            the_person "But no cumming inside. I don't like to leak cum all day, agreed?"

        if not the_person.on_birth_control:
            the_person "I'm not using any contraception at the moment. So you have to promise not to cum inside me."
            call condomless_promise(the_person) from _call_condomless_promise_prostitute_agree_no_condom
    return

label fuck_without_condom_taboo_break_response(the_person, skill_tag == "Vaginal", condom_promise = True, skip_taboo_break = False):
    if the_person.has_taboo("condomless_sex") and skill_tag == "Vaginal" and not skip_taboo_break:
        $ the_person.call_dialogue("condomless_sex_taboo_break")
    else:
        # TODO: make this a personality based response.
        if the_person.opinion.bareback_sex > 0:
            the_person "I agree, nothing beats skin on skin."
        elif skill_tag == "Vaginal" and condom_promise:
            if the_person.on_birth_control:
                the_person "Okay. I'm on birth control, so it should be fine."
                $ the_person.update_birth_control_knowledge()
            elif not the_person.knows_pregnant:
                the_person "I'm not on birth control [the_person.mc_title], promise you won't cum inside me."
                call condomless_promise(the_person) from _call_condomless_promise_fuck_without_condom
        elif skill_tag == "Vaginal" and not condom_promise:
            if the_person.opinion.creampies > 0:
                the_person "I love it when you fill me up with your spunk."
        elif skill_tag == "Anal" and the_person.opinion.anal_creampies > 0:
            the_person "Just pump my ass full with that hot spunk of yours."
    return

label put_on_condom_routine(the_person):
    if the_person.oral_sex_skill > 3 and the_person.opinion.giving_blowjobs > 1: #Knows what she's doing
        "[the_person.title] gets a condom out of their own bag and opens it."
        "She carefully puts it in her mouth, behind her teeth."
        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
        "She starts bobbing up and down on your cock."
        "As she goes down on your dick she unrolls the condom onto it with her mouth."
        if the_person.is_submissive:
            $ play_gag_sound()
            "She keeps going to the very base of your cock, deep-throating you and entirely covering your cock."
        else:
            "Once she has rolled on about two thirds of the condom she brings her head back up and rolls the rest on with her hand."
    elif the_person.opinion.giving_handjobs > 0:
        "You pull out a condom from your wallet and rip open the package."
        the_person "Let me help with that."
        "[the_person.title] takes the condom out of your hand."
        "She holds it at the top of your cock with one hand as she strokes farther and farther with the other hand, rolling the condom down onto it."
    elif the_person.opinion.bareback_sex < 0: # condoms are good
        if the_person.is_dominant:
            the_person "Good choice."
            "You roll the condom onto your cock as [the_person.title] watches eagerly."
        else:
            "[the_person.title] watches eagerly while you roll the condom on."
    elif the_person.opinion.bareback_sex > 0:
        "You pull out a condom from your wallet and rip open the package. [the_person.title] watches disappointingly while you slide it on."
    else:
        "You pull out a condom from your wallet and rip open the package. [the_person.title] watches while you slide it on."

    $ mc.condom = True
    return

label put_on_next_condom_routine(the_person, the_position):
    if the_person.oral_sex_skill > 3 and the_person.opinion.giving_blowjobs > 1: #Knows what she's doing
        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
        "[the_person.title] quickly puts another condom between her lips and rolls down the condom while swallowing your member."
        if the_person.is_submissive:
            $ play_gag_sound()
            "She keeps going to the very base of your cock, deep-throating you and entirely covering your cock."
        else:
            "Once she has rolled on about two thirds of the condom she brings her head back up and rolls the rest on with her hand."
        "When she's satisfied, she gets back into position."
        $ the_position.redraw_scene(the_person)
    elif the_person.opinion.giving_handjobs > 0:
        $ the_person.draw_person()
        the_person "Here, let me put another condom on."
        "With her nimble fingers [the_person.possessive_title] slides another condom around your hardening member."
        "When she's finished, she gets back into position."
        $ the_position.redraw_scene(the_person)
    elif the_person.opinion.bareback_sex < 0: # condoms are good
        if the_person.is_dominant:
            the_person "Quick, put on another condom!"
            "You comply and quickly slip over another condom."
        else:
            "[the_person.title] watches eagerly while you roll on another condom."
    elif the_person.opinion.bareback_sex > 0:
        "You pull out another condom, [the_person.title] watches disappointingly while you slide it on."
    else:
        "You pull out another condom, [the_person.title] watches while you slide it on."

    $ mc.condom = True
    return

label post_orgasm_condom_routine(the_person, the_position):
    $ the_person.increase_fill_up_condom()
    if the_person.has_cum_fetish:
        if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
            $ the_person.discover_opinion("drinking cum")
            if renpy.random.randint(0, 1) == 1:
                "[the_person.possessive_title!c] quickly grabs your cock. She hastily pulls your condom off, careful not to spill a drop."
                the_person "I'm not letting a drop of this delicious cum go to waste!"
            else:
                "[the_person.possessive_title!c] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                the_person "It would be a shame to waste all of this, right?"

            "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
            $ the_person.change_slut(the_person.opinion.drinking_cum, 70)
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans as she pours your cum into her mouth."
            $ the_person.cum_in_mouth()
            $ the_position.redraw_scene(the_person)
            $ play_swallow_sound()
            if renpy.random.randint(0, 3) == 1:
                "She shudders at the sensation. It is apparent to you, if it was not before, that [the_person.possessive_title] is literally addicted to your cum."
            else:
                "Her body trembles as her fetish is fulfilled."
        else:
            $ the_person.discover_opinion("cum facials")
            "[the_person.possessive_title!c] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
            the_person "It would be a shame to waste all of this, right?"
            $ the_person.cum_on_face()
            $ the_position.redraw_scene(the_person)
            "She smiles and tips the contents of the condom out onto one of her hands. She tosses the condom aside and rubs her palms together."
            "She takes a deep breath and closes her eyes. She reaches to her cheeks and starts to smear your cum over her face."
            $ play_moan_sound()
            the_person "Mmmmm. So good."
    elif the_person.opinion.drinking_cum > 1 and the_person.effective_sluttiness() > 50:
        "[the_person.possessive_title!c] gets on her knees and reaches for your cock."
        $ the_person.draw_person(position = "kneeling1")
        $ the_person.discover_opinion("drinking cum")
        "With delicate fingers she slides the condom off of you."
        the_person "It would be a shame to waste all of this, right?"
        "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
        $ play_swallow_sound()
        the_person "Mmmm, delicious."
        $ the_person.change_slut(the_person.opinion.drinking_cum, 70)
    else:
        "[the_person.possessive_title!c] reaches for your cock, removes the condom, and ties the end in a knot."
        the_person "Look at all that cum. Well done."
    return

label watcher_check(the_person, the_position, the_object, report_log, fixed_watcher = None): # Check to see if anyone is around to comment on the characters having sex.
    if not fixed_watcher:
        $ the_watcher = cheating_check_get_watcher(the_person, the_position)
    else:
        $ the_watcher = fixed_watcher

    if the_watcher:
        # you only get one chance for starting a threesome per public sex action (avoid spamming threesome question)
        # threesome has no watcher loop, so all watching stops when threesome has started.
        # TODO: add watchers to threesome core
        if not ask_for_threesome and willing_to_threesome(the_person, the_watcher) and not the_person.has_role(caged_role):
            $ the_watcher.draw_person(display_transform = character_left_flipped)
            the_watcher "Oh my god, that looks amazing..."
            if can_join_threesome(the_watcher, the_person, the_position.position_tag):
                the_watcher "Can I... can I join you? I want some too!"
                $ ask_for_threesome = True
                menu:
                    "Let her join":
                        the_watcher "Yes! Thank you [the_watcher.mc_title]!"
                        $ scene_manager = Scene()
                        $ scene_manager.add_actor(the_person, the_person.outfit, position = the_position.position_tag)
                        $ scene_manager.add_actor(the_watcher, the_watcher.outfit, display_transform = character_center_flipped)
                        if not the_watcher.vagina_visible:
                            "You both watch as [the_watcher.possessive_title] takes off some clothes."
                            $ scene_manager.strip_to_vagina(the_watcher)
                        call join_threesome(the_person, the_watcher, the_position.position_tag, private = mc.location.person_count <= 2, report_log = report_log) from _call_join_threesome_watcher_check
                        $ scene_manager.update_actor(the_watcher, position = "default", display_transform = character_left_flipped)
                        the_watcher "Thank you both for letting me join, I had a great time."
                        $ scene_manager.apply_outfit(the_watcher)
                        $ scene_manager.update_actor(the_watcher, position = "walking_away")
                        $ scene_manager.update_actor(the_person, position = "default", display_transform = character_right)
                        if isinstance(the_watcher, Person): # extra check if she still exists (prevent exception when this was cleared inadvertently)
                            "After [the_watcher.possessive_title] has rearranged her clothes, she goes back to what she was doing."
                            $ scene_manager.remove_actor(the_watcher)
                        $ report_log = _return
                        $ the_watcher = None  # explicitly clear watcher to prevent slipping out of door
                        $ finished = True
                        return
                    "Not this time":
                        the_person "Aww, okay. Maybe next time..."
                        $ the_person.change_obedience(3, 160)

        if town_relationships.is_family(the_watcher, the_person):
            call relationship_sex_watch(the_person, the_watcher, town_relationships.get_relationship_type(the_watcher, the_person).lower(), the_position) from _call_relationship_sex_watch
            $ the_position.redraw_scene(the_person)
            call relationship_being_watched(the_person, the_watcher, town_relationships.get_relationship_type(the_person, the_watcher).lower(), the_position) from _call_relationship_being_watched
            $ the_person.change_arousal(the_person.opinion.public_sex)
            $ the_person.discover_opinion("public sex")
        else:
            # NOTE: the dialogue here often draws the person talking with various emotions or positions, so we redraw the scene after we call them.
            $ the_watcher.call_dialogue("sex_watch", the_sex_person = the_person, the_position = the_position) #Get the watcher's reaction to the people having sex. This might include dialogue calls from other personalities as well!

            if not _return and renpy.random.randint(0, 1) == 1:
                $ the_watcher.draw_person(position = "walking_away", display_transform = character_left_flipped)
                "It seems [the_watcher.title] had enough and walks away."
                python:
                    if the_watcher.is_at(mc.location):
                        # she's in the same room, move her to another location to prevent 'rewatching'
                        if the_watcher.is_employee and the_watcher.is_at_office:
                            the_watcher.change_location(lobby)
                        elif the_watcher.is_home:
                            the_watcher.change_location(downtown)
                        else:
                            the_watcher.change_location(the_watcher.home)
                    the_watcher.clear_situational_slut("public sex watcher")
                    the_watcher.clear_situational_slut("at stripclub")
                    the_watcher = None
                    the_position.redraw_scene(the_person)
                return

            python:
                the_position.redraw_scene(the_person)
                the_person.call_dialogue("being_watched", the_watcher = the_watcher, the_position = the_position) #Call her response to the person watching her.
                the_person.change_arousal(the_person.opinion.public_sex)


        python:
            if watch_list is None:
                watch_list = []
            if not the_watcher.identifier in watch_list:
                watch_list.append(the_watcher.identifier)
            the_person.discover_opinion("public sex")
            the_watcher.clear_situational_slut("public sex watcher")
            the_watcher.clear_situational_slut("at stripclub")
    return

label walk_in_watcher_check(the_person, the_position, the_object, report_log):
    # special case (no walk in)
    if the_person == camila and mc.is_at(downtown_bar_bathroom):
        return

    # not a valid location for walk in
    if not mc.location.allow_walk_in:
        return

    if isinstance(the_watcher, Person):
        call watcher_check(the_person, the_position, the_object, report_log, fixed_watcher = the_watcher) from _call_watcher_check_walk_in
    elif renpy.random.randint(0, 100) < 3:
        $ the_watcher = get_random_from_list([person for x in mc.current_location_hub for person in x.people if person.is_available and person != the_person])
        if the_watcher:
            $ the_watcher.change_location(mc.location)
            $ the_watcher.draw_person(display_transform = character_left_flipped)

            if the_person.is_family and the_watcher.is_family and not willing_to_threesome(the_person, the_watcher):
                the_watcher "What the fuck [the_person.fname], you and [the_watcher.mc_title]."
                "You and [the_person.possessive_title] quickly stop what you were doing."
                mc.name "Hey [the_watcher.title], I'm sorry, things just got a little out of hand."
                the_watcher "I better hope so, you two better make sure this never happens again, now let's get out of here you two."
                "This was not exactly how you imagined it, but it could have been worse, you all leave, trying to forget what just happened."
                $ finished = True
                $ report_log["is_angry"] = True
                return

            if the_watcher.sluttiness < the_position.slut_requirement:
                the_watcher "Oh my god, I'm so sorry, I didn't mean to disturb you."
                "[the_watcher.possessive_title!c] just walked in while you were [the_position.verbing] [the_person.possessive_title]."
                $ the_watcher.draw_person(position = "walking_away", display_transform = character_left_flipped)
                "[the_watcher.possessive_title!c] quickly turns around and walks out."
                $ the_watcher.change_location(the_watcher.get_destination() or the_person.home)
                if town_relationships.is_family(the_watcher, the_person):
                    $ the_relation = town_relationships.get_relationship_type(the_watcher, the_person).lower()
                    "Luckily, she walked out so fast, she didn't notice you're fooling around with her [the_relation]."
                $ the_position.redraw_scene(the_person)
                $ the_watcher = None    # reset to no watcher
            else:
                the_watcher "Hello [the_watcher.mc_title], I see you are having fun with [the_person.fname]."
                "[the_watcher.possessive_title!c] just walked in while you were [the_position.verbing] [the_person.possessive_title]."
                "Instead of walking away, she is watching you and [the_person.possessive_title] intently, while blocking the door with her body."
                if town_relationships.is_family(the_watcher, the_person):
                    call relationship_sex_watch(the_person, the_watcher, town_relationships.get_relationship_type(the_watcher, the_person).lower(), the_position) from _call_relationship_sex_watch_walk_in
                    $ the_position.redraw_scene(the_person)
                    call relationship_being_watched(the_person, the_watcher, town_relationships.get_relationship_type(the_person, the_watcher).lower(), the_position) from _call_relationship_being_watched_walk_in
                else:
                    $ the_watcher.call_dialogue("sex_watch", the_sex_person = the_person, the_position = the_position) #Get the watcher's reaction to the people having sex. This might include dialogue calls from other personalities as well!
                    $ the_position.redraw_scene(the_person)
                    $ the_person.call_dialogue("being_watched", the_watcher = the_watcher, the_position = the_position) #Call her response to the person watching her.
    return

label relationship_sex_watch(the_person, the_watcher, the_relation, the_position):
    $ title = the_watcher.title if not the_watcher.is_stranger else "The stranger"
    if the_watcher.sluttiness < the_position.slut_requirement - 20:
        $ the_watcher.draw_person(emotion = "angry", display_transform = character_left_flipped)
        if the_person.has_significant_other:
            the_watcher "Oh my god [the_relation], I can't believe you're doing that here in front of everyone. What would your [the_person.so_title] think of this?"
        else:
            the_watcher "Oh my god [the_relation], I can't believe you're doing that here in front of everyone. Don't either of you have any decency?"
        $ the_watcher.change_stats(obedience = -2, happiness = -1)
        "[title] looks away while you and her [the_relation] [the_position.verb]."
        return False

    if the_watcher.sluttiness < the_position.slut_requirement - 10:
        $ the_watcher.draw_person(emotion = "sad", display_transform = character_left_flipped)
        $ the_watcher.change_happiness(-1)
        "[title] shakes her head and tries to avoid watching you and her [the_relation] [the_position.verb]."
        return False

    if the_watcher.sluttiness < the_position.slut_requirement:
        $ the_watcher.draw_person(display_transform = character_left_flipped)
        $ the_watcher.change_slut(1, 20)
        "[title] tries to avert her gaze, but keeps glancing over while you and her [the_relation] [the_position.verb]."
        return True

    if the_watcher.sluttiness > the_position.slut_requirement and the_watcher.sluttiness < the_position.slut_cap:
        $ the_watcher.draw_person(display_transform = character_left_flipped)
        if the_person.has_significant_other:
            the_watcher "Oh my... I wonder what your [the_person.so_title] would say..."
        else:
            the_watcher "Oh my..."
        $ the_watcher.change_slut(1, 30)
        "[title] continues watching you and her [the_relation] [the_position.verb]."
        return True

    $ the_watcher.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_watcher "Glad to see you two are having a good time. [the_watcher.mc_title], careful you aren't too rough with my [the_relation]."
    else:
        call watcher_position_comment(the_watcher, the_person, the_position) from _call_watcher_position_comment_relationship_sex_watch
    "[title] watches quietly while you and her [the_relation] [the_position.verb]."
    return True

label relationship_being_watched(the_person, the_watcher, the_relation, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by her [the_relation] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Don't listen to my [the_relation], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by her [the_relation] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by her [the_relation] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with her [the_relation] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with her [the_relation] around."

    return

label girl_orgasm_watch(the_person):
    if not the_watcher: # use global variable
        return

    $ the_watcher.draw_person(display_transform = character_left_flipped)
    $ the_watcher.change_stats(slut = 1, max_slut = 40, arousal = 10)
    $ ran_num = renpy.random.randint(0, 3)
    $ the_choice = renpy.random.choice(["slut", "bitch", "whore", "cumdump"])
    if ran_num == 0:
        the_watcher "Oh yes [the_watcher.mc_title], make that little [the_choice] cum hard!"
    elif ran_num == 1:
        the_watcher "That looks so hot [the_person.fname], can I be his little [the_choice] next time?"
    elif ran_num == 2:
        the_watcher "Yes, [the_watcher.mc_title] make [the_person.fname] cum harder!"
    else:
        the_watcher "Yes, cum for him [the_person.fname], you little [the_choice]!"
    "[the_watcher.fname] is getting aroused from watching [the_person.fname] have an orgasm."
    return

label strip_menu(the_person, the_position, is_private = True, ignore_taboo = False): #TODO: Add an arousal cost to stripping a girl down, but give an arousal boost if she likes getting naked.
    python:
        the_verbing = the_position.verbing if isinstance(the_position, Position) else "wooing"
        the_position_tag = the_position.position_tag if isinstance(the_position, Position) else the_person.idle_pose

    call screen main_choice_display(build_menu_items(build_sex_mechanic_strip_menu(the_person)))
    $ choice_return = _return

    if not choice_return == "Go Back":
        $ strip_choice = choice_return[0] #Gets what the actual potentially stripped item was.
        $ strip_type = choice_return[1] #Gets if this was a half-off or a full strip

        $ test_outfit = the_person.outfit.get_copy()
        if strip_type == "Half":
            $ test_outfit.half_off_clothing(strip_choice)
        else:
            $ test_outfit.remove_clothing(strip_choice)

        $ underwear_revealed = False
        $ boobs_revealed = False
        $ ass_revealed = False
        if (the_person.outfit.bra_covered and the_person.outfit.panties_covered) and not (test_outfit.bra_covered and test_outfit.panties_covered):
            $ underwear_revealed = True
        if (not the_person.tits_visible) and test_outfit.tits_visible:
            $ boobs_revealed = True
        if (not the_person.vagina_visible) and test_outfit.vagina_visible:
            $ ass_revealed = True

        $ willing_to_strip = False
        $ ordered_to_strip = False #TODO: Use this for some dialogue stuff later

        $ strip_requirement = 0
        if ass_revealed: #Doubles for pussy revealed
            $ strip_requirement = 40
        elif boobs_revealed:
            $ strip_requirement = 30
        elif underwear_revealed:
            $ strip_requirement = 20

        if ass_revealed and the_person.has_taboo("bare_pussy"):
            $ strip_requirement += 10
        if boobs_revealed and the_person.has_taboo("bare_tits"):
            $ strip_requirement += 10
        if underwear_revealed and the_person.has_taboo("underwear_nudity"):
            $ strip_requirement += 10

        if the_person.effective_sluttiness() >= strip_requirement: #Note that taboos are added separately.
            $ willing_to_strip = True

        # TODO: Check if we really care about this private option.
        if not is_private: #She also cares about what she will end up wearing in front of other people.
            $ willing_to_strip = willing_to_strip and the_person.judge_outfit(test_outfit, use_taboos = True)

        $ willing_if_ordered = False
        if not willing_to_strip: #If she won't strip we might have a chance to command her toself.
            $ ran_num = the_person.obedience - 100
            if strip_type == "Half":
                $ ran_num += 10 #She's more likely to listen to you obediently when you strip her quickly.

            if is_private:
                $ willing_if_ordered = the_person.effective_sluttiness() + ran_num >= strip_requirement
            else:
                $ willing_if_ordered = the_person.judge_outfit(test_outfit, temp_sluttiness_boost = ran_num, use_taboos = True)

            if willing_if_ordered:
                $ the_person.call_dialogue("strip_obedience_accept", the_clothing = strip_choice, strip_type = strip_type)
                menu:
                    "Do it anyways":
                        "You proceed despite [the_person.possessive_title]'s objections, trusting her to remain obedient and docile."
                        $ willing_to_strip = True
                        $ ordered_to_strip = True
                        $ the_person.discover_opinion("being submissive")
                        $ the_person.change_happiness(-5 + (5 * the_person.opinion.being_submissive))

                    "Let it be":
                        "You leave [the_person.possessive_title]'s [strip_choice.display_name] in place, and she relaxes."

        if willing_to_strip:
            if not ignore_taboo:
                if ass_revealed and the_person.has_taboo("bare_pussy"):
                    $ the_person.call_dialogue("bare_pussy_taboo_break", the_clothing =  strip_choice)
                elif boobs_revealed and the_person.has_taboo("bare_tits"):
                    $ the_person.call_dialogue("bare_tits_taboo_break", the_clothing = strip_choice)
                elif underwear_revealed and the_person.has_taboo("underwear_nudity"):
                    $ the_person.call_dialogue("underwear_nudity_taboo_break", the_clothing = strip_choice)

            if strip_type == "Half":
                $ the_person.draw_animated_removal(strip_choice, position = the_position_tag, half_off_instead = True)
                $ renpy.say(None, f"You pull her {strip_choice.display_name} out of the way.")
            else:
                $ the_person.draw_animated_removal(strip_choice, position = the_position_tag)
                if strip_choice.half_off:
                    $ renpy.say(None, f"You pull her {strip_choice.display_name} off entirely and drop it on the ground.")
                else:
                    $ renpy.say(None, f"You pull her {strip_choice.display_name} off, dropping it to the ground.")

            $ arousal_change = 0
            if strip_type == "Full":
                $ arousal_change -= 5

            if underwear_revealed or boobs_revealed or ass_revealed:
                $ arousal_change += the_person.opinion.not_wearing_anything * 2
                $ the_person.discover_opinion("not wearing anything")
                if underwear_revealed:
                    $ the_person.break_taboo("underwear_nudity")

            if boobs_revealed:
                $ arousal_change += the_person.opinion.showing_her_tits * 3
                $ the_person.discover_opinion("showing her tits")
                $ the_person.break_taboo("bare_tits")
                if the_person.has_large_tits and the_person.tits_available:
                    "Her big tits drop free, begging to be felt up."

            if ass_revealed:
                $ arousal_change += the_person.opinion.showing_her_ass * 3
                $ the_person.discover_opinion("showing her ass")
                $ the_person.break_taboo("bare_pussy")

            if arousal_change > 0:
                the_person "Oh my god..."
                $ the_person.change_arousal(arousal_change)
                if the_person.arousal_perc > 100:
                    $ play_moan_sound()
                    "[the_person.possessive_title!c] moans and shivers, seemingly on the edge of an orgasm."
                else:
                    $ play_moan_sound()
                    if strip_type == "Half":
                        "[the_person.possessive_title!c] bites her lip and moans as you pull at her clothing."
                    else:
                        "[the_person.possessive_title!c] bites her lip and moans as you strip her down."
            elif arousal_change < 0:
                $ the_person.change_arousal(arousal_change)
                if strip_type == "Half":
                    "[the_person.possessive_title!c] is impatient as you pull at her clothing."
                else:
                    "[the_person.possessive_title!c] is impatient as you strip her down."

        else:
            if not willing_if_ordered: #If she was willing if ordered then the dialogue is called up top.
                if strip_type == "Half":
                    $ renpy.say(None, f"You start to pull {the_person.display_name}'s {strip_choice.name} out of the way.")
                    $ renpy.say(None, "She grabs your hand gently.")
                else:
                    $ renpy.say(None, f"You start to pull off {the_person.display_name}'s {strip_choice.name} when she grabs your hand and stops you.")
                $ the_person.call_dialogue("strip_reject", the_clothing = strip_choice , strip_type = strip_type) #TODO: pass the piece of clothing and base some dialogue off of that.
        $ renpy.call("strip_menu", the_person, the_position, is_private, ignore_taboo) #TODO: Girl sometimes interrupts you to get you to keep going. Have to strip them down in segments.

    python:
        choice_return = None
        test_outfit = None
        strip_choice = None
        the_verbing = None
        the_position_tag = None
    return

label girl_strip_event(the_person, the_position, the_object):
    $ the_clothing = choose_strip_sex_position_item(the_person, position = the_position)
    if not the_clothing:
        return  # nothing to strip (based on position, improves flow of sex loop)

    python:
        ran_num = the_person.effective_sluttiness() - the_person.outfit.outfit_slut_score
        ran_num += the_person.opinion.not_wearing_anything * 5
        if not mc.location.is_private:  # less chance when not private (based on public sex opinion)
            ran_num += (the_person.opinion.public_sex - 2) * 5

    if renpy.random.randint(0,100) < ran_num and the_clothing:
        if renpy.random.randint(0,100) < the_person.obedience - the_person.arousal:
            $ the_position.call_strip_ask(the_person, the_clothing, mc.location, the_object)
        else:
            $ the_position.call_strip(the_person, the_clothing, mc.location, the_object) #If a girl's outfit is less slutty than she is currently feeling (with arousal factored in) she will want to strip stuff off.

        $ the_person.update_outfit_taboos()

        if the_person.outfit.has_clothing(the_clothing):
            # you told her not to strip, so we will not ask again until player initiates stripping
            $ stop_stripping = True

    $ the_clothing = None
    return

# call after striping to show the stripping taboo break dialog
label break_strip_outfit_taboos(the_person):
    $ taboo_broken = False
    if the_person.tits_visible and the_person.vagina_visible:
        "Once she's done stripping [the_person.possessive_title] is practically naked."
        if the_person.has_taboo(["bare_pussy", "bare_tits"]):
            "She makes a vain attempt to keep herself covered with her hands, but soon enough seems to be comfortable being nude in front of you."
            $ the_person.break_taboo("bare_pussy")
            $ the_person.break_taboo("bare_tits")
            $ taboo_broken = True
    elif the_person.tits_visible:
        "Once she's done stripping [the_person.possessive_title] has her nice [the_person.tits] tits out on display."
        if the_person.has_taboo("bare_tits"):
            if the_person.has_large_tits:
                "She makes a hopeless attempt to cover her [the_person.tits_description] with her hands, but comes to the realisation it's pointless."
            else:
                "She tries to hide her [the_person.tits_description] from you with her hands, but quickly realises how impractical that would be."
            "Soon enough she doesn't even mind having them out."
            $ the_person.break_taboo("bare_tits")
            $ taboo_broken = True
    elif the_person.vagina_visible:
        "Once she's done stripping [the_person.possessive_title] has her pretty little pussy out on display for everyone."
        if the_person.has_taboo("bare_pussy"):
            "She tries to hide herself from you with her hand, but quickly realises how impractical that would be."
            "Soon enough she doesn't seem to mind."
            $ the_person.break_taboo("bare_pussy")
            $ taboo_broken = True
    else:
        "[the_person.possessive_title!c] finishes stripping and looks back at you."
        if (the_person.are_panties_visible) or (the_person.is_bra_visible):
            if the_person.has_taboo("underwear_nudity"):
                "She seems nervous at first, but quickly gets used to being in her underwear in front of you."
                $ the_person.break_taboo("underwear_nudity")
                $ taboo_broken = True
    return taboo_broken

label pick_position(the_person, current_position = None, ignore_taboo = False, prohibit_tags = [], condition = Condition_Type.default_condition()):
    call screen main_choice_display(build_menu_items(build_grouped_sex_position_menu(the_person, current_position = current_position, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, condition = condition)))
    $ position_choice = _return if isinstance(_return, Position) else None
    return

label public_sex_post_round(the_person, position_choice, report_log):
    $ scrutiny = report_log.get("scrutiny",0)
    if position_choice is None: #We got here by accident
        return
    if finished:
        return False
    if mc.location.is_private:
        return True     #Its a private room, don't do anything
    if (not the_watcher and mc.location.person_count <= 1) or (the_watcher and mc.location.person_count <= 2):
        return True     # no other people or only watcher around

    if the_person.is_employee and the_person.is_at_office:    #It's at work. possibly effect HR efficiency?
        if position_choice.slut_requirement < mc.location.room_average_slut:
            "You [position_choice.verb] [the_person.title] in front of everyone in the [mc.location.formal_name!i], you hear a few murmurs and get a few looks, but mostly they don't seem to mind."
        elif position_choice.slut_requirement < mc.location.room_average_slut + 15:
            "You [position_choice.verb] [the_person.title] in front of everyone in the [mc.location.formal_name!i], you are getting some dirty looks from the other employees in the room, but they keep working despite the distraction."
            $ mc.business.change_team_effectiveness(-1)
            $ mc.log_event("Business efficiency reduced", "float_text_yellow")
        else:
            "You [position_choice.verb] [the_person.title] in front of everyone in the [mc.location.formal_name!i], you are getting dirty looks and comments from your other employees. Your session is disrupting work."
            $ mc.business.change_team_effectiveness(-3)
            $ mc.log_event("Business efficiency reduced", "float_text_yellow")
    elif mc.location.privacy_level in (1, 2):    #Somewhere things are not usually permitted but if kept low key can get away with it.
        $ scr_change = get_scrutiny_value(the_person, position_choice) * 3
        if (scrutiny + scr_change) // 25 > scrutiny // 25: # only show when 'level' changes
            "You [position_choice.verb] [the_person.title] in public at the [mc.location.formal_name!i]."
            if mc.business.public_sex_is_legal:
                "Since public sex is legal, you get no more than a few dirty, maybe even interested looks."
            elif position_choice.associated_taboo not in ["vaginal_sex", "anal_sex"] and mc.business.public_sex_act_is_legal:
                "Since public sex acts are legal, you get some curious looks but little else."
            elif scrutiny < 25:
                "So far, your actions are being mostly ignored. If you go quick and stay quiet, you might get away with it."
            elif scrutiny < 50:
                "A few employees have noticed what you are up to, but so far just seem annoyed. You should finish up."
            elif scrutiny < 75:
                "You are getting looks from the employees. Several have noticed your unwanted actions."
            elif scrutiny < 100:
                "Employees and customers have noticed what you are up to. You need to finish up quickly or things could get ugly."
            else:
                "Employee" "Hey! You can't do that here! Knock it off or I'm calling the cops!"
                "Sadly, you pushed your luck too far. You decide to stop before you get in any real trouble."
                return False
        if not mc.business.public_sex_is_legal and not (position_choice.associated_taboo not in ["vaginal_sex", "anal_sex"] and mc.business.public_sex_act_is_legal):
            $ report_log["scrutiny"] = scrutiny + scr_change
    elif mc.location.privacy_level == 3:    #You are out in public
        $ scr_change = get_scrutiny_value(the_person, position_choice) * 5
        if (scrutiny + scr_change) // 25 > scrutiny // 25: # only show when 'level' changes
            "You [position_choice.verb] [the_person.title] in public at the [mc.location.formal_name!i]."
            if mc.business.public_sex_is_legal:
                "Since public sex is legal, you get no more than a few dirty, maybe even interested looks."
            elif position_choice.associated_taboo not in ["vaginal_sex", "anal_sex"] and mc.business.public_sex_act_is_legal:
                "Since public sex acts are legal, you get some curious looks but little else."
            elif scrutiny < 25:
                "So far, your actions are being mostly ignored. If you go quick and stay quiet, you might get away with it."
            elif scrutiny < 50:
                "A few people have noticed what you are up to, but so far just seem annoyed. You should finish up."
            elif scrutiny < 75:
                "You are getting nasty looks from other people. Several have noticed your illegal actions."
            elif scrutiny < 100:
                "A small crowd has gathered to watch, and you are getting several comments from people to stop."
            else:
                if the_person == police_chief: #Exclude scrutiny when doing the police chief
                    "A small crowd is watching you and [the_person.possessive_title], but they are too intimidated to interfere."
                else:
                    call police_chief_public_sex_intervention(the_person) from _arrested_during_public_sex_01
                    return False
        if not mc.business.public_sex_is_legal and not (position_choice.associated_taboo not in ["vaginal_sex", "anal_sex"] and mc.business.public_sex_act_is_legal):
            $ report_log["scrutiny"] = scrutiny + scr_change
    return True

label describe_girl_climax(the_person, the_position, the_object, private, report_log):
    $ the_position.call_orgasm(the_person, mc.location, the_object)
    $ the_person.change_arousal(-builtins.max(the_person.arousal/(report_log.get("girl orgasms", 0)+2)+20, the_person.arousal - the_person.max_arousal - 1)) # Repeated orgasms make it easier and easier to make a girl cum. It's possible to make her cum every single round!
    $ trance_chance_modifier = the_position.get_trance_chance_modifier(the_person) + report_log.get("girl orgasms", 0)
    $ report_log["girl orgasms"] = report_log.get("girl orgasms", 0) + 1
    $ the_person.run_orgasm(trance_chance_modifier = trance_chance_modifier, sluttiness_increase_limit = the_position.slut_requirement, reset_arousal = False)
    call girl_orgasm_watch(the_person) from _call_girl_orgasm_watch_describe_girl_climax
    $ the_position.redraw_scene(the_person)
    return

label affair_check(the_person, report_log): #Report log is handed over so we can make reference to the specific scene if we want.
    $ the_person.draw_person()
    the_person "[the_person.mc_title], you make me feel ways my [the_person.so_title] never does. I feel alive! Excited! Aroused..."
    the_person "We both have feelings for each other, right? Maybe we can see each other some more. My [the_person.so_title] doesn't need to know. He'll never find out."
    $ the_person.discover_opinion("cheating on men")
    menu:
        "Have an affair with [the_person.title]":
            mc.name "I want that too, anything that will let me be close to you."
            $ the_person.draw_person(emotion = "happy")
            $ the_person.add_role(affair_role)
            $ the_person.change_slut(2, 60)
            "She smiles and hugs you."

        "Refuse":
            mc.name "That's not what I'm here for [the_person.title]. This was fun, but I don't want it to be anything but completely casual."
            $ the_person.change_love(-1)
    return

label sex_description(the_person, the_position, the_object, private = True, report_log = None):
    # Processes a single normal "round" of sex. Removes energy, increases arousal, calls for dialogue from people nearby, etc. then returns to the main loop.

    # Draw the person and deliver the position specific description
    $ the_position.redraw_scene(the_person)
    $ the_position.call_scene(the_person, mc.location, the_object)

    # parse the positions scene to a new position/object
    $ forcedNewPosition, forcedNewObject = the_position.parseReturnToNewPostionAndObject(_return)

    $ mc.listener_system.fire_event("sex_event", the_person = the_person, the_position = the_position, the_object = the_object)

    if report_log is not None:
        $ report_log["total rounds"] = report_log.get("total rounds", 0) + 1
    if report_log:
        $ report_log["positions_used"].append(the_position)

    # this is the point where you definitely find out if she likes vaginal or anal
    if the_position.skill_tag == "Vaginal":
        $ the_person.discover_opinion("vaginal sex")
    if the_position.skill_tag == "Anal":
        $ the_person.discover_opinion("anal sex")

    # If we have a new position, transition to new position and skip arousal, climax and watcher
    if forcedNewPosition is not None:
        return (forcedNewPosition, forcedNewObject)

    # Change the arousal for both people:
    # Her arousal first
    $ her_arousal_change = the_position.girl_arousal * (1.0 + 0.1 * mc.sex_skills[the_position.skill_tag]) # Each level the other party has in the sex class adds 10% arousal.
    if the_position.skill_tag == "Vaginal":
        $ the_person.discover_opinion("bareback sex")
        if mc.condom:
            $ her_arousal_change += -1 # Condoms don't feel as good (but matter less for her)
            $ her_arousal_change += -2 * the_person.opinion.bareback_sex
        else:
            $ her_arousal_change += 2 * the_person.opinion.bareback_sex

    $ opinion_score = the_position.get_opinion_score(the_person)
    $ her_arousal_change += opinion_score

    if the_person.effective_sluttiness() > the_position.slut_cap: #She's sluttier than this position, it's only good to warm her up.
        if opinion_score < 1 and the_person.arousal_perc > the_position.slut_cap: #Once her arousal is higher than the cap she's completely bored by it.
            $ mc.log_event(f"{the_person.display_name} is bored", "float_text_red")
            $ her_arousal_change = her_arousal_change / 2

    $ clothing_count = 0
    $ interfering_clothing = []
    if the_position.skill_tag == "Vaginal" or the_position.skill_tag == "Anal":
        python:
            for clothing in the_person.outfit.get_lower_ordered():
                if clothing.anchor_below and clothing.half_off_gives_access and clothing.half_off:
                    clothing_count += 1 #Each piece of clothing that's only half off lowers the amount of arousal gain for both parties
                    interfering_clothing.append(clothing)

    elif the_position.requires_large_tits:
        python:
            for clothing in the_person.outfit.get_upper_ordered():
                if clothing.anchor_below and clothing.half_off_gives_access and clothing.half_off:
                    clothing_count += 1 #Each piece of clothing that's only half off lowers the amount of arousal gain for both parties
                    interfering_clothing.append(clothing)

    if clothing_count > 0:
        $ clothing_string = format_list_of_clothing(interfering_clothing)
        $ obstruction_phrase = "get in the way" if " and " in clothing_string else "gets in the way"
        "[the_person.title]'s half–off [clothing_string] [obstruction_phrase], lowering your enjoyment somewhat."
    $ del interfering_clothing

    $ her_arousal_change += -clothing_count
    $ the_person.change_arousal(her_arousal_change)

    # Now his arousal change
    $ his_arousal_change = the_position.guy_arousal * (1.0 + 0.1 * the_person.sex_skills[the_position.skill_tag])
    $ his_arousal_change += -clothing_count
    if the_position.skill_tag in ("Vaginal", "Anal") and mc.condom:
        $ his_arousal_change -= 2 # Condoms don't feel as good.

    $ mc.change_arousal(his_arousal_change)
    # $ amount = (the_person.sex_skills[the_position.skill_tag] + mc.sex_skills[the_position.skill_tag]) // 2    OLD lust increase.
    # lust gain based on sluttiness of the position and how naked she is
    # $ amount = (the_position.slut_cap + the_person.outfit.outfit_lust_score) // 4
    # if amount + mc.locked_clarity > 1000: # locked clarity maxes out at 1000
    #     $ amount = 1000 - mc.locked_clarity
    # $ mc.locked_clarity += amount
    # Fuck it, just call the locked clarity function. Will cause MC's arousal to rise faster maybe
    $ mc.change_locked_clarity(the_position.slut_cap // 4, person = the_person)
    if mc.recently_orgasmed and mc.arousal_perc >= 10:
        $ mc.recently_orgasmed = False
        "Your cock stiffens again, coaxed back to life by [the_person.title]."

    # Change their energy as well.
    python:
        the_person.change_energy(-the_position.calculate_energy_cost(the_person), add_to_log = False)
        mc.change_energy(-the_position.calculate_energy_cost(mc), add_to_log = False)

    # $ the_person.change_energy(-the_position.girl_energy, add_to_log = False) #NOTE: Don't show the energy cost to avoid energy notice spam. The energy cost is already displayed to the player.
    # $ mc.change_energy(-the_position.guy_energy, add_to_log = False)

    if the_person.lactation_sources > 0:
        call lactation_description(the_person, the_position, the_object, report_log) from _call_lactation_description

    # If someone orgasms describe that.
    if the_person.arousal_perc >= 100:
        call describe_girl_climax(the_person, the_position, the_object, private, report_log) from _call_describe_girl_climax_2

    if mc.arousal_perc >= 80: #NOTE: use to be mc.max_arousal, this number is now the threshold for being forced to cum.
        call climax_check() from _call_climax_check_sex_description
        $ is_cumming = _return

        if is_cumming:
            $ the_position.call_outro(the_person, mc.location, the_object)
            # parse the scene outro to a new position / object
            $ forcedNewPosition, forcedNewObject = the_position.parseReturnToNewPostionAndObject(_return)

            if the_person.effective_sluttiness(the_position.associated_taboo) < the_position.slut_requirement: # bonus obedience if she if she had to be ordered to do this position ("I guess I really am just doing this for him...")
                $ the_person.change_obedience(3 + the_person.opinion.being_submissive, 160)
            else:
                $ the_person.change_obedience(3, 160)

            $ mc.recently_orgasmed = True
            $ report_log["guy orgasms"] = report_log.get("guy orgasms", 0) + 1

    if not mc.recently_orgasmed:
        if not private:
            call watcher_check(the_person, the_position, the_object, report_log) from _call_watcher_check
        else:
            call walk_in_watcher_check(the_person, the_position, the_object, report_log) from _call_walk_in_watcher_check

    return (forcedNewPosition, forcedNewObject)       # pass back new object

label lactation_description(the_person, the_position, the_object, report_log): #NOTE: Is only called if lactation_sources > 0.
    $ tit_rank = Person.rank_tits(the_person.tits)
    $ strength = (the_person.arousal_perc / 100) * (the_person.lactation_sources + (tit_rank * 0.1)) #ie large tits add anywhere from 0 to 0.9 extra lactation sources.
    if strength > tit_rank + 1:
        $ strength = tit_rank + 1

    if the_person.tits_available:
        if strength <= 0.5:
            pass
        elif strength <= 0.75:
            "[the_person.title]'s bare tits are leaking milk, a single drop hanging from each nipple."
        elif strength <= 1.0:
            "[the_person.title]'s naked tits drip milk, a drop every couple of seconds."
        elif strength <= 1.5:
            "[the_person.title]'s tits are leaking faster now. With every move a couple of drops escape from her nipples." #Triggers at 100% arousal w/ 1 lactation source, 50% arousal w/ 2 sources or max sized tits.
        elif strength <= 2.0:
            "[the_person.title] has a steady trickle of milk running from her nipples and over her breasts."
        elif strength <= 3.0:
            "[the_person.title]'s tits are producing a steady stream of breast milk, which gets flung around in fat drops every time she moves."
        elif strength <= 4.0: #This is 100% arousal w/ big tits and 1 source, or the result of 2+ sources
            "Breast milk squirts out of [the_person.title]'s tits, provoked only by her own arousal."
        elif strength <= 6.0: #This is 100% arousal w/ hucow modification
            "Breast milk jets out of [the_person.title]'s nipples. It sprays out in an arc, pulsing farther with every jolt of pleasure."
        elif strength <= 7.5:
            "[the_person.title]'s tits continue to pulse out hot breast milk, unprovoked by anything other than her own arousal."
        else:
            "[the_person.title]'s tits are producing a heavy spray of milk, making a wet mess of her chest and anything within two feet that she points herself at."


    elif the_person.outfit.is_bra_visible or not the_person.outfit.wearing_bra:
        if strength <= 0.5:
            pass #Not a noticeable effect, do nothing
        elif strength <= 1.5:
            "[the_person.title]'s nipples must be dripping milk, because there are two wet spots on her [the_person.outfit.get_upper_top_layer.display_name] forming around them."
        elif strength <= 3.0:
            "[the_person.title]'s lactating tits have soaked through her [the_person.outfit.get_upper_top_layer.display_name], leaving large wet spots around her nipples."
        elif strength <= 7.5:
            "[the_person.title]'s milky tits have completely soaked her [the_person.outfit.get_upper_top_layer.display_name] now. Warm milk drips off away from the edges in a steady stream."
        else:
            "[the_person.title]'s tits are squirting milk so hard that it's spraying right through her [the_person.outfit.get_upper_top_layer.display_name]. Little arcs of the warm liquid sail out two {height_system} from her chest."


    else:
        if strength <= 2.0:
            pass #Not a noticeable effect under all of her clothing.
        elif strength <= 4.0:
            "[the_person.title]'s nipples must be dripping milk, because there are two wet spots on her [the_person.outfit.get_upper_top_layer.display_name] forming around them."
        elif strength <= 7.5:
            "[the_person.title]'s lactating tits have soaked through her [the_person.outfit.get_upper_top_layer.display_name], leaving large wet spots around her nipples."
        else:
            "[the_person.title]'s milky tits have completely soaked her [the_person.outfit.get_upper_top_layer.display_name] now. Warm milk drips off away from the edges in a steady stream."
    return

label climax_check():
    # when perk active use orgasm control
    if mc.business.event_triggers_dict.get('orgasm_control_active', False):
        call climax_check_orgasm_control from _call_climax_check_orgasm_control_climax_check
        return _return

    $ is_cumming = False
    if mc.arousal_perc < 100:
        menu:
            "Try and cum early":
                if renpy.random.randint(0,100) < 10*mc.focus + (mc.max_arousal - mc.arousal):
                    $ is_cumming = True
                    "You focus as hard as you can and feel yourself grow closer and closer to climax."
                else:
                    "You focus as hard as you can, but you're unable to push yourself over the edge."

            "Keep going!":
                pass
    else:
        menu:
            "Try to hold back":
                if renpy.random.randint(0,100) < 10*mc.focus + (mc.max_arousal - mc.arousal): #Note: arousal is > max_arousal, so that's focus - some number, ie it's harder and harder as your arousal increases.
                    "You focus yourself and stave off your climax for a little longer."
                else:
                    "You focus as hard as you can, but there's nothing you can do at this point!"
                    $ is_cumming = True

            "Cum!":
                $ is_cumming = True

    return is_cumming

# this must be a label since renpy.call() always return to next label statement
# and not python code, so renpy.call must always be the last statement
label double_orgasm_label(the_position, the_person, the_location, the_object):
    $ orgasm_choice = True
    if the_position.double_orgasm and perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
        if mc_serum_feat_orgasm_control.trait_tier >= 1 or mc.arousal >= mc.max_arousal:
            call climax_check_double_orgasm_control_label() from _double_orgasm_check_01
            $ orgasm_choice = _return

    if orgasm_choice and the_position.double_orgasm and mc.arousal >= mc.max_arousal:
        $ renpy.call(the_position.double_orgasm, the_person, the_location, the_object)
    else:
        $ renpy.call(the_position.orgasm_description, the_person, the_location, the_object)
    return
