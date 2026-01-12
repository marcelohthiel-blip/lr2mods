from __future__ import annotations
import copy
import renpy
from renpy.display import im
from renpy.defaultstore import AlphaBlend, Composite, Solid
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.clothing_offsets_ren import master_clothing_offset_dict
from game.clothing_lists_ren import position_size_dict, pumps, high_heels, leggings, pinafore, two_part_dress, thin_dress, nightgown_dress, thigh_high_boots, micro_skirt, daisy_dukes, jean_hotpants, all_regions, wet_nipple_region, chandelier_earings, gold_earings, modern_glasses, big_glasses, sunglasses, secret_mask, leotard, garter_with_fishnets, forearm_gloves
from game.major_game_classes.clothing_related.zip_manager_ren import supported_positions
from game.major_game_classes.clothing_related.Clothing_Images_ren import Clothing_Images
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder, real_dress_list, real_bra_list, one_piece_list, panties_list, socks_list, skirts_list, pants_list, shoes_list, boots_list, high_heels_list, shirts_list, low_socks_list, thigh_high_sock_list, bracelet_list, neckwear_list, always_uses_pattern, nightgown_list, tights_list, makeup_list, glasses_list

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -15 python:
"""
from functools import cached_property

class Clothing():
    _pattern_sets: dict[str, dict[str, Clothing_Images]] = {}
    _position_sets: dict[str, dict[str, Clothing_Images]] = {}

    @property
    def pattern_sets(self) -> dict[str, Clothing_Images]:
        if self.proper_name not in Clothing._pattern_sets:
            Clothing._pattern_sets[self.proper_name] = {}
        return Clothing._pattern_sets[self.proper_name]

    @property
    def position_sets(self) -> dict[str, Clothing_Images]:
        if self.proper_name not in Clothing._position_sets:
            Clothing._position_sets[self.proper_name] = {}
        return Clothing._position_sets[self.proper_name]

    @property
    def crop_offset_dict(self) -> dict[str, tuple[int, int]]:
        return master_clothing_offset_dict.get(self.proper_name, {})

    _half_off_regions: dict[str, list[Clothing]] = {}

    @property
    def half_off_regions(self) -> list[Clothing]:
        if not self.proper_name or self.proper_name not in Clothing._half_off_regions:
            return []
        return Clothing._half_off_regions[self.proper_name]

    @half_off_regions.setter
    def half_off_regions(self, value: list[Clothing]):
        Clothing._half_off_regions[self.proper_name] = value

    _half_off_ignore_regions: dict[str, list[Clothing]] = {}

    @property
    def half_off_ignore_regions(self) -> list[Clothing]:
        if not self.proper_name or self.proper_name not in Clothing._half_off_ignore_regions:
            return []
        return Clothing._half_off_ignore_regions[self.proper_name]

    @half_off_ignore_regions.setter
    def half_off_ignore_regions(self, value: list[Clothing]):
        Clothing._half_off_ignore_regions[self.proper_name] = value

    _constrain_regions: dict[str, list[Clothing]] = {}

    @property
    def constrain_regions(self) -> list[Clothing]:
        if not self.proper_name or self.proper_name not in Clothing._constrain_regions:
            return []
        return Clothing._constrain_regions[self.proper_name]

    @constrain_regions.setter
    def constrain_regions(self, value: list[Clothing]):
        Clothing._constrain_regions[self.proper_name] = value

    def __init__(self, name: str, layer: int, hide_below: bool, anchor_below: bool, proper_name: str, draws_breasts: bool, underwear: bool, slut_value: int,
            has_extension: Clothing = None, is_extension = False, colour: list[float] = None, tucked = False, body_dependant = True,
            opacity_adjustment = 1, whiteness_adjustment = 0.0, contrast_adjustment = 1.0, supported_patterns: dict[str, str] = None, default_pattern: str = None, colour_pattern: list[float] = None,
            ordering_variable = 0, display_name: str = None, can_be_half_off = False, half_off_regions: list[Clothing] = None,
            half_off_ignore_regions: list[Clothing] = None, half_off_gives_access = False, half_off_reveals = False, constrain_regions: list[Clothing] = None):
        self.name = name
        self.proper_name = proper_name #The true name used in the file system
        if display_name is None:
            self.display_name = self.name
        else:
            self.display_name = display_name #The name that should be used any time the item is talked about in a more general sense (ie. "she takes off her panties" instead of "she takes of her cute lace panties")

        self.hide_below = hide_below #If true, it hides the clothing beneath so you can't tell what's on.
        self.anchor_below = anchor_below #If true, you must take this off before you can take off anything of a lower layer.
        self.layer = layer #A list of the slots above that this should take up or otherwise prevent from being filled. Slots are a list of the slot and the layer.

        if supported_patterns is None:
            self.supported_patterns = {"Default": None}
        else:
            self.supported_patterns = supported_patterns
            self.supported_patterns["Default"] = None

        for pos in supported_positions:
            self.position_sets[pos] = Clothing_Images(proper_name, pos, draws_breasts, body_dependant = body_dependant)
            if supported_patterns and proper_name is not None:
                for the_pattern in supported_patterns:
                    pattern_name = supported_patterns[the_pattern]
                    if pattern_name:
                        self.pattern_sets[f"{pos}_{pattern_name}"] = Clothing_Images(f"{proper_name}_{pattern_name}", pos, draws_breasts, body_dependant = body_dependant)

        # self.crop_offset_dict = master_clothing_offset_dict.get(self.proper_name, {}) # All of the offsets are stored in a single array and distributed. Saves time having to manually change values any time a clothing item render is updated.

        self.draws_breasts = draws_breasts
        self.underwear = underwear #True if the item of clothing satisfies the desire for underwear for upper or lower (bra or panties), false if it can pass as outerwear. Underwear on outside of outfit gives higher slut requirement.
        self.slut_value = slut_value #The amount of sluttiness that this piece of clothing adds to an outfit.
        self.has_extension = has_extension #If the item of clothing spans two zones (say, lower and feet or upper and lower body) has_extension points towards the placeholder item that fills the other part.
        self.is_extension = is_extension #If this is true the clothing item exists only as a placeholder. It will draw nothing and not be removed unless the main piece is removed.
        if not colour:
            self.colour = [1.0, 1.0, 1.0, 1.0]
        else:
            self.colour = colour
        self.tucked = tucked #Items of clothing that are tucked are drawn a "half level", aka we cycle thorugh all layer 2's and do untucked items, then do all tucked items.

        self.body_dependant = body_dependant #Items that are not body dependant are always draw as if they are on a standard body, ideal for facial accessories that do not vary with emotion like earrings.

        self.whiteness_adjustment = whiteness_adjustment #A modifier applied to the greyscale version of a piece of clothing to bring it closer to a white piece of clothing instead of grey. Default is 0, ranges from -1 to 1.
        self.contrast_adjustment = contrast_adjustment #Changes the contrast, good for getting proper whites and blacks after changing whiteness. Default is 1.0, 0.0 is min contrast, >1 is increasing contrast
        self.opacity_adjustment = opacity_adjustment #An opacity modifier applied to the piece of clothing before any other modifiers are considered (including colour). A value >1 makes slightly transparent clothing opaque, perfect for fixing imperfect renders.

        self.pattern = default_pattern #If not none this should be a string that will let us find the proper pattern mask.
        if not colour_pattern:
            self.colour_pattern = [1.0, 1.0, 1.0, 1.0]
        else:
            self.colour_pattern = colour_pattern #If there is a pattern assigned this is the colour used for the masked section.

        self.ordering_variable = ordering_variable #Used for things like hair and pubes when we need to know what can be trimmed into what without any time taken.
        self.half_off = False
        self.can_be_half_off = can_be_half_off
        #If True the piece of clothing does not block accessability for tits or vagina
        self.half_off_gives_access = half_off_gives_access
        #If True a piece of clothing does not block visability for anything underneath it when half off.
        self.half_off_reveals = half_off_reveals

        if half_off_regions is None: #A list of body region "clothing items". When self.half_off is True these regions are hidden.
            self.half_off_regions = []
        elif isinstance(half_off_regions, list):
            self.half_off_regions = half_off_regions
        else:
            self.half_off_regions = [half_off_regions]

        if half_off_ignore_regions is None: #A list of region "clothing items" that are added _back_ onto an item when half off. These use no blur, so can preserve sharp edges where, for example, arms interact with a torso.
            self.half_off_ignore_regions = []
        elif isinstance(half_off_ignore_regions, list):
            self.half_off_ignore_regions = half_off_ignore_regions
        else:
            self.half_off_ignore_regions = [half_off_ignore_regions]

        if constrain_regions is None: #an area of the body that other clothing items are "constrained" to if this item is worn over top.
            self.constrain_regions = []
        elif isinstance(constrain_regions, list):
            self.constrain_regions = constrain_regions
        else:
            self.constrain_regions = [constrain_regions]

    @property
    def identifier(self) -> int:
        return self.__hash__()

    @cached_property
    def colour_adjustment(self) -> im.matrix:
        brightness_matrix = im.matrix.brightness(self.whiteness_adjustment)
        contrast_matrix = im.matrix.contrast(self.contrast_adjustment)
        opacity_matrix = im.matrix.opacity(self.opacity_adjustment)

        return opacity_matrix * brightness_matrix * contrast_matrix

    def __hash__(self) -> int:      # need a hash and equality for current state (draw routines)
        return generate_identifier(
            (self.name, self.half_off, self.pattern) +
            tuple(self.colour) +
            tuple(self.colour_pattern))

    def __eq__(self, other: Clothing) -> bool:
        if not isinstance(other, Clothing):
            return NotImplemented

        return (self.name, self.half_off, self.pattern, self.colour, self.colour_pattern) == \
            (other.name, other.half_off, other.pattern, other.colour, other.colour_pattern)

    def is_similar(self, other: Clothing) -> bool: #Checks that two pieces of clothing are similar. ie. their base clothing item is the same, even if pattern or colour differs.
        if not isinstance(other, Clothing):
            return False

        return (self.name, self.hide_below, self.layer, self.is_extension) == \
            (other.name, other.hide_below, other.layer, other.is_extension)

    def get_copy(self) -> Clothing: #Returns a copy of the piece of clothing with the correct underlying references.
        return_copy = copy.copy(self)
        if self.has_extension:
            return_copy.has_extension = self.has_extension.get_copy() # Extensions need to be coppied a layer down, since they can store extra information.
        return return_copy

    @property
    def transparency(self) -> float:
        return self.colour[3]

    @transparency.setter
    def transparency(self, value: float):
        self.colour[3] = value

    @property
    def pattern_transparency(self) -> float:
        if self.pattern is None:
            return 1.0
        return self.colour_pattern[3]

    @pattern_transparency.setter
    def pattern_transparency(self, value: float):
        if self.pattern is None:
            return
        self.colour_pattern[3] = value

    @property
    def layers(self) -> tuple[int, ...]:
        if self.has_extension:
            return (self.layer, self.has_extension.layer)
        return (self.layer, )

    @cached_property
    def is_dress(self) -> bool:
        return any(x for x in real_dress_list if x.is_similar(self))

    @cached_property
    def is_bra(self) -> bool:
        return any(x for x in real_bra_list if x.is_similar(self))

    @cached_property
    def is_one_piece(self) -> bool:
        '''
        Clothing items with bottom and top part that are not dresses
        '''
        return any(x for x in one_piece_list if x.is_similar(self))

    @cached_property
    def is_panties(self) -> bool:
        return any(x for x in panties_list if x.is_similar(self))

    @cached_property
    def is_socks(self) -> bool:
        return any(x for x in socks_list if x.is_similar(self))

    @cached_property
    def is_skirt(self) -> bool:
        return any(x for x in skirts_list if x.is_similar(self))

    @cached_property
    def is_shoes(self) -> bool:
        return any(x for x in shoes_list if x.is_similar(self))

    @cached_property
    def is_boots(self) -> bool:
        return any(x for x in boots_list if x.is_similar(self))

    @cached_property
    def is_high_heels(self) -> bool:
        return any(x for x in high_heels_list if x.is_similar(self))

    @cached_property
    def is_shirt(self) -> bool:
        return any(x for x in shirts_list if x.is_similar(self))

    @cached_property
    def is_pants(self) -> bool:
        return any(x for x in pants_list if x.is_similar(self))

    @cached_property
    def is_low_sock(self) -> bool:
        return any(x for x in low_socks_list if x.is_similar(self))

    @cached_property
    def is_thigh_high_sock(self) -> bool:
        return any(x for x in thigh_high_sock_list if x.is_similar(self))

    @cached_property
    def is_tights(self) -> bool:
        return any(x for x in tights_list if x.is_similar(self))

    @cached_property
    def is_bracelet(self) -> bool:
        return any(x for x in bracelet_list if x.is_similar(self))

    @cached_property
    def is_neckwear(self) -> bool:
        return any(x for x in neckwear_list if x.is_similar(self))

    @cached_property
    def is_leotard(self) -> bool:
        '''
        Clothing items where bottom half is underwear and top part is overwear
        '''
        return any(x for x in (leotard, ) if x.is_similar(self))

    @cached_property
    def is_garterbelt(self) -> bool:
        '''
        Socks that have a garter belt (is drawn below panties)
        '''
        return any(x for x in (garter_with_fishnets, ) if x.is_similar(self))

    @cached_property
    def is_gloves(self) -> bool:
        '''
        Clothing items that cover hands / wrists (draw below bracelets)
        '''
        return any(x for x in (forearm_gloves, ) if x.is_similar(self))

    @cached_property
    def is_nightgown(self) -> bool:
        return any(x for x in nightgown_list if x.is_similar(self))

    @cached_property
    def is_makeup(self) -> bool:
        return any(x for x in makeup_list if x.is_similar(self))

    @cached_property
    def is_earring(self) -> bool:
        return any(x for x in (chandelier_earings, gold_earings) if x.is_similar(self))

    @cached_property
    def is_glasses(self) -> bool:
        return any(x for x in (modern_glasses, big_glasses, sunglasses) if x.is_similar(self))

    @cached_property
    def is_mask(self) -> bool:
        return any(x for x in (secret_mask, ) if x.is_similar(self))

    @cached_property
    def always_use_pattern(self) -> bool:
        return any(x for x in always_uses_pattern if x.is_similar(self))

    @cached_property
    def slut_score(self) -> int:
        new_score = self.slut_value
        if WardrobeBuilder.clothing_in_preferences("skimpy outfits", self):
            new_score += 1
        # if WardrobeBuilder.clothing_in_preferences("conservative outfits", self):
        #     new_score -= 3
        if WardrobeBuilder.clothing_in_preferences("showing her tits", self):
            new_score += 1
        if WardrobeBuilder.clothing_in_preferences("showing her ass", self):
            new_score += 1
        if WardrobeBuilder.clothing_in_preferences("lingerie", self):
            new_score += 1
        if WardrobeBuilder.clothing_in_preferences("high heels", self):
            new_score += 1
        if any(x for x in (pumps, high_heels, leggings) if x.is_similar(self)):
            new_score += 2 # small extra modifier
        if any(x for x in (pinafore, two_part_dress, thin_dress, nightgown_dress, thigh_high_boots, micro_skirt, daisy_dukes, jean_hotpants) if x.is_similar(self)):
            new_score += 4 # extremely slutty clothing (applies extra modifier)
        return new_score if new_score > 0 else 0

    def generate_raw_image(self, body_type: str, tit_size: str, position: str) -> im.ImageBase: #Returns the raw ZipFileImage or Image, instead of the displayable (used for generating region masks)
        if not self.body_dependant:
            body_type = "standard_body"
        if position in self.position_sets:
            image_set = self.position_sets[position]
        else:
            image_set = self.position_sets["stand3"]

        return image_set.get_image(body_type, tit_size if self.draws_breasts else "AA")

    def generate_item_displayable(self, body_type: str, tit_size: str, position: str, lighting: list[float] | None = None, regions_constrained: list[Clothing] | None = None, nipple_wetness = 0.0) -> renpy.display.core.Displayable:
        def _build_composite(items: list[Clothing], body_type, tit_size, position) -> tuple[im.ImageBase, list]:
            composite_list = [position_size_dict.get(position, (0, 0))]
            for item in items:
                region_mask = item.generate_raw_image(body_type, tit_size, position)
                composite_list.extend([item.crop_offset_dict.get(position, (0, 0)), region_mask])

            return im.Composite(*composite_list), composite_list

        if self.is_extension:
            return None

        if lighting is None:
            lighting = [.98, .98, .98]

        if not self.body_dependant:
            body_type = "standard_body"

        image_set = self.position_sets.get(position, self.position_sets["stand3"])
        the_image = image_set.get_image(body_type, tit_size if self.draws_breasts else "AA")

        if regions_constrained is None:
            regions_constrained = []

        mask_image = None
        if self.pattern:
            pattern_set = self.pattern_sets.get(f"{position}_{self.pattern}")
            if not pattern_set:
                mask_image = None
            else:
                mask_image = pattern_set.get_image(body_type, tit_size if self.draws_breasts else "AA")

            if not mask_image:
                self.pattern = None

        #This is the base greyscale image we have
        greyscale_image = im.MatrixColor(the_image, self.colour_adjustment) #Set the image, which will crush all modifiers to 1 (so that future modifiers are applied to a flat image correctly with no unusually large images

        colour_matrix = im.matrix.tint(self.colour[0], self.colour[1], self.colour[2]) * im.matrix.tint(*lighting)
        alpha_matrix = im.matrix.opacity(self.transparency)
        shader_image = im.MatrixColor(greyscale_image, alpha_matrix * colour_matrix) #Now colour the final greyscale image

        if self.pattern:
            colour_pattern_matrix = im.matrix.tint(self.colour_pattern[0], self.colour_pattern[1], self.colour_pattern[2]) * im.matrix.tint(*lighting)
            pattern_alpha_matrix = im.matrix.opacity(self.pattern_transparency) #The opacity of the pattern is independent from the rest of the clothing.
            shader_pattern_image = im.MatrixColor(greyscale_image, pattern_alpha_matrix * colour_pattern_matrix)

            # mask_red_alpha_invert = im.MatrixColor(mask_image, [0,0,0,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,1]) #Inverts the pattern colour so the shader applies properly.

            final_image = AlphaBlend(mask_image, shader_image, shader_pattern_image, alpha=False)
        else:
            final_image = shader_image

        final_image = Composite(position_size_dict.get(position, (0, 0)), self.crop_offset_dict.get(position, (0, 0)), final_image) #Transform the clothing image into a composite with the image positioned correctly.
        # Images need to be put into a composite here so we can properly apply masks, which themselves need to be composited to apply correctly.

        if len(regions_constrained) > 0:
            # We want to support clothing "constraining", or masking, lower images. This is done by region.
            # Each constraining region effectively subtracts itself + a blurred border around it, and then the body region is added back in so it appears through clothing.

            composite, composite_list = _build_composite(regions_constrained, body_type, tit_size, position)
            blurred_composite = im.Blur(composite, 10) #Blur the combined region mask to make it wider than the original. This would start to incorrectly include the interior of the mask, but...
            constrained_region_mask = im.MatrixColor(blurred_composite, [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 10, 0]) #This is the area to be subtracted from the image.

            full_body_mask = all_regions.generate_raw_image(body_type, tit_size, position)
            composite_list.extend([all_regions.crop_offset_dict.get(position, (0, 0)), full_body_mask])
            full_body_comp = im.Composite(*composite_list) # This ensures all constrained regions are part of the body mask, enabling support for items like skirts w/ clothing between body parts.

            constrained_mask = AlphaBlend(constrained_region_mask, Solid("#FFFFFFFF"), full_body_comp) #This builds the proper final image mask (ie all shown, except for the region around but not including the constrained region)
            final_image = AlphaBlend(constrained_mask, Solid("#00000000"), final_image)

        if nipple_wetness > 0:
            region_mask = wet_nipple_region.generate_raw_image(body_type, tit_size, position)
            #region_mask = Image(wet_nipple_region.__generate_item_image_name(body_type, tit_size, position))
            position_size = position_size_dict.get(position, (0, 0))
            region_mask = im.MatrixColor(region_mask, [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, nipple_wetness, 0])
            region_composite = Composite(position_size, (0, 0), Solid("00000000", size = position_size), wet_nipple_region.crop_offset_dict.get(position, (0, 0)), region_mask)
            #print(str(position_size))
            final_image = AlphaBlend(region_composite, final_image, Solid("#00000000"))

        if self.half_off or (self.has_extension and self.has_extension.half_off):
            total_half_off_regions: set[Clothing] = set() #Check what all of the half-off regions should be
            total_half_off_ignore_regions: set[Clothing] = set() #Check what half-off regions should be ignored
            if self.half_off:
                total_half_off_regions.update(self.half_off_regions)
                total_half_off_ignore_regions.update(self.half_off_ignore_regions)
            if (self.has_extension and self.has_extension.half_off):
                total_half_off_regions.update(self.has_extension.half_off_regions)
                total_half_off_ignore_regions.update(self.has_extension.half_off_ignore_regions)

            # print(f"Half off regions {self.name} -> {'. '.join(x.name for x in total_half_off_regions)}")

            if total_half_off_regions:  # only build composite when we have regions
                composite, _ = _build_composite(total_half_off_regions, body_type, tit_size, position)
                blurred_composite = im.Blur(composite, 12) #Blur the combined region mask to make it wider than the original. This would start to incorrectly include the interior of the mask, but...
                transparency_control_image = im.MatrixColor(blurred_composite, [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 7, 0]) #...We increase the contribution of alpha from the mask, so a small amount ends up being 100% (this still preserves some gradient at the edge as well)

                if total_half_off_ignore_regions: #Sometimes you want hard edges, or a section of a piece of clothing not to be moved. These regions are not blurred/enlarged and are subtracted from the mask generated above.
                    composite, _ = _build_composite(total_half_off_ignore_regions, body_type, tit_size, position)
                    transparency_control_image = AlphaBlend(im.Blur(composite, 1.5), transparency_control_image, Solid("#00000000"), True) #This alpha blend effectively subtracts the half_off_ignore mask from the half_off region mask

                final_image = AlphaBlend(transparency_control_image, final_image, Solid("#00000000"), True) #Use the final mask to hide parts of the clothing image as appropriate.

        return final_image

    def update_colour(self, new_colour: list[float], preserve_alpha = True):
        item_colour = new_colour[:] if not preserve_alpha else [*new_colour[:3], self.colour[3]]

        self.colour = item_colour
        if self.has_extension:
            self.has_extension.colour = item_colour

    def update_pattern_colour(self, new_colour = list[float], preserve_alpha = True):
        if not self.pattern:
            return

        pattern_colour = new_colour[:] if not preserve_alpha else [*new_colour[:3], self.colour_pattern[3]]

        self.colour_pattern = pattern_colour
        if self.has_extension:
            self.has_extension.colour_pattern = pattern_colour
