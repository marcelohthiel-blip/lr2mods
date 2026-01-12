### PERSONALITY CHARACTERISTICS ###

### DIALOGUE ###
################################
##### Reserved Personality #####
################################

label reserved_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around and looks at you quizzically."
    the_person "I suppose you could. How can I help you?"
    mc.name "I'm so sorry, I know this is silly but I just couldn't let you walk by without knowing your name."
    "She laughs and rolls her eyes."
    $ the_person.set_title()
    $ the_person.set_possessive_title()
    the_person "Well then, I suppose I shouldn't disappoint you. You can call me [the_person.title]."
    "[the_person.possessive_title!c] holds her hand out to shake yours."
    the_person "What about you, what's your name?"
    return

label reserved_greetings(the_person):
    if the_person.love < 0:
        the_person "... Do you need something?"
    elif the_person.happiness < 90:
        the_person "Hello..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title]."
            else:
                the_person "Hello, are you feeling as good as you're looking today?"
        else:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title]."
            else:
                the_person "Hello, I hope you're doing well."
    return

label reserved_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] moans softly, then stops herself and laughs."
            the_person "Oh lord, I sound like a horny schoolgirl!"
        else:
            "[the_person.possessive_title!c] keeps her composure, giving you little feedback to work with."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know just what I like, don't you?"
        else:
            the_person "Oh my... that feels very good, [the_person.mc_title]!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person "Keep doing that [the_person.mc_title]... Wow, you're good!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Oh gods above that feels amazing!"
        else:
            the_person "Oh lord... I could get used to you touching me like this!"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Touch me [the_person.mc_title], I want you to touch me!"
            else:
                the_person "I should feel bad... but my [the_person.so_title] never touches me this way!"
                the_person "I need this, so badly!"
        else:
            the_person "I want you to keep touching me. I never thought you could make me feel this way, but I want more of it!"

    return

label reserved_sex_responses_oral(the_person):
    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Oh.... Oh! Mmm, I could get used to this!"
            "She laughs happily as you eat her out."
        else:
            "[the_person.possessive_title!c] twitches and squirms."
            the_person "Sorry, I'm just so sensitive down there... Keep going, it's a good feeling."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title], you're so good to me."
        else:
            the_person "Oh my... that feels..."
            "She sighs happily."
            the_person "So good!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Yes, just like that! Mmm!"
        else:
            the_person "Keep doing that [the_person.mc_title], it's making me feel... very aroused."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you really know how to put that tongue of yours to good use. That feels amazing!"
        else:
            the_person "Oh lord... your tongue is addictive, I just want more of it!"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Oh I need this so badly [the_person.mc_title]! If you keep going you'll make me climax!"
            else:
                the_person "I should feel bad, but you make me feel so good and my [the_person.so_title] never does this for me!"
        else:
            the_person "Oh sweet lord in heaven... This feeling is intoxicating!"

    return

label reserved_sex_responses_vaginal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_vaginal(the_person) from _call_low_energy_sex_responses_vaginal_9
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            the_person "Fuck me slowly, I want to feel every inch when it slides inside..."
        else:
            the_person "Take me slowly [the_person.mc_title], make the moment last."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, I love feeling you inside me!"
        else:
            the_person "Oh lord, you're so big... Whew!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person "Oh that feels very good, keep doing that!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Yes! Oh god yes, fuck me!"
        else:
            the_person "Oh lord your... cock feels so big!"

    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:

                the_person "Keep... keep going [the_person.mc_title]! I'm going to climax soon!"
            else:
                the_person "Keep going! My [the_person.so_title]'s tiny dick never makes me climax and I want it so badly!"
                the_person "I should feel bad, but all I want is your cock in me right now!"
        else:
            "[the_person.title]'s face is flush as she pants and gasps."
    return

label reserved_sex_responses_anal(the_person):
    if the_person.energy < 10:
        call low_energy_sex_responses_anal(the_person) from _call_low_energy_sex_responses_anal_9
        return

    if the_person.arousal_perc < 45:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title!c] grunts and squirms, but doesn't put up any complaints."
        else:
            the_person "Oh lord, give me strength..."
            "She grunts and squirms as you stretch her ass out."

    elif the_person.arousal_perc < 60:
        if the_person.sluttiness > 50:
            the_person "Mmm, you feel so big when you're inside me like this."
        else:
            the_person "Be gentle, it feels like you're going to tear me in half!"

    elif the_person.arousal_perc < 75:
        if the_person.sluttiness > 50:
            the_person "Give it to me, [the_person.mc_title], give me every last inch!"
        else:
            the_person "Oh god! Oww!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "I hope my ass isn't too tight for you, I don't want you to cum early."
        else:
            the_person "I don't think I will be able to walk straight after this!"
    else:
        if the_person.sluttiness > 50:
            if not the_person.has_significant_other:
                the_person "Your cock feels so good, stuffed deep inside me! Keep going, I might actually climax!"
            else:
                the_person "My [the_person.so_title] always wanted to try anal, but I told him it would never happen. My ass belongs to you, [the_person.mc_title]!"
        else:
            the_person "Oh lord, this is actually starting to feel good... I might be able to climax after all!"

    return

label reserved_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh my... I'm going to... cum!"
    else:
        the_person "I... Oh my god, this feeling is..."
        "She pauses and moans excitedly."
        the_person "So good!"
    return

label reserved_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Keep going [the_person.mc_title], you're going to make me..."
        "She barely finishes her sentence as her body shivers with pleasure."
        the_person "... Orgasm!"
    else:
        the_person "This feeling... Oh... Oh!"
        "Her eyes close and she takes a deep breath."
    return

label reserved_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Yes [the_person.mc_title], keep going... just like that!"
            "She squeals as her orgasm hits her."
        elif the_person.is_submissive:
            the_person "Yes [the_person.mc_title], pound my pussy hard! Yes, just like that!"
            "She squeals as her orgasm hits her."
        else:
            the_person "You're going to... Ah! You're going to make me climax [the_person.mc_title]!"
            "She closes her eyes as she tenses up. She freezes for a long second, then lets out a long, slow breath."
    else:
        the_person "Oh, I think I'm about to... Oh yes!"
    return

label reserved_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        if the_person.arousal_perc > 120:
            the_person "Oh god, keep going [the_person.mc_title], keep shoving that big cock in my ass!"
        elif the_person.is_submissive:
            the_person "Oh god, keep going [the_person.mc_title], punish my ass with your big cock!"
        else:
            the_person "Mmmm, fuck me [the_person.mc_title], fuck my ass and make me cum!"
    else:
        the_person "Oh lord, I think I'm going to climax. You're going to make me cum by fucking my ass!"
    return

label reserved_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "You're too kind [the_person.mc_title]. I'll add it to my wardrobe right away."
    else:
        the_person "For me? Oh, I'm not used to getting gifts like this..."
    return

label reserved_clothing_reject(the_person):
    if the_person.obedience > 180:
        the_person "You're too kind [the_person.mc_title], really. I don't think I can accept such a... beautiful gift from you though."
    else:
        if the_person.sluttiness > 60:
            the_person "It's very nice [the_person.mc_title], but I think it's a little too revealing, even for me. Maybe when I'm feeling a little more bold, okay?"
        else:
            the_person "Really [the_person.mc_title]? Just suggesting that I would wear something like that is a little too forward, don't you think?"
    return

label reserved_clothing_review(the_person):
    if the_person.outfit.cum_covered:
        if (the_person.sluttiness > 40 and the_person.opinion.being_covered_in_cum >=0) or the_person.opinion.being_covered_in_cum > 0:
            the_person "I suppose I should wipe this up..."
            "[the_person.title] quickly wipes away the most obvious splashes of cum on her body."
        else:
            "[the_person.title] starts to wipe up all the cum on her, moving slowly and carefully to avoid missing any."

    if the_person.should_wear_uniform:
        the_person "One moment [the_person.mc_title], I need to get my uniform sorted out."
    elif the_person.obedience > 180:
        the_person "I'm such a mess right now [the_person.mc_title], I just have to go and get tidied up for you. I'll be back in a moment."
    else:
        if the_person.sluttiness > 40:
            the_person "Oh dear, my clothes are just a mess after all of that. Not that I'm complaining, of course, but I should go get tidied up. Back in a moment."
        else:
            the_person "Oh, I look like such a mess right now. I'll be back in a moment."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label reserved_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "I'm sorry [the_person.mc_title], but I think my [the_clothing.display_name] should stay where it is for now. For modesty's sake."
    elif the_person.obedience < 70:
        the_person "That's going to stay right there for now. I'll decide when I want it to come off, okay?"
    else:
        the_person "[the_person.mc_title], I don't feel comfortable taking that off. Just leave it put."
    return

label reserved_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] speaks quietly as you start to move her [the_clothing.display_name]."
    if the_person.obedience > 180:
        the_person "I... I'm sorry, but I don't know if you should take that off [the_person.mc_title]..."
    else:
        the_person "I really shouldn't take that off [the_person.mc_title]..."
    return

label reserved_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        "She shoots you a cold look and steps back, away from your touch."
        the_person "I'm sorry, I'd prefer if you didn't touch me without permission."
        mc.name "Of course, I was just trying to be friendly."
        the_person "I understand, it just makes me... Uncomfortable."
        "She seems more guarded, but you both try and move past the awkward moment."
    else: #Fail point for touching waist
        "[the_person.title] shifts and tries to move away from you."
        the_person "Sorry, but could you... Move your hand? I'm just not comfortable with this."
        "You take a step back and pull your hand away."
        mc.name "Of course, no problem. Just trying to be friendly."
        "She seems unconvinced, but decides not to say anything else."
    return

label reserved_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Good, I didn't want to be the one to suggest it but that sounds like fun."
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Mmm, you think we should give that a try? I'm feeling adventurous today—let's go."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    the_person "I like that idea, get down there and show me what you can do."
                else:
                    the_person "Okay, I don't mind sucking it for a while."
            else:
                the_person "I think I want you to shove that throbbing monster into me."
    else:
        the_person "Oh, I know I shouldn't [the_person.mc_title]... but I think you've managed to convince me."
    return

