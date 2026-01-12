# Candace's obedience story involves her having problems due to her bimbo status and preference for public nudity.
# After a certain level of progress here and in her slut story, we introduce her to Starbuck, the sex shop owner.
# This arc is Candace's resisted story, but in the capstone we have the option to either cure her of her bimboism, or takeover as her legal protector
# Her capstone requires all other arcs to be completed, and once completed, changes her personality to Genius Candace

#Labels
label candace_browsing_tinder_at_work_label(the_person):
    # TODO: Write Story
    "Here candace is finding new ways to enjoy her new found freedom."
    $ add_candace_topless_at_mall_action()
    return

label candace_topless_at_mall_label(the_person):
    $ scene_manager = Scene()
    python:
        candace_check_police_chief_met()
        police_chief.wear_uniform() # make sure whe wears her uniform

    "As you walk around the mall, you notice a commotion. A small group of mostly men have gathered around someone, you walk over to see what is going on."
    "When you walk over, you find [the_person.possessive_title], and it immediately becomes clear why there is a crowd gathering around..."
    # TODO: Write Story for topless is legal
    # if mc.business.topless_is_legal():  #Right now it is always illegal
    #     pass
    # else:
    $ the_person.outfit.remove_all_upper_clothing()
    if the_person.vagina_visible or the_person.are_panties_visible:
        # she was wearing a dress so give her a skirt in her favourite colour to make her topless only
        $ the_person.outfit.add_lower(mini_skirt.get_copy(), colour_pink)

    $ scene_manager.add_actor(the_person, the_person.outfit)
    $ scene_manager.update_actor(the_person)
    "[the_person.title] is walking around the PUBLIC mall topless. Something that you are pretty sure is illegal."
    mc.name "[the_person.title], what are you doing?"
    the_person "Oh hey [the_person.mc_title]! Not much, I was just going for a little walk."
    "???" "Alright everyone, what seems to be the issue here? Let's move along now, okay?"
    "You look over. It's a police officer!"
    $ scene_manager.add_actor(police_chief, display_transform = character_left_flipped)
    police_chief "Come on now, let's all just go back to our shopping."
    "Suddenly, she sees [the_person.title]."
    police_chief "Move along now..."
    $ police_chief.call_dialogue("surprised_exclaim")
    $ scene_manager.update_actor(police_chief, emotion = "angry")
    police_chief "Excuse me Ma'am? You can't just walk around the mall with your titties out!"
    $ scene_manager.update_actor(the_person, emotion = "sad")
    the_person "I... I can't? Really? Why not?"
    police_chief "Ma'am... That's ILLEGAL! That is called public indecency!"
    the_person "But... everyone always loves it when I get my tits out..."
    police_chief "Sure, in the privacy of your own home you can do whatever, but this is a public place!"
    police_chief "I'm gonna have to run you in, now put your hands behind your back."
    "You decide to intervene."
    mc.name "I'm sorry officer, I know this looks bad, but I know her. I'll buy her a shirt really quick and get her covered up."
    mc.name "I'm sure she won't do it again!"
    "[police_chief.possessive_title!c] looks at you, then back at [the_person.title], then shakes her head."
    police_chief "I mean, there are worse crimes that could be committed here... Okay, just make it quick."
    if not mc.is_at(clothing_store):
        "You quickly grab [the_person.possessive_title]'s hand and lead her into the clothing store."
        $ mc.change_location(clothing_store)
    $ scene_manager.remove_actor(police_chief)
    "You grab the first t-shirt you find and have her put it on."
    $ the_person.outfit.add_upper(tanktop.get_copy(), [1.0, 1.0, 1.0, 1.0])
    $ scene_manager.draw_scene()
    the_person "This shirt is boring!"
    mc.name "[the_person.title], I know. But you can't be doing that, okay?"
    the_person "I still don't understand what I was doing wrong!"
    mc.name "There are laws in place! As nice as it would be, you can't just walk around in public, topless."
    mc.name "If you want to do that at work, that is fine, but you have to wear a shirt to the mall!"
    "[the_person.possessive_title!c] pouts."
    the_person "Okay. I'm sorry [the_person.mc_title], I didn't mean to cause you trouble."
    "You walk with [the_person.title] to the check-out counter. You have the cashier ring up the shirt."
    $ mc.business.change_funds(-20, stat = "Shopping")
    "After you check out, suddenly [the_person.possessive_title] turns to you and hugs you."
    $ scene_manager.update_actor(the_person, position = "kissing")
    the_person "Thank you. You've always been so nice to me..."
    "You put your hands on her back and hold her for a few seconds."
    "You start to wonder if she is going to be okay. Whatever happened that turned her into a bimbo, she seems to be barely functional."
    mc.name "You stay out of trouble, okay?"
    $ scene_manager.update_actor(the_person, emotion = "happy", position = "stand3")
    "[the_person.title] lets go of you and gives you a big smile."
    the_person "Okay!"
    mc.name "I'll see you at work."
    the_person "Yes Sir!"
    $ the_person.change_love(5, 60)
    $ the_person.change_location(the_person.home) # make her leave
    $ scene_manager.clear_scene()
    $ add_candace_midnight_wakeup_action()
    return

label candace_sex_toy_in_public_label(the_person):
    pass
    return

label candace_sex_with_vendor_label():
    pass
    return
