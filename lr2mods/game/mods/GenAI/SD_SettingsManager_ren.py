# Ren'Py integration for SD Settings Manager.
# This file provides Ren'Py-compatible functions to replace persistent usage.

"""renpy
init 4 python:
"""
import json
import os

# Global settings manager instance
sd_settings_manager = None

def init_sd_settings():
    global sd_settings_manager
    if sd_settings_manager is None:
        sd_settings_manager = SDSettingsManager()
    return sd_settings_manager

# =============================================================================
# SETTINGS MANAGER CLASS
# Handles loading, saving, and managing settings.
# =============================================================================
class SDSettingsManager:
    def __init__(self, settings_file_path="game/Mods/GenAI/sd_settings.json"):
        self.settings_file_path = settings_file_path
        self.settings = {}
        self._load_settings()
    
    def _get_default_settings(self):
        return {
            "sd_selected_model": None,
            "sd_selected_sampler": "Euler",
            "sd_steps_value": 20,
            "sd_cfg_scale_value": 7.0,
            "sd_upscaling_enabled": False,
            "sd_upscaling_size": 1.75,
            "sd_selected_upscaler": "SwinIR_4x",
            "sd_width_value": 512,
            "sd_height_value": 768,
            "sd_adetailer_enabled": False,
            "sd_selected_adetailer": "face_yolov8n.pt",
            "sd_selected_prompt": "default",
            "sd_selected_scheduler": "automatic",
            "sd_global_positive_prepend": "",
            "sd_global_negative_prepend": "",
            "sd_img2img_enabled": False,
            "sd_denoising_strength": 0.5,
            "sd_json_correction": False,
            "sd_adetailer_model": None,
            "sd_latent_enabled": False,
            "sd_noise_strength": 25,     
            "sd_noise_type": "add"            
        }
    
    # Load settings from JSON or create with defaults if not found.
    def _load_settings(self):
        try:
            if os.path.exists(self.settings_file_path):
                with open(self.settings_file_path, 'r', encoding='utf-8') as f:
                    loaded_settings = json.load(f)
                    self.settings = self._get_default_settings()
                    self.settings.update(loaded_settings)
            else:
                self.settings = self._get_default_settings()
                self._save_settings()
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.settings = self._get_default_settings()
            self._save_settings()
    
    def _save_settings(self):
        try:
            with open(self.settings_file_path, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def get_setting(self, key, default=None):
        return self.settings.get(key, default)
    
    def set_setting(self, key, value):
        self.settings[key] = value
        self._save_settings()
    
    def get_all_settings(self):
        return self.settings.copy()
    
    def reset_to_defaults(self):
        self.settings = self._get_default_settings()
        self._save_settings()
    
    def apply_to_persistent(self, persistent):
        for key, value in self.settings.items():
            setattr(persistent, key, value)
        
        print("Settings applied to persistent object.")

# =============================================================================
# PUBLIC INTERFACE FUNCTIONS
# =============================================================================
def sd_get_setting(key, default=None):
    global sd_settings_manager
    if sd_settings_manager is None:
        init_sd_settings()
    return sd_settings_manager.get_setting(key, default)

def sd_set_setting(key, value):
    global sd_settings_manager
    if sd_settings_manager is None:
        init_sd_settings()
    sd_settings_manager.set_setting(key, value)

def sd_get_all_settings():
    global sd_settings_manager
    if sd_settings_manager is None:
        init_sd_settings()
    return sd_settings_manager.get_all_settings()

def sd_reset_settings():
    global sd_settings_manager
    if sd_settings_manager is None:
        init_sd_settings()
    sd_settings_manager.reset_to_defaults()

# =============================================================================
# PROMPT MANAGEMENT FUNCTIONS
# =============================================================================

# Load prompt data from the prompts directory by name.
# Returns the full prompt data dictionary or None if not found.
def sd_get_prompt_data_by_name(prompt_name):
    try:
        from inspect import getsourcefile
        from os.path import dirname
        import json
        
        # Get the prompts directory path.
        folder_name = dirname(getsourcefile(lambda:0))+'/prompts'

        # Format the prompt name to replace spaces with underscores.
        formatted_prompt_name = prompt_name.replace(" ", "_")
        
        # Try to load the specific prompt file.
        # First try to load the file with the same name as the prompt name,
        # if this is the case there is no need to read all the available prompt sets.
        prompt_file = os.path.join(folder_name, f'{formatted_prompt_name}.json')
        if os.path.exists(prompt_file):
            with open(prompt_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # If not found, search through all available prompt sets.
        # This is a fallback for when the file structure is different.
        available_prompt_sets = sd_get_available_prompt_sets()
        for prompt_set in available_prompt_sets:
            if prompt_set.get('Name') == prompt_name:
                return prompt_set
                
        return None
    except Exception as e:
        print(f"Error loading prompt data for '{prompt_name}': {e}")
        return None

# Load all available prompt sets from the prompts directory.
# Returns a list of prompt data dictionaries.
def sd_get_available_prompt_sets():
    try:
        from inspect import getsourcefile
        from os.path import dirname
        import json
        
        folder_name = dirname(getsourcefile(lambda:0))+'/prompts'
        json_data = []
        defaultdata = []

        # Load default.json first.
        default_file = os.path.join(folder_name, 'default.json')
        if os.path.exists(default_file):
            with open(default_file, 'r', encoding='utf-8') as f:
                try:
                    defaultdata = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"Error loading default.json: {e}")

        # Load all JSON files in the prompts directory.
        for filename in os.listdir(folder_name):
            if filename.endswith('.json'):
                filepath = os.path.join(folder_name, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        if data['Name'] != "default" and sd_get_setting("sd_json_correction", True):
                            # Merge with default data if correction is enabled.
                            sd_merge_json_dict(data, defaultdata, data["Name"])
                        json_data.append(data)
                    except json.JSONDecodeError as e:
                        print(f"Error loading json file {filename}: {e}")

        return json_data
    except Exception as e:
        print(f"Error loading available prompt sets: {e}")
        return []

# Helper function to merge JSON dictionaries.
def sd_merge_json_dict(target, src, name):
    for k in src:
        if (k in target) and (type(src[k]) != type(target[k])):
            print(f"JSON type mismatch for {name}")
            continue
        if str(type(src[k])) == "<class 'dict'>":
            if not k in target:
                target[k] = dict()
            sd_merge_json_dict(target[k], src[k], name)
        elif str(type(src[k])) == "<class 'list'>":
            if k in target:
                continue
            target[k] = list()
            # NOTE: This is a simplified merge for lists.
            target[k].extend(src[k])
        else:
            if not (k in target):
                target[k] = src[k]