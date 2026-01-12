# This file is NOT a progression scene, but contains the labels for Nora and Stephanie's serum experiments with MC.
# The first two scenes are fully scripted events where each girl gets dosed and trained.
# Once the initial trainings have been complete, both girls agree to allow future trainings, but only under specific conditions.
# Followup labels are follow up training sessions OR just generically fun sex sessions if players don't want to train one of the girls.
# Training sessions are setup to allow for a variety of improved opinions, possibly with custom training for specific opinions


###### TRAINING SESSION OUTLINES ######
# Each training session consists of three parts
# Stats are required to move through all three parts. If MC lacks stats, players only get one or two of the applicable training scenes
# Major opinions should have applicable forks, EG: Anal sex opinion training should involve a segment of anal sex.

# Stephanie
# Scene 1 is similar to the teamup intro. Put Nora behind Stephanie, playing with her while stephanie blows MC
# Scene 2 is MC fucking Stephanie missionary while Nora sits on her face
# Scene 3 is MC fucking Stephanie doggy while Nora cuddles with her and they make out.

# Nora
# Scene 1, use the intro scene, with Nora on her back on the bed, with Stephanie eating her out and MC face fucking her.
# Scene 2, Nora rides MC cowgirl, while Stephanie sits on MC's face
# Scene 3, MC fucking Nora while she lays on top of Stephanie and they make out.


# Both
# Scene 1, the girls 69. MC can penetrate either girl
# Scene 2, Nora gets on top of Stephanie and they make out. MC takes turns fucking both, making them both cum.
# Scene 3, Both girls on their knees for a double blowjob finish with cum swapping


