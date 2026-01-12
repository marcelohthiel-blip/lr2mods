label shower_0(the_person):
    $ sluttiness = 0 + renpy.random.randint(0,19)
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_0
    "[the_person.title] reaches for the shampoo, applying it to her hair with practiced efficiency, her movements lacking the enthusiasm that often accompanies more indulgent self-care routines."
    "As she lathers soap over her body, [the_person.title]'s gestures seem automatic, devoid of any particular pleasure."
    "There is a sense of detachment in her actions, as if the shower is a task to be completed rather than a moment to be relished."
    "Her [the_person.tits_description] and [the_person.pubes_description] mound are there, but even the voyeuristic thrill is barely enough to counteract the boredom of her actions."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "Her hands move mechanically, following the well-worn routine of cleansing without the added embellishments of mindfulness."
    "In this mundane act of self-care, [the_person.title]'s demeanor remains composed and unremarkable."
    "The shower, serving more as a functional necessity than a luxurious retreat."
    call shower_exit(the_person, sluttiness) from _call_shower_exit_0
    $ scene_manager.clear_scene()
    return

label shower_20(the_person):
    $ sluttiness = 20 + renpy.random.randint(0,19)
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_20
    call shower_hates_masturbation(the_person, sluttiness) from _call_shower_hates_masturbation_200
    return

label shower_hates_masturbation(the_person, sluttiness):
    $ body_description = get_body_description(the_person)
    $ body_word = get_body_word(the_person)
    if renpy.random.randint(0,1) == 0:
        "[the_person.title] reaches for a bottle of lavender-scented shower gel, applying it to a soft loofah with a gentle touch."
        "She closes her eyes briefly, breathing deeply as if savouring the smell before resuming her routine."
        "The water droplets cascade down [the_person.title]'s body, carrying away the suds and leaving her skin glistening." 
        "Her movements in the shower are unhurried, as if she is taking a moment to appreciate the sensation of warm water against her skin."
    else:
        "With a loofah in hand, she applies lavender-scented shower gel with a gentle touch, savouring the fragrance."
        "Her movements are deliberate, as if taking a moment to appreciate the warmth against her skin."
        "Water droplets trace down [the_person.title]'s body, carrying away suds and leaving her skin glistening."
        "Her actions in the shower are unhurried, a pause for self-appreciation before resuming the routine."
    $ scene_manager.update_actor(the_person, position = "stand4")
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(5)
    "Her pace gives you time to observe her [the_person.tits_description] as she squeezes them back and forth, rubbing her hands over every inch of them."
    $ scene_manager.update_actor(the_person, position = "against_wall")
    $ mc.change_arousal(5)
    $ mc.change_locked_clarity(5)
    "When she runs her hand along her [the_person.pubes_description] slit you have time to imagine what it would be like to have your hand there, feeling the wetness from within."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "As she slowly turns to ensure every angle gets rinsed you drink in the sight of her [body_description] including a lingering view of her [body_word] ass."
    if sluttiness > 39:
        "It is a real shame that [the_person.title] hates masturbation. If you could fine a way to shift her opinion her showers would be more exciting."
    $ del body_description
    $ del body_word
    call shower_exit(the_person, 30) from _call_shower_exit_hate
    $ scene_manager.clear_scene()
    return

label shower_40(the_person):
    $ sluttiness = 40 + renpy.random.randint(0,9)
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_40
    if the_person.opinion.masturbating < -1:
        call shower_hates_masturbation(the_person, sluttiness) from _call_shower_hates_masturbation_40
    else:
        "She lets out a moan as the hot water cascades over her body, washing away the day's stress along with any lingering shame or embarrassment about what comes next."
        if renpy.random.randint(0,1):
            "Using every part of her supple form, [the_person.title] massages soap between her fingers and across her skin, letting her hands glide lower and lower until finally they reach the apex of her desire."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            $ scene_manager.update_actor(the_person, position = "against_wall")
            "She bites down on her bottom lip as she focuses intently on bringing herself pleasure, rubbing and stroking until an orgasm overtakes her in waves of bliss."
        else:
            "Using every part of her supple form, [the_person.title] massages soap between her fingers and across her skin, letting her hands glide lower and lower until finally they reach the apex of her thighs."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            $ scene_manager.update_actor(the_person, position = "against_wall")
            "She parts them slightly, revealing the damp curls between as she begins to rub herself in circles, moaning into the steamy air."
            "Her hips buck and grind against her hands as pleasure washes over her like a wave; it's clear that this is no mere shower for cleanliness."
            "Her movements become more frantic now, fingers digging deeper with each stroke until finally, her body tenses and shudders."
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(10)
        "[the_person.title] cries out in ecstasy, arching her back and pressing forward into the spray of water as she comes hard - waves of relief coursing through every fiber of her being."
        call shower_exit(the_person, sluttiness) from _call_shower_exit_40
        $ scene_manager.clear_scene()
    return

