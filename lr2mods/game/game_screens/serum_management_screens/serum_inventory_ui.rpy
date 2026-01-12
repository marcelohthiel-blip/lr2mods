screen show_serum_inventory(the_inventory, extra_inventories = [],inventory_names = []): #You can now pass extra inventories, as well as names for all of the inventories you are passing. Returns nothing, but is used to view inventories.
    add science_menu_background_image
    hbox:
        $ count = 0
        xalign 0.05
        yalign 0.05
        spacing 40
        for an_inventory in [the_inventory] + extra_inventories:
            frame:
                background "#0a142688"
                xsize 500
                viewport:
                    mousewheel True
                    scrollbars "vertical"

                    vbox:
                        xalign 0.02
                        yalign 0.02
                        frame:
                            background "#000080"
                            xfill True
                            if builtins.len(inventory_names) > 0 and count < builtins.len(inventory_names):
                                $ inv_name = inventory_names[count]
                                text "[inv_name]" style "menu_text_title_style" xalign 0.5
                            else:
                                text "Serums in Inventory" style "menu_text_title_style" xalign 0.5

                        for design, dose_count in sorted(an_inventory.serums_held, key = lambda x: x[0].name):
                            textbutton "[design.name]: [dose_count] Doses":
                                xfill True
                                style "textbutton_style"
                                text_style "serum_text_style"
                                action Show("serum_tooltip",None,design, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                sensitive True
                                hovered Show("serum_tooltip",None,design, given_align = (0.97,0.07), given_anchor = (1.0,0.0))

                    $ count += 1

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
