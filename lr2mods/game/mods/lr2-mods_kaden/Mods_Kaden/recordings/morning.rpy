label morning_0(the_person): #TODO draw twice to show back
    $ sluttiness = 0 + renpy.random.randint(0,19)
    $ temp_outfit = get_pajama_outfit(the_person, sluttiness = sluttiness)
    $ the_person.home.show_background()
    $ scene_manager = Scene()
    # $ temp_person = the_person
    # $ wear_pajamas(temp_person, sluttiness = sluttiness)
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ body_description = get_body_description(the_person)
    "A soft glow fills the room as dawn breaks outside, casting a warm light across [the_person.title]'s body."
    call sleeping_in_bed(the_person, sluttiness) from _call_sleeping_in_bed_0
    call wake_up_wrapper(the_person, sluttiness) from _call_wake_up_wrapper_0
    $ scene_manager.update_actor(the_person, temp_outfit, position = "stand3")
    "[the_person.title] rolls out of bed and pads over to her dresser, stretching lazily as she does so."
    # $ scene_manager.add_actor(temp_person, position = "walking_away")
    call bedroom_strip(the_person, sluttiness) from _call_morning_strip_0
    call bedroom_dress(the_person, sluttiness) from _call_morning_dress_0
    "Standing before the mirror, she smooths her hands over her [body_description], feeling the fabric against her skin."
    $ scene_manager.update_actor(the_person, temp_outfit, position = "walking_away")
    $ the_clothing = new_outfit.get_upper_top_layer
    "A contented sigh escapes her lips as she adjusts the hem of her [the_clothing.display_name]. Satisfied with her appearance, she turns to leave the room."
    $ del sluttiness
    $ del the_clothing
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return

label morning_20(the_person):
    $ sluttiness = 20 + renpy.random.randint(0,19)
    $ temp_outfit = get_pajama_outfit(the_person, sluttiness = sluttiness)
    $ the_person.home.show_background()
    $ scene_manager = Scene()
    # $ temp_person = the_person
    # $ wear_pajamas(temp_person, sluttiness = sluttiness)
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ body_description = get_body_description(the_person)
    "The video feed opens up to reveal [the_person.title] lying peacefully in her bed. Her [the_person.hair_colour[0]!l] [the_person.hair_description] cascades over the pillow, framing her delicate features perfectly."
    if the_person.age < 25:
        "The sunlight streaming through her window casts a warm glow across her skin, emphasizing her youthful beauty."
    elif the_person.age < 45:
        "The sunlight streaming through her window casts a warm glow across her skin, emphasizing her refined beauty."
    else:
        "The sunlight streaming through her window casts a warm glow across her skin, emphasizing her mature beauty."
    "As [the_person.title] sleeps peacefully, her [body_description] shifts under the sheets, revealing her smooth bare skin."
    call sleeping_in_bed(the_person, sluttiness) from _call_sleeping_in_bed_20
    call wake_up_wrapper(the_person, sluttiness) from _call_wake_up_wrapper_20
    call bedroom_strip(the_person, sluttiness) from _call_morning_strip_20
    call bedroom_dress(the_person, sluttiness) from _call_morning_dress_20
    $ scene_manager.update_actor(the_person, temp_outfit, position = "walking_away")
    "Finally, she grabs her phone, wallet, and car keys, heading towards the door."
    $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
    $ the_clothing = new_outfit.get_upper_top_layer
    "Before exiting, she gives one last glance in the mirror, smirking coyly as she adjusts her [the_clothing.display_name] once again."
    "With that final flirtatious gesture, she leaves the room."
    $ del sluttiness
    $ del the_clothing
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return

label morning_40(the_person):
    $ sluttiness = 40 + renpy.random.randint(0,19)
    $ temp_outfit = get_pajama_outfit(the_person, sluttiness = sluttiness)
    $ the_person.home.show_background()
    $ scene_manager = Scene()
    # $ temp_person = the_person
    # $ wear_pajamas(temp_person, sluttiness = sluttiness)
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ body_description = get_body_description(the_person)
    "The video feed opens up to reveal [the_person.title] laying in her bed, partially covered by her sheets."
    "Her soft breaths caress the air, while her [the_person.hair_colour[0]!l] [the_person.hair_description] flows gracefully across the pillow like a waterfall."
    if the_person.age < 25:
        "The morning light pours in through the open window, bathing her body in a golden hue that accentuates her youthful innocence and beauty."
    elif the_person.age < 45:
        "The morning light pours in through the open window, bathing her body in a golden hue that hides the faint signs of age normally visible."
    else:
        "The dim light filtering through the curtains does little to hide the wrinkles on her skin, but they only add character to her face."    
    call sleeping_in_bed(the_person, sluttiness) from _call_sleeping_in_bed_40
    call wake_up_wrapper(the_person, sluttiness) from _call_wake_up_wrapper_40
    call bedroom_strip(the_person, sluttiness) from _call_morning_strip_40
    call bedroom_dress(the_person, sluttiness) from _call_morning_dress_40
    "She takes one last look at herself in the mirror, admiring how good her [body_description] looks."
    "Finally satisfied with her appearance, [the_person.title] gathers up her things and heads out into the hallway."
    $ del sluttiness
    $ del body_description
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return

label morning_60(the_person):
    $ sluttiness = 60 + renpy.random.randint(0,19)
    $ temp_outfit = get_pajama_outfit(the_person, sluttiness = sluttiness)
    $ the_person.home.show_background()
    $ scene_manager = Scene()
    # $ temp_person = the_person
    # $ wear_pajamas(temp_person, sluttiness = sluttiness)
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ body_description = get_body_description(the_person)
    "[the_person.title] lies invitingly in her bed, one arm flung above her head and the other curled beneath her pillow."
    "Her breathing is deep and steady, each exhale sending ripples through her [body_description]."
    "One arm stretches lazily overhead while the other hugs a well-used pillow tightly to her chest, revealing the swell of her breasts beneath the thin fabric."
    call sleeping_in_bed(the_person, sluttiness) from _call_sleeping_in_bed_60
    call wake_up_wrapper(the_person, sluttiness) from _call_wake_up_wrapper_60
    call bedroom_strip(the_person, sluttiness) from _call_morning_strip_60
    call bedroom_dress(the_person, sluttiness) from _call_morning_dress_60
    "She takes one last look at herself in the mirror, admiring how good she looks as she cups her [the_person.tits_description] to accentuate her cleavage."
    "Finally satisfied with her appearance, [the_person.title] blows a kiss to her reflection, gathers up her things, and heads out into the hallway."
    $ del sluttiness
    $ del body_description
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return

