import renpy

from game.major_game_classes.character_related.Person_ren import Person, list_of_instantiation_functions
from game.helper_functions.character_display_functions_ren import clear_scene
from game.Mods.GenAI.SD_PromptBuilder_ren import sd_get_prompts, sd_get_style_prompt
from game.Mods.GenAI.SD_SettingsManager_ren import sd_get_setting
from game.clothing_lists_ren import position_size_dict

"""renpy
init -1 python:
"""
import random
import zlib
import os
import requests
import json
import base64
import pprint

# =================================================================================
# INITIALIZATION
# =================================================================================

# Initialize store variable for save game data.
if not hasattr(store, 'sd_saved_person_data'):
    store.sd_saved_person_data = ""
if not hasattr(store, 'sd_prompt_style'):
    store.sd_prompt_style = ""

# Add SDClient to instantiation functions.
list_of_instantiation_functions.append("MakeSDClient")

# =============================================================================
# CLIENT INSTANTIATION
# =============================================================================

def MakeSDClient():
    global sdClient
    if not 'sdClient' in globals() or sdClient is None:
        sdClient = SDClient()
    # Ensure currentPerson is set before image operations.
    if sdClient.currentPerson is None and getattr(store, "last_active_person", None):
        sdClient.currentPerson = store.last_active_person

# =============================================================================
# DATA CLASSES
# =============================================================================

# Stores image data for a single state of a person.
class StateImageData(object):

    def __init__(self):
        self.image = None
        self.imagePath = ""
        self.filePath = ""
        self.prompt = ""

# Stores all image and prompt data for a person.
class PersonImageData(object):

    def __init__(self):
        self.personIdentifier = 0
        self.stateImages = []
        self.currentIndex = 0
        self.seed = 0
        self.positivePromptOverride = False
        self.positiveCustomPrompt = ""
        self.positiveAppendedPrompt = ""
        self.negativePromptOverride = False
        self.negativeCustomPrompt = ""
        self.negativeAppendedPrompt = ""
        self._nameOverridePrompt = ""
        
    @property
    def nameOverridePrompt(self):
        # Safe fallback for old saves
        if not hasattr(self, '_nameOverridePrompt') or self._nameOverridePrompt is None:
            return ""
        return self._nameOverridePrompt  
        
    @nameOverridePrompt.setter
    def nameOverridePrompt(self, value):
        self._nameOverridePrompt = value    

# =============================================================================
# MAIN SDCLIENT CLASS
# Handles Stable Diffusion integration, prompt configuration and image generation.
# =============================================================================

