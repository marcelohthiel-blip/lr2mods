label lily_buddy_threesome_label(): #14+
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ the_person.event_triggers_dict["friend_with_benefits"] = the_person.event_triggers_dict.get("friend_with_benefits", 0) + 1
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 15:
        $ surprise_lesson = Action("Surprise Lesson", lily_followup_requirement, "surprise_lesson_label")
        $ mc.business.add_mandatory_crisis(surprise_lesson)
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 17:
        $ sister_invite = Action("Sister Invite", lily_followup_requirement, "sister_invite_label")
        $ mc.business.add_mandatory_crisis(sister_invite)
    #recordings unlock
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 14:
        if "Love Triangle Chat" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Love Triangle Chat")
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) > 16:
        if "Threesome Chat" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("Threesome Chat")
    #current scene
    if the_person.event_triggers_dict.get("friend_with_benefits", 0) < 15:
        pass #TODO move 13 here?
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 16:
        if not mc.business.event_triggers_dict.get("home_cameras", []):
            "SERIOUSLY?!? You still don't have the cameras?"
            if mc.business.funds > 100000:
                $ temp_funds = mc.business.funds/2
                $ mc.business.change_funds(-temp_funds)
            elif mc.business.funds > 10000:
                $ mc.business.change_funds(-1000)
            $ mc.business.event_triggers_dict["home_cameras"].append(lily)
            $ lily.event_triggers_dict["camera_level"] = 0
            $ mc.business.event_triggers_dict["home_cameras"].append(mom)
            $ mom.event_triggers_dict["camera_level"] = 0
            "There you go, these recordings contain story stuff, but the rest can now be watched from your bedroom too."
        "You get an alert on your phone, it looks like [the_sister.title] and [the_person.possessive_title] are hanging out in her room."
        "Things have been a little weird since you watched them together on your bed."
        if mc.current_location_hub != home_hub:
            "You better head home and watch to see if you need to do anything to keep it from spiralling out of control."
        elif mc.location != bedroom:
            "You head to your room to watch and see if you need to do anything to keep it from spiralling out of control."
        else:
            "You should watch and see if you need to do anything to keep it from spiralling out of control."
        $ mc.change_location(bedroom)
        "Pulling up the camera feed you see [the_sister.possessive_title] and [the_person.title] hanging out and chatting."
        "While their other recent activies have been more exciting, you are curious about what they are saying."
        call love_triangle_label(the_sister, the_person) from _call_love_triangle_label
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 17:
        if mc.current_location_hub != home_hub:
            "You head home curious about what will happen next."
        elif mc.location != bedroom:
            "You head to your room curious about what will happen next."
        else:
            "It takes all of your self control to wait and see what will happen next."
        $ mc.change_location(bedroom)
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 18:
        "You get an alert on your phone, it looks like [the_sister.title] and [the_person.possessive_title] are hanging out in her room."
        "Your not sure how they are doing since your and [the_sister.title]'s exhibition for [the_person.title]"
        if mc.current_location_hub != home_hub:
            "You better head home and watch to see if you need to do anything to keep it from spiralling out of control."
        elif mc.location != bedroom:
            "You head to your room to watch and see if you need to do anything to keep it from spiralling out of control."
        else:
            "You should watch and see if you need to do anything to keep it from spiralling out of control."
        $ mc.change_location(bedroom)
        "Pulling up the camera feed you see [the_sister.possessive_title] and [the_person.title] hanging out and chatting."
        "While their other recent activies have been more exciting, you are curious about what they are saying."
        call threesome_chat_label(the_sister, the_person) from _call_threesome_chat_label
    elif the_person.event_triggers_dict.get("friend_with_benefits", 0) < 19:
        "You aren't supposed to know, but tonight is the night."
        if mc.current_location_hub != home_hub:
            "You quickly head home so that you can be ready for them to come find you."
        elif mc.location != bedroom:
            "You head to your room so that you can be ready for them to come find you."
        else:
            "It takes all of your self control to not seek them out, but sit and wait for them to come find you."
        $ mc.change_location(bedroom)
        call first_threesome_label(the_sister, the_person) from _call_first_threesome_label
    else:
        call repeat_threesome_label(the_sister, the_person) from _call_repeat_threesome_label
    $ scene_manager.clear_scene
    return

