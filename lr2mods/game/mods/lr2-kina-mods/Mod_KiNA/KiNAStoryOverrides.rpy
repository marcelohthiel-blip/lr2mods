#Counter = KSO01

#Overrides contained storyline that doesnt considers alternative scenarios. For example, Sarah first date fails to considers the scenario where Mom working for us, thus already knows Sarah fro the office.

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["girlfriend_wakeup_spooning_label"] = "tweaked_girlfriend_wakeup_spooning_label"
    config.label_overrides["mom_girlfriend_intro"] = "take_mom_as_girlfriend"
    config.label_overrides["sister_girlfriend_intro"] = "take_sis_as_girlfriend"
    config.label_overrides["mom_work_secretary_replacement_intro"] = "mom_secretary_replacement_intro"
    config.label_overrides["mom_date_intercept"] = "mom_date_blocker"
    config.label_overrides["stephanie_nora_teamup_choose_trainable_label"] = "stephanie_nora_3some_choose_trainable_label"

label tweaked_girlfriend_wakeup_spooning_label(the_person):
    $ the_person.draw_person(position = "walking_away")
    "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
    "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
    $ mc.change_locked_clarity(50)
    if the_person.has_large_tits:
        "Your hands cup and squeeze one of her [the_person.tits_description]. It's so full and hot, it feels so good in your hands."
    else:
        "Your hand cups one of her [the_person.tits_description]. It's so soft and warm, it feels good in your hand."
    $ play_moan_sound()
    the_person "Mmmmmmmm......"
    "[the_person.title] moans but doesn't stir. Maybe you could surprise her with a little good morning dicking."
    menu:
        "Try to slide yourself in":
            pass
        "Get ready for the day":
            "Thinking about your tasks for the day, you feel yourself get a bit anxious about wasting the morning."
            "You get up and head for the bathroom to take a leak."
            "When you come back, [the_person.title] is awake."
            $ the_person.draw_person(position = "missionary")
            the_person "Good morning! I slept great."
            $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            $ the_person.draw_person(position = "stand3")
            "You both get ready for the day before heading out."
            $ clear_scene()
            return
    "Your cock is already hard, being up against [the_person.title], but she may not be fully wet yet."
    "You spit into your hand and rub it on your dick a few times, getting it lubed up."
    $ the_person.increase_vaginal_sex()
    "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
    "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
    the_person "Oh [the_person.mc_title]. Mmmmmm..."
    "She's asleep, but is still responding to your touch. She must be a heavy sleeper! Or maybe she is just really worn out from last night..."
    "You give her a few gentle, smooth strokes. You can feel her pussy getting wetter with each stroke as her body begins to respond to the stimulation."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "With her legs closed and on her side like this, her pussy feels really tight. You can feel her gripping you every time you start to pull it out."
    $ mc.change_arousal(15)
    "Your reach around her with your hand and grab one of her tits. You start to get a little rough with her and pinch and pull at one of her nipples."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    the_person "Mmm, that feels so... wait... [the_person.mc_title]?"
    $ the_person.draw_person( position = "back_peek", emotion = "happy")
    "[the_person.possessive_title!c] wakes up and looks back at you smiling."
    the_person "Oh my god that feels so good... Baby you know how to give a wakeup call, holy fuck!"
    "Encouraged by her words, you reach your hand down and lift her leg, giving you a better angle for deeper penetration."
    "You pick up the pace and begin to fuck her earnestly."
    $ the_person.change_arousal(30) #70
    $ mc.change_locked_clarity(30)
    the_person "Oh yes that feels so good, fuck me good!"
    "She reaches down and holds her leg for you, freeing up your hand. You reach down between her legs and start to play with her clit."
    "Her ass is making smacking noises now, every time your hips drive your cock deep inside her."
    $ the_person.change_arousal(40) #110
    the_person "Oh fuck, yes! YES!"
    $ mc.change_locked_clarity(30)
    "She shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
    $ the_person.have_orgasm()
    $ mc.change_arousal(20) #110
    mc.name "I'm gonna cum!"
    $ the_person.call_dialogue("cum_pullout")
    menu:
        "Cum inside":
            $ the_person.cum_in_vagina()
            $ the_person.draw_person( position = "back_peek")
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
            "You grab her hip and shove your cock deep and hold it there, cumming deep inside her."
            $ play_moan_sound()
            "She moans and gasps with every spurt."
            $ the_person.call_dialogue("cum_vagina")
            "Satisfied, you slowly pull out of her."
            the_person "That's certainly one way to start the day... holy hell."
        "Pull out":
            $ the_person.cum_on_ass()
            $ the_person.draw_person( position = "back_peek")
            $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
            "You pull out at the last second. Large, thick ropes of cum rocket out of your cock, coating her ass."
            the_person "Oh my god... it's so warm!"
            "When you finish you lay back, admiring your painting skills."
            the_person "That's certainly one way to start the day..."
    $ the_person.reset_arousal()
    $ mc.reset_arousal()
    "You lay in bed together for a little longer, but soon it is time to start the day."
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "stand4")
    "You both get ready for the day."
    if the_person in people_in_mc_home():
        $ random_reply = get_random_from_list(["Alright,love you!", "Alright, I need to get some things done today. See you!", "Alright, see you later!"])
        the_person "[random_reply]"
    else:
        the_person "Alright, I need to get some things done today. Thanks for the sleepover!"
    $ clear_scene()
    return

label take_mom_as_girlfriend(the_person):
    $ the_person.draw_person(emotion = "happy")
    mc.name "There's something important I need to talk you about [the_person.title]. Do you have a moment?"
    the_person "Of course, what do you want to talk about?"
    if not the_person.event_triggers_dict.get("mom_girlfriend_asked_before", False):
        $ the_person.event_triggers_dict["mom_girlfriend_asked_before"] = True
        mc.name "You've always been the most important woman in my life..."
        the_person "Aww..."
        mc.name "... and I feel like our relationship has evolved. I feel like you're more than just my mother now, and I want to be more than just your son."
        mc.name "I want to be your boyfriend."
        "[the_person.possessive_title!c] doesn't say anything for a long moment. At long last she sighs and smiles weakly."
        $ the_person.draw_person(emotion = "happy")
        the_person "[the_person.mc_title], that's so sweet of you to say, but that's really not something we can do."
    else:
        mc.name "I still want to make you my girlfriend. I don't care about anyone the way I care about you."
        $ the_person.draw_person(emotion = "happy")
        the_person "That really is sweet [the_person.mc_title], but I haven't changed my mind."

    the_person "It's natural for us to feel a connection, but you're young and the world is full of wonderful girls your own age to meet."
    the_person "Why would you want to be with someone old like me?"

    $ convinced = False

    menu:
        "I can provide for us!":
            if not the_person.event_triggers_dict.get("mom_girlfriend_provided_cash", False):
                mc.name "Because we make an amazing team, and I want to contribute even more."
                mc.name "You've worked your whole life to take care of me and [lily.fname]. When we're together I can help take care of both of you."
                "[the_person.possessive_title!c] seems unconvinced, but doesn't immediately turn you down."
                mc.name "Come on [the_person.title], let me prove it. Are there any bills we need to pay?"
                the_person "I suppose there is one thing that I certainly don't have the money for right now... but it's expensive!"
                the_person "The car has been giving me trouble every morning. I took it to a shop to have it looked at and repairs are going to cost five thousand dollars!"
                menu:
                    "Pay for the repairs\n{menu_red}Costs: $5000{/menu_red} " if mc.business.has_funds(5000):
                        "You pull out your phone and open up your banking app."
                        mc.name "No problem at all. Just one moment..."
                        the_person "[the_person.mc_title], you really don't have to do this! I'm sure I could have taken care of it eventually..."
                        mc.name "You shouldn't have to take care of it all by yourself. I want to be your partner in all of this!"
                        $ mc.business.change_funds(-5000, stat = "Family Support")
                        "You send [the_person.possessive_title] the money she needs and put your phone away again."
                        mc.name "There. The money should be in your account next time you check."
                        "She smiles and her eyes soften. She seems almost on the verge of tears."
                        the_person "[the_person.mc_title]... I don't know what to say..."
                        the_person "Okay, you've made your point. It would be nice to have someone to support me when I need it."


                        $ convinced = True
                        $ the_person.event_triggers_dict["mom_girlfriend_provided_cash"] = True

                    "Pay for the repairs\n{menu_red}Requires: $5000{/menu_red} (disabled)" if not mc.business.has_funds(5000):
                        pass

                    "Start saving up":
                        mc.name "Five grand? Whew, that's going to take me a little bit of time..."
                        the_person "It's fine, really. I'm sure I'll be able to pay for it eventually."
                        mc.name "Don't worry [the_person.title], I'm going to get the money together real soon."
                        the_person "If you do I promise I'll think about your... proposal. Deal?"
                        mc.name "Deal."
                        "She smiles warmly at you."
                        the_person "I must be the only mother in the world who has trouble with her son loving her {i}too much!{/i}"

            else:
                $ convinced = True
                mc.name "Because I want to take care of you, just like you always took care of me."
                mc.name "Remember the car? It's fixed because you treated me like your partner, not just your son."
                the_person "That's true, I wouldn't have been able to do it without you."
                the_person "And it would be nice to be with someone I can trust..."
                "She smiles and her eyes soften."
                the_person "Okay, you've made your point."

        "Order her to agree" if the_person.obedience >= 200:
            "You step closer to [the_person.possessive_title] and put your hand on the back of her neck. Her breath catches in her throat as she waits for you to speak."
            mc.name "Because I don't want to share you with anyone else. I want you to be mine, and only mine. Do you understand?"
            "She nods obediently, eyes wide and fixed on yours. She trembles slightly under your touch."
            the_person "Yes [the_person.mc_title], I understand. I'll be whatever you want me to be."
            $ convinced = True

        "Order her to agree\n{menu_red}Requires: 200 Obedience{/menu_red} (disabled)" if the_person.obedience < 200:
            pass

        "Think of the baby!" if persistent.pregnancy_pref > 0 and (the_person.has_child_with_mc or (the_person.knows_pregnant and the_person.is_mc_father)):
            mc.name "What about our baby, [the_person.title]. This isn't just about the two of us any more."
            if the_person.knows_pregnant:
                "[the_person.possessive_title!c] puts a hand on her stomach and sighs happily before returning her attention to you."

            else: #Pregnant before and already had the kid.
                pass

            the_person "I told you that I would take full responsibility for what happened. It was a happy little accident."
            mc.name "I want it to be more than an accident. I want this to be an experience we can share together."
            "She thinks for a long moment, then nods and smiles."
            the_person "You're right. I want to share this with you too."
            $ convinced = True

        "Think of the baby!\n{menu_red}Requires: Get her pregnant!{/menu_red} (disabled)" if persistent.pregnancy_pref > 0 and not (the_person.has_child_with_mc or (the_person.knows_pregnant and the_person.is_mc_father)):
            pass

        "Let it go":
            mc.name "You're being too hard on yourself [the_person.title]. Maybe you're right though, I should try dating someone else first."
            the_person "Of course I am. A mother is {i}always{/i} right when she's giving advice to her child."
            the_person "Don't worry [the_person.mc_title], I'll always be here when you need me."

    if not convinced:
        return

    the_person "We still need to be practical. A mother dating her own son, it's not something most people would agree with."
    if the_person.is_employee:
        the_person "Well, at least I don't have to worry about my boss..."
    elif the_person.has_job(unemployed_job):
        the_person  "What will the neighbours think?"
    else:
        the_person "I could even lose my job if my boss finds out!"

    $ convinced = False
    menu:
        "We shouldn't care what other people think!" if the_person.get_known_opinion_score("incest") > 0:
            $ convinced = True
            mc.name "We shouldn't hide our love just because some people may not agree with it."
            mc.name "You aren't ashamed of me, are you [the_person.title]?"
            the_person "What!? Of course not, you're the most important thing in the world to me! It's just... I..."
            "[the_person.possessive_title!c] stumbles over her words, then sighs in defeat."
            the_person "You're right, of course. We shouldn't hide anything. I'm just a little scared."
            mc.name "It's okay, I'll be with you the whole way through."

        "We shouldn't care what other people think!\n{menu_red}Requires: Positive incest opinion{/menu_red} (disabled)" if the_person.get_known_opinion_score("incest") <= 0:
            pass

        "We'll hide it from everyone" if mc.charisma >= 4 and the_person.charisma >= 4:
            $ convinced = True
            mc.name "You're right, we'll have to be very careful. When other people are around we'll just pretend to be a normal family."
            the_person "I'll even have to lie to my sister..."
            mc.name "I think that's true. Do you think you can do that?"
            "She thinks for a moment, then nods confidently."
            the_person "She was never very good at telling when I'm lying."

        "We'll hide it from everyone\n{menu_red}Requires: Both 4+ Charisma{/menu_red} (disabled)" if mc.charisma <4 or the_person.charisma < 4:
            pass

        #"You can stay at home all day. #TODO: Add support for this in a future update

        #"You can stay at home all day\n{menu_red}Requires: [mom.title] isn't working{/menu_red} (disabled)":

        "Let it go":
            mc.name "You're right, this could go really badly if we aren't prepared. We shouldn't rush things."
            the_person "I think that's a wise decision. Maybe it'll be easier for us one day. Or maybe you'll even meet another cute girl you like more than me."

    if not convinced:
        return

    the_person "I can't believe we might actually be doing this! What are we going to tell [lily.fname]?"
    the_person "I couldn't do this if she doesn't approve. I won't make her life difficult just for my own happiness."
    $ convinced = False
    menu:
        "We already have threesome together" if had_family_threesome():
            $ convinced = True
            mc.name "What do you mean she didn't approve of us? Threesome? You, me and her?"
            "[the_person.possessive_title!c] cheeks turns bright red at the mentioned threesome."
            the_person "Well... I guess... I'd be sharing my own son with my own daughter."
            $ random_comment = get_random_from_list(["I could teach her a thing or two about being in a relationship.", "I'm not worried, there's no replacement for a mother's love.", "You must make us both happy, you hear me."])
            the_person "[random_comment]"
            the_person "You will also take her as your girlfriend too, right? You have too!"
            if lily.is_girlfriend:
                $ already_knows = mom_knows_about_lily()
                mc.name "I am."
                if already_knows:
                    the_person "I forgot about that..."
                else:
                    $ the_person.event_triggers_dict["sister_girlfriend_mom_knows"] = True
            else:
                mc.name "I promise, [the_person.title]. I just wanted you to be my girlfriend first because she doesn't mean nearly as much to me as you do."
            the_person "At least I don't have to be worried she'd be dating a bad guy."
                
        "We already have threesome together\n{menu_red}Requires: Family Threesome{/menu_red} (disabled)" if not had_family_threesome():
            pass

        "I'll talk to her and explain everything":
            $ convinced = False #NOTE: this isn't a direct success, but it does enable other events
            mc.name "I'll talk to [lily.fname] and explain everything. I'm sure when she hears it all laid out she'll be happy for us."
            the_person "Well... if you think that will work, okay. I hope you're as convincing with her as you were with me."
            $ lily.event_triggers_dict["mom_girlfriend_ask_blessing"] = True
            $ the_person.event_triggers_dict["mom_girlfriend_waiting_for_blessing"] = True

        "Don't worry, I'm dating her too" if lily.is_girlfriend:
            $ convinced = True
            $ already_knows = mom_knows_about_lily()
            mc.name "If she had any problems she probably wouldn't be dating me too."
            if already_knows:
                the_person "I hadn't thought about that..."
            else:
                $ the_person.event_triggers_dict["sister_girlfriend_mom_knows"] = True
                the_person "You're dating [lily.name]? Oh my god, for how long?"
                mc.name "A while, but that's not important now. She doesn't mean nearly as much to me as you do."
            # "Vren" "The harem variant of this relationship is still under construction. It will be added in a future update!"
            # "Vren" "Until then enjoy having both girls as your girlfriend!"
            the_person "Well, I suppose if she's willing to date you she won't have any problems with me doing it too."
            the_person "I'm not worried, there's no replacement for a mother's love."

        "Don't worry, I'm dating her too\n{menu_red}Requires: Dating [lily.title]{/menu_red} (disabled)" if not lily.is_girlfriend:
            pass

        "She's too dumb to notice" if lily.int < 2:
            $ convinced = True
            mc.name "I don't think we'll have any issues with her. [lily.fname]'s... well, she's not terribly hard to trick."
            mc.name "As long as she doesn't catch us fucking I doubt she'll notice anything has changed."
            the_person "[the_person.mc_title], do you really have to be so crude?"
            the_person "... But you do have a point. Just a little discretion on our part and we won't have to bother her at all."

        "She's too dumb to notice\n{menu_red}Requires: [lily.title] 1 Int{/menu_red} (disabled)" if lily.int >= 2:
            pass

        "Let it go":
            mc.name "I don't think she'll take it well."
            the_person "Then we should wait. Maybe you'll even find a nice girl in the meantime."

    if convinced:
        "She takes a deep breath and nods her final approval."
        the_person "Okay then, I'll be your girlfriend [the_person.mc_title]!"
        call mom_girlfriend_setup(the_person, lily_knows = False) from _call_mom_girlfriend_setup_KSO01

    return

