# We pick up this story after the event where she is afraid of losing her job.
# First, we tie this thread up by making sure she has pleased her boss with sexual favours. She may have only gotten bigger tits at this point.

label mom_lust_story_bridge_label(the_person):    #We can make this an on talk event.
    $ the_person.draw_person(emotion = "happy")
    $ the_person.progress.lust_step = 6
    "When you walk into the room, you notice [the_person.possessive_title]. She is humming and seems to be in a great mood."
    mc.name "Hey [the_person.title]. You seem like you are having a good day! How was work?"
    if the_person.event_triggers_dict.get("mom_replacement_approach", "seduce") == "seduce":
        the_person "Oh! Hello honey! It was a great day indeed!"
        the_person "My boss has really been having it rough lately, but it has really given me the opportunity to shine!"
        the_person "There is something so satisfying about helping a man let go of all his stress for even just a few minutes when you get down on your knees and..."
        if the_person.love > 40 or the_person.is_girlfriend:
            the_person "I umm... sorry, this probably isn't something you are interested hearing about..."
        elif the_person.opinion.incest > 0:
            the_person "You know... I love to make ALL the men in my life's day better once in a while!"
        else:
            the_person "Well, let's just say that more and more of my time lately has been spent under his desk!"
        $ mc.change_locked_clarity(20)
    else:
        the_person "Ah, you could say that. I think I had a breakthrough with my boss."
        the_person "He has been so stressed out lately, and I could tell that just teasing him with my tits was really getting to him..."
        the_person "So I felt like it would be okay if I could help him relieve his stress some. Just a little!"
        the_person "So when he had his lunch break, I got down below his desk and... well..."
        menu:
            "Congratulate her":
                mc.name "Hey, that's great! Good job [the_person.title], I knew you could do it."
                the_person "Thank you [the_person.mc_title]. It's a huge weight off of my shoulders, that's for sure."

            "Ask how she did it":
                mc.name "That's great! So, how did you do it?"
                the_person "Well, I... Are you sure you want me to tell you this? Oh, I guess it's not a big deal."
                the_person "I asked to have a discussion with him in his office during lunch today."
                the_person "He wasn't happy about having his lunch interrupted, but he seemed much more interested when I took my top off."
                mc.name "Mmhm? Go on."
                the_person "Once I had his attention I told him I was really worried about how stressed he was. He asked me what I was going to do about it."
                "She blushes a little and shrugs innocently."
                the_person "So I got onto my knees and sucked him dry."
                $ mc.change_locked_clarity(30)
                the_person "When he {i}finished{/i} he couldn't stop talking about how glad he was he hired me!"
                the_person "Thank you for your help [the_person.mc_title], I never would have gotten this promotion if it weren't for you!"
                mc.name "My pleasure [the_person.title], I'm just happy that you're doing what you enjoy."
                "She smiles and gives you a quick hug." #Copy the seduction menu choices
    "Things with [the_person.possessive_title] and her boss seem to be going well... but is this something you really want to continue?"
    "How much longer will it be until he is fucking her on the regular? Is that what you want? Would that make her happy?"
    "Maybe instead of encouraging things... you should try and hire her yourself? It is something to think about anyway."
    "For now, you are just happy that she is happy."
    $ add_mom_lust_boss_prostitutes_intro_action()
    return

