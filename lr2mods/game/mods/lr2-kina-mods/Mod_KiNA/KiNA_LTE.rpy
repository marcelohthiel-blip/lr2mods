#Counter = KLTE01

#Limited Time Event

label chat_break_label(the_person):
    if mc.is_at_work:
        if the_person.is_employee:
            "As you walk around the office you saw [the_person.fname] taking a break making herself coffee."
            the_person "Hey [the_person.mc_title], want some coffee? I'm a bit sleepy today."
            the_person "Are you busy? Why not join me here? I just need a 5 minutes break, I promised."
    elif mc.is_home:
        if the_person in people_in_mc_home():
            "As you are walking down the hallway in your house you heard your name called by [the_person.fname]."
            the_person "Hey [the_person.mc_title], gimme a hand please. Need to move this thing over here. And it's heavy by myself."
    else:
         "As you are wandering around you saw [the_person.fname] sitting idly by.."
         the_person "Are you busy? Come join me here. Just chilling."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "sitting")    
    "You think for a while and decided to join her. Getting to know her more would be nice."
    "..."
    "As you spend time with her, the idle chats continue from topics to topics."
    if the_person.effective_sluttiness() > 60: #She is pretty comfortable talking about sexy stuff with you
        $ her_opinion = the_person.get_random_opinion(include_known = False, include_sexy = True)
    else:
        $ her_opinion = the_person.get_random_opinion(include_known = False, include_sexy = False)
    if her_opinion:
        $ the_person.discover_opinion(her_opinion)
        $ opinion_string = opinion_score_to_string(the_person.opinion(her_opinion))
        "She openly admits that she [opinion_string] [her_opinion]."
    else:
        #We know everything.
        "You don't learn anything new, but she probably more willing to sharing her wilder fantasy if she is less inhibit by her morality."
    "After a while, you excuse yourself and leave."
    $ the_person.change_stats(happiness = 2, love = 1, obedience = -1)
    $ scene_manager.clear_scene()    
    return

