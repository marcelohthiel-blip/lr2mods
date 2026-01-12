from __future__ import annotations
from renpy.rollback import NoRollback
from game.clothing_lists_ren import lace_skirt, long_skirt, lab_coat, suitpants, long_tshirt, camisole, dress_shirt, long_sleeve_blouse, tie_sweater, long_sweater, bath_robe
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.clothing_related.wardrobe_builder_ren import Outfit
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""

class WardrobePreference(NoRollback):
    hide_ass_list = [lace_skirt, long_skirt, lab_coat, suitpants, long_tshirt, camisole]
    hide_tits_list = [lab_coat, dress_shirt, long_sleeve_blouse, tie_sweater, long_sweater, bath_robe]

    @staticmethod
    def get_skirt_dress_and_pants_preference(person: Person):
        skirts_score = person.opinion.skirts
        pants_score = person.opinion.pants
        dress_score = person.opinion.dresses
        exclude_skirts = skirts_score == -2
        exclude_pants = pants_score == -2
        exclude_dresses = dress_score == -2

        # break tie when they don't like both.
        if exclude_skirts and exclude_pants and exclude_skirts:
            if pants_score > skirts_score and pants_score > dress_score:
                exclude_pants = False
            elif skirts_score > pants_score and pants_score > dress_score:
                exclude_skirts = False
            elif dress_score > skirts_score and dress_score > pants_score:
                exclude_dresses = False
        if exclude_skirts and exclude_pants and exclude_skirts:
            if dress_score > skirts_score:
                exclude_dresses = False
            else:
                exclude_skirts = False

        return (exclude_skirts, exclude_pants, exclude_dresses)

    def __init__(self, person: Person = None):
        if not isinstance(person, Person):
            self.exclude_skirts = False
            self.exclude_pants = False
            self.exclude_dresses = False
            self.lingerie = False
            self.no_lingerie = False
            self.skimpy_outfits = False
            self.skimpy_uniforms = False
            self.conservative_outfits = False
            self.show_tits = False
            self.no_show_tits = False
            self.show_ass = False
            self.no_show_ass = False
            self.no_underwear = False
            self.prefer_boots = False
            self.no_boots = False
            self.prefer_high_heels = False
            self.no_high_heels = False
            self.no_clothes = False
            self.prefer_clothes = False
            return

        self.exclude_skirts, self.exclude_pants, self.exclude_dresses = WardrobePreference.get_skirt_dress_and_pants_preference(person)
        self.lingerie = person.opinion.lingerie > 0
        self.no_lingerie = person.opinion.lingerie < 0
        self.skimpy_outfits = person.opinion.skimpy_outfits > person.opinion.conservative_outfits
        self.skimpy_uniforms = person.opinion.skimpy_uniforms > person.opinion.conservative_outfits
        self.conservative_outfits = person.opinion.conservative_outfits > person.opinion.skimpy_outfits
        self.show_tits = person.opinion.showing_her_tits > 0
        self.no_show_tits = person.opinion.showing_her_tits < 0
        self.show_ass = person.opinion.showing_her_ass > 0
        self.no_show_ass = person.opinion.showing_her_ass < 0
        self.no_underwear = person.opinion.not_wearing_underwear > 0 and person.opinion.lingerie < person.opinion.not_wearing_underwear
        self.prefer_boots = person.opinion.boots > 0
        self.no_boots = person.opinion.boots < 0
        self.prefer_high_heels = person.opinion.high_heels > 0
        self.no_high_heels = person.opinion.high_heels < 0
        self.no_clothes = person.opinion.not_wearing_anything > 0
        self.prefer_clothes = person.opinion.not_wearing_anything < 0
        self.slut_modifier = person.opinion.conservative_outfits * 2

        # skimpy preference overrides conservative outfit choice
        if (self.skimpy_outfits or self.skimpy_uniforms):
            self.conservative_outfits = False

        #renpy.say(None, "Person: " + person.name + "  " + person.last_name)
        # renpy.say(None,  person.name + "  " + person.last_name + ": " + (self.exclude_skirts and "no skirts, " or "") + (self.exclude_pants and "no pants, " or "") + (self.lingerie and "lingerie, " or "")
        #       + (self.skimpy_outfits and "skimpy outfits, " or "") + (self.conservative_outfits and "conservative outfits, " or "")
        #       + (self.prefer_boots and "boots, " or "") + (self.no_boots and "no boots, " or "") + (self.prefer_high_heels and "high heels, " or "") + (self.no_high_heels and "no heels, " or ""))

    def evaluate_outfit(self, outfit: Outfit, sluttiness_limit, sluttiness_min = 0) -> bool:
        is_overwear = outfit.is_suitable_overwear_set
        slut_score = is_overwear and outfit.overwear_slut_score or outfit.outfit_slut_score

        if slut_score > sluttiness_limit or slut_score < sluttiness_min:
            #print("Outfit: {} is out of sluttiness range".format(outfit.name))
            return False
        if not self.no_clothes and (outfit.vagina_available or outfit.tits_available):
            return False
        if self.no_clothes and not (outfit.vagina_available or outfit.tits_available):
            return False
        if outfit.vagina_visible and not mc.business.nudity_is_legal:
            #print("Outfit: {} has too many clothing items".format(outfit.name))
            return False
        if outfit.tits_visible and not mc.business.topless_is_legal:
            return False
        if self.prefer_clothes and (outfit.vagina_available or outfit.tits_available):
            #print("Outfit: {} has not enough clothing items".format(outfit.name))
            return False
        if self.exclude_skirts and outfit.has_skirt:
            #print("Outfit: {} has a skirt".format(outfit.name))
            return False
        if self.exclude_dresses and outfit.has_dress:
            #print("Outfit: {} has a dress".format(outfit.name))
            return False
        if self.exclude_pants and outfit.has_pants:
            #print("Outfit: {} has a pants".format(outfit.name))
            return False
        if (self.show_tits and any(outfit.has_clothing(item) for item in WardrobePreference.hide_tits_list)) or (self.no_show_tits and not any(outfit.has_clothing(item) for item in WardrobePreference.hide_tits_list)):
            #print("Outfit: {} hides tits".format(outfit.name))
            return False
        if (self.show_ass and any(outfit.has_clothing(item) for item in WardrobePreference.hide_ass_list)) or (self.no_show_ass and not any(outfit.has_clothing(item) for item in WardrobePreference.hide_ass_list)):
            #print("Outfit: {} hides ass".format(outfit.name))
            return False
        if (self.prefer_high_heels and not outfit.has_high_heels) or (self.no_high_heels and outfit.has_high_heels):
            #print("Outfit: {} has no heels".format(outfit.name))
            return False
        if (self.prefer_boots and not outfit.has_boots) or (self.no_boots and outfit.has_boots):
            #print("Outfit: {} has no boots".format(outfit.name))
            return False

        # checks differ when overwear or full outfit
        if is_overwear:
            if self.conservative_outfits and (slut_score > (sluttiness_limit // 2 + self.slut_modifier) or (outfit.tits_available or outfit.vagina_available or not outfit.bra_covered or not outfit.panties_covered)):
                return False
            if (self.skimpy_outfits or self.skimpy_uniforms) and slut_score < (sluttiness_limit // 4 + self.slut_modifier):
                return False
        else:
            if self.conservative_outfits and (slut_score > (sluttiness_limit // 2 + self.slut_modifier) or (not outfit.wearing_panties or not outfit.bra_covered or not outfit.panties_covered)):
                #print("Outfit: {} is too slutty".format(outfit.name))
                return False
            if (self.skimpy_outfits or self.skimpy_uniforms) and slut_score < (sluttiness_limit // 4 + self.slut_modifier):
                #print("Outfit: {} not slutty enough".format(outfit.name))
                return False

        #renpy.say(None, "Add: " + outfit.name)
        return True

    def evaluate_outfit_get_return(self, outfit: Outfit, sluttiness_limit: int, sluttiness_min = 0): #A copy of the previous method but returns what is wrong with an outfit instead of False
        is_overwear = outfit.is_suitable_overwear_set
        slut_score = is_overwear and outfit.overwear_slut_score or outfit.outfit_slut_score

        if slut_score > sluttiness_limit:
            return "is too slutty"
        if slut_score < sluttiness_min:
            return "is too conservative"

        if not self.no_clothes and (outfit.vagina_available or outfit.tits_available):
            return "leaves me too exposed"
        if self.no_clothes and not (outfit.vagina_available or outfit.tits_available):
            return "restricts access"
        if outfit.vagina_visible and not mc.business.nudity_is_legal:
            #print("Outfit: {} has too many clothing items".format(outfit.name))
            return "shows my vagina"
        if outfit.tits_visible and not mc.business.topless_is_legal:
            return "shows my tits"
        if self.prefer_clothes and (outfit.vagina_available or outfit.tits_available):
            return "is missing some parts"
        if self.exclude_skirts and outfit.has_skirt:
            return "has a skirt"
        if self.exclude_dresses and outfit.has_dress:
            return "is a dress"
        if self.exclude_pants and outfit.has_pants:
            return "has pants"
        if (self.show_tits and any(outfit.has_clothing(item) for item in WardrobePreference.hide_tits_list)):
            return "doesn't show my assets"
        if (self.no_show_tits and not any(outfit.has_clothing(item) for item in WardrobePreference.hide_tits_list)):
            return "shows too much"
        if (self.show_ass and any(outfit.has_clothing(item) for item in WardrobePreference.hide_ass_list)):
            return "doesn't show my bum"
        if (self.no_show_ass and not any(outfit.has_clothing(item) for item in WardrobePreference.hide_ass_list)):
            return "shows my bum"
        if (self.prefer_high_heels and not outfit.has_high_heels):
            return "doesn't have heels"
        if (self.no_high_heels and outfit.has_high_heels):
            return "has high heels"
        if (self.prefer_boots and not outfit.has_boots):
            return "doesn't have boots"
        if (self.no_boots and outfit.has_boots):
            return "has boots"

        # checks differ when overwear or full outfit
        if is_overwear:
            if self.conservative_outfits and (slut_score > (15 + self.slut_modifier) or (outfit.tits_available or outfit.vagina_available or not outfit.bra_covered or not outfit.panties_covered)):
                return "isn't conservative"
            if (self.skimpy_outfits or self.skimpy_uniforms) and not slut_score > (10 + self.slut_modifier) and (not outfit.tits_available or not outfit.vagina_available):
                return "is too conservative"
        else:
            if self.conservative_outfits and (slut_score > (10 + self.slut_modifier) or (not outfit.wearing_panties or not outfit.bra_covered or not outfit.panties_covered)):
                return "isn't conservative"
            if (self.skimpy_outfits or self.skimpy_uniforms) and not slut_score > (5 + self.slut_modifier):
                return "is too conservative"

        #renpy.say(None, "Add: " + outfit.name)
        return True

    def evaluate_underwear(self, underwear: Outfit, sluttiness_limit, sluttiness_min = 0) -> bool:
        slut_score = underwear.underwear_slut_score

        if not (slut_score <= sluttiness_limit and slut_score >= sluttiness_min):
            return False
        if (self.no_underwear and underwear.wearing_bra and underwear.wearing_panties) or (not self.no_underwear and not (underwear.wearing_bra or underwear.wearing_panties)):
            return False
        if self.lingerie and (underwear.has_low_socks or any(item.slut_value < 1 for item in underwear.lower_body) or any(item.slut_value < 1 for item in underwear.upper_body) or not underwear.wearing_panties):
            return False
        if (self.no_lingerie or self.conservative_outfits) and (underwear.has_thigh_high_socks or any(item.slut_value > 2 for item in underwear.lower_body) or any(item.slut_value > 2 for item in underwear.upper_body)):
            return False
        if (self.skimpy_outfits or self.skimpy_uniforms) and slut_score < 15:
            return False
        # no makeup check, default wardrobe has no underwear with makeup
        return True
