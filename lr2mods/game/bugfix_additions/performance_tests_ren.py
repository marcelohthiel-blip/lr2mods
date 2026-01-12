import time
import renpy
from game.bugfix_additions.debug_info_ren import add_to_debug_log, write_log
from game.bugfix_additions.ActionMod_ren import crisis_list, morning_crisis_list
from game.game_loops.advance_time_definition_ren import advance_time_assign_limited_time_events, advance_time_run_day, advance_time_run_move, advance_time_run_turn
from game.helper_functions.list_functions_ren import get_random_from_list
from game.helper_functions.random_generation_functions_ren import make_person
from game.major_game_classes.character_related.Person_ren import mc, town_relationships, list_of_people
from game.major_game_classes.game_logic.Room_ren import bedroom, rd_division, office, downtown, downtown_bar
from game.major_game_classes.clothing_related.wardrobe_builder_ren import WardrobeBuilder, real_dress_list, real_shirt_list
from game.major_game_classes.clothing_related.Wardrobe_ren import default_wardrobe
from game.map.map_code_ren import list_of_hubs, clear_map_cache, create_tooltip_dictionary, get_hub_tile_text

time_of_day = 0
day = 0
"""renpy
init 100 python:
"""
import threading
import pstats
import profile

def update_debug_profile_button(button_text):
    cs = renpy.get_screen("DebugInfo")
    cs.scope["profile_button_text"] = button_text

def outfit_selection_test(apply_outfits = False):
    start_time = time.time()
    for x in list_of_people:
        x.planned_outfit = x.decide_on_outfit()
        if apply_outfits:
            x.apply_planned_outfit()
    add_to_debug_log("World Wardrobe Update {total_time:.3f}", start_time)

def outfit_upper_body_item_selection_test():
    start_time = time.time()
    for x in list_of_people:
        _ = WardrobeBuilder.get_item_from_list(x, "upper_body", real_dress_list + real_shirt_list)
    add_to_debug_log("World outfit upper body item selection {total_time:.3f}", start_time)

def personalize_outfit_test():
    start_time = time.time()
    for x in list_of_people:
        x.planned_outfit = x.personalize_outfit(x.planned_outfit)
        x.apply_planned_outfit()
    add_to_debug_log("Personalize Outfit {total_time:.3f}", start_time)

def outfit_copy_test():
    start_time = time.time()
    for x in list_of_people:
        test = x.planned_outfit.get_copy()
        if not x.planned_outfit.matches(test) or not x.planned_outfit.matches_overwear(test) or not x.planned_outfit.matches_underwear(test):
            write_log(f"Outfit copy failed for {x.name}")
            current_clothing = tuple(x.planned_outfit.upper_body + x.planned_outfit.lower_body + x.planned_outfit.feet)
            other_clothing = tuple(test.upper_body + test.lower_body + test.feet)

            for a in current_clothing:
                if not any(b.is_similar(a) for b in other_clothing):
                    write_log(f"Tried to find {a.name} but not found in copied outfit.")

    add_to_debug_log("Outfit Copy Test {total_time:.3f}", start_time)

def time_to_get_home_hubs():
    start_time = time.time()
    for x in list_of_people:
        _ = x.home_hub.formal_name
    add_to_debug_log("Home Hub Time {total_time:.3f}", start_time)


def profile_game_engine():
    def run_profiler():
        profile.runctx("profiler_script(1)", globals(), locals(), "lr2-profile.prof")

    update_debug_profile_button("Running")
    profile_thread = threading.Thread(target = run_profiler)
    profile_thread.start()


def profiler_script(loops = 1):
    global time_of_day
    global day

    try:
        for _ in range(loops):
            mc_locations = {0: bedroom, 1: rd_division, 2: office, 3: downtown, 4: downtown_bar}
            for i in range(5):
                advance_time_run_turn()
                time_of_day = i # go to a scheduled location
                advance_time_run_move()
                mc.change_location(mc_locations[time_of_day])
                advance_time_assign_limited_time_events()
                clear_map_cache()
                # pre-load map cache
                for x in list_of_hubs:
                    get_hub_tile_text(x)
                # check crisis requirements for time slot
                [x.is_action_enabled() for x in crisis_list]

                create_tooltip_dictionary(mc.current_location_hub.visible_locations)

            advance_time_run_turn()
            advance_time_run_move()
            mc.change_location(mc_locations[time_of_day])
            advance_time_assign_limited_time_events()
            advance_time_run_day()
            if loops > 1: # only when more than one loop (allow for repeatable testing on 1 loop)
                day += 1
            time_of_day = 0 # go back home and run day code
            mc.change_location(bedroom)
            clear_map_cache()
            # pre-load map cache
            for x in list_of_hubs:
                get_hub_tile_text(x)
            # check crisis requirements for time slot
            [x.is_action_enabled() for x in morning_crisis_list]
            create_tooltip_dictionary(mc.current_location_hub.visible_locations)
    except Exception as ex:
        print(ex)

    threading.Thread(target = parse_profile_file).start()

def profiler_script2():
    try:
        for x in default_wardrobe.outfit_sets:
            for y in list_of_people:
                for a in y.wardrobe.outfit_sets:
                    a.matches(x)

        for x in default_wardrobe.overwear_sets:
            for y in list_of_people:
                for a in y.wardrobe.overwear_sets:
                    a.matches_overwear(x)

        for x in default_wardrobe.underwear_sets:
            for y in list_of_people:
                for a in y.wardrobe.underwear_sets:
                    a.matches_underwear(x)
    except Exception as ex:
        print(ex)

    threading.Thread(target = parse_profile_file).start()

def profile_crisis_list():
    for x in crisis_list + morning_crisis_list:
        start_time = time.time()
        x.is_action_enabled()
        write_log(f"{x.name} took {time.time() - start_time:.3f} seconds to execute.")

def fill_up_business_with_employees():
    for _ in range(8):
        candidates = []
        for _ in range(5):
            candidate = make_person(allow_premade = True, **(mc.business.generate_candidate_requirements()))
            candidate.generate_home().add_person(candidate)
            candidates.append(candidate)

        mc.business.add_employee_hr(candidates[0])
        mc.business.add_employee_marketing(candidates[1])
        mc.business.add_employee_research(candidates[2])
        mc.business.add_employee_production(candidates[3])
        mc.business.add_employee_supply(candidates[4])

    for person in mc.business.employee_list:
        rnd = renpy.random.randint(0, 2)
        other_person = get_random_from_list([x for x in mc.business.employee_list if x != person])
        if rnd == 0:
            town_relationships.improve_relationship(person, other_person)
        elif rnd == 1:
            town_relationships.worsen_relationship(person, other_person)

def parse_profile_file():
    time.sleep(.5)
    stream = open('lr2-profile.txt', 'w')
    stats = pstats.Stats('lr2-profile.prof', stream = stream)
    stats.sort_stats('tottime')
    #stats.sort_stats('cumtime')
    #stats.reverse_order()
    stats.print_stats()
    stream.close()

    update_debug_profile_button("Profile")