label shower_50(the_person):
    $ sluttiness = 40 + renpy.random.randint(0,9)
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_50
    if the_person.opinion.masturbating < -1:
        call shower_hates_masturbation(the_person, sluttiness) from _call_shower_hates_masturbation_50
    else:
        $ body_word = get_body_word(the_person)
        if renpy.random.randint(0,1) == 0:
            "Her [the_person.hair_description] is tied back into a loose ponytail, revealing her [body_word] neck and shoulders which glisten with beads of water."
            "Her [the_person.tits_description] are topped by nipples that harden under the spray."
            #if
            "A thin trail of [the_person.pubes_description] runs from her belly button down between her legs where it disappears beneath the bubbles."
            $ mc.change_arousal(5)
            $ mc.change_locked_clarity(5)
            "[the_person.title] begins to soap herself up slowly, paying special attention to her breasts and stomach before moving lower."
            $ scene_manager.update_actor(the_person, position = "cowgirl")
            "She squats down low, spreading her legs wide apart, exposing her wet pussy."
            "Her fingers dip into the warm water between her legs, spreading it around her opening."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            "Moaning softly, she reaches behind herself and inserts two fingers deep into her tight hole."
            "She starts fucking herself slowly, her fingers going deeper with each thrust."
            "Her other hand moves between her legs, rubbing her clit roughly as she continues fucking herself with her fingers."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            "Her body shudders violently, and she cries out in ecstasy as she climaxes."
            "After several minutes of intense orgasms, she pulls her fingers from her pussy, rinsing them clean in the water." 
        else:
            "[the_person.title] squirts a generous amount of body wash into her cupped palm and rubs it between her fingers."
            $ scene_manager.update_actor(the_person, position = "against_wall")
            "She leans back against the cool tile wall and starts to massage herself slowly at first; circling her clit with her thumb while using a finger to probe deeper inside her [the_person.pubes_description] pussy."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            "As she continues to work herself up, she begins moving faster, pressing harder and swifter until tiny droplets of water fly from her wet hair."
            "The sight is mesmerizing: her [the_person.tits_description] bobbing with each thrust of her hand, her [body_word] stomach flexing as she arches her back in pleasure."
            "Her other hand slides downward, teasing at her entrance as if preparing to penetrate herself further."
            "But instead, she brings it back up to cup one breast, pinching a rosy nipple roughly between her fingers."
            "Her pace quickens again, hips rocking back and forth in time with her movements."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            "Soon enough, her entire body trembles with the intensity of it, and finally, she lets out a primal scream that echoes throughout the bathroom."
            "Afterward, she lays there in the water for a moment longer, limp and spent."
        call shower_exit(the_person, sluttiness) from _call_shower_exit_50
        $ scene_manager.clear_scene()
    return

label shower_60(the_person):
    $ sluttiness = 60 + renpy.random.randint(0,19)
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_60
    if the_person.opinion.masturbating < -1:
        call shower_hates_masturbation(the_person, sluttiness) from _call_shower_hates_masturbation_60
    else:
        $ body_word = get_body_word(the_person)
        "Slowly but surely, [the_person.title] begins exploring every inch of her skin with practiced precision."
        "Starting at her neck then moving downwards towards her [the_person.tits_description] before heading further south towards her [body_word] thighs."
        $ mc.change_arousal(5)
        $ mc.change_locked_clarity(5)
        "She traces delicate patterns across sensitive areas such as her inner thighs while keeping one eye trained firmly on the mirrored wall opposite her."
        if the_person.get_opinion_score("masturbating") < 1:
            "With each passing moment, [the_person.title] becomes increasingly bolder pressing her soft palms directly against her [the_person.pubes_description] pussy."
            "Finally reaching peak levels of arousal, [the_person.title] closes her eyes briefly."
            "When they open she stares at the removable shower head above her head."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            $ scene_manager.update_actor(the_person, position = "against_wall")
            "Reaching up to pull it down, she aims it directly at her crotch, letting its powerful spray pulsate forcefully against her already aching flesh."
            "Caught up entirely in this euphoria-inducing act, [the_person.title] arches back against the tiles trembling under waves of pleasure"
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            "[the_person.title] lets loose a primal scream that reverberates throughout the small space around her."
            "Her limbs flail uncontrollably as she experiences several blissful orgasms brought about by the combination of water and self-stimulation."
            "Each climax leaves her shaking uncontrollably."
        else:
            "With a mischievous glint in her eye, [the_person.title] reaches for the detachable shower head and gives it an experimental twist."
            "To your shock (and arousal), she easily removes it from its housing on the wall, revealing a long, flexible hose with a pointed nozzle at one end."
            "She turns the water on full blast before positioning herself directly beneath the spray; hot droplets splatter against her skin as she takes aim."
            "Then, slowly and deliberately, she lowers the nozzle towards her dripping wet pussy."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            $ scene_manager.update_actor(the_person, position = "against_wall")
            "The tip of the shower head presses gently against her [the_person.pubes_description] folds, causing her to let out a moan of pleasure as it massages her sensitive flesh."
            "You can see through the rushing water that her fingers are buried deep inside too."
            "The high pressure stream hits her clit relentlessly now, driving her wild with need."
            "Her hips buck violently back and forth under the force of it."
            "Her breath comes in ragged gasps as she loses control entirely, letting out animalistic sounds of pleasure that echo off the tiled walls."
            $ mc.change_arousal(10)
            $ mc.change_locked_clarity(10)
            "Finally, after what feels like an eternity, [the_person.title]'s whole body goes rigid and she cries out hoarsely."
            "Her muscles convulse as wave after wave of orgasmic release washes over her, and she collapses against the shower wall with a contented sigh."
        $ scene_manager.update_actor(the_person, position = "stand5")
        "After what feels like ages [the_person.title] finally manages to regain some semblance of composure, enough to hang up the shower head."
        $ scene_manager.update_actor(the_person, position = "back_peek")
        "Standing under the normal cascade of water, [the_person.possessive_title] rinses off her body, including the newest layer of sweat and other fluids."
        call shower_exit(the_person, sluttiness) from _call_shower_exit_60
        $ scene_manager.clear_scene()
    return

