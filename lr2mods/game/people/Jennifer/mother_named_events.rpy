#Named events are for unique character specific overrides to generic labels.
# init 2 python:

# Kina's Take Jennifer Home event
label jennifer_date_take_home_her_place(date_type = None): #Your date went well and you go back to her place. This event starts off when you enter the door.
    $ the_person = mom
    $ noisy_neighbor = False
    $ spend_the_night = False
    $ door_sex = False
    $ the_report = None

    # exclude her from any work duties
    $ the_person.change_location(hall)
    $ mc.change_location(hall)

    #date_type can be passed through to identify what type of date it was to trigger different dialogue
    #if the_person.is_affair:
    #    $ mc.change_location(the_person.home)

    #    call fuck_date_event(the_person) from _call_fuck_date_event_1 #You're having an affair, leads to all of the normal affair stuff like being caught. #TODO: Make sure the date seduction dialogue leads into this properly.
    #    return "Advance Time"
    # KiNA's Note : It's our home, and she never have affair in any of my games so far, needs checking thus commented out.

    #First, check and see if we just fuck her as soon as we walk in the door
    if her_place_door_fuck_check(the_person):
        $ mc.change_location(hall)
        if the_person.arousal_perc >= 70:   #She comes after MC eagerly
            "You're barely in the door before [the_person.title] has her hands all over you."
            the_person "Fuck, I can't wait any longer [the_person.mc_title]! I've been thinking about this all night long!"
            $ mc.change_locked_clarity(20)
            $ the_person.draw_person(position = "kissing")
            "She puts her arms around you and kisses your neck, grinding her body against you."
            mc.name "Don't you want to go to your bedroom first?"
            if aunt_living_with_mc():
                mc.name "Becky might hear us."
                the_person "I told her where I stashed my wine. She probably drunk herself out already."
                mc.name "My... You've prepared."
            elif had_family_threesome():
                mc.name "Lily might caught us."
                the_person "I... We... have our secret agreement. I get to have you tonight."
            else:
                mc.name "Lily might caught us."
                the_person "It's past her bedtime. She's asleep or have her headphone stucked in her ears."
            menu:
                "Fuck her against her front door":
                    "You return the kiss. A moment later [the_person.possessive_title] has her hand down your pants, fondling your cock."
                    the_person "My, what do we have here? It's already hard! Oh my god... I have such a perverted son lusting over his own mother?"
                    "You grab her ass and push her up against the wall, eliciting a moan from her as you begin to grind your body against hers."
                    mc.name "You are my woman now. I'm gonna make you scream all night long."
                    call date_take_home_her_place_fuck_against_door_label(the_person) from _front_door_sex_K01
                    $ the_report = _return
                    $ noisy_neighbor = the_report.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex)
                    $ door_sex = True

                "Insist on the bedroom":
                    the_person "Come on, how do you want me?"
                    mc.name "Patient [the_person.title], I'm not going anywhere. I promised. Let's go inside, first."
                    "She steps back. An awkward silence hangs for a few moments before she nods shyly."

                "Turn her down":
                    $ the_person.draw_person()
                    "You push her back firmly. She seems confused and tries to kiss you again, but you don't let her."
                    mc.name "Not tonight, [the_person.title]. You need to get yourself under control."
                    the_person "What? All those flirting... Don't lie to your own mother, please! I need this."
                    mc.name "I was thinking about it, but you're acting like the only thing you care about is getting at my cock!"
                    mc.name "Now I just want to head to my room. Maybe you'll calm down."
                    $ the_person.change_stats(happiness = -20, love = -(2 + the_person.opinion.taking_control))
                    if the_person.is_dominant:
                        the_person "If you felt like that why did you start flirting at the restaurant?"
                        the_person "Do you really intent to treat your own mother like a whore?"
                        "She scoffs and backs away from you."
                        the_person "Whatever, if that's how you feel then fine. Go and reflect on your behaviour in your room."
                        mc.name "Right. Have a good night [the_person.title]."
                        "She sighs unhappily and watches you leave."

                    "[the_person.possessive_title!c] deflates like a balloon. She steps back."
                    the_person "I... I'm sorry [the_person.mc_title], I didn't know you felt like that."
                    "An awkward silence hangs for a few moments before you speak again."
                    mc.name "I'm going to my room. Have a good night."
                    "[the_person.title] watches you leave, then sulks back inside her own."
                    return "Advance Time"
        else:
            "She pauses for a moment, looking at you. It is like she is waiting for you to do something."
            "Your libido spikes. You wonder how she would react if you just took her right here, up against her front door."
            menu:
                "Fuck right here":
                    "You step toward her. She lifts up her arms and puts them around your neck as you begin to make out."
                    $ mc.change_locked_clarity(20)
                    $ the_person.draw_person(position = "kissing")
                    "You push her body against the wall as you eagerly make out. She moans into your mouth as you grind your body into hers."
                    $ the_person.change_arousal(10)
                    call date_take_home_her_place_fuck_against_door_label(the_person) from _front_door_sex_K02
                    $ the_report = _return
                    $ noisy_neighbor = the_report.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex)
                    $ door_sex = True
                "Wait for her to continue":
                    $ finish_type = her_place_get_finish_type(the_person)


    # Fuck in the hallway, or atleast present it as an option
    if door_sex:
        $ spend_the_night = her_place_spend_the_night_check(the_person, the_report)
        $ the_person.draw_person(position = "stand3")
        "You gather your clothes off the floor."
        the_person "That was nice, but..."

        #Next, determine if we got caught by Lily
        if noisy_neighbor: #There are other people in the apartment and you made a lot of noise.
            call jennifer_date_take_home_her_place_noisy_roomate_door_fuck_label(the_person) from _noisy_sex_at_front_door_K01





    # Next, decide what one night stand action we are going to take.
    # If the girl has lower scores, she may suggest a relatively innocent 'netflix and chill'
    # At higher obedience, she may offer to service MC
    # At higher love score, offer the chance to make out, then take things to the bedroom.
    # At high slut score, she changes into lingerie to seduce MC.
    $ finish_type = her_place_get_finish_type(the_person)

    #The next 4 sequences return True of if there is a possibility of spending the night, otherwise False
    if finish_type == "TV":
        call jennifer_date_take_home_her_place_tv_finish_label(the_person) from _date_her_place_TV_finish_K01
        $ spend_the_night = _return
    elif finish_type == "Slut":
        call jennifer_date_take_home_her_place_lingerie_finish_label(the_person) from _date_her_place_lingerie_finish_K01
        $ spend_the_night = _return
    elif finish_type == "Obedience":
        call jennifer_date_take_home_her_place_service_offer_label(the_person) from _date_her_place_service_offer_finish_K01
        $ spend_the_night = _return
    else:
        call jennifer_date_take_home_her_place_romance_finish_label(the_person) from _date_her_place_romance_finish_K01
        $ spend_the_night = _return


    if spend_the_night:
        $ mc.change_location(mom_bedroom)
        $ the_person.change_location(mom_bedroom)
        $ the_person.draw_person(position = "missionary")
        # "She plops down on her bed sprawling."
        # the_person "That was...amazing."
        # "She whispered, her voice soft and sated. You kissed her forehead, your hands stroking her hair as you lay there together."
        # mc.name "You are amazing."
        # "She sighed, her fingers tracing lazy circles on your chest as she nestled closer to you."
        # "You both lay there in silence for a while, the world outside disappearing as you focused on each other."
        # "The night stretched on, the hours slipping away as both basked in the warmth of your connection."
        # "Eventually, exhaustion overtook both of you, and you drifted off to sleep."
        # "Your bodies entwined, hearts beating as one. The last thing you remember before falling asleep was the feel of her breath against your skin, her warmth enveloping you as you held her close."
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_her_place_K01
        return

    "You head for your bedroom."
    $ mc.change_location(bedroom)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_her_place_K02
    return

