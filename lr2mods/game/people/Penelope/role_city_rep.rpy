## Holds all of the information required for the city rep who visits your company when Attention gets too high.
#TODO: write our requirements. Remember to check if "currently_interrogating" is True if it's explicitly for a bribe, if not we've met her somewhere else!
label city_rep_negotiate(the_person):
    mc.name "This is a waste of everyone's time. I'm sure you have better things to be doing today."
    the_person "I go where the city sends me. That's all."
    mc.name "Couldn't we come to some sort of agreement so this isn't necessary? What does the city need to stay out of my hair?"
    if the_person.love < 0:
        the_person "They need you to stop peddling unregulated, unethical pharmaceuticals. Do you think you can do that for me?"
        mc.name "That's my whole business..."
        the_person "Then I suppose we'll be seeing a lot of each other."
    elif the_person.love < 25:
        the_person "It would help if you stopped selling unregulated pharmaceuticals, but I don't think you can really do that."
        the_person "If you could get a restricted goods business license there would be far fewer questions, but those are particularly hard to obtain."
        mc.name "How would I get one?"
        the_person "You? Oh, you don't. You would need someone to vouch for the importance of this business. Someone like me."
        the_person "And frankly, I don't think you deserve one. You're a nice enough man [the_person.mc_title], but I take my work very seriously."
        mc.name "So if I change your mind you could get me one of those licenses?"
        "She shrugs non-committally."
    else:
        the_person "Assuming you want to stay in business? What you really need is a restricted goods business license."
        mc.name "And how would I get one of those?"
        the_person "Well... The first step would be having someone vouch for the importance of this business to the welfare of the city."
        the_person "Someone like me."
        mc.name "Would you do that for me?"
        "She thinks for a moment."
        the_person "It would be a big risk for me. This isn't the most savoury business, and if one of my higher-ups reviews my work there could be trouble."
        $ obedience_requirement = 130 - 10*the_person.opinion.being_submissive
        menu:
            "Pay her\n{menu_red}Costs: $2500{/menu_red}" if mc.business.has_funds(2500):
                mc.name "I can pay you for it. I'm sure there are application fees, extra taxes, and so on..."
                the_person "[the_person.mc_title], are you trying to bribe me?"
                mc.name "Of course not! But if you're taking a risk, you deserve to be compensated. Consider it insurance in case something does go wrong."
                "A longer pause this time."
                the_person "Okay, I'll arrange for the paperwork to be put through."
                mc.name "And I'll be sending you your funds. Thank you for your help [the_person.title]."
                the_person "Don't make me regret this."
                $ mc.business.change_funds(-2500, stat = "Policies")
                $ purchase_policy(attention_floor_increase_2_policy,ignore_cost = True)
                $ mc.log_event("Business License acquired", "float_text_green")

            "Pay her\n{menu_red}Requires: $2500{/menu_red} (disabled)" if not mc.business.has_funds(-2500):
                pass

            "Order her" if the_person.obedience >= obedience_requirement:
                mc.name "That's a risk you're going to have to take. Get me that license."
                $ the_person.change_love(-5 + 2*the_person.opinion.being_submissive)
                "[the_person.title] seems unhappy with being ordered around, but she nods obediently anyways."
                the_person "Fine, I'll sort out the paperwork for you."
                $ purchase_policy(attention_floor_increase_2_policy,ignore_cost = True)
                $ mc.log_event("Business License acquired", "float_text_green")

            "Order her\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
                pass

            "Never mind":
                mc.name "I wouldn't want you to put your career in danger. I'm sure I can figure something else out."
                the_person "You've proven to be quite ingenious to date, so I don't doubt it."
    return

label city_rep_bribe(the_person):
    $ add_bribe_attempt("cash_bribe")
    mc.name "This is a waste of everyone's time. Isn't there some sort of fee I can pay you and we can all get back to doing real work?"
    if the_person.love < 0:
        the_person "I hope you aren't trying to bribe me [the_person.mc_title]."
        mc.name "Of course not, I was just trying to move this along a little more quickly."
        the_person "Unfortunately I do not believe that will be possible. You should get comfortable with the wait."
    else:
        the_person "That sounds an awful lot like you're trying to offer me a bribe [the_person.mc_title]."
        mc.name "Of course it's not a bribe, but I understand there's a cost to all of this administrative work you are doing."
        mc.name "So if you could just tell me what that cost is I could pay it, right now."
        $ bribe_cost = 1000
        if the_person.obedience < 80:
            $ bribe_cost = 2000

        elif the_person.obedience < 120:
            pass

        else:
            $ bribe_cost = 500

        "She considers this for a moment."
        the_person "That sounds quite reasonable. For a simple fee of, oh... $[bribe_cost] I think we can avoid any further punishments."
        menu:
            "Pay the bribe\n{menu_red}Costs: $[bribe_cost]{/menu_red}" if mc.business.has_funds(bribe_cost):
                mc.name "That seems like a reasonable cost of doing business. I can send the money over right away."
                "She seems a little surprised that you've taken her up on her offer."
                the_person "Excellent. When my men come back I'll let them know that we've already settled your fine and that we're done here."
                $ the_person.change_obedience(2)
                $ mc.business.change_funds(-bribe_cost, stat = "City Fines")
                $ the_person.event_triggers_dict["bribe_successful"] = "cash"


            "Pay the bribe\n{menu_red}Requires: $[bribe_cost]{/menu_red} (disabled)" if not mc.business.has_funds(bribe_cost):
                pass

            "Refuse to pay":
                mc.name "Well, maybe we should just wait until your thugs are back."
                the_person "They're perfectly respectable governmental employees, thank you very much."
    return

