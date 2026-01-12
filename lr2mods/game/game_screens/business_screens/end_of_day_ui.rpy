screen end_of_day_update():
    add paper_background_image
    zorder 100
    modal True

    hbox:
        xalign 0.5
        yoffset 20
        spacing 200
        ysize 100

        text mc.business.name style "menu_text_title_style" size 40 xalign 0.5

    frame:
        background "#1a45a1aa"
        yoffset 100
        xalign 0.05
        xanchor 0.0
        yanchor 0.0
        xsize 1410
        ysize 230

        hbox:
            spacing 100
            vbox:
                xsize 650
                text "Daily Statistics:" style "textbutton_text_style" size 26
                text f"     Company Efficiency: {mc.business.team_effectiveness:.0f}%" style "textbutton_text_style"
                text f"     Production Potential: {mc.business.production_potential:,.0f} Units" style "textbutton_text_style"
                text f"     Supplies Procured: {mc.business.supplies_purchased:,.0f} Units" style "textbutton_text_style"
                text f"     Production Used: {mc.business.production_used:,.0f} Units" style "textbutton_text_style"
                text f"     Research Produced: {mc.business.research_produced:,.0f}" style "textbutton_text_style"

            vbox:
                xsize 650
                $ profit = mc.business.funds - mc.business.funds_yesterday
                $ mc.business.listener_system.fire_event("daily_profit", profit = profit)
                text f"{('Profit' if profit > 0 else 'Loss')}: $ {abs(profit):,.0f}" style "textbutton_text_style" size 26 color ("#00A000" if profit > 0 else "#A00000")
                text f"     Total Funds: $ {mc.business.funds:,.0f}" style "textbutton_text_style"
                text f"     Sales Made: $ {mc.business.sales_made:,.0f}" style "textbutton_text_style"
                if day % 7 not in (6, 0):   # can't use workday -> day is already +1 when we show this dialogue
                    text f"     Daily Salary Paid: $ {mc.business.paid_salaries:,.0f}" style "textbutton_text_style"
                    text f"     Daily Operating Costs: $ {mc.business.operating_costs:,.0f}" style "textbutton_text_style"
                #text "     Serums Sold Today: " + str(mc.business.serums_sold) + " Vials" style "textbutton_text_style"
                text f"     Serums Ready for Sale: {mc.business.inventory.total_serum_count:,.0f} Vials" style "textbutton_text_style"

    frame:
        background "#1a45a1aa"
        xalign 0.05
        yoffset 350
        xanchor 0.0
        yanchor 0.0

        viewport:
            mousewheel True
            scrollbars "vertical"
            xsize 1400
            ysize 500
            vbox:
                text "Highlights:" style "textbutton_text_style" size 26
                for item in mc.business.message_list:
                    text f"     {item}" style "textbutton_text_style" size 20

                for item in mc.business.counted_message_list:
                    text f"     {item} x {builtins.int(mc.business.counted_message_list[item])}" style "textbutton_text_style" size 20


    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action [Return()]
        textbutton "End Day" align (0.5, 0.5) text_style "return_button_style"

    frame:
        background "#1a45a1aa"
        yoffset 100
        xalign 0.92
        xsize 230
        ysize 800
        use show_single_day_schedule(day % 7)
