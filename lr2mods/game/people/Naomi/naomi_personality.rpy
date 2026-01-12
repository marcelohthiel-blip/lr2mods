label Naomi_greetings(the_person):
    if the_person.is_at_work:
        the_person "Goodday Sir, is there anything I can do for you?"
    else:
        the_person "Hello [the_person.mc_title], how are you?"
    return
