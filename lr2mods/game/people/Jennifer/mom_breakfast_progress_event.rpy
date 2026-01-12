#Jennifer breakfast in bed progress scene
#This scene is for Jennifer giving MC breakfast in bed.
#At a certain obedience you can ask her for it the day before, otherwise it is a random crisis event
#Starting out, she just serves MC.
#As she gets sluttier and/or more obedience she shows up nude, or in just an apron, giving MC a show while he eats.
#Eventually MC can get a blowjob or revere cowgirl sex while he eats his breakfast.

label mom_breakfast_prog_scene_action_label():
    call progression_scene_label(mom_breakfast_prog_scene, [mom]) from _mom_breakfast_in_bed_prog_scene_proc_01
    return

label mom_breakfast_prog_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ the_person.set_event_day("breakfast_in_bed")
    "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
    mc.name "Ahhh... umm... who is it?"
    the_person "It's me."
    mc.name "What... what is it?"
    the_person "I... I thought you might like some breakfast. I brought you some."
    mc.name "Ummm... sure!... Come in!"
    $ the_person.draw_person()
    "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
    the_person "I know it is early... I normally hear your alarm going off by now."
    "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
    mc.name "Wow... this looks great!"
    the_person "Yeah I... I woke up this morning a little early and was just thinking about how nice it has been, with you stepping up around the house lately."
    the_person "I just wanted to make sure you know that I appreciate you helping with the bills and everything else."
    mc.name "Of course... wow..."
    the_person "I'll just let you enjoy this and give you some privacy..."
    "She starts to leave your room, but you stop her."
    mc.name "Hey, you don't have to leave. Why don't you stay and we can chat for a bit?"
    the_person "Oh! Sure honey..."
    "You grab the tray of food and start to dig in. Once in a while [the_person.possessive_title] will make a little extra breakfast for you, but this is way beyond what she normally does."
    if the_person.is_employee:
        the_person "So, I know that I work there now, but I don't really dig into the financials."
        the_person "I was wondering, how are things going at your business?"
    else:
        the_person "So... while you are eating, I was wondering... how are things going at your business?"
    mc.name "They are going pretty well. Sometimes research is a little bit slow, but we are making steady progress."
    the_person "I see, is there anything I could do? To help?"
    mc.name "Well... we could always use more test participants. It is helpful to have test subjects when we have proposed final version of drugs ready."
    the_person "Oh... you need me to be a... a lab rat?"
    mc.name "I guess you could call it that. Mostly we are looking for subtle things, like rare or hard to measure side effects."
    mc.name "The drugs themselves are perfectly safe, but it would be useful to be able to try them in a home like setting, in a position where we could measure the effects in a real world environment."
    the_person "I see... hmmm..."
    "She thinks about it for a minute."
    the_person "I would be okay with that... with being your lab rat once in a while."
    the_person "But only after I get off work. I don't want them to effect my job performance!"
    mc.name "Most of them wear off after a good night's sleep anyway."
    the_person "Okay. Come find me in my room after dinner. If I'm not too tired, I'll help you test your serums."
    mc.name "Wow, thanks mom!"
    "You return to eating your breakfast in bed."
    $ mc.change_energy(50)
    "When you finish, [the_person.title] takes the tray."
    mc.name "That was amazing. Feel free to do that anytime!"
    the_person "Don't expect it every day, but I'll keep that in mind!. I'll take this to the kitchen. I hope you have a great day!"
    mc.name "Thanks!"
    $ clear_scene()
    "[the_person.possessive_title!c] leaves your room. You look at your phone and see the alarm coming up in three minutes. You turn it off."
    "It is interesting that she felt the need to make you breakfast in bed. You certainly don't mind it."
    "You've noticed in general that she has been getting submissive to you since you started helping with the house and bills."
    "You wonder if you could manage to convince her to do other things for you too..."
    "You briefly imagine [the_person.title], walking around the house in just an apron, greeting you at the door when you get off work, and slowly getting on her knees..."
    $ mc.change_locked_clarity(30)
    "Step by step, you think to yourself. You don't want to rush anything."
    "Being able to reliably get her to test your serums will really help though. You can now visit her at night in her room and ask her to help you test a serum."
    $ mom.progress.obedience_step = 2   #This setting enables this progress event to be called in the future randomly.
    $ add_mom_obedience_home_uniform_action()
    return

label mom_breakfast_prog_scene_request_label(the_person): #players can ask for breakfast in bed the night before once it has been unlocked.
    mc.name "Hey, do you think you could do me a favour tomorrow morning?"
    the_person "Probably, what do you need?"
    mc.name "Do you think you could make me some breakfast? It really helps me get a good start to the day."
    the_person "Sure, I can do that for you honey. Did you need anything else?"
    $ the_person.set_event_day("breakfast_in_bed")
    $ add_mom_breakfast_prog_scene_mand_action()
    return

#Intro Scenes

label mom_breakfast_prog_scene_intro_0(the_group):
    $ the_person = the_group[0]
    "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
    the_person "[the_person.mc_title]? It's me. I made you some breakfast again."
    mc.name "Oh great! Come in!"
    $ the_person.draw_person()
    "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
    the_person "I'm so proud of you and all your hard work, I just wanted to make you some breakfast to help you start your day."
    "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
    mc.name "Wow... this looks great!"
    return

label mom_breakfast_prog_scene_intro_1(the_group):
    $ the_person = the_group[0]
    "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
    the_person "[the_person.mc_title]? It's me. I made you some breakfast again."
    mc.name "Oh great! Come in!"
    $ the_person.draw_person()
    "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
    the_person "You work so hard, I just wanted to give you a little extra *motivation* today."
    "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
    mc.name "Wow... this looks great!"
    the_person "Yes, I know how much a good breakfast, among other things, helps to motivate you."
    "[the_person.title] gives you a subtle wink."
    return

label mom_breakfast_prog_scene_intro_2(the_group):
    $ the_person = the_group[0]
    "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
    the_person "[the_person.mc_title]? It's me. I've got your breakfast ready!"
    mc.name "Oh good! Come in!"
    $ the_person.draw_person()
    "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
    the_person "It's time to start the day out right. I've got some breakfast for you!"
    "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
    mc.name "Wow... this looks great!"
    if the_person.energy < 60:
        pass
    else:
        the_person "This will give you a full stomach to start the... are there any other *needs* you might have that I could help with while you eat?"
    return

label mom_breakfast_prog_scene_intro_3(the_group):
    $ the_person = the_group[0]
    "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
    the_person "[the_person.mc_title]? It's me. I've got your breakfast ready!"
    mc.name "Oh good! Come in!"
    $ the_person.draw_person()
    "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
    the_person "It's time to start the day out right. I've got some breakfast for you!"
    "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
    mc.name "Wow... this looks great!"
    if the_person.energy < 60:
        pass
    else:
        the_person "While you eat I could help you with your morning *issue*, but if you would rather have some privacy I understand."
        the_person "I could go for a nice protein snack myself."
        "She gives you a not so subtle wink and licks her lips."
    return

label mom_breakfast_prog_scene_intro_4(the_group):
    $ the_person = the_group[0]
    "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
    the_person "[the_person.mc_title]? It's me. I've got your breakfast ready!"
    mc.name "Oh good! Come in!"
    $ the_person.draw_person()
    "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
    the_person "It's time to start the day out right. I've got some breakfast for you!"
    "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
    mc.name "Wow... this looks great!"
    if the_person.energy < 60:
        pass
    else:
        "She stands at the side of your bed for a moment before she sets down your food."
        the_person "While you eat, can mommy take that morning wood for a quick ride? I want to send you to work *fully* satisfied!"
        the_person "But if you want some privacy I understand"
        "She gives you a big smile."
    return

#Choice Scene
label mom_breakfast_prog_scene_choice_label(the_group):
    $ the_person = the_group[0]
    $ the_person.set_event_day("breakfast_in_bed")
    if the_person.energy < 60:
        "After she sets down your breakfast, she looks at you."
        the_person "So, normally I would offer to stick around a bit but, I'm really worn out."
        the_person "I'm going to go have some coffee to try and wake up. Can you set your dishes by the sink when you are done?"
        mc.name "Sure."
        return False

    else:
        "[the_person.title] sets your breakfast in front of you, then she looks at you intently."
        the_person "So... did you want some privacy? Or should I wait for you to eat?"
        menu:
            "Stay with me {image=progress_token_small}" if mom_breakfast_prog_scene.progression_available:
                "Something about the look in her eyes tells you it is a good day to accept."
                mc.name "Why don't you hang out with me for a bit? It is always nice to spend time with you [the_person.title]."
                the_person "Certainly honey."
                return True
            "Stay with me" if not mom_breakfast_prog_scene.progression_available:
                mc.name "Why don't you hang out with me for a bit? It is always nice to spend time with you [the_person.title]."
                the_person "Certainly honey."
                return True
            "Eat alone":
                mc.name "This looks great, but I think I'd prefer to eat alone this morning."
                the_person "Ahh, okay [the_person.mc_title]. Can you set your dishes by the sink when you are done?"
                mc.name "Sure."
                return False
    return False

