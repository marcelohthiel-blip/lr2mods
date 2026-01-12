screen girl_title_header(person, x_size, y_size, include_details_button = False):
    python:
        job_title = person_info_ui_get_job_title(person)


    frame:
        xsize x_size
        ysize y_size
        xalign 0.5
        background "#1a45a1aa"

        if include_details_button:
            textbutton "Show Details":
                style "textbutton_style"
                text_style "textbutton_text_style"
                action Show("person_info_detailed", None, person)
                xanchor 1.0
                xalign 0.95
                yanchor 0.5
                yalign 0.5

        vbox:
            xalign 0.5 xanchor 0.5
            text "[person.name] [person.last_name]" style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color person.char.who_args["color"] font person.char.what_args["font"]
            if person in mc.business.on_payroll:
                text "Job: [job_title] ($[person.salary:.2f]/day)" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
            else:
                text "Job: [job_title]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

            $ visible_roles = [x.role_name for x in person.special_role if not x.hidden]
            if visible_roles:
                text f"Special Roles: {', '.join(visible_roles)}" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
