from __future__ import annotations
import builtins
import renpy
from game.general_actions.interaction_actions.chat_actions_definition_ren import demand_panties_requirement
from game.helper_functions.convert_to_string_ren import remove_display_tags
from game.major_game_classes.character_related.Person_ren import Person
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.game_logic.Action_ren import Action
from game.game_loops.sexmechanic_code_ren import apply_sex_modifiers, clear_sex_modifiers

day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""
def build_wardrobe_change_menu(person: Person) -> list[str | list[str]]:
    return list(
        filter(
            None,
            [
                "Choose",
                ["Modify her wardrobe", "wardrobe"],
                ["Change her base outfit", "makeup"],
                ["Wear an outfit right now", "wear"] if len(person.wardrobe.outfit_sets) > 0 else None,
                ["Wear stockings", "stockings"] if person.obedience > 140 and not person.has_thigh_high_socks else None,
                ["Back", "back"],
            ],
        ),
    )

def build_title_selection_menu(person: Person) -> list[list]:
    person_titles: list[str | list[list | str]] = [[title, [0, title]] for title in person.get_titles()]
    mc_titles: list[str | list[list | str]] = [[title, [1, title]] for title in person.get_player_titles()]
    person_possessive_titles: list[str | list[list | str]] = [[title, [2, title]] for title in person.get_possessive_titles()]

    person_titles.insert(0, "Their Title")
    mc_titles.insert(0, "Your Title")
    person_possessive_titles.insert(0, "Possessive Title")

    return [person_titles, mc_titles, person_possessive_titles]

def build_her_title_selection_menu(person: Person) -> list[str]:
    person_titles = list(person.get_titles())
    person_titles.insert(0, "Her Title")
    return [person_titles]

def demand_strip_tits_requirement(person: Person) -> bool | str:
    if person.tits_visible:
        return False #Can't strip if they're already visible
    if person.obedience < 140:
        return "Requires: 140 Obedience"
    return builtins.len(person.outfit.get_tit_strip_list()) > 0

def demand_strip_underwear_requirement(person: Person) -> bool | str:
    if person.tits_visible or person.vagina_visible:
        return False #Can't strip if we're already past underwear
    if person.outfit.are_panties_visible and person.outfit.is_bra_visible:
        return False #Can't strip if we can already see all of her underwear.
    if person.obedience < 130:
        return "Requires: 130 Obedience"
    return True

def demand_strip_naked_requirement(person: Person) -> bool | str:
    if person.tits_visible and person.vagina_visible:
        return False
    if person.obedience < 150:
        return "Requires: 150 Obedience"
    return builtins.len(person.outfit.get_full_strip_list(strip_feet = False)) > 0

def demand_strip_get_obedience_req(person: Person, outfit: Outfit, min_obedience = 100, private = False) -> int:
    obedience_req = outfit.outfit_slut_score - person.effective_sluttiness() / 2
    obedience_req -= (person.opinion.showing_her_tits * 3)
    obedience_req -= (person.opinion.showing_her_ass * 3)

    if private:
        obedience_req /= 2  # privacy reduces obedience requirements

    return builtins.max(min_obedience, builtins.int(builtins.round(100 + obedience_req, -1)))

def demand_strip_judge_public(person: Person, outfit: Outfit, opinion: str) -> bool:
    apply_sex_modifiers(person, False)
    judge = person.judge_outfit(outfit, temp_sluttiness_boost = -10 + 5 * person.opinion(opinion))
    clear_sex_modifiers(person)
    return judge

def demand_strip_judge_private(person: Person, outfit: Outfit, opinion: str) -> bool:
    apply_sex_modifiers(person) # quickly add and remove modifiers to get that sweet, sweet love bonus
    judge = person.judge_outfit(outfit, temp_sluttiness_boost = 5 * person.opinion(opinion))
    clear_sex_modifiers(person)
    return judge

def strip_description_possessive_title(person: Person) -> str:
    possessive_title = remove_display_tags(person.possessive_title)
    return person.create_formatted_title(possessive_title.capitalize())