label jennifer_date_take_home_her_place_fuck_against_door_label(the_person): #Use this label if you fuck her right inside her front door.
    "You pinned her to the front door, her body pressed flush against you. Her breath was warm against your neck, her lips brushing your skin."
    $ mc.change_locked_clarity(20)
    mc.name "I'm going to pin you to your front door and fuck you here."
    if the_person.opinion.public_sex < 0:
        if aunt_living_with_mc():
            mc.name "Becky might hear us. Or worse, Gabby!"
            mc.name "And they going to see you getting pounded by me~"
            mc.name "What will they think of {i}you{/i}?"
            the_person "NO! Wait... I...I don’t know if I can do this, they can't know about us! Let's go to my room!"
            mc.name "Well, control your screams or they'll caught us for sure then."
        elif had_family_threesome():
            mc.name "Lily might caught us."
            the_person "We...We had an agreement. I get to have you tonight."
        else:
            mc.name "Lily might caught us."
            the_person"Oh... I don't know... I'm not sure I can stay quiet, what if she really do hear?"
    elif the_person.opinion.public_sex < 2:
        if aunt_living_with_mc():
            mc.name "Becky might hear us. Or worse, Gabby!"
            mc.name "And they going to see you getting pounded by me~"
            mc.name "What will they think of {i}you{/i}?"
            the_person "I'll be quiet. They won't hear us."
            mc.name "Well, control your screams or they'll caught us for sure then."
        elif had_family_threesome():
            mc.name "Lily might caught us."
            the_person "We...We had an agreement. I get to have you tonight."
        else:
            mc.name "Lily might caught us."
            the_person"Oh... I don't know... I'm not sure I can stay quiet, what if she really do hear?"
        the_person "Oh fuck... let's do it! I think I can stay quiet enough the neighbors won't hear..."
        "She doesn't seem particularly worried about it though."
    else:
        if aunt_living_with_mc():
            mc.name "Becky might hear us. Or worse, Gabby!"
            mc.name "And they going to see you getting pounded by me~"
            mc.name "What will they think of {i}you{/i}?"
            the_person "My heart is beating like crazy right now thinking about it."
            mc.name "Let them hear."
        elif had_family_threesome():
            mc.name "Lily might caught us."
            the_person "We...We had an agreement. I get to have you tonight."
            the_person "So fuck me! Make me cum all over your big cock and make me scream for her to hear!"
        else:
            the_person "I've done pretending for too long, I can’t pretend anymore."
        "She seems more excited than ashamed at the idea of her family hearing lustful voices."
    if not the_person.vagina_available:
        $ the_person.strip_to_vagina(prefer_half_off = False, position = "kissing")
        "You quickly reach down and strip off anything between you and her cunt, making a small pile on the floor."
    "You fumbled with your zipper, freeing your hard cock. The cool air hit you, but you barely noticed. "
    $ the_person.draw_person(position = "against_wall")
    "[the_person.possessive_title!c] wrapped her legs around your waist, her arms clinging to your shoulders. As you pinned her against the door, your body pressed tightly against hers. "
    "All you could focus on was [the_person.title], the way her body fit against you, the way her breath hitched as you positioned himself at her pussy."
    if the_person.has_taboo("vaginal_sex"):
        the_person "Oh my god... I... I can’t believe this is happening... with my own son!"
        "Although her words are unsure, you could feel the heat of her, the desperate need radiating from her."
    elif the_person.has_taboo("condomless_sex"):
        the_person "Oh my god... I forgot to ask you to put a condom on..."
        if the_person.opinion.bareback_sex < 0:
            "She seems hesitant to let you continue bare, but doesn't make the jump to telling you to put one on."
        "Although her words are unsure, her legs pull your body into hers, making it clear she wants this as much as you do."
    "You pushed into her slowly, savoring the feel of her tight warmth enveloping you. She gasped, her nails digging into your shoulders. "
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(20)
    "You could feel her walls clenching around you, pulling you deeper. You paused, letting her adjust to you, but she wasn’t having it. She rolled her hips, urging you on."
    $ play_moan_sound()
    "The sound of flesh meeting flesh filled the hallway, mingling with both ragged breaths."
    if aunt_living_with_mc():
        "She moaned, her voice barely contained, but the thought of [aunt.possessive_title] in the living room only spurred you on."
    else:
        "She moaned, her voice barely contained, but the thought of [lily.possessive_title] upstairs only spurred you on."
    if the_person.wants_creampie:
        the_person "Oh fuck that is so deep... Are you... are you going to cum inside me like this?"
    else:
        the_person "Oh fuck that is so deep... You aren't going to cum inside me like this, are you?"
    mc.name "Maybe. I haven't decided yet."
    "You give your hips a gentle thrust, getting a feel for the angle and penetration depth."
    the_person "MMMM... ahh... okay..."
    call fuck_person(the_person, private = True, condition = make_condition_apartment_door_sex(), start_position = against_wall, start_object = make_door(), skip_intro = True, girl_in_charge = False, position_locked = False, skip_condom = True) from _call_fuck_date_against_front_door_K01
    $ the_report = _return
    return the_report

