init -50 python: #Init -10 is used for all project wide imports of external resources
    import os
    import copy
    import math
    import builtins
    import xml.etree.ElementTree as ET
    import time
    import hashlib
    import io
    from collections import defaultdict
    from collections import OrderedDict
    import unicodedata
    import sys
    from functools import partial
    import re
    import string
    from operator import attrgetter



    renpy.music.register_channel("sex", "sfx", loop=False, stop_on_mute=True, tight=False, file_prefix="", file_suffix="", buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("effects", "sfx", loop=False, stop_on_mute=True, tight=False, file_prefix="", file_suffix="", buffer_queue=True, movie=False, framedrop=True)


    # non stored list arrays
    list_of_instantiation_labels = [] #Strings added to this list will be called at the start of the game. Use to initialize things which need their game state saved.
    list_of_instantiation_functions = [] #String added to this list will be callled as python functions at start of the game
    list_of_positions = [] # These are sex positions that the PC can make happen while having sex.
    list_of_girl_positions = [] # These are sex positions that the girl can make happen while having sex.
    list_of_strip_positions = [] # These are positions a girl can take while putting on a stirp tease for you.


#Init -5 establishes all game classes
#Init -2 is then used by all game content that will use those game classes (ie. instantiates different Crises that could be generated)
#Init 0 establishes Renpy settings, including callbacks for display code.

init -2: # Establish some platform specific stuff.
    default persistent.colour_palette = []
    default persistent.pregnancy_pref = 0 # 0 = no content, 1 = predictable, 2 = realistic
    default persistent.vren_display_pref = "None" # "Float" = Aura, "None" = without Aura
    default persistent.text_effects = True
    default persistent.nearby_locations_enabled = True
    default persistent.use_imperial_system = True

    # initialize with defaults (standard)
    default GAME_SPEED = 1
    default TIER_1_TIME_DELAY = 3
    default TIER_2_TIME_DELAY = 7
    default TIER_3_TIME_DELAY = 14

init -2 python:
    global emotion_images_dict
    emotion_images_dict = {}
    for skin in ("white", "tan", "black"):
        emotion_images_dict[skin] = {}
        for face in Person._list_of_faces:
            emotion_images_dict[skin][face] = Expression(f"{skin}_{face}", skin, face)

    global body_images_dict
    body_images_dict = {
        "white": white_skin,
        "tan": tan_skin,
        "black": black_skin
    }

    global tan_images_dict
    tan_images_dict = {
        x.name: x for x in [no_tan, normal_tan, sexy_tan, one_piece_tan, slutty_tan]
    }

    def update_game_speed(speed):
        global GAME_SPEED, TIER_1_TIME_DELAY, TIER_2_TIME_DELAY, TIER_3_TIME_DELAY

        GAME_SPEED = speed
        if speed == 0:
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 5
        elif speed == 1:
            TIER_1_TIME_DELAY = 3
            TIER_2_TIME_DELAY = 7
            TIER_3_TIME_DELAY = 10
        elif speed == 2:
            TIER_1_TIME_DELAY = 5
            TIER_2_TIME_DELAY = 11
            TIER_3_TIME_DELAY = 15
        else:
            TIER_1_TIME_DELAY = 7
            TIER_2_TIME_DELAY = 15
            TIER_3_TIME_DELAY = 20
        return



init 0 python:
    config.gl2 = True  #Required to enable the model based renderer and use shaders.
    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 32
    config.cache_surfaces = False   # prevent render surfaces from being cached

    # Don't predict screens, it eats resources since every screen reloaded on a screen action (like hover)
    config.predict_screen_statements = False
    config.predict_screens = False

    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if renpy.variant("pc"):
        config.image_cache_size_mb = 1536 if is64Bit else 768
    else:
        config.image_cache_size_mb = 512 if is64Bit else 256

    config.rollback_enabled = True  # allows for smoother dialogues while skipping
    config.autoreload = False

    config.debug_text_overflow = False #If enabled finds locations with text overflow. Turns out I have a lot, kind of blows up when enabled and generates a large text file. A problem for another day.

    # THIS IS WHAT PREVENTS IT FROM INDEXING IMAGES
    # SEE 00images.rpy for where this is created
    config.images_directory = None

    _preferences.show_empty_window = False #Prevents Ren'py from incorrectly showing the text window in complex menu situations (which was a new bug/behaviour in Ren'py v7.2)

    global draw_layers
    draw_layers = []

    add_draw_layer("solo") # Add the main default draw layer, used for all single character displays
    add_draw_layer("extra", "solo") # Used for menu choice draw operation (person selection)
    add_draw_layer("mannequin", "screens")  # draw above screens

    renpy.add_layer("hud", "extra") # draw HUD elements above the main screen mannequin

    config.layer_clipping["mannequin"] = [1380, 0, 540, 1080] # for outfit mannequin


label start():
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."

    "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."
    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Semi-Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

        "Realistic pregnancy content\n{size=16}Realistic cycles. Girls know their fertile times. Pulling out not 100%% effective. Girls don't want to get pregnant.{/size}":
            $ persistent.pregnancy_pref = 3

    "How quickly would you like stories from the game to play out? This will affect spacing between story events."
    menu:
        "Quick":
            $ update_game_speed(0)
        "Standard":
            $ update_game_speed(1)
        "Epic":
            $ update_game_speed(2)
        "Marathon":
            $ update_game_speed(3)

    $ easy_mode = False
    "Do you want to play with default game difficulty or make the game easier?"
    menu:
        "Default Game Play":
            pass
        "Easier Game Play":
            "All options for making the game easier will be applied after character creation."
            $ easy_mode = True

    "Finally, the game uses random generated characters, the mod offers you the ability to control the random generation."
    "We will now open that screen for you, so you can set it to your preferences."

    call screen generic_preference_ui()

    $ starting_hires = False
    "Do you want to start the game employing just the head researcher? Or would you like to hire someone for each department?"
    menu:
        "Just Head Researcher":
            pass
        "Hire for Each Department":
            $ starting_hires = True

    "That's all, the game will now initialize, this might take a moment."

    $ renpy.block_rollback()
    if persistent.stats:
        $ name = persistent.stats['name']
        $ l_name = persistent.stats['l_name']
        $ b_name = persistent.stats['b_name']
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    $ setattr(persistent, "stats", {})
    $ [[persistent.stats["cha"],persistent.stats["int"],persistent.stats["foc"]], [persistent.stats["h_skill"],persistent.stats["m_skill"],persistent.stats["r_skill"],persistent.stats["p_skill"],persistent.stats["s_skill"]], [persistent.stats["F_skill"],persistent.stats["O_skill"],persistent.stats["V_skill"],persistent.stats["A_skill"]]] = _return
    $ [persistent.stats["name"],persistent.stats["l_name"],persistent.stats["b_name"]] = [store.name,store.l_name,store.b_name]


    python:
        renpy.show("Loading", layer = "solo", at_list = [truecenter], what = Image(get_file_handle("creating_world.png")))
        renpy.pause(0.5)
        renpy.game.interface.timeout(30)
        if easy_mode:
            for array in range(0, builtins.len(return_arrays)):
                for val in range(0, builtins.len(return_arrays[array])):
                    return_arrays[array][val] += 2

    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2]) from _call_initialize_game_state

    python:
        if easy_mode:
            # increased business stats
            mc.business.funds = 10000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 1000
            mc.business.base_effectiveness_cap = 110
            mc.business.marketability = 100
            # increased player stats
            mc.max_energy = 120
            mc.free_clarity += 500
            mc.clarity_multiplier = 3.0     # gain clarity 3 times faster
            # default unlock policies
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(theoretical_research, ignore_cost = True)
            purchase_policy(max_attention_increase_1_policy, ignore_cost = True)
        renpy.hide("Loading", layer = "solo")

        if starting_hires:
            market_hire = create_random_person()
            hr_hire = create_random_person()
            prod_hire = create_random_person()
            supply_hire = create_random_person()

            market_hire.market_skill = 4
            market_hire.charisma = 4
            market_hire.focus = 1
            market_hire.int = 1
            market_hire.hr_skill = 1
            market_hire.research_skill = 1
            market_hire.production_skill = 1
            market_hire.supply_skill = 1
            market_hire.set_opinion("marketing work", 2, False)
            market_hire.generate_home().add_person(market_hire)

            hr_hire.market_skill = 1
            hr_hire.charisma = 4
            hr_hire.focus = 1
            hr_hire.int = 1
            hr_hire.hr_skill = 4
            hr_hire.research_skill = 1
            hr_hire.production_skill = 1
            hr_hire.supply_skill = 1
            hr_hire.set_opinion("hr work", 2, False)
            hr_hire.generate_home().add_person(hr_hire)

            prod_hire.market_skill = 1
            prod_hire.charisma = 1
            prod_hire.focus = 4
            prod_hire.int = 1
            prod_hire.hr_skill = 1
            prod_hire.research_skill = 1
            prod_hire.production_skill = 4
            prod_hire.supply_skill = 1
            prod_hire.set_opinion("production work", 2, False)
            prod_hire.generate_home().add_person(prod_hire)

            supply_hire.market_skill = 1
            supply_hire.charisma = 1
            supply_hire.focus = 4
            supply_hire.int = 1
            supply_hire.hr_skill = 1
            supply_hire.research_skill = 1
            supply_hire.production_skill = 1
            supply_hire.supply_skill = 4
            supply_hire.set_opinion("supply work", 2, False)
            supply_hire.generate_home().add_person(supply_hire)

            mc.business.add_employee_marketing(market_hire)
            mc.business.add_employee_hr(hr_hire)
            mc.business.add_employee_production(prod_hire)
            mc.business.add_employee_supply(supply_hire)

    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start

