import builtins

from __future__ import annotations
from game.Mods.GenAI.SD_ColorConversion_ren import SD_get_color_opinion
from game.Mods.GenAI.SD_Cache_ren import SdPromptsCache, PersonPromptInputData
from game.Mods.GenAI.SD_SettingsManager_ren import sd_get_setting, sd_get_prompt_data_by_name
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from renpy.color import Color


time_of_day = 0

"""renpy
init -1 python:
"""

import random

# -----------------------------------------------------------------------------
# POSITION DATA CLASS
# Tracks visibility of body parts, defaults to True
# -----------------------------------------------------------------------------

class PositionData:

    def __init__(self):
        self.feet_visible = True
        self.legs_visible = True
        self.face_visible = True
        self.breasts_visible = True

# -----------------------------------------------------------------------------
# PROMPT BUILDER CLASS
# Assemblies the positive and negative prompts and gives final output
# -----------------------------------------------------------------------------

class PromptBuilder(object):

    def __init__(self):
        self.positive_prompt_parts = []
        self.negative_prompt_parts = []

    def append_positive(self, prompt_part: str) -> None:
        if prompt_part is not None and prompt_part != "":
            for single_part in prompt_part.split(", "):
                self.positive_prompt_parts.append(single_part)

    def get_positive(self) -> str:
        return ", ".join(self.positive_prompt_parts)

    def append_negative(self, prompt_part: str) -> None:
        if prompt_part is not None and prompt_part != "":
            self.negative_prompt_parts.append(prompt_part)

    def get_negative(self) -> str:
        return ", ".join(self.negative_prompt_parts)

    # Remove phrases from positive prompts that appear in negative prompts
    def clean_positives(self, negatives: list[str]) -> None:
        negative_set = set(negatives)
        self.positive_prompt_parts = filter(lambda p: p not in negative_set, self.positive_prompt_parts)

# -----------------------------------------------------------------------------
# MAIN PROMPT GENERATION FUNCTION
# Gets the prompts from specific prompt generators and returns positive and negative prompts
# Current order of prompts: style, position, face, eye color, expression, skin, age, hair, 
# outfit, breasts, body type, appended prompts.
# -----------------------------------------------------------------------------

