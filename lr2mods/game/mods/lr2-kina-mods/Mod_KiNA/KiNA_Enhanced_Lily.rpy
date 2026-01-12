#Counter = KEL01

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["lily_sex_accept"] = "lily_sex_accept_revamp"
    config.label_overrides["lily_greetings"] = "lily_greetings_revamp"
    config.label_overrides["lily_flirt_response_high"] = "lily_flirt_response_high_revamp"
    config.label_overrides["lily_cum_pullout"] = "lily_cum_pullout_revamp"
    config.label_overrides["lily_cum_vagina"] = "lily_cum_vagina_revamp"
    config.label_overrides["lily_sex_review"] = "lily_sex_review_revamp"
    config.label_overrides["lily_condom_demand"] = "lily_condom_demand_revamp"
    config.label_overrides["lily_condom_ask"] = "lily_condom_ask_revamp"
    config.label_overrides["lily_condom_bareback_ask"] = "lily_condom_bareback_ask_revamp"
    config.label_overrides["lily_condom_bareback_demand"] = "lily_condom_bareback_demand_revamp"
    config.label_overrides["lily_vaginal_sex_taboo_break"] = "lily_vaginal_sex_taboo_break_revamp"



label lily_sex_accept_revamp(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            $ random_reply = get_random_from_list(["You're definitely my brother, I was thinking the same thing.", "Perverts DO thinks alike!", "Pervert! Just like me!"])
            the_person "[random_reply]"
        else:
            if the_position.skill_tag == "Foreplay":
                if "giving tit fucks" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["You love these, aren't you?", "Well, technically, these are {i}yours{/i}", "These puppers?", "Boob sandwich, coming up!", "You {i}pervert!{/i}"])
                    the_person "[random_reply]"
                elif "kissing" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Mmmm, kiss me  " + the_person.mc_title + ".", "You're definitely my brother, I was thinking the same thing.", "Let's french kiss"])
                    the_person "[random_reply]"
                else:
                    the_person "You want to do that with your little sister [the_person.mc_title]? Well, you're lucky I'm just as perverted."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Don't just stare, you making me shy~","Oh, come here and give your little sister some pleasure.", "Be gentle, I'm sensitive down there.", "Pervert! Going down on his own little sister! OHHHH.. Don't stop~"])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["Come here, let your little sister take care of you.", "I found a banana just as big the other day, ends up buying it so I could train myself. ", "Be lucky, your sister is perverted as much as you do. "])
                    the_person "[random_reply]"
            else:
                if not lily_knows_about_mom(): # mod only
                    $ random_reply = get_random_from_list(["Oh yes, brother, please, fuck my brains out.", "Oh yes, come here and fuck " + the_person.possessive_title + "!", "Look here... It's twitching so much for your dick!" "Screw your sister till she can't walk properly!!", "Put it in.. Give it to me!", "Mmmm, I want it! I want your penis, " + the_person.mc_title + "!"])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["Lemme me show you what you can't get with mom.", "We are gonna fuck like rabbits!", "Oh yes, come here and fuck me!", "I'm yours however you want me."])
                    the_person "[random_reply]"
    else:
        if the_person.love < 40:
            if not had_family_threesome(): # mod only
                $ random_reply = get_random_from_list(["Okay, let's do it. Just make sure Mom never finds out, okay?", "Okay, let's do it.", "As long as Mom doesn't know..."])
                the_person "[random_reply]"
            else:
                $ random_reply = get_random_from_list(["Okay, let's do it, next time we should include Mom, okay?", "Okay, let's do it.", "Should we call Mom?"])
                the_person "[random_reply]"
        else:
            if the_position.skill_tag == "Foreplay":
                the_person "Okay, lets play a little with each other."
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Okay, brother show me what you can do with your tongue.", "Be gentle, I'm sensitive down there.", "Such a gentleman~"])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["Okay, let me show you what your little sister can do with her mouth.", "That banana training better be worth it."])
                    the_person "[random_reply]"
            else:
                if the_person.has_taboo(["vaginal_sex", "anal_sex"]):
                    $ random_reply = get_random_from_list(["Oh, right, well...okay, you can fuck your sister, but only this time.", "Promise me. Just this once, okay?"])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["I don't mind fucking with my big brother.", "Be gentle, I'm still scared of your size.", "I'm ready... I think."])
                    the_person "[random_reply]"
    return

