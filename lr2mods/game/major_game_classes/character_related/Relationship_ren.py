from __future__ import annotations
import builtins
from game.random_lists_ren import get_random_from_weighted_list
from game.major_game_classes.character_related.Person_ren import Person, mc
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
class Relationship(): #A class used to store information about the relationship between two people. Do not manipulate directly, use RelationshipArray to change things.
    def __init__(self, person_a: Person, person_b: Person, type_a: str, type_b: str | None = None, visible = None):
        self._person_a = person_a.identifier
        self._person_b = person_b.identifier
        self.type_a = type_a #person_a TO person_b, written so you could tell what person_b is if you listed them. Ie. "Lily - Daughter".
        if type_b is None: #Type can vary depending on what direction you view the relationship ie. mother-daughter, employee-boss.
            self.type_b = type_a
        else:
            self.type_b = type_b

        if visible is None:
            self.visible = True
        else:
            self.visible = visible

    def __hash__(self) -> int:
        return hash((self.person_a, self.person_b))

    def __eq__(self, other: Relationship) -> bool:
        if not isinstance(other, Relationship):
            return NotImplemented
        return (self.person_a, self.person_b) == (other.person_a, other.person_b)

    @property
    def person_a(self) -> Person:
        return Person.get_person_by_identifier(self._person_a)

    @property
    def person_b(self) -> Person:
        return Person.get_person_by_identifier(self._person_b)

    def get_other_person(self, person: Person) -> Person | None: #Used to make it simpler to get a relationship for one person and know who the "other" person is.
        if person.identifier == self._person_a:
            return self.person_b
        if person.identifier == self._person_b:
            return self.person_a
        return None

    def get_other_person_identifier(self, identifier: int) -> int | None:
        if identifier == self._person_a:
            return self._person_b
        if identifier == self._person_b:
            return self._person_a
        return None

    def get_type(self, person: Person = None) -> str | None:
        if not isinstance(person, Person):
            return None
        if person.identifier == self._person_a:
            return self.type_a
        if person.identifier == self._person_b:
            return self.type_b
        return None

    def get_type_by_identifier(self, identifier: int) -> str | None:
        if identifier == self._person_a:
            return self.type_a
        if identifier == self._person_b:
            return self.type_b
        return None


