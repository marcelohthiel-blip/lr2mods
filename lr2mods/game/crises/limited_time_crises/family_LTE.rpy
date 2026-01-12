
label sister_walk_in_label(the_person):
    if the_person.effective_sluttiness() < 10:
        "You try to open the door to [the_person.title]'s room, but find it locked."
        $ the_person.change_arousal(30, add_to_log = False)
        the_person "Ah! One... One second!"
        "You hear scrambling on the other side of the door, then the lock clicks and [the_person.possessive_title] pokes her head out."
        $ the_person.draw_person()
        the_person "Oh... [the_person.mc_title], it's only you. Come on in, what's up?"
        "Her face is flush and her breathing rapid. You wonder for a moment what you almost caught her doing as she leans nonchalantly against the door frame."
        $ mc.change_locked_clarity(5)
        $ clear_scene()
        return

    elif the_person.effective_sluttiness() < 25:
        "You try to open the door to [the_person.title]'s room, but find it locked."
        $ the_person.change_arousal(40, add_to_log = False)
        the_person "Ah! One... One second!"
        "You hear scrambling on the other side of the door, then the lock clicks and [the_person.possessive_title] pokes her head out."
        $ the_person.draw_person()
        the_person "[the_person.mc_title], it's you. What's up?"
        "Her face is flush and her breathing rapid. Her attempt at being nonchalant is ruined when a loud moan comes from her laptop, sitting on her bed."
        "Laptop" "Ah! Fuck me! Ah! Yes!"
        the_person "Oh my god, no!"
        "She sprints to her bed, opening up her laptop and turning it off as quickly as possible."
        $ mc.change_locked_clarity(10)
        mc.name "Am I interrupting?"
        "[the_person.possessive_title!c] spins around, beet red, and stammers for a moment."
        the_person "I... I don't... Umm... I think my laptop has a virus, all these crazy popups!"
        mc.name "Mmmhm? Do you want me to take a look?"
        the_person "No, no that's okay. It's probably fine."
        menu:
            "Encourage her":
                mc.name "You know there's nothing wrong with watching porn, right?"
                the_person "I wasn't! I..."
                mc.name "Of course not, but even if you were there's nothing wrong with that. It's a natural thing, everyone does it. I certainly do."
                $ the_person.change_stats(slut = 1, max_slut = 20, happiness = 5)
                the_person "Really? Ew, I don't need to know about that."
                "She still seems more interested than her words would suggest."

            "Threaten to tell [mom.possessive_title]":
                mc.name "I can let [mom.fname] know, maybe she can take it somewhere to get it fixed."
                the_person "No! I mean, you can't tell Mom. Nothing's wrong with it, okay?"
                mc.name "So you were..."
                $ the_person.change_stats(obedience = 2, love = -1)
                the_person "I was watching porn, okay? Can you not make such a big deal about it?"
                mc.name "You should have just told me that right away, there's nothing wrong with watching some porn and getting off."
                the_person "I wasn't getting off, I was just..."
                mc.name "Watching it for the acting?"
                the_person "Ugh, shut up. What do you need?"

    else:
        $ the_person.outfit.strip_to_vagina()
        $ the_person.draw_person(position = "missionary")
        $ the_person.change_arousal(40, add_to_log = False)
        "You open the door to [the_person.title]'s room and find her sitting up in bed with her laptop beside her, legs splayed open and fingers deep in her own pussy."
        "Her eyes are closed, and because of her headphones it doesn't seem like she's noticed you come in. She lets out the softest moan."
        $ mc.change_locked_clarity(20)
        the_person "Mmmph..."
        menu:
            "Offer to help":
                "You step into the room and close the door."
                mc.name "Having a good time?"
                if the_person.effective_sluttiness("touching_vagina") < 35:
                    the_person "Hmm? Oh my god!"
                    "She opens her eyes slowly, before yelling in surprise and grabbing desperately for her blankets in an attempt to salvage her decency."
                    the_person "Oh my god, [the_person.mc_title]! What are you... I... Get out of here!"
                    mc.name "Don't be so dramatic [the_person.title], I just want to know if you want some help."
                    the_person "Help?! Ew, oh god!"
                    "She grabs a pillow and throws it at you."
                    the_person "Get out! Get out!"
                    "You retreat from the room before [mom.title] hears what's happening and comes to investigate."

                else:
                    the_person "Hmm?"
                    if the_person.effective_sluttiness("touching_vagina") < 55 or the_person.has_taboo(["touching_vagina","bare_pussy"]):
                        "She opens her eyes slowly, then gasps in surprise. She grabs a pillow and uses it to cover herself."
                        the_person "Oh my god, [the_person.mc_title]! What are you doing, I'm..."
                        "She blushes a little."
                        the_person "Well, you know."
                        mc.name "I just wanted to know if you need a hand."
                        the_person "I... We really shouldn't..."
                        "Despite her verbal hesitations she slides the pillow out of the way and gives you \"fuck me\" eyes."
                        $ mc.change_locked_clarity(10)

                    else:
                        "She opens her eyes slowly."
                        the_person "Oh, it's you [the_person.mc_title]. What do you need? I was just relaxing a little."
                        "She rubs her pussy gently while she talks to you, stroking the wet pink slit with a finger."
                        $ mc.change_locked_clarity(20)
                        mc.name "I don't need anything, but it looks like you might. Do you need a hand with that?"
                        "She nods and gives you \"fuck me\" eyes."
                    $ the_person.update_outfit_taboos()


                    "You slide onto the bed and run your fingers along [the_person.title]'s body, moving down towards her already-wet pussy."
                    $ the_person.break_taboo("touching_vagina")
                    $ play_moan_sound()
                    "When you first touch her she gasps and quivers, and when you slide your middle finger into her pussy she moans."
                    "She slides her body against you, and when you pull her off the bed she doesn't argue."
                    "You stand behind her, one hand grasping a breast and the other gently pumping a finger in and out of her."
                    call fuck_person(the_person, start_position = standing_finger, private = True) from _call_fuck_person_2
                    $ the_report = _return
                    if the_report.get("girl orgasms", 0) > 0:
                        "[the_person.possessive_title!c] falls back on her bed and sighs happily."
                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                        $ the_person.change_stats(obedience = 1, love = 2)
                        the_person "Thank you [the_person.mc_title], that's exactly what I wanted. Ahh..."
                        "She rolls over and gathers up a collection of pink blankets on top of herself, quickly falling asleep."
                        "You step out of the room to give her some time to recover."

                    elif the_report.get("guy orgasms", 0) > 0:
                        $ the_person.draw_person(position = "stand4", emotion = "angry")
                        the_person "So... Is that it?"
                        mc.name "What do you mean?"
                        $ the_person.change_stats(obedience = -2, love = -2)
                        $ the_person.draw_person(position = "missionary", emotion = "angry")
                        "She scoffs and falls back onto her bed, pulling her blankets over herself."
                        the_person "Nothing, I'm glad you enjoyed yourself at least. Get out of here so I can get off."

                    else:
                        $ the_person.draw_person(position = "stand4", emotion = "angry")
                        the_person "So... are you finished?"
                        mc.name "Heh, yeah. Sorry [the_person.title], I'm just not feeling it."
                        $ the_person.draw_person(position = "missionary", emotion = "angry")
                        "She frowns, but nods. She gathers her blankets over herself as you are walking out of her room."
                        $ the_person.change_obedience(-2)

            #Consider a taboo break for this action if she is slutty enough. For now, require them already broken
            "Mutual Masturbation" if not the_person.has_taboo(["touching_vagina", "touching_penis"]):
                "You step into the room and close the door."
                mc.name "That looks fun. Mind if I join you?"
                if the_person.effective_sluttiness("touching_vagina") < 35:
                    the_person "Hmm? Oh my god!"
                    "She opens her eyes slowly, before yelping in surprise."
                    the_person "Oh my god, [the_person.mc_title]! I didn't even hear you come in!"
                    "You drop your pants and underwear and walk over to her bed, laying down next to her."
                    mc.name "Keep going [the_person.title], I'll do it too."

                else:
                    the_person "Hmm?"
                    "She opens her eyes slowly, then gasps in surprise."
                    the_person "Oh my god, [the_person.mc_title]! What are you doing, I'm..."
                    "She blushes a little."
                    the_person "Well, you know."
                    "You drop your pants and underwear and walk over to her bed, laying down next to her."
                    mc.name "I noticed, and I liked it. Keep going, I'll do it too."
                    the_person "Oh! I... I guess..."

                $ mc.change_locked_clarity(15)
                "You put your hand on your cock and start to stroke it. She realises what you are doing and continues to touch herself also."
                the_person "Mmm... that's nice..."
                "She looks over at the porn at her laptop, then looks back at your dick."
                the_person "You know, I don't really need this anymore..."
                "She reaches with her foot and closes the laptop lid. The sounds cut off."
                "[the_person.possessive_title!c] looks back at your groin and resumes touching herself. You give yourself several more strokes."
                $ mc.change_locked_clarity(25)
                the_person "Mmmm!... ahhh..."
                "Her eyes are glued to your cock as she plays with herself."
                mc.name "Hey... why don't we trade jobs? I'll touch you and you can touch me. It'll feel a lot better that way."
                if the_person.effective_sluttiness("touching_vagina") < 35:
                    the_person "Oh? I don't know..."
                    "She hesitates for a moment."
                    mc.name "Here, I'll show you."
                    "You reach between her legs and take her hand. She let's you take her hand from between her legs and you put it on your erection."
                    "She wraps her hand around it and starts to stroke it. You return your hand between her legs and start to touch her there."
                else:
                    the_person "Mmmm, sounds great..."
                    "She takes her hand from between her legs and reaches over. She grasps your erection and starts to stroke it."
                    "You return the favour, putting your hand between her legs and begin to touch her."
                $ mc.change_locked_clarity(35)
                $ the_person.change_arousal(15)
                $ mc.change_arousal(15)
                "[the_person.possessive_title!c]'s soft hand beings stroking you as you slide your middle finger between her outer labia, along her slit."
                the_person "Mmmm... ahhh... that's nice..."
                "Her body tenses up for a second when you push your middle finger inside of her. She sighs in appreciation."
                mc.name "Feels better when it is someone else doing it, doesn't it?"
                if the_person.love >= 40:
                    the_person "Yeah, I love it when you touch me [the_person.mc_title]..."
                    $ mc.change_locked_clarity(35)
                else:
                    the_person "Mmm, less talking more touching..."
                    $ mc.change_locked_clarity(20)
                $ the_person.change_arousal(15)
                $ mc.change_arousal(15)
                "[the_person.possessive_title!c]'s pussy is already soaking wet. She was probably close to finishing before you interrupted her..."
                "You stroke the inside of her vagina slowly, being careful for now to stay away from her g-spot. You want to give yourself time to catch up."
                "She brings her hand up to her mouth and gives it a bunch of spit, then reaches down and resumes stroking your cock."
                $ mc.change_locked_clarity(35)
                $ the_person.change_arousal(5)
                $ mc.change_arousal(15)
                the_person "Ahhh..."
                "She sighs and lays her head on your shoulder. Her hips are moving slightly as you continue to stroke each other."
                if the_person.love >= 40:
                    "[the_person.title] turns her head towards you. You can feel her warm breath on your neck."
                    "You sigh when she starts to kiss you on your neck, just below your jawline."
                    $ mc.change_locked_clarity(30)
                    "The sensations of her lips on your neck and soft sighs next to your ear makes your cock twitch in her hand."
                else:
                    "The soft sighs and strokes she is giving you feel great."
                $ mc.change_arousal(20)
                "Your body is responding to her touch, and your arousal is starting to build with each stroke."
                "You push a second finger inside of [the_person.possessive_title] and begin to stroke her g-spot."
                $ mc.change_locked_clarity(35)
                $ the_person.change_arousal(15)
                $ mc.change_arousal(15)
                the_person "Ooohhhh fffuuu... [the_person.mc_title], are you close too?"
                mc.name "Very close."
                if the_person.love >= 40:
                    "[the_person.title] nuzzles her nose against your ear and whispers urgently."
                    the_person "Cum with me [the_person.mc_title]. Cum with your little sister!"
                    $ mc.change_locked_clarity(35)
                else:
                    the_person "Mmm, good. I can't wait...!"
                    $ mc.change_locked_clarity(15)
                $ the_person.change_arousal(15)
                $ mc.change_arousal(15)
                "She continues to stroke you, her hand moving faster and faster. You can feel your orgasm building, your balls tightening."
                "Her back arches and her body starts to tremble as she starts to cum."
                $ the_person.have_orgasm()
                "Watching [the_person.title] orgasm right next to you sends you over the edge as well."
                $ ClimaxController.manual_clarity_release(climax_type = "hand", person = the_person)
                "Your cum bursts out, coating Lily's hand and the bed beneath her. She keeps stroking you, milking every drop she can."
                "After several seconds, movements stop and you lay together in bed with [the_person.possessive_title], your hands still on each other's body."
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                $ the_person.change_stats(obedience = 1, love = 2, max_love = 60, max_obedience = 140)
                if the_person.love >= 40:
                    the_person "Mmm, that was just what I needed, I'm so glad you walked in [the_person.mc_title]."
                else:
                    the_person "Wow... that was nice..."
                if the_person.opinion.drinking_cum > 0:
                    "Her hand leaves your penis and she brings it close to her face."
                    the_person "Mmm, you made a LOT of cum for me..."
                    "She opens her mouth and begins to eagerly lick your cum from her hand."
                    $ the_person.discover_opinion("drinking cum")
                    "Soft slurping noises echo in your ear as she licks her hand clean, swallowing it all."
                    $ the_person.change_happiness(3)
                else:
                    the_person "You're kinda messy though..."
                    $ the_person.draw_person(position = "walking_away")
                    "She rolls on her side and reaches over to her night stand, grabbing some wipes. She cleans her hand off and then rolls back over."
                    $ the_person.draw_person(position = "missionary")
                the_person "Thank you [the_person.mc_title], but I'm about to fall asleep now..."
                "She rolls over and gathers up a collection of pink blankets on top of herself, quickly falling asleep."
                "You get up and get dressed, then step out of the room."


            "Just watch":
                "You step into the room and close the door to [the_person.title]'s room."
                "You lean on the doorframe and watch her fingering herself."
                $ mc.change_arousal(5)
                the_person "Ah... Mmmm."
                "She opens her eyes and glances at her laptop, then finally notices you."
                if the_person.effective_sluttiness("bare_pussy") + (the_person.obedience - 100) < 40: #If she's not slutty or obedient she yells at you to get out
                    the_person "Oh my god, [the_person.mc_title]! What are you... I... Get out of here!"
                    mc.name "Don't be so dramatic [the_person.title], just keep going."
                    the_person "What?! Ew, how long have you been there? Oh god!"
                    "She grabs a pillow and throws it at you."
                    the_person "Get out! Get out!"
                    "You retreat from the room before [mom.title] hears what's happening and comes to investigate."

                else: #Otherwise she lets you stay long enough for you to tell her to keep going.
                    the_person "Oh my god, [the_person.mc_title]! What are you doing, I'm..."
                    "She blushes a little."
                    the_person "Well, you know."
                    mc.name "Don't worry about me, just keep going."
                    if the_person.effective_sluttiness("bare_pussy") < 60: #She's a little unsure about it, but goes for it
                        the_person "Really? I... I mean, do you really want to see me like this?"
                        "[the_person.possessive_title!c] relaxes a little, her hand unconsciously drifting back between her legs."
                        mc.name "I think it's hot, keep touching yourself for me."
                        "She shrugs and nods, spreading her legs and sliding a finger along her wet slit."
                        $ the_person.change_obedience(2)
                    else:
                        the_person "If you want..."
                        "She smiles and spreads her legs, sliding a finger along her wet slit."

                    $ mc.change_locked_clarity(10)
                    $ the_person.update_outfit_taboos()

                    "[the_person.possessive_title!c] starts to finger herself again, slowly moving a pair of fingers in and out, in and out."
                    "Soon she's almost forgotten about you standing and watching at her door. She arches her back and turns her head, moaning into a pillow."
                    "She starts to rock her hips against her own hand as her fingering becomes increasingly intense."
                    "Even as she starts to climax she keeps her legs wide open, giving you a clear view of her dripping wet cunt."
                    $ the_person.have_orgasm()
                    "Her body spasms as she cums, fingers buried deep inside herself. She holds them there for a long moment, eyes shut tight."
                    "Finally she relaxes and pulls her fingers out, trailing her own juices behind them. She glances up at you and smiles weakly."
                    $ mc.change_locked_clarity(20)
                    the_person "Ah... That was good."
                    "You smile at her and walk out of the room."
                    $ the_person.change_slut(1+the_person.opinion.masturbating, 50)
                    $ the_person.discover_opinion("masturbating")
                    $ the_person.reset_arousal()

            "Leave her alone":
                $ clear_scene()
                $ the_person.run_orgasm(show_dialogue = False, add_to_log = False, fire_event = False)
                "You take a quick step back and, as quietly as you can manage and close her door."



    $ mc.change_location(hall)
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return

