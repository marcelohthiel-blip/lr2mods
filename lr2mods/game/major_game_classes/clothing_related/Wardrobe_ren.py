from __future__ import annotations
from collections.abc import Iterator
from typing import Callable, Literal
import xml.etree.ElementTree as ET
import builtins
import copy
import renpy
from renpy import str
from game.bugfix_additions.debug_info_ren import write_log
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.helper_functions.list_functions_ren import get_random_from_list
from game.clothing_lists_ren import sports_bra, lab_coat, apron, bralette, lace_bra, strappy_bra, boy_shorts, lace_panties, thong, string_panties, panties_list, bra_list, pants_list, skirts_list, dress_list, shirts_list, socks_list, tights_list, shoes_list, earings_list, bracelet_list, rings_list, neckwear_list
from game.business_policies.clothing_policies_ren import male_focused_marketing_policy, dress_code_policy, creative_colored_uniform_policy, personal_bottoms_uniform_policy, commando_uniform_policy, easier_access_policy, creative_skimpy_uniform_policy, corporate_enforced_nudity_policy
from game.major_game_classes.character_related._job_definitions_ren import doctor_job, waitress_job
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.Outfit_ren import Outfit, Person, mc
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder
from game.major_game_classes.clothing_related.wardrobe_preferences_ren import WardrobePreference

default_wardrobe: Wardrobe
lingerie_wardrobe: Wardrobe
insta_wardrobe: Wardrobe
mom_business_wardrobe: Wardrobe
barista_uniforms: Wardrobe
nurse_uniforms: Wardrobe
maid_uniforms: Wardrobe

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
from itertools import chain

#TODO: Redesign implicit validations -> allow wardrobe to have custom validation functions
#      for outfit and uniform, with default functions for standard wardrobes, but exceptions
#      for limited wardrobes / personal wardrobes etc.

