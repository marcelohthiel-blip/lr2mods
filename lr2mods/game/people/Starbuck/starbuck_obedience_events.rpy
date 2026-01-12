#starbuck's obedience arc involves MC helping out with the financial aspect of her business
# At first it is just practical advice, but as it goes along he starts having her dress up for the part


label starbuck_no_profit_label(the_person):
    $ eager_obedience = False
    # TODO figure out what steps numbers are appropriate for this
    if starbuck.progress.love_step > 2 or starbuck.progress.lust_step > 1: #If we have already progressed her other arcs, she is eager to be obedient to MC.
        $ eager_obedience = True
    "You stop by the sex shop to see how things are going. You see [the_person.possessive_title] behind the counter."
    $ the_person.draw_person()
    "You walk over to the counter."
    mc.name "Hello [the_person.title]. How is it going today?"
    the_person "Oh hey [the_person.mc_title]. Things are good. I was just getting ready to work on some new product orders."
    mc.name "Neat. Anything new and fun coming soon?"
    the_person "No, just restocks. To be honest, I'm having trouble keeping good stock on what we already carry."
    mc.name "Ah, you're selling through it too fast?"
    the_person "Well, yeah, there's that..."
    "She clearly doesn't want to tell you more. You decide to push into it."
    mc.name "And what else?"
    "She mumbles something, but relents."
    the_person "I suppose there's no use trying to hide it from you. I'm having trouble with the finances of running the place."
    the_person "I'm not sure why... I'm selling enough product, but each week my account balance is still getting lower."
    the_person "I... I'm not making any profit."
    the_person "The money you put in, it really helped to jumpstart product sell through, but for some reason it just hasn't been enough to make any money."
    "Wow. You have to stop and think about it for a moment. When you've stopped by, you definitely see people shopping."
    "You wonder what is going on behind the scenes that is causing her to have issues."
    mc.name "[the_person.title]... I don't want to invade your privacy but, could I have a look at your finances?"
    mc.name "I offered an investment because I want you to do well, and I just want to see if there is anything I can do to help?"
    $ the_person.draw_person(emotion = "sad")
    the_person "I don't want to bother you... I keep thinking, maybe I should hire a professional, or if I just work a little harder surely things will turn around soon."
    mc.name "I'm fairly new to running a business myself, but maybe there is something obvious that I could help with."
    the_person "I... guess it couldn't do any harm. Here, come around."
    "You step around the counter. Behind it she has a very messy desk with envelops and papers and bills strewn about."
    "She quickly starts up a laptop then loads some small business budgeting software."
    the_person "Here is what I have... I'm going to keep working the counter."
    mc.name "Okay."
    $ the_person.draw_person(position = "walking_away")
    "You sit down and start going through her finances. You take a look at her expenses for a while, then go through her revenue."
    "You go through things for quite a while, but something is definitely missing."
    mc.name "Hey, [the_person.title]."
    $ the_person.draw_person(position = "back_peek")
    the_person "Yeah?"
    mc.name "These invoices for product... they all have taxes on them?"
    the_person "Yeah?"
    mc.name "But on your revenue... none of them show sales tax collected."
    the_person "Right. I paid the tax when I ordered the product..."
    mc.name "[the_person.title]... you are running a retail business. You aren't supposed to be paying taxes on the product you stock."
    mc.name "The customer is supposed to pay the sales tax, and you are supposed to collect it on their behalf..."
    the_person "I... I don't pay that?"
    mc.name "No... Do you have a small business tax ID?"
    the_person "Let's just pretend like... I have no idea what that is..."
    mc.name "So... you've been paying taxes on all your product, and then selling them at MSRP? And not charging customers sales tax?"
    $ the_person.draw_person()
    "She turns to face you."
    the_person "Errmm... is that bad?"
    mc.name "[the_person.title], you are missing something like 15 percent of your margin off of EVERY item!"
    the_person "Oh my god... can you help me fix it?"
    "You think about it for a moment. You can help her fix this at least, but she really needs to have a professional come check her books."
    "You have no idea what kind of financial penalties she might be facing for this."
    "However, this is going to cost you most of your evening. Of course, you could always ask her for some kind of compensation."
    $ mc.change_locked_clarity(15)
    if not eager_obedience:
        "You check her out for a moment. Maybe you could convince her to give you a little show in exchange for your time."
        mc.name "I'll make you a deal. I'll help you with this issue, but you have to do something for me."
        the_person "Oh?"
        mc.name "I'll do it if you let me pick out one set of lingerie from your store and you model it for me."
        the_person "I... you... what???"
        mc.name "Just one outfit. It's clear you aren't in a position to pay me, and I do want to help. But it would make me feel better about losing my evening plans tonight."
        $ the_person.change_stats(happiness = -2, obedience = 3, slut = 2, max_slut = 40)
        "She mutters for a moment, but relents."
        the_person "Fine..."
        mc.name "Alright! We have a deal."
    else:
        "You check out [the_person.possessive_title] for a moment. Maybe you could have some fun with it."
        mc.name "I'll make you a deal. I'll help you with this issue, but you have to do something for me."
        the_person "Oh?"
        mc.name "I'll do it if you let me pick out one set of lingerie from your store and you model it for me."
        "She giggles."
        the_person "Oh, is that all? You know I would probably do that for you anyway."
        mc.name "I know. But it is more fun to make you do it because you feel like you owe me."
        $ the_person.change_stats(happiness = 2, obedience = 3, slut = 2, max_slut = 40)
        "She considers it for a moment."
        the_person "Fine, but only because I can't wait to see your eyes bug out of your head."
        mc.name "Alright! We have a deal."
    $ the_person.draw_person(position = "walking_away")
    "She turns back to the counter and you turn back to the laptop."
    "You spend a considerable amount of time on local government websites, getting her registered as a local business and applying for her tax exempt retailer status."
    "Thankfully, most of this is digital. It takes you a while to gather all the necessary documents, but soon you have her all set up."
    mc.name "Alright, I think I have you all setup. Do you want to make a restock purchase to test and make sure it worked?"
    $ the_person.draw_person()
    the_person "Yeah! And it is closing time anyway, let me go close up shop and I'll make an order up."
    "She quickly locks the door then returns."
    the_person "Alright, I have a list I already started... may I?"
    "She motions for you to get up."
    mc.name "Aww, I'm kind of comfy. Why don't you just sit on my lap?"
    if eager_obedience:
        the_person "Oh yeah, good idea!"
        $ the_person.draw_person(position = "sitting")
        "[the_person.possessive_title!c] eagerly obeys and sits down on your lap."
        "As she starts making an order from a vendor, you think you even feel a little wiggle in her hips..."
        $ mc.change_arousal(10)
        "You put your hands on her hips and run them up and down her body a bit. She giggles a bit but doesn't let herself get too distracted."
    else:
        the_person "I... I don't know..."
        mc.name "Oh come on. I'm about to see you in lingerie anyway, I promise I'll keep my hands to myself."
        $ the_person.change_obedience(3)
        $ the_person.draw_person(position = "sitting")
        "[the_person.possessive_title!c] eventually obeys, sitting down on your lap."
        "Her body feels great up against yours, but you keep your promise and keep your hands to yourself as she starts a new stock order."
        $ mc.change_arousal(5)
    the_person "Alright, here we go."
    "She makes a couple final clicks."
    the_person "Stock is ordered. It worked!"
    $ the_person.draw_person()
    "She quickly gets up."
    the_person "While you were working back here, I messed with some settings on the register and figured out how to enable sales tax."
    the_person "I think this is going to be just what I need to get things turned around... thank you, I really appreciate it."
    mc.name "Of course. I'll go ahead and find what you'll be modeling for me now."
    if eager_obedience:
        the_person "Oh boy! I can't wait to see what kind of naughty thing you pick out for me."
    else:
        the_person "I do owe it to you. Honestly, I'm a little excited to see what you pick out anyway..."
    mc.name "Good! I'll just be one minute."
    $ clear_scene()
    "You step out from behind the counter and walk through the store. You pick out an outfit for [the_person.possessive_title]."
    call outfit_master_manager(slut_limit = the_person.sluttiness + 40, show_overwear = False, show_underwear = False, start_mannequin = the_person) from _call_outfit_master_manager_starbuck_dressup_one_enhanced
    $ third_outfit = _return    #Copy paste is cruise control for cool
    if third_outfit is None:    #MC rolls nat 1
        "You take a while, but just can't seem to come up with a good outfit for [the_person.possessive_title]."
        "You return to her."
        $ the_person.draw_person()
        the_person "Hey... where's the outfit?"
        mc.name "I'm not sure, I couldn't come up with anything."
        $ the_person.change_stats(obedience = -5, love = -2, slut = -2)
        the_person "You... you couldn't figure out anything? Wow..."
        "She looks a bit dejected."
        the_person "That's okay. I'm just an old lady anyway. I still appreciate your help though."
        mc.name "Yeah..."
        "Suddenly, an idea enters your head."
        mc.name "Hey... have you ever thought about dressing sexier when you run the shop?"
        the_person "What do you mean?"
        mc.name "With the nature of your shop, it might help you sell through more merchandise."
        the_person "Ummm, no, I don't think I could do that. I enjoy running the shop, but to use my attire to sell more? It feels wrong."
        mc.name "I see..."
    else:
        "You return to her with the outfit."
        $ the_person.draw_person()
        the_person "Hey, get something good?"
        mc.name "Of course. Here you go."
        "She takes the clothes from you, then disappears into a changing room."
        $ clear_scene()
        "You wait patiently for a few minutes as she gets changed."
        $ the_person.apply_outfit(third_outfit, update_taboo = True)
        $ the_person.draw_person(position = "stand4")
        "She steps out in the outfit you picked out."
        if not the_person.judge_outfit(the_person.outfit, 20):  #She thinks it is slutty.
            "She smiles shyly."
            the_person "Damn, you really got your money's worth with this one... I can't believe I'm wearing this!"
            $ the_person.change_stats(obedience = 3, slut = 1, max_slut = 50)
            $ mc.change_locked_clarity(50)
            mc.name "Wow! That looks incredible..."
        elif not the_person.judge_outfit(the_person.outfit):    #She thinks it is hot.
            "She smiles at you."
            the_person "I have to admit, I wouldn't normally wear something like this... but I think it looks good!"
            $ the_person.change_obedience(2)
            $ mc.change_locked_clarity(30)
            mc.name "You're goddam right it looks good!"
        else:
            "She smiles at you."
            the_person "I figured you would go a little more skimpy, but I hope you like it!"
            $ the_person.change_obedience(1)
            $ mc.change_locked_clarity(30)
            mc.name "Mmm, me likey."
        mc.name "Show me the back."
        $ the_person.draw_person(position = "back_peek")
        the_person "Like this?"
        $ mc.change_locked_clarity(30)
        mc.name "Close. Bend over and let me get a really good look."
        $ the_person.draw_person(position = "standing_doggy")
        "She bites her lip but does as she is told."
        $ mc.change_locked_clarity(50)
        "She stands there for several seconds."
        $ the_person.draw_person(position = "stand4")
        the_person "Alright, that's good for now..."
        $ post_model_action = False
        if the_person.is_willing(handjob):
            "[the_person.possessive_title!c] steps over to you. She reaches down and starts to stroke your cock with her hand through your clothes."
            the_person "Mmm, you've gotten all excited now..."
            the_person "I really DO appreciate you helping me. Is it alright if I help you with this now?"
            menu:
                "Take care of me":
                    $ post_model_action = True
                "Not today":
                    mc.name "I've had a long day, but I appreciate the offer."
                    the_person "Ah... of course."
        else:
            "Seeing [the_person.possessive_title] in this outfit has you incredibly aroused."
            "You wonder if you could push the boundaries just a bit further and convince her to get you off."
            menu:
                "Ask for handjob":
                    $ post_model_action = True
                    mc.name "Fuck, you've got me hard as a rock."
                    "She glances down at your crotch, blushing slightly."
                    the_person "So I see..."
                    mc.name "I know we agreed to just the outfit, so it is fine if you say no but..."
                    mc.name "Would you umm... be willing to take care of this for me?"
                    the_person "You... you want to fuck? I don't think so..."
                    mc.name "No no, we don't have to go that far. Just a quick handjob. I'm so turned on, I promise it won't take long."
                    "She bites her lip looking down at your crotch for a moment, but then nods."
                    the_person "You really did help me out... Okay, I'll do it."
                    $ the_person.change_obedience(3)
                    "She steps closer to you and reaches down, rubbing your cock through your clothes."
                    $ the_person.add_situational_obedience("seduction_approach", 10, "I will do this for you.")
                "Leave it be":
                    pass
        if post_model_action:
            "[the_person.possessive_title!c] quietly reaches down with both hands and unclasps your pants, then pulls them down with your underwear."
            "Your erection springs free, and she grasps it with both hands and gives it a couple soft strokes."
            $ the_person.break_taboo("touching_penis")
            if the_person.is_willing(blowjob):
                $ the_person.draw_person(position = "blowjob")
                "To your surprise, she gets down on her knees and brings her face to your dick, running her tongue along it."
                mc.name "Oh fuck... I thought you were just going to give me a handjob..."
                "She looks up at you with a smile."
                the_person "Shhh, just enjoy."
                "Your breathe catches in your throat as [the_person.title] opens her mouth and swallows the tip."
                $ the_person.break_taboo("sucking_cock")
                "She starts slowly bobbing her head up and down."
                call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_starbuck_no_profit
            else:
                "You let yourself enjoy it as [the_person.title] starts to give you a handjob."
                call mc_sex_request(the_person, the_request = "titfuck") from _call_mc_sex_request_starbuck_no_profit_2
            "Done for now, you look at [the_person.title]."
        $ the_person.clear_situational_slut("seduction_approach")
        $ the_person.draw_person()
        "Suddenly, an idea enters your head."
        mc.name "Hey... have you ever thought about dressing sexier when you run the shop?"
        the_person "What do you mean? Like THIS?"
        mc.name "No, I just mean in general. With the nature of your shop, it might help you sell through more merchandise."
        the_person "Ummm, no, I don't think I could do that. I enjoy running the shop, but to use my attire to sell more? It feels wrong."
        mc.name "I see..."
    "[the_person.possessive_title!c] seems resistant to your idea. Maybe with a few more obedience serums, you could convince her to give it a try."
    "She seems pretty independent though, so it might be a tough thing to convince her."
    $ the_person.draw_person()
    the_person "Well, I think I'm going to get dressed and get going. I'll see you next time, [the_person.mc_title]."
    $ clear_scene()

    "You step out of the sex shop. You consider her finances and what you learned about her."
    "Maybe you should see if she would be willing to bring in an accountant of some sort? Someone with more expertise than you have."
    if aunt.progress.obedience_step >= 3:
        "You suddenly remember [aunt.possessive_title], who recently finished renewing her CPA license."
        "Wow! Getting her and [the_person.title] together could present some really interesting possibilities."
        "You decide to talk to [aunt.title] about it at her apartment sometime."
        $ add_starbuck_rebecca_teamup_setup_one_action()
    else:
        "Do you know anyone like that? You consider it for a bit, but in the end, you can't come up with anything."
    $ the_person.event_triggers_dict["shop_promo_market_rate"] = 0.2
    $ del third_outfit
    $ del eager_obedience
    $ starbuck.progress.obedience_step = 1
    $ add_starbuck_dressup_intro_action()
    call advance_time() from _call_advance_time_starbuck_obedience_intro_01
    #Cleanup

    return