label reserved_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "I shouldn't... I really shouldn't. But I know you want me, and I think I want you too. Promise you'll make me feel good too?"
    else:
        if the_person.obedience > 180:
            the_person "Okay [the_person.mc_title], if that's what you want. I'll do what I can to serve you."
        else:
            the_person "If it were anyone other than you I'd say no [the_person.mc_title]. Don't get too used to this, okay?"
    return

label reserved_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Wait, a lady must be romanced first [the_person.mc_title]. At least get me warmed up first."
    else:
        the_person "This doesn't seem like the kind of thing a proper lady would do. Let's do something else, please."
    return

label reserved_sex_angry_reject(the_person):
    if the_person.has_significant_other:
        the_person "Excuse me? I have a wonderful [the_person.so_title] and I would never dream of doing anything to betray him!"
        "She glares at you and shakes her head."
        the_person "I need some space, [the_person.mc_title]. I didn't think you were that kind of man."
    elif the_person.sluttiness < 20:
        the_person "Excuse me? Do I look like some sort of prostitute?"
        the_person "Get away from me, you're lucky I don't turn you into the police for that! Give me some space, I don't want to talk after that."
    else:
        the_person "Um, what do you think you're doing [the_person.mc_title]? That's disgusting, and certainly no way to act around a lady!"
    return

label reserved_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Hello [the_person.mc_title], is there something I can help you with? Something of a personal nature perhaps?"
        else:
            the_person "Hello [the_person.mc_title], is there something I can help you with?"
    else:
        if the_person.sluttiness > 50:
            the_person "You've got that look in your eye again. There's just no satisfying you, is there? You're lucky I'm such a willing participant."
        elif the_person.sluttiness > 10:
            the_person "Oh [the_person.mc_title], you always know how to make a woman feel wanted..."
        else:
            the_person "[the_person.mc_title], isn't that a little bit forward of you? I'm not saying no though..."
    return

label reserved_seduction_accept_crowded(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "I don't think anyone will miss us for a few minutes. We can... get closer and see where things go."
        elif the_person.sluttiness < 50:
            the_person "Come on, let's go find someplace quiet then."
        else:
            the_person "Well then, do you want to take me right here or should we get a room?"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Well you have my attention. We should find some place private, unless you want my [the_person.so_title] to hear about us."
        else:
            the_person "I know I shouldn't... We need to keep it quiet, so my [the_person.so_title] doesn't find out."
    return

label reserved_seduction_accept_alone(the_person):
    if not the_person.has_significant_other:
        if the_person.sluttiness < 20:
            the_person "How about we start with a little kissing and just see where it goes."
        elif the_person.sluttiness < 50:
            the_person "Oh [the_person.mc_title], you're going to make me blush! Come over here!"
        else:
            the_person "Mmm, that sounds so nice [the_person.mc_title]. Don't make me wait, get over here!"
    else:
        if the_person.sluttiness + (5*the_person.opinion.cheating_on_men) > 50:
            the_person "Come here [the_person.mc_title], I want you to touch me in ways my [the_person.so_title] never does!"
        else:
            the_person "This is so improper."
            "She locks eyes with you, deadly serious."
            the_person "You can never tell my [the_person.so_title] about this, is that understood?"
            "You nod and she melts into your arms."
    return

label reserved_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Oh... I'm sorry [the_person.mc_title] but I couldn't imagine doing anything like that."

    elif the_person.sluttiness < 50:
        the_person "I'm sorry, but I'm just not in the mood for any fooling around right now. Maybe some other time though."

    else:
        the_person "Oh [the_person.mc_title], that sounds like a lot of fun, but I think we should save it for another time."
    return

label reserved_compliment_response(the_person):
    mc.name "Hello [the_person.fname]. How are you doing today? You're looking amazing, that's for sure."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call reserved_flirt_response_employee_uniform_low(the_person) from _call_reserved_flirt_response_employee_uniform_low_compliment_response
        elif the_person.is_at_job(prostitute_job):
            the_person "I'm good [the_person.mc_title], are you looking for something special today?"
        elif the_person.sluttiness > 50:
            the_person "I'm doing alright. And I must say, you look quite handsome yourself."
        else:
            the_person "Please [the_person.mc_title], behave yourself. I'm doing fine."
    else:
        the_person "Well, thank you, [the_person.mc_title]. I'm doing quite alright."
    "You chat with [the_person.possessive_title] for a while carefully slipping in a compliment once in a while. She seems charmed by all the attention."
    return

label reserved_compliment_response_girlfriend(the_person):
    mc.name "Hello [the_person.title]. You're looking very sensual this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call reserved_flirt_response_employee_uniform_mid(the_person) from _call_reserved_flirt_response_employee_uniform_mid_compliment_response_girlfriend
            $ the_person.call_dialogue("flirt_response_employee_uniform_mid")
        elif the_person.sluttiness > 50:
            the_person "Well, thank you, [the_person.mc_title]. If you play your cards right, I might show you how sexy I am..."
        else:
            the_person "Indeed, I do like this outfit! Perhaps we could go shopping sometime to expand my wardrobe."
    else:
        the_person "Well, thank you, this outfit does accentuate my looks. We could go on a date sometime and have some fun."
    "You chat with [the_person.possessive_title] for a while, making subtle remarks where you can. She is quite charmed by your efforts."
    return

label reserved_compliment_response_affair(the_person):
    mc.name "Hello [the_person.title]. You're looking absolutely stunning this [StringInfo.time_of_day_string]."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call reserved_flirt_response_employee_uniform_mid(the_person) from _call_reserved_flirt_response_employee_uniform_mid_compliment_response_affair
        elif the_person.sluttiness > 50:
            the_person "Well, thank you [the_person.mc_title], perhaps you could show me just how stunning I am, when we are alone..."
        else:
            the_person "Lower your voice, [the_person.mc_title]!...So you like my outfit? If you can convince me, I will show you what I'm wearing underneath..."
    else:
        the_person "It's a great ensamble isn't it? If you buy me a nice dinner, I might let you see what's underneath..."
    "You keep chatting with [the_person.possessive_title] for a while, slipping in as many subtle compliments as possible. She is quite flattered by your attentiveness."
    return

label reserved_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "It would be so improper, but for you I'm sure I could arrange something special."
        else:
            the_person "Thank you for the compliment, [the_person.mc_title], I appreciate it."

    elif the_person.has_significant_other:
        if the_person.sluttiness + (the_person.opinion.cheating_on_men*5) > 50:
            the_person "I'm glad you appreciate it. My [the_person.so_title] hardly even looks at me any more."
            "She spins, giving you a full look at her body."
            the_person "His loss, right?"
        else:
            the_person "[the_person.mc_title], I should remind you I have a [the_person.so_title]. We can be friendly with each other, but that's where it should end."
            "She seems more worried about maintaining appearances than she was about actually flirting with you."
    else:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title], that's so naughty of you to even think about..."
            "[the_person.title] winks at you and spins, giving you a full look at her body."
            the_person "How will I ever get you to contain yourself?"
        else:
            the_person "Please [the_person.mc_title], a woman like me likes a little romance in her relationships. At least buy me dinner first."
    return