label take_sis_as_girlfriend(the_person):
    mc.name "[the_person.title], I want to ask you something important."
    "[the_person.possessive_title!c] nods and listens attentively."

    $ the_person.draw_person(emotion = "happy")
    if not the_person.event_triggers_dict.get("sister_girlfriend_asked_before", False):
        $ the_person.event_triggers_dict["sister_girlfriend_asked_before"] = True
        mc.name "I've been thinking about this—and you—for a while. We've grown really close, closer than I could imagine being with anyone else."
        mc.name "I want you to be my girlfriend. What do you say?"
    else:
        mc.name "I haven't stopped thinking about you. I still can't imagine being with anyone other than you."
        mc.name "I still want you to be my girlfriend. What do you say?"
    $ the_person.draw_person(emotion = "happy")
    "[the_person.title] smiles, but she seems conflicted."
    the_person "I love you, but I love you like a brother."
    the_person "I don't know if I could see you as anything {i}other{/i} than family."

    $ convinced = False
    $ most_done = None
    $ most_phrase = "do anything"

    if not the_person.has_taboo("vaginal_sex"):
        $ most_done = "vaginal"
        $ most_phrase = "fuck their brother"
    elif not the_person.has_taboo("anal_sex"):
        $ most_done = "anal"
        $ most_phrase = "get ass fucked by their brother"
    elif not the_person.has_taboo("sucking_cock"):
        $ most_done = "suck"
        $ most_phrase = "suck their brother's cock"
    elif not the_person.has_taboo("kissing"):
        $ most_done = "kiss"
        $ most_phrase = "make out with their brother"

    menu:
        "Most sisters don't [most_phrase]":
            if most_done == "vaginal":
                $ convinced = True
                mc.name "Most sisters don't fuck their brother."
                if the_person.effective_sluttiness() < 40:
                    the_person "Oh god, I knew that was a mistake!"
                    the_person "[the_person.mc_title], we need to forget about that!"
                    if the_person.sex_record["Vaginal Sex"] > 1:
                        mc.name "Once might have been a mistake, but we're so far past that now."
                    else:
                        mc.name "I can't forget it [the_person.title], you were incredible! Now you're all I want!"
                else:
                    the_person "That was... I know we shouldn't have..."
                mc.name "We're so far past being \"just family\", we need to throw all of that out and decide what makes us happy."

            elif most_done == "anal":
                $ convinced  = True
                mc.name "Most sisters don't take their brother's cock in their ass."
                mc.name "I think we're a little more than \"just family\" at this point."
                if the_person.effective_sluttiness() < 40:
                    the_person "Oh god, I knew that was a mistake!"
                    the_person "[the_person.mc_title], we need to forget about that!"
                    if the_person.sex_record["Anal Sex"] > 1:
                        mc.name "Once might have been a mistake, but we're so far past that now."
                    else:
                        mc.name "I can't forget it [the_person.title], you were incredible! Now you're all I want!"
                else:
                    the_person "That was... I know we shouldn't have..."
                mc.name "Don't be scared. Just think about what makes you happy."

            elif most_done == "suck":
                mc.name "Most sisters don't take their brother's cock down their throat."
                mc.name "Aren't we a little more than \"just family\" at this point?"
                if the_person.sex_record["Blowjobs"] > 1:
                    the_person "It's not like we actually had sex or anything like that."
                    the_person "I just... need to get practice doing that sort of thing, and I trust you!"
                else:
                    the_person "That was just a one-time thing, don't expect me to do that for you all the time!"

            elif most_done == "kiss":
                mc.name "Most sisters don't make out with their brother."
                mc.name "Doesn't that make us a little more than \"just family\"?"
                the_person "Oh, that? It was just a little kissing [the_person.mc_title]. It doesn't mean anything."
                the_person "I've heard so many stories at school of girls making out with their brothers."
                the_person "It happens all the time!"

            if convinced:
                the_person "You do make me happy..."
                "She stares deep into your eyes as you take her hands and hold them in yours."
                mc.name "Just be with me [the_person.title]. It's that simple."
                "[the_person.possessive_title!c] hesitates for a long moment. At long last she nods."
                the_person "Okay, you're right. We've gone this far already..."

            else:
                the_person "It's not like we've done anything serious like fuck each other."
                "[the_person.possessive_title!c] shakes her head."
                the_person "Let's not make this weird [the_person.mc_title], it's all just been casual fun."
                "You don't think you're going to change her mind without taking things further first."
                mc.name "You're right, I was reading too much into things."

        "Order her to agree" if the_person.obedience >= 200:
            $ convinced = True
            mc.name "Then I don't want you to think of me as family."
            "You put a hand on the back of her neck and make sure she's looking you directly in the eye."
            mc.name "Think of me as your master. I want you in my life, and I don't want to share."
            "[the_person.possessive_title!c]'s eyes are wide and fixed on yours. You can feel her trembling under your touch."
            mc.name "Do you understand?"
            the_person "Yes, I understand [the_person.mc_title]. Of course I'll do whatever you want me to do."

        "Order her to agree\n{menu_red}Requires: 200 Obedience{/menu_red} (disabled)" if the_person.obedience < 200:
            pass

        "Think of the baby!" if persistent.pregnancy_pref > 0 and (the_person.has_child_with_mc or (the_person.knows_pregnant and the_person.is_mc_father)):
            $ convinced = True
            mc.name "Most sisters don't end up knocked up with their brother's baby."
            if the_person.knows_pregnant:
                "You put a hand on her stomach and look deeply into her eyes."
                mc.name "Think about the baby [the_person.title]. Don't you want me by your side for this?"
                "She places her hands over yours and sighs happily."

            else:
                "You take her hand and look deeply into her eyes."
                mc.name "Think about the baby [the_person.title]. Shouldn't we be together for this?"
                "She sighs happily and hold your gaze."
            the_person "You're right. Of course you're right!"
            "[the_person.possessive_title!c] hugs you tight, pressing her head against your chest."
            "After a long moment she steps back, looking happy but concerned."

        "Think of the baby!\n{menu_red}Requires: Get her pregnant!{/menu_red} (disabled)" if persistent.pregnancy_pref > 0 and not (the_person.has_child_with_mc or (the_person.knows_pregnant and the_person.is_mc_father)):
            pass

        "Let it go":
            mc.name "You know what, you're right. I shouldn't ruin a good thing by trying to force it to be more than it is."
            "[the_person.possessive_title!c] sighs in relief."
            the_person "I'm glad you understand."

    if not convinced:
        return

    #Assuming she hasn't told you directly no yet:
    the_person "What do we tell other people? Someone's going to notice what's going on eventually."
    $ convinced = False
    menu:
        "Who cares what other people think?" if the_person.get_known_opinion_score("incest") > 0:
            $ convinced = True #Tell everyone that you're in a relationship, and you don't care what they think!
            mc.name "I think our love is more important than what other people think of us!"
            mc.name "We shouldn't have to hide how we really feel just to satisfy other people!"
            "[the_person.possessive_title!c] nods in agreement, gaining confidence with each moment."
            the_person "You're right! Love is the most important thing in the world, and I love you!"

        "Who cares what other people think?\n{menu_red}Requires: Positive incest opinion{/menu_red} (disabled)" if the_person.get_known_opinion_score("incest") <= 0:
            pass

        "We'll keep it a secret" if mc.focus >= 4 and the_person.focus >= 4:
            $ convinced = True #Don't tell anyone at all. Kind of like an affair but for fucking your sister. A perfect analogy.
            mc.name "We'll have to keep it a secret from everyone. It won't be easy, but if we're careful nobody needs to know but us."
            "[the_person.possessive_title!c] nods her understanding."
            the_person "I think I can do that. At least we can be together when we are here at home."

        "We'll keep it a secret\n{menu_red}Requires: Both 4+ Focus{/menu_red} (disabled)" if mc.focus < 4 or the_person.focus < 4:
            pass

        "We'll pretend we aren't related" if mc.charisma >= 4 and the_person.charisma >= 4:
            $ convinced = True
            mc.name "Nobody needs to know that we're siblings. If we're careful and convincing enough nobody will know we aren't just a normal couple."
            the_person "What about all of my friends? They're going to recognise you if they see us together."
            mc.name "We'll avoid them when we are together. If they ask do your best to convince them I'm just a normal big brother."
            "[the_person.possessive_title!c] nods her understanding."
            the_person "I think I can do that. I can be pretty convincing when I need to be."

        "We'll pretend we aren't related\n{menu_red}Requires: Both 4+ Charisma{/menu_red} (disabled)" if mc.charisma < 4 or the_person.charisma < 4:
            pass

        "Let it go":
            mc.name "You're right, there's no good way for us to do this even if we wanted to."
            "[the_person.possessive_title!c] sighs and shrugs."
            the_person "I'm sorry, but it's just not the right time. I don't know if it ever will be..."

    if not convinced:
        return


    the_person "Okay, but what about mom? I don't know how long we could hide this from her."
    the_person "I don't think she would be very happy with us being together..."

    $ convinced = False
    menu:
        "We already have threesome together" if had_family_threesome():
            $ convinced = True
            "You grinned."
            mc.name "Hello? Threesome~"
            "[the_person.possessive_title!c] punched your shoulder while trying to hide her blushing face."
            the_person "How did you managed to keep it a secret for so long? Going after both of us at the same time."
            $ random_comment = get_random_from_list(["I could learn a thing or two about being in a relationship from her though.", "I'm not worried though, I'm younger ... and {i}tighter{/i}.", "Pervert..."])
            the_person "[random_comment]"
            the_person "Oh... You will also take her as your girlfriend too, right? I imagined you are... cause you are, you know, {i}pervert{/i}!"
            if mom.is_girlfriend:
                $ already_knows = lily_knows_about_mom()
                mc.name "Way ahead of you. Already dating her~"
                if already_knows:
                    the_person "Oh yeah, huh..."
                else:
                    $ the_person.event_triggers_dict["mom_girlfriend_sister_knows"] = True # She knows now!
            else:
                mc.name "Of course, silly. My dick can support you both, no problem!"
            the_person "At least I don't have to be worried about getting a stepdad."

        "We already have threesome together\n{menu_red}Requires: Family Threesome{/menu_red} (disabled)" if not had_family_threesome():
            pass

        "I'll get [mom.title]'s blessing":
            $ convinced = False #Note that this _isn't_ a success, but opens up the path to a success later.
            mc.name "I'll talk to [mom.fname]. I'm sure I can convince her that love is more important than anything."
            the_person "I hope you're right [the_person.mc_title]. Just try not to get us in trouble, okay?"
            "She gives you a hopeful smile."
            $ mom.event_triggers_dict["sister_girlfriend_ask_blessing"] = True #This flags an action for Mom to be enabled.
            $ the_person.event_triggers_dict["sister_girlfriend_waiting_for_blessing"] = True #STops you from asking her to be your girlfriend until you come back with an answer.

        "Don't worry, I'm dating her too" if mom.is_girlfriend:
            $ convinced = True
            $ already_knows = lily_knows_about_mom()
            mc.name "If she had any problems she probably wouldn't be dating me too."
            if already_knows:
                the_person "I hadn't thought about that..."
                the_person "Oh yeah, huh..."
            else:
                $ the_person.event_triggers_dict["mom_girlfriend_sister_knows"] = True # She knows now!
                the_person "Oh my god, you are? I should have known!"
                "[the_person.possessive_title!c] slaps you playfully on the arm."
                the_person "That's my mother you're fucking... I mean, dating, you know!"

            the_person "She can't be angry about us dating if she's already dating you, so fine!"
            the_person "She's old anyway, I'll show you that you want someone younger to be with you."
            "She takes a deep breath and nods her final approval."
            the_person "Okay then, I'll be your girlfriend [the_person.mc_title]!"

        "Don't worry, I'm dating her too\n{menu_red}Requires: Dating [mom.title]{/menu_red} (disabled)" if not mom.is_girlfriend: 
            pass

        "She's too dumb to notice" if mom.int < 2:
            $ convinced = True
            mc.name "Have you noticed how distracted she's been lately? She's so focused on work that she'll never notice anything is different."
            the_person "She has seemed... different lately. Do you really think we can hide it from her?"
            mc.name "As long as we aren't fucking on the kitchen table in front of her I think we can get away with it."
            "[the_person.possessive_title!c] considers this, then nods in agreement."
            the_person "Alright then, you've convinced me! I can't believe this is really happening!"
            "She smiles happily and hugs you tight."
            the_person "[the_person.mc_title], my... boyfriend!"

        "She's too dumb to notice\n{menu_red}Requires: [mom.title] 1 Int{/menu_red} (disabled)" if mom.int >= 2:
            pass

        "Let it go":
            mc.name "I... didn't think about that."
            "[the_person.possessive_title!c] sighs and shrugs."
            the_person "I'm sorry, but it's just not the right time. I don't know if it ever will be..."

    if convinced:
        "She ponders for a while with her decision."
        the_person "We are in an unfamiliar territory here, [the_person.mc_title]..."
        the_person "But okay. I'll be your girlfriend. But we are still siblings in public, okay."
        call sister_girlfriend_setup(the_person, mom_knows = False) from _call_sister_girlfriend_setup_KSO01
    return

