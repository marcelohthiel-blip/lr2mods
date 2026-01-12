label maid_slap_ass_label(the_person):
    mc.name "Hello [the_person.title], I see you are slacking off again."
    the_person "I... I wasn't [the_person.mc_title]."
    mc.name "Didn't I tell you that I would be the judge of your competence?"
    the_person "Yes, of course, [the_person.mc_title]."

    mc.name "You know what to do..."
    $ the_person.draw_person(position = "standing_doggy")
    "She slowly bends over, pushing out her peachy bottom."

    call maid_spank_loop(the_person) from _call_maid_spank_loop_maid_slap_ass

    mc.name "Good, perhaps we will do this again sometime. Now get dressed and get back to work."
    the_person "Yes, [the_person.mc_title]."

    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person()
    "She rearranges her uniform and gets back to work."
    return

label maid_spank_loop(the_person):
    if the_person.outfit.has_apron:
        mc.name "Now, take off your apron, [the_person.title]."
        "She only nods in agreement, but there is slight uncertainty in her movements."
        $ the_clothing = the_person.outfit.get_lower_top_layer
        $ the_person.draw_animated_removal(the_clothing, position = "standing_doggy")

    $ the_clothing = the_person.outfit.get_lower_top_layer
    if the_clothing:
        mc.name "Hmmm... This won't do, please get your [the_clothing.display_name] out of the way."
        if the_person.has_taboo("underwear_nudity"):
            "She looks a little nervous, pausing for a moment, giving you a quick glance."
            "You just give a her a small nod, indicating that she should continue."
        $ the_person.break_taboo("underwear_nudity")
        $ the_person.draw_animated_removal(the_clothing, position = "standing_doggy", half_off_instead = True)
        "She slowly pulls the [the_clothing.display_name] out of the way."
        mc.name "That's a good girl."

    "You slowly move closer and rub her butt a little to determine how to maximize the effect of the spanking."
    $ play_moan_sound()
    "She lets out a small moan, while you rub her ass cheeks."

    mc.name "Right, let's begin, I haven't got all day."
    $ the_person.slap_ass()
    "She lets out a small cry, but otherwise stands still."

    $ the_person.slap_ass(update_stats = False)
    $ the_person.slap_ass(update_stats = False)

    mc.name "Good, keep this position and we can finish this quickly."
    the_person "Yes [the_person.mc_title]."

    $ the_person.slap_ass()
    $ the_person.slap_ass(update_stats = False)

    the_person "Argh, shit..."
    "You inspect her ass and it is [the_person.ass_spank_description]."

    mc.name "Shh... we are almost done."
    "She only gives a small nod of agreement, but there is a light tremor in her legs."

    $ the_person.slap_ass()
    $ the_person.slap_ass(update_stats = False)

    the_person "Please, [the_person.mc_title]. I promise I will do better!"
    "You rub her ass a little, while you whisper in her ear."
    mc.name "Be a good little girl, for your Master."
    $ play_moan_sound()
    $ the_person.change_stats(arousal = 10, obedience = 1)
    "The mere mentioning of her being a good girl makes her moan."

    $ the_person.slap_ass()
    $ the_person.slap_ass(update_stats = False)

    mc.name "That is enough for now."
    $ play_moan_sound()
    $ the_person.change_stats(arousal = 10, obedience = 1)
    "You start rubbing her ass as a reward, promptly making her moan again."

    mc.name "What do good girls say after receiving a proper spanking?"
    the_person "Thank you, [the_person.mc_title], for showing me how to be a good girl."
    return

label maid_grope_label(the_person):
    "While watching [the_person.possessive_title] performing her duties, you notice that she's making an effort..."
    $ the_person.draw_person(position = "standing_doggy")
    "to move as gratuitously as possible to show off her ass, wiggling it and pushing out her bottom while cleaning."

    $ the_person.draw_person("doggy")
    "Getting down on all fours to pick something up, she makes sure to keep her perky ass pointed right at you."

    mc.name "[the_person.title], would you come over here please? We need to have a talk."
    $ the_person.draw_person("back_peek")
    the_person "Oh... Yes, [the_person.mc_title]."
    $ the_person.draw_person()

    call maid_grope_loop(the_person) from _call_maid_grope_loop_maid_grope

    $ the_person.draw_person()
    "You step back and turn her around."

    mc.name "That concludes our lesson for today, [the_person.fname]."
    the_person "Thank you, [the_person.mc_title], for showing me how to be a good girl."

    mc.name "Good, now get dressed and get back to work."
    the_person "Yes, [the_person.mc_title]."

    $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person()
    "She rearranges her uniform and gets back to work."
    return