label jennifer_date_take_home_her_place_noisy_roomate_door_fuck_label(the_person):
    "Upstairs, a door creaked open. Both of you froze, bodies tensing. The sound of footsteps padding down the hallway sent a jolt of panic through both of you."
    $ the_person.draw_person(position = "stand2")
    lily "Mom? [lily.mc_title]?"
    if had_family_threesome():
        the_person "Yes, dear... it's us."
        lily "Figures. You guys being too loud. I can hear you from my room."
        mc.name "Sorry, blame Mom, she's the one who screamed!"
        "[the_person.title!c] gave you an angry pinch on your waist."
        lily "Oh well, have fun... I'm going back to sleep. Oh, and [lily.mc_title], you owe me a date!"
        mc.name "Absolutely!"
    else:
        "[the_person.possessive_title!c]’s body tense beneath your own, her chest rising and falling rapidly as she stared up at him, her eyes wide with a mix of fear and lust."
        the_person "Let me handle this."
        "“Mom?” Lily's voice came again, closer now, followed by the soft creak of the stairs."
        "[the_person.possessive_title!c] straighten out her looks and strut forward like nothing happened."
        the_person "Yes, dear. I just got back home. Is something a matter?"
        "[lily.possessive_title!c] flickers a bit suspiciously."
        lily "I thought I heard [mc.name] as well just."
        the_person "Yeah, we just happened to arrive at the same time. Go back to bed."
        "Lily narrows her eyes once again at both of you before silently goes back to her room."
        mc.name "That was close."


    # "In this label, as we walk with [the_person.title] to her bedroom, her flatmate complains about you having noisy sex in the hall."
    # "At the end of it, you go to her bedroom."
    return True

label jennifer_date_take_home_her_place_meet_roomate_label(the_person):
    pass
    # "In this label, as we walk into [the_person.title]'s apartment, her flatmate is there and we meet her."
    # "At the end of this interaction, return True if we continue on the normal date path."
    # "Use False if we aren't, EG we decided to have a threesome, or the flatmate got pissed and chased us out."
    return True

