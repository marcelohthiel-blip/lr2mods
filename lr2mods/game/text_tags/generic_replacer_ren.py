from __future__ import annotations
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -20 python:
"""
import re
rc_word_finder = re.compile(r"\b[A-Za-z_]\w*\b(?!(\w*\.)?\w*\])")

# replace each word in text with word from replace_dict
def word_replace(text: str, replace_dict: dict[str, str]):
    def translate(match: re.Match[str]):
        word = match.group(0)
        found = replace_dict.get(word.lower(), word)

        # try to preserve casing of words
        if len(word) > 1 and word.isupper():
            return found.upper()
        elif word[0].isupper():
            return found.title()
        return found

    return rc_word_finder.sub(translate, text)

# removes last letter of each word if letter in last_letters string
def letter_dropper(text: str, last_letters = ""):
    def translate(match: re.Match[str]):
        word = match.group(0)
        if word[-1] in last_letters:
            return word[:-1]
        return word

    return rc_word_finder.sub(translate, text)

# replace letter combination in dictionary with replacement letters
def letter_replacer(text: str, letter_replace_dict: dict[str, str]):
    def translate(match: re.Match[str]):
        word = match.group(0)
        for f, r in letter_replace_dict.items():
            word = word.replace(f, r)
        return word

    return rc_word_finder.sub(translate, text)

# replace word combinations in dictionary
def word_group_replacer(text: str, word_replace_dict: dict[str, str]):
    def replace_keep_case(word: str, replacement: str, text: str):
        def func(match: re.Match[str]):
            g = match.group()
            if g.islower():
                return replacement.lower()
            if g.istitle():
                return replacement.title()
            if g.isupper():
                return replacement.upper()
            if g[0].isupper():
                return replacement[:1].upper() + replacement[1:]
            return replacement
        return re.sub(word, func, text, flags=re.I)

    for f, r in word_replace_dict.items():
        text = replace_keep_case(f, r, text)
    return text
