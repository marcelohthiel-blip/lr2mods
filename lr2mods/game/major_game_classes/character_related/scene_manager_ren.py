from __future__ import annotations
import builtins
import renpy
from game.bugfix_additions.debug_info_ren import write_log
from game.helper_functions.character_display_functions_ren import clear_scene
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.character_related.Person_ren import Person, mc

def character_center(x):
    return x
scene_manager: 'Scene'
character_right = None
character_right_flipped = None
character_center_flipped = None
character_left = None
character_left_flipped = None
character_far_left_flipped = None
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
def hide_ui(): # Hides the UI
    renpy.hide_screen("player_status_hud")
    renpy.hide_screen("phone_hud")
    renpy.hide_screen("business_status_hud")
    renpy.hide_screen("goal_hud")
    renpy.hide_screen("floating_notifications")

def show_ui(): # Show the UI
    renpy.show_screen("player_status_hud")
    renpy.show_screen("phone_hud")
    renpy.show_screen("business_status_hud")
    renpy.show_screen("goal_hud")
    renpy.show_screen("floating_notifications")


# z_order determines the order in which the actors are drawn, low number first, high number later
class Actor():
    def __init__(self, person: Person, outfit: Outfit, position: str = "default", emotion: str = None, special_modifier: str = None, lighting = None, display_transform = None, z_order: int = None, visible = True):
        self.person_identifier = person.identifier
        self.outfit = outfit.get_copy()
        self.position = position
        self.emotion = emotion
        self.special_modifier = special_modifier
        self.lighting = lighting
        self.display_transform = display_transform
        self.sort_order = 2
        self.z_order = 0
        self.visible = visible

        if position == "default" or position is None:
            self.position = person.idle_pose

        if emotion is None:
            self.emotion = person.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if display_transform is None:
            self.display_transform = character_right

        if z_order:
            self.z_order = z_order

        if display_transform in (character_center, character_center_flipped):
            self.sort_order = 1
        if display_transform in (character_left, character_left_flipped):
            self.sort_order = 0

    def __hash__(self) -> int:
        return hash(self.person_identifier)

    def __eq__(self, other: Actor) -> bool:
        if not isinstance(other, Actor):
            return NotImplemented
        return self.person_identifier == other.person_identifier

    @property
    def person(self) -> Person:
        return Person.get_person_by_identifier(self.person_identifier)

    def draw_actor(self):
        self.person.draw_person(position = self.position, emotion = self.emotion, special_modifier = self.special_modifier, lighting = self.lighting, display_transform = self.display_transform, display_zorder = self.z_order, wipe_scene = False, show_person_info = False)

    def hide(self):
        self.visible = False
        self.person.hide_person()

