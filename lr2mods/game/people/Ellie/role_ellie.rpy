#Ellie's story is a coming of age story (even though she's 24) because she grew up in a strict religious family.
#Ellie has ZERO experience, and therefore ZERO sex opinions.
#During her story, MC will have choices in her initial sexual encounters. MC choices will shape her opinions
#E.G., if you make her fingering scene good, she loves getting fingered. If you degrade her during, she hates it.
#Good ending to scenes should be available to 90% of players based on stats. don't make them too restrictive.
#GOOD OPTIONS ALWAYS OPEN WITH LOVE. She is supposed to be your souther belle sweetheart.
#All sexual options are opened during story. EG she is completely frigid until players progress with her.
#Progressing with Ellie may also open up new nanobot improvements.
#Uses the date override code from the old casual sex code to modify her dates so MC can't go back to her place until appropriate point in the story.


# def ellie_grope_followup_requirement():
#     if mc.is_at_office and mc.business.is_open_for_business:
#         return True
#     return False
#

# ellie_grope_followup = Action("Ellie confronts you", ellie_grope_followup_requirement, "ellie_grope_followup_label")
#
# def ellie_turned_on_while_working_requirement():
#     return False
# ellie_turned_on_while_working = Action("Ellie gets horny", ellie_turned_on_while_working_requirement, "ellie_turned_on_while_working_label")    #NOTE: This should probably get moved to a separate crisis file

label ellie_start_intro_note_label():
    $ the_person = mc.business.head_researcher
    "You get an email notification on your phone. Normally you would brush something like this off as spam, but the subject line has your name in it."
    "You open it up and are surprised by what you read. It is short and to the point."
    "???" "I know what your company is doing with the nanobots, and I'll go public with it if you don't meet my demands."
    "???" "Meet me tomorrow night in the alley between 3rd and 5th street downtown. Come alone, and bring cash."
    "Well that's not good. That sounds very not good. You find yourself panicking for a moment."
    "You take a deep breath. You should get with [the_person.possessive_title]. You quickly page her to meet you in your office."
    if not mc.is_at(ceo_office):
        $ mc.change_location(ceo_office)
    "You sit at your desk and anxiously wait for her to meet you."
    $ the_person.draw_person()
    the_person "Hey, you wanted to see me?"
    mc.name "Close the door and come sit down."
    $ the_person.draw_person(position = "sitting")
    "She slides quietly into the chair."
    the_person "Boy, you sure are sombre... something on your mind?"
    mc.name "You could say that..."
    "You pull up the email and show it to her."
    "She is just as surprised as you."
    the_person "Wow... fuck... okay. What can I do to help?"
    mc.name "So, here is what I am thinking. Across from the alley is a bar where you can get on the roof fairly easily."
    mc.name "Can you come with me, but hide up on the roof with like... a camera or binoculars or something? Just watch while I deal with this."
    the_person "Yeah. I can do that. I think I know where you are talking about."
    mc.name "I'll pull out some cash the day of and be ready. Although the email doesn't even say how much cash to bring."
    the_person "Yeah... it's a little ambiguous... But I can do that."
    "You spend some time in your office with [the_person.title], making a quick and dirty plan for how to deal with the blackmail threat."
    mc.name "Alright, it's a plan. I won't meet with you tomorrow night, in case we are being watched or tracked, but it's a plan at least."
    the_person "Ok... We'll talk then."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] gets up and leaves your office. This is a precarious situation, and you can't help but worry about it."
    $ clear_scene()
    $ mc.location.show_background()
    $ add_ellie_meet_ellie_intro_action()
    return

