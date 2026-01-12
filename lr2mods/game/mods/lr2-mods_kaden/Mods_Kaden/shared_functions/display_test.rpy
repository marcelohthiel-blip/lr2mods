init -1 python:
    # person
    # outfit
    # position
    # emotion ["default", "happy", "sad", "angry", "orgasm"]
    # special_modifier ["kissing", "blowjob"]
    # lighting
    # display_transform
        # xoffset
        # yoffset
        # zoom
        # rotate
    # z_order (#)
    def get_person_number(person, person_list):
        number = 0
        for x in person_list:
            if x == person:
                return number
            number += 1
        return 0

    def build_position_menu():
        temp_list = []
        for x in ["stand2","stand3","stand4","stand5", "walking_away", "back_peek", "sitting", "kissing", "doggy", "missionary", "blowjob", "against_wall", "standing_doggy", "kneeling1", "cowgirl"]:
            temp_list.append(x)
        return temp_list

    def build_emotion_list():
        temp_list = []
        for x in ["default", "happy", "sad", "angry", "orgasm"]:
            temp_list.append(x)
        return temp_list

    def build_transform_menu():
        temp_list = []
        for x in [["character_right", ["character_right", character_right]], 
            ["character_right_flipped", ["character_right_flipped", character_right_flipped]], 
            ["character_center", ["character_center", character_center]], 
            ["character_center_flipped", ["character_center_flipped", character_center_flipped]], 
            # ["character_center_focus", character_center_focus], 
            # ["character_center_focus_flipped", character_center_focus_flipped], 
            ["character_left", ["character_left", character_left]], 
            ["character_left_flipped", ["character_left_flipped", character_left_flipped]], 
            ["character_far_left_flipped", ["character_far_left_flipped", character_far_left_flipped]],
            ["character_69_bottom", ["character_69_bottom", character_69_bottom]],
            ["character_69_on_top", ["character_69_on_top", character_69_on_top]]]:
            temp_list.append(x)
        return temp_list

    def display_test_initialization(self):
        clothing_store.add_action(display_test_action)
        return

    def display_test_requirement():
        return True

    display_test_action = ActionMod("DEV: Display Test", display_test_requirement, "display_test", menu_tooltip = "Test settings to build a scene with 1 or more girls", initialization = display_test_initialization)

