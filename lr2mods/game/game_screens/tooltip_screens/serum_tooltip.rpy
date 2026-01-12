init -1 python:
    def serum_rename_func(new_name):
        cs = renpy.current_screen()
        cs.scope["serum_design"].name = new_name

screen serum_tooltip(the_serum, given_anchor = (0.0,0.0), given_align = (0.0,0.0), allow_edit = False):
    zorder 130

    frame:
        background "#0a142688"
        anchor given_anchor
        align given_align
        vbox:
            xsize 540
            ysize 960
            xalign 0.5
            spacing 10

            if allow_edit:
                button:
                    id "serum_rename_id"
                    selected True

                    style "serum_textbutton_style_header"
                    xalign 0.5
                    xsize 520

                    action NullAction()

                    add Input(
                    size =  24,
                    color = "#dddddd",
                    default = the_serum.name,
                    changed = serum_rename_func,
                    length = 25,
                    exclude = "{}[]",
                    button = renpy.get_widget("serum_tooltip", "serum_rename_id")
                    ) xalign 0.5

                    unhovered Function(renpy.restart_interaction) #TODO: Tweak this so it is less annoying  and fix any associated errors
            else:
                frame:
                    background "#000080"
                    xsize 520
                    text "[the_serum.name]" style "menu_text_title_style" xalign 0.5

            use aspect_grid(the_serum)

            frame:
                background "#0a142688"
                xalign 0.5
                xsize 520
                ysize 150
                vbox:
                    hbox:
                        spacing 5
                        vbox:
                            spacing 5
                            frame:
                                background "#000080"
                                xsize 245
                                text "Research Required: {color=#98fb98}[the_serum.research_needed]{/color}" style "serum_text_style_traits"

                            frame:
                                background "#000080"
                                xsize 245
                                text "Production Cost: {color=#cd5c5c}[the_serum.production_cost]{/color}" style "serum_text_style_traits"

                            frame:
                                background "#000080"
                                xsize 245
                                $ calculated_profit = builtins.round((mc.business.get_serum_base_value(the_serum)-(the_serum.production_cost/mc.business.batch_size)) * the_serum.market_demand, 2)
                                if calculated_profit > 0:
                                    text "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}" style "serum_text_style_traits"
                                else:
                                    $ calculated_profit = 0 - calculated_profit
                                    text "Expected Profit:{color=#ff0000} -$[calculated_profit]{/color}" style "serum_text_style_traits"

                        vbox:
                            spacing 5

                            frame:
                                background "#000080"
                                xsize 245
                                text "Duration: [the_serum.total_duration] Turns" style "serum_text_style_traits"

                            if not the_serum.unlocked:
                                frame:
                                    background "#000080"
                                    xsize 245
                                    text "Clarity Cost: [the_serum.clarity_needed]" style "serum_text_style_traits"
                            else:
                                frame:
                                    background "#000080"
                                    xsize 245
                                    text "Market Demand: [the_serum.market_demand:.1%]" style "serum_text_style_traits"


                            if renpy.get_screen("review_designs_screen") and time_of_day < 4: #Make it so you have to be in the review screen to edit things (still need to protect already created serum somehow)
                                textbutton "Clone Design":
                                    style "textbutton_style"
                                    text_style "menu_text_title_style"
                                    xsize 245
                                    action [
                                        Call("serum_design_action_description", SerumDesign.clone_serum("Clone", the_serum.traits)),
                                        Hide("review_designs_screen")
                                    ]
            frame:
                background "#0a142688"
                xalign 0.5
                xsize 520
                if the_serum.side_effects:
                    ysize 450
                else:
                    ysize 710

                viewport:
                    scrollbars "vertical"
                    xsize 520
                    mousewheel True
                    vbox:
                        spacing 5
                        for trait in the_serum.traits:
                            use serum_tooltip_trait_info(trait)

            if the_serum.side_effects:
                frame:
                    background "#0a142688"
                    xsize 520
                    text "Side Effects" style "menu_text_title_style" xalign 0.5

                frame:
                    background "#0a142688"
                    xalign 0.5
                    xsize 520
                    viewport:
                        scrollbars "vertical"
                        xsize 520
                        mousewheel True
                        vbox:
                            spacing 5
                            for side_effect in the_serum.side_effects:
                                use serum_tooltip_trait_info(side_effect)

            transclude #If you hand the serum tooltip a child it's added to the vBox

screen serum_tooltip_trait_info(trait):
    frame:
        background "#000080"
        xsize 520
        text "[trait.name]" style "serum_text_style"

    hbox:
        spacing 5
        frame:
            background ("#43B197" if trait.positive_slug else None)
            xsize 245
            text "[trait.positive_slug]" style "serum_text_style_traits" size 16

        frame:
            background ("#B14365" if trait.negative_slug else None)
            xsize 245
            text "[trait.negative_slug]" style "serum_text_style_traits" size 16
