# Kaya's love route starts her whole setup. On a first date, we learn about her education and what she is trying to do.
# MC get's her in touch with Nora who brings her to the local university.
# In the 40 event, we hire her for work at MC's business and she begins her work there.
# At 60, we discover her stances on birth control if we haven't already. Let's us knock her up at will
# at 80, we start a small event series where we set out to cure her mother of her illness. Completing this quest makes her wholly devoted to MC (max obedience and Love)

label kaya_ask_out_reject_label(the_person):    #20
    #Kaya rework has her no longer gated behind Alexia. We still gate her one additional week, gives players a chance to talk her up and get her love stat up via small talk.
    $ the_person.draw_person()

    "You really want to get to know this girl better, so you decide to keep trying."
    mc.name "What about after work? Any plans for after work?"
    the_person "Me? Oh I'll be hitting the books. I've got some studying to do."
    mc.name "I see. Want to go out and get a couple drinks instead?"
    the_person "WAIT… you mean… like a date or something?"
    mc.name "Probably a date, yeah, but the 'or something' could be interesting too."
    "She smiles, but suddenly groans."
    the_person "Ahhhh, I… I want to."
    mc.name "It's okay. I'll pay for the drinks."
    the_person "Drinks? No, it isn't about the money."
    mc.name "Oh…"
    the_person "Stop! Don't give me the long face. I have finals this week… I REALLY need to be studying!"
    mc.name "Finals? What like at the university?"
    the_person "Yeah!"
    mc.name "That's weird. My sister goes there, but they aren't running finals for her classes for a while."
    the_person "Oh, I'm… I'm kind of on an accelerated program…"
    the_person "I… want to go out with you. You seem really funny! But I… I really REALLY need to study this week."
    mc.name "It's okay, we don't have to…"
    the_person "Come back? Like next weekend!"
    the_person "I promise, this is a rain check. Please?"
    "She seems pretty sincere. And you wouldn't want to distract this beautiful girl from her studies. Not yet anyway…"
    mc.name "I'm pretty busy, but I'll try to stop by next week."
    the_person "Okay! I'm really sorry… I'm good for it I swear!"
    "You got your coffee and sit down."
    "Well, for now you suppose all you can do is wait."

    $ add_kaya_first_date_action()
    $ kaya.progress.love_step = 1
    return

