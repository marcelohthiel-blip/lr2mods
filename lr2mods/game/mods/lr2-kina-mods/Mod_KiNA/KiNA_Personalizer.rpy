#Counter = KP01
# This set of labels for personalize event

init 5 python:
#making it a habit to init hijank label lower priority
 
    config.label_overrides["pregnant_finish_announce"] = "personalize_pregnant_finish_announce"

label personalize_pregnant_finish_announce(the_person): #TODO: have more variants for girlfriend_role, affair_role, etc.
    # The girl tells you she'll need a few days to have the kid and recover, and she'll be back in a few days.
    if get_named_label("pregnant_finish_announce", the_person):
        $ run_named_label("pregnant_finish_announce", the_person)
        return

    $ play_ring_sound()
    "You get a call from [the_person.possessive_title]. You answer it."
    mc.name "Hey [the_person.title], what's up?"

    if the_person.is_employee:
        the_person "Hi [the_person.mc_title]. I wanted to let you to know that I won't be at work for a few days."
    else:
        the_person "Hi [the_person.mc_title], I have some exciting news."

    the_person "I saw my doctor yesterday and he tells me I'm going to pop any day now."

    if day - the_person.event_triggers_dict.get("preg_start_date", day) <= 90: #It's unusually short
        the_person "It's earlier than I expected, but he tells me everything looks like it's perfectly normal."

    mc.name "That's amazing news. Do you need me to do anything?"
    the_person "No, I know you're very busy. You just focus on work and I'll focus on this. I know you'll be there for me in spirit."
    mc.name "Okay, I'll talk to you soon then."
    the_person "I'll let you know as soon as things are finished. Bye!"

    $ pregnant_finish_announce_person(the_person)
    return
