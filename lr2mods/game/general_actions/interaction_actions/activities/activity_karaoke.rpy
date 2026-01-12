# This is a file that contains the bar game Karaoke
# Currently not in the game, but planned in future content involving Candace.

init -1 python:
    BAR_DATE_GAME_KARAOKE_THRESHOLD = 18
    activity_names["karaoke"] = "Sing Karaoke"
    activity_response_list.append("karaoke")

    # Charisma and oral skill check, stats additive since it is checking if girl has fun.
    def bar_date_skills_karaoke(person):
        skill_total = mc.charisma + mc.oral_sex_skill + person.drink_level + person.charisma + person.oral_sex_skill
        #MAX possible totals: 10 + 10 + ~8 + 8 + 8 = 44?
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        return [skill_total, (skill_total + rand_roll)]

    

label bar_date_karaoke_label(the_person):
    #OUTLINE
    "In this label we sing karaoke with [the_person.title]."
    return False

label bar_group_date_karaoke_label(the_group):
    #OUTLINE
    "In this label we sing karaoke with the girls."
    return False