label kaya_first_date_label(the_person):
    #Her actual first love label. One week after the initial rejection.
    $ the_person.draw_person()
    "You step into the coffee shop. Kaya is working the counter and sees you when you walk in."
    the_person "Ah! It's you!"
    "She seems very excited to see you. You step over to the counter."
    the_person "This is perfect, I was hoping you would swing by! I'm off work at 8!"
    "Wow, it seems she really was too preoccupied to go out last week."
    mc.name "Nice, mind if I get a coffee and just hang out until then?"
    the_person "Sure! It's on the house. I'll have it right out!"
    $ the_person.draw_person(position = "walking_away")
    "She turns and start to make it with her back to you."
    $ the_person.draw_person(position = "standing_doggy")
    "She reaches down and grabs an ingredient from below the counter, giving you the chance to sneak a peek at her backside."
    $ the_person.draw_person(position = the_person.idle_pose)
    "She stands up and hands you a coffee."
    the_person "Here you go."
    mc.name "Thank you. I think I'll step outside and sit on the patio."
    $ clear_scene()

    $ mc.change_location(downtown)
    "You step out the door and sit down at a nearby table. You take the chance to pull out your phone and catch up on some company emails."
    "There's a lot of the usual drama between girls. Your head researcher needs clarification on a recent serum trait you were experimenting with…"
    "You answer her, but she emails you right back with a bunch more questions."
    "You spend a while catching up. It is nice to get some work done in a quiet environment like this…"
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ the_person.draw_person(position = "sitting")
    the_person "Wow, you are really focused on those emails."
    "You suddenly look up. Kaya is sitting across from you at the table."
    mc.name "What?… how long have you been sitting there?"
    the_person "Just a couple of minutes. I saw when I was walking over that you had an email app up and you were typing really fast."
    the_person "Don't worry! I didn't read any of it. I wanted to let you finish, but you were so focused on that thing!"
    mc.name "Ah, I didn't even realise. Don't worry, for the rest of the night this thing can go in my pocket."
    the_person "Aww, if something comes up, I understand. But I appreciate the thought!"
    the_person "So umm… I know you said something about getting drinks tonight but… I actually don't drink."
    mc.name "Oh… I'm sorry…"
    the_person "It's fine. It's not that I have a problem with it, but I'm just 20, and I don't feel comfortable having people do the fake ID or smuggle me drinks or whatever."
    "Wow… she is YOUNG. She seems mature for her age though…"
    mc.name "Well… let me see… we… could… ummm…"
    "You struggle a moment to come up with an alternative..."

    the_person "If you're okay with it, we could still go to a bar. There is a place near the university actually."
    mc.name "Yeah?"
    the_person "Yeah. They have some pool tables there for college students to blow off steam, so they let underage students in."
    mc.name "Pool? As in like, billiards?"
    the_person "Yeah! It is one of my favourite ways to just relax and unwind."
    $ the_person.discover_opinion("billiards")
    the_person "I've always been a bit of a nerd… and learning to play around the board and angle shots is really fun."
    "Wow, this girl keeps getting more and more interesting."

    mc.name "That does sound fun, when you put it like that. But I have to be honest…. I've never played!"
    the_person "What!?! You've never played pool???"
    mc.name "I haven't. Never had reason to I guess."
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly jumps up."

    the_person "Lets go! I got some ones from tips tonight, I'll pay for the table if you buy the sodas!"
    mc.name "Sodas…. Right…"
    $ mc.change_location(downtown_bar)
    "It is a short walk to the place she has in mind, and soon you are stepping inside."
    "She waves to the bartender and he nods as you step up to the counter."
    "???" "Evening. IDs?"
    the_person "Ah, just here to play some pool. Can I have a coke?"
    "The bartender turns to grab a glass and starts to get her order."
    the_person "I see an open table, I'll go reserve it!"
    "[the_person.title] leaves you at the bar."
    $ clear_scene()

    "A minute later, the bartender turns to you."
    "???" "And for you?"
    mc.name "Ah, just a Sprite."
    "Soon, you step away from the bar with the two drinks. "
    $ mc.business.change_funds(-5, stat = "Food and Drinks")
    $ the_person.draw_person(position = "standing_doggy")
    "You bring the drinks over to the pool table where [kaya.possessive_title] appears to be just getting done setting up."

    menu:
        "Read the pool game intro dialogues\n{menu_yellow}If you like reading{/menu_yellow}":
            "A number of pool balls are in a neat triangle and a white ball is sitting opposite of it."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Alright, I just got done setting up! I know it is your first time, so I figure we could play a couple games just to teach you the rules."
            mc.name "Do you normally play for stakes?"
            the_person "Once in a while a pool shark will be around and I'll play for something, but for tonight a couple laid back games sounds great."
            the_person "I'll just teach you the rules as we go. Ready to get started?"
            mc.name "Sure."
            the_person "Alright, the most common variant is called 8 Ball…"
            "She begins walking you through the rules as she walks over to the end of the table."
            $ the_person.draw_person(position = "standing_doggy")
            "She strikes the white ball and sends it crashing through the others. They split wide open and you notice a striped ball goes into a pocket."
            the_person "Alright! So since I sunk a ball first, I will be stripes this game, and you are solids…"
            $ the_person.draw_person(position = the_person.idle_pose)
            "She quickly surveys the table and then lines herself up for another shot."
            $ the_person.draw_person(position = "standing_doggy")
            the_person "So, my goal is to hit in all the striped balls, and you want to hit in all the solid coloured ones, EXCEPT the black 8 ball."
            "She strikes the white ball, that she called the cue ball, again. She easily knocks in another striped ball."
            the_person "Alright… let's see…"
            $ the_person.draw_person(position = the_person.idle_pose)
            "You look at the table, but don't see any obvious plays."
            the_person "Alright, normally I wouldn't try this, but since we are just playing for fun…"
            $ the_person.draw_person(position = "standing_doggy")
            "She points at her stick at the cue ball, but this time it appears that she is hitting it away from all the balls with stripes on them."
            "She strikes the ball and it goes between two of your balls, hits the side wall… then it curves back?"
            "It strikes a striped ball and pushes it close to a corner pocket, but it doesn't quite go in."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Damn, so close. Alright, your turn!"
            "You look at the table. The placing of the cue ball makes it look fairly easy to get a solid in near a corner."
            the_person "Alright, line it up, and make sure you hit the cue ball dead centre…"
            "She shows you the basics of how to handle the pool stick and to line up a shot."
            "You lean over the table and carefully line it up. Here goes nothing."
            "You strike the ball, and somehow, it goes across the table and knocks it in."
            the_person "Oh ho! And on your first try? You might be a natural at this!"
            the_person "Or are you actually a pool shark? Looking to try his luck with me?"
            mc.name "No, I promise I've never played before, but I suspect I have a very capable teacher."
            "You look at the table. No matter how you look at it though, there aren't any clear shots."
            the_person "Alright, time for a real test. See how this ball here is in near this pocket, but one of my balls is in the way?"
            the_person "You can't hit my ball first, but you can bank it off the wall."
            the_person "To make it easier, they put diamonds on the wall at equal distances, so you can determine the proper place on the wall to aim for… see?"
            "You see the idea she is suggesting, and you try to figure out the proper place on the wall to hit…"

            if mc.int > 3:
                "*Intelligence Check Passed*"
                "A quick calculation of the angle in your head, and you line up a shot."
                "You stroke the cueball, and it bounces of the wall and strikes your intended target."
                "It gets close to a pocket, but doesn't quite go in. Still, pretty good for your first attempt, you tell yourself."
                the_person "Hey, that was close! I'm impressed, it usually takes a few tries to get used to the angles of the game!"
                $ the_person.change_love(1, 40)
            else:
                "*Intelligence Check Failed*"
                "You look and get the idea for how to bank the shot, so you give it a try."
                "However, something about the way the balls are positioned aren't quite right. You strike the cueball and it bounces off the side, but doesn't hit your target."
                the_person "Close! Don't worry, it takes some practice to learn how to use the diamonds and to play them correctly."

            the_person "Alright, my turn!"
            $ the_person.draw_person(position = "standing_doggy")
            "[the_person.title] turns and lines up a straight shot. She sinks it easily."
            $ the_person.draw_person(position = the_person.idle_pose)
            "When you look at the table, you see a similar shot as what you attempted earlier. She sees it too."
            the_person "Alright, see here? Now we need to make sure to think about where we want the cue ball to hit in order to angle it into the pocket…"
            $ the_person.draw_person(position = "standing_doggy")
            "She takes several seconds to line up her angled shot, then strikes. The cue ball bounces against the far wall then comes back, driving the ball into a side pocket."
            "Wow… she makes it look easy!"
            "The cue ball is left in a place where she easily lines up another shot. She sinks it easily."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Alright, I don't want to run the table on you. Why don't you go ahead and take another turn?"
            mc.name "Okay… let's see…"
            "You spot what looks to be an easy shot. You slowly line it up. Somehow, you manage to knock it in."
            "You survey the table again. This time, there are no obvious shots, and you don't see any easy way to bank it off of the wall, either."
            the_person "Ah, here we go, this would be a good chance to try what is called a jump shot. See the ball there, straight in line with the corner pocket?"
            mc.name "Yeah, but the 8 ball is in the way."
            the_person "Right. What you can do is, if you strike the cue in just the right way, you can cause it to jump up off the table and clear the 8 ball, jumping it."
            "She spends some time explaining to you how to hit the cue."
            the_person "Alright. You seem like you are good with your hands, give it a try!"
            "Alright… I'll give it a shot…"

            if mc.sex_skills.get("Foreplay", 0) > 3:
                "*Foreplay check passed*"
                "After several seconds of lining up, you attempt a strike similar to the one [the_person.title] described."
                "The cue ball bounces up off the table, and over the 8 ball!"
                "It strikes your target, pushing it close to a pocket but not quite in."
                the_person "Wow! Nice one! That was so close!"
                the_person "It took me a long time to get those down. You must have excellent dexterity..."
                $ the_person.change_slut(1, 40)
            else:
                "*Foreplay check Failed*"
                "After several seconds of lining up, you attempt a strike similar to the one [the_person.title] described."
                "The cue ball bounces, but it doesn't go as far as you were hoping."
                "It strikes the 8 ball and sends it perilously close to a pocket, but thankfully it doesn't go in."
                the_person "Whew! That was a nice try!"

            the_person "Alright, I'll go again. Let's see here…"
            "She doesn't have any obvious shots either, but she starts to line something up."
            the_person "Alright, this type of shot is much harder, but if you hit the cue ball slightly to the side instead of dead on, you can get it to curve as it spins…"
            "She briefly explains the math behind curving a shot around an obstacle. You understand the idea, but the math of the curve and the precision hit required seems daunting."
            $ the_person.draw_person(position = "standing_doggy")
            the_person "Alright… let's see if I can demonstrate…"
            "[the_person.possessive_title!c] strikes the cue ball. It curves between the 8 ball and one of yours and strikes one of her 2 remaining balls, driving it into a corner pocket."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Woo! Alright!"
            mc.name "Wow, you make it looks so easy. I can tell you are very well practised."
            the_person "Thanks!"
            "She looks at the table."
            the_person "Here, why don't you try it? You could hit it here and swing it around my last ball."
            the_person "I know you probably won't sink it, but just to try it."
            mc.name "Hmmm… okay…"
            "She explains to you how to line up the curve and how to strike the cue ball to get it to curve the way you want it to."
            mc.name "Ahh what the hell, here we go."

            if mc.sex_skills.get("Foreplay", 0) > 3 and mc.int > 3:
                "*Foreplay and Intelligence check passed!"
                "You are starting to understand the allure of the game, as you try to line up a difficult curve shot."
                "Your only goal this early is to make contact with the target, but you think with just a bit of spin..."
                "You strike the cue ball. It curves around [kaya.possessive_title]'s striped ball and hits the target."
                "It doesn't go in, but it does stop just in front of a corner pocket, effectively blocking it from being available for [kaya.title] to use."
                the_person "Holy... you almost got that one?"
                the_person "Like, I can tell you haven't played before, but you are picking this up crazy fast."
                the_person "I can't wait to keep playing you as you get better and better!"
                $ the_person.change_love(4, 60)
            else:
                "*Foreplay and Intelligence check failed*"
                "You do your best to line up a curved shot, but at this point you can tell you are in way over your head."
                "You hit the ball as described, and watch it curve around [kaya.possessive_title]'s ball, but it doesn't go anywhere near your target."
                the_person "Hey, that's the idea! Nice try!"

            the_person "Alright, I think I've shown you the basics… time to finish you off."
            "She gives you a smirk when she finishes the sentence. She knows exactly what she just said…"
            $ the_person.draw_person(position = "standing_doggy")
            "Next thing you know, [the_person.title] sinks her last two striped balls, then lines up the 8 ball."
            "She strikes the cue and sinks it easily, winning the game."
            $ the_person.draw_person(position = the_person.idle_pose)
            the_person "Woo! Good game! How about one more?"
            mc.name "Yeah, let's play one more."
            the_person "Alright! Let me show you how to rack it up."
            "She inserts some quarters into the table and the pool balls get released."
            "You grab the triangular rack and help gather the balls together."
            the_person "Alright, that looks good, the 8 goes in the middle, one corner gets a stripe and the other a solid…"
            mc.name "Like this?"
            the_person "Yeah… you got it!"

        "Skip the pool game intro dialogues\n{menu_yellow}No consequence for event{/menu_yellow}":
            $ the_person.draw_person(position = the_person.idle_pose)

    the_person "Alright, this game I'll take it easy on you, okay?"
    mc.name "Sounds good. Should we play for stakes?"
    the_person "Wow, I just said I was taking it easy on you… but what do you have in mind?"
    mc.name "Well, if I win, you have to go out with me again sometime."
    the_person "Ahhhh, I see. A night of free drinks and billiards? That sounds terrible!"
    "Her tone makes it clear she is just teasing."
    the_person "Alright, I'll take that. And if I win, you have to walk me home tonight."
    mc.name "Alright, deal."
    the_person "Nice. Alrighty your break!"

    call bar_date_billiards_label(the_person) from _kaya_first_date_billiard_scene_01
    if _return: #You won
        the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
        mc.name "The horror!"
        the_person "Guess I'll just have to walk myself home now, dreading the day the mysterious stranger shows up at the coffee-shop and demands my presence again!"

    else:
        the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
        mc.name "Too bad you didn't make that your wager then."
        "At first she looks at you, a bit startled, thinking you mean you don't want to, but then realises you are teasing her."
        the_person "Guess you'll just have to walk me home and we'll go our separate ways then."

    "The teasing between you two has definitely become playful. You are really enjoying her company."
    the_person "But uh... we're doing both... right?"
    mc.name "Of course."
    "You both finish off what is left of your drinks, then leave the bar together."
    $ mc.change_location(downtown)

    mc.name "Hey, I forgot to ask you, how did your finals go?"
    the_person "Oh, they went great! I'm finally done!"
    mc.name "With finals?"
    the_person "With my undergrad. I did it online so I could help take care of my mom. They don't do a big ceremony or anything but I finished up the final classes for my degree."
    mc.name "What… at 20?"
    the_person "Yeah, I umm, I took some classes while I was still in high school. I was always good at academics."
    the_person "I've been trying to get into a master's program at the local university, but I just can't get in."
    mc.name "What? Why not?"
    the_person "Apparently if you didn't graduate from there, they require a sponsorship from one of the staff, but I just don't know anyone there!"
    the_person "I've cold called a couple of them but they just blow me off."
    mc.name "What are you looking to study?"
    the_person "Well my degree is in biology, and I'm trying to get into a pre-med program."
    mc.name "Wow… so you want to go into the medical field? Be a doctor?"
    the_person "Well, something like that… I'd like to get more into the research side of things… for personal reasons…"
    "She seems hesitant to explain more, so you decide not to push for more information."

    mc.name "Have I ever told you what I do for a living?"
    the_person "Umm, no. I've been curious, but my mom always told me it is rude to ask a man what he does on a first date…"
    mc.name "I actually run a pharmaceutical research and development company. I have an excellent working relationship with a professor at the university."
    "She stops walking and looks at you in surprise."
    $ the_person.draw_person(position = "stand2")

    the_person "You… you what?"
    mc.name "She has actually been on my case lately about recruiting one of her lab assistants… I could probably convince her to sponsor you."
    the_person "I… that would be amazing… but… I mean we don't really even know each other?"
    mc.name "No, not really, but I'm a good judge of character, and I can tell just from what I do know that you would be a great candidate."
    mc.name "I'll try to talk to her soon and get back to you."
    the_person "I… I don't even know what to say. I would owe you a huge favour."
    mc.name "Well, speaking from experience, that is how a lot of things in the world work. Some people will help you, and ask for your help in exchange later."
    mc.name "So many things are just all about who you know."
    $ the_person.draw_person(position = the_person.idle_pose)
    "You walk the rest of way to her place in silence. She is clearly lost in her thoughts."
    $ the_person.learn_home()
    $ mc.change_location(kaya.home)
    $ the_person.change_location(the_person.home)
    $ renpy.show("Apartment Entrance", what = bg_manager.background("Apartment_Lobby"), layer = "master")
    "Soon you walk up to the steps of a run-down apartment building. This must be where she is living."
    the_person "Ahh, we're here already..."
    the_person "Do you... should I like, give you my number?"
    mc.name "Oh yeah, I'll probably need that. I'll let you know as soon as I can talk to her though."
    $ mc.phone.register_number(the_person)

    the_person "Hey, I just want to say, it's been a long time since I had a night like this to just relax and have fun. I had a great time... please come back and see me at the coffee shop, okay?"
    the_person "Even if it doesn't work out with your friend and a sponsorship... you owe me another night out, remember?"
    mc.name "Your charm is difficult to resist. And the coffee is good too."
    $ clear_scene()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, the_person.outfit, position = "kissing") # keep outfit the same
    "[the_person.title] holds her arms out for a hug, and you draw her close. She is looking up at you, and feeling right, you kiss her."
    "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
    "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when your hand wanders down to her ass, but reaches back and moves your hand back up."
    $ the_person.change_arousal(15)
    $ the_person.break_taboo("kissing")
    "You make out for several seconds."
    $ scene_manager.add_actor(sakari)
    "Suddenly, the front door opens up. There is an older woman standing there. [the_person.title] backs away quickly."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "Whaea!(????)! I... Ahhh! What are you doing?"
    sakari "Tamahine...(????)... ahh, am I interrupting?"
    the_person "Mom! Yes I... ahhh..."
    "She lets out a long sigh."
    the_person "Well, I guess we're doing this now... Mom, this is my friend, [mc.name]. He and I were playing some pool, and he was just walking me home..."
    the_person "[mc.name] this is my mom..."
    $ sakari.set_title(sakari.name)
    $ sakari.set_possessive_title("your friend's mother")
    $ sakari.set_mc_title(mc.name)
    $ sakari.set_event_day("day_met")

    sakari "Ahh hello sir. You can call me [sakari.title]."
    mc.name "Good evening [sakari.title]. I'm [mc.name]."
    sakari "Nice to meet you. Sorry I heard a noise and was just looking to see what was going on out here."
    the_person "Right... well... I guess this is goodnight."
    the_person "[mc.name]... see you soon?"
    mc.name "Yes, I'll get back to you as soon as I can."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ scene_manager.update_actor(sakari, position = "walking_away")
    "[the_person.possessive_title!c] and her mother step into their apartment and then the door closes behind them."
    $ scene_manager.clear_scene()
    "You hear [the_person.title] chiding her mother after the door closes."
    $ mc.change_location(downtown)
    "You step out of the apartment building, thinking about the date you just had."
    "[the_person.possessive_title!c] seems impressively smart, and graduating from college at 20 while working at a coffeeshop on weekends points to a strong work ethic."
    "You're certain she would make a great candidate for an advanced program at the local university. Now you just need to convince [nora.title]."
    "It's interesting that she lives with her mother, also. She mentioned once that she helps take care of her.  It makes you wonder about her health - her lack of hair might be an indication she's undergoing cancer treatment?"
    "There's no use dwelling on it now. Hopefully you'll be able to learn more soon."
    "For now, you should focus on getting her that sponsorship!"
    $ add_kaya_ask_nora_for_sponsorship_action()
    $ kaya.progress.love_step = 2
    call advance_time(no_events = True) from _call_advance_time_kaya_first_date_label
    return