label reserved_flirt_response_employee_uniform_low(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "It's not much of an outfit at all though."
        mc.name "I know, but I had to make you understand you can't ignore company rules."
        mc.name "But you do look very attractive."
        $ mc.change_locked_clarity(5)
        "[the_person.possessive_title!c] smiles."
        the_person "Well, thank you. I appreciate the compliment."
    elif the_person.judge_outfit(the_person.outfit):
        # She's in uniform and likes how it looks.
        the_person "Thank you [the_person.mc_title]. I think these are nice uniforms as well."
        mc.name "It helps having such an attractive employee to wear it."
        $ mc.change_locked_clarity(5)
        "[the_person.possessive_title!c] smiles."
        the_person "Well, thank you. I appreciate the compliment."
    else:
        #She's in uniform, but she thinks it's a little too slutty.
        if the_person.vagina_visible:
            # Her pussy is on display.
            the_person "It's not much of an outfit at all though."
            the_person "I understand it's the company uniform, but it would be nice to have a little more coverage."
            mc.name "It will take some getting used to, but I think it would be a shame to cover up your wonderful figure."
            $ mc.change_locked_clarity(5)
            "[the_person.possessive_title!c] doesn't seem so sure, but she smiles and nods anyways."

        elif the_person.tits_visible:
            # Her tits are out
            if the_person.has_large_tits:
                the_person "Thank you, but I can tell this uniform was designed by a man."
                $ mc.change_locked_clarity(5)
                the_person "Larger chested women, like myself, appreciate a little more support in their outfits."
            else:
                the_person "Thank you, but I do hope you'll consider a uniform with a proper top in the future."
                $ mc.change_locked_clarity(5)
                the_person "It still doesn't feel natural having my... breasts so visible."
            mc.name "I understand it's a little uncomfortable, but I'm sure you'll get used to it."
            the_person "Yes, given enough time I'm sure I will."

        elif the_person.underwear_visible:
            # Her underwear is visible.
            the_person "Thank you. I always feel a touch self-conscious when I put it on. I wish it kept me a little more covered."
            mc.name "I know it can take some getting used to, but you look fantastic in it. You're a perfect fit for it."
            $ mc.change_locked_clarity(5)
            "[the_person.possessive_title!c] doesn't seem so sure, but she smiles and nods anyways."

        else:
            # It's just generally slutty.
            "[the_person.possessive_title!c] smiles warmly."
            the_person "Thank you, although I don't think I would ever wear this if it wasn't company policy."
            mc.name "Well you look fantastic in it either way. Maybe you should rethink your normal wardrobe."
            $ mc.change_locked_clarity(5)
            the_person "I'll think about it."
    return

label reserved_flirt_response_employee_uniform_mid(the_person):
    if the_person.is_wearing_forced_uniform:
        the_person "I do look good, wearing this, don't I?"
        mc.name "Yes, you do, and I don't mind looking."
        $ mc.change_locked_clarity(10)
        "She smiles and nods."
    elif the_person.judge_outfit(the_person.outfit):
        if the_person.tits_visible:
            the_person "What it shows off most are my breasts. I'm not complaining though. Between you and me, I kind of like it."
            $ mc.change_locked_clarity(10)
            "She winks and shakes her shoulders, jiggling her tits for you."
        else:
            the_person "With my body and your fashion taste, how could I look bad? These uniforms are very flattering."
            mc.name "It's easy to make a beautiful model look wonderful."
            $ mc.change_locked_clarity(10)
            if the_person.effective_sluttiness() > 20:
                $ the_person.draw_person(position = "back_peek")
                the_person "It makes my butt look pretty good too. I don't think that was an accident."
                "She gives her ass a little shake."
                mc.name "It would be a crime to not try and show your ass off."
                $ the_person.draw_person()
            "She smiles softly."
            the_person "You know just what to say to make a woman feel special."

    else:
        # the_person "I think it shows off a little too much!"
        if the_person.vagina_visible:
            the_person "What doesn't this outfit show off!"

        elif the_person.tits_visible:
            the_person "It certainly shows off my breasts!"

        else:
            the_person "And it shows off a {i}lot{/i} of my body!"

        the_person "I don't mind it so much if it's just me and you, but when there are other people around I wish it kept me a little more covered."
        mc.name "It may take some time to adjust, but with enough time you'll be perfectly comfortable in it."
        $ mc.change_locked_clarity(10)
        "She smiles and nods."
        the_person "You're right, of course. If you think it's the best option for the company I trust you."
    return

label reserved_flirt_response_low(the_person):
    "[the_person.possessive_title!c] seems caught off guard by the compliment."
    the_person "Oh, thank you! I'm not wearing anything special, it's just one of my normal outfits."
    mc.name "Well, you make it look good."
    $ mc.change_locked_clarity(5)
    "She smiles and laughs self-consciously."
    the_person "Oh stop."
    return

label reserved_flirt_response_low1(the_person):
    if the_person.has_significant_other:
        the_person "[the_person.mc_title], I should remind you I have a [the_person.so_title]. We can be friendly with each other, but that's where it should end."
        "She seems more worried about maintaining appearances than she was about actually flirting with you."
    else:
        the_person "Please [the_person.mc_title], a woman like me likes a little romance in her relationships. At least buy me dinner first."
    $ mc.change_locked_clarity(5)
    return

label reserved_flirt_response_low2(the_person):
    the_person "Thank you, it's about time you noticed."
    $ mc.change_locked_clarity(5)
    $ the_person.draw_person(position = "back_peek", emotion = "happy")
    "[the_person.possessive_title!c] turns to give you a good look of her and smiles at you."
    $ the_person.draw_person()
    return

label reserved_flirt_response_mid(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
        "[the_person.possessive_title!c] smiles, then glances around self-consciously."
        the_person "Keep your voice down [the_person.mc_title], there are other people around."
        mc.name "I'm sure they're all thinking the same thing."
        "She rolls her eyes and laughs softly."
        the_person "Maybe they are, but it's still embarrassing."
        $ mc.change_locked_clarity(10)
        the_person "You'll have better luck if you save your flattery for when we're alone."
        mc.name "I'll keep that in mind."

    else:
        "[the_person.possessive_title!c] gives a subtle smile and nods her head."
        the_person "Thank you [the_person.mc_title]. I'm glad you like it... And me."
        the_person "What do you think of it from the back? It's hard for me to get a good look."
        $ the_person.draw_person(position = "back_peek")
        $ mc.change_locked_clarity(10)
        "She turns and bends over a little bit, accentuating her butt."
        if not the_person.outfit.wearing_panties and not the_person.vagina_visible: #Not wearing underwear, but you can't see so she comments on it.
            the_person "My panties were always leaving unpleasant lines, so I had to stop wearing them. I hope you can't tell."
        else:
            the_person "Well?"
        mc.name "You look just as fantastic from the back as you do from the front."
        $ the_person.draw_person()
        "She turns back and smiles warmly."
    return

label reserved_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    if mc.location.person_count > 1:
        "[the_person.possessive_title!c] smiles, then glances around self-consciously."
        the_person "Keep it down, people might get the wrong impression."
    the_person "You are right, it does suit me very well."
    if (the_person.has_skirt or the_person.has_dress) and not the_person.has_thigh_high_socks:
        mc.name "I wouldn't mind if you added some sexy stockings next time."
        the_person "I bet you wouldn't."
    $ mc.change_locked_clarity(10)
    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other and not the_person.has_job(prostitute_job):
        the_person "We can't do that [the_person.mc_title], what if my [the_person.so_title] finds out?"
        mc.name "Come on, it's just a coffee, we are not going to a party."
        the_person "I guess so, you're right. I can have a coffee with anyone I want."
    else:
        the_person "Sure, why not?"
    return

label reserved_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.opinion.public_sex)): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "[the_person.mc_title], there are people around."
        "She bites her lip and leans close to you, whispering in your ear."
        $ mc.change_locked_clarity(15)
        the_person "But if we were alone, maybe we could figure something out..."
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Follow me."
                "[the_person.possessive_title!c] nods and follows a step behind you."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_reserved_flirt_response_high_2
                "Once you're alone you put one hand around her waist, pulling her close against you. She looks into your eyes."
                the_person "Well? What now?"

                if the_person.is_willing(kissing):
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You lean in and kiss her. She closes her eyes and leans her body against yours."
                    else:
                        "You answer with a kiss. She closes her eyes and leans her body against yours."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_51
                else:
                    if the_person.has_taboo("touching_body"):
                        $ the_person.call_dialogue("touching_body_taboo_break")
                        $ the_person.break_taboo("touching_body")
                        "You take her hand and pull her close against you. She looks into your eyes."
                    else:
                        "You answer by pulling her close against you."
                    call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_reserved_flirt_grope

                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_reserved_flirt_response_high_2

            "Just flirt":
                mc.name "I'll just have to figure out how to get you alone then. Any thoughts?"
                the_person "You're a smart man, you'll figure something out."
                "She leans away from you again and smiles mischievously."

    else:
        if mc.location.person_count == 1: #She's shy but you're alone
            "[the_person.title] blushes and stammers out a response."
            the_person "I... I don't know what you mean [the_person.mc_title]."
            mc.name "It's just the two of us, you don't need to hide how you feel. I feel the same way."
            "She nods and takes a deep breath, steadying herself."
            the_person "Okay. You're right. What... do you want to do then?"

        else:  #You're not alone, but she doesn't care.
            the_person "Well I wouldn't want you to go crazy. You'll just have to do something to get me out of this outfit then..."
            $ mc.change_locked_clarity(15)
            if the_person.has_large_tits: #Bounces her tits for you
                "[the_person.possessive_title!c] bites her lip sensually and grabs her boobs, jiggling them for you."

            else: #No big tits, so she can't bounce them (as much
                "[the_person.possessive_title!c] bites her lip sensually and looks you up and down, as if mentally undressing you."

            the_person "Well? What do you want to do?"

        menu:
            "Touch her" if not the_person.is_willing(kissing):
                "You step closer to [the_person.title] and move your hands down her waist."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")

                call fuck_person(the_person, start_position = standing_grope, private = False) from _call_fuck_person_flirt_response_reserved_touching

            "Kiss her" if the_person.is_willing(kissing):
                $ the_person.draw_person()
                "You step close to [the_person.title] and put an arm around her waist."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She presses her body up against yours."
                else:
                    "When you lean in and kiss her she responds by pressing her body tight against you."

                call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_reserved_flirt_response_high
                call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _call_fuck_person_52
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call mc_restore_original_location(the_person) from _call_mc_restore_original_location_reserved_flirt_response_high

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Nothing right now, but I've got a few ideas for later."
                "If [the_person.title] is disappointed she does a good job hiding it. She nods and smiles."
                the_person "Well maybe if you take me out for dinner we can talk about those ideas. I'm interested to hear about them."
    return

label reserved_flirt_response_low_energy(the_person):
    if the_person.sluttiness > 40:
        the_person "Mmhm thanks, I like your compliments, try again when I'm a little more rested."
    else:
        the_person "Thank you, but I'm too tired for this right now."
    return

label reserved_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.opinion.public_sex)):
            # Not very slutty, so she wants to find somewhere private
            "[the_person.title] smiles happily."
            the_person "Oh, well thank you [the_person.mc_title]. You're so sweet."
            "She leans in and gives you a quick peck on the cheek."
            the_person "I wish we had a little more privacy. Oh well, maybe later."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Why wait until later? Come on."
                    "You take [the_person.possessive_title]'s hand. She hesitates for a moment, then follows as you lead her away."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_reserved_flirt_response_girlfriend_2
                    mc.name "So, what did you want that privacy for again?"
                    the_person "Oh, a few things. Let's start with this..."
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "She leans in and kisses you passionately while rubbing her body against you."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_66
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_reserved_flirt_response_girlfriend_2

                "Just flirt":
                    mc.name "Aw, you're going to make me wait? That's so cruel."
                    $ mc.change_locked_clarity(10)
                    "You reach around and place a hand on [the_person.possessive_title]'s ass, rubbing it gently."
                    "She sighs and bites her lip, then clears her throat and glances around to see if anyone else noticed."
                    the_person "I'll make sure to make it worth the wait, but let's take it easy while other people are around."
                    "You give her butt one last squeeze, then slide your hand off."

        else:
            # the_person "Oh [the_person, mc_title], you're so sweet. Come on, kiss me!"
            "She smiles and sighs happily."
            the_person "Ahh, you're so sweet. Here..."
            "[the_person.possessive_title!c] leans in and kisses you. Her lips lingering against yours for a few long seconds."
            the_person "Was that nice? You're very nice to kiss."
            menu:
                "Make out":
                    "You respond by putting your arm around her waist and pulling her tight against you."
                    "You kiss her, and she eagerly grinds her body against you."

                    call mc_move_to_private_location(the_person) from  _call_mc_move_to_private_location_reserved_flirt_response_girlfriend
                    call fuck_person(the_person, start_position = kissing, private = _return, skip_intro = True) from _call_fuck_person_67
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_reserved_flirt_response_girlfriend

                "Just flirt":
                    mc.name "It was very nice. I've got some other nice things for you to kiss too, if you'd like."
                    if the_person.effective_sluttiness("sucking_cock") >= 60 or the_person.opinion.giving_blowjobs > 0:
                        "She bites her lip and runs her eyes up and down your body."
                        the_person "Mmmm, stop it [the_person.mc_title]. You're going to get me all wet in public."
                        $ mc.change_locked_clarity(10)
                        "You reach around and place your hand on her ass, rubbing it gently."
                        mc.name "Well we don't want that. I'll keep my thoughts to myself then."
                        "You give her butt one last squeeze, then slide your hand away."

                    else:
                        "She laughs and glances around."
                        the_person "Oh my god, [the_person.mc_title]! Save it for later though, I like what you're thinking..."
    else:
        # You're alone, so she's open to fooling around.
        "She smiles happily."
        the_person "Oh, well thank you [the_person.mc_title]. I'm lucky to have you too."
        "[the_person.possessive_title!c] leans in and kisses you. Her lips linger against yours for a few seconds."
        menu:
            "Kiss her more":
                "You put your arm around her waist and pull her against you, returning her sensual kiss."
                "She presses her body against you and hugs you back. Her hands run down your hips and grab at your ass as you make out."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_68
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ mc.change_locked_clarity(10)
                "You reach around [the_person.title] and place a hand on her ass, rubbing it gently. She sighs and leans her body against you."
                the_person "Mmm, that's nice... Maybe when we have some more time together we can take this further."
                mc.name "That sounds like fun. I'm looking forward to it."
                "You give her butt a light slap, then move your hand away."

    return

