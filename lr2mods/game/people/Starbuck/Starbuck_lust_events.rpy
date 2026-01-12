#Starbuck's Lust events revolve around her getting new products into the shop, and then requesting to test them with MC.
#Each one is a product designed to enhance the sexual pleasure in some way, and then can be bought by MC after.

label starbuck_foreplay_enhancer_label(the_person): #20 Sluttiness
    $ the_person.arousal = 0
    "You step into the Sex Shop. As you walk around, you spot [the_person.possessive_title] stocking a shelf."
    $ the_person.draw_person()
    mc.name "Good day [the_person.title]."
    the_person "Oh hey there, [the_person.mc_title]! Check it out! I just got these in stock!"
    the_person "Usually I set up stuff after I close, but I was so excited to see these come in I wanted to get them out right away!"
    "She hands you a small package. The package is for a small vibrating ring. It is advertised as making manual stimulation better for both men and women."
    mc.name "Interesting. Do they work?"
    the_person "Umm, you know, I'm not sure! I was thinking about testing one out later."
    "You get a devilish idea."
    mc.name "That's a good idea, but how will you be able to tell if they work on men, too?"
    the_person "Well, I wouldn't, silly. But I could at least figure out if they work as advertised on women!"
    mc.name "I see. Well, why don't I stick around and help you close up tonight, and we could test them together?"
    mc.name "We could run a control, stimulating each other without, and then with the rings."
    mc.name "Then if they work, you can confidently recommend them to the needs of any kind of couple."
    the_person "Oh! You... you want to touch me... with that?"
    "She points at the package she handed you."
    mc.name "Sure. It could be fun, right?"
    "She thinks about it, but for only a moment."
    the_person "That's a great idea! You keep that one, I'll mark it down in the system later."
    the_person "My understanding is that the battery lasts for about a week, and in order to be safe to be immersed in fluid, they are disposable."
    mc.name "Sounds handy."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Small, finger mounted vibrator. Increases foreplay skill. Lasts one week. +2 Foreplay Skill", foreplay_bonus = 2, bonus_is_temp =True, duration = 7), "Small Finger Vibrator")
    the_person "It is almost time for closing, let me just work on a few things and then we'll try 'em out!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] walks back to the front of the store, leaving you in the aisle with the vibrator."
    $ clear_scene()
    "You inspect the box. It seems easy enough to use. Just slip it on your index or middle finger, then do what you normally do."
    "You open up the box and try it on. It turns on and off easily."
    "Soon, it is closing time. You help [the_person.title] close the shop, then she grabs one off the shelf and drags you to the back room."
    $ mc.change_location(sex_store_storage)
    $ the_person.draw_person()
    "She opens hers up."
    the_person "This thing looks fun... Alright, who goes first?"
    mc.name "Let's test it on you first. Why don't you lay back on the desk?"
    the_person "Ahh... okay..."
    $ the_person.draw_person(position = "missionary")
    "You step over to her as she lays back on the desk."
    if not (the_person.vagina_available and the_person.vagina_visible):
        mc.name "Let's just get these off..."
        "You quickly strip off her bottoms."
        $ the_person.strip_to_vagina(position = "missionary")
    "She spreads her legs, exposing her cunt to your lustful gaze."
    $ the_person.break_taboo("bare_pussy")
    $ the_person.change_arousal(5)  #5
    $ mc.change_locked_clarity(30)
    mc.name "Wow... you look incredible."
    the_person "Hush. We are just testing the products out..."
    mc.name "Right... for science?"
    the_person "Yeah!"
    mc.name "Ok, first up, the control session. Do you need to get a little warmed up first?"
    the_person "I'll be good, just start slow..."
    mc.name "Of course."
    "Without turning on the finger mounted vibrator, you reach down and run a couple of fingers along her slit."
    $ the_person.break_taboo("touching_vagina")
    $ play_moan_sound()
    $ the_person.change_arousal(5)  #10
    "She moans at the intimate contact. You run your fingers along her slit, back and forth a few times."
    "Her pussy rapidly responds, getting wetter with each pass."
    the_person "Mmm god. That feels really good..."
    mc.name "Good. I can't wait to feel you cum all over my fingers."
    the_person "Cum? I didn't realise we were going to go that far..."
    "Still working slowly, you push a finger into her rapidly moistening cunt."
    $ play_moan_sound()
    $ the_person.change_arousal(15) #25
    $ mc.change_locked_clarity(30)
    the_person "Oh! Oh fuck!..."
    "[the_person.possessive_title!c]'s back arches a bit when you penetrate her."
    "You give her insides a couple long, persistent strokes."
    the_person "That's it... Ahhh that is nice!"
    mc.name "Alright, I'm going to go slow and try and set a nice baseline. Here we go."
    $ the_person.change_arousal(15) #40
    $ mc.change_locked_clarity(30)
    "Working slowly, but with pressure, you slide your finger deep inside of [the_person.possessive_title] and back out."
    "You are careful not to escalate things as you go, and avoid any extra touching of her G-Spot and clitoris... for science?"
    $ the_person.change_arousal(5)  #45
    "After a while, she plateaus a bit, as her pleasure reaches a point but doesn't go any further."
    the_person "[the_person.mc_title]... It's good but... but... I can't finish like this..."
    mc.name "Alright, sounds like we are ready for part 2. Ready?"
    the_person "Okay..."
    "You reach down on turn on the vibrating ring. Then resume the exact same slow, stroking manoeuvre."
    $ play_moan_sound()
    $ the_person.change_arousal(15) #60
    $ mc.change_locked_clarity(30)
    the_person "Ahhh! Mmmmmmmmhmmmm. That DOES feel better! Mmmm..."
    "You continue giving her long, prolonged strokes, with one finger."
    "Her back arches and she moans in pleasure."
    $ the_person.change_arousal(15) #75
    $ mc.change_locked_clarity(30)
    the_person "Mmm, yes. Keep going! I... it feels good!"
    "Her body continues to respond positively to the vibrator."
    $ the_person.change_arousal(5)  #80
    "After several strokes though, it becomes clear that she still won't cum from your current method."
    "However, you definitely feel like she got more aroused with the ring than without."
    mc.name "I think the ring definitely works. Before you liked it, but you were still a ways from finishing."
    mc.name "But now, I think I could push you over the edge with just the littlest bit of extra stimulation."
    the_person "Ah... Yes!... I think you are right... You should find out!"
    the_person "Please... Please make me cum... It is so good... let me finish?"
    $ mc.change_locked_clarity(50)
    "Hearing her beg you to make her cum really turns you on. You quickly decide to oblige."
    mc.name "Alright, I would say the test is complete then. But don't worry, I won't leave you hanging."
    "You quickly insert a second finger into [the_person.possessive_title]'s soaked pussy. You change your motion from penetration to an upward curl, stimulating her g-spot."
    $ the_person.change_arousal(25)  #105
    the_person "Gah! OH FUCK that feels so good! I'm...!"
    "Her body begins to spasm and her back arches up off the desk as she starts to cum."
    $ the_person.have_orgasm()
    "[the_person.title] orgasms hard on the desk. Her body squeezes your fingers in waves, and a bit of her juices are running down onto the desk."
    "After several seconds, she lays back on the desk, satisfied."
    the_person "Ahhh... that felt so good... mmm..."
    the_person "Just give me a minute! It is your turn next!"
    "You don't mind waiting a bit. Looking down at a post orgasm [the_person.title] with her legs still spread wide is a pretty hot view."
    $ mc.change_locked_clarity(50)
    "You have a brief urge to just whip your cock out and plunge it into her unprotected cunt right then and there, but you know that wasn't the condition you agreed on."
    "[the_person.possessive_title!c] is so hot, hopefully that is exactly what you'll be doing to her soon."
    "You go ahead and start to disrobe as she starts to get up."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person "Ahh, alright, I think I'm ready. Sorry if I have a dopey grin... my husband always used to make fun of me for having a dopey smile after sex... hahaha.."
    mc.name "Ah, don't worry. It just means you are having a good time."
    the_person "Alright... why don't you lay down on the desk now too? And then we can run part two of the test."
    mc.name "Sounds good."
    "You lay down on the desk, and then [the_person.title] climbs up on top of you."
    $ the_person.draw_person(position = "kneeling1")
    mc.name "Ah, you are getting on top of me?"
    the_person "Yeah. I umm, I think it'll be easier for me this way."
    "She reaches down and takes your cock in her hands, giving it a couple light strokes."
    $ the_person.break_taboo("touching_penis")
    the_person "Wow! Its so big and hard!"
    mc.name "I got really turned on getting you off."
    the_person "I see that."
    "[the_person.possessive_title!c]'s soft hands begin to stroke you. It feels good to have her hands on you."
    $ mc.change_locked_clarity(30)
    $ mc.change_arousal(10)
    "She looks you right in the eyes as she strokes you."
    "Your eyes meet with a burning passion, and you find yourself wishing she would just scoot forward a few {height_system} and sit on your pulsating cock..."
    "But instead, she just keeps going, doing exactly what you did. Her soft hands feel good, but you quickly tire of the same pace."
    "It feels good, but you can tell there is no way you orgasm like this."
    mc.name "Alright, I think we have a good baseline."
    the_person "Mmm, yeah... Alright..."
    "She reaches down and turns on the vibrating ring, and then continues to stroke you."
    "You immediately notice a change in the sensation. It is different, but definitely pleasant."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(30)
    "It definitely feels better. Her stroking is really turning you on."
    "The vibrations add an extra element to [the_person.possessive_title]'s soft hand. It is actually very pleasant."
    $ mc.change_arousal(20)
    "You feel your hips move a bit in time with her strokes. Her soft hand and the vibrations are very pleasing indeed."
    "Looking up at [the_person.title]'s body, your hands act with a mind of their own."
    if the_person.tits_available:
        "You reach and grab [the_person.title]'s tits. They feel so soft and hot in your hands."
        "They bounce pleasingly as she strokes you."
    else:
        "You reach and grab [the_person.title]'s tits through her clothes. They feel soft in your hands."
        "Her chest heaves pleasingly as she strokes."
    the_person "Mmm.... Hey wait, that wasn't part of the test!"
    mc.name "Are you telling me to stop?"
    the_person "No, of course not."
    $ mc.change_arousal(50)
    "Her body weight on yours is setting off fireworks in your brain. She just pushed you past the point of no return."
    mc.name "Oh fuck, [the_person.fname], I'm gonna cum!"
    the_person "Mmmmm yes, do it!"
    $ the_person.cum_on_stomach()
    $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
    $ the_person.draw_person(position = "kneeling1")
    "She strokes you eagerly as you start to cum all over her stomach."
    the_person "Yes... oh my god, let me have it!"
    "She keeps stroking you until you are forced to stop her."
    mc.name "Ohhh fuck! That's enough!"
    $ the_person.change_slut(1, 40)
    the_person "Wow... you had a lot stored up in there..."
    "You spend a moment catching your breath."
    the_person "Well... what do you think?"
    mc.name "It works. It was weird at first, but once I got into it, the extra vibrations felt really good."
    the_person "Hmm, interesting."
    "She struggles to stand up on shaky legs."
    $ the_person.draw_person(position = "stand2")
    the_person "Well, I'm wiped out. I'm going to go get cleaned up and head home... thanks for the help!"
    the_person "Now I can give a better recommendation to potential customers!"
    mc.name "Of course. Take care."
    $ clear_scene()
    $ mc.change_location(sex_store)
    "You step out of the back room and leave."
    "You hope she calls you soon to test out something new!"
    $ starbuck.progress.lust_step = 1
    $ add_starbuck_oral_enhancer_action()
    call advance_time() from _call_advance_time_starbuck_foreplay_enhancer
    return

