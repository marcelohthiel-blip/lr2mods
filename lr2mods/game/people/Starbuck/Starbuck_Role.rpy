label sex_shop_unlock_label():
    "While reading the local newspaper on your phone, you notice an advertisement for a new adult store close to the mall."
    "Perhaps you should check it out and see if you can find some toys or clothing for your employees."
    $ unlock_sex_shop_and_starbuck()
    return

#SBS10
label starbuck_vaginal_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at vaginal sex. You ask if she has any tips or products for further improvement, even if it's temporary."
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title!c] leads you over to an area of the store where she sells a number of cock rings."
    the_person "Personally, I recommend this one."
    "[the_person.possessive_title!c] picks one off the shelf, it looks like it has a number of features, like vibration and heat."
    "It looks like a good buy, but unfortunately it has a built-in battery that cannot be recharged. Once it's done, it's done!"
    menu:
        "Purchase ($500)":
            $ mc.business.change_funds(-500, stat = "Sex Toys")
            $ perk_system.add_stat_perk(Stat_Perk(description = "Cock ring that increases pleasure during vaginal sex. Lasts one week. +2 Vaginal skill", vaginal_bonus = 2, bonus_is_temp =True, duration = 7), "Vibrating Cock Ring")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 70:
                "[the_person.possessive_title!c] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Fuck her":
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, it's only fair you be the first to feel it."
                        the_person "Ah... I can't wait! Let's go!"
                        $ mc.change_locked_clarity(50)
                        "She quickly takes off some clothes to give you easy access and hops on the counter."
                        $ the_person.strip_to_vagina(prefer_half_off = True, position = "stand3")
                        call fuck_person(the_person, start_position = missionary, start_object = make_counter(), skip_intro = True) from _call_fuck_person_SBS10
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 1:
                            the_person "Oh wow... I've never... I came so many times..."
                            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 60)
                            the_person "Let's do that again soon!"
                        elif the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... The orgasms that thing gives..."
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 60)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS20
label starbuck_anal_skillup_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    "You explain to [the_person.possessive_title] that you feel like you need something to help take anal sex to the next level. You ask if she has any tips or products for further improvement, even if the benefits are temporary."
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title!c] leads you over to an area of the store where she sells a number of lubrications."
    the_person "You see [the_person.mc_title], the key to great anal sex, is using the perfect lube!"
    the_person "Personally, I recommend this one."
    "[the_person.possessive_title!c] picks one off the shelf."
    the_person "This company has made a ton of advances in lube technology recently."
    the_person "This one has full effectiveness with just a small application, and is designed to both lubricate, {i}and{/i} increases blood flow to the nerve endings, making anal more pleasurable for the receiver!"
    menu:
        "Purchase ($800)":
            $ mc.business.change_funds(-800, stat = "Sex Toys")
            $ perk_system.add_stat_perk(Stat_Perk(description = "Sensitizing and highly effective anal lubricant. Lasts one week. +2 Anal Skill", anal_bonus = 2, bonus_is_temp =True, duration = 7), "Perfect Anal Lube")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 90:
                "[the_person.possessive_title!c] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Fuck her ass":
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, it's only fair I use it on you first!"
                        the_person "Ah... I can't wait! Let's go!"
                        $ mc.change_locked_clarity(50)
                        "She quickly takes off some clothes to give you easy access, turns around and bends over the counter."
                        $ the_person.strip_to_vagina(prefer_half_off = True, position = "stand3")
                        call fuck_person(the_person, start_position = anal_standing, start_object = mc.location.get_object_with_name("counter"), skip_intro = True) from _call_fuck_person_SBS20
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 1:
                            the_person "Oh wow... I've never... I came so many times!"
                            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 70)
                            the_person "Let's do that again soon!"
                        elif the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... I came so hard!"
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 70)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS30
label starbuck_oral_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at oral sex. You ask if she has any tips or products for further improvement, even if the effects are temporary."
    the_person "Oh [the_person.mc_title]... I think I can probably help you with that!"
    "[the_person.possessive_title!c] leads you over to an area of the store where she sells a number of balms and oils."
    "She picks a balm up off the shelf. It looks like it's some kind of lip balm, but it's designed to increase blood flow and pleasure to female partners genitals it comes into contact with."
    the_person "Personally, I recommend this one."
    menu:
        "Purchase ($250)":
            $ mc.business.change_funds(-250, stat = "Sex Toys")
            $ perk_system.add_stat_perk(Stat_Perk(description = "Lip balm that feels good when you go down on women. Lasts one week. +2 Oral Skill", oral_bonus = 2, bonus_is_temp =True, duration = 7), "Stimulating Lip Balm")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 45:
                "[the_person.possessive_title!c] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Eat her pussy":
                        mc.name "Sounds good, [the_person.title]."
                        the_person "Ah yes!"
                        "She quickly takes off some clothes to give you easy access and leans against her counter."
                        $ mc.change_locked_clarity(25)
                        $ the_person.strip_to_vagina(prefer_half_off = True, position = "stand3")
                        call fuck_person(the_person, start_position = cunnilingus, start_object = mc.location.get_object_with_name("floor"), skip_intro = True) from _call_fuck_person_SBS30
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 1:
                            the_person "Oh my god, I came so many times... did you make me squirt?"
                            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 30)
                            the_person "Let's do that again soon!"
                        elif the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... That felt so good!"
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 30)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."
                        "You head back to your house and watch the video. You pick up several new tips and tricks to try next to eat a girl out!"

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS40
label starbuck_foreplay_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at foreplay. You ask if she has any tips or products for further improvement, even if it's only temporary."
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title!c] leads you over to an area of the store where she sells a number of sex toys."
    the_person "Personally, I recommend this one."
    "[the_person.possessive_title!c] picks a small vibrator off the shelf. It looks like it has a number of features, like vibration and heat."
    menu:
        "Purchase ($100)":
            $ mc.business.change_funds(-100, stat = "Sex Toys")
            $ perk_system.add_stat_perk(Stat_Perk(description = "Small, finger mounted vibrator. Increases foreplay skill. Lasts one week. +2 Foreplay Skill", foreplay_bonus = 2, bonus_is_temp =True, duration = 7), "Small Finger Vibrator")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 30:
                "[the_person.possessive_title!c] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Grope her":
                        $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, it's only fair you be the first to feel it."
                        the_person "Ah... I can't wait! Let's go!"
                        $ mc.change_locked_clarity(15)
                        "She quickly takes off some clothes to give you easy access."
                        $ the_person.strip_to_vagina(prefer_half_off = True, position = "stand3")
                        call fuck_person(the_person, start_position = standing_grope, skip_intro = True) from _call_fuck_person_SBS40
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... The orgasms that thing gives..."
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 20)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

