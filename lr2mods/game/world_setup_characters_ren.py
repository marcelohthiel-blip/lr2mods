from __future__ import annotations
import builtins
from game.helper_functions.list_functions_ren import get_random_from_list, people_with_job
from game.helper_functions.random_generation_functions_ren import create_random_person, create_stripper, make_person
from game.helper_functions.wardrobe_from_xml_ren import wardrobe_from_xml
from game.clothing_lists_ren import ponytail, long_hair, short_hair, messy_ponytail, shaved_side_hair, bobbed_hair
from game.personality_types._personality_definitions_ren import wild_personality, relaxed_personality, introvert_personality, reserved_personality, alpha_personality, bimbo_personality, cougar_personality
from game.major_game_classes.character_related.Person_ren import mc, list_of_patreon_characters
from game.major_game_classes.character_related._job_definitions_ren import JobDefinition, list_of_jobs, electronics_support_job, waitress_job, unemployed_job, bartender_job, student_job, salon_hairdresser_job, yoga_teacher_job, nurse_job, night_nurse_job, doctor_job, barista_job, hotel_maid_job, hotel_maid_job2
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""
def generate_patreon_character_list():
    global list_of_patreon_characters

    #original height 0.99
    dinah_wardrobe = wardrobe_from_xml("Dinah_Wardrobe")
    person_dinah = create_random_person(name = "Dinah", last_name = "Midari", body_type = "standard_body", height=1.035, skin="black",
        personality = alpha_personality, age_range = [30, 40], stat_array= [5, 5, 3], tits="D", hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style=short_hair, starting_wardrobe = dinah_wardrobe, type="unique")
    list_of_patreon_characters.append(person_dinah)

    #original height 0.96
    sylvia_wardrobe = wardrobe_from_xml("Sylvia_Wardrobe")
    person_sylvia = create_random_person(name = "Sylvia", last_name = "Weissfeldt", age_range = [45, 55], body_type = "curvy_body", height=0.99, skin="white", tits="C", hair_colour = ["dirty blonde", [0.663, 0.549, 0.373, 0.95]], hair_style = long_hair, starting_wardrobe = sylvia_wardrobe,
        personality = cougar_personality, stat_array = [6, 3, 2], skill_array = [3, 5, 2, 1, 1], sex_skill_array = [2, 3, 2, 4], type="unique")
    list_of_patreon_characters.append(person_sylvia)

    #original height 0.98
    # Well educated and raised in a very middle-class family.
    # Paige is a cool-headed young woman who has confidence without exuberance or extraversion.
    # her favourite activities are generally calm and solitary: reading, playing musical instruments, watching TV, etc.
    # She doesn't make friends quickly, but she is pleasant and easy to get along with, and the bonds she does cultivate are likely to last for life.
    # She has no passion for her work, but she is good at it and takes pride in that fact.
    paige_wardrobe = wardrobe_from_xml("Paige_Wardrobe")
    person_paige = create_random_person(name = "Paige", last_name = "Sallow", body_type = "thin_body", height = 1.02, skin = "white", tits="A", hair_colour = ["light auburn", [0.566, 0.332, 0.238, 0.95]], hair_style = messy_ponytail, starting_wardrobe = paige_wardrobe,
        personality = reserved_personality, job = electronics_support_job, stat_array = [1, 4, 3], skill_array = [5, 1, 2, 3, 2], sex_skill_array = [2, 1, 4, 2], type="unique")
    list_of_patreon_characters.append(person_paige)

    #original height 0.94
    # Kendra's family owns one of the largest pharmaceutical companies in the country. All of the Rivera children went to the finest prep schools.
    # Unlike her siblings, Kendra didn't inherit her parent's good looks or their general attitudes. She also disagreed with her families' viewpoint that being rich makes you better than everyone else.
    # This point of view put her at odds with everyone in her social class so she mostly hung out with the outcasts of her school.
    # By the time Kendra turned 16, she had grown into a stunningly beautiful woman and enjoyed the newfound attention she was receiving from boys. She was a free spirit, who just wanted to enjoy life.
    # When she graduated High School, she decided that college was not for her and pursued a career as glamor model. Kendra's parents were not pleased and cut her off financially but Kendra didn't care.
    # She was ready to be free and live her life.
    kendra_wardrobe = wardrobe_from_xml("Kendra_Wardrobe")
    person_kendra = create_random_person(name = "Kendra", last_name = "Rivera", age = 18, body_type = "curvy_body", height = 0.96, skin = "tan", hair_colour = ["chestnut", [0.59, 0.31, 0.18, 0.95]], hair_style = shaved_side_hair, starting_wardrobe = kendra_wardrobe,
        personality = relaxed_personality, stat_array = [4, 3, 1], skill_array = [5, 3, 1, 2, 2], sex_skill_array = [2, 2, 4, 1], face_style = "Face_4", type="unique")
    list_of_patreon_characters.append(person_kendra)

    #original height 1.00
    # Svetlanna moved to the fictional city from a fictional Russian land at the age of 16. She was always fascinated with biochemistry and when her mother became ill, she dove even deeper into her studies.
    # After graduating from public education, she immediately moved to higher studies. She was hell-bent to learn all she could to help her mother.
    # Unfortunately, her mother died before Svetlanna could find a cure for her mysterious disease, which put her into a deep depression.
    # After some time, she met a woman that rekindled her love for biotechnology and put her on the path of a wild woman, never tied down with any one man or woman.
    svetlanna_wardrobe = wardrobe_from_xml("Svetlanna_Wardrobe")
    person_svetlanna = create_random_person(name = "Svetlanna", last_name = "Ivanova", body_type= "thin_body", height = 1.05, skin = "white", tits="E", hair_colour = ["toasted wheat", [0.848, 0.75, 0.469, 0.95]], hair_style = long_hair, starting_wardrobe = svetlanna_wardrobe,
        personality = wild_personality, job = waitress_job, stat_array = [3, 1, 4], skill_array = [1, 3, 5, 2, 2], sex_skill_array = [2, 1, 2, 4], type="unique")
    person_svetlanna.set_opinion("research work", 2, False) #Always loves research work # Patron reward
    list_of_patreon_characters.append(person_svetlanna)

    #original height 0.98
    kelly_wardrobe = wardrobe_from_xml("Kelly_Wardrobe")
    person_kelly = create_random_person(name = "Kelly", last_name = "Uhls", body_type = "curvy_body", height = 1.02, skin = "white", eyes = "dark blue", tits = "E", hair_colour = ["knight red", [0.745, 0.117, 0.235, 0.95]], hair_style = ponytail, starting_wardrobe = kelly_wardrobe,
        personality = reserved_personality, stat_array = [2, 2, 4], skill_array = [2, 1, 2, 1, 5], sex_skill_array = [3, 4, 2, 1], type="unique")
    list_of_patreon_characters.append(person_kelly)

    #original height 0.90
    # sativa_wardrobe = wardrobe_from_xml("Sativa_Wardrobe")
    # Sativa's parents are very strict and traditional. They were determined to protect her from all the bad things in life, such as boys and booze.
    #When she turned 18,  Sativa moved out on her own.  Now she is determined to experience everything that she was previously denied.
    person_sativa = create_random_person(name = "Sativa", last_name = "Menendez", body_type = "curvy_body", face_style = "Face_7", height = 0.90, skin = "tan", eyes = "green", tits = "FF", hair_colour = ["barn red", [0.484, 0.039, 0.008, 0.95]], hair_style = bobbed_hair,
        personality = wild_personality, job = unemployed_job, stat_array = [3, 1, 4], skill_array = [2, 2, 1, 1, 5], sex_skill_array = [4, 3, 2, 1], type="unique")
    list_of_patreon_characters.append(person_sativa)

    #original height 0.96
    #nuoyi_wardrobe = wardrobe_from_xml("Nuoyi_Wardrobe") #NOTE: Patron did not want a specific wardrobe, she'll draw her wardrobe randomly as normal.
    person_nuyoi = create_random_person(name = "Nuoyi", last_name = "Pan", body_type = "thin_body", height = 0.99, skin = "white", eyes = "dark blue", tits = "FF", hair_colour = ["black", [0.09, 0.07, 0.09, 0.95]], hair_style = long_hair,
        personality = wild_personality, job = bartender_job, stat_array = [4, 3, 1], skill_array = [5, 2, 2, 1, 1], sex_skill_array = [1, 3, 4, 2], type="unique")
    list_of_patreon_characters.append(person_nuyoi)

    #original height 0.94
    # An exchange student who is doing a year abroad at a Catholic school. Especially to get away from her helicopter parents.
    lynn_wardrobe = wardrobe_from_xml("Lynn_Wardrobe")
    person_lynn = create_random_person(name = "Lynn", last_name = "Borch", body_type = "thin_body", height = 0.96, age = 19, skin = "white", eyes = "brown", tits = "C", hair_colour = ["light auburn", [0.566, 0.332, 0.238, 0.95]], hair_style = long_hair, starting_wardrobe = lynn_wardrobe,
        personality = introvert_personality, job = student_job, stat_array = [1, 3, 4], skill_array = [1, 2, 1, 5, 2], sex_skill_array = [2, 1, 5, 1], type="unique")
    person_lynn.set_opinion("cheating on men", -2, False) #Always hates cheating on men, you don't know this
    list_of_patreon_characters.append(person_lynn)

    #original height 0.95
    # Olga is a young library employee who likes to dress colourfully and is childish by behaviour.
    # As if she wants to overplay something.
    olga_wardrobe = wardrobe_from_xml("Olga_Wardrobe")
    person_olga = create_random_person(name = "Olga", last_name = "Schaad", body_type = "standard_body", height = 0.975, skin = "tan", eyes = "green", tits = "E", hair_colour = ["honey blonde", [0.745, 0.592, 0.471, 0.95]], hair_style = messy_ponytail, starting_wardrobe = olga_wardrobe,
        personality = bimbo_personality, stat_array = [4, 1, 3], skill_array = [2, 5, 2, 1, 1], sex_skill_array = [2, 4, 1, 1], type="unique")
    person_olga.set_opinion("working", 1, False) #Always likes working, you don't know this
    list_of_patreon_characters.append(person_olga)

    #original height 0.92
    # Svenja wants to become a fashion designer; she dropped out of college to do so and started working in a fashion boutique. She is 18 years old.
    # svenja_wardrobe = wardrobe_from_xml("Svenja_Wardrobe") #NOTE: Patron did not want a specific wardrobe, she'll draw her wardrobe randomly as normal.
    person_svenja = create_random_person(name = "Svenja", last_name = "Beitel", body_type = "standard_body", height = 0.93, skin = "white", eyes = "dark blue", tits = "B", hair_colour = ["platinum blonde", [0.792, 0.749, 0.694, 0.95]], hair_style = ponytail,
        personality = wild_personality, job = salon_hairdresser_job, age = 18, stat_array = [3, 1, 4], skill_array = [1, 3, 1, 5, 1], sex_skill_array = [3, 4, 1, 1], type="unique")
    list_of_patreon_characters.append(person_svenja)

    # anna_wardrobe = wardrobe_from_xml("Anna_Wardrobe") #NOTE: Patron did not provide a specific wardrobe; she'll draw from the default pool.
    person_anna = create_random_person(name = "Anna", last_name = "Kostenko", body_type = "thin_body", height = 0.93, skin = "white", eyes = "light blue", tits = "A", hair_colour = ["strawberry blonde", [0.644, 0.418, 0.273, 0.95]], hair_style = ponytail,
        personality = introvert_personality, job = yoga_teacher_job, age = 25, stat_array = [1, 3, 4], skill_array = [1, 1, 3, 3, 5], sex_skill_array = [1, 3, 4, 1], type = "unique")
    list_of_patreon_characters.append(person_anna)

