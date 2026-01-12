#Prone anal position. Girl is pinned down on her front, very submissive position, so we make sure to use lots of references to submissive or dominant girls in dialogue and actions.
#These actions generally increase obedience and sluttiness in dominant girls, increase happiness in submissives.
init python:
    # not available as normal position
    def build_prone_anal_decision_menu(position, person):
        position_option_list = []
        position_option_list.append((position.build_position_willingness_string(person, ignore_taboo = True).replace("Prone", "Fuck her prone"), position))
        position_option_list.append(("Let her take a break", "Nothing"))
        return position_option_list

label prone_anal_decision_label(the_girl, the_location, the_object, the_position):
    "[the_girl.possessive_title!c] seems exhausted, but you are still full of vigour. You could probably push her down and fuck her ass prone, but she may or may not like it..."

    $ picked_position = renpy.display_menu(build_prone_anal_decision_menu(prone_anal, the_girl),True,"Choice")

    if not isinstance(picked_position, Position):
        return None

    mc.name "That's too bad. I'm not done with you yet though."

    call check_position_willingness(the_girl, prone_anal, skip_dialog = True, skip_condom_ask = True) from _call_check_position_willingness_prone_anal_decision
    if _return < 1:
        the_girl "I'm sorry [the_girl.mc_title], but I really had enough."
        return None

    if not the_object.has_trait(prone_anal.requires_location):
        $ the_object = pick_object(the_girl, prone_anal)

    $ prone_anal.redraw_scene(the_girl)
    if the_position.position_tag == "missionary":
        "You grab [the_girl.title]'s hips and roll her over onto her stomach."
    elif the_position.position_tag == "doggy":
        "You grab [the_girl.title]'s ass and push her forward onto her stomach."
    else:
        "You push [the_girl.title] down onto the [the_object.name] on her stomach."

    if the_girl.is_submissive:
        "[the_girl.possessive_title!c] gives a moan as you line yourself up and push back into her ass. She is completely helpless but submits to you obediently."
        $ the_girl.change_happiness(5)
    elif the_girl.is_dominant:
        the_girl "Are you serious? Can't we just take a quick break?..."
        "[the_girl.possessive_title!c]'s question gets cut off as you line yourself up and push back into her ass. She isn't happy with being used like this but is too tired to resist."
        $ the_girl.change_happiness(-5)
    else:
        "[the_girl.possessive_title!c] gives a little yelp as you line yourself up and push back into her. She is completely helpless but submits to you obediently."
        $ the_girl.change_obedience(2)
    return the_object

label intro_prone_anal(the_girl, the_location, the_object):
    "You turn [the_girl.title] so her back is to you, then push her down onto the [the_object.name]."
    mc.name "Just lay down. I'm going to have my way with your ass now."
    if the_girl.is_submissive:
        the_girl "I'll do whatever you want, you always make me feel so good too..."
        $ the_girl.change_stats(happiness = 1, obedience = 1)
        mc.name "Yeah, that's my girl.'"
    elif the_girl.is_dominant:
        the_girl "Is that so? What do I get out of it?"
        mc.name "Why should I care? Lay down."
        "She murmurs but begins to lay down obediently."
        $ the_girl.change_stats(happiness = -2, obedience = 1)
    else:
        the_girl "Okay, just don't do anything too crazy, okay?"
        $ the_girl.change_obedience(1)
    $ prone_anal.redraw_scene(the_girl)
    "She lies down on the [the_object.name], waiting while you climb on top of her. Before you get started, you give her ass a couple smacks with your dick."
    "[the_girl.possessive_title!c] looks back at you as you line your cock up with her puckered hole. She groans as you slide your cock into her intestines."
    return

