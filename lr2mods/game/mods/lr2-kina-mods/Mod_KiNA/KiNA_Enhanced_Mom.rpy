#Counter = KEM01

#revamped dialogue for mom, but I still hope I keep her shyness/awkwardness toward everything slutty

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["mom_greetings"] = "mom_greetings_revamp"
    config.label_overrides["mom_sex_accept"] = "mom_sex_accept_revamp"
    config.label_overrides["mom_sex_review"] = "mom_sex_review_revamp"
    config.label_overrides["mom_flirt_response_high"] = "mom_flirt_response_high_revamp"
    config.label_overrides["mom_vaginal_sex_taboo_break"] = "mom_vaginal_sex_taboo_break_revamp"
    config.label_overrides["mom_cum_pullout"] = "mom_cum_pullout_revamp"
    config.label_overrides["mom_cum_vagina"] = "mom_cum_pullout_revamp"
    config.label_overrides["mom_condom_demand"] = "mom_condom_demand_revamp"
    config.label_overrides["mom_condom_ask"] = "mom_condom_ask_revamp"
    config.label_overrides["mom_condom_bareback_ask"] = "mom_condom_bareback_ask_revamp"
    config.label_overrides["mom_condom_bareback_demand"] = "mom_condom_bareback_demand_revamp"
    
