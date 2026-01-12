label check_business_inventory_loop():
    call screen show_serum_inventory(mc.business.inventory,[],["Business Inventory"])
    return

screen business_status_hud(): #Shows some information about your business.
    layer "hud"
    zorder 200

    python:
        count = number_of_hints()
        employee_count = f"{mc.business.employee_count:.0f}/{mc.business.max_employee_count:.0f}"
        funds = f"${mc.business.funds:,.0f}"
        daily_salary = f"${mc.business.calculate_base_salaries():,.0f} | ${mc.business.operating_costs:,.0f}"
        efficiency = f"{mc.business.team_effectiveness:.0f}%"
        supplies = f"{mc.business.supply_count:.0f}/{mc.business.supply_goal:.0f}"
        map_events = check_for_any_room_events()
        if mc.business.active_research_design:
            current_research = f"({mc.business.active_research_design.current_research:.0f}/{mc.business.active_research_design.research_needed:.0f})"
            if isinstance(mc.business.active_research_design, SerumTrait) and mc.business.active_research_design.researched:
                current_research += f"\n{{color=#fff}}{{size=14}}Mastery Level: {get_trait_mastery_text(mc.business.active_research_design)} | Side Effect Chance: {get_trait_side_effect_text(None, mc.business.active_research_design)}{{/size}}{{/color}}"

    frame:
        background Transform(info_frame_image, yzoom = -1.0, alpha=persistent.hud_alpha)
        xsize 600
        ysize 400
        yalign 1.0
        vbox:
            yanchor 1.0
            yalign 1.0
            yoffset -5
            spacing 5
            text "[mc.business.name]" style "menu_text_title_style" xalign 0.03
            textbutton "Employee Count: [employee_count]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Your current and maximum number of employees. Purchase new business policies from your CEO office to increase the number of employees you can have."
                action NullAction()

            textbutton "Company Funds: [funds]":
                style "transparent_style"
                text_style "menu_text_style"
                if mc.business.funds < 0:
                    text_color "#DD0000"
                tooltip "The amount of money in your business account. If you are in the negatives for more than three days your loan defaults and the game is over!"
                action NullAction()

            textbutton "Daily Salary Cost: [daily_salary]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "The amount of money spent daily to pay your employees along with daily operating costs. Neither apply during the weekend."
                action NullAction()

            textbutton "Company Efficiency: [efficiency]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "The more employees you have the faster your company will become inefficient. Perform HR work at your office or hire someone to do it for you to raise your company Efficiency. All productivity is modified by company Efficiency."
                action NullAction()

            textbutton "Raw Supplies: [supplies]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Your current and goal amounts of serum supply. Manufacturing serum requires supplies, spend time ordering supplies from your office or hire someone to do it for you. Raise your supply goal from your office if you want to keep more supply stockpiled."
                action NullAction()

            textbutton "Research:":
                style "transparent_style"
                text_style "menu_text_style"
            if not mc.business.active_research_design is None:
                textbutton "[mc.business.active_research_design.name] [current_research]":
                    xoffset 16
                    yminimum 8
                    xsize 360
                    style "transparent_style"
                    text_style "menu_text_style"
                    text_color "#43B197"
                    tooltip "The current research task of your R&D division. Visit them to set a new goal or to assemble a new serum design."
                    action NullAction()

            else:
                textbutton ("None!" if not theoretical_research.is_active else "Theoretical Research"):
                    xoffset 16
                    yminimum 8 #52
                    xsize 360
                    style "transparent_style"
                    text_style "menu_text_style"
                    text_color "#B14365"
                    tooltip "The current research task of your R&D division. Visit them to set a new goal or to assemble a new serum design."
                    action NullAction()

            hbox:
                vbox:
                    xsize 230
                    textbutton "Review Staff" action Show("employee_overview") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Review all of your current employees."
                    vbox:
                        textbutton "Check Inventory" action ui.callsinnewcontext("check_inventory_loop") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check what serums you are currently carrying."
                        hbox:
                            textbutton "Check Stock" action ui.callsinnewcontext("check_business_inventory_loop") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check the doses of serum currently waiting to be sold or sitting in your production area."
                            fixed:
                                xysize (120, 40)
                                offset (54 , 4)
                                hbox:
                                    spacing 0
                                    if map_events:
                                        imagebutton:
                                            idle "gui/extra_images/event_info.png"
                                            xysize (40, 32)
                                            background None
                                            action NullAction()
                                            tooltip "Check map for events"
                                    else:
                                        fixed:
                                            xysize (40, 32)

                                    if count > 0:
                                        imagebutton:
                                            idle "gui/extra_images/question.png"
                                            xysize (40, 32)
                                            background None
                                            action NullAction()
                                            hovered [
                                                Show("game_hints_tooltip")
                                            ]
                                            unhovered [
                                                Hide("game_hints_tooltip")
                                            ]
                                        text "[count]" style "serum_text_style_header" xysize (30, 32) yalign 0.5

    use default_tooltip("business_status_hud")