label kaya_ask_nora_for_sponsorship_label(the_person):  #Nora on talk event
    $ the_person.draw_person()
    "You swing by the university. You catch [the_person.possessive_title] between lectures."
    the_person "Hello there [the_person.mc_title]. It's good to see you, what can I do for you?"
    mc.name "I've got some good news for you [the_person.title]."
    the_person "Oh?"
    mc.name "I think I've found someone eager to be your lab assistant, like [stephanie.fname] in the past."
    the_person "That WOULD be nice. Who is it?"
    mc.name "I recently met her at a coffee shop. She just finished her biology degree online and is trying to get into a pre-med program here, but can't…"
    the_person "Ah yes, she would need a sponsor. And I assume you think I would be the sponsor?"
    mc.name "Yes. She's willing to help you out in the lab between classes in exchange."
    the_person "Hmmm… a favour for a favour… that makes sense. She isn't too dumb, is she?"
    mc.name "Well, she had several college credits by doing dual enrolments by the time she was 18, and graduated for her biology degree at the age of 20."
    the_person "Ohhh… interesting. I'd like to meet with her. Can you give her my office hours and ask her to swing by?"
    mc.name "Sure, I'll text her with it right now."
    $ mc.start_text_convo(kaya)
    mc.name "Hey, I just got done talking with a possible sponsor at the university, she asked if you could swing by sometime."
    "You add on [the_person.possessive_title]'s office hours."
    "A few moments later, she responds."
    kaya "!!!!!!!"
    kaya "Can I swing by now? It shows she has hours now? I can be there in 10 minutes???"
    $ mc.pause_text_convo()
    mc.name"Can she come by in about 10 minutes?"
    the_person "Oh, certainly. She seems eager?"
    mc.name "She is very eager, and highly motivated."
    $ mc.resume_text_convo()
    mc.name "Here is her room number. She'll be expecting you."
    kaya "Thanks!!! I'm on my way!!!"
    $ mc.end_text_convo()
    $ kaya.change_happiness(20)
    "Well that was easy."
    mc.name "Alright, she is on her way."
    the_person "Excellent. She seems motivated."
    mc.name "She is. I think she will make an excellent understudy and assistant."
    the_person "Alright. Was there something else you needed?"
    "You make a mental note to check back in with [kaya.possessive_title] at the coffee shop this weekend."
    $ add_kaya_nora_sponsorship_action()
    return

