#Counter = KQOL01

#QoL contains every tweaks that directly involves the gameplay. Most likely things that got tweaked for annoying me.
#Credits to afterd4rk and SAMarcus over at LR2 discord with his inputs

#Using Silence's code
init 0 python:
    #Add titles for the girl
    def get_titles_ext(org_func):
        def get_titles_wrapper(person):
            list_of_titles = org_func(person)

            #If mom loves/likes incest, she allows you to call her by her name
            if person.has_role(mother_role) and (person.get_opinion_score("incest") > 0) and (person.love > 99): #very SPECIFIC .. Only at 100 love!
                    list_of_titles.append("Jen")
                    list_of_titles.append("Jenny")
                    list_of_titles.append(person.name)
            
            #If she loves you
            if person.love > 90:
                list_of_titles.append("Babe")
                list_of_titles.append("Dear")
                if person.sluttiness > 80:
                    list_of_titles.append("Sexy")
                if person.get_opinion_score("taking control") > 0 and (person.get_opinion_score("being submissive") < 0):   
                    list_of_titles.append("Queen")

            #If you have child together 
            if (person.has_child_with_mc or (person.knows_pregnant and person.is_mc_father)):
                list_of_titles.append("Mommy")
                list_of_titles.append("Mama")

            #If she has an anal fetish
            if person.has_anal_fetish:
                if person.love > 50:
                    if person.body_is_average:
                        list_of_titles.append("Sexy Ass")
                        list_of_titles.append("Sexy Butt")
                    elif person.body_is_thin:
                        list_of_titles.append("Cute Butt")
                    else:
                        list_of_titles.append("Big Butt")
                        list_of_titles.append("Fat Ass")
            return list(set(list_of_titles))
        return get_titles_wrapper
    Person.get_titles = get_titles_ext(Person.get_titles)
    
    #Add possessive titles
    def get_possessive_titles_ext(og_func):
        def get_possessive_titles_wrapper(person):
            list_of_titles = og_func(person)

            #If she loves you
            if person.love > 90:
                #if she bears your child and hates cheating
                if ((person.has_child_with_mc or (person.knows_pregnant and person.is_mc_father)) and (person.get_opinion_score("cheating on men") <= -2)):
                    if person.has_role(mother_role):
                        list_of_titles.append("your momwife")
                    elif person.has_role(sister_role):
                        list_of_titles.append("your siswife")
                    elif person.has_role(aunt_role):
                        list_of_titles.append("your auntwife")
                    elif person.has_role(cousin_role):
                        list_of_titles.append("your cuzwife")
                    else:
                        list_of_titles.append("your couple")
                        list_of_titles.append("your significant other")                     
            #If she is slutty
            if person.sluttiness > 50:
                if person.has_role(mother_role):
                    list_of_titles.append("your slutty mom")
                    list_of_titles.append("your slutty mother")
                    list_of_titles.append("your mommy")
                elif person.has_role(sister_role):
                    list_of_titles.append("your slutty sister")
                elif person.has_role(aunt_role):
                    list_of_titles.append("your slutty aunt")
                elif person.has_role(cousin_role):
                    list_of_titles.append("your slutty cousin")

            if person.sluttiness > 60:
                if affair_role in person.special_role and (person.get_opinion_score("skimpy outfits") > 0):
                    list_of_titles.append("your sexy lover")
                    list_of_titles.append("your seductive lover")
                elif person.has_role(girlfriend_role) and (person.get_opinion_score("skimpy outfits") > 0):   
                    list_of_titles.append("your sexy girlfriend") 
                elif person.has_role(mother_role) and (person.get_opinion_score("skimpy outfits") > 0):   
                    list_of_titles.append("your sexy mother") 
                elif person.has_role(sister_role) and (person.get_opinion_score("skimpy outfits") > 0):   
                    list_of_titles.append("your sexy sister")
                elif person.has_role(aunt_role) and (person.get_opinion_score("skimpy outfits") > 0):   
                    list_of_titles.append("your sexy aunt")
                elif person.has_role(cousin_role) and (person.get_opinion_score("skimpy outfits") > 0):   
                    list_of_titles.append("your sexy cousin")
                elif person.has_role(girlfriend_role) and (person.get_opinion_score("lingerie") > 0):   
                    list_of_titles.append("your seductive girlfriend") 
                elif person.has_role(mother_role) and (person.get_opinion_score("lingerie") > 0):   
                    list_of_titles.append("your seductive mother") 
                elif person.has_role(sister_role) and (person.get_opinion_score("lingerie") > 0):   
                    list_of_titles.append("your seductive sister")
                elif person.has_role(aunt_role) and (person.get_opinion_score("lingerie") > 0):   
                    list_of_titles.append("your seductive aunt")
                elif person.has_role(cousin_role) and (person.get_opinion_score("lingerie") > 0):   
                    list_of_titles.append("your seductive cousin")
                elif person.get_opinion_score("taking control") > 0:   
                    list_of_titles.append("your dom queen")

            return list(set(list_of_titles))
        return get_possessive_titles_wrapper
    Person.get_possessive_titles = get_possessive_titles_ext(Person.get_possessive_titles)

    #Add titles for player
    def get_player_titles_ext(og_func):
        def wrapper(person):
            list_of_titles = og_func(person)

            #If she loves you
            if person.love > 90:
                list_of_titles.append("Dear")
                if (person.sluttiness > 80) and (person.get_opinion_score("big dicks") > 0):
                    list_of_titles.append("Big Dick")
                if person.has_role(aunt_role) and person.progress.lust_step >= 3:
                    list_of_titles.append("Tiger")

            #If you have child together 
            if (person.has_child_with_mc or (person.knows_pregnant and person.is_mc_father)):
                list_of_titles.append("Daddy")

            #If she hates you 
            if person.love < 0:
                list_of_titles.append("Bastard")
                list_of_titles.append("Jerk")
                list_of_titles.append("Dick")

            return list(set(list_of_titles))
        return wrapper
    Person.get_player_titles = get_player_titles_ext(Person.get_player_titles)

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["mc_spend_the_night_label"] = "mc_spend_the_night_revamp_label"
    config.label_overrides["mc_stop_follow_label"] = "tweaked_mc_stop_follow_label"
    config.label_overrides["bc_demand_label"] = "tweaked_bc_demand_label"
    config.label_overrides["pregnant_finish"] = "tweaked_pregnant_finish"
    config.label_overrides["silent_pregnant_finish"] = "tweaked_silent_pregnant_finish"
    config.label_overrides["girlfriend_unplanned_sleepover_label"] = "tweaked_girlfriend_unplanned_sleepover_label"