label starbuck_sex_store_investment_one_label(the_person):
    mc.name "So, I'm seriously considering investing in your shop. What kind of stock can you get if I invest $1000?"
    the_person "Oh! That would be amazing! Well, with that money, I could get basic toys, creams, and lubricants. There are some pretty good creams for male endurance enhancement you can get..."
    the_person "As well as some toys for better foreplay and masturbation. Some dildos, male masturbation sleeves, vibrating rings..."
    "That sounds like a pretty good list of stuff that you would be interested in buying if you were to go to a sex shop."
    "Do you want to invest?"
    menu:
        "Invest ($1000)":
            "You discuss with [the_person.possessive_title] for a while what the terms of your investment are. Once you are both happy, you write her a check from your business account."
            $ mc.business.change_funds(-1000, stat = "Investments")
            $ the_person.change_stats(obedience = 5, happiness = 20)
            the_person "Don't worry, [the_person.mc_title]! You won't regret this!"
            "Even if the business winds up flopping, in your heart you know you are doing the right thing, helping this widow achieve her dream of owning a sex shop."
            $ starbuck.event_triggers_dict["shop_investment_total"] += 1000
            $ starbuck.event_triggers_dict["shop_investment_basic_total"] += 1000
            $ starbuck.event_triggers_dict["shop_progress_stage"] = 1
            $ starbuck.event_triggers_dict["shop_investment_rate"] = 1.0
            $ starbuck.set_event_day("shop_stage_one_day")
            $ add_starbuck_coffee_time_action()
            $ add_starbuck_no_profit_action()
            $ add_starbuck_foreplay_enhancer_action()
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title!c] frowns, but she nods in understanding."
            the_person "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard-earned money!"
    return

label starbuck_sex_store_investment_two_label(the_person):
    "While things at [the_person.possessive_title]'s sex shop have definitely picked up, you can't help but notice there are several sections of the store that lack variety."
    "There are some dildos, but only a couple varieties. Same with condoms, lubricants, and other items."
    "You decide to bring it up with [the_person.possessive_title]."
    mc.name "Hey [the_person.title]. I see things are going good around here, but I'm curious. You've got basic items around the store, but why don't you have more variety?"
    "She frowns and responds."
    the_person "Well, I'd love to have more variety, but unfortunately I'm not bringing in very much profit. I'm in the black now, thanks to your investment, but I'm not really making enough to expand inventory significantly."
    "You watch as a customer comes in the store. He looks around for a bit, then leaves. You wonder how much business you are missing out on due to the lack of stock."
    mc.name "Have you done any research on what it would take to get more variety in?"
    "She nods."
    the_person "I have. And it's too much for me to ask from you. You've already done so much for me and shop..."
    "You interrupt her."
    mc.name "How much?"
    "[the_person.possessive_title!c] clears her throat."
    the_person "Well, the way I added it up, to expand beyond just basic stock, and include a variety of novelty items, edibles, and accessories would be about $5000."
    "You consider the amount. It is steep, to be sure, but it also might be a good investment."
    if get_shop_promo_stage() == 3.0:
        "It might also open up new opportunities with [the_person.possessive_title]. You wouldn't mind a few more excuses to get intimate with her..."
    "Do you want to invest?"
    menu:
        "Invest ($5000)":
            "You discuss with [the_person.possessive_title] for a while what the terms of your investment are. Once you are both happy, you write her a check from your business account."
            $ mc.business.change_funds(-5000, stat = "Investments")
            $ the_person.change_stats(obedience = 5, happiness = 20, love = 5)
            the_person "Wow... are you really doing this? I can hardly believe it. Don't worry, I won't let you down!"
            "Even as you write your check, she is already going on about the stock she'll be able to get."
            the_person "... hmmm... OH! And edible underwear! And nipple clamps! Maybe some handcuffs..."
            $ mc.change_locked_clarity(20)
            $ starbuck.event_triggers_dict["shop_investment_total"] += 5000
            $ starbuck.event_triggers_dict["shop_investment_advanced_total"] += 5000
            $ starbuck.event_triggers_dict["shop_progress_stage"] = 2
            "She is so excited, you can tell already, this is an investment that is going to pay off for you... one way or another!"
            $ starbuck.set_event_day("shop_stage_two_day")
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title!c] frowns, but she nods in understanding."
            the_person "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard-earned money!"
    return

label starbuck_sex_store_investment_three_label(the_person):
    "You take a look around at the sex shop. You see a sexy looking redhead checking out some lingerie. In the back corner is a guy looking at strap-ons. In an aisle you see a couple looking at edibles."
    "Everyone seems to be shopping and finding what they are looking for... but you can't help but have a nagging in you head that you could make the store even better."
    mc.name "Hey [the_person.title]. Looks like things are going great here, how is business?"
    the_person "Oh, it's been great! I've been meeting so many new people, and I'm actually making a decent income now!"
    "She gives you a warm smile. It nice seeing her so happy with her work."
    mc.name "Are you pretty happy with all the stuff you are able to keep in stock now? Seems like you've got just about anything you could ever need."
    the_person "Well, I don't know about EVERY thing, but we definitely have a great selection now."
    mc.name "What do you mean?"
    the_person "Well, goodness, there is so much stuff out there, there's no way we could fit it all in this little store. That's why I'm saving up."
    the_person "The store next to us recently went out of business, once I save up enough money, I'm gonna buy it out and expand my store. Turn this place into [the_person.fname]'s MEGA sex shop!"
    "You consider what she is saying."
    mc.name "What kind of stuff could you carry with the extra space that you aren't carrying now?"
    the_person "Oh, well in here we sell mostly accessories, lingerie, that kind of thing, but with more room we could get in all kinds of kinky stuff. Sex furniture, like chairs and swings, massage tables..."
    "Wow, you had no idea there was so much stuff out there..."
    the_person "... could even get into bondage gear, fetish items like furry tail butt plugs... I mean, the sky is the limit, you know?"
    "So far, all of your investments in the shop have paid off... plus, you start to imagine what it would be like to try some of these items with [the_person.possessive_title]..."
    mc.name "Let's say I was interested in investing again... How much would you need to make all that happen?"
    "[the_person.possessive_title!c]'s mouth drops in surprise."
    the_person "Well... my estimates put it at about $15000. But please, don't think you have to do that! I'm making decent money, I'll be able to afford it eventually..."
    "You consider the investment."
    menu:
        "Invest ($15000)":
            mc.name "How about this. You've done an incredible job managing this place. How about if I front the money, and from now on we're partners?"
            the_person "Wow... partners?... I mean... you're talking business partners, right?"
            if get_shop_promo_stage() > 3.0:
                mc.name "[the_person.title], I'd be lying if I said I don't thoroughly enjoy the time we've spent together. So yeah, we would be business partners, but I'd also love the excuse to spend more time with you."
                $ the_person.draw_person(emotion = "happy")
                if starbuck.love > 60:
                    the_person "Oh, [the_person.mc_title]... I'm so glad to hear that. I feel the same way."
                else:
                    the_person "Wow... that's nice to hear! I'm interested in spending more time with you in the future too."
            else:
                mc.name "Of course, we'll keep things perfectly professional..."
            $ mc.business.change_funds(-15000, stat = "Investments")
            $ the_person.change_stats(obedience = 10, happiness = 20, love = 10)
            the_person "Wow... this is it! The opportunity of a lifetime. I'm speechless [the_person.mc_title]. Thank you so much!"
            "Even as you write your check, she is beginning to plan the expansion to the shop."
            $ starbuck.event_triggers_dict["shop_investment_total"] += 15000
            $ starbuck.event_triggers_dict["shop_investment_fetish_total"] += 15000
            $ starbuck.event_triggers_dict["shop_progress_stage"] = 3
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title!c] frowns, but she nods in understanding."
            the_person "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard-earned money!"
    return

