############################################################
# MOD Implementation of ZIP file loading and image caching #
############################################################
from __future__ import annotations
import renpy
from renpy import persistent
from renpy.rollback import NoRollback
from game.bugfix_additions.debug_info_ren import write_log
from game.clothing_lists_ren import white_skin, black_skin, tan_skin, hair_styles, breast_region, butt_region, all_regions, torso_region, stomach_region, pelvis_region, upper_arm_region, upper_leg_region, lower_arm_region, lower_leg_region, foot_region, hand_region, skirt_region, wet_nipple_region, vagina_region
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.Expression_ren import Expression
from game.major_game_classes.clothing_related.Clothing_Images_ren import Clothing_Images
from game._image_definitions_ren import get_file_handle

emotion_images_dict: dict[str, dict[str, Expression]] = {}
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -99 python:
"""
from pylru import LRUCache # type: ignore
from threading import RLock
import time
import zipfile
import sys
import io
import threading

global is64Bit
is64Bit = sys.maxsize > 2**32

# all image sets available
global supported_positions
supported_positions = ["stand2", "stand3", "stand4", "stand5",
    "walking_away", "kissing", "doggy", "missionary", "blowjob",
    "against_wall", "back_peek", "sitting", "kneeling1", "standing_doggy", "cowgirl"]

# zipfile caching
global mobile_zip_dict
mobile_zip_dict = {}
for sup_pos in supported_positions:
    renpy_file = renpy.exports.file(f"images/character_images/{sup_pos}.zip")
    mobile_zip_dict[sup_pos] = zipfile.ZipFile(renpy_file, "r") #Cache all of the zip files so we have a single static pointer to them.

# add zip dictionary for MOD character images
mobile_zip_dict["character_images"] = zipfile.ZipFile(renpy.exports.file(get_file_handle("character_images.zip")), "r") #Cache all of the zip files so we have a single static pointer to them.

# special class for managing thread locks and cache objects for zipfile loading
class ZipManager(NoRollback):
    BODIES = ("standard_body", "thin_body", "curvy_body")
    SKINS = ("white", "tan", "black")

    def __init__(self):
        self.Locks = {}
        self.Cache = {}
        if is64Bit:
            self.max_items = 1200 if persistent.zip_cache_size == 0 else 2500
        else:
            self.max_items = 300 if persistent.zip_cache_size == 0 else 500

        for x in supported_positions + ["character_images"]:
            self.Locks[x] = RLock()
            self.Cache[x] = LRUCache(self.max_items)    # most used character images per position

    def preload(self):  # load main character images into the zip file cache
        while not hasattr(renpy.context(), "_main_menu"):
            time.sleep(.2)
        while not renpy.context()._main_menu:
            time.sleep(.2)

        load_functions = [self.load_main_character_images, self.load_hair_styles, self.load_masking_areas, self.load_emotions]

        try:
            for func in load_functions:
                t = threading.Thread(target = func)
                t.daemon = True
                t.start()
        except Exception as e:
            write_log(f"ZipManager preload error: {e}")

    def load_main_character_images(self):
        for cloth, pos in ((i, j) for i in (white_skin, black_skin, tan_skin) for j in supported_positions):
            for body in ZipManager.BODIES if cloth.body_dependant else ("standard_body"):
                for tits in Clothing_Images.BREAST_SIZES if cloth.draws_breasts else ("AA"):
                    if file := cloth.position_sets[pos].get_image(body, tits):
                        file.load()

    def load_hair_styles(self):
        for cloth, pos in ((i, j) for i in hair_styles for j in supported_positions):
            for body in ZipManager.BODIES if cloth.body_dependant else ("standard_body"):
                for tits in Clothing_Images.BREAST_SIZES if cloth.draws_breasts else ("AA"):
                    if file := cloth.position_sets[pos].get_image(body, tits):
                        file.load()

    def load_masking_areas(self):
        for cloth, pos in ((i, j) for i in (breast_region, butt_region, all_regions, torso_region, stomach_region, pelvis_region, upper_arm_region, upper_leg_region, lower_arm_region, lower_leg_region, foot_region, hand_region, skirt_region, wet_nipple_region, vagina_region) for j in supported_positions):
            for body in ZipManager.BODIES if cloth.body_dependant else ("standard_body"):
                for tits in Clothing_Images.BREAST_SIZES if cloth.draws_breasts else ("AA"):
                    if file := cloth.position_sets[pos].get_image(body, tits):
                        file.load()

    def load_emotions(self):
        for skin, face in ((i, j) for i in ZipManager.SKINS for j in Person._list_of_faces):
            exp = emotion_images_dict[skin][face]
            for pos, emotion in ((i, j) for i in supported_positions for j in Expression.emotion_set):
                if file := exp.generate_raw_image(pos, emotion):
                    file.load()

    @property
    def size(self) -> int:
        return sum(len(x) for x in self.Cache.values())

    @property
    def byte_size(self) -> int:
        return sum(x.byte_size for x in self.Cache.values())

    def utilization(self) -> float:
        # result = {}
        # for k, v in self.Cache.iteritems():
        #     result[k] = []
        #     result[k].append(v.size())
        #     result[k].append(v.size() * 100.0 / float(self.max_items))
        # return result
        return (self.size * 100.0 / (self.max_items * float(len(self.Cache))))

class ZipContainer(NoRollback, renpy.display.im.ImageBase):
    def __init__(self, position, filename, mtime=0, **properties):
        super().__init__(position, filename, mtime, **properties)
        self.position = position
        self.filename = filename

    def __repr__(self):
        return self.filename

    def load(self):
        try:
            with zip_manager.Locks[self.position]:
                if self.filename not in zip_manager.Cache[self.position]:
                    global mobile_zip_dict
                    zip_manager.Cache[self.position][self.filename] = mobile_zip_dict[self.position].read(self.filename)

                sio = io.BytesIO(zip_manager.Cache[self.position][self.filename])
                return renpy.display.pgrender.load_image(sio, self.filename)
        except Exception:
            return renpy.display.pgrender.surface((2, 2), True)    # same object als the Renpy image zip returns https://github.com/renpy/renpy/blob/master/renpy/display/im.py

zip_manager = ZipManager()

if persistent.zip_cache_preload:
    # start background thread for pre-loading zip cache
    background_thread = threading.Thread(target=zip_manager.preload)
    background_thread.daemon = True
    background_thread.start()