label lily_greetings_revamp(the_person):
    if the_person.love < 0:
        the_person "Ugh, can you tell [mom.fname] whatever you want to say to me right now? I don't want to hear it."
    elif the_person.happiness < 90:
        the_person "Hey [the_person.mc_title]..."
    else:
        if (the_person.has_event_day("last_birth") and (the_person.days_since_event("last_birth") < 21 ) and (time_of_day in (0, 3, 4))) and renpy.random.randint(0, 2) == 2: #roughly 33% .. She's given birth and lactating
            #Dont want to be obnoxious much
            $ event = renpy.random.randint(0, 2)
            if event == 0:
                $ the_person.outfit.strip_to_tits(prefer_half_off = True) #Make sure she is topless
                $ the_person.draw_person(position = "sitting")
                "[the_person.possessive_title!c] sat on the bed as she cradled the tiny bundle in her arms."
                "The gentle curve of her breast revealed as the baby nestled against it, eagerly sucking without a care in the world. "
                "[the_person.title]'s fingers brushed lightly over the baby’s head, smoothing down the wisps of hair that clung to her delicate scalp."
                "Her eyes lifted from the baby, meeting your own, smiling warmly as you approached."
                the_person "She’s beautiful, isn’t she?"
                the_person "So perfect. Like me."
                mc.name "Yeah..."
                mc.name "Both of you are beautiful."
            elif event == 1:
                $ the_person.draw_person(position = "sitting")
                "[the_person.possessive_title!c] sat on the bed as she cradled the tiny bundle in her arms."
                "[the_person.title]'s fingers brushed lightly over the baby’s head, smoothing down the wisps of hair that clung to her delicate scalp."
                "The baby cooed contently at the attention she's getting from her mom."
                "[the_person.possessive_title!c]'s gaze lifted from the baby, smiling warmly as you approached."
                the_person "Wanna hold her?"
                "She said softly, holding the baby out to me. "
                the_person "She won't bite."
                "You hesitated for a moment before taking the baby from her arms."
                "The tiny bundle was warm and fragile, and you felt a surge of protectiveness as you cradled her close."
                "[the_person.possessive_title!c] watched you, her eyes filled with surprise."
                the_person "You surprised me... I didn't expect my brother to be a natural with babies."
            else:
                "You find the baby laying on the bed, crying loudly."
                $ the_person.draw_person(position = "back_peek")
                the_person "Good morning, papa..."
                the_person "Would you be a dear and check up on her?"
                if time_of_day == 0:
                    the_person "Mama gotta dress a bit."
                else:
                    the_person "Mama gotta take her makeup off."
                "She winks."
                mc.name "Sure. No problem mama."
                "You lovingly picked the baby up and attempt to sooth her."
                "As expected, she have wetted herself. You expectly change her diaper and sure enough, the crying stopped and she cooed at your teasing."
                "Her little fingers tries to grab your face as you bring her closer."                
                $ the_person.draw_person(position = "stand2")
                "[the_person.possessive_title!c] watched as you play with the baby, her eyes softening as she watches you both."
                the_person "Well, now I know little Pumpkin is fine staying with papa if needs be."
            
        elif the_person.is_pregnant and ( day < the_person.event_triggers_dict.get("preg_transform_day", -1) ) and (time_of_day == 0 or time_of_day == 1) and renpy.random.randint(0, 2) == 2: #roughly 33%
            #Dont want to be obnoxious much                  
            if the_person.knows_pregnant:
                if the_person.is_mc_father:
                    the_person "[the_person.mc_title]. Can you help please?"
                    "She is clutching her stomach, her face pale and sweaty."
                    mc.name "What's wrong?"   
                    the_person "I think I'm having morning sickness again..."
                    "She said, her voice barely above a whisper. She swallowed hard, trying to fight back the nausea."
                    mc.name "Do you need anything? Water? Ginger ale?"
                    "[the_person.fname] shook her head, her hair sticking to her damp forehead."
                    the_person "Just... hold me, [the_person.mc_title]."
                    "You wrapped your arms around her shoulder. She leaned into you, her body tense with the effort to stay composed."
                    "After a few minutes, [the_person.fname]'s breathing steadied, and she pulled back slightly, looking up at you with watery eyes."
                    the_person "Thank you. I'm fine now."
                    "She gives you a loving smile."
                else:
                    #Dont care much tbh
                    the_person "Hey [the_person.mc_title]..."
                    mc.name "You look aweful, are you okay?"
                    the_person "Yeah, morning sickness... it's been getting worse lately."
                    "But as she spoke, her expression suddenly changed, a hand flying to her mouth as her face paled."
                    "Without a word, she rushed past you and disappeared into the bathroom, the sound of retching echoing through the house."
                    "You took a sit on her bed waiting. Few minutes later, she's back."
                    the_person "Sorry [the_person.mc_title]... You know how it is. It probably go away in few weeks."
            else:
                the_person "Hey [the_person.mc_title]. Good mmhmm..."
                "She suddenly closed her mouth and bolted for the bathroom."
                if the_person.number_of_children_with_mc > 0:
                    "You checked the date on your phone. It's likely she is suffering from morning sickness. Looks like you managed to get her pregnant again."
                else:
                    "Confused, you stood there for a moment, unsure of what to do. You had never seen [the_person.possessive_title] like this before."
                "Still concerned, you followed her to the bathroom door, hesitating before knocking softly."
                $ mc.change_location(home_shower)
                mc.name "[the_person.title] ? Are you okay?"
                "Inside, she knelt before the toilet, her body convulsing with each wave of nausea."
                if the_person.has_child_with_mc:
                    the_person "I {i}think{/i} I'm pregnant again. Can you buy me a test kit later?"
                else:
                    the_person "Oh shit... Oh shit... Oh shit! It better not be!"
                "[the_person.possessive_title!c] took a big breath."
                the_person "Let’s go back to my room."
                $ mc.change_location(lily_bedroom)                
        elif the_person.obedience > 180 and renpy.random.randint(0, 1) == 1:
            if the_person.sluttiness > 60:
                the_person "Hey [the_person.mc_title], do you need your little sister for something?"
                "[the_person.title] crosses her arms behind her back."
            else:
                the_person "Hi [the_person.mc_title]."
        else:
            if the_person.sluttiness > 60:
                the_person "Oh hey [the_person.mc_title], I was just thinking about you."
                "[the_person.title] smiles seductively."
            else:
                the_person "Hey, need something?"
    return