#60
label mom_lust_boss_prostitutes_intro_label(the_person):    #At 60 sluttiness, she finds out her boss is using prostitutes after finding his bank statements
    $ label_outcome = None
    $ the_person.draw_person(emotion = "sad", position = "stand4")
    $ the_person.progress.lust_step = 7
    "You walk into the kitchen and see [the_person.possessive_title]. She seems upset."
    mc.name "Hey [the_person.title]... are you okay?"
    the_person "Yes... yes I'm just fine... of course..."
    mc.name "You don't sound fine."
    "She lets out a long sigh."
    $ the_person.draw_person(position = "stand2")
    the_person "It's my boss. Today I was helping out with some financial files when I noticed it."
    the_person "He... he's been paying for prostitutes... with company money!"
    mc.name "Wow, that's terrible."
    the_person "I know!"
    "Hmmm, that seems like a big problem. You wonder if you could get your hands on those documents for future blackmail material..."
    mc.name "Did you... happen to get a copy of the financial documents?"
    the_person "The documents? I... yes I guess I do. I grabbed them and took them to him to confront him."
    the_person "I went straight to him and was just like... why am I even there!?! I thought that what I was doing was enough for him..."
    the_person "He just said he has needs that go beyond blowjobs, but that he still appreciates what I do."
    mc.name "Wait... why are you upset exactly?"
    the_person "Don't you get it? He promised not to hire someone to replace me, but by hiring a prostitute he is basically doing that anyway!"
    mc.name "So you're upset because... he ISN'T having sex with you?"
    "Suddenly her face turns red."
    the_person "No, that's... errr..."
    the_person "I wasn't going to take things that far with him."
    mc.name "But now you want to. Don't you?"
    "[the_person.title] bites her lip and looks away from you."
    if the_person.is_girlfriend or the_person.is_willing(standing_doggy):
        $ label_outcome = "vaginal"
        the_person "I would never... do something that I thought would hurt you."
        mc.name "And I feel the same way. But what if I told you it's okay?"
        "She seems genuinely surprised by your statement."
        the_person "That is crazy... why would you say that?"
        mc.name "I guess because it genuinely would not bother me. Besides..."
        "You grab her ass and pull her close to you."
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(20)
        the_person "Oh!"
        mc.name "I think we both know you'll still come home to daddy."
    elif the_person.is_willing(anal_standing):
        $ label_outcome = "anal"
        the_person "I... I don't want to do something that might drive a wedge between us."
        the_person "I assumed that going that far with him would hurt you..."
        mc.name "That is very kind of you, but what if I told you it's okay?"
        "She seems genuinely surprised by your statement."
        the_person "That is crazy... why would you say that?"
        mc.name "I guess because it genuinely would not bother me. Besides..."
        "You grab her ass and pull her close to you."
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(20)
        the_person "Oh!"
        mc.name "You'll still be coming home to me every night."
    elif the_person.love >= 40:
        the_person "I don't know if I want to answer that question."
        mc.name "It seems like a pretty natural thing to me. Why wouldn't you want to fuck him?"
        the_person "[the_person.mc_title]! There's no reason to be so coarse."
        mc.name "You do though, right?"
        "She sighs and nods."
        the_person "Yes. I do."
        mc.name "I'm not sure why that would be an issue. You'd be doing him and the company a service."
        mc.name "And if it is something you want, where are the downsides?"
        the_person "I wasn't sure if it was something that you would be okay with."
        the_person "You mean so much to me, and for me to go and do something like that would feel like some sort of a betrayal of trust."
        mc.name "What if I tell you that it's okay?"
        the_person "I... I guess that would make the decision easy!"
    else:
        the_person "It feels crazy. To have sex with my own boss! It isn't right."
        mc.name "It seems like a pretty natural thing to me. Why wouldn't you want to fuck him?"
        the_person "[the_person.mc_title]! There's no reason to be so coarse."
        mc.name "Just do it. See what happens."
        "She sighs and shakes her head, but then looks up at you."
        the_person "I guess it couldn't hurt to try."
        mc.name "You'd be doing him and the company a service. And if you have fun doing it? Why not?"

    if label_outcome == None:
        $ the_person.draw_person(position = "kissing")
        "[the_person.possessive_title!c] pulls you in for a hug."
        "After a few moments, she backs away from you."

    elif label_outcome != None:   #Anal or Vaginal, the setup is mostly the same.
        mc.name "We'd probably better get you prepared for what is likely to happen."
        if the_person.opinion.incest > 0:
            "You see a sudden flash of interest in her eyes"
        if the_person.event_triggers_dict.get("anal_revisit_complete", False) == False and label_outcome == "anal":
            "You start to try to turn her around to face the kitchen counter but she resists you."
            the_person "[the_person.mc_title], don't joke like that. You know we can't have sex."
            mc.name "No, but I think there is another way we could get you ready for it."
            the_person "What? What do you mean?"
            mc.name "There's another way for me to fill you up without risking you getting pregnant..."
            if the_person.event_triggers_dict.get("anal_revisit_count", 0) == 0:
                the_person "Oh my god, you mean my butt! I... That's not where that goes, [the_person.mc_title]!"
                mc.name "Oh... so you would prefer I put it, how'd you say it, *where that goes*?"
                the_person "Of course not! You're my son, which means we absolutely should not be having sex."
                mc.name "That's why we should try anal. I couldn't get you pregnant, so it's not really incest."
                the_person "I don't know..."
                mc.name "How different is it from using your mouth? Or your tits?"
                the_person "I kind of see what you mean..."
            else:
                the_person "We shouldn't... not again."
                mc.name "We could just fuck..."
                the_person "No! We shouldn't do that either!"
                mc.name "I'm trying to get you ready for what is going to happen at work [the_person.title]."
                mc.name "Do you really want to go into that completely unprepared?"

            "She stops and thinks for a moment."
            the_person "Okay... Just make sure you get it in the right... errr.... hole..."
        elif the_person.event_triggers_dict.get("vaginal_revisit_complete", False) == False and label_outcome == "vaginal":
            the_person "Except my boss probably isn't going to stick it my ass... at first anyway..."
            mc.name "Right, which is why we should just fuck, so we can prepare you for the real thing."
            the_person "[the_person.mc_title], don't joke like that. You know we can't have REAL sex."
            if the_person.event_triggers_dict.get("vaginal_revisit_count", 0) == 0:
                mc.name "[the_person.title], I'm already dicking you down regularly in the ass, don't you think it about time we did it right?"
                the_person "Oh my god [the_person.mc_title], NOTHING about our relationship is right!"
                the_person "A mother and a son shouldn't be doing ANY of the things we've been doing!"
                mc.name "I'm not just your son though, am I? We've done so much together already, isn't this just natural?"
                the_person "Nothing about this is natural..."
                mc.name "Yeah it is. It's natural for a young, virile man to want to fuck a beautiful woman like you."
                mc.name "And it's natural for you, a beautiful woman, to want to get fucked by someone she loves and trusts."
                mc.name "Especially with how things are going at your work... Don't you want to prove your loyalty to your family?"
                the_person "This isn't about loyalty..."
                mc.name "I mean, you said it earlier, you would never do something you thought would hurt me. I feel the same way."
                mc.name "This isn't going to hurt. It is going bring our family together in a way that will hold up against all adversity."
            else:
                the_person "We need to stop [the_person.mc_title]. We talked about this, this is too far!"
                mc.name "You don't want to stop here though, do you?"
                "She sighs and shrugs."
                the_person "I don't know what I want... I want to be a good mother!"
                mc.name "I want YOU to be ready for anything that may happen at your work, to prepare you completely."
            "After a long pause, she sighs softly and nods."
            the_person "Okay, just to prepare me for my boss... okay?"
            mc.name "Of course."

        mc.name "So I'm thinking the most likely scenario is that he bends you over his desk."
        the_person "That sounds about right... should I pretend you are my boss while we are doing this?"
        mc.name "That is probably for the best. I'll pretend to be him as well. Here we go."
        "You turn her around and bend her over the kitchen counter."
        $ the_person.draw_person(position = "standing_doggy")
        mc.name "Alright you little slut. You've been waving this ass around my office all day, it is time someone put it to good use."
        the_person "OH... yes sir..."
        if the_person.vagina_available and the_person.vagina_visible:
            "You give [the_person.possessive_title]'s bare ass a solid spank, once on each cheek."
        else:
            mc.name "Let's get these off and see what you're working with bitch."
            $ the_person.strip_to_vagina(prefer_half_off = False, position = "standing_doggy")
            "Once her ass is bare, you give it a solid spank, once on each cheek."
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(40)
        "She gives a whimper, but at the end it turns into a slight moan."
        mc.name "Of course. I should have known the office slut would like a little spanking. You like this whore?"
        "You give her several more firm spanks. She moans audibly after the last one."
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(40)
        mc.name "You know I can see everything from back here, right? Damn, look at how wet you are getting."
        "You slide two fingers into her rapidly dampening pussy. Her body reflexively pushes back against you a bit."
        the_person "Aahh! Mmm... Boss, don't you have something... else for me?"
        mc.name "Of course a slut like you would ask to get dicked down. Well, you're lucky I'm in a good mood."
        "You pull down your pants and underwear, your hard on springing free."
        "You take it in your hand and use it to smack [the_person.possessive_title]'s ass cheeks a couple times. They wobble enticingly."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(50)
        if label_outcome =="anal":
            "You put your fingers back inside of [the_person.title]'s pussy, then pull them out. You wipe her juices onto your cock, then repeat the process a few times."
            "You gather a large amount of saliva in your mouth then let it slide out of your mouth, landing right next to her puckered hole."
            "You take your slightly lubricated cock and work the saliva all around her anus. You feel like you are ready, and put the tip against her and begin to push."
            the_person "Oh fuck... don't we need a little more lube? That..."
            mc.name "Listen slut, your holes are for MY pleasure. Just be thankful I'm choosing you to be my cumdump today."
            the_person "Oh... yes... yes sir!"
            "You put one hand on her hip, and with the other hand you grab her hair and start to earnestly push."
            "She gasps when her sphincter gives way, and after several seconds of slow, delicious penetration, you bottom out inside [the_person.possessive_title]'s forbidden hole."
            $ the_person.break_taboo("anal_sex", add_to_log = False)
            $ the_person.change_arousal(-10)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(15)
            the_person "Ohhh fuckkkk... please tell me... it's all the way in..."
            mc.name "Let's check..."
            "You slowly pull yourself all the way out. [the_person.possessive_title] back door gapes a little."
            "You push forward and slide into her ass much easier this time."
            $ the_person.change_arousal(5)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(15)
            the_person "Ohhhh ffffuck... [the_person.mc_title]..."
            mc.name "Boss. I'm your boss."
            the_person "Oh! Right..."
            "You pull back on her hair a bit, emphasizing your point."
            mc.name "Alright you little butt slut, let's take you for a ride and see what you can do."
            "You give [the_person.title]'s ass a few slow strokes, but it is clear that she is ready for more."
            "You pull most of the way out and then give your cock another couple rounds of saliva."
            "You let go of her hair and give her ass a couple more spanks, then grab her hips."
            "You push forward with increased urgency and begin to fuck [the_person.possessive_title]'s ass."
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(15)
            the_person "Ohhhh ... my god... b...boss!"
            "With your hands on [the_person.title]'s hips, you start to give her ass an eager pounding."
            $ play_moan_sound()
            "[the_person.possessive_title!c] moans and starts matching each hip movement of yours with a movement of her own."
            the_person "Oh god, you fuck me so good boss, I can barely keep up!"
            "[the_person.possessive_title!c] reaches back with one hand and pulls her ass cheek back, giving you a great view of her puckered hole stretched wide to accommodate you."
            $ the_person.change_arousal(25)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(25)
            "Having [the_person.possessive_title] bent over the kitchen counter is really turning you on. You feel yourself getting close to release."
            call anal_standing_double_orgasm(the_person, kitchen, make_counter()) from _jen_anal_boss_practice_01

        else:
            "You put one hand on her hip and the other on your cock. You run it up and down her wet slit a few times."
            mc.name "Wow, you really are ready for this, aren't you? My little office slut, always ready to get bent over the nearest piece of furniture in my office."
            the_person "I am! I've been waiting for you to do this for so long boss..."
            mc.name "I'll bet."
            "You push forward and easily slip inside [the_person.possessive_title] slippery cunt."
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(15)
            $ the_person.break_taboo("vaginal_sex")
            the_person "Oh fuck!... ohhhhh..."
            mc.name "Finally got what you wanted, whore?"
            "You move your hips a little bit, stirring her womb a bit before you begin to thrust in and out of her."
            $ the_person.change_arousal(25)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(15)
            the_person "Oh god... honey... this... this isn't going to work!"
            mc.name "I'm your boss. Stick with the plan."
            the_person "I don't think I can... my boss's dick isn't nearly this big!"
            "Hmm... well that certainly brings a smile to your face."
            mc.name "Hmm... well... I guess maybe we could try something else..."
            "As you start to pull out, [the_person.possessive_title]'s ass pushes back, keeping you inside of her."
            the_person "Don't you dare! Keep going I'm so close..."
            mc.name "Oh! Okay, well in that case..."
            "You grab her hips with both hands and start to aggressively move your hips again."
            $ the_person.change_arousal(30)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(20)
            if the_person.event_triggers_dict.get("vaginal_revisit_complete", False) == False:
                the_person "Oh my god, this is so wrong, but don't stop! Give it to me [the_person.mc_title]!"
            else:
                the_person "Oh my god, I can't believe I get to come home to this everyday! Give it to me [the_person.mc_title]!"
            "Motivated by her words, you thrust yourself in and out of [the_person.possessive_title] even harder."
            "With each thrust a lewd slapping noise fills the kitchen. Her moans are getting louder and more desperate."
            $ the_person.change_arousal(30)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(20)
            the_person "Honey I... I...!!!"
            $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 80, half_arousal = False, reset_arousal = False)
            "Suddenly her knees buckle and she starts to cum. Urgent moans and gasps escape her lips as you fuck her all the way through it."
            "Her pussy quivers and spasms with every thrust. Watching [the_person.possessive_title] cum all around your cock has you getting ready to finish also."
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(50)
            mc.name "Oh my god [the_person.title], I'm gonna cum too!"
            if the_person.wants_creampie:
                the_person "Don't you dare pull out! Give it to mommy!"
                "Her hand reaches back and grabs your hip, urging you deep inside of her."
                "You grab her hips and thrust as deep as you can as you begin to cum."
                $ the_person.cum_in_vagina()
                $ the_person.draw_person(position = "standing_doggy")
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", person = the_person)
                the_person "Yes! Fill me up [the_person.mc_title]!"
                "You keep your cock fully inserted as you cum wave after wave. Each spurt going as deep inside her as you can manage."
                "Once you are finished, you don't pull back for several seconds, savouring your intense orgasm."
            else:
                the_person "Pull out... you need to pull out!"
                "Her hand reaches back and pushes against your hip. You decide to do what she says, this time anyway."
                "You pull back and take your cock in your hand and stroke it, right as you are getting ready to finish."
                $ the_person.cum_on_ass()
                $ the_person.draw_person(position = "standing_doggy")
                $ ClimaxController.manual_clarity_release(climax_type = "body", person = the_person)
                "You cum hard, with the initial few spurts landing on her ass and lower back."
                "You do your best to coat each ass cheek equally as you plaster her with your cum."
                the_person "Oh my god... it is so warm!"
                "When you finish, you stand there for several more seconds, enjoying the view of [the_person.possessive_title]'s cum covered ass bent over the kitchen counter."
            if the_person.event_triggers_dict.get("vaginal_revisit_complete", False) == False:
                "Progress with her has been slow, but steady. You resolve yourself to do whatever it takes to make this a regular occurrence."
            else:
                "Life at home has been amazing ever since you corrupted [the_person.title] into taking your cock like this whenever you want."
        "After several seconds, [the_person.possessive_title] stands up and turns around, facing you."
        $ the_person.draw_person(position = the_person.idle_pose)
        the_person "Sorry I umm... got a little carried away there..."
        mc.name "Yeah. Me too."
        "She clears her throat and there are several seconds of awkward silence."
        the_person "Well... I'm going to go take a quick shower I think."
        $ label_outcome = None
    the_person "I'm surprised you're okay with things between me and my boss... but thank you for being so understanding."
    "[the_person.title] leans forward and gives you a quick kiss on the cheek."
    if the_person.opinion.incest > 0:
        the_person "I'm so blessed to have you in my life too."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks out of the room."
    $ clear_scene()
    "Well, you've given her permission to fuck her boss. You wonder what kind of things this might set in motion."
    "Her boss is a very influential man. If you remember correctly he is a member of the city council."
    "Maybe if things go well, you could convince him to help you with some things from his council position?"
    "Or... knowing that he is a married man... you could force his hand a bit."
    "You decide for now to just wait and follow up with [the_person.title] in a few days and see how things go."
    $ add_mom_lust_boss_prostitute_followup_action()
    return

