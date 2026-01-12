### MOM ACTION LABELS ###

label mom_offer_make_dinner_label(the_person): #you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    mc.name "You've been working yourself so hard lately Mom, how about you let me make dinner tonight?"
    the_person "Oh [the_person.mc_title], that's such a sweet thing for you to offer!"
    $ the_person.change_stats(happiness = 5, love = 2, max_love = 40)

    the_person "Do you know where everything is?"
    mc.name "Yeah, I think I can take care of it."
    the_person "Well thank you, you're always such a help around here!"
    if the_person.love < 20 and the_person.effective_sluttiness() < 10:
        $ mc.change_locked_clarity(5)
        "[the_person.possessive_title!c] gives you a quick hug."
    elif the_person.love < 40 and the_person.effective_sluttiness() < 30:
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title!c] gives you a hug, then a quick kiss on the lips."
    else:
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title!c] gives you a hug, then kisses you on the lips."
        the_person "It's so nice having a man around the house again..."
        "She leans her head happily on your shoulder for a moment."
        menu:
            "Hold her gently":
                "You just hold [the_person.title] in your arms for a few moments."
                $ the_person.change_love(1, 40)
                "After a little while she sighs and steps back."
                the_person "I should get out of your way."

            "Slap her ass":
                $ play_spank_sound()
                "You reach around [the_person.possessive_title] and give her ass a quick slap."
                $ play_spank_sound()
                $ the_person.change_obedience(1, 140)
                if the_person.vagina_visible:
                    "The strike makes a satisfying smack and sets her butt jiggling for a few moments."
                    $ mc.change_locked_clarity(20)
                    "You give her bare ass a few more taps before letting her step back."
                else:
                    $ mc.change_locked_clarity(10)
                    "The strike makes a satisfying smack and sets her butt jiggling for a few moments."
                the_person "Oh!"
                mc.name "Come on [the_person.title], I've got dinner to cook. Run along, or I'll find some way to put you to work."


    the_person "Let me know if you need anything."
    $ clear_scene()
    $ kitchen.show_background()
    "You get to work. The cooking isn't hard, but it takes up most of your evening."
    if mc.inventory.has_serum:
        "As you're plating out dinner you have a perfect opportunity to give everyone some serum in secret."
        call screen serum_inventory_select_ui(mc.inventory, batch_size = (4 if aunt_living_with_mc() else 2))
        if isinstance(_return, SerumDesign):
            $ dose_dinner_with_serum(_return)
        else:
            "You decide not to add any serum to the dinner."

    "You bring the food out and have a nice family dinner together."
    call advance_time() from _call_advance_time_10
    return