label ellie_meet_ellie_intro_label():
    $ the_person = mc.business.head_researcher
    "As night falls, you make your way downtown. Tonight you are meeting with your mysterious blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.turn_lights_off()
    "You text [the_person.possessive_title] to make sure she is still going to be there."
    $ mc.start_text_convo(the_person)
    mc.name "In the alley between 3rd and 5th. Did you manage to find a good vantage point?"
    the_person "Sure did. I don't see anyone yet, and I brought a taser, you know, just in case."
    $ mc.end_text_convo()
    "You have no idea how organized this person or group is, but you doubt that if things turn sour a taser will make much of a difference. You decide to keep that to yourself, though."
    "Hopefully she will go unnoticed if the blackmailer decides to have reinforcements of his own."
    "The blackmail note said to bring cash... But not how much. You pulled some strings at the bank and got $1000 in 20s, hopefully that will be enough."
    "Your business is just getting off the ground, so you really don't have the cash to handle a huge demand."
    "Eventually, the time comes, so you head down the alley. As you hit the halfway mark, a shadowy figure emerges from behind a dumpster."
    $ ellie.change_location(downtown)
    $ ellie.draw_person()
    $ ellie.set_event_day("day_met")
    ellie "That's far enough, stay right there."
    "The first thing you notice is the heavy southern twang in her accent. Secondly, it is heavily feminine. A southern woman is blackmailing you? It catches you completely off guard."
    ellie "You got cash?"
    mc.name "Yeah, although the note failed to mention exactly how much you were expecting."
    ellie "I'm figuring a million dollars in cold hard cash."
    "You pause. She can't be serious? If she knows anything about your business, she has to know you have no way of pulling that kind of liquidity."
    mc.name "I'm sorry, my business is just founded, and I don't have the ability to pull that much, especially on such short notice."
    ellie "Ah lordie help me. Hmm. How about this. You give me some cash now as a show of good faith, and we'll meet again next week and you kin give me the money then."
    ellie "As a fellow criminal, surely you can understand that I got bills to pay."
    "You doubt you will be able to find a million dollars between now and next week, but at least this will give you some time to try and figure things out."
    mc.name "Alright, that's a deal."
    ellie "Alright. For now, let me have a hundred dollars. That'd ought get me through until next week..."
    "This whole conversation is throwing up serious red flags. Is she really just asking a hundred for now? The whole thing reeks of amateurism."
    "You look up and around, trying to see if you see any motion or hint that she may have someone else watching, but don't see anything. You decide to play along for now."
    "You pull out a hundred dollars, being careful not to show the remaining bills you have with you, and extend your hand with them."
    $ mc.business.change_funds(-100)
    "She slowly walks forward and takes her money from you. The alley is dark, but is that red hair? She quickly pulls away."
    ellie "Same time next week."
    "The mysterious blackmailer turns and quickly leaves the alley. You stand there observing her until she turns the corner, when you turn around and leave the alley."
    $ clear_scene()
    "Once you are a safe distance away from the alley, you pull out your phone and text [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    mc.name "Hey, meet me at the bar. We have a lot to talk about."
    the_person "Okay, see you there."
    $ mc.end_text_convo()
    $ mc.location.turn_lights_on()
    $ mc.change_location(downtown_bar)
    $ the_person.change_location(downtown_bar)
    "You grab a secluded table away from the crowd around the bar with [the_person.title]."
    $ the_person.draw_person(position = "sitting")
    the_person "So, how'd it go?"
    mc.name "Confusing, to be honest. You see anything from where you were at?"
    the_person "Not much, to be honest. I could tell it was a woman, but I didn't see anyone else and couldn't make out much about her."
    mc.name "Well, first thing, she had a heavy southern accent. She could have been faking it, but I doubt it. The whole thing felt... Like she was an amateur, to be honest."
    the_person "Why do you say that?"
    mc.name "Well, she really seemed to have no idea how much money to ask for, so she just said she needed a million dollars."
    the_person "Wow, there's no way you could make a ransom like that, at least as far as I know."
    mc.name "Right? And then when I said I didn't have that kind of money, she told me had she had bills to pay?"
    mc.name "So she just asked for a hundred dollars as a show of good faith, and to meet again next week..."
    the_person "Wow... That's so weird."
    mc.name "It was hard to see, the alley was so dark but... When she took the money from me... I think she's a redhead."
    the_person "Ahhh, a southern redhead? Of all the luck you have, your blackmailer happens to be a southern redhead? Did she have another obvious feature? Missing a leg perhaps?"
    "Your head researcher is joking with you, but you can't help but laugh. This has to be a setup... Right? How many southern redheads could possibly live in this town?"
    mc.name "Nothing else that I noticed. But the bills to pay thing bugs me."
    the_person "You think she's unemployed maybe?"
    mc.name "Maybe. I don't know. Up for helping me out with some research?"
    the_person "Oi. I guess I can do that. I'll do some searching on the internet this weekend and see if anything comes up."
    mc.name "Thanks. I appreciate it."
    "You decide you've had quite enough adventure for one night, so you decide to head home."
    mc.name "Thanks for your help [the_person.title]. I appreciate it."
    $ the_person.change_happiness(2)
    the_person "Well, I admit, I feel partially responsible since I was the one to bring in the nanobots in the first place."
    mc.name "I don't know why, but I feel a lot better about this whole thing. If we can figure out who she is, maybe we can come up with an alternative solution."
    the_person "Err... you don't mean like... 'taking care of her' do you?"
    mc.name "Of course not! But there may be other things we can do about this, I think."
    "With your business concluded, you and [the_person.possessive_title] part ways."
    $ mc.change_location(bedroom)
    $ clear_scene()
    $ add_ellie_head_researcher_halfway_intro_action()
    return

