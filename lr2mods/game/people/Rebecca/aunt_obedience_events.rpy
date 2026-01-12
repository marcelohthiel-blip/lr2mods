# Rebecca's obedience story.
# At first, we convincer her to help out with the business accounting.
# Later, we find out she used to help her ex with his business finances, and that he used to launder money
# She helps us with MC's business, laundering money
# Later, we gain the ability to blackmail her ex

#Obedience story intro
# Scene: We enter Aunt's house and find her working on an online class on her laptop.
label aunt_accounting_intro_label(the_person):
    "You step into [the_person.possessive_title]'s apartment. At first, you don't see her."
    $ the_person.draw_person(position = "sitting")
    "Then you notice her sitting at a desk with her laptop, working on some kind of paper."
    mc.name "Hey [the_person.title]."
    the_person "Oh? Oh hi [the_person.mc_title]. Give me a minute..."
    "She turns back to her laptop and continues typing for a couple minutes, a couple of times firing up the calculator app as well."
    "When she finishes, she gets up and turns to you."
    $ the_person.draw_person()
    the_person "Good to see you. What brings you here?"
    mc.name "Oh, you know, just checking up on my favourite aunt! What are you up to anyway?"
    the_person "I was just finishing up with a short essay I'm writing. I'm working on renewing my CPA license, and I need 40 hours of online learning."
    mc.name "CPA? You mean like accounting?"
    the_person "Yeah. Your uncle is paying for most of this, but I'd like to be able to make my own living, and the sooner the better."
    the_person "There's no telling what could happen if he hires the right lawyer."
    mc.name "I didn't know that you were an accountant."
    the_person "Yeah, that is actually how your uncle and I met. We were both working at the same office and had an office romance."
    the_person "I got knocked up, and instead of the company firing us both for fraternizing, I quit and we eloped."
    mc.name "Oh wow, I never knew."
    "She sighs."
    the_person "Yeah well, we didn't exactly make it public knowledge either. Good for your mom for keeping it to herself."
    the_person "But, I don't really care if people know about that anymore."
    the_person "I'm at a good stopping point for now, so I think I'll take a break. Make yourself at home, okay?"
    mc.name "Sounds good, [the_person.title]."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks toward her kitchen."
    "That is very interesting, you had no idea she had a background in accounting. You start thinking about your own business."
    "Right now, you just have some old budgeting software you use now and then... you wonder if it might be a good idea to bring on an accountant of some sort?"
    "Of course, if you had someone come in... they would have access to all your financial ledgers... it would need to be someone you could really trust."
    "You quickly call out to her before she disappears into the kitchen."
    mc.name "Hey [the_person.title]."
    $ the_person.draw_person(position = "back_peek")
    the_person "Yes?"
    mc.name "How long until you have your renewal finished?"
    the_person "It goes pretty quick. I should be able to have it done in a week or so."
    mc.name "Right..."
    $ clear_scene()
    "[the_person.possessive_title!c] leaves the room. You start to come up with a rudimentary plan."
    "Maybe if you moulded her obedience with a few serums, you could bring her in to work on your books as well."
    "For now, you decide to let her finish up her renewal and check back in with her about it on another day."
    $ aunt.progress.obedience_step = 1
    $ add_aunt_accounting_cpa_renewal_action()
    return