init 0 python:
    def initialize_stephanie_in_our_business():
        mc.business.add_employee_research(stephanie, start_day = 0)
        mc.business.hire_head_researcher(stephanie)
        stephanie.change_location(lobby)
        stephanie.primary_job.add_duty(theoretical_research_duty)
        # setup Nano bot quest line
        add_fetish_serum_quest_intro()

label normal_start():
    ## For now, this ensures reloading the game doesn't reset any of the variables.
    $ show_ui()
    $ renpy.scene()
    $ bedroom.show_background()
    "It's Monday, and the first day of operation for your new business!"
    "[stephanie.title] said she would meet you at your new office for a tour."
    $ unlock_blue_serum()
    #TODO: Have an on_enter event for Steph if you see her the first day. Minor interaction stuff.

    #Add Stephanie to our business and flag her with a special role.

    $ initialize_stephanie_in_our_business()

    #TODO: movement overlay tutorial thing.
    jump game_loop

init 0 python:
    def build_actions_list():
        actions_list = []
        if mc.has_date_now:
            prep_string = "Prepare for date {image=gui/heart/Time_Advance.png}\n{menu_yellow}10% Extra {image=energy_token_small}{menu_yellow} (tooltip)Get ready for your next date. Recovers more energy than working."
            actions_list.append((prep_string, "Wait"))
        elif time_of_day == 4:
            if not mc.location.actions.has_action("sleep_action_description"): #If they're in a location they can sleep we shouldn't show this because they can just sleep here.
                location_word = "home" if not mc.is_at(home_hub) else "to bedroom"
                actions_list.append((f"Go {location_word} and sleep {{image=time_advance}}{{image=time_advance}} (tooltip)It's late. Go {location_word} and sleep.", "Wait"))
        else:
            actions_list.append(("Wait here {image=time_advance}\n{menu_yellow}10% Extra {image=energy_token_small}{menu_yellow} (tooltip)Kill some time and wait around. Recovers more energy than working.", "Wait"))
        actions_list.append(("Go somewhere else", "Travel"))
        actions_list.append(("Check your phone", "Phone"))
        actions_list.extend(mc.location.valid_actions)
        actions_list.insert(0, "Do Something")
        return actions_list

    def build_people_list():
        people_list = []
        people_list.extend(mc.location.people)
        people_list.sort(key = sort_display_list, reverse = True)
        people_list.insert(0, "Talk to Someone")
        return people_list

    def build_nearby_location_list():
        location_list = []
        if not persistent.nearby_locations_enabled:
            return location_list
        nearby = [x for x in mc.current_location_hub.visible_locations if x != mc.location and x.is_accessible]
        if not nearby:
            return location_list

        tt_dict = create_tooltip_dictionary(nearby)
        for loc in sorted(nearby, key = lambda x: x.formal_name):
            tooltip = get_location_tile_text(loc, tt_dict)
            location_list.append((f"{loc.formal_name} (tooltip){tooltip}", loc))
        location_list.insert(0, "Go to nearby location")
        return location_list

    def main_loop_pick_talk_event(person):
        talk_actions = person.on_talk_event_list.enabled_actions(person)

        # out of uniform takes precedence for other talk events
        out_of_uniform = next((x for x in talk_actions if x.name == "Uniform Disobedience LTE"), None)
        if out_of_uniform:
            person.on_talk_event_list.remove(out_of_uniform)
            return out_of_uniform

        # non LTE events take priority over LTE events
        chosen = get_random_from_list([x for x in talk_actions if not isinstance(x, Limited_Time_Action)])
        if chosen:
            person.on_talk_event_list.remove(chosen)
            return chosen

        chosen = get_random_from_list(talk_actions)
        if chosen:
            person.on_talk_event_list.remove(chosen)
            return chosen
        return None

    def main_loop_pick_room_event(location):
        enter_actions = []
        for person in location.people:
            enter_actions.extend([[[person, x], x.priority + 1] for x in person.on_room_enter_event_list.enabled_actions(person)])

        if enter_actions:
            chosen = get_random_from_weighted_list(enter_actions)
            chosen[0].on_room_enter_event_list.remove(chosen[1]) #Remove the event from their list since we will be running it.
            return chosen
        return None

    def main_loop_pick_silent_events(location):
        silent_actions = [(None, x) for x in location.on_room_enter_event_list.enabled_actions() if x.silent]
        chosen = get_random_from_list(silent_actions)
        if chosen:
            location.on_room_enter_event_list.remove(chosen[1])
            return chosen

        if not silent_actions:
            silent_actions = [(x, y) for x in location.people for y in x.on_room_enter_event_list.enabled_actions(x) if y.silent]
            chosen = get_random_from_list(silent_actions)
            if chosen:
                chosen[0].on_room_enter_event_list.remove(chosen[1])
                return chosen
        return None

    def main_loop_pick_location_event(location):
        location_actions = [[x, x.priority + 1] for x in location.on_room_enter_event_list.enabled_actions()]
        chosen = get_random_from_weighted_list(location_actions)
        if chosen:
            location.on_room_enter_event_list.remove(chosen)
            return chosen
        return None

    def main_loop_select_greeter(location):
        possible_greetings = [x for x in location.people if x.is_employee]
        return get_random_from_list(possible_greetings)

    common_variable_list = ["talk_action", "picked_option", "picked_event", "outfit", "insta_outfit", \
        "the_outfit", "new_outfit", "old_outfit", "the_uniform", "the_underwear", "person_one", "person_two", "the_person_one", \
        "the_person_two", "the_item", "the_clothing", "clothing", "the_group", "the_report", "the_trait", "the_mom", "the_action", \
        "the_aunt", "the_sister", "the_student", "the_place", "the_girl", "test_outfit", "object", "the_object", "the_start_object", \
        "the_location", "next_item", "file_path", "title_choice", "title_one", "title_two", "placeholder", \
        "formatted_title_one", "formatted_title_two", "new_title", "the_type", "the_person", "player_choice", \
        "strip_list", "first_item", "feet_ordered", "top_feet", "crisis", "the_morning_crisis", \
        "report_log", "position_choice", "object_choice", "round_choice", "start_position", "the_group", \
        "report", "the_relationship", "partner", "the_subject", "stripper", "potential_people",\
        "not_stripper", "the_student", "strip_choice", "new_pose", "picked_object", "picked_position", "picked_pose", "picked_serum", "pose_choice", "new_person" \
        "clothing", "formatted_name", "formatted_title", "hair_style_check", "pubic_style_check", "the_cause", "a_duty", \
        "text_one", "text_two", "the_goal", "the_serum", "title", "opinion_tag", "overhear_topic", "the_choice", "the_position", \
        "opinion_string", "mc_opinion_string", "talk_opinion_text", "opinion_learned", "place", "the_place", "the_taboo",
        "climax_controller", "the_watcher", "person_choice", "t", "x", "y", "z", "so_title", "a_person", "person_1", "person_2", "test_person",
        "grope_tits_slut_token", "grope_pussy_slut_token", "jerk_off_slut_token", "titfuck_slut_token", "facefuck_slut_token", "sex_token",
        "slut_token", "tease_token", "red_heart_token", "blowjob_slut_token", "exclude_list",
        "sex_slut_token", "scene_manager", "HR_employee_list", "the_target"]

    def main_loop_cleanup():
        clear_scene()
        # generic cleanup routine for common variable names
        for name in common_variable_list:
            if name in globals():
                del globals()[name]

    def main_loop_auto_save():
        last_save_day = mc.business.get_event_day("last_save_day")
        if day > last_save_day and time_of_day == 0:
            #renpy.notify("Saving game: " + str(day))
            renpy.force_autosave(take_screenshot = True, block = True)
            mc.business.set_event_day("last_save_day")


