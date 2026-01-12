init python:
  def set_pos_align(trans, xchange, ychange):
    trans.xalign = xchange
    trans.yalign = ychange
    return None


transform threesome_test_1():
    yalign 0.5
    yanchor 0.5
    function set_pos_align
    zoom 1.0

transform threesome_test_2():
    yalign 0.5
    yanchor 0.5
    function set_pos_align
    zoom 1.0

init -1 python:
    list_of_threesomes = []
    girl_swap_pos = False  #Nasty hack to tell threesome code to swap girl 1 and girl 2. #TODO find a better way to do this
    THREESOME_BASE_SLUT_REQ = 80  #A constant to hold the usual base sluttiness requirements for threesomes.

label threesome_test():
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom)
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    $ scene_manager.strip_full_outfit(delay = 0)
    call start_threesome(mom, lily) from threesome_test_call_1
    $ scene_manager.clear_scene()
    return "Test Complete"

label threesome_join_test():
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom, position = "standing_doggy")
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    $ scene_manager.strip_full_outfit(delay = 0)

    $ test_pos = ["against_wall", "doggy", "blowjob", "missionary", "cowgirl", "standing_doggy"]
    $ count = 0
    while count < len(test_pos):
        $ scene_manager.add_actor(mom, position = test_pos[count])
        $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
        $ renpy.say(None, f"Starting Position: {test_pos[count]}")
        call join_threesome(mom, lily, test_pos[count], private = True) from _call_threesome_join_test
        $ count += 1

    $ scene_manager.clear_scene()
    return "Test Complete"

label threesome_alignment():
    $ position_choice = threesome_double_blowjob
    $ position_choice.update_scene(mom, lily)
    $ finished = False
    while not finished:
        menu:
            "mom + x":
                $ position_choice.p1_transform.xpos += .01
                pass
            "mom - x":
                $ position_choice.p1_transform.xpos -= .01
                pass
            "mom + y":
                $ position_choice.p1_transform.yalign += .01
                pass
            "mom - y":
                $ position_choice.p1_transform.yalign -= .01
                pass
            "mom + zoom":
                $ position_choice.p1_transform.zoom += .01
                pass
            "mom - zoom":
                $ position_choice.p1_transform.zoom -= .01
                pass
            "lily + x":
                pass
            "lily - x":
                pass
            "lily + y":
                pass
            "lily - y":
                pass
            "lily + zoom":
                pass
            "lily - zoom":
                pass
        $ scene_manager.draw_scene()

