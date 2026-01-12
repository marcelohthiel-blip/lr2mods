# Personal secretary actions.
# She works in front of the CEO Office. Use her to give MC some relief when his lust is high
# Generally she should slowly work up sluttiness actions until becoming his willing sub
# Options open up thru obedience and sluttiness

label personal_secretary_general_hire_label():   # use this label after hiring a generic girl to be your secretary.
    $ the_person = mc.business.personal_secretary
    "You call [the_person.title] to your office. After a minute, she appears in the door."
    $ the_person.change_location(ceo_office)
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "Yes. Sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "I have a position that I would like to move you to. I am in need of a personal secretary."
    mc.name "You will continue your work in HR, but instead of being down in the main offices you will be up here in front of my office."
    if the_person.is_girlfriend:
        the_person "So I'll be right here? With access to my boyfriend? All alone in his office?"
        the_person "That seems like a total win!"
    elif the_person.is_affair:
        the_person "Oh my god... that's a great idea."
        the_person "I'll be able to tell me [the_person.so_title] about my promotion... and why I've been spending so much time with my boss lately!"
    elif the_person.is_family:
        the_person "Huh, that is going to be great!"
        the_person "It'll be like the two of us are running a family business together!"
    elif the_person.sluttiness >= 60:
        the_person "Oh my god... so I'll be up here? With you?"
        the_person "You think you might... need some attention in your office from time to time?..."
        "She bites her lip for a moment when she finishes her lusty question."
    elif the_person.obedience >= 160:
        the_person "Oh! Of course, I'll be able to help you with anything you need [the_person.mc_title]!"
    elif the_person.love >= 60:
        the_person "Oh! That sounds great! It'll be so much fun to be so close to you!"
    else:
        the_person "Oh? Okay, that sounds doable."
        the_person "I'd be glad to take on a little extra responsibility."
    mc.name "Good. Glad to hear it."

    call initial_set_duties_label(the_person) from _call_initial_set_duties_personal_secretary_hire

    mc.name "Now go and get your stuff moved to the desk up here and I'll let you know when I need your personal assistance."
    the_person "Okay, I'll go right away!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] gets up and walks out of your office. You watch her hips swaying as she leaves."
    "You now have a personal secretary. While she usually just performs HR duties, she may be useful for other duties if you feel your lust building too high..."
    $ clear_scene()
    return

label personal_secretary_set_lust_tier_label(the_person):   #Use this label to set when the personal secretary should sex MC.
    mc.name "I wanted to talk to you about when you come in to my office when you notice that I'm... distracted."
    the_person "Oh? What did you want to change?"
    mc.name "Only come in if you see that I'm..."
    menu:
        "... distracted. \n{menu_green}Lust > 25%%{/menu_green}":
            mc.name "I still need to have time to accomplish all of my regular work tasks."
            the_person "I understand sir."
            $ the_person.event_triggers_dict["ps_lust_tier"] = 2
        "... very distracted. \n{menu_green}Lust > 50%%{/menu_green}":
            mc.name "Just when you see that my work is starting to suffer."
            the_person "Of course sir."
            $ the_person.event_triggers_dict["ps_lust_tier"] = 3
        "... extremely distracted. \n{menu_green}Lust > 90%%{/menu_green}":
            mc.name "Only when you see it is almost impossible for me to get any work accomplished."
            the_person "Sounds good, sir."
            $ the_person.event_triggers_dict["ps_lust_tier"] = 4

    return

label personal_secretary_test_label(the_person):
    the_person "Hey, this is great, being your very own personal secretary!"
    mc.name "Yes.... yes it is...."
    return

label personal_secretary_quick_service_choice_label():
    if not personal_secretary_will_suck():
        return
    if mc.lust_tier >= 4:
        "Your recent encounters with employees and other women in your life has left you painfully aroused."
    elif mc.lust_tier >= 3:
        "You find your mind wandering, day dreaming about sexual encounters with your employees."
    else:
        return
    "Maybe you should utilize your personal secretary for some relief..."
    menu:
        "Use your secretary":
            call personal_secretary_quick_service_label from _personal_secretary_choice_scene_01
        "Keep working":
            "Maybe later, for now you want to get back to work."
    return

