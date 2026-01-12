label tutorial_start():
    menu:
        "I have played Lab Rats 1 Before":
            "It has been a year since the end of your summer job at the university lab."

        "I am new to Lab Rats":
            "A year ago you were a chemical engineering student, getting ready to graduate soon and looking for something to do over the summer."
            "You ended up with a summer job on campus as a lab assistant working with a two-person team."
            "Your lab director, [nora.fname], and her long time lab assistant [stephanie.fname] were investigating the properties of a new lab created molecule."
            "It didn't take long before you discovered it could be used to deliver mind–altering agents. You spent the summer creating doses of \"serum\" in secret."
            "It has been a year since the end of your summer job at the university lab."

    "Your experimentation with the inhibition removing serum was fun, but in the end the effects were temporary."
    "The end of the summer also meant the end of your access to the serum making supplies."
    "Little by little the women slid back into their previous lives."

    scene
    $ bedroom.show_background()

    "Four months ago you graduated from university with a degree in chemical engineering."
    "Since then you have been living at home and sending out resumes."
    "You have had several interviews, followed by rejection letter after rejection letter."
    "You are starting to get really discouraged. It is like someone has poisoned the job well for you. You can't seem to find work anywhere."
    "Today you have an interview with a small pharmaceutical company. It is one of the last ones in the area."
    "You've gotten up early and dressed in your finest suit. You reach into your pocket, feeling a small vial."
    "It is your last vial of Blue Serum, the one you spent so much time researching and developing last summer."
    "You just know if you can land a job at a pharmaceutical plant, somehow you'll be able to keep working on it in secret..."
    $ hall.show_background()
    "You head for the front door, eager to get to your interview early."
    mom "[mom.mc_title], are you leaving already?"
    "[mom.possessive_title!c]'s voice comes from the kitchen, along with the smell of breakfast."
    mc.name "Yeah, I want to make sure I make it on time."
    mom "You haven't had any breakfast yet. You should eat, I'll drive you if you're running late."
    "The smell of cooked toast and frying eggs wins you over and you head to the kitchen."
    $ kitchen.show_background()
    $ mom.draw_person(emotion = "happy", position = "back_peek")
    "[mom.possessive_title!c] is at the stove and looks back at you when you come into the room."
    mom "The food's almost ready. Just take a seat and I'll make you a plate."
    mc.name "Thanks Mom, I didn't realise how hungry I was. Nerves, I guess."
    mom "Don't worry, I'm sure they'll love you."
    "She turns back and focuses her attention on her cooking. A few minutes later she presents you with a plate."
    $ mom.draw_person(emotion = "happy")
    mom "Here you go sweetheart. You look very sharp in your suit, by the way. My little boy is all grown up."
    "You eat quickly, keeping a sharp eye on the time. When you're done you stand up and move to the front door again."
    mc.name "Okay, I've got to go if I'm going to catch my bus. I'll talk to you later and let you know how it goes."
    mom "Wait."
    "Mom follows you to the front door. She straightens your tie and brushes some lint off of your shoulder."
    mom "Oh, I should have ironed this for you."
    mc.name "It's fine, Mom. Really."
    mom "I know, I know, I'll stop fussing. Good luck sweety."
    "She wraps her arms around you and gives you a tight hug. You hug her back then hurry out the door."
    $ clear_scene()
    $ downtown.show_background()
    "It takes an hour on public transit then a short walk to find the building. It's a small single level office attached to a slightly larger warehouse style building."
    "You pull on the door handle. It thunks loudly—it's locked. You try the other one and get the same result."
    mc.name "Hello?"
    "You pull on the locked door again, then take a step back and look around for another entrance you might have missed. You don't see any."
    "You get your phone out and call the contact number you were given a few days earlier. It goes immediately to a generic voice mail system."
    "With nothing left to do you give up and turn around. Suddenly there's a click and the front door to the office swings open."
    "Janitor" "Hey, who's making all that noise?"
    "A middle–aged man is standing at the door wearing grey-brown overalls. He's holding a stack of papers in one hand and a tape gun in the other."
    mc.name "That was me. I'm supposed to be here for a job interview, do you know where I should be going?"
    "Janitor" "Well I think you're shit out of luck then. They went belly up yesterday. This place belongs to the bank now."
    mc.name "What? That can't be right, I was talking to them less than a week ago."
    "Janitor" "Here, take a look for yourself."
    "The man, who you assume is a janitor of some sort, hands you one of the sheets of paper he's holding."
    "It features a picture of the building along with an address matching the one you were given and a large \"FORECLOSED\" label along the top."
    "The janitor turns around and holds a page up to the front door, then sticks it in place with tape around all four edges."
    "Janitor" "They must have been neck deep in debt, if that makes you feel better about not working for 'em."
    "Janitor" "They left all their science stuff behind; must've been worth less than the debt they're ditching."
    mc.name "So everything's still in there?"
    "Janitor" "Seems like it. Bank doesn't know where to sell it and didn't want me to warehouse it, so it goes with the property."
    "You look back at the foreclosure notice and read until you see the listing price."
    "The price on the unit is expensive, but an order of magnitude less than what you would have expected a fully stocked lab to be worth."
    mc.name "Would you mind if I take a quick look around? I promise I won't be long."
    "The janitor gives you a stern look, judging your character, then nods and opens the door."
    "Janitor" "I'm just about done tidying this place up so the bank can sell it. If you can be in and out in five minutes you can look around."
    mc.name "Thank you, I'll be quick."
    "You step inside the building and take a walk around."
    "The main office building contains a small lab, much like the one you worked at while you were in university, suitable for research and development tasks."
    "The connected warehouse space has a basic chemical production line installed. The machines are all off-brand but seem functional."
    "At the back of the building is a loading dock for shipping and receiving materials."
    "While you're exploring you hear the janitor yell from across the building."
    "Janitor" "I need to be heading off. Are ya done in there?"
    mc.name "Yeah, I'm done. Thanks again."
    "The janitor locks the door when you leave. You get on a bus heading home and do some research on the way."
    "You look up the price of some of the pieces of equipment you saw and confirm your suspicion. The bank has no idea how valuable the property really is."
    $ clear_scene()
    $ kitchen.show_background()
    "Three days later..."
    $ mom.draw_person(position = "sitting")
    "[mom.possessive_title!c] looks over the paperwork you've laid out. Property cost, equipment value, and potential earnings are all listed."
    mom "And you've checked all the numbers?"
    mc.name "Three times."
    mom "It's just... this is a lot of money [mom.mc_title]. I would need to take a second mortgage out on the house."
    mc.name "And I'll be able to pay for that. This is the chance of a lifetime, Mom."
    mom "What was it you said you were going to make again?"
    mc.name "When I was working at the lab last summer we developed some prototype chemical carriers. I think they have huge commercial potential."
    mc.name "And there's no regulation around them yet, because they're so new. I can start production and be selling them tomorrow."
    "[mom.possessive_title!c] leans back in her chair and pinches the brow of her nose."
    mom "Okay, you've convinced me. I'll get in touch with the bank and put a loan on the house."
    "You jump up and throw your arms around [mom.possessive_title]. She laughs and hugs you back."

    lily "What's going on?"
    $ lily.draw_person()
    "[lily.possessive_title!c] steps into the doorway and looks at you both."
    $ mom.draw_person(position = "sitting")
    mom "Your brother is starting a business. I'm his first investor."
    $ lily.draw_person(emotion = "happy")
    lily "Is that what you've been excited about the last couple days? What are you actually making?"
    mc.name "I'll have to tell you more about it later Lily, I've got some calls to make. Thanks Mom, you're the best!"
    $ clear_scene()
    "You leave [mom.possessive_title] and [lily.possessive_title] in the kitchen to talk. You retreat to your room for some privacy."

    $ bedroom.show_background()
    "You can manage the machinery of the lab, but you're going to need help refining the serum design from last year. You think back to your old lab job."
    "The antics you had at the lab with [nora.fname] and [stephanie.fname] were great, but after so long without being dosed with your serum, you doubt you could convince them..."
    "On your dresser, a small blue vial catches your eye. Your last vial of Blue Serum."
    "A desperate plan forms in your head. Maybe, just maybe, you could convince [nora.fname] to quit her job at the university and run YOUR research department."
    "If you had thought about it longer, you probably would have stopped yourself, but with the financials already worked out, desperation forces your hand."
    "You pick up your phone and call [nora.fname]."
    nora "Hello?"
    mc.name "[nora.fname], this is [mc.name]."
    nora "[nora.mc_title]. Is there a reason a former pupil is calling me?"
    mc.name "I'd like to talk to you about a business offer. Any chance we could meet somewhere?"
    nora "[nora.mc_title], whatever hair brained MLM scheme you've concocted isn't worth..."
    mc.name "No no no, it isn't anything like that. I'm working on a pharmaceutical project."
    "There are several seconds of silence on the line."
    nora "I can't believe I am about to say this... but I'm about done at the lab for the night. Meet me there in a bit."
    "[nora.fname] sends you the address of a bar close to the university."
    nora "I have other plans for the evening, so I can give you ten minutes. Got it?"
    mc.name "I'll meet you there."
    "You hang up the phone. You suddenly aren't so sure this is a good idea..."
    $ clear_scene()
    $ scene_manager = Scene()
    $ mc.change_location(downtown_bar)
    "It takes you an hour to get your pitch prepared and to get over to the bar."
    "When you arrive [nora.possessive_title] is sitting at a booth near the back. She nods when you see each other."
    $ scene_manager.add_actor(nora, position = "sitting")
    "You quickly point to the bar to indicate you are getting drinks. She rolls her eyes, then nods."
    "You order a beer and a blue lagoon. While waiting for the drinks, you look over and notice that [nora.fname] is watching you intently."
    "You had hoped you could get here before her. This is really starting to make you nervous."
    "The bartender sets your drinks on the counter and you quickly pay for them. In your pocket, you take off the cap to the vial of serum."
    "Doing your best to conceal it, you turn your back to [nora.possessive_title] for a second... and quietly splash the serum into the fruity drink. It dissolves quickly."
    "You take the drinks over to the table, setting the blue lagoon in front of [nora.fname]."
    mc.name "Hey [nora.fname], it's great to see you!"
    nora "Yes, I'm sure it is. Your ten minutes started when you walked in, and you are down to eight."
    mc.name "Ohhhh don't be like that."
    "You take a seat across from her and take a sip of your drink. She doesn't touch the drink you put in front of her."
    "You try to break the ice a bit with some small talk."
    mc.name "So, how are things going at the university?"
    $ nora.change_happiness(-1)
    $ nora.create_opinion("small talk", start_positive = False, start_known = False, add_to_log = False)
    $ nora.discover_opinion("small talk")
    nora "Small talk? Really? Is that what you've dragged me out here for?"
    "That's right, [nora.possessive_title] isn't the type for small talk."
    "You try to switch tactics."
    mc.name "Of course not. I've been thinking about my beautiful former professor for a while now and I wanted to get in touch again."
    $ nora.change_happiness(-1)
    $ nora.create_opinion("flirting", start_positive = False, start_known = False, add_to_log = False)
    $ nora.discover_opinion("flirting")
    $ scene_manager.update_actor(nora, position = "sitting", emotion = "angry")
    "She sighs and shakes her head."
    nora "Flirting now? Your words are empty [nora.mc_title]. Tell me why you've really asked me here. I don't have time for games."
    nora "Does it have something to do with whatever you put in this?"
    "She points to her drink."
    nora "Some kind of date rape drug? Is that really how low you've let yourself go since you graduated?"
    mc.name "Whaaaaat? I didn't put anything..."
    "She gets ready to stand up."
    nora "Unfortunate. You still have five minutes, but clearly this is a waste of time so I'll..."
    "Seeing your opportunity go up in smoke, you quickly interrupt her."
    mc.name "It's a serum I created. It isn't some kind of date rape drug. I designed it originally while I was working in the lab with you."
    $ scene_manager.update_actor(nora, position = "sitting", emotion = "happy")
    "[nora.fname] stops herself from getting up. Was that a brief smile?"
    mc.name "I made it to make people more... shall we say... suggestible. It doesn't do anything too crazy, but helps me sway others' opinions the way I want."
    mc.name "The reason I contacted you... I bought a pharmaceutical manufacturing lab. I need someone to help me run the research department."
    "She chuckles for a moment."
    nora "Haha... and you think... that if I took this drink, that you could convince me to quit my tenured job at a prestigious university and work for you?"
    mc.name "Ummmm, well, when you say it that way."
    "There are several seconds of silence, before she speaks up again."
    nora "Yes... Yes it all makes sense now."
    mc.name "Yeah... it does?"
    nora "Yes. About 3 months ago I was cleaning out my office, as my department was getting... shall we say downsized."
    nora "Several chemicals had gone missing... which I now realize was likely your doing in the first place... and my superior had just swung by to say goodbye."
    nora "I had just stumbled on an old vial filled with blue liquid. He asked me what it was, and I just laughed and said it was an experiment by a former student, trying to replicate the flavor of blueberries."
    nora "I don't know what possessed me to say it, but I told him to try it, after assuring him it was perfectly safe."
    nora "Of course... it tasted NOTHING like blueberries. But in those moments after he drank it and grimaced, something changed."
    nora "I was about to be out of a job, and so I asked him one last time. Was there any way we could make changes to keep the lab?"
    nora "He looked at me for several seconds, and then I couldn't believe what he said."
    nora "He said, only if there were cutbacks. The real problem wasn't missing chemicals, but the budget."
    nora "If I could figure out a way to balance the budget, I could keep the lab."
    "Huh. That is interesting."
    "Wait... she said he? Your serum worked on a man?"
    "Of course it worked on a man. Why wouldn't it? You just never got farther than thinking with the thing in your pants about possible applications..."
    "[nora.possessive_title!c] looks at you, curiously."
    nora "I didn't realize what had actually happened... until just now, when I saw you put that blue liquid in this drink at the bar."
    nora "It was you the whole time. All those... indiscretions... at the lab. And the missing chemicals."
    "You sigh. Looks like there's no way out of this."
    mc.name "Yeah... yeah it was me."
    "It feels good to confess it, finally. But with this information... you could wind up in jail!"
    "You quickly look back at [nora.fname], alarmed."
    mc.name "I... I never intended to hurt anyone..."
    nora "No, I know. And you didn't. It was certainly a hell of a summer."
    nora "Well, you didn't hurt me anyway. But [stephanie.fname], the poor girl."
    nora "Let's just say that you have been a frequent topic of discussion, since you disappeared on us."
    mc.name "Yeah, how is she doing?"
    nora "Not great. Ever since our budget got cut, we've just been strangled in bureaucratic red tape trying to procure ANY kind of chemical supplies..."
    nora "And, well, one of the items that got cut was payroll for my assistants. I'm afraid she's barely able to make ends meet right now."
    "She looks down at the drink, thoughtfully."
    nora "Well, I believe your ten minutes are up. It was certainly an *interesting* proposal."
    mc.name "I did mean it earlier, it *is* good to see you. I'm sorry if I wasted your time."
    nora "Oh [nora.mc_title], this wasn't a waste of time. You see, I'm meeting someone else here tonight, too."
    nora "Let's see... ah here she comes, right on time."
    "From behind you comes a friendly, familiar voice."
    stephanie "Hey [nora.fname]! Already got a drink? And met a GUY???"
    $ scene_manager.add_actor(stephanie)
    stephanie "I can't believe you are meeting a... [stephanie.mc_title]? Is that you?"
    "A big grin spreads across her face, but quickly changes to wrath."
    stephanie "What. The. FUCK man!?! I haven't heard from you for months!!! Where the hell have you been!"
    "She smacks your arm, making clear her displeasure with your distance."
    mc.name "I'm sorry, I graduated and I've been looking for work..."
    $ scene_manager.update_actor(stephanie, position = "sitting")
    "[stephanie.possessive_title!c] plops down into the booth next to [nora.fname]."
    stephanie "Well, sorry to say it, but if you're hitting up Professor [nora.fname] for work, you're barking up the wrong tree."
    stephanie "The budget people came in and made HUGE cuts. There's barely enough work for me there."
    mc.name "Yeah, she was just telling me about that. Actually I asked her to meet me tonight for something else."
    stephanie "Oh? Did you miss our smiling faces in the lab and just want to catch up for a bit?"
    mc.name "Yeah, something like that."
    "Suddenly, something happens that you weren't expecting."
    nora "Don't be too mad at him, [stephanie.fname], he already bought you a drink. Here you go."
    "[nora.possessive_title!c] slides the blue lagoon that you got her over in front of [stephanie.fname]."
    stephanie "Oh yum! This looks great, I love fruity drinks..."
    "She picks up the drink and quickly downs about half of it. Your face must have displayed shock, as [nora.fname] quickly signals to you with her hands and eyes to act casual."
    $ stephanie.give_serum(get_blue_serum())
    stephanie "Oh wow, that's really nice."
    "[stephanie.possessive_title!c] looks at you, trying to give you a stern warning."
    stephanie "Look, if you think you can butter me up with free booze, you're gonna have to come up with something better than that."
    "[nora.fname] is looking at you expectantly. Is she watching to see what you do?"
    "She's testing you. She wants to see how you work the serum to your advantage."
    menu:
        "Flirt with her":
            pass
    mc.name "Of course not... but is there something else I could butter you up with?"
    "You lay it on thick with a flirting tone, and [stephanie.possessive_title]'s cheeks turn red."
    stephanie "Oh! Wow... I mean I could probably think of something..."
    $ stephanie.change_slut(3, 40)
    $ stephanie.change_happiness(5)
    "You feel a foot under the table rub along the side of yours."
    "[nora.possessive_title!c] eyes widen as she witnesses just how quickly your serum takes effect, and how easily you are able to turn [stephanie.fname]'s opinion."
    "She clears her throat and then interrupts."
    nora "Yes, he was actually telling me all about a business he is trying to start up. An ambitious one."
    stephanie "Oh?"
    nora "Yes, and he was asking me if I knew of anyone who he could trust to help run his research department. Naturally I thought of you."
    stephanie "That's... whoooaaaa, what are you saying?"
    "You suddenly realize what [nora.fname] is doing. Yes, [stephanie.fname] could step into the role perfectly."
    mc.name "Yes, you remember last summer?"
    stephanie "That was a crazy summer we had together. It seems like such a blur now, but I had a lot of fun."
    mc.name "Me too, that's actually part of what I want to talk to you about."
    "You lay out your idea to [stephanie.fname]: the commercial production and distribution of the experimental serum."
    stephanie "Well that's... Fuck, it's bold, I'll say that. And you need me to handle the R&D side of the business?"
    mc.name "Right. Production processes are my bread and butter, but I need your help to figure out what we're actually making."
    "[stephanie.possessive_title!c] finishes off her drink and flags down the bartender for another."
    stephanie "I would need to quit my job at the lab. [nora.fname]... are you really okay with this?"
    nora "I am. You know how much trouble it has been lately with the damn red tape for every single experiment."
    nora "Besides, this serum he is working on is... interesting. I want to see where it goes."
    nora "I don't have the budget to make any direct contributions, but we may have opportunities for mutual benefits down the road."
    "[stephanie.fname] looks back at you."
    stephanie "Do you have any clients?"
    mc.name "Not yet. It's hard to have clients without a product."
    "[stephanie.fname] gets her drink and sips it thoughtfully."
    mc.name "The pay won't be great either, but I can promise..."
    stephanie "I'm in."
    mc.name "I... what?"
    stephanie "I'm in. [nora.fname] is right. The lab just hasn't been the same since you left, and the oversight has been suffocating."
    stephanie "I need to shake things up. I need change in my life, something to bring back excitement."
    stephanie "I think this is it."
    "She raises her drink and smiles a huge smile."
    stephanie "A toast: To us, and stupid risks!"
    mc.name "To us!"
    $ stephanie.change_love(3, 40)
    "You clink glasses together and drink."
    nora "Alright. You can consider this your official resignation [stephanie.fname]."
    stephanie "Wow, what a crazy night."
    nora "I'll let you two have a couple weeks to get the financials sorted. Then I'd like to meet here again. Say two weeks from Saturday?"
    mc.name "Yeah? Why here?"
    nora "It'll be easier to meet here than somewhere at the university. You'll have to trust me on that."
    nora "Besides, university security has been increasingly tight lately. I'm not even sure that they would let you on property anymore."
    mc.name "Wow, I suppose I'll wait to hear from you then."
    nora "Well, I need to be off. [stephanie.fname], feel free to run up [mc.name]'s bar tab tonight."
    stephanie "You got it, boss! Hey, I've already got a couple ideas..."
    $ scene_manager.remove_actor(nora)
    "[stephanie.fname] grabs a napkin and starts doodling on it while [nora.possessive_title] gets up and leaves. You spend the rest of the night with her, drinking and talking until you have to say goodbye."
    $ scene_manager.clear_scene()
    "Two weeks later [mom.possessive_title] has a new mortgage on the house and purchases the lab in your name."
    "You are the sole shareholder of your own company and [stephanie.fname] is the first, and so far only, employee. She takes her position as your head researcher."
    python:
        mc.business.event_triggers_dict["Tutorial_Section"] = True
        mc.change_location(bedroom)
        for location in office_hub:
            location.accessible = False
        lobby.accessible = True
        stephanie.serum_effects = []
    return

