#Counter = KSPE01
# This set of labels for personalize sis pregnancy


label lily_pregnant_announce(the_person):
    $ the_person.draw_person()
    $ the_person.knows_pregnant = True #Set here and in the larger tits, represents the person knowing they're pregnant so they don't ask for condoms ect.
    "[the_person.title] rushed over to you as soon as you enter her room." #ASSUMPTION. She always in her room when this triggers.
    mc.name "Hey, [the_person.title]? Everything okay?"
    if the_person.has_child_with_mc: # > 0:
        "She drags you to her bed and sits on your lap."
        "She wrapped her arms around your neck before tilting her head to you."
        the_person "We need to talk."        
    else:
        "She drags you to her bed and get you to sit next to her."
        "She pulled her knees to her chest, wrapping her arms around them. The defensive posture did nothing to hide the tremor in her hands."
        the_person "There’s something I need to tell you… something that’s going to change everything."
    mc.name "What is it?"

    if day - the_person.event_triggers_dict.get("preg_start_date", 0) > 30:
        return # If you don't ever check in with her for 30 days you probably don't care and we don't need to show this event.
        
    if the_person.event_triggers_dict.get("immaculate_conception", False):
        $ mc.change_locked_clarity(100)
        the_person "There's no easy way to explain this, so I'll just say it. I'm pregnant."
        the_person "I don't know how it could have even happened. Or even who the father was. I haven't had sex in so long!"
        the_person "It's not important now though, what is important is that I'm pregnant!"
    elif the_person.event_triggers_dict.get("preg_accident", False):
        $ mc.change_locked_clarity(100)
        "She holds out her hand with a pink test kit to you."
        the_person "It's positive."
        mc.name "What?"
        the_person "I know this is a lot to take in, but... it’s true."
        mc.name "How? We’ve always been careful. I mean, we’ve used protection every time."
        the_person "How? Are you seriously asking me that? After... after all the sex? We haven’t exactly been... careful."
        if not lily_want_baby(): #She doesn't want it.
            if the_person.has_child_with_mc: # == 0: #1st child
                the_person "We got another mouth to feed. The last one is barely walking."
                the_person "I don’t know... But I know that I can’t do this alone. I need you... more than ever."
                mc.name "I'm here... Whatever happens... I’m here."
                the_person "Thank you."
            else:
                the_person "I don’t know if I can do this."
                mc.name "Yes, you can. You’re stronger than you think. And I'll be here with you every step of the way. We’ll figure it out together."
                the_person "This is insane. You’re my brother. We... we can't do this. We can’t have a baby together. People will—"
                mc.name "People don’t have to know. It’s our secret. Ours alone. We can figure this out. We can make it work."
                mc.name "This is just... the next step. Trust me."
                the_person "Yeah."
        else: #shes fine having the baby
            if the_person.has_child_with_mc: # == 0: #1st child
                the_person "It’s not like this hasn’t happened before."
                the_person "We’ve been through this before, we’ll figure it out. Just like we did last time."
                mc.name "Yeah."
                the_person "But, really [the_person.title], you really have fetish getting your sister pregnant over and over!"
                the_person "Not that I'm against it anyway."
            else:
                mc.name "What are we going to do?"
                the_person "I don't know how to fix this. I don’t know if it can even be fixed."
                mc.name "Maybe... maybe we should tell someone. Someone who can help us."
                the_person "NO! We can’t tell anyone. You don’t understand what would happen if people found out. They’d take everything away from us. They’d destroy us."
                mc.name "But what other choice do we have? We can’t keep this secret forever."
                the_person "We have to... We have no other choice. We have to protect ourselves, and..."
                the_person "And the baby."
                mc.name "You can’t seriously be thinking about keeping it? This is insane."
                the_person "Do you think I planned for any of this to happen? But it did, and now we have to deal with it. We have to figure out what’s best for all of us."
                the_person "I know it's hard. And I know it's easier to just run away, to escape. But we can’t. We have to face this head-on, together."
                the_person "Say something... Please, just say something."
                "You opened your mouth, but no words came out. Instead, you simply pulled her into your arms."
                "[the_person.title] gasped in surprise, then melted into your embrace, her arms wrapping around your waist."
                mc.name "Together."
                the_person "Together."
    else:
        $ mc.change_locked_clarity(100)
        if not lily_want_baby(): #She doesn't want it.
            if the_person.has_child_with_mc: # == 0: #1st child
                the_person "I'm... I'm carrying your baby. Again."
                mc.name "Again?"
                the_person "Yes... You got me pregnant again."
                "She trailed off, her hands instinctively moving to her stomach, as if she could already feel the life growing inside her."
                "You took a step closer to her, your body moving on its own. "
                "You reached out, fingers brushing against her hand, and she shuddered at the touch."
                the_person "We’ve been… careless. We’ve been really really reckless. And you! You should be more responsible! You the older one!"
                "You smiled sheepishly."
                mc.name "I'm sorry... but you just feel so good."
                the_person "So what? It's my fault?"
                "She raised her eyes to yours directly."
                mc.name "No, nope. Mine. Totally mine."
                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                mc.name "You can be scary sometime... But I forgive you. Because you are pretty. Especially pregnant."
                "She hits your head."
                the_person "Sweet talker. You are hopeless, Big Bro."
            else:
                the_person "I'm... I'm carrying your baby."
                mc.name "What?"
                the_person "I'm... I'm carrying your baby."
                "She trailed off, her hands instinctively moving to her stomach, as if she could already feel the life growing inside her."
                "You took a step closer to her, your body moving on its own. "
                "You reached out, fingers brushing against her hand, and she shuddered at the touch."
                the_person "I don’t know if I can do this."
                mc.name "Yes, you can. You’re stronger than you think. And I'll be here with you every step of the way. We’ll figure it out together."
                the_person "This is insane. You’re my brother. This is not supposed to happened... We can’t have a baby together. People will—"
                mc.name "People don’t have to know. It’s our secret. Ours alone. We can figure this out. We can make it work."
                mc.name "This is just... the next step. Trust me."
        else: #shes fine having the baby
            if the_person.has_child_with_mc: # == 0: #1st child
                "She let out a small, almost breathless laugh, her cheeks flushing a faint pink."
                the_person "Sorry, I just… I didn’t know how to say this."
                "She took a deep breath, her hand resting lightly on her stomach—a gesture that made your heart skip a beat."
                the_person "I’m pregnant."
                mc.name "Holy shit, again?"
                "She laughed softly, her hand still resting on her stomach."
                the_person "I’m serious. I just found out this morning. I couldn’t wait to tell you."
                "She leaned in, her lips brushing softly against yours in a kiss that was both tender and hungry."
                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                mc.name "You’re so fucking beautiful...Carrying my baby again… it’s driving me crazy."
                the_person "I love it when you talk like that...It makes me feel so… wanted."
            else:
                the_person "I'm pregnant... with your child."
                mc.name "What?"
                the_person "I'm... I'm carrying your baby."
                "She trailed off, her hands instinctively moving to her stomach, as if she could already feel the life growing inside her."
                "You took a step closer to her, your body moving on its own. "
                "You reached out, fingers brushing against her hand, and she shuddered at the touch."
                mc.name "What do we do now?"
                the_person "I don't know... But we’re in this together. You know that, right? Whatever happens."
                the_person "Together."
    
    $ clear_scene()

    call evaluate_ovulation_perception_perk(the_person) from _call_evaluate_ovulation_perception_perk_pregnant_announce_KSPE01
    return

label lily_pregnant_tits_announce(start_day, the_person):
    if day - start_day >= 7:
        return #If it's been a week she doesn't comment on it.

    if the_person.effective_sluttiness() + (the_person.opinion.showing_her_tits*10) > 50: #She's happy to show off her new tits
        the_person "Hey [the_person.mc_title]. I was looking in the mirror this morning and I noticed something."
        "She cups her tits and jiggles them."
        $ mc.change_locked_clarity(50)
        if the_person.wants_creampie:
            the_person "My tits are starting to swell. It feels like my body is transforming into a sluttier version of me."
            the_person "Soon everyone is going to realize that I'm pregnant."
            the_person "I wonder what they'll think of me if they realize who the father is."
            "She looks at you teasingly."
        else:
            the_person "My tits are starting to swell up. I wonder how long it's going to be until people figure out I'm pregnant."
            mc.name "I think you've got a little longer before it's obvious. But for now... My favourite toys just gets a bit bigger ."
            "She smiles and lets her tits drop out of her hands. They bounce a few times before coming to a stop."

    else: #She's a little embarrassed about it
        the_person "Hey [the_person.mc_title], I have a question."
        mc.name "Okay, what is it?"
        the_person "Can you tell that my boobs are bigger? I think it did and I'm nervous people are going to figure out I'm pregnant."
        $ mc.change_locked_clarity(30)
        "She moves her arms and gives you a clear look at her chest. Her tits do look bigger than they were before."
        "You cups her tits and jiggles them."
        mc.name "They're definitely larger, I love it. I'm sure all the other girls will be jealous of your great rack."
        the_person "You think so? Thanks [the_person.mc_title]. I guessed if you love them, it's fine then."
        "She holds your hand still on her boobs."
        the_person "Just don't do this in front of everyone."

    call talk_person(the_person) from _call_talk_person_KSPE11
    return

