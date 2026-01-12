init 2 python:
    def change_generic_preferences_requirement():
        return True

    change_generic_preferences_action = Action("Change Preferences", change_generic_preferences_requirement, "show_generic_preference_ui", menu_tooltip = "Change the chance of a certain body type / cup size / skin tone will be generated for a random person.")

init 5 python:
    add_label_hijack("normal_start", "activate_generic_preference")
    add_label_hijack("after_load", "activate_generic_preference")

label activate_generic_preference(stack):
    python:
        bedroom.add_action(change_generic_preferences_action)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_generic_preference_ui():
    $ renpy.call_screen("generic_preference_ui")
    return

init 10 python:
    def switch_preference(pref):
        cs = renpy.current_screen()
        cs.scope["pref_selected"] = pref
        preference_value_changed(pref)
        return

    def preference_value_changed(pref):
        cs = renpy.current_screen()

        total = 0
        for x in generic_preference[pref]:
            total += getattr(persistent, generic_preference[pref][x][0])

        cs.scope["current_total"] = total
        return

screen generic_preference_ui():
    modal True
    zorder 49

    default pref_selected = "Body Type"
    default current_total = 100

    frame: # top frame
        background "#0a1426dd"
        xsize 1200
        yalign 0.4
        xalign 0.5
        xanchor 0.5

        vbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.3
            spacing 10

            hbox:
                for pref in sorted(generic_preference):
                    textbutton pref:
                        style "textbutton_style"
                        text_style "menu_text_title_style"
                        xsize 220
                        sensitive pref != pref_selected
                        action [
                            Function(switch_preference, pref) # If a clothing item is selected and currently being previewed then remove it from preview.
                        ]

            for pref in sorted(generic_preference):
                if pref == pref_selected:
                    vbox:
                        for x in (x[0] for x in sorted(generic_preference[pref].items(), key = lambda x: x[1][2])):
                            hbox:
                                spacing 5
                                vbox:
                                    xsize 340
                                    ysize 50
                                    yoffset 5
                                    text x style "textbutton_text_style"
                                vbox:
                                    xsize 600
                                    ysize 50
                                    bar value FieldValue(persistent, generic_preference[pref][x][0], 100, step = 1, style = "slider", action = [ Function(preference_value_changed, pref_selected) ]) xsize 600 ysize 45
                                vbox:
                                    xsize 60
                                    ysize 50
                                    yoffset 5
                                    text (str(getattr(persistent, generic_preference[pref][x][0])) + "%" if getattr(persistent, generic_preference[pref][x][0]) > 0 else "None") style "menu_text_style" xsize 100

            hbox:
                text f"Total: {current_total}%":
                    xalign 1.0
                    style "menu_text_style"

            hbox:
                xsize 800
                text "{size=16}Warning: setting all values to the same value will result in even chance, for correct percentage make sure they sum close to 100. If you want all random characters to adhere to these value, start a new game after you changed these values." style "warning_text"

            hbox:
                xalign 0.5
                textbutton "Close" action [Return()] style "textbutton_style" text_style "textbutton_text_style" text_text_align 0.5 text_xalign 0.5 xysize (155,60)

style warning_text:
    color "B22222"
    size 16
    xalign 0.5
