# This is a file that contains the bar game Billiards
# Introduced by Kaya as part of her bar date storyline.

init -1 python:
    # BAR_DATE_GAME_RANDOM_MARGIN = 10         This is defined elsewhere, listed here for a coding reference
    activity_names["billiards"] = "Billiards"
    activity_response_list.append("billiards")

    # Intelligence and focus checks
    def bar_date_skills_billiards(person):
        skill_dif = (mc.focus + mc.int + person.drink_level) - (person.focus + person.int)
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        return [skill_dif, (skill_dif + rand_roll)]

    

label bar_date_billiards_label(the_person):
    "In this scene, you face off against [the_person.possessive_title] in a game of pool."
    "The only problem is, Starbuck hasn't written this stuff yet!"
    "You might have the opportunity to distract her with tickling, smacking her ass, or more."
    "It will be included in a future bar date update... until then..."
    menu:
        "You win!":
            return True
        "You Lose!":
            return False
        # "Simulate Game":
        #     $ won_game = billiards_simulate_game(the_person)
        #     if won_game:
        #         "The simulation resolves based on your skills. You win!"
        #         return True
        #     else:
        #         "The simulation resolves based on your skills. You lose!"
        #         return False
    return False