label lobby_tutorial_intro():
    "You arrive at your newly purchased lab building. It's small, out of date, and run down, but it's yours!"
    "You can see [stephanie.fname] through the glass front door as you walk up. She turns and waves when you come in."
    $ stephanie.draw_person(emotion = "happy")
    stephanie "Hey [stephanie.mc_title]. I can't believe you were able to find this place, this is a once-in-a-lifetime opportunity."
    mc.name "I got lucky, that's all. Have you been here long?"
    stephanie "Just a few minutes. I figured we could take a walk through the place together and make sure we know what we're doing."
    mc.name "Sounds like a good idea."
    "[stephanie.possessive_title!c] motions to the room you're standing in. The only item of interest in the small room is a welcome desk covered in a thin layer of dust."
    stephanie "This is the lobby I guess. I doubt we'll be spending much time here."
    mc.name "There's a lab section down here that I thought would be ideal for your R&D work."
    stephanie "Sweet, let's go take a look."
    $ lobby.accessible = False
    $ rd_division.accessible = True
    $ clear_scene()
    return

label research_tutorial_intro():
    $ stephanie.draw_person(emotion = "happy")
    "The small room has a couple of lab benches with fume hoods, old but serviceable glassware, and a few more delicate instruments you don't recognise by sight."
    mc.name "Here we are, what do you think?"
    "[stephanie.possessive_title!c] starts to walk down the benches, checking cabinets and machinery."
    stephanie "I'll need some more time to check it all out, but it all looks like it works. Holy crap [stephanie.mc_title], I can't believe you're giving me my own lab."
    mc.name "I need you [stephanie.fname]. You've got the expertise and talent to get this place off the ground."
    stephanie "I'll try not to let you down. So, let's talk about how this R&D is going to work."
    stephanie "I have a few different ideas I can explore right now. With some time I should be able to figure out some new fundamental property."
    stephanie "When you want to produce an actual product we will need to create a new serum design."
    stephanie "It will take some more research work to figure out how we can actually produce the design."
    stephanie "Right now I think we'll struggle to get a few properties to express themselves properly in our serums, but with some experience we can combine a bunch."
    mc.name "Right, I think I understand."
    "[stephanie.possessive_title!c] pulls out a notebook and flips it open, handing it over to you."
    stephanie "These are my first ideas, you should pick something for me to work on right now. If you change your mind you can always come back here and pick a new topic."
    $ clear_scene()
    call research_select_action_description() from _call_research_select_action_description
    "You read through the options she's laid out. \"Suggestion Drugs\", \"Inhibition Suppression\", and vague hints of even more {i}questionable{/i} developments down the line."
    $ mc.change_locked_clarity(10)
    "You weren't planning for this to be a repeat of last year, but [stephanie.fname] seems happy to hand you all the tools you would need."
    "You're so distracted by your thoughts that [stephanie.possessive_title] needs to clear her throat to get your attention again."
    $ stephanie.draw_person()
    stephanie "Well? What do you think?"
    if mc.business.active_research_design:
        mc.name "[mc.business.active_research_design.name] seems like it would be the most promising option for now."
        $ stephanie.draw_person(emotion = "happy")
        stephanie "That's a very clever thought [stephanie.mc_title], I'll start studying that right away."
    else:
        mc.name "It, uh... It all looks good. Start wherever you want."
        stephanie "I'm going to need a little more direction than that [stephanie.mc_title]."
        stephanie "This isn't quite brain surgery, but you could throw a rock into their backyard. I need your input."
        "You try to take another look through her notes, but you can't focus your mind."
        $ mc.change_arousal(40)
        "Your dick seems to be using more than its fair share of brain power to run some imaginative scenarios."
        menu:
            "Go jerk off":
                "You can only think of one immediate solution to the problem."
                mc.name "I'll need a moment to think about this. Just wait here, I'm going to stretch my legs and take a walk around."
                stephanie "Sure, I'll come with..."
                mc.name "I think better alone, actually."
                stephanie "Oh, sure... Uh, I'll be here then..."
                $ clear_scene()
                $ mc.change_location(ceo_office)
                "You find your personal office, or what will be once you get the old name plate removed, and step inside."
                "You close the door and sit down at the desk, pulling out your phone to find some porn to get you off."
                $ mc.change_arousal(10)
                $ mc.change_locked_clarity(10)
                "You settle on an old favourite and start to jack off, determined to make it quick."
                "After a couple of minutes you notice something odd—you're barely paying attention to the bouncing tits on your tiny screen."
                $ mc.change_arousal(10)
                $ mc.change_locked_clarity(10)
                "Instead you're remembering all the trouble you got up to last year, and all the new opportunities you will have now."
                "Does [stephanie.fname] really not care what you're making here, and what it can do? How could she not?"
                "Maybe she likes it? Maybe you really left an impression on her with your last serum-based mind control spree?"
                $ mc.change_arousal(20)
                $ mc.change_locked_clarity(10)
                "... Maybe she wants to help this time?"
                "That thought pushes you over the edge!"
                $ climax_controller = ClimaxController(["Cum!", "masturbation"])
                $ climax_controller.show_climax_menu()
                $ climax_controller.do_clarity_release()
                "You snatch at some tissues and do your best to contain the mess as you cum."
                "A cold calm washes over you now that you're finished, and along with it the razor sharp focus you'll need to achieve your goals."
                "You double-check that you're presentable and return to the research lab."
                $ mc.change_location(rd_division)
                $ stephanie.draw_person()
                stephanie "Well, any ideas?"
                "This time when you look at her notes they all make perfect sense. You see what will need to be studied, and how to turn that knowledge into a useful discovery."
                call research_select_action_description() from _call_research_select_action_description_1
                $ stephanie.draw_person(emotion = "happy")
                stephanie "That's a very clever thought [stephanie.mc_title], I'll start studying that right away."

            "Pick your research later":
                mc.name "I'll need some time to look these options over. Make sure all of these machines are working at peak efficiency until then."
                "[stephanie.fname] seems disappointed by the slow start."
                stephanie "Fine, I'll run them all through a diagnostic cycle. Don't keep me waiting though, I don't want to just sit around and waste time."

    stephanie "Can we take a look at the production lab now?"
    $ rd_division.accessible = False
    $ p_division.accessible = True
    $ clear_scene()
    return

