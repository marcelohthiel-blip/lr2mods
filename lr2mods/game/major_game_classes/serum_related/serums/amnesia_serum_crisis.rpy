label amnesia_girl_crisis_label(the_person):
    if the_person.is_family:
        "As you walk around the house, you see [the_person.title] standing around with a pensive look on her face, as if trying to remember something important."
    elif the_person.is_employee:
        "As you walk around the office, you see [the_person.title] standing at her desk with a pensive look on her face, as if trying to remember something important."
    elif the_person.is_strip_club_employee:
        "As you walk around the club, you see [the_person.title] standing around with a pensive look on her face, as if trying to remember something important."
    else:
        "While walking around, you see [the_person.title] standing around with a pensive look on her face, as if trying to remember something important."

    $ the_person.draw_person()
    mc.name "[the_person.title], are you alright?"
    the_person "I wouldn't say that... Not really."
    mc.name "Tell me, what's the matter? Is there anything I can do to help?"
    the_person "Lately I've been haunted by strange memory lapses. I've even started making notes on my phone."
    the_person "It wouldn't be so strange, but some things I suddenly remember, though I didn't remember them before, as if they didn't exist at all..."
    "[the_person.possessive_title!c] shows you her smartphone."
    the_person "See, right here I wrote that I don't remember anything about what happened that day, when in fact I remember everything else perfectly well."
    the_person "And I have absolutely no recollection of what happened that day."
    "You listen to her with a satisfied grin. The serum is working!"
    "However, you suddenly realise the full meaning of what she said, and you begin to let her words pass you by."
    "... You don't understand what's going on. The serum was supposed to erase all her memories, but they're suddenly coming back?!"
    "Cold sweat breaks out on your forehead."
    "Shit! I could get myself into a lot of trouble!"
    "What's this! What's going on? Will all the serum with this property not work?!"
    "But just as suddenly you remember that she could .... no, she took another dose of the serum with the same effect! It's something you need to work on, and you can't stop thinking about it."
    "You suddenly guess that taking a new dose of this serum when the same serum has been in effect for some time would restore in the girl's memory the events that occurred between serum doses instead of continuing its effect!"
    mc.name "[the_person.title], you know, I don't think there's anything wrong with you. It's probably just stress. You need to calm down, everything's gonna be okay."
    "You smile as warmly and sincerely as you can, making a deeply reassuring face:"
    mc.name "[the_person.title], you'll be fine, but you've reminded me of something important I'd forgotten. Thank you!"
    the_person "Thank you! But..."
    $ clear_scene()
    if mc.is_at(mc.business.r_div):
        "You cut yourself off from the world around you and go to work."
    else:
        "You quickly head to your research lab, never giving [the_person.possessive_title] a chance to finish her sentence."
        $ mc.change_location(mc.business.r_div)

    "After working for a few hours, you were able to modify the molecular structure of the serum to prevent future mishaps."
    $ mc.business.event_triggers_dict["enhanced_selective_amnesia"] = True
    $ mc.business.event_triggers_dict.pop("trigger_amnesia_event", None)
    $ mc.log_event("Selective Amnesia will no longer cause memory problems", "float_text_grey")
    call advance_time(no_events = True) from _call_advance_time_amnesia_girl_crisis
    return

label amnesia_trait_crisis_label():
    "While going over the reports of the R&D team you notice something strange."
    if mc.is_at_office and mc.business.active_research_design and mc.business.active_research_design == find_serum_trait_by_name("Selective Amnesia"):
        "The amnesia-inducing trait you are currently researching has an unexpected side effect."
    else:
        "There might be a problem with the amnesia-inducing trait in a serum that never came up while studying the initial research reports."
    "Cold sweat breaks out on your forehead."
    mc.name "Shit! I could get myself into a lot of trouble if I hadn't discovered this now!"
    "You realised that taking a new dose of this serum while the same serum has been in effect for some time will partially restore the persons memory instead of continuing its effect!"
    if mc.is_at(mc.business.r_div) and mc.business.active_research_design and mc.business.active_research_design == find_serum_trait_by_name("Selective Amnesia"):
        "Luckily, your experience with this serum has already given you a ready-made solution. You quickly make some changes to the structure of the molecule that negates the unintended side effect."
    else:
        $ mc.change_location(mc.business.r_div)
        "You quickly make your way to your research lab to make some changes to the serums molecular structure, to prevent the unintended side effect."

    $ mc.business.event_triggers_dict["enhanced_selective_amnesia"] = True
    $ mc.log_event("Selective Amnesia will no longer cause memory problems", "float_text_grey")
    call advance_time(no_events = True) from _call_advance_time_amnesia_trait_crisis
    return
