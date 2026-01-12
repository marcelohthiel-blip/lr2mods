label erica_greetings(the_person):
    if mc.is_at(gym):
        if erica_get_progress() >= 2:
            the_person "Hey there, [the_person.mc_title]."
            "You see [the_person.title] here at the Gym, in her usual spot on the treadmill."
            the_person "You want to join me for another workout? I always leave the gym feeling so satisfied when we work out together!"
        else:
            the_person "Hey there!"
    elif mc.is_at(the_person.home):
        if erica_get_progress() > 3:
            the_person "Hey there, [the_person.mc_title]! I wasn't expecting you! Are you here for some fun?"
            "She looks at you hopefully."
        else:
            the_person "Hey there, [the_person.mc_title]. I wasn't expecting you, are you sure you should be here?"

    elif the_person.effective_sluttiness() > 60:
        if the_person.obedience > 180:
            the_person "Hello, [the_person.mc_title], it's good to see you."
        else:
            the_person "Hey there handsome, feeling good?"
    else:
        if the_person.obedience > 180:
            the_person "Hello, [the_person.mc_title]."
        else:
            the_person "Hey there!"
    return

label erica_sex_responses(the_person):
    if the_person.effective_sluttiness() > 50:
        if the_person.obedience > 180:
            the_person "Oh my, keep doing that please!"
        else:
            the_person "Fuck it feels good when you do that. Keep going!"
    else:
        "[the_person.title] closes her eyes and moans quietly to herself."
    return

label erica_climax_responses_foreplay(the_person):
    if the_person.effective_sluttiness() > 50:
        the_person "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        the_person "Oh fuck, you're going to make me cum! Fuck!"
        "She goes silent, then lets out a shuddering moan."
    return