label jennifer_date_take_home_her_place_tv_finish_label(the_person):
    the_person "I hope you aren't too sleepy, I was thinking about watching a movie."
    mc.name "Sounds good to me."
    the_person "Okay!"
    $ popup_text = date_take_home_her_place_tv_finish_popup_text(the_person)
    $ show_popup_hint(popup_text)
    "You and [the_person.possessive_title] walk into your living room and sit down on the couch."
    $ the_person.draw_person(position = "sitting")
    "She grabs the remote and fires up a streaming service. Soon a movie is playing but you couldn't care less what is happening with it."
    $ the_person.draw_person(position = "sitting", display_transform = character_center_focus)
    "After the intro, [the_person.title] scoots over, her body now up against yours. She lays her head on your shoulder and softly sighs."
    the_person "Mmm, this is nice..."
    "You put your arm around her. You try to pay attention to the movie but it is impossible with her body up against yours."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(20)
    "Slowly, you let your hand slide down her shoulder, across her collarbone, and down to her breast..."
    #TODO go through and do all the  taboo breaks for this scene
    if the_person.is_willing(standing_grope) or the_person.is_willing(standing_finger):
        "She sighs when she feels you start to feel her up. She turns her head towards you."
        the_person "Mmm, that feels nice..."
        "She nuzzles up against you and starts to kiss your neck. You take it as a sign that she is eager for you to continue."
        $ mc.change_locked_clarity(20)
        $ the_person.change_arousal(5)
    else:
        "When you give her a little grope, she jumps, surprised at your forwardness."
        "She pushes your hand back up onto her shoulder."
        the_person "What are you doing?"
        mc.name "Sorry..."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    if mc.sex_skills["Foreplay"] < 2:
        "You clumsily grope her tit for a few minutes while she gives occasional kisses on your neck."
        "You start to move your head down to meet her lips with yours, but she pulls back."
        the_person "Ahh, are you seriously trying to kiss your mother on her lips?"
        mc.name "Yes."
        the_person "We can't. We are family."
        "She puts her hand on yours. She lets you leave your hand on her chest, but she stops you from actively groping her and goes back to watching the movie."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your time bonding with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    else:
        "You softly grope her, mixing it up, sometimes rubbing softly, sometimes teasing her nipple, and sometimes groping forcefully."
        "She moans into you as she begins to eagerly lick, suck, and kiss the side of your neck."
        "After several seconds, she stops."
        the_person "Oh god, that feels so good...It's wrong, but ..."
        "You look down at her and see her looking at your lips. You lean forward and she pushes up, your lips meeting together."
        "She opens her mouth and you begin to make out with [the_person.possessive_title] while your hand keeps groping her."
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(10)
    if mc.sex_skills["Foreplay"] < 4:
        "You make out with [the_person.possessive_title] for several minutes."
        "Your tongues lash against each other, and you eagerly grope her chest."
        "However, things eventually start to slow down, and she eventually pulls back."
        the_person "Ahh, you make me feel good, but we really shouldn't cross the line... We are still mother and son..."
        "Your cock aches a bit in disappointment, but you don't want to push her into anything she doesn't want to do."
        mc.name "I understand."
        "She leans back against you, putting her head on your chest."
        $ the_person.change_love(5, 40)
        "She appreciates you respecting her boundaries."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False
    else:
        "You make out passionately with [the_person.possessive_title] for several minutes."
        "You can feel the heat building between you two when you finally feel her hand on your body."
        "[the_person.title]'s hand has started to stroke your cock in your pants as you make out. You make sure to moan your approval into her mouth."
        "Thankfully, it appears that you are going to get far enough with [the_person.title] tonight to at least cum, from the way things are going."
        "She stops making out with you and looks down at your lap. She uses both hands and starts to fumble with your pants."
        "You lift up your hips as she pulls them down and off, your cock springing free."
        the_person "Oh fuck, you're so big!..."
        "She begins to stroke you with her hand again, this time skin on skin. She looks you in the eyes."
        if the_person.is_willing(blowjob):
            the_person "I want to taste it. I want to feel this monster in my mouth!"
        else:
            the_person "Fuck, I never do this but... I want to taste it! Can I taste it?"
        mc.name "Of course."
        "She gets up for a moment and turns, laying down on her stomach with her head on your lap."
        $ the_person.draw_person(position = "walking_away", display_transform = character_center_focus_flipped_test)
        "You put your hand on the back of [the_person.possessive_title]'s head as she slides her tongue up and down your cock a few times."
        if the_person.vagina_available:
            "You reach over with your other hand up between her legs."
        else:
            "You reach over with your other hand and slide it down her bottoms, along her backside and between her legs."
        "The angle is a little awkward but you manage to slide your middle finger along her pussy, feeling how wet she has gotten."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "After several seconds of teasing each other, [the_person.title] moves her mouth up to the tip of your cock, then opens her mouth and slides it inside."
        "At the same time, you slide your middle finger into her, causing a moan to reverberate around her now full mouth."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
    # if mc.max_energy < 140 or mc.sex_skills["Oral"] < 4: #Cum in her mouth
        "You can feel her ass pushing up, eagerly accepting your finger inside her."
        "[the_person.title]'s mouth working your cock is really turning you on, combined with her moans you can barely concentrate on fingering her."
        $ mc.change_arousal(15)
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "The angle of your hand around her back side makes it difficult for you to finger her properly, but you work it as best as you can."
        "Her mouth is really getting you turned on, you make sure to voice how good it feels."
        mc.name "Mmm, damn, that feels amazing [the_person.title]. I'm not going to last long if you keep going like that."
        the_person "Mmmmm, mmmhmmm..."
        "She doesn't stop sucking you, just murmurs her approval with a throaty moan."
        $ mc.change_arousal(25)
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "You do your best to make her feel good too, but after another minute of her oral attention, you feel yourself getting ready to orgasm."
        mc.name "Oh fuck, [the_person.title], that's it, I'm gonna cum!"
        $ mc.change_arousal(25)
        $ mc.change_locked_clarity(50)
        if the_person.facial_or_swallow() == "swallow":
            the_person "Mmmm..."
            "Her mouth keeps going, and you feel yourself peak and begin to cum into her mouth."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
            "You fill her mouth with wave after wave of cum. She lets out a couple gasps and when you finish, you hear as she gulps it down."
            $ play_swallow_sound()
            "For a few blissful moments, you revel in your post orgasm haze."
        else:
            "Suddenly, her mouth pops off your cock with a pop, and she starts stroking you with her hand."
            the_person "Mmm, that's it, cum for me!"
            $ the_person.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", person = the_person)
            "You begin to orgasm. Her head is blocking your view, but she is letting you cover her face with your seed."
            "After several waves, your orgasm winds down, and for a few blissful moments, you revel in your post orgasm haze."
        $ the_person.draw_person(position = "missionary", display_transform = character_center_focus_flipped_test)
        "She turns over onto her back. When she does so, your pull you hand back from between her legs."
        the_person "Mmm, that was nice, but I'm almost there!"
        "She takes your hand puts it back between her legs. You easily slide two fingers inside of her."
        the_person "Mmmmmm, yessss!"
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(15)
        "This position makes it much easier for you to finger her and to stimulate her g-spot. She closes her eyes and moans."
        the_person "Ohhhh, that's it [the_person.mc_title]... right there..."
        "Suddenly, you feel her whole body tense up and she has her own orgasm."
        $ the_person.change_arousal(35)
        $ the_person.have_orgasm()
        the_person "Yes!!! Oh!"
        "She body quivers as she orgasms. You eagerly finger her through the spasms until she starts to come down."
        "She lays there for several seconds with her head on your lap as she recovers."
        the_person "Wow... that was nice..."
        $ the_person.apply_planned_outfit()
        "She quickly hops up and cleans up her face and then comes back."
        $ the_person.draw_person(position = "missionary", display_transform = character_center_focus_flipped_test)
        "You watch the rest of the movie together with [the_person.possessive_title] while she lays her head in your lap."
        "You watch a movie together, just enjoying your proximity with [the_person.possessive_title]."
        the_person "I should probably go to sleep now.."
        the_person "Thank you for a wonderful date [the_person.mc_title]."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "After giving you a long kiss, she steps back."
        $ the_person.draw_person(emotion = "happy")
        mc.name "You're welcome, [the_person.title]!"
        return False

    # else:   #Make her cum first
    #     "As you start to finger her, you realize the angle is a bit awkward, but you are determined to get her off."
    #     "[the_person.possessive_title!c]'c warm, wet mouth feels good, but you focus on her first."
    #     $ mc.change_arousal(15)
    #     $ mc.change_locked_clarity(50)
    #     $ the_person.change_arousal(15)
    #     "You realize there is a pillow on the side of the couch, so you quickly grab it. You have her stop for a second and slide it under her."
    #     "The pillow forces her hips up a little higher, giving you a better angle for penetrating her with your fingers, and so you continue."
    #     $ play_moan_sound()
    #     the_person "Mmmmmm.... slllck... mmmm.... slllp sllp"
    #     "She begins to moan around your cock along with the occasional slurping noises as she sucks you off."
    #     $ mc.change_arousal(15)
    #     $ mc.change_locked_clarity(50)
    #     $ the_person.change_arousal(25)
    #     the_person "Mmmmm!... OH fuck!"
    #     "After a particularly urgent moan, she pulls away from your cock and strokes it a couple times with her hand."
    #     the_person "Fuck, I'm... I'm gonna cum...!"
    #     $ the_person.change_arousal(25)
    #     $ the_person.draw_person(position = "back_peek", display_transform = character_center_focus_flipped_test, emotion = "orgasm")
    #     "She looks up at you with her mouth open as she moans and begins to orgasm."
    #     $ the_person.have_orgasm(half_arousal = True)
    #     "Her eager moans are music to your ears as she cums from your touch."
    #     "After several seconds, her moans begin to slow down."
    #     the_person "Wow! That felt so good... I want to make you feel good too...!"
    #     $ the_person.draw_person(position = "walking_away", display_transform = character_center_focus_flipped_test)
    #     "She turns her face back to your cock. You feel her mouth lick up and down the sides a few times, then you feel her mouth engulf your erection."
    # if mc.sex_skills["Foreplay"] < 6 or mc.max_energy < 160:   #Cum in her mouth while she has a second orgasm
    #     "[the_person.title]'s orgasm has caused her to redouble her efforts to suck you off."
    #     "You keep fingering her as well. You aren't sure if you'll be able to get her off again, but you figure it is worth trying."
    #     $ mc.change_arousal(15)
    #     $ mc.change_locked_clarity(50)
    #     $ the_person.change_arousal(25)





    # else:   #She orgasms again and sets up to ride cowgirl




    # if mc.sex_skills["Vaginal"] < 6 or mc.max_energy < 180:    #Cowgirl orgasm





    # else:   #She orgasms a third time and is exhausted, MC rides her prone bone


    return False