label starbuck_dressup_intro_label(the_person): #Another closing time room entry event. 140 obedience
    $ starbuck.progress.obedience_step = 2
    # try to make her wear something conservative
    $ the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = -.4))
    "You swing by the sex shop. You look over at the counter and see [the_person.title]."
    $ the_person.draw_person()
    "You look around the store. You see a few people, browsing various sections, as well as one couple looking at lingerie."
    "You happen to overhear the couple talking."
    "?Woman?" "No, I don't think so. It looks so uncomfortable!"
    "?Man?" "I'm sure it is fine, you can wear it under that dress and no one will know."
    "Woman" "I don't know... that doesn't seem right!"
    "Man" "Let's ask the lady working here, I bet she knows."
    "Woman" "Her? No way. I doubt she even knows what half this stuff is for..."
    "As you listen to the couple talk, you look back at [the_person.possessive_title]."
    "You know her well enough, and she could definitely help them, but she just doesn't really look the part."
    "You wonder if she could get more business if she looked more like the part of a sex shop owner. You decide to approach her about it."
    "You walk up to the counter."
    the_person "Oh hey [the_person.mc_title]. Here to do some shopping?"
    mc.name "Not today, I'm just here to visit with you. Mind if I help you close up tonight?"
    the_person "Of course! I always appreciate the help."
    "You hang out with [the_person.possessive_title] for a bit. The couple that was browsing lingerie eventually leaves without making any purchases."
    mc.name "Hey, did you see that couple that just walked out?"
    the_person "Yeah. They were here for a while. Too bad they didn't buy anything. Maybe they'll come back?"
    mc.name "When I walked in, I happened to overhear them chatting about some of the lingerie. They had some questions about it, but didn't think you would be able to answer them."
    the_person "What? Huh. Why would they think that?"
    mc.name "Well... As great as it is that you run this shop, if I'm being honest... you really don't look the part."
    the_person "I... you mean because I'm old?"
    mc.name "What? No no, I mean because of the way you dress."
    the_person "My clothes?"
    mc.name "Yeah. They are so conservative! You really should consider dressing sexier while you're working behind the counter."
    mc.name "Couples with questions would be more likely to approach you, and I'm sure anyone coming in by themselves would be more likely to buy something."
    "[the_person.title] looks a bit embarrassed."
    the_person "Look... I understand what you are saying, but that just doesn't feel right. I don't want my business to succeed just because of the way I dress."
    mc.name "It won't, things are already starting to get better, right? A lot of places have uniforms for their girls that help push their business to the next level."
    mc.name "It isn't just about showing some skin, it is about company image and reputation."
    the_person "I'm not sure..."
    mc.name "How about this. Let me pick something out for you to wear tomorrow. When you are done, see if you had any extra business, or unique interactions you don't usually get."
    mc.name "You'll see! It'll make a difference, I'm sure!"
    the_person "I guess it couldn't hurt to try it once. Okay, but nothing too crazy! And it needs to still cover everything!"
    mc.name "Of course. Let me just put something together."
    "You step into the shop and try to piece together an outfit for [the_person.possessive_title]."
    "Note: For an outfit to be acceptable at this time, it must have a sluttiness score between 30 and 50, and tits and vagina should NOT be visible!"
    $ acceptable_outfit = False
    while not acceptable_outfit:
        $ clear_scene()
        call outfit_master_manager(slut_limit = 50, show_overwear = False, show_underwear = False, start_mannequin = the_person) from _call_outfit_master_manager_starbuck_dressup_intro_01
        $ dressup_outfit = _return
        if sex_shop_owner_outfit_check(dressup_outfit):
            "You pick out an acceptable outfit for [the_person.possessive_title]."
            $ acceptable_outfit = True
        else:
            "You pick out an outfit for [the_person.possessive_title], but quickly realise it doesn't meet her requirements."
            "Note: For an outfit to be acceptable at this time, it must have a sluttiness score between 30 and 50, and tits and vagina should NOT be visible!"

    $ the_person.next_day_outfit = dressup_outfit
    $ sex_shop_wardrobe.add_outfit(dressup_outfit)
    $ the_person.event_triggers_dict["dressup_testing"] = True
    $ the_person.event_triggers_dict["dressup_count"] = 1
    $ the_person.event_triggers_dict["dressup_finish_day"] = day + 2
    "You bring the outfit back to [the_person.title]."
    $ the_person.draw_person()
    mc.name "Here. This is kind of what I was thinking."
    the_person "Ah... I see. This is definitely a bit showier than I would normally wear."
    "She thinks for a moment."
    the_person "But, I can see where you are going with this."
    "She finally nods."
    the_person "Alright. I'll do it. I'll let you know how it goes!"
    mc.name "Great! Glad to hear it."
    $ add_starbuck_dressup_recap_action()
    return