label erica_climax_responses_oral(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Fuck yes, I'm going to cum! Make me cum!"
    else:
        the_person "Oh my god, you're good at that! I'm going to... I'm going to cum!"
    return

label erica_climax_responses_vaginal(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Ah! I'm cumming! Oh fuck! Ah!"
    the_person "Fuck this feels better than winning a marathon!"
    return

label erica_climax_responses_anal(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person "Ah! Mmhmmm!"
    else:
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "I think you're going to make me..."
        "She barely finishes her sentence before her body is racked with pleasure."
        the_person "Cum!"
    return

label erica_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person "Thanks, [the_person.mc_title]! I wonder if I could wear this at the gym."
    return

#label erica_clothing_reject(the_person):
#    if the_person.obedience > 180:
#        the_person "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
#    else:
#        if the_person.effective_sluttiness() > 60:
#            the_person "Wow. I'm usually up for anything but I think that's going too far."
#        else:
#            the_person "Wow. It's a little... skimpy. I don't think I could wear that."
#    return

label erica_clothing_review(the_person):
    if mc.is_at(gym):
        if the_person.effective_sluttiness() > 40:
            the_person "I love when you look at me like that, but I don't think the gym staff would appreciate it as much. I'd better clean up a bit."
        else:
            the_person "I'd better clean up some before I go to leave the gym..."
    elif the_person.obedience > 180:
        the_person "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
    else:
        if the_person.effective_sluttiness() > 40:
            the_person "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
        else:
            the_person "My clothes are a mess! I can't go out like this, let me get cleaned up."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

#label erica_strip_reject(the_person, the_clothing, strip_type = "Full"):
#    if the_person.obedience > 180:
#        the_person "I'm sorry, but can we leave that where it is for now?"
#    elif the_person.obedience < 70:
#        the_person "Slow down there, I'll decide when that comes off."
#    else:
#        the_person "I think that should stay where it is for now."
#    return

label erica_sex_accept(the_person, the_position):
    if the_person.effective_sluttiness() > 70:
        if the_person.obedience < 70:
            the_person "I was just about to suggest the same thing."
        else:
            the_person "Mmm, you have a dirty mind [the_person.mc_title], I like it."
    else:
        the_person "Okay, we can give that a try."
    return

label erica_sex_obedience_accept(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Oh god [the_person.mc_title], I should really say no... But you always make me feel so good, I can't say no to you."
    else:
        if the_person.obedience > 180:
            the_person "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person "I... Okay, if you really want to, let's give it a try."
    return

label erica_sex_gentle_reject(the_person):
    if the_person.effective_sluttiness() > 50:
        the_person "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
    else:
        the_person "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
    return

label erica_sex_angry_reject(the_person):
    if the_person.effective_sluttiness() < 20:
        the_person "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person "Ugh! Get away from me, I don't even want to talk to you after that."
    else:
        the_person "What the fuck do you think you're doing, that's disgusting!"
        the_person "Get the fuck away from me, I don't even want to talk to you after that!"
    return

label erica_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.effective_sluttiness() > 50:
            the_person "Yes [the_person.mc_title]? Do you need help relieving some stress?"
        else:
            the_person "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.effective_sluttiness() > 10:
            the_person "Oh, do you see something you like?"
        else:
            the_person "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label erica_seduction_accept_crowded(the_person):
    if mc.is_at(gym):
        if the_person.effective_sluttiness() < 20:
            the_person "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
        elif the_person.effective_sluttiness() < 70:
            the_person "Come on, let's sneak into the locker room and do it!"
        else:
            the_person "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
        return

    if the_person.effective_sluttiness() < 20:
        the_person "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
    elif the_person.effective_sluttiness() < 50:
        the_person "Come on, let's go find someplace quiet where we won't be interrupted."
    else:
        the_person "No point wasting any time then, right? Let's get to it!"
    return

label erica_seduction_accept_alone(the_person):
    if mc.is_at(gym):
        if the_person.effective_sluttiness() < 20:
            the_person "Well, there's nobody around to see us..."
        elif the_person.effective_sluttiness() < 50:
            the_person "I can't believe how empty the gym is right now. Let's do it right here!"
        else:
            the_person "Oh [the_person.mc_title], the gym is empty, fuck me now!"
        return
    if the_person.effective_sluttiness() < 20:
        the_person "Well, there's nobody around to stop us..."
    elif the_person.effective_sluttiness() < 50:
        the_person "Mmm, that's a fun idea. Come on, let's get to it!"
    else:
        the_person "Oh [the_person.mc_title], don't make me wait!"
    return

#label erica_seduction_refuse(the_person):
#    if the_person.effective_sluttiness() < 20:
#        "[the_person.title] blushes and looks away from you awkwardly."
#        the_person "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
#
#    elif the_person.effective_sluttiness() < 50:
#        the_person "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
#        "[the_person.title] smiles and gives you a wink."
#
#    else:
#        the_person "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
#    return

label erica_flirt_response(the_person):
    if mc.is_at(gym):
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person "Didn't your mother ever tell you it's rude to hit on girls at the gym?"
            return
        if erica_get_progress() >= 2:
            the_person "Well why don't you work out with me for a bit and we can work up a sweat together?"
        else:
            the_person "Hey, maybe if you work out with me first."
            "[the_person.title] gives you a wink and smiles."
        return

    if the_person.obedience > 180:
        if the_person.effective_sluttiness() > 50:
            the_person "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person "Thank you for the compliment, [the_person.mc_title]."
    else:
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peek."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

label erica_flirt_response_low(the_person):
    "[the_person.possessive_title!c] blushes and smiles."
    $ mc.change_locked_clarity(5)
    the_person "Thanks. I didn't think anyone even paid attention to what I wear. I mean it's just gym clothes..."
    mc.name "Yeah, and the way you dress makes it obvious how well you take care of yourself. It's pretty incredible."
    return

label erica_flirt_response_low1(the_person):
    "[the_person.possessive_title!c] stands up and gives you a naughty smile."
    $ the_person.draw_person(position = "back_peek", emotion = "happy")
    $ mc.change_locked_clarity(5)
    the_person "How does it look from this angle?"
    mc.name "Don't move, let me take a mental picture."
    the_person "Anything else?"
    $ the_person.draw_person()
    return

label erica_flirt_response_mid(the_person):
    if the_person.effective_sluttiness() < 20:
        $ mc.change_locked_clarity(10)
        the_person "Thanks! I work hard to take care of myself. It's kind of weird to hear, but I'm glad it shows."
    else:
        the_person "Thanks! One of the benefits of being in shape I guess, you can wear clothing to show off your body."
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        the_person "Good?"
        $ mc.change_locked_clarity(10)
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title!c] smiles and turns back to face you."
        $ the_person.draw_person()
        the_person "I'm sure you do. Maybe instead of shooting the breeze you should work out with me..."
    return

label erica_flirt_response_mid1(the_person):
    $ mc.change_locked_clarity(10)
    if mc.location.person_count > 1:
        "[the_person.possessive_title!c] smiles, then glances around self-consciously."
        the_person "Keep it down, people might get the wrong impression."
    the_person "You are right, it does suit me very well."
    $ mc.change_locked_clarity(10)
    mc.name "How about you and me go and grab a coffee sometime?"
    if the_person.has_significant_other:
        the_person "We can't do that [the_person.mc_title], what if my [the_person.so_title] finds out?"
        mc.name "Come on, it's just a coffee, we are not going to a party."
    the_person "I guess so, you're right, ask me after a workout someday."
    return

label erica_flirt_response_high(the_person):
    # change response when we are in a relationship
    if the_person.has_relation_with_mc:
        call reserved_flirt_response_high(the_person) from _call_reserved_flirt_response_high_erica_flirt_response_high
        return

    if the_person.love > 50: #She is going to ghost soon
        the_person "I feel like you are going a little overboard there with the flattery. Could you please stop?"
    else:
        "She looks at you and her eyes narrow."
        the_person "I appreciate the comment, I really do... but I'm worried you are taking things a little too far."
        the_person "Remember, we need to keep things CASUAL. Okay?"
    return


#TODO: wire up this up with the_person.call_dialogue("hookup_rejection") -> also needs a default implementation in relaxed personality
label erica_hookup_rejection(the_person):
    the_person "Your loss! I've been working out so much lately, and you could have had some of this..."
    return

#TODO: wire up this up with the_person.call_dialogue("hookup_accept") -> also needs a default implementation in relaxed personality
label erica_hookup_accept(the_person):
    the_person "Meet me at the gym... you know the place!"
    "You put your phone in your pocket and head to the gym."

    $ mc.change_location(gym)
    "A few minutes later, you walk into the gym."
    $ mc.change_location(gym_shower)
    "You locate the family locker room in the shower section and discover it to be unlocked. You quietly let yourself in."
    $ the_person.draw_person(position = "missionary")
    $ the_person.arousal = 20
    "You discover [the_person.possessive_title] sitting at one of the sinks, touching herself while waiting for you. Her pussy glistens with arousal."
    "You quickly lock the door behind you. She notices you walk in but doesn't say a word."
    "You walk over to her silently, and then get down on your knees in front of her. Her pussy is hanging off the side of the sink, right in front of your face."
    $ the_person.increase_cunnilingus()
    "You waste no time and dive your tongue straight into her cunt. Her tangy juices greet your tongue."
    the_person "Mmmm, this is my favourite warm up..."
    $ the_person.change_arousal( 15 + (mc.oral_sex_skill * 2)) #35 + 2
    $ mc.change_locked_clarity(10)
    "You quickly lap up the juices available along her labia, then focus your attention on her clitoris with the goal of making more."
    "You circle your tongue around it several times, teasing her. Just when she thinks you are going to lick it you dart down to her hole."
    the_person "What a tease! I had a boyfriend once who couldn't find my clit either... here let me help you."
    $ the_person.change_arousal( 15 + (mc.oral_sex_skill * 2)) #50 + 4
    $ mc.change_locked_clarity(10)
    "[the_person.title] runs a hand through your hair, then grabs some of it on the back of your head. She begins to gyrate her hips as she grinds into you."
    "You decide to go with it. You flatten your tongue out and begin to move it across her clitoris in long strokes."
    "She grinds herself happily against your face. She moans appreciatively at your skilled oral stimulation."
    $ the_person.change_arousal( 15 + (mc.oral_sex_skill * 2)) #65 + 6
    if the_person.arousal_perc > 100: #She is surprised how fast you make her cum
        "Suddenly, you feel her body go stiff and her moans ramp up quickly."
        the_person "Fuck! I'm gonna... you're gonna make me...!"
        $ mc.change_locked_clarity(20)
        $ the_person.have_orgasm()
        "[the_person.title] convulses as she orgasms. She is caught completely off guard by how fast you made her cum."
        "The hand on the back of your head lets go but you continue your assault for several more seconds."
    else:
        the_person "Mmm, that's it. Your tongue feels so good. Give it a good workout..."
        "[the_person.title]'s hand leaves the back of your head but you keep going. You lightly suck on her clit, drawing it into your mouth a few seconds at a time before licking it again."
        "Her body is responding. Her hips are starting to twitch back and forth on their own as she approaches an orgasm."
        $ the_person.change_arousal( 15 + (mc.oral_sex_skill * 2)) #80 + 8
        if the_person.arousal_perc > 100: #She orgasms
            $ mc.change_locked_clarity(20)
            the_person "Yes! That's it! I'm gonna cum!"
            $ the_person.have_orgasm()
            "[the_person.title] convulses as she orgasms. She moans and runs her hands through your hair."
            "You continue your assault for several more seconds."
        else:   #Not skilled enough to make her orgasm.
            $ mc.change_locked_clarity(10)
            "You are feverishly working at her pussy, but for some reason you can't seem to find the right spot."
            "Soon, the stimulation gets to be too much for her and she puts her hand on your head and slowly pushes it back."
    $ the_person.change_arousal(-30) #50 + 8
    the_person "Mmm, that was a great warm-up. Let me return the favour."
    "[the_person.possessive_title!c] hops down from the sink. She quickly helps you undress, then gets down on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    $ the_person.increase_blowjobs()
    "She gives your cock a few slow strokes before she begins to lick the tip. Her tongue feels like wet velvet as it circles around your glans."
    "[the_person.title] opens her mouth and then envelops the end of your dick with her warm, wet mouth."
    $ mc.change_locked_clarity(20)
    "[the_person.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "It feels amazing, you can tell if you let her keep going you will cum quickly."
    #TODO write blowjob finish scene#
    mc.name "That feels great, but I don't want to finish in your mouth. Why don't you stand up and turn around..."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.effective_sluttiness() > 40: #She asks if you want to use a condom
        the_person "Do you want to put on a condom first?"
        menu:
            "Put on a condom":
                mc.name "Yeah, I'd probably better. I may not be able to resist not pulling out."
                if the_person.effective_sluttiness() > 60:
                    the_person "I mean... it's okay with me if you wanted to stick it in for a little bit without one on, you know, just to get started..."
                    if the_person.effective_sluttiness() > 90:
                        the_person "... or even just finish inside me. I promise I wouldn't mind at all!"
                    mc.name "Maybe next time!"
                "You get a condom and put it on quickly."
                $ mc.condom = True
            "Fuck her raw":
                $ mc.condom = False
                mc.name "No way, I want to feel everything."
                if the_person.effective_sluttiness() > 60:
                    the_person "Mmmm, sounds good. I was hoping you would say that!"
                    if the_person.effective_sluttiness() > 80:
                        "She wiggles her ass back and forth a little bit."
                        the_person "You don't need to worry about pulling out. I like it better when I feel the splash anyway..."
                else:
                    the_person "Okay, just make sure to pull out before you finish, okay?"
    else:
        the_person "You have a condom right? Make sure you put one on..."
        mc.name "Right! I'd probably better. I may not be able to resist not pulling out."
        "You get a condom and put it on quickly."
        $ mc.condom = True
    $ the_person.increase_vaginal_sex()
    "You put your hands on her hips and put your dick at her entrance. She is still soaked from your oral earlier, so you easily slide into her."
    "Her pussy feels amazing wrapped around your erection. Her legs shake a bit as she gets used to the depth of your penetration."
    $ the_person.change_arousal(20) #70 + 8
    $ mc.change_locked_clarity(20)
    the_person "Ohhh, [the_person.mc_title]... That is exactly what I was hoping for when I sent you that text earlier. That feels so good..."
    "You give her a few tentative thrusts, then quickly pick up the pace and begin fucking her in earnest."
    "Your hips slap against [the_person.possessive_title]'s ass as you fuck her vigorously."
    $ the_person.call_dialogue("sex_responses_vaginal")
    if mc.condom:
        "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
        $ the_person.change_arousal(20) #90 + 8
        if the_person.arousal_perc > 100:
            $ the_person.have_orgasm()
            "You can feel [the_person.title]'s pussy begin to spasm as she cums. You can see in the mirror that her mouth is hanging open and her eyes are closed."
        "After the stimulation from her blowjob earlier, you know you aren't going to last long. You give her ass a loud spank."
        mc.name "That's it, bitch. I'm about to cum!"
        if the_person.effective_sluttiness() > 90: #She is so slutty, she begs for your cum.
            the_person "The condom! Take it off! Please!?! Your cock is so good, I want to feel you dump your load inside me!"
            "Your brain is getting a little hazy with lust. Surely there's nothing wrong with that, right?"
            menu:
                "Take It Off":
                    $ mc.condom = False
                    "In one swift motion you pull out of [the_person.title], pull the condom off, then shove yourself deep back inside her."
                    "You wad up the condom then throw it on the counter. It lands with a splat."
                    the_person "Yes! Cum for me! I want to feel it!"
                    $ the_person.change_arousal(20) #110 + 8
                    $ mc.change_locked_clarity(20)
                    "Her excitement is too much. You bottom out and cum, dumping wave after wave of your semen deep inside her."
                    the_person  "Yes! Fill me with your cum!"
                    "You feel her pussy convulsing around your dick as she also starts to orgasm."

                    python:
                        the_person.have_orgasm()
                        the_person.cum_in_vagina()
                        the_person.draw_person( position = "standing_doggy") # draw cum
                        ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)

                    "You wait until your orgasm has passed completely, then pull out and stand back. Your cum leaks from her well-used pussy."
                    "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the locker room."
                    return
                "Leave It On":
                    mc.name "I can't pull out, even for a second!"

        $ the_person.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        "You bottom out and cum, dumping your load into the condom."
        "You wait until your orgasm has passed completely, then pull out and stand back. Your condom is bulged on the end where it is filled with your seed."
        if the_person.arousal_perc < 100:
            the_person "Wow, okay, I guess we are done?"
            $ the_person.change_stats(happiness = -5, obedience = -5)
            "She is a bit disappointed she didn't finish."
        else:
            the_person "That was nice. I'll make sure next time I'm in the mood to hit you up again..."
        "You take your condom off and throw it in the trash can."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
        "You and [the_person.title] get cleaned up and dressed."
        $ mc.change_location(gym)
        "You quietly sneak out of the locker room."
        return
    else: #You went in raw
        $ the_person.cum_in_vagina()
        $ the_person.draw_person( position = "standing_doggy") # draw cum
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        "You push yourself in as deep as you can go. [the_person.possessive_title!c] moans as you fill her completely."
        "With every thrust, her ass ripples pleasantly. You give her cheek an open–handed spank and watch as shockwaves expand from the epicentre."
        "[the_person.title] moans at your rough treatment."
        $ the_person.change_arousal(20) #70 + 8
        if the_person.arousal_perc > 100:
            $ the_person.have_orgasm()
            "You can feel [the_person.title]'s pussy begin to spasm as she cums. Her silky wetness contracting around you feels amazing."

    if the_person.effective_sluttiness() > 70:
        the_person "You should umm, you know, stick a finger in my other hole..."
        "Wow, it's not every day you have a beautiful woman ask you to finger her ass while you bend her over and fuck her!"
        "You reach a hand forward and put your index finger in front of her face. She quickly gets the idea and opens her mouth with her tongue out, and begins slathering your finger with saliva."
        "When satisfied, you bring you finger back to her tight back passage. You pull your cock almost completely out and stop you hip motion as you begin to press your finger against [the_person.title]'s puckered hole."
        "She forces her sphincter to relax and your finger begins to slip inside her."
        the_person "Ohh, yes. You can move your hips, that feels good..."
        $ mc.change_locked_clarity(30)
        "You give [the_person.possessive_title]'s cunt a few slow thrusts, while simultaneously fingering her other hole."
        $ the_person.change_arousal(20)#90 + 8
        if the_person.arousal_perc > 120:
            the_person "OH! It's so good... fuck I'm gonna cum again!!!"
            "You get the now familiar feeling of [the_person.title] cumming around your cock, but this time you can also feel the waves around your finger."
            "You wonder what it would feel like to make her cum again, but with your cock in her ass instead..."
            menu:
                "Stay Vaginal":
                    "As [the_person.title]'s pussy quivers around you, you decide to just keep doing what you are doing."
                "Fuck Her Ass" if the_person.effective_sluttiness() >= 70:
                    "You pull out of her pussy. Her juices leave a strand attached to you, connecting you to her cunt."
                    the_person "Mmm, [the_person.mc_title]? Why did you pull out... OH!"
                    "Her question is swiftly answered when she feels your manhood poking her puckered hole."
                    if the_person.effective_sluttiness() > 90:
                        the_person "Yes! Fuck my ass good!"
                    else:
                        the_person "Oh my... be careful!"
                    $ the_person.increase_anal_sex()
                    "With your hands firmly on her hips, you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
                    the_person "Oh god you make me feel so dirty... I love it!"
                    $ mc.change_locked_clarity(30)
                    "You fuck her hard but at a steady, even pace."
                    "[the_person.possessive_title!c] moans, matching each hip movement of yours with a movement of her own."
                    the_person "It feels so deep... I can't... my legs!"
                    "Her knees give out, but you are too close to stop fucking her. You grab her hips roughly and pick up the pace."
                    $ the_person.change_arousal(20)#110 + 8
                    "Her ass begins to spasm. Her buttery smooth back passage squeezes you over and over as her body is racked with yet another orgasm. It feels incredible."
                    $ the_person.change_stats(happiness = 5, slut = 2)
                    mc.name "Get ready, I'm gonna cum!"
                    "[the_person.title] is incoherent, and doesn't process your words."
                    "You plunge deep into her ass and hold it there while you cum. She gasps in time with each new shot of hot semen inside her."
                    $ the_person.cum_in_ass()
                    $ the_person.draw_person(position = "standing_doggy") # draw cum
                    $ ClimaxController.manual_clarity_release(climax_type = "anal", person = the_person)

                    "You stand there for a minute, holding her hips in the air, you dick buried in her bowel as it softens. Eventually she speaks up."
                    the_person "Wow... okay... I think I can stand now..."
                    "You slowly let her down. Her legs buckle for a second, but she catches herself."
                    "You see a faint trace of your semen running down the back of her leg."
                    the_person "That was {i}so{/i} good. You'll be hearing from me again, I'm sure... I came so many times..."
                    $ the_person.apply_planned_outfit(show_dress_sequence = True)
                    "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed."
                    $ mc.change_location(gym)
                    "You quietly sneak out of the locker room."
                    return
                "Fuck Her Ass\n{menu_red}Requires 80 sluttiness{/menu_red} (disabled)" if the_person.effective_sluttiness() < 80:
                    pass
    "[the_person.possessive_title!c]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    mc.name "Get ready, I'm gonna cum!"
    $ the_person.change_arousal(35)
    if the_person.effective_sluttiness() > 90:
        "To your surprise [the_person.title] reaches back with both hands and grabs your hips, pulling you deep inside her."
        "Her grip is startlingly strong. You don't think you could pull out even if you wanted to!"
        $ mc.change_locked_clarity(30)
        the_person "That's it, cum with me!"
        "Your cum erupts in a torrent. Your seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
        python:
            the_person.have_orgasm()
            the_person.cum_in_vagina()
            the_person.draw_person( position = "standing_doggy") # draw cum
            ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        "You wait until your orgasm has passed completely, then pull out and stand back. Your cum leaks from her well-used pussy."
    elif the_person.effective_sluttiness() > 60:
        the_person "Oh god... you should probably pull out but... it feels so good..."
        $ mc.change_locked_clarity(30)
        "You briefly consider pulling out."
        menu:
            "Pull Out":
                "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
                the_person "Oh! It's so hot on my skin!"
                $ the_person.cum_on_ass()
                $ the_person.draw_person(position = "standing_doggy")
                $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)

                "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
            "Creampie":
                "Her pussy feels too good. You bottom out and cum, dumping wave after wave of your semen deep inside her."
                "Your seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
                python:
                    the_person.have_orgasm()
                    the_person.cum_in_vagina()
                    the_person.draw_person(position = "standing_doggy")
                    ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
                "You wait until your orgasm has passed completely, then pull out and stand back. Your cum leaks from her well-used pussy."
    else:
        "[the_person.title] suddenly moves her hips forward, your cock slides out of her."
        the_person "Cum on my ass!"
        "You stroke your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        $ the_person.cum_on_ass()
        $ the_person.draw_person(position = "standing_doggy")
        $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
        "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."

    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed."
    $ mc.change_location(gym)
    "You quietly sneak out of the locker room."
    return

#label erica_cum_face(the_person):
#    if the_person.obedience > 180:
#        if the_person.effective_sluttiness() > 60:
#            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
#            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
#        else:
#            the_person "I hope this means I did a good job."
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    else:
#        if the_person.effective_sluttiness() > 80:
#            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
#        else:
#            the_person "Fuck me, you really pumped it out, didn't you?"
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    return

label erica_cum_mouth(the_person):
    if mc.is_at(gym) or the_person.has_cum_fetish:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 70 or the_person.opinion.drinking_cum > 1:
            the_person "Your cum tastes great [the_person.mc_title]! Thanks for giving me so much extra protein!"
            $ play_swallow_sound()
            "[the_person.possessive_title!c] winks at you as she swallows your load."
        elif the_person.effective_sluttiness() > 50 or the_person.opinion.drinking_cum > 0:
            the_person "Thanks, [the_person.mc_title]. I could really use the extra protein after that workout!"
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title]. It doesn't taste the best, but I could always use a little extra protein."
    elif the_person.obedience > 180:
        if the_person.effective_sluttiness() > 60 or the_person.opinion.drinking_cum > 0:
            the_person "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.opinion.drinking_cum > 0:
            the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person "Bleh, I don't know if I'll ever get used to that."
    return