label stephanie_nora_teamup_intro_label():  #No need for group. We know who the two girls are.
    python:
        scene_manager = Scene()
        scene_manager.update_actor(stephanie, display_transform = character_left_flipped, position = "sitting")
        scene_manager.update_actor(nora, position = "sitting")
        mc.change_location(downtown)

    "You catch a cab to [nora.title]'s place with her and [stephanie.possessive_title]. There is a playful tension in the air."
    "You sit between the two women. [stephanie.title] has her hand on your leg and is rubbing it back and forth."
    stephanie "I'm excited to see your place [nora.fname]. After years of working together, it'll be neat to see!"
    mc.name "She has a neat style, I'm sure you will be impressed with her decor."
    "[stephanie.title] looks at you, quizzically."
    stephanie "Oh... have you been to her place before?"
    "Whoops. You try to come up with an excuse, but [nora.title] quickly cuts in."
    nora "Of course he's been there. You aren't the only one to help him test serum designs once in a while."
    stephanie "Oh! Right... that makes sense."
    "She seems to accept the answer without much thought. Thankfully alcohol keeps her from processing that entire thought."
    "You arrive and are quickly escorted inside by [nora.title]. Once inside she closes the door."
    python:
        nora.change_to_bedroom()
        stephanie.change_location(nora.location)
        mc.change_location(nora.location)
        scene_manager.update_actor(stephanie, display_transform = character_right, position = stephanie.idle_pose)
        scene_manager.update_actor(nora, display_transform = character_center, position = nora.idle_pose)

    "All three of you move to her bedroom, and then [nora.possessive_title] turns to [stephanie.title]."
    nora "[stephanie.fname], come here..."
    $ scene_manager.update_actor(stephanie, display_transform = character_right, position = "kissing")
    $ scene_manager.update_actor(nora, display_transform = character_right, position = "walking_away", z_order = 10)
    "The two women embrace, and then like something from a wonderful, distant memory, they begin to kiss."
    "The kissing quickly gets passionate as their tongues begin to dance, and hands begin to gently explore each other."
    $ mc.change_locked_clarity(50)
    "You simply stand and watch for several moments as things get heated. [stephanie.title] eventually pulls back."
    stephanie "Oh my god, [nora.fname] I didn't realize you were into this..."
    nora "I didn't think I would be either, but it feels right."
    "[nora.title] takes [stephanie.possessive_title]'s hands and holds them for a moment."
    nora "Now, what sounds like fun tonight?"
    "[stephanie.title] hesitates for a moment, then sheepishly responds."
    stephanie "This sounds so weird to say but, honestly, I want to suck [stephanie.mc_title]'s cock..."
    "You feel the specified organ twitch in your pants."
    nora "Mmm, that does sound nice."
    $ scene_manager.update_actor(nora, display_transform = character_right, position = "back_peek", z_order = 10)
    "[nora.title] looks over at you."
    nora "[nora.mc_title], sit on the edge of the bed. You're getting a treat tonight."
    "Fuck yeah! You quickly step over to the bed and sit down, as instructed. Your former employer and head researcher get on their knees in front of you."
    $ scene_manager.update_actor(stephanie, display_transform = character_center_flipped, position = "blowjob", z_order = 10)
    $ scene_manager.update_actor(nora, display_transform = character_right, position = "blowjob")
    "[stephanie.possessive_title!c] pulls down your pants and underwear, releasing your erection and then begins it lick it up and down."
    "She opens her mouth and begins to eagerly suck your cock while [nora.possessive_title] takes off her top."
    $ scene_manager.strip_to_tits(nora)
    $ mc.change_locked_clarity(30, nora)
    "Once her tits are free, she leans forward right next to [stephanie.title]."
    nora "Let me have a taste while you get your tits out."
    "[stephanie.title]'s mouth audibly pops off your cock, and she points it toward [nora.possessive_title]'s mouth."
    "[nora.title] leans forward and begins to slowly suck you off."
    $ scene_manager.strip_to_tits(stephanie)
    $ mc.change_locked_clarity(30, stephanie)
    "[stephanie.possessive_title!c] takes the opportunity to take off her top. Both women's tits are now available for your viewing pleasure."
    "[stephanie.title] reaches over and gropes [nora.possessive_title]'s chest, causing her to give a low, throaty moan that vibrates all around your cock."
    $ nora.change_arousal(15)
    $ stephanie.change_arousal(15)
    "[nora.title] keeps bobbing her head slowly up and down your erection. She savours your manhood while enjoying her former lab assistant's hands on her body."
    "After several more seconds, she slowly pulls off and relinquishes you back to [stephanie.title]."
    nora "Alright [stephanie.fname]. Go slow and enjoy it."
    "[stephanie.possessive_title!c] responds by opening her mouth and enveloping your cock inside her warm, wet mouth once again."
    "Instead of joining her, [nora.title] instead moves around behind [stephanie.title], embracing her from behind."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "kneeling1", z_order = 1)
    "Her hands begin to run up and down her former lab assistant's body. Her hands move to her chest and she starts to play with her tits."
    stephanie "Mmmmmmnhh... that's nice..."
    $ stephanie.change_arousal(15)
    $ mc.change_locked_clarity(80)
    "[stephanie.title] moans her approval as best as she can with a mouth full of your dick. Soft moans enhance the pleasure of her skilled tongue."
    "You watch in interest as one of [nora.title]'s hands begins to move down [stephanie.possessive_title]'s body and then between her legs."
    "[stephanie.title]'s mouth stops bobbing up and down for a moment and she looks up at you with her eyes wide as her former boss slides a finger inside her pussy."
    $ stephanie.change_arousal(25)
    "Her eyes glaze over a bit and she resumes sliding your shaft in and out of her warm mouth, but at a significantly slower pace than before."
    stephanie "Mmmfff... that's gooooooood."
    "Her rumbling approval sends a shiver up your spine."
    $ mc.change_locked_clarity(80)
    $ mc.change_arousal(20)
    "Pleasured moans enhance the skilful blowjob [stephanie.possessive_title] is giving you as [nora.title] fingers and gropes her."
    "When a second finger slides inside her, [stephanie.title] is forced to pop off your cock for a few moments while she adjusts."
    stephanie "Oh fuck [nora.fname], that feels so good!"
    "[stephanie.possessive_title!c] sticks out her tongue and runs it up and down the sides of your shaft several times."
    "Her hips are starting to move with her former boss's fingers when [stephanie.title] opens her mouth and slides her lips over and down your cock again."
    "Urgent moans reverberate around your erection as your head researcher services you eagerly."
    $ stephanie.change_arousal(25)
    $ mc.change_locked_clarity(80)
    $ mc.change_arousal(20)
    "[nora.title] senses the urgency and encourages what is about to happen."
    nora "That it you little slut. Swallow all your boss's seed and then cum all over my fingers!"
    "The sounds of slurping, moaning, and dirty talk are too much. You manage a quick warning."
    $ stephanie.change_arousal(25)
    $ mc.change_locked_clarity(80)
    $ mc.change_arousal(20)
    mc.name "Oh fuck, I'm gonna cum!"
    "[nora.possessive_title!c] keeps fingering your head researcher, but takes her other hand off her tits and grabs the back of her head, slowly pushing those soft lips down your shaft and your tip goes down her throat."
    "[stephanie.title] gags for a moment but she offers no resistance as you start to cum directly down her throat."
    $ stephanie.cum_in_mouth()
    $ ClimaxController.manual_clarity_release(climax_type = "throat", person = stephanie)
    $ scene_manager.update_actor(stephanie, display_transform = character_center_flipped, position = "blowjob", z_order = 10)
    "Escalating moans match wave after wave of cum as [stephanie.title] gets ready to get off too."
    "[nora.title] releases the back of her head and [stephanie.possessive_title] suddenly pulls off your cock as she begins to orgasm."
    stephanie "glffff, AH! OH FUCK"
    $ stephanie.have_orgasm(force_trance = True, sluttiness_increase_limit = 80, half_arousal = False)
    "Her hips and body begin to spasm as her orgasm begins. The last couple spurts of your cum splatter down onto her nose and chin."
    $ stephanie.cum_on_face()
    $ scene_manager.update_actor(stephanie, display_transform = character_center_flipped, position = "blowjob", z_order = 10)
    "[nora.possessive_title!c] skillfully stimulates her former lab assistant through her orgasm, until the last wave is done."
    "[stephanie.title] looks up at you, her eyes glazed over with the telltale signs of being in a trance."
    "[nora.title] carefully supports her as she lays back against her."
    "After several moments of being held, [stephanie.title] stirs."
    stephanie "Wow... that was amazing..."
    nora "Why don't you lay down for a moment on the bed..."
    "You reach down and help [stephanie.possessive_title] up off the floor, and then she quickly lays down on [nora.title]'s bed."
    $ scene_manager.update_actor(stephanie, display_transform = character_right, position = "missionary", z_order = 10)
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "walking_away", z_order = 10)
    nora "Hmm, interesting..."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = nora.idle_pose, z_order = 10)
    "[nora.possessive_title!c] takes your hand and starts to lead you away."
    nora "Here [nora.mc_title], let me show you the bathroom so you can get cleaned up..."
    "She says it loudly, to make sure that [stephanie.title] hears you, then leads you out of the bedroom, leaving her behind."
    $ nora.change_to_hallway()
    $ scene_manager.remove_actor(stephanie, reset_actor = False)
    nora "That worked, didn't it? Her demeanour and posture... this is a trance?"
    mc.name "Yes, it is."
    nora "And in her current state, she becomes much more open to suggestions?"
    mc.name "Yes. We aren't sure yet how long it lasts, but suggestions can be trained into someone in a trance, and it lasts for at least several weeks, or maybe longer."
    nora "Fascinating. I want to study this more..."
    mc.name "Yeah, but I can hardly have you out at the lab while you are still in your current position."
    nora "Yes yes. I'm aware. Still... maybe we could do this again..."
    "She thinks for several minutes."
    nora "I know just what to do."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "walking_away", z_order = 10)
    $ nora.change_to_bedroom()
    $ scene_manager.add_actor(stephanie, display_transform = character_right, position = "missionary", z_order = 10)
    "You feel yourself raise an eyebrow, but just follow as she goes back into the room with [stephanie.possessive_title]."
    nora "[stephanie.fname], you had a good time tonight, yes?"
    stephanie "Mmm? Oh, yes [nora.fname], it has been great."
    nora "Coming here with me and [nora.mc_title] has been good, hasn't it?"
    stephanie "Yeah..."
    nora "You LOVE sharing him with me, don't you?"
    stephanie "Sharing... sharing [stephanie.mc_title]? I... I don't want to share..."
    nora "That's what you say, but you DO love it, don't you? Sharing him with me, and with other women."
    stephanie "I... I didn't realize it, but you might be right."
    $ stephanie.set_opinion("threesomes", 2, False)
    $ stephanie.discover_opinion("threesomes")
    $ stephanie.event_triggers_dict["is_jealous"] = False
    "You can't believe what you are hearing. [nora.title] is trying to train [stephanie.possessive_title] to have an open relationship with you so she can study the serum effects easier in the future."
    "It's smart, of course. But also a little bit scary."
    nora "Of course I'm right. You DO love it. You want to share him with me, and with all the women at the lab too."
    stephanie "Yeah... Yeah you're right..."
    "[nora.possessive_title] spends several more minutes training [stephanie.title] into loving threesomes and sharing you with other women."
    stephanie "I'm tired... can I sleep here?"
    nora "Of course. Go ahead."
    $ scene_manager.remove_actor(stephanie)
    $ nora.change_to_hallway()
    $ scene_manager.update_actor(nora, display_transform = character_center, position = nora.idle_pose, z_order = 10)
    "You and [nora.title] leave the bedroom again. She closes the bedroom door behind her."
    mc.name "So... same time next week?"
    nora "I'll plan on it. Obviously things may come up from time to time, but I wouldn't mind being able to see what these trances are capable of doing."
    mc.name "Alright, I'm going to head home. Have a good night."
    nora "Goodnight [nora.mc_title]."
    $ mc.change_locked_clarity(10, nora)
    "You take one last look at [nora.fname]'s tits before you turn around."
    python:
        scene_manager.remove_actor(nora)
        nora.change_location(nora.home)
        stephanie.change_location(nora.home)
        scene_manager.clear_scene()
        mc.change_location(downtown)

    "You see yourself out of [nora.possessive_title]'s apartment and start the walk home."
    "You run a quick recap in your head."
    "Tonight, [nora.fname] helped you dose your head researcher, made her cum while she sucked you off, then trained her to be into an open an relationship and threesomes."
    "There's no way this doesn't get more interesting. You wonder if you could convince [stephanie.title] to help you turn the tables and do the same thing back to [nora.title]."
    "You can imagine, weeks from now, fucking both of them silly, and getting them to train each other into being better and better sluts for you to have your way with..."
    "As you approach your home, you make a mental note to follow up with [stephanie.title] sometime next week at the lab to make sure her training is holding, and to make a plan for progressing things further with [nora.possessive_title]..."
    $ nora.event_triggers_dict["steph_teamup_stage"] = 1
    $ add_stephanie_nora_teamup_followup_action()
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_nora_steph_teamup_intro
    return

