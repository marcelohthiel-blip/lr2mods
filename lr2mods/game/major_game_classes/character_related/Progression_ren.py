from __future__ import annotations
from functools import cached_property
from game.helper_functions.misc_helpers_ren import call_global_func, has_global_func
from game.major_game_classes.character_related.Person_ren import Person

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""

class Progression():
    def __init__(self, person: Person):
        self.person = person

    def __hash__(self) -> int:
        return hash(self.person)

    def __eq__(self, other: Progression) -> bool:
        if not isinstance(other, Progression):
            return NotImplemented
        return self.person == other.person

    def __getstate__(self) -> dict:
        state = self.__dict__.copy()
        for x in ("has_description", "has_love_story", "has_lust_story", "has_obedience_story"):
            state.pop(x, None)
        return state

    @property
    def love_step(self) -> int:
        return self.person.event_triggers_dict.get("love_step", 0)

    @love_step.setter
    def love_step(self, value: int):
        self.person.event_triggers_dict["love_step"] = value

    @property
    def lust_step(self) -> int:
        return self.person.event_triggers_dict.get("lust_step", 0)

    @lust_step.setter
    def lust_step(self, value: int):
        self.person.event_triggers_dict["lust_step"] = value

    @property
    def obedience_step(self) -> int:
        return self.person.event_triggers_dict.get("obedience_step", 0)

    @obedience_step.setter
    def obedience_step(self, value: int):
        self.person.event_triggers_dict["obedience_step"] = value

    @cached_property
    def has_description(self) -> bool:
        return self.__has_global_func(f"{self.person.func_name}_story_character_description")

    @property
    def story_character_description(self) -> str:
        return self.__call_global_func(f"{self.person.func_name}_story_character_description", "")

    @cached_property
    def has_love_story(self) -> bool:
        return self.__has_global_func(f"{self.person.func_name}_story_love_list")

    @property
    def story_love_list(self) -> dict[int, str]:
        return self.__call_global_func(f"{self.person.func_name}_story_love_list", {
            0: "This character's love progress has not yet been created."
        })

    @property
    def story_love_is_complete(self) -> bool:
        return (
            not self.has_love_story
            or self.__call_global_func(f"{self.person.func_name}_story_love_is_complete", False)
        )

    @cached_property
    def has_lust_story(self) -> bool:
        return self.__has_global_func(f"{self.person.func_name}_story_lust_list")

    @property
    def story_lust_list(self) -> dict[int, str]:
        return self.__call_global_func(f"{self.person.func_name}_story_lust_list", {
            0: "This character's lust progress has not yet been created."
        })

    @property
    def story_lust_is_complete(self) -> bool:
        return (
            not self.has_lust_story
            or self.__call_global_func(f"{self.person.func_name}_story_lust_is_complete", False)
        )

    @cached_property
    def has_obedience_story(self) -> bool:
        return self.__has_global_func(f"{self.person.func_name}_story_obedience_list")

    @property
    def story_obedience_list(self) -> dict[int, str]:
        return self.__call_global_func(f"{self.person.func_name}_story_obedience_list", {
            0: "This character's obedience progress has not yet been created."
        })

    @property
    def story_obedience_is_complete(self) -> bool:
        return (
            not self.has_obedience_story
            or self.__call_global_func(f"{self.person.func_name}_story_obedience_is_complete", False)
        )

    @property
    def story_other_list(self) -> dict[int, str]:
        return self.__call_global_func(f"{self.person.func_name}_story_other_list", {})

    @cached_property
    def has_teamup(self) -> bool:
        return self.__has_global_func(f"{self.person.func_name}_story_teamup_list")

    @property
    def story_teamup_list(self) -> dict[int, tuple[Person | None, str]]:
        return self.__call_global_func(f"{self.person.func_name}_story_teamup_list", {
            0: [None, "No teamups have been written for this character yet!"]
        })

    def __has_global_func(self, func_name: str) -> bool:
        return has_global_func(func_name)

    def __call_global_func(self, func_name: str, default_message: dict[int, str]) -> dict[int, str]:
        result = call_global_func(func_name)
        if result:
            return result
        return default_message
