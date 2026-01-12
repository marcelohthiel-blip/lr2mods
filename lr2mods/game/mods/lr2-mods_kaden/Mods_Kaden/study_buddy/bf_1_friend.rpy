init -1 python:
    def lunch_reminder_requirement(the_person):
        if 0 <= day%7 <= 4:
            if time_of_day == 1:
                if the_person.love < 50 and the_person.is_available:
                    if not the_person.is_girlfriend:
                        if town_relationships.get_relationship(the_person, lily).type_a =="Friend":
                            return True
        return False

    def movie_reminder_requirement(the_person):
        if not mc.business.event_triggers_dict.get("movie_date_scheduled", False):
            if the_person.energy > 60 and the_person.is_available:
                if 40 < the_person.love <= 60:
                    if not the_person.is_girlfriend:
                        if town_relationships.get_relationship(the_person, lily).type_a =="Friend":
                            if day%7 == 2:
                                return True
        return False

    def dinner_reminder_requirement(the_person):
        if not mc.business.event_triggers_dict.get("dinner_date_scheduled", False):
            if the_person.energy > 60 and the_person.is_available:
                if 50 < the_person.love <= 60:
                    if not the_person.is_girlfriend:
                        if town_relationships.get_relationship(the_person, lily).type_a =="Friend":
                            if day%7 == 5:
                                return True
        return False

    friend_test_action = Action("BFF 1 Test", kaden_test_req, "friend_test", menu_tooltip = "Hang out with friend. See Lily's reaction. Get reminded about lunch/movie/dinner date. Loop. Get congratulated by Lily.")

label lily_study_buddy_friend(the_sister, the_person):
    $ scene_manager = Scene()
    the_person "Yeah, we ran out of note cards and [the_sister.fname] thought you might have some extra."
    mc.name "I think I can help you out, why don't you come in and talk with me while I look?"
    $ scene_manager.add_actor(the_person, position = "sitting")
    if the_person.love < 10:
        call small_talk_person(the_person, apply_energy_cost = False, is_phone = False)
    elif the_person.love < 20:
        call compliment_person(the_person)
    elif the_person.love < 25:
        call flirt_person(the_person)
    elif the_person.love < 35:
        call small_talk_person(the_person, apply_energy_cost = False, is_phone = False)
    else:
        if the_person.outfit.shows_off_her_ass:
            mc.name "You're looking hot today [the_person.title]. That outfit really shows off your cute butt."
        elif the_person.outfit.shows_off_her_tits:
            mc.name "You're looking tasty today [the_person.title]. That outfit really shows off your [the_person.tits_description]."
        else:
            $ body_word = get_body_word(the_person)
            mc.name "You're looking cute today [the_person.title]. That outfit really shows off your [body_word] body."
        if the_person.energy > 15:
            $ the_person.call_dialogue("flirt_response_mid")
        else:
            $ the_person.call_dialogue("flirt_response_low_energy")
        python:
            mc.listener_system.fire_event("player_flirt", the_person = the_person)
            change_amount = 1 + the_person.opinion.flirting
            if change_amount <= 0:
                change_amount = 1
            the_person.change_stats(happiness = the_person.opinion.flirting, arousal = change_amount, slut = change_amount, max_slut = 20, love = 1, max_love = 60)
            the_person.discover_opinion("flirting")
            the_person.apply_serum_study()
    if the_person.love >= 60 or the_person.is_girlfriend:
        $ town_relationships.improve_relationship(the_person, the_sister)
        if the_person.is_girlfriend:
            $ lily_congrats = Action("[the_sister.title] Congrats", lily_mon_followup_requirement, "lily_congrats_label")
            $ mc.business.add_mandatory_crisis(lily_congrats)
    else:
        $ lily_jealous = Action("Sister Jealous", lily_mon_followup_requirement, "lily_jealous_label")
        $ mc.business.add_mandatory_crisis(lily_jealous)
        $ planned_date = False
        if the_person.love >= 20:
            the_person "You know, this isn't really fair to [the_sister.fname]. Do you maybe want to spend time together when I'm not supposed to be working with her?"
            mc.name "That is a great idea, actually..."
        if the_person.love >= 40:
            if not mc.business.event_triggers_dict.get("dinner_date_scheduled", False):
                call dinner_date_plan_label(the_person) from _call_dinner_date_plan_label_study
                $ planned_date = True
            else:
                $ dinner_date_reminder = Action("Dinner Date Reminder", dinner_reminder_requirement, "dinner_date_reminder_label", args=the_person, requirement_args=the_person)
                $ mc.business.add_mandatory_crisis(dinner_date_reminder)
        if the_person.love >= 30 and not planned_date:
            if not mc.business.event_triggers_dict.get("movie_date_scheduled", False):
                call movie_date_plan_label(the_person) from _call_movie_date_plan_label_study
                $ planned_date = True
            else:
                $ movie_date_reminder = Action("Movie Date Reminder", movie_reminder_requirement, "movie_date_reminder_label", args=the_person, requirement_args=the_person)
                $ mc.business.add_mandatory_crisis(movie_date_reminder)
        if not planned_date and the_person.love >= 20:
            if the_person.love < 50:
                $ planned_date = True
                mc.name "...did you have something in mind?"
                the_person "I don't know, I'm pretty busy with school, but I usually have some free time in the middle of the day."
                the_person "Maybe if you find yourself on campus we could get lunch together sometime."
                mc.name "That sounds great, I'll try to arrange my schedule to have lunch free."
                "[the_person.title] will be on campus every weekday afternoon, you should invite her to lunch before next week."
                $ lunch_date_reminder = Action("Lunch Date Reminder", lunch_reminder_requirement, "lunch_date_reminder_label", args=the_person, requirement_args=the_person)
                $ mc.business.add_mandatory_crisis(lunch_date_reminder)
        if not planned_date and the_person.love >= 20:
            "You chat for a bit, but things have gone about as far as they can in your room. If you want to do more you should probably ensure you are free to do other things."
            if mc.business.event_triggers_dict.get("dinner_date_scheduled", False) and the_person.love >= 40:
                "You should probably ensure you are free to take her to dinner next Friday."
            if mc.business.event_triggers_dict.get("movie_date_scheduled", False) and the_person.love >= 30:
                "You should probably ensure you are free to take her to the movies next Tuesday."
    "After your talk [the_person.title] gets up to go back to [the_sister.possessive_title]'s room."
    if not mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"] = []
    if mc.business.event_triggers_dict.get("home_cameras", []):
        "You could check your cameras to see how their study session goes."
        if "1. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("1. Friend Recording")
        elif "2. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("2. Friend Recording")
        call study_recordings_menu_label() from _study_recording_menu_label_repeat
    else:
        "It's a shame you don't have any way to see what is happeneing in there."
        if mc.business.funds < 10000:
            "It might be possible to buy a camera if you save up $10,000."
        else:
            "You should visit the mall and see if the electronics store has anything that could help."
    $ scene_manager.clear_scene()
    return

