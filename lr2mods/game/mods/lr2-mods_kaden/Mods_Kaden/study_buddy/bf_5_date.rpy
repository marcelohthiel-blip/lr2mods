init 4 python:
    def lily_buddy_corruption_requirement(the_day):
        if not lily.event_triggers_dict.get("pending_lesbian_lesson", False):
            if lily.available and get_lab_partner().available:
                if day%7 not in [0, 1, 4]:
                    if not (erica.event_triggers_dict.get("insta_pic_intro_complete", False) and day%7 == 5):
                        if time_of_day > 2:
                            if day > the_day + TIER_1_TIME_DELAY:
                                return True
        return False

    def teaching_request_requirement(the_person, the_day):
        if not lily.event_triggers_dict.get("pending_lesbian_lesson", False):
            if time_of_day > 3:
                if day >= the_day + TIER_1_TIME_DELAY:
                    if the_person.is_available:
                        if day%7 not in [0, 1, 4]:
                            return True
        return False

    def lesbian_teaching_requirement(the_person, the_day):
        if time_of_day > 3:
            if day >= the_day + TIER_1_TIME_DELAY:
                if the_person.is_available:
                    if day%7 not in [0, 1, 4]:
                        return True
        return False

# 8/9/10: recording unlock, only one girl orgasms, needy girl asks for help, disappointing girl ask for teaching
# 11/12/13: recording unlock, both girls cum, one girl ask for bonus lessons
label lily_buddy_corruption_label(): #8/9/10 and 11/12/13
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ the_person.event_triggers_dict["friend_with_benefits"] = the_person.event_triggers_dict.get("friend_with_benefits", 0) + 1
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 11:
        if the_sister.sluttiness + the_sister.event_triggers_dict.get("orgasm_guilt", 0) > the_person.sluttiness + the_person.event_triggers_dict.get("orgasm_guilt", 0):
            $ lily_overnight = Action("[the_person.title] Overnight", lily_followup_requirement, "lily_overnight_label")
            $ mc.business.add_mandatory_crisis(lily_overnight)
            $ person_one = the_person
            $ person_two = the_sister
        else:
            $ best_friend_overnight = Action("Best Friend Overnight", lily_followup_requirement, "best_friend_overnight_label")
            $ mc.business.add_mandatory_crisis(best_friend_overnight)
            $ person_one = the_sister
            $ person_two = the_person
        $ teaching_request = Action("Teaching Request", teaching_request_requirement, "teaching_request_label", args=[person_one, person_two], requirement_args=[person_one, day])
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 14:
        if the_sister.sluttiness > the_person.sluttiness and the_person.event_triggers_dict.get("lesbian_lessons", 0) < 5:
            $ person_one = the_person
            $ person_two = the_sister
        elif the_sister.event_triggers_dict.get("lesbian_lessons", 0) < 5:
            $ person_one = the_sister
            $ person_two = the_person
        else:
            $ person_one = the_person
            $ person_two = the_sister
        if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 13:
            $ teaching_request = Action("Training Request", teaching_request_requirement, "training_request_label", args=[person_one, person_two], requirement_args=[person_one, day])
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 13:
        $ mc.business.add_mandatory_crisis(teaching_request)
    #recordings unlock
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 7:
        if "Lesbian Failure 1" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lesbian Failure 1")
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 8:
        if "Lesbian Failure 2" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lesbian Failure 2")
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 9:
        if "Lesbian Failure 3" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lesbian Failure 3")
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 10:
        if "Lesbian Success 1" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lesbian Success 1")
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 11:
        if "Lesbian Success 2" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lesbian Success 2")
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 12:
        if "Lesbian Success 3" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Lesbian Success 3")
    #effect on girls
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 14:
        $ person_one.change_stats(happiness = 5, slut = 5, arousal = 30)
        $ lesbian_orgasm(person_one)
        if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 11:
            $ person_two.change_stats(happiness = -5, arousal = 30)
            $ person_one.event_triggers_dict["orgasm_guilt"] = person_one.event_triggers_dict.get("orgasm_guilt", 0) + 20
        else:
            $ person_two.change_stats(happiness = 5, slut = 5, arousal = 30)
            $ lesbian_orgasm(person_two)
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
        "From time to time you hear a bed squeaking and once or twice it crashes into the wall. When it does there is some giggling followed by extreme silence."
        if not mc.business.event_triggers_dict.get("home_cameras", []):
            "You wonder if they really think their activities are going unnoticed, and once again wish you had picked up a camera."
        else:
            "You wonder if they really think their activities are going unnoticed, and once again are glad you picked up a camera."
            if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 9:
                call lesbian_fail_1(person_one, person_two) from _call_lesbian_fail_1_bf
                "You are concerned about [person_one.title] and how frustrated she seemed when she couldn't reciprocate for her girlfriend."
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 10:
                call lesbian_fail_2(person_one, person_two) from _call_lesbian_fail_2_bf
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 11:
                call lesbian_fail_3(person_one, person_two) from _call_lesbian_fail_3_bf
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 12:
                call lesbian_success_1(person_one, person_two) from _call_lesbian_success_1_bf
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 13:
                call lesbian_success_2(person_one, person_two) from _call_lesbian_success_2_bf
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 14:
                call lesbian_success_3(person_one, person_two) from _call_lesbian_success_3_bf
            if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 11:
                if person_two == lily:
                    "While it is a shame [person_two.title] didn't get her release, you do hope you might be able to help her again."
                else:
                    "While you feel bad that [person_two.title] didn't get off, you know their relationship is strong enough to get past it."
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 12:
                "It is nice to see that your lessons have paid off, and both girls are getting what they need, although you do wonder if that means you won't get to play with them any more."
            elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 13:
                "It's nice to see both girls getting what they need, and you are looking forward to helping them improve even more."
            else:
                "It looks like you might have taught the girls all you could, you wonder where things will go from here."
    $ scene_manager.clear_scene
    return
    
label lily_overnight_label():
    $ the_person = get_lab_partner()
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 11:
        return
    $ the_sister = lily
    $ scene_manager = Scene()
    $ temp_outfit = get_pajama_outfit(the_sister)
    $ scene_manager.add_actor(the_sister, temp_outfit, emotion = "sad")
    "Lying in bed with the lights off, you are preparing to sleep after a long day. Suddenly there is a soft noise at your door."
    "It opens slightly and [the_sister.possessive_title] quickly slips in and pushes it closed."
    if the_sister.event_triggers_dict.get("first_overnight", True):
        mc.name "Hey [the_sister.title]."
        the_sister "Shh... I don't want Mom to hear us."
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            mc.name "You know she is fine with basically anything we do now right?"
            the_sister "I know, but I just want you to myself tonight."
        else:
            mc.name "Do you have something planned that she shouldn't find out about?"
            the_sister "Yeah, it would be a bit embarrassing if she picked the wrong moment to walk in."
        mc.name "Really? Didn't get enough with [the_person.title]?"
        the_sister "No, she's gone for the night, that's the problem."
        "Sensing that there is more going on here, you press for details."
        if not the_sister.has_taboo("touching_vagina"):
            mc.name "How can I help you, [the_sister.title]?"
            the_sister "[the_person.title] and I... she tried really hard tonight, but she just couldn't make me orgasm."
            if mc.business.event_triggers_dict.get("home_cameras", []):
                "Your heart races, remembering the video you just watched between them."
            else:
                "Your heart races, imagining the scene that unfolded between them."
            mc.name "I understand... maybe I could help?"
            $ temp_top = the_sister.outfit.get_upper_top_layer
            the_sister "I'd hoped you might say that, it's why I'm here."
            if temp_top:
                "[the_sister.title] nods eagerly, her nipples poking through her [temp_top.display_name]."
            else:
                "[the_sister.title] nods eagerly, her [the_sister.tits_description] jiggling enticingly."
            "You guide her towards your bed and then step away towards your door."
        else:
            mc.name "What's wrong?"
            the_sister "It's... um, it's about [the_person.title], we were trying to be intimate earlier, but she just couldn't make me orgasm."
            "Her voice cracks slightly, revealing her frustration and disappointment."
            "You swallow hard, trying to hide your own arousal."
            mc.name "Don't worry about it, [the_sister.title]. Sometimes things just don't work out that way."
            the_sister "But I'm so horny, I need to cum."
            mc.name "Maybe I could help?"
            "You eye her up and down hungrily as [the_sister.title] blushes deeper, understanding your meaning."
            the_sister "R-Really?"
            mc.name "Of course, come here."
            "As she approaches, you can't help but admire her curves and the way her [the_sister.tits_description] bounce slightly with each step."
            "You wrap her up in an embrace and plant a kiss on her forehead, before turning to look at your door."
    else:
        mc.name "Welcome back [the_sister.title]."
        mc.name "Another unsatisfying night with [the_person.title]?"
        the_sister "You could say that. She's trying but doesn't ever seem to be able to get me off like you."
        the_sister "Do you think you could help me out again?"
        if mc.business.event_triggers_dict.get("family_threesome", False):
            menu:
                "Help her":
                    pass
                "Not tonight":
                    mc.name "I'm sorry [the_sister.title], as nice as it is to have you here I am just too tired."
                    mc.name "Why don't you go see if Mom can help you?"
                    the_sister "Oh... okay. Have a good night [the_sister.mc_title]."
                    $ the_sister.change_stats(love = -2, happiness = -2, obedience = 2)
                    #TODO video 
                    call lesbian_sex(the_sister, mom, path = ["finger1", "finger1", "finger1", "oral1", "oral1", "oral1"]) from _call_lesbian_sex_lily_overnight
                    $ scene_manager.clear_scene()
                    return
        mc.name "Of course, you know I'm always happy to help you."
        "You gesture towards your bed, inviting [the_sister.title] further into the room before stepping towards your door."
    "You quickly check that the door is closed and locked then turn back to [the_sister.title]."
    call help_to_orgasm(the_sister, temp_outfit) from _call_help_to_orgasm_sister
    if the_sister.event_triggers_dict.get("first_overnight", True):
        mc.name "So... what does this mean for you and [the_person.fname]?"
        the_sister "I don't know. I still like spending time with her..."
        mc.name "Well, there's no reason you need to stop. I'm certainly not going to tell her about this."
        the_sister "I figured you could keep this secret, but it's not even really like I'm cheating."
        the_sister "We aren't exclusive or anything yet, just kinda playing around. You know... trying things."
        the_sister "Plus, we talked a bit about what she used to do with you when we were supposed to be studying."
        mc.name "Then I guess we'll all just keep trying things."
    if the_sister.has_role(slave_role) and wakeup_duty_crisis not in mc.business.mandatory_morning_crises_list:
        $ slave_add_wakeup_duty_action(the_sister)
        mc.name "You can't leave [the_sister.title]."
        the_sister "What?"
        mc.name "I'm going to need you to return this favour in the morning. Find some place comfortable on the floor and wake me up tomorrow."
        the_sister "Right, yes [the_sister.mc_title]."
    if the_sister.event_triggers_dict.get("first_overnight", True) and the_person.event_triggers_dict.get("first_overnight", True):
        "Now that [the_sister.title] has come to you for help you wonder if there is any possibility of [the_person.title] needing you as well."
    elif not the_person.event_triggers_dict.get("first_overnight", True) and the_sister.event_triggers_dict.get("first_overnight", True):
        "Now that both [the_person.title] and [the_sister.title] have come looking for help you wonder what it would take to get them to both join you at the same time."
    "You turn off the light by your bed and quickly sink into a satisfied sleep."
    $ the_sister.event_triggers_dict["first_overnight"] = False
    $ scene_manager.clear_scene()
    return

