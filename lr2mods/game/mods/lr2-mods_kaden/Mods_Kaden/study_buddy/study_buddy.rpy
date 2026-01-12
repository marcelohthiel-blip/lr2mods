init -1 python:
    def study_buddy_nora_requirement(person):
        if lily.has_job(sister_student_job):
            if mc.business.event_triggers_dict.get("knows_study_day", False):
                if time_of_day < 3:
                    return True
        return False

    def study_buddy_prep_requirement(): # monday morning
        if lily.has_job(study_buddy_job) and get_lab_partner():
            if lily.is_available and get_lab_partner().is_available:
                if day%7 == 0 and time_of_day == 0:
                        return True
        return False

    def study_buddy_serum_requirement(person):
        return person.location == lily.location and time_of_day == 3 and day%7 == 0

    def lily_followup_requirement():
        if time_of_day > 3:
            if lily.is_available:
                return True
        return False

    def lily_mon_followup_requirement():
        if day%7 == 0:
            if time_of_day > 3:
                if lily.is_available:
                    return True
        return False

    def buddy_followup_requirement(the_person):
        return the_person.is_at_work

    def rival_int_chat_requirement(person):
        return 0 < time_of_day < 4

    def lily_classmates():
        classmates = []
        for person in known_people_in_the_game(excluded_people = [lily]):
            if person.has_role(generic_student_role):
                classmates.append([person.name, person])
        return classmates

    def get_lab_partner():
        if lily.has_job(study_buddy_job):
            students = []
            for person in known_people_in_the_game(excluded_people = [lily]):
                if person.has_job(study_buddy_job):
                    return person
            for person in known_people_in_the_game(excluded_people = [lily]):
                if person.has_role(generic_student_role):
                    students.append(person)
            if students:
                person = get_random_from_list(students)
                person.set_side_job(study_buddy_job)
                if not town_relationships.get_relationship(person, lily):
                    town_relationships.begin_relationship(person, lily)
                return person
        return

    def lily_willing_threesome():
        if Person.get_person_by_identifier(sarah.event_triggers_dict.get("initial_threesome_target", None)) == the_sister:
            return True
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            return True
        if "threesome" in erica_get_wakeup_options():
            return True
        if lily.sex_record.get("threesomes", 0) > 0:
            return True
        return False

    def study_date_trigger(day_of_week):
        if time_of_day == 3 and day % 7 == day_of_week: #Day of week is a number from 0 to 6, where 0 is Monday.
            return True
        return False


    study_buddy_serum_action = Action("Study buddy serum", study_buddy_serum_requirement, "study_buddy_serum_label")
    study_buddy_date_action = Action("Study buddy date", study_date_trigger, "study_buddy_date_label", requirement_args=0) #it happens on a monday
    study_buddy_prep_action = Action("Study buddy prep", study_buddy_prep_requirement, "study_buddy_prep_label")

    study_buddy_test_action = Action("Study Buddy Test", kaden_test_req, "study_buddy_test", menu_tooltip = "Meet study buddy. Chat with Nora. Dose Studdy session. Have the Study Buddy drop by.")

    def study_buddy_mod_initialization():
        global study_buddy_role
        study_buddy_role = Role("Study Buddy", [], hidden = True)
        global study_buddy_job
        study_buddy_job = JobDefinition("Study Buddy", study_buddy_role, job_location = lily_bedroom, day_slots = [0], time_slots = [3], wardrobe = limited_university_wardrobe)
        global study_buddy_nora_action
        study_buddy_nora_action = Action("Talk to [nora.fname] about [lily.fname]'s lab partner", study_buddy_nora_requirement, "study_buddy_nora_label", menu_tooltip = "Talk to Nora about Lily's lab partner.")
        nora.get_role_reference("nora").add_action(study_buddy_nora_action)
        mc.business.add_mandatory_crisis(study_buddy_prep_action)
        lily_bedroom.add_action(college_girl_test_action)
        lily_bedroom.add_action(study_buddy_test_action)
        lily_bedroom.add_action(friend_test_action)

