#### Sex Shop Promotional Events ####
# This arc is based around ever increasinly sexual promotional events.
# They don't fit into the 3 seperate arcs, and require at least some sort of progress into an arc in order to progress them
# Once completed, they increase the profitability of the shop permanently.
# These events should have some dialogue changes based on if we are corrupting Starbuck thru a single path, or multiple.
# Milestone references to refer to in this set
# lust steps: 1 == foreplay, 2 == oral, 3 == vaginal, 4 == anal
# obedience steps: 3 == basic dressup, 5 == underwear dressup, 7 == cop bribed, 9 == nude dressup
# love steps: 1 == coffee, 2 == MC rebound talk, 3 == therapy started, 4 == open for steady

label starbuck_sex_store_promo_one_label(the_person):
    # TODO make a function to determine if we are here due to multiple story arc advancements, or a single one.
    $ arc_focus = None
    the_person "Well, it is going okay. Thanks to your investment, I'm finally turning a profit at least!"
    the_person "But, I feel like I'm just not getting the foot traffic I need. I need to find a way to attract more customers."
    "You consider what she is saying. Given the nature of the store, what you really need is some seriously sexy advertising."
    "You check out [the_person.possessive_title]. She has an amazing body. Maybe you should get her to pose with some of her product, take some pictures and turn it into an ad!"
    "[the_person.possessive_title!c] sees you checking her out, and the wheels turning in your head as you think about it."
    $ mc.change_locked_clarity(5)
    the_person "[the_person.mc_title]? Are you still with me here? Or are you too busy checking me out?"
    "You give her a smile as a plan comes together."
    mc.name "I know just what you need to do [the_person.title], that will help drive traffic here. You need to do some advertising!"
    "[the_person.possessive_title!c] shakes her head."
    the_person "I do, but it doesn't seem to be very effective."
    mc.name "That's right, because your advertising is so plain! What you need to do is get a sexy woman in your advertising, in some lingerie, showing off some of the products you have for sale!"
    "She thinks about your proposal."
    the_person "That sounds great, [the_person.mc_title], but... where am I going to find a model for something like that? Let alone pay her?"
    "You pretend to think hard about it."
    mc.name "Well, [the_person.title], I think YOU are pretty fucking sexy..."
    "[the_person.possessive_title!c] quickly realises you are suggesting that she dress up in lingerie for some advertising."

    if the_person.sluttiness > 50 : #We easily pass the sluttiness check.
        the_person "Oh! I mean, that would be fun for sure... but... do you really think I'm sexy enough for that?"
        "You give her another once over."
        mc.name "Absolutely. If I was a guy and I saw you in some lingerie on an advertisement, I'd be sure to come check the store out!"
        $ mc.change_locked_clarity(10)
        the_person "Hmm... okay! If nothing else, I'll have some nice pictures I can send to guys who hit me up on my dating app..."
    elif the_person.sluttiness > 20 :  #Barely passes the sluttiness check.
        the_person "Oh... I don't know [the_person.mc_title]. I mean, believe me, I love sex, I even opened a shop... But to put myself out there in public like that? Are you sure I'm sexy enough for that?"
        "You make a show of checking her out."
        mc.name "Absolutely. If I was a guy and I saw you in some lingerie on an advertisement, I'd be sure to come check the store out!"
        $ mc.change_locked_clarity(10)
        the_person "Hmm... okay, I mean, we can give a shot anyway. What's the worst that could happen?"
    else: #She fails the sluttiness check. Give dialogue to come back when she's sluttier.
        the_person "Wow, [the_person.mc_title]. I'm sorry I just... I don't think I could do that. To put myself out there in public like that?"
        "[the_person.possessive_title!c] considers for a bit."
        the_person "No, I'm sorry [the_person.mc_title]. It's a great idea, I just don't think I'm ready to do something like that. I'm sorry!"
        "You understand she's just not ready for something like that. Maybe at some point in the future she'd be willing to do something like that."
        return

    $ the_person.wardrobe.add_underwear_set(starbuck_promo_classic_black_lingerie())
    $ the_person.wardrobe.add_underwear_set(starbuck_promo_blue_nightgown_lingerie())
    $ the_person.wardrobe.add_underwear_set(starbuck_promo_pink_onepiece_lingerie())

    "Yes! [the_person.possessive_title] is gonna show off that amazing body of hers while you take pictures!"
    $ mc.change_locked_clarity(20)
    "You coordinate with her on the items you want to advertise and some outfits that would be suitable to show them off."
    $ the_person.draw_person(position = "walking_away")
    "You collect the items, while [the_person.possessive_title] grabs a few sets of lingerie. You meet her in the back room."
    $ mc.change_location(sex_store_storage)
    $ clear_scene()
    $ the_person.draw_person(position = "stand4")
    "Once in the backroom, you can see that [the_person.possessive_title] has three outfits picked out. Some classic black lingerie with fishnet and garter belt, a light blue nightgown, and a pink lacy one piece."
    "The first item to model is a bottle of some good quality, oil based lube. You figure a regular standing pose should work for this."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_classic_black_lingerie(), show_dress_sequence = True)
        "The blue nightgown":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_blue_nightgown_lingerie(), show_dress_sequence = True)
        "The pink one piece":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_pink_onepiece_lingerie(), show_dress_sequence = True)
    $ the_person.break_taboo("underwear_nudity")
    "Now dressed in her outfit, [the_person.possessive_title] hands you her phone. She grabs the first item, the bottle of lubricant."
    $ mc.change_locked_clarity(20)
    mc.name "Wow... you look great..."
    "You murmur. She smiles at your compliment."
    mc.name "Okay, why don't you just stand and put your hand on your hip."
    $ starbuck.draw_person(position = "stand4", emotion = "happy")
    "[the_person.possessive_title!c] strikes a pose for you. You take several pictures, trying to find the best angles to show off her body... and the product."
    "You can tell that [the_person.possessive_title] is actually enjoying herself and your attention. Her cheeks are starting to get a little flushed."
    $ the_person.change_arousal(15)
    "The next item for her to model will be a male masturbation sleeve."
    "It is designed to look like a famous porn actress' asshole, so you figure to model this product, [the_person.possessive_title] should have her back to you."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_classic_black_lingerie(), show_dress_sequence = True)
        "The blue nightgown":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_blue_nightgown_lingerie(), show_dress_sequence = True)
        "The pink one piece":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_pink_onepiece_lingerie(), show_dress_sequence = True)
    "Now dressed in her outfit, [the_person.possessive_title] looks to you for direction."
    $ mc.change_locked_clarity(25)
    mc.name "[the_person.title]. You look incredible..."
    "She clears her throat to get your attention."
    mc.name "Right! Why don't you turn around and peek back at me and hold this to the side, right next to your hip."
    $ starbuck.draw_person(position = "back_peek", emotion = "happy")
    "[the_person.possessive_title!c] turns around and looks back at you. You get a bunch of pictures of her amazing ass. You almost forget to get pictures of the product!"
    mc.name "Perfect! These pictures are perfect, you are going to get a flood of guys in here looking for this!"
    "Once you are done [the_person.possessive_title] turns back to face you."
    $ starbuck.draw_person(position = "stand2", emotion = "happy")
    $ the_person.change_arousal(30)
    "The attention you are giving her is really starting to excite [the_person.possessive_title]. You can see her nipples sticking out proudly in her outfit."
    "The last item for her to model is a dildo. You figure since you are mainly targeting a male audience with this advertisement, a good pose for her would be on her knees, like she's getting ready to put it in her mouth."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_classic_black_lingerie(), show_dress_sequence = True)
        "The blue nightgown":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_blue_nightgown_lingerie(), show_dress_sequence = True)
        "The pink one piece":
            "[the_person.possessive_title!c] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_pink_onepiece_lingerie(), show_dress_sequence = True)
    "As she changes you stand and gawk at her amazing body."
    $ mc.change_locked_clarity(30)
    the_person "Don't worry [the_person.mc_title], we're almost done. What should I do for this one?"
    mc.name "I think you should get down on your knees, you know, like you are getting ready to suck on it."
    the_person "Oh! That sounds like fun... sucking on a... a dildo, right!"
    $ starbuck.draw_person(position = "blowjob")
    "[the_person.possessive_title!c] gets down on her knees. She looks at the dildo longingly. You take multiple pictures of her."
    $ the_person.change_arousal(45)
    the_person "Mmm... it looks so tasty..."
    $ mc.change_arousal(15)
    "[the_person.possessive_title!c] opens her mouth, and slowly starting to run her tongue along the dildo. You see one of her hands slowly drift down between her legs and she begins to touch herself."
    "She has her eyes closed, so you snap a few more pictures of her sucking on the dildo. She suddenly realises what she is doing and pulls off."
    the_person "Right! So, I thought maybe a picture like that... I mean maybe we could include a picture like that free with every purchase... or something?"
    "You can tell she is fumbling with her words, trying to cover up that she lost her awareness and started sucking on the dildo."
    "You are all done with the pictures... maybe you should offer her something else to suck on?"
    menu:
        "Want a real dick?":
            "[the_person.possessive_title!c] looks up at you, still on her knees."
            the_person "Oh [the_person.mc_title], getting all dressed up has me all turned on. If you'd let me do that, I would really appreciate it."
            $ the_person.add_situational_slut("Excited", 10, "I want to suck your cock")
            mc.name "Go ahead, you look amazing. I can't wait to feel your mouth."
            $ mc.change_locked_clarity(50)
            "You walk up to [the_person.possessive_title]. She unzips your pants and pulls your cock out from your pants."
            "She runs her tongue up and down the sides a few times, then opens her mouth and sucks you into her hot mouth."
            $ the_person.break_taboo("sucking_cock")
            call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBS70
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] takes a few minutes to recover from her orgasm. Eventually she gets up."
                "Giving [the_person.title] an orgasm makes you feel more confident in your foreplay skills."
            else:
                "After you finish, [the_person.possessive_title] takes a second, then gets up."
            $ the_person.clear_situational_slut("Excited")
            $ perk_system.add_stat_perk(Stat_Perk(description = "Increase foreplay skill after helping Starbuck with her advertisement photos. +1 Foreplay Skill", foreplay_bonus = 1, bonus_is_temp =False), "Starbuck Foreplay Bonus")
            $ starbuck.draw_person(position = "stand2", emotion = "happy")
            the_person "Mmm... That was nice. It's been a while since I sucked on a hard cock. It was kinda nice!"
            if the_person.opinion.giving_blowjobs < 1:
                $ the_person.update_opinion_with_score("giving blowjobs", 1)
            "You are still recovering from your orgasm. You take a look at her phone and start looking at the pictures you got."
            the_person "If this advertisement works, we'll have to make more right?"
            mc.name "Definitely. Alright, I'll go ahead and get some advertisements done, and we'll see if we can't get better foot traffic in here."
            if perk_system.has_item_perk("Dildo"):
                pass
            else:
                "[the_person.possessive_title!c] looks at the dildo she was modelling for a few minutes ago."
                the_person "Hey... I probably shouldn't sell this in the store anymore. Do you want it?"
                "You consider... what would you need a dildo for?"
                the_person "I know you may not use it on yourself, but, you never know when a toy like this can spice up an encounter."
                mc.name "That's true. Sure, I'm sure I could find a use for it."
                $ dildo_unlock()
                "You are now the proud owner of a dildo."
                the_person "Maybe even use it on me sometime..."
            $ clear_scene()
            $ mc.change_location(downtown)
            "You say goodbye to [the_person.possessive_title] and head out. You look through the pictures again."
            "With pictures like these, you are sure the business here will increase."
        "Give her some privacy":
            "You decide to give her some time to herself. You use her phone to forward all the pictures you took to your account."
            mc.name "Okay, those should be good. I'll go ahead and get some advertisements done, and we'll see if we can't get better traffic in here."
            $ clear_scene()
            $ mc.change_location(downtown)
            "You say goodbye to [the_person.possessive_title] and head out. With pictures like these, you are sure the business here will increase."

    python:
        the_person.event_triggers_dict["shop_investment_rate"] = 2.0
        the_person.event_triggers_dict["shop_advert_step"] = 1
        the_person.set_event_day("promo_event")
        the_person.apply_planned_outfit()
        clear_scene()

    call advance_time(no_events = True) from _call_advance_time_starbuck_sex_store_promo_one
    return #Toy modelling, ends in blowjob