init 2 python:
    def starbuck_promo_classic_black_lingerie():
        outfit = Outfit("Lingerie Set Classic Black")
        outfit.add_upper(lace_bra.get_copy(),colour_black)
        outfit.add_lower(lace_panties.get_copy(), colour_black)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_black)
        outfit.add_feet(high_heels.get_copy(), colour_black)
        return outfit

    def starbuck_promo_blue_nightgown_lingerie():
        outfit = Outfit("Lingerie Set Blue Nightgown")
        outfit.add_upper(nightgown_dress.get_copy(), colour_sky_blue)
        outfit.add_lower(cute_panties.get_copy(), colour_sky_blue)
        outfit.add_feet(thigh_highs.get_copy(),colour_sky_blue)
        outfit.add_feet(sandal_heels.get_copy(), colour_sky_blue)
        return outfit

    def starbuck_promo_pink_onepiece_lingerie():
        outfit = Outfit("Lingerie Set Pink Onepiece")
        outfit.add_upper(lacy_one_piece_underwear.get_copy(),colour_pink)
        outfit.add_feet(fishnets.get_copy(), colour_pink)
        outfit.add_feet(pumps.get_copy(), colour_pink)
        return outfit

#SBS70

#SBS120
label starbuck_spend_the_night_label(the_person): #You spend the night at her place. You'll probably get busy
    mc.name "I was thinking I could spend the night here tonight."
    "[the_person.title] looks delighted."
    the_person "Oh! That would be great! I'd love the company!"
    $ ran_num = renpy.random.randint(0,100)
    if ran_num < 10 or mc.energy < 30: #No event, just cuddle up and go to bed.
        mc.name "Thanks. It's been a long day and I'm exhausted."
        $ the_person.change_to_bedroom()
        "You strip off your work clothes, down to your boxers. You head to [the_person.title]'s bedroom and hop in her bed."
        the_person "I'll be in in a minute!"
        "You see [the_person.title] step into the bathroom. In a few minutes she emerges, ready for bed."
        $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(sluttiness_min = 10, guarantee_output = True))
        $ the_person.draw_person()
        "She crawls into bed beside you. You cuddle up behind her and enjoy the warmth of her body as you drift off to a restful night's sleep."
    elif ran_num < 40: #She seduces you
        mc.name "Thanks. I just have a little bit of work stuff to finish up. I brought my laptop, mind if I take over your desk for a few?"
        the_person "Help yourself! I'll tell you what, I'm going to hop in the shower."
        "You sit down at the desk and pull out your laptop. You review some of the days research notes and begin emailing instructions for tomorrow."
        "You make note of a couple issues serum production, so write yourself a reminder to talk with an employee tomorrow about it..."
        "You delve into your work emails for a while longer, totally forgetting you are at [the_person.title]'s house. You are vaguely aware when you feel her coming up behind you."
        "Your mind is brought immediately back to the present when you feel the heavenly sensation of [the_person.title]'s warm, soft tit flesh on the back of your neck as she wraps her arms around you from behind."
        mc.name "Mmm, that feels great..."
        $ mc.change_locked_clarity(20)
        "She runs her hands up and down your chest, slowly unbuttoning your shirt. You lean your head back, your neck nestled between her amazing tits."
        "[the_person.title] begins to move her chest up and down slightly, rubbing her breasts along your neck and shoulders."
        the_person "Are you about at a stopping point?"
        mc.name "Yes, definitely."
        "You close your eyes and enjoy the sensations. [the_person.title]'s hands move lower down your belly and begins to stroke you through your pants."
        "She expertly begins to unbuckle your belt, and undoes your pants. You sigh when she puts one hand down your underwear and begins to jack you off slowly. She whispers into your ear."
        the_person "Come on... let's go to bed."
        $ the_person.apply_outfit(Outfit("Nude"))
        $ the_person.draw_person(position = "back_peek")
        "She backs away from you and walks into her bedroom. You turn and watch her, seeing she is completely naked."
        $ the_person.change_to_bedroom()
        "You quickly follow her."
        $ the_person.draw_person(position = "stand4")
        "[the_person.title] stops when she gets to the bed and turns to you."
        the_person "Lay down... there's something I want to do..."
        $ the_person.draw_person(position = "standing_doggy")
        "You nod. You take off what is left of your clothes and lay down. You watch [the_person.title] rummage through her nightstand. Her ass wiggles back and forth, right in front of you."
        $ mc.change_locked_clarity(30)
        $ play_spank_sound()
        "*{b}SMACK{/b}*"
        "You reach up and give her ass a firm spank. She gives a sigh."
        the_person "Ah! Here it is..."
        $ mc.change_arousal(10)
        $ the_person.draw_person(position = "stand4")
        "She stands up and you see that she is holding a bottle of anal lubricant. You feel your dick twitch when you realise what she has in mind."
        "She squirts some of it out onto your cock and works her hand up and down you a few times. Then she squirts a bit more into her hand and then reaches back to her ass."
        "[the_person.title] gives another gasp as you imagine she works a bit of the lube into her tight hole."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.possessive_title!c] climbs up on top of you. She takes you in her hand and points it towards her back passage."
        the_person "Oh god, [the_person.mc_title], it's so big! Okay, here we go..."
        $ mc.change_arousal(10)
        "[the_person.possessive_title!c] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
        #Fuck her#
        call fuck_person(the_person, start_position = anal_cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_SBS120
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh god, I came so hard..."
            $ the_person.draw_person(position = "missionary")
            "[the_person.possessive_title!c] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
        else:
            the_person "Mmm, that was so good, thank you [the_person.mc_title]..."
            $ the_person.draw_person(position = "missionary")
            "[the_person.possessive_title!c] rolls off you and lays down on the bed next to you."
        "[the_person.title] doesn't bother to get up, she just cuddles up next to you."
        the_person "Thanks, [the_person.mc_title], I needed that so bad."
        "She stretches her arms out and yawns."
        the_person "I'm worn out! Goodnight!"
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex-induced haze, you quickly drift off to sleep with her."
    elif ran_num < 70 or mc.energy < 60: #You seduce her
        $ the_person.draw_person(position = "kissing")
        "[the_person.possessive_title!c] wraps her arms around you to give you a hug. You use the opportunity."
        "You grab her ass and pick her up easily. She yelps for a second but quickly wraps her legs around you in an embrace."
        "Your lips meet and you begin to kiss her hungrily. She returns your kiss. You pull her tight against you and begin to grind your needy cock up against her."
        $ the_person.change_arousal(5)
        $ mc.change_locked_clarity(20)
        "She breaks the kiss for a second."
        the_person "Oh [the_person.mc_title], I missed you too."
        "[the_person.possessive_title!c] clings to you and begins to kiss your neck eagerly. You carefully carry her towards her bedroom."
        $ the_person.change_to_bedroom()
        $ the_person.draw_person(position = "missionary")
        "When you get to her bed, you roughly throw her down on it."
        if the_person.vagina_available and the_person.tits_available:
            "You stop for a second and admire [the_person.title], her body on display in front of you. You guess she walks around the house like this?"
        else:
            "Your mind hazy with lust, you begin to pull [the_person.title]'s clothes off."
            $ the_person.strip_outfit(position = "missionary")
            "Now naked, you stop for a second and admire [the_person.title]'s incredible body."
        $ mc.change_locked_clarity(30)
        "Before you go any further, you decide to make sure that [the_person.title] is wet and ready for you. You pull her over so her legs are hanging off the edge of the bed and get down on your knees in front of her."
        "She spreads her legs instinctively as you begin to kiss along her knee. You trail wet kisses along the inside of her thigh, working your way farther up."
        "When you reach her cunt, you waste no time, pushing your tongue between her lips and running it up and down her delicious slit."
        "[the_person.title] moans and begins to run her hands through your hair. When you push your tongue up inside her he gently urges you deeper."
        $ the_person.change_arousal(10)
        "You reach forward with your hands and grasp her tits. You roll her nipples in your fingers for a second causing her moans to grow louder."
        "You lick circles around her clit, then close your mouth over and gently suck on it."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        the_person "Oh! Baby I'm ready, come fuck me!"
        call fuck_person(the_person) from _call_fuck_person_SBS121
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh god, I came so hard..."
        else:
            the_person "Mmm, that was so good, thank you [the_person.mc_title]..."
        "You lay down on the bed, hopping in the covers."
        "[the_person.title] doesn't bother to get up, she just cuddles up next to you."
        the_person "Thanks, [the_person.mc_title], I didn't know I needed that until you got here."
        "She stretches her arms out and yawns."
        the_person "You wore me out! Goodnight!"
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex-induced haze, you quickly drift off to sleep with her."

    else: # You both want it, and MC has stamina for a wild ride
        "She gives you a flirty smile."
        the_person "I'm kinda sweaty from a long day at the shop, so I was just getting ready to hop in the shower. Why don't you get comfortable? I won't be long."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] turns and walks into her bathroom. She closes the door... mostly... leaving it open a crack. You're sure she left it open on purpose, but you decide for now to let her get started solo."
        $ clear_scene()
        "You head into her kitchen and notice her coffee pot is on and full. Was she expecting you? You pour yourself a cup and take a few sips."
        "You sit down and enjoy your coffee. It has been about 5 minutes now. The crack in the door is calling you. Should you join her in the shower? Or let her finish?"
        menu:
            "Shower with her":
                $ the_person.apply_outfit(Outfit("Nude"))
                $ mc.change_location(home_shower)
                "You decide you've waited long enough and make your way into the bathroom. Inside you smell the scent of lavender body wash and quickly spy [the_person.title]'s soapy body through the hazy steam."
                $ the_person.draw_person(position = "back_peek")
                $ mc.change_locked_clarity(30)
                mc.name "Have room for me in there?"
                the_person "Of course! I was hoping you would join me..."
                "You strip down and enter the shower. [the_person.fname] gives you a turn under the hot running water."
                the_person "Great timing... can you wash my back?"
                $ mc.change_arousal(10)
                "She hands you her loofah and you begin to work circles up and down her back. The soap bubbles make her already smooth skin slick and soft."
                "When her back is all soapy, you reach over her shoulder and hand the loofah back to her. You put your other hand against her hip and slowly pull her back against you."
                "You now wrap your arms around her from behind, and she melts back into you. Your hands roam her body but quickly begin to grope her generous bosom, while she wiggles her ass back against you."
                $ mc.change_locked_clarity(20)
                the_person "Mmm, I'm glad we're thinking the same thing. I'm really hungry for you tonight, [the_person.mc_title]!"
                "You whisper into her ear."
                mc.name "Is that so? I don't believe you... Why don't you show me."
                $ mc.change_arousal(10)
                if the_person.obedience > 110:  #She gets on her knees#
                    "[the_person.title] chuckles."
                    the_person "Mmm, for you, [the_person.mc_title]? I'll do just about anything..."
                    $ the_person.draw_person(position = "blowjob")
                    "[the_person.possessive_title!c] turns to you and gets down on her knees. She looks up at you. Her eyes certainly look a bit hungry..."
                    "She puts her hands on her breasts. She leans forward and nestles your cock between her bountiful tits."
                    call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBS122
                    "You spend a moment recovering while [the_person.title] rinses your cum off her body."

                else:                           #She gets Feisty
                    "[the_person.title] chuckles and pushes her ass back against you."
                    the_person "Mmm, I have a better idea..."
                    "[the_person.possessive_title!c] leans forward a bit, against the shower wall. She reaches back and grabs your hardness, pointing it down towards her slit."
                    the_person "Why don't you just push it in... I'm ready for it, I promise..."
                    "You decide to go for it. She has you lined up, so you slowly push yourself forward inside her."
                    the_person "Oh my god..."
                    "[the_person.possessive_title!c] sighs as you bottom out."
                    "She wiggles her ass back and forth a few times, enjoying the familiar feel of fullness you give her when you fuck her."
                    call fuck_person(the_person, start_position = standing_doggy, start_object = make_wall(), skip_intro = True, position_locked = True) from _call_sex_description_SBS123
                    "You spend a moment recovering while [the_person.title] rinses herself off."
                #TODO set outfit to regular nude again. She washed the cum off!
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.arousal = 50   #A hard setting of arousal... Did this to avoid an entry in the log. Not ideal code#
                $ the_person.draw_person(position = "stand2")
                "You both quickly finish showering. As you hop out, you quickly dry off and [the_person.title] takes your hand."
                the_person "Let's go to bed! I'm so charged tonight, I think I can go all night!"
                mc.name "Sounds good. I'm gonna fuck your brains out tonight."
                $ the_person.draw_person(position = "walking_away")
            #"Wait for her":  #TODO
        $ the_person.change_to_bedroom()
        "You follow [the_person.title] to her bedroom."
        "Her amazing ass sways back and forth as she walks. Your cock twitches thinking about the night ahead of you."
        "She gets to her bed and immediately opens her nightstand and begins looking for something."
        "She pulls out the strap-on dildo you helped her demonstrate for her advertisement and some anal lube and turns to you."
        $ the_person.draw_person(position = "stand4")
        $ mc.change_arousal(20)
        the_person "How about we give this another run? Last time we used it, the results were very good..."
        menu:
            "Agree":
                mc.name "Let's do it. I love fucking your tight little ass."
                $ the_person.draw_person(position = "blowjob")
                "[the_person.possessive_title!c] gets down on her knees in front of you and starts securing the strap-on."
                mc.name "Hey... while you're down there..."
                "[the_person.possessive_title!c] looks up at you and smiles. She sticks out her tongue and slithers it along your aching shaft, teasing you."
                $ mc.change_locked_clarity(20)
                the_person "Mmm... you taste so good. But I have other plans for this."
                "She squirts some lube into her hand and then gives you a couple strokes."
                the_person "Okay, you're ready, now it's my turn!"
                $ the_person.draw_person(position = "doggy")
                "[the_person.title] stands up and hands you the lube, then crawls up on the bed on all fours, presenting her ass to you. She gives her hips a little shake."
                the_person "Lube me up, [the_person.mc_title]. Don't be stingy!"
                "You squirt a generous amount of lube onto your fingers. You run your fingers along her ass crack, coating it in a glaze of lube."
                "You take a finger and begin to push it up against her sphincter. You can feel her physically force herself to relax and then your finger eases right in."
                $ mc.change_locked_clarity(50)
                the_person "Mmm... that feels good already. I think I'm getting better at this!"
                "You apply some more lube, then slowly push two fingers into her smooth back passage. You feel like she is ready for you."
                "You get into position behind her. She arches her back and presents her ass."
                "[the_person.possessive_title!c]'s pussy is already dripping with arousal. You line yourself up with her ass, while she reaches down and lines the dildo up with her pussy."
                $ mc.change_arousal(10)
                "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
                the_person "Oh my god! I'm so full... It's so good [the_person.mc_title]! Fuck me like you paid for this! Like I'm just a whore!"
                call fuck_person(the_person, start_position = doggy_anal_dildo_dp, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBS124
                "Finished with your anal plundering, you let yourself collapse onto [the_person.title]'s bed."
                "She cuddles up next to you."
                $ the_person.draw_person(position = "missionary", emotion = "happy")

            "Fuck her your way":
                mc.name "Not tonight. I have something different in mind."
                "[the_person.title] looks a little disappointed, but waits to see what you DO have in mind."
                call fuck_person(the_person) from _call_fuck_person_SBS125
                "Finished for the night, you let yourself collapse onto [the_person.title]'s bed."
                "She cuddles up next to you."
                $ the_person.draw_person(position = "missionary", emotion = "happy")

        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex-induced haze, you quickly drift off to sleep with her."

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_SBS129
    #Good morning!
    $ perk_system.add_stat_perk(Stat_Perk(description = "Temporary increased max energy after sleeping with a lover. +20 Energy Cap", energy_bonus = 20, bonus_is_temp = True, duration = 2, energy_cap = 20), "Overnight Lover")
    $ mc.change_location(the_person.home)

    $ clear_scene()
    if renpy.random.randint(0,100) < 50:        #Roll for morning sex is successful
        "[the_person.title]'s naked body against yours makes for a very pleasant night of sleep. A couple times throughout the night you stirred for a bit and gave her a grope, but quickly fell back asleep."
        "Pleasant sensations and the feeling of weight around your torso slowly wakes you up."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(30)
        $ the_person.draw_person(position = "cowgirl")
        "When you awaken, you discover that [the_person.title] is on top of you, with your morning wood already hilted inside her pussy."
        "You moan in appreciation at the wonderful wake-up call."
        $ mc.change_locked_clarity(50)
        the_person "Mmm... Good morning [the_person.mc_title]... When I woke up this morning you were poking me pretty good... I figured you wouldn't mind if I took it for a quick ride."
        "You murmur your acceptance. Her mesmerizing tits are bouncing up and down right in front of you. You take them both in your palms and give them a good squeeze."
        # call fuck_person(the_person, start_position = cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_SBS125
        call get_fucked(the_person, the_goal = "vaginal creampie", private= True, start_position = cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_get_fucked_starbuck_spend_the_night_01
        the_person "Mmmff. So good... I wish I could call in sick and we could fuck all day... but I need to get to the shop."
        $ the_person.draw_person(position = "stand3")
        the_person "I'm gonna go hop in the shower. Feel free to let yourself out! Thanks for spending the night [the_person.mc_title]!"
        "[the_person.title] slowly gets up and heads to the bathroom. You grab your stuff and head out."
    else:                                    #No morning sex
        "You wake up in the next morning after sleeping soundly the night before. As your stir it wakes up your bedwarmer, [the_person.title]. She yawns and stretches."
        "Slowly, [the_person.title] yawns and sits up at the side of the bed."
        $ the_person.draw_person(position = "sitting")
        the_person "Good morning, sleepyhead! Wow, I slept so good last night... you really wore me out!"
        "You chat for a few minutes, enjoying the warmth of her bed, until she gets up."
        $ the_person.draw_person(position = "stand3")
        the_person "I'm gonna go hop in the shower. Feel free to let yourself out! Thanks for spending the night [the_person.mc_title]!"
        "[the_person.title] heads to the bathroom. You grab your stuff and head out."
    $ mc.change_location(downtown)
    $ the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = 0.4))
    $ clear_scene()
    return "Advance Time"

