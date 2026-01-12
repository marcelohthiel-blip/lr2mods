# Overrides the default advance time function in the game
# it adds a increased chance for a crisis to occur when more time passed without a crisis
# it adds a way of preventing the same crisis popping up over and over, whilst others never get triggered by remembering a set of occurred events
init 10 python:
    add_label_hijack("after_load", "update_advance_time_action_list_label")

init -49 python:    # init early so other files can add
    limited_time_event_pool: ActionList = ActionList()
    crisis_list: ActionList = ActionList()
    morning_crisis_list: ActionList = ActionList() #Morning crises are called when a new day starts. They are for events that take place after the MC has been able to rest and is at home.

    excluded_crisis_tracker_events = [
        "work_relationship_change_label",
        "sister_phone_crisis_action_label",
        "mom_selfie_label",
        "late_for_work_action_label",
        "trait_for_side_effect_label"
    ]

label update_advance_time_action_list_label(stack):
    python:
        # update actions in action mod list with the ones defined (in loaded instances)
        update_advance_time_action_list()
    $ execute_hijack_call(stack)
    return

label advance_time(no_events = False, jump_to_game_loop = True):
    # 1) Turns are processed _before_ the time is advanced.
    # 1a) crises are processed if they are triggered.
    # 2) Time is advanced, day is advanced if required.
    # 3) People go to their next intended location.
    # Note: This will require breaking people's turns into movement and actions.
    # Then: Add research crisis when serum is finished, requiring additional input from the player and giving the chance to test a serum on the R&D staff.

    python:
        renpy.dynamic("count", "mandatory_event", "mandatory_advance_time", "jumped_day")
        #renpy.say(None, "advance time -> location: " + mc.location.name + ", time: [time_of_day]") # DEBUG
        count = 0 # NOTE: Count and Max might need to be unique for each label since it carries over.
        advance_time_max_actions = builtins.len(advance_time_action_list) # This list is automatically sorted by priority due to the class properties.
        clear_follow_mc_flag()
        mandatory_advance_time = False
        mandatory_event = False
        jumped_day = False

    while count < advance_time_max_actions:
        if not no_events or (not advance_time_action_list[count] in advance_time_event_action_list):
            if advance_time_action_list[count].is_action_enabled(): # Only run actions that have their requirement met.
                $ start_time = time.time()
                # $ renpy.say(None, "Run: " + advance_time_action_list[count].name)
                call expression advance_time_action_list[count].effect pass (*advance_time_action_list[count].args) from _call_advance_time_action_advance_time
                $ add_to_debug_log(f"Adv time: {advance_time_action_list[count].name} ({{total_time:.3f}})", start_time)

                $ clear_scene()
                if jumped_day:  # an event jumped to the next day, break current loop
                    $ count = advance_time_max_actions
        $ count += 1

    python:
        # increase crisis chance (every time slot)
        crisis_chance += 1
        mc.location.show_background()
        x = None
        c = None
        jumped_day = False

    if mandatory_advance_time and not time_of_day == 4: #If a crisis has told us to advance time after it we do so (not when night to prevent spending night at current location).
        call advance_time(no_events = True) from _call_advance_time_advance_time
    if no_events or not jump_to_game_loop:
        return

    $ jump_game_loop()
    return

label advance_time_move_to_next_day():
    $ current_day = day
    while day == current_day:
        call advance_time(no_events = True, jump_to_game_loop = False) from _call_advance_time_advance_time_move_to_next_day
    $ jumped_day = True
    return

label advance_time_bankrupt_check_label():
    python:
        if mc.business.funds < 0:
            # "advance_time_bankrupt_check_label" # DEBUG
            mc.business.bankrupt_days += 1
            if mc.business.bankrupt_days == mc.business.max_bankrupt_days:
                renpy.say(None,"With no funds to pay your creditors you are forced to close your business and auction off all of your materials at a fraction of their value. Your story ends here.")
                renpy.full_restart()
            else:
                days_remaining = mc.business.max_bankrupt_days-mc.business.bankrupt_days
                renpy.say(None,"Warning! Your company is losing money and unable to pay salaries or purchase necessary supplies! You have [days_remaining] days to restore yourself to positive funds or you will be foreclosed upon!")
        else:
            mc.business.bankrupt_days = 0
    return

label advance_time_random_crisis_label():
    # "advance_time_random_crisis_label - timeslot [time_of_day]" #DEBUG
    $ crisis = get_crisis_from_crisis_list()
    if crisis:
        #$ mc.log_event("General [[" + str(builtins.len(possible_crisis_list)) + "]: " + crisis.name, "float_text_grey")
        $ crisis_chance = crisis_base_chance
        call expression crisis.effect pass (*crisis.args) from _call_random_crisis_advance_time
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        $ add_to_debug_log(f"Random crisis: {remove_display_tags(crisis.name)}")
        $ crisis = None
    $ mc.location.show_background()
    return

