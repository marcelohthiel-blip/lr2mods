label serum_demand_label(the_person):
    # Description called when you use a girls obedience to have her take a dose of serum for you.

    if the_person.is_employee:
        mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this."
        "You pull out a vial of serum and present it to [the_person.title]."
        if mandatory_unpaid_serum_testing_policy.is_active:
            the_person "Sure no problem."
        else:
            the_person "What is it for, is it safe to take?"
            mc.name "Of course it is, you know about our testing procedures."
            the_person "Okay, I'm glad to help out."
    elif the_person.is_strip_club_employee:
        mc.name "[the_person.title], I'm testing a new type of energy booster, that would make it easier to work all night. Would you like to test it?"
        "You pull out a vial of serum and present it to [the_person.title]."
        if the_person.obedience < 150:
            the_person "I don't know [the_person.mc_title], is it dangerous."
            mc.name "Don't worry, it's completely safe, I just want to take care of my girls."
            the_person "Okay, then I will give it a try."
        else:
            the_person "Of course, you always take good care of us."
    elif the_person == nora:
        mc.name "[the_person.title], we're running field trials and I know you like to participate. I'm going to need you to take this."
        "You pull out a vial of serum and present it to [the_person.title]."
        the_person "I know you are a very capable bio chemist, so I'll be happy to help."
    else:
        mc.name "[the_person.title], you're going to drink this for me."
        "You pull out a vial of serum and present it to [the_person.title]."
        if the_person.obedience < 150:
            the_person "What is it for, is it important?"
            mc.name "Of course it is, I wouldn't ask you to if it wasn't."
            "[the_person.title] hesitates for a second, then nods obediently."
            the_person "Okay, if that's what you need me to do."
        else:
            the_person "Sure no problem."

    call give_serum(the_person) from _call_give_serum_enhanced_serum_demand
    return

label wardrobe_change_label(the_person):
    call screen main_choice_display(build_menu_items([build_wardrobe_change_menu(the_person)]))
    $ strip_choice = _return

    if strip_choice == "wardrobe":
        mc.name "[the_person.title], let's have a talk about what you've been wearing."
        $ clear_scene()

        call outfit_master_manager(wardrobe = the_person.wardrobe, start_mannequin = the_person, main_selectable = False, show_duplicate = False, show_export = False) from _call_outfit_master_manager_change_enhanced
        $ the_person.draw_person()

    elif strip_choice == "wear":
        mc.name "[the_person.title], I want you to get changed for me."
        $ clear_scene()
        call screen girl_outfit_select_manager(the_person.wardrobe, slut_limit = the_person.effective_sluttiness() + 20)
        if isinstance(_return, Outfit):
            $ the_person.current_planned_outfit = _return
            $ the_person.apply_planned_outfit()
            if the_person.update_outfit_taboos():
                "[the_person.title] seems nervous wearing her new outfit in front of you, but quickly warms up to it."
            the_person "Is this better?"
        else:
            $ the_person.apply_planned_outfit()
        $ the_person.draw_person()

    elif strip_choice == "stockings":
        mc.name "[the_person.title], I just love how your legs look in stockings, could you put some on for me?"
        the_person "Oh, I really like to doll up for you [the_person.mc_title]. Gimme a sec."
        python:
            the_clothing = renpy.random.choice(thigh_high_sock_list).get_copy()
            WardrobeBuilder.neutralize_item_colour(the_clothing)
            if the_clothing.is_similar(high_socks):
                the_clothing.transparency = .33
            else:
                the_clothing.transparency = .95
            the_person.outfit.remove_socks_or_stockings()
            the_person.outfit.add_feet(the_clothing)
            the_clothing = None
            the_person.draw_person()
        the_person "How's this?"

    elif strip_choice == "makeup":
        mc.name "[the_person.title], let's have a talk about the makeup you've been wearing."
        call screen outfit_creator(the_person.base_outfit, outfit_type = "makeup", start_mannequin = the_person)
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person()
    return

label change_titles_person(the_person):
    call screen main_choice_display(build_menu_items(build_title_selection_menu(the_person)))
    if _return[0] == 0:
        $ the_person.set_title(_return[1])
    elif _return[0] == 1:
        $ the_person.set_mc_title(_return[1])
    elif _return[0] == 2:
        $ the_person.set_possessive_title(_return[1])
    return

label change_her_title(the_person):
    call screen main_choice_display(build_menu_items(build_her_title_selection_menu(the_person)))
    if _return:
        $ the_person.set_title(_return)
    return