label mom_greetings_revamp(the_person):
    if the_person.happiness > 140: #Very Happy
        #if (the_person.has_event_day("last_birth") and the_person.days_since_event("last_birth") < 21) and renpy.random.randint(0, 2) == 2: #roughly 33%
        if (the_person.has_event_day("last_birth") and (the_person.days_since_event("last_birth") < 21 ) and (time_of_day in (0, 4))) and renpy.random.randint(0, 2) == 2: #roughly 33% .. She's given birth and lactating
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
                the_person "So perfect. Just like you were."
                mc.name "Yeah..."
                mc.name "She is."
            elif event == 1:
                $ the_person.draw_person(position = "sitting")
                "[the_person.possessive_title!c] sat on the bed as she cradled the tiny bundle in her arms."
                "Your newborn baby cooed softly, tiny fingers curling around her thumb."
                "The noise you made make [the_person.possessive_title] looked up, smiling warmly as you approached."
                "She patted the bed beside her, the invitation clear."
                the_person "Here..."
                "She said softly, holding the baby out to me. "
                the_person "Hold her."
                "You hesitated for a moment before taking the baby from her arms."
                "The tiny bundle was warm and fragile, and you felt a surge of protectiveness as you cradled her close."
                "[the_person.possessive_title!c] watched you with a soft smile, her eyes filled with love."
                the_person "You’re a natural...Just like I knew you would be."
            else:
                "You find the baby laying on the bed, letting out a soft cry."
                $ the_person.draw_person(position = "back_peek")
                if time_of_day == 0:
                    the_person "Good morning, sweetheart."
                else:
                    the_person "Is that you, [the_person.mc_title]?"
                the_person "Would you be a dear and check on her?"
                mc.name "Sure. No problem."
                "You lovingly picked the baby up and attempt to sooth her."
                "As expected, she have wetted herself. You expectly change her diaper and sure enough, the crying stopped and she cooed at your teasing."
                "Her little fingers tries to grab your face as you bring her closer."                
                $ the_person.draw_person(position = "stand3")
                "[the_person.possessive_title!c] watched you play with the baby, her eyes filled with love."
                the_person "You’re a natural...Just like I knew you would be."
            
        elif the_person.is_pregnant and ( day < the_person.event_triggers_dict.get("preg_transform_day", -1) ) and (time_of_day == 0 or time_of_day == 1) and renpy.random.randint(0, 2) == 2: #roughly 33%
            #Dont want to be obnoxious much
            the_person "Good morning, sweetheart."
            "But as she spoke, her expression suddenly changed, a hand flying to her mouth as her face paled."
            if mc.is_at(home_hub):
                "Without a word, she rushed past you and disappeared into the bathroom, the sound of retching echoing through the house."
            elif mc.is_at(office_hub):                
                "Without a word, she rushed past you and disappeared into the restroom, the sound of retching echoing through the office."
            if the_person.knows_pregnant:
                if the_person.is_mc_father:
                    if mc.is_at(home_hub):
                        $ mc.change_location(home_shower)
                    elif mc.is_at(office_hub): 
                        $ mc.change_location(work_bathroom) 
                    "You followed her through the bathroom door, gently massaging her back while she still leaning over the sink."
                    the_person "Thanks [the_person.mc_title], I'm okay now."
                    "She managed to say, though her voice wavered."
                    the_person "Just a bit of morning sickness, that's all."
                    the_person "I'm fine now, honey."
                    "She gives you a loving smile."
                    if mc.is_at(home_hub):
                        the_person "Let’s go back to my room."
                        $ mc.change_location(mom_bedroom)
                    elif mc.is_at(office_hub): 
                        the_person "Let’s go back to your office."
                        $ mc.change_location(ceo_office)
                else:
                    #Dont care much tbh 
                    "She probably having her bout of morning sickness. You took a sit on her bed waiting."
                    "Few minutes later, she's back."
                    the_person "Sorry honey... You know how it is. It probably go away in few weeks."
                    
            else:
                #wincest?
                "Confused, you stood there for a moment, unsure of what to do."
                if the_person.has_child_with_mc:
                    "Then it dawned upon yourself. Seems like you've managed to get your own mother pregnant again."
                else:
                    "You had never seen [the_person.possessive_title] like this before."
                "Still concerned, you followed her to the bathroom door, hesitating before knocking softly."
                if mc.is_at(home_hub):
                    $ mc.change_location(home_shower)
                elif mc.is_at(office_hub): 
                    $ mc.change_location(work_bathroom) 
                mc.name "[the_person.title] ? Are you okay?"
                "Inside, she was leaning over the sink, her breathing ragged. She looked up at her reflection in the mirror, her eyes dull with discomfort."
                the_person "I {i}think{/i} I need to drop at the pharmacy after work to buy a test kit."
                if mc.is_at(home_hub):
                    the_person "Let’s go back to my room."
                    $ mc.change_location(mom_bedroom)
                elif mc.is_at(office_hub): 
                    the_person "Let’s go back to your office."
                    $ mc.change_location(ceo_office)

        elif the_person.sluttiness > 80 and renpy.random.randint(0, 1) == 1: #she's a total slut now but we want some love dialogues as well.
            if the_person.arousal_perc > 50: #she's quite aroused
                $ random_greeting = get_random_from_list(["Hello ", "Hi", "Hey"])
                $ random_lines = get_random_from_list(["are you free right now? I could use a bit of ... urm... {i}help{/i}.", "sorry, I'm a bit occupied right now... Unless you willing to help.", "it's a bit {i}hot{/i} over here right now, isn't it?"])
                $ random_act = get_random_from_list(["blushes and quickly looks away from you.", "takes a deep breath.", "bites her lip and looks at the floor, avoiding your eye contact while she speaks softly.", "looks flustered."])
                the_person "[random_greeting] [the_person.mc_title]. [random_lines]"
                "[the_person.possessive_title!c] [random_act]"
            else: 
                if mc.location == kitchen:
                    $ random_greeting = get_random_from_list(["Hello ", "Hi"])
                    $ random_lines = get_random_from_list(["Know what's on the menu today? Me 'n u.", "Did you just come out of the oven? Because you're too hot to handle.", "What did the microwave said to the frozen pizza? I want {i}you{/i} inside of me.", "Dinner first, or can we go straight for dessert?"]) 
                    the_person "[random_greeting] [the_person.mc_title]. [random_lines]"
                    mc.name "That is so corny [the_person.title]."
                elif time_of_day == 4:
                    $ random_greeting = get_random_from_list(["Hello ", "Hi"])
                    $ random_lines = get_random_from_list(["Aren't you tired? From running through my mind all day?", "If you let me borrow a kiss, I promise I'll give it right back.", "My bed, your bed, we should have our bed, don't you think?", "Mommy's ready for {i}anything{/i}. Just tell me."]) 
                    the_person "[random_greeting] [the_person.mc_title]. [random_lines]"
                    mc.name "That is so corny [the_person.title]."
                else:
                    $ random_greeting = get_random_from_list(["Hello ", "Hi"])
                    $ random_lines = get_random_from_list(["Is there anything your mother can take care of for you? {i}Anything{/i}?", "I was... well, I was just {i}thinking{/i} about you, how has your day been?", "Mommy's ready for {i}anything{/i}. Just tell me."]) 
                    the_person "[random_greeting] [the_person.mc_title]. [random_lines]"
                    mc.name "That is so sweet [the_person.title]. I love you too."           
        elif the_person.love > 40: #She loves you 
            if time_of_day == 0 or time_of_day == 1:
                if mc.is_at(home_hub):
                    $ random_lines = get_random_from_list(["Breakfast will be ready soon!", "Will you be having dinner with us this evening?", "Your toasts are ready, eat it while it still hot.", "I can’t focus today. I don't know why."])
                elif mc.is_at(office_hub):
                    $ random_lines = get_random_from_list(["Did you breakfast? I have a pack if you want!", "Did Lily have her breakfast? She overslept this morning.", "Here's a cup of coffee, drink it while it hot. I saw you yawning just now.", "I can’t focus today. I don't know why."])
                the_person "Good morning, [the_person.mc_title]. [random_lines]"
            elif time_of_day == 1 or time_of_day == 2:
                $ random_lines = get_random_from_list(["Will you be having dinner at home this evening?", "I was thinking of just ordering pizza for dinner tonight, would it be fine?", "Would you mind buying some grocery after work for me?"]) 
                the_person "Good afternoon, [the_person.mc_title]. [random_lines]"
            elif time_of_day == 3 and mc.location == kitchen:
                $ random_lines = get_random_from_list(["Dinner will be ready soon!", "Almost done, it's your favourite dish.", "Thanks for the grocery pickup. You are such a life saver.", "Can you call your sister? I'm about to serve dinner."]) 
                the_person "Good evening, [the_person.mc_title]. [random_lines]"
            else:
                $ random_lines = get_random_from_list(["How is your day?", "You are working so hard. It's fine to take some time off.", "If there's anything I can help with, do let me know, okay?", "Thanks for the grocery pickup. You are such a life saver."]) 
                the_person "Good evening, [the_person.mc_title]. [random_lines]"
        else:
            the_person "Hello [the_person.mc_title]. I hope everything is going well, if there's anything I can help with let me know."
    else:
        if the_person.love > 40: #She loves you enough... but is sad.
            if time_of_day == 0 or time_of_day == 1:
                $ random_lines = get_random_from_list(["Can you heat up last night's pizza for breakfast? I don't feel like making anything today.", "Will you be having dinner at home this evening? Take away dinner, I need some me time on my own."]) 
                the_person "Morning, [the_person.mc_title]. [random_lines]"
            elif time_of_day == 1 or time_of_day == 2:
                $ random_lines = get_random_from_list(["Can you order take away for dinner later?", "I was thinking of just ordering pizza for dinner tonight, would it be fine?", "Would you mind buying some grocery after work for me?"]) 
                the_person "Afternoon, [the_person.mc_title]. [random_lines]"
            elif time_of_day == 3 and the_person._location == the_person._home:
                $ random_lines = get_random_from_list(["Dinner in the microwave.", "Can you setup the table? I'm a bit tired today.", "Almost done, can you setup the table?", "Thanks for the grocery pickup."]) 
                the_person "Evening, [the_person.mc_title]. [random_lines]"
            else:
                the_person "Evening, [the_person.mc_title]!"            
        elif the_person.sluttiness > 60:
            $ random_greeting = get_random_from_list(["Hello ", "Hi", "Hey"])
            $ random_lines = get_random_from_list(["Is there anything your mother can take care of for you?", "I was... well, I was just {i}thinking{/i} about you, how has your day been?", "I think about you a little more than I should.", "I can’t focus today. I’m too distracted thinking about you."]) 
            the_person "[random_greeting] [the_person.mc_title]. [random_lines]"
        else:
            if time_of_day == 0 or time_of_day == 1:
                the_person "Good morning, [the_person.mc_title]!"
            elif time_of_day == 1 or time_of_day == 2:
                the_person "Good afternoon, [the_person.mc_title]!"
            else:
                the_person "Good evening, [the_person.mc_title]!"
                
    return