label starbuck_oral_enhancer_label(the_person): #40 Sluttiness
    $ the_person.arousal = 0
    $ mc.arousal = 0
    "You step into the Sex Shop. As you walk around, you spot [the_person.possessive_title] stocking a shelf."
    $ the_person.draw_person()
    mc.name "Good day [the_person.title]."
    the_person "Oh hey there, [the_person.mc_title]! Check it out! I just got these in stock!"
    the_person "Usually I set up stuff after I close, but I was so excited to see these come in I wanted to get them out right away!"
    "She hands you a small package. The package is for a lip balm that claims to make oral sex better for the receiver, both male and female."
    mc.name "Interesting. Does it work?"
    the_person "I have no idea! And unfortunately, I can't exactly test it on myself."
    "You get a devilish idea."
    $ mc.change_locked_clarity(15)
    mc.name "Well, sounds like we should test it out together. Remember the finger vibrator?"
    the_person "Oh! I... ah, yeah I certainly do remember that."
    mc.name "We could run a test. For research purposes of course."
    mc.name "We'll give each other oral, both with and without the lip balm and see if the other person can feel the difference."
    "She thinks about it, but for only a moment."
    the_person "That's a great idea! You keep that one, I'll mark it down in the system later."
    the_person "My understanding is that due to some of the organic compounds, once it is open it lasts for about a week until you need to throw it out."
    mc.name "Sounds handy."
    the_person "It is almost time for closing, let me just work on a few things and then we'll try it out!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] walks back to the front of the store, leaving you in the aisle with the lip balm."
    $ clear_scene()
    "You can't believe how easy it was to convince [the_person.title] to test out this alleged pleasure enhancer."
    "Soon, it is closing time. You help [the_person.title] close the shop, then she grabs one off the shelf and drags you to the back room."
    $ mc.change_location(sex_store_storage)
    "She stops when she gets to the break room couch."
    $ the_person.draw_person()
    starbuck "Just through here! Oh it is so great that you are willing to test these products with me."
    mc.name "Ah, well, I can't say I don't enjoy it also."
    starbuck "Alright, so... I guess... we could start without the lip balm, then put it on and see if it feels any different?"
    mc.name "Yeah that's a good plan."
    starbuck "So like... should I go first or?"
    "You think about it for a moment."
    mc.name "Why don't we both start at the same time?"
    starbuck "Oh?"
    mc.name "Let me lay down, and you can get on top of me and we can 69 a bit to warm up."
    starbuck "Ohhhhh. Great idea! Alright let's go!"
    "[the_person.possessive_title!c] starts to get naked. You start taking off your clothes as well."
    $ the_person.strip_full_outfit()
    $ mc.change_locked_clarity(35)
    "DAMN, she is so hot naked! You feel yourself getting harder by the second."
    the_person "Ah, there we go!"
    "She notices your erection."
    $ the_person.change_arousal(5)  #5
    the_person "Ah... I see you are ready to go..."
    mc.name "Yeah, what can I say, your body is incredible [the_person.title]."
    the_person "I'm already naked, you don't have to flatter me [the_person.mc_title]."
    "She gives you a wink as she finishes her remark."
    the_person "Alright, lay down! I want to get started!"
    "You lay down on the couch, and then [the_person.possessive_title] starts to climb on top of you."
    $ the_person.draw_person(position = "doggy")
    $ mc.change_locked_clarity(50)
    "Her ass wiggles back and forth a bit as she backs it up closer to your face."
    $ the_person.draw_person(position = "doggy", display_transform = character_right(zoom = 1.4))
    "It is so close... you can't wait to just dive in..."
    the_person "Alright, so first let's just get wa... AH!"
    $ the_person.break_taboo("licking_pussy")
    "You can hear her start to say something but you barely hear it. Once she is situated, you lash out with your tongue to taste [the_person.possessive_title]'s pussy."
    the_person "Oh... Yeah that's... Let's just get each other warmed up a bit... mmmm..."
    "Her words become muffled and you feel her hot mouth take in the tip of your cock. It feels amazing."
    $ the_person.break_taboo("sucking_cock")
    $ the_person.change_arousal(15) #20
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(15)
    "You feel her tongue dance around the tip a few times, then her mouth starts to give long, slow strokes down your length."
    "You press your face into [the_person.title]'s cunt. You lap at her clit several times with your tongue, making her gasp."
    the_person "[the_person.mc_title]! Oh... MMMMmmmfff"
    "She stops sucking you off for a moment while she moans, then you hear her voice muffle again as her lips wrap around your cock again."
    $ the_person.change_arousal(15) #35
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(20) #40
    "Fuck, she is really enthusiastic about sucking your cock! She must really enjoy it."
    $ the_person.discover_opinion("giving blowjobs")
    "You keep working on her pussy, but it is getting difficult to keep up with [the_person.title]."
    "She's moaning loudly as her head bobs up and down your dick. The sexy noises filling up the room are really turning you on."
    the_person "MMmmm... mmmmffffff.... mmmmmmm... Mmmmmgggglp."
    $ the_person.change_arousal(15) #50
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(25) #65
    $ play_gag_sound()
    "Oh FUCK you feel her take your length down her throat. Her technique is incredible."
    "It is almost TOO good... you need to test the lip balm!"
    "You give her ass a loud spank."
    $ the_person.change_arousal(5)  #55
    the_person "Mmmm!"
    mc.name "Hey, slow down! We need to test that lip balm... did you just moan when I spanked you?"
    "She quickly pulls off."
    the_person "Oh... ahh... umm... maybe..."
    the_person "Sorry, I umm... was getting a little carried away there."
    mc.name "Don't worry, it felt amazing. But we still need to test that lip balm."
    the_person "Right... okay I have it right over here. I'll go first, okay?"
    mc.name "Ohh... sure..."
    "You can hear her rustling around with the package as she opens it. She takes the cap off and then applies it."
    "She hands it back to you."
    the_person "Here you go. Put it on, but let me go first, you just lay back and concentrate. See if you can feel any difference in the sensations."
    mc.name "Right, okay."
    "You apply the lip balm as you feel [the_person.title] lean forward and take your cock in her hand."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Lip balm that feels good when you go down on women. Lasts one week. +2 Oral Skill", oral_bonus = 2, bonus_is_temp =True, duration = 7), "Stimulating Lip Balm")
    "You feel her lips running up and down the side of your cock a few times, and it feels mostly... normal?"
    "But there seems to be a little something extra... you can't tell what it is yet."
    "She takes the tip in her mouth, and you feel her tongue dance around it. Yes... there is something extra there."
    "Is it a little warmer? A little wetter? It is hard to tell for sure but you definitely feel it."
    $ mc.change_arousal(10) #75
    "It feels a little better than without, but the extra sensations are faint and hard to pin down. You suppose that is the idea, to just give a little extra sensation."
    mc.name "That does feel good... I think I can feel it!"
    "She pulls off."
    the_person "Oh, really?"
    mc.name "Alright, now it is your turn. Just concentrate on the sensations."
    "You resume licking [the_person.title]'s pussy. She sighs as you start back in nice and slow."
    $ play_moan_sound()
    the_person "Ahh... hmmm..."
    "You take a few moments to run circles around her clit with your tongue, then across it a few times."
    the_person "Mmm... that is good..."
    $ the_person.change_arousal(15) #70
    $ mc.change_locked_clarity(50)
    "Her hips are starting to move a little bit as you run your tongue up and down her slit."
    the_person "It's like there is a little extra... warmth or something..."
    the_person "Mmm but it is nice!"
    "She reaches back and runs her hand through your hair."
    $ the_person.change_arousal(10) #80
    $ mc.change_locked_clarity(50)
    the_person "That IS good... oh... Oh!"
    "You focus in on her clit. Her hips immediately twitch and she starts to moan."
    the_person "Oh FUCK yes! Right there! Oh fuck don't stop I... I... I have to! Mmmmmfffff"
    $ play_gag_sound()
    "Her voice suddenly muffles as she leans forward and swallows your cock. The sudden stimulation gives you a jolt of pleasure."
    "You feel your hips thrust all on their own as she expertly takes you in her throat."
    "You attack her clit with your tongue and lips with the same determination. While this started out as a product test, it is quickly going beyond that."
    "Your brain is locked in. You are going to make her cum all over your face and you're going to cum straight down her throat."
    "*SMACK*"
    the_person "MMMffff....glllp"
    "You smack her ass, making her whole body twitch. Her moans are vibrating all around your cock, pushing you over the edge."
    "Her hips stop moving and she starts to twitch when she starts to cum."
    $ the_person.have_orgasm(force_trance = True)
    "You have no idea if she realises you are on the edge too, but you are in no position to warn her."
    "With a final thrust of your hips, you start to cum straight down [the_person.possessive_title]'s throat."
    $ the_person.cum_in_mouth()
    $ play_swallow_sound()
    "Wave after wave of cum erupts from your cock and straight down [the_person.title]'s throat. Her moans and gulps echo in the small room."
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
    "Even after you finish cumming, [the_person.title]'s mouth keeps giving you slow, sensuous strokes."
    mc.name "I... I think the lip balm works."
    "Her mouth comes off your cock with a loud smack."
    the_person "Mmm... yeah... I think so..."
    "She starts to slowly get up."
    $ the_person.draw_person()
    the_person "Wow... my legs are a little wobbly..."
    "You get up and look at her. A bit of your cum is dribbling down her chin, and her eyes have a bit of a faraway look."
    "Hmm... is... is she in a trance?"
    mc.name "That was great [the_person.title], we should do it again sometime!"
    the_person "Yeah... soon..."
    call trance_train_label(the_person) from _call_trance_train_label_starbuck_40_slut_event_01
    mc.name "That was great. Next time you get a new product, you should just call me."
    mc.name "Even if the product doesn't work, it would still be fun to try it!"
    the_person "Yeah, I'll keep that in mind."
    the_person "Well, I'm wiped out. I'm going to go get cleaned up and head home... thanks for the help!"
    the_person "Now I can give a better recommendation to potential customers!"
    mc.name "Of course. Take care."
    $ clear_scene()
    $ mc.change_location(sex_store)
    "You step out of the back room and start to leave."
    "[the_person.possessive_title!c] sure enjoyed sucking your cock, and remembering the way she swallowed all your cum gives you goosebumps."
    "You hope she calls you soon to test out something new!"
    $ starbuck.progress.lust_step = 2
    $ add_starbuck_vaginal_enhancer_action()
    call advance_time() from _call_advance_time_starbuck_oral_enhancer
    return

