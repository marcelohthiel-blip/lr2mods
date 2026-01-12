screen floating_notifications():
    layer "hud"
    style_prefix "notify"
    zorder 400

    frame:
        background None
        xminimum 400
        xmaximum 400
        xanchor 1.0
        xalign 1.0
        vbox:
            spacing 2

            for notification in active_notifications:
                frame:
                    background "#00000055"
                    padding (2, 2)
                    text notification.text style notification.text_style size 18 xsize 400
