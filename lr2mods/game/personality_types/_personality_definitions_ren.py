from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, Personality, mc

list_of_personalities: list[Personality] = []
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
#########################
# Generic Personalities #
#########################
def relaxed_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Candy")
    if person.sluttiness > 60:
        valid_titles.append("Hot Stuff")

    return valid_titles

def relaxed_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your eyecandy")
    return valid_titles

def relaxed_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 10:
        valid_titles.append(mc.name)
    if person.has_breeding_fetish:
        valid_titles.append("Bull")
    return valid_titles

relaxed_activity_opinions = {}
relaxed_activity_opinions["pong"]= 2
relaxed_activity_opinions["salsa"]= -2
relaxed_activity_opinions["arcade"]= 0
relaxed_activity_opinions["billiards"]= 1
relaxed_activity_opinions["darts"]= 1
relaxed_activity_opinions["karaoke"]= 0
relaxed_activity_opinions["trivia"]= -1

def introvert_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Baby Girl")
    if person.sluttiness > 60:
        valid_titles.append("Lollipop")
    return valid_titles

def introvert_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your baby girl")
    return valid_titles

def introvert_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.has_breeding_fetish:
        valid_titles.append("Daddy")
    return valid_titles

introvert_activity_opinions = {}
introvert_activity_opinions["pong"] = -1
introvert_activity_opinions["salsa"] = -1
introvert_activity_opinions["arcade"] = 2
introvert_activity_opinions["billiards"] = 1
introvert_activity_opinions["darts"] = 1
introvert_activity_opinions["karaoke"] = -2
introvert_activity_opinions["trivia"] = 0


def reserved_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Cherry")
    if person.sluttiness > 60:
        valid_titles.append("Minx")
    return valid_titles

def reserved_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your cherrylips")
    if person.sluttiness > 60:
        valid_titles.append("your little minx")
    return valid_titles

def reserved_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    if person.love > 30:
        valid_titles.append(mc.name)
    if person.has_breeding_fetish:
        valid_titles.append("Bull")
    return valid_titles

reserved_activity_opinions = {}
reserved_activity_opinions["pong"]= 0
reserved_activity_opinions["salsa"]= 1
reserved_activity_opinions["arcade"]= 1
reserved_activity_opinions["billiards"]= 2
reserved_activity_opinions["darts"]= 1
reserved_activity_opinions["karaoke"]= -2
reserved_activity_opinions["trivia"]= -1


def wild_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("Sugar Lips")
    if person.sluttiness > 60:
        valid_titles.append("Bitch")

    return valid_titles

def wild_possessive_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    valid_titles.append(person.name)
    if person.sluttiness > 40:
        valid_titles.append("your sugarlips")
    if person.sluttiness > 60:
        valid_titles.append("your little bitch")
    return valid_titles

def wild_player_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"Mr. {mc.last_name}")
    valid_titles.append(mc.name)
    if person.has_breeding_fetish:
        valid_titles.append("Stud")
    return valid_titles


wild_activity_opinions = {}
wild_activity_opinions["pong"]= 1
wild_activity_opinions["salsa"]= 2
wild_activity_opinions["arcade"]= -1
wild_activity_opinions["billiards"]= 0
wild_activity_opinions["darts"]= -1
wild_activity_opinions["karaoke"]= 1
wild_activity_opinions["trivia"]= -2


