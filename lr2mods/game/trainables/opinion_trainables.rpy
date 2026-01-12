label train_learn_opinion_label(the_person):
    mc.name "Let's talk about you, what do you have strong feelings about?"
    the_person "Me? Oh, I don't know..."
    menu:
        "Tell me a normal opinion" if the_person.has_unknown_normal_opinions:
            mc.name "Really, tell me anything at all."
            $ sexy_opinion = False

        "Tell me a sexy opinion" if the_person.has_unknown_sexy_opinions:
            mc.name "Really, I promise I won't tell anyone else. You must have something interesting to share."
            $ sexy_opinion = True

    "You keep prompting [the_person.possessive_title] to share more information."

    if sexy_opinion:
        $ revealed_opinion = the_person.get_random_opinion(include_known = False, include_normal = False, include_sexy = True)
    else:
        $ revealed_opinion = the_person.get_random_opinion(include_known = False)

    if revealed_opinion:
        $ the_person.discover_opinion(revealed_opinion)
        "She can't resist for long. You listen as she tells you her opinion about [revealed_opinion]."
        if sexy_opinion:
            the_person "I hope that wasn't too personal to share..."
            mc.name "No, that's exactly what I wanted to know about. Thank you [the_person.title]."
        else:
            the_person "I hope that's what you wanted to hear about..."
            mc.name "It was perfect, thank you [the_person.title]."
        return True

    "[the_person.title] seems happy to share her opinions with you after some prompting."
    "Unfortunately, she doesn't have anything to tell you that you don't already know."
    return False

init 0 python:
    def build_opinion_change_menu(person, positive = True):
        opinion_list = person.get_opinion_topics_list(include_unknown = False)
        show_list = [[], []]
        list_name = ["Negative Opinion", "Positive Opinion"]
        for topic in opinion_list:
            score = person.opinion(topic)
            name = opinion_score_to_string(score) + " " + topic
            if positive and score in (-1, 1):
                show_list[0 + (0 if score < 0 else 1)].append((name.title(), topic))
            elif not positive:
                if score != -2 or topic not in special_trainable_opinions: # exclude hated with special trainable opinions
                    show_list[0 + (0 if score < 0 else 1)].append((name.title(), topic))

        menu_list = []
        for i in (0, 1):
            if show_list[i]:
                target_list = sorted(show_list[i], key = lambda x: x[1])
                target_list.insert(0, list_name[i])
                menu_list.append(target_list)

        menu_list.append(["Other", ("Never Mind", "Never Mind")])
        return menu_list

label train_strengthen_opinion_label(the_person): #TODO: Only have this enabled if she has a known moderate opinion
    mc.name "I want to talk to you about something."
    the_person "Okay, what do you want to talk about?"

    call screen main_choice_display(build_menu_items(build_opinion_change_menu(the_person, True)))

    $ player_choice = _return
    if not player_choice == "Never Mind":
        if player_choice in opinion_training_dialogue_dict and the_person.get_opinion_score(player_choice) >= 0:
            $ dialogue_list = opinion_training_get_dialogue(player_choice)
            mc.name "I think you have the right idea, but you could take it even further..."
            "[the_person.possessive_title!c] listens attentively as you talk to her."
            mc.name "[dialogue_list[0]]..."
            the_person "Hmmm... I'm not sure..."
            mc.name "...[dialogue_list[1]]..."
            the_person "That... does make sense..."
            mc.name "...[dialogue_list[2]]"
            the_person "Yeah... Yeah you're right..."
            $ the_person.strengthen_opinion(player_choice)
            "After a while you feel confident you have strengthened her opinion."
            return True
        else:
            mc.name "I think you have the right idea, but you could take it even further..."
            "[the_person.possessive_title!c] listens attentively as you talk to her."
            $ the_person.strengthen_opinion(player_choice)
            "After a while you feel confident you have strengthened her opinion."
            return True

    mc.name "On second thought, never mind."
    "She shrugs, completely unbothered."
    return False


