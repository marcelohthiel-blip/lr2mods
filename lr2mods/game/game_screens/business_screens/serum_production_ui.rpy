init -1 python:
    def color_indicator(variable, max_value = 100): # Gives color indication to a value range split into 5.
        if variable >= max_value / 1.25: # 80%
            return f"{{color=#24ed27}}{variable}{{/color}}"
        if variable >= max_value / 1.67: # 60%
            return f"{{color=#8edb21}}{variable}{{/color}}"
        if variable >= max_value / 2.5: # 40%
            return f"{{color=#ffec6e}}{variable}{{/color}}"
        if variable >= max_value / 5: # 20%
            return f"{{color=#ed9d4c}}{variable}{{/color}}"
        return f"{{color=#ff6347}}{variable}{{/color}}"

screen serum_production_select_ui():
    add science_menu_background_image
    modal True
    default line_selected = None
    default production_line_weight_tooltip = "Work done by production employees will be split between active lines based on production weight."
    default production_line_autosell_tooltip = "Doses of serum above the auto-sell threshold will automatically be flagged for sale, note that each marketing employee has a limited potential for auto-selling serums, so some serums might not get sold automatically if there are insufficient people in marketing to sell the serums."
    $ production_remaining = 100 - mc.business.used_line_weight
    hbox:
        xalign 0.04
        yalign 0.4
        ysize 900
        spacing 20
        frame:
            background "#0a142688"
            xsize 600
            vbox:
                spacing 5
                xalign 0.5
                frame:
                    background "#000080"
                    xfill True

                    text "Production Lines" style "menu_text_title_style" xalign 0.5

                frame:
                    background "#000080"
                    xfill True

                    textbutton f"Capacity Remaining: {color_indicator(production_remaining)}%":
                        style "serum_text_style" text_style "serum_text_style"
                        action NullAction()
                        tooltip "You can increase the number of production lines using production business policies (CEO Office)."

                frame:
                    background "#000080"
                    xfill True
                    textbutton "Max Serum Tier: [mc.business.max_serum_tier]":
                        style "serum_text_style" text_style "serum_text_style"
                        action NullAction()
                        tooltip "The highest tier of serum you can produce is limited by your production facilities.\nYou can upgrade to a higher production tier using your business policies (CEO Office)."

                viewport:
                    draggable True
                    if len(mc.business.production_lines) > 3:
                        scrollbars "vertical"
                    mousewheel True
                    xysize (600, 770)

                    vbox:
                        xfill True
                        spacing 10

                        $ line_number = 0
                        for line in mc.business.production_lines: #For the non-programmers we index our lines to 1 through production_lines.
                            $ line_number += 1
                            vbox:
                                xfill True
                                spacing 0
                                frame:
                                    background "#0a142688"

                                    vbox:
                                        xfill True
                                        spacing 0

                                        textbutton "Production Line [line_number]":
                                            action [
                                                SetScreenVariable("line_selected", line),
                                                Hide("serum_tooltip")
                                            ]
                                            style "serum_textbutton_style_header"
                                            text_style "menu_text_title_style"
                                            margin (0,0)
                                            if line.selected_design:
                                                hovered Show("serum_tooltip",None, line.selected_design, given_anchor = (1.0,0.0), given_align = (0.97,0.07))
                                                unhovered Hide("serum_tooltip")
                                            background ("#000080" if line_selected == line else "#0a142688")
                                            xfill True
                                            xalign 0.5 xanchor 0.5

                                        $ header = f"Producing: {(line.selected_design.name if line.selected_design else 'Nothing')}"
                                        if line.selected_design:
                                            $ header += f" {{menu_yellow}}[Stock: {mc.business.inventory.get_serum_count(line.selected_design)}]{{/menu_yellow}}"

                                        textbutton "[header]":
                                            action [
                                                SetScreenVariable("line_selected", line),
                                                Hide("serum_tooltip")
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            margin (0,0)
                                            if line.selected_design:
                                                hovered Show("serum_tooltip",None, line.selected_design, given_anchor = (1.0,0.0), given_align = (0.97,0.07))
                                                unhovered Hide("serum_tooltip")
                                            background ("#000080" if line_selected == line else "#0a142688")
                                            xfill True
                                            xalign 0.5 xanchor 0.5

                                    #null height 20
                                        frame:
                                            background "#000080"
                                            xfill True
                                            grid 1 2:
                                                hbox:
                                                    frame:
                                                        background None

                                                        text "Production Weight:   " style "serum_text_style"

                                                    if line.selected_design:
                                                        textbutton "-10%":
                                                            action Function(line.change_line_weight, -10)
                                                            style "textbutton_style"
                                                            text_style "serum_text_style"
                                                            sensitive line.production_weight >= 10
                                                            xsize 60
                                                            tooltip production_line_weight_tooltip

                                                        frame:
                                                            xsize 140
                                                            background None

                                                            text str(color_indicator(line.production_weight)) + "%" style "serum_text_style"

                                                        textbutton "+10%":
                                                            action Function(line.change_line_weight, 10)
                                                            style "textbutton_style"
                                                            text_style "serum_text_style"
                                                            sensitive production_remaining >= 10
                                                            xsize 60
                                                            tooltip production_line_weight_tooltip

                                                        textbutton "X":
                                                            style "textbutton_style"
                                                            text_style "serum_text_style"
                                                            xsize 40
                                                            action Function(line.clear_product)
                                                            tooltip "Cancel production on this line."

                                                    else:
                                                        frame:
                                                            background None
                                                            xsize 60
                                                            text "-10%" style "serum_text_style"
                                                            tooltip production_line_weight_tooltip

                                                        frame:
                                                            background None
                                                            xsize 140
                                                            text "0%" style "serum_text_style"

                                                        frame:
                                                            background None
                                                            xsize 60
                                                            text "+10%" style "serum_text_style"
                                                            tooltip production_line_weight_tooltip

                                                hbox:

                                                    frame:
                                                        background None
                                                        text "Auto-sell: " style "serum_text_style"

                                                    if line.autosell:
                                                        button action Function(line.toggle_line_autosell) background "#44aa44" xsize 35 ysize 35 yalign 0.5 yanchor 0.5 xalign 0.0 xanchor 0.0 tooltip production_line_autosell_tooltip
                                                    else:
                                                        button action Function(line.toggle_line_autosell) background "#444444" xsize 35 ysize 35 yalign 0.5 yanchor 0.5 xalign 0.0 xanchor 0.0 tooltip production_line_autosell_tooltip

                                                    frame:
                                                        background None
                                                        xsize 60
                                                        ysize 20

                                                    if line.selected_design:
                                                        if line.autosell:
                                                            hbox:
                                                                xsize 60
                                                                yoffset 4
                                                                textbutton "<<" action Function(line.change_line_autosell, -10) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5  text_style "serum_text_style" tooltip production_line_autosell_tooltip
                                                                textbutton "<" action Function(line.change_line_autosell, -1) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5  text_style "serum_text_style" tooltip production_line_autosell_tooltip

                                                            frame:
                                                                xsize 180
                                                                text "When > [line.autosell_amount] doses" style "menu_text_style" ysize 30 yalign 0.5 yanchor 0.5

                                                            hbox:
                                                                xsize 60
                                                                yoffset 4
                                                                textbutton ">" action Function(line.change_line_autosell, 1) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5 text_style "serum_text_style" tooltip production_line_autosell_tooltip
                                                                textbutton ">>" action Function(line.change_line_autosell, 10) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5 text_style "serum_text_style" tooltip production_line_autosell_tooltip

        if line_selected:
            frame:
                background "#0a142688"
                xsize 440
                xalign 0.5
                vbox:
                    textbutton "Choose Production":
                        style "serum_textbutton_style_header"
                        text_style "menu_text_title_style"
                        xfill True
                        action [SetScreenVariable("line_selected",None), Hide("serum_tooltip")]

                    if builtins.len(mc.business.serum_designs) == 0:
                        textbutton "No designs researched! Create and research a design in the R&D department first!":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            action NullAction()
                            xfill True
                    else:
                        viewport:
                            draggable True
                            scrollbars "vertical"
                            mousewheel True
                            xysize (440, 750)
                            vbox:
                                for a_serum in sorted(mc.business.serum_designs, key = lambda x: x.name):
                                    if a_serum.researched:
                                        $ serum_title = f"{a_serum.name} {{menu_yellow}}[Stock: {mc.business.inventory.get_serum_count(a_serum)}]{{/menu_yellow}}" if a_serum.tier <= mc.business.max_serum_tier else f"{a_serum.name}\n{{color=#ff0000}}{{size=18}}Requires Policy: Tier {a_serum.tier} Serum Production{{/size}}{{/color}}"
                                        textbutton "[serum_title]":
                                            action [
                                            Hide("serum_tooltip"),
                                            Function(line_selected.set_product, a_serum, production_remaining),
                                            SetScreenVariable("line_selected",None)
                                            ]
                                            hovered [
                                            Show("serum_tooltip", None, a_serum, given_align = (0.97, 0.5), given_anchor = (1.0, 0.0))
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            sensitive a_serum.tier <= mc.business.max_serum_tier
                                            xfill True
                                            xalign 0.5

        else:
            fixed:
                xsize 440

        fixed:
            xsize 160

        if not line_selected and len(mc.business.active_contracts) > 0:
            python:
                active_contracts = f"{len(mc.business.active_contracts)}"
                max_active_contracts = f"{mc.business.max_active_contracts}"

            frame:
                background "#0a142688"
                ysize 800
                vbox:
                    ysize 740
                    text "Active Contracts ([active_contracts]/[max_active_contracts] Max)" style "menu_text_title_style"
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        vbox:
                            spacing 20
                            xsize 600
                            for contract in mc.business.active_contracts:
                                use contract_select_button(contract)

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [Return(), Hide("serum_tooltip")]
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    imagebutton:
        auto "/tutorial_images/restart_tutorial_%s.png"
        xysize (54, 54)
        yanchor 1.0
        align (0.0, 1.0)
        action Function(mc.business.reset_tutorial,"production_tutorial")

    if mc.business.event_triggers_dict.get("production_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("production_tutorial", 1) <= 5: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xysize (1920, 1080)
            idle f"/tutorial_images/production_tutorial_{mc.business.event_triggers_dict.get('production_tutorial', 1)}.png"
            hover f"/tutorial_images/production_tutorial_{mc.business.event_triggers_dict.get('production_tutorial', 1)}.png"
            action Function(mc.business.advance_tutorial,"production_tutorial")

    use default_tooltip("serum_production_select_ui")
