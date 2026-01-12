screen mc_perk_sheet():
    add paper_background_image
    modal True
    zorder 100
    vbox:
        xanchor 0.5
        xalign 0.5
        yalign 0.1
        frame:
            background "#1a45a1aa"
            hbox:
                xysize 770, 80
                text "Perks:" style "menu_text_title_style" size 40 xanchor 0.7 xalign 0.5 yalign 0.5
                text f"{mc.name} {mc.last_name}" style "menu_text_style" size 40 xanchor 0.3 xalign 0.5 yalign 0.5
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
                vbox:

                    xsize 500
                    text "Stat Perks" style "menu_text_title_style" size 32 xalign 0.5
                    for stat_perk in perk_system.stat_perks.values():
                        hbox:
                            xalign 0.5
                            textbutton stat_perk.title:
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                                hovered [
                                Show("perk_tooltip", None, stat_perk.name)
                                ]

            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:
                    xsize 500
                    text "Item Perks" style "menu_text_title_style" size 32 xalign 0.5
                    for item_perk in perk_system.item_perks.values():
                        hbox:
                            xalign 0.5
                            textbutton item_perk.title:
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                                hovered [
                                Show("perk_tooltip", None, item_perk.name)
                                ]



            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:
                    xsize 500
                    text "Ability Perks" style "menu_text_title_style" size 32 xalign 0.5
                    for ability_perk in perk_system.ability_perks.values():
                        hbox:
                            xalign 0.5
                            textbutton ability_perk.title:
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                action Function(ability_perk.execute)
                                sensitive True
                                background ("#0a142688" if not (ability_perk.togglable or ability_perk.usable) else ("#43B197" if ability_perk.is_active else "#b14343"))
                                xalign 0.5
                                yalign 0.5
                                hovered [
                                Show("perk_tooltip", None, ability_perk.name)
                                ]

    # frame:
    #     background None
    #     anchor [0.5,0.5]
    #     align [0.2,0.88]
    #     xysize [500,125]
    #     imagebutton:
    #         align [0.5,0.5]
    #         auto "gui/button/choice_%s_background.png"
    #         focus_mask "gui/button/choice_idle_background.png"
    #         action Show("mc_character_sheet")
    #     textbutton "Character Sheet" align [0.5,0.5] text_style "return_button_style"

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [Hide("mc_perk_sheet"),
                    Hide("perk_tooltip")]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    if mc.business.event_triggers_dict.get("perk_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("perk_tutorial", 1)  <= 4: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle Image(get_file_handle(f"perk_tutorial_{mc.business.event_triggers_dict.get('perk_tutorial',1)}.png"))
            hover Image(get_file_handle(f"perk_tutorial_{mc.business.event_triggers_dict.get('perk_tutorial',1)}.png"))
            action Function(mc.business.advance_tutorial,"perk_tutorial")

screen perk_tooltip(the_perk):
    default hint_height = 120
    default window_height = hint_height

    $ perk_desc = perk_system.get_perk_desc(the_perk)

    zorder 105
    frame:
        background "#1a45a1aa"
        xpos 1000
        #xalign 0.1
        yalign 0.065
        xsize 760
        ysize window_height

        vbox:
            spacing 5
            frame:
                background "#33333388"
                xsize 750
                ysize hint_height - 10
                padding (0,0)
                vbox:
                    spacing 0
                    text "{size=24}[the_perk]{/size}" style "serum_text_style_header" xalign 0 text_align 0 xpos 2
                    text "{size=18}[perk_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