label production_tutorial_intro():
    $ stephanie.draw_person(emotion = "happy")
    "This lab room is larger than [stephanie.possessive_title]'s research lab and filled with bulkier and more familiar equipment."
    stephanie "When I'm finished creating a serum design you can take it here and tool up the production lines to make it on an industrial scale."
    stephanie "There's enough storage space to keep our finished products here, but eventually you'll want to sell them."
    mc.name "Right, I saw some space next to a loading dock that looks like it would be good for marketing."
    mc.name "Of course I'm also going to need some basic chemical supplies, so I need to make sure to order them."
    stephanie "Or hire someone else to do that for you. If you want to turn this into a successful business we will probably need more than just the two of us."
    "You take a quick walk around the production lab."
    mc.name "Let's go check out the marketing area."
    stephanie "Lead on!"
    $ p_division.accessible = False
    $ m_division.accessible = True
    $ clear_scene()
    return

label marketing_tutorial_intro():
    $ stephanie.draw_person(emotion = "happy")
    "The marketing room is a combination of office and mail room. It comes with all the supplies you would need to mail out your product to your customers."
    mc.name "When we've got actual products to sell I'll be able to come here and mail them off."
    stephanie "I suppose we'll be relying on word of mouth for now, but we should see about advertising in the future."
    "You nod in agreement and wander around the room until you're satisfied there's nothing more of interest."
    stephanie "I think the proper offices are down here, let's go take a look."
    $ m_division.accessible = False
    $ office.accessible = True
    $ clear_scene()
    return

