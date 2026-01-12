# Contains all of the code related to the punishment events, used when an employee has broken a rule of some sort.

# LEVEL 1

label punishment_verbal_scolding(the_person, the_infraction): #Note: Pass the infraction so we can reference it if we want.
    "You stare down [the_person.title] and shake your head."
    mc.name "What makes you think this was acceptable?"
    if the_person.obedience < (110 - (15*the_person.opinion.being_submissive)):
        the_person "I..."
        "You hold up your hand."
        mc.name "Stop. I don't want to hear excuses or half-baked reasons."
    else:
        "[the_person.possessive_title!c] looks meekly at the floor."
        mc.name "Look at me."
        $ the_person.draw_person(emotion = "sad")
        "She raises her head slowly and looks you in the eye."
    mc.name "I need you get it through your head that what I want are results."
    $ the_person.change_stats(happiness = -2 + the_person.opinion.being_submissive, obedience = 1 + the_person.opinion.being_submissive)
    $ the_person.discover_opinion("being submissive")
    menu:
        "Keep going":
            # Insult her work ethic. More obedience, lowers happiness
            mc.name "I expect results because I'm paying you for those results. If you can't deliver I'll have to cut your pay, or cut you loose."
            mc.name "You need to get yourself together and improve, because right now you're letting everyone down."
            if the_person.obedience < (100 - (15*the_person.opinion.being_submissive)):
                "She opens her mouth to respond, but stops herself at the last moment."
                $ the_person.draw_person(emotion = "angry")
                "Instead she simply glares at you and nods."
            else:
                "[the_person.title] listens and nods apologetically, remaining silent the whole time."
            $ the_person.change_stats(happiness = -5 + (2*the_person.opinion.being_submissive), obedience = 2 + the_person.opinion.being_submissive)
            menu:
                "Insult her":
                    mc.name "Frankly, I'm not sure you really even deserve to be here."
                    mc.name "There were plenty of eager applicants who could have had your job, and I'm sure they could have followed simple instructions."
                    if the_person.obedience < (90 - (15*the_person.opinion.being_submissive)):
                        "She clenches her fists and grits her teeth, but finally she can take no more."
                        the_person "Do I deserve to be here? I... I can't believe you!"
                        the_person "I come in every day and work my hardest, and this is the thanks I get?"
                        $ the_person.draw_person(position = "walking_away")
                        "She scoffs and turns around to walk away."
                        mc.name "I haven't dismissed you yet, if you leave there will be further disciplinary actions."
                        the_person "Discipline this!"
                        $ the_person.change_stats(happiness = -10, love = -4, obedience = -2)
                        "[the_person.title] puts up one hand and gives you the finger over her shoulder, storming out of the room."
                        $ the_person.add_infraction(Infraction.disobedience_factory())
                        return

                    else:
                        $ the_person.draw_person(emotion = "sad")
                        "[the_person.title] seems disheartened and docile, waiting in silence until you finish."
                        "You wait a moment to let your words sink in."
                        mc.name "I'm glad you understand. Now, get back to work and stop wasting my time."
                        $ the_person.change_stats(happiness = -10, love = -2, obedience = 2 + the_person.opinion.being_submissive)

                    # More obedience, lowers happiness and Love
                    # Low obedience girls or girls who dislike being submissive may mouth back at you, generating a more severe infraction (at the cost of stats to get there though.)

                "Let her go":
                    mc.name "Do you understand me?"
                    the_person "Yes [the_person.mc_title], I understand."
                    mc.name "Good. Now get back to work, you're wasting everyone's time."


        "Let her go":
            mc.name "Do you understand me?"
            the_person "Yes, [the_person.mc_title]."
            mc.name "Good. Now get back to work, you've wasted enough time already."

    $ clear_scene()
    return

label punishment_wrist_slap(the_person, the_infraction):
    mc.name "Let's get this over with. Put your hands out, palms down."
    if the_person.obedience < (110 - (15*the_person.opinion.being_submissive)):
        "[the_person.title] hesitates for a split second before moving her hands out."
    else:
        "[the_person.title] nods and moves her hands."

    $ play_spank_sound()
    "You take her left hand in yours to hold it steady., holding it steady, and give it a fast slap."
    if the_person.obedience < (120 - (15*the_person.opinion.being_submissive)):
        "[the_person.possessive_title!c] gasps and instinctively tries to pull her hand away."
        the_person "Ow, that stings..."
    else:
        "[the_person.possessive_title!c] closes her eyes briefly, but bears her punishment without comment."

    $ play_spank_sound()
    "You switch hands and repeat the process, smacking the back of [the_person.title]'s right hand."
    if the_person.obedience < (120 - (15*the_person.opinion.being_submissive)):
        the_person "Ouch..."
    elif the_person.is_submissive:
        the_person "Ah..."
    else:
        "[the_person.title] doesn't react beyond a short catch in her breath."

    $ the_person.change_stats(love = -1 + the_person.opinion.being_submissive, obedience = 2 + the_person.opinion.being_submissive)

    the_person "I'm sorry [the_person.mc_title], it won't happen again."
    menu:
        "Keep going":
            mc.name "I hope not, or I'll have to find some way to actually get through to you."
            "She tries to gently pull her hand back, but you keep your grip on it."
            $ play_spank_sound()
            "You give it another hard slap across the back, and this time she jumps slightly."
            if the_person.obedience < (120 - (15*the_person.opinion.being_submissive)):
                the_person "Ach... How many times do you need to do this, exactly?"
                mc.name "Until I think you've learned your lesson."
            else:
                the_person "Oh..."

            "You continue, alternating between hands. After a few strikes the backs of [the_person.title]'s hands are starting to turn red."
            $ the_person.change_stats(love = -2 + the_person.opinion.being_submissive, obedience = 2 + the_person.opinion.being_submissive)
            "When you're satisfied you let go of her hands. She holds them, rubbing their backs gingerly."
            mc.name "Have you learned your lesson?"
            the_person "Yes [the_person.mc_title], I have."
            mc.name "Good. I don't enjoy this, but I'll continue to do what is necessary to maintain good discipline in my staff."
            "She nods obediently."


        "Let her go":
            "You let go of her hands. She holds them, rubbing their backs gingerly."
            mc.name "It better not, or I won't be so gentle with you."
            $ the_person.change_love(1 + the_person.opinion.being_submissive)
            if the_person.is_submissive:
                the_person "If you need to be rough with me I understand. Sometimes I deserve it."
                the_person "Thank you [the_person.mc_title]."
            else:
                the_person "I understand."

    mc.name "Now get back to work."
    $ clear_scene()
    return

