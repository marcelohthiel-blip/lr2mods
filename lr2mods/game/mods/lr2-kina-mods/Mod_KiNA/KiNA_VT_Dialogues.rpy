#Counter = KED01

#revamped dialogue for base personalities, mainly to catch virgins, introduced with Elkrose's VT mod

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["reserved_vaginal_sex_taboo_break"] = "reserved_vaginal_sex_taboo_break_revamp"
    config.label_overrides["wild_vaginal_sex_taboo_break"] = "wild_vaginal_sex_taboo_break_revamp"
    config.label_overrides["relaxed_vaginal_sex_taboo_break"] = "relaxed_vaginal_sex_taboo_break_revamp"
    config.label_overrides["introvert_vaginal_sex_taboo_break"] = "introvert_vaginal_sex_taboo_break_revamp"
    config.label_overrides["cougar_vaginal_sex_taboo_break"] = "introvert_vaginal_sex_taboo_break_revamp"

label reserved_vaginal_sex_taboo_break_revamp(the_person):
    if vt_enabled():
        if the_person.vaginal_virgin == 0:
            mc.name "Are you sure about this?"
            "She nods."
            the_person "I want this. I wanted it to be yours, [the_person.mc_title]."
            "She closes her eyes and takes a deep breath."
            the_person "I...I'm ready."
            mc.name "I'll be gentle, tell me if you want it slow, okay."
            "She nods."
            $ take_virginity(the_person)
        elif the_person.effective_sluttiness() >= 60:
            the_person "[the_person.mc_title], I'm not ashamed to say I'm very excited right now!"
            "She giggles gleefully."
            the_person "Come on and fuck me!"
        elif the_person.love >= 45:
            the_person "Go ahead [the_person.mc_title]. I think we're both ready for this."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Oh my god, what am I doing here [the_person.mc_title]?"
                the_person "I'm not the type of person to do this... Am I? Is this who I've always been, and I've just been lying to myself?"
                mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
                "She closes her eyes and takes a deep breath."
                the_person "I... I want to have sex with you. I'm ready."
            else:
                the_person "I'm glad you're doing this properly this time."
                "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    else:
        if the_person.effective_sluttiness() >= 60:
            the_person "[the_person.mc_title], I'm not ashamed to say I'm very excited right now!"
            "She giggles gleefully."
            the_person "Come on and fuck me!"
        elif the_person.love >= 45:
            the_person "Go ahead [the_person.mc_title]. I think we're both ready for this."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Oh my god, what am I doing here [the_person.mc_title]?"
                the_person "I'm not the type of person to do this... Am I? Is this who I've always been, and I've just been lying to myself?"
                mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
                "She closes her eyes and takes a deep breath."
                the_person "I... I want to have sex with you. I'm ready."
            else:
                the_person "I'm glad you're doing this properly this time."
                "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    return

label wild_vaginal_sex_taboo_break_revamp(the_person):
    if vt_enabled():
        if the_person.vaginal_virgin == 0:
            mc.name "Tell me what you want."
            the_person "I want you to have my virginity, [the_person.mc_title]."
            "She closes her eyes and takes a deep breath."
            the_person "Fuck me. Make me scream."
            "She bit her lip, anticipation making her quiver with need."
            $ take_virginity(the_person)
        elif the_person.effective_sluttiness() >= 60:
            the_person "It's about time we did this. Come on then, get that cock inside me and fuck me!"
        elif the_person.love >= 45:
            the_person "Are you ready for this? I hope you're planning to rock my world."
            mc.name "That is the plan, I hope you can handle it."
            the_person "I can handle anything you can throw at me. Come on then, fuck me like you mean it!"
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Look at that cock... Fuck, I hope you don't stretch out my pussy too badly."

            else:
                the_person "If your cock feels half as big in my pussy as it did up my ass I'm in for a good time."
                the_person "Come on, fuck me [the_person.mc_title]!"
    else:
        if the_person.effective_sluttiness() >= 60:
            the_person "It's about time we did this. Come on then, get that cock inside me and fuck me!"
        elif the_person.love >= 45:
            the_person "Are you ready for this? I hope you're planning to rock my world."
            mc.name "That is the plan, I hope you can handle it."
            the_person "I can handle anything you can throw at me. Come on then, fuck me like you mean it!"
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Look at that cock... Fuck, I hope you don't stretch out my pussy too badly."

            else:
                the_person "If your cock feels half as big in my pussy as it did up my ass I'm in for a good time."
                the_person "Come on, fuck me [the_person.mc_title]!"
    return