label lunch_date_reminder_label(the_person):
    "On Monday [the_person.title] said she wants to spend more time with you."
    "If you still want to build a relationship with her you should head over to campus and ask her out to lunch."
    $ lunch_date_reminder = Action("Lunch Date Reminder", lunch_reminder_requirement, "lunch_date_reminder_label", args=the_person, requirement_args=the_person)
    $ mc.business.add_mandatory_crisis(lunch_date_reminder)
    return

label movie_date_reminder_label(the_person):
    "Your date at the movies last night was great."
    "Since your next Tuesday is still free, now would be a great time to track down [the_person.title] if you still want to build a relationship with her."
    return

label dinner_date_reminder_label(the_person):
    "Your dinner date last night was great."
    "Since your next Friday is still free, now would be a great time to track down [the_person.title] if you still want to build a relationship with her."
    return

label lily_jealous_label():
    $ scene_manager = Scene()
    $ the_sister = lily
    $ the_person = get_lab_partner()
    if town_relationships.get_relationship(the_person, the_sister).type_a =="Best Friend":
        return
    if the_sister.event_triggers_dict.get("friend_frustration", 0) < 1:
        $ the_sister.event_triggers_dict["friend_frustration"] = 1
        $ temp_outfit = the_sister.planned_outfit
    else:
        $ the_sister.event_triggers_dict["friend_frustration"] += 1
        $ temp_outfit = Outfit("Nude")
        $ temp_bra = None
        $ temp_panties = None
        if the_sister.has_taboo("bare_tits") or the_sister.has_taboo("bare_pussy"):
            $ [main_colour, second_colour] = random_colours(the_sister, 2)
            if the_sister.has_taboo("underwear_nudity"):#underwear
                $ temp_bra = sports_bra.get_copy()
                $ temp_bra.colour = main_colour
                $ temp_outfit.add_upper(temp_bra)
            if the_sister.has_taboo("bare_tits"): #panties
                $ temp_panties = cute_panties.get_copy()
                $ temp_panties.colour = second_colour
                $ temp_outfit.add_lower(temp_panties)
        $ temp_outfit.add_dress(bath_robe.get_copy())
    $ the_sister.apply_outfit(temp_outfit)
    if the_sister.event_triggers_dict.get("friend_frustration", 0) < 2:#first talk shoulder rub
        if the_sister.is_girlfriend:
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion = "sad", position = "stand2")
            "[the_sister.title] knocks lightly on your door, hesitating briefly before entering."
            "She closes the door behind her and walks towards your bed. Her hair is messy from running her fingers through it, and there's a pink hue staining her cheeks."
            "[the_sister.possessive_title!c] sighs heavily."
            the_sister "Hi, [mc.name]."
            $ scene_manager.update_actor(the_sister, emotion = "sad", position = "sitting")
            "Her voice is slightly strained. She perches on the edge of your bed, looking nervously at you."
            the_sister "I wanted to talk to you about something..."
            "You look at her curiously, sensing there's trouble brewing beneath her usually calm exterior."
            the_sister "So, tonight was supposed to be my study session with [the_person.fname] right?"
            "She avoids eye contact. You nod, understanding immediately what's bothering her."
            mc.name "Yeah, I know. Sorry, [the_sister.title], we ended up talking about other things."
            "[the_sister.title] rolls her eyes exasperatedly."
            the_sister "It's fine, really. But don't you think it's rude though? I really needed her help!"
            "You reach out and take hold of her delicate hand, giving it a gentle squeeze."
            "[the_sister.title] looks at your entwined hands for a moment before meeting your gaze. A small smile plays on her lips."
            the_sister "Thanks, [mc.name]. I know you're just trying to be nice, but sometimes it's hard..."
            $ body_word = get_body_word(the_sister)
            "You pull her closer, wrapping your arms around her [body_word] frame."
            "[the_sister.title] rests her head on your shoulder. Your heart beats faster as you wrap your arm around her waist."
            the_sister "... To remember how much you care about me."
            "You lean forward and kiss her softly on the forehead."
            the_sister "I love you, [mc.name]."
            "You pull back, smiling gently."
            "[the_sister.title] relaxes into your embrace, feeling safe and secure in your arms. As the tension between you ebbs away, she finally seems to find peace within herself once more."
            mc.name "Why don't you let me make you feel better."
            call lily_comfort_label() from _call_lily_comfort_label_1
            $ the_sister.event_triggers_dict["friend_frustration"] += 1
            the_sister "Thank you, [mc.name]. For always being there for me."
            "You brush a strand of hair out of her face, tucking it behind her ear."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "stand3")
            "[the_sister.title] gives you a shy smile before standing up."
            the_sister "I guess I'll head back to my room now. I'll try to talk to [the_person.fname] tomorrow."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
            "You walk her to the door, giving her one last reassuring squeeze before she leaves."
        elif the_sister.love > 40:
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion = "sad", position = "stand2")
            "After a gentle knock [the_sister.title] enters your room with an anxious expression on her face. Her eyes dart around your room before settling back onto you."
            $ scene_manager.update_actor(the_sister, emotion = "sad", position = "sitting")
            the_sister "Hi [mc.name], is it okay if I sit on your bed?."
            "After your nod, she moves to your bed and takes a seat at the edge. Meanwhile, you scoot up to a more seated position."
            "[the_sister.title] takes a deep breath before speaking again, clearly gathering courage for whatever she needs to say next."
            the_sister "So, there's something we need to discuss... About my project with [the_person.fname]. You know we agreed to work together right?"
            the_sister "Well, she spent so much time over here we needed to keep working late to get done."
            the_sister "I mean, don't get me wrong, I'm glad you guys are having such great chemistry and everything... but shouldn't she focus on OUR project first?"
            "She pauses briefly then continues in a rush, afraid that this conversation may spiral out of control emotionally."
            the_sister "But also, I kinda miss doing things together like we used to... Like watching movies or playing video games or even talking about random stuff till dawn breaks..."
            the_sister "Do you still wanna hang out with me sometimes? Even though [the_person.fname] is always around these days?"
            "You hesitate for only a moment before reaching across your lap and placing your warm hand upon hers reassuringly."
            mc.name "Of course, [the_sister.title]. We'll always have time for each other. Besides, [the_person.fname] isn't trying to replace us or anything like that."
            mc.name "She knows how important our bond is, and I do too."
            "[the_sister.title] sighs heavily, relieved by your words but still feeling slightly uneasy about sharing your time with someone else."
            the_sister "Alright... Thank you for understanding, [the_sister.mc_title]. Let's just try to find some balance between studying and having fun, okay?"
            "You nod enthusiastically, grateful for her compromise and willingness to adapt."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "sitting")
            "A small smile creeps onto her lips as she finally seems content with your agreement."
            mc.name "Deal."
            "The air between you two lightens immediately and you get an idea, shifting to swing your legs over the side of the bed."
            mc.name "Why don't you let me relieve some of your tension? Maybe a massage?"
            the_sister "I suppose that would be pretty nice."
            mc.name "Come here. I promise, this will make you feel better."
            "She moves towards you, cuddling into your embrace."
            call lily_comfort_label() from _call_lily_comfort_label_2
            $ the_sister.event_triggers_dict["friend_frustration"] += 1
            the_sister "Thanks, that was a good idea."
            mc.name "Anytime."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
            "Despite the new dynamic in your life, one thing remains constant - [the_sister.title] will always be your supportive best friend and loving sister through thick and thin."
        else:
            "You're lying on your bed, replaying the evening's events in your head when there's a knock at your door."
            mc.name "Come in."
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion = "angry", position = "stand2")
            "The door opens slowly, revealing [the_sister.title] standing in the doorway with her arms crossed. She glares at you, looking annoyed."
            the_sister "You know, I was starting to think [the_person.fname] was never coming back."
            mc.name "Yeah, sorry about that, we got kind of caught up talking."
            $ scene_manager.update_actor(the_sister, emotion = "angry", position = "sitting")
            "[the_sister.title] huffs and walks further into the room, plopping down on your bed beside you."
            the_sister "She just abandoned me there, [the_sister.mc_title]! We had so much work to do!"
            $ scene_manager.update_actor(the_sister, emotion = "angry", position = "missionary")
            "She sighs dramatically, flopping onto her back."
            the_sister "I don't get it. One minute she's all about studying with me, and the next she's more interested in spending time with you."
            "You bite your lip, feeling guilty for a moment but also unable to deny the excitement coursing through you."
            mc.name "Um… thanks?"
            "[the_sister.title] snorts derisively."
            mc.name "Hey, can I make it up to you?"
            "[the_sister.title] considers this for a moment before nodding."
            the_sister "Okay, sure, I could really use a massage to help with the tension from worrying about my project alone."
            "You laugh and scoot back, sitting against your headboard while leaving room for [the_sister.possessive_title] to sit in front of you."
            mc.name "Come here. I promise, this will make you feel better."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "sitting")
            "She sits up and scooches back towards you, stopping a few inches away."
            call lily_comfort_label() from _call_lily_comfort_label_3
            the_sister "Thanks, I really needed that."
            mc.name "Anytime."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
            "As [the_sister.title] leaves your room, you can't help but feel grateful for her presence in your life—even if she does occasionally cause trouble."
    elif the_sister.event_triggers_dict.get("friend_frustration", 0) < 3:#second talk massage + 
        if the_sister.is_girlfriend:
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion="angry", position="stand2")
            "[the_sister.title] bursts into your room, frustration evident in her every step. She shoots you a pained glance before pacing back and forth, visibly agitated."
            the_sister "I can't believe [the_person.fname] ditched me for you again!"
            "You sense the distress in [the_sister.title]'s voice and set aside your work, opening your arms for her to come close."
            mc.name "Come here, [the_sister.title]. Let's talk about it."
            "[the_sister.title] hesitates for a moment before walking into your embrace, seeking comfort in your warmth."
            $ scene_manager.update_actor(the_sister, position = "sitting")
            "You gently guide her to sit on the bed, and you wrap your arms around her, creating a cocoon of support."
            mc.name "I understand it's frustrating, and it's okay to feel that way. I'm here for you."
            "You run your fingers through [the_sister.title]'s hair, offering a soothing touch as she vents about the situation."
            the_sister "I just miss our time together, you know? It feels like she's taking you away from me."
            mc.name "I get it, [the_sister.title]. I value our time too. Let me talk to [the_person.fname], help her understand."
            "You continue to hold [the_sister.title] close, providing a comforting presence as she expresses her feelings."
            the_sister "Do you think things can go back to the way they were?"
            mc.name "We'll find a way to balance everything. Your feelings matter, and I'll make sure we make time for each other."
            "You press a gentle kiss on [the_sister.title]'s forehead, reinforcing your commitment to the bond you share."
            "[the_sister.title] gradually relaxes in your embrace, finding solace in the comfort you offer during this challenging moment."
            "The room transforms into a haven of support and understanding as you continue to cuddle, reassuring [the_sister.title] that she is not alone."
            mc.name "How about another massage?"
            the_sister "Alright, but this time I think I need more than just my shoulders rubbed."
            "You slide out from under [the_sister.possessive title], and stand up, gripping the neckline of her robe and tugging on it gently."
            $ the_sister.draw_animated_removal(the_sister.outfit.get_upper_top_layer, position = "walking_away")
            "She loosens the belt, puts her arms behind her, and lifts her hips enough for you to pull the robe off."
            $ body_word = get_body_word(the_sister)
            if temp_panties:
                if temp_bra:
                    $ mc.change_arousal(2)
                    "Underneath she is wearing a modest bra and panties, but you can see most of her [body_word] body as she rolls over to lay on her stomach."
                else:
                    $ mc.change_arousal(5)
                    "Underneath she's topless, wearing just a modest pair of panties. You get a good look at her [the_sister.tits_description] before she rolls over to lay on her stomach."
            elif temp_bra:
                $ mc.change_arousal(5)
                "Underneath she is wearing a modest bra, but is bottomless. You get a glimpse of her [the_sister.pubes_description] mound before she rolls over to lay on her stomach."
            else:
                $ mc.change_arousal(10)
                "Underneath she is nude, so you get a lovely view of her [the_sister.tits_description] and her [the_sister.pubes_description] mound before she rolls over to lay on her stomach."
            $ the_sister.update_outfit_taboos()
            $ scene_manager.update_actor(the_sister, position = "walking_away")
        else:
            "You're lying on your bed when there's a knock at your door. You roll over and sit up, rubbing your eyes, trying to sound more awake than you are."
            mc.name "Come in."
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion = "angry", position = "stand2")
            "The door opens slowly, revealing [the_sister.title] standing in the doorway with her arms crossed."
            "She glares at you, looking even more annoyed than last week."
            the_sister "You know what? I give up, why do I even bother with her?"
            $ scene_manager.update_actor(the_sister, emotion = "sad", position = "missionary")
            "She flings herself onto your bed, throwing her hands dramatically into the air."
            mc.name "Uh… [the_sister.title], what's wrong? Was it [the_person.fname] again? I tried not to distract her for too long."
            "[the_sister.title] sighs heavily, flopping back onto your pillow. She huffs, staring up at the ceiling."
            the_sister "I don't get why she can't just focus on school like we agreed to."
            mc.name "Well, maybe if she sees how hard you've been working without her, she'll realise she needs to step it up too."
            the_sister "Yeah, right. Like that's ever going to happen."
            $ scene_manager.update_actor(the_sister, position = "walking_away")
            "She rolls over onto her side, facing away from you. You hesitate for a moment before speaking up again."
            mc.name "Hey [the_sister.title], want me to give you a real massage this time?"
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "back_peek")
            "She freezes for a second before turning back towards you with a look of surprise on her face."
            the_sister "Really? You'd do that for me?"
            mc.name "Of course! I'm partially to blame after all. Come on, get comfortable."
            "[the_sister.title] hesitates for another moment before opening her robe and rolling over to lay on her stomach."
            "You slide out from the bed, and stand up, gripping the neckline of her robe and tugging on it gently."
            $ the_sister.draw_animated_removal(the_sister.outfit.get_upper_top_layer, position = "back_peek")
            "She rocks her body so you are able to slide the robe down her arms and off."
            $ body_word = get_body_word(the_sister)
            if temp_panties:
                if temp_bra:
                    $ mc.change_arousal(2)
                    "Underneath she is wearing a modest bra and panties, but most of her [body_word] body is visible."
                else:
                    $ mc.change_arousal(5)
                    "Underneath she's topless, wearing just a modest pair of panties."
            elif temp_bra:
                $ mc.change_arousal(5)
                "Underneath she is wearing a modest bra, but is bottomless."
            else:
                $ mc.change_arousal(10)
                "Underneath she is nude, so you get a lovely view of her [body_word] body."
            $ the_sister.update_outfit_taboos()
        call lily_comfort_label() from _call_lily_comfort_label_4
        "[the_sister.possessive_title!c] doesn't seem to be in any rush to leave so you roll over and lay on the bed next to her."
        "The two of you enjoy a few moments of companionable silence while she collects herself."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "sitting")
        if the_sister.is_girlfriend or the_sister.love > 60:
            "Eventually she climbs to her knees and leans over to give you a passionate and lingering kiss."
            $ the_sister.break_taboo("kissing")
        elif the_sister.love > 35:
            "Eventually she climbs to her knees and leans over to give you a tenative and gentle kiss on the lips."
            $ the_sister.break_taboo("kissing")
        else:
            "Eventually she climbs to her knees and carefully leans over you, hesitating for a moment before giving you a kiss on the forehead."
        "Then she turn off your bed and stands up, grabbing her robe from the floor."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "stand4")
        $ scene_manager.show_dress_sequence(the_sister, temp_outfit)
        the_sister "Thanks again [the_sister.mc_title], that was exactly what I needed."
        mc.name "Of course [the_sister.title], I'm always here for you."
        the_sister "Then I'll probably see you next week if things keep going like they are."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
        "With a final flash of a smile she turns and moves towards the door, heading back to her room for the night."
    elif the_sister.event_triggers_dict.get("friend_frustration", 0) < 4:#third massage+
        if the_sister.is_girlfriend:
            $ the_sister.event_triggers_dict["friend_frustration"] += 1
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion = "happy", position = "stand2")
            "Finding your door slightly ajar, [the_sister.title] pushes it open enough to peer inside."
            "You notice that she is wearing a robe and has a hopeful look in her eyes."
            the_sister "[the_sister.mc_title]? Can I… um… can I have another massage? Please?"
            mc.name "Sure, [the_sister.title], just give me a minute, go ahead and get comfortable."
        else:
            $ scene_manager.add_actor(the_sister, the_sister.outfit, position = "stand2")
            "[the_sister.title] finds your bedroom door, slightly ajar. You notice her as she takes a deep breath, steeling her nerves, before knocking softly."
            the_sister "[the_sister.mc_title]?"
            mc.name "Come in [the_sister.title] What's up?"
            "She smiles shyly and steps into the room, closing the door behind her."
            the_sister "I… um… I was wondering if you could give me another massage, you know, to help me relax?"
            mc.name "Sure, [the_sister.title]. Are you feeling okay? You seem kind of… distracted lately."
            "She hesitates for a moment before nodding."
            the_sister "Yeah, I'm fine, just been busy with school and stuff. It's nice to have someone to take care of me."
        if the_sister.has_taboo("bare_tits") or the_sister.has_taboo("bare_pussy"): #push just past taboo
            $ the_sister.draw_animated_removal(the_sister.outfit.get_upper_top_layer, position = "back_peek")
            "Swallowing hard, she climbs onto the bed and drops the robe before she lies face down on the mattress."
            if the_sister.has_taboo("underwear_nudity"):
                $ mc.change_arousal(5)
                $ the_sister.break_taboo("underwear_nudity")
                "You have a clear view of her bra and panties."
            elif the_sister.has_taboo("bare_tits"):
                $ mc.change_arousal(5)
                $ the_sister.break_taboo("bare_tits")
                "You have a clear view of her exposed back and panties."
            else:
                $ mc.change_arousal(10)
                $ the_sister.break_taboo("bare_pussy")
                "You have a clear view of her exposed back and ass."
        else:
            $ the_sister.draw_animated_removal(the_sister.outfit.get_upper_top_layer)
            $ mc.change_arousal(15)
            "She drops her robe, giving you a glorious view of her [the_sister.tits_description] and [the_sister.pubes_description] mound."
            "Then she moves to your bed, laying down which gives you a view of her ass instead."
        $ the_sister.update_outfit_taboos()
        call lily_comfort_label() from _call_lily_comfort_label_5
        "[the_sister.possessive_title!c] doesn't seem to be in any rush to leave so you roll over and lay on the bed next to her."
        "The two of you enjoy a few moments of companionable silence while she collects herself."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "missionary")
        "Eventually she rolls onto her back, staring up at the cieling wistfully."
        if the_sister.is_girlfriend or the_sister.love > 60:
            the_sister "You make me feel so good [the_sister.mc_title]. I wish I could stay here with you forever."
            mc.name "Forever sounds pretty good to me too, but I don't think we should spend it in my bed."
            "[the_sister.title] give you a skeptical look."
            mc.name "Don't worry we'll spend plenty of time here, but there is more to life and I want to experience it all with you."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "missionary")
            "This earns you a big dopey smile as she rolls over to you and gives you a passionate kiss."
            $ the_sister.break_taboo("kissing")
            "It almost seems like the two of you are going to go another round, but she manages to stop herself."
        elif the_sister.love > 35:
            the_sister "This feels so right but also so weird. I never would have imagined feeling this way about you."
            the_sister "I can't get over the nagging sensation that I shouldn't enjoy this as much as I do."
            mc.name "It's certianly a bit unexpected, but I think it is just our love evolving."
            mc.name "This new dimension doesn't invalidate the love I've always had for you, it just makes it deeper."
            "[the_sister.possessive_title!c] looks deep into your eyes for a moment as she thinks."
            if the_sister.has_taboo("kissing"):
                "Then, leaning toward you slowly she brings her lips to yours, pressing a very soft kiss against them."
                $ the_sister.break_taboo("kissing")
                "When she pulls back she blushes slightly and looks almost embarassed."
            else:
                "Then she leans forward, planting a gentle kiss on your lips."
                "She lets it linger for awhile but doesn't seem to want it to go further."
                "When she pulls back she looks relieved."
            the_sister "Thanks, I think I needed to hear that."
        else:
            the_sister "This is weird right? I mean your my brother but you make me feel so good."
            mc.name "There's nothing wrong with weird as long as we both enjoy ourselves."
            mc.name "I love making you happy, and if that means doing things that most siblings don't, I don't care."
            the_sister "I guess that is fine, but no one else can know. Okay?"
            mc.name "Of course, what we do in private is no one else's business."
        "With reluctant movements [the_sister.title] rolls off your bed and grabs her robe from the floor."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "stand4")
        the_sister "Thanks again [the_sister.mc_title], that was exactly what I needed."
        mc.name "Of course, [the_sister.title] I think I needed it too."
        the_sister "In some ways I'm already looking forward to next week."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
        "With a final flash of a smile she turns and moves towards the door, heading back to her room for the night."
    elif the_sister.event_triggers_dict.get("friend_frustration", 0) < 5:#fourth talk kiss
        if not the_sister.has_taboo("kissing"):
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion="sad", position="stand2")
            "[the_sister.title] enters your room, visibly tired and emotionally drained. She gives you a weary smile, seeking solace."
            the_sister "Hey, [mc.name]. Mind if I sit for a bit?"
            $ scene_manager.update_actor(the_sister, emotion = "sad", position = "sitting")
            "You nod, patting the space next to you on the bed. [the_sister.title] walks over and sits down, shoulders slouched."
            mc.name "Long day?"
            the_sister "Yeah, and I just needed to get away for a moment. [the_person.fname] and I had another disagreement, and I can't shake this feeling of frustration."
            "Sensing [the_sister.title]'s need for comfort, you decide to provide it in a more physical way."
            mc.name "Come here, [the_sister.title]."
            "[the_sister.title] shifts closer, and you wrap your arms around her, pulling her into a warm embrace. Your touch offers a sense of security and understanding."
            the_sister "Thanks, [mc.name]. Your hugs always make things feel a bit lighter."
            mc.name "Anytime, [the_sister.title]. You know I'm here for you."
            "As you continue to hold [the_sister.title] close, the room fills with a quiet intimacy. The physical connection becomes a language of its own, expressing support and comfort."
            the_sister "It's just hard, you know? I feel like I'm constantly on edge with [the_person.fname]."
            mc.name "I get it. We'll figure this out together. Maybe we can all sit down and talk about our expectations and find a middle ground."
            "Your fingers absentmindedly trace soothing patterns on [the_sister.title]'s back, intensifying the closeness between you two."
            "[the_sister.title] seems lost in the comfort of your touch, her weariness momentarily forgotten. In response to the warmth and connection, you find yourself leaning in, and your lips meet in a tender kiss."
            call fuck_person(the_sister, start_position = kissing) from call_fuck_person_lily_jealous_1
        else:
            $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion="sad", position="stand2")
            "[the_sister.title] enters your room with a hint of resignation in her expression. There's a lingering tension in the air as she glances at you, her eyes reflecting a mix of emotions."
            the_sister "Hey, [mc.name]. [the_person.fname] and I had another disagreement. It's getting exhausting, you know?"
            "You nod, understanding the ongoing challenges in their relationship. [the_sister.title] takes a deep breath before continuing."
            the_sister "I know you've been there for me, and I appreciate it. It's just... it's hard dealing with this all the time."
            mc.name "I understand, [the_sister.title]. It's not easy for you, and I want to help however I can."
            "You pat the space beside you on the bed, silently inviting [the_sister.title] to join you. She hesitates for a moment before accepting the offer and sitting down."
            $ scene_manager.update_actor(the_sister, position = "sitting")
            the_sister "I was thinking... what if we make this a thing? Every week, after dealing with [the_person.fname], I come here, and we just... unwind together."
            "You can see a glimmer of hope in [the_sister.title]'s eyes, a desire for a consistent source of comfort amidst the ongoing challenges."
            mc.name "I'm all for that, [the_sister.title]. We can make it a routine. Your well-being is important, and I want you to feel supported."
            "You pull [the_sister.title] into a comforting embrace, and she leans into it, finding solace in the familiar warmth of your touch."
            the_sister "Thanks, [mc.name]. It means a lot to me. I just need a bit of peace after dealing with everything out there."
            mc.name "You can count on me. We'll get through this together, one week at a time."
            "[the_sister.title] settles into the comforting embrace, a sense of contentment replacing the earlier tension."
            "Your fingers absentmindedly trace soothing patterns on [the_sister.title]'s back, intensifying the closeness between you two."
            "[the_sister.title] seems lost in the comfort of your touch, her weariness momentarily forgotten. In a moment of vulnerability, she leans in, and your lips meet in an hesitant, tender kiss."
            "There's a brief pause, a shared realisation, and then [the_sister.title] pulls back, her eyes wide with surprise and a hint of embarrassment."
            $ the_sister.break_taboo("kissing")
            the_sister "I-I'm sorry, [mc.name]. That was... I didn't mean to..."
            "You can see the mix of emotions on [the_sister.title]'s face, and you gently reassure her."
            mc.name "It's okay, [the_sister.title]. No need to apologise. We all have moments of connection. Let's take things one step at a time."
            "The room is filled with a new tension, a shift in the dynamics of your relationship, as you navigate the unexpected turn of events with care and understanding."
            menu:
                "Kiss her":
                    "In a gentle and intentional movement, your lips meet again, this time with a subtle hint of passion."
                    "The room seems to shift as the connection between you and [the_sister.title] deepens."
                    "The initial surprise transforms into a shared, unspoken desire as the kiss lingers, becoming a moment of genuine connection."
                    mc.name "I didn't expect this, [the_sister.title], but it feels right."
                    the_sister "Yeah... It does."
                    $ the_sister.change_stats(love = 5)
                    $ the_sister.break_taboo("kissing")
                    "Passion begins to build as the kisses become more intentional and fervent. The room is filled with an electrifying energy, a shared acknowledgment of the depth of your connection."
                    mc.name "I care about you, [the_sister.title]. This feels right for us, doesn't it?"
                    the_sister "It does, [mc.name]. I care about you too."
                    "The admission deepens the connection between you, as you continue to explore this unexpected development in your relationship."
                    call fuck_person(the_sister, start_position = kissing, position_locked = True) from call_fuck_person_lily_jealous_2
                "Don't":
                    "An awkward air lingers in the room after the accidental kiss. [the_sister.title] stands, her eyes flickering between yours, uncertainty written across her face."
                    $ the_sister.change_stats(slut = 2, obedience = 2)
                    "You clear your throat, breaking the silence that has settled in the wake of the unexpected kiss."
                    mc.name "Hey, [the_sister.title], we're siblings. Things might feel a bit different right now, but we've always been there for each other, and we'll figure this out together."
                    "Your words carry a reassurance, a reminder of the deep bond that exists between you and [the_sister.title]. You extend a hand, inviting her to sit beside you once more."
                    the_sister "I didn't mean for that to happen, [mc.name]. It caught me off guard."
                    mc.name "I know, [the_sister.title]. It caught me off guard too. But what's important is that we understand each other, and we can move forward from here."
                    "As [the_sister.title] hesitantly takes a seat, you offer a comforting smile, attempting to ease the lingering tension in the room."
                    "Your fingers find their way back to tracing soothing patterns on [the_sister.title]'s back, a gesture of comfort and familiarity that transcends the momentary awkwardness."
                    the_sister "I just... I don't want things to be weird between us."
                    mc.name "They won't be, [the_sister.title]. We'll navigate this together. Our bond is strong, and moments like these don't change that."
                    "She gradually relaxes as the weight of the situation lifts."
        if not the_sister.has_taboo("kissing"):
            $ the_sister.call_dialogue("sex_review", the_report = _return)
            if the_sister.has_role(trance_role):
                call check_date_trance(the_sister) from _call_check_date_trance_jealous
            # TODO more text?
        else:
            "The two of you continue in companionable silence for awhile."
            "She seems to be comfortable without seeking out anything more, and for now you are content to spend time just cuddling."
            "Your not sure how much time has passed, but eventually she gets up to leave."
        the_sister "Thanks for being here for me [mc.name], it really means a lot to know that I can always count on you."
        mc.name "Of course, I love you and will always be here for you."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
        "With a final flash of a smile she turns and moves towards the door, heading back to her room for the night."
    else:#fifth+ massage+
        $ scene_manager.add_actor(the_sister, the_sister.outfit, emotion = "happy", position = "stand2")
        "The door creaks open, revealing [the_sister.title]. There is a hint of weariness on her face, but also a look of anticipation."
        "Without exchanging words, she walks over to you."
        $ scene_manager.update_actor(the_sister, emotion = "sad", position = "sitting")
        "You open your arms, and [the_sister.title] steps into your embrace, both of you sinking into the softness of the mattress."
        "You gently run your fingers through [the_sister.title]'s hair, wordlessly trying to convey support and reassurance."
        "The weight of the day starts to lift from her as the physical connection takes over."
        "The sigh that escapes [the_sister.title]'s lips is one of relief."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "stand3")
        "After a lingering embrace, [the_sister.possessive_title] climbs off the bed and toys with the belt of her robe."
        if the_sister.has_taboo("bare_tits") or the_sister.has_taboo("bare_pussy"): #push just past taboo
            $ the_sister.draw_animated_removal(the_sister.outfit.get_upper_top_layer)
            if the_sister.has_taboo("underwear_nudity"):
                $ mc.change_arousal(5)
                $ the_sister.break_taboo("underwear_nudity")
                "Swallowing hard, she opens and drops the robe giving you a clear view of her bra and panties."
            elif the_sister.has_taboo("bare_tits"):
                $ mc.change_arousal(5)
                $ the_sister.break_taboo("bare_tits")
                "Swallowing hard, she opens and drops the robe giving you a clear view of her exposed [the_sister.tits_description] and panties."
            else:
                $ mc.change_arousal(10)
                $ the_sister.break_taboo("bare_pussy")
                "Swallowing hard, she opens and drops the robe before, giving you a clear view of her [the_sister.tits_description] and [the_sister.pubes_description] mound."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
            "Then she climbs back onto the bed and lies face down on the mattress."
        else:
            $ the_sister.draw_animated_removal(the_sister.outfit.get_upper_top_layer)
            $ mc.change_arousal(15)
            "She pulls it open and drops her robe, giving you a glorious view of her [the_sister.tits_description] and [the_sister.pubes_description] mound."
            $ scene_manager.update_actor(the_sister, emotion = "happy", position = "walking_away")
            $ body_word = get_body_word(the_sister)
            "Then she moves to your bed, laying down, which gives you a view of her [body_word] ass instead."
        $ the_sister.update_outfit_taboos()
        call lily_comfort_label() from _call_lily_comfort_label_7
        "[the_sister.possessive_title!c] lingers for awhile as the two of you collect yourselves."
        "Eventually she starts to move, and you reach out to take her hand, looking up at her face."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "back_peek")
        mc.name "You don't have to leave, there's plenty of room here for you too."
        "You pat the bed as you scoot over, making sure there is enough room for her to lay down again."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "stand2")
        the_sister "That's sweet, but I think maybe we've done enough for tonight."
        if the_sister.is_employee:
            the_sister "We've both got work in the morning... we should get some sleep."
            mc.name "Your boss would 100%% understand if you were a bit sleepy tomorrow."
            mc.name "But, don't worry sleep is all I have in mind."
        else:
            the_sister "I've got school in the morning and you have work... we should get some sleep."
            mc.name "Don't worry, sleep is all I have in mind."
        "[the_sister.name] gives you a doubtful look, it's pretty clear how well she knows you."
        if not the_sister.has_taboo("anal_sex"):
            mc.name "As much as I enjoy fucking you, I also understand the importance of sleep."
        mc.name "Seriously, I just know that wrapping my arms around you all night is a sure way to have pleasant dreams."
        the_sister "God, [the_sister.mc_title] that is such a cheesy line."
        mc.name "That doesn't mean it isn't true."
        $ scene_manager.update_actor(the_sister, emotion = "happy", position = "sitting")
        "She hesitates a moment longer before sitting back down on the bed."
        the_sister "Alright, I'll trust you, but no funny business tonight."
        mc.name "Scout's honor."
        $ body_word = get_body_word(the_sister)
        "As she lays down you reach out to pull her close, spooning against her [body_word] ass."
        "Certian parts of your anatomy might react to her presence, and the way you press against her all but guarantees she is aware of that fact."
        "However, true to your word you settle in, content to be close to her as you drift towards sleep."
        # TODO write and attach a morning scene
    $ scene_manager.clear_scene()
    $ the_sister.change_stats(love = 2)
    return

