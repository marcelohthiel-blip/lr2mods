init -1 python:
    biotech_body_modifications = []

init 3 python:
    def build_cloning_facility_requirement():
        if clone_facility.visible:
            return False
        if not genetic_modification_policy.is_owned:
            return False
        if not mc.business.has_funds(100000):
            return "Requires: $100,000"
        return True

    biotech_build_cloning_facility = Action("Build Cloning Facility", build_cloning_facility_requirement, "biotech_build_cloning_facility")

    def biotech_clone_person_requirement():
        if time_of_day == 4:
            return "Too late"
        elif not clone_facility.visible:
            return "Cloning facility required"
        return True

    biotech_clone_person = Action("{image=dna_sequence} Clone a person {image=time_advance}", biotech_clone_person_requirement, "biotech_clone_person",
        menu_tooltip = "Create a near identical clone of the targeted person")

    def biotech_modify_person_requirement():
        return True

    biotech_modify_person = Action("Modify a person", biotech_modify_person_requirement, "biotech_modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")

    def biotech_change_body_requirement():
        if mc.business.is_trait_researched(weight_gain) and mc.business.is_trait_researched(weight_loss):
            return True
        return "Requires: Weight Promoter traits researched"

    biotech_change_body = Action("Change body: [the_person.body_type]", biotech_change_body_requirement, "biotech_change_body",
        menu_tooltip = "Modify [the_person.title]'s body type.")
    biotech_body_modifications.append(biotech_change_body)

    def biotech_change_skin_requirement():
        if mc.business.is_trait_researched("Pigment"):
            return True
        return "Requires: Pigment Trait researched"

    biotech_change_skin = Action("Change skin: [the_person.skin]", biotech_change_skin_requirement, "biotech_change_skin",
        menu_tooltip = "Modify [the_person.title]'s skin tone.")
    biotech_body_modifications.append(biotech_change_skin)

    def biotech_change_face_requirement():
        return True

    biotech_change_face = Action("Change face: [the_person.face_style]", biotech_change_face_requirement, "biotech_change_face",
        menu_tooltip = "Modify [the_person.title]'s face style.")
    biotech_body_modifications.append(biotech_change_face)

    def biotech_change_breasts_requirement():
        if mc.business.is_trait_researched(breast_enhancement) and mc.business.is_trait_researched(breast_reduction):
            return True
        return "Requires: Breast modification traits"

    biotech_change_breasts = Action("Change breasts: [the_person.tits]", biotech_change_breasts_requirement, "biotech_change_breasts",
        menu_tooltip = "Modify [the_person.title]'s cup size.")
    biotech_body_modifications.append(biotech_change_breasts)

    def clone_completion_requirement(min_day):
        return day > min_day

    def create_clone(person, clone_name, clone_last_name, clone_age):
        if clone_name is None:
            clone_name = Person.get_random_name()
        if clone_last_name is None:
            clone_last_name = Person.get_random_last_name()
        if clone_age is None:   # create clones as younger version of donor
            clone_age = renpy.random.randint(Person.get_age_floor(), min(person.age, Person.get_age_floor() + 3))
        clone_body = person.body_type
        if "pre_preg_body" in person.event_triggers_dict: # make sure we don't have the pregnant body type
            clone_body = person.event_triggers_dict["pre_preg_body"]

        clone = make_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = clone_body, face_style = person.face_style, tits = person.tits, height = person.height, hair_colour = person.hair_colour, hair_style = person.hair_style, skin = person.skin, eyes = person.eyes,
            personality = person.personality, starting_wardrobe = person.wardrobe, stat_array = [person.charisma, person.int, person.focus], skill_array = [person.hr_skill, person.market_skill, person.research_skill, person.production_skill, person.supply_skill], sex_skill_array = [person.foreplay_sex_skill, person.oral_sex_skill, person.vaginal_sex_skill, person.anal_sex_skill],
            sluttiness = person.sluttiness, obedience = person.obedience, happiness = person.happiness, love = person.love, job = unemployed_job, suggestibility = 25, work_experience = person.work_experience, start_home = clone_facility, title = "Clone", possessive_title = "your creation", mc_title = "Creator", relationship = "Single", kids = 0, forced_sexy_opinions = [["being submissive", 2 , True]])

        clone.set_schedule(clone_facility, time_slots = [0, 1, 2, 3, 4])
        clone.add_role(clone_role)
        clone.learn_job()

        #TODO: Do we want to add an option where the process fails?

        clone_facility.add_unique_on_room_enter_event(
            Action("Clone Finished {clone.identifier}",
                clone_completion_requirement,
                "clone_finished_label",
                requirement_args = day + TIER_3_TIME_DELAY,
                args = [clone],
                priority = 30)
        )
        return

    def simple_list_format(list_to_format, what_to_format, string = "", ignore = "", attrib = ""): # Returns a simple list for use in generic menus. Extensive use in the Biotech Actions.
        tuple_list = []                                                    # NOTE: Needed a generic list setup, this seems to cover most usecases I came across.
        for what_to_format in list_to_format:
            if what_to_format is not ignore:
                if attrib != "":
                    tuple_string = str(string) + str(vars(what_to_format)[attrib]) # e.g attrib = "name" for SerumTrait.name to be displayed
                    tuple_list.append((tuple_string, what_to_format))
                else:
                    tuple_list.append((str(string) + str(what_to_format), what_to_format))
            else:
                tuple_list.append((str(what_to_format), what_to_format))
        return tuple_list

    def build_body_type_choice_menu():
        body_types = [(x.replace("_", ' ').title(), x) for x in Person._list_of_body_types]
        body_types.append("Back")
        body_types.insert(0, "Body Type")
        return body_types

    def build_skin_style_choice_menu():
        skin_styles = [(x[0].title(), x[0]) for x in Person._list_of_skins]
        skin_styles.append("Back")
        skin_styles.insert(0, "Skin Type")
        return skin_styles

    def build_face_style_choice_menu():
        face_styles = [(x.replace("_", ' ').title(), x) for x in Person._list_of_faces]
        face_styles.append("Back")
        face_styles.insert(0, "Face Type")
        return face_styles

    def build_cup_size_choice_menu():
        cup_sizes = [x[0] for x in Person._list_of_tits]
        cup_sizes.append("Back")
        cup_sizes.insert(0, "Cup Size")
        return cup_sizes

    def build_gene_modification_menu():
        gene_modification_options = []
        for act in biotech_gene_modifications:
            gene_modification_options.append(act)
        gene_modification_options.append("Back")
        return gene_modification_options

    def build_body_modification_options_menu():
        body_modification_options = []
        for act in biotech_body_modifications:
            body_modification_options.append(act)
        body_modification_options.append("Back")
        return body_modification_options


    def cloning_facility_complete_requirement():
        return mc.business.is_open_for_business and day >= mc.business.get_event_day("cloning_facility_complete")

    def add_cloning_facility_completed_action():
        finish_day = (day + TIER_3_TIME_DELAY + renpy.random.randint(0, 5))
        mc.business.set_event_day("cloning_facility_complete", finish_day)
        cloning_facility_complete_action = Action("Cloning Facility Completed", cloning_facility_complete_requirement, "biotech_cloning_facility_completed")
        mc.business.add_mandatory_crisis(cloning_facility_complete_action)