label best_friend_overnight_label():
    $ the_person = get_lab_partner()
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 11:
        return
    $ the_sister = lily
    $ scene_manager = Scene()
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    "Lying in bed with the lights off, you are preparing to sleep after a long day. Suddenly there is a soft knock at your window."
    if the_person.event_triggers_dict.get("first_overnight", True):
        "Curiously, you roll out of bed and walk over, where you are startled to see [the_person.fname] standing just outside."
        $ scene_manager.add_actor(the_person, temp_outfit, emotion = "sad")
        "She is wearing her school uniform, but looks a bit disheveled."
        "Looking closer you also see her biting her lip nervously, her eyes filled with desire."
        "You are a bit puzzled, but since she is gesturing for you to open the window you move to comply."
        mc.name "[the_person.title]? What are you doing here? Is everything okay?"
        the_person "We need to talk, can I come in?"
        mc.name "Um, yeah, you know you could have just walked down the hall."
        the_person "No, [the_sister.fname] can't know I'm here. I had to leave and then sneak back."
        the_person "Can you give me a hand?"
        "You hold out a hand and help her through the window as quietly as you can, and then give her a moment to straighten herself out."
        mc.name "So.... how can I help you?"
        "[the_person.title] steps closer, close enough that you can feel the heat radiating off her body."
        the_person "This is kind of awkward, you know since I broke up with you, but could we maybe..."
        "[the_person.title] stammers to a halt and blushes very red. Suddenly her appearance takes on a new meaning."
        mc.name "Wait, is this a booty call? Weren't you and [the_sister.fname] just... you know...."
        the_person "We were... and it was great. I'm really glad that I'm getting to explore something with her."
        the_person "It's just... she got tired... and I didn't get to... you know... finish."
        mc.name "So it is a booty call? You just want to use me to get yourself off."
        the_person "...I mean... if you don't mind?"
        "[the_person.title] trails a finger along your arm, bringing her other hand up to fondle her own breast."
        the_person "We used to have so much fun together. I think you probably miss it too."
        "It is pretty tempting, having [the_person.possessive_title] offer herself to you after your breakup, but what about [the_sister.possessive_title]?"
        mc.name "What about [the_sister.fname]? You want me to let you cheat on my sister and not tell her?"
        the_person "It's not really cheating. We aren't exclusive or anything yet, just kinda playing around. You know... trying things."
        the_person "Plus, we talked a bit about what I used to do with you when we were hanging out."
        mc.name "So she knows that you and I..."
        the_person "Yeah, and it's fine. We're both in college, and keeping things casual for now."
        "With that said, [the_person.title] moves towards your bed. It is pretty clear she thinks the issue is settled."
    else:
        $ scene_manager.add_actor(the_person, emotion = "happy")
        "It's [the_person.title] again, practically bouncing with excitement as she looks in at you."
        "It is pretty clear why she is back again so you quickly move to open the window."
        "You help her through the opening and then pull her into an embrace."
        mc.name "I feel a bit bad that you need my help again, but I'd be lying if I said I wasn't looking forward to assisting you."
        the_person "Honestly I'm a bit excited too. It feels disloyal to say this, but you are so much better than [the_sister.fname] at this part."
    the_person "Why don't you get the window and I'll get ready for you."
    "You quickly pull the window shut and turn back to [the_person.title]."
    call help_to_orgasm(the_person, temp_outfit) from _call_help_to_orgasm_buddy
    if the_person.has_role(slave_role) and wakeup_duty_crisis not in mc.business.mandatory_morning_crises_list:
        $ slave_add_wakeup_duty_action(the_person)
        mc.name "You can't leave [the_person.title]."
        the_person "What?"
        mc.name "Well, first of all [the_sister.fname] could be out there and it would be hard to explain why you are coming out of my room."
        "She turns and starts to make her way to the window instead."
        mc.name "Also, I'm going to need you to return this favour in the morning. Find someplace comfortable on the floor and wake me up tomorrow."
        the_person "Right, yes [the_person.mc_title]."
    else:
        mc.name "Aren't you forgetting something?"
        "You catch her just as her hand is on the door and she turns to look back at you."
        $ scene_manager.update_actor(the_person, position = "back_peek")
        "With a smile you point towards the window she used to climb into your room."
        "She groans slightly, but does turn the rest of the way and make her way to the window."
        menu:
            "Help her out":
                $ the_person.change_love(2)
                "You get up and give her a hand getting out, earning you a quick kiss on the cheek before she leaves."
            "Just watch":
                $ the_person.change_obedience(2)
                "You just watch from your bed as she struggles her way out."
    if the_sister.event_triggers_dict.get("first_overnight", True) and the_person.event_triggers_dict.get("first_overnight", True):
        "Now that [the_person.title] has come to you for help you wonder if there is any possibility of [the_sister.title] needing you as well."
    elif not the_sister.event_triggers_dict.get("first_overnight", True) and the_person.event_triggers_dict.get("first_overnight", True):
        "Now that both [the_person.title] and [the_sister.title] have come looking for help you wonder what it would take to get them to both join you at the same time."
    "You turn off the light by your bed and quickly sink into a satisfied sleep."
    $ the_person.event_triggers_dict["first_overnight"] = False
    $ scene_manager.clear_scene()
    return

label help_to_orgasm(person_one, temp_outfit):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(person_one, temp_outfit, emotion = "happy")
    if mc.energy < 50:
        $ person_one.event_triggers_dict["first_overnight"] = False
    "You return to [person_one.title] wrapping her up in an intimate embrace."
    "Feeling the warmth of her body against you as the familiar scent of her perfume fills your nose causes your cock to stir."
    "You wrap an arm around her waist and pull her closer still, your hips grinding together in a primal dance full of unspoken desires."
    "Your free hand finds its way to her ass cheek, squeezing gently before tracing upwards along her spine."
    if person_one.has_taboo("kissing"):
        $ person_one.call_dialogue("kissing_taboo_break")
        $ person_one.break_taboo("kissing")
    "Looking deep into her eyes, you lean in for a kiss, pushing your tongue against her lips until they gap open for you."
    "Shifting to the side, you breathe into her ear, nibbling softly on her lobe as one hand begins to work at her clothes."
    mc.name "Tell me what you want, show me how much you need this."
    "She shivers with anticipation beneath your touch, arching her back slightly as if begging for more contact."
    person_one "I just... I need release."
    if person_one.event_triggers_dict.get("first_overnight", True):
        if not person_one.has_taboo("sucking_cock") or not person_one.has_taboo("vaginal_sex") or not person_one.has_taboo("anal_sex"):
            "[person_one.title] is desperately horny. How would you like to go about getting her off?"
            menu:
                "Fingering":
                    $ temp_path = "fingering"
                "Oral" if not person_one.has_taboo("sucking_cock"):
                    $ temp_path = "oral"
                "Vaginal" if not person_one.has_taboo("vaginal_sex"):
                    $ temp_path = "vaginal"
                "Anal" if not person_one.has_taboo("anal_sex"):
                    $ temp_path = "anal"
        else:
            $ temp_path = "fingering"
    "Her words are punctuated by heavy pants as she struggles to control herself under your gaze—a gaze filled with lust and understanding."
    $ old_outfit = temp_outfit.get_copy()
    call strip_while_grope(person_one, temp_outfit) from _call_stripe_while_grope_help_to_orgasm
    $ scene_manager.update_actor(person_one, position = "missionary", emotion = "happy")
    "Once she is naked [person_one.title] drops back onto your bed, ready for you to take care of her."
    "As you climb on top of her, [person_one.title] leans up, her lips finding yours once again in a hungry kiss that sends shivers down your spine."
    $ body_word = get_body_word(person_one)
    "Your tongue dances with hers while one hand cups her breast tenderly, rolling her nipple between thumb and forefinger as your other hand slips lower to squeeze her [body_word] ass."
    "She moans into your mouth, legs trembling as she clings tightly to you."
    "You break the kiss long enough to look into her eyes, seeing nothing but desire reflected back at you."
    "You move your head, starting with soft kisses along her jawline before moving down towards her neck where you gently nibble on her skin."
    "This elicits moans of pleasure from deep within her throat."
    "Your hands roam over her body, exploring every curve and contour as if for the first time."
    "As one hand travels further southward, it finds its way between her legs, parting them ever so slightly to reveal her wetness."
    "The scent of arousal fills the air as you tease her entrance with gentle fingers, circling around but never quite penetrating."
    "Her hips buck against you in response, begging for the release that she needs so badly."
    "With each passing second, she becomes more desperate for satisfaction—a sight that ignites something inside you: a powerful feeling of control."
    mc.name "[person_one.title], you're so beautiful."
    "Your mouth finds hers again in a tender yet demanding kiss while your other hand cups her breast firmly, massaging it gently as you continue to tease her folds with skillful fingers."
    "She whimpers into your mouth, arching her back off the bed as she seeks relief from your touch."
    if person_one.event_triggers_dict.get("first_overnight", True):
        if temp_path == "fingering":
            "You take this as an invitation to increase pressure; thrusting two fingers inside her tight channel while pinching her nipple roughly between thumb and forefinger."
            "Her cries intensify now, muffled by your kiss as she grinds herself against your hand."
            "Her orgasm builds rapidly under your skilled ministrations until finally she gasps your name and shudders violently around your fingers."
            $ person_one.have_orgasm()
            "Waves of pleasure wash over her body like water crashing upon the shore, leaving her panting."
            "When she finally subsides, you lay down beside her. You can feel the rapid thrum of her heartbeat beating in her chest."
            person_one "Thank you, that was amazing."
            "You squeeze her hand reassuringly."
            mc.name "You're welcome, [person_one.title]. Anytime."
        elif temp_path == "oral":
            "You can tell she's close, but something tells you she needs more. You slide down the bed."
            "Dipping your head, you take her pretty pussy into your mouth, sucking on her clit while your fingers explore her soaking wet folds."
            "Her scent fills your nostrils, making you dizzy with desire."
            "She cries out, clawing at the sheets, losing control entirely."
            "And then, finally, she orgasms, her whole body shuddering violently as wave after wave of pleasure washes over her."
            $ person_one.have_orgasm()
            "You drink in every sound, every movement, savoring this moment of power."
            "When she finally subsides, you crawl up beside her. You can feel the rapid thrum of her heartbeat beneath your palm."
            person_one "Thank you, that was amazing."
            "You squeeze her hand reassuringly."
            mc.name "You're welcome, [person_one.title]. Anytime."
        else:
            $ scene_manager.update_actor(person_one, position = "walking_away", emotion = "happy")
            "Taking control, you roll her over to lie down on her stomach."
            "Your heart races as you kneel behind her, running your hands up and down her smooth skin."
            "Gently, you spread her cheeks, exposing her tight little holes, and she lets out a soft moan of submission."
            if temp_path == "anal":
                "Running a finger along her wet slit, you gather enough lubrication to gently push against her puckered rosebud."
                "After a few probing thrusts, you add another finger, widening her more in preparation for the next step."
            else:
                $ scene_manager.update_actor(person_one, position = "doggy", emotion = "happy")
                "Gripping her by the waist, you pull her up slightly, lifting her hips off the bed and allowing you more direct access to her dripping wet pussy."
            "Without further words, you push your cock deep inside her from behind, filling her up completely."
            "It takes a few forceful thrusts before you find a steady rhythm, matching her moans with your own grunts of pleasure."
            "As you pick up speed, [person_one.title]'s body quivers in anticipation, begging for release."
            "After a few moments, you feel her body start to tremble beneath you."
            mc.name "That's it [person_one.title], cum for me."
            "She responds with a long, low moan, acknowledging your dominance."
            "And then, with one final thrust, you bury yourself to the hilt, wrapping a hand around to press against her clit."
            "She cums hard, screaming out your name as waves of ecstasy wash over her."
            $ person_one.have_orgasm()
            "The spasms trembling through her body are enough to push you over the edge."
            if temp_path == "anal":
                $ climax_controller = ClimaxController(["Cum inside her", "anal"],["Cum on her ass", "body"])
                $ the_choice = climax_controller.show_climax_menu()
            else:
                $ climax_controller = ClimaxController(["Cum inside her","pussy"], ["Cum on her ass", "body"])
                $ the_choice = climax_controller.show_climax_menu()
            if the_choice == "Cum inside her":
                "You pull back on [person_one.possessive_title]'s hips, holding your cock deep inside her as you cum."
                if temp_path == "anal":
                    "Her body trembles and shudders as you pump ropes of cum deep into her bowels."
                    $ person_one.cum_in_ass()
                else:
                    "Her body trembles and shudders as you pump ropes of cum deep into her womb."
                    $ person_one.cum_in_vagina()
                $ old_outfit.add_creampie_cum()
                $ scene_manager.update_actor(person_one)
                "Satisfied, you pull out and collapse next to her, wrapping your arms around her waist."
            else:
                "You pull out of [person_one.title] at the last moment, stroking your shaft as you blow your load over her ass."
                $ person_one.cum_on_ass()
                $ old_outfit.add_ass_cum()
                $ scene_manager.update_actor(person_one)
                "Her body trembles and shudders as you cover her ass and lower back with your seed."
                "Satisfied, you sit back on your heels, watching as the aftershocks move through her body, her now empty hole flexing as it closes the gape you left behind."
            "For a moment, neither of you speak, content simply to bask in the afterglow of your mutual satisfaction."
            $ scene_manager.update_actor(person_one, position = "back_peek", emotion = "happy")
            person_one "Thank you, for helping me."
            "She whispers, turning to look at you with a small smile. You grin back in satisfaction."
            mc.name "Anytime, [person_one.title]. Anytime."
    else:
        "Her neediness is exactly what you had hoped for, and it is clear you have a lot of control over what happens next. Looking at her you just need to make a decision."
        call fuck_person(person_one, affair_ask_after = False) from _call_fuck_person_orgasm_help
        $ the_report = _return
        $ the_person.call_dialogue("sex_review", the_report = the_report)
        if the_report.get("girl_orgasms",0)>0:
            person_one "God [person_one.mc_title] that was exactly what I needed."
        else:
            person_one "You too? God, I can't believe no one is able to make me cum."
            $ scene_manager.update_actor(person_one, position = "stand4")
            $ scene_manager.show_dress_sequence(person_one, old_outfit)
            "After quickly pulling on her clothes, [person_one.title] storms out of the room."
            return
    $ person_one.change_stats(obedience = 10, slut = 1, love = 1)
    mc.name "Always happy to help you out."
    person_one "I'll keep that in mind if I'm ever in need again."
    $ scene_manager.update_actor(person_one, position = "sitting")
    if person_one.has_role(trance_role):
        call check_date_trance(person_one) from _call_check_date_trance_best_friend_overnight
    $ scene_manager.update_actor(person_one, position = "stand4")
    $ scene_manager.show_dress_sequence(person_one, old_outfit)
    "With that [person_one.title] gets herself dressed."
    return
    
