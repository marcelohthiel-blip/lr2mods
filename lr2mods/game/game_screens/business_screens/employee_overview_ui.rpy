init 1 python:
    def people_list_potential_stat(people):
        r_stat = 0
        p_stat = 0
        s_stat = 0
        m_stat = 0
        h_stat = 0
        salary = 0
        for person in people:
            if person in mc.business.research_team + mc.business.college_interns_research:
                r_stat += person.research_potential
            if person in mc.business.production_team + mc.business.college_interns_production:
                p_stat += person.production_potential
            if person in mc.business.supply_team + mc.business.college_interns_supply:
                s_stat += person.supply_potential
            if person in mc.business.market_team + mc.business.college_interns_market:
                m_stat += person.marketing_potential
            if person in mc.business.hr_team + mc.business.college_interns_HR:
                h_stat += person.human_resource_potential
            salary += person.salary

        return [["Salary", round(salary, 2), "$", ""], ["Research", r_stat, "", "points"], ["Production", p_stat, "", "points"], ["Supply", s_stat, "", "units"], ["Marketing", m_stat, "", "people"], ["HR", h_stat, "", "%"]]

transform overview_button():
    xysize (400, 80)

screen employee_overview(white_list = None, black_list = None, person_select = False, allow_none = False): #If select is True it returns the person's name who you click on. If it is false it is a normal overview menu that lets you bring up their detailed info.
    modal True
    zorder 100
    add paper_background_image
    default button_mappings = [["All","none", 0],["Research","r", 0],["Production","p", 0],["Supply","s", 0],["Marketing","m", 0],["Human Resources","h", 0]]
    default division_select = "none"
    default division_name = "All"
    default sort_employees_by = "name"
    default show_list = "Staff"
    default reverse_sort = False
    default sort_attributes = [
        ["Name", "name"],
        ["Salary", "salary"],
        ["Happiness", "happiness"],
        ["Obedience", "obedience"],
        ["Love", "love"],
        ["Sluttiness", "sluttiness"],
        ["Suggest", "suggestibility"],
        ["Charisma", "charisma"],
        ["Intellect", "int"],
        ["Focus", "focus"],
        ["Research", "research_skill"],
        ["Production", "production_skill"],
        ["Supply", "supply_skill"],
        ["Marketing", "market_skill"],
        ["HR", "hr_skill"]
        ]


    python:
        if not white_list: #If a white list is passed we will only display people that are on the list
            white_list = []
        if not black_list:
            black_list = [] #IF a black list is passed we will not include anyone on the blacklist. Blacklist takes priority


    $ showing_team = []
    $ display_list = []
    $ valid_person_count = 0

    python:
        total_count = 0
        for x in range(1, len(button_mappings)):
            if show_list == "Staff":
                div_count = mc.business.get_employee_count(button_mappings[x][1])
            else:
                div_count = mc.business.get_intern_count(button_mappings[x][1])
            total_count += div_count
            button_mappings[x][2] = div_count
        button_mappings[0][2] = total_count

        if division_select == "none":
            if show_list == "Staff":
                showing_team = mc.business.employee_list
            else:
                showing_team = mc.business.intern_list
            division_name = "Everyone"
        elif division_select == "r":
            if show_list == "Staff":
                showing_team = mc.business.research_team #ie. take a shallow copy, so we can modify the team without everything exploding.
            else:
                showing_team = mc.business.college_interns_research
            division_name = "Research"
        elif division_select == "p":
            if show_list == "Staff":
                showing_team = mc.business.production_team
            else:
                showing_team = mc.business.college_interns_production
            division_name = "Production"
        elif division_select == "s":
            if show_list == "Staff":
                showing_team = mc.business.supply_team
            else:
                showing_team = mc.business.college_interns_supply
            division_name = "Supply Procurement"
        elif division_select == "m":
            if show_list == "Staff":
                showing_team = mc.business.market_team
            else:
                showing_team = mc.business.college_interns_market
            division_name = "Marketing"
        elif division_select == "h":
            if show_list == "Staff":
                showing_team = mc.business.hr_team
            else:
                showing_team = mc.business.college_interns_HR
            division_name = "Human Resources"

        display_list = [person for person in showing_team if (not white_list or person in white_list) and (not black_list or person not in black_list)] #Create our actual display list using people who are either on the white list or not on the black list

    vbox:
        xalign 0.5
        xanchor 0.5
        yalign 0.05
        yanchor 0.0
        spacing 5
        xsize 1860
        frame:
            background "#1a45a1aa"
            xsize 1860
            ysize 60
            if person_select:
                text "[show_list] Selection" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_title_style"
            else:
                text "[show_list] Review" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_title_style"
        frame:
            background "#1a45a1aa"

            hbox:
                xfill True
                xalign 0.5
                xanchor 0.5
                spacing 40
                for button_map in button_mappings:
                    frame:
                        xsize 274
                        ysize 60
                        background ("#4f7ad6" if division_select == button_map[1] else "#1a45a1")
                        button:
                            action SetScreenVariable("division_select", button_map[1])
                            hover_background "#4f7ad6"
                            xsize 262
                            ysize 48
                            text f"{button_map[0]} ({button_map[2]})" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "textbutton_text_style"

        $ grid_count = (15 if show_list == "Staff" else 14)
        if person_select:
            $ grid_count += 1
        frame:

            yanchor 0.0
            background "#1a45a1aa"
            ysize 60

            grid grid_count 1 ysize 60 xfill True:
                if person_select:
                    frame:
                        background None
                        xsize 90
                for attribute in sort_attributes:
                    if show_list != "Staff" and attribute[1] == "salary":
                        continue
                    frame:
                        background None
                        textbutton "[attribute[0]]":
                            style "textbutton_style"
                            text_style "menu_text_style"
                            xfill True
                            if sort_employees_by == attribute[1]:
                                action [
                                    SetScreenVariable("sort_employees_by", attribute[1]),
                                    ToggleScreenVariable("reverse_sort")
                                ]
                            else:
                                action [
                                    SetScreenVariable("sort_employees_by", attribute[1]),
                                ]
                            if sort_employees_by == attribute[1]:
                                background "#4f7ad6"
                            margin (5, 0)

        frame:
            ypos -5
            yanchor 0.0
            background "#1a45a1aa"
            xfill True
            viewport:
                if builtins.len(display_list) > 5:
                    scrollbars "vertical"
                mousewheel True
                ysize 620
                grid grid_count builtins.len(display_list) xfill True:
                    for person in sorted(display_list, key = lambda person: getattr(person, renpy.current_screen().scope["sort_employees_by"]), reverse = renpy.current_screen().scope["reverse_sort"]):
                        $ show_employee_status = ""
                        if person.is_at_office and person.current_job.job_happiness_score < 0:
                            $ show_employee_status += " {image=sad_token_small}"
                        if person_select:
                            textbutton "Select" style "textbutton_style" text_style "menu_text_style" action Return(person) xsize 100
                        frame:
                            background None
                            xsize 148
                            ysize 80
                            textbutton "[person.name]\n[person.last_name][show_employee_status]":
                                style "textbutton_style" text_style "menu_text_style"
                                action Show("person_info_detailed", None, person)
                                xfill True
                                xalign 0.0
                                yfill True
                                margin (2, 0)
                                hover_background "#4f7ad6"
                                background ("#a1451aaa" if show_employee_status != "" else None)


                        for attribute in sort_attributes[1:]:
                            if show_list != "Staff" and attribute[1] == "salary":
                                continue
                            frame:
                                background None
                                xsize 124
                                margin (2,0)
                                if attribute[1] == "salary":
                                    text f"${getattr(person, attribute[1]):.2f}" style "menu_text_style" xfill True xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                else:
                                    text str(getattr(person, attribute[1])) style "menu_text_style" xfill True xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5

        frame: # Create a frame that displays production / research / supply / hr per turn when filtering by departments
            background "#1a45a1aa"
            hbox:
                xfill True
                xalign 0.5
                xanchor 0.5
                spacing 10
                for stat in (x for x in people_list_potential_stat(display_list) if x[1] != 0):
                    frame:
                        background None
                        xsize 300
                        ysize 60
                        text "[stat[0]]: [stat[2]] [stat[1]] [stat[3]]" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "textbutton_text_style"

    if not person_select or allow_none:
        frame:
            background None
            anchor (0.5,0.5)
            align (0.5,0.98)
            xysize (300,80)
            imagebutton:
                align (0.5,0.5)
                idle At("gui/button/choice_idle_background.png", overview_button)
                hover At("gui/button/choice_hover_background.png", overview_button)
                focus_mask At("gui/button/choice_idle_background.png", overview_button)
                action [Hide("employee_overview"), Return()]
            textbutton "Return" align [0.5,0.5] style "return_button_style"
    if mc.business.college_interns_unlocked:
        frame:
            background None
            anchor (0.5,0.5)
            align (0.8,0.98)
            xysize (300,80)
            imagebutton:
                align (0.5,0.5)
                idle At("gui/button/choice_idle_background.png", overview_button)
                hover At("gui/button/choice_hover_background.png", overview_button)
                focus_mask At("gui/button/choice_idle_background.png", overview_button)
                action SetScreenVariable("show_list", ("Interns" if show_list == "Staff" else "Staff"))
            textbutton ("Interns" if show_list == "Staff" else "Staff") align [0.5,0.5] style "return_button_style"
