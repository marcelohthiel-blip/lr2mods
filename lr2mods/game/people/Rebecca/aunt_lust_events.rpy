init 10 python:
    def get_aunt_drunk_cuddle_outfit():
        night_clothes_sexy = Outfit("Sexy Night Clothes")
        night_clothes_sexy.add_upper(nightgown_dress.get_copy(),colour_pink)
        night_clothes_sexy.add_lower(cute_lace_panties.get_copy(),colour_pink)
        night_clothes_sexy.add_feet(thigh_highs.get_copy(), colour_pink)
        night_clothes_sexy.add_feet(high_heels.get_copy(), colour_pink)
        return night_clothes_sexy

label aunt_drunk_cuddle_label():
    python:
        scene_manager = Scene()
        the_person = aunt
        mc.change_location(kitchen)
        scene_manager.add_actor(the_person, the_person.planned_outfit, position = "sitting")
        scene_manager.add_actor(mom, mom.planned_outfit, position = "sitting", emotion = "happy", display_transform = character_center_flipped)
        the_person.story_event_log("slut")

    "Before you go to bed, you come out into the kitchen to get a drink of water. [mom.possessive_title!c] and [the_person.title] are sitting there, drinking some wine."
    "It is pretty clear from their conversation that they have both had a lot to drink. They are cracking dirty jokes to each other."
    the_person "... So then I said, it's okay my partner is no good, I've got a good hand!"
    "[mom.title] laughs at [the_person.possessive_title]'s joke."
    if aunt.get_destination() == aunt_bedroom:
        mom "Ah that's too funny. Oh hi [mom.mc_title], your aunt and I were just having a few glasses of wine. You want some?"
        mc.name "No thanks, I'm just grabbing a glass of water."
        "[mom.possessive_title!c] looks at the clock and realises how late it is."
        mom "Oh my, it is already so late!"
        "She looks over at your aunt."
        mom "I... I didn't realise... should we get you a cab ride home?"
        the_person "Oh, that's okay. Maybe I could just crash on your couch again? For old times sake?"
        mom "Oh, of course! You're always welcome to it."
        "[mom.title] finishes her glass, then stands up."
        mom "Well, I'd best get ready for bed. Goodnight!"
        $ scene_manager.update_actor(mom, position = "walking_away")
        the_person "Good night Jen!"
        mc.name "Night Mom."
        $ scene_manager.remove_actor(mom)
    else:
        mom "Ah that's too funny. Oh hi [mom.mc_title], your aunt and I were just having some wine before bed. Would you like some?"
        mc.name "No thanks, I'm just grabbing a glass of water."
        "[mom.possessive_title!c] looks at the clock and realises how late it is."
        mom "Oh my. Yeah I'd better get to bed too. Good night!"
        $ scene_manager.update_actor(mom, position = "walking_away")
        the_person "Good night Jen!"
        mc.name "Night Mom."
        $ scene_manager.remove_actor(mom)
    the_person "Hey [the_person.mc_title], would you get me a glass of water too? I've had a LOT of wine and water helps keep you from getting hungover..."
    mc.name "Sure thing."
    $ scene_manager.update_actor(the_person, position = "default")
    "You pour two glasses of water and hand one to [the_person.possessive_title]."
    if aunt.get_destination() == aunt_bedroom:
        the_person "It is good to see you again, [the_person.mc_title]. It was so nice of you and your mom to let [cousin.fname] and I stay here for a while."
        mc.name "Of course. You are family, and it was worth it for you two to be able to move somewhere so close by."
    else:
        the_person "It has been so nice of your family to let me and [cousin.fname] stay here for a bit. I hope we haven't been too much of a bother?"
        mc.name "Of course not. You are family, and honestly it is nice having you close by."
    the_person "That's sweet of you to say. Well, goodnight!"
    mc.name "Night."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title!c] turns and walks out of the kitchen. However, a moment later you hear a loud yelp and the sound of glass breaking. You run into the living room."
    $ aunt_apartment.show_background()
    $ scene_manager.update_actor(the_person, position = "doggy")
    "[the_person.title] is on the floor on her hands and knees. Her water glass is shattered on the floor next to the couch, and the couch is soaked."
    mc.name "Are you okay?"
    the_person "I'm sorry! I slipped..."
    $ scene_manager.update_actor(the_person, position = "default")
    "You quickly help her up."
    the_person "I'm so sorry... oh no the couch is soaked..."
    "She walks over to the couch and starts picking up the pieces of glass."
    the_person "I'll pay for the glass! I didn't mean to..."
    mc.name "It's okay, it's just a glass. I'm glad you aren't hurt."
    "You help [the_person.possessive_title] pick up the glass off the floor and grab a towel that you lay down on the couch."
    the_person "Ahh, I guess I'll just be a little wet tonight."
    mc.name "Don't be crazy. You can sleep in my bed tonight."
    the_person "Oh my, I don't want to impose..."
    mc.name "You aren't. It's fine [the_person.title]. You would never get a decent night's sleep out here!"
    the_person "Well... okay... I'll go change into my pyjamas..."
    $ scene_manager.remove_actor(the_person)
    "[the_person.title] grabs a couple things out of her suitcase and heads to the bathroom. You head to your room and quickly straighten up a bit."

    $ the_person.add_situational_slut("Drunk", 5, "More than a little tipsy.")
    $ mc.change_location(bedroom)

    "After a minute, [the_person.possessive_title] knocks on your door, then slowly enters."
    $ scene_manager.add_actor(the_person, the_person.personalize_outfit(get_aunt_drunk_cuddle_outfit()))
    the_person "I appreciate this [the_person.mc_title]... sometimes I get a little clumsy when I've had a couple drinks..."
    mc.name "It's fine, really!"
    $ scene_manager.update_actor(the_person, position = "missionary")
    "[the_person.title] lays down in your bed and starts to get comfortable."
    mc.name "I'm gonna go check the closet, pretty sure we have a sleeping bag or something in there."
    the_person "Huh? What do you need a sleeping bag for?"
    mc.name "I'll just sleep on the floor, I don't want..."
    the_person "No! Absolutely not. There's more than enough room here for both of us."
    mc.name "I don't want it to be awkward..."
    "[the_person.title] chuckles and shakes her head."
    the_person "[the_person.mc_title], it's just me, your aunt! It'll be fine. It might even be kind of nice... I haven't shared a bed with someone since your uncle..."
    "There is a bit of an awkward silence."
    the_person "It's nonsense. Now get in!"
    mc.name "Okay... it's okay... I usually just sleep in my underwear..."
    the_person "Whatever you need to feel comfortable!"
    "You take your shirt off, then undo your belt and slide your pants down. You can't help but notice [the_person.possessive_title] watching you, her eyes glancing down at your crotch..."
    $ the_person.change_slut(2)
    $ mc.change_locked_clarity(10)
    "You slide into bed next to her. You have to admit, the heat of her body is kind of nice. [the_person.title] rolls over on her side, her back facing you."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    mc.name "Goodnight."
    the_person "Goodnight..."
    "After a few minutes, [the_person.possessive_title] fidgets around a bit then asks you."
    the_person "Hey... could you... you know... cuddle up with me?"
    mc.name "You... want me to be your big spoon?"
    the_person "Ahhh, sorry... that's silly..."
    "Before she can say anymore, you decide to do it anyway. You slide over behind her, putting your arm over her and pushing your body up against hers."
    the_person "Ahhh... that's nice. I haven't had a man hold me like this in so long..."
    $ mc.change_locked_clarity(10)
    "You lay there, holding [the_person.possessive_title] close for a while. However, soon the close proximity with her makes your loins start to stir."
    "You try to will it down, but it's no use."
    "Soon, you have a full–fledged erection, pressing against [the_person.title]. There's no way she doesn't feel it."
    if the_person.sluttiness < 15:
        "After a while she turns her head back to you."
        the_person "Ahh... I'm sorry, I didn't realise... anyone still thought I was..."
        mc.name "[the_person.title] I'm sorry I didn't mean to it just happened..."
        the_person "It's okay! A young, virile man like you... I shouldn't be surprised."
        "You push your hips against her, grind yourself against her ass for a moment. She gasps, but quickly puts a stop to it."
        the_person "I'm sorry, that's enough for tonight..."
        "You roll on your back. It takes a while for your erection to finally subside, but you finally manage it and fall asleep."
        $ the_person.change_slut(3)
    else:
        "After a while she turns her head back to you."
        the_person "Ahh... I'm sorry, I didn't realise... anyone still thought I was... sexy..."
        "You start to apologise, but to your surprise, you feel her ass push back and start to grind against you."
        the_person "You're such a young... sexy... virile man... it's okay..."
        $ mc.change_locked_clarity(15)
        "You groan and start to grind your hips against hers. The curves of her ass feel amazing, your cock straining against your underwear as you grind against her."
        if the_person.sluttiness < 25:  # she finishes you like this.
            "Despite the clothing in the way, the naughtiness of grinding against your aunt while she grinds against you makes the situation so hot."
            "You grind eagerly against her for a few minutes, and soon you feel yourself getting ready to orgasm."
            $ mc.change_locked_clarity(20)
            mc.name "[the_person.title]... I'm..."
            the_person "Shhh... do it honey... I want you to..."
            "[the_person.possessive_title!c]'s soothing encouragement pushes you over the edge. You gasp and moan as you dump your load in your underwear against her."
            the_person "Ahhh... that's it baby..."
            "When you finish, you are exhausted. You consider getting up and cleaning up, but it feels too good to be up against [the_person.title]'s body still..."
            $ the_person.change_slut(5)
            $ ClimaxController.manual_clarity_release(climax_type = "air", person = the_person)
            the_person "Goodnight..."
            mc.name "Goodnight..."
        else:
            "It's incredibly sexy to be up against [the_person.possessive_title], but soon the sensation of rubbing against your underwear is more frustrating than pleasurable."
            "[the_person.title] seems to be feeling the same way."
            the_person "Could you... you know... just... take it out? It feels good, but I'm getting a wedgie like this..."
            "You can't believe your ears. You quickly pull your cock out. As you are doing so, you feel [the_person.title] wiggling under the covers..."
            $ scene_manager.strip_to_vagina(person = the_person)
            "When you push up against her again, you realise she was taking her panties off! Your cock is now pushed up against [the_person.possessive_title]'s naked ass."
            $ mc.change_locked_clarity(20)
            the_person "Oh god... you feel so hard..."
            "She pushes back against you and begins to grind against you again. It feels amazing to push yourself between her soft ass cheeks."
            if the_person.sluttiness < 35:
                "You eagerly grind your crotch against her ass for a few minutes. The heat of her body feels amazing, and every little gasp and moan she makes turns you on."
                "Soon, you feel yourself getting ready to cum."
                $ mc.change_locked_clarity(20)
                mc.name "[the_person.title]... I'm..."
                the_person "Shhh... do it honey... I want you too..."
                "[the_person.possessive_title!c]'s soothing encouragement pushes you over the edge. You gasp and moan as you dump your load on her ass."
                $ the_person.cum_on_ass()
                $ scene_manager.update_actor(the_person, position = "walking_away")
                $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
                "Your sticky cum coats her ass, but she doesn't seem to mind."
                $ the_person.change_slut(5)
                the_person "Oh [the_person.mc_title]... I didn't know anyone... would feel that way about me..."
                "She grabs your arm and holds you close to her. You consider getting up to try and get cleaned up, but you are so tired..."
                the_person "Goodnight..."
                mc.name "Goodnight..."
            else:
                "You eagerly grind your crotch against her ass. She lets out a quiet gasp."
                the_person "Oh god... [the_person.mc_title]... you make me feel so sexy..."
                "She takes your hand and guides it to her chest. You start to grope her soft tits as you grind up against her."
                $ mc.change_locked_clarity(30)
                the_person "Do you mind if I... if I... get myself off too?"
                mc.name "Of course not! Do you want me...?"
                the_person "No! No it's okay, your hand is great right where it's at..."
                "You feel her shift a little as she props one leg up. You can't see under the covers, but she gasps as she begins to touch herself."
                "You resume grinding your hips against her and fondling her tits as she plays with herself. Things really start to get heated."
                $ mc.change_locked_clarity(30)
                "After a few minutes, you feel yourself getting ready to cum."
                mc.name "[the_person.title]... I'm..."
                the_person "Oh god [the_person.mc_title]... me too! Cum for me!"
                "[the_person.possessive_title!c]'s encouragement pushes you over the edge. You gasp and moan as you dump your load on her ass."
                $ the_person.cum_on_ass()
                $ scene_manager.update_actor(the_person, position = "walking_away")
                $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
                "Your sticky cum coats her ass. Her body goes rigid as she has an orgasm of her own."
                $ the_person.have_orgasm()
                $ the_person.change_slut(5)
                the_person "Oh [the_person.mc_title]... I didn't know anyone... would feel that way about me..."
                "She grabs your arm and holds you close to her. You consider getting up to try and get cleaned up, but you are so tired..."
                the_person "Goodnight..."
                mc.name "Goodnight..."

    $ the_person.discover_opinion("incest")

    "You slowly drift off to sleep with [the_person.possessive_title]."
    $ scene_manager.clear_scene()
    $ the_person.clear_situational_slut("Drunk")

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_aunt_cuddle_01

    "You wake up, but [the_person.possessive_title] isn't there. You slowly get up and walk out of your room and into the kitchen."
    $ mc.change_location(kitchen)
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(mom, position = "sitting", emotion = "happy", display_transform = character_center_flipped)
    "[mom.title] and [the_person.title] are sitting at the kitchen table, drinking some coffee."
    mom "Good morning!"
    the_person "Ahh, good morning [the_person.mc_title]..."
    mc.name "Good morning."
    "You notice as you walk past them to the coffee pot, your aunt is sneaking looks your way. Her cheeks a little rosy and blushed."
    $ mc.change_locked_clarity(5)
    "You pour yourself a cup and lean against the counter. The two sisters are chatting about plans for a bit, when suddenly [mom.possessive_title] stands up."
    $ scene_manager.update_actor(mom, position = "default")
    mom "Well, I need to head out. Have a good day [aunt.fname]!"
    the_person "Thank you! You as well!"
    $ scene_manager.update_actor(mom, position = "walking_away")
    "As [mom.possessive_title] leaves the room, an awkward silence ensues."
    $ scene_manager.remove_actor(mom)
    "You sip your coffee for a while, but finally [the_person.title] stands up and looks at you."
    $ scene_manager.update_actor(the_person, position = "default")
    the_person "[the_person.mc_title]... I appreciate what you did for me last night..."
    the_person "But umm... what happened after we went to bed... that was a one time thing, okay?"
    mc.name "It doesn't have to be."
    if the_person.sluttiness < 30:
        the_person "Yes... yes it does. I was drinking, I wasn't thinking about what I was doing, I just did whatever my body told me to..."
        mc.name "Are you saying you didn't enjoy it?"
        the_person "No, of course not. I definitely enjoyed it, but it can't happen again, okay?"
        mc.name "If that is what you want, [the_person.title]."
        the_person "What I want... right... that's what I want..."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title!c] slowly walks out of the kitchen, muttering to herself."
    else:
        "You can see her open her mouth to say something, but then she stops. She looks at you, as if searching for something."
        the_person "Are you just teasing me? I don't understand why you are doing this."
        mc.name "[the_person.title], you are a fun, sexy woman. I enjoy spending time with you, and after last night... honestly I want to do that again!"
        "She thinks for a moment, but then shakes her head."
        the_person "I wish we could too... but I'm sorry. You need to find someone else..."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] turns and walks out of the kitchen, muttering to herself."
    $ scene_manager.clear_scene()
    "This definitely seems like a good start for things with [the_person.title]."
    "You aren't sure if you are going to continue to pursue her, but with the right mix of serums and time, you're sure you can push her boundaries."
    $ the_person.change_stats(happiness = 5, obedience = 5)
    $ aunt.progress.lust_step = 1
    $ add_aunt_surprise_walk_in_action()
    return

