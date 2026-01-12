init -1 python:
    def wear_pajamas(self, sluttiness = None):
        if sluttiness is None:
            sluttiness = self.sluttiness
        pajamas = get_pajama_outfit(self, sluttiness = sluttiness)
        self.apply_outfit(pajamas)
        return

    def get_pajama_outfit(person, sluttiness = None):
        if sluttiness is None:
            sluttiness = person.sluttiness
        [main_colour, second_colour, third_colour] = random_colours(person, 3)
        main_colour[3] *= 1.0-(sluttiness/400.0)
        second_colour[3] *= 1.0-(sluttiness/300.0)
        pajamas = Outfit("Pajamas")
        bottom_list = []
        bottom_list.append(cotton_panties.get_copy())
        bottom_list.append(cute_panties.get_copy())
        if person.opinion.showing_her_ass > 0:
            bottom_list.append(thong.get_copy())
        bottom = get_random_from_list(bottom_list)
        bottom.colour = third_colour
        if hasattr(bottom, "supported_patterns") and bottom.supported_patterns and renpy.random.randint(1, 100) > 50:
            bottom.pattern = bottom.supported_patterns[renpy.random.choice(list(bottom.supported_patterns.keys()))]
            bottom.colour_pattern = WardrobeBuilder.get_color(person, bottom.colour)
        if sluttiness + person.opinion.not_wearing_underwear*5 < 45:
            pajamas.add_lower(bottom)
        elif sluttiness + person.opinion.not_wearing_anything*5 < 85:
            pajamas.add_lower(bottom)

        if sluttiness < 20 + Person.rank_tits(person.tits)*5 - person.opinion.not_wearing_underwear*5:
            pajamas.add_upper(sports_bra.get_copy(), third_colour)
        covered = False
        lower = None
        if sluttiness < 15 + person.opinion.pants*5:
            lower = leggings.get_copy()
            covered = True
        else:
            if sluttiness < 35 + person.opinion.pants*5:
                lower = booty_shorts.get_copy()
                covered = True
            if renpy.random.randint(1, 100) > 70 - sluttiness/5:
                socks = high_socks.get_copy()
                socks.colour = second_colour
                if hasattr(socks, "supported_patterns") and socks.supported_patterns and renpy.random.randint(1, 100) > 50:
                    socks.pattern = socks.supported_patterns[renpy.random.choice(list(socks.supported_patterns.keys()))]
                    socks.colour_pattern = WardrobeBuilder.get_color(person, socks.colour)
                pajamas.add_feet(socks)
        if lower:
            lower.colour = second_colour
            if hasattr(lower, "supported_patterns") and lower.supported_patterns and renpy.random.randint(1, 100) > 50:
                lower.pattern = lower.supported_patterns[renpy.random.choice(list(lower.supported_patterns.keys()))]
                lower.colour_pattern = WardrobeBuilder.get_color(person, lower.colour)
            pajamas.add_lower(lower)
        upper_list = []
        if covered:
            upper_list.append(long_tshirt.get_copy())
            if sluttiness > 10 - person.opinion.skimpy_outfits*5:
                upper_list.append(wrapped_blouse.get_copy())
                upper_list.append(long_sweater.get_copy())
            if sluttiness > 15 - person.opinion.skimpy_outfits*5:
                upper_list.append(sleeveless_top.get_copy())
                upper_list.append(camisole.get_copy())
                upper_list.append(tshirt.get_copy())
            if sluttiness > 20 - person.opinion.skimpy_outfits*5:
                upper_list.append(tanktop.get_copy())
                upper_list.append(sports_bra.get_copy())
        else:
            if sluttiness >= 25 - person.opinion.skimpy_outfits*5 and sluttiness < 45:
                upper_list.append(sweater_dress.get_copy())
                upper_list.append(long_tshirt.get_copy())
                upper_list.append(wrapped_blouse.get_copy())
            if sluttiness > 35 - person.opinion.skimpy_outfits*5 and sluttiness < 65:
                upper_list.append(long_sweater.get_copy())
                upper_list.append(sleeveless_top.get_copy())
            if sluttiness > 45 - person.opinion.skimpy_outfits*5 and sluttiness < 85:
                upper_list.append(camisole.get_copy())
                upper_list.append(tshirt.get_copy())
                upper_list.append(nightgown_dress.get_copy())
            if sluttiness > 55 - person.opinion.skimpy_outfits*5:
                upper_list.append(tanktop.get_copy())
                upper_list.append(sports_bra.get_copy())
                upper_list.append(teddy.get_copy())
        if sluttiness + person.opinion.not_wearing_anything*5 < 85:
            upper = get_random_from_list(upper_list)
            if upper:
                upper.colour = main_colour
                if hasattr(upper, "supported_patterns") and upper.supported_patterns and renpy.random.randint(1, 100) > 50:
                    upper.pattern = upper.supported_patterns[renpy.random.choice(list(upper.supported_patterns.keys()))]
                    upper.colour_pattern = WardrobeBuilder.get_color(person, upper.colour)
                pajamas.add_upper(upper)
                pajamas.add_dress(upper)
        return pajamas

init 0 python:
    def run_move_enhanced(org_func):
        def run_move_enhanced_wrapper(person):
            # run original function
            org_func(person)
            # run extension code
            if time_of_day > 3:
                if person.location == person.home:
                    wear_pajamas(person)
                if not aunt.event_triggers_dict.get("invited_for_drinks", False):
                    if aunt.location == hall:
                        wear_pajamas(aunt)
                    if cousin.location == lily_bedroom:
                        wear_pajamas(cousin)
            if person.location.name == "beach":
                person.apply_outfit(get_beach_outfit(person))
            return
        return run_move_enhanced_wrapper

    Person.run_move = run_move_enhanced(Person.run_move)

label pajama_test():
    call screen main_choice_display(build_menu_items([get_sorted_people_list(known_people_in_the_game(), "Pajama Test", "Back")]))
    $ person_choice = _return
    if person_choice != "Back":
        $ number = 1
        while number < 100:
            $ wear_pajamas(person_choice, sluttiness = number)
            $ person_choice.draw_person(emotion = "happy")
            $ outfit_slut = person_choice.outfit.outfit_slut_score
            "Current sluttiness = [number]. Outfit sluttiness = [outfit_slut]."
            $ number += 1
        $ del person_choice
    return