label stephanie_nora_teamup_followup_label(the_person = stephanie):   #Stephanie asks for a chance to return the favour
    $ the_person = stephanie
    "You swing by your research department."
    $ the_person.draw_person(position = "sitting")
    "You spot [the_person.possessive_title] working at her desk. You have a flashback from the weekend, when you, her, and [nora.title] had some sexual fun..."
    "The night went well, but you want to followup with her."
    "[nora.title] helped you train her to be more receptive to future group activities, but you'd like to turn the tables on her."
    "You walk over to [stephanie.title]'s desk. When she sees you approach she flashes you a smile."
    the_person "Hey [the_person.mc_title]. Here to go over some serum designs?"
    mc.name "Not exactly. I actually wanted to talk to you about what happened over the weekend."
    the_person "Ahh, you mean at [nora.name]'s? How crazy was that?"
    mc.name "It was definitely something. Is that something you'd be interested in doing more often?"
    the_person "Oh geeze... Ever since that night, I've been struggling to STOP thinking about it. I really hope you and her are interested in getting together again this weekend."
    mc.name "Ah, well, there is something you should know."
    mc.name "[nora.fname] asked for help setting it up. She wanted to observe our trance induced states directly."
    mc.name "After you had an orgasm, she trained you a bit... to be more open to threesomes and... other things."
    mc.name "She wants to observe the state more in the future, so she trained you to be more open to it."
    "[stephanie.title] takes several moments to process what you are saying."
    the_person "Wow... That... That makes a lot of sense actually."
    the_person "I've never really had a lot of fantasies about other women before this past weekend..."
    if stephanie.is_girlfriend:
        the_person "... And I keep thinking about you and me getting with other women too. [nora.fname] and other girls here..."
    else:
        the_person "... And about you and me with other women... not that we are like, dating or anything!"
    $ the_person.change_arousal(10)
    "From her tone of voice, you can tell she is getting a little excited, just talking about it."
    mc.name "Well, I was thinking. This weekend, maybe we should turn things around a bit with [nora.title]."
    the_person "Oh? What did you have in mind?"
    mc.name "She wants to get together again, and she thinks I'm going to give you some serum again so we can induce a trance for her to observe."
    mc.name "But I figure, we should switch it up and train her instead."
    mc.name "If we trained her to be more into threesomes the same way she did to you, we could have a LOT more fun together..."
    "[the_person.possessive_title!c] thinks about it for several moments, then smiles."
    the_person "That's a pretty devious plan, but I like it!"
    the_person "But ummm... Once [nora.fname] realizes what we did, she's going to get PISSED."
    mc.name "Yeah, she might. Let's be honest though, we are really just returning the favour."
    the_person "Alright. I'm willing to give it a try. If she get's pissed off though, I'm going to blame it all on you."
    mc.name "That's fair."
    "You step away from [the_person.title]'s desk, leaving her to resume work."
    "You have a plan in place. Next time you meet with your former lab mates at the bar, you are going to try and turn the tables on [nora.title]."
    $ nora.event_triggers_dict["steph_teamup_stage"] = 2
    return