label lily_pregnant_transform_announce(start_day, the_person):
    if day - start_day > 14: #If you haven't noticed in 2 weeks you probably just don't care. Skip the event.
        return

    $ the_person.draw_person()
    "[the_person.possessive_title!c] notices you and comes over to talk."

    if day - the_person.event_triggers_dict.get("preg_start_date", day)  <= 30:
        # Unusually short pregnancy.
        the_person "Hey [the_person.mc_title]. Tada~!"
        $ mc.change_locked_clarity(50)
        "She stand straight, fingers on hip, accentuating the new and prominent curves that have formed."
        the_person "My doctor tells me everything is fine, I'm just ahead of the curve. I think she just wanna see her Daddy faster."
        mc.name "She?"
        the_person "Yup."

    else:
        # Normal length pregnancy
        the_person "Hey [the_person.mc_title]. Do [the_person.possessive_title] look sexy?"
        $ mc.change_locked_clarity(50)
        "She turns and runs a hand over her belly, accentuating the new and prominent curves that have formed there."
        mc.name "You sure do, especially since you are mine."

    the_person "My boobs are starting to swell with milk too. It's a little embarrassing but..."
    the_person "Now when I get aroused they leak just a little bit."
    mc.name "You look fantastic. You really are glowing."
    $ the_person.change_happiness(10)
    "[the_person.possessive_title!c] smiles and holds your hand for a moment."
    the_person "Well, just wanna share this with you, I'm sure you were doing something important."
    return

label lily_pregnant_finish_announce(): #TODO: have more variants for girlfriend_role, affair_role, etc.
    # The girl tells you she'll need a few days to have the kid and recover, and she'll be back in a few days.
    $ the_person = lily
    $ play_ring_sound()
    "You get a call from [the_person.possessive_title]. You answer it."
    mc.name "Hey [the_person.title], what's up?"
    the_person "I'm at the hospital."
    mc.name "Hospital? Are you okay? I'm coming to you now."
    the_person "Relax. I saw my doctor yesterday and he tells me I'm going to pop any day now."
    the_person "I already admited to the ward."

    if day - the_person.event_triggers_dict.get("preg_start_date", day) <= 90: #It's unusually short
        the_person "It's earlier than I expected, but he tells me everything looks like it's perfectly normal."

    if the_person.is_employee:
        the_person "Anyway, I won't be able to go to work for a few days."
        mc.name "That should be the last thing you worry about. Do you need me to do anything?"
    else:
        the_person "Anyway, I won't be around at home for a few days. Don't miss your cute sister too much."
        mc.name "Do you need me to do anything?"

    if the_person.has_child_with_mc:
        the_person "No, I got this. Just relax, this is not our first kid. I'm pretty experienced in this, thanks to you~"
    else:
        the_person "No, it's fine. I've asked some tips from Mom, it should be fine."

    mc.name "Okay, I'll talk to you soon then."
    the_person "I'll let you know as soon as things are finished. Love you. Bye!"

    $ pregnant_finish_announce_person(the_person)
    return

label lily_pregnant_finish(the_person):
    $ done = pregnant_finish_person(the_person)
    if not done:
        return

    $ play_ring_sound()
    "You get a call from [the_person.possessive_title] early in the morning. You answer it."
    if the_person.number_of_children_with_mc == 1:
        the_person "Hey [the_person.mc_title], good news! I gave birth to our first daughter two days ago!"
    elif the_person.number_of_children_with_mc > 1:
        the_person "Hey [the_person.mc_title], good news! Two days ago I gave birth to our daughter!"
    else:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
    mc.name "That's amazing, where is she now?"
    the_person "I'll be home later this evening or tomorrow the latest. You'll be able to meet her yourself."
    the_person "I just wanted to let you know. Say hi to Mom for me."
    "You say goodbye and [the_person.possessive_title] hangs up."

    if not the_person.has_breeding_fetish:
        $ the_person.change_baby_desire(-the_person._baby_desire)
        $ amount = the_person.kids * 20
        $ the_person.change_baby_desire(-amount)
    return

label lily_tits_shrink_announcement_one(the_person):
    if the_person.is_pregnant:  # quick exit when she's pregnant again
        return
    the_person "Hey [the_person.mc_title]."
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title!c] sighs and looks down at her chest. She cups a boob and rubs it gently."
    the_person "It looks like my milk is starting to dry up. I'm going to miss having my tits that big..."
    if the_person.wants_creampie:
        $ mc.change_locked_clarity(50)
        if the_person.number_of_children_with_mc > 1:
            the_person "If you really wanted to keep them around you could always get me pregnant again."
            "She bites her lip and eyes your crotch, obviously fantasizing."
            "You jokingly covered your crotch."
            mc.name "Help! A pervert!"
            "She hits your chest playfully."
            the_person "And who made me one?"
        else:
            mc.name "I love you, big or small boobs notwithstanding, but we can always work toward getting it big again, [the_person.title]."

        $ the_person.change_arousal(10)
        "She nods and sighs happily."
    else:
        the_person "I won't miss milk soaking through all my clothing. That was a huge pain."
    call talk_person(the_person) from _call_talk_person_KSPE12
    return

label lily_tits_shrink_announcement_two(the_person):
    if the_person.is_pregnant:  # quick exit when she's pregnant again
        return

    the_person "Hey [the_person.mc_title]."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] sighs and looks down at her chest. She cups one of her boobs and rubs it gently."
    the_person "My chest is back to its old size. I had gotten so used to them when I was pregnant that these feel tiny now."
    if the_person.number_of_children_with_mc > 1:
        mc.name "That's a pretty easy problem to solve. I'll just have to get you pregnant again."
    else:
        mc.name "That's a pretty easy problem to solve. You would just have to get pregnant again."
    "She hits your chest playfully."
    if the_person.wants_creampie:
        $ the_person.change_arousal(10)
        $ play_moan_sound()
        "[the_person.title] moans and nods happily."
        $ mc.change_locked_clarity(30)
        if the_person.number_of_children_with_mc > 1:
            the_person "Son... no, Husband, when do we start~"
        else:
            the_person "Oh god yes, that would be amazing, getting filled up with all that cum again."
    else:
        the_person "That was a lot of work to go through just for some bigger tits. Maybe I'll get a boobjob though..."
    call talk_person(the_person) from _call_talk_person_KSPE13
    return