label surprise_lesson_label(): #14
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    "TODO: visuals, check code"
    if the_person.arousal_perc > the_sister.arousal_perc:
        $ person_one = get_lab_partner()
        $ person_two = lily
        $ temp_outfit = limited_university_wardrobe.decide_on_outfit(person_one)
        "Lying in bed with the lights off, you are preparing to sleep after a long day. Suddenly there is a soft knock at your window."
        $ scene_manager.add_actor(person_one, emotion = "happy")
        "It's [person_one.title] again, practically bouncing with excitement as she looks in at you."
        "It is pretty clear why she is back again so you quickly move to open the window."
        "You help her through the opening and then pull her into an embrace."
        mc.name "I feel a bit bad that you need my help again, but I'd be lying if I said I wasn't looking forward to assisting you."
        person_one "Actually I don't need your help tonight, [person_two.fname] has gotten much better, I just really want a cock to play with."
    else:
        $ person_two = get_lab_partner()
        $ person_one = lily
        $ temp_outfit = get_pajama_outfit(person_one)
        $ scene_manager.add_actor(person_one, temp_outfit, emotion = "happy")
        "Lying in bed with the lights off, you are preparing to sleep after a long day. Suddenly there is a soft noise at your door."
        "It opens slightly and [person_one.possessive_title] quickly slips in and pushes it closed."
        mc.name "Welcome back [person_one.title]."
        mc.name "Another unsatisfying night with [person_two.title]?"
        person_one "Actually she has been getting a lot better, but tonight I just really want a cock to play with."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "Wasting no time, [person_one.title] starts to strip off her clothes."
    $ generalised_strip_description(person_one, strip_list = person_one.outfit.get_underwear_strip_list())
    "You admire the sight before you, but don't have long before her next move."
    $ the_object = make_bed()
    if person_one.has_taboo("touching_cock"):
        "[person_one.title] motions to the [the_object.name]. When you sit down she drops to her knees."
        $ scene_manager.update_actor(person_one, position = "kneeling1")
        person_one "I'm sorry, I know I'm not usually this forward, but I just have to see what you're packing..."
        "She gazes up at you as her hands drift down to your pajamas."
        "She slowly undoes your pants, then pulls them down and off, revealing your erection."
        person_one "Oh [person_one.mc_title]..."
        "[person_one.possessive_title!c] looks at your shaft for a moment, giving it a couple strokes."
    else:
        "Pulling at the waist of your pajamas and fishing out your hardening cock, she then pushes you back to sit on the bed "
        $ scene_manager.update_actor(person_one, position = "kneeling1")
        "Wrapping her hand around you, she kneels at your feet, looking at your cock with wonder as it swells in her hands."
    "She brings her hand back to her mouth, spitting a generous portion of saliva on it, before returning it to your cock."
    "You hear your phone ping from the charger, but have no intention of reaching for it as she begins slowly stroking you."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "[person_one.title] takes her time, enjoying the feel of you pulsing in her hand as she alternates speeds."
    person_one "As much as I love [person_two.fname]. I don't think I could ever give up real cock for her."
    mc.name "I'm glad to hear that, I wouldn't want our fun to stop completely."
    person_one "It's so warm, soft and hard at the same time. Plus it is so clear how desperate you are for more of my attention."
    "She plants a few kisses on your thighs, nibbling lightly towards your groin."
    "You are slightly distracted by the fact that your phone is still pinging as someone tries to text you."
    mc.name "Having you beg to service me certianly helps, plus you've gotten pretty good at taking care of it."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    if not person_one.has_taboo("vaginal_sex"):
        person_one "This is just the warm up to make sure you last long enough when I start riding you."
    elif not person_one.has_taboo("anal_sex"):
        person_one "This is just the warm up to make sure you can pound my tight little ass for a good long time."
    else:
        person_one "I want to make sure you get off now so we can keep having fun all night long."
    "The idea of spending all night with [person_one.title] gets you closer to your peak."
    "Combined with her skilled ministrations, it isn't long before you can feel yourself building towards an orgasm."
    if not person_one.has_taboo("sucking_cock"):
        "Your phone starts to ring, but you ignore it as [person_one.title] takes your tip into her mouth, causing you to moan in pleasure."
    else:
        "Your phone starts to ring, but you ignore it as [person_one.title] plants a gentle kiss on the tip of your cock, causing you to moan in pleasure."
    mc.name "[person_one.title] keep going, I'm so close."
    "She pulls back, smiling up at you as she continues to stroke your slowly."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    person_one "Where do you want to cum [person_one.mc_title]?"
    mc.name "Take it in your mouth so we don't have to clean anything up and can keep right on having fun."
    if person_one.get_opinion_score("drinking cum") < 0:
        person_one "I guess, for you I can do that."
    else:
        person_one "Great idea, plus you always taste so good."
    "With a smile she starts to lean her head back towards your cock as she stokes you and massages your balls."
    "Just before she get you in her mouth, your door swings open to reveal [person_two.title]."
    $ scene_manager.add_actor(person_two, display_transform = character_left_flipped, emotion = "angry")
    "The shock breaks your focus and suddenly you are cumming violently in [person_one.title]'s hand."
    $ person_two.cum_on_tits()
    $ person_one.cum_on_face()
    $ ClimaxController.manual_clarity_release(climax_type = "face", person = person_one)                        
    "The first shot flies across the room to splatter on [person_two.possessive_title]'s chest while the rest unloads to coat [person_one.possessive_title]'s face."
    person_two "Sorry, I thought... wait [person_one.fname]?"
    "[person_one.title] had started to turn to see who it was but now seems frozen in panic while [person_two.title] is struck motionless by shock."
    mc.name "[person_two.fname] I can explain..."
    if the_person.arousal_perc > the_sister.arousal_perc:
        person_two "You can explain why my girlfriend is kneeling in my brother's room and sucking him off? Really?"
    else:
        person_two "You can explain why my girlfriend is kneeling in her brother's room and sucking him off? Really?"
    "The shock combined with the orgasm still pusling through you stalls your brain as you hope some clarity will kick in soon."
    mc.name "Yes? Look it's not that big of a deal... I've been helping her with some... things."
    person_two "And what demanding sexual favors in return?"
    "Before you can get out a reply [person_one.title] comes to your defense."
    person_one "He is helping me [person_two.fname]. He's been teaching me how to take care of you in bed and well..."
    person_one "We both get so horny during our lessons that we needed some release."
    person_two "Wait, he's teaching you too?"
    person_one "Yes, but for you!"
    "There is a momentary pause, then [person_one.title] seems to realise what [person_two.title] said."
    person_one "Wait... what do you mean too?"
    "Another pause as [person_two.title] realises her slip and stammers as she shifts from accusation to defense."
    person_two "Well... me and you were having some trouble... and I wanted to be able to get you off and..."
    person_two "I needed someone with more experience with women than me."
    person_two "I was doing it for you, I just want to make you happy!"
    person_one "That's what I want too, you were so good and I wanted to make sure I could keep you satisfied."
    person_two "You thought I was good? I thought I was letting you down."
    person_one "You weren't perfect, but I felt so clumsy at first and you seemed so confident."
    "A range of emotions flicker across the girl's faces before they move towards each other, wrapping their girlfriend up in a loving embrace."
    $ scene_manager.update_actor(person_one)
    $ person_two.cum_on_face()
    $ scene_manager.update_actor(person_two)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "Soon they are locked in a passionate kiss. Neither seems to care, or remember, that [person_one.title]'s face is covered in your cum."
    $ the_person.change_arousal(10)
    $ the_sister.change_arousal(10)
    "[person_one.title] starts to pull at [person_two.title]'s clothes, almost like they forgot where they were."
    "You don't mind the show, and it is starting to restore your spent memeber, but you figure you should probably remind them of your presence."
    mc.name "Um... girls?"
    $ scene_manager.update_actor(person_one)
    $ scene_manager.update_actor(person_two)
    "They pull apart a bit to look at you, another parade of emotions running across their features."
    person_one "Sorry, [person_one.mc_title] we can go... unless..."
    "She takes a look at her girlfriend, raising an eyebrow in a silent question. [person_two.title] nods, turning to you."
    person_two "Do you want to watch?"
    mc.name "Seriously?"
    person_one "Yeah, maybe you could give us some more pointers once you see us in action."
    mc.name "Of course I want to watch you together, you're both incredibly hot."
    $ scene_manager.update_actor(person_one)
    $ scene_manager.update_actor(person_two)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "With mirrored smiles, they waste no time before resuming their actions, hands roaming over each other as they pull at clothes."
    # strip to one layer
    $ scene_manager.strip_to_underwear(person_two)
    $ generalised_strip_description(person_two, strip_list = person_two.outfit.get_underwear_strip_list())
    "As they shift towards your bed, you get up and move to take a seat on your computer chair."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "[the_person.title] lays back on your bed, pulling [the_sister.title] on top of her."
    $ scene_manager.update_actor(the_sister, position = "doggy")
    if not the_person.tits_visible:
        $ temp_top = the_person.outfit.get_upper_top_layer
        $ scene_manager.draw_animated_removal(the_person, temp_top)
        "As [the_sister.possessive_title] lowers herself down, she pushes at [the_person.title]'s [temp_top.display_name], revealing her [the_person.tits_description]."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "[the_sister.title] lowers her head, licking around one of [the_person.title]'s nipples before pulling it into her mouth with a gentle sucking motion."
    $ the_person.change_arousal(10)
    "[the_person.title] moans softly. Satisfied with that recation, [the_sister.title] swaps to the other nipple, giving it the same treatment before moving up for a lingering kiss. "
    if not the_sister.tits_visible:
        $ temp_top = the_sister.outfit.get_upper_top_layer
        $ scene_manager.draw_animated_removal(the_sister, temp_top)
        "When they come up for air, [the_person.possessive_title] wastes no time pulling aside [the_sister.title]'s [temp_top.display_name] to reveal her [the_sister.tits_description]."
    $ the_sister.change_arousal(10)
    "[the_person.title] attempts to return the favor by tilting her head towards [the_sister.possessive_title]'s chest, but she has a different idea."
    if the_person.outfit.vagina_available:
        "Moving slowing down [the_person.possessive_title]'s body, and pulling her [temp_bottom.dispaly_name] with her, [the_sister.title] gets into position over her [the_person.pubes_description] pussy."
    else:
        "Moving slowing down [the_person.possessive_title]'s body, [the_sister.title] gets into position over her [the_person.pubes_description] pussy."
    $ the_person.change_arousal(10)
    $ the_sister.change_arousal(10)
    "Although they are both likely warmed up enough, [the_sister.title] takes her time teasing [the_person.title]'s inner thighs."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "As eager as you are for them to continue, it is good to see your lessons have paid off."
    the_person "Mmm... Ooo... p-please [the_sister.name]..."
    "Satisfied with that response, [the_sister.possessive_title] finally gets to work on her girlfriend's pussy."
    the_person "Yesss... right there... keep going..."
    $ the_person.change_arousal(10)
    if the_sister.outfit.vagina_available:
        $ temp_bottom = the_sister.outfit.get_lower_top_layer
        "While continuing to take care of her girlfriend, [the_sister.title] begins rubbing her [temp_bottom.display_name] clad pussy against her leg."
    else:
        "While continuing to take care of her girlfriend, [the_sister.title] begins rubbing her [the_sister.pubes_description] pussy against her leg."
    $ the_sister.change_arousal(10)
    "As she grinds down, you see a wet spot spread on [the_person.title]'s leg."
    "As they get more and more passionate you think about how disappointing the videos are in comparison to having a front row seat."
    if the_person.get_opinion_score("anal sex") >0:
        "Sensing that she is ready for more, [the_sister.title] pivots to free a hand and brings her fingers to rest against [the_person.title]'s puckered asshole."
    else:
        "Sensing that she is ready for more, [the_sister.title] pivots to free a hand and brings her fingers to rest against [the_person.title]'s glistening cunt."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "Pushing firmly but gently, she works first one and then two into her girlfriend's tight hole."
    "Curling them back and forth in search of the right spot, it isn't long before [the_person.title]'s moans raise a notch."
    $ the_person.change_arousal(10)
    $ the_sister.change_arousal(10)
    "All the while, [the_sister.title] continues to lick and suck at her clit while taking care of herself as well."
    "The request for pointers was mostly in jest, which is fortunate, they seem to really know one another's bodies now."
    $ the_person.have_orgasm()
    "In fact, it isn't long before [the_person.title] clenches up and lets out a loud cry as she starts to orgasm."
    "As she trembles, she pushes feebly at [the_sister.title], trying to get her attention away from her sensitive flesh."
    $ scene_manager.update_actor(the_sister)
    "With a final lick, [the_sister.title] sits up, grinding down harder as she moves one hand to her pussy and another to her [the_sister.tits_description]."
    $ the_sister.have_orgasm()
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "[the_person.title] is in no state to help, but [the_sister.title] quickly finishes herself off, shaking through a more subuded orgasm of her own."
    $ scene_manager.update_actor(the_sister)
    "By the time her spasms stop, [the_person.title] has recovered enough to pull her down into an embrace, kissing her lovingly on the cheek."
    "Wrapping her arms around [the_sister.title], [the_person.title] turns toward you with a tired smile."
    the_person "How did we do coach?"
    mc.name "That was incredible, I've got a standing ovation here for how hot the performace was."
    "You glace down at your cock standing up firmly to drive home your point. She looks down too, before shifting slighty."
    the_person "Come here [the_person.mc_title], I think I can help you with that."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(10)
    "As you walk over, [the_sister.title] pivots to the side, giving you room to get to her lover's mouth."
    "The show really does have you on the edge, and as you slip into [the_person.title]'s mouth, you know you won't last long."
    "Having [the_sister.possessive_title] casually watch as she idly runs a finger over [the_person.title]'s nipple helps even more."
    "Sure enough, the situation, the view, and [the_person.title]'s talented tongue soon have you shooting your load into her mouth."
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
    $ the_person.cum_in_mouth()
    "Although she swallows most of it, your rapidly softening cock pulls a strand of it out along her cheek."
    "Your eyes are drawn to [the_sister.title] as she leans down to kiss [the_person.title], first on her lips and then along her cheek as she licks up your cum."
    "When [the_person.title] is clean, [the_sister.title] looks up at you with a smile."
    the_sister "That's twice in one day that I've had your cum on my lips. It's weird how normal it is starting to feel."
    if the_person.get_opinion_score("incest") < 1:
        $ the_person.increase_opinion_score("incest")
    $ the_person.discover_opinion("incest")
    if the_person.get_opinion_score("incest") < 0:
        the_person "It's a little weird how comfortable you are with your bother's cum, but I don't hate it."
    elif the_person.get_opinion_score("incest") < 1:
        the_person "I'm not sure how to feel about how comfortable you are with your brother's cum."
    elif the_person.get_opinion_score("incest") < 2:
        the_person "I'm surprised your so comforable with your bother's cum, but I kinda like it."
    else:
        the_person "It's so hot watching you enjoy your brother's cum."
    if the_sister.get_opinion_score("drinking cum") > 0:
        the_sister "Despite my obvious appretiation for the female form I also really enjoy the taste of cum."
    elif the_sister.get_opinion_score("drinking cum") < 0:
        the_sister "I've never been a huge fan of the taste of cum, but licking it off you makes it better."
    else:
        the_sister "I don't mind, and licking it off your beautiful face makes it worthwhile."
    if the_sister.get_opinion_score("incest") > 0:
        the_sister "Somehow, the fact that it is my brother's makes it taste even better."
    else:
        the_sister "Although, there is still some instictive weirdness because it belongs to my brother."
    "They linger a bit longer, kissing gently as they recover from their orgasms."
    "After two loads in quick succession, you don't feel like you'll be able to rally, despite the enticing sight."
    $ scene_manager.update_actor(the_sister)
    "Sensing that things are at an end for the night, [the_sister.title] climbs off of [the_person.title] and helps pull her to her feet."
    $ scene_manager.update_actor(the_person)
    "They each step up to you to give you a quick kiss before heading for the door."
    $ scene_manager.update_actor(the_sister)
    $ scene_manager.update_actor(the_person)
    $ body_description = get_body_description(the_sister)
    "As you watch their [body_description] asses walk out of your room, you wonder where things will go from here."
    "It wasn't exactly a threesome, but pretty close. If nothing else, everything is out in the open now, so you'll have to see how they feel about this evolution of your relationship."
    $ surprise_follow_up_1 = Action("Surprise Follow Up 1", teaching_request_requirement, "surprise_follow_up_1_label", requirement_args=[the_sister, day])
    $ mc.business.add_mandatory_crisis(surprise_follow_up_1)
    $ scene_manager.clear_scene()
    return

