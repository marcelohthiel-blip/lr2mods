#Used to display stats for multi people while you're talking to them, takes an array of Actor objects.
init 2 python:
    def multi_person_info_ui_get_formatted_tooltip(person):
        (role_list, fetish_list) = person_info_ui_get_special_role_information(person)

        tooltip = [
            f"Happiness: {person.happiness}\n",
            f"Suggestibility: {min(100, person.suggestibility)}%\n",
            f"Age: {person.age}\n",
            f"Height: {height_to_string(person.height)}\n",
            f"Cup size: {person.tits}\n",
            f"Weight: {get_person_weight_string(person)}\n",
            f"Novelty: {person.novelty:.0f}%\n",
        ]
        tooltip.insert(0, f"Job: {person_info_ui_get_job_title(person)}\n")
        if fetish_list:
            tooltip.append(f"Fetishes: {', '.join(fetish_list)}\n")
        if role_list:
            tooltip.append(f"{', '.join(role_list)}\n")
        return "".join(tooltip)

screen multi_person_info_ui(actors):
    tag master_tooltip
    layer "solo"
    zorder 200

    frame:
        background Transform("gui/topbox.png", alpha=persistent.hud_alpha)
        xsize 1100
        ysize 200
        yalign 0.0
        xalign 0.5
        xanchor 0.5

        hbox:
            xanchor 0.5
            xalign 0.5
            spacing 10
            xsize 1000
            xoffset 50

            for actor in sorted(actors, key=lambda a: a.sort_order):
                use actor_info_block(actor)

screen actor_info_block(actor):
    python:
        love_label = person_info_ui_get_label_tag(actor.person, "Love", "Love")
        obedience_label = person_info_ui_get_label_tag(actor.person, "Obedience", "Obedience")
        slut_label = person_info_ui_get_label_tag(actor.person, "Sluttiness", "Slut")
        energy_label = person_info_ui_get_label_tag(actor.person, "Energy", "Energy")
        love_info = get_love_hearts(actor.person.love, 5)
        sluttiness_info = get_heart_image_list(actor.person.sluttiness, actor.person.effective_sluttiness())
        obedience_info = f"{actor.person.obedience} {{image=triskelion_token_small}} {get_obedience_string(actor.person.obedience)}"

    vbox:
        hbox:
            textbutton "{image=question_mark_small}":
                yoffset 4
                style "transparent_style"
                tooltip multi_person_info_ui_get_formatted_tooltip(actor.person)
                action NullAction()

            text format_titles_short(actor.person) style "menu_text_style" size 30 ysize 30
            use favourite_toggle_button(actor.person)

            if actor.person.serum_tolerance == 0:
                textbutton "{image=serum_vial3}":
                    xoffset 4
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip "Warning: this person has no tolerance for serums\n" + person_info_ui_get_serum_info_tooltip(actor.person)
                    action NullAction()
            elif actor.person.serum_effects:
                textbutton (f"{{image=serum_vial3}} +{min(100, actor.person.suggestibility)}%" if actor.person.active_serum_count > actor.person.serum_tolerance
                        else f"{{image=serum_vial2}} +{min(100, actor.person.suggestibility)}%" if actor.person.active_serum_count == actor.person.serum_tolerance
                        else f"{{image=serum_vial}} +{min(100, actor.person.suggestibility)}%"):
                    xoffset 4
                    style "transparent_style"
                    text_style "menu_text_style"
                    tooltip person_info_ui_get_serum_info_tooltip(actor.person)
                    action NullAction()

        textbutton f"Arousal: {get_arousal_with_token_string(actor.person.arousal, actor.person.max_arousal)}":
            style "transparent_style"
            text_style "menu_text_style"
            tooltip f"When a girl is brought to 100% arousal she will start to climax. Climaxing will increase sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider.\nCurrently: {get_arousal_number_string(actor.person.arousal, actor.person.max_arousal)}"
            action NullAction()

        textbutton f"[energy_label]: {get_energy_string(actor.person.energy, actor.person.max_energy)}":
            style "transparent_style"
            text_style "menu_text_style"
            tooltip f"Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back overnight.\nCurrently {get_energy_number_string(actor.person.energy, actor.person.max_energy)}"
            action NullAction()

        textbutton "[love_label]: [love_info]":
            style "transparent_style"
            text_style "menu_text_style"
            tooltip f"Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation.\nWhen a girl is not part of your harem, she will slowly lose love until it reaches 80, having sex once every five days will stop the love bleed.\nLove: {get_attention_number_string(actor.person.love, 100)}"
            action NullAction()

        hbox:
            textbutton f"[obedience_label]: [obedience_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                action NullAction()

            if bool(actor.person.situational_obedience):
                textbutton "{image=question_mark_small}":
                    style "transparent_style"
                    tooltip person_info_ui_get_formatted_obedience_tooltip(actor.person)
                    action NullAction()

        hbox:
            textbutton f"[slut_label]: [sluttiness_info]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Her arousal adds a temporary sluttiness ({image=red_heart_token_small}). Her base sluttiness ({image=gold_heart_token_small}) is permanent, but can be increased by situational modifiers."
                action NullAction()

            if bool(actor.person.situational_sluttiness):
                textbutton "{image=question_mark_small}":
                    style "transparent_style"
                    tooltip person_info_ui_get_formatted_tooltip(actor.person)
                    action NullAction()
