label strip_dancing_intro(the_person, guy_state, for_pay = False):
    "[the_person.possessive_title!c] takes up a position a few {long_height_system} in front of you."
    "She sets her feet a shoulder-width apart and starts to move, shifting her shoulders and hips to imagined music."
    return

label strip_dancing_transition(the_person, guy_state, for_pay = False):
    "[the_person.possessive_title!c] starts to get a little more comfortable."
    "After warming up for a little bit she starts to move her body."
    "She sways her hips and shoulders from side to side in time with imagined music, giving you a more dynamic view of her body."
    return

label strip_dancing_turn_towards(the_person, guy_state, for_pay = False):
    $ the_person.draw_person()
    "She gives her ass a few more shakes, then turns back to you and runs her hand down her hips."
    return

label strip_dancing_turn_away(the_person, guy_state, for_pay = False):
    "She swings her hips a few times, then lets the movement carry her in a half-circle."
    $ the_person.draw_person(position = "back_peek")
    "She looks at you over her shoulder, giving you a wink and a smile."
    return

label strip_dancing_towards_1(the_person, guy_state, for_pay = False):
    if the_person.has_large_tits:
        "[the_person.title] moves her body side to side for you, letting her large tits bounce and jiggle while you watch."
    else:
        "[the_person.title] moves her body side to side for you while you watch."

    if guy_state == "jerking":
        "You stroke your cock slowly as she dances in front of you."
    return

label strip_dancing_towards_2(the_person, guy_state, for_pay = False):
    if the_person.has_large_tits:
        if the_person.tits_visible:
            "She cups her big tits in her hands and jiggles them playfully."
        else:
            "She rolls her shoulders, emphasizing her big tits hidden underneath her [the_person.outfit.get_upper_top_layer.display_name]."
    else:
        if the_person.tits_visible:
            "She plants her hands on her tits and rubs them playfully."
        else:
            "She runs her hands over her chest, emphasizing her breasts."

    if guy_state == "jerking":
        "Your cock responds, twitching with excitement in your hand. You keep stroking yourself and enjoy the show."
    return

label strip_dancing_away_1(the_person, guy_state, for_pay = False):
    "[the_person.title] lifts her hands above her body, giving you a good look at her ass."
    if the_person.vagina_visible:
        "She shakes her hips and jiggles her ass for you."
    else:
        "She shakes her hips and jiggles her ass. You wonder what it would look like without her [the_person.outfit.get_lower_top_layer.display_name] in the way."

    if guy_state == "jerking":
        "You can't help but be turned on by the view. You stroke your shaft faster, unconsciously keeping time with the rhythm of [the_person.title]'s hips."
    return

label strip_dancing_climax(the_person, guy_state, for_pay = False):
    "[the_person.possessive_title!c]'s dancing speeds up and takes on a frantic, almost jerky quality."
    the_person "Oh my... Ah...!"
    "She squeals and locks her knees together, climaxing just from you watching her."
    $ the_person.have_orgasm(trance_chance_modifier = the_person.opinion(("public sex", "masturbating")), reset_arousal = False)
    "Her thighs quiver with effort for a few seconds, then relax as the orgasm passes."
    "Her shoulders slump and she takes long, deep breaths to try and regain control of herself."
    "When she has caught her breath she gives you a weak smile and wiggles her hips, starting to dance for you again."
    return