label shower_80(the_person):
    $ sluttiness = 80 + renpy.random.randint(0,19)
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_80
    if the_person.opinion.masturbating < -1:
        call shower_hates_masturbation(the_person, sluttiness) from _call_shower_hates_masturbation_80
    else:
        $ body_word = get_body_word(the_person)
        $ body_description = get_body_description(the_person)
        menu:
            "View anal variant (disabled)" if the_person.get_opinion_score("anal sex") < 1:
                pass
            "View anal variant" if the_person.get_opinion_score("anal sex") > 0:
                "In the warm embrace of her shower, [the_person.title] stands before a cool tile wall."
                "She squirts some body wash onto her palm and begins to massage it between her fingers."
                $ scene_manager.update_actor(the_person, position = "doggy")
                "She lowers herself down until she's kneeling on the floor with her [body_word] ass up in the air."
                $ mc.change_arousal(10)
                $ mc.change_locked_clarity(10)
                "Gingerly, she reaches back and presses two fingertips against her anus."
                "The tight muscles resist at first but soon give way under the pressure, allowing her digits to slip inside."
                "A shiver runs through her entire body as she moans softly, slowly working her fingers deeper into her ass."
                "Her other hand moves up, cupping her [the_person.tits_description] in her palm and rolling the hardened nipple between her thumb and forefinger."
                "The contrast of rough skin against sensitive flesh sends shockwaves of pleasure coursing through her veins."
                "After a few moments of this, she reaches behind her, grabs hold of the small bottle of body wash and guides it towards her aching opening."
                $ mc.change_arousal(10)
                $ mc.change_locked_clarity(10)
                "With grunts of pleasure, [the_person.title] begins thrusting her hips back, fucking herself on the makeshift dildo as she alternates between fondling her [the_person.tits_description] and [the_person.pubes_description] clit with abandon."
                "Her moans echo through the tiled bathroom, muffled by water streaming from the shower head above."
                $ mc.change_arousal(10)
                $ mc.change_locked_clarity(10)
                "Soon enough, she reaches climax - teeth gritted against ecstasy. Her whole body convulses, her orgasm rippling through her core like wildfire."
                "As the waves subside, she collapses forward onto her knees, panting heavily and covered in sweat."
            "View vaginal variant":
                if the_person.get_opinion_score("masturbating") < 1:
                    "[the_person.title] twists apart a small, slender shampoo bottle, revealing a surprisingly phallic shape."
                    "Smirking to herself, she squirts a liberal amount of soap onto her hands and begins to lather up, paying special attention to her [body_word] curves."
                    "As she massages the suds over her [the_person.tits_description] and stomach, [the_person.title] seems to flush with arousal."
                    $ mc.change_arousal(10)
                    $ mc.change_locked_clarity(10)
                    $ scene_manager.update_actor(the_person, position = "against_wall")
                    "Moving lower, she spreads her legs slightly, coating the outside of her thighs before slipping a soapy finger between them to rub her [the_person.pubes_description] mound."
                    "Gasping, she rubs her clitoris in slow, circular motions, her fingers dancing over the sensitive nub."
                    "The sound of the running water provides the perfect cover for her quiet moans as [the_person.title] inserts two fingers into her waiting hole."
                    "Her other hand continues to caress her [the_person.tits_description], applying just the right amount of pressure to send shockwaves of pleasure throughout her body."
                    "Emboldened by the privacy of the steamy shower, [the_person.title] brings the shampoo bottle into play."
                    $ mc.change_arousal(10)
                    $ mc.change_locked_clarity(10)
                    "Lubricating its tip with soap, she carefully guides it into her eager pussy, feeling it stretch and yield to the intrusion."
                    "With slow, methodical strokes, she thrusts the bottle in and out, relishing the unique sensation of fullness it provides."
                    "Faster and faster her hips move, desperately seeking release."
                    "Her breath comes in ragged gasps as her orgasm draws near, until finally, a loud cry echoes through the confined space."
                    $ mc.change_arousal(10)
                    $ mc.change_locked_clarity(10)
                    $ scene_manager.update_actor(the_person, position = "standing_doggy")
                    "She crumples forward against the cool tile wall behind her, her [body_description] wracked by wave after wave of mind-shattering orgasm."
                    "As the last tremors subside, [the_person.title] slowly lowers herself back onto the shower chair, panting heavily."
                else:
                    "[the_person.title] steps into the warm embrace of the shower, letting out a contented sigh as she leans against the cool tile wall."
                    "She squirts some body wash onto her palm and begins to massage it between her fingers."
                    $ scene_manager.update_actor(the_person, position = "kneeling1")
                    "Carefully setting down the bottle on the floor beside her, she lowers herself down until she's sitting with her legs spread wide apart."
                    $ mc.change_arousal(10)
                    $ mc.change_locked_clarity(10)
                    "Gingerly at first, then more boldly, she guides the rounded base of the body wash bottle towards her [the_person.pubes_description] opening, pressing forward until it slides easily inside."
                    "A shiver runs through her entire body at the feel of it filling her up like this; so full that every breath comes out ragged and unsteady."
                    "She starts rocking back and forth slowly, finding a rhythm that feels good against her clit and the bottle nestled deep inside her."
                    "Her hips begin to move faster now, grinding against the smooth plastic surface of the bottle as if seeking release."
                    "Water cascades over her [the_person.tits_description], running trails down her stomach and thighs where they meld together in a slippery mess."
                    $ mc.change_arousal(10)
                    $ mc.change_locked_clarity(10)
                    "With one final thrust, [the_person.title] cries out in ecstasy around the foreign object lodged deep inside her." 
                    "Waves of pleasure roll through her body, making her limbs drop weakly."
                    "When she finally manages to catch her breath again, she looks down at herself."
                    "She pulls the bottle out slowly, reluctantly, and reaches between her legs to clean up any residual mess before standing once more under the spray of water."
        "The water continues to pour over her, washing away any evidence of her recent indulgence."
        $ del body_description
        $ del body_word
        call shower_exit(the_person, sluttiness) from _call_shower_exit_80
        $ scene_manager.clear_scene()
    return

