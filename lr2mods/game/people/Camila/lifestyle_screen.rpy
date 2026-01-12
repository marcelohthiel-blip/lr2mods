# This file contains the provisions for the lifestyle coach screen for setting personal goal lists.
init -2 style textbutton_green_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding (5,5)
    margin (5,5)
    background "#43B197"
    insensitive_background "#239177"
    hover_background "#aaaaaa"

label lifestyle_coach_review_goals_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    $ mc.business.change_funds(-20)
    mc.name "Hey [the_person.title]. Do you have time to talk about goals again?"
    the_person "Certainly! Tell me about how things are going and what you would like to change."
    $ update_available_goals()
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    mc.name "Thanks for the help!"
    $ scene_manager.clear_scene()
    return

screen lifestyle_goal_sheet():
    add paper_background_image
    modal True
    zorder 100

    vbox:
        xanchor 0.5
        xalign 0.5
        yalign 0.1
        frame:
            background "#1a45a1aa"
            xanchor 0.5
            xalign 0.5
            hbox:
                xsize 1600
                ysize 110
                vbox:
                    xsize 600
                    text f"Goal Lists {mc.name} {mc.last_name}" style "menu_text_style" size 36
                    text "Each category requires a minimum of 2 selections" size 20

                $ tooltip = GetTooltip("lifestyle_goal_sheet")
                if tooltip:
                    vbox:
                        xsize 1000
                        text "[tooltip]" size 20

        null height 40
        hbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.4
            spacing 40

            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                use goal_overview("Stat Goals", stat_goals)
            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                use goal_overview("Work Goals", work_goals)
            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                use goal_overview("Sex Goals", sex_goals)

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [Return(True), Hide("serum_tooltip")]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

screen goal_overview(title, goal_list):
    vbox:
        $ active_count = sum(1 for x in goal_list if x.enabled)
        xsize 500
        text "[title]" style "menu_text_style" size 32 xalign 0.5
        text "Current Total: [active_count]"  style "menu_text_style" size 24 xalign 0.5
        for goal in sorted(goal_list, key = lambda x: x.name):
            if goal.available:
                hbox:
                    xalign 0.5
                    textbutton "[goal.name]":
                        xalign 0.5
                        yalign 0.5
                        if goal.enabled:
                            style "textbutton_green_style"
                            sensitive active_count > 2
                        else:
                            style "textbutton_style"
                            sensitive True
                        text_style "textbutton_text_style"
                        action [
                            Function(goal.toggle_enabled)
                        ]
                        tooltip Text(f"{{font=title}}{{size=24}}{goal.name}{{/size}}{{/font}}\n{goal.description}").get_all_text()