label punishment_serum_test(the_person, the_infraction):
    mc.name "To make up for your disappointing actions, you're going to help the company further its research goals."
    mc.name "I have a dose of serum here. You're going to take it, so we can observe the effects."
    "[the_person.possessive_title!c] nods."
    the_person "Alright, hand it over."
    call give_serum(the_person) from _call_give_serum_31
    if _return:
        $ the_person.change_obedience(1)
        "You hand [the_person.title] the small vial. She looks at it for a moment, then removes the stopper at the top and drinks the contents down."
        the_person "Is that all?"
        menu:
            "Make her pay for it" if mandatory_unpaid_serum_testing_policy.is_active:
                mc.name "Not quite. You're going to have to pay for that dose."
                if the_person.obedience >= 130:
                    the_person "Right, of course."
                else:
                    the_person "What? But this was your idea, why do I need to pay?"
                    mc.name "It's already company policy that I can have you test serum whenever I need you to."
                    mc.name "As this is a punishment, you have forfeit the right to any special company access. You need to pay for it just like anyone else."
                    "She sighs."
                    the_person "This should be illegal. Fine."
                    $ the_person.change_stats(love = -1, obedience = 1)

                $ cost = int(mc.business.get_serum_sales_value(_return))
                "[the_person.title] hands over the market value of $[cost] for the dose you gave her."
                $ mc.business.change_funds(cost, stat = "Serum Sales")

            "Make her pay for it\n{menu_red}Requires Policy: Mandatory Unpaid Serum Testing{/menu_red} (disabled)" if not mandatory_unpaid_serum_testing_policy.is_active:
                pass

            "Let her go":
                pass

        mc.name "That's all for now. I may need to speak with you to record the effects of that dose."
        "She seems slightly nervous, but nods."


    else:
        mc.name "Your punishment will have to wait until later. I don't have the material I need at the moment."
        "She seems slightly apprehensive, but nods."
        $ the_person.add_infraction(the_infraction, add_to_log = False) #The infraction is about to be cleared, we re-add it so the end result is as if this never happened.

    $ clear_scene()
    return

# LEVEL 2

label punishment_office_busywork(the_person, the_infraction):
    # The employee gains +1 Obedience every work day, but the company loses an extra company efficiency.

    mc.name "As punishment, for the next week you are expected to carry out all the basic busywork of the office."
    mc.name "If the printer needs paper, you fill it. If someone needs coffee, you get it for them."
    "[the_person.title] nods their understanding."
    mc.name "If I don't hear a glowing review from your coworkers by the end of the week there will be further disciplinary action."
    mc.name "Your punishment does not, of course, absolve you of your normal duties."

    $ add_office_busywork_action(the_person)
    return

label punishment_spank(the_person, the_infraction):
    mc.name "I have no choice but to punish you for your infraction. Turn around and put your hands on the desk."
    if not the_person.is_submissive: #She complains
        the_person "What are you going to do?"
        mc.name "You're going to put your hands on the desk, bend forward, and I'm going to spank you."
        the_person "Really? I don't think that's..."
        mc.name "Company policy is clear as day. Would you prefer to see what the punishment is for disobedience?"
        "She hesitates, then sighs and turns around and plants her hands flat on the desk."
        the_person "Fine..."

    else: #She follows instructions rightaway
        "[the_person.title] follows your instructions without any hesitation."

    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "standing_doggy")

    "You stand to the side of [the_person.possessive_title] and place one hand on her hip, ready to spank her with the other."
    #If she has a skirt on, option to pull it up.
    $ top_clothing = the_person.outfit.get_lower_top_layer
    if top_clothing and top_clothing.can_be_half_off and top_clothing.half_off_gives_access and top_clothing.hide_below and not top_clothing.anchor_below and not top_clothing.underwear:
        menu:
            "Pull up her [top_clothing.display_name] first":
                if not the_person.is_submissive and the_person.effective_sluttiness("underwear_nudity") < 30:
                    "You grab the hem of [the_person.title]'s [top_clothing.display_name]."
                    the_person "Hey! What are you doing?"
                    mc.name "Making sure your [top_clothing.display_name] doesn't get in the way of your punishment."
                    the_person "Are... Are you allowed to do that?"
                    if reduced_coverage_uniform_policy.is_active:
                        mc.name "Of course, I have authority over everything you wear."
                    else:
                        mc.name "No clothing is being removed, so yes I can."
                    "You pull her [top_clothing.display_name] up and leave it bunched around her waist."
                else:
                    "You grab the hem of [the_person.title]'s [top_clothing.display_name] and pull it up around her waist."

                $ mc.change_locked_clarity(10)
                $ the_person.draw_animated_removal(top_clothing, position = "standing_doggy", half_off_instead = True)
                if not the_person.outfit.wearing_panties:
                    mc.name "No panties today, I see."

                $ the_person.update_outfit_taboos()

            "Leave her [top_clothing.display_name] in place":
                pass

    call spank_description(the_person, the_infraction) from _call_spank_description
    $ the_person.review_outfit()
    $ clear_scene()
    return

label spank_description(the_person, the_infraction):
    $ play_spank_sound()
    "You rub her butt briefly, then slap it hard."
    $ not_cushioned = the_person.vagina_available or the_person.outfit.are_panties_visible
    $ play_spank_sound()
    if not_cushioned: #ouch!
        "Your hand makes a satisfying smack as it makes contact with her ass cheek. Her ass jiggles for a few moments before settling down."
        the_person "Ah... That really stings..."
    else: #Not too bad.
        "Her clothing absorbs some of the blow, but you still make good contact and set her ass jiggling for a moment."
        the_person "Ah..."

    menu:
        "Go easy on her":
            $ play_spank_sound()
            "You give her butt a few more smacks, alternating between her left and right cheek, and then step back."
            if the_person.is_submissive:
                the_person "Is that all? I thought this would go on longer..."
                $ the_person.outfit.restore_all_clothing()
                $ the_person.draw_person()
                "She seems disappointed as she stands up straight."
            else:
                the_person "Are we done?"
                $ the_person.outfit.restore_all_clothing()
                $ the_person.draw_person()
                "She stands up straight, massaging her butt."
            mc.name "We're done. Get back to work."

            $ the_person.change_obedience(2)
            the_person "Right away."

        "Teach her a lesson":
            $ play_spank_sound()
            "You keep smacking her butt, putting more force behind your blow each time."
            if not_cushioned: #Ass gets red, she gets sore.
                $ mc.change_locked_clarity(10)
                "Her exposed ass jiggles with each hit, and quickly starts to turn red."
                the_person "Ah... Am I almost done [the_person.mc_title]?"

                if the_person.is_submissive: #She likes it and is getting turned on.
                    $ play_spank_sound()
                    "You spank her again, and she moans."
                    $ play_moan_sound()
                    $ the_person.discover_opinion("being submissive")
                    $ the_person.change_arousal(5*the_person.opinion.being_submissive)
                    the_person "I... Don't know if I can take much more of this! Mmph..."

                else:
                    $ play_spank_sound()
                    "You spank her again, making her gasp."
                    the_person "I... Don't know how much more of this I can take!"

                mc.name "You'll take it until I think you have learned your lesson. Do you understand?"
                $ play_spank_sound()
                "Another smack, another ass jiggle."
                if the_person.is_submissive:
                    the_person "Yes [the_person.mc_title]! I understand! Ah!"
                else:
                    "She lowers her head and grits her teeth."

                    the_person "Yes [the_person.mc_title]. Ah..."

                mc.name "Do you have anything to say for your actions?"
                if the_person.is_submissive:
                    the_person "It won't happen again [the_person.mc_title], I..."
                    $ play_spank_sound()
                    "You interrupt her with a slap on the ass. She pauses, then continues."
                    the_person "I'm sorry to let you down, and I see just how wrong I was now! Ah!"

                else:
                    $ play_spank_sound()
                    the_person "Ow... It won't happen again [the_person.mc_title], I... Ow!"
                    $ play_spank_sound()
                    "You interrupt her with a slap on the ass. She takes a moment to collect herself before continuing."
                    the_person "I promise it won't happen again!"

                $ mc.change_locked_clarity(10)
                $ play_spank_sound()
                "You give her one last hit on her now red butt and then step back, letting her stand up."
                $ the_person.outfit.restore_all_clothing()
                $ the_person.draw_person()
                if the_person.is_submissive:
                    $ the_person.change_stats(arousal = 5 * the_person.opinion.being_submissive, obedience = the_person.opinion.being_submissive)
                    the_person "Thank you [the_person.mc_title]. I promise I'll do better."
                else:
                    $ the_person.change_stats(love = -2 + the_person.opinion.being_submissive, obedience = 3)
                    the_person "Finally. Ow..."
                mc.name "I expect you've learned your lesson. Now get back to work, you've wasted enough time already."

            else: #Doesn't particularly mind."
                $ play_spank_sound()
                if top_clothing:
                    "[the_person.title] jerks forward with each strike, but her [top_clothing.display_name] seems to be saving her from the worst of it."
                else:
                    "[the_person.title] jerks forward with each strike, but she doesn't seem to mind getting spanked."
                $ play_spank_sound()
                the_person "Ah... Ow..."
                "After a few more strikes it's clear you aren't having the effect on [the_person.possessive_title] that you were hoping for."
                $ play_spank_sound()
                "You give her one last slap on the ass and step back."
                mc.name "Stand up, we're done here."
                $ the_person.outfit.restore_all_clothing()
                $ the_person.draw_person()
                $ mc.change_locked_clarity(10)
                "She turns around, rubbing her butt."
                the_person "I'll get back to work..."
                $ the_person.change_stats(love = -1, obedience = 2)
    return