label mc_spend_the_night_revamp_label(person): # hijacking.. if the girls have not broken their pusssy taboo.. Keep it the same as before. For mom/sis, they would gladly go to your room.

    $ no_luck = False

    if the_person == lily and aunt_living_with_mc():
        the_person "Yeah... Gab would surely appreciate you in the room tonight."
        the_person "Now shoo... Before her big butt returns from her shower."
        $ mc.change_location(hall)
        return
    elif the_person.has_taboo("vaginal_sex") or mc.energy < 80 or person.energy < 40:
        #This is cheat assumption.. Because I'm lazy to write every possible scenario. Maybe later.
        $ the_person.draw_person(position = "back_peek")
        the_person "Sure, my bed is big enough for both of us."
        "She scoots over to give room until you lay down next to her."
        "As you get comfortable on your side of her bed, she shifted her body."
        $ the_person.draw_person(position = "kissing")
        "[the_person.possessive_title!c] breathing started to slow, but her fingers never stopped tracing shapes into your chest."
        "You rolled into her and pulled her into your chest with your arm under her head."
        "She murmured something unintelligible, then wrapped her own arms around your middle and pulled herself close, pressing her forehead into your shoulder."
        "She lightly dragging her nails up and down your back, but that only made you wrap her up tighter. She pressed a kiss to your chest, then said,"
        the_person "Goodnight [the_person.mc_title]."
        "You ran your fingers through her hair, massaging her scalp, and she melted into your chest with a shiver."
        mc.name "Goodnight [the_person.title]."
        $ the_person.change_stats(happiness = 5, love = 3, slut = 1, max_slut = 60, max_love = 80)
        "You spend the night in the comfort of [person.possessive_title]'s warm embrace."
        #$ sleep_outfit = the_person.outfit
    else:
        if the_person in people_in_mc_home():
            if not (had_family_threesome() or home_harem()):
                "You sneaked into [the_person.possessive_title]'s room."
                $ the_person.draw_person(position = "back_peek")
                if the_person.has_role(sister_role):
                    $ random_reply = get_random_from_list(["Pervert...", "If Mom caught us, {i}you{/i} are getting kicked out of the house..", "Your bed isn't warm enough?"])
                else:
                    $ random_reply = get_random_from_list(["Quiet...Lily could hear us!", "Ready to sleep with Mommy?", "No one must know of this."])
            else:
                "You decided to sleep with [the_person.possessive_title]."
                $ the_person.draw_person(position = "back_peek")
                if the_person.has_role(sister_role):
                    $ random_reply = get_random_from_list(["Mom kicked you out of her room? *grins*", "Oh, it's my turn tonight. Right... Gimme a sec... And done!", "Missed your sister's warm embrace?"])
                else:
                    $ random_reply = get_random_from_list(["Oh, I thought it's Lily's turn tonight.", "Ready to sleep with Mommy?", "Maybe we should consider a bigger bed for all three of us."])
            the_person "[random_reply]"
            call fuck_person(the_person, start_position = kissing, private = True) from _call_fuck_person_spend_the_night_KQOL02
            $ the_person.call_dialogue("sex_review", the_report = _return)
            call check_date_trance(the_person) from _call_check_date_trance_spend_the_night_KQOL02
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title!c] snuggles closer to you, allowing you to wrap your arms around her sexy body."
            if the_person.has_large_tits:
                "Your hands playfully land on her [the_person.tits_description]."
                $ the_person.draw_person( position = "back_peek", emotion = "happy")
            the_person "Goodnight [the_person.mc_title]."
            mc.name "Goodnight [the_person.title]."
            $ the_person.change_stats(happiness = 5, love = 3, slut = 1, max_slut = 60, max_love = 80)
            #$ sleep_outfit = the_person.outfit
        else:
            if affair_role in the_person.special_role:
                "You thought of spending quality time with [person.possessive_title] at her home."
                mc.name "Kinda missed you, [person.title]."
                the_person "You shouldn't be here. My [person.so_title] could return any moment now."
                "As if by cue, a car pulls in and turns its engine off."
                mc.name "Is that..."
                the_person "My [the_person.so_title]! Oh my god, quick, use the back door!"
                $ no_luck = True
            elif (not (the_person.relationship == "Single")) and the_person.opinion.cheating_on_men > 0:
                "You thought of spending quality time with [person.possessive_title] at her home."
                mc.name "Kinda missed you, [person.title]."
                the_person "Missed you too [person.mc_title]. My [person.so_title] won't appreciate sleeping on the couch while we locked the bedroom door. Not to mention, mad too."
                mc.name "Ah okay. See you tomorrow then."
                the_person "Love you."
                $ no_luck = True
            elif (not (the_person.relationship == "Single")) and the_person.opinion.cheating_on_men < 0:
                "You thought of spending quality time with [person.possessive_title] at her home."
                mc.name "Kinda missed you, [person.title]."
                the_person "You idiot! Did you forget I have a [person.so_title]?"
                the_person "Get out!"
                $ no_luck = True
            else:
                "You decided to spend the night with [person.possessive_title] at her home."
                mc.name "Webflix and chill?"
                the_person "With you? Always."
                "..."
                "She let out a squeak when you suddenly pulled her to your chest, kissing her hard enough before she could throw her arms around your neck."
                the_person "Bedroom?"
                "You scooped her up and she squealed again with delight while you carried her."
                $ the_person.change_to_bedroom()
                $ the_person.draw_person(position = "missionary")
                $ random_reply = get_random_from_list(["Alright, sexy time now.", "Come on tiger~", "Ravage me!", "Your lips look lonely. Would they like to meet mine?", "Let's fuck~"])
                the_person "[random_reply]"
                call fuck_person(the_person, private = True) from _call_fuck_person_spend_the_night_KQOL03
                $ the_person.call_dialogue("sex_review", the_report = _return)
                call check_date_trance(the_person) from _call_check_date_trance_spend_the_night_KQOL03
                $ the_person.draw_person(position = "kissing")
                "[the_person.possessive_title!c] snugs closer to you."
                if the_person.has_large_tits:
                    "Her [the_person.tits_description] feels so nice on your bare chest."
                the_person "Goodnight [the_person.mc_title]."            
                mc.name "Goodnight [the_person.title]."
                $ the_person.change_stats(happiness = 5, love = 3, slut = 1, max_slut = 60, max_love = 80)
                $ sleep_outfit = the_person.outfit
    
    $ sleep_outfit = the_person.outfit
    if day % 7 == 4 or no_luck: #its Friday night. We need to make sure Saturday wage event are not blocked.
        if no_luck:
            "Dissappointed, you simply go back home. It seems like you'll be sleeping alone tonight."
        else:
            if the_person in people_in_mc_home(): #With lily or mom                
                "You wake up in the middle of the night and went to the bathroom. You absentmindedly went back to your own room afterward."
            else:
                "You wake up earlier then usual. After kissing [the_person.possessive_title] goodbye, you went back home."
        $ mc.change_location(bedroom)
        $ clear_scene()        
        call advance_time() from _call_advance_time_spend_the_night_KQOL01
    else:
        #"Not Friday night."
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_spend_the_night_KQOL02          
        if the_person.energy < the_person.max_energy:
            $ the_person.energy = the_person.max_energy
        $ the_person.apply_outfit(sleep_outfit)
        if the_person.has_taboo("vaginal_sex"):
            #$ the_person.apply_outfit(sleep_outfit)
            $ the_person.draw_person(position = "walking_away")
            "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
            "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
            $ mc.change_locked_clarity(50)
            if the_person.has_large_tits:
                "Your hands cup and squeeze one of her [the_person.tits_description]. It's so full and hot, it feels so good in your hands."
            else:
                "Your hand cups one of her [the_person.tits_description]. It's so soft and warm, it feels good in your hand."
            "You still haven't gone all the way with [the_person.title]... It will be a dick move to continue."
            "You get up and head for the bathroom to take a leak."
            "When you come back, [the_person.title] is awake."
            $ the_person.draw_person(position = "missionary", emotion = "happy")
            the_person "Morning already?"
            mc.name "Not yet, the sun’s barely up."
            $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
            $ the_person.apply_planned_outfit(show_dress_sequence = True)
            $ the_person.draw_person(position = "stand3")
            "You both get ready for the day before heading out."
        else:    
            #She just wakes up, full of energy            
            #if the_person.energy < the_person.max_energy:
            #    $ the_person.energy = the_person.max_energy
            #$ the_person.apply_outfit(sleep_outfit)
            if renpy.random.randint(0, 2) == 1:
                call girlfriend_wakeup_spooning_label(the_person) from _call_spend_the_night_KQOL01
            elif renpy.random.randint(0, 2) == 2:
                call girlfriend_wakeup_cowgirl_label(the_person) from _call_spend_the_night_KQOL02
            
    return