#label erica_surprised_exclaim(the_person):
#    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
#    the_person "[rando]"
#    return

label erica_talk_busy(the_person):
    if mc.is_at(gym):
        the_person "Hey, I'm really sorry, but I need to keep my workout going. Maybe another time?"
    if the_person.obedience > 120:
        the_person "Hey, I'm really sorry, but I've got some stuff I need to take care of. Could we catch up some other time?"
    else:
        the_person "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
    return

#label erica_sex_strip(the_person):
#    if the_person.effective_sluttiness() < 20:
#        if the_person.arousal < 50:
#            the_person "Let me get this out of the way..."
#        else:
#            the_person "Let me get this out of the way for you..."
#
#    elif the_person.effective_sluttiness() < 60:
#        if the_person.arousal < 50:
#            the_person "This is just getting in the way..."
#        else:
#            the_person "Ah... I need to get this off."
#
#    else:
#        if the_person.arousal < 50:
#            the_person "Let me get this worthless thing off..."
#        else:
#            the_person "Oh god, I need all of this off so badly!"

#    return

label erica_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if not the_person.is_stranger else "The stranger"
    if the_person.effective_sluttiness() < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry", display_transform = character_left_flipped)
        $ the_person.call_dialogue("surprised_exclaim")
        the_person "Are you really doing this in front of everyone?"
        $ the_person.change_stats(happiness = -1, obedience = -2)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.effective_sluttiness() < the_position.slut_requirement - 10:
        $ the_person.draw_person(display_transform = character_left_flipped)
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze while you and [the_sex_person.fname] [the_position.verb]."
        return False

    if the_person.effective_sluttiness() < the_position.slut_requirement:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "You two are just... Wow..."
        $ the_person.change_slut(1, 30)
        "[title] averts her gaze, but keeps glancing over while you and [the_sex_person.fname] [the_position.verb]."
        return True

    if the_person.effective_sluttiness() > the_position.slut_requirement and the_person.effective_sluttiness() < the_position.slut_cap:
        $ the_person.draw_person(display_transform = character_left_flipped)
        if not is_watching(the_person):
            $ the_person.call_dialogue("surprised_exclaim")
            the_person "That's... Wow that looks... Hot."
        $ the_person.change_slut(1, 50)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."
        return True

    $ the_person.draw_person(emotion = "happy", display_transform = character_left_flipped)
    if renpy.random.randint(0, 1) == 0:
        the_person "Come on [the_person.mc_title], you can give her fit ass more than that."
    else:
        call watcher_position_comment(the_person, the_sex_person, the_position) from _call_watcher_position_comment_erica_sex_watch
    "[title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."
    return True