label biotech_build_cloning_facility():
    "You decide to build the cloning facility and give a call to your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I want to extend my company with a high-tech facility."
    $ rnd_num = (TIER_3_TIME_DELAY + 5)
    "You go over the details with your contractor. It can take up to [rnd_num] days to complete."
    python:
        mc.business.change_funds(-100000, stat = "Real Estate")
        ceo_office.remove_action("biotech_build_cloning_facility")
        add_cloning_facility_completed_action()
    return

label biotech_cloning_facility_completed():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The cloning facility has been completed and is now ready for inspection."
    python:
        clone_facility.visible = True
    return

label biotech_gene_modifications():
    $ act_choice = call_formated_action_choice(build_gene_modification_menu())
    if act_choice == "Back":
        return
    else:
        $ act_choice.call_action()
        $ del act_choice
    jump biotech_gene_modifications

label biotech_clone_person():
    # only known people who are not unique character or clone herself (genetic degradation too high)
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list([x for x in known_people_in_the_game(unique_characters()) if x.can_clone], "Clone Person", "Back")]
        ))
    if isinstance(_return, Person):
        $ the_person = _return
        call cloning_process() from _call_cloning_process
    $ clear_scene()
    return

label clone_finished_label(the_person):
    $ clone_facility.add_person(the_person)

    "As you walk into the facility, you see the cloning process of [the_person.fname] has finished."
    "You open the tank and inspect the clone."
    $ the_person.draw_person()

    mc.name "Hello, [the_person.fname], how are you feeling?"
    the_person "Hello, [the_person.mc_title], I feel good, thank you."

    "It seems the process was successful."

    $ clear_scene()
    return


