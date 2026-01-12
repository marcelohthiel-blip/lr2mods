# Harem Role - girl is accepted into the harem and accepts that she is not the only love interest
# - requires Threesome and love higher than 80
# Things to Consider:
# - can make a harem, lovable, or slavable? currently its lovable as per default and most easiest to implement
# - knows of the others in your harem
# - can have girlfriend and affair roles - when suggested, they may become sole harem, or need to be slowly integrated
# - girlfriend roles - suggestion to complete, may take time to accept.
# - if affair role - similar to gf role, if they leave SO = harem, continues affair as harem but for the children
# - Harem_Mansion - eventually a place where they all can live together?
# - Dialogues can be done way better than the way I did them XD
init 1 python:
    def ask_harem_requirement(person):
        if person.love < 60:    # hide option until love >= 60
            return False
        if person.in_harem: # already in harem
            return False
        if mc.stats.harem == 0 and mc.stats.girlfriends < 2: # don't show harem option until we have more than 1 girlfriend
            return False
        if person.love < 80:
            return "Requires: 80 Love"
        if person.opinion.polyamory < 1:
            return "Requires: like polyamory"

        # extra person lock-outs (finish story line)

        if (person == alexia
            and (not mc.business.event_triggers_dict.get("has_expensive_camera", False) or not willing_to_threesome(myra, alexia))):
            return "Requires: finish story line"

        if (person == ashley
            and (ashley.progress.love_step < 3 or ashley.progress.lust_step < 2 or ashley.progress.obedience_step < 2)):
            return "Requires: finish story line"

        if (person == camila
            and (not camila.event_triggers_dict.get("formal_date", False) or not camila.event_triggers_dict.get("home_sex", False) or not camila.event_triggers_dict.get("obedience_titfuck", False))):
            return "Requires: finish story line"

        if (person == candace
            and (not candace.event_triggers_dict.get("clothes_shopping", 0) != 0 or not candace.event_triggers_dict.get("supply_discount", False))):
            return "Requires: finish story line"

        if (person == christina
            and (not christina.is_willing(kissing))):
            return "Requires: finish story line"

        if (person == ellie
            and (not ellie_has_given_blowjob())):
            return "Requires: finish story line"

        if (person == emily
            and (not emily.event_triggers_dict.get("tutor_enabled", False) or emily.event_triggers_dict.get("study_blowjob_level", 0) < 2)):
            return "Requires: finish story line"

        if (person == erica
            and (not erica.is_willing(against_wall) or erica_get_progress() < 4 or kaya_erica_teamup.get_stage() < 4 or not willing_to_threesome(kaya, erica))):
            return "Requires: finish story line"

        if (person == cousin
            and get_strip_club_foreclosed_stage() not in (-1, 5)):
            return "Requires: finish story line"

        # if (person == iris
        #     and ):
        #     return "Requires: finish story line"

        if (person == kaya
            and (kaya.progress.love_step < 8 or kaya.progress.lust_step < 3 or not willing_to_threesome(kaya, erica))):
            return "Requires: finish story line"

        if (person == myra
            and (not myra_has_been_sponsored() or not myra_is_expanding_business() or not willing_to_threesome(myra, alexia))):
            return "Requires: finish story line"

        if (person == naomi
            and (naomi.corruption_level < 2)):
            return "Requires: finish story line"

        # if (person == nora
        #     and ):
        #     return "Requires: finish story line"

        if (person == salon_manager
            and ophelia_get_pubic_style_state() > 1):
            return "Requires: finish story line"

        if (person == city_rep
            and (city_rep.event_triggers_dict.get("attention_times_visited", 0) < 3 or not city_rep.event_triggers_dict.get("discussed_topless_is_legal", False))):
            return "Requires: finish story line"

        if (person == aunt
            and (aunt.progress.lust_step < 3 or aunt.progress.obedience_step < 4)):
            return "Requires: finish story line"

        # if (person == sakari
        #     and ):
        #     return "Requires: finish story line"

        if (person == sarah
            and (not sarah_story_80_love_complete_func() or not sarah_story_80_lust_complete_func())):
            return "Requires: finish story line"

        if (person == starbuck
            and (starbuck.progress.love_step < 1 or starbuck.progress.lust_step < 3 or starbuck.progress.obedience_step < 3 or starbuck.event_triggers_dict.get("shop_progress_stage", 0) < 3)):
            return "Requires: finish story line"

        if (person == stephanie
            and (stephanie.progress.love_step < 2 or stephanie.progress.obedience_step < 3)):
            return "Requires: finish story line"

        if person.is_affair:
            return True

        #kept special girlfriend roles for future
        if person.has_role(sister_role) and person.event_triggers_dict.get("sister_girlfriend_waiting_for_blessing", False):
            return "Requires: Mom's approval"
        if person.has_role(mother_role) and person.event_triggers_dict.get("mom_girlfriend_waiting_for_blessing", False):
            return "Requires: Sister's approval"
        if not person.is_girlfriend:
            return "Requires: be your girlfriend"
        return True

    make_harem_action = Action("Ask her to join your harem", requirement = ask_harem_requirement, effect = "ask_to_join_harem_label",
        menu_tooltip = "Ask her to start an official, polyamorous relationship and be part of your Harem.", priority = 10)
    chat_actions.append(make_harem_action)

    def move_into_harem(person):
        # set up relationship between harem girls
        for harem_girl in (x for x in list_of_people if x.home == harem_mansion):
            if not town_relationships.get_relationship(person, harem_girl):
                town_relationships.begin_relationship(person, harem_girl)
                #print(f"Add relation between {person.name} and {harem_girl.name}")

        person.change_home_location(harem_mansion)

        if person == lily:
            lily.bedroom.visible = False
        elif person == mom:
            mom_bedroom.visible = False
            mc.business.remove_mandatory_crisis("mom_weekly_bills_label")
        elif person == aunt:
            aunt_bedroom.visible = False
        elif person == cousin:
            cousin_bedroom.visible = False

        if aunt.home == harem_mansion and cousin.home == harem_mansion:
            aunt_home_hub.visible = False

    def move_out_of_harem(person):
        # she is not happy and will reset her obedience to 100 and love to 10
        person.change_stats(love = -(person.love - 10), happiness = -40, obedience = 100 - person.obedience)
        # she loses her submissive trait (even resents it a little)
        person.set_opinion("being submissive", -1)
        # disappointed in polyamorous relationships
        person.set_opinion("polyamory", -1)
        person.remove_role(harem_role)
        person.remove_role(affair_role) # also ends affair if still present
        person.remove_role(girlfriend_role)

        if person.home != harem_mansion:
            return

        if person == lily:
            person.change_home_location(lily_bedroom)
            lily_bedroom.visible = True
        elif person == mom:
            person.change_home_location(mom_bedroom)
            mom_bedroom.visible =True

            add_mom_obedience_weekly_bills_action()
        elif person == aunt:
            person.change_home_location(aunt_bedroom)
            aunt_bedroom.visible = True
            aunt_home_hub.visible = True
        elif person == cousin:
            person.change_home_location(cousin_bedroom)
            cousin_bedroom.visible = True
            aunt_home_hub.visible = True
        else:
            other_person = get_random_from_list([x for x in town_relationships.get_family_members(person) if x.home != harem_mansion]) # find family member that doesn't live in harem
            if other_person:
                person.change_home_location(other_person.home)  # she moves in with family
            else:
                person.generate_home(force_new_home = True)  # she moves to a new apartment
            person.change_location(person.home)


    #Setting Harem Roles = Polyamory, Polyamorous relationship for more ideas refer to
    #https://affirmativecouch.com/polyamorous-relationship-structures/
    # Hierarchical Polyamory would be what everyone is familiar with as a Harem
    # mc viewed as the Primary, then rest would fall under the following
    # Dependant Polyamory - chooses to live with mc
    # Solo Polyamory - chooses to live separately
    # Polycules formed by individuals... so they might want only one-on-one with mc, but eventually threesome with another
    # - so you can make a relationship dependant on polycules = ie Emily will do threesome with mc and Sarah, but doesn't like others that way
    # - could use the relationship structure to define polycules between persons in the harem?
    # harem_role/cousin/aunt when they are girlfriend and added to the poly they get the generic girlfriend role, this is just to keep things tied up

