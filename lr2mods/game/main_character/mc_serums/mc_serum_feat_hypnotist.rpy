#The very first Mc serum trait. Regenerates extra energy for the MC every turn.
init 5 python:
    def hypnotize_in_convo_requirement(person):
        if not mc_serum_feat_hypnotist.is_active:
            return False
        if mc.energy < 30:
            return "Requires: {energy=30}"
        if the_person.is_in_trance:
            return "Already in Trance"
        return True

    chat_actions.append(
        Action("Hypnotize her {energy=-30}\n Serum: Hypnotism",
        hypnotize_in_convo_requirement,
        "hypnotize_in_convo_label",
        menu_tooltip = "You can utilize your feat of hypnosis serum to put her into a trance.")
        )

label perk_feat_hypnotist_upg_label(the_person):
    the_person "Research with the Permanent Bimbofication serum trait has yielded some significant gains in inducing temporary trances."
    the_person "By stripping out some of the compounds making bimbofication permanent, it makes it easier to subdue a target using hypnosis."
    mc.name "That sounds very useful. I'll give it a try when I have the chance."
    return

label hypnotize_in_sex_label(the_person, the_position):
    mc.name "Hey, look at me for a second."
    if the_position.position_tag == "doggy" or the_position.position_tag == "standing_doggy":
        "[the_person.title] looks back at you."
    elif the_position.position_tag == "blowjob":
        "[the_person.title] looks up at you."
    else:
        "[the_person.title] looks at you."
    "Using your hypnosis ability, you quickly hypnotize her into a trance."
    $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    if mc_serum_feat_hypnotist.trait_tier > 1:
        "[the_person.possessive_title!c]'s eyes quickly go blank as she starts to go under."
        "With the power of your hypnosis serum, you push her into a deeper trance."
        $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
        if mc_serum_feat_hypnotist.trait_tier > 2:
            "Your eyes focus on [the_person.title]'s, while her pupils dilate as she slips farther into your hypnosis."
            "Your ability has driven her even deeper."
            $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    "With her now in a trance, you can continue [the_position.verbing] her."
    $ mc.change_energy(-30)
    return

label hypnotize_in_convo_label(the_person):
    mc.name "Hey, can I have your attention for a moment?"
    the_person "Sure [the_person.mc_title], what is it?"
    "Using your hypnosis ability, you quickly hypnotize her into a trance."
    $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    if mc_serum_feat_hypnotist.trait_tier > 1:
        "[the_person.possessive_title!c]'s eyes quickly go blank as she starts to go under."
        "With the power of your hypnosis serum, you push her into a deeper trance."
        $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
        if mc_serum_feat_hypnotist.trait_tier > 2:
            "Your eyes focus on [the_person.title]'s, while her pupils dilate as she slips farther into your hypnosis."
            "Your ability has driven her even deeper."
            $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    "With her now in a trance, you consider if there was anything else you needed from [the_person.title]."
    $ mc.change_energy(-30)
    return