label nude_walk_in_label(the_person):
    if renpy.random.randint(0,100) < 50:
        $ the_person.apply_outfit(Outfit("Nude"))
        $ mc.change_locked_clarity(15)
        $ the_person.draw_person()
        "You open the door to [the_person.possessive_title]'s room and see her standing in front of her mirror, completely nude."
        if the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) < (50 - (the_person.opinion.not_wearing_anything*10)):
            # She asks you to step out for a moment.
            if the_person.has_large_tits:
                "She turns and tries to cover herself with her hands, but her big tits are still easily on display."
            else:
                "She turns and tries to cover herself with her hands."
            the_person "Just... Just a minute, I was getting changed!"
            $ clear_scene()
            "[the_person.title] shoos you out of the room. You can hear her getting dressed on the other side."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person()
            "Soon enough she opens the door and invites you in."
            $ the_person.change_slut(1+the_person.opinion.not_wearing_anything, 60)
            $ the_person.discover_opinion("not wearing anything")
            the_person "Sorry about that, I always forget to lock the door."
        else:
            # She doesn't mind and invites you in to talk, while being nude
            if the_person.update_outfit_taboos():
                "She turns around and waves you in, then seems to realise that she's naked and tries to cover herself with her hands."
                the_person "Oh, I'm not dressed! If you want I can put something on."
                mc.name "Don't worry about it. We're family, we should be comfortable around each other."
                $ mc.change_locked_clarity(10)
                "She smiles and nods, moving her hands away from her tits and pussy."
            else:
                $ mc.change_locked_clarity(10)
                "She turns to you and smiles, seemingly oblivious to her own nudity."
                the_person "Come on in! Did you need something?"



    else:
        # She's in her underwear
        $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True))
        $ the_person.draw_person(position = "sitting")
        $ mc.change_locked_clarity(10)
        "You open the door to [the_person.possessive_title]'s room and find her sitting on her bed, wearing nothing but her underwear."
        if the_person.effective_sluttiness("underwear_nudity") < (30 - (the_person.opinion.not_wearing_anything*10)):
            the_person "Oh! One second, I'm not dressed!"
            $ clear_scene()
            "She hurries to the door and closes it in your face, locking it quickly. You can hear her quickly getting dressed on the other side."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person()
            "When she opens the door she's fully dressed and invites you in."
            $ the_person.change_slut(1+the_person.opinion.not_wearing_anything, 40)
            $ the_person.discover_opinion("not wearing anything")
            the_person "Sorry about that, I was just relaxing and forgot the door wasn't locked."
        else:
            if the_person.update_outfit_taboos():
                "She turns around and waves you in, then seems to realise how little she is wearing."
                the_person "Oh, I'm not fully dressed! If you mind I can put something on."
                mc.name "Of course I don't mind. We're family, we can trust each other."
                "She smiles and nods."
            else:
                "She turns to you and smiles, waving a hand to invite you in."
                the_person "Come on in, do you need something?"


    call talk_person(the_person) from _call_talk_person_19

    # redress after event
    if the_person.outfit.item_count == 0:
        "After you finish talking, she puts on her clothes and looks at you."
        $ the_person.apply_planned_outfit()
    return

