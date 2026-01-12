# Labels
label clone_recall_label(the_person):
    "You order [the_person.title] back to [clone_facility.formal_name]."

    $ the_person.change_location(clone_facility)

    the_person "Okay, [the_person.mc_title]. I'll head there next."
    return

label clone_rent_apartment_label(the_person):
    $ the_person.draw_person()
    mc.name "Listen, [the_person.fname], you are very dear to me and I have decided that you are mature enough to live on your own."
    mc.name "So I am willing to rent you a place where you can live by yourself."
    the_person "Please [the_person.mc_title], I love being with you, do I really have to go?"
    menu:
        "Let her stay":
            mc.name "Do you really want to live here, in this facility?"
            the_person "Yes, [the_person.mc_title], please let me stay..."
            mc.name "Ok, if that is what you want."
            return
        "Rent the apartment":
            mc.name "I think it's better for your development if you have your own place. Trust me."
            the_person "Ok [the_person.mc_title], if you think that is best, I will honour your wish."

            python:
                the_person.generate_home(force_new_home = True)
                mc.business.change_funds(-25000, stat = "Real Estate")
                the_person.set_schedule(None, time_slots = [1, 2, 3])

            "You make all the necessary arrangements, your clone [the_person.fname] will now stay at the new apartment and start living her own life."

    $ clear_scene()
    return
