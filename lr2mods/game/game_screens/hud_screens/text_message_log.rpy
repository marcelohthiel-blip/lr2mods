init -2 style digital_text_2 is textbutton_style:
    color "#ffffffff"
    outlines [(1,"#000000ff",0,0)]
    yanchor 0.5
    yalign 0.5
    size 18

screen text_message_log(the_person, newest_who = None, newest_what = None):
    default size_x = 460

    fixed:
        xanchor 0.5
        xalign 0.5
        frame:
            imagemap:
                ground phone_background
                hotspot (180, 855, 285, 895) clicked Hide("text_message_log")

            background None
            xanchor 0.5
            xalign 0.5
            yanchor 1.0
            yalign 0.98
            xsize size_x
            ysize 920


            viewport: #The display for the text, which can be scrolled up and down.
                mousewheel True
                scrollbars "vertical"
                xoffset 32
                yoffset 90
                xsize (size_x - 60)
                ysize 732
                yinitial 1.0
                vbox:
                    box_reverse False
                    xanchor 0.5
                    xalign 0.5
                    spacing 10
                    yanchor 1.0
                    yalign 1.0


                    $ display_who = ""
                    $ display_what = ""
                    $ who_align = 0.0
                    $ what_align = 1.0
                    $ display_list = mc.phone.get_message_list(the_person)
                    if newest_what is not None:
                        $ display_list.append((newest_who, newest_what))

                    for history_item in display_list:
                        $ log_who = history_item[0]
                        $ log_what = remove_display_tags(history_item[1])

                        frame:
                            padding (6,6)
                            if log_who == mc.name:
                                background Frame(text_bubble_blue, 6, 6, 6, 6)
                            elif log_who is None:
                                background Frame(text_bubble_gray, 6, 6, 6, 6)
                            else:
                                background Frame(text_bubble_yellow, 6, 6, 6, 6)

                            hbox:
                                xsize (size_x - 90)
                                if log_who == mc.name:
                                    box_reverse True
                                    $ display_who = mc.name
                                    $ display_what = log_what
                                    $ who_align = 1.0
                                    $ what_align = 0.0
                                elif log_who is None:
                                    $ what_align = 0.5
                                    $ display_who = ""
                                    $ display_what = log_what
                                else:
                                    box_reverse False
                                    $ display_who = the_person.fname
                                    $ display_what = log_what
                                    $ who_align = 0.0
                                    $ what_align = 1.0

                                if log_who is not None:
                                    text display_who xsize 75 text_align who_align xalign who_align style "digital_text_2"
                                text display_what xsize (size_x - 160) text_align what_align xalign what_align style "digital_text_2"
