
transform overview_button():
    xysize (400, 80)

screen mc_appointment_schedule(): #Displays MC's full schedule for the next week.
    modal True
    zorder 100
    add paper_background_image
    default day_frames = [["Monday", 0], ["Tuesday", 1], ["Wednesday", 2], ["Thursday", 3], ["Friday", 4], ["Saturday", 5], ["Sunday", 6]]
    default time_frames = [["Early Morning", 0], ["Morning", 1], ["Afternoon", 2], ["Evening", 3], ["Night", 4]]
    default appt_list = True

    $ showing_team = []
    $ display_list = []
    $ appointment_dict = []
    # $ event_dict = []
    $ valid_person_count = 0

    python:
        for day_slot in [0,1,2,3,4,5,6]:
            appointment_dict.append(mc.schedule.get_formatted_day_appt_schedule((day + day_slot) % 7))
            # event_dict.append(mc.schedule.get_formatted_day_event_schedule((day + day_slot) % 7))

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
            if appt_list:
                text "Appointment Schedule" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_title_style"
            else:
                text "Event Schedule" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 36 style "menu_text_title_style"
        frame:
            background "#1a45a1aa"

            hbox:
                xfill True
                xalign 0.5
                xanchor 0.5
                spacing 40
                for day_frame in day_frames:
                    frame:
                        background "#09296faa"
                        xsize 230
                        ysize 800
                        use show_single_day_schedule((day + day_frame[1]) % 7)

    frame:
        background "#1a45a1aa"
        xsize 600
        ysize 80
        anchor (0.5,0.5)
        align (0.8,0.96)
        text "Mandatory Events In {b}Bold{/b}\nOptional Events In {i}Italics{/i}" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 size 24 style "textbutton_text_style"
    frame:
        background None
        anchor (0.5,0.5)
        align (0.3,0.96)
        xysize (300,80)
        imagebutton:
            align (0.5,0.5)
            idle At("gui/button/choice_idle_background.png", overview_button)
            hover At("gui/button/choice_hover_background.png", overview_button)
            focus_mask At("gui/button/choice_idle_background.png", overview_button)
            action [Hide("mc_appointment_schedule")]
        textbutton "Return" align [0.5,0.5] style "return_button_style"

screen show_single_day_schedule(day_index = 0):
    zorder 200  #Not sure if this should be here
    $ appointment_list = mc.schedule.get_formatted_day_appt_schedule(day_index % 7)

    frame:
        background "#09296f6c"
        xsize 230
        ysize 800
        vbox:
            spacing 10
            for entry in appointment_list:
                textbutton "[entry]":
                    xysize (220, 120)
                    align (0.5, 0.5)
                    style "textbutton_style"
                    if entry != appointment_list[0]:
                        text_style "menu_text_style"
                        background "#214593"
                    else:
                        text_style "textbutton_text_style"
                        background "#4f7ad6"
                    text_align (0.5,0.5)