label mom_house_work_nude_label(the_person):
    # When she's in the kitchen (or any other part of the house, for later events) she'll work in her underwear or (later) nude.
    $ effective_slut = the_person.effective_sluttiness("underwear_nudity") + (the_person.opinion.not_wearing_anything*10)
    $ the_person.event_triggers_dict["housework_apron"] = True
    if effective_slut < 20: #TODO: This method of adding clothing with specific colours is dumb. (I suppose we could do the apron as being an overwear and then add it to underwear, but we should still have a system for it).
        # She's in her underwear but self-conscious about it
        $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True))
        $ add_mom_outfit_coloured_apron(the_person)
        if not the_person.has_shoes:
            $ the_person.outfit.add_feet(heels.get_copy(), colour_black)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen working on dinner. She glances over her shoulder when you enter, seeming meek."
        the_person "Hi [the_person.mc_title]. I hope you don't mind the way I'm dressed, it's nice to wear something more comfortable after I come home from work."
        $ mc.change_locked_clarity(5)
        mc.name "It's fine, I don't mind."
        "She turns her attention back to preparing dinner."

    elif the_person.effective_sluttiness("underwear_nudity") < 40:
        $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True))
        $ add_mom_outfit_coloured_apron(the_person)
        if not the_person.has_shoes:
            $ the_person.outfit.add_feet(pumps.get_copy(), colour_black)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen working on dinner in her underwear. She glances over her shoulder when you enter."
        $ mc.change_locked_clarity(5)
        the_person "Hi [the_person.mc_title], I hope you've had a good day."
        "She turns back to her work and hums happily."

    elif the_person.effective_sluttiness(["bare_pussy","bare_tits"]) < 60:
        $ the_person.apply_outfit(Outfit("Nude"))
        $ the_person.outfit.add_feet(high_heels.get_copy(), colour_white)
        $ add_mom_outfit_coloured_apron(the_person)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen, completely nude except for her apron and high heels. She glances over her shoulder when you enter."
        the_person "Hi [the_person.mc_title]. If me being... naked makes you uncomfortable just let me know. It's just nice to relax a little after work."
        $ mc.change_locked_clarity(10)
        mc.name "I don't mind at all Mom."
        "She turns her attention back to preparing dinner."

    else:
        $ the_person.apply_outfit(Outfit("Nude"))
        $ add_mom_outfit_coloured_apron(the_person)
        $ the_person.outfit.add_feet(thigh_highs.get_copy(), colour_red)
        $ the_person.outfit.add_feet(high_heels.get_copy(), colour_red)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen, completely nude except for her apron, sexy stockings and high heels. She glances over her shoulder when you enter."
        $ mc.change_locked_clarity(15)
        the_person "Hi [the_person.mc_title], I hope you've had a great day. Dinner should be ready soon!"
        "She turns back to her work and sings happily to herself, wiggling her butt as she works."

    $ the_person.update_outfit_taboos()
    $ the_person.discover_opinion("not wearing anything")
    $ clear_scene()
    return