label morning_80(the_person):
    $ sluttiness = 80 + renpy.random.randint(0,19)
    $ temp_outfit = get_pajama_outfit(the_person, sluttiness = sluttiness)
    $ the_person.home.show_background()
    $ scene_manager = Scene()
    # $ temp_person = the_person
    # $ wear_pajamas(temp_person, sluttiness = sluttiness)
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ body_description = get_body_description(the_person)
    "Her room is dimly lit, but sunlight streams through the curtains, casting a warm glow across the floor."
    "Your eyes focus in on [the_person.title]'s chest, watching her [the_person.tits_description] breasts rising and falling with each gentle breath."
    "A bead of sweat trickles down between her cleavage, drawing attention to her sensitive nipples which harden under the touch of the cool air."
    "As she tosses and turns restlessly in her slumber, her arms occasionally lift above her head, offering tantalizing glimpses of her [body_description]."
    call sleeping_in_bed(the_person, sluttiness) from _call_sleeping_in_bed_80
    call wake_up_wrapper(the_person, sluttiness) from _call_wake_up_wrapper_80
    call bedroom_strip(the_person, sluttiness) from _call_morning_strip_80
    call bedroom_dress(the_person, sluttiness) from _call_morning_dress_80
    "[the_person.title] looks again as she sees her shapely legs in profile for the first time."
    the_person "I'm gonna look so hot."
    "[the_person.title] strikes a series of seductive poses in front of the full-length mirror, arching her back and sticking out her ass ever so slightly to showcase the sexy lines of her new outfit."
    #insta check
    # "In each shot, her face is filled with lust and anticipation, knowing that these images will end up pleasing her mysterious benefactors immensely."
    $ del sluttiness
    $ del body_description
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return

label morning_90(the_person):
    $ sluttiness = 90
    $ temp_outfit = get_pajama_outfit(the_person, sluttiness = sluttiness)
    $ the_person.home.show_background()
    $ scene_manager = Scene()
    # $ temp_person = the_person
    # $ wear_pajamas(temp_person, sluttiness = sluttiness)
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ body_description = get_body_description(the_person)
    "Even in her deepest slumber, [the_person.title]'s body radiates sexuality."
    "The camera captures every sultry breath and the gentle shift of her hips as she adjusts herself beneath the sheets."
    "She moans softly in her sleep, betraying her arousal even before wakefulness."
    "Despite being unconscious, it's clear that [the_person.title] is achingly turned on by whatever thoughts are running through her mind."

    "Her [body_description] moves restlessly in her sleep, reflecting the lingering heat and desire within her."
    "Your eyes focus on her flushed cheeks and parted lips as she tosses and turns, revealing a dreamy expression etched onto her face."
    "Her [the_person.tits_description] rise and fall with each breath, causing the sheet to stretch enticingly across her chest."
    "Her legs are intertwined beneath the sheets, offering glimpses of smooth thighs and soft skin as they shift against one another."
    "A thin sheen of sweat coats her body, highlighting every curve and contour."
    #NTR options
    #"As you peer into the video feed, [the_person.title] sleeps soundly in her bed."
    #"Her body is flushed with heat and she tosses and turns restlessly as if caught in a dream."
    #"The covers are pulled up to her chin, revealing one smooth thigh and part of an arm belonging to another person who lies close beside her."
    #"Their breathing synchronizes, indicating they're deeply asleep as well."
    #"Their bodies are entwined, hinting at a night of passionate lovemaking shared between them."
    #"A trail of kisses and hickeys adorns [the_person.title]'s neck and shoulder, testament to their intimate encounter."
    #"Even in slumber, it's clear that both are still feeling the aftereffects of their sexual adventure."
    call sleeping_in_bed(the_person, sluttiness) from _call_sleeping_in_bed_90
    call wake_up_wrapper(the_person, sluttiness) from _call_wake_up_wrapper_90
    call bedroom_strip(the_person, sluttiness) from _call_morning_strip_90
    call bedroom_dress(the_person, sluttiness) from _call_morning_dress_90
    $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
    "She turns around slowly, taking in every angle of her body. A small smile appears on her lips as she admires how good she looks in this outfit."
    "Finally, she looks at herself in the mirror one last time before leaving the room."
    $ del sluttiness
    $ del body_description
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    return