label tweaked_mc_stop_follow_label(person):
    python:
        if the_person.get_destination() is the_person.home:
            schedule_destination = "my room"
        elif the_person.get_destination():
            schedule_destination = f"the {the_person.get_destination().formal_name}"
        else:
            schedule_destination = "somewhere else"

    "You tell [person.title] to stop following you around."
    if the_person.opinion.kissing < 0: #She hates kissing
        "She steps close and gives you a quick hug, then steps back."
    else:        
        if the_person.is_family: #mom,sis,aunt,cuz      
            if the_person.has_broken_taboo("vaginal_sex") and mc.location.person_count == 1: # they might have fucked you, but its a family secret! sadly is_private considers room, not peoples in it.
                $ the_person.draw_person(position = "kissing", emotion = "happy")
                "She steps in close and kisses you. Her lips are soft and warm against yours."
                "After a brief second she steps back and smiles."
            else:
                $ the_person.draw_person(position = "stand2")
                "She steps close and gives you a quick hug, then steps back."
        elif the_person.has_role(girlfriend_role) or (the_person.has_role(affair_role) and mc.location.is_private):
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "She steps in close and kisses you. Her lips are soft and warm against yours."
            "After a brief second she steps back and smiles."
        else:
            $ the_person.draw_person(position = "stand2")
            "She steps close and gives you a quick hug, then steps back."
    the_person "See you later then."

    $ the_person.follow_mc = False

    $ the_person.draw_person(position = "walking_away")

    $ the_person.run_move() # This will trigger stat changes based on clothing, but shouldn't be problematic although it can be exploited.

    the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."


    return