label lily_comfort_label():
    $ the_sister = lily
    $ the_person = get_lab_partner()
    $ body_word = get_body_word(the_person)
    if the_sister.event_triggers_dict.get("friend_frustration", 0) < 2:
        $ scene_manager.update_actor(the_sister, position = "sitting")
        "Your fingers trail delicately along [the_sister.title]'s back, tracing soothing patterns."
        "You feel the subtle rise and fall of [the_sister.title]'s breath, synchronized with your own."
        "Your hands move with a gentle purpose, finding the knots of tension in [the_sister.title]'s shoulders and massaging them away."
        "The act is not just a physical relief but a symbolic gesture of unwinding the stress she carries."
        $ the_sister.change_arousal(5)
        "As you feel the tension leave her body, your hands start to wander away from her shoulders."
        if not the_sister.has_taboo("touching_body"):
            "You wrap one around her torso, gripping her [the_sister.tits_description], while the other traces a line down her side to explore her thigh."
            #always uniform?
            "Your deft fingers work up under her skirt and through the neck of her top, brushing across her bare skin."
            $ the_sister.change_arousal(10)
            "[the_sister.title] moans against you, grinding backwards into your growing bulge as you drive her arousal to new heights."
            $ mc.change_arousal(5)
            "Your fingers dance, tracing slow circles around [the_sister.possessive_title]'s entrance before dipping inside with a gentle probe."
            if not the_sister.has_taboo("touching_vagina"):
                $ scene_manager.update_actor(the_sister, position = "missionary")
                "[the_sister.title]'s breath hitches in her throat as she tries desperately not to make any noise, but it's no use; moans of pleasure escape her lips despite her best efforts."
                $ the_sister.change_arousal(10)
                "Your fingers work their magic on [the_sister.title], teasing and probing until she's writhing in pleasure."
                $ mc.change_arousal(5)
                "You increase the pace, thrusting deeper and faster into her tight heat, eliciting whimpers of delight from her trashing body."
                "Her entire body trembles with anticipation as you bring her closer and closer to the edge."
                if not the_sister.has_taboo("vaginal_sex"):
                    "Unsatisfied with just grinding against [the_sister.title]'s ass, you reach down and free your rock hard cock from the confines of your shorts."
                    $ scene_manager.strip_to_vagina(the_sister, visible_enough = True, prefer_half_off = True)
                    "Pulling her panties to the side, you push her body forward, planting her face on your bed while lifting her ass."
                    "You quickly move to align your cock with her dripping pussy."
                    call fuck_person(the_sister, start_position = doggy, skip_intro = True) from _call_fuck_person_lily_comfort_v
                    #transition and report
                elif not the_sister.has_taboo("anal_sex"):
                    "Unsatisfied with just grinding against [the_sister.title]'s ass, you reach down and free your rock hard cock from the confines of your shorts."
                    $ scene_manager.strip_to_vagina(the_sister, visible_enough = True, prefer_half_off = True)
                    "Pulling her panties to the side, you slide the tip of your cock down along her ass crack until you reach her puckered hole."
                    call fuck_person(the_sister, start_position = anal_on_lap, skip_intro = True) from _call_fuck_person_lily_comfort_a
                    #transition and report
                else:
                    "Finally, [the_sister.title] cries out in ecstasy as her orgasm crashes over her."
                    $ the_sister.have_orgasm(half_arousal = True, force_trance = True, sluttiness_increase_limit = 30, add_to_log = True)
                    "Her hips buck violently against your hand, as waves of pleasure course through her body."
                    $ mc.change_arousal(5)
                    "Tears stream down her cheeks as all kinds of tension flow out of her."
                    "As [the_sister.title] recovers from her climax, you pull her close and kiss her softly on the forehead."
                    mc.name "That was amazing, [the_sister.title], you're so beautiful when you cum."
            else:
                $ the_sister.break_taboo("touching_vagina")
                "[the_sister.name] freezes, holding her breath. You do too, not wanting to stop, but knowing you are crossing a line."
                "She doesn't pull back, and she doesn't tell you to stop, but it is clear you need to choose your next move carefully."
                "Slowly, but deliberately, you start to move your fingers, keeping them right at the edge of her entrance, running along her lips and brushing against her clit."
                $ mc.change_arousal(5)
                $ scene_manager.update_actor(the_sister, position = "missionary")
                "Relaxing slightly, she leans back against you, spreading her legs ever so subtly to give you better access."
                $ the_sister.change_arousal(10)
                "You can feel her arousal growing, but sense that she doesn't want this to go anywhere right now."
                "Carefully modulating your hand, you help her relax, leaning back into your body, practically melting under your touch."
                "Slowing down, you come to a stop, gently resting your hand on her dripping pussy, and relaxing back against your headboard."
        else:
            $ the_sister.break_taboo("touching_body")
            "Your hands move down her back, tracing gentle circles around her spine, the scent of her shampoo fills the air."
            "You continue massaging her, working your way down to her legs, your touches turning from professional to intimate, lingering on her flushed skin."
            $ mc.change_arousal(5)
            "Boldly, you push the boundaries of casual contact, tracing along her inner thighs and brushing against her breasts."
            $ the_sister.change_arousal(10)
            "Occasionally she tenses up, letting you know to rein yourself in, but never telling you to stop."
            "She must be able to feel your erection pressing against her, but neither one of you draws attention to that fact."
        "After a while, [the_sister.title] lets out a contented sigh, her head lolling to the side."
        the_sister "Thank you, I feel so much better now."
        mc.name "No problem, I'm always here for you, [the_sister.title]."
    else:
        $ scene_manager.update_actor(the_sister, position = "walking_away")
        if the_sister.vagina_visible:
            if the_sister.tits_visible:
                "You stare for a moment at her nude body, drinking in the sight of her bare ass, and the hint of her pussy."
            else:
                "You stare for a moment at her bare ass, and the hint of her pussy."
        else:
            if the_sister.tits_visible:
                "You stare for a moment at her bare back and panty clad ass."
            else:
                "You stare for a moment at her back and panty clad ass."
        "Grabbing a bottle of massage oil from your nightstand and pouring some onto your hands. You rub them together vigorously to warm the liquid."
        "As you approach [the_sister.possessive_title] from behind, she tenses slightly, anticipation playing across her features."
        "Your strong hands begin to knead her shoulders, working their way down her back."
        "[the_sister.title] sighs contentedly, arching her back to give you better access to her muscles."
        $ the_sister.change_arousal(5)
        mc.name "So... tell me about the project you are working on."
        the_sister "We made a lot of progress, but I'm tired now... I just want to relax."
        "Your hands slip lower, gliding over her back and [body_word] hips as you work the kinks out of her muscles."
        $ the_sister.change_arousal(5)
        "All the while, [the_sister.title] remains still, her breath coming faster and shallower, her pulse racing under your firm touch."
        "She shutters, feeling your hands move lower, skimming over the tops of her thighs before exploring down her legs."
        $ the_sister.change_arousal(5)
        "Your fingers begin to knead into her flesh, working up a gentle rhythm that sends shivers of pleasure coursing through her body."
        "As your massage returns to her upper legs, [the_sister.title] occasionally flexes towards your hands, almost like she is eager for more."
        "As one of your hands works its way to the heights of her inner thigh, the other slides up her body to cup one of her breasts."
        $ the_sister.change_arousal(5)
        "[the_sister.title] moans softly, arching to give you better access to her tits while slightly parting her legs."
        $ mc.change_arousal(5)
        if not the_sister.has_taboo("touching_body"):
            the_sister "[the_sister.mc_title]... please..."
            "Sensing your opening, you quickly climb on the bed, kneeling to straddle [the_sister.possessive_title] as you abandon the pretense of a massage to grope at her body."
            $ the_sister.change_arousal(5)
            $ mc.change_arousal(5)
            "Savouring the feel of her skin under you, you explore every inch of her body, teasingly avoiding her pussy as she writhes beneath you, occasionally thrusting her hips suggestively."
            if the_sister.vagina_visible:
                "Finally, after what feels like an eternity, you bring your fingers to her glistening pussy lips."
            else:
                "Finally, after what feels like an eternity, you pull aside her panties and rest your fingers on her damp pussy lips."
            "Pressing firmly, you slowly and gently slide two fingers deep inside her, curling them down to massage her G-spot."
            if not the_sister.has_taboo("touching_vagina"):
                $ the_sister.change_arousal(5)
                "She cries out, her voice muffled against your pillow."
                the_sister "[the_sister.mc_title]! I'm going to—oh God— I'm so close."
                "Her words are cut off by another wave of pleasure as you continue to work your fingers inside her, milking every last drop of ecstasy from her body."
                $ the_sister.change_arousal(10)
                "She moans, arching her back and pressing herself against your hand. Her breath comes in ragged gasps as you continue to work your fingers inside her, setting off one wave of pleasure after another."
                "With a final thrust, you push [the_sister.title] over the edge, watching intently as her eyes roll back in her head and she cries out your name."
                $ the_sister.have_orgasm()
                "Her body trembles with the force of her orgasm, every muscle taut and shuddering from the intensity of the sensation."
                "As she comes down from the peak, you slide your fingers free and press them to your lips, tasting her sweet essence."
                "[the_sister.title] lays there, panting heavily, her heart racing."
                the_sister "That was… incredible."
                if not the_sister.has_taboo("vaginal_sex") or not the_sister.has_taboo("anal_sex"):
                    $ scene_manager.update_actor(the_sister, position = "doggy")
                    "Her voice still thick with arousal, she looks up at you, then pulls her knees forward, lifting her ass from the bed."
                    the_sister "I can go another round if you want."
                    "With a growl of approval, you position yourself at her entrance, guiding your hardness towards her opening."
                    $ the_sister.change_arousal(5)
                    $ mc.change_arousal(10)
                    "[the_sister.title] gasps as she feels you press against her, the head of your shaft nudging against her tight entrance."
                    "She arches her back, pushing herself closer to you as you begin to thrust slowly, inching deeper with each stroke."
                    "The sensation is almost too much to bear; you can feel every inch of her gripping you as you fill her completely."
                    "With a final push, you bury yourself deep inside her, hitting her sweet spot with your full length."
                    "[the_sister.title] cries out in pleasure as her muscles clench around you in a tight embrace."
                    "You start to move, thrusting slowly and deliberately, each motion sending waves of pleasure through both of your bodies."
                    "She moans your name with every thrust, her hips meeting yours in perfect rhythm."
                    if not the_sister.has_taboo("vaginal_sex"):
                        call fuck_person(the_sister, start_position = doggy) from _call_fuck_person_lily_comfort_v2
                    else:
                        call fuck_person(the_sister, start_position = doggy_anal) from _call_fuck_person_lily_comfort_a2
            else:
                $ the_sister.break_taboo("touching_vagina")
                $ the_sister.have_orgasm()
                "Her body convulses around your hand, her hips bucking wildly as she comes undone."
                the_sister "[the_sister.mc_title]!"
                $ mc.change_arousal(10)
                "She cries out, her voice echoing through the room as she throws her head back and loses herself in the sensation."
                "You continue to work your fingers inside her, milking every last drop of pleasure from her body until she is spent and gasping for breath."
                $ scene_manager.update_actor(the_sister, position = "back_peek")
                "As her panting subsides, [the_sister.title] turns to face you, her eyes still glassy with desire."
                the_sister "Thank you, you have no idea how much this means to me."
                mc.name "I know exactly what it means, [the_sister.title], and I'm always here for you—day or night."
                "With that, you pull her close, wrapping your arms around her and holding her tightly against your chest."
                "You remain like that for several long moments, your hearts beating in sync as you savour the afterglow of your intimate encounter."
        else:
            $ the_sister.break_taboo("touching_body")
            "Accepting the invitation, you abandon the pretense of the massage and begin exploring her body in earnest."
            "Her [the_sister.tits_description] are pliable in your hands, and you can feel her nipples hardening in arousal."
            "Trailing lower, you run your fingers across her [the_sister.pubes_description] pubic mound, feeling the heat radiate from her core."
            $ the_sister.change_arousal(5)
            "When you brush across her pussy lips there is a hitch in her breath and she tenses up, no longer moving."
            "Sensing that might be a bridge too far, you float your hand past and move to her thighs."
            "She relaxes almost instantly, her moans resuming a short time later."
            "You continue to explore the rest of her body."
            call fuck_person(the_sister, start_position = standing_grope, start_object = make_bed(), position_locked = True) from _call_fuck_person_lily_comfort_g
    if the_sister.has_role(trance_role):
        call check_date_trance(the_sister) from _call_check_date_trance_comfort
    $ del body_word
    return