label family_accept_incest_label(the_person):

    if the_person == mom:
        #$ mom_bedroom.show_background()
        
        if ((the_person.sex_record.get("Orgasms", 0) > 20) and the_person.known_opinion.incest == -2):
            $ the_person.draw_person(position="sitting")
            "You see [the_person.possessive_title] staring absentmindedly at the ceiling."
            mc.name "Earth to [the_person.title]... Is everything alright?"
            the_person "*gasps*"
            the_person "How long have you been there?"
            mc.name "A while... You okay?"
            "[the_person.possessive_title!c] seems to steel herself before she looks back at you."
            the_person "Everything is fine, it's just that... well... {i}We really should stop doing that{/i}."
            mc.name "Do {i}what{/i}?"
            the_person "You know... having sex."
            mc.name "Ah..."
            the_person "What if other people found out?"
            "You pull her makeup chair over and sit in front of her."
            "Holding both her hands, you ask:"
            mc.name "So what if they knew? Why do other people matter?"
            the_person "Of course it matters. And we really shouldn't. It's not right—guys shouldn't want to do that with their own mother..."
            the_person "You... You should be having sex with people your age. Not with {i}me{/i}..."
            mc.name "I don't mind having sex with you. No, I *want* to have sex with you. I think you're {i}beautiful{/i}. And fucking sexy."
            the_person "You... you do?"
            "You hold her hands tighter."
            mc.name "[the_person.fname]... Do you hate having sex with me that much?"
            the_person "That's not... I don't... But... peo—"
            mc.name "Then screw people. We don't need to tell anyone. It'll be our little {i}family secret{/i}."
            "[the_person.possessive_title!c] seems torn."
            the_person "I... I don't know..."
            "You give her a calming, reassuring hug. And a kiss on top of her head."
            mc.name "That's just the way we are. We're just more physical in how we express our love."
            "It takes a while to convince her, but at least she no longer hates incest."
            $ the_person.weaken_opinion("incest")
    
        elif ((the_person.cum_exposure_count > 20) and the_person.known_opinion.incest == -1):
            $ the_person.draw_person(position = "walking_away")  
            "[the_person.possessive_title!c] seems to be energetic lately."
            "You decided to approach her from behind and gave her a hug."
            mc.name "Somebody is quite perky today."
            "Your hand grabs her boobs and starts to play with them while giving her neck a light kiss."
            $ the_person.change_arousal(4 + mc.foreplay_sex_skill)
            $ mc.change_locked_clarity(10)
            $ the_person.draw_person(position = "back_peek", emotion = "happy")
            the_person "Naughty guy... I'm your mother~ {i}*gasps*{/i} Ohh.. that tickles!"
            mc.name "I sort of recall {i}someone{/i} hating me doing this before."
            the_person "Well, I figure - as you said, if no one knows - then, it's a secret. Just between us."
            the_person "Might as well enjoys it."
            the_person "And, honestly.."
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "Her hand snakes over your pants, her cheeks reddens..."
            the_person "This thing is so much fun to play with."
            mc.name "Is that so?"
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KHH03
            $ the_report = _return
            "Your hard work -or rather hard cock- seducing [the_person.possessive_title] is paying off."
            "It seems like [the_person.possessive_title] no longer bothered having incestual relationship with you."
            $ the_person.weaken_opinion("incest")
            #$ the_person.update_opinion_with_score("incest", 0, add_to_log = True)
            #"No opinion incest"
            
        elif ((the_person.sex_record.get("Vaginal Creampies", 0) > 20) and the_person.known_opinion.incest == 0):
            "[the_person.possessive_title!c] notices you immediately as you enter."
            $ the_person.draw_person(position="stand2", emotion="happy")
            if time_of_day == 0:
                the_person "Good morning, sweetheart!"
                mc.name "Morning."
            else:
                the_person "How's your day, darling?"
                mc.name "Couldn't be better."
            mc.name "Someone's happy."
            the_person "{i}Someone{/i} is happy to see you."
            "You take a step toward [the_person.possessive_title], and she opens her arms to pull you into a hug."
            mc.name "Oh, why is that?"
            "Her body is soft—you can feel her breasts pressing against your chest. She lets out a slow, hot breath on your neck."
            "Your hands slip down to her waist, then to her butt. For someone her age, her butt is surprisingly firm."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            the_person "You know why..."
            "You cup one of her buttocks and slowly drag your lips across her neck, taking in the familiar scent of her perfume."
            "She's always wearing this one. It smells sweet, like lavender."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            "You pull your head back, and for a moment, your eyes meet."
            the_person "[the_person.mc_title!c]..."
            the_person "I'm your mother..."
            mc.name "Again thi—"
            "She places a finger over your lips, silencing you."
            the_person "I know it's not right..."
            the_person "But... I don't care."
            "You feel her hand over your crotch, gently caressing your erection through your pants."
            the_person "I like it... when it ravages my insides."
            the_person "Promise your mother you'll keep doing her... Keep {i}me{/i} satisfied."
            if mc.energy > 80 and the_person.energy > 40:
                mc.name "No need to ask me twice."
                call fuck_person(the_person, private=True, start_position=kissing, skip_intro=True) from _call_fuck_person_KHH04
                $ the_report = _return
            elif mc.energy < 80:
                mc.name "I'd strip and take you right now, but I'm spent."
                if time_of_day == 0:
                    the_person "Oh no, maybe you should take the day off? You must be overworked."
                    "You give her a light kiss."
                    mc.name "I could use a healthy breakfast."
                    "She grabs a handful of your butt, giving it a good squeeze before slapping it hard."
                    the_person "Go have your shower. I'll get your breakfast ready."
                else:
                    the_person "Do you want me to give you a massage?"
                    "You give her a light kiss."
                    mc.name "It's fine. Nothing beats a good night's sleep."
                    mc.name "Good night."
            elif the_person.energy < 40:
                mc.name "I promise. I'd prove it right now if you weren't so tired."
                mc.name "Do you want me to give you a massage?"
                if time_of_day == 4:
                    mc.name "Come on. Lay down on your bed. I'll give you a massage."
                    $ the_person.draw_person(position="walking_away")
                    "You spend some time massaging her."
                    $ the_person.change_arousal(4 + mc.foreplay_sex_skill)
                    $ mc.change_locked_clarity(10)
                    mc.name "Good night."
            "[the_person.possessive_title!c] now favors incest with you."
            "She's almost yours. Consummate this relationship with the ultimate prize."
            "A baby."
            $ the_person.create_opinion("incest")
            # "Liked incest"
            
        elif ((the_person.knows_pregnant and the_person.is_mc_father) and the_person.known_opinion.incest == 1):  
            $ the_person.draw_person(position = "sitting", emotion = "happy")  
            "You saw your mother absent mindedly caressing her growing belly." 
            "As you approached her, her smile widens."
            if time_of_day == 0:
                the_person "Good morning, Sweetheart!"
                mc.name "Morning, beautiful. Did you have a good sleep?"
                mc.name "Don't tire yourself out, it's not good for our baby."
            else:
                the_person "How's your day, darling?"
                mc.name "Couldn't be better."
                mc.name "Did the little one misbehaving inside there?"
            "You kneeled next to her and put your ear on her belly."
            if the_person.pregnancy_is_visible:
                "You can feel the baby moving around excitedly, likely feeling you closeby."
            else:
                "I don't think you can hear her... yet."
                mc.name "Her?"
                the_person "I can feel it. Her."
            "[the_person.possessive_title!c] gently runs her hand through your hair."
            "The room filled with silence, both of you enjoying this moment together."
            the_person "You know, never in my life, I'd imagined that I'll be pregnant with my own son's child."
            mc.name "Regret?"
            the_person "I don't regret it. Not this. Not us."
            "She sighed, looking at you."
            the_person "How do we go on like this? When peoples start noticing..."
            "You brushed a strand of hair from her face."
            mc.name "We keep going, one day at a time. We protect our family, no matter what. We love each other, and we love this baby. That's all that matters. As long as we are together."
            "She nods."
            the_person "Together."
            "She echoed, her resolve strengthening."
            "You hug her lovingly."
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "Her body was soft, and her cloth was thin and insubstantial."
            "You pulled [the_person.possessive_title] against you, feeling her breasts rubbing against your chest."
            "[the_person.possessive_title!c] let out a slow, hot breath on your neck."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            the_person "Husband..."
            "She lifted one of her legs, wrapping it around your waist, grinding your lower half."
            "You brought your lips to hers and felt her kissing you back, raw passion exploding as both tongues flicked out to greet each other."
            #burst of energy because sex!
            if the_person.energy < the_person.max_energy:
                $ the_person.energy = the_person.max_energy
            if mc.energy < mc.max_energy:
                $ mc.energy = mc.max_energy
            call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KHH05
            $ the_report = _return
            mc.name "I love you, mother."
            "She gazed at you lovingly before replying..."
            the_person "And I love you too, son."
            "[the_person.possessive_title!c] now love incest with you."
            "She no longer be bothered with other peoples opinion regarding her fucking her own son."
            $ the_person.strengthen_opinion("incest") 
            "And the baby will be the ultimate proof of your relationship."
            #$ the_person.update_opinion_with_score("incest", 2, add_to_log = True)
            #"Loved incest"
        else:
            #Should never triggers
            pass
    else:
        #$ lily_bedroom.show_background()
        
        if ((the_person.sex_record.get("Orgasms", 0) > 20) and the_person.known_opinion.incest == -2):
            $ the_person.draw_person(position = "sitting")  
            "As you enter her room, you saw [the_person.possessive_title] was watching something on her laptop."
            "She didn't realized you entering, so you managed to get close to see what see is watching."
            "It was a porn video. More specifically a porn about a brother and his sexy little sister."
            mc.name "Interesting..."
            the_person "*gasps*"
            the_person "How long have you been there?"
            mc.name "A while...So, researching? About us?"
            "She shuffles around nervously for a moment before speaking."
            the_person "I mean what our friends would think if they find out? They would think we're crazy!"
            the_person "I'm sure you are capable to get yourself a girlfriend. Someone that not your sister."
            the_person "Why would you do that? With me?"
            mc.name "Why? Why not? We both liked it, right?"
            "She shrugs non-committally."
            the_person "Sure, but you're my brother. It's a little weird."
            "You give her a calming, reassuring hug."
            mc.name "We are weird, and we don't need to make a big deal about it. It's just the way we are."
            the_person "Fine, whatever. But if you tell anyone I'll deny it!"
            "It takes a while to convince her, but at least she no longer hates incest."
            $ the_person.weaken_opinion("incest")
            
        elif ((the_person.cum_exposure_count > 20) and the_person.known_opinion.incest == -1):
            $ scene_manager = Scene()
            $ scene_manager.add_actor(the_person)
            "You heard music coming from [the_person.possessive_title]'s room."
            "As you enter, she was spinning around.."
            $ scene_manager.update_actor(the_person, position = "kissing")
            "[the_person.possessive_title!c] is dancing?"
            "Noticing you, she quickly holds out her hand to you, inviting you to join."
            $ the_person.change_arousal(10)
            $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_left_flipped)
            "You join her, just going with the flow, moving [the_person.possessive_title] away from you a bit and allowing her to make a graceful spin back to you."
            $ the_person.change_arousal(10)
            $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
            "She spins beautifully and stops with her back to you. She looks back and gives you a sly smile."
            $ the_person.change_arousal(10)
            $ scene_manager.update_actor(the_person, position = "kissing")
            "You easily lead her into a reverse spin out the other side as she gracefully finishes her spinning before returning to you."
            $ scene_manager.update_actor(the_person, position = "default")
            $ the_person.change_arousal(10)
            "[the_person.title] whispers in your ear."
            the_person "Fuck... I'm horny~"
            mc.name "Well that escalated quickly."
            "Your hand roams on her back and her petite ass while giving her neck a light kiss."
            $ the_person.change_arousal(4 + mc.foreplay_sex_skill)
            $ mc.change_locked_clarity(10)
            $ the_person.draw_person(position = "back_peek", emotion = "happy")
            the_person "I blamed you~"
            mc.name "I sort of recall you saying its weird."
            the_person "Oh shut up, that's not... I mean, it was back then."
            the_person "Now..."
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "Her hand snakes over your pants, her cheeks reddens."            
            the_person "Fuck, I can't believe I'm going to say this."
            the_person "I - want — this — thing."
            mc.name "Is that so?"
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KHH06
            $ the_report = _return
            "It seems like [the_person.possessive_title] no longer bothered with incest. With you."
            $ the_person.weaken_opinion("incest")
            #$ the_person.update_opinion_with_score("incest", 0, add_to_log = True)
            #"No opinion incest"
            
        elif ((the_person.sex_record.get("Vaginal Creampies", 0) > 20) and the_person.known_opinion.incest == 0):
            $ the_person.draw_person(position = "sitting", emotion = "happy") 
            "[the_person.possessive_title!c] noticed you immediately as you enter."
            $ the_person.draw_person(position = "stand2", emotion = "happy") 
            if time_of_day == 0:
                the_person "Good morning, [the_person.mc_title]!"
                mc.name "Morning."
            else:
                the_person "How's your day, darling?"
                mc.name "Couldn't be better."
            mc.name "Somebody is happy."
            the_person "{i}Somebody{/i} is happy to see you."
            "You took a step toward [the_person.possessive_title], and she opened her arms to pull you into a hug."
            mc.name "Oh, why is that?"
            "Her body was soft, you can feel her breasts rubbing against your chest. She let out a slow, hot breath on your neck."
            "Your hands slipped down to her waist, and then to her butt. You always love how good her butt feels in your hands."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            the_person "You know why..."
            "You cupped one of her buttocks in your hand and slowly dragged your lips across her neck, smelling her familiar scent."
            "She hasn't bath. You always get aroused by her scent."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            "You pulled back your head, and for a moment, both of you met each other eye to eye."
            the_person "Well, it might sound cheesy..."
            the_person "But... but but but... What if, what if I say I missed you?"
            mc.name "We lived in the same-"
            "You find her finger above your mouth, shushing."
            the_person "I want to be close to you always."
            "You can feel her hand over your dick, caressing it over your pants."
            the_person "Well {i}-technically-{/i} close to your dick. I don't really want to be seen with my brother all the time."
            "She stuck her tongue out and grinned."
            mc.name "Sorry, but I only come as a whole package."
            mc.name "Speaking of cum..."
            "You lift her up and lay her on her bed."
            "She giggled but quickly closed her mouth with her free hand."
            #burst of energy because sex!
            if the_person.energy < the_person.max_energy:
                $ the_person.energy = the_person.max_energy
            if mc.energy < mc.max_energy:
                $ mc.energy = mc.max_energy
            if the_person.vagina_available:
                "She eagerly spread her legs for you."
                the_person "Cum in me then! Mark me as yours!"
            else:
                $ the_person.strip_to_vagina(prefer_half_off = False, position = "missionary")
                "She eagerly pulls her panty off before spreading her legs for you."
                the_person "Mark me as yours! Cum in your sister!"
                $ mc.change_locked_clarity(10)
            call fuck_person(the_person, private = True, start_position = missionary, start_object = make_bed(), skip_intro = True) from _call_fuck_person_KHH08
            $ the_report = _return
            "[the_person.possessive_title!c] now favors incest with you."
            $ the_person.create_opinion("incest")
            #"Liked incest"
            
        elif ((the_person.knows_pregnant and the_person.is_mc_father) and the_person.known_opinion.incest == 1):
            $ the_person.draw_person(position = "stand2", emotion = "happy")  
            if the_person.pregnancy_is_visible:
                "You saw your sister admiring her pregnant belly in front her mirror." 
            else:
                "Your sister seems to look for any noticeable change to her belly in front her mirror."
            "She caught your reflection approaching her, earning you an enchanting smile."
            if time_of_day == 0:
                the_person "Good morning, Sweetheart!"
                mc.name "Morning, beautiful. Did you have a good sleep?"
                mc.name "Don't tire yourself out, it's not good for our baby."
            else:
                the_person "How's your day, darling?"
                mc.name "Couldn't be better."
                mc.name "Did the little one misbehaving inside there?"
            "You kneeled next to her and put your ear on her belly."
            if the_person.pregnancy_is_visible:
                "You can feel the baby moving around excitedly, likely feeling you closeby."
            else:
                the_person "I don't think you can hear her... yet."
                mc.name "Her?"
                the_person "I can feel it. Her."
            "[the_person.possessive_title!c] gently runs her hand through your hair."
            "The room filled with silence, both of you enjoying this moment together."
            the_person "You know, I didn't expect to be a mother so early, nor did I expect that I'd be pregnant with my own brother's child."
            the_person "But... I don't regret it one bit."
            the_person "You are so good to me."
            "[the_person.possessive_title!c]’s voice was soft, something you never expected of her."
            "You’re practically my husband now, [the_person.mc_title]."
            mc.name "And you are my wife, [the_person.fname]."
            "You hug her warmly."
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "Her body was soft, and her cloth was thin and insubstantial."
            "You pulled [the_person.possessive_title] against you, feeling her breasts rubbing against your chest."
            "[the_person.possessive_title!c] let out a slow, hot breath on your neck."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(10)
            the_person "As my husband, you are dutybound to your wife..."
            "She parted one of her legs, giving you an even better angle to access her. "
            "You brought your lips to hers and felt her kissing you back, raw passion exploding as both tongues flicked out to greet each other."
            #burst of energy because sex!
            if the_person.energy < the_person.max_energy:
                $ the_person.energy = the_person.max_energy
            if mc.energy < mc.max_energy:
                $ mc.energy = mc.max_energy
            call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KHH07
            $ the_report = _return
            mc.name "I love you, sis."
            "She gazed at you lovingly before replying..."
            the_person "I love you too, brother."
            "[the_person.possessive_title!c] now love incest with you."
            "She no longer be bothered with other peoples opinion regarding her fucking her own brother."
            $ the_person.strengthen_opinion("incest") 
            #$ the_person.update_opinion_with_score("incest", 2, add_to_log = True)
            #"Loved incest"
        else:
            pass
    $ clear_scene()
    return