label taboo_break_prone_anal(the_girl, the_location, the_object):
    mc.name "Lay down. I want to be in control the first time I take your ass."
    $ prone_anal.redraw_scene(the_girl)
    "You take [the_girl.title]'s hands in yours and guide her down onto the [the_object.name]. You turn her back to you."
    $ the_girl.call_dialogue(f"{prone_anal.associated_taboo}_taboo_break")
    the_girl "Okay, just don't do anything too crazy, okay?"
    $ the_girl.change_obedience(2)
    $ prone_anal.redraw_scene(the_girl)
    "She lies down on the [the_object.name] on her belly. She wiggles her ass at you, waiting while you climb on top of her."
    "[the_girl.possessive_title!c] looks back at you as you line your cock up with her puckered hole. She groans as you slide into her."
    return

label scene_prone_anal_1(the_girl, the_location, the_object):
    #Scene 1, focus on visuals of prone (ass, back)
    "You push down on [the_girl.possessive_title] with your weight as you fuck her. She is pinned helplessly to the [the_object.name]."
    if the_girl.body_is_thin:
        "Your hips slap up against [the_girl.possessive_title]'s fit ass."
        "Her cheeks are tight from the exercise and care she puts into her body."
    elif the_girl.body_is_average:
        "Your hips begin to slap up against [the_girl.possessive_title]'s delicious ass."
        "Her cheeks are round but firm with just a hint of quaking with each impact."
    elif the_girl.body_is_thick:
        "Your hips begin to slap up against [the_girl.possessive_title]'s thick ass."
        "Her cheeks are full and generous, and they quake back and forth enticingly as you pound her."
    elif the_girl.body_is_pregnant:
        "Your hips begin to slap up against [the_girl.possessive_title]'s wide ass."
        "Her cheeks make a pleasing heart shape since her body has been changing with the baby growing in her belly."
        "Her belly is up against the [the_object.name], forcing her ass up at a pleasing angle."
    else:
        "Your hips begin to slap up against [the_girl.possessive_title]'s ass."
        "Her cheeks respond delightfully with each thrust."
    menu:
        "Grab her [the_girl.hair_description]":
            "You grab [the_girl.title] by her [the_girl.hair_description] and pull. The leverage helps you pound her ass harder."
            $ play_moan_sound()
            the_girl "Oh my god... ooohhhhh..."
            "She is moaning as you thrust yourself in hard and deep. [the_girl.possessive_title!c] is taking your cock like a slut."
            mc.name "That's it. Be a good little cum dump and take it."
            $ play_moan_sound()
            "She can only moan as you continue to have your way with her."

        "Spank her" if the_girl.is_submissive and the_girl.spank_level <= 8:
            "You look down at [the_girl.possessive_title]'s ass. It is [the_girl.ass_spank_description]"
            $ the_girl.slap_ass()
            "With your erection buried deep inside her bowel, you give her ass a firm spank. Her sexy cheeks quake in response."
            mc.name "[the_girl.title], your ass looks amazing when I spank it. You are such a slut. I bet you love it, don't you?"
            $ play_moan_sound()
            "[the_girl.possessive_title!c] moans at your words."
            $ play_spank_sound()
            "You pull her ass cheeks apart. You give her a hard spank with your other hand and enjoy the feeling of her buttery backdoor."
            mc.name "Do you let any guy with a hard cock fuck you in the ass like this? Or just me?"
            "[the_girl.possessive_title!c] responds quietly."
            if the_girl.is_submissive and not the_girl.can_be_spanked:
                the_girl "Just you! I love it when you get rough with me, and spank me when I've been naughty!"
                "She really seems to enjoy her spanking. Maybe you should work it into your normal foreplay..."
                $ the_girl.unlock_spanking()
            else:
                the_girl "Just you, [the_girl.mc_title]. I don't know why but it just feels so good... so right when you dominate me..."
            if the_girl.is_family:
                the_girl "It makes me so happy to serve you like this... To be [the_girl.relation_possessive_title]!"
            "You give her ass a few rough thrusts before bottoming out again."
            mc.name "That's right bitch, I own every single hole. I'll push you down and fuck you anytime I please."
            $ the_girl.discover_opinion("being submissive")
            $ the_girl.change_arousal(the_girl.opinion.being_submissive * 2)

            if mc.arousal_perc > 70:
                "[the_girl.possessive_title!c]'s tight ass feels so good. You are getting close to cumming."
                mc.name "You feel amazing. You're gonna make me cum soon."
                if the_girl.opinion.anal_creampies > 0:
                    "[the_girl.possessive_title!c] looks back at you and smiles."
                    the_girl "Oh [the_girl.mc_title], I can't wait to feel you fill me up. I hope you finish deep!"
                    "[the_girl.possessive_title!c]'s ass quivers a bit, as she imagines you cumming deep inside her backdoor."
                    $ the_girl.discover_opinion("anal creampies")
                    $ the_girl.change_arousal(the_girl.opinion.anal_creampies)
                    if the_girl.opinion.being_covered_in_cum > 0:
                        the_girl "Or you could pull out? It feels amazing when your hot cum splashes against my skin!"
                        $ the_girl.discover_opinion("being covered in cum")
                        $ the_girl.change_arousal(the_girl.opinion.being_covered_in_cum)
                        if the_girl.opinion.cum_facials > 0:
                            the_girl "Or my face! You haven't cum on my face in a while either..."
                            $ the_girl.discover_opinion("cum facials")
                            $ the_girl.change_arousal(the_girl.opinion.cum_facials)
                            "[the_girl.possessive_title!c] starts muttering to herself, fantasizing about all the different ways you could cum on, or in, her."
                elif the_girl.opinion.being_covered_in_cum > 0:
                    the_girl "Are you going to pull out? It feels amazing when your cum splashes all over my skin..."
                    "Instead of answering her, you put your hands on her hips and fuck her harder."
            else:
                "You put your hands on her hips and continue fucking her."

        "Spank her\nToo bruised to continue (disabled)" if the_girl.is_submissive and the_girl.spank_level > 8:
            pass

    return