label punishment_underwear_only(the_person, the_infraction):
    mc.name "You've let me down [the_person.title], and more importantly you've let down the entire company."
    mc.name "Strip down to your underwear."
    if the_person.should_wear_uniform:
        mc.name "You don't deserve to wear your uniform, so for the rest of the week you won't."
    else:
        mc.name "You can consider that your official uniform for the rest of the week."

    if not (the_person.has_underwear): # Whoops, not wearing underwear today! Tough luck.
        the_person "I... I can't do that [the_person.mc_title]."
        mc.name "What do you mean you can't? These are the rules you agreed with to work here, if you..."
        "She shakes her head and interrupts you."
        $ slut_requirement = 40
        if not the_person.is_wearing_underwear:
            the_person "No, I mean I can't strip down to my underwear because... I'm not wearing any."
            $ slut_requirement = 60
            $ slut_requirement += -(5*the_person.opinion.not_wearing_anything)

        elif not the_person.outfit.wearing_bra:
            the_person "No, I mean I can't strip down to my underwear because... I'm not wearing a bra."
            the_person "My... breasts would be out."
            $ slut_requirement += -(5*the_person.opinion.showing_her_tits)

        else: #not wearing panties
            the_person "No, I mean I can't strip down to my underwear because... I'm not wearing any panties."
            $ slut_requirement += -(5*the_person.opinion.showing_her_ass)

        "You consider this for a moment, then shrug."
        mc.name "That's unfortunate, but your inability to wear a decent outfit doesn't absolve you of your punishment."
        the_person "So you still want me to..."
        mc.name "Strip. Now."

        if the_person.effective_sluttiness() < slut_requirement:
            # She's not slutty enough to do it, she'll defy you and accept a disobedience infraction instead.
            "[the_person.possessive_title!c] shuffles nervously."
            the_person "I don't think I can do it. I'm sorry [the_person.mc_title]."
            mc.name "If you're refusing the only choice I have is to write you up for disobedience, which will carry an even heavier penalty."
            $ the_person.change_stats(happiness = -5, obedience = -1)
            the_person "I'm sorry, but I just can't do it. I'll accept a worse punishment if I have to."
            $ the_person.add_infraction(Infraction.disobedience_factory())
            mc.name "Fine, we'll do it your way."
            $ clear_scene()
            return
        else:
            $ the_person.change_stats(happiness = -5, obedience = 2 + the_person.opinion.being_submissive)
            "Your words seem to shock her into action."

    elif the_person.obedience < (130 - (10*the_person.opinion.being_submissive)): # She's not very obedient
        if the_person.effective_sluttiness("underwear_nudity") < 40:
            $ the_person.draw_person(emotion = "angry")
            the_person "You... You can't make me do that!"
            if reduced_coverage_uniform_policy.is_active:
                mc.name "Of course I can, it's company policy. I could even tell you what underwear to wear if I wanted, but I'm keeping this simple."
            else:
                mc.name "Of course I can. It's company policy that I set the uniform you have to wear, and I'm telling you that it's nothing over your underwear."
                mc.name "You have the freedom to wear any style of underwear you like, or none at all, under your uniform. I hope you've dressed appropriately today."

            mc.name "You lost any right to complain when you failed to follow company policy in the first place."
            the_person "But... It's not..."
            mc.name "Strip. Now."
            "[the_person.possessive_title!c] glares at you, and for a moment you think she is going to refuse."
            the_person "Fine."
            $ the_person.change_obedience(1 + the_person.opinion.being_submissive)
        else: #Not obedient, but slutty enough to not care
            "[the_person.title] seems to relax a little."
            the_person "Okay, I understand."
    else:
        if the_person.effective_sluttiness("underwear_nudity") < 40:
            # Obedient but very shy about it
            "She blushes and looks away."
            the_person "Are you sure [the_person.mc_title]? I'm not used to... being undressed in front of people."
            mc.name "Of course I'm sure. Now strip."
            "She nods meekly."
            the_person "Okay, if you say I have to..."

        else:
            # Obedient and slutty, the perfect combination
            "[the_person.title] nods obediently."
            the_person "Yes [the_person.mc_title], I'll go change into my new uniform."
            mc.name "You'll change right here. Now strip."
            the_person "Of course. Right away."

    python:
        generalised_strip_description(the_person, the_person.outfit.get_underwear_strip_list())
        mc.change_locked_clarity(20)

    if the_person.update_outfit_taboos() or the_person.effective_sluttiness() < 40:
        "[the_person.possessive_title!c] blushes and tries to cover her body."
        the_person "This is so embarrassing..."

    python:
        the_person.current_job.forced_uniform = the_person.outfit.get_copy()
        the_person.wear_uniform()
        slut_change = 0
        if the_person.tits_visible:
            slut_change += the_person.opinion.showing_her_tits
        if the_person.vagina_visible:
            slut_change += the_person.opinion.showing_her_ass
        if the_person.tits_visible and the_person.vagina_visible:
            slut_change += the_person.opinion.not_wearing_anything
        the_person.change_slut(slut_change, 40)

    call notify_other_girls_in_department(the_person) from _call_notify_other_girls_in_department_punishment_underwear_only

    mc.name "I expect you to stay in your new uniform for the rest of the week. Any deviation from it and there will be further punishments."
    mc.name "Understood?"
    the_person "Yes, [the_person.mc_title]."
    mc.name "Good. We're done here."
    return