init 5 python:
    def build_threesome_round_start_menu(position_choice, person_one, person_two):
        option_list = []
        option_list.append("Start Choice")
        for options in position_choice.mc_position:
            if options.requirement(person_one, person_two):
                option_list.append((options.description,options.name))
        option_list.append(("Change your mind and leave", "Leave"))
        return option_list

    def build_threesome_round_choice_menu(position_choice, person_one, person_two, position_locked, hide_leave):
        option_list = []
        option_list.append("Round Choice")
        if position_choice is not None:
            option_list.append(("Keep going", "Continue")) #Note: you're prevented from continuing if the energy cost would be too high by the pre-round checks.
            if not (person_one.outfit.has_full_access or person_two.outfit.has_full_access):
                option_list.append(("Pause and strip them down", "Strip"))

            #Give option for MC to change position without changing the girls positions
            for options in position_choice.mc_position:
                if options != active_mc_position:
                    if options.requirement(person_one, person_two):
                        option_list.append((options.description, options.name))

            if not position_locked:
                option_list.append(("Pause and change position\n-5 {image=gui/extra_images/arousal_token.png}", "Change"))
                #### For now, no implementation of connections
                # for position in position_choice.connections:
                #     if object_choice.has_trait(position.requires_location):
                #         appended_name = "Transition to " + position.build_position_willingness_string(the_person) #Note: clothing and energy checks are done inside build_position_willingness, invalid positions marked (disabled)
                #         option_list.append((appended_name,position))

            if not hide_leave: #TODO: Double check that we can always get out
                option_list.append(("Stop fucking and leave", "Leave")) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

        else:
            if not position_locked:
                option_list.append(("Pick a new position\n-5 {image=gui/extra_images/arousal_token.png}", "Change"))
            if not (person_one.outfit.has_full_access or person_two.outfit.has_full_access):
                option_list.append(("Strip them down", "Strip"))
            if not hide_leave:
                option_list.append(("Stop and leave", "Leave"))
        return option_list

    def build_threesome_person_one_position_choice_menu(person_one, person_two):
        option_list = []
        option_list.append(person_one.name + " position:")
        for threeway in list_of_threesomes:
            if threeway.requirements(person_one, person_two):
                if (get_initial_threesome_pairing(threeway.position_one_tag)) not in option_list: #This doesn't work for stand2-5 TODO
                    option_list.append(get_initial_threesome_pairing(threeway.position_one_tag))
                if (get_initial_threesome_pairing(threeway.position_two_tag)) not in option_list:
                    option_list.append(get_initial_threesome_pairing(threeway.position_two_tag))
        return option_list

    def build_threesome_person_two_position_choice_menu(person_one, person_two, initial_position):
        option_list = []
        option_list.append(person_two.name + " position:")
        for threeway in list_of_threesomes:
            if threeway.requirements(person_one, person_two):
                if threeway.position_one_tag == initial_position:            #Look for positions that match with any position taken by girl 1
                    option_list.append((threeway.girl_two_final_description, threeway.position_two_tag))
                elif threeway.position_two_tag == initial_position:
                    option_list.append((threeway.girl_one_final_description, threeway.position_one_tag))
        if builtins.len(option_list) == 0:
            renpy.say(None, "Something has gone wrong, no available positions")  #Return something default?
        return option_list

    def build_threesome_strip_menu(person_one, person_two):
        option_list = []
        option_list.append("Stripping Choice")
        if not person_one.outfit.has_full_access:
            option_list.append (["Strip " + person_one.title, "strip_one"])
        if not person_two.outfit.has_full_access:
            option_list.append (["Strip " + person_two.title, "strip_two"])
        option_list.append (["Finished", "Leave"])
        return option_list

    def update_threesome_action_description(position, swapped):
        for mc_pos in position.mc_position:
            if mc_pos.action_description:
                if swapped:
                    mc_pos.description = mc_pos.action_description.replace("{0}", "one" if mc_pos.default_action_person == "two" else "two")
                else:
                    mc_pos.description = mc_pos.action_description.replace("{0}", "two" if mc_pos.default_action_person == "two" else "one")
        return

    def choose_threesome_position(girl_one_choice, girl_two_choice):
        for threeway in list_of_threesomes:
            if girl_one_choice == threeway.position_one_tag and girl_two_choice == threeway.position_two_tag:
                position_choice = threeway
                swapped = False
            if girl_one_choice == threeway.position_two_tag and girl_two_choice == threeway.position_one_tag:
                position_choice = threeway
                swapped = True

        #print ("Chosen Position: " + threeway.name + (" (Swapped)" if girl_swap_pos else ""))

        update_threesome_action_description(position_choice, swapped)
        return (position_choice, swapped)

    def valid_threesome_position(position):
        return any([x for x in list_of_threesomes if position in [x.position_one_tag, x.position_two_tag]])

    def get_mc_round_choice(position_choice, person_one, person_two):
        option_list = []
        for options in position_choice.mc_position:
            if options.requirement(person_one, person_two):
                option_list.append((options.description, options.name))
        option_list.append(("Change your mind and leave", "Leave"))
        return renpy.display_menu(option_list, True, "Choice")

    def get_mc_active_position(position_choice, round_choice):
        for options in position_choice.mc_position:
            if round_choice == options.name:
                return options
        return None

