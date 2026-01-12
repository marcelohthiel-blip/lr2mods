#Counter = KHH01

#Home harem contains sex events related to Mom and Lily.

init 4 python:
    
    def shower_initialization(self):
        # No Init code for this yet.
        return

    def mom_willing_to_shower():
        if not mom.has_taboo("condomless_sex") and mom.is_available:
            return True
        return False

    def lily_willing_to_shower():
        if not lily.has_taboo("condomless_sex") and lily.is_available:
            return True
        return False

    def watching_tv_requirement():
        if not time_of_day == 4:
            return "It is too early"
        return True

    def watch_tv_initialization(self):
        hall.add_action(self)
        return

    def waking_up_next_to_mom_requirement():
        return (time_of_day == 0
            and mom.known_opinion.incest > 0
            and not mom.has_taboo("vaginal_sex")
            and mom.days_since_event("Last Vaginal Day") > 2
            and day%2 == 0
            and mom.is_available
            and mc.is_at(bedroom)
            and not mom.has_queued_event("sleeping_walk_in_label"))

    def waking_up_next_to_sis_requirement():
        return (time_of_day == 0
            and lily.known_opinion.incest > 0
            and not lily.has_taboo("vaginal_sex")
            and lily.days_since_event("Last Vaginal Day") > 2
            and day%2 == 1
            and lily.is_available
            and mc.is_at(bedroom)
            and not lily.has_queued_event("sleeping_walk_in_label"))

    morning_crisis_list.append(
        Action("Waking up to Mom next to me", waking_up_next_to_mom_requirement, "mom_morning_wakeup_label"))

    morning_crisis_list.append(
        Action("Waking up to Sis next to me", waking_up_next_to_sis_requirement, "lily_morning_wakeup_label"))
        
    mom_morning_shower_action = ActionMod("Asking mom to shower together", mom_willing_to_shower,"mom_shower_together_label", initialization = shower_initialization,
        menu_tooltip = "Mom is about to shower.", category="Home", is_crisis = True, is_morning_crisis = True)

    lily_morning_shower_action = ActionMod("Asking lily to shower together", lily_willing_to_shower,"lily_shower_together_label", initialization = shower_initialization,
        menu_tooltip = "Lily is about to shower.", category="Home", is_crisis = True, is_morning_crisis = True)

    watch_tv_action = ActionMod("Watch TV {image=gui/heart/Time_Advance.png}", watching_tv_requirement, "watching_tv_label",
        initialization = watch_tv_initialization, menu_tooltip = "Watch TV (with someone, hopefully, maybe?)", category="Home")

label mom_shower_together_label():
    $ the_person = mom
    "As you are about to enter the shower room, you saw the light from [the_person.possessive_title]'s room."
    "She probably just wake up and going to shower herself."
    $ mc.change_location(mom_bedroom)
    $ the_person.draw_person(position = "stand2")
    mc.name "Morning my beautiful [the_person.title], did you have had a good sleep?"
    the_person "Good morning handsome. Seems you had a good night sleep."
    mc.name "It'd be better if you were sleeping besides me. Anyway..."
    mc.name "Wanna take a bath together?"
    mc.name "I can wash your back."
    "[the_person.possessive_title!c] blushes and gives a shy nod."
    $ the_person.change_arousal(5)
    the_person "Okay, just give me one moment..."
    "[the_person.title!c] starts to strip down."
    $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list())
    $ mc.change_locked_clarity(20)
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "She looks up at you, slightly blushing."
    the_person "Shall we?"
    $ mc.change_location(home_shower)
    "You took a bit of time to admire her sexiness."
    $ the_person.change_arousal(10)
    $ the_person.strip_outfit(position = "stand5", exclude_feet = False)
    "Now completely nude, she gets into the shower."
    "You see the water running down her chest."
    if the_person.has_large_tits:
        "You can't help but admire [the_person.possessive_title]'s great body and [the_person.tits_description] some more."
        "Just as this thought flashes through your mind, she starts rubbing her boobs."
    else:
        "You can't help but admire [the_person.possessive_title]'s slim body and [the_person.tits_description]."
        "Just as this thought flashes through your mind, she starts rubbing her breasts, pinching her small nipples."
    the_person "Come.."
    $ mc.change_locked_clarity(10)
    "As you wash each other body, it's clear that both of you wanted more then just touching."
    the_person "[the_person.mc_title!c]..."
    $ the_person.change_arousal(10)
    $ mc.change_arousal(30)
    $ the_person.draw_person(position = "back_peek", emotion = "happy")
    if the_person.has_taboo("vaginal_sex"):
        "She bends over a little pushing her backside against your hard cock, trying to get it in her ass."
    else:        
        "She bends over a little pushing her backside against your hard cock, slowly pushing your hard member into her slick, [the_person.pubes_description] pussy."
    call fuck_person(the_person, start_position = (anal_standing if the_person.has_taboo("vaginal_sex") else standing_doggy), start_object = make_wall(), skip_intro = True) from _call_fuck_shower_together_KHH01
    $ the_report = _return
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "When you're finished [the_person.title] steps out of the shower and grabs a towel. She dries herself off, then wraps herself in it."
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    if the_report.get("girl orgasms",0)>0:
        the_person "Well that's a good way to start the day. Love you [the_person.mc_title]."
    elif the_report.get("guy orgasms",0)>0:
        the_person "Well I hope you enjoyed your start to the day. See you later."
    else:
        the_person "Well maybe we can pick this up some other time. See you later."
    $ clear_scene()
    "Feeling refreshed with the shower, you go back to your room to get dressed."
    $ mc.change_location(bedroom)
    return

