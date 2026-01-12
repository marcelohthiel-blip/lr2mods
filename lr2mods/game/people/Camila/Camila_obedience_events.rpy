# Camila's obedience events involve unlocking new and interesting goals for MC
# At first, they are normal goals, but eventually evolve into sexual goals.
# Nora gets introduced to Camila through her love story if Camila is far enough along in this storyline.

#Obedience Labels.
label camila_obedience_new_goals_label(the_person):    #100 obedience
    $ the_person.story_event_log("obedience")
    mc.name "Glad to see you here again. How have you been?"
    the_person "Pretty good. You?"
    mc.name "I'm doing well. You seem calmer around me, more together somehow. I like it."
    "She looks a little embarrassed, but seems to realize the truth of your statement."
    "[the_person.possessive_title!c] shrugs and engages with you."
    the_person "You're not wrong. I guess that is because I feel a bit more comfortable around you."
    "Considering how independent and rebellious she was when you first met her this is a real sign of the effort you put into [the_person.possessive_title]."
    mc.name "That's great! I was hoping you would be free to talk about further developing my business and my goals?"
    the_person "Yes! Each goal you achieve helps your company grow and gives you confidence to face new challenges."
    mc.name "I have been responding to these little accomplishments.  They definitely help me and improve my work. So do you have any more advice?"
    the_person "Well, we have been hanging out a lot and have been paying attention to you. Professionally, of course."
    "[the_person.possessive_title!c] smiles and winks at you in a flirtatious but entirely professional way."
    the_person "I don't know why but, it's nice being able to talk to you. Something about you puts me at ease."
    "Considering how much time we have spent together it would be more suprising if she hadn't noticed something."
    the_person "You know I love to dance right?  Dancing is a window to how we approach problems both in life and in work."
    the_person "And what I can see with you is that you are a excellent lead!  If we were to dance here in the mall I  can see myself following you lead in that dance.  Before I doubt I would have been comfortable and able to follow."
    the_person "This can help you in work.  As you become a better leader your employee's become better followers of where you lead."
    the_person "It is a give and take.  One where you are giving direction, purpose, and motion to the company."
    the_person "Your staff in turn get better and receiving your lead."
    mc.name "You are absolutely right with that. My staff have been getting better at receiving my lead."
    "[the_person.possessive_title!c] seems to ignore your innuendo."
    the_person "So, do you want to talk about your current goals and maybe change one?"

    $ add_camila_obedience_new_personal_goals_action()
    $ camila.progress.obedience_step = 1
    return

label camila_obedience_new_personal_goals_label(the_person):    #120 Obedience
    $ the_person.story_event_log("obedience")
    "In this label, we convince Camila to help us come up with new personal goals."
    "She walks MC through the process, encourages him to learn what he wants to do with his life and what he wants to accomplish."

    $ add_camila_obedience_sexual_goals_intro_action()
    $ camila.progress.obedience_step = 2
    return


label camila_obedience_sexual_goals_intro_label(the_person):   #140 obedience
    "In this label, Camila works with MC to come up with new sexual goals. This level of sexual goals a will be fairly tame."
    $ add_camila_obedience_tit_fuck_action()
    $ camila.progress.obedience_step = 3
    return

label camila_obedience_tit_fuck_label(the_person): #160 obedience. Previously sluttiness trigger.
    $ the_person.draw_person()
    $ the_person.story_event_log("obedience")
    "You step up to [the_person.possessive_title]. She smiles as you approach her."
    the_person "Hey [the_person.mc_title] here to review your goals?"
    "You do want to... but you find yourself faltering for a second."
    "Setting goals, both long term and short term is important... but what really are your goals, anyway?"
    mc.name "I think so, but to be honest, I'm having trouble deciding what I even want."
    the_person "I see. Well, an exercise that might help. Let's pretend like money wasn't an obstacle. If you could do anything you wanted to right now, what would you do?"
    "You look at [the_person.possessive_title]. You think about the question for a moment... but soon your eyes drift down from her face..."
    "Her chest... her belly... her hips..."
    $ mc.change_locked_clarity(10)
    "You close your eyes."
    "Try as you might, you can't get images of her sexy body out of your head."
    the_person "That's it. Visualize what you want. What drives you? What gets you out of bed every morning? Your endgame?"
    "Try as you might, you can't get the women in your life out of your brain. Maybe... all the money... the company... is really all about?"
    "Having the women in your life serve your needs, physically, emotionally, sexually..."
    $ mc.change_locked_clarity(30)
    "Maybe it is time to just embrace it. There's nothing wrong with that, right? Any guy in your position would do the same thing."
    "You open your eyes and look at [the_person.possessive_title]. Your eyes are immediately drawn to her tits."
    the_person "That's it. Can you envision your goal, [the_person.mc_title]?"
    "You look down at [the_person.title]'s ample chest. You can imagine your cock sliding between them, her smooth flesh caressing you."
    $ the_person.change_obedience(3)
    mc.name "I can envision it... and I can almost feel it."
    "She gasps when she realises you are staring right at her chest."
    #TODO increase her sluttiness with new sluttiness score.
    mc.name "[the_person.title]... would you follow me to someplace more private?"
    the_person "Oh my... I suppose..."
    call mc_change_to_private_location(the_person) from _call_mc_change_to_private_location_camila_obedience_tit_fuck
    "You quickly duck into a side hall and find a family restroom, she joins you inside and you lock the door."
    mc.name "Take your top off."
    "You don't give her a choice in the matter, but she quickly complies."
    $ the_person.strip_outfit(exclude_lower = True)
    mc.name "I want to feel my cock between your tits, and I'm not taking no for an answer."
    the_person "Then I suppose it's a good thing I don't want to say no!"
    "You can't wait to cum all over her incredible tits."
    call get_fucked(the_person, private= True, start_position = tit_fuck, skip_intro = True, allow_continue = False) from _call_get_fucked_life_coach_tit_fuck_01
    the_person "Oh my god... that was so hot..."
    $ the_person.draw_person()
    "[the_person.title] stands up, her tits coated in your cum."
    "It felt amazing, but something also felt different."
    "You made the decision to just let yourself go, enjoy the moment, and cover her tits in cum."
    "Normally you feel like you would find yourself wishing you could have cum inside her somewhere, but this time... it doesn't matter."
    "What matters was that she did it willingly, happy to serve you and your needs, however you told her to."
    "You decide that in the future, you'll be open to cumming all over a girl's fun bags whenever the mood strikes you."
    $ tits_man_perk_unlock()
    "You have unlocked the perk 'Tits Man'! You now have the same clarity multiplier for cumming on tits as you do for creampies!"
    the_person "I'm going to get cleaned up... you should probably slip out when you can..."
    mc.name "I'll do that. Thanks for the help, [the_person.title]."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    call mc_restore_original_location(the_person) from _call_mc_restore_original_location_camila_obedience_tit_fuck
    $ add_camila_obedience_ass_man_action()
    $ camila.progress.obedience_step = 4
    return

label camila_obedience_ass_man_label(the_person):  #180 obedience
    $ the_person.story_event_log("obedience")
    "In this label, MC cums all over Camila's ass after sex. Gains the Ass Man perk."
    # $ camila.add_unique_on_room_enter_event(camila_obedience_tit_fuck)
    $ camila.progress.obedience_step = 5
    return