label game_loop(): ##THIS IS THE IMPORTANT SECTION WHERE YOU DECIDE WHAT ACTIONS YOU TAKE
    python:
        main_loop_cleanup()
        main_loop_auto_save()
        renpy.block_rollback()
        renpy.checkpoint()
        clear_map_cache()
        # pre-load map cache
        for x in list_of_hubs:
            get_hub_tile_text(x)
        create_tooltip_dictionary(mc.current_location_hub.visible_locations)

    call screen main_choice_display(build_menu_items([build_people_list(), build_actions_list(), build_nearby_location_list()]))
    $ picked_option = _return

    if isinstance(picked_option, Person):
        $ talk_action = main_loop_pick_talk_event(picked_option)
        if talk_action:
            $ picked_option.draw_person()
            $ talk_action.call_action(picked_option)
        elif (time_of_day == 4 and picked_option.love < 40 and picked_option.sluttiness < 40 and
                mc.is_at(picked_option.home) and not picked_option in (mom, lily)):
            call unhappy_with_visit(picked_option) from _call_unhappy_with_visit_game_loop
        else:
            if picked_option.is_stranger:
                "You decide to approach the stranger and introduce yourself."
                $ picked_option.draw_person()
            else:
                "You approach [picked_option.title] and chat for a little bit."
                $ picked_option.draw_person()
                $ picked_option.call_dialogue("greetings")

            if not picked_option.is_job_known and picked_option.is_wearing_uniform:
                $ picked_option.learn_job()
                if picked_option.is_stranger:
                    "As you walk up her, you notice her uniform, she's a [picked_option.current_job.job_title]."
                else:
                    "As you walk up to [picked_option.fname], you notice her uniform, she's a [picked_option.current_job.job_title]."

            if picked_option.has_taboo(["underwear_nudity","bare_tits", "bare_pussy"]) and picked_option.judge_outfit(picked_option.outfit, -30): #If she's in anything close to slutty she's self-conscious enough to comment on it.
                if picked_option.vagina_visible and picked_option.has_taboo("bare_pussy") and picked_option.tits_visible and picked_option.has_taboo("bare_tits"):
                    "[picked_option.title] doesn't say anything about it, but seems uncomfortable being naked in front of you."
                    "As you talk she seems to become more comfortable with her own nudity, even if she isn't thrilled by it."

                if picked_option.vagina_visible and picked_option.has_taboo("bare_pussy"):
                    "[picked_option.title] doesn't say anything about it, but angles her body to try and conceal her bare pussy from you."
                    "As you talk she seems to become more comfortable, even if she isn't thrilled about it."

                elif picked_option.tits_visible and picked_option.has_taboo("bare_tits"):
                    "[picked_option.title] doesn't say anything about it, but brings her arms up to try and conceal her tits."
                    if picked_option.has_large_tits:
                        "Her large chest isn't easy to hide, and she quickly realises it's hopeless."
                    else:
                        "As you talk she seems to become more comfortable, and eventually lets her arms drop again."

                elif (picked_option.outfit.are_panties_visible or picked_option.outfit.is_bra_visible) and picked_option.has_taboo("underwear_nudity"):
                    "[picked_option.title] doesn't say anything about it, but she tries to cover up her underwear with her hands."
                    "As you talk she seems to become more comfortable, and eventually she lets her arms drop to her sides."

                $ picked_option.update_outfit_taboos()
            call talk_person(picked_option) from _call_talk_person

    elif isinstance(picked_option, Action):
        $ picked_option.call_action()

    elif isinstance(picked_option, Room):

        call change_location(picked_option) from _call_change_location_nearby #_return is the location returned from the map manager.

    elif picked_option == "Travel":
        call screen map_manager()
        if isinstance(_return, Room):
            call change_location(_return) from _call_change_location #_return is the location returned from the map manager.

    elif picked_option == "Phone":
        call browse_internet() from _call_browse_internet

    elif picked_option == "Wait":
        if time_of_day == 4:
            $ mc.change_location(bedroom)
        else:
            $ mc.change_energy(mc.max_energy * .1) #Extra 10% energy gain if you spend your time waiting around
        call advance_time() from _call_advance_time_15

    jump game_loop