label ellie_head_researcher_halfway_intro_label():
    $ the_person = mc.business.head_researcher
    if the_person is None:
        $ add_ellie_unnecessary_payment_action()
        return

    "You feel your phone vibrate in your pocket. It's [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "I'm a genius. Meet me in your office!"
    if not mc.is_at(ceo_office):
        mc.name "I'll be right there."
    else:
        mc.name "I'll be waiting for you."
    $ mc.end_text_convo()
    if not mc.is_at(ceo_office):
        $ mc.change_location(ceo_office)
        $ the_person.draw_person(position = "sitting")
        "You step into your office, as you do, you see [the_person.title] sitting behind your desk."
        "You close the door and walk over."
    else:
        "[the_person.title] steps into your office and sits down."
        $ the_person.draw_person(position = "sitting")
    mc.name "What is it?"
    the_person "Well, following a hunch, I got in touch with the contact I had that got us the nanobots and the software in the first place."
    the_person "It was just too weird that this girl had so much info about them."
    the_person "I gave him a description of the blackmailer, and he finally got back to me this morning."
    the_person "The company launched an investigation trying to figure out who leaked the bots, but they got the wrong person."
    the_person "The company came down hard on a relatively new person. A woman they had hired about a year ago. A fresh computer science college graduate from University of Alabama..."
    mc.name "Ahhhhh."
    the_person "He sent me her basic details..."
    "[the_person.possessive_title!c] hands you a dossier she has put together on this person. The first thing you notice is her red hair."
    the_person "[ellie.name] [ellie.last_name]. Redhead, southern computer expert."
    mc.name "It's perfect. What happened with her employer?"
    the_person "She got fired. The kicker is, she signed a 5 year non-compete contract when she got hired, and so the company threatened her with a lawsuit if she tries to get another job in her field."
    mc.name "Wow... So now here she is, far away from home, and no way to pay the bills."
    the_person "That's right!"
    "You feel conflicted about this. Surely, this is the girl that is blackmailing you... but you are also partially responsible for it, having acquired the nanobots in the first place."
    "When you look at [the_person.title], she is looking at you funny."
    the_person "So... you're going to try and help her... aren't you?"
    mc.name "I mean... I am kind of responsible for her getting fired..."
    the_person "Maybe. But how do you want to help? You can't just give her easy money every week."
    mc.name "No. But that non-compete... Those are usually for specific position descriptions, right?"
    the_person "Yeah, usually..."
    mc.name "Maybe we could hire her? Having a computer person could be seriously handy around here... but we could make her official position something that isn't obvious."
    the_person "That might work actually."
    mc.name "If this other company ever calls us, we could just say she works in HR, for example. She's a college graduate, I'm sure she could handle that work too."
    the_person "Hey, you don't have to convince me. It would be nice to have a tech person around here for sure though."
    mc.name "Alright. Next time I meet with her, I'll consider trying to hire her. If nothing else, maybe I can at least scare her off."
    the_person "Okay. Let me know if there is anything else I can help out with, [the_person.mc_title]!"
    $ clear_scene()
    "[the_person.possessive_title!c] gets up and leaves you alone in your office."
    "You meet again with [ellie.name] on Thursday night. You feel like you could definitely hire her."
    "WARNING: If you want to hire [ellie.name], make sure you have an open employee position! You may miss the opportunity to hire her if you don't!"
    $ add_ellie_end_blackmail_action()
    $ mc.location.show_background()
    return