#SBS130
label starbuck_close_up_label(the_person): #You offer to help her close up. Mainly a chance to give her serum, also can screw around at higher sluttiness settings.
    mc.name "Can I help you close up tonight?"
    the_person "Oh! That would be great! I really appreciate it [the_person.mc_title]. I suppose it is about closing time..."
    "You continue to chat with her for a while, until it reaches the regular closing time. [the_person.title] locks the front door."
    the_person "I noticed earlier we had some pretty good lube sales. I think I'm going to bring out some boxes from the back. Want to help me restock?"
    mc.name "Sure! I can do that. Got anything to drink around here?"
    the_person "I have a mini fridge behind the counter. I have beer, some bottled water, maybe a soda or two in there."
    mc.name "Nice. Want anything?"
    the_person "A beer sounds great!"
    $ the_person.draw_person(position = "walking_away")
    "You grab two beers from the fridge and pop the caps on both with a bottle opener magnet you find stuck to the front of the fridge."
    "[the_person.possessive_title!c] is in the back, you could probably drop some serum into her beer if you want to."
    menu:
        "Add some serum to her beer" if mc.inventory.has_serum:
            call give_serum(the_person) from _call_give_serum_SBS130
            if _return:
                "You double-check to make sure she is still in the back, then add the serum to [the_person.title]'s beer."
            else:
                "You think about adding a dose of serum to [the_person.title]'s beer, but decide against it."

        "Add some serum to her beer\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
            pass

        "Leave her beer alone":
            "You take a long sip of your drink, waiting until [the_person.title] returns."
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title!c] returns with several boxes and sets them down, then grabs the beer and takes a sip."
    "You help her with the boxes and start to unpack as you both enjoy your drinks and each other's company."
    "When the boxes are unpacked, you help her take the empty ones to the back and put them in the recycling."
    the_person "Thanks for your help."
    if the_person.sluttiness > 40 and the_person.energy > 50:
        the_person "Is there something... ANYTHING I can do to return the favour?"
        "She bats her eyelashes as she looks at you. She licks her lips as you notice she steals a glance between your legs..."
    else:
        mc.name "It's no problem. Take care!"
        "You say goodbye to [the_person.title] and head out."
        call advance_time() from _call_advance_time_starbuck_close_up_label_1
        return

    menu: #This menu is just to weed out if we don't want to have fun
        "Have some fun with her":
            pass
        "Some other time":
            mc.name "Honestly, I'm pretty tired out. Can I have a rain check?"
            "You can tell she is a little disappointed, but soon she is stretching and yawning."
            the_person "You know what?... I'm pretty tired too. Good night [the_person.mc_title]."
            "She walks you to the door of the business and you walk out together, before going your separate ways."
            call advance_time() from _call_advance_time_starbuck_close_up_label_2
            return
    mc.name "I can definitely think of something."
    the_person "Oh yeah? I hope it's the same thing I'm thinking..."
    $ mc.change_locked_clarity(10)
    menu:
        "Just mess around some":
            "You grab [the_person.possessive_title]. She wraps her arms around you."
            $ mc.change_arousal(20)
            call fuck_person(the_person, skip_intro = False, private = True) from _call_fuck_person_SBS131
            the_person "So... you'll help me close up every night, right?"
            mc.name "I'm sorry, I can't promise something like that, my business keeps me busy."
            the_person "Damn. A girl can dream though."
            $ the_person.change_love(3, 30)
        "Dress up for you" if get_shop_promo_stage() >= 2.0:
            call starbuck_replay_dressup_label(the_person) from _call_starbuck_replay_SBS132
        # "Play with a dildo for you" if get_shop_investment_rate() >= 3.0:   #TODO these options.
        #     pass
        # "Try more edible underwear" if get_shop_investment_rate() >= 4.0:
        #     pass
        # "Use whip and strap-on" if get_shop_investment_rate() >= 5.0:
        #     pass
        # "Anal on the swingset" if get_shop_investment_rate() >= 6.0:

    "[the_person.title] lets out a big yawn, while rearranging her clothes."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person()

    if the_person.is_in_trance:
        "[the_person.title] is tired and in a suggestible state, you can take a moment to train her."
        call do_training(the_person) from _call_do_training_starbuck_close_up_01

    the_person "You really wore me out! Good night [the_person.mc_title]."
    "She walks you to the door of the business and you walk out together, before going your separate ways."

    # time goes forward and exit the talk menu by jumping to game loop
    call advance_time() from _call_advance_time_starbuck_close_up_label_3
    return