label stephanie_nora_teamup_revenge_label():
    python:
        scene_manager = Scene()
        scene_manager.update_actor(stephanie, display_transform = character_left_flipped, position = "sitting")
        scene_manager.update_actor(nora, position = "sitting")
        mc.change_location(downtown)

    "You catch a cab to [nora.title]'s place with her and [stephanie.possessive_title]. Sexual tension is thick."
    "You sit between the two women. [stephanie.title] has her hand on one of your legs and [nora.possessive_title] has a hand on the other."
    nora "I can't wait to get home, I've been looking forward to this all week."
    "[stephanie.title] shoots you a quick, knowing glance and gives you a wink."
    stephanie "I bet so. I've been looking forward to it also."
    "You see the cab driver look back at you in the rear view mirror. He has a smile on his face."
    "You get to [nora.title]'s place and soon you are walking in the door with the two women."
    python:
        nora.change_location(nora.home)
        stephanie.change_location(nora.home)
        mc.change_location(nora.home)
        scene_manager.update_actor(stephanie, display_transform = character_right, position = stephanie.idle_pose)
        scene_manager.update_actor(nora, display_transform = character_center, position = nora.idle_pose)

    nora "Finally! Now, how should we..."
    $ scene_manager.update_actor(nora, display_transform = character_right, position = "kissing")
    $ scene_manager.update_actor(stephanie, display_transform = character_right, position = "walking_away", z_order = 10)
    "She gets cut off when [stephanie.title] pulls her into an embrace and a kiss."
    "[nora.possessive_title!c] reciprocates and the two women start to make out."
    "[stephanie.possessive_title!c]'s hands drop to [nora.title]'s ass."
    $ nora.change_arousal(15)
    $ stephanie.change_arousal(15)
    $ mc.change_locked_clarity(30)
    "It isn't surprising that [stephanie.title] is taking a more active role, after the suggestions that were made to her last week."
    "[nora.title] pulls back from the kiss with a moan."
    nora "Let's go to the bedroom, you can suck [nora.mc_title] off again or maybe he could even fuck you..."
    stephanie "Mmm, yeah maybe, but last week was about me. This week, let's make sure you feel good."
    "[nora.possessive_title!c] hesitates for a few moments. She wants to put her former lab assistant into a trance, but the serum you gave her earlier is working against her."
    nora "I... it would be nice to have an orgasm..."
    python:
        nora.change_to_bedroom()
        stephanie.change_location(nora.location)
        mc.change_location(nora.location)
        scene_manager.update_actor(nora, display_transform = character_center, position = "walking_away")

    "She leads you back to her bedroom, and [stephanie.title] immediately starts helping her get out of her clothes."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "stand3", z_order = 10)
    $ scene_manager.update_actor(stephanie, display_transform = character_right_flipped, position = "stand3", z_order = 1)
    $ scene_manager.strip_full_outfit(nora, strip_feet = True)
    "Once naked, [stephanie.possessive_title] gives her ass a smack. It makes a delightful sound."
    $ mc.change_locked_clarity(20, nora)
    $ play_spank_sound()
    stephanie "Mmm, I can't wait to taste your pussy."
    nora "Oh! Yes that does sound nice..."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "stand3", z_order = 10)
    "[stephanie.title] starts to strip down also while [nora.possessive_title] turns to you and starts to pull down your pants."
    $ scene_manager.strip_full_outfit(stephanie, strip_feet = True)
    "Soon the three of you are completely naked in [nora.title]'s bedroom."
    $ mc.change_locked_clarity(30, stephanie)
    stephanie "Alright, [nora.fname], lay down on your back, with your head off the edge of the bed. I know just what to do..."
    nora "Hmm... okay..."
    "The normally dominant [nora.title] just goes along with it as [stephanie.possessive_title] helps her get into position."
    $ scene_manager.update_actor(nora, display_transform = character_center_focus(yoffset = -0.1, rotate = 180), position = "missionary", z_order = 10)
    $ scene_manager.update_actor(stephanie, display_transform = character_center_focus_flipped(xoffset = -0.03), position = "kneeling1", z_order = 1)
    "You step around the side of the bed next to [nora.possessive_title]'s head when the two girls finish getting into position."
    "When [nora.title] puts her head back, she looks up at you. Your cock fills her vision and she realizes she is the one pleasuring you tonight."
    nora "[nora.mc_title]? Why don't you go over there, you could fuck [stephanie.fname] while she..."
    "You cut her off."
    mc.name "Nah, I want to feel that mouth of yours. Besides, [stephanie.title] was right. Last week was her week, this week it is your turn."
    "There is a brief moment of panic in [nora.title]'s face when she connects the dots and realizes that you and [stephanie.possessive_title] were planning this"
    "Her concerned look quickly fades when her former lab assistant puts her face between her legs and starts to lick her pussy."
    "Concern changes to surprise, which changes to pleasure, and then resignation."
    $ nora.change_arousal(20)
    nora "Ohhh, [stephanie.fname]... okay... I'll go along with it... this time..."
    "You step forward a little farther, your cock now resting on [nora.possessive_title]'s nose and lips."
    "She sticks her tongue out and licks your shaft a few times."
    nora "I can't move my head much, you'll have to move some, carefully..."
    mc.name "Alright. If you need a break just use your hands to push my hips back."
    nora "Mmm, mmhmm..."
    "You reach down and put a hand on the back of [nora.title]'s head. She opens her mouth and once you get the right angle, you slip your cock past her eager lips and into her mouth."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    "You are careful to thrust your cock into her mouth without going too deep. You might finish down her throat, but you don't want to start things out too rough."
    "You look up and marvel at [nora.possessive_title]'s completely exposed body, laid out on her bed in front of you."
    "[stephanie.title] is licking eagerly at the slit between her former boss's legs, causing pleasurable moans around your manhood."
    $ nora.change_arousal(20)
    "Blowjobs have always been amazing, but your last couple rounds with your former boss and lab partner have been especially good, with the girl blowing you moaning and cumming during the process."
    "Of course, in your current position, you can help. You reach down with both hands and start to grope [nora.possessive_title]'s tits."
    "You pinch her nipples, eliciting another reverberating moan around your cock. You feel your legs get weak for a moment from the pleasure."
    $ nora.change_arousal(20)
    nora "Mmmm... stho goooodth..."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    "[nora.title] has reached down with a hand and has it on the back of [stephanie.possessive_title]'s head. She must really be enjoying her tongue."
    "[nora.possessive_title!c] is pulling her head deeper toward her crotch. You have a brief insight of how much fun you're going to have in the future with the dominating personality of [nora.title] and her former lab assistant."
    "You give her nipples another rough pinch and thrust into her mouth a little deeper. You want to be sure to make yourself the most dominant force in this ménage à trois."
    "[nora.title] puts her free hand on your leg, but doesn't push you away yet. She obediently takes your cock just a little bit deeper."
    $ nora.change_arousal(25)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    nora "Aannhh... mm... MMM"
    "[nora.possessive_title!c]'s moans are growing urgent. She is going to cum already."
    "You stop moving your hips and just enjoy the growling vibrations of her hot mouth as she starts to cum."
    $ nora.change_arousal(25)
    $ nora.have_orgasm(force_trance = True, half_arousal = True)
    "[nora.title]'s stomach and legs start to twitch and spasm, and her hand on the back of [stephanie.possessive_title]'s head grabs her hair and grinds her pussy against her face."
    "When she finishes, you pull your cock from her mouth and look down. Her eyes have the glazed, empty look of a trance."
    "You lean down and whisper in her ear."
    mc.name "That's it. A wonderful dream-like state. Just lay back and submit yourself to me. [stephanie.title] and I are going to make you feel so good."
    nora "Mmm, I know... aahhhh"
    "You look up and see that [stephanie.possessive_title] has backed off her urgency a bit but is still licking [nora.title]'s pussy."
    mc.name "Alright, let's see if you can get my cock a little deeper in that incredible throat of yours. Lean your head back and relax."
    nora "Mmm... okay..."
    "You stand up straight and take your cock in hand. You rub it along the side of each of her cheeks first, then point it at her mouth."
    "[nora.title] opens her mouth and you slowly push your erection back into her steamy mouth."
    $ nora.change_arousal(25)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    nora "Oooohhhnn, yessshhh."
    "[stephanie.title] is picking up the pace again, and [nora.possessive_title]'s urgent moans and gasps are driving you towards your own orgasm."
    "You are careful not to push too deep into her throat, but you definitely feel the tip of your manhood hitting the curve at the back of her mouth."
    "You feel [nora.title]'s hand on your hip and at first you start to pull back, thinking you might be gagging her, but instead you feel her pull your hip toward you, urging you to push yourself deeper into her slutty mouth."
    "You oblige, let her urge your hips forward slowly until your dick has vanished completely inside her eager mouth. You can feel your balls resting on her nose."
    nora "Mmmmfff... mmm... mmm... mmmgLCK"
    "She runs her tongue along the underside of your shaft a few times, then gags for a moment."
    "You instinctively pull back until just the tip is inside her mouth to give her a quick respite."
    "After a moment, the hand on your hip urges you forward again."
    $ nora.change_arousal(25)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    "You push your hips forward, your cock disappears behind her lips and down her throat once again."
    "You give [nora.title]'s mouth a few shallow thrusts, being careful not to fully pull out of her throat, until she gags again and then you pull back."
    nora "UNMH, ahh... fuck..."
    "[nora.possessive_title!c] takes her hand off your hip and puts it at the base of your cock and starts to stroke you a bit while she recovers."
    "She continues to moan and quiver from the sensations [stephanie.title]'s tongue is delivering her."
    nora "Aahhh... okay... I'm ready again..."
    "You don't wait for her hand, you slowly push your hips forward again. You groan in pleasure when your cock is completely engulfed by the warmth of her mouth and throat."
    $ nora.change_arousal(25)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    "She doesn't have the skill to do much to please you like this, but [nora.possessive_title]'s rapidly intensifying moans are driving you toward your own orgasm."
    "You enjoy [nora.title]'s reverberating throat for a few more seconds, then pull back and give her one last respite."
    nora "Ohhhh, fuck [stephanie.fname], you're gonna make me cum again.. ahhhMMMM"
    $ nora.change_arousal(25)
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20, nora)
    "As she gets ready to orgasm, you push your cock down her throat again."
    "Her hand grabs your hip, but she doesn't push you away. [nora.title] spasms and pleasured moans rack her body."
    $ nora.have_orgasm(force_trance = True, half_arousal = False)
    "Watching [nora.possessive_title] helplessly orgasm beneath you drives you past the point of return as well. You enjoy the wonderful sensation of the final building pleasure in your groin."
    "[nora.title] is just coming down from her orgasm when you unload your first wave of cum in her mouth and down her throat."
    $ nora.cum_in_mouth()
    $ ClimaxController.manual_clarity_release(climax_type = "throat", person = nora)
    $ scene_manager.update_actor(nora, display_transform = character_center_focus(yoffset = -0.1, rotate = 180), position = "missionary", z_order = 10)
    "She grabs your hips with both hands now and pulls you toward her as far as she can manage as you start to unload wave after wave of cum straight to her stomach."
    mc.name "OH FUCK, that's it, TAKE IT SLUT!"
    "You look down and notice that [stephanie.title] has stopped licking [nora.possessive_title] and is watching in awe as you cum down her former boss's throat."
    "[nora.title] gags a couple of times as you finish cumming, and then slowly pull out."
    nora "GUHHHH! OH fuck...!"
    "She catches her breath once her airways are clear of your manhood, breathing heavily with occasional soft moans."
    "You can tell from her face that her trance has deepened. You lean down and whisper in her ear again."
    mc.name "See? I know you love to take control, but once in a while you need to be submissive too. The things I can make you feel will be worth it, I promise."
    $ nora.increase_opinion_score("being submissive")
    nora "Mmm, yes... so good..."
    "You stand up straight."
    stephanie "Holy shit that was so hot. You just dumped your whole load down her throat!"
    "[stephanie.title] crawls up on top of [nora.possessive_title]."
    $ scene_manager.update_actor(stephanie, position = "cowgirl", display_transform = character_center_focus_flipped(yoffset = -0.1),z_order = 15)
    stephanie "Oh! She didn't get all of it.."
    "She leans forward and starts to lick a bit of cum that has dribbled down [nora.title]'s face clean."
    "When she recovers, [nora.title] puts her arms around [stephanie.possessive_title] and the two women start to make out."
    "You walk around the bed the to the other side."
    $ scene_manager.update_actor(nora, display_transform = character_center_focus(zoom = .8, xoffset = -.1, yoffset = 0.05), position = "missionary", z_order = 10)
    $ scene_manager.update_actor(stephanie, display_transform = character_center_focus_flipped, position = "doggy", z_order = 15)
    "From your new vantage point, you can see the mess that [stephanie.title] made of her former boss's pussy, while her own is pristine, with just a hint of moisture beginning to leak out, down the side of her labia and her inside thigh."
    "You step forward and give [stephanie.possessive_title]'s ass a heavy spank. She moans in surprise, breaking her kiss with [nora.title]."
    $ stephanie.change_arousal(10)
    $ mc.change_locked_clarity(10, stephanie)
    stephanie "Ah! HEY! I thought I did good tonight?"
    mc.name "You were amazing. Do you need some attention yourself?"
    "She thinks about it for a moment, but turns you down."
    stephanie "Next time. I loved sharing you with [nora.fname] though... didn't you love it too?"
    nora "Mmm, yes... that was incredible... but I need to rest soon..."
    stephanie "Okay, I'll see him out..."
    "You get dressed as [stephanie.title] stands up, then walks with you out of [nora.possessive_title]'s bedroom."
    python:
        nora.change_to_hallway()
        scene_manager.remove_actor(nora)
        scene_manager.update_actor(stephanie, position = stephanie.idle_pose, display_transform = character_center_focus)

    stephanie "I'm going to spend the night here. I want to give her a bit of training too, like what she did to me last time."
    stephanie "Watching you train her into being more submissive was amazing though. I want you to stay and have a little more fun, but I don't want to forget about the reason we came here tonight in the first place."
    mc.name "You're right. After tonight, we'll be able to have all kinds of fun together."
    $ scene_manager.update_actor(stephanie, position = "kissing", display_transform = character_center_focus)
    "[stephanie.possessive_title] reaches up and gives you a hug. You lean forward and give her a passionate kiss."
    stephanie "Mmm.."
    "You can taste [nora.title]'s pussy on her lips."
    $ mc.change_locked_clarity(10, stephanie)
    $ scene_manager.update_actor(stephanie, position = stephanie.idle_pose, display_transform = character_center_focus)
    "You step back and say goodnight."
    mc.name "Alright, I'll see you at work on Monday."
    stephanie "Of course. Bye boss!"
    "You leave [nora.title]'s apartment and start your trek home."
    python:
        scene_manager.remove_actor(stephanie)
        nora.change_location(nora.home)
        stephanie.change_location(nora.home)
        scene_manager.clear_scene()
        mc.change_location(downtown)

    "Right now, as you walk, you imagine [stephanie.title], cuddled up with [nora.possessive_title], gently training and suggesting her in her trance-like state to share you with them both."
    $ nora.set_opinion("threesomes", 2, False)
    $ nora.discover_opinion("threesomes")
    $ nora.event_triggers_dict["is_jealous"] = False
    "You are sure you'll hear more about it from both of them, and you are a little concerned that [nora.title] may not take it well."
    "However, you've got your hooks in place. Now it is only a matter of time until you are banging both girls as you please, at the same time even."
    $ nora.event_triggers_dict["steph_teamup_stage"] = 3
    $ add_stephanie_nora_teamup_revenge_followup_1_action()
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_nora_steph_teamup_revenge
    return