label starbuck_sex_store_promo_two_label(the_person):
    # TODO make a function to determine if we are here due to multiple story arc advancements, or a single one.
    $ arc_focus = None
    the_person "Oh, business is going pretty good! I have definitely been getting more traffic ever since you... you know... helped me with some advertising flyers."
    "[the_person.possessive_title!c]'s voice trails off for a second before she continues."
    the_person "And it's been nice, all the attention I've been getting from the guys that come in here."
    the_person "But, it's only guys coming in! I feel like I'm really missing market share, but I can't figure out a way to get more women in here!"
    "You consider her problem for a bit. Then you come up with an idea."
    mc.name "Have you ever considered doing reviews of the products you carry?"
    "She pauses and looks at you."
    the_person "I'm not sure what you mean."
    mc.name "Well, for example, that dildo over there. If I'm a girl, how do I know how well it's going to hold up? Is it going to hit all the right places? Is it easy to clean?"
    "[the_person.possessive_title!c] thinks about what you are saying."
    mc.name "What we could do is, take a video of yourself trying out the product. We post it online, and make sure people know, come get it here!"
    the_person "So... you're basically saying, I should take a video of myself... using dildos? And post it online?"
    #Sluttiness Check!
    if the_person.sluttiness > 70 : #We easily pass the sluttiness check.
        $the_person.draw_person(emotion = "happy")
        the_person "Oh! That's an amazing idea! I could put QR labels next to the tags too, so people can scan it with their phone and check it out!"
        "[the_person.possessive_title!c] seems to really like the idea."
        mc.name "Hey, that's a good idea too! Let's do it!"
    elif the_person.sluttiness > 40 :  #Barely passes the sluttiness check.
        the_person "Oh... I don't know [the_person.mc_title]. I mean, it sounds like it would work... but videos of me, on the internet? Using sex toys?"
        "You do your best to reassure her."
        mc.name "Absolutely. I mean, when have I steered you wrong? The last idea worked too, didn't it?"
        the_person "Hmm... okay. Let's do it!"
    else: #She fails the sluttiness check. Give dialogue to come back when she's sluttier.
        the_person "Wow, [the_person.mc_title]. I'm sorry I just... I don't think I could do that. To put myself out there on the internet like that?"
        "[the_person.possessive_title!c] considers for a bit."
        the_person "No, I'm sorry [the_person.mc_title]. It's a great idea, I just don't think I'm ready to do something like that. I'm sorry!"
        "You understand she's just not ready. Maybe at some point in the future she'd be willing to do something like that."
        return
    "[the_person.possessive_title!c] looks at you for a moment."
    the_person "So... You're going to help me... right? I mean, I'm sure I could figure it out eventually, but it would be really nice to have someone help me make the first couple..."
    "You consider her request. It sounds pretty reasonable, plus maybe you'll get to watch her masturbate!"
    $ mc.change_locked_clarity(10)
    mc.name "Sure, I'd be glad to help! Any idea which products you would like to review first?"
    the_person "Yeah, I've got a pretty good idea. Meet me in the back in a few minutes while I get everything together!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] walks away. You see her going around and grabbing a few things from around the store. You decide to head to the back room and wait for her there."
    $ mc.change_location(sex_store_storage)
    $ clear_scene()
    $ SB_advert_four_outfit = Outfit("Lingerie Set Dark Blue Corset")
    $ SB_advert_four_outfit.add_upper(corset.get_copy(),[0.15, 0.2, 0.45, 1])
    #$ SB_advert_four_outfit.add_lower(lace_panties.get_copy(), [0.15, 0.2, 0.45, 1])
    $ SB_advert_four_outfit.add_feet(garter_with_fishnets.get_copy(), [0.15, 0.2, 0.45, 1])
    $ SB_advert_four_outfit.add_feet(heels.get_copy(), colour_black)
    $ the_person.draw_person(position = "stand2")
    "She joins you in the backroom carrying a couple of dildos and a set of lingerie."
    the_person "Okay, let me just get changed really quick."
    $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
    $ mc.change_locked_clarity(20)
    "Once she finishes stripping, she grabs the lingerie set and puts it on."
    $ the_person.apply_outfit(SB_advert_four_outfit, show_dress_sequence = True)
    $ the_person.wardrobe.add_underwear_set(SB_advert_four_outfit)
    $ del SB_advert_four_outfit
    $ mc.change_locked_clarity(20)
    "You check out [the_person.possessive_title] in her outfit. Damn she looks hot!"
    the_person "Okay, so here's what I'm thinking..."
    "[the_person.possessive_title!c] starts going over the details of how she wants to do it. You take mental notes. Soon you are ready to begin."
    "You get the camera recording as [the_person.possessive_title] begins her reviews."
    $ the_person.draw_person(position = "stand4")
    the_person "Hello! This is [the_person.fname]! Owner of [the_person.fname]'s sex shop, and welcome to my review of the Ramboner dildo by..."
    "You check to make sure she is in frame. She talks for a few minutes about the quality of the toy."
    the_person "Okay! Time to try it out!"
    $ the_person.draw_person(position = "missionary")
    "[the_person.possessive_title!c] lays down on the floor. She begins by stroking herself with the dildo a few times up and down her slit."
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(20)
    the_person "Mmm, that texturing feels great sliding up and down, let's see how it feels going in..."
    "She slowly takes the head of the dildo and begins pushing it into her pussy."
    the_person "Oh! Wow the curve on the tip feels great sliding in..."
    $ the_person.change_arousal(15)
    "[the_person.possessive_title!c] begins working the dildo in and out of her."
    the_person "Yes! And with the flared base, it's easy to hold... so I can control the depth... oh fuck!"
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    "She is working the dildo in and out of herself now at a steady pace. Each time she pulls it out, you can see her juices glistening on the toy."
    the_person "The texturing on the outside... it really... stimulates the nerve endings as it... oh god."
    $ the_person.change_arousal(15)
    "[the_person.possessive_title!c] is now fucking herself earnestly with the dildo. The sights and sounds are starting to turn you on. You absentmindedly begin to stroke yourself through your pants."
    the_person "Okay... now seems like a good time to test the curve, and see how well it stimulates the g-spot."
    "She pulls the dildo mostly out, then changes the angle of penetration. She gives herself short, shallow thrusts, focusing on her g-spot."
    the_person "YES! Okay this toy stimulates the g-spot... SO GOOD."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] looks up and notices you stroking yourself. Her mouth goes wide in a moan as her orgasm approaches."
    "She looks directly at you and cries out."
    the_person "YES! OH god, fuck me... YES! FUCK ME!!!"
    $ the_person.change_arousal(25)
    $ mc.change_locked_clarity(50)
    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
    $ the_person.have_orgasm()
    "[the_person.possessive_title!c]'s body begins to spasm as she orgasms. She shoves the toy in deep inside her. Her juices are trickling down beneath her out of her cunt."
    "Her body relaxes after she finishes. She slowly pulls the toy from her sopping wet cunt."
    the_person "So... overall... I rate this toy... a solid 9 out of 10... thanks for watching!"
    $ the_person.event_triggers_dict["shop_investment_rate"] = 3.0
    "You step out from behind the camera. Her sultry eyes look up at you as you walk over to her."
    if (the_person.love > 50):
        the_person "Oh [the_person.mc_title]. That toy was so good... but honestly the whole time I was imagining it was you fucking me..."
        "She pushes herself up on her elbows, but makes no motion to stand up."
        the_person "Don't get me wrong, toys are great, but I want you! Seeing you touching yourself... looking at me... Please fuck me [the_person.mc_title]!"
    else:
        the_person "Damn [the_person.mc_title]. I'm glad you were enjoying the show..."
        "She pushes herself up on her elbows, but makes no motion to stand up."
        the_person "Toys are great... but nothing beats a real cock inside me. Would you please fuck me [the_person.mc_title]?"
    $ mc.change_locked_clarity(30)
    menu:
        "Fuck Her":
            mc.name "[the_person.title], that was so hot! I can't wait to bury myself into your amazing cunt."
            "She smiles at your response."
            the_person "Then come get some! I just came, no need to warm me up!"
            "You quickly strip out of your clothes and lay down on top of her."
            $ mc.change_locked_clarity(20)
            if (the_person.love > 50):
                "[the_person.possessive_title!c] wraps her arms around you and holds you close. You move your face in for a kiss and she greedily accepts your tongue in her mouth."
                "While you make out with her, you use one hand to get yourself lined up with her soaked slit. You slide in easily with no resistance, bottoming out inside her."
            else:
                "[the_person.possessive_title!c] runs her hands along your sides as you get into position."
                "She grabs your cock with her hand and points it at her soaked slit. With one smooth motion you thrust into her. She's so wet you glide in with no resistance."
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            "Wasting no time, you begin thrusting into her. Her pussy feels amazing wrapped around you."
            call fuck_person(the_person, start_position = missionary, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_fuck_person_SBS80
            $ the_person.draw_person(position = "missionary")
            "[the_person.possessive_title!c] lays there in a daze. Between the toy and your cock, she had multiple orgasms."
            if (the_person.love > 50):
                "As your start getting dressed again, out of the corner of your eye you see [the_person.possessive_title] begin to shudder."
                "You see a tear roll down from one of her eyes."
                the_person "Thank you [the_person.mc_title]... It means so much to me, everything you've done for me... and for the shop."
            else:
                "You get up and start getting dressed. [the_person.possessive_title] calls out to you."
                the_person "Thank you [the_person.mc_title], for all your help. I wouldn't have made it this far without you."
            mc.name "Thanks, [the_person.title]. It has been a pleasure helping you out. Please let me know if you'd like... help... again in the future with your reviews!"
            $ the_person.change_stats(love = 5, happiness = 10, slut = 1, max_slut = 50)
            if not perk_system.has_stat_perk("Starbuck Vaginal Bonus"):
                $ perk_system.add_stat_perk(Stat_Perk(description = "Increase vaginal skill after helping Starbuck with her demonstration video. +1 Vaginal Skill", vaginal_bonus = 1, bonus_is_temp =False), "Starbuck Vaginal Bonus")
                "Fucking and pleasing an experienced woman like [the_person.title] makes you feel more confident in your vaginal skills."
            "You go back and take a look at the camera. You accidentally left it recording! It has a recording of you and [the_person.possessive_title] fucking!"
            "You decide you should probably just be honest and tell her."
            mc.name "So... I accidentally forgot to stop the camera... it caught the whole scene of us having sex."
            the_person "Oh! Let me see!"
            $ the_person.draw_person(position = "stand2")
            "[the_person.possessive_title!c] hops up and takes a look at the camera."
            the_person "Oh my... this is hot... I didn't think I would like this but... it's kinda hot watching yourself on video get fucked..."
            "You raise an eyebrow. Is she starting to like showing off a bit?"
            if the_person.opinion.public_sex < 1:
                $ the_person.update_opinion_with_score("public sex", 1)
            "You chat with her for a few minutes about the details of setting up a review site, but eventually it's time to say goodbye."
            the_person "Thanks again for everything [the_person.mc_title]. Don't be a stranger now!"
        "Refuse":  #Lol really? I guess some people may not have the energy.
            mc.name "Sorry, I've had a long day, and I should probably get to work on editing this video."
            "She seems surprised by your answer."
            the_person "Oh... right, I'm sure that's going to be a lot of hard work..."
            "You chat with her for a few minutes about the details of setting up a review site, but eventually it's time to say goodbye."
            the_person "Thanks for the help [the_person.mc_title], if you find yourself needing anything later... just ask okay?"
            $ the_person.change_stats(love = -5, happiness = -5, slut = -1)

    python:
        the_person.event_triggers_dict["shop_advert_step"] = 2
        the_person.set_event_day("promo_event")
        the_person.apply_planned_outfit()
        mc.change_location(sex_store)
        clear_scene()

    call advance_time(no_events = True) from _call_advance_time_starbuck_sex_store_promo_two
    return #Masturbation, ends in sex


label starbuck_sex_store_promo_three_label(the_person):
    # TODO make a function to determine if we are here due to multiple story arc advancements, or a single one.
    $ arc_focus = None
    the_person "Oh, business is great! I'm definitely getting more women in here now."
    "[the_person.possessive_title!c]'s voice trails off for a second before she continues."
    the_person "The interest has been booming now for masturbation tools, but one thing I've noticed as I've had customers come in, as well as my sales..."
    the_person "A huge percentage of my sales are to singles. I get almost no couples in here shopping together."
    "You consider her problem for a bit, but it is actually her that comes up with an idea first."
    the_person "So, I was thinking, maybe for my next video review you could umm, you know, help me demonstrate something?"
    "She looks at you hopefully. This is an easy decision."
    mc.name "Absolutely. It's only fair. You've already put yourself out there, I'm ready to do my part."
    "[the_person.possessive_title!c] gives you a bright, beaming smile."
    the_person "Yes! Okay! Give me a minute and I'll meet you in the back! Get the camera ready!"
    $ mc.change_location(sex_store_storage)
    $ clear_scene()
    "You make your way to the back. You get the camera set up and ready to go."
    $ SB_advert_five_outfit = Outfit("Lingerie Just Red Panties")
    $ SB_advert_five_outfit.add_lower(panties.get_copy(), colour_red)
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title!c] enters the room."
    the_person "Ok, I figure we can get through a couple things... I have a pair of edible panties, and a nice set of fuzzy handcuffs..."
    "Wow... so at her suggestion, you are about to eat panties off of [the_person.possessive_title]... and then handcuff her... all on camera."
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title!c] starts to strip down."
    $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
    "Once she finishes stripping, she grabs the panties and puts them on."
    $ the_person.apply_outfit(SB_advert_five_outfit, show_dress_sequence = True)
    $ the_person.wardrobe.add_underwear_set(SB_advert_five_outfit)
    $ del SB_advert_five_outfit
    "[the_person.possessive_title!c] stands before you almost completely exposed, her incredible body on full display."
    $ mc.change_locked_clarity(30)
    if starbuck.love > 50:
        the_person "Do you think that before we get started, maybe you could just hold me for a little bit?"
        "You step up to her. Your hands go to her waist and she wraps her arms around you."
        $ the_person.draw_person(position = "kissing")
        the_person "Mmm... it feels so good when you hold me."
        "She looks up into your eyes. You bring your face down to hers and begin to kiss. Her lips open submissively to allow your tongue to invade her mouth."
        "You embrace each other for a while, just enjoying the heat and softness of her skin."
        the_person "Okay, are you ready to get this started?"
    else:
        the_person "You just gonna watch? Or are you ready to get started?"
    "You walk over and start up the camera. You give her a nod to show her that it's running."
    the_person "Hello! This is [the_person.fname], from [the_person.fname]'s Sex Shop! Here to review another couple of products."
    the_person "Today, we are going to review a couple of products meant for couples! So today I've asked a friend to be here to help me review them..."
    "You step into frame next to [the_person.possessive_title]."
    the_person "This is [the_person.mc_title], and we are going to review some edible underwear by Skinworks, and some neat fuzzy handcuffs by PowerTrips Inc..."
    "[the_person.possessive_title!c] gives some of the details on the products."
    the_person "Ok, I guess we're ready to get started! Are you ready [the_person.mc_title]?"
    "You nod. [the_person.possessive_title!c] lies down on the table and spreads her legs, angled in such a way that the camera can get a good view of her barely hidden pussy."
    $ the_person.draw_person(position = "missionary")
    "You get down on your knees between her legs. You kiss and lick up along her leg, working your way up to her pussy."
    "When you reach her mound, you stop and breath deeply in through your nose, savouring the musky scent of her sex."
    "[the_person.possessive_title!c] runs her hands through your hair, gently urging your face down into her edible panty-clad cunt."
    $ mc.change_locked_clarity(20)
    "You push your face into her mound, and begin to nibble at the gummy panties that are between your tongue and [the_person.possessive_title]'s sweet cunt."
    $ the_person.change_arousal(10)#10
    the_person "Mmm, how do they taste, [the_person.mc_title]?"
    "You give her a loud MMMmmm of approval."
    "You are starting to make good-sized holes in the cherry flavoured covering. One is close enough to her slit, you are able to snake your tongue through it and along her moist fuckhole."
    $ the_person.change_arousal(10)#20
    $ mc.change_locked_clarity(20)
    the_person "Oh! Mmm, that felt good. These panties would be good if you had a significant other who... maybe doesn't usually like to go down on you..."
    "You chew the hole a little wider. You can now access her clit easily through the hole. You take the opportunity to roll her clit between your lips for a few seconds before resuming your panty eating."
    $ the_person.change_arousal(15)#35
    the_person "Oooohhhhh, he just got through to my clit... Mmmm, that feels so good."
    "[the_person.possessive_title!c] reaches down and tears a piece off her panties, now giving you almost free rein to eat her pussy."
    the_person "Okay, let's see how they taste..."
    $ play_swallow_sound()
    "She takes a bite of the panties, chews and swallows. While she does that you push your tongue deep into her cunt."
    $ the_person.change_arousal(15)#50
    $ mc.change_locked_clarity(30)
    the_person "Yes! Mmm, they actually taste pretty good, I can see why [the_person.mc_title] here is so eager..."
    $ strip_choice = the_person.choose_strip_clothing_item()
    $ the_person.draw_animated_removal(strip_choice)
    $ the_person.draw_person(position = "missionary")
    "Her panties now in shreds, [the_person.possessive_title] gathers what is left of them and pulls them off."
    $ the_person.change_arousal(20)#70
    "[the_person.possessive_title!c]'s juices are beginning to flow freely from her slit. You lap them up before circling your tongue around her clit a few times."
    "After licking at her clit, you move your tongue down to her entrance. You push your tongue up inside her as far as it will go."
    $ the_person.change_arousal(10)#80
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] has stopped providing commentary and is now just moaning and encouraging you."
    the_person "Oh [the_person.mc_title]! That feels so good..."
    "She starts to rock her hips, grinding herself against your face."
    $ the_person.change_arousal(10)#90
    "[the_person.possessive_title!c] is bucking her hips wildly as you lick her. Suddenly, she grabs the back of your head and gasps."
    $ the_person.change_arousal(20)#110
    $ the_person.call_dialogue("climax_responses_oral")
    $ the_person.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(30)
    "Her pussy is drooling wet as she climaxes. She paws at the table, trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down a bit and lap up her sweet, creamy juices."
    the_person "Oh fuck [the_person.mc_title], your tongue feels so good. Wow!"
    "You slowly push yourself back from her pussy. [the_person.possessive_title!c]'s juices are dripping down your chin. You lick up as much as you can."
    the_person "Ok... wow... so, moving on... you know... to the handcuffs..."
    "You step over and grab the handcuffs. They have linings on them so they are nice and soft, but you can tell that underneath the cloth lining is strong steel. They feel very sturdy."
    the_person "That was great for when you want to get your pussy eaten... as my incredibly able assistant just showed, but these, they are good for when you want your man to take control."
    $ the_person.draw_person(position = "sitting")
    "You approach [the_person.possessive_title] with the handcuffs. She sits up and puts her hands behind her back. As you put the handcuffs on her hands, she whispers in your ear."
    the_person "[the_person.mc_title] that was amazing. I want you to be rough with me now. Don't worry, I can take it, and I want to show off how sturdy the cuffs are for the camera..."
    $ mc.change_locked_clarity(30)
    "You nod in acknowledgement. Even though the camera is running, you know that the real reason [the_person.possessive_title] has you here isn't for the video, but because she wants you to dominate her."
    "She could have chosen any other toy, and she could have chosen any other guy, but she chose you. You snap the second handcuff in place."
    the_person "So, these handcuffs are soft enough they don't hurt or dig into the skin, but they are very sturdy. [the_person.mc_title] can do whatever he wants to me now, there's no way I'll be able to break free."
    "You take that as your cue. You grab her shoulders and turn her away from you, then push her down onto the table. Soon, she has her face down and her ass up."
    $ the_person.draw_person(position = "doggy")
    "Her pussy lips are wildly engorged, slick from the juices of her previous orgasm."
    "You rub your dick back and forth across her slit, getting it nice and slick. Then you grab her hips, and in one smooth motion you thrust yourself deep inside her."
    # manual break and discover since custom sex loop
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.discover_opinion("vaginal sex")
    $ the_person.discover_opinion("bareback sex")
    $ the_person.discover_opinion("doggy style sex")
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "You thrust yourself deep into her steamy sex. Her moans begin immediately, her arousal still high from her previous orgasm."
    "You hold onto [the_person.possessive_title]'s hips and settle into a steady rhythm, pumping your cock in and out of her tight pussy."
    $ play_spank_sound()
    "You take a hand off of [the_person.possessive_title]'s hips and squeeze her ass cheeks with it. She moans happily in response, and you give her a hard slap."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] struggles a bit against her handcuffs, but she is helpless to defend herself from your spanking."
    $ play_moan_sound()
    "[the_person.possessive_title!c]'s moaning intensifies rapidly, until finally she takes a sharp breath and tenses up."
    $ the_person.call_dialogue("climax_responses_vaginal")
    $ the_person.have_orgasm(half_arousal = False)
    $ the_person.change_stats(happiness = 4, slut = 1, max_slut = 50)
    "You keep up your pace while [the_person.possessive_title] cums. With each pulse of her pussy around your cock you spank her ass."
    the_person "Ah!"
    "You enjoy the way her tight ass jiggles and spank it again."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "You take your hands off of her hips and lean forward to put them on her shoulders. With her hands in cuffs she is powerless to resist when you pull her shoulder back towards you, forcing her to arch her back."
    "With the leverage of your hands on her shoulders, holding her body weight up off the table. Your hips make heavy slapping noises as they slam into her ass with each thrust."
    the_person "OHHH! Fuck me [the_person.mc_title]! HOLY FUCK!"
    "[the_person.possessive_title!c]'s entire body begins to tremble as another orgasm hits her. Her pussy spasms wildly all around you and you can see her hips quaking."
    $ the_person.call_dialogue("climax_responses_vaginal")
    $ the_person.change_stats(happiness = 4, arousal = 20, slut = 1, max_slut = 50)
    $ mc.change_locked_clarity(30)
    $ the_person.have_orgasm()
    "[the_person.possessive_title!c]'s orgasm is milking your cock. It is rapidly pushing you past the point of no return."
    "You can't help but grunt with each thrust as you fuck her roughly. [the_person.possessive_title!c] is having trouble speaking intelligible words."
    the_person "[the_person.mc_title]! Oh cum for me baby... please cum! I want it so bad!"
    $ the_person.change_arousal(20)
    $ mc.change_arousal(25)#105
    "You can't take anymore. You let go of her shoulders and her upper body crashes roughly to the table. You grab her hips and plough deep into her pussy."
    $ the_person.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    "You bottom out and explode deep inside [the_person.possessive_title]. The heat of your semen painting her vaginal walls sends her into another orgasm."
    the_person "OH! I'M CUMMING AGAIN! YES [the_person.mc_title]!"
    $ the_person.have_orgasm()
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "doggy")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
    "You are completely spent. [the_person.possessive_title!c] is a sweaty, handcuffed mess beneath you. She takes a few seconds to recover."
    $ mc.reset_arousal()
    the_person "So... as you can see... the handcuffs... fuck... they can hold up to... some pretty intense... amazing... mind-blowing... fucking..."
    "You move off to the side to exit the frame. You can see in the camera your seed slowly dripping out of [the_person.possessive_title], when you press the stop button."
    mc.name "Wow, that was amazing. I'd be surprised if we don't get at least a little bit of traffic from couples out of that!"
    "[the_person.possessive_title!c] turns her head to look at you. You laugh when you realise you forgot to uncuff her."
    mc.name "Sorry, I forgot you still had those on."
    "You grab the key and undo the cuffs. She slowly sits up, but is hesitant to stand."
    $ the_person.draw_person(position = "sitting")
    the_person "[the_person.mc_title]... it's been so long... since I've been fucked like that..."
    if the_person.love > 50:
        the_person "I've missed that, having someone take control of me and just fuck my brains out..."
        "While she is normally a very independent woman, you think maybe [the_person.possessive_title] is starting to get a bit of a submissive streak when you are around."
        if the_person.opinion.being_submissive < 1:
            $ the_person.update_opinion_with_score("being submissive", 1)
    the_person "So... I'm just gonna throw this out there. I have at least 4 other sets of fuzzy cuffs... we could totally try them out anytime you want..."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] slowly stands up. She walks over toward you."
    $ the_person.reset_arousal()
    the_person "Except right now... I'm going to need some time to recover from that."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title!c] wraps her arms around you. She kisses you twice on the neck, then whispers in your ear."
    the_person "I can feel you running down my leg... and I love it..."
    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "walking_away")
    the_person "I'm gonna go get cleaned up now... Get to work on that video!"
    $ the_person.event_triggers_dict["shop_investment_rate"] = 4.0
    $ the_person.apply_planned_outfit()
    "You grab the camera, and start looking at the footage. The first thing you do is copy it onto a thumb drive, for you to enjoy at a later date."
    $ clear_scene()
    $ mc.change_location(downtown)
    "You head out to start work on the advertisement video."
    if not perk_system.has_stat_perk("Starbuck Oral Bonus"):
        $ perk_system.add_stat_perk(Stat_Perk(description = "Increase oral skill after helping Starbuck demonstrate edible panties. + 1 Oral Skill", oral_bonus = 1, bonus_is_temp =False), "Starbuck Oral Bonus")
        "Giving [the_person.title] an orgasm with your tongue gives you more confidence in your oral skills."

    python:
        the_person.event_triggers_dict["shop_advert_step"] = 3
        the_person.set_event_day("promo_event")
        strip_choice = None

    call advance_time(no_events = True) from _call_advance_time_starbuck_sex_store_promo_three
    return


