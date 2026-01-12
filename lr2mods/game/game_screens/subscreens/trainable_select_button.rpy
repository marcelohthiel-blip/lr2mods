init 2 python:
    def get_training_slug(trainable, person): #If an unlock function returns a string that is shown here as the reason.
        clarity_string = f"{trainable.get_cost(person)} Clarity"
        if mc.free_clarity < trainable.get_cost(person):
            clarity_string = f"{{color=#ff0000}}{clarity_string}{{/color}}"

        return_string = f"{trainable.display_name} - {clarity_string}"
        if trainable.unlocked_function is not None:
            unlock_return = trainable.unlocked_function(person, *trainable.extra_args)
            if isinstance(unlock_return, str):
                return_string += f"\n{{menu_red=14}}Requires: {unlock_return}{{/menu_red}}"

        return return_string

screen trainable_select_button(the_trainable, the_person):
    textbutton get_training_slug(the_trainable, the_person):
        style "textbutton_style"
        xfill True
        text_style "textbutton_text_style"
        text_text_align 0.0
        text_size 16
        sensitive the_trainable.is_valid_trainnee(the_person)
        action Return(the_trainable)