class RelationshipArray():  # pylint: disable=protected-access
    RELATIONSHIP_FAMILY = ("Mother", "Daughter", "Sister", "Cousin", "Niece", "Aunt", "Grandmother", "Granddaughter")
    RELATIONSHIP_SCALE = ("Nemesis", "Rival", "Acquaintance", "Friend", "Best Friend")

    @staticmethod
    def relationship_type_sort_index(type: str) -> int:
        if type in RelationshipArray.RELATIONSHIP_FAMILY:
            return RelationshipArray.RELATIONSHIP_FAMILY.index(type)
        if type in RelationshipArray.RELATIONSHIP_SCALE:
            return 30 - RelationshipArray.RELATIONSHIP_SCALE.index(type)
        return 999

    def __init__(self):
        self.relationships: list[Relationship] = [] #List of relationships. Relationships are bi-directional, so if you look for person_a, person_b you'll get the same object as person_b, person_a (but the type can be relative to the order).
        ### Types of Relationships (* denotes currently unused but planned roles)
        # Family: Mother, Daughter, Cousin, Niece, Aunt, Grandmother*, Granddaughter*
        # Positive: Acquaintance, Friend, Best Friend, Girlfriend*, Fiancée*, Wife*
        # Negative: Rival, Nemesis*

    def update_relationship(self, person_a: Person, person_b: Person, type_a: str, type_b: str | None = None, visible = None): #Note that type_a is required, but if you want to do just one half of a relationship you can flip the person order around.
        # Don't form relationships with yourself or an empty one !
        if person_a == person_b or not person_a or not person_b:
            return

        the_relationship = self.get_relationship(person_a, person_b)
        if the_relationship is None: #No relationship exists yet, make one.
            self.relationships.append(Relationship(person_a, person_b, type_a, type_b, visible))
            return

        #A relationship exists, update it to the new state.
        if person_a.identifier == the_relationship._person_a: #Relationships may have been referred to in the opposite order, so flip the references around if needed.
            if type_a is not None:
                the_relationship.type_a = type_a

            if type_b is None:
                the_relationship.type_b = type_a
            else:
                the_relationship.type_b = type_b

        elif person_a.identifier == the_relationship._person_b:
            if type_a is not None:
                the_relationship.type_b = type_a

            if type_b is None:
                the_relationship.type_a = type_a
            else:
                the_relationship.type_a = type_b

        if visible is not None:
            the_relationship.visible = visible

    def get_relationship(self, person_a: Person, person_b: Person) -> Relationship | None:
        return next((x for x in self.relationships
                if x._person_a == person_a.identifier and x._person_b == person_b.identifier
                    or x._person_a == person_b.identifier and x._person_b == person_a.identifier), None)

    def get_relationship_list(self, person: Person, types: tuple[str] | list[str] | str | None = None, visible = None) -> tuple[Relationship]:
        if isinstance(types, str):
            types = [types]

        return tuple(x for x in self.relationships
            if (visible is None or x.visible == visible)
            and ((x._person_a == person.identifier and x._person_b and (types is None or x.type_a in types))
            or (x._person_b == person.identifier and x._person_a and (types is None or x.type_b in types))))

    def get_relationship_type_list(self, person: Person, types = None, visible = None) -> list[tuple[Person, str]]:
        return_list = []
        if isinstance(types, str):
            types = [types]
        for relationship in self.get_relationship_list(person, types, visible):
            other_person = relationship.get_other_person(person)
            if other_person:
                return_list.append((other_person, self.get_relationship_type(person, other_person))) #Creates a tuple of [Person, Type] for every entry in the list.
        return return_list

    def get_business_relationships(self, types: list[str] | str = None) -> tuple[Relationship]: #Returns a list containing all relationships between people in your company.
        '''
        Returns a list containing all relationships between people in your company
        '''
        if isinstance(types, str):
            types = [types]
        employee_list_ids = [x.identifier for x in mc.business.employee_list + mc.business.intern_list]

        return tuple(x for x in self.relationships
            if (not types or any(y in types for y in (x.type_a, x.type_b)))
            and all(y in employee_list_ids for y in (x._person_a, x._person_b)))

    def get_relationship_type(self, person_a: Person, person_b: Person) -> str | None: #Note that getting relationship for (person_a, person_b) may yield a different result from (person_b, person_a), because the perspective is different.
        '''
        Return the relationship type between two people from the perspective of person_a
        Example: when using (mom, lily) it will return 'Daughter' since lily is mom's daughter.
                 when using (lily, mom) it will return 'Mother' since mom is lily's mother.
        '''
        the_relationship = self.get_relationship(person_a, person_b)
        if the_relationship is not None:
            return the_relationship.get_type_by_identifier(person_a.identifier)
        return None

    def get_existing_children(self, person: Person) -> list[Person]:
        return_list = []
        for relationship in self.get_relationship_type_list(person, "Daughter"):
            return_list.append(relationship[0])
        return return_list

    def get_existing_child_count(self, person: Person) -> int: #Returns a count of how many children this character has who are "real" characters, vs just a stat.
        return len(self.get_existing_children(person))

    def get_existing_parents(self, person: Person) -> list[Person]:
        return_list = []
        for relationship in self.get_relationship_type_list(person, types = "Mother"):
            return_list.append(relationship[0])
        return return_list

    def get_existing_parent_count(self, person: Person) -> int: #Returns a count of how many children this character has who are "real" characters, vs just a stat.
        return builtins.len(self.get_existing_parents(person))

    def remove_all_relationships(self, person: Person): #Clears this person out of the relationship database (if, for example, we want to delete a person from the game)
        for relationship in self.get_relationship_list(person):
            self.relationships.remove(relationship)

    def improve_relationship(self, person_a: Person, person_b: Person, visible = None): #Improves a non-familial relationship between the two people.
        the_relationship = self.get_relationship(person_a, person_b)
        if the_relationship is not None: #If it exists we're going to improve it by one step, up to best friend.
            the_type = the_relationship.get_type_by_identifier(person_a.identifier)
            if the_type in RelationshipArray.RELATIONSHIP_SCALE: #You can only change non-family and non-romantic relationships like this.
                the_state = RelationshipArray.RELATIONSHIP_SCALE.index(the_type)
                the_state += 1
                if the_state + 1 >= len(RelationshipArray.RELATIONSHIP_SCALE): #Get the current state and increase it by one.
                    the_state = len(RelationshipArray.RELATIONSHIP_SCALE) - 1

                self.update_relationship(person_a, person_b, RelationshipArray.RELATIONSHIP_SCALE[the_state], visible)

        else:
            self.update_relationship(person_a, person_b, "Friend", visible)

    def worsen_relationship(self, person_a: Person, person_b: Person, visible = None): #Worsens a non-familial relationship between two people
        the_relationship = self.get_relationship(person_a, person_b)
        if the_relationship is not None: #If it exists we're going to improve it by one step, up to best friend.
            the_type = the_relationship.get_type_by_identifier(person_a.identifier)
            if the_type in RelationshipArray.RELATIONSHIP_SCALE: #You can only change non-family and non-romantic relationships like this.
                the_state = RelationshipArray.RELATIONSHIP_SCALE.index(the_type)
                the_state -= 1
                the_state = max(the_state, 0) # 0 is lowest value

                self.update_relationship(person_a, person_b, RelationshipArray.RELATIONSHIP_SCALE[the_state], visible)

        else:
            self.update_relationship(person_a, person_b, "Rival", visible)

    def begin_relationship(self, person_a: Person, person_b: Person): #Sets their relationship to Acquaintance if they do not have one, otherwise leaves it untouched.
        the_relationship = self.get_relationship(person_a, person_b)
        if the_relationship is None: #Only sets a relationship for these people if one does not exist, so as to not override friendships or familial relationships
            self.update_relationship(person_a, person_b, get_random_from_weighted_list([[RelationshipArray.RELATIONSHIP_SCALE[1], 20], [RelationshipArray.RELATIONSHIP_SCALE[2], 60], [RelationshipArray.RELATIONSHIP_SCALE[3], 20]]))

    def is_family(self, person_a: Person, person_b: Person) -> bool:
        return self.get_relationship_type(person_a, person_b) in RelationshipArray.RELATIONSHIP_FAMILY

    def get_family_members(self, person: Person) -> list[Person]:
        return_list = []
        for relationship in self.get_relationship_type_list(person, types = RelationshipArray.RELATIONSHIP_FAMILY):
            return_list.append(relationship[0])
        return return_list

    def get_existing_mother(self, person: Person) -> Person | None:
        return_list = []
        for relationship in self.get_relationship_type_list(person, types = "Mother"):
            return_list.append(relationship[0])
        if return_list:
            return return_list[0]
        return None

    def get_existing_sisters(self, person: Person) -> list[Person]:
        return_list = []
        for relationship in self.get_relationship_type_list(person, types = "Sister"):
            return_list.append(relationship[0])
        return return_list
