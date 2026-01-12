# This is a file that contains the bar game Trivia
# Introduced through Nora and Stephanie's weekly meetings.

init -1 python:
    BAR_DATE_GAME_TRIVIA_THRESHOLD = 15
    activity_names["trivia"] = "Trivia Contest"
    activity_response_list.append("trivia")

    trivia_smart_answers = [
        "Who is Jane Austen?",
        "What is sedementary rock?",
        "What is quantum entanglement?",
        "Who is the Goths?",
        "What is Venus?",
        "Who is Warren G. Harding?",
        "What is a flamboyance?",
        "Who is McDonnell Douglas?",
        "Who was Nancy Smith?"
    ]

    # Team game, checks intelligence and RND. WORSE odds when drunk
    def bar_date_skills_trivia(person):
        skill_total = (mc.int + mc.research_skill + person.int + person.research_skill) - person.drink_level
        #MAX possible totals: 10 + 10 + 8 + 8 = 36?
        if person == nora:
            skill_total += 5
        rand_roll = renpy.random.randint(-BAR_DATE_GAME_RANDOM_MARGIN, BAR_DATE_GAME_RANDOM_MARGIN)
        return [skill_total, (skill_total + rand_roll)]
    

label bar_date_trivia_label(the_person):
    $ game_check = bar_date_skills_trivia(the_person)
    "At a small group of tables, you sign up for couples trivia with [the_person.possessive_title]."
    "There are a few other couples there, and the host explains the rules as things get ready to start."
    "Thankfully, either person can answer the questions, so you get ready to try and impress [the_person.possessive_title]."
    "The trivia game begins."
    if game_check[0] >= BAR_DATE_GAME_TRIVIA_THRESHOLD: #Early lead
        "You jump out to an early lead against the other couples."
        $ smart_answer = get_random_from_list(trivia_smart_answers)
        if the_person.int >= mc.int or the_person == nora:
            the_person "[smart_answer]"
            "Host" "That's correct! Another point for your team."
            the_person "Yes!"
            $ the_person.change_happiness(1)
            "[the_person.title] is breezing through the questions."
        else:
            mc.name "[smart_answer]"
            "Host" "That's correct! Another point for your team."
            the_person "Wow, how'd you know that?"
            $ the_person.change_love(1, 50)
            $ the_person.change_obedience(1, 150)
        if game_check[1] >= BAR_DATE_GAME_TRIVIA_THRESHOLD: #Winners
            "Your lead is so overwhelming, other teams start to make mistakes just trying to catch up."
            "Host" "Alright! That's the game. Here are our winners, by a landslide!"
            $ the_person.change_happiness(10)
            $ the_person.change_love(3, 40)
            $ the_person.draw_person(emotion = "happy")
            $ the_person.call_dialogue("activity_trivia_response", mc_won = True)
        else:
            "However, you get a little cocky and start to get a few questions wrong."
            "During the final round, you confidently answer the game winning question wrong."
            "The host walks over to another couple and declares them the winners."
            $ the_person.draw_person(emotion = "sad")
            $ the_person.call_dialogue("activity_trivia_response", mc_won = False)
    else:
        "As the game starts, you are facing some stiff competition."
        "You fall behind a few questions, and you are trailing leading into the final round."
        if game_check[1] >= BAR_DATE_GAME_TRIVIA_THRESHOLD:
            $ smart_answer = get_random_from_list(trivia_smart_answers)
            if the_person.int >= mc.int or the_person == nora:
                the_person "[smart_answer]"
                "Host" "That's correct! You win the game."
                the_person "Yessss!"
                $ the_person.change_happiness(10)
                $ the_person.change_love(3, 40)
                $ the_person.draw_person(emotion = "happy")
                $ the_person.call_dialogue("activity_trivia_response", mc_won = True)
            else:
                mc.name "[smart_answer]"
                "Host" "That's correct! Another point for your team."
                the_person "Wow! How'd you know that? That was amazing!"
                $ the_person.change_obedience(3, 150)
                $ the_person.change_happiness(10)
                $ the_person.change_love(3, 40)
                $ the_person.draw_person(emotion = "happy")
                $ the_person.call_dialogue("activity_trivia_response", mc_won = True)
        else:
            if the_person.int >= mc.int or the_person == nora:
                "[the_person.possessive_title!c] manages to string together a few correct answers, but it just isn't enough."
                "You blunder the final question, and your team loses by a few points."
                the_person "UGH, so close!"
                $ the_person.draw_person(emotion = "sad")
                $ the_person.call_dialogue("activity_trivia_response", mc_won = False)
            else:
                "You manage to string together a few correct answers keeping you within range of winning until the final round."
                "Unfortunately, [the_person.title] blunders the final answers."
                $ the_person.draw_person(emotion = "sad")
                the_person "I'm so sorry [the_person.mc_title]! If only I'd known that final question."
                mc.name "Don't worry about it. I learned something and had fun too."
                $ the_person.change_love(1, 40)
                $ the_person.change_obedience(1, 60)
                $ the_person.call_dialogue("activity_trivia_response", mc_won = False)

    if game_check[1] >= BAR_DATE_GAME_TRIVIA_THRESHOLD:
        "You and [the_person.title] grab your free shot from the bar and quickly down it."
        mc.name "To victory!"
        the_person "Cheers!"
        $ the_person.increase_drink_level(1)
    return False

label bar_group_date_trivia_label(the_group):
    #OUTLINE
    "In this label we do trivia with the girls."
    return False