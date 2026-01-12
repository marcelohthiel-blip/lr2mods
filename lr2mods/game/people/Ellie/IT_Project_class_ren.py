from __future__ import annotations
from game.bugfix_additions.mapped_list_ren import generate_identifier
from game.helper_functions.list_functions_ren import all_IT_projects
from game.major_game_classes.business_related.Policy_ren import Policy, mc
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -8 python:
"""


def IT_proj_generic_req_True() -> bool:
    return True

def IT_proj_test_req_False() -> bool:
    return False

class IT_Project(Policy):
    @staticmethod
    def get_by_identifier(identifier: int) -> IT_Project:
        return next((x for x in all_IT_projects() if x.identifier == identifier), None)

    def __init__(self, name, desc, cost = 0, requirement = None, toggleable = False,
            on_buy_function = None, extra_arguments = None, on_apply_function = None, on_remove_function = None, on_turn_function = None, on_move_function = None, on_day_function = None, dependant_policies = None,
            project_progress = 0, project_cost = 100, category = "", tier = 0):

        if requirement is None:
            requirement = IT_proj_generic_req_True

        super().__init__(name, desc, cost, requirement, toggleable = toggleable,
            on_buy_function = on_buy_function, extra_arguments = extra_arguments, on_apply_function = on_apply_function, on_remove_function = on_remove_function,
            on_turn_function = on_turn_function, on_move_function = on_move_function, on_day_function = on_day_function, dependant_policies = dependant_policies)

        self.project_progress = project_progress
        self.project_cost = project_cost
        self.category = category
        self.tier = tier
        self.identifier = generate_identifier((self.name, self.category))

    def __eq__(self, other: IT_Project) -> bool:
        if not isinstance(other, IT_Project):
            return NotImplemented
        return (self.category, self.name) == (other.category, other.name)

    def apply_policy(self):
        mc.business.active_IT_projects.append(self)
        if self.on_apply_function is not None:
            self.on_apply_function(**self.extra_arguments)

    def remove_policy(self):
        if self in mc.business.active_IT_projects:
            mc.business.active_IT_projects.remove(self)
            if self.on_remove_function is not None:
                self.on_remove_function(**self.extra_arguments)

    def buy_policy(self, ignore_cost = False):  #Only use this function if an IT Project can be outright bought.
        mc.business.IT_projects.append(self)
        if not ignore_cost:
            mc.business.funds -= self.cost
        if self.on_buy_function is not None:
            self.on_buy_function(**self.extra_arguments)