label jennifer_date_take_home_her_place_service_offer_label(the_person):
    the_person "Do you... erm.. do you want to ... I mean.. we could go back to my room, and I could show you just how much [the_person.possessive_title] appreciate it..."
    if the_person.is_willing(anal_standing) and the_person.is_willing(standing_doggy) and the_person.is_willing(blowjob):
        the_person "You can pick any hole you want and have your way with it. I wouldn't mind!"
    elif the_person.is_willing(anal_standing):
        the_person "I could bend over the side of the bed and let you pick a hole..."
        the_person "You could stick it in my butt if you want. I wouldn't mind!"
    elif the_person.is_willing(standing_doggy):
        the_person "I could bend over the side of the bed and let you fuck me as hard as you want. I wouldn't mind!"
    elif the_person.is_willing(blowjob):
        the_person "I could get on my knees and service you with a nice blowjob if you want. I don't mind!"
    else:
        the_person "I think we could figure out a way to make it feel good for you. I don't mind!"
    mc.name "That's a nice offer..."
    menu:
        "Get serviced":
            mc.name "I'd be an idiot to say no. Let's do it."
            the_person "Mmm, okay! Let's go..."
            $ the_person.change_to_bedroom()
            mc.name "Alright, first things first. Get naked."
            "She turned to face you, slowly backing up to the bed."
            "Her hands went to the straps of her dress, and slipped them down her shoulders with a deliberate slowness."
            $ the_person.change_arousal(5)
            the_person "As you wish, [the_person.mc_title]..."
            $ the_person.strip_outfit(position = "stand3")
            $ mc.change_locked_clarity(20)
            the_person "Do you like what you see?"
            "She ran her hands down her sides, her nails lightly grazing her skin, as she stand waiting."
            menu:
                "Fuck her Tits" if the_person.has_large_tits and the_person.is_willing(tit_fuck):
                    mc.name "Get on your knees. I want to have some fun with those amazing tits of yours."
                    "[the_person.possessive_title!c] quickly drops to her knees."
                    $ the_person.draw_person(position = "blowjob")
                    "She takes her considerable tits in her hands as you step over to her, looking up at you with a smile."
                    the_person "Go ahead. Use [the_person.possessive_title] tits to make yourself feel good!"
                    "You push your cock into the valley of her ample titflesh."
                    $ mc.change_locked_clarity(30)
                    "She begins to stroke your cock with her breasts, using her hands to control the tempo."
                    call fuck_person(the_person, private = True, start_position = tit_fuck) from _call_fuck_person_her_place_service_tit_fuck_K01
                    $ the_person.call_dialogue("sex_review", the_report = _return)

                "Fuck her Mouth" if the_person.is_willing(blowjob):
                    mc.name "Get on your knees. I want to feel those pouty lips of yours around my cock."
                    "[the_person.possessive_title!c] quickly drops to her knees."
                    $ the_person.draw_person(position = "blowjob")
                    "She licks her lips, staring at your cock as you step over to her."
                    "[the_person.title] looks up at you and opens her mouth, silently waiting for you to use her."
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "You put your hand on the back of her head and gently guide her mouth onto your erection."
                    $ mc.change_locked_clarity(40)
                    "You feel a gently moan as your cock slides into her mouth. You let go of her head and she begins to suck you off."
                    call fuck_person(the_person, private = True, start_position = blowjob) from _call_fuck_person_her_place_service_blowjob_K01
                    $ the_person.call_dialogue("sex_review", the_report = _return)

                "Fuck her Pussy" if the_person.is_willing(standing_doggy):
                    mc.name "Bend over the bed. Let me see what I'll be working with tonight."
                    "[the_person.possessive_title!c] quickly obeys, bending over her bed and preseting her ass to you."
                    $ the_person.draw_person(position = "standing_doggy")
                    "She looks back at you, hungrily, watching as you step over to her."
                    "You grab [the_person.title]'s hips and you push yourself up against her, grinding your dick against her ass."
                    $ the_person.change_arousal(10)
                    "She moans and grinds back against you a bit. Soon, you're ready for more."
                    "You use one hand to point your cock down and then push your hips forward, letting your cock slide inside her."
                    $ mc.change_locked_clarity(50)
                    "Once you are all the way in, you move your hand back to her hip and giver her a couple thrusts. Time to fuck this slut."
                    call fuck_person(the_person, private = True, start_position = standing_doggy, skip_condom = True) from _call_fuck_person_her_place_service_doggy_K01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                "Fuck her Ass" if the_person.is_willing(anal_standing):
                    mc.name "Bend over your bed and show me these holes you mentioned."
                    "[the_person.possessive_title!c] quickly obeys, bending over her bed and preseting her ass to you."
                    $ the_person.draw_person(position = "standing_doggy")
                    "She looks back at you, hungrily, watching as you step over to her."
                    "You grab [the_person.title]'s hips and you push yourself up against her, grinding your dick against her ass."
                    $ the_person.change_arousal(10)
                    "She moans and grinds back against you a bit. Soon, you're ready for more."
                    mc.name "Do you have any lube?"
                    the_person "Oh, yeah! One second..."
                    "She reaches over to her bedside table and grabs some lubricant, quickly passing it to you."
                    "You quickly apply ample amounts. Your cock and her puckered hole now glisten from it."
                    "You use one hand to point your cock down and then push your hips forward."
                    "There are several moments of resistance as your erection slowly loosens and then pushes inside her sphincter."
                    $ mc.change_locked_clarity(70)
                    "When it finally gives way, you easily slide all the way in."
                    "You give [the_person.title] Time to fuck this slut."
                    call fuck_person(the_person, private = True, start_position = anal_standing, skip_condom = True) from _call_fuck_person_her_place_service_doggy_anal_K01
                    $ the_person.call_dialogue("sex_review", the_report = _return)

                "Just fool around":
                    mc.name "Why don't we just fool around some? No need for anything specific."
                    the_person "Mmm, okay!"
                    $ the_person.change_to_bedroom()
                    call fuck_person(the_person, private = True) from _call_fuck_person_her_place_service_fool_around_K01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
        "Not tonight":
            mc.name "Sorry, I don't have time for that tonight, but I appreciate the offer."
            the_person "Huh? Really?"
            "She seems shocked at your answer, but is obedient enough to know not to second guess it."
            $ the_person.change_stats(happiness = -20, love = -2)
            the_person "Ok... well... maybe another time then..."
            mc.name "I should probably get going."
            the_person "Right..."
            "You say goodnight and leave, heading back to your room."
            return False
    $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
    the_person "That was good, but you really wore me out."
    if spend_the_night:
        the_person "You could sleep here... If you want."
        menu:
            "Stay the night":
                mc.name "Yeah that sounds good. I'm definitely worn out."
                the_person "Ah, lovely..."
                return True
            "Head out":
                "You gives her forehead a kiss before picking up your clothes."
                mc.name "Well, I better go back to my room."
                if lily_knows_about_mom():
                    mc.name "Don't want Lily to catch us sleeping together."
                    the_person "What's wrong with us sleeping together?"
                    the_person "It's not like it's a secret anymore."
                else:
                    mc.name "Don't want Lily to catch us sleeping together."
                    the_person "That's true."
                    the_person "Oh... I hope she didn't hear any of that."
                    "She blushes red at the thought."
                    the_person "Thank you for a wonderful date [the_person.mc_title]."

    the_person "I should probably see you out..."
    mc.name "It's just across the hall. Just sleep."
    the_person "Thank you for a wonderful date [the_person.mc_title]."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "After giving you a long kiss, she steps back."
    $ the_person.draw_person(emotion = "happy")
    mc.name "You're welcome, [the_person.title]!"
    return False