#SBS140
label starbuck_replay_dressup_label(the_person):
    mc.name "Remember that one time, you got dressed up in a bunch of different lingerie and I took pictures for that ad?"
    the_person "Of course! The last picture I was sucking on a dildo and it got me all hot and bothered and..."
    mc.name "Right... right... well, have any new lingerie sets that need modeled? Maybe before we head out I could umm, you know, take some pictures for another ad..."
    the_person "Oh! I supposed I would be up for that. I don't really have any new sets though, but I do have a pretty wide selection!"
    the_person "You know what would be fun? Why don't you go pick something out? I'll put it on and you can snap some pics."
    "Oh god, she wants you to dress her up... in lingerie."
    the_person "You're a guy, so I'm sure you probably have a better idea of what would be good for a new advertisement anyway, right?"
    mc.name "Yes. I absolutely am the best person I know of to dress you up in lingerie."
    "She laughs at your reply."
    the_person "I guess when you put it that way. Anyway, go pick out something!"
    "You head out into the store and look at the lingerie. You try to come up with a racy outfit to put [the_person.possessive_title] in."

    call screen outfit_creator(Outfit("New Outfit"), outfit_type="under", slut_limit = the_person.effective_sluttiness(), start_mannequin = the_person)
    $ the_person.draw_person()
    if isinstance(_return, Outfit):
        $ the_outfit = _return
        "You pull out a few pieces of clothing and take them to [the_person.possessive_title]."
        "She looks at the outfit you've picked out for her and seems to think for a second."
        if the_outfit.outfit_slut_score <= the_person.effective_sluttiness() * .2: #She likes it enough to try it on.
            the_person "Are you sure? This seems kinda tame..."
            mc.name "I know. I just want to see what it looks like on you."
        elif the_outfit.outfit_slut_score >= the_person.effective_sluttiness() * .8:
            the_person "Wow! I can honestly say I was not expecting you to go all in like this!"
            mc.name "If you don't feel comfortable..."
            "She interrupts you."
            the_person "Ha! No way, I can't wait to see you start drooling after I get this on..."
        else:
            the_person "Ah, this look great! I bet this generates a lot of interest..."
            "She gives you a quick wink."
            the_person "And I bet if we put it on an ad it would get some interest too!"
    else:
        mc.name "It seems I've lost my touch, why don't you surprise me?"
        the_person "Oh hotshot, give me a minute."
        $ the_outfit = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under", allow_skimpy = True)
        "After a few minutes she is back, holding an outfit in her hand."

    "[the_person.possessive_title!c] starts to get undressed in front of you."
    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
    while strip_choice is not None:
        $ the_person.draw_animated_removal(strip_choice)
        "You watch as [the_person.possessive_title] takes off her [strip_choice.name]."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

    $ strip_choice = None
    "Once she's stripped out of her clothing, [the_person.possessive_title] puts on the outfit you've made for her."
    $ the_person.apply_outfit(the_outfit, update_taboo = True, show_dress_sequence = True)

    $ mc.change_locked_clarity(30)
    the_person "Mmm, I like it! Alright, let's take some pictures!"
    if the_person.outfit.is_suitable_underwear_set:
        $ the_person.wardrobe.add_underwear_set(the_outfit)
    elif the_person.outfit.is_suitable_overwear_set:
        $ the_person.wardrobe.add_overwear_set(the_outfit)
    else:
        $ the_person.wardrobe.add_outfit(the_outfit)
    "[the_person.title] hands you her phone with the photo app already up."
    $ the_person.draw_person(position = "back_peek")
    "In the first photo, you get some great shots of her backside. She sways her ass slowly, being careful not to go too fast in a way that would make the photos blurry."
    $ the_person.draw_person(position = "against_wall")
    "Next, she props up her leg on a stool and adopts a really sultry pose, with her legs open. She runs her hands down her sides and then back up between her legs..."
    $ the_person.change_arousal(10)
    $ the_person.draw_person(position = "cowgirl")
    "Finally, she gets down on her knees and slowly starts crawling over to you in a sultry display of her femininity."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    mc.name "Jesus girl, you are stunning..."
    the_person "Showing off for you is getting me all worked up again. Will you ummm... lay down for me?"
    "Thank god, things are about to get steamy."
    mc.name "For you? Anything."
    "You lay down on your back."
    if not the_person.vagina_available:
        "As you lay down, you notice [the_person.possessive_title] is stripping her bottoms off."
        $the_person.strip_outfit(top_layer_first = True, exclude_upper = True, exclude_lower = False, exclude_feet = True)
    $ the_person.draw_person(position = "stand4")
    "From the floor, you look up at the stunning sex shop owner. You notice a hint of moisture starting to form on her labia."
    the_person "When we made the first ad, I sucked you off. But this time, I want a little action too..."
    "[the_person.title] gets down beside you, then swings her leg over your body, her pussy right in your face. She adjusts her body into the classic sixty-nine position."
    $ the_person.draw_person(position = "doggy")
    mc.name "I suppose that is only fair."
    "You put your hands on her heavenly ass cheeks and get her to adjust her body a bit until she is in the perfect position for you to dive in."
    "You push your nose into her slit and begin to lick and suck on her clit. She exhales forcefully and you feel her hot breath on your dick."
    the_person "Mmmm, that's it. Oh god you are so hard, I have to taste it..."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    "You feel her tongue circling around the tip. She gives the head a couple of quick kisses and then parts her lips."
    "Her lips slowly descend your length, entering her blissfully hot mouth. You refrain from bucking your hips to keep from gagging her."
    call fuck_person(the_person, start_position = sixty_nine, start_object = mc.location.get_object_with_name("floor"), skip_intro = True) from _call_fuck_person_SBS141
    "When you finish, you slowly get up off the floor. You help [the_person.title] up as well."
    $ the_person.draw_person()
    the_person "So... you'll help me close up every night, right?"
    mc.name "I'm sorry, I can't promise something like that, my business keeps me busy."
    the_person "Damn. A girl can dream though."
    $ the_person.change_love(3, 40)
    $ the_outfit = None
    return