label reserved_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.opinion.cheating_on_men *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            the_person "Oh [the_person.mc_title], stop. If you keep talking like that you're going to get me turned on."
            mc.name "And what would be so bad about that?"
            the_person "It would be so frustrating being in public and not being able to do anything to get my satisfaction."
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "Then let's go find someplace that isn't public. Come on, follow me."
                    "[the_person.possessive_title!c] glances around, then follows behind you as you search for a quiet spot."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_reserved_flirt_response_affair
                    "Neither of you say anything as you put your hands around her and pull her into a tight embrace."
                    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                    "You kiss her, slowly and sensually. She moans and presses her body against you in return."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_69
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_reserved_flirt_response_affair

                "Just flirt":
                    mc.name "Well that would just be cruel of me..."
                    $ mc.change_locked_clarity(10)
                    "You put your arm around [the_person.possessive_title] and rest your hand on her ass."
                    mc.name "... If I got you all excited thinking about the next time I'm going to fuck you."
                    "She leans her body against yours for a moment and sighs happily. You give her butt a final slap and let go of her."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title!c] glances around, then glares at you sternly."
            the_person "[the_person.mc_title], you can't talk like that when there are other people around."
            the_person "You don't want my [the_person.so_title] to hear any rumours, do you? If he gets suspicious you might not get to see me so much..."
            "She runs a hand discretely along your arm."
            the_person "That would be such a shame, wouldn't it?"
            mc.name "Alright, I'll be more careful."
            the_person "Thank you. Just hold onto all those naughty thoughts and we can check them off one by one when we're alone."
    else:
        the_person "Oh is that so [the_person.mc_title]? Well, maybe you need to work out some of those naughty instincts..."
        "She stands close to you and runs her hand teasingly along your chest."
        menu:
            "Feel her up":
                mc.name "That sounds like a good idea. Come here."
                "You wrap your arms around [the_person.possessive_title]'s waist, resting your hands on her ass."
                "Then you pull her tight against you, squeezing her tight butt. She sighs happily and starts to kiss your neck."
                "You massage her ass for a moment, then spin her around and cup a tit with one hand. You move your other hand down to caress her inner thigh."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_70
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I want to, but I'm going to have to wait until we have more time together for that."
                $ mc.change_locked_clarity(15)
                "Her hand moves lower down, brushing over your crotch and sending a brief shiver up your spine."
                the_person "I understand. When we have the chance we'll take our time and really enjoy each other."
    return

label reserved_flirt_response_text(the_person):
    mc.name "Hey [the_person.title]. Hope you're doing well."
    mc.name "I was thinking of you and wanted to talk."
    "There's a brief pause, then she texts back."
    if the_person.is_affair:
        the_person "If you were here we could do more than just talk."
        the_person "I hope you don't make me wait too long to see you again."
        mc.name "It won't be long. Promise."

    elif the_person.is_girlfriend:
        the_person "It's sweet of you to think of me. I hope we can see each other soon."
        the_person "I want to spend more time with you in person. Texting isn't the same."
        mc.name "It won't be long, I promise."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Oh? And what did you want to talk about?"
        else:
            the_person "Oh, that's nice of you to say."
            the_person "What did you want to talk to me about?"

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Mhmm, what to tell me what sort of dirty things you were thinking about me?"
            the_person "That would be something fun to talk about."

        else:
            the_person "It's sweet of you to be thinking of me."
            the_person "I'd love to chat, what would you like to talk about?"
    return

label reserved_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Please put on a condom first. I say silly things when I get excited."
        the_person "I don't want us making a... mistake."
    else:
        the_person "You have a condom with you, right? If not, I have one."
        the_person "Just slip it on and we can get to it."
    return

label reserved_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "I'm on the pill, so you don't need to put on a condom unless you want to be very safe."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Maybe you should put on a condom. Then you can keep fucking me as you cum..."
        the_person "It's not as nice as the real thing, but it would still be nice."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "It would be smart for you to put on a condom. But if you promise to be careful..."
        the_person "Maybe we don't need one, just this once."
    return

label reserved_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.on_birth_control:
            the_person "Don't bother with a condom [the_person.mc_title]. I'm on the pill, so it's perfectly safe."
            the_person "You can cum right inside me, as often as you want."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Don't bother with a condom [the_person.mc_title], we don't need it."
            the_person "I want you to fuck me unprotected and cum inside me, like nature intended."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You don't need to bother with a condom [the_person.mc_title]."
        the_person "It feels so much better without one. You agree, right?"
    return

label reserved_condom_bareback_demand(the_person):
    if the_person.has_breeding_fetish: #Actively looking to get knocked up.
        if the_person.knows_pregnant:
            the_person "No, don't do that! If you're wearing a condom I can't feel your cum filling me up."
            the_person "Don't you want to fill me up?"
        else:
            the_person "No, don't do that! If you're wearing a condom you can't get me pregnant."
            the_person "Don't you want to knock me up?"

    elif the_person.opinion.bareback_sex > 0 or the_person.wants_creampie: #Just likes raw sex
        if the_person.on_birth_control:
            the_person "You don't need that, I'm on birth control."
            the_person "Come on [the_person.mc_title], I want you to cum inside me!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "You don't need to don't need to do that, I want you to take me raw."
            if the_person.knows_pregnant:
                the_person "I don't love it when you fill me up, [the_person.mc_title], I just want you to fuck me already!"
            else:
                the_person "I don't care if you get me pregnant [the_person.mc_title], I just want you to fuck me already!"
    else:
        if the_person.on_birth_control:
            the_person "You don't need to do that [the_person.mc_title], I'm on birth control."
            the_person "So hurry up and fuck me!"
            $ the_person.update_birth_control_knowledge()
        else:
            if the_person.knows_pregnant:
                the_person "Don't waste our time on that thing, I want you to fuck me!"
            else:
                the_person "Don't waste our time on that. I don't care about the risks, I want you to fuck me!"
    return

label reserved_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.cum_facials > 0:
            if the_person.cum_facial_count <= 1:
                the_person "I really enjoy it when you cum all over my face, [the_person.mc_title]."
            else:
                the_person "Ah, always nice to feel your cum on my face, [the_person.mc_title]."
        else:
            the_person "Well that's certainly a lot. I hope that means I did a satisfactory job."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.cum_facials > 0:
            the_person "Oh [the_person.mc_title], what are you doing to me? I'm beginning to like looking like this!"
        else:
            the_person "Oh god [the_person.mc_title], could you imagine if someone saw me like this? I really should go and get cleaned up."
    return

label reserved_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            if the_person.cum_mouth_count <= 1:
                the_person "Mmm, I love the taste of your cum [the_person.mc_title]. I wouldn't mind if we did this again."
            else:
                the_person "Mmm, always a pleasure to taste you [the_person.mc_title]. I hope you had a good time."
        else:
            "[the_person.title] puckers her lips, obviously not happy with the taste but too polite to say anything."
    else:
        if the_person.effective_sluttiness() > 80  or the_person.opinion.drinking_cum > 0:
            the_person "You're making me act like such a slut [the_person.mc_title], what would other women think if they knew what I just did?"
        elif the_person.has_tits_cum:
            the_person "Well, it seems we made quite a mess here, [the_person.mc_title]. I need to get cleaned up and brush my teeth."
        else:
            the_person "Well, at least there's no mess to clean up. I need to go wash my mouth out after that though."
    return

label reserved_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "I'm already pregnant, do you want to cum inside me again?"
            elif the_person.on_birth_control:
                the_person "Do you want to cum inside me? I shouldn't, but..."
                "She moans desperately."
                the_person "I want you to take that condom off and pump me full of your seed!"
            else:
                "She pants eagerly."
                the_person "Take... Take off the condom, I want you to cum inside me!"
                $ the_person.update_birth_control_knowledge()
                the_person "I don't care if you get me pregnant, I need it [the_person.mc_title]!"

                # the_person "Oh fuck... Do you want to knock me up?"

            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."

        else:
            the_person "Finish whenever you're ready [the_person.mc_title]!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant:
                the_person "Cum for me [the_person.mc_title], I want you to cum for me!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Oh [the_person.mc_title], I want you to cum inside me! I want to feel every last drop!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Oh [the_person.mc_title], I want you cum inside me and get me pregnant! I want you to make me a mother!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum for me! I'm on birth control, you can let it out wherever you want!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Cum for me [the_person.mc_title], I want you to cum for me!"
        else:
            if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                the_person "Wait! You need to pull out, I'm not taking birth control!"

            elif the_person.opinion.creampies < 0:
                the_person "I want you to pull out, okay? You can finish somewhere else!"

            else:
                the_person "We should be safe, you should pull out and finish somewhere else!"
    return

label reserved_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
        the_person "Oh... your seed is so close to me. Just a thin, thin condom in the way..."
    else:
        the_person "I can feel your seed through the condom. Well done, there's a lot of it."
    return