label kaya_nora_sponsorship_label(the_person):  #Kaya room entry event
    $ the_person.draw_person()
    "You step into the coffee shop. [the_person.possessive_title!c] spots you as you walk in."
    "With no one in line, you step up to the counter. She is smiling wide."
    the_person "Hey! Guess what!"
    mc.name "You got a sponsor?"
    the_person "Yes! And Dr. [nora.last_name] pushed it through so fast, I'm already signed up for classes! I start this week!"
    mc.name "That's great! I'm excited for you."
    the_person "The registrar is making me take a couple easy ones that my original degree program left out, according to them, but it is a solid course load."
    the_person "Dr. [nora.last_name] agreed to let me assist her in the labs on Thursdays when I get done with class."
    the_person "We talked for a long time about things when I met with her… I can't wait to get started."
    mc.name "You're going to do great, I just know it."
    the_person "Yeah... It is so hard to believe… a random hot guy here at the coffee shop hits on me, and next thing I know…"
    the_person "I… guess what I'm saying is… thank you."
    $ the_person.change_love(3, 60)
    mc.name "You're welcome. You are talented young woman, and you deserve it "
    the_person "Aww… anyway, I'll get you a coffee."
    $ the_person.draw_person(position = "walking_away")
    "She turns away and makes you up a fresh coffee. Apparently she remembers how you like it."
    "You make a quick mental note this week her new classes start and Thursday is her first day as Nora's lab assistant."
    "You should probably swing by and check up on her."
    "You notice a couple people have walked in and are in line behind you."
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title!c] turns and hands you your coffee."
    the_person "Here you go! This one is on the house."
    mc.name "Thanks. Have a good week at class, if I don't see you before then."
    the_person "I will!"
    "You step away from the counter with your coffee."
    $ mc.change_energy(50)
    $ add_kaya_first_day_of_class_action()
    return

label kaya_first_day_of_class_label():
        # Outline
    #This completes Kaya's 20 love story arc, and she is now a student at the university, taking new classes and Thursday works for Nora.
    $ the_person = kaya
    "In this label, we check up on [the_person.possessive_title] who has had some new classes today."
    "She is excited to be in class, and has signed on to be [nora.fname]'s lab assistant on Thursday nights."
    "A teamup with [nora.fname] begins after this."
    $ kaya.progress.love_step = 3
    $ add_kaya_needs_residency_action()
    $ add_kaya_study_struggle_action()
    $ add_kaya_meet_erica_at_uni_action()   #Is this the right place for this?
    $ add_kaya_nora_teamup_intro_action()
    $ add_kaya_condom_talk_action()
    return

