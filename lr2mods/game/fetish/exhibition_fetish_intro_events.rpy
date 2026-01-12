# Fetish Labels
label exhibition_fetish_employee_intro_label(the_person):
    return False

label exhibition_fetish_family_intro_label(the_person):
    return False

label exhibition_fetish_generic_intro_label(the_person):
    return False

label exhibition_fetish_mom_intro_label():
    return False

label exhibition_fetish_lily_intro_label():
    return False

label exhibition_fetish_rebecca_intro_label():
    return False

label exhibition_fetish_gabrielle_intro_label():
    return False

label exhibition_fetish_stephanie_intro_label():
    return False

label exhibition_fetish_alex_intro_label():
    return False

label exhibition_fetish_nora_intro_label():
    return False

label exhibition_fetish_emily_intro_label():
    return False

label exhibition_fetish_christina_intro_label():
    return False

label exhibition_fetish_starbuck_intro_label():
    return False

label exhibition_fetish_sarah_intro_label():
    $ the_person = sarah
    $ scene_manager = Scene()
    $ other_people = mc.business.employees_at_office
    $ other_people.remove(sarah)
    $ other_person = get_random_from_list(other_people)
    "It's another Wednesday morning. The girls are starting to arrive for work and getting set up for the day."
    "You always enjoy when the girls get there in the morning. You check out some of their outfits, not so subtly, as they arrive."
    $ mc.change_locked_clarity(20)
    "You are just starting to think about calling one to the office for a quickie when someone interrupts your thoughts..."
    the_person "Ahem..."
    $ scene_manager.add_actor(the_person)
    mc.name "Ah, good morning [the_person.title]."
    the_person "Good morning. I umm, noticed you were checking out some of the employees..."
    mc.name "Ah, yes I was."
    the_person "I try to take care of your urges for you at the Monday meetings..."
    mc.name "Well, maybe..."
    the_person "Do you need me to take care of you again? I know it's hump day... I could do it right here?"
    "You look around. Several girls have already sat down at their desks and begun their work."
    "You look back at [the_person.possessive_title]. Is she blushing?"
    "You've been testing Social Sexual Proclivity Nanobots quite a bit on her lately. Is she doing this {i}because{/i} all the other girls are here?"
    "You reply to her in a voice that is louder than necessary, making sure all the girls around you hear it."
    mc.name "Yes [the_person.title]. Why don't you get on your knees and take care of it for me."
    $ the_person.change_happiness(3)
    the_person "Yes sir!"
    $ scene_manager.update_actor(the_person, position = "blowjob", display_transform = character_center)
    $ the_person.change_arousal(10)
    "[the_person.possessive_title!c] gleefully gets down on her knees and pulls down your zipper. After pulling your cock out, she smiles up at you, then licks the tip."
    "You can hear murmurs from some of the girls around you, but it doesn't seem to phase her. If anything, she seems to be emboldened..."
    $ the_person.change_happiness(3)
    $ play_blowjob_sound()
    "[the_person.title] eagerly opens up and starts sucking you off, right here in the entryway."
    $ mc.change_locked_clarity(30, True, sarah)
    $ mc.change_arousal(15)
    "You let out a moan. Having [the_person.possessive_title] service you like this, right here in front of everyone is really turning you on."
    "One of your employees walks in the door."
    $ scene_manager.add_actor(other_person, display_transform = character_right)
    "She stops when she sees [the_person.title] on her knees, sucking you off."
    "[the_person.possessive_title!c] senses that someone is watching."
    if the_person.tits_available and the_person.tits_visible:
        "With one hand she starts to play with one of her breasts, and the other hand goes down between her legs..."
    else:
        "She quickly pulls her tits out."
        $ scene_manager.strip_to_tits(the_person)
        "Once exposed, she starts to play with one of her breasts with one hand, and the other goes down between her legs..."
    $ the_person.change_arousal(20)
    $ play_moan_sound()
    "[the_person.title] moans with her mouth full of your cock as she starts to play with herself."
    $ mc.change_locked_clarity(30, True, sarah)
    if other_person.sluttiness < 20:    #Uptight response
        other_person "Holy shit... what have I gotten myself into, taking the job here..."
    elif other_person.sluttiness < 60:    #Excited
        other_person "Wow! Way to go [the_person.fname]."
    else:
        other_person "Damn! I was hoping to get some action today but it looks like [the_person.fname] beat me to it..."
    $ scene_manager.remove_actor(other_person)
    $ other_people.remove(other_person)
    $ other_person = get_random_from_list(other_people)
    "[other_person.possessive_title!c] walks past you two, murmuring to herself."
    $ mc.change_arousal(20)
    "Instead of being embarassed, having someone walk by seems to have made [the_person.title] even more aroused."
    "You put your hand on the back of her head and she looks up at, smiling as she pulls off for a moment."
    the_person "Your cock tastes so good! Use my mouth however you want!"
    "She says it louder than is necessary considering she is on her knees in front of you."
    mc.name "Of course, if that is what you want."
    "You grab her by the back of her head and she opens her mouth. You guide her mouth back onto your cock and slowly push your cock down her throat."
    $ mc.change_locked_clarity(30, True, sarah)
    $ mc.change_arousal(20)
    $ the_person.change_arousal(20)
    $ play_gag_sound()
    "You start slowly but are soon fucking [the_person.title]'s face, right here in the lobby in front of everyone."
    "She moans in between gags as she throats you, every once in a while you give her a few moments to gasp for air."
    "One time after catching her breath she looks up at you."
    the_person "Will you cum all over my face? I want every other HR girl to see how a good leader takes care of her boss when I walk back to my desk!"
    $ mc.change_locked_clarity(30, True, sarah)
    $ mc.change_arousal(20)
    $ the_person.change_arousal(20)
    "Fuuuuuck. You've clearly made [the_person.possessive_title] into an exhibitionist."
    "You pretend to think about it for a moment. She senses your hesitation and speaks up, once again louder than necessary..."
    the_person "Please! Please [the_person.mc_title]! Cover my face with your wonderful cum so I can wear it proudly!"
    mc.name "Okay slut, I'll do what you want, this time at least."
    "Before she can respond, you take her by the hair and shove your cock back in her mouth and down her throat."
    $ play_gag_sound()
    $ mc.change_locked_clarity(30, True, sarah)
    $ mc.change_arousal(20)
    $ the_person.change_arousal(20)
    "This entire situation has you so turned on, you fuck [the_person.title]'s throat for a bit more, but you are rapidly approaching orgasm."
    mc.name "Oh fuck, that's it [the_person.title]. I'm gonna cover your face!"
    $ scene_manager.add_actor(other_person, display_transform = character_right)
    "Right as you pull [the_person.possessive_title]'s head back to cum, another employee walks in the entry door."
    "They stop when they see what is happening. You begin stroking yourself to finish and you point your cock at [the_person.title]'s face."
    other_person "Holy shit, is he really about to..."
    $ the_person.cum_on_face()
    $ scene_manager.update_actor(the_person, position = "blowjob", display_transform = character_center)
    $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
    "[other_person.possessive_title!c]'s words die off when explode, your cock spurting cum all over [the_person.title]'s face."
    $ the_person.change_arousal(40)
    "You see her hand between her legs, masturbating furiously, and [the_person.possessive_title] begins to cum too."
    $ the_person.have_orgasm()
    "[the_person.title]'s entire body is trembling as you paint her face with spurts of cum. She moans loudly through her orgasm."
    "When she finally recovers, she looks up at you and smiles."
    the_person "Th... Thank you sir..."
    mc.name "You're welcome. Now clean me off and then get back to work."
    the_person "Right!"
    "She quickly licks your cock, up and down. You hold out your hand you used to finish yourself off and she careful licks off a few drops of cum that dribbled down onto your fingers."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "Finished, she stands up, then carefully straightens her clothes, being careful to preserve your cum on her face as she gets dressed."
    $ the_person.apply_planned_outfit()
    $ the_person.outfit.add_face_cum()
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    $ mc.change_locked_clarity(10, True, sarah)
    "You feel your cock twitch for a moment when you look at [the_person.possessive_title]. Back in uniform but her face clearly plastered with your cum."
    the_person "Will that be all?"
    mc.name "Yes. Now get back to work."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ play_spank_sound()
    "When she turns to walk away, you give [the_person.title]'s ass a firm spank."
    $ the_person.change_arousal(5)
    "You look over at [other_person.title], who is still standing there in disbelief."
    $ scene_manager.remove_actor(the_person)
    "You carefully slide your cock back into your trousers and zip them up."
    mc.name "Sorry, if you are waiting your turn, it might be a few minutes before I can oblige you."
    other_person "What? I wasn't... Ah!"
    $ other_person.change_stats(slut = 3, max_slut = 60, arousal = 10)
    $ scene_manager.remove_actor(other_person)
    "She quickly rushes off."
    "Wow. [the_person.title] appears to have developed an exhibitionism kink!"
    "You should look for opportunities to fuck around with her in public and in front of other people to have more fun!"
    $ add_exhibition_fetish(sarah)
    return