def sd_get_prompts() -> tuple[str, str]:
    global sdClient
    global sdPromptCache
    person_image_data = sdClient.get_person_image_data(makeNew=True)
    if (person_image_data is not None
            and person_image_data.positivePromptOverride
            and person_image_data.negativePromptOverride):
        return (str(person_image_data.positiveCustomPrompt), str(person_image_data.negativePromptOverride))

    person = PersonPromptInputData(
        sdClient.currentPerson,
        sdClient.currentPosition,
        person_image_data.positiveAppendedPrompt,
        person_image_data.negativeAppendedPrompt
    )
    cache_key = person.to_cache_key()
    cached_prompt = sdPromptCache.get(cache_key, None)
    if cached_prompt is not None:
        positive_result = cached_prompt[0]
        negative_result = cached_prompt[1]
        return positive_result, negative_result

    prompt_name = sd_get_setting('sd_selected_prompt', 'default')
    settings_json = sd_get_prompt_data_by_name(prompt_name)
    if settings_json is None:
        # Fallback to default if the prompt data can't be loaded
        settings_json = sd_get_prompt_data_by_name('default') or {}

    # Initialize the prompt builder
    prompt_builder = PromptBuilder()
    #prompt_builder.append_positive(settings_json.get("positive_prompt_prefix", ""))
    prompt_builder.append_positive(sd_get_style_prompt())
    #prompt_builder.append_negative(settings_json.get("negative_prompt_prefix", ""))
    prompt_builder.append_negative(settings_json.get("negative_prompt", ""))
    
    if "location_prompt" in settings_json:
        sd_get_location_prompt(prompt_builder, person, settings_json.get("location_prompt", {}))    

    if "time_prompt" in settings_json:
        sd_fill_time_prompt(prompt_builder, settings_json.get("time_prompt", {}))
        

    if "position_prompt" in settings_json:
        position_data = sd_process_position_prompt(
            prompt_builder,
            person,
            settings_json.get("position_prompt", {})
        )
    else:
        position_data = PositionData()
    
    if position_data.face_visible:
        # face_prompt mapped to json
        if "face_prompt" in settings_json:
            sd_fill_face_prompt(prompt_builder, person, settings_json.get("face_prompt", {}))
        # eye_prompt mapped to json
        if "eye_prompt" in settings_json:
            sd_fill_eye_color_prompt(prompt_builder, person, settings_json.get("eye_prompt", {}))
        if "expression_prompt" in settings_json:
            sd_fill_expression_prompt(prompt_builder, person, settings_json.get("expression_prompt", {}))
    
    if "skin_prompt" in settings_json:
        sd_fill_skin_prompt(prompt_builder, person, settings_json.get("skin_prompt", {}))
    
    
    age_settings = settings_json.get("age_prompt", None)
    if age_settings is None:
        age_settings = {}
        pos = settings_json.get("age_prompt_pos", {})
        neg = settings_json.get("age_prompt_neg", {})
        for key in PersonPromptInputData.age_range_keys():
            age_settings[key] = {
                "pos": pos.get(key, ""),
                "neg": neg.get(key, "")
            }
    else:
        sd_fill_age_prompt(prompt_builder, person, age_settings)
        

    if "details_prompt" in settings_json:
        sd_fill_hair_prompt(prompt_builder, person, settings_json.get("details_prompt", {}))
    
    if "outfit_prompt" in settings_json:
        sd_fill_outfit_prompt(prompt_builder, person, position_data, settings_json.get("outfit_prompt", {}))
    
    if position_data.breasts_visible and "breasts_prompt" in settings_json:
        breasts_settings = settings_json.get("breasts_prompt", {})
        if isinstance(breasts_settings, builtins.list):
            breasts_settings = dict(zip(list(map(lambda x: x[0], Person.get_tit_weighted_list())), breasts_settings))
            sd_fill_breasts_prompt(prompt_builder, person, breasts_settings)
        else:
            sd_fill_breasts_prompt(prompt_builder, person, breasts_settings)
            
  
      
    if "height_prompt" in settings_json:
        sd_fill_height_prompt(prompt_builder, person, settings_json.get("height_prompt", {}))
    if "body_type_prompt" in settings_json:
        sd_fill_body_type_prompt(prompt_builder, person, settings_json.get("body_type_prompt", {}))    
    
    prompt_builder.append_positive(person_image_data.positiveAppendedPrompt)
    prompt_builder.append_negative(person_image_data.negativeAppendedPrompt)

    if person_image_data.negativePromptOverride:
        negative_result = str(person_image_data.negativePromptOverride)
    else:
        negative_result = prompt_builder.get_negative()
    if not person_image_data.positivePromptOverride:
        prompt_builder.clean_positives(negative_result.split(", "))
    if person_image_data.positivePromptOverride:
        positive_result = str(person_image_data.positivePromptOverride)
    else:
        positive_result = prompt_builder.get_positive()
    sdPromptCache[cache_key] = (positive_result, negative_result)
    return positive_result, negative_result

# -----------------------------------------------------------------------------
# PROMPT PROCESSING UTILITIES
# -----------------------------------------------------------------------------

def sd_process_prompt_value(prompt_builder: PromptBuilder, value: str, settings: {}) -> None:
    prompt_value = settings.get(value, None)
    if prompt_value is None:
        return
    if isinstance(prompt_value, str):
        prompt_builder.append_positive(prompt_value)
        return

    prompt_builder.append_positive(prompt_value.get("pos", ""))
    prompt_builder.append_negative(prompt_value.get("neg", ""))


def sd_process_substitution(prompt_builder: PromptBuilder, format_str: str, value: str, settings: {}) -> None:
    sd_process_resolved_substitution(
        prompt_builder,
        format_str,
        value,
        sd_get_substitution(value, settings),
        settings
    )


def sd_process_resolved_substitution(
        prompt_builder: PromptBuilder,
        format_str: str,
        value: str,
        substitution: dict[str, ...],
        settings:{}
) -> None:
    
    add_strength=settings.get("add_strength", None)
    if substitution is None:
        if add_strength is None:
            prompt_builder.append_positive(format_str.format(value=value))
        else:     
            prompt_builder.append_positive('(' + format_str.format(value=value) + ':'+ add_strength +')')
    else:
        override_positive_substitution = substitution.get("override_pos", None)
        if override_positive_substitution is not None:    
            prompt_builder.append_positive(override_positive_substitution)
        else:
            positive_substitution = substitution.get("pos", None)
            if positive_substitution is not None and positive_substitution != "":
                if add_strength is None:
                    prompt_builder.append_positive(format_str.format(value=positive_substitution))
                else:
                    prompt_builder.append_positive('(' + format_str.format(value=positive_substitution) + ':'+ add_strength +')')
        negative_substitution = substitution.get("neg", None)
        if negative_substitution is not None and negative_substitution != "":
            prompt_builder.append_negative(negative_substitution)