label surprise_follow_up_1_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ mc.change_location(lily_bedroom)
    $ scene_manager.add_actor(the_sister, position = "sitting")
    "You walk into [the_sister.possessive_title]'s room, finding her sitting on the bed, typing away on her laptop."
    "She looks up as you enter, a hint of a smile playing on her lips."
    the_sister "Hey, [the_sister.mc_title]!"
    mc.name "[the_sister.title], can we talk?"
    "She closes her laptop and sets it aside, her expression turning serious for a moment before relaxing again."
    the_sister "Of course, [the_sister.mc_title]. What's on your mind?"
    "You take a deep breath, choosing your words carefully."
    mc.name "I wanted to check in with you about last night. With [the_person.fname]... everything that happened."
    "[the_sister.title]'s eyes sparkle with amusement, but she remains calm, her voice even when she responds."
    the_sister "Oh, you mean when [the_person.fname] sucked you off and then shared a little kiss with me afterwards?"
    if the_sister.has_taboo("blowjob"):
        the_sister "You didn't hear me complaining last night did you?"
        mc.name "But are you okay with it? I know it's a bit weird, us being siblings..."
        "[the_sister.title] waves a hand dismissively."
        the_sister "[the_sister.mc_title], after the other things we've been doing, that didn't seem out of bounds."
    elif the_sister.has_taboo("anal_sex"):
        the_sister "It's not like I haven't tasted your cum before."
    else:
        the_sister "It's not like we haven't crossed bigger lines than that before."
    $ the_sister.discover_opinion("drinking cum")
    if the_sister.has_cum_fetish:
        the_sister "Plus, you know how much I love the taste of your cum."
    elif the_sister.opinion.drinking_cum > 0:
        the_sister "Besides, I kinda like the taste of cum."
    else:
        the_sister "I'm not a huge fan of the taste, but sometimes it is okay."
    "Her words reassure you and you sit down beside her, feeling a sense of camaraderie wash over you."
    mc.name "So, what did [the_person.fname] think about our... actions? Did she enjoy it as much as we did?"
    "[the_sister.title]'s face lights up with a mischievous grin."
    $ the_person.discover_opinion("incest")
    if the_person.opinion.incest > 0:
        the_sister "[the_person.fname] loved every minute of it. She told me later that she felt so close to us after experiencing such an intimate moment together."
        "Your heart swells with happiness knowing that [the_person.fname] enjoyed the experience."
        mc.name "That's great to hear. I was worried she might not feel the same way."
        the_sister "Don't worry, [the_sister.mc_title]. [the_person.fname] is enthusiastic about these kinds of things, she's always looking for new ways to spice up our sessions."
    else:
        the_sister "[the_person.fname] was a little weirded out by it. She told me later that she felt so close to us, but wasn't sure about us being together as siblings."
        "You falter, concerned about how much [the_person.fname] actually enjoyed the experience."
        mc.name "I was worried she might not feel the same way."
        the_sister "Don't worry, [the_sister.mc_title]. [the_person.fname] is open minded about these kinds of things, she's willing to try new things to spice up our sessions."
    mc.name "I guess we've got quite the dynamic going here, huh?"
    "You chuckle at a situation that would have seemed absurd a few months ago. [the_sister.title] laughs along with you, her eyes twinkling with delight."
    the_sister "Absolutely. Our dynamic is unique, and it works for us. We just need to keep communicating openly and making sure everyone's on board."
    "You relax a bit, relieved that things are going well enough that they can continue as is, maybe there is even hope for more."
    the_sister "You know, we could plan another session soon if you're interested."
    mc.name "Really?"
    the_sister "Sure, why not? Now that everything is out in the open we shouldn't need to sneak in time together."
    mc.name "That would be pretty great."
    the_sister "I might still spend some alone time with [the_person.fname], but if you are around maybe we can play together again."
    "Bouyed by that thought, you head out and procede through your day."
    $ surprise_follow_up_2 = Action("Surprise Follow Up 2", teaching_request_requirement, "surprise_follow_up_2_label", requirement_args=[the_person, day])
    $ mc.business.add_mandatory_crisis(surprise_follow_up_2)
    $ scene_manager.clear_scene()
    return