label change_location(the_place):
    $ renpy.scene()
    if not mc.change_location(the_place):
        $ mc.location.show_background() # redraw background (is cleared by map)
    else:
        $ character_cache.clear()
        $ portrait_cache.clear()
        if the_place.trigger_tutorial and the_place.tutorial_label is not None and mc.business.event_triggers_dict.get("Tutorial_Section",False):
            $ the_place.trigger_tutorial = False
            $ renpy.call(the_place.tutorial_label)

    $ silent_room_event = main_loop_pick_silent_events(the_place)
    while silent_room_event:
        $ silent_room_event[1].call_action(silent_room_event[0])
        $ silent_room_event = main_loop_pick_silent_events(the_place)

    $ picked_room_event = main_loop_pick_location_event(the_place)
    if picked_room_event:   # the location enter event has higher priority
        $ picked_room_event.call_action()
        $ picked_room_event = None
    elif the_place.people: #There are people in the room, let's see if there are any room events
        $ picked_event = main_loop_pick_room_event(the_place)
        if picked_event: #If there are room events to take care of run those right now.
            $ picked_event[1].call_action(picked_event[0]) #Run the action with the person as an extra argument.
        elif renpy.random.randint(0, 2) == 0 and the_place in (mc.business.m_div, mc.business.p_div, mc.business.r_div, mc.business.s_div, mc.business.h_div): #There are no room events, so generate a quick room greeting from an employee if one is around.
            $ the_greeter = main_loop_select_greeter(the_place)
            if the_greeter:
                $ the_greeter.draw_person()
                $ the_greeter.call_dialogue("work_enter_greeting")
                $ clear_scene()
                $ the_greeter = None
        $ picked_event = None
    return