def init_base_personalities():
    global relaxed_personality
    relaxed_personality = Personality("relaxed", #Lily style personality
        common_likes = ["skirts", "the weekend", "small talk", "the colour pink", "flirting", "punk music", "pop music", "high heels"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "pants", "the colour yellow", "research work", "work uniforms", "boots", "dresses"],
        common_sexy_dislikes = ["taking control", "doggy style sex", "showing her tits", "showing her ass", "bareback sex", "creampies"],
        titles_function = relaxed_titles, possessive_titles_function = relaxed_possessive_titles, player_titles_function = relaxed_player_titles,
        insta_chance = 50, dikdok_chance = 10)
    global introvert_personality
    introvert_personality = Personality("introvert", 
        common_likes = ["conservative outfits", "punk music", "working", "the colour black", "pants", "boots"],
        common_sexy_likes = ["big dicks", "kissing", "anal sex", "getting head", "giving blowjobs", "masturbating", "anal creampies", "giving tit fucks"],
        common_dislikes = ["skirts", "HR work", "marketing work", "makeup", "flirting", "small talk", "pop music", "high heels"],
        common_sexy_dislikes = ["skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "lingerie"],
        titles_function = introvert_titles, possessive_titles_function = introvert_possessive_titles, player_titles_function = introvert_player_titles,
        insta_chance = 20, dikdok_chance = 0)
    global reserved_personality
    reserved_personality = Personality("reserved",
        common_likes = ["pants", "Mondays", "working", "makeup", "the colour blue", "conservative outfits", "jazz", "classical music", "dresses", "boots"],
        common_sexy_likes = ["missionary style sex", "kissing", "lingerie", "being submissive", "vaginal sex", "creampies", "giving tit fucks"],
        common_dislikes = ["the colour red", "flirting", "skirts"],
        common_sexy_dislikes = ["masturbating", "giving blowjobs", "getting head", "doggy style sex", "public sex", "not wearing underwear", "not wearing anything", "bareback sex", "cum facials"],
        titles_function = reserved_titles, possessive_titles_function = reserved_possessive_titles, player_titles_function = reserved_player_titles,
        insta_chance = 0, dikdok_chance = 0)
    global wild_personality
    wild_personality = Personality("wild", #Stephanie style personality
        common_likes = ["skirts", "small talk", "Fridays", "the weekend", "the colour red", "makeup", "flirting", "heavy metal music", "punk music", "high heels", "dresses"],
        common_sexy_likes = ["anal creampies", "doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "bareback sex", "threesomes"],
        common_dislikes = ["Mondays", "the colour pink", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "giving handjobs"],
        titles_function = wild_titles, possessive_titles_function = wild_possessive_titles, player_titles_function = wild_player_titles,
        insta_chance = 40, dikdok_chance = 30)

    list_of_personalities.extend((
        relaxed_personality,
        introvert_personality,
        reserved_personality,
        wild_personality,
    ))

#########################
# Special Personalities #
#########################

def bimbo_titles(person: Person) -> list[str]:
    return [person.name]

def bimbo_possessive_titles(person: Person) -> list[str]:
    return bimbo_titles(person)

def bimbo_player_titles(person: Person) -> list[str]:
    valid_titles = [mc.name]
    valid_titles.append("Cutie")
    return valid_titles

bimbo_activity_opinions = {}
bimbo_activity_opinions["pong"]= 0
bimbo_activity_opinions["salsa"]= 1
bimbo_activity_opinions["arcade"]= 0
bimbo_activity_opinions["billiards"]= -1
bimbo_activity_opinions["darts"]= 0
bimbo_activity_opinions["karaoke"]= 2
bimbo_activity_opinions["trivia"]= -2


def alpha_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.sluttiness > 90 and person.opinion.anal_sex > 0 and person.anal_sex_skill > 4:
        valid_titles.append("Anal Queen")
    return valid_titles

def alpha_possessive_titles(person: Person) -> list[str]:
    valid_possessive_titles = []
    valid_possessive_titles.append(f"{person.formal_address} {person.last_name}")
    if person.sluttiness > 80 and person.opinion.threesomes > 0:
        valid_possessive_titles.append("your bi-sexual queen")
    if person.sluttiness > 90 and person.opinion.anal_sex > 0 and person.anal_sex_skill > 4:
        valid_possessive_titles.append("your anal queen")
    return valid_possessive_titles

def alpha_player_titles(person: Person) -> list[str]:
    valid_player_titles = []
    valid_player_titles.append(f"Mr. {mc.last_name}")
    if person.happiness < 70:
        valid_player_titles.append("Small balls")
    if person.love > 40:
        valid_player_titles.append("Queen's King")
    if person.sluttiness > 60:
        valid_player_titles.append("Queen's Dick")
    return valid_player_titles


alpha_activity_opinions = {}
alpha_activity_opinions["pong"]= 0
alpha_activity_opinions["salsa"]= -2
alpha_activity_opinions["arcade"]= 1
alpha_activity_opinions["billiards"]= 1
alpha_activity_opinions["darts"]= 0
alpha_activity_opinions["karaoke"]= -1
alpha_activity_opinions["trivia"]= 2


def cougar_titles(person: Person) -> list[str]:
    valid_titles = []
    valid_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_titles.append(person.name)
    if person.love > 40:
        valid_titles.append("Cougar")
    if person.sluttiness > 70:
        valid_titles.append("Old Bitch")
    if person.sluttiness > 90 and person.opinion.anal_sex > 0 and person.anal_sex_skill > 4:
        valid_titles.append("Anal Harlot")
    return valid_titles

def cougar_possessive_titles(person: Person) -> list[str]:
    valid_possessive_titles = []
    valid_possessive_titles.append(f"{person.formal_address} {person.last_name}")
    if person.love > 20:
        valid_possessive_titles.append(person.name)
    if person.sluttiness > 60:
        valid_possessive_titles.append("your slutty cougar")
    if person.sluttiness > 90 and (person.opinion.drinking_cum > 0 or person.opinion.being_covered_in_cum > 0):
        valid_possessive_titles.append("your cum-dump cougar")
    if person.sluttiness > 90 and person.opinion.anal_sex > 0 and person.anal_sex_skill > 4:
        valid_possessive_titles.append("your anal minx")
    return valid_possessive_titles

def cougar_player_titles(person: Person) -> list[str]:
    valid_player_titles = []
    valid_player_titles.append(f"Mr. {mc.last_name}")
    if person.happiness < 70:
        valid_player_titles.append("Little Boy")
    if person.love > 25:
        valid_player_titles.append("Darling")
    if person.sluttiness > 60:
        valid_player_titles.append("Young Stud")
    return valid_player_titles

cougar_activity_opinions = {}
cougar_activity_opinions["pong"]= 1
cougar_activity_opinions["salsa"]= 2
cougar_activity_opinions["arcade"]= -2
cougar_activity_opinions["billiards"]= 0
cougar_activity_opinions["darts"]= -1
cougar_activity_opinions["karaoke"]= 1
cougar_activity_opinions["trivia"]= 1

def cougar_bar_opinions():
    bar_opinions = []
    bar_opinions.append(
        ["pong", 1],
        ["salsa", 2],
        ["arcade", -2],
        ["billiards", 0],
        ["darts", -1],
        ["karaoke", 1],
        ["trivia", 1]
    )
    return bar_opinions

def init_special_personalities():
    global bimbo_personality
    bimbo_personality = Personality("bimbo", #Currently used in the head researcher event line.
        common_likes = ["skirts", "small talk", "the colour pink", "makeup", "pop music"],
        common_sexy_likes = ["giving blowjobs", "missionary style sex", "being submissive", "skimpy outfits", "showing her tits", "showing her ass", "not wearing anything", "not wearing underwear", "lingerie", "cum facials"],
        common_dislikes = ["working", "research work", "work uniforms", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = bimbo_titles, possessive_titles_function = bimbo_possessive_titles, player_titles_function = bimbo_player_titles,
        insta_chance = 75, dikdok_chance = 25)
    global alpha_personality
    alpha_personality = Personality("alpha", default_prefix = reserved_personality.default_prefix,
        common_likes = ["flirting", "work uniforms", "working", "sports", "small talk", "boots", "dresses", "high heels", "skirts", "the colour black", "the colour red"],
        common_sexy_likes = ["taking control", "threesomes", "getting head", "lingerie", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"],
        common_dislikes = ["conservative outfits", "pants", "punk music", "the colour green", "the colour pink", "classical music", "jazz"],
        common_sexy_dislikes = ["being submissive", "bareback sex", "being fingered", "missionary style sex"],
        titles_function = alpha_titles, possessive_titles_function = alpha_possessive_titles, player_titles_function = alpha_player_titles)
    global cougar_personality
    cougar_personality = Personality("cougar", default_prefix = reserved_personality.default_prefix, #Cougar style personality
        common_likes = ["skirts", "small talk", "Mondays", "the weekend", "the colour red", "makeup", "sports", "flirting", "high heels", "dresses"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "anal creampies", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour pink", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "bareback sex"],
        titles_function = cougar_titles, possessive_titles_function = cougar_possessive_titles, player_titles_function = cougar_player_titles)
    return