label aunt_surprise_walk_in_label(the_person):
    $ scene_manager = Scene()
    $ the_person.outfit.strip_to_underwear()
    $ scene_manager.add_actor(the_person, the_person.outfit, position = "walking_away", display_transform = character_center_flipped(zoom = 0.7))
    $ mc.change_locked_clarity(10)
    $ the_person.story_event_log("slut")
    "You find [the_person.possessive_title] humming a happy tune, dressed only in her underwear, as you open the door to her apartment."
    "She has her back turned to the door, and for some reason doesn't notice you. You quietly close the door behind you."
    "You check out [the_person.title] thoroughly. Her sexy legs and ass on display in her underwear. You can't help but think naughty thoughts."
    $ mc.change_locked_clarity(30)
    $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_center_flipped(zoom = 0.7))
    "You clear your throat and she turns around and sees you. For a moment she panics."
    the_person "Oh! I'm sorry [the_person.mc_title], I didn't hear you come in! Let me just cover..."
    "Her words stop when she looks down at your crotch. You look down and realise [the_person.possessive_title]'s outfit has given you an obvious erection."
    $ the_person.change_arousal(10)
    $ the_person.add_situational_slut("Horny", 5, "I can't believe I turn him on!")    #TODO make sure this sluttiness level will always allow BJs
    mc.name "Sorry, I umm... I was just..."
    $ scene_manager.update_actor(the_person, position = "default", display_transform = character_center_flipped(zoom = 0.7))
    "She turns to face you, but instead of getting angry, she just smiles."
    the_person "Did I do that to you? Just little old me?"
    "She steps closer to you. This was not the reaction you were expecting, but you decide to roll with it."
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(zoom = 0.8))
    mc.name "I didn't mean to stare, but after I started checking you out... I just couldn't help myself..."
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(zoom = 0.9))
    "She takes another step closer."
    the_person "It's alright [the_person.mc_title]. You're a young man. If you saw someone you found attractive half-naked, it would only be natural..."
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(zoom = 1.0))
    "Another step closer."
    the_person "Can... can I see it?"
    mc.name "I... you want to see my dick?"
    the_person "That's what I asked. Can I?"
    mc.name "I'm not sure..."
    if the_person.tits_visible:
        "[the_person.possessive_title!c] reaches up and gives her tits a shake."
        $ mc.change_locked_clarity(30)
        the_person "I mean, I feel like you've gotten a good look at me..."
    else:
        the_person "Here, I'll go first."
        $ scene_manager.strip_to_tits(the_person, prefer_half_off = True)
        "[the_person.possessive_title!c] pulls up the last piece of cloth covering her tits."
        $ mc.change_locked_clarity(30)
        the_person "There, how about now?"
    mc.name "Okay, I guess it would only be fair."
    "You reach down and unzip your pants, and then pull out your erection."
    $ the_person.change_arousal(20)
    the_person "Oh my god... you poor thing! You look ready to burst!"
    $ scene_manager.update_actor(the_person, position = "default", display_transform = character_center_flipped(zoom = 1.1))
    "Her big tits wobble as she steps even closer. You could reach out and touch her."
    the_person "Hmm... Alright... It's settled."
    mc.name "Wha... what is?"
    the_person "I can't be letting you leave here with blue balls. The last thing I want is to leave you in pain!"
    $ scene_manager.update_actor(the_person, position = "blowjob")
    "Before you can respond, she drops to her knees, reaches out and grabs your cock, giving it a few tentative strokes."
    the_person "You just enjoy this, okay? And just keep it between you and me..."
    $ scene_manager.update_actor(the_person, position = "blowjob", special_modifier="blowjob")
    "[the_person.possessive_title!c] leans forward, opens her mouth, and slides your cock in, sending a jolt of pleasure up your spine."
    $ the_person.break_taboo("sucking_cock")
    mc.name "Oh fuck... [the_person.title]..."
    "You feel her moan around your penis a bit as she starts to slide her mouth up and down your shaft, her tongue lapping at the sensitive underside with each stroke."
    $ mc.change_arousal(20)
    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_aunt_lust_story_01
    $ scene_manager.update_actor(the_person, position = "blowjob", special_modifier = None)
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        the_person "Mmm, yeah! I still got it!"
        $ the_person.change_happiness(20)   #She LOVES being hot stuff still
        $ scene_manager.update_actor(the_person, position = "default")
        if the_person.outfit.has_mouth_cum:
            "[the_person.title] stands up, a bit of your cum has escaped her hungry mouth and is dribbling down her chin."
        elif the_person.outfit.has_face_cum:
            "[the_person.title] stands up, her face still plastered with your cum."
        else:
            "[the_person.title] stands up."
    else:
        mc.name "Sorry, I just really wasn't expecting this, and I'm just completely wore out..."
        mc.name "It felt really good though. Maybe we could finish this up another time?"
        "[the_person.possessive_title!c] looks disappointed, but understanding."
        the_person "Yeah... of course..."
        $ the_person.change_happiness(-5)
        $ scene_manager.update_actor(the_person, position = "default")
        "[the_person.title] stands up, looking away sheepishly."
    $ the_person.clear_situational_slut("Horny")
    "You quickly put your dick back in your pants."
    the_person "Well... you'll keep this between you and me... right?"
    the_person "I don't need Jen, or God forbid Gabby finding out about this..."
    mc.name "Of course. I appreciate your discretion as well."
    the_person "Right. I think I'll go get dressed then before someone else walks in!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title!c] turns and walks away, headed for her bedroom."
    $ scene_manager.clear_scene()
    "As she disappears, you can't help but smirk at how far you've gotten her to go with you."
    "It won't be long until you've got her bent over her couch, moaning your name as you fuck her silly if you keep up with her serums."
    $ aunt.progress.lust_step = 2
    $ aunt.story_event_log("slut")
    # The next slut event is triggered at the end of a family card game, so there is no event to add here.
    # It checks for lust_step progress to trigger, which is set above.
    return

