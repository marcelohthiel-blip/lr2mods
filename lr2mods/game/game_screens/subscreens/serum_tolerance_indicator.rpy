screen serum_tolerance_indicator(the_person): #Produces a hoverable textbutton that contains the current serum count vs current serum tolerance
    textbutton f"Serum Tolerance: {the_person.active_serum_count}/{the_person.serum_tolerance}\n{{menu_green}}Total serums taken: {the_person.total_serum_count}{{/menu_green}}":
        style "textbutton_style"
        text_style "textbutton_text_style"
        tooltip "Being under the effects of too many serums at once will have negative side effects, temporary lowering sluttiness and obedience, permanent lower happiness and shorter duration of active serums."
        action NullAction()
        sensitive True
        if the_person.active_serum_count > the_person.serum_tolerance:
            text_color "#FF0000"