label city_rep_seduce(the_person): #TODO: Figure out if we can have something like this trigger automatically if you seduce her by groping her or something
    $ add_bribe_attempt("seduction_attempted")
    mc.name "It seems like we have some time to spare [the_person.title]."
    "You step close to her and put your hand on the small of her back."
    if not the_person.has_taboo("vaginal_sex"):
        mc.name "How about we head to my office and I give you another good fucking while your thugs are running around this place."
    else:
        mc.name "How about we head to my office and get to know each other better while your thugs are searching the place."
    $ should_fuck = False
    if the_person.effective_sluttiness() < 20: #Offended
        $ the_person.change_love(-1)
        "She slaps your hand away and glares at you."
        the_person "Please, let's keep this professional."
        "You hold your hands up innocently and wait a few minutes for her to cool off."
    elif the_person.effective_sluttiness() < 40: #Tempted, but not convinced
        "She tenses under your touch, but doesn't pull away."
        the_person "Tempting, but I don't think that would be a wise idea. It's important that I appear impartial."
        the_person "If anyone suspects we are involved with each other there might be serious repercussions."
        menu: #TODO: Think of some other ways to convince her. Opinion based?
            "Order her" if the_person.obedience >= 120:
                mc.name "I'm not going to stand around and let you rob me without getting something else in return."
                "You push on her back and have her start walking towards your office."
                the_person "You make it sound like I'm sort of prostitute."
                "After a few steps she realises that this is happening one way or another and falls into line."
                mc.name "Maybe I can convince you to let me keep my stuff."
                mc.name "Then you'll just be a slut. Better?"
                the_person "Hardly."
                $ should_fuck = True

            "Order her\n{menu_red}Requires: 120 Obedience{/menu_red} (disabled)" if the_person.obedience < 120:
                pass

            "Let it go":
                mc.name "You're probably right."
                "You wait a few minutes in silence."


    else: #Hell yeah (TODO: Have an option for her to proposition you when she shows up instead)
        "She leans into you, pressing her weight into your side."
        the_person "I thought you'd never ask. Your office is a good idea, I think we'd cause a bit of a scene if we stayed here..."
        $ should_fuck = True

    if should_fuck:
        $ mc.change_location(ceo_office)
        "You lead her into your office and lock the door behind you."
        $ ceo_office.lock()  # special case we don't want to be disturbed
        if the_person.vaginal_sex_count > 3 and renpy.random.randint(0, 1) == 0:
            the_person "Why don't you lie down on the couch [the_person.mc_title] and let met have a ride today."
            mc.name "That sounds like a great idea, [the_person.title]."
            call mc_sex_request(the_person, the_request = "cowgirl", start_object = ceo_office.get_object_with_name("White Leather Couch")) from _call_mc_sex_request_city_rep_seduce
        else:
            call fuck_person(the_person, private = True) from _call_fuck_person_city_rep_seduce
        $ ceo_office.unlock()
        $ the_report = _return
        $ the_person.draw_person()
        if the_report.get("girl orgasms", 0) > 0:
            $ the_person.event_triggers_dict["bribe_successful"] = "orgasm"
            mc.name "I trust I've given you sufficient reason to take your thugs and leave?"
            "[the_person.possessive_title!c] is still breathing heavy, recovering from her climax."
            the_person "What? Oh... Fine, I'll call off my men."
            $ the_person.change_obedience(2)
            the_person "But nobody can know about this, understood?"
            mc.name "Of course [the_person.title]. It will be our little secret."
        else:
            $ the_report = _return
            $ the_person.call_dialogue("sex_review", the_report = the_report)
        the_person "Just a moment, please."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
        "After she got cleaned up, you move back to the lobby."
        $ mc.change_location(lobby)
    return

