#Counter = KFC01

#Base game #TODO improvement

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["lily_new_underwear_crisis_label"] = "lily_new_underwear_crisis_revamp_label"
    config.label_overrides["mom_lingerie_surprise_label"] = "mom_lingerie_surprise_revamp_label"

label lily_new_underwear_crisis_revamp_label():
    # Lily has some new underwear she wants to demo for you.
    # We base the underwear sluttiness on Lily's sluttiness and use Love+Sluttiness to see if she'll show you as a "full outfit".
    $ the_person = lily #Just so we can keep
    $ the_underwear = lily_new_underwear_get_underwear(the_person)
    if the_underwear is None:
        return #Lily doesn't have any skimpy underwear to show us :(

    $ mc.change_location(bedroom) #Make sure we're in our bedroom.
    if the_person.obedience >= 95:
        "There's a knock at your door."
        the_person "[the_person.mc_title], can I talk to you for a sec?"
        mc.name "Uh, sure. Come in."
        "Your bedroom door opens and [the_person.possessive_title] steps in. She's carrying a shopping bag in one hand."
    else:
        "There's a single knock at your bedroom door before it's opened up. [the_person.possessive_title!c] steps in, carrying a shopping bag in one hand."

    $ the_person.draw_person(emotion = "happy")
    if the_underwear.underwear_slut_score < 10:
        the_person "This is a little awkward, but I picked up some new underwear at the mall today but I don't know if I like the way it looks."
        the_person "Would you take a look and let me know what you think?"
    elif the_underwear.underwear_slut_score < 20:
        the_person "I was at the mall today and picked up some new underwear. I know Mom would say it's too skimpy, but I wanted a guys opinion."
        $ mc.change_locked_clarity(5)
        the_person "Would you let me try it on and tell me what you think?"
    else:
        the_person "I was at the mall today and picked up some lingerie. I was hoping you'd let me model it for you and tell me what you think."
        $ mc.change_locked_clarity(10)

    menu:
        "Take a look at [the_person.title]'s new underwear":
            "You sit up from your bed and give [the_person.possessive_title] your full attention."
            mc.name "Sure thing, is it in there?"
            "You nod your head towards the bag she is holding."
            the_person "Yeah, I'll go put it on and be back in a second. Don't move!"
            $ clear_scene()
            "[the_person.title] skips out of your room, closing the door behind her."
            $ the_person.apply_outfit(the_underwear)
            "You're left waiting for a few minutes. Finally, your door cracks open and [the_person.title] slips inside."
            $ the_person.draw_person(emotion="happy")
            if the_person.update_outfit_taboos():
                the_person "Oh my god, this is so much more embarrassing than I thought it would be."
                mc.name "Come on [the_person.title], I'm your brother. You can trust me."
                "She takes a deep breath and nods."
                the_person "Yeah, sure. Just don't stare too much, okay?"
                the_person "So, what do you think?"
                mc.name "Turn around, I want to see the other side."
            else:
                the_person "Here we go. What do you think?"
            $ the_person.draw_person(emotion="happy", position = "back_peek")
            "She turns around to give you a good look from behind."
            $ mc.change_locked_clarity(10)
            $ verdict = "meh"
            menu:
                "She looks beautiful": #Raises love
                    mc.name "You look beautiful [the_person.title]. You're a heart-stopper."
                    $ the_person.change_love(2)
                    the_person "Aww, you really think so?"
                    $ verdict = "beautiful"

                "She looks sexy": #Raises sluttiness
                    mc.name "You look damn sexy in it [the_person.title]. Like you're just waiting to pounce someone."
                    $ the_person.change_slut(2, 30)
                    the_person "Ooh, I like being sexy. Rawr!"
                    $ verdict = "sexy"

                "She looks elegant": #Raises obedience
                    mc.name "It makes you look very elegant, [the_person.title]. Like a proper lady."
                    $ the_person.change_obedience(2)
                    the_person "It's not too uptight, is it? Do you think Mom would wear something like this?"
                    $ verdict = "elegant"

                "You don't like it": #Raises nothing.
                    mc.name "I'm not sure it's a good look on you [the_person.title]."
                    $ the_person.change_happiness(-2)
                    the_person "No? Darn, it was starting to grow on me..."

            "[the_person.title] stands in front of your mirror and poses."
            $ the_person.draw_person(emotion = "happy")
            the_person "Do you think I should keep it? I'm on the fence."
            menu:
                "Keep it":
                    $ the_person.wardrobe.add_underwear_set(the_underwear)
                    mc.name "You should absolutely keep it. It looks fantastic on you."
                    $ the_person.change_happiness(3)
                    "[the_person.title] grins and nods."
                    the_person "You're right, of course you're right. Thank you [the_person.mc_title], you're the best!"


                "Return it":
                    mc.name "I think you have other stuff that looks better."
                    $ the_person.change_obedience(2)
                    the_person "I think you're right, I should save my money and get something better. Thank you [the_person.mc_title], you're the best!"

            $ the_person.change_love(3)
            if not the_person.has_taboo("vaginal_sex"):
                "[the_person.possessive_title!c] walks over and sits on your lap."
                $ the_person.draw_person(position = "sitting", emotion = "happy")  
                "She looks at you, eyes filled with lust, and spreads her legs wider."
                the_person "So, I look [verdict] in this, eh?"
                if not verdict == "meh":
                    the_person "[verdict!c] enough for you to fuck?"
                else:
                    the_person "Sorry to dissappoint.. How can I ever make it up to you?"
                menu:
                    "Fuck her":
                        mc.name "You know I prefer you in your birthday suit."
                        $ strip_list = the_person.outfit.get_vagina_strip_list(visible_enough = False)
                        if strip_list:
                            the_person "Let's compromise~"
                            "She jumps up and starts to strip for you."
                            $ generalised_strip_description(the_person, strip_list)
                            $ the_person.draw_person(position = "missionary")
                            "[the_person.title] lays on your bed, legs wide apart for you."
                            $ strip_list = None
                            the_person "Come at me tiger, ravage [the_person.possessive_title]!"
                            call fuck_person(the_person, start_position = missionary, start_object = mc.location.get_object_with_name("bed"), skip_intro = True, skip_condom = True) from _call_fuck_person_lily_new_underwear_crisis_KFC01
                            $ the_person.call_dialogue("sex_review", the_report = _return)
                    "Maybe later":
                        mc.name "I don't have the time right now, but maybe later."
                        $ the_person.draw_person(position = "default")
                        "She stands up and pouts at you."
                        the_person "Aww... Alright."
            else:
                "[the_person.possessive_title!c] walks over to you and gives you a hug."
            the_person "It's getting cold. I'm going to go put some clothes on!"
            $ clear_scene()
            $ the_person.apply_planned_outfit() # make her change back to her normal outfit (for morning crisis events)
            "[the_person.title] slips out into the hall, leaving you alone in your room."


        "Send her away":
            mc.name "Sorry [the_person.title], but I'm busy right now. You'll have to figure out if you like it by yourself."
            the_person "Right, no problem. Have a good night!"
            $ clear_scene()
            "She leaves and closes your door behind her."

    $ clear_scene()
    $ the_underwear = None
    return