def build_demand_strip_menu(person: Person) -> list[str | Action | list]:
    demand_panties_action = Action("Give me your panties   {energy=-5}", demand_panties_requirement, "demand_panties_label", args = person, requirement_args = person,
        menu_tooltip = f"Ask {person.display_name} to hand over her panties.")
    demand_strip_underwear_action = Action("Strip to your underwear   {energy=-5}", demand_strip_underwear_requirement, "demand_strip_underwear_label", args = person, requirement_args = person,
        menu_tooltip = "Have her strip down until she's only in her underwear.")
    demand_strip_tits_action = Action("Get your tits out   {energy=-5}", demand_strip_tits_requirement, "demand_strip_tits_label", args = person, requirement_args = person,
        menu_tooltip = "Have her strip down until you can see her tits.")
    demand_strip_naked_action = Action("Get naked   {energy=-5}", demand_strip_naked_requirement, "demand_strip_naked_label", args = person, requirement_args = person,
        menu_tooltip = "Have her strip until she is completely naked.")

    return ["Strip Command", demand_panties_action, demand_strip_underwear_action, demand_strip_tits_action, demand_strip_naked_action, ["Never mind", "Return"]]

def top_strip_description(person: Person, strip_list: list[Clothing]) -> None:
    for item_to_strip in strip_list:
        person.draw_animated_removal(item_to_strip)
        if item_to_strip == strip_list[-1]: #Special line for the last item.
            if person.has_large_tits:
                renpy.say(None, f"She pulls off her {item_to_strip.display_name}, letting her tits spill out.")
            else:
                renpy.say(None, f"She pulls off her {item_to_strip.display_name}, revealing her cute tits.")
        else:
            renpy.pause(1)

def underwear_strip_description(person: Person) -> None:
    cloth = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
    while cloth is not None and (person.outfit.bra_covered or (cloth.has_extension and not cloth.underwear)):
        person.draw_animated_removal(cloth)
        cloth = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)

    cloth = person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
    while cloth is not None and (person.outfit.panties_covered or (cloth.is_extension and not cloth.underwear)):
        person.draw_animated_removal(cloth)
        if person.underwear_visible:
            renpy.say(None, f"{strip_description_possessive_title(person)} strips off her {cloth.display_name}, leaving her wearing only her underwear.")
        cloth = person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)

def naked_strip_description(person: Person) -> None:
    cloth = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
    while cloth is not None and not person.tits_visible:
        person.draw_animated_removal(cloth)
        if person.tits_visible:
            renpy.say(None, f"{strip_description_possessive_title(person)} pulls her tits out from her {cloth.display_name}, putting them on display for you.")
        cloth = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)

    if not person.tits_visible:
        renpy.say(None, f"{strip_description_possessive_title(person)} looks at you, you just nod, indicating she should continue.")

    cloth = person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
    while cloth is not None and not person.vagina_visible:
        person.draw_animated_removal(cloth)
        if person.vagina_visible:
            renpy.say(None, f"{strip_description_possessive_title(person)} peels off her {cloth.display_name}, revealing her cute little pussy.")
        cloth = person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)

    if not person.vagina_visible:
        renpy.say(None, f"{strip_description_possessive_title(person)} looks at you, you motion her to keep going.")

    # special case where the item is a two part item and did not get removed from the first upper run
    cloth = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
    while cloth is not None and not person.tits_visible:
        person.draw_animated_removal(cloth)
        if person.tits_visible and person.vagina_visible:
            renpy.say(None, f"{strip_description_possessive_title(person)} takes of her {cloth.display_name}, displaying her naked body to you.")
        cloth = person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)