label aunt_accounting_cpa_renewal_label():
    $ the_person = aunt
    $ the_person.draw_person(emotion = "happy")
    $ mc.change_location(aunt_apartment)
    "You walk in to [the_person.fname]’s apartment. You find her in her living room, drinking a glass of wine."
    mc.name "Hello [the_person.title]. Drinking this early?"
    the_person "Hello [the_person.mc_title]! I am! I am celebrating!"
    mc.name "Oh? What are we celebrating this evening?"
    "You grab a wine glass and start to pour yourself some."
    the_person "Well, I just finished up with the last test for my CPA renewal!"
    the_person "It went well, so I was able to print off a temporary certificate while I wait for the official one in the mail!"
    the_person "Your aunt is now a certified accountant!"
    mc.name "That's great! Congratulations!"
    "You lift up your glass."
    mc.name "A toast!"
    the_person "Cheers!"
    "You clink your glasses together and then take a sip."
    mc.name "So… what’s next for you?"

    the_person "Well I suppose I'll be starting the job hunt! Surely there is a business or two around here who needs an accountant."
    "You think about it for a moment."
    mc.name "You know, I don't think I could employ you full time, but I could probably use a professional to help me with my books part time, if you need something to do while you search for something more stable."
    "She chuckles and then responds."
    the_person "I couldn't possibly. I'm not one to take charity."
    "She finishes off her glass of wine, then looks at you."
    the_person "I appreciate the offer, but it wouldn't feel right working for you anyway. I'm sure I'll be able to find work soon enough."
    "She looks down at her empty glass, then back at you."
    mc.name "Can I get you a second glass tonight, [the_person.title]?"
    the_person "Oh... normally I wouldn't, but what's the harm in it?"
    call aunt_share_drinks_mid_entry_label(the_person) from _aunt_mid_entry_drinks_cpa_renewal_01
    $ clear_scene()
    $ mc.change_location(downtown)
    "You leave [the_person.possessive_title]'s apartment."
    "She is very smart, you are sure she'll find something soon... but still..."
    "If you could get her into your company, even just for some part time consulting, you're SURE you could find the opportunity to get closer to her."
    "Maybe if you work on her obedience she'll come around."
    $ add_aunt_employment_problems_action()
    $ aunt.progress.obedience_step = 2
    call advance_time() from _call_advance_time_aunt_obedience_renewal_01
    return

