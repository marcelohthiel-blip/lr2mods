screen review_designs_screen(show_designs = True, show_traits = True, allow_exit = True, select_instead_of_delete = False, hide_partially_researched = False):
    add science_menu_background_image
    default selected_research = None

    frame:
        xalign 0.1
        yalign 0.1
        background "#0a142688"
        hbox:
            if show_designs:
                viewport:
                    xsize 540
                    ymaximum 800
                    scrollbars "vertical"
                    mousewheel True
                    vbox:
                        text "Serum Designs:" style "menu_text_title_style" size 30
                        for serum_design in sorted(mc.business.serum_designs, key = lambda x: x.name):
                            $ serum_name = serum_design.name
                            if serum_design.researched:
                                $ serum_name += " - Research Finished"
                            else:
                                $ serum_name += f" - {serum_design.current_research:.0f}/{serum_design.research_needed:.0f} Research Required"

                            if serum_design == selected_research:
                                textbutton "[serum_name]":
                                    action SetScreenVariable("selected_research", None)
                                    sensitive serum_design.researched or not hide_partially_researched
                                    style "textbutton_style"
                                    text_style "serum_text_style"

                            else:
                                textbutton "[serum_name]":
                                    action SetScreenVariable("selected_research", serum_design)
                                    sensitive serum_design.researched or not hide_partially_researched
                                    style "textbutton_style"
                                    text_style "serum_text_style"

            if show_traits:
                viewport:
                    xsize 540
                    ymaximum 800
                    scrollbars "vertical"
                    mousewheel True
                    vbox:
                        text "Designed Traits:" style "menu_text_title_style" size 30
                        for trait_design in mc.business.blueprinted_traits:
                            $ trait_name = trait_design.name
                            if trait_design.researched:
                                $ trait_name += " - Research Finished"
                            else:
                                $ trait_name += f" - {trait_design.current_research:.0f}/{trait_design.research_needed:.0f} Research Required"

                            if trait_design == selected_research:
                                textbutton "[trait_name]":
                                    action SetScreenVariable("selected_research", None)
                                    sensitive trait_design.researched or not hide_partially_researched
                                    style "textbutton_style"
                                    text_style "serum_text_style"

                            else:
                                textbutton "[trait_name]":
                                    action SetScreenVariable("selected_research", trait_design)
                                    sensitive trait_design.researched or not hide_partially_researched
                                    style "textbutton_style"
                                    text_style "serum_text_style"


    if selected_research:
        if isinstance(selected_research, SerumDesign):
            use serum_tooltip(selected_research, given_align = (0.96,0.02), given_anchor = (1.0,0.0)):
                hbox:
                    spacing 5
                    xalign 0.5
                    xoffset -10
                    if select_instead_of_delete:
                        textbutton "Select Design":
                            action Return(selected_research)
                            style "textbutton_style" text_style "menu_text_title_style"
                    else:
                        textbutton "Rename Design":
                            xsize 245
                            action Call("rename_serum_label", selected_research, noun = "serum design", from_current=True)
                            style "textbutton_style" text_style "menu_text_title_style"
                        textbutton "Scrap Design":
                            xsize 245
                            action [Function(mc.business.remove_serum_design,selected_research), SetScreenVariable("selected_research", None)]
                            style "textbutton_style" text_style "menu_text_title_style"
        if isinstance(selected_research, SerumTrait):
            use trait_tooltip(selected_research, given_align = (0.96,0.02), given_anchor = (1.0,0.0)):
                hbox:
                    xalign 0.5
                    if select_instead_of_delete:
                        textbutton "Select Trait":
                            action Return(selected_research)
                            style "textbutton_style" text_style "menu_text_title_style"
                    else:
                        textbutton "Rename Trait":
                            action Call("rename_serum_label", selected_research, noun = "trait", from_current=True)
                            style "textbutton_style" text_style "menu_text_title_style"
                        textbutton "Scrap Trait":
                            action [Function(mc.business.remove_trait,selected_research), SetScreenVariable("selected_research", None)]
                            style "textbutton_style" text_style "menu_text_title_style"

    if allow_exit:
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

label rename_serum_label(item_to_rename, noun = "item"):
    $ name = item_to_rename.name
label .retry_rename_serum():
    $ name = renpy.input("Please give this [noun] a new name.", default = name, exclude="[]{}").strip()
    if len(name) < 3:
        jump rename_serum_label.retry_rename_serum
    if name != item_to_rename.name and any(x for x in mc.business.serum_designs if x.name == name):
        jump rename_serum_label.retry_rename_serum
    $ item_to_rename.name = name
    return