label lily_shower_together_label():
    $ the_person = lily
    "As you are about to enter the shower room, you saw the light from [the_person.possessive_title]'s room."
    "She probably just wake up and going to shower herself."
    $ mc.change_location(lily_bedroom)
    mc.name "Morning [the_person.title], you look fabulous this morning."
    $ the_person.draw_person(position = "stand5")
    "She looks you up and down suspiciously."
    the_person "All right, what do you want..."
    mc.name "I was going to take my shower..."
    the_person "And..."
    mc.name "Well, I was thinking... wanna take the bath together?"
    mc.name "I can wash your back. And front. From top to bottom. Free of charge!"
    "[the_person.possessive_title!c] throws her pillow at you."
    the_person "Pervert!"
    $ the_person.change_arousal(5)
    the_person "Just give me a sec..."
    "[the_person.title!c] starts to strip down."
    $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list())
    $ mc.change_locked_clarity(20)
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    the_person "Come on. Lets have you cleaned. {i}*grins*{/i}"
    $ mc.change_location(home_shower)
    "She looks up at you, teasingly."
    $ the_person.change_arousal(10)
    $ the_person.strip_outfit(position = "stand5", exclude_feet = False)
    the_person "TA-DA!"
    "Now completely nude, she gets into the shower."
    "You see the water running down her chest."
    if the_person.has_large_tits:
        "You can't help but admire [the_person.possessive_title]'s great body and [the_person.tits_description]."
        "Just as this thought flashes through your mind, she starts rubbing her boobs."
    else:
        "You can't help but admire [the_person.possessive_title]'s slim body and [the_person.tits_description]."
        "Just as this thought flashes through your mind, she starts rubbing her breasts, pinching her small nipples."
    the_person "Don't just stand there oogling me..."
    $ mc.change_locked_clarity(10)
    "As you wash each other body, it's clear that both of you wanted more then just touching."
    the_person "[the_person.mc_title!c]..."
    $ the_person.change_arousal(10)
    $ mc.change_arousal(30)
    $ the_person.draw_person(position = "back_peek", emotion = "happy")
    if the_person.has_taboo("vaginal_sex"):
        "She bends over a little pushing her backside against your hard cock, trying to get it in her ass."
    else:        
        "She bends over a little pushing her backside against your hard cock, slowly pushing your hard member into her slick, [the_person.pubes_description] pussy."
    call fuck_person(the_person, start_position = (anal_standing if the_person.has_taboo("vaginal_sex") else standing_doggy), start_object = make_wall(), skip_intro = True) from _call_fuck_shower_together_KHH02
    $ the_report = _return
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "When you're finished [the_person.title] steps out of the shower and grabs a towel. She dries herself off, then wraps herself in it."
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    if the_report.get("girl orgasms",0)>0:
        the_person "Well that's a good way to start the day. Love you [the_person.mc_title]."
    elif the_report.get("guy orgasms",0)>0:
        the_person "Well I hope you enjoyed your start to the day. See you later."
    else:
        the_person "Well maybe we can pick this up some other time. See you later."
    $ clear_scene()
    "Feeling refreshed with the shower, you go back to your room to get dressed."
    $ mc.change_location(bedroom)
    return

