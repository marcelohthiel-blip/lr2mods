#Counter = KME01

# Regular events 

init 4 python:
    def mom_sister_talk_requirement():
        return ((lily.knows_pregnant or mom.knows_pregnant 
            and lily.is_available and mom.is_available) 
            and not (mom.has_queued_event("sleeping_walk_in_label") or lily.has_queued_event("sleeping_walk_in_label")))

    def mom_sister_snoop_initialization(self):
        # No Init code for this yet.
        return

    def lily_helping_in_kitchen_requirement():
        return (mom.is_pregnant and mom.location == kitchen and time_of_day == 3 and lily.is_available)

    def baby_shopping_requirement():
        if time_of_day == 3 and mc.business.has_funds(500):
            person = get_baby_shopping_person()  # Get the person first
            if person is not None:  # Check if we actually got someone
                return True
        return False

    def get_baby_shopping_person():
        #temp_list = []
        #for person in known_people_in_the_game():
        #    if person.has_role(girlfriend_role) and person.pregnancy_is_visible:
        #        temp_list.append(person) 
        return get_random_from_list([x for x in list_of_people if (x.has_role(girlfriend_role) and x.pregnancy_is_visible)])

    def girlfriend_needs_requirement():
        if schedule_sleepover_available():
            person = get_needy_girlfriend()  # Get the person first
            if person is not None:  # Check if we actually got someone
                return True
        return False

    def get_needy_girlfriend():
        #temp_list = []
        #if time_of_day == 3: 
        #    for person in known_people_in_the_game():
        #        if person.has_role(girlfriend_role) and person.novelty == 100: # and person.is_available:
                    #A gf who have 100 novelty havent had sex for at least a week..
        #            temp_list.append(person)
        return get_random_from_list([x for x in list_of_people if (x.has_role(girlfriend_role) and x.novelty == 100)])

    def busy_kitchen_requirement():
        return ((mom.is_mc_father and mom.pregnancy_is_visible) and (lily.is_mc_father and lily.pregnancy_is_visible) and mom.location == kitchen and time_of_day == 3 and lily.is_available)

    def cs_thanks_requirement():
        person = get_mama()
        if person is not None:  # Check if we actually got someone
            return (child_support_enabled and day % 7 == 5)
        return False

    def get_mama():
        return get_random_from_list([x for x in list_of_people if x.has_child_with_mc])

    def mom_sister_exclusive_home_harem_requirement():
        # Alternative way to get Mom and Sis as girlfriends
        # They need to maxxed out love and slut and incest opinion
        # Both are pregnant
        # Hate 3some
        return ( (lily.love == 100 and lily.sluttiness == 100) and (mom.love == 100 and mom.sluttiness == 100)
            and (lily.knows_pregnant or mom.knows_pregnant 
            and lily.is_available and mom.is_available) 
            and family_prefer_incest()
            and not willing_to_threesome(lily, mom)
            and time_of_day == 4
            and not aunt_living_with_mc()
            and not (mom.has_queued_event("sleeping_walk_in_label") or lily.has_queued_event("sleeping_walk_in_label")))
        
    mom_sister_talk_action = ActionMod("Mom and Lily pregnancy talk", mom_sister_talk_requirement,"mom_sister_pregnancy_talk_label", initialization = mom_sister_snoop_initialization,
        menu_tooltip = "You overhear something from the hallway.", category="Home", is_crisis = True, is_morning_crisis = True)

    sis_help_in_kitchen_action = ActionMod("Lily a sous chef.", lily_helping_in_kitchen_requirement, "lily_helping_in_kitchen_label",  #Using ActionMod automatically adds this event to the crisis list
        menu_tooltip = "Lily helping in the kitchen.", category = "Home", is_crisis = True, is_morning_crisis = False)   #Categories include Home, Business, Fetish

    baby_shopping_child_support = ActionMod("Paying for baby supplies.", baby_shopping_requirement, "baby_shopping_support_label",
            menu_tooltip = "Your baby, your money.", category = "Mall", is_crisis = True, is_morning_crisis = False)

    needy_gf_invite = ActionMod("Needy Girlfriend.", girlfriend_needs_requirement, "girlfriend_in_need_label",
        menu_tooltip = "Satisfy your girlfriend's sex need.", category = "Mall", is_crisis = True, is_morning_crisis = False)

    busy_kitchen_action = ActionMod("Family Dinner.", busy_kitchen_requirement, "flirty_dinner_label",  #Using ActionMod automatically adds this event to the crisis list
        menu_tooltip = "Lily helping in the kitchen.", category = "Home", is_crisis = True, is_morning_crisis = False)   #Categories include Home, Business, Fetish

    thanks_child_support = ActionMod("A grateful mom.", cs_thanks_requirement, "child_support_thanks_label",
            menu_tooltip = "You are such a responsible father.", category = "Mall", is_crisis = True, is_morning_crisis = True)

    busy_kitchen_action = ActionMod("Family Exclusive Harem.", mom_sister_exclusive_home_harem_requirement, "home_harem_label",  #Using ActionMod automatically adds this event to the crisis list
        menu_tooltip = "The secret is out.", category = "Home", is_crisis = True, is_morning_crisis = False)   #Categories include Home, Business, Fetish