def generate_random_characters():
    def create_new_characters(job: JobDefinition, max = 0):
        while len(people_with_job(job)) < max - 1:
            person = make_person(job = job)
            person.generate_home().add_person(person)

    for job in (x[0] for x in list_of_jobs):
        create_new_characters(job, 2)

    for job in (x for x in (waitress_job, bartender_job, barista_job, hotel_maid_job, hotel_maid_job2)):
        create_new_characters(job, 3)

    for job in (x for x in (nurse_job, night_nurse_job)):
        create_new_characters(job, 4)

    for job in (x for x in (unemployed_job, )):
        create_new_characters(job, 10)

def clear_alternating_days(job: JobDefinition):
    count = 0
    for person in people_with_job(job):
        if count % 2 == 0:
            person.primary_job.set_schedule(None, day_slots=[1, 3, 5])
        else:
            person.primary_job.set_schedule(None, day_slots=[0, 2, 4, 6])
        count += 1

def add_stripclub_strippers():
    for _ in builtins.range(0, 4):
        create_stripper()

    # make one of the strippers an alpha-personality (simplifies stripclub story-line)
    alpha_stripper = get_random_from_list([x for x in mc.business.stripclub_strippers if x.age >= 25 and not x.personality == alpha_personality])
    if not alpha_stripper: # fallback if we don't have an initial one old enough
        alpha_stripper = get_random_from_list([x for x in mc.business.stripclub_strippers if not x.personality == alpha_personality])
        alpha_stripper.age = 28

    if alpha_stripper:
        print(f"Converted stripper {alpha_stripper.name} to alpha personality.")
        alpha_stripper.change_personality(alpha_personality)
        alpha_stripper.charisma = 5
        alpha_stripper.int = 6
        alpha_stripper.update_opinion_with_score("taking control", 2, False)
        alpha_stripper.update_opinion_with_score("being submissive", -1, False)
