#This event mimics Lab Rats 1 teamup with Nora and Stephanie
#We join the two girls at the lab as they work on one of Nora's projects.

label kaya_nora_teamup_intro_action_label(): #Use this for the first time mandatory business event
    call progression_scene_label(kaya_nora_teamup, [kaya, nora]) from _kaya_nora_teamup_scene_call_test_03
    return

label kaya_nora_teamup_action_label(the_person):    #Use this for the recurring on room entry event
    $ mc.change_location(university)
    call progression_scene_label(kaya_nora_teamup, [kaya, nora]) from _kaya_nora_teamup_scene_call_test_02
    return

label kaya_nora_teamup_intro_scene(the_group):
    $ scene_manager = Scene()
    "It is Thursday evening, and it is the first day of [kaya.title] assisting [nora.possessive_title] in her lab."
    $ mc.change_location(university)
    "You decide to swing by the university to check up on things and see how they are going. They should be about done for the day."
    "You make your way through campus to [nora.fname]'s lab."
    $ mc.change_location(university_lab)
    "You step inside, finding the door unlocked."
    $ scene_manager.add_actor(nora, display_transform = character_center_flipped, position = "walking_away")
    $ scene_manager.add_actor(kaya, position = "walking_away")
    nora "So, by splitting the reactants first we can better control the reaction by introducing them to each other slowly..."
    kaya "Yeah, that makes sense to do it that way."
    $ scene_manager.update_actor(nora, position = "back_peek")
    "[nora.possessive_title!c] notices you approaching."
    nora "Ah, hello [nora.mc_title]."
    $ scene_manager.update_actor(nora, position = nora.idle_pose)
    $ scene_manager.update_actor(kaya, position = kaya.idle_pose)
    kaya "Hey [kaya.mc_title]."
    mc.name "Good evening. How'd the lab go today?"
    nora "Well, I daresay you have found me an excellent lab assistant."
    nora "It ALMOST makes up for taking [stephanie.fname] away from me. Almost."
    kaya "...[stephanie.fname]?"
    mc.name "Her previous lab assistant. She works for me now."
    kaya "ahh..."
    mc.name "In fact, I also used to assist in this very lab. Remember that?"
    "[nora.title] crinkles her nose as she looks at you."
    nora "That was a very busy summer... I'm sorry I don't recall ALL of it..."
    mc.name "Nah, it's okay. It was a very busy summer for me as well."
    mc.name "Say remember how once in a while you used to have me get drinks for everyone as a way to relax? Then we would just hang out here in the lab for a while?"
    nora "Yes. Work hard, play hard, as [stephanie.fname] used to say."
    mc.name "Want to hang out for a bit? I'll treat for the drinks this time."
    nora "That IS tempting... but unfortunately I've made other commitments, I need to be out of here on time tonight."
    nora "But if you swing by again another time, I could keep my Thursday evenings clear."
    mc.name "Hmm... okay. Would you be up for that once in a while, [kaya.title]?"
    kaya "I could. Just once in a while though, I don't want to get home too late..."
    nora "Alright. I'll have you know I've grown fond of a particular sparkling green tea they have started to serve at the cafeteria here."
    kaya "Ohhh, that does sound good..."
    nora "You should try it. Alright you two, I DO need to be off, and I DO need to lock the lab up behind me."
    mc.name "I kind of want to try it too... [kaya.title], want to get one and I'll walk to you home?"
    kaya "Oh! Sure!"
    "[nora.possessive_title!c] gives you a look. For a moment, it feels like her eyes pierce into you, laying bare your plans of corrupting the two girls with your serums..."
    "You wonder how much of that summer she really remembers, and if she has connected the dots back to you and your serum business now."
    $ scene_manager.update_actor(nora, position = "standing_doggy")
    "But the moment passes. She turns to gather her things from her desk."
    "[kaya.title] appears to be ready, as she quickly grabs a back pack."
    kaya "Let's go!"
    $ scene_manager.update_actor(nora, position = nora.idle_pose)
    nora "Goodbye, [kaya.fname] I'll see you next week."
    kaya "Bye professor!"
    $ scene_manager.remove_actor(nora)
    $ mc.change_location(coffee_shop)
    "You walk with [kaya.possessive_title] along the quad to the cafeteria. Thankfully you manage to get in just before it closes and get two sparkling green teas."
    $ mc.change_location(downtown)
    "You are chatting a bit with [kaya.title] as you start to walk her home."
    mc.name "So, how was your first day as a lab assistant?"
    kaya "Ahh, it went great I think. It was really interesting, learning about some of the compounds that Professor [nora.fname] has been working on."
    mc.name "Yeah?"
    kaya "Yeah... She told me though umm... I'm not really supposed to talk about them."
    mc.name "Oh, did she?"
    kaya "Yeah. And she told me about someone SPECIFICALLY I'm not supposed to share with."
    mc.name "Is that so?"
    kaya "Yeah. I was kind of surprised at first... but she seemed really serious about it."
    "You take a few more steps in silence."
    kaya "You and her... you have some kind of history together, I take it?"
    mc.name "Yes... I'm not sure how I would describe it, to be honest."
    mc.name "It is a professional relationship at this point... almost a bit competitive... but also cooperative."
    mc.name "Sometimes in the academic setting, she runs into issues that she needs some assistance with."
    mc.name "Subjects that require study, but that she can't do at the school due to bureaucracy."
    kaya "Hmmm... yeah that makes sense..."
    "A few more steps."
    kaya "There were some things that... I... I don't really understand..."
    mc.name "Oh?"
    kaya "Yeah... like... AH! I'm doing it!"
    kaya "I'm not supposed to talk about it!"
    mc.name "It's okay. Whatever it is, you don't need to tell me about it."
    kaya "Right. She said it would make more sense as I spend more time there."
    kaya "And you. She said you would help it make more sense over time?"
    kaya "I don't know. I almost got the feeling like she wanted you to swing by the lab more often too."
    "Hmmm... [nora.possessive_title] may indeed have some sort of ulterior motive for accepting [kaya.title] as her lab assistant, at your recommendation."
    kaya "Ah, anyway, I'm just happy to be back in class, and she seems like a great mentor in the field."
    "You continue until you get to her apartment."
    $ renpy.show("Apartment Entrance", what = bg_manager.background("Apartment_Lobby"), layer = "master")
    "When you get to the door, she turns to you."
    kaya "Anyway, it was great to hang out with you again today! Who knew that the creepy guy hitting on me at the coffee shop would have so many useful connections!"
    "She gives you a quick wink. Her wit is quick, but often with a barb of truth worked in."
    "She appears to be waiting for you to do something, and you quickly realise what it is when you notice her eyes break contact with with yours and flicker down to your lips."
    $ scene_manager.update_actor(kaya, position = "kissing")
    "You move close to her and she puts her arms up. You pull her close and start to kiss."
    "Her tongue eagerly slides out and meets yours. She playfully teases you bit, the moves her head sideways a bit and opens wide."
    $ mc.change_arousal(25)
    $ mc.change_locked_clarity(20)
    "You hands start to drop down to her ass, but this time she just moans when you finally get to cop a feel."
    "Your tongue slides deep past her lips and she gently sucks on it for a few moments, her motions suspiciously similar to giving head..."
    "*CLICK*"
    $ scene_manager.add_actor(sakari, display_transform = character_center_flipped)
    "Suddenly her door opens. Her mother is standing there."
    kaya "Gah!"
    $ scene_manager.update_actor(kaya, position = "stand2")
    kaya "Mom! Wha... Why did you open the door?"
    sakari "[kaya.fname]! You didn't tell me you were bringing your boyfriend over tonight!"
    if kaya.is_girlfriend:
        kaya "Mom! I told you not to... ahh!"
    else:
        kaya "Mom! He's not my boyfriend he's just... ahh!"
    kaya "How did you even know we were out here!?! Again!?!"
    "[kaya.possessive_title!c] looks completely flustered. It is actually a little bit funny."
    sakari "You're the one who helped me install the doorbell camera, daughter."
    kaya "Aaaggghhhhh...."
    "She sighs in exasperation. Then looks at you."
    mc.name "It's good to see you again [sakari.title]."
    sakari "Same, although not as good for me as it was for her I think."
    "Ahhhhh so the quick wit runs in the family."
    kaya "Oh my god... I... I'm sorry, I'll see you later, okay?"
    mc.name "Of course."
    sakari "Take care now, [mc.name]."
    $ scene_manager.update_actor(kaya, position = "walking_away")
    $ scene_manager.update_actor(sakari, position = "walking_away")
    kaya "Mom! I mean... even if you see me on the camera... can't you just let me say goodnight..."
    $ scene_manager.clear_scene()
    "The door closes behind [kaya.possessive_title] and her mother."
    $ mc.change_location(downtown)
    $ mc.location.show_background() # force redraw of background
    "You step out of the apartment building and out onto the street."
    "So, it seems that [kaya.title] and [nora.possessive_title] will be together in the lab every Thursday, and in the evenings you could hang out with them."
    "Refreshments would be an easy way to slip them some serums. You remember what it was like last summer when you had similar flings with [nora.fname] and [stephanie.fname]..."
    "It seems like a good opportunity to hang out with [kaya.possessive_title] in general though, and maybe learn more about what is going on with her mother."
    "You know that she is having some health issues, but you don't really know the details."
    "For now though, the sun is setting and night will be here soon."
    return

label kaya_nora_teamup_intro_0(the_group):
    "This is the end of the current story line."
    "More in a future update."
    return

label kaya_nora_teamup_study_choice(the_group):
    # old label can be removed
    return

label kaya_nora_teamup_labwork_choice(the_group):
    return

label kaya_nora_teamup_exit_scene(the_group):
    return