label scene_prone_anal_2(the_girl, the_location, the_object):
    #Scene 2, focus on submissiveness of scene (spank, dirty talk, hair pulling)

    if the_girl.is_submissive:
        the_girl "Yes! Oh fuck yes!"
        $ play_spank_sound()
        "[the_girl.possessive_title!c] is really getting into being dominated. You give her ass a quick smack."
    elif the_girl.is_dominant:
        if the_girl.has_taboo("vaginal_sex"):
            the_girl "This isn't right... at least let me be on top..."
        else:
            the_girl "This isn't right... at least put it in my pussy... okay?"
        $ play_spank_sound()
        "You give her ass a smack, making her yelp."
    else:
        the_girl "Oh god... I don't know if I can take this..."
        $ play_spank_sound()
        "You give her ass a quick smack, reminding her of who is fucking whom."
    "You consider for a moment. Maybe you should take this opportunity to train her a bit..."
    menu:
        "Dominate her":
            if the_girl.is_submissive:
                mc.name "That's it, my little cock sleeve. You're doing great."
                the_girl "Oh god, thank you, I..."
                "When she starts to respond, you bring your hand around her neck and give it a little squeeze, cutting her words off."
                mc.name "I don't remember asking for a response, slut."
                $ the_girl.change_stats(happiness = 3, obedience = 3, arousal = 5)
                "Her ass clenches around in response. You can feel it quivering as you dominate her."
            elif the_girl.is_dominant:
                mc.name "I don't think so. You're my little slut, and I'll take you the way I want to, when I want to."
                $ the_girl.change_stats(happiness = -5, obedience = 2, slut = 1)
                if the_girl.is_bald:
                    "[the_girl.title] starts to say something, but you grab her neck and pull her back a little. Her ass clenches around you in response."
                else:
                    "[the_girl.title] starts to say something, but you grab her hair and pull it back some. Her ass clenches around you in response."
                "She decides to just stay quiet for now and accept it as you continue to have you way with her."
            else:
                the_girl "That's it... oh god, it's so good..."
                if the_girl.is_bald:
                    "You reach forward and grab her neck at the base of her head and pull it back some."
                else:
                    "You reach forward and grab her hair near the base of her head and pull it back some."
                the_girl "Oh fuck! Oh god fuck my ass [the_girl.mc_title]!"
                $ the_girl.change_stats(obedience = 2, arousal = 5)
                if the_girl.is_bald:
                    "You oblige her, helping correlate in her head your rough treatment with the pleasure of sex. Her ass clenches around you as you squeeze her neck."
                else:
                    "You oblige her, helping correlate in her head your rough treatment with the pleasure of sex. Her ass clenches around you as you pull her hair."
                "She is exhausted, but constantly moaning from your dominating approach."
        "Go easy on her":
            "You decide for now just to enjoy the puckered hole [the_girl.possessive_title] has pointed up at you."
            "You put both your hands around her, letting your weight pin her to the [the_object.name]."
            "Her body is trying to push back against you as you fuck her, but her exhaustion and your weight on top of her leave her helpless."
            the_girl "Mmmfff... god [the_girl.mc_title]... so good..."
    return

