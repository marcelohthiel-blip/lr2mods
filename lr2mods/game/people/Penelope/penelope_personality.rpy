
label penelope_flirt_response_low(the_person):
    if the_person.is_at_work:
        if any(x for x in city_rep.primary_job.wardrobe if x.matches(the_person.outfit)):
            "[the_person.possessive_title!c] blushes and looks away, suddenly shy."
            the_person "Well... you made me wear this..."
            mc.name "I know, but you do look great."
            $ mc.change_locked_clarity(5)
            "[the_person.title] looks back at you and smiles."
            the_person "Thank you."
        else:
            $ mc.change_locked_clarity(5)
            "[the_person.possessive_title!c] blushes and smiles."
            the_person "Thank you, it's just one of my work outfits."
            mc.name "I just wanted to complement your on your outfit."
    else:
        call expression f"{the_person.personality.default_prefix}_flirt_response_low" pass (the_person) from _call_penelope_flirt_response_low
    return

label penelope_flirt_response_mid(the_person):
    if the_person.is_at_work:
        if any(x for x in city_rep.primary_job.wardrobe if x.matches(the_person.outfit)):
            the_person "Ah..."
            "[the_person.possessive_title!c] blushes and looks away."
            $ mc.change_locked_clarity(10)
            mc.name "Come now, give me a twirl and show me how my outfit looks on you."
            $ the_person.draw_person(position = "back_peek")
            $ mc.change_locked_clarity(10)
            mc.name "Perfect."
            $ the_person.draw_person()
        else:
            the_person "Oh... Thanks."
            "[the_person.possessive_title!c] blushes and looks away."
            the_person "Sorry. I'm just not used to someone paying this much attention to me."
            mc.name "It's alright. Come on, give me a spin."
            "She hesitates for a moment, then smiles meekly and nods."
            $ the_person.draw_person(position = "back_peek")
            $ mc.change_locked_clarity(10)
            the_person "Like this?"
            $ the_person.draw_person()
            mc.name "Perfect."
    else:
        call expression f"{the_person.personality.default_prefix}_flirt_response_mid" pass (the_person) from _call_penelope_flirt_response_mid
    return

label penelope_flirt_response_high(the_person):
    if the_person.is_at_work:
        if any(x for x in city_rep.primary_job.wardrobe if x.matches(the_person.outfit)):
            "[the_person.possessive_title!c] blushes and glances around nervously."
            the_person "[the_person.mc_title], what if someone heard you!"
            mc.name "Don't worry, I'm just admiring the outfit I put together for you."
            mc.name "Come now, turn around and bend over, let me see that sexy but."
            $ the_person.draw_person(position = "standing_doggy")
            $ mc.change_locked_clarity(20)
            the_person "Alright, but only for a minute."
            mc.name "Just amazing, thank you [the_person.fname]."
            $ the_person.draw_person()
        else:
            "[the_person.possessive_title!c] glances around."
            the_person "Well it's just the two of us here... Maybe we could just..."
            "She steps close to you and nervously holds your hand."
            mc.name "Well now, [the_person.title], you're not proposing something indecent here?"
            "[the_person.possessive_title!c] blushes and looks away."
            $ the_person.slap_ass()
            "She's startled by the slap on her ass and looks back to you."
            mc.name "I will see what I can do."
    else:
        call expression f"{the_person.personality.default_prefix}_flirt_response_high" pass (the_person) from _call_penelope_flirt_response_high
    return
