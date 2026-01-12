
#Kaya is busy 7 days a week with her updated schedule.
#As it starts to wear on her, MC catches her taking a nap in an empty room at work.
#MC has the option to arrange a day off each week for her or allow her to take naps while at work.
#If the latter, we get a new sleep event crisis, similar to Lily and Jennifer, but at work.

label kaya_needs_a_break_label():
    $ the_person = kaya
    #In this label, we catch Kaya taking a nap while at MC's business.
    #MC empathises and is given a choice
    #He can either arrange to give her fridays off, covering it with HR
    #Or he can give her permission to take naps at the office, leading to possible sleeping encounters with her.

    menu:
        "Give her Fridays off":
            pass
        "Let her nap at work":
            $ the_person.event_triggers_dict["work_naps"] = True
    pass
    return

label kaya_naps_at_work_label():
    $ the_person - kaya
    #This label should be similar to Jennifer and Lily's sleeping events, but located at MC's business.

    pass
    return


#Call this label anytime MC gets coffee while Kaya is working.
#Because her intro is room entry, there SHOULDN'T be a possibility that we don't know who she is when running this label.
label kaya_get_coffee_label(the_person):
    $ the_person = kaya
    "You step up to the coffee shop counter. [the_person.possessive_title!c] is working today."
    $ the_person.draw_person()
    the_person "Hello there [the_person.mc_title]. Here for a coffee?"
    mc.name "Of course."
    if the_person.event_triggers_dict.get("milk_coffee", False):    #Triggered in Kaya's pregnancy path
        if the_person.lactation_sources >= 3:   #Her milk is in strong enough. Kaya is milkier than average woman in LR2
            the_person "There is plenty of fresh milk today, if you wanted some in your coffee..."
            $ the_person.change_arousal(5)
            "She seems excited by the prospect of adding her breastmilk to your order."
        else:
            the_person "Sorry, there isn't enough fresh milk today, but I have regular if you want some."
            "It seems her body isn't lactating enough to provide you with fresh breastmilk in your order."

    menu:
        "Black Coffee":
            "You give her your order."
            if the_person.love >= 40:   #at 40 love she offers free coffee to MC.
                the_person "Don't worry about the price, it is on the house today."
                "She gives you a wink and starts to make your order. Soon she is handing you a cup of fresh coffee."
            else:
                "You give her your order and pay. Soon she is handing you a cup of fresh coffee."
                $ mc.business.change_funds(-5, stat = "Food and Drinks")
            menu:
                "Leave a tip":
                    "You drop an extra $5 in the tip jar."
                    $ mc.business.change_funds(-5, stat = "Food and Drinks")
                    the_person "Aww, thank you!"
                    $ the_person.change_love(2, 30)
                "No tip":
                    pass
            "You sit down at a table and enjoy the fresh brew. The flavour and caffeine perks you up a bit."
            $ mc.change_energy(30)
        "Coffee with Fresh Cream" if (the_person.event_triggers_dict.get("milk_coffee", False) and the_person.lactation_sources >= 3):
            the_person "Coming right up! And don't worry about the price, it is on the house today."
            "She gives you a wink and starts to make your order."
            if the_person.sluttiness > 40:   #This will be if topless is legal. For now do a sluttiness check but later change to the legal question.
                if the_person.tits_visible:
                    "After pouring your coffee, she brings the cup up to her exposed chest."
                else:
                    "After pouring your coffee, she quickly pulls up her top."
                    $ the_person.strip_to_tits(prefer_half_off = True)
                    "With her tits out, she brings your coffee up to her exposed chest."
                if the_person.sluttiness > 60:
                    mc.name "Hang on, I prefer to add the cream myself, to make sure I get just enough."
                    the_person "Of course! I'm sorry sir, go ahead!"
                    "[the_person.possessive_title!c] hands you the cup, then leans in over the counter."
                    $ the_person.draw_person(position = "stand2", display_transform = character_right(zoom = 1.2))
                    if the_person.has_large_tits:
                        "Her big, milky tits wobble enticingly as she waits for you to milk her."
                    else:
                        "Her perky, milky tits sit out, begging you to milk her."
                    $ mc.change_locked_clarity(50)
                    "You bring your cup up to her left breast, then reach around with your other hand and begin to squeeze it."
                    "A stream of milk immediately begins, and you begin to milk her with firm squeezing motions."
                    the_person "Mmmmmfff..."
                    "She stifles a moan and looks around the shop for a moment, but clearly enjoys being milked."
                    $ the_person.change_arousal(10)
                    $ mc.change_locked_clarity(30)
                    if the_person.lactation_sources >= 5:   #She has too much supply
                        "You stop squeezing, wanting to move to the other side, but milk continues to stream from [the_person.possessive_title]'s milk heavy breast."
                        the_person "Oh god... here I'll go get an extra cup..."
                        "She quickly grabs an empty coffee cup and replaces yours, catching the excess milk."
                    else:
                        "You stop squeezing and the milk slowly stops coming out."
                    "You move your cup over to the other side and begin again. Another stream of milk beings from the other side."
                    the_person "AAAhhhhhmmmmfff..."
                    $ the_person.change_arousal(20)
                    $ mc.change_locked_clarity(40)
                    "A loud moan escapes before she is able to cut it off. She closes her eyes and focuses on keeping herself quiet."
                    if not mc.business.public_sex_act_is_legal: #Technically this act is probably illegal.
                        "You hear a couple murmurs from some of the other coffee shop patrons."
                        "Groping [the_person.title] here probably crosses the line into a public sex act, which is currently illegal."
                    else:
                        mc.name "It's okay, you can moan. Let everyone else here know how much you enjoy being milked like this."
                        the_person "Oh fuck... I know I'm just not used to it being legal yet. God it feels so good!"
                        $ the_person.change_arousal(10)
                        $ mc.change_locked_clarity(40)
                    if the_person.lactation_sources >= 5:
                        "Again, you finish getting the milk you want, but the stream from her chest continues."
                        the_person "Ah geeze... okay this one has stopped..."
                        "She moves the cup she is holding from her left breast to her right, replacing yours and catching the excess."
                    else:
                        "Once you feel you have enough milk, you stop milking her, and her supply slowly cuts off."
                    #Next, split paths depending on if public sex or public sex acts are legal and if Kaya is willing.
                    #Kaya gets milk after getting pregnant, so she likely just gets dicked down here.
                    #if mc.business.public_sex_is_legal and kaya_had_condom_talk():             #Same legal issue here.
                    if the_person.sluttiness > 80 and kaya_had_condom_talk():
                        if the_person.arousal > 60: #She asks you for it. also check for her public sex opinion?
                            the_person "[the_person.mc_title]... I'm so close... can you come around the counter and just..."
                            mc.name "You want me to bend you over the counter and fuck you, right here in front of everyone?"
                            #"Your recent actions have made all acts of public sex legal, so there is nothing wrong it."
                            the_person "Yes! Oh yes please!"
                        else:
                            the_person "Wow... that felt really good."
                            "You look behind you. There isn't anyone in line behind you."
                            #"Your recent actions have made all acts of public sex legal, you could walk around the counter and fuck her right here..."
                        menu:
                            "Fuck her now":
                                "[the_person.possessive_title!c] watches as you leave your coffee on the counter and start to step around it."
                                mc.name "I think it is only fair that I milked you, so you should milk me now, with that hot young body of yours."
                                the_person "Mmm, that sounds fair!"
                                $ the_person.draw_person(position = "standing_doggy")
                                "You bend her over the counter."
                                if the_person.vagina_available:
                                    "When she bends over, her hot young cunt is open and ready for you penetrate."
                                else:
                                    "You quickly pull away the clothing between you and her hot young cunt."
                                    $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
                                $ mc.change_locked_clarity(50)
                                "You pull your cock out and put your hands on her hips. You run yourself along her wet slit a few times, her arousal collecting on your tip."
                                if the_person.wants_creampie:
                                    the_person "Make sure you finish inside me!"
                                    $ mc.change_locked_clarity(30)
                                    mc.name "Why?"
                                    the_person "Ummm... errmm... I mean... this is a food preperation area..."
                                    the_person "Can't have your cum contaminating the area... we need to keep it contained!... *where it belongs*"
                                    mc.name "Ah, I see. I'll keep that in mind then."
                                "She is very aroused from milking her earlier. You pull her hips back a bit and easily slide inside her."
                                the_person "Yes! Mmmm ohhh god..."
                                "[the_person.title] moans loudly as you begin to fuck her in the middle of the coffee shop, bent over the front counter."
                                #Make a condition here? For her to take orders from customers while you fuck her?
                                call fuck_person(the_person, private = False, skip_intro = True, start_position = standing_doggy, start_object = mc.location.get_object_with_name("counter"), position_locked = True, skip_condom = True ) from _call_fuck_kaya_public_coffeeshop
                                $ the_report = _return
                                if the_report.get("creampies", 0) >= 1: #She took your cum internally
                                    "As you step back from [the_person.possessive_title], a little bit of your cum flows out of her and dribbles down between her legs."
                                    if the_report.get("girl orgasms", 0) > 0:   #She also finished
                                        the_person "Oh god... how am I supposed to keep working now..."
                                        "Her legs are a bit wobbly, but she manages to stand up and turn around."
                                    else:
                                        the_person "Mmm... that was nice..."
                                        "She stands up and turns around."
                                else:
                                    "She stands up and turns around."
                                $ the_person.draw_person(position = "stand2")
                                mc.name "Thank you for the excellent service [the_person.fname]."
                                the_person "Of course... please enjoy your... your coffee..."
                                "She is still catching her breath."
                                "You step back around the counter and pick up your coffee as she tries to straighten out her uniform."

                            "Ask for blowjob":
                                call kaya_get_coffee_blowjob(the_person) from _call_kaya_get_coffee_blowjob_2

                            "Fuck her tits" if the_person.is_willing(tit_fuck) and the_person.has_large_tits:
                                call kaya_get_coffee_titfuck(the_person) from _call_kaya_get_coffee_titfuck_2

                            "Finish up":
                                "You decide not to fuck her right now."

                    # elif mc.business.public_sex_act_is_legal and the_person.is_willing(blowjob):
                    elif the_person.is_willing(blowjob):

                        the_person "Wow... that felt really good."
                        "You look behind you. There isn't anyone in line behind you."
                        #"Your recent actions have made all acts of foreplay in public legal. You could probably but that mouth of hers to good use while it is slow."
                        if the_person.has_large_tits:
                            "Or maybe even make use of those big tits you just milked."
                        menu:
                            "Ask for a blowjob":
                                call kaya_get_coffee_blowjob(the_person) from _call_kaya_get_coffee_blowjob_1
                            "Fuck her tits" if the_person.is_willing(tit_fuck) and the_person.has_large_tits:
                                call kaya_get_coffee_titfuck(the_person) from _call_kaya_get_coffee_titfuck_1
                            "Finish up":
                                "You decide not to just leave her to her work for now."
                $ the_person.apply_planned_outfit(show_dress_sequence = True)
            else:   #Sad path where we can't see her milking herself.
                the_person "Sorry, the boss says I have to go to the back to do this..."
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title!c] steps away and out of sight."
                $ clear_scene()
                "She is gone for a minute, as she expresses milk into your coffee..."
                $ the_person.change_arousal(20)
                "Eventually, she emerges from the back room with your cup in hand."
                $ the_person.draw_person()
                the_person "Here you go, [the_person.mc_title]!"
                "She sets your coffee on the counter. It swirls a bit and is a pleasingly light brown, a mixture of the coffee and her fresh breastmilk."
            menu:
                "Leave a tip":
                    "You drop an extra $5 in the tip jar."
                    $ mc.business.change_funds(-5, stat = "Food and Drinks")
                    the_person "Aww, thank you!"
                    $ the_person.change_love(2, 30)
                "No tip":
                    pass

            "You sit down at a table and enjoy the fresh brew. The mixture of sweet breast milk and bitter coffee tastes great and really perks you up."
            $ mc.change_energy(60)  #Breast milk doubles energy gain from coffee because fuck yeah.

    return