label stephanie_nora_teamup_revenge_followup_1_label():
    $ the_person = nora
    $ mc.change_location(ceo_office)
    $ scene_manager = Scene()
    $ scene_manager.add_actor(nora)
    the_person "Knock knock, [the_person.mc_title]."
    "You are surprised to see [nora.possessive_title] at your business, away from the university."
    mc.name "[the_person.title]? What are you doing here?"
    the_person "We need to talk. And it is urgent."
    "She closes your office door and locks it. Then walks over and sits across from you."
    $ scene_manager.update_actor(nora, position = "sitting", display_transform = character_center_focus)
    the_person "You know why I'm here."
    mc.name "[nora.title], look, I understand that..."
    the_person "I'm not upset. Not anymore anyway."
    mc.name "You... you aren't?"
    the_person "Oh, I was PISSED on Sunday after [stephanie.fname] left my place. But I've had some time to calm down and think about it."
    the_person "I realized two things, and today I want to talk to you about what I realized."
    the_person "First, it really WASN'T fair of me to put [stephanie.fname] through that trance without asking or informing her about it first."
    the_person "And second, even though I wasn't part of planning it, it WAS an extremely pleasurable experience to be on the other side of it."
    the_person "So, for you, and for [stephanie.fname], I have a bit of a proposal."
    mc.name "Oh?"
    the_person "I'm okay with what happened, and even repeating it in the future, but only under two specific conditions."
    the_person "When we were done, I realized that the experience has made me, shall we say, open up to new and exciting experiences in the future."
    the_person "I'm okay with both being put into a trance and trained, and doing so to [stephanie.fname], ONLY if we both know about it beforehand..."
    the_person "... AND if the training only helps us to enjoy and try new things, NOT making us hate something and then making us do it anyway."
    mc.name "That is an interesting proposal."
    the_person "I hope you understand, this process you are developing has IMMENSE applications. Not just for sexual use."
    the_person "Imagine, a weekend spent training, and suddenly a person loves to exercise? Or is able to learn to love eating healthy, or read, or..."
    "She gets lost in the possibilities for a moment."
    the_person "I want to experience this first hand. What do you say?"
    mc.name "That sounds great to me, but we are missing one important piece. Give me one second."
    the_person "Of course."
    "You get on your phone and quickly text [stephanie.title], telling her to come to your office ASAP."
    "A minute later, there is a knock on your door. You unlock it from your desk and then she steps inside and closes the door behind her."
    $ scene_manager.add_actor(stephanie)
    stephanie "Hey, you wanted to see me?... Oh! Hey [nora.fname]... what ummm... what brings you here?"
    "[stephanie.possessive_title!c] nervously walks over and takes a seat beside her former boss."
    $ scene_manager.update_actor(stephanie, position = "sitting")
    the_person "[nora.mc_title] and I were just discussing last weekend and how we would like things to be going forward."
    stephanie "I swear, the whole thing was [stephanie.mc_title]'s idea, I was just..."
    the_person "[stephanie.fname], stop. I'm not angry. In fact, I think we have an incredible opportunity here."
    stephanie "Oh... wait really?"
    "You briefly explain to her [nora.title]'s proposal. She considers it for a moment."
    stephanie "So... we only train each other toward's enjoying new and fun things... and we just enjoy fucking each other when we do it?"
    mc.name "Yeah... that's basically it."
    stephanie "Wow! Sounds great to me! Do you want me to start bringing whatever the most current suggestibility serum is each week?"
    stephanie "We could just hang out at the bar, have a few drinks, then whoever is going to get trained can take it and then we go back to [nora.fname]'s..."
    mc.name "That's a good idea. Yes, can you be in charge of bringing some each week?"
    stephanie "You got it, boss!"
    the_person "Good. Then it is agreed. We all know about it before hand."
    stephanie "And good vibes only. Wow! I can't wait until Saturday..."
    $ scene_manager.update_actor(nora, position = nora.idle_pose, display_transform = character_center_focus)
    $ scene_manager.update_actor(stephanie, position = stephanie.idle_pose)
    "The two women stand up."
    mc.name "I'm glad we have come to a consensus. I'll see you both soon."
    the_person "Goodbye, [the_person.mc_title]. [stephanie.fname]. OH!"
    "Suddenly, [stephanie.title] embraces her former boss."
    $ scene_manager.update_actor(nora, position = "kissing", display_transform = character_center_focus, z_order = 1)
    $ scene_manager.update_actor(stephanie, position = "walking_away", display_transform = character_center_focus, z_order = 10)
    "The two women begin to make out. [stephanie.title]'s hands drop to [nora.possessive_title]'s ass and she begins to grope her."
    "DAMN. Right here in your office."
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(10)
    $ stephanie.change_arousal(20)
    $ nora.change_arousal(20)
    "However, just as you are getting ready to stand up and walk over to them, they break their embrace."
    $ scene_manager.update_actor(nora, position = nora.idle_pose, display_transform = character_center_focus)
    $ scene_manager.update_actor(stephanie, position = stephanie.idle_pose)
    the_person "Oh my..."
    stephanie "Mmm. Boss, I know you're a busy guy, but please make sure you come hang out with us Saturday night, okay?"
    mc.name "Right. Yes, if I can, I'll be there."
    stephanie "Great!"
    $ scene_manager.update_actor(nora, position = "walking_away", display_transform = character_center_focus)
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "The two women and turn to leave your office. You notice [nora.title] give [stephanie.possessive_title]'s ass a playful spank as they walk out..."
    $ scene_manager.clear_scene()
    "You are left alone in your office."
    "Your weekend dates with [nora.possessive_title] and [stephanie.title] are about to get a LOT more interesting!"

    $ nora.event_triggers_dict["bar_meetup_both_stay"] = True
    $ nora.event_triggers_dict["steph_teamup_stage"] = 4
    call personal_secretary_quick_service_choice_label() from _nora_steph_teamup_setup_sec_relief_call_01
    return