init 16 python: # hijack
    add_label_hijack("normal_start", "activate_study_buddy_mod_core")
    add_label_hijack("after_load", "update_study_buddy_mod_core")

label activate_study_buddy_mod_core(stack):
    python:
        study_buddy_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_study_buddy_mod_core(stack):
    python:
        if "study_buddy_job" not in globals():
            study_buddy_mod_initialization()
        execute_hijack_call(stack)
    return

label study_buddy_nora_label(the_teacher):
    $ the_teacher = nora
    $ the_sister = lily
    $ the_other_person = get_lab_partner()
    if not the_other_person:
        return
    $ change = True
    mc.name "I was hoping to talk to you about [the_sister.fname]'s current lab partner."
    the_teacher "Oh, you mean [the_other_person.fname]? Is something wrong?"
    if not town_relationships.get_relationship(the_other_person, the_sister):
        $ town_relationships.begin_relationship(the_other_person, the_sister)
    if town_relationships.get_relationship(the_other_person, the_sister).type_a =="Rival" or town_relationships.get_relationship(the_other_person, the_sister).type_a =="Nemesis":
        mc.name "Yeah, actually. They really don't get along, and I am worried that it is making it hard for them to agree on the way they should do things."
    elif town_relationships.get_relationship(the_other_person, the_sister).type_a =="Friend" or town_relationships.get_relationship(the_other_person, the_sister).type_a =="Best Friend":
        mc.name "Kind of, they are friends. Usually that would be great, but they've been spending more time chatting than working and I'm worried about it impacting [the_sister.fname]'s grades."
    else:
        mc.name "Not really, but I was thinking that she could have a better partner to really shine in your class."
    the_teacher "That makes sense, but I can't just go changing lab partners in the middle of the semester."
    mc.name "Surely you've had to do it in the past."
    the_teacher "Occasionally. I should have said I can't change them without a reason. A good one, not just because someone asks."
    if the_teacher.love > 50:
        mc.name "Someone huh, I didn't think I was just someone to you."
        if the_teacher.is_girlfriend:
            the_teacher "That's not what I meant, you know I love you [the_teacher.mc_title]."
        else:
            the_teacher "I know we've been getting close, but I can't let every fling impact my career."
        mc.name "This is important to me, and any chance we have at a future is going to involve my sister. Surely you want her to be happy as much as I do."
        the_teacher "Okay, let me see if I can move people around a bit."
    elif the_teacher.obedience > 160:
        mc.name "Sorry, I wasn't really asking. I need you to do this for me."
        the_teacher "Yes [the_teacher.mc_title]. Sorry, I sometimes forget myself in teacher mode."
    else:
        mc.name "What if I could find a way to make it worth your while?"
        the_teacher "I suppose a sizable grant for my research would necessitate some reorganization of class groups to allow me to focus on other priorities."
        menu:
            "Give her\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}" if mc.business.funds >= 5000:
                mc.name "Well I think we could arrange something along those lines. What do you think you'll need?"
                the_teacher "I imagine that $5000 would be enough to require me to shift focus, maybe bring in another teaching assistant."
                mc.name "I can certainly handle that."
                $ mc.business.change_funds(-5000)
                "You hand over the funds and she tucks them into her purse."
            "Reconsider":
                $ change = False
                mc.name "What do you think it would take to justify something like that?"
                the_teacher "I imagine that $5000 would be enough to require me to shift focus, maybe bring in another teaching assistant."
                mc.name "That's a bit steeper than I was hoping."
                the_teacher "Sorry, [the_teacher.mc_title], but I don't think I can justify something like this without a reason."
                mc.name "I understand, I'll get back to you if something changes."
            "Give her\n{color=#ff0000}{size=18}Requires: $5000{/size}{/color} (disabled)" if mc.business.funds < 5000:
                pass
    if change:
        "[the_teacher.title] pulls out her planner, flipping through to find [the_sister.fname]'s class."
        the_teacher "Who would you like your sister to be partnered with from now on?"
        call screen main_choice_display(build_menu_items([["Pick Lab Partner"] + lily_classmates()], draw_hearts_for_people = True))
        $ choice = _return
        mc.name "I think it would be best if she was partnered with [choice.fname]."
        $ the_other_person.quit_job(study_buddy_job)
        if the_other_person.is_favourite:
            $ the_other_person.toggle_favourite()
        $ choice.set_side_job(study_buddy_job)
        if not choice.is_favourite:
            $ choice.toggle_favourite()
        if day%7 == 0:
            call study_buddy_prep_label from _call_study_buddy_prep_label_nora
        the_teacher "Alright, I'll let them know the next time that we have class."
        mc.name "Thank you [the_teacher.title], I knew I could count on you to help me and my sister."
        the_teacher "Of course, is there anything else you need?"
    return

