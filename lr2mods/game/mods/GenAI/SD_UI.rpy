define config.log = "customlog.txt"
init 5 python:
    import webbrowser
    import os
    import json
    from inspect import getsourcefile
    from os.path import dirname
    import tarfile
    from pathlib import Path

    # Initialize store.last_active_person
    if not hasattr(store, "last_active_person"):
        store.last_active_person = None

    # Existing store variable checks
    if not hasattr(store, 'sd_saved_person_data'):
        store.sd_saved_person_data = ""
    if not hasattr(store, 'sd_prompt_style'):
        store.sd_prompt_style = ""

    # Initialize settings manager (replaces all persistent initialization)
    init_sd_settings()

    # Initialize non-persistent variables
    available_models = []
    available_samplers = []
    available_upscalers = []
    available_adetailers = []
    available_prompt_sets = []
    available_schedulers = []
    available_loras = []
    current_person_data = None
    have_connection = True
    is_fullscreen = False

    def get_available_models():
        global have_connection
        if not have_connection:
            return []
        global available_models
        global sdClient
        available_models = sdClient.get_available_models()
        if len(available_models) == 0:
            sdClient.show_connection_error()
            return []
        global available_loras
        available_loras = sdClient.get_available_loras()
        have_connection = True
        sd_set_setting("sd_selected_model", sdClient.get_current_model())
        return available_models

    def get_available_samplers():
        global have_connection
        if not have_connection:
            return []
        global available_samplers
        if len(available_samplers) == 0:
            global sdClient
            available_samplers = sdClient.get_available_samplers()
            if len(available_samplers) == 0:
                sdClient.show_connection_error()
                return []
            if sd_get_setting("sd_selected_sampler") is None:
                sd_set_setting("sd_selected_sampler", available_samplers[0])
        return available_samplers

    def get_available_upscalers():
        global have_connection
        if not have_connection:
            return []
        global available_upscalers
        if len(available_upscalers) == 0:
            global sdClient
            available_upscalers = sdClient.get_available_upscalers()
            if len(available_upscalers) == 0:
                sdClient.show_connection_error()
                return []
            if sd_get_setting("sd_selected_upscaler") is None:
                sd_set_setting("sd_selected_upscaler", available_upscalers[0])
        return available_upscalers

    def get_available_adetailers():
        global have_connection
        if not have_connection:
            return []
        global available_adetailers
        if len(available_adetailers) == 0:
            global sdClient
            available_adetailers = sdClient.get_available_adetailers()
            if len(available_adetailers) == 0:
                sdClient.show_connection_error()
                return []
            if sd_get_setting("sd_selected_adetailer") is None:
                sd_set_setting("sd_selected_adetailer", available_adetailers[0])
        return available_adetailers

    def get_available_schedulers():
        global have_connection
        if not have_connection:
            return []
        global available_schedulers
        if len(available_schedulers) == 0:
            global sdClient
            available_schedulers = sdClient.get_available_schedulers()
            if len(available_schedulers) == 0:
                sdClient.show_connection_error()
                return []
            if sd_get_setting("sd_selected_scheduler") is None:
                sd_set_setting("sd_selected_scheduler", available_schedulers[0])
        return available_schedulers

    def merge_json_list(target: list, src:list, name):
        for i in range(len(src)):
            if str(type(src[i])) == "<class 'dict'>":
                t = dict()
                merge_json_dict(t, src[i], name)
                target.append(t)
            elif str(type(src[i])) == "<class 'list'>":
                target.append(list())
                merge_json_list(target[i], src[i], name)
            else:
                target.append(copy.copy(src[i]))

    def merge_json_dict(target: dict, src:dict, name):
        for k in src:
            if (k in target) and (type(src[k]) != type(target[k])):
                print("JSON type mismatch for "+name)
                continue
            if str(type(src[k])) == "<class 'dict'>":
                if not k in target:
                    target[k] = dict()
                merge_json_dict(target[k], src[k], name)
            elif str(type(src[k])) == "<class 'list'>":
                if k in target:
                    continue
                target[k] = list()
                merge_json_list(target[k], src[k], name)
            else:
                if not (k in target):
                    target[k] = copy.copy(src[k])


    def read_available_prompt_sets():
        global available_prompt_sets
        available_prompt_sets = sd_get_available_prompt_sets()
        
        # Set default prompt if none is selected
        if sd_get_setting("sd_selected_prompt") == None:
            sd_set_setting("sd_selected_prompt", "default")

    def retry_connection():
        global have_connection
        have_connection = True

    def set_selected_model(model_name):
        global sdClient, have_connection
        if not have_connection:
            return
        sd_set_setting("sd_selected_model", model_name)
        sdClient.set_model(model_name)

    def on_steps_value_changed(value):
        try:
            sd_set_setting("sd_steps_value", max(1, min(100, int(value))))
        except ValueError:
            sd_set_setting("sd_steps_value", 20)  # Default to 20 if invalid input

    def on_cfg_scale_value_changed(value):
        try:
            sd_set_setting("sd_cfg_scale_value", max(1.0, min(10.0, float(value))))
        except ValueError:
            sd_set_setting("sd_cfg_scale_value", 7.0)  # Default to 7.0 if invalid input

    def on_upscaling_size_changed(value):
        try:
            sd_set_setting("sd_upscaling_size", max(1.0, min(4.0, float(value))))
        except ValueError:
            sd_set_setting("sd_upscaling_size", 1.75)  # Default to 1.75 if invalid input

    def on_width_value_changed(value):
        try:
            sd_set_setting("sd_width_value", max(64, min(2048, int(value))))
        except ValueError:
            sd_set_setting("sd_width_value", 512)  # Default to 512 if invalid input

    def on_height_value_changed(value):
        try:
            sd_set_setting("sd_height_value", max(64, min(2048, int(value))))
        except ValueError:
            sd_set_setting("sd_height_value", 768)  # Default to 768 if invalid input

    def on_seed_value_changed(value, person_data=None):
        if person_data is None:
            person_data = get_current_person_data()
        if person_data is None:
            return
        person_data.seed = int(value)
        sdClient.save_persons_image_data_json()

    def generate_new_seed(person_data=None):
        if person_data is None:
            person_data = get_current_person_data()
        if person_data is None:
            return
        person_data.seed = sdClient.generate_new_random_seed()
        sdClient.save_persons_image_data_json()

    def get_current_person_data():
        global sdClient
        if not 'sdClient' in globals() or sdClient is None or sdClient.currentPerson is None:
            return None
        return sdClient.get_person_image_data(makeNew=True)

    def get_positive_prompt():
        global sdClient
        return sdClient.get_positive_prompt()

    def get_positive_custom_prompt():
        global sdClient
        return sdClient.get_person_image_data(makeNew=True).positiveCustomPrompt

    def get_is_positive_prompt_override_enabled():
        global sdClient
        return sdClient.get_person_image_data(makeNew=True).positivePromptOverride

    def get_positive_prompt_override_text():
        global sdClient
        return "On" if get_is_positive_prompt_override_enabled() else "Off"

    def toggle_positive_prompt_override():
        global sdClient
        sdClient.toggle_positive_prompt_override()

    def on_positive_prompt_value_changed(value):
        global sdClient
        sdClient.set_positive_custom_prompt(value)

    def is_positive_prompt_different_to_current_image():
        global sdClient
        current_person_data = get_current_person_data()
        if current_person_data == None:
            return False
        current_state_image = sdClient.get_current_state_image(current_person_data)
        if current_state_image == None:
            return False
        current_prompt = sdClient.get_positive_prompt()
        stored_prompt = current_state_image.prompt
        result = stored_prompt !=current_prompt

        # print(f"Current Prompt: {current_prompt}")
        # print(f"Stored Prompt: {stored_prompt}")
        # print(f"Prompt Changed: {result}")
        return result

    def get_positive_appended_prompt():
        global sdClient
        current_person_data = get_current_person_data()
        if current_person_data == None:
            return False
        return current_person_data.positiveAppendedPrompt

    def on_positive_appended_prompt_value_changed(value):
        global sdClient
        sdClient.set_positive_appended_prompt(value)

    def get_negative_appended_prompt():
        global sdClient
        current_person_data = get_current_person_data()
        if current_person_data == None:
            return False
        return current_person_data.negativeAppendedPrompt

    def on_negative_appended_prompt_value_changed(value):
        global sdClient
        sdClient.set_negative_appended_prompt(value)

    def get_negative_prompt():
        global sdClient
        return sdClient.get_negative_prompt()

    def get_negative_custom_prompt():
        global sdClient
        return sdClient.get_person_image_data(makeNew=True).negativeCustomPrompt

    def get_is_negative_prompt_override_enabled():
        global sdClient
        return sdClient.get_person_image_data(makeNew=True).negativePromptOverride

    def get_negative_prompt_override_text():
        global sdClient
        return "On" if get_is_negative_prompt_override_enabled() else "Off"

    def toggle_negative_prompt_override():
        global sdClient
        sdClient.toggle_negative_prompt_override()

    def on_negative_prompt_value_changed(value):
        global sdClient
        sdClient.set_negative_custom_prompt(value)

    def on_global_positive_prepend_value_changed(value):
        sd_set_setting("sd_global_positive_prepend", value)

    def on_global_negative_prepend_value_changed(value):
        sd_set_setting("sd_global_negative_prepend", value)

    def toggle_auto_generate():
        global sdClient
        sdClient.toggle_auto_generate()

    def get_auto_generate_toggle_text():
        global sdClient
        return "On" if sdClient.autoGenerate else "Off"

    def toggle_SDConfig_menu():
        if renpy.get_screen("SDConfig_menu"):
            renpy.hide_screen("SDConfig_menu")
        else:
            renpy.show_screen("SDConfig_menu")

        renpy.restart_interaction()

    config.keymap["toggle_SDConfig_menu"] = ["u", "U"]
    config.underlay.append(renpy.Keymap(toggle_SDConfig_menu=toggle_SDConfig_menu))

    def toggle_genAI_fullscreen():
        global sdClient, is_fullscreen
        is_fullscreen = not is_fullscreen
        if is_fullscreen:
            renpy.hide_screen("genAI_image")
            renpy.show_screen("genAI_image_fullscreen", sdClient.currentImagePath)
        else:
            renpy.hide_screen("genAI_image_fullscreen")
            renpy.show_screen("genAI_image", sdClient.currentImagePath)

    def open_local_html(filepath):
        # Convert the filepath to an absolute file URL
        abs_path = os.path.abspath(filepath)
        url = 'file:///' + abs_path.replace('\\', '/')
        webbrowser.open(url)

    def SD_LeftImage():
        global sdClient
        sdClient.switch_to_previous_image()

    def SD_RightImage():
        global sdClient
        sdClient.switch_to_next_image()

    def SD_NewImage():
        if sd_get_setting("sd_selected_prompt") == None:
            read_available_prompt_sets()
        global sdClient, have_connection
        if sdClient.sd_generation_in_progress:
            return # Don't start if already running
        have_connection = True
        renpy.invoke_in_thread(sdClient.add_new_image)
        #sdClient.add_new_image()

    def SD_RefreshImage():
        if sd_get_setting("sd_selected_prompt") == None:
            read_available_prompt_sets()
        global sdClient, have_connection
        if sdClient.sd_generation_in_progress:
            return # Don't start if already running
        have_connection = True
        renpy.invoke_in_thread(sdClient.replace_current_image)
        #sdClient.replace_current_image()

    def Check_SD_Completion():
        global sdClient
        # Show generating indicator if generation is running
        if sdClient.sd_generation_in_progress:
            renpy.show_screen("generating_indicator")
        # Hide generating indicator if generation is complete
        elif sdClient.sd_was_generating and not sdClient.sd_generation_in_progress:
            renpy.hide_screen("generating_indicator")
            sdClient.sd_was_generating = False # Reset the flag
            sdClient.show_current_image(updateIndex=False)
            
            if not sdClient.autoGenerate:
                # Force the SD_update_button screen to refresh
                if renpy.get_screen("SD_update_button"):
                    renpy.hide_screen("SD_update_button")
                renpy.show_screen("SD_update_button")

            renpy.restart_interaction() #Force redraw
            debug_image_status()
            #print("SD Generation completion detected.")

    def get_progress_text():
        global sdClient
        return str(sdClient.get_progress_text())

    def SD_DeleteImage():
        global sdClient
        sdClient.delete_current_image()

    def get_upscaling_toggle_text():
        return "On" if sd_get_setting("sd_upscaling_enabled", False) else "Off"

    def get_adetailer_toggle_text():
        return "On" if sd_get_setting("sd_adetailer_enabled", False) else "Off"

    def calculate_display_height():
        # Calculate height while maintaining aspect ratio with width of 512
        aspect_ratio = float(sd_get_setting("sd_height_value", 768)) / float(sd_get_setting("sd_width_value", 512))
        return int(512 * aspect_ratio)

    def calculate_fullscreen_dimensions():
        # Get the screen dimensions (assuming 1920x1080 as max bounds)
        max_width = 1920
        max_height = 1080

        # Calculate the aspect ratio of the image
        aspect_ratio = float(sd_get_setting("sd_height_value", 768)) / float(sd_get_setting("sd_width_value", 512))

        # Start with maximum possible width
        width = max_width
        height = int(width * aspect_ratio)

        # If height exceeds screen height, scale down based on height instead
        if height > max_height:
            height = max_height
            width = int(height / aspect_ratio)

        # Add some padding (10% margin)
        width = int(width * 0.9)
        height = int(height * 0.9)

        return (width, height)

    def toggle_upscaling():
        current = sd_get_setting("sd_upscaling_enabled", False)
        sd_set_setting("sd_upscaling_enabled", not current)

    def on_adetailer_model_changed(value):
        sd_set_setting("sd_adetailer_model", value)

    def toggle_adetailer():
        current = sd_get_setting("sd_adetailer_enabled", False)
        sd_set_setting("sd_adetailer_enabled", not current)

    def open_SDConfig_menu_with_models():
        # First get the available models
        get_available_models()
        read_available_prompt_sets()
        # Then toggle the screen
        if renpy.get_screen("SDConfig_menu"):
            renpy.hide_screen("SDConfig_menu")
        else:
            renpy.show_screen("SDConfig_menu")

    def set_data_from_json(promptData):
        if promptData is None:
            return

        global sdPromptCache
        sdPromptCache.clear()

        # Store just the prompt name instead of the full data
        promptProfileName = promptData["Name"]
        sd_set_setting("sd_selected_prompt", promptProfileName)

        # switch model to the one in the json
        model_name = promptData["Model"]
        if model_name != None and model_name != "" and is_model_installed(model_name):
            full_model_name = get_full_model_name(model_name)
            if full_model_name != sd_get_setting("sd_selected_model"):
                set_selected_model(full_model_name)

        json = promptData["settings"]
        sd_set_setting("sd_selected_sampler", json["sampler"])
        sd_set_setting("sd_selected_scheduler", json.get("scheduler", "automatic"))
        sd_set_setting("sd_steps_value", int(json["steps"]))
        sd_set_setting("sd_cfg_scale_value", float(json["cgi"]))
        resolution = json["resolution"].split('x')
        sd_set_setting("sd_width_value", resolution[0])
        sd_set_setting("sd_height_value", resolution[1])
        if json.get("adetailer", "") == "":
            sd_set_setting("sd_adetailer_enabled", False)
        else:
            sd_set_setting("sd_adetailer_enabled", True)
            sd_set_setting("sd_selected_adetailer", json["adetailer"])

        sd_set_setting("sd_global_positive_prepend", promptData.get("positive_prompt_prefix", ""))
        sd_set_setting("sd_global_negative_prepend", promptData.get("negative_prompt_prefix", ""))
        #img2img support
        if promptData.get("img2img", "") == "":
            sd_set_setting("sd_img2img_enabled", False)
        else:
            sd_set_setting("sd_img2img_enabled", bool(promptData["img2img"]))
        if promptData.get("denoising_strength", "") == "":
            sd_set_setting("sd_denoising_strength", 0.5)
        else:
            sd_set_setting("sd_denoising_strength", float(promptData["denoising_strength"]))
        #latent support
        if promptData.get("latent_modifier", "") == "":
            sd_set_setting("sd_latent_enabled", False)
        else:
            sd_set_setting("sd_latent_enabled", bool(promptData["latent_modifier"]))
            if promptData.get("extra_noise_multiplier", "") == "":
                sd_set_setting("sd_noise_strength", 0)
            else:
                sd_set_setting("sd_noise_strength", float(promptData["extra_noise_multiplier"]))
            if promptData.get("extra_noise_type", "") == "":
                sd_set_setting("sd_noise_type", 'add')
            else:
                sd_set_setting("sd_noise_type", promptData["extra_noise_type"])

    def check_installed():
        global sdClient
        global available_models
        global available_loras
        available_models = sdClient.get_available_models()
        available_loras = sdClient.get_available_loras()

    def is_model_installed(model_name):
        global available_models
        for model in available_models:
            if model_name in model:
                return True
        return False

    def get_full_model_name(model_name):
        global available_models
        for model in available_models:
            if model_name in model:
                return model
        return model_name

    def is_lora_installed(lora_name):
        global available_loras
        for lora in available_loras:
            if lora == lora_name:
                return True
        return False

    def default_serializer(o):
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError(f"Type " + str(type(o)) +" non sérialisable")

    def create_debug_tar():
        ARCHIVE_NAME = "debug_genAI.tgz"
        FILE_TO_ADD  = Path("debug_persistent.json")
        LOGS_TO_ADD = Path("customlog.txt")
        DIR_TO_ADD   = Path(dirname(getsourcefile(lambda:0))+'/prompts')
        d = {}
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                d[str(attr)] = getattr(persistent, attr)
        with open("debug_persistent.json", "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, default=default_serializer)
        with tarfile.open("debug_genAI.tgz", mode="w:gz") as tgz:
            tgz.add(FILE_TO_ADD, arcname=FILE_TO_ADD.name)
            tgz.add(LOGS_TO_ADD, arcname=LOGS_TO_ADD.name)
            tgz.add(DIR_TO_ADD, arcname=DIR_TO_ADD.name, recursive=True)

    def debug_image_status():
        print(f"CurrentImagePath: {sdClient.currentImagePath}")
        print(f"Image exists: {os.path.exists(sdClient.currentImagePath)}")
        print(f"Prompt match: {not is_positive_prompt_different_to_current_image()}")

    def get_promptprofile_name(promptProfileData):
        textstring = promptProfileData['Name']
        if promptProfileData.get('Model', "") != "":
            textstring += "\nModel: " + promptProfileData['Model']
        if promptProfileData.get('Description', "") != "":
            textstring += "\n" + promptProfileData['Description']
        return textstring

# OVERRIDE to squeeze the main LR2R menus over a bit (main_choice_display.rpy/game/subscreens
#Main Menus, adjust as needed
screen main_choice_display(menu_items):
    tag master_tooltip
    layer "hud"
    zorder 100

    hbox:
        spacing 5
        align (0.458, 0.2) # align (0.518, 0.2)
        anchor (0.5, 0.0) # anchor (0.5, 0.0), flush to left menu (0.5, 0.0)
        for count in builtins.range(len(menu_items)):
            if builtins.len(menu_items[count]) > 1:
                frame:
                    background Frame ("gui/LR2_Main_Choice_Box.png")
                    xysize (350, 700) #(380, 700)  therefore 350/380 will be 0.9210 reduce accordingly
                    $ title_element = menu_items[count][0]
                    if isinstance(title_element, basestring):
                        text "[title_element]" xalign 0.5 ypos 45 anchor (0.5,0.5) size 18 style "menu_text_title_style" xsize 240
                    else:
                        add title_element xalign 0.5 ypos 45 anchor (0.5,0.5)

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        xalign 0.5
                        xanchor 0.5
                        yanchor 0.0

                        ypos 99
                        xsize 345 #360
                        ysize 588 #588
                        vbox:
                            for item in (x for x in menu_items[count][1:] if x.display):
                                textbutton "[item.title!i]":
                                    xysize (345, 80)
                                    align (0.5, 0.5)
                                    #if item.highlight_green:
                                    #    style "textbutton_style_highlight_green"
                                    #elif item.highlight_yellow:
                                    #    style "textbutton_style_highlight_yellow"
                                    #else:
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    text_align (0.5,0.5)
                                    if not (renpy.mobile or renpy.android) and item.display_key:
                                        hovered [Function(item.show_person)]
                                        unhovered [Function(item.hide_person)]
                                    action [
                                        Function(item.hide_person),
                                        Return(item.return_value)
                                    ]
                                    tooltip item.the_tooltip
                                    sensitive item.is_sensitive

# Override the quick_menu screen to add our GenAI Config button
screen quick_menu():
    # Ensure this appears on top of other screens.
    zorder 200

    # Add an in-game quick menu.
    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu('save')
        if config.has_quicksave:
            textbutton _("Q.Save") action QuickSave()
        if config.has_quicksave:
            textbutton _("Q.Load") action QuickLoad()
        textbutton _("Prefs") action ShowMenu('preferences')
        textbutton _("GenAI Config") action Function(open_SDConfig_menu_with_models)
        if persistent.cheats_visible:
            textbutton _("Cheat") action ToggleScreen("cheat_menu")
            textbutton _("Research") action ToggleScreen("serum_cheat_menu")
            if "the_person" in globals() and isinstance(the_person, Person):
                textbutton _("Opinions") action ToggleScreen("opinion_edit_menu")

screen SD_update_button():
    zorder 11
    layer "solo"
    if sdClient and sdClient.currentPerson is not None:

        frame:
            xalign 0.95 # 0.925
            yalign 0.085 # 0.1
            #background "#1a45a1aa"
            # Green: if character has changed (i.e., is_positive_prompt_different_to_current_image() is True) = background "#45a11aaa"
            # Red: if there's no picture (current image path is invalid or doesn't exist)  background "#a11a45aa"
            # Blue: if neither of the above (no change and picture exists) frame  background "#1a45a1aa"
            background Solid(
                "#45a11aaa" if is_positive_prompt_different_to_current_image() else 
                "#a11a45aa" if (not sdClient or sdClient.currentImagePath is None or (sdClient.get_current_state_image(sdClient.get_person_image_data(makeNew=True)) is None)) else "#1a45a1aa"
            )
            padding (20, 5) # Padding inside the frame 20,20

            vbox:
                spacing 5 # 10
                
                hbox:
                    xalign 0.5
                    text [ "New Pose!" if is_positive_prompt_different_to_current_image() else "Pose does not exist!" if (not sdClient or sdClient.currentImagePath is None or (sdClient.get_current_state_image(sdClient.get_person_image_data(makeNew=True)) is None or not os.path.exists(sdClient.get_current_state_image(sdClient.get_person_image_data(makeNew=True)).filePath))) else "Current Pose" ] size 20
                    
                hbox:
                    spacing 20 # Spacing between buttons

                    button:
                        style "textbutton_style"
                        action Function(SD_LeftImage)
                        tooltip "Previous image"
                        text "<"
                    button:
                        style "textbutton_style"
                        action Function(SD_NewImage)
                        tooltip "Generate new image"
                        text "+"
                    button:
                        style "textbutton_style"
                        action Function(SD_RefreshImage)
                        tooltip "Regenerate current image"
                        text "o"
                    button:
                        style "textbutton_style"
                        action Function(SD_DeleteImage)
                        tooltip "Delete current image"
                        text "X"
                    button:
                        style "textbutton_style"
                        action Function(SD_RightImage)
                        tooltip "Next image"
                        text ">"

        use default_tooltip("SD_update_button")
    else:    
        # Optional: show a disabled state or nothing
        frame:
            xalign 0.95 # 0.925
            yalign 0.085 # 1
            background Solid("#000000aa")
            padding (20, 5) # Padding inside the frame
            vbox:
                spacing 5
                hbox:
                    xalign 0.5
                    text "No one in view... how boring..." size 20 xalign 0.5 color "#ffffff"

transform middle_right:
    xpos 1400 xanchor 1 ypos 550 yanchor 0.5
transform center:
    xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5

screen genAI_image(image_path):
    modal False

    layer "solo"
    zorder 10

    frame:
        background None
        xfill True
        yfill True

        # Center the image
        frame:
            background None
            at middle_right
            imagebutton:
                idle Transform(Image(image_path), size=(512, calculate_display_height()))
                hover Transform(Image(image_path), size=(512, calculate_display_height()))
                action Function(toggle_genAI_fullscreen)

screen genAI_image_fullscreen(image_path):
    modal True

    #layer "master"
    zorder 100

    frame:
        background "#000000aa"
        xfill True
        yfill True

        # Center the image
        frame:
            background None
            at center
            $ width, height = calculate_fullscreen_dimensions()
            imagebutton:
                idle Transform(Image(image_path), size=(width, height))
                hover Transform(Image(image_path), size=(width, height))
                action Function(toggle_genAI_fullscreen)

screen generating_indicator():
    zorder 101 # Ensure it's above the image but below the fullscreen overlay potentially
    layer "solo"

    frame:
        background "#000000aa" # Semi-transparent background
        xalign 0.925
        yalign 0.27
        padding (20, 10)

        text "Generating " + get_progress_text() size 24 color "#ffffff" xalign 0.5

screen sd_event_handler():
    layer "solo"
    # Persistent screen to poll for thread completion
    timer 0.1 repeat True action Function(Check_SD_Completion)

screen SDConfig_menu():
    modal True

    frame:
        xalign 0.95
        yalign 0.5
        background "#1a45a1ee"
        padding (20, 20)

        viewport:
            ysize 800
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                spacing 15

                # Header
                frame:
                    background "#ffffff22"
                    padding (10, 5)
                    xfill True
                    text "Stable Diffusion Settings" size 24 xalign 0.5 color "#ffffff"

                # Connection Status
                if not have_connection:
                    frame:
                        background "#ff000044"
                        padding (10, 10)
                        vbox:
                            xalign 0.5
                            spacing 10
                            text "No connection to Stable Diffusion API" size 16 xalign 0.5
                            button:
                                style "dropdown_button"
                                xalign 0.5
                                action Function(retry_connection)
                                text "Retry Connection"
                else:
                    # Main Settings Area
                    vbox:
                        spacing 10

                        # Prompt profile settings
                        frame:
                            background "#ffffff22"
                            padding (10, 10)
                            vbox:
                                spacing 8

                                # Prompts
                                hbox:
                                    spacing 10
                                    text "Profile:"
                                    $ prompts = available_prompt_sets
                                    if prompts:
                                        button:
                                            style "dropdown_button"
                                            action ShowMenu("prompts_selection_dropdown")
                                            text "[sd_get_setting('sd_selected_prompt', 'No Profile')]" size 16
                                    else:
                                        text "No prompts available" size 16 color "#ff0000"

                        # Is Model Installed and are required Lora installed
                        frame:
                            background "#ffffff22"
                            padding (10, 10)
                            vbox:
                                spacing 8
                                button:
                                    style "toggle_button_wide"
                                    action Function(check_installed)
                                    text "Check Installed Models and Loras" size 16
                                $ prompt_data = sd_get_prompt_data_by_name(sd_get_setting('sd_selected_prompt', 'default'))
                                if prompt_data:
                                    $ model_name = prompt_data.get('Model', None)
                                    if model_name != None and model_name != "":
                                        $ model_installed = is_model_installed(model_name)
                                        text "[model_name] - Installed: " + str(model_installed) size 16 color ("#00ff00" if model_installed else "#ff0000")
                                        if not model_installed and "ModelURL" in prompt_data:
                                            button:
                                                style "toggle_button"
                                                action Function(webbrowser.open, prompt_data.get('ModelURL', ''))
                                                text "Download" size 12
                                
                                # LoRA List
                                if prompt_data and 'loras' in prompt_data:
                                    text "Required LoRAs:" size 16
                                    hbox:
                                        spacing 10
                                        box_wrap True
                                        for i, lora_data in enumerate(prompt_data.get('loras', [])):
                                            hbox:
                                                spacing 5
                                                $ lora_installed = is_lora_installed(lora_data['Name'])
                                                text "[lora_data['Name']] installed: [str(lora_installed)]" size 14 color ("#00ff00" if lora_installed else "#ff0000")
                                                if not lora_installed:
                                                    button:
                                                        style "toggle_button"
                                                        action Function(webbrowser.open, lora_data['URL'])
                                                        text "Download" size 12
                                                if i < len(prompt_data.get('loras', [])) - 1:
                                                    text " - " size 14
                        # Create debug file
                        frame:
                            background "#ffffff22"
                            padding (10, 10)
                            button:
                                style "toggle_button_wide"
                                action Function(create_debug_tar)
                                text "Generate a debug file to report a bug" size 12

                        # Model Settings
                        frame:
                            background "#ffffff22"
                            padding (10, 10)
                            vbox:
                                spacing 8
                                # Model Selection
                                hbox:
                                    spacing 10
                                    text "Model:" yalign 0.5
                                    $ models = available_models
                                    if len(models) > 0:
                                        button:
                                            style "dropdown_button"
                                            action ShowMenu("model_selection_dropdown")
                                            text "[sd_get_setting('sd_selected_model', 'No Model')]" size 16
                                    else:
                                        text "No models available" size 16 color "#ff0000"

                                # Sampler Selection
                                hbox:
                                    spacing 10
                                    text "Sampler:" yalign 0.5
                                    $ samplers = get_available_samplers()
                                    if samplers:
                                        button:
                                            style "dropdown_button"
                                            action ShowMenu("sampler_selection_dropdown")
                                            text "[sd_get_setting('sd_selected_sampler', 'No Sampler')]" size 16
                                    else:
                                        text "No samplers available" size 16 color "#ff0000"

                                # Scheduler Selection
                                hbox:
                                    spacing 10
                                    text "Scheduler:" yalign 0.5
                                    $ schedulers = get_available_schedulers()
                                    if schedulers:
                                        button:
                                            style "dropdown_button"
                                            action ShowMenu("scheduler_selection_dropdown")
                                            text "[sd_get_setting('sd_selected_scheduler', 'No Scheduler')]" size 16
                                    else:
                                        text "No scheduler available" size 16 color "#ff0000"

                        # Generation Settings
                        frame:
                            background "#ffffff22"
                            padding (10, 10)
                            vbox:
                                spacing 8

                                # Steps and CFG Scale
                                hbox:
                                    spacing 20
                                    vbox:
                                        spacing 5
                                        text "Steps:"
                                        button:
                                            style "value_button"
                                            action Show("input_dialog", title="Enter Steps", current_value=sd_get_setting('sd_steps_value', 20), value_changed_func=on_steps_value_changed, allow="0123456789", max_length=3)
                                            text "[sd_get_setting('sd_steps_value', 20)]" size 16

                                    vbox:
                                        spacing 5
                                        text "CFG Scale:"
                                        button:
                                            style "value_button"
                                            action Show("input_dialog", title="Enter CFG Scale", current_value=sd_get_setting('sd_cfg_scale_value', 7.0), value_changed_func=on_cfg_scale_value_changed, allow="0123456789.", max_length=4)
                                            text "[sd_get_setting('sd_cfg_scale_value', 7.0)]" size 16

                                    # Resolution
                                    vbox:
                                        spacing 5
                                        text "Resolution:" yalign 0.5
                                        hbox:
                                            button:
                                                style "value_button"
                                                action Show("input_dialog", title="Enter Width", current_value=sd_get_setting('sd_width_value', 512), value_changed_func=on_width_value_changed, allow="0123456789", max_length=4)
                                                text "[sd_get_setting('sd_width_value', 512)]" size 16
                                            text "×" yalign 0.5
                                            button:
                                                style "value_button"
                                                action Show("input_dialog", title="Enter Height", current_value=sd_get_setting('sd_height_value', 768), value_changed_func=on_height_value_changed, allow="0123456789", max_length=4)
                                                text "[sd_get_setting('sd_height_value', 768)]" size 16
                                    vbox:
                                        spacing 5
                                        text "Auto Generate:" yalign 0.5
                                        hbox:
                                            button:
                                                style "toggle_button"
                                                action Function(toggle_auto_generate)
                                                text get_auto_generate_toggle_text()

                        #frame:
                        #    background "#ffffff33"
                        #    padding (10, 5)
                        #    vbox:
                        #        spacing 5
                        #        hbox:
                        #            spacing 10
                        #            text "Prompt Style:"
                        #            button:
                        #                style "dropdown_button"
                        #                action Show("input_dialog", title="Enter Prompt Style", current_value=sdClient.get_style_prompt(), value_changed_func=sdClient.set_custom_prompt_style, allow=None, max_length=1000)
                        #                text sdClient.get_style_prompt().replace("[","[[")
                                # Global positive prepend
                        #        hbox:
                        #            spacing 10
                        #            text "Global positive prepend" yalign 0.5
                        #            button:
                        #                style "dropdown_button"
                        #                action Show("input_dialog", title="Enter Global positive prepend", current_value=sd_get_setting('sd_global_positive_prepend', ''), value_changed_func=on_global_positive_prepend_value_changed, allow=None, max_length=1000)
                        #                text "[sd_get_setting('sd_global_positive_prepend', '')]"
                                # Global negative prepend
                        #        hbox:
                        #            spacing 10
                        #            text "Global negative prepend" yalign 0.5
                        #            button:
                        #                style "dropdown_button"
                        #                action Show("input_dialog", title="Enter Global negative prompt", current_value=sd_get_setting('sd_global_negative_prepend', ''), value_changed_func=on_global_negative_prepend_value_changed, allow=None, max_length=1000)
                        #                text "[sd_get_setting('sd_global_negative_prepend', '')]"

                        # Seed Controls
                        $ person_data = get_current_person_data()
                        if person_data != None:
                            frame:
                                background "#ffffff22"
                                padding (10, 10)
                                vbox:
                                    spacing 5
                                    hbox:
                                        spacing 10
                                        text "Seed:" yalign 0.5
                                        button:
                                            style "dropdown_button"
                                            action Show("input_dialog", title="Enter Seed", current_value=person_data.seed, value_changed_func=on_seed_value_changed, extra_args=[person_data], allow="0123456789", max_length=10)
                                            text "[person_data.seed]" size 16
                                            xsize 150
                                        button:
                                            style "dropdown_button"
                                            action Function(generate_new_seed, person_data)
                                            text "New Random Seed" size 16

                            # Prompt Controls
                            frame:
                                background "#ffffff22"
                                padding (10, 10)
                                vbox:
                                    spacing 8

                                    # Positive Prompt
                                    vbox:
                                        spacing 5
                                        hbox:
                                            spacing 10
                                            text "Positive Prompt:" yalign 0.5
                                            button:
                                                style "toggle_button"
                                                action Function(toggle_positive_prompt_override)
                                                text "Override: " + get_positive_prompt_override_text().replace("[","[[") size 14

                                        if get_is_positive_prompt_override_enabled():
                                            button:
                                                style "prompt_button"
                                                action Show("input_dialog", title="Enter Prompt", current_value=get_positive_custom_prompt(), value_changed_func=on_positive_prompt_value_changed, allow=None, max_length=1000)
                                                text get_positive_custom_prompt().replace("[","[[")
                                        else:
                                            frame:
                                                background "#ffffff11"
                                                padding (10, 5)
                                                text get_positive_prompt().replace("[","[[")
                                            hbox:
                                                spacing 10
                                                text "Append:" yalign 0.5
                                                button:
                                                    style "prompt_button"
                                                    action Show("input_dialog", title="Append To Prompt", current_value=get_positive_appended_prompt(), value_changed_func=on_positive_appended_prompt_value_changed, allow=None, max_length=1000)
                                                    text get_positive_appended_prompt().replace("[","[[") or "None"

                                    # Negative Prompt
                                    vbox:
                                        spacing 5
                                        hbox:
                                            spacing 10
                                            text "Negative Prompt:" yalign 0.5
                                            button:
                                                style "toggle_button"
                                                action Function(toggle_negative_prompt_override)
                                                text "Override: " + get_negative_prompt_override_text().replace("[","[[") size 14

                                        if get_is_negative_prompt_override_enabled():
                                            button:
                                                style "prompt_button"
                                                action Show("input_dialog", title="Enter Prompt", current_value=get_negative_custom_prompt(), value_changed_func=on_negative_prompt_value_changed, allow=None, max_length=1000)
                                                text get_negative_custom_prompt().replace("[","[[")
                                        else:
                                            frame:
                                                background "#ffffff11"
                                                padding (10, 5)
                                                text get_negative_prompt().replace("[","[[")
                                            hbox:
                                                spacing 10
                                                text "Append:" yalign 0.5
                                                button:
                                                    style "prompt_button"
                                                    action Show("input_dialog", title="Append To Prompt", current_value=get_negative_appended_prompt(), value_changed_func=on_negative_appended_prompt_value_changed, allow=None, max_length=1000)
                                                    text get_negative_appended_prompt() or "None"
                                        
                        # Advanced Settings
                        frame:
                            background "#ffffff22"
                            padding (10, 10)
                            vbox:
                                spacing 8

                                # Upscaling
                                hbox:
                                    spacing 10
                                    text "Upscaling:" yalign 0.5
                                    button:
                                        style "toggle_button"
                                        action Function(toggle_upscaling)
                                        text get_upscaling_toggle_text()

                                if sd_get_setting('sd_upscaling_enabled', False):
                                    hbox:
                                        spacing 20
                                        vbox:
                                            spacing 5
                                            text "Size:"
                                            button:
                                                style "value_button"
                                                action Show("input_dialog", title="Enter Upscaling Size", current_value=sd_get_setting('sd_upscaling_size', 1.75), value_changed_func=on_upscaling_size_changed, allow="0123456789.", max_length=4)
                                                text "[sd_get_setting('sd_upscaling_size', 1.75)]" size 16
                                        vbox:
                                            spacing 5
                                            text "Method:"
                                            $ upscalers = get_available_upscalers()
                                            if upscalers:
                                                button:
                                                    style "dropdown_button"
                                                    action ShowMenu("upscaler_selection_dropdown")
                                                    text "[sd_get_setting('sd_selected_upscaler', 'No Upscaler')]" size 16
                                            else:
                                                text "No upscaler available" size 16 color "#ff0000"


                                # ADetailer
                                hbox:
                                    spacing 10
                                    text "ADetailer:" yalign 0.5
                                    button:
                                        style "toggle_button"
                                        action Function(toggle_adetailer)
                                        text get_adetailer_toggle_text()

                                if sd_get_setting('sd_adetailer_enabled', False):
                                    hbox:
                                        spacing 20
                                        vbox:
                                            spacing 5
                                            text "Method:"
                                            $adetailers = get_available_adetailers()
                                            if adetailers:
                                                button:
                                                    style "dropdown_button"
                                                    action ShowMenu("adetailer_selection_dropdown")
                                                    text "[sd_get_setting('sd_selected_adetailer', 'No ADetailer')]" size 16
                                            else:
                                                text "No adetailer available" size 16 color "#ff0000"


style toggle_button:
    background "#ffffff22"
    hover_background "#ffffff44"
    padding (10, 5)
    xsize 120

style toggle_button_wide:
    background "#ffffff22"
    hover_background "#ffffff44"
    padding (10, 5)
    xsize 200

style value_button:
    background "#ffffff22"
    hover_background "#ffffff44"
    padding (10, 5)
    xsize 100

style prompt_button:
    background "#ffffff22"
    hover_background "#ffffff44"
    padding (10, 5)
    xfill True

style dropdown_button:
    background None
    hover_background "#ffffff33"
    padding (10, 5)
    xfill True
    ysize None

screen model_selection_dropdown():
    modal True  # Makes the dropdown modal (blocks interaction with other elements)

    frame:
        style_prefix "dropdown"
        background "#2a55b1ee"
        xalign 0.95
        yalign 0.4

        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 2
                $ models = available_models
                for model in models:
                    button:
                        style "dropdown_button"
                        action [Function(set_selected_model, model), Return()]
                        text "[model]" size 16
                        padding (10, 5)
                        background "#ffffff33"
                        hover_background "#ffffff66"

screen sampler_selection_dropdown():
    modal True  # Makes the dropdown modal (blocks interaction with other elements)

    frame:
        style_prefix "dropdown"
        background "#2a55b1ee"
        xalign 0.95
        yalign 0.4

        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 2
                for sampler in available_samplers:
                    button:
                        style "dropdown_button"
                        action [Function(sd_set_setting, "sd_selected_sampler", sampler), Return()]
                        text "[sampler]" size 16
                        padding (10, 5)
                        background "#ffffff33"
                        hover_background "#ffffff66"

screen scheduler_selection_dropdown():
    modal True  # Makes the dropdown modal (blocks interaction with other elements)

    frame:
        style_prefix "dropdown"
        background "#2a55b1ee"
        xalign 0.95
        yalign 0.4

        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 2
                for scheduler in available_schedulers:
                    button:
                        style "dropdown_button"
                        action [Function(sd_set_setting, "sd_selected_scheduler", scheduler), Return()]
                        text "[scheduler]" size 16
                        padding (10, 5)
                        background "#ffffff33"
                        hover_background "#ffffff66"

screen upscaler_selection_dropdown():
    modal True  # Makes the dropdown modal (blocks interaction with other elements)

    frame:
        style_prefix "dropdown"
        background "#2a55b1ee"
        xalign 0.95
        yalign 0.4

        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 2
                for upscaler in available_upscalers:
                    button:
                        style "dropdown_button"
                        action [Function(sd_set_setting, "sd_selected_upscaler", upscaler), Return()]
                        text "[upscaler]" size 16
                        padding (10, 5)
                        background "#ffffff33"
                        hover_background "#ffffff66"

screen adetailer_selection_dropdown():
    modal True  # Makes the dropdown modal (blocks interaction with other elements)

    frame:
        style_prefix "dropdown"
        background "#2a55b1ee"
        xalign 0.95
        yalign 0.4

        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 2
                for adetailer in available_adetailers:
                    button:
                        style "dropdown_button"
                        action [Function(sd_set_setting, "sd_selected_adetailer", adetailer), Return()]
                        text "[adetailer]" size 16
                        padding (10, 5)
                        background "#ffffff33"
                        hover_background "#ffffff66"

screen prompts_selection_dropdown():
    modal True  # Makes the dropdown modal (blocks interaction with other elements)

    frame:
        style_prefix "dropdown"
        background "#2a55b1ee"
        xalign 0.95
        yalign 0.4

        viewport:
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 2
                for prompts in available_prompt_sets:
                    $ prompt_display_name = get_promptprofile_name(prompts)
                    button:
                        style "dropdown_button"
                        action [Function(set_data_from_json, prompts), Return()]
                        text "[prompt_display_name]" size 16
                        padding (10, 5)
                        if sd_get_setting('sd_selected_model') != None and sd_get_setting('sd_selected_model').split('.')[0] == prompts['Model'] and sd_get_setting('sd_selected_prompt') == prompts['Name']:
                            background "#ff00ff33"
                        else:
                            background "#ffffff33"
                        hover_background "#ffffff66"

screen input_dialog(title, current_value, value_changed_func, allow="0123456789.", max_length=4):
    modal True

    default input_value = str(current_value)

    frame:
        style_prefix "confirm"
        xalign 0.5
        yalign 0.5
        background "#1a45a1ee"
        padding (30, 30)

        has vbox:
            spacing 10
            xalign 0.5

        label title:
            style "confirm_prompt"
            xalign 0.5

        frame:
            background "#888888"
            xsize 500
            ysize 50
            xalign 0.5
            xpadding 10
            ypadding 5

            has fixed:
                xfit True
                yfit True

            input:
                value ScreenVariableInputValue("input_value")
                length max_length
                if allow != None:
                    allow allow
                style "menu_text_style"
                xalign 0.5
                yalign 0.5
                copypaste True

        hbox:
            spacing 20
            xalign 0.5
            textbutton "Confirm" action [Function(value_changed_func, input_value), Hide("input_dialog")]
            textbutton "Cancel" action Hide("input_dialog")

screen setup_info_box(title, description):
    modal True  # Makes the box block interaction with other elements

    frame:
        background "#1a45a1ee"  # Matching the style of other screens
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 15
            xsize 600  # Fixed width for the box

            text title:
                size 24
                xalign 0.5
                color "#ffffff"

            text description:
                size 16
                color "#ffffff"
                text_align 0.5
                xalign 0.5

            vbox:
                xalign 0.5
                spacing 20

                button:
                    style "dropdown_button"
                    action Function(open_local_html, "game/Mods/GenAI/stable-diffusion-guide.html")
                    text "Open Documentation" size 16

                button:
                    style "dropdown_button"
                    action Hide("setup_info_box")
                    text "Close" size 16