#SBS150
label starbuck_replay_dildo_demo_label(the_person):




    return

#SBS160
label starbuck_replay_edible_undies_label(the_person):




    return

label starbuck_replay_anal_DP_label(the_person):



    return

label starbuck_replay_anal_on_swing_label(the_person):




    return

init 2 python:
    def starbuck_intro_choose_title(person):
        title_tuples = []
        for title in person.get_player_titles():
            title_tuples.append((title, title))

        return renpy.display_menu(title_tuples, True, "Choice")

    def starbuck_anal_fetish_prepare_demo_audience(the_person):
        count = 0
        for girl in [x for x in mc.location.people if not x is the_person]:
            if girl.sluttiness > 60:
                count += 1
            else:
                girl.change_location(mall)
        return count

label starbuck_intro():
    $ the_person = starbuck

    $ the_person.draw_person(emotion = "happy")
    if not the_person.event_triggers_dict.get("starbuck_intro_complete", False):
        "You enter the sex shop. A beautiful woman comes up to you and begins to introduce herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        $ the_person.event_triggers_dict["starbuck_intro_complete"] = True
        the_person "Hello there sir! Welcome to Starbuck's Sex Shop!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.is_stranger:
            mc.name "Hello."
            $ the_person.set_title()
            $ the_person.set_possessive_title()
            the_person "Let me introduce myself, I am [the_person.title]."
            "She holds her hand out to shake yours."
            the_person "And how may I address you?"
            $ title_choice = starbuck_intro_choose_title(the_person)
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)
            $ the_person.primary_job.job_known = True
            $ the_person.set_event_day("day_met")

        the_person "We've just opened, so stock is still fairly limited, but feel free to browse and I'm here to answer any questions you might have!"
        "You smile at [the_person.possessive_title] and promise to take a look."
        the_person "Sounds great!"
        $ clear_scene()
        "After [the_person.possessive_title] goes back to the counter, you walk around the shop a bit. Unfortunately, things are pretty bare. There are several shelves with just labels on them."
        "You walk by one labelled as anal toys, but there aren't any on the shelf available for purchase."
        "You walk over to the counter."
        $ the_person.draw_person(position = "stand3", emotion = "happy")
        mc.name "This is pretty interesting, to open a sex shop like this, but the shelves seem pretty empty? Are you going to get more stock soon?"
        $ the_person.draw_person(position = "stand3", emotion = "sad")
        the_person "Yes, I'm sorry they are fairly empty, I didn't have much money to invest in the store. I'm hoping I'll be able to attract some customers, and reinvest the money back into the shop..."
        "You can see she is struggling a bit to open up."
        the_person "You see, it was always my husband's and my dream to open a shop like this, to help people be more adventurous and have fun in the bedroom..."
        the_person "When he died... it was hard. It has been a struggle to make ends meet, but I feel like I'm finally ready to move on with my life, and decided to chase my dreams!"
        "You glance around the shop for a bit. You can tell she is very... optimistic."
        mc.name "That's great that you are moving on... but surely you should get a bit more stock? Have you tried finding any investors?"
        "[the_person.possessive_title!c] mumbles for a second before answering."
        the_person "Well, you would be surprised how hard it is to find investors for a sex shop..."
        "You can tell that she is a hard worker, and is dedicated to making her shop work. Maybe you should consider investing in her shop?"
        mc.name "How much money would you need, say if someone were interested in investing in your shop, to get some basic stock on the shelves?"
        "[the_person.possessive_title!c] considers for a moment."
        the_person "Well, I really want the stock to be good, quality product. I'd say I could probably get everything set up for a basic shop for... say $1000?"
        "That seems pretty reasonable. You decide to consider investing. You should talk to [the_person.title] again if you decide to invest in the shop!"
    elif not the_person.is_at(sex_store):
        call relaxed_greetings(the_person) from _call_relaxed_greetings_starbuck_intro
    elif sex_shop_stage() == 0:
        the_person "Hello there sir! Welcome back to Starbuck's Sex Shop! Feel free to look around."
        "You smile at [the_person.possessive_title] and promise to take a look."
        the_person "Sounds great, [the_person.mc_title]! I'll be here if you have any questions!"
    elif sex_shop_stage() == 1:
        the_person "Hey there, [the_person.mc_title]! It's good to see you!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title!c] smiles playfully."
            the_person "I was just thinking about you. Anything I can help you with?"
        else:
            the_person "Is there anything I can help you with?"
    elif sex_shop_stage() >= 2 and get_shop_promo_stage() >= 3.0 and candace_get_has_gone_clothes_shopping() and candace.personality == bimbo_personality and not the_person.event_triggers_dict.get("Candi_event_start", False):
        if candace.sluttiness >= 60: #Separate candace slut check since I never check to make sure she exists in globals
            call starbuck_cargo_shipment_label(the_person) from _begin_candi_duo_event_intro_01
        else:
            "[the_person.possessive_title!c] smiles playfully."
            the_person "I don't think I could ever repay you, is there anything I can help you with?"
    elif sex_shop_stage() == 2:
        the_person "[the_person.mc_title]! I'm so glad to see you! This place is starting to do really well, thanks to you!"
        "[the_person.possessive_title!c] smiles playfully."
        the_person "Is there anything I can help you with?"
    elif sex_shop_stage() == 3:
        the_person "[the_person.mc_title]! Thanks for checking in! Thing are going amazing here, all thanks to you and your generous investments!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title!c] smiles playfully."
            the_person "I'll be forever in your debt. Is there anything I can help you with?"
        else:
            the_person "Is there anything I can help you with?"
    return