label surprise_follow_up_2_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You spot [the_person.possessive_title] across the quad, sitting alone under a sprawling oak tree. Her long, [the_person.hair_colour[0]!l] hair cascades down her back as she reads a book, seemingly lost in thought."
    "You take a deep breath and clear your throat to announce your arrival. [the_person.title] looks up, her [the_person.eyes[0]!l] eyes meeting yours with a mix of recognition and wariness."
    mc.name "Hey, how are you doing today?"
    the_person "I'm alright, considering everything that went down last night."
    mc.name "Yeah, I can imagine. It must've been pretty intense, seeing [the_sister.title] and me... you know."
    the_person "I'd be lying if I said it wasn't shocking at first, but looking back I guess it makes sense."
    mc.name "I just wanted to check in and make sure you're cool with everything that happened between us."
    "[the_person.title] looks back up at you, a hint of a smile playing on her lips."
    if the_person.opinion.incest > 0:
        the_person "To be honest, [the_person.mc_title], I found it incredibly hot thinking of you with [the_sister.fname]."
        the_person "And when she licked up your cum...well, let's just say it was a new experience I won't soon forget."
        mc.name "I'm glad you enjoyed it. I was worried you might feel weird about the whole situation since she is my sister."
    else:
        the_person "To be honest, [the_person.mc_title], I found it a bit odd thinking of you with [the_sister.fname]."
        the_person "But when she licked up your cum... well, it was something I won't soon forget."
        mc.name "I was worried you might feel weird about the whole situation since she is my sister."
    "[the_person.fname] shrugs, her expression thoughtful."
    the_person "Honestly, it made me realize that desire knows no bounds - not even familial ones."
    the_person "If I'm fully honest, it's sparked a newfound curiosity within me about exploring that further."
    "You swallow hard, processing her statement. The idea of delving into more taboo scenarios sends a thrill through you, but you also want to ensure [the_person.fname] is comfortable with the pace."
    mc.name "So, um, would you be open to maybe... recreating something like that again sometime?"
    "[the_person.fname]'s eyes sparkle with intrigue as she considers your proposal."
    the_person "I think that could be arranged, as long as we're all on the same page, of course."
    "You exhale a sigh of relief, feeling a sense of excitement and anticipation wash over you. The possibilities seem endless, and you can't wait to see where this new dynamic will lead."
    "You give [the_person.title] a quick embrace before you head back to the rest of your day, excited for the future."
    $ scene_manager.clear_scene()
    return