label breeding_mom_intro_label(the_person):
    $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True))
    $ the_person.draw_person(position = "sitting")
    $ the_person.update_outfit_taboos()
    $ mc.change_locked_clarity(10)
    "You walk into [the_person.title]'s room and find her sitting on the edge of her bed, sexily dressed without any panties."
    if the_person.has_breeding_fetish:
        if the_person.knows_pregnant:
            "She is idly rubbing her belly. Your seed has already taken root there and a baby is growing."
            the_person "I was just thinking about... you know... the night where you knocked me up..."
            the_person "Do you want to re-enact it? It would be nice..."
        elif the_person.is_highly_fertile:
            the_person "Why don't you come here? I was just getting ready to come find you..."
            "She lowers her voice a bit."
            the_person "I'm pretty sure I'm fertile right now... and you know how bad I've been wanting you to knock me up!"
        return
    else:
        the_person "[the_person.mc_title], close the door, please. I have something I need to ask you."
        "You close the door to [the_person.possessive_title]'s bedroom and walk over to her bed."
        "She pats the bed beside her and you sit down."
        the_person "I've been thinking a lot about this. You're all grown up and [lily.fname] isn't far behind."
        the_person "Soon you'll both be leaving home, but I don't think I'm done being a mother yet."
        "She takes your hands in hers and looks passionately into your eyes."
        the_person "I want you to give me a child. I want you to breed me."

    if the_person.has_large_tits:
        "Her face is flush and her breathing rapid. Her [the_person.tits_description] heave up and down."
    else:
        "Her face is flush and her breathing rapid."
    $ mc.change_locked_clarity(50)

    menu:
        "Try to breed her":
            "You nod, and the mere confirmation makes her shiver. She lies down on the bed and holds out her hands for you."
            $ the_person.outfit.strip_to_vagina()
            $ the_person.draw_person(position = "missionary")
            "You strip down and climb on top of her. The tip of your hard cock runs along the entrance of her cunt and finds it dripping wet."
            the_person "Go in raw [the_person.mc_title], enjoy my pussy and give me your cum!"
            $ mc.change_locked_clarity(20)
            $ the_person.break_taboo("vaginal_sex")
            $ the_person.break_taboo("condomless_sex")
            "She wraps her arms around your torso and pulls you tight against her. She gives you a breathy moan when you slide your cock home."
            the_person "Ah... Fuck me and give me your baby! I'll take such good care of it, just like I did for you and [lily.fname]!"
            call fuck_person(the_person, start_position = breeding_missionary, start_object = mc.location.get_object_with_name("bed"), skip_intro = True, position_locked = True, skip_condom = True) from _call_fuck_person_breeding_mom_enhanced_label
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum:
                "You roll off of [the_person.possessive_title] and onto the bed beside her, feeling thoroughly spent."
                "She brings her knees up against her chest and tilts her hips up, holding all of your cum deep inside her."
                mc.name "Do you think that did it?"

                if the_person.is_highly_fertile:
                    the_person "I don't know. It's the right time of the month."
                else:
                    the_person "Chances are not very high, but I'm still hopeful."

                $ the_person.change_stats(love = 2)

                "You lie together in silence. [the_person.possessive_title!c] rocks herself side to side. You imagine your cum sloshing around her womb."
                $ the_person.draw_person(position = "sitting")
                "Eventually she puts her legs down and the two of you sit up in bed."

            else:
                "You roll off of [the_person.possessive_title] and onto the bed beside her."
                $ the_person.change_happiness(-20)
                the_person "I'm sorry... I'm sorry I'm not good enough to make you cum. I'm not good enough to earn your child..."
                "She sounds as if she is almost on the verge of tears."
                "You wrap your arms around her and hold her close."
                mc.name "Shh... You were fantastic. It's me, I'm just not feeling it today. Maybe we can try some other day."
                the_person "I don't know, this might have all been a mistake. Let's just... be quiet for a while, okay?"
                $ the_person.draw_person(position = "sitting")
                "You hold [the_person.possessive_title] until she's feeling better, then sit up in bed with her."

        "Say no":
            $ the_person.draw_person(position = "sitting", emotion = "sad")
            "You shake your head. [the_person.title] looks immediately crestfallen."
            $ the_person.change_happiness(-20)
            the_person "But why..."
            mc.name "[the_person.title], I love you but I can't give you what you want."
            "She nods and turns her head."
            $ the_person.change_stats(love = -2)
            the_person "Of course... I was just being silly. I should know better."

    $ clear_scene()
    return