label lily_date_take_home_her_place(date_type = None): #Your date went well and you go back to her place. This event starts off when you enter the door.
    $ the_person = lily
    $ noisy_neighbor = False
    $ spend_the_night = False
    $ door_sex = False
    $ the_report = None

    $ downtown.show_background()
    $ the_person.change_location(downtown)
    $ mc.change_location(downtown)
    $ current_outfit = the_person.outfit #save this 
    the_person "[the_person.mc_title], we should really do this more often. Are you afraid to be seen out drinking at the bar with [the_person.possessive_title]?"
    mc.name "Why would I be afraid to be seen with a hot chick?"
    the_person "Heh, you should babysit me more... at the bar preferably. Hihihi."
    mc.name "You are drunk."
    the_person "Nooo, I. AM. NOT. DRUNK."
    the_person "Well, maybe a {i}teeny weeny{/i} bit. Hihihi."
    "As you approached the car, she hooked her arm through yours, attempting to steady her stride, her body near enough that you could feel the heat radiating from her."
    the_person "Don't tell Mom. She's going to nag me all week."
    mc.name "I won't. I'm not suicidal either."
    $ the_person.draw_person(position = "sitting")
    "The ride back was peaceful, the sound of the engine filling the quiet gaps between the two of you."
    "She falls asleep on your shoulder peacefully."
    "Before long, you find yourself having to wake her up, albeit reluctantly, since you have arrived."
    $ the_person.change_location(hall)
    $ mc.change_location(hall)
    $ the_person.draw_person(position = "stand2")

    #First, check and see if we just fuck her as soon as we walk in the door
    if her_place_door_fuck_check(the_person):
        if the_person.arousal_perc >= 70:   #She comes after MC eagerly
            "[the_person.title] has her hands all over you while leaning on you."
            the_person "It might be the drink, but I'm wet, [the_person.mc_title]."
            $ mc.change_locked_clarity(20)
            $ the_person.draw_person(position = "kissing")
            "She puts her arms around you and kisses your neck, grinding her body against you."
            if aunt_living_with_mc():
                mc.name "Don't you want to go to my bedroom first?"
                mc.name "Gabby will hate watching us fucking. And Becky in the living room..."
                the_person "Becky drinking with Mom. They probably wasted."
                mc.name "My bedroom then?"
            elif had_family_threesome() or home_harem():
                mc.name "Mom might caught us."
                the_person "Schedule. My night."
            else:
                mc.name "Mom might caught us."
                the_person "Fuck her. It's her bedtime."
            menu:
                "Fuck her against her front door":
                    "You return the kiss. A moment later [the_person.possessive_title] has her hand down your pants, fondling your cock."
                    the_person "Perverted Big Brother! Did you get hard from watching your innocent little sister?"
                    "You grab her ass and push her up against the wall, eliciting a moan from her as you begin to grind your body against hers."
                    mc.name "Innocent? When you this wet right now? I'm gonna make you scream all night long."
                    call date_take_home_her_place_fuck_against_door_label(the_person) from _front_door_sex_KSPE01
                    $ the_report = _return
                    $ noisy_neighbor = the_report.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex)
                    $ door_sex = True

                "Insist on the bedroom":
                    the_person "Come on, how do you want me?"
                    mc.name "Patient [the_person.title], I'm not going anywhere. I promised. Let's go inside, first."
                    "She steps back. An awkward silence hangs for a few moments before she nods shyly."

                "Turn her down":
                    $ the_person.draw_person()
                    "You push her back firmly. She seems confused and tries to kiss you again, but you don't let her."
                    mc.name "Not tonight, [the_person.title]. You need to get yourself under control."
                    the_person "What? Don't dissappoint your sister, please! I need this."
                    mc.name "I was thinking about it, but you're acting like the only thing you care about is getting at my cock!"
                    mc.name "Now I just want to head to my room. Maybe you'll calm down."
                    $ the_person.change_stats(happiness = -20, love = -(2 + the_person.opinion.taking_control))
                    if the_person.is_dominant:
                        the_person "If you felt like that why did you start flirting at the bar?"
                        the_person "Do you really intent to treat your own sister like a whore?"
                        "She scoffs and backs away from you."
                        the_person "Whatever, if that's how you feel then fine. My dildo is bigger then YOUR DICK!"
                        mc.name "Right. Have fun [the_person.title]."
                        "She stomped her feet angrily."

                    "[the_person.possessive_title!c] deflates like a balloon. She steps back."
                    the_person "I... I'm sorry [the_person.mc_title], I didn't know you felt like that."
                    "An awkward silence hangs for a few moments before you speak again."
                    mc.name "I'm going to my room. Have a good night."
                    "[the_person.title] watches you leave, then sulks back inside her own."
                    return "Advance Time"
        else:
            "She still leaning on your side. You can feel her [the_person.tits_description] fully pressed on your arm."
            "Your libido spikes. You wonder how she would react if you just took her right here, up against her front door."
            menu:
                "Fuck right here":
                    "You gently tug her cheek to direct her gaze at you. She stretches her arms out and encircles your neck while you lean in to make out."
                    $ mc.change_locked_clarity(20)
                    $ the_person.draw_person(position = "kissing")
                    "You shove her body against the wall as you both eagerly exchange kisses. She lets out soft sounds into your mouth while you press your body against hers."
                    $ the_person.change_arousal(10)
                    call lily_date_fuck_against_door_label(the_person) from _front_door_sex_KSPE02
                    $ the_report = _return
                    $ noisy_neighbor = the_report.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex)
                    $ door_sex = True
                "Wait for her to continue":
                    "You decides against it and waits patiently for her to enter."
                    $ finish_type = her_place_get_finish_type(the_person)
                    #The next 4 sequences return True of if there is a possibility of spending the night, otherwise False
                    if finish_type == "TV":
                        call lily_date_tv_finish_label(the_person) from _date_her_place_TV_finish_KSPE02
                        $ spend_the_night = _return
                    elif finish_type == "Slut":
                        call lily_date_lingerie_finish_label(the_person) from _date_her_place_lingerie_finish_KSPE02
                        $ spend_the_night = _return
                    elif finish_type == "Obedience":
                        call lily_date_service_offer_label(the_person) from _date_her_place_service_offer_finish_KSPE02
                        $ spend_the_night = _return
                    else:
                        call lily_date_romance_finish_label(the_person) from _date_her_place_romance_finish_KSPE02
                        $ spend_the_night = _return

    # Fuck in the hallway, or atleast present it as an option
    if door_sex:
        $ spend_the_night = her_place_spend_the_night_check(the_person, the_report)
        "You gather your clothes off the floor."
        the_person "That was good, but you really wore me out."
        "She worked to approach you, but her quivering legs made her lose her balance."        

        #Next, determine if we interact with anyone else as we enter.
        if noisy_neighbor: #There are other people in the apartment and you made a lot of noise.
            call lily_date_meet_mom_label(the_person) from _noisy_sex_at_front_door_KSPE01
 
    else:
        # Next, decide what one night stand action we are going to take.
        # If the girl has lower scores, she may suggest a relatively innocent 'netflix and chill'
        # At higher obedience, she may offer to service MC
        # At higher love score, offer the chance to make out, then take things to the bedroom.
        # At high slut score, she changes into lingerie to seduce MC.
        $ finish_type = her_place_get_finish_type(the_person)
        #The next 4 sequences return True of if there is a possibility of spending the night, otherwise False
        if finish_type == "TV":
            call lily_date_tv_finish_label(the_person) from _date_her_place_TV_finish_KSPE01
            $ spend_the_night = _return
        elif finish_type == "Slut":
            call lily_date_lingerie_finish_label(the_person) from _date_her_place_lingerie_finish_KSPE01
            $ spend_the_night = _return
        elif finish_type == "Obedience":
            call lily_date_service_offer_label(the_person) from _date_her_place_service_offer_finish_KSPE01
            $ spend_the_night = _return
        else:
            call lily_date_romance_finish_label(the_person) from _date_her_place_romance_finish_KSPE01
            $ spend_the_night = _return

    if spend_the_night:
        if noisy_neighbor:                   
            "She groggily tried to stay standing."
            "You quickly grab her arm and lead her to your own room."
        $ mc.change_location(bedroom)
        $ the_person.change_location(bedroom)
        $ the_person.draw_person(position = "missionary")
        "She plops down on your bed sprawling."
        the_person "That was...amazing."
        "She whispered, her voice soft and sated. You pressed your lips to her forehead, gently caressing her hair with your hands while you both rested together."
        mc.name "You are amazing."
        "As she nestled up to you, she sighed and let her fingers lazily roam in circles on your chest."
        "You lay in silence for a bit, the external world disappearing as you devoted your focus to each other."
        "The night stretched on, the hours slipping away as both basked in the warmth of your connection."
        "Eventually, exhaustion overtook both of you, and you drifted off to sleep."
        "Your bodies entwined, hearts beating as one. Just before you drifted off to sleep, the final sensation you experienced was the softness of her breath on your skin, her warmth surrounding you as you embraced her tightly."
    else:
        the_person "Good night [the_person.mc_title], you have sucked out all your little sister's energy tonight."
        mc.name "Good night, [the_person.title]. It was my pleasure."
        "You gave a sly grin, which earns you a slap on your arm."
        "You picked up your scattered clothes and head for your bedroom stark naked."
        $ mc.change_location(bedroom)
        
        #call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_her_place_KSPE01
        #return

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_her_place_KSPE02
    return

label lily_date_fuck_against_door_label(the_person): #Use this label if you fuck her right inside her front door.
    mc.name "I'm going to pin and fuck you there."
    if the_person.opinion.public_sex < 0:
        the_person "Here? In front of our house?"
        the_person "Oh... I don't know... I'm not sure I can stay quiet, what if Mom hear?"
        mc.name "That's the point!"
    elif the_person.opinion.public_sex < 2:
        the_person "Oh fuck... let's do it! I think I can stay quiet enough Mom won't hear..."
        "She doesn't seem particularly worried about it though."
    else:
        the_person "Oh fuck yes! Make me cum all over your big cock and make me scream for Mom to hear!"
        "She seems more excited than ashamed at the idea of Mom hearing you have sex."
    if not the_person.vagina_available:
        $ the_person.strip_to_vagina(prefer_half_off = False, position = "kissing")
        "You quickly reach down and strip off anything between you and her cunt, making a small pile on the floor."
    "You take your pants and underwear off, kicking them off onto the floor. then you grab [the_person.possessive_title] and pick her up."
    $ the_person.draw_person(position = "against_wall")
    "You push her back against her front door, pinning her to it. She wraps her legs around you."
    "You move your hips back and forth a bit, your cock sliding along her slit."
    if the_person.has_taboo("vaginal_sex"):
        the_person "Oh my god... I can't believe we're about to have sex... let alone like this!"
        "Although her words are unsure, her legs pull your body into hers, making it clear she wants this as much as you do."
    elif the_person.has_taboo("condomless_sex"):
        the_person "Oh shit... Condom..."
        if the_person.opinion.bareback_sex < 0:
            "She seems hesitant to let you continue bare, but doesn't make the jump to telling you to put one on."
        "Although her words are unsure, her legs pull your body into hers, making it clear she wants this as much as you do."
    "You push her slightly higher, then reach down and take your cock at the base, pointing it up."
    "Slowly, you let [the_person.title] slide down the side of her front door, your erection easily sliding inside of her pussy."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(20)
    $ play_moan_sound()
    "When you are fully inserted, she lets out a low moan. She holds on to your back with her arms and her legs urge you to go as deep as you can."
    if the_person.wants_creampie:
        the_person "Oh fuck that is so deep... Are you... are you going to cum inside me like this?"
    else:
        the_person "Oh fuck that is so deep... You aren't going to cum inside me like this, are you?"
    mc.name "Maybe. I haven't decided yet."
    "You give your hips a gentle thrust, getting a feel for the angle and penetration depth."
    the_person "MMMM... ahh... okay..."
    call fuck_person(the_person, private = True, condition = make_condition_apartment_door_sex(), start_position = against_wall, start_object = make_door(), skip_intro = True, girl_in_charge = False, position_locked = False, skip_condom = True) from _call_fuck_date_against_front_door_KSPE01
    $ the_report = _return
    return the_report