# LEVEL 3 #

label punishment_pay_cut(the_person, the_infraction): #There is a similar option in the performance review, but this doesn't have a chance for her to quit and has reduced happiness penalties.
    mc.name "As punishment for your rules infraction I will be cutting your pay."
    the_person "By how much?"
    python:
        minor_amount = builtins.int(0.05 * the_person.current_job.salary)
        mod_amount = builtins.int(0.15 * the_person.current_job.salary)
        maj_amount = builtins.int(0.25 * the_person.current_job.salary)
        if minor_amount <= 1:
            minor_amount = 1
        if mod_amount <= 3:
            mod_amount = 3
        if maj_amount <= 5:
            maj_amount = 5
        # Cap the reduction so we can't end up with a negative salary (Although this would be an interesting extra punishment!
        if minor_amount >= the_person.current_job.salary:
            minor_amount = the_person.current_job.salary
        if mod_amount >= the_person.current_job.salary:
            mod_amount = the_person.current_job.salary
        if maj_amount >= the_person.current_job.salary:
            maj_amount = the_person.current_job.salary

    menu:
        "Minor cut\n{menu_green}Profit: $[minor_amount:.2f] / day{/menu_green}":
            mc.name "I'm going to be generous. Your pay will only be cut by $[minor_amount:.2f] per day."
            $ the_person.current_job.salary -= minor_amount
            $ the_person.change_stats(happiness = -2, obedience = 1)
            $ the_person.draw_person(emotion = "sad")
            "[the_person.possessive_title!c] seems upset by the news, but she nods her understanding."
            mc.name "Good. Now get back to work."

        "Moderate cut\n{menu_green}Profit: $[mod_amount:.2f] / day{/menu_green}":
            mc.name "You will see a $[mod_amount:.2f] reduction in your daily pay, effective immediately."
            $ the_person.current_job.salary -= mod_amount
            $ the_person.change_stats(happiness = -5, obedience = 2)
            $ the_person.draw_person(emotion = "sad")
            if not the_person.is_submissive:
                "[the_person.possessive_title!c] seems upset by the news, but she nods obediently."
                the_person "Of course. Thank you [the_person.mc_title], for being so understanding."
            else:
                the_person "I... Is there anything else I can do to make it up? That's a big cut."
                mc.name "If you impress me with your performance maybe you'll earn a raise."
                "She seems uncertain, but nods."
            mc.name "Good, now get back to work before I have to write you up again."


        "Major cut\n{menu_green}Profit: $[maj_amount:.2f] / day{/menu_green}":
            mc.name "There will be a $[maj_amount:.2f] cut to your daily pay, effective immediately."
            $ the_person.current_job.salary -= maj_amount
            $ the_person.change_stats(happiness = -10, obedience = 3)
            $ the_person.draw_person(emotion = "sad")
            if not the_person.is_submissive:
                "[the_person.possessive_title!c] seems shocked for a moment, but finally nods obediently."
                the_person "I... I understand. I'm sorry for letting you down like this [the_person.mc_title]..."
                mc.name "Don't let it happen again. Now get back to work."
                the_person "Right away."
            else:
                "[the_person.possessive_title!c] seems shocked for a moment before responding."
                the_person "Are you sure? That seems like a very big change."
                mc.name "Well, I need to make sure you've learned your lesson."
                mc.name "If you are unhappy with your pay you're welcome to quit."
                "She shakes her head."
                the_person "No, I don't want to do that. I... I understand."
                mc.name "Good, now don't let it happen again. Now get back to work."
                the_person "Right away, [the_person.mc_title]."

    $ clear_scene()
    return

label punishment_strip_and_spank(the_person, the_infraction):
    mc.name "It's time for your disciplinary punishment [the_person.title]."
    the_person "What are you going to do?"
    mc.name "I'm going to bend you over and spank you, until you've learned your lesson."

    if not ((the_person.vagina_available or the_person.vagina_visible) and (the_person.tits_available or the_person.tits_visible)): #She's wearing something, let's strip her down.
        mc.name "But first we need to ensure there's nothing that will get in my way. Strip naked."
        call strip_naked_command_helper(the_person, the_infraction) from _call_strip_naked_command_helper
        $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list(strip_feet = _return))
        $ mc.change_locked_clarity(15)
        if the_person.update_outfit_taboos(): #Being nude has broken a taboo
            "[the_person.title] stands meekly in front of you, completely nude. She tries to cover herself up with her hands."
            mc.name "Hands down, there's no point hiding anything from me now."
            "She frowns, but follows your instructions. She lowers her hands to her sides, letting you get a good view of her body."
        mc.name "Good girl. Now put your hands on the desk, bend over, and stick your ass out for your punishment."

    else: #Already basically nude.
        mc.name "You're already dressed for the occasion, so let's get right to it."
        mc.name "Hands on the desk, bend over, and stick your ass out for your punishment."

    $ the_person.draw_person(position = "standing_doggy")
    call spank_description(the_person, the_infraction) from _call_spank_description_1
    $ the_person.review_outfit()
    $ clear_scene()
    return

label punishment_office_nudity(the_person, the_infraction):
    mc.name "I have decided on a suitable punishment for your violation of company rules."
    mc.name "You're going to spend the rest of the week working while nude."
    if not (the_person.tits_available and the_person.vagina_available and the_person.tits_visible and the_person.vagina_available): #Something to strip
        mc.name "Let's start by having you strip down."
        call strip_naked_command_helper(the_person, the_infraction) from _call_strip_naked_command_helper_1
        $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list(strip_feet = _return))
        $ mc.change_locked_clarity(15)
        if the_person.update_outfit_taboos(): # Broke a taboo
            "[the_person.title] stands meekly in front of you, completely nude. She tries to cover herself up with her hands."
            mc.name "Hands down, there's no point hiding anything from me now."
            "She frowns, but follows your instructions. She lowers her hands to her sides, letting you get a good view of her body."

        mc.name "Good. Now I want you to consider this your uniform for the rest of the week."

    else:
        mc.name "You're already undressed for the occasion, consider this your uniform for the rest of the week."

    python:
        the_person.current_job.forced_uniform = the_person.outfit.get_copy()
        the_person.wear_uniform()
        slut_change = 0
        if the_person.tits_visible:
            slut_change += the_person.opinion.showing_her_tits
        if the_person.vagina_visible:
            slut_change += the_person.opinion.showing_her_ass
        if the_person.tits_visible and the_person.vagina_visible:
            slut_change += the_person.opinion.not_wearing_anything
        the_person.change_slut(slut_change, 60)

    call notify_other_girls_in_department(the_person) from _call_notify_other_girls_in_department_punishment_office_nudity

    mc.name "If I find you attempting to wear anything else there will have to be further punishments."
    mc.name "Understood?"
    the_person "Yes [the_person.mc_title], I understand."
    mc.name "Good, now get back to work."
    return

