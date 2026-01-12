label study_friend_transition(the_sister, the_person):
    $ scene_manager = Scene()
    if the_person.event_triggers_dict.get("anger", 0) == 0:
        $ lily_transition_followup = Action("Lily Transition Followup", lily_mon_followup_requirement, "lily_transition_followup_label")
        $ mc.business.add_mandatory_crisis(lily_transition_followup)
        $ the_person.event_triggers_dict["anger"] = 0
        $ happy = 10
        the_person "[the_person.mc_title], can we talk?"
        mc.name "Sure, what's up?"
        if the_person.event_triggers_dict.get("study_sessions", 0) > 6:
            the_person "I've been having a lot of fun with you the last few months, but..."
        else:
            the_person "I've been having a lot of fun with you the last few weeks, but..."
        if the_person.has_role(girlfriend_role):
            the_person "There's no easy way to say this, so I'll just say it: I think we should break up."
        else:
            the_person "There's no easy way to say this, I just don't see a real future for us together. I wanted to stop things before they develop further."
        $ scene_manager.add_actor(the_person, emotion = "sad")
        menu:
            "Be dismissive":
                mc.name "Oh, that's fine. I was thinking the same thing actually."
                the_person "Oh... um... well I've been developing feelings for someone else... and..."
                mc.name "That's fine, I hope they make you happy."
                if the_person.has_role(girlfriend_role):
                    the_person "Nothing happened."
                    mc.name "I believe you, it's fine. We are both young, plenty of fish and all that."
            "Be understanding":
                mc.name "Oh, really?"
                the_person "I'm sorry I just don't feel a spark, I think I want to see what else is out there."
                mc.name "Oh, well okay. School is a great time to explore. I hope you can find happiness."
                the_person "Thanks, you too."
            "Get angry":
                $ happy +=10
                $ the_person.event_triggers_dict["anger"] += 1
                if the_person.has_role(girlfriend_role):
                    mc.name "You're breaking up with me? I'm the best thing that ever happened to you."
                    the_person "I'm not sure that's true, but I think I'm looking for something else."
                    mc.name "Oh yeah, what is his name? Have you already started cheating on me?"
                    $ scene_manager.update_actor(the_person, emotion = "angry")
                    the_person "It's not like that, nothing happened."
                    mc.name "Oh, but there is someone else? One of the other students?"
                    the_person "What... no."
                    "It seems like you might have hit pretty close to the mark there, but she doesn't seem like she is going to elaborate."
                if the_person.number_of_children_with_mc > 0:
                    if the_person.number_of_children_with_mc > 1:
                        mc.name "What about our kids?"
                    else:
                        mc.name "What about our kid?"
                    the_person "I'm not going to spend the next 20 years with someone just so they can have their parents in the same house."
                    the_person "We'll figure something out if you actually want to be a part of their life."
        the_person "I'm sorry, but it's just the way things are."
        menu:
            "Let her go":
                $ scene_manager.update_actor(the_person, emotion = "sad")
                mc.name "I guess this is goodbye?"
                the_person "Well I'll still be around, but probably going to stick to your sister's room a bit more when we study."
            "Be cruel":
                $ happy +=10
                $ the_person.event_triggers_dict["anger"] += 1
                mc.name "Well at least now I don't have to keep hiding my other girls from you."
                mc.name "I've got this one, you should see her..."
                $ scene_manager.update_actor(the_person, emotion = "angry")
                if not the_person.has_large_tits:
                    mc.name "You can actually tell she is a girl with tits big enough to find under her shirt."
                elif the_person.body_type == "curvy_body":
                    mc.name "She actually takes care of herself, not waddling around like your fat ass."
                elif the_person.int < 3:
                    mc.name "In addition to the body she has a brain, I never have to explain things to her."
                else:
                    mc.name "She should be a model, not like your ugly mug."
                mc.name "I can't believe I put up with you so long."
                the_person "I can't believe I was agonizing over this decision, I should have made it weeks ago."
        $ the_person.remove_role(girlfriend_role)
        $ the_person.change_stats(love = -40, happiness = -happy)
    else:
        the_person "Yeah, your sister ran out of note cards again. I think she wants us to talk."
        if the_person.event_triggers_dict.get("anger", 0) > 1:
            mc.name "Because it worked so well last time?"
            the_person "I know, but I think she is worried about me, and probably about you too."
            mc.name "She does have a tendency to care about the people around her."
            the_person "Yeah, she can be annoyingly great that way..."
            "The conversation stalls as you both reflect on what has happened."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "I'm leaving."
            mc.name "No, wait we can talk."
            the_person "I don't just mean right now, I... I'm transferring schools. There is too much baggage here, and it's really easy to change schools this early."
            "That is pretty huge, you could probably stop her if you wanted to, but she might be gone forever after this."
            menu:
                "Let her go":
                    mc.name "That's... a big step, but if you think you need to go I'm not going to stop you."
                    the_person "I didn't figure you would, I just feel bad about [the_sister.fname]. I don't want her blaming herself."
                    mc.name "I'll talk to her, that is at least one thing we can agree on. I'll make sure she is okay."
                    the_person "Thanks, and well goodbye I guess."
                    mc.name "Goodbye."
                    $ the_person.remove_person_from_game()
                    "Things sort of spiralled out of control there. [the_sister.title] is going to need a new study buddy. You'll have to see who it is next week."
                    $ get_lab_partner()
                "Stop her":
                    mc.name "Wait, you don't need to do that. We can get past this."
                    the_person "Can we? Really?"
                    mc.name "Look, [the_sister.fname] really likes spending time with you and I don't want to break that up."
                    mc.name "I could have handled this better, why don't we give it another week and see if things can get better."
                    the_person "Okay, I'll see you next week I guess."
                    "Things are better, but if you really want to patch things up you are probably going to have to apologise next week."
                    $ the_person.change_happiness(10)
                    $ the_person.event_triggers_dict["anger"] -= 1
        else:
            mc.name "Yeah, sure. Maybe you'd like to mooch off of me some more."
            $ scene_manager.update_actor(the_person, emotion = "angry")
            the_person "It's not like that, she knows things are broken between us it is upsetting her."
            "Things are a bit rough, but you could probably salvage the situation if you are willing to be the bigger person."
            menu:
                "Apologise":
                    mc.name "I know, she can care so much. It is one of the best things about her."
                    $ scene_manager.update_actor(the_person, emotion = "sad")
                    the_person "Something we can agree on, she really is great."
                    mc.name "Look, for what it's worth I am sorry. I got carried away in the moment."
                    the_person "You did let a bit of rage show, but I was breaking up with you, can't expect something like that to go well."
                    mc.name "I still should have handled it better, really I am sorry. Can we put that behind us, maybe be friends."
                    the_person "I think I'd like that, after all, I'm still going to be hanging around with your sister all the time."
                    mc.name "Right, that's good. I guess I'll see you next week."
                    the_person "Yeah, thanks [the_person.mc_title]."
                    $ the_person.event_triggers_dict["anger"] -= 1
                    $ the_person.change_happiness(20)
                    $ town_relationships.improve_relationship(the_person, the_sister)
                "Taunt her":
                    mc.name "Remind me whose fault that is? You're the one who broke things."
                    the_person "I know, but that doesn't mean we can't be civil."
                    mc.name "Civil? Tell me, did you find the something else you were looking for? Is he rocking your world?"
                    the_person "Look, I'm trying to salvage this for [the_sister.fname], surely you care about her even if you don't care about me."
                    mc.name "She's a big girl, if she wants us to get along she'll just have to be unhappy."
                    the_person "Fine, whatever, I can't believe I thought this would work. Hopefully she won't make me do this again next week."
                    $ the_person.change_happiness(-10)
                    $ the_person.change_love(-10)
                    $ the_person.event_triggers_dict["anger"] += 1
    "With that she leaves you alone in your room to think."
    $ the_person.relationship = "Single"
    $ the_person.SO_name = None
    $ scene_manager.clear_scene()
    return