label mom_lust_boss_prostitute_followup_label(the_person):
    $ the_person.draw_person()
    "You walk into the kitchen. You notice [the_person.possessive_title] is there."
    "It has been a few days since you gave her the green light to fuck her boss. You wonder how it's going."
    mc.name "Oh hey [the_person.title]. Have a good day at work?"
    the_person "Oh hi [the_person.mc_title]. Yeah! It went pretty good."
    mc.name "Yeah? Any updates on the issue with the boss hiring hookers?"
    the_person "[the_person.mc_title]! They're escorts. No reason to give such nasty names to sex workers."
    the_person "But to answer your question... I don't think he is going to be using any prostitutes anymore."
    the_person "Things aren't great for him at home, but at work I'll be able to help him with his needs..."
    the_person "So he can concentrate on things around the office, of course."
    mc.name "That's great [the_person.title]."
    if not the_person.on_birth_control and not the_person.is_pregnant:
        the_person "There is one thing I had to do though. As much as I enjoy working with him, I certainly don't want there to be any little ones..."
        the_person "During my lunch break today I swung by the gynaecologist and got a birth control prescription."
        $ start_birth_control(the_person, True)
        $ the_person.change_baby_desire(-40)
    elif the_person.is_pregnant:
        the_person "I'm a little bit concerned though... he might get jealous about me getting pregnant. Or WORSE."
        the_person "He might think it's... HIS."
        the_person "After this little one comes, I'm going to go on birth control for as long as I'm working there."
    else:
        the_person "I stopped by the gynaecologist on my lunch break today too. I got tested to make sure I am STI free."
        the_person "I also made sure to update my birth control. As much as I enjoy working with him, I certainly don't want there to be any little ones..."
        $ the_person.update_birth_control_knowledge()
        $ the_person.change_baby_desire(-40)
    mc.name "That is understandable."
    the_person "I've got him wearing condoms also, but knowing men who knows how long he will put up with that."
    "Sounds like for as long as [the_person.title] is working at this office, she is going to be on birth control."
    "Maybe if you can get some influence with her boss, you could convince her to quit and maybe she would be willing to go off it..."
    mc.name "Alright, I'm glad things are going well at work, I'm gonna go to my room for a bit."
    the_person "Okay honey."
    $ clear_scene()
    $ the_person.progress.lust_step = 8
    $ the_person.event_triggers_dict["mom_office_slutty_level"] = 3
    $ add_mom_boss_phase_two_checkup_action()
    return

label mom_boss_phase_two_checkup_label():
    $ mom.progress.lust_step = 9
    if mom.event_triggers_dict.get("boss_teamup", False) == True:
        "It has been a while since you talked to [mom.possessive_title]'s boss about helping him seduce her."
        "With the recent news that they've finally started fucking, you figure it is probably about time to catch up with him."
    else:
        "With the news that [mom.possessive_title] is finally fucking her boss, you feel like you should probably pay him a visit."
        "You're certain he has noticed how fast she has gone from conservative employee to office slut."
        "You wonder if you could find a way to work with him, or even get some sort of compensation from him for it."
    "You should swing by [mom.title]'s office sometime and talk to her boss."
    $ add_mom_lust_boss_bareback_intro_action()
    return

