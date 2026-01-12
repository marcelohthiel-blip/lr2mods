from __future__ import annotations
import renpy
from renpy.defaultstore import Composite
from renpy.display import im
from game.major_game_classes.clothing_related.Clothing_ren import Clothing, position_size_dict, master_clothing_offset_dict, supported_positions
from game.major_game_classes.clothing_related.Clothing_Images_ren import Facial_Accessory_Images

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -15 python:
"""
class Facial_Accessory(Clothing): #This class inherits from Clothing and is used for special accessories that require extra information
    _position_sets: dict[str, dict[str, Facial_Accessory_Images]] = {}

    @property
    def position_sets(self) -> dict[str, Facial_Accessory_Images]:
        if self.proper_name not in Facial_Accessory._position_sets:
            Facial_Accessory._position_sets[self.proper_name] = {}
        return Facial_Accessory._position_sets[self.proper_name]

    @property
    def crop_offset_dict(self):
        return master_clothing_offset_dict.get(self.proper_name, {})

    def __init__(self, name: str, layer: int, hide_below: bool, anchor_below: bool, proper_name: str, draws_breasts: bool, underwear, slut_value: int,
            has_extension: Clothing | None = None, is_extension = False, colour = None, tucked = False,
            opacity_adjustment = 1, whiteness_adjustment = 0.0, contrast_adjustment = 1.0, display_name = None, modifier_lock = None):

        super().__init__(name, layer, hide_below, anchor_below, proper_name, draws_breasts, underwear, slut_value, has_extension, is_extension, colour, tucked, False,
            opacity_adjustment, whiteness_adjustment, contrast_adjustment,
            display_name = display_name, can_be_half_off = False, half_off_reveals = None)

        for pos in supported_positions:
            self.position_sets[pos] = Facial_Accessory_Images(proper_name, pos)

        self.modifier_lock = modifier_lock #If set to something other than None this facial accessory adds the modifier to all positions if possible.

    def generate_item_displayable(self, position: str, face_type: str, emotion: str, special_modifiers = None, lighting: list[float] | None = None) -> renpy.display.core.Displayable:
        if self.is_extension:
            return None

        if lighting is None:
            lighting = [.98, .98, .98]

        image_set = self.position_sets.get(position, self.position_sets["stand3"])
        the_image = image_set.get_image(face_type, emotion, special_modifiers) or image_set.get_image(face_type, emotion)

        greyscale_image = im.MatrixColor(the_image, self.colour_adjustment) #Set the image, which will crush all modifiers to 1 (so that future modifiers are applied to a flat image correctly with no unusually large images

        colour_matrix = im.matrix.tint(self.colour[0], self.colour[1], self.colour[2]) * im.matrix.tint(*lighting)
        alpha_matrix = im.matrix.opacity(self.colour[3])
        shader_image = im.MatrixColor(greyscale_image, alpha_matrix * colour_matrix) #Now colour the final greyscale image

        return Composite(position_size_dict[position], self.crop_offset_dict.get(position, (0, 0)), shader_image)

    def generate_raw_image(self, position, face_type, emotion, special_modifier):
        image_set = self.position_sets[position]
        if image_set is None:
            image_set = self.position_sets["stand3"] #Get a default image set if we are looking at a position we do not have.

        the_image = image_set.get_image(face_type, emotion, special_modifier)
        if not the_image:
            the_image = image_set.get_image(face_type, emotion) # If we weren't able to get something with the special modifier just use a default to prevent a crash.

        return the_image