label office_tutorial_intro():
    $ stephanie.draw_person(emotion = "happy")
    "The offices are divided into a few separate cubicles and a small private office."
    stephanie "This seems like a good place to do any of your supply ordering from, and there's even a private office for you to do administrative tasks."
    mc.name "The more people we take on the more paperwork I'm going to have to do to keep everyone organized."
    stephanie "With enough employees that would end up being a full time job all by itself. I don't envy you [stephanie.mc_title], I much prefer my cosy little lab."
    mc.name "That's all there is to see here. Let's check out my swanky corner office."
    $ office.accessible = False
    $ ceo_office.accessible = True
    $ clear_scene()
    return

label ceo_tutorial_intro():
    $ stephanie.draw_person(emotion = "happy")
    "The corner office is pretty fancy. All the furniture is a few steps above what fills the rest of the building."
    stephanie "Impressive! You can use this office to interview anyone who you're thinking of hiring."
    mc.name "It will also give me a quite place to plan out any major changes, like policies for how I staff and run the business."
    stephanie "Also if we end up getting any big clients who need your personal touch, you'll be able to discuss their contracts here."
    mc.name "That's everything there is to see, so I guess it's time to get to work!"
    stephanie "I'll get back to the lab, come see me if you want to check in on my progress."
    #End Tutorial
    python:
        mc.business.event_triggers_dict["Tutorial_Section"] = False
        for place in office_hub:
            place.accessible = True
        clear_scene()
    call advance_time() from _call_advance_time_11
    return
