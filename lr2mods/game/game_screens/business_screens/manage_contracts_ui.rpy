screen manage_contracts_ui(show_available = True):
    add science_menu_background_image
    default select_contract = False

    python:
        active_contracts = f"{len(mc.business.active_contracts)}"
        max_active_contracts = f"{mc.business.max_active_contracts}"
        number_of_contracts = f"{len(mc.business.offered_contracts)}"

    modal True
    hbox:
        spacing 40
        xanchor 0.5
        align (0.5, 0.1)

        fixed:
            align (0.05, 0.05)
            xysize (780, 860)
            vbox:
                frame xfill True:
                    background "#1a45a1aa"
                    ysize 840
                    vbox:
                        spacing 20
                        text "Active Contracts ([active_contracts]/[max_active_contracts] Max)" style "menu_text_title_style"
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            vbox:
                                spacing 20
                                xsize 800
                                for contract in mc.business.active_contracts:
                                    use contract_select_button(contract):
                                        textbutton "Add Serum":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Show("serum_trade_ui", None, mc.business.inventory, contract.inventory, name_1 = "Stockpile", name_2 = contract.name, trade_requirement = contract.check_serum, hide_instead = True, inventory_2_max = contract.amount_desired)

                                        textbutton "Abandon": #TODO: This should probably require a double click or something.
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Function(mc.business.abandon_contract, contract)

                                        textbutton "Complete":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Function(mc.business.complete_contract, contract)
                                            sensitive contract.can_finish_contract

        if show_available:
            fixed:
                align (0.95, 0.05)
                xysize (780, 860)

                frame xfill True:
                    background "#1a45a1aa"
                    ysize 840
                    vbox:
                        spacing 20
                        text "Available Contracts:" style "menu_text_title_style"
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            vbox:
                                spacing 20
                                xsize 800
                                for new_contract in mc.business.offered_contracts:
                                    use contract_select_button(new_contract):
                                        textbutton "Accept Contract":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "menu_text_style"
                                            action Function(mc.business.accept_contract, new_contract)
                                            sensitive len(mc.business.active_contracts) < mc.business.max_active_contracts

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            if (show_available):
                action Return()
            else:
                action Hide("manage_contracts_ui")
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    use default_tooltip("manage_contracts_ui")
