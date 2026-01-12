from __future__ import annotations
import renpy
import builtins
from typing import Callable, Iterable
from renpy.display import im
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.helper_functions.list_functions_ren import get_random_from_list, people_at_location
from game.major_game_classes.character_related.Person_ren import Person, list_of_people
from game.major_game_classes.game_logic.ActionList_ren import ActionList, Action
from game.major_game_classes.game_logic.BackGroundManager_ren import bg_manager
from game.major_game_classes.game_logic.RoomObject_ren import RoomObject
from game.major_game_classes.game_logic.RoomObject_factories_ren import make_floor

list_of_places: list[Room]
time_of_day = 0
bedroom: Room
lily_bedroom: Room
mom_bedroom: Room
kitchen: Room
hall: Room
home_bathroom: Room
aunt_apartment: Room
aunt_bedroom: Room
cousin_bedroom: Room
harem_mansion: Room
university: Room
university_bathroom: Room
university_lab: Room
strip_club: Room
bdsm_room: Room
strip_club_dressing_room: Room
dungeon: Room
clone_facility: Room
mall: Room
mall_bathroom: Room
office: Room
office_store: Room
mom_offices: Room
mom_office_lobby: Room
office_photocopy_room: Room
clothing_store: Room
electronics_store: Room
home_store: Room
sex_store: Room
gaming_cafe: Room
gaming_cafe_store_room: Room
mall_salon: Room
downtown_bar: Room
downtown_bar_bathroom: Room
downtown_hotel: Room
downtown: Room
hospital: Room
hospital_room: Room
gym: Room
gym_shower: Room
coffee_shop: Room
purgatory: Room
police_station: Room
city_hall: Room
prostitute_bedroom: Room
generic_bedroom_1: Room
generic_bedroom_2: Room
generic_bedroom_3: Room
generic_bedroom_4: Room
her_hallway: Room
lobby: Room
rd_division: Room
m_division: Room
p_division: Room
ceo_office: Room
storage_room: Room
break_room: Room

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
darken_matrix = im.matrix.saturation(0.9) * im.matrix.tint(.9, .9, .9) * im.matrix.brightness(-0.15)
standard_indoor_lighting = [[0.91, 0.91, 0.95], [0.98, 0.98, 0.98], [0.98, 0.98, 0.98], [0.98, 0.98, 0.98], [0.91, 0.91, 0.95]]
standard_outdoor_lighting = [[0.7, 0.7, 0.8], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0.7, 0.7, 0.8]]
standard_club_lighting = [[0.8, 0.8, 0.9], [0.8, 0.8, 0.9], [0.8, 0.8, 0.9], [0.8, 0.8, 0.9], [0.8, 0.8, 0.9]]
dark_lighting = [[0.4, 0.4, 0.55], [0.4, 0.4, 0.55], [0.4, 0.4, 0.55], [0.4, 0.4, 0.55], [0.4, 0.4, 0.55]]

