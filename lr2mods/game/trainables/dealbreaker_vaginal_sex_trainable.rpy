init 2 python:

    def dealbreaker_vaginal_factor(the_person):
        base_factor = -2    #We start with the person's base opinion level
        if mc.inventory.has_serum_with_trait(vaginal_enhancer):
            base_factor += 1
        if the_person.has_broken_taboo(["licking_pussy", "anal_sex"]):
            base_factor += 1
        if the_person.energy >= DEALBREAKER_HIGH_ENERGY:
            base_factor += 1
        return base_factor

label train_dealbreaker_vaginal_sex_label(the_person):
    python:
        after_training_opinion_score = dealbreaker_vaginal_factor(the_person)
        mc.reset_arousal()
        the_person.draw_person() # make her stand up

    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    if mc.location.is_public:
        mc.name "Not here, let's go somewhere private."
        call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_train_dealbreaker_vaginal_sex

    mc.name "I've noticed that you don't like sex in general. This is a dealbreaker for me."
    mc.name "I want you to reconsider. I think if you try it again, with an open mind, you might be pleasantly surprised."
    the_person "You want me to what!?!"
    "For a second, it almost appears that her hatred of sex has snapped her out of her trance, but your soothing words soon have her back to her trance state."
    mc.name "It's okay that you may not necessarily like it, but I think with the right partner and some patience, you could actually enjoy it some."
    the_person "Hmmm... I don't know..."
    if dealbreaker_give_enhancing_serum(the_person, vaginal_enhancer):
        "In her trance like state, [the_person.possessive_title] drinks the serum obediently. This will help with the process."
    else:
        mc.name "Don't worry, you can go slow."
        "You wish you had a serum with you that you could give her that would help ease her into this."

    if the_person == camila:
        the_person "Well, it's just that I can't get pregnant, so I never bothered too much."
        mc.name "That doesn't prevent you from enjoying it, right?"
        the_person "I guess..."
        mc.name "I know you like me, let's give it a try, maybe you would enjoy it afterall."
    elif the_person == mom:
        the_person "The problem is that I love sex and I want all of you inside me."
        the_person "But we shouldn't do that, imagine if I got pregnant, that's why we can't do it."
        mc.name "I know you love me, so as long as we are careful, we should be okay, right?"
        the_person "Maybe... perhaps..."
        mc.name "Let's give it a try and see how it works out."
    elif the_person.has_broken_taboo(["licking_pussy", "anal_sex"]):
        if the_person.has_broken_taboo("anal_sex"):
            mc.name "You do like it when I shove my cock into your ass, right?"
            the_person "Yes, of course."
            mc.name "I guess it feels really good when I do it."
            the_person "Mmm, yes, it does."
            mc.name "Wouldn't it feel good if I tease your pussy and slide it in?"
            the_person "I don't know, I could get pregnant..."
            if the_person.kids == 0:
                "It seems you found the root cause of her aversion, she's not ready to be a mother."
            else:
                "It seems you found the root cause of her aversion, she doesn't want to get pregnant again."
            mc.name "Millions of people have sex every day and they don't get pregnant, especially if I don't cum inside your beautiful pussy."
            the_person "Yeah...that's true."
            mc.name "Should we give it a try? I promise I won't cum inside you and you will love the feeling."
        elif the_person.has_broken_taboo("licking_pussy"):
            mc.name "I know you love it when I lick your wet pussy and shove my fingers inside."
            the_person "Ohh yeah, that does feel good..."
            mc.name "Doesn't that mean I can give you the same kind of pleasure when I shove my cock inside and kiss you deeply?"
            the_person "Yes, of course. But I won't get pregnant if you lick me."
            if the_person.kids == 0:
                "It seems you found the root cause of her aversion, she's not ready to be a mother."
            else:
                "It seems you found the root cause of her aversion, she doesn't want to get pregnant again."
            mc.name "How about we start slow and I don't cum inside you? I bet you will enjoy it."
            the_person "I... I don't know..."
            mc.name "Shhh, just let it happen. I promise I won't cum inside you and you will love the feeling."
    else:
        mc.name "You are so beautiful and I really want to make you happy, shall we try it, just one time, so you know how it feels?"
        the_person "I don't know, I could get pregnant..."
        if the_person.kids == 0:
            "It seems you found the root cause of her aversion, she's not ready to be a mother."
        else:
            "It seems you found the root cause of her aversion, she doesn't want to get pregnant again."
        mc.name "If I promise I won't get you pregnant, will you at least give it a chance with me?"
        the_person "I really like you, but..."
        mc.name "Shhh, just let it happen. I will take you to heaven and keep you safe..."

    the_person "I could... try it, once...just once..."

    if the_person.energy <= DEALBREAKER_HIGH_ENERGY:
        "[the_person.possessive_title!c] is too tired to resist from your earlier sexual activity, but she doesn't seem to have much enthusiasm either."
        the_person "Ok... lets try it."
        "You wonder how this would have gone if she had more energy before you tried to convince her."
    else:
        the_person "I do want to make you feel good. I think you talked me into trying it at least."
        "[the_person.possessive_title!c] is energetic. She actually seems a little eager to give it a try now that you've talked her into it."

    if not the_person.vagina_visible:
        "You start to undress her so you have access to her lovely pussy."
        $ the_person.strip_to_vagina(prefer_half_off = True)

    # copy missionary taboo break
    "You take [the_person.title]'s hands in yours and guide her down on her back. She follows your lead, lying down for you."
    $ the_person.draw_person(position = "missionary")
    "You place your hands on her knees and spread her legs, kneeling down between them."
    "You slide your hard cock over her lips and clit, teasingly close to pushing inside of her."
    "[the_person.possessive_title!c] looks at you with a combination of lust and fear."

    mc.name "Don't worry, I will be careful, just enjoy the feeling."

    $ mc.change_locked_clarity(20)
    $ play_moan_sound()
    "You slowly slide the tip of your cock inside of her, and she gasps with pleasure."
    "As you try to move back, she wraps her legs around your buttocks and pulls you completely inside her."
    the_person "Oh god, this is so good..."

    $ mc.change_locked_clarity(20)
    $ play_moan_sound()
    "She moans into your ear and pulls you closer to her."
    "You kiss her neck a few more times, then divert all of your attention to making love."

    $ mc.change_locked_clarity(20)
    mc.name "You feel amazing [the_person.title], I wish I could fuck you like this all day."
    $ play_moan_sound()
    "She moans and trembles beneath you."
    the_person "Please do, [the_person.mc_title], keep going all day long."

    $ mc.change_locked_clarity(20)
    "[the_person.title] is scratching her fingernails down your back. She is moaning with every thrust."
    the_person "It's so good... I'm gonna cum!"
    "You use your full weight to push your cock deep inside [the_person.possessive_title]'s cunt as she climaxes."
    $ the_person.have_orgasm()
    "She quivers with pleasure pushing you over the edge."

    if the_person not in (camila, mom):
        the_person "PULL OUT!"
        mc.name "I'm cumming..."

    $ orgasm_choice = renpy.display_menu(orgasm_location_formatted_menu(the_person, [["Inside her", "creampies"], ["On her belly", "being covered in cum"],["On her face", "cum facials"]]), True, "Choice")
    if orgasm_choice[0] == "On her face":
        "You quickly pull out of [the_person.possessive_title]'s wet slit, and take aim at her face."
        "[the_person.title] quickly closes her eyes, knowing what it is going to happen."
        $ the_person.cum_on_face()
        $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
        $ the_person.draw_person(position = "missionary")
        "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s face."
        $ the_person.draw_person(position = "missionary", emotion = "happy")
        "When you are done, she gives you a big smile."
        $ after_training_opinion_score += 1

    elif orgasm_choice[0] == "On her belly":
        "You pull just far enough out of [the_person.possessive_title]'s wet slit."
        $ the_person.cum_on_stomach()
        $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
        $ the_person.draw_person(position = "missionary")
        "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s belly."
        $ the_person.draw_person(position = "missionary", emotion = "happy")
        "When you are done, she gives you a big smile."

    elif orgasm_choice[0] == "Inside her":
        "The warm feeling of her slick pussy is just to good to pull out."
        if the_person in (camila, mom):
            "As you start pumping your seed deep inside of her, she puts her legs around you pulling you deeper inside her."
        else:
            "As you start pumping your seed deep inside of her, you can feel her desperately trying to push you off."
        $ the_person.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        $ the_person.draw_person(position = "missionary", emotion = "angry")
        if the_person in (camila, mom):
            the_person "Ah, yes, fill me up with your hot cum!"
            $ after_training_opinion_score += 1
        else:
            the_person "What the fuck are you doing? You promised..."
            $ the_person.change_stats(love = -20, happiness = -30, slut = -15)
            "It seems you fucked up, badly."
            mc.name "I'm sorry, you just felt so amazing, I just couldn't pull out."
            the_person "I don't care, you shouldn't have done that."
            "She rearranges her clothes and gets up, giving you an angry stare."
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            $ the_person.draw_person(emotion = "angry")
            "It seems you didn't succeed in changing her mind about vaginal sex."
            return False

    "After taking a moment to recover, you both stand up."
    $ the_person.update_opinion_with_score("vaginal sex", after_training_opinion_score, add_to_log = True)
    $ the_person.draw_person(emotion = "happy")
    mc.name "So, what do you think?"
    if after_training_opinion_score == -1:
        the_person "I guess it wasn't as bad, as long as you don't cum inside me."
        mc.name "So you would be up for it again sometime?"
        the_person "... perhaps... ask me again another time, okay?"
    elif after_training_opinion_score == 0:
        the_person "That was nice. I think you're right, it does feel good."
        mc.name "Do you think you would be up for it again sometime?"
        if the_person == camila:
            the_person "Yeah, I think so."
        else:
            the_person "Yeah, I think so, as long as you don't get me pregnant!"
    elif after_training_opinion_score == 1:
        the_person "You are right. I didn't think I would like it this much..."
    elif after_training_opinion_score >= 2:
        the_person "I... I came so hard, I was so excited. Can we give it another try?"
        mc.name "Soon, don't worry."

    "You feel like you made excellent headway with [the_person.possessive_title]. She no longer hates vaginal sex!"
    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_dealbreaker_vaginal_sex
    python:
        the_person.apply_planned_outfit()
        del after_training_opinion_score
        del orgasm_choice
    return True