label aunt_card_game_aftermath_label():
    $ the_person = aunt
    $ mc.location.turn_lights_off()
    if the_person.arousal < the_person.max_arousal * .6:
        $ the_person.change_arousal((the_person.max_arousal * .6) - the_person.arousal, add_to_log = False)
    "Lying in bed, you are just drifting to sleep when a noise causes you to open your eyes."
    $ the_person.draw_person()
    "At your bedroom door is a figure, you can just barely see."
    mc.name "... [aunt.title]? Is that you?"
    "She steps inside your room, closing the door. You hear it click a bit louder than usual."
    "Was that the lock?"
    the_person "Yeah... it's me."
    mc.name "Do... you need to crash here tonight? I didn't realise..."
    the_person "No, no that's okay. I wanted to come in here with you for a bit first."
    the_person "I had a great time tonight, playing cards with you... and the rest of the family."
    the_person "For some reason... I just couldn't stop looking at you... you've grown up so much."
    the_person "You remind me so much of your father... I remember when he and your mother met."
    the_person "I was so jealous, she had met such a nice man. I made up my mind I was going to find one for myself."
    the_person "We all know how that turned out... oh god I'm babbling."
    mc.name "It's okay [the_person.title]... I'm just really tired."
    the_person "Yeah... of course you are..."
    the_person "[the_person.mc_title], when I look at you now... it gets so many crazy emotions going inside of me, sometimes I don't know what to do!"
    $ the_person.draw_person(position = "kneeling1")
    "[the_person.possessive_title!c] climbs onto your bed and on top of you... is her hand between her legs?"
    the_person "[the_person.mc_title]... I haven't had a man in so long... I think I'm going to go crazy!"
    "She pulls down your duvet."
    the_person "This... this is just a one time thing... okay?"
    "Her hands are on your shorts now."
    the_person "You can't tell your mother. Or your cousin."
    "She is pulling your shorts down..."
    mc.name "[the_person.fname]..."
    the_person "Hush. I'm sorry, I need this!"
    "She pulls your shorts down farther, and your rapidly rising cock springs free."
    the_person "Oh my god... it looks so hard!"
    $ the_person.draw_person(position = "blowjob")
    "She lowers her face, and without pausing, she opens her mouth and takes your cock deep."
    the_person "Mmmffff... itsshhh shooo gooodf..."
    $ mc.change_arousal(10)
    "Without thinking, you put your hand on the back of her head, guiding her mouth as she starts giving you eager strokes."
    "She is moaning and you can see that she is touching herself with her other hand."
    $ mc.change_locked_clarity(50)
    "Her soft slurps and slutty moans fill your brain with lust for [the_person.possessive_title]."
    $ mc.change_arousal(20)
    "Suddenly, she pulls off."
    the_person "Mmm, good. Your cock feels so hot... I have to feel it inside me!"
    mc.name "[the_person.title]... are you sure?"
    the_person "Of course I'm sure. I snuck into your room in the middle of the night! I fucking NEED this!"
    $ the_person.strip_to_vagina(position = "cowgirl")
    "You watch in awe as she takes her bottoms off, then climbs up on top of you."
    if the_person.on_birth_control or the_person.wants_creampie:  #She goes for a ride bare  #TODO check for condom preferences here
        "She takes your dick in her hand and gives it a couple strokes."
        the_person "Oh fuck it's so hot... I know I should probably wrap it up..."
        "She lifts herself up a bit, then points you at her cunt. In one smooth motion she lowers her body weight down, impaling herself on your bare cock."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(15)
        $ the_person.break_taboo("condomless_sex")
        if the_person.has_taboo("vaginal_sex"):
            $ the_person.break_taboo("vaginal_sex")
            "You can barely believe it. [the_person.possessive_title!c] is riding your cock for the first time, without a condom, in your bedroom, while your family is sleeping!"
        else:
            "You can barely believe it. [the_person.possessive_title!c] is riding your cock bareback, in your bedroom, while your family is sleeping!"
        if the_person.on_birth_control:
            the_person "Don't worry, I'm on birth control... I'm sure I won't get knocked up just from this one time.... right?"
        else:
            the_person "Oh fuck. It feels so good... it'll be okay. What are the odds I get knocked up from just one time?"
        $ the_person.update_birth_control_knowledge()
        mc.name "Oh fuck, it feels way too good to put a condom on now anyway."
        "[the_person.title] starts to move her hips enthusiastically. Her moans are ragged and needy already."
        the_person "Oh fuck I need this so bad. I'm gonna cum my brains out, and then you're gonna fill me up with your hot, sticky seed!"
        call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, start_object = bedroom.get_object_with_name("bed"), allow_continue = False) from _rebecca_first_time_card_game_get_fucked_01
    else:   #Wraps it up.
        "You hear a little rustle, as you realise [the_person.possessive_title] is opening a condom wrapper."
        "She must have come in with one?"
        the_person "Gotta be safe... I'm not on birth control right now..."
        $ the_person.update_birth_control_knowledge()
        "You feel the condom slide down over your cock. You can't believe it... is she really gonna go through with this?"
        $ mc.condom = True
        "She takes your dick in her hand and gives it a couple strokes."
        the_person "Oh fuck it's so hot..."
        "She lifts herself up a bit, then points you at her cunt. In one smooth motion she lowers her body weight down, impaling herself on your cock."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(15)
        if the_person.has_taboo("vaginal_sex"):
            $ the_person.break_taboo("vaginal_sex")
            "You can barely believe it. [the_person.possessive_title!c] is riding your cock for the first time, in your bedroom, while your family is sleeping!"
        else:
            "You can barely believe it. [the_person.possessive_title!c] is riding your cock, in your bedroom, while your family is sleeping!"
        the_person "Oh my god... it feels even better than I imagined."
        "[the_person.possessive_title!c] starts to rock her hips, slowly at first."
        mc.name "Oh fuck, it feels so good to finally be inside you [the_person.title]."
        "[the_person.title] starts to move her hips enthusiastically. Her moans are ragged and needy already."
        the_person "Oh fuck I need this so bad. I'm gonna cum my brains out, and then you're gonna fill up that condom with your hot, sticky seed!"
        call get_fucked(the_person, the_goal = "get mc off", start_position = cowgirl, private = True, skip_intro = True, start_object = bedroom.get_object_with_name("bed"), allow_continue = False) from _rebecca_first_time_card_game_get_fucked_02
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 1:
        "Finished with your fucking, [the_person.possessive_title] turns to you."
        the_person "Oh my god... your dick is amazing..."
        $ the_person.change_slut(3, 80)
    elif the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title!c] is breathing hard, recovering from her orgasm."
        the_person "Oh my god... I needed that so bad."
        $ the_person.change_slut(1, 80)
    "After a few moments, [the_person.title] suddenly sits up."
    $ the_person.draw_person(position = "sitting")
    if the_person.vaginal_sex_count < 2:
        the_person "OH my god... I can't believe I just did that..."
        the_person "[the_person.mc_title], we can't ever do that again, okay?"
        mc.name "What? Why not? That was incredible!"
        the_person "I know! I mean... no! It wasn't! It..."
        mc.name "It was, just admit it. You loved it. I bet you're already thinking about doing it again!"
    else:
        the_person "OH my god... I can't believe I just did that... again..."
        the_person "[the_person.mc_title], we can't ever do that again, okay?"
        mc.name "What? Why not? That was incredible!"
        the_person "I know! I mean... no! We can't do it here, with my sister down the hall..."
        mc.name "Sure, I can come visit you..."
        the_person "Alright, just remember not here... ever..."
    $ the_person.draw_person(position = "stand3")
    "She quickly hops out of your bed."
    the_person "No! I ... oh fuck... I have to go home!"
    $ the_person.draw_person(position = "walking_away")
    "She turns and races out of your room, closing the door behind her."
    $ clear_scene()
    if the_person.vaginal_sex_count < 2:
        "She finally gave in to her slutty desires and fucked you, but for now you should probably just let her be for a few days."
        "You are pretty sure she'll be ready for more soon. You should probably try and hang out with her again soon at her place and see if you can fuck while she's on HER back next time."
        "For now, you are content to just let sleep overtake you."
    else:
        "It seems she just can't resist you. Let's see if she sticks to her own rules."

    $ mc.location.turn_lights_on()
    $ aunt.progress.lust_step = 3
    $ aunt.story_event_log("slut")
    # The next slut event is another triggered event for drinking at her place.
    # It checks for lust_step progress to trigger, which is set above.
    return

