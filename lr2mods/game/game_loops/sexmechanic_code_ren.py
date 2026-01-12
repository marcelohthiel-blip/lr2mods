from __future__ import annotations
from itertools import chain
from typing import Any, Callable
import renpy
from game.helper_functions.misc_helpers_ren import call_global_func, has_global_func
from game.random_lists_ren import get_random_from_weighted_list, get_random_from_list
from game.game_roles._role_definitions_ren import mother_role, sister_role, hypno_orgasm_role
from game.game_roles.relationship_role_definition_ren import add_caught_affair_cheating_action, add_caught_cheating_action
from game.main_character.mc_serums._mc_serum_definitions_ren import mc_serum_aura_obedience, mc_serum_feat_orgasm_control
from game.main_character.perks.Perks_ren import perk_system
from game.major_game_classes.game_logic.RoomObject_ren import RoomObject
from game.major_game_classes.character_related._job_definitions_ren import prostitute_job
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.clothing_related.Clothing_ren import Clothing
from game.sex_positions._position_definitions_ren import Position, list_of_positions, prone_bone, prone_anal, list_of_girl_positions, spanking, cunnilingus, cowgirl_cunnilingus, standing_finger, standing_grope, standing_oral, standing_cunnilingus, kissing, handjob, blowjob, deepthroat, skull_fuck, tit_fuck, sarah_tit_fuck, sixty_nine, drysex_cowgirl
from game.sex_positions.conditions.Condition_ren import Condition_Type
from game.sex_positions.threesome.Threesome_Position_ren import willing_to_threesome

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 1 python:
"""

foreplay_giving_positions = [kissing, standing_finger, standing_grope]
foreplay_receiving_positions = [handjob, tit_fuck, kissing]
oral_giving_positions = [cunnilingus, standing_oral, sixty_nine]
oral_receiving_positions = [blowjob, deepthroat, skull_fuck, sixty_nine]

def girl_choose_position(person: Person, ignore_taboo = False):
    extra_positions = []
    # when she enjoys blow jobs, add one to her choices (to prevent always going to blowjob variant)
    if person.oral_sex_skill >= 5 and person.opinion.giving_blowjobs > 1 and person.is_submissive:
        extra_positions.append(skull_fuck)
    elif person.oral_sex_skill > 3 and person.opinion.giving_blowjobs > 1:
        extra_positions.append(deepthroat)
    elif person.oral_sex_skill > 2 and person.opinion.giving_blowjobs > 0:
        extra_positions.append(blowjob)
    if person.foreplay_sex_skill > 2 and person.opinion.giving_tit_fucks > 1:
        extra_positions.append(tit_fuck)

    position_option_list = []
    for position in chain(list_of_girl_positions, extra_positions):
        if person.allow_position(position) and mc.location.has_object_with_trait(position.requires_location):
            if position.her_position_willingness_check(person, ignore_taboo = ignore_taboo):
                position_option_list.append((position, person.sex_skills[position.skill_tag] + 1))

    if len(position_option_list) == 0:  # we have an empty list, revert to cowgirl dry humping
        return drysex_cowgirl

    return get_random_from_weighted_list(position_option_list)

def girl_choose_object(person: Person, position: Position) -> RoomObject | None:
    if position is None:
        return None

    possible_object_list = [x for x in mc.location.objects_with_trait(position.requires_location)]

    picked_object = get_random_from_list(possible_object_list)

    if isinstance(picked_object, RoomObject):
        return picked_object
    return None

def cheating_check_get_watcher(person: Person, position: Position) -> Person | None:
    # skip cheating check when person is Office Free Use Slut
    if not person.is_free_use:
        # only check if she is jealous and not willing to threesome with the girl
        for other_person in (y for y in (x for x in mc.location.people if x != person) if not y.in_harem and y.is_jealous and not willing_to_threesome(person, y)):
            if other_person.is_girlfriend and position.slut_requirement > (other_person.sluttiness * .6) + ((other_person.opinion.threesomes + other_person.opinion.polyamory + other_person.opinion.public_sex) * 5): #You can get away with 60% as slutty as she would do +- threesome inclination / public sex
                if not other_person.has_queued_event("caught_cheating_label"):
                    add_caught_cheating_action(person, other_person)
                    renpy.say(None, f"{other_person.display_name} gasps when she sees what you and {person.display_name} are doing and storms off.")
                    other_person.change_location(other_person.home)

            elif other_person.is_affair and position.slut_requirement > (other_person.sluttiness * .8) + ((other_person.opinion.threesomes + other_person.opinion.polyamory + other_person.opinion.public_sex) * 5): #You can get away with 80% as slutty as she would do +- threesome inclination / public sex
                if not other_person.has_queued_event("caught_affair_cheating_label"):
                    add_caught_affair_cheating_action(person, other_person)
                    renpy.say(None, f"{other_person.display_name} gasps when she sees what you and {person.display_name} are doing and storms off.")
                    other_person.change_location(other_person.home)

    # get watcher from remaining people
    watcher = get_random_from_list([x for x in mc.location.people if x != person])
    if watcher:
        if watcher.opinion.public_sex > 0:
            watcher.add_situational_slut("public sex watcher", 5 * watcher.opinion.public_sex, "They're doing it right in front of me! That's so fucking hot!")
        elif watcher.opinion.public_sex < 0:
            watcher.add_situational_slut("public sex watcher", 5 * watcher.opinion.public_sex, "Right here in front of me?! That's disgusting!")
        if watcher.is_at_stripclub:
            watcher.add_situational_slut("at stripclub", 20, "I always get turned on at a strip club")

        # Perk Modifiers
        if perk_system.has_ability_perk("Serum: Aura of Compliance"):
            if mc_serum_aura_obedience.trait_tier == 2:
                watcher.add_situational_obedience("aura", 10, "He has an overpowering aura about him...")
            elif mc_serum_aura_obedience.trait_tier >= 3:
                watcher.add_situational_obedience("aura", 20, "His aura is overpowering!")
    return watcher #Get a random person from the people in the area, if there are any.

def apply_sex_modifiers(person: Person, private: bool = True):
    #Family situational modifiers
    if person.has_family_taboo: #Check if any of the roles the person has belong to the list of family roles.
        person.add_situational_slut("taboo_sex", -20, "We're related, we shouldn't be doing this.")

    #Cheating modifiers
    person.discover_opinion("cheating on men")
    if person.has_job(prostitute_job):
        person.add_situational_slut("cheating", 20, "Prostitutes don't care about cheating")
    elif person.relationship == "Girlfriend":
        if person.opinion.cheating_on_men > 0:
            person.add_situational_slut("cheating", person.opinion.cheating_on_men * 5, "I'm cheating on my boyfriend!")
        elif person.opinion.cheating_on_men < 0:
            person.add_situational_slut("cheating", person.opinion.cheating_on_men * 10, "I can't cheat on my boyfriend!")
    elif person.relationship == "Fiancée":
        if person.opinion.cheating_on_men > 0:
            person.add_situational_slut("cheating", person.opinion.cheating_on_men * 8, "I'm cheating on my fiancé!")
        elif person.opinion.cheating_on_men < 0:
            person.add_situational_slut("cheating", person.opinion.cheating_on_men * 15, "I could never cheat on my fiancé!")
    elif person.relationship == "Married":
        if person.opinion.cheating_on_men > 0:
            person.add_situational_slut("cheating", person.opinion.cheating_on_men * 10, "I'm cheating on my husband!")
        elif person.opinion.cheating_on_men < 0:
            person.add_situational_slut("cheating", person.opinion.cheating_on_men * 20, "I could never cheat on my husband!")

    #Privacy modifiers
    if not private:
        if person.sluttiness < 50:
            person.add_situational_slut("public_sex", -10 + person.opinion.public_sex * 5, "There are people watching...")
        else:
            person.add_situational_slut("public_sex", person.opinion.public_sex * 5, "There are people watching!")

    slut_multiplier = (95 - person.sluttiness) / 100.0 # last 5 sluttiness no extra modifiers
    if slut_multiplier > 0:
        #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.
        if person.love < 0:
            person.add_situational_slut("love_modifier", int((person.love / 4.0) * slut_multiplier), "I hate you, get away from me!")
        elif private:
            if person.is_girlfriend: #Girlfriend and affairs gain full Love
                person.add_situational_slut("love_modifier", int((person.love / 2.0) * slut_multiplier), "You're my special someone, I love you!")
            elif person.is_affair:
                person.add_situational_slut("love_modifier", int((person.love / 2.0) * slut_multiplier), "I have kept it a secret, but I love you!")
            elif person.has_family_taboo: #Family now only gains 1/4 (but this now helps offset the taboo penalty)
                if person.has_role(mother_role):
                    person.add_situational_slut("love_modifier", int((person.love / 4.0) * slut_multiplier), "Even if it's wrong, a mother should do everything she can for her son!")
                elif person.has_role(sister_role):
                    person.add_situational_slut("love_modifier", int((person.love / 4.0) * slut_multiplier), "I love my brother, and even if it's wrong I want to be close to him!")
                else: #Generic family one
                    person.add_situational_slut("love_modifier", int((person.love / 4.0) * slut_multiplier), "I love you, even though we're related!")
            else: #If you aren't in a relationship with them only half their Love applies.
                person.add_situational_slut("love_modifier", int((person.love / 2.0) * slut_multiplier), "I really like you, let's see where this goes!")

        # Happiness modifiers
        happiness_effect = int(((person.happiness - 100) / 4.0) * slut_multiplier)
        if happiness_effect <= -10:
            person.add_situational_slut("happiness_modifier", happiness_effect, "I'm so unhappy, I just don't want to do anything!")
        elif happiness_effect <= -5:
            person.add_situational_slut("happiness_modifier", happiness_effect, "I'm just not in the mood right now.")
        elif happiness_effect >= 5:
            person.add_situational_slut("happiness_modifier", happiness_effect, "I'm so happy, I'm up for anything!")
        elif happiness_effect >= 10:
            person.add_situational_slut("happiness_modifier", happiness_effect, "Today's a good day, let's see where this goes!")

    # Perk Modifiers
    if perk_system.has_ability_perk("Serum: Aura of Compliance"):
        if mc_serum_aura_obedience.trait_tier == 2:
            person.add_situational_obedience("aura", 10, "He has an overpowering aura about him...")
        elif mc_serum_aura_obedience.trait_tier >= 3:
            person.add_situational_obedience("aura", 20, "His aura is overpowering!")

def clear_sex_modifiers(person: Person):
    # Teardown the sex modifiers
    person.clear_situational_slut("happiness_modifier")
    person.clear_situational_slut("love_modifier")
    person.clear_situational_slut("public_sex")
    person.clear_situational_slut("cheating")
    person.clear_situational_slut("taboo_sex")
    person.clear_situational_slut("aura")
    person.clear_situational_obedience("aura")

def pick_object(person: Person, position: Position, forced_object: RoomObject | None = None) -> RoomObject | None:
    if position is None:
        return None

    if forced_object:
        picked_object = forced_object
    else:
        object_option_list = [[x.formatted_name.capitalize(), x] for x in mc.location.objects if x.has_trait(position.requires_location)]

        # if we have only one object to pick for position, select it automatically (saves the user for selecting the only obvious choice)
        if not object_option_list:
            picked_object = renpy.random.choice(mc.location.objects)
        elif len(object_option_list) == 1:
            picked_object = object_option_list[0][1]
        else:
            picked_object = renpy.display_menu(object_option_list, True, "Choice")

    return picked_object

def build_round_choice_menu(person: Person, position: Position | None, position_locked: bool, room_object: RoomObject | None, ignore_taboo: bool = False, condition: Condition_Type = Condition_Type.default_condition(), allow_transitions: bool = True, hide_leave: bool = False):
    option_list = []
    option_list.append("Round Choices")
    if position is not None:
        option_list.append((f"Keep {position.verbing}\n{position.build_energy_arousal_line(person)}", "Continue")) #NOTE: you're prevented from continuing if the energy cost would be too high by the pre-round checks.

        if not position_locked and room_object:
            option_list.append(("Pause and change position\n-5 {image=arousal_token_small}", "Change"))
            for pos in position.connections:
                if allow_transitions and person.allow_position(pos) and not person.is_position_filtered(pos) and room_object.has_trait(pos.requires_location) and condition.filter_condition_positions(pos):
                    appended_name = f"Transition to {pos.build_position_willingness_string(person, ignore_taboo = ignore_taboo)}" #NOTE: clothing and energy checks are done inside build_position_willingness, invalid position marked (disabled)
                    option_list.append((appended_name, pos))

        if position_locked and room_object:
            # allow transition to positions with same traits and skill requirements
            for pos in position.connections:
                if isinstance(room_object, RoomObject): # Had an error with cousin's kissing blackmail where it would pass object_choice as a list, haven't looked further into it
                    if allow_transitions and person.allow_position(pos) and not person.is_position_filtered(pos) and room_object.has_trait(pos.requires_location) and pos.skill_tag == position.skill_tag and condition.filter_condition_positions(pos):
                        appended_name = f"Transition to {pos.build_position_willingness_string(person, ignore_taboo = ignore_taboo)}" #NOTE: clothing and energy checks are done inside build_position_willingness, invalid position marked (disabled)
                        option_list.append((appended_name, pos))

        if not person.outfit.has_full_access:
            option_list.append(("Pause and strip her down", "Strip"))

        if person.has_role(hypno_orgasm_role) and room_object is not None and not person.event_triggers_dict.get("hypno_orgasmed_recently", False):
            option_list.append(("Trigger an orgasm", "Hypno_Orgasm"))

        if perk_system.has_ability_perk("Serum: Feat of Orgasm Control") and mc_serum_feat_orgasm_control.trait_tier >= 2:
            option_list.append(("Orgasm Early", "early_orgasm"))

        if perk_system.has_ability_perk("Serum: Feat of Hypnotism") and not person.is_in_trance and mc.energy > 30:
            option_list.append(("Hypnotize Her", "hypnotize"))

        if not hide_leave: #TODO: Double check that we can always get out
            option_list.append((f"Stop {position.verbing} and leave", "Leave")) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

    else:
        if not position_locked:
            option_list.append(("Pick a new position\n-5 {image=arousal_token_small}", "Change"))
            if not person.outfit.has_full_access: # only show strip option if we can choose another position
                option_list.append(("Pause and strip her down", "Strip"))
        if not hide_leave:
            option_list.append(("Stop and leave", "Leave"))
    return option_list

def _character_position_filter(person: Person, position_type = "foreplay") -> Callable[[], bool]:
    def position_always_allowed(position: Position) -> bool:
        return True

    func_name = f"{person.func_name}_{position_type.lower()}_position_filter"
    if has_global_func(func_name):
        return globals()[func_name]
    return position_always_allowed

def apply_menu_position_filter(person: Person, positions: list[tuple[str, Position]], position_type: str = "foreplay") -> list[str, Position]:
    return [x for x in positions if _character_position_filter(person, position_type)(x[1])]

def apply_position_filter(person: Person, positions: list[Position], position_type: str = "foreplay") -> list[Position]:
    return [x for x in filter(_character_position_filter(person, position_type), positions)]

def build_grouped_sex_position_menu(person: Person, current_position: Position | None = None, ignore_taboo = False, prohibit_tags = [], condition = Condition_Type.default_condition()):
    def character_unique_sex_positions(person: Person, prohibit_tags: list[str] = []) -> list[tuple[Position, int]]:
        positions = default_unique_sex_positions(person, prohibit_tags)
        func_name = f"{person.func_name}_unique_sex_positions"
        if has_global_func(func_name):
            positions.extend(call_global_func(func_name, person, prohibit_tags))
        return positions

    def character_unlock_information(person: Person, position: str) -> Callable[[], str]:
        func_name = f"{person.func_name}_{position.lower()}_position_info"
        return call_global_func(func_name)

    positions = {
        "Foreplay": [],
        "Oral": [],
        "Vaginal": [],
        "Anal": []
    }
    for position in sorted(list_of_positions, key = lambda x: x.name):
        if position == current_position:
            continue
        if mc.location.has_object_with_trait(position.requires_location) and condition.filter_condition_positions(position): #There is a valid object and if it requires large tits she has them.
            if person.allow_position(position):
                willingness = position.build_position_willingness_string(person, ignore_taboo = ignore_taboo)
                if position.skill_tag not in prohibit_tags:
                    positions[position.skill_tag].append((willingness, position))
            else: # inform user that person hates position
                positions[position.skill_tag].append((position.build_position_rejection_string(person), position))

    # insert unique positions into choices
    for (position, insert_index) in character_unique_sex_positions(person, prohibit_tags):
        if position == current_position:
            continue
        if mc.location.has_object_with_trait(position.requires_location) and condition.filter_condition_positions(position): #There is a valid object and if it requires large tits she has them.
            if person.allow_position(position):
                willingness = position.build_position_willingness_string(person, ignore_taboo = ignore_taboo)
                if position.skill_tag not in prohibit_tags:
                    positions[position.skill_tag].insert(insert_index, [willingness, position])
            else:
                positions[position.skill_tag].insert(insert_index, [position.build_position_rejection_string(person), position])

    # filter positions
    positions["Foreplay"] = apply_menu_position_filter(person, positions["Foreplay"], "foreplay")
    positions["Oral"] = apply_menu_position_filter(person, positions["Oral"], "oral")
    positions["Vaginal"] = apply_menu_position_filter(person, positions["Vaginal"], "vaginal")
    positions["Anal"] = apply_menu_position_filter(person, positions["Anal"], "anal")

    for tag in ("Oral", "Vaginal", "Anal"):
        if not positions[tag]:
            info = character_unlock_information(person, tag)
            if info:
                positions[tag].append((f"{info} (disabled)", None))
                break

    if current_position:
        positions[current_position.skill_tag].insert(0, [f"Keep {current_position.verbing}\n{current_position.build_energy_arousal_line(person)}", current_position])
    else:
        positions["Foreplay"].append(("Go back", None))

    # Add headers
    if positions["Foreplay"]:
        positions["Foreplay"].insert(0, "Pick Foreplay")
    if positions["Oral"]:
        positions["Oral"].insert(0, "Pick Oral")
    if positions["Vaginal"]:
        positions["Vaginal"].insert(0, "Pick Vaginal")
    if positions["Anal"]:
        positions["Anal"].insert(0, "Pick Anal")

    return [
        positions["Foreplay"],
        positions["Oral"],
        positions["Vaginal"],
        positions["Anal"],
    ]

def is_watching(person: Person) -> bool:
    global watch_list
    return isinstance(watch_list, list) and person.identifier in watch_list

def build_sex_mechanic_strip_menu(person: Person) -> list[list[tuple[str, tuple[Clothing, str] | Any]]]:
    full_off_list = ["Take off"]
    for clothing in person.outfit.get_unanchored():
        if not clothing.is_extension:
            formatted_name = clothing.display_name.capitalize() + "\n-5 {image=gui/extra_images/arousal_token.png}"
            full_off_list.append((formatted_name, (clothing, "Full"))) #Keeps track if this was a full or partial strip, so we can reuse all of the strip taboo logic/dialogue

    half_off_list = ["Move away"]
    for clothing in person.outfit.get_unanchored(half_off_instead = True):
        if not clothing.half_off:
            half_off_list.append((clothing.display_name.capitalize(), (clothing, "Half")))

    other_list = ["Other", "Go Back"]
    return [full_off_list, half_off_list, other_list]

def default_unique_sex_positions(person: Person, prohibit_tags: list[str] = []) -> list[tuple[Position, int]]:
    positions = []
    if "Foreplay" not in prohibit_tags:
        if person.can_be_spanked:
            positions.append((spanking, 1))
    return positions

def check_person_position_tags(person: Person, position: Position) -> bool:
    return not any(x for x in position.opinion_tags if person.opinion(x) <= -2)

def suggest_alt_foreplay_sex_position(person: Person, position: Position, room_object: RoomObject, ignore_taboo = False) -> Position:
    alternate_position = kissing
    if position.guy_arousal > position.girl_arousal:    #checking arousal should show us if giving or receiving
        renpy.random.shuffle(foreplay_receiving_positions)
        for pos in (x for x in foreplay_receiving_positions if not x == position and x.requires_location in room_object.traits and check_person_position_tags(person, x)):
            if pos.her_position_willingness_check(person, ignore_taboo = ignore_taboo):
                alternate_position = pos
                break
    else:
        renpy.random.shuffle(foreplay_giving_positions)
        for pos in (x for x in foreplay_giving_positions if not x == position and x.requires_location in room_object.traits and check_person_position_tags(person, x)):
            if pos.her_position_willingness_check(person, ignore_taboo = ignore_taboo):
                alternate_position = pos
                break
    return alternate_position

def suggest_alt_oral_sex_position(person: Person, position: Position, room_object: RoomObject, ignore_taboo = False) -> Position:
    alternate_position = None
    if position.guy_arousal > position.girl_arousal:
        person.discover_opinion("giving blowjobs")
        renpy.random.shuffle(oral_receiving_positions)

        for pos in apply_position_filter(person, [x for x in oral_receiving_positions if not x == position and x.requires_location in room_object.traits and check_person_position_tags(person, x)], "oral"):
            if pos.her_position_willingness_check(person, ignore_taboo = ignore_taboo):
                alternate_position = pos
                break
    else:
        person.discover_opinion("getting head")
        renpy.random.shuffle(oral_giving_positions)

        for pos in apply_position_filter(person, [x for x in oral_giving_positions if not x == position and person.allow_position(x) and x.requires_location in room_object.traits and check_person_position_tags(person, x)], "oral"):
            if pos.her_position_willingness_check(person, ignore_taboo = ignore_taboo):
                alternate_position = pos
                break

    if alternate_position is None: #We didn't find a suitable alternative. Step down to foreplay
        alternate_position = suggest_alt_foreplay_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)

    return alternate_position

def suggest_alt_vaginal_sex_position(person: Person, position: Position, room_object: RoomObject, ignore_taboo = False) -> Position:
    vaginal_positions_avail = apply_position_filter(person, [x for x in list_of_positions if x.skill_tag == "Vaginal" and not x == position and person.allow_position(x) and x.requires_location in room_object.traits and check_person_position_tags(person, x) and x.her_position_willingness_check(person, ignore_taboo = ignore_taboo)], "vaginal")
    if person.opinion.vaginal_sex <= -2 or not vaginal_positions_avail:   #She isn't willing to do any type of vaginal sex. Step down to oral.
        person.discover_opinion("vaginal sex")
        alternate_position = suggest_alt_oral_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)
    else:
        alternate_position = renpy.random.choice(vaginal_positions_avail)
    return alternate_position

def suggest_alt_anal_sex_position(person: Person, position: Position, room_object: RoomObject, ignore_taboo = False) -> Position:
    anal_positions_avail = apply_position_filter(person, [x for x in list_of_positions if x.skill_tag == "Anal" and not x == position and person.allow_position(x) and x.requires_location in room_object.traits and check_person_position_tags(person, x) and x.her_position_willingness_check(person, ignore_taboo = ignore_taboo)], "anal")
    if person.opinion.anal_sex <= -2 or not anal_positions_avail:   #She isn't willing to do any type of anal sex. Step down to vaginal.
        person.discover_opinion("anal sex")
        alternate_position = suggest_alt_vaginal_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)
    else:
        alternate_position = renpy.random.choice(anal_positions_avail)
    return alternate_position

def suggest_alternate_sex_position(person: Person, position: Position, room_object: RoomObject, ignore_taboo = False) -> Position:
    alternate_position = kissing    #Default alternate position in case we can't find any others.
    #First, split the function based on type of sex attempted. Similar positions should have similar alternates.
    if position.skill_tag == "Foreplay":
        alternate_position = suggest_alt_foreplay_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)

    elif position.skill_tag == "Oral":
        alternate_position = suggest_alt_oral_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)

    elif position.skill_tag == "Vaginal":
        alternate_position = suggest_alt_vaginal_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)

    elif position.skill_tag == "Anal":
        alternate_position = suggest_alt_anal_sex_position(person, position, room_object, ignore_taboo = ignore_taboo)
    return alternate_position

def get_scrutiny_value(person: Person, position: Position) -> int:
    return ["Foreplay", "Oral", "Vaginal", "Anal"].index(position.skill_tag) + 1

def create_report_log(extra_values: dict[str, Any] = {}) -> dict[str, Any]:
    report_log = {
        "positions_used": [],
        "girl orgasms": 0,
        "guy orgasms": 0,
    }
    report_log.update(extra_values)
    return report_log

def post_double_orgasm(person: Person):
    mc.reset_arousal()
    mc.recently_orgasmed = True
    person.change_stats(happiness = 3, love = 1, max_love = 40)
    global report_log
    if "report_log" in globals() and isinstance(report_log, dict):
        report_log["guy orgasms"] = report_log.get("guy orgasms", 0) + 1

def choose_strip_sex_position_item(person: Person, position: Position) -> Clothing | None:
    '''
    Determine if we need to strip a clothing item to improve sex experience for passed sex position
    '''
    if position in (prone_bone, prone_anal):
        return None     # she is too exhausted to strip
    if ((position in (standing_finger, standing_grope, sixty_nine, cunnilingus, standing_cunnilingus, cowgirl_cunnilingus)
            or position.skill_tag in ("Vaginal", "Anal"))
            and person.wearing_panties):
        return person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, exclude_upper = True, do_not_remove = True)
    if ((position in (tit_fuck, sarah_tit_fuck)
            or position.skill_tag == "Oral")
            and person.wearing_bra):
        return person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, exclude_lower = True, do_not_remove = True)
    return None
