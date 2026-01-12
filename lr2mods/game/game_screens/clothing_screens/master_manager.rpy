#Not technically a screen, but critical for managing proper access to all of the other screens.
label outfit_master_manager(wardrobe = mc.designed_wardrobe, **kwargs): #New outfit manager that centralizes exporting, modifying, duplicating, and deleting. Call this and pass any args/kwargs that would normally be passed to outfit_creator.

label .continue_manage_outfit():  # internal loop label
    # hide existing scene
    $ clear_scene()

    call screen outfit_select_manager(wardrobe, **kwargs)

    $ outfit_type = None
    $ outfit = None
    $ slut_limit = kwargs.get("slut_limit", None)
    $ outfit_validator = kwargs.get("outfit_validator", None)

    if isinstance(_return, (list, tuple, set)):
        #If we are returning an outfit we should be in one of the three sets (if not: panic!)
        $ command = _return[0]
        $ wardrobe = _return[1]

        if command in ("finish", "select"):
            $ wardrobe = None
            if "the_person" in globals():   # restore character on screen
                $ the_person.draw_person()
            else:
                $ clear_scene()
            if command == "select":
                return _return[2]
            return None #We're done and want to leave.

        if command == "new_full":
            $ outfit_type = "full"
            call screen outfit_creator(Outfit("New Outfit"), outfit_type = outfit_type, slut_limit = slut_limit, start_mannequin = kwargs.get("start_mannequin", "mannequin"), outfit_validator = outfit_validator)
            $ outfit = _return

        elif command == "new_over":
            $ outfit_type = "over"
            call screen outfit_creator(Outfit("New Overwear Set"), outfit_type = outfit_type, slut_limit = slut_limit, start_mannequin = kwargs.get("start_mannequin", "mannequin"), outfit_validator = outfit_validator)
            $ outfit = _return

        elif command == "new_under":
            $ outfit_type = "under"
            call screen outfit_creator(Outfit("New Underwear Set"), outfit_type = outfit_type, slut_limit = slut_limit, start_mannequin = kwargs.get("start_mannequin", "mannequin"), outfit_validator = outfit_validator)
            $ outfit = _return

        else:
            $ outfit = _return[2]
            if outfit in wardrobe.outfit_sets:
                $ outfit_type = "full"

            elif outfit in wardrobe.overwear_sets:
                $ outfit_type = "over"

            elif outfit in wardrobe.underwear_sets:
                $ outfit_type = "under"

            else:
                "We couldn't find it anywhere! PANIC!"
                return None

            $ original_outfit = outfit.get_copy()

            call screen outfit_creator(outfit, outfit_type = outfit_type, slut_limit = slut_limit, start_mannequin = kwargs.get("start_mannequin", "mannequin"), outfit_validator = outfit_validator)
            $ outfit = _return

            if isinstance(outfit, Outfit) and command == "modify":
                # remove original outfit
                $ wardrobe.remove_outfit(original_outfit)

            $ original_outfit = None

    if isinstance(outfit, Outfit):
        $ outfit.name = renpy.input("Please name this outfit.", default = outfit.name, exclude="[]{}")
        while outfit.name == "" or wardrobe.has_outfit_with_name(outfit.name):
            if wardrobe.has_outfit_with_name(outfit.name):
                $ outfit.name = renpy.input("Please enter a name that does not already exist in this wardrobe.", default = outfit.name, exclude="[]{}")
            if outfit.name == "":
                $ outfit.name = renpy.input("Please enter a non-empty name.", default = outfit.name, exclude="[]{}")

        python:
            if outfit_type == "under":
                wardrobe.add_underwear_set(outfit)
            elif outfit_type == "over":
                wardrobe.add_overwear_set(outfit)
            else: #Generally outfit_type == full, or some other uncaught error.
                wardrobe.add_outfit(outfit)

    # keep managing outfits until the user is done
    jump outfit_master_manager.continue_manage_outfit