label aunt_employment_problems_label(the_person):  #120
    $ the_person.draw_person(emotion = "angry")
    "You stop by to visit [the_person.possessive_title]. When you walk inside, you see her in the kitchen."
    "She seems to be in a state of distress."
    mc.name "Hey [the_person.title]… are you okay?"
    the_person "Hi… no. I'm not."
    mc.name "What is going on?"
    the_person "I just got off the phone with an accounting firm."
    the_person "I had made it to a phone interview, and they had told me they just needed to check my references… but then called me today and said I wouldn't be a good fit."
    $ the_person.draw_person(position = "back_peek", emotion = "angry")
    "She turns into her kitchen, and starts pulling out a wine glass and a bottle of wine from her fridge."
    the_person "This was my third interview in a week that turned me down."
    the_person "I pressed their HR person asking why, and at first they were very hesitant."
    the_person "I managed to persuade one of them though… they said that when checking my work history, they said my previous company reported that I had been fired for embezzling a large sum of money."
    $ the_person.draw_person(position = "stand2", emotion = "angry")
    mc.name "That's crazy."
    the_person "I know! And you know who I worked for last? The company my husband later took over!"
    the_person "I called him absolutely irate over the issue, and he just laughed it off. I threatened legal action for slander, but he knows I'm bluffing."
    the_person "They've got an army of lawyers who could drag down any proceedings for YEARS."
    $ the_person.draw_person(position = "sitting", emotion = "sad")
    "[the_person.possessive_title!c] sits down at her table with her head in her hands."
    the_person "I don't think I'll ever find work like this… he has absolutely RUINED my professional reputation!"
    "She uncorks her bottle of wine and pours herself a very full glass then takes a big swig."
    "You remember when she first finished her CPA license that you offered to bring her on to do some part time work… maybe now she would be willing to?"
    mc.name "What if you could find a couple part time consulting gigs?"
    "She looks up at you."
    the_person "I don't know… most of things are about who you know. And I don't know anyone anymore!"
    mc.name "Well, I could really use an extra set of eyes on my books at my company. It would be great to have a professional checking everything."
    mc.name "Plus, weirdly enough, it feels like my employees are constantly asking me about their taxes… I could refer them to you?"
    the_person "I… hate to feel you are doing this just to do me a favour…"
    mc.name "It's fine. Just come out and check the place out, see how it goes. If you can't find anything, I'll still pay you a one time consulting fee."
    "She takes another drink, finishing her glass of wine."
    the_person "Oh what the hell. I don't have anything to lose, and I guess you could be alright... boss?"
    $ the_person.draw_person(emotion = "happy")
    if the_person.love > 20:
        the_person "It might even be nice to have a little more time with my favourite nephew..."
    elif the_person.sluttiness > 20:
        the_person "It might even be nice to work for such a handsome young man..."
    else:
        the_person "You've been so good to me so far, it might even be nice."
    mc.name "Glad to hear it. My Mondays are usually pretty busy... how about you swing by on Tuesday morning?"
    the_person "Deal. I'll look forward to it."
    the_person "Know anyone else who might have use for a part time accountant, mister businessman?"
    "You think about it for a moment. Is there anyone else you can think of that could some help with accounting?"
    if starbuck.progress.obedience_step >= 1:
        call starbuck_rebecca_teamup_setup_one_label(the_person, skip_intro = True) from _call_starbuck_rebecca_teamup_setup_one_label
    else:
        "You think about it for a bit, but no one comes to mind, so you just shrug."
        mc.name "Not off the top of my head, but I'll keep my eyes out."
    the_person "Well, how about another round of wine tonight? A toast to my new employer?"
    "She hands you a second wine glass."
    mc.name "Part time employer, of course."
    the_person "Of course."
    call aunt_share_drinks_mid_entry_label(the_person) from _aunt_mid_entry_drinks_job_trouble_01
    $ clear_scene()
    $ mc.change_location(bedroom)
    "As you leave [the_person.possessive_title]'s apartment and go home, you start to prepare yourself mentally for her coming to your office."
    "She'll be alone in your office, so it would be a prime opportunity to spend some alone time with her, or possibly dose her with serums."
    "If you can get her to be more obedient, maybe you could even let her in on the more explicit details of your business, and help cover your tracks."

    $ add_aunt_cpa_first_day_action()
    $ aunt.progress.obedience_step = 3
    call advance_time() from _call_advance_time_aunt_obedience_employment_01
    return


