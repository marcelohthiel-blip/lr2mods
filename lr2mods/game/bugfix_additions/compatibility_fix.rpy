init -100 python:
    import functools

    @renpy.pure
    def get_loaded_version():
        if "game_version" in globals():
            loaded_version = game_version
        else:
            loaded_version = "v0.33.3"
        return loaded_version

    # python 3 no longer supports callable, this is an easy fix for all places where it is used
    @renpy.pure
    def callable(obj):
        return hasattr(obj, '__call__')

    @renpy.pure
    def inform_label_not_found(label_name):
        global missing_label_name
        missing_label_name = label_name
        return "missing_label_called"

init -2:
    default persistent.serum_messages = True
    default persistent.stat_change_messages = True
    default persistent.skill_change_messages = True
    default persistent.clarity_messages = True
    default persistent.energy_messages = True
    default persistent.scene_popups = True

    default persistent.zip_cache_preload = False
    default persistent.zip_cache_size = 0 # default is small size
    default persistent.show_ntr = False     # default turn of NTR
    default persistent.keep_patreon_characters = True  # keep VREN original characters from hire process
    default persistent.mc_noncon_pref = 0   #Default to disabled. MC does not allow himself to be raped in any situation.
    default persistent.mark_unique_as_favourite = True
    default persistent.skip_end_of_day = False
    default missing_label_name = ""

    #don't force low power usage -> let the configure themselves SHIFT-G
    #default preferences.gl_framerate = 30
    #default preferences.gl_powersave = True

init python: # place first on the hijack stack
    add_label_hijack("after_load", "check_save_version")

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")
    add_label_hijack("start", "check_mod_installation")

init 100 python:
    add_label_hijack("normal_start", "store_game_version")

init -5 python:
    # override some of the default settings to improve performance
    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if is64Bit:
        config.image_cache_size_mb = 768 # fixed at 768 Mb * 4 bytes per pixel
    else:
        config.image_cache_size_mb = 384 # fixed at 384 Mb * 4 bytes per pixel

    # disable gl2 extensions
    if renpy.android or renpy.mobile:
        config.gl2 = False

    # allow for more idle objects
    config.automatic_images = None
    config.check_conflicting_properties = True
    config.optimize_texture_bounds = True
    config.predict_statements = 64 if is64Bit else 32
    config.rollback_length = 64 if is64Bit else 32      # since refactor we can allow a longer rollback history
    config.cache_surfaces = False
    config.predict_screen_statements = False
    config.predict_screens = False
    config.list_compression_length = 200        # increase list compression length for rollback
    config.missing_label_callback = inform_label_not_found
    # disable auto save
    config.autosave_on_choice = False
    config.autosave_on_quit = False
    config.autosave_on_input = False
    config.autosave_frequency = None
    config.has_autosave = True
    config.has_quicksave = True
    config.autosave_slots = 6
    # config.autosave_frequency = 200 # default: 200

    # for DEBUG only (uncomment when you get a cPickle error)
    # config.debug_image_cache = True

    # disable sound settings
    config.has_sound = True
    config.has_music = False
    config.has_voice = False

    # remove full outfits / overwear from default wardrobe that have no shoes or no layer 2 clothing items (nude outfits)
    # to prevent messed up outfits to be used by girls in daily life
    def cleanup_default_wardrobe():
        remove = []
        for outfit in default_wardrobe.outfit_sets + default_wardrobe.overwear_sets:
            if not any(x for x in outfit.feet if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 3 or x.layer == 4):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 3 and x.has_extension) and \
                not any(x for x in outfit.lower_body if x.layer == 3):
                remove.append(outfit)

        if builtins.len(remove) > 10:
            write_log("WARNING: Something is wrong with the clothing layers, too many outfits ({}) are being removed.".format(len(remove)))
        # print("Removing {} outfits from default wardrobe.".format(len(remove)))
        for outfit in remove:
            # print("Removing: " + outfit.name)
            default_wardrobe.remove_outfit(outfit)
        return

    # add code here to keep save games compatible
    def save_game_compatibility():
        if not sarah.has_event_day("day_met") and day >= TIER_1_TIME_DELAY:
            sarah.set_event_day("day_met", TIER_1_TIME_DELAY)
        if not camila.has_event_day("day_met") and not camila.is_stranger:
            camila.set_event_day("day_met", min(day, 7))
        if not iris.has_event_day("day_met") and not iris.is_stranger:
            iris.set_event_day("day_met", min(day, 56))
        if not nora.has_event_day("day_met") and not nora.is_stranger:
            nora.set_event_day("day_met", min(day, 44))
        if not salon_manager.has_event_day("day_met") and not salon_manager.is_stranger:
            salon_manager.set_event_day("day_met", min(day, 44))
        if not candace.has_event_day("day_met") and not candace.is_stranger:
            candace.set_event_day("day_met", min(day, 44))
        if not myra.has_event_day("day_met") and not myra.is_stranger:
            myra.set_event_day("day_met", min(day, 50))
        if not kaya.has_event_day("day_met") and not kaya.is_stranger:
            kaya.set_event_day("day_met", min(day, 50))
        if not naomi.has_event_day("day_met") and not naomi.is_stranger:
            naomi.set_event_day("day_met", min(day, 50))
        if not sakari.has_event_day("day_met") and not sakari.is_stranger:
            sakari.set_event_day("day_met", min(day, 50))

        # replace broken 'stand' object with enhanced floor object
        for x in list_of_places:
            stand= next((x for x in x.objects if x.name == "stand"), None)
            if stand:
                x.objects.remove(stand)

            floor= next((x for x in x.objects if x.name == "floor"), None)
            if floor:
                if not "Stand" in floor.traits:
                    floor.traits.append("Stand")
            else:
                x.objects.append(make_floor())

        return

label check_mod_installation(stack):
    $ execute_hijack_call(stack)
    return

label activate_compatibility_fix(stack):
    # make sure we store the crisis tracker in the save game
    $ crisis_tracker_dict = {}
    $ execute_hijack_call(stack)
    return

label update_compatibility_fix(stack):
    if not "crisis_tracker_dict" in globals():
        $ crisis_tracker_dict = {}

    $ save_game_compatibility()

    $ execute_hijack_call(stack)
    return

label store_game_version(stack):
    $ game_version = config.version
    $ execute_hijack_call(stack)
    return

label check_save_version(stack):
    $ loaded_version = get_loaded_version()

    if "game_version" in globals() and loaded_version != game_version:
        "Warning" "You are loading a game created by a previous build ([loaded_version]), you might run into errors because of this. Before reporting errors, please start a new game with and see if the problem persists."
    $ execute_hijack_call(stack)
    return

label missing_label_called(arg1 = None, Arg2 = None):
    "System" "Something went wrong, the game called label '[missing_label_name]', but this label does not exist."
    return