label starbuck_dressup_recap_label(the_person): #Obedience break event #1
    $ the_person.event_triggers_dict["dressup_testing"] = False
    $ first_time = (the_person.event_triggers_dict.get("dressup_count", 2) == 1)
    $ sb_convinced = (the_person.event_triggers_dict.get("dressup_count", 2) >= 3)
    $ outcome_convince = False
    "You swing by the sex shop. You want to talk to [the_person.title] and see how it went wearing her uniform yesterday."
    if first_time:
        "While it's hard to know for sure, you feel she should have sold more products in the outfit you picked out for her."
    else:
        "You feel like one more day of higher sales should be enough to establish a pattern of increased sales."
    $ the_person.draw_person()
    "You step up to the counter where [the_person.possessive_title] is working."
    mc.name "Good day [the_person.title]."
    "She looks at you a bit sheepish."
    the_person "Ah, hello [the_person.mc_title]."
    mc.name "So... How'd it go?"
    if first_time:
        the_person "How'd what go?"
        mc.name "Ah don't be coy. You know I'm asking about how yesterday went with your enhanced uniform."
        "She blushes a bit, but nods."
        the_person "Ah yes... that..."
        the_person "It went good. It was embarrassing, but I definitely noticed a difference with customer interactions."
    elif sb_convinced:
        the_person "It went really well, actually. I had one really great customer interaction!"
        the_person "This couple came in, and the girl started dragging me all over the store, asking me all sorts of questions."
        the_person "They had just recently gotten together, and you could just feel the energy coming from her, and the excitement of exploring sex with her new partner."
        mc.name "That's great!"
    else:
        the_person "It went good. I had several interesting customer interactions outside what I normally get."
        the_person "A few of them even led to sales, I think."
    mc.name "What about overall sales?"
    the_person "They were up. Not a lot, and not really enough for me to say for certain it was because of my uniform."
    if sb_convinced:
        mc.name "Okay, maybe not just from one day... but this has been an ongoing thing now."
        mc.name "How many more days is it going to take to convince you that this is working?"
        the_person "I... I know... you're right."
    else:
        mc.name "Hmm... well what else could it have been?"
        the_person "I don't know, but even if sales are up a little, I'm not sure that wearing something like that every day is something I'm willing to do..."

    menu:
        "Admit it, you love wearing skimpy uniforms" if the_person.opinion.skimpy_uniforms >= 2:
            mc.name "[the_person.title]. Are you honestly going to tell me that you don't love wearing outfits that show off your amazing body?"
            the_person "I do enjoy it, but doing it just to drive sales feels... wrong."
            mc.name "But driving sales is just a secondary thing. It makes YOU feel good. And this is YOUR store. Right?"
            the_person "Well yeah..."
            mc.name "Isn't that enough? Do what makes you happy. And if the store gets a sales boost from it, that's just a bonus?"
            $ the_person.change_happiness(2)
            the_person "Do you really think it's okay?"
            mc.name "Yes."
            the_person "Oh [the_person.mc_title]... You're right!"
            $ the_person.draw_person(position = "kissing")
            "She reaches out and pulls you into a big hug."
            $ outcome_convince = True

        "Admit it, you love wearing skimpy uniforms\n{menu_red}Requires: Loves Skimpy Uniforms{/menu_red} (disabled)" if the_person.opinion.skimpy_uniforms < 2:
            pass

        "We need the sales boost\n{menu_red}Warning: Reduces Love{/menu_red}" if starbuck.event_triggers_dict.get("shop_progress_stage", 0) > 1:
            mc.name "Look, I don't really know how to be more blunt about this."
            mc.name "I've invested a lot of money into this store, and to have you waffling about a simple uniform is concerning."
            mc.name "Are you saying you aren't willing to do what it takes to make your business successful?"
            the_person "Of course! I want to succeed, but this just feels wrong..."
            mc.name "Tons of businesses use tactics like these. I'm going to need you to accept it if we are going to keep up our friendly business partnership."
            $ the_person.change_stats(happiness = -15, love = -5)
            "[the_person.title] looks hurt, but eventually nods."
            the_person "Fine. I'll do it."
            $ outcome_convince = True

        "We need the sales boost\n{menu_red}Requires: Higher Investment{/menu_red} (disabled)" if starbuck.event_triggers_dict.get("shop_progress_stage", 0) <= 1:
            pass

        "The results are conclusive" if sb_convinced:
            mc.name "Let's stop pretending. The results are conclusive. Wearing an enhanced uniform is good for your business."
            mc.name "Be honest with yourself too. You kind of enjoy it, don't you?"
            the_person "I do, but it just felt wrong."
            the_person "But I think it was just something I needed to try for myself a few times. I think I've gotten used to it now."
            the_person "I agree with you."
            $ outcome_convince = True

        "The results are conclusive\n{menu_red}Requires: More attempts{/menu_red} (disabled)" if not sb_convinced:
            pass

        "Understood" if not sb_convinced:
            mc.name "I understand. Maybe we should try again?"
            the_person "No, I don't think that is a good idea. I just don't feel comfortable with it."

    if outcome_convince:
        the_person "You're going to help me with the uniforms though... right?"
        the_person "I need a man's opinion to make sure I hit the sweet spot. Not too sexy, not too tame."
        mc.name "Of course. Start with what we already have, and we can expand from there."
        the_person "Okay. Just let me know when you want to make changes."
        "[the_person.possessive_title!c] will now wear a uniform when she is working at the sex shop."
        "You can talk to her anytime to see a list of her uniforms and change them accordingly."
        "For now, she accepts full outfits with a sluttiness higher than 30 and less than her own sluttiness, and that covers her privates."
        "If things keep going though, you wonder if you could convince her to push her limits even further..."
        $ starbuck.progress.obedience_step = 3    #This should unlock all her uniform related dialogue options
        $ add_starbuck_underwear_intro_action()
        $ the_person.event_triggers_dict["shop_promo_market_rate"] += 0.2
    else:
        $ add_starbuck_dressup_retry_action()
        $ the_person.change_obedience(-10)
        "[the_person.title] isn't willing to wear a sexy uniform regularly yet, but you feel like if you can get her obedient enough, she would give it another try."
    $ clear_scene()
    #cleanup
    $ del first_time
    $ del sb_convinced
    $ del outcome_convince
    return

