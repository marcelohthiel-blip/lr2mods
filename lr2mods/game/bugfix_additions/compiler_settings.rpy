init -2 python:
    build.script_version = True
    build.classify("**.rpy", None) # don't include rpy files in build
    build.classify("**.bak", None)
    build.classify("**.ref", None)
    build.classify('**~', None)
    build.classify('**/#**', None)
    build.classify("**.back", None)
    build.classify("**.txt", None)
    build.classify("**.save", None)
    build.classify("**.drawio", None)
    build.classify("**/game/saves/**.**", None)
    build.classify("**.rpyb", None)
    build.classify("**.code-workspace", None)
    build.classify("game/animation/**.png", None)
    build.classify("game/customizations/**.**", None)
    build.classify("game/cache/**", None)
    build.classify("*.exe", None)
    build.classify("**.", None)
    build.classify("*.ps1", None)
    build.classify('*.json', None)
    # exclude icon images from build
    build.classify("game/images/**.ico", None)
    build.classify("game/images/**.icns", None)
    build.classify("game/images/**.pdn", None)

    # test labels
    build.classify("game/people/jennifer/jennifer_test_functions.*", "None")
    build.classify("game/game_roles/pregnant_roles/temp_preg_test.*", "None")


    if not renpy.mobile:
        # include existing .rpa files
        build.classify("**.rpa", "renpy")

        build.archive("background_images") #When building all mod background images are placed into an archive.
        build.classify("game/images/**.jpg", "background_images")
        build.classify("game/images/**.png", "background_images")

        build.archive("gui")
        build.classify("game/gui/**.png", "gui")
        build.classify("game/map/**.png", "gui")

        # include all wardrobe files (allow user modification, so not in archive)
        build.classify("game/wardrobes/**.xml", "all")

        build.archive("scripts")
        build.classify("game/**.rpyc", "scripts") # put compiled game files into scripts.rpa
        build.classify("game/python-packages/**.**", "scripts")   # include python packages
        build.classify("**.py", None)   # exclude other python files

        build.archive("fonts")
        build.classify("game/**.ttf", "fonts")
        build.classify("game/**.otf", "fonts")

        build.archive("sounds")
        build.classify("game/sounds/**", "sounds")

        build.archive("tutorial_images")
        build.classify("game/images/tutorial_images/**.png", "tutorial_images")
        build.classify("game/images/tutorial_images/**.jpg", "tutorial_images")

        build.archive("character_images")
        build.classify("game/images/character_images/**.zip", "character_images")
        build.classify("game/images/character_images/empty_holder.png", "character_images")
        build.classify("game/images/character_images/mannequin_average.png", "character_images")

    # include mods folder info (not archived)
    build.classify("game/mods/putyourmodshere.info", "all")
    # exclude runtime zip file and profiler files
    build.classify("LR2R-Runtime.zip", None)
    build.classify("lr2-profile.*", None)

    build.include_i686 = False
    build.include_old_themes = False

    # switch version prior to building, but check-in the 'beta' version
    config.version = "2025.07-beta"
    # current AiO release version
    # config.version = "2025.04"

    # disable developer for release
    config.developer = True
    config.console = True

    # extra debug settings only enable when needed
    # config.debug = True
    # config.profile = True
    # config.manage_gc = False
    # config.gc_print_unreachable = True

python early:
    config.window_icon = "images/mod_icon.png"

    # persisten storage folder, change when saves are not compatible
    config.save_directory = "LR2_R202408"