label mom_sex_accept_revamp(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            $ random_reply = get_random_from_list(["This can't be wrong... not if I get so turned on by it, right?", "No one will know, right?", "I can't believe I'm doing this!"])
            the_person "[random_reply]"  
        else:
            if the_position.skill_tag == "Foreplay":
                if "giving tit fucks" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list([" You love Mommy's boobs?, aren't you?", "Lemme smoother you with these.", "Oh my, these juggers?", "Boob sandwich, coming up!", "I'll make you cum with these~"])
                elif "kissing" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Mmmm, kiss me  " + the_person.mc_title + ".", "Come kiss your mommy!", "I'm yours.", "Always the romantic.", "French kiss~"])
                else:
                    $ random_reply = get_random_from_list(["Okay, lets play a little with each other.",  "Come play with mommy's pussy.", "Mmmm, come here!", "Mmmmm...", "I want to taste me on your fingers."])
                the_person "[random_reply]"
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Oh yes, come here and take care of mommy.", "Such a good son.", "Oh my, such a gentleman.", "Tease me until I'm begging for it.", "Lick me mmmore..."])
                else:
                    $ random_reply = get_random_from_list(["Come here, let mommy take care of her big boy.", "Mommy gonna clean you... {i}thoroughly.{/i}", "Oh my, so healthy, so big.", "Arousing you arouses me.", "I'll taste you, my son.", "Yours definitely bigger then your dad."])
                the_person "[random_reply]"
            else:
                if not mom_knows_about_lily() or not (the_person._location == the_person._home): # mod only
                    $ random_reply = get_random_from_list(["Oh yes baby, come here and fuck mommy's brains out.", "Let’s misbehave~", "Give Mommy your hot stuff!", "Mess me up!! Make me cum!", "Put it in.. Give it to me!", "Mmmm, I want it! I want your cock, " + the_person.mc_title + "!", "Make your mother your woman!", "Just fill me and make me feel like a true woman again!"])
                else:
                    $ random_reply = get_random_from_list(["Do you think " + [lily.fname] + "can make you feel like this?", "Now, let me show you what it means to be fucked by a woman who knows exactly what you need.", "Push me up against a wall and do dirty things to " + the_person.possessive_title + ".", "My indecent body... is yours, " + the_person.mc_title + "!", "I can hardly control myself either..."])
                the_person "[random_reply!i]"
    else:
        if the_person.love < 40:
            the_person "Okay, lets try it. I just hope this brings us closer together as mother and son."
        else:
            if the_position.skill_tag == "Foreplay":
                if "giving tit fucks" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["You love these, aren't you?", "Lemme smoother you with these.", "Sandwich your dick like this?"])
                    the_person "[random_reply]"
                elif "kissing" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Mmmm, kiss me baby.", "Come kiss your mommy!", "I'm yours."])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["Whatever you want me to do, " + the_person.mc_title + ". I just want to make sure you're happy.", "Play with mommy.", "I'm yours."])
                    the_person "[random_reply]"
            elif the_position.skill_tag == "Oral":
                $ random_reply = get_random_from_list(["Okay, lets try it. I just hope this brings us closer together.", "Come play with mommy.", "I don't mind giving it another try.", "I'm yours."])
                the_person "[random_reply]"
            else:
                if the_person.has_taboo(["vaginal_sex", "anal_sex"]):
                    $ random_reply = get_random_from_list(["Oh my, I don't know why I let you talk me into this.", "Promise me. Just this once, okay?", "Put it in.. Give it to me!"])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["I don't mind giving it another try.", "Oh my, I don't know why I let you talk me into this.", "Okay, lets try it. I just hope this brings us closer together."])
                    the_person "[random_reply]"
    return