label aunt_fucking_round_two_label(the_person): #We trigger this scene by drinking with Rebecca a few days after she hops on MC's cock.
    "After another few minutes of small talk, you decide that it is time to bring up what happened the other night after the card game."
    mc.name "Hey, we really need to talk about something."
    the_person "Ahhhh, no... I really don't think we do."
    mc.name "You may not want to, but I have to. The other night, when you came in to my room. That was incredible."
    the_person "Haaa, incredible...ly stupid you mean?"
    mc.name "No, it was so fucking hot. I can't stop thinking about the way you were bouncing up and down on my cock, the way you were moaning... everything!"
    the_person "Hey, don't talk to your ancient aunt like that!"
    $ the_person.change_arousal(10)
    $ mc.change_arousal(10)
    mc.name "Why not? Why can't I tell you what I've been dreaming about non stop?"
    the_person "[the_person.mc_title]... you don't understand, it isn't nice to lead an older woman on."
    the_person "I have needs, and it had just been so long since I had a man..."
    mc.name "Old? [the_person.title] you're in your prime. And what about me? Am I not allowed to have needs?"
    the_person "No, of course you are."
    $ the_person.change_arousal(10)
    $ the_person.draw_person() # stand her up for rest of dialogue
    "As you stand up and step closer to her she also stands up. You can tell she's trembling, but not from fear. She is getting excited."
    mc.name "[the_person.title], we both want this. Can't you see that? You get me so worked up. Who else could I share these desires with?"
    the_person "With someone your own age! Surely there are girls younger than me you could be ravishing with that incredible cock of yours..."
    "You come closer to her again. You put one hand on the back of her neck and the other on her hip."
    mc.name "Do you hear yourself? I can tell you want it too."
    "You reach down and grab her ass, pulling her body into yours."
    mc.name "Feel this and tell me you don't want it inside you again."
    "You push your hips forward and start to grind your erection through your clothes against [the_person.possessive_title]."
    $ the_person.change_arousal(20)
    "She just gasps, but she doesn't say a word."
    $ the_person.draw_person(position = "kissing")
    "Instead, she leans forward and wraps her arms around you. She draws you into a passionate kiss, and then begins to grind back."
    $ the_person.change_arousal(10)
    "You stand there, grinding against each other for several seconds, passion building as you make out."
    "Then, you push her back onto the couch."
    $ the_person.draw_person(position = "missionary")
    the_person "Ah!"
    "She lets out a little yelp when she lands. You reach down and eagerly start to pull off her bottoms."
    $ the_person.strip_to_vagina(position = "missionary")
    "You reach down and start to undress yourself."
    the_person "This has to be a secret. We can't tell anyone! Do you understand?"
    the_person "We can't tell your family, we can't tell Gabby... we... no one can know!"
    mc.name "I know. But that's okay. This is our secret."
    the_person "Oh my god... let's do it! Fuck me!"
    call fuck_person(the_person, start_position = missionary, start_object = make_couch(), skip_intro = False, skip_condom = False, private = True, position_locked = True) from _call_fuck_person_aunt_fucking_round_two
    $ the_report = _return
    $ the_person.draw_person(position = "missionary")
    if the_report.get("guy orgasms",0) > 0:
        if the_report.get("girl orgasms", 0) > 1:   #You both orgasmed, her more that once.
            "You slowly get up from the couch, but [the_person.possessive_title] is in a stupor from her orgasms."
        if the_report.get("girl orgasms", 0) > 0:
            "You slowly get up from the couch, while [the_person.possessive_title] catches her breath."
        else:
            "You slowly get up from the couch."
    else:
        "You slowly get up from the couch, finished for now."
    "[the_person.title] reaches down between her legs and plays with herself just a bit as you watch."
    $ mc.change_locked_clarity(20)
    the_person "Wow. I think... you're going to need to come over again soon..."
    "She sighs."
    the_person "I guess I'd better get cleaned up before [cousin.fname] gets home... this would certainly be difficult to explain."
    mc.name "I don't think she will be back for a while, but I suppose you never know."
    "Your mind is racing with possibilities."
    if the_person.progress.obedience_step >= 3:
        "Maybe you could have a little fun with her in your office next time she swings by?"
    "You've finally gotten in her pants, and you can't wait to fuck her again."
    "You quickly get yourself dressed."
    the_person "Don't worry, I'll get up... you go on ahead."
    mc.name "Goodnight [the_person.title]."
    the_person "Goodnight."
    $ clear_scene()
    $ aunt.progress.lust_step = 4
    $ aunt.story_event_log("slut")
    # This is the end of this storyline for now.
    return
