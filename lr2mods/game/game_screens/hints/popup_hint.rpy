
style popup_hint_frame:
    ypos 210
    xpos 400

    background Frame("gui/notify.png", Borders(180, 140, 380, 340), tile=gui.frame_tile)


screen popup_hint(message):
    zorder 100
    frame:
        style "popup_hint_frame"
        text "{size=24}[message!tq]" at _popup_hint_transform

    # This controls how long it takes between when the screen is
    # first shown, and when it begins hiding.
    timer 5 action Hide('popup_hint')

transform _popup_hint_transform:
    # These control the position.
    xpos 0 ypos 0

    # These control the actions on show and hide.
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init 2 python:
    def show_popup_hint(message):
        if persistent.scene_popups:
            renpy.show_screen("popup_hint", message)
            # show screen popup_hint(message)
        return
