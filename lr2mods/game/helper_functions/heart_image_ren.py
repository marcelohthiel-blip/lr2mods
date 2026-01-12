# this class can generate a heart image based on their respective base images
from __future__ import annotations
import renpy
import pygame_sdl2 # type: ignore
from renpy.rollback import NoRollback
from game._image_definitions_ren import get_file_handle

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""
class HeartImage(NoRollback, renpy.display.im.ImageBase):
    images: dict[str, str] = {
        "empty_heart.png": get_file_handle("gui/heart/empty_heart.png"),
        "red_heart.png": get_file_handle("gui/heart/red_heart.png"),
        "grey_heart.png": get_file_handle("gui/heart/grey_heart.png"),
        "gold_heart.png": get_file_handle("gui/heart/gold_heart.png"),
    }

    def __init__(self, name, background, foreground, value = 0, secondary_foreground = None, secondary_value = 0, max_value = 20.0, **properties):
        super().__init__(name, **properties)
        self.name = name
        self.background = background
        self.foreground = foreground
        self.secondary_foreground = secondary_foreground
        self.value = value
        self.secondary_value = secondary_value
        self.max_value = max_value

    def _repr_info(self):
        return repr(self.name)

    def get_hash(self):
        return renpy.loader.get_hash(self.name)

    def load(self):
        filename = renpy.loader.load(HeartImage.images[self.background], directory="images")
        surface = renpy.display.pgrender.load_image(filename, self.background)
        size = surface.get_size()
        image = pygame_sdl2.Surface(size, pygame_sdl2.SRCALPHA)
        image.blit(surface, (0, 0))

        width = size[0] * min(self.value / self.max_value, 1)
        filename2 = renpy.loader.load(HeartImage.images[self.foreground], directory="images")
        surface2 = renpy.display.pgrender.load_image(filename2, self.foreground)
        image.blit(surface2.subsurface(0, 0, width, size[1]), (0, 0))

        if self.secondary_foreground:
            secondary_width = size[0] * min(self.secondary_value / self.max_value, 1)
            filename3 = renpy.loader.load(HeartImage.images[self.secondary_foreground], directory="images")
            surface3 = renpy.display.pgrender.load_image(filename3, self.secondary_foreground)
            image.blit(surface3.subsurface(width, 0, secondary_width, size[1]), (width, 0))

        return image

    def predict_files(self):
        return self.name