label mom_sex_review_revamp(the_person, the_report):
    $ comment_position = the_person.pick_position_comment(the_report)
    if comment_position is None:
        return #You didn't actually do anything, no need to comment.

    $ used_obedience = the_report.get("obedience_used", False) #True if a girl only tried a position because you ordered her to.
    $ the_person.draw_person()  # make sure she stands up for talking with you

    #She's worried about her SO finding out because it was in public
    if the_report.get("was_public", False) and (the_person.effective_sluttiness()+10*the_person.opinion.public_sex < comment_position.slut_cap):
        if used_obedience:
            the_person "Oh, why did I let you do that here... People are watching [the_person.mc_title], someone might recognise me!"
            mc.name "It's fine [the_person.title], I don't think anyone knows who we are."
            "[the_person.possessive_title!c] seems unconvinced, but she doesn't say anything more."

        else:
            the_person "Oh [the_person.mc_title], what was I thinking... People are watching, someone might recognise me!"
            mc.name "It's fine [the_person.title], I don't think anyone knows who we are."
            "[the_person.possessive_title!c] seems unconvinced, but she doesn't say anything more."

    # special condition - you fucked her brains out
    elif the_report.get("girl orgasms", 0) > 5 and the_report.get("guy orgasms", 0) > 2:
        if used_obedience:
            $ random_line1 = get_random_from_list(["Huff... Huff", "Oh my God", "Thish ish jhust too ghood", "Ah jeez"])
            $ random_line2 = get_random_from_list(["Gimme a sec...", "So much cum, no, I might cum again.", "You chame sho muuch...", "So much cum..."])
            the_person "[random_line1]... [random_line2]"
            the_person "Satisfied now, [the_person.mc_title]?"
            mc.name "Yeah, it's pretty satisfying to see you enjoying it too. Maybe far more then me."
            "[the_person.possessive_title!c] blushes and looks away from you."
            $ random_line1 = get_random_from_list(["I won't ask you who you learned that from.", "I forgive you.", "but that isn't issue here."])
            the_person "It was... amazing. You're so good, [random_line1]"
        else:
            $ random_line1 = get_random_from_list(["Huff... Huff", "Oh my God", "Ah jeez", "Thish ish jhust too ghood"])
            $ random_line2 = get_random_from_list(["Gimme a sec...", "You mesh me up sho much", "You chame sho muuch...", "So much cum..."])
            the_person "[random_line1]... [random_line2]"
            "You just hugged her and give her forehead a kiss."
            $ random_reply = get_random_from_list(["I'll be craving for your dick every day if this continues.", "I could get addicted to this.","My only regret right now is we didn't do it sooner.", "I'm addicted to my own son's dick. Peoples be damned."])
            the_person "[random_reply]"
            "She stops herself and takes a deep breath."
            mc.name "I'll be here for you, [the_person.title]."            
    elif the_report.get("girl orgasms", 0) > 2:
        if used_obedience:
            the_person "Are you feeling satisfied now [the_person.mc_title]?"
            mc.name "Yeah, that was great [the_person.title]. I know you enjoyed it too?"
            "[the_person.possessive_title!c] blushes and looks away from you."
            the_person "It was... amazing. You're so good, I won't ask you who you learned that from."
        else:
            $ random_reply = get_random_from_list(["Oh my... I'm sorry, sweetheart, I shouldn't have let myself go like that.", "Oh dear me... Your mother shouldn't behave like that. Sorry."])
            the_person "[random_reply]"
            $ random_reply = get_random_from_list(["I just stopped thinking straight after my second orgasm! I...", "I just wanted you to continue {i}forever{/i}...","I'm so un{i}lady{/i}like right now.", "I just stopped thinking straight and wanted more!"])
            the_person "I don't know what came over me, [random_reply]"
            "She stops herself and takes a deep breath."
            $ random_reply = get_random_from_list(["I really enjoyed our time together.", "it just show that we love each other.", "I love this side of you too."])
            mc.name "Don't worry [the_person.title], [random_reply]"

            call sex_review_trance(the_person) from _call_sex_review_trance_mom_sex_review_KEM01
            
    # special condition abort due to lack of girl energy without orgasm
    elif the_report.get("girl orgasms", 0) == 0 and the_person.energy < 20:
        the_person "I'm sorry, [the_person.mc_title] but I'm totally spent. We can talk about this another time."
        mc.name "No problem [the_person.title], we had fun, right?"
        the_person "Yes, baby we did!"

    #No special conditions, just respond based on how orgasmed and how slutty the position was.
    elif the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #You both came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position cap, it was tame
            the_person "Did you have a good time sweetheart? That was some fun exercise."
            $ random_reply = get_random_from_list(["We could even... go a little further, next time.", "Maybe something wilder? ... Oh! ", "I'm willing to go a little further, next time. "])
            $ random_extend = get_random_from_list(["Only if you're comfortable with that, of course!", "I think that could be even better."])
            the_person  "[random_reply] [random_extend]"

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            $ random_reply = get_random_from_list(["That was nice.", "I know I am.", "It's {i}so{/i} satisfying for me."])
            the_person "I hope you're feeling satisfied sweetheart. [random_reply]"
            "She gives you a warm, loving smile."

        elif used_obedience: #She only did it because she was commanded
            the_person "Are you feeling satisfied now sweetheart?"
            mc.name "Yeah, that was great [the_person.title]. Did you like it too?"
            "[the_person.possessive_title!c] blushes and looks away from you."
            the_person "It was... nice. You're very good at that, I'm not sure I want to know where you learned it."

        else: # She's surprised she even tried that.
            the_person "Oh my... I'm sorry, sweetheart, I shouldn't have let that get so serious."
            the_person "I don't know what came over me, I just stopped thinking straight and wanted more! I..."
            "She stops herself and takes a deep breath."
            $ random_reply = get_random_from_list(["I think I'm going to need a moment to catch my breath.", "Wow... I think I need a sec.", "We shouldn't have done that... But it felt really good."])
            the_person "[random_reply]"

    elif the_report.get("girl orgasms", 0) > 0: #Only she came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "All done? Well, it's very kind of you making sure your partner finishes even if you don't."
            the_person "I didn't realise I raised such a gentleman, but I'm glad I did!"
            the_person "I'll have to give you some sort of reward. I'm sure I'll think of something for next time."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Thank you for being so considerate and making sure I finished even though you're tired."
            the_person "It felt wonderful, and I'll try and make it up to you some other way, okay?"

        elif used_obedience: #She only did it because she was commanded
            the_person "We're done? I thought you would want to finish too."
            mc.name "Maybe some other time, but I wanted to make sure you were taken care of first."
            "[the_person.possessive_title!c] blushes and looks away from you."
            the_person "Oh [the_person.mc_title], I didn't realise you were being thoughtful, not selfish. I feel a little silly now..."
            the_person "It felt amazing. Thank you."

        else: # She's surprised she even tried that.
            the_person "Oh, that's all? I mean, you're right... we should stop. We've taken this too far already."
            the_person "It felt wonderful, but I should have stopped you earlier."
            the_person "I think I need to catch my breath after that. Ah..."

    elif the_report.get("guy orgasms", 0) > 0: #Only you came
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "How was that sweetheart, was it everything you wanted it to be?"
            mc.name "Yeah, that was great [the_person.title]."
            the_person "Good, that's what I like to hear. Next time we can go even further, if you'd like."
            the_person "Anything to make my special man happy."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "How was that sweetheart, did you have a good time?"
            mc.name "Yeah, that was great [the_person.title]."
            "She smiles warmly."
            the_person "Good, that's what I like to hear. I love making you happy."

        elif used_obedience: #She only did it because she was commanded
            "[the_person.possessive_title!c] sighs, obviously relieved that you're finished."

        else:  # She's surprised she even tried that.
            the_person "I hope you enjoyed yourself [the_person.mc_title]."
            mc.name "Yeah, that was great [the_person.title]."
            the_person "Good, but... we shouldn't take things so far in the future, okay?"
            the_person "It's my fault, really. I should be the more responsible of the two of us."

    else: #Nobody came.
        if the_person.effective_sluttiness() > comment_position.slut_cap: #She's sluttier than the position
            the_person "Are you tired out already [the_person.mc_title]?"
            the_person "Next time you should just let me take care of you, okay? I'll do everything for my special man."

        elif the_person.effective_sluttiness() > comment_position.slut_requirement: #She thought it was fun/exciting
            the_person "Tired out already? Oh, well that's okay [the_person.mc_title], you have a busy life."
            the_person "Next time we'll take it slower, and I'll spend a little more time focused on you."

        elif used_obedience: #She only did it because she was commanded
            the_person "Tired out? Well, that's okay [the_person.mc_title]."
            the_person "We shouldn't be doing this anyways, so it's probably for the best."
            "[the_person.possessive_title!c] seems relieved that you're stopping."

        else:  # She's surprised she even tried that.
            the_person "Oh what am I thinking! Of course we should stop, this has gone too far already."
            the_person "I'm sorry [the_person.mc_title], it's my job to be the responsible one and set boundaries."
            # the_person "You're right, we should probably stop. I just go so carried away, I wouldn't normally do something like this..."
            # "She laughs nervously, trying to hide her embarrassment."

    # Gave creampie while she is not on birth control (extra dialogue when she could get pregnant)
    if the_report.get("creampies", 0) > 0 and not the_person.on_birth_control and not the_person.knows_pregnant:
        if home_harem(): #the_person.event_triggers_dict.get("mom_girlfriend_sister_knows", False):
            if the_person.has_child_with_mc :
                $ random_reply = get_random_from_list(["how am I going to explain it to your sister, again?", "what do we tell Lily if I'm pregnant again from this?"])
            else:
                $ random_reply = get_random_from_list(["how am I going to explain it to your sister if you get me pregnant?", "Lily will be full of questions if it starts showing.", "what do we tell Lily if I'm pregnant from this?"])
            #the_person "Oh [the_person.mc_title], [random_reply]"
        else:
            if the_person.has_child_with_mc :
                $ random_reply = get_random_from_list(["can we afford another mouth to feed if you get me pregnant again?", "will we {i}really{/i} be okay?", "can we afford me getting pregnant... again?", "Do you have a fetish with getting your mom pregnant over and over?"])
            else:
                $ random_reply = get_random_from_list(["can we afford another mouth to feed if you get me pregnant?", "will we be okay?", "can we afford me getting pregnant?"])
        the_person "Oh [the_person.mc_title], [random_reply]"

    $ del comment_position
    return