label kaya_needs_residency_label(the_person):   #40
    $ the_person.draw_person(emotion = "sad")
    "You swing by the coffee shop. It's the weekend, and your favourite barista, [the_person.title], should be working today."
    "When you walk in, she is busy with several customers."
    "You wait patiently in line until you step up to the counter."
    the_person "Hello sir and welcome to… Oh! Hey."
    "She seems distracted."
    mc.name "Hey… you okay? You seem a little off."
    the_person "Ahh, yeah… just some school stuff… nothing you need to worry about."
    if the_person.progress.lust_step >= 1:  #Event where she dry humps MC to relieve sexual tension in a school study room.
        mc.name "Still too distracted in class?"
        the_person "Ahhh, no, not that."
    mc.name "Hmm… what's going on?"
    the_person "Look it's… it isn't anything I need to bother you about."
    "She bites her lip and looks down. You can't imagine what could be giving her problems."
    mc.name "Why don't you tell me about it anyway? You never know if it is something I could help with."
    the_person "Ahhh… geeze… I… I guess…"
    "She looks over at a coworker."
    the_person "Hey, can I take my break real quick?"
    "Coworker" "Sure thing, I'll take over"
    the_person "Thanks!"
    "You go sit down in a booth and a minute later [the_person.possessive_title] comes and sits down next to you."
    $ the_person.draw_person(position = "sitting")
    mc.name "So what's going on?"
    the_person "Well, I got kinda blindsided this week. The university registrar asked me on Thursday what I'm doing for my work study program."
    the_person "Normally people do clinicals or shadowing or something during summer vacation, and I thought I could just do mine next summer…"
    the_person "But she said that is a requirement to even just get in and if I don't have one figured out ASAP they are going to remove me from the program."
    mc.name "Whoa. So… you need like… an internship of some sort?"
    the_person "Yeah, something related to my field."
    the_person "I've tried reaching out to a couple local hospitals, but so far I haven't had any luck."
    "Hmm. An internship? You wonder if that is something that she could do at your business."
    "It would be a bit of a risk though. You make a wide variety of pharmaceuticals, not all of them for medical reasons…"
    "However, you have made pretty good progress with [the_person.fname]… you should be able to handle bringing her on…"
    "You look up and realise she is looking at you and chuckling."
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    mc.name "What?"
    the_person "You're cute when you're thinking, you know?"
    the_person "Your eyebrows all furrowed and your face all serious."
    mc.name "[the_person.title]... have I ever told you what my business does?"
    the_person "Umm, well, you mentioned once that you run some kind of pharmacy..."
    mc.name "Well... not really. I am involved in the research and development for a small pharmaceuticals company that cover a... wide range of goals."
    mc.name "While some of these are for clandestine defence contracts... we do have a set of medical formulas as well."
    mc.name "With [nora.fname]'s help, I wonder if we could set you up to do a work study helping me with research."
    "[the_person.possessive_title!c] is just looking at you in disbelief."
    the_person "So you... make drugs?"
    mc.name "Basically yes. If that doesn't qualify as being in your area of study, I don't know what would."
    mc.name "You should know something ahead of time though."
    the_person "Yeah?"
    mc.name "There are medical formulations we work on, yes, but a lot of our business comes from small run contracts from drugs used for... different purposes."
    the_person "Okay... are you selling like... meth or something?"
    mc.name "No! No. All of it is legal, and many of my customers are government three letter agencies."
    mc.name "If you want to focus on medical research while you are there, I'm perfectly fine with that, but I just want you to be aware."
    mc.name "We have a small team, and our focus shifts fairly often. We might be researching a variety of different effects while you are there."
    the_person "Ahh, I think I understand... it sounds... honestly a lot like what professor [nora.fname] has been doing."
    mc.name "Yes, that is why I have a fairly close working relationship with her. A lot of what I'm doing now started as a side project in her lab."
    the_person "Aaahhhh, I get it. This is all making a lot of sense."
    "She looks down for a moment, thinking. Then looks back up at you."
    the_person "Have I ever told you what is going on with my mom?"
    mc.name "You've said before that she is sick, but you never got more specific."
    the_person "My mom... she has a rare blood disorder. It leaves her anaemic and weak, and she has to have regular transfusions."
    the_person "It... it made her hair fall out... and there are a number of other side effects."
    the_person "It has been progressing for years... slowly but surely..."
    the_person "When I was a little girl, I decided that someday I was going to be a doctor so I could save her."
    the_person "I was going to find the cure... somehow."
    the_person "I never knew my dad, and the thought of losing her is soul crushing, but watching as things have gotten worse for her, year after year, has made it feel inevitable."
    mc.name "[the_person.fname]... I'm so sorry..."
    "[the_person.title] shrugs and looks away. You can tell she is fighting back tears."
    the_person "As I've gotten older, I've realised that the whole thing was probably a silly fantasy... but... if I could spend some time and see?"
    the_person "If something you happen to have could maybe even just... help her?"
    mc.name "I'll make sure that you have access to our medical suites and if you think you stumble on something, you are welcome to pursue it as you see fit."
    mc.name "But first, let me check in with professor [nora.fname]. I want to make sure that this will qualify for your work study program before we get too far into it."
    the_person "God... I can't believe it. I never thought that when I took the job working weekends here that I would meet someone like you."
    mc.name "Well [the_person.title], you are so smart and talented, you make it easy to help you."
    the_person "And you... you're so hopelessly addicted to coffee. I guess it was fate."
    "You both smile at each other."
    mc.name "I'll plan to talk to [nora.fname] on Monday. Hopefully we can get everything setup to get you started on Wednesday."
    the_person "Wow! That would be great."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "Umm, I should probably get back to work, I don't want to press my luck with my coworkers."
    the_person "They are pretty great though. There are a few of us who work exclusively on weekends and have gotten to be good friends."
    mc.name "That's good. It is always good when you get along with your coworkers."
    "You stand up as well."
    the_person "Alright... here..."
    $ the_person.draw_person(position = "kissing")
    "She reaches up and quickly gives you a quick kiss, right on the lips."
    "She lingers for a moment, but then moves back."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "See you on Wednesday!"
    mc.name "Sounds good!"
    the_person "Oh, and if you ever want a coffee while I'm working, I can make it on the house. It's the least I can do!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and heads back to her work."
    "You set yourself a reminder to talk to [nora.possessive_title] on Monday. You'll go in the afternoon, when she normally has some free time."
    $ kaya.progress.love_step = 4
    $ add_kaya_nora_residency_action()
    return

label kaya_nora_residency_label(the_person):
    "You swing by the university to talk to [the_person.possessive_title]."
    "You need to get her to approve [kaya.title] doing a work study program at your business, but you know this is going to be a hard sell."
    "She hasn't been fully trusting of you, ever since you recruited [stephanie.title] out from under her."
    $ the_person.draw_person()
    mc.name "Good day [the_person.title]."
    the_person "Ah, hello [the_person.mc_title]."
    mc.name "I have another favour to ask of you."
    the_person "Oh joy. Let's hear it."
    mc.name "Your new lab assistant, [kaya.fname], is at risk of being removed from her study program."
    mc.name "The registrar is telling her she must complete a work study program in order to continue in the program."
    the_person "Ah yes, I recall there being a requirement along those lines. That certainly seems like an issue."
    the_person "I'm not sure how I can help though. I certainly can't hire her any more than I already have."
    mc.name "No... but you could help convince the powers that be to accept her joining a work study that you approve of."
    mc.name "Perhaps someone who runs a pharmaceutical business that you are already consulting for..."
    the_person "Jesus, there really isn't any shame with you, is there? She hasn't even started working for me, and you are already trying to steal her from me?"
    mc.name "Not steal, no, just share."
    mc.name "The girl works hard, and she is highly motivated. I've no doubt that she'll be able to do both."
    "[the_person.possessive_title!c] sighs."
    #Split the story here based on Nora's story progress. She requests some sort of favour in return.
    #Since Nora doesn't have a story yet, just make her threaten MC for favours.
    the_person "You know, at some point, I'm going to start calling in all these favours you owe me."
    the_person "Fine. I'll put a bug in the registar's ear about your program."
    the_person "The girl still owes Tuesdays and Thursdays to the university though. The other days you can have her."
    mc.name "It's not for me. It's for her."
    "[the_person.title] rolls her eyes."
    the_person "Yes yes, I'm sure this is purely altruistic on your behalf. What a saint you are."
    the_person "But just know, I'll still expect her coursework to be done on time and at a continuing high quality."
    the_person "If her work slips... I'll have to cut her."
    mc.name "Understood."
    mc.name "Thank you [nora.fname]. It is always a pleasure working with you."
    the_person "Goodbye for now, [the_person.mc_title]. Until you need yet another favour from me I suppose."
    $ clear_scene()
    "As you step away from [the_person.title]'s office, you pull out your phone and text [kaya.title] the details."
    $ mc.start_text_convo(kaya)
    mc.name "Hey, I just talked to Professor [nora.fname]."
    mc.name "Here is my office location, you'll be good to start the work study on Monday.."
    "A few moments later, she responds."
    kaya "!!!!!!!"
    kaya "You're amazing. I'll be there!!!"
    kaya "I don't have much to offer, but if you swing by the coffee shop this weekend, I'll hook you up for free."
    mc.name "I might. Either way I'll see you on Monday."
    $ mc.end_text_convo()
    "You have successfully managed to sponsor [kaya.possessive_title]'s work study program."
    "You make a mental note to be at the office Monday morning to introduce her to the rest of the Research department."
    $ add_kaya_residency_first_day_action()
    $ kaya.progress.love_step = 5
    return