label lily_date_meet_mom_label(the_person):
    $ current_outfit = the_person.outfit #save this 
    "Upstairs, a door creaked open. Both of you froze, bodies tensing. The sound of footsteps padding down the hallway sent a jolt of panic through both of you."
    mom "Is that you [mom.mc_title]?"
    if mom_knows_about_lily():
        the_person "It's us."
        mom "Figures. You guys being too loud. I can hear you from my room."
        mc.name "Sorry, blame [the_person.fname], she's the one who screamed!"
        "[the_person.title] gave you an angry pinch on your waist."
        the_person "Sorry. You know how it felt too."
        mom "Well, try keeping it down... I'm trying to sleep. Oh, and [mom.mc_title], fair rule!"
        mc.name "Absolutely!"
    else:
        "[the_person.possessive_title!c]’s body tense beneath your own, her chest rising and falling rapidly as she stared up at you, her eyes wide with a mix of fear and lust."
        mc.name "Let me handle this. Wear your clothes."
        $ the_person.draw_person(position = "stand2")
        $ the_person.apply_outfit(current_outfit, show_dress_sequence = True)
        mc.name "Mom? You haven't sleep yet?"
        "[mom.possessive_title!c] flickers a bit suspiciously."
        mom "I thought I heard [the_person.fname] as well just now."
        "[the_person.possessive_title!c] straighten out her looks and strut forward like nothing happened."
        the_person "Yeah, we just happened to arrive at the same time. Go back to bed."
        "Mom narrows her eyes once again at both of you before silently goes back to her room."
        mc.name "That was close."

    return True

label lily_date_tv_finish_label(the_person):
    the_person "I hope you aren't too sleepy, I was thinking about watching a movie."
    mc.name "Sounds good to me."
    the_person "Okay!"
    $ popup_text = date_take_home_her_place_tv_finish_popup_text(the_person)
    $ show_popup_hint(popup_text)
    "You and [the_person.possessive_title] walk into the living room and sit down on the couch."
    $ the_person.draw_person(position = "sitting")
    "She grabs the remote and fires up a streaming service. Soon a movie is playing but you couldn't care less what is happening with it."
    $ the_person.draw_person(position = "sitting", display_transform = character_center_focus)
    "After the intro, [the_person.title] scoots over, her body now up against yours. She lays her head on your shoulder and softly sighs."
    the_person "Mmm, this is nice..."
    "You put your arm around her. You try to pay attention to the movie but it is impossible with her body up against yours."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(20)
    "Slowly, you let your hand slide down her shoulder, across her collarbone, and down to her breast..."
    #TODO go through and do all the  taboo breaks for this scene
    if the_person.is_willing(standing_grope) or the_person.is_willing(standing_finger):
        "She sighs when she feels you start to feel her up. She turns her head towards you."
        the_person "Mmm, that feels nice..."
        "She nuzzles up against you and starts to kiss your neck. You take it as a sign that she is eager for you to continue."
        $ mc.change_locked_clarity(20)
        $ the_person.change_arousal(5)
    else:
        "When you give her a little grope, she jumps, surprised at your forwardness."
        "She pushes your hand back up onto her shoulder."
        the_person "What are you doing?"
        mc.name "Sorry..."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    if mc.sex_skills["Foreplay"] < 2:
        "You clumsily grope her tit for a few minutes while she gives occasional kisses on your neck."
        "You start to move your head down to meet her lips with yours, but she pulls back."
        the_person "Ahh, are you seriously trying to kiss your mother on her lips?"
        mc.name "Yes."
        the_person "We can't. We are family."
        "She puts her hand on yours. She lets you leave your hand on her chest, but she stops you from actively groping her and goes back to watching the movie."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your time bonding with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    else:
        "You softly grope her, mixing it up, sometimes rubbing softly, sometimes teasing her nipple, and sometimes groping forcefully."
        "She moans into you as she begins to eagerly lick, suck, and kiss the side of your neck."
        "After several seconds, she stops."
        the_person "Oh god, that feels so good...It's wrong, but ..."
        "You look down at her and see her looking at your lips. You lean forward and she pushes up, your lips meeting together."
        "She opens her mouth and you begin to make out with [the_person.possessive_title] while your hand keeps groping her."
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(10)
    if mc.sex_skills["Foreplay"] < 4:
        "You make out with [the_person.possessive_title] for several minutes."
        "Your tongues lash against each other, and you eagerly grope her chest."
        "However, things eventually start to slow down, and she eventually pulls back."
        the_person "Ahh, you make me feel good, but we really shouldn't cross the line... We are still mother and son..."
        "Your cock aches a bit in disappointment, but you don't want to push her into anything she doesn't want to do."
        mc.name "I understand."
        "She leans back against you, putting her head on your chest."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    else:
        "You make out passionately with [the_person.possessive_title] for several minutes."
        "You can feel the heat building between you two when you finally feel her hand on your body."
        "[the_person.title]'s hand has started to stroke your cock in your pants as you make out. You make sure to moan your approval into her mouth."
        "Thankfully, it appears that you are going to get far enough with [the_person.title] tonight to atleast cum, from the way things are going."
        "She stops making out with you and looks down at your lap. She uses both hands and starts to fumble with your pants."
        "You lift up your hips as she pulls them down and off, your cock springing free."
        the_person "Oh fuck, you're so big!..."
        "She begins to stroke you with her hand again, this time skin on skin. She looks you in the eyes."
        if the_person.is_willing(blowjob):
            the_person "I want to taste it. I want to feel this monster in my mouth!"
        else:
            the_person "Fuck, I never do this but... I want to taste it! Can I taste it?"
        mc.name "Of course."
        "She gets up for a moment and turns, laying down on her stomach with her head on your lap."
        $ the_person.draw_person(position = "walking_away", display_transform = character_center_focus_flipped_test)
        "You put your hand on the back of [the_person.possessive_title]'s head as she slides her tongue up and down your cock a few times."
        if the_person.vagina_available:
            "You reach over with your other hand up between her legs."
        else:
            "You reach over with your other hand and slide it down her bottoms, along her backside and between her legs."
        "The angle is a little awkward but you manage to slide your middle finger along her pussy, feeling how wet she has gotten."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "After several seconds of teasing each other, [the_person.title] moves her mouth up to the tip of your cock, then opens her mouth and slides it inside."
        "At the same time, you slide your middle finger into her, causing a moan to reverberate around her now full mouth."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
    # if mc.max_energy < 140 or mc.sex_skills["Oral"] < 4: #Cum in her mouth
        "You can feel her ass pushing up, eagerly accepting your finger inside her."
        "[the_person.title]'s mouth working your cock is really turning you on, combined with her moans you can barely concentrate on fingering her."
        $ mc.change_arousal(15)
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "The angle of your hand around her back side makes it difficult for you to finger her properly, but you work it as best as you can."
        "Her mouth is really getting you turned on, you make sure to voice how good it feels."
        mc.name "Mmm, damn, that feels amazing [the_person.title]. I'm not going to last long if you keep going like that."
        the_person "Mmmmm, mmmhmmm..."
        "She doesn't stop sucking you, just murmurs her approval with a throaty moan."
        $ mc.change_arousal(25)
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "You do your best to make her feel good too, but after another minute of her oral attention, you feel yourself getting ready to orgasm."
        mc.name "Oh fuck, [the_person.title], that's it, I'm gonna cum!"
        $ mc.change_arousal(25)
        $ mc.change_locked_clarity(50)
        if the_person.facial_or_swallow() == "swallow":
            the_person "Mmmm..."
            "Her mouth keeps going, and you feel yourself peak and begin to cum into her mouth."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            "You fill her mouth with wave after wave of cum. She lets out a couple gasps and when you finish, you hear as she gulps it down."
            $ play_swallow_sound()
            "For a few blissful moments, you revel in your post orgasm haze."
        else:
            "Suddenly, her mouth pops off your cock with a pop, and she starts stroking you with her hand."
            the_person "Mmm, that's it, cum for me!"
            $ the_person.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            "You begin to orgasm. Her head is blocking your view, but she is letting you cover her face with your seed."
            "After several waves, your orgasm winds down, and for a few blissful moments, you revel in your post orgasm haze."
        $ the_person.draw_person(position = "missionary", display_transform = character_center_focus_flipped_test)
        "She turns over onto her back. When she does so, your pull you hand back from between her legs."
        the_person "Mmm, that was nice, but I'm almost there!"
        "She takes your hand puts it back between her legs. You easily slide two fingers inside of her."
        the_person "Mmmmmm, yessss!"
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "This position makes it much easier for you to finger her and to stimulate her g-spot. She closes her eyes and moans."
        the_person "Ohhhh, that's it [the_person.mc_title]... right there..."
        "Suddenly, you feel her whole body tense up and she has her own orgasm."
        $ the_person.change_arousal(35)
        $ the_person.have_orgasm()
        the_person "Yes!!! Oh!"
        "She body quivers as she orgasms. You eagerly finger her through the spasms until she starts to come down."
        "She lays there for several seconds with her head on your lap as she recovers."
        the_person "Wow... that was nice..."
        $ the_person.apply_planned_outfit()
        "She quickly hops up and cleans up her face and then comes back."
        $ the_person.draw_person(position = "missionary", display_transform = character_center_focus_flipped_test)
        "You watch the rest of the movie together with [the_person.possessive_title] while she lays her head in your lap."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False

    return False

