from game.major_game_classes.character_related.Person_ren import Person, mc, nora, stephanie
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Room_ren import downtown_bar
from game.sex_positions._position_definitions_ren import blowjob

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 12
day = 0
time_of_day = 0
"""renpy
init 5 python:
"""

###################
#   Love Events   #
###################






###################
#   Lust Events   #
###################






###################
# Obedience Events#
###################



###################
#   Other Events  #
###################

#Event located in nora/nora_other_events.rpy
def stephanie_first_bar_date_followup_requirement(person):
    return person.is_at_work

def add_stephanie_first_bar_date_followup_action():
    stephanie.add_unique_on_room_enter_event(
        Action("One Night Stand Followup", stephanie_first_bar_date_followup_requirement, "stephanie_first_bar_date_followup_label")
    )
    return


