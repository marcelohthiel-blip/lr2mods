init 4 python:
    def lily_buddy_date_requirement(the_day):
        if lily.available and get_lab_partner().available:
            if day%7 not in [0, 1, 4]:
                if not (erica.event_triggers_dict.get("insta_pic_intro_complete", False) and day%7 == 5):
                    if time_of_day > 2:
                        if day > the_day + TIER_1_TIME_DELAY:
                            return True
        return False

label lily_buddy_date_label(): # 4/5/6/7
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ the_person.event_triggers_dict["friend_with_benefits"] = the_person.event_triggers_dict.get("friend_with_benefits", 0) + 1
    $ single_orgasm = None
    #recordings unlock and follow up events
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 3:
        if "Lily/Buddy Kissing" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lily/Buddy Kissing")
            $ date_followup = Action("Date followup", lily_followup_requirement, "date_followup_label")
            $ mc.business.add_mandatory_crisis(date_followup)
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 4:
        if "Lily/Buddy Groping" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lily/Buddy Groping")
            if the_sister.sluttiness > the_person.sluttiness: #TODO both?
                $ lily_cuddle = Action("Lily cuddle", lily_followup_requirement, "lily_cuddle_label")
                $ mc.business.add_mandatory_crisis(lily_cuddle)
            else:
                $ buddy_gossip = Action("Buddy Gossip", buddy_followup_requirement, "buddy_gossip_label")
                $ the_person.add_unique_on_talk_event(buddy_gossip)
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 5:
        if "Lily/Buddy Stripping" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lily/Buddy Stripping")
            $ date_followup = Action("Date followup", lily_followup_requirement, "date_followup_label")
            $ mc.business.add_mandatory_crisis(date_followup)
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 6:
        if "Lily/Buddy Oral Sex" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lily/Buddy Oral Sex")
            if the_sister.sluttiness > the_person.sluttiness:
                $ lily_cuddle = Action("Lily cuddle", lily_followup_requirement, "lily_cuddle_label")
                $ mc.business.add_mandatory_crisis(lily_cuddle)
            else:
                $ buddy_gossip = Action("Buddy Gossip", buddy_followup_requirement, "buddy_gossip_label")
                $ the_person.add_unique_on_talk_event(buddy_gossip)
    #effect on girls
    $ temp_sluttiness = 0
    $ temp_happiness = 0
    $ temp_arousal = 0
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 5: #kiss
        $ temp_sluttiness = 2
        $ temp_happiness = 5
        $ temp_arousal = 20
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 6: #grope
        $ temp_sluttiness = 5
        $ temp_happiness = 10
        $ lesbian_orgasm(the_person)
        $ lesbian_orgasm(the_sister)
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 7: #strip
        $ temp_sluttiness = 5
        $ temp_happiness = 2
        $ temp_arousal = 40
    else: #oral
        $ temp_sluttiness = 10
        $ temp_happiness = 10
        $ lesbian_orgasm(the_person)
        $ lesbian_orgasm(the_sister)
    if the_sister.sluttiness > the_person.sluttiness:
        $ the_sister.change_stats(happiness = temp_happiness, arousal = temp_arousal)
        $ the_person.change_stats(happiness = temp_happiness, slut = temp_sluttiness, arousal = temp_arousal)
    else:
        $ the_person.change_stats(happiness = temp_happiness, arousal = temp_arousal)
        $ the_sister.change_stats(happiness = temp_happiness, slut = temp_sluttiness, arousal = temp_arousal)
    $ del temp_sluttiness
    $ del temp_happiness
    $ del temp_arousal
    #current scene
    if day%7 == 0:
        "Unsurprisingly you do not get a visit during [the_sister.possessive_title]'s study time with [the_person.title]."
    if mc.business.event_triggers_dict.get("home_cameras", []):
        "You get an alert on your phone, it looks like [the_sister.title] and [the_person.title] are having some alone time in [the_sister.possessive_title]'s room."
    else:
        $ mc.start_text_convo(the_sister)
        the_sister "I'll be in my room with [the_person.fname], if you could run interference with mom." (what_style = "text_message_style")
        $ mc.end_text_convo()
        "You respond with a quick thumbs up, and wish you had a camera to see what they were up to."
    if mc.current_location_hub != home_hub:
        menu:
            "Go home":
                $ mc.change_location(bedroom)
                "Not wanting to miss a thing, you quickly go home and head to your room."
            "Stay where you are":
                pass
    elif mc.location != bedroom:
        "You move to your bedroom, so you can be sure not to miss a thing."
        $ mc.change_location(bedroom)
    if mc.location == bedroom:
        if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 7:
            if not mc.business.event_triggers_dict.get("home_cameras", []):
                "You do occasionally hear the murmur of them talking. Maybe you should try to find a way to spy on their dates in the future."
            else:
                "You do occasionally hear the murmur of them talking. You should check your camera to see what is happening."
                if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 5:
                    call lily_room_kiss(the_sister, the_person) from _call_lily_room_kiss_bf
                elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 6:
                    call lily_room_grope(the_sister, the_person) from _call_lily_room_grope_bf
                elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 7:
                    call lily_room_strip(the_person, the_sister) from _call_lily_room_strip_bf
                "With the action over (for now), you shut down your computer and get ready for bed."
            if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 5:
                call lesbian_sex(the_sister, the_person, path = ["kiss", "kiss", "grope", "grope"] ) from _call_lesbian_sex_kiss_bf
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 6:
                call lesbian_sex(the_sister, the_person, path = ["kiss", "grope", "finger1", "both_finger", "both_finger", "both_finger", "both_finger"]) from _call_lesbian_sex_grope_bf
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 7:
                call lesbian_sex(the_sister, the_person, path = ["self_strip1", "self_strip1", "self_strip1", "self_strip1", "self_strip1", "self_strip1"]) from _call_lesbian_sex_strip_bf
        else:
            if not mc.business.event_triggers_dict.get("home_cameras", []):
                "You do occasionally hear what could be muffled moans. Some kind of spy camera is definitely sounding like a good investment."
            else:
                "You do occasionally hear what could be muffled moans. You should check your camera to see what is happening."
                if the_sister.sluttiness >= the_person.sluttiness:
                    call lily_room_oral(the_sister, the_person) from _call_lily_room_oral_bf
                else:
                    call lily_room_oral(the_person, the_sister) from _call_lily_room_oral_bf2
            call lesbian_sex(the_sister, the_person, path = ["suck1", "suck2", "oral1", "oral2", "69", "69", "69", "69"])
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 7:
        $ lily_buddy_date = Action("Lesbian Date", lily_buddy_date_requirement, "lily_buddy_date_label", requirement_args=day)
        $ mc.business.add_mandatory_crisis(lily_buddy_date)
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 13:
        $ lily_buddy_corruption = Action("Lesbian Date", lily_buddy_corruption_requirement, "lily_buddy_corruption_label", requirement_args=day)
        $ mc.business.add_mandatory_crisis(lily_buddy_corruption)
    $ scene_manager.clear_scene
    return

