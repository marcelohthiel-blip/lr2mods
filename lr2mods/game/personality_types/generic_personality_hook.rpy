# Generic Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels
init 2:
    default persistent.low_memory_wardrobes = True

init 100 python: # add to stack later then other mods (;ast to load)
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init 2 python:

    def create_bimbo():
        # add one bimbo to the game (on start of game)
        person = make_person(age=renpy.random.randint(21, 35), tits="DD", face_style = "Face_4", skin = "tan", stat_array = [4, 1, 2],
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 0.9]], personality = bimbo_personality,
            forced_opinions = [["high heels", 2, False]],
            forced_sexy_opinions = [["skimpy outfits", 2, False]])
        person.generate_home().add_person(person)
        return

    def create_alpha_personality():
        person = make_person(age = renpy.random.randint(25,35), personality = alpha_personality, relationship = "Single", stat_array = [5, 4, 3],
            forced_opinions = [["high heels", 2, False], ["the colour black", 2, False], ["the colour pink", -2, False], ["the colour green", -2, False]],
            forced_sexy_opinions = [["skimpy outfits", 2, False], ["being submissive", -1, False], ["taking control", 2, False]])
        person.generate_home().add_person(person)
        return

    def update_characters():
        for person in all_people_in_the_game(unique_characters()):
            update_special_personalities(person)
            create_party_schedule(person)
        return

    def make_character_unique(person, home_hub):
        '''
        Unique people need a fixed home hub since they are handled differently
        '''
        if person.is_unique:
            return False

        home_hub.people.append(person)
        person.type = "story"
        return True

    def update_main_character_actions():
        if "main_character_actions_list" in globals():
            for action in main_character_actions_list:
                mc.main_character_actions.add_action(action)
        return

    def generate_random_mothers_and_daughters():
        for person in (x for x in all_people_in_the_game(excluded_people = unique_characters()) if x.age > 35 or x.age < 25):
            if renpy.random.randint(0, 1) == 1:
                if person.age > 35:
                    for count in range(0, renpy.random.randint(1, 3)):
                        person.generate_daughter(True)
                else:
                    person.generate_mother(True)

    def generate_random_studying_daughters():
        count = 0
        for person in (x for x in all_people_in_the_game(excluded_people = unique_characters()) if x.age > 35 and x.kids == 0):
            if count >= 3:
                break
            if renpy.random.randint(0, 1) == 1:
                daughter = person.generate_daughter(True, job = student_job)
                count += 1

        # make sure we have at least 3 students that are not story characters
        count = sum(1 for x in all_people_in_the_game(excluded_people = unique_characters()) if x.has_job(student_job))
        while count < 3:
            person = make_person(job = student_job)
            person.generate_home().add_person(person)
            count += 1

    def generate_random_sisters_cousins_nieces():
        mothers = (x for x in all_people_in_the_game(excluded_people = unique_characters()) if town_relationships.get_existing_child_count(x) > 0)
        linked_mothers = []

        def get_new_mother_from_list():
            available_mothers = [x for x in mothers if x not in linked_mothers]
            if not available_mothers:
                return None
            mother = renpy.random.choice(available_mothers)
            linked_mothers.append(mother)
            return mother

        for i in range(4):
            mother = get_new_mother_from_list()
            other_mother = get_new_mother_from_list()

            if not mother or not other_mother:
                break

            town_relationships.update_relationship(mother, other_mother, "Sister")
            if mother.age < 45 and other_mother.age < 45:
                if mother.age >= other_mother.age:
                    mother.generate_mother()
                else:
                    other_mother.generate_mother()

            grand_mother = town_relationships.get_existing_mother(mother)
            if grand_mother:
                grand_mother.kids = town_relationships.get_existing_child_count(grand_mother)

            for cousin in town_relationships.get_existing_children(mother):
                town_relationships.update_relationship(other_mother, cousin, "Niece", "Aunt")
                if grand_mother:
                    town_relationships.update_relationship(grand_mother, cousin, "Granddaughter", "Grandmother")
                for other_cousin in town_relationships.get_existing_children(other_mother):
                    town_relationships.update_relationship(cousin, other_cousin, "Cousin")
                    town_relationships.update_relationship(mother, other_cousin, "Niece", "Aunt")
                    if grand_mother:
                        town_relationships.update_relationship(grand_mother, other_cousin, "Granddaughter", "Grandmother")
        return

    def generate_random_sisters():
        linked_sisters = []

        def get_new_sister_from_list():
            no_family = [x for x in all_people_in_the_game(excluded_people = unique_characters()) if x.age < 30 and len(town_relationships.get_relationship_type_list(x, types = RelationshipArray.RELATIONSHIP_FAMILY)) == 0]
            available_sisters = [x for x in no_family if x not in linked_sisters]
            if not available_sisters:
                return None
            sister = renpy.random.choice(no_family)
            linked_sisters.append(sister)
            return sister

        def update_sister_relationship(sister, other_sister):
            town_relationships.update_relationship(sister, other_sister, "Sister")
            # when not married, their last names should be identical
            if other_sister.relationship != "Married" and sister.relationship != "Married":
                other_sister.last_name = sister.last_name

        for i in range(4):
            sister = get_new_sister_from_list()
            other_sister = get_new_sister_from_list()

            if not sister or not other_sister:
                break

            update_sister_relationship(sister, other_sister)

        return

    def get_low_energy_sex_response_vaginal():
        responses = [
            "[the_person.possessive_title!c] moans and her vagina contracts as you keep pounding her pussy.",
            "[the_person.possessive_title!c] groans while you keep pounding her pussy.",
            "[the_person.possessive_title!c] moans and pushes back a little while you keep fucking her.",
            "[the_person.possessive_title!c] moans and wiggles as you keep slamming your dick inside her.",
            "[the_person.possessive_title!c] groans and wriggles while you keep pounding her wet pussy.",
            "[the_person.possessive_title!c] moans and gasps unable to speak while you slam your hard cock deep inside her.",
        ]
        return renpy.random.choice(responses)

    def get_low_energy_sex_response_anal():
        responses = [
            "[the_person.possessive_title!c] moans, while you feel her bowels milk your cock.",
            "[the_person.possessive_title!c] groans and sighs, while you keep pounding her bowels.",
            "[the_person.possessive_title!c] moans and pushes back a little while you keep slamming your cock into her slutty ass.",
            "[the_person.possessive_title!c] moans and keeps pushing back while as you keep slamming your cock inside her ass.",
            "[the_person.possessive_title!c] groans and wriggles while you keep pounding her tightening buttocks.",
            "[the_person.possessive_title!c] moans and gasps unable to speak while you slam your hard cock deep inside her spasming ass.",
        ]
        return renpy.random.choice(responses)

label activate_generic_personality(stack):
    python:
        for i in builtins.range(2):
            create_bimbo()

        # create two random people with the alpha personality (they have a very low chance of being created at random)
        for i in builtins.range(3):
            create_alpha_personality()

        # add two random hookers to the game (on start of game)
        for i in builtins.range(3):
            create_hooker()

        update_main_character_actions()

        generate_random_mothers_and_daughters()

        generate_random_sisters_cousins_nieces()

        generate_random_sisters()

        generate_random_studying_daughters()

        create_old_hooker_with_daughter()

        # special routine for nurses, they have an alterating pattern with one day off between rotatations
        clear_alternating_days(nurse_job)
        clear_alternating_days(night_nurse_job)

        # final routine to create initial party schedules and set special personalities
        update_characters()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    python:
        update_main_character_actions()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label low_energy_sex_responses_vaginal(the_person):
    $ play_moan_sound()
    $ title_choice = get_low_energy_sex_response_vaginal()
    "[title_choice!i]"
    return

label low_energy_sex_responses_anal(the_person):
    $ play_moan_sound()
    $ title_choice = get_low_energy_sex_response_anal()
    "[title_choice!i]"
    return