label mom_lust_boss_bareback_intro_label(): #Room entry event where we talk to Jennifer's boss
    # This event determines the final path we take to try and control Jennifer's boss
    # If we team up with him, he keeps fucking Jennifer, but we gain a business partner and his vote in the council
    # If we make him a rival, we must begin to take steps to blackmail him. Jennifer should already have prostitution information we can steal.
    # If we cooperate, continue corrupting Jennifer.
    # If we make a rival, if we continue to corrupt jennifer, she eventually gives up her ass and comes home struggling to walk straight
    # Hold there until we manage to blackmail him

    $ mom.progress.lust_step = 10
    $ mom_boss_quick_name = "Mr. " + iris.last_name
    $ the_person = get_mom_secretary()
    $ the_person.draw_person(position = "sitting")
    $ first_meeting = not (mom.event_triggers_dict.get("boss_teamup", False) or mom.event_triggers_dict.get("boss_rival", False))
    "You step up to the counter where the secretary is sitting."
    mc.name "Hello. I was hoping to talk to [mom_boss_quick_name]."
    # If we've seen the boss before, we are expected.
    if not first_meeting:
        "She looks up at and quickly recognizes you."
        the_person "Ah! Mr. [mc.last_name]. I was told you would be coming by, and to let him know as soon as you arrived."
        the_person "Give me one second."
        "She picks up the phone and dials a number."
        the_person "Ah yes, sir? [mc.last_name] is here to see you. Yes you did say that. Yes I'll send him right in."
        "She hangs up her phone."
        the_person "He will see you now. Do you remember the way?"
        mc.name "Yes I do. Thank you."
    else:
        "She looks up at you, and looks confused."
        the_person "His schedule is empty... did you have an appointment?"
        mc.name "I don't, but I was hoping to set one up. I need to speak to [mom_boss_quick_name]."
        "She nods and turns to her computer briefly, typing something in before turning back to you."
        the_person "Okay, and who should I say is trying to reach him?"
        menu:
            "Reference your business":
                $ business_name = mc.business.name
                mc.name "Mr. [mc.last_name]. I'm here representing [business_name]. I have work I need to discuss with him."

            "Reference [mom.title]":
                mc.name "Mr. [mc.last_name]. I'm the son of [mom.name], there's a family matter I need to discuss with him."
        "She types on her computer again."
        the_person "Understood. I'll let him know you are here. Give me one second."
        "You step back from the desk for a moment while she picks up the phone. You avoid listening over the conversation."
        "After a minute, she hangs up."
        the_person "Mr. [mc.last_name]? He is available to see you now."
        the_person "He is up on the sixth floor, to the right."
        mc.name "Thank you."
    $ clear_scene()
    "You step onto the lift, riding it up to the sixth floor."
    $ renpy.show("luxury office", what = bg_manager.background("Luxury_Office_Background"), layer = "master")
    "Soon, you step into a luxurious business office. Sitting behind the only desk in the room is [mom_boss_quick_name]."
    if first_meeting:
        mom_boss_quick_name "Ah, Mr. [mc.last_name]. I know the last name well, but I didn't realise that my secretary had a son."
        mom_boss_quick_name "I'm not sure what brings you here..."
        mc.name "Oh, I'm sure you know exactly what I'm here to talk about."
        mc.name "How has [mom.fname] been performing? Ever since you hired her as your personal secretary?"
        mom_boss_quick_name "Well young man, I would say that she meets or exceeds expectations, but what kind of performance are you speaking about, specifically?"
        menu:
            "I've been helping you":
                $ mom.event_triggers_dict["boss_teamup"] = True
                mc.name "It has been amazing, hasn't it? The speed at which she has... adapted... to her job demands."
                mom_boss_quick_name "I'm not sure what you are getting at kid."
                mc.name "Alright, then, I'll speak plainly. When you first hired her, would you ever have expected to be able to bend her over your desk at will?"
                mom_boss_quick_name "Kid, if you think I've been having relations with your mom..."
                mc.name "There is no need to play dumb. I know full well what has been going on during her time here."
                mc.name "There is more to it than just that. I also run my own business, and I am in need of helpful partnerships."
                mc.name "I create and sell small pharmaceuticals that have helped many women get in touch with their more intimate desires."
                mom_boss_quick_name "You... you make drugs?"
                mc.name "Yes, of a sort. A new line of mind opening formulas that can do a number of things."
                mc.name "Unfortunately, time and volunteers for testing have been limited. But you've seen firsthand how quickly and effectively they can work."
                mom_boss_quick_name "Fuck... you're drugging your own mother?"
                mom_boss_quick_name "That is absolutely ruthless."
                "He sits back and thinks about what you've just revealed for a moment."

            "Watch your step":
                $ mom.event_triggers_dict["boss_rival"] = True
                "You need to be careful about what you say here. This room may very well be under surveillance right now."
                "You need to make him aware of your ulterior motives with him and your mother, but without revealing too much."
                mc.name "I just wanted to make sure you are aware that your personal indiscretions with her have not gone unnoticed."
                mc.name "You should be careful. Should these indiscretions be made public, it would be unfortunate for someone in your position."
                mom_boss_quick_name "Kid, if you think I've been having relations with your mom..."
                mc.name "There is no need to play dumb. I know full well what has been going on during her time here."
                "He sits back and thinks about what you've just revealed for a moment."
    elif mom.event_triggers_dict.get("boss_teamup", False):
        mom_boss_quick_name "Ah, Mr. [mc.last_name]. I figured you would be stopping by again."
        mom_boss_quick_name "I take it, since you're here, that you think you somehow have something to do with recent... progress that has been made."
        "He is careful not to outright confess his adulterous relationship with [mom.possessive_title]."
        mc.name "There is no need to play dumb. I know full well what has been going on during her time here."
        mc.name "There is more to it than just that. I also run my own business, and I am in need of helpful partnerships."
        mc.name "I create and sell small pharmaceuticals that have helped many women get in touch with their more intimate desires."
        mom_boss_quick_name "You... you make drugs?"
        mc.name "Yes, of a sort. A new line of mind opening formulas that can do a number of things."
        mc.name "Unfortunately, time and volunteers for testing have been limited. But you've seen firsthand how quickly and effectively they can work."
        mom_boss_quick_name "Fuck... you're drugging your own mother?"
        mom_boss_quick_name "That is absolutely ruthless."
        "He sits back and thinks about what you've just revealed for a moment."
    else:
        mom_boss_quick_name "Kid, I already told you once to get lost. Why are you back here?"
        "You need to be careful about what you say here. This room may very well be under surveillance right now."
        "You need to make him aware of your ulterior motives with him and your mother, but without revealing too much."
        mc.name "I just wanted to make sure you are aware that your personal indiscretions with her have not gone unnoticed."
        mc.name "You should be careful. Should these indiscretions be made public, it would be unfortunate for someone in your position."
        "He sits back and thinks about what you've just revealed for a moment."

    if mom.event_triggers_dict.get("boss_teamup", False):
        mom_boss_quick_name "You know, I think I almost believe you. But if you really want to go as far as some kind of business partnership, I'm going to need better proof."
        mc.name "Oh? And what kind of proof would you need?"
        mom_boss_quick_name "Your mom, she bends over my desk at my slightest whim now, but there is still one thing off limits that I can't seem to get around."
        mom_boss_quick_name "Every time, she makes me wear a fucking condom. Says she isn't willing to risk it, mentions me visiting prostitutes."
        mom_boss_quick_name "Make her beg me to take her bare. If you can do that, I'd be open to looking into some kind of... partnership."
        mc.name "Ah, that should be easy enough."
        "[mom_boss_quick_name] shakes his head at your words. He is still in disbelief."
        mom_boss_quick_name "Goddamm... your own mother..."
        mom_boss_quick_name "If what you are saying is really true, and you really have these capabilities, I'll make it worth your while."
        mc.name "Don't worry, she'll be begging you to slide raw into her hot cunt before you know it."
        mom_boss_quick_name "Whatever kid. I'm still not sure I believe you are for real. But I'll follow along, for now."
        mc.name "I'll swing by when it is done, and we can talk about other matters."
        "You stand up and turn, leaving the office."
        $ mc.location.show_background()
        "As you enter the lift, you think about what he is asking you to do."
        if mom.opinion.bareback_sex >= 2:
            "Thankfully, you've already convinced [mom.possessive_title] to love bareback sex, so it should only be a matter of time until she begs him for it."
            "You should just work on getting her a little more slutty."
        else:
            "It should be a fairly trivial matter, to change [mom.possessive_title]'s opinion to loving bareback sex."

        "Thankfully, you already know that she is on birth control, so there won't be any complications as a result."
        $ add_mom_lust_boss_bareback_followup_action()
    else:
        mom_boss_quick_name "You walk into my office... just to threaten ME?"
        mom_boss_quick_name "You know that you have no proof whatsoever?"
        mc.name "[mom.fname] has nothing to do with it. I'm talking about your time spent with ladies of the night."
        if mc.business.prostitution_is_legal:
            mc.name "I can't imagine things would do well at home if that kind of information went public."
        else:
            mc.name "It would be difficult to explain that away to the local prosecutor."
        "[mom_boss_quick_name] sighs, and then chuckles."
        mom_boss_quick_name "Kid, if you think anyone gives a rats ass about what I do with my spare time, you're mistaken."
        mom_boss_quick_name "Now get the fuck out of my office before I have you thrown out."
        mc.name "We'll see each other again, soon. After you learn to be more cooperative."
        "You don't wait for a response, you just get up and leave the office."
        $ mc.location.show_background()
        "As you enter the lift, you think about what you need to do break him."
        "What would his family think if they knew about his indiscretions?"
        "Or better yet, maybe you could seduce someone in his family... force you way in from the inside."
        "Would it break this man? To fuck his wife? Or his daughter? Both?"
        "Hopefully [mom.possessive_title] doesn't get too much retaliation for this while working here..."
        $ add_mom_lust_boss_anal_intro_action()
    return

