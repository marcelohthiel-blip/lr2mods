label check_inventory_loop():
    call screen show_serum_inventory(mc.inventory)
    return

screen player_status_hud(): #The UI that shows most of the important information to the screen.
    layer "hud"
    zorder 200

    python:
        known = len(known_people_in_the_game())
        total = len(list_of_people)
        day_info = f"{{size=16}}{StringInfo.formatted_date_string} (day {day}){{/size}}"
        arousal_info = get_arousal_with_token_string(mc.arousal, mc.max_arousal)
        energy_info = get_energy_string(mc.energy, mc.max_energy)
        clarity_info = str(builtins.int(mc.free_clarity))
        locked_clarity_info = get_locked_clarity_with_token_string(mc.locked_clarity)
        attention_info = get_attention_string(mc.business.attention, mc.business.max_attention)
        corruption = sum(x.sluttiness for x in list_of_people) / total * 1.0
        favourites = sum(1 for x in known_people_in_the_game() if x.is_favourite)
        time_of_need_perk = perk_system.get_ability_perk("Time of Need") if perk_system.has_ability_perk("Time of Need") else None
        second_wind_perk = perk_system.get_ability_perk("Second Wind") if perk_system.has_ability_perk("Second Wind") else None
        schedule_button_text = mc.schedule.get_hud_text()
        schedule_button_tooltip = mc.schedule.get_hud_tooltip()

    frame:
        background Transform(info_frame_image, alpha=persistent.hud_alpha)
        xsize 600
        ysize 400
        yalign 0.0
        vbox:
            text "[day_info]" style "menu_text_style" size 18
            textbutton "[schedule_button_text]" action Show("mc_appointment_schedule") style "textbutton_style" text_style "textbutton_text_style" text_size 20 xsize 220 tooltip schedule_button_tooltip
            textbutton "Outfit Manager" action Call("outfit_master_manager", main_selectable = False, allow_switch_wardrobe = True, from_current = True) style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Design outfits to set as uniforms or give to suggest to women."
            # textbutton "Check Inventory" action ui.callsinnewcontext("check_inventory_loop") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check what serums you are currently carrying."
            if persistent.show_goal_ui:
                textbutton "Character Sheet" action Show("mc_character_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 220 background ("#43B197" if mc.stat_goal.completed or mc.work_goal.completed or mc.sex_goal.completed else "#0a142688") hover_background "#143869" tooltip "Check your stats, skills, and goals."
            else:
                hbox:
                    spacing 5
                    textbutton "Character Sheet" action Show("mc_character_sheet") style "textbutton_style" text_style "textbutton_text_style"
                    for goal in (mc.stat_goal, mc.work_goal, mc.sex_goal):
                        textbutton f"{(1.0 if goal.completed else goal.progress_fraction):.0%}":
                            yoffset 2
                            style "textbutton_style" text_style "outfit_description_style"
                            tooltip f"{goal.name}\n{{color=#aaaaaa}}{goal.progress_string}{{/color}}\n{goal.description}"
                            action Show("mc_character_sheet")
                            hover_background "#0a142688"
                            #background ("#43B197" if goal.completed else "#0a142688")

            hbox:
                textbutton "Perks" action Show("mc_perk_sheet") style "textbutton_style" text_style "textbutton_text_style" xsize 110 tooltip "Check your stat, item, and ability perks."

                textbutton "Stats" action Show("global_stat_ui") style "textbutton_style" text_style "textbutton_text_style" xsize 110 tooltip "Show global statics"

            null height 10

            textbutton "Arousal: [arousal_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip f"Your personal arousal. When you reach your limit you will be forced to climax and your energy will drop.\nCurrently: {get_arousal_number_string(mc.arousal, mc.max_arousal)}"
                action NullAction()

            hbox:
                spacing 3
                textbutton "Energy: [energy_info]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip f"Many actions require energy to perform, sex especially. Energy comes back slowly throughout the day, and most of it is recovered after a good night's sleep.\nCurrently: {get_energy_number_string(mc.energy, mc.max_energy)}"
                    action NullAction()

                if time_of_need_perk and time_of_need_perk.is_active and mc.energy < mc.max_energy - (mc.max_energy * .3):
                    textbutton "+30%":
                        style "transparent_style"
                        text_style "menu_text_style"
                        action Function(time_of_need_perk.execute)
                        tooltip "Use your time of need perk to gain extra energy"
                        text_color "#43B197"

                if second_wind_perk and second_wind_perk.is_active and mc.energy < mc.max_energy / 2:
                    textbutton "+50%":
                        style "transparent_style"
                        text_style "menu_text_style"
                        action Function(second_wind_perk.execute)
                        tooltip "Use your second wind perk to gain extra energy"
                        text_color "#43B197"

            textbutton "Clarity: [clarity_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Post-nut clarity is generated by climaxing. The higher the lust, the higher the clarity gained. It can be used to unlock new serum traits for research or to create new serum designs."
                action NullAction()

            textbutton "Lust: [locked_clarity_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip f"Exposure to sexual encounters produces lust. Converts into clarity during orgasm. Different lust to clarity ratios may create different dialogue options.\nCurrently: {get_locked_clarity_number_string(mc.locked_clarity)}"
                action NullAction()

            textbutton "Attention: [attention_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip f"The attention your company is attracting from the local authorities.\nCurrently: {get_attention_number_string(mc.business.attention, mc.business.max_attention)}"
                action NullAction()

            textbutton "City: [favourites]/[known]/[total] - [corruption:.1f]%":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Shows the number of favourites, known and total people in the city, including the average corruption."
                action NullAction()

    use default_tooltip("player_status_hud")
    use default_tooltip("master_tooltip")
