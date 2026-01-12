# In Kaya's lust events, we discover she has some type of post nut clarity, similar to MC, and we begin to exploit it.
# This knowledge then leads to multiple side stories as well as her teamups.
# At 20, she reports to MC really struggling with her master's program, asking MC for a chance to 'blow off steam'
# At 40, we celebrate her 21st birthday with a date at the bar, where MC takes her back to his place.
# at 60, MC gets the birth control talk, and Kaya asks for sex. IF not love 60, she demands to be on top so she can pull off.
# at 80...?

label kaya_study_struggle_label(the_person):
    $ the_person = kaya
    $ the_person.arousal = 50
    "You get a text message on your phone. It is from [the_person.possessive_title]."
    $ mc.start_text_convo(kaya)
    the_person "Hey, are you busy right now?"
    mc.name "Not really. Need something?"
    the_person "Feel like swinging by the university? I need a hand."
    the_person "I'm having an issue with one of my classes and I think you could help me with it."
    mc.name "Sure, I could swing by."
    the_person "Okay! I'm in a study room, here's the number..."
    $ mc.end_text_convo()
    "Hmm, this is definitely a strange request from [kaya.possessive_title]. You don't think she would be the type to need help studying."
    "Regardless, you make your way over to the university, and then to the study hall. You find the appropriate room and knock on the door."
    $ mc.change_location(university_study_room)
    $ the_person.draw_person()
    "[the_person.possessive_title!c] opens the door and lets you in. After you step inside, she closes the door and then stands with her back up against it."
    "You look at her and notice she is locking the door behind her."
    mc.name "Hey... you okay?"
    the_person "Yes!... no... I don't know!"
    the_person "This class is easy... but... I feel like I just can't concentrate!"
    the_person "My grades have been middling... but I know I can do better."
    mc.name "So you need some help studying?"
    the_person "No, I can study fine on my own. I study better alone actually."
    mc.name "Okay, so... what can I help you with?"
    the_person "I mean, it's your fault, really."
    the_person "The other night when you walked me home, you know, and we started kissing, and then you grabbed my ass..."
    the_person "I'm trying to study but I can't get it out of my head!"
    $ mc.change_locked_clarity(20)
    mc.name "Are you saying I... shouldn't have grabbed your ass?"
    the_person "I'm saying... you shouldn't start stuff you can't finish!"
    mc.name "Wait... you moved my hand off when I did it last time."
    the_person "Because I knew my mom would probably be snooping, I didn't want... hey!"
    "You get close to her, then pull her close, reaching behind her and grabbing her ass."
    $ the_person.change_arousal(5)
    $ the_person.draw_person(position = "kissing")
    mc.name "Don't worry, I won't leave you hanging this time."
    the_person "Hmm, I think I believe you... but I'm not taking any chances this time!"
    the_person "Lay down on the desk!"
    "Her commanding demeanour kind of throws you off for a moment. You decide to go with it for now, to see what happens."
    $ the_person.draw_person(position = "stand2")
    mc.name "Want me to take my clothes off?"
    the_person "No, I'm sorry to say, your clothes stay on, for now anyway..."
    $ the_person.draw_person(position = "cowgirl")
    if the_person.outfit.has_skirt:   #School uniform? I think she'll be in one... they are all skirts? Maybe not forever though. Check this just in case.
        "[the_person.possessive_title!c] gets on top of you. She pulls her skirt out from under her and lowers herself down, grinding her crotch against yours."
    else:
        "[the_person.possessive_title!c] gets on top of you, grinding her crotch against yours."
    call get_fucked(the_person, private= True, start_position = drysex_cowgirl, start_object = make_desk(), skip_intro = True, allow_continue = False) from _call_get_kaya_drysex_01
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0 and the_report.get("girl orgasms", 0) >0:
        the_person "Mmm, thank goodness, I really needed that..."
        "As she starts to get up, she notices a stain on the front of your pants."
        the_person "Wow... I can't believe you finished too..."
    elif the_report.get("girl orgasms", 0) > 0:
        the_person "Mmm, thank goodness, I really needed that..."


    $ kaya.progress.lust_step = 1
    $ add_kaya_birthday_night_out_action()
    return