label scene_prone_anal_3(the_girl, the_location, the_object):
    "Being completely in control of [the_girl.possessive_title]'s body is such a turn-on. You push your weight down onto her as you fuck her."
    the_girl "Oh fuck... [the_girl.mc_title] it's so good..."
    menu:
        "Threaten to creampie her ass" if not mc.condom:
            mc.name "God your ass is so tight. I can't wait to dump my load inside it."
            $ the_girl.discover_opinion("anal creampies")
            if the_girl.has_anal_fetish or the_girl.has_cum_fetish:
                the_girl "Yes! Oh fuck yes make sure you cum deep [the_girl.mc_title]!"
                $ the_girl.change_arousal(the_girl.opinion.anal_creampies * 3)
                "Goosebumps raise up all along her shoulders. It is a massive turn-on for her to hear you threaten to cum inside her."
            elif the_girl.opinion.anal_creampies > 0:
                the_girl "Oh god, you can cum inside me if you want... I think I want you to!"
                $ the_girl.change_arousal(the_girl.opinion.anal_creampies * 2)
            elif the_girl.opinion.anal_creampies < 0:
                the_girl "No way... please don't! It's so gross after when guys cum back there..."
                $ the_girl.change_arousal(the_girl.opinion.anal_creampies * 2)
            else:
                the_girl "Oh my god... you wouldn't... would you?"
        "Threaten to remove the condom" if mc.condom and not mc.has_removed_condom:
            mc.name "Your ass feels great... but I bet it would feel even better raw. Maybe I should just slip this thing off?"
            $ the_girl.discover_opinion("anal creampies")
            if the_girl.has_anal_fetish or the_girl.has_cum_fetish:
                the_girl "You should! I don't know why you wear those stupid things anyway. You should take it off!"
            elif the_girl.opinion.anal_creampies > 0:
                the_girl "I mean, if you really wanted to... I wouldn't mind it if you went in bare..."
                "Her voice drops to a whisper."
                the_girl "Or if you even finish in me like that..."
            elif the_girl.opinion.anal_creampies < 0:
                the_girl "No! Please don't, I really don't want your cum leaking out of my ass all day long."
            else:
                the_girl "I mean, if you really wanted to... it's not like I could stop you!"
            menu:
                "Remove Condom":
                    "You slowly pull out of [the_girl.possessive_title]. You reach down and pull the condom off, then toss it up by her face, making sure she sees it."
                    if the_girl.has_anal_fetish or the_girl.has_cum_fetish:
                        "When she sees the condom and realises what you are about to do, she pushes her ass back towards you, trying to help you penetrate her bare."
                        $ play_moan_sound()
                        "You slide into her backdoor without any protection this time. She moans and arches her back."
                        $ the_girl.change_arousal(the_girl.opinion.anal_creampies * 3)
                        the_girl "That's it... now fuck my ass good, [the_girl.mc_title]!"
                    elif the_girl.opinion.anal_creampies > 0:
                        the_girl "Oh god, you're really going to do it! Oh fuck..."
                        $ play_moan_sound()
                        "You slide into her backdoor without any protection this time. She moans and arches her back."
                        $ the_girl.change_arousal(the_girl.opinion.anal_creampies * 2)
                    elif the_girl.opinion.anal_creampies < 0:
                        the_girl "Oh my god. This can't be happening..."
                        $ the_girl.change_stats(happiness = -10, love = -3, obedience = 3, arousal = the_girl.opinion.anal_creampies * 2)
                        "You slide into her ass without any protection this time. Her body is stiff and unmoving."
                    else:
                        the_girl "Oh god, you're really going to do it! Oh fuck..."
                        $ play_moan_sound()
                        "You slide into her ass without any protection this time. She moans at the sensations."
                    $ mc.condom = False
                    $ use_condom = False # don't put a condom on again this loop
                "Leave it on":
                    mc.name "Well maybe I will do that in a minute, you little ass slut."
        "Degrade her":
            mc.name "Damn right it's good. You are such a cock hungry slut; your holes are just begging to be stuffed."
            mc.name "Don't worry, I'm gonna fuck your slutty holes until you can barely walk, bitch!"
            if the_girl.is_submissive:
                $ play_moan_sound()
                "[the_girl.possessive_title!c] moans as you degrade her. Her submission to you is total."
                the_girl "I'm just glad you find my holes pleasurable, [the_girl.mc_title]!"
                mc.name "Me too, whore."
                $ play_moan_sound()
                "You grab her by her [the_girl.hair_description] and pull a little bit as you fuck her harder for a bit. She moans and writhes from being treated like a fuck doll."
                $ the_girl.change_arousal(5)
            else:
                the_girl "I just want you to feel good [the_girl.mc_title]..."
                mc.name "Me too, whore."
                "You grab her by her [the_girl.hair_description] and pull a little bit as you fuck her harder for a bit, showing her who the male alpha is."
                $ the_girl.change_obedience(1)
        "Threaten to pull out":
            mc.name "I can't wait to pull out and cum all over that amazing ass of yours."
            if the_girl.has_cum_fetish:
                the_girl "Oh fuck yes! Cover me in your sticky cum [the_girl.mc_title]!"
                "Goosebumps erupt all over her back as she imagines you cumming all over her. She is such a cum slut."
                $ the_girl.change_arousal(the_girl.opinion.being_covered_in_cum * 3)
            elif the_girl.opinion.being_covered_in_cum > 0:
                the_girl "Ohhh, that sounds nice. I love the feeling of your hot cum on my skin..."
                "[the_girl.possessive_title!c] moans a bit as she imagines the feel of your cum splashing all over her."
                $ the_girl.change_arousal(the_girl.opinion.being_covered_in_cum * 2)
            else:
                "[the_girl.title] stays quiet as you continue to fuck her."

    return