label unhappy_with_visit(the_person):
    "As you approach [the_person.title], she looks at you."
    $ the_person.draw_person(emotion = "angry")
    $ the_person.change_stats(happiness = -5, love = -1, obedience = -1)
    the_person "My god [the_person.mc_title], what are you doing here at this hour."
    the_person "I think it's better that you leave now."
    "She's clearly not happy about you being in her home, so you decide to leave."
    $ mc.change_location(downtown)
    $ clear_scene()
    return

label talk_person(the_person, keep_talking = True):
    $ mc.having_text_conversation = None #Just in case some event hasn't properly reset this.
    if the_person.is_stranger:
        $ the_person.draw_person()
        call person_introduction(the_person) from _call_person_introduction

label .continue_talk():
    $ renpy.restart_interaction()
    $ the_person.draw_person()
    call screen main_choice_display(build_menu_items([build_chat_action_list(the_person, keep_talking), build_specific_action_list(the_person, keep_talking), build_special_role_actions_list(the_person, keep_talking)]))

    $ explicit_exit = True # Use to check if the player selected an explicit "stop talking" option
    if isinstance(_return, Action):
        $ starting_time_of_day = time_of_day
        $ _return.call_action(the_person)

        if the_person in mc.location.people and time_of_day == starting_time_of_day and keep_talking:
            jump talk_person.continue_talk #If we're in the same place and time hasn't advanced keep talking to them until we stop talking on purpose.

        $ explicit_exit = False
    $ clear_scene()
    return explicit_exit