label strip_while_grope(the_person, temp_outfit, remove_shoes = False, remove_socks = False, remove_top = True, remove_skirt = True):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit)
    $ temp_bra = temp_outfit.get_bra()
    $ temp_panties = temp_outfit.get_panties()
    if temp_panties and temp_panties.is_extension:
        $ temp_panties = None
    $ finished_stripping = 0
    if remove_socks or (temp_outfit.get_lower_top_layer and temp_outfit.get_lower_top_layer.layer > 1 and pelvis_region in temp_outfit.get_lower_top_layer.constrain_regions):
        $ remove_shoes = True
    if temp_outfit.get_panties() and temp_outfit.get_panties().is_extension:
        $ remove_skirt = True
        $ remove_top = True
    while finished_stripping < 5:
        if remove_top and temp_outfit.get_upper_top_layer:
            while temp_outfit.get_upper_top_layer and temp_outfit.get_upper_top_layer.layer == 4: #remove coat
                $ temp_item = temp_outfit.get_upper_top_layer
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                if renpy.random.randint(0,4) == 0:
                    if temp_outfit.get_upper_top_layer:
                        $ next_item = temp_outfit.get_upper_top_layer
                        "You grasp the lapels of [the_person.title]'s [temp_item.display_name] and pull it off her shoulders, revealing a [next_item.display_name] that clings to her curves."
                    else:
                        "You grasp the lapels of [the_person.title]'s [temp_item.display_name] and pull it off her shoulders, revealing her naked torso."
                    "As you peel it away, exposing her smooth skin, goosebumps rise on her arms from the cool air."
                    "Her [the_person.tits_description] jut out enticingly, nipples hardening under your gaze. She shivers with anticipation."
                elif renpy.random.randint(0,3) == 0:
                    "As you slip off [the_person.possessive_title]'s [temp_item.display_name], your hands graze over her shoulders and down her back, sending shivers of pleasure through her body."
                    "She gasps softly as the cool air hits her skin, goosebumps rising in response to your touch."
                    if temp_outfit.get_upper_top_layer:
                        $ next_item = temp_outfit.get_upper_top_layer
                        "Her nipples harden beneath her [next_item.display_name], straining against the fabric as she leans into you, her breath hot on your neck."
                        "You can feel the weight of her [the_person.tits_description] pressed against your arm, aching for release from their confines."
                    else:
                        "Her nipples harden beneath your gaze. She leans into you, her breath hot on your neck."
                        "You can feel the weight of her [the_person.tits_description] pressed against your arm, aching for attention."
                elif renpy.random.randint(0,2) == 0:
                    "As you take off [the_person.possessive_title]'s [temp_item.display_name], your fingers trace along her arms and down her spine, leaving trails of heat in their wake."
                    "Her breath hitches at the sensation, and she lets out a soft moan that echoes in your ear."
                    if temp_outfit.get_upper_top_layer:
                        $ next_item = temp_outfit.get_upper_top_layer
                        "The cooler air hits her bare skin, making her shiver delightfully, and you can feel her nipples pebble against your chest through her [next_item.display_name]."
                    else:
                        "The cooler air hits her bare skin, making her shiver delightfully, and you can feel her nipples pebble against your chest."
                    "Her whole body trembles with anticipation as she stands close to you, craving more intimate contact."
                elif renpy.random.randint(0,1) == 0:
                    "As you help her out of her [temp_item.display_name], [the_person.possessive_title]'s breath catches in her throat, and her eyes flutter closed with pleasure."
                    "A small smile plays at the corners of her mouth when she opens them again, meeting your gaze with a heated stare."
                    the_person "Please, don't stop now."
                else:
                    "You help [the_person.title] remove her [temp_item.display_name], your fingers grazing against her bare skin as you pull it off."
                    "She shivers from the cooler air, but also from the electricity between the two of you."
                    if temp_outfit.get_upper_top_layer:
                        $ next_item = temp_outfit.get_upper_top_layer
                        "The [next_item.display_name] beneath it showcases her [the_person.tits_description] and hardened nipples. Your heart races at the sight of her vulnerability."
                    else:
                        "Your heart races at the sight of her vulnerability."
            $ the_person.update_outfit_taboos()
            if temp_outfit.get_upper_top_layer and temp_outfit.get_upper_top_layer.has_extension and temp_outfit.get_upper_top_layer.layer > 1: #remove dress
                $ temp_item = temp_outfit.get_upper_top_layer
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                if renpy.random.randint(0,1) == 0:
                    if renpy.random.randint(0,1) == 0:
                        "As you reach up to unzip her [temp_item.display_name], your fingers brush against her soft skin, sending shivers down her spine."
                        "The zipper lowers slowly, revealing more of her body with each pull."
                        "You take your time, savoring the anticipation that builds between you as the fabric slips away, exposing her curves."
                        if temp_bra and temp_panties:
                            "Her breath hitches when the [temp_item.display_name] finally falls to the floor, leaving her standing before you in nothing but her [temp_bra.display_name] and [temp_panties.display_name]."
                        elif temp_bra:
                            "Her breath hitches when the [temp_item.display_name] finally falls to the floor, leaving her standing before you in nothing but her [temp_bra.display_name]."
                        elif temp_panties:
                            "Her breath hitches when the [temp_item.display_name] finally falls to the floor, leaving her standing before you in nothing but her [temp_panties.display_name]."
                        else:
                            "Her breath hitches when the [temp_item.display_name] finally falls to the floor, leaving her standing before you completely nude."
                        if len(temp_outfit.feet) < 1:
                            "She steps out of it, kicking the silky material aside, feeling the cool air on her bare legs."
                        else:
                            "She steps out of it, kicking the silky material aside."
                    else:
                        "With eager hands, you grasp the zipper of her [temp_item.display_name] and begin to pull it downwards, the metal teeth making a satisfying sound as they part ways."
                        if temp_bra:
                            "The garment slides off her shoulders, revealing her [temp_bra.display_name] before falling to the ground in a pool at her feet."
                        else:
                            "The garment slides off her shoulders, revealing her [the_person.tits_description] before falling to the ground in a pool at her feet."
                        if temp_bra and temp_panties:
                            "She steps out of it, her body now bared except for her [temp_bra.display_name] and [temp_panties.display_name]."
                        elif temp_bra:
                            "She steps out of it, her body now bared except for her [temp_bra.display_name]."
                        elif temp_panties:
                            "She steps out of it, her body now bared except for her [temp_panties.display_name]."
                        else:
                            "She steps out of it, her body now bared to your gaze."
                        "She kicks the discarded fabric towards you playfully, enjoying the thrill of being so exposed for your eyes alone."
                        "Each motion sends shivers through her core, heightening her arousal as she stands before you achingly beautiful."
                else:
                    if renpy.random.randint(0,1) == 0:
                        "As you grasp the hem of her [temp_item.display_name] and lift it over her head in one fluid motion, her hair cascades around her shoulders like a waterfall, exposing her body to your hungry gaze."
                        "Your fingers trace the line of her collarbone, sending shivers down her spine as they graze across her bare skin."
                        if temp_bra or temp_panties:
                            "With the [temp_item.display_name] now draped over your arm, you admire her figure clad in only underwear. The scent of her arousal fills the air."
                        else:
                            "With the [temp_item.display_name] now draped over your arm, you admire her nude figure. The scent of her arousal fills the air."
                        "She stands before you, legs slightly parted, her breath coming in short gasps as she anticipates what comes next."
                        if temp_bra and temp_panties:
                            "The sight of her curves, accentuated by the lingerie that hugs them tightly, has you aching to touch every inch of her perfect skin."
                        else:
                            "The sight of her curves, has you aching to touch every inch of her perfect skin."
                    else:
                        "As you slowly slide your hands up and down her back, the silky fabric of her [temp_item.display_name] brushing against your fingertips, you feel an electric current course through your veins."
                        "Her breath hitches in anticipation, her heart racing as she leans back against your embrace for support."
                        "The gentle pressure of your palms on her skin sends shivers down her spine, causing goosebumps to form along her arms and legs."
                        if temp_panties:
                            "With each deliberate stroke, the material bunches higher on her thighs, eventually offering you a view of her [temp_panties.display_name]."
                        else:
                            "With each deliberate stroke, the material bunches higher on her thighs, eventually offering you a view of her [the_person.pubes_description] mound."
                        $ body_word = get_body_word(the_person)
                        if temp_bra:
                            $ temp_colour = clothing_colour_name(temp_bra.colour)
                            "Continuing upward you see her [body_word] stomach and the lacy edge of her [temp_colour] [temp_bra.display_name]."
                        else:
                            "Continuing upward you see her [body_word] stomach and [the_person.tits_description]."
                        "Finally, you pull it up, lifting her arms as you slip it over her head."
                        $ temp_colour = clothing_colour_name(temp_item.colour)
                        "The [temp_item.display_name] falls to the floor in a pool of [temp_colour] around her feet, leaving her standing before you, her breasts heaving from excitement and desire."
                $ the_person.update_outfit_taboos()
            if renpy.random.randint(0, 1) == 0 and temp_outfit.get_upper_top_layer:
                if temp_outfit.get_upper_top_layer.layer > 1: #remove shirt
                    $ temp_item = temp_outfit.get_upper_top_layer
                    $ scene_manager.draw_animated_removal(the_person, temp_item)
                    $ temp_outfit.remove_clothing(temp_item)
                    if temp_bra:
                        $ temp_colour = clothing_colour_name(temp_bra.colour)
                        "You carefully peel off [the_person.title]'s [temp_item.display_name], revealing her [temp_colour] [temp_bra.display_name] beneath."
                        "Her nipples are already hard as rocks, poking through the delicate fabric."
                        "Her body trembles with desire. The cool air only serves to heighten her arousal, making her skin flush and her breath quicken."
                    else:
                        "You gently pull [the_person.title]'s [temp_item.display_name] over her head, revealing her soft, supple [the_person.tits_description]."
                        "Her nipples harden under your gaze as you admire their perfect shape and size."
                        "She gasps when the cool air hits them, causing goosebumps to form on her skin."
                        "With a playful smile, you tease one of her nipples with your tongue before kissing it gently, making her moan in response."
                        "The other nipple is next, receiving the same treatment until both are wet and pebbled from your attention."
                    $ the_person.update_outfit_taboos()
                if temp_outfit.get_upper_top_layer and not temp_outfit.get_upper_top_layer.has_extension: #remove bra
                    $ temp_item = temp_outfit.get_upper_top_layer
                    $ scene_manager.draw_animated_removal(the_person, temp_item)
                    $ temp_outfit.remove_clothing(temp_item)
                    if the_person.has_large_tits:
                        "As you gently unclasp her [temp_item.display_name], your fingers grazing over the soft fabric and lace, she gasps in anticipation."
                        "The cool air hits her warm skin, sending shivers down her spine as the delicate garment falls to the ground with a whisper."
                        "Her [the_person.tits_description] are revealed, full and firm, nipples hardening at your touch."
                        "Your eyes drink in the sight of her beauty, and you can't help but lean forward for a closer inspection."
                        "With a gentle hand, you cup one breast, feeling its weight in your palm before giving it a soft squeeze, eliciting a moan from her lips."
                        "You tease her other nipple between your thumb and forefinger, watching as it pebbles under your touch."
                    else:
                        "As you undo the clasp on her [temp_item.display_name], her breath catches in her throat."
                        "The cool air rushes against her heated skin, causing goosebumps to form along her collarbone and across her chest."
                        "Her [the_person.tits_description] are now free, perky and proud, begging for your attention."
                        "You can't resist the urge to caress them, tracing circles around her areolas before pinching each nipple in turn."
                        "She arches her back, moaning deeply as you tease her sensitive peaks, her body craving more of your touch."
                    $ the_person.update_outfit_taboos()
        if remove_shoes and len(temp_outfit.feet) > 0:#remove shoes
                if temp_outfit.feet[0].layer > 1:
                    $ temp_item = temp_outfit.feet[0]
                    $ scene_manager.draw_animated_removal(the_person, temp_item)
                    $ temp_outfit.remove_clothing(temp_item)
                    "As you gently tug at [the_person.possessive_title]'s [temp_item.display_name], the leather comes loose with a soft click."
                    if len(temp_outfit.feet) > 0:
                        $ next_item = temp_outfit.feet[0]
                        "The heel falls to the floor with a dainty thud, revealing her foot, still wrapped up in her [next_item.display_name]."
                    else:
                        "The heel falls to the floor with a dainty thud, revealing her foot now free from constraint."
                    "You continue to massage her instep as you focus on removing the other [temp_item.display_name] in the same way."
                    "This time, the heel hits the ground more firmly, causing it to vibrate slightly beneath your palm."
        if remove_socks and len(temp_outfit.feet) > 0: #remove socks
            if temp_outfit.feet[0].display_name == "socks" or (not temp_outfit.get_lower_top_layer or not upper_leg_region in temp_outfit.get_lower_top_layer.constrain_regions):#remove socks
                $ temp_item = temp_outfit.feet[0]
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                if renpy.random.randint(0,1) == 0:
                    "As you kneel in front of her, your hands gently caress the soft, warm skin of her calves."
                    "Your touch is light and teasing as you begin to slide each sock down, revealing more of her smooth legs with every inch."
                    "Her breath hitches slightly at the sensation, and she can't help but squirm a bit in anticipation."
                    "With each sock removed, her ankles are bared to your gaze, and you take pleasure in watching her blush deepen."
                    "You lean forward, placing a gentle kiss on her inner thigh as you reach the bottom of her legs, making her shiver in delight."
                    "The scent of her arousal fills your nose, and it only serves to heighten your own desire for her."
                else:
                    "As your fingers dance across her skin, you carefully pull off her [temp_item.display_name] one at a time."
                    "Each movement is slow and deliberate, allowing you both to savor the intimacy of the moment."
                    "She leans back, her eyes closed, enjoying the tender touch that sends shivers down her spine."
                    "When the second is removed, you can't resist the urge to plant a soft kiss on her foot before continuing."
                    "Now her legs are bare and ready for your exploration and the air around you crackles with unspoken lust."
        if remove_skirt and temp_outfit.get_lower_top_layer:#remove skirt
            if temp_outfit.get_lower_top_layer.layer > 1 and not pelvis_region in temp_outfit.get_lower_top_layer.constrain_regions:
                $ temp_item = temp_outfit.get_lower_top_layer
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                if renpy.random.randint(0,3) == 0:
                    "You trace your fingers down her stomach, stopping at the hem of her [temp_item.display_name]."
                    if temp_panties:
                        "Slowly, you slide it off, exposing her smooth thighs and her [temp_panties.display_name] beneath."
                        "As she steps out of it, you can feel her warmth against your legs. Your heart races at the thought of what lies beneath those garments."
                    else:
                        "Slowly, you slide it off, exposing her smooth thighs and [the_person.pubes_description] mound."
                        "As she steps out of it, you can feel her warmth against your legs. Your heart races at the thought of what comes next."
                elif renpy.random.randint(0,1) == 0:
                    $ body_word = get_body_word(the_person)
                    "As you slide your hands down her hips, feeling the soft fabric of her [temp_item.display_name] brush against your fingertips, she gasps softly in anticipation."
                    "The sound sends shivers down your spine as you continue to work on removing the garment from her body, revealing more and more of those perfect, [body_word] legs that you've always admired."
                    if temp_panties:
                        "With a gentle tug, it finally comes off, leaving her standing before you in nothing but her [temp_panties.display_name]."
                    else:
                        "With a gentle tug, it finally comes off, leaving her standing before you with her [the_person.pubes_description] mound bare to the world."
                    if temp_outfit.get_upper_top_layer:
                        $ next_item = temp_outfit.get_upper_top_layer
                        "Her breath catches in her throat at the sight of your lustful gaze devouring every inch of her exposed skin, causing her nipples to harden beneath her [next_item.display_name]."
                    else:
                        "Her breath catches in her throat at the sight of your lustful gaze devouring every inch of her exposed skin, causing her nipples to harden on her [the_person.tits_description]."
                    "You can't help but feel a surge of power and desire well up inside you as you watch her reaction unfold."
                else:
                    $ body_word = get_body_word(the_person)
                    "Your fingers tremble slightly as you reach for the hem of her [temp_item.display_name], hesitating only momentarily before sliding it downward."
                    if temp_panties:
                        $ temp_colour = clothing_colour_name(temp_panties.colour)
                        "She shudders with excitement as the material begins to pool around her ankles, leaving her in nothing but her sexy [temp_colour] [temp_panties.display_name]."
                    else:
                        "She shudders with excitement as the material begins to pool around her ankles, leaving her [the_person.pubes_description] mound bare."
                    "You take a deep breath, savoring the view of her long, [body_word] legs, and can't help but feel a rush of adrenaline course through your veins."
                    if temp_outfit.get_upper_top_layer:
                        $ next_item = temp_outfit.get_upper_top_layer
                        "Her eyes lock onto yours, filled with need and anticipation, causing her nipples to pebble against her [next_item.display_name]."
                    else:
                        "Her eyes lock onto yours, filled with need and anticipation, causing her nipples to harden on her [the_person.tits_description]."
                    "It's clear that she's enjoying this as much as you are—and it only serves to heighten your arousal even further."
                $ the_person.update_outfit_taboos()
        if temp_outfit.get_lower_top_layer and temp_outfit.get_lower_top_layer.layer > 1:
            if upper_leg_region in temp_outfit.get_lower_top_layer.constrain_regions:#remove pants
                $ temp_item = temp_outfit.get_lower_top_layer
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                $ body_word = get_body_word(the_person)
                if renpy.random.randint(0,2) == 0:
                    if temp_panties:
                        "As you gently tug at her [temp_item.display_name], the fabric slips down her legs, revealing a pair of [temp_colour] [temp_panties.display_name] that cling to her curves like a second skin."
                        "With each inch they slide lower, your anticipation grows, and you can feel your heart racing as you catch a glimpse of her smooth, [body_word] thighs and the edge of her [the_person.pubes_description] mound peeking out from beneath the material."
                    else:
                        "As you gently tug at her [temp_item.display_name], the fabric slips down her legs, revealing her [the_person.pubes_description] mound."
                        "With each inch they slide lower, your anticipation grows, and you can feel your heart racing as you catch sight of her smooth, [body_word] thighs and calves."
                    "The look on her face is one of both surprise and amusement as she watches you struggle to maintain control, her eyes filled with desire for what's to come."
                elif renpy.random.randint(0,1) == 0:
                    "You grasp the hem of her [temp_item.display_name] and give it a firm yet gentle tug, sliding them down over her hips and along her long legs."
                    if temp_panties:
                        $ temp_colour = clothing_colour_name(temp_panties.colour)
                        "Her [body_word], muscular thighs are exposed, adorned in a pair of [temp_colour] [temp_panties.display_name] that hug her body like a second skin."
                        "Your breath catches as you see the outline of her mound through the thin fabric, and you can't help but picture what lies beneath."
                    else:
                        "Your breath catches as you see her [the_person.pubes_description] mound, and you can't help but think about what comes next."
                    "She smirks playfully at your obvious arousal, knowing exactly how much this teasing turns you on."
                else:
                    if clothing_plural(temp_item):
                        "Grasping the waistband of her [temp_item.display_name], you slowly work them down her hips and thighs, savoring every inch of skin you expose."
                    else:
                        "Grasping the waistband of her [temp_item.display_name], you slowly work it down her hips and thighs, savoring every inch of skin you expose."
                    if temp_panties:
                        $ temp_colour = clothing_colour_name(temp_panties.colour)
                        "Her [body_word] legs emerge, encased in a pair of sexy [temp_colour] [temp_panties.display_name]."
                        "A hint of her wetness peeks out from between the fabric, driving you wild with desire."
                    else:
                        "Her [body_word] legs emerge and you can see a hint of wetness glistening on her [the_person.pubes_description] folds."
                    "She watches you intently, enjoying your struggle to contain yourself as you get closer to her."
                $ the_person.update_outfit_taboos()
            else:#remove shorts
                $ temp_item = temp_outfit.get_lower_top_layer
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                $ body_word = get_body_word(the_person)
                if renpy.random.randint(0,1) == 0:
                    "As you gently tug at the hem of [the_person.possessive_title]'s [temp_item.display_name], they begin to inch their way down her smooth, [body_word] legs."
                    if temp_panties:
                        $ temp_colour = clothing_colour_name(temp_panties.colour)
                        "With each passing moment, she parts them further, allowing for a tantalizing view of her soft, [temp_colour] [temp_panties.display_name] peeking out from beneath."
                        "Her eyes are locked on yours, filled with desire and anticipation as she bites her bottom lip nervously."
                        "The fabric slides down her thighs, finally revealing the delicate lace that covers her mound, causing your heart to race and your cock to twitch in excitement."
                    else:
                        "With each passing moment, she parts them further, allowing for a tantalizing view of her [the_person.pubes_description] mound peeking out from beneath."
                        "Her eyes are locked on yours, filled with desire and anticipation as she bites her bottom lip nervously."
                        "The fabric slides down her thighs, finally revealing the delicate folds of her pussy, causing your heart to race and your cock to twitch in excitement."
                    "You can feel her warmth radiating off of her, making it difficult to focus on anything else but the forbidden fruit waiting to be devoured."
                else:
                    "As you reach for the button of [the_person.possessive_title]'s [temp_item.display_name], your hands tremble slightly in anticipation."
                    "She watches intently, her breath hitching as you undo each one slowly, deliberately."
                    if temp_panties:
                        "The fabric falls away to reveal her smooth, [body_word] legs, and she parts them invitingly, granting you a teasing glimpse of her [temp_panties.display_name]."
                        "Your gaze is drawn irresistibly to the outline of her sex through the thin material, and her scent fills your senses, driving you wild."
                    else:
                        "The fabric falls away to reveal her smooth, [body_word] legs, and she parts them invitingly, granting you a view of her [the_person.pubes_description] mound."
                        "Your gaze is drawn irresistibly to the folds of her sex, and her scent fills your senses, driving you wild."
                    "With a final tug, the [temp_item.display_name] slide down to her knees, leaving her vulnerable and aroused before you."
                    "Your fingers itch to touch, to explore, but for now, you savor this moment of control and desire."
                $ the_person.update_outfit_taboos()
        if temp_outfit.get_panties():
            if temp_outfit.get_panties().is_extension:#remove one piece
                if temp_outfit.get_upper_top_layer and temp_outfit.get_upper_top_layer.layer < 2:
                    $ temp_item = temp_outfit.get_upper_top_layer
                    $ scene_manager.draw_animated_removal(the_person, temp_item)
                    $ temp_outfit.remove_clothing(temp_item)
                    if renpy.random.randint(0,1) == 0:
                        "As you reach for the zipper of her [temp_item.display_name], your fingers tremble slightly with anticipation."
                        "The material slides down her body easily, revealing more and more of her smooth skin beneath."
                        "Her [the_person.tits_description], previously held snugly in place by the cups, are now freed, spilling out and swaying gently as she breathes."
                        "The lace trim at the edges of the cup tickles her nipples, already hard and erect from your touch."
                        "You continue to pull the [temp_item.display_name] down her body, reveling in the sight of her curves revealed: the dip of her waist, the flare of her hips, the defined muscles of her thighs."
                        "With each inch you uncover, your desire grows, threatening to overwhelm you."
                        "Finally, the [temp_item.display_name] pools at her feet, leaving her completely bare."
                        "You take a step back, admiring your work."
                        "Her chest heaves with every labored breath, her nipples standing proudly against the skin of her breasts."
                        "Sweat beads on her forehead, mingling with the remnants of the perfume she'd dabbed behind her ears earlier."
                        "And there, between her legs... her [the_person.pubes_description] pussy, wet and glistening with her arousal."
                    else:
                        $ body_word = get_body_word(the_person)
                        "As you carefully unzip [the_person.possessive_title]'s [temp_item.display_name], the cool air brushes against her skin, causing goosebumps to rise along her arms and back."
                        "Her breasts, still confined by the lacy cups, heave with anticipation as she gasps for breath."
                        if the_person.pubes_style != shaved_pubes:
                            "You slip the zipper down slowly, teasingly revealing more of her [body_word] stomach and the tiny lines of hair that trail downwards towards her pelvis."
                        else:
                            "You slip the zipper down slowly, teasingly revealing more of her [body_word] stomach and the expanse of smooth skin running downwards towards her pelvis."
                        "Her hands tremble as they reach up to help you pull the [temp_item.display_name] off her shoulders, revealing the soft flesh beneath."
                        "The cups of the bra are next, sliding easily over her [the_person.tits_description] before dropping to her waist."
                        "With a seductive wiggle, she shimmies out of the panty portion of the [temp_item.display_name], leaving her completely bare."
                        "You take in her naked form, drinking in every detail: the flush on her cheeks, the sparkle in her eyes, the way her nipples peak into hard buds." 
                        "She stands before you, utterly exposed and achingly beautiful. For a moment, you feel like the luckiest man alive."
            else:#remove panties
                $ temp_item = temp_outfit.get_lower_top_layer
                $ scene_manager.draw_animated_removal(the_person, temp_item)
                $ temp_outfit.remove_clothing(temp_item)
                if renpy.random.randint(0,3) == 0:
                    "As you carefully slide your fingers down the front of her [temp_item.display_name], you can feel her heart racing."
                    "She takes a deep breath and closes her eyes as if she's savoring the anticipation."
                    "Her hips buck slightly against your touch, and with each inch that they slide lower, she moans louder, unable to contain her excitement."
                    "Finally, her [temp_item.display_name] hit the floor, leaving both of you staring at her [the_person.pubes_description] mound, glistening with desire."
                elif renpy.random.randint(0,2) == 0:
                    if clothing_plural(temp_item):
                        "You slip your fingers underneath the thin fabric of her [temp_item.display_name], slowly inching them down her thighs."
                        "Her body trembles with anticipation as she parts her legs for you."
                        "With a gentle tug, they finally come off, revealing her [the_person.pubes_description], wet folds."
                    else:
                        "You slip your fingers underneath the thin fabric of her [temp_item.display_name], slowly inching it down her thighs."
                        "Her body trembles with anticipation as she parts her legs for you."
                        "With a gentle tug, it finally comes off, revealing her [the_person.pubes_description], wet folds."
                    "She gasps and shudders, her eyes locked on yours as if begging for more."
                elif renpy.random.randint(0,1) == 0:
                    "Grasping the waistband of her [temp_item.display_name], you pull them down over her hips, taking your time to expose her most intimate area."
                    "Her breath catches in her throat, and her eyes flutter closed as she leans back and spreads her legs, giving you better access."
                    "The moment her [temp_item.display_name] hits the ground, she opens her eyes wide, her face flushed with arousal and excitement."
                else:
                    "Gently grasping the hem of her [temp_item.display_name], you begin to slide them down her thighs, taking in the view of her soft skin beneath."
                    "Her breath quickens, and her hips start to move in time with your movements."
                    "With a final tug, they're gone, leaving her standing there before you in all her glory—her [the_person.pubes_description] pussy glistening with excitement."
                    "She bites her bottom lip and smiles coyly, her eyes promising all sorts of naughty things to come."
            $ the_person.update_outfit_taboos()
        if remove_socks and len(temp_outfit.feet) > 0:#remove stockings
            $ temp_item = temp_outfit.feet[0]
            $ scene_manager.draw_animated_removal(the_person, temp_item)
            $ temp_outfit.remove_clothing(temp_item)
            if renpy.random.randint(0,1) == 0:
                "You kneel in front of her, your fingers deftly working the elastic bands of her [temp_item.display_name] until they slip off her feet."
                "The gentle friction as they slide down her legs sends tingles up your spine, and you watch with fascination as goosebumps rise on her skin."
                "She giggles softly, her cheeks flushing red from the unexpected ticklish sensation."
                "When they're finally off, you admire how her smooth legs stretch out before you, inviting your touch."
                "You lean in closer, inhaling deeply of her scent, and then trace a finger along her inner thigh, making her gasp as pleasure courses through her body."
            else:
                "As your fingers dance across her skin, you carefully pull off her [temp_item.display_name] one at a time."
                "Each movement is slow and deliberate, allowing you both to savor the intimacy of the moment."
                "She leans back, her eyes closed, enjoying the tender touch that sends shivers down her spine."
                "When the second is removed, you can't resist the urge to plant a soft kiss on her foot before continuing."
                "Now her legs are bare and ready for your exploration and the air around you crackles with unspoken lust."
        #check success
        if not remove_shoes or not (len(temp_outfit.feet) > 0 and temp_outfit.feet[0].layer > 1):
            $ finished_stripping +=1
        if not remove_socks or not len(temp_outfit.feet) > 0:
            $ finished_stripping +=1
        if not remove_skirt or not temp_outfit.get_lower_top_layer:
            $ finished_stripping +=1
        if not remove_top or not temp_outfit.get_upper_top_layer:
            $ finished_stripping +=1
        if temp_outfit.vagina_visible:
            $ finished_stripping +=1
    return temp_outfit