label aunt_home_lingerie_label(the_person):
    $ the_person.outfit.strip_to_underwear()
    $ the_person.draw_person()
    $ mc.change_locked_clarity(10)
    "You find [the_person.possessive_title] humming a happy tune, dressed only in her underwear, as you open the door to her apartment."
    if the_person.effective_sluttiness("underwear_nudity") < 10 or the_person.has_taboo("underwear_nudity"):
        "[the_person.title] jumps when she notices you."
        the_person "Oh, [the_person.mc_title]! I didn't know you were coming over!"
        $ the_person.draw_person(position = "back_peek")
        "She turns away, trying to hide the view. You step inside and close the door."
        mc.name "Sorry, I can come back later if you'd like."
        the_person "No, it's fine. I just need a moment to get dressed. You startled me, is all."
        "[the_person.title] seems to relax now that she's recovered from the shock."
        $ the_person.draw_person(position = "walking_away")
        $ the_person.change_slut(1, 35)

        the_person "I'm sure you don't want to see me prancing around like this. Just wait there, I'll be back in a moment!"
        $ get_dressed = True
        menu:
            "Tell her to stay":
                mc.name "Don't worry about it [the_person.title], I really don't mind."
                $ the_person.draw_person(position = "back_peek")
                "[the_person.possessive_title!c] stops and peeks over her shoulder again."
                if the_person.effective_sluttiness("underwear_nudity") >= 10:
                    $ get_dressed = False
                    the_person "You don't? Isn't it embarrassing to have to look at a half-naked old woman?"
                    mc.name "We're family, we're supposed to be comfortable with each other."
                    the_person "Well... I suppose if you don't mind then I won't bother."
                    $ the_person.draw_person()
                    the_person "But you just let me know if you want me to get dressed!"
                    $ the_person.break_taboo("underwear_nudity")
                    the_person "I'm so glad you stopped by!"

                else:
                    the_person "You're sweet, but you really shouldn't see me like this. We're family, it's a little... strange."
                    the_person "I'll be back before you know it!"

            "Let her get dressed":
                pass


        if get_dressed:
            $ clear_scene()
            "[the_person.title] steps into her bedroom and closes the door."
            $ the_person.apply_planned_outfit()
            "After a brief wait she steps back out."
            $ the_person.draw_person()
            the_person "So sorry about that. [cousin.fname] is out, so I was just lounging around."
            the_person "Anyways, I'm glad you stopped by!"

    elif the_person.effective_sluttiness() < 40:
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] jumps when she notices you, turning her body away to hide the view."
        the_person "Oh, one second, I... Oh, it's just you [the_person.mc_title]! I nearly had a heart attack!"
        $ the_person.draw_person()
        "She laughs and relaxes, turning back to face you."
        mc.name "Sorry [the_person.title], I didn't mean to scare you."
        the_person "It's not your fault, I was scared I had left the door unlocked is all. [cousin.fname] is out, so I'm not dressed for company."
        the_person "You don't mind, do you? I can go throw something on."
        menu:
            "Tell her to stay":
                mc.name "Not at all, you're looking good."
                "[the_person.possessive_title!c] smiles and pats you playfully on the shoulder."
                the_person "Oh, stop. I'm just so glad you stopped by!"

            "Tell her to get dressed":
                mc.name "Might be a good idea, in case [cousin.fname] comes home."
                the_person "Good point, that would be hard to explain..."
                the_person "I'll be back in a second!"
                $ clear_scene()
                $ the_person.apply_planned_outfit()
                "[the_person.possessive_title!c] hurries into her bedroom."
                "After a short wait she's back again."
                $ the_person.draw_person()
                the_person "Now, I'm so glad you stopped by!"

    else:
        "She smiles when she notices you."
        the_person "Oh, hey there [the_person.mc_title]. Just lock the door behind you, okay?"
        the_person "I wouldn't want anyone else walking in on me in my undies."
        "You lock the door again and step inside."
        the_person "I'm so happy you stopped by!"

    $ the_person.set_event_day("home_lingerie")
    call talk_person(the_person) from _call_talk_person_1
    return