label shower_90(the_person):
    $ sluttiness = 90
    $ scene_manager = Scene()
    call shower_enter(the_person, sluttiness) from _call_shower_enter_90
    if the_person.opinion.masturbating < -1:
        call shower_hates_masturbation(the_person, sluttiness) from _call_shower_hates_masturbation_90
    else:
        $ body_word = get_body_word(the_person)
        $ body_description = get_body_description(the_person)
        "[the_person.title] lets out a contented groan as the warm water cascades down over her skin."
        "Her gaze drifts to the side where you notice a suction cup dildo mounted on the wall."
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(10)
        "Carefully positioning herself in front of it, she leans forward and presses its smooth surface against her [the_person.pubes_description] opening."
        $ scene_manager.update_actor(the_person, position = "standing_doggy")
        "There's resistance at first but then slides inside her."
        "A shiver runs through her entire body as she begins rocking her hips back and forth, fucking herself on the mounted dildo."
        "Water streams down across her [the_person.tits_description] and stomach, adding another layer of wetness to their already slippery state."
        "As she picks up speed, her movements become less controlled; grunts and moans filling the air as she loses herself entirely in the moment."
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(10)
        "Her fingers dig into the porcelain edge of the tub for purchase, as she pushes harder against the dildo embedded deep inside her."
        "Finally, it hits her like a tidal wave - an orgasm so powerful that she cries out into the steamy air."
        $ mc.change_arousal(10)
        $ mc.change_locked_clarity(10)
        "Her body shudders uncontrollably as waves of release wash over her, leaving her spent as she slips off the wall mounted dildo."
        $ scene_manager.update_actor(the_person, position = "sitting")
        "With a satisfied sigh, [the_person.title] collapses onto the shower bench; panting heavily."
        "The water continues to pour over her, washing away any evidence of her recent indulgence."
        $ del body_description
        $ del body_word
        call shower_exit(the_person, sluttiness) from _call_shower_exit_90
        $ scene_manager.clear_scene()
    return