label strip_while_grope_test():
    $ scene_manager = Scene()
    call screen main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game(), "Strip and Grope", "Back")]))
    $ the_person = _return
    $ scene_manager.add_actor(the_person)
    $ sluttiness_modifier = -the_person.sluttiness
    while sluttiness_modifier + the_person.sluttiness < 101:
        $ temp_outfit = the_person.decide_on_outfit(sluttiness_modifier = sluttiness_modifier)
        call strip_while_grope(the_person, temp_outfit) from _call_strip_while_grope_test
        $ sluttiness_modifier +=5
    return

label teaching_request_label(the_person, the_other_person): #in progress
    $ scene_manager = Scene()
    $ mc.change_location(bedroom)
    if the_person == lily:
        $ temp_outfit = get_pajama_outfit(the_person)
    else:
        $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    if the_person.event_triggers_dict.get("lesbian_lessons", 0) < 1:
        $ the_person.event_triggers_dict["lesbian_lessons"] = 1
    else:
        $ the_person.event_triggers_dict["lesbian_lessons"] += 1
    if the_person.event_triggers_dict.get("lesbian_lessons", 0) < 2:
        "As you're relaxing in your room, you hear a light knock on the door. It's [the_person.title], looking nervous but also... excited?"
        $ scene_manager.add_actor(the_person, emotion = "sad", visible = False)
        $ scene_manager.apply_outfit(the_person, temp_outfit)
        $ scene_manager.show_actor(the_person)
        the_person "[the_person.mc_title]?"
        mc.name "Hey, [the_person.title], what's up?"
        "At a gesture from you, she takes a few steps into the room."
        $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
        "She takes a deep breath and sits down on the edge of your bed, her hands fidgeting in her lap."
        the_person "I wanted to talk to you about something kind of awkward."
        mc.name "Go on, you know I'm always here for you."
        the_person "Well... I've been trying to make [the_other_person.fname] cum but sometimes... I can't."
        "[the_person.title] shifts uncomfortably before meeting your gaze directly."
        the_person "I feel kinda bad that I couldn't give her an orgasm. I mean, it's something every woman deserves, isn't it? And now that we're together..."
        "She trails off, clearly unsure how to continue."
        mc.name "Of course, [the_person.title]. Every woman deserves an orgasm."
        "You smile reassuringly at her."
        mc.name "And it's okay if you don't know how to give one right away. It takes practice and patience."
        "[the_person.title] looks relieved by your response but still a bit unsure of herself."
        the_person "I was wondering if... if maybe you could teach me how to please a woman... sexually."
        "Her cheeks turn even redder as she asks this question, but there's determination in her eyes that tells you she's serious about wanting to learn how to please [the_other_person.fname]."
        if the_person.sex_record.get("Orgasms", 0) > 5:
            the_person "You have always been able to get me off, so I figured you might have some tips."
        elif the_person.sex_record.get("Orgasms", 0) > 0:
            the_person "You did okay... with me, so I thought you might have some ideas."
        else:
            the_person "You've been able to... you know... satisfy a girl before right?"
        "The request catches you off guard, but you can't help feeling flattered that [the_person.title] trusts you enough to ask for help."
        mc.name "Of course, I'd be happy to help you learn."
        $ the_person.change_stats(happiness = 5, obedience = 2, slut = 1)
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "She smiles back gratefully before asking cautiously."
        the_person "Really? That would mean a lot."
        mc.name "Of course, we'll find a way to have fun while learning new techniques together."
        "The two of you agree that she can come over for a lesson soon."
        "As [the_person.possessive_title] turns to go, your mind races with the possibilities that are now in front of you."
        if the_other_person.event_triggers_dict.get("lesbian_lessons", 0) > 0:
            "The fact that you also \"helped\" [the_other_person.title] with this problem means that your relationship is becoming a true love triangle."
            "Could you be close to getting them to have a threesome with you?"
    else:
        "You get a quick text from [the_person.title]:"
        $ mc.start_text_convo(the_person)
        the_person "Hey, up for another \"lesson\" soon? I still have a lot to learn."
        mc.name "Of course, can't wait!"
        $ mc.end_text_convo()
    $ lily.event_triggers_dict["pending_lesbian_lesson"] = True
    $ lesbian_teaching = Action("Lesbian teaching", lesbian_teaching_requirement, "lesbian_teaching_label", args=[the_person, the_other_person], requirement_args=[the_person, day])
    $ mc.business.add_mandatory_crisis(lesbian_teaching)
    $ scene_manager.clear_scene()
    return