label starbuck_dressup_retry_label(the_person): #Convince her to try dressing up again.
    $ the_person.draw_person()
    "You walk up to [the_person.possessive_title] at the counter."
    "You feel like it is time to try and get her to wear a skimpier uniform again. You decide to convince her."
    mc.name "Hello [the_person.title]. How are you doing today?"
    the_person "Hey [the_person.mc_title]. I'm doing good. You?"
    mc.name "Pretty good. I have something I wanted to ask you."
    the_person "Yeah?"
    mc.name "Last time we ran that experiment on your work outfit, it was good but kind of inconclusive. I want to run another outfit test."
    the_person "Outfit? I mean... we talked about that..."
    mc.name "I know, but if I'm being honest, I really think this is something that will help your business succeed."
    mc.name "I only want what is best for you and the business, and I know you disagree a bit, but I think the idea merits another experiment."
    the_person "I... I don't know..."
    "She mumbles."
    mc.name "Don't worry. You did great last time, it'll just be one day."
    mc.name "I'll even pick out a different outfit for you."
    "She sighs."
    the_person "Fine. If it'll satisfy your curiosity. Pick something out, and I'll wear it tomorrow."
    mc.name "Excellent."
    $ clear_scene()
    "You step away from the counter and pick her out something to wear."
    "Note: For an outfit to be acceptable, it must have a sluttiness score between 30 and 50, and tits and vagina should NOT be visible!"
    $ acceptable_outfit = False
    while not acceptable_outfit:
        $ clear_scene()
        call outfit_master_manager(slut_limit = 50, show_overwear = False, show_underwear = False, start_mannequin = the_person) from _call_outfit_master_manager_starbuck_dressup_intro_02
        $ dressup_outfit = _return
        if sex_shop_owner_outfit_check(dressup_outfit):
            "You pick out an acceptable outfit for [the_person.possessive_title]."
            $ acceptable_outfit = True
        else:
            "You pick out an outfit for [the_person.possessive_title], but quickly realise it doesn't meet her requirements."
            "Note: For an outfit to be acceptable at this time, it must have a sluttiness score between 30 and 50, and tits and vagina should NOT be visible!"

    $ the_person.next_day_outfit = dressup_outfit
    $ sex_shop_wardrobe.add_outfit(dressup_outfit)
    $ the_person.event_triggers_dict["dressup_testing"] = True
    $ the_person.event_triggers_dict["dressup_count"] += 1
    $ the_person.event_triggers_dict["dressup_finish_day"] = day + 2
    "You bring the outfit back to [the_person.title]."
    $ the_person.draw_person()
    mc.name "Here. This is kind of what I was thinking."
    the_person "Alright. I'll wear it tomorrow and we'll see what happens."
    mc.name "Great! Glad to hear it."
    $ add_starbuck_dressup_recap_action()
    return