label study_buddy_prep_label():
    $ mc.business.add_mandatory_crisis(study_buddy_date_action)
    $ the_person = get_lab_partner()
    $ test_outfit = limited_university_wardrobe.decide_on_outfit(the_person, sluttiness_modifier = the_person.love/5)
    $ the_panties = test_outfit.get_panties()
    $ the_bra = test_outfit.get_bra()
    if the_person.event_triggers_dict.get("bedroom_tax", 0) > 1:
        if the_panties:
            if the_panties.is_extension: #two piece item
                $ test_outfit.remove_clothing(the_bra)
                $ the_bra = None
            else:
                $ test_outfit.remove_clothing(the_panties)
    else:
        if not the_panties:
            $ test_outfit.add_lower(panties.get_copy(),colour_white)
    if the_person.event_triggers_dict.get("bedroom_tax", 0) > 4:
        if the_bra:
            $ test_outfit.remove_clothing(the_bra)
    else:
        if not the_bra:
            $ test_outfit.add_upper(bra.get_copy(),colour_white)
    $ the_person.planned_outfit = test_outfit
    $ test_outfit = limited_university_wardrobe.decide_on_outfit(lily)
    if len(test_outfit.get_upper_ordered()) > 2:
        $ test_outfit.remove_clothing(test_outfit.get_upper_top_layer)
    $ lily.planned_outfit = test_outfit
    if mc.business.event_triggers_dict.get("knows_study_day", False):
        $ the_person.add_unique_on_room_enter_event(study_buddy_serum_action)
    if not town_relationships.get_relationship(the_person, lily):
        $ town_relationships.begin_relationship(the_person, lily)
    return

