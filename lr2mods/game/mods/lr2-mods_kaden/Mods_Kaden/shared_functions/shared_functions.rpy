init -99 python:
    global kaden_mod
    kaden_mod = True

    def kaden_test_req():
        return mc.business.name == "A Team"
    
init -1 python:
    def build_robe(the_person):
        temp_robe = None
        the_colour = the_person.favourite_colour
        color_list = []
        for col in WardrobeBuilder.color_prefs[the_colour]:
            color_list.append(WardrobeBuilder.color_prefs[the_colour][col])
        main_colour = get_random_from_list(color_list)
        temp_robe = bath_robe.get_copy()
        temp_robe.colour = main_colour
        temp_robe.colour[3] *= 1.0-(the_person.sluttiness/300.0)
        temp_robe.pattern = temp_robe.supported_patterns[renpy.random.choice(list(temp_robe.supported_patterns.keys()))]
        temp_robe.colour_pattern = WardrobeBuilder.get_color(the_person, main_colour)
        temp_robe.colour_pattern[3] *= 1.0-(the_person.sluttiness/300.0)
        return temp_robe

    def clothing_formatted_title(the_item):
        hexcode = Color(rgb = (the_item.colour[0], the_item.colour[1], the_item.colour[2]))
        formatted_title = "{color=" + hexcode.hexcode + "}" + the_item.name + "{/color}"
        return formatted_title

    def return_underwear(the_item):
        temp_list = []
        for key, list_of_values in mc.stolen_underwear.items():
            if the_item in list_of_values:
                mc.stolen_underwear[key] = []
                if len(list_of_values) > 1:
                    temp_list = list_of_values
                    temp_list.remove(the_item)
                    for clothing in temp_list:
                        mc.stolen_underwear[key].append(clothing)
        return

    def can_add_clothing(outfit, new_clothing):
        if new_clothing in dress_list:
            if outfit.can_add_dress(new_clothing):
                return True
        elif new_clothing in shirts_list or new_clothing in bra_list:
            if outfit.can_add_upper(new_clothing):
                return True
        elif new_clothing in pants_list or new_clothing in skirts_list or new_clothing in panties_list:
            if outfit.can_add_lower(new_clothing):
                return True
        elif new_clothing in socks_list or new_clothing in shoes_list:
            if outfit.can_add_feet(new_clothing):
                return True
        elif new_clothing in earings_list or new_clothing in bracelet_list or new_clothing in rings_list or new_clothing in neckwear_list:
            if outfit.can_add_accessory(new_clothing):
                return True
        return False

    def add_clothing(outfit, new_clothing, re_colour = None, pattern = None, colour_pattern = None):
        if can_add_clothing(outfit, new_clothing):
            if new_clothing in dress_list:
                outfit.add_dress(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in shirts_list or new_clothing in bra_list:
                outfit.add_upper(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in pants_list or new_clothing in skirts_list or new_clothing in panties_list:
                outfit.add_lower(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in socks_list or new_clothing in shoes_list:
                outfit.add_feet(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
            elif new_clothing in earings_list or new_clothing in bracelet_list or new_clothing in rings_list or new_clothing in neckwear_list:
                outfit.can_add_accessory(new_clothing, re_colour = None, pattern = None, colour_pattern = None)
        return

    def random_colours(person, number):
        if number < 1:
            number = 1
        the_colour = person.favourite_colour
        color_list = []
        for col in WardrobeBuilder.color_prefs[the_colour]:
            color_list.append(WardrobeBuilder.color_prefs[the_colour][col])
        if number > len(color_list):
            color_list.append([0.15,0.15,0.15,0.95])
            color_list.append([1.0,1.0,1.0,0.95])
        return_list = []
        for x in range(number):
            main_colour = get_random_from_list(color_list)
            if len(color_list) > number - x:
                color_list.remove(main_colour)
            main_colour = Color(rgb=(main_colour[0], main_colour[1], main_colour[2]), alpha = main_colour[3])
            main_colour = [main_colour.rgb[0], main_colour.rgb[1], main_colour.rgb[2], main_colour.alpha]
            return_list.append(main_colour)
        return return_list

    def generalised_dressing_description(the_person, outfit, group_display = None, other_people = None, position = None):
        scene_manager = Scene()
        for cloth in [x for x in the_person.outfit.upper_body + the_person.outfit.lower_body + the_person.outfit.feet + the_person.outfit.accessories if x.half_off]:
            cloth.half_off = False
            scene_manager.add_actor(the_person)
            renpy.say(None, the_person.title + " adjusts her " + cloth.display_name + ", restoring it to the way it is normally worn.")
        if isinstance(outfit, Clothing):
            temp_list = [temp_list] #Lets you hand over a single item to put on
        else:
            temp_list = []
            for item in outfit.get_full_strip_list():
                temp_list.append(item)
        test_outfit = the_person.outfit.get_copy() #Use a copy to keep track of what's changed between iterations, so we can narrate tits being out, etc.
        loop_count = 0 #Used to keep all of the other people on the same track as the main stripper
        for item in list(reversed(temp_list)):
            if group_display is not None:
                if can_add_clothing(the_person.outfit, item):
                    add_clothing(the_person.outfit, item)
                group_display.redraw_group()
                if other_people is not None:
                    for person_tuple in other_people:
                        another_person = person_tuple[0]
                        another_temp_list = person_tuple[1]
                        if item == temp_list[-1]:
                            if can_add_clothing(another_person.outfit, another_temp_list):
                                add_clothing(another_person.outfit, another_temp_list)
                        elif len(another_temp_list) > loop_count:
                            if can_add_clothing(another_person.outfit, another_temp_list[loop_count]):
                                add_clothing(another_person.outfit, another_temp_list[loop_count])
                        group_display.redraw_group()
            else:
                if can_add_clothing(the_person.outfit, item):
                    add_clothing(the_person.outfit, item)
                    scene_manager.update_actor(the_person)
                    if test_outfit.tits_available and not the_person.tits_available: #Tits are contained
                        if the_person.has_large_tits:
                            renpy.say(None, the_person.title + " pulls on her " + item.display_name + ", covering her " + the_person.tits_description + ".")
                        else:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + " concealing her " + the_person.tits_description + ".")
                    elif test_outfit.tits_visible and not the_person.outfit.tits_visible: #Tits are fully covered
                        if the_person.has_large_tits:
                            renpy.say(None, the_person.title + " pulls on her " + item.display_name + ", hiding away all trace of her " + the_person.tits_description + ".")
                        else:
                            renpy.say(None, the_person.title + " dons her " + item.display_name + ", hiding away her " + the_person.tits_description + ".")
                    elif test_outfit.vagina_available and not the_person.vagina_available: #Pussy contained
                        if item.underwear:
                            renpy.say(None, the_person.title + " slips on her " + item.display_name + ", adjusting them to cover her " + the_person.pubes_description + " pussy.")
                        else:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + " hiding her " + the_person.pubes_description + " pussy underneath.")
                    elif test_outfit.vagina_visible and not the_person.outfit.vagina_visible: #Pussy fully covered
                        renpy.say(None, the_person.title + " puts on her " + item.display_name + ", covering her " + the_person.pubes_description + " pussy.")
                    elif item.layer == 2:
                        if test_outfit.wearing_panties and pelvis_region in item.half_off_regions:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + ", covering her " + test_outfit.get_panties().display_name + ".")
                        elif test_outfit.wearing_bra and torso_region in item.half_off_regions:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + ", concealing her " + test_outfit.get_bra().display_name + ".")
                    else:
                        rand = renpy.random.randint(0,3)
                        if rand == 0:
                            renpy.say(None, the_person.title + " slips on her " + item.display_name + ".")
                        elif rand == 1:
                            renpy.say(None, the_person.title + " puts on her " + item.display_name + ".")
                        elif rand == 2:
                            renpy.say(None, the_person.title + " slips her " + item.display_name + " on.")
                        else:
                            renpy.say(None, the_person.title + " pulls on her " + item.display_name + ".")
                    if can_add_clothing(test_outfit, item):
                        add_clothing(test_outfit, item) #Update our test outfit.
                    loop_count += 1
                    if group_display is not None: #This is needed to ensure the animation times for the clothing fade out are reset. Not ideal for a speedy draw, but it'll do for now.
                        scene_manager.clear_scene()
                        group_display.redraw_group()
        return

    def plural_display_name(clothing):
        if clothing in shoes_list or socks_list or pants_list or panties_list:
            if clothing not in [thong, tiny_g_string]:
                return True
        return False

    def home_residents(temp_location):
        residents = []
        for person in [x for x in all_people_in_the_game() if x.home == temp_location]:
            residents.append(person)
        return residents

    def get_existing_rivals(self, person):
        return_list = []
        for relationship in self.get_relationship_type_list(person, types = ["Nemesis", "Rival"]):
            return_list.append(relationship[0])
        return return_list

    def get_existing_rival_count(self, person):
        return builtins.len(get_existing_rivals(self, person))

    def get_existing_friends(self, person):
        return_list = []
        for relationship in self.get_relationship_type_list(person, types = ["Friend", "Best Friend"]):
            return_list.append(relationship[0])
        return return_list

    def get_exisiting_friend_count(self, person):
        return builtins.len(get_existing_friends(self, person))

    def get_exisiting_family_count(self, person):
        return builtins.len(town_relationships.get_family_members(person))

    def pregnant_family(person):
        the_mothers = []
        if len(town_relationships.get_family_members(person)) > 0:
            for x in town_relationships.get_family_members(person):
                if x.event_triggers_dict.get("preg_knows", False):
                    if x.event_triggers_dict.get("preg_tits_date", 999) < day-5:
                        the_mothers.append(x)
        return the_mothers

    def pregnant_friends(person):
        the_mothers = []
        if len(get_existing_friends(town_relationships, person)) > 0:
            for x in get_existing_friends(town_relationships, person):
                if x.event_triggers_dict.get("preg_knows", False):
                    if x.event_triggers_dict.get("preg_tits_date", 999) < day-5:
                        the_mothers.append(x)
        return the_mothers

    def pregnant_enemies(person):
        the_mothers = []
        if len(get_existing_rivals(town_relationships, person)) > 0:
            for x in get_existing_rivals(town_relationships, person):
                if x.event_triggers_dict.get("preg_knows", False):
                    if x.event_triggers_dict.get("preg_tits_date", 999) < day-5:
                        the_mothers.append(x)
        return the_mothers

    def pregnant_people(person): #change to body type check?
        the_mothers = []
        if pregnant_family(person):
            the_mothers.extend(pregnant_family(person))
        if pregnant_friends(person):
            the_mothers.extend(pregnant_friends(person))
        if pregnant_enemies(person):
            the_mothers.extend(pregnant_enemies(person))
        return the_mothers