label kaya_get_coffee_blowjob(the_person):
    mc.name "Damn that was hot. Maybe you could repay the favour and milk me with that hot mouth of yours?"
    "[the_person.possessive_title!c] quickly looks around the shop and bites her lip."
    the_person "Let's do it! Come around the counter."
    "You waste no time. As you step around the counter, [the_person.title] gets on her knees."
    $ the_person.draw_person(position = "blowjob")
    "As you pull out cock, she urges you on."
    the_person "I'm going to try and work fast, I'm not technically on break right now, okay?"
    mc.name "Sounds great. I'll try to keep and out for anyone that... aahhhhh"
    "[the_person.possessive_title!c] opens her mouth and eagerly slides your cock into her mouth."
    $ mc.change_arousal(20)
    "You reach down and help hold her hair as her hot little mouth starts to work over your erection."
    "Her tongue slithers back and forth across the tip for a moment, enjoying your precum, and then she leans forward and takes your full length again."
    $ mc.change_arousal(20)
    "Loud slurping and sucking noises come from behind the checkout counter as she sucks you off."
    "You glance around the shop and see a couple people looking your way, realizing what is going on, but no one seems bothered by it."
    "One guy by himself in the corner even gives you a thumbs up while [the_person.title] sucks your cock in the middle of the shop."
    call fuck_person(the_person, private = False, skip_intro = True, start_position = blowjob, start_object = make_floor(), position_locked = True, skip_condom = True ) from _call_blowjob_kaya_public_coffeeshop_1
    "Finished, you put your cock away while [the_person.title] licks her lips."
    $ the_person.draw_person(position = "stand2")
    mc.name "Thank you for the excellent service [the_person.fname]."
    the_person "Of course... please enjoy your coffee!"
    "You step back around the counter and pick up your coffee as she tries to straighten out her uniform."
    return