label training_request_label(the_person, the_other_person): #in progress
    $ scene_manager = Scene()
    $ mc.change_location(bedroom)
    if the_person == lily:
        $ temp_outfit = get_pajama_outfit(the_person)
    else:
        $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    if the_person.event_triggers_dict.get("lesbian_lessons", 0) < 1:
        $ the_person.event_triggers_dict["lesbian_lessons"] = 1
    else:
        $ the_person.event_triggers_dict["lesbian_lessons"] += 1
    if the_person.event_triggers_dict.get("lesbian_training", 0) < 1:
        $ the_person.event_triggers_dict["lesbian_training"] = 1
    else:
        $ the_person.event_triggers_dict["lesbian_training"] += 1
    if the_person.event_triggers_dict.get("lesbian_lessons", 0) < 2:
        "BUG: We really should have trained them once before getting here for the recording to make sense."
        "As you're relaxing in your room, you hear a light knock on the door. It's [the_person.title], looking nervous but also... excited?"
        $ scene_manager.add_actor(the_person, emotion = "sad", visible = False)
        $ scene_manager.apply_outfit(the_person, temp_outfit)
        $ scene_manager.show_actor(the_person)
        the_person "[the_person.mc_title]?"
        mc.name "Hey, [the_person.title], what's up?"
        "At a gesture from you, she takes a few steps into the room."
        $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
        "She takes a deep breath and sits down on the edge of your bed, her hands fidgeting in her lap."
        the_person "I wanted to talk to you about something kind of awkward."
        mc.name "Go on, you know I'm always here for you."
        the_person "Well... I've been trying to make [the_other_person.fname] cum but sometimes... I can't."
        "[the_person.title] shifts uncomfortably before meeting your gaze directly."
        the_person "I feel kinda bad that I couldn't give her an orgasm. I mean, it's something every woman deserves, isn't it? And now that we're together..."
        "She trails off, clearly unsure how to continue."
        mc.name "Of course, [the_person.title]. Every woman deserves an orgasm."
        "You smile reassuringly at her."
        mc.name "And it's okay if you don't know how to give one right away. It takes practice and patience."
        "[the_person.title] looks relieved by your response but still a bit unsure of herself."
        the_person "I was wondering if... if maybe you could teach me how to please a woman... sexually."
        "Her cheeks turn even redder as she asks this question, but there's determination in her eyes that tells you she's serious about wanting to learn how to please [the_other_person.fname]."
        if the_person.sex_record.get("Orgasms", 0) > 5:
            the_person "You have always been able to get me off, so I figured you might have some tips."
        elif the_person.sex_record.get("Orgasms", 0) > 0:
            the_person "You did okay... with me, so I thought you might have some ideas."
        else:
            the_person "You've been able to... you know... satisfy a girl before right?"
        "The request catches you off guard, but you can't help feeling flattered that [the_person.title] trusts you enough to ask for help."
        mc.name "Of course, I'd be happy to help you learn."
        $ the_person.change_stats(happiness = 5, obedience = 2, slut = 1)
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "She smiles back gratefully before asking cautiously."
        the_person "Really? That would mean a lot."
        mc.name "Of course, we'll find a way to have fun while learning new techniques together."
        "The two of you agree that she can come over for a lesson soon."
        "As [the_person.possessive_title] turns to go, your mind races with the possibilities that are now in front of you."
        if the_other_person.event_triggers_dict.get("lesbian_lessons", 0) > 0:
            "The fact that you also \"helped\" [the_other_person.title] with this problem means that your relationship is becoming a true love triangle."
            "Could you be close to getting them to have a threesome with you?"
    elif the_person.event_triggers_dict.get("lesbian_training", 0) < 2:
        "As you relax on your bed, there is a light knock on your door, as [the_person.title] confidently pushes it open."
        $ scene_manager.add_actor(the_person, emotion = "happy", visible = False)
        $ scene_manager.apply_outfit(the_person, temp_outfit)
        $ scene_manager.show_actor(the_person)
        the_person "Hey, [the_person.mc_title] I wanted to stop in and thank you for your... help."
        mc.name "I take it things are going better with [the_other_person.fname] when you two are alone?"
        the_person "Yeah, and I owe it all to you."
        mc.name "Trust me, it was my pleasure."
        the_person "I know you got to enjoy it too, but I think I probably benefitted more."
        $ scene_manager.update_actor(the_person, position = "sitting")
        "She strides over, taking a seat next to you on your bed and running a hand along your arm."
        the_person "In fact... I was thinking.. there's always room for improvement. Maybe we could do a little more training sometime."
        mc.name "I certainly wouldn't say no to that. We can always find some new area to focus on."
        $ the_person.change_stats(happiness = 5, obedience = 2, slut = 1)
        "She smiles back gratefully."
        the_person "Great! I'll stop by sometime when I have a night free so we can resume our lessons."
        mc.name "Looking forward to it! Seriously, stop by anytime."
        "It seems like [the_person.possessive_title] has moved past the pretense of needing your help and just wants to spend more time with you."
        "You're not complaining, but you do wonder where this is all going."
        if the_other_person.event_triggers_dict.get("lesbian_training", 0) > 0:
            "The fact that [the_other_person.title] is also eager to spend time with you is extremely promising."
            "You wonder how you could go about letting them know about each other's visits without destroying everything."
    else:
        "You get a quick text from [the_person.title]:"
        $ mc.start_text_convo(the_person)
        the_person "Hey, up for another \"lesson\" soon? I still have a lot to learn."
        mc.name "Of course, can't wait!"
        $ mc.end_text_convo()
    $ lily.event_triggers_dict["pending_lesbian_lesson"] = True
    $ lesbian_teaching = Action("Lesbian teaching", lesbian_teaching_requirement, "lesbian_teaching_label", args=[the_person, the_other_person], requirement_args=[the_person, day])
    $ mc.business.add_mandatory_crisis(lesbian_teaching)
    $ scene_manager.clear_scene()
    return