label personal_secretary_quick_service_label():
    if mc.business.personal_secretary == None:
        return False
    $ the_person = mc.business.personal_secretary
    "You are way too turned on to go back to your work now."
    if mc.location == ceo_office:
        "You call in your personal secretary."
    else:
        $ mc.change_location(ceo_office)
        "You head straight to your office, sit at your desk and call in your personal secretary."
    $ the_person.draw_person()
    the_person "You wanted to see me sir?"
    menu:
        "Bend her over your desk" if personal_secretary_will_fuck():
            mc.name "Yes. Get over here and bend over my desk. Now."
            $ popup_text = personal_secretary_quick_service_fuck_popup_text()
            $ show_popup_hint(popup_text)
            $ the_person.change_arousal(10)
            "You stand up and walk around the front of your desk as you pull out your cock."
            the_person "Oh! Yes sir!"
            $ the_person.draw_person(position = "standing_doggy")
            if the_person.vagina_available and the_person.vagina_visible:
                "As soon as she bends over, her hot little cunt is exposed and ready for you to penetrate."
            else:
                "You quickly pull down all the clothing between you and her hot little cunt."
                $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = True)
            "You grab her hip with one hand, and with your other hand you line up your cock with her slit."
            "You rub yourself up and down it a few times before you inform her what is about to happen."
            mc.name "I can't promise that you'll finish, but I NEED to cum!"
            $ the_person.change_obedience(2, 160)
            $ the_person.change_arousal(10)
            the_person "Yes sir! That's my job!"
            "Her slit seems wet enough, so you push your hips forward, sliding your manhood into [the_person.possessive_title]'s inviting cunt."
            if the_person == mom:
                the_person "OH my god, I'm so glad I left my last job to come here!"
            else:
                the_person "Oh my god... I'm so glad I took this position..."
            "Seeing no reason to hold back, you grab her hips with both hands and begin to fuck her eagerly."
            $ the_person.change_arousal(20)
            if mc.sex_skills["Vaginal"] >= 6:   #You atleast get a double orgasm,
                the_person "Yes! Oh fuck that's so good..."
                "[the_person.possessive_title!c] reaches back with both hands, spreading her ass cheeks for you, giving you an amazing view while also providing for maximum penetration."
                "She is clearly enjoying herself. While you don't really care if she gets off, you figure if she is that turned out, might as well put in the extra effort and make sure she cums."
                "Besides, feeling her hot little cunt quiver and cum around your cock will only make your own orgasm even better."
                $ the_person.change_arousal(20)
                mc.name "That's it slut. Take your boss's cock like a good little whore."
                if the_person == mom:
                    the_person "Yes Hon... I mean boss! Fuck me good!"
                else:
                    the_person "Oh yes! fuck me good!"
                if (mc.max_energy >= 160 or perk_system.has_ability_perk("Serum: Feat of Orgasm Control")):
                    $ the_person.change_arousal(50)
                    "You hips slap relentless against [the_person.possessive_title]'s ass, filling the room with lewd noises."
                    "Her moans grow urgent and soon you are rewarded for your endurance as she gets ready to orgasm."
                    "[the_person.possessive_title!c]'s legs start to quiver, and then suddenly she tenses up."
                    if the_person.effective_sluttiness() >= 80:
                        if the_person.is_bald:
                            "You thrust yourself in all the way, burying yourself inside of her as she starts to cum."
                            "You spank her ass harshly as her cunt quivers and spasms all around you. She yelps and moans in pleasure."
                        else:
                            "You grab her by the hair and yank back roughly a you thrust all the way inside her as she starts to cum."
                            "Her cunt quivers and spasms all around you and she yelps and moans in pleasure."
                    else:
                        "You bury your cock deep in [the_girl.possessive_title]'s cunt while she cums. Her pussy spasms around you."
                    $ the_person.have_orgasm(half_arousal = True)
                    "You don't bother waiting for her to recover. Before she even finishes, you grab her hips and resume roughly fucking her."
                    the_person "Ahh! Oh fuck..."
                    "She cries out when your hips start to slap against her ass yet again. She is so turned on by getting used by you, she's probably going to cum again."
                "Your secretary's eager pussy is so good, you feel your own orgasm approaching."
                mc.name "That's it my little slut, I'm going to give you your reward!"

                call standing_doggy_double_orgasm(the_person, ceo_office, make_desk()) from _secretary_quick_service_double_orgasm_fuck_01
                "It takes [the_person.title] several seconds before she recovers enough to get her bearings."
                "She carefully stands up."
                $ the_person.draw_person(position = the_person.idle_pose)
                the_person "Th... Thank you... sir!"
            else:
                pass

        "Use her mouth":
            $ popup_text = personal_secretary_quick_service_suck_popup_text()
            $ show_popup_hint(popup_text)
            mc.name "Yes. Get over and get on your knees. Now."
            $ the_person.change_arousal(10)
            "You stand up and walk around the front of your desk as you pull out your cock."
            the_person "Oh! Yes sir!"
            $ the_person.draw_person(position = "blowjob")
            "She gets down on her knees and looks up at you as you walk up to her. You put your hand on the back of her head."
            mc.name "Alright, open up. It's time to earn your paycheck."
            the_person "Yes sir!"
            $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
            "Your secretary obediently opens her mouth."


    "Satisfied with your secretary for now, you dismiss her."
    mc.name "I'm done with you for now. Clean up and get back to work."
    the_person "Yes sir!"
    $ the_person.draw_person(position = "walking_away")
    "She leaves your office and closes the door behind her, leaving you to enjoy your post orgasm buzz."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    return