label kaya_birthday_night_out_label():
    $ the_person = kaya
    "Your phone buzzes. It is from [the_person.possessive_title]."
    $ mc.start_text_convo(kaya)
    the_person "Hey. Busy tonight?"
    mc.name "Not really, you?"
    the_person "I want to go out tonight! Meet me at the coffee shop?"
    mc.name "Sounds good. I'll swing by."
    $ mc.end_text_convo()

    $ mc.change_location(coffee_shop)
    $ the_person.draw_person()
    "You swing by the coffee shop. [the_person.title] is behind the counter. She spots you when you walk in."
    the_person "Hey! I'm just closing up! I'll be right out. Can you lock the front door and flip the sign?"
    mc.name "Yeah sure."
    $ clear_scene()
    "You step over to the door and turn the lock, then flip the sign over to closed."
    "You wait for a few minutes, but eventually [the_person.title] emerges from the back room."

    $ the_person.apply_outfit(the_person.decide_on_outfit())
    $ the_person.draw_person()
    the_person "Alright! Let's go!"

    $ mc.change_location(downtown)
    "You step out into the night with [the_person.possessive_title]."
    mc.name "So... we off to play some billiards tonight? Or is there something else you wanted to do?"
    the_person "Well, something like that, yeah. I thought maybe we could combine two activities."
    the_person "I know this was kind of last second, I was going to go out with my mom to celebrate, but she texted me earlier and isn't feeling well."
    the_person "I don't really have many friends yet, but I don't want to go out by myself."
    the_person "Today is my birthday!"
    $ the_person.age = 21
    mc.name "Oh wow! Happy birthday! I... I didn't get you anything!"
    the_person "Good! There was no way for you to know, so that would have been a little creepy!"
    if the_person.knows_pregnant:
        "Provide an alternate here for pregnant [the_person.title]. Maybe just a regular date? Movies?"
    the_person "Anyway, I thought we could go get wasted. As long as you promise to make sure I get home okay!"
    mc.name "Ahhh, so I'm here to buy the drinks."
    the_person "Well... yeah? That sounds horrible when you say it out loud doesn't it?"
    "She stops walking and looks at you."
    the_person "I'm sorry... I didn't even think about it that way... we could do something else?"
    mc.name "I'm teasing you. I'm pretty sure I asked you to drinks when we first met, anyway. Didn't you take a rain check on that?"
    $ the_person.change_obedience(1)
    "She sighs, but starts to walk again."
    the_person "You're right. There was something about that wasn't there? When I won the game of pool?"
    mc.name "Umm I believe I won that game."
    the_person "Yeah right! I think I would remember that!"
    "You keep walking to the bar, trading jokes as you go. Soon you step in the front door."

    $ mc.change_location(downtown_bar)
    "You and [the_person.possessive_title] step up to the bar. The bartender seems to recognize you."
    "???" "Ah, you two again. A coke and a sprite?"
    the_person "Not tonight my good man. I'll have a cosmopolitan and I'll have it on this sucker's tab."
    "She points at you. The bartender looks at you for a moment and you nod back."
    "???" "Right, I'll need to see some..."
    "[the_person.title] whips out her photo ID, clearly she was ready for this."
    the_person "Here's where it has my birthday, right... here..."
    "???" "Ahh, I see. Well happy birthday to you there, Miss [the_person.last_name]."
    mc.name "I'll have a Woodford Reserve, neat."
    "You hand the bartender the company card, and he turns to get the drinks."
    mc.name "A cosmopolitan? Really? THAT'S your first drink?"
    the_person "What? I did a bunch of research, it is one of the most popular drinks for women..."
    mc.name "It's a fruity cocktail designed for women who want to stand around being social with a pink drink in their hand."
    mc.name "Not for someone on their 21st birthday trying to... how did you put it? Get WASTED?"
    "She rolls her eyes."
    the_person "Fine, Mr EXPERT. I'll let you order me something next."
    mc.name "Deal."
    "The bartender returns with your drinks."
    mc.name "Alright. Pool?"
    the_person "Maybe later, let's just grab a table for now."
    "You spot a booth tucked away to the side. You sit down across from [the_person.title]."
    $ the_person.draw_person(position = "sitting")
    the_person "Alright! Here goes..."
    "She takes a quick sip from her drink."
    the_person "Ahhh... hmmm..."
    "Her face turns into a bit of a grimace."
    the_person "That's... a drink... wow..."
    mc.name "Your face tells me everything I need to know."
    the_person "Oh whatever. This is great, I love it..."
    "She takes another sip and grimaces again."
    the_person "Ah who am I kidding. This is awful. Can't believe I picked this for my first alcoholic drink."
    mc.name "Wait... you've NEVER had alcohol?"
    the_person "No? I mean, I just hit 21, how was I supposed to..."
    mc.name "You never had a friend buy you some? Or use a fake ID?"
    the_person "I think you overestimate my social life."
    "She gives a long sigh."
    the_person "I'm guessing you've already figured most of that out... I've never even met my dad, and with mom getting sicker..."
    the_person "Let's just say that I'm content to spend as much time as possible with her, while I still can."
    mc.name "I understand. If there is anything I can do to help, let me know."
    "[the_person.possessive_title!c] finishes her drink, then looks at you."
    the_person "Well, you could help me with this empty glass!"
    the_person "If you're so smart, why don't you go order me something yourself?"
    mc.name "Of course, I'd be glad to."
    "You get up and step away from the table going back to the bartender."
    "You explain to him that she wants to try a variety of drinks, and ask that he get creative and bring out several for her to try."
    "You come back to the table and sit down."
    the_person "Welcome back... did you forget something?"
    mc.name "No, of course not. The bartender will be back soon, I asked him to make you a variety of things."
    the_person "Oh?"
    "After a minute, the bartender comes back with 6 different cocktails."
    "???" "Alright, I have a Zombie, a Margarita, a Gin And Tonic, a Black Manhattan, a Harvey Wallbanger, and a Long Island."
    the_person "Geeze! [the_person.mc_title], I can't drink all of this! You really ARE trying to get me wasted, aren't you?"
    mc.name "I don't mean for you to drink the whole thing, just try a sip or two of each."
    the_person "Yeah but... that would be a big waste of the other drinks..."
    mc.name "Don't worry about it. I'm sure between the two of us we'll be able to finish them all off."
    the_person "Hhmm... Alright sir. You've convinced me. Here we go."
    "She picks up the first one."
    the_person "What is this one?"
    mc.name "Looks like the Margarita."
    "She takes a sip, then smacks her lips."
    the_person "Hmm... not bad... I kinda like it."
    "You keep chatting with [the_person.title], making small talk as she works her way through a few of the drinks."
    "She takes a sip of one, then suddenly stops."
    the_person "Oh my god, this one! What is this? It's amazing!"
    mc.name "Ummm, that looks like the black Manhattan. It's a bourbon drink but it has a couple twists to a classic recipe."
    the_person "This one is mine! I kinda like the wallbanger thing too."
    mc.name "Sounds good. I'll take the Long Island and the gin and tonic for now."
    the_person "Yeah I didn't really care for those."
    "You and [the_person.title] sit and enjoy your drinks together for a bit. Eventually, the topic turns to dating history."
    the_person "So, I'm guessing you've been with like... a LOT of girls?"
    mc.name "Oh, yeah I've been with a few. Not a huge number, but I've been able to be successful in my love life."
    the_person "Yeah, I'm sure. What's the deal with you and Professor [nora.fname] anyway? The way she acts around you, I can tell you two have a history."
    mc.name "That is a bit complicated. I know her from my time at the university as well..."
    the_person "And you two hooked up? I can hardly imagine it, but from the way she talks about you..."
    mc.name "She talks about me?"
    the_person "I mean... yeah? Once in a while anyway? Sometimes it is like... she starts to talk about something involving you... then she will just stop and look out into space..."
    the_person "But you didn't answer!  Have you two hooked up before?"
    mc.name "Umm, well basically yeah."
    the_person "I knew it! God! Suddenly a lot of things make so much more sense."
    mc.name "What about you? I'm sure you've had boyfriends before?"
    the_person "Me? Oh... I mean yeah of course! I've totally dated a few guys before..."
    mc.name "Yeah? I wasn't sure. It seems like you've had a bit of a rough road."
    the_person "Yeah... I guess... I've dated a few guys but it just seems like they always get flaky after a couple months."
    the_person "I think my heritage and my family life can kind of put people off a bit."
    the_person "So... I guess I've never really gotten serious with anyone."
    mc.name "Ah, I understand."
    "The small talk continues, and a couple more rounds are ordered as well."
    "Soon you are both slurring your speech and laughing more than you should."
    the_person "Oh, hang on a sec, that's my phone."
    "[the_person.possessive_title!c] looks at her phone."
    the_person "Oh SHIT. I forgot to tell my mom I was gonna go out tonight. One second..."
    "She sends a flurry of text messages. Her phone vibrates a few times with responses."
    mc.name "Everything okay?"
    the_person "Yeah. She was just getting worried. I told her what I was up to and she just reminded me it was getting late but to have a good time and to let her know if I'm not gonna make it home..."
    the_person "That's funny, why wouldn't I make it home? I always make it home..."
    mc.name "Did you tell her you were with me?"
    the_person "Yeah, I did, what does that.... OOOOOHHHHHHHHHHHHHH!!!!!"
    "She looks horrified for a moment. Then smiles."
    the_person "Well... I guess she must like you alright, if she's giving me permission to crash at your place!"
    the_person "But... it IS getting late. I wouldn't mind crashing at your place sometime... but tonight I want to go home."
    mc.name "That seems perfectly reasonable. Can I walk you there?"
    the_person "Of course!"
    "You get up and settle your tab with the bartender, and then head toward the front door."

    $ mc.business.change_funds(-150, stat = "Food and Drinks")
    $ the_person.add_situational_slut("drunk", 10, "She's very drunk")
    $ mc.change_location(downtown)
    $ the_person.draw_person(emotion = "happy")
    "You step out from the bar. You give [the_person.title] a hand, since she is very drunk."
    the_person "Why thanks you sir!"
    "Her slurred speech is a bit concerning, but she seems to be doing okay for now."
    "You begin walking her home. About halfway there, she stops you next to an alley."
    the_person "Hang on, I want to do one more thing on my birthday..!"
    "She starts to pull you down the alley with a smile on her face."
    mc.name "You sure you feel up to this?"
    the_person "Of course, I've been wanting to do this since way before tonight!"
    "She pulls you farther down the alley until you are well out of sight from the main road."
    "She suddenly turns and pulls you into a kiss."
    $ the_person.draw_person(position = "kissing")
    "Your hands drop to [the_person.possessive_title]'s hips. Her lips meet yours and her mouth opens, her tongue darting out to meet yours."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(50)
    "You spend several seconds making out with [the_person.title], then she pulls her head back."

    # Check here, if we have already had sex in the love path, give players the options to fuck her agains the wall or something.
    the_person "You know, I usually don't like to do this, but for some reason I can't stop thinking about it with you..."
    mc.name "Doing... what?"
    $ the_person.draw_person(position = "blowjob")
    $ the_person.discover_opinion("giving blowjobs")
    "As she gets down on her knees, her intentions suddenly become much clearer."
    mc.name "[the_person.title], you don't have to..."
    the_person "Shut up. I want to!"
    "She reaches forward and starts to stroke your cock through your pants."
    the_person "Mmm... can you take it out for me?"
    "You quickly reach down, unzip your pants and pull it out for her."
    the_person "Oh my god... you're huge, you know that right?"
    mc.name "If you're having second thoughts..."
    the_person "Oh for fuck's sake."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "[the_person.possessive_title!c] opens her mouth and the tip slides into her warm, wet mouth."
    $ mc.change_arousal(15) #15
    $ the_person.change_arousal(5)
    "Her tongue twirls multiple times around the tip, and then her mouth slides farther down, taking a couple {height_system} of your length."
    the_person "Mmmmffff..."
    "[the_person.title] skillfully bobs her head up and down, her wonderful lips gliding across your skin."
    $ mc.change_arousal(15) #30
    $ the_person.change_arousal(5)
    mc.name "For someone who doesn't like to give blowjobs, you sure are good at it."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    "She pops off for a second."
    the_person "Well yeah? If you want to get it over as quick as possible, give better head."
    "She goes down and runs her tongue along the entire length of your shaft a couple of times."
    the_person "YOU though... I kind of want to take my time..."
    "It feels amazing. You are more than happy to let her."
    $ mc.change_arousal(20) #50
    $ the_person.change_arousal(5)
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "[the_person.possessive_title!c] opens her mouth and takes your cock in her mouth again. You put your hand on the back of her head."
    "She uses her hand to stroke the portion she can't get into her mouth. Despite claiming to want to take her time, her eager mouth is pushing your arousal fast."
    $ mc.change_arousal(20) #70
    mc.name "Oh fuck, who knew you were such a talented cocksucker. This won't be the last time you get on your knees."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    $ the_person.change_slut(1, 50)
    $ the_person.change_arousal(5)
    "Her lips smack as she pops off again."
    the_person "Coming from anyone else, I'd probably roll my eyes... and maybe it is just the alcohol talking, but this is so hot..."
    "She runs her tongue along the shaft a few more times."
    the_person "It tastes so hot and virile... I can't help but imagine putting this somewhere else..."
    mc.name "Why don't you stand up and we can make that happen."
    "She gives your dick a couple strokes with her hand. She looks at it, then back up at you."
    the_person "That is tempting... but not like this, while I'm drunk and in an alley..."
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "[the_person.title] opens her mouth and the tip of your erection slides into her heavenly mouth again."
    $ mc.change_arousal(20) #90
    $ the_person.change_arousal(5)
    "Soft moans and hums accompany each stroke as she eagerly sucks you off."
    "The sexy sounds of her mouth engulfing your cock are driving you over the edge. Your climax is rapidly approaching."
    $ mc.change_arousal(20) #110
    mc.name "[the_person.title]... I'm gonna cum!"
    "[the_person.possessive_title!c] looks up at you and for a moment you see her panic, as she realises what is about to happen."
    "She quickly closes her eyes and pumps your cock with her hand rapidly, leaving just the tip inside her lips."
    "[the_person.possessive_title!c] keeps going when you shoot your first blast of hot cum across the back of her throat."
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
    $ the_person.cum_in_mouth()
    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
    "You give [the_person.title] several spurts of cum as you orgasm, filling up her slutty little mouth with your seed."
    "A little bit escapes and dribbles down the side of her mouth."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    "When you finish, she pulls off and looks up at you, showing you your load with her mouth open for a second."

    #TODO if we've already changed her cum tastes, change up this dialogue a bit.
    "She closes her mouth, and with a big gulp, she swallows it down, then noticeably grimaces."
    the_person "Ugh... That was fun... but that was definitely my least favourite drink of the night."
    mc.name "I mean... you could always spit it out if you want to."
    the_person "I thought guys always like... expected girls to swallow?"
    mc.name "It's really hot, I'm not gonna lie. But that doesn't mean you have to."
    the_person "I guess if I'm going through the trouble of a blowjob, might as well go all out."
    "[the_person.possessive_title!c] takes a few moments to lick the tip of your cock again, cleaning up any cum still left on it."
    $ the_person.draw_person(position = the_person.idle_pose)
    "She stands up. The cum still dribbling down her chin makes your cock stir for a moment."
    if the_person.opinion.giving_blowjobs < 1:
        mc.name "Wow... so when are we doing that again? That was amazing."
        the_person "Honestly, I never used to like doing that... but that was actually really fun."
        the_person "I don't know when we'll have another opportunity, but if we have any alone time, I wouldn't mind doing that again!"
        $ the_person.update_opinion_with_score("giving blowjobs", 1)
        $ the_person.discover_opinion("giving blowjobs")
    mc.name "Hey, you got a little something there..."
    the_person "Oh?"
    "She pulls a tissue from her purse, wiping off her face."
    $ the_person.outfit.remove_all_cum()
    $ the_person.draw_person()
    the_person "Did I get it?"
    mc.name "Yeah... yeah I think so."
    the_person "Alright... I'd better get home..."
    "You and [the_person.possessive_title] leave the alley and resume walking to her apartment building."
    "Once at the main entrance, she turns to you."
    the_person "I'll make it from here. I don't want mom to catch us again..."
    mc.name "Hmm, okay. Well I hope you had a wonderful birthday."
    the_person "Oh geeze! I had almost forgotten about that! Thank you. You helped make it very special."
    the_person "I'm still excited to try all kinds of new drinks, but everytime I have a Black Manhattan, I'll remember tonight!"
    mc.name "I'll see you soon. Good night."
    the_person "Goodnight!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks into her apartment building."
    $ clear_scene()
    "When the doors close, you turn and start to walk away."
    "You've introduced [the_person.title] to alcohol, and also learned that she is an incredibly talented cock sucker."
    "Unfortunately, her mom's condition sounds bad. You aren't sure if you'll be able to do anything for her, but at least you can be there for [the_person.title] as things progress."
    "You step away from her apartment building, thinking about where things are likely to go with her."
    $ the_person.clear_situational_slut("drunk")
    $ kaya.progress.lust_step = 2
    $ the_person.event_triggers_dict["drink"] = True

    $ add_kaya_booty_call_action()  #Condom talk is linked in character creation, no need to link that here.
    return

