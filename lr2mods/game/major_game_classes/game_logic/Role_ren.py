from __future__ import annotations
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.major_game_classes.game_logic.ActionList_ren import ActionList, Action
from game.major_game_classes.character_related.Person_ren import Person

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -5 python:
"""
class Role(): #Roles are assigned to special people. They have a list of actions that can be taken when you talk to the person and acts as a flag for special dialogue options.
    def __init__(self, role_name, actions = None, hidden = False, on_turn = None, on_move = None, on_day = None, role_dates = None, looks_like = None, role_trainables = None, internet_actions = None):
        self.role_name = role_name
        self.actions = ActionList(actions)
        self.internet_actions = ActionList(internet_actions)

        # At some point we may want a separate list of role actions that are available when you text someone.
        self.hidden = hidden #A hidden role is not shown on the "Roles" list
        self.on_turn = on_turn #A function that is run each turn on every person with this Role.
        self.on_move = on_move #A function that is run each move phase on every person with this Role.
        self.on_day = on_day

        if role_dates is None:
            self.role_dates = [] # A role date is an action that should be added to the list of date triggers.
        elif isinstance(role_dates, list):
            self.role_dates = role_dates
        else:
            self.role_dates = [role_dates]

        self.linked_roles = [] #A list of other roles. If this role is removed, all linked roles are removed as well.
        self.looks_like = None
        if isinstance(looks_like, Role):
            self.looks_like = looks_like

        if role_trainables is None: #Trainable entries added when a girl is in a trance.
            self.role_trainables = []
        elif isinstance(role_trainables, list):
            self.role_trainables = role_trainables
        else:
            self.role_trainables = [role_trainables]
        self.identifier = generate_identifier(
            tuple(role_name) +
            tuple(self.actions)
        )

    def __hash__(self) -> int:
        return self.identifier

    def __eq__(self, other: Role) -> bool:
        if not isinstance(other, Role):
            return NotImplemented
        return self.identifier == other.identifier

    @property
    def parent_role(self) -> Role:
        return self.looks_like

    def check_parent_role(self, role: Role | str):
        if not self.parent_role:
            return False
        if isinstance(role, str):
            return self.parent_role.role_name == role or self.parent_role.check_parent_role(role)
        if isinstance(role, Role):
            return self.parent_role == role or self.parent_role.check_parent_role(role)
        return False

    def run_turn(self, person: Person):
        if self.on_turn is not None:
            self.on_turn(person)

    def run_move(self, person: Person):
        if self.on_move is not None:
            self.on_move(person)

    def run_day(self, person: Person):
        if self.on_day is not None:
            self.on_day(person)

    def link_role(self, role: Role) -> None:
        if role not in self.linked_roles:
            self.linked_roles.append(role)

    def add_action(self, action: Action):
        self.actions.add_action(action)

    def remove_action(self, action: Action):
        self.actions.remove_action(action)

    def has_action(self, action: Action | str) -> bool:
        return self.actions.has_action(action) or self.internet_actions.has_action(action)

    def add_internet_action(self, action: Action):
        self.internet_actions.add_action(action)

    def remove_internet_action(self, action: Action):
        self.internet_actions.remove_action(action)