label shower_enter(the_person, sluttiness): #enter room, strip, enter shower
    $ home_bathroom.show_background()
    $ scene_manager = Scene()
    $ body_description = get_body_description(the_person)
    $ body_word = get_body_word(the_person)
    $ temp_colour = None
    $ temp_outfit = None
    $ overcoat = None
    if renpy.random.randint(60, 120) < sluttiness:
        $ temp_outfit = Outfit("Nude")
    else:
        $ sluttiness_modifier = sluttiness - the_person.sluttiness
        $ stored_outfit = None
        if day%7 < 5 and (the_person.has_role(generic_student_role) or the_person.is_employee):
            if the_person.has_role(generic_student_role):
                $ temp_outfit = limited_university_wardrobe.decide_on_outfit(the_person, sluttiness_modifier = sluttiness_modifier)
            else:
                $ temp_outfit = the_person.primary_job.wardrobe.decide_on_outfit(the_person, sluttiness_modifier = sluttiness_modifier)
        else:
            $ temp_outfit = the_person.decide_on_outfit(sluttiness_modifier = sluttiness_modifier)
        $ del sluttiness_modifier
        if temp_outfit:
            $ overcoat = next((x for x in temp_outfit.upper_body if x.layer == 4), None)
        if overcoat:
            $ temp_outfit.remove_clothing(overcoat)
        if renpy.random.randint(50, 100) < sluttiness:
            $ temp_outfit.strip_to_underwear()
        while len(temp_outfit.feet) > 0:
            $ temp_bottom = temp_outfit.feet[0]
            $ temp_outfit.remove_clothing(temp_bottom)
    $ temp_top = None
    $ temp_bottom = None
    $ temp_bra = None
    $ temp_panties = None
    if temp_outfit.get_upper_top_layer:
        $ temp_top = temp_outfit.get_upper_top_layer
    if temp_outfit.get_bra():
        $ temp_bra = temp_outfit.get_bra()
    if temp_outfit.get_lower_top_layer:
        $ temp_bottom = temp_outfit.get_lower_top_layer
    if temp_outfit.get_panties():
        $ temp_panties = temp_outfit.get_panties()
    if temp_top == temp_bra:
        $ temp_top = None
    if temp_panties and temp_panties.is_extension:
        $ temp_panties = None
    if temp_bottom == temp_panties or (temp_bottom and temp_bottom.is_extension):
        $ temp_bottom = None
    $ scene_manager.add_actor(the_person, temp_outfit)
    if renpy.random.randint(0,3) == 0:
        "[the_person.title] walks into the bathroom, the soft light casting a warm glow on the tiled floor."
    elif renpy.random.randint(0,2) == 0:
        "[the_person.title] enters the bathroom, the soft light casting a subtle glow on the tiled floor."
    elif renpy.random.randint(0,1) == 0:
        "[the_person.title] enters her bathroom, the soft glow of morning light illuminating the space."
    else:
        "[the_person.title] enters the bathroom, where the morning light casts a soft glow."
    if temp_top:
        $ temp_colour = clothing_colour_name(temp_top.colour)
        if temp_bottom:
            if sluttiness < 20:
                "Clad in a [temp_colour] [temp_top.display_name] and [temp_bottom.display_name], she exudes comfort."
            elif sluttiness < 40:
                if clothing_plural(temp_bottom):
                    "She wears a loose-fitting, [temp_colour] [temp_top.display_name] that hangs effortlessly over her frame, paired with well-worn [temp_bottom.display_name] that cling comfortably to her legs."
                else:
                    "She wears a loose-fitting, [temp_colour] [temp_top.display_name] that hangs effortlessly over her frame, paired with a well-worn [temp_bottom.display_name] that clings comfortably to her waist."
                "Her attire suggests a balance between comfort and simplicity."
            else:
                if clothing_plural(temp_bottom):
                    "She wears a simple, [temp_top.display_name] paired with [temp_bottom.display_name] that cling to her legs."
                else:
                    "She wears a simple, [temp_top.display_name] paired with a [temp_bottom.display_name] that hugs her waist."
        else:
            if sluttiness < 20:
                "She wears a loose-fitting, [temp_colour] [temp_top.display_name] that hangs effortlessly over her frame, and clings comfortably to her waist."
            elif sluttiness < 40:
                "She wears a form-fitting, [temp_colour] [temp_top.display_name] that accentuates the gentle curves of her frame, and hugs her hips gracefully."
            else:
                "She wears a skimpy, [temp_top.display_name] that clings to her legs and presents the cleavage of her [the_person.tits_description]."
        if renpy.random.randint(0,3) == 0:
            "As [the_person.title] closes the bathroom door behind her, she begin to undress with a casual grace."
        elif renpy.random.randint(0,2) == 0:
            "Closing the door behind her, [the_person.title] begins to undress with a quiet confidence."
        elif renpy.random.randint(0,1) == 0:
            "Closing the door behind her, [the_person.title] begins to undress with a certain deliberate grace."
        else:
            "Closing the door behind her, [the_person.title] undresses deliberately, revealing her smooth skin."
        if temp_bottom:
            $ scene_manager.draw_animated_removal(the_person, temp_top)
            if temp_bra:
                $ temp_colour = clothing_colour_name(temp_bra.colour)
                "The [temp_top.display_name] slips off her shoulders, revealing a simple [temp_colour] [temp_bra.display_name] underneath."
            else:
                "The [temp_top.display_name] slides off her shoulders, revealing smooth skin and her [the_person.tits_description]."
            $ scene_manager.draw_animated_removal(the_person, temp_bottom)
            if temp_panties:
                if clothing_plural(temp_bottom):
                    "[the_person.title] pulls down her [temp_bottom.display_name], peeling them off with a deliberate slowness that seems almost intentional."
                else:
                    "[the_person.title] pulls down her [temp_bottom.display_name], peeling it off with a deliberate slowness that seems almost intentional."
                "As she does so, it exposes the gentle curve of her [body_word] hips and the intricate lace of her [temp_panties.display_name]."
            else:
                if clothing_plural(temp_bottom):
                    "She unbuttons her [temp_bottom.display_name], allowing them to gently fall to the floor, exposing her [body_description] and [the_person.pubes_description] pussy."
                else:
                    "She unbuttons her [temp_bottom.display_name], allowing it to gently fall to the floor, exposing her [body_description] and [the_person.pubes_description] pussy."
        else:
            "Bending down, [the_person.title] grabs the hem of her [temp_top.display_name] and begins to slide it up her body."
            if temp_panties:
                $ temp_colour = clothing_colour_name(temp_panties.colour)
                if clothing_plural(temp_panties):
                    "Once she gets it high enough you get a view of her [temp_colour] [temp_panties.display_name] and the way they cling to her [body_word] hips."
                else:
                    "Once she gets it high enough you get a view of her [temp_colour] [temp_panties.display_name] and the way it clings to her [body_word] hips."
            else:
                $ mc.change_arousal(5)
                $ mc.change_locked_clarity(5)
                "Once she gets it high enough you see her [the_person.pubes_description] pussy in all it's glory. She's been walking around commando."
            $ scene_manager.draw_animated_removal(the_person, temp_top)
            if temp_bra:
                $ temp_colour = clothing_colour_name(temp_bra.colour)
                "Continuing higher her [body_description] comes into full view, that is until the [temp_colour] [temp_bra.display_name] that hugs her [the_person.tits_description]."
            else:
                $ mc.change_arousal(5)
                $ mc.change_locked_clarity(5)
                "Continuing higher her [body_description] comes into full view, including her [the_person.tits_description]."
        if renpy.random.randint(0,1) == 0:
            "As [the_person.title] continues undressing, she discards each piece of clothing with nonchalant ease."
        else:
            "[the_person.title]'s body carries a natural grace as she moves through the familiar ritual of undressing."
    elif temp_bottom:
        if sluttiness < 20:
            if clothing_plural(temp_bottom):
                "Clad in a pair of [temp_bottom.display_name], she exudes comfort."
            else:
                "Clad in a [temp_bottom.display_name], she exudes comfort."
        elif sluttiness < 40:
            if clothing_plural(temp_bottom):
                "She wears a well-worn set of [temp_bottom.display_name] that cling comfortably to her legs."
            else:
                "She wears a loose-fitting, [temp_bottom.display_name] that clings comfortably to her waist."
            "Her attire suggests a balance between comfort and simplicity."
        else:
            if clothing_plural(temp_bottom):
                "She wears a simple set of [temp_bottom.display_name] that cling to her legs."
            else:
                "She wears a simple [temp_bottom.display_name] that hugs her waist."
        $ scene_manager.draw_animated_removal(the_person, temp_bottom)
        if temp_panties:
            if clothing_plural(temp_bottom):
                "[the_person.title] pulls down her [temp_bottom.display_name], peeling them off with a deliberate slowness that seems almost intentional."
            else:
                "[the_person.title] pulls down her [temp_bottom.display_name], peeling it off with a deliberate slowness that seems almost intentional."
            "As she does so, it exposes the gentle curve of her [body_word] hips and the intricate lace of her [temp_panties.display_name]."
        else:
            $ mc.change_arousal(5)
            $ mc.change_locked_clarity(5)
            if clothing_plural(temp_bottom):
                "She unbuttons her [temp_bottom.display_name], allowing them to gently fall to the floor, exposing her [body_description] and [the_person.pubes_description] pussy."
            else:
                "She unbuttons her [temp_bottom.display_name], allowing it to gently fall to the floor, exposing her [body_description] and [the_person.pubes_description] pussy."
    if temp_bra:
        if not temp_top:
            if temp_panties:
                $ temp_colour = clothing_colour_name(temp_panties.colour)
                "It appears that she walked down the hall in just her underwear."
                if clothing_plural(temp_panties):
                    "A [temp_colour] [temp_bra.display_name] supports her breasts while a pair of [temp_panties.display_name] hug her waist."
                else:
                    "A [temp_colour] [temp_bra.display_name] supports her breasts while a [temp_panties.display_name] hugs her waist."
            else:
                $ temp_colour = clothing_colour_name(temp_bra.colour)
                "It appears that she walked down the hall in just her [temp_colour] [temp_bra.display_name]."
            if renpy.random.randint(0,3) == 0:
                "As [the_person.title] closes the bathroom door behind her, she begin to undress with a casual grace."
            elif renpy.random.randint(0,2) == 0:
                "Closing the door behind her, [the_person.title] begins to undress with a quiet confidence."
            elif renpy.random.randint(0,1) == 0:
                "Closing the door behind her, [the_person.title] begins to undress with a certain deliberate grace."
            else:
                "Closing the door behind her, [the_person.title] undresses deliberately, revealing her smooth skin."
        if temp_panties:
            $ scene_manager.draw_animated_removal(the_person, temp_bra)
            if the_person.skin == "white":
                "She reaches behind her back to unclasp her [temp_bra.display_name], letting it slide down her arms to reveal her [the_person.tits_description] adorned with pale pink nipples."
            elif the_person.skin == "tan":
                "She reaches behind her back to unclasp her [temp_bra.display_name], letting it slide down her arms to reveal her [the_person.tits_description] adorned with light brown nipples."
            else:
                "She reaches behind her back to unclasp her [temp_bra.display_name], letting it slide down her arms to reveal her [the_person.tits_description] adorned with nearly black nipples."
            $ scene_manager.draw_animated_removal(the_person, temp_panties)
            $ mc.change_arousal(5)
            $ mc.change_locked_clarity(5)
            "Then, with a seductive wiggle, she slips her [temp_panties.display_name] down over her hips, revealing her smooth legs and [the_person.pubes_description] pubic region."
        else:
            "Pulling the straps of her [temp_bra.display_name] over her shoulders, [the_person.title] starts to shimmy it down her body."
            $ mc.change_arousal(5)
            $ mc.change_locked_clarity(5)
            "This reveals her [the_person.tits_description], which jiggle enticingly as she works it down her torso and legs."
            "As she stands back up you get a lovely view of her [the_person.pubes_description] pubic mound."
    elif temp_panties:
        if not temp_top:
            $ temp_colour = clothing_colour_name(temp_panties.colour)
            if clothing_plural(temp_panties):
                    "It appears that she walked down the hall in just a pair of [temp_panties.display_name] that hug her waist."
            else:
                "It appears that she walked down the hall in just a [temp_panties.display_name] that hugs her waist."
            "Her [the_person.tits_description] on proud display if their were anyone (other than your camera) around to see."
            "Closing the door behind her, [the_person.title] undresses deliberately, revealing her smooth skin."
        $ scene_manager.draw_animated_removal(the_person, temp_panties)
        $ mc.change_arousal(5)
        $ mc.change_locked_clarity(5)
        "With a seductive wiggle, she slips her [temp_panties.display_name] down over her hips, revealing her smooth legs and [the_person.pubes_description] pubic region."
    else:
        "It appears that she walked down the hall completely nude."
        "Not bothering to close the door, [the_person.title] takes a look at her [body_description] in the mirror."
        "Your eyes can't help but be drawn to her [the_person.tits_description] and [the_person.pubes_description] vagina."
    if renpy.random.randint(0,2) == 0:
        "Stepping toward the shower, [the_person.title] turns on the faucet, the sound of running water filling the space."
        "She steps into the warm cascade, the water streaming over her, a steady rhythm."
    elif renpy.random.randint(0,1) == 0:
        "Stepping towards the shower, [the_person.title] turns the knob, and the sound of water fills the room."
        "She steps into the warm cascade, the routine of the daily shower unfolding. The water streams over her, enveloping her in its warmth."
    else:
        "Approaching the shower, [the_person.title] turns the faucet with purpose. Stepping into the warm cascade, her [the_person.hair_colour[0]!l] hair darkens with moisture."
    $ del temp_bra
    $ del temp_panties
    $ del temp_bottom
    $ del temp_top
    $ del temp_colour
    $ del body_description
    $ del body_word
    return