label kaya_residency_first_day_label():
    $ the_person = kaya
    $ scene_manager = Scene()
    "It is Monday morning. Today is [the_person.possessive_title]'s first day at your office for her work study program."
    $ mc.change_location(lobby)
    "You head to the office and hang out in the lobby, waiting for her to get there."
    $ scene_manager.add_actor(the_person)
    "Right on time, she steps into the lobby. She spots you immediately."
    the_person "Hey! I wasn't sure if this was the right place or not. There's like, no signs outside?"
    mc.name "Yes, we keep things pretty low key around here. We don't necessarily want to advertise our presence."
    the_person "Right... anyway, this is awesome! I can't wait to get started, and to learn a bit more about my mysterious benefactor and his company!"
    the_person "You just keep saying stuff like... pharmaceuticals... and... drugs..."
    the_person "You know those two things are enormous categories, right?"
    mc.name "Ah yes, well, as you will see in a minute, we research a wide array of chemicals. First though, I have some basic paperwork for you to fill out."
    the_person "Of course. Always with paperwork."
    mc.name "Now, as an intern, you need to sign this NDA and confidentiality agreement. Standard business forms."
    mc.name "However, I don't have a full employment contract for you, this is for a work study only, so your access to ALL the functions of the business will be restricted."
    mc.name "We contract out with multiple... sensitive... departments... which won't be a concern for you at all."
    the_person "Ah yes, top secret mystery stuff, got it."
    mc.name "You will have access to all our medical related research though, as well as team members in the research department, in case you need guidance."
    if mc.business.head_researcher is None: #Sadness
        mc.name "The research department is currently undergoing restructuring, so I don't have anyone for you to report to directly right now."
        mc.name "So for now if you have any issues you can report directly to me."
        the_person "Okay, sounds good."
    else:
        mc.name "Let's head down to the research department now so you can meet the department head."
        the_person "Okay."
    $ mc.change_location(rd_division)
    "[the_person.possessive_title!c]'s eyes go wide as you walk into the research area."
    the_person "Wow, this is a way more impressive setup than I was expecting..."
    if mc.business.head_researcher is None:
        "You show her around the department, eventually settling her in at her desk."
    else:
        $ scene_manager.add_actor(mc.business.head_researcher)
        "[mc.business.head_researcher.title] sees you walk in and comes over to greet you."
        mc.business.head_researcher "Good morning."
        mc.name "Good morning, [mc.business.head_researcher.title]. I'd like to introduce you to [kaya.fname]."
        mc.name "She is a student at the university and is going to be doing a work study here for us."
        mc.business.head_researcher "Nice to meet you."
        mc.name "This is [mc.business.head_researcher.fname], my department head. You'll be reporting to her with any progress or questions you might have."
        the_person "Ah, nice to meet you too."
        mc.name "[mc.business.head_researcher.title], she will be given access to medical trait research only, but will have full access to the lab otherwise."
        mc.business.head_researcher "Ah, I understand. Let me know if you need any help settling in, [the_person.fname]!"
        the_person "Thanks!"
        $ scene_manager.remove_actor(mc.business.head_researcher)
        "You finish showing her around the department, then helping her settle in at her desk."
    the_person "Wow, I can't wait to get started."
    mc.name "Perfect. I'll be around at the end of the day to check up and see how you are settling in."
    $ scene_manager.clear_scene()
    "You step away from [the_person.title]'s desk and let her get to work."
    "You aren't sure how beneficial it will be to have an intern here just a few days a week, but at least it will give you an opportunity to spend some more time with [the_person.title]..."
    $ kaya.progress.love_step = 6
    $ add_kaya_nora_research_pilfer_intro_action()
    # $ add_kaya_working_late_action()
    $ add_kaya_first_research_day_action()
    $ kaya_begin_work_program_schedule()
    return

label kaya_first_research_day_label():
    # This event completes Kaya's 40 love story arc. At the end, she has a full schedule, working MWF for MC, TTH for Nora, and SA SU at the coffee shop.
    $ the_person = kaya
    $ the_trait = get_random_from_list(serum_traits_by_function(function = "Medical", researched = True))
    "You swing by the research wing to check up on [the_person.possessive_title] and see how her first day went."
    $ mc.change_location(rd_division)
    $ the_person.draw_person(position = "sitting")
    mc.name "Hello [the_person.title]. It's about closing time, how was your first day?"
    the_person "Oh, hey [the_person.mc_title]. Really good actually."
    the_person "There is so much to get caught up on! I spent most of the day just looking at your recent medical research."
    the_person "Some of it was really... eye opening!"
    the_person "There was one drug in particular... let me see here..."
    the_person "[the_trait.name]?"
    mc.name "Yes, I'm familiar with that one."
    the_person "Well, I noticed in the formulation directions, it has several superfluous steps..."
    the_person "I took a bit to re-write the mixing process, and I was able to streamline it."
    the_person "I mixed up a batch and so far testing on mice has been going well! I think it might help you in the future using this formulation."
    mc.name "Wow... let me see..."
    "She excitedly shows you the original process and her optimized process."
    "It takes a while to show you her changes, and the rest of your research employees have gone home by the time she finishes."
    mc.name "Yes... that all makes sense. Wow, first day, and already producing results. I'm really impressed."
    $ the_person.change_love(2, 70)
    the_person "Ah, thank you [the_person.mc_title]."
    $ the_trait.add_mastery(2)
    "Her work has increased your mastery of [the_trait.name]."
    "[the_person.possessive_title!c] looks around, realizing that you two are alone and that everyone else has gone home."
    the_person "Ah, looks like I got a little carried away. I'm sorry I didn't mean to keep you late."
    mc.name "Oh it's no bother. I'm usually the last one to leave anyway."
    $ the_person.draw_person(position = the_person.idle_pose)
    "She stands up and starts to gather her things."
    "She turns back to you."
    the_person "Wow... this is like... one of the first times we've ever actually had a few minutes like, alone."
    $ the_person.add_situational_slut("alone_time", 10, "We're finally alone")
    call perk_time_of_need_story_label() from _time_of_need_kaya_love_alone_01
    $ the_person.change_arousal(20)
    mc.name "Yeah, it does seem like getting time to ourselves is very rare."
    the_person "I still can't believe everything you've done for me these past few weeks. I owe you more than I could hope to repay..."
    mc.name "It isn't about the money, [the_person.title]. A great person like yourself just needs the opportunity to do great things."
    $ the_person.change_love(2, 70)
    the_person "Ah, you're such a charmer. Thank you."
    the_person "But umm, I was thinking... maybe I could show you my gratitude in another way..."
    if the_person.is_willing(blowjob):  #with 20 sluttiness earlier, we want this to be the most likely outcome...
        $ the_person.draw_person(position = "kissing")
        "She puts her arms around you and whispers in your ear."
        the_person "...with my mouth..."
        $ mc.change_locked_clarity(40)
        "One of her hands drops down to your crotch, and starts to rub you through your pants."
        mc.name "Mmm... I'm certainly not going to stop you from showing your gratitude, however you see fit..."
        "She gives a brief chuckle."
        the_person "Yeah, I didn't figure you would."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.possessive_title!c] gets down on her knees. She undoes your belt and pants, and quickly slides them down."
        if the_person.has_taboo("sucking_cock"):
            "She lets out a little gasp when your cock springs free."
            $ the_person.change_arousal(20)
            the_person "Fuck, I've never seen this monster up close like this before."
            "She gives it a few tentative strokes with her hand, then looks up at you."
            the_person "[the_person.mc_title]... I'm going to do my best, but be patient with me, okay?"
            mc.name "Of course, take your time. Here, let me help."
            "You gather her hair up behind her head, helping keep it out of her face."
            the_person "What a gentleman. Alright... here it goes..."
            "[the_person.possessive_title!c] leans forward and licks up and down the shaft a few times."
            "Her hot tongue and breath feel great. She runs her tongue along the tip a few times, licking up your pre-cum."
            "The moment comes, and she opens her mouth, sliding the tip in past her lips."
            $ mc.change_locked_clarity(50)
            $ the_person.break_taboo("sucking_cock")


        else:
            "She lets out a little moan when your cock springs free."
            $ the_person.change_arousal(20)
            the_person "Fuck, everytime I do this, the size surprises me again!"
            "She starts to lick and kiss up the side of your length. Her hot lips and breath feel great."
            "She happily licks your precum from the tip, then opens her mouth and slides the tip in past her lips."
            $ mc.change_locked_clarity(50)
        "She gives a strong moan when she feels the heat and hardness filling her mouth for the first time."
        "She pulls off and looks up at you again."
        the_person "God, it's so hard. Alright, time for some fun!"
        "[the_person.possessive_title!c] opens up and takes you into her steamy mouth again."
        "Her head begins to bob up and down as she begins to suck you off."
        $ mc.change_locked_clarity(40)
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_kaya_office_bj_01
        $ the_report = _return
        $ the_person.draw_person(position = "blowjob", emotion = "happy")
        if the_report.get("guy orgasms", 0) > 0:
            "[the_person.possessive_title!c] looks up at you from her knees with a goofy smile on her face."
            mc.name "Fuck that was good... give me a minute..."
            the_person "Of course!"
        "You back up a bit, and [the_person.title] stands up."
        $ the_person.draw_person(position = the_person.idle_pose)
    else:   #but if blowjob isn't available for some god forsaken reason, let MC freestyle a bit.
        mc.name "Did you have something specific in mind?"
        the_person "I umm... ermmm... not really..."
        the_person "But we could mess around a little?"
        mc.name "Sounds good to me."
        call fuck_person(the_person, private = True,) from _call_fuck_person_kaya_office_non_bj_01
    "As things wind down with [the_person.possessive_title], you realise how late it is getting."
    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    mc.name "Well, I need to get home. I look forward to having you around here, [the_person.title]."
    the_person "Yeah, take care!"
    $ clear_scene()
    $ add_kaya_working_late_action()    #Condom talk gets added during character creation.
    $ kaya.progress.love_step = 7
    return