def generalised_strip_description(person: Person, strip_list: list[Clothing], half_off_instead = False, position = "default") -> None:
    # This acts as a generic strip function that can be used in any scene. Hand over a list of clothing items to strip and this narrates it.
    # Note: half_off_instead assumes you are handing over a valid half_off list. Not sure what happens if you don't do that.

    if isinstance(strip_list, Clothing):
        strip_list = [strip_list] #Lets you hand over a single item to strip off.

    if not isinstance(strip_list, (list, tuple, set)) or len(strip_list) == 0:
        return

    outfit = person.outfit.get_copy() #Use a copy to keep track of what's changed between iterations, so we can narrate tits being out, ect.
    for cloth in strip_list:
        if not isinstance(cloth, Clothing):
            continue

        person.draw_animated_removal(cloth, half_off_instead = half_off_instead, position = position)

        if person.tits_available and not outfit.tits_available: #Tits are fully out
            if person.has_large_tits:
                if half_off_instead:
                    renpy.say(None, f"{person.display_name} pulls her {cloth.display_name} out of the way, letting her {person.tits_description} spill out.")
                else:
                    renpy.say(None, f"{person.display_name} pulls off her {cloth.display_name}, letting her {person.tits_description} spill out.")
            elif half_off_instead:
                renpy.say(None, f"{person.display_name} pulls her {cloth.display_name} aside and sets her {person.tits_description} free.")
            else:
                renpy.say(None, f"{person.display_name} takes off her {cloth.display_name} and sets her {person.tits_description} free.")
        elif person.tits_visible and not outfit.tits_visible: #Tits aren't out for use, but her clothing lets you get a good look.
            if person.has_large_tits:
                if half_off_instead:
                    renpy.say(None, f"{person.display_name} pulls her {cloth.display_name} aside, letting you get an eye full of the {person.tits_description} she had hidden away.")
                else:
                    renpy.say(None, f"{person.display_name} pulls off her {cloth.display_name}, and now you're able to get a good look at the {person.tits_description} she had hidden away.")
            elif half_off_instead:
                renpy.say(None, f"{person.display_name} pulls her {cloth.display_name} to the side, giving you a look at her cute {person.tits_description}.")
            else:
                renpy.say(None, f"{person.display_name} removes her {cloth.display_name}, and now you're able to see the cute {person.tits_description} she had hidden away.")
        elif person.vagina_available and not outfit.vagina_available: #Pussy is out in the open
            if cloth.underwear:
                if half_off_instead:
                    renpy.say(None, f"{person.display_name} slips her {cloth.display_name} to the side, exposing herself to you.")
                else:
                    renpy.say(None, f"{person.display_name} slips off her {cloth.display_name}, peeling it away from her {person.pubes_description} pussy.")
            elif half_off_instead:
                renpy.say(None, f"{person.display_name} pulls her {cloth.display_name} to the side, getting it out of the way of her pussy.")
            else:
                renpy.say(None, f"{person.display_name} takes off her {cloth.display_name} and reveals her {person.pubes_description} pussy underneath.")
        elif person.vagina_visible and not outfit.vagina_visible: #Pussy can be seen, but not touched yet
            if half_off_instead:
                renpy.say(None, f"{person.display_name} moves her {cloth.display_name}, letting you see her pussy.")
            else:
                renpy.say(None, f"{person.display_name} takes off her {cloth.display_name}, letting you see her {person.pubes_description} pussy.")

        else:
            rand = renpy.random.randint(0, 3) #Add some random variants so it's not always the same.
            if rand == 0:
                if half_off_instead:
                    renpy.say(None, f"{person.display_name} slides her {cloth.display_name} away.")
                else:
                    renpy.say(None, f"{person.display_name} strips out of her {cloth.display_name}.")
            elif rand == 1:
                if half_off_instead:
                    renpy.say(None, f"{person.display_name} moves her {cloth.display_name}.")
                else:
                    renpy.say(None, f"{person.display_name} takes off her {cloth.display_name}.")
            elif rand == 2:
                if half_off_instead:
                    renpy.say(None, f"{person.display_name} shifts her {cloth.display_name} so it's not in the way.")
                else:
                    renpy.say(None, f"{person.display_name} slips her {cloth.display_name} off.")
            elif half_off_instead:
                renpy.say(None, f"{person.display_name} pulls her {cloth.display_name} out of the way.")
            else:
                renpy.say(None, f"{person.display_name} pulls off her {cloth.display_name}.")

        if half_off_instead:
            outfit.half_off_clothing(cloth)
        else:
            outfit.remove_clothing(cloth) #Update our test outfit.