label study_buddy_serum_label(the_person):
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_person.apply_planned_outfit()
    $ the_sister = lily
    $ the_sister.apply_planned_outfit()
    if town_relationships.get_relationship(the_person, the_sister).type_a =="Best Friend":
        if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 14:
            "[the_person.title] and [the_sister.title] have started to include you in their adventures. Perhaps you could give them some drinks laced with serums make it even more rewarding.."
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) > 9:
            "[the_person.title] are [the_sister.title] are having great sex, thanks to you. Perhaps you could give them some drinks laced with serums push them even further."
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) > 6:
            "[the_person.title] and [the_sister.title] having sex, with mixed results. Perhaps you could give them some drinks laced with serums to help them along."
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) > 3:
            "[the_person.title] and [the_sister.title] are fooling around a bit. Perhaps you could give them some drinks laced with serums to help them along."
        elif the_person.event_triggers_dict.get("friend_with_benefits", 0) > 0:
            "[the_person.title] is working on figuring things out with [the_sister.title]. Perhaps you could give them some drinks laced with serums to help them along."
        elif the_person.event_triggers_dict.get("anger", -1) > -1:
            "Things are a bit weird with [the_person.title] since she broke up with you, but you could still stop by with serum laced drinks."
    elif the_person.event_triggers_dict.get("study_sessions", 0) < 1:
        "Typically you could expect a visit from [the_sister.fname]'s lab partner, but thanks to you she has a new one this week."
        if mc.inventory.total_serum_count > 0:
            "Expecting them to be hard at work you decide to just head to the kitchen and grab some drinks to bring up."
    else:
        "You can expect a visit from [the_person.title] sometime this evening."
        if mc.inventory.total_serum_count > 0:
            "Before that happens you want to take the opportunity to give her and [the_sister.possessive_title] a serum, so you head down to the kitchen and grab some drinks."
    if mc.inventory.total_serum_count > 0:
        $ mc.change_location(kitchen)
        menu:
            "Add serum to [the_person.title]'s drink" if mc.inventory.total_serum_count > 0:
                call give_serum(the_person) from _call_give_serum_new_study_buddy
                if _return:
                    "You add a dose to her drink, then top it off with water."
                else:
                    "You think about adding a dose of serum to her drink, but decide against it."
            "Add serum to [the_person.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                pass
            "Leave her drink alone":
                "You top it off with water."
        menu:
            "Add serum to [the_sister.title]'s drink" if mc.inventory.total_serum_count > 0:
                call give_serum(the_sister) from _call_give_serum_new_study_buddy2
                if _return:
                    "You add a dose to her drink, then top it off with water."
                else:
                    "You think about adding a dose of serum to her drink, but decide against it."
            "Add serum to [the_sister.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                pass
            "Leave her drink alone":
                "You top it off with water."
        "With your hands full you announce yourself as you approach the door."
        if the_person.event_triggers_dict.get("study_sessions", 0) < 1:
            mc.name "Oh, hello [the_person.fname]! I'm surprised to see you here today."
        else:
            mc.name "Hey girls, I brought you some water. Hard at work on your project?"
    else:
        if the_person.event_triggers_dict.get("study_sessions", 0) < 1:
            "You decide to stop in and say hello briefly."
            "When you get to the door you knock on the door frame and see [the_sister.title] and [the_person.title] turn to greet you."
        else:
            "Before that you figure you can stop and say hello briefly."
            "When you get to the door you knock on the door frame and see [the_sister.title] and [the_person.title] turn to greet you."
    if the_person.event_triggers_dict.get("study_sessions", 0) < 1:
        $ mc.change_location(lily_bedroom)
        $ scene_manager.add_actor(the_person, display_transform = character_left_flipped, position = "stand3", emotion = "happy")
        $ scene_manager.add_actor(the_sister, position = "stand3", emotion = "happy")
        if town_relationships.get_relationship(the_person, the_sister).type_a =="Friend":
            the_person "Hi, [the_person.mc_title], nice to see you again!"
        elif town_relationships.get_relationship(the_person, the_sister).type_a =="Rival":
            the_person "Quite the pleasant surprise isn't it?"
            mc.name "I must admit that it is."
        else:
            the_person "Hello again."
        mc.name "Isn't today usually the day when you work with your lab partner, [the_sister.fname]?"
        if mc.charisma > 4:
            "With acting skills worthy of Hollywood you deftly deliver your line."
        elif mc.charisma > 2:
            "Although you are neither surprised or confused you do a passable job of making it sound that way."
        else:
            "You can't help but feel like your question is a bit wooden, fortunately they don't seem to notice."
        the_sister "Professor [nora.last_name] came into class this week with a new TA and rearranged a bunch of lab partners."
        the_sister "She said something about how adapting to changing workplaces would be an important skill to learn."
        mc.name "Well that makes sense, sometimes I have to move people around at work as priorities shift between research and production."
        the_sister "Yeah, I suppose, it's just tough starting over when the two different groups were approaching the project in different ways."
        the_person "It is somewhat beneficial though because we now have access to four people's work up to this point, even if there is some overlap in what got done."
        if town_relationships.get_relationship(the_person, the_sister).type_a =="Friend":
            the_person "Plus it is great to be able to work with [the_sister.fname] so we can spend more time hanging out."
            the_sister "Yeah, that is a bonus, if we had gotten to pick partners to start with I would have wanted to work with you."
            mc.name "I'm glad this is working out for you."
        elif town_relationships.get_relationship(the_person, the_sister).type_a =="Rival":
            the_person "Of course my previous lab partner was more knowledgeable than [the_sister.fname], but over coming challenges is an important skill to learn too."
            the_sister "As if I'm going to be the one holding us back. If you spent more time studying I wouldn't need to spend so much explaining things to you as we work."
            mc.name "Hey now, it sounds like you might be stuck together, so you should at least try to be civil to each other."
        $ the_person.event_triggers_dict["study_sessions"] = 1
    else:
        $ mc.change_location(lily_bedroom)
        $ scene_manager.add_actor(the_person, display_transform = character_left_flipped, position = "stand3", emotion = "happy")
        $ scene_manager.add_actor(the_sister, position = "stand3", emotion = "happy")
        $ the_person.event_triggers_dict["study_sessions"] += 1
    "You chat with them a bit more about what their project is, and give some advice based off of your time spent with [nora.fname]."
    mc.name "I should probably let you get back to work. I'll be in my room for the night, early start tomorrow at work."
    $ scene_manager.clear_scene()
    call advance_time from _call_advance_study_buddy_serum
    return