label reserved_cum_vagina(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh my... There's so much of it..."
            "She closes her eyes and sighs happily."
            the_person "It's no mystery how you got me pregnant."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "You've made such a mess of my pussy. I never let my [the_person.so_title] do this to me."
                "She closes her eyes and sighs happily as you cum inside her."
                the_person "Oh [the_person.mc_title], look what you've done."
            else:
                the_person "Oh [the_person.mc_title]... I can feel your cum inside me. It's so warm."
                "She closes her eyes and sighs happily as you cum."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Yes, give me all of your cum!"
                the_person "If I become pregnant I can say it's my [the_person.so_title]'s. I'm sure he would believe it."
            else:
                the_person "Mmm, your semen is so nice and warm. I wonder how potent it is. You might have gotten me pregnant, you know."
        else:
            if the_person.has_significant_other:
                the_person "Oh my... That's a lot of cum. It feels so nice."
                the_person "I hope my [the_person.so_title] doesn't mind if I get pregnant."

            else:
                the_person "Oh my... That's a lot of cum. It feels so nice."
                the_person "I wonder if today was a risky day? I haven't been keeping track."


    else: #She's angry
        if not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person "What would I tell my [the_person.so_title] if I got pregnant? He might not believe it's his!"
            else:
                the_person "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person "I'm in no position to be getting pregnant."
                the_person "Well, I suppose you have me in the literal position to get pregnant, but you know what I mean."

        elif the_person.has_significant_other:
            the_person "[the_person.mc_title], I told you to pull out!"
            the_person "I know you're having a good time, but I still have a [the_person.so_title]. There are boundaries."

        elif the_person.opinion.creampies < 0:
            the_person "[the_person.mc_title], I told you to pull out. Now look at what a mess you've made... It's everywhere."

        else:
            the_person "[the_person.mc_title], I told you to pull out. I guess you just lost control."

    return

label reserved_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.opinion.anal_creampies > 0:
        the_person "Cum inside me [the_person.mc_title], fill my ass with your cum!"
    elif the_person.opinion.anal_creampies < 0:
        the_person "Not inside my ass, pull out!"
    else:
        the_person "Oh lord, I hope I'm ready for this!"
    return

label reserved_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my!","Oh, that's not good!", "Whoa!", "Ah!", "My word!", "Oops!", "Bah!", "Dangnabbit!"])
    the_person "[rando]"
    return

label reserved_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I'd love to chat some more, but I've already spent far too much time getting distracted. Maybe we can catch up some other day, okay?"
    else:
        the_person "Sorry to interrupt, but I've got some work I really need to see to. I'd love to catch up some other time though."
    return

label reserved_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "I think I can do away with this for a few minutes..."
        else:
            the_person "Oh, I bet this has been in your way the whole time..."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "I think I'm past the point of needing this..."
        else:
            the_person "I don't need this any more, one second!"

    else:
        if the_person.arousal_perc < 50:
            the_person "One moment, I'm wearing entirely too much right now."
        else:
            the_person "I need this off, I want to feel you against more of me!"

    return

label reserved_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        the_person "Oh my god, I can't believe you're doing that here in front of everyone. Don't either of you have any decency?"
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        $ the_person.change_happiness(-1)
        "[title] shakes her head and tries to avoid watching you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        $ the_person.change_slut(1,30)
        "[title] tries to avert her gaze, but keeps glancing over while you and [the_sex_person.fname] [the_position.verb]."
        return True

    if the_person.sluttiness >= the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        the_person "Oh my..."
        $ the_person.change_slut(1, 50)
        "[title] watches quietly while you and [the_sex_person.fname] [the_position.verb]."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "Glad to see you two are having a good time. [the_person.mc_title], careful you aren't too rough with her."
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_reserved_sex_watch
    "[title] watches quietly while you and [the_sex_person.fname] [the_position.verb]."
    return True

label reserved_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "It's okay [the_person.mc_title], you don't have to be gentle with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        "[the_person.title] ignores [title] and keeps [the_position.verbing] you."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Mmm, come on [the_person.mc_title], let's give [title] a show!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Being watched shouldn't... I didn't think it would feel so good!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Maybe [title] is right, we shouldn't be doing this..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] glances at [title]..."
        the_person "Oh god, you shouldn't be watching me do this..."
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around."

    return

label reserved_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] pretends not to notice you come into the room."

    elif the_person.happiness > 130:
        "[the_person.title] smiles happily when you come into the room."
        the_person "Hello [the_person.mc_title], always glad to have you stop by."

    else:
        if the_person.obedience < 100:
            "You pass by [the_person.title] as you enter the room. She's absorbed by her work and only gives you a grunt and a nod."
        else:
            "You pass by [the_person.title] as you enter the room. She looks up, startled."
            the_person "Oh! Sorry [the_person.mc_title], I was distracted and didn't notice you come in. Let me know if you need help with anything."
    return

label reserved_date_seduction(the_person):
    if the_person.is_girlfriend:
        "[the_person.possessive_title!c] takes your hand and holds it in hers."
        the_person "I had a wonderful evening [the_person.mc_title]."
        "She gazes romantically into your eyes."
        $ mc.change_locked_clarity(30)
        if the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Come home with me, fuck me, and dump your virile cum inside my unprotected pussy."
                the_person "I want you to breed me, okay? I want to fuck and get pregnant."
            else:
                the_person "Come home with me and fuck me. Any way you want—no condoms, no protection."
                the_person "I'm yours [the_person.mc_title], heart and body."
        elif the_person.effective_sluttiness(["vaginal_sex", "condomless_sex"]) > 60 and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Come home with me and fuck me. I want your cock [the_person.mc_title]. I want it hard and raw inside me."
        elif the_person.effective_sluttiness(["vaginal_sex"]) > 50 and the_person.opinion.vaginal_sex > 0:
            the_person "Come home with me and we can have sex. Feeling you slide into me would be the perfect end to a perfect night."
        elif the_person.effective_sluttiness(["anal_sex"]) > 60 and the_person.opinion.anal_sex > 0:
            the_person "Come home with me. Feeling you slide your cock into my ass would be the perfect end to an already amazing date."
            the_person "Doesn't that sound like fun?"
        elif the_person.effective_sluttiness(["sucking_cock"]) > 40 and the_person.opinion.giving_blowjobs > 0:
            the_person "Come home with me. I want to repay you for this wonderful night by throating your cock."
            the_person "Doesn't that sound like fun?"
        elif the_person.effective_sluttiness() > 40 and the_person.opinion.being_covered_in_cum > 0:
            the_person "Come home with me. I want to end tonight in my favourite way; covered in cum."
            the_person "Do you think you could help me out with that?"
        elif the_person.effective_sluttiness(["touching_body"]) > 40 and the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Come home with me [the_person.mc_title]. I want to repay you for this wonderful night by working your cock with my tits."
            the_person "Does that sound like fun to you?"
        else: #She's not very slutty, so she leaves the invitation open to interpretation
            the_person "Come home with me [the_person.mc_title]. We can share another drink and keep each other company for the evening."

    elif the_person.is_affair:
        the_person "My [the_person.so_title] is staying at the office overnight."
        "She holds onto your arm and leans close, whispering softly into your ear."
        $ mc.change_locked_clarity(40)
        if the_person.wants_creampie and the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex >= 0 and the_person.opinion.creampies >= 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
            if the_person.opinion.creampies > 0: #No condoms, loves creampies, she's basically asking you to knock her up. So... have her ask you to knock her up!
                the_person "Come home with me. You'll have all night to fill my fertile pussy with your cum. I'm sure by morning you'll have me pregnant."
            else:
                the_person "Come home with me. You can fuck me all night long, any way you want, with no protection."
        elif the_person.effective_sluttiness() > the_person.get_no_condom_threshold() and the_person.opinion.bareback_sex > 0:
            the_person "Come home with me. I want to ride your cock raw, all night long."
        elif the_person.opinion.vaginal_sex > 0:
            the_person "Come home with me, and you can fuck my sweet little pussy all night long."
        elif the_person.opinion.anal_sex > 0:
            the_person "Come home with me. I want to spend all night with your cock pounding my tight little asshole."
        elif the_person.opinion.giving_blowjobs > 0:
            the_person "Come home with me. I want to worship that big cock of yours with my mouth, slide it into my throat..."
            the_person "Mmm... You can fuck my face and make me gag on it. Wouldn't you like that?"
        elif the_person.opinion.being_covered_in_cum > 0:
            the_person "Come home with me. Lay me out on his bed and cover his [the_person.so_girl_title] with cum from head to toe."
        elif the_person.opinion.giving_tit_fucks > 0 and the_person.has_large_tits:
            the_person "Come home with me. Let me worship your cock with my tits all night long."
            the_person "I'll massage you with them, fuck you with them, and make you cum with them. Over, and over again."
        elif the_person.opinion.cheating_on_men > 0:
            the_person "Come home with me. My [the_person.so_title] tries to treat me like a lady..."
            the_person "But you know that I just want to be treated like a dirty fucking whore."
        else:
            the_person "Come home with me. We can spend all night together."

    elif not the_person.has_significant_other:
        if the_person.sluttiness > the_person.love:
            $ mc.change_locked_clarity(20)
            if the_person.sluttiness > 40:
                the_person "[the_person.mc_title], would you like to come back home with me? I've got some wonderful wine that makes me do crazy things."
            else:
                the_person "You were a fantastic date [the_person.mc_title]. I know I should be getting to bed soon, but would you like to come back for a quick drink?"
        else:
            if the_person.love > 40:
                the_person "You're such great company [the_person.mc_title]. Would you like to come back to my place so we can spend some more time together?"
            else:
                the_person "I had a fantastic night [the_person.mc_title]. Before you head home would you like to share a glass of wine with me?"
    else:
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                $ mc.change_locked_clarity(20)
                the_person "[the_person.mc_title], would you like to come home with me tonight? My [the_person.so_title] is away on business and I'd love to drink some of his wine with you."
            else:
                $ mc.change_locked_clarity(20)
                the_person "This was a lot of fun. I shouldn't be out too late, but could I invite you back for a drink? My [the_person.so_title] shouldn't be home until much later."
        else:
            if the_person.love > 40:
                $ mc.change_locked_clarity(20)
                the_person "You're making me feel the same way I did when I first fell in love... Do you want to come back to my house to share one last drink?"
                the_person "My [the_person.so_title] won't be home until much later. I think he stays at work so late to avoid me."

            else:
                the_person "I had a fantastic night [the_person.mc_title], it's been so long since my [the_person.so_title] treated me this way."
                $ mc.change_locked_clarity(20)
                the_person "Would you like to share one last glass of wine at my house? My [the_person.so_title] is away on business, so I would be home all alone..."
    return

