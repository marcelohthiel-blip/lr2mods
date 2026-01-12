screen duty_tooltip(duty):
    zorder 130
    frame:
        background None
        vbox:
            spacing 20
            text "[duty.duty_name]" style "serum_text_style_header"
            text "[duty.duty_description]" style "menu_text_style" size 20 text_align 0.0

            transclude