label sleeping_in_bed(the_person, sluttiness):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ the_clothing = temp_outfit.get_upper_top_layer
    $ the_other_clothing = temp_outfit.get_bra()
    if the_clothing == the_other_clothing:
        $ the_clothing = None
    $ body_description = get_body_description(the_person)
    $ body_word = get_body_word(the_person)
    if renpy.random.randint(0,100) < sluttiness: #bare chest
        if the_clothing:
            if the_other_clothing:
                if sluttiness%2 == 0:
                    "Her sheets have slipped down her body, leaving only the faint outline of her [the_other_clothing.display_name] visible, as her [the_clothing.display_name] conceals the rest."
                else:
                    "With each breath, the fabric of her [the_clothing.display_name] rises and falls, teasingly revealing a glimpse of the delicate [the_other_clothing.display_name] underneath."
            else:
                if sluttiness%2 == 0:
                    "Her sheets have slipped down her body, yet the [the_clothing.display_name] conceals everything, leaving only a subtle shadow where her nipples press against the fabric."
                else:
                    "The fabric of her [the_clothing.display_name] clings to her skin, revealing just enough to hint at what lies beneath."
        elif the_other_clothing:
            if the_person.has_large_tits:
                "Her sheets have slipped down her body, exposing her [the_other_clothing.display_name] and the manner in which it strains to hold her [the_person.tits_description]."
            else:
                "Her sheets have slipped down her body, exposing the [the_other_clothing.display_name], which unfortunately provides nearly complete coverage for her [the_person.tits_description]."
        else:
            "Her sheets have gracefully slipped down her body, revealing a stunning glimpse of her [the_person.tits_description]."
    else: # bare shoulder
        if the_clothing:
            if the_other_clothing:
                if sluttiness%2 == 0:
                    "Her sheets have subtly shifted, revealing just a hint of her [the_clothing.display_name] draping over her shoulder and the faint silhouette of her [the_other_clothing.display_name]'s strap."
                else:
                    $ temp_colour = clothing_colour_name(the_other_clothing.colour)
                    "As she moves, the fabric of her [the_clothing.display_name] shifts, exposing a hint of lace from her [temp_colour] [the_other_clothing.display_name]."
            else:
                "Her sheets have gently moved, revealing just a hint of her [the_clothing.display_name] draping over her shoulder."
                "Yet upon closer inspection, there's no sign of a bra strap beneath the [the_clothing.display_name]."
        elif the_other_clothing:
            if the_person.has_large_tits:
                "The sheets have sensually shifted, unveiling the alluring strap of her [the_other_clothing.display_name] caressing her shoulder."
            else:
                "The sheets have gently shifted, unveiling the [the_other_clothing.display_name]'s strap, which rests delicately upon her shoulder."
        else:
            "The sheets have subtly shifted, offering a seductive peek at her naked shoulder, but any other tantalizing secrets remain hidden, just out of sight under her covers."
    $ the_clothing = temp_outfit.get_lower_top_layer
    $ the_other_clothing = temp_outfit.get_panties()
    $ body_word = get_body_word(the_person)
    if the_clothing == the_other_clothing:
        $ the_clothing = None
    if renpy.random.randint(0,100) < sluttiness: #hint of waist
        if the_clothing:
            if lower_leg_region in the_clothing.constrain_regions: #long legs
                "Glancing downward, you notice she's mostly emerged from beneath her sheet, yet her [body_word] legs remain concealed by her [the_clothing.display_name]."
            else:
                "As you gaze lower, you notice that she has gracefully extended herself from beneath the sheet, granting you a captivating view of her [body_word] legs, until they are veiled by her [the_clothing.display_name]."
            if the_other_clothing:
                "You can also catch a subtle glimpse of her [the_other_clothing.display_name] teasingly peering above the waistband."
        elif the_other_clothing:
            "Gazing downward, you notice she has emerged from beneath her sheet, unveiling the entirety of her [body_word] leg."
            "Moreover, a tantalizing hint of the [the_other_clothing.display_name] hugging her waist beckons your attention."
        else:
            "Gazing further down, you notice that she has gracefully rolled halfway out from under her sheet."
            "Her long, [body_word] leg is fully revealed, extending sensuously, and you catch a tantalizing glimpse of her waist, confirming her lack of clothing."
            "Yet, the sheet still veils the more intimate regions, leaving them to your imagination."
    elif renpy.random.randint(0,50) < sluttiness: #lots of leg
        if the_clothing in []: #long legs
                "Glancing downward, you notice that one of her [body_word] legs gently emerges from beneath the sheets."
                "The gentle fabric of her [the_clothing.display_name] lovingly adheres to her thighs, subtly revealing the promise of [body_word], well-defined legs concealed beneath."
        else:
            "Gazing downward, you notice one of her mostly exposed, [body_word] legs, exuding an irresistible allure."
            "However, her outfit remains hidden above the knee due to the sheet, making it difficult to discern what she's wearing."
    else: #just a foot/calf
        if the_clothing in []: #long legs
                "The majority of her body remains concealed under the sheet, yet a peek of her foot and the hem of her [the_clothing.display_name] is visible."
        else:
            "Her sheet conceals most of the rest of her body, leaving only a tantalizing glimpse of a foot exposed."
    $ del the_clothing
    $ del the_other_clothing
    $ scene_manager.clear_scene()
    return

label wake_up_wrapper(the_person, sluttiness):
    if hasattr(the_person.primary_job, "day_slots") and hasattr(the_person.primary_job, "time_slots") and day%7 in the_person.primary_job.day_slots and 1 in the_person.primary_job.time_slots:
        call alarm_wake_up(the_person, sluttiness) from _call_alarm_wake_up
    else:
        call natural_wake_up(the_person, sluttiness) from _call_natural_wake_up
    $ scene_manager.clear_scene()
    return

label alarm_wake_up(the_person, sluttiness):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    if the_person.opinion.working > 1:
        "[the_person.title] wakes up to the sound of her alarm, but instead of looking groggy or annoyed, she seems happy, maybe even thrilled."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
        "She quickly gets out of bed and heads towards her closet."
    elif the_person.opinion.working > 0:
        "[the_person.title] groans softly as her alarm clock goes off, signaling the start of another day."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
        "She rolls over in bed, trying to ignore its obnoxious ringtone but ultimately failing."
        "With a heavy sigh, she reaches over and silences the device before climbing out from underneath the warm covers."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
        "She rubs at her eyes vigorously until they finally open. The sunlight streaming through her window seems blinding, and she squints against it as she sits up straight."
        $ the_clothing = temp_outfit.get_upper_top_layer
        $ the_other_clothing = temp_outfit.get_bra()
        if the_clothing == the_other_clothing:
            $ the_clothing = None
        else:
            $ the_other_clothing = temp_outfit.get_lower_top_layer
        if the_clothing and the_other_clothing:
            "She stretches languidly, yawning deeply as she does so. Her [the_clothing.display_name] rides up slightly, revealing a hint of the [the_other_clothing.display_name] she wears beneath it."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
            "[the_person.title] stands up slowly, making her way over to her vanity table and gazing at herself in the mirror."
            "She runs a hand through her unkempt hair, pushing back some stray strands."
    elif the_person.opinion.working > -1:
        if renpy.random.randint(0,1) == 1:
            "As the morning sun begins to peek through the blinds, [the_person.title] finally drags herself out of bed after hitting the snooze button one too many times."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
            "Her body appears to ache from being curled up in the same position for hours, but she forces herself to stand up straight."
            "She walks over to her closet, still half asleep, and reaches for some new clothes."
        else:
            "[the_person.title] rolls over in bed, her eyes still closed as she tries to ignore the piercing sound of her alarm."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
            "But when it continues to shrill, she finally gives in and forces herself out of bed."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
            "She stumbles forward, heading towards her dresser with the attached mirror."
    elif the_person.opinion.working > -2:
        "[the_person.title]'s sleepy eyes flutter open as her phone buzzes next to her ear."
        "She reaches over and slaps at the snooze button, grunting in annoyance as the noise ceases momentarily."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
        "With a heavy sigh, she rolls onto her side, pulling the covers over her head to block out the early morning light streaming through the window."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
        "Groaning, she tosses aside the sheets and swings her feet off the bed, wincing as they brush against the cold wood floor."
    else:
        "Suddenly, there's a pinging noise from her dresser drawer followed by a soft moan escaping her lips."
        "[the_person.title] groans, her eyes fluttering open as she hits the snooze button on her alarm clock."
        the_person "Ugh, five more minutes."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
        "[the_person.possessive_title!c] mumbles to herself before rolling over and snuggling back into her pillow."
        "After what feels like an eternity but is actually only another minute, the alarm goes off again with its shrill tone."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
        "This time, [the_person.title] reluctantly pushes herself up and out of bed, rubbing at her eyes with one hand while stretching her arms overhead with the other."
        "Her [the_person.hair_description] sticks up in every direction from where it was buried beneath her head during sleep."
    $ scene_manager.clear_scene()
    return

