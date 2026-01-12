init 2:
    style debug_label_text:
        size 14
        italic False
        bold False
        color "#ffffff"
        outlines [(2,"#222222",0,0)]

    screen DebugInfo():
        layer "hud"
        style_prefix "debug"
        zorder 400

        default profile_button_text = "Profile"

        drag:
            drag_name "DebugInfo"
            xalign .9
            yalign 0
            drag_handle(0.0,0.0, 1.0,1.0)
            frame:
                background "#00000055"
                xminimum 400
                xmaximum 600
                padding (5,5)
                has vbox
                frame:
                    background None
                    pos (320, 10)
                    xysize (60, 20)
                    button:
                        xysize (60, 20)
                        text "[profile_button_text]" size 12 xalign .5
                        background "#44444488"
                        hover_background "#0000FF88"
                        align (0.5, 0.5)
                        action [Function(profile_game_engine)]

                grid 2 4:
                    pos (0, -20)
                    label "Zip Cache:"
                    label f"{system_info.total_zip_size / 1024.0 / 1024.0:.2f} MB ({system_info.total_zip_items}) {system_info.zip_utilization:.1f}%"
                    label "Outfit Queue:"
                    label f"{system_info.outfit_queue_size}"
                    label "Texture Memory:"
                    label f"{system_info.texture_size / 1024.0 / 1024.0:.2f} MB ({system_info.texture_count})"
                    label "Image Cache:"
                    label f"{4.0 * system_info.cache_size / 1024.0 / 1024.0:.1f} / {4.0 * renpy.display.im.cache.cache_limit / 1024.0 / 1024.0:.1f} MB ({system_info.cache_size * 100.0 / renpy.display.im.cache.cache_limit:.1f}%)"
                label get_debug_log()


    # renpy.profile_screen("main_ui", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
    # renpy.profile_screen("business_ui", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
    # renpy.profile_screen("person_info_ui", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
    # renpy.profile_screen("main_choice_display", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