#Early Exit Scene
label mom_breakfast_prog_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turn and steps out of your room, closing the door behind her."
    $ clear_scene()
    "You dig in to the delicious breakfast she prepared you. It tastes great and really helps start your day out right."
    $ mc.change_energy(100)
    return



#Transition scenes
label mom_breakfast_prog_trans_scene_0(the_group):  #Should never be called
    $ the_person = the_group[0]
    return

label mom_breakfast_prog_trans_scene_1(the_group):  #Ask for striptease
    $ the_person = the_group[0]
    "You dig in to the delicious breakfast she prepared you. It tastes great and really helps start your day out right."
    $ mc.change_energy(100)
    "[the_person.title] watches you quietly. Her normal small talk is absent today."
    "You don't mind it, but soon a naughty idea pops into your head."
    "You've been influencing her a bit more recently with serums, you wonder if you could get her to make this a bit more interesting."
    mc.name "I really appreciate breakfast [the_person.title]. It is so hard to get up and get going on these early mornings."
    mc.name "Sometimes I have to use ummm... other things to motivate me..."
    the_person "Oh? Like what?"
    mc.name "Ah well... sometimes on my phone I will pull up porn to help me you know... get the heart rate up."
    the_person "Oh! Yes... I... I suppose that would do it."
    $ the_person.change_slut(1, 40)
    "You pretend to think about it for a moment."
    mc.name "Hey, you know what would be really nice? You could take off your clothes and give me a little show while I eat."
    the_person "[the_person.mc_title]..."
    mc.name "It would really help get my heart rate up and ready for the day!"
    if the_person.event_triggers_dict.get("kissing_revisit_complete", False):
        "She thinks about it for a moment, then chuckles."
        the_person "Well, I suppose we agreed a little show now and then would be okay."
    else:
        if the_person.event_triggers_dict.get("kissing_revisit_count", 0) == 0: #First time
            the_person "I don't mind helping you get a good start to the day, but that seems a little crazy [the_person.mc_title]."
            the_person "I'm your mother, I'm here to help you with your physical needs, not your sexual needs!"
            mc.name "I'm not asking you for a blowjob, just something nice to look at while I eat."
            the_person "Your old mother is hardly *something nice to look at*"
            mc.name "Wow mom, I disagree completely. You look amazing."
            the_person "You're just saying that to make me feel good..."
            mc.name "No I'm not. I am asking you to strip for me because it would really turn me on and it would help me start my day motivated."
            "She tries to a hide a smile, then agrees."
            the_person "Okay... if it would really mean that much to you. Just this once, okay?"
        else:
            the_person "[the_person.mc_title], we talked about this. You shouldn't be seeing your own mother naked like that."
            mc.name "Why not? I'm just looking, and it would REALLY help me start my day motivated!"
            mc.name "Don't you want me to be successful with my new business?"
            "She tries to a hide a smile, then agrees."
            the_person "Okay... if it would really mean that much to you. Just one more time, okay?"
        mc.name "Of course."
    return

label mom_breakfast_prog_trans_scene_2(the_group):  #Ask for handjob
    $ the_person = the_group[0]
    "You dig in to the delicious breakfast she prepared you. It tastes great and really helps start your day out right."
    $ mc.change_energy(100)
    "[the_person.title] watches as you start to dig in, then speaks up."
    the_person "Did you ummm... want a little show while you eat?"
    "While you definitely enjoy seeing [the_person.possessive_title] naked, it can also leave you frustrated. You decide to try and push her a little further."
    mc.name "That does sound nice [the_person.title], but the last couple of times have left me... well... with blue balls."
    mc.name "It kind of hurts and leaves me distracted at work. I thought maybe you could do something a little different for me."
    the_person "Oh? Like what?"
    mc.name "Why don't you get naked and get me hard, then sit beside me on the bed while I eat and give me a handjob."
    if the_person.has_taboo("touching_penis"):
        the_person "Oh... I... I didn't even realise you liked handjobs."
        mc.name "I mean, I definitely like other things better, but this would be a little easier and wouldn't cross any lines..."
        the_person "Yeah, that makes sense."
    else:
        the_person "Oh! You want a handjob?"
    "She thinks about it for a moment."
    the_person "Okay, I can do that for you. It might actually be kind of fun!"
    $ the_person.change_slut(1, 50)
    return

label mom_breakfast_prog_trans_scene_3(the_group):  #Ask for blowjob
    $ the_person = the_group[0]
    "You dig in to the delicious breakfast she prepared you. It tastes great and really helps start your day out right."
    $ mc.change_energy(100)
    if the_person.is_naked:
        "You look up after your first bite, admiring [the_person.possessive_title]'s naked body."
    else:
        "She doesn't even wait for you to ask, she starts stripping down immediately."
        $ the_person.strip_full_outfit(strip_feet = True, strip_accessories = True)
    the_person "So... having any *morning* issues I can help with?"
    "[the_person.possessive_title!c] seems eager to serve you, so you decide to see if she is willing to service you with her mouth instead of her hand this morning."
    mc.name "Damn, well if I didn't before I saw your amazing body, I sure do now!"
    "She blushes for a moment."
    mc.name "You know what would be hot for a change of pace though? If you used your lips instead of fingers."
    the_person "Oh... you mean like a... blowjob?"
    mc.name "Exactly."

    if the_person.event_triggers_dict.get("oral_revisit_complete", False):
        "She thinks about it for a moment, then shrugs."
        the_person "Well, I suppose I could spoil you with a blowjob while you eat breakfast."
        the_person "Maybe you could return the favour sometime too?"
        mc.name "Yeah sure thing [the_person.title]."
    else:
        if the_person.event_triggers_dict.get("oral_revisit_count", 0) == 0: #First time
            the_person "Messing around with petting is one thing [the_person.mc_title], but that would take things to far!"
            the_person "I'm your mother, not some whore you pay to suck you off anytime you want!"
            mc.name "I know you aren't, you're the most important woman in my entire life."
            mc.name "It has been so nice, being able to get closer to you lately, and it feels good when share moments of intimacy."
            the_person "Yeah but this is a level of intimacy that is for *lovers*, not a mother and son! This is wrong!"
            mc.name "But it doesn't feel wrong, does it? In fact, every step we take feels the opposite. It feels so right!"
            "She tries to a hide a smile while shaking her head."
            the_person "I can't believe I'm even entertaining the idea. What kind of mother am I?"
            mc.name "The kind that really loves her son. It would make me so happy [the_person.title]."
            "Her face visibly softens as she finally gives in to it."
            the_person "Oh [the_person.mc_title] I can't say no to you. Okay... I'll do it!"
        else:
            the_person "[the_person.mc_title], we talked about this. It isn't right for me to... you know..."
            mc.name "To what? Tell me what it is that you can't do."
            the_person "I can't just be putting that... that wonderful cock of yours in my... my mouth!"
            mc.name "Do you even hear yourself? I bet you were thinking about it the entire time you were making breakfast!"
            "She shakes her head, in disbelief rather than refusal."
            the_person "I wasn't! I just... I mean, even if I was, that doesn't make it right!"
            mc.name "Are you really going to tell me it isn't right to make an important man in your life feel good? To satisfy him?"
            "She looks down, but slowly nods her head."
            the_person "Oh God you're right... even though we agreed not to, I just can't get the thought out of my head."
            "She turns her face back to you, looking you in the eyes."
            the_person "Oh [the_person.mc_title], I want to make you feel good. Can mommy make you feel good?"
            $ mc.change_locked_clarity(30)
            mc.name "Absolutely"
    $ the_person.change_slut(1, 70)
    $ the_person.change_obedience(3)
    return