label natural_wake_up(the_person, sluttiness):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit, position = "missionary")
    $ temp_bra = None
    $ temp_panties = None
    $ temp_top = None
    $ temp_bottom = None
    $ body_description = get_body_description(the_person)
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
    if temp_bottom == temp_panties:
        $ temp_bottom = None
    if the_person.opinion.masturbating > 0 and renpy.random.randint(0,3) == 1 and temp_panties and not temp_bra and not temp_bottom and temp_top:
        "[the_person.title] awakens groggily, her eyes fluttering open as the sun streams in through the window."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "back_peek")
        "She rolls onto her side, causing her [the_person.tits_description] to shift enticingly within the confines of her thin [temp_top.display_name]."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
        "Stretching her [body_word] limbs, she arches her back, elongating her supple body and drawing attention to her perfect posterior."
        "Gently, she trails her fingers along her collarbone, tracing the path of her shoulder down to her breast."
        "Cupping it gently, she massages the soft mound, eliciting a moan from deep within her throat."
        "Her hand glides lower, caressing her [body_word] stomach until it reaches the hem of her [temp_panties.display_name]."
        $ mc.change_arousal(5)
        $ scene_manager.draw_animated_removal(the_person, temp_panties)
        "Taking her time, [the_person.title] slides them down her toned thighs, revealing her [the_person.pubes_description] vagina covered in a layer of morning dew."
        "She teasingly brushes her index finger over her labia, earning a sharp intake of air."
        "With increasing boldness, she starts rubbing circles around her clitoris, applying just enough pressure to heighten her arousal without reaching climax."
        $ mc.change_arousal(10)
        "Her hips start moving rhythmically, urging her hand to speed up its pace."
        "Breath coming faster, her hand expertly finds her entrance, two fingers slipping inside, stroking the wet walls of her tight passage."
        "Feeling the familiar build up of pleasure, [the_person.title] lets out a high pitched whine, her entire body tensing in anticipation..."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "missionary")
        $ mc.change_arousal(15)
        $ the_person.have_orgasm()
    elif temp_top or temp_bra and renpy.random.randint(0,3) == 1:
        if renpy.random.randint(0,2) == 1:
            "As [the_person.title] slowly opens her eyes, she takes in the bright morning sunlight streaming through her window."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
            "Yawning, she rubs the sleep from her eyes before sitting up straight in bed."
            "Her breasts, still partially hidden by her top, bounce slightly as she stretches her arms above her head."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
            "With a contented sigh, [the_person.title] swings her legs over the edge of the bed and plants them firmly on the ground."
        elif renpy.random.randint(0,1) == 1:
            if temp_top:
                "[the_person.title] stretches lazily, her arms above her head, causing her [the_person.tits_description] to jiggle enticingly underneath her [temp_top.display_name] before finally sitting up in bed"
            else:
                "[the_person.title] stretches lazily, her arms above her head, causing her [the_person.tits_description] to jiggle enticingly underneath her [temp_bra.display_name] before finally sitting up in bed"
            "Blinking sleepily she rubs at her eyes with one hand while pushing her [the_person.hair_colour[0]!l] [the_person.hair_description] out of her face with the other."
            "She yawns widely, exposing the inside of her mouth and the light dusting of freckles across her cheeks, before reaching down to pull her bottom lip between her teeth gently, biting lightly."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
            "After a few moments of thoughtful contemplation, [the_person.title] quickly gets out of bed and begins moving around the room with purposeful determination."
        else:
            "[the_person.title] wakes up with a soft moan, her body gently rising from the sheets."
            the_person "Ahhh… what time is it?"
            "She mumbles, stretching her arms above her head."
            if temp_top:
                "Her breasts jiggle beneath her [temp_top.display_name], and her [the_person.hair_colour[0]!l] [the_person.hair_description] falls over her shoulders, covering one eye."
            else:
                "Her breasts jiggle beneath her [temp_bra.display_name], and her [the_person.hair_colour[0]!l] [the_person.hair_description] falls over her shoulders, covering one eye."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
            "She rubs her eyes, yawning loudly before sitting up in bed."
    elif temp_bottom and renpy.random.randint(0,1) == 1:
        "She stretches languidly, arching her back before rolling over onto her stomach, exposing her [body_word] ass cheeks which part slightly from each other invitingly."
        $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
        if clothing_plural(temp_bottom):
            "Her movements become more deliberate now - she pushes herself off the bed and stands up straight, giving you an excellent view of her thighs and shapely legs encased in the [temp_bottom.display_name] that clings enticingly to every curve."
        else:
            "Her movements become more deliberate now - she pushes herself off the bed and stands up straight, giving you an excellent view of her thighs and shapely legs encased in the [temp_bottom.display_name] that cling enticingly to every curve."

    elif not temp_bottom and not temp_panties:
        "[the_person.title]'s eyes flutter open as she awakens from her slumber, the warm sunlight streaming through the window casting a gentle glow over her nude body."
        "She stretches languidly and yawns, her breasts rising and falling with each breath."
    else: #any
        if renpy.random.randint(0,4) == 1:
            "[the_person.title] wakes up and stretches luxuriously, letting out a contented yawn as she rolls over onto her side."
            "Her eyes flutter open, taking in the warm light filtering through the window."
        elif renpy.random.randint(0,3) == 1:
            "As [the_person.title] begins to stir, you can't help but admire the way her soft curves move beneath her delicate skin."
            "Her[the_person.hair_colour[0]!l] [the_person.hair_description] is a mess of tangles around her face, and there's an innocent look in her deep [the_person.eyes[0]!l] eyes that tugs at your heartstrings."
            "Her movements are slow and deliberate, almost as if she's taking pleasure in the simple act of being alive."
        elif renpy.random.randint(0,2) == 1:
            "She mumbles to herself, rubbing the sleep out of her eyes."
            "Her [the_person.hair_colour[0]!l] [the_person.hair_description] is messy from tossing and turning during the night."
            "[the_person.title] slowly gets out of bed, stretching her arms above her head before reaching for her phone on the nightstand."
        elif renpy.random.randint(0,1) == 1:
            "[the_person.title] wakes up in the morning with a smile on her face, feeling refreshed and energized."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
            "She rolls over onto her side and stretches her arms out, yawns loudly, and then sits up in bed."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "stand2")
            "As she gets out of bed, she smiles to herself."
        else:
            "The room is dimly lit, soft light coming from a small nightlight near her headboard."
            "You can see her body moving beneath the sheets, her breathing slow but steady."
            $ scene_manager.update_actor(the_person, temp_outfit, position = "sitting")
            "Suddenly, she stirs slightly before sitting up abruptly in her bed with a soft moan escaping her lips as she stretches languidly like a cat before yawning adorably."
            "She looks around sleepily before starting to move."
    $ del temp_bra
    $ del temp_panties
    $ del temp_bottom
    $ del temp_top
    $ scene_manager.clear_scene()
    return