label lily_date_service_offer_label(the_person):
    if aunt_living_with_mc():
        the_person "Do you... erm.. we could ... I mean.. do you want to go back to your room, and I could show you just how much [the_person.possessive_title] appreciate it... without Gabby's big butts interfering us."
    else:
        the_person "Do you... erm.. do you want to ... I mean.. we could go back to my room, and I could show you just how much [the_person.possessive_title] appreciate it..."
    if the_person.is_willing(anal_standing) and the_person.is_willing(standing_doggy) and the_person.is_willing(blowjob):
        the_person "You can pick any hole you want and have your way with it. I wouldn't mind!"
    elif the_person.is_willing(anal_standing):
        the_person "I could bend over the side of the bed and let you pick a hole..."
        the_person "You could stick it in my butt if you want. I wouldn't mind!"
    elif the_person.is_willing(standing_doggy):
        the_person "I could bend over the side of the bed and let you fuck me as hard as you want. I wouldn't mind!"
    elif the_person.is_willing(blowjob):
        the_person "I could get on my knees and service you with a nice blowjob if you want. I don't mind!"
    else:
        the_person "I think we could figure out a way to make it feel good for you. I don't mind!"
    mc.name "That's a nice offer..."
    menu:
        "Get serviced":
            mc.name "I'd be an idiot to say no. Let's do it."
            the_person "Mmm, okay! Let's go..."
            $ mc.change_location(bedroom)
            $ the_person.change_location(bedroom)
            mc.name "Alright, first things first. Get naked."
            "She turned to face you, slowly backing up to the bed."
            "Her hands went to the straps of her dress, and slipped them down her shoulders with a deliberate slowness."
            $ the_person.change_arousal(5)
            the_person "As you wish, [the_person.mc_title]..."
            $ the_person.strip_outfit(position = "stand3")
            $ mc.change_locked_clarity(20)
            the_person "Do you like what you see?"
            "She ran her hands down her sides, her nails lightly grazing her skin, as she stand waiting."
            menu:
                "Fuck her Tits" if the_person.has_large_tits and the_person.is_willing(tit_fuck):
                    mc.name "Get on your knees. I want to have some fun with those amazing tits of yours."
                    "[the_person.possessive_title!c] quickly drops to her knees."
                    $ the_person.draw_person(position = "blowjob")
                    "She takes her considerable tits in her hands as you step over to her, looking up at you with a smile."
                    the_person "Go ahead. Use [the_person.possessive_title] tits to make yourself feel good!"
                    "You push your cock into the valley of her ample titflesh."
                    $ mc.change_locked_clarity(30)
                    "She begins to stroke your cock with her breasts, using her hands to control the tempo."
                    call fuck_person(the_person, private = True, start_position = tit_fuck) from _call_fuck_person_her_place_service_tit_fuck_KSPE01
                    $ the_person.call_dialogue("sex_review", the_report = _return)

                "Fuck her Mouth" if the_person.is_willing(blowjob):
                    mc.name "Get on your knees. I want to feel those pouty lips of yours around my cock."
                    "[the_person.possessive_title!c] quickly drops to her knees."
                    $ the_person.draw_person(position = "blowjob")
                    "She licks her lips, staring at your cock as you step over to her."
                    "[the_person.title] looks up at you and opens her mouth, silently waiting for you to use her."
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "You put your hand on the back of her head and gently guide her mouth onto your erection."
                    $ mc.change_locked_clarity(40)
                    "You feel a gently moan as your cock slides into her mouth. You let go of her head and she begins to suck you off."
                    call fuck_person(the_person, private = True, start_position = blowjob) from _call_fuck_person_her_place_service_blowjob_KSPE01
                    $ the_person.call_dialogue("sex_review", the_report = _return)

                "Fuck her Pussy" if the_person.is_willing(standing_doggy):
                    mc.name "Bend over the bed. Let me see what I'll be working with tonight."
                    "[the_person.possessive_title!c] quickly obeys, bending over her bed and preseting her ass to you."
                    $ the_person.draw_person(position = "standing_doggy")
                    "She looks back at you, hungrily, watching as you step over to her."
                    "You grab [the_person.title]'s hips and you push yourself up against her, grinding your dick against her ass."
                    $ the_person.change_arousal(10)
                    "She moans and grinds back against you a bit. Soon, you're ready for more."
                    "You use one hand to point your cock down and then push your hips forward, letting your cock slide inside her."
                    $ mc.change_locked_clarity(50)
                    "Once you are all the way in, you move your hand back to her hip and giver her a couple thrusts. Time to fuck this slut."
                    call fuck_person(the_person, private = True, start_position = standing_doggy, skip_condom = True) from _call_fuck_person_her_place_service_doggy_KSPE01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                "Fuck her Ass" if the_person.is_willing(anal_standing):
                    mc.name "Bend over your bed and show me these holes you mentioned."
                    "[the_person.possessive_title!c] quickly obeys, bending over her bed and preseting her ass to you."
                    $ the_person.draw_person(position = "standing_doggy")
                    "She looks back at you, hungrily, watching as you step over to her."
                    "You grab [the_person.title]'s hips and you push yourself up against her, grinding your dick against her ass."
                    $ the_person.change_arousal(10)
                    "She moans and grinds back against you a bit. Soon, you're ready for more."
                    mc.name "Do you have any lube?"
                    the_person "Oh, yeah! One second..."
                    "She reaches over to her bedside table and grabs some lubricant, quickly passing it to you."
                    "You quickly apply ample amounts. Your cock and her puckered hole now glisten from it."
                    "You use one hand to point your cock down and then push your hips forward."
                    "There are several moments of resistance as your erection slowly loosens and then pushes inside her sphincter."
                    $ mc.change_locked_clarity(70)
                    "When it finally gives way, you easily slide all the way in."
                    "You give [the_person.title] Time to fuck this slut."
                    call fuck_person(the_person, private = True, start_position = anal_standing, skip_condom = True) from _call_fuck_person_her_place_service_doggy_anal_KSPE01
                    $ the_person.call_dialogue("sex_review", the_report = _return)

                "Just fool around":
                    mc.name "Why don't we just fool around some? No need for anything specific."
                    the_person "Mmm, okay!"
                    $ the_person.change_to_bedroom()
                    call fuck_person(the_person, private = True) from _call_fuck_person_her_place_service_fool_around_KSPE01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
        "Not tonight":
            mc.name "Sorry, I don't have time for that tonight, but I appreciate the offer."
            the_person "Huh? Really?"
            "She seems shocked at your answer, but is obedient enough to know not to second guess it."
            $ the_person.change_stats(happiness = -20, love = -2)
            the_person "Ok... well... maybe another time then..."
            mc.name "I should probably get going."
            the_person "Right..."
            "You say goodnight and leave, heading back to your room."
            return False
    $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
    
    return False

label lily_date_romance_finish_label(the_person):
    "The house felt different tonight, quieter, more intimate."
    "She led you to the living room, where she poured a glass of wine for both of you, her movements slow and deliberate. "
    "When she handed you the glass, your fingers brushed, and you felt a spark of electricity shoot through you."
    $ the_person.draw_person(position = "sitting")
    the_person "Well, what would you like to do now?"
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] leans closer to you and puts her hand on your thigh. It's obvious what she wants, but she's waiting for you to make the first move."
    menu:
        "Kiss her":
            "You put your drink aside, then put one hand on the back of [the_person.possessive_title]'s neck and pull her into a kiss."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            if mom_knows_about_lily():
                "She returns the kiss eagerly."
            else:
                "She returns the kiss for a moment, then breaks away. Her lips hover, barely separated from yours."
                the_person "Mom gonna find us here..."
                "You kiss her again, and this time all resistance falls away."
            "After a long moment spent making out [the_person.title] pulls away."
            the_person "I think we'd be more comfortable in the bedroom, don't you?"
            $ the_person.draw_person(position = "walking_away")
            mc.name "I couldn't agree more."
            if aunt_living_with_mc():
                $ mc.change_location(bedroom)
                $ the_person.change_location(bedroom)
                "[the_person.possessive_title!c] quickly push you towards your own bedroom and starts to undress."
            else:
                $ the_person.change_to_bedroom()
                "[the_person.possessive_title!c] leads you to her bedroom and starts to undress."
            $ the_person.strip_to_underwear()
            call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_KSPE104
            $ the_person.call_dialogue("sex_review", the_report = _return)
            $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
            
        "Go back to your room":
            if aunt_living_with_mc():
                mc.name "It's been a fun evening, but you need to return before Gabby starts gossiping."
                $ the_person.change_happiness(-5)
                "[the_person.possessive_title!c] seems a little disappointed, but she smiles politely."
                the_person "I guessed you are right."
                the_person "I had a fun time, we should do this again."
                mc.name "I think I'd like that."
                "You finish your drink and say goodnight to [the_person.title]."
            else:
                mc.name "It's been a fun evening, but I have a bit of work to finish in my room. I hope we can do this again some time though."
                $ the_person.change_happiness(-5)
                "[the_person.possessive_title!c] seems a little disappointed, but she smiles politely."
                if not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0:
                    the_person "Of course. It's getting late, I should probably be going to bed as well."
                else:
                    the_person "Of course, that's fine. My [the_person.so_title] probably wouldn't like it that I have other men visiting anyways."

                the_person "I had a fun time, we should do this again."
                mc.name "I think I'd like that."
                "You finish your drink and say goodnight to [the_person.title]."

    return False