label city_rep_order(the_person):
    $ add_bribe_attempt("order_attempted")
    if the_person.obedience < 110:
        mc.name "[the_person.title], you're going to stop with this stupid charade. There isn't going to be any punishment today."
        "She smirks and glares at you."
        the_person "You really think that? You don't have any power here [the_person.mc_title]."
        the_person "Now take a breath and get yourself under control before you say something that makes this worse for yourself."

    elif the_person.obedience < 130:
        mc.name "[the_person.title], you need to make this go away for me."
        the_person "I can't just snap my fingers and make it go poof [the_person.mc_title]."
        the_person "There's paperwork, bosses to report to, a whole system."
        mc.name "But you can bypass all of that, right?"
        the_person "Only if I want to get fired! No, no, you're stuck with whatever punishment the rulebook lays out for you."

    else:
        mc.name "[the_person.title], you're going to make all of this go away for me. Change whatever paperwork you have to."
        if the_person.is_submissive:
            "[the_person.possessive_title!c] doesn't argue. She just nods her head obediently."
            the_person "Yes [the_person.mc_title], I'll make it happen."
            $ the_person.event_triggers_dict["bribe_successful"] = "order"
            mc.name "That's what I like to hear."
        else:
            the_person "I can't do that [the_person.mc_title], there would be so much trouble for me if someone found out."
            "Even as she protests she sounds unsure, as if uncertain about disobeying you."
            menu:
                "Do this and we're even":
                    mc.name "Do it anyways. I won't ask you to do anything else if you can do this for me."
                    the_person "Well... If it's just this once I think I can manage it..."
                    $ the_person.event_triggers_dict["bribe_successful"] = "order"
                    $ the_person.change_obedience(-5)

                "Forget it":
                    mc.name "Fine, forget about it then."
                    the_person "I'm sorry, if there was any way I could do it safely I would!"


    return


label city_rep_dressup_training(the_person):
    mc.name "[the_person.title], I'm sure you get bored of these stuffy work uniforms you have to wear."
    the_person "... Sometimes I want to wear something more fun..."
    mc.name "Of course you do. Let's talk about that and give you something a lot more fun to wear next time..."
    "You describe your ideal uniform for her."
    "NOTE: since she is a city employee, her outfit must be legal in public"
    call outfit_master_manager(slut_limit = the_person.sluttiness + 30, show_overwear = False, show_underwear = False, start_mannequin = the_person, outfit_validator = city_rep_outfit_check) from _call_outfit_master_manager_city_rep_dressup_training
    $ the_person.draw_person()
    if _return:
        $ add_city_rep_advocates_topless_is_legal()
        $ the_uniform = _return
        $ city_rep.primary_job.add_outfit(the_uniform)
        "She listens attentively. At one point she even starts taking notes."
        if the_uniform.vagina_visible:
            the_person "... But everyone at the office will be able to see my..."
            mc.name "Say it."
            the_person "They'll be able to see my pussy, [the_person.mc_title]."
            "She doesn't sound very worried about it, but that might just be the trance taking hold."
            the_person "Won't I get in trouble?"
            mc.name "I'm sure you can come up with something. Maybe you need to start working from home."
            $ the_person.discover_opinion("showing her ass")
            $ the_person.change_slut(the_person.opinion.showing_her_ass)
            the_person "But... I want to go to the office like this."
            mc.name "Then I hope your boss likes what he sees and decides to keep you around."
            "She nods obediently."
        elif the_uniform.tits_visible:
            the_person "But everyone at the office will see my..."
            mc.name "Say it."
            the_person "They'll be able to see my tits. I'll be showing my tits to everyone."
            "She doesn't sound very worried about it, but that might just be the trance taking hold."
            the_person "What if I get in trouble?"
            mc.name "I doubt anyone will complain much. Everyone likes to ogle a good set of tits."
            $ the_person.discover_opinion("showing her tits")
            $ the_person.change_slut(the_person.opinion.showing_her_tits)
            "She bites her lips and nods obediently."
        elif the_uniform.underwear_visible:
            the_person "But I'll barely be covered..."
            mc.name "You're going to like it."
            "It's not a suggestion, it's a command. She nods."
            the_person "Okay. What if my boss comments on my outfit?"
            mc.name "Tell him he's welcome to look as much as he wants."
            mc.name "He probably has a boring job, he should be thanking me for giving him some eye candy."
            "She nods obediently."
        the_person "Okay, I'll go and buy everything I need tonight."
        mc.name "Good girl."
        return True
    return False