def sd_get_substitution(value: str, settings: {}) -> dict[str, ...]:
    substitutions = settings.get("substitutions", {})
    substitution_object = substitutions.get(value, None)
    if substitution_object is None:
        return None
    if (isinstance(substitution_object, str)):
        return {"pos": substitution_object}
    elif isinstance(substitution_object, builtins.dict):
        return substitution_object
    else:
        print(f'"{value}" substitution has invalid type {type(substitution_object)}')
        return None
            

# -----------------------------------------------------------------------------
# SPECIFIC PROMPT COMPONENT GENERATORS
# Gets the specific prompts and fills the prompt builder with them
# -----------------------------------------------------------------------------

# mapped to json file for editing
def sd_fill_eye_color_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    eye_color = current_person.eye_color
    prompt_builder.append_positive(settings.get(eye_color, settings["default"]))

# mapped faces to json file for editing
def sd_fill_face_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, face_prompt: {}) -> None:
    person_type = current_person.type
    person_funcname = current_person.func_name

    # Check to see if they are using the custom face settings
    story_faces = face_prompt.get("use_story_faces_prompt", False)
    unique_faces = face_prompt.get("use_unique_faces_prompt", False)
    random_faces = face_prompt.get("use_random_faces_prompt", False)

    # Determine the appropriate face prompt based on the person type and settings
    if person_type == "story" and story_faces and person_funcname in face_prompt:
        face_settings = face_prompt[person_funcname]
    elif person_type == "unique" and unique_faces and person_funcname in face_prompt:
        face_settings = face_prompt[person_funcname]
    elif person_type == "random" and random_faces and person_funcname in face_prompt:
        face_settings = face_prompt[person_funcname]
    elif person_type == "random" and not random_faces:
        face_settings = face_prompt[person_type]
    else:
        return

    # Append the positive and negative face-related prompts to the prompt_builder
    prompt_builder.append_positive(face_settings.get("pos", ""))
    prompt_builder.append_negative(face_settings.get("neg", ""))

def sd_fill_expression_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    sd_process_prompt_value(
        prompt_builder,
        current_person.resolve_happiness_range_key(),
        settings
    )

def sd_fill_skin_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    ethnicities = settings.get("ethnicities", None)
    if ethnicities is not None:
        ethnicities_list = ethnicities.get(current_person.skin_color, None)
        if ethnicities_list is not None:
            # We use the name to make the ethnicity deterministic, so that the same name always gives the same ethnicity
            simple_deterministic_seed = sum(ord(char) for char in current_person.name)
            random.seed(simple_deterministic_seed)
            ethnicity_prompt = random.choice(ethnicities_list)
            random.seed()
            prompt_builder.append_positive(ethnicity_prompt)
            return
    sd_process_substitution(prompt_builder, "{value} skin", current_person.skin_color, settings)

def sd_fill_age_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    age = current_person.age
    explicit_age_field = settings.get("add_explicit_age_prompt", False)
    if explicit_age_field:
        prompt_builder.append_positive("age " + str(age))


    sd_process_prompt_value(prompt_builder, current_person.resolve_age_range_key(), settings)

def sd_fill_height_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:

    sd_process_prompt_value(prompt_builder, current_person.resolve_height_range_key(), settings)    
    
def sd_fill_time_prompt(prompt_builder: PromptBuilder,settings: {}) -> None:

    if time_of_day == 0:   
        time_prompt = settings.get("early_morning", False)
    elif time_of_day == 1:   
        time_prompt = settings.get("morning", False)
    elif time_of_day == 2:   
        time_prompt = settings.get("afternoon", False)
    elif time_of_day == 3:   
        time_prompt = settings.get("evening", False)            
    elif time_of_day == 4:   
        time_prompt = settings.get("night", False)       
    prompt_builder.append_positive(time_prompt)    

def sd_get_location_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    location_name = current_person.location
    
    name = current_person.name
    if name in location_name or "bedroom" in location_name:
        location_name = "Bedroom"
    
    sd_process_substitution(prompt_builder,"{value}", location_name, settings)
    

def sd_fill_hair_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    if current_person.is_bald:
        prompt_builder.append_positive("bald")
    else:
        sd_process_substitution(prompt_builder, "{value} hair", current_person.hair_colour, settings)
        sd_process_substitution(prompt_builder, "{value}", current_person.hair_style, settings)