label mom_compliment_response(the_person):
    $ random_greet = get_random_from_list(["Hello " + the_person.fname + ".", "My favourite person in the world!", "Hey..."])
    $ random_com = get_random_from_list(["looking amazing", "gorgeous", "looking very pretty"])
    mc.name "[random_greet] How are you doing today? You're [random_com], that's for sure."
    if the_person.is_at_work:
        if (the_person.is_employee or the_person.is_strip_club_employee) and the_person.is_wearing_uniform:
            call reserved_flirt_response_employee_uniform_low(the_person) from _call_reserved_flirt_response_employee_uniform_low_compliment_response_KEM01
        elif the_person.has_job(prostitute_job):
            the_person "I'm good [the_person.mc_title], are you looking for something special today?"
        elif the_person.sluttiness > 50:
            $ random_reply = get_random_from_list(["look quite handsome yourself", "are not bad either", "look dashing as well"])
            the_person "I'm doing alright. And I must say, you [random_reply]."
        else:
            the_person "Please [the_person.mc_title], behave yourself. I'm doing fine."
    else:
        the_person "Well, thank you, [the_person.mc_title]. I'm doing quite alright."
    "You chat with [the_person.possessive_title] for a while carefully slipping in a compliment once in a while. She seems charmed by all the attention."
    $ del random_greet
    $ del random_com
    return