label notify_other_girls_in_department(the_person):
    if the_person.location.person_count <= 1:
        return

    $ scene_manager = Scene()
    $ scene_manager.add_group([x for x in the_person.location.people if x != the_person][:5])
    $ scene_manager.add_actor(the_person, display_transform = character_right)
    mc.name "Let this be a lesson to all of you, [the_person.fname] decided she didn't need to follow regulations."
    mc.name "If any you might get the same idea, this could be you next time."
    $ the_watcher = max(scene_manager.current_actors, key = lambda x: x.obedience)
    the_watcher "Yes [the_watcher.mc_title], thank you!"

    "It seems the girls watching are a little more obedient."
    python:
        for x in scene_manager.current_actors:
            x.change_stats(happiness = -1, obedience = 1, add_to_log = False)
        the_watcher = None
        scene_manager.clear_scene()
        the_person.draw_person()
    return

label strip_naked_command_helper(the_person, the_infraction): #Helper function for events that need a girl to strip naked.
    $ remove_shoes = False
    if not the_person.is_submissive and the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) < 60:
        # not obedient or slutty enough to do it without comment.
        "[the_person.title] hesitates and looks away."
        the_person "Isn't there something else I could do? Do you really need me to be naked?"
        mc.name "I've made my decision. Get naked, or your punishment will only be worse."
        "She sighs and nods."
        the_person "Yes [the_person.mc_title]."

        $ the_item = the_person.outfit.get_feet_top_layer
        if the_item:
            the_person "Can I keep my [the_item.display_name] on?"
            menu:
                "Strip it all off":
                    mc.name "Take it all off, I don't want you to be wearing anything."
                    $ remove_shoes = True

                "Leave them on":
                    mc.name "Fine, you can leave them on."
        $ the_item = None

    else: # No big deal, she just gets right to it
        "She nods and starts to strip immediately."
        $ the_item = the_person.outfit.get_feet_top_layer
        if the_item:
            the_person "Would you like me to take off my [the_item.display_name] too?"
            menu:
                "Strip it all off":
                    mc.name "Take it all off, I want you naked."
                    $ remove_shoes = True

                "Leave them on":
                    mc.name "Fine, you can leave them on."
        $ the_item = None

    return remove_shoes

# LEVEL 4 #

label punishment_office_humiliating_work(the_person, the_infraction):
    mc.name "As punishment for your flagrant disregard of company policy you responsible for the cleaning of this office for the next week."
    mc.name "Contact the cleaning agency for the building and inform them they will not be needed."
    if the_person.int >= 3 and not the_person.is_submissive: #She went to university, she doesn't want to scrub toilets!
        the_person "You... expect me to clean up after everyone in here?"
        mc.name "I do. I expect you to be scrubbing toilets, washing floors, and taking out the garbage."
        the_person "I have a degree! This is just a complete waste of my time!"
        mc.name "I hope you'll learn some humility during your punishment. Of course, I also expect you to keep up with your normal work."
        the_person "I don't know how you can expect that [the_person.mc_title], there aren't enough hours in the day!"
        mc.name "You better figure it out, or there will be further punishments when you're done."
        mc.name "Maybe you'll think about this next time you think about ignoring company rules."
        "[the_person.title] is about to respond, but you wave your hand and cut her off."
        mc.name "There's nothing to discuss here, I've made my decision. Call the cleaning company and get back to work."
        the_person "I... Fine. Right away, [the_person.mc_title]."
    else:
        mc.name "I expect you to be scrubbing toilets, washing floors, and taking out the garbage."
        the_person "Understood [the_person.mc_title]."
        mc.name "Of course, I expect you to keep up with your normal responsibilities as well."
        the_person "I'll do my best, [the_person.mc_title]."
        mc.name "Good. If I find there have been performance issues there will have to be further disciplinary action."
        "She nods her understanding."
        mc.name "We're done here, you can get back to work."
        the_person "Right away, [the_person.mc_title]."

    $ add_humiliating_work_action(the_person)
    return

