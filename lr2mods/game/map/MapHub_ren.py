from __future__ import annotations
from typing import Iterator
from game.bugfix_additions.mapped_list_ren import MappedList, generate_identifier
from game.helper_functions.list_functions_ren import all_locations_in_the_game
from game.major_game_classes.game_logic.Room_ren import Room

office_hub: MapHub
strip_club_hub: MapHub
home_hub: MapHub
mall_hub: MapHub
university_hub: MapHub
harem_hub: MapHub
aunt_home_hub: MapHub
downtown_hub: MapHub
gym_hub: MapHub
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""
import math

class MapHub():
    def __init__(self, name: str, formal_name: str, locations: list[Room] | None = None,
            position: 'Point' | None = None, icon = None, accessible_func = None, visible = True):
        self.name = name
        self.formal_name = formal_name
        # internal property don't use in code -> user iterator of hub to get its locations
        self.locations = MappedList(Room, all_locations_in_the_game)
        self.position = position
        self.icon = icon
        self.accessible_func = accessible_func
        self.visible = visible
        self.locations.extend(locations)
        self.identifier = generate_identifier((name, formal_name))

    def __hash__(self):
        return self.identifier

    def __eq__(self, other: MapHub) -> bool:
        if not isinstance(other, MapHub):
            return NotImplemented
        return self.identifier == other.identifier

    def __iter__(self) -> Iterator[Room]:
        return iter(self.locations)

    def add_location(self, location: Room):
        self.locations.append(location)

    def remove_location(self, location: Room):
        self.locations.remove(location)

    @property
    def is_accessible(self) -> bool:
        if self.accessible_func and callable(self.accessible_func):
            return self.accessible_func()
        return True

    @property
    def is_visible(self) -> bool:
        return self.visible and self.visible_count > 0

    @property
    def is_expandable(self) -> bool:
        return self.visible_count > 1

    @property
    def visible_count(self) -> bool:
        return len(self.visible_locations)

    @property
    def visible_locations(self) -> list[Room]:
        return [x for x in self if x.visible]

class Point():
    def __init__(self, x: int, y: int):
        self.X = x
        self.Y = y

    def __str__(self) -> str:
        return f"Point({self.X}, {self.Y})"

    def distance(self, other: Point):
        if isinstance(other, Point):
            dx = self.X - other.X
            dy = self.Y - other.Y
            return math.sqrt(dx ** 2 + dy ** 2)
        raise TypeError
