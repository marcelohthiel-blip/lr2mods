label lily_first_best_friend(the_sister, the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "I've got some note cards right here if you need more."
    "You give a weak smile and she returns it, shaking her head a bit at the joke."
    the_person "No... I wanted to apologise again. I know I kind of blind sided you and I wanted to make sure things were good between us."
    mc.name "I admit it was surprising, but I'll get over it. Does that mean you'll still be around."
    the_person "At least for the semester, and after that... well I hope to keep spending time with [the_sister.fname]. If that's okay with you."
    mc.name "Of course, I'd never put some minor awkwardness over the happiness of my sister."
    the_person "Thank you, spending time with [the_sister.fname] is important to my happiness too."
    mc.name "It is good that you two get along so well. I know it can sometimes be hard to find friends in a class."
    the_person "Friends... right, has she... um... said anything about our friendship?"
    mc.name "She likes you, thinks you are smart and hard working."
    the_person "Oh, likes me as a classmate, that is good I suppose."
    mc.name "As a person too, she thinks you are fun to spend time with."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    the_person "Yeah... she is great too..."
    "Something about the way she looks off into space as she talks about [the_sister.fname] catches your attention."
    mc.name "Were you hoping maybe for something more than just friendship with my sister?"
    "[the_person.fname] blushes and turns her head slightly."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "I never see her with boys at school, it's like she just doesn't see them. So I started to wonder if she was, you know..."
    the_person "Sorry, is this going to make things more awkward?"
    mc.name "It doesn't have to, in fact it might make it less so. I mean I don't have to worry about what I did wrong if [the_sister.fname] is the reason you broke off our relationship."
    the_person "That was a big part of it, I meant it when I said I was looking for something different. I didn't think explaining it at the time would help."
    mc.name "At the time it probably wouldn't have, but I understand."
    the_person "At the risk of making it awkward again... do you know if [the_sister.fname] would ever consider someone like me?"
    "That is a tough question, you might want to be careful how you answer. It could have a pretty big impact on how your relationships progress."
    menu:
        "Absolutely (not fully written) (disabled)":
            mc.name "She would definitely be open to the idea of spending time with another woman."
            mc.name "She has done it before, but usually with a man present as well."
            the_person "Wow, I didn't think she was that adventurous. Do you happen to know what guy it was with?"
            menu:
                "Tell her":
                    mc.name "It was me, we have been fucking for awhile, and recently our mom joined us as well."
                    mc.name "If you'd like, I could suggest that you join us the next time we are looking for an extra partner."
                    "[the_person.title]'s face clearly shows her shock. She stands there frozen not sure how to react."
                    mc.name "I'm serious, if you'd like we can go ask right now. I'm sure she wouldn't mind."
                    "She stammers a bit, but clearly can't form a coherent response."
                    "You figure it might be better to cut to the chase, so you take her by the wrist and gently pull her down the hall to your sister's room."
                    $ scene_manager.add_actor(the_sister, position = "sitting")
                    mc.name "Hey, [the_sister.title], [the_person.fname] thinks you are hot and wondered if you would ever consider someone like her."
                    if willing_to_threesome(the_person, the_sister):
                        the_sister "That is sweet, she is pretty sexy too. Do you think we should get together."
                        mc.name "Absolutely, you two would be so hot together. I'd love to watch, or maybe even join in."
                        the_sister "Sounds good to me, what do you think [the_person.fname]."
                        "[the_person.fname] still can't figure out what to do, and stands there stunned."
                        "[the_sister.fname] grins and starts to walk forward, slowly pulling at the hem of her shirt to expose part of her midriff."
                        if willing_to_threesome(the_person, the_sister):
                            "[the_person.fname] is still frozen, but it is clear she wants this to happen."
                            "By the time [the_sister.title] is next to [the_person.fname] her shirt is off, and she leans forward to kiss her tentatively."
                            the_person "God, this is going so fast but I am so excited."
                            $ the_person.event_triggers_dict["friend_with_benefits"] = 100




                        else:
                            "[the_person.fname] takes a step back, horror starting to appear on her face."
                            "Suddenly, [the_sister.fname] doubles over laughing, dropping her seductive act."
                            the_sister "I'm so sorry, [the_person.fname]. I couldn't resist playing along. The look on your face."
                            "[the_sister.fname] shoots you a dirty look while [the_person.fname] isn't watching."
                            $ the_sister.change_happiness(-5)
                            the_person "Wait, what do you mean?"
                            mc.name "I'm sorry [the_person.title], I was just messing with you."
                            the_sister "I should have warned you about my brother, he can be so inappropriate sometimes."
                            the_person "Oh, right, I should have known you wouldn't be interested in me."
                            "[the_person.title] looks crestfallen as she takes another step back"
                            the_sister "Wait, he didn't make up that part?"
                            "[the_person.title] stammers a bit but can't get anything coherent out, instead she turns and rushes down the hall towards the bathroom."
                            the_sister "God, [mc.name], you have a real way with people you know that."
                            mc.name "I just don't see any reason to hesitate, I was trying to help."
                            the_sister "Well I think you've done enough, why don't you leave us alone for a bit."
                            $ the_person.change_happiness(-5)
                            $ the_person.event_triggers_dict["friend_with_benefits"] = 4
                            "Well, that was interesting. You head back to your room while [the_sister.title] goes to try and talk with [the_person.title]."


                    else:
                        the_sister "Not funny, [mc.name]. I've told you not to harass my friends when they are over."
                        $ the_sister.change_happiness(-5)
                        $ the_sister.change_love(-5)




                "Be cautious":
                    mc.name "It's not really something I got a ton of details about..."
                    the_person "Right, of course. She is your sister after all."
                    mc.name "Exactly, but if you want I can try and talk to her and find out more. See if maybe you have a chance."
                    the_person "Really? Thanks, [mc.name] that would be great."
                    $ the_person.change_happiness(5)
                    mc.name "Come see me next week and I'll give you an update."
        "Potentially":
            mc.name "I know she has been fairly non-traditional with relationships in the past."
            mc.name "I don't see any reason why it wouldn't work with you."
            the_person "Oh, good, I've been so nervous about scaring her away if it wasn't something she wants."
            mc.name "I could talk to her if you want, see what she thinks of the idea."
            the_person "That would be great, thanks [the_person.mc_title]!"
            mc.name "Come see me next week and I'll give you an update."
        "Maybe":
            mc.name "I'm not really sure, we haven't spent a lot of time talking about her sexual preferences."
            the_person "Oh, right, of course. I just meant has she ever dated anyone like me?"
            mc.name "Sorry, [the_person.fname], you would be the first but that doesn't mean it can't happen."
            mc.name "I could try and bring the topic up, get a feel for which way she would lean."
            the_person "Really? That would be awesome, thanks [the_person.mc_title]!"
            mc.name "Come see me next week and I'll give you an update."
        "No":
            mc.name "I can't imagine that she would."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            if not the_sister.has_taboo("sucking_cock") or not the_sister.has_taboo("vaginal_sex") or not the_sister.has_taboo("anal_sex"):
                mc.name "I am confident that she likes dick and is currently getting all she needs."
            else:
                mc.name "I've never known her to show an interest in other girls. You should probably look elsewhere."
            mc.name "If you want, I could try to help you find someone who is interested."
            if the_person.sluttiness > 160: # currently disabled
                the_person "You know that would be kind of nice."
                # crisis to find her a partner
                mc.name "Come see me next week and I'll give you an update."
            else:
                the_person "No, that isn't really what I'm looking for."
                the_person "I guess I'll just keep hanging out with your sister and see if anything develops."
                mc.name "Alright, I'm here if that doesn't work out."
            $ the_person.event_triggers_dict["friend_with_benefits"] = 4 # she has to do it alone
    the_person "Alright, have a good night."
    "[the_person.title] waves goodbye as she leaves to get back to [the_sister.fname]."
    $ willing = lily_willing_threesome()
    if willing:
        "[the_sister.title] is certainly willing to do things with another girl."
    else:
        "You aren't sure what [the_sister.title] thinks of sex with another girl."
    "You definitely need to talk to her about this. Of course you also need to decide what you want her to do."
    if the_sister.event_triggers_dict.get("vaginal_revisit_complete", False) == True:
        "She has become your fuck toy and getting her into a new relationship might change that."
    elif the_sister.event_triggers_dict.get("anal_revisit_complete", False) == True:
        "She has been letting you fuck her ass, and getting her into a new relationship might put a stop to that."
    elif the_sister.event_triggers_dict.get("oral_revisit_complete", False) == True:
        "Now that she is willing to suck you off you aren't sure you want her to find someone else."
    "Should you encourage her to start dating [the_person.title]? If you do is there any possibility that you end up joining them in the future?"
    $ lily_first_followup = Action("[the_sister.name] First Followup", lily_mon_followup_requirement, "lily_first_followup_label")
    $ mc.business.add_mandatory_crisis(lily_first_followup)
    $ scene_manager.clear_scene() 
    call advance_time from _call_advance_first_bf
    return

label lily_first_followup_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    "As you are getting ready for bed you decide there is no time like the present and make your way to [the_sister.possessive_title]'s room."
    $ mc.location = lily_bedroom
    $ scene_manager.add_actor(the_sister, position = "sitting")
    the_sister "Hey there, [the_sister.mc_title]. Should I get used to seeing you on Mondays?"
    if cousin.location == lily_bedroom:
        $ cousin.change_location(downtown)
        mc.name "Hey, [the_sister.title], where is [cousin.fname]?"
        the_sister "Don't know, don't care. Just happy to have some alone time."
        mc.name "Oh, sorry, I can go."
        the_sister "No, wait! I meant from her, I like spending time with you."
        the_sister "You are always welcome to spend time with me."
    if mc.event_triggers_dict.get("lily_comfort", None) == "sex" or mc.event_triggers_dict.get("lily_comfort", None) == "hand" or mc.event_triggers_dict.get("lily_comfort", None) == "oral":
        "While it is tempting to try for a repeat of last time, you should actually talk to her first."
        "Maybe afterwards..."
        mc.name "I mean... I'm not gonna argue if you want me to come see you at night."
        "She smiles and starts to walk towards you before you hold out a hand to stop her."
        mc.name "Unfortunately that isn't why I'm here. I need to ask you some delicate questions."
    else:
        mc.name "I'd like that, but it's kinda going to depend on how you answer some delicate questions."
    the_sister "Oh, what's going on?"
    mc.name "First, I want you to promise to take some time to think. This is a bit complicated and I don't want you to make any rash decisions."
    the_sister "Now I'm a little worried, is something wrong with you or mom?"
    mc.name "No, nothing like that. Nothing is wrong, it's just well... [the_person.fname] asked me something and I wasn't sure how to answer her."
    the_sister "[the_person.fname]? She was just here. What did she ask?"
    mc.name "Look, she is scared of messing up your friendship and that is the last thing she wants."
    mc.name "Can you just promise you'll think before you do anything major with this information?"
    the_sister "...okay... I promise."
    if the_sister.has_role(girlfriend_role):
        "Well, no going back now. How are you going to ask your sister/girlfriend if she wants to start dating your ex?"
        mc.name "So you and I are dating, but obviously that relationship has some inherent difficulties."
        mc.name "[the_person.fname] and I hit it off after a few conversations, and started spending some time together too."
        the_sister "I know, and that is fine. I still don't understand where this is going."
        mc.name "I'm getting there, hang on."
        mc.name "So you know she kinda broke up with me, but neither of us have told you why."
        mc.name "The thing is that while she was getting closer to me she started to develop a crush on someone else..."
        mc.name "You."
        "Understanding dawns on [the_sister.possessive_title]'s face and you can tell that she is deep in thought, no doubt re-examining her recent interactions with [the_person.title]."
        mc.name "Obviously I can't blame her for picking you over me, I would do the same thing."
        "That earns you a faint smile, although she is still thinking."
        mc.name "And it would be pretty hypocritical of me to say you couldn't explore a relationship with her when I already have."
        mc.name "So she is scared to come out to you and wreck your friendship if you wouldn't be interested, but I couldn't exactly explain why she hasn't seen you flirting with boys at school."
    else:
        "Well, no going back now. How are you going to ask your sister if she wants to start dating your ex?"
        if not the_sister.has_taboo("vaginal_sex"):
            mc.name "So you and I have gotten very close, but I'm not sure what kind of future we really have."
        elif not the_sister.has_taboo("sucking_cock"):
            mc.name "Getting close to you has been lots of fun, but there are limits to what we should really do together."
        mc.name "[the_person.fname] and I hit it off after a few conversations, and started spending some time together too."
        the_sister "I know, and that is fine. I still don't understand where this is going."
        mc.name "I'm getting there, hang on."
        mc.name "So you know she kinda broke up with me, but neither of us have told you why."
        mc.name "The thing is that when we fooled around it was clear she wanted something else, and she was developing a crush on someone else..."
        mc.name "You."
        "Understanding dawns on [the_sister.possessive_title]'s face and you can tell that she is deep in thought, no doubt re-examining her recent interactions with [the_person.title]."
        mc.name "Obviously I can't blame her for picking you over me, I would do the same thing."
        "That earns you a faint smile, although she is still thinking."
        mc.name "And it would be pretty hypocritical of me to say you couldn't fool around with her when I already have."
        mc.name "So she is scared to come out to you and make unwelcome advances, but I couldn't exactly explain why she hasn't seen you hanging off any boys at school."
    the_sister "Wow... that is a lot. I want to say I'm surprised, but I guess I'm really not."
    the_sister "It is sort of like finally figuring out an optical illusion. Things make more sense now when I think about the way she behaves."
    the_sister "Plus I'm a little flattered but at the same time embarrassed that she didn't think she could talk to me directly."
    mc.name "It can be a tough conversation to have, and I don't think she has really had it with too many people yet."
    the_sister "Oh god, do you think we are the only two people that know? Will it mess her up if I reject her?"
    mc.name "I don't know. Like I said, it is a delicate situation."
    the_sister "Yeah..."
    mc.name "Of course the real question is what you want to do. You can't guilt yourself into a relationship you don't want to make her happy."
    $ willing = lily_willing_threesome()
    if willing:
        the_sister "Well first things first, I obviously don't have a problem with being intimate with another girl."
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            the_sister "Even when you aren't around me and Mom have been getting pretty... involved."
    else:
        the_sister "I'm not opposed to the idea, I just kinda always pictured myself with a man."
    mc.name "Okay, that is one aspect of this taken care of, what about the relationship aspect?"
    the_sister "I don't know, I hadn't really thought of her in that way, and it's gonna take some time for me to process."
    mc.name "That's good, but she will want to know what I found out about your sexuality. What should I tell her?"
    if willing:
        the_sister "Go ahead and tell her I have some experience with women, but don't be too specific."
        mc.name "Obviously."
    else:
        the_sister "Tell her the truth, I've never been with a woman but I don't think I'd have a problem if we had a good connection."
        mc.name "Okay."
    the_sister "Does she know you were going to out her to me?"
    mc.name "No, and I feel terrible about that, but I didn't see a way to ask you without telling you why."
    the_sister "Yeah... maybe I can try and set her up with a boy and see how she reacts. Or maybe I could call a girl hot and see what she does... I'll figure something out."
    mc.name "Then what? If she confesses and asks you out are you going to say yes?"
    the_sister "I guess. I mean if it is just a date it won't be too different than hanging out with my friend."
    the_sister "What do you think I should do?"
    menu:
        "Go for it" if willing:
            $ the_person.event_triggers_dict["lily_truth"] = 3
            mc.name "My vote is definitely that you go for it. The two of you would be so hot together."
            the_sister "You know I'm not gonna let you watch right?"
            mc.name "Don't worry, I can imagine it just fine."
            mc.name "But seriously, I think she could make you happy. You are only young once, might as well take advantage of the opportunity while you have it."
        "Go for it \n Must have had a threesome (disabled)" if not willing:
            pass
        "Take it slow":
            $ the_person.event_triggers_dict["lily_truth"] = 1
            mc.name "You can always take things slow too, no need to rush right into sex."
            if not the_sister.has_taboo("vaginal_sex"):
                the_sister "Really? Promoting abstinence while you fuck your sister is a bit disingenuous."
                mc.name "Well everyone is different. You don't need to model your sex life after mine."
            elif not the_sister.has_taboo("sucking_cock") or not the_sister.has_taboo("anal_sex"):
                the_sister "Really? The restraint speech from you sounds a bit hypocritical."
                mc.name "Hey, I'm just saying it is an option."
            else:
                the_sister "Yeah, wouldn't want to do anything we regret."
                mc.name "Exactly."
        "Don't do it":
            $ the_person.event_triggers_dict["lily_truth"] = -1
            mc.name "It's not a good idea. If something goes wrong what are you going to do the rest of the semester?"
            the_sister "I guess you're right."
    if willing or (the_sister.sluttiness + 10*the_sister.opinion.getting_head) > 60:
        if the_person.event_triggers_dict.get("lily_truth", 0) > 1:
            the_sister "I guess you're right. I mean she is hot."
            the_sister "I'm kind of excited about next week now."
        elif the_person.event_triggers_dict.get("lily_truth", 0) > 0:
            the_sister "Right, no harm no foul. She is kinda hot."
            the_sister "Maybe I'll just make the first move and see what happens."
        else:
            the_sister "It's a shame, she is pretty hot."
            the_sister "I'll just wait for her to make the first move."
        $ the_person.event_triggers_dict["lily_truth"] += 1
    else:
        if the_person.event_triggers_dict.get("lily_truth", 0) > 0:
            the_sister "Sounds like a plan. I'll just wait for her to make the first move."
        else:
            the_sister "I'll just think of it as a compliment and try to move past this."
    mc.name "I think that whatever happens and whatever you ultimately decide she wants to keep your friendship strong."
    if the_person.event_triggers_dict.get("lily_truth", 0) > 0:
        the_sister "I know, and I do too, but if we could have something more that might be even better."
    else:
        the_sister "I know, I just hope she isn't too upset."
    $ scene_manager.clear_scene()
    return

label lily_second_best_friend(the_sister, the_person):
    the_person "So... did you talk to [the_sister.fname] about... things."
    "You did, but that doesn't mean you have to be honest about it. Plus you should be able to talk to [the_sister.possessive_title] again."
    if the_person.event_triggers_dict.get("lily_truth", 0) >= 3:
        "Last week you told [the_sister.title] to pursue [the_person.title]."
    elif the_person.event_triggers_dict.get("lily_truth", 0) >= 1:
        "Last week you told [the_sister.title] to accept a relationship with [the_person.title]."
    elif the_person.event_triggers_dict.get("lily_truth", 0) >= -1:
        "Last week you told [the_sister.title] to avoid a relationship with [the_person.title]."
    else:
        "You can't remember what you told [the_sister.title] last week, better just make something up for [the_person.title]."
    menu:
        "She is curious":
            mc.name "She is certainly curious. When I brought up the idea of her dating a girl she seemed intrigued."
            mc.name "If I had to guess she has thought about it before, but probably liked boys enough to go with the flow."
            mc.name "I think I could get her to ask you out if you give me a bit of time."
            $ the_person.event_triggers_dict["lily_lie"] = 2
        "Give her time":
            mc.name "She seemed a little surprised when I asked, sort of like she had never really thought about it before."
            mc.name "When we finished talking it seemed like she was deep in thought."
            mc.name "I think you need to give her some time, let her come around to the idea of seeing you as more than a friend."
            mc.name "I'll be sure to bring it up again, see if I can help nudge her in the right direction."
            $ the_person.event_triggers_dict["lily_lie"] = 1
        "Not going to happen":
            mc.name "She likes you, she really does, but nothing is going to happen."
            mc.name "I don't think she is ever going to return your feelings."
            mc.name "I'll talk to her again, but I think you might need to look elsewhere."
            $ the_person.event_triggers_dict["lily_lie"] = -1
    the_person "Well, that is good to know. At least I have some idea of what to expect."
    the_person "I guess no matter what I'm still gonna be hanging around. Maybe I'll be able to sway her a bit more while we are studying."
    mc.name "Sure, you never know what will happen."
    "You better make sure that your story checks out before [the_person.title] catches you in a lie."
    "Maybe your serums could help out. Can you convince [the_sister.title] that she wants to do what you already promised [the_person.title]?"
    the_person "Thanks again. I know this is kind of awkward and I really appreciate the help."
    if the_person.height < 0.9:
        "She steps forward goes up on her toes and kisses you on the cheek."
    else:
        "She steps forward and gives you a kiss on the cheek."
    $ lily_second_followup = Action("[the_sister.name] Second Followup", lily_mon_followup_requirement, "lily_second_followup_label")
    $ mc.business.add_mandatory_crisis(lily_second_followup)
    $ scene_manager.clear_scene()
    call advance_time from _call_advance_second_bf
    return

label lily_second_followup_label():
    $ scene_manager = Scene()
    $ the_person = get_lab_partner()
    $ the_sister = lily
    $ the_person.event_triggers_dict["friend_with_benefits"] = 2
    "As you are getting ready for bed you decide there is no time like the present and make your way to [the_sister.possessive_title]'s room."
    $ mc.location = lily_bedroom
    $ scene_manager.add_actor(the_sister, position = "sitting")
    the_sister "Hey there, [the_sister.mc_title]. Back again?"
    if cousin.location == lily_bedroom:
        $ cousin.change_location(downtown)
        mc.name "Hey, [the_sister.title], where is [cousin.fname]?"
        the_sister "Don't know, don't care. Just happy to have some alone time."
        mc.name "Oh, sorry, I can go."
        the_sister "No, wait! Did you want to talk?"
    mc.name "Yeah, I seems like [the_person.fname] chickened out."
    the_sister "Yeah... There were a few times where it seemed like she wanted to ask me something, but she kept changing the topic when I asked."
    mc.name "Have you thought anymore about what you want to do?"
    $ willing = lily_willing_threesome()
    if the_person.event_triggers_dict.get("lily_truth", 0) < 0 and willing:
        the_sister "Well since last week things have changed a bit."
        the_sister "I obviously don't have a problem with being intimate with another girl."
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            the_sister "Even when you aren't around me and mom have been getting pretty involved."
    else:
        the_sister "Nothing has really changed for me. Did you change your mind about what I should do?"
    menu:
        "Go for it" if willing:
            $ the_person.event_triggers_dict["lily_truth"] = 2
            mc.name "In light of recent developments I think you should go for it."
            the_sister "You know I'm not gonna let you watch right?"
            mc.name "Don't worry, I can imagine it just fine."
            mc.name "But seriously, I think she could make you happy. You are only young once, might as well take advantage of the opportunity while you have it."
        "Go for it \n Must have had a threesome (disabled)" if not willing:
            pass
        "Take it slow":
            $ the_person.event_triggers_dict["lily_truth"] = 1
            mc.name "I've been thinking about it and you should give her a chance."
            mc.name "You can always take things slow too, no need to rush right into sex."
            if not the_sister.has_taboo("vaginal_sex"):
                the_sister "Really? Promoting abstinence while you fuck your sister is a bit disingenuous."
                mc.name "Well everyone is different. You don't need to model your sex life after mine."
            elif not the_sister.has_taboo("sucking_cock") or not the_sister.has_taboo("anal_sex"):
                the_sister "Really? The restraint speech from you sounds a bit hypocritical."
                mc.name "Hey, I'm just saying it is an option."
            else:
                the_sister "Yeah, wouldn't want to do anything we regret."
                mc.name "Exactly."
        "Don't do it":
            $ the_person.event_triggers_dict["lily_truth"] = -1
            mc.name "It's still not a good idea. If something goes wrong what are you going to do the rest of the semester?"
            the_sister "I guess you're right."
    if willing or (the_sister.sluttiness + 10*the_sister.opinion.getting_head) > 60:
        if the_person.event_triggers_dict.get("lily_truth", 0) > 1:
            the_sister "I guess you're right. I mean she is hot."
            the_sister "I'm kind of excited about next week now."
        elif the_person.event_triggers_dict.get("lily_truth", 0) > 0:
            the_sister "Right, no harm no foul. She is kinda hot."
            the_sister "Maybe I'll just make the first move and see what happens."
        else:
            the_sister "It's a shame, she is pretty hot."
            the_sister "I'll just wait for her to make the first move."
        $ the_person.event_triggers_dict["lily_truth"] += 1
    else:
        if the_person.event_triggers_dict.get("lily_truth", 0) > 0:
            the_sister "Sounds like a plan. I'll just wait for her to make the first move."
        else:
            the_sister "I'll just think of it as a compliment and try to move past this."
    mc.name "I think that whatever happens and whatever you ultimately decide she wants to keep your friendship strong."
    if the_person.event_triggers_dict.get("lily_truth", 0) > 0:
        the_sister "I know, and I do too, but if we could have something more that might be even better."
    else:
        the_sister "I know, I just hope she isn't too upset."
    $ scene_manager.clear_scene()
    return

label lily_third_best_friend(the_sister, the_person):
    $ wait = False
    if the_person.event_triggers_dict.get("lily_truth", 0) > 2: # lily starts things
        "As it gets later and later it seems like [the_person.title] is not going to visit you today."
        "That makes sense, [the_sister.title] was pretty excited about initiating things after your talk last week."
        if the_person.event_triggers_dict.get("lily_lie", 0) < 1: # it is a surprise
            "[the_person.title] must have been incredibly surprised when she made the first move."
        else: # it is welcome
            "[the_person.title] must have been thrilled when she made the first move."
    elif the_person.event_triggers_dict.get("lily_lie", 0) <1: # wait for next week
        $ wait = True
        if the_person.event_triggers_dict.get("lily_lie", 0) <0: # doesn't want to be disappointed LOOP
            the_person "Hey, [the_person.mc_title]."
            mc.name "Hey, shouldn't you be talking with [the_sister.fname]?"
            the_person "I chickened out. I was hoping maybe you had talked with her again."
            the_person "If anything has changed in the last week it might give me the courage to talk to her."
            mc.name "As a matter of fact..."
        else: # first time answer
            the_person "Hey, [the_person.mc_title]. Sorry to sound like a broken record, but did you happen to talk to [the_sister.fname]?"
            mc.name "I did, we had a bit of a heart–to–heart, and she is a bit like you."
            mc.name "She is young and she isn't exactly sure what kind of relationships she will be okay with."
        "Now for the moment of truth. Your serums give you some control over [the_sister.possessive_title] so if you want to change her opinion you probably have that power."
        if the_person.event_triggers_dict.get("lily_truth", 0) < 0:
            "She is currently opposed to the idea, but you don't need to tell [the_person.title] that."
        else:
            "She would go along with it, but not too eagerly. That doesn't mean you have to tell [the_person.title] the truth."
        menu:
            "She loves you":
                $ the_person.event_triggers_dict["lily_lie"] = 2
                mc.name "Despite that I think she has a bit of a crush on you too."
                mc.name "When I brought up the idea of being with another girl she seemed to keep thinking of you as that girl."
                mc.name "So at the very least I can assure you she thinks you are hot. Combine that with your shared friendship and I think you'll be pleased with her response."
                the_person "Wow, that is great. I've got butterflies just thinking about this."
            "You have a shot":
                $ the_person.event_triggers_dict["lily_lie"] = 1
                mc.name "She is certainly curious. Maybe not as much as you are, but she definitely does not have a problem with the idea."
                mc.name "It seems like it hadn't really occurred to her before, but now that I brought up the idea she is open to something."
                mc.name "She might still be a bit shocked when you come out to her, but you have a real shot of getting her to go out with you."
                the_person "That's good to know, takes some of the pressure off to not be scared of her reaction."
            "It's hopeless":
                $ the_person.event_triggers_dict["lily_lie"] = -1
                mc.name "Despite that I think you are going to have trouble convincing her to go out with you."
                mc.name "She still has some pretty strongly ingrained beliefs of what an appropriate relationship looks like."
                mc.name "Secretly I think she is curious but the social stigma she associates with the idea is going to make it hard to actually act on that curiosity."
                the_person "That is disappointing. I still think I need to take my shot, even if it doesn't work out."
        the_person "Alright, now I just need to work up the courage to tell her how I feel."
        mc.name "Give me another week to talk with her. I might be able to improve your odds."
        the_person "Yeah, of course. It is too late now anyway. I really hope we don't have too much homework next week."
        "With the conversation set for next week you have another chance to try and change [the_sister.title]'s opinion."
    else: # person starts things
        "As it gets later and later it seems like [the_person.title] is not going to visit you today."
        if the_person.event_triggers_dict.get("lily_lie", 0) > 1:
            "That makes sense, you already told her [the_sister.title] would definitely be interested."
        else:
            "That makes sense, you already told her you thought [the_sister.title] would come around eventually."
        if the_person.event_triggers_dict.get("lily_truth", 0) > 0: # it is welcome
            "Fortunately for her, [the_sister.possessive_title] is going to eagerly accept."
        elif the_person.event_triggers_dict.get("lily_truth", 0) > -1: # it is acceptable
            "Luckily [the_sister.title] is not going to object too much to the idea."
        else: # it is not good
            "Unfortunately [the_sister.title] is going to reject her. [the_person.title] is going to be pissed."
            $ the_person.change_stats(happiness = -20, love = -20, obedience = -20)
            $ the_person.event_triggers_dict["anger"] = 2
    if wait:
        $ lily_second_followup = Action("[the_sister.name] Second Followup", lily_mon_followup_requirement, "lily_second_followup_label")
        $ mc.business.add_mandatory_crisis(lily_second_followup)
    else:
        "You'll have to check in with [the_sister.title] and see how things went."
        $ lily_third_followup = Action("[the_sister.name] Third Followup", lily_mon_followup_requirement, "lily_third_followup_label")
        $ mc.business.add_mandatory_crisis(lily_third_followup)
    $ scene_manager.clear_scene()
    call advance_time from _call_advance_third_bf
    return

label lily_third_followup_label():
    $ scene_manager = Scene()
    $ temp_recording = None
    $ the_person = get_lab_partner()
    $ the_sister = lily
    if the_person.event_triggers_dict.get("lily_truth", 0) > 2: # she started
        $ temp_recording = "[the_sister.title] Proposes"
        $ scene_manager.add_actor(the_sister, emotion = "happy")
        "As you are getting ready for bed you hear a rapid knock at your door before [the_sister.title] pushes it open and lets herself in."
        "She is smiling widely and practically bubbling over with excitement."
        the_sister "Oh my god! [the_sister.mc_title] me and [the_person.fname] are dating!"
        the_sister "We were studying and I basically propositioned her."
        $ scene_manager.update_actor(the_sister, position = "sitting")
        "She makes her way over to your bed and sits down next to you."
        if the_person.event_triggers_dict.get("lily_lie", 0) < 1: #surprise
            the_sister "At first she was a little surprised. Honestly I worried for a moment that you were lying to me about her feelings."
        else: # as expected
            the_sister "She was acting nervous all day and I figured I would just cut to the chase. She was so relieved and excited."
        the_sister "We had some work to do, but we are both eager to start spending more time together."
    elif the_person.event_triggers_dict.get("lily_truth", 0) > -1: # she accepted
        $ temp_recording = "Buddy Proposes"
        if the_person.event_triggers_dict.get("lily_truth", 0) > 0: # that is great
            $ scene_manager.update_actor(the_sister, emotion = "happy")
            "As you are getting ready for bed you hear a knock at your door before [the_sister.title] pushes it open and lets herself in."
            "She has a silly grin on her face. It is pretty clear something good happened tonight."
            the_sister "Hey [the_sister.mc_title], you'll never guess what happened today."
            "You grin back and put on a thoughtful expression."
            mc.name "You got a good score on a test?"
            the_sister "No, silly, [the_person.fname] worked up the courage to ask me out."
            mc.name "Really, what did you say?"
            the_sister "I said yes, just like you wanted. She was so relieved and excited."
        else: # you told her not to
            $ scene_manager.update_actor(the_sister, emotion = "sad")
            "As you are getting ready for bed you hear a hesitant knock at your door before [the_sister.title] pushes it open a crack."
            the_sister "Hey, [the_sister.mc_title] could I come in a talk to you?"
            mc.name "Yeah, sure. Is something wrong?"
            "She makes her way over to your bed and sits down next to you taking your hand in hers."
            $ scene_manager.update_actor(the_sister, position = "sitting", emotion = "sad")
            the_sister "Kind of, [the_person.fname] asked me out tonight. I know you said I should turn her down, but she looked so..."
            the_sister "I don't know exactly. It was like she was hanging all of her hopes on my answer."
            the_sister "I just couldn't say no to that face. I want to explore a relationship with her."
            if the_sister.obedience > 180:
                menu:
                    "Be understanding":
                        pass
                    "Break them up":
                        mc.name "[the_sister.title] that is completely unacceptable. I told you what to do."
                        mc.name "Now you are going to have to break up with her."
                        the_sister "What? No I couldn't... it will break her heart."
                        mc.name "I'll take some of the blame, I should have been more clear the first time. This is not a request it is an order."
                        mc.name "You WILL do this."
                        $ the_sister.change_stats(happiness = -20, love = -20, obedience = 20)
                        the_sister "Yes, sorry I will."
                        mc.name "What was that?"
                        the_sister "Yes Master. I live to serve you."
                        if the_person.obedience > 180:
                            $ the_person.change_stats(happiness = -20, love = -20, obedience = 20)
                        else:
                            $ the_person.change_stats(happiness = -20, love = -20, obedience = -20)
                        $ the_person.event_triggers_dict["anger"] = 2
                        "That was harder than it should have been. Now you are going to have to deal with [the_person.title] too."
                        $ scene_manager.clear_scene()
                        if temp_recording not in mc.business.event_triggers_dict.get("study_recordings", []):
                            $ mc.business.event_triggers_dict["study_recordings"].append(temp_recording)
                        # Scene where you the_person comes to you after the_sister breaks up with her. New study buddy
                        return
            mc.name "That's okay. I understand."
            mc.name "I should have expected this. You've been so adventurous I really can't fault you for wanting to experiment more."
            mc.name "After all, I am the one who has pushed you to keep going further."
            if the_sister.obedience > 180:
                the_sister "I'll try to be better Master. I want to serve you and make you happy."
                $ the_sister.change_stats(happiness = 10, love = 10, obedience = 20)
            else:
                the_sister "I'm sorry I let you down, thank you for understanding."
                $ the_sister.change_stats(happiness = 10, love = 10, obedience = -10)
            mc.name "What are you plans now?"
    else: # she rejected
        $ temp_recording = "[the_sister.title] Rejects"
        "As you are getting ready for bed your door suddenly slams open and an angry looking [the_sister.fname] storms in."
        $ scene_manager.update_actor(the_sister, emotion = "angry")
        the_sister "What the FUCK!?! Did you tell [the_person.fname] that I would go out with her?"
        the_sister "What were you thinking? You told me to turn her down and then sent her in there to get rejected."
        the_sister "She was so confident she just blurted it out and I had to tell her no. The look on her face broke my heart, it was like she couldn't even understand what I was saying."
        the_sister "Fuck, you are such an asshole [mc.name]."
        $ scene_manager.update_actor(the_sister, position = "walking_away")
        $ the_sister.change_stats(happiness = -20, love = -20, obedience = -20)
        "With that she spins and walks out, leaving your door standing open."
        $ scene_manager.clear_scene()
        "Maybe that was a mistake..."
        #mom comes to check on you maybe
        if not mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"] = []
        if "1. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("1. Friend Recording")
        if "2. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append("2. Friend Recording")
        if temp_recording not in mc.business.event_triggers_dict.get("study_recordings", []):
            $ mc.business.event_triggers_dict["study_recordings"].append(temp_recording)
        return
    the_sister "We are going to start doing our classwork on campus between classes so that we can come back here on Monday night."
    the_sister "She hasn't told her parents yet, and I don't really want mom to know so soon."
    if mc.business.event_triggers_dict.get("family_threesome", False) == True:
        the_sister "I don't think she would be jealous, but still better safe than sorry."
    elif lily.event_triggers_dict.get("vaginal_revisit_complete", False) or the_sister.is_girlfriend:
        the_sister "After all it isn't like I'm a lesbian. We are just fooling around a bit."
    else:
        the_sister "I'm not really sure how I would explain it. I'm not even sure how much I'm going to like girls."
    the_sister "We also might try to meet up on some other days, but that will depend on how our schedules work out."
    mc.name "Don't worry, your secret is safe with me. I am excellent at keeping secrets."
    the_sister "Thanks, I knew I could count on you."
    if the_sister.is_girlfriend:
        the_sister "This doesn't have to change anything between us."
        the_sister "Our relationship is still my highest priority, but I'm looking forward to exploring something with her too."
    elif the_sister.has_role(slave_role):
        the_sister "Of course you can still use me anytime you need."
        the_sister "I'll always be here for you [the_sister.mc_title], and maybe someday I can get her to be here for you too."
    elif lily.event_triggers_dict.get("vaginal_revisit_complete", False):
        the_sister "Don't worry you will still get to fuck me when you want."
        the_sister "I don't think I could give up real hot dick for her. Maybe I can even convince her to join us."
    elif lily.event_triggers_dict.get("anal_revisit_complete", False):
        the_sister "Don't worry, I'll still let you use my ass for relief."
        the_sister "We just have to be careful so she doesn't taste your cum if she eats me out."
    elif lily.event_triggers_dict.get("oral_revisit_complete", False):
        the_sister "I can still service you from time to time if you want."
        the_sister "But you better return the favour, [the_person.fname] might be better than you."
    else:
        the_sister "I'm sure you'll find someone too, maybe one of the girls at your office?"
    $ scene_manager.clear_scene()
    if not mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"] = []
    if "1. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"].append("1. Friend Recording")
    if "2. Friend Recording" not in mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"].append("2. Friend Recording")
    if temp_recording not in mc.business.event_triggers_dict.get("study_recordings", []):
        $ mc.business.event_triggers_dict["study_recordings"].append(temp_recording)
    # mention that mc can watch the video
    # figure out how to reduce duplication in this label
    $ lily_buddy_date = Action("Lesbian Date", lily_buddy_date_requirement, "lily_buddy_date_label", requirement_args=day)
    $ mc.business.add_mandatory_crisis(lily_buddy_date)
    $ buddy_thanks = Action("Buddy Thanks", buddy_followup_requirement, "buddy_thanks_label")
    $ the_person.add_unique_on_talk_event(buddy_thanks)
    $ scene_manager.clear_scene()
    return

