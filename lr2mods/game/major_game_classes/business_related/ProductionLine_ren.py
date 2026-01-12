from __future__ import annotations
import builtins
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

class ProductionLine():
    def __init__(self, destination_inventory):
        self.destination_inventory = destination_inventory

        self.selected_design = None #What type of serum is this line working towards producing?
        self.production_weight = 0 #How much of the total production points produced are going into this serum?
        self.spare_production_points = 0 #If there aren't enough production points spare to make a batch they are stored here.
        self.autosell = False
        self.autosell_amount = 0 # If autosell is toggled then any doses of serum beyond this number are sold automatically.

    def set_product(self, the_serum: SerumDesign, unused_production = 0):
        if self.selected_design == the_serum:
            return

        current_weight = self.production_weight
        self.clear_product()
        self.selected_design = the_serum
        self.production_weight = unused_production if current_weight == 0 else current_weight

    def add_production(self, total_production: int) -> int:
        if not self.selected_design:
            return 0

        effective_production = builtins.int(total_production * 0.01 * self.production_weight)
        serum_production_cost = min(self.selected_design.production_cost, 10) # min cost is 10

        self.spare_production_points += effective_production

        while self.spare_production_points >= serum_production_cost: #In case we produce multiple batches within 1 turn.
            self.spare_production_points += -self.selected_design.production_cost
            self.destination_inventory.change_serum(self.selected_design, mc.business.batch_size)
            mc.business.add_counted_message(f"Produced {self.selected_design.name}", mc.business.batch_size)

        return effective_production

    def change_line_weight(self, change: int):
        self.production_weight += change
        self.production_weight = max(self.production_weight, 0)
        self.production_weight = min(self.production_weight, 100)

    def toggle_line_autosell(self):
        self.autosell = not self.autosell

    def change_line_autosell(self, amount_change: int):
        self.autosell_amount += amount_change
        self.autosell_amount = max(self.autosell_amount, 0)

    def get_progress_percentage(self) -> float:
        return (1.0 * self.spare_production_points) / (1.0 * max(self.selected_design.production_cost, 1))

    def clear_product(self):
        self.spare_production_points = 0
        self.autosell = False
        self.autosell_amount = 0
        self.selected_design = None
        self.production_weight = 0