label stephanie_nora_teamup_repeat_intro_label():   #Generic intro that gives MC the option of who and what to train
    "NOTE: The remainder of this event has several portions that are OUTLINE ONLY."
    "Thanks for your patience as I work through updating threesome content at a later date. - Starbuck"
    $ scene_manager = Scene()
    $ scene_manager.update_actor(stephanie, display_transform = character_left_flipped, position = "sitting")
    $ scene_manager.update_actor(nora, position = "sitting")
    "You catch a cab to [nora.title]'s place with her and [stephanie.possessive_title]."
    #TODO write some foreplay that can happen here if public sexual acts are legal.
    #EG: Girls take their tops off, put their hands in MC's pants, a quick blowjob, ETC.
    "You sit between the two women. [stephanie.title] has her hand on one of your legs and [nora.possessive_title] has a hand on your crotch..."
    nora "I can't wait to get home, I've been looking forward to this all week."
    "[stephanie.title] starts to kiss you on your neck, then nuzzles up against your ear, whispering."
    stephanie "I hope it's my turn this week..."
    $ mc.change_locked_clarity(20)
    $ nora.change_arousal(25)
    $ stephanie.change_arousal(25)
    nora "I don't know what you just said, but I just felt him twitch."
    "You see the cab driver look back at you in the rear view mirror. He has a smile on his face."
    "You get to [nora.title]'s place and soon you are walking in the door with the two women."
    $ mc.change_location(nora.home)
    $ scene_manager.update_actor(stephanie, display_transform = character_right, position = stephanie.idle_pose)
    $ scene_manager.update_actor(nora, display_transform = character_center, position = nora.idle_pose)
    stephanie "Finally! Alright [stephanie.mc_title], what's the plan for tonight?"
    menu:
        "Train [stephanie.fname]":  #We fuck Stephanie week 1 usually
            call stephanie_nora_teamup_train_stephanie_label from _train_steph_during_teamup_01
        "Train [nora.fname]" if not nora.has_taboo("vaginal_sex"):
            call stephanie_nora_teamup_train_nora_label from _train_nora_during_teamup_02
        "Train Both Women\n{menu_red}Not yet written{/menu_red} (disabled)":
            pass
        "Just Have Fun\n{menu_red}Not yet written{/menu_red} (disabled)":
            pass
    return

### Nora Training Labels ###