label shower_exit(the_person, sluttiness): #exit shower, dry, robe, exit room
    $ temp_outfit = Outfit("Nude")
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit)
    $ temp_robe = build_robe(the_person)
    if sluttiness < 20:
        if renpy.random.randint(0,1) == 0:
            "After rinsing off, [the_person.title] turns off the water and steps out onto the bath mat."
            "She grabs a fluffy white towel and begins to dry herself with brisk strokes, the routine almost mechanical."
            $ temp_outfit.add_dress(bath_robe.get_copy())
            $ scene_manager.apply_outfit(the_person, temp_outfit)
            "Droplets of water cling to her skin as she moves, and once dry, [the_person.title] wraps herself in a plush white robe that was hanging from a hook on the back of the door."
            "The soft fabric embraces her, creating a cocoon of comfort."
        else:
            "Stepping out of the shower onto a plush bath mat, [the_person.title] reaches for a fluffy white towel."
            "With a tenderness in her touch, she pats her skin dry, the fabric absorbing the droplets with care."
            $ temp_outfit.add_dress(bath_robe.get_copy())
            $ scene_manager.apply_outfit(the_person, temp_outfit)
            "[the_person.title] then wraps herself in a luxurious white robe, the soft material cocooning her in warmth."
        call shower_head_towel(the_person) from _call_shower_head_towel_0
        "She cinches the robe gently at the waist, a small, contented smile playing on her lips."
        "With a final glance in the mirror, she opens the door and leaves the room."
    elif sluttiness < 40:
        "[the_person.title] rinses off, the water trailing down her body in rivulets."
        "Stepping out of the shower onto a plush bath mat, [the_person.title] reaches for a fluffy white towel." 
        "With a tenderness in her touch, she pats her skin dry, the fabric absorbing the droplets with care."
        if the_person.get_opinion_score("skimpy outfits") < 1:
            $ temp_outfit.add_dress(bath_robe.get_copy())
            $ scene_manager.apply_outfit(the_person, temp_outfit) 
            "[the_person.title] then wraps herself in a luxurious white robe, the soft material cocooning her in warmth."
        else:
            $ temp_outfit.add_dress(temp_robe)
            $ scene_manager.apply_outfit(the_person, temp_outfit)
            "When she finally finishes drying off, every curve is visible under the thin robe that barely reaches mid-thigh."
        call shower_head_towel(the_person) from _call_shower_head_towel_20
        "She cinches the robe gently at the waist, a small, contented smile playing on her lips."
        "As [the_person.title] leaves the bathroom, you hear the delicate rustle of the robe and the quiet echoes of her steps."
    elif sluttiness < 60:
        if renpy.random.randint(0,1) == 0:
            "When at last [the_person.title] is clean again, she turns off the water and steps out onto the bath mat with shaky legs."
            if the_person.get_opinion_score("skimpy outfits") < 1:
                $ temp_outfit.add_dress(temp_robe)
                $ scene_manager.apply_outfit(the_person, temp_outfit)
                "Using a towel to dry every corner of her body, she pats it vigorously before wrapping herself up in the most decadent robe you've ever seen."
            else:
                $ temp_outfit.add_dress(towel.get_copy(), [.95, .95, .95, .95])
                $ scene_manager.apply_outfit(the_person, temp_outfit)
                "Using a towel to dry every corner of her body, she pats it vigorously before wrapping herself up in it."
        else:
            "Once she's satisfied that she's clean enough to be presentable again, [the_person.title] turns off the water and steps out of the shower stall."
            "She dries herself carefully using a plush white towel, making sure not to miss any spot as it glides across her skin."
            if the_person.get_opinion_score("skimpy outfits") < 1:
                $ temp_outfit.add_dress(temp_robe)
                $ scene_manager.apply_outfit(the_person, temp_outfit)
                "When everything is finally dry and soft once more, she wraps herself in an equally luxurious robe - its belt tied snugly around her waist."
            else:
                $ temp_outfit.add_dress(towel.get_copy(), [.95, .95, .95, .95])
                $ scene_manager.apply_outfit(the_person, temp_outfit)
                "When everything is finally dry and soft once more, she wraps herself in the towel, pulling it snugly around her [the_person.tits_description]."
        call shower_head_towel(the_person) from _call_shower_head_towel_40
        "With one final glance at herself in the mirror, [the_person.title] pads silently out of the bathroom."
    elif sluttiness < 80:
        "Slowly regaining control over her breathing, she reaches for the faucet handle and turns off the water, stepping out of the stall to grab a towel."
        "Drying herself off leisurely, [the_person.title] takes stock of herself in the mirror - [the_person.skin] skin flushed with arousal, dark [the_person.hair_description] plastered to her sweat-dampened form."
        call shower_head_towel(the_person) from _call_shower_head_towel_60
        "Despite feeling drained yet exhilarated, there's no denying that she looks absolutely irresistible."
        $ temp_outfit.add_dress(towel.get_copy(), [.95, .95, .95, .95])
        $ scene_manager.apply_outfit(the_person, temp_outfit)
        "Pulling a towel tight around her torso, she makes her way out of the bathroom, trying not to let anyone see the smug grin playing at her lips."
        "Today has indeed been quite eventful!"
    else:
        "Slowly regaining control over her breathing, she reaches for the faucet handle and turns off the water, stepping out of the stall to grab a towel."
        "Drying herself off leisurely, [the_person.title] takes stock of herself in the mirror - [the_person.skin] skin flushed with arousal, dark [the_person.hair_description] plastered to her sweat-dampened form."
        call shower_head_towel(the_person) from _call_shower_head_towel_80
        "Despite feeling drained yet exhilarated, there's no denying that she looks absolutely irresistible."
        $ mc.change_arousal(5)
        $ mc.change_locked_clarity(5)
        "Hanging the towel back on the rack, [the_person.title] walks out of the bathroom totally unconcerned with her nudity."
    $ del temp_robe
    return