class SDClient(object):

    def __init__(self):
        self.currentPerson = None
        self.currentPersonIdentifer = 0
        self.currentPosition = None
        self.jsonSavedPersonImageData = ""
        self.savedPersonsImageData = []
        self.currentImagePath = ""
        self.customPromptStyle = "full body portrait, d780 80mm lens, photorealistic, black background"
        self.autoGenerate = False
        self.sd_generation_in_progress = False
        self.sd_was_generating = False
        self.port = "7860"

    # -------------------------------------------------------------------------
    # CORE DISPLAY METHODS
    # -------------------------------------------------------------------------

    # Override draw person so that goes through SD instead of the default Ren'Py drawing.
    def draw_person_SD(self, position: str = "default", emotion: str = None, special_modifier: str = None, show_person_info = True, lighting = None,
        draw_layer = "solo", display_transform = None, display_zorder: int = 0, wipe_scene = True):
        global sdClient
        sdClient.draw_person_SD_Local(self, position, emotion, special_modifier, show_person_info, lighting, draw_layer, display_transform, display_zorder, wipe_scene)

    Person.draw_person = draw_person_SD

    # Override draw_animated_removal to use SD instead.
    def draw_animated_removal_SD(self, clothing: Clothing, position: str = "default", emotion: str = None, special_modifier: str = None, lighting: list[float] = None, show_person_info = True,
            half_off_instead = False, draw_layer = "solo", display_transform = None, display_zorder: int = 0, wipe_scene = True, scene_manager: Scene = None):

        if clothing.can_be_half_off and half_off_instead:
            self.outfit.half_off_clothing(clothing)  # Half-off the clothing
        else:
            self.outfit.remove_clothing(clothing)  # Remove the clothing

        global sdClient
        sdClient.draw_person_SD_Local(self, position, emotion, special_modifier, show_person_info, lighting, draw_layer, display_transform, display_zorder, wipe_scene)

    Person.draw_animated_removal = draw_animated_removal_SD

    # Override draw_quick_removal to use SD instead.
    def draw_quick_removal_SD(self, clothing: Clothing, position: str = "default", emotion: str = None, special_modifier: str = None, lighting: list[float] = None, show_person_info = True,
            half_off_instead = False, draw_layer = "solo", display_transform = None, display_zorder: int = 0, wipe_scene = True, scene_manager: Scene = None):

        if clothing.can_be_half_off and half_off_instead:
            self.outfit.half_off_clothing(clothing)  # Half-off the clothing
        else:
            self.outfit.remove_clothing(clothing)  # Remove the clothing

        global sdClient
        sdClient.draw_person_SD_Local(self, position, emotion, special_modifier, show_person_info, lighting, draw_layer, display_transform, display_zorder, wipe_scene)

    Person.draw_quick_removal = draw_quick_removal_SD

    # Override draw_quick_addition to add clothing using SD.
    def draw_quick_addition_SD(self, clothing: Clothing, position: str = "default", emotion: str = None, special_modifier: str = None, lighting: list[float] = None,
            draw_layer = "solo", display_transform = None, display_zorder: int = 0, add_function = None):

        if not isinstance(clothing, list):  # Convert clothing to list, if not already.
            clothing = [clothing]

        for cloth in clothing:
            add_function(cloth)

        global sdClient
        sdClient.draw_person_SD_Local(self, position, emotion, special_modifier, True, lighting, draw_layer, display_transform, display_zorder, True)

    Person.draw_quick_addition = draw_quick_addition_SD

    # Override quick_draw_slide_back to redraw slide clothing back using SD.
    def quick_draw_slide_back_SD(self, clothing: Clothing, position: str = "default", emotion: str = None, special_modifier: str = None, lighting: list[float] = None,
            draw_layer = "solo", display_transform = None, display_zorder: int = 0):

        if not isinstance(clothing, list):  # Convert clothing to list, if not already.
            clothing: list[Clothing] = [clothing]

        for cloth in clothing:
            cloth.half_off = False

        global sdClient
        sdClient.draw_person_SD_Local(self, position, emotion, special_modifier, True, lighting, draw_layer, display_transform, display_zorder, True)

    Person.quick_draw_slide_back = quick_draw_slide_back_SD

    # Hides character from the screen.
    def hide_person_SD(self):
        global sdClient
        sdClient.hide_person_SD_Local()

    Person.hide_person = hide_person_SD

    # Handles display logic of SD rendered persons.
    def draw_person_SD_Local(self, person:Person, position: str = "default", emotion: str = None, special_modifier: str = None, show_person_info = True, lighting = None,
        draw_layer = "solo", display_transform = None, display_zorder: int = 0, wipe_scene = True, scene_manager: Scene = None):

        if position == "default" or position is None:
            position = person.idle_pose

        if emotion is None:
            emotion = person.get_emotion()

        if display_transform is None:
            display_transform = character_right

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        image = person.build_person_displayable(position, emotion, special_modifier, lighting, cache_item=False)
        
        backgroundcolor = "#008000"; # leaving black if we don't try to remove it, might be easier to replace for stable diffusion than a solid purple?
        if persistent.sd_removebackground_enabled:
            backgroundcolor = "#008000";

        