label mom_breakfast_prog_trans_scene_4(the_group):  #Ask for sex
    $ the_person = the_group[0]
    "You dig in to the delicious breakfast she prepared you. It tastes great and really helps start your day out right."
    $ mc.change_energy(100)
    "After you take your first bite, she speaks up."
    the_person "I hope you've got some morning wood for me to suck on this morning. Mommy needs her own breakfast this morning!"
    $ mc.change_locked_clarity(30)
    "Damn, hearing her dirty mouth makes your cock twitch. She is so eager to please you, but you have a naughty idea for how to take this to the ultimate level."
    mc.name "You know [the_person.title], I appreciate you being willing to do that, but have you ever thought about doing something that would feel good for both of us?"
    the_person "Of course [the_person.mc_title], but it would be hard for you to eat your breakfast if mommy sits on your face for a 69..."
    "Fuck, that sounds hot too... maybe you'll have to circle back to that idea sometime."
    mc.name "No, that isn't what I was thinking."
    "She looks at you, puzzled."
    the_person "Oh? What do you mean?"
    mc.name "Just get on top and ride me. Go nice and slow and we can both enjoy ourselves."
    if the_person.event_triggers_dict.get("vaginal_revisit_complete", False):
        the_person "Oh? I mean that sounds great but... how would that even work? How could you eat your breakfast?"
        mc.name "Just hop on reverse doggy. Go nice and slow, like when you did the blowjob."
        mc.name "I'll eat my breakfast and I'll get to watch that amazing ass of yours bounce up and down on my cock for a while."
        mc.name "And if the pacing is too slow for you, you could even touch yourself and get yourself off so you can feel good too."
        the_person "Oh! Wow I hadn't even thought of that. That sounds fun!"
    else:
        if the_person.event_triggers_dict.get("vaginal_revisit_count", 0) == 0: #First time
            the_person "Ohhh, I'm sorry [the_person.mc_title], I'm not sure I'm up for anal this morning..."
            mc.name "Oh, I didn't mean anal anyway. It would be much easier to just have sex..."
            the_person "[the_person.mc_title]! Don't joke like that. We have an arrangement, you know we can't have REAL sex!"
            "You sigh."
            mc.name "Mom, look me in the eyes and tell me you don't want to try it."
            the_person "Honey! It's not about wants... it is about what is right..."
            mc.name "And think about how right it would feel to finally indulge yourself and make me the happiest son on the planet at the same time."
            "[the_person.title] sighs, but looks at you and smiles."
            the_person "... it was always going to come to this, wasn't it?"
            the_person "I've been denying myself and the way you make me feel for so long... but deep down, somehow, I think I always knew this would happen eventually."
            mc.name "I've known it too. It's natural for a young, virile man to want to fuck a beautiful woman like you."
            mc.name "And it's natural for you, a beautiful woman, to want to get fucked by someone she loves and trusts."
            mc.name "You love me, don't you?"
            the_person "I do..."
            "Her face softens visibly, then she looks at you."
            the_person "Okay... how do we even do this?"
            mc.name "Just turn around and ride me, with your back to me. Go nice and slow and we'll both just enjoy it."
            the_person "Let's do it [the_person.mc_title]!"
        else:
            the_person "Oh God [the_person.mc_title], please, don't ask me to do that again."
            the_person "You know I can't say no to you..."
            mc.name "Is that what you want? We've tasted carnal knowledge, and how amazing it is. Do you want to leave that behind us forever?"
            "She moans and shrugs."
            the_person "I don't know what I want... I want to be a good mother!"
            mc.name "Then ride me [the_person.title]. That will make me the happiest boy in the world."
            "She moans softly and nods."
            the_person "Okay... how do we even do this?"
            mc.name "Just turn around and ride me, with your back to me. Go nice and slow and we'll both just enjoy it."
            the_person "Let's do it [the_person.mc_title]!"
    return


#Final Scenes
label mom_breakfast_prog_scene_scene_0(the_group, scene_transition = False):
    $ the_person = the_group[0]
    "You dig in to the delicious breakfast she prepared you. It tastes great and really helps start your day out right."
    $ mc.change_energy(100)
    the_person "So how is work going?"
    if the_person.is_employee:
        the_person "I mean, I know that I work there now, but I don't really dig into the financials."
    mc.name "It is going well. Research is continuing to produce favourable results, so I think we have the opportunity to make good progress."
    "You share with her the basics of some recent advancements you've made."
    the_person "That sounds amazing honey. Remember, I'm always willing to help you out in the evenings once I get off work."
    mc.name "Thanks [the_person.title]."
    $ the_person.change_obedience(1)
    "You decide to steer the conversation in another direction for a bit..."
    menu:
        "Talk about girls":
            mc.name "Hey, let me ask you about something. I've been hanging out with this girl lately..."
            the_person "Oh! A girl?"
            "You talk to [the_person.possessive_title] about your love life. She listens intently."
            $ the_person.change_slut(1, 40)
            the_person "I've always thought it's important to be adventurous. You might connect with someone you wouldn't expect."

        "Talk about her":
            mc.name "Other than that, it has been pretty quiet lately. What about you?"
            "You get [the_person.possessive_title] talking about herself and some gossip about your aunt and cousin."
            "It is clear she is worried about them but just wants what is best for her family."
            $ the_person.change_love(1)
            the_person "Whew. That felt good to talk about actually."
    "When you finish, [the_person.title] takes the tray."
    mc.name "That was so good. Thanks again [the_person.title]."
    the_person "I'll take this to the kitchen. I hope you have a great day!"
    mc.name "Thanks!"
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title!c] leaves your room. You look at your phone and see your alarm coming up in three minutes. You turn it off."
    "Time to get the day started."
    return