label aunt_cpa_first_day_label():
    $ the_person = aunt
    $ mc.change_location(lobby)
    $ scene_manager = Scene()

    "You feel your phone vibrate in your pocket. You check and see that [the_person.possessive_title] has texted you that she is on her way to your business."
    "You hurry to the lobby. Soon, she walks through the front doors."
    $ scene_manager.add_actor(the_person)
    the_person "Hello, so this is it huh?"
    mc.name "This is it. Let me give you a quick tour and I'll show you my office."
    the_person "Great, lead the way."

    $ mc.change_location(office)
    "First you swing by the main offices."
    mc.name "Here is where we do logistics and HR. I've got cubicles setup for doing computer work and supply."
    the_person "I see. Seems like pretty standard stuff in here."
    if mc.business.hr_director == sarah:
        $ scene_manager.add_actor(sarah, display_transform = character_center_flipped)
        "[sarah.possessive_title!c] approaches you as you talk, curious about the woman she's never met before."
        mc.name "This is [sarah.fname]. She is my HR director. [sarah.fname] this is [the_person.name]. I've hired her as a consultant to look through my finances."
        sarah "Ah, hello [the_person.fname], it is a pleasure to meet you."
        the_person "Nice to meet you as well."
        sarah "I imagine we'll be working together on payroll related work. I look forward to working with you soon."
        "She steps back to her previous work."
        $ scene_manager.remove_actor(sarah)

    $ mc.change_location(m_division)
    "You step out from the main offices and into marketing."
    mc.name "And here is where marketing does their work."
    mc.name "We have professional video conferencing setups in here to help make sales, as well as promotional materials."

    if mc.business.company_model == alexia:
        $ scene_manager.add_actor(alexia, display_transform = character_left_flipped, position = "sitting")
        "To the side, [alexia.possessive_title] appears to be in the middle of a video call, but when she sees you she gives you a quick wave."
        mc.name "That is [alexia.fname]. She is currently the company model, helping us with most of the promotional materials."
        the_person "I can see why, she's beautiful."
        $ scene_manager.remove_actor(alexia)

    $ mc.change_location(rd_division)
    "You continue along the tour to Research and Development."
    mc.name "Alright, in here is where the magic happens. Research and Development is the key to a successful operation here, as we create and test new lines of drugs."

    if mc.business.head_researcher == stephanie:
        $ scene_manager.add_actor(stephanie, display_transform = character_center_flipped, position = "sitting")
        "You walk along until you come to [stephanie.possessive_title]'s desk. She is working hard, and doesn't notice you until you are right behind her."
        stephanie "Oh! Oh hey, I didn't hear you walk up. Who is this?"
        mc.name "[stephanie.fname], this is [the_person.name]. I'm showing her around. I've hired her to do some financial consulting."
        stephanie "Nice to meet you."
        mc.name "[the_person.name], this is [stephanie.fname], my lead researcher. She oversees the whole department."
        the_person "Wow, that is amazing. Nice to meet you."
        $ scene_manager.remove_actor(stephanie)

    $ mc.change_location(p_division)
    "The tour continues to production."
    mc.name "Alright, in here is the lab where we synthesize all the serums and drugs that we produce."
    mc.name "Everything is done in small batches, due to the precarious nature of the synthesis process."

    if mc.business.prod_assistant == ashley:
        $ scene_manager.add_actor(ashley, display_transform = character_center_flipped)
        "[ashley.possessive_title!c] is talking to another employee when you walk in, but notices you and walks over to you."
        ashley "Hey there, another employee for production? We could use some help down here."
        mc.name "Ah, [ashley.fname], this is [the_person.name]. I've actually hired her to do some financial consulting, but I wanted to show her around first."
        ashley "Ahh, I should have guessed. Her hands are too clean to be down here anyway."
        mc.name "[the_person.name], this is [ashley.fname]. She manages the production department."
        the_person "I see. Pleasure to meet you [ashley.fname]."
        "Ashley just nods, then turns to walk back to her previous conversation."
        $ scene_manager.remove_actor(ashley)
    $ mc.change_location(ceo_office)
    "You finish the tour when you enter your office."
    if mom.is_employee:
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
        "When you enter your office, [mom.possessive_title] greets you and [aunt.fname]."
        mom "Ah good day sir and… ummm… Becky?"
        the_person "Jen? I… what are you doing here?"
        "(Make an interesting conversation here)"
    else:
        "You enter your office and close door. You are now alone with [the_person.possessive_title]."

    mc.name "So… what do you think?"
    the_person "I think you have an impressive operation here…"
    mc.name "Thanks."
    the_person "But… why are there so many women? I mean… are there ANY other men here?"
    mc.name "At this time I only employ women. This is a necessity due to the nature of the serums we are creating."
    the_person "That… doesn't make any sense. What does that have to do with it?"
    mc.name "That isn't a concern for you, I am just looking for your financial expertise."
    "Your aunt gives a humph, then sighs."
    the_person "Right… okay, let me see what you have."
    "You sit down at your desk and log in, pulling up programs containing your financial records."
    mc.name "Anything you need should be available on these programs."
    the_person "Okay. With the size of this place… it might take me a while to sort through everything."
    $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_left_flipped)
    "She sits down at your computer. You put your hands on her shoulders."
    mc.name "Of course. I'll leave you to it, I prefer to be hands on with my employees anyway."
    the_person "Yeah I bet…"
    mc.name "Let me know if you need any help finding anything, or have questions about my records."
    the_person "Sounds good."
    $ mc.change_location(office)
    $ scene_manager.clear_scene()
    "You step away from your desk, and then exit your office."
    "You decide to get back to your business and just let [the_person.title] work her magic alone for a while."
    $ aunt.progress.obedience_step = 3
    $ add_aunt_cpa_first_day_finish_action()
    $ add_aunt_cpa_job_for_business(ceo_office) # set CPA job to CEO office for first day
    return