label demand_touch_label(the_person):
    #TODO: You demand she stays still and lets you touch her. Leads directly into the sex system at a standing massage
    #TODO: Think about what this means for being public/private.
    $ mc.change_energy(-10)
    $ should_be_private = True
    $ ignore_taboo = False
    $ old_location = None
    mc.name "All you have to do is relax and stay still. Understood?"
    if the_person.obedience > 180:
        "[the_person.possessive_title!c] nods obediently."
    else:
        the_person "I... Okay. What are you going to do?"
        mc.name "Don't worry, you'll understand soon."
        "[the_person.possessive_title!c] seems nervous, but follows your instructions for now."


    "You step closer to her and place your hands on her shoulders, rubbing them gently."
    $ mc.change_locked_clarity(10)
    "You slide your hands lower, down her sides and behind her back. You cup her ass with both hands and squeeze."

    if the_person.effective_sluttiness("touching_body") < 0:
        the_person "Hey, I..."
        mc.name "I said silent, didn't I?"
        if the_person.obedience > 180:
            the_person "I... I'm sorry."
        else:
            "[the_person.possessive_title!c]'s body is tense as you touch her."
        $ the_person.change_love(-1)
        $ the_person.call_dialogue("seduction_refuse")
        return

    else:
        "[the_person.title] places her hands in front of her and waits passively as you grope her ass."


    $ mc.change_locked_clarity(10)
    if the_person.has_large_tits:
        "You take your hand off her ass and walk behind her. You cup one of her heavy breasts in one hand, moving the other down between her thighs."
    else:
        "You take your hand off her ass and walk behind her. You grab one of her [the_person.tits_description] with one hand and move the other down between her thighs."

    # special case for camila (who wants to keep up appearances for a while)
    if the_person == camila and not camila.event_triggers_dict.get("booty_call", False):
        the_person "Stop it [the_person.mc_title], I'm not ready for this."
        $ the_person.change_stats(happiness = -5, love = -1, obedience = -1)
        "You nod and stop."
        return

    # special case for prostitute
    if the_person.is_at_job(prostitute_job):
        the_person "We can continue what you started, but it would cost you two hundred dollars."
        menu:
            "Pay her\n{menu_red}Costs: $200{/menu_red}" if mc.business.funds > 200:
                $ mc.business.change_funds(-200, stat = "Hookers")
                $ the_person.change_obedience(1, max_amount = 160)
                $ ignore_taboo = True
            "Pay her\n{menu_red}Requires: $200{/menu_red} (disabled)" if mc.business.funds <= 200:
                pass
            "No":
                mc.name "Thanks for the offer, but no thanks."
                "She shrugs."
                the_person "Your loss."
                return

    if mc.location.person_count > 1: #We're not in private, give the option to go somewhere quiet.
        $ extra_people_count = mc.location.person_count - 1
        $ the_person.discover_opinion("public sex")
        if the_person.effective_sluttiness("touching_body") < (10 - (the_person.opinion.public_sex * 5)) and the_person.obedience < 140:
            #She's very embarrassed and _demands_ to go somewhere else
            "[the_person.possessive_title!c] grabs your hands and glances around nervously."
            the_person "[the_person.mc_title], there are people around! If you want me to do this, we need to go somewhere else."
            "She has a fierce look in her eye, like this might be the limit of her obedience."
            menu:
                "Find somewhere quiet\n{menu_yellow}No interruptions{/menu_yellow}":
                    mc.name "Alright, come with me."
                    "You take [the_person.title] by her wrist and lead her away."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_demand_touch
                    "You don't waste any time getting back to what you were doing, grabbing [the_person.possessive_title]'s tits and groping her ass."

                "Stay where you are\n{menu_yellow}[extra_people_count] watching{/menu_yellow}":
                    mc.name "We're going to stay right here."
                    the_person "I... No, I'm not going to let you do this!"
                    "She pushes your hands away from her and steps back, glaring at you."
                    "After a moment [the_person.title] seems almost as shocked by her actions as you are. She glances around, then looks down at the ground, as if embarrassed."
                    $ the_person.change_stats(happiness = -5, love = -2, obedience = -2)
                    the_person "I'm sorry, I just can't do it."
                    return

        elif the_person.effective_sluttiness("touching_body") < (30 - (the_person.opinion.public_sex * 5)):
            #She's embarrassed by it and demands to go somewhere else.
            "[the_person.possessive_title!c] looks around nervously."
            the_person "[the_person.mc_title], there are other people looking. Could we please find somewhere private?"
            menu:
                "Find somewhere quiet\n{menu_yellow}No interruptions{/menu_yellow}":
                    mc.name "Alright, come with me."
                    "You take [the_person.title] by her wrist and lead her away."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_demand_touch_2
                    "You don't waste any time getting back to what you were doing, grabbing [the_person.possessive_title]'s tits and groping her ass."

                "Stay where you are\n{menu_yellow}[extra_people_count] watching{/menu_yellow}":
                    mc.name "We're going to stay right here."
                    the_person "But people are watching, and..."
                    mc.name "I don't care if they're watching."
                    $ the_person.change_stats(arousal = 5 * the_person.opinion.being_submissive, love = -1 + the_person.opinion.being_submissive, slut = 1, max_slut = 25, max_love = 25)
                    $ should_be_private = False

        else:
            #She's fine with it, but we'll give you the option anyways.
            "There are other people around, but [the_person.possessive_title] either doesn't care or is too determined to follow your instructions exactly."
            menu:
                "Find somewhere quiet\n{menu_yellow}No interruptions{/menu_yellow}":
                    mc.name "Come with me, I don't want to be interrupted."
                    "You take [the_person.title] by the wrist and lead her away. She follows without question."
                    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_demand_touch_3
                    "You don't waste any time getting back to what you were doing, grabbing [the_person.possessive_title]'s tits and groping her ass."

                "Stay where you are\n{menu_yellow}[extra_people_count] watching{/menu_yellow}":
                    $ should_be_private = False

    if the_person.has_taboo("touching_body"):
        $ the_person.call_dialogue("touching_body_taboo_break") #TODO: Have a variant when a person is being _commanded_ instead of seduced.
        $ the_person.break_taboo("touching_body")

    call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True, ignore_taboo = ignore_taboo) from _call_fuck_person_44
    $ the_person.call_dialogue("sex_review", the_report = _return)

    if should_be_private:
        call mc_restore_original_location(the_person) from _call_mc_restore_original_location_demand_touch
    else:
        $ the_person.review_outfit()
    return

label demand_strip_label(the_person):
    call screen main_choice_display(build_menu_items([build_demand_strip_menu(the_person)]))
    if isinstance(_return, Action): #Just return, we either don't want to select any of these options, or we _can't_
        $ _return.call_action()
    return

label demand_strip_tits_label(the_person):
    $ mc.change_energy(-5)
    mc.name "You're going to get your tits out for me."

    $ test_outfit = the_person.outfit.get_copy()
    $ test_outfit.strip_to_tits()
    $ willing_private = demand_strip_judge_private(the_person, test_outfit, "showing her tits")
    $ willing_public = demand_strip_judge_public(the_person, test_outfit, "showing her tits")
    $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min_obedience = 140, private = not willing_public)
    $ test_outfit = None

    $ strip_list = the_person.outfit.get_tit_strip_list()
    $ first_item = strip_list[0]

    $ the_person.discover_opinion("showing her tits")

    if the_person.location.person_count > 1: #You aren't alone
        if willing_public: #She's into it
            "[the_person.possessive_title!c] doesn't seem to care about the other people around and starts to pull off her [first_item.display_name] right away."
            call .start_stripping() from _demand_strip_tits_willing_public
            return

        "[the_person.possessive_title!c] looks around nervously, then back at you."
        if willing_private: # She's willing, but shy
            the_person "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're finally alone she moves to pull off her [first_item.display_name] for you."
                    call .start_stripping(private = True) from _demand_strip_tits_move_to_private
                    return

                "Stay right here" if the_person.obedience >= obedience_requirement:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title!c] doesn't argue. She just blushes and starts to pull off her [first_item.display_name] for you."
                    call .start_stripping(ordered = True) from _demand_strip_tits_stay_in_public
                    return

                "Stay right here\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Never mind. Let's do something else."
                    $ the_person.change_stats(obedience = -1)

        elif the_person.obedience >= obedience_requirement - 20: # She doesn't even want to do it in private
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title!c] stops arguing and resignedly starts to pull off her [first_item.display_name]."
                    call .start_stripping(ordered = True) from _demand_strip_tits_ordered_public
                    return

                "That's an order\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."

    else: #You are alone
        if willing_private: #She's into it.
            "[the_person.possessive_title!c] nods obediently and begins to take off her [first_item.display_name] while you watch."
            call .start_stripping(private = True) from _demand_strip_tits_willing_private
            return

        if the_person.obedience >= obedience_requirement - 20: # She's considering it
            "[the_person.possessive_title!c] seems uncomfortable and hesitates to follow instructions."
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title!c] stops arguing and resignedly begins to take off her [first_item.display_name]."
                    call .start_stripping(private = True, ordered = True) from _demand_strip_tits_ordered_private
                    return

                "That's an order\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."

    $ strip_list = None
    $ first_item = None
    return

