label progression_scene_label(progression_scene, the_group):
    #First, add the event back so that it recurs. For a role event, leave these two properties false.
    if progression_scene.business_action:
        $ mc.business.add_mandatory_crisis(progression_scene.progression_scene_action)
    if progression_scene.person_action:
        $ the_group[0].add_unique_on_room_enter_event(progression_scene.progression_scene_action)

    # If the stage is -1, it has not been run before. Call the intro.
    if progression_scene.stage == -1:
        $ progression_scene.stage = 0
        # "Progressions stage should now be 0"

        if progression_scene.intro_scene:
            $ progression_scene.call_intro(the_group)
            if progression_scene.is_multiple_choice:    #IF it is multiple choice, add the basic scene to the list of options.
                $ progression_scene.scene_unlock_list.append(0)
            if progression_scene.advance_time:
                python:
                    for x in the_group:
                        x.apply_serum_study()
                call advance_time() from _call_advance_progression_scene_class_02
            return
        #If there isn't an intro scene, just play the [0] scene

    #First, play the start scene
    $ progression_scene.call_start_scene(the_group)
    #Allow players to opt out
    $ progression_scene.call_choice_scene(the_group)
    if not _return:
        $ progression_scene.call_exit_scene(the_group)
        return

    $ scene_transition = False    #pass in to the final scene if we played a transition or not. It may change the final scene.

    #If the scene is multiple choice, check and see if we unlocked any new "choices"
    if progression_scene.is_multiple_choice:
        $ counter = 0
        $ scene_choice = None
        python:
            while counter < len(progression_scene.trans_list):
                if counter not in progression_scene.scene_unlock_list:
                    if progression_scene.req_list[counter]():
                        progression_scene.scene_unlock_list.append(counter)
                        scene_transition = True
                        scene_choice = counter
                        progression_scene.call_multi_trans_scene(the_group, counter)
                        break
                counter += 1

        if not scene_transition:    #If we didn't unlock any new choices, let player choose what scene to play in multiple choice scene.
            $ progression_scene.call_multiple_choice_scene(the_group)
            $ scene_choice = _return

        #Now play the final scene
        $ progression_scene.call_multi_final_scene(the_group, scene_transition, scene_choice)



    else:
        #if it is linear progression, first check if we can progress this scene.
        if len(progression_scene.req_list) > progression_scene.stage + 1: #Only try if there is another scene
            if progression_scene.req_list[progression_scene.stage + 1]():
                $ progression_scene.stage = progression_scene.stage + 1
                $ progression_scene.call_trans_scene(the_group)
                $ scene_transition = True
        #If the scene can regress, check and see if we need to regress a step
        if not progression_scene.is_progress_only() and progression_scene.stage != 0:
            if not progression_scene.req_list[progression_scene.stage](the_group):
                $ progression_scene.stage = progression_scene.stage - 1
                $ progression_scene.call_regress_scene(the_group)
                $ scene_transition = True

        #Call the appropriate final scene.
        $ progression_scene.call_final_scene(the_group, scene_transition)
    if progression_scene.advance_time:
        python:
            for x in the_group:
                x.apply_serum_study()
        call advance_time(no_events = True) from _call_advance_progression_scene_class_01
    return

label progression_scene_stage_test_label(progression_scene, the_group):
    "This is a unit test for [progression_scene.name] scene."
    "First, I'll load each person in the group for you to modify stats."
    $ count = 0
    $ the_stage
    while count < len(the_group):
        $ the_person = the_group[count]
        "[the_person.title] is now loaded as the person."
        "Please use the cheat menu to set to appropriate stats you want to test them at."
        "Done? Okay moving on to the next one."
        $ count += 1
    "Okay, now I'll attempt to let you set the event stage."
    "Note: this will reset progress on this scene in this save file."
    "Note: This menu does nothing for multiple choice scenes. If you are testing a multiple choice scene, I recommend setting their stats and just calling the scene over and over."
    "Note, if you have a large number of stages, you might have to go and edit this scene to make it possible to see them all here."
    "This label is at the bottom of progression_scene.rpy found in mods/core/helper_functions !"
    "What stage should we set the event to?"
    menu:
        "-1":
            $ the_stage = -1
        "0":
            $ the_stage = 0
        "1" if len(progression_scene.req_list) > 1:
            $  the_stage = 1
        "2" if len(progression_scene.req_list) > 2:
            $  the_stage = 2
        "3" if len(progression_scene.req_list) > 3:
            $  the_stage = 3
        "4" if len(progression_scene.req_list) > 4:
            $  the_stage = 4
        "5" if len(progression_scene.req_list) > 5:
            $  the_stage = 5
        "6" if len(progression_scene.req_list) > 6:
            $  the_stage = 6
        "7" if len(progression_scene.req_list) > 7:
            $  the_stage = 7
        "8" if len(progression_scene.req_list) > 8:
            $  the_stage = 8
        "9" if len(progression_scene.req_list) > 9:
            $  the_stage = 9
        "10" if len(progression_scene.req_list) > 10:
            $  the_stage = 10
        "11" if len(progression_scene.req_list) > 11:
            $  the_stage = 11
    $ progression_scene.stage = the_stage
    "Okay, here we go!"
    $ progression_scene.call_scene(the_group)
    "Unit test complete?"
    return