label lily_congrats_label(): #TODO write variants
    $ scene_manager = Scene()
    $ the_sister = lily
    $ the_person = get_lab_partner()
    $ scene_manager.add_actor(the_sister, emotion = "happy", position = "stand2")
    "As you are shutting down your computer for the night, [the_sister.title] enters the room quietly and closes the door behind her. You look up in surprise."
    mc.name "[the_sister.title]! What are you doing here?"
    the_sister "Well, I heard some interesting news today, [the_sister.mc_title]."
    "She smirks at you, but you are a bit confused about what she could mean."
    mc.name "What news?"
    the_sister "Oh, you know, something about a certain someone named [the_person.fname]."
    "Realisation strikes as [the_sister.possessive_title] grins wider."
    mc.name  "How did you find out?"
    the_sister  "Let's just say, the signs haven't exactly been subtle."
    mc.name "Figures. So, you're here to tease me, aren't you?"
    the_sister "Of course! But also to say congratulations."
    $ the_sister.change_stats(happiness = 5)
    mc.name "Congratulations? You're not going to make fun of me?"
    the_sister "Nah, I can't resist teasing you a bit, but I'm genuinely happy for you. [the_person.fname] is great."
    mc.name "She is, isn't she?"
    the_sister "No promises. But seriously, I'm glad you found someone special. You deserve it."
    mc.name "Thanks, [the_sister.title]. That means a lot."
    the_sister "Just remember, no matter how wrapped up you get in your newfound romance, I'll always be here to remind you of your embarrassing past."
    mc.name "I wouldn't have it any other way, [the_sister.title]."
    the_sister "Well, congratulations again, [the_sister.mc_title]. I hope you and [the_person.fname] are really happy together."
    mc.name "Thanks, [the_sister.title]. I'm sure we will be."
    "After giving you a pat on the shoulder [the_sister.possessive_title] wishes you a good night and heads back to her room."
    $ scene_manager.clear_scene()
    return

label friend_test():
    $ the_person = get_lab_partner()
    call study_buddy_prep_label() from _call_study_buddy_prep_label_ft
    $ done = False
    while not done:
        menu:
            "LILY STUDY BUDDY FRIEND":
                call lily_study_buddy_friend(lily, the_person) from _call_lily_study_buddy_friend_test
            "LILY JEALOUS LABEL":
                call lily_jealous_label() from _call_lily_jealous_label_test
            "LILY COMFORT LABEL":
                call lily_comfort_label() from _call_lily_comfort_label_test
            "LUNCH DATE REMINDER":
                call lunch_date_reminder_label(the_person) from _call_lunch_date_reminder_test
            "MOVIE DATE REMINDER":
                call movie_date_reminder_label(the_person) from _call_movie_date_reminder_label_test
            "DINNER DATE REMINDER":
                call dinner_date_reminder_label(the_person) from _call_dinner_date_reminder_label_test
            "LILY CONGRATS LABEL":
                call lily_congrats_label() from _call_lily_congrats_label_test
            "DONE":
                $ done = true
    return