label mom_breakfast_prog_scene_scene_1(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if not scene_transition:
        "[the_person.possessive_title!c] watches quietly as you dig in to your breakfast."
        if the_person.event_triggers_dict.get("kissing_revisit_complete", False):
            the_person "So... were you wanting a show today too?"
            mc.name "Yeah, I was just about to ask. Go ahead and get naked, and show me what you got!"
            $ the_person.change_obedience(2)
            the_person "Okay [the_person.mc_title]."
        else:
            "You look up, realizing she is just standing there."
            mc.name "Why don't you go ahead and get naked? It was nice last time."
            the_person "[the_person.mc_title], we talked about this... I'm not a stripper."
            mc.name "I know. You're so much more than that to me. Please [the_person.title]? It really does help me with the start of my work day."
            "She tries to a hide a smile, then agrees."
            the_person "Okay... if it would really mean that much to you. Just one more time, okay?"
            mc.name "Of course."
    mc.name "Start with your top, I want to see those amazing tits of yours [the_person.title]."
    the_person "Okay..."
    $ the_person.strip_to_tits(prefer_half_off = False)
    if the_person.has_large_tits:
        "You stop and watch as [the_person.possessive_title]'s big tits bounce free."
    else:
        "You stop and watch as [the_person.possessive_title] exposes her perky tits."
    $ mc.change_locked_clarity(20)
    mc.name "Wow [the_person.title], you've got a nice rack. Can I get a closer look?"
    if the_person.obedience >= 130 or the_person.effective_sluttiness("bare_tits") > 20:
        if the_person.effective_sluttiness("bare_tits") > 30:
            the_person "Of course, you can hardly get a good look from there, can you?"
        else:
            the_person "Oh... If that is what you want, [the_person.mc_title]."
        $ the_person.draw_person(position = "cowgirl", display_transform = character_center_flipped(zoom = 1.2))
        "She climbs on the bed beside you. Her tits are just a few feet away from your face."
        $ mc.change_locked_clarity(20)
        "You lick your lips, then instinctively lean forward, intent to give her nipples a little nibble..."
        if the_person.effective_sluttiness("bare_tits") > 40:
            "[the_person.possessive_title!c] moans when your lips make contact with her breast."
            "You feel her hand on the back of your head urging you to continue as you start to lick and suck on her nipple."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(30)
            $ the_person.change_obedience(1)
            "You spend several moments enjoying [the_person.possessive_title]'s teat before you sit back."
            "You glance at [the_person.title] as you resume eating your breakfast. Her face looks a little flushed."
        elif the_person.obedience >= 130:
            the_person "Hey, that's not part of it..."
            "[the_person.title] offers a token word of resistance, but obediently let's your mouth approach her body."
            "[the_person.possessive_title!c] gasps when your lips make contact with her breast."
            the_person "Ahhh that... okay... just for a little bit..."
            $ the_person.change_obedience(2)
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(30)
            "You spend several moments enjoying [the_person.possessive_title]'s teat before you sit back."
            "You glance at [the_person.title] as you resume eating your breakfast. Her face looks a little flushed."
        else:
            "A hand on your forhead stops you."
            the_person "Hey! That wasn't part of it. You can look, that's all."
            mc.name "Ah, sorry, I wasn't thinking. Of course [the_person.title], but they look amazing. Not even a little touch?"
            the_person "I... I mean... I guess if you go quickly..."
            "Before she can change her mind, you reach up and begin to fondle her chest."
            if the_person.has_large_tits:
                "They feel so heavy and hot in your hand. You would love to have her tits in your face as she bounces up and down on your cock..."
            else:
                "They are so perky and soft. You would leave to have her tits in your face as she bounces up and down on your cock..."
            $ the_person.change_obedience(2)
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(30)
            "For now though, you know better than to press your luck. You let go and continue eating your breakfast."
        "When you go back to eating, she quietly gets up from your bed."
        $ the_person.draw_person(position = "stand2", display_transform = character_right(zoom = 1.0))
    else:
        $ the_person.draw_person(position = "stand4")
        the_person "I don't feel comfortable with that [the_person.mc_title]. You'll have to enjoy it from there."
        mc.name "Alright, I can do that."
        "You resume eating your breakfast, but check out [the_person.possessive_title]'s chest between bites."
        "She start to blush a bit, embarrassed by being exposed to you like this."
        $ the_person.change_arousal(10)
        $ the_person.change_slut(1, 40)
        $ mc.change_locked_clarity(20)
    "As you keep working on your meal, you are ready for more."
    mc.name "Alright, now your bottoms."
    the_person "Hmmm, okay..."
    $ the_person.draw_person(position = "back_peek")
    "She turns away from you and starts to remove her bottoms."
    $ the_person.change_obedience(1)
    $ the_person.strip_to_vagina(prefer_half_off = False, position = "back_peek")
    $ mc.change_locked_clarity(25)
    mc.name "Wow mom, you look amazing. Can I get a closer look?"
    if the_person.obedience >= 130 or the_person.effective_sluttiness("bare_pussy") > 20:
        if the_person.effective_sluttiness("bare_pussy") > 30:
            the_person "Of course, what is the point of getting naked if you can't get a good look at my ass?"
        else:
            the_person "Oh... If you want me to, [the_person.mc_title]."
        $ the_person.draw_person(position = "standing_doggy", display_transform = character_center_flipped(zoom = 1.2))
        $ the_person.change_arousal(15)
        "[the_person.title] comes around to the side of the bed, the turns around and bends over, giving you an incredible view of her ass."
        "The damp lips of her pussy are just barely peaking out at the bottom of her crack."
        menu:
            "Finger her" if the_person.effective_sluttiness("touching_vagina") >= 30 or the_person.obedience > 140:
                mc.name "Wow [the_person.title], you look like you are enjoying this as much as I am... Look how wet you are."
                "You reach toward her."
                the_person "Ahh, yeah I admit it is getting me... AHH!"
                "You fingers make contact with her slit. You slide them up and down a couple times, marvelling at how wet she already is."
                $ the_person.change_arousal(20)
                $ mc.change_locked_clarity(40)
                $ the_person.break_taboo("touching_vagina")
                "Her back arches and she moans as you slide two fingers into her."
                the_person "Oh [the_person.mc_title]... this was supposed to be for you to enjoy and to have a good day..."
                mc.name "And I am absolutely going to enjoy this and this amazing view is going to be stuck in my head all day, motivating me to work hard."
                "You begin to stroke the inside of [the_person.possessive_title]'s cunt. Her body responds and she begins to move her hips involuntarily for you."
                $ the_person.change_arousal(20)
                $ mc.change_locked_clarity(40)
                the_person "Oh god [the_person.mc_title], you're making mommy feel so good...!"
                "You push your to fingers deep inside her, then curl them forward, rubbing against her g-spot."
                "She responds immediately, her back arching even further and pushing her ass back against your hand."
                $ the_person.change_arousal(40)
                $ mc.change_locked_clarity(40)
                the_person "Oh baby right there! OH Fuuuuck...."
                "Her body suddenly goes rigid as she starts to cum."
                $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 50, half_arousal = False)
                "[the_person.possessive_title!c]'s entire body shakes as she orgasms. You eagerly stroke her g-spot to prolong her pleasure."
                the_person "Ohhhh! Mmmmm ohhh fuck... Ahhh! Oh honey... AHHH!"
                "When you feel the movements of her hips slow down and then stop, you do the same. You slowly pull your fingers out of her."
                the_person "Oh god... my legs... ohhhh..."
                "She drops to her knees and turns around. Her face now rests on the side of your bed with her knees on the floor beside it."
                $ the_person.draw_person(position = "blowjob")
                "Your fingers are coated in her cum. You move them towards her face."
                mc.name "Be a good girl now and clean these off."
                "She looks up and sees your fingers. Without thinking, she obediently opens her mouth and you slide your fingers into her mouth."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "[the_person.possessive_title!c] closes her eyes and eagerly starts to suck on your fingers. Her tongue swirls around them, tasting herself on your fingers."
                "She even begins to bob her head forward and backward, her lips making little smacking noises as she eagerly sucks off your fingers."
                $ mc.change_locked_clarity(50)
                "Suddenly she realises what she is doing and how it must look to you. She pops off your fingers."
                $ the_person.draw_person(position = "blowjob")
                $ the_person.increase_opinion_score(get_random_from_list(["being submissive", "giving blowjobs"]), max_value = 2)
                the_person "Ah... there... that should be good enough..."
                mc.name "Yes... that was amazing..."
                "She gives you a sheepish smile before standing up on wobbly legs."

            "Finger her\n{menu_red}Requires: Sluttiness{/menu_red} (disabled)" if the_person.effective_sluttiness("touching_vagina") < 30:
                pass

            "Grope her ass":
                "You take a bite of your breakfast. You glance over at [the_person.title]'s ass, just begging to get felt up..."
                "You give her ass a playful swat."
                $ play_spank_sound()
                $ the_person.change_arousal(5)
                $ mc.change_locked_clarity(30)
                if the_person.effective_sluttiness("bare_pussy") > 30:  #She likes it
                    the_person "Oh! Mmmm..."
                    "You run your hand along the soft curves of her buttocks, making sure to grope her a few times."
                    "She seems to really enjoy the attention. Her wiggles her hips slowly, encouraging your hand to keep going."
                    $ the_person.change_arousal(15)
                    $ mc.change_locked_clarity(30)
                else:
                    the_person "Hey! I thought you just wanted to look."
                    mc.name "What? I never said I ONLY wanted to look. An ass this nice needs to be grabbed and spanked."
                    $ play_spank_sound()
                    $ the_person.change_arousal(5)
                    $ mc.change_locked_clarity(30)
                    "You give her ass another smack, then continue to grope it. She stands there in quiet obedience."
                    $ the_person.change_obedience(2)
                "You go back to eating your breakfast. Once in a while you give [the_person.possessive_title]'s ass some attention with your hands."
                "All too fast, the food on your plate dwindles and soon you are taking your last bite."

    else:
        the_person "Sorry, I don't think that would be a good idea. You'll have to enjoy it from there, [the_person.mc_title]."
        mc.name "Alright."
        "You resume eating your breakfast, but check out [the_person.possessive_title]'s ass between bites."
        $ the_person.change_slut(1, 40)
        $ mc.change_locked_clarity(20)

    "When you finish, [the_person.title] picks up the tray with your dishes."
    $ the_person.draw_person(position = "stand2", display_transform = character_right(zoom = 1.0))
    mc.name "That was so good. Thanks again [the_person.title]."
    the_person "I'll take this to the kitchen. I hope you have a great day!"
    mc.name "Thanks!"
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title!c] leaves your room. You look at your phone and see your alarm coming up in three minutes. You turn it off."
    "Time to get the day started."
    return