class Scene():
    def __init__(self):
        self.actors: list[Actor] = []

    @property
    def current_actors(self) -> list[Person]:
        '''
        Returns list of Person objects of actors current visible on screen
        '''
        return [x.person for x in self.actors if x.visible]

    def get_actor(self, person: Person) -> Actor | None:
        return next((x for x in self.actors if x.person == person), None)

    def add_group(self, people: list[Person], position: str = "default", emotion: str = None, special_modifier: str = None, lighting = None, z_order = None):
        xoffset = 0.1
        for person in people:
            self.add_actor(person, None, position, emotion, special_modifier, lighting, character_center(xoffset), z_order)
            xoffset -= .1
        self.draw_scene()

    def update_group(self, position: str = "default", emotion: str = None, special_modifier: str = None, lighting = None):
        for person in (x.person for x in self.actors if x.visible):
            self.update_actor(person, None, position = position, emotion = emotion, special_modifier = special_modifier, lighting = lighting)

    def add_actor(self, person: Person, outfit: Outfit | None = None, position: str | None = None, emotion: str = None, special_modifier: str = None, lighting = None, display_transform = None, z_order = None, visible = True):
        # adds actor to scene, note that actor will change to location appropriate outfit
        # when another outfit is required for scene, this need to be passed to the outfit parameter
        if not isinstance(person, Person):
            write_log("Actor requires a Person object.")
            return None

        actor = next((x for x in self.actors if x.person == person), None)
        if actor:   # we have an existing actor object, so use that
            self.show_actor(actor.person, outfit, position, emotion, special_modifier, lighting, display_transform, z_order)
        else:       # add person as actor
            # move actor to mc location
            person.change_location(mc.location)
            if outfit:
                person.apply_outfit(outfit)
            else:
                person.apply_outfit(person.current_planned_outfit)
            if display_transform is None:
                display_transform = self.get_random_free_position()
            actor = Actor(person, person.outfit, position, emotion, special_modifier, lighting, display_transform, z_order, visible)
            self.actors.append(actor)
            if visible:
                self.draw_scene()
        return actor

    # Removes all actors from the scene
    def clear_scene(self, reset_actor = True):
        # cleanup scene, when reset_actor = False, she will not revert back to her default outfit
        # and will keep wearing the same outfit as at the end of the scene
        # when a time slot change occurs, she will change the outfit
        for person in (actor.person for actor in self.actors):
            person.hide_person()
            self.remove_actor(person, reset_actor = reset_actor)
        clear_scene()

    def review_outfits(self, dialogue = True):
        for person in (actor.person for actor in self.actors):
            person.review_outfit(dialogue = dialogue)

    def apply_outfits(self, planned_outfits = False):
        for actor in self.actors:
            actor.person.apply_outfit(
                (actor.person.planned_outfit if planned_outfits else actor.outfit),
                show_dress_sequence = actor.visible,
                scene_manager = self)

    def apply_outfit(self, person: Person, outfit: Outfit | None = None):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            actor.person.apply_outfit(
                (outfit if outfit else actor.outfit),
                show_dress_sequence = actor.visible,
                scene_manager = self)

    def remove_clothing(self, person: Person, clothing: list[Clothing]):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            actor.person.remove_clothing(clothing, position = actor.position, emotion = actor.emotion, display_transform = actor.display_transform,
                lighting = actor.lighting, scene_manager = self, wipe_scene = False, delay = 1 if actor.visible else 0)

    def update_actor(self, person: Person, outfit: Outfit | None = None, position: str | None = None, emotion: str = None, special_modifier: str = None, lighting = None, display_transform = None, z_order = None):
        actor = next((x for x in self.actors if x.person == person), None)
        if not actor:
            self.add_actor(person, outfit, position, emotion, special_modifier, lighting, display_transform, z_order)
            return

        if not actor.visible: # update makes actor visible too
            actor.visible = True
        if outfit:
            actor.outfit = outfit.get_copy()
            actor.person.apply_outfit(outfit)
        if position:
            if position == "default" or position is None:
                actor.position = person.idle_pose
            else:
                actor.position = position
        if emotion:
            actor.emotion = emotion
        actor.special_modifier = special_modifier   # always set special modifier
        if lighting:
            actor.lighting = lighting
        if display_transform:
            actor.display_transform = display_transform
        if z_order is not None:
            actor.z_order = z_order

        # print("Update actor:" + actor.person.name + " (position: " + actor.position + ", z-order: " + str(actor.z_order) + ")")
        self.draw_scene()

    def strip_actor_outfit_to_max_sluttiness(self, person, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, temp_sluttiness_boost = 0):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            #mc.log_event("Strip " + actor.person.title, "gray_float_text")
            return actor.person.strip_outfit_to_max_sluttiness(top_layer_first = top_layer_first, exclude_upper = exclude_upper, exclude_lower = exclude_lower, exclude_feet = exclude_feet, narrator_messages = narrator_messages, display_transform = actor.display_transform, lighting = actor.lighting, temp_sluttiness_boost = temp_sluttiness_boost, position = actor.position, emotion = actor.emotion, scene_manager = self)
        return False

    def strip_full_outfit(self, person: Person | None = None, strip_feet = False, strip_accessories = False, lighting = None, delay = 1, only_visible_actors = True):
        strip_matrix = []
        if person is None:
            actors = (x for x in self.actors if not only_visible_actors or x.visible)
        else:
            actors = (x for x in self.actors if x.person == person)

        for actor in actors:
            strip_list = actor.person.outfit.get_full_strip_list(strip_feet = strip_feet, strip_accessories = strip_accessories)
            strip_matrix.append((actor, strip_list, False))

        self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)

    def strip_to_underwear(self, person: Person | None = None, visible_enough = True, avoid_nudity = False, lighting = None, delay = 1, only_visible_actors = True):
        strip_matrix = []
        if person is None:
            actors = (x for x in self.actors if not only_visible_actors or x.visible)
        else:
            actors = (x for x in self.actors if x.person == person)

        for actor in actors:
            strip_list = actor.person.outfit.get_underwear_strip_list(visible_enough = visible_enough, avoid_nudity = avoid_nudity)
            strip_matrix.append((actor, strip_list, False))

        self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)

    def strip_to_tits(self, person: Person | None = None, visible_enough = True, prefer_half_off = False, lighting = None, delay = 1, only_visible_actors = True):
        strip_matrix = []
        if person is None:
            actors = (x for x in self.actors if not only_visible_actors or x.visible)
        else:
            actors = (x for x in self.actors if x.person == person)

        for actor in actors:
            half_off_instead = False
            if prefer_half_off and actor.person.outfit.can_half_off_to_tits(visible_enough = visible_enough):
                strip_list = actor.person.outfit.get_half_off_to_tits_list(visible_enough = visible_enough)
                half_off_instead = True
            else:
                strip_list = actor.person.outfit.get_tit_strip_list()

            strip_matrix.append((actor, strip_list, half_off_instead))

        self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)

    def strip_to_vagina(self, person: Person | None = None, visible_enough = True, prefer_half_off = False, lighting = None, delay = 1, only_visible_actors = True):
        strip_matrix = []
        if person is None:
            actors = (x for x in self.actors if not only_visible_actors or x.visible)
        else:
            actors = (x for x in self.actors if x.person == person)

        for actor in actors:
            half_off_instead = False
            if prefer_half_off and actor.person.outfit.can_half_off_to_vagina():
                strip_list = actor.person.outfit.get_half_off_to_vagina_list(visible_enough = visible_enough)
                half_off_instead = True
            else:
                strip_list = actor.person.outfit.get_vagina_strip_list()

            strip_matrix.append((actor, strip_list, half_off_instead))

        self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)

    def strip_actor_strip_matrix(self, strip_matrix: list[Actor, list[Clothing], bool], lighting = None, delay = 1):
        keep_stripping = True
        while keep_stripping:
            keep_stripping = False
            for am in strip_matrix:
                actor: Actor = am[0]
                if am[1]:
                    the_clothing = am[1].pop(0)
                    if delay > 0:
                        actor.person.draw_quick_removal(the_clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = am[2]) #Draw the strip choice being removed from our current outfit
                    else:
                        actor.person.outfit.remove_clothing(the_clothing)
                    keep_stripping = True

    def strip_actor_strip_list(self, person: Person, strip_list: list[Clothing], lighting = None, half_off_instead = False):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            for item in strip_list:
                actor.person.draw_quick_removal(item, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = half_off_instead)

    def draw_animated_removal(self, person: Person, clothing: Clothing, lighting: list[float] = None, half_off_instead = False): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            #mc.log_event("Remove clothing " + actor.person.title, "gray_float_text")
            actor.person.draw_animated_removal(clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = half_off_instead)

    def show_dress_sequence(self, person: Person, target_outfit: Outfit, lighting: list[float] = None):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            actor.person.show_dress_sequence(outfit = target_outfit, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self)

    def get_random_free_position(self):
        if not any(x for x in self.actors if x.display_transform in (character_right, character_right_flipped)):
            return renpy.random.choice([character_right, character_right_flipped])
        if not any(x for x in self.actors if x.display_transform in (character_center, character_center_flipped)):
            return renpy.random.choice([character_center, character_center_flipped])
        if not any(x for x in self.actors if x.display_transform in (character_left, character_left_flipped)):
            return renpy.random.choice([character_left, character_left_flipped])
        return character_far_left_flipped

    # removes specific actor from scene
    def remove_actor(self, person: Person, reset_actor = True):
        # removes actor from scene and reset_actor will move her to her original location and reset her outfit
        # if an actor is only temporary not present, use hide_actor methods
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            if reset_actor:
                # move person to original location
                actor.person.change_location(actor.person.get_destination())
                # reset actor clothing
                actor.person.apply_planned_outfit()
            actor.person.hide_person()
            self.actors.remove(actor)
            self.draw_scene()

    def has_actor(self, person: Person) -> bool:
        return any(x for x in self.actors if x.person == person)

    def hide_actor(self, person: Person):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            actor.hide()
            self.draw_scene()

    def hide_actors(self, people: list[Person] | None = None):
        # hide all or specific actors from scene
        # so you can bring them back later
        if people is None:
            for actor in (x for x in self.actors if x.visible):
                actor.hide()

        if isinstance(people, (list, tuple, set)):
            for actor in (x for x in self.actors if x.person in people):
                actor.hide()

    def show_all_actors(self):
        for actor in self.actors:
            actor.visible = True
        self.draw_scene()

    def show_actor(self, person: Person, outfit: Outfit | None = None, position: str | None = None, emotion: str = None, special_modifier: str = None, lighting = None, display_transform = None, z_order = None):
        actor = next((x for x in self.actors if x.person == person), None)
        if actor:
            actor.visible = True
            self.update_actor(actor.person, outfit, position, emotion, special_modifier, lighting, display_transform, z_order)
        else:
            self.add_actor(person, outfit, position, emotion, special_modifier, lighting, display_transform, z_order)

    def draw_info_ui(self):
        clear_scene()
        visible_actors = [x for x in self.actors if x.visible]
        if builtins.len(visible_actors) > 3:
            return  # we cannot display more info than 3

        if builtins.len(visible_actors) > 1:
            renpy.show_screen("multi_person_info_ui", visible_actors)
        elif builtins.len(visible_actors) == 1:
            renpy.show_screen("person_info_ui", visible_actors[0].person)

    def draw_scene(self, exclude_list: list[Person] = []):
        self.draw_info_ui()
        for actor in sorted([x for x in self.actors if x.visible and x not in exclude_list], key = lambda x: x.z_order):
            #print("Draw: " + actor.person.name + " at: " + str(actor.z_order))
            actor.draw_actor()

    # update each actor and draw scene
    def update_scene(self, position: str | None = None, emotion: str = None, special_modifier: str = None, lighting = None):
        for actor in sorted(self.actors, key = lambda x: x.z_order):
            if position:
                actor.position = position
            if emotion:
                actor.emotion = emotion
            actor.special_modifier = special_modifier   # always set special modifier
            if lighting:
                actor.lighting = lighting
        self.draw_scene()