label study_buddy_date_label():
    $ mc.business.add_mandatory_crisis(study_buddy_prep_action)
    $ skip_event = False
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_person.apply_planned_outfit()
    $ the_sister = lily
    $ the_sister.apply_planned_outfit()
    if not mc.business.event_triggers_dict.get("knows_study_day", False):
        call lily_first_study_buddy(the_sister, the_person) from _call_lily_first_study_buddy
    elif mc.location == lily_bedroom:
        "You clear out, and head to your room to pass some time before bed."
    else:
        "Today is the normal day for [the_sister.title] to study with her lab partner."
        if not mc.is_home:
            "Interacting with [the_person.title] is always a good way to spend an evening, of course if you have other plans you could always stay out until later tonight."
            menu:
                "Go home {image=gui/heart/Time_Advance.png}":
                    "You make the short trip home and put your things in your room."
                "Stay where you are":
                    "You decide not to head home today. There is always next week."
                    $ skip_event = True
        elif mc.location == lily_bedroom:
            pass
        else:
            "Interacting with [the_person.title] is always a good way to spend an evening, of course if you have other plans you could always go out until later tonight."
            menu:
                "Stay home {image=gui/heart/Time_Advance.png}":
                    "You decide to wait for [the_person.title] and head to your bedroom so she can find you."
                    pass
                "Go out":
                    "You make the short trip downtown and start looking around for something to pass the time."
                    $ mc.change_location(downtown)
                    $ skip_event = True
    if not skip_event:
        $ mc.change_location(bedroom)
        if the_person.event_triggers_dict.get("friend_with_benefits", 0) >= 2:
            call lily_study_buddy_best_friend(the_sister, the_person) from _call_lily_study_buddy_best_friend_date
        elif town_relationships.get_relationship(the_person, the_sister).type_a == "Nemesis":
            call lily_study_buddy_nemesis(the_sister, the_person) from _call_lily_study_buddy_nemesis_date
        else:
            call lily_study_buddy_visit(the_person) from _call_lily_study_buddy_visit
        "A bit of time passes, but you eventually hear the front door closing as [the_person.title] goes home for the night."
    if town_relationships.get_relationship(the_person, lily).type_a == "Rival":
        if the_person.event_triggers_dict.get("teasing_lily", 999) > the_person.obedience:
            $ rival_study_time = Action("Rival Study Time", lily_mon_followup_requirement, "rival_study_time_label")
            $ mc.business.add_mandatory_crisis(rival_study_time)
        else:
            $ the_person.event_triggers_dict["teasing_lily"] += 30
    $ scene_manager.clear_scene()
    return "Advance Time"