label leave_harem_label(the_person):
    # Stop being in a relationship.
    mc.name "[the_person.title], can we talk?"
    if the_person.happiness > 100:
        the_person "Sure, what's up?"
    else:
        the_person "Oh no, that's never good."

    mc.name "There's no easy way to say this, so I'll just say it: It's not working out."
    $ the_person.draw_person(emotion = "sad")
    #TODO: Add a variant where you've passed below the girlfriend threshold and she feels the same way.
    "She seems to be in shock for a long moment, before slowly nodding her head."
    the_person "Okay... I don't know what to say."
    mc.name "I'm sorry, but it's just the way things are."

    $ move_out_of_harem(the_person)
    return

label ask_to_join_harem_label(the_person):
    #Requires high love, if successful she becomes your girlfriend (which unlocks many other options). Requires high love and her not being in a relationship.
    #Hide this event at low love, show it when it at it's lowest love possibility and let it fail out for specific reasons (thus informing the player WHY it failed out).
    #requires you have to make her a girlfriend/paramour before you can suggest harem
    #General dialogue used for everyone.
    mc.name "[the_person.title], can I talk to you about something important?"
    the_person "Of course. What's on your mind."
    mc.name "I've been thinking about this for a while. I really hope you feel as strongly as I do about us."
    mc.name "I want you to be part of something bigger, we both have a lot of love to share."
    mc.name "I want us to be part of a strong and healthy polyamorous relationship, do you accept?"
    "[the_person.possessive_title!c] takes a moment before responding."
    #you are already in a relationship with them, but want to make them accept the harem
    $ convinced = False
    if the_person.is_single:
        if the_person.opinion.threesomes > 0:
            "[the_person.possessive_title!c] hesitates for a long moment. At long last she nods."
            "[the_person.possessive_title!c] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            the_person "Of course! [the_person.mc_title], the more the merrier!"
            the_person "I look forward to seeing our family grow!"
            $ convinced  = True
        else:
            the_person "I'm not ready yet [the_person.mc_title], I really like having you all to myself...."

    elif the_person.has_exact_role(girlfriend_role):
        the_person "Well, we are together already...."
        the_person "And I really like having you all to myself..."
        the_person "Including more into the mix?"
        if the_person.opinion.threesomes > 0:
            "[the_person.possessive_title!c] hesitates for a long moment. At long last she nods."
            "[the_person.possessive_title!c] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            the_person "I look forward to seeing our growing family!"
            $ convinced  = True
        else:
            the_person "I'm not ready yet [the_person.mc_title], I really like having you all to myself..."

    elif the_person.is_affair: #we keep the paramour til she is ready to leave the husband or told to by mc
        the_person "Well technically I'm already in a polyamorous relationship, but I am the link."
        the_person "So it does make sense you want something more than what I can offer you..."
        the_person "I mean, I already have a [the_person.so_title] and I can't just leave him like this."
        if the_person.opinion.threesomes > 0:
            "[the_person.possessive_title!c] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            "[the_person.possessive_title!c] hesitates for a long moment. At long last she nods."
            the_person "I look forward to seeing what I can add to our growing family!"
            $ convinced  = True
        else:
            the_person "I care about you a lot, but it's just not something I could do."
            the_person "Oh [the_person.mc_title], I'm so flattered, but you know that I have a [the_person.so_title]."
            if the_person.kids > 0:
                if the_person.kids > 1:
                    the_person "I would never dream of leaving him, and it would devastate our children."
                else:
                    the_person "I would never dream of leaving him, and it would devastate our child."
            else:
                the_person "I would never dream of leaving him."

    elif the_person in (lily, cousin):
        the_person "[the_person.mc_title], you do make me happy..."
        if the_person.opinion.threesomes > 0:
            "She stares deep into your eyes as you take her hands and hold them in yours."
            mc.name "Just be with me [the_person.title]. It's that simple."
            "[the_person.possessive_title!c] hesitates for a long moment. At long last she nods."
            the_person "Okay, you're right. We've gone this far already..."
            $ convinced  = True
        else:
            the_person "I care about you a lot, but it's just not something I could do."

    elif the_person in (mom, aunt):
        the_person "A bigger family?"
        the_person "As long as you understand where we stand, I think we can be."
        if the_person.opinion.threesomes > 0:
            "[the_person.possessive_title!c] stares deep into your eyes as you take her hands and hold them in yours."
            mc.name "Just be with me [the_person.title]. It's that simple."
            "[the_person.possessive_title!c] hesitates for a long moment. At long last she nods."
            the_person "Okay, you're right. We've gone this far already..."
            $ convinced  = True
        else:
            the_person "I care about you a lot, we are family, that will never change."
            the_person "Adding more, I don't know? I need to think about it..."
    else:
        the_person "[the_person.possessive_title!c] taps her leg thinking about the pros and cons."

    if convinced:
        # She agrees, you're now in a relationship! Congratulations!
        $ the_person.draw_person(emotion = "happy")
        $ the_person.change_stats(happiness = 15, love = 5)
        $ the_person.discover_opinion("threesomes")
        if the_person.age > 40:
            the_person "Oh I'm so happy to hear you say that! I was worried about our age difference, but I don't want that to stop us!"
        else:
            the_person "Oh my god, I'm so happy! Yes, I want to be part of your flock!"
        "She puts her arms around you and pulls you close."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        $ mc.change_locked_clarity(10)
        "She kisses you, and you kiss her back just as happily."
        $ the_person.add_role(harem_role)
    else:
        mc.name "Remember [the_person.title], we will never be alone again."
        mc.name "If you change your mind, I'll be here for you."
        "Perhaps her willingness to share you with another is not high enough (threesomes opinion)."

    return


label harem_move_to_mansion_label(the_person):
    # TODO: Write more elaborate dialogue for inviting to mansion
    mc.name "[the_person.title], would you like to live with me?"
    the_person "Oh [the_person.mc_title], I've been waiting for you to ask me this."
    the_person "Ever since you asked me to explore out relationship further. Of course I want to live with you!"
    mc.name "Perfect, I've already made arrangements, I will see you at my new mansion soon."

    $ move_into_harem(the_person)
    return