label kaya_working_late_label():    #60
    # In this label, Kaya assumes ideal waifu form, asking for dick and wanting creampies and babies. Optional go steady at the end.
    $ the_person = kaya
    $ kaya.change_baby_desire(60)
    $ the_trait = get_random_from_list(serum_traits_by_function(function = "Medical", researched = True))
    "It is closing time. You make the rounds at work to make sure you can lock up."
    "You swing by the research wing and discover [the_person.possessive_title] sitting at her desk."
    $ mc.change_location(rd_division)
    $ the_person.draw_person(position = "sitting", emotion = "sad")
    "She is staring at the screen, with a rough look on her face."
    mc.name "Hey... you doing okay over there?"
    the_person "What? Oh!... Hey [the_person.mc_title]."
    the_person "There is something about this serum trait that just isn't right... but for some reason something just isn't clicking."
    the_person "I don't know what it is... it is like there is something just on the edge of my mind but I just can't figure it out."
    mc.name "Ah, yeah, I know that feeling."
    "She turns back to the computer for a moment, with a long sigh."
    the_person "Yeah... you always seem to figure stuff out though. How do you do it?"
    the_person "Out of nowhere, you seem to have these ideas that just click and solve these seemingly impossible problems."
    mc.name "Ah... well... I guess I have a lot of sources of inspiration."
    mc.name "Honestly though, I find my best times of thinking to be when my mind is completely clear of distractions."
    mc.name "Working around so many women, that often means right after a satisfying orgasm."
    $ the_person.draw_person(position = "sitting", emotion = "angry")
    "She shoots you a sarcastic look."
    the_person "I'm being serious. Don't pretend like letting you get in my pants will help me with this serum formula."
    mc.name "Hey, I'm not saying it works for everyone, but I'm being serious."
    "[the_person.title] rolls her eyes and turns back to the computer."
    "She sits there for several moments, thinking."
    "Eventually she turns back to you, a grin on her face this time."
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    the_person "Were you just saying that to try and get me to mess around a little?"
    $ the_person.add_situational_slut("alone_time", 10, "We're finally alone")
    call perk_time_of_need_story_label() from _time_of_need_kaya_love_alone_03
    mc.name "No, I was being serious."
    if the_person.has_taboo("vaginal_sex"): #Use taboo as a test for her virginity, which she should have explained during condom talk.
        the_person "So... you don't want to mess around?"
        mc.name "I didn't say that either. I would love to have some intimate fun, if you're offering."
        mc.name "It really does work for me though."
        the_person "I see..."
        "[the_person.possessive_title!c] bites her lip and looks down for a bit."
        the_person "Hey... do you remember that conversation we had the other day... at the coffee shop? About having sex?"
        mc.name "Of course."
        the_person "I... I was wondering if you'd thought it over..."
        mc.name "To be honest, there really isn't much to think about."
        mc.name "You're one of the hottest, brightest women I've ever met. I'm down for it anytime you are."
        the_person "Well, has everyone else gone home for the day?"
        "Oh fuck yes this is finally happening!"
        mc.name "Yeah, it is just you and me here now."
        the_person "[the_person.mc_title]... I... I'm falling so hard for you. Will you please take my virginity now?"
        $ mc.change_locked_clarity(50)
        mc.name "Yes. Yes I will do so gladly."
        the_person "Just... I have one request."
        mc.name "Yes?"
        the_person "I know I said all that stuff about pulling out but, for my first time... I want to experience everything."
        the_person "Will you please cum inside me?"
        the_person "I just... for my first time, I want to experience it, the connection and... everything!"
        mc.name "I... I don't know... I thought I'd be able to pull out if I needed to..."
        the_person "It's okay... I know... just... if you decide you want to, then do it, okay?"
        the_person "I want you to!"
        mc.name "Wow. Okay."
    else:
        mc.name "Don't get me wrong. I DO want to get back in your pants, but that isn't why I'm saying that."
        the_person "Haha, yeah okay..."
        "She lets out an exasperated sigh."
        the_person "Ugh, fuck it. Has everyone else gone home for the day?"
        mc.name "Yep. It's just us here."
        the_person "Maybe I do just need to get laid. Are you down?"
        mc.name "Fuck yes."
        $ mc.change_locked_clarity(30)
        if the_person.has_taboo("creampie"):
            the_person "Hey, can I ask you for one thing though?"
            mc.name "Sure thing."
            the_person "I know that we've been messing around a bit lately but... I was wondering if this time, if you would finish inside me..."
            the_person "I've never gotten to experience that before, and I... fuck I... I'm just falling really hard for you."
            the_person "I know that is crazy and we've only known each other a short time, but..."
            mc.name "I don't know."
            the_person "It's okay... I know... just... if you decide you want to, then do it, okay?"
            the_person "I want you to!"
            mc.name "Wow. Okay."
        else:
            the_person "Are you gonna cum inside me again?"
            mc.name "Do you want me to?"
            the_person "[the_person.mc_title], lately I've just... I've really started falling for you."
            the_person "I know that it'll always be up to you, but if you want to cum inside me... I really want it too!"
            $ mc.change_locked_clarity(30)
            mc.name "Fuck that's hot. I'll keep that in mind."
            the_person "Mmm, okay!"
    the_person "You wanna go to your office?"
    mc.name "Nah, there's no one else here."
    $ the_person.draw_person(position = "missionary")
    the_person "Ah!"
    "She gives a little yelp as you suddenly push her back onto some open space on her desk. A few papers get knocked off."
    if the_person.vagina_available:
        "You grab her legs and spread them apart."
    else:
        "You quickly pull off her bottoms."
        $ the_person.strip_to_vagina(position = "missionary")
    $ mc.change_locked_clarity(50)
    mc.name "Let's get you warmed up first..."
    "You lean forward, getting on your knees next to desk, and start kissing up the inside of her left thigh."
    the_person "Mmm..."
    $ the_person.change_arousal(10)
    "When you reach her cunt, you slide your tongue up and down her perfect slit a few times, then slowly push it inside of her."
    "You feel her hands running through your hair as your tongue pushes inside her vagina. She gives a low moan as you let yourself explore her a bit."
    "You lick all around and explore her cunt with your tongue for a good minute or so. You aren't trying to get her off, you just want her to get aroused."
    $ the_person.change_arousal(20)
    the_person "Ahhh! Mmm..."
    "Her moans are starting to get a little urgent, signalling time for you to stop."
    "She watches you as you stand and remove your clothing. She gasps when your cock springs free."
    if the_person.has_taboo("vaginal_sex"): #Virginity time. Should we give the option to take her virginity multiple times, for the sake of seeing all story events? Like ellie?
        the_person "Oh god I can't believe that monster is going inside me..."
        mc.name "So... you're a smart girl... you're aware that this might be... uncomfortable?"
        the_person "Why yes, I did read something about that. Let me see... what did I read..."
        the_person "That's right, first times can be painful, but that after I can look forward to a lifetime of amazing pleasure."
        the_person "Seems worth it to me!"
        mc.name "Wow, okay smartass, let's get this going then."
        the_person "Yeah... but um... go slow... okay?"
        mc.name "Of course."
        "You step up to the edge of the desk. [the_person.possessive_title]'s legs are spread wide and she jumps slightly when your cock makes contact with her slit."
        mc.name "Alright... ready?"
        the_person "You know it."
        mc.name "Okay."
        "You put one hand on her hip, and with the other you guide your cock up and down her slit, getting it good and wet."
        "Then you stop, pointing it straight into her virgin hole."
        "With a gentle push, the head of your cock sinks just into her opening. Just inside, your penetration stops at her hymen."
        mc.name "Alright... here we go."
        "With both hands on her hips, you pull her body farther onto yours. Her virginity tears, and you push deeper inside of her."
        $ take_virginity(the_person)
        $ the_person.draw_person(position = "missionary")
        the_person "Ahhh fffuuuuck... God you're so big [the_person.mc_title]... Ahhh..."
        "She groans in a mixture of pleasure and pain as she gets penetrated for the first time."
        "You take your time, slowly pushing more and more inside of her."
        "You push the rest of the way in, at long last, your bare cock deep inside of [the_person.possessive_title]."
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True, condition = make_condition_taking_virginity()) from _call_fuck_person_kaya_love_first_time_01
        $ the_report = _return
        if the_report.get("creampies", 0) > 0:  #You gave her what she wanted
            "You step back. Your cum has mixed with some of [the_person.title]'s blood as it runs down between her legs."
            "[the_person.possessive_title!c] is looking up at you happily."
            the_person "Oh fuck... [the_person.mc_title] that was so good..."
            the_person "You can just... you can finish inside me everytime... okay?"
            mc.name "And knock you up?"
            $ the_person.change_arousal(10)
            $ the_person.change_love(2, 80)
            the_person "Mmm... yeah... I could handle that..."
        else:
            the_person "Oh wow... that... that was amazing..."


    else:
        the_person "Fuck, I still can't believe that monster fits inside of me."
        the_person "But I'm so glad it does!"
        "You step up to the edge of the desk. [the_person.possessive_title]'s legs are spread wide and she jumps slightly when your cock makes contact with her slit."
        "You put one hand on her hip, and with the other you guide your cock up and down her slit, getting it good and wet."
        "After a brief moment of resistance, you slip your cock into her vagina, pushing yourself deep in one smooth stroke."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_kaya_love_first_time_02
        $ the_report = _return
        if the_report.get("creampies", 0) > 0:  #You gave her what she wanted
            "As you step back, [the_person.possessive_title] looks up at you happily."
            the_person "Oh fuck... that was so good."
            the_person "Can you just cum inside me everytime from now on? It is so gooood..."
            mc.name "And knock you up?"
            $ the_person.change_arousal(10)
            $ the_person.change_love(2, 80)
            the_person "Mmm... yeah... I could handle that..."
        else:
            the_person "Mmm, that was as amazing as always..."
    "As you back away from her, [the_person.possessive_title] slowly stands up, her legs a little wobbly."
    $ the_person.draw_person(position = "stand2")
    the_person "I think you were right... what I really needed was to get laid, haha!"
    "[the_person.title] looks at you thoughtfully for a few moments."
    the_person "Wait... if... you combined the serum with a different catalyst... oh my god!"
    $ the_person.draw_person(position = "standing_doggy")
    "Suddenly, she turns back to her computer and starts typing at an incredible pace."
    "The ass that you just tapped is on full display in front of you, jiggling enticingly as she types at the computer..."
    $ mc.change_locked_clarity(30)
    "Wow... round two? Maybe you could start while she just keeps working..."
    "You step closer to her, then put your hand on her ass. She pushes back against your hand a bit but keeps working."
    "You reach down and give yourself a couple strokes, getting hard again."
    "You run your hand along her ass again... this could be..."
    $ the_person.draw_person(position = "stand2")
    the_person "Yes, that's it! Whoa!"
    "[the_person.title] suddenly stands up and turns into you."
    the_person "Getting a little close there? Anyway, I figured it out!"
    the_person "The issue I was having wasn't with the serum at all! The catalyst that was being used in the second stage of synthesis was all wrong."
    "She looks down and notices your erection."
    the_person "Ohh, damn! I wish I had time for this again... but I really need to get home..."
    "She reaches down and gives your cock a couple quick strokes, before turning away."
    $ the_person.draw_person(position = "back_peek")
    the_person "Sorry! I'm all out of sorts, I need to go get cleaned up..."
    "As she starts to walk away, you find yourself longing to spend more time with her. Not just for the sex, but because of how much fun she is, in general."
    mc.name "[the_person.fname], wait!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "She comes to a stop and turns back."
    the_person "Yeah?"
    menu:
        "Have a good night":
            pass
        "Ask her to be your girlfriend" if not the_person.is_girlfriend:
            mc.name "I know our relationship is kind of complicated, and something like this might be frowned upon, with you working here."
            mc.name "But, I really enjoy spending time with you... do you want to go steady?"
            the_person "What like... you want me to be your girlfriend or something?"
            mc.name "Yes, that is exactly what I'm asking."
            the_person "Oh my god... I... I didn't think you felt that way about me too... I just thought..."
            the_person "Yes! Yes I will! But I still really have to go!"
            $ the_person.add_role(girlfriend_role)
            $ the_person.change_love(5, 80)
            $ the_person.change_happiness(10)
            mc.name "That's okay. I'll see you again soon, I'm sure."
            the_person "Okay!"
    mc.name "Have a good night."
    the_person "Goodnight!"
    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.possessive_title] as she disappears out the door."
    $ clear_scene()
    "You look over at her computer screen. She has up notes on [the_trait.name], and has already submitted a request for testing a new catalyst."
    $ the_trait.add_mastery(2)
    "That girl is working herself so hard trying to keep up with everything, you are glad you have finally gotten her to open up with you."
    "She certainly NEEDs the opportunity to blow off some steam once in a while, which now she can get from you!"
    $ kaya.progress.love_step = 8
    $ add_kaya_sakari_cure_intro_action()
    $ the_person.apply_planned_outfit()
    # Once we actually do the sleeping kaya thing, probably link it here also. Maybe in lust arc instead?
    # After this event, we also need to add a new random crisis, where Kaya randomly makes a discovery regarding a medical trait.
    # Optional, she is having trouble figuring something out, you dick her down, and she suddenly makes a new discovery. Evening time slot only random crisis.
    return

label kaya_sakari_cure_intro_label():   #80
    # Outline
    # This storyline is not yet created. Kaya finally makes a link with medical serums that could cure her mother, but it would be costly, and require a lot of individualized research
    # Once complete, Kaya bypasses all obedience checks for the rest of the game, including obedience taboo breaks.
    # MC can also direct her to research other subjects at the business, allowing her to make random discoveries in her
    "In this label, we take the first step towards curing [sakari.fname]'s illness. Details have yet to be determined."
    $ kaya.progress.love_step = 8
    return


label kaya_research_development_label():
    $ the_person = kaya
    pass
    "This label is designed to be a random crisis that occurs only when [the_person.title] is working."
    "She makes a large leap of progress, advancing your mastery of a random medical serum trait by a lot."
    "Optionally, she might be struggling to make the final leap of logic, requiring MC to dick her down before she realises the final piece with post orgasm clarity."
    "This can probably copy paste a chunk of kaya_work_late_label, minus the virginity taking."
    return