label lily_first_study_buddy(the_sister, the_person):
    if mc.is_home:
        "You are puttering around the house after a long day when you hear a surprising amount of noise coming from [the_sister.title]'s bedroom."
    elif mc.is_at_work:
        "It has been a long day and you are suddenly struck by the urge to go home for the night to relax."
        $ mc.change_location(bedroom)
        "A quick trip later you are home and in your room."
        "As you are unpacking your things from the day you hear a surprising amount of noise coming from [the_sister.title]'s bedroom."
    else:
        "It has been a long day and you are suddenly struck by the urge to go home for the night to relax."
        $ mc.change_location(hall)
        "When you get home and open the door you hear a surprising amount of noise coming from [the_sister.title]'s bedroom."
    $ scene_manager = Scene()
    $ the_person.apply_planned_outfit()
    $ the_sister.apply_planned_outfit()
    "Curious, you head down the hall to see what is going on."
    $ mc.change_location(lily_bedroom)
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped(xoffset = 0.05), position = "standing_doggy", emotion = "happy")
    $ scene_manager.add_actor(the_sister, display_transform = character_right, position = "standing_doggy", emotion = "happy")
    "It looks like [the_sister.title] has company, and judging from the fact that they are both still in uniform, it must be one of her classmates."
    $ mc.change_arousal(5)
    "They are both bent over [the_sister.title]'s desk, so you take a moment to enjoy the view before knocking on the door frame."
    mc.name "Hey girls, what are you up to?"
    $ scene_manager.update_actor(the_sister, position = "stand4", display_transform = character_right_flipped(zoom = 1.1))
    the_sister "Hey, [the_sister.mc_title], we've got a bit of a project for school and were working here instead of on campus."
    if not town_relationships.get_relationship(the_person, the_sister):
        $ town_relationships.begin_relationship(the_person, the_sister)
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(xoffset = 0.11, zoom = 1.1), position = "stand2")
    if town_relationships.get_relationship(the_person, the_sister).type_a =="Friend":
        the_sister "Do you remember my friend [the_person.fname]? You met briefly on campus the other day."
        the_person "Hi, [the_person.mc_title], nice to see you again!"
    elif town_relationships.get_relationship(the_person, the_sister).type_a =="Rival":
        the_sister "I bet you remember [the_person.fname]? She certainly did her best to make an impression."
        the_person "I'm sure he remembers me, after all who could forget a body like mine?"
    else:
        the_sister "Do you remember [the_person.fname]? You met briefly on campus the other day."
        the_person "Hello again."
    mc.name "Hi, I was about to grab something to drink from the kitchen, would you like me to get you something too?"
    the_sister "Yeah, that would be great. I'll take a cola."
    the_person "Just water for me, thanks."
    mc.name "Alright, be right back."
    $ scene_manager.hide_actor(the_person)
    $ scene_manager.hide_actor(the_sister)
    $ scene_manager.clear_scene()
    $ mc.change_location(kitchen)
    if mom.location == kitchen:
        $ scene_manager.add_actor(mom, emotion = "happy")
        "When you get to the kitchen you see [mom.possessive_title] hard at work preparing dinner."
        mc.name "Just grabbing a drink for myself and the girls."
        mom "Alright, [mom.mc_title], dinner will be ready in a bit."
        $ scene_manager.update_actor(mom, position = "walking_away")
        "She turns back to her work as you move towards the fridge."
        if mom.obedience > 130:
            if mom.vagina_visible:
                "The sight of her bare ass wiggling as she works is just too tempting, and you step up to give it a quick slap."
            elif mom.outfit.are_panties_visible:
                "The sight of her panty clad ass wiggling as she works is just too tempting, and you step up to give it a quick slap."
            else:
                "The sight of her ass wiggling as she works is just too tempting, and you step up to give it a quick slap."
            $ mom.slap_ass()
            #TODO opinion based response
            "She lets out a little gasp, but keep working on the food."
            "Knowing the girls will be expecting you back, you stop for now and start gathering the drinks."
        else:
            "You take a moment to appreciate the view before grabbing the drinks."
        "Once you have everything you need you head back to the hall."
        $ scene_manager.remove_actor(mom)
        $ scene_manager.clear_scene()
        $ mc.change_location(hall)
    else:
        "When you get to the kitchen it doesn't take long for you to grab the drinks."
    if mc.inventory.total_serum_count > 0:
        "With a moment of privacy you have the opportunity to slip some serum into the drinks."
        menu:
            "Add serum to [the_person.title]'s drink" if mc.inventory.total_serum_count > 0:
                call give_serum(the_person) from _call_give_serum_first_study_buddy
                if _return:
                    "You add a dose to her drink."
                else:
                    "You think about adding a dose of serum to her drink, but decide against it."
            "Add serum to [the_person.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                pass
            "Leave her drink alone":
                "You think about adding a dose of serum to her drink, but decide against it."
        menu:
            "Add serum to [the_sister.title]'s drink" if mc.inventory.total_serum_count > 0:
                call give_serum(the_sister) from _call_give_serum_first_study_buddy2
                if _return:
                    "You add a dose to her drink."
                else:
                    "You think about adding a dose of serum to her drink, but decide against it."
            "Add serum to [the_sister.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                pass
            "Leave her drink alone":
                "You think about adding a dose of serum to her drink, but decide against it."
    "You head back up to [the_sister.possessive_title]'s bedroom, drinks in hand."
    $ mc.change_location(lily_bedroom)
    $ scene_manager.show_actor(the_person, display_transform = character_center_flipped(xoffset = 0.11, zoom = 1.1), position = "stand2", emotion = "happy")
    $ scene_manager.show_actor(the_sister, position = "stand4", display_transform = character_right_flipped(zoom = 1.1), emotion = "happy")
    "Once you deliver the beverages you are satisfied to see them each take a substanstial swallow."
    "You chat with them a bit more about what their project is, and give some advice based off of your time spent with [nora.fname]."
    mc.name "I should probably let you get back to work. I'll be in my room for the night, early start tomorrow at work."
    $ mc.business.event_triggers_dict["knows_study_day"] = True
    "As you make your way back to your room you realise that since you know their teacher, [nora.fname], it might be possible to change who [lily.fname] is studying with."
    "It might take some effort, but if you don't want to see [the_person.title] next week you should pay the campus a visit."
    $ the_person.event_triggers_dict["study_sessions"] = 1
    return