label watching_tv_label():

    $ scene_manager = Scene()
    "Since you have nothing better to do, you decided to just stay home and watch the tv."
    
    $ the_choice = None
    $ series_type = None
    
    menu:
        "Watch an action series":
            $ the_choice = get_random_from_list(["69", "Games of Whores", "The Flasher", "Supergirl", "The Cunt Whore Universe", "She-Suck", "The Ass-Team"])
            $ series_type = "action"
            #if the_person == aunt:
            #    $ likes_genre = True

        "Watch a comedic series":
            $ the_choice = get_random_from_list(["The Big Cum Theory", "Friends - with benefit", "How I fuck your mother", "Whose Cum Is It Anyway", "The Fresh Princess of Bel Air"])
            $ series_type = "comedy"
            #if the_person == lily:
            #    $ likes_movie = True

        "Watch a romantic series":
            $ the_choice = get_random_from_list(["Family Matters", "Cummed","Twin Cheeks", "Beaverly Hills 96910"])
            $ series_type = "romantic"
            #if the_person == mom:
            #    $ likes_genre = True

        "Watch an anime":
            $ the_choice = get_random_from_list(["Naruto", "Dragon Ball", "Fairy Tail", "One Piece", "Initial D", "My Hero Academia"])
            $ series_type = "anime"
            #if the_person == cousin: #Never cared about her, so maybe.. wrong?
            #    $ likes_genre = True

    "You decided to watch '[the_choice]' after looking to the offerings. It's been a while since you watched a good [series_type] series."

    if aunt_living_with_mc(): 
        $ guest = renpy.random.randint(0, 4) 
    else:
        #after testing, so many uninteresting lonely event. so now, until home harem established, theres 33% chance of loneliness
        $ guest = renpy.random.randint(0, 2) 

    if guest == 0 and (mom.is_available and lily.is_available):        
        if had_family_threesome():
            $ the_person = mom
            $ the_other = lily
            "You were watching the tv in peace when [the_person.fname] walks in."
            $ scene_manager.add_actor(the_person, the_person.get_random_appropriate_underwear(guarantee_output = True))
            $ mc.change_locked_clarity(10)
            the_person "So... What are we watching?"
            "You shift the end of the couch to let [the_person.possessive_title] to sit down next to you."
            $ scene_manager.update_actor(the_person, display_transform = character_left_flipped, position = "sitting")
            mc.name "'[the_choice]'. Do you prefer we watch something else?"
            the_person "Ah no, no... I'm fine with whatever you wanna watch."
            "[the_person.title] settles into the couch, sitting right next to you as she watches."
            "As time goes on though, [the_person.title] scoots over a bit closer to you, putting her head on your shoulder."
            if the_person.wearing_panties:
                "At a particular steamy scene, you feel [the_person.title] take your hand. She guides your hand to her stomach and starts to slide your hand over her panties."
            elif the_person.vagina_visible:
                "At a particular steamy scene, you feel [the_person.title] take your hand. She guides your hand to her stomach and starts to slide your hand down her pussy."

            $ mc.change_locked_clarity(10)
            "[the_person.possessive_title!c] shifts in her seat a little, pulling off her panties, before opening her legs up to give your fingers easy access."
            $ scene_manager.strip_full_outfit(person = the_person)
            $ scene_manager.update_actor(the_person, position = "missionary")     
            $ the_person.change_arousal(10)       
            "She sighs when your finger slides between her labia. You can feel that she is already a little aroused as you slide your fingers along her slit."
            "Her hand moves over into your lap as well. Through your pants you feel her start to stroke your rapidly hardening cock."
            "Things getting more heated up at the moment, the tv forgotten."
            $ mc.change_locked_clarity(10)    
            $ the_person.change_arousal(10)       
            "Both didn't realized until.."
            the_other "Ehem.."
            $ scene_manager.add_actor(the_other, the_other.get_random_appropriate_underwear(guarantee_output = True), emotion = "happy")
            the_other "Leaving me out?"
            $ scene_manager.strip_full_outfit(person = the_other)
            $ scene_manager.update_actor(the_other, position = "sitting")
            $ mc.change_locked_clarity(20)
            call start_threesome(the_person, the_other) from _threesome_watch_tv_KHH01
            $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_center_flipped)
            $ scene_manager.update_actor(the_other, position = "missionary", display_transform = character_right)
            $ the_report = _return
            if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0:  #Happy family
                "[the_person.possessive_title!c] falls into the couch on one side of you on her side, while [the_other.title] lies on her back next to you."
                the_person "Oh my god... you two... that was amazing!"
                $ the_person.change_happiness(10)
                the_other "I know... I swear [the_person.mc_title] makes me cum my brains out."
                $ the_other.change_obedience(10)
                "You all lay together for a while in your sex-induced afterglow. You enjoy the two girls warming you from each side."
                mc.name "Whatever happens to my series?"
                "Both chuckles."
                the_other "Just rewatch the episode then."
            else:
                "The girls fall into the couch beside you. You relax for a little bit, enjoying the warmth of their bodies."
            the_person "Well. I should get up before I fall asleep. Goodnight you two!"
            $ scene_manager.update_actor(the_person, position = "walking_away")
            the_other "Goodnight [the_person.fname]! Actually, I should probably get to bed as well, I just remembered I have to get up early..."
            $ scene_manager.remove_actor(the_person)
            $ scene_manager.update_actor(the_other, position = "walking_away", display_transform = character_right)
            "You watch as [the_other.possessive_title] gets up and excuses herself, her ass swaying back and forth as she walks away."
            "God damn guess you have to rewatch the episode!"
            $ scene_manager.remove_actor(the_other)
        else:
            "[the_choice] was quite entertaining."    
            "You find yourself humming to the ending theme as it plays at the end."
    elif guest == 1 and mom.is_available:
        $ the_person = mom
        $ scene_manager.add_actor(the_person, the_person.outfit, position = "stand5")
        if series_type == "romantic":
            "You were watching the tv in peace when [the_person.fname] walks in."
            the_person "So... What are you watching?"
            mc.name "'[the_choice]'."
            the_person "Oh nice, my son is such a romantic guy."
            the_person "Mind if [the_person.possessive_title] watches with you?"
            "You shift the end of the couch to let [the_person.possessive_title] to sit down next to you."
            mc.name "Of course, [the_person.title], always a pleasure."
            $ the_person.change_stats(happiness = 2, love = 1, max_love = 50)
            $ scene_manager.update_actor(the_person, position = "sitting", emotion = "happy")
            "[the_person.title] settles into the couch, sitting right next to you as she watches."
            "As time goes on though, [the_person.title] scoots over a bit closer to you, putting her head on your shoulder."
            "At a particular steamy scene, you feel [the_person.title] starts breathing hard."
            $ the_person.change_arousal(10)
            "Her free hand snaked down between her legs. She bites her lip as her eyes glued to the hot scene on tv."
            $ the_person.change_arousal(10)
            "The action escalates, and [the_person.possessive_title]'s breathing becoming more irregular."
            $ the_person.change_arousal(10)
        else:
            "You were watching the tv in peace when [the_person.fname] walks in."
            the_person "So... What are you watching?"
            mc.name "'[the_choice]'."
            the_person "Oh..."
            the_person "Mind if [the_person.possessive_title] watches with you?"
            "You shift the end of the couch to let [the_person.possessive_title] to sit down next to you."
            mc.name "Of course, [the_person.title], always a pleasure."
            $ scene_manager.update_actor(the_person, position = "sitting")
            "[the_person.title] settles into the couch, sitting right next to you as she watches."
            "As time goes on though, it's becoming clear that [the_person.title] isn't enthralled by it."
            "Her hand sneakily slides down her crotch. She bites her lip trying to stiffle her moans."
        
        if aunt_living_with_mc() or the_person.has_taboo("vaginal_sex"):
            #game wise, the aunt is always there but event wise she gone somewhere, so starting sex with mom/lily will get aunt as audience
            "As it happens, she caught you staring, prompting her to stands up."
            $ the_person.change_arousal(10)
            $ scene_manager.update_actor(the_person, position = "stand5")
            the_person "Ah, I'm sorry, I just remembered I need to wake up early tomorrow."
            the_person "Good night."  
            $ scene_manager.update_actor(the_person, position = "walking_away")
            $ the_person.change_slut(1, 30)
            "She hurriedly walks away."
            "You chuckles. She definitely ain't sleeping any time soon in that state."
            "You continue watching the tv alone." 
            $ scene_manager.hide_actor(the_person)
        else:
            "There's no reason to hold back now that you already done everything with her."
            "You shift yourself and slide your hand down to where her hand are."
            $ the_person.change_arousal(10)
            "She gasps but quickly shifts a bit more, opening her legs up to give your fingers easy access."
            call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_KHH01
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0:  
                "[the_person.possessive_title!c] falls into the couch on her back."
                $ scene_manager.update_actor(the_person, position = "missionary")
                the_person "Oh my god... that was amazing!"
                $ the_person.change_stats(happiness = 2, obedience = 1, slut = 1, max_slut = 60)
                "You both lay together for a while in your sex-induced afterglow. You enjoy having her warmth by your side."
                mc.name "Heh, this definitely better then watching tv."
                "She chuckles."
                the_person "Definitely. Oh, it's ended as well."
                call check_date_trance(the_person) from _call_check_date_trance_watch_tv_KHH01
                the_person "Go on, wash yourself first. My legs still shaky."
            else:
                "[the_person.possessive_title!c] fall into the couch beside you. You relax for a little bit, enjoying her warmth."
                the_person "I'm going to bed."
                the_person "Good night."  
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "She hurriedly walks away."
                "You continue watching the tv alone." 
                $ scene_manager.hide_actor(the_person)

    elif guest == 2 and lily.is_available:
        $ the_person = lily
        $ scene_manager.add_actor(the_person, the_person.outfit, position = "stand5")
        if series_type == "comedy":
            "You were laughing out loud enjoying '[the_choice]' alone when [the_person.fname] walks in."
            the_person "You are loud [the_person.mc_title]. Way too loud!"
            the_person "Oh! It's '[the_choice]'."
            $ scene_manager.update_actor(the_person, position = "stand5", emotion = "happy")
            the_person "Scoot over, I wanna watch too!"
            "You shift the end of the couch to let [the_person.possessive_title] to sit down next to you."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion = "happy")
            "It's clear that [the_person.fname] is having a great time. She's leaning forward in her seat, eyes fixed firmly on the screen."
            "Both of you laugh together just like any normal siblings watching tv together."
            $ the_person.change_happiness(3)
            if the_person.has_broken_taboo("vaginal_sex") and not aunt_living_with_mc():
                "She glanced at mom's bedroom door."
                the_person "Hey [the_person.mc_title], mom's asleep."
                mc.name "Oh... what nefarious plan are you planning with that information?"
                "She chuckles."
                the_person "Lets fuck!"
                $ mc.change_locked_clarity(10)
                mc.name "Straight to the point, eh sis?"
                $ mc.change_locked_clarity(10)
                the_person "Oh shut up... Do you want to or not?"
                $ the_person.change_arousal(10)
                mc.name "I'm certainly not going to stop you."
                $ mc.change_locked_clarity(10)
                "She grins."
                "Her hand slides up to your waist and undoes the button to your pants. You get a jolt of pleasure as her fingers slide onto your hardening cock."
                $ the_person.change_arousal(10)
                "She quickly repositioned herself, now kneeling in front of you."
            else:
                the_person "That was fun. Don't forget to call me if you watching [the_choice] again."
        else:
            "You were watching the tv in peace when [the_person.fname] walks in."
            the_person "So... What are you watching?"
            mc.name "'[the_choice]'."
            the_person "Eww...Bet you just watching it because of that character there?"
            "She smirks at you while holding her boobs together and jiggles it."
            the_person "What's her name again? Miss Bew-bies?~"
            "You throw a nearby cushion at her."
            "She playfully ducked while still laughing at you."
            the_person "Since I'm bored, let this beautiful [the_person.title] watch with you, now scoot over!"
            "You shift the end of the couch to let [the_person.possessive_title] to sit down next to you."
            $ the_person.change_stats(happiness = 2, love = 1, max_love = 50)
            mc.name "You can really be annoying at times."
            the_person "Of course, who else could I annoy if not my own bro."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion = "happy")
            if the_person.has_broken_taboo("vaginal_sex") and not aunt_living_with_mc():
                "It doesn't take long before it's clear that [the_person.title] isn't enthralled by it."
                "You feel her hand on your thigh. She squeezes it gently and slides her hand up higher and higher while whispering into your ear."
                $ the_person.change_arousal(10)
                the_person "I'm bored. You don't mind if I make this a little more interesting, do you?"
                $ the_person.change_arousal(10)
                mc.name "I'm certainly not going to stop you."
                $ mc.change_locked_clarity(10)
                "Her hand slides up to your waist and undo the button to your pants. You get a jolt of pleasure as her fingers slide onto your hardening cock."
                $ the_person.change_arousal(10)
                "She quickly repositioned herself, now kneeling in front of you."
            else:
                "After a while..."
                the_person "This is boring~"
                the_person "And I'm sleepy."
                the_person "I'm going to bed."
                        
        if aunt_living_with_mc() or the_person.has_taboo("vaginal_sex"):
            #game wise, the aunt is always there but event wise she gone somewhere, so starting sex with mom/lily will get aunt as audience
            $ scene_manager.update_actor(the_person, position = "stand5")
            the_person "Good night."  
            $ scene_manager.update_actor(the_person, position = "walking_away")
            "She walks away."
            $ scene_manager.hide_actor(the_person)
        else:
            call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True) from _call_fuck_person_KHH02
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0:  
                "[the_person.possessive_title!c] falls into the couch on her back."
                $ scene_manager.update_actor(the_person, position = "missionary")
                the_person "Oh my god... that was amazing!"
                $ the_person.change_stats(happiness = 2, obedience = 1, slut = 1, max_slut = 60)
                "You both lay together for a while in your sex-induced afterglow. You enjoy having her warmth by your side."
                mc.name "Heh, this definitely better then watching tv."
                "She chuckles."
                the_person "Definitely. Oh, it's ended as well."
                call check_date_trance(the_person) from _call_check_date_trance_watch_tv_KHH02
                the_person "Go on, wash yourself first. My legs still shaky."
            else:
                "[the_person.possessive_title!c] fall into the couch beside you. You relax for a little bit, enjoying her warmth."
                the_person "I'm going to bed."
                the_person "Good night."  
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "She hurriedly walks away."
                "You continue watching the tv alone." 
                $ scene_manager.hide_actor(the_person)

    elif guest == 3:
        $ the_person = aunt
        $ scene_manager.add_actor(the_person, the_person.outfit, position = "stand5")
        if series_type == "action":                                        
            the_person "You watching [the_choice]? Awesome!"
            the_person "You won't mind your old aunt watch together, aren't you?"
            mc.name "How about sexy?"
            the_person "Sexy?"
            mc.name "I don't mind my {i}~sexy~{/i} aunt watching tv together with me."
            "You patted the couch next to you and scoot over to give her space."
            $ the_person.change_stats(happiness = 2, love = 1)
            the_person "Sweet talker."
            $ scene_manager.update_actor(the_person, position = "sitting")
            "[the_person.possessive_title!c] settles into the couch, sitting right next to you as her eyes glued to the action on tv."
            the_person "I love this scene! Never get bored even though I've rewatched it several times already."
            "You chatted comfortably throughout the evening with her about the show."
            "..."
            "After the episode ends, [the_person.possessive_title] looks at you."
            the_person "Thank you. For entertaining me. For letting us stay."
            mc.name "That's what family is. Sorry, it's getting late, I have to go sleep."
            the_person "Oh my. Time really flies. I'll go and wash my face first."
            the_person "Good night, [the_person.mc_title]."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            "She pulls you into a hug before promptly left to the bathroom."
            $ scene_manager.hide_actor(the_person)
        else:
            the_person "Ah, you watching this?"
            the_person "Everytime I tried watching it, I ended up snoring halfway through."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            the_person "Have fun. I'll go hunting for your mom's wine stash."
            the_person "Don't stay up too late. Aunty needs her beauty sleep as well."
            $ scene_manager.hide_actor(the_person)
            "You continue watching the tv alone."
    elif guest == 4:
        # I dont think we can do much to change her in that short span of time.. So she stays as unfriendly as she is. 
        if series_type == "anime":                    
            $ the_person = cousin
            $ scene_manager.add_actor(the_person, the_person.outfit, position = "kneeling1")
            "As [the_choice]'s' opening theme starting, you saw [cousin.possessive_title] came to the living room and sat at the nearby corner."
            "Her eyes shifting from time to time to the show."
            mc.name "Just come sit at the couch and be comfortable."
            mc.name "I'm not a monster, you know."
            $ the_person.change_stats(happiness = 2, obedience = 1)
            $ scene_manager.update_actor(the_person, position = "sitting")
            "She paused, then simply move to sit at one of the single couch."
            mc.name "So-"
            the_person "Be quiet. I'm here to watch not talk."
            "There's a lot of thing you want to say back, but you decide against it and just enjoy the show."
            "..."
            "After the episode ends, [the_person.possessive_title] looks at you."
            the_person "Next episode?"
            mc.name "Nope, I have a busy morning tomorrow."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            $ the_person.change_stats(happiness = 2, obedience = 1)
            "She promptly stand and leave without a word."
            $ scene_manager.hide_actor(the_person)
        else:
            "[the_choice] was definitely the right choice tonight."    
            "You find yourself humming to the ending theme as it plays at the end."
            
    "You turned off the tv then heads to the empty bathroom a while later."
    "You clean yourself up in the bathroom, then head to bed."
    $ del the_choice
    $ del series_type
    $ mc.change_location(bedroom)
    $ clear_scene()
    call advance_time() from _call_advance_time_spend_the_night_KHH01
    return