label punishment_orgasm_denial(the_person, the_infraction):
    mc.name "It's time for your punishment [the_person.title]."
    the_person "What are you going to do?"
    mc.name "We'll get to that. First, I need you to strip down."
    call strip_naked_command_helper(the_person, the_infraction) from _call_strip_naked_command_helper_2

    $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list(strip_feet = _return))

    if the_person.update_outfit_taboos(): # Broke a taboo
        "[the_person.title] stands meekly in front of you, completely nude. She tries to cover herself up with her hands."
        mc.name "Hands down, there's no point hiding anything from me now."
        "She frowns, but follows your instructions. She lowers her hands to her sides, letting you get a good view of her body."

    mc.name "Good, now we can get started."
    "You step close to [the_person.possessive_title] and cup one of her breasts, squeezing it softly."
    mc.name "You've really disappointed me [the_person.title], so in return..."
    "You place your other hand on her hip."
    mc.name "... I'm going to disappoint you. I'm going to bring you right to the edge of cumming and leave you there."
    if the_person.effective_sluttiness() < 40:
        the_person "You can't... You aren't allowed to do that, are you?"
        $ mc.change_locked_clarity(10)
        "You slide your hand from her hip down to her inner thigh."
        mc.name "Of course I can, punishments are all listed in the employee manual. Of course, if you'd prefer to quit I can walk you to the door."
        if reduced_coverage_uniform_policy.is_active:
            mc.name "Your clothing is company property though, so you'd be walking out of that door naked."
        "She stands frozen in place as you caress her body. She finally mutters out her answer."
        the_person "I'll take my punishment, [the_person.mc_title]... I doubt you'll even get me close."
        mc.name "Good girl. I won't make you wait any longer..."
    elif the_person.effective_sluttiness() < 80:
        the_person "Okay [the_person.mc_title], I'll take my punishment."
        $ mc.change_locked_clarity(10)
        "You slide your hand from her hip down to her inner thigh."
        mc.name "Good girl."
    else:

        the_person "You wouldn't be that cruel, would you [the_person.mc_title]?"
        the_person "Come on, wouldn't it be better if we both enjoyed ourselves?"
        mc.name "I fully intend to enjoy myself with you, but you aren't going to get to cum."
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title!c] pouts while you slide your hand from her hip down to her inner thigh."
        mc.name "So be a good girl and take your punishment."

    "You move behind [the_person.possessive_title], keeping one hand between her legs and the other massaging a tit."
    $ the_person.break_taboo("touching_body")
    $ the_person.add_situational_obedience("punishment", 20, "I'm being punished, I don't have any right to refuse.")
    call fuck_person(the_person, private = False, start_position = standing_grope, start_object = mc.location.objects_with_trait("Stand")[0], skip_intro = True, affair_ask_after = False) from _call_fuck_person_92
    $ the_report = _return
    $ the_person.clear_situational_obedience("punishment")
    $ the_person.draw_person()

    if the_report.get("girl orgasms", 0) == 0: #Successfully didn't let her orgasm.
        if the_report.get("end arousal", 0) >= 95 : # Got her very close
            the_person "No [the_person.mc_title], you can't... You can't leave me like this!"
            $ play_moan_sound()
            "She moans desperately."
            if the_person.wants_creampie and the_person.opinion.vaginal_sex > -2:
                $ mc.change_locked_clarity(15)
                the_person "Please, just fuck me and make me cum! You can cum inside me, I don't care!"
                the_person "I need it!"
                $ the_person.add_situational_slut("orgasm denial", 10, "I was so close! I need to cum, I need to!")
                menu:
                    "Fuck her":
                        mc.name "Beg for it."
                        the_person "Please, I... I want you to fuck me! Fuck me and cum inside me, I want it!"
                        $ mc.change_locked_clarity(15)
                        the_person "Put that cock in me before I go crazy!"
                        call fuck_person(the_person, private = False, skip_condom = True, affair_ask_after = False) from _call_fuck_person_93
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 0:
                            mc.name "I hope that satisfied you."
                            the_person "It was everything I needed it to be. Ah..."
                            $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 80)
                            $ the_person.draw_person()
                            mc.name "Good, now get back to work."
                            the_person "Yes [the_person.mc_title], right away."
                        else:
                            the_person "No, no, no, you can't... Not again!"
                            mc.name "Sorry [the_person.title], but you need to learn your lesson."
                            the_person "Fuck... I'm so horny, I can't think straight!"
                            mc.name "If I catch you trying to pleasure yourself, or having someone else do it for you, there will be further punishments."
                            mc.name "Do you understand?"
                            $ the_person.change_stats(happiness = -5, obedience = 4)
                            $ the_person.draw_person()
                            the_person "I understand [the_person.mc_title]..."
                            mc.name "Good, now get back to work."

                    "Ignore her pleas":
                        mc.name "Need it or not, this is your punishment."
                        mc.name "If I catch you trying to pleasure yourself, or having someone else do it for you, there will be further punishments."
                        mc.name "Do you understand me?"
                        the_person "I... Oh fuck, fine. I understand."
                        $ the_person.change_stats(happiness = -5, obedience = 4)
                        $ the_person.draw_person(emotion = "sad")
                        mc.name "Good, now get back to work."
                        the_person "Yes [the_person.mc_title]."

            else:
                mc.name "I can, and I am. If I catch you trying to pleasure yourself, or having someone else do it for you, there will be further punishments."
                mc.name "Do you understand?"
                the_person "I understand [the_person.mc_title]..."
                mc.name "Good. Now get back to work, you've wasted enough of our time."
                the_person "Yes [the_person.mc_title]."


        elif the_report.get("end arousal", 0) >= 80: # Reasonably high
            the_person "God, I was getting close... Fuck."
            "She groans unhappily."
            mc.name "Good, that's the point. If I catch you trying to pleasure yourself, or having someone else do it for you, there will be further punishments."
            the_person "I understand... God this is going to be hard!"
            $ the_person.change_stats(happiness = -5, obedience = 3)
            $ the_person.draw_person(emotion = "sad")
            mc.name "Get back to work, It'll take your mind off of it."
            the_person "Yes [the_person.mc_title]."


        elif the_report.get("end arousal", 0) >= 50: # At least you tried
            the_person "Ah... Ah..."
            mc.name "If I catch you trying to pleasure yourself, or having someone else do it for you, there will be further punishments."
            the_person "Right, I understand [the_person.mc_title]."
            $ the_person.change_stats(happiness = -5, obedience = 2)
            $ the_person.draw_person(emotion = "sad")
            mc.name "Good, now get back to work."
            the_person "Yes [the_person.mc_title]."

        else: #You didn't even try
            the_person "So, are we done?"
            mc.name "We are, and if I catch you trying to pleasure yourself, or having someone else do it for you, there will be further punishments."
            the_person "I understand, but I think I'll be able to manage."
            $ the_person.change_obedience(1)
            $ the_person.draw_person(emotion = "sad")
            mc.name "Get back to work, you've wasted enough time already."
            the_person "Yes [the_person.mc_title]."

    else: #You let her cum. Woops.
        the_person "Ah, that was nice..."
        mc.name "It wasn't supposed to be nice, it was supposed to be a punishment."
        the_person "Do you want to punish me some more?"
        $ the_person.change_stats(obedience = -3, slut = 2, max_slut = 60)
        $ the_person.draw_person(emotion = "happy")
        "You sigh and give up."
        mc.name "Get back to work, or I'll come up with something more unpleasant."
        the_person "Yes [the_person.mc_title]."

    $ clear_scene()
    return

label punishment_forced_punishment_outfit(the_person, the_infraction):
    #TODO: In the future some clothing items should only be possible through this (and other) special events
    mc.name "I've decided on a suitable punishment for your violation of company rules."
    if not (the_person.tits_available and the_person.vagina_available and the_person.tits_visible and the_person.vagina_available): #Something to strip
        mc.name "Let's start by having you strip down."

        call strip_naked_command_helper(the_person, the_infraction) from _call_strip_naked_command_helper_3

        $ generalised_strip_description(the_person, strip_list = the_person.outfit.get_full_strip_list(strip_feet = _return))

        if the_person.update_outfit_taboos(): # Broke a taboo
            "[the_person.title] stands meekly in front of you, completely nude. She tries to cover herself up with her hands."
            mc.name "Hands down, there's no point hiding anything from me now."
            "She frowns, but follows your instructions. She lowers her hands to her sides, letting you get a good view of her body."
        the_person "What now, [the_person.mc_title]?"
    else:
        the_person "What is it going to be, [the_person.mc_title]?"

    mc.name "I've put together a special outfit for you. It will be your outfit for the rest of the week."
    call outfit_master_manager(wardrobe = mc.business.punishment_wardrobe, show_overwear = False, show_underwear = False, start_mannequin = the_person) from _call_outfit_master_manager_punishment_forced_punishment_outfit
    $ the_outfit = _return
    if not isinstance(the_outfit, Outfit):
        "You consider what to dress [the_person.possessive_title] for a moment, then shrug."
        mc.name "On second thought, I think wearing nothing at all suits a disobedient slut like you."
        mc.name "Consider this your uniform for the rest of the week. Do you understand?"
        $ the_person.current_planned_outfit = the_person.outfit

    else:
        "You collect the clothing from a stash in your office and hand it over to [the_person.title]."
        mc.name "Get changed."
        "She nods obediently."
        $ the_person.apply_outfit(the_outfit, show_dress_sequence = True)
        "You watch as she gets changed. When [the_person.possessive_title] is finished she stands in front of you."

        $ the_person.current_planned_outfit = the_outfit
        if the_person.effective_sluttiness() < the_person.outfit.outfit_slut_score:
            the_person "Is this it? This is so embarrassing..."

    python:
        the_person.current_job.forced_uniform = the_person.outfit.get_copy()
        the_person.wear_uniform()
        slut_change = 0
        if the_person.tits_visible:
            slut_change += the_person.opinion.showing_her_tits
        if the_person.vagina_visible:
            slut_change += the_person.opinion.showing_her_ass
        if the_person.tits_visible and the_person.vagina_visible:
            slut_change += the_person.opinion.not_wearing_anything
        the_person.change_slut(slut_change, 30)

    mc.name "If I find you attempting to wear anything else there will have to be further punishments."
    mc.name "Understood?"
    the_person "Yes [the_person.mc_title], I understand."
    mc.name "Good, now get back to work."

    $ clear_scene()
    return