label mom_lingerie_surprise_revamp_label():
    #In which your Mom comes to your room at night in some sexy lingerie and fools around with you. Triggers at high sluttiness and love.
    $ the_person = mom
    $ mc.change_location(bedroom)
    "You are woken up in the middle of the night by the sound of your bedroom door closing."
    "You sit up and turn on the lamp beside your bed."
    $ the_person.apply_outfit(the_person.personalize_outfit(lingerie_wardrobe.pick_random_outfit()), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    the_person "I'm sorry to wake you up [the_person.mc_title], but I wanted to ask you something."
    "[the_person.possessive_title!c] is standing by the door, wearing some very revealing lingerie. She walks over to your bed and sits down beside you."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "sitting")
    mc.name "What did you want to ask?"
    the_person "I know you've been busy with work, and I'm very proud, but sometimes I worry you're not having your needs met."
    "She places a hand on your arm and slides it up to your chest, caressing you with her soft fingers."
    the_person "Your physical needs, I mean. I know I'm your mother, but I thought I could dress up and you could pretend I was someone else. Someone not related to you."
    menu:
        "Ask for her help (tooltip)Ask your mother to help satisfy your physical desires.":
            mc.name "That would be amazing Mom, I could really use your help."
            $ the_person.change_slut(2, 50)
            "[the_person.possessive_title!c] smiles and bounces slightly on your bed."
            if the_person.effective_sluttiness() < 50:
                the_person "Excellent! Now you just pretend that I'm... your highschool sweetheart, and that we aren't related. Okay?"
                $ mc.change_locked_clarity(10)

            elif the_person.effective_sluttiness() < 80:
                the_person "Excellent! Don't think of me as your mother, just think of me as a sexy mom from down the street. I'm a real MILF, okay?"
                $ mc.change_locked_clarity(20)

            else:
                the_person "Excellent! Now don't think of me as your mom, just think of me as your private, slutty MILF. I'll do whatever your cock wants me to do, okay?"
                $ mc.change_locked_clarity(40)
            "You nod and she slides closer to you on the bed."

            $ the_person.add_situational_obedience("crisis_stuff", 10, "I'm doing it for my family.")
            call fuck_person(the_person) from _call_fuck_person_KFC14
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0 and the_report.get("girl orgasms", 0) > 0:
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "[the_person.possessive_title!c] lays back with a dopey smile on her face as you both recover from your orgasms."
                $ the_person.change_love(5)
                mc.name "Are you sure you came in here because you were worried about MY needs?"
                $ the_person.draw_person(position = "sitting", emotion = "happy")
                "She chuckles and starts to grab her cloths."
                $ the_person.clear_situational_obedience("crisis_stuff")
                mc.name "Stay the night, [the_person.title]."
                "She nods, and quickly settles in herself on the bed."
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title!c] snuggles closer to you, allowing you to wrap your arms around her sexy body."
                if the_person.has_large_tits:
                    "Your hands playfully land on her [the_person.tits_description]."
                    $ the_person.draw_person( position = "back_peek", emotion = "happy")
                the_person "Love you, [the_person.mc_title]."
                mc.name "Love you too, [the_person.title]."
                $ clear_scene()        
                call advance_time() from _call_advance_time_spend_the_night_KFC01

            elif the_report.get("girl orgasms", 0):
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "[the_person.possessive_title!c] needs a few minutes to lie down when you're finished. Bit by bit her breathing returns to normal."
                $ the_person.change_love(5)
                the_person "Oh [the_person.mc_title], that was magical. I've never felt so close to you before..."
                $ the_person.draw_person(position = "sitting", emotion = "happy")
                "She chuckles and starts to grab her cloths."
                $ the_person.clear_situational_obedience("crisis_stuff")
                mc.name "Stay the night, [the_person.title]."
                "She nods, and quickly settles in herself on the bed."
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title!c] snuggles closer to you, allowing you to wrap your arms around her sexy body."
                if the_person.has_large_tits:
                    "Your hands playfully land on her [the_person.tits_description]."
                    $ the_person.draw_person( position = "back_peek", emotion = "happy")
                the_person "Goodnight [the_person.mc_title]."
                mc.name "Goodnight [the_person.title]."
                $ clear_scene()        
                call advance_time() from _call_advance_time_spend_the_night_KFC02

            else:
                $ the_person.draw_person(emotion = "happy")
                "When you're finished [the_person.possessive_title] gives you a kiss on your forehead and stands up to leave."
                $ the_person.change_love(3)
                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                the_person "Sweet dreams."
                $ the_person.clear_situational_obedience("crisis_stuff")

            
        "Not tonight":
            mc.name "That's very sweet of you Mom, and you look very nice, but I really just need a good night's sleep."
            "You see a split second of disappointment on [the_person.possessive_title]'s face, then it's gone and she blushes and turns away."
            the_person "Of course, I'm so sorry to have bothered you. I mean, it would be strange if we did anything like that, right?"
            $ the_person.draw_person(position = "walking_away")
            "She stands up and leaves your room. You're asleep within minutes."

    $ clear_scene()
    return