label reserved_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "You're done? You're going to drive me crazy [the_person.mc_title], I'm so horny..."
            else:
                the_person "All done? I hope you were having a good time."
        else:
            if the_person.arousal_perc > 60:
                the_person "That's all? I don't know how you can stop, I'm so horny after that!"
            else:
                the_person "Is that all? Well, that's disappointing."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "You're done? Well, you could have at least thought about me."
            else:
                the_person "All done? Maybe we can pick this up another time when we're alone."
        else:
            if the_person.arousal_perc > 60:
                the_person "I... I don't know what to say, you've worn me out."
            else:
                the_person "That's all you wanted? I guess we're finished then."
    return


label reserved_sex_take_control (the_person):
    if the_person.arousal_perc > 60:
        the_person "I can't let you go [the_person.mc_title], I'm going to finish what you started!"
    else:
        the_person "Do you think you're going somewhere? We're just getting started [the_person.mc_title]."
    return

label reserved_sex_beg_finish(the_person):
    the_person "Wait, you aren't stopping are you? Please [the_person.mc_title], I'm so close to cumming, I'll do anything!"
    return

label reserved_sex_review(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught.
            the_person "Oh [the_person.mc_title], we really need to be more discrete in the future."
            the_person "We might have to stop seeing each other if my [the_person.so_title] starts to get suspicious."

        elif used_obedience:
            the_person "[the_person.mc_title], I can't be doing this where people are watching."
            the_person "What am I going to tell my [the_person.so_title] when he hears about this?"
            mc.name "Relax, nobody here is going to tell him. You have my word."
            the_person "I suppose we'll find out..."

        else:
            the_person "Oh no, what did I just do... [the_person.mc_title], if people tell my [the_person.so_title] I..."
            mc.name "Relax, nobody here is going to tell him. You have my word."
            the_person "I hope you're right..."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "I can't believe I let you talk me into that [the_person.mc_title]... There are people around, they all saw!"
            mc.name "Relax, nobody here really cares what we were doing."
            the_person "I still don't like it..."
        else:
            the_person "I can't believe we just did that, I just... Oh lord, I wasn't thinking."
            the_person "What are people going to say about me? I..."
            mc.name "Relax, nobody here cares what we were doing. It isn't a big deal."
            "She scowls, seeming unconvinced."
            the_person "I hope you're right. Can we find somewhere more private next time?"

    # special condition - you fucked her brains out
    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            "[the_person.possessive_title!c] looks away, embarrassed by what she's done with you."
            the_person "Are we done now? It was nice, but a little too much for me..."
            mc.name "Really, so that multi-orgasmic train you were riding is your default setting?"
            the_person "Well not that... perhaps we could give it another try, someday."
        else:
            "[the_person.possessive_title!c] looks away, embarrassed by her own actions."
            the_person "Oh my... my apologies, it seems I lost control of myself."
            mc.name "Don't worry, I really enjoyed giving you the time of your life."
            the_person "Indeed, that was quite a feat, I didn't even know I could do that."

        call sex_review_trance(the_person) from _call_sex_review_trance_reserved_sex_review

    # special condition abort due to lack of girl energy without orgasm
    elif the_report.get("girl orgasms", 0) == 0 and the_person.energy < 20:
        the_person "I'm sorry, but I'm done for now."
        mc.name "No problem, we had fun, right?"
        the_person "It was very enjoyable."

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Ah, that was nice. Maybe next time we can... go a little further. Does that sound like fun to you?"
            "She gives you a dirty smile, already imagining your next encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Ah, that was exciting. I think I'm all finished too, I need to catch my breath."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks away, embarrassed by what she's done with you."
            the_person "You're all finished? Good, that went too far for me..."
            mc.name "You didn't seem to mind when you were cumming your brains out."
            the_person "I just... I wasn't thinking straight. I have myself under control now."

        else: # She's surprised she even tried that.
            "[the_person.possessive_title!c] looks away, embarrassed by what she's done with you."
            the_person "Oh my... I'm sorry, I think I lost control of myself."
            mc.name "Hey, I'm not complaining. That was a great time."
            the_person "Yeah, it was. I think I need a moment to catch my breath."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Don't you want to finish, or are you too tired already?"
            mc.name "Maybe next time, I'm just happy to make you happy."
            the_person "Such a gentleman. I'll make it up to you next time."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "All tired out? Sorry to hear that."
            "She sighs happily, still enjoying the chemical rush from her orgasm."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks away, embarrassed by what you've just done together."
            the_person "Are we finished?"
            mc.name "For now, yeah. Don't be so shy, you were obviously had a good time."
            the_person "I just... wasn't myself, that's all. I'm in control again."
            mc.name "If you say so, but I like you when you lose control."

        else: # She's surprised she even tried that.
            the_person "Finished? That's good, I think I need to sit down. My head is still spinning."
            $ the_person.draw_person(position = "sitting")
            the_person "I didn't think I was going to... climax like that. I wasn't prepared."
            mc.name "Hopefully you will be next time."
            the_person "Maybe. I don't think I could ever get used to that."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "All done? Well, I think we can call that a success."
            the_person "If we do this again I have some ideas we can try out. I think you'll {i}really{/i} enjoy them."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "All done then? Oh, I thought I was going to get to..."
            "She trails off, a little disappointed."
            mc.name "Sorry, I'm just a little worn out. Next time, I promise."

        elif used_obedience: #She only did it because she was commanded
            the_person "Finished? Good."
            "She looks away, embarrassed by what you've just done."
            mc.name "Yeah, all done for now."

        else:  # She's surprised she even tried that.
            the_person "Ah... We're done? Right, of course. Sorry, I don't even know what I'm thinking."
            "She laughs nervously."
            the_person "I just got a little carried away, I'm, ah... I'm fine now."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "All done, I'm too tired, time to go."
        mc.name "Sure, we will continue this another time."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "That's all? Well, that's a little disappointing. I was just getting excited."
            the_person "Make it up to me next time, okay?"
            mc.name "Yeah, sure thing."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Finished already?"
            "[the_person.possessive_title!c] seems a little disappointed."
            the_person "Next time you're going to have to pace yourself, or you're going to keep disappointing me."
            # the_person "Done already? We'll have to take it more slowly so you don't get so tired next time."
            # "[the_person.possessive_title!c] seems a little disappointed."

        elif used_obedience: #She only did it because she was commanded
            the_person "Finished? I thought you were going to..."
            the_person "Never mind. If you're done that's fine with me."

        else:  # She's surprised she even tried that.
            the_person "You're right, we should stop. I'm getting far too excited, I might do something I regret."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        the_person "Oh [the_person.mc_title], you should really be more careful, I could get pregnant."

    $ del comment_position
    return


## Role Specific Section ##
label reserved_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get used to the lab there is something I want to talk to you about."
    the_person "Sure, what can I help you with?"
    mc.name "Our R&D up to this point has been based on my old notes from university."
    mc.name "There were some unofficial experiment results that suggested the effects might be enhanced by sexual arousal."
    "[the_person.title] nods her understanding."
    the_person "Ah, so you had noticed that too? I have a hypothesis that an orgasm opens chemical receptors that are normally blocked."
    mc.name "What else can we do if we assume that is true? Does that open up any more paths for our research?"
    the_person "If it's true I could leverage the effect to induce greater effects in our subjects."
    "[the_person.possessive_title!c] thinks for a long moment, then smiles mischievously."
    the_person "But we'll need to do some experiments to be sure."
    mc.name "What sort of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects."
    the_person "Then I'll make myself climax, and we can compare the effects after."
    mc.name "Do you think that's a good idea?"
    the_person "Not entirely, no. But we can't trust anyone else with this information if we're right."
    the_person "We might be able to make progress by brute force, but this is a chance to catapult our knowledge to another level."
    the_person "A finished dose of serum that raises my Suggestibility. The higher it gets my Suggestibility the better, but any amount should do."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my orgasms will have."
    return

# label reserved_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] nods in agreement."
#     the_person "I think I have an idea that could really help us along. All of our testing procedures focus on human safety, but what I really need to know about are the subjective effects of our creations."
#     the_person "With your permission, I would like to take a dose of serum myself and have you record my experience with it."
#     return

## Taboo break dialogue ##
label reserved_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, well hello there! Do you... Want to do anything with me?"
    elif the_person.love >= 20:
        the_person "So you feel it too?"
        "She sighs happily."
        the_person "I... I want to kiss you. Would you kiss me?"
    else:
        the_person "I don't know if this is a good idea [the_person.mc_title]..."
        mc.name "Let's just see how it feels. Trust me."
        "[the_person.title] eyes you warily, but you watch her resolve break down."
        the_person "Okay... Just one kiss, to start."
    return

label reserved_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Do you want to know something?"
        mc.name "What?"
        the_person "I've had dreams just like this before. They always stop just before you touch me."
        mc.name "Well, let's fix that right now."

    elif the_person.love >= 20:
        the_person "I want you to know I take this very seriously, [the_person.mc_title]."
        mc.name "Of course. So do I [the_person.title]."
        the_person "I normally wouldn't even think about letting someone like you touch me."
        mc.name "What do you mean, \"Someone like me\"?"
        the_person "You're a troublemaker. I always get the feeling you're bad news for me, but..."
        the_person "But I just can't say no to you."
    else:
        the_person "You shouldn't be doing this [the_person.mc_title]. We... We barely know each other."
        mc.name "You don't want me to stop though, do you?"
        the_person "I don't... I don't know what I want."
        mc.name "Then let me show you."
    return

label reserved_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Look at how big your penis is. You poor thing, that must be very uncomfortable."
        the_person "Just relax and I'll see what I can do about it, okay?"
    elif the_person.love >= 20:
        the_person "Oh my... If I'm honest I wasn't expecting it to be quite so... Big."
        mc.name "Don't worry, it doesn't bite. Go ahead and touch it, I want to feel your hand on me."
        "She bites her lip playfully."
    else:
        the_person "We should stop here... I don't want you to get the wrong idea about me."
        mc.name "Look at me [the_person.mc_title], I'm rock hard. Nobody would ever know if you gave it a little feel."
        "You see her resolve waver."
        the_person "It is very... Big. Just feel it for a moment?"
        mc.name "Just a moment. No longer than you want to."
        "She bites her lip as her resolve breaks completely."
    return

label reserved_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Do it [the_person.mc_title]. Touch my pussy."
    elif the_person.love >= 20:
        the_person "I'm so nervous [the_person.mc_title], do you feel that way too?"
        mc.name "Just take a deep breath and relax. You trust me, right?"
        the_person "Of course. I trust you."
    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
    return

label reserved_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "What would you like?"
    mc.name "I'd like you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "I... I really should say no."
        mc.name "But you aren't going to."
        "She shakes her head."
        the_person "I've told people all my life that I didn't do things like this, but now it's all I can think about."
    elif the_person.love >= 30:
        the_person "Oh [the_person.mc_title]! Really? I know most men are into that sort of thing, but I..."
        the_person "Well, I think I'm a little classier than that."
        mc.name "What's not classy about giving your partner pleasure? Come on [the_person.title], aren't you a little curious?"
        the_person "I'm curious, but I... Well... How about I just give it a taste and see how that feels?"
        mc.name "Alright, we can start slow and go from there."
    else:
        the_person "I'm sorry, I think I misheard you."
        mc.name "No you didn't. I want you to put my cock in your mouth and suck on it."
        the_person "I could never do something like that [the_person.mc_title], what would people think?"
        the_person "I'm not some kind of slut, I don't \"suck cocks\"."
        mc.name "Yeah you do, and you're going to do it for me."
        the_person "Why would I do that?"
        mc.name "Because deep down, you want to. You can be honest with me, aren't you a little bit curious what it's going to be like?"
        "She looks away, but you both know the answer."
        mc.name "Just get on your knees, put it in your mouth, and if you don't like how it feels you can stop."
        the_person "What are you doing to me [the_person.mc_title]? I used to think I was better than this..."
    return

label reserved_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Oh what a gentleman I have! I'm ready [the_person.mc_title], eat me out!"
    elif the_person.love >= 30:
        the_person "You're such a gentleman [the_person.mc_title], but you don't have to do that."
        mc.name "I don't think you understand. I {i}want{/i} to eat you out, I'm not doing it as a favour."
        "[the_person.title] almost seems confused by the idea."
        the_person "Oh... Well then, I suppose you can get right to it."
    else:
        the_person "You're a gentleman [the_person.mc_title], but you don't need to do that."
        if not the_person.has_taboo("sucking_cock"):
            the_person "It's flattering that you'd want to return the favour though, so thank you."

        mc.name "No, I don't think you understand what I'm saying. I {i}want{/i} to eat you out, I'm not doing it as a favour."
        "[the_person.title] almost seems confused by the idea."
        the_person "Really? I mean... I just haven't met many men who want to do that."
        mc.name "Well you have one now. Just relax and enjoy yourself."
    return

label reserved_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "[the_person.mc_title], I'm not ashamed to say I'm very excited right now!"
        "She giggles gleefully."
        the_person "Come on and fuck me!"
    elif the_person.love >= 45:
        the_person "Go ahead [the_person.mc_title]. I think we're both ready for this."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Oh my god, what am I doing here [the_person.mc_title]?"
            the_person "I'm not the type of person to do this... Am I? Is this who I've always been, and I've just been lying to myself?"
            mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
            "She closes her eyes and takes a deep breath."
            the_person "I... I want to have sex with you. I'm ready."
        else:
            the_person "I'm glad you're doing this properly this time."
            "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    return

label reserved_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "She takes a few deep breaths."
        the_person "I'm ready if you are [the_person.mc_title]. Come and fuck my ass."

    elif the_person.love >= 60:
        the_person "This is really something you want to do then [the_person.mc_title]?"
        mc.name "Yeah, it is."
        the_person "Okay then. It wouldn't be my first pick, but we can give it a try."
        the_person "I don't know if you'll even fit though. Your penis is quite large."
        mc.name "You'll stretch out more than you think."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Oh lord, what happened to me?"
            the_person "I thought I was a respectable lady, now I'm about to get fucked in the ass..."
            the_person "We've never even had sex before and now I'm doing anal!"

            #TODO: "At least my vagina still belongs to my SO... At least I still have that one thing."

        else:
            the_person "I'm not sure about this [the_person.mc_title]... I'm not even sure if you can fit inside me there!"
            mc.name "I can stretch you out, don't worry about that."
            the_person "Oh lord, what happened to me..."
            the_person "I used to think I was a respectable lady, now I'm about to get fucked in the ass..."
        mc.name "Relax, you'll be fine and this isn't the end of the world. Who knows, you might even enjoy yourself."
        the_person "I doubt it. Come on then, there's no point stalling any longer."
    return

label reserved_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "You want to have sex without any protection? I'll admit, that would really turn me on."
        if the_person.wants_creampie:
            the_person "I want you to fill me up completely."
        else:
            the_person "When you finish I want you to cover me with all that cum."

    elif the_person.opinion.bareback_sex > 0:
        the_person "You want to have sex without any protection? I'll admit, that would really turn me on."
        if the_person.on_birth_control:
            the_person "I am on birth control, so it should be perfectly safe. I do want to know what you feel like raw..."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "It would be very naughty if you came inside me though. I'm not on any birth control..."
            $ the_person.update_birth_control_knowledge()
            mc.name "Don't you think we're being naughty already?"
            "She bites her lip and nods."
            the_person "I think we are."
        elif the_person.opinion.creampies < 0:
            the_person "You will need to pull out though. I hate having cum dripping out of me all day."
        else:
            the_person "I'm not on birth control, so you will need to pull out. Understood? Good."
            $ the_person.update_birth_control_knowledge()

    elif the_person.love > 60:
        the_person "If you think you're ready for this commitment, I am too. I want to feel close to you."
        if the_person.on_birth_control:
            the_person "I'm on birth control, so the chances of getting me pregnant are slim, but you should know they still exist."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "When you're going to finish you don't have to pull out unless you want to. Okay?"
            mc.name "Are you on the pill?"
            "She shakes her head."
            the_person "No, but I trust you to make the decision that is right for both of us."
            $ the_person.update_birth_control_knowledge()
        elif the_person.opinion.creampies < 0:
            if the_person.kids == 0:
                the_person "You will have to pull out though, okay? I really don't plan on being a mother."
            else:
                the_person "You will have to pull out though, okay? I've been pregnant before and it isn't pretty."
        else:
            if the_person.kids == 0:
                the_person "You will have to pull out though. I don't want you to make me a mother."
            else:
                the_person "You will have to pull out though, understood? I don't think either of us are ready for that."

    else:
        the_person "You want to have sex without protection? That's very risky [the_person.mc_title]."
        if the_person.on_birth_control:
            the_person "I'm on birth control, but nothing is one hundred percent effective."
            $ the_person.update_birth_control_knowledge()
            mc.name "I'm willing to take that chance. Are you?"
            "She thinks for a moment, then nods."
            the_person "I believe I am."
        elif the_person.has_taboo("vaginal_sex"):
            mc.name "I want our first time to be special though, don't you?"
            "She takes a second to think, then nods."
            the_person "I do. You need to be very careful where you finish, okay?"
        else:
            mc.name "It will feel so much better raw, for both of us."
            the_person "I have wondered what it would be like..."
            "She takes a moment to think, then nods."
            the_person "Fine, you don't need a condom. Please be very careful where you finish, okay?"
    return

label reserved_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.opinion.skimpy_outfits * 5):
        the_person "This is the first time you've gotten to see my underwear. I hope you like what you see."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm sure I will. You have good taste."
            the_person "Well then, what are you waiting for then?"
        else:
            mc.name "I've already seen you out of your underwear, but I'm sure it complements your form."
            the_person "Time to find out. What are you waiting for?"

    elif the_person.love > 15:
        the_person "This is going to be the first time you've seen me in my underwear. I have to admit, I'm feeling a little nervous."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Don't be, I'm sure you look stunning in it."
            the_person "Well then, take off my [the_clothing.display_name] for me."

        else:
            mc.name "I already know you have a beautiful body, some nice underwear can only enhance the experience."
            the_person "You're too kind. Help me take off my [the_clothing.display_name]."

    else:
        the_person "If I take off my [the_clothing.display_name] you'll see me in my underwear."
        mc.name "That's the plan, yes."
        the_person "I shouldn't be going around half-naked for men I barely know. What would people think?"

        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Why do you care what other people think? Forget about them and just focus on the moment."
            the_person "I'll try..."

        else:
            mc.name "You might have wanted to worry about that before I saw you naked. You don't have anything left to hide."
            the_person "I suppose you're right..."
    return

