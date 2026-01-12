# Assign Division Daily Serum UI - Based on screen designed by DaMatt
# to be put in \game\Mods\Screens\Serum_Screens\

init 2 python:
    def get_division_serum_name(division):
        serum = get_division_serum(division)
        if serum:
            return serum.name
        else:
            return "No serum"

    def get_division_serum(division):
        if not hasattr(division[1], division[2]):
            setattr( division[1], division[2], None);
        return getattr(division[1], division[2])

    def set_division_serum(division, serum):
        setattr( division[1], division[2], serum)

    def get_division_serum_mapping():
        mapping = [
            ("Research", mc.business, "r_serum"),
            ("Production", mc.business, "p_serum"),
            ("Supply", mc.business, "s_serum"),
            ("Marketing", mc.business, "m_serum"),
            ("Human Resources", mc.business, "h_serum")
        ]
        if mc.business.event_triggers_dict.get("foreclosed_stage", 0) >= 5:
            mapping.append(("Strippers", mc.business, "strippers_serum"))
        if builtins.len(mc.business.stripclub_waitresses) > 0:
            mapping.append(("Waitresses", mc.business, "waitresses_serum"))
        if bdsm_room_available():
            mapping.append(("BDSM performers", mc.business, "bdsm_performers_serum"))
        if strip_club_has_manager_or_mistress():
            mapping.append(("Manager/Mistress", mc.business, "manager_serum"))
        return mapping

init 2:
    screen assign_division_serum():
        add science_menu_background_image

        default division_selected = -1
        default division_serums = get_division_serum_mapping()

        vbox:
            xalign 0.5
            xanchor 0.5
            yalign 0.05
            yanchor 0.0
            spacing 20
            frame:
                background "#1a45a1aa"
                xsize 1860
                ysize 60
                text "Assign Daily Serum Dose" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_title_style"

            hbox:
                vbox:
                    xsize 500
                    yalign 0.0

                    frame:
                        background "#777777"
                        xalign 0.5

                        hbox:
                            xalign 0.5
                            vbox:
                                frame:
                                    xsize 500
                                    ysize 50
                                    background "#000080"
                                    text "Division" style "menu_text_title_style" xalign 0.5

                                viewport:
                                    xsize 500
                                    ysize 700
                                    xalign 0.5
                                    spacing 0

                                    vbox:
                                        for division in builtins.range(0,builtins.len(division_serums)):
                                            $ division_name = division_serums[division][0]
                                            $ serum_name = get_division_serum_name(division_serums[division])
                                            button:
                                                vbox:
                                                    xalign 0.5
                                                    text "[division_name]" style "serum_text_style"
                                                    text "[serum_name]" style "serum_text_style" size 14
                                                style "textbutton_style"
                                                background ("#000080" if division_selected else "#222222")
                                                hover_background ("#0030A0" if division_selected else "#333333")
                                                xsize 500
                                                action SetScreenVariable("division_selected", division)

                null width 10

                vbox:
                    xsize 500
                    if division_selected > -1:

                        frame:
                            background "#777777"
                            xalign 0.5

                            hbox:
                                xalign 0.5
                                vbox:
                                    frame:
                                        xsize 500
                                        ysize 50
                                        background "#000080"
                                        text "Assign Serum" style "menu_text_title_style" xalign 0.5

                                    viewport:
                                        scrollbars "vertical"
                                        mousewheel True
                                        xsize 500
                                        ysize 700
                                        xalign 0

                                        vbox:

                                            button:
                                                xsize 500
                                                ysize 38
                                                xalign 0.5
                                                text "No serum" style "serum_text_style"
                                                style "textbutton_style"
                                                sensitive True
                                                if get_division_serum(division_serums[division_selected]) is None:
                                                    background "#000080"
                                                    hover_background "#0030A0"
                                                else:
                                                    background "#222222"
                                                    hover_background "#333333"
                                                action Function(set_division_serum, division_serums[division_selected], None)

                                            for design, dose_count in sorted(mc.business.inventory.serums_held, key = lambda e: e[0].name):
                                                button:
                                                    xsize 500
                                                    ysize 44
                                                    hbox:
                                                        frame:
                                                            background None
                                                            xsize 300
                                                            text "[design.name]" xsize 300 style "serum_text_style"
                                                        frame:
                                                            background None
                                                            text "Available: [dose_count]" style "serum_text_style" size 16
                                                    style "textbutton_style"
                                                    sensitive True
                                                    if get_division_serum(division_serums[division_selected]) == design:
                                                        background "#000080"
                                                        hover_background "#0030A0"
                                                    else:
                                                        background "#222222"
                                                        hover_background "#333333"
                                                    hovered [
                                                        Show("serum_tooltip", None, design, given_align = (0.97,0.11), given_anchor = (1.0,0.0))
                                                    ]
                                                    unhovered [
                                                        Hide("serum_tooltip")
                                                    ]
                                                    action Function(set_division_serum, division_serums[division_selected], design)

            frame:
                background None
                align (0.5, 0.98)
                xysize (300, 150)
                imagebutton:
                    align (0.5, 0.5)
                    auto "gui/button/choice_%s_background.png"
                    focus_mask True
                    action [Hide("assign_division_serum"), Return(), Hide("serum_tooltip")]
                textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

        frame:
            pos (1300, 940)
            xysize (550, 80)
            text "Note that daily serums will only be given to people with the 'Daily Serum Doses' duty assigned." style "serum_text_style" size 22
