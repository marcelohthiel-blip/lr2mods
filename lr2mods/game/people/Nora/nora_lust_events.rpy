
#20
label nora_initial_closing_visit_label(the_person = nora, scene_replay = False):
    $ the_person = nora
    $ the_person.arousal = 60

    call non_consent_tutorial_label() from _nora_non_con_setting_check_01
    "It is nearing the end of the business day. You head to your office to close up for the day."
    $ show_popup_hint("Non consent scene\nCheck preferences")
    # show screen popup_hint("Non consent scene\n Check your preferences")
    $ mc.change_location(ceo_office)
    "You sit down at your desk and are working through some daily reports, when someone appears in the door."
    $ the_person.draw_person()
    "[the_person.possessive_title!c] gives a little smirk at your surprise as she closes and locks your office door, then walks over to your desk and sits down."
    $ the_person.draw_person(position = "sitting")
    "Before saying hello, you notice a bit of color in her cheeks..."
    mc.name "[the_person.title]? To what do I owe the pleasure?"
    "She takes a few moments, then begins speaking."
    the_person "Well, I have a bit of a problem. With you, specifically."
    mc.name "Oh?"
    the_person "Today, while teaching class, one of the male students kept distracting me. He is a fine looking male specimen, and for some reason I couldn't stop checking him out."
    the_person "Later, when I was working on a new synthesis process, I was daydreaming about male companionship and almost wasted an entire batch."
    mc.name "Ummm, I'm not sure what this has to do with me..."
    "She sighs, annoyed."
    the_person "[the_person.mc_title], I'm not stupid. You're dosing me. And [stephanie.fname] too probably, along with who knows how many others."
    the_person "I know the symptoms when I see them."
    mc.name "I would never..."
    the_person "Oh save it. This serves to confirm what I've suspected all along."
    mc.name "Which is?"
    the_person "Your serum works. I KNOW about it. And I still didn't realize I was under the effects at first."
    the_person "Now, I could call half a dozen three letter agencies and they would be raiding this place within the hour..."
    mc.name "But... you aren't?"
    the_person "No. I'm not. Because I want to see where this progress goes. What you are doing here is outside the scope of anything at the university."
    the_person "I'm even a little bit okay with being on the receiving end of it once in a while, but we need to make sure we understand each other if that is going to be the case."
    the_person "If I'm going to be dealing with these enhanced sexual urges, YOU are going to do something about it."
    the_person "Now get up and come over here and take your pants off."
    "You hesitate for a moment. [nora.title] DOES have the leverage here, but you aren't sure you like how this is going."
    "Sensing your hesitation, she reiterates her expectations."
    nora "Come on. You and I both know this is the best way to deal with it."
    $ ending_forced = (persistent.mc_noncon_pref == 2)
    if persistent.mc_noncon_pref == 1:
        "You make a split second decision. Do you go along with this? Or do you stand up to her, and do things your own way?"
        menu:
            "Go along with it":
                $ ending_forced = True
            "Stand up to her":
                $ ending_forced = False
    if ending_forced:  #Enabled
        "You do as you are told and stand up. You walk over to [nora.possessive_title]."
        nora "Take your pants off, but leave your underwear on. We'll do this as clinically as possible."
        "You take your pants off, and watch as she does the same, leaving her in her panties."
        $ the_person.outfit.strip_bottom_to_underwear()
        $ the_person.draw_person()
        $ mc.change_locked_clarity(15)
        "She steps towards you and reaches down, stroking your crotch through your underwear."
        nora "Alright... let's see what we're working with here..."
        "You have to admit it feels good, after a minute your cock is standing at full attention."
        nora "Wow... You are certainly well endowed. This will make things easier..."
        "[the_person.possessive_title!c] bites her lip, and you notice signs of arousal showing in her cheeks."
        "After a few more seconds of fondling you, she speaks up."
        nora "Alright, lay back on your desk."
        "Thankfully your desk is mostly empty, so you are able to make a clear place without having to make a mess."
        "You lay back on your desk and soon after, [nora.title] climbs up on top of you."
        $ the_person.draw_person(position = "cowgirl")
        $ mc.change_locked_clarity(25, person = nora)
        "She takes a moment to get herself positioned, then she begins to rub her crotch along your manhood, only two thin layers of fabric separating them."
        nora "Ahhh... there we go..."
        "She sighs as she begins to move her hips. You admit that it feels good, and it is certainly hot to get mounted by your former professor this way, but you don't think you can finish this way."
        "[nora.title] doesn't seem to care though. She closes her eyes and continues to pleasure herself on you."
        "After a while, she certainly seems to be enjoying herself. You try to think of a way to help her get off."
        mc.name "Can you get your tits out?"
        nora "Yes, that's a good idea..."
        $ the_person.strip_to_tits(position = "cowgirl", prefer_half_off = True)
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        "She quickly pulls her clothing to the side, exposing her perky tits."
        "She takes both your hands at the wrist and brings them up to her chest. She lets out an audible moan and resumes grinding against you as you start to fondle her."
        nora "Ahhh, that's it... mmmm."
        "You can feel a hint of humidity between her legs as her arousal continues to build."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        "Once in a while her grinding gets a little uncomfortable, and you really wish the clothing between you two was gone, but she doesn't seem interested in taking things that far."
        "You give her nipples a little pinch and she gives a moan that is starting to get urgent."
        nora "Ahhh!... Mmmm, fuck yes..."
        "Her hips grind against you rapidly now, and you push back against her a bit."
        "She pushes herself a little farther and then begins to orgasm."
        $ the_person.change_arousal(10)
        nora "Yes! Ohhhhhhhhhhh so good..."
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 40, add_to_log = True)
        "Her chest heaves and her body twitches as she orgasms. You just watch as your former professor cums all over you."
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        "When she finishes, she slowly pushes herself up off you."
        $ the_person.draw_person(position = the_person.idle_pose)
        "After standing up, she takes a few moments to recover, then speaks."
        nora "Ugh, much better. You have been most useful, [nora.mc_title]."

    else:
        mc.name "No."
        nora "N... No? What do you mean NO?"
        mc.name "I mean no. You come into my office, we do things my way, not your way."
        nora "What? You can't be serious, if you think…"
        mc.name "I think you wouldn't have walked in here unless you were pretty desperate for some relief."
        "You stand up and walk around your desk towards her. She takes a hesitant step back."
        mc.name "Don't worry, I'll get you off and help you deal with those urges, safely and effectively, but it will be on my terms."
        "She tries to scoff at you, but even at the minimal doses you've given her so far, she finds herself compelled to go along with it."
        nora "I guess I could see how it goes before I make any rash decisions."
        mc.name "That's the spirit."
        $ the_person.draw_person(position = "walking_away")
        "You walk around behind [nora.possessive_title], standing between her and the exit."
        "You put your hands on her hips, then run them forward to her stomach, then slowly creep up to her breasts."
        "She gasps when your hands begin to grope her generous tits."
        nora "Ahhh… mnn…"
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        $ the_person.change_arousal(10)
        "You pull her close to you. You begin to grind yourself up against her backside as you grope her."
        "You bring your hands back to her waist, but this time one hand goes up under her shirt, while the other hand slips down into her panties."
        "[nora.title]'s legs shake for a moment when you slip a finger inside of her."
        nora "Aaahhhh… yeah, yeah this will do it…"
        "It's been a year since you last played with [nora.possessive_title], and it feels amazing to finally get back on that path with her."
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        "Her pussy is soaked with arousal, and her moans are getting eager fast."
        nora "Ohhhhhhhhh fuck. [nora.mc_title]...!"
        $ the_person.change_arousal(20)
        "REALLY fast actually… wait… is she cumming already?"
        "Suddenly, her legs start to give out. You use your arms to hold her upright as she begins to cum on your finger."
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 40, add_to_log = True)
        "You only put one inside her, but her body is so sensitive, she gets off from it almost immediately."
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        "It takes her several seconds before she can hold herself up again."
        $ the_person.draw_person(position = the_person.idle_pose)
        mc.name "Wow. You must have really needed that."
        nora "Yeah… oh god that was nice."
    mc.name "Of course. Now that you're done maybe..."
    nora "I didn't come here today to take care of you. I'm sure one of your employees here that you've been dosing would be more than happy to take care of that."
    # Exchange phone numbers here. She must have MCs phone for the next event.
    "She straightens her clothes while you do the same."
    $ the_person.apply_planned_outfit()
    nora "Alright, I'll be in touch. Goodbye [the_person.mc_title]."
    "She turns and walks out of your office."
    "After she leaves, you replay the scenario in your head."
    "You can't believe she is playing along with your serums for now, although her threats of going to law enforcement are concerning."
    "Maybe you should dose her with obedience related serums. It wouldn't necessarily keep her from taking control during sexual encounters, but it might keep her from going to law enforcement."

    call personal_secretary_quick_service_choice_label() from _nora_20_slut_erection_secretary_call_01
    $ add_nora_house_call_intro_action()
    $ nora.progress.lust_step = 1
    return