label mom_sister_pregnancy_talk_label():
    "You wake up. You're a little groggy, but you manage to get out of bed."
    "You grab yourself some clothes and quietly leave your room. You aren't sure if you are the first one awake or not."
    "However, as you walk by [mom.possessive_title]'s room, you hear her talking to [lily.title] inside. Her door is cracked so you take a quick peek."
    $ mom_bedroom.show_background()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(lily, position = "sitting")
    "[lily.title] is sitting on the bed while [mom.possessive_title] talks with her."
    "It seems like they are having a pretty lively conversation."
    if mom.knows_pregnant and not lily.knows_pregnant: 
    #Mom is pregnant but not lily
        if mom.is_mc_father:
        #mc is the father
            if lily_knows_about_mom(): 
            #lily knows mc is the bf
                lily "... I still can't believe it, does that made me an aunt? Or the older sister?"
                if lily.is_girlfriend:
                    mom "Well, you can also consider the baby your child too." 
                    mom "I'll be hoping you be able to help raising her up."
                else:
                    mom "Older sister, of course. It's better to keep the secret in the family."
                    lily "Oh right.."
                lily "Don't worry, Mom. You can count on me."
                mom "It can be a good preparation too, just in case..."
                lily "OMG Mom! I'm still in college!"
            else:
            #lily doesnt know
                lily "... I still can't believe it, I'm gonna be an older sister?"
                mom "Are you implying that I'm too old to have a baby?"
                mom "I'll have you know that the father is very handsome."
                lily "No no Mom, I mean you are very beautiful still. Obviously."
                lily "The age gap is more like, my soon little sister feels more like a daughter to me."
                lily "More importantly, when are you gonna bring the 'handsome' father to introduce us?"
                mom "Soon dear.. soon."
                lily "That what you said before too."
        else:
            mom "... So that's that."
            mom "Will you go shopping with me for the baby this weekend?"
            mom "Your brother will be bored to death if I drag him shopping."
            lily "Why not asking that guy? Its his child."
            mom "His wife works at the mall. It's too risky."
            mom "He already agree to pay for child support. Please?"
            lily "OMG...Fine Mom... I'll go with you."
    elif not mom.knows_pregnant and lily.knows_pregnant:
    #Lily is pregnant but not mom
        if lily.is_mc_father:
        #mc is father
            if mom_knows_about_lily(): 
            #mom knows mc is the bf
                mom "Are you sure you are fine?"
                lily "It's just morning sickness. I'll be fine in a while."
                mom "I'm gonna tell [mc.name] to pay more attention to you."
                mom "He needs to learn how to be a father better."
                lily "He is learning. He promised to go shopping for baby stuff this weekend."
                if mom.is_girlfriend:
                    mom "... I wonder if I'm too old to carry his baby as well."
                    lily "Mom?"
                    mom "I was just wondering if I should let your brother creampie me more"
                    "Theres a hint of redness on her cheeks."
                    lily "Maybe you just being unlucky. You been fucking him like rabbit too so it probably is just a matter of time, I'm sure."
                    "[mom.title]'s cheeks redden."
                    mom "You knew?"
                    lily "It hard not to when you scream so loud...everytime..."
                    "[mom.title]'s cheeks redden furiously."
                else:
                    lily "Mom?"
                    mom "Yes dear."
                    lily "Are you mad at us?"
                    mom "What? No, both of you love each other, and this baby is the prove."
                    mom "And I get to become a grandma too."
            else:
                #mom hasnt realized yet
                mom "*humming happily*"
                lily "You are awfully happy these day."
                mom "I'm about to become a grandma."
                "...The girls continues talking..."
                mom "But for God's sake, why aren't you using protection?"
                mom "Is your boyfriend working? When are you bringing him to meet me?"
                lily "Yes Mom, he isn't one of my classmates. He have a job. You'll meet him soon."
                mom "That what you said before too."
        else:
        #mc not the father
            mom "I thought I already told you to be careful when fooling around the boys."
            mom "Did you skipped your pills?"
            lily "It was by accident, Mom. I never been off pills since I'm 16."
            lily "We both got drunk at the party and didn't think its matters anyway since I'm always on birth control."
    else:
    #both pregnant
        "[mom.title] is sitting on her bed while [lily.possessive_title] talks with her."
        "It seems like they are having a pretty lively conversation."
        if (mom.is_girlfriend and lily.is_girlfriend) or had_family_threesome(): #case where they both aware your are the father 
        #WINCEST
        #TODO should be split like above, but I have no idea what to write lol
        #TODO Also, we making a huge assumption here whether these really is our child.
            mom "I still can't believe [mc.name] got both of us pregnant."
            mom "I'm almost twice his age."
            if lily.get_opinion_score("cheating on men") < 0:
                lily "I know, right? But now I can't imagined fucking anyone else. Despite him being my own brother." 
            if mom.get_opinion_score("cheating on men") < 0:
                mom "I should be mad at you for fucking your brother, but then, I'm equally guilty of fucking my own son too." 
            if mom.get_opinion_score("being submissive") > 0:             
                mom "But honestly, just listening to his voice sometimes made me wet." 
            if lily.get_opinion_score("being submissive") > 0:
                lily "OMG, yes! Especially when he gets rough during sex."
            "..."
            mom "And now we both carrying his child."
            lily "Well at least, he is being responsible, to both of us."
            "...The girls continues talking..."
            mom "...So you free to go shopping for our babies together this week?"
            lily "Yeah, wanna drag [mc.name] with us shopping too?"
            mom "Nope, he can be helpful when we buy our outfits and lingeries. But baby stuffs? Oh dear, he is helpless.."
            mom "Let's just save him the despair of it."
            mom "I already told him about it and he told me to use his card for payment."
            lily "That's settles it then."
        elif mom.is_girlfriend and not lily.is_girlfriend: 
            mom "...So you free to go shopping for our babies together this week?"
            lily "You aren't going with [mc.name]?"
            mom "Then who gonna accompany you? I didn't even get to meet him yet."
            mom "I'll speak to [mc.name] so he'll support you until you can support yourself."
            lily "Do you think he will accept it. This isn't his child, unlike your's."
        elif not mom.is_girlfriend and lily.is_girlfriend: 
            lily "...So you free to go shopping for our babies together this week?"
            mom "You aren't going with [mc.name]?"
            lily "Then who gonna accompany you? That guy's wife works at the mall, right?"
            mom "Thanks Lily. I'll ask him to wire me some money for the shopping."
            lily "That's settles it then."
        else:
            mom "It'll be interesting once they grown up. Your daughter gonna call mine aunty."
            lily "They probably just refer each other by names."
            lily "By the way, [mc.name] seems to spending more times at his office lately."
            mom "Theres 2 beautiful girls at his office, right. Stephanie and ... Sarah, I think."
            mom "You think he is dating either of them?"
            lily "Either? He probably date both if possible."
            mom "OMG No way!"
    "The girls keep talking. They keep bouncing back and forth between multiple topics."
    "They keep talking, but you decide to keep heading to the bathroom."
    if (lily.knows_pregnant and lily.is_mc_father) or (mom.knows_pregnant and mom.is_mc_father):
        "You feel somehow energetic with the soon arrival of your own child."
    $ clear_scene()
    $ lily.change_to_bedroom()
    $ mom.change_to_bedroom()
    $ mc.change_location(bedroom)
    return