label bedroom_strip(the_person, sluttiness):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit)
    $ body_description = get_body_description(the_person)
    $ body_word = get_body_word(the_person)
    if renpy.random.randint(0,1000) == 666:
        "You observe [the_person.title]'s deliberate rise from her bed, the slow steps that take her to the vanity table."
        "Her gaze locks onto her reflection in the mirror, and her fingers gently smooth down unruly strands of hair."
        "As you watch the footage, a single line of static slices down the screen, casting an unsettling ripple."
        "It takes a moment for the realisation to dawn - [the_person.title]'s reflection is not in sync."
        "It trails slightly behind her movements. Unbeknownst to her, she continues to examine herself in the mirror."
        "Suddenly, a surge of static engulfs the scene, and the transformation is disconcerting."
        "When [the_person.title] turns on her heel to face away from the mirror, her reflection remains fixed, gazing out at her."
        "Her expression shifts from nonchalance to shock, mirroring your own."
        "Reality starts to fray, and the footage deteriorates into a maelstrom of static, but within that chaos, a discernible shape emerges."
        "A physical hand, tangible and real, pushes its way out of the mirror."
        "Just before the video cuts to black, the profound terror of the moment is etched into your memory."
        "You swiftly reach for your mouse, your heart pounding, and hurriedly rewind the footage on your computer, needing to confirm the inexplicable."
        "As the video plays once more, everything appears utterly normal."
        "The static has vanished, and [the_person.title]'s reflection behaves as it should."
        "You stop the footage, feeling a mounting sense of confusion."
        "You watch it again, leaning back in your chair and blinking, as uncertainty gnaws at you."
        "You silently question your own well-being, thinking, /'How much sleep did I get last night? Did I eat dinner yesterday? Maybe I'm spending too much time on the computer.'/"
        "You rub your tired eyes and shake your head to clear your thoughts, focusing on the control panel."
        "With a shaky hand, you restart the footage, but you look up just a fraction too slowly."
        "Unbeknownst to you, a look of abject horror sweeps across the face of [the_person.title]'s reflection as the footage resumes, a chilling revelation slipping through the cracks of your understanding."
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
    if temp_bottom == temp_panties or temp_bottom.is_extension:
        $ temp_bottom = None
    if not temp_bra and not temp_bottom and not temp_panties and not temp_top: #nude
        "[the_person.title] stands naked in front of the mirror."
        "Her reflection casts an ethereal glow across the room as she takes in her own stunning form."
        "At [the_person.age] years old, she's confident and unafraid to showcase her beauty."
        "Her breasts are full and round, nipples hardening in the cool air."
        "They jut proudly forward, drawing attention to their perky presence on her chest."
        "Her flat and toned stomach tapers down to a narrow waist that leads to long, slender legs."
        "Each muscle and curve is meticulously defined from head to toe, testament to her dedication to self-care and fitness."
        "[the_person.title] spins slowly around, taking in different angles of herself."
        "She runs her hands along her hips, appreciating how they accentuate her curves before moving higher up her body again."
        "Cupping one breast with her hand, she squeezes gently while watching intently."

        #We see [the_person.title] standing naked in front of the mirror, her reflection casting an ethereal glow across the room. Her body is a work of art, confident and unafraid to showcase its beauty.

        #Her breasts, full and round, jut proudly forward, nipples hardening at the slightest touch. Her stomach, flat and toned, tapers down to a narrow waist that leads to long, slender legs. Each muscle and curve is meticulously defined, a testament to her dedication to self-care and fitness.

        #[the_person.title] runs her hands along her hips, tracing the outline of her curves before moving higher, cupping her breasts and squeezing gently. Her expression changes from introspective to sensual as she rubs herself against the edge of the vanity, her movements slow and deliberate.

        #Her moans echo throughout the room, a mix of pleasure and yearning that only grows stronger as she continues to explore her body. With each passing moment, her confidence swells, emboldened by the knowledge that she is completely alone in this intimate space.

        #As [the_person.title] nears climax, her face contorts in ecstasy, her teeth biting into her lip as she rides the crest of orgasmic bliss. Her body convulses, her arms flailing wildly as she loses control, her voice rising to a crescendo of pleasured whispers. Finally, with a final cry, she collapses, spent and satisfied, her vision clouding for a brief moment before returning to clarity.
        $ del temp_bra
        $ del temp_panties
        $ del temp_bottom
        $ del temp_top
        $ scene_manager.clear_scene()
        return
    if sluttiness > 50:
        "[the_person.title] then begins to remove her pajamas, revealing her naked body underneath."
        "Her skin is smooth and soft, with a natural glow that catches your eye."
        "As she takes off each piece, you can't help but notice how her slutty nature shines through even when she's not trying to seduce anyone."
    else:
        "As she stands in front of the mirror, she gazes at her reflection, admiring her [body_description] clad in her snug pajamas."
        "Without any further hesitation, she begins to undress as you watch."
    if temp_top: # strip top
        $ scene_manager.draw_animated_removal(the_person, temp_top)
        # $ scene_manager.draw_animated_removal(temp_person, temp_top)
        if renpy.random.randint(0,2) == 1:
            "Grasping her [temp_top.display_name], [the_person.title]'s hands slowly slide up her torso, exposing her belly and then her chest, in a soft rustle of fabric."
        elif renpy.random.randint(0,1) == 1:
            "She starts by pulling her [temp_top.display_name] up and over her head."
        else:
            "First comes the [temp_top.display_name], which is easy to remove - just a simple pull over her head and it's off in one swift motion."
        if temp_bra:
            "This exposes the [temp_bra.display_name] containing her [the_person.tits_description]."
        else:
            if renpy.random.randint(0,2) == 1:
                "Her breasts are exposed, their nipples hardening against the cool air in her bedroom."
            elif renpy.random.randint(0,1) == 1:
                "Her bra-less breasts are now completely unrestrained, jiggling with every movement she makes as if they're begging for attention."
            else:
                "She discards her top, exposing her [the_person.tits_description] with their hardened nipples."
        if temp_bottom:
            "Looking lower you can now see the entirety of her stomach until the [temp_bottom.display_name] hugging her waist."
            if temp_panties:
                if clothing_plural(temp_panties):
                    "Moreover, the waistband of her [temp_panties.display_name] subtly peek above the top of her [temp_bottom.display_name]."
                else:
                    "Moreover, the waistband of her [temp_panties.display_name] subtly peeks above the top of her [temp_bottom.display_name]."
        elif temp_panties:
            if renpy.random.randint(0,2) == 1:
                if clothing_plural(temp_panties):
                    "As she removes her [temp_top.display_name] her [temp_panties.display_name] are fully exposed, showing off hints of her [the_person.hair_description] and [the_person.skin] skin."
                else:
                    "As she removes her [temp_top.display_name] her [temp_panties.display_name] is fully exposed, showing off hints of her [the_person.hair_description] and [the_person.skin] skin."
            elif renpy.random.randint(0,1) == 1:
                if clothing_plural(temp_panties):
                    "You can also now clearly see that below the waist she is clad in nothing but a skimpy pair of [temp_panties.display_name]."
                else:
                    "You can also now clearly see that below the waist she is clad in nothing but a skimpy [temp_panties.display_name]."
            else:
                if clothing_plural(temp_panties):
                    "This also reveals a pair of skimpy [temp_panties.display_name] that barely cover the essentials."
                else:
                    "This also reveals a skimpy [temp_panties.display_name] that barely covers the essentials."
                "The thin strip of fabric disappears between the cheeks of her ass, drawing attention to its roundness."
        else:
            if renpy.random.randint(0,1) == 1:
                "This also completely reveals her bare ass cheeks and the [the_person.pubes_description] pussy between her legs."
            else:
                "There is now nothing in the way of her smooth, [body_word] legs and [the_person.pubes_description] pubic region."
    if temp_bra: # strip bra
        $ scene_manager.draw_animated_removal(the_person, temp_bra)
        # $ scene_manager.draw_animated_removal(temp_person, temp_bra)
        if renpy.random.randint(0,1) == 1 and temp_top:
            if the_person.skin == "white":
                "Next she reaches behind her back to unclasp her [temp_bra.display_name], letting it slide down her arms to reveal her [the_person.tits_description] adorned with pale pink nipples."
            elif the_person.skin == "tan":
                "Next she reaches behind her back to unclasp her [temp_bra.display_name], letting it slide down her arms to reveal her [the_person.tits_description] adorned with light brown nipples."
            else:
                "Next she reaches behind her back to unclasp her [temp_bra.display_name], letting it slide down her arms to reveal her [the_person.tits_description] adorned with nearly black nipples."
        elif renpy.random.randint(0,1) == 1:
            "Her breathing seems to speed up as she reaches behind her back, unclasping her bra."
            "It falls away, leaving her breasts free and bouncing slightly with every move."
            "She looks down at herself in the mirror, taking in the sight of her topless body."
        else:
            if not the_person.has_large_tits:
                "Her fingers trace along the edges of her bra straps, almost teasingly she lowers them over her shoulders, revealing her perky breasts."
            else:
                "She reaches behind her back and undoes the clasp of her bra, letting it fall to the floor in a silky whoosh."
                "Her breasts bounce free, their weight pulling them down slightly."
    if (temp_top or temp_bra) and (temp_bottom or temp_panties):
        if temp_top:
            "'Mmm' [the_person.title] murmurs appreciatively as she feels the cool air caress her newly exposed skin before bending over to pick up the discarded [temp_top.display_name] from the floor, folding it neatly and placing it on top of her dresser."
        else:
            "'Mmm' [the_person.title] murmurs appreciatively as she feels the cool air caress her newly exposed skin before bending over to pick up the discarded [temp_bra.display_name] from the floor, folding it neatly and placing it on top of her dresser."
        if renpy.random.randint(0,1) == 1:
            "Catching her reflection in the mirror she smiles, enjoying the shape of her body."
        else:
            "She then takes a moment to gaze at her reflection, admiring her [body_description]."
        "The rest of her outfit comes off next, piece by piece, unveiling her [body_word] and sensuous curves."
    if temp_bottom: # strip bottom
        $ scene_manager.draw_animated_removal(the_person, temp_bottom)
        # $ scene_manager.draw_animated_removal(temp_person, temp_bottom)
        if clothing_plural(temp_bottom):
            "She peels off those cumbersome [temp_bottom.display_name] that have been clinging to every curve of her body all night long."
        else:
            "She peels off the cumbersome [temp_bottom.display_name] that has been clinging to every curve of her body all night long."
        if temp_panties:
            if renpy.random.randint(0,2) == 1:
                if clothing_plural(temp_panties):
                    "As she steps out of them, her [temp_panties.display_name] are exposed, showing off hints of her [the_person.pubes_description] pussy and [the_person.skin] skin."
                else:
                    "As she steps out of them, her [temp_panties.display_name] is exposed, showing off hints of her [the_person.pubes_description] pussy and [the_person.skin] skin."
            elif renpy.random.randint(0,1) == 1:
                if clothing_plural(temp_panties):
                    "This leaves her clad in nothing but the [temp_panties.display_name] that cling snugly to her waist."
                else:
                    "This leaves her clad in nothing but the [temp_panties.display_name] that clings snugly to her waist."
            else:
                if clothing_plural(temp_panties):
                    "[the_person.title] steps out of her [temp_bottom.display_name], revealing a pair of skimpy [temp_panties.display_name] that barely cover the essentials."
                else:
                    "[the_person.title] steps out of her [temp_bottom.display_name], revealing a skimpy [temp_panties.display_name] that barely covers the essentials."
                "The thin strip of fabric disappears between the cheeks of her ass, drawing attention to its roundness."
        else:
            if renpy.random.randint(0,1) == 1:
                "Then she slips out of her [temp_bottom.display_name], revealing her bare ass cheeks and the [the_person.pubes_description] pussy between her legs."
            else:
                "With deliberate slowness, she pulls down her [temp_bottom.display_name], revealing her smooth [body_word] legs and [the_person.pubes_description] pubic region."
    if temp_panties: # strip panties
        $ scene_manager.draw_animated_removal(the_person, temp_panties)
        # $ scene_manager.draw_animated_removal(temp_person, temp_panties)
        if sluttiness > 50:
            "She slides her [temp_panties.display_name] down her thighs, revealing her wetness and the outline of her labia."
            "Next, she steps out of them, leaving them pooled around her feet."
        elif renpy.random.randint(0,2) == 1:
            if clothing_plural(temp_panties):
                "Then, she runs her fingers along the edge of her [temp_panties.display_name], teasing herself before finally lowering and stepping out of them."
            else:
                "Then, she runs her fingers along the edge of her [temp_panties.display_name], teasing herself before finally lowering and stepping out of it."
        elif renpy.random.randint(0,1) == 1:
            "Then, with a seductive wiggle, she slips her [temp_panties.display_name] down over her hips, revealing her smooth legs and [the_person.pubes_description] pubic region."
        else:
            if clothing_plural(temp_panties):
                "Taking a deep breath, she continues undressing, slipping her [temp_panties.display_name] down her thighs and stepping out of them, feeling the cool air brush against her most sensitive areas."
            else:
                "Taking a deep breath, she continues undressing, slipping her [temp_panties.display_name] down her thighs and stepping out of it, feeling the cool air brush against her most sensitive areas."
    $ temp_top = len(temp_outfit.feet)
    while temp_top > 0:
        $ temp_top -=1
        $ temp_bottom = temp_outfit.feet[temp_top]
        $ scene_manager.draw_animated_removal(the_person, temp_bottom)
    $ del temp_bra
    $ del temp_panties
    $ del temp_bottom
    $ del temp_top
    $ scene_manager.clear_scene()
    return

