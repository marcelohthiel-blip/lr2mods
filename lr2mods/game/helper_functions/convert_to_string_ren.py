from __future__ import annotations
import renpy
import builtins
from renpy import persistent
from game.major_game_classes.character_related.Person_ren import Person

day = 0
time_of_day = 0

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 20 python:
"""
from typing import Callable, Generic, TypeVar
import re
from math import floor

@renpy.pure
def height_to_string(person_height: float) -> str: #Height is a value between 0.8 and 1.0
    height_in_inches = builtins.round((person_height * 100) / 1.5, 0)

    if persistent.use_imperial_system:
        return f"{floor(height_in_inches / 12):.0f}' {height_in_inches % 12:.0f}\""
    return f"{height_in_inches * 2.54:.0f} cm"

@renpy.pure
def feet_and_inches_to_cm(feet: int, inches: int) -> float:
    return ((feet * 12) + inches) * 2.54

@renpy.pure
def cm_to_feet_and_inches(cm: float) -> tuple[int, int]:
    inches = cm / 2.54
    return (inches // 12, builtins.int(inches % 12))

@renpy.pure
def SO_relationship_to_title(relationship_string: str) -> str:
    if relationship_string == "Girlfriend":
        return "boyfriend"
    if relationship_string == "Fiancée":
        return "fiancé"
    return "husband"

@renpy.pure
def girl_relationship_to_title(relationship_string: str) -> str:
    if relationship_string == "Girlfriend":
        return "girlfriend"
    if relationship_string == "Fiancée":
        return "fiancée"
    return "wife"

@renpy.pure
def get_obedience_string(obedience: int) -> str:
    if obedience < 50:
        return "Maverick"
    if obedience < 70:
        return "Disobedient"
    if obedience < 90:
        return "Freethinking"
    if obedience < 120:
        return "Respectful"
    if obedience < 150:
        return "Loyal"
    if obedience < 200:
        return "Docile"
    if obedience < 250:
        return "Devoted"
    return "Submissive"

@renpy.pure
def last_sex_to_string(day: int, value: int) -> str:
    if day - value == 0:
        return "Today"
    if day - value == 1:
        return "Yesterday"
    return f"{day - value} days ago"

opinion_names = ("hates", "dislikes", "has no opinion on", "likes", "loves")

@renpy.pure
def opinion_score_to_string(score: int) -> str:
    return opinion_names[score + 2]

remove_punctuation_regex = re.compile(r"[.,!;:()\?\"-']")

@renpy.pure
def safe_string(value: str) -> str:
    '''
    Replaces all { and } with {{ and }}.
    This is used to prevent the string from being interpreted as an expression
    when it is passed to f-string functions.
    '''
    if value is None:
        return ""
    return value.replace("{", "{{").replace("}", "}}")

@renpy.pure
def remove_punctuation(message: str) -> str:
    return remove_punctuation_regex.sub("", message)

remove_display_tags_regex = re.compile(r"([{[[].*?[]}])")

@renpy.pure
def remove_display_tags(message: str) -> str:
    return remove_display_tags_regex.sub("", message)

@renpy.pure
def capitalize_first_word(value: str) -> str:
    if value:
        groups = remove_display_tags_regex.sub("||", value).strip("||").split("||", 1)[0].split(None)
        position = next(re.finditer(groups[0], value))
        value = value[:position.start()] + value[position.start():position.end()].capitalize() + value[position.end():]
    return value

@renpy.pure
def get_color_value_for_fraction(percent: float) -> str:
    color_string = "#43B197"
    if percent < .5:
        color_string = "#e1e113"
    if percent < .2:
        color_string = "#f13355"
    return color_string

@renpy.pure
def get_inverted_color_value_for_fraction(percent: float) -> str:
    color_string = "#43B197"
    if percent > .5:
        color_string = "#e1e113"
    if percent > .8:
        color_string = "#f13355"
    return color_string

@renpy.pure
def get_energy_string(energy: int, max_energy: int) -> str:
    percent = energy * 1.0 / max(max_energy, 1)
    return f"{{color={get_color_value_for_fraction(percent)}}}{percent * 100:.0f}%{{/color}} {{image=energy_token_small}}"

@renpy.pure
def get_energy_number_string(energy: int, max_energy: int) -> str:
    percent = energy * 1.0 / max(max_energy, 1)
    return f"{{color={get_color_value_for_fraction(percent)}}}{energy:.0f}/{max_energy:.0f}{{/color}} {{image=energy_token_small}}"

@renpy.pure
def get_arousal_with_token_string(arousal: int, max_arousal: int) -> str:
    percent = arousal * 1.0 / max(max_arousal, 1)
    return f"{{color={get_inverted_color_value_for_fraction(percent)}}}{percent * 100:.0f}%{{/color}} {{image=arousal_token_small}}"

@renpy.pure
def get_arousal_number_string(arousal: int, max_arousal: int) -> str:
    percent = arousal * 1.0 / max(max_arousal, 1)
    return f"{{color={get_inverted_color_value_for_fraction(percent)}}}{arousal:.0f}/{max_arousal:.0f}{{/color}} {{image=arousal_token_small}}"

@renpy.pure
def get_locked_clarity_with_token_string(locked_clarity: int) -> str:
    percent = locked_clarity * 1.0 / 1000.0
    return f"{{color={get_inverted_color_value_for_fraction(percent)}}}{percent * 100:.0f}%{{/color}} {{image=lust_eye_token_small}}"

@renpy.pure
def get_locked_clarity_number_string(locked_clarity: int) -> str:
    percent = locked_clarity * 1.0 / 1000.0
    return f"{{color={get_inverted_color_value_for_fraction(percent)}}}{locked_clarity:.0f}/1000{{/color}} {{image=lust_eye_token_small}}"

@renpy.pure
def get_attention_string(attention: int, max_attention: int) -> str:
    percent = attention * 1.0 / max(max_attention, 1)
    return f"{{color={get_inverted_color_value_for_fraction(percent)}}}{percent * 100:.0f}%{{/color}}"

@renpy.pure
def get_attention_bleed_string(bleed: int, max_attention: int) -> str:
    percent = bleed * 1.0 / max(max_attention, 1)
    return f"-{percent * 100:.0f}%"

@renpy.pure
def get_attention_number_string(attention: int, max_attention: int) -> str:
    percent = attention * 1.0 / max(max_attention, 1)
    return f"{{color={get_inverted_color_value_for_fraction(percent)}}}{attention:.0f}/{max_attention:.0f}{{/color}}"

def get_person_weight_string(person: Person) -> str:
    kg = person.weight
    # add some weight based on number of days pregnant
    if person.pregnancy_is_visible:
        # calculates a factor for the current day in relation to show day and due day, multiplied by average pregnancy weight of 11.4 kg
        kg += (1 - ((person.pregnancy_due_day - day) / float(person.pregnancy_due_day - person.pregnancy_show_day))) * 11.4

    if persistent.use_imperial_system:
        return f"{kg * 2.205:.1f} lbs"
    return f"{kg:.1f} kg"

def get_baby_desire_format(person: Person) -> str:
    if person.baby_desire < -60:
        return (f"Loathsome ({person.baby_desire:.0f})")
    if person.baby_desire < -40:
        return (f"Horrifying ({person.baby_desire:.0f})")
    if person.baby_desire < -20:
        return (f"Frightening ({person.baby_desire:.0f})")
    if person.baby_desire < 0:
        return (f"Objectionable ({person.baby_desire:.0f})")
    if person.baby_desire < 20:
        return (f"Unwanted ({person.baby_desire:.0f})")
    if person.baby_desire < 40:
        return (f"Curious ({person.baby_desire:.0f})")
    if person.baby_desire < 60:
        return (f"Acceptable ({person.baby_desire:.0f})")
    if person.baby_desire < 80:
        return (f"Wanted ({person.baby_desire:.0f})")
    return (f"Extreme ({person.baby_desire:.0f})")

@renpy.pure
def person_body_shame_string(body_type: str, pronoun: str = "girl") -> str:
    if body_type == "curvy_body":
        return f"chubby {pronoun}"
    if body_type == "standard_body":
        return f"curvy {pronoun}"
    if body_type == "standard_preg_body":
        return f"pregnant {pronoun}"
    return f"skinny {pronoun}"

# instead of using 'call name' in menus, use the actual person name to avoid confusion
def format_titles(person: Person) -> str:
    person_title = f"{person.name} {person.last_name}"
    if person.is_stranger:
        return "???"    # we don't know her yet
    return f"{{color={person.char.who_args['color']}}}{{font={person.char.what_args['font']}}}{person_title}{{/font}}{{/color}}"

def format_titles_short(person: Person) -> str:
    person_title = person.name + " "
    if person.last_name and builtins.len(person.last_name) > 0:
        person_title += person.last_name[0] + "."
    if person.is_stranger:
        return "???"    # we don't know her yet
    return f"{{color={person.char.who_args['color']}}}{{font={person.char.what_args['font']}}}{person_title}{{/font}}{{/color}}"

month_names = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") #Arrays that hold the names of the days of the week and times of day. Arrays start at 0.
day_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #Arrays that hold the names of the days of the week and times of day. Arrays start at 0.
time_names = ("Early Morning", "Morning", "Afternoon", "Evening", "Night")
time_food_names = ("Breakfast", "Breakfast", "Lunch", "Dinner", "Midnight Snack")

def time_of_day_string(time_slot: int = None) -> str:
    if not time_slot:
        time_slot = time_of_day
    return time_names[time_slot].lower()

def time_of_day_food_string(time_slot: int = None) -> str:
    if not time_slot:
        time_slot = time_of_day
    return time_food_names[time_slot]

def day_and_time_string(game_day: int = None, time_slot: int = None):
    if not game_day:
        if game_day == 0:
            pass
        else:
            game_day = day
    if not time_slot:
        time_slot = time_of_day
    day_name = day_names[game_day % 7]
    day_part = time_names[time_slot]
    return f"{day_name} {day_part}"


def get_formatted_date_string(game_day: int = None, time_slot: int = None) -> str:
    if not game_day:
        game_day = day
    if not time_slot:
        time_slot = time_of_day
    day_name = day_names[game_day % 7]
    day_part = time_names[time_slot]
    return f"{day_name} {get_formatted_date_only_string(game_day)} - {day_part}"

def get_formatted_date_only_string(game_day: int = None) -> str:
    if not game_day:
        game_day = day
    day_in_month = (game_day % 30) + 1
    month_name = month_names[int((game_day / 30) + 8) % 12]
    return f"{month_name} {day_in_month}"


R = TypeVar("R")

class static_property(Generic[R]):
    def __init__(self, getter: Callable[[], R]) -> None:
        self.__getter = getter

    def __get__(self, obj: object, objtype: type) -> R:
        return self.__getter()

    @staticmethod
    def __call__(getter_fn: Callable[[], R]) -> static_property[R]:
        return static_property(getter_fn)

class StringInfo:
    @static_property
    def time_of_day_string() -> str:
        return time_of_day_string()

    @static_property
    def time_of_day_food_string() -> str:
        return time_of_day_food_string()

    @static_property
    def formatted_date_string() -> str:
        return get_formatted_date_string()

    @static_property
    def formatted_date_only_string() -> str:
        return get_formatted_date_only_string()