label date_followup_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ needs_help = None
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) == 4:
        $ needs_help = the_sister
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) == 6:
        $ needs_help = the_person
    if the_person.sluttiness < 40 < the_sister.sluttiness:
        $ needs_help = the_person
    elif the_sister.sluttiness < 40 < the_person.sluttiness:
        $ needs_help = the_sister
    if needs_help == the_sister: # lily needs work
        "Some time late in the night, you're awoken by the buzz of your phone getting a text. You roll over and ignore it."
        "A few minutes later it buzzes again, then again. You're forced to wake up and see what is the matter."
        $ mc.phone.add_non_convo_message(the_person, "Hey, are you awake?")
        $ mc.phone.add_non_convo_message(the_person, "I want to ask you about your sister")
        $ mc.phone.add_non_convo_message(the_person, "She is being a bit of a prude")
        "[the_person.title] has been texting you. She's sent you several messages, with the last ending:"
        $ mc.start_text_convo(the_person)
        the_person "Hello? I really need your help"
        mc.name "Sorry, I was sleeping. What's up?"
        the_person "Well, we've been spending a lot of time together, but she just doesn't seem to be interested in taking things to the next level"
        if not the_person.has_taboo("vaginal_sex") or not the_person.has_taboo("anal_sex"):
            the_person "I figured, being related to you, she would have no problem with physical relationships but she is holding back"
        elif not the_person.has_taboo("sucking_cock"):
            the_person "I mean, you and me didn't go too fast, but she is really reluctant to take the next step"
        else:
            the_person "I know you and I didn't really do much, but I was hoping to get a bit more physical with her"
        mc.name "And this is my problem how?"
        the_person "Please I don't know who else to go to with this. I was hoping maybe you could find some way to encourage her more wild side"
        mc.name "Okay, I'll see what I can do. You're gonna owe me one"
        the_person "Oh my god, thank you so much!"
        $ the_person.change_stats(happiness = 10)
        mc.name "Going back to sleep now"
        the_person "Right, sorry"
        the_person "Good night"
        the_person "Sorry"
        $ mc.end_text_convo()
        "You should probably find some time this week to try and corrupt [the_sister.title]. If you slip her a serum on Monday night it wouldn't hurt."
        if the_sister.sluttiness > 50:
            "Although, to be honest she probably just needs time. She has been pretty throughly corrupted already."
    elif needs_help == the_person: # person needs work
        $ scene_manager.add_actor(the_sister, get_pajama_outfit(the_sister))
        "As you are getting comfortable [the_sister.title] steps into the room and closes the door."
        the_sister "Hey, [the_person.mc_title] do you have a few minutes to talk?"
        mc.name "For you? Always."
        the_sister "It's about [the_person.fname]. We have been having fun lately, a lot of fun, but she seems reluctant to go further."
        mc.name "Well not everyone is as free spirited as we are."
        the_sister "I know, but you have done so much this year to help me open up..."
        if not the_sister.has_taboo("anal_sex"):
            "You reach out and give her ass a squeeze."
            mc.name "In more ways than one."
            "She moans slightly, but playfully swats your hand away."
            the_sister "I'm serious."
        mc.name "You're wondering if I could help her open up too?"
        the_sister "Yes, exactly. If you did I would be happy to repay you. Maybe I could even get [the_person.fname] to help."
        mc.name "For such a noble cause I'd be happy to help."
        the_sister "Great, maybe next time she is here you could talk to her."
        mc.name "Of course, I'll try to swing by with some drinks for you again. Make some excuse to leave the room and we will talk."
        the_sister "Awesome, I'm so excited to be able to spend time with both of you."
        $ scene_manager.update_actor(the_sister, position = "walking_away")
        "With her problem taken care of for the night [the_sister.possessive_title] turns to head back to her room for the night."
        if not the_sister.has_taboo("sucking_cock"):
            menu:
                "Stop her":
                    mc.name "Wait!"
                    $ scene_manager.update_actor(the_sister, position = "back_peek")
                    the_sister "Yeah?"
                    mc.name "Instead of repaying me after I help, what if you prepaid me now?"
                    the_sister "What's the matter, does the thought of helping me corrupt [the_person.fname] get you excited?"
                    $ scene_manager.update_actor(the_sister, position = "stand3", emotion = "happy")
                    the_sister "Are you picturing me playing with her [the_person.tits_description]?"
                    $ body_word = get_body_word(the_person)
                    the_sister "Or burying my head between her [body_word] thighs as I lick her sweet pussy?"
                    mc.name "Well I certainly am now."
                    "You reach down to adjust your pants, and then start to open them."
                    mc.name "Come on [the_sister.title], help me take care of this before you go back to bed."
                    $ scene_manager.update_actor(the_sister, position = "kneeling1")
                    "Coming closer with a grin, [the_sister.possessive_title] drops to her knees in front of you."
                    "You don't waste any more time, quickly revealing your half hard cock and subtly thrusting it towards [the_sister.title]'s eager mouth."
                    the_sister "You poor thing, let me see what I can do."
                    "She starts by planting a few kisses on your rapidly hardening shaft."
                    the_sister "Is this all for me? Or are you still thinking about [the_person.fname]?"
                    "She wraps her lips around your head, suckling gently while looking up at you for an answer."
                    mc.name "Honesty, [the_person.fname] is hot, but you are even hotter. What really gets me going though, is the idea of you two together."
                    "She moans appreciatively sliding further down your now fully erect dick before pulling off."
                    the_sister "Good enough, I can't wait to get to share you with her, but you've got some work to do first."
                    mc.name "Of course, speaking of work..."
                    "You thrust your hips suggestively. [the_sister.possessive_title!c] takes the hint and takes you back into her mouth."
                    "She works her way up and down a few times as you imagine how much better it will be to have two girls servicing you."
                    call fuck_person(the_sister, private = True, start_position = blowjob, start_object = mc.location.get_object_with_name("floor"), skip_intro = False, girl_in_charge = False, self_strip = True, hide_leave = False, position_locked = True, report_log = None, affair_ask_after = False, ignore_taboo = False, skip_condom = False) from _call_fuck_person_corruption_visit
                    mc.name "Thanks, you're incredible [the_sister.title]."
                    the_sister "I'm always happy to trade favors, but now I'm tired."
                    mc.name "Good night."
                    $ scene_manager.update_actor(the_sister, position = "back_peek")
                    "She treats you to one last smile as she leaves, swaying her hips deliberately as she steps into the hallway."
                "Let her go":
                    pass
    elif the_person.sluttiness < 40 and the_sister.sluttiness < 40: # they need a push
        if not mc.business.event_triggers_dict.get("home_cameras", []):
            "It is hard to tell from your room, but it seems like [the_sister.title] and [the_person.title] are taking things slow in their relationship."
        else:
            "Judging from the footage, it seems like [the_sister.title] and [the_person.title] are taking things slow in their relationship."
        "If you want them to get more physical with one another you are probably going to have to give them a push."
        "Maybe some serums slipped in their drinks Monday evening could get the job done."
    else:
        if not mc.business.event_triggers_dict.get("home_cameras", []):
            "It is hard to tell from your room, but it seems like [the_sister.title] and [the_person.title] are making progress in their physical relationship."
        else:
            "Judging from the footage, it seems like [the_sister.title] and [the_person.title] are taking things pretty fast in their physical relationship."
    "You roll over and try to get to sleep."
    $ scene_manager.clear_scene()
    return