label mom_flirt_response_high_revamp(the_person):
    if mc.location.person_count == 1: #If you are alone she'll flirt with you
        if the_person.effective_sluttiness() > (25 - the_person.opinion.incest*5): # High sluttiness flirt
            if ((the_person.sex_record.get("Vaginal Sex", 0) > 20) or (the_person.sex_record.get("Anal Sex", 0) > 20)):
                the_person "Oh [the_person.mc_title], you naughty boy..."
                $ random_flirt = get_random_from_list(["Are you truly seducing your mother?", "I can see a tent down there.", "Why are you hard down there?"])
                the_person "[random_flirt]"
                mc.name "Can you blamed me? You are such a sexy lady... I can't help myself."
                the_person "Aww... I suppose I'm partly to blamed as well. Come here."
                $ mc.change_locked_clarity(5)
                "She opens her arms up and pulls you into a hug. After a quick squeeze she steps back to arms length and smiles, looking into your eyes."
                the_person "Let us just be man and woman together."
            else:
                the_person "Oh [the_person.mc_title], you know you shouldn't be saying things like that to me."
                the_person "You should be thinking about women your own age. Isn't there anyone else you think is pretty?"
                mc.name "You're the most beautiful woman I know, [the_person.title]. No matter how much I try I can't get you out of my head."
                the_person "Aww... I suppose I can't be too angry at you then. Come here."
                $ mc.change_locked_clarity(5)
                "She opens her arms up and pulls you into a hug. After a quick squeeze she steps back to arms length and smiles, looking into your eyes."
                the_person "No matter what you're always going to be my amazing little boy."
            menu:
                "Kiss her":
                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        "You lean in and kiss [the_person.possessive_title]. She does her best to kiss you back, but it's clear she's still adjusting."
                        $ the_person.break_taboo("kissing")
                    else:
                        "She leaned in, her lips brushing softly against yours in a kiss that was both tender and hungry."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KEM01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "And you'll always be my beautiful, loving mom."
                    "[the_person.possessive_title!c] smiles warmly and hugs you again. This time you let your hands slide down her back and rest them on her ass."
                    the_person "You shouldn't... Oh what's the harm. Go ahead, give it a squeeze."
                    $ mc.change_locked_clarity(10)
                    "You grab [the_person.possessive_title]'s ass and massage it gently. She sighs softly into your ear as you play with her."
                    the_person "Okay... That's enough for now. I don't want you getting too excited."
                    mc.name "Okay [the_person.title]."
                    $ play_spank_sound()
                    "You give her ass one last slap and leave it jiggling as you step back. She rolls her eyes."
                    the_person "Oh... Some days I don't know what I'm going to do with you."
        else: # Just high love flirt
            the_person "[the_person.mc_title], I'm your mother. That's not funny."
            mc.name "Oh come on [the_person.title], there's nobody else around. You don't have to be so uptight."
            the_person "It's not right though, you shouldn't be... looking at me like this."
            mc.name "You're an attractive woman and I'm a young man, it's just how my brain work. Just take it as a compliment."
            "She sighs and rolls her eyes."
            the_person "Okay, thank you. Just... Don't expect me to actually take anything off for you."
    else: #peoples around
        if the_person.effective_sluttiness() > (25 - the_person.opinion.incest*5): #She's slutty, but you need to find somewhere private so people don't find out.
            the_person "[the_person.mc_title], watch what you're saying! There are other people around."
            mc.name "It's fine [the_person.title], nobody else is listening."
            "She puts her hands on her hips and shakes her head severely."
            the_person "Do we need to go somewhere private to talk about your behaviour?"
            menu:
                "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                    mc.name "I think we should, we don't want to bother anyone else."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_mom_flirt_response_high_KEM01
                    the_person "I don't mind you joking around like that, but if there are other people around you should be more... discrete."
                    mc.name "I know [the_person.title], but you're so beautiful I just get carried away."
                    "Her stern glare soften. She sighs and smiles."
                    the_person "I can't be angry, you're just feeling the same way every young man does. Come here."
                    "She pulls you into a hug and kisses you on the cheek. You put your hands around her and move them down her back."
                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        "You lean in and kiss [the_person.possessive_title]. She does her best to kiss you back, but it's clear she's still adjusting."
                        $ the_person.break_taboo("kissing")
                    else:
                        the_person "Hey... What are you doing? We shouldn't..."
                        "You slide your hands onto her ass and rub it gently."
                        mc.name "Come on, just for a few minutes. I'm so horny right now..."
                        "You rub [the_person.possessive_title]'s butt while she thinks. Finally she sighs reluctantly and nods."
                        the_person "Only because you really need it."
                        "You lean forward and kiss her passionately. It takes her a few seconds to warm up, but soon she is kissing you back with just as much enthusiasm."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_KEM02
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_mom_flirt_response_high_KEM01

                "Just flirt":
                    mc.name "Relax, I'm just joking around. What I mean is you're looking stunning today."
                    the_person "Thank you, that's a much more appropriate way of saying it."
                    "Her eyes soften and she sighs."
                    the_person "I'm sorry, I didn't mean to be so tough on you. If we're alone you can joke around like that, but when there are other people around..."
                    the_person "I just don't want anyone to misunderstand our... relationship."
                    mc.name "I understand [the_person.title]. I'll be more careful."

        else: #She's not slutty, so she's embarrassed about what you're doing.
            "[the_person.possessive_title!c] gasps and covers her mouth."
            the_person "Oh my god, [the_person.mc_title]!"
            mc.name "Relax [the_person.title], I'm just joking around."
            "She shakes her head sternly."
            the_person "Well I don't find it very funny when other people are around. It's embarrassing."
            mc.name "I'm sorry, I'll wait until we're alone next time."
            the_person "I'm not even sure if you should be making comments like that to me alone, but... It's fine."
    return

label mom_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Such a gentleman."
    "She seductively smile after taking a sip."
    the_person "Now then, about this fucking my brains out..."
    "She sets her wine down on her nightstand."
    the_person "Don't dissapoint your mother~"
    return