label cousin_home_panties_label(the_person):
    $ the_person.outfit.strip_to_underwear()
    $ the_person.draw_person(position = "sitting")
    $ mc.change_locked_clarity(10)
    "You open the door to [the_person.possessive_title]'s room. She's sitting on her bed in her underwear, browsing her phone."
    if the_person.effective_sluttiness("underwear_nudity") < 10 or the_person.has_taboo("underwear_nudity"):
        "She looks up and glares at you."
        the_person "Hey, have you heard of knocking?"
        mc.name "I was..."
        "She cuts you off."
        the_person "I'm not dressed, you idiot! Get out!"
        $ mc.change_location(aunt_apartment)
        $ clear_scene()
        "[the_person.title] chucks a pillow at you. You step back and close the door."
        "You wait a moment, then shout through the door."
        mc.name "Can I come in yet?"
        the_person "Are you still out there? Ugh..."
        if the_person.effective_sluttiness("underwear_nudity") >= 10:
            the_person "Fuck it, just come in."
            $ mc.change_location(cousin.home)
            $ the_person.draw_person(position = "sitting")
            "You open the door. [the_person.possessive_title!c] never even moved from the bed."
            $ the_person.break_taboo("underwear_nudity")
            the_person "Just don't fucking stare, and don't get cum on my stuff if you're going to jizz your pants."
        else:
            $ the_person.change_happiness(-5)
            $ the_person.apply_planned_outfit()
            "You hear [the_person.possessive_title]'s bed creak, then her shuffle around her room for a moment."
            the_person "Alright dweeb, come in and say what you have to say."
            $ mc.change_location(cousin.home)
            $ the_person.draw_person()

    elif the_person.effective_sluttiness() < 40:
        "She looks up and glares at you."
        the_person "Hey, have you heard of knocking?"
        mc.name "I was..."
        "She cuts you off."
        the_person "I bet you were hoping for this, right? To see me in my panties?"
        if not the_person.tits_available:
            the_person "Maybe you even thought you'd see my tits? My big, juicy, naked tits?"
            "She laughs sharply."
        else:
            the_person "Probably the closest you can get to seeing a real girl naked."
        the_person "Whatever, I don't even care. Just don't get cum on my stuff if you're going to jizz your pants."
        pass
    else:
        "She looks up at you and sighs."
        the_person "Hey, have you heard of knocking?"
        mc.name "I was..."
        "She cuts you off."
        the_person "Whatever. What do you want?"

    $ the_person.set_event_day("home_panties")
    call talk_person(the_person) from _call_talk_person_30
    return

