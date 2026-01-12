from __future__ import annotations
from game.major_game_classes.character_related.Person_ren import Person, town_relationships
from game.major_game_classes.character_related.scene_manager_ren import scene_manager
from game.sex_positions.threesome.threesome_position_definitions_ren import list_of_threesomes


THREESOME_BASE_SLUT_REQ = 80
girl_swap_pos = True
report_log = {}
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def get_initial_threesome_pairing(position_tag):
    if position_tag in ("stand2", "stand3", "stand4", "stand5"):
        return (["Stand Right There", "stand"])
    if position_tag == "walking_away":
        return (["Turn Away From Me", "walking_away"])
    if position_tag == "kissing":
        return (["Put Your Arms Up", "kissing"])
    if position_tag == "missionary":
        return (["Lay on Your Back", "missionary"])
    if position_tag == "blowjob":
        return (["Get on Your Knees", "blowjob"])
    if position_tag == "against_wall":
        return (["Put Your Back to the Wall", "against_wall"])
    if position_tag == "back_peek":
        return (["Turn Away But Look At Me", "back_peek"])
    if position_tag == "sitting":
        return (["Sit Down", "sitting"])
    if position_tag == "kneeling1":
        return (["Lay Forward", "kneeling1"])
    if position_tag == "standing_doggy":
        return (["Bend Over", "standing_doggy"])
    if position_tag == "doggy":
        return (["Get on Your Hands and Knees", "doggy"])
    if position_tag == "cowgirl":
        return (["Sit on Top", "cowgirl"])
    return (["Broken Position", "stand4"])

def can_join_threesome(person_one: Person, person_two: Person, initial_position_tag: str): #Can use this function to check if there is a threesome position available that a second girl can join.
    if person_one.energy < 50 or person_two.energy < 50:
        return False

    for threeway in (x for x in list_of_threesomes if x.requirements(person_one, person_two)):
        #Look for positions that match with any position taken by girl 1
        if initial_position_tag in (threeway.position_one_tag, threeway.position_two_tag):
            return True
    return False

def willing_to_threesome(person_one: Person, person_two: Person) -> bool:    #Use this function to check and see if two people are willing to engage in a threesome
    # only allow threesomes when we had sex before (without condom)
    if person_one.has_taboo(["sucking_cock", "condomless_sex"]):
        return False
    if person_two.has_taboo(["sucking_cock", "condomless_sex"]):
        return False
    if person_one.opinion.threesomes <= -2 or person_two.opinion.threesomes <= -2:
        return False

    person_one_slut_req = THREESOME_BASE_SLUT_REQ
    person_two_slut_req = THREESOME_BASE_SLUT_REQ
    if town_relationships.is_family(person_one, person_two):
        person_one_slut_req += (-5 * (person_one.opinion.incest - 2)) #Incest modifier
        person_two_slut_req += (-5 * (person_two.opinion.incest - 2)) #Incest modifier

    # threesome opinion modifier
    person_one_slut_req += (person_one.opinion.threesomes * -5)
    person_two_slut_req += (person_two.opinion.threesomes * -5)

    if person_one.effective_sluttiness() > person_one_slut_req \
            and person_two.effective_sluttiness() > person_two_slut_req:
        return True
    return False

class Threesome_Position():
    def __init__(self, name, slut_requirement, position_one_tag, position_two_tag, girl_one_final_description, girl_two_final_description, requires_location, requirements,
            p1_transform, p2_transform, p1_z_order = 0, p2_z_order = 1, mc_position = None, can_swap = False, verb = "fuck", verbing = None):
        self.name = name
        self.slut_requirement = slut_requirement #The required slut score of the girl. Obedience will help fill the gap if possible, at a happiness penalty. Value from 0 (almost always possible) to ~100
        self.position_one_tag = position_one_tag # The tag used to get the correct position image set
        self.position_two_tag = position_two_tag # The tag used to get the correct position image set
        self.girl_one_final_description = girl_one_final_description   #Textual position description if girl one is the final one in position
        self.girl_two_final_description = girl_two_final_description      #textual position description if girl two is the final one in position
        self.requires_location = requires_location #
        self.requirements = requirements        #The requirements to run this position. Should be a function
        self.verb = verb #A verb used to describe the position. "Fuck" is default, and mostly used for sex positions or blowjobs etc. Kiss, Fool around, etc. are also possibilities.
        self.verbing = verbing
        self.current_modifier = None #We will update this if the position has a special modifier that should be applied, like blowjob.
        self.p1_transform = p1_transform
        self.p2_transform = p2_transform
        self.p1_z_order = p1_z_order
        self.p2_z_order = p2_z_order
        self.mc_position = mc_position          #Holds the positions that MC can take during this position
        self.can_swap = can_swap

        if verbing is None:
            self.verbing = verb + "ing"

    # requires the existence of a scene_manager with both actors
    def update_scene(self, person_one: Person, person_two: Person):
        #print("Render: " + self.name + (" (Swapped)" if girl_swap_pos else ""))
        if girl_swap_pos:
            #print(person_two.name + " at: " + self.position_one_tag + ", z-order: " + str(self.p1_z_order))
            #print(person_one.name + " at: " + self.position_two_tag + ", z-order: " + str(self.p2_z_order))
            scene_manager.update_actor(person_two, position = self.position_one_tag, display_transform = self.p1_transform, z_order = self.p1_z_order)
            scene_manager.update_actor(person_one, position = self.position_two_tag, display_transform = self.p2_transform, z_order = self.p2_z_order)
        else:
            #print(person_one.name + " at: " + self.position_one_tag + ", z-order: " + str(self.p1_z_order))
            #print(person_two.name + " at: " + self.position_two_tag + ", z-order: " + str(self.p2_z_order))
            scene_manager.update_actor(person_one, position = self.position_one_tag, display_transform = self.p1_transform, z_order = self.p1_z_order)
            scene_manager.update_actor(person_two, position = self.position_two_tag, display_transform = self.p2_transform, z_order = self.p2_z_order)
        scene_manager.draw_scene()

    def redraw_scene(self, person_one: Person, person_two: Person):
        scene_manager.draw_scene()

    def have_orgasm(self, person: Person):
        actor = scene_manager.get_actor(person)
        if "report_log" in globals() and isinstance(report_log, dict) and actor:
            if actor.position == self.position_one_tag if girl_swap_pos else self.position_two_tag:
                report_log["girl two orgasms"] = report_log.get("girl two orgasms", 0) + 1
            else:
                report_log["girl one orgasms"] = report_log.get("girl one orgasms", 0) + 1
        person.have_orgasm()