label city_rep_penalty_reduction_training(the_person):
    mc.name "[the_person.title], these penalties my business is being hit with are going to ruin me."
    mc.name "I need you to reduce them for me."
    "She shakes her head weakly."
    the_person "I can't... There are rules about this sort of thing..."
    mc.name "I'm sure they're more like guidelines. You're a smart girl, I'm certain you can figure something out."
    "The trance takes hold and she nods obediently."
    the_person "Okay, I'll figure something out."
    $ the_person.event_triggers_dict["city_rep_reduced_penalties_trained"] = True
    "All penalties levied by the city will now be reduced by 50%%."
    return


label city_rep_internal_sabotage_training(the_person):
    mc.name "[the_person.title], all of these visits are nice, but I'd like a little less attention from the city."
    mc.name "I want you to start destroying any evidence about me that crosses your desk."
    "She shakes her head weakly."
    the_person "I... I can't do that [the_person.mc_title]. It's not what I'm supposed to do."
    mc.name "It is now, because I'm telling you to do it."
    "She resists a moment longer, but she can only hold out so long while in a trance."
    the_person "Okay, I'll get rid of anything I can..."
    mc.name "Good girl."
    $ purchase_policy(attention_bleed_increase_2_policy, ignore_cost = True)
    "The attention that your business generated will now decrease by another 10%% per day."
    return

label city_rep_offer_hire(the_person):
    mc.name "Tell me [the_person.title], have you ever thought about finding work in the private sector?"
    mc.name "I'm sure you could make a lot more money at, random example, a friendly pharmaceutical company."
    "She shakes her head, dismissing the idea."
    the_person "I don't do this for the money, I do it for the people."
    the_person "It's not glamorous, but I know that I'm making a difference and keeping people safe."
    mc.name "Surely there's something I could offer you to change your mind."
    "She smiles politely and shakes her head again."
    the_person "Sorry [the_person.mc_title], I'm not for sale."
    return

label city_rep_discuss_topless_is_legal(the_person):
    $ the_person.draw_person()

    the_person "Hello [the_person.mc_title], could we discuss something important?"
    mc.name "Hello [the_person.title], of course, what would you like to talk about?"

    the_person "Well, it's about the work outfit you designed for me."
    mc.name "Yes?"
    the_person "I would like it to be more liberating."
    mc.name "I see."
    the_person "The problem is that current public decency acts don't allow for any city employee to wear anything more revealing."
    the_person "I think it would be possible to bring this up in the city counsel, but I would require some backing from another official."
    mc.name "What do you propose?"
    the_person "If we could get our police chief Ms. [police_chief.last_name] to co-sign and have enough funds to grease the wheels, we could change the law."
    mc.name "That does sound interesting, how much funding would that require?"
    the_person "About $75,000."
    mc.name "Ah, well that's a lot of cash, what would I get out of this?"
    "She puts her hands on your crotch and starts rubbing your cock."
    the_person "You would be able to dress me up in a slutty outfit that would show off my [the_person.tits_description] for everyone to see."
    the_person "And I'm guessing it would benefit your business if the city was more liberal."
    mc.name "You might be right and I wouldn't mind seeing you run around with your tits on display."
    the_person "Should we go somewhere private so I can give you a preview?"
    menu:
        "Go somewhere more private":
            call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_city_rep_discuss_topless_is_legal
            the_person "Okay, now I want you to imagine seeing this walking into the door when I visit your offices."
            $ the_person.strip_to_tits()
            $ the_person.break_taboo("bare_tits")
            "After removing her clothes, she cups her breasts squeezing them together."
            the_person "Mmmm, would you like that [the_person.mc_title]?"
            $ the_person.draw_person(position = "kissing")
            "She walks up to you and wraps her arms around your neck and whispers in your ear..."
            the_person "I want you touch me... I want you to satisfy me... like the little slut I am..."
            call fuck_person(the_person, start_position = standing_grope, start_object = make_floor(), private = _return, skip_intro = True) from _call_fuck_person_city_rep_discuss_topless_is_legal
            $ the_person.draw_person()
            mc.name "You do make a convincing argument [the_person.title]."
            the_person "I do, don't I?"
            mc.name "Let's talk a walk and discuss this some more."
            call mc_restore_original_location(the_person) from _call_mc_restore_original_location_city_rep_discuss_topless_is_legal

        "Another time":
            mc.name "We can do that another time."
            $ the_person.change_stats(happiness = -5, slut = -1, love = -1)
            "She pouts a little, rather disappointed."
            "You talk for a while longer working out some of the minor details."

    $ the_person.draw_person()
    mc.name "Well, let me see what I can arrange. As soon as I figure it out, I'll get back to you."
    the_person "Thank you [the_person.mc_title], I look forward to hearing from you."
    $ city_rep.event_triggers_dict["discussed_topless_is_legal"] = True
    return