label lily_helping_in_kitchen_label():
    #TODO: Cover all base
    $ the_person = lily

    $ kitchen.show_background()
    $ scene_manager = Scene()
    "As the tantalizing aroma of spices wafted through the air, my stomach growled in anticipation." 
    "Dinner preparations were in full swing, and the kitchen was a bustling hub of activity."
    $ scene_manager.add_actor(the_person, position = "walking_away")
    "[the_person.title] stood by the counter, expertly chopping vegetables."
    if mom.is_girlfriend: #technically, theres an option that we didnt tell lily about our relation so she didnt know, but I assumed most will
        #No need to pretend, so we use normal titles
        mc.name "You have a sous chef now, [mom.title]?"
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "back_peek")
        "[mom.possessive_title!c] navigated the kitchen like a maestro, orchestrating the entire cooking process."
        $ scene_manager.update_actor(the_person, position = "stand4")
        if mom.is_mc_father and mom.pregnancy_is_visible:
            the_person "You are the one that should be the sous chef."
            the_person "That's your bun in her oven."
            mom "[the_person.fname]!"
            "[mom.possessive_title!c] blushed."
            if had_family_threesome() or home_harem():
                if the_person.pregnancy_is_visible:
                    the_person "Here's another of *YOUR* bun."
                    the_person "Congratulation! Here's your grand achievement - Keeping it in the family!"
                else:
                    the_person "Soon, you'll see another bun of yours. Inside my \"oven\"."
                    the_person "You must be *sooo* proud."
            "[the_person.possessive_title!c] keeps on nagging you while helping in the kitchen."
            "You wonder if she woke up on the wrong side of the bed today."
            "You signaled [mom.possessive_title] and leave the kitchen quietly."
    else:
        mc.name "You have a sous chef now, Mom?"
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "back_peek")
        $ scene_manager.update_actor(the_person, position = "stand4")
        if mom.pregnancy_is_visible:
            the_person "Our lil sis gonna popped soon, Bro."
        else:
            the_person "I thought Mom looks a bit tired today."
        the_person "And I just got a bit of free time, so I helped."
        mc.name "Good job. Can't wait to taste dinner tonight. Need any help?"
        mom "That's fine, sweety. I think we can managed."
        the_person "Hear that? Now shoo. We having girls talk as well."
    $ scene_manager.clear_scene()
    $ mc.change_location(hall)

    return