label train_weaken_opinion_label(the_person): #TODO; Only have this enabled if you know of an opinion
    mc.name "I want to talk to you about something."
    the_person "Okay, what do you want to talk about?"

    call screen main_choice_display(build_menu_items(build_opinion_change_menu(the_person, False)))

    $ player_choice = _return
    if not player_choice == "Never Mind":
        if player_choice in opinion_training_dialogue_dict and the_person.get_opinion_score(player_choice) <= 0:
            $ dialogue_list = opinion_training_get_dialogue(player_choice)
            mc.name "You've got it all wrong, you need to think about this some more."
            mc.name "Here, let me explain it to you..."
            mc.name "[dialogue_list[0]]..."
            the_person "No! I... I would never..."
            mc.name "...[dialogue_list[1]]..."
            the_person "I... I don't know... I guess that makes sense..."
            mc.name "...[dialogue_list[2]]"
            the_person "Yeah... I never though about it that way..."
            $ the_person.weaken_opinion(player_choice)
            "After a while you feel confident you have weakened her opinion."
            return True
        else:
            mc.name "You've got it all wrong, you need to think about this some more."
            mc.name "Here, let me explain it to you..."
            "[the_person.possessive_title!c] listens attentively while you mould her opinions of [player_choice]."
            $ the_person.weaken_opinion(player_choice)
            "When you're finished you feel confident that you have weakened her opinion."
            return True
    if not player_choice == "Never Mind":
        mc.name "You've got it all wrong, you need to think about this some more."
        mc.name "Here, let me explain it to you..."
        "[the_person.possessive_title!c] listens attentively while you mould her opinions of [player_choice]."
        $ the_person.weaken_opinion(player_choice)
        "When you're finished you feel confident that you have weakened her opinion."
        return True

    mc.name "On second thought, never mind."
    "She shrugs, completely unbothered."
    return False


init 0 python:
    def build_opinion_training_list(person, sexy_list):
        if sexy_list:
            opinion_train_options = person.get_sexy_opinions_list()
        else:
            opinion_train_options = person.get_normal_opinions_list()

        for known_opinion in person.get_opinion_topics_list(include_unknown = False):
            if known_opinion in opinion_train_options:
                opinion_train_options.remove(known_opinion) #Remove opinions we already know about.
        return sorted(opinion_train_options, key = lambda x: x)

    def build_opinion_training_menu(person, sexy_list):
        option_list = []
        for train_option in build_opinion_training_list(person, sexy_list):
            option_list.append((train_option.title(), train_option))

        if sexy_list:
            option_list.insert(0, "Sexy Opinions")
        else:
            option_list.insert(0, "Opinions")
        option_list.append(("Never Mind", "Never Mind"))
        return [option_list]

label train_new_opinion_label(the_person, sexy_list = False):
    mc.name "I want to talk to you about something."
    the_person "Okay, what do you want to talk about?"

    call screen main_choice_display(build_menu_items(build_opinion_training_menu(the_person, sexy_list)))

    $ player_choice = _return
    if not player_choice == "Never Mind":
        mc.name "Let's talk about [player_choice]."
        if the_person.opinion(player_choice) == 0:
            "[the_person.possessive_title!c] nods and listens attentively as you explain to her what her opinion should be."
            menu:
                "Create a positive opinion of [player_choice]":
                    $ the_person.create_opinion(player_choice)
                    if player_choice in opinion_training_dialogue_dict:
                        $ dialogue_list = opinion_training_get_dialogue(player_choice)
                        mc.name "I want you to consider this carefully."
                        "[the_person.possessive_title!c] listens attentively as you talk to her."
                        mc.name "[dialogue_list[0]]..."
                        the_person "Hmmm... I'm not sure..."
                        mc.name "...[dialogue_list[1]]..."
                        the_person "That... does make sense..."
                        mc.name "...[dialogue_list[2]]"
                        the_person "Yeah... Yeah you're right..."

                "Create a negative opinion of [player_choice]":
                    $ the_person.create_opinion(player_choice, start_positive = False)
            "It takes some time, but after a long conversation you feel confident you've put a strong opinion in [the_person.title]'s mind."
            return True
        else:
            the_person "[player_choice!c]? Yeah, I have some thoughts about that..."
            $ the_person.discover_opinion(player_choice)
            "It quickly becomes clear that [the_person.possessive_title] already has an opinion about [player_choice]."
            "You'll need a different approach if you want to change an opinion she has already formed."
            return False

    mc.name "On second thought, never mind."
    "She shrugs, completely unbothered."
    return False