label erica_being_watched(the_person, the_watcher, the_position):
    $ title = the_watcher.fname if not the_watcher.is_stranger else "the stranger"
    if the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Don't listen to [title], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [title] watching you and her [the_position.verb]."

    elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_stats(arousal = -1, slut = -1)
        "[the_person.title] seems uncomfortable with [title] nearby."

    else: #the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title!c] looks at [title] and says..."
        the_person "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [title] around."

    return

label erica_work_enter_greeting(the_person):
    if the_person.happiness < 80:
        if the_person.obedience > 120:
            "[the_person.title] gives you a curt nod and then turns back to what she was doing."
        else:
            "[the_person.title] glances at you when you enter the room then looks away quickly to avoid starting a conversation."

    elif the_person.happiness > 120:
        if the_person.effective_sluttiness() > 50:
            "[the_person.title] looks up from her work when you enter the room."
            the_person "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
            "She smiles and winks, then turns back to what she was doing."
        else:
            "[the_person.title] turns to you when you enter the room and shoots you a smile."
            the_person "Hey, good to see you!"

    else:
        if the_person.obedience < 90:
            "[the_person.title] glances up from her work."
            the_person "Hey, how's it going?"
        else:
            "[the_person.title] waves at you as you enter the room."
            the_person "Hey, let me know if you need anything [the_person.mc_title]."
    return

label erica_date_seduction(the_person):
    $ mc.change_locked_clarity(30)
    if the_person.effective_sluttiness() > the_person.love:
        if the_person.effective_sluttiness() > 40:
            the_person "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
            # the_person "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
        else:
            the_person "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
            #the_person "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
    else:
        if the_person.love > 40:
            the_person "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
        else:
            the_person "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
    return

## Role Specific Section ##
label erica_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
    mc.name "Go on, I'm interested."
    the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return