label sister_invite_label(): #16
    $ scene_manager = Scene()
    $ the_sister = lily
    $ the_person = get_lab_partner()
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_sister).get_copy()
    if temp_outfit.get_bra():
        $ temp_outfit.remove_clothing(temp_outfit.get_bra())
    if temp_outfit.get_panties():
        $ temp_outfit.remove_clothing(temp_outfit.get_panties())
    $ scene_manager.add_actor(the_sister, visible = False)
    $ scene_manager.apply_outfit(the_sister, temp_outfit)
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person).get_copy()
    if temp_outfit.get_bra():
        $ temp_outfit.remove_clothing(temp_outfit.get_bra())
    $ scene_manager.add_actor(the_person, visible = False)
    $ scene_manager.apply_outfit(the_person, temp_outfit)
    "INCOMPLETE LABEL" #TODO
    "A soft knock echoes through your bedroom door, breaking the silence of the evening."
    mc.name "Come in!"
    $ scene_manager.show_actor(the_sister, emotion = "happy")
    "The door swings open to reveal [the_sister.possessive_title] standing in the doorway with a coy smile playing on her lips."
    the_sister "Hey, [the_sister.mc_title], I was thinking... why don't you come over to my room for a bit?"
    the_sister "[the_person.fname]'s here too, and we've got some fun plans in store for you."
    "Your pulse quickens at the prospect of spending time with both girls, especially given the intimate nature of your recent group activities."
    mc.name "Sure thing, [the_sister.title]. Lead the way."
    $ scene_manager.update_actor(the_sister, position = "walking_away")
    $ mc.change_location(hall)
    "[the_sister.title] grins, her eyes sparkling with mischief as she takes your hand and leads you down the dimly lit hallway."
    "You take a moment to appreciate the view of her skirt covered ass."
    $ mc.change_location(lily_bedroom)
    $ scene_manager.show_actor(the_person, emotion = "happy", position = "sitting", display_transform = character_left_flipped(xoffset = .3))
    "When you arrive at her room, you find [the_person.title] already there, leaning back in a chair at the desk."
    the_person "Welcome, [the_person.mc_title], we've been looking forward to this moment all evening."
    $ scene_manager.update_actor(the_sister, position = "stand3")
    "[the_sister.title] releases your hand and steps back, her gaze raking over your body with an appreciative hunger."
    the_sister "Why don't you get comfortable, big brother?"
    $ temp_top = the_sister.outfit.get_upper_top_layer
    $ scene_manager.draw_animated_removal(the_sister, temp_top)
    "Without waiting for a response, [the_sister.title] begins to undress, peeling off her [temp_top.display_name] to reveal that she was not wearing a bra."
    $ temp_bottom = the_sister.outfit.get_lower_top_layer
    $ scene_manager.draw_animated_removal(the_sister, temp_bottom)
    "Your mouth goes dry as she continues to strip, pulling down her [temp_bottom.display_name] and revealing smooth, toned skin and the tantalizing curves of her hips."
    "You stand there frozen in place, unable to tear your eyes away from the sight before you."
    $ mc.change_arousal(10)
    $ scene_manager.strip_full_outfit(the_sister)
    "As [the_sister.title] discards her final article of clothing, she takes your hand and gently guides you towards the bed."
    the_sister "Let's get you out of these clothes."
    "[the_sister.title]'s deft fingers work swiftly, undoing each button until your shirt falls open, exposing your chest to her hungry gaze."
    "She leans in, pressing her lips to your collarbone as her hands slide down to palm your growing erection through your pants."
    $ mc.change_arousal(10)
    the_sister "Mmm, look at you, so hard already, just for me."
    "[the_person.title] watches intently from her perch, a blush coloring her cheeks as she toys with her own nipples through the thin fabric of her top."
    the_person "That's right, get your big brother ready for your tight little cunt."
    $ the_person.change_arousal(10)
    "[the_sister.title] chuckles, nipping at your jawline before trailing kisses down your neck."
    the_sister "Patience, [the_person.fname]. We'll get there."
    $ scene_manager.update_actor(the_sister, position = "kneeling1")
    "She drops to her knees, fumbling with your belt buckle as she gazes up at you with lust-filled eyes."
    the_sister "Gonna suck this big cock till you're begging for [the_sister.possessive_title]'s pussy."
    $ mc.change_arousal(10)
    "Her words send a jolt of pleasure straight to your groin, and you groan as she frees your length, stroking it firmly."
    $ scene_manager.update_actor(the_sister, position = "blowjob")
    "She smirks, licking a bead of precum from the tip before engulfing you in her warm mouth. Her head bobs eagerly, taking you deeper with each pass until she's swallowing around your shaft."
    mc.name "Fuck, [the_sister.fname]... your mouth feels amazing."
    "The wet sounds of her sucking fill the room, mingling with your moans of delight."
    $ scene_manager.update_actor(the_person, position = "cowgirl")
    $ temp_top = the_person.outfit.get_upper_top_layer
    $ scene_manager.draw_animated_removal(the_person, temp_top)
    "Meanwhile, [the_person.fname] has shed her [temp_top.display_name], revealing [the_person.tits_description] topped with rosy nipples."
    "She pinches and tugs at them, panting softly as she watches the lewd display."
    $ the_person.change_arousal(10)
    the_person "Oh god, [the_sister.mc_title], [the_sister.fname]'s such a slut for your dick."
    $ temp_bottom = the_person.outfit.get_lower_top_layer
    $ scene_manager.draw_animated_removal(the_person, temp_bottom, half_off_instead = True)
    "Her free hand dips between her thighs to rub at her clit as she continues to watch."
    $ mc.change_arousal(10)
    "[the_sister.title] hums in approval around your shaft, pulling back to take a breath."
    $ scene_manager.update_actor(the_sister, position = "missionary")
    "The moment [the_sister.title] releases your cock, you take advantage of the pause to pull her up to the bed, rolling on your side."
    $ the_sister.change_arousal(10)
    "You part her legs, settling a hand between them as you begin to explore the territory between her thighs."
    "The first touch of your fingertips sends shivers coursing through [the_sister.title]'s body, her hips bucking upward in search of more contact."
    "You oblige, increasing the pressure and tempo as you delve deeper into her folds. Her moans grow louder, the sound causing your cock to twitch with anticipation."
    $ the_sister.change_arousal(10)
    "As you build toward her first climax, you glance up to find [the_person.title] still watching, her face aglow with excitement."
    "Her fingers are busy now, pumping into her cunt as she urges you on with whispered encouragement."
    $ the_person.change_arousal(10)
    the_person "Faster, [the_sister.mc_title], faster! Make [the_sister.possessive_title] scream!"
    $ mc.change_arousal(10)
    "Her words send a surge of heat through your veins, and you groan as [the_sister.title]'s hand wraps around your hard length."
    "She strokes you slowly, her grip firm and purposeful as she watches your reaction."
    $ the_sister.change_arousal(10)
    "You lean down to [the_sister.title], capturing her lips in a searing kiss. Her tongue delves into your mouth, tangling with yours as she arches into your touch."
    "A short time later, [the_sister.title] pulls back from the kiss to take a deep breath as her cries reach a fever pitch and you push her over the edge."
    $ the_sister.have_orgasm()
    $ play_female_orgasm()
    "As [the_sister.title]'s climax crashes over her, her inner walls clench rhythmically around your exploring fingers."
    "You continue to stroke her through the aftershocks, prolonging her pleasure until she's limp and gasping beneath you."
    $ the_sister.change_arousal(10)
    if the_sister.has_taboo("vaginal_sex"):
        $ temp_word = "ass"
    else:
        $ temp_word = "cunt"
    $ the_person.change_arousal(10)
    the_person "I want to watch you take him, [the_sister.fname], I want to see his cock stretching your tight little [temp_word] while you scream his name."
    "[the_sister.title] moans at the crude description, thrusting her hips up in response."
    the_sister "Fuck yes, I need my brother's dick so bad right now."
    "Turning to you she continues."
    the_sister "Please, I need you inside me. Fuck me like only a big brother can."
    "Satisfied that she's thoroughly worked up, you withdraw your hand and position yourself at the entrance to her [temp_word]."
    "With a slow, deliberate thrust, you bury yourself inside her warm, welcoming depths."
    "As you sink into [the_sister.title], her walls clamping down on your length, you feel the world narrow to the sensation of [the_sister.possessive_title]'s [temp_word] surrounding you."
    if the_sister.has_taboo("anal_sex"):
        the_sister "You have no idea how long I've wanted this, to have my big brother's cock buried deep inside me..."
        $ the_sister.break_taboo("anal_sex")
    $ the_sister.change_arousal(10)
    the_sister "Ohhh, [the_sister.mc_title]! My big brother's cock feels so good inside me..."
    "You set a steady pace, savoring the sensation of being buried within [the_sister.possessive_title]'s tight heat."
    mc.name "You're such a dirty girl, [the_sister.fname], taking your big brother's cock like the slutty little sister you are..."
    $ the_sister.change_arousal(10)
    "[the_sister.title]'s moans grow louder, her hips bucking towards yours with increasing urgency."
    the_sister "Yes, [the_sister.mc_title], fuck me harder! Use me like your personal fucktoy!"
    $ the_person.change_arousal(10)
    "[the_person.fname]'s eyes never leave the intimate scene unfolding before her, her hand moving in time with your thrusts as she pleases herself."
    the_sister "Look at him go, [the_person.fname], my big brother's cock is stretching me out so good..."
    the_person "Oh god... so hot..."
    "[the_person.title] gets suddenly louder and you turn to look as she starts to shake her way through an orgasm."
    $ the_person.have_orgasm()
    $ play_female_orgasm()
    "You and [the_sister.possessive_title] pause for a moment to watch as your shared girlfriend cums while watching you have sex."
    "She collects herself, bringing her hand up to lick off her fingers before refocusing on the two of you."
    the_person "Keep going, [the_sister.mc_title], make her cum again on that huge dick. I want to see her lose control again."
    $ mc.change_arousal(10)
    the_sister "Yeah big brother, fuck me nice and hard then fill me up with your seed."
    "[the_sister.title]'s words and [the_person.fname]'s urging spur you on, your pace quickening as you chase another peak for your willing sister."
    "With a final, powerful thrust, you send [the_sister.title] careening over the edge again."
    $ the_sister.have_orgasm()
    $ play_female_orgasm()
    "[the_sister.title]'s screams of ecstasy echo off the walls, her body trembling with the force of her release."
    "Her inner muscles clamp down around you, milking your length as she rides out her second intense climax."
    "Hilt deep, her pulsing triggers your own orgasm and you erupt inside [the_sister.title], flooding her womb with your hot seed."
    if the_sister.has_taboo("vaginal_sex"):
        $ the_sister.cum_in_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "ass", person = the_sister)
    else:
        $ the_sister.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_sister)
    "As the waves subside, she collapses back onto the mattress, her chest heaving with ragged breaths."
    "As you relax, your softening member slips free from [the_sister.title]'s tender grasp, she wraps her arms around your shoulders, holding you close as her body continues to tremble with aftershocks."
    "A trickle of cum escapes from [the_sister.title]'s stretched opening, glistening in the dim light."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[the_person.fname], who'd been watching with rapt attention, finally slides off the desk and pads across the floor to join you both."
    $ scene_manager.update_actor(the_person, position = "doggy") #TODO offset
    "[the_person.fname] crawls onto the bed, positioning herself between [the_sister.title]'s thighs."
    "She leans in, her tongue darting out to lap at the spillage, then delving deeper to taste [the_sister.title]'s still-sensitive [temp_word]."
    the_person "Mmm, [the_person.mc_title]'s cum tastes so good."
    "[the_sister.title], still reeling from the intensity of your lovemaking, winces slightly as [the_person.fname]'s tongue brushes against her oversensitive flesh."
    "[the_person.fname] notices and pauses, her apologetic gaze flicking up to meet [the_sister.title]'s strained expression."
    the_person "I'm sorry [the_sister.fname] I didn't mean to hurt you."
    the_sister "It's okay, [the_person.fname]. I'm just... a bit sensitive right now."
    "[the_person.fname] pulls back and glances up at you with a sultry smile, her intentions clear."
    "You nod, understandingly, and shift closer to offer [the_person.fname] access to your spent member."
    "She takes it eagerly, wrapping her lips around the head and sucking gently to collect the remaining drops of cum."
    $ the_person.cum_in_mouth()
    $ scene_manager.update_actor(the_person, position = "stand3") #TODO offset
    "When she pulls away, she climbs up to press a lingering kiss to [the_sister.title]'s mouth, sharing the salty-sweet flavor of your combined essence."
    "[the_sister.title]'s eyes flutter closed, a soft moan vibrating against [the_person.fname]'s lips as she savors the taste."
    "As [the_person.fname] pulls back, a satisfied sigh escapes her lips."
    the_person "Mmm, that hit the spot, thanks for sharing, [the_sister.title]."
    "[the_sister.title] grins, her own satisfaction evident in the languid sprawl of her body beside you."
    the_sister "Anytime, [the_person.fname], anytime."
    $ scene_manager.update_actor(the_person, position = "missionary") #TODO offset both sitting?
    "[the_sister.title]'s words hang in the air, a soft smile spreading across her face as she settles back against the pillows, drawing [the_person.fname] close."
    "The two lovers nestle together as they bask in the afterglow of your lovemaking."
    # lighting
    "You get up to turn off the light and after hesitating at the door a moment you turn around and climb into bed with them."
    "They don't object, so you settle down, exhaustion and contentment helping you quickly drift off to sleep."
    $ scene_manager.clear_scene
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sister_invite
    call sister_invite_morning_label() from _call_sister_invite_morning_label
    return "Advance Time"