label initialize_game_state(character_name, business_name, last_name, stat_array, skill_array, _sex_array): #Gets all of the variables ready. TODO: Move some of this stuff to an init block?

    ##Global Variable Initialization##
    python:
        renpy.not_infinite_loop(5)
        day = 0 ## Game starts on day 0.
        time_of_day = 0 ## 0 = Early morning, 1 = Morning, 2 = Afternoon, 3 = Evening, 4 = Night

        action_mod_list = []
        perk_system = Perks()
        list_of_people = []
        list_of_patreon_characters = []
        general_duties_list = []
        general_rd_duties = []
        general_market_duties = []
        general_supply_duties = []
        general_production_duties = []
        general_hr_duties = []
        talking_person = None

        default_wardrobe = wardrobe_from_xml("Master_Default_Wardrobe")
        lingerie_wardrobe = wardrobe_from_xml("Lingerie_Wardrobe")
        insta_wardrobe = wardrobe_from_xml("Insta_Wardrobe")

        # cleanup the default wardrobe
        cleanup_default_wardrobe()

    #NOTE: These need to be established in a separate label to ensure they are loaded/saved correctly
    call instantiate_serum_traits() from _call_instantiate_serum_traits #Creates all of the default LR2 serum traits. TODO: Create a mod loading list that has labels that can be externally added and called here.
    call instantiate_roles() from _call_instantiate_roles
    call instantiate_personalities() from _call_instantiate_personalities
    call instantiate_side_effect_traits() from _call_instantiate_side_effect_traits
    call instantiate_business_policies() from _call_instantiate_business_policies
    call instantiate_map_locations() from _call_instantiate_map_locations

    python:
        ##PC starts in his bedroom##
        mc = MainCharacter(bedroom, character_name, last_name, stat_array, skill_array, _sex_array)
        mc.business = Business(business_name, m_division, p_division, rd_division, office, office)

        town_relationships = RelationshipArray() #Singleton class used to track relationships. Removes need for recursive character references (which messes with Ren'py's saving methods)

        # setup perk system tutorial
        mc.business.event_triggers_dict["perk_tutorial"] = 1
        mc.business.add_mandatory_crisis(
            Action("Perk Tutorial",Perk_Tutorial_Crisis_requirement,"Perk_Tutorial_Crisis_label")
        )

        init_duty_lists()
        init_job_list()

    call instantiate_goals() from _call_instantiate_goals

    python:
        generate_patreon_character_list()
        c = 0
        renpy.not_infinite_loop(5)
        while c < builtins.len(list_of_instantiation_functions):
            call_global_func(list_of_instantiation_functions[c])
            c += 1

    $ c = 0
    $ renpy.not_infinite_loop(5)
    while c < builtins.len(list_of_instantiation_labels):
        $ renpy.call(list_of_instantiation_labels[c])
        $ c += 1

    python:
        renpy.not_infinite_loop(5)
        generate_random_characters()
        add_stripclub_strippers()
        instantiate_limited_wardrobes()

    call instantiate_map_hubs() from _call_instantiate_map_hubs
    return

label instantiate_serum_traits(): #Creates all of the default LR2 serum trait objects.
    python:
        list_of_traits = []
        list_of_nora_traits = []
        list_of_mc_traits = []

        init_T0_traits()
        init_T1_traits()
        init_T2_traits()
        init_T3_traits()

        init_blueprint_traits()
        init_nora_special_traits()
        init_mc_traits()
    return

label instantiate_side_effect_traits(): #Creates all of the default LR2 serum trait objects.
    python:
        list_of_side_effects = []

        init_side_effect_traits()
    return

label instantiate_roles():
    python:
        init_generic_roles()
        init_relationship_roles()
        init_business_roles()
        init_strip_club_roles()
        init_pregnant_role()
        init_maid_role()
    return

label instantiate_personalities():
    python:
        list_of_personalities = []

        init_base_personalities()
        init_special_personalities()
    return