label stephanie_nora_teamup_train_nora_label():     #Choose to train Nora
    $ training_subject = ""
    call stephanie_nora_teamup_choose_trainable_label(nora)
    $ training_subject = _return
    if nora.get_opinion_score(training_subject) == 2:    #She already loves it
        nora "I see. I'm not sure how effective the training will be though. I already love [training_subject]."
        mc.name "True, but I'd like to practice training technique, in general."
        nora "Hmmm, okay."


    $ nora.increase_opinion_score(training_subject)
    return


### Stephanie Training Labels ###

label stephanie_nora_teamup_train_stephanie_label():        #Choose to train Stephanie
    $ training_subject = ""
    call stephanie_nora_teamup_choose_trainable_label(stephanie)
    $ training_subject = _return
    $ training_dialogue = opinion_training_get_dialogue(training_subject)
    if stephanie.get_opinion_topic(training_subject) == 2:    #She already loves it
        stephanie "Really? Why though? I already love [training_subject]."
        mc.name "I know, but I'd like to practice training technique, in general."
        stephanie "I guess..."
    elif stephanie.get_opinion_topic(training_subject) == -2:    #She hates it.
        stephanie "Ohhh boy. Okay, I probably should have seen this coming."
        mc.name "We can't tell how successful your training is if we don't train something you truly hate."
        stephanie "Yeah... but [training_subject]???"
        "She lets out a long sigh."
        stephanie "Alright. I've seen this work before. Let's do this."
    else:
        stephanie "Hmm... Okay, that seems reasonable."
    "[stephanie.possessive_title!c] produces a vial of serum from her bag and quickly drinks it down while [nora.title] gets naked."
    $ scene_manager.strip_full_outfit(nora, strip_feet = True)
    $ mc.change_locked_clarity(20, nora)
    "You check out [nora.possessive_title] while [stephanie.title] takes a few seconds to let the serum take effect."
    "She opens her eyes and see her former boss is already naked."
    stephanie "Oh! Sorry just a moment..."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "stand3", z_order = 10)
    "[stephanie.title] starts to strip down also while [nora.possessive_title] turns to you and starts to pull down your pants."
    $ scene_manager.strip_full_outfit(stephanie, strip_feet = True)
    "You strip down as well. It is time to get things started."
    call stephanie_nora_teamup_train_stephanie_base_1_label(training_subject, training_dialogue) from _base_1_label_call_for_now_01

    return

label stephanie_nora_teamup_train_stephanie_base_1_label(training_subject, training_dialogue):
    mc.name "[stephanie.title], get on your knees and we'll start this up slow."
    stephanie "Mmm, sounds good."
    $ scene_manager.update_actor(stephanie, display_transform = character_center_flipped, position = "blowjob", z_order = 10)
    $ scene_manager.update_actor(nora, display_transform = character_right, position = "blowjob")
    "Both girls get down on their knees but [stephanie.title] takes the initiative."
    "She opens her mouth and begins to eagerly suck your cock while [nora.possessive_title] watches."
    $ mc.change_locked_clarity(30, stephanie)
    $ play_blowjob_sound()
    "After several seconds, she lets up."
    nora "Here, let me have a turn."
    "[stephanie.possessive_title!c] holds the base of your cock and points it at [nora.title]'s face. She takes a few moments to lick it up and down, then opens up."
    "When [nora.possessive_title]'s mouth glides up and down your cock, it feels just as good, but in a different way."
    $ mc.change_locked_clarity(30, nora)
    "She uses more delicate licking and suction, but it teases you in all the right places."
    "After several seconds, she backs off."
    nora "Mmm. Alright, he's all yours."
    stephanie "Thanks..."
    "[stephanie.title] leans toward her former boss and kisses her. They make out for a few seconds before she turns back to you."
    "[nora.title] moves behind her and starts to grope her body."
    $ scene_manager.update_actor(nora, display_transform = character_center, position = "kneeling1", z_order = 1)
    $ play_mouthful_sound()
    "[stephanie.possessive_title!c] moans as her mouth engulfs your cock again."
    "You watch in awe as [stephanie.title]'s head bobs up and down on your erection while [nora.possessive_title] presses herself up against her back and gropes and fingers her."
    $ nora.change_arousal(5)
    $ stephanie.change_arousal(15)
    $ mc.change_locked_clarity(30, stephanie)
    "[stephanie.title] tries to concentrate on sucking you off but as her former boss gets her worked up, she is forced to pull off to moan and catch her breath."
    $ play_moan_sound()
    stephanie "Ohhhhh fuck... so good..."
    "She looks up at you and her eyes are glazing over in pleasure. You decide to start things out."
    mc.name "[training_dialogue[0]]..."
    $ stephanie.increase_opinion_score(training_subject)
    stephanie "Yeah... that sounds right..."
    "She looks down and opens her mouth, swallowing your cock once again."
    $ play_mouthful_sound()
    $ nora.change_arousal(5)
    $ stephanie.change_arousal(25)
    $ mc.change_locked_clarity(30, stephanie)
    nora "That's it, swallow that big piece of meat..."
    "[nora.title] is whispering into her ear, encouraging her to please you. She has two fingers buried in her former student's pussy."
    ###Temporary dialogue###
    nora "...[training_dialogue[1]]..."
    "[stephanie.title] doesn't respond since her mouth is full of cock. Instead she looks up at you, clearly accepting what her former boss is saying."
    $ stephanie.increase_opinion_score(training_subject)
    $ play_mouthful_sound()
    $ nora.change_arousal(5)
    $ stephanie.change_arousal(25)
    $ mc.change_locked_clarity(30, stephanie)
    "She is trying to hard to please you but the hands on her body are winning the race to orgasm."
    "[stephanie.possessive_title!c] pops off your cock and gives up, letting pleasure overwhelm her."
    $ stephanie.change_arousal(25)
    stephanie "Oh fuck, oh my god, oh!!!"
    $ stephanie.have_orgasm(force_trance = True, sluttiness_increase_limit = 80, half_arousal = False, reset_arousal = False)
    "You watch as [stephanie.possessive_title] is brought to orgasm by [nora.title]."
    $ mc.change_locked_clarity(30, stephanie)
    "When her moans slow down, she looks up at you. She has the telltale signs of a trance."
    "One of [nora.possessive_title]'s hands goes to the back [stephanie.title]'s head, guiding her mouth back down onto your cock."
    nora "That's it..."
    mc.name "...[training_dialogue[2]]"
    stephanie "Mmmm... yessshhh..."
    $ stephanie.increase_opinion_score(training_subject)
    "She bobs her head up and down and moans her agreement as her mouth gets back to work. She has completely accepted your training."

    #Normally we would check and see if we move to orgasm or not, but until more scenes get fleshed out, go to orgasm no matter what here.
    call stephanie_nora_teamup_train_stephanie_base_1_orgasm(training_subject, training_dialogue) from _steph_nora_training_orgasm_base_01

    #Normally, we would check conditions to move on to the second scene here, but for now let's call it a night.
    $ scene_manager.update_actor(stephanie, display_transform = character_right, position = stephanie.idle_pose)
    $ scene_manager.update_actor(nora, display_transform = character_center, position = nora.idle_pose)
    "The two girls turn to you."
    call stephanie_nora_teamup_outro_label() from _stephanie_nora_teamup_train_steph_outro_call_01
    return




