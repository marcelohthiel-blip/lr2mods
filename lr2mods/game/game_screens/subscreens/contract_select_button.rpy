screen contract_select_button(contract, allow_create = False):
    frame:
        background "#00000088"
        xsize 800
        hbox:
            ysize 140
            vbox:
                xsize 580
                text "[contract.name]":
                    style "textbutton_text_style"
                    size 20

                use contract_aspect_grid(contract)

                text "[contract.description]" style "textbutton_text_style" size 14 text_align 0.0
                $ usable = get_design_names_that_satisfy_contract(contract)
                if allow_create and usable == "None":
                    textbutton "Research Reference Design":
                        action [
                            Hide("contract_select"),
                            Call("serum_design_action_description", the_serum = contract.reference_design)
                        ]
                        style "textbutton_style"
                        text_style "textbutton_text_style"
                        sensitive (time_of_day != 4)
                        text_size 16
                        text_align 0.0
                        tooltip "Opens the serum design UI with a trait combination that should satisfy this contract. Please note that flaws during research might make the design not qualify."

                else:
                    text f"Usable designs: {usable}" style "textbutton_text_style" size 16 text_align 0.0

            vbox:
                yfill False
                xanchor 1.00
                xalign 0.95
                xsize 195
                transclude #Place things on the right side of this entry for things like accessing the inventory.