label maid_grope_loop(the_person):
    menu:
        "Give her another spanking" if the_person.spank_level <= 4:
            mc.name "I have been checking your work, but it seems you are not putting in the required effort."
            the_person "But I've been doing my best."
            "You give her a stern look."
            the_person "Sir!"
            mc.name "Who is your employer? And who evaluates your work?"
            the_person "Euh... you do, [the_person.mc_title]."
            mc.name "I think another spanking would teach you to be a better employee, don't you agree?"
            if the_person.spank_level > 2:
                "Her bottom still hurts a little from the last time."
            the_person "If you think that would help, [the_person.mc_title]."
            mc.name "Good, please assume the position..."
            $ the_person.draw_person(position = "standing_doggy")
            "She slowly bends over, pushing out her perky ass."

            call maid_spank_loop(the_person) from _call_maid_spank_loop_maid_grope

            mc.name "Now its time for your reward, for being a good girl."

        "Give her another spanking\nToo recently spanked (disabled)" if the_person.spank_level > 4:
            pass

        "Continue":
            mc.name "I think a good girl deserves a little reward. Don't you agree [the_person.fname]?"
            "She gives you a quick glance, unsure how to respond."
            mc.name "Please stand here and bend over forward..."
            $ the_person.draw_person(position = "standing_doggy")
            "She assumes the position, slightly trembling, unsure about what is going to happen next."

    $ the_clothing = the_person.outfit.get_lower_top_layer
    if the_clothing and the_clothing != the_person.panties:
        mc.name "Could you please take off your [the_clothing.display_name]?"
        "She gives you a quick glance, but proceeds as asked."
        $ the_person.draw_animated_removal(the_clothing, position = "standing_doggy", half_off_instead = False)

    if the_person.outfit.wearing_panties:
        $ the_clothing = the_person.panties
        mc.name "Now be a good girl and remove your [the_clothing.display_name], please?"
        if the_person.has_taboo("bare_pussy"):
            the_person "But Sir, is that really necessary?"
            mc.name "I think it is, the extra humiliation of being naked will improve the impact of the lesson."
            "You can see the resignation on her face and she starts to remove her [the_clothing.display_name]."
        else:
            "Again, she gives you a glance, but proceeds to remove her [the_clothing.display_name]."

        $ the_person.draw_animated_removal(the_clothing, position = "standing_doggy", half_off_instead = False)
        $ the_person.break_taboo("bare_pussy")

    "You position yourself behind her so you can softly talk into her ear while giving you full access to her exposed body."
    "You can hear her breathing with a mix of anticipation and fear."

    $ the_person.slap_ass(update_stats = False)
    mc.name "You do have a magnificent butt, [the_person.fname], I could spank it all day long..."
    $ play_moan_sound()
    $ the_person.change_arousal(10)
    if the_person.spank_level > 4:
        the_person "Please Sir, don't, it still hurts so much."
    else:
        the_person "Please Sir, couldn't you punish me in another way."

    mc.name "Sssh... It's not a punishment."
    "You slowly start rubbing her ass cheeks."
    mc.name "It's an education."
    $ play_moan_sound()
    $ the_person.change_arousal(10)
    the_person "Thank you, [the_person.mc_title], this feels a lot better."

    "As you move your fingers between her legs, you can feel the wetness of her labia."
    $ play_moan_sound()
    $ the_person.change_arousal(20)
    mc.name "Would you like me to continue the lesson?"
    the_person "Oh, [the_person.mc_title], please do?"

    mc.name "Good girl, let's see what we can do."

    $ play_moan_sound()
    $ the_person.change_arousal(10)
    $ the_person.draw_person(position = "walking_away")
    "You stand behind her and pull her into a warm embrace, enticing another moan."

    menu:
        "Keep groping":
            call fuck_person(the_person, start_position = standing_grope, start_object = make_floor(), skip_intro = True, girl_in_charge = False, self_strip = False, position_locked = True) from _call_fuck_person_maid_grope_1

        "Finger her":
            call fuck_person(the_person, start_position = standing_finger, start_object = make_floor(), skip_intro = True, girl_in_charge = False, self_strip = False, position_locked = True) from _call_fuck_person_maid_grope_2

    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 1:
        "[the_person.possessive_title!c] is trembling on her legs. You know she had multiple orgasms from your skilled movements."
        $ the_person.draw_person()
        "She looks back at you with a deepfound respect and gratitude."
    elif the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title!c] is slightly uncertain on her feet, gratefull for the release of her tension."
        $ the_person.draw_person()
        "She looks back at you and smiles."
    return

label maid_service_label(the_person):
    return