label lily_cuddle_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ temp_outfit = get_pajama_outfit(the_sister)
    "You are stirred awake as your bed is shifted by the weight of someone else climbing on the edge."
    $ scene_manager.add_actor(the_sister, temp_outfit, position = "sitting", emotion = "sad")
    $ scene_manager.apply_outfit(the_sister, temp_outfit)
    "Opening your eyes you are not terribly surprised to see [the_sister.possessive_title] looking at you with a bashful smile."
    the_sister "Sorry to wake you, [the_sister.mc_title], I was having trouble getting to sleep and thought you could help me."
    mc.name "Okay, I don't mind as long as you aren't keeping me up all night."
    if the_sister.arousal_perc < 50:
        the_sister "I hope I don't, but I need some help."
    elif the_sister.arousal_perc < 66:
        the_sister "That's okay, this shouldn't take too long."
    else:
        the_sister "That's okay. This should be quick."
    $ scene_manager.update_actor(the_sister, position = "walking_away")
    "[the_sister.title] slips under the covers next to you."
    "You can feel the heat radiating from her body, and she can't seem to settle down, shifting back and forth endlessly."
    "You roll onto your side and put your arm around [the_sister.title], pulling her close so you can spoon."
    if not the_sister.has_taboo("vaginal_sex") or not the_sister.has_taboo("anal_sex"):
        "As soon as she is in position she pushes back and starts to grind against you."
        mc.name "Were you looking for more than just cuddling [the_sister.title]?"
        the_sister "Sorry, yes. [the_person.fname] and I were fooling around earlier and it left me wanting more."
        the_sister "She's fun, but nothing compares to your big hard cock."
        "[the_sister.title] sighs and snuggles closer to you."
        if not the_sister.vagina_visible or not the_sister.tits_visible:
            mc.name "I don't think I'll be able to help you in all those clothes."
            $ scene_manager.update_actor(the_sister, position = "stand2")
            "[the_sister.title] nods and slips out of your arms. She quickly strips out of everything, including her panties, then slides back into bed."
            $ scene_manager.strip_to_vagina(the_sister)
            $ scene_manager.strip_to_tits(the_sister)
            $ scene_manager.update_actor(the_sister, position = "back_peek", emotion = "happy")
            the_sister "Is this better?"
            mc.name "Much."
        "You slip an arm around her chest and grab hold of a tit, then grind your hips against her ass a little bit."
        $ the_sister.change_arousal(5)
        "[the_sister.title] just lays next to you and moans softly while you play with her."
        "After a few minutes you slide your pants down and pull your cock out."
        mc.name "You've got me all worked up now too [the_sister.title]. We're going to have to take care of this before I can get to sleep."
        the_sister "I'm sorry. Do whatever you want, it's my fault anyway."
        "You slip your cock between her legs and run the tip along her pussy. [the_sister.title] moans softly, but stays perfectly still for you."
        $ the_sister.change_arousal(5)
        mc.name "That's a good girl, stay just like that until I'm finished."
        if not the_sister.has_taboo("vaginal_sex"):
            "Once you've gotten your tip wet from her juices you slide all the way into your sister."
            "[the_sister.title] gasps the first few times you pump into her, but before long the only noises she's making are soft moans. You pinch her nipple and roll it between your fingers while you fuck her."
            $ the_sister.change_arousal(5)
            "With her legs together [the_sister.title]'s pussy is incredibly tight, and within a few minutes you're ready to finish."
            $ the_sister.change_arousal(5)
            "You pump faster, bumping your hips into her ass each time, then begin to fire your load inside her."
            if the_sister.has_role(breeding_fetish_role):
                the_sister "Oh god, yes! Fill me up!"
                "[the_sister.title] quivers with pleasure, suddenly climaxing at the same time as you."
            else:
                "[the_sister.title] gasps in surprise, but still doesn't move."
            $ the_sister.have_orgasm(sluttiness_increase_limit = 50, reset_arousal = False, add_to_log = True)
            "You hold yourself tight against her, then give a few final thrusts before pulling out. [the_sister.title] sighs as you slip out of her, going limp against you."
            mc.name "That was great [the_sister.title]. Now we can get to bed."
            if the_sister.has_role(breeding_fetish_role) or the_sister.on_birth_control:
                "[the_sister.title] nods and cuddles closer to you. You fall asleep together, your cum dripping slowly out of her pussy."
            elif the_sister.knows_pregnant:
                "[the_sister.title] nods and cuddles closer to you as you rest on hand on her swelling belly. You fall asleep together, your cum dripping slowly out of her pussy."
            else:
                the_sister "We have to be more careful in the future [the_sister.mc_title], that or I need to start taking my birth control again. Eventually you're going to get me pregnant like this..."
                "[the_sister.title] cuddles closer to you. You fall asleep together, your cum dripping slowly out of her pussy."
        else:
            "Once you've gotten your tip wet from her juices you shift backward and slide all the way into your sister's ass."
            "[the_sister.title] gasps the first few times you pump into her, but before long the only noises she's making are soft moans. You pinch her nipple and roll it between your fingers while you fuck her ass."
            $ the_sister.change_arousal(5)
            "With her legs together [the_sister.title]'s ass is incredibly tight, and within a few minutes you're ready to finish."
            $ the_sister.change_arousal(5)
            "You pump faster, bumping your hips into her ass each time, then begin to fire your load into her bowels."
            if the_sister.has_role(cum_fetish_role):
                the_sister "Oh god, yes! Fill me up!"
                "[the_sister.title] quivers with pleasure, suddenly climaxing at the same time as you."
            else:
                "[the_sister.title] gasps in surprise, but still doesn't move."
            $ the_sister.have_orgasm(sluttiness_increase_limit = 50, reset_arousal = False, add_to_log = True)
            "You hold yourself tight against her, then give a few final thrusts before pulling out. [the_sister.title] sighs as you slip out of her, going limp against you."
            mc.name "That was great [the_sister.title]. Now we can get to bed."
            "[the_sister.title] nods and cuddles closer to you. You fall asleep together, your cum dripping slowly out of her ass."
    elif not the_sister.has_taboo("touching_vagina"):
        the_sister "Oh, hey there."
        mc.name "There isn't much room on the bed, so we're going to have to get nice and close."
        the_sister "You're right. In that case..."
        $ mc.change_locked_clarity(10)
        $ scene_manager.update_actor(the_sister, position = "stand2")
        "[the_sister.title] slips out of your arms and stands up, pulling her pajamas off and leaving them in a pile. When she's down to just her underwear she slips back in and slides against you."
        $ scene_manager.strip_to_underwear(the_sister)
        the_sister "I don't want to get too hot, if we're right next to each other."
        $ scene_manager.update_actor(the_sister, position = "back_peek")
        if the_sister.tits_visible:
            "She pulls your arm around her again, planting your hand firmly on one of her naked tits. While she's getting comfortable she also rubs her ass up and down against your hard cock."
        else:
            "She pulls your arm around her again, planting your hand firmly on one of her tits. While she's getting comfortable she also rubs her ass up and down against your hard cock."
        $ scene_manager.update_actor(the_sister, temp_outfit)
        $ mc.change_locked_clarity(10)
        mc.name "Easy there [the_sister.title], or I'm going to have to repay the favour."
        "You pinch her nipple between a finger and thumb and she gasps."
        $ the_sister.change_arousal(5)
        mc.name "Or maybe that's what you want, right? To be played with?"
        "You slip your other hand down her legs, rubbing the inside of her thighs."
        the_sister "No, I just couldn't sleep and want to be comfortable."
        "[the_sister.title] moans while you play with her tits, then gasps again when you rub a finger along the length of her pussy."
        $ the_sister.change_arousal(5)
        mc.name "You're already wet, what's really going on?"
        the_sister "Okay... so me and [the_person.fname] were fooling around and well... I'm so horny, I need more."
        mc.name "So you came to me to see if I could help you get off?"
        $ scene_manager.strip_to_vagina(the_sister, prefer_half_off = True)
        "You pull her panties to the side and slip two fingers inside her, causing her to moan and arch her back a little bit."
        $ the_sister.change_arousal(5)
        the_sister "No, I just... ah..."
        mc.name "Don't say a word, I'll take care of you."
        "You knead your sister's breast with one hand while you finger her with the other. She was already wet when you slid your hand down, and now she's completely soaked."
        $ the_sister.change_arousal(5)
        "[the_sister.title] pants and moans, gasping any time your fingers brush against her clit. After a few minutes you feel her thighs start to tighten up around your hand."
        $ the_sister.change_arousal(5)
        mc.name "Are you getting close?"
        "[the_sister.title] whimpers and nods, legs clenching up."
        $ the_sister.change_arousal(5)
        "You finger her faster for a while, then pull out and rub her clit as fast as you can with two fingers."
        $ the_sister.change_arousal(5)
        "[the_sister.title] tenses up, curling into a ball and moaning loudly. Her breathing comes in short gasps for a few moments while you keep playing with her through her orgasm."
        $ the_sister.have_orgasm(sluttiness_increase_limit = 50, reset_arousal = False, add_to_log = True)
        "Finally you stop and let her recover. She straightens out on the bed again and pushes herself back against you."
        mc.name "Was that good?"
        the_sister "Mmhm. Thank you."
        mc.name "Good. Now let's get to sleep."
        "You hold [the_sister.title] next to you as you both drift off to sleep."
    elif not the_sister.has_taboo("touching_body"):
        the_sister "Hey!"
        mc.name "There isn't much room on the bed [the_sister.title]. If you want to sleep in here we're going to have to be close to each other."
        "[the_sister.title] thinks for a moment, then nods and pulls closer to you. You wrap an arm around her torso, ending up with one hand cupping a boob."
        $ mc.change_locked_clarity(10)
        the_sister "Comfortable?"
        mc.name "Ya, that feels good. Goodnight [the_sister.title]."
        the_sister "Goodnight [the_sister.mc_title]."
        "You both drift off to sleep cuddling with each other."
        $ the_sister.change_stats(happiness = 5, slut = 2)
    else:
        the_sister "Hey!"
        mc.name "There isn't much room on the bed [the_sister.title]. If you want to sleep in here we're going to have to be close to each other."
        the_sister "Sorry, this was a bad idea. I'll just go back to my room."
        $ the_sister.change_stats(slut = 2)
    $ scene_manager.clear_scene()
    return