label .start_stripping(private = False, ordered = False):
    $ top_strip_description(the_person, strip_list)

    $ strip_list = None
    $ first_item = None

    $ person_is_shy = not the_person.judge_outfit(the_person.outfit, temp_sluttiness_boost = 5 * the_person.opinion.showing_her_tits)

    if the_person.update_outfit_taboos() or person_is_shy: # She's shy
        "[the_person.title] brings her hands up to cover her breasts."
        the_person "Are we done?"
        mc.name "I want to get a look first, and I can't see anything if you're hiding like this."
        $ mc.change_locked_clarity(10)
        "She nods and moves her hands to her side again. She blushes and looks away as you ogle her tits."
        $ the_person.change_stats(happiness = -2 + the_person.opinion.showing_her_tits, slut = 1 + the_person.opinion.showing_her_tits, max_slut = 35)
        "When you've seen enough you give her an approving nod. She sighs and moves towards her clothes."
        the_person "Can I get dressed now?"
    else: # She's into it
        $ the_person.draw_person() #TODO Make sure this effect looks right
        $ mc.change_locked_clarity(20)
        "[the_person.title] places her hands behind her and bounces on her feet, jiggling her tits for your amusement."
        "When you've seen enough you nod approvingly. [the_person.possessive_title!c] smiles happily."
        the_person "So you want me to get dressed again?"

    menu:
        "Let her get dressed":
            mc.name "Yeah, you can."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            "You watch her put her clothes back on, covering up her tits."

        "Keep your tits out":
            mc.name "I think you look good with your tits out. Stay like this for a while, okay?"
            if willing_public:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            elif the_person.obedience >= obedience_requirement:
                $ the_person.change_stats(obedience = 1, max_obedience = 150, slut = 1, max_slut = 35, happiness = -2)
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            else:
                $ the_person.change_stats(obedience = -2, love = -1)
                the_person "Very funny. I'm not about to go out like this."
                $ the_person.apply_planned_outfit(show_dress_sequence = True)
                "She starts putting her clothes back on."

    return

label demand_strip_underwear_label(the_person):
    mc.name "You're going to strip into your underwear for me."
    if not the_person.outfit.wearing_panties or not the_person.outfit.wearing_bra:
        the_person "I can't do that [the_person.mc_title]."
        mc.name "Yes you can, you..."
        "She interrupts you."
        if not the_person.outfit.wearing_panties and not the_person.outfit.wearing_bra:
            the_person "No, I can't show you my underwear because... I'm not wearing any."
        elif not the_person.outfit.wearing_panties:
            the_person "No, I can't show you my underwear because... I'm not wearing any panties."
        else:
            the_person "No, I can't show you my underwear because... I'm not wearing a bra in the first place."
        mc.name "Well, that's as good a reason as any."
        return

    if mc.location.person_count > 1: #You aren't alone.
        if the_person.effective_sluttiness("underwear_nudity") < (40 - (5*the_person.opinion.lingerie)): #She's shy and wants to go somewhere private
            "[the_person.possessive_title!c] looks around nervously, then back at you."
            the_person "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to pull off her clothes for you."


                "Stay right here" if the_person.obedience >= 140:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title!c] doesn't argue. She just blushes and starts to pull off her clothes."

                "Stay right here\n{menu_red}Requires: 140 Obedience{/menu_red} (disabled)" if the_person.obedience < 140:
                    pass

        else: #She's into it
            "[the_person.possessive_title!c] nods obediently, seemingly unbothered by your command."


        $ underwear_strip_description(the_person)


    else: #You are alone
        if the_person.effective_sluttiness("underwear_nudity") < (40 - (5*the_person.opinion.lingerie)): #She's shy
            "[the_person.possessive_title!c] seems uncomfortable, but she nods obediently and starts to pull off her clothes."

        else: #She's into it.
            the_person "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."

        $ underwear_strip_description(the_person)

    $ the_person.update_outfit_taboos()

    if the_person.effective_sluttiness() < (40 - (5*the_person.opinion.lingerie)): # She's shy
        the_person "Um... So what do we do now?"
        mc.name "Just relax and let me take a look. You look cute."
        $ mc.change_locked_clarity(10)
        "She nods and puts her hands behind her back. She blushes and looks away self-consciously as you ogle her."
        $ the_person.change_stats(happiness = -2 + the_person.opinion.lingerie, slut = 1 + the_person.opinion.lingerie, max_slut = 35)
        mc.name "Let me see what it looks like from behind."
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] spins around obediently."
        "You enjoy the view for a little while longer. [the_person.possessive_title!c] seems anxious to cover up again."
        the_person "Can I get dressed now?"
        $ the_person.draw_person()
    else:
        "[the_person.title] immediately puts her hands behind her back and pushes her chest forward, accentuating her tits."
        the_person "So, what do you think? Does my underwear look good?"
        mc.name "It does, you look cute."
        $ mc.change_locked_clarity(15)
        "She smiles and gives you a spin, letting you take a look at her from behind."
        $ the_person.draw_person(position = "back_peek")
        "You enjoy the view for a little while longer, then nod approvingly to [the_person.possessive_title]."
        $ the_person.draw_person()
        the_person "Would you like me to get dressed again?"

    menu:
        "Let her get dressed":
            mc.name "Yeah, you can."
            "You watch her put her clothes back on."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)

        "Stay in your underwear":
            mc.name "Your underwear is too cute to hide it away, you should should stay in it for a while."
            if the_person.effective_sluttiness() < (40 - (5*the_person.opinion.lingerie)):
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_stats(happiness = -2, slut = 1, max_slut = 35)
            else:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
    return

