screen serum_sell_ui():
    add science_menu_background_image

    python:
        market_reach = f"{mc.business.market_reach:,.0f}"
        funds = f"${mc.business.funds:,.0f}"
        attention_info = f"{get_attention_string(mc.business.attention, mc.business.max_attention)} ({get_attention_bleed_string(mc.business.attention_bleed, mc.business.max_attention)}/Day)"
        mental_price = f"{mc.business.get_aspect_price('Mental'):.2f}"
        physical_price = f"{mc.business.get_aspect_price('Physical'):.2f}"
        sexual_price = f"{mc.business.get_aspect_price('Sexual'):.2f}"
        medical_price = f"{mc.business.get_aspect_price('Medical'):.2f}"
        flaw_cost = f"{mc.business.get_aspect_price('Flaw'):.2f}"
        mental_percentage = f"{200 * mc.business.get_aspect_percent('Mental'):.0f}"
        physical_percentage = f"{200 * mc.business.get_aspect_percent('Physical'):.0f}"
        sexual_percentage = f"{200 * mc.business.get_aspect_percent('Sexual'):.0f}"
        medical_percentage = f"{200 * mc.business.get_aspect_percent('Medical'):.0f}"
        flaw_percentage = f"{200 * mc.business.get_aspect_percent('Flaw'):.0f}"

    modal True
    hbox:
        spacing 40
        xanchor 0.5
        align (0.5, 0.1)
        frame:
            background "#1a45a1aa"
            align (0.05, 0.05)
            xysize (780, 820)
            vbox:
                hbox:
                    xsize 700
                    text "Serum In Stock" style "menu_text_title_style" size 20 xalign 0.0
                    text "Sell Serum" style "menu_text_title_style" size 20 xalign 0.9 xanchor 1.0
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    vbox:
                        for design, dose_count in sorted(mc.business.inventory.serums_held, key = lambda x: x[0].name):
                            hbox:
                                $ serum_dose_value = mc.business.get_serum_sales_value(design)
                                use serum_design_menu_item(design, name_addition = f": {dose_count} Doses {{color=#ffff00}}{{size=12}}${serum_dose_value:,.0f}/Dose -> Demand: {design.market_demand:.1%}{{/size}}{{/color}}")
                                textbutton "1":
                                    ysize 64
                                    xsize 50
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_yanchor 0.5
                                    action Function(mc.business.sell_serum, design)
                                    style "textbutton_style" text_style "textbutton_text_style"
                                    sensitive dose_count >= 1
                                textbutton "10":
                                    ysize 64
                                    xsize 50
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_yanchor 0.5
                                    action Function(mc.business.sell_serum, design, serum_count = 10)
                                    style "textbutton_style" text_style "textbutton_text_style"
                                    sensitive dose_count >= 10
                                textbutton "All":
                                    ysize 64
                                    xsize 50
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_yanchor 0.5
                                    action Function(mc.business.sell_serum, design, serum_count = dose_count)
                                    style "textbutton_style" text_style "textbutton_text_style"
                                    sensitive dose_count > 0

        fixed:
            align (0.05, 0.05)
            xysize (780, 800)
            vbox:
                spacing 40
                frame xfill True:
                    background "#1a45a1aa"
                    ysize 210
                    #TODO: Holds current information about aspect price, attention, market reach
                    vbox:
                        grid 4 2:
                            xfill True
                            textbutton "Market Reach:":
                                xalign 0.0
                                action NullAction()
                                style "serum_text_style" text_style "serum_text_style"
                                tooltip "How many people have heard about your business. The larger your market reach the more each serum aspect point is worth."

                            text "[market_reach] people" style "serum_text_style" yalign 0.5 xalign 0.0

                            text "Current Funds:" style "serum_text_style" yalign 0.5 xalign 1.0

                            text "{color=#98fb98}[funds]{/color}" style "serum_text_style" yalign 0.5 xalign 0.0

                            textbutton "Attention:":
                                xalign 0.0
                                action NullAction()
                                style "serum_text_style" text_style "serum_text_style"
                                tooltip f"How much attention your business has drawn. If this gets too high the authorities will act, outlawing a serum design, leveling a fine, or seizing your inventory.\nCurrently: {get_attention_number_string(mc.business.attention, mc.business.max_attention)}"

                            text "[attention_info]" style "serum_text_style" yalign 0.5 xalign 0.0

                        null height 20

                        text "Aspect Data" style "menu_text_title_style"
                        frame:
                            background "#00000088"
                            xsize 760
                            grid 6 3:
                                xfill True
                                null

                                text "Mental" style "menu_text_style" color "#387aff"
                                text "Physical" style "menu_text_style" color "#00AA00"
                                text "Sexual" style "menu_text_style" color "#FFC0CB"
                                text "Medical" style "menu_text_style" color "#FFFFFF"
                                text "Flaws" style "menu_text_style" color "#AAAAAA"

                                text ("Values") style "menu_text_style"
                                text "$ [mental_price]" style "menu_text_style"
                                text "$ [physical_price]" style "menu_text_style"
                                text "$ [sexual_price]" style "menu_text_style"
                                text "$ [medical_price]" style "menu_text_style"
                                text "$ [flaw_cost]" style "menu_text_style"

                                text ("Desire") style "menu_text_style"
                                text "[mental_percentage]%" style "menu_text_style"
                                text "[physical_percentage]%" style "menu_text_style"
                                text "[sexual_percentage]%" style "menu_text_style"
                                text "[medical_percentage]%" style "menu_text_style"
                                text "-[flaw_percentage]%" style "menu_text_style"

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action Return()
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    use default_tooltip("serum_sell_ui")