label buddy_gossip_label(the_person):
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 6:
        $ scene_manager.add_actor(the_person)
        "It's been a while since you checked in with [the_person.title] so you approach her on campus."
        the_person "Hey [the_person.mc_title], how are you doing?"
        mc.name "I've been pretty good, but what about you? How are things going?"
        "[the_person.possessive_title!c]'s cheeks flush slightly."
        "There good... there's something I've been wanting to talk to you about. It involves [the_sister.fname]."
        mc.name "Oh? What about her?"
        the_person "Well... we've been seeing each other more often lately. Spending time together outside of class."
        "A mischievous grin spreads across her lips."
        the_person "And things have been getting pretty intense between us."
        "You nod slowly."
        the_person "She's just so amazing [the_person.mc_title], her body feels so good against mine, and when she kisses me... oh god, it makes me crazy."
        mc.name "Um, well, that's... great, I guess?"
        "Your voice sounds a little unconvinving, and [the_person.title] seems to notice the discomfort."
        the_person "Oh, sorry, I guess that was a bit inappropriate."
        the_person "I just wanted to fill you in. I know we've had some difficulty in the past, but I really value your opinion and advice."
        mc.name "Of course, it's been a long road for us, but I'm happy with where the three of us are right now."
        the_person "Thanks, I knew I could count on you!"
    else:
        $ scene_manager.add_actor(the_person, position = "sitting")
        "As you make your way across campus, you spot [the_person.title] sitting on a nearby bench, staring off in the distance."
        "Without thinking too much about it, you decide to join her."
        "You wave when you get close, but she doesn't notice until you walk right up and say hello."
        the_person "Hey there, sorry, I was a bit lost in thought."
        mc.name "Everything okay?" 
        the_person "Better than okay, I think I know what they mean by head over heels in love now."
        mc.name "So you and [the_sister.fname] are having fun?"
        the_person "Oh my god, [the_person.mc_title], you would not believe how amazing last night was!"
        the_person "[the_sister.fname] and I went out for dinner, then we ended up at this super sexy club..."
        the_person "The music was incredible, and the atmosphere was just electric. We started dancing together, and pretty soon we couldn't keep our hands off each other."
        "Her voice drops to a husky whisper as she leans closer to you."
        the_person "She was grinding against me so hard, I swear I could feel every inch of her through our clothes."
        the_person "And when she wrapped her legs around my waist and arched her back... God, it was like nothing I've ever experienced before."
        "She bites her bottom lip, remembering the sensation clearly."
        "Her hands flutter nervously in her lap, but eventually find their way back to her thigh, tracing tiny circles along the muscle."
        the_person "And then we found this private little area where we could be alone, and she undid my top and started sucking on my nipples... It felt incredible." 
        "Her eyes meet yours, searching for approval or understanding."
        the_person "I never knew she had it in her, it makes me want to explore even more... With her, I mean."
        "The more she talks, the harder it becomes to concentrace on anything besides the images forming in your mind."
        "Your cock strains painfully against your pants, and when she is staring off into space you take a moment to adjust yourself."
        if not the_person.has_taboo("touching_penis") or not the_person.has_taboo("sucking_cock") or not the_person.has_taboo("touching_body"):
            the_person "Is everything alright down there?"
            "She's caught you, and rests her hand on your thigh, rubbing up towards your crotch."
            the_person "I'm sorry [the_person.mc_title]! Here, let me help you with that."
            "Her fingers brush lightly against your erection, causing a wave of pleasure to ripple through your entire body."
            "Taking a deep breath, you nod slowly and close your eyes as she starts to stroke you."
            "After a quick look around at your surroundings, she opens your pants and lets your cock spring free."
            if not the_person.has_taboo("sucking_cock"):
                the_person "Yep, I was right you definitely need my help."
                call get_fucked(the_person, start_position = blowjob) from _call_get_fucked_buddy_gossip_1
            elif not the_person.has_taboo("touching_body") and the_person.has_large_tits:
                call get_fucked(the_person, start_position = tit_fuck) from _call_get_fucked_buddy_gossip_2
                the_person "Feeling better?"
            else:
                call get_fucked(the_person, start_position = handjob) from _call_get_fucked_buddy_gossip_3
            "You nod, still trying to catch your breath."
            mc.name "Yeah... thanks. That was really intense"
        else:
            "When she looks back, her eyes widen a bit, can she see the effect her story had on you?"
            the_person "I'm sorry [the_person.mc_title]! I shouldn't be talking about [the_sister.fname] like that to you... her brother."
            mc.name "It's okay, I'm just glad you're happy."
            the_person "I am happy. Really happy, and I'm pretty sure she is too."
            mc.name "Good, then I'm always here for you if you need someone to talk too."
        the_person "Now, I really should get going. Thanks for listening."
        "With one last glance in your direction she turns and walks away, disappearing around the corner of a building."
    $ the_person.change_stats(happiness = 10, obedience = 10, slut = 2)
    $ scene_manager.clear_scene()
    return