label ellie_unnecessary_payment_label():    #Use this scene each week if MC can't find out info on Ellie for some reason (head researcher fired, etc)
    $ the_person = ellie
    "As night falls, you make your way downtown. Tonight you are meeting with your blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.turn_lights_off()
    "The time comes so you head for the alley. As you approach, you hear the southern twang of her accent as she steps from the shadows."
    $ the_person.change_location(downtown)
    $ the_person.draw_person()
    the_person "'Ey. Got the money?"
    "You stop."
    if ellie.event_triggers_dict.get("blackmail_stage", 0) == 0:    #First time
        mc.name "I have some money... but a million dollars is a lot of money. My business doesn't pull that much in a year."
        the_person "Sounds like you have a problem then. I want my money."
        mc.name "What are you going to do with a million dollars, anyway? How are you going to keep it secret from the IRS?"
        the_person "You let me worry about that hun."
        mc.name "Well, for now, I have the same amount as last week. I'll keep working on it, but it's going to take me a while to get that much money."
        the_person "Work on it. I'll be watching you."
        "You hand the mysterious blackmailer $100 again. She turns and walks away."
        $ mc.business.change_funds(-100)
        $ ellie.event_triggers_dict["blackmail_stage"] = 1
        $ clear_scene()
        $ add_ellie_unnecessary_payment_action()
    elif ellie.event_triggers_dict.get("blackmail_stage", 0) == 1:
        mc.name "I'm still working on the million dollars. For today I have the same amount as last time."
        the_person "You are testing my patience. How am I supposed to live off of $100 a week? It's your fault I got fired in the first place!"
        "This is an interesting piece of information."
        mc.name "My fault? What did I do to get you fired?"
        the_person "Those damn nanobots..."
        "She suddenly realises she is giving away too much information."
        the_person "Forget it. Give me the money you got. Don't make me wait much longer for my money, or the good Lord help you..."
        "You hand the mysterious blackmailer $100 again. She turns and walks away."
        $ mc.business.change_funds(-100)
        $ ellie.event_triggers_dict["blackmail_stage"] = 2
        $ clear_scene()
        $ add_ellie_unnecessary_payment_action()
    elif ellie.event_triggers_dict.get("blackmail_stage", 0) >= 2:
        mc.name "I've almost got the million dollars. For today I have the same amount as last time."
        the_person "I'm starting to think you are just dragging this out. I'm not going to wait forever while you get the money!"
        the_person "Being jobless sucks. My family has been asking questions about what I'm doing out here."
        mc.name "Why don't you just get another job?"
        the_person "Lordie knows I've tried! But they told me I got a non-compete..."
        "Your blackmailer gives away a bit more information. You feel like this might finally be the final piece you need to figure out her identity."
        the_person "What do you care anyway? Bunch of godless drug makers. Just give me what you got, and next week you better have it all or I'm going straight to the police!"
        "You hand the mysterious blackmailer $100 again. She turns and walks away."
        $ mc.business.change_funds(-100)
        $ ellie.event_triggers_dict["blackmail_stage"] = 3
        $ clear_scene()
        $ add_ellie_self_research_identity_action()

    $ mc.location.turn_lights_on()
    return