class Room(): #Contains objects.
    def __init__(self, name: str, formal_name: str, background_name: str, objects: Iterable[RoomObject] = None,
            actions: list[Action] = None, map_pos = None, tutorial_label = None, visible = True, hide_in_known_house_map = True,
            lighting_conditions = None, privacy_level = 0, darken = True, accessible_func: Callable[[], bool] = None, room_events = None, allow_walk_in = False):
        '''
        map_pos: tuple of tile location in (see GRID_MAP_POS)
        darken: if True, darken the room at night else artificial lighting is used
        privacy_level: 0 = private, 1 = semi-public, 2 = semi-private, 3 = public
            when (1, 3) room is marked as public and availabe for random travel
        allow_walk_in: if True, people can walk into this room during generic sex loop
        '''
        self.name = name
        self.formal_name = formal_name
        self.background_name = background_name

        self.objects: list[RoomObject] = []
        if isinstance(objects, (list, tuple, set)):
            for x in objects:
                self.add_object(x)
        elif isinstance(objects, RoomObject):
            self.add_object(objects)

        if not any(x for x in self.objects if x.name == "floor"):
            self.add_object(make_floor())   # make sure we always have a floor to stand on.

        self.actions = ActionList(actions)

        self.on_room_enter_event_list = ActionList() #A list of Actions that are triggered when you enter a location. People events take priority.

        if map_pos is None:
            self.map_pos = [-1, -1] #off screen
        else:
            self.map_pos = map_pos #A tuple of two int values giving the hex coords, starting in the top left. Using this guarantees locations will always tessalate.

        self.visible = visible #If true this location is shown on the map. If false it is not on the main map and will need some other way to access it.
        self.hide_in_known_house_map = hide_in_known_house_map #If true this location is hidden in the house map, usually because their house is shown on the main map.

        self.tutorial_label = tutorial_label #When the MC first enters the room the tutorial will trigger.
        self.trigger_tutorial = True #Flipped to false once the tutorial has been done once
        self.accessible = True #If true you can move to this room. If false it is disabled

        if lighting_conditions is None: #Default is 100% lit all of the time.
            self.lighting_conditions = standard_outdoor_lighting
        else:
            self.lighting_conditions = lighting_conditions

        self.privacy_level = privacy_level
        self.darken = darken
        self.accessible_func = accessible_func
        self.room_events = room_events
        self.allow_walk_in = allow_walk_in
        self.lights_off = False
        self.identifier = generate_identifier((name, formal_name))

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Room) -> bool:
        if not isinstance(other, Room):
            return NotImplemented
        return self.identifier == other.identifier

    def show_background(self):
        if (time_of_day in (0, 4) and self.darken) or self.lights_off:
            bg_image = im.MatrixColor(bg_manager.background(self.background_name), darken_matrix)
        else:
            bg_image = bg_manager.background(self.background_name)

        renpy.scene("master")
        renpy.show(name = self.name, what = bg_image, layer = "master")

    def add_object(self, the_object: RoomObject):
        if isinstance(the_object, RoomObject) and the_object not in self.objects:
            self.objects.append(the_object)

    def remove_object(self, object_or_name: RoomObject | str):
        found = next((x for x in self.objects if x == object_or_name), None)
        if not found and isinstance(object_or_name, str):
            found = next((x for x in self.objects if x.name == object_or_name), None)

        if found:
            self.objects.remove(found)

    def add_person(self, person: Person):
        if not isinstance(person, Person):
            return
        if person not in list_of_people:
            list_of_people.append(person)
        person.change_location(self)

    def add_unique_on_room_enter_event(self, action: Action) -> bool:
        '''
        Return True when action added to room event list
        '''
        if action not in self.on_room_enter_event_list:
            self.on_room_enter_event_list.append(action)
            return True
        return False

    @property
    def people(self) -> list[Person]:
        return people_at_location(self)

    @property
    def person_count(self) -> int:
        return len(self.people)

    def objects_with_trait(self, the_trait: str) -> list[RoomObject]:
        return_list = []
        for obj in self.objects:
            if obj.has_trait(the_trait):
                return_list.append(obj)
        return return_list

    def has_object_with_trait(self, the_trait: str) -> bool:
        if the_trait == "None":
            return True
        return any(obj.has_trait(the_trait) for obj in self.objects)

    def get_object_with_trait(self, the_trait: str) -> RoomObject:
        if self.has_object_with_trait(the_trait):
            return get_random_from_list(self.objects_with_trait(the_trait))
        return None

    def get_object_with_name(self, name: str) -> RoomObject: #Use this to get objects from a room when you know what they should be named but don't have an object reference yet (ik
        for obj in self.objects:
            if obj.name == name:
                return obj
        return None

    def lock(self):
        self.allow_walk_in = False

    def unlock(self):
        self.allow_walk_in = True

    def get_lighting_conditions(self):
        return self.lighting_conditions[time_of_day]

    def add_action(self, action: Action):
        self.actions.add_action(action)

    def remove_action(self, action: Action):
        self.actions.remove_action(action)

    def turn_lights_off(self):
        if not hasattr(self, "old_lighting_conditions"): # only store old condition once
            self.old_lighting_conditions = self.lighting_conditions
        self.lighting_conditions = dark_lighting
        self.lights_off = True
        self.show_background()

    def turn_lights_on(self):
        if hasattr(self, "old_lighting_conditions"): # only restore if we have a saved condition
            self.lighting_conditions = self.old_lighting_conditions
            self.lights_off = False
            self.show_background()

    @property
    def is_accessible(self) -> bool:
        # func overrides property
        if self.accessible_func and callable(self.accessible_func):
            return self.accessible_func()
        return self.accessible

    @property
    def valid_actions(self) -> list[Action]:
        actions = [x for x in self.actions if x.is_action_enabled() or x.is_disabled_slug_shown()]
        actions.sort(key = lambda x: x.priority if x.is_action_enabled() else -1000, reverse = True)
        return actions

    def has_action(self, action: Action | str) -> bool:
        return self.actions.has_action(action)

    @property
    def has_cum_slut(self) -> bool:
        return not self.get_cum_slut() is None

    def get_cum_slut(self) -> Person:
        return get_random_from_list([x for x in self.people if x.has_cum_fetish])

    @property
    def has_anal_slut(self) -> bool:
        return not self.get_anal_slut() is None

    def get_anal_slut(self) -> Person:
        return get_random_from_list([x for x in self.people if x.has_anal_fetish])

    @property
    def has_breeder(self) -> bool:
        return not self.get_breeder() is None

    def get_breeder(self) -> Person:
        return get_random_from_list([x for x in self.people if x.has_breeding_fetish])

    @property
    def has_exhibitionist(self) -> bool:
        return not self.get_exhibitionist() is None

    def get_exhibitionist(self) -> Person:
        return get_random_from_list([x for x in self.people if x.has_exhibition_fetish])

    @property
    def is_private(self) -> bool:
        return self.privacy_level == 0

    @property
    def is_public(self) -> bool:
        return self.privacy_level in (1, 3)

    @property
    def room_average_slut(self) -> int:
        if self.person_count == 0:
            return 0
        total = 0
        for person in self.people:
            total += person.sluttiness
        return builtins.int(total / self.person_count)

    @property
    def room_max_slut(self) -> int:
        total = 0
        for person in self.people:
            total = builtins.max(person.sluttiness, total)
        return builtins.int(total)

    @property
    def room_outfit_average_sluttiness(self) -> int:
        if self.person_count == 0:
            return 0
        total = 0
        for person in self.people:
            total += person.outfit.outfit_slut_score
        return builtins.int(total / self.person_count)

    @property
    def room_outfit_max_sluttiness(self) -> int:
        total = 0
        for person in self.people:
            total = builtins.max(person.outfit.outfit_slut_score, total)
        return builtins.int(total)

    @property
    def room_outfit_eye_candy_score(self) -> int:
        if self.person_count == 0:
            return 0
        total = 0
        for person in self.people:
            total += person.outfit.outfit_slut_score // 5
            total += 5 if person.outfit.cum_covered else 0

        return builtins.int(total)

    @property
    def watcher_info_text(self) -> str:
        if self.person_count < 2:
            return "You are alone with her"
        if self.person_count < 3:
            return "One person watching"
        return f"{self.person_count - 1} people watching"

    @property
    def interruption_info_text(self) -> str:
        if self.is_private:
            return "No interruptions"
        return "Less chance of interruptions"

    def random_room_event(self) -> str:
        if self.room_events is None:
            return "default_room_event"
        return get_random_from_list(self.room_events)