label sister_invite_morning_label():
    $ scene_manager = Scene()
    $ the_sister = lily
    $ the_person = get_lab_partner()
    $ scene_manager.add_actor(the_sister, visible = False)
    $ scene_manager.add_actor(the_person, visible = False)
    $ scene_manager.strip_full_outfit(the_sister)
    $ scene_manager.show_actor(the_sister, emotion = "happy")
    $ scene_manager.strip_full_outfit(the_person)
    $ scene_manager.show_actor(the_person, emotion = "happy")
    "INCOMPLETE LABEL" #TODO
    "It's morning, and as you lay there, drifting into consciousness, you remember last night."
    "Fucking [the_sister.possessive_title] while her girlfriend watched was quite the achievement."
    "That fact that she seemed so into the taboo nature of it really added to the experience."
    "You're awake enough to feel the presence of at least one other person in the bed, and wonder if they're both still asleep."
    "Suddenly, a warm tongue darts out to trace circles around the head of your morning wood. So at least one is awake."
    "You let out a groan, looking down to see [the_person.title]'s beautiful face, her eyes locked onto yours as she takes you deeper into her mouth."
    "At the same time, [the_sister.title] stirs, propping herself up to look down at the way her girlfriend is slobbering on your cock."
    "[the_person.title]'s tongue dances, stroking and teasing every inch of your length. You can feel the wet heat surrounding you, driving you wild with lust."
    "As she works her magic, her hands explore your body, tracing patterns across your chest and stomach before finding their way down to caress your balls."
    "The sensation is overwhelming—the combination of her hot mouth, skilled fingers, and loving gazes sending you spiraling into a world of pure pleasure."
    "You reach out to run your fingers through [the_person.title]'s hair, guiding her movements as she bobs her head up and down on your cock."
    "In response, [the_person.title] increases the pressure of her suction, causing you to moan loudly."
    "As she continues her assault on your senses, you can feel the familiar tingling in your balls building to a crescendo."
    $ ClimaxController.manual_clarity_release(climax_type = "throat", person = the_person)
    "With one firm thrust you force [the_person.title] to take all of you into her mouth, and you explode in a wave of bliss."
    $ the_person.cum_in_mouth()
    "Your cum pours down her throat as she greedily sucks away every last drop."
    $ scene_manager.update_actor(the_sister, position = "stand2")
    "As the two of you catch your breaths, [the_sister.title] climbs out of bed, streching her nude body before grabbing one of your shirts from the laundry basket."
    # apply item
    the_sister "I need to go take a shower to rinse off last night's fun... do either of you want to join me?"
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[the_person.title] scoots up the bed until she is next to you."
    the_person "I'm too comfortable to get all the way up yet. I think I might just cuddle with [mc.name]."
    the_sister "[mc.name]?"
    menu:
        "Go with her /n not written (disabled)":
            pass
        "Stay here":
            mc.name "Cuddling sounds nice. You have fun in the shower [the_sister.fname]."
            $ scene_manager.update_actor(the_sister, position = "walking_away")
            "As [the_sister.title] turns to leave [the_person.title] wraps her arms around your waist, nuzzling her face into your chest."
            $ scene_manager.hide_actor(the_sister)
            the_person "I love how you make me feel."
            "With a gentle smile, you pull [the_person.title] closer, and you can feel her heart racing against your chest."
            "Lingering in the embrace you explore every inch of her beautiful form with your hands."
            "Her soft skin feels like silk beneath your fingertips, and the gentle curves of her hips and thighs are a enough to stir your recently spent cock."
            "She moans softly as you nibble on her earlobe, sending shivers down her spine."
            "Your fingers trace circles on her stomach before moving lower, caressing the smooth skin of her inner thighs."
            "She arches her back slightly, inviting you closer as she parts her legs for you."
            "The moment you touch her wetness, she gasps, her eyes fluttering shut at the sensation."
            "You tease her gently at first, circling your finger around her swollen clit before dipping it inside her tight warmth."
            "Her hips buck off the bed in response, and she lets out a long, low moan that fills the room."
            "As you continue to pleasure her, with one hand you reach down to stroke yourself, guiding your member towards its target."
            "With one long smooth thrust, you push yourself inside her, filling her tight warmth with your hard length."
            "She cries out in pleasure, her eyes squeezed shut as she clings to you for support."
            # audio
            "You begin to move together, your hips meeting in a rhythmic dance that sends waves of pleasure coursing through both of your bodies."
            "The sound of skin slapping against skin fills the room as you pick up speed, driving each other towards climax."
            "With every thrust, [the_person.title]'s moans grow louder, and her nails dig into your shoulders as she tries to maintain control."
            "You can feel her walls start to pulse around your cock, signaling that she's close. You quicken your pace, determined to send her over the edge."
            "Finally, [the_person.title]'s body tenses, and she lets out a long, piercing scream."
            "Her inner muscles convulse around you, triggering your own orgasm and milking every last drop of your cum from your aching shaft."
            # cum in vagina
            "As you both come crashing down from the heights of ecstasy, you collapse onto the bed next to her, exhausted but satisfied."
            "As the two of you catch your breath, [the_person.title] turns to face you and smiles."
            the_person "That was amazing!"
            "She leans in and kisses you gently on the lips."
            # towel/robe
            $ scene_manager.show_actor(the_sister)
            "A moment later [the_sister.title] returns from the bathroom, a satisfied smile on her face as she surveys the scene before her."
            "She crawls onto the bed beside you, her fingers running through [the_person.title]'s hair as she plants a kiss on her lips."
            the_sister "How was cuddling?"
            the_person "Incredible... I wish I could stay in bed with the two of you all day."
            "Looking between [the_sister.possessive_title], who you fucked last night, and her girlfriend who is still dripping your cum you have to agree."
            mc.name "I can't think of a better way to spend a day, but unfortunately real life calls."
            the_person "Yeah, I guess it does. Can I use your shower too?"
            the_sister "Of course, I'll see if I can find some clothes that will fit you."
            "Although they don't rush out of the room, both girls eventually depart, leaving you to start your day."
    $ scene_manager.clear_scene
    return

