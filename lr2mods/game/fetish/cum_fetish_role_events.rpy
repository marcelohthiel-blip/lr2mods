label cum_fetish_get_dosage_label(the_person):
    mc.name "[the_person.title], get on your knees. It's time for your dosage of cum."
    "[the_person.possessive_title!c] smiles wide."
    the_person "Oh!? Yes! It's my favourite!"
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title!c] immediately drops to her knees. She doesn't even seem to care that there could be other people around."
    $ the_person.draw_person(position = "blowjob")
    # call fuck_person(the_person, private = False, start_position = cum_fetish_blowjob, start_object = make_floor(), girl_in_charge = True, position_locked = True) from _call_fuck_person_SBR30
    call get_fucked(the_person, private = mc.location.is_private, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = False, allow_continue = False) from _call_get_fucked_cum_fetish_get_dosage
    return

label cum_fetish_post_sex_cleanup_label(the_person_one, the_person_two):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person_one)
    $ scene_manager.add_actor(the_person_two, display_transform = character_center_flipped)
    "When you finish with [the_person_one.possessive_title], you notice that [the_person_two.title] is watching you intently."
    the_person_two "You done? Does [the_person_one.fname] need some help... cleaning up?"
    mc.name "Go for it."
    the_person_two "Yes! Thank you!"
    if the_person_one.outfit.has_ass_cum or the_person_one.outfit.has_creampie_cum:
        $ scene_manager.update_actor(the_person_two, display_transform = character_right_flipped, position = "kneeling1")
    else:
        $ scene_manager.update_actor(the_person_two, display_transform = character_right_flipped, position = "walking_away")

    return