label jennifer_date_take_home_her_place_romance_finish_label(the_person):
    "The house felt different tonight, quieter, more intimate."
    "She led you to the living room, where she poured a glass of wine for both of you, her movements slow and deliberate. "
    "When she handed you the glass, your fingers brushed, and you felt a spark of electricity shoot through you."
    $ the_person.draw_person(position = "sitting")
    the_person "Well, what would you like to do now?"
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title!c] leans closer to you and puts her hand on your thigh. It's obvious what she wants, but she's waiting for you to make the first move."
    menu:
        "Kiss her":
            "You put your drink aside, then put one hand on the back of [the_person.possessive_title]'s neck and pull her into a kiss."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            if not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0:
                "She returns the kiss eagerly."
            else:
                "She returns the kiss for a moment, then breaks away. Her lips hover, barely separated from yours."
                the_person "I shouldn't... My [the_person.so_title]..."
                "You kiss her again, and this time all resistance falls away."
            "After a long moment spent making out [the_person.title] pulls away."
            the_person "I think we'd be more comfortable in the bedroom, don't you?"
            $ the_person.draw_person(position = "walking_away")
            mc.name "I couldn't agree more."
            $ the_person.change_to_bedroom()
            "[the_person.possessive_title!c] leads you to her bedroom and starts to undress."
            $ the_person.strip_to_underwear()
            call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_K104
            $ the_person.call_dialogue("sex_review", the_report = _return)
            $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
            the_person "That was...amazing."
            "She whispered, her voice soft and sated. You kissed her forehead, your hands stroking her hair as you lay there together."
            mc.name "You are amazing."
            "She sighed, her fingers tracing lazy circles on your chest as she nestled closer to you. "
            "You both lay there in silence for a while, the world outside disappearing as you focused on each other."
            "The night stretched on, the hours slipping away as both basked in the warmth of your connection."
            if spend_the_night:
                menu:
                    "Stay the night":
                        "Eventually, exhaustion overtook both of you, and you drifted off to sleep."
                        "Your bodies entwined, hearts beating as one. The last thing you remember before falling asleep was the feel of her breath against your skin, her warmth enveloping you as you held her close."
                        return True

                    "Head out":
                        "You gives her forehead a kiss before picking up your clothes."
                        mc.name "Well, I better go back to my room."
                        if lily_knows_about_mom():
                            mc.name "Don't want Lily to catch us sleeping together."
                            the_person "What's wrong with us sleeping together?"
                            the_person "It's not like it's a secret anymore."
                        else:
                            mc.name "Don't want Lily to catch us sleeping together."
                            the_person "That's true."
                            the_person "Oh... I hope she didn't hear any of that."
                            "She blushes red at the thought."
                            the_person "Thank you for a wonderful date [the_person.mc_title]."

            the_person "I should probably see you out..."
            mc.name "It's just across the hall. Just sleep."
            the_person "Thank you for a wonderful date [the_person.mc_title]."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "After giving you a long kiss, she steps back."
            $ the_person.draw_person(emotion = "happy")
            mc.name "You're welcome, [the_person.title]!"

        "Go back to your room":
            mc.name "It's been a fun evening, but I need to be going soon. I hope we can do this again some time though."
            $ the_person.change_happiness(-5)
            "[the_person.possessive_title!c] seems a little disappointed, but she smiles politely."
            if not the_person.has_significant_other or the_person.opinion.cheating_on_men > 0:
                the_person "Of course. It's getting late, I should probably be going to bed as well."
            else:
                the_person "Of course, that's fine. My [the_person.so_title] probably wouldn't like it that I have other men visiting anyways."

            the_person "I had a fun time, we should do this again."
            mc.name "I think I'd like that."
            "You finish your drink and say goodnight to [the_person.title]."

    return False