label baby_shopping_support_label():
    #Adapted from Kaden's code
    $ the_person = get_baby_shopping_person()
    $ is_text = False
    if mc.is_at_work:
        if the_person.is_employee and the_person.is_at_office or the_person.location == mc.location:
            "As you are packing up to head home for the day you are approached by [the_person.title]."
        else:
            "As you are packing up to head home for the day you get a text from [the_person.title]."
            $ is_text = True
    elif mc.is_home:
        if the_person in people_in_mc_home():
            "As you are walking down the hallway in your house you are approached by [the_person.title]."
        else:
            "As you are walking down the hallway in your house you get a text from [the_person.title]."
            $ is_text = True
    else:
        if the_person.location == mc.location:
            "As you are wandering around you are approached by [the_person.title]."
        else:
            "As you are wandering around you get a text from [the_person.title]."
            $ is_text = True
    if is_text:
        $ mc.start_text_convo(the_person)
    the_person "I was going to head to the mall, to buy some stuff for our baby."
    the_person "Wanna come with me? Just kidding, I won't bother you to death."
    mc.name "Thanks. I'll wire you some money."
    if is_text:
        $ mc.end_text_convo()
    $ mc.business.change_funds(-500)
    return

label girlfriend_in_need_label():
    $ the_person = get_needy_girlfriend()
    $ is_text = False
    if mc.is_at_work:
        if the_person.is_employee and the_person.is_at_office or the_person.location == mc.location:
            "As you are packing up to head home for the day you are approached by [the_person.title]."
        else:
            "As you are packing up to head home for the day you get a text from [the_person.title]."
            $ is_text = True
    elif mc.is_home:
        if the_person in people_in_mc_home():
            "As you are walking down the hallway in your house you are approached by [the_person.title]."
        else:
            "As you are walking down the hallway in your house you get a text from [the_person.title]."
            $ is_text = True
    else:
        if the_person.location == mc.location:
            "As you are wandering around you are approached by [the_person.title]."
        else:
            "As you are wandering around you get a text from [the_person.title]."
            $ is_text = True
    if is_text:
        $ mc.start_text_convo(the_person)

    the_person "Hey [the_person.mc_title]! Got any plans for tonight?"
    the_person "We both have been busy lately, want to Wetflix and chill for a bit?"
    if the_person in people_in_mc_home():
        menu:
            "My room":
                mc.name "Come over to my room, I'll order takeout then we can makeout."
                $ the_person.call_dialogue("sleepover_yourplace_response")
                $ schedule_sleepover_in_story(the_person)
                $ mc.business.event_triggers_dict["your_place"] = True
            "Your room":
                mc.name "I'll bring a bottle of wine to your room tonight."
                $ the_person.call_dialogue("sleepover_herplace_response")
                $ schedule_sleepover_in_story(the_person, your_place = False)
                $ mc.business.event_triggers_dict["your_place"] = False
            "Decline the date":
                mc.name "Sorry I can't tonight. I've got other plans."
                the_person "Oh, okay."
                #Major stat hits
                $ the_person.change_love(-10)
                $ the_person.change_happiness(-10)
                if is_text:
                    $ mc.end_text_convo()
                return
    else:
        menu:
            "My place":
                mc.name "Come over tonight, I'll order takeout then we can makeout."
                $ the_person.call_dialogue("sleepover_yourplace_response")
                $ schedule_sleepover_in_story(the_person)
                $ mc.business.event_triggers_dict["your_place"] = True
            "Your place":
                mc.name "How about your place? I'll bring a bottle of wine."
                $ the_person.call_dialogue("sleepover_herplace_response")
                $ schedule_sleepover_in_story(the_person, your_place = False)
                $ mc.business.event_triggers_dict["your_place"] = False
            "Decline the date":
                mc.name "Sorry I can't tonight. I've got other plans."
                the_person "Oh, okay."
                #Major stat hits
                $ the_person.change_love(-10)
                $ the_person.change_happiness(-10)
                if is_text:
                    $ mc.end_text_convo()
                return
    if is_text:
        $ mc.end_text_convo()
    return