label reserved_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.opinion.showing_her_tits * 5):
        the_person "Oh, so you want to take a look at my breasts?"
        if the_person.has_large_tits:
            "She bounces her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
        else:
            "She bounces her chest and gives her [the_person.tits_description] a little jiggle."
        the_person "Well it would be a shame not to let you get a glimpse, right? I've been waiting for you to ask."
        mc.name "Let's get that [the_clothing.display_name] off so I can see them then."

    elif the_person.love > 25:
        the_person "Oh, you want to get my breasts out?"
        if the_person.has_large_tits:
            "She looks down at her own large rack, tits hidden restrained by her [the_clothing.display_name]."
            the_person "I don't have to ask why. I'm glad you're interested in them."
        else:
            the_person "I'm glad you're still interested in smaller breasts. It seems like every man is mad boob-crazy these days."
        mc.name "Of course I'm interested. let's get that [the_clothing.display_name] out of the way so I can get a good look at you."

    else:
        the_person "Hey there! If you take off my [the_clothing.display_name] I won't be decent any more!"
        mc.name "I want to see your tits and it's in the way."
        the_person "I'm aware it's \"in the way\", that's why I put it on this morning."
        if the_person.has_large_tits and the_clothing.underwear:
            the_person "Besides, a girl like me needs a little support. These aren't exactly light."
        mc.name "Come on [the_person.title]. You're gorgeous, I'm just dying to see more of you."
        the_person "Well I'm glad I have that effect on you. I suppose..."
        "She takes a moment to think, then sighs and nods."
        the_person "You can take off my [the_clothing.display_name] and have a look. Just be kind to me, I'm feeling very vulnerable."
    return

