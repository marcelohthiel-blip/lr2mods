init 10 python:
    class CharacterPoser():
        def __init__(self, person: Person = None, position: str = "default", xalign = .5, yalign = .5, zoom = 1, order = 1):
            self.person = person
            self.position = position
            self.xalign = xalign
            self.yalign = yalign
            self.zoom = zoom
            self.order = order
            self.base_transform = None

    def update_position(char, position):
        char.position = position
        update_drawn_characters()

    def update_drawn_characters():
        clear_scene()
        cs = renpy.current_screen()
        for x in range(3):
            char = cs.scope["chars"][x]
            char.person.draw_person(position = char.position, show_person_info = False, wipe_scene = False,
                display_transform = character_poser(xalign = char.xalign, yalign = char.yalign, zf = char.zoom), display_zorder = char.order)

    def show_character_poser_requirement():
        return debug_log_enabled

    character_poser_action = Action("Character Poser", show_character_poser_requirement, "show_character_poser")

label show_character_poser():
    $ hide_ui()
    call screen position_test_screen()
    $ show_ui()
    return

transform character_poser(xalign = 0, yalign = 0, zf = 1):
    align (xalign, yalign)
    xzoom zf
    yzoom zf


screen position_test_screen():
    layer "hud"
    zorder 200

    default chars = [CharacterPoser(mom, xalign = .2), CharacterPoser(lily, xalign = .4), CharacterPoser(aunt, xalign = .6)]
    default cur_char = None
    default select_position = False

    hbox:
        pos (40, 860)
        for char in chars:
            use position_test_character_screen(char)

    frame:
        background None
        pos (0,0)
        textbutton "Draw":
            style "textbutton_no_padding"
            text_style "menu_text_style"
            action [Function(update_drawn_characters)]

    frame:
        background "#0a142688"
        align (0.9, 0.98)
        xysize (300, 120)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [Return()]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"


    if select_position:
        frame:
            background "#0a142688"
            pos (1700, 200)
            xsize 220
            vbox:
                spacing 0
                for x in supported_positions:
                    textbutton "[x]":
                        text_style "serum_text_style"
                        style "textbutton_style"
                        xfill True
                        sensitive True
                        action [
                            Function(update_position, cur_char, x),
                            ToggleScreenVariable("select_position", True, False),
                            SetScreenVariable("cur_char", None),
                            Function(renpy.restart_interaction)
                        ]

screen position_test_character_screen(char):
    frame:
        background "#0a142688"
        xysize (450, 200)
        has vbox

        hbox:
            text "Position:" style "menu_text_style"
            textbutton "[char.position]":
                style "textbutton_no_padding"
                text_style "menu_text_style"
                action [SetScreenVariable("cur_char", char), ToggleScreenVariable("select_position", True, False)]


        hbox:
            text f"X-Align:\n{char.xalign:.2f}" style "menu_text_style"
            bar:
                value FieldValue(char, "xalign", 1.0, step = .01)
                xysize (300, 40)
                style style.slider

        hbox:
            text f"Y-Align:\n{char.yalign:.2f}" style "menu_text_style"
            bar:
                value FieldValue(char, "yalign", 1.0, step = .01)
                xysize (300, 40)
                style style.slider

        hbox:
            text f"Zoom:\n{char.zoom:.2f}" style "menu_text_style"
            bar:
                value FieldValue(char, "zoom", 2.00, step = .01)
                xysize (300, 40)
                style style.slider


        hbox:
            text f"Order:\n{char.order:.0f}" style "menu_text_style"
            bar:
                value FieldValue(char, "order", 5, step = 1)
                xysize (300, 40)
                style style.slider


        # hbox:
        #     text "Y-Pos:"
        #     input:
        #         value local_ypos
        #         default char.yalign
        #         allow ".0123456789"
        #         style "menu_text_style"
        #         length 8