label starbuck_vaginal_enhancer_label(the_person):  # 60 sluttiness
    # OUTLINE
    "In this event, [the_person.title] is stocking a new multifunction cock ring that supposedly makes vaginal sex feel better for both partners.."
    "She offers to try it out with MC. He accepts and they fuck."
    "Once the event it complete it is now available for purchase from the store."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Cock ring that increases pleasure during vaginal sex. Lasts one week. +2 Vaginal skill", vaginal_bonus = 2, bonus_is_temp =True, duration = 7), "Vibrating Cock Ring")
    $ starbuck.progress.lust_step = 3
    $ add_starbuck_anal_enhancer_action()
    call advance_time() from _call_advance_time_starbuck_vaginal_enhancer
    return

label starbuck_anal_enhancer_label(the_person): # 80 sluttiness
    # OUTLINE
    "In this event, [the_person.title] is stocking a new anal lubricant that supposedly makes anal sex much more pleasurable."
    "She offers to try it out with MC. He accepts and fucks her ass with it"
    "Once the event it complete it is now available for purchase from the store."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Sensitizing and highly effective anal lubricant. Lasts one week. +2 Anal Skill", anal_bonus = 2, bonus_is_temp =True, duration = 7), "Perfect Anal Lube")
    $ starbuck.progress.lust_step = 4
    call advance_time() from _call_advance_time_starbuck_anal_enhancer
    return
