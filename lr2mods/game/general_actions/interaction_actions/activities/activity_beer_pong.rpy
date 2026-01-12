# This is a file that contains the bar game Beer Pong
# Introduced near the beginning of the game by Stephanie.

init -1 python:
    # BAR_DATE_GAME_RANDOM_MARGIN = 10         This is defined elsewhere, listed here for a coding reference
    activity_names["pong"] = "Beer Pong"
    activity_response_list.append("pong")

    # Pong uses focus and "foreplay" (hand skills). Drunker girls struggle more
    def bar_date_skills_pong(person):
        skill_dif = (mc.focus + mc.foreplay_sex_skill + person.drink_level) - (person.focus + person.foreplay_sex_skill)
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        if person == stephanie:
            skill_dif += (-5)
        return [skill_dif, (skill_dif + rand_roll)]


label bar_date_pong_label(the_person):
    $ mc_distraction = False
    $ date_distraction = False
    $ game_check = bar_date_skills_pong(the_person) # returns [int(advantage), int(result)]
    $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
    "You and [the_person.possessive_title] step over to one of the beer pong tables."
    "After pouring in the drinks and racking the cups, you being taking turns throwing the ping pong ball."
    if game_check[0] >= 0:  #MC advantage
        "You jump out to an early, leaving [the_person.title] trying to catch up."
        if bar_date_game_distraction_check(the_person, distraction_level = 1):
            if the_person.tits_visible: #Already out, so she taunts MC with them.
                the_person "Hey [the_person.mc_title], check this out!"
                $ the_person.draw_person(position = "kneeling1", display_transform = character_center_flipped(zoom = 0.9))
                "[the_person.possessive_title!c] leans over the side of the table, and shakes her chest back and forth for a moment."
            else:
                the_person "Hey [the_person.mc_title], look at this!"
                $ the_person.strip_to_tits(prefer_half_off = True)
                $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
                "[the_person.possessive_title!c] flashes her tits at you, giving them a good shake before restoring her clothing."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person(display_transform = character_center_flipped(zoom = 0.9))
            $ date_distraction = True
            $ mc.change_locked_clarity(40)
            $ the_person.change_arousal(10)
            $ game_check[1] += (-4)
            "Her distraction causes you to miss your next shot."
        if game_check[1] >= 0:  #mc wins
            if date_distraction:
                "However, despite the distraction, your lead is insurmountable."
            else:
                "She manages to string together a few good shots, but your lead turns out to be insurmountable."
            $ the_person.call_dialogue("activity_pong_response", mc_won = True)
            $ the_person.increase_drink_level(1)
            "[the_person.title] quickly finishes her drink."
            return True
        else:
            if date_distraction:
                "The distraction proves to be enough to get her in the lead, and somehow she accomplishes an impossible comeback."
            else:
                "Despite your early lead, she manages to string together several in a row, winning her the game." 
            $ the_person.call_dialogue("activity_pong_response", mc_won = False)    
    else:
        "[the_person.possessive_title!c] jumps out to an early lead."
        "You give it your best shot, managing to string together a few good shots here and there."
        if game_check[1] >= 0:  #mc wins
            "Somehow, you manage to string together several in a row, winning you the game, despite your slow start."
            $ the_person.call_dialogue("activity_pong_response", mc_won = True)
            $ the_person.increase_drink_level(1)
            "[the_person.title] quickly finishes her drink."
            return 1
        else:
            "You never manage to catch up with her though, and soon she sinks her final shot in victory."
            $ the_person.call_dialogue("activity_pong_response", mc_won = False)
    return False


# Use this label to make a group version in the future if we ever want to.
# label bar_date_group_pong_label(the_group):
#     pass
#     return