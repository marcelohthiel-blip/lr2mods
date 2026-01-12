init 5 python:
    def set_active_IT_project(project):
        if mc.business.current_IT_project and mc.business.current_IT_project_progress < mc.business.current_IT_project.project_cost and mc.business.current_IT_project_progress > 0:
            mc.business.IT_partial_projects[mc.business.current_IT_project.identifier] = mc.business.current_IT_project_progress
        if project.identifier in mc.business.IT_partial_projects:
            mc.business.current_IT_project = project
            mc.business.current_IT_project_progress = mc.business.IT_partial_projects.get(project.identifier, 0)
            mc.business.IT_partial_projects.pop(project.identifier, None)
        else:
            mc.business.current_IT_project = project
            mc.business.current_IT_project_progress = 0
        return

    def IT_toggle_project(project):
        if project in mc.business.active_IT_projects:
            project.remove_policy()
            # print("Toggle project: " + project.name + " -> Removed")
        else:
            project.apply_policy()
            # print("Toggle project: " + project.name + " -> Added")


label check_business_it_projects():
    call screen business_project_screen()
    return

label check_nanobot_it_projects():
    call screen nanobot_project_screen()
    return

init 5:

    screen it_project_screen():
        add IT_background_image
        modal True
        zorder 100
        use screen_IT_active_project()
        use screen_IT_return_button()
        vbox:
            #xanchor 0.5
            #xalign 0.5
            xcenter 960
            yalign 0.2
            # background "#1a45a1aa"
            text "Manage your IT projects" style "menu_text_title_style" size 48 xanchor 0.5 xalign 0.5
            null height 60
            hbox:
                xanchor 0.5
                xalign 0.5
                yalign 0.4
                spacing 40

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    xysize (500, 300)
                    fixed:
                        imagebutton:
                            auto "gui/button/choice_%s_background.png"
                            action ui.callsinnewcontext("check_business_it_projects")
                            align (0.5, 0.5)
                        textbutton "Business Project" align [0.5,0.4] text_style "menu_text_title_style" text_size 36

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    xysize (500, 300)
                    fixed:
                        imagebutton:
                            auto "gui/button/choice_%s_background.png"
                            action ui.callsinnewcontext("check_nanobot_it_projects")
                            align (0.5, 0.5)
                        textbutton "Nanobot Project" align [0.5,0.4] text_style "menu_text_title_style" text_size 36

    screen nanobot_project_screen():
        add IT_background_image
        modal True
        zorder 100
        use screen_IT_active_project()
        use screen_IT_return_button()
        vbox:

            xcenter 960
            yalign 0.1
            # background "#1a45a1aa"
            text "Select a New Nanobot Project" style "menu_text_title_style" size 42 xanchor 0.5 xalign 0.5
            null height 60
            hbox:
                xanchor 0.5
                xalign 0.5
                yalign 0.4
                spacing 40
                for name, nano_info_data in {
                        "Basic": ["basic", always_true_requirement, None],
                        "Breeder": ["breeder", fetish_breeding_serum_is_unlocked, breeder_unlock_project],
                        "Anal": ["anal", fetish_anal_serum_is_unlocked, anal_unlock_project],
                        "Cum": ["cum", fetish_cum_serum_is_unlocked, cum_unlock_project],
                        "Exhibitionism": ["exhibition", fetish_exhibition_serum_is_unlocked, exhibition_unlock_project]
                        }.items():
                    frame:
                        background "#1a45a1aa"
                        xalign 0.5
                        xanchor 0.5
                        vbox:
                            xsize 300
                            text "[name]" style "menu_text_title_style" size 28 xalign 0.5
                            if nano_info_data[1]():
                                for project in IT_get_nanobot_projects(nano_info_data[0]):
                                    use screen_IT_project_button(project)

                                if name == "Exhibitionism":
                                    text "{color=#ffff00}NOT AN EXPLICIT FETISH IN GAME{/color}" style "serum_text_style_traits"
                            elif nanobot_program_is_IT():
                                use screen_IT_project_button(nano_info_data[2])
                            else:
                                text "{color=#ff0000} Not Unlocked {/color}" style "menu_text_title_style" size 18 xanchor 0.5 xalign 0.5


    screen business_project_screen():
        add IT_background_image
        modal True
        zorder 100
        use screen_IT_active_project()
        use screen_IT_return_button()
        vbox:

            xcenter 960
            yalign 0.1
            # background "#1a45a1aa"
            text "Select a New Business IT Project" style "menu_text_title_style" size 42 xanchor 0.5 xalign 0.5
            null height 60
            hbox:
                xanchor 0.5
                xalign 0.5
                yalign 0.4
                spacing 40
                for name, category in {
                        "HR": "HR",
                        "Supply": "supply",
                        "Marketing": "market",
                        "Research": "research",
                        "Production": "production"}.items():
                    frame:
                        background "#1a45a1aa"
                        xalign 0.5
                        xanchor 0.5
                        vbox:
                            xsize 300
                            text [name] style "menu_text_title_style" size 28 xalign 0.5
                            for project in IT_get_business_projects(category):
                                use screen_IT_project_button(project)