label jennifer_date_take_home_her_place_lingerie_finish_label(the_person):
    the_person "Wait here a moment, I'll go change."
    $ clear_scene()
    if the_person.opinion.not_wearing_anything > the_person.opinion.lingerie:
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True) #She's wearing nothing at all. nothing at all. nothing at all...

    elif the_person.opinion.lingerie >= 0:
        $ the_person.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness + 20, the_person.sluttiness // 4, guarantee_output = True, preferences = WardrobePreference(the_person)), update_taboo = True) #She's just wearing lingerie for the evening.

    else: #She doesn't like being nude or wearing lingerie, so just strip her to her underwear
        $ the_person.outfit.strip_to_underwear()
    "You sit down on the couch and relax while you wait for [the_person.possessive_title]. A few minutes later she calls out for you."
    the_person "[the_person.mc_title], could you come here?"
    "You down the rest of your drink and leave the empty glass behind, following the sound of her voice."
    "Her bedroom door was slightly ajar, the warm glow of her bedside lamp spilling out into the dimly lit hall."
    mc.name "Yeah, Mom?"
    the_person "Come in..."
    "You pushed the door open slowly, and there she was, sitting on the edge of her bed. "
    $ the_person.draw_person(position = "sitting")
    $ mc.change_locked_clarity(15)
    $ the_person.change_to_bedroom()
    if the_person.is_naked:
        "She is fully naked, baring everything to you."
    elif the_person.opinion.lingerie >= 0:
        "She’ve changed out of her dress and into a silky lingerie that clung to her figure, the fabric hinting at the curves beneath."
        "Her hair was down, cascading over her shoulders in soft waves, and her lips curved into a smile that took your breath away."
    else:
        "She stood there in nothing but her underwear, her curves just took your breath away."
    the_person "Close the door. Don't want Lily to accidentally see us."
    $ the_person.draw_person()
    "She patted the space beside her on the bed, her movements slow and deliberate."
    the_person "Sit with me."
    "A slight hesitation, but you moved toward her, the bed dipping slightly as you sat down."
    if the_person.is_naked:
        "She shifted closer, her thigh pressing against yours, and you could feel the heat of her naked body."
    else:
        "She shifted closer, her thigh pressing against yours, and you could feel the heat of her body."

    menu:
        "Kiss her":
            if the_person.has_taboo("kissing"):
                $ the_person.call_dialogue("kissing_taboo_break")
                $ the_person.break_taboo("kissing")
            mc.name "You're perfect."
            "Without thinking, you leaned in, capturing her lips in a soft, hesitant kiss."
            "[the_person.possessive_title!c] responded immediately, her arms wrapping around his neck as she deepened the kiss."
            call fuck_person(the_person, private = True, start_position = kissing) from _call_fuck_person_K17
            $ the_person.call_dialogue("sex_review", the_report = _return)
            $ spend_the_night = her_place_spend_the_night_check(the_person, _return)
            the_person "That was...amazing."
            "She whispered, her voice soft and sated. You kissed her forehead, your hands stroking her hair as you lay there together."
            mc.name "You are amazing."
            "She sighed, her fingers tracing lazy circles on your chest as she nestled closer to you. "
            "You both lay there in silence for a while, the world outside disappearing as you focused on each other."
            "The night stretched on, the hours slipping away as both basked in the warmth of your connection."
            if spend_the_night:
                menu:
                    "Stay the night":
                        "Eventually, exhaustion overtook both of you, and you drifted off to sleep."
                        "Your bodies entwined, hearts beating as one. The last thing you remember before falling asleep was the feel of her breath against your skin, her warmth enveloping you as you held her close."
                        return True
                    "Head out":
                        "You gives her forehead a kiss before picking up your clothes."
                        mc.name "Well, I better go back to my room."
                        if lily_knows_about_mom():
                            mc.name "Don't want Lily to catch us sleeping together."
                            the_person "What's wrong with us sleeping together?"
                            the_person "It's not like it's a secret anymore."
                        else:
                            mc.name "Don't want Lily to catch us sleeping together."
                            the_person "That's true."
                            the_person "Oh... I hope she didn't hear any of that."
                            "She blushes red at the thought."
                        the_person "Thank you for a wonderful date [the_person.mc_title]."
                        $ mc.change_location(bedroom)
                        return False
            the_person "I should probably see you out..."
            mc.name "It's just across the hall. Just sleep."
            the_person "Thank you for a wonderful date [the_person.mc_title]."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "After giving you a long kiss, she steps back."
            $ the_person.draw_person(emotion = "happy")
            mc.name "You're welcome, [the_person.title]!"

        "Turn her down":
            "Just as you are about to kiss her, you hear something from the hallway."
            lily "Mom? [lily.mc_title]?"
            "[the_person.possessive_title!c] quickly hides her nakedness under the sheet."
            mc.name "Be a sec, actually [lily.fname], can you get a cup of water for mom?"
            lily "Ah... Okay."
            "As her footstep goes down, you turn around to [the_person.possessive_title] apologetically."
            mc.name "I better go back to my room."
            "You gives her forehead a kiss before leaving the room."
            $ the_person.change_stats(happiness = -20, love = -2)
            $ mc.change_location(bedroom)
            return False
    return False