label lily_transition_followup_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ sleeping = False
    "Now that things have fallen apart you should probably give [the_sister.title] a heads up, in case [the_person.title] acts weird."
    "As you are getting ready for bed you decide there is no time like the present and make your way to [the_sister.possessive_title]'s room."
    $ mc.location = lily_bedroom
    $ old_location = mc.location
    $ mc.location.show_background()
    $ scene_manager.add_actor(the_sister, position = "sitting")
    if cousin.location == lily_bedroom:
        $ cousin.change_location(downtown)
        mc.name "Hey, [the_sister.title], where is [cousin.fname]?"
        the_sister "Don't know, don't care. Just happy to have some alone time."
        mc.name "Oh, sorry, I can go."
        the_sister "No, wait..."
    else:
        mc.name "Hey, [the_sister.title] how are you doing?"
        the_sister "Pretty good, how about you?"
    the_sister "Is everything okay?"
    mc.name "Yeah, why wouldn't it be?"
    the_sister "I don't know, [the_person.fname] was a bit weird today and when I tried to bring it up she brushed me off."
    "Looks like you were too late. Well, damage done..."
    mc.name "Don't worry about it, I'm sure she'll be fine next week."
    if the_sister.has_role(girlfriend_role):
        the_sister "Don't be like that, I love you and telling me not to worry will just make me worry more."
        "She does love you, telling her would probably be for the best."
    else:
        the_sister "Fine, bury your feelings."
        "As she says that you can see her interest growing, if you don't tell her it will just make her more curious."
    mc.name "Alright, we sort of broke up I guess."
    the_sister "Oh, I'm sorry, was it serious?"
    if the_sister.has_role(girlfriend_role):
        "While it is clear she is concerned you also see a hint of jealousy in her eyes."
        mc.name "Nothing you needed to worry about, we were just having some fun."
    else:
        "Her compassion eases some of the pain you had been feeling."
        mc.name "Not really, she is fun but I didn't think we were going to get married or anything."
    the_sister "Still break-ups can be rough. Is there anything I can do for you?"
    mc.name "As a matter of fact I am feeling a bit lonely, do you think we could spend some time together?"
    the_sister "Of course."
    $ scene_manager.update_actor(the_sister, position = "stand4")
    "[the_sister.title] stands up and approaches you, wrapping her arms around you in a tight hug."
    if not the_sister.has_taboo("kissing"):
        $ scene_manager.update_actor(the_sister, position = "kissing")
        "The hug is nice, but you want more so you gently tilt her head up and lower yours to plant a gentle kiss on her lips."
        "As it lingers you feel her mouth start to part and you push forward more."
        "A slight moan runs through her as her body melts against yours."
        $ mc.change_arousal(10)
        $ the_sister.change_arousal(10)
    if not the_sister.has_taboo("touching_body"):
        "The warmth and closeness is amazing and you feel tension you were not aware of pouring out of your body."
        "Your cock begins to stir and as it hardens you press it against [the_sister.possessive_title]'s warm crotch."
        "She moans more audibly and starts to run her hands over your body, taking the hug from comforting to sexual."
        $ mc.change_arousal(10)
        $ the_sister.change_arousal(10)
    "The hug lingers, but eventually [the_sister.title] pulls away and you reluctantly let her go."
    if not the_sister.has_taboo("sucking_cock") and the_sister.has_taboo("vaginal_sex"):
        $ the_person.event_triggers_dict["lily_comfort"] = "oral"
        the_sister "Why don't you lay down on my bed? I'll get the door and then do something you take your mind off [the_person.fname]."
        $ scene_manager.update_actor(the_sister, position = "walking_away")
        "You drop back onto her bed and sprawl out, leaving your legs hanging down to the floor while [the_sister.title] goes and turns off the lights."
        $ scene_manager.update_actor(the_sister, position = "blowjob", lighting = dark_lighting[time_of_day])
        "By the time your eyes adjust to the darkness she is standing at the end of the bed and lowers herself down to her knees in front of you."
        "She rests her hands on your knees and slowly starts to run them up your thighs. Getting the idea you are quick to help her open them up so that she has easier access."
        the_sister "Well, someone is eager!"
        $ mc.change_arousal(10)
        if the_sister.opinion.giving_blowjobs > 0:
            the_sister "I have to admit I'm a bit excited to get a taste of you too."
            if the_sister.opinion.being_submissive > 0:
                the_sister "You know I'm always happy to serve you when you want me too."
                $ the_sister.change_arousal(10)
        else:
            the_sister "Don't expect this every time you get a little sad."
        $ scene_manager.update_actor(the_sister, position = "kneeling1")
        "By the time she has herself in position you are already standing at attention for her. She kisses the head and then licks the shaft a few times."
        "It is pretty clear you don't need any more prep and she opens her mouth to take your tip into her mouth, gently sucking on it and licking up your precum."
        "Next she opens wider and slowly slides down your shaft, taking more and more into her soft mouth."
        call get_fucked(the_sister, the_goal = "get mc off", sex_path = None, private= True, start_position = blowjob, start_object = make_bed(), skip_intro = True, report_log = None, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_comfort1
        mc.name "Thank you [the_sister.title], I think that was exactly what I needed."
        the_sister "Good, does that mean you are feeling better?"
        mc.name "Absolutely, I'm going to sleep like a rock tonight."
        the_sister "It is a little small, but if you wanted to sleep in here tonight I could make room for you."
        mc.name "You want me to sleep with you?"
        if the_sister.is_willing(missionary) or the_sister.is_willing(doggy):
            "She pauses for a second, and it almost looks like she is imagining that, possibly even considering saying yes."
            "Unfortunatly she catches herself and gives a little shake to clear her head."
        else:
            "She fliches back a bit, surprised you would even ask something like that."
            "With a studious gaze at your face she relaxes, maybe hoping that you were joking."
        the_sister "Not like that, just a little cuddling to further comfort you."
        "Disappointed, but not surprised you respond."
        mc.name "That sounds nice, thank you."
    else:
        the_sister "It is a little small, but if you wanted to sleep in here tonight I could make room for you."
        mc.name "You want me to sleep with you?"
        if not the_sister.has_taboo("vaginal_sex"):
            $ the_person.event_triggers_dict["lily_comfort"] = "sex"
            the_sister "I was just going to comfort you a bit, but you never know where the night will go."
            the_sister "I'll get the lights, you make yourself comfortable."
            "Not wanting to waste this opportunity you quickly strip and climb under the covers."
            $ scene_manager.update_actor(the_sister, lighting = dark_lighting[time_of_day])
            "It is hard to see in the sudden darkness, but you hear clothing shifting as [the_sister.title] prepares to join you."
            $ scene_manager.strip_to_underwear(the_sister)
            $ mc.change_locked_clarity(10)
            "You leave room for her to fit next to you, but aren't terribly surprised when she instead climbs on top of you, dropping a leg to each side and lowering her body to yours."
            $ scene_manager.update_actor(the_sister, position = "cowgirl")
            if the_sister.tits_visible:
                if the_sister.has_large_tits:
                    "Her sizable breasts press warmly against your bare chest as she settles down."
                else:
                    "Her firm nipples point into your chest as she settles down."
            else:
                "Her bra lessens the experience as she settles down."
            the_sister "So... do you want to talk about [the_person.fname]?"
            mc.name "Sorry, who?"
            the_sister "Funny... but I'm serious. Do you need to talk?"
            if the_sister.has_role(girlfriend_role):
                the_sister "I know our relationship has its challenges, but I don't just want to be a rebound for you when something else doesn't work out."
                mc.name "I know, and I love you as both my sister and my girlfriend."
            else:
                the_sister "I'll save you from making a terrible decision while you are on the rebound, but I also want to be here if you need to talk."
                mc.name "I know, and I'm so grateful to have someone who I can talk to about anything."
            mc.name "Honestly, it wasn't that serious. I miss her a bit but I'm sure I'll be fine in a few days."
            the_sister "Alright, in that case..."
            "She lowers her face to yours, resuming the kiss but with more passion. She also begins to grind her pelvis against yours."
            if the_sister.vagina_visible:
                if not the_sister.pubes_style == shaved_pubes:
                    "Her fine hairs send tingles along your skin where it brushes you and you can feel the heat radiating from her pussy"
                else:
                    "Her bare skin is incredibly smooth and you can feel the heat radiating from her pussy."
            else:
                "Her silky panties rub against you but don't dampen the heat radiating from her pussy."
            "It isn't long before you stiffen enough for her to feel your cock pressing against her folds."
            "You slide your hands down to her ass, pulling her more tightly against you and grinding harder."
            if the_sister.vagina_visible:
                "She slides her hands between your hips and lifts up a bit so she can spread her lips with one hand and grasp your rock hard pole with the other."
            else:
                "She slides her hands to her crotch, pulling her panties aside with one and grasping your rock hard pole with the other."
                $ the_sister.outfit.strip_to_vagina()
                $ scene_manager.add_actor(the_sister)
            "She makes a few more passes, spreading her juices along the length of your cock, before lifting her hips and guiding you into her waiting hole."
            "She sinks down slowly enveloping you in her tight warm pussy and stopping once you are buried to the hilt."
            the_sister "God, you always make me feel so full [the_sister.mc_title]."
            mc.name "And you always feel so tight. I must be the luckiest man in the world."
            "She smiles down at you and then starts to move, at first just slowly sliding up and down about an inch."
            call get_fucked(the_sister, the_goal = "get mc off", sex_path = None, private= True, start_position = cowgirl, start_object = make_bed(), skip_intro = True, report_log = None, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_comfort2
            mc.name "That was amazing [the_sister.title]. I'm not sure if comforted is the right word, but I definitely feel better."
            if the_sister.opinion.vaginal_sex > 0:
                the_sister "I have to admit I enjoyed myself too."
            if the_sister.opinion.being_submissive > 0:
                the_sister "You know how much I love satisfying your needs and giving you pleasure."
            "[the_sister.title] drapes herself over you, wrapping her arms around you as much as she can."
            "You are struck by how it can be so similar and at the same time wildly different than the hug you got when you first entered the room."
            "You smile to yourself at how lucky you are to have [the_sister.title] as you drift off to sleep."
            $ sleeping = True
        elif not the_sister.has_taboo("touching_penis"):
            $ the_person.event_triggers_dict["lily_comfort"] = "hand"
            the_sister "Not like that... but maybe we can find a way to help you relax."
            $ mc.change_arousal(10)
            the_sister "I'll get the lights, you make yourself comfortable."
            $ scene_manager.update_actor(the_sister, lighting = dark_lighting[time_of_day])
            "Not wanting to presume too much you strip, but only to your boxers, before you climb into her bed."
            "She quickly joins you, pressing her body up against yours as you squeeze into the bed together."
            $ mc.change_arousal(10)
            the_sister "Roll onto your side [the_sister.mc_title]. I'll be the big spoon and soothe you to sleep."
            "You comply, and feel her press against your bare back as she settles into place."
            "She wraps her top arm around you, pulling tighter, sort of like a hug."
            "It is comforting, but when her hand starts to wander down towards your waist other thoughts enter your mind."
            the_sister "Give me a bit of help here."
            "She starts to pull at the waist of your boxers and you lift your hips to let her pull them down."
            $ mc.change_arousal(10)
            "Her hand then travels back up and she gently strokes your stomach, brushing her hand against your rapidly hardening cock as she does so."
            call get_fucked(the_sister, the_goal = "get mc off", sex_path = None, private= True, start_position = handjob, start_object = make_bed(), skip_intro = True, report_log = None, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = False) from _call_get_fucked_comfort3
            mc.name "That was amazing [the_sister.title], I'm not sure I've ever been so relaxed."
            the_sister "Good, does that mean you are feeling better?"
            mc.name "Absolutely, I'm going to sleep like a rock tonight."
            the_sister "It is a little small, but since you're already here you might as well stay."
            mc.name "That sounds nice, thank you."
            $ sleeping = True
        else:
            the_sister "Get your mind out of the gutter [the_sister.mc_title], I just thought you might be lonely."
            the_sister "It's not like we never shared a bed before, I'll just keep you company."
            the_sister "I'll get the lights, you make yourself comfortable."
            $ scene_manager.update_actor(the_sister, position = "walking_away")
            "You drop your pants, but decide it would be prudent to keep your boxers and shirt on before you climb into bed."
            $ scene_manager.update_actor(the_sister, lighting = dark_lighting[time_of_day])
    if not sleeping:
        "You press your back against the wall, leaving plenty of room for [the_sister.title] to fit as well."
        "She climbs in and lies on her back, then turns towards you and then away, trying to find a comfortable position."
        $ scene_manager.update_actor(the_sister, position = "stand2")
        the_sister "Maybe I was wrong, we are going to have to get a little closer if we ever want to get to sleep."
        mc.name "I can go if you want..."
        the_sister "No, just scoot away from the wall a bit and I'll cuddle up to you."
        mc.name "Alright."
        "You position yourself and feel her slide up against your body. It is a bit surprising how natural she seems to fit in your arms."
        the_sister "See, this is nice. Although, I was supposed to be comforting you and you seem to be the one holding me."
        mc.name "It's fine, having you here is comforting even if you are in my arms instead of me being in yours."
        the_sister "Alright, good night [the_sister.mc_title]."
        mc.name "Good night."
        if the_sister.love > 50:
            the_sister "..."
            "She seems to tense up, like she wants to say something more."
            the_sister "..."
            the_sister "I love you."
            "She mumbles, almost too quiet to hear."
            menu:
                "Respond":
                    mc.name "I love you too."
                    "The tension bleeds out of her body as she relaxes back against you."
                    $ the_sister.change_stats(happiness = 5, love = 5)
                "Stay silent":
                    mc.name "..."
                    "You stay quite, the tension seems to grow a bit, but you deepen your breathing, like you somehow fell asleep already."
                    "It seems like she isn't going to make an issue of it, but she isn't happy."
                    $ the_sister.change_stats(happiness = -5, love = -5)
        "Yout drift off to sleep, happily holding [the_sister.possessive_title] close."
    $ scene_manager.clear_scene()
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_lily_transition_followup
    call lily_transition_followup_morning() from _call_lily_transition_followup_morning
    return "Advance Time"

label lily_transition_followup_morning(): ##TODO borrow a bunch from main
    $ scene_manager = Scene()
    $ mc.change_location(lily_bedroom)
    $ the_mom = mom
    $ the_mom.change_location(kitchen)
    $ the_sister = lily
    $ the_sister.change_location(kitchen)
    $ wear_pajamas(the_mom)
    $ wear_pajamas(the_sister)
    $ mom_slutty = False
    $ sis_slutty = False
    $ the_cousin = None
    if aunt in hall.people:
        $ the_cousin = cousin
        # $ the_cousin.change_location(kitchen)
        $ the_aunt = aunt
        $ the_aunt.change_location(kitchen)
        $ wear_pajamas(the_cousin)
        $ wear_pajamas(the_aunt)
        $ aunt_slutty = False
        $ cousin_slutty = False
        if the_cousin.effective_sluttiness() > 60:
            $ cousin_slutty = True
        if the_aunt.effective_sluttiness() > 60:
            $ aunt_slutty = True
        if the_mom.effective_sluttiness() > 60:
            $ mom_slutty = True
        if the_sister.effective_sluttiness() > 60:
            $ sis_slutty = True
    else:
        if the_mom.effective_sluttiness() > 40 or mc.business.event_triggers_dict.get("family_threesome", False) == True:
            $ mom_slutty = True
        if the_sister.effective_sluttiness() > 40 or mc.business.event_triggers_dict.get("family_threesome", False) == True:
            $ sis_slutty = True
    "When you wake up in the morning you are briefly disoriented until you remember where you are."
    "[the_sister.title]'s room is recognisable. You just aren't used to seeing it from her bed, especially after spending the night with her."
    "You were right about sleeping like a rock, you never even noticed [the_sister.possessive_title] getting out of bed this morning."
    if mc.event_triggers_dict.get("lily_comfort", None) == "sex":
        "Still naked from your late night activities you look to the thankfully closed door."
        "You get out of bed and get yourself dressed."
    elif mc.event_triggers_dict.get("lily_comfort", None) == "hand":
        "Thankfully the door is closed so you get out of bed and pull on your pants."
    elif mc.event_triggers_dict.get("lily_comfort", None) == "oral":
        "Fortunately you pulled your clothes back on last night, but you are still glad the door is closed."
        "You climb to your feet and stretch out some kinks from the unfamiliar bed."
    "It seems like [the_sister.title] has already started her day, and you figure you should probably follow suit."
    if the_cousin:
        "Suddenly you remember that [the_cousin.title] has been sleeping in here. She was out last night but must have come home at some point. Did she see you and [the_sister.title] sleeping together?"
        "This could be bad... you better get out there and see if you need to do damage control."
        "You head to your bedroom first and are somewhat relieved to see that the bed was slept in. Hopefully [the_cousin.possessive_title] just took advantage of the free bed and doesn't care about the reason."
    "You head for the kitchen to see who is around."
    $ mc.change_location(kitchen)
    $ x = 0
    while x < len(mc.location.people)-1:
        $ the_person = mc.location.people[x]
        $ scene_manager.add_actor(the_person, get_pajama_outfit(the_person), position = "sitting")
        $ x +=1
    $ scene_manager.update_actor(the_mom, position = "walking_away")
    if mom_slutty:
        if the_mom.wearing_panties:
            "[the_mom.possessive_title!c] is just in her underwear in front of the stove, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(5)
        else:
            "[the_mom.possessive_title!c] is in front of the stove naked, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(10)
    else:
        "[the_mom.possessive_title!c] is at the stove and humming to herself as she scrambles a pan full of eggs."
    $ the_mom.update_outfit_taboos()
    $ scene_manager.update_actor(the_mom, position = "back_peek")
    the_mom "Good morning [the_mom.mc_title]. I'm almost ready to serve, have a seat."
    if sis_slutty:
        if the_sister.wearing_panties:
            "[the_sister.possessive_title!c] is sitting at the kitchen table wearing her underwear. She gives a dramatic yawn before nodding to you."
            $ mc.change_locked_clarity(5)
        else:
            "[the_sister.possessive_title!c] is sitting at the kitchen table naked. She gives a dramatic yawn before nodding to you."
            $ mc.change_locked_clarity(10)
    else:
        "[the_sister.possessive_title!c] is sitting at the kitchen table and gives a dramatic yawn before nodding to you."
    $ the_sister.update_outfit_taboos()
    the_sister "Good morning [the_sister.mc_title]."
    if the_cousin:
        if aunt_slutty:
            if the_aunt.wearing_panties:
                "[the_aunt.possessive_title!c] is also sitting at the kitchen table. You are a bit surprised she is just wearing her underwear."
                $ mc.change_locked_clarity(5)
            else:
                "[the_aunt.possessive_title!c] is also sitting at the kitchen table. Shockingly she is naked."
                $ mc.change_locked_clarity(10)
        else:
            "[the_aunt.possessive_title!c] is also sitting at the kitchen table."
        "There is no sign of [the_cousin.possessive_title], but you settle down at the table with the rest of your family."
        #TODO finish this branch
    else:
        "You quickly take a seat next to [the_sister.title], leaning close to whisper in her ear."
        mc.name "Listen, about last night..."
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            "[the_sister.title] smiles up at you and then leans forward for a kiss."
            "As your lips connect you feel her hand running up your thigh."
            $ scene_manager.update_actor(the_mom, position = "walking_away")
            "Your mother takes the pan off the stove and begins to slide the contents off onto three plates."
            $ scene_manager.update_actor(the_mom)
            "She turns around and hands one plate to you and one plate to [the_sister.title]."
            $ scene_manager.update_actor(the_sister, position = "sitting")
            the_mom "Now, now you two. The table is for eating. I would have thought that last night was enough for you."
            the_sister "Sorry mom. We'll be good."
            "[the_sister.title] sets both her hands on the table before starting to dig in to breakfast."
            mc.name "Yeah, sorry."
            the_mom "Don't worry, I understand. I just want to have a nice meal right now."
        elif mom_slutty and sis_slutty:
            "[the_sister.title] smiles up at you and then quickly glances at [the_mom.possessive_title]."
            "Her grin turns mischeivous as she looks down and moves her hand to your leg, running it up your thigh."
            $ scene_manager.update_actor(the_mom, position = "walking_away")
            "Your mother takes the pan off the stove and begins to slide the contents off onto three plates."
            $ scene_manager.update_actor(the_mom)
            "She turns around and hands one plate to you and one plate to [the_sister.title]."
            "Sadly, [the_sister.title] pulls her hand from your leg to dig into breakfast."
            $ scene_manager.update_actor(the_sister, position = "sitting")
        if mom_slutty and sis_slutty:
            if mom.lactation_sources > 0 and mom.tits_visible:
                mom "Want a little milk for your coffee, honey?"
                "[mom.title] gives you a quick wink."
                mc.name "Sure mom."
                "[mom.possessive_title!c] bends slightly over your coffee. She takes one of her breasts in her hand and starts to squeeze."
                "It takes a second, but soon a stream of her milk is pouring out into you coffee."
                mom "Just say when!"
                "You let her continue for a few more moments, until you can see the cream start to circulate around your hot coffee."
                $ mom.change_stats(happiness = 5, slut = 1, max_slut = 40)
                mc.name "That's good!"
                lily "Thanks Mom, you're the best!"
            elif lily.lactation_sources > 0 and lily.tits_visible:
                mom "Want some coffee, honey?"
                mc.name "Sure mom."
                mom "Here you go, maybe [lily.fname] could help you out with some milk."
                "[mom.title] gives you a quick wink."
                lily "Really, Mom?"
                mc.name "I mean... if you don't mind it would be nice."
                "[lily.possessive_title!c] gives an exasperated sigh, but then bends slightly over your coffee. She takes one of her breasts in her hand and starts to squeeze."
                "It takes a second, but soon a stream of her milk is pouring out into you coffee."
                lily "Let me know when you have enough."
                "You let her continue for a few more moments, until you can see the cream start to circulate around your hot coffee."
                $ lily.change_stats(happiness = 5, slut = 1, max_slut = 40)
                mc.name "That's good!"
            else:
                lily "Thanks Mom, you're the best!"
            $ scene_manager.update_actor(the_mom, position="sitting")
            the_mom "No problem, I'm just happy to spend my morning relaxing with my two favourite people!"
            $ mc.change_locked_clarity(10)
            $ lily.change_stats(love = 3)
            $ mom.change_stats(love = 3, happiness = 5)
            if mc.business.event_triggers_dict.get("family_threesome", False) == True:
                "You enjoy a relaxing breakfast bonding with your mother and sister. [the_mom.possessive_title] seems particularly happy she gets to spend time with you."
                "Neither [lily.title] or [mom.possessive_title] seem to think it's strange to relax in their underwear and [lily.title] manages to keep you going throughout the meal."
                "The combined stimulation is starting to take a toll on you."
                "You try to focus on something work related, but instead all you can focus on are [mom.possessive_title]'s heaving tits, across the table from you."
                mom "Honey? Are you feeling okay? You seem a little zoned out..."
                "Next to you, [lily.title] grasps your erection and speaks up."
                lily "I'm sure he's fine mom, but us dressing like this has him all worked up. He's hard as a rock!"
                mom "It doesn't help that you keep encouraging him. [lily.fname] honey, let's take care of him before the day gets going."
                lily "Good idea mom!"
                menu:
                    "Accept their help":
                        mc.name "Oh wow, that would be great!"
                        $ scene_manager.update_actor(mom, position = "stand2")
                        $ scene_manager.update_actor(lily, position = "blowjob")
                        "[mom.possessive_title!c] gets up and starts walking around the table, while [lily.title] gets on her knees and starts pulling off your pants and underwear."
                        "Your cock springs out of your clothes, nearly smacking [lily.possessive_title] in the face. [mom.title] gets on her knees next to [lily.title]."
                        call start_threesome(lily, mom, start_position = threesome_double_blowjob, position_locked = True) from _call_start_threesome_study_morning
                        $ the_report = _return
                        if the_report.get("guy orgasms", 0) > 0:
                            "You enjoy your post-orgasm bliss for a few moments while [mom.possessive_title] and [lily.possessive_title] get up."
                        else:
                            "Finished for now, you decide to put your cock away while [mom.possessive_title] and [lily.possessive_title] get up."
                        $ scene_manager.update_actor(mom, position="stand3", display_transform = character_center_flipped)
                        $ scene_manager.update_actor(lily, position = "stand4", display_transform = character_right)
                        mc.name "Mmm, thanks for breakfast mom!"
                        if the_report.get("guy orgasms", 0) > 0:
                            "[lily.title] laughs and jokes back."
                            lily "Thanks for breakfast, bro!"
                    "Refuse":
                        mc.name "That's okay, I have a ton of stuff to get done today. Maybe tonight after dinner?"
                        mom "Okay, if that's what you want [mom.mc_title]."
                        $ scene_manager.update_actor(mom, position="walking_away", display_transform = character_left_flipped)
                        "[mom.possessive_title!c] gets up and starts to do the dishes."
            else:
                "You enjoy a relaxing breakfast bonding with your mother and sister. [the_mom.possessive_title] seems particularly happy she gets to spend time with you."
                "Neither [lily.title] or [mom.possessive_title] seem to think it's strange to relax in their underwear and [lily.title] reaches over to stroke you occasionally."
                "It is difficult, but your head wins out and you are able to resist the urge to take things further in front of [the_mom.possessive_title]."
            "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."
        elif sis_slutty:
            $ scene_manager.update_actor(the_sister, position = "sitting")
            "Before you can finish your sentence your mother turns around and gasps."
            $ scene_manager.update_actor(the_mom, emotion = "angry")
            the_mom "[the_sister.fname]! What are you wearing?"
            $ scene_manager.update_actor(the_sister, position = "sitting")
            the_sister "What do you mean? I just got up, I haven't had time to pick out an outfit yet."
            $ scene_manager.update_actor(the_mom, emotion = "angry")
            the_mom "You shouldn't be running around the house naked. Go put some clothes on young lady."
            $ scene_manager.update_actor(the_sister, position = "sitting", emotion = "angry")
            "[the_sister.possessive_title!c] scoffs and rolls her eyes."
            the_sister "Come on Mom, you're being ridiculous. This is my house too, I should be able to wear whatever I want!"
            "Your mother and sister lock eyes, engaged in a subtle battle of wills."
            if the_sister.obedience > the_mom.obedience:
                $ scene_manager.update_actor(the_mom, position = "walking_away")
                "Mom sighs loudly and turns back to the stove."
                the_mom "Fine! You're so stubborn [the_sister.title], I don't know how I survive around here!"
                $ the_sister.change_obedience(-2)
                $ the_sister.change_happiness(10)
                $ the_sister.change_slut(2, 50)
                $ the_mom.change_obedience(10)
                $ scene_manager.update_actor(the_sister, position = "sitting", emotion = "happy")
                "[the_sister.possessive_title!c] looks at you, obviously pleased with herself, and winks."
                "Breakfast proceeds, but there is a bit of tension at the table."
                "[the_sister.title] looks pleased with herself and from time to time she runs her hand along your thigh."
            else:
                "[the_sister.title] finally sighs loudly and looks away. She pushes her chair back and stands up in defeat."
                $ scene_manager.update_actor(the_sister, emotion = "angry")
                the_sister "Fine! I'll go put on some stupid clothes so my stupid mother doesn't keep worrying."
                $ scene_manager.update_actor(the_sister, position = "walking_away")
                "[the_sister.title] sulks out of the kitchen."
                $ scene_manager.update_actor(the_mom)
                the_mom "I don't know how I manage to survive with you two around!"
                $ the_sister.apply_planned_outfit()
                $ the_sister.change_obedience(10)
                $ the_sister.change_happiness(-5)
                $ the_mom.change_obedience(-2)
                $ scene_manager.update_actor(the_sister, position = "sitting")
                "[the_sister.possessive_title!c] is back by the time [the_mom.title] starts to plate breakfast. She sits down and starts to eat without saying a word."
                "The table is a bit tense, but breakfast proceeds somewhat normally."
                "About halfway through [the_sister.title] glances down at your pants and then proceeds to reach over and run her hand along your thigh. It is almost like she wants to be caught."
            "It seems that spending the night with her might have made her a bit more comfortable being bold around you."
            "When you're done you help Mom put the dirty dishes away and get on with your day."
        else:
            "[the_sister.title] flushes with embarrassment and angrily cuts you off, while trying to keep her voice quiet."
            the_sister "Not now!"
            if mom_slutty:
                "She then turns away from you just as [the_mom.possessive_title] spins around."
                the_sister "Oh my god Mom, what are you wearing?"
                $ scene_manager.update_actor(the_mom, position = "back_peek")
                the_mom "What? It's the weekend and it's just the three of us. I didn't think anyone would mind if I was a little more casual."
                $ scene_manager.update_actor(the_sister, position = "sitting")
                if the_mom.vagina_visible:
                    the_sister "Mom, I don't think you know what casual means. Could you at least put on some panties or something?"
                elif the_mom.tits_visible:
                    the_sister "Mom, I don't think you know what casual means. I mean, couldn't you at least put a bra?"
                else:
                    the_sister "Mom, you're prancing around the kitchen in your underwear. In front of your son and daughter. That's weird."
                    "[the_sister.title] looks at you."
                    the_sister "Right [the_sister.mc_title], that's weird?"
                if the_mom.obedience > 115:
                    $ scene_manager.update_actor(the_mom, position = "back_peek")
                    the_mom "What do you think [the_mom.mc_title], do you think it's \"weird\" for your mother to want to be comfortable in her own house?"
                    $ mc.change_locked_clarity(5)
                    menu:
                        "Side with Mom":
                            mc.name "I think Mom's right [the_sister.title]. It's nothing we haven't seen before, she's just trying to relax on her days off."
                            $ the_mom.change_obedience(-5)
                            $ the_sister.change_obedience(5)
                            "[the_sister.title] looks at the two of you like you're crazy then sighs dramatically."
                            the_sister "Fine, but this is really weird, okay?"
                            $ scene_manager.update_actor(the_mom, position = "sitting")
                            "[the_mom.possessive_title!c] dishes out three portions and sits down at the table with you. [the_sister.title] eventually gets used to her mother's outfit and joins in on your conversation."
                            $ the_sister.change_slut(2, 30)
                            $ the_mom.change_happiness(10)
                        "Side with [the_sister.title]":
                            mc.name "I actually think [the_sister.title] is right, this is a little weird. Could you go put something on, for our sakes?"
                            $ the_sister.change_obedience(-2)
                            $ the_sister.change_slut(1, 30)
                            $ the_mom.change_obedience(5)
                            the_mom "Oh you two, you're so silly. Fine, I'll be back in a moment. [the_sister.title], could you watch the eggs?"
                            $ scene_manager.update_actor(the_sister, position = "walking_away")
                            "Your mother leaves to get dressed. [the_sister.possessive_title] ends up serving out breakfast for all three of you."
                            $ the_mom.apply_planned_outfit()
                            the_sister "She's been so weird lately. I don't know what's going on with her..."
                            $ scene_manager.update_actor(the_mom, position = "sitting")
                            $ the_sister.change_happiness(5)
                            $ the_mom.change_happiness(5)
                            "When [the_mom.possessive_title] gets back she sits down at the table and the three of you enjoy your breakfast together."
                else:
                    $ scene_manager.update_actor(the_mom, position = "back_peek")
                    the_mom "Well luckily I'm your mother and it doesn't matter what you think. I'm going to wear what makes me comfortable."
                    "She takes the pan off the stove and slides the scrambled eggs out equally onto three plates."
                    the_mom "Now, would you like some breakfast or not?"
                    "[the_sister.title] sighs dramatically."
                    the_sister "Fine, but this is really weird, okay?"
                    $ the_sister.change_slut(1, 30)
                    $ the_mom.change_happiness(10)
                    $ scene_manager.update_actor(the_mom, position = "sitting")
                    "[the_mom.possessive_title!c] gives everyone a plate and sits down. [the_sister.title] eventually gets used to her mother's outfit and joins in on your conversation."
                    "When you're done you help Mom put the dirty dishes away and get on with your day."
            else:
                $ scene_manager.update_actor(the_sister, position = "sitting")
                the_sister "So what's the occasion Mom?"
                $ scene_manager.update_actor(the_mom)
                "[the_mom.possessive_title!c] takes the pan off the stove and scoops the scrambled eggs out equally onto three waiting plates."
                the_mom "Nothing special, I just thought we could have a nice quiet breakfast together."
                "She slides one plate in front of you and one plate in front of [the_sister.title], then turns around to get her own before sitting down to join you."
                $ scene_manager.update_actor(the_mom, position = "sitting")
                the_mom "Go ahead, eat up!"
                $ the_sister.change_love(3)
                $ the_mom.change_love(3)
                $ the_mom.change_happiness(5)
                "While the food is good [the_sister.possessive_title] seems tense. Still, [the_mom.possessive_title] seems particularly happy she gets to spend time with you."
                "When you're done you help [the_mom.title] put the dirty dishes away and get on with your day."
    $ scene_manager.clear_scene()
    return