label lily_study_buddy_visit(the_person):
    $ scene_manager = Scene()
    $ the_sister = lily
    $ mc.change_location(bedroom)
    $ scene_manager.add_actor(the_person)
    "A bit later in the evening, you hear a knock at your open door and look up to see [the_person.title] leaning against the door frame."
    mc.name "Oh, hey [the_person.fname]. Do you need something?"
    if town_relationships.get_relationship(the_person, the_sister).type_a == "Rival": # increase obedience to progress
        the_person "Yeah, I think I've endured as much of your sister as I can for now."
        mc.name "Sorry to hear that, I know how she can be sometimes."
        the_person "Exactly, I was so glad for an excuse to come talk to you instead."
        call lily_study_buddy_rival(the_person) from _call_lily_study_buddy_rival
        if town_relationships.get_relationship(the_person, the_sister).type_a == "Nemesis":
            $ nemesis_transition = Action("Nemesis Transition", lily_mon_followup_requirement, "nemesis_transition_label")
            $ mc.business.remove_mandatory_crisis(rival_study_time)
            $ mc.business.add_mandatory_crisis(nemesis_transition)
    elif town_relationships.get_relationship(the_person, the_sister).type_a == "Friend": # increase love to progress
        call lily_study_buddy_friend(the_sister, the_person) from _call_lily_study_buddy_friend
    elif town_relationships.get_relationship(the_person, the_sister).type_a == "Best Friend":
        call lily_study_buddy_best_friend(the_sister, the_person) from _call_lily_study_buddy_best_friend
    else: # pick a path
        if not town_relationships.get_relationship(the_person, the_sister):
            $ town_relationships.begin_relationship(the_person, the_sister)
        the_person "Your sister had to go help your mom with dinner. I did a bit of work alone, but figured I would come chat with you awhile instead."
        if mom.has_job(mom_secretary_job) or mom.has_job(mom_associate_job):
            mc.name "Yeah, our mom has been working a bit harder than normal lately and as a result we end up helping out more around home."
        elif mom.is_employee:
            mc.name "Yeah, our mom has been working for my company which can mean long days sometimes."
        else:
            mc.name "Sorry about that, sometimes she just can't get everything done in a day."
        the_person "That's understandable, family comes first, we have all week to work on this stuff."
        "[the_person.title] doesn't seem to have developed much of a relationship with [the_sister.possessive_title] yet, which means you can probably influence how they get along."
        "There could be some serious repercussions of interfering with their relationship, but then again, there could be some benefits as well."
        "It seems like maybe you have been thinking about the possibilities a bit too long and [the_person.title] has noticed."
        the_person "You seem a little distracted, would it be better if I left?"
        menu:
            "Bring them together":
                mc.name "Sorry, I was just thinking how lucky my sister is to have a friend like you."
                the_person "Oh, I mean we are lab partners, but we barely know each other outside of class."
                mc.name "Really? I got the impression that you two were really hitting it off."
                the_person "She is nice, sweet, but the semester hasn't been going that long and well..."
                mc.name "That's fine, I just thought... she seems so happy on days she has class with you."
                the_person "I guess I thought she was just always happy, so upbeat. I don't really see her on the days when we aren't in class together."
                "She stops to consider your words. It is early, but it seems like she might be seeing their relationship in a new light."
                $ town_relationships.improve_relationship(the_person, the_sister)
            "Drive them apart":
                mc.name "Sorry, I'm a little surprised, based on some of the things [the_sister.fname] has said I was expecting something different."
                the_person "What? What do you mean? What has she said about me?"
                mc.name "I don't remember exactly, but I just got the impression that you weren't a great lab partner."
                the_person "Is that right? Well I guess I'll go see what makes me so terrible."
                mc.name "No, I shouldn't have said that. Please, just forgot it, maybe she was talking about someone else."
                the_person "Really?"
                mc.name "I don't know, is there anyone else named [the_person.fname] in your classes?"
                the_person "Well we don't share all the same classes..."
                mc.name "Look, I don't want the two of you to fight, and you're probably stuck together for the semester so it would be best if you forget I said anything."
                "She stops to consider your words, but it is pretty clear that you have driven a wedge between them and they'll probably never be friends."
                $ town_relationships.worsen_relationship(the_person, the_sister)
        "You let the pause linger, but it starts to get a bit awkward."
        mc.name "So... um... sorry for overstepping a bit. I didn't mean to kill the conversation."
        the_person "No, it's okay. I should probably be getting back anyway. We do have work to do tonight."
        mc.name "Okay, good luck and have a good night."
        the_person "Thanks, I'll probably see you next week if we are still studying here."
    $ scene_manager.clear_scene()
    return