label grope_teaching_label(the_person, the_other_person, temp_outfit):
    $ scene_manager = Scene()
    if temp_outfit.get_upper_top_layer and temp_outfit.get_upper_top_layer.layer > 3:
        $ the_item = temp_outfit.remove_random_upper(top_layer_first = True, do_not_remove = False)
        "[the_person.title] slips off her [the_item.display_name] to buy some time, swallowing hard before answering."
    else:
        "[the_person.title] swallows hard before answering."
    $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
    $ temp_top = temp_outfit.get_upper_top_layer
    $ temp_bra = temp_outfit.get_bra()
    if temp_top == temp_bra:
        $ temp_top = None
    $ temp_bottom = temp_outfit.get_lower_top_layer
    $ temp_panties = temp_outfit.get_panties()
    if temp_bottom == temp_panties or (temp_top and temp_top.has_extension):
        $ temp_bottom = None
    $ taboo_broken = False
    the_person "I guess... I want to know how to touch her properly. How to make her feel good."
    "She looks at you expectantly."
    "You nod encouragingly, eager to make today productive and enjoyable for both of you."
    mc.name "Alright, let's start with the basics. When you're touching [the_other_person.fname] it is okay to linger, and take things slow."
    "Your hands trace delicate lines in the air, trying to demonstrate what you mean."
    mc.name "Use your hands to explore her body. Start by gently touching her neck and shoulders, then work your way down to her breasts."
    "Her hands flutter in the air, trying to copy your actions, although it seems like she is struggling to grasp exactly what you mean."
    mc.name "I think I might need to give you a more practical demonstration to really explain."
    "You grasp the bottom of your shirt, pulling it up and over your head in one quick movement."
    if the_person.has_taboo("underwear_nudity"):
        "[the_person.title] blushes a bit, crossing her arms over her chest defensively."
        "You continue, ignoring her hesitance, after all you are still more dressed than you would be at the beach."
    else:
        "[the_person.title] drops her eyes, taking a moment to appreciate your body."
        "You pause for a moment, letting her get a good look before you continue."
    "Reaching up to your neck, you gently run the tips of your fingers along your skin. With a gentle caress you make small circles as you move across your skin."
    mc.name "Now you try."
    if temp_top:
        "[the_person.title] reaches up, rubbing her neck gently but quickly runs into the obstruction of her clothes."
        if the_person.has_taboo("underwear_nudity"):
            "She struggles for a bit, determined to copy you, but clearly not prepared to take off her [temp_top.display_name] in front of you."
        else:
            "She struggles for a bit, determined to copy you, but clearly having trouble with her [temp_top.display_name]."
        mc.name "When you start off you and [the_other_person.fname] will probably have some clothes on, but I assume you'll start taking them off once you get going."
        the_person "Well, yeah... but this is just practice."
        mc.name "I know, but the more we can replicate reality the better I'll be able to guide you."
        the_person "What do you mean?"
        mc.name "You can't press against your clothes in the same way that you can press against a body."
        if the_person.has_taboo("underwear_nudity"):
            $ taboo_broken = True
            the_person "You want me to take off my [temp_top.display_name]?"
            "You can tell this might be a problem for her, but gently push her boundaries."
            mc.name "I think that is the best way to proceed."
            "She pauses for a moment to consider this."
        else:
            the_person "That makes sense. I should take off my [temp_top.display_name]."
        if temp_bra and (temp_panties or not temp_top.has_extension):
            the_person "I guess it isn't anything you wouldn't see at the beach."
        else:
            if temp_top.has_extension and not temp_panties and the_person.has_taboo("bare_vagina"):
                $ taboo_broken = True
                if not temp_bra and the_person.has_taboo("bare_tits"):
                    the_person "Unfortunately I'm not wearing underwear right now. You'll be able to see all of me if I take it off."
                else:
                    the_person "Unfortunately I'm... not wearing panties. You'll be able to see my pussy."
            elif not temp_bra and the_person.has_taboo("bare_tits"):
                $ taboo_broken = True
                the_person "I guess that would normally be okay... but I don't have a bra on under my [temp_top.name!l]."
            mc.name "If you're serious about making [the_other_person.fname] happy I think that is a sacrifice you are going to have to make."
            "[the_person.title] thinks for a moment, her face settling into a grimace of determination as she reaches down."
        "[the_person.title] tugs at the hem of her [temp_top.display_name], pulling it up and over her head."
        $ scene_manager.draw_animated_removal(the_person, temp_top)
        if not the_person.has_taboo("bare_tits") and temp_bra:
            the_person "While I'm at it, I might as well take off my [temp_bra.display_name] too."
            $ scene_manager.draw_animated_removal(the_person, temp_bra)
            $ temp_bra = None
        $ the_person.update_outfit_taboos()
        "Once she is ready, she resumes her actions, running her hand across her shoulder and trailing her fingers down her arm."
    else:
        "[the_person.title] reaches up, rubbing her neck gently then running her hand across her shoulder and trailing her fingers down her arm."
    "You drink in the sight of [the_person.possessive_title] as she fondles herself and consider what your next step should be."
    mc.name "That's good [the_person.title], now move over to your breasts."
    if temp_bra:
        "You watch as her hands drift to cup her [the_person.tits_description], squeezing them through her [temp_bra.display_name]."
        if not the_person.has_taboo("bare_tits"):
            "Before you get a chance to suggest it, she reaches back and unclasps it, letting it slide down her arms to drop on the floor."
            $ scene_manager.draw_animated_removal(the_person, temp_bra)
            $ temp_bra = None
        else:
            mc.name "You could take off your [temp_bra.display_name] too."
            if taboo_broken:
                the_person "That's not going to happen. I want your help, but I'm not ready to let you ogle my entire body in exchange."
            else:
                the_person "Is that really necessary?"
                mc.name "I guess not, I thought you cared about [the_other_person.fname] and wanted to make her happy."
                "She pauses, clearly torn between demonstrating her commitment to [the_other_person.title] and letting you see more of her body."
                the_person "Fine, but there's no way I'm going to take off any more than this."
                $ generalised_strip_description(the_person, [temp_bra])
                $ scene_manager.draw_animated_removal(the_person, temp_bra)
                $ temp_bra = None
                $ the_person.update_outfit_taboos()
    if temp_bra or (taboo_broken and the_person.has_taboo("touching_body")):
        "Her hands continue to explore her body and you have the overwhelming urge to reach out and touch her."
        "Reaching out slowly, you place your hand over hers, but she jerks back almost instantly."
        the_person "What do you think you're doing?"
        mc.name "Helping you?"
        the_person "You don't need to touch me to do that. I'm already stripping for you, isn't that enough."
        mc.name "I just want to make sure you are doing it right."
        the_person "Sorry, this is just... too much."
        "She scoots away, trying to cover her body while reaching for her discarded clothes."
        the_person "Thanks, but I think I've got it from here."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "As she makes her way to the door, you are a bit disappointed, but you did get her to go a bit further than she has before."
        $ scene_manager.clear_scene()
        return False
    "Her hands rove over her bare [the_person.tits_description], fondling and squeezing as you watch."
    mc.name "Once she is warmed up you can pinch her nipples too, just watch her to make sure you don't do it too hard."
    "As she continues to manipulate her body you feel the overwhelming urge to touch her."
    "Reaching out slowly, you place your hand over hers, guiding it over her skin while demonstrating different speeds and pressures."
    if the_person.has_taboo("touching_body"):
        $ the_person.call_dialogue("touching_body_taboo_break")
        $ the_person.break_taboo("touching_body")
        $ taboo_broken = True
        "You reach out to resume your assistance, guiding her small hand with yours."
    "Her breath hitches when your hand brushes against her smooth skin, causing her to moan softly."
    "Your cock twitches in response, pressing against your jeans uncomfortably. With each passing moment, your desire grows stronger."
    "As you guide [the_person.title]'s hands over her body, your touch is gentle yet confident."
    "Getting bolder, you begin to trace circles around her nipples, watching as they harden in response to your teasing touch."
    "Next, you move down her body, guiding her hand lower and lower until it is brushing against her belly button."
    if taboo_broken and the_person.has_taboo("touching_vagina"):
        if temp_panties:
            "Finally, you slip lower, pressing against her skin as you slip under the waist of her [temp_panties.display_name]."
        elif temp_bottom:
            "Finally, you slip lower, pressing against her skin as you slip under the waist of her [temp_bottom.display_name]."
        else:
            "Finally, you slip lower, sliding your fingers over her [the_person.pubes_description] mound."
        "Her eyes go wide and she pushes your hand away, suddenly realising how far things have gone."
        the_person "You can't touch me down there!"
        mc.name "I just want to make sure you are doing it right."
        the_person "Sorry, this is just... too much."
        "She scoots away, trying to cover her body while reaching for her discarded clothes."
        $ scene_manager.update_actor(the_person, position = "stand4")
        $ scene_manager.show_dress_sequence(the_person, temp_outfit)
        the_person "Thanks, but I think I've got it from here."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "As she makes her way to the door, you are a bit disappointed, but you did get her to go a bit further than she has before."
        $ scene_manager.clear_scene()
        return False
    if temp_bottom:
        if temp_panties:
            "Then, sliding your fingers lower down her stomach, you slip into her [temp_bottom.display_name] and under her [temp_panties.display_name]. You part her folds and brush against her clit."
        else:
            "Then, sliding your fingers lower down her stomach and into her [temp_bottom.display_name], you part her folds and brush against her clit."
    elif temp_panties:
        "Then, sliding your fingers lower down her stomach and into her [temp_panties.display_name], you part her folds and brush against her clit."
    else:
        "Then, sliding your fingers lower down her stomach and over her [the_person.pubes_description] mound, you part her folds and brush against her clit."
    if the_person.has_taboo("touching_vagina"):
        $ the_person.call_dialogue("touching_vagina_taboo_break")
        $ the_person.break_taboo("touching_vagina")
    "You show her how to stroke it slowly at first and then faster as she becomes more aroused."
    "Her breath comes in ragged gasps as pleasure washes over her, making her arch her back off the bed slightly for leverage."
    "Her hips buck forward involuntarily, seeking more contact with your hand; all she can focus on now is the sensation building inside of her."
    the_person "Oh God, that feels so good..."
    if taboo_broken:
        "You smile encouragingly at her, pleased that she is enjoying your lesson too much to stop you from taking advantage of her."
    "The sight of her writhing beneath your instruction fills you with a mixture of lust and pride—you are helping her become the best lover possible not just for [the_other_person.fname] but also for you."
    "[the_person.title]'s eyes are closed tightly as she focuses on the sensations washing over her body."
    "Her hands tremble slightly as they explore her own curves, mimicking your movements while trying to find that perfect rhythm that will send her over the edge."
    the_person "[the_person.mc_title], this feels amazing... but I need more."
    "You smile reassuringly at her before leaning forward and kissing her forehead softly."
    "Dropping all pretense of teaching, you sit next to her on the bed and pull her body towards you."
    "As she settles onto your lap you use both hands to explore her body freely."
    call fuck_person(the_person, start_position = standing_grope, start_object = make_bed(), position_locked = True, affair_ask_after = False) from _call_fuck_person_groping_teach
    $ the_report = _return
    return the_report

label finger_teaching_label(the_person, the_other_person, temp_outfit):
    if temp_outfit.get_upper_top_layer and temp_outfit.get_upper_top_layer.layer > 3:
        $ the_item = temp_outfit.remove_random_upper(top_layer_first = True, do_not_remove = False)
        "[the_person.title] slips off her [the_item.display_name] to buy some time, swallowing hard before answering."
    else:
        "[the_person.title] swallows hard before answering."
    $ scene_manager.add_actor(the_person, visible = False)
    $ scene_manager.apply_outfit(the_person, temp_outfit)
    $ scene_manager.show_actor(the_person)
    $ temp_bottom = the_person.outfit.get_lower_top_layer
    $ temp_panties = the_person.outfit.get_panties()
    if temp_bottom == temp_panties:
        $ temp_bottom = None
    the_person "I want to... uh... I want to learn how to finger her."
    "She blushes crimson with that admission, clearly a bit embarrassed."
    mc.name "Of course, [the_person.title]. I'd be happy to help with that."
    "You smile at her as you move your hands up into the air, cupping one in a circle while you rest the fingers of the other on your thumb."
    mc.name "Start by stroking her thighs lightly, working higher and higher as you warm her up."
    mc.name "Take your time and let her reactions show you when she is ready for you to take the next step."
    the_person "What about finger placement?"
    mc.name "That's where things can get a bit tricky. Everyone is different so it might take some time to find the right spot."
    "Slipping two fingers into your cupped hand you move them to different depths, then you pull them out to show her how you curl them to explore."
    if the_person.has_taboo("touching_vagina"):
        mc.name "It is a little hard to explain but I could... show you if you are up for it?"
        "You let the question hang in the as you watch the emotions run across her face."
        if the_person.has_taboo("underwear_nudity"):
            the_person "I... don't know. I mean you haven't even seen my [temp_panties.display_name] before and now you want me to let you finger me?"
        elif the_person.has_taboo("bare_vagina"):
            the_person "I... don't know. I didn't think I'd have to get fully nude for these lessons."
        elif the_person.has_taboo("touching_body"):
            the_person "I'm not sure I'm comfortable with you touching me... especailly like that."
        else:
            the_person "I know we fooled around a bit, but isn't that a bit intimate for a lesson?"
        mc.name "I just think it would be the best way to train you. You liked your last lesson right?"
        the_person "I guess, but..."
        "She pauses for awhile, you can tell this is a lot for her."
        the_person "Okay... for [the_other_person.fname]."
    else:
        mc.name "It is a little hard to explain, but if you let me demonstrate this should go faster."
        if the_person.event_triggers_dict.get("lesbian_training", 0) > 0:
            the_person "Yeah, I guess that is probably for the best. But this is just a lesson, I'm still with [the_other_person.fname]."
            mc.name "Of course."
        else:
            the_person "Great, I love practical lessons."
    call strip_bottom_label(the_person) from _call_strip_bottom_label_finger
    $ scene_manager.update_actor(the_person, position = "missionary")
    if temp_bottom and skirt_region in temp_bottom.constrain_regions:
        "She sits up, sliding forward to the edge of the bed before spreading her legs wide open to give you better access."
    elif temp_bottom or temp_panties:
        "She sits down on the edge of the bed, spreading her legs wide open to give you better access."
    else:
        "She spreads her legs wide, giving you a great view of her [the_person.pubes_description] pussy."
    mc.name "Alright, let's start with the basics."
    "You reach out for her, resting your hand gently on her inner thigh as you look into her eyes to see her reaction."
    if the_person.has_taboo("touching_body"):
        "She tenses up a bit, clearly uncertain about this, but she doesn't object."
        mc.name "Don't worry [the_person.title], we'll take things slow."
        $ the_person.break_taboo("touching_body")
    else:
        "She closes her eyes, tilting her head back slightly as she sighs in pleasure."
    "Rubbing against her sensitive skin, you move higher and higher approaching your goal."
    mc.name "Focus on using your fingertips, you should barely be putting any pressure on her, just enough to tease."
    "Sensing that she is ready, you lift your hand and bring it to your mouth, licking two fingers for some extra moisture."
    "Moving it back down, you slide it along her folds with just the faintest hint of pressure."
    if the_person.has_taboo("touching_vagina"):
        "She inhales sharply and reaches out to grab your wrist, stopping your movement."
        "You stare into one another's eyes as she collects herself and you try to remain still."
        "Slowly she relaxes her body and the grip on your arm."
        "You rotate your wrist, sliding back up and pressing the pad of your finger against her clit."
        $ the_person.break_taboo("touching_vagina")
    else:
        "At the bottom you rotate your wrist, sliding back up and pressing the pad of your finger against her clit."
    "Her body rocks back as she clenches her ass, pushing slightly up to get more contact."
    "Pushing forward you insert your finger slowly giving her time to object, but she seems to be swept up in the moment."
    "Adding another finger you start to explore, watching her face for any reactions to the places you touch."
    mc.name "Once you're inside [the_other_person.fname] keep your eyes on her face. Even the subtlest hints can help you know which way to go."
    "You emphasize your point by pressing firmly against her G-spot, causing her to buck her hips and moan."
    the_person "Oh god... [the_person.mc_title] keep going."
    call fuck_person(the_person, start_position = cuddle_finger, start_object = make_bed(), skip_intro = True, position_locked = True, affair_ask_after = False) from _call_fuck_person_finger_teach
    $ the_report = _return
    return the_report

