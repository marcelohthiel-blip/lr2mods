screen serum_inventory_select_ui(the_inventory, the_person = None, batch_size = 1, select_requirement = None): #Used to let the player select a serum from an inventory.
    add science_menu_background_image
    frame:
        background "#1a45a1aa"
        xysize (440, 900)
        pos (40, 20)
        anchor (0.0, 0.0)
        vbox:
            frame:
                background "#000080"
                xsize 420
                text "Serum Available" style "serum_text_style_header"

            null height 10

            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox:
                    for serum, dose_count in sorted(the_inventory.serums_held, key = lambda x: x[0].name):
                        textbutton "[serum.name] - [dose_count] Doses":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            xsize 400

                            xalign 0.5
                            xanchor 0.5
                            yalign 0.5
                            yanchor 0.5

                            action [Hide("serum_tooltip"),Return(serum)]
                            hovered Show("serum_tooltip",None,serum, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                            sensitive dose_count >= batch_size and (not callable(select_requirement) or select_requirement(serum))

    if batch_size > 1:
        frame:
            background "#00000088"
            xysize (240, 34)
            pos (40, 930)
            anchor (0.0, 0.0)
            text "Required: [batch_size] serums" style "textbutton_text_style" text_align 0.0


    if the_person:
        frame:
            background None
            anchor [0.5, 0.5]
            align [0.5,0.2]
            use serum_tolerance_indicator(the_person)

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [Hide("serum_tooltip"), Return(None)]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"


    use default_tooltip("serum_inventory_select_ui")