label study_buddy_test():
    $ the_person = get_lab_partner()
    $ the_person.change_location(lily_bedroom)
    "STUDY BUDDY PREP"
    call study_buddy_prep_label() from _call_study_buddy_prep_label_test
    menu:
        "First time":
            "LILY FIRST STUDY BUDDY"
            call lily_first_study_buddy(lily, the_person) from _call_lily_first_study_buddy_test
            $ mc.business.change_funds(6000)
            "STUDY BUDDY NORA"
            call study_buddy_nora_label(nora) from _call_study_buddy_nora_label_test
            $ the_person = get_lab_partner()
            "STUDY BUDDY PREP"
            call study_buddy_prep_label() from _study_buddy_prep_label_test_2
            "STUDY BUDDY DATE"
            call study_buddy_date_label() from _call_study_buddy_date_label_test
        "Loop":
            $ stop = False
            while not stop:
                $ mc.change_energy(100)
                $ the_person.change_energy(100)
                "STUDY BUDDY DATE/VISIT"
                $ the_person.change_stats(love = 5, obedience = 5)
                call study_buddy_date_label() from _call_study_buddy_date_label_test_2
                menu:
                    "Continue":
                        pass
                    "Stop":
                        $ stop = True
    "STUDY BUDDY SERUM: This label is optional before date but breaks the test by advancing time."
    call study_buddy_serum_label(the_person) from _call_study_buddy_serum_label_test
    return