# LEVEL 5 #

label punishment_unpaid_intern(the_person, the_infraction):
    mc.name "Because of your actions, I have no choice but to slash your salary."
    the_person "Slash how badly?"
    mc.name "Completely. Right down to zero. The next week you will be working as an unpaid intern."
    $ the_person.draw_person(emotion = "sad")
    if the_person.obedience < 150:
        $ the_person.change_stats(happiness = -20, love = -5)
        the_person "You can't do that, how am I going to live?"
        mc.name "I can, and I am. I could fire you if I wanted to, but I want to give you the chance to redeem yourself."
        mc.name "You're welcome to quit, but with this on your record, well..."
        mc.name "You may have a hard time finding future employment without my reference."
        "[the_person.title] stands still for a moment, completely stunned."
        the_person "That's blackmail, there's no way this is legal."
        mc.name "You could hire a lawyer, but you should probably be a little more responsible with your finances."
        mc.name "If you work hard enough maybe you'll earn yourself a promotion to a paying position again."
        $ the_person.change_obedience(5)
        "[the_person.possessive_title!c] seems speechless."
        mc.name "I'll give you some time to process all of this. Your updated employee contract will be in the mail."

    else:
        $ the_person.change_stats(happiness = -10, obedience = 1)
        "[the_person.title] looks devastated, but after a moment of shock she nods."
        the_person "Right, I understand. Do you need anything else?"
        mc.name "You're taking this well..."
        the_person "You've made your decision, that's all I need to know [the_person.mc_title]."
        mc.name "Good, I'm glad to hear such dedication from you. Keep it up and I'm sure you'll earn a promotion."
        the_person "Thank you [the_person.mc_title], I'll try."


    "You leave [the_person.title] to consider her new position in the company."
    $ add_unpaid_intern_clear_punishment_action(the_person.current_job, the_person.current_job.salary)
    $ the_person.current_job.salary -= the_person.current_job.salary #You get nothing! Good day sir!
    $ clear_scene()
    return

label employee_unpaid_remove_label(job, restore_amount):
    $ job.salary += restore_amount
    return

label punishment_office_freeuse_slut(the_person, the_infraction):
    mc.name "It is time for your punishment to begin."
    the_person "What is it going to be, [the_person.mc_title]?"
    mc.name "Obviously, I could fire you, but I hope that your disobedience can be corrected instead."
    mc.name "This next week is going to be an exercise in obedience, because your body is going to be company property."
    mc.name "And I'm going to make sure you're well-used by the end of your punishment."
    if the_person.effective_sluttiness() + (10*the_person.opinion.being_submissive) < 40: #Not very slutty, needs it explained
        if the_person.obedience < 140: # Not obedient enough to let it happen without complaining.
            the_person "I don't understand, what does that even mean? I already have to show up to work, what else can I do?"
            mc.name "That's cute. Let me demonstrate what I mean."
            $ mc.change_locked_clarity(15)
            if the_person.has_large_tits:
                "You reach out and grab one of [the_person.title]'s hefty breasts."
            else:
                "You reach out and grab at one of [the_person.title]'s tits."
            mc.name "These tits are what I'm interested in, along with the rest of you."
            the_person "[the_person.mc_title]! I can't... You don't really expect me to just take this, do you?"
            mc.name "I do. all the punishments are laid out in the employee manual. I suggest you read through it at some point."
            mc.name "You're welcome to quit, but you might have a hard time finding future employment without a positive reference."
            "You play with her tits while she stands still, frozen by indecision."
            "She finally sighs and lowers her head."
            the_person "Just for a week... Fine."

        else: # Not slutty, but obedient enough to let it happen. Nun style answers
            the_person "I can show up for work earlier, if that's what you mean."
            mc.name "That's cute, but that's not what I mean. Let me demonstrate."
            $ mc.change_locked_clarity(15)
            if the_person.has_large_tits:
                "You reach out and grab one of [the_person.title]'s hefty breasts."
            else:
                "You reach out and grab at one of [the_person.title]'s tits."
            mc.name "These tits are what I'm interested in, along with the rest of you."
            the_person "Oh... I think I understand now."

    elif the_person.effective_sluttiness() + (10*the_person.opinion.being_submissive) < 80: #Moderately slutty, assumes you mean things like handjobs at first
        if the_person.obedience < 140:
            the_person "I think I can see where this is going. You want me to act all sexy around the office to keep you entertained."
            mc.name "That's cute, but not quite what I mean."
            $ mc.change_locked_clarity(15)
            if the_person.has_large_tits:
                "You reach out and grab one of [the_person.title]'s hefty breasts."
            else:
                "You reach out and grab at one of [the_person.title]'s tits."
            mc.name "You aren't going to just be teasing the office, you're going to have to put out."
        else: # Slightly shocked when you tell her she'll have to go "all the way", but that's all
            the_person "I understand [the_person.mc_title]. I will be yours to use, whenever you want me."
            mc.name "Good, I'm glad you've understood so quickly."

    else: #Very slutty, excited by the idea of being used.
        if the_person.obedience < 140: # Eager slut answer
            the_person "You're going to fuck me, [the_person.mc_title]? All week long?"
            $ mc.change_locked_clarity(10)
            "She doesn't seem very upset by the idea."
            the_person "I understand, if that's my punishment I accept it."
        else: # Obedient fuck slut answer
            $ mc.change_locked_clarity(20)
            the_person "Yes [the_person.mc_title]. My holes are yours to fuck whenever you want."
            the_person "I'll be your fuck slut to make up for my mistakes, and I promise to do better."

    mc.name "For the rest of the week you are to make yourself available to myself, all other employees, and visitors, during business hours."
    menu:
        "Give her an outfit to wear":
            mc.name "Nothing is off limits, I would like you the wear this outfit, to make it easier for everyone."
            call outfit_master_manager(wardrobe = mc.business.punishment_wardrobe, show_overwear = False, show_underwear = False, start_mannequin = the_person) from _call_outfit_master_manager_punishment_office_freeuse_slut
            $ the_outfit = _return
            if isinstance(the_outfit, Outfit):
                $ add_freeuse_role_and_clear_punishment_action(the_person, the_outfit)
                "You collect the clothing from a stash in your office and hand it over to [the_person.title]."
                mc.name "Get changed."
                "She nods obediently."
                $ the_person.apply_outfit(the_outfit, show_dress_sequence = True)

            else:
                mc.name "On second thought, just pick something that allows some easy access."
                $ add_freeuse_role_and_clear_punishment_action(the_person)
                mc.name "Go to the company locker and pick something out, I will check on you later."
                the_person "Yes sir, I will be ready."

        "Let her decide her outfit":
            mc.name "Nothing is off limits, and it would be easier for everyone involved if you wore something with easy access."
            $ add_freeuse_role_and_clear_punishment_action(the_person)
            mc.name "Do you understand?"
            "She nods obediently."

    mc.name "Good. Now get back to work, you've wasted enough of my time."
    return