label mom_date_intercept(the_mom, the_date): #TODO: Add some relationship awareness to Mom so she can comment on you dating multiple girls, ect.
    #Triggers when you've got a date planned with a girl, but Mom has high Love.
    #TODO: Write a Mom specific movie date. Maybe mirror the LR1 event and have Lily join in sometimes.

    $ mc.change_location(bedroom)

    "You're getting ready for your date with [the_date.title] when you hear a knock at your door."
    the_mom "Knock knock. Are you in there [the_mom.mc_title]?"
    mc.name "Yeah, come on in [the_mom.title]."
    $ the_mom.draw_person()
    "[the_mom.possessive_title!c] steps into your room and closes the door behind her."
    the_mom "Oh, you're looking very handsome tonight. Is there some special occasion?"
    if the_date.is_girlfriend and (not the_date.is_family or the_date.event_triggers_dict.get("sister_girlfriend_mom_knows", False)):
        mc.name "I'm taking [the_date.title] on a date tonight."
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
                call fuck_person(the_mom, private = True, skip_intro = skip_intro, start_position = start_position, skip_condom = skip_condom) from _call_fuck_person_36
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
                            call fuck_person(the_mom, private = True) from _call_fuck_person_40
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
                call fuck_person(the_mom, start_position = blowjob, skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_99
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
                call fuck_person(the_mom, start_position = handjob, skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_100
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

label mom_office_person_request():
    $ the_person = get_mom_secretary()
    $ the_person.draw_person(position = "sitting")
    "You walk up to the reception desk. The receptionist looks up at you."
    the_person "Hello, can I help you? Do you have an appointment?"

    call screen main_choice_display(build_menu_items(get_mom_office_actions(), draw_person_previews = False, draw_hearts_for_people = False))

    if _return == "Leave":
        mc.name "Sorry to bother you."
        $ clear_scene()
    elif _return == "Boss":
        call mom_promotion_boss_phase_one(the_person) from _call_mom_promotion_boss_phase_one

    else:
        mc.name "I'm here to see Ms. [mc.last_name]. Can you let her know I'm here?"
        the_person "Of course, one moment."
        "The receptionist picks up her phone and calls someone. After a brief quiet conversation she hangs up."
        if mom.is_at(mom_offices):
            the_person "She's coming down right now to meet you."
            "After a brief wait [mom.title] steps out of the lift and smiles happily at you."
            $ mom.change_location(mom_office_lobby)
            $ clear_scene()
            $ mom.draw_person() #TODO: Make sure she's wearing her work uniform.
            mom "Hi [mom.mc_title], did you need me for something?"
            call talk_person(mom) from _call_talk_person_25

        else:
            the_person "I'm sorry, but she doesn't seem to be in the building at the moment."
            mc.name "Right, okay. Sorry to bother you."
    return

label mom_found_serums(the_person = mom): #TODO: Triggers a couple of days after the start of the game
    # Triggers in the morning (so you have a chance to interact with her after dosing her)
    $ the_person = mom

    "There's a knock on your door."
    $ the_person.draw_person()
    the_person "[the_person.mc_title], can I come in?"
    mc.name "Sure [the_person.title]."
    "[the_person.possessive_title!c] opens up your bedroom door. She's holding a dusty cardboard box."
    the_person "I was doing some tidying in the attic and found this. It has your name on it..."
    "She turns the other side to face you. \"[mc.name]—Serum Reserve DO NOT TOUCH\"."
    menu:
        "Snatch the box from her":
            "You step close and grab at the box."
            mc.name "I can take that!"
            "She laughs and steps away, mistaking your worry for play."
            the_person "Oh? Hiding something away in here? Something you don't want your mother to see?"
            the_person "Am I about to find a stack of dirty magazines?"
            "She opens up the top of the box and looks inside."

        "Ask calmly for it":
            mc.name "Oh, that. I can take that from you."
            "You step close and motion to take the box from her, but she holds onto it for a moment and opens the top of the box."

    the_person "What is all of this, anyways? A whole lot of glass..."
    mc.name "It's some... stuff from the university lab."
    the_person "[the_person.mc_title], were you stealing?"
    "You were."
    mc.name "No, of course not! It's stuff I... made. I didn't know it was still around. Can I have the box now?"
    "She pulls out one of the glass vials inside and holds it up to the light. It's a light blue."
    the_person "Is this the stuff you're making in your lab now?"
    mc.name "Sort of, yeah."
    the_person "Hmm... What does it do?"
    menu:
        "You should try it and find out":
            mc.name "Drink it and find out. It's not harmful."
            the_person "Really? It's not a drug, is it?"
            mc.name "Everything's a drug, [the_person.title]. It won't get you high, if that's what you're asking."
            "She considers it, then shrugs and uncorks the top of the vial."
            the_person "I have to admit I am a little curious..."
            $ the_person.give_serum(get_blue_serum())
            "[the_person.possessive_title!c] drinks down the liquid and drops the empty vial back into the box."
            the_person "Well? Now what?"
            mc.name "You probably won't feel anything. The effects are subtle."
            the_person "But it's good for me?"
            mc.name "Yes [the_person.title], it's good for you."
            "She smiles happily and hands you the box full of old serum doses."


        "Nothing, really":
            mc.name "Nothing, really. But it's quite delicate, so if I could just have those..."
            the_person "Right, sorry."
            "She puts the vial back and hands the box to you."

    the_person "Now I'll get out of your way. Have a good day!"
    $ clear_scene()

    "She closes the door behind her, leaving you alone with your spoils. You had forgotten you stashed these away as an emergency reserve."
    "You dig through the box. Some vials are empty—maybe you used them, or they were never full to begin with."
    $ mc.inventory.change_serum(get_blue_serum(), 6)
    $ mc.log_event("Found 6 doses of Blue Serum!", "float_text_blue")
    "You find a number of blue serum doses. Back in university they did a wonderful job of making girls slutty and influenceable."
    "Best to save them for when you have a specific boundary to push though, because they don't last very long."

    "You dig a little deeper. There are a few specialised doses of serum in here too."
    $ mc.inventory.change_serum(get_red_serum(), 3)
    $ mc.log_event("Found 3 doses of Red Serum!", "float_text_blue")
    "Red serum. It was stronger than your Blue design, making girls slutty and obedient on the spot."
    "It was also particularly likely to make a girl suggestible after she climaxed."

    $ mc.inventory.change_serum(get_purple_serum(), 3)
    $ mc.log_event("Found 3 doses of Purple Serum!", "float_text_blue")
    "And some Purple serum. It's a gentler, longer duration serum."
    "It didn't make girls any sluttier directly, but it gave you a lot of time to try and make them cum."
    "If you did you could usually put some very fun ideas in their heads."
    "Useful when you have the time and opportunity to focus on one girl in particular."


    "Of course you could always sell these doses at the office. Sometime soon you'll be able to recreate them and more anyways."
    "But maybe it's a good idea to hold onto them, in case you find any interesting opportunities to apply them."
    "After you pull the serums out of the box, you find a couple note cards in the bottom of the box."
    "They are your original notes on formulating the red and purple serums. You could use these to recreate these!"
    "However, you note that it takes some fairly intricate equipment to synthesize. Do you even have the equipment to make these right now?"
    $ unlock_red_serum()
    $ unlock_purple_serum()

    $ the_person.set_event_day("obedience_event")
    $ the_person.set_event_day("love_event")
    $ the_person.set_event_day("slut_event")
    $ the_person.set_event_day("story_event")
    # Jennifer's sluttiness arc starts through her work events.
    $ add_mother_love_lunch_date_action()


    return
