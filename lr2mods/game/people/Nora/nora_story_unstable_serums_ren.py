#Use this file to test Story_Step and Story_Path commands for Nora's short Unstable Serums Questline
#This story path is exclusive to Nora

from __future__ import annotations
from game.major_game_classes.serum_related.SerumTrait_ren import list_of_traits
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.character_related.Story_ren import Story_Step, Story_Path
from game.major_game_classes.serum_related.serums._nora_serum_traits_ren import nora_unstable_slut_trait, nora_unstable_obedience_trait, nora_unstable_love_trait, nora_unstable_happiness_trait, nora_unstable_energy_trait

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
clothing_fade = None
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 5 python:
"""

### Unstable Serums Research Path ###
# This path is a supplementary procedure for adding Nora's Unstable Serums to the game.
# Planned for 4 total steps.

# Step 0

# Actions:
#None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_unstable_serum_story_0_init(person: Person):
    list_of_traits.append(nora_unstable_slut_trait)
    return True

def nora_unstable_serum_story_0_finish(person: Person):
    return True

def nora_unstable_serum_story_0_cheat_to(person: Person):
    list_of_traits.append(nora_unstable_slut_trait)

def nora_unstable_serum_story_0_cheat_past(person: Person):
    list_of_traits.append(nora_unstable_slut_trait)

def nora_unstable_serum_story_0_remove(person: Person):
    list_of_traits.remove(nora_unstable_slut_trait)

def nora_unstable_serum_story_0_progress(person: Person, complete: bool):
    if complete:
        return "The Unstable Libido Enhancer serum trait is available."
    if nora_unstable_slut_trait.mastery_level >= 10:
        return "Talk to [nora.fname] about your research of the Unstable Libido Enhancer at the bar on Saturday night."
    else:
        return "Research the Unstable Libido Enhancer to at least 10%% mastery."
    return "Error"

nora_unstable_serum_story_0_step = Story_Step(nora_unstable_serum_story_0_init, nora_unstable_serum_story_0_finish,
                                          nora_unstable_serum_story_0_cheat_to, nora_unstable_serum_story_0_cheat_past,
                                          nora_unstable_serum_story_0_remove, nora_unstable_serum_story_0_progress)

# Step 1

# Actions:
#None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_unstable_serum_story_1_init(person: Person):
    list_of_traits.append(nora_unstable_obedience_trait)
    return True

def nora_unstable_serum_story_1_finish(person: Person):
    return True

def nora_unstable_serum_story_1_cheat_to(person: Person):
    list_of_traits.append(nora_unstable_obedience_trait)

def nora_unstable_serum_story_1_cheat_past(person: Person):
    list_of_traits.append(nora_unstable_obedience_trait)

def nora_unstable_serum_story_1_remove(person: Person):
    list_of_traits.remove(nora_unstable_obedience_trait)

def nora_unstable_serum_story_1_progress(person: Person, complete: bool):
    if complete:
        return "The Unstable Obedience Enhancer serum trait is available."
    if nora_unstable_obedience_trait.mastery_level >= 10:
        return "Talk to [nora.fname] about your research of the Unstable Obedience Enhancer at the bar on Saturday night."
    return "Research the Unstable Obedience Enhancer to at least 10%% mastery."

nora_unstable_serum_story_1_step = Story_Step(nora_unstable_serum_story_1_init, nora_unstable_serum_story_1_finish,
                                          nora_unstable_serum_story_1_cheat_to, nora_unstable_serum_story_1_cheat_past,
                                          nora_unstable_serum_story_1_remove, nora_unstable_serum_story_1_progress)

# Step 2

# Actions:
#None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_unstable_serum_story_2_init(person: Person):
    list_of_traits.append(nora_unstable_love_trait)
    return True

def nora_unstable_serum_story_2_finish(person: Person):
    return True

def nora_unstable_serum_story_2_cheat_to(person: Person):
    list_of_traits.append(nora_unstable_love_trait)

def nora_unstable_serum_story_2_cheat_past(person: Person):
    list_of_traits.append(nora_unstable_love_trait)

def nora_unstable_serum_story_2_remove(person: Person):
    list_of_traits.remove(nora_unstable_love_trait)

def nora_unstable_serum_story_2_progress(person: Person, complete: bool):
    if complete:
        return "The Unstable Love Enhancer serum trait is available."
    if nora_unstable_love_trait.mastery_level >= 10:
        return "Talk to [nora.fname] about your research of the Unstable Love Enhancer at the bar on Saturday night."
    return "Research the Unstable Love Enhancer to at least 10%% mastery."

nora_unstable_serum_story_2_step = Story_Step(nora_unstable_serum_story_2_init, nora_unstable_serum_story_2_finish,
                                          nora_unstable_serum_story_2_cheat_to, nora_unstable_serum_story_2_cheat_past,
                                          nora_unstable_serum_story_2_remove, nora_unstable_serum_story_2_progress)

# Step 3
# Final Step

# Actions:
#None! These are all a part of Nora's weekly meetings.

# Step Functions

def nora_unstable_serum_story_3_init(person: Person):
    list_of_traits.append(nora_unstable_happiness_trait)
    list_of_traits.append(nora_unstable_energy_trait)
    return True

def nora_unstable_serum_story_3_finish(person: Person):
    return True

def nora_unstable_serum_story_3_cheat_to(person: Person):
    list_of_traits.append(nora_unstable_happiness_trait)
    list_of_traits.append(nora_unstable_energy_trait)

def nora_unstable_serum_story_3_cheat_past(person: Person):
    list_of_traits.append(nora_unstable_happiness_trait)
    list_of_traits.append(nora_unstable_energy_trait)

def nora_unstable_serum_story_3_remove(person: Person):
    list_of_traits.remove(nora_unstable_happiness_trait)
    list_of_traits.remove(nora_unstable_energy_trait)

def nora_unstable_serum_story_3_progress(person: Person, complete: bool):
    return "Research the Unstable Energy Enhancer and Unstable Happiness Enhancer are both available.\nThis is the end of this story path."


nora_unstable_serum_story_3_step = Story_Step(nora_unstable_serum_story_3_init, nora_unstable_serum_story_3_finish,
                                          nora_unstable_serum_story_3_cheat_to, nora_unstable_serum_story_3_cheat_past,
                                          nora_unstable_serum_story_3_remove, nora_unstable_serum_story_3_progress)

def nora_unstable_serum_path_req():
    return mc.business.research_tier >= 1

nora_story_path_unstable_serum = Story_Path("Unstable Serums",
    [nora_unstable_serum_story_0_step, nora_unstable_serum_story_1_step, nora_unstable_serum_story_2_step, nora_unstable_serum_story_3_step],
    False,
    nora_unstable_serum_path_req,
    "Reach Tier 1 research at your business, then talk to Nora at your Saturday night meetup.")