label lily_flirt_response_high_revamp(the_person):
    if mc.location.person_count == 1: #If you are alone she'll flirt with you
        if the_person.effective_sluttiness() > (25 - the_person.opinion.incest*5): # High sluttiness flirt
            if ((the_person.sex_record.get("Vaginal Sex", 0) > 20) or (the_person.sex_record.get("Anal Sex", 0) > 20)):
                "She blinks seductively..."
                the_person "Oh my god, you're so bad [the_person.mc_title]! Do I... Do I really look that good?"
                mc.name "Yeah you do! You look amazing."
                "She blushes and smiles."
                the_person "Thank you. I think you are very handsome too.."
                menu:
                    "Kiss her":
                        "You step closer to [the_person.possessive_title] and put your hand around her waist. She looks into your eyes."
                        the_person "[the_person.mc_title]..."
                        "She whispered, almost like a plea."
                        the_person "Please."
                        "You leaned in further, lips brushing against hers in a tender, passionate kiss."
                        call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KEL01
                        $ the_person.call_dialogue("sex_review", the_report = _return)
                        $ the_person.review_outfit()

                    "Just flirt":
                        mc.name "Thanks. Do you want to get me out of my clothes?"
                        "She giggles and slaps your shoulder gently."
                        the_person "Oh my god, stop!"
                        mc.name "It's fine if you do, I totally get it."
                        "You catch her eyes glancing down at your crotch, then she turns away and laughs you off."
                        the_person "Pervert."
            else:
                the_person "Oh my god, you're so bad [the_person.mc_title]! Do I... Do I really look that good?"
                mc.name "Yeah you do! You look amazing."
                "She blushes and smiles."
                the_person "Thank you. I think you look good too."
                menu:
                    "Kiss her":
                        "You step closer to [the_person.possessive_title] and put your hand around her waist. She looks into your eyes."
                        if the_person.has_taboo("kissing"):
                            $ the_person.call_dialogue("kissing_taboo_break")
                            $ the_person.break_taboo("kissing")
                            "You kiss her. She hesitates for a second before relaxing and leaning her body against yours."
                        else:
                            the_person "What are you doing..."
                            "You respond by kissing her. She hesitates for a second, then relaxes and leans her body against you."
                        call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KEL02
                        $ the_person.call_dialogue("sex_review", the_report = _return)
                        $ the_person.review_outfit()

                    "Just flirt":
                        mc.name "Thanks. Do you want to get me out of my clothes?"
                        "She giggles and slaps your shoulder gently."
                        the_person "Oh my god, stop!"
                        mc.name "It's fine if you do, I totally get it."
                        "You catch her eyes glancing down at your crotch, then she turns away and laughs you off."
                        the_person "You're my brother, that would be weird."

        else: # Just high love flirt
            "[the_person.possessive_title!c] laughs and blushes."
            the_person "[the_person.mc_title], I'm your sister! Don't be so weird."
            mc.name "I'm just joking around. You're looking good, that's all."
            if mom_knows_about_lily():
                the_person "Thanks! I don't really mind."
            else:
                the_person "Thanks! I don't really mind, but I think [mom.fname] would freak out if she heard you talking like that."


    else: #She shushes you and rushes you off somewhere private.
        if the_person.effective_sluttiness() > (25 - the_person.opinion.incest*5): #She's slutty, but you need to find somewhere private so people don't find out.
            "[the_person.possessive_title!c] blushes, then glances around nervously."
            the_person "Shhh... What if someone heard you?"
            mc.name "Relax, we're not doing anything wrong, are we?"
            the_person "No but... They might not understand, you know?"

            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    if ((the_person.sex_record.get("Vaginal Sex", 0) > 20) or (the_person.sex_record.get("Anal Sex", 0) > 20)):
                        "She grabs your arm and drag you along while glancing around."
                        the_person "We gonna find a hidden place so peoples can hear me... err.. I mean us!"
                        call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_lily_flirt_response_high_KEL03
                        the_person "Secret, right?"
                        mc.name "Nobody is going to find out."
                        "You leaned down, your lips brushing against hers tenderly at first, then deepening the kiss with a hunger that matched her own."
                    else:
                        mc.name "Fine, come with me then."
                        "You take [the_person.title]'s hand and start to lead her away."
                        the_person "Where are we going?"
                        mc.name "We're going somewhere nobody will overhear us, so that you don't have to worry about that any more."
                        call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_lily_flirt_response_high_KEL01
                        "You turn to [the_person.possessive_title] and pull her close to you."
                        the_person "Ah! We... Nobody is going to find out, right?"
                        mc.name "Nobody is going to find out."

                        if the_person.has_taboo("kissing"):
                            "You lean down to kiss her. She pulls her head back, surprised."
                            $ the_person.call_dialogue("kissing_taboo_break")
                            $ the_person.break_taboo("kissing")
                        else:
                            "You lean down and kiss her. She hesitates for a split second before returning the kiss, pressing her body against yours."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KEL03
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_lily_flirt_response_high_KEL02

                "Just flirt":
                    mc.name "I'll save all the really dirty stuff for when we're alone then."
                    the_person "Oh my god, you're so bad!"
                    "She blushes and slaps you playfully on the shoulder."
                    the_person "Isn't my big brother supposed to be taking care of me? You're just going to get us in trouble!"
                    mc.name "Don't worry, I'll always be around to take care of you. We're just having a little fun."
                    "[the_person.possessive_title!c] smiles and gives you a quick hug."

        else: #She's not slutty, so she's embarrassed about what you're doing.
            "[the_person.possessive_title!c] blushes, then glances around nervously."
            the_person "Oh my god, you can't just say stuff like that when there are people around!"
            mc.name "So it's fine if I say things like that when we're alone?"
            if mom_knows_about_lily():
                the_person "Well... I don't really mind, as long as we're just joking around."
                mc.name "Don't worry, nobody cares."
                the_person "Okay, I actually kind of like hearing I look pretty."
            else:
                the_person "Well... I don't really mind, as long as we're just joking around. I just don't want [mom.fname] to get upset with us."
                mc.name "Don't worry, I promise she won't find out."
                the_person "Okay, then it's fine. I actually kind of like hearing I look pretty."
    return

