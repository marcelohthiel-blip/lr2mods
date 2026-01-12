# This is a file that contains the bar game Darts
# Introduced in an early date with Sarah.

init -1 python:
    # BAR_DATE_GAME_RANDOM_MARGIN = 10         This is defined elsewhere, listed here for a coding reference
    activity_names["darts"] = "Darts"
    activity_response_list.append("darts")

    # Foreplay and focus checks
    def bar_date_skills_darts(person):
        skill_dif = (mc.focus + mc.foreplay_sex_skill + person.drink_level) - (person.focus + person.foreplay_sex_skill)
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        return [skill_dif, (skill_dif + rand_roll)]

label bar_date_darts_label(the_person):
    $ mc_distraction = False
    $ date_distraction = False
    $ game_check = bar_date_skills_darts(the_person) # returns [int(advantage), int(result)]
    $ the_person.draw_person(display_transform = character_center_focus_flipped)
    "You and [the_person.possessive_title] step over to one of the dart boards."
    "There is a small table to one side where you can set your drinks while you play."
    if game_check[0] >= 0:  #MC advantage
        "After the first couple of turns, it is clear that you have the skill advantage."
        "[the_person.possessive_title] gives you a pouty face when you jump to an early lead."
        if bar_date_game_distraction_check(the_person, distraction_level = 3):
            $ clear_scene()
            "As you set up to throw your next round, you feel her presence strangely close behind you."
            "You feel [the_person.title]'s hands run a long your sides as she starts to hug you from behind."
            "One of her hands goes down and starts to rub your cock through your pants as she whispers in your ear."
            the_person "The things you can do with your hands are amazing..."
            $ date_distraction = True
            $ mc.change_locked_clarity(50)
            $ the_person.change_arousal(10)
            $ game_check[1] += (-6)
            "Her words send a shiver up your spine. She is clearly attempting to distract you, and you do your best to concentrate on the darts game."
            "You throw the round and then turn back to her."
            $ the_person.draw_person(display_transform = character_center_flipped(zoom = 1.2))
        elif bar_date_game_distraction_check(the_person, distraction_level = 2):
            "After you throw a round, you look at [the_person.possessive_title]."
            $ the_person.draw_person(position = "standing_doggy", display_transform = character_center_flipped(zoom = 1.2))
            "She is leaning over, picking up her darts that she set down on the side table. She is obviously wiggling her hips at you and taking her time picking up the darts."
            if the_person.vagina_visible:
                "You check out her ass as she wiggles it. She looks back at you and catches you checking her out."
                the_person "Like what you see, [the_person.mc_title]?"
                mc.name "Absolutely."
            else:
                "You check out her ass as she wiggles it. She looks back at you and catches you checking her out."
                the_person "Checking out my ass?"
                "Before you can respond, she quickly flashes you her ass."
                $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy", display_transform = character_center_flipped(zoom = 1.2))
                "You just watch as she wiggles her exposed ass at you for a few moments, then strands up and straighten her outfit."
                $ the_person.apply_planned_outfit()
            $ the_person.draw_person(display_transform = character_center_flipped(zoom = 1.2))
            $ date_distraction = True
            $ mc.change_locked_clarity(40)
            $ the_person.change_arousal(10)
            $ game_check[1] += (-4)
            "She is clearly attempting to distract you, and you do your best to concentrate on the darts game, but you find yourself thinking about her ass wiggling back and forth..."
        if game_check[1] >= 0:  #mc wins
            if date_distraction:
                "However, despite the distraction, your lead is insurmountable."
            else:
                "She manages to string together a few throws, but your lead turns out to be insurmountable."
            $ the_person.call_dialogue("activity_darts_response", mc_won = True)
            $ the_person.increase_drink_level(1)
            "[the_person.title] quickly finishes her drink."
            return True
        else:
            if date_distraction:
                "Unfortunately, her distraction works, and somehow she accomplishes an impossible comeback."
            else:
                "Despite your early lead, she manages to string together several throws in a row, winning her the game." 
            $ the_person.call_dialogue("activity_darts_response", mc_won = False)
    else:
        "After the first couple of turns, it is clear that you are at a disadvantage."
        "You might have to get creative if you want to win this game."
        menu:
            "Try and distract her":
                $ the_person.draw_person(position = "walking_away", display_transform = character_center_flipped(zoom = 1.2))
                "[the_person.possessive_title!c] is setting up her next set of throws, when you get an idea."
                "You step close behind her, putting your hands on her hips, then lean forward to whisper in her ear."
                if the_person.effective_sluttiness() < 20:  #Hell nah
                    "Before you can enact your plan, she gives you a quick elbow to the gut."
                    $ the_person.draw_person(position = "back_peek", display_transform = character_center_flipped(zoom = 1.2))
                    the_person "Hands off mister. Nothing can stop me from dominating this game."
                    "Oof. Your plan appears to have backfired. You move away, and she seems even more focused than before."
                    $ mc_distraction = False
                    $ game_check[1] += (-3)
                elif the_person.effective_sluttiness() > 60:    #Hell yeah
                    mc.name "No wonder you are so good at this game, your form is amazing..."
                    "You feel her entire body shiver at your unexpected touch. You move forward, pressing your body against hers."
                    the_person "Ahhh, good to know my form is... appreciated..."
                    "After a few seconds, you let go and back away. She is glancing back at you, clearly distracted as she starts her next set of throws."
                    $ mc_distraction = True
                    $ mc.change_locked_clarity(40)
                    $ the_person.change_arousal(20)
                    $ game_check[1] += (6)
                else:
                    mc.name "You have a great form, no wonder you are so good at darts."
                    "She startles for a moment at your touch, but chuckles and gives you a playful elbow to get you to back away."
                    the_person "Glad to know my form is appreciated, but stop trying to distract me!"
                    "You back away, but she glances back at you throughout her next set of throws. You were able to distract her a little bit, at least."
                    $ mc_distraction = True
                    $ mc.change_locked_clarity(20)
                    $ the_person.change_arousal(5)
                    $ game_check[1] += (2)
            "Try to focus":
                "You don't want to cause a scene, so you just focus on playing as well as you can."
        if game_check[1] >= 0:  #mc wins
            if mc_distraction:
                "While she plays distracted, you manage to string together a series of excellent throws and win the game."
            else:
                "Somehow, through sheer force of will, you manage to string together a series of excellent throws and win the game."
            $ the_person.call_dialogue("activity_darts_response", mc_won = True)
            $ the_person.increase_drink_level(1)
            "[the_person.title] quickly finishes her drink."
            return True
        else:
            if mc_distraction:
                "For a while, it seems you might be able to come back, but [the_person.possessive_title] dominates the final throws."
            else:
                "Unfortunately, you have no chance of catching up. [the_person.possessive_title] wins the game easily." 
            $ the_person.call_dialogue("activity_darts_response", mc_won = False)
    return False

label bar_group_date_darts_label(the_group):
    #OUTLINE
    "In this label we play darts with the girls."
    return False