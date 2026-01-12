screen outfit_select_manager(wardrobe, slut_limit = 999, show_outfits = True, show_overwear = True, show_underwear = True, main_selectable = True, show_make_new = True, show_export = True, show_modify = True, show_duplicate = True, show_delete = True, start_mannequin = "mannequin", outfit_validator = None, allow_switch_wardrobe = False):
    #If sluttiness_limit is passed, you cannot exit the creator until the proposed outfit has a sluttiness below it (or you create nothing).
    add paper_background_image
    modal True
    zorder 100
    default demo_outfit = None
    default hide_underwear = False
    default hide_shoes = False
    default hide_base = False
    default hide_overwear = False
    default hide_list = []
    default mannequin = start_mannequin
    default mannequin_pose = "stand3" if mannequin == "mannequin" else mannequin.idle_pose
    default current_wardrobe = wardrobe
    default show_personalisation = False

    default outfit_info_array = [
        ## ["Category name", is_category_enabled, "return value when new is made", slut score calculation field/function, "export field type", add_outfit_to_wardrobe_function] ##
        (show_outfits, "Outfit", "new_full", "outfit_slut_score" , "FullSets", Wardrobe.add_outfit, "outfit_sets", "full"),
        (show_overwear, "Overwear", "new_over", "overwear_slut_score", "OverwearSets",  Wardrobe.add_overwear_set, "overwear_sets", "over"),
        (show_underwear, "Underwear", "new_under", "underwear_slut_score", "UnderwearSets", Wardrobe.add_underwear_set, "underwear_sets", "under")
    ]

    vbox:
        spacing 10
        align (.1, .05)
        if allow_switch_wardrobe:
            frame:
                background "#1a45a1aa"
                xysize (1390, 40)
                align (0.5, 0.5)
                hbox:
                    spacing 50
                    align (0.0, 0.5)
                    text "Wardrobe:" style "serum_text_style_header" yalign 0.5 ysize 40 yoffset 4
                    textbutton "{image=dropdown_token} [current_wardrobe.name]":
                        align (0.0, 0.5)
                        ysize 40
                        padding (2, 2, 20, 2)
                        style "textbutton_no_padding"
                        text_style "serum_text_style_header"
                        action CaptureFocus("wardrobe_dropdown")

                    if show_personalisation:
                        textbutton "Personalisation Active":
                            align (1.0, 0.5)
                            padding (2, 2)
                            style "textbutton_no_padding"
                            text_style "serum_text_style"
                            action NullAction()
                            tooltip "When an outfit is chosen from this wardrobe the girl will change it based on her preferences"

                    if debug_log_enabled and hasattr(current_wardrobe, "filename") and current_wardrobe.filename:
                        textbutton "Reload Wardrobe":
                            align (1.0, 0.5)
                            padding (2, 2)
                            style "textbutton_no_padding"
                            text_style "serum_text_style"
                            action Function(current_wardrobe.reload)
                            tooltip "Reload wardrobe from original XML file"

        hbox:
            spacing 20
            for category_info in outfit_info_array:
                if category_info[0]:
                    frame:
                        background "#1a45a1aa"
                        xsize 450
                        ysize 850
                        viewport:
                            scrollbars "vertical"
                            xsize 450
                            ysize 850
                            mousewheel True
                            vbox:
                                text "[category_info[1]]s" style "menu_text_title_style" size 30 xalign 0.5 #Add an s to make it plural so we can reuse the field in the new button. Yep, I'm that clever-lazy.
                                if show_make_new:
                                    textbutton "Create New [category_info[1]]":
                                        action Return([category_info[2], current_wardrobe])
                                        sensitive True
                                        style "textbutton_style"
                                        text_style "serum_text_style_header"
                                        xfill True

                                    null height 20

                                for outfit in sorted(getattr(current_wardrobe, category_info[6]), key = lambda x, prop = category_info[3]: getattr(x, prop)):
                                    $ enabled = True
                                    if callable(outfit_validator):
                                        $ enabled = outfit_validator(outfit, category_info[7])
                                    elif slut_limit:
                                        $ enabled = getattr(outfit, category_info[3]) <= slut_limit
                                    textbutton f"{outfit.name}\n{getattr(outfit, category_info[3])} {{image=gold_heart_token_small}}":
                                        if main_selectable:
                                            action [
                                                Function(hide_mannequin),
                                                Return(["select", current_wardrobe, outfit.get_copy()])
                                            ]
                                            tooltip "Pick this outfit."
                                        else:
                                            action NullAction()
                                        sensitive enabled
                                        hovered [
                                            SetScreenVariable("demo_outfit", outfit),
                                            Function(preview_outfit)
                                        ]
                                        unhovered [
                                            SetScreenVariable("demo_outfit", None),
                                            Function(hide_mannequin)
                                        ]
                                        style "textbutton_style"
                                        text_style "outfit_description_style"
                                        xfill True

                                    if show_export or show_modify or show_duplicate or show_delete:
                                        hbox:
                                            yoffset -4
                                            spacing 6
                                            if show_export:
                                                default exported = []
                                                textbutton "Export":
                                                    action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = category_info[4], wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")]
                                                    sensitive outfit not in exported
                                                    hovered [
                                                        SetScreenVariable("demo_outfit", outfit),
                                                        Function(preview_outfit)
                                                    ]
                                                    unhovered [
                                                        SetScreenVariable("demo_outfit", None),
                                                        Function(hide_mannequin)
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "outfit_description_style"
                                                    tooltip "Export this outfit. The export will be added as an xml section in game/wardrobes/Exported_Wardrobe.xml."
                                                    xsize 100

                                            if show_modify:
                                                textbutton "Modify":
                                                    action Return(["modify", current_wardrobe, outfit.get_copy()]) #If we are modifying an outfit just return it. outfit management loop will find which category it is in.
                                                    sensitive (getattr(outfit, category_info[3]) <= slut_limit)
                                                    hovered [
                                                        SetScreenVariable("demo_outfit", outfit),
                                                        Function(preview_outfit)
                                                    ]
                                                    unhovered [
                                                        SetScreenVariable("demo_outfit", None),
                                                        Function(hide_mannequin)
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "outfit_description_style"
                                                    tooltip "Modify this outfit."
                                                    xsize 100

                                            if show_duplicate:
                                                textbutton "Duplicate":
                                                    action [Function(category_info[5], current_wardrobe, outfit.get_copy()), Return(["duplicate", current_wardrobe, outfit.get_copy()])]
                                                    #sensitive (getattr(outfit, category_info[3]) <= slut_limit)
                                                    hovered [
                                                        SetScreenVariable("demo_outfit", outfit),
                                                        Function(preview_outfit)
                                                    ]
                                                    unhovered [
                                                        SetScreenVariable("demo_outfit", None),
                                                        Function(hide_mannequin)
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "outfit_description_style"
                                                    tooltip "Duplicate this outfit and edit the copy, leaving the original as it is."
                                                    xsize 100

                                            if show_delete:
                                                textbutton "Delete":
                                                    action [Function(current_wardrobe.remove_outfit, outfit), SetScreenVariable("demo_outfit", None), Function(hide_mannequin)]
                                                    #sensitive (getattr(outfit, category_info[3]) <= slut_limit)
                                                    hovered [
                                                        SetScreenVariable("demo_outfit", outfit),
                                                        Function(preview_outfit)
                                                    ]
                                                    unhovered [
                                                        SetScreenVariable("demo_outfit", None),
                                                        Function(hide_mannequin)
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "outfit_description_style"
                                                    tooltip "Remove this outfit from your wardrobe. This cannot be undone!"
                                                    xsize 100

                                    null height 5

        if slut_limit != 999:
            frame:
                background "#888888"
                text f"Slut Limit: {min(slut_limit, 100)} {{image=gui/heart/gold_heart.png}}" style "textbutton_text_style" text_align 0.0
    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [
                Function(hide_mannequin),
                Function(renpy.free_memory),
                Return(["finish", current_wardrobe])
            ]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    if GetFocusRect("wardrobe_dropdown"):
        dismiss action ClearFocus("wardrobe_dropdown")
        nearrect:
            focus "wardrobe_dropdown"

            # Finally, this frame contains the choices in the dropdown, with
            # each using ClearFocus to dismiss the dropdown.
            frame:
                background "#0a142688"
                modal True
                xsize 300
                vbox:
                    spacing 0
                    for w in [(mc.designed_wardrobe, False), (nurse_uniforms, False), (barista_uniforms, False), (maid_uniforms, False), (doctor_job.wardrobe, False)] + [(x.wardrobe, x.allow_personalisation) for x in limited_wardrobes if x.allow_edit]:
                        textbutton "[w[0].name]":
                            text_style "serum_text_style"
                            style "textbutton_style"
                            xfill True
                            action [ SetScreenVariable("current_wardrobe", w[0]), SetScreenVariable("show_personalisation", w[1]), ClearFocus("wardrobe_dropdown") ]

    use default_tooltip("outfit_select_manager")
