label edit_uniform(uniform, outfit_type):
    call screen outfit_creator(uniform, outfit_type = outfit_type, target_wardrobe = None)
    if isinstance(_return, Outfit):
        return _return
    return None

init 2 python:
    def edit_uniform(uniform: UniformOutfit):
        outfit_type = "full"
        if uniform.overwear_flag or uniform.outfit.is_suitable_overwear_set:
            outfit_type = "over"
        if uniform.underwear_flag or uniform.outfit.is_suitable_underwear_set:
            outfit_type = "under"
        if uniform.full_outfit_flag: # force back to full
            outfit_type = "full"

        result = renpy.call_in_new_context("edit_uniform", uniform.outfit.get_copy(), outfit_type)

        if isinstance(result, Outfit):
            uniform.outfit = result

screen uniform_manager():
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
            spacing 56

            #text "Name" style "menu_text_style" size 30
            null width 315 + slide_amount

            text "Full" style "menu_text_style" size 25 xsize 50 #TODO: Make these textbuttons so we can have tooltips
            text "Over" style "menu_text_style" size 25 xsize 50
            text "Under" style "menu_text_style" size 25  xsize 50

            null width 10

            text "Market" style "menu_text_style" size 25 xsize 50
            text "R&D" style "menu_text_style" size 25 xsize 50
            text "Prod" style "menu_text_style" size 25 xsize 50
            text "Supply" style "menu_text_style" size 25 xsize 50
            text "HR" style "menu_text_style" size 25 xsize 50
        viewport:
            xalign 0.05
            yalign 0.05
            scrollbars "vertical"
            ysize 750
            mousewheel True
            vbox:
                for uniform in mc.business.business_uniforms:
                    use uniform_entry(uniform)

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
            action [mc.business.update_uniform_wardrobes(), Return()]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    use button_tooltip("uniform_manager")

screen uniform_entry(given_uniform):
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
                    action [Function(hide_mannequin), Function(edit_uniform, given_uniform)]

                imagebutton:
                    auto "gui/button/delete_%s.png"
                    focus_mask True
                    yanchor 0.5
                    yalign 0.5
                    xsize 40
                    tooltip "Remove Uniform"
                    hovered Function(draw_average_mannequin, given_uniform.outfit)
                    unhovered Function(hide_mannequin)
                    action [Function(hide_mannequin), RemoveFromSet(mc.business.business_uniforms, given_uniform)]

                null width 50

            #null
            use uniform_button(state = given_uniform.full_outfit_flag, is_sensitive = given_uniform.can_toggle_full_outfit_state, toggle_function = given_uniform.set_full_outfit_flag)
            use uniform_button(state = given_uniform.overwear_flag, is_sensitive = given_uniform.can_toggle_overwear_state, toggle_function = given_uniform.set_overwear_flag)
            use uniform_button(state = given_uniform.underwear_flag, is_sensitive = given_uniform.can_toggle_underwear_state, toggle_function = given_uniform.set_underwear_flag)

            null
            use uniform_button(state = given_uniform.marketing_flag, is_sensitive = True, toggle_function = given_uniform.set_marketing_flag)
            use uniform_button(state = given_uniform.research_flag, is_sensitive = True, toggle_function = given_uniform.set_research_flag)
            use uniform_button(state = given_uniform.production_flag, is_sensitive = True, toggle_function = given_uniform.set_production_flag)
            use uniform_button(state = given_uniform.supply_flag, is_sensitive = True, toggle_function = given_uniform.set_supply_flag)
            use uniform_button(state = given_uniform.hr_flag, is_sensitive = True, toggle_function = given_uniform.set_hr_flag)

screen uniform_button(state, is_sensitive, toggle_function):
    imagebutton:
        if state:
            idle "gui/extra_images/check_mark.png"
        elif is_sensitive:
            idle "gui/extra_images/uncheck_mark.png"
        else:
            idle "gui/extra_images/empty_token.png"
        background ("#449044" if state else "#904444" if is_sensitive else "#00000088")
        hover_background ("#66a066" if state else "#a06666" if is_sensitive else "#00000088")
        sensitive is_sensitive
        action Function(toggle_function, not state)
        xysize (50, 40)
        padding (9, 4)
        yanchor 0.5 yalign 0.5