label ellie_self_research_identity_label():
    "Suddenly, you make a connection in your head."
    "The strange southern woman who is blackmailing you. She recently got fired, and blames you. She must work at the company you stole the nanobots from!"
    "Unfortunately, your old head researcher isn't available anymore, but you think you can remember the name of the company."
    "You run a search for local job applications looking for work, with that company as a previous employer."
    "There are a couple that come up, but one specifically immediately jumps out at you. Her picture is perfect."
    $ ellie.draw_person()
    "[ellie.name] [ellie.last_name]. Graduate of University of Alabama in Computer Science. Worked at the other company for 6 months. Looking for non–IT–related work."
    "It HAS to be her! It's just too perfect."
    "You feel conflicted about this. Surely, this is the girl that is blackmailing you... but you are also partially responsible for it, having acquired the nanobots in the first place."
    "Her previous employer must have blamed her for the leak. Now they are keeping her from finding work in her field of study with a non-compete agreement."
    "You think to yourself... she got information on you pretty easily. Your IT setup here is okay... but it could definitely be improved if you brought an expert on board."
    "Maybe you should hire her?"
    "You meet again with [ellie.name] on Thursday night. You feel like you could definitely hire her."
    "WARNING: If you want to hire [ellie.name], make sure you have an open employee position! You may miss the opportunity to hire her if you don't!"
    $ add_ellie_end_blackmail_action()
    return

label ellie_end_blackmail_label():
    $ the_person = ellie
    "As night falls, you make your way downtown. Tonight you are meeting with your blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.turn_lights_off()
    "The time comes so you head for the alley. As you approach, you hear the southern twang of her accent as she steps from the shadows."
    $ the_person.change_location(downtown)
    $ the_person.draw_person()
    the_person "'Ey. Got the money?"
    "You stop."
    mc.name "I'm going to be honest. I don't have any money with me [ellie.name] [ellie.last_name]."
    "She gasps when she hears her full name."
    the_person "That's... Oh heavens..."
    mc.name "That's right. I figured out who you are. I did my research. I found out who you used to work for. I found out what happened. That you got fired."
    $ the_person.draw_person(emotion = "angry")
    "She hesitates for a moment, then gets angry."
    the_person "That was it! I'd finally found a good job, I was working hard..."
    $ the_person.draw_person(emotion = "sad")
    "Suddenly, she breaks down crying."
    the_person "Then... they told me that I'd been stealing! That I leaked company secrets! Me!"
    the_person "They fired me... but it was you! And now I can't find another job anywhere! Anytime I give my work history, I get an instant \"no, thanks\" from any employer."
    "She seems ready to chat. Do you want to try and hire her?"
    menu:
        "Hire Her":
            pass
        "Scare her off\n{menu_yellow}Ends story line{/menu_yellow}":
            "She is so emotional. You can't imagine her being a good fit for your company now."
            mc.name "Now listen carefully..."
            mc.name "I think it's time for you to move back to that little town you came from."
            mc.name "I've got enough evidence to get you locked up for a long time."
            the_person "Please Sir, don't...I will go back home and work on my parents farm."
            mc.name "Make sure you do, if I ever see you again, I will make certain you will regret it."
            the_person "Don't worry, you will never see me again."
            $ the_person.draw_person(position = "walking_away")
            "You watch her as she turns around and walks away."
            # restore default lighting before exit label
            $ the_person.remove_person_from_game()
            $ clear_scene()
            "You are certain she will keep her promise and decide to go home."
            $ mc.location.turn_lights_on()
            $ mc.change_location(bedroom)
            $ add_it_director_alt_intro_action()
            return
    mc.name "I get it. You just want to work, and something in your field."
    the_person "I... I just moved here a year ago... I just want to do my family proud..."
    mc.name "What if you came and worked for me?"
    "She startles. She clearly had not expected this at all."
    the_person "Me? You... after I blackmailed you and..."
    mc.name "How did you get information on my company anyway? About the nanobots?"
    the_person "Oh gee, finding your involvement was the hard part. Your password security is nonexistent. I used a dictionary attack and accessed [stephanie.fname]'s emails using those stolen passwords." #BB- Even dated servers would have some kind of firewall. Having poor password policies is much more common and exploitable
    mc.name "I could really use someone with your talents to help me with stuff like that."
    the_person "I could help... but I can't... I signed a non-compete..."
    mc.name "I run a small company. We all know each other. I could make your official position be in HR, but you could run IT projects for me on the side. Your prior employer doesn't need to know."
    mc.name "I'll match your previous salary plus ten percent. And if you decide to move on, I'll give you a proper reference."
    "She seems sceptical, but agrees."
    the_person "Okay... Let's say I decide I want to try it out."
    mc.name "Come on out to the business tomorrow morning. I'll show you around, give you a chance to settle in, and then you can think about it over the weekend."
    the_person "Okay mister. I'll come out tomorrow and you can show me the ropes."
    mc.name "That's all I ask. I think you'll fit right in."
    $ add_ellie_work_welcome_action()
    "You exchange some information with [the_person.title]. You feel pretty certain she'll decide to stick around."
    $ mc.business.event_triggers_dict["previous_it"] = True
    $ mc.location.turn_lights_on()
    $ mc.change_location(bedroom)
    return