label transition_prone_anal_prone_bone(the_girl, the_location, the_object):
    "You slide your cock out of her ass and drag it down between her legs, ending with your tip resting against her pussy."
    mc.name "No, this is what I really want."
    if the_girl.has_taboo("vaginal_sex"):
        $ the_girl.call_dialogue(f"{doggy.associated_taboo}_taboo_break")
        "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
        "After a moment of resistance your cock spreads her [the_girl.pubes_description] pussy open and you slide smoothly inside her."
        the_girl "Mmmhph...YES!!"
    else:
        "You ram your whole length into her wet pussy and start pounding her."
        the_girl "Aahhh...mmmhph...aahhh..."
    return


label outro_prone_anal(the_girl, the_location, the_object):
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her ass it's not long before you're pushed past the point of no return."
    mc.name "I'm going to cum!"
    $ climax_controller = ClimaxController(["Cum inside her", "anal"],["Cum on her ass","body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside her":
        $ play_moan_sound()
        "You use your full weight to push your cock deep inside [the_girl.possessive_title]'s ass as you climax. She gasps and moans as you pin her to the [the_object.name]."

        if mc.condom and not mc.has_removed_condom:
            #$ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."
            "Your condom is ballooned with your seed, hanging off your cock to one side."

            call post_orgasm_condom_routine(the_girl, prone_anal) from _call_post_orgasm_condom_routine_prone_anal
        else:
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish or the_girl.has_anal_fetish:
                "[the_girl.possessive_title!c]'s body goes rigid as your cum pours into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
            $ the_girl.call_dialogue("cum_anal")
            $ the_girl.cum_in_ass()
            $ prone_anal.redraw_scene(the_girl)
            if not mc.condom and the_girl.has_anal_fetish:
                # If she's into both...
                $ the_girl.discover_opinion("anal creampies")
                the_girl "Please keep it inside... Just a little while longer, please!"
                $ play_moan_sound()
                "She bites her lip, closes her eyes, and moans."
                "Eventually your dick starts to soften..."

        "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."

    elif the_choice == "Cum on her ass":
        $ the_girl.cum_on_ass()
        $ prone_anal.redraw_scene(the_girl)
        if mc.condom and not mc.has_removed_condom:
            "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s ass."
        else:
            "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_girl.title]'s ass."
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title!c]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            $ play_moan_sound()
            "[the_girl.possessive_title!c] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            "She truly is addicted to your cum."
        if the_girl.is_submissive:
            "[the_girl.title] lays there, whimpering. It seems you nearly fucked her senseless, and she loved it."
            $ the_girl.change_happiness(10)
        elif the_girl.is_dominant:
            "[the_girl.title] lays there, whimpering. It seems you nearly fucked her senseless, and it scared her."
            $ the_girl.change_stats(happiness = -5, obedience = 2)
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s exhausted body covered in your semen."
    return


label transition_default_prone_anal(the_girl, the_location, the_object):
    $ prone_anal.redraw_scene(the_girl)
    "You put [the_girl.title] on her stomach and lie down on top of her, lining your hard cock up with her tight asshole."
    "After running the tip of your penis along her slit a few times to get it wet, you push forward, sliding inside her backdoor. She gasps softly and closes her eyes."
    return

label strip_prone_anal(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = prone_anal.position_tag)
    "[the_girl.possessive_title!c] struggles out of her [the_clothing.name] and throws it to the side."
    "You line yourself up and push back into her ass. She sighs happily when you slip back inside her."
    return

label strip_ask_prone_anal(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], can you take off my [the_clothing.name], I need to feel more?"
    "[the_girl.title] pants as you fuck her."
    menu:
        "Take it off":
            mc.name "Alright."
            $ the_girl.draw_animated_removal(the_clothing, position = prone_bone.position_tag)
            "You move back and pull off her [the_clothing.name], throwing it to the side."
            "She sighs happily when you get on top of her and slide your cock back into her bowels."

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her ass back up and moans happily."
            else:
                the_girl "Does it make me look like the cum–hungry slut that I am? That's all I want to be for you [the_girl.mc_title], your dirty little cum dumpster!"
                $ play_moan_sound()
                "She grinds her ass on your cock and moans ecstatically."
    return

label orgasm_prone_anal(the_girl, the_location, the_object):
    "[the_girl.title] turns her head and pants loudly. Suddenly she bucks her hips up against yours and gasps."
    $ the_girl.call_dialogue("climax_responses_anal")
    "Her [the_girl.pubes_description] pussy is dripping wet as you fuck through her assgasm. She paws at the [the_object.name], trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down your thrusts to catch your own breath."
    the_girl "[the_girl.mc_title]... fuck! I Can't... oh my god..."
    "[the_girl.possessive_title!c] is getting fucked senseless as you continue to have your way with her."
    return

label prone_anal_double_orgasm(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You smack [the_girl.title]'s ass and moan, in the final stretch before your orgasm."
    the_girl "[the_girl.mc_title]... [the_girl.mc_title]... I'm gonna cum!"
    "She weakly manages to call out your name as she gets ready to cum."
    mc.name "I'm cumming too!"

    $ climax_controller = ClimaxController(["Cum inside her","anal"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside her":
        if mc.condom and not mc.has_removed_condom:
            $ play_moan_sound()
            "You push your weight down on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum. She moans as you dump your load into her, barely contained by your condom."
            the_girl "Oh god!"
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.have_orgasm()
            "You can feel her ass pulsating all around you as you cum in unison. Her bowels are milking your cum, with only a thin layer of latex keeping it from spilling deep inside her."
            "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock."
            "You pull out and sit back. The condom is ballooned and sagging with the weight of your seed."
            if the_girl.opinion.drinking_cum > 1 and the_girl.sluttiness > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title!c] points to your crotch, but can't get out the words she wants to say."
                mc.name "You want my cum, slut?"
                "She nods. You take the condom off. Instead of handing it to her though, you put the end of it up to her lips and try to feed it to her."
                "It drops down her chin but she managed to drink some of it."
                $ the_girl.cum_in_mouth()
                $ the_girl.change_slut(the_girl.opinion.drinking_cum, 70)
            else:
                "You take off the condom, tie the end in a knot and throw it away."
            "You sigh contentedly and enjoy the post-orgasm feeling of relaxation. [the_girl.possessive_title!c] can barely move, still face down on the [the_object.name]."
        else:
            $ play_moan_sound()
            "You push your weight down on [the_girl.possessive_title]'s hips and drive your cock deep inside her as you cum. She moans in time with each new shot of hot semen deep inside her rectum."
            "You can feel her bowels quivering all around you as you cum in unison. Her body is milking your cum, you swear it feels like she's sucking your cock with her intestines."
            "After you finish, you leave your cock deep inside her, enjoying her hole pulsating with each aftershock."
            $ the_girl.call_dialogue("cum_anal")
            $ the_girl.cum_in_ass()
            $ prone_anal.redraw_scene(the_girl)
            $ the_girl.have_orgasm()
            $ climax_controller.do_clarity_release(the_girl)
            if not mc.condom and the_girl.has_anal_fetish:
                # If she's into both...
                $ the_girl.discover_opinion("anal creampies")
                the_girl "Please keep it inside... Just a little while longer, please!"
                $ play_moan_sound()
                "She bites her lip, closes her eyes, and moans."
                "Eventually your dick starts to soften..."

            "You slowly pull out of [the_girl.possessive_title]'s asshole, then roll over next to her."

    elif the_choice == "Cum on her ass":
        if mc.condom and not mc.has_removed_condom:
            "You pull out of [the_girl.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
        else:
            "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass."
        $ the_girl.cum_on_ass()
        $ prone_anal.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        "She reaches down between her legs and starts to play with herself, bringing herself to orgasm in unison with you."
        $ the_girl.have_orgasm()
        the_girl "Oh god I'm cumming!"
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.title] covered in your semen."
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title!c]'s body goes rigid and goosebumps erupt all over her body as her brain registers your cum on her."
            "[the_girl.possessive_title!c] revels in bliss as she mindlessly rubs in your cum and licks of her fingers to heighten her orgasm."
            "She truly is addicted to your cum."
        elif the_girl.opinion.anal_creampies > 0:
            the_girl "What a waste, you should have put that inside me."
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh wow, there's so much of it..."

    $ post_double_orgasm(the_girl)
    return
