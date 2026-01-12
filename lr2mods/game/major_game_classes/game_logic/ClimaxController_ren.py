from __future__ import annotations
import renpy
from game.bugfix_additions.debug_info_ren import write_log
from game.major_game_classes.character_related.Person_ren import Person, mc

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

class ClimaxController(): #A class that allows for the easy formatting and menu display of sex climax options.
    climax_type_dict = {
        "masturbation": 0.5,
        "air": 0.75, #ie a girl gets you off somehow, but you cum into open air/the floor/yourself
        "body": 1.0, #Generic bodyshot. Stomach or ass, normally.
        "face": 1.25, #Onto her face, but not explicitly her mouth
        "tits": 1.25, #You already know what these are.
        "mouth": 1.5, #Cum into her mouth explicitly. Bonus for her swallowing?
        "pussy": 2.0, #Creampie. Knocked down to 1.5x if you're wearing a condom.
        "anal": 2.0, #Butt-pie? Does this have some sexy name I don't know about?
        "throat": 2.0, #Throatpie. Down the hatch!
        "threesome": 3.0 #Threesomes rule
    }

    def __init__(self, *args): #Each argument provided should be a list of "display_name" and the climax type that should be associated with that climax
        self.selected_climax_type = None #Set when the player selects a return value, lets us call run_climax() at the correct moment later.
        self.climax_options = args

    @staticmethod
    def get_climax_multiplier(climax_type):
        multiplier = ClimaxController.climax_type_dict.get(climax_type, 1.0)
        if mc.condom and not mc.has_removed_condom and climax_type in ("pussy", "anal"):
            multiplier -= 0.5

        return multiplier

    def set_climax_type(self, climax_type):
        self.selected_climax_type = climax_type

    def show_climax_menu(self):
        display_list = []
        for climax_option in self.climax_options:
            display_name = climax_option[0]
            climax_type = climax_option[1]
            if climax_type in ClimaxController.climax_type_dict:
                enhanced = [display_name]
                enhanced.append("{size=20}{color=#29B6F6}\n")
                enhanced.append(f"x{self.get_climax_multiplier(climax_type):.2f} Clarity Produced")
                enhanced.append("{/color}{/size}")
                enhanced.append(" (tooltip)All Locked Clarity is released when you climax. How much Clarity is produced varies depending on how you cum, and it's possible to have a multiplier greater than 1!")
                display_name = "".join(enhanced)
            else:
                climax_option = "masturbation"
            display_list.append((display_name, climax_option))

        if len(display_list) == 1: # When there is only one option, don't bother with the menu
            selected = display_list[0][1]
        else:
            selected = renpy.exports.display_menu(display_list, screen = "choice")

        if not selected:
            self.set_climax_type("masturbation")
            return ""

        self.set_climax_type(selected[1])
        return selected[0] #Returns the display string so an event can flow to the appropriate branch

    def do_clarity_release(self, person: Person | None = None, add_to_log = True):
        multiplier = ClimaxController.get_climax_multiplier(self.selected_climax_type)
        if person:
            mc.convert_locked_clarity(multiplier, with_novelty = person.novelty)
            person.change_novelty(-5, add_to_log = add_to_log)
        else:
            mc.convert_locked_clarity(multiplier, with_novelty = mc.masturbation_novelty)
            mc.change_masturbation_novelty(-5, add_to_log = False)
        mc.reset_arousal()

    @staticmethod
    def manual_clarity_release(climax_type = "masturbation", person: Person | None = None, add_to_log = True):
        multiplier = ClimaxController.get_climax_multiplier(climax_type)

        if climax_type != "masturbation" and person is None:
            write_log(f"Error: called manual clarity release with {climax_type} without passing a person parameter.")
            return

        if person:
            mc.convert_locked_clarity(multiplier, with_novelty = person.novelty, add_to_log = add_to_log)
            person.change_novelty(-5, add_to_log = add_to_log)
        else:
            mc.convert_locked_clarity(multiplier, with_novelty = mc.masturbation_novelty)
            mc.change_masturbation_novelty(-5, add_to_log = False)
        mc.reset_arousal()