label reserved_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.opinion.showing_her_ass * 5):
        the_person "You want to get me out of my [the_clothing.display_name]? Well, I'm glad you've finally asked."

    elif the_person.love > 35:
        the_person "Oh, careful there [the_person.mc_title]. If you take off my [the_clothing.display_name] I won't be decent any more."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I don't particularly want you to be decent at the moment, though. I want to get a look at your sweet pussy."
            the_person "Oh stop, you're going to make me blush."
            "She thinks for a moment, then nods timidly."
            the_person "Okay, you can take it off and have a look, if you'd like."

        else:
            mc.name "I think you stopped being decent when you let me touch your pussy."
            the_person "Oh stop, you. I suppose you can take it off and have a look, if you'd like."

    else:
        the_person "Oh! Careful, or you're going to have me showing you everything!"
        mc.name "That is what I was hoping for, yeah."
        the_person "Well! I mean... I'm not that sort of woman [the_person.mc_title]!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Don't you want to be though? Don't you want me to enjoy your body?"
            the_person "I... I mean, I might, but I shouldn't... You shouldn't..."
        else:
            mc.name "Of course you are! I've had my hand on your pussy already, I just want to see what I was feeling before."
            the_person "I... I mean, that wasn't... I..."

        "You can tell her protests are just to maintain her image, and she already knows what she wants."
        mc.name "Just relax and let it happen, you'll have a good time."
    return

# label reserved_facial_cum_taboo_break(the_person):

#     return

# label reserved_mouth_cum_taboo_break(the_person):

#     return

# label reserved_body_cum_taboo_break(the_person):

#     return

label reserved_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Hmm, that's right, were it belongs."
            "She sighs happily."

        elif the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Oh, you came inside me... My poor [the_person.so_title], he will get sloppy seconds!"

            else:
                the_person "Oh my god, you really filled me up... but it does feel good!"

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "Ah, you finally filled me up, I'm sure my [the_person.so_title] would mind! He's been neglecting his duty."

            else:
                the_person "Ah, you finally filled me up! I've been wondering how it would feel! I don't even care I'm not on the pill!"
                $ the_person.update_birth_control_knowledge()

            "She pants happily for a moment."
            the_person "Do you think you got me pregnant? We should do it again, just to make sure."

        else:
            if the_person.has_significant_other:
                the_person "Ah, I should have told you to pull out, but I do love the feeling..."
                the_person "You shouldn't do it again though, I don't want to explain to my [the_person.so_title] how I got pregnant."

            else:
                the_person "Ah, you should have pulled out... I'm not on birth control..."
                $ the_person.update_birth_control_knowledge()
                the_person "It's fine, I shouldn't get pregnant from one cumshot..."

    else:
        if the_person.knows_pregnant:
            the_person "Oh my, you finished so deep inside me."

        elif not the_person.on_birth_control:
            the_person "Oh my god, [the_person.mc_title]! You didn't cum inside me, did you?"
            "She groans unhappily."
            if the_person.has_significant_other:
                the_person "Ugh, what if I get pregnant? I can't tell my [the_person.so_title] it's his."
            else:
                the_person "Ugh, what if I get knocked up? This was only meant for fun!"
                the_person "Ah well, it should be fine, nobody is that potent."

        elif the_person.has_significant_other:
            the_person "Hey, I told you to pull out. I don't want my [the_person.so_title] to find out that I have some fun on the side..."
            the_person "I guess it's done. You need to be more careful in the future."

        elif the_person.opinion.creampies < 0:
            the_person "I said to pull out! Now look at what you've done, you've made such a mess inside me."

        else:
            the_person "[the_person.mc_title], not inside me! I'm a lady and you should respect my wishes."
    return

label reserved_anal_creampie_taboo_break(the_person):
    if the_person.opinion.anal_creampies > 0:
        if the_person.effective_sluttiness() > 75 or the_person.opinion.anal_creampies > 1:
            if the_person.has_significant_other:
                the_person "Ah yes! All that cum inside my ass, my [the_person.so_title] is too composed for filling me up like this!"

            else:
                the_person "Ah, yes! You should have put that load inside my ass sooner!"

            "She pants happily for a moment."
            the_person "Oh god, my ass will drip cum all day long, I love it."

        else:
            if the_person.has_significant_other:
                the_person "Ah, you should have pulled out, but it does feel good..."
                the_person "My [the_person.so_title] never fills my ass, but I think I like it."

            else:
                the_person "Ah, you should have pulled out... but it does feel good..."
                the_person "All that cum in my tight little rectum..."

    else:
        if the_person.has_significant_other:
            the_person "Hey, didn't I tell you to pull out?! I don't want my [the_person.so_title] to see my leaking ass..."
            the_person "I guess it's done. You should cum on my ass next time!"

        elif the_person.opinion.anal_creampies < -1:
            the_person "I said to pull out! Look at this mess you made, my ass will be dripping cum all day long."

        else:
            the_person "I said to pull out! Don't you make a habit of filling my ass up with your spunk."
    return

label reserved_dual_penetration_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "She takes a few deep breaths."
        the_person "I'm ready if you are [the_person.mc_title]. Come and fuck my ass."
    elif the_person.love >= 60:
        the_person "This is really something you want to do then [the_person.mc_title]?"
        mc.name "Yeah, it is."
        the_person "Okay then. It wouldn't be my first pick, but we can give it a try."
        the_person "I don't know if you'll even fit though. Your penis is quite large."
        mc.name "You'll stretch out more than you think."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Oh lord, what happened to me?"
            the_person "I thought I was a respectable lady, now I'm about to get fucked in the ass..."
            the_person "We've never even had sex before and now I'm doing anal!"
            #TODO: "At least my vagina still belongs to my SO... At least I still have that one thing."
        else:
            the_person "I'm not sure about this [the_person.mc_title]... I'm not even sure if you can fit inside me there!"
            mc.name "I can stretch you out, don't worry about that."
            the_person "Oh lord, what happened to me..."
            the_person "I used to think I was a respectable lady, now I'm about to get fucked in the ass..."
        mc.name "Relax, you'll be fine and this isn't the end of the world. Who knows, you might even enjoy yourself."
        the_person "I doubt it. Come on then, there's no point stalling any longer."
    return

label reserved_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        the_person "That might be possible! Make sure you are well rested, I have some high expectations."
    else:
        the_person "I am willing to come over, make sure you have some wine cooled. We can make it a great night!"
    return

label reserved_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        the_person "I wouldn't mind you coming over. I'm sure you won't be able to go home, after our night together."
    else:
        the_person "I will make sure to chill some wine, you just make sure that you can keep up."
    return

label reserved_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] slowly walks over to you, with slow calculated erotic movements."
    the_person "Thanks... are you ready for me?"
    return

label reserved_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Alright, let's cuddle up and watch a movie!"
    "She gives you a smirk. You can't help but frown at the thought of just cuddling..."
    the_person "Why so glum? Isn't that what you had in mind..."
    "She sets her wine down on her nightstand."
    the_person "Don't worry, I was just kidding, now show me what you can do!"
    return

label reserved_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Oh my god, how did you do that... this is amazing..."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I could go for another round... how about you?"
    return

label reserved_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ahhh, that was adequate..."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I could use some more stimulation, if you are up for it?"
    return

label reserved_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Right, well... let's have another drink and show me something more interesting!"
    "You take some time to catch your breath, and take a few sips from your wine."
    "You slowly start caressing [the_person.title] while she touches herself, keeping herself ready for you."
    return


label reserved_activity_arcade_response(the_person, mc_won):
    # 1
    the_person "That was fun, nothing like a good arcade game once in a while."
    if mc_won:
        the_person "You won this time, but next time you won't be so lucky."
        $ the_person.change_stats(obedience = 1, max_obedience = 140, happiness = 2, arousal = 5)
    else:
        the_person "Maybe next time you'll get lucky and win."
        $ the_person.change_stats(obedience = -1, happiness = 2)
    return

label reserved_activity_billiards_response(the_person, mc_won):
    # 2
    the_person "Pool is such a fun game."
    if mc_won:
        the_person "I guess I shouldn't be surprised you are so good at it. Well played!"
        $ the_person.change_stats(obedience = 2, max_obedience = 180, happiness = 3, arousal = 5, love = 2, max_love = 60)
    else:
        the_person "If you practice, maybe one day you'll be able to beat me!"
        $ the_person.change_stats(obedience = -1, happiness = 5, love = 2, max_love = 40)
    return

label reserved_activity_salsa_response(the_person, mc_won):
    # 1
    if mc_won:
        the_person "Thank you for the dance! That was really fun!"
        $ the_person.change_stats(obedience = 2, max_obedience = 140, happiness = 3, arousal = 10, love = 1, max_love = 40)
    else:
        the_person "Thank you for trying. I still had fun, even if we stepped on each other's feet once in a while!"
        $ the_person.change_stats(obedience = -2, happiness = 3, love = 1, max_love = 30)
    return

label reserved_activity_darts_response(the_person, mc_won):
    # 1
    if mc_won:
        the_person "You're pretty good at that. Thankfully I don't mind having an extra drink!"
        $ the_person.change_stats(obedience = 2, max_obedience = 160, happiness = 2, arousal = 10)
    else:
        the_person "Drink up! Maybe you'll do better next time, though I doubt it!"
        $ the_person.change_stats(happiness = 2, arousal = 5)
    return

label reserved_activity_karaoke_response(the_person, mc_won):
    # -2
    pass
    return

label reserved_activity_trivia_response(the_person, mc_won):
    # 0
    if mc_won:
        the_person "Wow, I'm glad you were on our team, [the_person.mc_title]!"
        $ the_person.change_stats(obedience = 1, max_obedience = 140, happiness = 2, arousal = 5)
    else:
        "[the_person.possessive_title!c] shrugs"
        the_person "Sorry, I guess trivia just isn't really my thing."
        $ the_person.change_stats(happiness = -2, obedience = 1, max_obedience = 130)
    return

label reserved_activity_pong_response(the_person, mc_won):
    # 0
    the_person "That was fun. Did you have fun?"
    if mc_won:
        the_person "Nevermind, I'm sure you did. You seem pretty good at that, actually..."
        $ the_person.change_stats(obedience = 1, max_obedience = 130, happiness = 2, arousal = 5)
    else:
        the_person "Hope so. Drink up!"
        $ the_person.change_stats(happiness = 2, obedience = -1)
    return