label tweaked_bc_demand_label(the_person):
    # Contains the obedience based approach to asking someone to stop taking birth control.
    # This event can have a moderately low Obedience requirement, with higher requirements to actually make changes.
    mc.name "Tell me about your birth control."
    if the_person.event_triggers_dict.get("is_changing_birth_control", False):
        the_person "We already discussed this, so let's talk about something else."
        return

    $ the_person.update_birth_control_knowledge()

    if the_person.fertility_percent < 0:
        the_person "I have an IUD, so there is nothing to worry about."
        mc.name "That's good to know, thanks you for letting me know."
        return

    if the_person.on_birth_control:
        the_person "I'm taking birth control right now."
    else:
        the_person "I'm... not taking any right now."

    menu:
        "Start taking birth control" if not the_person.on_birth_control and the_person.obedience >= 130 and the_person.has_event_delay("changed_bc", 7):
            mc.name "I want you to start taking some. I don't want you getting pregnant."
            if the_person in (kaya, sakari):
                the_person "I'm sorry, that's against everything we believe in, so I can't do that."
            elif the_person.event_triggers_dict.get("refuse_bc", False):
                "She shakes her head."
                the_person "I'm sorry, but I have personal reason for not going on birth control. Please don't ask me to do that."
            elif the_person.has_breeding_fetish:
                #breeding fetish dialogue
                "She shakes her head."
                the_person "I'm sorry, but I do want to be pregnant. It's very satisfying to be knocked up. Over... and over again."
                "She rubs her belly mindlessly."
            elif the_person.baby_desire > 60:
                #want babies
                "She smiles while gently grabbing your hands."
                the_person "It's fine, [the_person.mc_title]. I want to get pregnant with your baby."
            else:
                "[the_person.possessive_title!c] nods."
                the_person "Okay, I can do that. I'll talk to my doctor, I think I'll be able to start taking them tomorrow."
                mc.name "Good."
                $ manage_bc(the_person, start = True)

        "Start taking birth control\n{menu_red}Requires: 130 Obedience{/menu_red} (disabled)" if not the_person.on_birth_control and the_person.obedience < 130 and the_person.has_event_delay("changed_bc", 7):
            pass

        "Stop taking birth control" if the_person.on_birth_control and the_person.obedience >= 160 and the_person.has_event_delay("changed_bc", 7):
            mc.name "I want you to stop taking it."
            $ complains_threshold = 45 - (15 * the_person.opinion.creampies)
            if the_person.event_triggers_dict.get("mandate_bc", False):
                "She shakes her head."
                if the_person == mom:
                    the_person "I'm sorry, but I can't go off birth control."
                    the_person "Things have gotten intimate between me and my boss, but I don't want him to get me pregnant!"
                    the_person "I can't go off birth control right now. Okay?"
                else:
                    the_person "I'm sorry, but I have personal reason for being on birth control. Please don't ask me to do that."
            elif the_person.effective_sluttiness() >= complains_threshold:
                # She's slutty enough that it's not even a concern.
                "[the_person.possessive_title!c] nods obediently."
                the_person "Okay, I'll stop right away, but I already took one this morning."
            elif the_person.is_family:
                "[the_person.possessive_title!c] shuffles nervously before working up the nerve to speak back."
                the_person "[the_person.mc_title], I can't do that. If you got me pregnant I... I don't know what I would do!"
                mc.name "I didn't say I was going to get you pregnant. I just told you to stop taking your birth control."
                mc.name "I'm sure you can avoid getting knocked up if you really put your mind to it. Now, do we have a problem?"
                "[the_person.title] starts to say something, then thinks better of it. She shakes her head."
                the_person "No, there's no problem. I won't take any birth control in the morning."

            else:
                "[the_person.possessive_title!c] shuffles nervously before working up the nerve to speak back."
                the_person "I... I don't know if that's a good idea. I don't know if I want to get pregnant."
                mc.name "I didn't ask if you wanted to get pregnant. I told you to stop taking your birth control. Is there a problem with that?"
                "She blushes and looks away under your glare."
                the_person "No. I'll stop right away. Sorry, but I already took one this morning."

            $ manage_bc(the_person, start = False)

        "Stop taking birth control\n{menu_red}Requires: 160 Obedience{/menu_red} (disabled)" if  the_person.on_birth_control and the_person.obedience < 160 and the_person.has_event_delay("changed_bc", 7):
            pass

        "That's all I wanted to know":
            mc.name "Good. That's all I wanted to know."
    return