# SPECIAL MC PUNISHMENTS


label punishment_service_mc_label(the_person, the_infraction):
    mc.name "It's time for your punishment [the_person.title]."
    the_person "What are you going to do?"
    mc.name "When you break company rules, you are being selfish. You're only serving yourself."
    mc.name "I think it's time you learned a lesson by servicing someone else. Namely, me."
    if the_person.effective_sluttiness() < 40:
        the_person "What do you mean?"
        "You step closer to her and put your hands on her shoulders."
        mc.name "Get down on your knees. It will be obvious momentarily."
        the_person "Wha... What? You can't be serious... You can't do that!"
        if the_person.is_employee:
            mc.name "Of course I can, punishments are all listed in the employee manual. Of course, if you'd prefer to quit I can walk you to the door."
        elif the_person.is_intern:
            mc.name "Of course I can, punishments are all listed in the employee manual. Of course, if you'd prefer I can remove you from the scholarship program."
        the_person "Fine... Just warn me when you get close [the_person.mc_title]... I don't want you finishing in my mouth."
        mc.name "I'll warn you if I please. Now get on your knees."
    elif the_person.effective_sluttiness() < 80:
        the_person "Okay [the_person.mc_title], I'll take my punishment."
        "You step closer to her and put your hands on her shoulders."
        mc.name "Good girl. Now get on your knees."
    else:
        the_person "Come on, wouldn't it be better if we both enjoyed ourselves?"
        mc.name "I fully intend to enjoy myself with you, but you aren't going to get anything in return."
        "[the_person.possessive_title!c] pouts while you step closer to her. You put your hands on her shoulders."
        mc.name "So be a good girl and get on your knees."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] sinks down to her knees while you reach down and pull out your cock. She tentatively sticks her tongue out and runs it over the tip."
    mc.name "It's going to take a bit more than that. Now open up."
    $ the_person.break_taboo("sucking_cock")
    "Finally relenting, [the_person.possessive_title] opens her mouth and takes you. While her technique isn't amazing, the soft confines of her mouth feels great."
    $ the_person.add_situational_obedience("punishment", 20, "I'm being punished, I don't have any right to refuse.")
    call fuck_person(the_person, private = False, start_position = blowjob, skip_intro = True, position_locked = True, affair_ask_after = False, condition = make_condition_blowjob_training()) from _call_custom_bj_punishment_01
    $ the_report = _return
    $ the_person.clear_situational_obedience("punishment")
    $ the_person.draw_person()

    if the_report.get("guy orgasms", 0) == 0: #She didn't finish you off. Berate her verbally.
        mc.name "I'm sorry, but that was not an acceptable performance. It seems you can't even get something as basic as sucking my cock done right."
        the_person "I'm... I'm sorry sir... I tried my best..."
        mc.name "I have a new punishment for you. I want you to practice sucking cock for the next week. Then come back to me and try again."
        the_person "That's... that's crazy!"
        mc.name "What's crazy is how bad at giving head you are. You heard me, now get back to work."
        $ the_person.change_stats(happiness = -5, obedience = 2)
        $ add_practice_cocksucking_work_action(the_person)
    else:
        "You give a sigh, satisfied after [the_person.possessive_title] drained your balls."
        mc.name "You look good like that. Next time this happens, I'll have you wear my cum on your face for the rest of the day."
        the_person "Yes sir..."
        $ the_person.change_stats(happiness = -5, obedience = 3)
        mc.name "Alright, I hope you learned something. Now get back to work."
    $ clear_scene()
    return

label employee_cocksucking_practice_remove_label(the_person):
    $ add_practice_cocksucking_report_action(the_person)
    return

label employee_cocksucking_practice_report_label(the_person):
    if not the_person.is_employee: #She doesn't work here, bail out!
        return

    $ the_person.draw_person()
    "[the_person.title] catches your attention while you are working."
    the_person "Do you have a moment [the_person.mc_title]?"
    mc.name "Sure, what do you need?"
    the_person "I wanted to let you know that I've finished my week of punishment."
    mc.name "Good. Show me."
    the_person "Like... right here?"
    "You put your hands on her shoulders."
    mc.name "There's no time like the present. Now get on your knees and give this another shot."
    the_person "Ahh... okay..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] sinks down to her knees while you reach down and pull out your cock. She tentatively sticks her tongue out and runs it over the tip."
    mc.name "It's going to take a bit more than that. Now open up."
    $ the_person.break_taboo("sucking_cock")
    "Finally relenting, [the_person.possessive_title] opens her mouth and takes you. While her technique isn't great, the soft confines of her mouth feel great."
    $ the_person.add_situational_obedience("punishment", 20, "I'm being punished, I don't have any right to refuse.")
    call fuck_person(the_person, private = False, start_position = blowjob, skip_intro = True, affair_ask_after = False, condition = make_condition_blowjob_training()) from _call_custom_bj_punishment_02
    $ the_report = _return
    $ the_person.clear_situational_obedience("punishment")
    $ the_person.draw_person(position = "kneeling1")

    if the_report.get("guy orgasms", 0) == 0: #She didn't finish you off. Berate her verbally.
        mc.name "God, that was awful. Are you sure you've been practising?"
        the_person "I'm... I'm sorry sir... I tried my best..."
        $ the_person.draw_person()
        mc.name "Fine... next time I'll just have you service me with a different hole."
        the_person "Yes sir."
        mc.name "It's crazy how bad at giving head you are. Now get back to work."
        $ the_person.change_stats(happiness = -5, obedience = 3)
    else:
        "You give a sigh, satisfied after [the_person.possessive_title] drained your balls."
        mc.name "Much better performance."
        $ the_person.draw_person()
        mc.name "You look good like that. Next time this happens, I'll have you wear my cum on your face for the rest of the day."
        the_person "Yes sir..."
        $ the_person.change_stats(happiness = -5, obedience = 4)
    mc.name "Alright, I hope you learned something. Now get back to work."
    $ clear_scene()
    return
