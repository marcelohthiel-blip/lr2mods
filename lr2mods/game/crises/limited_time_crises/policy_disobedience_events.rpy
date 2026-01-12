## This file contains events that are triggered by employees not being slutty/obedient enough for certain policies
# These are generally Limited Time Events, usually available only for a single turn, and triggered when you either walk into the room
# or when you talk to the person.
label uniform_disobedience_event(planned_uniform, the_person):
    $ scene_manager = Scene()
    "As you walk up to [the_person.title] you notice that she isn't wearing her company uniform."
    $ scene_manager.add_actor(the_person)

    if the_person.obedience < 110:
        $ the_person.call_dialogue("greetings")
    else:
        "[the_person.possessive_title!c] seems nervous when she notices you approaching."
    mc.name "Is there some reason you're out of your uniform [the_person.title]?"

    if the_person.effective_sluttiness() >= planned_uniform.outfit_slut_score: #Just disobedient
        $ random_excuse = renpy.random.randint(0,2) #Get a random excuse for why she's not wearing her uniform. #TODO: Base this on her obedience/sluttiness. Personality maybe?
        if random_excuse == 0:
            the_person "I'm sorry, I just had to step out for a moment to pick something up. I was assuming that wouldn't be a problem."
        elif random_excuse == 1:
            the_person "It's so impractical, I couldn't get anything done. I'm going to wear this for a few hours and get some real work done."
        else: # random_excuse == 2:
            the_person "That uniform policy is just a suggestion, right? There's no way you expect us to actually wear it all the time."

    elif planned_uniform.vagina_visible:
        if the_person.obedience < 120:
            the_person "I just can't wear it [the_person.mc_title], it's ridiculous!"
            the_person "It doesn't cover anything, and makes me feel like a cheap prostitute while I'm working."
            the_person "I don't know how it's even legal to require us to wear it!"
        else:
            the_person "I'm sorry [the_person.mc_title]. It just provides so little coverage, I didn't think you'd notice..."
            the_person "If we could have some variations with some underwear, I'd be a lot more comfortable in uniform."

    elif planned_uniform.tits_visible:
        if the_person.obedience < 120:
            the_person "I just can't wear it [the_person.mc_title], it's demeaning!"
            the_person "If I wear your uniform I would have my tits out, all day long! How am I supposed to focus like that?"
        else:
            the_person "I'm sorry [the_person.mc_title], I know I should be wearing it, but..."
            the_person "It's just so revealing! If I could wear a bra, or anything, to keep me a little covered I would be more comfortable."
    elif planned_uniform.underwear_visible:
        if the_person.obedience < 120:
            the_person "Do you really expect us to wear that uniform all the time? I would be half-naked, all day!"
            the_person "It's demeaning, I feel like I'm just here for men to leer at."
        else:
            the_person "I'm sorry [the_person.mc_title]! I was feeling embarrassed about standing around in my underwear."
            the_person "Maybe we could have a uniform with some more coverage? Just a little would go a long way!"
    else:
        if the_person.obedience < 120:
            the_person "Do we really have to wear that uniform all day? It's so... revealing, it's just embarrassing to be in."
        else:
            the_person "I'm sorry [the_person.mc_title]!"
            the_person "It's nothing like what I would normally wear, I'm kind of embarrassed to be in it."


    $ the_person.add_infraction(Infraction.out_of_uniform_factory())
    mc.name "The uniform policy isn't a suggestion [the_person.title], it's a requirement for continued employment."
    menu:
        "Send her to get changed":
            mc.name "Go get your uniform and get changed."
            if the_person.obedience < 90:
                "[the_person.possessive_title!c] sighs and rolls her eyes."
                the_person "Fine, I'll go put it on."
            else:
                the_person "Right away [the_person.mc_title]."
            $ scene_manager.hide_actor(the_person)
            "She hurries out of the room. You wait by her desk until she comes back."
            $ the_person.current_planned_outfit = planned_uniform
            $ scene_manager.show_actor(the_person)
            "A few moments later [the_person.possessive_title] comes back, now properly in uniform."


        "Have her change right here" if reduced_coverage_uniform_policy.is_active:
            mc.name "Do you have your uniform with you?"
            the_person "I have it in my desk."
            mc.name "Good. Get it and get changed."
            "She nods and slides open one of her desk drawers, grabbing her uniform and tucking it under her arm."
            the_person "I'll be back in a moment..."
            mc.name "No, you're going to get changed here. I obviously need to make sure you're wearing it properly."
            if the_person.effective_sluttiness(["bare_pussy", "bare_tits"]) > 40: #No big deal.
                the_person "Fine, I guess it doesn't really matter."

            else: #Shy about it
                the_person "You don't really mean that, do you? Right here?"
                mc.name "Do I need to write you up for insubordination too?"
                the_person "No, I'll do it..."
                $ the_person.change_obedience(1 + the_person.opinion.being_submissive)

            $ scene_manager.strip_full_outfit(the_person, strip_feet = True)
            $ mc.change_locked_clarity(10)
            $ the_watcher = get_random_from_list([x for x in the_person.location.people if x != the_person])
            if the_watcher:
                $ scene_manager.add_actor(the_watcher, display_transform = character_left_flipped)
                "[the_watcher.possessive_title!c] has been watching the entire scene."
                if the_watcher.sluttiness > 40:
                    the_watcher "Looking good, [the_person.fname]."
                else:
                    the_watcher "Oh, right here, in front of everyone."

            "Reluctantly [the_person.possessive_title] puts on her uniform."
            $ the_person.current_planned_outfit = planned_uniform
            $ scene_manager.show_dress_sequence(the_person, planned_uniform)

            if the_watcher:
                $ scene_manager.remove_actor(the_watcher)
                "After [the_person.possessive_title] got dressed, [the_watcher.fname] returns to her job."

        "Have her change right here\n{menu_red}Requires policy: [reduced_coverage_uniform_policy.name]{/menu_red} (disabled)" if not reduced_coverage_uniform_policy.is_active:
            pass

        "Let her stay out of uniform":
            mc.name "But, just this once, I'll make an exception. I expect you in uniform for your next shift."
            the_person "Thank you [the_person.mc_title], the break is appreciated."

            $ the_person.change_stats(happiness = 10, love = 1, obedience = -2)

    the_person "Is there something you needed to talk to me about?"
    $ scene_manager.clear_scene()
    call talk_person(the_person) from _call_talk_person_18
    return