label ellie_work_welcome_label():
    $ the_person = ellie
    "You head into work a bit early. You are meeting [the_person.title], who you are hoping will be your new IT girl."
    $ mc.change_location(ceo_office)
    "Shortly after you arrive, you hear a knock on your office door."
    mc.name "Come in."
    $ the_person.draw_person()
    the_person "Hello. I'm here..."
    mc.name "[the_person.title]! I'm glad you came. I wasn't sure if you would show up or not. Please come in."
    "Sheepishly, [the_person.title] steps inside your office, walks over and sits down across from you at your desk."
    $ the_person.draw_person(position = "sitting")
    mc.name "So, basically, this is a small company, as you know. I'd love to bring you onboard and have you primarily running cybersecurity / IT projects."
    mc.name "However, I'm not sure that, due to the size of the company, I'll be able to keep you busy full time with those projects, so when you have downtime, I'll assign you to the Research department."
    mc.name "We'll make the Research department your official job position, with the other projects on the side. How does that sound?"
    the_person "Well... that sounds okay, I guess. What kind of security policies do you currently have in place?"
    mc.name "Ah, well... we use the anti-virus software that came with the computers..." #BB- I changed it to this because it seems like something someone unfamiliar with network security would say
    the_person "Lordie. You don't have any kind of security measures in place?"
    mc.name "That's just something we haven't given much thought..." #BB- Network security would be an oversight for a small business
    the_person "Alright. Tell you what, I'll look things over today and I'll see what I can do. I'll do some research over the weekend and on Monday I'll let you know what I decide."
    mc.name "Deal! Why don't we get your onboarding paperwork complete?"
    the_person "Okay."
    $ the_person.draw_person(position = "sitting")
    "You sit down at your desk, filling out some paperwork and getting her officially hired by the company."
    $ add_ellie_work_welcome_monday_action()
    call initial_set_duties_label(the_person) from _call_initial_set_duties_ellie_work_welcome
    mc.name "Alright, that's all, then I'll see you next Monday, welcome aboard [the_person.title]."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] gets up and leaves your office."
    $ clear_scene()
    return