label lily_date_lingerie_finish_label(the_person):
    the_person "Have a seat and enjoy your drink, I'll be back in a moment."
    $ clear_scene()
    if the_person.opinion.not_wearing_anything > the_person.opinion.lingerie:
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True) #She's wearing nothing at all. nothing at all. nothing at all...

    elif the_person.opinion.lingerie >= 0:
        $ the_person.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness + 20, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person)), update_taboo = True) #She's just wearing lingerie for the evening.

    else: #She doesn't like being nude or wearing lingerie, so just strip her to her underwear
        $ the_person.outfit.strip_to_underwear()
    "You sit down on the couch and relax while you wait for [the_person.possessive_title]. A few minutes later she calls out for you."
    the_person "[the_person.mc_title], could you come here?"
    "You down the rest of your drink and leave the empty glass behind, following the sound of her voice."
    if aunt_living_with_mc():
        "Your bedroom door was slightly ajar, the warm glow of bedside lamp spilling out into the dimly lit hall."
        "You pushed the door open slowly, and there she was, sitting on the edge of your bed. "
        the_person "Gabby was asleep. I hope you didn't mind I entered your bedroom."
        $ the_person.draw_person(position = "sitting")
        $ mc.change_locked_clarity(15)            
        $ mc.change_location(bedroom)
        $ the_person.change_location(bedroom)
    else:
        "Her bedroom door was slightly ajar, the warm glow of her bedside lamp spilling out into the dimly lit hall."
        mc.name "[the_person.title]?"
        the_person "Come in..."
        "You pushed the door open slowly, and there she was, sitting on the edge of her bed. "
        $ the_person.draw_person(position = "sitting")
        $ mc.change_locked_clarity(15)
        $ the_person.change_to_bedroom()
    if the_person.is_naked:
        "She is fully naked, baring everything to you."
    elif the_person.opinion.lingerie >= 0:
        "She’ve changed out of her dress and into a silky lingerie that clung to her figure, the fabric hinting at the curves beneath."
        "Her hair was down, cascading over her shoulders in soft waves, and her lips curved into a smile that took your breath away."
    else:
        "She stood there in nothing but her underwear, her curves just took your breath away."
    if aunt_living_with_mc():
        the_person "Close the door. Don't want others to accidentally see us."
    else:
        the_person "Close the door. Don't want Mom to accidentally see us."
    $ the_person.draw_person()
    "She patted the space beside her on the bed, her movements slow and deliberate."
    the_person "Sit with me."
    "A slight hesitation, but you moved toward her, the bed dipping slightly as you sat down."
    if the_person.is_naked:
        "She shifted closer, her thigh pressing against yours, and you could feel the heat of her naked body."
    else:
        "She shifted closer, her thigh pressing against yours, and you could feel the heat of her body."
    if the_person.has_taboo("kissing"):
        $ the_person.call_dialogue("kissing_taboo_break")
        $ the_person.break_taboo("kissing")
    mc.name "You're perfect."
    "Without thinking, you leaned in, capturing her lips in a soft, hesitant kiss."
    "[the_person.possessive_title!c] responded immediately, her arms wrapping around your neck as she deepened the kiss."
    call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_KSPE17
    $ the_person.call_dialogue("sex_review", the_report = _return)
    $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
            

    return False

label lily_plan_fuck_date_label():
    $ the_person = lily
    
    mc.name "Hey [the_person.title]... When was the last time we went at it like rabbits all night?"
    "Your question left her bewildered initially, but then it became clear to her. The suggestion caused a visible redness to spread across her cheeks."
    the_person "You perverted brother! Stop corrupting your pure innocent little sister~"
    "You snickers."
    mc.name "Well?"
    if the_person.days_since_event("Last Vaginal Day") == 0: #had sex today
        the_person "Mmm... We already fucked today... and it's not all night long, so it didn't count..."
    elif the_person.days_since_event("Last Vaginal Day") == 1: #had sex yesterday
        the_person "Mmm... We've fucked yesterday..."
    else:
        the_person "Mmm... Been a while, doesn't it?"
        "[the_person.possessive_title!c] glares at you. You would have found it believable if her face hadn't been getting redder."
    mc.name "Did you actually kept a log of us fucking?"
    the_person "Shut up! Stupid brother! Anyway, weekend? You'll definitely need the rest after that... But I AM NOT WEARING FUCKING BUNNY EARS!"
    
    menu:
        "Plan a date":
            call date_schedule_selection(the_person, 4, day_restriction = (2, 3, 4)) from _call_date_schedule_selection_plan_fuck_date_KSPE
            if _return:
                $ create_fuck_date_action(the_person, _return)
                mc.name "It settled then."
                mc.name "You {i}do{/i} look cute in it though."
                $ mc.change_locked_clarity(10)
                the_person "I'll leave the door unlock. And no."
                the_person "Cave man."
                "She playfully stuck her tongue out towards you."
            else:
                mc.name "I'm sorry to get your hopes up. It seems my schedule is full this week."
                the_person "Stupid brother! I don't want to talk to you anymore."
                "She pouts."
                mc.name "Cheer up. It's not like we are not fucking everyday any way. Just not gonna be an all night long marathon."

        "Maybe some other time":
            mc.name "Damn, Maybe I should ask Gabby next if she's willing to wear the bunny ears. It seems my schedule is full this week."
            the_person "Stupid brother! I don't want to talk to you anymore."
            "She pouts."

    return