init 3 python:
    def get_body_description(person):
        if person.body_type == "thin_body":
            body_description = get_random_from_list(["slender physique", "lithe frame", "trim figure", "lean build"])
        elif person.body_type == "standard_body":
            body_description = get_random_from_list(["average physique", "typical frame", "standard figure", "regular build"])
        elif person.body_type == "curvy_body":
            body_description = get_random_from_list(["shapely silhouette", "hourglass figure", "voluptuous curves", "well-defined contours"])
        else: #pregnant
            body_description = get_random_from_list(["radiant physique", "blossoming frame", "radiant figure", "expectant build"])
        return body_description

    def get_body_word(person):
        if person.body_type == "thin_body":
            body_word = get_random_from_list(["slender", "lithe", "trim", "lean", "sleek", "graceful", "graceful"])
        elif person.body_type == "standard_body":
            body_word = get_random_from_list(["limber", "supple", "sculpted", "sinuous"])
        elif person.body_type == "curvy_body":
            body_word = get_random_from_list(["shapely", "curvaceous", "voluptuous", "sensuous"])
        else: #pregnant
            body_word = get_random_from_list(["swelling", "blossoming", "expanding", "curving"])
        return body_word

    def wardrobe_exporter_requirement():
        return True

    def wardrobe_exporter_initialization(self):
        clothing_store.add_action(wardrobe_exporter_action)
        return

    wardrobe_exporter_action = ActionMod("DEV: Build and export outfits", wardrobe_exporter_requirement, "wardrobe_exporter_label",
        initialization = wardrobe_exporter_initialization, menu_tooltip = "Build and export outfits", category = "Misc")