label starbuck_underwear_intro_label(the_person):   #160 obedience. We can give her underwear as a uniform
    $ starbuck.progress.obedience_step = 4
    "In this label, we convince [the_person.title] to try wearing underwear only as her outfit."
    "She is willing to do it, but requires that everything remains covered up."
    $ add_starbuck_underwear_recap_action()
    pass

return

label starbuck_underwear_recap_label(the_person):
    "In this label, we recap how it went wearing just underwear as the shop owner."
    "She states that it definitely worked, but that she doesn't feel comfortable with it, beginning her limit break mechanic."
    pass
    $ starbuck.progress.obedience_step = 5
    $ add_starbuck_underwear_retry_action()
return

label starbuck_underwear_retry_label(the_person):
    "In this label, we convince Starbuck to try wearing underwear as the shop owner again."
    "She agrees."
    pass
    $ add_starbuck_underwear_recap_action()
return

label starbuck_trial_room_label(the_person):    #180 obedience, we convince her to make a trial room.
    $ starbuck.progress.obedience_step = 6

    pass

label starbuck_trial_legal_trouble_label(the_person):   #Follow up. Starbuck faces legal trouble.


    pass
    return

label starbuck_bribery_attempt_label(the_person):   #We attempt to convince Starbuck to bribe the cop


    pass
    return

label starbuck_bribery_final_label(the_person): #We manage to convince Starbuck to bribe the cop.

    $ starbuck.progress.obedience_step = 7
    return


label starbuck_nudity_label(the_person):    #200 obedience. We convince her to work exposed.

    $ starbuck.progress.obedience_step = 8
    return

label starbuck_nudity_recap_label(the_person):

    pass
    $ starbuck.progress.obedience_step = 9
return

label starbuck_nudity_retry_label(the_person):

    pass
return
# label starbuck_test_outfit_label():
#     $ clear_scene()
#     $ the_person = starbuck
#     "This is a test of the limited wardrobe selector."
#     call screen girl_outfit_select_manager(sex_shop_wardrobe.wardrobe, slut_limit = 40, show_sets = True)
#     "We give it a minute."
#     "Now make sure the changes worked."
#     call screen girl_outfit_select_manager(sex_shop_wardrobe.wardrobe, slut_limit = 40, show_sets = True)
#     "test complete."
#     return