# 40 - Unlocks Nora's place progression scene
label nora_house_call_intro_label(the_person = nora, scene_replay = False):
    $ the_person = nora
    $ the_person.arousal = 69   #Nice
    $ passive_mc = None
    if the_person.wardrobe.get_outfit_with_name("Nora Lingerie"):
        $ the_person.apply_outfit(the_person.wardrobe.get_outfit_with_name("Nora Lingerie"))
    else:
        $ the_person.apply_outfit(lingerie_wardrobe.pick_random_outfit(), update_taboo = True)
    # Just call the progression scene intro
    $ show_popup_hint("Non consent scene\nCheck preferences")
    "It is late, but you feel your phone vibrating in your pocket."
    "You take it out, and see a text from [nora.possessive_title]."
    nora "I'm trying to grade papers, but I can't concentrate."
    "As soon as you read her text, you see three dots appear as she starts writing you another message. She must have been waiting to make sure you read her text."
    nora "Here's my address. When you get here, the front door is unlocked. Come in and lock it behind you. I'll be in the bedroom."
    "Damn! This is certainly an exciting proposition. You quickly text her back."
    mc.name "On my way."
    "You put your phone away and get a rideshare over to her apartment complex."
    "You step out and walk inside. Just as she said, her front door is unlocked. You step inside and lock it."
    $ mc.change_location(the_person.home)
    mc.name "[the_person.title]? I'm here..."
    nora "In here..."
    "You follow her voice through a door, stepping into her bedroom."
    "What you see when you walk through the door is an absolute delight."
    $ the_person.strip_to_vagina()
    $ the_person.draw_person(position = "missionary")
    "[nora.possessive_title!c] is laying on her bed in extremely revealing lingerie."
    "She isn't wearing panties, and she has one hand between her legs, playing with herself."
    $ mc.change_locked_clarity(20, nora)
    nora "It's about time."
    mc.name "Wow. [nora.title], you look amazing..."
    "You start to walk over towards the bed."
    nora "Fingers and toys just aren't going to cut it anymore. Come here and eat my pussy."
    mc.name "I can do that... but last time you left me hanging pretty bad, and I can't just call an employee here this time."
    "[nora.title] rolls her eyes, but agrees."
    nora "If you do a good job, I'll make sure you cum too."
    if persistent.mc_noncon_pref == 1:
        "You make a split second decision. Do you go along with this? Or do you stand up to her, and do things your own way?"
        menu:
            "Go along with it":
                $ passive_mc = True
            "Do things your way":
                $ passive_mc = False
    if persistent.mc_noncon_pref == 2 or passive_mc == True:  #Enabled
        $ passive_mc = True
        "You suppose that is probably about the best you'll get from her for now, so you agree."
        "You climb onto the bed and up between [nora.possessive_title]'s legs. You can see and smell her arousal as you bring your face closer to her pussy."
        "You feel her hand on the back of your head as you get closer. You close the final few inches, sticking out your tongue and running it along her slit."
        "She moans from the initial contact."
        $ the_person.break_taboo("bare_pussy")
        $ the_person.break_taboo("licking_pussy")
        nora "Ahhh, ah good. That's it..."
        $ the_person.change_arousal(10)
        "[nora.title]'s cunt is clearly already very aroused. You tease her with your tongue for only a few moments before you begin to lick her properly."
        "The hand on the back of your head urges you on as your tongue circles around her clit. Urgent moans and gasps reiterate how close she already is to finishing."
        nora "That's it. Make me cum [nora.mc_title]. Oh fuuuuuck."
        $ mc.change_locked_clarity(20, nora)
        "You eagerly lap at her clit as she pulls your head between her legs. Her body begins to shudder and spasm and she cries out in orgasm."
        nora "Yes! Oh yes!"
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 60, add_to_log = True, half_arousal = True)
        $ mc.change_locked_clarity(20, nora)
        "You dutifully stimulate her through her orgasm until she is finished."
        "The hand on the back of your head releases you and you come up for air."
        nora "Damn, I really needed that. That was good..."
        mc.name "Yeah... now... about..."
        nora "Hold on. Do you think you're done already? That was just a warm up."
        mc.name "It... huh?"
        nora "Get on your back."
        if persistent.mc_noncon_pref == 1:
            "You're not sure you like where this is going. Maybe you should take control of the situation?"
            menu:
                "Go along with it":
                    $ passive_mc = True
                "Do things your way":
                    $ passive_mc = False
                    mc.name "No, I want a better look at your ass in that outfit."
                    nora "What? That's not what I told you to do, get over... ah!"
                    "You grab her legs and pull her to the edge of her bed, then turn her over."
                    $ the_person.draw_person(position = "standing_doggy")
                    $ mc.change_locked_clarity(20, nora)
                    mc.name "WOW, your ass looks amazing in this."
                    nora "I'm sure it does, but this isn't what I meant..."
    else:
        mc.name "Alright. I'll eat you out, but before I do, I want a better look at your ass in that outfit."
        nora "What? That's not what I told you to do, get over... ah!"
        "You grab her legs and pull her to the edge of her bed, then turn her over."
        $ the_person.draw_person(position = "standing_doggy")
        $ mc.change_locked_clarity(20, nora)
        mc.name "WOW, your ass looks amazing in this."
        nora "This isn't what I meant! Let me go this... aahhhhh!"
        "You lean forward and bury your face between her cheeks and begin to lick up and down between her legs."
        $ the_person.change_arousal(10)
        $ play_moan_sound()
        $ the_person.break_taboo("bare_pussy")
        $ the_person.break_taboo("licking_pussy")
        "Your tongue slides easily into her cunt as you begin to eat her out. She stops putting up any resistance and just enjoys it."
        nora "Yes! Oh yes!"
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 60, add_to_log = True, half_arousal = True)
        $ mc.change_locked_clarity(20, nora)
        "She starts to orgasm almost immediately??? Damn she really cums fast sometimes."

    if passive_mc == True:  #Enabled
        "Uhhh... what is she going to do? You decide for now to play along with it."
        "You turn over onto your back. As you do, [nora.possessive_title] quickly gets up and climbs on top of you, her lower body now sitting on your chest."
        $ the_person.draw_person(position = "cowgirl")
        "Her pussy is inches from your face, and you lean forward a bit, trying to lick her again while she messes with something at the end of the bed."
        "She takes your arms and spreads them out about your head. When she does so, her lower body shifts forward a bit, and you are able to lick the inside of her thighs for a moment."
        "You aren't really even paying attention to anything other than the honeypot in front of your face, when you feel something click into place around your right wrist."
        mc.name "Hey, what are you..."
        "She quickly clicks something into place around your other wrist, then sits up."
        "You try to bring your hands back, but quickly realize that she has cuffed your hands to the bedpost."
        nora "There we go. Now I can REALLY enjoy this..."
        mc.name "[nora.fname], I'm not sure this..."
        "Your words are cut off when [nora.title] lowers herself down, sitting on your face."
        $ mc.change_locked_clarity(30, nora)
        $ the_person.change_arousal(20)
        "Suddenly, there is nothing else in the world than the wonderful pussy pressing down on you."
        "Both her hands are on your head as she begins to grind against you. You immediately get to work pleasing her."
        "Since you are restrained, [nora.possessive_title] is able to set the pacing she wants as you begin to lick and kiss at all of her most sensitive bits."
        "Once in a while she presses down a bit forcefully, grinding against you for several seconds, then moving downward a bit to let you catch your breath."
        nora "Ohhh fuck. That's it. Eat my pussy you little bitch..."
        $ the_person.change_arousal(20)
        "Even though she just got off, [nora.title] is already getting ready to cum again."
        "She must really get off on taking control of things, and between that and your serums, her body seems to be extra responsive to having multiple orgasms."
        nora "Fuck! I'm gonna cum again... oh!!!"
        "Her body presses down again, but her grinding pattern changes into an erratic twitching as she starts to cum."
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 60, add_to_log = True, half_arousal = True)
        $ mc.change_locked_clarity(30, nora)
        $ mc.change_arousal(10)
        "Breathing is impossible, but you don't care as you dutifully lick the spasming cunt grinding against you."
        "Waves of orgasm crash over her, and you are just starting to get desperate for air when she pulls up."
        nora "Ohhh fuck, why didn't I do this sooner. That was so good."
        "She sighs, then starts to turn around."
        nora "Alright, I think I got one more in me. I want to taste your cum too..."
        $ the_person.draw_person(position = "doggy")
        "Fuck, she wants to cum again? After she turns around, her ass slowly starts back up towards your face."
        "You feel her hands on your pants and you feel her pulling them down. You lift up your hips and you hear her gasp when your cock springs free."
        nora "[nora.mc_title], you look ready to burst. Don't worry, you've been good to me, I'll be good to you..."
        "Warm breath tickles your shaft for a moment, then you feel the tip of your cock slide into her warm, wet mouth."
        "She moans as her tongue slides around the tip a few times inside her mouth, then she pulls back."
        nora "I'm glad you taste good. Now don't forget, you still have work to do too..."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "Her hips wiggle for a moment, then she pushes them back against you and you get to work, eating her pussy yet again."
        $ the_person.change_arousal(20)
        $ the_person.break_taboo("sucking_cock")
        "This time, however, you finally get your efforts reciprocated. Having to wait so long makes it feel even better when her mouth engulfs your painfully hard erection."
        "You've finally got your former professor's mouth on your cock. As you lay back and enjoy the sensations, you realize she is actually very skilled."
        "[nora.title] takes your length into her mouth and throat, and you even feel her tongue sliding up and down the shaft as she does it."
        "You had no idea [nora.possessive_title] would be so good at sucking cock."
        $ mc.change_locked_clarity(30, nora)
        $ mc.change_arousal(20)
        $ the_person.change_arousal(20)
        "You don't remember her being a particularly good cock sucker last year... is this some sort of holdover of previous serums?"
        "After several seconds, the incredible sensations are making it difficult to concentrate on eating her out."
        "She pulls off and starts stroking you with her hand, giving you a brief respite."
        nora "Having some trouble back there? Don't worry, I'll help you out."
        "Before you can respond, she pushes her ass back a bit more forcefully onto your face."
        "She grinds her slit along your chin, lips, and nose as she strokes you with her hand."
        $ the_person.change_arousal(20)
        "[nora.title] moans loudly and then eases up, giving you a moment to catch your breath."
        nora "Mmm, fuck you're gonna make me finish again, but first I want you to cum for me..."
        $ mc.change_locked_clarity(30, nora)
        $ mc.change_arousal(10)
        "She leans forward and swallows the length of your shaft again."
        "You try to keep licking her cunt, but her skill is driving you past the point of no return."
        "[nora.possessive_title!c]'s expert mouth drives you to the point of orgasm, and with her pussy in your face you can't even manage to warn her."
        "Her mouth stops moving with the tip of your erection inside her lips and she starts to stroke you with her hand as you begin to cum."
        "Your orgasm slams into your body, and you dump waves of cum into [nora.title]'s eager mouth."
        $ mc.change_locked_clarity(40, nora)
        $ mc.change_arousal(30)
        $ ClimaxController.manual_clarity_release(climax_type = "throat", person = the_person)
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "doggy")
        "She hungrily swallows everything. You even hear a loud gulp after a majority of your ejaculation has finished."
        "[nora.title]'s lips smack when she pulls off your cock. Your balls are thoroughly drained."
        nora "Mmm, that was nice, but it is time for you to get back to work."
        "[nora.possessive_title!c] straights up a bit and pushes her pussy back onto your face."
        "You quickly get back to work, licking and kissing along her slit and paying a lot of attention to her clit."
        "Her ass is nearly smothering you as you fight to make her cum again. Thankfully it doesn't take long."
        nora "Yes! Oh that's it [nora.mc_title]!"
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 60, add_to_log = True)
        "You eagerly lap up at her cunt as she orgasms in your face again. Her orgasmic cries and moans drive you to please her more."
        "When she finishes, she shifts her weight forward, letting you catch your breath."
        "Thankfully she cums so easily... you wonder how things would have gone if she had sat on your face like that and didn't, especially with your hands tied up..."
        "Eventually her leg swings over your head and she gets off you."
        "It takes a few moments, but she releases you from your restraints."
        "You get up out of [nora.title]'s bed and straighten your clothes. She flops down on her bed."
        $ the_person.draw_person(position = "missionary")
        nora "That was just what I needed, [nora.mc_title]. I should be able to sleep well now."
    else:
        "You dive right back in. You give [the_person.title]'s ass a couple playful swats before you bury your face between her cheeks."
        "Her pussy is soaked from her orgasm, so you just spend some time enjoying tasting her for a bit."
        $ mc.change_locked_clarity(20, nora)
        $ the_person.change_arousal(20)
        $ play_moan_sound()
        "Her moans are really starting to turn you on. While you are eating her out, you reach down and unzip your pants, pulling out your cock."
        "You give yourself a couple strokes while you pleasure [the_person.possessive_title] with your tongue."
        the_person "Yes! [the_person.mc_title] that is good, oh my god..."
        $ mc.change_locked_clarity(20, nora)
        $ the_person.change_arousal(20)
        $ mc.change_arousal(5)
        "You start to focus on her clit a little bit more, and her whole body is quivering again."
        "Her moans are getting urgent. Is she going to cum again already?"
        $ mc.change_locked_clarity(20, nora)
        $ the_person.change_arousal(20)
        $ mc.change_arousal(5)
        "Her hips are pushing back against your face as her moans crescendo. She reaches back with both hands and pulls her cheeks apart, giving you an enticing view of her holes."
        the_person "That's it... oh fuck!"
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 60, add_to_log = True, half_arousal = True)
        $ mc.change_locked_clarity(20, nora)
        "Wow! Another orgasm! You can barely believe it. She must have been really turned on."
        "When her orgasm finishes, you sit back for a moment and look at her."
        "She is bent over her bed, her pussy dripping from her orgasms. Her beautiful puckered hole just above it..."
        $ mc.change_locked_clarity(30, nora)
        "You give yourself a couple more strokes. They make tempting targets, for sure, but you aren't sure it is a good idea to push things that far yet."
        "However, she DID promise you some relief this time. Suddenly you get a wonderful idea."
        "You put your hands on [the_person.title]'s hips, groping her ass for a bit."
        the_person "Ah, just give me a few moments, and I'll repay the favor..."
        mc.name "Don't worry, I've got a better idea."
        the_person "Wha? Just give me a moment to... ah!"
        "You reach both arms between her legs then reach up and grab her by the waist."
        "You stand up, dragging her off the edge of the bed as you pick her up, upside down."
        $ the_person.draw_person(position = "missionary", display_transform = character_right_rotate(yoffset = -0.1, rotate = 180))
        "You step away from the bed, holding [the_person.title] upside down, her pussy right in your face."
        "It takes her a few seconds to realize your cock is right in her face, but when she does, she gets to work."
        "You feel your cock slide into her eager mouth and she begins to lick and suck you off."
        "You lean your face forward and start to lick her pussy once again."
        $ mc.change_locked_clarity(30, nora)
        $ the_person.change_arousal(20)
        $ mc.change_arousal(15)
        "[the_person.possessive_title!c] carefully locks her legs behind your head for stability, being careful not to do it to tightly."
        "Holding your former lab teacher helpless in a standing sixty nine as she squirms and moans while sucking you off is a sexual fantasy come true."
        $ play_blowjob_sound()
        $ the_person.break_taboo("sucking_cock")
        "Somehow, even upside down, her mouth is really working you over. The soft sounds of blowjob noises and moans are turning you on faster than you expected."
        $ mc.change_locked_clarity(30, nora)
        $ the_person.change_arousal(20)
        $ mc.change_arousal(15)
        "You attack her pussy with your mouth aggressively. [the_person.title] swallowing your cock feels so good, you push to drive her to orgasm too."
        $ play_moan_sound()
        "Her moans are growing urgent again, but all that does is vibrate your oral cocksleeve, driving your pleasure further."
        "Fuck! You are going to cum. From the sound of her moans though, she isn't far behind."
        $ mc.change_locked_clarity(30, nora)
        $ the_person.change_arousal(30)
        $ mc.change_arousal(25)
        "You moan into [the_person.possessive_title]'s pussy as you approach the edge."
        "She senses it and you feel her swallow your cock, the tip going into her throat."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", person = the_person)
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "missionary", display_transform = character_right_rotate(yoffset = -0.1, rotate = 180))
        $ play_gag_sound()
        "You start to cum straight down her throat. She gags once or twice but keeps your cock deep."
        $ play_moan_sound()
        "Her own moans are muffled as she approaches her own orgasm. As your orgasm subsides, [the_person.title] starts her own."
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 70)
        "[the_person.possessive_title!c]'s body quivers and shakes through her orgasm, but she keeps her mouth on your cock the entire time."
        "When she finishes, she uses one hand to milk to the last of your cum into her mouth before pulling off. You hear her swallow it."
        $ play_swallow_sound()
        the_person "Fuck... that was amazing... can you... put me down?"
        mc.name "Ahhh, right."
        "You carefully put her on her bad and lays down on her back and starts to get comfortable."
        $ the_person.draw_person(position = "missionary")
        nora "That was just what I needed, [nora.mc_title]."
        nora "While your methods weren't what I would have preferred, they were certainly effective."
    mc.name "[nora.title]... that was something. Do you always cum like that?"
    nora "Like what? I'm not sure what you mean."
    mc.name "It started so fast, and then three times, back to back..."
    nora "Yes, women can have multiple orgasms dear."
    "You shake your head. She is being patronizing, but you know women don't usually go off THAT easily."
    nora "Anyway, can you see yourself out? I have to get up early."
    mc.name "Sure. Goodnight [nora.title]."
    "You leave [nora.possessive_title]'s apartment."

    "As you step out into the night and walk home, you can't help but think about your encounter with your former professor."
    "You hadn't imagined her being such a talented cock sucker. You can't wait to feel her mouth working you over again."
    "Maybe you can start pushing things with her and [stephanie.title] during your weekly meetings?"
    $ nora.progress.lust_step = 2
    $ unlock_nora_place_prog_scene()
    $ add_nora_university_booty_call_action()
    return

