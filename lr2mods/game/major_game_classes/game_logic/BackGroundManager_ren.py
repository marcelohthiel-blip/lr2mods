import renpy
from renpy.rollback import NoRollback
from renpy.display.im import Image
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -99 python:
"""
import os

class BackGroundManager(NoRollback):
    bg_list: dict[str, Image] = {}

    def __init__(self):
        self.load("images/background_images")

    def load(self, path: str):
        '''
        Load all images from path as background images
        When calling method again, images with same filename will be changed
        '''
        for bg in (x for x in renpy.exports.list_files() if path in x):
            # extract filename without extension
            name = os.path.splitext(os.path.basename(bg))[0]
            BackGroundManager.bg_list[name] = Image(bg)

    def background(self, name: str) -> Image:
        '''
        Retrieve background image by name -> filename without extension
        '''
        return BackGroundManager.bg_list[name]

bg_manager = BackGroundManager()
