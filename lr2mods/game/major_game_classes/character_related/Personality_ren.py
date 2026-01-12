from __future__ import annotations
import renpy
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.helper_functions.play_sounds_ren import play_female_orgasm
from game.helper_functions.list_functions_ren import get_random_from_list
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.personality_types._personality_definitions_ren import relaxed_activity_opinions

list_of_personalities: list[Personality]
activity_response_list: list[str]
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
#How the character responds to various actions
# global relaxed_activity_opinions

class Personality():
    RESPONSE_LABEL_ENDING = ["greetings",
        "sex_responses_foreplay", "sex_responses_oral", "sex_responses_vaginal", "sex_responses_anal",
        "climax_responses_foreplay", "climax_responses_oral", "climax_responses_vaginal", "climax_responses_anal",
        "clothing_accept", "clothing_reject", "clothing_review",
        "strip_reject", "strip_obedience_accept", "grope_body_reject", "sex_accept", "sex_obedience_accept", "sex_gentle_reject", "sex_angry_reject",
        "seduction_response", "seduction_accept_crowded", "seduction_accept_alone", "seduction_refuse",
        "compliment_response", "compliment_response_girlfriend", "compliment_response_affair",
        "flirt_response_employee_uniform_low", "flirt_response_employee_uniform_mid",
        "flirt_response_low", "flirt_response_mid", "flirt_response_high",
        "flirt_response_girlfriend", "flirt_response_affair", "flirt_response_text",
        "condom_demand", "condom_ask", "condom_bareback_ask", "condom_bareback_demand",
        "cum_face", "cum_mouth", "cum_pullout", "cum_condom", "cum_vagina", "cum_anal", "surprised_exclaim", "talk_busy",
        "improved_serum_unlock", "sex_strip", "sex_watch", "being_watched", "work_enter_greeting", "date_seduction", "sex_end_early", "sex_take_control", "sex_beg_finish", "sex_review", "introduction",
        "kissing_taboo_break", "touching_body_taboo_break", "touching_penis_taboo_break", "touching_vagina_taboo_break", "sucking_cock_taboo_break", "licking_pussy_taboo_break", "vaginal_sex_taboo_break", "anal_sex_taboo_break",
        "condomless_sex_taboo_break", "underwear_nudity_taboo_break", "bare_tits_taboo_break", "bare_pussy_taboo_break",
        "facial_cum_taboo_break", "mouth_cum_taboo_break", "body_cum_taboo_break", "creampie_taboo_break", "anal_creampie_taboo_break",
        # added by mod team
        # "hookup_accept", "hookup_rejection", TODO: wire this up and add default implementation in relaxed personality
        "sex_toy_taboo_break", "roleplay_taboo_break", "sleepover_yourplace_response", "sleepover_herplace_response", "sleepover_yourplace_sex_start",
        "sleepover_herplace_sex_start", "sleepover_impressed_response", "sleepover_good_response", "sleepover_bored_response",
        "lingerie_shopping_tame_response", "lingerie_shopping_excited_response", "lingerie_shopping_wow_response", "GIC_finish_response",
        "flirt_response_low_energy"] #, "bar_arcade_response", "bar_billiards_response", "bar_salsa_response", "bar_darts_response",
        #"bar_karaoke_response", "bar_trivia_response", "bar_pong_response"]

    def __init__(self, personality_type_prefix: str, default_prefix = None,
            common_likes: list[str] | None = None, common_dislikes: list[str] | None = None, common_sexy_likes: list[str] | None = None, common_sexy_dislikes: list[str] | None = None,
            titles_function = None, possessive_titles_function = None, player_titles_function = None,
            insta_chance = 0, dikdok_chance = 0, activity_opinions = None):
        '''
        The personality type prefix is used to determine the response label.
        The default prefix is the fallback for response labels (usually one of the base personalities).
        '''
        self.personality_type_prefix = personality_type_prefix
        if default_prefix is None:
            self.default_prefix = personality_type_prefix
        else:
            self.default_prefix = default_prefix

        self.titles_function = titles_function
        self.possessive_titles_function = possessive_titles_function
        self.player_titles_function = player_titles_function

        self.insta_chance = insta_chance
        self.dikdok_chance = dikdok_chance
        #NOTE: Girls never generate with Onlyfans naturally
        self.last_target = None
        self.rebuild_response_dictionary()

        #Establish our four classes of favoured likes and dislikes. Intensity (ie. love vs like, dislike vs hate) is decided on a person to person basis.
        if common_likes:
            self.common_likes = common_likes
        else:
            self.common_likes = []

        if common_sexy_likes:
            self.common_sexy_likes = common_sexy_likes
        else:
            self.common_sexy_likes = []

        if common_dislikes:
            self.common_dislikes = common_dislikes
        else:
            self.common_dislikes = []

        if common_sexy_dislikes:
            self.common_sexy_dislikes = common_sexy_dislikes
        else:
            self.common_sexy_dislikes = []

        self.build_activity_opinions()
        self.identifier = generate_identifier(self.personality_type_prefix)

    def __hash__(self):
        return self.identifier

    def __eq__(self, other: Personality) -> bool:
        if not isinstance(other, Personality):
            return NotImplemented
        return self.identifier == other.identifier

    @property
    def base_personality_prefix(self):
        if self.default_prefix:
            return self.default_prefix
        return self.personality_type_prefix

    def _select_target_label(self, label_ending: str) -> str:
        target = self.response_dict[label_ending]
        if isinstance(target, (list, tuple, set)): # multiple possible responses
            # exclude last target to prevent repetition
            target = renpy.random.choice([x for x in target if x != self.last_target])
        return target

    def get_dialogue(self, person: Person, label_ending: str, *args, **kwargs):
        '''
        Calls dialog for person based on label ending and passes arguments to call
        label_ending: one of the ending defined in Personality.RESPONSE_LABEL_ENDING
        '''
        if label_ending not in self.response_dict:
            # self repairing personality response type (helps with upgrades / changes to personality files)
            self.rebuild_response_dictionary()

        target = self._select_target_label(label_ending)

        if not renpy.has_label(target): # self repairing personality response dictionary (helps with upgrades / changes to personality files)
            self.rebuild_response_dictionary()
            target = self._select_target_label(label_ending)

        if target and renpy.has_label(target):
            if "climax_responses" in label_ending:
                play_female_orgasm()
            self.last_target = target
            renpy.call(target, person, *args, **kwargs)

    def generate_default_opinion(self) -> tuple[str, list]:
        if renpy.random.randint(1, 2) == 1:
            #Positive
            degree = renpy.random.randint(1, 2)
            the_key = get_random_from_list(self.common_likes)
            return (the_key, [degree, False])

        #Negative
        degree = renpy.random.randint(-2, -1)
        the_key = get_random_from_list(self.common_dislikes)
        return (the_key, [degree, False])

    def generate_default_sexy_opinion(self) -> tuple[str, list]:
        if renpy.random.randint(1, 2) == 1:
            #Positive
            degree = renpy.random.randint(1, 2)
            the_key = get_random_from_list(self.common_sexy_likes)
            return (the_key, [degree, False])

        #Negative
        degree = renpy.random.randint(-2, -1)
        the_key = get_random_from_list(self.common_sexy_dislikes)
        return (the_key, [degree, False])

    def get_personality_titles(self, person: Person) -> list[str]: #This should be a function defined for each
        if callable(self.titles_function):
            return self.titles_function(person)
        return [person.name]

    def get_personality_possessive_titles(self, person: Person) -> list[str]:
        if callable(self.possessive_titles_function):
            return self.possessive_titles_function(person)
        return [person.name]

    def get_personality_player_titles(self, person: Person) -> list[str]:
        if callable(self.player_titles_function):
            return self.player_titles_function(person)
        return [mc.name]

    def rebuild_response_dictionary(self):
        self.response_dict = {}
        for ending in Personality.RESPONSE_LABEL_ENDING:
            targets = []

            for prefix in (self.personality_type_prefix, self.default_prefix, "relaxed"):
                if targets:
                    break
                for i in range(9):
                    variation = "" if i == 0 else f"{i}"
                    target = f"{prefix}_{ending}{variation}"
                    if renpy.has_label(target):
                        targets.append(target)

                    if i > len(targets):
                        break   # quick exit if no more multiple responses

            if not targets and ending in self.response_dict:
                del self.response_dict[ending]
            elif len(targets) == 1:
                self.response_dict[ending] = targets[0]
            else:
                self.response_dict[ending] = targets
        for game in activity_response_list:
            targets = []
            target_text = "activity_" + game + "_response"
            for prefix in (self.personality_type_prefix, self.default_prefix, "relaxed"):
                if targets:
                    break
                for i in range(9):
                    variation = "" if i == 0 else f"{i}"
                    target = f"{prefix}_{target_text}{variation}"
                    if renpy.has_label(target):
                        targets.append(target)

                    if i > len(targets):
                        break   # quick exit if no more multiple responses

            if not targets and target_text in self.response_dict:
                del self.response_dict[target_text]
            elif len(targets) == 1:
                self.response_dict[target_text] = targets[0]
            else:
                self.response_dict[target_text] = targets

    def build_activity_opinions(self):
        # Use similarly to build response dict.
        # Checks in a descending order of priority, ending with relaxed if no other opinion is found.
        self.activity_opinions = {}
        for prefix in (self.personality_type_prefix, self.default_prefix, "relaxed"):
            activity_string_name = prefix + "_activity_opinions"
            if activity_string_name in globals():
                for activity_opinion in globals()[activity_string_name]:
                    if activity_opinion not in self.activity_opinions:
                        self.activity_opinions[activity_opinion] = globals()[activity_string_name][activity_opinion]        #Fuck me I think I got this right but who the hell knows
        return