#        newimage = Composite(position_size_dict.get(position), 
#            (0,0), Solid(person.get_display_colour_code()),
#            (0,0),image)
        newimage = Composite(position_size_dict.get(position), 
            (0,0), Solid(backgroundcolor),
            (0,0),image)
    
        renpy.render_to_file(newimage, "img2imgsrc.png", int(sd_get_setting('sd_width_value', 512)), int(sd_get_setting('sd_height_value', 768)), 0.0, None, True)


        #clear_scene()
        if wipe_scene:
            clear_scene() #Make sure no other characters are drawn either.
            
        if scene_manager is None:
            if show_person_info:
                renpy.show_screen("person_info_ui", person)
        else:   # when we are called from the scene manager we have to draw the other characters
            scene_manager.draw_scene(exclude_list = [person])            

        self.currentPerson = person
        self.currentPersonIdentifer = person.identifier
        self.currentPosition = position
        if not self.autoGenerate:
            renpy.show_screen("SD_update_button")
        renpy.show_screen("sd_event_handler")
        
        self.show_current_image(updateIndex=True)
        print("shown person " + self.currentPerson.title)

    # Clear current image display and reset person tracking.
    def hide_person_SD_Local(self):
        clear_scene()
        self.currentPerson = None
        self.currentPersonIdentifer = 0
        renpy.hide_screen("SD_update_button")
        renpy.hide_screen("genAI_image")
        renpy.hide_screen("sd_event_handler")
        renpy.hide_screen("generating_indicator")
        print("hidden person")

    # -------------------------------------------------------------------------
    # IMAGE DATA SAVE/LOAD METHODS
    # -------------------------------------------------------------------------

    # Save image data into JSON format and store it in the current game save.
    def save_persons_image_data_json(self):
        listSavedPersonImageData = []
        for personImageData in self.savedPersonsImageData:
            listStateImagesDatas = []
            for stateImageData in personImageData.stateImages:
                listStateImagesDatas.append({
                        "imagePath":stateImageData.imagePath,
                        "filePath":stateImageData.filePath,
                        "prompt":stateImageData.prompt})
            listSavedPersonImageData.append({
                    "personIdentifier":personImageData.personIdentifier,
                    "stateImages":listStateImagesDatas,
                    "currentIndex":personImageData.currentIndex,
                    "seed":personImageData.seed,
                    "positivePromptOverride":personImageData.positivePromptOverride,
                    "positiveCustomPrompt":personImageData.positiveCustomPrompt,
                    "positiveAppendedPrompt":personImageData.positiveAppendedPrompt,
                    "negativePromptOverride":personImageData.negativePromptOverride,
                    "negativeCustomPrompt":personImageData.negativeCustomPrompt,
                    "negativeAppendedPrompt":personImageData.negativeAppendedPrompt,
                    "nameOverridePrompt":personImageData.nameOverridePrompt})
        json_data = json.dumps(listSavedPersonImageData)
        # Store in the current save game's store instead of persistent.
        store.sd_saved_person_data = json_data
        store.sd_prompt_style = self.customPromptStyle
        store.sd_auto_generate = self.autoGenerate
        # Also keep in memory for immediate use.
        self.jsonSavedPersonImageData = json_data
        # print("saving " + self.jsonSavedPersonImageData)

    # Load image data from Renpy store into memory.
    def load_persons_image_data_json(self):
        try:
            # Try to load from store instead of persistent.
            if hasattr(store, 'sd_saved_person_data') and store.sd_saved_person_data:
                self.jsonSavedPersonImageData = store.sd_saved_person_data
            if hasattr(store, 'sd_prompt_style'):
                self.customPromptStyle = store.sd_prompt_style
            if hasattr(store, 'sd_auto_generate'):
                self.autoGenerate = store.sd_auto_generate

            if not self.jsonSavedPersonImageData:
                print("No saved data found")
                return

            listSavedPersonImageData = json.loads(self.jsonSavedPersonImageData)
            self.savedPersonsImageData = []  # Clear existing data before loading.

            for data_element in listSavedPersonImageData:
                try:
                    personImageData = PersonImageData()
                    # Use get() to handle missing keys gracefully.
                    personImageData.personIdentifier = data_element.get("personIdentifier", 0)
                    personImageData.currentIndex = data_element.get("currentIndex", 0)
                    personImageData.seed = data_element.get("seed", 0)
                    personImageData.positivePromptOverride = data_element.get("positivePromptOverride", False)
                    personImageData.positiveCustomPrompt = data_element.get("positiveCustomPrompt", "")
                    personImageData.positiveAppendedPrompt = data_element.get("positiveAppendedPrompt", "")
                    personImageData.negativePromptOverride = data_element.get("negativePromptOverride", False)
                    personImageData.negativeCustomPrompt = data_element.get("negativeCustomPrompt", "")
                    personImageData.negativeAppendedPrompt = data_element.get("negativeAppendedPrompt", "")
                    personImageData.nameOverridePrompt = data_element.get("nameOverridePrompt", "")

                    # Validate image files exist.
                    for stateImageElement in data_element.get("stateImages", []):
                        stateImageData = StateImageData()
                        stateImageData.imagePath = stateImageElement.get("imagePath", "")
                        stateImageData.filePath = stateImageElement.get("filePath", "")

                        # Only add if the image file still exists.
                        if os.path.exists(stateImageData.filePath):
                            stateImageData.prompt = stateImageElement.get("prompt", "")
                            personImageData.stateImages.append(stateImageData)

                    if personImageData.stateImages:  # Only add if it has valid images.
                        self.savedPersonsImageData.append(personImageData)

                except Exception as e:
                    print(f"Error loading person data: {e}")
                    continue

        except Exception as e:
            print(f"Error loading saved data: {e}")
            self.jsonSavedPersonImageData = ""
            self.savedPersonsImageData = []

    # Validate if saved person image data is loaded and contains valid entries.
    def validate_saved_person_image_data(self):
        if len(self.savedPersonsImageData) == 0:
            self.load_persons_image_data_json()
            if len(self.savedPersonsImageData) == 0:
                return False
        return True

    # -------------------------------------------------------------------------
    # PROMPT UTILITIES METHODS
    # -------------------------------------------------------------------------

    def _prepend_global_prompt(self, base_prompt: str, global_prepend: str) -> str:
        if global_prepend:
            return ", ".join([global_prepend, base_prompt])
        else:
            return base_prompt

    def get_positive_prompt(self):
        
        return self._prepend_global_prompt(sd_get_prompts()[0], sd_get_setting('sd_global_positive_prepend', ''))

    def get_negative_prompt(self):
        return self._prepend_global_prompt(sd_get_prompts()[1], sd_get_setting('sd_global_negative_prepend', ''))

    def get_style_prompt(self):
        return sd_get_style_prompt()

    def toggle_positive_prompt_override(self):
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None:
            return
        if not personImageData.positivePromptOverride:
            personImageData.positiveCustomPrompt = self.get_positive_prompt()
        else:
            personImageData.positiveCustomPrompt = ""
        personImageData.positivePromptOverride = not personImageData.positivePromptOverride
        self.save_persons_image_data_json()

    def set_positive_custom_prompt(self, prompt: str):
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None:
            return
        personImageData.positiveCustomPrompt = prompt
        self.save_persons_image_data_json()

    def set_positive_appended_prompt(self, prompt: str):
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None:
            return
        personImageData.positiveAppendedPrompt = prompt
        self.save_persons_image_data_json()

    def toggle_negative_prompt_override(self):
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None:
            return
        if not personImageData.negativePromptOverride:
            personImageData.negativeCustomPrompt = self.get_negative_prompt()
        else:
            personImageData.negativeCustomPrompt = ""
        personImageData.negativePromptOverride = not personImageData.negativePromptOverride
        self.save_persons_image_data_json()

    def set_negative_custom_prompt(self, prompt: str):
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None:
            return
        personImageData.negativeCustomPrompt = prompt
        self.save_persons_image_data_json()

    def set_negative_appended_prompt(self, prompt: str):
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None:
            return
        personImageData.negativeAppendedPrompt = prompt
        self.save_persons_image_data_json()

    def set_custom_prompt_style(self, style: str):
        self.customPromptStyle = style
        self.save_persons_image_data_json()

    # Toggle auto-generation of images and hide the UI if enabled.
    def toggle_auto_generate(self):
        self.autoGenerate = not self.autoGenerate
        if self.autoGenerate:
            renpy.hide_screen("SD_update_button")
        else:
            renpy.show_screen("SD_update_button")
        self.save_persons_image_data_json()

    # Update the index of current image if the current prompt matches the saved state.
    def update_index(self, personImageData:PersonImageData):
        if personImageData == None or not self.validate_saved_person_image_data() or len(personImageData.stateImages) == 0:
            return
        currentPrompt = self.get_positive_prompt()
        for index, stateImageData in enumerate(personImageData.stateImages):
            if stateImageData.prompt == currentPrompt:
                personImageData.currentIndex = index
                return
            
    # -------------------------------------------------------------------------
    # IMAGE DISPLAY/SWITCHING METHODS
    # -------------------------------------------------------------------------

    # Displays the current image using show_image for the person, or generates a new one if needed.
    def show_current_image(self, updateIndex:bool = True):
        if not self.validate_saved_person_image_data():
            if self.autoGenerate and not self.sd_generation_in_progress and not self.sd_was_generating:
                renpy.invoke_in_thread(self.add_new_image)
            return
        personImageData = self.get_person_image_data(makeNew=True)
        if personImageData is None or len(personImageData.stateImages) == 0:
            if self.autoGenerate and not self.sd_generation_in_progress and not self.sd_was_generating:
                renpy.invoke_in_thread(self.add_new_image)
            return
        if updateIndex:
            self.update_index(personImageData)
        stateImageData = self.get_current_state_image(personImageData)
        if stateImageData is None or not os.path.exists(stateImageData.filePath):
            if self.autoGenerate and not self.sd_generation_in_progress and not self.sd_was_generating:
                renpy.invoke_in_thread(self.add_new_image)
            return
        current_prompt = self.get_positive_prompt()
        if current_prompt != stateImageData.prompt and self.autoGenerate and not self.sd_generation_in_progress and not self.sd_was_generating:
            renpy.invoke_in_thread(self.add_new_image)

        self.show_image(stateImageData)

    # Displays the image on the screen.
    def show_image(self, stateImageData: StateImageData):
        if stateImageData.image == None:
            if os.path.exists(stateImageData.filePath):
                stateImageData.image = Image(stateImageData.imagePath)
            else:
                #renpy.hide("genAI")
                renpy.hide_screen("genAI_image")
                return

        self.currentImagePath = stateImageData.imagePath
        renpy.show_screen("genAI_image", stateImageData.imagePath)

    # Gets the image data for current person or creates a new one if needed.
    def get_person_image_data(self, makeNew:bool):
        if not makeNew and not self.validate_saved_person_image_data():
            return None
        person_saved_data = None
        # Only proceed if currentPerson exists.
        if self.currentPerson is None:
            if makeNew:
                raise ValueError("Cannot create new PersonImageData without active person")
            return None
        for savedPersonData in self.savedPersonsImageData:
            if savedPersonData.personIdentifier == self.currentPerson.identifier:
                person_saved_data = savedPersonData
                break
        if makeNew and person_saved_data == None:
            person_saved_data = PersonImageData()
            person_saved_data.personIdentifier = self.currentPerson.identifier
            person_saved_data.seed = self.generate_new_random_seed()
            self.savedPersonsImageData.append(person_saved_data)
            self.save_persons_image_data_json()
        return person_saved_data

    def get_current_state_image(self, personImageData:PersonImageData):
        if personImageData == None or len(personImageData.stateImages) == 0:
            return None
        if personImageData.currentIndex >= len(personImageData.stateImages):
            personImageData.currentIndex = 0
        return personImageData.stateImages[personImageData.currentIndex]

    def switch_to_previous_image(self):
        self.switch_image(False)

    def switch_to_next_image(self):
        self.switch_image(True)

    def switch_image(self, next:bool):
        person_saved_data:PersonImageData = self.get_person_image_data(makeNew=True)
        if person_saved_data == None or len(person_saved_data.stateImages) == 0:
            if person_saved_data == None:
                print("no person data " + self.currentPerson.title + " " + str(self.currentPersonIdentifer))
            else:
                print("no images")
            return
        if next:
            print("next " + self.currentPerson.title + " " + str(self.currentPersonIdentifer))
            person_saved_data.currentIndex += 1
            if person_saved_data.currentIndex >= len(person_saved_data.stateImages):
                person_saved_data.currentIndex = 0
        else:
            print("previous")
            person_saved_data.currentIndex -= 1
            if person_saved_data.currentIndex < 0:
                person_saved_data.currentIndex = len(person_saved_data.stateImages)-1

        self.show_current_image(updateIndex=False)

    # Adds a new image by triggering SD generation.
    def add_new_image(self):
        if self.currentPerson == None:
            #print("trying to get person by ident " + self.currentPersonIdentifer)
            self.currentPerson = Person.get_person_by_identifier(self.currentPersonIdentifer)
        print("new image " + self.currentPerson.title)
        self.sd_generate_action(False)

    def replace_current_image(self):
        if self.sd_generation_in_progress:
            return

        self.sd_generation_in_progress = True
        current_person_data = self.get_person_image_data(makeNew=True)
    
        if current_person_data is None:
            self.sd_generation_in_progress = False
            return

        #current_state_image = self.get_current_state_image(current_person_data)
        #if current_state_image is None:
        #    self.sd_generation_in_progress = False
        #    return

        self.sd_generate_action(True)

    def delete_current_image(self):
        print("delete image")
        personImageData:PersonImageData = self.get_person_image_data(makeNew=True)
        if personImageData == None or len(personImageData.stateImages) == 0:
            return
        current_state_image = self.get_current_state_image(personImageData)
        try:
            os.remove(current_state_image.filePath)
            print("deleted " + current_state_image.filePath)
        except OSError as error:
            print(f"Error deleting old image '{current_state_image.filePath}': {error}")
        personImageData.stateImages.remove(current_state_image)
        personImageData.currentIndex -= 1
        if personImageData.currentIndex < 0:
            personImageData.currentIndex = 0
        if len(personImageData.stateImages) == 0:
            renpy.hide_screen("genAI_image")
            #renpy.hide("genAI")
        else:
            self.show_current_image(updateIndex=False)



    def generate_new_random_seed(self):
        hash_string = str(random.randrange(1000,9999))
        return zlib.adler32(hash_string.encode("utf-8"))
    
    # -------------------------------------------------------------------------
    # IMAGE GENERATION LOGIC
    # -------------------------------------------------------------------------

    # Responsible for generating a new image using Stable Diffusion API by sending a request with the current prompts and settings.
    def sd_generate_action(self, replaceCurrent:bool):
        self.sd_generation_in_progress = True
        self.sd_was_generating = True

        base_positive, base_negative = sd_get_prompts()
        positive_prompt = self._prepend_global_prompt(base_positive, sd_get_setting('sd_global_positive_prepend', ''))
        negative_prompt = self._prepend_global_prompt(base_negative, sd_get_setting('sd_global_negative_prepend', ''))

        #seed = self.generate_new_random_seed()
        person_saved_data:PersonImageData = self.get_person_image_data(makeNew=True)
        if self.currentPerson is None:
            personName = str(person_saved_data.personIdentifier)
        else:
            personName = self.currentPerson.name

        seed = person_saved_data.seed

        upscaleEnabledString = "false"
        if sd_get_setting('sd_upscaling_enabled', False):
            upscaleEnabledString = "true"
        adetailerEnabledString = "false"
        if sd_get_setting('sd_adetailer_enabled', False):
            adetailerEnabledString = "true"
        if sd_get_setting('sd_selected_model') != None:
            model_name = self.get_current_model()
            if model_name != sd_get_setting('sd_selected_model'):
                self.set_model(sd_get_setting('sd_selected_model'))
                   

        headers = {'content-type': 'application/json'}
        payload = '{' + \
            '"prompt":"' + positive_prompt + '",' + \
            '"seed":' + str(seed) + ',' + \
            '"sampler_name":"' + sd_get_setting('sd_selected_sampler', 'Euler') + '",' + \
            '"scheduler":"' + sd_get_setting('sd_selected_scheduler', 'automatic') + '",' + \
            '"batch_size":1,' + \
            '"n_iter":1,' + \
            '"steps":' + str(sd_get_setting('sd_steps_value', 20)) + ',' + \
            '"cfg_scale":' + str(sd_get_setting('sd_cfg_scale_value', 7.0)) + ',' + \
            '"width":' + str(sd_get_setting('sd_width_value', 512)) + ',' + \
            '"height":' + str(sd_get_setting('sd_height_value', 768)) + ',' + \
            '"negative_prompt":"' + negative_prompt + '",' + \
            '"override_settings":{"always_discard_next_to_last_sigma":true,"CLIP_stop_at_last_layers":1},' + \
            '"override_settings_restore_afterwards":true'
        if sd_get_setting('sd_latent_enabled', False):
            payload = payload + \
            ',"alwayson_scripts": {' + \
            '"LatentModifier Integrated": {' + \
            '"args": [true, 0, "anisotropic", 0, "reinhard", 100, 0, "subtract", 0, 0, "pyramid",' +\
            '"' + str(sd_get_setting('sd_noise_type','add')) + '",' +\
              str(sd_get_setting('sd_noise_strength', 0)) + ',' +\
            '100, 127, 0, "hard_clamp", 5, 0, "None", "None"]}' + \
            '}'
            
            
        if sd_get_setting('sd_upscaling_enabled', False) and not sd_get_setting('sd_img2img_enabled', False):
            # Check if hr_additional_modules is valid before using it.
            if hasattr(self, 'hr_additional_modules') and isinstance(self.hr_additional_modules, (list, set)) and 'Use same choices' not in self.hr_additional_modules:
                payload = payload + \
                    ',"enable_hr":' + upscaleEnabledString + ',' + \
                    '"denoising_strength":0.3,' + \
                    '"firstphase_width":' + str(sd_get_setting('sd_width_value', 512)) + ',' + \
                    '"firstphase_height":' + str(sd_get_setting('sd_height_value', 768)) + ',' + \
                    '"hr_scale":"' + str(sd_get_setting('sd_upscaling_size', 1.75)) + '",' + \
                    '"hr_upscaler":"' + sd_get_setting('sd_selected_upscaler', 'SwinIR_4x') + '",' + \
                    '"hr_second_pass_steps":10,' + \
                    '"hr_sampler_name":"' + sd_get_setting('sd_selected_sampler', 'Euler') + '",' + \
                    '"hr_scheduler":"' + sd_get_setting('sd_selected_scheduler', 'automatic') + '",' + \
                    '"hr_prompt":"' + positive_prompt + '",' + \
                    '"hr_negative_prompt":"' + negative_prompt + '"'
                
        if sd_get_setting('sd_img2img_enabled', False):
            with open("img2imgsrc.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            payload = payload + \
                ',"init_images":["' + encoded_string + '"]' + \
                ',"denoising_strength":' + str(sd_get_setting('sd_denoising_strength', 0.5)) + \
                ',"resize_mode":2' 
                
        # if sd_get_setting('sd_latent_enabled', False):
            # payload = payload + \
                # ',"alwayson_scripts": {' + \
                # '"LatentModifier Integrated": {' + \
                # '"args": [ '+\
                # 'true, 0, "anisotropic", 0, "reinhard", 100, 0, "subtract", 0, 0, "pyramid",' + \
                # '' + str(sd_get_setting('sd_noise_type','add')) + ',' + \
                # '' + str(sd_get_setting('sd_noise_strength', 0)) + ',' + \
                # '100, 127, 0, "hard_clamp", 5, 0, "None", "None"]}' + \
                # '}'                
                
        if sd_get_setting('sd_adetailer_enabled', False):
            payload = payload + \
            ',"alwayson_scripts": {' + \
                '"ADetailer": {' + \
                    '"args": [' + \
                        adetailerEnabledString + ',' + \
                        "false" + ',' + \
                        '{' + \
                            '"ad_model": "' + sd_get_setting('sd_selected_adetailer', 'face_yolov8n.pt') + '",' + \
                            '"ad_model_classes": "",' + \
                            '"ad_tab_enable": true,' + \
                            '"ad_prompt": "",' + \
                            '"ad_negative_prompt": "",' + \
                            '"ad_confidence": 0.3,' + \
                            '"ad_mask_filter_method": "Area",' + \
                            '"ad_mask_k": 0,' + \
                            '"ad_mask_min_ratio": 0.0,' + \
                            '"ad_mask_max_ratio": 1.0,' + \
                            '"ad_dilate_erode": 4,' + \
                            '"ad_x_offset": 0,' + \
                            '"ad_y_offset": 0,' + \
                            '"ad_mask_merge_invert": "None",' + \
                            '"ad_mask_blur": 4,' + \
                            '"ad_denoising_strength": 0.4,' + \
                            '"ad_inpaint_only_masked": true,' + \
                            '"ad_inpaint_only_masked_padding": 32,' + \
                            '"ad_use_inpaint_width_height": false,' + \
                            '"ad_inpaint_width": 512,' + \
                            '"ad_inpaint_height": 512,' + \
                            '"ad_use_steps": false,' + \
                            '"ad_steps": 28,' + \
                            '"ad_use_cfg_scale": false,' + \
                            '"ad_cfg_scale": 7.0,' + \
                            '"ad_use_checkpoint": false,' + \
                            '"ad_checkpoint": null,' + \
                            '"ad_use_vae": false,' + \
                            '"ad_vae": null,' + \
                            '"ad_use_sampler": false,' + \
                            '"ad_sampler": "DPM++ 2M Karras",' + \
                            '"ad_scheduler": "Use same scheduler",' + \
                            '"ad_use_noise_multiplier": false,' + \
                            '"ad_noise_multiplier": 1.0,' + \
                            '"ad_use_clip_skip": false,' + \
                            '"ad_clip_skip": 1,' + \
                            '"ad_restore_face": false,' + \
                            '"ad_controlnet_model": "None",' + \
                            '"ad_controlnet_module": "None",' + \
                            '"ad_controlnet_weight": 1.0,' + \
                            '"ad_controlnet_guidance_start": 0.0,' + \
                            '"ad_controlnet_guidance_end": 1.0' + \
                        '}' + \
                    ']}' + \
                '}' + \
            '}'
        else:
            payload = payload + \
            '}'
        renpy.log(payload)
        
        if sd_get_setting('sd_img2img_enabled', False):
            apiurl = "http://127.0.0.1:" + self.port + "/sdapi/v1/img2img"
        else:
            apiurl = "http://127.0.0.1:" + self.port + "/sdapi/v1/txt2img"
        try:
            response = requests.post(apiurl, headers=headers, data=payload)

        except requests.exceptions.RequestException as e:
            print("error: ", e)
            self.show_connection_error()
            self.sd_generation_in_progress = False
            return

        #print("response: ", response.text)

        data = json.loads(response.text)
        image_data = data.get("images")
        if not image_data:
            print("No image data returned from SD API")
            self.sd_generation_in_progress = False
            renpy.log(data)
            return

        # Convert base64 image data string to bytes.
        image_bytes = base64.b64decode(str(image_data))

        # Create folder to store images (if doesn't exist already).
        folder_name = 'game/Mods/GenAI/generated_images'
        try:
            os.makedirs(folder_name, exist_ok=True)  # Creates the folder and any necessary parent directories.
            print(f"Folder '{folder_name}' created successfully.")
        except OSError as error:
            print(f"Error creating folder '{folder_name}': {error}")

        current_state_image:PersonImageData
        if replaceCurrent and len(person_saved_data.stateImages) != 0:
            current_state_image = self.get_current_state_image(person_saved_data)
            try:
                os.remove(current_state_image.filePath)
                print("deleted " + current_state_image.filePath)
            except OSError as error:
                print(f"Error deleting old image '{current_state_image.filePath}': {error}")
        else:
            current_state_image = StateImageData()
            person_saved_data.stateImages.append(current_state_image)
            person_saved_data.currentIndex = len(person_saved_data.stateImages)-1

        #print("Name: ", person_saved_data.personIdentifier, len(person_saved_data.stateImages), " prompt: ", positive_prompt)

        # Save image data
        #image_name = '{0}{1}.png'.format(self.currentPerson.name,self.generate_new_random_seed())
        image_name = f'{personName}{self.generate_new_random_seed()}.png'
        #prepath = 'game/Mods/GenAI/'
        # FULL OS path for saving .
        filePath = os.path.join(folder_name, image_name)  # ✅ Actual file path
        # Ren'Py path for display.
        imagePath = f"Mods/GenAI/generated_images/{image_name}"  # ✅ Ren'Py path (no Mods prefix needed)

        # Save image file.
        with open(filePath, 'wb') as f:
            f.write(image_bytes)

        newImage = Image(imagePath)
        current_state_image.image = newImage
        current_state_image.imagePath = imagePath
        current_state_image.filePath = filePath
        current_state_image.prompt = positive_prompt
        self.save_persons_image_data_json()

        self.sd_generation_in_progress = False

    # -------------------------------------------------------------------------
    # SD API COMMUNICATION METHODS
    # -------------------------------------------------------------------------

    def _make_get_request(self, url, headers):
        try:
            response = requests.get(url, headers=headers, timeout=1)
            return response.text
        except requests.exceptions.RequestException as e:
            print("error: ", e)
            self.show_connection_error()
            return None

    def show_connection_error(self):
        global have_connection
        have_connection = False
        renpy.hide_screen("SDConfig_menu")
        renpy.restart_interaction()
        renpy.show_screen("setup_info_box", title="Connection Error", description="Unable to connect to the Stable Diffusion API. Please make sure the API is running and try again.")

    def get_progress_text(self):
        try:
            # Make a web request to the local server to get the progress.
            response = requests.get("http://127.0.0.1:" + self.port + "/sdapi/v1/progress")
            if response.status_code == 200:
                data = json.loads(response.text)
                progress = round(data['progress']*100)
                return str(progress) + "%"
        except Exception as e:
            print(f"Error getting progress: {e}")
        return ""

    def get_available_models(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/sd-models", headers)
        if response_text:
            try:
                data = json.loads(response_text)
                return [model['title'] for model in data]
            except (KeyError, TypeError) as e:
                print(f"Error parsing model data: {e}")
                global have_connection
                have_connection = False
                renpy.hide_screen("SDConfig_menu")
                renpy.restart_interaction()
                renpy.show_screen("setup_info_box", title="API Error", description="Unable to parse model data from Stable Diffusion API. The API may be running an incompatible version.")
        return []

    def get_current_model(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/options", headers)
        if response_text:
            data = json.loads(response_text)
            return data['sd_model_checkpoint']
        return ""

    def set_model(self, model_name):
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post("http://127.0.0.1:" + self.port + "/sdapi/v1/options", headers=headers, data='{"sd_model_checkpoint":"'+model_name+'"}', timeout=3)
            print("response: ", response.text)
        except requests.exceptions.RequestException as e:
            print("error: ", e)

    def get_available_samplers(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/samplers", headers)
        if response_text:
            data = json.loads(response_text)
            return [sampler['name'] for sampler in data]
        return []

    def get_has_adetailer(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/script-info", headers)
        if response_text:
            data = json.loads(response_text)
            return any(script['name'] == 'adetailer' for script in data)
        return False

    def get_available_upscalers(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/upscalers", headers)
        if response_text:
            data = json.loads(response_text)
            return [upscaler['name'] for upscaler in data]
        return []

    def get_available_adetailers(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/adetailer/v1/ad_model", headers)
        if response_text:
            data = json.loads(response_text)
            return data["ad_model"]
        return []

    def get_available_schedulers(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/schedulers", headers)
        if response_text:
            data = json.loads(response_text)
            return [scheduler['name'] for scheduler in data]
        return []
    
    def get_available_loras(self):
        headers = {'content-type': 'application/json'}
        response_text = self._make_get_request("http://127.0.0.1:" + self.port + "/sdapi/v1/loras", headers)
        returnArray = []
        if response_text:
            try:
                data = json.loads(response_text)
                for loradict in data:
                    returnArray.append(loradict.get('name', ''))
                
            except (KeyError, TypeError, json.JSONDecodeError, IndexError) as e:
                print(f"Error parsing LoRA data: {e}")
                print(f"Raw response: {response_text}")
        return returnArray
        
        
# =============================================================================
# GLOBAL CLIENT INSTANTIATION
# =============================================================================

sdClient: SDClient

# Initialize sdClient if it doesn't exist.
if not 'sdClient' in globals():
    sdClient = SDClient()