label cloning_process(): # default to the_person when not passed as parameter
    $ the_person.draw_person()
    $ clone_name = the_person.name.replace("a", "@").replace("e", "3").replace("i", "!").replace("o", "0")
    $ clone_last_name = the_person.last_name.replace("a", "@").replace("e", "3").replace("i", "!").replace("o", "0")
    $ clone_age = the_person.age

label .continue_cloning_process():
    menu:
        "Give the clone a name":
            $ clone_name = str(renpy.input("Name: ", clone_name, length = 20, exclude="[]{ }"))
            $ clone_last_name = str(renpy.input("Last name: ", clone_last_name, length = 20, exclude="[]{ }"))
        "Age":
            $ clone_age = builtins.int(renpy.input("Age: ", clone_age))
            if clone_age < 18:
                $ clone_age = 18
        "Begin production: {image=time_advance}\n{menu_red}Name: [clone_name] [clone_last_name], Age: [clone_age]{/menu_red}" if len(clone_name) >= 3 and len(clone_last_name) >= 3:
            $ create_clone(the_person, clone_name, clone_last_name, clone_age)
            "You enter all parameters in the system and start the cloning process by adding the sample DNA."
            "The new clone should be ready in about [TIER_3_TIME_DELAY] days."
            call advance_time() from _call_advance_time_cloning_process
            return
        "Begin production\n{menu_red}Requires: name parts at least 3 chars{/menu_red} (disabled)" if len(clone_name) < 3 or len(clone_last_name) < 3:
            pass
        "Back":
            return
    jump cloning_process.continue_cloning_process

label biotech_modify_person():
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_in_the_game(), "Modify Person", "Back")]
        ))
    if isinstance(_return, Person):
        $ the_person = _return
        call modification_process() from _call_modification_process
    return

#TODO: change modification process to custom screen that allows player to modify various aspects
#      of a person -> after confirming changes she moves into modification process (purgatory)
#      and is unavailable until all changes have been completed.
#      Perhaps also have her refuse the changes if they are to radical for her taste.

label modification_process(): # when called without specific person use the_person variable
    $ the_person.draw_person()
    $ act_choice = call_formated_action_choice(build_body_modification_options_menu())
    if act_choice == "Back":
        $ clear_scene()
        return
    else:
        $ act_choice.call_action()
        $ del act_choice
    jump modification_process

label biotech_change_body():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    call screen main_choice_display(build_menu_items([build_body_type_choice_menu()], False, False))
    if _return == "Back":
        return
    elif isinstance(the_person, Person):
        $ the_person.clean_cache()
        $ the_person.body_type = _return
        $ the_person.draw_person()
    jump biotech_change_body

label biotech_change_skin():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    call screen main_choice_display(build_menu_items([build_skin_style_choice_menu()], False, False))
    if _return == "Back":
        return
    elif isinstance(the_person, Person):
        $ the_person.clean_cache()
        $ the_person.skin = _return
        $ the_person.match_skin(_return)
        $ the_person.draw_person()
    jump biotech_change_skin

label biotech_change_face():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    call screen main_choice_display(build_menu_items([build_face_style_choice_menu()], False, False))
    if _return == "Back":
        return
    elif isinstance(the_person, Person):
        $ the_person.clean_cache()
        $ the_person.face_style = _return
        $ the_person.match_skin(the_person.skin)
        $ the_person.draw_person()
    jump biotech_change_face

label biotech_change_breasts():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    call screen main_choice_display(build_menu_items([build_cup_size_choice_menu()], False, False))
    if _return == "Back":
        return
    elif isinstance(the_person, Person):
        $ the_person.clean_cache()
        $ the_person.tits = _return
        $ the_person.draw_person()
    jump biotech_change_breasts