label jennifer_bc_talk_label():
    $ the_person = mom
    mc.name "Can we talk about something?"
    the_person "Mmhm, what's that?"
    mc.name "I want to talk about your birth control."
    if the_person.event_triggers_dict.get("is_changing_birth_control", False):
        the_person "We already talked about that..."
        mc.name "Oh, right."
        $ the_person.update_birth_control_knowledge()
        return


    if the_person.event_triggers_dict.get("mandate_bc", False):
        if the_person.on_birth_control:
            the_person "I'm on birth control, and I'm not going off it any time soon."
            the_person "Things have gotten intimate with me and my boss, but there is NO WAY I'm going to have a baby with him."
            mc.name "That makes sense."
        else:
            the_person "I am actually just going back on birth control"
            the_person "Things have gotten intimate with me and my boss, but there is NO WAY I'm going to have a baby with him."
            mc.name "That makes sense."
            $ manage_bc(the_person, start = True)
        $ the_person.update_birth_control_knowledge()
        return

    if the_person.has_relation_with_mc:
        #She'll talk to you about it. High Love or moderate sluttiness are needed to convince her to stop taking BC. Easier to convince her to start.
        # High influence from opinion of creampies.

        $ needed_start = 30 + (15 * the_person.opinion.creampies)
        $ needed_stop = 45 - (15 * the_person.opinion.creampies)
        if the_person.is_affair:
            $ needed_stop += -10*the_person.opinion.cheating_on_men #They think it's hot to have another man's baby

        if the_person.on_birth_control:
            if the_person.wants_creampie: #She's not happy about it
                the_person "Oh, sure. I'm taking it right now, so if you get a little too excited and unload inside me..."
                "She smiles and shrugs."
                the_person "Well that wouldn't be the end of the world."
            else:
                the_person "Oh, sure. I'm taking it right now, so we shouldn't have any \"accidents\" to worry about."
        else:
            if the_person.wants_creampie: #She's happy about not being on BC
                the_person "I'm not taking any right now, so..."
                "She smiles and shrugs."
                the_person "If you cum in me you might get me knocked up. It's kind of hot to think about that..."
            else:
                the_person "Oh, well... I'm not taking any right now."
        $ the_person.update_birth_control_knowledge()

        menu:
            "Start taking birth control" if not the_person.on_birth_control and the_person.has_event_delay("changed_bc", 7):
                mc.name "You should start taking some, I don't want you getting pregnant."
                if the_person not in (kaya, sakari) and (the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start):
                    "She thinks about it for a moment, then nods."
                    if the_person.has_taboo("condomless_sex"):
                        the_person "It would be nice to not have to worry about a condom breaking when we have sex."
                        the_person "Okay, I'll talk to my doctor and start taking it as soon as possible."
                    else:
                        the_person "If we keep doing it raw that's a smart idea."
                        the_person "I'll talk to my doctor and start taking it as soon as possible."
                    the_person "I should be able to start tomorrow, we will still need to be careful until then."
                    $ manage_bc(the_person, start = True)

                elif the_person.event_triggers_dict.get("refuse_bc", False):
                    "She shakes her head."
                    the_person "I'm sorry, but I have personal reasons for not going on birth control. Please don't ask me to do that."

                else:
                    "She shakes her head."
                    if the_person.wants_creampie:
                        the_person "I don't care about that. I love the thrill of a hot load of cum inside my perfectly fertile pussy."
                        the_person "There's nothing hotter than that. You're just going to have to accept that it's a risk."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "I'm sorry [the_person.mc_title], but I've tried it before and it plays hell with my hormones."
                        the_person "We can just use a condom, or do something else to have fun together."

            "Stop taking birth control" if the_person.on_birth_control and the_person.has_event_delay("changed_bc", 7):
                mc.name "I want you to stop taking it."
                if the_person.love >= needed_stop or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.wants_creampie:
                        the_person "Yeah? I've wanted to stop too, I don't care if it's risky."
                        the_person "There's nothing that's more of a turn-on than having a hot load inside my pussy. Ah..."
                        "[the_person.possessive_title!c] sighs and seems lost in thought for a moment."
                        the_person "Sorry, I'm getting distracted."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "Do you think that's a good idea? What if something happened?"
                        mc.name "We can deal with that when it happens. If we don't want you to get pregnant we can always use a condom."
                        "She thinks about it for a long moment, then nods and smiles."
                        the_person "Okay, I won't take my birth control in the morning. We'll just be careful, it'll be fine..."

                    $ manage_bc(the_person, start = False)

                elif the_person.event_triggers_dict.get("mandate_bc", False):
                    "She shakes her head."
                    if the_person == mom:
                        the_person "I'm sorry, but I can't go off birth control."
                        the_person "Things have gotten intimate between me and my boss, but I don't want him to get me pregnant!"
                        the_person "I can't go off birth control right now. Okay?"
                    else:
                        the_person "I'm sorry, but I have personal reason for being on birth control. Please don't ask me to do that."

                else:
                    if the_person.opinion.bareback_sex > 0:
                        the_person "I don't think that's a good idea. If I'm on my birth control you don't need to wear a condom when we fuck."
                        the_person "I love feeling you raw inside me. I don't want to have to give that up."
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "I don't think that's a good idea. What if something happened? Are we ready for that change in our lives?"
                        the_person "Maybe one day, but I'm not comfortable with it right now."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check on that."

    elif the_person.effective_sluttiness() > 40:
        $ needed_start = 40 + (15 * the_person.opinion.creampies)
        $ needed_stop = 75 - (15 * the_person.opinion.creampies)

        if the_person.on_birth_control:
            if the_person.opinion.bareback_sex > 0:
                the_person "Oh, is that all? Yeah, I'm on birth control right now because I hate how condoms feel."
                $ the_person.discover_opinion("bareback sex")
            else:
                the_person "Oh, is that all? Yeah, I'm on birth control right now so I don't have to worry about getting pregnant."
        else:
            the_person "Oh, I guess that's probably an important thing for you to know about."
            the_person "I'm not taking any birth control right now."

        $ the_person.update_birth_control_knowledge()
        menu:
            "Start taking birth control" if not the_person.on_birth_control and the_person.has_event_delay("changed_bc", 7):
                mc.name "You should probably start taking it, before something happens and you get pregnant."
                if the_person.event_triggers_dict.get("refuse_bc", False):
                    "She shakes her head."
                    the_person "I'm sorry, but I have personal reason for not going on birth control. Please don't ask me to do that."
                elif the_person not in (kaya, sakari) and (the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start):
                    the_person "That's probably a good idea. I'll talk to my doctor as soon as possible about it."
                    $ manage_bc(the_person, start = True)
                else:
                    if the_person.wants_creampie:
                        "She shrugs and shakes her head."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person "I don't care about that. I love the feeling of a warm, risky creampie too much to ever give it up."
                    else:
                        the_person "Sorry, I've tried it before and it just messes with my hormones too badly."
                        the_person "We'll just be careful and use a condom, or you can pull out. Okay?"

            "Stop taking birth control" if the_person.on_birth_control and the_person.has_event_delay("changed_bc", 7):
                mc.name "You should stop taking it. Wouldn't that be really hot?"
                if the_person.event_triggers_dict.get("mandate_bc", False):
                    "She shakes her head."
                    if the_person == mom:
                        the_person "I'm sorry, but I can't go off birth control."
                        the_person "Things have gotten intimate between me and my boss, but I don't want him to get me pregnant!"
                        the_person "I can't go off birth control right now. Okay?"
                    else:
                        the_person "I'm sorry, but I have personal reason for being on birth control. Please don't ask me to do that."
                elif the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.wants_creampie:
                        the_person "Do you think so? I've always wanted to, I don't think I can trust myself to tell a man to pull out."
                        the_person "Even if I know that's the smart thing to do I would probably just beg for a hot load inside me..."
                        $ play_moan_sound()
                        "She closes her eyes and moans softly, obviously lost in a fantasy of her own making."
                        "After a moment she shakes her head and focuses again."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person "Sorry... I guess if you think it's a good idea I can give it a try. What's the worst that can happen..."
                    else:
                        the_person "Do you really think so? I mean, it sounds kind of hot but I would have to trust you to pull out, or have you wear a condom."
                        mc.name "Then that's what I'll do. I just think it's so much sexier to know there's a little bit of risk."
                        "[the_person.possessive_title!c] thinks about it for a long moment. Finally she shrugs and nods."
                        the_person "Okay, we can give it a try. We'll just need to be very careful."
                    $ manage_bc(the_person, start = False)
                else:
                    "[the_person.possessive_title!c] shakes her head."
                    the_person "That would be crazy! There's no way I could gamble the rest of my life on some guy pulling out or me getting lucky."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check."
    else:
        if the_person.love > 30:
            # She loves you enough to tell you her status
            the_person "Well that's kind of private, but if it really matters to you I guess I can tell you."
            if the_person.on_birth_control:
                the_person "I'm not looking to get pregnant right now, so I'm taking birth control."
            else:
                the_person "I'm not taking any birth control right now."

            $ the_person.update_birth_control_knowledge()
            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        elif the_person.effective_sluttiness() > 20:
            the_person "Oh, I guess I can tell you if you're really curious."
            if the_person.on_birth_control:
                the_person "I'm taking birth control right now. I don't want to worry about getting pregnant by accident."
            else:
                the_person "I'm not taking birth control right now."

            $ the_person.update_birth_control_knowledge()
            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        elif the_person.is_family:
            the_person "Come on [the_person.mc_title], you can't ask me that."
        else:
            the_person "That's a pretty personal question. Let's get to know each other a little more before we talk about that, okay?"
    return
