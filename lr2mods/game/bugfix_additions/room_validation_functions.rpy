init 10 python:
    add_label_hijack("normal_start", "validate_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

    def fix_duplicate_objects_in_rooms():
        for room in list_of_places:
            unique = list(set(room.objects))
            if len(unique) != len(room.objects):    # mismatch update
                room.objects = unique
        return

    def update_room_visibility():
        remove_list = []
        for i in range(0, len(list_of_places) - 1):
            for j in range(i + 1, len(list_of_places)):
                if not list_of_places[j] in remove_list:
                    if i == j:
                        remove_list.append(list_of_places[j])

        if len(remove_list) > 0:
            for room in remove_list:
                renpy.say("Warning", f"Duplicate room {room.name}, game is corrupt, you are advised to start a new game.")

        return

label update_custom_rooms(stack):
    python:
        update_room_visibility()
        fix_duplicate_objects_in_rooms()

        execute_hijack_call(stack)
    return

label validate_custom_rooms(stack):
    # extra code run after creation of all rooms
    python:
        # initialize dungeon room creation action
        fix_duplicate_objects_in_rooms()

        execute_hijack_call(stack)
    return
