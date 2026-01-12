label mother_anal_curiosity_intro_label():
    $ the_person = mom
    $ the_person.change_energy(-the_person.energy + 1)   #Set energy very low

    "It is late, and before you go to bed, you walk into the kitchen to grab a glass of water."
    $ mc.change_location(kitchen)
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title!c] is sitting at the table on the phone when you walk in."
    the_person "Next month? You're kidding... but... is there someone else there?"
    the_person "Ugh... Yes... No... I'll call back tomorrow..."
    the_person "Right. Thank you."
    "She hangs up her phone and sighs. She looks exhausted and is rubbing her neck."
    mc.name "Everything okay?"
    the_person "Yes, I was just trying to get an appointment at the chiropractor... my back has been killing me the last few days."
    the_person "What I wouldn't give for a back rub."
    mc.name "Umm, I mean, I could always rub your back for you."
    the_person "Oh! Would you? That would be so nice of you! You aren't just saying that to be nice?"
    mc.name "I'd be glad to. Let me just get this glass of water, and I have a couple work emails to deal with tonight too."
    the_person "Is my room okay?"
    mc.name "Sure. If you are relaxed enough you could just fall asleep and I'll see myself out."
    the_person "Okay! You have your drink, I'm going to take a quick shower. Whenever you are ready come on in."
    "She pauses for a second."
    the_person "Maybe you should lock the door as well... I don't want your sister to walk in, that might get awkward."
    mc.name "Okay."
    $ clear_scene()
    $ the_person.apply_outfit(Outfit("Nude"))
    "You get yourself a drink of water and slowly drink it. It'll take her a few minutes to get ready, so you take your time."
    "You get out your phone and deal with a few work issues. You spend several minutes responding to some vendor questions, then put your phone down."
    "You think that should have been plenty of time, so you make your way to [the_person.title]'s bedroom."
    $ mc.change_location(mom_bedroom)
    $ the_person.draw_person(position = "walking_away")
    "You step inside her room, close the door and lock it. When you look over, you see her on her bed, face down and completely naked."
    call perk_time_of_need_story_label() from _time_of_need_jen_anal_massage_01
    "Her room smells like her shampoo and bodywash and her hair still looks damp."
    $ mc.change_locked_clarity(30)
    "She hears when you close the door."
    the_person "I put some lotion on the bedside table. Is that okay?"
    mc.name "Yeah, of course..."
    "You walk over to the bed. You take the lotion, then climb up on top of [the_person.possessive_title]."
    $ the_person.draw_person(position = "walking_away", display_transform = character_center(yoffset = .2, zoom = 1.2))
    "You swear you feel her ass wiggle and push back against you a bit when you squirt some lotion onto her back and begin to rub it in."
    "You start with rubbing wide circles up and down her back, making sure to cover the entirety of her back with the lotion."
    "It takes a few extra applications before you've got full coverage."
    the_person "Mmm... [the_person.mc_title], that feel so good..."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(15)
    "You swear you feel her ass push back against you a bit again..."
    "You decide to push the limits a bit. You reach forward and rub her shoulders, but you shift your weight forward."
    "With your shorts and underwear on, you press your erection gently against her ass crack as you rub her shoulders."
    "There's no way she doesn't feel it, and you sigh when you feel her react by pushing her ass back against you again, slightly arching her back."
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        the_person "Mmm... take it slow [the_person.mc_title], mommy is really sore..."
        "You weren't sure if she was down for anything tonight, but that answer's that question!"
        "She definitely seems wore out though. You'll just have to go slow and do the work to make it happen."
    else:
        the_person "Aahhh.... mmm..."
        "She seems really wore out, but also receptive to some fun. You'll just have to go slow and see what happens."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(15)
    "You keep rubbing her shoulders, but slowly move your hips too, your cock pressing into her ass crack."
    $ play_moan_sound()
    "Her lotion and hair smell amazing. It is tempting to let your arms down and to let your full weight pin her to the bed, but you feel a duty to finish her back rub first."
    "You rub her neck and shoulders for a few minutes, then let your hands go a little further down, to her waist and the small of her back."
    $ the_person.draw_person(position = "walking_away", display_transform = character_center(yoffset = .15, zoom = 1.3))
    "When you move down, you are forced to move your hips back and away from her ass. Your cock aches for a moment, you long press it up against [the_person.possessive_title] again."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(15)
    "Another application of lotion to her lower back, and you keep rubbing. You are treated to a closer view of her curvy backside."
    "You fight the urge to lean forward and bury your face between her legs... for now anyway."
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        "[the_person.title] is clearly exhausted, but if you play your cards right, you are pretty sure you'll be burying your cock in that fantastic puckered hole soon..."
    else:
        "[the_person.title] is clearly exhausted. A naughty plan begins to form in your head. Maybe if you get her excited enough, you can take advantage and..."
        "You stop that thought in your head. Don't get ahead of yourself. She could put a stop to this at any moment."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(10)
    "You keep massaging. You are extra thorough, and soon you are past her waist, working further down to where her hourglass figure flares back out toward her hips."
    $ the_person.draw_person(position = "walking_away", display_transform = character_center(yoffset = .1, zoom = 1.4))
    "A bit more lotion. Now your hands are rubbing on the top curve of her pelvis. Once in a while you grope the top of her ass cheeks."
    the_person "Mmm... [the_person.mc_title], that feels amazing... can you keep going?"
    "She wiggles her ass back at you again. If there was any question about what she meant, her wiggle dispels any confusion."
    "You squirt a considerable amount of lotion onto [the_person.possessive_title]'s ass, then your hands get to work."
    "Your hands eagerly grope and massage [the_person.title]'s ass. She is moaning in appreciation as you work her body with your hands."
    $ play_moan_sound()
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(10)
    $ the_person.add_situational_slut("Exhausted", 20, "Too tired to fight her body's urges.")
    "After several minutes of groping her ass, you push things a little further, squirting some lotion at the top of her crack."
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        $ play_moan_sound()
        "She gasps pleasantly when you work the lotion down between her cheeks, up to and around her puckered hole."
    else:
        "She twitches, then gasps when you work the lotion down between cheeks, and around her puckered hole."
    "You take the lotion bottle, then squirt another portion onto her backdoor."
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        "[the_person.possessive_title!c] reaches her hands back and grabs her cheeks, pulling them apart to give you easy access to her rectum."
    else:
        "[the_person.possessive_title!c] starts to reach back with her hands and you startle to a stop. Did you push her too far?"
        "Your fears vanish when she grabs her cheeks, and then pulls them apart, giving you easy access to her rectum."
    $ mc.change_locked_clarity(50)
    "You take your middle finger and work the lotion all around the rim, then you target the puckered centre and lightly begin to push."
    "It takes several seconds of slowly building pressure, then her body's resistance gives way and your finger penetrates her."
    $ play_moan_sound()
    $ the_person.change_arousal(10)
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        "She moans and her back arches in this now familiar sensation. It still takes work to make her ass relax enough for penetration, but she is getting better at it."
    else:
        "She gives a startled moan from this unfamiliar sensation. With a couple of strokes though, she is able to will her body to relax."
    "You finger her asshole gently for a while, and her moans are soft and husky. Soon, you pull it back, then up your middle and index fingers together."
    "[the_person.possessive_title!c] arches her back and moans from the enlarged penetrator."
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        the_person "More lotion, honey! Get mommy good and warmed up..."
    else:
        the_person "Ahhh, can you add some more lotion? It needs more..."
    mc.name "Of course."

    "You pull your fingers almost all the way out, and with the other hand you squirt a large portion of lotion around her asshole."
    "You gently work the lotion into her ass with your fingers, then apply another dollop."
    "After another minute, you are working your two fingers in and out of her forbidden hole easily."
    the_person "Oh [the_person.mc_title]... okay."
    if the_person.event_triggers_dict.get("anal_revisit_complete", False):
        the_person "That feels amazing. You can fuck me now."
        mc.name "Yeah?"
        the_person "You make me feel so good, I want you to feel good!"
        the_person "I'm too tired to do anything to help, but you can use my ass. I WANT you to, okay?"
        "You had every intention of fucking her ever since you stepped foot in her room, but hearing her ask you for it makes your cock twitch."
        "You get up... a moment later... your shorts and underwear are off and discarded. You climb back up on top of [the_person.possessive_title]."
        $ the_person.draw_person(position = "walking_away")
        "You get the lotion bottle and use a bunch to lubricate your cock thoroughly, then you press your body up against hers."
        "[the_person.possessive_title!c] reaches back with her hands and spreads her ass cheeks again, and you take your cock at the base and point it at her puckered hole."
        "Using your weight, you slide yourself inside all the way in, buried in her incredible ass."
        $ play_moan_sound()
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(10)
        "She moans as you begin to move your hips."
        call fuck_person(the_person, private = True, start_position = prone_anal, start_object = make_bed(), skip_condom = True, skip_intro = True, position_locked = True) from _call_massage_anal_prone_jen_01
        "She sighs when you finish, slowly pushing yourself up and standing carefully."
    else:
        "You freeze again, waiting for her to continue."
        the_person "Fuck that feels amazing. Honey... I... I can't believe I'm about to say this..."
        mc.name "What is it, [the_person.title]?"
        the_person "Mommy is so worked up, but I need more than just fingers. Could you... Oh god..."
        mc.name "It's ok mom. What do you want me to do?"
        the_person "Could you get your cock out? I want to feel it pressed up against me... skin on skin this time..."
        "Hmm... you thought she was about to tell you to fuck her... but this is still a nice compromise."
        "Her ass is lotioned up pretty thoroughly. You bet it would feel good to rub up against it."
        mc.name "Sure, if that is what you want."
        the_person "Yeah... yeah that's what I want..."
        "Her voice is husky with arousal. You can tell she is conflicted, but you play along."
        "You get up... a moment later... your shorts and underwear are off and discarded. You climb back up on top of [the_person.possessive_title]."
        $ the_person.draw_person(position = "walking_away", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "You get the lotion bottle and use a bunch to lubricate your cock thoroughly, then you press your body up against hers."
        "Your cock slips between her cheeks and you begin to hotdog along the length of her crack. Her soft cheeks press up against your hips."
        $ play_moan_sound()
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(10)
        "You use your arms to support some of your weight, but you use most of it to pin [the_person.title] facedown to her bed."
        "It feels so good to be pressed up against her. If you started thrusting eagerly you could probably cum right here."
        "However, you know in this position there's no way she could finish, so instead you take a leisurely pace, thrusting against her."
        "She moans in pleasure from the contact, but soon you can sense she is starting to get frustrated."
        the_person "Ah... this is nice... but I think your fingers were a bit better..."
        "She waits for a few seconds, then speaks up again."
        the_person "Stop... for a second..."
        "You stop thrusting."
        the_person "Maybe you could just put the tip in a little... just to feel what it's like..."
        "You scoff inwardly, but manage to stifle a laugh. A game of just the tip, NEVER ends with JUST the tip!"
        mc.name "Yeah, that's a good idea..."
        "You know you've got her ass conquered, now it is just a matter of a little bit more patience."
        "You pull your hips back, and she reaches back with her hands and spreads her ass cheeks again."
        $ mc.change_locked_clarity(50)
        "You grab the lotion. One more round of lube."
        "You grab your cock at the base, then point it right at her puckered hole. Slowly, you let your body weight down."
        "Her puckered hole resists for a few seconds, then with a jolt it gives way, your cock sinking halfway in all at once."
        $ play_moan_sound()
        the_person "OH! Oh fffff.... oh my god [the_person.mc_title]..."
        "She takes several seconds to adjust."
        the_person "That... is way more intense than fingers, just give me a moment..."
        "You can feel her ass clench you a couple times as she tries to force her body to relax."
        "Even without movement, her clenching almost makes you cum, but you managed to keep the sensations in check."
        the_person "Okay... more. My body needs more honey!"
        mc.name "But mom I thought you said just the tip..."
        the_person "I know, oh god I'm a horrible mother... but my body needs more!"
        the_person "I'm so sorry, I'm going to regret this in the morning, but please [the_person.mc_title]! Please fuck my ass!"
        mc.name "It's okay [the_person.title]. You're a wonderful mother, but you said just the tip, and I didn't want to scare you by taking things too far or too fast."
        "Before she can respond, you let your weight down. Your cock slides all the way in, buried in her incredible ass."
        $ play_moan_sound()
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(30)
        $ mc.change_arousal(20)
        "You let your weight pin her to the bed. She whimpers in pleasure as you begin to thrust yourself in and out of her tight hole."
        $ the_person.break_taboo("anal_sex")
        $ play_moan_sound()
        "Her moans are loud and urgent. You are thankful because all the teasing and touching leading up to this has you on edge as well."
        the_person "That's it... ohhhhhh GOD..."
        "Her body is desperately pushing back against you, but being pinned to the bed leaves her with little room to manoeuvre."
        "However, the sensations overwhelm you when her body suddenly tenses up and then begins to quiver from head to toe."
        $ the_person.have_orgasm()
        "Her orgasm comes fast and hard, and between her blissful moans and her ass rhythmically clenching around your cock, your orgasm hits you fast too."
        "You barely have time to blurt out a warning, and in the throes of her own orgasm, [the_person.possessive_title] doesn't even seem to register them."
        mc.name "[the_person.title]! I'm gonna... OH FUCK!"
        $ the_person.cum_in_ass()
        $ the_person.draw_person(position = "walking_away", display_transform = character_center(yoffset = .2, zoom = 1.2))
        $ ClimaxController.manual_clarity_release(climax_type = "anal", person = the_person)
        "Her eyes snap open when she feels the splash of your cum inside her rectum."
        the_person "OH! Oh my god I can feel it!"
        "She reaches back as best as she can and grabs your leg, trying to pull you deeper inside of her."
        "You give her body spurt after spurt of your cum, she pushes her ass back against you with each one."
        the_person "Oh my god baby... I could feel it twitching... and... oh god..."
        "Her words catch in her throat when your cock twitches again. After a few more seconds, one last wave moves through your body, causing her to gasp."
        $ the_person.increase_opinion_score("anal sex")
        $ the_person.increase_opinion_score("anal creampies")
        the_person "I didn't know... it could be so good..."
        "Well, you are sure you'll hear about this tomorrow, but at the same time, you are pretty sure she'll never forget the night her son pinned her down and creamed her ass while she orgasmed..."
        "You push yourself up, your cock sliding out from her bowel, then carefully stand up."
    $ the_person.draw_person(position = "walking_away")
    "You look around and grab your underwear and shorts and put them on, then turn back to the bed."
    "You start to say something, but realise [the_person.possessive_title] has fallen asleep. You gently whisper to her."
    mc.name "Goodnight [the_person.title]..."
    "You quietly leave her room and head back to yours."
    $ mc.change_location(bedroom)
    $ clear_scene()
    "You aren't sure if you'll have the opportunity to give [the_person.possessive_title] a massage like that again in the future, but that was certainly an encounter to remember!"
    $ the_person.clear_situational_slut("Exhausted")
    return