# coop path
label mom_lust_boss_bareback_followup_label(the_person):
    $ the_person.draw_person()
    "You walk into the kitchen. You notice [the_person.possessive_title] is there."
    "You've managed to convince her to love bareback sex, you wonder if she has started taking her boss's dick bare yet."
    mc.name "Good evening [the_person.title], how are you?"
    the_person "Oh hi [the_person.mc_title]. It is going great! Work is better than ever too."
    mc.name "Oh? Your boss still *satisfied* with your work?"
    the_person "Oh yes. And me too."
    mc.name "Keeping things safe though right?"
    the_person "OH... I made him wear condoms for a while but... I mean... I'm on birth control... and he kept complaining about them."
    the_person "So one day I went in while he was on a call, and without saying a word, I opened his desk drawer, took out his condoms and threw them in the trash."
    the_person "Then I bent over his desk and umm... well I wasn't wearing any panties..."
    $ mc.change_locked_clarity(30)
    mc.name "Damn that sounds fun."
    the_person "Yeah... he finished up that call quick! But..."
    the_person "I... I didn't think it would bother you..."
    mc.name "Oh, it doesn't. Last time we talked about it you said you were making him wrap it up, so I was just wondering if you still did."
    #TODO figure out what to do here if she is already pregnant?
    if the_person.on_birth_control:
        the_person "Oh! Well no, we aren't. I'm still on birth control though, so it is still safe!"
    else:
        the_person "I decided to go back on birth control though. I don't want his baby!"
        $ manage_bc(the_person, start = True)
    $ the_person.event_triggers_dict["mandate_bc"] = True
    $ mc.change_locked_clarity(30)
    mc.name "What a lucky guy. Alright, I have some things to catch up on in my room."
    the_person "Of course honey. Dinner will be ready in a while."
    $ clear_scene()
    "You step out of the kitchen. Sounds like [the_person.possessive_title]'s boss is getting EXACTLY what he asked you for."
    "You should check up with him soon."
    $ the_person.progress.lust_step = 11
    $ the_person.event_triggers_dict["mom_office_slutty_level"] = 4
    $ add_mom_boss_bareback_teamup_action()
    return

label mom_boss_bareback_teamup_label():
    $ mom.progress.lust_step = 10
    $ mom_boss_quick_name = "Mr. " + iris.last_name
    $ the_person = get_mom_secretary()
    $ the_person.draw_person(position = "sitting")
    $ first_meeting = not (mom.event_triggers_dict.get("boss_teamup", False) or mom.event_triggers_dict.get("boss_rival", False))
    "You step up to the counter where the secretary is sitting."
    mc.name "Hello. I was hoping to talk to [mom_boss_quick_name]."

    "She looks up at and quickly recognizes you."
    the_person "Ah! Mr. [mc.last_name]. I was told when you stopped by to send you up immediately."
    the_person "Give me one second."
    "She picks up the phone and dials a number."
    the_person "Ah yes, sir? Mr. [mc.last_name] is here to see you. Yes you did say that. Yes I'll send him right in."
    "She hangs up her phone."
    the_person "He will see you now. Do you remember the way?"
    mc.name "Yes I do. Thank you."
    $ clear_scene()
    "You step onto the lift, riding it up to the sixth floor."
    $ renpy.show("luxury office", what = bg_manager.background("Luxury_Office_Background"), layer = "master")
    "As you walk into the office, a familiar voice calls out to you."
    mom_boss_quick_name "Ahh, there he is, Mr. [mc.last_name]."
    mc.name "Good day [mom_boss_quick_name]. I was wondering if we could follow up with our last meeting."
    mom_boss_quick_name "Yes, I've been looking forward to it, actually."
    mom_boss_quick_name "I assume you are aware that your recent efforts have been very... successful."
    mc.name "Of course."
    mom_boss_quick_name "I'm ready to work out a deal. I'm willing to pay top dollar to get my hands on these serums of yours."
    mc.name "Glad to hear it, but surely you realize I can already get top dollar for them elsewhere."
    "He looks at you, somewhat surprised by your response."
    mom_boss_quick_name "Yes, I suppose with the nature of them, that you could."
    mom_boss_quick_name "What, then, are looking for in a business deal?"
    mc.name "You have quite a bit of influence over the city with your position on the Council."
    mc.name "There is some legislation that I would like to have considered."
    mc.name "Nothing crazy, mind you, just things that I think would be good for the city itself."
    mom_boss_quick_name "Ahh, I see. You understand I'm just one of five, right?"
    mom_boss_quick_name "I can propose things, and vote for things, but I don't run the council. And the head still has veto authority."
    mc.name "Of course, but with your support, I think we could begin to make changes to the city that would be a benefit everyone."
    "His brow wrinkles as [mom_boss_quick_name] considers it. Then he gives you a smile."
    mom_boss_quick_name "You have a deal. You have my support on the council, and in exchange, fulfill my serum contracts."
    mom_boss_quick_name "Have your people send me over some kind of catalogue. I have a new batch of interns starting next week that would be excellent recipients..."
    mc.name "I'll have it done. Pleasure doing business with you."
    mom_boss_quick_name "Likewise, Mr. [mc.last_name]."
    "You turn and leave the office."
    "You have secured a long term, recurring contract with Vandalay Financial. In exchange, you now have influence over a vote in the city council."
    "You should try and fulfill as many contracts as you can for him as well. There may be additional benefits of doing so."
    "You step out of the building and into the street. Next Monday when your contracts refresh, look for one from Vandalay Financial."
    $ the_person = mom
    $ the_person.progress.lust_step = 12
    $ mc.business.event_triggers_dict["vandalay_contracts"] = True
    if mc.business.event_triggers_dict.get("council_influence", None):
        $ mc.business.event_triggers_dict.get("council_influence", None).append([("Vandalay", "teamup")])
    else:
        $ mc.business.event_triggers_dict["council_influence"] = [("Vandalay", "teamup")]
    $ add_mom_lust_boss_anal_intro_action()
    $ mc.change_location(downtown)
    return

# rival path
label mom_lust_boss_anal_intro_label(the_person):
    #FUTURECONTENT
    "In this event, we notice that [the_person.title] is walking around the house a little funny."
    "When we ask her about it, we discover that she has started allowing her boss to have anal sex with her."
    $ the_person.progress.lust_step = 13
    if mom.event_triggers_dict.get("boss_teamup", False):
        "Because we are teaming up with the boss, she smiles and indicates how much she enjoys her time with him."
        $ add_mom_lust_boss_tied_up_action()
        $ the_person.event_triggers_dict["mom_office_slutty_level"] = 5
    else:
        "Because we are moving against her boss, she indicates he is maybe taking things too far and that she doesn't enjoy it."
        $ add_mom_lust_boss_anal_followup_action()



    return

label mom_lust_boss_anal_followup_label(the_person):
    #FUTURECONTENT
    $ the_person.progress.lust_step = 14
    "In this event, we confront [mom.title]'s boss with blackmail material to get him to back off."
    "Tell him for his continued cooperation, he will support MC in future council votes etc."
    "We convince him to advance a new piece of legislation."
    "However, Starbuck hasn't written any of it yet. So this is where this story ends for now."
    return

#90
label mom_lust_boss_tied_up_label(the_person):
    $ the_person.progress.lust_step = 15
    "In this event, you pay a visit to [mom.possessive_title]'s."
    "When you get there, she is all tied up in his office."
    $ the_person.event_triggers_dict["mom_office_slutty_level"] = 6
    return




#The next set of labels allow us to pick up where she left off if we hire her.




