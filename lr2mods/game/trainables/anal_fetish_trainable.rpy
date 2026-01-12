init 2 python:
    def increase_anal_fetish(person):
        if renpy.random.randint(0,100) < 25: # only chance to increase skill
            person.increase_sex_skill("Anal", 5, add_to_log = True)
        person.change_slut(2, 90, add_to_log = True)
        if not fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, 2, person):
            mc.log_event(f"{person.display_name} anal fetish training is less effective, but she hasn't got a fetish yet.", "float_text_blue")
        return


label train_anal_fetish_label(the_person):
    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    mc.name "I've noticed that you really enjoy when I play with your ass."
    the_person "Yeah... I do..."
    mc.name "I was thinking that we should explore this a little further, what do you think?"
    the_person "Well, I wouldn't mind if you did."
    mc.name "Good, stand up and show me your butt."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title!c] turns around to show you her bottom."
    if not the_person.vagina_available:
        mc.name "Let's get these clothes out of the way."
        $ the_person.strip_to_vagina(position = "standing_doggy")
    "Now since you got her sweet ass on display, what do you plan to do with it?"
    menu:
        "Rub her ass":
            "You reach out and start to rub her ass."
            the_person "Hmmm, that feels nice..."
            "As you slowly move your thumbs closer to her rectum, she starts pushing her butt in your direction."
            mc.name "You like this, don't you?"
            $ play_moan_sound()
            the_person "Oh yes, please, just push them a little inside."
            "You place your thumbs on either side and slide the tips inside, provoking a little sigh from [the_person.possessive_title]."
            mc.name "Do you want me to stretch it a bit for you?"
            $ play_moan_sound()
            the_person "Mmm... get that dirty hole ready for your big cock."
            "You continue stretching her asshole for a while, until you notice that her [the_person.pubes_description] pussy starts glistening."

        "Spank her" if the_person.is_submissive and the_person.spank_level < 4:
            "You reach out and start to rub her ass."
            the_person "Hmmm, that feels nice..."
            $ the_person.slap_ass()
            the_person "Ah, fuck..."
            $ the_person.slap_ass()
            the_person "Mmmh, yes... that's it."

            "Her ass is [the_person.ass_spank_description]"
            "You also notice that some juices are flowing out of her slit."
            "You move your hand between her legs and start to lube up her asshole with her own pussy fluids."
            the_person "Oh, yes, right there [the_person.mc_title]."
            mc.name "You like this, don't you?"
            the_person "Oh yes, please, just push it a little inside."
            $ play_moan_sound()
            "You slowly insert a finger into her bowels. While you start to slap her ass cheeks with your other hand."
            $ the_person.slap_ass(update_stats = False)
            $ the_person.slap_ass(update_stats = False)
            the_person "Ahhh... YES... stretch my dirty hole [the_person.mc_title]."
            mc.name "You are going to be my slutty anal bitch, aren't you [the_person.fname]?"
            $ play_moan_sound()
            the_person "Yes... I will... hmmm... right there..."
            "You shove your finger as deep as possible up her bum. Her [the_person.pubes_description] slit is overflowing with juices as you give her ass another swat."
            $ the_person.slap_ass(update_stats = False)


        "Finger her ass" if the_person.anal_sex_skill > 2:
            "You reach out and start to rub her bottom."
            the_person "Hmmm, that feels nice..."
            "After awhile, you slowly start tracing her orifice with your fingers. Causing a slight tremble from [the_person.possessive_title]."
            the_person "Oh, yes, right there [the_person.mc_title]."
            "That's all the encouragement you need to slide your finger inside."
            the_person "Mmmm... yes... that's it. Every time I play with myself I have to push a finger inside."
            menu:
                "Continue":
                    "Using some spit as lube, you shove your entire finger inside her."
                    $ play_moan_sound()
                    the_person "Oh god, YES, just like that..."
                    "You continue to finger-fuck her ass for a while, until her [the_person.pubes_description] pussy gets really wet."
                "Slide in a second finger":
                    "You lube up a second finger with your saliva and push both fingers inside."
                    $ play_moan_sound()
                    the_person "Ahhh... YES... stretch my dirty hole [the_person.mc_title]."
                    mc.name "You are going to be my slutty anal bitch, aren't you [the_person.fname]?"
                    $ play_moan_sound()
                    the_person "Yes... I will... hmmm... right there..."
                    "You continue to shove your fingers up her bum, until her [the_person.pubes_description] pussy gets really wet."

        "Shove a dildo inside" if the_person.anal_sex_skill > 3 and perk_system.has_item_perk("Dildo"):
            if the_person.event_triggers_dict.get("has_used_dildo", False):
                mc.name "I have brought your favourite toy."
                the_person "Ok, slide that bad boy right in there!"
            else:
                mc.name "I have something I think you might enjoy."
                the_person "Oh? What might that be?"
                "You pull the dildo out of your backpack. Her eyes fix on it and she realises what you want to do."
                if the_person.sluttiness > 40: #She is excited.
                    the_person "Oh! That looks like fun..."
                else:
                    the_person "Oh my god, it's so big! I don't know about this..."
                    mc.name "Don't worry, I'll go slow."

            "You lube up the dildo and slide it all the way into her bowels, leaving just enough room to hold it."
            the_person "Oh god, that's it [the_person.mc_title]."
            mc.name "You enjoy this, don't you?"
            the_person "Oh yes, please, can you push it a little farther."
            mc.name "Do you want to swallow it with your ass?"
            the_person "I wouldn't mind giving it a try..."
            "You smile, and press the last part of the toy into her ass until her sphincter closes over the end caressing your fingers."
            $ play_moan_sound()
            the_person "Ahhh....Yes...sooo deep...keep moving..."
            mc.name "You are going to be my little anal whore, aren't you [the_person.fname]?"
            $ play_moan_sound()
            the_person "I am...YES...deeper...your greedy little anal whore!!"
            "You continue to push the toy back when it slowly starts moving out again, until you finally let it pop out completely."

    mc.name "Alright, [the_person.title], that's enough for now. We will continue this another time."
    $ increase_anal_fetish(the_person)
    the_person "Oh [the_person.mc_title], that felt... just... amazing."
    if start_anal_fetish_quest(the_person):
        $ the_person.event_triggers_dict["anal_fetish_start"] = True
        "It seems you have awoken something inside her, just wait and see what happens."
    else:
        if the_person.sluttiness < 70:
            "Although you have made some progress, you have the feeling she needs to be sluttier to fully develop this fetish."
        else:
            "You have come one step closer to awakening her anal desires. Perhaps another session or a serum with the Anal Nanobots will push her over the edge."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    the_person "Please, don't make me wait too long."
    return True
