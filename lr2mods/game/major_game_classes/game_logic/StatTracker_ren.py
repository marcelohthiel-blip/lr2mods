from __future__ import annotations

from game.major_game_classes.character_related.Person_ren import list_of_people, girlfriend_role

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -20 python:
"""
class StatTracker():
    sex_stats = ["Handjobs", "Kissing", "Fingered",
        "Insertions", "Spankings",
        "Cunnilingus", "Tit Fucks", "Blowjobs",
        "Vaginal Sex", "Anal Sex"]

    cum_stats = ["Cum Facials", "Cum in Mouth", "Cum Covered",
        "Vaginal Creampies", "Anal Creampies", "Filled Condom"]

    info_stats = ["Threesomes", "Orgasms", "Public Sex", "Children with MC"]

    def __init__(self) -> None:
        self._tracked_stats: dict[str, dict[str, int]] = {}

    def change_tracked_stat(self, category: str, stat: str, value: int) -> None:
        if category not in self._tracked_stats:
            self._tracked_stats[category] = {}
        self._tracked_stats[category][stat] = self._tracked_stats[category].get(stat, 0) + value

    def tracked_stats(self, category: str) -> dict[str, int]:
        return self._tracked_stats.get(category, {})

    @property
    def income(self) -> dict[str, int]:
        return {k: v for k, v in self.tracked_stats("Money").items() if v > 0}

    @property
    def expenses(self) -> dict[str, int]:
        return {k: abs(v) for k, v in self.tracked_stats("Money").items() if v < 0}

    def sex_stat(self, name) -> int:
        return sum(x.sex_record.get(name, 0) for x in list_of_people)

    def cum_stat(self, name) -> int:
        return sum(x.sex_record.get(name, 0) for x in list_of_people)

    def info_stat(self, name) -> int:
        return sum(x.sex_record.get(name, 0) for x in list_of_people)

    @property
    def harem(self) -> int:
        return sum(1 for x in list_of_people if x.in_harem)

    @property
    def girlfriends(self) -> int:
        return sum(1 for x in list_of_people if x.has_role(girlfriend_role))

    @property
    def paramours(self) -> int:
        return sum(1 for x in list_of_people if x.is_affair)

    @property
    def slaves(self) -> int:
        return sum(1 for x in list_of_people if x.is_slave)

    @property
    def cum_fetish(self) -> int:
        return sum(1 for x in list_of_people if x.has_cum_fetish)

    @property
    def anal_fetish(self) -> int:
        return sum(1 for x in list_of_people if x.has_anal_fetish)

    @property
    def breeding_fetish(self) -> int:
        return sum(1 for x in list_of_people if x.has_breeding_fetish)

    @property
    def pregnancies(self) -> int:
        return sum(1 for x in list_of_people if x.is_pregnant)

    @property
    def in_trance(self) -> int:
        return sum(1 for x in list_of_people if x.is_in_trance)

    @property
    def active_serums(self) -> int:
        return sum(x.active_serum_count for x in list_of_people)

    @property
    def opinions_discovered(self) -> int:
        return self._tracked_stats["Girl"].get("Opinion Discovered", 0)

    @property
    def sexy_opinions_discovered(self) -> int:
        return self._tracked_stats["Girl"].get("Sexy Opinion Discovered", 0)