label lily_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Mmm... Are you trying to make [the_person.possessive_title] drunk?"
    "She gives you a smirk."
    the_person "Hah! I was right, aren't I? Is the drunk me more sexier?"
    "She sets her wine down on her nightstand."
    the_person "Get over here! Fuck me crazy!"
    return

label lily_cum_pullout_revamp(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Wait... Do you want to take the condom off and cum inside me?"
                the_person "I'm already pregnant, and it felt so good before..."

            elif the_person.on_birth_control:
                the_person "Take... Take the condom off, I want you to cum inside me raw!"
                $ the_person.update_birth_control_knowledge()
                the_person "I'm on the pill, so it doesn't even matter, and creampies feel so good!"
                "She moans happily."
            else:
                the_person "Wait, take the condom off first! I... I want you to cum bareback!"
                "She pants happily."
                the_person "It's my fault if I get pregnant, okay? You don't need to worry, I know it would be my fault!"

            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."

        else:
            the_person "Oh my god, do it! Cum [the_person.mc_title]!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Cum wherever you want [the_person.mc_title]!"
            elif the_person.opinion.creampies > 0:
                "[the_person.possessive_title!c] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Yes! Cum inside me [the_person.mc_title], I want it!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    the_person "I... Oh god, I want you to cum inside me [the_person.mc_title]!"
                    the_person "Go ahead and knock your little sister up!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                $ the_person.update_birth_control_knowledge()
                the_person "Cum wherever you want [the_person.mc_title], I'm on the pill!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Oh god, I'm going to make my brother cum! Ah!"
        else:
            if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                if the_person.has_child_with_mc : # == 0:
                    the_person "Oh god, pull out! I don't want to get pregnant again for now!"
                else:
                    the_person "Oh god, pull out! I'm not ready to become a mother!"

            elif the_person.opinion.creampies < 0:
                the_person "Pull out, I want you to cum all over me [the_person.mc_title]!"

            else:
                if the_person.has_child_with_mc : # == 0:
                    if the_person.baby_desire < 20: #She doesn't want it.
                        the_person "Wait, you need to pull out! No!"
                    else:
                        the_person "Ah! You... You need to pull out! I am not risking another baby"
                else:
                    if the_person.baby_desire < 20: #She doesn't want it.
                        the_person "Wait, Pull out! I can't risk getting pregnant with your baby!"
                    else:
                        the_person "Wait, you need to pull out! We can't have baby together!"
    return

label lily_cum_vagina_revamp(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh god, your cum feels so nice and warm inside me..."
            "She sighs happily."
            the_person "I guess that's one perk of you knocking me up. No more condoms to worry about."

        elif the_person.on_birth_control:
            the_person "Oh god, you really did it... You came inside your own sister."

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            if the_person.has_significant_other:
                the_person "I know I shouldn't, but I love having my own brother's cum inside me."
                the_person "I guess if you get me pregnant I'll have to say it's my [the_person.so_title]'s though, so people don't judge us."
            else:
                the_person "Pump me full of your hot cum, I don't care that you're my brother, I want you to get me pregnant!"
        else:
            if the_person.has_significant_other:
                the_person "Oh god, you really did it... I'm not on the pill and you still came inside me."
                $ the_person.update_birth_control_knowledge()
                the_person "I hope my [the_person.so_title] never finds out about this..."

            else:
                the_person "Oh god, you really did it... I'm not on the pill and you still came inside me."
                $ the_person.update_birth_control_knowledge()
                the_person "I can't believe I let you do that."


    else: #She's angry
        if not the_person.on_birth_control:
            if the_person.has_significant_other:
                the_person "Fuck, fuck! You can't cum in me, I'm not on the pill!"
                $ the_person.update_birth_control_knowledge()
                the_person "What if you got me pregnant? What would [mom.fname] say?"
                "She groans unhappily."
                the_person "What would my [the_person.so_title] say? I don't know if I could lie to him."
            else:
                the_person "Oh god no, you can't cum inside me, I'm not on the pill!"
                $ the_person.update_birth_control_knowledge()
                "She groans unhappily."
                if the_person.has_child_with_mc : # == 0:
                    the_person "You trying to get your sister pregnant again?"
                    the_person "My friend gonna teased me all day again!"
                else:
                    the_person "What would I do if my own brother got me pregnant?"
                    the_person "I'd die of embarrassment if anyone found out!"

        elif the_person.has_significant_other:
            the_person "Oh god, I can't believe you just came inside me... What if my birth control doesn't work?"
            $ the_person.update_birth_control_knowledge()
            "She takes a deep breath and tries to calm herself down."
            the_person "I would have to tell everyone it was my [the_person.so_title]'s, but I would still know..."

        elif the_person.opinion.creampies < 0:
            the_person "Hey, I told you to pull out! Ugh, you've made such a mess inside me now."

        else:
            the_person "Oh god, I can't believe you just came inside me... What if my birth control doesn't work?"
            $ the_person.update_birth_control_knowledge()
            "She takes a deep breath and calms herself down."
            the_person "It's probably fine... Right? Yeah, I'm sure it's fine. The pill is like a ninety-nine percent effective, right?"

    return

label lily_sex_review_revamp(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and the_person.has_significant_other and the_person.opinion.cheating_on_men <= 0: #It was public and she cares.
        if the_person.is_affair: #Dialogue about her being into it, but you can't do this in case she gets caught. #NOTE: Shouldn't currently be possible, but might be useful for mods/ updates
            the_person "[the_person.mc_title], we need to be more sneaky next time. What do I tell my [the_person.so_title] if someone tells him about this?"
            mc.name "Don't worry, nobody knows who we are and nobody is going to tell your [the_person.so_title]."
            "[the_person.possessive_title!c] seems unconvinced, but nods anyways."
        elif used_obedience:
            the_person "I can't believe you made me do that right here... What if people recognise us, [the_person.mc_title]?"
            the_person "How would I explain any of this to my [the_person.so_title] if they tell him?"
            mc.name "Don't worry, nobody knows who we are and nobody is going to tell your [the_person.so_title]."
            "[the_person.possessive_title!c] seems unconvinced, but nods anyways."

        else:
            the_person "We should have found somewhere else, people are looking at us now... What if someone recognises us?"
            mc.name "Nobody knows who we are, and nobody really cares anyways. Just relax, everything's alright."
            "[the_person.possessive_title!c] seems unconvinced, but nods anyways."

    #She's single, but worried that you did in public.
    elif the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "I can't believe you made me do that right here... What if people recognise us, [the_person.mc_title]?"
            mc.name "Don't worry, nobody knows who you are, and nobody cares what we do together. Just relax, everything's alright."
            "[the_person.possessive_title!c] seems unconvinced, but nods anyways."
        elif mom_knows_about_lily():
            the_person "We really should have found somewhere private, I don't know what I was thinking..."
            the_person "What if someone recognises us? We are family after all!"
            mc.name "Relax, no one is going to find out. Nobody here knows who you are, and nobody cares what we do together."
            "[the_person.possessive_title!c] seems unconvinced, but nods anyways."
        else:
            the_person "We really should have found somewhere private, I don't know what I was thinking..."
            the_person "What if someone recognises us? [mom.fname] could find out!"
            mc.name "Relax, [mom.fname] isn't going to find out. Nobody here knows who you are, and nobody cares what we do together."
            "[the_person.possessive_title!c] seems unconvinced, but nods anyways."

    # special condition - you fucked her brains out
    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            "[the_person.possessive_title!c] looks away, embarrassed by what just happened."
            the_person "Are we done?"
            mc.name "Don't act so innocent [the_person.title], you obviously had a great time."
            mc.name "Did you know you looked really cute when you came the third time?"
            the_person "It was... amazing. But I don't want to discuss how my brother fucked my brains out, please?"
        else:
            the_person "Oh wow, that was... I can't believe we just did that."
            "She seems dazed by her orgasms as she struggles to put full sentences together."
            the_person "We shouldn't have done that... But it felt really good."

        call sex_review_trance(the_person) from _call_sex_review_trance_lily_sex_review_K01

    # special condition abort due to lack of girl energy without orgasm
    elif the_report.get("girl orgasms", 0) == 0 and the_person.energy < 20:
        the_person "I'm sorry [the_person.mc_title], but I'm tired."
        mc.name "No problem [the_person.title], we had fun, right?"
        if the_person.is_home:
            the_person "I had fun, now let me study."
        else:
            the_person "Yeah, we did."

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "That was fun [the_person.mc_title], but don't you think that next time we could..."
            "She hesitates, obviously still a little embarrassed."
            the_person "Uh... Go a little further? I think that could be even better."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Oh my god, that was fun [the_person.mc_title]! Whew, I think I need to sit down."
            $ the_person.draw_person(position = "sitting")
            "She gives you a dopey smile, still reeling from her climax."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks away, embarrassed by what you've just done."
            the_person "Are we finished?"
            mc.name "Don't act so innocent [the_person.title], you obviously had a great time."
            mc.name "Did you know you look really cute when you cum?"
            the_person "It was... nice, I guess. Can we just talk about something other than me touching my own brother, please?"

        else: # She's surprised she even tried that.
            the_person "Oh wow, that was... I can't believe we just did that."
            "She seems dazed by her orgasm as she struggles to put full sentences together."
            the_person "We shouldn't have done that... But it felt really good."

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Is that all? I mean, I had a great time, but you should get to cum too."
            mc.name "Maybe next time, making you feel good was fun enough."
            the_person "Well, maybe we can go even further next time, alright? I've got some fun ideas for both of us."
            "She gives you a dirty smile, already imagining your next encounter."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Don't you want to finish too? I had a great time, it's only fair..."
            mc.name "Maybe next time. Watching you cum is all I really wanted."
            the_person "Well, it was amazing. Ah..."
            "She gives you a dopey smile, still riding the chemical high of her orgasm."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] looks away, embarrassed by what she's done with you."
            the_person "Is that it? Did you really just want to make me... climax?"
            mc.name "Yeah, that's all for now. You look really cute when you cum, did you know that?"
            "She blushes more intensely, still avoiding making eye contact."
            the_person "Thanks, I guess... Can we talk about something else now?"

        else: # She's surprised she even tried that.
            the_person "Oh my god, that was intense! I... don't think we should have done that though."
            mc.name "Why not? Obviously you enjoyed yourself."
            the_person "Yeah, but it's wrong, isn't it? Whatever, it's happened now..."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "I hope that was everything you wanted it to be [the_person.mc_title]."
            the_person "But I think we could take it a little further next time, if you want. I can think of a bunch of fun things for us to try."
            the_person "Just something for you to keep in mind, okay?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "All done then, huh?"
            "She seems a little disappointed, but is trying to hide it."
            the_person "Maybe, uh... You could make me cum too next time?"
            mc.name "Yeah, sure thing [the_person.title]."

        elif used_obedience: #She only did it because she was commanded
            the_person "We're done then?"
            "[the_person.possessive_title!c] avoids making eye contact with you, obviously embarrassed."
            mc.name "Yeah, we're all done for now. Thanks [the_person.title], that felt great."
            the_person "I... Good, I'm glad you liked it."

        else:  # She's surprised she even tried that.
            the_person "We're done? I mean, I hope that felt good for you."
            "She laughs nervously, trying to hide her embarrassment."
            the_person "I think we took things a little too far, though. It got kind of crazy, huh?"
            the_person "Whatever, let's just talk about something else..."

    elif the_person.energy < 10: #Nobody came and she's tired
        the_person "I'm really sorry, [the_person.mc_title], but I'm too tired."
        mc.name "Don't worry [the_person.fname], we had a good time."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Done already? But we just barely started!"
            the_person "Well... I guess you'll have to make it up to me later, okay?"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "You're tired out already? Aww, but I was just starting to have fun!"
            "[the_person.possessive_title!c] seems a little disappointed."

        elif used_obedience: #She only did it because she was commanded
            the_person "You're done? But you didn't... climax."
            "She looks away, suddenly embarrassed."
            the_person "Never mind, it doesn't matter. Let's just talk about something else, this is getting awkward."

        else:  # She's surprised she even tried that.
            the_person "Oh my god, you're totally right. I don't know what I was thinking, agreeing to that..."
            "She laughs nervously, trying to hide her embarrassment."
            the_person "Let's not tell [mom.fname] about this, obviously."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        if home_harem():            
            if the_person.has_child_with_mc:
                $ random_reply = get_random_from_list(["how am I going to explain it to " + mom.fname + ", again?", "hope " + mom.fname + " okay with another grandchild if this stick."])
            else:
                $ random_reply = get_random_from_list(["She will be mad once it starts showing.", "do you think " + mom.fname + " will be jealous if I'm pregnant from this?"])
            #the_person "Oh [the_person.mc_title], [random_reply]"
        else:
            if the_person.has_child_with_mc :
                $ random_reply = get_random_from_list(["hope you earned enough dough for more child suppport.", "you are lucky because I'm the one getting berated for this", "I give up, it's definitely your fetish in getting your own sister pregnant.", "Do you have a fetish with getting your sister pregnant over and over?"])
            else:
                $ random_reply = get_random_from_list(["you have to tell " + mom.fname + " when I get pregnant.", "will we be okay? What about " + mom.fname + "?", "Can I take pregnancy leave from school? ", "who gonna tell " + mom.fname + "?"])
        the_person "Hmm [the_person.mc_title], [random_reply!i]"

    
    return

label lily_condom_demand_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        the_person "STOP! STOP! STOP! Really?"
        the_person "You've planned this, isn't it? That's why you've prepared!"
    else:
        if the_person.wants_creampie:
            the_person "Uurghhh... It sucks, but [the_person.mc_title]..."
            the_person "You need to put on a condom first."
            the_person "You have one on you, right?"
        else:
            the_person "Wait! Wait! Time out! [the_person.mc_title], Condom! Condom!"
            the_person "Come on, [the_person.possessive_title] might have second thoughts if you make her wait too long."
    return

label lily_condom_ask_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        "[the_person.title] shakes her head hopelessly."
        the_person "I know its's useless to talk you out of this, but condom, maybe?"
    else:
        if the_person.on_birth_control:
            the_person "I'm taking the pill, but you should probably still wear a condom. Right?"
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            # the_person "If you want to cum inside me you should put on a condom."
            # the_person "I know it's less fun than fucking raw, but it's still better than pulling out, right?"
            the_person "Put on a condom, then you don't need to worry about cumming inside me."
            $ the_person.discover_opinion("creampies")
        else:
            the_person "Condom check! It would be really bad if you... finished inside your own sister."
            the_person "That's the smart thing to do, right?"
    return

label lily_condom_bareback_ask_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        "[the_person.title] looks straight at you."
        the_person "I don't like that look you giving me..."
    else:
        if the_person.wants_creampie:
            if the_person.on_birth_control:
                the_person "I'm on the pill, so don't worry about protection."
                the_person "You can even cum in me, if you want. That would be so hot."
                $ the_person.update_birth_control_knowledge()
            else:
                if the_person.has_child_with_mc:
                    the_person "Let's go bareback again!"
                    the_person "You can even cum inside me, if you want. Worse case, I get pregnant again with your kid."
                else:
                    the_person "Don't worry about protection, I don't care about that any more."
                the_person "You can even cum in me, if you want. Might get me pregnant tho. Hehe."
            $ the_person.discover_opinion("creampies")
        else:
            the_person "Don't worry about protection, I don't care about that any more."
            the_person "Take me raw, it feels so much better!"
    return

label lily_condom_bareback_demand_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        "[the_person.title] looks straight at you."
        the_person "I recognized that look you giving me..."
    else:
        if the_person.has_breeding_fetish: #Actively looking to get knocked up.
            if the_person.knows_pregnant:
                the_person "We don't need that [the_person.mc_title], I'm already pregnant."
                the_person "So just come and do it already! Fuck me, Big Bro!"
            else:
                the_person "Screw condom, your sister want to get pregnant."
                the_person "So be a good Big Brother and knock me up!"
        elif the_person.on_birth_control:
            the_person "Forget it [the_person.mc_title], I'm on the pill."
            the_person "Fuck your sister already!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Raw baby, Raw! You're going to fuck me raw today!"
            the_person "Come on, hurry up and put it inside me!"
    return

label lily_vaginal_sex_taboo_break_revamp(the_person):
    if the_person.event_triggers_dict.get("vaginal_revisit_count", 0) == 0:
        if vt_enabled():
            if the_person.vaginal_virgin == 0:
                if the_person.love > 60:
                    the_person "This is so crazy! We should really stop, we've taken this too far..."
                    if the_person.has_taboo("kissing"):
                        mc.name "[the_person.title], stop. You love me, right?"
                    else:
                        if the_person.has_taboo("sucking_cock"):
                            mc.name "Was it too far when we kissed? I liked doing that a lot."
                            the_person "I did too, but that was different. We were just experimenting. Right?"
                            mc.name "That's what we told ourselves, but I think we both knew it meant more. Do you love me?"
                        else:
                            mc.name "Was it too far when we kissed? What about when you sucked my cock?"
                            the_person "That was... Maybe that was a mistake."
                            mc.name "I don't think it was. I think we've been lying to ourselves."
                            the_person "What do you mean?"
                            mc.name "Do you love me?"
                    the_person "You're my brother, of course I love you, but..."
                    mc.name "\"But\" nothing. I love you too and want to share that with you."
                    the_person "I've never did it before... with anyone."
                    mc.name "So, you haven't lost your virginity yet?"
                    "She is quiet for a long moment, then nods uncertainly."
                    mc.name "I'll go slow, it may be painful at first, but I promised it will feel real good very quickly."
                else:
                    the_person "I can't believe we are really doing this... Is it wrong? Should we stop?"
                    mc.name "What do you think? Do you want to stop?"
                    "She bites her lip and shakes her head."
                    the_person "No. I want to see what it feels like. It's my first time, and it's going to be my own brother."
                    mc.name "You are still a virgin?"
                    the_person "Stop teasing me [the_person.mc_title]! I want to feel your... cock inside me."
                    mc.name "I'll go slow, it may be painful at first, but I promised it will feel real good very quickly."
                $ take_virginity(the_person)
            else: #Not virgin
                if the_person.love > 60:
                    the_person "This is so crazy! We should really stop, we've taken this too far..."
                    if the_person.has_taboo("kissing"):
                        mc.name "[the_person.title], stop. You love me, right?"
                    else:
                        if the_person.has_taboo("sucking_cock"):
                            mc.name "Was it too far when we kissed? I liked doing that a lot."
                            the_person "I did too, but that was different. We were just experimenting. Right?"
                            mc.name "That's what we told ourselves, but I think we both knew it meant more. Do you love me?"
                        else:
                            mc.name "Was it too far when we kissed? What about when you sucked my cock?"
                            the_person "That was... Maybe that was a mistake."
                            mc.name "I don't think it was. I think we've been lying to ourselves."
                            the_person "What do you mean?"
                            mc.name "Do you love me?"
                    the_person "You're my brother, of course I love you, but..."
                    mc.name "\"But\" nothing. I love you too and want to share that with you."
                    "She is quiet for a long moment, then nods uncertainly."
                    the_person "Okay... We can do this, but we can't let anyone know! And we aren't, like, a couple, okay?"
                    the_person "You're still my brother, we just... Do other things together. Understand?"
                    mc.name "Sure thing sis."
                else:
                    the_person "I can't believe we are really doing this... Is it wrong? Should we stop?"
                    mc.name "What do you think? Do you want to stop?"
                    "She bites her lip and shakes her head."
                    the_person "No. I want to see what it feels like."
                    mc.name "What do you want to feel?"
                    the_person "Stop teasing me [the_person.mc_title]! I want to feel your... cock inside me."
                    mc.name "That's a good girl. Well, let's give it a try!"
        else: #No VT
            if the_person.love > 60:
                the_person "This is so crazy! We should really stop, we've taken this too far..."
                if the_person.has_taboo("kissing"):
                    mc.name "[the_person.title], stop. You love me, right?"
                else:
                    if the_person.has_taboo("sucking_cock"):
                        mc.name "Was it too far when we kissed? I liked doing that a lot."
                        the_person "I did too, but that was different. We were just experimenting. Right?"
                        mc.name "That's what we told ourselves, but I think we both knew it meant more. Do you love me?"
                    else:
                        mc.name "Was it too far when we kissed? What about when you sucked my cock?"
                        the_person "That was... Maybe that was a mistake."
                        mc.name "I don't think it was. I think we've been lying to ourselves."
                        the_person "What do you mean?"
                        mc.name "Do you love me?"
                the_person "You're my brother, of course I love you, but..."
                mc.name "\"But\" nothing. I love you too and want to share that with you."
                "She is quiet for a long moment, then nods uncertainly."
                the_person "Okay... We can do this, but we can't let anyone know! And we aren't, like, a couple, okay?"
                the_person "You're still my brother, we just... Do other things together. Understand?"
                mc.name "Sure thing sis."
            else:
                the_person "I can't believe we are really doing this... Is it wrong? Should we stop?"
                mc.name "What do you think? Do you want to stop?"
                "She bites her lip and shakes her head."
                the_person "No. I want to see what it feels like."
                mc.name "What do you want to feel?"
                the_person "Stop teasing me [the_person.mc_title]! I want to feel your... cock inside me."
                mc.name "That's a good girl. Well, let's give it a try!"
    else: #Not 1st time
        the_person "We should stop... Fuck, I don't know what to do [the_person.mc_title]!"
        mc.name "Just stop worrying. Your body knows what it wants."
        the_person "You're my brother..."
        mc.name "That didn't stop us last time, and we both had a pretty good time."
        mc.name "You want it, right?"
        "She hesitates for a long moment, then nods meekly."
        mc.name "You're such a slut [the_person.title]. You're really going to let your brother fuck you?"
        the_person "Oh shut up and just do it already!"
    return