label tweaked_pregnant_finish(the_person):
    $ done = pregnant_finish_person(the_person)
    if not done:
        return

    $ play_ring_sound()
    "You get a call from [the_person.possessive_title] early in the morning. You answer it."
    if the_person in (aunt, mom):
        if the_person.number_of_children_with_mc == 1:
            the_person "Hey [the_person.mc_title], good news! I gave birth to our first daughter two days ago!"
        elif the_person.number_of_children_with_mc > 1:
            the_person "Hey [the_person.mc_title]! We got another daughter! She's pretty like all her sisters!"
        else:
            if the_person == mom:
                the_person "Hey [the_person.mc_title], good news! You got a new sister!"
            else:
                the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, where is she now?"
        if the_person == mom:
            the_person "I'll be leaving her with my mother—your grandmother—for now, so I'll be home soon."
            the_person "I just wanted to let you know. Tell Lily I love her too."
        else:
            the_person "I've contacted my mother-your grandmother, and she agreed to babysit her."
            the_person "I don't really trust Gabriel to babysit."
            the_person "I just wanted to let you know. Later, 'kay."
        "You say goodbye and [the_person.possessive_title] hangs up."
    
        if not the_person.has_breeding_fetish:
            $ the_person.change_baby_desire(-the_person._baby_desire)
            $ amount = the_person.kids * 20
            $ the_person.change_baby_desire(-amount)
        return

    elif the_person in (lily, cousin):
        if the_person.number_of_children_with_mc == 1:
            the_person "Hey [the_person.mc_title], good news! I gave birth to our first daughter two days ago!"
        elif the_person.number_of_children_with_mc > 1:
            the_person "Hey [the_person.mc_title], good news! Two days ago I gave birth to our daughter!"
        else:
            the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, where is she now?"
        if the_person == lily:
            the_person "I'll be leaving her with our grandma for now, so I'll be home soon."
            the_person "I just wanted to let you know. Say hi to Mom for me."
        else:
            the_person "I'll be leaving her with our grandma for now, so we can continue seeing each other."
            the_person "I just wanted to let you know. Urm. Later."
        "You say goodbye and [the_person.possessive_title] hangs up."
    
        if not the_person.has_breeding_fetish:
            $ the_person.change_baby_desire(-the_person._baby_desire)
            $ amount = the_person.kids * 20
            $ the_person.change_baby_desire(-amount)
        return

    if the_person.is_employee:
        if mc.business.is_weekend:    # event triggers at start of day (so on sat or sun, next workday is monday)
            the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl! I'll be coming back to work Monday." #Obviously they're all girls for extra fun in 18 years.
        else:
            the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl! I'll be coming back to work today." #Obviously they're all girls for extra fun in 18 years.
        #TODO: Let you pick a name (or at low obedience she's already picked one)
        mc.name "That's amazing, but are you sure you don't need more rest?"
    else:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, how are you doing?"


    if the_person.is_affair:
        the_person "I'll be fine, I'll be leaving our girl with her \"father\" so I can come back and see you again."
    else:
        the_person "I'll be fine. I'm leaving her with my mother for a little while so I can get back to a normal life."

    the_person "I just wanted to let you know. I'll talk to you soon."
    "You say goodbye and [the_person.possessive_title] hangs up."
    
    if not the_person.has_breeding_fetish:
        $ the_person.change_baby_desire(-the_person._baby_desire)
        $ amount = the_person.kids * 20
        $ the_person.change_baby_desire(-amount)
        
    return