label mom_morning_wakeup_label():
    $ mc.location.turn_lights_off()
    python:
        (sleep_wear, ran_num) = mom.event_triggers_dict.get("event_sleepwear", (None, 1))
        if sleep_wear is None or ran_num < day:
            sleep_wear = mom.get_random_appropriate_underwear(guarantee_output = True)
            sleep_wear.remove_shoes()   # she won't wear shoes to bed
            sleep_wear.remove_tights()  # she won't wear tights to bed
            mom.event_triggers_dict["event_sleepwear"] = (sleep_wear, day)

        mom.apply_outfit(sleep_wear) #She's sleeping in her underwear.
        sleep_wear = None

    "Your eyes fluttered open, your senses still foggy with sleep."
    "As you stretched lazily, you feel the warmth of the bed beneath you."
    "As you shifted, however, something—or rather, someone—caught your attention."    
    $ mom.draw_person(position = "missionary")
    "Her hair fanned out on the pillow, framing her peaceful face."
    "She must have sneaked in after you dozed off last night."
    "She is still sleeping, you can see the rise and fall of her chest with each breath, hear the faint whisper of her exhales."
    "You gave a sly smile. This was unexpected, but not unwelcome."
    "You scooted closer, inches apart from her. You can even feel the warmth radiating from her, and it sent a shiver down your spine."
    $ mc.change_locked_clarity(10)
    mc.name "Morning~"
    "You whispered softly, your voice barely audible. [mom.possessive_title!c] didn't stir, her breathing steady and rhythmic."
    "This gonna be fun."
    "You reached out slowly, fingers brushing against her smooth and warm arm."
    "Your hand travels higher, gently tracing the outline of her shoulder. She let out a soft sigh, but remained asleep."
    "Thrilled, you continued your exploration, fingertips now dancing lightly over her collarbone."
    mom "Mmm... Husband~"
    "[mom.possessive_title!c] murmured, her voice drowsy and confused. But then she settled back into her slumber, her breathing once again steady."
    "A sigh of relief, you leaned closer, lips almost touching her ears."
    mc.name "Good morning~"
    "You whispered again, teasing her."
    "But she only stirred slightly, turning her head towards you. Her hair brushed against your cheek, soft as silk."
    $ mc.change_locked_clarity(10)
    "You decided to switch tactic. Your hand slides lower, revealing more of her skin."
    "Your fingers trailed down to her waist, where you paused, savoring the sensation of her body beneath your hand."
    "She whimpered softly, her hips shifting subtly as if searching for comfort."
    $ mc.change_locked_clarity(10)
    "You began to trace small circles on her hip, each movement calculated to keep her relaxed and unalarmed. Your other hand crept up to her hair, brushing of a strand of hair over her face."
    mc.name "You're so beautiful when you sleep."
    "You leaned in and pressed a soft kiss to her temple. Her skin was warm and inviting, and you lingered there for a moment, inhaling her familiar scent."
    "It was a blend of lavender and something uniquely hers, something that always made you feel at ease."
    "As you pulled away, you noticed her eyelashes fluttering."
    "You held your breath, waiting to see if she woke up."
    "But after a few seconds, she settled back into her peaceful slumber, oblivious to your antic."
    "With gentle fingers, you brushed a stray lock of hair from her face, tucking it behind her ear."
    "Then, leaning in close, you whispered, "
    mc.name "I love you, Jennifer."
    "She opened her eyes, staring right at you."
    "Her lips curved into the faintest of smiles."
    mom "And I love you too, [mom.mc_title]."
    mc.name "You've awoke?"
    mom "Barely..."

    menu:
        "Escalate":
            "You lay there together in silence for a moment, just looking at each other. The air between felt thick, charged with an energy you couldn’t name."
            "The entire length of her leg pressed against you. Her gaze dipped from your eyes to your mouth, then back up. "
            "That's an invitation as clear as a day to you."
            $ mom.change_arousal(5)
            $ mc.change_locked_clarity(10)
            call fuck_person(mom, private = True, start_position = kissing, skip_intro = True) from _call_fuck_mom_KHH0
            $ the_report = _return
        "Wake up":
            pass

    "You lay in bed together for a little longer, but soon it is time to start the day."
    $ mc.location.turn_lights_on()
    $ mom.draw_person(position = "stand4")
    mom "Well, I better get back to my room."
    $ clear_scene()
    #$ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    #$ the_person.apply_planned_outfit(show_dress_sequence = True)
    return