label mom_secretary_replacement_intro(the_person): #TODO: Set up as an on_talk added by her "promotion", triggers some time after she's received her promotion (if she has been, maybe a way to re-trigger the event?).
    #TODO: Event where Mom is worried that her boss is going to hire a new secretary and replace her.
    $ mom.progress.lust_step = 4
    the_person "Oh, hi [the_person.mc_title]. Say, can I have your opinion on something?"
    mc.name "Sure [the_person.title], what is it?"
    the_person "It's about my boss. I've been happy with my new role in the company, and I think he has been too, but..."
    the_person "Well, he's a man with a wandering eye, and I know part of the reason he hired me for the job was because of my \"womanly charm\"."
    the_person "Today I received a call from a woman asking for more information about an interview. I told her I didn't know anything, but something felt wrong." #NOTE: Make sure this event triggers at the end of a work day, not the start, and only on week days
    the_person "I did some snooping, and nobody knows what position that interview would have been for. I think he's trying to replace me!"
    the_person "You had such good instincts last time, I was hoping you would know what I should do now."
    the_person "I don't want to be replaced, but I don't know what I can do about it!"
    menu:
        "Seduce your boss":
            mc.name "I think the answer here is pretty clear."
            the_person "You do? It is?"
            mc.name "Well, yeah [the_person.title]. Your boss hired you with certain expectations, and you aren't living up to them."
            mc.name "If you want to keep your job, you're going to have to start putting out."
            the_person "Do you mean I should have sex with him? [the_person.mc_title], I couldn't do that! I'm not a prostitute!"
            mc.name "You don't necessarily need to start fucking him, but I'm sure there are other things you could do that would convince him to keep you around."
            mc.name "If you give him a blowjob every now and then I'm positive he'll stop trying to replace you."
            the_person "I... I shouldn't do that though..."
            mc.name "Then just show him your tits [the_person.title]. You're going to have to do something if you don't want to get replaced by someone younger and hotter!"
            $ mc.change_locked_clarity(20)
            "She frowns, but after a moment of thought nods in agreement."
            the_person "You're right, of course. I knew what he wanted the moment we went on that lunch date..."
            the_person "Fine, I'll do what I have to do... I just hope I'm able to convince him."
            menu:
                "You need to practice":
                    mc.name "You should practice first. You might only have one chance."
                    the_person "That's a good idea, would you... be able to help me?"
                    mc.name "Of course [the_person.title], I'm always here to help."
                    menu:
                        "Give me a blowjob":
                            $ the_person.event_triggers_dict["mom_replacement_seduce_practice"] = "blowjob"
                            $ mom.event_triggers_dict["oral_position_filter"] = None    #Temporarily suspend any position filters
                            "You unzip your pants and start to pull it down."
                            mc.name "Are you ready?"
                            $ taboo_path = False
                            if the_person.has_taboo("sucking_cock"): #Taboo break stuff
                                the_person "[the_person.mc_title], what are you doing? I thought I was just going to show him my breasts!"
                                mc.name "Maybe that would work, but are you willing to take the risk?"
                                mc.name "If you're going to do it, I think you need to commit."
                                the_person "But I can't practice... That... with you!"
                                mc.name "Who else would you go to? Is there anyone you trust more than me?"
                                "You pull your pants down low enough that your hard cock springs free. [the_person.possessive_title!c] looks at it, momentarily transfixed."
                                the_person "I... I shouldn't... We shouldn't be intimate like that..."
                                mc.name "This isn't about intimacy [the_person.title], it's about keeping your job."
                                mc.name "Just relax and pretend I'm not your son."
                                "You take her hand and bring it to your cock. She brushes her fingers over it as she considers."
                                "After a long moment she makes her decision and wraps her fingers around your shaft."
                                the_person "Alright, I trust you [the_person.mc_title]. This is just so I can practice though."
                                $ the_person.draw_person(position = "blowjob")
                                $ mc.change_locked_clarity(30)
                                "She sinks to her knees in front of you, glances around quickly to make sure you are still alone, and then leans in."
                                "[the_person.possessive_title!c] kisses the tip experimentally, then parts her lips and begins to suck it."
                                $ taboo_path = True
                            else: #
                                $ the_person.draw_person(position = "blowjob")
                                $ mc.change_locked_clarity(20)
                                "She nods and sinks to her knees."
                                the_person "Thank you for your help [the_person.mc_title]."
                                "You respond by letting your hard cock spring free and bouncing it onto her face."
                                "She kisses the tip experimentally, then parts her lips and slips it inside to suck on it."

                            call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _call_fuck_person_KSO01

                            if _return.get("guy orgasms", 0) > 0:
                                the_person "Well... I think that was a success."
                                mc.name "That was great [the_person.title]. Do that for your boss and I don't think you'll have any problems."

                            else:
                                the_person "I'm sorry, I just can't keep going [the_person.mc_title]."
                                mc.name "You'll get there [the_person.title], you just need some more practice."

                            $ mom.event_triggers_dict["oral_position_filter"] = jennifer_oral_position_filter    #Restore any position filters
                            if taboo_path:
                                the_person "I'm... glad I was able to try that with you first [the_person.mc_title]."
                                the_person "It might not be right, but I feel safe with you. It was even kind of fun."
                                the_person "Not that we should be doing that very often, of course!"

                            else:
                                pass

                            "[the_person.possessive_title!c] stands up and takes a moment to tidy herself up."
                            $ the_person.apply_planned_outfit(show_dress_sequence = True)


                        "Show me your tits":
                            mc.name "What are you waiting for? Get your tits out! That's what your boss is going to want to see!"
                            the_person "Right, okay then."
                            $ strip_list = the_person.outfit.get_tit_strip_list()
                            $ half_off_instead = False
                            if the_person.outfit.can_half_off_to_tits():
                                $ strip_list = the_person.outfit.get_half_off_to_tits_list()
                                $ half_off_instead = True

                            $ generalised_strip_description(the_person, strip_list, half_off_instead = half_off_instead)
                            $ mc.change_locked_clarity(30)
                            $ strip_list = None
                            the_person "Well, there you are..."
                            "[the_person.possessive_title!c] stands awkwardly in front of you, unsure of what else to do."
                            mc.name "You can't just stand there if you want to convince him, [the_person.title]."
                            menu:
                                "Shake them for me":
                                    mc.name "Shake them around for me. You want to show off how nice they are!"
                                    the_person "Right, right..."
                                    $ mc.change_locked_clarity(20)
                                    "[the_person.possessive_title!c] shakes her shoulders, bouncing her tits up and down for you."
                                    mc.name "That's better. Now pretend I'm your boss. What are you going to say to me?"
                                    the_person "Oh... [the_person.mc_title], do you like my breasts? Are they... big enough for you?"
                                    mc.name "More enthusiasm."
                                    the_person "Uh... Okay, I'm just so happy to be showing you my breasts [the_person.mc_title]. I hope you like them."
                                    mc.name "Jiggle them more, and don't call them \"breasts\". Call them something sexier, like tits."
                                    "[the_person.possessive_title!c] puts her back into it, jiggling her tits up and down, then side to side."
                                    $ mc.change_locked_clarity(20)
                                    the_person "Mmm, do I look sexy [the_person.mc_title]? I hope you like looking at my big MILF tits!"
                                    the_person "I bet they'd look even better with your... cock between them!"
                                    mc.name "That's it! Now you've got it!"
                                    $ mc.change_locked_clarity(10)
                                    "She slows down her tit bouncing, a little out of breath from the effort."
                                    the_person "Was that good? I didn't take it too far?"
                                    mc.name "No, that's perfect! I liked it, I'm sure he will too."
                                    the_person "I just hope I can keep my job. If I can do that I'll be happy. Do you think this will work?"

                                "Titfuck me" if the_person.has_large_tits:
                                    $ the_person.event_triggers_dict["mom_replacement_seduce_practice"] = "blowjob"
                                    "You pull down your pants, and your hard cock springs free of your underwear."
                                    mc.name "You need to practice putting those to use. Show him they're more than just eye candy."
                                    the_person "Do you think I'll need to?"
                                    "You shrug."
                                    mc.name "Better to be prepared, right?"
                                    $ mc.change_locked_clarity(20)
                                    "She nods and gets onto her knees in front of you. She collects her tits up in her hands and presses them on either side of your cock."
                                    the_person "How does that feel?"
                                    "[the_person.possessive_title!c] gives your shaft a few slow strokes with her tits. They feel warm and soft wrapped around you."
                                    mc.name "It feels great [the_person.title], keep doing that."
                                    call fuck_person(the_person, start_position = tit_fuck, private = True, skip_intro = True, position_locked = True) from _call_fuck_person_KSO02
                                    $ the_person.draw_person()
                                    if _return.get("guy orgasms", 0) > 0:
                                        the_person "Well... What do you think? Do you think this will work?"

                                    else:
                                        the_person "I'm sorry, I just can't keep going [the_person.mc_title]."
                                        mc.name "You'll get there [the_person.title], you just need some more practice."
                                        the_person "I hope so... Do you think this will work?"


                            menu:
                                "Get bigger tits" if Person.rank_tits(the_person.tits) < 8:
                                    mc.name "Well, there's one more thing you could do..."
                                    the_person "What is it? What do you think I should do?"
                                    call mom_work_secretary_replacement_intro_bigger_tits(the_person) from _call_mom_secretary_replacement_intro_bigger_tits

                                "You'll be fine":
                                    mc.name "Yeah, I think it'll work [the_person.title]. Just be confident and remember that you have what he wants."
                            "[the_person.title] takes a moment to tidy themselves up."
                            $ the_person.apply_planned_outfit(show_dress_sequence = True)
                            the_person "Thank you for the help [the_person.mc_title]."


                "You'll do fine":
                    mc.name "You'll be fine [the_person.title], I think you're going to find that you're a natural."

            $ add_mom_work_seduce_action(the_person, "seduce")


        "Get bigger tits" if the_person.tits != the_person.get_larger_tit(the_person.tits) and not the_person.event_triggers_dict.get("getting boobjob", False):
            mc.name "Well, I have an idea..."
            the_person "I knew you would! Tell me, what do you think I should do?"
            mc.name "Your boss hired you for this job because he likes how you look, so you should give him some more to look at."
            call mom_work_secretary_replacement_intro_bigger_tits(the_person) from _call_mom_secretary_replacement_intro_bigger_tits_1

            $ add_mom_work_seduce_action(the_person, "tits")

        "I'll take care of it": #Same as do nothing, but gives some dialogue to point you in the right direction.
            mc.name "[the_person.title], you don't need to worry. I'm going to take care of it."
            the_person "What are you going to do?"
            mc.name "I'll try and get in touch with your boss and have a conversation with him. I'll tell him how much this position means to you."
            mc.name "I'm sure I'll be able to work out some sort of deal with him."
            "[the_person.possessive_title!c] smiles and pulls you into a hug."
            the_person "Oh, thank you [the_person.mc_title]. I knew you would be able to help somehow."
            mc.name "No problem [the_person.title]. You just relax and leave it to me."
            "She gives you one last squeeze, then lets you go."
            $ the_person.event_triggers_dict["mom_promotion_boss_phase_one"] = True
            $ add_mom_lust_story_bridge_action()    # jump right to the lust story bridge and skip the bigger tits / seduction part

        "Work for me then" if not mc.business.at_employee_limit:
            mc.name "Let me be honest with you. I don't feel like sharing you with your boss."
            "She grab hold of your arms."
            the_person "Sharing me? What do you mean?"
            "You look straight to her eyes."
            if the_person.is_girlfriend or mom.event_triggers_dict.get("vaginal_revisit_complete", False): #mom_taboo_completed():
                mc.name "I don't like other peoples having dirty thoughts on you."
                mc.name "You are mine and mine alone."
            mc.name "Why don't you come work for me instead. How about that?"
            mc.name "You don't have to worry about getting replaced by anyone."
            if the_person.is_girlfriend or mom.event_triggers_dict.get("vaginal_revisit_complete", False): #mom_taboo_completed():
                "She smiles."
                the_person "Oh... You are jealous aren't you?"
                the_person "I'm yours already, [the_person.mc_title]."
            "She thinks long and hard about this."
            the_person "I don't know... What if your business doesn't work out?"
            menu:
                "I want you by my side" if the_person.is_girlfriend:
                    mc.name "We're not just a couple, we're a team [the_person.title]. We should work together like one."
                    mc.name "I want you to trust me, and I want you by my side."
                    "Another long pause as she thinks."
                    the_person "Okay, I'll do it."
                    call stranger_hire_result(the_person) from _call_stranger_hire_result_mom_KSO01
                    if _return:
                        mc.name "Welcome to the team [the_person.title]."
                        menu:
                            "Pay her nothing" if the_person.obedience >= 130:
                                mc.name "If we're a couple, and I'm the owner of the business, it doesn't really make much sense for me to put you on the official payroll."
                                mc.name "I think the accounting will be easier if you just come to me for anything you need, okay?"
                                the_person "Of course, that sounds reasonable."
                                $ the_person.event_triggers_dict["mandate_bc"] = False

                                $ the_person.primary_job.wage_adjustment = 0
                                $ the_person.primary_job.recalculate_salary()

                            "Pay her nothing\n{menu_red}Requires: 130 Obedience{/menu_red} (disabled)" if the_person.obedience < 130:
                                pass

                            "Pay her a normal salary":
                                pass #

                        the_person "Now I just need to tell my boss I won't be coming into work. I'm sure he won't be happy to hear that!"
                        $ add_mom_new_employee_first_day_action()
                    else:
                        mc.name "I'm going to need some time to get everything ready, actually."
                        mc.name "We can revisit this later, alright?"
                        the_person "I understand. Whenever you're ready."


                "I want you by my side\n{menu_red}Requires: Make her your girlfriend{/menu_red} (disabled)" if not the_person.is_girlfriend:
                    pass

                "We'll see each other so much more often" if the_person.love >= 50:
                    mc.name "Think about how much more time we'll be able to spend together."
                    the_person "You do spend a lot of time at work..."
                    mc.name "And so do you! If you worked for me we would see each other every day."
                    "She smiles and sighs."
                    the_person "That would be nice... Okay, I'll do it!"
                    call stranger_hire_result(the_person) from _call_stranger_hire_result_mom_KSO02
                    if _return:
                        mc.name "Welcome to the team [the_person.title]."
                        the_person "Thank you [the_person.mc_title], I'm sure this is going to be great!"
                        the_person "Now I just need to call my boss and tell him I won't be coming into work. I'm sure he won't be happy to hear that!"
                        $ add_mom_new_employee_first_day_action()
                        $ the_person.event_triggers_dict["mandate_bc"] = False
                    else:
                        mc.name "I'm going to need some time to get everything ready, actually."
                        mc.name "We can revisit this later, alright?"
                        the_person "I understand. Whenever you're ready."


                "We'll see each other so much more often\n{menu_red}Requires: 50 Love{/menu_red} (disabled)" if the_person.love < 50:
                    pass


                "You can be MY personal secretary\n{menu_red}Hires to HR{/menu_red}" if the_person.has_job(mom_secretary_job):
                    mc.name "Seeing you advance in your career has made it clear to me, I need a personal secretary of my own."
                    mc.name "You can keep doing basically what you are doing now, but for me."
                    the_person "Oh? You mean I could keep doing HR work?"
                    mc.name "I mean, yeah... ALL the things you are doing now."
                    "[the_person.title] hesitates for a moment. While you don't say it explicitly, she seems to understand that it might include her sexual duties to her boss."
                    the_person "I mean... if I'm doing HR work..."
                    the_person "Ah what the hell. I'll do it!"
                    $ mc.business.add_employee_hr(the_person)
                    mc.name "Welcome to the HR team [the_person.title]."
                    the_person "Thank you [the_person.mc_title], I'm sure this is going to be great!"
                    the_person "Now I just need to call my boss and tell him I won't be coming into work. I'm sure he won't be happy to hear that!"
                    $ the_person.event_triggers_dict["personal_sec"] = True
                    $ the_person.event_triggers_dict["mandate_bc"] = False
                    $ add_mom_new_employee_first_day_action()

                "You can be MY personal secretary\n{menu_red}Requires: Jennifer is Secretary{/menu_red} (disabled)" if not the_person.has_job(mom_secretary_job):
                    pass

                "I'll pay you more than they do":
                    mc.name "I can pay you double what you're earning right now [the_person.title]."
                    mc.name "I need people I can trust working for me, and I know I can trust you more than anyone."
                    the_person "Really? Can you actually afford to do that?"
                    "You nod, and she thinks for a moment longer."
                    the_person "That would really help with all the bills... Okay, you've convinced me!"
                    $ the_person.salary_modifier = 2.0
                    call stranger_hire_result(the_person) from _call_stranger_hire_result_mom_KSO03
                    if _return:
                        mc.name "Welcome to the team [the_person.title]."
                        the_person "Thank you [the_person.mc_title], I'm sure this is going to be great!"
                        the_person "Now I just need to call my boss and tell him I won't be coming into work. I'm sure he won't be happy to hear that!"
                        $ the_person.event_triggers_dict["mandate_bc"] = False
                        $ add_mom_new_employee_first_day_action()
                    else:
                        mc.name "I'm going to need some time to get everything ready, actually."
                        mc.name "We can revisit this later, alright?"
                        the_person "I understand. Whenever you're ready."

                "Never mind":
                    mc.name "I suppose you're right."

        "You can work for me\n{menu_red}Requires: Free employee slot{/menu_red} (disabled)" if mc.business.at_employee_limit:
            pass

        "Do nothing":  #Do nothing, and imply she's on her own to figure this out.
            mc.name "That's a tough situation [the_person.title], but I don't think there's much you can do."
            mc.name "Just keep doing your best, I'm sure your dedication and enthusiasm will convince him."
            the_person "I hope you're right..." #If she doesn't do anything the quest fizzles out (For now, at least)
            $ the_person.event_triggers_dict["mom_promotion_boss_phase_one"] = True
            $ add_mom_lust_story_bridge_action()    # jump right to the lust story bridge and skip the bigger tits / seduction part

    call talk_person(the_person) from _call_talk_person_KSO01
    return