label exhibition_fetish_ophelia_intro_label():
    return False

label exhibition_fetish_candace_intro_label():
    return False

label exhibition_fetish_dawn_intro_label():
    return False

label exhibition_fetish_erica_intro_label():
    return False

label exhibition_fetish_ashley_intro_label():
    return False

label unit_test_exhibition_fetish_intro():

    "Generic intros"
    $ debug_set_stats_for_exhibition_fetish_mins(mom)
    "Method: exhibition_fetish_family_intro_label"
    call exhibition_fetish_family_intro_label(mom) from _unit_test_exhibition_fetish_intro_01
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(starbuck)
    "Method: exhibition_fetish_generic_intro_label"
    call exhibition_fetish_generic_intro_label(starbuck) from _unit_test_exhibition_fetish_intro_02
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(stephanie)
    "Method: exhibition_fetish_employee_intro_label"
    call  exhibition_fetish_employee_intro_label(stephanie) from _unit_test_exhibition_fetish_intro_03
    $ mc.energy = mc.max_energy

    $ stephanie.remove_role(exhibition_fetish_role)
    $ mom.remove_role(exhibition_fetish_role)
    $ starbuck.remove_role(exhibition_fetish_role)

    "Unique intros"
    $ debug_set_stats_for_exhibition_fetish_mins(mom)
    "Method: exhibition_fetish_mom_intro_label"
    call exhibition_fetish_mom_intro_label() from _unit_test_exhibition_fetish_intro_04
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(lily)
    "Method: exhibition_fetish_lily_intro_label"
    call exhibition_fetish_lily_intro_label() from _unit_test_exhibition_fetish_intro_05
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(aunt)
    "Method: exhibition_fetish_rebecca_intro_label"
    call exhibition_fetish_rebecca_intro_label() from _unit_test_exhibition_fetish_intro_06
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(cousin)
    "Method: exhibition_fetish_gabrielle_intro_label"
    call exhibition_fetish_gabrielle_intro_label() from _unit_test_exhibition_fetish_intro_07
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(stephanie)
    "Method: exhibition_fetish_stephanie_intro_label"
    call exhibition_fetish_stephanie_intro_label() from _unit_test_exhibition_fetish_intro_08
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(alexia)
    "Method: exhibition_fetish_alex_intro_label"
    call exhibition_fetish_alex_intro_label() from _unit_test_exhibition_fetish_intro_09
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(nora)
    "Method: exhibition_fetish_nora_intro_label"
    call exhibition_fetish_nora_intro_label() from _unit_test_exhibition_fetish_intro_10
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(emily)
    "Method: exhibition_fetish_emily_intro_label"
    call exhibition_fetish_emily_intro_label() from _unit_test_exhibition_fetish_intro_11
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(christina)
    "Method: exhibition_fetish_christina_intro_label"
    call exhibition_fetish_christina_intro_label() from _unit_test_exhibition_fetish_intro_12
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(starbuck)
    "Method: exhibition_fetish_starbuck_intro_label"
    call exhibition_fetish_starbuck_intro_label() from _unit_test_exhibition_fetish_intro_13
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(sarah)
    "Method: exhibition_fetish_sarah_intro_label"
    call exhibition_fetish_sarah_intro_label() from _unit_test_exhibition_fetish_intro_14
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(salon_manager)
    "Method: exhibition_fetish_ophelia_intro_label"
    call exhibition_fetish_ophelia_intro_label() from _unit_test_exhibition_fetish_intro_15
    $ mc.energy = mc.max_energy

    $ create_debug_candace()
    $ debug_set_stats_for_exhibition_fetish_mins(candace)
    "Method: exhibition_fetish_candace_intro_label"
    call exhibition_fetish_candace_intro_label() from _unit_test_exhibition_fetish_intro_16
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(dawn)
    "Method: exhibition_fetish_dawn_intro_label"
    call exhibition_fetish_dawn_intro_label() from _unit_test_exhibition_fetish_intro_17
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(erica)
    "Method: exhibition_fetish_erica_intro_label"
    call exhibition_fetish_erica_intro_label() from _unit_test_exhibition_fetish_intro_18
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(ashley)
    "Method: exhibition_fetish_ashley_intro_label"
    call exhibition_fetish_ashley_intro_label() from _unit_test_exhibition_fetish_intro_19
    $ mc.energy = mc.max_energy

    return