label kaya_booty_call_label():  #60
    #In this label, we take kaya virginity if she still has it, and then have an all night fuck fest.
    #Kitchen sex gets caught on the charging doorbell camera and Sakari sees it all.
    # positions are missionary in bedroom, standing doggy in kitchen, then prone in the bedroom.
    # MC wakes up to panicking Kaya who slept in, 'Mom is coming home right now! Get out!'
    # Mc passes Sakari in the lift. Sakari says she isn't surprised to see you. Alludes to knowing you had sex in the kitchen last night
    $ the_person = kaya
    $ first_time = the_person.has_taboo("vaginal_sex")   #She is still a virgin
    "You get a text on your phone. It appears to be from [the_person.possessive_title]."
    $ mc.start_text_convo(kaya)
    the_person "Hey. WYD tonight?"
    mc.name "Not much, you?"
    the_person "Nothing. You should come over ;)"
    mc.name "Sure. Do I get to meet your mom officially?"
    the_person "My mom is doing a sleep study. She won't be back until the morning :)"
    "Oh shit this is a booty call!... or... text?"
    mc.name "I'll be right there."
    the_person "Bring a toothbrush ;)"
    $ mc.end_text_convo()
    "You immediately drop what you are doing and set out for [the_person.title]'s place."
    call perk_time_of_need_story_label() from _time_of_need_kaya_booty_call_lust_60
    $ mc.change_location(the_person.home)
    "Soon, you find yourself knocking on [the_person.title]'s front door. You notice that the doorbell camera isn't there..."
    $ the_person.draw_person()
    the_person "Ah! You really came! Come in come in!"
    "You step inside."
    mc.name "What happened to the doorbell camera?"
    the_person "I told mom it needed charging. She's not very good with electronic stuff, so I've got it charging up over in the kitchen."
    mc.name "Alright. So, what upstanding, wholesome activities do we have planned for this evening?"
    if the_person.progress.love_step >= 7:  #Fucked her at the office already and she's down for pies
        "She laughs."
        the_person "Babe, if you think anything wholesome is happening this evening, you clearly don't know me as well as I thought you did!"
    else:
        "She laughs."
        the_person "Well, I suppose at some point one of us may be 'upstanding' tonight, but wholesome isn't really the word I would use to describe it!"
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and walks through a door into what you assume is her room."
    $ the_person.change_to_bedroom()
    $ the_person.draw_person(position = "stand2")
    if the_person.progress.love_step >= 7:
        the_person "I've been waiting for an opportunity like this ever since the other night at the office... damn that was hot!"
    elif the_person.has_taboo("vaginal_sex"):   #She is still a virgin
        the_person "Alright so... you remember the conversation we had the other day at the coffeeshop, right?"
        mc.name "Of course."
        the_person "Good..."
        if the_person.is_highly_fertile:
            the_person "I'll just say... now would probably be a BAD time to cum inside me... unless you're looking to have kids."
            mc.name "Got it. So no creampies."
            if the_person.wants_creampie:
                the_person "I mean... I'm sure one wouldn't hurt anything..."
                the_person "But you should be aware of the risk ahead of time!"
            else:
                the_person "I would certainly appreciate that, if you can manage!"

        else:
            the_person "Honestly, I'm kind of in a low point in my cycle right now though so..."
            if the_person.wants_creampie:
                the_person "If you want to cum inside me... it would be a risk, but I think it would be an acceptable one."
            else:
                the_person "I would prefer that you pullout, but if you can't manage, it will probably be okay."
        mc.name "Understood."
        the_person "And go slow! This... this is my first time."
        mc.name "Don't worry, I'll make sure to take care of you."
    else:
        the_person "It has been so hard to find time for sex, it is so nice to have the place all to ourselves all night!"
        the_person "We can take our time instead of it being this crazy intense race!"
        mc.name "Mmm, that does sound nice."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] starts to strip down. You do the same."
    $ the_person.strip_full_outfit(position = "stand3")
    "With her perky tits out, you quickly kiss down the side of her neck and to her chest. You lick and suckle on one nipple while you grope her other tit with your hands."
    the_person "{=kaya_lang}He pai te ahua{/=kaya_lang}."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(40)
    "You can't tell what she is saying, but you can tell from her moans she is enjoying your attention."
    "While you lick at her nipple, your hands drop to her ass, which you grope eagerly."
    "You pick up [the_person.title] and throw her on the bed."
    the_person "{=kaya_lang}Hika!{/=kaya_lang}"
    $ the_person.draw_person(position = "missionary")
    if the_person.has_taboo("vaginal_sex"):
        the_person "I said be gentle, you caveman!"
        "You jump on top of her."
        mc.name "You woman. Me man!"
        "She chuckles as you start to kiss the side of her neck."
        the_person "I knew you were just a savage brute!"
        "She moans as you kiss your way down to her chest. She seems to really like it when you suck on her nipples."
        $ the_person.change_arousal(20)
        the_person "Mmm, [the_person.mc_title]... I'm ready..."
        mc.name "Are you sure?"
        the_person "Yes."
        mc.name "Okay."
        "Moving back up her body, you reach down and guide your cock up and down her slit, getting it good and wet."
        "Then you stop, pointing it straight into her virgin hole."
        "With a gentle push, the head of your cock sinks just into her opening. Just inside, your penetration stops at her hymen."
        mc.name "Alright... here we go."
        "Using your body weight, you let yourself sink farther inside of her. Her virginity tears, and you push deeper inside of her."
        $ take_virginity(the_person)
        $ the_person.draw_person(position = "missionary")
        the_person "Ahhh fffuuuuck... God you're so big [the_person.mc_title]... Ahhh..."
        "She groans in a mixture of pleasure and pain as she gets penetrated for the first time."
        "You take your time, slowly pushing more and more inside of her."
        "You push the rest of the way in, at long last, your bare cock deep inside of [the_person.possessive_title]."
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True, condition = make_condition_taking_virginity()) from _call_fuck_person_kaya_lust_first_time_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0 and the_report.get("girl orgasms", 0) >0:
            "[the_person.possessive_title!c] just lays on the bed, her face looks dazed."
            the_person "Oh my god... and it only gets better?"
            the_person "That was amazing..."
        else:
            the_person "Mmm, that was fun. And it only gets better?"
            the_person "I can't wait to go again!"
    else:
        "You jump on top of her."
        "She sighs as you start to kiss the side of her neck."
        the_person "Oh god you are so warm... I love it when we get naked and you get on top of my like this..."
        "She moans as you kiss your way down to her chest. She seems to really like it when you suck on her nipples."
        $ the_person.change_arousal(20)
        the_person "Mmm, I've been looking forward to this! I'm good to go, fuck me already!"
        mc.name "Yes ma'am!"
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True, position_locked = True) from _call_fuck_person_kaya_lust_first_time_02
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0 and the_report.get("girl orgasms", 0) >0:
            the_person "Fuck, I love it when you cum. God you make me cum my brains out!"
            if the_report.get("creampies", 0) > 0:
                the_person "It went so deep... I'd be lying if I said I didn't love it when you do that!"
            "You both take a moment, panting softly as you recover from your orgasms."
        elif the_report.get("guy orgasms", 0) > 0:
            the_person "Fuck, I love it when you cum."
            if the_report.get("creampies", 0) > 0:
                the_person "It went so deep... I'd be lying if I said I didn't love it when you do that!"
        elif the_report.get("girl orgasms", 0) > 0:
            the_person "Wow, sorry I finished so fast!"
            the_person "It is going to be a long night... don't worry I'll get you off during round 2, I promise!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.title] slowly gets up, but her legs are a little wobbly."
    the_person "Wow... I think... I had a really long day..."
    mc.name "You aren't calling it a night already are you?"
    the_person "What? No! I... I just really feel like I need a shower!"
    the_person "Can you go make some coffee? Caffeine really perks me up."
    mc.name "Yeah, actually that is a really good idea. I'll do that."
    $ clear_scene()
    $ kitchen.show_background() #I don't actually want to move here... maybe a 'her_kitchen' room?
    "You get up and head to the kitchen. You grab a paper towel and clean up the leftovers from your sex with [the_person.possessive_title]."
    "You look around and find the coffee pot, some coffee, and some filters."
    "For shame, she doesn't even have coffee from the coffee shop she works at. Just some generic stuff."
    "Not that you mind that much. You set out to make some coffee."
    "You load up the grinds into the filter and fill up the water tank, then press the button to brew."
    "When you finish with that, you look around the kitchen a bit."
    "You notice next to the coffee pot is a USB cord going into what appears to be the doorbell camera. It has a green light on the front of it."
    "It must be done charging."
    "You pull out your phone and check on a few work related tasks while you wait for the coffee."
    "When it is done, you rummage around the cupboards, eventually finding two coffee mugs."
    "You fill up yours and take a sip. It is a little bitter, but it will do the job."
    $ mc.change_energy(50)
    $ the_person.change_energy(50)
    $ apply_towel_outfit(the_person)
    "You are almost done with your coffee when [the_person.title] comes into the kitchen."
    $ the_person.draw_person()
    the_person "Mmm, it smells good in here..."
    "She is wearing just a towel. Her dark legs contrast beautifully with it..."
    $ mc.change_locked_clarity(50)
    mc.name "You would think by now you would be sick of the smell of coffee."
    the_person "That's impossible, it is a magical substance."
    $ the_person.draw_person(position = "walking_away")
    "She walks over to the coffee pot and sees the mug you left out for her."
    the_person "Ah, you found everything, nice."
    "She pours herself a cup, then goes to the fridge and opens it. She bends over, grabbing some milk."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "You do your best to mentally will the towel to fall down, but unfortunately it stays, keeping her nubile body covered up."
    $ the_person.draw_person(position = "stand2")
    "She turns around, then stops when she sees your face."
    the_person "Are you okay? You look like you just got told you're allergic to blowjobs."
    mc.name "Yeah, I'm fine, I was just trying to will your towel to fall down, but with no success."
    the_person "Well... I would say your hands would be better tools to do that than your brain."
    "You take the last sip of your coffee, setting your mug down. She mixes some milk into her coffee then puts it back in the fridge."
    $ the_person.draw_person(position = "walking_away")
    "She turns away from you with her coffee, facing the island in the middle of the kitchen."
    "Did her hips just wiggle? You aren't sure, but you can't help but put your hands on them anyway."
    the_person "Mmm..."
    "She moans when you put your hands on her hips. You give a gentle pull to her towel..."
    $ the_person.strip_full_outfit(position = "walking_away")
    "Her towel falls away."
    $ mc.change_locked_clarity(50)
    the_person "See? No thinking required for that! Or for what hopefully comes next..."
    "You move up behind her, bringing your hips up against hers. Your cock is rapidly rising for round two."
    "You leans forward a bit when it begins to rub against her ass."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    the_person "Yes, I've got you all to myself for another 8 hours or so..."
    $ the_person.draw_person(position = "standing_doggy")
    if first_time:
        the_person "Do you think it would work... like this?"
    "She bends over the kitchen island then reaches down between her legs. She grabs your dick and points it forward, guiding it toward her pussy."
    "With her other hand, she reaches back and puts her hand on your hip, urging you to push forward."
    "You let yourself lean forward, slowly penetrating [the_person.possessive_title]'s eager cunt."
    "You look down and watch the last of your erection disappear inside of her. She lets out an involuntary moan."
    the_person "Ohhh... wow that is really deep..."
    "She lets go and puts her hands forward, onto the counter."
    if first_time:
        the_person "Wow... it doesn't hurt at all... this is soooo gooood...!"
    "You give her a few gentle strokes while she gets used to your girth, then give her a forceful one."
    "A sudden crash and a curse from [the_person.title] startles you."
    the_person "Fuck! I spilled my coffee... oh god..."
    $ the_person.change_arousal(20)
    mc.name "Do you want to clean it..."
    the_person "Don't stop! Oh fuck don't stop!"
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(20)
    "You grip her hips and start to fuck her. Her whole body quakes with each thrust."
    call fuck_person(the_person, private=True, start_position = standing_doggy, start_object = make_counter(), skip_intro = True, skip_condom = True, position_locked = True) from _call_fuck_person_kaya_lust_first_time_03
    $ the_report = _return
    $ the_person.energy = 10
    $ the_person.draw_person(position = "standing_doggy")
    if the_report.get("creampies", 0) > 0:
        "As you step back from [the_person.title], you hear a faint squelch and look down as your cum starts to dribble from her pussy and down the inside of her legs."
    the_person "Oh my god."
    "She just stands there for several moments, bent over the kitchen island."
    mc.name "...Are you okay?"
    the_person "I'm amazing. Thanks. I just really wish I hadn't spilled that coffee..."
    mc.name "Why don't you go lay down for a bit? I'll clean up the spill."
    the_person "Yeah... that sounds good..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] slowly stands upright on shaky legs, then walks back toward her bedroom."
    $ the_person.draw_person(position = "back_peek")
    the_person "Don't be long, okay?"
    $ clear_scene()
    "You quickly grab some paper towels and wipe up the spilled coffee, then dump them into a trash can."
    "You put the coffee mug into the sink and rinse it out."
    "You step into [the_person.possessive_title]'s bedroom and see her laying down on her bed."
    $ the_person.change_to_bedroom()
    $ mc.location.show_background()
    $ the_person.draw_person(position = "missionary")
    the_person "I'm worn out... but I want one more go..."
    call perk_time_of_need_story_label() from _time_of_need_kaya_booty_call_lust_61
    mc.name "Alright... I know how we can do this."
    "You step onto her bed, grab her hips and flip her over."
    $ the_person.draw_person(position = "back_peek")
    "Once on her stomach, you crawl up her body. You take your dick in your hand and playfully smack her ass with it a couple times."
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(50)
    the_person "Does it really work like this? I'm not sure you can get it in at this angle..."
    mc.name "Of course it does. Here, let me show you."
    "You sit up. With one hand you grab her ass cheek, spreading it open a bit, and with the other you guide your cock towards her used fuckhole."
    "Once lined up, you easily slide inside her sopping wet cunt. She gasps when she feels how deep you get."
    the_person "Ahhhh! Oh fuck okay... You definitely got it in! Oh fuck!"
    "You give her ass a couple playful spanks. Her cunt twitches around your cock with each one."
    $ the_person.change_arousal(25)
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(10)
    "You give her a couple slow strokes."
    the_person "God I think this might be my favourite position ever... I can just relax..."
    "You reach up and grab her by the hair."
    mc.name "Yeah and I can pin you down and do anything I want."
    "You give her a couple deep thrusts while pulling her hair."
    the_person "Aahh! Oh Fuuuuck..."
    "You let go."
    $ the_person.increase_opinion_score("doggy style sex")
    $ the_person.increase_opinion_score("being submissive")
    the_person "Yeah... definitely my favourite..."
    call fuck_person(the_person, private=True, start_position = prone_bone, start_object = make_bed(), skip_intro = True, skip_condom = True, position_locked = True) from _call_fuck_person_kaya_lust_first_time_04
    $ the_person.energy = 0
    the_person "Oh fuck... I'm done... I'm so tired..."
    "You get off of [the_person.title], she rolls on her side facing away from you."
    "You get in bed beside her, she takes your hand and holds it against her chest."
    the_person "...mmm..."
    "Her breathing slows a bit... did she just pass out?"
    mc.name "... [the_person.fname]?"
    "......"
    "Yep. She's out. Damn! You fucked her senseless. You feel pretty tired yourself."
    "Her body feels amazing up against yours. You pull her close to you and lay your head down."
    "Maybe a quick nap would be okay..."
    "You quickly drift to sleep."
    $ time_of_day = 4
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_kaya_slut_03_01
    $ kaya.outfit.strip_full_outfit()
    "Something rustling around starts to wake you up... suddenly there is a commotion."
    the_person "Oh fuck! WAKE UP!!!"
    $ the_person.draw_person(position = "cowgirl")
    "Suddenly, [the_person.possessive_title] is on top of you."
    the_person "GET UP! YOU GOTTA GO!"
    mc.name "This hardly seems like a proper..."
    "She jumps off you."
    $ the_person.draw_person(position = "walking_away")
    the_person "WE SLEPT IN! I FORGOT TO SET AN ALARM!"
    the_person "My mom is on her way home! YOU HAVE TO GET OUT OF HERE!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "As you sit up, you are hit in the face with a pile of clothes."
    the_person "Oh god... WHERE'S YOUR PANTS!?!"
    "You look around quickly. Somehow they got thrown across the room and are on the floor of her closet."
    mc.name "Over there."
    "You quickly start pulling a shirt over your head and your underwear. She grabs them and throws them to you."
    "You are still missing a sock but are quickly putting your shoes on anyway."
    $ the_person.change_to_hallway()
    "Soon, you are at her front door. You are dressed, but who knows the status of your clothes..."
    mc.name "So umm... call me again sometime?"
    the_person "God yes... last night was so good..."
    $ the_person.draw_person(position = "kissing")
    "She quickly hugs you and gives you a kiss on the cheek."
    $ the_person.draw_person(position = "stand2")
    the_person "GO! She's gonna be home any second! I'm gonna go hop in the shower!"
    mc.name "Bye."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "The door closes and [the_person.possessive_title] disappears behind it. You turn and start walking toward the lift."
    $ renpy.show("Apartment Entrance", what = bg_manager.background("Apartment_Lobby"), layer = "master")
    "Damn! You hit that ass three times last night! You wish you'd remembered to set an alarm or something so you could get one more round with her this morning..."
    $ mc.change_locked_clarity(30)
    "You feel yourself getting a little excited, thinking about your night last night."
    "As you approach the lift, it opens before you can hit the call button."
    $ sakari.draw_person()
    sakari "Ah, [mc.name], I wondered if I might see you this morning."
    "Ohhhh fuck!"
    mc.name "Ah... good morning, I was... errr... I wasn't..."
    "She steps off the lift."
    sakari "It's alright. I'm glad you are taking good care of my daughter. And for being considerate enough to clean up her spills..."
    mc.name "I... I don't know what you..."
    sakari "Relax. [kaya.fname] thought she was being smart by moving the doorbell camera, but she forgot to turn it off."
    if sakari.sluttiness > 60:
        if sakari.has_taboo("vaginal_sex"):
            sakari "When are you going to get around to giving me that treatment?"
        else:
            sakari "Hopefully you can swing by and visit me soon... she isn't the only needy woman who lives here."
    else:
        sakari "I'm just glad to see you are taking such good care of her..."
    $ sakari.draw_person(position = "walking_away")
    "She steps past you into the hallway. You are too dumbfounded to come up with a response."
    $ sakari.draw_person(position = "back_peek")
    sakari "Are you going to catch the lift down?"
    "You suddenly realise the door is closing. You reach out and stop it from closing just in time."
    "You step onto the lift and hit the ground floor. The doors slowly close."
    $ clear_scene()
    "Welp, you probably should have realised when you saw that doorbell camera last night with the green light on that it was recording, not just that the battery was charged."
    "Either way... [sakari.title] seems okay with the whole thing?"
    $ mc.change_location(downtown)
    "You step out of the apartment building. Time to get a new day started!"
    $ kaya.progress.lust_step = 3
    $ add_kaya_booty_call_followup_action()
    return

label kaya_booty_call_followup_label():
    # This label is a text message label between MC and Kaya
    # Kaya informs Mc that she had a long talk with her mom about things, and is glad to report they don't necessarily have to be secretive anymore
    # However, she doesn't feel comfortable banging just anytime she is around.
    $ add_kaya_study_struggle_redux_action()
    return

label kaya_study_struggle_redux_label(the_person):
    #Now that we are at least fuck buddies, once in a while Kaya asks you to bone her in a study room at the university.
    "In this label, Kaya gets more study help."

    $ kaya.progress.lust_step = 4
    # Link anal intro if it ever gets written here.
    return

#80
# At 80, we attempt to convince Kaya to try anal sex. Because of her love of vaginal sex, she originally resists, setting up a one time taboo break mechanic.
label kaya_try_anal_intro_label(the_person):

    $ kaya.progress.lust_step = 5
    return

label kaya_try_anal_recap_label(the_person):

    $ kaya.progress.lust_step = 6
    return

label kaya_try_anal_retry_label(the_person):
    return