label mom_vaginal_sex_taboo_break_revamp(the_person):
    #TODO: Add a "How do we tell your sister?" Event after this has been triggered.
    if the_person.event_triggers_dict.get("vaginal_revisit_count", 0) == 0:
        if the_person.love > 60:
            the_person "We should stop... If we do this there is no going back to the way things were."
            mc.name "I don't want to go back [the_person.title]. I want to be with you."
            the_person "I... I do too, but you shouldn't be taking your mother as your lover."
            mc.name "I want to be your lover, your son, your best friend, and your confidant."
            mc.name "I want to be your whole world, just like you're already mine."
            the_person "Aww... How did I raise such a romantic gentleman?"
            the_person "Okay, if you're ready then I'm ready. Take me [the_person.mc_title]!"
        else:
            the_person "I should stop you here... This is so wrong. Isn't it?"
            mc.name "I don't think there's anything wrong. Why do you?"
            the_person "My son has his cock out and I'm actually thinking about letting him have sex with me!"
            the_person "Isn't that crazy!? Did we both go insane?"
            mc.name "I'm not just your son though, am I? We've done so much together already, isn't this just natural?"
            the_person "Nothing about this is natural..."
            mc.name "Yeah it is. It's natural for a young, virile man to want to fuck a beautiful woman like you."
            mc.name "And it's natural for you, a beautiful woman, to want to get fucked by someone she loves and trusts."
            mc.name "You love me, don't you?"
            the_person "I do..."
            mc.name "Then there's no good reason to hold back our love. We need to follow our hearts and do what makes us happy."
            mc.name "[the_person.title], you make me happy."
            the_person "You make me happy too. Okay, if you're ready then I think I'm ready."
            the_person "Come and fuck your mother!"
    else:
        if vt_enabled():
            if the_person.vaginal_virgin == 0:
                if mom_virgin_before():
                    the_person "You are weird.."
                    mc.name "Excuse me?"
                    the_person "You are fucking your mother, but you keep making me a virgin."
                    mc.name "Are we seriously talking about this right now?"
                    "Another long pause, then she chuckles softly and starts aligning her pussy against your dick."
                    the_person "Just kidding, let's continue. "
                else:
                    $ mom.event_triggers_dict["virgin_mom"] = True
                    the_person "Wait, I'll bleed?"
                    mc.name "Like a virgin, yes."
                    the_person "But, we already fucked a couple of times."
                    mc.name "That's what the itchy serum do. They rebuild your hymen, so you can be virgin again."
                    the_person "Ah... so that what it do."
                    the_person "So, now I get lose my virginity to my own son."
                    the_person "That sounds weird... But, kinda sexy too."
                    "Another long pause, then she moans softly and nods."
                    the_person "Okay, you can have mom's virginity... It's not the original, but we can play pretend you are my first."
                $ take_virginity(the_person)
            else:
                the_person "We need to stop [the_person.mc_title]. We talked about this, this is too far!"
                mc.name "You don't want to stop here though, do you?"
                "She moans and shrugs."
                the_person "I don't know what I want... I want to be a good mother!"
                mc.name "Then let me fuck you [the_person.title]. That will make me the happiest boy in the world."
                "Another long pause, then she moans softly and nods."
                the_person "Okay, you can fuck me... Hurry up before I change my mind!"
        else:
            the_person "We need to stop [the_person.mc_title]. We talked about this, this is too far!"
            mc.name "You don't want to stop here though, do you?"
            "She moans and shrugs."
            the_person "I don't know what I want... I want to be a good mother!"
            mc.name "Then let me fuck you [the_person.title]. That will make me the happiest boy in the world."
            "Another long pause, then she moans softly and nods."
            the_person "Okay, you can fuck me... Hurry up before I change my mind!"
    return

