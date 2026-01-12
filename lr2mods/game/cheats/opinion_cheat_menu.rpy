init python:
    def update_opinion_score(person, topic, category, value):
        info = person.get_opinion_topic(topic)
        if not info:
            info = [0, False]

        if value > 0 and info[0] >= 2:
            vars(person)[category][topic] = [-2, info[1]]
        elif value < 0 and info[0] <= -2:
            vars(person)[category][topic] = [2, info[1]]
        else:
            vars(person)[category][topic] = [info[0] + value, info[1]]

    def toggle_opinion_known(person, topic, category):
        info = person.get_opinion_topic(topic)
        if info:
            vars(person)[category][topic] = [info[0], not info[1]]

    def remove_opinion(person, topic, category):
        person.remove_opinion(topic)

    def get_opinion_status(person, topic): #topic is a string matching the topics given in our random list (ie. "the colour blue", "sports"). Returns a tuple containing the score: -2 for hates, -1 for dislikes, 0 for no opinion, 1 for likes, and 2 for loves, and a bool to say if the opinion is known or not.
        if topic in person.opinions:
            return "Discovered" if person.opinions[topic][1] else "Unknown"

        if topic in person.sexy_opinions:
            return "Discovered" if person.sexy_opinions[topic][1] else "Unknown"

        return "No opinion"

    def cheat_opinion_score_to_string(target, topic):
        status = get_opinion_status(target, topic)
        score = target.opinion(topic)
        if status == "No opinion":
            return "No opinion"
        if score == 0:
            return " ".join(["Neutral", "|", status]).title()

        return " ".join([opinion_score_to_string(score), "|", status]).title()

    # Define function to open the screen
    def toggle_opinion_edit_menu():
        if renpy.get_screen("opinion_edit_menu"):
            renpy.hide_screen("opinion_edit_menu")
        else:
            renpy.show_screen("opinion_edit_menu")

        renpy.restart_interaction()

    config.keymap["toggle_opinion_edit_menu"] = ["p", "P"]
    config.underlay.append(renpy.Keymap(toggle_opinion_edit_menu=toggle_opinion_edit_menu))


screen opinion_edit_menu():
    zorder 120
    default categories = {"Sexy Opinions": [Person._sexy_opinions_list, "sexy_opinions"], "Normal Opinions": [Person._opinions_list, "opinions"]}
    if "the_person" in globals():
        default target = the_person
    else:
        default target = None

    if isinstance(target, Person):
        grid builtins.len(categories) 1:
            xalign 0.37
            for n in categories:
                frame:
                    xsize 678
                    margin (0, 40, 0, 24)
                    vbox:
                        frame:
                            text "[n]" style "menu_text_title_style"

                        viewport:
                            draggable True
                            mousewheel True
                            scrollbars "vertical"
                            yfill True
                            vbox:
                                spacing 0
                                for x in sorted(categories[n][0], key=lambda s: s.lower()):
                                    hbox:
                                        textbutton "[x!c]":
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            xsize 260
                                            padding (4,2,4,0)
                                            # action Function(update_opinion_score, target, x, categories[n][1], 1)
                                            # alternate Function(update_opinion_score, target, x, categories[n][1], 0)

                                        textbutton " ? ":
                                            padding (0,2,0,0)
                                            xsize 36
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(toggle_opinion_known, target, x, categories[n][1])
                                            ]
                                        textbutton " - ":
                                            padding (0,2,0,0)
                                            xsize 36
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(update_opinion_score, target, x, categories[n][1], -1)
                                            ]
                                        textbutton cheat_opinion_score_to_string(target, x):
                                            padding (0,2,0,0)
                                            xsize 230
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            #action NullAction()
                                        textbutton " + ":
                                            padding (0,2,0,0)
                                            xsize 36
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(update_opinion_score, target, x, categories[n][1], 1)
                                            ]
                                        textbutton "{color=#D00}{b} X {/b}{/color}":
                                            padding (0,2,0,0)
                                            xsize 44
                                            style "textbutton_no_padding_highlight"
                                            text_style "serum_text_style"
                                            action [
                                                Function(remove_opinion, target, x, categories[n][1])
                                            ]
    else:
            frame:
                background "gui/button/main_choice_idle_background.png"
                anchor [0.5,0.5]
                align [0.5,0.55]
                xysize [600,120]
                textbutton "Interact with girl first" align [0.5,0.5] text_style "serum_text_style_header"
