init 2 python:
    def edit_stripclub_uniform(uniform: StripClubOutfit):
        outfit_type = "full"
        if uniform.overwear_flag:
            outfit_type = "over"
        if uniform.underwear_flag:
            outfit_type = "under"

        result = renpy.call_in_new_context("edit_uniform", uniform.outfit.get_copy(), outfit_type)

        if isinstance(result, Outfit):
            uniform.outfit = result


screen stripclub_uniform_manager():
    add paper_background_image
    modal True
    $ slide_amount = 120 #Easier modification for where the headers sit.

    frame:
        background "#0a142688"
        xpos 1520
        ypos 0
        xysize (400, 1080)

    vbox:
        spacing 10
        hbox:
            null width 330 + slide_amount
            text "Uniform Style" style "menu_text_header_style"
            null width 260
            text "Used By"  style "menu_text_header_style"

        null height -20
        hbox:
            hbox:
                spacing 60

                #text "Name" style "menu_text_style" size 30
                null width 315 + slide_amount

                text "Full" style "menu_text_style" size 25 xsize 50 #TODO: Make these textbuttons so we can have tooltips
                text "Over" style "menu_text_style" size 25 xsize 50
                text "Under" style "menu_text_style" size 25  xsize 50

            hbox:
                spacing 30
                null width 60

                text "Stripper" style "menu_text_style" size 25 xsize 50
                text "Waitress" style "menu_text_style" size 25 xsize 50
                text "BDSM" style "menu_text_style" size 25 xsize 50
                text "Manager" style "menu_text_style" size 25 xsize 50
                text "Mistress" style "menu_text_style" size 25 xsize 50
        viewport:
            xalign 0.05
            yalign 0.05
            scrollbars "vertical"
            ysize 750
            mousewheel True
            vbox:
                for uniform in mc.business.stripclub_uniforms:
                    use stripclub_uniform_entry(uniform)

        textbutton "Add Uniform":
            style "textbutton_style"
            text_style "textbutton_text_style"
            xysize (160, 46)
            yanchor 0.5
            yalign 0.5
            background "#43B197"
            hover_background "#143869"
            action Return("Add")

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [mc.business.update_stripclub_wardrobes(), Return(None)]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    use button_tooltip("stripclub_uniform_manager")

screen stripclub_uniform_entry(given_uniform):
    frame:
        background "#0a142688"
        hbox:
            spacing 70
            hbox:
                spacing 10
                textbutton "[given_uniform.outfit.name]":
                    xsize 250
                    yanchor 0.5
                    yalign 0.5
                    hovered Function(draw_average_mannequin, given_uniform.outfit)
                    unhovered Function(hide_mannequin)
                    action NullAction()
                    style "textbutton_style"
                    text_style "textbutton_text_style"

                imagebutton:
                    auto "gui/button/dress_%s.png"
                    focus_mask True
                    yanchor 0.5
                    yalign 0.5
                    xsize 40
                    tooltip "Edit Uniform"
                    hovered Function(draw_average_mannequin, given_uniform.outfit)
                    unhovered Function(hide_mannequin)
                    action [Function(hide_mannequin), Function(edit_stripclub_uniform, given_uniform)]

                imagebutton:
                    auto "gui/button/delete_%s.png"
                    focus_mask True
                    yanchor 0.5
                    yalign 0.5
                    xsize 40
                    tooltip "Remove Uniform"
                    hovered Function(draw_average_mannequin, given_uniform.outfit)
                    unhovered Function(hide_mannequin)
                    action [Function(hide_mannequin), RemoveFromSet(mc.business.stripclub_uniforms, given_uniform)]

                null width 50

            #null
            use uniform_button(state = given_uniform.full_outfit_flag, is_sensitive = given_uniform.can_toggle_full_outfit_state, toggle_function = given_uniform.set_full_outfit_flag)
            use uniform_button(state = given_uniform.overwear_flag, is_sensitive = given_uniform.can_toggle_overwear_state, toggle_function = given_uniform.set_overwear_flag)
            use uniform_button(state = given_uniform.underwear_flag, is_sensitive = given_uniform.can_toggle_underwear_state, toggle_function = given_uniform.set_underwear_flag)

            null #Spacing purposes
            use uniform_button(state = given_uniform.stripper_flag, is_sensitive = True, toggle_function = given_uniform.set_stripper_flag)
            use uniform_button(state = given_uniform.waitress_flag, is_sensitive = True, toggle_function = given_uniform.set_waitress_flag)
            use uniform_button(state = given_uniform.bdsm_flag, is_sensitive = True, toggle_function = given_uniform.set_bdsm_flag)
            use uniform_button(state = given_uniform.manager_flag, is_sensitive = True, toggle_function = given_uniform.set_manager_flag)
            use uniform_button(state = given_uniform.mistress_flag, is_sensitive = True, toggle_function = given_uniform.set_mistress_flag)