label kaya_1st_date_label(the_person):
    #Her actual first love label. One week after the initial rejection.
    $ the_person.draw_person()
    "You step into the coffee shop. Kaya is working the counter and sees you when you walk in."
    the_person "Ah! It's you!"
    "She seems very excited to see you. You step over to the counter."
    the_person "This is perfect, I was hoping you would swing by! I'm off work at 8!"
    "Wow, it seems she really was too preoccupied to go out last week."
    mc.name "Nice, mind if I get a coffee and just hang out until then?"
    the_person "Sure! It's on the house. I'll have it right out!"
    $ the_person.draw_person(position = "walking_away")
    "She turns and start to make it with her back to you."
    $ the_person.draw_person(position = "standing_doggy")
    "She reaches down and grabs an ingredient from below the counter, giving you the chance to sneak a peek at her backside."
    $ the_person.draw_person(position = the_person.idle_pose)
    "She stands up and hands you a coffee."
    the_person "Here you go."
    mc.name "Thank you. I think I'll step outside and sit on the patio."
    $ clear_scene()

    $ mc.change_location(downtown)
    "You step out the door and sit down at a nearby table. You take the chance to pull out your phone and catch up on some company emails."
    "There's a lot of the usual drama between girls. Your head researcher needs clarification on a recent serum trait you were experimenting with…"
    "You answer her, but she emails you right back with a bunch more questions."
    "You spend a while catching up. It is nice to get some work done in a quiet environment like this…"
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ the_person.draw_person(position = "sitting")
    the_person "Wow, you are really focused on those emails."
    "You suddenly look up. Kaya is sitting across from you at the table."
    mc.name "What?… how long have you been sitting there?"
    the_person "Just a couple of minutes. I saw when I was walking over that you had an email app up and you were typing really fast."
    the_person "Don't worry! I didn't read any of it. I wanted to let you finish, but you were so focused on that thing!"
    mc.name "Ah, I didn't even realize. Don't worry, for the rest of the night this thing can go in my pocket."
    the_person "Aww, if something comes up, I understand. But I appreciate the thought!"
    the_person "So umm… I know you said something about getting drinks tonight but… I actually don't drink."
    mc.name "Oh… I'm sorry…"
    the_person "It's fine. It's not that I have a problem with it, but I'm just 20, and I don't feel comfortable having people do the fake ID or smuggle me drinks or whatever."
    "Wow… she is YOUNG. She seems mature for her age though…"
    mc.name "Well… let me see… we… could… ummm…"
    "You struggle a moment to come up with an alternative..."

    the_person "If you're okay with it, we could still go to a bar. There is a place near the university actually."
    mc.name "Yeah?"
    the_person "Yeah. They have some pool tables there for college students to blow off steam, so they let underage students in."
    mc.name "Pool? As in like, billiards?"
    the_person "Yeah! It is one of my favourite ways to just relax and unwind."
    $ the_person.discover_opinion("billiards")
    the_person "I've always been a bit of a nerd… and learning to play around the board and angle shots is really fun."
    "Wow, this girl keeps getting more and more interesting."

    mc.name "That does sound fun, when you put it like that. But I have to be honest…. I've never played!"
    the_person "What!?! You've never played pool???"
    mc.name "I haven't. Never had reason to I guess."
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly jumps up."

    the_person "Lets go! I got some ones from tips tonight, I'll pay for the table if you buy the sodas!"
    mc.name "Sodas…. Right…"
    $ mc.change_location(downtown_bar)
    "It is a short walk to the place she has in mind, and soon you are stepping inside."
    "She waves to the bartender and he nods as you step up to the counter."
    "???" "Evening. IDs?"
    the_person "Ah, just here to play some pool. Can I have a coke?"
    "The bartender turns to grab a glass and starts to get her order."
    the_person "I see an open table, I'll go reserve it!"
    "[the_person.title] leaves you at the bar."
    $ clear_scene()

    "A minute later, the bartender turns to you."
    "???" "And for you?"
    mc.name "Ah, just a Sprite."
    "Soon, you step away from the bar with the two drinks. "
    $ mc.business.change_funds(-5, stat = "Food and Drinks")
    $ the_person.draw_person(position = "standing_doggy")
    "You bring the drinks over to the pool table where [kaya.possessive_title] appears to be just getting done setting up."
    "A number of pool balls are in a neat triangle and a white ball is sitting opposite of it."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "Alright, I just got done setting up! I know it is your first time, so I figure we could play a couple games just to teach you the rules."
    mc.name "Do you normally play for stakes?"
    the_person "Once in a while a pool shark will be around and I'll play for something, but for tonight a couple laid back games sounds great."
    the_person "I'll just teach you the rules as we go. Ready to get started?"
    "KiNA EDIT : You still get the stat change if you skipped. It just a hassle to read everything. Sorry Starbuck <3"
    menu:
        "Skip":    
            if mc.int > 3:
                $ the_person.change_love(1, 40)        
            if mc.sex_skills.get("Foreplay", 0) > 3:
                $ the_person.change_slut(1, 40)
            if mc.sex_skills.get("Foreplay", 0) > 3 and mc.int > 3:
                $ the_person.change_love(4, 60)
        "I wanna learn":
            mc.name "Sure."
            the_person "Alright, the most common variant is called 8 Ball…"
            "She begins walking you through the rules as she walks over to the end of the table."
            $ the_person.draw_person(position = "standing_doggy")
            "She strikes the white ball and sends it crashing through the others. They split wide open and you notice a striped ball goes into a pocket."
            the_person "Alright! So since I sunk a ball first, I will be stripes this game, and you are solids…"
            $ the_person.draw_person(position = the_person.idle_pose)
            "She quickly surveys the table and then lines herself up for another shot."
            $ the_person.draw_person(position = "standing_doggy")
            the_person "So, my goal is to hit in all the striped balls, and you want to hit in all the solid coloured ones, EXCEPT the black 8 ball."
            "She strikes the white ball, that she called the cue ball, again. She easily knocks in another striped ball."
            the_person "Alright… let's see…"
            $ the_person.draw_person(position = the_person.idle_pose)
            "You look at the table, but don't see any obvious plays."
            the_person "Alright, normally I wouldn't try this, but since we are just playing for fun…"
            $ the_person.draw_person(position = "standing_doggy")
            "She points at her stick at the cue ball, but this time it appears that she is hitting it away from all the balls with stripes on them."
            "She strikes the ball and it goes between two of your balls, hits the side wall… then it curves back?"
            "It strikes a striped ball and pushes it close to a corner pocket, but it doesn't quite go in."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Damn, so close. Alright, your turn!"
            "You look at the table. The placing of the cue ball makes it look fairly easy to get a solid in near a corner."
            the_person "Alright, line it up, and make sure you hit the cue ball dead center…"
            "She shows you the basics of how to handle the pool stick and to line up a shot."
            "You lean over the table and carefully line it up. Here goes nothing."
            "You strike the ball, and somehow, it goes across the table and knocks it in."
            the_person "Oh ho! And on your first try? You might be a natural at this!"
            the_person "Or are you actually a pool shark? Looking to try his luck with me?"
            mc.name "No, I promise I've never played before, but I suspect I have a very capable teacher."
            "You look at the table. No matter how you look at it though, there aren't any clear shots."
            the_person "Alright, time for a real test. See how this ball here is in near this pocket, but one of my balls is in the way?"
            the_person "You can't hit my ball first, but you can bank it off the wall."
            the_person "To make it easier, they put diamonds on the wall at equal distances, so you can determine the proper place on the wall to aim for… see?"
            "You see the idea she is suggesting, and you try to figure out the proper place on the wall to hit…"

            if mc.int > 3:
                "*Intelligence Check Passed*"
                "A quick calculation of the angle in your head, and you line up a shot."
                "You stroke the cueball, and it bounces of the wall and strikes your intended target."
                "It gets close to a pocket, but doesn't quite go in. Still, pretty good for your first attempt, you tell yourself."
                the_person "Hey, that was close! I'm impressed, it usually takes a few tries to get used to the angles of the game!"
                $ the_person.change_love(1, 40)
            else:
                "*Intelligence Check Failed*"
                "You look and get the idea for how to bank the shot, so you give it a try."
                "However, something about the way the balls are positioned aren't quite right. You strike the cueball and it bounces off the side, but doesn't hit your target."
                the_person "Close! Don't worry, it takes some practice to learn how to use the diamonds and to play them correctly."

            the_person "Alright, my turn!"
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.title] turns and lines up a straight shot. She sinks it easily."
            $ the_person.draw_person(position = the_person.idle_pose)
            "When you look at the table, you see a similar shot as what you attempted earlier. She sees it too."
            the_person "Alright, see here? Now we need to make sure to think about where we want the cue ball to hit in order to angle it into the pocket…"
            $ the_person.draw_person(position = "standing_doggy")
            "She takes several seconds to line up her angled shot, then strikes. The cue ball bounces against the far wall then comes back, driving the ball into a side pocket."
            "Wow… she makes it look easy!"
            "The cue ball is left in a place where she easily lines up another shot. She sinks it easily."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Alright, I don't want to run the table on you. Why don't you go ahead and take another turn?"
            mc.name "Okay… let's see…"
            "You spot what looks to be an easy shot. You slowly line it up. Somehow, you manage to knock it in."
            "You survey the table again. This time, there are no obvious shots, and you don't see any easy way to bank it off of the wall, either."
            the_person "Ah, here we go, this would be a good chance to try what is called a jump shot. See the ball there, straight in line with the corner pocket?"
            mc.name "Yeah, but the 8 ball is in the way."
            the_person "Right. What you can do is, if you strike the cue in just the right way, you can cause it to jump up off the table and clear the 8 ball, jumping it."
            "She spends some time explaining to you how to hit the cue."
            the_person "Alright. You seem like you are good with your hands, give it a try!"
            "Alright… I'll give it a shot…"

            if mc.sex_skills.get("Foreplay", 0) > 3:
                "*Foreplay check passed*"
                "After several seconds of lining up, you attempt a strike similar to the one [the_person.title] described."
                "The cue ball bounces up off the table, and over the 8 ball!"
                "It strikes your target, pushing it close to a pocket but not quite in."
                the_person "Wow! Nice one! That was so close!"
                the_person "It took me a long time to get those down. You must have excellent dexterity..."
                $ the_person.change_slut(1, 40)
            else:
                "*Foreplay check Failed*"
                "After several seconds of lining up, you attempt a strike similar to the one [the_person.title] described."
                "The cue ball bounces, but it doesn't go as far as you were hoping."
                "It strikes the 8 ball and sends it perilously close to a pocket, but thankfully it doesn't go in."
                the_person "Whew! That was a nice try!"

            the_person "Alright, I'll go again. Let's see here…"
            "She doesn't have any obvious shots either, but she starts to line something up."
            the_person "Alright, this type of shot is much harder, but if you hit the cue ball slightly to the side instead of dead on, you can get it to curve as it spins…"
            "She briefly explains the math behind curving a shot around an obstacle. You understand the idea, but the math of the curve and the precision hit required seems daunting."
            $ the_person.draw_person(position = "standing_doggy")
            the_person "Alright… let's see if I can demonstrate…"
            "[the_person.possessive_title!c] strikes the cue ball. It curves between the 8 ball and one of yours and strikes one of her 2 remaining balls, driving it into a corner pocket."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Woo! Alright!"
            mc.name "Wow, you make it looks so easy. I can tell you are very well practised."
            the_person "Thanks!"
            "She looks at the table."
            the_person "Here, why don't you try it? You could hit it here and swing it around my last ball."
            the_person "I know you probably won't sink it, but just to try it."
            mc.name "Hmmm… okay…"
            "She explains to you how to line up the curve and how to strike the cue ball to get it to curve the way you want it to."
            mc.name "Ahh what the hell, here we go."

            if mc.sex_skills.get("Foreplay", 0) > 3 and mc.int > 3:
                "*Foreplay and Intelligence check passed!"
                "You are starting to understand the allure of the game, as you try to line up a difficult curve shot."
                "Your only goal this early is to make contact with the target, but you think with just a bit of spin..."
                "You strike the cue ball. It curves around [kaya.possessive_title]'s striped ball and hits the target."
                "It doesn't go in, but it does stop just in front of a corner pocket, effectively blocking it from being available for [kaya.title] to use."
                the_person "Holy... you almost got that one?"
                the_person "Like, I can tell you haven't played before, but you are picking this up crazy fast."
                the_person "I can't wait to keep playing you as you get better and better!"
                $ the_person.change_love(4, 60)
            else:
                "*Foreplay and Intelligence check failed*"
                "You do your best to line up a curved shot, but at this point you can tell you are in way over your head."
                "You hit the ball as described, and watch it curve around [kaya.possessive_title]'s ball, but it doesn't go anywhere near your target."
                the_person "Hey, that's the idea! Nice try!"

    the_person "Alright, I think I've shown you the basics… time to finish you off."
    "She gives you a smirk when she finishes the sentence. She knows exactly what she just said…"
    $ the_person.draw_person(position = "standing_doggy")
    "Next thing you know, [the_person.title] sinks her last two striped balls, then lines up the 8 ball."
    "She strikes the cue and sinks it easily, winning the game."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "Woo! Good game! How about one more?"
    mc.name "Yeah, let's play one more."
    the_person "Alright! Let me show you how to rack it up."
    "She inserts some quarters into the table and the pool balls get released."
    "You grab the triangular rack and help gather the balls together."
    the_person "Alright, that looks good, the 8 goes in the middle, one corner gets a stripe and the other a solid…"
    mc.name "Like this?"
    the_person "Yeah… you got it!"
    the_person "Alright, this game I'll take it easy on you, okay?"
    mc.name "Sounds good. Should we play for stakes?"
    the_person "Wow, I just said I was taking it easy on you… but what do you have in mind?"
    mc.name "Well, if I win, you have to go out with me again sometime."
    the_person "Ahhhh, I see. A night of free drinks and billiards? That sounds terrible!"
    "Her tone makes it clear she is just teasing."
    the_person "Alright, I'll take that. And if I win, you have to walk me home tonight."
    mc.name "Alright, deal."
    the_person "Nice. Alrighty your break!"

    call bar_date_billiards_label(the_person) from _kaya_first_date_billiard_scene_KSO01
    if _return: #You won
        the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
        mc.name "The horror!"
        the_person "Guess I'll just have to walk myself home now, dreading the day the mysterious stranger shows up at the coffee-shop and demands my presence again!"

    else:
        the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
        mc.name "Too bad you didn't make that your wager then."
        "At first she looks at you, a bit startled, thinking you mean you don't want to, but then realises you are teasing her."
        the_person "Guess you'll just have to walk me home and we'll go our separate ways then."

    "The teasing between you two has definitely become playful. You are really enjoying her company."
    the_person "But uh... we're doing both... right?"
    mc.name "Of course."
    "You both finish off what is left of your drinks, then leave the bar together."
    $ mc.change_location(downtown)

    mc.name "Hey, I forgot to ask you, how did your finals go?"
    the_person "Oh, they went great! I'm finally done!"
    mc.name "With finals?"
    the_person "With my undergrad. I did it online so I could help take care of my mom. They don't do a big ceremony or anything but I finished up the final classes for my degree."
    mc.name "What… at 20?"
    the_person "Yeah, I umm, I took some classes while I was still in high school. I was always good at academics."
    the_person "I've been trying to get into a master's program at the local university, but I just can't get in."
    mc.name "What? Why not?"
    the_person "Apparently if you didn't graduate from there, they require a sponsorship from one of the staff, but I just don't know anyone there!"
    the_person "I've cold called a couple of them but they just blow me off."
    mc.name "What are you looking to study?"
    the_person "Well my degree is in biology, and I'm trying to get into a pre-med program."
    mc.name "Wow… so you want to go into the medical field? Be a doctor?"
    the_person "Well, something like that… I'd like to get more into the research side of things… for personal reasons…"
    "She seems hesitant to explain more, so you decide not to push for more information."

    mc.name "Have I ever told you what I do for a living?"
    the_person "Umm, no. I've been curious, but my mom always told me it is rude to ask a man what he does on a first date…"
    mc.name "I actually run a pharmaceutical research and development company. I have an excellent working relationship with a professor at the university."
    "She stops walking and looks at you in surprise."
    $ the_person.draw_person(position = "stand2")

    the_person "You… you what?"
    mc.name "She has actually been on my case lately about recruiting one of her lab assistants… I could probably convince her to sponsor you."
    the_person "I… that would be amazing… but… I mean we don't really even know each other?"
    mc.name "No, not really, but I'm a good judge of character, and I can tell just from what I do know that you would be a great candidate."
    mc.name "I'll try to talk to her soon and get back to you."
    the_person "I… I don't even know what to say. I would owe you a huge favour."
    mc.name "Well, speaking from experience, that is how a lot of things in the world work. Some people will help you, and ask for your help in exchange later."
    mc.name "So many things are just all about who you know."
    $ the_person.draw_person(position = the_person.idle_pose)
    "You walk the rest of way to her place in silence. She is clearly lost in her thoughts."
    $ the_person.learn_home()
    $ mc.change_location(kaya.home)
    $ the_person.change_location(the_person.home)
    $ renpy.show("Apartment Entrance", what = bg_manager.background("Apartment_Lobby"), layer = "master")
    "Soon you walk up to the steps of a run-down apartment building. This must be where she is living."
    the_person "Ahh, we're here already..."
    the_person "Do you... should I like, give you my number?"
    mc.name "Oh yeah, I'll probably need that. I'll let you know as soon as I can talk to her though."
    $ mc.phone.register_number(the_person)

    the_person "Hey, I just want to say, it's been a long time since I had a night like this to just relax and have fun. I had a great time... please come back and see me at the coffee shop, okay?"
    the_person "Even if it doesn't work out with your friend and a sponsorship... you owe me another night out, remember?"
    mc.name "Your charm is difficult to resist. And the coffee is good too."
    $ clear_scene()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, the_person.outfit, position = "kissing") # keep outfit the same
    "[the_person.title] holds her arms out for a hug, and you draw her close. She is looking up at you, and feeling right, you kiss her."
    "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
    "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when your hand wanders down to her ass, but reaches back and moves your hand back up."
    $ the_person.change_arousal(15)
    $ the_person.break_taboo("kissing")
    "You make out for several seconds."
    $ scene_manager.add_actor(sakari)
    "Suddenly, the front door opens up. There is an older woman standing there. [the_person.title] backs away quickly."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "Whaea!(????)! I... Ahhh! What are you doing?"
    sakari "Tamahine...(????)... ahh, am I interrupting?"
    the_person "Mom! Yes I... ahhh..."
    "She let's out a long sigh."
    the_person "Well, I guess we're doing this now... Mom, this is my friend, [mc.name]. He and I were playing some pool, and he was just walking me home..."
    the_person "[mc.name] this is my mom..."
    $ sakari.set_title(sakari.name)
    $ sakari.set_possessive_title("your friend's mother")
    $ sakari.set_mc_title(mc.name)
    $ sakari.set_event_day("day_met")

    sakari "Ahh hello sir. You can call me [sakari.title]."
    mc.name "Good evening [sakari.title]. I'm [mc.name]."
    sakari "Nice to meet you. Sorry I heard a noise and was just looking to see what was going on out here."
    the_person "Right... well... I guess this is goodnight."
    the_person "[mc.name]... see you soon?"
    mc.name "Yes, I'll get back to you as soon as I can."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ scene_manager.update_actor(sakari, position = "walking_away")
    "[the_person.possessive_title!c] and her mother step into their apartment and then the door closes behind them."
    $ scene_manager.clear_scene()
    "You hear [the_person.title] chiding her mother after the door closes."
    $ mc.change_location(downtown)
    "You step out of the apartment building, thinking about the date you just had."
    "[the_person.possessive_title!c] seems impressively smart, and graduating from college at 20 while working at a coffeeshop on weekends points to a strong work ethic."
    "You're certain she would make a great candidate for an advanced program at the local university. Now you just need to convince [nora.title]."
    "It's interesting that she lives with her mother, also. She mentioned once that she helps take care of her.  It makes you wonder about her health - her lack of hair might be an indication she's undergoing cancer treatment?"
    "There's no use dwelling on it now. Hopefully you'll be able to learn more soon."
    "For now, you should focus on getting her that sponsorship!"
    $ add_kaya_ask_nora_for_sponsorship_action()
    $ kaya.progress.love_step = 2
    call advance_time(no_events = True) from _call_advance_time_kaya_first_date_label_KSO01
    return    