label mom_cum_pullout_revamp(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "Do you want to take off that condom? You already got mommy pregnant..."

            elif the_person.on_birth_control:
                the_person "Do you... want to take the condom off, [the_person.mc_title]?"
                the_person "We can take the risk, just this once. You can put your big load right inside my pussy, raw!"
                "She moans happily, excited just by the thought."

            else:
                the_person "Ah... Do you want to take the condom off and cum inside me?"
                $ the_person.update_birth_control_knowledge()
                the_person "You can do it, okay? You can put your big load right into mommy's unprotected pussy!"
                "She moans happily, excited just by the thought."

            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                    $ use_condom = False  # prevent putting on a new condom next sex loop
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."
        else:
            the_person "Go ahead [the_person.mc_title]!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Cum for mommy [the_person.mc_title]!"
            elif the_person.opinion.creampies > 0:
                $ play_moan_sound()
                "[the_person.possessive_title!c] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Cum inside me [the_person.mc_title]! I want you to give me all of your cum!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    $ the_person.update_birth_control_knowledge()
                    the_person "Cum inside me [the_person.mc_title]! Cum in me and get mommy pregnant!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                the_person "You can cum wherever you want [the_person.mc_title], I'm ready!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Cum for mommy [the_person.mc_title]! Ah!"
        else:
            if the_person.knows_pregnant:
                the_person "Yes [the_person.mc_title], cum for me, spray it all over me!!"
            elif not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                $ the_person.update_birth_control_knowledge()
                if the_person.has_child_with_mc : # == 0:
                    the_person "Oh no, you need to pull out sweetheart! I'm not on birth control, you'll get me pregnant again!!"
                else:
                    the_person "Oh no, you need to pull out sweetheart! I'm not on birth control, you'll get me pregnant"

            elif the_person.opinion.creampies < 0:
                the_person "Pull out and cum all over me [the_person.mc_title]!"

            else:
                if the_person.has_child_with_mc : # == 0:
                    if the_person.baby_desire < 20: #She doesn't want it.
                        the_person "No! Not inside! We can't have a baby together!"
                    else:
                        the_person "Wait, you need to pull out! I can't risk getting pregnant with your baby!"
                else:
                    if the_person.baby_desire < 20: #She doesn't want it.
                        the_person "Wait, you need to pull out! You gonna get me pregnant again!"
                    else:
                        the_person "Wait, you need to pull out! No!"
    return

label mom_cum_vagina_revamp(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Pump it out sweetheart, give mommy all of your cum!"

        elif the_person.on_birth_control:
            the_person "That's it sweetheart, cum inside mommy. I'm on the pill, so you don't have to worry about getting me pregnant."
            $ the_person.update_birth_control_knowledge()

        elif the_person.effective_sluttiness() > 75 or the_person.opinion.creampies > 0:
            the_person "Aaah... I can feel it... So hot... So much of it inside of me~"
        else:
            the_person "That's it, cum inside mommy. We can worry about me getting pregnant later, just enjoy yourself right now."


    else: #She's angry
        if not the_person.on_birth_control:
            if the_person.has_child_with_mc: # == 0:
                the_person "Oh sweety, you shouldn't finish inside me! You're so young and virile, it wouldn't take much to get mommy pregnant again especially when she's not on her birth control!"
                $ the_person.update_birth_control_knowledge()
            else:
                the_person "Oh sweety, you shouldn't finish inside me! You're so young and virile, it wouldn't take much to get mommy pregnant when she's not on her birth control!"
                $ the_person.update_birth_control_knowledge()

        elif the_person.opinion.creampies < 0:
            the_person "Why in the world did you cummed inside me? Didn't I tell you not to?"

        else:
            if the_person.has_child_with_mc: # == 0:
                the_person "Oh sweetheart, you really need to be pulling out. You gonna get me pregnant again very very quickly."
            else:
                the_person "Oh sweetheart, you really need to be pulling out. I know you're just having fun, but we can't take risks like this every time."
        the_person "Oh well, it's done now. Just be more careful next time."

    return

label mom_condom_demand_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        "She gives you a stern, motherly look."
        the_person "Wait... Why are you putting on a condom? You are serious?"
        the_person "Are we really?! I'm your mother!"
    else:
        if the_person.wants_creampie:
            the_person "Young man, you need to put on a condom before we can do anything."
            the_person "We might get carried away without one, and I don't even trust myself when we're... distracted."
        else:
            the_person "[the_person.mc_title], do you have a condom? You're going to need to put one on."
            the_person "If you don't have one we could do something else."
    return

label mom_condom_ask_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        "She gives you a stern, motherly look."
        the_person "Wait... Why are you putting on a condom? You are serious?"
        the_person "Are we really?! I'm your mother!"
    else:
        if the_person.on_birth_control:
            the_person "Now [the_person.mc_title], I'm on birth control, but we really should use protection though."
            the_person "Do you have a condom with you? I hope you're always prepared."
            $ the_person.update_birth_control_knowledge()
        elif the_person.wants_creampie:
            the_person "Condom, young man! I don't want you to have to pull out when you finish."
            $ the_person.discover_opinion("creampies")
        else:
            if the_person.has_child_with_mc :
                the_person "Wait, wait!"
                mc.name "What is it?"
                the_person "I need you to wear a condom."
                mc.name "A condom? But... why now?"
                the_person "I don’t want to get pregnant again so soon. Not at my age. It’s... too risky."
            else:
                the_person "You should really put on a condom [the_person.mc_title]."
                the_person "I trust you, but it's so easy for accidents to happen when we're... distracted."
    return

label mom_condom_bareback_ask_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        if the_person.wants_creampie:
            if the_person.on_birth_control:
                the_person "I'm out of my mind but... you don't need to use any protection [the_person.mc_title]. I'm on birth control."
                the_person "That means you can cum right inside [the_person.possessive_title]'s pussy if you want. I'd like it very much if you did."
                $ the_person.update_birth_control_knowledge()
            else:
                the_person "This is crazy... But you don't need to use any protection [the_person.mc_title]."
                the_person "I would love it if you came inside me, even with the risks."
                "She barely whispers..."
                the_person "I'm not on BC. Does it turn you on? A chance to impregnate [the_person.possessive_title]?"
                $ the_person.update_birth_control_knowledge()
            $ the_person.discover_opinion("creampies")
        else:
            the_person "This is crazy... But you don't need any protection with me [the_person.mc_title]."
            the_person "Let's have the best time possible, even if it's a little risky..."
    else:
        if the_person.wants_creampie:
            if the_person.on_birth_control:
                the_person "This is crazy... But you don't need to use any protection [the_person.mc_title]. I'm on birth control."
                the_person "That means you can cum right inside my pussy if you want. I'd like it very much if you did."
                $ the_person.update_birth_control_knowledge()
            else:
                the_person "You don't need to use any protection [the_person.mc_title]."
                the_person "I would love it if you came inside me, even with the risks."
                "She barely whispers..."
                the_person "I'm not on BC. Does it turn you on? A chance to impregnate [the_person.possessive_title]?"
                $ the_person.update_birth_control_knowledge()
            $ the_person.discover_opinion("creampies")
        else:
            the_person "You don't need any protection with me [the_person.mc_title]."
            the_person "I want you to have the best time possible, even if it's a little risky..."
    return

label mom_condom_bareback_demand_revamp(the_person):
    if the_person.has_taboo("vaginal_sex") or the_person.has_taboo("anal_sex"):
        the_person "This sounds crazy, but I want you just the way you are."
        the_person "If I'm going to have my son fucking me, might as well do it raw!"
    else:
        if the_person.has_breeding_fetish: #Actively looking to get knocked up.
            the_person "Don't bother [the_person.mc_title], I want it raw so you can get me pregnant!"
            if not the_person.knows_pregnant:
                the_person "Make sure to cum inside me so you knock me up!"

        elif the_person.on_birth_control:#Just likes raw sex
            the_person "Don't bother with that. I'm on birth control, so we don't need to worry."
            the_person "I want you to fuck me [the_person.mc_title], and I want you to do it raw!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Don't bother with that, I want you just the way you are."
            the_person "Go ahead [the_person.mc_title], put it inside me!"
    return