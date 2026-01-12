from __future__ import annotations
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

class RoomObject():
    def __init__(self, name: str, traits: list[str], sluttiness_modifier = 0, obedience_modifier = 0):
        self.name = name
        if isinstance(traits, list):
            self.traits = traits
        elif traits is None:
            traits = []
        else:
            self.traits = [traits]
        self.sluttiness_modifier = sluttiness_modifier #Changes a girls sluttiness when this object is used in a sex scene
        self.obedience_modifier = obedience_modifier #Changes a girls obedience when this object is used in a sex scene.

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: RoomObject) -> bool:
        if not isinstance(other, RoomObject):
            return NotImplemented
        return self.name == other.name

    def has_trait(self, the_trait: str) -> bool:
        return any(trait == the_trait for trait in self.traits)

    @property
    def formatted_name(self) -> str:
        if self.sluttiness_modifier == 0 and self.obedience_modifier == 0:
            return self.name

        the_string = [f"{self.name}\n{{menu_red}}"]
        if self.sluttiness_modifier != 0 or self.obedience_modifier != 0:
            modifiers = []
            if self.sluttiness_modifier != 0:
                modifiers.append(f"{self.sluttiness_modifier:+} Sluttiness")
            if self.obedience_modifier != 0:
                modifiers.append(f"{self.obedience_modifier:+} Obedience")
            the_string.append("Temporary Modifiers\n" + ", ".join(modifiers))

        the_string.append("{/menu_red} (tooltip)The object you have sex on influences how enthusiastic and obedient a girl will be.")
        return "".join(the_string)