label mom_date_blocker(the_mom, the_date): #TODO: Add some relationship awareness to Mom so she can comment on you dating multiple girls, ect.
    #Triggers when you've got a date planned with a girl, but Mom has high Love.
    #TODO: Write a Mom specific movie date. Maybe mirror the LR1 event and have Lily join in sometimes.
    if not mom.is_available:
        return
    
    $ mc.change_location(bedroom)

    "You're getting ready for your date with [the_date.title] when you hear a knock at your door."
    the_mom "Knock knock. Are you in there [the_mom.mc_title]?"
    mc.name "Yeah, come on in [the_mom.title]."
    $ the_mom.draw_person()
    "[the_mom.possessive_title!c] steps into your room and closes the door behind her."
    the_mom "Oh, you're looking very handsome tonight. Is there some special occasion?"
    if the_date == lily and home_harem():
        mc.name "I'm taking [the_date.title] on a date tonight."
        mc.name "I believed this is her night?"
        the_mom "Oh... You are right. My bad."
        "[the_mom.possessive_title!c] pulls you into her arms. She rests her head on your shoulder while you hold her."
        "You're silent for a few moments, then she steps back and holds you at arms length."
        $ the_mom.change_love(1)
        the_mom "You take care of your sister well, you hear me."
        mc.name "I'll see you tomorrow."
        $ clear_scene()
        return False #Returns False if the date was not intercepted.
    else:
        mc.name "I'm going out on a date tonight."

    if the_mom.love > 70 and the_mom.effective_sluttiness() > 60: #High slut, she offers to fuck you (with slut bonus) if you stay at home
        if the_mom.opinion.not_wearing_anything > 0 or the_mom.opinion.lingerie < 0:
            the_mom "You are? Oh [the_mom.mc_title]..."
            $ strip_list = the_mom.outfit.get_full_strip_list()
            if strip_list:
                $ first_item = strip_list[0]
                $ the_mom.draw_animated_removal(first_item)
                "[the_mom.possessive_title!c] grabs her [first_item.display_name] and pulls it off."
                $ strip_list.remove(first_item)
                $ del first_item
            else:
                "[the_mom.possessive_title!c] spreads her legs, displaying her naked body for you."

            mc.name "[the_mom.title], what are you doing?"
            $ mc.change_locked_clarity(10)
            the_mom "Convincing you to stay home tonight."
            $ generalised_strip_description(the_mom, strip_list)
            $ mc.change_locked_clarity(20)
            $ strip_list = None

        else:
            the_mom "You are? I... Don't go anywhere, okay? I'll be right back."
            $ clear_scene()
            "Before you can ask her any questions she's hurried out of your room."
            "You shrug and go back to preparing for your date. A few short minutes later [the_mom.possessive_title] steps back into your room."
            $ the_mom.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_mom.sluttiness + 20, the_mom.sluttiness // 3, guarantee_output = True, preferences = WardrobePreference(the_mom)), update_taboo = True)
            $ the_mom.draw_person()
            $ mc.change_locked_clarity(30)
            the_mom "[the_mom.mc_title], are you still sure you want to go out and see some other girl?"
            mc.name "[the_mom.title], what are you doing?"
            the_mom "Convincing you to stay home tonight."

        the_mom "What are you expecting this girl to do for you that I can't? You know nobody will ever love you like your mother."
        the_mom "You're a man now, which means you have different needs, but I still want to be the one to take care of you."
        $ mc.change_locked_clarity(20)
        "She steps close to you and cups your crotch, rubbing your already-hard cock through your pants."
        the_mom "Let me take care of you. Stay home tonight."
        menu:
            "Cancel your date with [the_date.title]":
                mc.name "[the_mom.title]... You know you're the most important woman in my life. I'll call [the_date.title] and cancel."
                $ the_mom.change_stats(happiness = 10, love = 2, slut = 1, max_slut = 70)
                "[the_mom.possessive_title!c]'s face lights up."
                the_mom "Thank you [the_mom.mc_title], you're making the right decision. We're going to have such a wonderful time together."
                mc.name "Just give me a moment, okay? She's probably not going to be happy about this."
                $ skip_intro = False
                $ start_position = None
                $ skip_condom = False
                if the_mom.opinion.giving_blowjobs > the_mom.opinion.vaginal_sex or the_mom.effective_sluttiness("vaginal_sex") < 70:
                    $ the_mom.draw_person(position = "kneeling1")
                    "[the_mom.possessive_title!c] drops to her knees in front of you."
                    the_mom "I'll be quiet. Go ahead, I'm going to get you warmed up and show you just how thankful I am!"
                    "You get your phone out while [the_mom.title] pulls down your pants. Your hard cock bounces against her face when it springs free of your underwear."
                    the_mom "Oh! Sorry, sorry..."
                    $ mc.change_locked_clarity(20)
                    "You call [the_date.title] as [the_mom.possessive_title] starts to lick at your shaft."
                    $ the_mom.draw_person(position = "blowjob", special_modifier = "blowjob")
                    the_date "Hello?"
                    if the_date.is_family:
                        mc.name "Hey Sweety, it's me."
                    else:
                        mc.name "Hey [the_date.title], it's [the_date.mc_title]."
                    the_date "Hey [the_date.mc_title], I was just about to head out the door. Is everything okay?"
                    mc.name "Well, I hate to tell you this so late, but..."
                    $ mc.change_locked_clarity(30)
                    "[the_mom.possessive_title!c] looks up at you from her knees, your cock bulging out one cheek."
                    mc.name "Something important has come up, and it needs to be taken care of. I won't be able to go out tonight."
                    $ the_mom.change_stats(love = 3, max_love = 80, slut = 1, max_slut = 70)
                    $ mc.change_locked_clarity(30)
                    "[the_mom.title]'s eyes light up, and she bobs her head up and down on your shaft happily. You have to stifle a moan."
                    the_date "Oh no, is everyone okay?"
                    $ the_date.change_stats(happiness = -20, love = -3)
                    "[the_date.possessive_title!c]'s disappointment is clear, even over the phone."
                    if the_date.is_family:
                        mc.name "Something urgent came up at work, that has to be taken care of."
                    else:
                        mc.name "It's a family situation, I'm sorry that I can't say any more."
                    $ mc.change_locked_clarity(20)
                    "[the_mom.possessive_title!c] sucks gently on the tip of your cock."
                    the_date "Okay, well... I hope you get that resolved. Let's try and reschedule, okay?"
                    mc.name "Yeah, I'll be in touch. Thanks for understanding [the_date.title]. Bye."
                    the_date "Bye..."
                    "[the_mom.possessive_title!c] pulls off your cock, smiling happily."
                    the_mom "Thank you [the_mom.mc_title]. I'm the only woman you'll ever need in your life."
                    "With that she slides you back into her warm, wet mouth and continues to suck you off."
                    $ skip_intro = True
                    $ start_position = blowjob

                else:
                    the_mom "I'll just be over here, ready for you..."
                    $ the_mom.draw_person(position = "doggy")
                    $ mc.change_locked_clarity(20)
                    "[the_mom.title] climbs onto your bed, face down and ass up, while she waits for you."
                    if the_date.is_family:
                        mc.name "Hey Sweety, it's me."
                    else:
                        mc.name "Hey [the_date.title], it's [the_date.mc_title]."
                    the_date "Hey [the_date.mc_title], I was just about to head out the door. Is everything okay?"
                    if not the_mom.vagina_available:
                        if the_mom.outfit.can_half_off_to_vagina():
                            $ generalised_strip_description(the_mom, the_mom.outfit.get_half_off_to_vagina_list(), position = "doggy", half_off_instead = True)
                        else:
                            $ generalised_strip_description(the_mom, the_mom.outfit.get_full_strip_list(), position = "doggy")
                        $ mc.change_locked_clarity(40)
                    "You're distracted as [the_mom.possessive_title] reaches back and jiggles her butt for you."
                    the_date "[the_date.mc_title]? Are you there?"
                    mc.name "Uh, yeah. Sorry, I hate to tell you this so late, but something important has come out."
                    mc.name "I'm not going to be able to make it for our date tonight."
                    the_date "Oh no, is everyone okay?"
                    $ the_date.change_stats(happiness = -20, love = -3)
                    $ mc.change_locked_clarity(30)
                    "[the_mom.title] grabs one ass cheek and pulls it to the side, giving you a clear view of her pretty pink pussy."
                    menu:
                        "Fuck [the_mom.title]'s pussy right away":
                            "You unzip your pants and step closer to [the_mom.possessive_title]."
                            if the_date.is_family:
                                mc.name "Something urgent came up at work and requires my full attention."
                            else:
                                mc.name "It's my Mom, she really needs me close right now."
                            $ mc.change_locked_clarity(40)
                            "You grab [the_mom.title]'s hips with your free hand and hold her steady as you slide your cock into her wet pussy. You fuck her slowly while you talk."
                            $ the_mom.draw_person(position = "doggy")
                            mc.name "I can't really say any more than that right now. I'm sorry."
                            the_date "I understand, I hope everything works out. Let's try and reschedule some time soon, okay?"
                            $ mc.change_locked_clarity(30)
                            $ play_moan_sound()
                            "[the_mom.possessive_title!c] grabs one of your pillows to muffle her moans with."
                            if the_date.is_family:
                                mc.name "Yeah, I'll be in touch. Thanks for understanding sweety. Bye."
                            else:
                                mc.name "Yeah, I'll be in touch. Thanks for understanding [the_date.title]. Bye."
                            the_date "Bye..."
                            if the_mom.has_taboo("condomless_sex") or the_mom.wants_condom():
                                the_mom "[the_mom.mc_title], did you put on a condom?"
                                mc.name "Nope. [the_date.title] doesn't like condoms."
                                the_mom "Then... I'll give you everything she could give you! I don't care if you fuck my pussy unprotected [the_mom.mc_title]!"
                                $ the_mom.break_taboo("condomless_sex")
                            else:
                                "As soon as you put your phone down [the_mom.title] starts to moan loudly."
                                $ play_moan_sound()
                                the_mom "Oh [the_mom.mc_title], that feels amazing!"
                            $ skip_intro = True
                            $ start_position = doggy
                            $ skip_condom = True


                        "Wait until you're off the phone":
                            "You place a hand on [the_mom.possessive_title]'s butt and squeeze it idly as you talk."
                            if the_date.is_family:
                                mc.name "Something urgent came up at work and requires my full attention."
                            else:
                                mc.name "It's my Mom, she really needs me close right now."
                            mc.name "I can't really say any more than that right now. I'm sorry."
                            the_date "I understand, I hope everything works out. Let's try and reschedule some time soon, okay?"
                            $ mc.change_locked_clarity(30)
                            "[the_mom.possessive_title!c] puts a hand between her legs and starts to massage her clit while you're talking."
                            if the_date.is_family:
                                mc.name "Yeah, I'll be in touch. Thanks for understanding sweety. Bye."
                            else:
                                mc.name "Yeah, I'll be in touch. Thanks for understanding [the_date.title]. Bye."
                            the_date "Bye..."


                $ the_mom.add_situational_slut("Eager", 5, "I'll show that skank how a {i}real{/i} woman should treat him!")
                call fuck_person(the_mom, private = True, skip_intro = skip_intro, start_position = start_position, skip_condom = skip_condom) from _call_fuck_person_KSO036
                $ the_report = _return
                $ the_mom.clear_situational_slut("Eager")
                if the_report.get("guy orgasms", 0) > 0:
                    the_mom "Ah... Well, wasn't that better than anything that girl would have done?"
                    mc.name "That was great [the_mom.title]."
                    $ the_mom.change_happiness(10)
                    $ the_mom.draw_person()
                    the_mom "Anything for my special man."
                else:
                    the_mom "I'm sorry [the_mom.mc_title], I just don't have the energy I used to have..."
                    mc.name "It's okay [the_mom.title], maybe later we can finish this up."
                    $ the_mom.draw_person()
                    $ the_mom.change_happiness(-5)
                    the_mom "I'll do my best. For my special man I'll try anything at all."

                the_mom "Now, would you like to watch some TV with me? I'll get us some snacks, we can spend the whole night together."
                mc.name "Sounds good [the_mom.title]."
                $ the_mom.change_love(1 + mc.charisma)
                $ the_mom.apply_planned_outfit(show_dress_sequence = True)
                $ the_mom.draw_person(position = "sitting")
                "You spend the rest of the evening with [the_mom.possessive_title], sitting on the couch, watching TV, and chatting."
                return True

            "Tell her no":
                mc.name "Sorry [the_mom.title], but I just can't cancel my plans this suddenly."
                mc.name "I need to get going."
                if the_mom.love > 80:
                    "You hurry to the door, but [the_mom.possessive_title] grabs your arm."
                    $ mc.change_locked_clarity(10)
                    the_mom "Wait! How about just a quickie? You can tell her you're running late."
                    the_mom "I want to take all of your cum, so she doesn't get any. Can you give me that, at least?"
                    menu:
                        "Fuck [the_mom.title] before your date":
                            "You sigh, then nod."
                            mc.name "Fine, but we need to make it quick."
                            $ the_mom.change_stats(love = 1, max_love = 80, slut = 1, max_slut = 80)
                            "She nods happily."
                            $ the_mom.add_situational_slut("Eager", 10, "I need to drain those balls before that skank touches him!")
                            call fuck_person(the_mom, private = True) from _call_fuck_person_KSO40
                            $ the_report = _return
                            $ the_mom.clear_situational_slut("Eager")
                            if the_report.get("guy orgasms", 0) > 0:
                                the_mom "Mmm, that was great [the_mom.mc_title]. Whatever happens I'll always be the first woman you come to, right?"
                                mc.name "Of course [the_mom.title]."
                                $ the_mom.change_happiness(5)
                            else:
                                the_mom "I'm sorry [the_mom.mc_title], I just don't have the energy I used to have..."
                                mc.name "It's okay [the_mom.title], maybe later we can finish this up."
                                the_mom "Maybe you do need this other girl... You should find someone who can take care of you properly."
                                $ the_mom.change_happiness(-5)

                            "You're interrupted by a phone call. It's [the_date.title]."
                            if the_date.is_family:
                                mc.name "Hey Sweety...."
                                the_date "[the_date.mc_title], are you on your way?"
                                mc.name "I'm just heading out the door. Something important came up at work, but it's taken care of."
                            else:
                                mc.name "Hey [the_date.title]..."
                                the_date "[the_date.mc_title], are you on your way?"
                                mc.name "I'm just heading out the door. Something important came up, but it's taken care of. Family related."
                            $ the_date.change_stats(happiness = -5, love = -1)
                            the_date "Okay, well I'm waiting here."
                            mc.name "I'm on my way, I won't be long."
                            "You hang up and stuff your cock back into your pants."
                            $ the_mom.draw_person()
                            the_mom "Have a good date [the_mom.mc_title]. Give me a kiss before you go."
                            "You kiss [the_mom.possessive_title], then hurry out of your room."

                        "Tell her no again":
                            mc.name "I don't have time [the_mom.title]. I'm sorry, but I really need to go."
                            mc.name "We can spend time together later, okay?"
                            $ the_mom.change_stats(happiness = -10, love = -2)
                            $ clear_scene()
                            "You hurry out of the room, leaving [the_mom.possessive_title] behind."
                else:
                    "You hurry out of the room, leaving [the_mom.possessive_title] behind."
                    $ the_mom.change_stats(happiness = -10, love = -2)
                    $ clear_scene()

                return False

    elif the_mom.love > 50 and the_mom.effective_sluttiness("sucking_cock") > 40 and the_mom.opinion.giving_blowjobs >= 0: #TODO: Moderate sluttiness. She tries to convince you to stay home by offering sex (default sex system entry)
        the_mom "Oh, you are? I was hoping you would spend some time at home, I barely see you these days."
        mc.name "Sorry, but I've already made these plans. Maybe some other time, okay?"
        the_mom "[the_mom.mc_title], you aren't seeing this girl just for... physical reasons, are you?"
        mc.name "What? Why?"
        the_mom "Well, A boy your age can sometimes be thinking with his penis instead of his head."
        $ mc.change_locked_clarity(10)
        "She steps closer to you and puts a hand to your crotch. It twitches in response, quickly growing hard."
        the_mom "I don't want you out getting in trouble with girls if all you really need is some physical relief."
        the_mom "If you decide to stay home, maybe I can... take care of this for you?"
        if the_date.is_family:
            mc.name "[the_mom.title], my date won't be happy with me if I cancel last minute."
        else:
            mc.name "[the_mom.title], [the_date.title] won't be happy with me if I cancel last minute."
        $ the_mom.draw_person(position = "kneeling1")
        "[the_mom.possessive_title!c] gets onto her knees in front of you, face level with the large bulge in your pants."
        if the_mom.has_taboo("sucking_cock"):
            the_mom "Please [the_mom.mc_title]? You were probably hoping to get a blowjob from her, right? Well..."
            "She hesitates, as if she needs to be extra sure she means what she's about to say."
            $ mc.change_locked_clarity(20)
            the_mom "I could do that too! You wouldn't need to worry about dressing up, or paying for dinner, or even leaving the house."
            the_mom "Just stay home and I'll take better care of you than any whatever skank is trying to get her hands on you!"
        else:
            the_mom "Please [the_mom.mc_title]? If you stay you don't need to worry about dressing up or paying for dinner."
            $ mc.change_locked_clarity(20)
            the_mom "I'll give you a nice blowjob, then when you're finished we can watch some TV and relax."
            the_mom "Doesn't that sound so much nicer than trying to impress some skank you just met? You've known me your whole life already."

        menu:
            "Cancel your date with [the_date.title]":
                $ mc.change_locked_clarity(20)
                "[the_mom.possessive_title!c] cups your crotch and massages it gently while you think about it."
                mc.name "Fine, but she's really not going to be happy about this."
                the_mom "Don't worry about her, I'm the only woman you need in your life right now. You can worry about finding a wife when you're older."
                mc.name "Just... Give me a minute to call her, okay?"
                if the_mom.opinion.giving_blowjobs > 0 and the_mom.effective_sluttiness("sucking_cock") >= 50:
                    the_mom "I can be quiet. Go ahead, I'll just get started..."
                    $ mc.change_locked_clarity(10)
                    "You get your phone out while [the_mom.title] pulls down your pants. Your hard cock bounces against her face when it springs free of your underwear."
                    the_mom "Oh! Sorry, sorry..."
                    $ mc.change_locked_clarity(20)
                    "You call [the_date.title] as [the_mom.possessive_title] starts to lick at your shaft."
                    $ the_mom.draw_person(position = "blowjob", special_modifier = "blowjob")
                    the_date "Hello?"
                    if the_date.is_family:
                        mc.name "Hey Sweety, it's me."
                    else:
                        mc.name "Hey [the_date.title], it's [the_date.mc_title]."
                    the_date "Hey [the_date.mc_title], I was just about to head out the door. Is everything okay?"
                    mc.name "Well, I hate to tell you this so late, but..."
                    $ mc.change_locked_clarity(20)
                    "[the_mom.possessive_title!c] looks up at you from her knees, your cock bulging out one cheek."
                    mc.name "Something important has come up, and it needs to be taken care of. I won't be able to go out tonight."
                    $ the_mom.change_stats(love = 3, max_love = 80, slut = 1, max_slut = 70)
                    $ mc.change_locked_clarity(20)
                    "[the_mom.title]'s eyes light up, and she bobs her head up and down on your shaft happily. You have to stifle a moan."
                    the_date "Oh no, is everyone okay?"
                    $ the_date.change_stats(happiness = -20, love = -3)
                    "[the_date.possessive_title!c]'s disappointment is clear, even over the phone."
                    if the_date.is_family:
                        mc.name "Something urgent came up at work and requires my full attention."
                    else:
                        mc.name "It's a family situation, I'm sorry that I can't say any more."
                    "[the_mom.possessive_title!c] sucks gently on the tip of your cock."
                    the_date "Okay, well... I hope you get that resolved. Let's try and reschedule, okay?"
                    mc.name "Yeah, I'll be in touch. Thanks for understanding [the_date.title]. Bye."
                    the_date "Bye..."
                    $ mc.change_locked_clarity(20)
                    "[the_mom.possessive_title!c] pulls off your cock, smiling happily."
                    the_mom "Thank you [the_mom.mc_title]. Now, should I keep going?"
                    "She starts to suck you off again before you even respond."

                else:
                    "[the_mom.title] nods and waits, still on her knees, while you get your phone out and call [the_date.title]."
                    the_date "Hello?"
                    if the_date.is_family:
                        mc.name "Hey Sweety, it's me."
                    else:
                        mc.name "Hey [the_date.title], it's [the_date.mc_title]."
                    the_date "Hey [the_date.mc_title], I was just about to head out the door. Is everything okay?"
                    mc.name "Well, I hate to tell you this so late, but..."
                    mc.name "Something important has come up, and it needs to be taken care of. I won't be able to go out tonight."
                    "[the_mom.possessive_title!c]'s eyes light up, and she smiles happily at you."
                    $ the_mom.change_stats(love = 2, max_love = 80, slut = 1, max_slut = 70)
                    the_date "Oh no, is everyone okay?"
                    $ the_date.change_stats(happiness = -20, love = -3)
                    "[the_date.possessive_title!c]'s disappointment is clear, even over the phone."
                    if the_date.is_family:
                        mc.name "Something urgent came up at work and requires my full attention."
                    else:
                        mc.name "It's a family situation, I'm sorry that I can't say any more."
                    the_date "Okay, well... I hope you get that resolved. Let's try and reschedule, okay?"
                    if the_date.is_family:
                        mc.name "Yeah, I'll contact you soon, thanks for understanding. Bye."
                    else:
                        mc.name "Yeah, I'll be in touch. Thanks for understanding [the_date.title]. Bye."
                    the_date "Bye..."
                    the_mom "Thank you [the_mom.mc_title]. Now, should I take care of this?"
                    $ mc.change_locked_clarity(10)
                    "She unzips your pants and pulls them down. Your hard cock springs free, bouncing in front of her face."
                    the_mom "Oh!"
                    if the_mom.break_taboo("sucking_cock"):
                        $ mc.change_locked_clarity(20)
                        the_mom "It looks so much bigger when it's right in your face..."
                        "She takes a deep breath."
                        the_mom "It's fine, I can do this. Anything to make my [the_mom.mc_title] feel special and want to spend more time with me."
                    "She gives it an experimental kiss, then slips her lips over the tip."

                if not the_mom.vagina_visible or not the_mom.tits_visible:
                    menu:
                        "Order her to strip" if the_mom.obedience >= 140:
                            mc.name "You should be dressed for the occasion first. Strip."
                            the_mom "Of course, right away [the_mom.mc_title]."
                            $ the_mom.draw_person()
                            "She stands up to get undressed."
                            $ remove_shoes = False
                            $ the_item = the_mom.outfit.get_feet_top_layer
                            if the_item:
                                the_mom "Do you want me to keep my [the_item.display_name] on?"
                                menu:
                                    "Strip it all off":
                                        mc.name "Take it all off, I don't want you to be wearing anything."
                                        the_mom "Yes [the_mom.title]. I'll get completely naked for you."
                                        $ remove_shoes = True

                                    "Leave them on":
                                        mc.name "You can leave them on."
                            $ the_item = None

                            $ generalised_strip_description(the_mom, the_mom.outfit.get_full_strip_list(strip_feet = remove_shoes))
                            $ mc.change_locked_clarity(30)

                            the_mom "There, now you can properly enjoy the view. Shall I get to it, then?"
                            mc.name "Go ahead."

                        "Order her to strip\n{menu_red=16}Requires: 140 Obedience{/menu_red} (disabled)" if the_mom.obedience < 140:
                            pass

                        "Enjoy your blowjob":
                            pass

                $ the_mom.draw_person(position = "blowjob", special_modifier = "blowjob")
                "You rest a hand on the top of [the_mom.possessive_title]'s head as she starts to suck on your cock. She starts slowly, but quickly picks up speed and confidence."
                mc.name "That feels great [the_mom.title]."
                "She pops off your cock for a moment and smiles up at you."
                $ mc.change_locked_clarity(20)
                the_mom "See? You don't need any other women in your life. I'll take care of you [the_mom.mc_title], just like I always have."
                "With that she slides you back into her mouth."
                call fuck_person(the_mom, start_position = blowjob, skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_KSO99
                $ the_report = _return
                if the_report.get("guy orgasms", 0) > 0:
                    the_mom "Ah... Well, wasn't that better than anything that girl would have done?"
                    mc.name "That was great [the_mom.title]."
                    $ the_mom.change_happiness(10)
                    the_mom "Anything for my special man."
                else:
                    the_mom "I'm sorry [the_mom.mc_title], I just don't have the energy I used to have..."
                    mc.name "It's okay [the_mom.title], maybe later we can finish this up."
                    $ the_mom.change_happiness(-5)
                    the_mom "I'll do my best. For my special man I'll try anything at all."
                the_mom "Now, would you like to watch some TV with me? I'll get us some snacks, we can spend the whole night together."
                mc.name "Sounds good [the_mom.title]."
                $ the_mom.change_love(1 + mc.charisma)
                $ the_mom.apply_planned_outfit(show_dress_sequence = True)
                $ the_mom.draw_person(position = "sitting")
                "You spend the rest of the evening with [the_mom.possessive_title], sitting on the couch, watching TV, and chatting."
                return True

            "Tell her no":
                mc.name "I can't do that [the_mom.title]! I'm sorry, but I really do have to get going."
                "You leave her on her knees and hurry out of your room."
                $ the_mom.change_stats(happiness = -5, love = -1)
                return False

    elif the_mom.love > 30 and the_mom.effective_sluttiness("touching_penis") > 15 and the_mom.opinion.giving_handjobs >= 0:
        the_mom "That's nice, I'm sure you'll show her a wonderful time."
        the_mom "This girl, I assume you're interested in her... physically?"
        mc.name "I suppose so, why?"
        $ the_mom.draw_person(position = "sitting")
        "[the_mom.possessive_title!c] sits down on your bed and pats the spot beside her. You sit down with her to talk."
        the_mom "Well, for young men like yourself it's easy to get distracted by a girl's looks."
        the_mom "It's not your fault, your hormones just take over and suddenly all you can look at are her butt and breasts!"
        mc.name "[the_mom.title], I think I'll be fine."
        "She places her hand on your upper thigh and gives it a gentle squeeze."
        the_mom "I want you to find a girl that's really right for you emotionally, not just some bimbo with nice tits."
        the_mom "The easiest way to be sure is to flush out all of those hormones first, so you can see her with a clear head."
        if the_mom.has_taboo("touching_penis"):
            the_mom "I was thinking... Well, if you wanted me to, I could, umm..."
            "[the_mom.possessive_title!c] blushes and looks away, struggling to finish her sentence."
            mc.name "What is it [the_mom.title]?"
            the_mom "I can help you deal with all of those hormones, if you'd like."
            $ mc.change_locked_clarity(10)
            the_mom "I've got a bit of experience, I can... give you a handjob?"
        else:
            $ mc.change_locked_clarity(10)
            the_mom "Let me help you. I'll give you a quick handjob before you go, so you aren't thinking with your penis all night."
            the_mom "You'll feel better, and I promise she'll notice how much more respectful you are."

        menu:
            "Let her \"help\" you":
                if the_mom.has_taboo("touching_penis"):
                    mc.name "That sounds like a really good idea [the_mom.title]."
                    "She breathes a sigh of relief."
                    the_mom "Okay, well then... You just stand up and I'll take care of you."
                    the_mom "Nothing sexual here, of course. I'm just doing my motherly duty trying to help you."
                    mc.name "Of course [the_mom.title], of course."
                else:
                    mc.name "That sounds like a good idea [the_mom.title]."
                    "She smiles happily."
                    the_mom "Good, you just stand up and I'll take care of you."
                    the_mom "It's my job as your mother to do things like this, after all. I think it's more common than people say, really."

                $ the_mom.draw_person()
                "You and [the_mom.possessive_title] both stand up. She reaches down for your pants and unzips them."
                "She pulls them down, gasping softly when your hard cock springs out of your underwear."
                $ mc.change_locked_clarity(10)
                if the_mom.has_taboo("touching_penis"):
                    the_mom "Oh... This is just to help you, okay? There's nothing wrong with it, it's just because I love you..."
                else:
                    the_mom "Oh, you really do need this [the_mom.mc_title]. I'll take care of this for you, leave it to mommy."
                "She wraps her fingers gently around your shaft and gives it a few experimental strokes."
                if not the_mom.tits_visible and (the_mom.effective_sluttiness(["underwear_nudity","bare_tits"]) > 25 or the_mom.opinion.showing_her_tits > 0):
                    if the_mom.has_taboo(["underwear_nudity","bare_tits"]):
                        the_mom "This would probably be faster if you had some more... stimulation, right?"
                        the_mom "Let me take my breasts out... It's just to speed this along, there's nothing wrong about it."
                    else:
                        the_mom "Of course, you probably want to see mommy's tits. Let me get those out for you to look at."
                    "She lets go of your cock and steps back."
                    if the_mom.outfit.can_half_off_to_tits():
                        $ generalised_strip_description(the_mom, the_mom.outfit.get_half_off_to_tits_list(), half_off_instead = True)
                    else:
                        $ generalised_strip_description(the_mom, the_mom.outfit.get_tit_strip_list())
                    $ mc.change_locked_clarity(20)
                    the_mom "There, now you have something to ogle while I get you off."
                    if not the_mom.vagina_visible:
                        menu:
                            "Order her to strip completely" if the_mom.obedience >= 140:
                                mc.name "That's not enough for me. Get naked for me [the_mom.title]."
                                if the_person.has_taboo("bare_pussy"):
                                    the_mom "[the_mom.mc_title], I can't... I shouldn't do that."
                                    mc.name "Come on, I need to get off, and I need to see you naked to do that."
                                    mc.name "You're already jerking me off, it's not a big deal seeing you naked while you do it."
                                    mc.name "I'm going to be late if you keep stalling. Hurry up and get naked!"
                                    $ the_mom.change_obedience(5 + the_mom.opinion.being_submissive)
                                    "She takes a deep breath and starts to strip down."
                                else:
                                    $ the_mom.change_obedience(1 + the_mom.opinion.being_submissive)
                                    the_mom "Of course [the_mom.mc_title]. Whatever you need me to do to make you cum I'll do it."
                                $ remove_shoes = False
                                $ the_item = the_mom.outfit.get_feet_top_layer
                                if the_item:
                                    the_mom "Do you want me to keep my [the_item.display_name] on?"
                                    menu:
                                        "Strip it all off":
                                            mc.name "Take it all off, I don't want you to be wearing anything."
                                            $ remove_shoes = True

                                        "Leave them on":
                                            mc.name "You can leave them on."
                                $ the_item = None

                                $ generalised_strip_description(the_mom, the_mom.outfit.get_full_strip_list(strip_feet = remove_shoes))
                                $ mc.change_locked_clarity(20)
                                if the_mom.break_taboo("bare_pussy"):
                                    the_mom "There. I guess this isn't so strange, really. Now, where were we..."
                                else:
                                    the_mom "There you go [the_mom.mc_title], now enjoy my naked body while I stroke you off."

                            "Order her to strip completely\n{menu_red=16}Requires: 140 Obedience{/menu_red} (disabled)" if the_mom.obedience < 140:
                                pass

                            "Ogle her tits":
                                pass
                    "She wraps her fingers around your shaft again and starts to stroke it."

                else:
                    pass

                the_mom "You've got a date to keep, so cum quickly, okay?"
                call fuck_person(the_mom, start_position = handjob, skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_KSO0100
                $ the_report = _return
                if the_report.get("guy orgasms", 0) > 0:
                    the_mom "There we go [the_mom.mc_title], all taken care of. Now I don't have to worry about you getting into trouble while you're out."
                    "She gives you a happy smile."
                    $ the_mom.change_stats(love = 2, max_love = 80, slut = 2, max_slut = 80)
                    $ the_mom.draw_person()
                    the_mom "Now go on, you've got a date to keep. Have fun out there, okay?"
                    mc.name "Thanks [the_mom.title], I will."
                    "You stuff your cock back in your pants and get ready to leave."
                    the_mom "Wait, one last thing..."
                    $ the_mom.draw_person(position = "kissing", special_modifier = "kissing")
                    "She hurries over to you and kisses you, deeply and passionately."
                    $ the_mom.draw_person()
                    the_mom "Mmm... Remember, Mommy loves you and will always be here for you."
                    mc.name "I love you too [the_mom.title]. See you later."

                else:
                    the_mom "I'm sorry [the_mom.mc_title], I just don't have the energy to finish you off. I need more practice I guess."
                    "She seems rather disappointed in herself."
                    $ the_mom.change_slut(1, 60)
                    $ the_mom.draw_person()
                    mc.name "We can work on that. Thanks for trying [the_mom.title], it was still nice."
                    "[the_mom.possessive_title!c] gives you a weak smile."
                    the_mom "Go on, you've got a date to keep. Have fun out there."
                $ the_mom.break_taboo("touching_penis")
                $ the_mom.update_outfit_taboos()
                $ the_mom.apply_planned_outfit()
                "You hurry out of the house to meet [the_date.title]."
                $ clear_scene()
                return False

            "Tell her no":
                mc.name "Sorry [the_mom.title], but I'm going to pass."
                if the_mom.has_taboo("touching_penis"):
                    the_mom "Of course! It's not right, I'm your mother and I shouldn't... How could I even suggest that!"
                    mc.name "Relax, it's fine. I don't think it's a bad idea, but I might need my energy for later tonight."
                    the_mom "Oh, I... Oh [the_mom.mc_title], please promise me you'll be safe, at the very least."
                    mc.name "I will [the_mom.title], I promise."
                    $ the_mom.change_slut(1, 50)
                    the_mom "Well, if that's what you're planning... Be sure to show her a good time. Don't be selfish, girls don't like that."
                    mc.name "Okay [the_mom.title], I'll do that."
                else:
                    mc.name "Depending on how the date goes I might need all my energy for later tonight."
                    the_mom "Oh [the_mom.mc_title], well..."
                    $ the_mom.change_slut(1, 60)
                    the_mom "In that case, be sure to show her a good time. Don't be selfish, girls don't like that."
                    mc.name "Noted, thanks [the_mom.title]."
                $ the_mom.draw_person()
                "She stands up and moves to the door."
                the_mom "Don't be out too late, I worry when I don't know where you are. Love you sweetheart."
                mc.name "Love you too [the_mom.title]."
                $ clear_scene()
                return False

    else:
        the_mom "That's nice, I'm sure you'll have a wonderful time together."
        the_mom "Don't stay out too late, and make sure you use protection if you two are going to..."
        "She blushes and shrugs."
        the_mom "You know."
        mc.name "Relax [the_mom.title], I'm not a little kid."
        the_mom "I know. Oh lord, do I know. You've grown up into such a fine man, I just... hate to think of you leaving."
        the_mom "Come here, I need a hug."
        "[the_mom.possessive_title!c] pulls you into her arms. She rests her head on your shoulder while you hold her."
        "You're silent for a few moments, then she steps back and holds you at arms length."
        $ the_mom.change_love(1)
        the_mom "I love you sweetheart. Have a good night."
        mc.name "I love you too [the_mom.title]. I'll see you later."
        $ clear_scene()
        return False #Returns False if the date was not intercepted.
    return False

label stephanie_nora_3some_choose_trainable_label(the_person):
    # Training dialogue can be found in game/trainables/opinion_trainables.rpy
    # Currently writing for trainables is in progress.
    # I have defaulted this label to grab training for "anal creampies" since that is currently the only finished section.
    # Once more training dialogie is complete, I'll add in a method for choosing other things.
    stephanie "Okay, and what are we training tonight?"
    "You think about it for a moment."
    "KiNA edit: Add their opinion in choice"
    menu:
        # "Anal Creampies":
        #     return "anal creampies"
        # "Anal Sex":
        #     return "anal sex"
        # "Fucking Bareback":
        #     return "bareback sex"
        "Getting Covered in Cum (Current : [the_person.opinion.being_covered_in_cum])":
            return "being covered in cum"
        # "Getting Fingered":
        #     return "being fingered"
        "Being Submissive (Current : [the_person.opinion.being_submissive])":
            return "being submissive"
        #"Big Dicks (Current : [the_person.opinion.big_dicks])":
        #    return "big dicks"
        # "Cheating":
        #     return "cheating on men"
        # "Vaginal Creampies":
        #     return "creampies"
        "Receiving Cum Facials (Current : [the_person.opinion.cum_facials])":
            return "cum facials"
        # "Fucking Doggy Style":
        #     return "doggy style sex"
        "Swallowing Cum (Current : [the_person.opinion.drinking_cum])":
            return "drinking cum"
        # "Getting Eaten Out":
        #     return "getting head"
        "Giving Blowjobs (Current : [the_person.opinion.giving_blowjobs])":
            return "giving blowjobs"
        # "Giving Handjobs":
        #     return "giving handjobs"
        # "Giving Tit Fucks":
        #     return "giving tit fucks"
        # "Committing Incest":
        #     return "incest"
        # "Kissing":
        #     return "kissing"
        # "Wearing Lingerie":
        #     return "lingerie"
        # "Masturbating":
        #     return "masturbating"
        # "Fucking Missionary Style":
        #     return "missionary style sex"
        "Being Naked (Current : [the_person.opinion.not_wearing_anything])":
            return "not wearing anything"
        "Not Wearing Underwear (Current : [the_person.opinion.not_wearing_underwear])":
            return "not wearing underwear"
        # "Multiple Romantic Partners":
        #     return "polyamory"
        # "Having Sex in Public":
        #     return "public sex"
        # "Fucking While Standing Up":
        #     return "sex standing up"
        "Showing Off Your Ass (Current : [the_person.opinion.showing_her_ass])":
            return "showing her ass"
        "Showing Off Your Tits (Current : [the_person.opinion.showing_her_tits])":
            return "showing her tits"
        "Wearing Skimpy Outfits (Current : [the_person.opinion.skimpy_outfits])":
            return "skimpy outfits"
        "Wearing Skimpy Uniforms (Current : [the_person.opinion.skimpy_uniforms])":
            return "skimpy uniforms"
        # "Taking Control During Sex":
        #     return "taking control"
        # "Having Threesomes":
        #     return "threesomes"
        # "Vaginal Sex":
        #     return "vaginal sex"
    return "giving blowjobs"