label starbuck_anal_fetish_masturbate(alert = False):
    $ the_person = starbuck

    if alert == True:
        "You feel your phone vibrate with a notification."
        "You pull it out and take a look. Looks like [the_person.title] is masturbating with her plug!"
    else:
        "You decide to check up on [the_person.title]. You pull out your phone and check up on her."
        "You are mildly surprised to see that she is masturbating with her plug!"
    "Do you want to have some fun with the plug?"
    menu:
        "Leave her to her fun":
            #TODO this section
            return
        "Vibrate the plug":
            $ mc.change_locked_clarity(10)
            "You decide to have a little fun with the plug vibration. You push and the hold the vibration function for a solid three seconds."
            "The app registers a heart rate spike with the vibration. [the_person.possessive_title!c] knows you are watching the monitor as she masturbates!"
    #WE can assume we decided to vibrate the plug
    "You imagine [the_person.title], somewhere in her shop, pushing the plug in and out of herself."
    "You push and hold the vibrate button again, release it, then pulse again. You make it pulse with vibration every second or two."
    "You watch as her heart rate slowly climbs. It's 100 beats per minute now and still climbing."
    "You pulse the plug a bit faster now. Her heart rate keeps climbing."
    "You can imagine her, bent over, fucking herself with her plug as it vibrates deep inside her needy bowel."
    "After a minute, you see her heart rate peak. You give her ten or fifteen seconds of strong pulsing vibrations."
    $ mc.change_locked_clarity(10)
    $ the_person.change_stats(happiness = 5, obedience = 3)
    "You see the obvious spike on the chart now as her heart rate subsides. The plug registers that it is now back in place and not being used for masturbation."
    "After a few seconds you get a text message from [the_person.possessive_title]."
    #TODO picture of her bent over
    $ mc.start_text_convo(the_person)
    the_person "That felt good! You should come visit me soon though... get yourself some of this!"
    "She attached a picture of herself, bent over and showing her ass to you."
    $ mc.end_text_convo()
    return

label starbuck_anal_fetish_request(alert = False):
    $ the_person = starbuck
    "You feel your phone vibrate with a notification."
    "[the_person.title] sent you a text and a picture!"
    $ the_person.draw_person(position = SB_get_random_ass_position())
    the_person "Hey! You need to get over here and fuck this! I'm about to go crazy! I might jump the next guy that walks through my door!"
    "Sounds like she is desperate for a dick in her ass!"
    $ mc.change_locked_clarity(10)
    return

label starbuck_anal_fetish_checkup(alert = False):
    $ the_person = starbuck
    "You decide to check up on [the_person.title]. You pull out your phone and check up on her."
    "You see she has been good. She's had the plug in, just the way she said she would!"
    if the_person.arousal_perc > 40:
        "You can also see her temperature is a little elevated, consistent with what you would expect from someone in a consistent arousal state."
    "You decide to let her know you're thinking about her and her delicious ass."
    "You set the vibration setting to high, then press and hold the vibration button for several seconds. You can see her heart rate spike as her plug quakes inside her ass."
    "You wait for a few seconds, then send her another round of vibrations."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(10)
    "You decide that is enough for now and go back to what you were doing."
    return


