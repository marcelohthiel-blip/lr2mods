label lily_study_buddy_best_friend(the_sister, the_person):
    if not mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"] = []
        $ mc.business.event_triggers_dict["study_recordings"].append("1. Friend Recording")
    if "2. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"].append("2. Friend Recording")
    if the_person.event_triggers_dict.get("anger", 1) > 0:
        call study_friend_transition(the_sister, the_person) from _call_study_friend_transition
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 1:
        $ the_person.event_triggers_dict["friend_with_benefits"] = 1
        call lily_first_best_friend(the_sister, the_person) from _call_lily_first_best_friend
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 2:
        $ the_person.event_triggers_dict["friend_with_benefits"] = 2
        call lily_second_best_friend(the_sister, the_person) from _call_lily_second_best_friend
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 3:
        $ the_person.event_triggers_dict["friend_with_benefits"] = 3
        call lily_third_best_friend(the_sister, the_person) from _call_lily_third_best_friend
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 8:
        call lily_buddy_date_label() from _call_lily_buddy_date_label_bf
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 13:
        call lily_buddy_corruption_label() from _call_lily_buddy_corruption_label_bf
    else:
        call lily_buddy_threesome_label() from _call_lily_buddy_threesome_label_bf
    return

label best_friend_test():
    $ the_sister = lily
    $ the_person = get_lab_partner()
    $ stop = False
    while not stop:
        if the_person.event_triggers_dict.get("anger", 1) > 0:
            call study_friend_transition(the_sister, the_person)
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 1:
            $ the_person.event_triggers_dict["friend_with_benefits"] = 1
            call lily_first_best_friend(the_sister, the_person)
            call lily_first_followup_label()
            call lily_first_followup_morning()
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 2:
            $ the_person.event_triggers_dict["friend_with_benefits"] = 2
            call lily_second_best_friend(the_sister, the_person)
            call lily_second_followup_label()
            call lily_second_followup_loop_label()
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 3:
            $ the_person.event_triggers_dict["friend_with_benefits"] = 3
            call lily_third_best_friend(the_sister, the_person)
            call lily_third_followup_label()
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 100: #find end point
            call lily_buddy_date_label()
        else:
            "Unsurprisingly you do not get a visit during [the_sister.possessive_title]'s study time with [the_person.title]."
            if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 50:
                call lily_offscreen_corruption(the_sister, the_person)
                "You do occasionally hear the murmur of them talking. Maybe you should try to find a way to spy on their dates in the future."
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 70:
                call lesbian_sex(the_sister, the_person)
                "You do occasionally hear what could be muffled moans. Some kind of spy camera is definitely sounding like a good investment."
            else:
                call lesbian_sex(the_sister, the_person)
                $ (sister_orgasm, person_orgasm) = _return
                "From time to time you hear a bed squeaking and once or twice it crashes into the wall. When it does there is some giggling followed by extreme silence."
                "You wonder if they really think their activities are going unnoticed, and once again wish you had picked up a camera."
            if (sister_orgasm + other_orgasm) < 1 and the_person.event_triggers_dict.get("friend_with_benefits", 0) > 80:
                $ best_friend_threesome = Action("Best Friend Threesome", lily_followup_requirement, "best_friend_threesome_label")
                $ mc.business.add_mandatory_crisis(best_friend_threesome)
            elif sister_orgasm < 1:
                $ lily_overnight = Action("Lily Overnight", lily_followup_requirement, "lily_overnight_label")
                $ mc.business.add_mandatory_crisis(lily_overnight)
            elif person_orgasm < 1:
                $ best_friend_overnight = Action("Best Friend Overnight", lily_followup_requirement, "best_friend_overnight_label")
                $ mc.business.add_mandatory_crisis(best_friend_overnight)
            $ the_person.event_triggers_dict["friend_with_benefits"] += (sister_orgasm + other_orgasm)*5
            $ the_other_person.event_triggers_dict["friend_with_benefits"] += (sister_orgasm + other_orgasm)*5
        menu:
            "Continue":
                pass
            "Stop":
                $ stop = True
    return