label lily_fuck_date_label():
    #Lily personalized fuck date.
    # Occurs at night. You go to her room.
    $ the_person = lily
    
    "You have a fuck date planned with [the_person.title]."
    $ mom_block = False

    menu:
        "Get ready for the date {image=time_advance}":
            pass

        "Cancel the date (tooltip)She won't be happy with you cancelling last minute.":
            "You get your phone out and text [the_person.title]."
            mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
            $ the_person.change_stats(happiness = -5, love = -5)
            "There's a pause before she responds."
            the_person "And I just finished getting all dressed up for you. Oh well."
            return

    if mom_date_intercept_requirement(mom, the_person) and renpy.random.randint(0,100) < (mom.love):
        call mom_date_intercept(mom, the_person) from _call_mom_date_intercept_fuck_date_KSPE
        $ mom_block = True
        if _return:
            $ clear_scene()
            return "Advance Time"

    $ mc.stats.change_tracked_stat("Girl", "Dates", 1)
    $ clear_scene()
    $ lily_bedroom.show_background()
    $ the_person.change_to_bedroom()
    $ mc.change_location(lily_bedroom)
    "You go inside [the_person.possessive_title] bedroom as soon as you see [mom.possessive_title] enters her room. [the_person.title] greets you with a seductive smile."
    #Figure out her outfit for this
    if the_person.opinion.not_wearing_anything > the_person.opinion.lingerie:
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True) #She's wearing nothing at all. nothing at all. nothing at all...

    elif the_person.opinion.lingerie >= 0:
        $ the_person.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness + 20, the_person.sluttiness // 3, guarantee_output = True, preferences = WardrobePreference(the_person)), update_taboo = True) #She's just wearing lingerie for the evening.

    else:
        $ the_person.apply_outfit(the_person.decide_on_outfit(), update_taboo = True) #She picks a slutty outfit, but nothing truly "special".
    
    if mom_block:
        the_person "You are late."
        mc.name "Sorry.. Mom in the way."
        if home_harem():
            the_person "We followed the rule she established."
            the_person "Tonight, your dick belongs to me alone. All night long."
        else:
            the_person "You sure she's asleep?"
            the_person "I don't want to get caught."
    else:
        the_person "Right on time. You seems eager."
        the_person "Missed me?"
        mc.name "I'd say Fuck You... But that was my plan all along."
        "[the_person.possessive_title!c] giggles."
        the_person "The plan is mutual. All night long..."
    $ the_person.add_situational_slut("Date", 20, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness since you're committing incest

    call fuck_date_event(the_person) from _call_fuck_date_event_KSPE

    $ the_person.clear_situational_slut("Date")
    return "Advance Time"

label lily_fuck_date_event(): #A breakout function so we can call the fuck_date stuff any time you go back to a girls place.
    $ the_person = lily
    
    if the_person.is_submissive or the_person.opinion.giving_blowjobs > 0:
        "She approached you on her knees."
        #She's on her knees and ready to suck you off as soon as you come in.
        $ the_person.draw_person(position = "kneeling1")
        $ mc.change_locked_clarity(20)
        "She licks her lips and watches you from her knees."
        the_person "Let's start with my lollipop training."
        call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True) from _call_fuck_person_KSPE34
    else:
        #She's standing and ready to make out as soon as you come in."
        $ the_person.draw_person()
        $ mc.change_locked_clarity(10)
        "She wastes no time wrapping her arms around you and kissing you."
        the_person "I want it buried in my cunt. Right. Now."
        call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_KSPE35

    $ the_report = _return

    $ done = False
    #$ had_to_run = False  Don't need to run
    $ girl_came = False
    $ mom_awake = False
    $ count = 0
    $ energy_gain_amount = mc.max_energy // 3 #Drops each round, representing your flagging endurance.
    while not done:   # maximum of 8 loops
        if the_report.get("girl orgasms", 0) > 0: #TODO: Have some variation to this based on how many times we've looped around.
            $ the_person.change_love(2 + the_person.opinion.cheating_on_men)
            $ the_person.change_slut(1, 80)
            the_person "Oh god... That was amazing."
            $ the_person.draw_person(position = "missionary")
            "[the_person.title] lies down on her bed and catches her breath."
            #the_person "Ready to get back to it?"
            $ girl_came = True
        else:
            the_person "Whew, that's a good exercise. Pass me some water and let's go for another!"
            "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
            $ the_person.draw_person(position = "missionary")
            "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."

        if mc.energy  + energy_gain_amount < 50 or count > 7: #Forced to end the fuck date, so we set done to True.
            "You both lost track of time, indulging in the carnal desire for each other."
            the_person "You are out of juice, [the_person.mc_title]."
            if girl_came:
                the_person "I guessed we should stopped. Too much sex is bad for your health."
                "You gave her a slap at the back of her head"
                the_person "Ow..wee! Tee hee hee."
            else:
                $ the_person.change_love(-1)
                $ the_person.change_slut(-1)
                the_person "Well I guess we're done then... Maybe next time you can get me off as well."
            $ done = True
        elif the_person.energy + energy_gain_amount < 50:
            the_person "Time out! Time out! I surrender! Death by snu snu! Death by snu snu!"
            "She plops down on her bed sprawling."
            the_person "That was...amazing."
            "She whispered, her voice soft and sated. You kissed her forehead, your hands stroking her hair as you lay there together."
            $ done = True            
        else:
            "After a short rest you've recovered some of your energy and [the_person.possessive_title]'s eager to continue."
            $ mc.change_energy(energy_gain_amount)
            $ the_person.change_energy(energy_gain_amount) #She gains some back too
            if energy_gain_amount >= 10:
                $ energy_gain_amount -= 10 #Gain less and less energy back each time until eventually you're exhausted and gain nothing back.
            menu:
                "Fuck her again":
                    "Soon your dick hardened, ready for the next plunge into her holes."
                    mc.name "Ready, [the_person.title]? "
                    $ ran_num = renpy.random.randint(0, 100 - (count * 10))
                    $ count += 1
                    if ran_num < 30 and not mom_awake and mom.is_available: #Only once
                        #Mom awakes
                        $ mom_awake = True
                        "She smiles and moves to kiss you, when you hear footsteps across the hall."
                        the_person "Oh shit! It's Mom!"
                        $ the_person.draw_person(position = "sitting")
                        if mom_block and home_harem():
                            the_person "Oh wait, she knew you are here."
                        elif mom_block:
                            the_person "As long as she didn't pop in here... You did lock the door, didn't you?"
                        else:
                            "She sits on the edge of the bed, waiting for Mom to reenter her room."
                        the_person "If we stay quiet, we won't get caught, right?"
                        mc.name "I'm game if you are..."
                        menu:
                            "Stay quiet":
                                #Time passes then you fuck her as normal.
                                "You lie back and get comfortable on [the_person.title]'s bed alongside her."
                                if home_harem():
                                    "Despite them both knowingly sharing you, it seems the idea of getting caught in the act still bothers [the_person.possessive_title]. Or so you thought."
                                    "[the_person.title] gave you a smirk."
                                    "She leans over and starts fondling your balls."
                                    the_person "It's not like she doesn't know, right?"
                                else:
                                    "The idea of getting caught in the act is very enticing. But you have to think from [the_person.possessive_title]'s perspective too."
                                    "[the_person.title] gave you a playful look."
                                    "She leans over and starts fondling your balls."
                                "Soon, you can hear Mom reenters her room and the door clicked shut."
                                the_person "Now, where were we?"
                                call fuck_person(the_person, private = True) from _call_fuck_person_KSPE37 #Just normal start.
                                $ the_report = _return

                            "Grope her":
                                #Basically an extended intro.
                                $ mc.stats.change_tracked_stat("Girl", "Groped", 1)
                                "You shuffle across [the_person.title]'s bed next to her and wrap your arms around her torso."
                                "[the_person.title] gave a surprise look."
                                the_person "Don't... Uh huh... Mhmm."
                                $ mc.change_locked_clarity(15)
                                if the_person.has_large_tits:
                                    "You cup her tits and squeeze them together, then slide your hands down her chest and stomach toward her waist."
                                else:
                                    "You run your hands over her tits, stomach, and then down toward her waist."
                                the_person "Ah... Oh, wait ... [the_person.mc_title]!"
                                "You kneel on the bed behind [the_person.possessive_title] and move your hands lower. You stroke her inner thighs and she opens her legs for you."
                                $ mc.change_locked_clarity(10)
                                "Your hand finally slides over her pussy, gently brushing her clit, and she clasps her mouth to stifle her moans."
                                "[the_person.possessive_title!c] tries to grab your hand but it's too late."
                                "You slide a finger into her pussy and she holds her breath for a second."
                                the_person "You!"
                                $ the_person.change_stats(obedience = 1, slut = 2 + the_person.opinion.public_sex, max_slut = 60,
                                    arousal = mc.foreplay_sex_skill + (5 * the_person.opinion(("public sex", "being fingered"))))
                                the_person "Pervert..."
                                "Soon, you can hear Mom reenters her room and the door clicked shut."
                                $ mc.change_locked_clarity(20)
                                the_person "Now come here and fuck me!"
                                call fuck_person(the_person, private = True) from _call_fuck_person_KSPE38
                                $ the_report = _return

                            "Make her suck your cock" if the_person.effective_sluttiness("sucking_cock") >= 50:
                                #Basically an extended intro
                                "You shuffle across the bed and stand up in front of [the_person.title]. She looks at you quizzically before noticing your hard cock at face level."
                                if the_person.has_taboo("sucking_cock"):
                                    the_person "You serious?"
                                    "She looks up at you and shakes her head, pointing at the door."
                                    "You take a small step forward, pressing the tip of your cock to her cheek."
                                    mc.name "Your mouth will be too full to make a significant noise."
                                    "[the_person.possessive_title!c] glares at you. You shrug and flex your dick in her face."
                                    the_person "You are a bad rolemodel..."
                                    "[the_person.title] rolls her eyes and leans forward, kissing the tip of your cock before sliding it past her lips."
                                    $ the_person.break_taboo("sucking_cock")
                                    $ mc.change_locked_clarity(20)
                                else:
                                    the_person "You must be joking?"
                                    $ mc.change_locked_clarity(20)
                                    "You brush her cheek with the back of your hand. She leans forward, opening her mouth and kissing the tip of your cock."
                                    "She looks up at you from her sitting position while her tongue works around the tip in circles. Her eyes occasionally drifted to her door."
                                the_person "Mhmm? Mmmm. Hmmm. Uhmmmm."
                                "She tries to stifle her moans as she takes your cock deeper into her mouth. You can still hear Mom climbing the stairs back up to the second floor. Closer and closer."
                                "With a soft, wet smack she slides back off and takes a breath."
                                the_person "She's close!"
                                $ mc.change_locked_clarity(20)
                                "She licks the bottom of your dick and winks at you."
                                if home_harem():
                                    the_person "Mhmm, tell me, is she willing to do this?"
                                    "It seems like it triggers her competitive spirit."
                                    "She licks your balls while maintaining eye contact with you."
                                else:
                                    the_person "Mhmm, don't let her hear you!"
                                "Oh Fuck! Almost. She's a succubus!"
                                "Soon, you can hear Mom reenters her room and the door clicked shut. And [the_person.possessive_title] have instead transition into swallowing your dick deep."
                                call fuck_person(the_person, private = True, start_position = deepthroat, skip_intro = True) from _call_fuck_person_KSPE39
                                $ the_report = _return

                            "Fuck her while Mom's outside" if the_person.effective_sluttiness("vaginal_sex") >= 80:
                                #This is basically an extended intro
                                $ mc.change_locked_clarity(20)
                                "You shuffle behind [the_person.title] and wrap your arms around her, grabbing a tit with one hand while the other slides down to her waist and caresses her pussy."
                                "[the_person.possessive_title!c] quickly realized your intention and down onto her back willingly."
                                $ the_person.draw_person(position = "missionary")
                                if not the_person.vagina_available:
                                    "You pulled her panty away as she lift her cute butt off the bed."
                                    $ the_person.strip_to_vagina(prefer_half_off = False, position = "missionary")
                                    "Once her cute little pussy exposed, she spreads her legs for you."
                                    $ the_person.update_outfit_taboos()
                                else:
                                    "She spreads her legs as you climb on top of her, her eyes still tracking Mom's steps."
                                "The whole situation clearly aroused her."
                                $ the_person.change_arousal(10)
                                $ wanted_condom = False
                                if the_person.effective_sluttiness("condomless_sex") < the_person.get_no_condom_threshold():
                                    $ wanted_condom = True
                                    "She pauses and points towards your cock and mouthing \"C-O-N-D-O-M\""
                                else:
                                    $ mc.change_locked_clarity(10)
                                    "She reaches down with her free hand and strokes your hard cock, sliding the tip against her wet slit."

                                menu:
                                    "Wear a condom":
                                        if not wanted_condom:
                                            "You pause for a moment to grab a condom from her bedstand. [the_person.possessive_title!c] rolls her eyes impatiently underneath you."
                                        else:
                                            "You pause for a moment to grab a condom from her bedstand and put it on."
                                        $ mc.condom = True


                                    "Fuck her bareback":
                                        if wanted_condom:
                                            "You hold a finger up to your lips, reminding her to be quiet, and slide into her anyway."
                                            $ the_person.change_obedience(2 + the_person.opinion.bareback_sex)
                                            $ mc.change_locked_clarity(20)
                                            "Her eyes go wide as your hard dick slides into her raw pussy. She glares up at you, but the direct skin contact overwhelms her soon enough."
                                        else:
                                            "She closes her eyes and bites her lip as your hard dick slides into her raw pussy. She is barely able to keep her moans quiet."
                                        $ the_person.break_taboo("condomless_sex")

                                $ the_person.break_taboo("vaginal_sex")
                                the_person "Mmmhm? Oh [the_person.mc_title], move slowly."
                                $ mc.change_locked_clarity(20)
                                "She clasps her mouth to stifle her moans and turns her head to the side as you start to pump into her."
                                $ play_moan_sound()
                                the_person "[the_person.mc_title]!"
                                "Soon, you can hear Mom reenters her room and the door clicked shut."
                                $ mc.change_locked_clarity(20)
                                the_person "Oh fuck, you're crazy [the_person.mc_title]! What if we get caught?"
                                mc.name "We didn't. Relax and enjoy."

                                call fuck_person(the_person, private = True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = not mc.condom) from _call_fuck_person_KSPE102
                                $ the_report = _return

                        #TODO: At this point run a check on her arousal.
                    else:
                        call fuck_person(the_person) from _call_fuck_person_KSPE41
                        $ the_report = _return

                "Call it a night":
                    mc.name "I have wake up early tomorrow. This was fun."
                    if girl_came:
                        "She sighs happily and lies down on her bed."
                        $ the_person.draw_person(position = "walking_away")
                        "[the_person.possessive_title!c] snuggles closer to you, allowing you to wrap your arms around her sexy body."
                        if the_person.has_large_tits:
                            "Your hands playfully land on her [the_person.tits_description]."
                            $ the_person.draw_person( position = "back_peek", emotion = "happy")
                        the_person "Goodnight [the_person.mc_title]."
                        mc.name "Goodnight [the_person.title]."
                    else:
                        the_person "Really? I didn't even get to cum yet..."
                        $ the_person.change_love(-1)
                        $ the_person.change_slut(-1)
                        "You kiss [the_person.title], then get up and start collecting your clothes."
                        $ mc.change_location(bedroom) # go home
                    $ done = True

    #As soon as done is True we finish looping. This means each path should narrate it's own end of encounter stuff.
    #Generic stuff to make sure we don't keep showing anyone.
    call check_date_trance(the_person) from _call_check_date_trance_fuck_date_KSPE

    python:
        #the_person.clear_situational_slut("Date")
        clear_scene()
        del energy_gain_amount
    
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_fuckdate_KSPE01
    if mom_awake and home_harem():
        call lily_aftersex_breakfast_label(the_person) from _call_aftersex_breakfast_KSPE
    else:
        call girlfriend_wakeup_label(the_person) from _call_girlfriend_wakeup_fuckdate_KSPE01
    return 