label starbuck_anal_fetish_swing_demo_label(the_person):
    $ the_person = starbuck
    mc.name "Hey, I was just wondering, you wanna go for a swing in the back?"
    "[the_person.possessive_title!c] gives you a big smile."
    the_person "That sounds great!"
    $ in_private = True
    #TODO determine if there are people here
    if mc.location.person_count > 1 and starbuck.has_exhibition_fetish: #If Starbuck is not the only girl
        the_person "I've got an idea! I've got a few customers in here... want to do a demonstration for anyone who wants to attend?"
        "You consider her proposition carefully."
        menu:
            "Do a demo!":
                mc.name "That would be hot! Let's do it!"
                the_person "Yes! Okay, you head back there, I'll get ready, make an announcement, then meet you back there, okay?"
                "You head to the back room. You make sure the swing is in a good position for people to be watch you... demonstrate it."
                $ mc.change_locked_clarity(30)
                "Soon you hear [the_person.title] making her announcement."
                the_person "Attention everyone! In five minutes, myself and a partner will be demonstrating one of the sex swingsets that we have for sale! Feel free to come watch and ask questions!"
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.draw_person(position = "stand4")
                "Soon, [the_person.title] appears in the doorway, completely naked."
                #TODO: Determine if anyone wants to watch
                $ count = starbuck_anal_fetish_prepare_demo_audience(the_person)
                if count == 0:  #No one wants to watch
                    the_person "Well, I made my announcement, but it doesn't look like anyone is interested in watching..."
                    "You can hear the disappointment in her voice."
                    mc.name "Hey, their loss. Don't worry, it'll still feel just as good when I slide into that amazing ass of yours..."
                    "Her nipple stiffen slightly when she hears what you say."
                    the_person "Mmm... I can feel it already... Probably because I still have this thing in!"
                    $ the_person.draw_person(position = "back_peek")
                    "[the_person.possessive_title!c] turns away from you. You see her plug nestled between her cheeks."
                    $ mc.change_locked_clarity(20)
                    "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when it's fully removed."
                    mc.name "Alright, let's replace that with something a little... meatier... shall we?"
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
                    "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
                    the_person "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"
                else:   #People watch
                    the_person "Here they come! This is gonna be great!"
                    "[the_person.possessive_title!c] looks genuinely excited! She walks over next to swing and nonchalantly takes out her plug and sets it to the side."
                    $ get_random_from_list(known_people_at_location(mc.location, [the_person])).draw_person(position = "stand4")
                    "You watch as people begin to walk into the room..."
                    "You are about to fuck [the_person.title], in the ass, in front of customers..."
                    $ mc.change_locked_clarity(30)
                    "You can't believe this is actually happening!"
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.title] makes begin to speak. When you turn to her she is already seated in the swing. You quickly move around behind her."
                    the_person "So, today, my wonderful partner and I are going to demonstrate proper technique on this swing..."
                    "You zone out for a bit as she begins explaining the basics, how to set it up, etc."
                    "You can't wait to feel yourself slide into her tight rear end. You start to daydream a bit."
                    the_person "Alright, [the_person.mc_title], go ahead, I think we are ready for the demonstration."
                    "Hearing her mention you grabs your attention. You slide up behind her, your hands squeezing her pliant cheeks."
                    "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
                    "She whimpers back at you."
                    the_person "Alright, let's give 'em a good show."
                    $ in_private = False

            "Keep it private":
                mc.name "I think I'd like to keep it between me and you, if that's okay."
                "You can tell she is a little disappointed, but she quickly smiles again when she remembers that you are about to fuck her in the ass..."
                the_person "Okay! Let's go!"
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title!c] walks to the back room. You quickly follow her."
                "You get to the back room and [the_person.title] turns to you."
                the_person "Alright. Before we get started, let me get ready. You should probably get naked too!"
                $ the_person.draw_person( position = "stand2")
                "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."

                $ the_person.strip_outfit(position = "stand2")

                "When you finish stripping, she turns her back to you."
                $ the_person.draw_person(position = "back_peek")
                mc.name "It's going to feel so good when I slide into that amazing ass of yours..."
                "She gives her ass a little wiggle."
                the_person "Mmm... I can feel it already... Probably because I still have this thing in!"
                "[the_person.possessive_title!c] pulls her cheeks apart. You can see her plug nestled between her cheeks."
                "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when it's fully removed."
                mc.name "Alright, let's replace that with something a little... meatier... shall we?"
                $ the_person.draw_person(position = "sitting")
                "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
                "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
                the_person "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"
    else:
        the_person "Okay! Let's go!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title!c] walks to the back room. You quickly follow her."
        "You get to the back room and [the_person.title] turns to you."
        the_person "Alright. Before we get started, let me get ready. You should probably get naked too!"
        $ the_person.draw_person(position = "stand2")
        "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."

        $ the_person.strip_outfit(position = "stand2")

        "When you finish stripping, she turns her back to you."
        $ the_person.draw_person(position = "back_peek")
        mc.name "It's going to feel so good when I slide into that amazing ass of yours..."
        "She gives her ass a little wiggle."
        $ mc.change_locked_clarity(20)
        the_person "Mmm... I can feel it already... Probably because I still have this thing in!"
        "[the_person.possessive_title!c] pulls her cheeks apart. You can see her plug nestled between her cheeks."
        "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when it's fully removed."
        mc.name "Alright, let's replace that with something a little... meatier... shall we?"
        $ the_person.draw_person(position = "sitting")
        "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
        "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
        the_person "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"

    call fuck_person(the_person, private = in_private, start_position = anal_swing, start_object = make_swing(), skip_intro = True) from _call_sex_description_SBA080

    #TODO the rest of this scene.
    if in_private:
        the_person "Oooh, fuck that was just what I needed."
        $ the_person.draw_person(position = "stand3")
        "[the_person.possessive_title!c] slowly stands up. Her knees are a little wobbly."
        "She grabs her plug. She reaches back and slowly re-inserts it with a moan."
        the_person "Mmm, that feels nice. Alright, you run along now! Don't worry about me, I'll get cleaned up and back out front in a quick minute."
        "You excuse yourself as [the_person.title] heads to the bathroom."
    else:
        $ person_one = get_random_from_list(known_people_at_location(mc.location, [the_person]))
        "You look around the room. All eyes are on you and [the_person.title]."
        $ person_one.draw_person (position = "stand4")
        "To one side you see [person_one.title], clearly touching herself, after watching you and [the_person.title] fuck."
        person_one "Oh wow... maybe I should... I wonder if..."
        "She is muttering things under her breath as she touches herself. She closes her eyes and you see her body tense as she orgasms."
        $ person_one.have_orgasm()
        $ the_person.draw_person(position = "sitting")
        "[the_person.title] has noticed and is smiling wide."
        the_person "So... as you can see... the swing makes a wide variety of sexual manoeuvres possible... For anyone who attended, I'd like to offer a discount!"
        "You hear a few murmurs of approval. [the_person.title] looks up at you and winks."
        the_person "Thanks, [the_person.mc_title], that was amazing. Alright, you run along now! Don't worry about me, I'll get cleaned up and back out front in a quick minute."
        "You excuse yourself. You wonder if this will help sell the swing any!"
        $ del person_one

    call advance_time() from _call_advance_SB_Anal_call_time_SBA081

    return