label sister_go_shopping_label(the_person): #TODO: Hook this up as an on_enter event in her room.
    $ the_person.change_location(mall)
    $ the_person.draw_person()
    "You nearly run into [the_person.title] as you open the door to her room."
    $ trigger_date = False
    if the_person.love < 10:
        the_person "Oh! Hey [the_person.mc_title], I was just heading out."
        "She pushes past you and closes the door to her room behind her."
        the_person "Tell [mom.fname] I'm at the mall if she needs me. See ya later!"
        "[the_person.possessive_title!c] hurries past you and out of the house."
    elif the_person.love < 30:
        the_person "Oh! Hey [the_person.mc_title], I was just heading to the mall."
        "She pushes past you and closes the door to her room behind her."
        menu:
            "Ask to join {image=time_advance}":
                mc.name "That sounds like fun. Mind if I tag along?"
                the_person "You really want to come on a shopping trip with your sister? Man, you must be {i}booooooored{/i}!"
                "[the_person.possessive_title!c] smirks and shrugs."
                $ the_person.change_obedience(-1)
                the_person "I guess you can come with me though. I might need someone to carry my things!"
                $ trigger_date = True

            "Say goodbye":
                mc.name "Alright, have fun out there."
                the_person "Tell [mom.fname] where I am if she needs me, okay? See ya later!"
                "[the_person.possessive_title!c] hurries past you and out of the house."

    else:
        the_person "Oh, you have perfect timing [the_person.mc_title]!"
        "She grabs your hand and pulls you into the hallway, closing the door to her room behind her."
        the_person "I was going to head to the mall, but it's always more fun shopping with a friend."
        the_person "Wanna come with me?"
        menu:
            "Go shopping":
                mc.name "Sure, that sounds like fun."
                "[the_person.possessive_title!c] smiles and nods in agreement."
                $ the_person.change_happiness(5)
                $ trigger_date = True

            "Not right now":
                mc.name "Sorry [the_person.title], I'm busy right now actually."
                the_person "Aww, alright. I've got to get going, see ya later!"
                "[the_person.possessive_title!c] hurries past you and out of the house."


    if trigger_date:
        "You and [the_person.possessive_title] head downtown, to the largest shopping mall around."
        call shopping_date_intro(the_person, skip_intro = True) from _call_shopping_date_intro

    #TODO: Have a version of this event for Mom
    #TODO: Have a version where both Lily and Mom go shopping together.
    #TODO: Have a random event where Lily and Mom have already _gone_ shopping, and they want to show you what they bought.
    return

label mom_go_shopping_label(the_person):
    $ the_person.change_location(mall)
    $ the_person.draw_person()
    the_person "Oh, hello [the_person.mc_title]. I was just about to head out and do some shopping."
    $ trigger_date = False
    if the_person.love < 10:
        the_person "I might be back late, but there's dinner in the fridge. All you need to do is warm it up."
        the_person "Take care of your sister, and call me if you need me."
        $ the_person.draw_person(position = "walking_away")
        "She smiles and waves goodbye as she heads for the front door."

    elif the_person.love < 30:
        the_person "I might be back late, but there's dinner in the fridge. All you need to do is warm it up."
        menu:
            "Ask to join":
                mc.name "You know, I have some shopping to do too. Would you like some company?"
                "[the_person.possessive_title!c] smiles and puts her hand on her chest."
                $ the_person.change_stats(obedience = -1, love = 1)
                the_person "Oh, you're so sweet. Of course you can, if you don't mind being seen with your Mom out in public."
                the_person "I'll try not to embarrass you if we run into someone you know."
                $ trigger_date = True

            "Say goodbye":
                mc.name "Okay, have fun [the_person.title]."
                the_person "Take care of your sister, and call me if you need me."
                $ the_person.draw_person(position = "walking_away")
                "She smiles and waves goodbye as she heads for the front door."

    else:
        the_person "You have such good taste in clothing, would you like to come along and give me some advice?"
        the_person "If you aren't too embarrassed to be seen shopping with your mom, of course."
        menu:
            "Go shopping {image=time_advance}":
                mc.name "I've got some shopping to do of my own. Sure, I'll come along."
                "She smiles happily."
                the_person "It's always nice when we get to spend time together, just the two of us."
                $ trigger_date = True

            "Not right now":
                mc.name "Sorry [the_person.title], I've made plans for the afternoon already."
                the_person "Of course, you're a busy boy! Well then, there's dinner in the fridge."
                the_person "I'll be back later tonight. Take care of your sister."
                $ the_person.draw_person(position = "walking_away")
                "She smiles and waves goodbye, heading for the front door."

    if trigger_date:
        "You and [the_person.possessive_title] head downtown, to the largest shopping mall around."
        call shopping_date_intro(the_person, skip_intro = True) from _call_shopping_date_intro_1
    else:
        $ clear_scene()
    return