label display_test():
    $ scene_manager = Scene()
    $ done = False
    $ more_people = True
    $ temp_number = 0
    $ x_offset = 0
    $ person_list = []
    $ scene_list = []
    while not done:
        while more_people:
            call screen main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game(), "Pick a person", "Back")]))
            $ person_choice = _return
            if person_choice == "Back":
                $ more_people = False
            else:
                $ person_list.append(person_choice)
                $ scene_manager.add_actor(person_choice, display_transform = character_center(xoffset = x_offset))
                menu:
                    "Add another":
                        pass
                    "Proceed":
                        $ more_people = False
        while temp_number < len(person_list):
            $ scene_list.append([person_list[temp_number], "stand2", "happy", None, ["character_center", character_center], "0", "0", "1", "0", str(temp_number)])
            $ person_dict = scene_list[get_person_number(person_list[temp_number], person_list)]
            $ scene_manager.update_actor(person_dict[0], position = person_dict[1], emotion = person_dict[2], special_modifier = person_dict[3], display_transform = person_dict[4][1](xoffset = float(person_dict[5]) - temp_number/10.0, yoffset = float(person_dict[6]), zoom = float(person_dict[7])), z_order = float(person_dict[9]))
            $ temp_number +=1
        
        call screen main_choice_display(build_menu_items([get_sorted_people_list(person_list, "Pick a person", "Back")]))
        $ person_choice = _return
        if person_choice == "Back":
            $ done = True
        else:
            $ person_number = get_person_number(person_choice, person_list)
            $ person_dict = scene_list[person_number]
            $ done_with_person = False
            $ temp_adjust = None
            $ scene_manager.update_actor(person_dict[0], position = person_dict[1], emotion = person_dict[2], special_modifier = person_dict[3], display_transform = person_dict[4][1](xoffset = float(person_dict[5]), yoffset = float(person_dict[6]), zoom = float(person_dict[7])), z_order = float(len(person_list)+1))
            "draw_person([person_dict[0].name], position = [person_dict[1]], emotion = [person_dict[2]], special_modifier = [str(person_dict[3])], display_transform = [person_dict[4][0]])(xoffset = [person_dict[5]], yoffset = [person_dict[6]], zoom = [person_dict[7]]), z_order = [person_dict[9]]"
            while not done_with_person:
                if not temp_adjust:
                    menu:
                        "Position":
                            $ temp_adjust = "Position"
                        "Emotion":
                            $ temp_adjust = "Emotion"
                        "Display Transform":
                            $ temp_adjust = "Transform"
                        "Xoffset":
                            $ temp_adjust = "Xoffset"
                        "Yoffset":
                            $ temp_adjust = "Yoffset"
                        "Zoom":
                            $ temp_adjust = "Zoom"
                        "Back":
                            $ temp_adjust = None
                            $ done_with_person = True
                while temp_adjust:
                    if temp_adjust == "Position":
                        $ temp_list = build_position_menu()
                        call screen main_choice_display(build_menu_items([["Pick a position"] + temp_list + ["Back"]]))
                        $ temp_position = _return
                        if temp_position != "Back":
                            $ scene_list[person_number][1] = temp_position
                        else:
                            $ temp_adjust = None
                    elif temp_adjust == "Emotion":
                        $ temp_list = build_emotion_list()
                        call screen main_choice_display(build_menu_items([["Pick an emotion"] + temp_list + ["Back"]]))
                        $ temp_emotion = _return
                        if temp_emotion != "Back":
                            $ scene_list[person_number][2] = temp_emotion
                        else:
                            $ temp_adjust = None
                    elif temp_adjust == "Transform":
                        $ temp_list = build_transform_menu()
                        call screen main_choice_display(build_menu_items([["Pick a transform"] + temp_list + ["Back"]]))
                        $ temp_transform  = _return
                        if temp_transform != "Back":
                            $ scene_list[person_number][4] = temp_transform
                        else:
                            $ temp_adjust = None
                    elif temp_adjust == "Xoffset":
                        $ amount = renpy.input("Move left (negative) or right (positive). Typically < 1.00, currently [scene_list[person_number][5]] (repeat to return)", default = str(scene_list[person_number][5]), allow = "-.0123456789") 
                        if scene_list[person_number][5] == amount:
                            $ temp_adjust = None
                        $ scene_list[person_number][5] = amount
                    elif temp_adjust == "Yoffset":
                        $ amount = renpy.input("Move down (negative) or up (positive). Typically < 1.00, currently [scene_list[person_number][6]] (repeat to return)", default = str(scene_list[person_number][6]), allow = "-.0123456789") 
                        if scene_list[person_number][6] == amount:
                            $ temp_adjust = None
                        $ scene_list[person_number][6] = amount
                    elif temp_adjust == "Zoom":
                        $ amount = renpy.input("Get smaller (negative) or bigger (positive). Typically ~ 1.00, currently [scene_list[person_number][7]] (repeat to return)", default = str(scene_list[person_number][7]), allow = "-.0123456789") 
                        if scene_list[person_number][7] == amount:
                            $ temp_adjust = None
                        $ scene_list[person_number][7] = amount
                    else:
                        $ temp_adjust = None
                    if temp_adjust:
                        $ scene_manager.update_actor(person_dict[0], position = person_dict[1], emotion = person_dict[2], special_modifier = person_dict[3], display_transform = person_dict[4][1](xoffset = float(person_dict[5]), yoffset = float(person_dict[6]), zoom = float(person_dict[7])), z_order = float(len(person_list)+1))
                        "draw_person([person_dict[0].name], position = [person_dict[1]], emotion = [person_dict[2]], special_modifier = [str(person_dict[3])], display_transform = [person_dict[4][0]])(xoffset = [person_dict[5]], yoffset = [person_dict[6]], zoom = [person_dict[7]]), z_order = [person_dict[9]]"
    return
