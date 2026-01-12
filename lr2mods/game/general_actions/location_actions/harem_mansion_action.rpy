init 3 python:
    def harem_mansion_threesome_requirement():
        if mc.location.person_count > 1:
            return True
        return "Not enough girls around the mansion"

    def harem_mansion_threesome_initialization(self):
        harem_mansion.add_action(self)
        return

    def build_harem_mansion_threesome_partner_menu(person, partner_list = []):
        temp_list = []
        for other_person in partner_list:
            relationship = town_relationships.get_relationship(person, other_person)
            if relationship:
                temp_list.append((f"{other_person.name} {other_person.last_name}\n{{menu_green}}{relationship.type_b}{{/menu_green}}", other_person))
        temp_list.insert(0, "Partner")
        temp_list.append("Back")
        return temp_list

    mansion_threesome_action = ActionMod("Harem Threesome", harem_mansion_threesome_requirement, "harem_mansion_threesome_label",
        initialization = harem_mansion_threesome_initialization, menu_tooltip = "Start a threesome with any of your harem girls.", category = "Home")

label harem_mansion_threesome_label():
    $ scene_manager = Scene()
    "You take a look around your mansion to see which girls are around."
    call screen main_choice_display(build_menu_items([get_sorted_people_list(known_people_at_location(mc.location), "Start threesome with...", "Back")]))
    $ the_person = _return
    if isinstance(the_person, Person):
        $ scene_manager.add_actor(the_person)
        mc.name "Hey [the_person.title], we should have a threesome."
        the_person "Sounds fun, who do you want to join us?"
        call screen main_choice_display(build_menu_items([build_harem_mansion_threesome_partner_menu(the_person, partner_list = (known_people_at_location(mc.location)))]))
        $ the_other_person = _return
        if isinstance(the_other_person, Person):
            mc.name "[the_other_person.fname]."
            if town_relationships.is_family(the_person, the_other_person):
                $ name = town_relationships.get_relationship_type(the_person, the_other_person)
                if the_person.opinion.incest > 0:
                    the_person "Kinky, you know I like hooking up with my [name!l]!"
                    mc.name "I knew you would, you little slut."
                else:
                    the_person "Seriously? Isn't that a little weird, a threesome with my [name!l]?"
                    mc.name "Give it a try, you might even enjoy it."
            elif town_relationships.get_relationship(the_person, the_other_person).type_b in ["Rival", "Nemesis"]:
                the_person "Really? You know we don't exactly get along right?"
                mc.name "Don't worry, we are just going to have some fun."
            else:
                the_person "Great, we always have fun together."

            "You call [the_other_person.fname] over."
            $ scene_manager.add_actor(the_other_person, display_transform = character_center_flipped)

            mc.name "Hey [the_other_person.fname]. We are going to have some fun together."
            the_other_person "Alright, let's get started."

            "As you move over to one of the beds, the girls get ready for the threesome."
            $ scene_manager.strip_to_vagina()

            call start_threesome(the_person, the_other_person) from _call_start_threesome_mansion_threesome

            $ town_relationships.improve_relationship(the_person, the_other_person)

        else:
            mc.name "Nevermind, I don't know who else to pick."
            the_person "Oh, okay. Well if you change your mind let me know!"
            "She smiles at you and waits to see if you need something else."
    else:
        "None of them interest you enough to do anything right now."
    $ scene_manager.clear_scene()
    return