def sd_fill_breasts_prompt(prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    sd_process_prompt_value(prompt_builder, current_person.tits, settings)


def sd_process_position_prompt(
        prompt_builder: PromptBuilder,
        current_person: PersonPromptInputData,
        settings: {}
) -> PositionData:
    position_data = PositionData()

    current_sex_position = current_person.sex_position
    current_position = current_person.position
     
    position_settings = settings.get("current_position", "")
    if position_settings is None:
        prompt_builder.append_positive("standing")
        return position_data

    if current_sex_position is not None and "sex_position_prompt" in settings:
        if current_sex_position in settings.get("sex_position_prompt", ""):
            sd_process_prompt_value(prompt_builder, current_sex_position, settings.get("sex_position_prompt", ""))
        else:
            sd_process_prompt_value(prompt_builder, current_position, settings)    
    else:
        sd_process_prompt_value(prompt_builder, current_position, settings)
    if isinstance(position_settings, builtins.dict):
        if not position_settings.get("face_visible", True):
            position_data.face_visible = False
        if not position_settings.get("legs_visible", True):
            position_data.legs_visible = False
        if not position_settings.get("feet_visible", True):
            position_data.feet_visible = False
        if not position_settings.get("breasts_visible", True):
            position_data.breasts_visible = False


    return position_data


def sd_fill_body_type_prompt (prompt_builder: PromptBuilder, current_person: PersonPromptInputData, settings: {}) -> None:
    height = current_person.height 
    mheight = height / 100.0
    bmi = current_person.weight / (mheight * mheight)
    
    body_type = current_person.body_type
    
    #not sure how to best phrase these bmi-based prompt, feel free to improve...
    if bmi < 18.5: #underweight
        sd_process_prompt_value(prompt_builder, "severe_underweight", settings)
    elif bmi < 20.5: #slim
        sd_process_prompt_value(prompt_builder, "underweight", settings)
    elif bmi < 24.9: # "average", nothing in particular?
        sd_process_prompt_value(prompt_builder, "avarage_weight", settings)
    elif bmi < 26.9: #slightly overweight according to BMI, should curvy be in the early stages of overweight or the late stages of normal?
        sd_process_prompt_value(prompt_builder, "overweight", settings)
    else: #create a sliding value for overweighted-ness
        sd_process_prompt_value(prompt_builder, "severe_overweight", settings)            

    
    if body_type == "thin_body":
        sd_process_prompt_value(prompt_builder, "thin", settings)
    elif body_type == "curvy_body":
        sd_process_prompt_value(prompt_builder, "curvy", settings)
    elif body_type == "standard_preg_body":
        sd_process_prompt_value(prompt_builder, "default_preg", settings)
    else:
        sd_process_prompt_value(prompt_builder, "default", settings)


def sd_get_clothing_color(clothing: Clothing, settings: {}) -> str:
    if clothing and hasattr(clothing, 'colour'):
        color = clothing.colour
        # Convert the RGBA values to a Color object
        color_obj = Color(rgb=(color[0], color[1], color[2]))
        # Get the specific color name (e.g., "dark slate blue", "khaki", etc.)
        color_name = SD_get_color_opinion(color, settings.get("colors", None))
        return color_name
    return None


def sd_fill_clothing_prompt(prompt_builder: PromptBuilder, clothing: Clothing, settings: {}) -> None:
    name = clothing.name.lower()
    color = sd_get_clothing_color(clothing, settings)
    substitution = sd_get_substitution(name, settings)
    if (color is not None
            and (substitution is None or substitution.get("allow_color", True))):
        color_prefix = (color + " ")
    else:
        color_prefix = ""
    sd_process_resolved_substitution(prompt_builder,  color_prefix + "{value}", name, substitution, settings)


# Builds the outfit prompt 
# Based on the current person's upper/lower clothing layers, accessories, and visible body parts
def sd_fill_outfit_prompt(
        prompt_builder: PromptBuilder,
        current_person: PersonPromptInputData,
        position_data: PositionData,
        settings: {}
) -> None:
    outfit = current_person.outfit
    upper_clothing = current_person.outfit.get_upper_top_layer
    lower_clothing = current_person.outfit.get_lower_top_layer

    # Special case for apron and overwear, if one of them is present, default logic is overridden
    apron = upper_clothing is not None and upper_clothing.name == "Apron"
    overwear = upper_clothing is not None and upper_clothing.name in ["Suit Jacket", "Vest", "Lab Coat", "Bath_Robe"]
    if apron or overwear:
        sd_fill_clothing_prompt(prompt_builder, upper_clothing, settings)
        upper_clothes = outfit.get_upper_ordered()
        if len(upper_clothes) > 1:
            upper_clothing = upper_clothes[-2]
        else:
            upper_clothing = None

        if apron:
            lower_clothes = outfit.get_lower_ordered()
            if len(lower_clothes) > 1:
                lower_clothing = lower_clothes[-2]
            else:
                lower_clothing = None

    def find_underwear(ordered_clothes: list[Clothing]):
        for cloth in ordered_clothes[::-1]:
            if cloth.underwear:
                return cloth
        return None

    if outfit.vagina_visible:
        pube_description = current_person.pubes_description
        # Change pubes description, because Stable Diffusion will default "bald" to head causing literal baldness
        if current_person.pubes_description == "bald":
            pube_description = "shaved"
        sd_process_substitution(prompt_builder, "{value} pussy", pube_description, settings)

    if upper_clothing is None and lower_clothing is None:
        if not apron:
            sd_process_substitution(prompt_builder, "{value}", "naked", settings)
        else:
            sd_process_substitution(prompt_builder, "{value}", "naked apron", settings)
    else:
        bra = find_underwear(outfit.get_upper_ordered())
        top = upper_clothing
        if position_data.breasts_visible:
            if outfit.tits_visible:
                sd_process_substitution(prompt_builder, "{value}", "nipples", settings)
            if outfit.is_bra_visible and bra is not None:
                sd_fill_clothing_prompt(prompt_builder, bra, settings)
        if top is None:
            sd_process_substitution(prompt_builder, "{value}", "bare chest", settings)
        elif top != bra and not top.is_extension:
            sd_fill_clothing_prompt(prompt_builder, top, settings)

        panties = find_underwear(outfit.get_lower_ordered())
        bottom = lower_clothing
        if outfit.are_panties_visible and panties is not None:
            sd_fill_clothing_prompt(prompt_builder, panties, settings)
        if bottom is None:
            sd_process_substitution(prompt_builder, "{value}", "bottomless", settings)
        elif panties != bottom and not bottom.is_extension:
            sd_fill_clothing_prompt(prompt_builder, bottom, settings)

    added_makeup = False
    for accessory in outfit.accessories:
        accessory_name = accessory.name.lower()
        if accessory.is_glasses and position_data.face_visible:
            sd_process_substitution(prompt_builder, "{value}", "glasses", settings)
        elif accessory.is_makeup and position_data.face_visible and not added_makeup:
            sd_process_substitution(prompt_builder, "{value}", "makeup", settings)
            added_makeup = True
        elif accessory.is_gloves:
            sd_fill_clothing_prompt(prompt_builder, accessory, settings)
        elif "cum" in accessory_name:
            if (not ("face" in accessory_name and not position_data.face_visible)
                    and not ("tit" in accessory_name and not position_data.breasts_visible)):
                sd_process_substitution(prompt_builder, "{value}", accessory_name, settings)
        elif "creampie" in accessory_name:
            sd_process_substitution(prompt_builder, "{value}", accessory_name, settings)
        elif "collar" in accessory_name or "choker" in accessory_name or "scarf" in accessory_name:
            sd_fill_clothing_prompt(prompt_builder, accessory, settings)

    if position_data.feet_visible:
        if outfit.feet_visible:
            sd_process_substitution(prompt_builder, "{value}", "bare feet", settings)
        else:
            feet_layers = outfit.get_feet_ordered()
            if len(feet_layers) > 1:
                outer = feet_layers[-1]
                sd_fill_clothing_prompt(prompt_builder, outer, settings)
                inner = feet_layers[-2]
                if "socks" in inner.name:
                    sd_fill_clothing_prompt(prompt_builder, inner, settings)
            elif len(feet_layers) > 0:
                sd_fill_clothing_prompt(prompt_builder, feet_layers[-1], settings)

    if position_data.legs_visible:
        feet_layers = outfit.get_feet_ordered()
        if len(feet_layers) > 1:
            inner = feet_layers[-2]
            if not "socks" in inner.name:
                sd_fill_clothing_prompt(prompt_builder, inner, settings)


def sd_get_style_prompt():
    prompt_name = sd_get_setting('sd_selected_prompt', 'default')
    prompt_data = sd_get_prompt_data_by_name(prompt_name)
    if prompt_data:
        return prompt_data.get("style_prompt", "")
    return ""

# -----------------------------------------------------------------------------
# CACHE MANAGEMENT
# -----------------------------------------------------------------------------

def sd_clear_prompts_cache():
    global sdPromptCache
    sdPromptCache.clear()

# init cache
if not "sdPromptCache" in globals():
    sdPromptCache = SdPromptsCache()