label mom_new_employee_first_day_label():
    $ the_person = mom
    $ mom_first_day_duty = None
    #First, determine how far she was willing to go at her previous job#
    if the_person.progress.lust_step >= 3:  #She was willing to be flirty
        $ mom_first_day_duty = "Flirt"
    if the_person.progress.lust_step >= 6:
        $ mom_first_day_duty = "Blowjob"
    if the_person.progress.lust_step >= 8:
        $ mom_first_day_duty = "Blowjob"

    "You wake up. Today is [the_person.possessive_title]'s first day of working for you. This is your chance to set the tone for what lies ahead."
    $ mc.change_location(kitchen)
    "You quickly get ready then head to the kitchen. There is a note on the counter."
    the_person "Left early to get coffee before work. See you there!"
    "Ah, she wants to be properly caffeinated. You eat a quick breakfast."
    $ lily.draw_person()
    "As you eat, [lily.possessive_title] walks into the kitchen."
    lily "Morning bro. Where's [the_person.fname]?"
    mc.name "She left a little early. Today is her first day working for me."
    if lily.is_employee:
        lily "Oh wow, mom is working for you now too? That's great!"
        mc.name "Yeah, I'm looking forward to being able to spend more time with both of you while at work now!"
        $ lily.change_happiness(2)
    else:
        lily "Wow, YOU hired her? I didn't realise your business was doing so good."
        $ lily.change_obedience(2)
        mc.name "Yeah. Maybe once mom settles in, you could come work for me too!"
        "She just laughs."
        lily "Yeah right. Just drop out and work for you? [the_person.fname] would never let that happen."
        mc.name "Well, you never know."

    "You finish with breakfast, so you say goodbye the [lily.title] and leave."
    $ clear_scene()
    $ mc.change_location(lobby)
    $ the_person.change_location(ceo_office)
    "You get to work. You are just getting into the lobby, when [the_person.title] steps in the front door."
    $ the_person.wear_uniform()
    $ the_person.draw_person()
    "She is carrying a cup of coffee and greets you warmly."
    the_person "Ah! Good morning [the_person.mc_title]!"
    mc.name "Good morning."
    #TODO add the opportunity here to have her change her title for you to something work related. Boss, etc
    the_person "I'm ready to get started. What is first, [the_person.mc_title]?"
    mc.name "Before we get started, let me just say one thing."
    call add_role_family_employee_and_set_titles(the_person) from _call_add_role_family_employee_and_set_titles_mom_new_employee_first_day
    mc.name "Alright. Let me show you around now."
    $ mc.change_location(p_division)
    "You spend a while showing [the_person.possessive_title] around to your business."
    "She has several questions related to your business and what you manufacture, but you don't share the details of what EXACTLY the drugs you are making do."
    $ mc.change_location(office)
    "You show her to the general offices and where she will be working."
    mc.name "Alright, let me show you one more place."
    $ mc.change_location(ceo_office)
    "You lead her to your office. After she steps inside, you close the door."
    mc.name "And this is my office. Go ahead and have a seat."
    the_person "Wow... this is really nice!"
    $ the_person.draw_person(position = "sitting")
    "You sit down at your desk across from her."
    mc.name "So, what do you think?"
    the_person "Wow... well... I think that second mortgage has really paid off!"
    the_person "It is pretty impressive what you have built. I'm so proud of you honey!"

    if the_person.event_triggers_dict.get("personal_sec", False):
        #If we made her our personal secretary, change her job before we assign her duties
        $ mc.business.hire_personal_secretary(the_person)

    call initial_set_duties_label(the_person) from _call_initial_set_duties_mom_new_employee_first_day

    the_person "Shall I head back to my work space then?"
    "You think for a moment. Now is the chance for you to set the tone of the conditions of her employment."
    call perk_time_of_need_story_label() from _time_of_need_jen_11
    $ outcome_condition = None
    if the_person.event_triggers_dict.get("personal_sec", False):
        #If we made her our personal secretary, she submits at least as deep as her previous lust progress
        menu:
            "Emphasize her role":
                $ outcome_condition = "role"

            "Demand Tit Fuck" if mom.progress.lust_step >= 3:
                $ outcome_condition = "sexy"
                mc.name "I know this might be weird at first, but I want to make sure that before you start, that you understand your duties."
                mc.name "One of the reasons you got picked to be your old boss' personal secretary in the first place was because of your attitude."
                mc.name "Remember how you told me that one time he was having a rough day, and so you flashed him your tits?"
                the_person "[the_person.mc_title]! I'm your mother..."
                mc.name "At home, sure. But here, you are my personal secretary."
                mc.name "I'm not saying you have to go overboard, but I need you to be willing to be a fun little diversion for me from time to time."
                if the_person.event_triggers_dict.get("kissing_revisit_complete", False) == True:  #We've already broken foreplay taboos
                    "She seems to consider what you are saying for a moment, then responds."
                    the_person "Is that all? You need your mommy to help relieve your tension once in a while? At work?"
                    mc.name "That's right."
                    $ the_person.change_obedience(3)
                    the_person "Okay [the_person.mc_title], I think I understand."
                else:
                    "She mumbles something for a moment before responding."
                    the_person "[the_person.mc_title], my boss wasn't... he wasn't my own son!"
                    the_person "I mean, what if someone noticed us?"
                    mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are my personal secretary."
                    mc.name "It'll just be our little secret."
                    $ the_person.change_obedience(3)
                    the_person "Okay... this could be good. No one will know I'm... your mother."
                    $ the_person.event_triggers_dict["kissing_revisit_complete"] = True    #Breaks her taboo for good.
                    $ the_person.break_taboo("touching_body")
                    $ the_person.break_taboo("bare_tits")

            "Demand blowjob" if mom.progress.lust_step >= 6 and the_person.event_triggers_dict.get("kissing_revisit_complete", False):
                $ outcome_condition = "blowjob"
                mc.name "No, there is one more thing I need you to accomplish first."
                the_person "Oh?"
                mc.name "You know the main reason I hired you to be here. To be my personal secretary, the same way you were for your last boss."
                the_person "Ah, I'm not sure what you mean?"
                mc.name "When he was stressed out, you used to give him some special treatment. To help him relax."
                the_person "Oh... Oh!"
                if the_person.event_triggers_dict.get("oral_revisit_complete", False) == True:  #We've already broken her oral taboo
                    the_person "Is that all? You need your mommy to help relieve your tension once in a while? At work?"
                    mc.name "That's right."
                    the_person "And... right now?"
                    mc.name "Yes. Now."
                    $ the_person.change_obedience(3)
                    the_person "Oh my. Okay [the_person.mc_title]!"
                    "You pull out your cock as she gets up and walks around your desk, getting on her knees."
                else:
                    the_person "[the_person.mc_title], my boss wasn't... he wasn't my own son!"
                    the_person "The things I did for him..."
                    mc.name "What? You are willing to do them for him, but not for me?"
                    the_person "Honey, I... what if someone found out?"
                    mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are my personal secretary."
                    "You stand up. She stares wide-eyed as you pull your already erect cock from your pants, exposing yourself to [the_person.possessive_title]."
                    mc.name "Besides, I'm sure this is way better than whatever your old boss was packing."
                    "She gasps."
                    the_person "Oh my... It looks so..."
                    mc.name "Big?"
                    the_person "I was going to say, virile!... But yes, it looks so hard!"
                    "She trembles a moment, but eventually looks up and meets your eyes."
                    the_person "You need your mommy to help relieve your tension once in a while? At work?"
                    mc.name "Yes. And right Now."
                    $ the_person.change_obedience(3)
                    the_person "Okay... this could be good. No one will know I'm... your mother."
                    "You sit back down."
                    $ the_person.event_triggers_dict["oral_revisit_complete"] = True    #Breaks her oral taboo for good.
                    $ the_person.break_taboo("sucking_cock")
                    "She gets up and walks around your desk, getting on her knees."

            "Demand sex" if mom.progress.lust_step >= 8 and the_person.event_triggers_dict.get("oral_revisit_complete", False) == True:    #Jennifer will subvert this choice to anal if we haven't progressed enough for vaginal
                mc.name "No, there is one more matter we need to settle first."
                the_person "Oh?"
                mc.name "You know the main reason I hired you to be here. To be my personal secretary, the same way you were for your last boss."
                the_person "Ah, I'm not sure what you mean?"
                mc.name "When he was stressed out, you used to give him some special treatment. To help him relax."
                the_person "Oh... Oh!"
                mc.name "I expect the same cooperation, for you to make your body available for my use while at work."
                if the_person.event_triggers_dict.get("vaginal_revisit_complete", False) == True:   #Happy mommy
                    $ outcome_condition = "vaginal"
                    "She looks at you and smiles."
                    the_person "Is that why you hired me? You can't get enough of mommy at home, you have to bring me to work too?"
                    mc.name "That's correct."
                    the_person "I see... and right now?"
                    mc.name "Yes. Now. Bend over my desk."
                    $ the_person.change_obedience(5)
                    the_person "Oh my. Okay [the_person.mc_title]!"
                    "You pull out your cock as she obediently bends over the side of your desk."

                elif the_person.event_triggers_dict.get("anal_revisit_complete", False) == True:    #Only anal
                    $ outcome_condition = "anal"
                    "She smile at you, but hesitates for a moment."
                    the_person "[the_person.mc_title], I understand what you are saying but... you're my son!"
                    mc.name "Yeah, and?"
                    the_person "Our agreement is still in place right?"
                    the_person "You can still have my ass, but we can't take it further..."
                    mc.name "Yes, of course."
                    "She looks visibly relieved."
                    the_person "Oh! Good... so... right now?"
                    mc.name "Yes. Now. Bend over my desk."
                    $ the_person.change_obedience(5)
                    the_person "Oh my. Okay [the_person.mc_title]!"
                    "You pull out your cock as she obediently bends over the side of your desk."
                else:   #She puts up a bit of a fight, then gives in to anal only.
                    $ outcome_condition = "anal"
                    "[the_person.title] looks shocked for a moment."
                    the_person "You mean like... with my mouth?"
                    mc.name "That is one part of your body, yes, but you have other holes too."
                    the_person "[the_person.mc_title]! My boss wasn't... he wasn't my own son!"
                    the_person "The things I did for him..."
                    mc.name "What? You are willing to do them for him, but not for me?"
                    the_person "Honey, I... what if someone found out?"
                    mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are my personal secretary."
                    "You stand up. She stares wide-eyed as you pull your already erect cock from your pants, exposing yourself to [the_person.possessive_title]."
                    mc.name "Besides, I'm sure this will feel way better sliding into you than whatever your old boss was packing."
                    "She gasps."
                    the_person "Oh my... It looks so..."
                    mc.name "Big?"
                    the_person "I was going to say, virile!... But yes, it looks so hard!"
                    "She trembles a moment, but eventually looks up and meets your eyes."
                    "For a moment, you see her resistance star to crumble, but she suddenly gets an idea."
                    the_person "Honey what if... what if you just used my... oh god I can't believe I'm about to say this..."
                    the_person "What if you just used my ass? It would be a lot less risky..."
                    "You can't help but smile. Your own mother just suggested you fuck her ass! You decide to go along with it for now..."
                    mc.name "That would be acceptable."
                    "You start to walk around your desk. She begins to tremble."
                    the_person "You... right now?"
                    mc.name "Yes. Right Now. Bend over my desk."
                    $ the_person.change_obedience(3)
                    the_person "Okay... this could be good. No one will know I'm... your mother."
                    $ the_person.event_triggers_dict["anal_revisit_complete"] = True    #Breaks her anal taboo for good?
                    $ the_person.break_taboo("anal_sex")
                    "She gets up and bends over your desk, obediently."


    else:
        #If she isn't our personal secretary, initial progress is based only on her current taboo progress.
        menu:
            "Emphasize her role":
                $ outcome_condition = "role"

            "Emphasize her sexy attitude" if the_person.event_triggers_dict.get("kissing_revisit_complete", False) == True:
                $ outcome_condition = "sexy"
                mc.name "I know this might be weird at first, but I want to make sure that before you start, that you understand your duties."
                mc.name "I know we've already settled this, but I need someone to keep things fun around here."
                mc.name "Work is stressful for me, and once in a while I might need you to help me relieve some tension."
                the_person "What like... massage your back?"
                mc.name "Like that, sure. Or maybe even if I massage you."
                the_person "I'm not sure how that would help."
                mc.name "You'd be surprised how stress relieving playing with a set of tits for a while can be."
                the_person "Oh! Oh my... [the_person.mc_title]..."
                mc.name "Hey, we do it at home, why not here?"
                the_person "Well, what if someone noticed us?"
                mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are just another employee."
                mc.name "They like to gossip. They'll just think you're kinda slutty, nothing more."
                "She mumbles something for a moment."
                mc.name "It'll just be our little secret."
                $ the_person.change_obedience(3)
                the_person "Okay... this could be good. No one will know I'm... your mother."

            "Demand blowjob" if the_person.event_triggers_dict.get("oral_revisit_complete", False) == True:
                $ outcome_condition = "blowjob"
                mc.name "No, there is one more thing I need you to accomplish first."
                the_person "Oh?"
                mc.name "I know this might be weird at first, but I want to make sure that before you start, that you understand your duties."
                mc.name "I know we've already settled this, but I need someone to keep things fun around here."
                mc.name "Work is stressful for me, and once in a while I might need you to help me relieve some tension."
                the_person "Tension? Like what kind of tension?"
                mc.name "Once in a while, I may need to use your mouth."
                the_person "[the_person.mc_title]... just because we do that at home sometimes... what if someone noticed us?"
                mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are just another employee."
                mc.name "They like to gossip. They'll just think you're slutty, nothing more."
                "She mumbles something for a moment."
                mc.name "It'll just be our little secret."
                $ the_person.change_obedience(3)
                the_person "Okay... this could be good. No one will know I'm... your mother."
                the_person "And... right now?"
                mc.name "Yes. Now."
                $ the_person.change_obedience(3)
                the_person "Oh my. Okay [the_person.mc_title]!"
                "You pull out your cock as she gets up and walks around your desk, getting on her knees."

            "Demand Anal" if the_person.event_triggers_dict.get("anal_revisit_complete", False) == True:
                $ outcome_condition = "anal"
                mc.name "No, there is one more thing I need you to accomplish first."
                the_person "Oh?"
                mc.name "I know this might be weird at first, but I want to make sure that before you start, that you understand your duties."
                mc.name "We've already settled this, but I need someone to keep things fun around here."
                mc.name "Work is stressful for me, and once in a while I might need you to help me relieve some tension."
                the_person "Tension? You mean like, sexual tension?"
                mc.name "That's right. Once in a while I may need you to present your ass for my use."
                the_person "[the_person.mc_title]... I know we agreed to do that once in a while at home, but what if someone notices us?"
                mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are just another employee."
                mc.name "They like to gossip. They'll just think you're a nasty slut, nothing more."
                "She mumbles something for a moment."
                mc.name "It'll just be our little secret."
                $ the_person.change_obedience(3)
                the_person "Okay... this could be good. No one will know I'm... your mother."
                the_person "Did you want to do it right now? In your office?"
                mc.name "Yes. Now."
                $ the_person.change_obedience(5)
                the_person "Oh my. Okay [the_person.mc_title]!"
                "You stand up and walk around to the front side of your desk."
                mc.name "Bend over, I want to be able to start my day with a clear mind."

            "Demand Sex" if the_person.event_triggers_dict.get("vaginal_revisit_complete", False) == True:
                $ outcome_condition = "vaginal"
                mc.name "No, there is one more thing I need you to accomplish first."
                the_person "Oh?"
                mc.name "I know this might be weird at first, but I want to make sure that before you start, that you understand your duties."
                mc.name "We've already settled this, but I need someone to keep things fun around here."
                mc.name "Work is stressful for me, and once in a while I might need you to help me relieve some tension."
                the_person "Tension? You mean like, sexual tension?"
                mc.name "That's right. Once in a while I may need you to use any or all of your holes for my use."
                the_person "[the_person.mc_title], at home and in private is one thing, but here? What if someone found out?"
                mc.name "Someone here? That doesn't matter. No one here needs to know we are related. My employees will assume exactly what we tell them. That you are just another employee."
                mc.name "They like to gossip. They'll just think you're my naughty slut, nothing more."
                "She mumbles something for a moment."
                mc.name "It'll just be our little secret."
                $ the_person.change_obedience(3)
                the_person "Okay... this could be good. No one will know I'm... your mother."
                the_person "Did you want to do it right now? In your office?"
                mc.name "Yes. Now."
                $ the_person.change_obedience(5)
                the_person "Oh my. Okay [the_person.mc_title]!"
                "You stand up and walk around to the front side of your desk."
                mc.name "Bend over, I want to be able to start my day with a clear mind."

    if outcome_condition == "role":
        mc.name "I appreciate you being willing to do this, [the_person.title]."
        mc.name "It can be hard to find help that I can trust, and having you here is going to really help my operation."
        $ the_person.change_love(3)
        the_person "Of course. It means a lot to me to hear you say that."
    elif outcome_condition == "sexy":
        $ mc.change_arousal(10)
        mc.name "In fact, I think it might be a good idea to start now, at the beginning of the day."
        mc.name "Come here."
        "[the_person.possessive_title!c] quietly stands up and walks around to your chair."
        $ the_person.draw_person(position = "default")
        if not the_person.tits_visible:
            mc.name "Can I see them?"
            "You motion to her chest. She mutters under her breath for a moment. But then nods."
            $ the_person.strip_to_tits()
            "You help her take her top off, and her amazing tits spill free from their prior confines."
        "You notice a red tinge on her cheeks... her nipples are hard, ready to be sucked and pinched."
        "You lean forward, grabbing one of her tits with your hand and running your tongue along the nipple of the other."
        $ the_person.change_arousal(10)
        $ mc.change_arousal(15)
        "Having [the_person.possessive_title] in your office, ready to pleasure you at your whim is really turning you on."
        "You reach down and pull out your cock."
        mc.name "Alright, show me what you can do."
        the_person "Yes [the_person.mc_title]."
        $ the_person.draw_person(position = "blowjob")
        "She drops to her knees, and soon has your cock pressed into her cleavage."
        "You let out an appreciative moan as she starts to bounce them up and down. This is going to be the start of a fun and productive employee relationship."
        call fuck_person(the_person, private = True, start_position =tit_fuck, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_titfuck_work_jen_01
        $ the_report = _return
        $ the_person.draw_person(position = "blowjob")
        if the_report.get("guy orgasms", 0) > 0:
            "You spend a few moments recovering from your orgasm, then you look down at [the_person.possessive_title]."
            the_person "I would ask if I did okay... but I'm pretty sure the evidence speaks for itself."
            mc.name "Damn [the_person.title], it sure does."
        $ the_person.draw_person()
        the_person "I think I'm going to go get cleaned up, and then get to work?"
        mc.name "Sounds great. Enjoy your first day, I know I am!"
        $ the_person.draw_person(position = "walking_away")
    elif outcome_condition == "blowjob":
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_arousal(20)
        "The sight of [the_person.possessive_title] on her knees, ready to service you orally at your desk really turns you on."
        "You run your hand through her hair before she begins."
        call fuck_person(the_person, private = True, start_position =blowjob, start_object = make_floor(), skip_intro = False, position_locked = True) from _call_blowjob_work_jen_01
        $ the_report = _return
        $ the_person.draw_person(position = "blowjob")
        if the_report.get("guy orgasms", 0) > 0:
            "You spend a few moments recovering from your orgasm, then you look down at [the_person.possessive_title]."
            the_person "I would ask if I did okay... but I'm pretty sure the evidence speaks for itself."
            mc.name "Damn [the_person.title], it sure does."
        $ the_person.draw_person()
        the_person "I think I'm going to go get cleaned up, and then get to work?"
        mc.name "Sounds great. Enjoy your first day, I know I am!"
    elif outcome_condition == "anal":

        $ the_person.draw_person(position = "standing_doggy")
        if not the_person.vagina_available:
            "You roughly pull at her clothing."
            $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = True)
            "Once exposed, you give [the_person.possessive_title]'s ass a playful spank."
        else:
            "You give [the_person.possessive_title]'s ass a playful spank."
        "You quickly pull out your cock, then rub it along her ass. You gather a mouthful of saliva, then let it drop from your mouth to her ass."
        "You rub your cock through it and along her ass, then repeat the process a few more time."
        $ mc.change_arousal(15)
        mc.name "Damn it is going to be nice having you here at the office. I might need to buy a bottle of lube to keep in my desk though."
        mc.name "Actually, can you do that for me? Make sure I have a good stock of lube in my desk as part of your duties."
        $ the_person.change_obedience(3)
        the_person "Of course. It seems that might be in my best interest, anyway."
        "You are finally satisfied that you are ready for penetration after applying several rounds of saliva to [the_person.title]'s tight backdoor."
        "You hold your cock with one hand and [the_person.possessive_title]'s hip with the other, then push firmly."
        "Your erection pushes through after brief resistance, sinking deep into her tight forbidden hole."
        $ the_person.change_arousal(15)
        $ mc.change_arousal(20)
        the_person "OH! Fffff..."
        "Her voice dies out as you bottom out inside her bowel, filling her with an exquisite mixture of pleasure and pressure."
        call fuck_person(the_person, private = True, start_position =anal_standing, start_object = make_desk(), skip_intro = True, position_locked = True, skip_condom = True) from _call_anal_work_jen_01
        $ the_report = _return
        $ the_person.draw_person(position = "standing_doggy")
        if the_report.get("guy orgasms", 0) > 0 and the_report.get("girl orgasms", 0) > 1:
            "[the_person.possessive_title!c] remains bent over your desk, her body recovering from her orgasm."
            mc.name "Damn [the_person.title]. Maybe I should start every work day like this. Your ass is amazing."
            "She mumbles something incoherent, spending several more seconds slumped over."
        else:
            "It takes [the_person.possessive_title] a few moments to compose herself, before she stands up."
        $ the_person.draw_person()
        the_person "I think I'm going to go get cleaned up, and then get to work?"
        mc.name "Sounds great. Enjoy your first day, I know I am!"
    elif outcome_condition == "vaginal":
        $ the_person.draw_person(position = "standing_doggy")
        if not the_person.vagina_available:
            "You roughly pull at her clothing."
            $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = True)
            "Once exposed, you give [the_person.possessive_title]'s ass a playful spank."
        else:
            "You give [the_person.possessive_title]'s ass a playful spank."
        "You quickly pull out your cock, then rub it along her slit. She gasps when she feels your cock."
        $ the_person.change_arousal(15)
        the_person "Oh god... that's it baby..."
        "You give her ass a couple more playful spanks as your lubricate the tip of your cock with her arousal, sliding it up and down her slit a few more time."
        $ mc.change_arousal(15)
        mc.name "Damn it is going to be nice having you here at the office."
        if requires_condom(the_person):
            the_person "Do you have a condom? We don't want any accidents."
            "You consider pushing inside her anyway, but decide now isn't the time to test that limit."
            "You quickly grab a condom and put it on."
            $ mc.condom = True
            mc.name "I don't have very many left, I'll have to restock."
            mc.name "Actually, can you do that for me? Make sure I have a good stock of condoms in my desk as part of your duties."
            $ the_person.change_obedience(3)
            the_person "Of course. It seems that might be in my best interest, anyway."
        elif the_person.has_breeding_fetish:
            the_person "Mmm... it's so hard. Do you have a good load saved up for me? I can't wait to feel it splash inside me..."
        "You hold your cock with one hand and [the_person.possessive_title]'s hip with the other, then push forward."
        "Your erection pushes inside easily. She moans when you bottom out."
        $ the_person.change_arousal(15)
        $ mc.change_arousal(20)
        the_person "OH! Fffff..."
        "Her voice dies when your hips hit hers, filling her with pleasure."
        call fuck_person(the_person, private = True, start_position =standing_doggy, start_object = make_floor(), skip_intro = True, position_locked = True, skip_condom = True) from _call_vaginal_sex_work_jen_01
        $ the_report = _return
        $ the_person.draw_person(position = "standing_doggy")
        if the_report.get("guy orgasms", 0) > 0 and the_report.get("girl orgasms", 0) > 1:
            "[the_person.possessive_title!c] remains bent over your desk, her body recovering from her orgasm."
            mc.name "Damn [the_person.title]. Maybe I should start every work day like this. Your ass is amazing."
            "She mumbles something incoherent, spending several more seconds slumped over."
        else:
            "It takes [the_person.possessive_title] a few moments to compose herself, before she stands up."
        $ the_person.draw_person()
        the_person "I think I'm going to go get cleaned up, and then get to work?"
        mc.name "Sounds great. Enjoy your first day, I know I am!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and starts to walk out of your office. You watch her as she leaves."
    "She is now your employee, and subject to all the policies and work rules implied."

    call advance_time() from _call_advance_time_after_jen_hire_01
    return