label demand_strip_naked_label(the_person):
    $ mc.change_energy(-5)
    mc.name "You're going to strip naked for me."

    $ test_outfit = Outfit("Nude") # Doesn't include accessories. Don't actually apply this outfit.
    $ willing_private = demand_strip_judge_private(the_person, test_outfit, "not wearing anything")
    $ willing_public = demand_strip_judge_public(the_person, test_outfit, "not wearing anything")
    $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min_obedience = 150, private = not willing_public)
    $ test_outfit = None

    $ the_person.discover_opinion("not wearing anything")

    if mc.location.person_count > 1: #Other people are around
        if willing_public: #She's into it
            "[the_person.possessive_title!c] nods and starts to enthusiastically strip down."
            call .start_stripping() from _demand_strip_naked_willing_public
            return

        "[the_person.possessive_title!c] looks around nervously, then back at you."
        if willing_private:
            the_person "But... Here? I don't want to get naked in front of other people."
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to strip down immediately."
                    call .start_stripping(private = True) from _demand_strip_naked_move_to_private
                    return

                "Stay right here" if the_person.obedience >= 170:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title!c] doesn't argue. She just blushes and starts to strip down."
                    call .start_stripping(ordered = True) from _demand_strip_naked_stay_in_public
                    return

                "Stay right here\n{menu_red}Requires: 170 Obedience{/menu_red} (disabled)" if the_person.obedience < 170:
                    pass

                "Never mind":
                    mc.name "Never mind. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
                    return

        elif the_person.obedience >= obedience_requirement - 20: # She doesn't even want to do it in private
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title!c] stops arguing and resignedly starts to pull off her clothes."
                    call .start_stripping(ordered = True) from _demand_strip_naked_ordered_public
                    return

                "That's an order\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
                    return
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."
            return

    else: #You are alone
        if willing_private: #She's into it.
            the_person "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."
            call .start_stripping(private = True) from _demand_strip_naked_willing_private
            return

        if the_person.obedience >= obedience_requirement - 20:
            "[the_person.possessive_title!c] seems uncomfortable at your request."
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title!c] stops arguing and resignedly starts to pull off her clothes."
                    call .start_stripping(private = True, ordered = True) from _demand_strip_naked_ordered_private
                    return

                "That's an order\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
                    return
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."
            return
    return

label .start_stripping(private = False, ordered = False):
    $ remove_shoes = False
    $ the_item = the_person.outfit.get_feet_top_layer
    if the_item:
        the_person "Do you want me to keep my [the_item.display_name] on?"
        menu:
            "Strip it all off":
                mc.name "Take it all off, I don't want you to be wearing anything."
                $ remove_shoes = True
            "Leave them on":
                mc.name "You can leave them on."
    $ the_item = None

    $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list(strip_feet = remove_shoes))

    $ person_is_shy = not the_person.judge_outfit(the_person.outfit, temp_sluttiness_boost = 5 * the_person.opinion.not_wearing_anything)

    if the_person.update_outfit_taboos() or person_is_shy: # She's shy
        the_person "What would you like me to do now?"
        "She instinctively puts her hands behind her back while she waits for your instructions."
        $ mc.change_locked_clarity(20)
        mc.name "Give me a spin, I want to see your ass."
        "She blushes, but nods and turns around."
        $ the_person.draw_person(position = "back_peek")
        "[the_person.possessive_title!c] waits patiently until you signal for her to turn around again."
        $ the_person.draw_person()
        the_person "Are we finished? Is that all?"

    else:
        $ mc.change_locked_clarity(20)
        "[the_person.title] puts her hands behind her back and pushes her chest forward, accentuating her tits."
        "She waits silently for you to tell her what to do. You notice her nipples harden as you watch her."
        mc.name "Do you like this?"
        #TODO: THis should probably include dialogue based on their being naked opinions.
        the_person "If I'm doing it for you I do."
        mc.name "Good. Turn around, I want to see your ass."
        $ mc.change_locked_clarity(20)
        "She nods happily and turns around, wiggling her butt for you."
        $ the_person.draw_person(position = "back_peek")
        "You enjoy the view until you're satisfied."
        mc.name "Okay, turn around again."
        $ the_person.draw_person()
        the_person "Is there anything else, [the_person.mc_title]?"

    menu:
        "Let her get dressed":
            mc.name "I've seen enough. You can get dressed."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            "You watch her as she gets dressed again."

        "Keep her naked":
            mc.name "Your body is way too nice looking to hide away. Stay like this for a while."
            if willing_public:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
                "[the_person.title] doesn't seem to mind."
            elif the_person.obedience >= obedience_requirement:
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_stats(obedience = 1, max_obedience = 160, slut = 1, max_slut = 40, happiness = -2)
            else:
                the_person "Very funny. I'm not about to go out like this."
                $ the_person.apply_planned_outfit(show_dress_sequence = True)
                "She starts putting her clothes back on."
                $ the_person.change_stats(obedience = -1, love = -1)
    return

