init 10 python:
    def grid_hex_offset(idx, zoom = 1.0):
        row_idx = idx // 4
        offset_x = 132 * (idx % 4)
        offset_y = (150 * row_idx) + (0 if idx % 2 == 0 else 75)
        return (offset_x * zoom), (offset_y * zoom)

    def build_portrait_list():
        return { x.identifier: x.build_person_portrait() for x in (x for x in list_of_people if x.has_story) }

screen story_progress(story_person):
    # show_candidate(person)
    add paper_background_image
    modal True
    zorder 100

    default person = story_person
    default progress = person.progress
    default portrait_list = build_portrait_list()

    vbox:
        yalign 0.2
        xalign 0.4
        xanchor 0.5
        spacing 20
        frame:
            background "#1a45a1aa"
            xysize (1320, 130)

            hbox:
                spacing 0
                frame:
                    background None
                    xysize (120, 130)
                    offset (-100, -10)
                    imagebutton:
                        idle portrait_list[person.identifier] at zoom(.60)

                frame:
                    background None
                    vbox xfill True:
                        spacing 10
                        text "[person.name] [person.last_name]" xalign 0.5 style "menu_text_style" size 50 color person.char.who_args["color"] font person.char.what_args["font"]
                        text "[progress.story_character_description!i]" xalign 0.5 style "serum_text_style"

        viewport:
                xysize (1320, 420)
                mousewheel True
                draggable True
                scrollbars "horizontal"
                scrollbar_unscrollable "hide"
                scrollbar_ysize 12
                scrollbar_yoffset 2

                hbox:
                    spacing 20
                    frame:
                        background "#1a45a1aa"
                        xysize (400, 400)
                        vbox xfill True:
                            hbox:
                                text "Obedience Story Progress" style "serum_text_style_header" #Info about the persons raw stats, work skills, and sex skills
                                textbutton "{image=question_mark_small}" yoffset 2 style "transparent_style" tooltip "Story will only progress when obedience is high enough and mentioned condition is achieved" action NullAction()
                            viewport:
                                scrollbars "vertical"
                                draggable False
                                mousewheel True
                                vbox:
                                    spacing 10
                                    for _, obedience_text in sorted(progress.story_obedience_list.items(), key=lambda x:x[0]):
                                        text "[obedience_text!i]" style "menu_text_style"
                    frame:
                        background "#1a45a1aa"
                        xysize (400, 400)
                        vbox xfill True:
                            hbox:
                                text "Love Story Progress" style "serum_text_style_header" #Info about the persons raw stats, work skills, and sex skills
                                textbutton "{image=question_mark_small}" yoffset 2 style "transparent_style" tooltip "Story will only progress when love is high enough and mentioned condition is achieved" action NullAction()
                            viewport:
                                scrollbars "vertical"
                                draggable False
                                mousewheel True
                                vbox:
                                    spacing 10
                                    for _, love_text in sorted(progress.story_love_list.items(), key=lambda x: x[0]):
                                        text "[love_text!i]" style "menu_text_style"
                    frame:
                        #$ master_opinion_dict = dict(person.opinions, **person.sexy_opinions)
                        background "#1a45a1aa"
                        xysize (400, 400)
                        vbox xfill True:
                            hbox:
                                text "Lust Story Progress" style "serum_text_style_header" #Info about the persons loves, likes, dislikes, and hates
                                textbutton "{image=question_mark_small}" yoffset 2 style "transparent_style" tooltip "Story will only progress when sluttiness is high enough and mentioned condition is achieved" action NullAction()
                            viewport:
                                scrollbars "vertical"
                                draggable False
                                mousewheel True
                                vbox:
                                    spacing 10
                                    for _, lust_text in sorted(progress.story_lust_list.items(), key=lambda x:x[0]):
                                        text "[lust_text!i]" style "menu_text_style"

                    for stories in person.story_tracker.get_path_progress_list(person):
                        frame:
                            #$ master_opinion_dict = dict(person.opinions, **person.sexy_opinions)
                            background "#1a45a1aa"
                            xysize (400, 400)
                            vbox xfill True:
                                hbox:
                                    text stories[0] style "serum_text_style_header" #Info about the persons loves, likes, dislikes, and hates
                                    #textbutton "{image=question_mark_small}" yoffset 2 style "transparent_style" tooltip "Story will only progress when sluttiness is high enough and mentioned condition is achieved" action NullAction()
                                viewport:
                                    scrollbars "vertical"
                                    draggable False
                                    mousewheel True
                                    vbox:
                                        spacing 10
                                        for _, info in sorted(stories[1].items()):
                                            text "[info!i]" style "menu_text_style"

        hbox:
            spacing 20
            xsize 1320
            frame:
                background "#1a45a1aa"
                xysize (650, 280)
                vbox xfill True:
                    text "Other information" style "serum_text_style_header"
                    viewport:
                        scrollbars "vertical"
                        draggable False
                        mousewheel True
                        vbox:
                            spacing 10
                            for _, other_info in sorted(progress.story_other_list.items(), key=lambda x: x[0]):
                                text "[other_info!i]" style "menu_text_style"
                            if person.fetish_count == 0:
                                text "No known fetishes" style "menu_text_style"
                            if person.has_breeding_fetish:
                                text "Has breeding fetish" style "menu_text_style"
                            if person.has_anal_fetish:
                                text "Has anal fetish" style "menu_text_style"
                            if person.has_cum_fetish:
                                text "Has cum fetish" style "menu_text_style"
                            if person.has_exhibition_fetish:
                                text "Is an exhibitionist" style "menu_text_style"
                            if person.in_harem:
                                text "In Harem" style "menu_text_style"
                            elif person.is_girlfriend and not person.is_jealous:
                                text "Is polyamorous" style "menu_text_style"
                            elif person.is_girlfriend:
                                text "Is monogamous" style "menu_text_style"

            if progress.has_teamup:
                frame:
                    background "#1a45a1aa"
                    xysize (650, 280)
                    vbox xfill True:
                        text "Teamups" style "serum_text_style_header"
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                spacing 10
                                xalign 0.0
                                for teamup_info in (x for key, x in sorted(progress.story_teamup_list.items(), key=lambda x:x[0]) if isinstance(x, (list, tuple, set)) and len(x) == 2):
                                    if isinstance(teamup_info[0], Person) and teamup_info[0].has_story:
                                        if teamup_info[0] in known_people_in_the_game():
                                            hbox:
                                                spacing 10
                                                textbutton "[teamup_info[0].fname]":
                                                    xsize 120
                                                    action [
                                                        Show("story_progress", None, teamup_info[0])
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                text "[teamup_info[1]!i]" style "menu_text_style"
                                        else:
                                            text "You haven't met this person yet" style "menu_text_style"
        frame:
            background None
            align (0.5, 0.98)
            xysize (300, 150)
            imagebutton:
                align (0.5, 0.5)
                auto "gui/button/choice_%s_background.png"
                focus_mask True
                action [
                    (Hide("story_progress"))
                ]
            textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    frame:
        background None # "#1a45a1aa"
        align (0, 0)
        padding (0, 0)
        anchor (0, 0)
        pos (1450, 0)
        yfill True
        for idx, other_person in enumerate(sorted([x for x in list_of_people if x.has_story], key = lambda x: x.name)):
            use portrait_hex(idx, other_person, portrait_list)

    use default_tooltip("story_progress")

screen portrait_hex(idx, person, portrait_list):
    default is_known = person in known_people_in_the_game()

    frame:
        background None at zoom(.8)
        anchor (0, 0)
        xysize (170, 150)
        offset grid_hex_offset(idx, .8)
        imagebutton:
            if (
                is_known
                and person.progress.story_obedience_is_complete
                and person.progress.story_love_is_complete
                and person.progress.story_lust_is_complete
            ):
                auto "map/images/hexes/opaque_%s_alt.png"
            else:
                auto "map/images/hexes/opaque_%s.png"

            focus_mask "map/images/hexes/hex_focus_mask.png"
            if is_known:
                action [
                    Show("story_progress", None, person)
                ]

        if is_known:
            text person.fname style "serum_text_style" size 14 align (0.5, 1.0) offset (5, 10)
            imagebutton:
                anchor (0, 0)
                pos (0, 0)
                xoffset -110
                idle portrait_list[person.identifier] at zoom(.65)
        else:
            imagebutton:
                anchor (0, 0)
                pos (0, 0)
                offset (80, 60)
                idle "gui/extra_images/padlock.png"