label mom_fuck_during_housework_label(the_person):
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.outfit.add_feet(thigh_highs.get_copy(), colour_red)
    $ the_person.outfit.add_feet(high_heels.get_copy(), colour_red)
    $ add_mom_outfit_coloured_apron(the_person)
    $ the_person.draw_person(position = "back_peek")
    "You find [the_person.possessive_title] in the kitchen, completely nude except for her apron. She's been doing this more and more lately."
    the_person "Hi [the_person.mc_title], I hope you've had a great day. Dinner should be ready soon!"
    "She turns back, wiggling her butt as she works. Her ass is supple. You are tempted to do something with it while she works..."
    menu:
        "Spank her\n{menu_yellow}May increase submissiveness{/menu_yellow}" if the_person.spank_level <= 4: #chance to increase her submissiveness based on if she orgasms and if she is currently suggestible.
            "The swaying of [the_person.title]'s ass is hypnotic. It is [the_person.ass_spank_description]"
            mc.name "I don't mind you dressing like this, [the_person.title], but it is kind of naughty."
            "You step up behind her and start to run your hand along her hips."
            the_person "Ah, well, it definitely makes me feel kind of naughty..."
            call fuck_person(the_person, start_position = spanking, start_object = make_table()) from _call_spank_mommy_during_housework_01
            $ the_report = _return
            if the_person.opinion.being_submissive < 2:
                if renpy.random.randint(0,100)< (the_report.get("girl orgasms", 0) * 10) + the_person.suggestibility:  #Odds for improvement are 10% per orgasm plus suggestibility.
                    the_person "Oh... it's good to know I have a son who will discipline me if I get too naughty!"
                    $ the_person.increase_opinion_score("being submissive")
            elif not the_person.can_be_spanked:
                $ the_person.unlock_spanking()
                the_person "Oh god honey, it's amazing knowing I have such a good son, who keeps his naughty mother in line!"
                "She really seemed to enjoy her spanking. Maybe you should work it into your normal foreplay..."

            $ the_person.draw_person(position = "back_peek")
            "It takes [the_person.possessive_title] a few moments, but she gets back to work, making dinner for the family."

        "Spank her\nToo recently spanked (disabled)" if the_person.spank_level > 4:
            pass

        # taken from KiNASuki Mod
        "Fuck her" if mc.energy > 80 and not the_person.has_taboo("vaginal_sex"):
            "You hangs around the kitchen watching [the_person.possessive_title] working until she bends over the counter and starts to chop up some vegetables."
            $ the_person.draw_person(position = "standing_doggy")
            if the_person.vagina_available:
                "You steal a few glances over at [the_person.possessive_title]'s exposed pussy. It glistening wet and tempting you ever so slightly with every moves she made."
                mc.name "I think I'll take my {i}dinner{/i} now."
                "You slowly reach down and start to slowly caress her cunt."
            else:
                "You steal a glance over at [the_person.possessive_title]'s [the_person.outfit.get_lower_top_layer.display_name] as she is bent over. It's a bit wet."
                mc.name "I think I take my {i}dinner{/i} now."
                "You slowly reach down and start to slowly rub her pussy through her [the_person.outfit.get_lower_top_layer.display_name]."
            $ the_person.change_arousal(10)
            "[the_person.possessive_title!c] stifles a moan, she pushes her hips back against you as you continue to stroke her."
            the_person "Mmmmmm... as you wish, well... how do you want your dinner served?"
            if had_family_threesome():
                the_person "But be quick, your sister would likely want to join in."
            else:
                the_person "But be quick! I don't want your sister to catch us."

            if the_person.vagina_visible:           #If it's available no need to strip.
                "You quickly pull your cock out and line it up with her wet slit."
            else:                                              #Otherwise, strip her down.
                "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy.."
                $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
                "With her pussy finally exposed you waste no time. You quickly pull your cock out and line it up with her wet slit."
            "You thrust yourself inside her slowly. Her pussy accepts your length easily, well lubricated from her own horniness."
            $ the_person.change_arousal(15)
            $ mc.change_arousal(15)
            $ the_person.break_taboo("condomless_sex")
            call fuck_person(the_person, start_position = standing_doggy, start_object = make_table(), skip_intro = True, self_strip = False, skip_condom = True) from _call_fuck_mommy_during_housework_01
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title!c] is happy. She knows that even while preparing dinner, you may come and fuck her at any time."
            else:
                "[the_person.possessive_title!c] remains silent. She knows that even while preparing dinner, you may come use her for your pleasure at any time."

            "Clearly, in her current attire, it will be obvious what [the_person.possessive_title] has been up to. You look at the state of dinner. It's almost done."
            mc.name "Go. I'll finish preparing dinner."
            the_person "Ahhh... okay... thank you honey!"
            $ clear_scene()
            $ the_person.apply_planned_outfit()
            "[the_person.title] leaves the room, leaving you alone to set up dinner. You start portioning out plates."

        "Let her work":
            "You stomach growls. As much as you would like to take advantage of [the_person.title], you decide to let her work on dinner instead."

    return


#TODO: Add a Mom+Lily shopping haul review (or maybe a Mom+Aunt? They should get more screen time together)
#TODO: You come home and find that Mom/Lily/Aunt have just gotten back from the mall, and they have stuff to show you.
#TODO: Basic option to review their outfits, plus ability to have them strip down/dance/tease you while you watch.
#TODO: Maybe do that as part of the expanded Lily/Mom storyline stuff. I want more context aware stuff from them as well.

#TODO: Some late night events with Lily or Mom masturbating (LR1 vibes)
#TODO: Lily's bedroom search - maybe a generic search for everyone else?
# |-> Roll Gabrielle's room search into this, where you find info about her part-time job