label suck_demand_label(the_person):
    $ private = True
    if mc.location.person_count > 1:
        # There are other people here, let's ask if we want to go someplace quiet first.
        menu:
            "Find somewhere more quiet\n{menu_yellow}[mc.location.interruption_info_text]{/menu_yellow}":
                mc.name "Follow me."
                "[the_person.possessive_title!c] nods and follows obediently after you."
                call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_suck_demand

            "Do it right here":
                $ private = False

    "You unzip your pants and pull your cock free, already hardening with excitement."
    mc.name "Get on your knees. You're going to suck my cock."

    if not private and the_person.obedience < 200 and the_person.effective_sluttiness("sucking_cock") < 40 + (the_person.opinion.public_sex * 5):
        $ the_person.call_dialogue("sex_angry_reject")
        "This didn't go as expected, she is not ready to do this in public."
        return

    if the_person.effective_sluttiness("sucking_cock") + (the_person.opinion.being_submissive * 10) >= 60: #She would do it anyways and doesn't even think it's strange. Note: We require you to already have broken the blowjob taboo to get here as well.
        the_person "Right away [the_person.mc_title]."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(20)
        "She drops to her knees immediately, spreading her legs and planting her hands on the ground between them."

    elif the_person.effective_sluttiness("sucking_cock") + (the_person.opinion.being_submissive * 10) >= 40:
        if private:
            "[the_person.possessive_title!c] hesitates, but starts to move before you have to command her again."
        else:
            "[the_person.possessive_title!c] hesitates, glancing around."
            the_person "I... Right here? Wouldn't you like to find somewhere private so we can..."
            mc.name "Right here. Get on your knees and get my cock in your mouth before I run out of patience."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(10)
        "She drops to her knees, putting her hands on her thighs and moving her face to cock level."

    else:
        if private:
            "[the_person.possessive_title!c] hesitates, shaking her head."
            the_person "I can't do that, I..."
            mc.name "I wasn't asking you a question. On your knees, now. The longer you take the more stress I'm going to need relieved."
        else:
            "[the_person.possessive_title!c] looks around, almost panicked."
            the_person "I can't... We can't do that here! People would see me, I would..."
            mc.name "I've already got my cock out, and I'm not putting it back in my pants until it's been down your throat."
            mc.name "On your knees. Now."
        $ mc.change_locked_clarity(10)
        "She seems on the verge of refusing, but drops slowly to her knees to put her face at cock level."

    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
    "[the_person.title] licks the tip of your cock, then slides it tenderly into her mouth."
    menu:
        "Let her worship your cock":
            "You sigh and enjoy the feeling of her warm, wet blowjob."
            mc.name "That's a good girl..."
            call mc_sex_request(the_person, the_request = "blowjob", private = private) from _call_mc_sex_request_suck_demand

        "Grab her head and fuck her mouth":
            "You place your hands on either side of [the_person.possessive_title]'s head. She cocks her head and looks up at you."
            mc.name "That's a good girl, now let's put you to good use."
            "You hold her head in place as you shove your hips forward."
            if the_person.oral_sex_skill >= 4: #She throats you like a pro
                "[the_person.title] instinctively kneels a little lower and tilts her head up, giving your cock a clear path down her throat."
                $ mc.change_locked_clarity(30)
                $ play_gag_sound()
                "Her eyes flutter briefly as you bottom out, balls rubbing against her chin. You can feel her quiver as she tries to suppress her gag reflex."

            else: #Gags
                "[the_person.title] instinctively tries to jerk away, but you clamp down and don't let her move."
                $ mc.change_locked_clarity(20)
                $ play_gag_sound()
                "Her eyes open wide as you force your cock clear down her throat. She gags hard, blowing spit out where her lips meet the base of your shaft."
                mc.name "I think you still need a little more practice. Let's see what we can do about that..."

            "You hold yourself there for a moment, enjoying the feeling of your dick fully engulfed by your obedient [the_person.title]."
            $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
            "You can't resist moving for long though. You pull back to give yourself room, then thrust your cock home, then again, and again."
            if the_person.oral_sex_skill >= 4: #She throats you like a pro
                "[the_person.title] takes your cock as well as can be expected, eyes turned up to meet yours as you fuck her face."
            else:
                "[the_person.title] squirms and gags reflexively, but she seems to be trying her best to stay still as you fuck her face."

            call fuck_person(the_person, private = private, start_position = skull_fuck, start_object = mc.location.get_object_with_trait("Kneel"), skip_intro = True, ignore_taboo = True) from _call_fuck_person_88

    $ the_person.call_dialogue("sex_review", the_report = _return)
    if private:
        call mc_restore_original_location(the_person) from _call_mc_restore_original_location_suck_demand
    else:
        $ the_person.review_outfit()
    return

label demand_panties_label(the_person):
    $ mc.change_energy(-5)
    "You lean over and whisper softly in her ear..."
    mc.name "I want you to give me your panties..."

    if not the_person.wearing_panties:
        the_person "I would love to do that [the_person.mc_title], except that I'm not wearing any... "
        if the_person.can_half_off_to_vagina and (the_person.sluttiness > 60 or the_person.has_exhibition_fetish):
            $ the_person.strip_to_vagina(prefer_half_off = True)
            the_person "See for yourself..."
        mc.name "Ah, I see, you were expecting something to happen today..."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
        "[the_person.possessive_title!c] gives you a wink."
        return

    $ test_outfit = the_person.outfit.get_copy()
    $ the_item = test_outfit.get_panties()
    if the_item.is_extension: #two piece item
        $ the_item = next((x for x in test_outfit.get_upper_ordered() if x.has_extension == the_item), None)

    if test_outfit.can_remove_panties:
        $ test_outfit.remove_clothing(the_item)
    else:
        $ test_outfit.strip_to_vagina()
        if test_outfit.has_clothing(the_item): # in case of crotchless/half-off panties
            $ test_outfit.remove_clothing(the_item)

    $ the_person.discover_opinion("not wearing underwear")

    if the_person.location.privacy_level == 3:
        the_person "Right here? In public?"
        if demand_strip_judge_public(the_person, test_outfit, "not wearing underwear"):
            $ the_person.draw_person(emotion = "happy")
            "[the_person.title] smiles, clearly excited by the idea."
            jump .start_stripping
        else:
            the_person "I could do that [the_person.mc_title], but other people might notice if I start stripping down."
            call .thats_an_order from _demand_panties_public
            if _return:
                jump .start_stripping
            else:
                mc.name "Why don't you stop wearing panties, so I don't have to ask for them?"
                the_person "Maybe next time..."
    elif the_person.location.person_count > 1:
        $ the_watcher = get_random_from_list(known_people_at_location(mc.location, excluded_people = [the_person]))
        if the_watcher:
            the_person "Right here? With [the_watcher.fname] watching?"
            $ the_watcher = None
        if demand_strip_judge_public(the_person, test_outfit, "not wearing underwear"):
            $ the_person.draw_person(emotion = "happy")
            "[the_person.title] smiles, clearly excited by the idea."
            jump .start_stripping
        else:
            the_person "I don't know [the_person.mc_title], someone might notice if I start taking them off."
            call .thats_an_order from _demand_panties_multiple_people
            if _return:
                jump .start_stripping
            else:
                the_person "Perhaps I should stop wearing panties altogether..."
                mc.name "That sounds like a plan."
    else:
        if demand_strip_judge_private(the_person, test_outfit, "not wearing underwear"):
            jump .start_stripping
        else:
            the_person "I'm sorry [the_person.mc_title], but my panties stay on for now."
            call .thats_an_order(private = True) from _demand_panties_private
            if _return:
                jump .start_stripping
            else:
                mc.name "For now?"
                "[the_person.title] smirks and changes the subject."

    $ test_outfit = None
    $ the_item = None
    return

label .thats_an_order(private = False):
    $ was_ordered = False
    $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min_obedience = 120, private = private)
    menu:
        "That's an order" if the_person.obedience >= obedience_requirement:
            mc.name "I must not have been clear enough."
            mc.name "Give me your panties. Now."
            $ the_person.draw_person(emotion = "angry")
            the_person "..."
            $ the_person.draw_person(emotion = "sad")
            $ the_person.change_stats(happiness = -2)
            "[the_person.title] is cowed into compliance by the tone of your voice."
            $ was_ordered = True
            pass
        "That's an order\n{menu_red}Requires: [obedience_requirement] Obedience{/menu_red} (disabled)" if the_person.obedience < obedience_requirement:
            pass
        "Let it go":
            $ the_person.change_stats(obedience = -1)
            pass
    return was_ordered