class Wardrobe(): #A bunch of outfits!
    @staticmethod
    def build_assembled_outfit(outfit_under: Outfit, outfit_over: Outfit) -> Outfit:
        # print("Assemble outfit: {}".format(outfit_over.name))
        assembled_outfit = outfit_over.get_copy()

        # print("Overwear has {} items".format(outfit_over.item_count))
        # print("Underwear has {} items".format(outfit_under.item_count))

        for upper in (x for x in outfit_under.upper_body if not x.is_extension):
            assembled_outfit.add_upper(upper.get_copy())

        for lower in (x for x in outfit_under.lower_body if not x.is_extension):
            assembled_outfit.add_lower(lower.get_copy())

        for feet_wear in (x for x in outfit_under.feet if not x.is_extension):
            assembled_outfit.add_feet(feet_wear.get_copy())

        for acc in (x for x in outfit_under.accessories if not x.is_extension):
            assembled_outfit.add_accessory(acc.get_copy())

        # prevent tights in combination with socks or hose
        if assembled_outfit.has_tights and assembled_outfit.has_socks:
            if assembled_outfit.has_dress and assembled_outfit.has_socks:
                assembled_outfit.remove_socks_or_stockings() # when dress prefer tights
            else:
                assembled_outfit.remove_tights() # prefer socks/hose

        assembled_outfit.build_outfit_name()

        # print("Assembled Outfit: {}".format(assembled_outfit.name))
        return assembled_outfit

    @staticmethod
    def generate_random_appropriate_outfit(person: Person, outfit_type: Literal['over', 'under', 'full'] = "full", sluttiness_limit: int = None, opinion_color: str = None, coloured_underwear: bool = True, swap_bottoms: bool = False, allow_skimpy: bool = False) -> Outfit:
        wardrobe_builder = WardrobeBuilder(person)
        (min_slut, max_slut) = WardrobeBuilder.get_clothing_min_max_slut_value(sluttiness_limit or person.sluttiness)
        outfit = wardrobe_builder.build_outfit(outfit_type, max_slut, min_slut)
        return wardrobe_builder.personalize_outfit(outfit, opinion_color = opinion_color, coloured_underwear = coloured_underwear, swap_bottoms = swap_bottoms, allow_skimpy = allow_skimpy)

    def __init__(self, name: str, outfits: list[Outfit] = None, underwear_sets: list[Outfit] = None, overwear_sets: list[Outfit] = None, enforce_legal_status = True): #Outfits is a list of Outfit objects, or empty if the wardrobe starts empty
        self.name = name
        self.filename = None  # original filename that loaded the wardrobe
        self.outfit_sets = outfits #Outfits is now used to hold full outfits.
        self.underwear_sets = underwear_sets #Limited to layer 1 clothing items.
        self.overwear_sets = overwear_sets #Limited to layer 2 and 3 clothing items.
        if outfits is None:
            self.outfit_sets = []
        if underwear_sets is None:
            self.underwear_sets = []
        if overwear_sets is None:
            self.overwear_sets = []

        for outfit in self:
            outfit.restore_all_clothing() #Make sure none of them are stored half off.
        self.identifier = generate_identifier(self.name)
        self._enforce_legal_status = enforce_legal_status

    def __copy__(self) -> Wardrobe:
        outfit_copy_list = []
        for outfit in self.outfit_sets:
            outfit_copy_list.append(outfit.get_copy())

        under_copy_list = []
        for underwear in self.underwear_sets:
            under_copy_list.append(underwear.get_copy())

        over_copy_list = []
        for overwear in self.overwear_sets:
            over_copy_list.append(overwear.get_copy())

        return Wardrobe(self.name, outfit_copy_list, under_copy_list, over_copy_list)

    def __iter__(self) -> Iterator[Outfit]:
        return chain(self.outfit_sets, self.underwear_sets, self.overwear_sets)

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Wardrobe) -> bool:
        if not isinstance(other, Wardrobe):
            return NotImplemented
        return self.name == other.name

    @property
    def enforce_legal_status(self) -> bool:
        if not hasattr(self, '_enforce_legal_status'):
            self._enforce_legal_status = True
        return self._enforce_legal_status

    @property
    def has_outfits(self) -> bool:
        return self.outfit_sets or self.overwear_sets or self.underwear_sets

    @property
    def total_count(self) -> int:
        '''
        Total number of items in wardrobe
        Cumulation of outfit count, underwear count and overwear count
        '''
        return self.outfit_count + self.overwear_count + self.underwear_count

    @property
    def outfit_count(self) -> int:
        '''
        Total number of full outfits in wardrobe
        '''
        return len(self.outfit_sets)

    @property
    def overwear_count(self) -> int:
        '''
        Total number of overwear sets in wardrobe
        '''
        return len(self.overwear_sets)

    @property
    def underwear_count(self) -> int:
        '''
        Total number of underwear sets in wardrobe
        '''
        return len(self.underwear_sets)

    def clear_wardrobe(self):
        for outfit in self:
            outfit.clear()
        self.outfit_sets.clear()
        self.underwear_sets.clear()
        self.overwear_sets.clear()

    def merge_wardrobes(self, other_wardrobe, keep_primary_name = False): #Returns a copy of this wardrobe merged with the other one, with this taking priority for base outfits.
        merged_wardrobe = copy.copy(self)
        if isinstance(other_wardrobe, Wardrobe):
            for outfit in other_wardrobe.outfit_sets:
                merged_wardrobe.add_outfit(outfit.get_copy())

            for underwear in other_wardrobe.underwear_sets:
                merged_wardrobe.add_underwear_set(underwear.get_copy())

            for overwear in other_wardrobe.overwear_sets:
                merged_wardrobe.add_overwear_set(overwear.get_copy())

            if not keep_primary_name:
                merged_wardrobe.name = f"{merged_wardrobe.name} + {other_wardrobe.name}"
        return merged_wardrobe

    def add_outfit(self, outfit: Outfit):
        if not isinstance(outfit, Outfit):
            return
        outfit.restore_all_clothing() #Ensure none of the outfits have half-off clothing.
        if found := next((x for x in self.outfit_sets if x.name == outfit.name), None):   # if we already have an outfit with that name, replace it (outfit name must be unique)
            self.outfit_sets.remove(found)
        #print(f"Add outfit {outfit.name} to {self.name}")
        self.outfit_sets.append(outfit)

    def add_underwear_set(self, outfit: Outfit):
        if not isinstance(outfit, Outfit):
            return
        outfit.restore_all_clothing()
        if found := next((x for x in self.underwear_sets if x.name == outfit.name), None):   # if we already have an outfit with that name, replace it (outfit name must be unique)
            self.underwear_sets.remove(found)
        #print(f"Add underwear {outfit.name} to {self.name}")
        self.underwear_sets.append(outfit)

    def add_overwear_set(self, outfit: Outfit):
        if not isinstance(outfit, Outfit):
            return
        outfit.restore_all_clothing()
        if found := next((x for x in self.overwear_sets if x.name == outfit.name), None):   # if we already have an outfit with that name, replace it (outfit name must be unique)
            self.overwear_sets.remove(found)
        #print(f"Add overwear {outfit.name} to {self.name}")
        self.overwear_sets.append(outfit)

    def remove_outfit(self, outfit: Outfit | str):
        for outfit_set in (self.outfit_sets, self.underwear_sets, self.overwear_sets):
            if isinstance(outfit, str):
                if found := next((x for x in outfit_set if x.name == outfit), None):
                    outfit_set.remove(found)
            elif outfit in outfit_set:
                outfit_set.remove(outfit)

    def pick_random_outfit(self) -> Outfit:
        return get_random_from_list(self.outfit_sets).get_copy() # Get a copy of _any_ full outfit in this character's wardrobe.

    def pick_random_overwear(self) -> Outfit:
        return get_random_from_list(self.overwear_sets).get_copy()

    def pick_random_underwear(self) -> Outfit:
        return get_random_from_list(self.underwear_sets).get_copy()

    def get_random_appropriate_underwear(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0) -> Outfit | None:
        if preferences is None:
            preferences = WardrobePreference()

        sluttiness_min = max(sluttiness_min, 0) # minimum value = 0
        valid_underwear = [x for x in self.underwear_sets if preferences.evaluate_underwear(x, sluttiness_limit, sluttiness_min)]

        if not valid_underwear: # when we find no valid items, only validate sluttiness score
            valid_underwear = [x for x in self.underwear_sets if x.underwear_slut_score <= sluttiness_limit and x.underwear_slut_score >= sluttiness_min]

        if valid_underwear:
            return renpy.random.choice(valid_underwear).get_copy()
        if guarantee_output: # If an output is guaranteed we always return an Outfit object (even if it is empty). Otherwise we return None to indicate failure to find something.
            if depth < 2: #Sets an effective recursion limit.
                return self.get_random_appropriate_underwear(sluttiness_limit + 5, sluttiness_min - 5, guarantee_output, preferences, depth + 1)

            return self.__pick_underwear_with_lowest_sluttiness() or Outfit("Nothing")
        return None

    def get_random_appropriate_overwear(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0) -> Outfit | None:
        if preferences is None:
            preferences = WardrobePreference()

        sluttiness_min = max(sluttiness_min, 0) # minimum value = 0
        valid_overwear = [x for x in self.overwear_sets if preferences.evaluate_outfit(x, sluttiness_limit, sluttiness_min)]
        if not valid_overwear:  # when we find no valid items, only validate sluttiness score
            valid_overwear = [x for x in self.overwear_sets if x.overwear_slut_score <= sluttiness_limit and x.overwear_slut_score >= sluttiness_min]

        if valid_overwear:
            return renpy.random.choice(valid_overwear).get_copy()
        if guarantee_output:
            if depth < 2:
                return self.get_random_appropriate_overwear(sluttiness_limit + 5, sluttiness_min - 5, guarantee_output, preferences, depth + 1)

            return self.__pick_overwear_with_lowest_sluttiness() or Outfit("Nothing")
        return None

    def get_random_appropriate_outfit(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0) -> Outfit | None:
        if preferences is None:
            preferences = WardrobePreference()

        sluttiness_min = max(sluttiness_min, 0) # minimum value = 0
        valid_outfits = [x for x in self.outfit_sets if preferences.evaluate_outfit(x, sluttiness_limit, sluttiness_min)]

        # print("Valid outfits: {}".format(len(valid_outfits)))
        if not valid_outfits: # when we find no valid items, only validate sluttiness score
            valid_outfits = [x for x in self.outfit_sets if x.outfit_slut_score <= sluttiness_limit and x.outfit_slut_score >= sluttiness_min]

        if valid_outfits:
            return renpy.random.choice(valid_outfits).get_copy()
        if guarantee_output and depth < 2:
            if depth < 2:
                return self.get_random_appropriate_outfit(sluttiness_limit + 5, sluttiness_min - 5, guarantee_output, preferences, depth + 1)

            #print("Unable to get outfit from wardrobe, pick outfit with lowest sluttiness.")
            return self.__pick_outfit_with_lowest_sluttiness() or Outfit("Nothing")
        return None

    def decide_on_outfit(self, person: Person, sluttiness_modifier = 0.0, slut_limit = 999, allow_personal_wardrobe = True, is_uniform = False) -> Outfit:
        conservative_score = person.opinion.conservative_outfits / 20.0
        skimpy_outfit_score = person.opinion.skimpy_outfits / 20.0
        marketing_score = 0
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their outfit choice
        if mc.business.is_work_day and male_focused_marketing_policy.is_active and person in mc.business.market_team:
            marketing_score = .05

        target_sluttiness = builtins.int(person.sluttiness * (1.0 + skimpy_outfit_score + marketing_score + sluttiness_modifier - conservative_score))
        target_sluttiness = builtins.min(target_sluttiness, slut_limit)

        if not self.has_outfits:
            #print("{} - No available outfits in wardrobe {}, generate random.".format(person.name, self.name))
            #We have nothing to make a outfit out of. Use default builder function.
            return Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = target_sluttiness, swap_bottoms = True, allow_skimpy = person.sluttiness > 50)

        preferences = WardrobePreference(person)
        minimum_sluttiness = builtins.int(target_sluttiness * .3)

        # print(f"{person.name} - Decide on build outfit -> Target slut {target_sluttiness}, min slut {minimum_sluttiness}")

        if self.outfit_sets:
            #We have some full body outfits we might use.
            # depends on the ratio full outfits vs overwear sets (with slight skew towards composing)
            chance_to_use_full = int((self.outfit_count / (self.outfit_count + self.overwear_count + 1)) * 100.0)

            can_compose = (self.underwear_count > 0 or self.overwear_count > 0) if allow_personal_wardrobe else (self.underwear_count > 0 and self.overwear_count > 0)

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if renpy.random.randint(1, 100) < chance_to_use_full or not can_compose:

                full_outfit = self.get_random_appropriate_outfit(target_sluttiness, minimum_sluttiness, preferences = preferences)

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    # print("{} - Unable to find full outfit in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                    full_outfit = self.__pick_outfit_with_lowest_sluttiness()

                if not full_outfit and not self == person.wardrobe: # try personal wardrobe if available
                    full_outfit = person.wardrobe.get_random_appropriate_outfit(target_sluttiness, minimum_sluttiness, preferences = preferences)

                if full_outfit:
                    # print("{} - full outfit: {}".format(self.name, full_outfit.name))
                    return self.validate_outfit(full_outfit.get_copy(), person, is_uniform)

        #If we get to here we are assembling an outfit out of underwear or overwear.
        outfit_over = self.get_random_appropriate_overwear(target_sluttiness, minimum_sluttiness, preferences = preferences)
        outfit_under = None

        if outfit_over:
            slut_limit_remaining = max(target_sluttiness - outfit_over.overwear_slut_score, 10) # minimum value is 10
            outfit_under = self.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

            if not outfit_under:
                # print("{} - Unable to find underwear in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                outfit_under = self.__pick_underwear_with_lowest_sluttiness()

            if not outfit_under and not self == person.wardrobe: # try personal wardrobe if available
                # print("{} - Unable to find underwear in wardrobe, pick underwear from person wardrobe.".format(self.name))
                outfit_under = person.wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

            if not outfit_under:
                # print("{} - Unable to find underwear in wardrobe {}, generate random underwear set.".format(person.name, self.name))
                outfit_under = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under", sluttiness_limit = slut_limit_remaining)

        else:
            #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
            outfit_under = self.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if not outfit_under:
                # print("{} - Unable to find underwear in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                outfit_under = self.__pick_underwear_with_lowest_sluttiness()

            if not outfit_under and not self == person.wardrobe: # try personal wardrobe if available
                # print("{} - Unable to find underwear in wardrobe, pick underwear from person wardrobe.".format(self.name))
                outfit_under = person.wardrobe.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if not outfit_under:
                # print("{} - Unable to find underwear in wardrobe {}, generate random underwear.".format(person.name, self.name))
                outfit_under = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under", sluttiness_limit = target_sluttiness)

            if outfit_under:
                slut_limit_remaining = max(target_sluttiness - outfit_under.underwear_slut_score, 10) # mimimum value is 10
                outfit_over = self.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

                if not outfit_over:
                    # print("{} - Unable to find overwear in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                    outfit_over = self.__pick_overwear_with_lowest_sluttiness()

                if not outfit_over and not self == person.wardrobe: # try personal wardrobe if available
                    # print("{} - Unable to find overwear in wardrobe, pick overwear from person wardrobe.".format(self.name))
                    outfit_over = person.wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

                if not outfit_over:
                    # print("{} - Unable to find overwear in wardrobe {}, generate random underwear set.".format(person.name, self.name))
                    outfit_over = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "over", sluttiness_limit = slut_limit_remaining)

        #At this point we have our under and over, if at all possible.
        if not outfit_over or not outfit_under:
            # print("{} - Unable to find anything in wardrobe {}, generate a complete outfit.".format(person.name, self.name))
            # Something's gone wrong and we don't have one of our sets. Last attempt on getting a full outfit from any wardrobe.
            return Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = target_sluttiness, swap_bottoms = True, allow_skimpy = person.sluttiness > 50)

        full_outfit = Wardrobe.build_assembled_outfit(outfit_under, outfit_over)

        # print("{} - full outfit: {}".format(self.name, full_outfit.name))
        return self.validate_outfit(full_outfit, person, is_uniform)

    def decide_on_uniform(self, person: Person) -> Outfit:
        '''
        Decide on uniform for this person based on their job and wardrobe availabe for their job
        '''
        slut_limit = 999
        valid_wardrobe = None
        if (person.is_employee or person.is_intern) and dress_code_policy.is_active:
            slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
            valid_wardrobe = self.__build_uniform_wardrobe(slut_limit, underwear_limit, limited_to_top)
        else:
            valid_wardrobe = self.__build_uniform_wardrobe()

        sluttiness_modifier = person.opinion.work_uniforms / 40.0 # low impact on sluttiness
        sluttiness_modifier += person.opinion.skimpy_uniforms / 20.0 #larger impact
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
        if mc.business.is_work_day and male_focused_marketing_policy.is_active and person in mc.business.market_team:
            sluttiness_modifier += .05

        uniform = valid_wardrobe.decide_on_outfit(person, sluttiness_modifier = sluttiness_modifier, slut_limit = slut_limit, allow_personal_wardrobe = False, is_uniform = True)

        if not uniform: # generate an outfit since we have nothing in our wardrobe that is compliant
            uniform = Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = slut_limit)

        if uniform and (person.is_employee or person.is_intern):  # only apply policies for employees
            if person.should_wear_uniform and creative_colored_uniform_policy.is_active:
                uniform = WardrobeBuilder(person).personalize_outfit(uniform,
                    swap_bottoms = personal_bottoms_uniform_policy.is_active,
                    allow_skimpy = creative_skimpy_uniform_policy.is_active)
            elif person.should_wear_uniform and personal_bottoms_uniform_policy.is_active:
                person.apply_outfit_bottom_preference(uniform)
            elif person.should_wear_dress_code and easier_access_policy.is_active: # only when creative and relaxed are not active
                uniform.make_easier_access()

            if commando_uniform_policy.is_active and uniform.wearing_panties: # always applied, overrides uniform
                uniform.remove_panties()    # going commando means no panties

        # special handling for doctors -> she wears a labcoat over her uniform
        if uniform and person.has_job(doctor_job):
            uniform.remove_overcoat()
            uniform.add_upper(lab_coat.get_copy(), [.95, .95, .95, .95])

        # special handling for waitress -> she wears an apron over her normal clothes
        if uniform and person.has_job(waitress_job):
            uniform.remove_overcoat()
            uniform.add_upper(apron.get_copy(), [.33, .29, .38, .95])

        uniform.build_outfit_name()

        # print("Picked uniform: {} ({})".format(uniform.name, uniform.outfit_slut_score))

        return uniform

    def validate_outfit(self, outfit: Outfit, person: Person, is_uniform: bool = False) -> Outfit:
        '''
        Validate if outfit conforms to legal restrictions of town
        '''
        # legal check is disabled
        if not self.enforce_legal_status:
            return outfit

        # it's a uniform and we have the appropriate policies
        if (is_uniform and
            ((person.is_at_office and corporate_enforced_nudity_policy.is_owned)
                or (person.is_at_stripclub and person.is_strip_club_employee))):
            return outfit

        # check if all parts are valid
        colour = WardrobeBuilder.get_color_from_opinion_color(person.favourite_colour)
        colour[3] = .95

        if outfit.tits_visible and not (mc.business.topless_is_legal or mc.business.nudity_is_legal):
            outfit.remove_bra() # remove current if they do not conform to legal standards
            if person.sluttiness_tier < 1:
                outfit.add_upper(sports_bra.get_copy(), colour)
            elif person.sluttiness_tier < 2:
                outfit.add_upper(bralette.get_copy(), colour)
            elif person.sluttiness_tier < 4:
                outfit.add_upper(lace_bra.get_copy(), colour)
            else:
                outfit.add_upper(strappy_bra.get_copy(), colour)

        if outfit.vagina_visible and not mc.business.nudity_is_legal:
            outfit.remove_panties() # remove current if they do not conform to legal standards
            if person.sluttiness_tier < 1:
                outfit.add_lower(boy_shorts.get_copy(), colour)
            elif person.sluttiness_tier < 2:
                outfit.add_lower(lace_panties.get_copy(), colour)
            elif person.sluttiness_tier < 4:
                outfit.add_lower(thong.get_copy(), colour)
            else:
                outfit.add_lower(string_panties.get_copy(), colour)

        return outfit

    def has_outfit_with_name(self, name: str) -> bool:
        return any(x for x in self if x.name == name)

    def get_outfit_with_name(self, name: str) -> Outfit | None:
        if found := next((x for x in self if x.name.casefold() == name.casefold()), None):
            return found.get_copy()
        return None

    def __build_uniform_wardrobe(self, slut_limit = 999, underwear_limit = 999, limited_to_top = False) -> Wardrobe:
        def _filter_outfit_sets(outfit_sets: list[Outfit], slut_limit = 999) -> list[Outfit]:
            return [x for x in outfit_sets if x.outfit_slut_score <= slut_limit]

        def _filter_underwear_sets(underwear_sets: list[Outfit], underwear_limit = 999) -> list[Outfit]:
            return [x for x in underwear_sets if x.underwear_slut_score <= underwear_limit]

        def _filter_overwear_sets(overwear_sets: list[Outfit], slut_limit = 999) -> list[Outfit]:
            return [x for x in overwear_sets if x.overwear_slut_score <= slut_limit]

        outfit_sets = []
        underwear_sets = []
        overwear_sets = []

        if self.overwear_sets:
            overwear_sets = _filter_overwear_sets(self.overwear_sets, slut_limit)

        if limited_to_top:
            return Wardrobe("Valid Uniform Wardrobe", outfit_sets, underwear_sets, overwear_sets)

        if self.outfit_sets:
            outfit_sets = _filter_outfit_sets(self.outfit_sets, slut_limit)

        if self.underwear_sets:
            underwear_sets = _filter_underwear_sets(self.underwear_sets, underwear_limit)

        return Wardrobe("Valid Uniform Wardrobe", outfit_sets, underwear_sets, overwear_sets)

    def __pick_outfit_with_lowest_sluttiness(self) -> Outfit | None:
        if not self.outfit_sets:
            return None
        return min(self.outfit_sets, key=lambda x: x.outfit_slut_score).get_copy()

    def __pick_overwear_with_lowest_sluttiness(self) -> Outfit | None:
        if not self.overwear_sets:
            return None
        return min(self.overwear_sets, key=lambda x: x.overwear_slut_score).get_copy()

    def __pick_underwear_with_lowest_sluttiness(self) -> Outfit | None:
        if not self.underwear_sets:
            return None
        return min(self.underwear_sets, key=lambda x: x.underwear_slut_score).get_copy()

    def reload(self):
        if not self.filename:
            write_log(f"Cannot reload Wardrobe without filename [Wardrobe: {self.name}]")
        self.load(self.filename)

    ### Loader ###
    def load(self, xml_filename, clean_wardrobe = True):
        '''
        Load outfits from passed XML file into Wardrobe
        clean_wardrobe: if True, will clear Wardrobe before loading
                        if False, will add outfits to Wardrobe
        '''
        file_name = Wardrobe.get_wardrobe_file(xml_filename)
        if file_name is None:
            return

        print(f"Load wardrobe {file_name}")

        self.filename = xml_filename
        tree_root = ET.parse(file_name).getroot()

        if clean_wardrobe:
            self.clear_wardrobe()
            self.name = tree_root.attrib["name"]

        for outfit_element in tree_root.find("FullSets"):
            self.add_outfit(Wardrobe.outfit_from_xml(outfit_element))
        for outfit_element in tree_root.find("UnderwearSets"):
            self.add_underwear_set(Wardrobe.outfit_from_xml(outfit_element))
        for outfit_element in tree_root.find("OverwearSets"):
            self.add_overwear_set(Wardrobe.outfit_from_xml(outfit_element))

    @staticmethod
    def get_wardrobe_file(xml_filename: str):
        if not xml_filename.lower().endswith(".xml"):
            file_name = xml_filename + ".xml"
        wardrobe_file = None

        for file in renpy.list_files():
            if file_name in file:
                wardrobe_file = renpy.file(file)
                break

        return wardrobe_file

    @staticmethod
    def outfit_from_xml(outfit_element: ET.Element):
        def proper_name_to_clothing_copy(proper_name) -> Clothing | None:
            for match in panties_list + bra_list + pants_list + skirts_list + dress_list + shirts_list + socks_list + tights_list + shoes_list + earings_list + bracelet_list + rings_list + neckwear_list:
                if match.proper_name == proper_name:
                    return match.get_copy()
            return None

        return_outfit = Outfit(outfit_element.attrib["name"])
        clothing_mapping = {"UpperBody": Outfit.add_upper, "LowerBody": Outfit.add_lower, "Feet": Outfit.add_feet, "Accessories": Outfit.add_accessory}

        add_function: Callable[[Outfit, Clothing, list[float], str, list[float]], None]
        for location, add_function in clothing_mapping.items():
            for item_element in outfit_element.find(location):
                clothing_copy = proper_name_to_clothing_copy(item_element.attrib["name"])
                if clothing_copy:
                    clothing_colour = [float(item_element.attrib["red"]), float(item_element.attrib["green"]), float(item_element.attrib["blue"]), float(item_element.attrib["alpha"])]
                    pattern = item_element.get("pattern", None)
                    if pattern is not None:
                        colour_pattern = [float(item_element.attrib["pred"]), float(item_element.attrib["pgreen"]), float(item_element.attrib["pblue"]), float(item_element.attrib["palpha"])]
                    else:
                        colour_pattern = None
                    add_function(return_outfit, clothing_copy, clothing_colour, pattern, colour_pattern)
        return return_outfit