label advance_time_mandatory_crisis_label():
    # "advance_time_mandatory_crisis_label - timeslot [time_of_day]" #DEBUG
    python:
        renpy.dynamic(
            mandatory_list = get_sorted_active_and_filtered_mandatory_crisis_list(mc.business.mandatory_crises_list),
            crisis_count = 0,
            mandatory_crisis = None
        )

    while mandatory_list and crisis_count < builtins.len(mandatory_list):
        $ mandatory_crisis = mandatory_list[crisis_count]
        # check if condition is still valid, a mandatory event might invalidate the conditions
        if mandatory_crisis and mandatory_crisis.is_action_enabled():
            # remove from main list before we trigger
            if mandatory_crisis in mc.business.mandatory_crises_list: # extra check to see if crisis still in list
                $ mc.business.remove_mandatory_crisis(mandatory_crisis) #Clean up the list.
            call expression mandatory_crisis.effect pass (*mandatory_crisis.args) from _call_mandatory_crisis_advance_time
            if _return == "Advance Time":
                $ mandatory_advance_time = True

            python:
                add_to_debug_log(f"Mandatory crisis: {remove_display_tags(mandatory_crisis.name)}")
                clear_scene()
                mandatory_event = True
        $ crisis_count += 1

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
    return

label advance_time_people_run_turn_label():
    # "advance_time_people_run_turn_label - timeslot [time_of_day]" #DEBUG
    python:
        renpy.suspend_rollback(True)
        renpy.not_infinite_loop(10)
        mandatory_advance_time = False
        advance_time_run_turn()
        renpy.suspend_rollback(False)
    return

label advance_time_people_run_day_label():
    # "advance_time_people_run_day_label - timeslot [time_of_day]" # DEBUG
    python:
        renpy.suspend_rollback(True)
        renpy.not_infinite_loop(10)
        advance_time_run_day()

        # update party schedules once a week (sunday night)
        if day%7 == 6:
            update_party_schedules()
        renpy.suspend_rollback(False)
    return

label advance_time_end_of_day_label():
    python:
        #$ renpy.profile_memory(.5, 1024)
        renpy.block_rollback()
        # start selecting new outfits for the next day using outfit_thread
        queue_outfit_changes()

    # "advance_time_end_of_day_label - timeslot [time_of_day]" # DEBUG
    if not persistent.skip_end_of_day:
        call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.

    python:
        # renpy.restart_interaction()
        mc.business.clear_messages()
        # increase morning crisis chance (once a day)
        morning_crisis_chance += builtins.len(people_in_mc_home())

        mc.business.funds_yesterday = mc.business.funds
    return

label advance_time_mandatory_morning_crisis_label():
    # "advance_time_mandatory_morning_crisis_label  - timeslot [time_of_day]" # DEBUG
    #"advance_time_mandatory_morning_crisis_label" #DEBUG
    #Now we run mandatory morning crises. Nearly identical to normal crises, but these always trigger at the start of the day (ie when you wake up and before you have control of your character.)
    python:
        renpy.dynamic(
            mandatory_morning_list = get_sorted_active_and_filtered_mandatory_crisis_list(mc.business.mandatory_morning_crises_list),
            crisis_count = 0,
            mandatory_morning_crisis = None
        )

    while mandatory_morning_list and crisis_count < builtins.len(mandatory_morning_list):
        $ mandatory_morning_crisis = mandatory_morning_list[crisis_count]
        # check if condition is still valid, a mandatory event might invalidate the conditions
        if mandatory_morning_crisis.is_action_enabled():
            # remove from main list before we trigger
            if mandatory_morning_crisis in mc.business.mandatory_morning_crises_list:
                $ mc.business.remove_mandatory_crisis(mandatory_morning_crisis) #Clean up the list.

            call expression mandatory_morning_crisis.effect pass (*mandatory_morning_crisis.args) from _call_mandatory_morning_crisis_advance_time
            if _return == "Advance Time":
                $ mandatory_advance_time = True

            python:
                add_to_debug_log(f"Mandatory morning crisis: {remove_display_tags(mandatory_morning_crisis.name)}")
                clear_scene()
                mandatory_event = True
        $ crisis_count += 1

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
    return

label advance_time_random_morning_crisis_label():
    # "advance_time_random_morning_crisis_label  - timeslot [time_of_day]" #DEBUG
    $ crisis = get_morning_crisis_from_crisis_list()
    if crisis:
        $ start_time = time.time()
        #$ mc.log_event("Morning: [[" + str(builtins.len(possible_morning_crises_list)) + "] : " +  crisis.name, "float_text_grey")
        $ morning_crisis_chance = morning_crisis_base_chance
        call expression crisis.effect pass (*crisis.args) from _call_random_morning_crisis_advance_time
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        $ add_to_debug_log(f"Random morning crisis: {remove_display_tags(crisis.name)}")
        $ crisis = None
    $ mc.location.show_background()
    return

label advance_time_next_day_label():
    # "advance_time_next_day_label  - timeslot [time_of_day]" #DEBUG
    python:
        if time_of_day == 4: # NOTE: Take care of resetting it to 0 here rather than during end_day_label
            time_of_day = 0
            day += 1
        else:
            time_of_day += 1 ##Otherwise, just run the end of day code.
        mc.recently_orgasmed = False # reset on timeslot change
    return

label advance_time_people_run_move_label():
    python:
        renpy.suspend_rollback(True)
        renpy.not_infinite_loop(10)
        # "advance_time_people_run_move_label - timeslot [time_of_day]" #DEBUG
        advance_time_run_move()
        advance_time_assign_limited_time_events()
        advance_time_check_location_accessibility()
        renpy.suspend_rollback(False)
    return

label advance_time_update_progression_scenes_label():
    python:
        advance_time_update_progression_scenes()
    return