label lily_aftersex_breakfast_label(the_person):
    $ the_person = lily
    
    $ lily_bedroom.show_background()
    #$ the_person.apply_outfit(Outfit("Nude"))
    $ scene_manager = Scene()
    #$ scene_manager.add_actor(the_person, position = "missionary")
    "The scent of Lily’s shampoo—something sweet like coconut—was the first thing that registered. Then, the warm weight of her leg thrown over yours, the silk of her sheets tangled around our ankles."
    "Your eyes opened to the soft morning light filtering through her blinds, painting stripes across the bare skin of her back. She was still asleep, a contented, almost smug little smile on her face, her blonde hair fanned out across the pillow."
    "Last night... the memory was a vivid, heated flash that warmed your blood. The whispered promises, the stifled laughter, the way the headboard had gently tapped a rhythm against the wall that you’d both tried so hard to quiet."

    #$ scene_manager.hide_actor(the_person)
    #$ home_hall.show_background()
    "Carefully, so as not to wake her, you extricated yourself from the bed and pulled on your discarded jeans. "
    "You padded silently out of her room, the cool hardwood floor a shock against your bare feet. "
    "The house was quiet, but not silent. From downstairs came the familiar, comforting sounds of morning: the gentle sizzle of something in a pan, the clink of a glass, the soft hum of the refrigerator."
    $ kitchen.show_background()
    "You found [mom.possessive_title] in the kitchen, a vision of domestic efficiency. "
    mc.name "Morning."
    $ scene_manager.update_actor(mom, display_transform = character_center_flipped, position = "back_peek")
    mom "Good morning, [mom.mc_title]. You're up early."
    mc.name "Smelled the coffee."
    mom "Mmhmm..."
    mom "You look like you could use a good breakfast. You must be... depleted. Need to keep your energy up."
    $ scene_manager.update_actor(mom, position = "standing_doggy")
    "She turns back to the stove, giving you a deliberate, devastating view of her ass as she bends slightly to check the oven. "
    mom "Hope you're hungry..."
    mom "Pancakes?"
    $ scene_manager.update_actor(mom, position = "stand4")
    "You took a greedy bite of the pancakes."
    mc.name "This is great, [mom.title]. Thanks."
    mom "Anything for my boy."
    mom "You know I'll always take care of you. Make sure you're... {i}satisfied{/i}."
    "The sound of light footsteps on the stairs filled the silence.Her hair was a mess, and she looked gloriously, obviously well-loved."
    $ scene_manager.add_actor(the_person, position = "stand4")
    the_person "Ooh, pancakes! I'm starving."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "Slipping onto the stool next to you and leaning her head on your shoulder. "
    "She pressed a quick, daring kiss to your bicep, a move she’d never make if she thought Mom was really upset."
    $ scene_manager.update_actor(mom, position = "stand3")
    "Mom turned around, and place a plate of pancakes in front of [the_person.possessive_title]."
    mom "I'll bet you are, dear. You two must have had quite the... workout last night."
    the_person "Opps... You heard?"
    "Mom rolled her eyes."
    mom "I’m just glad [mom.mc_title] has such an... enthusiastic fitness partner. Though, I hope you at least remembered to stretch first. Proper form is so important to avoid... soreness."
    "[the_person.possessive_title!c]'s blush deepens, but a laugh bursts out of her anyway. She wrapped her arm around yours possessively."
    the_person "Don’t worry, Mom. We’re very flexible. {i}Both of us{/i}."
    mom "I’m sure you are. {i}Both of you{/i}."
    "Then she walked around the island, taking her spot next to you... sandwiching you in the middle."
    $ scene_manager.update_actor(mom, display_transform = character_left_flipped, position = "sitting")
    "Her thumbs began to knead the tight muscles on your shoulder in a slow, circular motion."
    mom "But everyone needs a good cool-down after an intense session. You wouldn't want to pull anything."
    mom "I'd hate to see you get... injured."
    mc.name "Hmmm...A bit to the left, please."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title!c] rolled her eyes at an obvious attempt to rile her."
    the_person "Sigh... I'm going back to bed."
    if mc.business.is_weekend:
        the_person "Don't bother waking me up for lunch."
    else:
        mom "And your class?"  
        the_person "Late. Noon class."    
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.update_actor(mom, position = "stand2")
    if mc.business.is_weekend:
        mom "I'll go take my shower. Just put the plate in the sink later."
    else:
        mom "I need to get ready for work. Just put the plate in the sink later. "
    mc.name "I'll clean. Don't worry. Go."
    $ mc.change_location(bedroom) # go home
    $ scene_manager.clear_scene()

    return









    