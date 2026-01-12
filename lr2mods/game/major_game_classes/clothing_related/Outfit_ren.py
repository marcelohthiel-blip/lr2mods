from __future__ import annotations
from typing import Iterable
import builtins
import renpy
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.helper_functions.misc_helpers_ren import build_transparency_factor_map
from game.helper_functions.list_functions_ren import get_random_from_list
from game.clothing_lists_ren import mouth_cum, tits_cum, stomach_cum, face_cum, ass_cum, creampie_cum, tights_list, big_glasses, modern_glasses, pinafore, vest, skirt, long_skirt, pencil_skirt, nightgown_dress, suit_jacket, lace_skirt, belted_skirt, mini_skirt, micro_skirt, jeans, jean_hotpants, suitpants, capris, leggings, booty_shorts, daisy_dukes, apron
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.clothing_related.Facial_Accessories_ren import Facial_Accessory
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder
from game.major_game_classes.clothing_related.wardrobe_builder_ren import low_socks_list

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -7 python:
"""
from itertools import chain

class Outfit:  # A bunch of clothing added together, without slot conflicts.
    _swap_bottoms_map: dict[str, tuple[Clothing]] = {
        "Jeans": (long_skirt, ),
        "Suit_Pants": (pencil_skirt, long_skirt),
        "Capris": (pencil_skirt, skirt),
        "Leggings": (skirt, lace_skirt),
        "Jean_Hotpants": (lace_skirt, belted_skirt),
        "Booty_Shorts": (mini_skirt, belted_skirt),
        "Daisy_Dukes": (mini_skirt, micro_skirt),

        "Long_Skirt": (jeans, suitpants),
        "Pencil_Skirt": (suitpants, capris),
        "Lace_Skirt": (leggings, capris),
        "Skirt": (capris, leggings),
        "Belted_Skirt": (leggings, jean_hotpants),
        "Mini_Skirt": (booty_shorts, daisy_dukes),
        "Micro_Skirt": (daisy_dukes, )
    }

    @staticmethod
    def __cloth_sort_key(cloth: Clothing) -> float:
        key = cloth.layer
        if cloth.is_leotard:
            key = 1.2 # for sorting to layer 1.2 (over underwear but under layer 2)
        if cloth.is_garterbelt:
            key = 1.3 # also draw above leotard
        if cloth.is_shirt or cloth.is_bracelet:
            key += .2 # draw shirts over pants
        if cloth.is_nightgown:
            key += .1 # draw nightgowns over pants / skirts
        if cloth.is_gloves: # draw gloves under normal bracelets
            key -= .1
        if cloth.tucked: # tucked is always a between layer value
            key += .5
        if cloth.is_neckwear: # draw higher than other items in base layer
            key += .6
        return key

    @staticmethod
    def classification(slut_score: int) -> str:
        classifications = ["Conservative", "Timid", "Modest", "Casual", "Trendy", "Stylish", "Enticing", "Provocative", "Sensual", "Sexy", "Seductive", "Sultry", "Slutty"]
        ci = builtins.int(slut_score * .14)
        if ci >= builtins.len(classifications):
            return classifications[-1]
        return classifications[ci]

    def __init__(self, name: str):
        self.name = name
        self.upper_body: list[Clothing] = []
        self.lower_body: list[Clothing] = []
        self.feet: list[Clothing] = []
        self.accessories: list[Facial_Accessory] = [] #Extra stuff that doesn't fit anywhere else. Hats, glasses, ect.

    @property
    def identifier(self) -> int:
        return self.__hash__()

    def __hash__(self) -> int:
        return generate_identifier([x.identifier for x in self])

    def __eq__(self, other: Outfit) -> bool:
        if not isinstance(other, Outfit):
            return NotImplemented
        return self.name == other.name

    def matches(self, other: Outfit) -> bool:
        if not isinstance(other, Outfit):
            return False

        current_clothing = tuple(self.upper_body + self.lower_body + self.feet)
        other_clothing = tuple(other.upper_body + other.lower_body + other.feet)

        if len(current_clothing) != len(other_clothing):
            return False    # quick check

        return all(any(x.is_similar(y) for y in current_clothing) for x in other_clothing)

    def matches_overwear(self, other: Outfit) -> bool:
        if not isinstance(other, Outfit):
            return False

        current_clothing = tuple(x for x in self.upper_body + self.lower_body + self.feet if x.layer >= 2)
        other_clothing = tuple(x for x in other.upper_body + other.lower_body + other.feet if x.layer >= 2)

        if len(current_clothing) != len(other_clothing):
            return False    # quick check

        return all(any(x.is_similar(y) for y in current_clothing) for x in other_clothing)

    def matches_underwear(self, other: Outfit) -> bool:
        if not isinstance(other, Outfit):
            return False

        current_clothing = tuple(x for x in self.upper_body + self.lower_body + self.feet if x.layer < 2)
        other_clothing = tuple(x for x in other.upper_body + other.lower_body + other.feet if x.layer < 2)

        if len(current_clothing) != len(other_clothing):
            return False    # quick check

        return all(any(x.is_similar(y) for y in current_clothing) for x in other_clothing)

    def __iter__(self):
        return chain(self.upper_body, self.lower_body, self.feet, self.accessories)

    @property
    def item_count(self) -> int:
        '''
        Total number of items in outfit (including accessories)
        '''
        return self.clothing_count + len(self.accessories)

    @property
    def clothing_count(self) -> int:
        '''
        Total number of clothing items in outfit (excluding accessories)
        '''
        return len(self.upper_body) + len(self.lower_body) + len(self.feet)

    def clear(self):
        self.upper_body.clear()
        self.lower_body.clear()
        self.feet.clear()
        self.accessories.clear()

    def get_copy(self) -> Outfit:
        copy_outfit = Outfit(self.name)

        copy_outfit.feet = [x.get_copy() for x in self.feet]
        copy_outfit.upper_body = [x.get_copy() for x in self.upper_body]
        copy_outfit.lower_body = [x.get_copy() for x in self.lower_body if not x.is_extension]
        # copy extension objects for upper body to lower body (make sure we have same obj reference)
        copy_outfit.lower_body.extend([x.has_extension for x in copy_outfit.upper_body if x.has_extension])
        copy_outfit.accessories = [x.get_copy() for x in self.accessories]
        return copy_outfit

    def generate_draw_list(self, person: Person, position: str, emotion = "default", special_modifiers = None, lighting = None, hide_layers = None): #Generates a sorted list of displayables that when drawn display the outfit correctly.
        nipple_wetness = 0.0 # Used to simulate a girl lactating through clothing. Ranges from 0 (none) to 1 (Maximum Effect)
        if not isinstance(person, Person):
            body_type = "standard_body"
            tit_size = "D"
            face_style = "Face_1"

        else:
            body_type = person.body_type
            tit_size = person.tits
            face_style = person.face_style
            if person.lactation_sources > 0:
                nipple_wetness = (0.1 * (float(Person.rank_tits(person.tits) + person.lactation_sources))) * (person.arousal_perc / 100)
                if nipple_wetness > 1.0:
                    nipple_wetness = 1.0

        if hide_layers is None:
            hide_layers = []

        all_items = self.__generate_clothing_list() #First generate a list of the clothing objects

        currently_constrained_regions = []
        ordered_displayables = []
        for item in reversed(all_items): #To properly constrain items we need to figure out how they look from the outside in, even though we eventually draw from the inside out
            if isinstance(item, Facial_Accessory):
                if item.layer not in hide_layers:
                    ordered_displayables.append(item.generate_item_displayable(position, face_style, emotion, special_modifiers, lighting = lighting))
            elif not item.is_extension:
                if item.layer not in hide_layers:
                    ordered_displayables.append(item.generate_item_displayable(body_type, tit_size, position, lighting = lighting, regions_constrained = currently_constrained_regions, nipple_wetness = nipple_wetness))
                    for region in item.constrain_regions:
                        if item.half_off and region in item.half_off_regions:
                            pass # If an item is half off the regions that are hidden while half off are also not constrained by the clothing.
                        elif item.has_extension and item.has_extension.half_off and region in item.has_extension.half_off_regions:
                            pass # If the extension for an item (a dress bottom, for example) is half off and hiding something that section is not contrained.
                        else:
                            currently_constrained_regions.append(region)

        return reversed(ordered_displayables) #We iterated over all_items backwards, so our return list needs to be inverted

    def get_forced_modifier(self) -> str | None: #Returns, if one exists, a forced modifier caused by one of the facial accessories (Currently used to support ball gags)
        forced_special_modifier = None
        for item in self.accessories:
            if isinstance(item, Facial_Accessory) and item.modifier_lock is not None:
                forced_special_modifier = item.modifier_lock
        return forced_special_modifier

    def merge_outfit(self, other_outfit: Outfit, underwear_only = False) -> Outfit:
        if not isinstance(other_outfit, Outfit):
            return self
        # Takes other_outfit
        for cloth in (x for x in other_outfit.upper_body if not underwear_only or x.layer <= 2):
            self.add_upper(cloth.get_copy())
        for cloth in (x for x in other_outfit.lower_body if not x.is_extension and (not underwear_only or x.layer <= 2)):
            self.add_lower(cloth.get_copy())
        for cloth in (x for x in other_outfit.feet if not underwear_only or x.layer <= 2):
            self.add_feet(cloth.get_copy())
        for cloth in (x for x in other_outfit.accessories if not underwear_only or x.layer <= 2):
            self.add_accessory(cloth.get_copy())
        return self

    def can_add_dress(self, new_clothing: Clothing) -> bool:
        # special cases for items the would intersect each other
        if new_clothing.is_leotard and any(x for x in self.upper_body if x.is_similar(nightgown_dress)):
            return False
        if new_clothing.is_similar(nightgown_dress) and any(x for x in self.upper_body if x.is_leotard):
            return False
        return self.can_add_upper(new_clothing)

    def add_dress(self, new_clothing: Clothing, re_colour: list[float] | None = None, pattern: str | None = None, colour_pattern: list[float] | None = None) -> None:
        self.add_upper(new_clothing, re_colour = re_colour, pattern = pattern, colour_pattern = colour_pattern)

    def can_add_upper(self, new_clothing: Clothing) -> bool:
        allowed = not any(x for x in self.upper_body if x.name == new_clothing.name or (x.layer > 0 and x.layer == new_clothing.layer))
        if allowed and new_clothing.has_extension:
            return not any(x for x in self.lower_body if x.layer == new_clothing.has_extension.layer) \
                and not any(x for x in self.upper_body if x.has_extension and x.layer == new_clothing.has_extension.layer and x.has_extension.layer == new_clothing.layer)
        return allowed

    def add_upper(self, new_clothing: Clothing, re_colour: list[float] | None = None, pattern: str | None = None, colour_pattern: list[float] | None = None) -> None:
        if re_colour is not None:
            new_clothing.colour = re_colour

        if pattern is not None:
            new_clothing.pattern = pattern
            if colour_pattern is not None:
                new_clothing.colour_pattern = colour_pattern
            else:
                new_clothing.colour_pattern = new_clothing.colour

        if self.can_add_upper(new_clothing): ##Always check to make sure the clothing is valid before you add it.
            self.upper_body.append(new_clothing)
            if new_clothing.has_extension:
                self.lower_body.append(new_clothing.has_extension)

    def can_add_lower(self, new_clothing: Clothing) -> bool:
        return not any(x for x in self.lower_body if x.layer == new_clothing.layer)

    def add_lower(self, new_clothing, re_colour: list[float] | None = None, pattern: str | None = None, colour_pattern: list[float] | None = None) -> None:
        if re_colour is not None:
            new_clothing.colour = re_colour
        if pattern is not None:
            new_clothing.pattern = pattern
            if colour_pattern is not None:
                new_clothing.colour_pattern = colour_pattern
            else:
                new_clothing.colour_pattern = new_clothing.colour

        if self.can_add_lower(new_clothing):
            self.lower_body.append(new_clothing)

    def can_add_feet(self, new_clothing: Clothing) -> bool:
        return not any(x for x in self.feet if x.layer == new_clothing.layer)

    def add_feet(self, new_clothing: Clothing, re_colour: list[float] | None = None, pattern: str | None = None, colour_pattern: list[float] | None = None) -> None:
        if re_colour is not None:
            new_clothing.colour = re_colour

        if pattern is not None:
            new_clothing.pattern = pattern
            if colour_pattern is not None:
                new_clothing.colour_pattern = colour_pattern
            else:
                new_clothing.colour_pattern = new_clothing.colour

        if self.can_add_feet(new_clothing):
            self.feet.append(new_clothing)

    def can_add_accessory(self, new_clothing: Clothing) -> bool:
        return not any(x for x in self.accessories if x.is_similar(new_clothing))

    def add_accessory(self, new_clothing: Clothing, re_colour: list[float] | None = None, pattern: str | None = None, colour_pattern: list[float] | None = None) -> None:
        if re_colour is not None:
            new_clothing.colour = re_colour
        if pattern is not None:
            new_clothing.pattern = None
            if colour_pattern is not None:
                new_clothing.colour_pattern = colour_pattern
            else:
                new_clothing.colour_pattern = new_clothing.colour

        if self.can_add_accessory(new_clothing):
            self.accessories.append(new_clothing)

    def has_clothing(self, clothing: Clothing) -> bool:  #Returns True if this outfit includes the given clothing item, false otherwise. Checks for exact parameter match (colour, name, ect), but not reference match.
        return any(x for x in self if x.is_similar(clothing))

    def get_clothing(self, clothing: Clothing) -> Clothing | None:
        return next(x for x in self if x.is_similar(clothing))

    def remove_clothing(self, clothing: Clothing):
        '''
        Removes passed clothing item from this outfit.
        '''
        # If this is an extension, we should be removing from the base clothing
        if clothing.is_extension: # find matching clothing item
            if parent := next((x for x in self.upper_body if x.has_extension and x.has_extension.is_similar(clothing)), None):
                self.remove_clothing(parent)
                # Early return to prevent endless recursion
                return

        # Remove extension, if it exists
        if clothing.has_extension:
            part: list[Clothing]
            for part in (self.upper_body, self.lower_body, self.feet, self.accessories):
                if found := next((x for x in part if x.is_similar(clothing.has_extension)), None):
                    part.remove(found)

        # Remove each piece of clothing that matches
        for part in (self.upper_body, self.lower_body, self.feet, self.accessories):
            if found := next((x for x in part if x.is_similar(clothing)), None):
                part.remove(found)

    @property
    def has_half_off_clothing(self) -> bool:
        return any(x for x in self if x.half_off)

    @property
    def half_off_clothing_list(self) -> tuple[Clothing, ...]:
        return tuple(x for x in self if x.half_off)

    def half_off_clothing(self, clothing: Clothing):
        found = next((x for x in self if x.is_similar(clothing)), None)
        if found and found.can_be_half_off:
            found.half_off = True

    def remove_clothing_list(self, clothing_list: list[Clothing] | tuple[Clothing] | set[Clothing], half_off_instead = False):
        if not isinstance(clothing_list, (list, tuple, set)):
            return

        for item in clothing_list:
            if half_off_instead:
                self.half_off_clothing(item)
            else:
                self.remove_clothing(item)

    def restore_all_clothing(self):
        for cloth in self.half_off_clothing_list:
            cloth.half_off = False

    def get_upper_ordered(self) -> list[Clothing]: #Returns a list of pieces from bottom to top, on the upper body. Other functions do similar things, but to lower and feet.
        return sorted(self.upper_body, key = Outfit.__cloth_sort_key)

    def get_lower_ordered(self) -> list[Clothing]:
        return sorted(self.lower_body, key = Outfit.__cloth_sort_key)

    def get_feet_ordered(self) -> list[Clothing]:
        return sorted(self.feet, key = Outfit.__cloth_sort_key)

    @property
    def get_upper_top_layer(self) -> Clothing | None:
        if self.upper_body:
            return self.get_upper_ordered()[-1]
        return None

    @property
    def get_lower_top_layer(self) -> Clothing | None:
        if self.lower_body:
            return self.get_lower_ordered()[-1]
        return None

    @property
    def get_feet_top_layer(self) -> Clothing | None:
        if self.feet:
            return self.get_feet_ordered()[-1]
        return None

    def remove_random_any(self, top_layer_first = False, exclude_upper = False, exclude_lower = False, exclude_feet = False, do_not_remove = False) -> Clothing | None:
        #Picks a random upper, lower, or feet object to remove. Is guaranteed to remove something if possible, or return None if nothing on the person is removable (They're probably naked).
        functs_to_try = []
        if not exclude_upper:
            functs_to_try.append(self.remove_random_upper)
        if not exclude_lower:
            functs_to_try.append(self.remove_random_lower)
        if not exclude_feet:
            functs_to_try.append(self.remove_random_feet)
        renpy.random.shuffle(functs_to_try) #Shuffle the functions so they appear in a random order.
        for remover in functs_to_try: #Try removing each of an upper, lower, and feet. If any succeed break there and return what we removed. Otherwise keep trying. If we run out of things to try we could not remove anything.
            success = remover(top_layer_first, do_not_remove)
            if success:
                return success
        return None

    def remove_random_upper(self, top_layer_first = False, do_not_remove = False) -> Clothing | None:
        #if top_layer_first only the upper most layer is removed, otherwise anything unanchored is a valid target.
        #if do_not_remove is set to True we only use this to find something valid to remove and return that clothing item. this lets us use this function to find things to remove with an animation.
        #Returns None if there is nothing to be removed.
        to_remove = None
        if top_layer_first:
            #Just remove the very top layer
            if self.__get_upper_unanchored():
                to_remove = self.__get_upper_unanchored()[0]
                if to_remove.is_extension:
                    return None #Extensions can't be removed directly.
            else:
                return None
        else:
            to_remove = get_random_from_list(self.__get_upper_unanchored())
            if to_remove and to_remove.is_extension:
                return None

        if to_remove and to_remove.layer == 0: # don not nipple covers or cinchers
            return None

        if to_remove and not do_not_remove:
            self.remove_clothing(to_remove)
        return to_remove

    def remove_random_lower(self, top_layer_first = False, do_not_remove = False) -> Clothing | None:
        to_remove = None
        if top_layer_first:
            #Just remove the very top layer
            if self.__get_lower_unanchored():
                to_remove = self.__get_lower_unanchored()[0]
                if to_remove.is_extension:
                    return None #Extensions can't be removed directly.
            else:
                return None
        else:
            to_remove = get_random_from_list(self.__get_lower_unanchored())
            if to_remove and to_remove.is_extension:
                return None

        if to_remove and not do_not_remove:
            self.remove_clothing(to_remove)
        return to_remove

    def remove_overcoat(self):
        '''
        Remove all items that are marked as overcoats (lab_coat, vest, suit_jacket, apron, bath_robe)
        '''
        overcoat = next((x for x in self.upper_body if x.layer == 4), None)
        if overcoat:
            self.remove_clothing(overcoat)

    def remove_dress(self):
        for dress in (x for x in self.upper_body if x.is_dress):
            self.remove_clothing(dress)

    def remove_pants(self):
        for pants in (x for x in self.lower_body if x.is_pants):
            self.remove_clothing(pants)

    def remove_skirt(self):
        for skirt in (x for x in self.lower_body if x.is_skirt):
            self.remove_clothing(skirt)

    def remove_shirt(self):
        for shirt in (x for x in self.upper_body if x.is_shirt):
            self.remove_clothing(shirt)

    def remove_shoes(self):
        if any(x.layer >= 2 for x in self.feet):
            self.remove_clothing(self.get_feet_top_layer)

    def remove_socks_or_stockings(self):
        for sock in (x for x in self.feet if x.is_socks):
            self.remove_clothing(sock)

    def remove_tights(self):
        for tight in (x for x in self.lower_body if x.layer == 2 and any(y for y in tights_list if y.is_similar(x))):
            self.remove_clothing(tight)

    def remove_random_feet(self, top_layer_first = False, do_not_remove = False) -> Clothing | None:
        to_remove = None
        if top_layer_first:
            #Just remove the very top layer
            if self.__get_foot_unanchored():
                to_remove = self.__get_foot_unanchored()[0]
                if to_remove.is_extension:
                    return None #Extensions can't be removed directly.
            else:
                return None
        else:
            to_remove = get_random_from_list(self.__get_foot_unanchored())
            if to_remove and to_remove.is_extension:
                return None

        if to_remove and not do_not_remove:
            self.remove_clothing(to_remove)
        return to_remove

    def get_unanchored(self, half_off_instead = False) -> list[Clothing]: #Returns a list of the pieces of clothing that can be removed.
        #Question: should be be able to remove accessories like this? We would need a way to flag some things like makeup as unremovable.
        # Note: half_off_instead returns a list of clothing items that can be half-offed, which means either they are completely unanchored, or they are anchored but all upper layers are half-off and half-off gives access
        return_list = []
        return_list.extend(self.__get_upper_unanchored(half_off_instead))
        return_list.extend(self.__get_lower_unanchored(half_off_instead))
        return_list.extend(self.__get_foot_unanchored(half_off_instead))

        return return_list

    def is_item_unanchored(self, the_clothing, half_off_instead = False, exclude_upper = False, exclude_lower = False, exclude_feet = False) -> bool: #Returns true if the clothing item passed is unanchored, ie. could be logically taken off.
        if not exclude_lower and the_clothing in self.lower_body:
            return the_clothing in self.__get_lower_unanchored(half_off_instead)
        if not exclude_upper and the_clothing in self.upper_body:
            return the_clothing in self.__get_upper_unanchored(half_off_instead)
        if not exclude_feet and the_clothing in self.feet:
            return the_clothing in self.__get_foot_unanchored(half_off_instead)
        return True

    @property
    def vagina_available(self) -> bool: ## Doubles for asshole for anal.
        return not any(x for x in self.lower_body if x.anchor_below and not (x.half_off and x.half_off_gives_access))

    @property
    def vagina_visible(self) -> bool:
        return not any(x for x in self.lower_body if x.hide_below and not (x.half_off and x.half_off_gives_access))

    @property
    def tits_available(self) -> bool:
        return not any(x for x in self.upper_body if x.anchor_below and x not in (vest, suit_jacket) and not (x.half_off and x.half_off_gives_access))

    @property
    def tits_visible(self) -> bool:
        return not any(x for x in self.upper_body if x.hide_below and x not in (vest, suit_jacket) and not (x.half_off and x.half_off_gives_access))

    @property
    def underwear_visible(self) -> bool:
        return (self.wearing_bra and not self.bra_covered) or \
            (self.wearing_panties and not self.panties_covered)

    @property
    def feet_available(self) -> bool:
        return not any(x for x in self.feet if x.anchor_below)

    @property
    def feet_visible(self) -> bool:
        return not any(x for x in self.feet if x.hide_below)

    @property
    def wearing_bra(self) -> bool:
        return any(x for x in self.upper_body if (x.underwear and not x.layer == 0))

    @property
    def bra_is_lingerie(self) -> bool:
        '''
        Returns True when wearing a bra that is lingerie
        '''
        return self.wearing_bra and self.get_bra().slut_value > 2

    @property
    def can_remove_bra(self) -> bool:
        if (bra := self.get_bra()):
            unanchored = self.__get_upper_unanchored()
            return bra in unanchored
        return None

    def get_bra(self) -> Clothing | None:
        return next((x for x in self.upper_body if x.underwear and not x.layer == 0), None)

    def remove_bra(self) -> Clothing | None:
        if (bra := self.get_bra()):
            self.remove_clothing(bra)
            return bra
        return None

    @property
    def wearing_panties(self) -> bool:
        return any(x for x in self.lower_body if x.underwear and not x.layer == 0) \
            or any(x for x in self.upper_body if x.is_leotard)

    @property
    def panties_is_lingerie(self) -> bool:
        '''
        Returns True when wearing panties that are lingerie
        '''
        return self.wearing_panties and self.get_panties().slut_value > 2

    @property
    def can_remove_panties(self) -> bool:
        if (panties := self.get_panties()):
            unanchored = self.__get_lower_unanchored()
            return panties in unanchored
        return False

    def get_panties(self) -> Clothing | None:
        return next((x for x in self.lower_body if x.underwear and not x.layer == 0),
                next((x for x in self.upper_body if x.is_leotard), None))

    def remove_panties(self) -> Clothing | None:
        if (panties := self.get_panties()):
            self.remove_clothing(panties)
            return panties
        return None

    def remove_bra_and_panties(self) -> tuple[Clothing, Clothing]:
        bra = self.remove_bra()
        panties = self.remove_panties()
        return (bra, panties)

    @property
    def bra_covered(self) -> bool:
        if not self.wearing_bra:
            return False

        for cloth in self.get_upper_ordered()[::-1]: #Traverse list from outside in
            if cloth.underwear:
                return False
            if cloth.hide_below and not (cloth.half_off and cloth.half_off_reveals):
                return True
        return False

    @property
    def is_bra_visible(self) -> bool:
        return self.wearing_bra and not self.bra_covered

    @property
    def panties_covered(self) -> bool:
        if not self.wearing_panties:
            return False

        for cloth in self.get_lower_ordered()[::-1]: #Traverse list from outside in
            if cloth.underwear:
                return False
            if cloth.hide_below and not (cloth.half_off and cloth.half_off_reveals):
                return True
        return False

    @property
    def are_panties_visible(self) -> bool:
        return self.wearing_panties and not self.panties_covered

    @property
    def has_overwear(self) -> bool: #Returns true if the outfit has layer 2 clothing items for upper and lower body.
        if any(x == nightgown_dress for x in self.upper_body):
            return False
        if (not any(x.layer >= 2 for x in self.upper_body)
                and not any(x.layer >= 2 for x in self.lower_body)):
            return False
        return True

    @property
    def has_underwear(self) -> bool:
        '''
        True when wearing bra and panties
        '''
        return self.wearing_bra and self.wearing_panties

    @property
    def is_wearing_underwear(self) -> bool:
        '''
        True when wearing either bra or panties
        '''
        return self.wearing_bra or self.wearing_panties

    @property
    def is_suitable_underwear_set(self) -> bool: #Returns true if the outfit could qualify as an underwear set ie. Only layer 1 clothing.
        return not any(x for x in self if x.layer > 2)

    @property
    def is_suitable_overwear_set(self) -> bool: #Returns true if the outfit could qualify as an overwear set ie. contains no layer 1 clothing.
        return not any(x for x in self if x.layer < 2)

    @property
    def shows_off_her_ass(self) -> bool:
        if self.has_overwear:
            return any(x for x in self if x.layer >= 2 and any(y for y in WardrobeBuilder.preferences["showing her ass"]["lower_body"] + WardrobeBuilder.preferences["showing her ass"]["upper_body"] if y.is_similar(x)))
        return any(x for x in self if any(y for y in WardrobeBuilder.preferences["showing her ass"]["lower_body"] + WardrobeBuilder.preferences["showing her ass"]["upper_body"] if y.is_similar(x)))

    @property
    def shows_off_her_tits(self) -> bool:
        if self.has_overwear:
            return any(x for x in self if x.layer >= 2 and any(y for y in WardrobeBuilder.preferences["showing her tits"]["upper_body"] if y.is_similar(x)))
        return any(x for x in self if any(y for y in WardrobeBuilder.preferences["showing her tits"]["upper_body"] if y.is_similar(x)))

    @property
    def underwear_slut_score(self) -> int: #Calculates the sluttiness of this outfit assuming it's an underwear set. We assume a modest overwear set is used (ie. one that covers visibility).
        # showing tits or ass has ony 50% impact on underwear slut score (fully naked == 30 slut)
        new_score = self.__get_body_parts_slut_score(outfit_type = "under")
        new_score += self.__get_total_slut_modifiers()
        return min(new_score, 100)

    @property
    def overwear_slut_score(self) -> int: #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
        new_score = self.__get_body_parts_slut_score(outfit_type = "over")
        new_score += self.__get_total_slut_modifiers()
        return min(new_score, 100)

    @property
    def outfit_slut_score(self) -> int: #Calculates the sluttiness of this outfit assuming it's a full outfit. Full penalties and such apply.
        new_score = self.__get_body_parts_slut_score(outfit_type = "full")
        new_score += self.__get_total_slut_modifiers()
        # penalty for not having an overwear item
        if not any(x.layer >= 3 for x in self.upper_body):
            new_score += 15
        if not any(x.layer >= 3 for x in self.lower_body):
            new_score += 15
        return min(new_score, 100)

    @property
    def outfit_lust_score(self) -> int: #Calculates the sluttiness of this outfit with no upper limit. User for determining outfit lust gains.
        new_score = self.__get_body_parts_slut_score(outfit_type = "full")
        new_score += self.__get_total_slut_modifiers()
        return new_score

    def get_full_strip_list(self, strip_feet = True, strip_accessories = False) -> list[Clothing]:
        items_to_strip = [x for x in self.lower_body if not x.is_extension] + [x for x in self.upper_body if x.layer > (-1 if strip_accessories else 0)]
        if strip_feet:
            items_to_strip.extend(self.feet)
        if strip_accessories: # exclude make-up and earrings
            items_to_strip.extend((x for x in self.accessories if not (x.is_makeup or x.is_earring or x.is_glasses or x.is_mask)))
        items_to_strip.sort(key= lambda clothing: clothing.tucked, reverse = True) #Tucked upper body stuff draws after lower body.
        items_to_strip.sort(key= lambda clothing: clothing.layer) #Sort the clothing so it is removed top to bottom based on layer.
        return items_to_strip[::-1] #Put it in reverse order so when stripped it will be done from outside in.

    def get_underwear_top_strip_list(self, visible_enough = True, avoid_nudity = False, test_outfit = None) -> list[Clothing]:
        items_to_strip = []

        if not test_outfit:
            test_outfit = self.get_copy() #We'll use a copy of the outfit. Slightly less efficient, but makes it easier to ensure we are generating valid strip orders.

        keep_stripping = not (self.is_bra_visible or self.tits_visible)
        while keep_stripping:
            keep_stripping = False
            item = test_outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
            if item is not None and not item.underwear:
                test_outfit.remove_clothing(item)
                if avoid_nudity and test_outfit.tits_visible:
                    pass # would result in nudity
                elif (test_outfit.is_bra_visible or test_outfit.tits_visible):
                    items_to_strip.append(item)
                else:
                    items_to_strip.append(item)
                    keep_stripping = True

        if self.has_overwear:   # special check for outer wear
            item = test_outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
            if item and not item.underwear:
                test_outfit.remove_clothing(item)
                items_to_strip.insert(0, item)

        return items_to_strip

    def get_underwear_bottom_strip_list(self, visible_enough = True, avoid_nudity = False, test_outfit = None) -> list[Clothing]:
        items_to_strip = []
        if not test_outfit:
            test_outfit = self.get_copy() #We'll use a copy of the outfit. Slightly less efficient, but makes it easier to ensure we are generating valid strip orders.

        keep_stripping = not (self.are_panties_visible or self.vagina_visible)
        while keep_stripping:
            keep_stripping = False
            item = test_outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
            if item is not None and not item.underwear:
                test_outfit.remove_clothing(item)
                if avoid_nudity and test_outfit.vagina_visible:
                    pass # would result in nudity
                elif (test_outfit.are_panties_visible or test_outfit.vagina_visible):
                    items_to_strip.append(item)
                    if test_outfit.has_tights:
                        keep_stripping = True
                else:
                    items_to_strip.append(item)
                    keep_stripping = True

        return items_to_strip

    def get_underwear_strip_list(self, visible_enough = True, avoid_nudity = False, strip_shoes = False) -> list[Clothing]:
        #If a girl isn't wearing underwear this ends up being a full strip. If she is wearing only a bra/panties she'll strip until they are visible, and the other slot is naked.
        test_outfit = self.get_copy() #We'll use a copy of the outfit. Slightly less efficient, but makes it easier to ensure we are generating valid strip orders.
        items_to_strip = []

        items_to_strip.extend(self.get_underwear_top_strip_list(avoid_nudity = avoid_nudity, test_outfit = test_outfit))
        items_to_strip.extend(self.get_underwear_bottom_strip_list(avoid_nudity = avoid_nudity, test_outfit = test_outfit))

        if strip_shoes:
            for item in self.get_feet_ordered():
                if item.layer == 2:
                    items_to_strip.insert(0, item) #Inserts shoes at the start of the list, since they're the first thing that should be removed.

        return items_to_strip

    def strip_full_outfit(self, strip_feet = False, strip_accessories = False, half_off_instead = False) -> bool:
        '''
        Use to off screen remove all clothing from the outfit
        strip_feet = True will also remove shoes and stockings
        strip_accessories = True will also remove any accessories she is wearing
        half_off_instead = True will half_off (partially hide) instead of remove the clothing items
        Return True when any clothing is removed else False
        '''
        clothing_list = self.get_full_strip_list(strip_feet = strip_feet, strip_accessories = strip_accessories)
        self.remove_clothing_list(clothing_list, half_off_instead)
        return len(clothing_list) > 0

    def strip_to_underwear(self, visible_enough = True, avoid_nudity = False, strip_shoes = False, half_off_instead = False) -> bool:
        '''
        Use to off screen remove all outerlayer clothing from the outfit
        [Deprecated]visible_enough = False will use is_availabe check instead of is_visible check
        avoid_nudity = True will not strip clothing that would result in nudity
        strip_shoes = True will also remove shoes
        half_off_instead = True will half_off (partially hide) instead of remove the clothing items
        Return True when any clothing is removed else False
        '''
        clothing_list = self.get_underwear_strip_list(visible_enough, avoid_nudity, strip_shoes)
        self.remove_clothing_list(clothing_list, half_off_instead)
        return len(clothing_list) > 0

    def strip_top_to_underwear(self, visible_enough = True, avoid_nudity = False, half_off_instead = False) -> bool:
        '''
        Use to off screen remove all outerlayer clothing from the upper body of the outfit
        [Deprecated]visible_enough = False will use is_availabe check instead of is_visible check
        avoid_nudity = True will not strip clothing that would result in nudity
        half_off_instead = True will half_off (partially hide) instead of remove the clothing items
        Return True when any clothing is removed else False
        '''
        clothing_list = self.get_underwear_top_strip_list(avoid_nudity = avoid_nudity, test_outfit = self.get_copy())
        self.remove_clothing_list(clothing_list, half_off_instead)
        return len(clothing_list) > 0

    def strip_bottom_to_underwear(self, visible_enough = True, avoid_nudity = False, half_off_instead = False) -> bool:
        '''
        Use to off screen remove all outerlayer clothing from the lower body outfit
        [Deprecated]visible_enough = False will use is_availabe check instead of is_visible check
        avoid_nudity = True will not strip clothing that would result in nudity
        half_off_instead = True will half_off (partially hide) instead of remove the clothing items
        Return True when any clothing is removed else False
        '''
        clothing_list = self.get_underwear_bottom_strip_list(avoid_nudity = avoid_nudity, test_outfit = self.get_copy())
        self.remove_clothing_list(clothing_list, half_off_instead)
        return len(clothing_list) > 0

    def get_tit_strip_list(self, visible_enough = True) -> list[Clothing]: #Generates a list of clothing that, when removed from this outfit, result in tits being visible. Useful for animated clothing removal.
        '''
        param:
            visible_enough [DEPRECATED] - had no effect
        '''
        test_outfit = self.get_copy()
        items_to_strip = []
        while not test_outfit.tits_visible:
            the_item = test_outfit.remove_random_upper(top_layer_first = True)
            if not the_item:
                the_item = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)
            if not the_item:
                break
            items_to_strip.append(the_item)
        # insert any coats (even if tits are visible)
        for item in (x for x in test_outfit.upper_body if x.layer > 3):
            items_to_strip.insert(0, item)
        return [x for x in items_to_strip if x.layer != 0]

    def strip_to_tits(self, visible_enough = True, prefer_half_off = False): #Removes all clothing from this item until breasts are visible.
        '''
        Use to off screen remove all clothing from the upper body outfit
        [Deprecated]visible_enough = False will use is_availabe check instead of is_visible check
        prefer_half_off = True will half_off (partially hide) if possible
        Return True when any clothing is removed else False
        '''
        half_off_instead = False
        if prefer_half_off and self.can_half_off_to_tits():
            clothing_list = self.get_half_off_to_tits_list(visible_enough)
            half_off_instead = True
        else:
            clothing_list = self.get_tit_strip_list()
        self.remove_clothing_list(clothing_list, half_off_instead)
        return len(clothing_list) > 0

    def get_vagina_strip_list(self, visible_enough = True) -> list[Clothing]:
        '''
        param:
            visible_enough [DEPRECATED] has no effect
        '''
        test_outfit = self.get_copy()
        items_to_strip = []
        while not test_outfit.vagina_visible:
            the_item = test_outfit.remove_random_lower(top_layer_first = True) #Try and remove lower layer clothing first each loop
            if not the_item:
                the_item = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True) #If that fails to make progress (ie. due to upper body items blocking things) remove upper body stuff until we can make progress again.
            if not the_item:
                break
            items_to_strip.append(the_item)
        return items_to_strip

    def strip_to_vagina(self, visible_enough = True, prefer_half_off = False):
        '''
        Use to off screen remove all clothing from the lower body outfit
        [Deprecated]visible_enough = False will use is_availabe check instead of is_visible check
        prefer_half_off = True will half_off (partially hide) if possible
        Return True when any clothing is removed else False
        '''
        half_off_instead = False
        if prefer_half_off and self.can_half_off_to_vagina(visible_enough):
            clothing_list = self.get_half_off_to_vagina_list(visible_enough)
            half_off_instead = True
        else:
            clothing_list = self.get_vagina_strip_list()
        self.remove_clothing_list(clothing_list, half_off_instead)
        return len(clothing_list) > 0

    def can_half_off_to_tits(self, visible_enough = True) -> bool:
        # Returns true if all of the clothing blocking her tits can be moved half-off to gain access, or if you already have access
        return (self.tits_visible
            or len(self.get_half_off_to_tits_list(visible_enough)) > 0)

    def get_half_off_to_tits_list(self, visible_enough = True) -> list[Clothing]:
        # If possible returns the list of clothing items, from outer to inner, that must be half-offed to gain view/access to her tits
        # If not possible returns an empty list.
        return_list = []
        possible = True
        anchored = None #Set to true when we hit something that stays anchored even if half-off. If that
        for item in self.get_upper_ordered()[::-1]: #Ordered top to bottom
            if visible_enough:
                if item.hide_below and not (item.can_be_half_off and item.half_off_reveals): #If a piece of clothing hides what's below and it's anchored or
                    possible = False
                    break
                if item.hide_below:
                    if anchored:
                        if item.can_be_half_off and item.half_off_gives_access:
                            if anchored not in return_list:
                                return_list.append(anchored)
                            anchored = None #Something would anchor the clothing, but it can be removed easily enough.
                        else:
                            possible = False #Something is in the way and we can't get it off because of something else
                            break
                    if item not in return_list:
                        return_list.append(item) #Half-off the anchoring item, then the thing in the way.

                if item.anchor_below:
                    anchored = item

            else:
                if item.anchor_below and not (item.can_be_half_off and item.half_off_gives_access):
                    possible = False
                    break

                if item.anchor_below and item not in return_list:
                    return_list.append(item)

        if not possible:
            return []
        return return_list

    def can_half_off_to_vagina(self, visible_enough = True) -> bool:
        # Returns true if all of the clothing blocking her vagina can be moved half-off to gain access
        return (self.vagina_visible
            or len(self.get_half_off_to_vagina_list(visible_enough)) > 0)

    def get_half_off_to_vagina_list(self, visible_enough = True) -> list[Clothing]:
        # If possible returns the list of clothing items, from outer to inner, that must be half-offed to gain view/access to her vagina
        # If not possible returns an empty list.
        return_list = []
        possible = True
        anchored = None #Set to true when we hit something that stays anchored even if half-off. If that
        for item in self.get_lower_ordered()[::-1]: #Ordered top to bottom
            if visible_enough:
                if item.hide_below and not (item.can_be_half_off and item.half_off_reveals): #If a piece of clothing hides what's be below and it's anchored or
                    possible = False
                    break
                if item.hide_below or item.can_be_half_off:
                    if anchored:
                        if item.can_be_half_off and item.half_off_gives_access:
                            if anchored not in return_list:
                                return_list.append(anchored)
                            anchored = None #Something would anchor the clothing, but it can be removed easily enough.
                        else:
                            possible = False #Something is in the way and we can't get it off because of something else
                            break

                    if item not in return_list:
                        return_list.append(item) #Half-off the anchoring item if we didn't already

                if item.anchor_below:
                    anchored = item

            else:
                if item.anchor_below and not (item.can_be_half_off and item.half_off_gives_access):
                    possible = False
                    break

                if (item.anchor_below or item.can_be_half_off) and item not in return_list:
                    return_list.append(item)

        if not possible:
            return []
        return return_list

    @property
    def cum_covered(self) -> bool:
        return any(x for x in self.accessories if x.name in (mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name))

    def remove_all_cum(self, from_clothing = True):
        for acc in (x for x in self.accessories if (from_clothing or x.layer == 0) and x.name in (mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name)):
            self.accessories.remove(acc)

    def add_mouth_cum(self):
        if self.can_add_accessory(mouth_cum):
            self.add_accessory(mouth_cum.get_copy())

    @property
    def has_mouth_cum(self) -> bool:
        return any(x.name == mouth_cum.name for x in self.accessories)

    def add_tits_cum(self):
        if self.can_add_accessory(tits_cum):
            layer = 0
            if clothing := next((x for x in reversed(self.get_upper_ordered()) if not x.half_off), None):
                layer = clothing.layer
            cumshot = tits_cum.get_copy()
            cumshot.layer = layer + 1
            self.add_accessory(cumshot)

    @property
    def has_tits_cum(self) -> bool:
        return any(x.name == tits_cum.name for x in self.accessories)

    def add_stomach_cum(self):
        if self.can_add_accessory(stomach_cum):
            layer = 0
            if clothing := next((x for x in reversed(self.get_upper_ordered()) if not x.half_off), None):
                layer = clothing.layer
            cumshot = stomach_cum.get_copy()
            cumshot.layer = layer + 1
            self.add_accessory(cumshot)

    @property
    def has_stomach_cum(self) -> bool:
        return any(x.name == stomach_cum.name for x in self.accessories)

    def add_face_cum(self):
        if self.can_add_accessory(face_cum):
            self.add_accessory(face_cum.get_copy())

    @property
    def has_face_cum(self) -> bool:
        return any(x.name == face_cum.name for x in self.accessories)

    def add_ass_cum(self):
        if self.can_add_accessory(ass_cum):
            layer = 0
            if clothing := next((x for x in reversed(self.get_lower_ordered()) if not x.half_off), None):
                layer = clothing.layer
            cumshot = ass_cum.get_copy()
            cumshot.layer = layer + 1
            self.add_accessory(cumshot)

    @property
    def has_ass_cum(self) -> bool:
        return any(x.name == ass_cum.name for x in self.accessories)

    def add_creampie_cum(self):
        if self.can_add_accessory(creampie_cum):
            self.add_accessory(creampie_cum.get_copy())

    @property
    def has_creampie_cum(self) -> bool:
        return any(x.name == creampie_cum.name for x in self.accessories)

    @property
    def has_dress(self) -> bool:
        return any(x for x in self if x.is_dress)

    @property
    def dress(self) -> Clothing | None:
        return next((x for x in self if x.is_dress), None)

    @property
    def has_skirt(self) -> bool:
        return any(x for x in self if x.is_skirt)

    @property
    def skirt(self) -> Clothing | None:
        return next((x for x in self if x.is_skirt), None)

    @property
    def has_pants(self) -> bool:
        return any(x for x in self if x.is_pants)

    @property
    def pants(self) -> Clothing | None:
        return next((x for x in self if x.is_pants), None)

    @property
    def has_shirt(self) -> bool:
        return any(x for x in self if x.is_shirt)

    @property
    def shirt(self) -> Clothing | None:
        return next((x for x in self if x.is_shirt), None)

    @property
    def has_socks(self) -> bool:
        return any(x for x in self if x.is_socks)

    @property
    def has_tights(self) -> bool:
        return any(self.has_clothing(item) for item in tights_list)

    @property
    def has_low_socks(self) -> bool:
        return any(self.has_clothing(item) for item in low_socks_list)

    @property
    def has_thigh_high_socks(self) -> bool:
        return any(x for x in self if x.is_thigh_high_sock)

    @property
    def has_shoes(self) -> bool:
        return any(x for x in self if x.is_shoes)

    @property
    def has_boots(self) -> bool:
        return any(x for x in self if x.is_boots)

    @property
    def has_apron(self) -> bool:
        return self.has_clothing(apron)

    @property
    def has_high_heels(self) -> bool:
        return any(x for x in self if x.is_high_heels)

    @property
    def has_one_piece(self) -> bool:
        return any(x for x in self if x.is_one_piece)

    @property
    def has_bracelet(self) -> bool:
        return any(x for x in self if x.is_bracelet)

    @property
    def has_glasses(self) -> bool:
        return any(x for x in self.accessories if x.name in (big_glasses.name, modern_glasses.name))

    def remove_glasses(self):
        for acc in (x for x in self.accessories if x.name in (big_glasses.name, modern_glasses.name)):
            self.accessories.remove(acc)

    @property
    def has_full_access(self) -> bool:
        return (self.tits_visible and self.tits_available and not self.wearing_bra
            and self.vagina_visible and self.vagina_available and not self.wearing_panties
            and not any(x.layer >= 2 for x in self.upper_body if not x.half_off)
            and not any(x.layer >= 2 for x in self.lower_body if not x.half_off))

    @property
    def is_easier_access(self) -> bool:
        return not any(x for x in self.lower_body if x.layer >= 2 and x.anchor_below)

    def make_easier_access(self) -> bool:
        if self.has_pants:
            self.swap_outfit_bottoms()
            return True

        for item in self.upper_body:
            if item.is_similar(pinafore):
                new_item_top = vest.get_copy()
                new_item_top.colour = item.colour
                new_item_bottom = skirt.get_copy()
                new_item_bottom.colour = item.colour
                self.remove_clothing(item)
                self.add_upper(new_item_top)
                self.add_lower(new_item_bottom)
                return True
        for item in self.lower_body:
            if item.is_similar(long_skirt) or item.is_similar(pencil_skirt):
                new_item = skirt.get_copy()
                new_item.colour = item.colour
                self.remove_clothing(item)
                self.add_lower(new_item)
                return True
        return False

    def swap_outfit_bottoms(self):
        for item in (x for x in self.lower_body if x.proper_name in Outfit._swap_bottoms_map):
            swap_item: Clothing = get_random_from_list(Outfit._swap_bottoms_map[item.proper_name]).get_copy()
            swap_item.colour = item.colour
            self.lower_body.remove(item)
            self.add_lower(swap_item)

    def remove_all_collars(self):
        for collar_name in ("Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Spiked_Choker"):
            if found := next((x for x in self.accessories if x.proper_name == collar_name), None):
                self.accessories.remove(found)

    # Quickly make her show tits
    # ignores stripping logic where skirt / pants might be removed to show tits
    def remove_all_upper_clothing(self):
        for item in self.get_upper_ordered():
            self.remove_clothing(item)

    def build_outfit_name(self) -> str:
        def get_clothing_items(outfit_part):
            return sorted([x for x in outfit_part if not x.is_extension and (x in (pinafore, ) or x.layer < 4)], key = lambda x: x.layer, reverse = True)

        outfitname = ""
        upper = get_clothing_items(self.upper_body)
        if upper:
            outfitname += upper[0].name

        lower = get_clothing_items(self.lower_body)
        if upper and lower:
            outfitname += " and "
        if lower:
            outfitname += lower[0].name

        feet = get_clothing_items(self.feet)
        if feet:
            if len(outfitname) == 0:
                outfitname = " with ".join([x.name for x in feet])
            else:
                if builtins.len(outfitname) != 0:
                    outfitname += " with "
                outfitname += feet[0].name

        if builtins.len(outfitname) == 0:
            return "Naked"

        self.name = f"{Outfit.classification(self.outfit_slut_score)} {outfitname}"

        return self.name

    def update_name(self):
        self.name = self.build_outfit_name()

    @property
    def is_legal_in_public(self) -> bool:
        if mc.business.nudity_is_legal or (not self.tits_visible and not self.vagina_visible):
            return True
        if self.vagina_visible:
            return False
        if mc.business.topless_is_legal and not self.vagina_visible:
            return True
        return False

    def __get_upper_unanchored(self, half_off_instead = False) -> list[Clothing]:
        return_list = []
        for top in reversed(self.get_upper_ordered()):
            if top.has_extension is None or self.is_item_unanchored(top.has_extension, half_off_instead, exclude_upper = True): #Clothing items that cover two slots (dresses) are unanchored if both halves are unanchored.
                if not half_off_instead or (half_off_instead and top.can_be_half_off):
                    return_list.append(top) #Always add the first item because the top is, by definition, unanchored

            if top.anchor_below and not (half_off_instead and top.half_off and top.half_off_gives_access):
                break #Search the list, starting at the outermost item, until you find something that anchors the stuff below it.
        return return_list

    def __get_lower_unanchored(self, half_off_instead = False) -> list[Clothing]:
        return_list = []
        for bottom in reversed(self.get_lower_ordered()):
            if bottom.has_extension is None or self.is_item_unanchored(bottom.has_extension, half_off_instead, exclude_lower = True):
                if not half_off_instead or (half_off_instead and bottom.can_be_half_off):
                    return_list.append(bottom)

            if bottom.anchor_below and not (half_off_instead and bottom.half_off and bottom.half_off_gives_access):
                break
        return return_list

    def __get_foot_unanchored(self, half_off_instead = False) -> list[Clothing]:
        return_list = []
        for foot in reversed(self.get_feet_ordered()):
            if foot.has_extension is None or self.is_item_unanchored(foot.has_extension, half_off_instead, exclude_feet = True):
                if not half_off_instead or (half_off_instead and foot.can_be_half_off):
                    return_list.append(foot)

            if foot.anchor_below and not (half_off_instead and foot.half_off and foot.half_off_gives_access):
                break
        return return_list

    def __generate_clothing_list(self) -> list[Clothing]:
        return sorted(self, key = Outfit.__cloth_sort_key)

    _transparency_factor_map = build_transparency_factor_map()

    def __get_body_parts_slut_score(self, outfit_type = "full") -> int:
        def get_transparency_factor(cloth_list: Iterable[Clothing]) -> float:
            if not cloth_list:
                return 0    # return zero to provide no points score for caller

            alpha_values = [(x.transparency if not x.underwear else (x.transparency - .2)) for x in cloth_list if x.hide_below]
            avg_transparency = max(sum(alpha_values) / len(alpha_values), .25)

            # the more transparent, the higher the factor returned, this scales logarithmically
            return Outfit._transparency_factor_map.get(round(avg_transparency, 2), 0.0)

        tits_score = 0
        if self.tits_visible:
            tits_score += 20
        elif self.tits_available:
            tits_score += 10 + (10 * get_transparency_factor(x for x in self.upper_body if x.hide_below))
        else:
            tits_score += 20 * get_transparency_factor(x for x in self.upper_body if x.hide_below)

        if outfit_type == "full":
            if self.tits_visible:
                tits_score += 15
            elif not self.wearing_bra:
                tits_score += 10
            elif self.wearing_bra and self.is_bra_visible:
                tits_score += 5
        elif outfit_type == "over" and self.tits_visible:
            tits_score += 10

        vagina_score = 0
        if self.vagina_visible:
            vagina_score += 20
        elif self.vagina_available:
            vagina_score += 10 + (10 * get_transparency_factor(x for x in self.lower_body if x.hide_below))
        else:
            vagina_score += 20 * get_transparency_factor(x for x in self.lower_body if x.hide_below)

        if outfit_type == "full":
            if self.vagina_visible:
                vagina_score += 15
            elif not self.wearing_panties:
                vagina_score += 10
            elif self.wearing_panties and self.are_panties_visible:
                vagina_score += 5
        elif outfit_type == "over" and self.vagina_visible:
            vagina_score += 10

        factor = 1.0
        if outfit_type == "under":
            factor = 0.5

        return builtins.int((tits_score + vagina_score) * factor)

    def __get_total_slut_modifiers(self) -> int: #Calculates the sluttiness boost purely do to the different pieces of clothing and not what is hidden/revealed.
        return sum(x.slut_score for x in self)