label shower_head_towel(the_person): #TODO figure out how to use this
    if renpy.random.randint(1,2) == 0: #disabled, change to % chance
        if renpy.random.randint(0,2) == 0:
            "[the_person.title] deftly gathers her damp hair and twists it into a snug bun atop her head."
            $ temp_outfit.add_accessory(head_towel.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
            "The plush towel, a shade darker from the absorbed moisture, wraps around her head like a cocoon."
            "Droplets of water bead along the edges, and a fleeting smile crosses her face as she revels in the warmth that radiates from her freshly washed hair."
        elif renpy.random.randint(0,1) == 0:
            "She reaches for a fluffy towel. With a graceful flick of her wrist, she transforms her wet locks into a makeshift turban."
            $ temp_outfit.add_accessory(head_towel.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
            "The towel clings to her hair, absorbing the excess moisture"
        else:
            "Her hair, still dripping with water, is carefully enveloped by a plush, white towel."
            $ temp_outfit.add_accessory(head_towel.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
            "The fabric molds around the curves of her head, creating a cocoon for her damp tresses."
            "Stray tendrils peek out, hinting at the softness beneath."
    return

label shower_test():
    $ camera_list = mc.business.event_triggers_dict.get("home_cameras", [])
    call screen main_choice_display(build_menu_items([get_sorted_people_list(camera_list, "Footage review", "Back")]))
    $ the_person = _return
    $ x = 0
    menu:
        "Shower Enter":
            while x < 100:
                "Sluttiness = [x]"
                call shower_enter(the_person, x) from _call_shower_enter_test
                $ x +=1
        "Shower Exit":
            while x < 100:
                "Sluttiness = [x]"
                call shower_exit(the_person, x) from _call_shower_exit_test
                $ x +=1
        "Full scene":
            while x < 100:
                menu:
                    "0":
                        call shower_0(the_person) from _call_shower_0_test
                    "20":
                        call shower_20(the_person) from _call_shower_20_test
                    "40":
                        call shower_40(the_person) from _call_shower_40_test
                    "50":
                        call shower_50(the_person) from _call_shower_50_test
                    "60":
                        call shower_60(the_person) from _call_shower_60_test
                    "80":
                        call shower_80(the_person) from _call_shower_80_test
                    "90":
                        call shower_90(the_person) from _call_shower_90_test
                    "Exit":
                        $ x +=100
    $ del camera_list
    return