label flirty_dinner_label():
    #TODO: Cover all base
    $ the_person = lily

    $ kitchen.show_background()
    $ scene_manager = Scene()
    "A familiar scent of dinner cooking wafting through the air."
    "Your stomach growled in anticipation, but your eyes were drawn to something far more captivating."
    $ scene_manager.add_actor(the_person, position = "walking_away")
    $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "walking_away")
    "Both stood by the counter, visibly pregnant, their swollen bellies a testament to your virility."
    $ scene_manager.update_actor(mom, display_transform = character_center_flipped, position = "back_peek")
    "[mom.fname] turned first, her face lighting up as she saw you."
    mom "Hey [mom.mc_title], We didn't expect you home so early."        
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "[the_person.fname] followed her mother's gaze, her light blue eyes twinkling with mischief as she met yours."
    the_person "Yeah, we thought you'd be out longer. Dinner's almost ready, though."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She leaned against the counter, her hands resting on her rounded belly."
    "You couldn't help but admire the way she carried herself."
    mc.name "What are you two making?"
    $ scene_manager.update_actor(mom, display_transform = character_center_flipped, position = "stand5")
    mom "Surprise!"
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[the_person.fname] giggled, pushing herself off the counter."
    the_person "Come on, [the_person.mc_title]. Help us finish up."
    mom "Alright, you two. Let's get this dinner on the table. [mom.mc_title], could you set the plates?"
    "..."
    "When the food was finally served, [mom.fname] joined them at the table, sitting beside you. [the_person.fname] took the seat across, her eyes never leaving you."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(mom, display_transform = character_left_flipped, position = "sitting")
    mom "So, how was your day?"
    mc.name "Not bad really.A lot of progress on the project I'm working on. How about yours?"
    the_person "Mom and I spent the morning shopping. We found this cute maternity dress that I think would look great."
    mc.name "Really? Maybe I'll have to see it later."
    "..."
    "(You spend times just talking about everything)"
    
    $ scene_manager.clear_scene()

    return

label child_support_thanks_label():
    #Adapted from Kaden's code
    $ the_person = get_mama()
    $ is_text = False
    if mc.is_at_office:
        if the_person.location == mc.location:
            "You are busy at work when you are approached by [the_person.title] carrying your daughter."
            the_person "Look Pumpkin, it's your daddy. So hard at work even on weekends."
            mc.name "My little Princess... Come to daddy~"
            "Her eyes looks at you suspiciously."
            "..."
            "You stopped your work to spend precious time with your family."
            mc.name "Do you need anything?"
            the_person "The bank already credited my account this morning."
        else:
            "You are busy at work when you get a text from [the_person.title]."
            $ is_text = True
    elif mc.is_home:
        if the_person in people_in_mc_home():
            "As you are walking down the hallway in your house you heard happy voices and baby giggling."
            "You approached it and was greeted by a warm scene of [the_person.title] playing with your daughter."
            the_person "Look Sweetie, It's Da-Da."
            mc.name "My little Princess... Come to daddy~"
            "Her eyes glitters in excitement seeing you."
            "..."
            "You spent precious time with your family."
            mc.name "Do you need to buy anything for her? I could drop at the mall later."
            the_person "There's no need for that. You are busy as it is."
            the_person "I've checked my account and it's already banked in this morning."
        else:
            "As you are walking down the hallway in your house you get a text from [the_person.title]."
            $ is_text = True
    else:
        if the_person.location == mc.location:
            "As you are wandering around, you saw [the_person.title] carrying your daughter."
            "She saw you as well and quickly approached you."
            the_person "Look Pumpkin, do you know who this is? It's your Da-Da."
            mc.name "My little Princess... Come to daddy~"
            "Her eyes looks at you suspiciously."
            "..."
            "You spent precious time with your family."
            mc.name "Do you need any money to buy her stuffs?"
            the_person "The bank already credited my account this morning."
        else:
            "As you are wandering around you get a text from [the_person.title]."
            $ is_text = True
    the_person "Thanks. It means a lot. I was thinking of shopping and that is definitely more then enough."
    the_person "Wanna come with me? Just kidding, I know you hate shopping."
    mc.name "Haha, sorry. Have fun shopping."
    if is_text:
        $ mc.end_text_convo()
    return

