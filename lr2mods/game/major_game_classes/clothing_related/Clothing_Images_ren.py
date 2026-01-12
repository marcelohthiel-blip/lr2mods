from __future__ import annotations
from renpy.display.im import ImageBase
from renpy.rollback import NoRollback
from game._image_definitions_ren import empty_image
from game.major_game_classes.clothing_related.zip_manager_ren import ZipContainer

mobile_zip_dict = {}
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -20 python:
"""
class Clothing_Images(NoRollback): # Stores a set of images for a single piece of clothing in a single position. The position is stored when it is put into the clothing object dict.
    BREAST_SIZES = ("AA", "A", "B", "C", "D", "DD", "DDD", "E", "F", "FF")
    BODIES = ("standard_body", "thin_body", "curvy_body", "standard_preg_body")

    def __init__(self, clothing_name: str, position_name: str, is_top: bool, body_dependant = True):
        self.images = {}
        self.clothing_name = clothing_name #Used for some debugging, not needed for the actual game logic.
        self.position_name = position_name #Used so we can access the correct .zip file

        for body in Clothing_Images.BODIES if body_dependant else ["standard_body"]:
            for breast in Clothing_Images.BREAST_SIZES if is_top else ["AA"]:
                if clothing_name:
                    image_name = f"{clothing_name}_{position_name}_{body}_{breast}.png"
                    self.images[f"{body}_{breast}"] = image_name

    def get_image(self, body_type: str, breast_size = "AA") -> ImageBase: #Generates a proper Image object from the file path strings we have stored previously. Prevents object bloat by storing large objects repeatedly for everyone.
        global mobile_zip_dict

        index_string = f"{body_type}_{breast_size}"
        if index_string in self.images and self.images[index_string] in mobile_zip_dict[self.position_name].namelist():
            return ZipContainer(self.position_name, self.images[index_string])

        if self.clothing_name: # check if we have a mod image for the clothing item
            file_name = f"{self.clothing_name}_{self.position_name}_{body_type}_{breast_size}.png"
            if file_name in mobile_zip_dict["character_images"].namelist():
                return ZipContainer("character_images", file_name)
        return empty_image

    def get_image_name(self, body_type, breast_size = "AA") -> str: #Generates a proper Image object from the file path strings we have stored previously. Prevents object bloat by storing large objects repeatedly for everyone.
        index_string = f"{body_type}_{breast_size}"
        if index_string in self.images:
            return self.images[index_string]
        return "empty_holder.png"

class Facial_Accessory_Images(NoRollback):
    supported_faces = ("Face_1", "Face_2", "Face_3", "Face_4", "Face_5", "Face_6", "Face_7", "Face_8", "Face_9", "Face_11", "Face_12", "Face_13", "Face_14")
    supported_emotions = ("default", "sad", "happy", "angry", "orgasm")

    def __init__(self, accessory_name: str, position: str):
        self.images = {}
        self.position_name = position
        self.special_modifiers = {self.position_name: "blowjob", "kissing": "kissing"} #As of v0.35 all positions support the blowjob modifier so we can have good-looking gags and a wider variety of facial expressions.

        for face in Facial_Accessory_Images.supported_faces:
            for emotion in Facial_Accessory_Images.supported_emotions:
                self.images[f"{face}_{emotion}"] = f"{accessory_name}_{position}_{face}_{emotion}.png" # Save the file string so we can generate a proper image from it easily later.
                if position in self.special_modifiers:
                    self.images[f"{face}_{emotion}_{self.special_modifiers[position]}"] = f"{accessory_name}_{position}_{face}_{emotion}_{self.special_modifiers[position]}.png"

    def get_image(self, face: str, emotion: str, special_modifier: str | None = None) -> ImageBase:
        global mobile_zip_dict
        index_string = f"{face}_{emotion}"
        if special_modifier:
            if self.images[f"{index_string}_{special_modifier}"] in mobile_zip_dict[self.position_name].namelist():
                return ZipContainer(self.position_name, self.images[f"{index_string}_{special_modifier}"])

        if self.images[index_string] in mobile_zip_dict[self.position_name].namelist():
            return ZipContainer(self.position_name, self.images[index_string])

        # check if we have a mod image for the clothing item
        if self.images[index_string] in mobile_zip_dict["character_images"].namelist():
            return ZipContainer("character_images", self.images[index_string])

        return empty_image

    def get_image_name(self, face: str, emotion: str, special_modifier: str | None = None) -> str:
        global mobile_zip_dict
        file = mobile_zip_dict[self.position_name]
        index_string = f"{face}_{emotion}"
        if special_modifier is not None and f"{index_string}_{special_modifier}" in file.namelist():
            index_string += f"_{special_modifier}"  #We only want to try and load special modifier images if they exist. Otherwise we use the unmodified image to avoid a crash. This lets us omit images we do not plan on actually using, such as glasses not needing blowjob poses.

        return self.images[index_string]