label ellie_work_welcome_monday_label():
    $ the_person = ellie
    $ mc.change_location(ceo_office)
    "When you arrive at work on Monday morning, you head to your office."
    "Shortly after you arrive, you hear a knock on your office door. It's [the_person.title]."
    $ the_person.draw_person()
    the_person "Hello. I've been looking at things over the weekend like I told you I would."
    mc.name "Great. Have a seat."
    $ the_person.draw_person(position = "sitting")
    the_person "Alright. So, your cybersecurity is basically nonexistent. Or, was, I should say."
    mc.name "Oh?"
    the_person "Before I left Friday, I was looking at login logs for your network... the only outside connections were from me, a few weeks ago, you know, when I got the access originally..." #Another reason to switch from no firewall to poor password - the servers are auditing events which AFAIK is not enabled by default
    the_person "So I set up a quick security layer with VPN access so I could work on it from home over the weekend..."
    mc.name "That's... good?"
    the_person "Well, it means it won't be as easy for someone to log in to your network with bogus credentials like I did anymore..."
    the_person "Anyways, I spent the weekend looking at your IT systems. They are... rather outdated?"
    mc.name "Umm, honestly when I bought the place there were some systems already in place so I just decided to use those..."
    the_person "Lordie... Okay well I made a short list of some new programs I could set up for you that will help in each department."
    the_person "None of them will be miracles, but you should see decent efficiency increases. Each one will probably take me about a week to set up."
    mc.name "That sounds great."
    the_person "The other thing I looked at..."
    "She lowers her voice a little."
    the_person "I... I get it that you are using the nanobots for... fornication..."
    the_person "So I looked through those programs a bit. There are definitely some gains to be made in those programs."
    the_person "I'm not saying I agree with what you are doing with them, but the programs themselves look like you just slapped them together over a weekend or something."
    mc.name "That's... basically what we did. The head researcher had a contact who put together the programs for us over a weekend..."
    the_person "You... bless your hearts. You are lucky he didn't put in some kinda back door or tracking program in there. He was probably just lazy."
    the_person "Anyway, I think I can improve those more for you, though if I'm honest, these bots are cutting edge tech. Some improvements might need more research into the bots themselves first."
    $ purchase_policy(it_director_creation_policy, ignore_cost = True)
    $ mc.business.hire_IT_director(the_person)
    the_person "First round of those would also take me about a week. After that, I'm not sure."
    the_person "So, here's the first set of things I can work on. Take a look and let me know if you want me to start on something."
    call screen it_project_screen()
    if mc.business.current_IT_project:
        the_person "Okay, I have a starting point. If you decide to have me work on something else just come talk to me."
    else:
        the_person "Alright well, when you decide what you want me to work on, let me know, I'll be in research."
    the_person "You might also consider, I was chatting with some of the other girls in the research department."
    the_person "If you need an IT project done quickly, some of them might be able to help me out to get things done a bit quicker."
    the_person "But it would be extra work, so the less experienced employees may not have time."
    mc.name "I'll keep that in mind. Thank you."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] gets up and starts to walk away. You have now unlocked IT projects!"
    $ clear_scene()
    $ the_person.change_location(rd_division)
    "Talk to your IT director to change projects when she is at work. If she is working on developing a new project, she will be in the Research Department."
    "You have also unlocked the IT Work duty for the research department. If assigned, an employee will help work on IT projects."
    $ add_ellie_never_been_kissed_action()
    return

# label ellie_grope_followup_label():
#     $ the_person = ellie
#     "You are going about your work, when [the_person.possessive_title] finds you."
#     $ the_person.draw_person()
#     if not mc.is_at(ceo_office):
#         the_person "Hey, can we talk somewhere private?"
#         mc.name "Sure."
#         $ mc.change_location(ceo_office)
#         "You take her to your office and close the door. You offer to let her sit down but she declines."
#     the_person "I'll keep this short, I just didn't want any other girls to hear this..."
#     the_person "I'm sorry for... yah know... peeing my pants like that..."
#     $ the_person.draw_person(emotion = "angry")
#     the_person "But to be fair, ya'll didn't tell me something like that could happen!"
#     mc.name "[the_person.title]... did it feel good? When that happened?"
#     the_person "I... I guess so... yeah it was nice..."
#     mc.name "[the_person.title]... I don't think you peed yourself, I think you just had an orgasm."
#     the_person "I had a... a what now?"
#     mc.name "[the_person.title], have you ever masturbated?"
#     the_person "What the hecking kind of question is that? Of course not, that's for unsavoury folk."
#     $ the_person.draw_person(emotion = "sad")
#     "You sigh. She is struggling in her brain to overcome her sexual desires, and being exposed to your serums is starting to overwhelm her."
#     "She is making progress, but you can tell it is going to be a long road before you can fully corrupt her."
#     mc.name "I tell you what. I'm going to email you some sexual health websites. I want you to do some research on things this weekend."
#     mc.name "With the work we do here on serums, it is important that you have a good understanding what is actually going on with your body."
#     the_person "You're saying... this is a work assignment?"
#     mc.name "That's right. It will help you do your job better."
#     mc.name "I'm not saying you have to masturbate, but getting to know your body better might help you better understand what we are trying to achieve here, in general."
#     the_person "Okay, I'll take a look."
#     $ clear_scene()
#     "[the_person.possessive_title!c] leaves your office. You take a few minutes and email her some links to positive sex health websites and information."
#     $ mc.business.add_mandatory_morning_crisis(ellie_text_message_apology)
#     return
#
# #Love Events
#
#

#
# #Sluttiness EVents
#
# init -1 python:
#
#
#     def ellie_turned_on_while_working_requirement():
#         return False
#
#
#
