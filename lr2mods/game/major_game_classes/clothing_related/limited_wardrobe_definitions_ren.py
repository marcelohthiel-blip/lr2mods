from __future__ import annotations
from game.game_roles._role_definitions_ren import generic_student_role
from game.major_game_classes.character_related._job_definitions_ren import prostitute_job
from game.major_game_classes.character_related.Person_ren import Person, erica, starbuck, mom
from game.major_game_classes.clothing_related.LimitedWardrobeCollection_ren import LimitedWardrobeCollection
from game.major_game_classes.clothing_related.LimitedWardrobe_ren import LimitedWardrobe
from game.map.MapHub_ren import gym_hub, university_hub, home_hub, aunt_home_hub, harem_hub

time_of_day = 0

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 10 python:
"""

def workout_wardrobe_validation(person: Person):
    return person.is_at(gym_hub)

def university_wardrobe_validation(person: Person):
    return person.is_at(university_hub) and person.has_role(generic_student_role)

def erica_workout_wardrobe_validation(person: Person):
    return person == erica and person.is_at(gym_hub)

def prostitute_wardrobe_validation(person: Person):
    return person.is_at_job(prostitute_job)

def sex_shop_wardrobe_validation(person: Person):
    return starbuck.progress.obedience_step >= 3 and person == starbuck and starbuck.is_at_work

def mom_home_wardrobe_validation(person: Person):
    return mom.progress.obedience_step >= 3 and person == mom and mom.is_at((home_hub, harem_hub))

def night_time_wardrobe_validation(person: Person):
    return (
        time_of_day == 4
        and (person.is_family and person.is_at((home_hub, aunt_home_hub))
             or person.is_home)
    )

def harem_wardrobe_validation(person: Person):
    return person.is_at(harem_hub)

def instantiate_limited_wardrobes():
    # limited wardrobes directly pick an outfit from the wardrobe for a specific person
    # when the validation requirement is met, that wardrobe is used to pick an outfit
    # use priority to determine which wardrobe has higher prevalence
    global limited_wardrobes
    limited_wardrobes = LimitedWardrobeCollection()

    global limited_workout_wardrobe
    limited_workout_wardrobe = LimitedWardrobe("Default_Workout_Wardrobe", 0, workout_wardrobe_validation, allow_personalisation = True)

    global limited_university_wardrobe
    limited_university_wardrobe = LimitedWardrobe("University_Wardrobe", 0, university_wardrobe_validation)

    limited_wardrobes.append(LimitedWardrobe("Erica_Workout_Wardrobe", 5, erica_workout_wardrobe_validation, allow_edit = False))
    limited_wardrobes.append(LimitedWardrobe("Prostitute_Wardrobe", 0, prostitute_wardrobe_validation, allow_personalisation = True))

    global sex_shop_wardrobe
    sex_shop_wardrobe = LimitedWardrobe("Sex_Shop_Wardrobe", 5, sex_shop_wardrobe_validation, allow_edit = False)

    global mom_home_wardrobe
    mom_home_wardrobe = LimitedWardrobe("Mom_Home_Wardrobe", 5, mom_home_wardrobe_validation, enforce_legal_status = False)

    global night_time_wardrobe
    night_time_wardrobe = LimitedWardrobe("Night_Time_Wardrobe", 0, night_time_wardrobe_validation, allow_edit = True, allow_personalisation = True, enforce_legal_status = False)

    global harem_wardrobe
    harem_wardrobe = LimitedWardrobe("Harem_Wardrobe", 10, harem_wardrobe_validation, allow_edit = True, allow_personalisation = False, enforce_legal_status = False)

    limited_wardrobes.extend((
        limited_workout_wardrobe,
        limited_university_wardrobe,
        sex_shop_wardrobe,
        mom_home_wardrobe,
        night_time_wardrobe,
        harem_wardrobe
    ))
