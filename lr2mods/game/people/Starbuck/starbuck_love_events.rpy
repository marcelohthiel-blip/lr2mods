# Starbuck's love path involves her getting over her lost husband and accepting that she might find someone else

# 20 love scene
label starbuck_coffee_time_label():
    $ mc.stats.change_tracked_stat("Girl", "Dates", 1)
    $ the_person = starbuck
    "You get a text on your phone. It appears to be from your new business partner, [the_person.title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey, you busy?"
    mc.name "A little, but not too much. What's up?"
    the_person "I'm dragging ass a bit this morning, and I was just going to grab some coffee."
    the_person "I wondered if maybe you would like to meet me there? We could talk about some ideas I had for the store."
    mc.name "I could use a coffee. I'll meet you there."
    $ mc.end_text_convo()
    "After determining the specifics, you head to the coffee shop downtown."
    $ mc.change_location(coffee_shop)
    $ starbuck.change_location(coffee_shop)
    $ starbuck.draw_person(position = "sitting")
    "When you get there, you spot [the_person.title] sitting at a table. You quickly order yourself a coffee and then go sit down next to her."
    $ mc.change_energy(20)
    the_person "Hey! Thanks for coming out on short notice."
    mc.name "Thanks for inviting me. I couldn't say no to a coffee date with you."
    "Your response takes her by surprise."
    the_person "Coffee... date? Ha, I didn't really think about it like that. Surely you have better prospects than a frumpy old widow like me."
    mc.name "Frumpy? Wow. Not at all how I would describe you. I was honestly excited to get the message."
    $ the_person.change_love(2)
    the_person "Ah, well that is very kind of you."
    "You both take a few sips of your coffees."
    mc.name "So how are things going at the shop? Has the stock investment been helpful?"
    the_person "Oh definitely! It helped me over the bump, I think I have enough stock now that I can turn inventory fast enough to turn a profit."
    the_person "The amount of stock I get in each day is actually overwhelming. It is so much work to put it all away."
    "She seems lost in thought for a moment."
    the_person "You know, if you had some extra time, you could swing by and help me put stock out."
    "Normally, an offer to help put out stock in a retail setting would be a quick pass."
    "However... putting out merchandise at a sex shop? And with [the_person.possessive_title]?"
    mc.name "I stay pretty busy with my own business, but I'll keep it in mind."
    $ the_person.change_happiness(2)
    the_person "Great!"
    "You chat with [the_person.title] for a while. It is nice to spend some time with her outside of her business."
    call small_talk_person(the_person) from _call_small_talk_starbuck_coffee_01
    "Soon, your coffees are consumed, and the morning is getting late."
    the_person "Well, I have a few things I need to take care of today. It was nice to have a coffee 'date', ha!"
    mc.name "We should do it again sometime."
    "She looks down at the table for a moment."
    the_person "You know... you should be careful."
    mc.name "Oh?"
    the_person "It isn't nice... to lead someone on. But I do appreciate you for humouring me."
    "Hmm, seems she doesn't believe that you would be interested in getting more involved with her."
    mc.name "[the_person.title]... I can't speak for every man in the world, but spending time with you is truly a pleasure. I look forward to doing it again."
    "[the_person.possessive_title!c] blushes a bit, but you see a smile on the corner of her lips."
    $ the_person.change_happiness(2)
    the_person "Well, I'll be going now. Take care [the_person.mc_title]!"
    $ the_person.draw_person()
    mc.name "Hang on a second."
    "You quickly stand up, then get close to her."
    "You lean forward to embrace her. She puts her arms up and you pull her close. You can feel her arms trembling."
    $ the_person.draw_person(position = "kissing")
    "After a few moments, you pull back just a bit, look her in the eyes, then lean forward for a kiss."
    $ the_person.break_taboo("kissing")
    "Your lips meet, and surprisingly hers meet yours eagerly. You test the waters with a bit of a tongue and she meets it with hers."
    $ mc.change_locked_clarity(25)
    "Soon you are making out with [the_person.possessive_title] right in the middle of the coffee shop."
    "???" "AHEM"
    "Someone nearby clears their throat, and you quickly realise this may not be the best place for this."
    $ the_person.draw_person()
    "[the_person.title] realises it too, and quickly pulls back."
    the_person "I umm, I really need to go... See you soon!"
    $ the_person.draw_person(position = "walking_away")
    "She turns to leave the coffee shop. You get a good look at her backside as she exits."
    $ mc.change_locked_clarity(15)
    $ starbuck.change_location(downtown)
    $ clear_scene()
    "[the_person.title] is such an interesting person. You have to wonder though, how long ago was it she lost her husband? Is she ready to move on?"
    "And if so, are you really interested? For now, you still have time to figure things out with her."
    # add the next step here.
    $ starbuck.progress.love_step = 1
    $ add_starbuck_rebound_talk_action()
    return


label starbuck_rebound_talk_label():
    # OUTLINE
    $ the_person = starbuck
    "In this label, MC and [starbuck.title] meet up for lunch."
    "She shares that she really enjoys spending time with MC, but she is worried."
    "She knows that she isn't over her husband's passing, and is worried she is treating MC like a rebound."
    "MC says he is willing to be a rebound, asks if shes ever considering counseling or therapy."
    "She says she can't really afford it, with the shop getting off the ground and the lack of health insurance."
    $ starbuck.progress.love_step = 2
    return
