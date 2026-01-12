####################################################
# Activate text modifier for person:			   #
# the_person.text_modifiers.append(southern_belle) #
####################################################

from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person
from game.text_tags.generic_replacer_ren import letter_replacer, word_group_replacer, word_replace

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""

# word replacer (no special chars like - or ')

southern_dict = {
    "everyone": "y'all",
    "mouth": "gizzard",
    "happy": "tickled pink",
    "stop": "cut",
    "crazy": "ding-dong",
    "suppose": "reckon'",
    "supposed": "reckon'd",
    "get": "git",
    "on": "own",
    "my": "mah",
    "can": "cain",
    "daddy": "diddy",
    "father": "diddy",
    "said": "sayd",
    "sweet": "swate",
    "hello": "howdy",
    "a": "ah",
    "you": "yah",
    "to": "tuh",
    "nice": "fine",
    "your": "yahr",
    "here": "heah",
    "like": "lahk",
    "red": "ray-ed",
    "for": "fer",
    "just": "jis",
    "did": "done",
    "already": "done",
    "mom": "mahma",
    "mother": "mahma",
    "true": "right",
    "cute": "precious",
    "aunt": "ant",
    "swallow": "swalluh",
    "yellow": "yelluh",
    "haven't": "ain't",
    "children": "chillins",
    "pants": "britches",
    "darn": "dagnabit",
    "himself": "hisself",
    "yes": "yessir",
    "something": "sumthing",
    "things": "thangs",
    "because": "cuz",
    "love": "luv",
    "what": "whut",
    "want": "wonna",
    "nothing": "nuthing",
}

# letter replace (in word)
southern_replace_dict = {
    "ing": "in'",
    "some": "sum",
    "other": "uther",
    "irst": "urst",
    "og": "awg",
}

# word group replacer
southern_word_group_dict = {
    "over there ": "over yonder",
    "hold on ": "hold your horses",
    "be quiet ": "hush up",
    "stop talking ": "hush up",
    "stop it": "cut that out",
    "give me a kiss": "gimme some sugar",
    "going": "fixing",
    "I think": "I reckon",
    "take it easy": "hold your horses",
    " is not ": " ain't ",
    " is all ": " 'sall ",
    "got a ": "gotta ",
    "isn't": "ain't",
    "going to": "gonna",
    "have to": "havta",
    "got to": "gotta",
    " ought to": " oughta",
    "want to": "wanna",
    "wanted to": "wanna",
    " am not ": " ain't ",
    " are not ": " ain't ",
    "aren't": "ain't",
    "you all": "y'all",
    "let me": " lemme",
    "stop that": "cut it out",
    "there you go": "air ye go",
    "very good": "real good",
    "yes sir": "yes", # replace with yes (word replacer will make it yessir)
    " is ": "'s ",   # often dropped in southern accent
    " are ": "'re ",  # should result in (those are -> those're)
    "supposed to": "s'posed ta", #fixes bad word replacement e.g. "That wasn't supposed to happen" -> "That's wasn't reckon'd tuh happen"
}

def southern_belle(person: Person, what: str):
    return word_replace(letter_replacer(word_group_replacer(what, southern_word_group_dict), southern_replace_dict), southern_dict)