label kaya_get_coffee_titfuck(the_person):
    mc.name "Damn, your tits are amazing. Wish I could feel them wrapped around my cock right now."
    "[the_person.possessive_title!c] quickly looks around the shop and bites her lip."
    the_person "Why don't you come around the counter and maybe we can make that happen!"
    "You waste no time. As you step around the counter, [the_person.title] gets on her knees."
    $ the_person.draw_person(position = "blowjob")
    if not the_person.tits_available:
        "She pulls off her top, giving you full access."
        $ the_person.strip_to_tits(position = "blowjob")
    "As you pull out cock, she urges you on."
    the_person "I'm going to try and work fast, I'm not technically on break right now, okay?"
    mc.name "Sounds great."
    "[the_person.possessive_title!c] puts her hands on the sides of her breasts, then leans forward."
    "She squeeze her tits together as your cock slides between them, their soft flesh feels amazing wrapped around your length."
    $ mc.change_arousal(20)
    "She bounces her tits up and down a couple times, then stops. She lets a large dollop of saliva fall from her mouth, coating the tip of your erection."
    "She rubs it up and down a few times, and you can feel the friction level reduce and your cock starts to slide easily between her tits."
    if the_person.lactation_sources >= 5:
        "Squeezing her tits together causes them to start leaking again."
    $ mc.change_arousal(20)
    "You glance around the shop and see a couple people looking your way, realizing what is going on, but no one seems bothered by it."
    "One guy by himself in the corner even gives you a thumbs up while [the_person.title] sucks your cock in the middle of the shop."
    call fuck_person(the_person, private = False, skip_intro = True, start_position = tit_fuck, start_object = make_floor(), position_locked = True, skip_condom = True ) from _call_tit_fuck_kaya_public_coffeeshop_1
    "Finished, you put your cock away while [the_person.title] looks up at you for a moment."
    the_person "Is that what you were thinking about? When you milking them?"
    mc.name "Mmm, indeed."
    "[the_person.title] slowly stands up."
    $ the_person.draw_person(position = "stand2")
    mc.name "Thank you for the excellent service [the_person.fname]."
    the_person "Of course... please enjoy your coffee!"
    "You step back around the counter and pick up your coffee as she tries to straighten out her uniform."
    return

