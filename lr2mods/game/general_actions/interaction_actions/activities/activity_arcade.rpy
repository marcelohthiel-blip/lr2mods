# This is a file that contains the bar game Super Street Kombat 2
# Introduced through Myra and her gaming cafe storyline

init -1 python:
    # BAR_DATE_GAME_RANDOM_MARGIN = 10         This is defined elsewhere, listed here for a coding reference
    activity_names["arcade"] = "Super Street Kombat 2"
    activity_response_list.append("arcade")

    # Skill check focus + production_skill (micro?)
    def bar_date_skills_arcade(person):
        skill_dif = (mc.focus + mc.production_skill + person.drink_level) - (person.focus + person.production_skill)
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        return [skill_dif, (skill_dif + rand_roll)]

    

label bar_date_arcade_label(the_person):
    $ mc_distraction = False
    $ date_distraction = False
    "In this scene, you square off against [the_person.title] playing the legendary arcade game Super Street Kombat 2 Turbo."
    "The only problem is, Starbuck hasn't written this stuff yet!"
    "You might have the opportunity to distract her with tickling, smacking her ass, or more."
    "It will be included in a future bar date update... until then..."
    if the_person.focus + the_person.foreplay_sex_skill + the_person.drink_level > mc.focus + mc.foreplay_sex_skill:
        "[the_person.possessive_title!c] wins the match easily!"
        return False
    else:
        "You beat [the_person.title] easily!"
        return True
    return False