label stephanie_nora_teamup_train_stephanie_base_1_orgasm(training_subject, training_dialogue):
    $ mc.change_arousal(50)
    "Having these two beautiful women on their knees before you is too much. The soft talented mouth of [stephanie.title] is driving you to orgasm."
    mc.name "Oh fuck, that's it. I'm gonna cum!"
    if training_subject == "being covered in cum" or training_subject == "cum facials":
        mc.name "Show me what you've learned tonight!"
        "She quickly pulls off with her mouth, but grabs your cock with both hands, one stroking it, and the other at the base, pointing it at her face."
        stephanie "Yes! Cover me in your cum [stephanie.mc_title]!"
        "Her hands and eager voice drive you over the edge."
        $ stephanie.cum_on_face()
        $ ClimaxController.manual_clarity_release(climax_type = "face", person = stephanie)
        $ scene_manager.update_actor(stephanie, display_transform = character_center_flipped, position = "blowjob", z_order = 10)
        "After a long night of drinking and teasing, your orgasm is explosive, blasting [stephanie.title] in the face with multiple waves of cum."
        stephanie "Ohhhh fuck yes..."
        "When you finish, she carefully opens her eyes. You look down at cum covered face with satisfaction."
        nora "Wow, let me have some..."
        "[nora.title] leans around [stephanie.possessive_title], and licks some of your cum off her cheek."
    else:
        if training_subject == "drinking cum":
            mc.name "Show me what you've learned tonight!"
        $ play_mouthful_sound()
        "[stephanie.title] moans but makes no motion to stop sucking you off as your orgasm swiftly approaches."
        "With a couple more head bobs, she pushes you over the edge."
        $ stephanie.cum_in_mouth()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = stephanie)
        $ scene_manager.update_actor(stephanie, display_transform = character_center_flipped, position = "blowjob", z_order = 10)
        "When you start to cum, [stephanie.title] pulls back until just the tip is still in her mouth, and eagerly reaches up and strokes you with her hand."
        "After a long night of drinking and teasing, your orgasm is explosive, cumming so much is starts to leak out the sides of her mouth and down her chin."
        "Once you are finished, she uses her hand to milk the last of your cum from your shaft before pulling off."
        nora "Don't you dare swallow until I get some!"
    $ nora.cum_in_mouth()
    $ scene_manager.update_actor(nora, display_transform = character_right, position = "kissing")
    $ scene_manager.update_actor(stephanie, display_transform = character_right, position = "walking_away", z_order = 10)
    "The two girls stand up and [nora.title] immediately spins [stephanie.possessive_title] around. The embrace and immediately start making out."
    "[stephanie.title]'s ass is directly in front of your face, so you give it a couple playful spanks."
    $ play_spank_sound()
    "Your swats make her moan as the two girls swap your cum back and forth for a bit."
    "After several moments, their lips part, and you hear the sound of swallowing from both of them..."
    $ play_swallow_sound()
    $ mc.change_locked_clarity(10, stephanie)
    return




### Train Both Training Labels ###
label stephanie_nora_teamup_train_both_label():         #Attempt to train both girls at the same time.
    $ training_subject = ""
    call stephanie_nora_teamup_choose_trainable_label(nora)
    $ training_subject = _return


    pass
    return

label stephanie_nora_teamup_just_sex_label():           #Just have a fun threesome


    pass
    return

label stephanie_nora_teamup_choose_trainable_label(the_person):
    #NOTE
    # Training dialogue can be found in game/trainables/opinion_trainables.rpy
    # Currently writing for trainables is in progress.
    # I have defaulted this label to grab training for "anal creampies" since that is currently the only finished section.
    # Once more training dialogie is complete, I'll add in a method for choosing other things.
    stephanie "Okay, and what are we training tonight?"
    "You think about it for a moment."
    "Note: It is recommended to check [the_person.title]'s opinions before choosing."
    menu:
        # "Anal Creampies":
        #     return "anal creampies"
        # "Anal Sex":
        #     return "anal sex"
        # "Fucking Bareback":
        #     return "bareback sex"
        "Getting Covered in Cum":
            return "being covered in cum"
        # "Getting Fingered":
        #     return "being fingered"
        "Being Submissive":
            return "being submissive"
        "Big Dicks":
            return "big dicks"
        # "Cheating":
        #     return "cheating on men"
        # "Vaginal Creampies":
        #     return "creampies"
        "Receiving Cum Facials":
            return "cum facials"
        # "Fucking Doggy Style":
        #     return "doggy style sex"
        "Swallowing Cum":
            return "drinking cum"
        # "Getting Eaten Out":
        #     return "getting head"
        "Giving Blowjobs":
            return "giving blowjobs"
        # "Giving Handjobs":
        #     return "giving handjobs"
        # "Giving Tit Fucks":
        #     return "giving tit fucks"
        # "Committing Incest":
        #     return "incest"
        # "Kissing":
        #     return "kissing"
        # "Wearing Lingerie":
        #     return "lingerie"
        # "Masturbating":
        #     return "masturbating"
        # "Fucking Missionary Style":
        #     return "missionary style sex"
        "Being Naked":
            return "not wearing anything"
        "Not Wearing Underwear":
            return "not wearing underwear"
        # "Multiple Romantic Partners":
        #     return "polyamory"
        # "Having Sex in Public":
        #     return "public sex"
        # "Fucking While Standing Up":
        #     return "sex standing up"
        "Showing Off Your Ass":
            return "showing her ass"
        "Showing Off Your Tits":
            return "showing her tits"
        "Wearing Skimpy Outfits":
            return "skimpy outfits"
        "Wearing Skimpy Uniforms":
            return "skimpy uniforms"
        # "Taking Control During Sex":
        #     return "taking control"
        # "Having Threesomes":
        #     return "threesomes"
        # "Vaginal Sex":
        #     return "vaginal sex"
    return "giving blowjobs"

label stephanie_nora_teamup_outro_label():
    mc.name "Well... I think that's it for me for tonight."
    nora "[stephanie.name], are you spending the night?"
    stephanie "Ahhh, yeah I think I better, I'm not sure my legs can handle walking home right now..."
    mc.name "So... same time next week?"
    stephanie "Only if you want to fuck around with us again."
    "[stephanie.title] teases you."
    mc.name "Alright, I'm going to head home. Have a good night."
    nora "Goodnight [nora.mc_title]."
    $ mc.change_locked_clarity(50)
    "You take one last look at the two naked beauties before you turn around."
    $ scene_manager.clear_scene()
    "You see yourself out of [nora.possessive_title]'s apartment and start the walk home."
    "You run a quick recap in your head."
    "Another successful threesome with your former lab partners."
    "Each week you continue to mold them into the perfect sluts, and they even train each other!"
    $ mc.change_location(bedroom)
    "You get home and get to bed."
    return