label .start_stripping():
    if the_person.can_remove_panties:
        if the_person.has_skirt or the_person.has_dress:
            $ name = "skirt" if the_person.has_skirt else "dress"
            if the_person.location.privacy_level > 0:
                "[the_person.possessive_title!c] takes a quick look around and pulls up her [name]."
            else:
                "[the_person.possessive_title!c] gives you a smile and pulls up her [name]."
            $ the_person.strip_to_vagina(prefer_half_off = True)
            "She quickly takes off her [the_item.display_name] and places them in your hand."
        else:
            if the_person.location.privacy_level > 0:
                "[the_person.possessive_title!c] takes a quick look around and pulls off her [the_item.display_name], placing them in your hand."
            else:
                "[the_person.possessive_title!c] gives you a smile and pulls off her [the_item.display_name], placing them in your hand."
        $ the_person.draw_animated_removal(the_item)
        $ the_person.change_stats(obedience = 1, max_obedience = 160, slut = 1, max_slut = 40)
        the_person "Is this what you were looking for?"
        $ the_person.current_planned_outfit = the_person.outfit.get_copy()
        $ the_person.current_planned_outfit.restore_all_clothing()
        $ the_person.apply_planned_outfit(update_taboo = True, show_dress_sequence = True)
    else:
        $ old_outfit = the_person.outfit.get_copy()
        $ old_outfit.remove_clothing(the_item)

        the_person "This might take a minute..."
        if the_person.location.privacy_level == 3 or the_person.location.person_count > 1:
            "[the_person.possessive_title!c] takes a quick look around and starts stripping down."
        else:
            "[the_person.possessive_title!c] starts stripping down, giving you her [the_item.display_name]."
        $ the_person.strip_to_vagina()
        if the_person.outfit.has_clothing(the_item):
            $ the_person.draw_animated_removal(the_item)
        $ the_person.change_stats(obedience = 1, max_obedience = 160, slut = 1, max_slut = 40)
        $ the_person.update_outfit_taboos()
        the_person "Here you are, anything else I can do for you?"
        $ the_person.apply_outfit(old_outfit)
        $ the_person.draw_person()
        "She quickly puts her clothes back on."

        $ old_outfit = None
        $ the_person.current_planned_outfit = the_person.outfit.get_copy()

    $ the_item = None
    return

label make_onlyfans_together_label(the_person):
    mc.name "Hey, aren't you a content creator on OnlyFans?"
    the_person "Yeah, I am."
    mc.name "Let's make a video together. I bet I can help you pull in a ton of views."
    if the_person.effective_sluttiness() < 60:
        the_person "I'm not sure that is a good idea..."
        mc.name "Why not? I mean, you're already on there, what's wrong with me dicking you down?"
        the_person "I... okay, I guess we can do that..."
    else:
        the_person "Sure! Just make sure you finish. My customers pay way better if there's a good cumshot, okay?"
        mc.name "I aim to please."

    if not mc.location.is_private:
        "You find a private area with [the_person.possessive_title] where you won't be disturbed."
        call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_make_only_fans

    call fuck_person(the_person, private = True, condition = make_condition_onlyfans_recording()) from _call_fuck_person_make_onlyfans_command_01
    "You hand [the_person.possessive_title]'s phone back to her."
    mc.name "If you want to make another video sometime, just let me know."
    the_person "Sure thing!"
    $ the_person.apply_planned_outfit()
    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_make_only_fans
    $ clear_scene
    return