label mom_breakfast_prog_scene_scene_2(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if not scene_transition:
        "[the_person.possessive_title!c] watches as you dig in to your breakfast, then speaks up."
        the_person "You umm... want the same treatment as last time while you eat?"
        mc.name "You mean a handjob?"
        the_person "Yeah..."
        mc.name "Yeah that would be great! I really appreciate it [the_person.title]."
        "You see quick smile on her face as she starts to walk over to the bed."
    if the_person.tits_available and the_person.tits_visible:
        pass
    else:
        "Without prompting, [the_person.title] takes her top off."
        $ the_person.strip_to_tits(prefer_half_off = False)
    "[the_person.possessive_title!c] starts walking over to your bed, then sits right next to you."
    $ the_person.draw_person(position = "sitting", display_transform = character_right_flipped(zoom = 1.2))
    $ mc.change_locked_clarity(20)
    "She is so close to you. You lick your lips as you check out her tits which are just a few inches away..."
    "[the_person.possessive_title!c] leans forward a bit, reaching down to take your cock out. When she does, you can't resist."
    "You lean forward, your tongue running along one of [the_person.title]'s sensitive nipples."
    if the_person.is_lactating:
        the_person "Ahhh... be careful, I might let down... I don't want to make a mess..."
        "[the_person.title] is lactating. Her fresh cream could make for a delicious dessert."
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(20)
    else:
        the_person "Mmmmm!..."
        $ the_person.change_arousal(10)
    $ play_moan_sound()
    "You run your tongue in circles around her nipple a few more times while she finishes exposing your manhood."
    "Once exposed, you feel her soft hand start to stroke you."
    $ the_person.break_taboo("touching_penis")
    if scene_transition:
        mc.name "Mmm. Can you go nice and slow? I want to finish my breakfast before I finish... you know..."
        the_person "Oh my... yeah... I'll go slow [the_person.mc_title]..."
    else:
        mc.name "Mmm. Can you go nice and slow again? It feels amazing to draw it out for a while."
        the_person "Of course [the_person.mc_title], let mommy make you feel good..."
    $ mc.change_locked_clarity(20)
    $ mc.change_arousal(20)
    "[the_person.possessive_title!c] strokes you slowly with her soft hand open. Even though it is dry, her soft skin feels great."
    "You take several bites of sausage and eggs, but soon [the_person.title]'s quivering tit flesh draws your attention."
    "As she strokes your cock with her hand, her chest jiggles. You're eager for another taste..."
    "You swallow a bite of breakfast, then lean forward with your tongue out, licking circles around her nipple."
    $ play_moan_sound()
    if the_person.is_lactating:
        the_person "Mmm!... Oh [the_person.mc_title] be careful... I'm really full this morning..."
        "You aren't quite ready for your dessert yet, so you make sure to just tease her for now."
        $ the_person.change_arousal(25)
    else:
        the_person "Mmm!... oh [the_person.mc_title], you make me feel so good..."
        "You flick her nipple up and down a few times with your tongue."
        $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(20)
    $ mc.change_arousal(20)
    "[the_person.possessive_title!c] changes her grip, going from open hand to closed, keeping her strokes soft but with a slight twisting motion."
    "The change feels great, but she keeps the pace slow. You get back to eating breakfast."
    "You take a long sip of coffee."
    if the_person.is_lactating:
        "You usually enjoy your coffee black, but you get a naughty idea."
        mc.name "Hang on a second."
        "[the_person.title] stops stroking you. You reach over with one hand and start to grope the breast farthest away from you."
        the_person "Ohhh... [the_person.mc_title], you're going to make mommy let down... be careful... ahhhh!"
        $ the_person.change_arousal(25)
        $ play_moan_sound()
        if the_person.lactation_sources > 2:    #Heavy milk production
            "Milk dribbles out from he breast, and then starts to spray. You start to catch it in your coffee mug."
        else:
            "Milk begins to dribble out from her breast in a slow stream. You catch it with your coffee mug."
        mc.name "Sorry, I just wanted a little fresh cream."
        the_person "Aaahhh, I see..."
        "You grope her for a while, catching all of her fresh milk in your coffee mug. The stream slows to a dribble and then stops."
        $ mc.change_locked_clarity(20)
        "You take a sip of your coffee."
        if the_person.lactation_sources > 2:
            "[the_person.title]'s copious milk has tempered your coffee's bitterness with a sweet and creamy flavour."
            "It tastes better than any creamer you've used before."
        else:
            "[the_person.title]'s milk has added a touch of sweetness and given the coffee a slightly creamy texture."
            "Even though you normally drink your coffee black, you appreciate the extra flavour."
        "You set your coffee down while [the_person.possessive_title] resumes the handjob."
    "A few more bites of breakfast. You are about halfway finished."
    "[the_person.title] shifts her weight a bit, leaning up against the headboard, putting her head on her shoulder as she strokes you."
    if the_person.opinion.kissing >= 0:
        "[the_person.possessive_title!c] nuzzles her nose against you neck, and starts to kiss you along your jaw, just below your ear."
        "The sounds of her gentle kisses in your ear gives you shivers and goosebumps."
    else:
        "The feeling of [the_person.possessive_title] cuddling against your shoulder is comforting, giving you a little shiver."
    "She lifts her head up and whispers into your ear."
    the_person "You make mommy so happy. Finish your breakfast so I can make you cum [the_person.mc_title]..."
    $ mc.change_locked_clarity(20)
    $ mc.change_arousal(20)
    if scene_transition:
        "[the_person.title]'s dirty talk catches you off guard. You take a couple quick bites of your food while she keeps whispering in your ear."
        the_person "I want to feel your big cock cum in my hand. I want to watch you cum, it makes me feel so sexy..."
    else:
        "Oh god, [the_person.title] is starting with the dirty talk again. You take a couple quick bites of your food while she keeps whispering in your ear."
        the_person "I love it when I feel your big cock cum in my hand. It makes me feel so sexy."
    mc.name "Oh my god... [the_person.title]..."
    "You take a few more bites of breakfast, barely tasting it. All you can think about now is that soft hand stroking you."
    "[the_person.possessive_title!c] shifts back to sitting all the way up. Her chest is next to your face again."
    "She brings her hand to her mouth, the gives it a generous spit. She rubs it onto your erection, finally getting it lubed up."
    "[the_person.title] repeats the process a few times, then begins stroking you again. She strokes you slowly, but with her wonderfully soft, lubricated hand."
    $ mc.change_locked_clarity(20)
    $ mc.change_arousal(20)
    "Two bites left. You chew fast and swallow each bite, finally finishing your food. You set the tray to the side, then turn your face into [the_person.title]'s chest."
    $ play_moan_sound()
    "You open your mouth and lick her nipple. You run your tongue in circles around it a few times and then latch on, sucking on it eagerly."
    "Her free hand comes up to the back of your head, running her fingers through your hair while holding your head to her breast."
    if the_person.is_lactating:
        the_person "Ohhh my god [the_person.mc_title]..."
        $ the_person.change_arousal(20)
        if the_person.lactation_sources > 2:
            "[the_person.possessive_title!c] milk begins to spurt out and into your eager mouth."
            "Her maternal cream tastes sweet and mild and flows rapidly into your mouth. You swallow it all in big gulps."
        else:
            "[the_person.possessive_title!c] milk begins to slowly stream into your eager mouth."
            "Her maternal cream tastes sweet and mild. You swallow your delicious dessert as it flows."
    else:
        the_person "Ahhh, that's it [the_person.mc_title]..."
        $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(40)
    "[the_person.title] starts stroking you rapidly, driving you to finish. Her hand makes wet, sloppy noises as she jerks you towards completion."
    "You moan into her body as you keep sucking on her tits as you start to orgasm."
    $ ClimaxController.manual_clarity_release(climax_type = "hand", person = the_person)
    "You reach your limit and start to pulse your load out in thick ropes, coating [the_person.possessive_title]'s hand."
    $ the_person.change_arousal(25)
    if the_person.arousal >= the_person.max_arousal:
        the_person "Oh my god! [the_person.mc_title]... OH!"
        "The hand on the back of your head presses your face urgently into her breast. Suddenly you her entire body quake."
        $ the_person.have_orgasm()
        "[the_person.possessive_title!c]'s body quivers again, and again. She is having an orgasm too!"
        "Your orgasm is finishing up, but you eagerly devour [the_person.title]'s titflesh, licking and sucking as she cums."
        if the_person.is_lactating:
            "Her warm, delicious milk is making this one of the most amazing sexual encounters you have ever experienced."
        "The grip on the back of your head starts to lessen as her orgasmic waves slow to a stop."
        the_person "Ohhh fuck... [the_person.mc_title], you made me cum..."
        $ the_person.change_obedience(3)
        "When she lets go, you unlatch and lean back against the headboard."
    else:
        "She keeps stroking you until you're completely spent, then lets go."
    "She looks down at her hand which is covered with a thick layer of your semen."
    if the_person.opinion.drinking_cum > 0:
        the_person "Wow! What a load... I hate to let it go to waste..."
        "She brings her hand up to her mouth and begins to lick your cum off of it."
        $ play_swallow_sound()
        "You grab a napkin and wipe the cum off that landed on your stomach as she gulps down the rest of your load."
        $ the_person.cum_in_mouth()
    else:
        the_person "Wow... that is certainly a healthy load..."
        "She grabs a napkin off your tray and starts to wipe her hand off. You grab the last napkin and use it to wipe off your stomach."
        "She can't quite clean her hand off completely, there is just too much for one napkin."
        the_person "Ahh, guess I should go wash up."
    "[the_person.title] stands up and gathers your dishes."
    $ the_person.draw_person(position = "stand2", display_transform = character_right(zoom = 1.0))
    mc.name "That was so good. Thanks again [the_person.title]."
    the_person "I'll take this to the kitchen. I hope you have a great day!"
    mc.name "Thanks!"
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title!c] leaves your room. You look at your phone and see your alarm coming up in three minutes. You turn it off."
    "Time to get the day started."
    return

