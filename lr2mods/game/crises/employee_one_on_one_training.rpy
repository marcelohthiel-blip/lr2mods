#####################################  Scene Idea  ##############################################
# Scene: One one One Training
#        Pick a random (obedient? intelligent? Probably not bimbo) employee during business hours. Verify they have at least one work skill lower than MC
#        Give MC the option to train the NPC in the skill for a random (small) increase
#        ***Optional:
#        If NPC is slutty (>60?), check and see if MC has sex skill greater than NPC
#        If yes, have NPC ask if MC will train her in sex skill
#        Check if MC has energy. If yes give MC option to train in sex skill
#        If yes, trigger sex skill training scene.
#
#        Future options: Other benefits for NPCs having high sex skills
#
################################################################################################
label SB_one_on_one_label():
    $ the_person = get_training_employee()
    if the_person is None: # "No one eligible for training!"
        return

    $ old_location = mc.location
    $ mc.change_location(break_room)

    "You take a quick break from work to go get a quick snack from the vending machine. While you are trying to decide what snack to buy, [the_person.possessive_title] enters the break room."
    $ the_person.draw_person()
    the_person "Oh, hey [the_person.mc_title]!"
    "You keep chatting with [the_person.possessive_title] for a while. Eventually, the subject of your role in the company and the various jobs you fulfil around the lab comes up."
    the_person "Yeah, I've heard that you are pretty skilled at some of the different jobs in the lab here. I was wondering if maybe you could give me some pointers?"
    "You consider [the_person.possessive_title]'s request for a moment, taking into account her personal ambitions and skill level."
    $ topic = None
    $ attribute_name = None
    menu:
        "Train HR" if the_person.hr_skill < mc.hr_skill and the_person.opinion.hr_work > -2:
            "You explain to [the_person.possessive_title] the ins and outs of HR work. You do it in pretty broad terms, but touch on all the important parts."
            $ topic = "HR work"
            $ attribute_name = "hr_skill"

        "Train Supply" if the_person.supply_skill < mc.supply_skill and the_person.opinion.supply_work > -2:
            "You do some hands-on training with [the_person.possessive_title], showing her various methods for securing the different chemicals required for serum production."
            $ topic = "supply work"
            $ attribute_name = "supply_skill"

        "Train Marketing" if the_person.market_skill < mc.market_skill and the_person.opinion.marketing_work > -2:
            "You spend some time with [the_person.possessive_title], giving all kinds of advice on the art of the sale. It's not just about good deals, but making people understand they need the product you offer."
            $ topic = "marketing work"
            $ attribute_name = "market_skill"

        "Train Research" if the_person.research_skill < mc.research_skill and the_person.opinion.research_work > -2:
            "You talk with [the_person.possessive_title] about various chemicals and scientific methods, and how they apply to different portions of the brain."
            $ topic = "research work"
            $ attribute_name = "research_skill"

        "Train Production" if the_person.production_skill < mc.production_skill and the_person.opinion.production_work > -2:
            "You share some insights with [the_person.possessive_title] about the chemical processes and reactions between common serum elements."
            $ topic = "production work"
            $ attribute_name = "production_skill"

        "Too Busy":
            "You apologise. You are just too busy to offer one–on–one training right now."

    if not topic:
        the_person "That's okay, [the_person.mc_title], I understand. Maybe another time then!"
    elif the_person.opinion(topic) < 0:
        if the_person.discover_opinion(topic):
            "As you talk you catch glimmers of what could be disgust cross her face. It seems like [topic] might have been the thing to discuss with [the_person.title]."
        else:
            "As you get further into the details you recall that [the_person.title] doesn't really like [topic]."
        "Since it is too late to start over you shift focus, talking up the positive and enjoyable parts of the job."
        if renpy.random.randint(0, 100) < mc.charisma * 5: # about 50% max success rate
            "Surprisingly it seems to work and [the_person.title] starts to nod along as you finish talking."
            $ the_person.increase_opinion_score(topic)
            the_person "You know, when you say it that way, maybe it wouldn't be so bad to do that every day."
        else:
            "Unfortunately she doesn't seem to be moved by your words."
            the_person "Sorry, I just don't think I would ever be happy doing [topic]."
    else:
        "By the end of the training session, [the_person.title] seems to have learned a lot about [topic]."
        $ one_on_one_update_skill(the_person, attribute_name, topic)
        the_person "Thanks for the help, [the_person.mc_title]. I'm sure that will come in handy during work around here!"
        $ one_on_one_training_check_perks(attribute_name)

    $ mc.change_location(old_location)
    $ old_location = None
    $ attribute_name = None
    $ topic = None
    $ clear_scene()
    return