screen IT_tooltip(the_project):
    $ hint_height = 150
    $ window_height = hint_height
    $ proj_desc = the_project.desc
    $ proj_name = the_project.name

    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 440
        #xalign 0.1
        ycenter 940
        xsize 760
        ysize window_height

        vbox:
            spacing 5
            frame:
                background Frame("gui/frame.png", 5,5)
                xsize 750
                ysize hint_height - 10
                ypadding 15
                xpadding 30
                vbox:
                    spacing 0
                    text "{size=24}[proj_name]{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                    text "{size=18}[proj_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2

screen screen_IT_active_project():
    $ hint_height = 150
    $ window_height = hint_height
    if mc.business.current_IT_project:
        $ proj_desc = mc.business.current_IT_project.name
    else:
        $ proj_desc = "Unassigned!"
    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 1160
        #xalign 0.1
        ycenter 940
        xsize 360
        ysize window_height

        vbox:
            spacing 5
            frame:
                background Frame("gui/frame.png", 5,5)
                xsize 350
                ysize hint_height - 10
                ypadding 15
                xpadding 30
                vbox:
                    spacing 0
                    text "{size=24}Current Project:{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                    text "{size=18}[proj_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                    if proj_desc != "Unassigned!":
                        bar:
                            value mc.business.current_IT_project_progress
                            range mc.business.current_IT_project.project_cost
                            xalign 0.5
                            yalign 0.5
                            xysize (200, 20)

screen screen_IT_project_button(proj):
    frame:
        background None
        ysize 160
        xalign 0.5
        if proj not in mc.business.IT_projects:
            if proj.requirement() == True:
                imagebutton:
                    ysize 160
                    auto "gui/button/IT_button_a_%s.png"
                    action Function (set_active_IT_project, proj)
                    sensitive True
                    if mc.business.current_IT_project is not None:
                        selected proj == mc.business.current_IT_project
                    hovered [
                        Show("IT_tooltip",None,proj)
                        ]
            else:
                imagebutton:
                    ysize 160
                    auto "gui/button/IT_button_a_%s.png"
                    sensitive False
                    hovered [
                        Show("IT_tooltip",None,proj)
                        ]

        if proj in mc.business.IT_projects:
            imagebutton:
                ysize 160
                if proj in mc.business.active_IT_projects:
                    auto "gui/button/IT_button_a_%s.png"
                    selected True
                else:
                    idle "gui/button/IT_button_a_inactive.png"
                    hover "gui/button/IT_button_a_hover.png"
                    selected False
                action Function (IT_toggle_project, proj)
                sensitive True
                hovered [
                    Show("IT_tooltip",None,proj)
                    ]
        vbox:
            yanchor 0.0
            xysize (280, 150)
            yoffset 5
            text proj.name size 28 xalign 0.5 xanchor 0.5 style "textbutton_text_style"
            if proj.identifier in mc.business.IT_partial_projects:
                bar:
                    xoffset 40
                    value mc.business.IT_partial_projects.get(proj.identifier, 0)
                    range proj.project_cost
                    xysize (200, 10)

            python:
                supplemental_text = ""
                if mc.business.current_IT_project is not None:
                    if proj == mc.business.current_IT_project:
                        supplemental_text = "In Progress"
                if proj not in mc.business.IT_projects and proj.requirement() != True and proj.requirement():
                    supplemental_text = "{color=#ff0000}" + proj.requirement() + "{/color}"
                elif proj not in mc.business.IT_projects and not  proj.requirement():
                    supplemental_text = "{color=#ff0000} Unknown Req {/color}"

            text supplemental_text style "menu_text_style" size 16 xalign 0.5 xanchor 0.5 yanchor 1.0

screen screen_IT_return_button():
    frame:
        background None
        align (0.92, 0.93)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [
                Hide("it_project_screen"),
                Hide("IT_tooltip"),
                Hide("nanobot_project_screen"),
                Hide("business_project_screen"),
                Hide("screen_IT_active_project"),
                Return()
            ]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

screen in_progress_text_box(x,y):
    text "In Progress" style "menu_text_title_style" size 18 xalign x ypos y