label kaya_office_fuck_label(the_person):
    # $ kaya.set_event_day("work_fuck_last_day")    #This was copy pasted from old code... I don't think it is used for anything anymore?
    "You step closer to [the_person.title] and rub your hand on her ass."
    mc.name "Then let's get to my office. I think we are both overdue for a break."
    the_person "Mmm, lead the way!"
    $ mc.change_location(ceo_office)
    "You step into your office with [the_person.possessive_title], then close and lock the door."
    menu:
        "Bend her over your desk" if the_person.is_willing(bent_over_breeding) and the_person.wants_creampie:
            "Alone with [the_person.title] you waste no time in bending her over your desk."
            $ the_person.draw_person(position = bent_over_breeding.position_tag)
            $ the_person.strip_to_vagina(position = bent_over_breeding.position_tag, prefer_half_off = True)
            "You step to the side and get into position behind [the_person.title]. You run your cock up and down her slit a couple times, getting the tip nice and wet."
            "You slowly push into her. She reaches back and grabs your leg, urging you forward as her cunt stretches to receive you."
            "She urges you in between moans."
            the_person "That's it! MMfff... Now don't stop until you fill me up...! YES!"
            call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), skip_intro = True, skip_condom = True, private = True) from _call_fuck_person_kaya_work
            $ report_log = _return
            $ the_person.draw_person(position = "standing_doggy")
            if report_log.get("creampies", 0) > 0 and report_log.get("girl orgasms", 0) > 0:
                "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
                "Your cum is dripping down the inside of her legs."
                call sex_review_trance(the_person) from _call_sex_review_trance_kaya_work_fuck
            elif report_log.get("girl orgasms", 0) > 0:
                "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
            else:
                "When you step back, [the_person.possessive_title] sighs happily."
        "Mess around":
            the_person "Well... what was it you wanted me all alone for again?"
            "She smiles mischievously as you close the gap between you two."
            call fuck_person(the_person, private = True) from _call_fuck_kaya_alone_in_office_01
            $ the_person.call_dialogue("sex_review", the_report = _return)
    $ the_person.draw_person()
    "You get yourself dressed and sit down at your desk."
    the_person "That was nice... I'm going to get back now?"
    mc.name "Sounds good, I'm going to stay here."
    "You enjoy the show as [the_person.possessive_title] gets dressed."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and leaves your office."
    $ clear_scene
    return