label start_threesome(the_person_one, the_person_two, start_position = None, start_object = None, skip_intro = False, private = True, girl_in_charge = False, position_locked = False, report_log = None, affair_ask_after = True, hide_leave = False, swapped = False):
    # When called
    if report_log is None:
        $ report_log = create_report_log({"was_public": not private})

    python:
        report_log["girl one orgasms"] = 0
        report_log["girl two orgasms"] = 0
        report_log["total orgasms"] = 0
        mc.recently_orgasmed = False

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = None
    $ object_choice = None
    $ girl_swap_pos = swapped

    #Family situational modifiers
    #Omitting these for now

    #Cheating modifiers
    #Also leaving these out

    #Privacy modifiers

    #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.

    #If no initial position set, get one now
    if start_position is None:
        call pick_threesome(the_person_one, the_person_two) from threesome_initial_position_set
        $ position_choice = _return[0]
        $ girl_swap_pos = _return[1]
    else:
        $ position_choice = start_position
        $ update_threesome_action_description(position_choice, girl_swap_pos)

    $ position_choice.update_scene(the_person_one, the_person_two)
    if not skip_intro:
        "As the girls get into position, you consider how to begin your threesome."

    # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ active_mc_position = None
    call screen main_choice_display(build_menu_items([build_threesome_round_start_menu(position_choice, the_person_one, the_person_two)]))
    $ round_choice = _return

    if round_choice == "Leave":
        "Really? You changed your mind? You leave the poor girls after you got them all ready for some action."
    else:
        $ mc.listener_system.fire_event("threesome", the_person_one = the_person_one, the_person_two = the_person_two)
        $ active_mc_position = get_mc_active_position(position_choice, round_choice)
        if active_mc_position is None:
            "Something broke..."
            $ round_choice = "Leave"
        elif not skip_intro:
            $ active_mc_position.call_intro(the_person_one, the_person_two, mc.location, object_choice)
            $ scene_manager.draw_scene()    # intro can cause stripping and wrong layer drawing
            $ round_choice = None
        else:
            $ round_choice = None
    while not finished:
        # if girl_in_charge:
        #     # For now, default to guys only in charge
        if round_choice is None: #If there is no set round_choice
            #TODO: Add a variant of this list when the girl is in control to ask if you want to resist or ask/beg for something.

            call screen main_choice_display(build_menu_items([build_threesome_round_choice_menu(position_choice, the_person_one, the_person_two, position_locked, hide_leave)]))
            $ round_choice = _return

        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignore all of that
                "You decide to change it up."
                call pick_threesome(the_person_one, the_person_two) from threesome_mid_position_set
                $ position_choice = _return[0]
                $ girl_swap_pos = _return[1]
                $ position_choice.update_scene(the_person_one, the_person_two)
                "As the girls get into position, you consider how to resume your threesome."
                $ round_choice = get_mc_round_choice(position_choice, the_person_one, the_person_two)
                $ active_mc_position = get_mc_active_position(position_choice, round_choice)
                if round_choice == "Leave":
                    $ finished = True
                    "You decide to finish the threesome instead."

                if not active_mc_position:
                    "Something broke..."
                    $ finished = True
                else:
                    $ active_mc_position.call_intro(the_person_one, the_person_two, mc.location, object_choice)
                    $ scene_manager.draw_scene() # call intro can cause stripping and wrong z-order draw

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            if active_mc_position and position_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call threesome_round(the_person_one, the_person_two, position_choice = active_mc_position, object_choice = None, private = private, report_log = report_log) from _call_threesome_round_1
                $ first_round = False
                if not active_mc_position.requirement(the_person_one, the_person_two):
                    "Your post-orgasm cock softens, stopping you from continuing for now."
                    $ position_choice = None
                    $ active_mc_position = None
                elif active_mc_position.guy_energy > mc.energy:
                    "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                    $ position_choice = None
                    $ active_mc_position = None
                elif not active_mc_position.check_girl_one_energy(the_person_one):
                    the_person_one "I'm exhausted [the_person_one.mc_title], I can't keep this up..."
                    $ position_choice = None
                    $ active_mc_position = None
                    if the_person_two.energy > 30:
                        #TODO give option to continue fucking the second girl
                        the_person_two "Don't worry, I'm still good to go!"
                        "Do you want to continue?"
                        menu:
                            "Fuck [the_person_two.title]":
                                "[the_person_one.title] moves to the side and recovers while you resume activities with [the_person_two.title]."
                                $ scene_manager.hide_actor(the_person_one)
                                $ report_log["girl orgasms"] = report_log["girl two orgasms"]
                                call fuck_person(the_person_two, private = private, report_log = report_log, skip_condom = True, the_watcher = the_person_one) from threesome_to_twosome_transition_1
                                "When you finally finish up [the_person_one.possessive_title], they both lay down to recover."
                                $ scene_manager.show_actor(the_person_one, position = "missionary", display_transform = character_center_flipped)
                                $ scene_manager.show_actor(the_person_two, position = "missionary", display_transform = character_right)
                                $ report_log["girl two orgasms"] = _return["girl orgasms"]

                            "Done for now":
                                mc.name "I think we should just be done for now." #TODO girl takes over if she needs to cum and hasn't yet
                        $ finished = True
                    else:
                        the_person_two "Yeah me too. I think I need a break!"
                        $ finished = True
                elif not active_mc_position.check_girl_two_energy(the_person_two):
                    the_person_two "I'm exhausted [the_person_two.mc_title], I can't keep this up..."
                    $ position_choice = None
                    $ active_mc_position = None
                    if the_person_one.energy > 30:
                        the_person_one "Don't worry, I'm still good to go!"
                        "Do you want to continue?"
                        menu:
                            "Fuck [the_person_one.title]":
                                "[the_person_two.title] moves to the side and recovers while you resume activities with [the_person_one.title]."
                                $ scene_manager.hide_actor(the_person_two)
                                $ report_log["girl orgasms"] = report_log["girl one orgasms"]
                                call fuck_person(the_person_one, private = private, report_log = report_log, skip_condom = True, the_watcher = the_person_two) from threesome_to_twosome_transition_2
                                "When you finally finish up [the_person_one.possessive_title], they both lay down to recover."
                                $ scene_manager.show_actor(the_person_two, position = "missionary", display_transform = character_center_flipped)
                                $ scene_manager.show_actor(the_person_one, position = "missionary", display_transform = character_right)
                                $ report_log["girl one orgasms"] = _return["girl orgasms"]
                            "Done for now":
                                mc.name "I think we should just be done for now." #TODO girl takes over if she needs to cum and hasn't yet
                        $ finished = True

                        pass
                    else:
                        the_person_one "Yeah me too. I think I need a break!"
                        $ finished = True
                #else: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                #for now disable stripping
                    #pass
                    #call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event

        elif round_choice == "Strip":
            #currently not implemented
            call threesome_strip_menu(the_person_one, the_person_two) from _call_strip_menu_threesome_1

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end


        elif round_choice == "Girl Leave":
            $ finished = True
        #Need to catch position changes here.
        else:
            $ active_mc_position = get_mc_active_position(position_choice, round_choice)
            $ active_mc_position.call_transition(the_person_one, the_person_two, mc.location, object_choice)

        $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the beginning of the loop we can set a mandatory choice for the first one.


    # Teardown the sex modifiers

    if report_log.get("girl one orgasms", 0) > 0:
        $ the_person_one.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person_one.arousal = (the_person_one.arousal / 2)
    if report_log.get("girl two orgasms", 0) > 0:
        $ the_person_two.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person_two.arousal = (the_person_two.arousal / 2)

    #Easy marker to add to log if EVERYONE orgasmed
    if report_log.get("girl one orgasms", 0) > 0 and report_log.get("girl two orgasms", 0) > 0 and report_log.get("guy orgasms", 0) > 0:
        $ report_log["trifecta"] = True

    python: #Log all of the different classes of sex, but only once per class.
        the_person_one.sex_record["Threesomes"] = the_person_one.sex_record.get("Threesomes", 0) + 1
        the_person_two.sex_record["Threesomes"] = the_person_two.sex_record.get("Threesomes", 0) + 1

        # record the last time we had sex
        the_person_one.sex_record["Last Sex Day"] = day
        the_person_two.sex_record["Last Sex Day"] = day

        mc.condom = False
        mc.recently_orgasmed = False
        active_mc_position = None
        object_choice = None
        position_choice = None
        round_choice = None
        options = None
        the_person_one = None
        the_person_two = None

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label threesome_round(the_person_one, the_person_two, position_choice, object_choice = None, private = True, report_log = None):
    #Draw event before calling this scene

    #Normal round events
    $ position_choice.call_scene(the_person_one, the_person_two, mc.location, object_choice)
    # TODO listener event, to log events for challenge
    if report_log is not None:
        $ report_log["total rounds"] = report_log.get("total rounds", 0) + 1

    #Calculate arousal gains
    $ position_choice.calc_arousal_changes(the_person_one, the_person_two)
    #Erection changes
    if mc.recently_orgasmed and mc.arousal_perc >= 10:
        $ mc.recently_orgasmed = False
        "Your cock stiffens again, coaxed back to life by the girls."

    #Energy Changes
    $ mc.change_energy(-position_choice.guy_energy)
    $ the_person_one.change_energy(-position_choice.girl_one_energy)
    $ the_person_two.change_energy(-position_choice.girl_two_energy)

    #If girl(s) orgasms, call orgasm scene
    if the_person_one.arousal_perc >= 100 or the_person_two.arousal_perc >= 100:
        $ position_choice.call_orgasm(the_person_one, the_person_two, mc.location, object_choice)

        if the_person_one.arousal_perc >= 100:
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person_one)
            $ the_person_one.change_stats(arousal = -the_person_one.arousal/2, happiness = 5)
            $ report_log["girl one orgasms"] = report_log.get("girl one orgasms", 0) + 1
            $ report_log["total orgasms"] = report_log.get("total orgasms", 0) + 1
        if the_person_two.arousal_perc >= 100:
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person_two)
            $ the_person_two.change_stats(arousal = -the_person_two.arousal/2, happiness = 5)
            $ report_log["girl two orgasms"] = report_log.get("girl two orgasms", 0) + 1
            $ report_log["total orgasms"] = report_log.get("total orgasms", 0) + 1

    #If MC orgasms, call outro
    if mc.arousal_perc >= 100:
        $ position_choice.call_outro(the_person_one, the_person_two, mc.location, object_choice)
        $ the_person_one.change_obedience(3)
        $ the_person_two.change_obedience(3)
        $ mc.reset_arousal()
        if perk_system.has_ability_perk("Serum: Energy Regeneration") and mc_serum_energy_regen.trait_tier >= 2 and mc.energy > 30:
            $ mc.recently_orgasmed = False
            "Your personal Energy Serum allows you to continue your threesome."
        else:
            $ mc.recently_orgasmed = True
        $ report_log["guy orgasms"] = report_log.get("guy orgasms", 0) + 1
        $ report_log["total orgasms"] = report_log.get("total orgasms", 0) + 1
        if position_choice.get_mc_pleasure_source(the_person_one, the_person_two):   #returns none if MC is pleasuring himself
            $ ClimaxController.manual_clarity_release(climax_type = "threesome", person = (position_choice.get_mc_pleasure_source(the_person_one, the_person_two)))
        else:
            $ ClimaxController.manual_clarity_release()

    #TODO set public sex responses

    return