label starbuck_sex_store_promo_four_label(the_person):
    # TODO make a function to determine if we are here due to multiple story arc advancements, or a single one.
    $ arc_focus = None
    the_person "Oh, yeah! It's great to see couples coming in now..."
    "[the_person.possessive_title!c]'s voice trails off for a second before she continues."
    the_person "You know, I've been tracking the stock of stuff we have been selling though. It's all very... vanilla? I guess you could say."
    mc.name "I'm not sure I understand what you mean?"
    "[the_person.possessive_title!c] stutters as she tries to figure out the best way to explain what she means."
    the_person "I guess I just mean that, the sales we are getting, it's for just generic sex items. Lingerie, condoms, handcuffs... but the more... shall we say, kinky items aren't really selling."
    mc.name "Like what kind of things aren't selling?"
    the_person "Well, some of the kinkier items... like whips, ropes, strap-ons... that kind of thing."
    "You consider some of the items she has in mind. The list she's said makes you a little nervous."
    mc.name "Well, I mean, I'm definitely willing to help you make another video showcasing an item or two... did you have anything specific in mind?"
    the_person "Well... I'm going to be honest here, you definitely seem like more of a dominant type... why don't we make a video where I play the submissive? See if we can get more business that way?"
    "Wow... she wants you to play the dom! You definitely like where this is going..."
    $ mc.change_locked_clarity(20)
    the_person "Tell you what... set up the camera and meet me in back in a few minutes... I've got a couple things in mind I wouldn't mind..."
    mc.name "Sounds great!"
    $ mc.change_location(sex_store_storage)
    $ clear_scene()
    "You make your way to the back. You get the camera set up and ready to go."
    $ SB_advert_six_outfit = Outfit("Starbuck's Pink Lingerie")
    $ SB_advert_six_outfit.add_upper(corset.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_feet(garter_with_fishnets.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_feet(high_heels.get_copy(), colour_pink)
    $ SB_advert_six_outfit.add_accessory(wide_choker.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_accessory(lipstick.get_copy(), [1.0,0.44,0.43,0.7])

    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title!c] enters the room. When you see what she is carrying you start to get excited."
    the_person "Ok, I figure we can start with the whip... I also have a bottle of premium anal lube, and a strap-on for guys designed for double penetration..."
    "Wow... you wonder which hole you are gonna get to fuck while the strap-on fucks the other..."
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title!c] starts to strip down in front of you."
    $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
    "Once she finishes stripping, she puts on some incredibly sexy pink lingerie."
    $ the_person.apply_outfit(SB_advert_six_outfit, show_dress_sequence = True)
    $ the_person.wardrobe.add_underwear_set(SB_advert_six_outfit)
    $ del SB_advert_six_outfit
    mc.name "[the_person.title]... that's... you look amazing."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] gives you a wide smile."
    the_person "Thank you! You know I can't give ALL my investors special views like this..."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title!c] turns around and wiggles her hips a bit. She peeks back at you and teases."
    the_person "But you've done so much for me... I figure this is the least I can do for you!"
    $ the_person.draw_person(position = "stand4")
    $ mc.change_locked_clarity(20)
    the_person "Okay! Let's start with the whip, go ahead and get the camera rolling, and I'll do the introduction."
    "You step over to the camera. When [the_person.possessive_title] is in frame you hit the record button."
    the_person "Hello! This is [the_person.fname], from [the_person.fname]'s Sex Shop! Here to review another couple of products."
    the_person "Today, we are going to review a couple of products meant for those who are looking to get things a little... kinkier in the bedroom..."
    "[the_person.possessive_title!c] talks about the whip she has in her hand. After explaining tips and tricks to proper usage, she cues you."
    the_person "And now, to demonstrate proper usage, I'm going to invite [the_person.mc_title] back to help me demonstrate it..."
    "You move in frame, and she hands you the whip."
    the_person "Okay! Now, it is important, anytime you get something like a whip involved, that you are very careful with where you strike the other person."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title!c] bends over a chair nearby."
    the_person "While really, you could use it on any fatty part of the body, the obvious place to utilize a whip during sex play is on the ass..."
    "You are partially mesmerized by [the_person.possessive_title]'s ass when she bends over. In her pink lingerie, you can't wait to fuck her... you are startled when she prompts you."
    $ mc.change_locked_clarity(30)
    the_person "... [the_person.mc_title]? I said I'm ready now. Show the viewers how to use that thing!"
    "You move behind her, but at an angle so that the camera can still see what is going on."
    "For your first strike, you spank her modestly. You aren't sure how much pain tolerance she has."
    $ play_spank_sound()
    "SMACK"
    the_person "OH! As you can see, another important thing when you are using a tool like this is... start slow! As you can see, my partner here is starting easy..."
    "[the_person.possessive_title!c] wiggles her hips back and forth a couple times."
    the_person "Don't worry [the_person.mc_title], you can give it to me harder than that."
    "You swing the whip with a little more force this time."
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(10)
    the_person "AHH! Mmmm, that's nice... Now remember, an important part of spicing up the bedroom is communication! Tell your partner how you like it!"
    "[the_person.possessive_title!c] wiggles her hips again."
    $ mc.change_locked_clarity(30)
    the_person "Okay [the_person.mc_title], that was about a 5 out of 10 for how hard you can spank... I want you give me a 7 this time..."
    "You'd never thought about rating how hard you swing the whip, but it makes total sense after [the_person.possessive_title] says that. It's pretty sexy the way she tells you the way she wants to get spanked..."
    "You put more force into the next one, but not too much."
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(10)#20
    the_person "Fuck! Oh that was good... That was just about perfect... now try and..."
    "SMACK"
    "You catch her off guard as you give her other ass cheek a whipping."
    the_person "AHH! Oh that hurt so good... that's it baby, I've been a bad girl... spank me!"
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(10)#30
    $ mc.change_locked_clarity(30)
    "You give her a couple more spanks with the whip."
    $ play_spank_sound()
    "SMACK"
    "You can see her ass cheeks beginning to turn red. She wiggles her hips as you spank her."
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(15)#45
    the_person "YES! Oh [the_person.mc_title]... okay... I think the viewers get the idea now..."
    $ play_spank_sound()
    "SMACK"
    "You give her one last spank, just for good measure... You can see her pussy is starting to glisten with excitement."
    $ the_person.draw_person(position = "stand2")
    $ mc.change_locked_clarity(30)
    the_person "Okay... time to move on. The other thing we have to demonstrate today is... mmm, that felt good..."
    "[the_person.possessive_title!c] takes a second to gather her thoughts."
    the_person "We are going to demonstrate proper usage of a special type of strap-on. This strap-on goes around a man and sits just below the penis..."
    "[the_person.possessive_title!c] explains the basics of the strap-on in her hand. When she gets done talking about it, she gets down on her knees."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    the_person "Okay, here is how we put it on..."
    "She grabs your dick and gives it a couple strokes. She puts the straps in place and secures the strap-on to you. You now have a second, rubber cock, sitting just below your fleshy one."
    "[the_person.possessive_title!c] gazes intently at your meat. She licks her lips and then runs her tongue along the side of it a couple times before she stands up."
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "stand4")
    the_person "Now, before we get to the good part, it is important, anytime you are getting ready to put anything in your ass, that you get it good and lubed up..."
    "She grabs the bottle of premium anal lube and squirts some in her hand. She lists the pro's of buying the higher quality lubes."
    "[the_person.possessive_title!c] takes your cock in her hand and started to lube it up. She takes the bottle and squirts some more into her hand, getting you nice and slick."
    $ mc.change_arousal(5)#10
    "She squirts some more in her hand, and you see her reach back and start to lube up her backside."
    the_person "Okay, I think we are all set..."
    $ the_person.draw_person(position = "doggy")
    "[the_person.possessive_title!c] gets down on her hands and knees and sticks her ass up in the air. Her puckered hole glistens from the lube she put on it, and her lips are puffy with arousal."
    $ mc.change_locked_clarity(30)
    the_person "[the_person.mc_title]... I want you to go slow when you put your cock in my ass... I'll guide the strap-on into my vagina..."
    "Her ass looks supple and firm. You are about to fuck [the_person.possessive_title]'s ass, while a dildo penetrates her pussy. You can't believe how lucky you are to be able to do this with her."
    "You get down on your knees behind her. With one hand on her hip and the other on your cock, you line yourself up with her tight back passage."
    "[the_person.possessive_title!c] reaches one hand between her legs and grabs the dildo. She lines it up with her other hole."
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    $ mc.change_locked_clarity(30)
    the_person "Oh my god! I'm so full... It's so good [the_person.mc_title]! This thing is amazing..."
    "With your hands on her hips, you slowly start to fuck her."
    call fuck_person(the_person, start_position = doggy_anal_dildo_dp, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_sex_description_SBS100
    "[the_person.possessive_title!c] is in a sex-induced daze after you finish. She struggles to make a coherent end to the video."
    the_person "So that's... when you use a strap-on... holy fuck people just get one."
    "You get up and head over to the camera and stop the recording."
    mc.name "Well... that was incredible. [the_person.title] if that doesn't bring in customers, I don't know what would."
    if the_person.love > 60:
        the_person "[the_person.mc_title]... you are amazing. Look... I'm going to be honest here. I couldn't care less about bringing in more business... I just wanted you to fuck me with that thing."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title!c] slowly stands up. Her feet are a bit wobbly."
        the_person "It has been amazing having you around [the_person.mc_title]. It just feels so right every time we have sex. It almost feels wrong... recording it just to bring in more business..."
        "You decide to interrupt her."
        mc.name "[the_person.title], it has been great being your business partner. I know what you are saying, but don't worry. I'd be doing this with you even if we weren't recording it."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        "She smiles at you happily."
        mc.name "But don't worry. If it helps the business grow, there's no reason not to record it. It doesn't make the sex any less meaningful to me. I mean really, you could ask any guy in here to do this stuff..."
        the_person "I can't imagine it though... doing this whole venture with anyone else as my partner. Thank you, [the_person.mc_title]."
    else:
        the_person "Thanks, [the_person.mc_title]. That was amazing... UGH I can barely get up."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        "[the_person.possessive_title!c] slowly stands up. Her feet are a bit wobbly."
    "[the_person.possessive_title!c] rubs her ass a bit where you spanked her earlier."
    the_person "I remember when... my husband used to use me like that... bending me over, spanking me like the naughty girl that I am."
    the_person "We should do this again. It felt so good when your cock started pushing into my ass..."
    if male_strapon_unlock():
        "She looks at the strap-on, then looks back at you."
        the_person "Actually... do you want this strap-on? I'm sure I probably can't sell it now. I could give it to you if you want it..."
        $the_person.draw_person(position = "stand4")
        "She gets closer and whispers in your ear."
        the_person "Just promise me you'll use it on me again..."
        mc.name "I promise!"

    if the_person.opinion.being_submissive < 2:
        $ the_person.update_opinion_with_score("being submissive", 2)
    if the_person.opinion.anal_sex < 1:
        $ the_person.update_opinion_with_score("anal sex", 1)
    "You grab the camera, and start looking at the footage."
    mc.name "Okay, you take it easy for a bit, I'm gonna go work on that advertisement video!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] starts to walk away. She is walking a little funny."
    if not perk_system.has_stat_perk("Starbuck Anal Bonus"):
        $ perk_system.add_stat_perk(Stat_Perk(description = "Increase anal skill after helping Starbuck demonstrate double penetration with a dildo. +1 Anal Skill", anal_bonus = 1, bonus_is_temp = False), "Starbuck Anal Bonus")
        "Fucking [the_person.title] anally makes you more confident in your anal skills."
    $ clear_scene()
    $ mc.change_location(downtown)
    "You head out to start work on the advertisement video."

    python:
        the_person.event_triggers_dict["shop_investment_rate"] = 5.0
        the_person.set_event_day("promo_event")
        the_person.event_triggers_dict["shop_advert_step"] = 4
        the_person.apply_planned_outfit()

    call advance_time(no_events = True) from _call_advance_time_starbuck_sex_store_promo_four
    return