label relaxed_vaginal_sex_taboo_break_revamp(the_person): #TODO: add a "I don't do anal""you do for me" style taboo break
    if vt_enabled():
        if the_person.vaginal_virgin == 0:
            mc.name "Are you sure about this?"
            the_person "No... But... Well, I don't want you to get blue balled either, [the_person.mc_title]."
            "She closes her eyes and takes a deep breath."
            the_person "This is it, then."
            "She bit her lip, trembling with anticipation."
            $ take_virginity(the_person)
        elif the_person.effective_sluttiness() >= 60:
            the_person "Whew, here we go! I'm so excited!"
        elif the_person.love >= 45:
            "[the_person.title] nods eagerly."
            the_person "I'm ready [the_person.mc_title], I'm ready to feel you inside me."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "So this is it, huh?"
                mc.name "Looks like it. Are you ready?"
                the_person "No... But I don't want you to stop either."
            else:
                "[the_person.title] giggles."
                the_person "This feels so backwards! You've already been in my ass, but now we're doing it properly."
                "She shrugs."
                the_person "At least this time it should be easier for you to fit inside."
    else:
        if the_person.effective_sluttiness() >= 60:
            the_person "Whew, here we go! I'm so excited!"
        elif the_person.love >= 45:
            "[the_person.title] nods eagerly."
            the_person "I'm ready [the_person.mc_title], I'm ready to feel you inside me."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "So this is it, huh?"
                mc.name "Looks like it. Are you ready?"
                the_person "No... But I don't want you to stop either."
            else:
                "[the_person.title] giggles."
                the_person "This feels so backwards! You've already been in my ass, but now we're doing it properly."
                "She shrugs."
                the_person "At least this time it should be easier for you to fit inside."
    return

label introvert_vaginal_sex_taboo_break_revamp(the_person):
    if vt_enabled():
        if the_person.vaginal_virgin == 0:
            the_person "Oh god, ohhh... god!"
            mc.name "Are you sure about this?"
            the_person "Is it painful? It's painful isn't it, [the_person.mc_title]?"
            "She closes her eyes and takes a deep breath."
            mc.name "Don't worry, I'll be gentle."
            the_person "This is it, then."
            "She bit her lip, trembling with anticipation."
            the_person "Mommy, Daddy, I'm a {i}big{/i} girl now."
            $ take_virginity(the_person)
        elif the_person.effective_sluttiness() >= 60:
            the_person "Do it [the_person.mc_title], I want to feel you inside me."
        elif the_person.love >= 45:
            the_person "I think I'm ready [the_person.mc_title]. I want to feel even closer to you."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Oh no, I'm so nervous!"
                mc.name "Don't be, I'll be gentle."
                the_person "You don't think... I'm a slut or something, do you?"
                menu:
                    "Of course you are":
                        if mc.condom:
                            mc.name "Of course I do. You're about to let me fuck your sweet little pussy."
                        else:
                            mc.name "Of course I do. You're about to let me fuck your pussy raw."
                        mc.name "You're a dirty little slut, but there's nothing wrong with that. You just have to embrace it."
                        "She nods."
                        $ the_person.change_slut(1 + the_person.opinion.being_submissive)
                        the_person "I think I've known that deep down for a while..."

                    "Of course not":
                        mc.name "Of course not. You're just doing what you want to do to be happy."
                        mc.name "Never let anyone tell you what should make you happy."
                        $ the_person.change_happiness(2)
                        "She smiles and nods."
                        the_person "Thank you. I've been feeling so unsure lately."
            else:
                the_person "You've fucked my ass, now tell me how my pussy feels."
    else:
        if the_person.effective_sluttiness() >= 60:
            the_person "Do it [the_person.mc_title], I want to feel you inside me."
        elif the_person.love >= 45:
            the_person "I think I'm ready [the_person.mc_title]. I want to feel even closer to you."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Oh no, I'm so nervous!"
                mc.name "Don't be, I'll be gentle."
                the_person "You don't think... I'm a slut or something, do you?"
                menu:
                    "Of course you are":
                        if mc.condom:
                            mc.name "Of course I do. You're about to let me fuck your sweet little pussy."
                        else:
                            mc.name "Of course I do. You're about to let me fuck your pussy raw."
                        mc.name "You're a dirty little slut, but there's nothing wrong with that. You just have to embrace it."
                        "She nods."
                        $ the_person.change_slut(1 + the_person.opinion.being_submissive)
                        the_person "I think I've known that deep down for a while..."

                    "Of course not":
                        mc.name "Of course not. You're just doing what you want to do to be happy."
                        mc.name "Never let anyone tell you what should make you happy."
                        $ the_person.change_happiness(2)
                        "She smiles and nods."
                        the_person "Thank you. I've been feeling so unsure lately."
            else:
                the_person "You've fucked my ass, now tell me how my pussy feels."
    return

label cougar_vaginal_sex_taboo_break_revamp(the_person):
    if vt_enabled():
        if the_person.vaginal_virgin == 0:
            the_person "Does this surprise you, [the_person.mc_title]?"
            the_person "You gonna fuck a virgin!"
            if (the_person.sex_record.get("Vaginal Sex", 0) == 0):
                mc.name "I am honored to be your first [the_person.title]"
            else:
                mc.name "If you like the feeling, just tell me so I can give the serum again."
            mc.name "You ready? I'll start slow."
            the_person "No... I want it hard! Go to town on my pussy!"
            mc.name "As you wish."
            $ take_virginity(the_person)

    else:
        if the_person.effective_sluttiness() >= 60:
            the_person "[the_person.mc_title], I'm not ashamed to say I'm very excited right now!"
            "She giggles gleefully."
            the_person "Come on and show me what you can do with that monster!"
        elif the_person.love >= 45:
            the_person "Go ahead [the_person.mc_title]. I think we're both ready for this."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "Oh my god, what am I doing here [the_person.mc_title]?"
                the_person "I'm not the type of person to do this... Am I? Is this who I've always been, and I've just been lying to myself?"
                mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
                "She closes her eyes and takes a deep breath."
                the_person "I... I want to have sex with you. I'm ready."
            else:
                the_person "I'm glad you're doing this properly this time."
                "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    return