init 1 python:
    opinion_training_dialogue_dict = {}
    # Opinion traing dialogue is a dictionary that contains a list of dialogue option for every sexual opinion in the game, for MC to train girls.
    # Can be called from inside of trainables, or any other event that involves training girls for something.
    # Intention is for each opinion to have 12 lines.
    # indexes 0-3 are for general positive statements
    # indexes 4-7 are for stronger positive statements
    # indexes 8-11 are for final training statements, EG the final straw that kicks the opinion up to the next level.
    # Easiest way to run all three dialogues is to use a random index of 0-3, then add 4 for a mid statement and 8 for the finale.
    # I try to keep a similar theme throughout the three ordered statements, so dialogue in order can make sense, but it may not always be possible.
    # Statements should also be neutral. There may be scenes where other women are using these lines to help train friends/coworkers etc.
    # To get this list up and running, expect multiple copies of the same dialogue or with just slight variations until I have time to populate everything - Starbuck
    opinion_training_dialogue_dict["anal creampies"] = [
        "It is only proper for you to receive your partner's cum, regardless of which hole of yours he happens to be using. ", #0
        "Letting him fuck you in the ass is so naughty, it woudn't be fair to make him pull out when he is done.", #1
        "Sometimes, he just can't pullout. It shouldn't be an expectation that your partner denies themselves pleasure just for your sake.", #2
        "You were made to take cum. Orally, vaginally, or anally. Are they really that much different?", #3
        "You are already letting him use your asshole for his pleasure. Why not let him finish there too?", #4
        "Anal is already so naughty, wouldn't letting him cum inside when he finishes be even naughtier?", #5
        "It is only natural. Your body was made for pleasure, and he wants to experience that to the fullest, ESPECIALLY as he is cumming!", #6
        "If you are already letting him use your forbidden hole, is it really that much farther to let him finish there too?", #7
        "It'll feel amazing, when he finally dumps his load deep inside your naughty backdoor.", #8
        "You want to be naughty, don't you? You love taking a big dick deep in your ass and letting him use you and cum deep inside your forbidden little hole.", #9
        "You're already taking his raw cock in your ass, what did you think was going to happen? You might as well enjoy it when he finishes inside you.", #10
        "Isn't that what it is all about? Draining him and feeling him fill you with his cum, no matter which hole he is using.", #11
    ]
    opinion_training_dialogue_dict["anal sex"] = [
        "When a man takes you, every inch of you belongs to him. Every curve, every hole.", #0
        "What is it about anal that makes you stop and say no?", #1
        "Is it a fear of discomfort that keeps you from enjoying anal? You'll never know how amazing it is if you don't try it.", #2
        "", #3
        "So what if he wants to stick it in your ass? Your his plaything, let him do it.", #4
        "You want to be his slut, right? Why would you resist it when he wants to slide his cock in your ass?", #5
        "Maybe it is time for you to get a butt plug? Train that slutty ass of yours for him to enjoy.", #6
        "", #7
        "Deep down, you aren't afraid of taking it in the ass, are you? What you are really afraid of is that you might LOVE IT.", #8
        "A good slut doesn't say no, they make every hole available for their lover to use.", #9
        "Get those slutty little holes trained up and ready. You'll know you did the right thing everytime you feel him penetrate your little asshole.", #10
        "", #11
    ]
    opinion_training_dialogue_dict["bareback sex"] = [
        "Put your hand in a glove. Can you even feel what you are touching anymore? Is it wet? Warm? Why would you make him wear one during sex?", #0
        "What if you're ready to fuck, but suddenly realize, neither of you even has a condom? Are you going to stop? Do something else?", #1
        "", #2
        "", #3
        "Don't you want to feel the pleasure of letting him go bare? To remove any barrier between him and you.", #4
        "Do you really want to stop, get out a package, open it, put it on, ruining the mood when his thick cock is right there, ready to penetrate you bare?", #5
        "", #6
        "", #7
        "It'll feel so good, he'll pound you even harder. You won't regret letting him go bare.", #8
        "Just tell him to SLIDE IT IN. Wrap your legs around him if you have to.", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["being covered in cum"] = [
        "When you play around with a man, it is only natural that they want to mark their territory.", #0
        "It is so much work to make a man feel good, but then you get to the end and make him waste his cum in a tissue? Or on himself?", #1
        "Cum is the most incredible fluid on earth. Why would you want to waste it?", #2
        "", #3
        "When he pulls out and you see him stroking himself pointed straight at you, it is just him, marking you as his.", #4
        "Want to blow his mind? Beg him to cover you with it. Make your body a canvas for his seed.", #5
        "Every drop is a blessing. It is full of protein and anti-oxidants. And most importantly, it his *his*.", #6
        "", #7
        "Isn't it wonderful? To take your man's cum all over? His hot seed coating your body, marking you as his?", #8
        "Ass, tits, face, stomach. Wherever he decides, let that hot cum cover you. Beg for it and revel in every drop.", #9
        "Learn to crave that warm splash every time he covers you with his invaluable cum.", #10
        "", #11
    ]
    opinion_training_dialogue_dict["being fingered"] = [
        "The vagina is incredible, built to be penetrated by all manner of sizes and shapes and to derive pleasure from it.", #0
        "", #1
        "", #2
        "", #3
        "Even when you are starting slow though, a finger can still give you so much pleasure. Let him in.", #4
        "", #5
        "", #6
        "", #7
        "Whether it is his bare cock, or just a finger, listen to your body when it tells you it feels amazing to be penetrated.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["being submissive"] = [
        "A skilled partner can use the submission of his partner to make her feel incredible, as well as meet his own needs with her.", #0
        "When the kissing gets heated and his cock comes out, what makes you stop when you feel his hands on your shoulders, pushing you down?", #1
        "", #2
        "", #3
        "Getting on your knees, bending over his desk, getting pinned to the wall. All you have to do is let him.", #4
        "And when you've been naughty, why would you resist him bending you over his knee?", #5
        "", #6
        "", #7
        "Your body was just built that way. You are the one getting fucked, and being submissive and letting him do what he wants with you can only lead to increased pleasure for both of you.", #8
        "On your knees, or bent over HIS knee, let him use you and you'll find pleasure you could never get otherwise.", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["big dicks"] = [
        "It's okay to feel that initial rush of fear when he finally drops his pants and instead of a penis, he reveals a monster.", #0
        "", #1
        "", #2
        "", #3
        "Learn to let that fear go, and replace it with excitement. His horse cock isn't a threat, it's a challenge.", #4
        "", #5
        "", #6
        "", #7
        "Your body can take it. Give it time, and when you finally conquer that monster it will fill you like you've never been filled before.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["cheating on men"] = [
        "You're a slut and you know it, don't you? You crave male attention from everywhere, not just a significant other.", #0
        "", #1
        "", #2
        "", #3
        "Isn't it so exciting? To catch the eye of a new man, to get him to chase you, and want you.", #4
        "", #5
        "", #6
        "", #7
        "Is there anything more amazing than the first time you get naked with a new partner? Why limit yourself just because you are seeing someone?", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["creampies"] = [
        "When it's inside you, bare, and he is in the final stretch, are you really going to make him pull out?", #0
        "Your body is longing to be filled with cum. Why on earth would you make him pull out?", #1
        "", #2
        "", #3
        "What if he pulled out right before you finish? And he made you finish with your own hand? How disappointing would that be?", #4
        "Your body craves it, doesn't it? That empty feeling when he pulls out and cums on skin. You are longing to get filled with his seed!", #5
        "", #6
        "", #7
        "Give him the ultimate rush. Wrap those legs around him if you can and beg him to fill you with his cum. You'll never go back to pulling out.", #8
        "The ultimate rush is that flood of warmth as his seed pours out inside you. Beg him for it every time!", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["cum facials"] = [
        "Women often find the idea of a cum facial as a dirty, repulsive act, but they couldn't be more wrong.", #0
        "", #1
        "", #2
        "", #3
        "Cum isn't dirty. It is evidence. Evidence that you pleased him, and when you wear it on your face proudly, you show him how proud you are to make him feel good.", #4
        "", #5
        "", #6
        "", #7
        "When his cum splashes onto your face, it isn't HIS cum anymore, it is YOUR cum. You earned it, and it is as natural and exciting to wear it on your face as it is to swallow it or taking it vaginally.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["doggy style sex"] = [
        "There's nothing wrong with bending over when it is time to get intimate.", #0
        "Is there really such a thing as a boob man or an ass man? Men all find your curves irresistable.", #1
        "", #2
        "", #3
        "You'll drive him wild when he sees his cock sliding inside you and his hips slap against your amazing ass.", #4
        "When you get on your hands and knees and he sees your ass pointed back at him, ready for him to fuck, you're going blow his mind.", #5
        "", #6
        "", #7
        "It'll go deeper than anything you've ever felt before as you rut like wild animals.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["drinking cum"] = [
        "Biologically, men are driven to do one thing. To cum inside of you.", #0
        "", #1
        "", #2
        "", #3
        "He needs to feel you accepting his seed no matter what hole you take it in. To spit it out is to reject him.", #4
        "", #5
        "", #6
        "", #7
        "It takes time to acquire the taste, but you'll learn to love it, every time his throbbing cock explodes in your mouth and you swallow every drop of it.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["getting head"] = [
        "It is okay to feel exposed to him, to have your most private area exposed for him to taste and touch.", #0
        "", #1
        "", #2
        "", #3
        "There isn't any pressure to do anything, all you have to do is let yourself go and receive the pleasure.", #4
        "", #5
        "", #6
        "", #7
        "If he wants to kiss you, let yourself revel in it. He just wants to make you feel as good as he can.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["giving blowjobs"] = [
        "You know what makes him feel absolutely amazing? A pair of lips and a tongue wrapped around his cock.", #0
        "You rely on him for so many things, it is only fair that repay him once in a while with your mouth.", #1
        "", #2
        "", #3
        "It is about give and take. You can't be willing to receive all the pleasure without being willing to give it as well.", #4
        "What is so bad about it that you can't use your mouth? Especially compared to the pleasure it gives him.", #5
        "", #6
        "", #7
        "Don't you want to blow his mind, as well as his cock? To be in charge of his pleasure in such a unique way?", #8
        "You owe it to him, to use your mouth to the best of your abilities to pleasure him.", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["giving handjobs"] = [
        "It's just a handjob. There's no reason to overthink it. He wants your soft, feminine hand wrapped around his cock.", #0
        "", #1
        "", #2
        "", #3
        "Would it feel better in your mouth or pussy? Sure, but your hand is one of many tools you've been given to please him.", #4
        "", #5
        "", #6
        "", #7
        "Afterall, it is just a handjob. You can always go further if you want, or just tease him, or even driving him wild and make him cum with just your hand, promising even more pleasure later.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["giving tit fucks"] = [
        "Men LOVE tits. Do you know what they love even more? When they slide their cock between yours.", #0
        "", #1
        "", #2
        "", #3
        "Your tits are sensitive. Explore yourself while he slides that thick, meaty cock between them and you'll be amazed at the sensations.", #4
        "", #5
        "", #6
        "", #7
        "Every inch of your body is built to please him. ESPECIALLY your tits!", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["incest"] = [
        "When we become adults, we are capable of self reasoning and decision making. The social taboos of incest are a relic of the past.", #0
        "", #1
        "", #2
        "", #3
        "Society's preferences are constantly changing. What is taboo today is in style tomorrow. Why waste time worrying about society will think about who you have sex with?", #4
        "", #5
        "", #6
        "", #7
        "After all, isn't sex something to be enjoyed with a partner you love and trust? Who do you love and trust more than a close family member?", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["kissing"] = [
        "Did you know first erogenous areas that meet between two people is often the lips?", #0
        "", #1
        "", #2
        "", #3
        "When his lips meet yours and your tongues dance, this is often the very beginning of pleasurable foreplay for both of you.", #4
        "", #5
        "", #6
        "", #7
        "Lips are drivers of an immense amount of pleasure during sex. Learn to love those soft licks and kisses that you give and receive.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["lingerie"] = [
        "There's nothing wrong with signaling to him that you crave his attention by wearing lingerie.", #0
        "", #1
        "", #2
        "", #3
        "Did you know men are as stimulated by visual sexual stimuli as women are by getting touched?", #4
        "", #5
        "", #6
        "", #7
        "Your body is a sexual weapon. Dress it accordingly, and you can use it as one.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["masturbating"] = [
        "You only get one body. How can you learn what your body wants, if you never find out?", #0
        "", #1
        "", #2
        "", #3
        "Preferences change, bodies change. How can you know what feels good if you never touch yourself?", #4
        "", #5
        "", #6
        "", #7
        "Of course it is fine to prefer he is the one touching you, but he isn't always around, is he? Learn to love yourself too.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["missionary style sex"] = [
        "Sex is an intimate, pleasurable act. What better way to enjoy it than to have your lover on top of you?", #0
        "", #1
        "", #2
        "", #3
        "Open up and accept him, let him pin you to the bed, or the desk, or whatever it is that he has laid you down on and have his way with you.", #4
        "", #5
        "", #6
        "", #7
        "Watch and enjoy his face when you feel him slide inside you. Your body will bring him incredible pleasure and you can just lay back and enjoy it.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["not wearing anything"] = [
        "Naked we enter the world, and naked we leave it. Why not spend time in between naked as well?", #0
        "", #1
        "", #2
        "", #3
        "You have the freedom to wear anything you want, or nothing at all.", #4
        "", #5
        "", #6
        "", #7
        "Its your body. Show it to the world, and let other's enjoy it.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["not wearing underwear"] = [
        "When you go out without underwear on, you have a naughty little secret only you know.", #0
        "", #1
        "", #2
        "", #3
        "Only you know, unless you decide to pull up your skirt and show someone anyway.", #4
        "", #5
        "", #6
        "", #7
        "Not only will it turn you on, knowing you aren't wearing anything underneath, but it gives easy access to him too.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["polyamory"] = [
        "Love is a powerful emotion, but it has become tainted by society into being private.", #0
        "", #1
        "", #2
        "", #3
        "Is there some built in limit on how many people you can love? Why do we limit the joy and desire in our lives to just one person?", #4
        "", #5
        "", #6
        "", #7
        "Let your love flow to everyone around you. Take joy in all your relationships, without artificially limiting it for pointless societal reasons.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["public sex"] = [
        "Is it not exciting, when you at the bar, or at dinner, or at the park, when his hands reach down and grab your ass?", #0
        "", #1
        "", #2
        "", #3
        "He just wants to mark you as his. Isn't the chance that someone sees it excite you?", #4
        "", #5
        "", #6
        "", #7
        "What if you did something about it, right there in public? Would someone seeing you REALLY be that bad?", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["sex standing up"] = [
        "Sometimes things get sexy at times and in places that aren't necessarily convenient, and you need to be able to think on your feet.", #0
        "", #1
        "", #2
        "", #3
        "Sometimes the urge is so strong he doesn't want to take the time to take you to bed, he just wants you right then, right there, up against that wall.", #4
        "", #5
        "", #6
        "", #7
        "Does his cock feel any less amazing because you are upright? Doesn't it make you feel good he wants you so bad, he couldn't wait a second longer to fuck you?", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["showing her ass"] = [
        "From your thighs to you waist is your most sensitive, erogenous zone. It is no surprise that highlighting it or exposing it illicits such an arousing response.", #0
        "", #1
        "", #2
        "", #3
        "It'll get you wet too, knowing his eyes are fixated on your ass when you show it off for him.", #4
        "", #5
        "", #6
        "", #7
        "Show off your ass, knowing he'll wish every moment he looks at it that he had his hands on it too.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["showing her tits"] = [
        "Did you know that humans are the only species where females development permanent breasts?", #0
        "", #1
        "", #2
        "", #3
        "The breasts are a marvel. An erogenous zone and a sign of sexual maturity. Why would you feel the need to cover them up?", #4
        "", #5
        "", #6
        "", #7
        "Your tits are built to arouse and visually stimulate him. Don't cover up, use them to seduce and excite him!", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["skimpy outfits"] = [
        "In nature, females use a variety of methods to signal to potential partners their mating availability.", #0
        "", #1
        "", #2
        "", #3
        "Don't you want him to understand that you want to get physical? Dressing sexy helps him know that you want and appreciate his attention.", #4
        "", #5
        "", #6
        "", #7
        "It isn't about being comfortable, it is about getting, and holding, the attention of potential sexual partners when you dress provacatively.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["skimpy uniforms"] = [
        "There's nothing new or strange about workplaces that require you to wear skimpy uniforms.", #0
        "", #1
        "", #2
        "", #3
        "Women have been showing their bodies in the workplace forever, and they are excellent tools for acquiring promotions and tips.", #4
        "", #5
        "", #6
        "", #7
        "Is it wrong to use your natural physical gifts to secure work? It is no different that using your natural talents.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["taking control"] = [
        "Everyone gets tired, and every has hard days. Why should your pleasure depend on his energy?", #0
        "", #1
        "", #2
        "", #3
        "Take control of your pleasure, AND his. Put him on his back and show him how good he makes you feel.", #4
        "", #5
        "", #6
        "", #7
        "When you're on top, you can control it. The angle, speed, when and where he cums. And he'll love you for it.", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["threesomes"] = [
        "Another of society's arbitrary constructs. That sex is between TWO consenting adults. Why two?", #0
        "", #1
        "", #2
        "", #3
        "Sex feels good. Why not share him with another woman? Or what if he wants to share you with another man?", #4
        "", #5
        "", #6
        "", #7
        "Has a man ever said no to his woman bringing home another woman for him to share? Pleasure isn't a competition, it is teamwork!", #8
        "", #9
        "", #10
        "", #11
    ]
    opinion_training_dialogue_dict["vaginal sex"] = [
        "Is there anything in the world more important or more naturaly, than for a female to be penetrated by a male?", #0
        "", #1
        "", #2
        "", #3
        "The survival of the species depends on it, but guess what? Your body finds it pleasurable too!", #4
        "", #5
        "", #6
        "", #7
        "You can learn to love that incredible sensation, doing what we've been doing for millions of years, when he slides inside of you.", #8
        "", #9
        "", #10
        "", #11
    ]

    #Get's a list of 3 dialogue lines for use for training.
    #Currently we only have a single set for each opinion, so we only grab 0, 4, and 8, but as we add more we can add more variety.
    def opinion_training_get_dialogue(the_opinion: str):
        if the_opinion in opinion_training_dialogue_dict:
            return [opinion_training_dialogue_dict.get(the_opinion, [""])[0], opinion_training_dialogue_dict.get(the_opinion, [""])[4], opinion_training_dialogue_dict.get(the_opinion, [""])[8]]
        return ["Error, no opinion", "", ""]