# 60
label nora_university_booty_call_label(the_person = nora, scene_replay = False):
    $ the_person = nora
    $ the_person.arousal = 60
    $ passive_mc = False
    $ show_popup_hint("Non consent scene\nCheck preferences")
    "You get a text on your phone. It is from [nora.possessive_title]."
    nora "Hey, come to my office at the university. It's urgent."
    mc.name "Sure, I'll be right over."
    "You make your way to the university and then into [nora.title]'s office."
    $ mc.change_location(university_lab)
    "You step inside and see her sitting at her desk."
    "She quickly stands up when she sees you."
    nora "There you are. Lock the door."
    "You do what she says."
    nora "You're just in time, I have a meeting with the Dean in less than an hour!"
    "She starts taking her clothes off."
    $ the_person.strip_to_tits()
    $ mc.change_locked_clarity(20)
    mc.name "Yeah... and?"
    nora "And? [nora.mc_title] take your clothes off."
    mc.name "Uhhh... okay... but why do you need me here for a meeting with the dean?"
    nora "You idiot. I'm meeting with him to discuss funding for my department. I need to be focused, I can't be thinking about dick the whole time!"
    $ the_person.strip_to_vagina()
    "You both finish getting naked."
    $ mc.change_locked_clarity(40)
    nora "Just lay on my desk, I'll do the rest."
    if persistent.mc_noncon_pref == 1:
        "Sounds like she wants to take control of the situation again. Do you want to go along with it this time?"
        menu:
            "Go along with it":
                $ passive_mc = True
            "Do things your way":
                $ passive_mc = False
    if persistent.mc_noncon_pref == 2 or passive_mc:  #Enabled
        $ passive_mc = True
        mc.name "Okay..."
        "You lay down on her desk as she requested. She opens up a desk drawer and takes a condom out."
        "She quickly takes the condom and expertly rolls it down your shaft."
        nora "There we go. No mess. Oh God I need this..."
        $ mc.condom = True
        $ the_person.draw_person(position = "cowgirl")
        "[nora.possessive_title!c] climb up on the desk on top of you. She takes your shaft in one hand and rubs it several times up and down her slit."
        "Her pussy is wet with clear signs of arousal. She's probably been day dreaming about fucking you all day long."
        nora "Mmm... ahh..."
        "After several seconds of rubbing herself up and down, she lifts her hips up a bit and points your cock up at the entrance."
        "She seems to take a moment, knowing that once she sits down and penetrates herself on your manhood, there is no going back."
        "The moment passes and she slowly lets her body sink down onto yours, with your erection sliding easily inside [nora.possessive_title]."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        $ the_person.break_taboo("vaginal_sex")
        "You are finally having sex with your former professor again. It has been over a year since your original foray into making serums, and now you've finally got your cock inside her again."
        nora "Ahhh, yes. Your admirable size should make this fairly quick..."
        "[nora.title] begins to rock her hips back and forth."
        nora "... for me anyway..."
        "[nora.possessive_title!c] takes it nice and slow, and you are a little surprised when her moans turn urgent and she begins to orgasm."
        nora "Oh! Mmmm..."
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 80, add_to_log = True)
        "You savor the sensations as her pussy quivers and cums all over your cock."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "When she finishes, she takes a few moments to recover."
        mc.name "[nora.title]... you really do orgasm easily."
        nora "Shut up, that was just the first little one, now we can do this properly."
        if persistent.mc_noncon_pref == 1:
            "You think about what she just said. You COULD turn the tables and do things 'properly' now."
            menu:
                "Let her keep going":
                    $ passive_mc = True
                "Take over":
                    $ passive_mc = False
                    mc.name "That's a good idea. Let's do this properly now."
                    the_person "What? Yes that's what I was... Ah!"
                    "You quickly stand up, picking her up as you do so. You turn her around and lay her down with her back on her desk."
                    $ the_person.draw_person(position = "missionary")
                    the_person "Ah, well, okay, as long as you give a good performance..."
                    "It takes a couple adjustments to get her position just right, with her ass just on the edge of her desk."
                    "Once you find it though, you put your hand son her hips and begin to fuck her."

    else:
        mc.name "I appreciate you calling me here to help you out, but I want to do this my way."
        "Before she can protest, you pick her up and lay her down, with her back on her desk."
        $ the_person.draw_person(position = "missionary")
        "You spread her legs and start to move in between them."
        the_person "Ah! Wait! Just one second..."
        "She rolls on her side and pulls out one of the drawers of her desk. After rummaging for a moment, she pulls out a condom."
        "You roll your eyes when you see it."
        the_person "Hey, you can take control if you want, but it is condom or nothing, okay?"
        mc.name "Well, when you put it that way..."
        "She quickly opens the package, then reaches down and slides the condom onto your cock."
        $ mc.condom = True
        "She strokes you with her hand a couple times to make sure it is on correctly."
        the_person "Ahh, there we go. No mess."
        "You grab her hips and pull her toward you."
        "It takes a couple adjustments to get her position just right, with her ass just on the edge of her desk."
        "You slide your latex clad erection up and down her slit a few times, eliciting a moan."
        "[the_person.title] is so wet, she has probably been day dreaming about this all day."
        "With one hand on your cock, you get yourself lined up with her pussy."
        "You look at each other in the eyes."
        "She seems to take a moment, knowing that once you penetrate her, there is no going back."
        "You feel her legs behind you back begin to pull you forward. You go with it, your erection sliding easily inside [nora.possessive_title]."
        $ the_person.break_taboo("vaginal_sex")
        "You are finally having sex with your former professor. It has been over a year since your original foray into making serums, and now you've finally got your cock inside her again."
        nora "Ahhh, yes. God I needed this so bad..."
        $ play_moan_sound()
        "With your hands on her hips, you start to slide yourself in and out of [the_person.title]."
        nora "Ohhhh, your size is admirable. This feels amazing."
        "Despite the condom, sliding in and out of your former professor feels amazing. You want to savor it."
        "You take it nice and slow, and you are a little surprised when [the_person.possessive_title]'s moans turn urgent and she begins to orgasm."
        nora "Oh! Mmmm..."
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 80, add_to_log = True)
        "You thrust deep and enjoy the sensations as her pussy quivers and cums all over your cock."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "When she finishes, she takes a few moments to recover."
        mc.name "[nora.title]... you really do orgasm easily."
        nora "Shut up, that was just the first little one, now we can do this properly."
        mc.name "Yes, let's do this properly now."
        "You put your hands on her hips and begin to fuck her."

    if persistent.mc_noncon_pref == 2 or passive_mc:  #Enabled
        "[nora.title] starts moving again, but this time instead of back and forth, she pushes herself up and down."
        $ the_person.change_arousal(20)
        "Her big tits begin to shake as she increases her pace, bouncing enticingly above your head."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "You reach up and take them both in your hands. She moans as you begin to grope her as she rides you."
        nora "Mmm, that's it. Ahhhh..."
        "[nora.possessive_title!c] picks up her pacing, her ass making beautiful smacking noises with each thrust."
        $ the_person.change_arousal(20)
        "You roll each of her nipples between your thumb and your index finger, causing her to cry out."
        nora "OH! Yes [the_person.mc_title]... ooohhhhhh!"
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 80, add_to_log = True)
        "[nora.title] starts to orgasm again. This is her second orgasm in as many minutes?"
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "She stops bouncing and grinds her hips down against yours as her pussy spasms in pleasure."
        "When she finishes she leans forward on her arms, steadying herself. Her tits are in your face, so you do what comes naturally and start to lick and suck on one of her nipples."
        "You feel her hand on the back of your head, going through your hair. She holds your head to her breast as you lick it."
        nora "Mmm... so good..."
        "Her hips start to move again, but a little slower this time as she savors her post orgasm bliss."
        nora "Ooohhh fuck... I'd forgotten how good your cock is. I'm not sure I can keep going."
        "Her hips keep moving, but sluggishly. Having [nora.possessive_title] cum all over you twice in a row has you really turned on, and you aren't ready to be done."
        "You decide to help push her over the edge again. You move your hands down to her hips and grip her firmly."
        mc.name "Don't worry, I can keep going for you."
        "You lift her hips up and then bring them back down. You thrust your hips up into her at the same time, causing her to moan in pleasure."
        nora "Ah! Oh yes..."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "You repeat the process and set an easy pace, thrusting your cock up inside of [nora.title]. She moves her hips with you a bit."
        "You pick up the pace, thrusting yourself at an eager pace and driving you both to an imminent orgasm."
        "Her arms give out and she lets her weight fall onto your body. She rubs her face into your neck as she runs her hands through your hair."
        "Her moans and gasps are right next to your ear and drive your arousal even higher."
        nora "Aaahhh! Oh fuck me [nora.mc_title], you're gonna make me cum again! Oooohhhh!"
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        $ the_person.change_arousal(20)
        "Having [nora.possessive_title] gasping and moaning right in your ear while you thrust up inside of her drives you over the edge."
        mc.name "Oh fuck, [nora.title] I'm gonna cum!"
        nora "Yes! ME TOO! CUM WITH ME!"
        "You have a split second of fear at how loud she is getting, but it is quickly replaced with orgasmic bliss."
        "You grab her ass and slam it down one last time as you begin to fill the condom wrapped around your cock."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        $ the_person.change_arousal(20)
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 80, add_to_log = True)
        "[nora.title]'s entire body quivers as her third orgasm hits and radiates out from her core."
        "You both finish cumming, and for a few moments, the only noise is her hot breath in your ear. Then she whispers to you."
        nora "That was... just what I needed..."
        "She sits up, then slowly stands up."

        #TODO once love story is progressed make her say love you or something if applicable
    else:
        "At long last, you are fucking [the_person.possessive_title] again."
        $ play_moan_sound()
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "Her familiar moans and gasps turn you on as you hips begin to slam into hers."
        "Her entire body is bouncing back and forth as you fuck her. You let go of her hips to reach forward and grope her tits that are heaving with each thrust."
        $ the_person.change_arousal(20)
        "You roll each of her nipples between your thumb and your index finger, causing her to cry out."
        nora "OH! Yes [the_person.mc_title]... ooohhhhhh!"
        $ the_person.change_arousal(20)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 80, add_to_log = True)
        "Her legs lock behind you as [nora.title] starts to orgasm again. This is her second orgasm in as many minutes?"
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "As she finishes, you lean your whole body forward, bringing your mouth to one of her nipples."
        "You feel her hand on the back of your head, going through your hair. She holds your head to her breast as you lick it."
        nora "Mmm... so good..."
        "Her legs release behind your back and her entire body relaxes."
        nora "Ooohhh fuck... I'd forgotten how good your cock is. I'm not sure I can keep going."
        "You stand back up."
        mc.name "Keep going? [nora.title], I'm not sure that decision it up to you."
        nora "Ah, if you still need to finish, you can use my mouth?"
        mc.name "No, no I don't think I will."
        "You step back just enough to grab her by the ankles, she lets out a surprised gasp when you use her legs to rotate her entire body."
        $ the_person.draw_person(position = "standing_doggy")
        "Once she is flipped over, she chuckles. Her vulva are puffy and exposed, peaking out from between her cheeks."
        "You give her ass a couple playful swats, enjoying the way her ass wiggles after each time."
        mc.name "Probably a good thing I've got this condom on. There is NO WAY I'd be able to pull out from an ass this amazing."
        the_person "Yes, that is the idea. It shouldn't interrupt MY pleasure just for you to pull out during orgasm."
        mc.name "Says the slut that has already cum twice on this cock."
        "You step up behind her. With one easy motion, you slide yourself back inside [the_person.possessive_title]."
        $ play_moan_sound()
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        "With your hands on her hips you fuck her hard and fast."
        "The sounds of moans and flesh clapping against flesh fills the room as you have your way with her."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        $ play_spank_sound()
        "You give her ass a few playful spanks, but you feel yourself rapidly approaching orgasm."
        "From the sound of her moans, [the_person.title] is cumming again soon too."
        mc.name "Oh fuck, [nora.title] I'm gonna cum!"
        nora "Yes! ME TOO! CUM WITH ME!"
        "You have a split second of fear at how loud she is getting, but it is quickly replaced with orgasmic bliss."
        "You grab her ass and slam it down one last time as you begin to fill the condom wrapped around your cock."
        $ mc.change_locked_clarity(50)
        $ mc.change_arousal(10)
        $ the_person.change_arousal(20)
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
        $ the_person.have_orgasm(trance_chance_modifier = -50, sluttiness_increase_limit = 80, add_to_log = True)
        "[nora.title]'s entire body quivers as her third orgasm hits and radiates out from her core."
        "Before you pull out, you lean forward and whisper in her ear."
        mc.name "I hope that was just what you needed..."
        "She shivers in pleasure as you slowly pull out."
        "After a few more moments of recovery, she stants up and turns around, facing you."

    $ the_person.draw_person(position = the_person.idle_pose)
    "She looks down at your slightly ballooning condom."
    nora "Well, can't let this go to waste..."
    "She carefully takes off your condom, then much to your surprise, brings it to her open mouth and dumps your cum into it."
    $ the_person.cum_in_mouth()
    $ the_person.draw_person(position = the_person.idle_pose)
    $ mc.condom = False
    "She quickly swallows and looks at you. You must be making a face because she quickly responds."
    nora "What? Don't give that look. Cum is full of protein and nutritional value. I take fish-oil for omega 3s every day?"
    mc.name "Umm, of course, I just... I wasn't expecting that. Most women don't care for the taste."
    nora "I don't take fish-oil for the taste either."
    "You don't remember her being so eager to drink your cum last year... Maybe it is some sort of lasting effect of your old serums?"
    "You don't have much time to dwell on it."
    nora "Alright, I have about 10 minutes until my meeting..."
    "She quickly cleans herself up and gets dressed while you do the same."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    nora "Okay. See yourself out. I have to get going."
    "She looks at you, and for a moment you see a hint of affection, but it quickly disappears."
    mc.name "Alright, good luck with your meeting."
    nora "Goodbye."
    $ the_person.draw_person(position = "walking_away")
    "[nora.possessive_title] turns and leaves you in her office. For a brief moment you consider exploring to see if she has anything interesting, but you quickly decide against it."
    "You leave her office and go out into the university campus."
    if scene_replay:
        return
    "You finally fucked your former lab teacher again! With her proximity to your serum program, you weren't sure that it would ever actually happen."
    "You are pretty sure you left a good impression with her though. You are sure you'll have more opportunities to get intimate with her soon."
    $ add_nora_house_call_followsup_action()
    $ nora.progress.lust_step = 3
    return

#80
label nora_house_call_followsup_label():
    $ the_person = nora
    $ the_person.arousal = 60
    "In this label, [the_person.title] texts MC demanding he come to her house."
    $ show_popup_hint("Non consent scene\nCheck preferences")
    "This label splits more explicitly based on non con settings."
    "Non Con allowed, she drugs MC and fucks him multiple times while he is tied up."
    "In roleplay, she asks to tie up mc and he allows it."
    "In non con prohibited, MC turns the tables on her and drugs her, having sex with her multiple times."
    $ nora.progress.lust_step = 4
    return
