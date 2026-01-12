from __future__ import annotations
import renpy

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -100 python:
"""
import re

find_display_tags_regex = re.compile(r"([{[[].*?[]}])")

def convert_override(value, conv, scope):
    conv = set(conv)

    if 'r' in conv:
        value = repr(value)
        conv.discard('r')

    elif 's' in conv:
        value = str(value)
        conv.discard('s')

    if not conv:
        return value

    # All conversion symbols below assume we have a string.
    if not isinstance(value, str):
        value = str(value)

    if 't' in conv:
        value = renpy.translation.translate_string(value)

    if 'i' in conv:
        try:
            value = renpy.substitutions.interpolate(value, scope)
        except RuntimeError: # PY3 RecursionError
            msg = f"Substitution {value!r} refers to itself in a loop."
            raise ValueError(msg)

    if 'q' in conv:
        value = value.replace('{', '{{')

    if 'u' in conv:
        value = value.upper()

    if 'l' in conv:
        value = value.lower()

    if 'c' in conv:
        # find first text only group not in {} tags to get position of the first
        # printable word then capitalize that word
        groups = find_display_tags_regex.sub("||", value).strip("||").split("||", 1)[0].split(None)
        position = next(re.finditer(groups[0], value))
        value = value[:position.start()] + value[position.start():position.end()].capitalize() + value[position.end():]

    return value

renpy.substitutions.convert = convert_override


def convert_field_override(self, value, conversion):
    value, kwargs = value

    if conversion is None:
        return value

    if not conversion:
        msg = "Conversion specifier can't be empty."
        raise ValueError(msg)

    if set(conversion) - set("rstqulci!"):
        msg = 'Unknown symbols in conversion specifier, this must use only the "rstqulci".'
        raise ValueError(msg)

    if "r" in conversion:
        value = repr(value)
        conversion = conversion.replace("r", "")
    elif "s" in conversion:
        value = str(value)
        conversion = conversion.replace("s", "")

    if not conversion:
        return value

    # All conversion symbols below assume we have a string.
    if not isinstance(value, str):
        value = str(value)

    if "t" in conversion:
        value = renpy.translation.translate_string(value)

    if "i" in conversion:
        try:
            value = self.vformat(value, (), kwargs)
        except RuntimeError as exc: # PY3 RecursionError
            msg = f"Substitution {value!r} refers to itself in a loop."
            raise ValueError(msg) from exc

    if "q" in conversion:
        value = value.replace("{", "{{")

    if "u" in conversion:
        value = value.upper()

    if "l" in conversion:
        value = value.lower()

    if "c" in conversion and value:
        # find first text only group not in {} tags to get position of the first
        # printable word then capitalize that word
        groups = find_display_tags_regex.sub("||", value).strip("||").split("||", 1)[0].split(None)
        position = next(re.finditer(groups[0], value))
        value = value[:position.start()] + value[position.start():position.end()].capitalize() + value[position.end():]

    return value

# HOOK FOR DIFFERENT SDK VERSIONS
try:
    dummy = renpy.substitutions.Formatter()
    print("Using old conversion function")
    renpy.substitutions.Formatter.convert_field = convert_field_override
except:
    renpy.substitutions.convert = convert_override
    print("Using new conversion function")