label wardrobe_exporter_label():
    $ temp_slut = 0
    $ temp_choice = None
    call screen main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game(), "Beach Outfit Test", "Back")]))
    $ person_choice = _return
    if person_choice != "Back":
        "Pick an outfit builder"
        menu:
            "Beach":
                $ temp_choice = "Beach_Wardrobe"
            "Pajamas":
                $ temp_choice = "Pajama_Wardrobe"
            "Company":
                $ temp_choice = "Company_Wardrobe"
            "Default Wardrobe":
                $ temp_choice = "New_Default"
            "Lingerie Wardrobe":
                $ temp_choice = "New_Lingerie"
            "Exit":
                $ temp_slut = 100
        while temp_slut < 100:
            if temp_choice == "Beach_Wardrobe":
                $ person_choice.apply_outfit(get_beach_outfit(person_choice, sluttiness = temp_slut))
            elif temp_choice == "Pajama_Wardrobe":
                $ person_choice.apply_outfit(get_pajama_outfit(person_choice, sluttiness = temp_slut))    
            elif temp_choice == "Company_Wardrobe":
                $ person_choice.apply_outfit(design_others_outfit(person_choice, person_choice, target = temp_slut))
            elif temp_choice == "New_Default":
                $ person_choice.apply_outfit(default_wardrobe.get_random_appropriate_outfit(temp_slut, sluttiness_min = temp_slut-1))
            elif temp_choice == "New_Lingerie":
                $ person_choice.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(temp_slut, sluttiness_min = temp_slut-1))
            $ person_choice.draw_person(emotion = "happy")
            $ outfit_slut = person_choice.outfit.outfit_slut_score
            "Current sluttiness = [temp_slut]. Outfit sluttiness = [outfit_slut]."
            $ done = False
            while not done:
                menu:
                    "Export Overwear":
                        $ over = person_choice.outfit.get_copy()
                        python:
                            for clothing in over.get_full_strip_list(strip_feet = True):
                                if clothing.layer < 2:
                                    over.remove_clothing(clothing)
                            over.update_name()
                        $ log_outfit(over, outfit_class = "OverwearSets", wardrobe_name = temp_choice)
                        "[over.name] exported."
                    "Export Underwear":
                        $ under = person_choice.outfit.get_copy()
                        python:
                            for clothing in under.get_full_strip_list(strip_feet = True):
                                if clothing.layer > 1:
                                    under.remove_clothing(clothing)
                            under.update_name()
                        $ log_outfit(under, outfit_class = "UnderwearSets", wardrobe_name = temp_choice)
                        "[under.name] exported."
                    "Export Full Outfit":
                        $ outfit = person_choice.outfit.get_copy()
                        $ outfit.update_name()
                        $ log_outfit(outfit, outfit_class = "FullSets", wardrobe_name = temp_choice)
                        "[outfit.name] exported."
                    "Continue":
                        $ done = True
                    "Exit":
                        $ done = True
                        $ temp_slut = 100
            $ temp_slut += 3
    return