label strip_bottom_label(the_person):
    $ temp_bottom = the_person.outfit.get_lower_top_layer
    $ temp_panties = the_person.outfit.get_panties()
    if temp_bottom == temp_panties:
        $ temp_bottom = None
    if temp_bottom:
        if temp_panties:
            if skirt_region in temp_bottom.constrain_regions:
                $ scene_manager.update_actor(the_person, position = "missionary")
                "[the_person.title] leans back, lifting her legs so that she can slide her [temp_bottom.display_name] up to her waist."
            else:
                $ scene_manager.update_actor(the_person, position = "stand2")
                "[the_person.title] stands up, working at the waist of her [temp_bottom.display_name] and then dropping them to the floor."
            $ scene_manager.remove_clothing(the_person, [temp_bottom])
            $ scene_manager.update_actor(the_person)
            $ the_person.update_outfit_taboos()
            if the_person.has_taboo("underwear_nudity"):
                "Her hands cover her panty clad mound, trying to shield herself from your view, despite the fact that you are about to finger her."
            if the_person.has_taboo("bare_vagina"):
                if clothing_plural(temp_panties):
                    "Her hands fiddle with the waist of her [temp_panties.display_name] before she seems to change her mind and pulls them slightly to the side instead."
                    "You're still able to see her [the_person.pubes_description] pussy, but if having them on makes her more comfortable you won't complain."
                else:
                    "Her hands fiddle with the waist of her [temp_panties.display_name] before she seems to change her mind and pulls it slightly to the side instead."
                    "You're still able to see her [the_person.pubes_description] pussy, but if having it on makes her more comfortable you won't complain."
                $ scene_manager.strip_to_vagina(the_person, prefer_half_off = True)
            else:
                if clothing_plural(temp_panties):
                    "Then she grips her [temp_panties], pulling them down to reveal her [the_person.pubes_description] pussy."
                else:
                    "Then she grips her [temp_panties], pulling it down to reveal her [the_person.pubes_description] pussy."
                $ scene_manager.remove_clothing(the_person, [temp_panties])
        else:
            if skirt_region in temp_bottom.constrain_regions:
                $ scene_manager.update_actor(the_person, position = "missionary")
                "[the_person.title] leans back, lifting her legs so that she can slide her [temp_bottom.display_name] up to her waist."
            else:
                $ scene_manager.update_actor(the_person, position = "stand3")
                "[the_person.title] stands up, working at the waist of her [temp_bottom.display_name] and then dropping them to the floor."
            $ scene_manager.remove_clothing(the_person, [temp_bottom])
            if the_person.has_taboo("bare_vagina"):
                "You get a brief glimpse of her [the_person.pubes_description] pussy before her hands move to cover it."
                "She takes a deep breath and seems to collect herself enough to let her hands drop, letting you drink in the view of her body."
            else:
                "It seems like she wasn't wearing panties, so you get a lovely view of her [the_person.pubes_description] pussy."
        $ the_person.update_outfit_taboos()
    elif temp_panties:
        $ body_word = get_body_word(the_person)
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.title] stands up, her hands going to her [body_word] waist."
        if the_person.has_taboo("bare_vagina"):
            if clothing_plural(temp_panties):
                "Her hands fiddle with the waistband of her [temp_panties.display_name] before she seems to change her mind and pulls them slightly to the side instead."
                "You're still able to see her [the_person.pubes_description] pussy, but if having them on makes her more comfortable you won't complain."
            else:
                "Her hands fiddle with the waistband of her [temp_panties.display_name] before she seems to change her mind and pulls it slightly to the side instead."
                "You're still able to see her [the_person.pubes_description] pussy, but if having it on makes her more comfortable you won't complain."
            $ scene_manager.strip_to_vagina(the_person, prefer_half_off = True)
        else:
            if clothing_plural(temp_panties):
                "Then she grips her [temp_panties], pulling them down to reveal her [the_person.pubes_description] pussy."
            else:
                "Then she grips her [temp_panties], pulling it down to reveal her [the_person.pubes_description] pussy."
            $ scene_manager.remove_clothing(the_person, [temp_panties])
        $ the_person.update_outfit_taboos()
    return

label oral_teaching_label(the_person, the_other_person, temp_outfit):
    $ temp_bottom = the_person.outfit.get_lower_top_layer
    $ temp_panties = the_person.outfit.get_panties()
    if temp_bottom == temp_panties:
        $ temp_bottom = None
    $ scene_manager.add_actor(the_person, position = "sitting")
    the_person "I want to... uh... I want to learn how to lick her."
    "She blushes crimson with that admission, clearly a bit embarrassed."
    mc.name "Of course, [the_person.title]. I'd be happy to help with that."
    "You smile at her as you move your hand up into the air, cupping it in a circle as you bring it towards your mouth."
    mc.name "Start by kissing her thighs lightly, working higher and higher as you warm her up."
    mc.name "Take your time and let her reactions guide you when it is time to take the next step."
    the_person "What about my tongue?"
    mc.name "That's where things can get a bit tricky. Everyone is different so it might take some time to find the right spot."
    "Opening your hand and your mouth, you stick out your tongue."
    "You probe at the air trying to demonstrate cunnilingus, but judging by her face you must look pretty comical."
    if the_person.has_taboo("licking_pussy"):
        mc.name "It is a little hard to explain but I could... show you if you are up for it?"
        "You let the question hang in the as you watch the emotions run across her face."
        #she brings up concerns and you reassure her
        #all other taboos were broken last time, but lily might reset, leave flavor text below
    else:
        mc.name "It is a little hard to explain, but if you let me demonstrate this should go faster."
        the_person "Yeah, I guess that is probably for the best. But this is just a lesson, I'm still with [the_other_person.fname]."
        mc.name "Of course."
    call strip_bottom_label(the_person) from _call_strip_bottom_label_oral
    if temp_bottom and skirt_region in temp_bottom.constrain_regions:
        "She sits up, sliding forward to the edge of the bed before spreading her legs wide open to give you better access."
    elif temp_bottom or temp_panties:
        "She sits down on the edge of the bed, spreading her legs wide open to give you better access."
    else:
        "She spreads her legs wide, giving you a great view of her [the_person.pubes_description] pussy."
    "You get off the bed and move around to kneel between her legs."
    mc.name "Alright, let's start with the basics."
    "You reach out for her, resting your hands gently on her knees as you lean forward to kiss her inner thigh."
    if the_person.has_taboo("touching_body"):
        "She tenses up a bit, clearly uncertain about this, but she doesn't object."
        mc.name "Don't worry [the_person.title], we'll take things slow."
        $ the_person.break_taboo("touching_body")
    else:
        "She sighs pleasantly, laying back to enjoy your attentions."
    "Brushing your lips against her sensitive skin, you move higher and higher approaching your goal."
    mc.name "When you start you should barely be putting any pressure on her, just enough to tease."
    "You lean over [the_person.title]'s exposed pussy, inhaling deeply of her musky scent as you watch [the_person.possessive_title] moan and writhe beneath you."
    "Sensing that she is ready, you center yourself in front of her and lean in to plant a kiss directly over her folds."
    if the_person.has_taboo("touching_vagina"):
        "She inhales sharply and reaches out to grab your head, stopping your movement."
        "You tilt your head back, searching for her eyes as she collects herself."
        "Slowly she relaxes her body and the grip on your head."
        "You lean in again, this time aiming your kiss for the hood of her clit."
        $ the_person.break_taboo("touching_vagina")
    else:
        "You follow this with a series of small pecks, moving up to plant a kiss on the hood of her clit."
    "Her body rocks back as she clenches her ass, pushing slightly up to get more contact with your lips."
    "Opening your lips, you dart your tongue out slowly, running it along her pussy."
    "You are gentle, giving her time to object, but she seems to be swept up in the moment."
    "Your tongue darts out to tease her entrance, circling it gently before dipping inside for a brief taste of her nectar."
    the_person "Oh god... [the_person.mc_title] keep going."
    mc.name "See? Your mouth can be just as powerful as your hands."
    "You demonstrate how to use the tip of the tongue to circle a clit while watching with satisfaction as she moans from your example."
    "Her eyes widen with wonder at the variety of sensations you give her, and you take fewer breaks to explain, just savoring the taste of her."
    call fuck_person(the_person, start_position = cunnilingus, start_object = make_bed(), skip_intro = True, position_locked = True, affair_ask_after = False) from _call_fuck_person_oral_teach
    $ the_report = _return
    return the_report

label anal_teaching_label(the_person, the_other_person, temp_outfit):
    $ scene_manager = Scene()
    $ temp_bottom = the_person.outfit.get_lower_top_layer
    $ temp_panties = the_person.outfit.get_panties()
    if temp_bottom == temp_panties:
        $ temp_bottom = None
    $ scene_manager.add_actor(the_person, position = "sitting")
    #We've already fingered, the only new thing is to demonstrate on her
    the_person "What about... anal?"
    mc.name "For you and [the_other_person.fname] anal fingering won't be much different than vaginal."
    mc.name "You can even do both at the same time without any real problems."
    if the_person.has_taboo("anal_sex"): #not really anal
        mc.name "It is a little hard to explain but I could... show you if you are up for it?"
        "You let the question hang in the as you watch the emotions run across her face."
        #she brings up concerns and you reassure her
    else:
        mc.name "It is a little hard to explain, but if you let me demonstrate this should go faster."
        the_person "Yeah, that makes sense."
    call strip_bottom_label(the_person) from _call_strip_bottom_label_anal
    if temp_bottom and skirt_region in temp_bottom.constrain_regions:
        "She rolls over, planting her head on the bed before pulling her knees under her and spreading her legs wide open to give you better access."
    elif temp_bottom or temp_panties:
        "She kneels on the bed, leaning forward to press her face into the sheets."
        "Spreading her legs wide open to give you better access, she reaches back to spread her cheeks."
    else:
        "She rolls over, planting her head on the bed before pulling her knees under her and spreading her legs wide open to give you better access."
        $ body_word = get_body_word(the_person)
        "You are met with a great view of her [body_word] ass and her [the_person.pubes_description] pussy."
    "You get off the bed and move around to lean over behind her."
    mc.name "Alright, let's start with the basics."
    "Without further ado, you dip two fingers into her pussy, lubing them up to explore her back door."
    "Next you position them near [the_person.title]'s anus, resting them gently on her puckered opening."
    "She squirms slightly but doesn't protest as you prepare yourself for this new experience together."
    "Slowly, carefully, you push one finger inside; the tightness surrounding your digit makes your eyes widen briefly before it slips easily within her asshole."
    "She lets out a sharp intake of breath but does not pull away."
    "Encouraged by this response, you add another finger to stretch her even further all of your focus is on pleasuring her ass."
    "Her moans intensify as you begin to work your fingers in and out of her rear end."
    "You bring your other hand up to rub her clit between thumb and forefinger."
    "The perfect blend of pleasure and discomfort has [the_person.title] thrusting her hips back in search of more stimulation."
    "She whimpers desperately into the pillows beneath her head."
    "[the_person.title] tilts her hips, granting better access to her sensitive entrance as you continue fingering her relentlessly."
    "You plant small kisses along her ass as it shakes with the force of your thrusting hand."
    "Her climax builds rapidly as her muscles quiver under your touch; soon enough she cries out"
    the_person "I'm close!"
    "[the_person.title]'s orgasm washes over her in waves, nearly too much to bear as her ass clenches tightly around your fingers and her pussy grips at the air."
    "You can feel the incredible pleasure radiating off of her as she finally releases into an earth-shattering climax."
    $ the_person.have_orgasm()
    "Her body goes limp for a moment before she gasps for breath, then rolls onto her back with a contented sigh."
    return

label lesbian_teaching_label(the_person, the_other_person):
    $ lily.event_triggers_dict["pending_lesbian_lesson"] = False
    if get_lab_partner().event_triggers_dict.get("friend_with_benefits", 0) < 13:
        $ lily_buddy_corruption = Action("Lesbian Date", lily_buddy_corruption_requirement, "lily_buddy_corruption_label", requirement_args=day)
        $ mc.business.add_mandatory_crisis(lily_buddy_corruption)
    $ scene_manager = Scene()
    if the_person == lily:
        $ temp_outfit = get_pajama_outfit(the_person)
    else:
        $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person)
    $ temp_top = temp_outfit.get_upper_top_layer
    $ temp_bra = temp_outfit.get_bra()
    if temp_top == temp_bra:
        $ temp_top = None
    $ temp_bottom = temp_outfit.get_lower_top_layer
    $ temp_panties = temp_outfit.get_panties()
    if temp_bottom == temp_panties or (temp_top and temp_top.has_extension):
        $ temp_bottom = None
    $ taboo_broken = False
    if get_lab_partner().event_triggers_dict.get("friend_with_benefits", 0) < 14:
        "Tonight is the night you agreed to help [the_person.title] learn how to please a woman."
    else:
        "Tonight is the night you agreed to help [the_person.title] improve her skills with women."
    if not mc.location == bedroom:
        if not mc.location_hub == home_hub:
            "You quickly make your way home and head to your bedroom."
        else:
            "You make your way to your bedroom."
        $ mc.change_location(bedroom)
    $ scene_manager.add_actor(the_person, visible = False)
    $ scene_manager.apply_outfit(the_person, temp_outfit)
    $ scene_manager.show_actor(the_person)
    "When she arrives, you greet her with a warm smile and usher her inside."
    if get_lab_partner().event_triggers_dict.get("friend_with_benefits", 0) < 14:
        "You sit down on your bed together, facing each other intimately but not too close—the air between you charged with curiosity and eagerness."
    else:
        "You sit down on your bed together, facing each other the air between you charged with curiosity and eagerness."
    $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
    mc.name "So, where would you like to start?"
    if the_person.event_triggers_dict.get("lesbian_lessons", 0) < 2:
        call grope_teaching_label(the_person, the_other_person, temp_outfit) from _call_grope_teaching_label_wrapper
        if not _return:
            return
        $ the_report = _return
        $ the_person.call_dialogue("sex_review", the_report = the_report)
    elif the_person.event_triggers_dict.get("lesbian_lessons", 0) < 3:
        call finger_teaching_label(the_person, the_other_person, temp_outfit) from _call_finger_teaching_label_wrapper
        if _return:
            $ the_report = _return
            $ the_person.call_dialogue("sex_review", the_report = the_report)
    elif the_person.event_triggers_dict.get("lesbian_lessons", 0) < 5:
        menu:
            "Teach her cunnilingus":
                call oral_teaching_label(the_person, the_other_person, temp_outfit) from _call_oral_teaching_label_wrapper
                if _return:
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)
            "Teach her anal":
                call anal_teaching_label(the_person, the_other_person, temp_outfit) from _call_anal_teaching_label_wrapper
                if _return:
                    $ the_report = _return
                    $ the_person.call_dialogue("sex_review", the_report = the_report)
    else:
        "BUG: lesbian_lessons too high"
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You pull back slowly, admiring your handiwork while she catches her breath on the bed beside you."
    if the_person.is_willing(standing_finger):
        "She looks up at you with a mix of lust and gratitude in her eyes before propping herself up and kissing your neck passionately."
        "Her tongue darts out teasingly against your skin as she whispers."
        the_person "Thank you for showing me this... I never knew it could be so good."
        "You turn to return her kiss with equal fervor, deepening it as your hands wander over her body once again."
        "Your fingers find their way back between her legs where they gently part them wider while your thumb circles her clit rapidly—driving her wild with pleasure."
        "The thought of having taught her such an intimate act excites you beyond measure, as the hard bulge in your pants can attest."
        "Confidant that in this state you can do basically anything with her, you consider your options."
        call fuck_person(the_person, affair_ask_after = False) from _call_fuck_person_lesbian_lesson
        $ the_report = _return
        $ the_person.call_dialogue("sex_review", the_report = the_report)
        "[the_person.title] takes a few moments to collect herself and then gets up to get dressed."
        $ scene_manager.update_actor(the_person, position = "stand2")
        $ scene_manager.show_dress_sequence(the_person, temp_outfit)
        "When she is presentable, she leans over the bed to give you a kiss on the cheek before turning to leave the room."
    else:
        "You can't help but notice how aroused she makes you as your rock hard cock, presses against your jeans."
        mc.name "[the_person.title], I think… I think we should take a break for now."
        "Her eyes scan your body and widen as she realises what's happening."
        the_person "Oh, um..."
        "She looks down at her hand, where she's still holding yours."
        "You slowly pull away from her and stand up, needing some distance."
        mc.name "This isn't the best time for us to be doing this, let's finish this another time when we're both more composed."
        "She nods in agreement, her cheeks flushed with embarrassment and desire."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person "Yeah, that would be good."
        "As she gets dressed, you can't help but feel a pang of disappointment."
        $ scene_manager.show_dress_sequence(the_person, temp_outfit)
        "You wanted to continue exploring her body, learning what makes her moan and gasp with pleasure."
        "But as she leaves the room, you remind yourself that this was just a lesson - nothing more."
    $ scene_manager.clear_scene()
    return

