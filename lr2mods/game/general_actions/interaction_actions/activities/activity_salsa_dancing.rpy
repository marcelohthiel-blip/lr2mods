# This is a file that contains the baractivity salsa dancing
# Introduced thru Camila and Salsa dancing lessons.

init -1 python:
    BAR_DATE_GAME_SALSA_THRESHOLD = 20         # Thresholds are combined scored that make the associated game a "success"
    activity_names["salsa"] = "Salsa Dancing"
    activity_response_list.append("salsa")

    # salsa checks if partner is having fun. ADDS mc and partner salsa skills. A good partner makes an easy success
    def bar_date_skills_salsa(person):
        skill_total = mc.charisma + builtins.int((mc.max_energy - 100) / 20) + mc.market_skill + person.drink_level + person.charisma + person.market_skill
        #MAX possible totals: 10 + 10 + 10 + ~8 + 8 + 8 = 54?
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        return [skill_total, (skill_total2 + rand_roll)] #At max stats MC and min stats, non drunk person, 24 skill check gives 90% success rate. 2 drinks gives 100%


label bar_date_salsa_label(the_person):
    $ game_check = bar_date_skills_salsa(the_person) # returns [int(advantage), int(result)]
    $ the_person.draw_person(display_transform = character_center_focus_flipped)
    $ skilled_date = ((the_person.drink_level + the_person.charisma + the_person.market_skill) >= 8)
    "You take [the_person.title]'s hand and head to the dance floor. An upbeat salsa song is just beginning, and you begin to dance with her."
    if skilled_date:
        "[the_person.possessive_title!c] starts quick and make a move away from you a bit, allowing her to make a graceful spin back to you."
        $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus_flipped)
        "She spins beautifully and stops with her back to you. She looks back and gives you a sly smile."
        if game_check[0] >= BAR_DATE_GAME_SALSA_THRESHOLD:
            "You easily lead her into a reverse spin out the other side."
            if the_person.has_skirt or the_person.has_dress:
                "Her skirt flares up as she spins gracefully and then returns to your side."
            else:
                "She spins gracefully and then returns to your side."
            $ mc.change_locked_clarity(10)
            $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
            "She smiles, clearly impressed as you match her dancing step for step."
            $ the_person.change_stats(happiness = 2, love = 3, max_love = 60)
            if game_check[1] >= BAR_DATE_GAME_SALSA_THRESHOLD:  #It goes well
                "You match your skilled partner with moves of your own. Throughout the first song and the next you have her spinning and moving to the music."
                $ the_person.draw_person(position = "stand2", display_transform = character_center_focus)
                "You take every opportunity to show off your skilled partner to the rest of the dance floor, and when an opportunity arises to bring your bodies together..."
                $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus)
                "You take it. In one spin, you feel yourself pressing up against her backside. She hesitates for a moment to grind herself against you before spinning back out."
                $ mc.change_locked_clarity(30)
                $ the_person.change_slut(2, 50)
                $ the_person.change_arousal(20)
                $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
                "Next time you are face to face, her breathing has picked up a little. She seems to be getting a little excited..."
                "When the second song ends, you are both a little out of breath and decide to be done."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = True)
            else:
                "However, you get a little cocky. You take every opportunity to run your hands over and grind against your dance partner."
                $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus)
                "One time, when she spins back towards you, you have a little incident trying to get too close to her."
                "It knocks her off balance and she gives you a fiery look."
                $ the_person.draw_person(position = "stand2", display_transform = character_center_focus, emotion = "angry")
                the_person "Hey, watch it! This is suppose to be dancing, not grinding."
                mc.name "Sorry."
                $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
                "She rolls her eyes but gets back to dancing."
                "When the second song is over, you both decide to be done."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = False)

        else:
            "Unfortunately you fumble a bit as she spins back out. You don't trip but you definitely feel awkward compared to the grace your partner is exhibiting."
            $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
            "[the_person.title] whispers in your ear."
            the_person "Don't worry, you are doing great!"
            $ the_person.change_stats(happiness = 2, love = 1, max_love = 40)
            if game_check[1] >= BAR_DATE_GAME_SALSA_THRESHOLD:
                "You do your best to keep up with your date, but thankfully she doesn't do anything too difficult."
                $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus)
                "One time when she does another spin and you start to dance behind her, you feel her hesitate for a moment to push her ass back against you."
                "You feel her body grind against yours for a few seconds before she spins back away from you."
                $ mc.change_locked_clarity(30)
                $ the_person.change_slut(2, 50)
                $ the_person.change_arousal(20)
                $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
                "Next time you are face to face, her breathing has picked up a little. She seems to be getting a little excited..."
                "When the second song ends, you are both a little out of breath and decide to be done."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = True)
            else:
                "You do your best to keep up with your date, but it is clear as you start the second song that your skill level is holding her back a little."
                $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus)
                "One time when she does a little spin and turns her back to you, you bump into each other awkwardly."
                mc.name "Sorry, I'm not very good at this."
                the_person "It's okay, I guess you're trying..."
                $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
                "She rolls her eyes but gets back to dancing."
                "When the second song is over, you both decide to be done."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = False)

    else:
        "[the_person.possessive_title!c] is a little awkward, so you take the lead. You push back a bit creating some space, then pull her back to you, spinning her as you do."
        $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus_flipped)
        "She spins awkwardly and stops with her back to you. She looks back and gives you a nervous smile."
        the_person "Sorry, I don't think I'm very good at this."
        if game_check[0] >= BAR_DATE_GAME_SALSA_THRESHOLD:
            mc.name "Don't worry, just follow my lead."
            "You easily lead her into a reverse spin out the other side."
            if the_person.has_skirt or the_person.has_dress:
                "Her skirt flares up as she spins and then returns to your side."
            $ mc.change_locked_clarity(10)
            $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
            "She smiles, clearly impressed as you lead the dance."
            $ the_person.change_stats(happiness = 2, love = 3, max_love = 60, obedience = 2, max_obedience = 150)
            if game_check[1] >= BAR_DATE_GAME_SALSA_THRESHOLD:
                "Throughout the first song and the next you have her spinning and moving to the music."
                $ the_person.draw_person(position = "stand2", display_transform = character_center_focus)
                "You take every opportunity to show off your partner to the rest of the dance floor, and when an opportunity arises to bring your bodies together..."
                $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus)
                "You take it. In one spin, you feel yourself pressing up against her backside. She hesitates for a moment to grind herself against you before spinning back out."
                $ mc.change_locked_clarity(30)
                $ the_person.change_slut(2, 50)
                $ the_person.change_arousal(20)
                $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
                "Next time you are face to face, her breathing has picked up a little. She seems to be getting a little excited..."
                "When the second song ends, you are both a little out of breath and decide to be done."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = True)
            else:
                "However, the pressure of trying to lead everything is a little bit much. You make a couple mistakes, and you bump into each other awkwardly."
                the_person "Ah, sorry!"
                "She apologizes over and over, but you reassure her you are just out to have fun."
                "When the second song ends, she asks to be done."
                the_person "That was fun, but can we be done now?"
                mc.name "Sure."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = False)
        else:
            mc.name "I'm not very good either, let's just have some fun with it."
            "She grimaces."
            the_person "Ah... okay... let's see what happens."
            if game_check[1] >= BAR_DATE_GAME_SALSA_THRESHOLD:
                $ the_person.draw_person(position = "kissing", display_transform = character_center_focus)
                "And have fun is what you do. What you wind up doing isn't really 'salsa', but you and your partner have fun anyway."
                $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus)
                "You spin her around a couple times, and she smiles when she stops."
                $ the_person.draw_person(position = "stand2", display_transform = character_center_focus)
                the_person "Woo! Alright, that's enough spinning for tonight, haha!"
                "When the second song ends, you decide not to press your luck."
                mc.name "That was fun."
                the_person "Yeah, but let's be done..."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = True)
            else:
                "You try to have fun dancing with [the_person.possessive_title], but the lack of skill from both of you is apparent."
                "You wind up stepping on each other's feet and bumping into one another and other couples awkwardly."
                "When the second song ends, you are both ready to be done."
                the_person "That was fun, but can we be done now?"
                mc.name "Sure."
                $ the_person.call_dialogue("activity_salsa_response", mc_won = False)
    $ the_person.draw_person(position = "stand2", display_transform = character_center_focus)
    return False