label home_harem_label():
    $ hall.show_background()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom, display_transform = character_center, position = "stand4", emotion = "angry")
    $ scene_manager.add_actor(lily, display_transform = character_left_flipped, position = "sitting", emotion = "angry")
    "Their voices can be heard from the front door. Curious, you entered the house stealthily.The front door clicked shut with a softness that felt criminal against the rising tide of voices in the living room."
    mom "—think I haven’t noticed?"
    mom "The unbuttoned top during breakfast? Or how your skirt rides up just enough to make me wonder if you’re even wearing anything underneath?  Don’t play naive with me, Lily. It doesn’t suit you."
    lily "Me?"
    lily "How about you? Since when do you parade around the house in lace lingerie? Black lace, no less. You think I didn’t notice how it peeks out from under your robe? Or the way you’ve been lingering in front of the mirror lately? Who are you trying to impress, Mom?"
    mom "Watch your tone... I am still your mother."
    lily "Then act like it! Stop pretending you don’t know exactly what you’re doing. You’re not being subtle. You’ve been parading around here like... like..."
    mom "Like a woman who is happy? Is that so impossible for you to conceive? That someone might find me desirable?"
    lily "I know who finds you desirable... I see the way he looks at you when he thinks no one’s watching. It makes me sick."
    mom "I don’t know what you’re talking about..."
    lily "Don’t you? You think I’m blind? You think I'm that clueless? The secret glances between the two of you?"
    lily "You are always wary of me, haven’t you? You couldn’t stand that he might want me, too."
    "The silence that followed was absolute, a vacuum that sucked all the sound from the world. You risked a glance around the corner."
    "They are facing each other, two beautiful, furious mirrors. [mom.fname], her [mom.hair_description] perfectly framing her face, her knuckles white where she gripped the back of the sofa."
    "[lily.fname], her [lily.hair_description] a chaotic contrast, her arms crossed over her chest in a gesture that was suddenly, unmistakably protective."
    "[mom.fname]’s eyes narrowed, her gaze dropping from Lily’s furious face down her body, lingering on the way her daughter’s hands cradled her own stomach. A dawning horror washed over her features, erasing the anger, replacing it with something pale and ghastly."
    mom "Lily, tell me I’m wrong."
    "[lily.fname]’s eyes flickered, a flash of defiance quickly giving way to uncertainty. She tightened her arms around herself, as if shielding the truth—or perhaps the life growing inside her—from her mother’s piercing stare."
    "The air between them grew heavier, charged with a truth neither one wanted to fully acknowledge."
    lily "Sigh..."
    lily "You’re not wrong."
    $ scene_manager.update_actor(mom, display_transform = character_center, position = "sitting", emotion = "sad")
    "[mom.fname]’s breath hitched, her hand flying to her mouth as if to stifle a gasp. Her eyes darted to [lily.fname]’s midsection again, then back to her face, searching for denial, for a reason to disbelieve what she was seeing."
    "But the truth was undeniable, written in the curve of [lily.fname]’s body, in the protective stance of her hands, in the way her youthful defiance couldn’t quite mask the fear beneath."
    mom "Oh my God..."
    lily "Don’t act so surprised, you’re the one who taught me how to fight for what I want."
    "[mom.fname]’s eyes, wide with disbelief, flicked down to her own waistline, to the slight, soft curve she’d been trying to hide as well."
    "The realization hung heavy in the air, unspoken but undeniable."
    "Both speechless."
    "The rivalry, the new clothes, the scent of perfume on the air—it all snapped into a horrifying, perfect focus."
    mom "You’re..."
    mom "My God. You’re pregnant. With his child."
    "Silence."
    lily "So are you."
    "Hell's freezing."
    mom "This is crazy... but...."
    mom "..."
    lily "I can't hear you."
    mom "I'm saying... I am not giving him up. This..."
    "She gestured vaguely at her own stomach..."
    mom "...changes nothing about how I feel. It only makes it more... permanent."
    lily "And you expect me to give up?"
    lily "This is my baby. With him. I’m not stepping aside so you can play happy family with my child’s father."
    mom "No! Lily, No. I’m not asking you to step aside. We are both unwilling to lose him. That is perfectly clear to me."
    mom "Therefore, we need rules. Structure. To prevent... overlap. Or conflict."
    lily "You mean to prevent us from getting jealous of each other?"
    mom "I mean to prevent this household from becoming untenable..."
    lily "Go on."
    mom "We’ll share him— his time, his attention, his... love . We establish boundaries. We are adults. We can be civilized about this."
    lily "Civilized? Mom, you got impregnated by your son! And he impregnated me too, his own damn sister! There is no handbook for civilized behavior here!"
    mom "Then we will write it! We will write the damned handbook!"
    $ scene_manager.update_actor(mom, display_transform = character_center, position = "stand4", emotion = "default")
    mom "Do you love him?"
    lily "Huh?"
    mom "It’s a simple question. {i}Do you love him?{/i} Or was he just a way to prove you could take something I wanted?"
    lily "That’s not fair."
    mom "None of {i}this{/i} is fair, Lily! Answer me."
    lily "Yes, I {i}very much{/i} love him."
    "[mom.possessive_title!c] nodded slowly, a strange look of resignation and understanding on her face."
    mom "So do I."
    mom "Then let's do this. We both share him. With {i}one{/i} rule."
    lily "Which is...?"
    mom "The bedroom. Our bedrooms will be our sanctuaries, where we can keep pretending that he is ours alone."
    "[mom.possessive_title!c]’s tone was final, brooking no argument."
    mom "What happens behind your closed door is your business. What happens behind mine is mine. We do not interfere. We do not compare. We do not... share our bed."
    mom "That means schedules."
    mom "I want to keep you as my daughter, not my love rival."
    "[lily.possessive_title!c] was silent for a long moment, considering. The rivalry was still there, simmering just beneath the surface, but it was being overlaid by a new, desperate pragmatism."
    lily "So, we just… what? Book appointments to be with him?"
    lily "Do we call his secretary?"
    if mom_our_secretary():
        lily "Oh wait, you are {i}his{/i} secretary!"
    mom "Lily! I am being serious."
    lily "So am I! I’m just trying to understand. What if I really need to see him on a night that’s {i}your night{/i}?"
    mom "Then you jump at him at the next possible moment..."
    mom "Look, I don't like this anymore than you do. But this is a compromise."
    mom "Beside, it's still similar, isn't it? We just no longer to keep it a secret from each other."
    lily "Hmm... Fine."
    "You breathe a sigh of relief. You always wonder how you are going to broach the subject to them one day."
    $ scene_manager.update_actor(lily, display_transform = character_left, position = "kissing")
    $ scene_manager.update_actor(mom, display_transform = character_left, position = "walking_away", z_order = 10)
    "They embraced each other in relief. Oh how you wished you are included in the family hug..."
    $ scene_manager.add_actor(mom, display_transform = character_center, position = "sitting", emotion = "default")
    $ scene_manager.add_actor(lily, display_transform = character_left_flipped, position = "sitting", emotion = "default")
    mom "Now, let's discuss with the devil responsible for this."
    "Uh-Oh."
    "You can see [mom.possessive_title] pull out her phone. And you can be sure who she is calling."
    "Huge breath. You entered."
    "Their heads snapped toward you in perfect, horrifying unison."
    mom "You are home...You've been listening!"
    "You nodded."
    $ scene_manager.add_actor(lily, display_transform = character_left_flipped, position = "sitting", emotion = "angry")
    $ scene_manager.add_actor(mom, display_transform = character_center, position = "sitting", emotion = "angry")
    lily "Why?"
    lily "Why would you do this to us?"
    "(You sure as hell can't say you've drugged them... That would be suicide.)"
    mom "Was it a game?"
    mom "Was it some... some conquest? Her to prove you could have someone young and beautiful? Me to prove you could still tempt someone older? Was that it?"
    mc.name "(yes)"
    lily "From where we’re sitting, it looks an awful lot like you were playing us against each other. Seeing how far you could go."
    mc.name "(Damn they are sharp!)"
    mc.name "I wasn’t— "
    mom "That’s it, isn’t it? You had us both and you... you just couldn’t choose."
    mc.name "(Who said anything about choosing...Gotta catch'em all~)"
    mc.name "It wasn’t about choosing..."
    mc.name "(Here we go... YOLO!)"
    mc.name "It was about.. what you both needed. What I wanted to give you."
    "You look at [mom.fname]."
    mc.name "That time you forget to pay the water bill, I couldn’t stand seeing you bear everything alone. You’ve always been so strong, so capable, but I saw the weight of it all crushing you."
    mc.name "I wanted to help, to ease that burden. "
    mc.name "But the more I tried, the more I fell for you— for the way you faced every struggle head-on, for the vulnerability you never showed anyone else. "
    mc.name "It wasn’t just desire; it was admiration. It was love."
    "[mom.possessive_title!c] gasps and covers her mouth."
    "You shifted your gaze to [lily.fname]."
    mc.name "When that guy broke your heart, you are so devastated. I just wanted to console you. I couldn’t stand seeing you hurt like that. "
    mc.name "I wanted to shield you from ever feeling that pain again. But then... it became more. "
    mc.name "You weren’t just my little sister anymore. You were this incredible, fierce person who deserved someone who would cherish you. And I couldn’t stop myself from wanting to be that person."
    "The room felt heavy with their silence, their breaths shallow, their eyes locked on me."
    mc.name "This wasn’t a game..."
    mc.name "(It is.)"
    mc.name "This wasn’t about conquest or proving anything. It was about you. {i}Both of you{/i}. And I know that doesn’t make it right, but it’s the truth."
    "[mom.fname]’s lips trembled, her composure slipping further as she processed my words. [lily.fname] stared at me, her expression unreadable, but the anger in her eyes had softened, replaced by something far more complicated. "
    lily "It was kinda inevitable, don’t you think? Living in the same house. Little things add up. What were you thinking?"
    mc.name "(I was hoping I could drug you gals enough that these doesn't matter.)"
    mc.name "Every... single... damn... minutes. I dreaded this moment. Especially -"
    "You shifted your gaze to their stomach."
    mom "Well, secret's out now."
    lily "So what happens next?"
    mom "That depends on him."
    mom "You've listened to our conversation. The bedroom rule is non-negotiable."
    mc.name "(For now.)"
    mom "This house...What will it be? What is your plan with this family?"
    mc.name "I can’t fix the past...I can’t undo what I’ve done, or the hurt I’ve caused. And I won’t stand here and insult your intelligence by pretending any of this is simple."
    mc.name "But I meant every word I said..."
    mc.name "What I feel for you, [mom.title]... it’s real. It’s the kind of love that sees the strength in someone and wants to be their shelter."
    mc.name "And you, [lily.title], it’s real, too. It’s a love that saw your fire and wanted to be the one you trusted with your heart."
    mc.name "You both agreed to share, which is all that matters to me. I was dreading if one of you forced the other to surrender."
    lily "So..."
    mc.name "I’m not planning to give up on any of you. And although I can't marry both of you, I can still become your boyfriend."
    mc.name "We will raise our children together. I will be the man who comes home to you, who supports you, who loves you. A husband and a father."
    mc.name "If you’ve both decided that my roaming between your bedrooms is the way to maintain our family's bond, then I will embrace that role."
    mc.name "And my room is unlocked. Should you feel a sudden desire for me in the middle of the night, I’ll be there by your side."
    mom "Do you really wish for this?"
    mom "Two wives. Your father ran with his second."
    mc.name "I'm not him."
    lily "This is insane. Can you keep up with us both?"
    mc.name "I sort of did, didn't I? Have you been dissatisfied before with me?"
    "She stuck her tongue out."
    "You reach out both hands to them."    
    $ scene_manager.add_actor(lily, display_transform = character_left_flipped, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(mom, display_transform = character_center, position = "sitting", emotion = "happy")
    "[lily.fname] paused for just a moment before leaping forward to embrace you. "
    "[mom.fname]’s hand, smooth and cool, reached out tentatively. You pulled her closer too and she responded by hugging you tightly."
    $ scene_manager.update_actor(lily, display_transform = character_center, position = "kissing")
    $ scene_manager.update_actor(mom, display_transform = character_center_flipped, position = "kissing", z_order = 10)
    mc.name "(Well, I got the hug I wanted earlier.)"   
    $ scene_manager.add_actor(lily, display_transform = character_left_flipped, position = "sitting", emotion = "happy")
    $ scene_manager.add_actor(mom, display_transform = character_center, position = "sitting", emotion = "happy")
    mom "By the way, everything we talked here, stays private."
    mom "To outsider, we are just a normal family."
    mom "Especially with Rebecca. Agree?"
    mc.name "Yes."
    lily "She's sharp. She will be suspicious."
    mom "We'll cross the line when it comes. Until then, zip it!"
    $ clear_scene()
    $ mc.change_location(hall)


    python:
        mc.business.event_triggers_dict["exclusive_home_harem"] = True
        mom.event_triggers_dict["mom_girlfriend_sister_knows"] = True
        lily.event_triggers_dict["sister_girlfriend_mom_knows"] = True
        lily.add_role(girlfriend_role)
        lily.increase_opinion_score("polyamory")
        mom.add_role(girlfriend_role)
        mom.increase_opinion_score("polyamory")
    return