label mom_breakfast_prog_scene_scene_3(the_group, scene_transition = False):
    $ the_person = the_group[0]
    $ eager_blowjob = False
    $ finish_type = the_person.favourite_opinion(["drinking cum","cum facials","being covered in cum"])  #Use the new opinion method here to make jennifer decide how to finish off mc.
    if not scene_transition:
        if the_person.event_triggers_dict.get("oral_revisit_complete", False) and the_person.opinion.giving_blowjobs >= 0:
            $ eager_blowjob = True
            "[the_person.possessive_title!c] watches as you dig in to your breakfast, then speaks up."
            the_person "You umm... want the same treatment as last time while you eat?"
            mc.name "You mean a blowjob?"
            the_person "Yeah..."
            mc.name "Yeah that would be great! I really appreciate it [the_person.title]."
            "You see quick smile on her face as she starts to walk over to the bed."
        else:
            "[the_person.possessive_title!c] stands there awkwardly as you dig in to your breakfast."
            mc.name "So... How about a blowjob? Like last time?"
            "She sighs."
            the_person "I was afraid you would say that..."
            mc.name "I know it isn't your favourite, but it feels so good [the_person.title]..."
            the_person "Ugh... alright honey... just one more time, okay?"
            mc.name "Of course."
            "You hide your smile behind a bite of scrambled eggs. You know this isn't the last time, but you go along with it for now."
    "[the_person.possessive_title!c] starts walking over to your bed."
    if not the_person.tits_available and not the_person.tits_visible:
        "As she walks over, she takes her top off."
        $ the_person.strip_to_tits(prefer_half_off = False)
    $ mc.change_locked_clarity(30)
    "She gets up on your bed and leans forward. She reaches forward and pulls down your underwear. Your cock springs free."
    $ the_person.change_arousal(10)
    "She gives a little gasp when she sees it. You spread your legs a bit to give her room to get between then, and she leans forward."
    $ the_person.draw_person(position = "blowjob", display_transform = character_center_flipped(zoom = 1.2))
    $ mc.change_locked_clarity(30)
    "You can feel her warm breath, her face inches your from erection."
    mc.name "Go nice and slow. There's no reason to rush, it will take me a while to finish my breakfast."
    if eager_blowjob:
        the_person "I'll try... but it looks so yummy..."
        if finish_type == "drinking cum":
            the_person "I can't wait to swallow all your hot cum..."
        elif finish_type == "cum facials":
            the_person "Do you want to cum all over mommy's face? That would be so hot..."
        elif finish_type == "being covered in cum":
            the_person "Maybe you could cover my tits with your cum? It feels so good when you cover me with your cum..."
        $ mc.change_locked_clarity(30)
        mc.name "Uhhh, yeah... that sounds great. I guess you do whatever you want with it when I cum."
        the_person "Okay [the_person.mc_title]. Just leave it to mommy, just enjoy your breakfast, and I'll enjoy mine."
    else:
        the_person "You'll finish when you finish. Don't press your luck!"
    "You watch as [the_person.possessive_title] leans forward the last couple of inches. She sticks her tongue out and runs it along the length of your shaft."
    $ the_person.break_taboo("sucking_cock")
    "The pleasure of that first, wet contact sends a shiver down your spine."
    $ mc.change_locked_clarity(40)
    $ mc.change_arousal(10)
    "[the_person.title]'s tongue runs a few circles around your tip, gathering up a few drops of your pre-cum. Then she opens her mouth."
    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob", display_transform = character_center_flipped(zoom = 1.2))
    "[the_person.possessive_title!c]'s soft lips slide down the first third of your cock."
    if eager_blowjob:
        the_person "Mmmm..."
        "A soft moan vibrates around dick, and it feels amazing."
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(5)
    "Obeying your request for now, [the_person.title] starts to slide her mouth up and down slowly, taking her time as she services you."
    "You resume eating your breakfast while [the_person.possessive_title] dutifully sucks your cock."
    $ mc.change_locked_clarity(40)
    $ mc.change_arousal(20)
    $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
    "After a bite of eggs, you pick up your cup of coffee and start to take a sip. You hear [the_person.title]'s lips smack and she pulls off for a second."
    "She licks down the side of the shaft, then her face continues down and she starts to lick your scrotum while one hand grasps the shaft and starts to stroke it."
    "You put your hand on her hand and stop it."
    mc.name "Just use your mouth, we want to make this last, right?"
    if eager_blowjob:
        the_person "Ahh sorry... I just like to make you feel good..."
        "She removes her hand but keeps licking, occasionally sucking lightly on your testicles."
        $ mc.change_locked_clarity(40)
        $ mc.change_arousal(10)
        $ the_person.change_obedience(2)
    else:
        "She rolls her eyes at you but obediently removes her hand as she continues licking your scrotum."
        $ the_person.change_obedience(2)
        $ mc.change_locked_clarity(30)
        $ mc.change_arousal(10)
    "After a while, [the_person.title] moves back up, licking up and down your length several times."
    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob", display_transform = character_center_flipped(zoom = 1.2))
    $ mc.change_locked_clarity(40)
    $ mc.change_arousal(20)
    "At the tip, she licks up more of your pre-cum, then opens her mouth and takes your tip again."
    "You are about halfway through enjoying your delicious breakfast while being treated to the soft sounds of [the_person.title]'s lips smacking and soft moans as she sucks your cock."
    "She is taking her time, prolonging your pleasure so you don't cum too quickly and have plenty of time to finish your meal."
    "You enjoy a crunchy bite of bacon while the soft waves of suction on your erection gives you another shiver of pleasure."
    if eager_blowjob:
        "[the_person.possessive_title!c] is picking up her pace some, and it feels so good you are forced to intervene."
        $ mc.change_locked_clarity(40)
        $ mc.change_arousal(10)
        "You put your hand on the back of her head, slowing her down. She looks up at you sheepishly."
        $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
        "Her mouth pops off you for a moment."
        the_person "Sorry, it's so hot I started to get carried away there for a moment..."
        mc.name "It's okay. I appreciate the enthusiasm, and don't worry, I'm almost done eating."
        the_person "MMmmm... okay..."
        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob", display_transform = character_center_flipped(zoom = 1.2))
        "You feel your cock twitch as she takes the tip in her mouth again. She's got you right on the edge."
    $ mc.change_locked_clarity(40)
    "You keep eating the last of your breakfast, but it is starting to get difficult to concentrate."
    "[the_person.possessive_title!c] is going slow, but every caress of her tongue and soft moan makes your erection twitch in pleasure."
    mc.name "Mmmm... ugh!"
    "You let out a moan of pleasure. You have two bites of food left."
    $ mc.change_locked_clarity(40)
    $ mc.change_arousal(20)
    "You bring one to your mouth but don't even taste it. All your brain can do is process the pleasure radiating from [the_person.title]'s hot mouth."
    "You set your fork down. Fuck it! You need to cum now!"
    mc.name "Oh fuck, [the_person.title], I'm gonna cum!"
    if finish_type == "drinking cum":
        if eager_blowjob:
            the_person "Mmmmmmm!"
            "Suddenly, [the_person.possessive_title]'s lips descend all the way to the base of your cock, with the tip going down her throat."
            $ mc.change_locked_clarity(50)
            "Her eager moans reverberate pleasure all around your shaft, and your hips begin to thrust all on their own up into her mouth as you start to cum."
            "You grab her hair with both hands, holding her head in place as you start to cum directly down her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "throat", person = the_person)
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob", display_transform = character_center_flipped(zoom = 1.2))
            $ play_gag_sound()
            "[the_person.title]'s throat spasms a couple of times as she gags, but she dutifully takes wave after wave of cum."
            "Orgasmic pulses begin to subside and you let go of her hair. She slowly backs off and then gasps for air."
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
            the_person "Gahhh! Ugh... ummm... mmmmm..."
            "She catches her breath and the start to lick up some of the cum that has leaked from the corners of her mouth."
        else:
            "[the_person.possessive_title!c] reaches up and starts to rapidly stroke your shaft while leaving the tip of your cock in her mouth."
            "You run your hand through her hair as you start to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob", display_transform = character_center_flipped(zoom = 1.2))
            "[the_person.title] dutifully takes wave after of cum in her mouth. A little bit leaks out of the corners of her mouth."
            "Your orgasmic pulses begin to subside. When you are done, she releases your cock with plop, and you can hear it as she gulps down your cum."
            $ play_swallow_sound()

    if finish_type == "cum facials":
        $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
        if eager_blowjob:
            the_person "Oh! Cum all over mommy's face!"
            "Suddenly, [the_person.possessive_title] backs off and starts stroking you eagerly with her hand."
            $ mc.change_locked_clarity(50)
            "Her eyes are locked to yours as she points your cock directly at her face as you start to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
            "She smiles as you paint her face with spurt after spurt of hot cum. One of them makes her jump when in hits her eyes, which she promptly closes."
            "[the_person.title] keeps stroking you until your orgasmic pulses stop."
            $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
        else:
            the_person "Why don't you cum on my face?"
            "[the_person.possessive_title!c] backs off and starts stroking you with her hand, pointing it at her face."
            $ mc.change_locked_clarity(30)
            "She closes her eyes as you being to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
            "She gives a slight smile as you paint her face with spurt after spurt of hot cum."
            "[the_person.title] keeps stroking you until your orgasmic pulses stop, then carefully opens her eyes."
            $ the_person.draw_person(position = "blowjob", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))

    if finish_type == "being covered in cum":
        $ the_person.draw_person(position = "kneeling1", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
        if eager_blowjob:
            the_person "Oh! Cover mommy's tits with your hot cum, [the_person.mc_title]!"
            "She jumps forward a bit and starts to eagerly stroke your cock with one hand. She runs her other arm beneath her chest, presenting her tits."
            $ mc.change_locked_clarity(30)
            "Her eyes are locked to yours as she points your cock directly at her chest as you start to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_person)
            $ the_person.cum_on_tits()
            $ the_person.draw_person(position = "kneeling1", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
            "She smiles as your paint her body with spurt after spurt of hot cum. She does her best to coat each breast evenly."
            "[the_person.title] keeps stroking you until your orgasmic pulses stop."
        else:
            the_person "Here, you can cum on my chest, [the_person.mc_title]."
            "She leans forward a bit and starts to stroke your cock with one hand. She runs her other arm beneath her chest, presenting her tits."
            $ mc.change_locked_clarity(30)
            "She closes her eyes as she points your cock directly at her chest as you start to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_person)
            $ the_person.cum_on_tits()
            $ the_person.draw_person(position = "kneeling1", emotion = "happy", display_transform = character_center_flipped(zoom = 1.2))
            "She slightly smiles as your paint her body with spurt after spurt of hot cum. She does her best to coat each breast evenly."
            "[the_person.title] keeps stroking you until your orgasmic pulses stop."
    mc.name "Oh my god, that was so hot..."
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title!c] stands up and starts to gather your dishes."
    the_person "I'll take this to the kitchen. I hope you'll be thinking about me today!"
    mc.name "Thanks! I'm sure I will."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title!c] leaves your room. You look at your phone and see your alarm coming up in three minutes. You turn it off."
    "Time to get the day started."
    $ del eager_blowjob
    return

