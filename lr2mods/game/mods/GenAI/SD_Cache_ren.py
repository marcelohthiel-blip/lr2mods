import json
import hashlib
from game.major_game_classes.character_related.Person_ren import Person
from pylru import LRUCache # type: ignore

time_of_day = 0

"""renpy
init -1 python:
"""

# =============================================================================
# PROMPT CACHE CLASS
# Implements LRU caching for SD prompts to improve performance.
# =============================================================================
class SdPromptsCache:

    def __init__(self, cache_size_limit: int = 1000):
        self._cache = LRUCache(cache_size_limit)

    def __setitem__(self, key, value) -> None:
        self._cache[key] = value

    def __getitem__(self, key) -> tuple[str, str]:
        return self._cache[key]

    def get(self, key, default=None) -> tuple[str, str]:
        return self._cache.get(key, default)

    def clear(self) -> None:
        self._cache.clear()


# =============================================================================
# PROMPT INPUT DATA CLASS
# Contains all character attributes needed for Stable Diffusion prompt generation.
# =============================================================================
class PersonPromptInputData:

    def __init__(self, person: Person, position: str, append_positive: str, append_negative: str):
        self.face_style = person.face_style
        self.type = person.type
        self.func_name = person.func_name
        self.name = person.name
        self.age = person.age
        self.eye_color = person.eyes[0].lower()
        self.skin_color = person.skin
        self.hair_colour = person.hair_colour[0].lower()
        self.hair_style = person.hair_style.display_name.lower()
        self.tits = person.tits
        self.body_type = person.body_type
        self.position = position
        try:
            self.sex_position = person.current_position.name
        except:
            self.sex_position = None
        self.happiness = person.happiness
        self.love = person.love
        self.outfit = person.outfit
        self.pubes_description = person.pubes_description

        self.append_positive = append_positive
        self.append_negative = append_negative
        self.time=time_of_day

        self.is_bald = person.is_bald
        self.location = mc.location.formal_name
        # internal height / 0.015 -> inch *2.54 -> cm
        self.height =  person.height/0.015 * 2.54
        self.weight =  person.weight
        

    def resolve_happiness_range_key(self) -> str:
        if self.happiness > 160:
            return "above160"
        elif self.happiness > 120:
            return "above120"
        elif self.happiness > 100:
            return "above100"
        else:
            if self.love > 0:
                return "sad"
            else:
                return "angry"

    @staticmethod
    def age_range_keys() -> list[str]:
        return ["above17", "above20", "above30", "above50", "above60"]

    def resolve_age_range_key(self) -> str:
        if self.age > 60:
            return "above60"
        elif self.age > 50:
            return "above50"
        elif self.age > 30:
            return "above30"
        elif self.age > 20:
            return "above20"
        else:
            return "above17"
            
    def resolve_height_range_key(self) -> str:

        
        height = self.height
        height_type = "average" 
        if height < 140:
            height_type = "extremly_short"
        elif height < 150:
            height_type = "very_short"
        elif height < 160:
            height_type = "short"
        elif height > 170:
            height_type = "tall"
        elif height > 180:
            height_type = "very_tall"
        elif height > 190:    
            height_type = "extremly_tall"      
        return height_type

    # Generates unique hash key for prompt caching.
    def to_cache_key(self) -> str:
        return hashlib.blake2b(
            json.dumps(
                {
                    "func_name": self.func_name,
                    "type": self.type,
                    "face_style": self.face_style,
                    "age": self.resolve_age_range_key(),
                    "eye_color": self.eye_color,
                    "skin_color": self.skin_color,
                    "hair_colour": self.hair_colour,
                    "hair_style": self.hair_style,
                    "tits": self.tits,
                    "body_type": self.body_type,
                    "position": self.position,
                    "sex_position": self.sex_position,
                    "happiness": self.resolve_happiness_range_key(),
                    "outfit": PersonPromptInputData._outfit_cache_key(self.outfit),
                    "pubes_description": self.pubes_description,
                    "append_positive": self.append_positive,
                    "append_negative": self.append_negative,
                    "height": self.height,
                    "weight": self.weight,
                    "location":self.location,
                    "time":self.time
                },
                sort_keys=True
            ).encode(),
            digest_size = 20 # Truncated to match SHA-1 20 bytes (160-bit).
        ).hexdigest() # Outputs in this case key of length 40 (2 hex symbols for every 1 byte).

    @staticmethod
    # Serialize outfit data so that it can be cached.
    def _outfit_cache_key(outfit: Outfit) -> dict[str, list[...]]:
        return {
            "upper_clothes": list(map(
                lambda clothing_piece: PersonPromptInputData._clothing_cache_key(clothing_piece),
                outfit.get_upper_ordered()
            )),
            "lower_clothes": list(map(
                lambda clothing_piece: PersonPromptInputData._clothing_cache_key(clothing_piece),
                outfit.get_lower_ordered()
            )),
            "feet_clothes": list(map(
                lambda clothing_piece: PersonPromptInputData._clothing_cache_key(clothing_piece),
                outfit.get_feet_ordered()
            )),
            "accessories": list(map(
                lambda clothing_piece: PersonPromptInputData._clothing_cache_key(clothing_piece),
                outfit.accessories
            ))
        }

    @staticmethod
    # Extracts clothing attributes for caching.
    def _clothing_cache_key(clothing: Clothing) -> dict[str, ...]:
        return {
            "name": clothing.name,
            "color": clothing.colour,
            "color_pattern": clothing.colour_pattern,
            "pattern": clothing.pattern,
            "half_off": clothing.half_off
        }