label tweaked_silent_pregnant_finish(the_person):
    $ pregnant_finish_person(the_person)
    if the_person.is_stranger:
        return  # unknown girls should not about the delivery

    $ play_ring_sound()
    "You get a call from [the_person.possessive_title] early in the morning. You answer it."
    if the_person in (aunt, mom):
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, where is she now?"
        the_person "I'll be leaving her with my mother—your grandmother—for now."

    elif the_person in (lily, cousin):
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, where is she now?"
        the_person "I'll be leaving her with our grandma for now, so I can get back to a normal life."

    elif employee_role in the_person.special_role:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl! I'll be coming back to work today." #Obviously they're all girls for extra fun in 18 years.
        mc.name "That's amazing, but are you sure you don't need more rest?"
        if the_person.has_significant_other:
            the_person "I'll be fine, I'll be leaving her with my [the_person.so_title], so I can come back to work sooner."
        else:
            the_person "I'll be fine. I'm leaving her with my mother for a little while so I can get back to a normal life."

    else:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, how are you doing?"
        if the_person.has_significant_other:
            the_person "I'll be fine, I'll be leaving her with my [the_person.so_title]."
        else:
            the_person "I'll be fine. I'm leaving her with my mother for a little while so I can get back to a normal life."

    the_person "I just wanted to let you know. I'll talk to you soon."
    "You say goodbye and [the_person.possessive_title] hangs up."
    if not the_person.has_breeding_fetish:
        #reset to 0 after giving birth
        $ the_person.change_baby_desire(-the_person.baby_desire)
        #she is more reluctant with more kids if she already have some
        $ the_person.change_baby_desire(-the_person.kids * 20)
    return