label first_threesome_label(the_sister, the_person): #18
    $ scene_manager = Scene()
    # TODO make slutty schoolgirl outfits
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_sister, sluttiness_modifier = 100).get_copy()
    if temp_outfit.get_bra():
        $ temp_outfit.remove_clothing(temp_outfit.get_bra())
    if temp_outfit.get_panties():
        $ temp_outfit.remove_clothing(temp_outfit.get_panties())
    $ scene_manager.add_actor(the_sister, visible = False)
    $ scene_manager.apply_outfit(the_sister, temp_outfit)
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person, sluttiness_modifier = 100).get_copy()
    if temp_outfit.get_bra():
        $ temp_outfit.remove_clothing(temp_outfit.get_bra())
    if temp_outfit.get_panties():
        $ temp_outfit.remove_clothing(temp_outfit.get_panties())
    $ scene_manager.add_actor(the_person, visible = False)
    $ scene_manager.apply_outfit(the_person, temp_outfit)
    $ scene_manager.show_actor(the_sister, emotion = "happy")
    $ scene_manager.show_actor(the_person, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    "INCOMPLETE LABEL" #TODO
    "As you lay sprawled across your bed, waiting for [the_sister.title] and [the_person.title] to arrive, your mind races with thoughts of what they might have planned to express their gratitude."
    "The door opens softly, and there they stand - [the_sister.fname], [the_sister.possessive_title], and her girlfriend [the_person.fname]."
    "As you sit up you look at their eyes, which are filled with desire and anticipation."
    the_sister "[mc.name], we wanted to thank you properly for all your help. We think the best way to do that is to offer ourselves to you."
    "[the_person.title] steps forward, her hand trailing along [the_sister.title]'s arm."
    the_person "You've been so focused on putting our needs first, we want to return the favor."
    "They strut forward, their exaggerated stride drawing your attention to their hips."
    the_sister "So tonight is all about you. You can have both of us any way you want."
    if the_sister.has_taboo("blowjob"):
        mc.name "You've been so careful not to cross any lines with me. Are you sure?"
        the_sister "Yes, tonight anything goes."
    elif the_sister.has_taboo("anal_sex"):
        mc.name "Does that mean I can fuck you?"
        the_sister "Yes, you can fuck my ass... or even my pussy if you want."
    elif the_sister.has_taboo("vaginal_sex"):
        mc.name "You've always drawn a line at your pussy, is it open for me tonight?"
        the_sister "Yes, any hole you want, I'm just your cocksleeve tonight."
    elif the_sister.has_taboo("condomless_sex"):
        mc.name "I've already had all of your holes, does this mean I can enter you bare now?"
        the_sister "Tonight you can. Fuck me raw like you've always wanted."
    mc.name "And what about you [the_person.fname]?"
    if the_person.has_taboo("sucking_cock"):
        the_person "Yep, I'll suck your cock and you can put it anywhere you want."
    elif the_person.has_taboo("vaginal_sex"):
        the_person "Yep, you can have my pussy... or even my ass if you want."
    elif the_person.has_taboo("anal_sex"):
        the_person "Yep, you can even fuck me up the ass if you want."
    elif the_person.has_taboo("condomless_sex"):
        the_person "Yep, you don't even need protection if you want to pump your cum deep into me."
    mc.name "Have I told the two of you how much I love you?"
    the_sister "We know."
    the_person "So where do you want to start?"
    mc.name "First things first, you are both wearing far too many clothes."
    $ scene_manager.strip_to_tits(the_sister)
    $ scene_manager.strip_to_tits(the_person)
    "They both quickly pull their tops over their heads, revealing that they were braless."
    $ the_person.update_outfit_taboos()
    $ the_sister.update_outfit_taboos()
    the_sister "We already took off our underwear to make this easier, do you want us to take off our skirts or shoes?"
    menu:
        "Remove everything":
            mc.name "Take it all off, I want to be able to properly appreciate your bodies."
            $ scene_manager.strip_full_outfit(the_person)
            $ scene_manager.strip_full_outfit(the_sister)
        "Remove skirts":
            mc.name "Drop those skirts, I don't want anything in the way of your holes."
            $ scene_manager.strip_to_vagina()
        "Remove shoes":
            $ the_person.outfit.remove_random_feet(top_layer_first = True)
            $ the_sister.outfit.remove_random_feet(top_layer_first = True)
        "Remove nothing":
            mc.name "I actually kind of like you like this. Sometimes being partially dressed is sexier than being nude."
    $ scene_manager.update_scene()
    $ the_person.update_outfit_taboos()
    $ the_sister.update_outfit_taboos()
    "You take a moment to drink in the sight of their nubile bodies, ready and waiting for anything you have in mind."
    mc.name "Now on your knees, crawl over here and help me with my pants."
    $ scene_manager.update_actor(the_sister, position = "kneeling1")
    $ scene_manager.update_actor(the_person, position = "kneeling1")
    "They drop to the floor, slowly making their way towards you while looking up reverantly."
    "Their hands move to your belt, working together to free your straining erection from its confines."
    if the_sister.has_taboo("sucking_cock"):
        $ the_sister.call_dialogue("sucking_cock_taboo_break")
        $ the_sister.break_taboo("sucking_cock")
    $ scene_manager.update_actor(the_sister, position = "blowjob")
    "[the_sister.title] takes the lead, wrapping her soft lips around the head of your cock as [the_person.title] positions herself between your legs."
    if the_person.has_taboo("sucking_cock"):
        $ the_person.call_dialogue("sucking_cock_taboo_break")
        $ the_person.break_taboo("sucking_cock")
    "The sight of [the_sister.possessive_title] going down on you while her girlfriend teases your balls with her tongue sends a jolt of pleasure through your body."
    mc.name "Ahhh, that's it, keep going."
    "You tangle your fingers in [the_sister.title]'s hair as she begins to bob her head, taking you deeper with each pass."
    "Meanwhile, [the_person.title]'s warm breath washes over your sack as she lavishes attention on it, her moans vibrating against your skin."
    mc.name "Fuck, you two look so hot like this, submitting to my commands and happy to serve."
    "[the_sister.title] slurps and gags around your shaft, the wet sounds filling the room as she works to take you all the way in."
    if the_sister.get_opinion_score("sucking cock") > 0:
        the_sister "Mmph, cawk is sooo good!"
    "[the_person.title], meanwhile, sucks harder on your balls, rolling them expertly in her mouth. The sensation is almost too much to bear."
    mc.name "Keep going, make me cum in your mouths."
    "[the_sister.title]'s throat muscles flex around your head as she works to take you deeper, her nose brushing against your pubes."
    "You thrust gently, helping [the_sister.title] take you deeper while not moving to far from [the_person.title]'s attention."
    "[the_sister.title]'s mouth continues to work its magic, her throat contracting and releasing in a rhythm that mimics the pounding of your heart."
    "The dual sensations from the girls, and their wilingness to do anything, quickly have you on the brink."
    $ climax_controller = ClimaxController(["Cum on her tits", "tits"],["Cum on her face", "face"],["Cum in her mouth", "mouth"],["Cum down her throat", "throat"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_sister)
        $ the_sister.cum_on_face()
        $ scene_manager.update_scene()
        "You pull out of [the_sister.possessive_title]'s mouth just in time to spray your first blast on her face."
        "[the_person.title] is quick to move up and you pivot to ensure she gets some too."
        $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
        $ the_person.cum_on_face()
        $ scene_manager.update_scene()
        "When your last spurt is done they lean in to share a sloppy kiss, licking at each other's faces to capture your cum."
    elif the_choice == "Cum in her mouth":
        mc.name "Fuck, I'm about to cum! I'm going to fill that cute mouth of yours up!"
        "You keep your hand on the back of [the_sister.title]'s head to make it clear you want her to keep sucking."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_sister)
        $ the_sister.cum_in_mouth()
        $ scene_manager.update_scene()
        "As you unload into [the_sister.possessive_title] you see her cheeks bulge, and a bit dribbles from the corner of her mouth."
        "As you pull out, [the_person.title] is quick to move in and lick the cum from her girlfriend's chin."
        $ the_person.cum_in_mouth()
        $ scene_manager.update_scene()
    elif the_choice == "Cum down her throat":
        mc.name "Fuck, here I come!"
        "You thrust forward, ensuring that you are buried deep in her throat as you begin to unload."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", person = the_sister)
        $ the_sister.cum_in_mouth()
        $ scene_manager.update_scene()
        "She takes most of it like a champ, but you pull out when she starts to cough. The last blast paints her face."
        "[the_person.title] is quick to move up to [the_sister.title] and hungrily licks up what she can."
    elif the_choice == "Cum on her tits":
        mc.name "Fuck, here I come!"
        "You push [the_sister.possessive_title] back slightly as you pull out, aiming down towards her [the_sister.tits_description]."
        $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_sister)
        $ the_sister.cum_on_tits()
        $ scene_manager.update_scene()
        "[the_person.title] raises up to join her and you shift to ensure she gets a generous blast of your cum too."
        $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_person)
        $ the_person.cum_on_tits()
        $ scene_manager.update_scene()
        "When you finish they look at each other, and it isn't long before [the_sister.title] leans down to lick at [the_person.title]'s [the_person.tits_description]."
        "They take turns, combining their clean up with nibbling and teasing one another's cum covered tits."
    $ scene_manager.update_actor(the_sister, position = "kneeling1")
    "Watching the girls play with each other while covered in your cum keeps your erection from fading too much."
    "Once they've gotten each other relatively clean they turn towards you with a questioning look."
    the_sister "What's next [the_sister.mc_title]?"
    the_person "Yeah, [the_person.mc_title], who do you want to fuck first?"
    $ choice = "pussy"
    while choice:
        menu:
            "Fuck [the_sister.title]'s pussy":
                $ person_one = the_sister
                $ person_two = the_person
            "Fuck [the_sister.title]'s ass":
                $ person_one = the_sister
                $ person_two = the_person
                $ choice = "ass"
            "Fuck [the_person.title]'s pussy":
                $ person_one = the_person
                $ person_two = the_sister
            "Fuck [the_person.title]'s ass":
                $ person_one = the_person
                $ person_two = the_sister
                $ choice = "ass"
            "Stop":
                $ choice = False
        if choice == "pussy":
            person_one "lay down and get comfortable, [person_one.mc_title]."
            $ scene_manager.update_actor(person_one, position = "cowgirl")
            "[person_one.title] grins, crawling onto the bed and straddling your waist. Her [person_one.hair_colour[0]!l] frames her face as she leans down, capturing your lips in a passionate kiss."
            $ scene_manager.update_actor(person_two, position = "kneeling1")
            "Meanwhile, [person_two.title] positions herself beside the bed, her [person_two.hair_colour[0]!l] locks cascading down her back as she runs a teasing finger along your chest."
            person_two "We're going to give you a night you'll never forget,"
            "With that, [person_one.title] brakes the kiss and shifts her weight, guiding your rigid cock to rest against her slick entrance."
            if person_one.has_taboo("vaginal_sex"):
                person_one "I can't believe we're really doing this. Be gentle with me [person_one.mc_title]."
                "She looks into your eyes, her gaze apprehensive but with hints of arousal, before slowly sinking down to envolop your head."
                person_one "Ahh, fuck, it's so big."
                "You respond with a groan, your hips instinctively thrusting up for more as [person_one.title] pauses."
                "She raises herself up a bit, letting out a noise somewhere between pain and pleasure, but not pulling off entirely."
                person_two "You've got this [person_one.fname], just relax."
                "After taking a deep breath, [person_one.possessive_title] begins to lower herself more, her tight little pussy swallowing you inch by inch."
                #virgin?
                $ person_one.call_dialogue("vaginal_sex_taboo_break")
                $ person_one.break_taboo("vaginal_sex")
                "Once she is fully seated on you, she pauses to collect herself before going any further."
            else:
                "She looks into your eyes, her gaze smoldering with arousal, before slowly sinking down onto your throbbing length."
                person_one "Ahh, fuck yeah."
                "You respond with a groan, your hands instinctively gripping [person_one.title]'s hips as she envelops you fully."
            $ scene_manager.update_actor(person_two, position = "cowgirl")
            "[person_two.title] climbs onto the bed, positioning herself behind [person_one.title], her [person_two.tits_description] pressing against her girlfriend's back as she nuzzles into the crook of her neck."
            person_two "You look so beautiful like this, riding [person_two.mc_title] like a slut." 
            "[person_one.title] rocks her hips, setting a languid rhythm that has your cock twitching inside her."
            person_one "Mmm, he feels amazing."
            "[person_one.title]'s nails dig lightly into your thighs as she moves herself slowly up and down."
            "[person_two.title] trails her fingers down [person_one.title]'s stomach, dipping them tantalizingly close to where you are entering her."
            "[person_one.title] gasps, her inner walls clenching around you in response to the added stimulation."
            mc.name "Fuck, your pussy is so tight!" 
            "[person_two.title] continues her teasing touch, occasionally brushing against [person_one.title]'s clit, sending jolts of pleasure through her."
            "[person_one.title] whimpers, her movements becoming more urgent as she chases her impending climax."
            "You match her fervor, thrusting up to meet each downward plunge of her hips."
            "The room fills with the lewd sounds of flesh slapping against flesh and ragged breathing."
            "[person_two.title] leans in, her lips brushing [person_one.title]'s ear as she murmurs."
            person_two "Cum for me, [person_one.fname]. Let go and cum all over [person_two.mc_title]'s big cock."
            "[person_one.title]'s body tenses, her inner muscles rippling around you as she teeters on the brink."
            $ person_one.have_orgasm()
            "With a keening cry, she comes undone, her orgasm crashing over her in waves of intense bliss."
            mc.name "Yesss, just like that."
            "As [person_one.title]'s contractions milk your cock, you feel the pressure become unbearable."
            "With a guttural roar, you explode inside her, your hot seed pumping deep into her core."
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = person_one)
            $ person_one.cum_in_vagina()
            $ scene_manager.update_scene()
            "[person_two.title] licks a path up [person_one.title]'s neck, pausing to nibble at her earlobe."
            person_two "Did you feel that, [person_one.fname]? [person_two.mc_title]'s cumming so hard inside you."
            "[person_one.title]'s eyes flutter closed, a satisfied sigh escaping her lips as she savors the feeling of your warmth flooding her insides."
            "Finally, your climax subsides, leaving you panting and spent."
            $ scene_manager.update_actor(person_one, position = "stand2")
            "[person_one.title] collapses onto your chest, her hair a wild tangle around her flushed face."
            $ scene_manager.update_actor(person_two, position = "stand3")
            "[person_two.title] crawls up to join you, snuggling against [person_one.title]'s side as you both bask in the afterglow of your shared climax."
            mc.name "Well?" 
            person_one "That was incredible, [person_one.mc_title]."
        else:
            mc.name "[person_one.title] bend over the bed for me while [person_two.title] spreads your cheeks for me."
            $ scene_manager.update_actor(person_one, position = "doggy")
            $ scene_manager.update_actor(person_two, position = "standing_doggy")
            "As the girls get into position you grab a bottle of lube from your nightstand and spread a liberal amount on your cock."
            if person_one.has_taboo("anal_sex"):
                $ person_one.call_dialogue("anal_sex_taboo_break")
                $ person_one.break_taboo("anal_sex")
                "FIRST TIME INTRO"
            else:
                person_one "I'm ready, just take it slow for me [person_one.mc_title]."
                "INTRO"
            "ANAL SEX WITH [person_one.title] WHILE [person_two.title] DOES SOMETHING."
            $ person_one.have_orgasm()
            $ ClimaxController.manual_clarity_release(climax_type = "ass", person = person_one)
            $ person_one.cum_in_ass()
            $ scene_manager.update_scene()
            "CONCLUSION"
        person_two "Can we do another round?"    
    mc.name "As much as I'd like to, I don't think I have another round in me. You girls have drained me dry."
    "Judging by the tired grins you get in return they don't have much energy left either."
    $ scene_manager.update_actor(person_one, position = "kissing", special_modifier = "kissing")
    $ scene_manager.update_actor(person_two, position = "kissing", special_modifier = "kissing")
    "Standing side by side, they pull you in for an alternating kiss."
    "It lingers for a bit, but none of you have the strength to take it further, and they pull back eventually."
    person_one "Thanks for tonight [person_one.mc_title] it was really special."
    person_two "Yeah, we wanted to reward you and you still made sure we had a good time too."
    mc.name "Trust me, it was my pleasure. Anytime you want a repeat performance just let me know."
    person_two "We'll definately let you know [person_two.mc_title]."
    "They bend to collect their clothes before walking to the door and looking out into the hallway."
    "Seeing that the coast is clear they make their way to the bathroom."
    "Any other time you'd be tempted to join them, but as you sink onto your bed you only want to go to sleep."
    $ scene_manager.clear_scene
    return