label bend_over_your_desk_label(the_person):
    mc.name "[the_person.title], I want you to bend over you desk and work on something on the computer terminal for a while."
    the_person "Oh?"
    mc.name "I'm going to sit behind you and enjoy your body for a bit. You don't mind do you?"
    if the_person.obedience > 180:
        the_person "No, anything you want sir."
        "She eagerly complies, trying to her best to please you."
    elif the_person.sluttiness > 50:
        the_person "I don't mind if you want to have some fun like that..."
        "She eagerly complies."
    else:
        the_person "Oh my... I suppose..."
        "She hesitates a bit, but obediently complies."
    $ the_person.draw_person(position = "standing_doggy")
    "You sit down in her chair. [the_person.possessive_title!c]'s ass is directly in front of you for your viewing pleasure as you sit down."
    call employee_lust_build_loop_label(the_person) from _obedience_lust_build_loop_call_02
    if the_person.energy < 30:
        "You are incredibly turned on, but you can tell that [the_person.title] is too tired to continue."
        "[the_person.possessive_title!c] adjusts her outfit."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
        return
    elif mc.energy < 30:
        "You are incredibly turned on, but you just don't have the energy to continue."
        "[the_person.possessive_title!c] adjusts her outfit."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
        return
    elif mc.lust_tier >= 4 or (mc.lust_tier * 2 > mc.focus):
        "You are incredibly turned on. You decide to take things with [the_person.title] a step further."
    else:
        "Do you want to take things with [the_person.title] a step further?"

    $ report_log = create_report_log({"was_public": True, "obedience_used": True}) # we already start with obedience used set
    menu:
        "Ask for handjob":
            mc.name "You are so fucking hot. Would you please finish me off? You can use your hand."
            the_person "Okay, I can do that."
            $ the_person.draw_person(position = "stand3")
            "She walks up to you."
            call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = False, skip_intro = False, allow_continue = False, report_log = report_log) from _obedience_lust_loop_handjob_finish_01
        "Demand blowjob" if the_person.is_willing(blowjob, private = False):
            mc.name "That's enough, now I need you to finish me off. Get on your knees and suck me off."
            if the_person.opinion.giving_blowjobs <= -2:
                the_person "I'm sorry, I can't do that... but I can get you off some other way!"
                mc.name "Fine, just do that then."
                the_person "Okay..."
                call get_fucked(the_person, the_goal = "get mc off", private = False, skip_intro = False, allow_continue = False, report_log = report_log) from _obedience_lust_loop_blowjob_finish_01
            else:
                $ the_person.draw_person(position = "blowjob")
                "[the_person.possessive_title!c] obediently turns and gets down on her knees."
                "You pull your cock out and she opens her mouth, taking you in her mouth obediently."
                call fuck_person(the_person, private = False, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True, report_log = report_log) from _obedience_lust_loop_blowjob_finish_02
        "Fuck her" if the_person.is_willing(standing_doggy, private = False) and the_person.vagina_available:
            "You stand up and pull your cock out. You rub yourself along her slit for a moment."
            the_person "Ah... sir?"
            mc.name "Just keep working. This will only take a moment."
            call fuck_person(the_person, private = False, start_position = standing_doggy, start_object = make_desk(), condition = make_condition_computer_work(), skip_intro = True, position_locked = True, report_log = report_log) from _obedience_lust_loop_doggy_finish_01
        "Fuck her ass" if the_person.is_willing(anal_standing, private = False) and the_person.vagina_available:
            "You stand up and pull your cock out. You rub yourself along her slit for a moment."
            the_person "Ah... sir?"
            mc.name "Just keep working. This will only take a moment."
            call fuck_person(the_person, private = False, start_position = anal_standing, condition = make_condition_computer_work(), start_object = make_desk(), skip_intro = True, position_locked = True, report_log = report_log) from _obedience_lust_loop_anal_finish_01
        "Leave her alone" if not (mc.lust_tier >= 4 or (mc.lust_tier * 2 > mc.focus)):
            pass
    mc.name "Thank you, [the_person.title]. That was just what I needed."
    if the_person.opinion.not_wearing_anything > 0:
        "[the_person.possessive_title!c] starts to clean herself up."
        menu:
            "Stay like that":
                mc.name "What are you doing? Did I say you could clean up?"
                the_person "N... no sir."
                mc.name "I want you to just stay like that for a while. It's a good look for you."
                the_person "Yes [the_person.mc_title]."
                $ the_person.change_obedience(1, max_amount = 180)
            "Don't say anything":
                "You decide to let her straighten her outfit this time."
                $ the_person.apply_planned_outfit(show_dress_sequence = True)
    else:
        "[the_person.possessive_title!c] cleans herself up and adjusts her outfit."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label employee_lust_build_loop_label(the_person):
    $ loop_choice = None
    $ ass_lubed = False
    $ fingers_wet = False
    while loop_choice != "finish":
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title!c] is standing in front of you, bent over her desk while you sit right behind her."
        if the_person.vagina_available:
            if the_person.arousal_perc > 75:
                "Her juices are leaking down the inside of her leg. Her lips are puffy with desperate arousal."
                "Her ass jiggles enticingly and her hips sway with every touch."
            elif the_person.arousal_perc > 30:
                "Her pussy is exposed to your view, and a hint of her arousal can be seen on her lips."
                "Her ass jiggles enticingly with every touch."
            else:
                "Her ass and pussy are exposed for you to view. Her ass jiggles with every touch and movement."
        else:
            "Her ass sways enticingly with every touch and movement."
        #Chance to unlock spanking submissive girls here
        if the_person.is_submissive and not the_person.can_be_spanked and the_person.vagina_available and renpy.random.randint(0, 100) < 30:
            "Something about [the_person.possessive_title]'s ass in your face and her submissive nature is getting your hormones going."
            "You reach up without warning and give her ass a firm spank."
            $ the_person.slap_ass()
            $ play_moan_sound()
            the_person "Mnnnf!"
            "She moans, with just a hint of pain in her voice."
            mc.name "[the_person.title], your ass looks amazing when I spank it. You are such a slut. I bet you love it, don't you?"
            the_person "Oh god, this is so naughty!"
            "She really seems to enjoy her spanking. Maybe you should work it into your normal foreplay..."
            $ the_person.unlock_spanking()
        menu:
            "Spank her {energy=-10}" if the_person.can_be_spanked and the_person.vagina_available and the_person.spank_level <= 8:
                $ mc.change_energy(-10)
                "You look at [the_person.possessive_title]'s ass. It is [the_person.ass_spank_description]"
                $ the_person.slap_ass()
                "You give her a solid spank. She lets out a little yelp."
                $ the_person.slap_ass(update_stats = False)
                $ the_person.slap_ass(update_stats = False)
                $ the_person.slap_ass(update_stats = False)
                "You don't let up, giving her a solid spanking, moving back and forth between each cheek."
                if the_person.spank_enjoyment_level > 5: #She loves it.
                    the_person "Oh god [the_person.mc_title]! Give it to me good! Oh god!"
                    "She is really getting into this. With each spank she wiggles her ass, giving you an enticing target."
                elif the_person.spank_enjoyment_level > 0:
                    the_person "Oh... I'm sorry [the_person.mc_title]! Oh god..."
                    $ play_spank_sound()
                    "She keeps her ass still, taking your blows. Her ass makes an enticing target."
                elif the_person.spank_enjoyment_level > -5:
                    the_person "Ouch! I'm sorry [the_person.mc_title]! That really hurts..."
                    $ play_spank_sound()
                    "With each spank, she flinches a bit."
                else:
                    the_person "Fuck! That hurts! Why are you doing this? Please stop!"
                    $ play_spank_sound()
                    "She's trembling. With each spank she flinches and quakes."

            "Spank her\nToo bruised to continue (disabled)" if the_person.spank_level > 8:
                pass


            "Pull her bottoms off" if not the_person.vagina_visible and (the_person.sluttiness > 30 or the_person.obedience > 140):
                "You decide that it is time to get a better view. You pull at her clothing."
                the_person "Sir... I..."
                mc.name "Shh, just keep working."
                the_person "Fuck... okay..."
                $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = True)
                "[the_person.possessive_title!c]'s ass is now exposed, directly in front of your face for your viewing pleasure as she works at the computer terminal."
                $ play_spank_sound()
                "You run your hands along it and give it a little smack."

            "Grope her ass {energy=-10}":    #The baseline option
                $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
                "You reach up and run your hands over her shapely ass as she works."
                $ mc.change_energy(-10)
                if the_person.vagina_available:
                    if the_person.body_is_thin:
                        "[the_person.title]'s tight cheeks are firm and pleasing to the touch. She works hard to keep a fit body and it shows."
                    elif the_person.body_is_average:
                        "[the_person.title]'s shapely ass wobbles a bit as you grope it. You love the feeling of her curves in your hands."
                    elif the_person.body_is_thick:
                        "[the_person.title]'s big bubble butt wobbles excessively as you grope it."
                    elif the_person.body_is_pregnant:
                        "[the_person.title]'s ass wobbles enticingly as you grope it. Her pregnant belly hangs underneath her as she enjoys your touches."
                    "You let yourself grope and rub her ass for several seconds as she sighs in pleasure."
                    $ the_person.change_arousal(5)
                else:
                    "[the_person.title]'s curves feel great through her clothing."

            "Order her to twerk" if the_person.energy > 10 and (the_person.sluttiness > 30 or the_person.obedience > 140):
                mc.name "Shake your ass for me. I want to see what this thing can do."
                "[the_person.possessive_title!c] doesn't say anything, but obediently starts to shake her ass the way you've instructed."
                if the_person.vagina_available:
                    if the_person.body_is_thin:
                        "[the_person.title] shakes her tight little ass up and down for you."
                    elif the_person.body_is_average:
                        "[the_person.title] shakes her shapely ass up and down for you. It wobbles pleasingly as she shakes it."
                    elif the_person.body_is_thick:
                        "[the_person.title] shakes her big ass up and down for you. Her cheeks make large waves as she bounces it up and down."
                    elif the_person.body_is_pregnant:
                        "[the_person.title] shakes her big, pregnant ass up and down for you. This angle really accentuates the curve of her cheeks and bump enticingly."
                    "You can't look away and can only imagine the pleasure it would bring to have your cock buried inside her while she did this..."
                else:
                    $ play_spank_sound()
                    "[the_person.title] twerks her ass up and down for you in an enticing display. You give it a couple light smacks as she moves."
                $ the_person.change_energy(-10)

            "Finger her {energy=-10}" if the_person.vagina_available and (the_person.sluttiness > 30 or the_person.obedience > 140) and the_person.opinion.being_fingered >= 0:
                "You run your hand along the curve of her hip, then across the top of her ass, then down along her crack."
                $ mc.change_energy(-10)
                "You get to her slit and run your finger along it a few times, then slowly push two fingers into her soft love tunnel."
                $ fingers_wet = True
                $ play_moan_sound()
                the_person "Mmmm..."
                mc.name "Keep working, this is for my enjoyment, not yours."
                the_person "Y... yes sir!"
                $ play_moan_sound()
                "[the_person.possessive_title!c] tries to muffle her moans as you start to finger her eagerly. Her soft gasps are incredibly arousing."
                $ the_person.change_arousal(15)
                if the_person.arousal_perc > 100:
                    the_person "Oh god... ohhh!"
                    "Her whole body tenses up and she pushes back against you. A shiver runs through her body as she climaxes."
                    $ the_person.call_dialogue("climax_responses_foreplay")
                    $ the_person.have_orgasm()
                    $ the_person.change_slut(1, 60)
                    "She quivers with pleasure for a few seconds before her whole body relaxes."
                elif the_person.arousal_perc > 50:
                    "You pull your fingers out for a moment. A long strand of her juices connects your fingers to her soaking wet cunt."
                    mc.name "Wow, you are soaked. I'm glad you are enjoying this as much as I am."
                    "You push your two fingers back inside her and finger her for a bit longer."
                else:
                    "[the_person.title] lets out a little gasp now and then as she tries to continue working at the computer terminal."
                    "Her body is just starting to get warmed up."

            "Finger her ass {energy=-10}" if the_person.opinion.anal_sex >= 0 and the_person.vagina_available and (the_person.sluttiness > 40 or the_person.obedience > 150):
                if not ass_lubed:
                    "You decide to stretch her asshole a bit, but first, you need to get it lubed up."
                    if the_person.arousal_perc > 50: #Use her natural arousal to lube her up.
                        "You take two fingers and push them into her soaking wet cunt, pumping them inside her a few times."
                        "Once they are good and wet, you pull them out, then run them along her puckered hole."

                    else:
                        if fingers_wet:
                            "You bring your fingers up to your mouth. You can taste her cunt on your fingers from when you fingered her earlier."
                            "You slobber on them excessively, then spit a large wad of saliva onto her puckered hole."
                        else:
                            "You bring your fingers up to your mouth and slobber on them excessively."
                            "You spit a large wad of saliva onto her puckered hole."
                    the_person "S... sir?"
                    mc.name "Shh, I already told you, this is for my benefit. Just keep working."
                    the_person "Yes [the_person.mc_title]..."
                    "Slowly, you push one finger into her puckered back door. There's a bit of resistance, but you manage to get it in."
                    $ play_moan_sound()
                    the_person "Aahh.... mmm..."
                    $ ass_lubed = True
                    "You pull your finger out, then spit onto them for more lubrication. This time, you easily slide both fingers into her bottom."
                else:
                    "Still lubed up from earlier, you easily slide two fingers into [the_person.possessive_title]'s bottom."
                the_person "Oh F..."
                $ mc.change_energy(-10)
                mc.name "Are you still working? You better be."
                the_person "Y... yes sir!"
                $ play_moan_sound()
                "[the_person.possessive_title!c] tries to muffle her groans as you finger her puckered hole."
                $ the_person.change_arousal(20)
                if the_person.arousal_perc > 100:
                    the_person "Oh god... ohhh!"
                    "Her whole body tenses up and she pushes back against you. A shiver runs through her body as she climaxes."
                    the_person "Your fingers... oh fuck!"
                    $ the_person.have_orgasm()
                    $ the_person.change_slut(1, 70)
                    "She quivers with pleasure for a few seconds before her whole body relaxes."
                elif the_person.arousal_perc > 50:
                    "[the_person.possessive_title!c]'s cunt is leaking juices as you finger her forbidden hole."
                    mc.name "You are such a good slut, you like my fingers in your tight little asshole, don't you?"
                    the_person "Yes [the_person.mc_title]!"
                    "You stroke her depths for a while longer as she tries to work at her terminal."
                else:
                    "[the_person.title] lets out a little gasp now and then as she tries to continue working at the computer terminal."
                    "Her body is warming up quickly from your touch as you stroke her depths a little longer."

            # "Finger her ass and pussy {energy=-10}" if the_person.opinion.anal_sex >= 0 and the_person.vagina_availableand (the_person.sluttiness > 50 or the_person.obedience > 160):
            #     pass
            "Finish":
                $ loop_choice = "finish"

        if loop_choice == "finish":
            "You are done with teasing yourself for now."
        else:
            #Right here we need the option to interact with other people in the room.
            if the_person.vagina_available:
                $ mc.change_locked_clarity(30)
            else:
                $ mc.change_locked_clarity(10)
            if mc.arousal_perc > 90 or mc.energy < 20:
                $ loop_choice = "finish"
                "You decide that it is time to stop teasing yourself."
            if mc.lust_tier >= 4 or (mc.lust_tier * 2 > mc.focus):
                $ loop_choice = "finish"
                "You stare blankly at the ass in front of you. You are painfully turned on and can't focus anymore."
                "The teasing has gone far enough. You need to stop now or move on."
    return
