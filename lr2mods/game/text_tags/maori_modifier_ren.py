####################################################
# Activate text modifier for person:			   #
# the_person.text_modifiers.append(maori_accent)   #
####################################################

from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person
from game.text_tags.generic_replacer_ren import letter_replacer, word_group_replacer, word_replace
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""


# word replacer (no special chars like - or ')
maori_dict = {
    "daughter": "tamāhine",
    "sacred": "tapu",
    "woman": "wahine",
    "yes": "āe",
    "god": "atua"
}

# letter replace (in word)
maori_replace_dict = {
    "wh": "vh",
}

# word group replacer
maori_word_group_dict = {
    "thank you ": "tēnā koe "
}

def maori_accent(person: Person, what: str):
    return word_replace(letter_replacer(word_group_replacer(what, maori_word_group_dict), maori_replace_dict), maori_dict)