label bedroom_dress(the_person, sluttiness):
    $ temp_outfit = Outfit("Nude")
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, temp_outfit)
    if renpy.random.randint(0,2) == 0:
        "With renewed determination, [the_person.possessive_title] moves onto the next step of her morning routine, getting dressed."
        "She walks over to her closet and surveys the outfits hanging inside, trying to decide what will be appropriate for the day ahead."
    elif renpy.random.randint(0,1) == 0:
        "Next, she moves onto picking her outfit. She opens her closet door, revealing an array of colourful clothes hanging neatly inside."
    else:
        "[the_person.title] collects an outfit from her dresser and holds it up as she admires herself in the mirror."
        "It is as if she is trying to decide whether or not she likes how it looks."
    $ sluttiness_modifier = sluttiness - the_person.sluttiness
    if day%7 < 5 and (the_person.has_role(generic_student_role) or the_person.is_employee):
        if the_person.has_role(generic_student_role):
            $ new_outfit = limited_university_wardrobe.wardrobe.decide_on_outfit(the_person, sluttiness_modifier = sluttiness_modifier)
        else:
            $ new_outfit = the_person.primary_job.wardrobe.decide_on_outfit(the_person, sluttiness_modifier = sluttiness_modifier)
    else:
        $ new_outfit = the_person.decide_on_outfit(sluttiness_modifier = sluttiness_modifier)
    $ del sluttiness_modifier
    $ bottom_list = sorted([x for x in new_outfit.lower_body if not x.is_extension and not temp_outfit.has_clothing(x)], key = lambda x: x.layer, reverse = False)
    $ top_list = sorted([x for x in new_outfit.upper_body if not x.is_extension and not temp_outfit.has_clothing(x)], key = lambda x: x.layer, reverse = False)
    $ foot_list = sorted([x for x in new_outfit.feet if not x.is_extension and not temp_outfit.has_clothing(x)], key = lambda x: x.layer, reverse = False)
    $ temp_bottom = None
    $ temp_top = None
    $ temp_bra = None
    $ temp_panties = None
    if new_outfit.get_upper_top_layer:
        $ temp_top = new_outfit.get_upper_top_layer
    if new_outfit.get_bra():
        $ temp_bra = new_outfit.get_bra()
    if new_outfit.get_lower_top_layer:
        $ temp_bottom = new_outfit.get_lower_top_layer
    if new_outfit.get_panties():
        $ temp_panties = new_outfit.get_panties()
    if temp_panties and temp_panties.is_extension:
        $ temp_panties = None
    if temp_bottom and temp_bottom.is_extension:
        $ temp_bottom = None
    if temp_top == temp_bra:
        $ temp_top = None
    if temp_bottom == temp_panties:
        $ temp_bottom = None
    if temp_panties:
        $ bottom_list.remove(temp_panties)
        if renpy.random.randint(0,1) == 0:
            if clothing_plural(temp_panties):
                "She reaches for her [temp_panties.display_name] first, sliding them up her slender legs."
            else:
                "She reaches for her [temp_panties.display_name] first, sliding it up her slender legs."
        else:
            $ temp_colour = clothing_colour_name(temp_panties.colour)
            if clothing_plural(temp_panties):
                "She slips on a pair of [temp_colour] [temp_panties.display_name], which hug her pubic mound snugly but not too tightly."
            else:
                "She slips on a [temp_colour] [temp_panties.display_name], which hugs her pubic mound snugly but not too tightly."
        $ temp_outfit.add_lower(temp_panties.get_copy())
        $ scene_manager.update_actor(the_person, temp_outfit)
    if temp_bra:
        $ top_list.remove(temp_bra)
        if not temp_bra.has_extension:
            if temp_panties:
                "Then she picks out a pretty little [temp_bra.display_name] from among several others hanging neatly in the closet."
            else:
                "She picks out a pretty little [temp_bra.display_name] from among several others hanging neatly in the closet."
        else:
            "She picks out a sexy [temp_bra.display_name] and steps into it, sliding it up her legs and then rolling it up her torso to insert her arms."
        $ temp_outfit.add_upper(temp_bra.get_copy())
        $ scene_manager.update_actor(the_person, temp_outfit)
    if temp_bottom:
        while len(bottom_list) > 0:
            $ temp_bottom = bottom_list.pop(0)
            #describe bottom
            if clothing_plural(temp_bottom):
                if renpy.random.randint(0,1) == 0:
                    "She pulls on a pair of [temp_bottom.display_name], fastening them at the waist."
                else:
                    "She steps into a pair of [temp_bottom.display_name], flattering her legs once again."
            else:
                if temp_bottom.slut_value > 5:
                    "Next comes the [temp_bottom.display_name] - so short that it doesn't even seem worth wearing."
                    if temp_panties:
                        "In fact, you still have an excellent view of her [temp_panties.display_name]."
                    else:
                        "Her [the_person.pubes_description] pussy still on full display for you, and everyone else."
                else:
                    if temp_bottom.slut_value > 4:
                        "Next comes the [temp_bottom.display_name] - short enough to show off all of her long legs, and probably raise a few eyebrows."
                    elif temp_bottom.slut_value > 1:
                        "Next comes the [temp_bottom.display_name] - short enough to show off those lovely legs but modest enough not to raise eyebrows if worn outside."
                    else:
                        "Then comes the [temp_bottom.display_name]. Snug around her waist, accentuating her hourglass figure."
                    if not temp_panties:
                        "Without a pair of panties on, she leaves her pussy open to the air all day."
            $ temp_outfit.add_lower(temp_bottom.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
    if temp_top:
        while len(top_list) > 0:
            $ temp_top = top_list.pop(0)
            if temp_top in real_dress_list:
                if renpy.random.randint(0,1) == 0:
                    "After much deliberation, she settles on a [temp_top.display_name] that barely covers her ass cheeks and hugs every curve of her body tightly."
                else:
                    "As she steps into the [temp_top.display_name], she lets out a contented sigh."
                    "The fabric falls gracefully around her body, hugging her curves just enough to accentuate them without being too revealing."
                    "She adjusts the top on her shoulders, making sure it sits perfectly against her skin."
                if not temp_panties:
                    "Without a pair of panties on, she leaves her pussy open to the air all day."
            elif not temp_top in [lab_coat, suit_jacket, vest]:
                if renpy.random.randint(0,1) == 0:
                    "Finally, there's the top: a crisp [temp_top.display_name] that hugs her curves perfectly."
                else:
                    "She pulls the [temp_top.display_name] down over her chest so that it fits snugly against her body."
            else:
                if renpy.random.randint(0,1) == 0:
                    "She weaves her arms through the [temp_top.display_name], pulling it up to her shoulders."
                else:
                    "She threads her arms through the [temp_top.display_name], lifting it up to her shoulders."
            $ temp_outfit.add_upper(temp_top.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
        if not temp_bra:
            "Without a bra, you can see the faintest hint of her nipples poking into the fabric of her top."
        else:
            "The clothes are snug around her [the_person.tits_description], emphasizing the shape of her chest."
    while len(foot_list) > 0:
        $ temp_item = foot_list.pop(0)
        if not temp_item.constrain_regions:
            if temp_item.display_name == "socks":
                $ temp_outfit.add_feet(temp_item.get_copy())
                $ scene_manager.update_actor(the_person, temp_outfit)
                "She also chooses a pair of [temp_item.display_name] that complement the rest of her outfit."
            else:
                $ temp_outfit.add_feet(temp_item.get_copy())
                $ scene_manager.update_actor(the_person, temp_outfit)
                "She also chooses a pair of [temp_item.display_name], slowly rolling them up her legs and smoothing them out."
        elif temp_item.constrain_regions:
            $ temp_outfit.add_feet(temp_item.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
            "Afterwards, she steps into a fresh set of [temp_item.display_name]."
        else:
            $ temp_outfit.add_accessory(temp_item.get_copy())
            $ scene_manager.update_actor(the_person, temp_outfit)
            "Finally she completes her ensemble with matching accessories."
    $ del temp_bra
    $ del temp_panties
    $ del temp_bottom
    $ del temp_top
    $ scene_manager.clear_scene()
    return new_outfit

label morning_test():
    $ scene_manager = Scene()
    $ camera_list = mc.business.event_triggers_dict.get("home_cameras", [])
    call screen main_choice_display(build_menu_items([get_sorted_people_list(camera_list, "Footage review", "Back")]))
    $ the_person = _return
    $ scene_manager.add_actor(the_person)
    $ x = 0
    menu:
        "Sleeping in bed":
            while x < 100:
                "Sluttiness = [x]"
                $ temp_outfit = get_pajama_outfit(the_person, sluttiness = x)
                call sleeping_in_bed(the_person, x) from _call_sleeping_in_bed_test
                $ x +=1
        "Alarm wake up":
            while x < 100:
                "Sluttiness = [x]"
                $ temp_outfit = get_pajama_outfit(the_person, sluttiness = x)
                call alarm_wake_up(the_person, x) from _call_alarm_wake_up_test
                $ x +=1
        "Natural wake up":
            while x < 100:
                "Sluttiness = [x]"
                $ temp_outfit = get_pajama_outfit(the_person, sluttiness = x)
                call natural_wake_up(the_person, x) from _call_natural_wake_up_test
                $ x +=1
        "Bedroom strip":
            while x < 100:
                "Sluttiness = [x]"
                $ temp_outfit = get_pajama_outfit(the_person, sluttiness = x)
                call bedroom_strip(the_person, x) from _call_bedroom_strip_test
                $ x +=1
        "Bedroom dress":
            while x < 100:
                "Sluttiness = [x]"
                call bedroom_dress(the_person, x) from _call_bedroom_dress_test
                $ x +=1
    $ del camera_list
    $ scene_manager.clear_scene()
    return