label mom_breakfast_prog_scene_scene_4(the_group, scene_transition = False):
    $ the_person = the_group[0]
    $ mc.condom = False
    if not scene_transition:
        "[the_person.possessive_title!c] watches quietly as you dig in to your breakfast."
        if the_person.event_triggers_dict.get("vaginal_revisit_complete", False):
            the_person "Would you like me to ride your cock while you eat again?"
            mc.name "That sounds great! I love to watch your ass bouncing up and down on my lap."
            $ the_person.change_obedience(1)
            the_person "Okay [the_person.mc_title]."
        else:
            the_person "Did you want me to service your cock while you eat?"
            mc.name "Oh that would be great. Why don't you ride me reverse cowgirl again? Last time was so hot."
            the_person "[the_person.mc_title], we talked about this... What we did last time was taking things way too far."
            mc.name "I know, but I can't stop thinking about how amazing it was and how close it brought us together."
            mc.name "You enjoyed it a little bit too, didn't you?"
            the_person "Of course I enjoyed it, but that doesn't make it right..."
            mc.name "It is just for fun. You'll be facing away from me, you can just pretend you are fucking someone else."
            "She tries to keep resisting, but her body is betraying her brain. No matter how much her brain says to stop, her body refuses."
            the_person "Okay... if it would really mean that much to you. Just one more time, okay?"
            mc.name "Of course."
    if not the_person.vagina_available:
        "[the_person.title] starts to strip down while you pull down your pants and underwear."
        $ the_person.strip_to_vagina(prefer_half_off = False, position = the_person.idle_pose)
    else:
        "You pull down your pants and underwear."
    "Your cock springs free as she moves closer to your bed."
    #Determine if we use a condom.
    if the_person.event_triggers_dict.get("vaginal_revisit_complete", False):
        if the_person.has_breeding_fetish:  #She refuses with a condom
            the_person "Mmm, I was hoping you'd let me ride that monster of yours this morning."
            the_person "I love the feeling of your cum slowly leaking out of my pussy all day long..."
            $ the_person.change_arousal(10)
            the_person "I'll go slow, but make sure you give me all your cum nice and deep, okay honey?"
            mc.name "OF course [the_person.title]."
        elif the_person.wants_creampie:   #She highly prefers to go bare.
            if persistent.always_ask_condom:
                the_person "Is it okay if we do it raw? I love it when I feel you pump me full of cum..."
                menu:
                    "Use a condom":
                        $ mc.condom = True
                        mc.name "Not today."
                        "She seems disappointed, but obediently relents."
                        $ the_person.change_happiness(-2)
                        $ the_person.change_obedience(2)
                        the_person "Alright, if you insist..."
                    "Go bareback":
                        $ mc.condom = False
                        mc.name "Absolutely, nothing beats skin on skin."
                        $ the_person.change_arousal(10)
                        $ the_person.change_happiness(2)
                        $ the_person.change_obedience(1)
                        the_person "Mmm, you make mommy so happy when you say that."
            else:
                the_person "God you are so big. I can't wait to feel that virile monster flood my pussy with your cum!"
        elif the_person.opinion.bareback_sex > 0 or the_person.opinion.creampies > 0:   #She kind of wants it bare.
            the_person "Do you think we should use a condom? It might be kind of nice to go without it..."
            $ the_person.change_arousal(5)
            "She shudders for a second."
            the_person "That might be a bit risky though... I'm not sure I'll be able to pull off if I get too excited..."
            menu:
                "Use a condom":
                    $ mc.condom = True
                    mc.name "Let's use a condom this time, that way you won't have to worry about pulling off in time."
                    "You think you notice a hint of disappointment on her face."
                    $ the_person.change_happiness(-1)
                    $ the_person.change_obedience(2)
                    the_person "Ah, you're right of course. I don't know what I was thinking..."
                "Go bareback":
                    $ mc.condom = False
                    mc.name "Nothing beats skin on skin, I want to feel everything that ass of yours is doing to me while I watch it bouncing on my lap."
                    $ the_person.change_arousal(10)
                    $ the_person.change_happiness(2)
                    $ the_person.change_obedience(1)
                    the_person "Oh god, when you say it like that... let's do it!"
        else:
            the_person "I'm going to need you to wear a condom though... I don't want any accidents."
            "You roll your eyes, but you know that now isn't the time to fight this fight."
            mc.name "That seems unnecessary, but if you feel that strongly about it, okay."
            $ mc.condom = True
    else:
        $ mc.condom = True
        the_person "You're going to have to wear a condom though. We don't want any accidents!"
        mc.name "What do you mean we? I certainly wouldn't mind a little accident."
        the_person "Honey, that's not funny."

    if mc.condom:
        the_person "Do you have any condoms handy?"
        mc.name "Of course, I have a bunch in my nightstand."
        "[the_person.title] walks over and opens your night stand. She gasps when she sees you actually do have a lot. She picks one and closes the drawer."
        "She opens it up and leans over the bed."
        $ the_person.draw_person("kneeling1")
        "With one hand she grasps your cock at the base, and with the other she slowly rolls the condom on."
        "Once you are wrapped up, she gives you a couple of strokes with her hand."
    else:
        $ the_person.draw_person("kneeling1")
        "[the_person.title] slowly climbs onto the bed and reaches down, giving your erection a few gentle strokes with her hand."
    the_person "Oh god... I can't believe my son has such an amazing cock..."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(5)
    the_person "Alright, you just eat your breakfast, okay? Let mommy take care of this..."
    $ the_person.draw_person(position = "doggy", display_transform = character_center_flipped(zoom = 1.3))
    "[the_person.possessive_title!c] turns around and leans forward, onto her hands and knees."
    "You spread your legs as puts hers underneath yours, slowly backing up until she feels your cock pressing against her ass crack."
    "She reaches down between her legs and grasps it. She arches her back a bit and uses her hand to rub your erection along her slit a few times."
    $ the_person.change_arousal(15)
    the_person "Just want to make sure I'm ready for this..."
    "You just watch as [the_person.title] lubricates the tip of your dick with her arousal."
    $ mc.change_locked_clarity(50)
    if the_person.event_triggers_dict.get("vaginal_revisit_complete", False):
        the_person "Mmm, there we go, that should be good."
    else:
        if scene_transition:
            the_person "Oh god... I can't believe I'm about to do this..."
        else:
            the_person "Oh god... I can't believe I'm about to do this again... here we go..."
    "[the_person.possessive_title!c] pushes herself up a bit to get a good angle, while holding the base of your erection firmly with her other hand."
    "She moves her hips up, then slowly lowers them, using her hand to guide your cock inside of her."
    $ the_person.break_taboo("vaginal_sex")
    if not mc.condom:
        $ the_person.break_taboo("condomless_sex")
    "Inch by inch, she lowers her hips down, and your erection easily slides up inside of her."
    the_person "Gaaaahhhhh..."
    "[the_person.possessive_title!c] lets out a soft gasp when your cock finishes sliding inside of her."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    "You look down between your legs. Your erection is engulfed inside [the_person.title]'s cunt."
    "You grab a piece of bacon and take a delicious bite while you marvel at the curves of the incredible ass sitting on your lap."
    "The bottom of her soft cheeks indent a little where they meet your hips."
    if scene_transition:
        "Is this it? The ultimate pleasure and servicing [the_person.possessive_title] has ever given you. How could ever top this?"
        the_person "Oh god... is it okay if I start moving now? It feels amazing... I'm afraid I might start to feel TOO good..."
    else:
        "It seem surreal everytime she does this, servicing you dutifully, and meeting all of your physical needs so wonderfully."
        the_person "Alright, I'm gonna start moving now. If I get too eager and it is too hard to eat, let me know, okay?"
    mc.name "Don't worry. If you start to go to fast I'll slow you down."
    $ the_person.change_obedience(2)
    the_person "Mmm... okay..."
    "Going slowly, [the_person.title] moves her body forward, causing your cock to slowly pull out."
    "When she feels it almost out, she pushes back, causing your length to disappear inside her again."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    "It takes all your willpower to keep from ditching breakfast and grabbing her hips with both hands and fucking her with wild abandon."
    "But you know it will be better to take it slow. You want to let yourself edge for a while."
    "So instead of grabbing her hips, you settle for giving her ass a playful spank."
    $ play_spank_sound()
    $ the_person.change_arousal(10)
    "You pull the tray of food close to you and carefully get some eggs and sausage on the fork, bringing it to your mouth."
    "You enjoy your savoury breakfast while watching [the_person.possessive_title]'s ass move up and down in slow motion on your morning wood."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(15)
    $ mc.change_arousal(10)
    "Every soft bounce and hushed moan brings you closer to finishing, and it takes incredible concentration to keep eating your breakfast."
    "You glance at your tray. You are about halfway done eating. You close your eyes for a moment and take a deep breath, trying to will yourself to last longer."
    "A husky voice challenges your resolve."
    the_person "Oh my god [the_person.mc_title]... I... I can't hold on much longer... Ahhhh!"
    $ the_person.change_arousal(25)
    "[the_person.title] starts to speed up her hips, but you stop her. You grab her hips with both hands and slam her all the way down and hold her there."
    the_person "Ahhh! Oh fff... I'm gonna cum!"
    "[the_person.possessive_title!c]'s back arches but you keep her hips pinned in place as she starts to orgasm."
    $ the_person.have_orgasm(force_trance = False)
    "Her hole quivers and twitches around your cock. Even her puckered hole seems to spasm as you watch in awe."
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(10)
    "It is almost enough to push you over the edge and cum... almost."
    "When her orgasm subsides, you let go of her hips and take another bite of breakfast."
    the_person "Sorry I... I couldn't help it..."
    mc.name "Don't worry. The view was amazing."
    the_person "Give me a minute..."
    mc.name "No rush, I still have a good bit of breakfast to eat."
    "You focus on eating your breakfast quickly now. All the action has you so turned on, you feel your cock twitch now and then, on the edge of cumming."
    "When [the_person.title] starts to moves her hips again, the sensations almost overwhelm you."
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(10)
    "You look at your plate. Two more bites."
    "You grab them both on your fork and shove them in your mouth, chewing fast, then swallowing."
    "You are ready to finish. All it is going to take is a couple rapid strokes."
    mc.name "Oh my god... [the_person.title], I'm gonna cum!"
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    "You grab her hips with both hands. She moans when you give her a couple rapid thrusts while you pull her hips down at the same time."
    if mc.condom:
        the_person "That's it [the_person.mc_title]! Cum for me!"
        $ play_moan_sound()
        "She moans as she feels your erection twitching inside her. You dump your load into the condom, hoping it can contain it."
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        "When you finish, she leans back, leaving you inside of her for several more seconds, enjoying the last few moments of being filled."
        "Eventually she leans forward again. She reaches down between her legs, holding the condom in place as you slip out of her pussy."
        "[the_person.title] carefully slips the condom off and examines it."
        the_person "Wow... that's a lot of cum you made for mommy..."
        if the_person.opinion.drinking_cum >= 1:
            "You watch dumbfounded as she opens her mouth and tips the condom up, letting your cum slide out the bottom and into her mouth."
            $ the_person.cum_in_mouth()
            $ play_swallow_sound()
            "She swallows it all with a loud gulp."
            $ mc.change_locked_clarity(30)
        else:
            "She ties off the end and throws it in your trash can before standing up."
    else:
        if the_person.wants_creampie:
            the_person "That's it [the_person.mc_title]! Cum in mommy!"
            $ play_moan_sound()
            "She slams her ass down, leaving you with no choice but to fill her with your cum."
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
            $ the_person.cum_in_vagina()
            $ the_person.draw_person(position = "doggy", display_transform = character_center_flipped(zoom = 1.3))
            "[the_person.possessive_title!c] moans as the first wave of your cum floods her [the_person.pubes_description] pussy. She rocks her hips back and forth on top of you as you dump your load inside her."
            "[the_person.title] stays still for several more seconds after you finish, reveling in the sensations of her creampie."
            the_person "Mmm... that was good... Alright, this might be a little messy..."
            "She carefully lifts her hips. When your cock slides out, your cum leaks out and lands on your stomach."
            if the_person.opinion.drinking_cum >= 1:
                the_person "Oh! Let me get that..."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob", display_transform = character_center_flipped(zoom = 1.3))
                "She quickly turns around and licks up the cum off your body, swallowing it all with a loud gulp."
                $ play_swallow_sound()
                $ mc.change_locked_clarity(30)
                if the_person.opinion.giving_blowjobs >= 1:
                    "She keeps going, kissing down your abdomen to your cock, which is still slick with your combined juices."
                    "[the_person.possessive_title!c] licks up and down your shaft, then opens her mouth and takes the entire length down her throat, her tongue running circles around it."
                    $ play_moan_sound()
                    $ mc.change_locked_clarity(30)
                    "She gives a little moan as she finishes cleaning you off with her mouth. Her lips smack when they pull away from the tip."
            else:
                the_person "Here... use this..."
                "She grabs a napkin from the tray and hands it to you. You wipe up the cum with the napkin, then throw it on the tray."
        else:
            "[the_person.possessive_title!c] lifts her hips off you, your twitching cock suddenly cold and aching to be back inside her."
            "She reaches down between her legs, moving your member between her ass cheeks with her hand."
            the_person "Oh my god, do it [the_person.mc_title]. Mommy wants you to cover her ass with your cum!"
            "You don't have time to respond before the first wave of cum erupts from your cock."
            $ the_person.cum_on_ass()
            $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
            $ the_person.draw_person(position = "doggy", display_transform = character_center_flipped(zoom = 1.3))
            "[the_person.title] rocks her hips gently up and down, your erection hot dogging between her cheeks as your orgasm begins."
            "You cum splashes all over her ass as she moves her hips."
            "When the last of your cum splashes onto her ass, she stops stroking you."
            "You lay back and take a few moments to enjoy the view."
            $ mc.change_locked_clarity(30)
            the_person "Mmmm, wow that was so good..."
            if the_person.opinion.giving_blowjobs >= 1:
                the_person "I bet you're a mess... let mommy clean you up..."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob", display_transform = character_center_flipped(zoom = 1.3))
                "She turns around and leans forward and begins to lick up and down your cock."
                "She opens her mouth and takes the entire length down her throat, her tongue running circles around it."
                $ play_moan_sound()
                $ mc.change_locked_clarity(30)
                "She gives a little moan as she finishes cleaning you off with her mouth. Her lips smack when they pull away from the tip."

    $ the_person.draw_person(position = "stand2")
    "[the_person.title] slowly stands up, her legs wobbling slightly."
    mc.name "That was amazing [the_person.title]. An absolutely perfect way to start my day."
    the_person "Ahhh, thank you honey, I quite enjoyed it also."
    "[the_person.possessive_title!c] starts to gather your dishes."
    the_person "I'll take this to the kitchen. I hope you'll be thinking about me today!"
    mc.name "Thanks! I'm not sure I'll be able to think about anything else."
    "She blushes but stays quiet."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title!c] leaves your room. You look at your phone and see your alarm coming up in three minutes. You turn it off."
    "Time to get the day started."
    return