label starbuck_sex_store_promo_five_label(the_person):
    # TODO make a function to determine if we are here due to multiple story arc advancements, or a single one.
    $ arc_focus = None
    the_person "Oh, yeah! Business is great! It has been amazing having all different types of people coming in here to try out all kinda of new things."
    "[the_person.possessive_title!c] gives you a big smile."
    the_person "I tell you what. I have a product I've been wanting to try out ever since we expanded and got it in..."
    "You like where this conversation is going!"
    the_person "If you are willing to try it out with me... I'd be willing to give you an extra that you can take home with you!"
    mc.name "Are we going to do another video of it? For advertising purposes?"
    the_person "Of course! I mean, as long as you are okay with it... honestly... I want to try it out either way, but if we're gonna try a new product, might as well take a video anyway, right?"
    "You nod in agreement."
    mc.name "Okay, I'm in. What exactly are we going to test out?"
    the_person "Well... I got in a special... ermm... swing set... with straps that I can get up in, so you can fuck me in while I'm suspended up in the air..."
    mc.name "Wow... do you need help setting it up?"
    the_person "Yes, actually. That would be really helpful!"
    $ mc.change_location(sex_store_storage)
    $ clear_scene()
    "You and [the_person.possessive_title] head to the back room. To the side of the room you can see a box that has the swing in it."
    "You pull it out and start going through the directions. It seems pretty straightforward to set up!"
    $ the_person.draw_person(position = "back_peek")
    "While working on the set-up, you look over and see [the_person.possessive_title] working on something with her back to you. You walk up behind her."
    "You run your hands along her hips, admiring their shape and form."
    if the_person.love > 70:
        the_person "Mmm... I love it when you run your hands all over me [the_person.mc_title]."
        "You work your hands along her belly and then slowly up to her wonderful tits."
        if the_person.tits_available:
            "They are so soft and warm in your hands. You give them a good squeeze and then pinch lightly at her nipples."
        else:
            "They feel so soft, even through her clothes. You give them a good squeeze, and you can feel her nipples start to poke through the fabric."
        "[the_person.possessive_title!c] pushes her ass back against you. She starts to grind her hips against your hardening erection."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        the_person "[the_person.mc_title] it is so nice having you close... let's get done with this swing. I want you!"
    else:
        the_person "That feels good... Let's focus on the swing though. I need a good fucking!"
        $ mc.change_locked_clarity(15)
    "You get back to work. It isn't long until the whole thing is finished. You stand with [the_person.possessive_title] and admire your handiwork."
    $ the_person.draw_person(position = "stand3")
    the_person "Alright. Before we get started, let me get ready. You should probably get naked too!"
    "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."
    $ the_person.strip_outfit(position = "stand3")
    $ mc.change_locked_clarity(30)
    "Now that she is naked, [the_person.possessive_title] grabs some of her anal lube of a shelf. You raise an eyebrow as she squirts some onto her hand."
    mc.name "Anal lube? Wow... going all out are we?"
    "[the_person.possessive_title!c] chuckles as she reaches back and starts to spread the lube around her backside."
    the_person "Of course! I mean, it feels so good when you push it into me back there..."
    the_person "Besides, I'm sure that the viewers would probably like it better anyway!"
    "[the_person.possessive_title!c] walks over to you and starts lubing up your cock. It feels great when she gives you a couple of strokes."
    $ mc.change_locked_clarity(30)
    the_person "Okay! I'm ready to do this! Go ahead and start up the camera, this is gonna be great!"
    "You step behind the camera. You make sure everything is in frame, then hit record. You give [the_person.possessive_title] a thumbs up."
    the_person "Hello! This is [the_person.fname], from [the_person.fname]'s Sex Shop! Here to review a new product we've just gotten in to the store!"
    the_person "Today, I am going to be reviewing the FEMco Sex Swing 3000..."
    "[the_person.possessive_title!c] starts talking about the swing set. As she talks, she is using hand gestures to illustrate some of the set-up methods."
    "Every time she moves her hands back and forth, her amazing tits quiver a bit."
    "After she is done introducing the swing, she sits down in it."
    $ the_person.draw_person(position = "sitting")
    the_person "And now to help me demonstrate one of the ways you could use it, the always amazing [the_person.mc_title]!"
    "You step into frame and start to walk up behind her."
    the_person "Today, he is going to show us how it could be used for a relaxed sodomy session. I'll be able to relax here in the swing, while my ass is at just the right height for him to fuck it..."
    "As you get close behind her, you put your hands on her hips. She reaches back and grasps your cock, and begins to guide it toward her bottom."
    "When your cock begins poking up against her puckered hole, you can feel a bit of resistance. With your hands firmly on her hips, you pull her ass towards you."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] forces herself to relax her sphincter, and you penetrate her with a wonderful pop. With more gentle pressure you are soon deep inside her bowel."
    the_person "Mmm... as you can see... I'm able to completely relax with my ass off the back of the swing, so I can just sit and enjoy the sensations."
    "You give her a modest thrust. The swing bounces forward for a second, but gravity soon causes her ass to pendulum back and smack against your hip."
    "The feeling is exquisite. You grab her hips and get ready to fuck [the_person.possessive_title]'s brains out."
    #Call sex scene#
    call fuck_person(the_person, start_position = anal_swing, start_object = make_swing(), skip_intro = True) from _call_sex_description_SBS110

    "Turning off the video camera, you turn to [the_person.possessive_title]."
    $ the_person.event_triggers_dict["shop_investment_rate"] = 6.0
    mc.name "Wow, that was good. You are so sexy."
    the_person "Aww, thanks, [the_person.mc_title]. Now, I promised that if you helped me make the video, I'd give you a swing for you to have."
    mc.name "Thanks, but you don't need to do that."
    the_person "No no, it's okay, I want you to have one... I was thinking... you helped me set up this one, why don't you let me come over and I'll help you set up one?"
    "Hmm, she is offering to come over to your place!"
    mc.name "Well, it would be rude to say no."
    "[the_person.possessive_title!c] gives you a big hug."
    the_person "Great! Let's get it done. It won't take us long!"
    $ the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = 0.4), show_dress_sequence = True)
    $ the_person.draw_person(position = "walking_away")
    "After she gets dressed, you both walk out."

    #TODO move the scene to the player's bedroom. and get dressed
    $ mc.change_location(bedroom)
    $ the_person.draw_person(position = "stand4")
    "You and [the_person.possessive_title] head back to your place. Having already put one together, you and her quickly have it all set up."

    the_person "Great! Now you have one of your own... you know... for when you have girls over..."
    "She gets a little shy."
    the_person "I think that I'm going to leave up the one I have in the back room at the shop, in case you ever want to try it out again..."
    if the_person.love > 70:
        "She looks at you. Her face is a little forlorn, clearly remembering something from her past."
        the_person "[the_person.mc_title], getting this shop up and running... and everything you've done for me. You really don't have any idea how much it all means to me. Thank you so much!"
        $the_person.draw_person(position = "kissing")
        "She wraps her arms around you and hugs you close."
        the_person "Look... I don't know any other way of saying this, so I'm just gonna say it. I'm falling for you, [the_person.mc_title]. And I know you have a busy job and there's other girls and I'm not saying..."
        "She stutters for a minute."
        the_person "I understand that you aren't looking to be tied down to one girl, and I just want you to know that I understand that. I just want to know if you, maybe have feelings for me too..."
        menu:
            "It's mutual":
                mc.name "Don't worry, [the_person.title]. The feeling is mutual. I love spending time with you."
                $ the_person.draw_person(position = "stand2", emotion = "happy")
                the_person "Oh! That is such a relief to hear."
                "You see her digging around in her pocket."
                the_person "Here... I want you to have this. It's a key to my apartment. You don't have to come over if you don't want to, but I just want you to know, you're always welcome in my bed."
                $ the_person.learn_home()
                mc.name "Thanks, [the_person.title]. It will be nice to be able to share a warm bed with a beautiful woman like you once in a while."
                $the_person.draw_person(position = "kissing")
                "She hugs you again and begins kissing you on your neck."
                the_person "You make me feel so good, [the_person.mc_title]... come visit me soon okay?"
            #TODO it's not mutual
    else:
        # alternative to learning her home location (needed for 'spend the night' event)
        the_person "Anyway, if you are ever in my neighbourhood make sure to drop by for a beer."
        $ the_person.learn_home()
        "She tells you her home address, so make sure you go visit her sometime."

    $ the_person.draw_person(position = "stand2")
    the_person "Okay, it's time for me to get to the shop. See you soon [the_person.mc_title]!"
    $ clear_scene()
    "You walk her to the door and say goodbye. Wow, you are now the proud owner of a sex swing! And with everything going on with [the_person.possessive_title], you brain is swimming a bit."
    "After having multiple sexual encounters with a woman like [the_person.title], you feel like if you put in the effort, you could become an even more skilled lover."

    python:
        perk_system.add_stat_perk(Stat_Perk(description = "Increase sexual skill cap from repeated sexual activity with Starbuck. +1 Sex Skill Cap", sex_cap = 1, bonus_is_temp =False), "Starbuck Sex Bonus")
        sex_store_storage.add_object(make_swing())
        bedroom.add_object(make_swing())
        the_person.set_event_day("promo_event")
        the_person.event_triggers_dict["shop_advert_step"] = 5

    return

#### Starbuck's lubricant story arc ####

#In this arc, Starbuck has trouble stocking personal lubricants due to a national shortage
#MC offers to develop a proprietary lubricant and stock it personally
#Once complete, personal lubricants are sold at the story, possibly being used by anyone who goes into the store.

label starbuck_lubricant_shortage_label(the_person):
    "In this label, [the_person.possessive_title] informs MC of a national personal lubricant shortage."
    "MC convinces her to allow him to develop his own proprietary lubricant, starting a quest chain."
    return