label lily_morning_wakeup_label():
    $ mc.location.turn_lights_off()

    python:
        (sleep_wear, ran_num) = mom.event_triggers_dict.get("event_sleepwear", (None, 1))
        if sleep_wear is None or ran_num < day:
            sleep_wear = mom.get_random_appropriate_underwear(guarantee_output = True)
            sleep_wear.remove_shoes()   # she won't wear shoes to bed
            sleep_wear.remove_tights()  # she won't wear tights to bed
            lily.event_triggers_dict["event_sleepwear"] = (sleep_wear, day)

        lily.apply_outfit(sleep_wear) #She's sleeping in her underwear.
        sleep_wear = None

    "The first thing you noticed was the warmth."
    "Not the usual solitary sprawl into cold sheets, but a radiating, living heat along your back."
    "Then, the scent. A faint trace of vanilla and something... younger. Sweeter. Her shampoo."
    "Eyes opened to the weak morning light filtering through the blinds. You was on your side, facing the door, and the space behind you was unmistakably occupied."
    "A soft, rhythmic sigh of breath ghosted over the nape of your neck, sending an involuntary ripple across skin. You didn’t need to turn around. You knew."
    "Lily."
    "You shifted, just an inch caused the duvet to slip, and a slender, pale arm came into view, draped possessively over you waist."
    $ lily.draw_person(position = "kissing")
    "Slowly, carefully, you turned around. The arm around you tightened instinctively, a sleepy murmur escaping her lips."
    "[lily.possessive_title!c] curled into a comma, her hair a messy halo across your pillow. Her face, smooth and free of the day’s worries, was so close you could count the faint, almost invisible freckles dusting the bridge of her nose."
    "She's wearing a very sexy lingerie, probably attempting to seduced you before finding you already asleep the night before."
    mc.name "Lily~"
    "She stirred again, her nose wrinkling adorably. The arm around your waist slid, her hand splaying flat against the small of your back, pulling you closer."
    "Your dick grew. This was no longer just a sleepy cuddle. This was... something else."
    "Her eyes opened."
    "Not all at once, but slowly, drowsily. Blinking away the remnants of a dream. Her light blue eyes focused on you, her gaze soft and unfocused."
    "A lazy, unconscious smile graced her lips."
    lily "Mornin~"
    "She mumbled, her voice thick with sleep. It was a comforting sound that wrapped around you, warm and familiar, yet it carried a new, unexpected weight."
    mc.name "Good morning beautiful... Did my bed seem more comfortable than yours?"
    "Her smile widened, becoming more mischievious. She didn’t remove her hand. If anything, her fingers pressed a little more firmly into your back."
    lily "Maybe. It smells like you."
    mc.name "And what do I smell like?"
    "She closed her eyes for a second, as if actually considering it."
    lily "Like... clean laundry. And that gross protein powder you use. And... just you."
    "Her eyes opened again, and now they were clearer, more present, holding a glint of playful challenge."
    lily "It's not a bad smell."
    "You grinned."
    mc.name "Ok. A question then... be honest now... What's with the lingerie then?"
    lily "Well, you see, I was actually ... urm... you know..."
    mc.name "Yes...?"
    "Her cheeks reddens."
    lily "You bully! You know why..."

    menu:
        "Give her what she want":
            "You pulled her closer without answering directly."
            "Her hand, the one that had been a casual weight on your back, begins to move."
            "Lower and lower until she finds her target. She shift her gaze to your face."
            "You lifted your hip so she could pull your brief. Your dick stands to attention proudly."
            $ lily.change_arousal(15)
            $ mc.change_locked_clarity(10)
            call fuck_person(lily, private = True, start_position = blowjob, skip_intro = True) from _call_fuck_sis_KHH0
            $ the_report = _return
            $ lily.draw_person(position = "stand4", emotion = "happy")
            lily "Well, I'm going back to my room."
            $ clear_scene()
        "Reject her":
            mc.name "It's late!"
            lily "Fine! Jerk!"
            $ lily.draw_person(position = "walking_away")
            $ lily.change_stats(happiness = -20, love = -10)
            "She stormed out of your room."
            $ clear_scene()

    $ mc.location.turn_lights_on()
    return