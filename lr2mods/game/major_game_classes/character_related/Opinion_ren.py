from __future__ import annotations
from typing import Iterable
from game.major_game_classes.character_related.Person_ren import Person

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""

class Opinion():
    def __init__(self, person: Person, known = False):
        self.person = person
        if known:
            self.get_func = self.person.get_known_opinion_score
        else:
            self.get_func = self.person.get_opinion_score

    def __hash__(self) -> int:
        return hash(self.person)

    def __eq__(self, other: Opinion) -> bool:
        if not isinstance(other, Opinion):
            return NotImplemented
        return self.person == other.person

    def __call__(self, topic: str | Iterable[str]) -> int:
        '''
        Default callable object for undefined topics
        When topic is iterable[str] sums the passed opinions scores and returns that value
        '''
        if isinstance(topic, str):
            return self.get_func(topic)

        value = 0
        for x in (x for x in topic if isinstance(x, str)):
            value += self.get_func(x)
        return value

    @property
    def doggy_style(self) -> int:
        return self.get_func("doggy style sex") #Has gameplay effect

    @property
    def missionary_style(self) -> int:
        return self.get_func("missionary style sex") #Has gameplay effect

    @property
    def sex_standing_up(self) -> int:
        return self.get_func("sex standing up") #Has gameplay effect

    @property
    def giving_blowjobs(self) -> int:
        return self.get_func("giving blowjobs") #Has gameplay effect

    @property
    def getting_head(self) -> int:
        return self.get_func("getting head") #Has gameplay effect

    @property
    def anal_sex(self) -> int:
        return self.get_func("anal sex") #Has gameplay effect

    @property
    def vaginal_sex(self) -> int:
        return self.get_func("vaginal sex") #Has gameplay effect

    @property
    def public_sex(self) -> int:
        return self.get_func("public sex") #Has gameplay effect

    @property
    def kissing(self) -> int:
        return self.get_func("kissing") #Has gameplay effect

    @property
    def lingerie(self) -> int:
        return self.get_func("lingerie") #Has gameplay effect

    @property
    def masturbating(self) -> int:
        return self.get_func("masturbating") #Has gameplay effect

    @property
    def giving_handjobs(self) -> int:
        return self.get_func("giving handjobs") #Has gameplay effect

    @property
    def giving_tit_fucks(self) -> int:
        return self.get_func("giving tit fucks") #Has gameplay effect

    @property
    def being_fingered(self) -> int:
        return self.get_func("being fingered") #Has gameplay effect

    @property
    def skimpy_uniforms(self) -> int:
        return self.get_func("skimpy uniforms") #Has gameplay effect

    @property
    def work_uniforms(self) -> int:
        return self.get_func("work uniforms")

    @property
    def skimpy_outfits(self) -> int:
        return self.get_func("skimpy outfits") #Has gameplay effect

    @property
    def not_wearing_underwear(self) -> int:
        return self.get_func("not wearing underwear") #Has gameplay effect

    @property
    def not_wearing_anything(self) -> int:
        return self.get_func("not wearing anything") #Has gameplay effect

    @property
    def showing_her_tits(self) -> int:
        return self.get_func("showing her tits") #Has gameplay effect

    @property
    def showing_her_ass(self) -> int:
        return self.get_func("showing her ass") #Has gameplay effect

    @property
    def being_submissive(self) -> int:
        return self.get_func("being submissive") #Has gameplay effect

    @property
    def taking_control(self) -> int:
        return self.get_func("taking control") #Has gameplay effect

    @property
    def drinking_cum(self) -> int:
        return self.get_func("drinking cum") #Has gameplay effect

    @property
    def creampies(self) -> int:
        return self.get_func("creampies") #Has gameplay effect

    @property
    def cum_facials(self) -> int:
        return self.get_func("cum facials") #Has gameplay effect

    @property
    def being_covered_in_cum(self) -> int:
        return self.get_func("being covered in cum") #Has gameplay effect

    @property
    def bareback_sex(self) -> int:
        return self.get_func("bareback sex") #Has gameplay effect.

    @property
    def big_dicks(self) -> int:
        return self.get_func("big dicks")

    @property
    def cheating_on_men(self) -> int:
        return self.get_func("cheating on men") #Has gameplay effect

    @property
    def anal_creampies(self) -> int:
        return self.get_func("anal creampies") #Has gameplay effect

    @property
    def incest(self) -> int:
        return self.get_func("incest") #Has gameplay effect

    @property
    def threesomes(self) -> int:
        return self.get_func("threesomes")

    @property
    def polyamory(self) -> int:
        return self.get_func("polyamory")

    @property
    def small_talk(self) -> int:
        return self.get_func("small talk")

    @property
    def dresses(self) -> int:
        return self.get_func("dresses")

    @property
    def skirts(self) -> int:
        return self.get_func("skirts")

    @property
    def pants(self) -> int:
        return self.get_func("pants")

    @property
    def high_heels(self) -> int:
        return self.get_func("high heels")

    @property
    def boots(self) -> int:
        return self.get_func("boots")

    @property
    def makeup(self) -> int:
        return self.get_func("makeup")

    @property
    def sports(self) -> int:
        return self.get_func("sports")

    @property
    def conservative_outfits(self) -> int:
        return self.get_func("conservative outfits")

    @property
    def flirting(self) -> int:
        return self.get_func("flirting")

    @property
    def hiking(self) -> int:
        return self.get_func("hiking")

    @property
    def yoga(self) -> int:
        return self.get_func("yoga")

    @property
    def working(self) -> int:
        return self.get_func("working")

    @property
    def hr_work(self) -> int:
        return self.get_func("HR work")

    @property
    def supply_work(self) -> int:
        return self.get_func("supply work")

    @property
    def marketing_work(self) -> int:
        return self.get_func("marketing work")

    @property
    def research_work(self) -> int:
        return self.get_func("research work")

    @property
    def production_work(self) -> int:
        return self.get_func("production work")