label pick_threesome(the_person_one, the_person_two, girl_one_position = None, object_choice = None):  #We can pass in a position for girl one if the second girl "walks in" on the sex event
    if not (girl_one_position and valid_threesome_position(girl_one_position)):
        call screen main_choice_display(build_menu_items([build_threesome_person_one_position_choice_menu(the_person_one, the_person_two)]))
        $ girl_one_choice = _return
    else:
        $ girl_one_choice = girl_one_position

    call screen main_choice_display(build_menu_items([build_threesome_person_two_position_choice_menu(the_person_one, the_person_two, girl_one_choice)]))
    $ girl_two_choice = _return

    return choose_threesome_position(girl_one_choice, girl_two_choice)

label threesome_strip_menu(the_person_one, the_person_two):
    call screen main_choice_display(build_menu_items([build_threesome_strip_menu(the_person_one, the_person_two)]))
    $ strip_choice = _return

    if strip_choice == "strip_one":
        mc.name "[the_person_one.title], I want you to give me full access."
        the_person_one "Of course!"
        $ scene_manager.strip_full_outfit(person = the_person_one)
        $ scene_manager.draw_scene()
    elif strip_choice == "strip_two":
        mc.name "[the_person_two.title], I want you to give me full access."
        the_person_two "Sounds good!"
        $ scene_manager.strip_full_outfit(person = the_person_two)
        $ scene_manager.draw_scene()
    else:
        return
    call threesome_strip_menu(the_person_one, the_person_two) from _threesome_recurrent_strip_call_1
    return

label join_threesome(the_person_one, the_person_two, initial_position, private = True, report_log = None):  #We can use this function to add a second girl to an existing sex scene.
    #Works by selecting a position then calling threesome with the first position pre-set
    call pick_threesome(the_person_one, the_person_two, girl_one_position = initial_position) from _join_threesome_position_selection_1
    call start_threesome(the_person_one, the_person_two, start_position = _return[0], skip_intro = True, private = private, report_log = report_log, swapped = _return[1]) from _join_threesome_in_progress_1
    return _return