label aunt_cpa_first_day_finish_label():
    $ the_person = aunt
    $ scene_manager = Scene()
    if mc.is_at_office:
        "You get a text from [the_person.fname], asking you to meet her in your office."
    else:
        "Since it was [the_person.fname]'s first day, you text her to meet you in your office."
    $ mc.change_location(ceo_office)
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_left_flipped)
    "You walk in and see her seated at your desk."
    "For a second you worry that she may have taken the opportunity to learn more about this place than you are ready for her to know."
    the_person "Alright, I'm done with the audit. That was… a LOT of work."
    mc.name "I'm sure it was. Find anything?"
    the_person "Yes, there is a lot to go over."
    "You sit down across from her as she begins."
    the_person "First off, your payroll software is ANCIENT. For real the 90's called and asked for their quickbooks back."
    the_person "The bank is charging you ridiculous fees to interface with it…"
    "...............      Several minutes later     ..............."
    the_person "… so yeah, they are taking you to the cleaners. This could all get streamlined."
    the_person "I estimate when finished, it would increase your overall efficiency considerably, while lowering your operating costs."
    mc.name "Wow. You're amazing. And… are you willing to tackle all these issues?"
    the_person "Of course. That is why you brought me in, right?"
    mc.name "Right."
    the_person "I can handle all of it, but this isn't a one time consulting thing… I'll need a chunk of time every week to work on it."
    mc.name "Why don't you just come back every Tuesday? I'll get you set up with a private office space near marketing."
    mc.name "It sounds like the cost savings would be well worth it."
    the_person "Okay. I'll plan on it. It'll take me a bit to secure the licensing needed for new accounting software anyway."
    the_person "I'll come back next Tuesday and I'll be ready for work!"
    mc.name "Great! I really appreciate this [the_person.title]. It means a lot to have someone I can trust here to help out."
    the_person "Yeah. I wasn't sure how this would go, but I'm actually really excited to be here. I feel like I can really make a difference."
    $ scene_manager.update_actor(the_person, position = "default", display_transform = character_right)
    "She stands up and you walk her to the door to your office."
    the_person "Alright, I might see you before then, but if not, see you next week!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    mc.name "Goodbye!"
    $ scene_manager.clear_scene()
    "[the_person.possessive_title!c] steps out of your office and you close the door."
    "She will now work at your business every Tuesday."
    "You go over all the things she said she would help out with."
    "While her effect on individual areas is fairly small, the total package should make a big impact on your business."
    "You now get an operational discount based on [the_person.title]'s intelligence, and a maximum efficiency bonus based on her Charisma."
    "In addition, having her at your business will almost certainly open up new opportunities to spend 'quality time' with her."
    $ add_aunt_money_launder_offer_action()
    $ aunt.progress.obedience_step = 4
    $ add_aunt_cpa_job_for_business(m_division)  # switch CPA job to marketing div location
    return

label aunt_money_launder_offer_label(): #140
    $ the_person = aunt
    "In this label, [the_person.title] presents MC with options for laundering money. MC can accept or refuse."
    "IF MC accepts, we gain improved attention drain, but possibly at some other consequence."
    $ aunt.progress.obedience_step = 5
    return

label aunt_money_launder_reverse_offer_label(): #160
    $ the_person = aunt
    "In this label, we ask [the_person.title] to purposely cook the books to look MORE suspicious, drawing the ire of the Penelope"
    "We discover they are actually former affection rivals for you uncle... she regrets the situation but refers to her as a 'total bitch'"
    "She decides to swing by the next morning to be there for her inevitable surprise inspection."
    $ aunt.progress.obedience_step = 6
    return