label kaya_study_room_fuck_label(the_person):
    "You step closer to [the_person.title] and rub your hand on her ass."
    mc.name "I'm pretty sure I have something you could study for a while. Why don't we get a study room."
    $ the_person.change_arousal(15)
    the_person "Mmm, okay! Follow me!"
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_location(university_study_room)
    "You follow [the_person.possessive_title] into the study room. Once inside she turns and locks the door."
    $ the_person.draw_person()
    menu:
        "Pin her to the wall" if the_person.is_willing(against_wall) and the_person.wants_creampie:
            "Alone with [the_person.title] you waste no time in pushing her up against the wall."
            the_person "So what did you have... WHOA!"
            $ the_person.draw_person(position = against_wall.position_tag)
            if not the_person.vagina_available:
                "You forcefully pull away her clothing."
                $ the_person.strip_to_vagina(position = against_wall.position_tag, prefer_half_off = True)
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(50)
            "You pin [the_person.title] into position against the wall. You run your cock up and down her slit a couple times, getting the tip nice and wet."
            "You slowly push into her. She grabs your back and wraps one leg around you, urging you to push deeper."
            "She moans as you bottom out inside her."
            the_person "Ohhhhh fff... God don't stop until you fill me up please!"
            call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = True, private = True) from _call_fuck_person_kaya_class_01
            $ report_log = _return
            $ the_person.draw_person(position = against_wall.position_tag)
            if report_log.get("creampies", 0) > 0 and report_log.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] clings to you, her legs are shaky."
                the_person "That was... just give me a moment..."
                "After several seconds, her legs drop and you are able to let her stand on her own."
                $ the_person.draw_person()
                call check_date_trance(the_person) from _call_check_date_trance_kaya_class_fuck
            elif report_log.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c]'s legs are shaking as she tries to stand by herself."
            else:
                "When you step back, [the_person.possessive_title] sighs happily."
        "Mess around":
            the_person "Well... what was it you wanted me all alone for again?"
            "She smiles mischievously as you close the gap between you two."
            call fuck_person(the_person, private = True) from _call_fuck_kaya_alone_in_class_01
            $ the_person.call_dialogue("sex_review", the_report = _return)
    $ the_person.draw_person()
    "You and [the_person.title] start to get yourselves dressed."
    the_person "That was nice... Oh SHIT. I'm late for class!"
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "I gotta go, can you close the door on your way out?"
    mc.name "Of course."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and leaves you in the study room."
    $ clear_scene
    "Once you are decent, you step out and back to the university."
    $ mc.change_location(university)
    return