label tweaked_girlfriend_unplanned_sleepover_label(the_person):
    if the_person in people_in_mc_home():
        the_person "You surprised me... I'm just about going to bed."
        mc.name "I know, I was thinking of sleeping with you tonight."
        mc.name "You know, like what every other boyfriend and girlfriend do."
        if the_person.has_role(sister_role):
            the_person "Awww.. How sweet. Mom asleep, right? What do you have planned?"
        else:
            the_person "Sleeping together? That would be nice. I hope Lily won't catch us. What do you have planned?"
        menu:
            "Plan to have sex":
                mc.name "Oh, just wanted to spend some quality time with you, maybe watch a movie or two... and then fuck your brains out."
                "You wink at her playfully."
                if the_person.has_role(sister_role):
                    "She grins."
                    the_person "Such a perverted idea. Luckily, this [the_person.possessive_title] is totally welcoming the idea of getting fucked... hard."
                    "Her cheeks reddens."
                else:
                    "She gave a playful slap on your arm."
                    the_person "Watch your language, young man! But, well... I hoped Lily won't hear my screams..."
                    "Her cheeks reddens."
                "As you settle in on her bed, you consider if the night would be improved with a serum."
                menu:
                    "Get wine mixed with a dose of serum" if mc.inventory.has_serum:
                        call give_serum(the_person) from _call_give_serum_girlfriend_unplanned_sleepover_KQOL02
                        "Deciding you should you step out to grab some wine and mix in the serum."
                    "Get wine mixed with a dose of serum\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                        pass
                    "Just get some wine":
                        "Deciding to just get some wine you step out to the kitchen and pick out a bottle."
                $ the_person.change_to_bedroom()
                $ the_person.draw_person(position = "sitting")
                "You walk down to her bedroom and hand her the wine glass. She takes a long sip."
                $ the_person.call_dialogue("sleepover_herplace_sex_start")
                call fuck_person_all_night(the_person, private = True) from _call_fuck_person_unplanned_sleepover_gf_KQOL02
            "Plan to just spend the night":
                mc.name "Oh, just wanted to spend some quality time with you, just you and me chatting."
                if the_person.has_role(sister_role):
                    "She grins."
                    the_person "Niiice. You can help me with my homeworks then."
                    mc.name "Wait, what? Oh well, sure."
                    the_person "You are THE BEST! Just let me change into my comfiest clothes."
                else:
                    the_person "I like that."
                    the_person "Sometimes we all need someone to talk to. You can always talk to me, you know that."
                    "She pats the side of the bed next to her."
                    the_person "Alright then! Just let me change into my comfiest clothes."
                $ the_person.change_stats(happiness = 5, love = 3)
                call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_unplanned_sleepover_KQOL02
                call girlfriend_wakeup_label(the_person) from _call_girlfriend_wakeup_girlfriend_unplanned_sleepover_KQOL02
    else:   
        mc.name "I was thinking about staying over tonight."
        the_person "Really? That would be nice. What do you have planned?"
        menu:
            "Plan to have sex":
                mc.name "Oh, just wanted to spend some quality time with you, maybe watch a movie or two... and then fuck your brains out."
                "You wink at her playfully."
                the_person "Well, I wouldn't mind that at all! Just remember to bring your A-game because I plan on giving it right back to you"
                "As you settle in to watch a movie you consider if the night would be improved with a serum."
                menu:
                    "Get wine mixed with a dose of serum" if mc.inventory.has_serum:
                        call give_serum(the_person) from _call_give_serum_girlfriend_unplanned_sleepover_KQOL01
                        "Deciding you should you step out to grab some wine and mix in the serum."
                    "Get wine mixed with a dose of serum\n{menu_red}Requires: Serum{/menu_red} (disabled)" if not mc.inventory.has_serum:
                        pass
                    "Just get some wine":
                        "Deciding to just get some wine you step out to the kitchen and pick out a bottle."
                $ the_person.change_to_bedroom()
                $ the_person.draw_person(position = "sitting")
                "You walk down to her bedroom and hand her the wine glass. She takes a long sip."
                $ the_person.call_dialogue("sleepover_herplace_sex_start")
                call fuck_person_all_night(the_person, private = True) from _call_fuck_person_unplanned_sleepover_gf_KQOL01
            "Plan to just spend the night":
                mc.name "Oh, just wanted to spend some quality time with you, maybe watch a movie or two."
                the_person "That sounds perfect. We can order pizza and make it a cozy night in."
                mc.name "Yeah, that's what I had in mind."
                the_person "Alright then! Sounds like a plan. Just let me change into my comfiest clothes."
                $ the_person.change_stats(happiness = 5, love = 3)
                call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_unplanned_sleepover_KQOL01
                call girlfriend_wakeup_label(the_person) from _call_girlfriend_wakeup_girlfriend_unplanned_sleepover_KQOL01
    return