label repeat_threesome_label(the_sister, the_person):
    $ scene_manager = Scene()
    # TODO make slutty schoolgirl outfits
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_sister, sluttiness_modifier = 100).get_copy()
    if temp_outfit.get_bra():
        $ temp_outfit.remove_clothing(temp_outfit.get_bra())
    if temp_outfit.get_panties():
        $ temp_outfit.remove_clothing(temp_outfit.get_panties())
    $ scene_manager.add_actor(the_sister, visible = False)
    $ scene_manager.apply_outfit(the_sister, temp_outfit)
    $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person, sluttiness_modifier = 100).get_copy()
    if temp_outfit.get_bra():
        $ temp_outfit.remove_clothing(temp_outfit.get_bra())
    if temp_outfit.get_panties():
        $ temp_outfit.remove_clothing(temp_outfit.get_panties())
    $ scene_manager.add_actor(the_person, visible = False)
    $ scene_manager.apply_outfit(the_person, temp_outfit)
    $ scene_manager.show_actor(the_sister, emotion = "happy")
    $ mc.change_location(lily_bedroom)
    $ scene_manager.show_actor(the_person, emotion = "happy", display_transform = character_left_flipped(xoffset = .3))
    $ scene_manager.strip_full_outfit(the_person)
    $ scene_manager.strip_full_outfit(the_sister)
    call start_threesome(the_sister, the_person) from _call_start_threesome_bf7
    $ scene_manager.clear_scene
    return