#TODO Does this go anywhere now?
    ##lesson result
    #"The sunlight streams through the kitchen window as you pour yourself a cup of coffee, taking a seat across from [the_sister.title] at the breakfast table."
    #mc.name "So, how did things go last night with [the_person.title]?"
    #"[the_sister.title] looks up from her plate, a blush creeping onto her cheeks."
    #the_sister "Oh, uh, it was... amazing, your lessons really paid off."
    #"You raise an eyebrow, curious for details. You encourage her, taking a sip of your coffee."
    #"She hesitates for a moment before diving in."
    #the_sister "Well, we started off slow, like you said. I used my fingers on her first, just like you showed us."
    #"Her hands trace invisible shapes in the air, mimicking the motions you demonstrated."
    #the_sister "And then... oh my god, the sounds she made!"
    #"You listen intently, feeling a thrill course through you as she shares her story."
    #the_sister "It was like nothing I'd ever experienced before."
    #"[the_sister.title] continues, her eyes shining with excitement."
    #the_sister "When I went down on her, she screamed my name like I was the best thing that ever happened to her. And when she returned the favor, it was even better."
    #"You chuckle softly, pleased that your lessons have had such a profound impact on their sex life."
    #mc.name "I'm glad to hear it, just remember, communication is key. Don't be afraid to ask for what you want or need."
    #"[the_sister.title] nods fervently."
    #the_sister "Trust me, we won't forget that, thank you again, [the_person.mc_title]. For everything."
    
    ##lesson result
    #"As you walk across campus, lost in thought, you feel someone tap you on the shoulder."
    #"Turning around, you're met with [the_person.title]'s beaming smile."
    #the_person "[the_person.mc_title]! Hi there, I just wanted to stop by and thank you for all your help."
    #mc.name "Of course, how did things go with [the_sister.title]?"
    #"[the_person.title] bites her lower lip, a look of pure bliss crossing her face."
    #the_person "Last night... Wow, we couldn't get enough of each other. Your techniques were incredible."
    #"Her eyes glitter with excitement as she leans closer to you, almost conspiratorially."
    #the_person "I had her beg for more than once, and when she came..."
    #"She trails off, shivering deliciously. You can't help but feel a surge of satisfaction at her words."
    #mc.name "That's wonderful to hear, just remember, communication is key. Keep practicing those dirty talk skills."
    #"[the_person.title] giggles, blushing deeply."
    #the_person "Oh trust me, we will. Thank you again, [the_person.mc_title]. You've changed our lives."
    #"With one final grateful glance, she turns and walks away, leaving you feeling warm and fuzzy inside."

    #group teaching
    #"The door opens slowly, and in walked two of the most beautiful women you've ever seen - [the_sister.title] and [the_person.title]."
    #"Their eyes are filled with curiosity and determination as they approach you."
    #the_sister "[the_person.mc_title], we wanted to ask if we can learn how to give each other better sex."
    #"You raise an eyebrow, intrigued by their request."
    #mc.name "Why would you want to do that?"
    #"[the_person.title] steps forward, her cheeks flushed."
    #the_person "Because we love each other, but we want our intimacy to be even more intense. We thought maybe you could show us some techniques."
    #"You consider their request for a moment before nodding."
    #mc.name"Alright, let's start with some basic communication exercises. Tell me what you like when you receive oral sex."
    #"[the_sister.title] blushes deeply, but [the_person.title] speaks up first."
    #the_person "Mmm... moaning louder helps me cum faster."
    #mc.name"Good job, [the_person.title]."
    #"Turning back to [the_sister.title], you ask again, and she responds hesitantly."
    #the_sister "Whispering dirty things in my ear really turns me on."
    #mc.name "Now, show me how you touch each other during foreplay."
    #"[the_sister.title] starts, gently caressing [the_person.title]'s [the_person.tits_description], while [the_person.title] reciprocates by massaging [the_sister.title]'s thighs. You stop them."
    #mc.name "A little more passionately, please."
    #"They both giggle nervously before trying again, their movements becoming more sensual, more urgent."
    #"You make sure to compliment them whenever they hit the mark, guiding their hands and lips until they both have a better idea of how to bring pleasure to the other."
    #mc.name "Now, undress each other slowly."
    #"The room falls silent as they strip naked, their bodies illuminated by the dim light."
    #"As they finish, they stand side by side, vulnerable and nervous yet excited."
    #"You start with [the_sister.title], taking your time to explore her body with your fingertips, showing [the_person.title] exactly how to tease and stroke her lover's skin."
    #"Then it's [the_person.title]'s turn for the same treatment."
    #"By now, both women are wet with anticipation, their breath coming in quick gasps."
    #"With one final command, you order them to get on all fours, facing away from each other."
    #mc.name "Slowly, rub your pussies together."
    #"Their moans fill the air as they grind against each other, their wetness creating a lubricant-like effect."
    #"It doesn't take long before they're both crying out in ecstasy, their bodies shuddering under the force of their climaxes."
    #"Finally, they collapse onto the bed, exhausted but satisfied."
    #the_sister "Thank you, [the_person.mc_title]. We had no idea we were capable of such intensity."
    #"[the_sister.title] whispers, nestling into [the_person.title]'s embrace."
    #"You smile warmly at them, knowing that you've helped them find a deeper connection through their love."

    ##group teaching
    #"[the_sister.title] and [the_person.title] stand nervously before you, their eyes downcast."
    #"It's clear they've come together for a reason, and you can't help but feel flattered by their trust."
    #the_sister "We... we wanted to ask for your help."
    #"[the_sister.title] stutters, glancing at [the_person.title] for support."
    #the_person "We think we could be better lovers for each other."
    #"[the_person.title] chimes in, her voice quivering with emotion."
    #"You smile warmly, feeling a surge of excitement at the prospect of teaching these two beautiful women how to please one another."
    #mc.name "I'd be happy to help."
    #"Over the next few sessions, you teach them everything you know about giving and receiving pleasure."
    #"You demonstrate techniques on both girls, showing them how to use their hands, mouths, and bodies to bring their partner to climax."
    #"You start by having [the_sister.title] lie down on the bed while [the_person.title] practices giving her oral pleasure."
    #"You watch as [the_person.title] takes [the_sister.title]'s perfectly shaped [the_person.tits_description] into her mouth, sucking gently before moving down to tease her nipples with her tongue."
    #"Then she slowly works her way down [the_sister.title]'s stomach, stopping at the edge of her wet panties."
    #the_person "Do you want me to remove them?"
    #the_sister "Yes!"
    #"[the_sister.title] moans, arching her back."
    #"[the_person.title] carefully unfastens the tiny buttons, sliding the material down [the_sister.title]'s slender legs."
    #"[the_sister.title] gasps when she sees her pussy exposed, but she doesn't move as [the_person.title] leans forward, tongue darting out to taste her juices."
    #"Meanwhile, you instruct [the_sister.title] on how to give [the_person.title] equal pleasure."
    #"You help her position herself above [the_person.title], her soft [the_person.tits_description] brushing against her lover's face."
    #"Slowly, she lowers herself, kissing along [the_person.title]'s neck and shoulders until she reaches her [the_person.tits_description]."
    #"With gentle pressure, she massages [the_person.title]'s [the_person.tits_description], tweaking her nipples with light pinches until [the_person.title] moans."
    #"Next, you show them how to use their hands, demonstrating on [the_person.title] first."
    #"You kneel between her legs, teasing her entrance with your fingertips before slipping one inside, gradually increasing the speed and depth."
    #"[the_person.title]'s eyes roll back in her head, lost in sensation. Then it's [the_sister.title]'s turn."
    #"You guide her hands over her own body, showing her how to touch herself, how to rub her clit and plunge her fingers into her dripping wetness."
    #"She watches you intently, mimicking your movements as best she can."
    #"By the end of the lessons, both [the_sister.title] and [the_person.title] have a newfound confidence in their abilities."
    #"As they thank you, you can't help but feel proud of the progress they've made, and even more turned on by the thought of them using their new skills on each other."

    ## group teaching
    #"[the_sister.title] and [the_person.title] sit on either side of you on the bed, their eyes fixed on your face, their breaths heavy with anticipation."
    #mc.name "First thing's first, always use some lubricant. Trust me, it makes everything much smoother."
    #"You apply some liberally on your index finger, then slide it between [the_sister.title]'s lips, eliciting a moan of surprise and pleasure."
    #mc.name "Start slow, using gentle circles around the entrance, pay attention to her responses, does she squirm, moan or gasp?"
    #mc.name "These are all signs telling you what she likes."
    #"You explain, demonstrating your technique on her wet labia."
    #"You shift your focus to [the_person.title] next, repeating the process with her."
    #"She arches her back, groaning softly, her hands gripping the armrests tightly."
    #mc.name "Now, gradually increase the pressure and speed until you reach her G-spot. This little nub of flesh, right here."
    #"You press a spot just inside her vagina, causing her to shiver with delight."
    #mc.name "Stroke it firmly yet gently, in a 'come hither' motion."
    #"As you demonstrate this, [the_sister.title] watches attentively, her fingers tracing the shape of [the_person.title]'s clitoris through her panties."
    #"You nod encouragingly, seeing the wheels turning in her mind."
    #mc.name "Remember, communication is key, don't be afraid to ask for what you want or need."
    #mc.name "And don't forget the power of sounds, moaning, sighing, even whispering dirty words can heighten the experience."
    #"By now, both girls are visibly aroused, their bodies trembling with desire."
    #"With one last instruction, you tell them to swap positions so they can experience each other's mouths."
    #"[the_person.title] kneels behind [the_sister.title], her hands caressing her lover's ass as she kisses her way down her spine."
    #"Meanwhile, [the_sister.title] leans over the back of the bed, presenting her pink folds to [the_person.title]."
    #"Their moans echo throughout the room as they lose themselves in their newfound skills, stroking, sucking, and licking each other's sensitive parts."
    #"It's clear they're learning fast, their passionate whispers fueling the fire between them."
    #"Before long, both girls are screaming your name, their orgasms intertwined as they come together in perfect harmony."
    #"When they finally catch their breath, they look up at you gratefully, their bond stronger than ever."
    #"While leaning into [the_person.title]'s embrace, [the_sister.title] whispers up to you."
    #the_sister "Thank you, [the_person.mc_title], we promise to put these new skills to good use tonight."

    ##group lesson result
    #"The following morning, you wake up to find [the_sister.title] and [the_person.title] curled up beside you, still dressed from last night's adventures."
    #"Yawning widely, you stretch and ask them how things went after you fell asleep."
    #"[the_sister.title] exclaims, her cheeks flushed with excitement."
    #the_sister "Last night was amazing! We used everything you taught us – the dirty talk, the techniques...it was like nothing we'd ever experienced before."
    #"[the_person.title] nods in agreement, running a finger along your chest lazily."
    #the_person "We couldn't get enough of each other. We kept going all night long."
    #mc.name "I'm glad to hear that, but don't exhaust yourselves too much. After all, practice makes perfect."
    #"[the_sister.title] giggles playfully."
    #the_sister "We will definitely keep practicing, in fact, maybe we could show you again later?"
    #"Her eyes sparkle mischievously, and you can't help but feel a surge of anticipation course through your veins."
    #mc.name "I wouldn't say no to that, but let's take it slow today. How about we order some breakfast in bed?"
    #"After placing the order, you snuggle closer to the girls, feeling their warmth seep into your bones."
    #"You know they have a long road ahead of them when it comes to mastering their new skills, but with every passing day, you grow more confident that they'll become unstoppable lovers."