label buddy_thanks_label(the_person):
    $ scene_manager = Scene()
    $ temp_recording = None
    $ the_sister = lily
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "As you wander across campus you spot [the_person.title]."
    "When she sees you, her face lights up, looking excited but then nervous."
    "Once you get close enough she seems almost bashful." 
    the_person "Hey, [the_person.mc_title]."
    mc.name "Hi [the_person.title], what's new?"
    "She takes a deep breath, her eyes shining with excitement."
    the_person "So... [the_sister.fname] said yes."
    mc.name "Really? That's great news! I'm so happy for both of you."
    the_person "Thank you, you were always there for me when things got tough. And now..."
    "Her voice breaks slightly as she trails off into silence."
    "You wrap an arm around her, and feel the tension in her shoulders."
    mc.name "It was never about anything more than wanting to see you happy, [the_person.title]. You deserve it."
    "Your words are soft and comforting, filling the space between the two of you with warmth."
    the_person "You've been so incredible. I'm so glad that I met you and [the_sister.fname]."
    mc.name "Me too."
    "You pause for a moment, letting her relax a bit more"
    mc.name "Does this mean I won't be seeing you anymore on Mondays?"
    the_person "Probably not, I think I'm gonna mostly be in [the_sister.fname]'s room. But I'll be around, maybe even more often than before."
    $ the_person.change_stats(happiness = 10, love = 2, obedience = 10)
    "The two of you make a bit of small talk, before she has to move on for her next class."
    $ scene_manager.clear_scene()
    return
