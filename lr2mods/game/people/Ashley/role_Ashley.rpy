#Ashley's story has two primary themes.
#First, dealing with jealousy involving her sister. The base story assumes Stephanie and MC get together.
#Ashley attempts to disrupt the relationship and/or corrupt MC
#Second is her obedience story. Via Serums Ashley attempts to enslave MC's mind.
#Possible bad end if MC alienates Stephanie and Ashley?
#The first plays out in Ashleys Love and Sluttiness stories
#The second plays out in her obedience story.
#Either story could get resolved at some point, and should have implications in the other.

# ashley_room_excitement_overhear = Action("Overhear Ashley",ashley_room_excitement_overhear_requirement,"ashley_room_excitement_overhear_label")
# ashley_ask_sister_about_attitude = Action("Ask about Ashley's attitude",ashley_ask_sister_about_attitude_requirement,"ashley_ask_sister_about_attitude_label")
# ashley_room_warming_up = Action("Ashley is warming up",ashley_room_warming_up_requirement,"ashley_room_warming_up_label")
# ashley_porn_video_discover = Action("Discover Ashley's porn video",ashley_porn_video_discover_requirement,"ashley_porn_video_discover_label")

# ashley_mandatory_ask_about_porn = Action("Decide to talk to Ashley about porn",ashley_mandatory_ask_about_porn_requirement,"ashley_mandatory_ask_about_porn_label")
# ashley_stephanie_saturday_coffee_intro = Action("Good Morning Coffee", ashley_stephanie_saturday_coffee_intro_requirement, "ashley_stephanie_saturday_coffee_intro_label")
# ashley_stephanie_saturday_coffee_recur = Action("Good Morning Coffee", ashley_stephanie_saturday_coffee_recur_requirement, "ashley_stephanie_saturday_coffee_recur_label")
# ashley_clothes_shopping = Action("Ashley goes clothes shopping", ashley_clothes_shopping_requirement, "ashley_clothes_shopping_label")
# ashley_second_concert_date = Action("Ashley gets a second date", ashley_second_concert_date_requirement, "ashley_second_concert_date_label")
# ashley_steph_second_date_confrontation = Action("Stephanie confronts you", ashley_steph_second_date_confrontation_requirement, "ashley_steph_second_date_confrontation_label")
# ashley_sneaks_over = Action("Ashley sneaks over", ashley_sneaks_over_requirement, "ashley_sneaks_over_label")
# ashley_steph_drinks_out = Action("Ashley and Stephanie date", ashley_steph_drinks_out_requirement, "ashley_steph_drinks_out_label")


label jumpstart_ashley():
    $ ashley._sluttiness = 20
    $ ashley._obedience = 110
    $ ashley.love = 20
    call ashley_intro_label() from _ashley_jumpstart_function
    return

#Ashley base line intro story.

# def ashley_room_excitement_overhear_requirement(the_person):
#     if the_person.is_at_work:
#         if the_person.current_job.days_employed > 5: #Been working for at least a few days week.
#             return True
#     return False
#
# def ashley_ask_sister_about_attitude_requirement(the_person):
#     if ashley_get_if_excitement_overheard():
#         if the_person.is_at_work:
#             return True
#     return False
#
# def ashley_room_warming_up_requirement(the_person):
#     if the_person.is_at_work:
#         if the_person.current_job.days_employed > 12: #Been working for at least a week.
#             return True
#     return False
#
# def ashley_porn_video_discover_requirement():
#     return False    #Disabled while working on her story.
#     if time_of_day == 4 and ashley.sluttiness > 20 and mc.energy > 80:
#         return ashley_get_attitude_discussed()
#     return False
#
# def ashley_mandatory_ask_about_porn_requirement():
#     if time_of_day > 1 and ashley.sluttiness >= 20 and ashley.love >= 40 and stephanie.love >= 60:
#         return day > ashley_get_porn_convo_day() and ashley_get_concert_date_stage() >= 2
#     return False
#
# def ashley_stephanie_saturday_coffee_intro_requirement(the_person):
#     return the_person.is_at(stephanie.location) and day%7 == 6 and time_of_day == 0
#
# def ashley_stephanie_saturday_coffee_recur_requirement(the_person):
#     return the_person.is_at(stephanie.location) and day%7 == 6 and time_of_day == 0
#
# def ashley_second_concert_date_requirement():
#     return time_of_day == 3
#
# def ashley_steph_second_date_confrontation_requirement():
#     return time_of_day == 2 and mc.is_at_office and ashley.sluttiness >= 60
#
#
# def ashley_clothes_shopping_requirement(the_person):
#     return the_person.is_at(clothing_store)
#




#Intro Labels
label ashley_intro_label():
    if ashley.is_employee:    #We already hired her somehow.
        return
    $ the_person = stephanie
    "You are deep in your work when a voice startles you from your concentration."
    the_person "Hey [the_person.mc_title]. Sorry to bug you, do you have a minute?"
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    mc.name "Of course. What can I do for you?"
    the_person "Well, I kind of need a favour."
    mc.name "Well, you've taken an awfully large risk coming to work for me here, so I suppose I owe you one."
    the_person "You see, it's my sister. She just graduated from college and moved in with me, but is having trouble finding work in her degree. She's had to move in with me because she can't find work!"
    the_person "She's really smart, but kind of wild. It has been hard for her to get through interviews."
    mc.name "What is her degree in?"
    the_person "She actually just finished her nursing certification and pre-med degree, but is taking a year off before returning to school."
    mc.name "She's a nurse and... she can't find work?"
    the_person "Errr, well she had a little incident at the hospital with an HR issue..."
    the_person "Look, I know that this won't be her final job, but having something to help fill in the gaps would be huge for her."
    the_person "I brought her resume, will you at least take a look at it? I think she would be great over in production."
    the_person "And it would be a huge favour for me!"
    menu:
        "Take a look":
            pass
        "Not right now":
            mc.name "I'm sorry, I'm not hiring anyone like that right now. But if I change my mind I'll come find you, okay?"
            the_person "Of course, that's all I can ask, is that you will keep her in mind. Thanks!"
            $ add_ashley_hire_later_action()
            return
        "Blow me and I'll look" if the_person.is_willing(blowjob):
            mc.name "I tell you what, why don't you come suck me off while I look over her documents."
            the_person "Oh! A favour for a favour then? Okay!"
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "[the_person.possessive_title!c] gets on her knees and starts to undo your pants."
            $ mc.change_locked_clarity(20)
            the_person "You know I would do this anyway, right?"
            mc.name "Of course, but being reminded of your blowjob skills will probably help me make up my mind if I want to hire someone you're related to."
            call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_sex_description_ashley_intro_bonus_BJ_1
            $ the_report = _return
            $ scene_manager.update_actor(the_person, position = "stand4")
            if the_report.get("guy orgasms", 0) > 0:
                mc.name "God your mouth is amazing. If your sister sucks anything like you, this will be a no-brainer..."
                the_person "Hah! Well, to be honest, I don't think she really cares for giving blowjobs, but I guess you never know."
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for her would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_1
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_stats(happiness = 5, obedience = 5)
        the_person "Oh! I didn't think you would say yes. This is great news! I'm sure she'll probably want to get started right away!"

        $ set_ashley_hired()

        "You complete the necessary paperwork and hire [ashley.fname], assigning her to the production department."
        "As you finish up, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as she leaves the room. You hope you made the right decision!"
        $ add_ashley_first_talk_action()
    else:
        "After looking at her profile, she doesn't seem like a good fit."
        "WARNING: selecting 'Never hire her' will remove [ashley.fname] from the game."
        menu:
            "Hire her later":
                pass
            "Never hire her":
                mc.name "I'm sorry, but she doesn't seem like a good fit."
                mc.name "I'm not going to hire her. Is that going to be a problem?"
                "[the_person.possessive_title!c] seems surprised."
                the_person "What?.. Wow... No... No sir, no problem..."
                $ the_person.change_stats(happiness = -10, love = -5, obedience = -5)
                "She is clearly disappointed, but drops the issue."
                $ add_production_assistant_alt_intro_action()
                $ ashley.remove_person_from_game()  #Oh boy, I bet this never causes any issues down the line
                return
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person "Ahhh, okay. I understand, but please let me know ASAP if you change your mind!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title!c] gets up and leaves the room. Did you make the right decision? Oh well, if you change your mind, you can always talk to her again."
        $ add_ashley_hire_later_action()
    return

label ashley_hire_directed_label():
    $ the_person = stephanie
    mc.name "I wanted to talk to you again about your sister."
    the_person "Oh? Have you decided to reconsider?"
    mc.name "I have. Do you still have her documents that I could look over again?"
    the_person "Of course! Let me get them."
    "[the_person.possessive_title!c] runs over to her desk and comes back with a folder."
    the_person "Here you go!"
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for her would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_2
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_stats(happiness = 5, obedience = 5)
        the_person "Oh! This is great news! I'm sure she'll probably want to get started right away!"

        $ remove_ashley_hire_later_action()
        $ set_ashley_hired()

        "You complete the necessary paperwork and hire [ashley.fname], assigning her to the production department."
        "As you finish up and start to leave, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ the_person.draw_person(position = "walking_away")
        the_person "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as you leave the room. You hope you made the right decision!"
        $ add_ashley_first_talk_action()
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person "Wow, really? Why did you even talk to me about this?"
        $ the_person.change_stats(happiness = -10, love = -5, obedience = -5)
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title!c] gets up and leaves the room. You should probably avoid getting her hopes up again like this."

    return

label ashley_first_talk_label(the_person):
    $ the_person.draw_person()
    $ add_production_assistant_alt_intro_action()   #Throw this in here just in case we fire Ashley
    mc.name "Hello there. You must be [the_person.fname]. I'm [mc.name], the one who owns this place."
    "She looks at you and smiles."
    the_person "Hello! So you're the guy my sister won't stop going on and on about. Nice to meet you."
    mc.name "Ah, yes I suppose that would be me."
    the_person "Thank you for the opportunity. I appreciate the work, especially in a pharma related field, it will really help my job prospects in the future."
    mc.name "Of course, [stephanie.fname] is a good friend. Do you go by [the_person.fname]? Or something else?"
    the_person "[the_person.title] is fine..."
    mc.name "[the_person.title] it is then."
    mc.name "We would only need to discuss your duties here."
    call set_duties_controller(the_person, the_person.primary_job) from _call_set_duties_controller_ashley_first_talk
    if _return:
        $ the_person.set_event_day("work_duties_last_set")
        mc.name "I trust you can handle all of that?"
        "[the_person.possessive_title!c] nods."
        the_person "Yes [the_person.mc_title], I can."
    else:
        mc.name "I'll need to make some other decisions first. We'll talk about this soon, okay?"
        "[the_person.possessive_title!c] nods."
    mc.name "Perfect, welcome to the team [the_person.title]."
    the_person "Thank you, [the_person.mc_title]."

    $ add_ashley_room_overhear_classical_action()
    return

label mc_serum_intro_label(the_person):
    $ the_person.draw_person()
    "You step into the production lab. As you are walking in, [the_person.possessive_title] is just walking out."
    the_person "Oh hey [the_person.mc_title], great timing. I was just getting coffee... do you want some?"
    mc.name "Oh, sure I could do that."
    the_person "How do you like it?"
    mc.name "Just black is fine."
    the_person "Alright."
    $ clear_scene()
    "She disappears out the door, headed toward the break room. You walk around the production room for a minute, checking up on the serum processing."
    "After you make a round, [the_person.title] reappears with two cups of coffee."
    $ the_person.draw_person()
    the_person "Here we go! Hey, have a few minutes? I wanted to talk to you about something."
    mc.name "Sure."
    $ the_person.draw_person(position = "sitting")
    "You sit down at [the_person.possessive_title]'s desk across from her and start to chat."
    "She talks with you for a while about how she is settling in and how much she appreciates you hiring her."
    "You drink your coffee fairly quickly. It is a nice to take a break from work and you feel re-energized."
    $ mc.change_energy(50)
    $ mc_serum_energy_regen.apply_trait()
    $ mc_serum_energy_regen.is_selected = True
    "As you finish up with your coffee, she changes the subject."
    the_person "So I was talking with my sister about how things are going here at work."
    the_person "She was just gushing all about how you built her a special room just for her science work."
    the_person "And of course, as we were talking, I had to ask her the obvious question..."
    the_person "These serums we keep making... they are designed entirely to be used by, and tested on, women."
    the_person "Why not work on similar designs to be used on men?"
    mc.name "Ah, well, there are a number of reasons..."
    the_person "Yeah, yeah I'm sure there are... But I asked her, why don't you ever test any of these serums?"
    the_person "I mean, some of these have some amazing effects..."
    mc.name "Well, I'm the owner of the business, and the business itself is built on marketing the serums to a specific demographic..."
    "[the_person.title] rolls her eyes."
    the_person "Yeah, she gave me a similar excuse. But why not? If we made something here that would be beneficial for you, specifically, why not try it?"
    mc.name "I guess I would certainly consider it, but I wouldn't want that to be the main focus for the employees here."
    the_person "Let me put it this way. If I made a serum, with help from the research department, for you, would you try it?"
    mc.name "I mean, I would need some assurances that some basic safeguards are in place..."
    the_person "Like the safeguards you put in place for the employees you are testing serums on?"
    mc.name "Look. I understand you have some concerns about the way things are done here, but..."
    the_person "So that's a no?"
    mc.name "No."
    "[the_person.possessive_title!c] shakes her head."
    the_person "That's too bad. I figured you would say that. But fortunately, science stops for no man."
    mc.name "I'm not going to take one..."
    the_person "That's okay! You already have!"
    "... You look down at your empty coffee with a sudden realisation. Holy shit, this bitch just used your own tactic against you?"
    the_person "Hey! Don't look at me like that! The coffee has you feeling good, doesn't it? Almost... re-energized?"
    mc.name "I... actually yeah, I do feel like I have more energy."
    "[the_person.title] smiles wide."
    the_person "There, see? All I did was adapt the caffeine infusion trait for your much more manly body."
    the_person "That burst of energy you got from the coffee? I think it should actually last a few days."
    "You are still a bit shocked by the revelation that [the_person.possessive_title] dosed you without your knowledge..."
    mc.name "Okay... we'll see how this one goes, okay?"
    mc.name "But I don't want you to spend all your work time on it, this is just a side project."
    the_person "Yes! Don't worry, this is gonna be great."
    "Yeah. Great... Great for who though?"
    mc.name "Alright. Get back to work, I'm going to do the same."
    the_person "You got it boss!"
    $ clear_scene()
    $ add_mc_serum_timeout_action()
    "You get up and step out of the serum production area."
    "You definitely feel conflicted about what just happened... but you have to admit, the prospect of getting your hands on serums that would enhance your personal performance is tempting."
    "You decide to go along with it for now, but you definitely need to keep a closer eye on [the_person.possessive_title] and her activities."
    return

label mc_serum_timeout_label():
    $ mc_serum_energy_regen.remove_trait()
    $ mc_serum_energy_regen.is_selected = False
    "Something about you feels different. You have... less energy?"
    "The serum that [ashley.possessive_title] gave you must have worn off."
    "Maybe you should talk to her about getting another dose? It definitely had a positive effect on you."
    "You feel like this is a direction worth pursuing. You decide to talk to her about taking it regularly."
    $ add_mc_serum_review_intro_action()
    return

label mc_serum_review_intro_label(the_person):
    $ remove_production_assistant_alt_intro_action()    #Clean this up. Not needed since we unlock the policy here
    "You approach [the_person.title] about the energy serum she gave you."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. Can I have one moment?"
    the_person "Oh hey, [the_person.mc_title]. Sure."
    mc.name "I wanted to let you know, I think that serum you gave me the other day was successful. I definitely felt more energy after."
    mc.name "I am curious... is this something that I could take regularly? I would like to have the option at least."
    the_person "That's great! Yeah I've been thinking about that too."
    the_person "In the medical world, we use a medication's half life to determine dosing requirements."
    the_person "It seems like a small, daily dose of these serums might be ideal in order to keep a consistent effect."
    mc.name "That makes sense."
    the_person "If you like, I could prepare your daily dose and leave it with your things in your office each day before I leave."
    the_person "I'll make a couple extra for the weekend on Fridays too. Then you can take one each morning when you wake up for consistent results."
    mc.name "Alright, that sounds like a good plan. I may not use them all the time, but it makes sense to do it that way."
    $ purchase_policy(production_assistant_creation_policy, ignore_cost = True)
    $ mc.business.hire_production_assistant(the_person)
    "You have officially made [the_person.title] your production assistant. The relevant Policy has automatically unlocked."
    the_person "I have ideas for other beneficial serum effects we could try also! We should start small, but if I come up with anything I'll let you know."
    "[the_person.possessive_title!c] seems eager to use you as a guinea pig..."
    the_person "Here is what I have so far... take a look, and I can have something ready for you at the end of the day if you want."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.title] turns and pulls up some serum info at her computer terminal."
    the_person "Here we go."
    call screen mc_personal_serum_screen()
    $ the_person.draw_person()
    the_person "Alright. Just let me know if you want to discuss something serum related, or change what you are taking."
    mc.name "Sounds good."
    $ add_prod_assistant_essential_oils_intro_action()
    $ add_prod_assistant_performance_upgrade_action()
    #Add events for Ashley's three story lines (the all reference the unlocked mc serums)
    $ add_ashley_afterhours_action()
    $ add_ashley_demands_relief_action()
    # $ add_ashley_submission_titfuck_action()
    $ ashley_story_path_submission.start_path(ashley)

    "You step away from [the_person.possessive_title]. You can now talk to her at work about serums for personal use."
    "She will leave them in your office for you each work day. If she needs your attention on something, she may hang around and wait for you to pick them up."
    return

label ashley_room_overhear_classical_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person "I know, the city symphony is performing a collection of Johannes Brahms' symphonies. I want to go so bad, but I can't find anyone to go with..."
    "As you enter the room, she looks up and stops talking."
    $ the_person.draw_person()
    the_person "Oh, hey [the_person.mc_title]. Having a good day?"
    "[the_person.title] has been stepping into a role on her own as your production assistant. You feel like you are really starting to warm up to her."
    mc.name "It's been great so far. And you?"
    the_person "Oh, I've been good. Thanks for asking."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ ashley.event_triggers_dict["concert_overheard"] = True
    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahms symphony recital, but you don't have anyone to go with?"
    the_person "Ummm yeah, something like that..."
    mc.name "That sounds like a great cultural event. I was wondering if you would be willing to let me take you?"
    "She is caught off guard. She wasn't expecting you to ask something like this!"
    the_person "Oh! I uhh, I'm not sure if Steph would be okay with that..."
    mc.name "Why wouldn't she be okay with it?"
    the_person "I... well..."
    "She mutters something unintelligible."
    the_person "I guess there's no reason, really."
    mc.name "Well, I would really like to take you, if you want to go."
    the_person "I suppose."
    mc.name "Ah, great! Do you know when the concert is?"
    if day % 7 == 3:
        the_person "It's actually tonight."
        mc.name "Ok. I'll make the arrangements and meet you there on tonight then?"
    else:
        the_person "It's on Thursday night."
        mc.name "Ok. I'll plan to meet you there on Thursday night then?"
    the_person "Okay, if you're sure about this..."
    "You feel good about this as you finish up your conversation."
    $ add_ashley_classical_concert_date_action()
    return

label ashley_classical_concert_date_label():
    $ mc.stats.change_tracked_stat("Girl", "Dates", 1)
    $ the_person = ashley
    "It's Thursday. You have a date planned with [the_person.title]. It's taken a while for her to warm up to you, so you don't even consider cancelling."
    "You head downtown. The plan is just to meet up at the concert hall itself. [stephanie.title] is going to drop her sister off and pick her up afterwards."
    $ mc.change_location(downtown)
    "Soon, you see the sisters."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, the_person.decide_on_outfit(sluttiness_modifier = 0.2), position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(stephanie, stephanie.decide_on_outfit(), display_transform = character_center_flipped)
    stephanie "Oh hey, there's [stephanie.mc_title]. Don't worry, I'm sure everything will be great."
    the_person "I know, I know... are you sure you don't want to go?"
    stephanie "Don't be silly, you've only got two tickets. You two will have a blast!"
    the_person "Okay..."
    "As you look at the two sisters, you have a sudden vision in your head of the two girls on top of each other, eating each other out, while you fuck [the_person.title]."
    "Right now a goal like that seems impossibly far away... but maybe someday you'll be able to get the two sisters to bend to your sexual desires."
    $ mc.change_locked_clarity(30)
    "You take a deep breath, then walk over and greet the pair."
    menu:
        "Cheerful greeting\n{menu_red}Increases love{/menu_red}":
            mc.name "Hello! Thanks for this, I've been looking forward to this ever since we arranged it. [the_person.title], you look great tonight!"
            the_person "Ah... thank you."
            $ the_person.change_stats(happiness = 2, love = 1)
            "[stephanie.title] gives you a smile after your kind words to her sister."
            $ stephanie.change_stats(obedience = 1, love = 1)

        "Sexual greeting\n{menu_red}Increases sluttiness{/menu_red}":
            mc.name "Wow. What a couple of hotties. You could hang on my other arm [stephanie.title]."
            "[stephanie.possessive_title!c] rolls her eyes."
            stephanie "Yeah right. Like you could handle both of us."
            mc.name "Is that a challenge?"
            stephanie "Not this time."
            "You glance at [the_person.title]. She is blushing a bit, but you notice a slight smile."
            $ the_person.change_stats(happiness = 1, slut = 1, max_slut = 50)
            $ stephanie.change_stats(obedience = 1, slut = 1, max_slut = 50)

        "Commanding greeting\n{menu_red}Increases obedience{/menu_red}":
            mc.name "Yeah, don't be silly. [stephanie.title] doesn't need to hear us talk about her anyway."
            the_person "Ha! I suppose I could share some secrets of hers."
            stephanie "Wow, gossiping is starting already, is it?"
            $ the_person.change_stats(happiness = 1, obedience = 1)
            $ stephanie.change_stats(obedience = 1, love = -1)
            "[stephanie.possessive_title!c] frowns, but otherwise doesn't protest."

    #End of love option
    stephanie "Alright you two, go enjoy your classical concert. Ash, just text me when you get done, I'm gonna go have a couple drinks."
    the_person "Okay. Bye [stephanie.fname]!"
    $ scene_manager.hide_actor(stephanie)
    mc.name "Shall we?"
    $ show_concert_hall_background()
    "You step into the concert hall, show your tickets, and make your way to your seats."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You have a few minutes before the concert starts, so you try making some small talk."
    mc.name "So, have you ever been to a concert like this before?"
    the_person "Oh, a few times, when I was in college, but not for over a year."
    mc.name "I'll admit it, this is my first time going to something like this. I'm really excited to have the chance to try something new, though."
    the_person "Oh yeah? I think most guys find classical music a bit boring..."
    mc.name "I'll admit I'm not an avid follower, but I think experiencing a variety of cultural events is an important thing for someone to do."
    the_person "Yeah, that's very insightful."
    mc.name "Plus, I'm glad to be able to spend some time with you and get to know you better."
    "You notice her blush a bit, but you can also see her smile."
    $ the_person.change_stats(love = 2, happiness = 2)
    #end branch
    $ show_concert_hall_background(True, True)    # dim lights
    "Soon, the lights dim, and the music begins, starting with a splendid piano melody."
    "You and [the_person.possessive_title] sit together silently, enjoying the music."
    "It goes through emotional highs and lows. At one point, you look over and you think you see a tear on [the_person.title]'s cheek."
    menu:
        "Hold her hand\n{menu_red}Increases love{/menu_red}":
            "You reach down and take her hand. She jumps at the contact, but quickly takes your hand in hers as the music reaches an especially poignant moment."
            $ mc.change_locked_clarity(5)
            $ the_person.change_stats(love = 5, happiness = 5)
            "You hold hands for the duration of the concert. You both share comments now and then about specific parts that you liked."
        "Put your hand on her leg\n{menu_red}Increases sluttiness{/menu_red}":
            "You reach down and put your hand on her thigh, just above her knee. She jumps at the contact, but puts her hand on top of yours."
            $ mc.change_locked_clarity(15)
            $ the_person.change_stats(slut = 2, happiness = 5)
            "You leave your hand on her leg for the duration of the concert."
        "Put your arm around her\n{menu_red}Increases obedience{/menu_red}":
            "You reach your arm around her and put your hand on her shoulder. You pull her closer to you."
            "At first she is a little reluctant, but after a tug, she leans towards you and puts her head on your shoulder."
            $ mc.change_locked_clarity(15)
            $ the_person.change_stats(obedience = 2, happiness = 5)
            "You watch the remainder of the concert in silence with her head against you."
    $ show_concert_hall_background(False, True)
    "When the concert is over, the lights slowly come back on. You let go of her as you both start to get up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "You slowly file out of the concert hall, chatting about the concert."
    $ mc.change_location(downtown)
    "When you get outside, [the_person.title] looks around."
    the_person "Oh! I was supposed to text Steph. I was having fun and totally forgot!"
    "She pulls out her phone and texts her sister."
    the_person "Okay, she says she'll be right over... You don't have to stay, I'm sure she won't be long."
    mc.name "And leave a pretty girl like you all by herself? Not a chance."
    $ the_person.change_stats(love = 2, happiness = 2)
    "She smiles, looking down at her feet."
    mc.name "So was it everything you hoped it would be?"
    "She thinks about it before responding. One of the things you appreciate about [the_person.title] is that she always thinks before she speaks."
    the_person "It was, and more. I really had a good time tonight."
    mc.name "Great! If you hear about another orchestra in town, I'd love to go again."
    the_person "I haven't heard anything, but I'll definitely keep it in mind. I'd like to do this again."
    $ scene_manager.show_actor(stephanie)
    stephanie "Hey Ash! Hey [stephanie.mc_title]! How'd it go?"
    the_person "Steph! We had a great time. The performers were amazing..."
    stephanie "And I assume you were a perfect gentleman?"
    "[stephanie.possessive_title!c] gives you a look. She smiles, but you can tell she is genuinely protective of [the_person.fname]."
    mc.name "As always, [stephanie.fname]."
    the_person "He really was. Thanks again [the_person.mc_title]!"
    "It's late, so you all agree to part ways."
    mc.name "Alright, don't forget work tomorrow. I'll see you both then."
    the_person "Bye!"
    stephanie "See ya then!"
    $ scene_manager.clear_scene()
    $ ashley.event_triggers_dict["concert_date"] = 2
    $ add_ashley_porn_video_discover_action()
    $ ashley.progress.love_step = 1
    return

#
# #Bonus scenes.
# init -1 python:
#     def ashley_repeatable_after_hours_requirement(the_person):
#         return False
#
#     def ashley_asks_for_second_date_requirement():
#         if not (mc.is_at_office and mc.business.is_open_for_business):
#             return False
#
#         if ashley_lily_are_friends() and ashley_dom_oral_avail():
#             if ashley.days_since_event("story_event") >= TIER_1_TIME_DELAY:
#                 return True
#         return False
#
#     def ashley_second_concert_date_requirement():
#         if time_of_day == 3 and day%7 == 4:  #Friday
#             return True
#         return False
#
#     def ashley_steph_second_date_confrontation_requirement():
#         if time_of_day == 1:
#             return True
#         return False
#
#     def ashley_sneaks_over_requirement():
#         if ashley.love > 60 and ashley.sluttiness > 60:
#             if time_of_day == 4 and ashley.days_since_event("story_event") >= TIER_1_TIME_DELAY:
#                 return True
#         return False
#
#     def ashley_steph_drinks_out_requirement():
#         return False
#
#
# init 1 python:
#     ashley_repeatable_after_hours = Action("Ashley needs relief crisis", ashley_repeatable_after_hours_requirement, "ashley_repeatable_after_hours_label")
#     ashley_asks_for_second_date = Action("Ashley asks for a second concert date", ashley_asks_for_second_date_requirement, "ashley_asks_for_second_date_label")
#     ashley_second_concert_date = Action("Ashley's second concert date", ashley_second_concert_date_requirement, "ashley_second_concert_date_label")
#     ashley_steph_second_date_confrontation = Action("Stephanie breaks up with you", ashley_steph_second_date_confrontation_requirement, "ashley_steph_second_date_confrontation_label")
#     ashley_sneaks_over = Action("Ashley spends the night", ashley_sneaks_over_requirement, "ashley_sneaks_over_label")
#     ashley_steph_drinks_out = Action("Ashley and Steph bar date", ashley_steph_drinks_out_requirement, "ashley_steph_drinks_out_label")
#
# label ashley_repeatable_after_hours_label():
#     $ the_person = ashley
#     if not ashley.is_employee:
#         return
#     # stage 1, set the scene. You walk in on Ashley at the end of the day in your office.
#
#
#     #stage 2, determine if Ashley is controlling or MC
#     $ dom_attempt = False
#     if ashley_dom_finger_avail():
#         if ashley_dom_fuck_avail():
#             the_person "Hey, sit in your chair and put your handcuffs on. I have needs and I know just how I want them met."
#         elif ashley_dom_oral_avail():
#             the_person "Hey, I could really use a good orgasm right now. I want to sit on your desk while you go down on me again."
#         else:   #She has taken control at least once.
#             the_person "Hey, while we're here... alone..."
#             the_person "I could really use a good orgasm. Could you use your fingers and get me off again?"
#         call ashley_obedience_struggle() from _ashley_crisis_obedience_check_01
#         $ dom_attempt = _return
#     else:
#         the_person "Well, I think I'll get going now..."
#     if dom_attempt: #She is successful and has her way with MC
#         "In this section, we replay a scene where Ashley has her way with MC."
#         "These scenes still need to be written."
#         $ ashley.change_obedience(-2)
#     else:
#         #Next, determine if MC wants to try and take charge.
#         if the_person.event_triggers_dict.get("sub_titfuck_count", 0) >= 1 and not ashley_sub_titfuck_avail() and ashley.obedience > 120:
#             mc.name "I have a better idea."
#             "You've been working on getting her to obediently service you with her tits lately, and you feel like you've pushed her obedience far enough to try again."
#             call ashley_submission_titfuck_label() from _ashley_random_crisis_sub_titfuck_scene_01
#             return
#         "You think about it for a moment. Maybe you should try and take charge? Maybe you should order HER to do something!"
#         menu:
#             "Demand tit fuck" if ashley_sub_titfuck_avail():
#                 "Sorry, I haven't written this yet!"
#                 pass
#             "Demand blowjob" if ashley_sub_oral_avail():
#                 "Sorry, I haven't written this yet!"
#                 pass
#             "Demand bare sex" if ashley_sub_fuck_avail():
#                 "Sorry, I haven't written this yet!"
#                 pass
#             "Demand anal sex" if ashley_sub_anal_avail():
#                 "Sorry, I haven't written this yet!"
#                 pass
#             "Demand tit fuck\n{menu_red}Not obedient enough{/menu_red} (disabled)" if ashley_sub_titfuck_avail():
#                 pass
#             "Demand blowjob\n{menu_red}Not obedient enough{/menu_red} (disabled)" if ashley_sub_oral_avail():
#                 pass
#             "Demand bare sex\n{menu_red}Not obedient enough{/menu_red} (disabled)" if ashley_sub_fuck_avail():
#                 pass
#             "Demand anal sex\n{menu_red}Not obedient enough{/menu_red} (disabled)" if ashley_sub_anal_avail():
#                 pass
#             "Just mess around":
#                 pass
#             "Just say goodnight.":
#                 mc.name "Goodnight [the_person.title]."
#                 the_person "Goodnight then."
#                 "You leave your office."
#                 return
#
#     return
#
# label ashley_asks_for_second_date_label():  #requires 40 love and 60 mc obedience scenes complete.
#     "In this label, Ashley interrupts a conversation MC is having with Steph."
#     "Asks Steph if she can steal you for a second concert date. Steph has reservations but relents."
#     "Sets up the second concert date."
#     $ mc.business.add_mandatory_crisis(ashley_second_concert_date)
#     return
#
# label ashley_second_concert_date_label():
#     $ the_person = ashley
#     $ arousal_gain = builtins.round((100 - the_person.arousal) / 4)
#     $ date_outcome = None
#     $ cum_clue = False
#     $ caught_ashley_cheating = False
#     $ the_person.planned_outfit = the_person.wardrobe.get_outfit_with_name("Ashley Night Out Outfit") or the_person.get_random_appropriate_outfit(guarantee_output = True)
#     $ the_person.apply_outfit(the_person.planned_outfit)
#     $ the_person.event_triggers_dict["second_date_complete"] = True
#     $ ashley.set_event_day("story_event")
#     "Evening falls and soon it is time to make your way downtown to meet [the_person.title], your girlfriend's sister, for a date to another classical music concert."
#     "Things with the two girls have gotten complicated. [ashley.fname] has been able to keep things between you a secret from her sister, but is getting more and more demanding and needy."
#     "Lately it seems like [stephanie.title] is getting a little suspicious, and [the_person.possessive_title]'s demand to share you for a date is certain to have her unsettled."
#     $ mc.change_location(downtown)
#     "When you arrive, you look around for a minute, but don't see [ashley.fname] yet at your agreed on meeting place. You decide to give her a few minutes. You are just about to pull out your phone and text her when you see her approaching."
#     "She is wearing a sexy black dress, and your eyes are immediately drawn to its curves. There's not a doubt in your mind that [the_person.title] has something planned for you this evening..."
#     $ mc.change_locked_clarity(20)
#     $ the_person.draw_person()
#     ashley "Hey! My eyes are up here."
#     mc.name "Yeah but I wasn't looking at your eyes."
#     "When you finally lift your eyes from her body and meet hers, she has a mischievous smile."
#     ashley "Good. God I finally get you all to myself for one evening."
#     mc.name "Are we still going to the concert?"
#     ashley "Of course! I wasn't lying, and I'll be damned if I miss the opportunity to see the Los Angeles Philharmonic. Tickets weren't cheap you know! And my cheapskate boss barely pays me enough to cover the cost of living."
#     "Wow, she is pretty sassy this evening. You tease each other a bit more but make your way into the concert."
#     $ show_concert_hall_background()
#     "As you take your seats, you try and fit in one last remark."
#     mc.name "I would think as an intern, YOU should be the one on your knees under the desk servicing the boss during the workday, not the other way around."
#     "A couple people near you give you a questioning look, but seem relieved when [the_person.title] starts to laugh."
#     $ the_person.draw_person(position = "sitting")
#     ashley "Thanks, I'll try to remember that for my next performance review."
#     "You sit down beside [the_person.possessive_title]. You are a bit surprised when she takes your hand and holds it."
#     "Even though things between you are supposed to be just physical, you have to wonder... Is she catching feelings for you? Normally, a situation with two sisters and one man could only possibly end in disaster."
#     "But with the serums... Maybe you could eventually convince the two girls that they can both get what they want? You decide to plant that seed now, and see how she reacts."
#     mc.name "You know what? I can't wait."
#     ashley "Oh? What for?"
#     mc.name "When we can go do stuff like this more often, then go back to your place after, and me, you, and [stephanie.fname] all hop in bed together and screw until the sun comes up."
#     ashley "Ha! Oh wow. You've been watching some good porn lately huh? I don't think Steph is really the sharing type... I'm usually not either..."
#     mc.name "And yet, here you are, with your sister's boyfriend. Maybe you just haven't met someone worth sharing before?"
#     "[the_person.title] is quiet. Right on cue, the lights turn down and the music begins."
#     $ show_concert_hall_background(darken = True)
#     "The music begins, playing through some classical music that you aren't familiar with, but it is quite enjoyable. When you look over at [the_person.possessive_title] she seems to be really enjoying herself."
#     "After a while, as the music goes through a crescendo, you feel her squeeze your hand, then turn it over, so her palm is against the back of your hand."
#     "She puts your hand on her leg, then slowly starts to push it up, under her dress..."
#     $ mc.change_locked_clarity(15)
#     $ the_person.change_arousal(arousal_gain)
#     "You are delighted but not surprised to discover she isn't wearing any panties. She lets go of your hand and takes a quick peek around."
#     "With the darkness in the room, no one notices your hand under her dress as you slowly start to push a finger inside her cunt."
#     "[the_person.title]'s body responds rapidly to your touch. After barely a minute her pussy is soaked, and you can see her chest rising and falling faster out of the corner of your eye."
#     "The angle is rough, but you do your best to rub the palm of your hand against her clit as you finger her."
#     "Her hips are beginning to wiggle gently in her seat as she squirms at your touch. You feel like she has to be close to cumming."
#     $ the_person.change_arousal(arousal_gain)
#     "What happens next surprises even you. She grabs your hand and stops you. You can't help but look at her questioningly. She leans over and whispers to you."
#     ashley "Go slow. It'll be more fun if you take your time..."
#     "She takes your hand and brings it back to her cunt, but this time she lifts her hips slightly and sits on it. She slowly grinds herself down on your hand."
#     $ mc.change_locked_clarity(20)
#     $ the_person.change_arousal(arousal_gain)
#     "She is using your hand to edge herself?"
#     "As the music continues, [the_person.possessive_title] keeps stimulating herself with your hand. Sometimes she goes completely still, letting herself calm down."
#     "Other times she lets you push your fingers back inside her for a minute or two, and other times just grinding against it. However, she never lets herself cum; each time she gets close, she stops. Your cock is getting uncomfortably hard."
#     "The music seems to be winding down. Is she going to let herself finish?"
#     mc.name "You umm..."
#     ashley "Of course. But not here. I decided earlier when I cum I want your face between my legs, not your hand..."
#     $ mc.change_locked_clarity(30)
#     "You slowly pull your hand away from her crotch. It's been wet with her arousal for so long it's starting to get a little wrinkled. She opens her clutch and starts to pull out a handkerchief, but you have another idea."
#     "You bring it to your mouth and taste it. Her flavour is musky but sweet. You can't wait to taste the source."
#     "[the_person.title] just watches as you clean your fingers."
#     $ show_concert_hall_background()
#     "The lights come back on and people start to get up. You can see [ashley.title]'s chest rising and falling rapidly. She is breathing heavily and is really turned on."
#     $ the_person.draw_person()
#     mc.name "Well, I promised to get you home straight away."
#     "You give her a wink as you say it. She chuckles and winks back."
#     $ mc.change_location(downtown)
#     "You step outside and start to walk her home. However, as you pass an empty alleyway, you feel her hand tug at yours as she drags you back into the alley."
#     "You both take a quick look around. Certain that you are alone, you push her up against the wall."
#     $ the_person.draw_person(position = "kissing")
#     "[the_person.possessive_title!c] moans as you kiss her neck. You feel her hands on your shoulders, pushing you down on your knees."
#     "You go with it. You're sure that after all that edging, she is probably close to cumming anyway."
#     $ the_person.draw_person(position = "against_wall")
#     "[the_person.title] props her leg up on a box, giving you easy access to her cunt. As you start to lick along the inside of her thighs, she runs her hands through your hair."
#     the_person "Mmm, do a good job and I'll repay the favour..."
#     "If you do good, she'll probably repay you. But you should be careful, you still have to go see [stephanie.possessive_title] later! If you make it too obvious, she'll probably know something is up..."
#     call fuck_person(the_person, start_position = standing_cunnilingus, skip_intro = True, position_locked = True, private = True) from _call_sex_description_ashley_second_date_cunnilingus_01
#     $ the_report = _return
#     #TODO make sure MC arousal stays the same?
#     if the_report.get("girl orgasms", 0) == 0:
#         $ the_person.draw_person()
#         "[the_person.title] puts her leg down. She is incredulous."
#         the_person "Seriously? [stephanie.fname] really has you wrapped around her finger, doesn't she? I don't know why I bother with you..."
#         $ the_person.change_stats(happiness = -10, obedience = -5)
#         "She seems pretty pissed you couldn't even get her off."
#     elif the_report.get("girl orgasms", 0) == 1:
#         $ the_person.draw_person()
#         "[the_person.title] puts her leg down. She gives you a little smile."
#         the_person "Mmm... not bad... but honestly, I was expecting more."
#         menu:
#             "Lean in for a kiss":
#                 "When you stand up, you lean in for a kiss, but she pushes against you to keep her distance."
#                 the_person "Easy now, remember where that tongue just was?"
#                 the_person "Look, I'll give you a handy... an orgasm for an orgasm, okay?"
#                 "[the_person.possessive_title!c] reaches down and undoes your fly. You look down and see her pulling your dick out."
#                 $ mc.change_locked_clarity(20)
#                 "She looks into your eyes as she starts to give you a handjob."
#                 the_person "Alright, don't hold back now."
#                 $ date_outcome = "handjob"
#                 call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_ashley_handjob_second_date_01
#                 $ the_report = _return
#                 if the_report.get("guy orgasms", 0) > 0:
#                     if the_person.has_face_cum:
#                         if the_person.outfit.has_dress:
#                             "[the_person.possessive_title!c]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
#                         else:
#                             "[the_person.possessive_title!c]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
#                     elif the_person.has_mouth_cum:
#                         "[the_person.possessive_title!c] has a bit of cum on her chin, but is able to quickly clean it up."
#                     elif the_person.has_tits_cum:
#                         if the_person.outfit.has_dress:
#                             "[the_person.possessive_title!c]'s chest looks great covered in your cum. But you slowly realise... it's all over her dress."
#                             $ cum_clue = True
#             "Tease her":
#                 "You stand up and tease her."
#                 mc.name "Wow, complaining about a free orgasm? Doesn't matter, I'm about to go back to your place and get my world rocked anyway."
#                 the_person "Geez, okay. I was about to offer you a handjob as thanks, but I guess you'd better save that load then champ."
#                 "[the_person.possessive_title!c] pulls a couple wipes from her clutch and wipes herself clean."
#     elif the_report.get("girl orgasms", 0) == 2:
#         $ the_person.draw_person(position = "kissing")
#         "When you finish, you start to stand up. [the_person.possessive_title!c]'s legs are a little wobbly, and she reaches out for you for support."
#         the_person "Fuck that was nice... you made me cum twice!"
#         "You lean in and start to make out. Her tongue searches out yours eagerly, tasting herself on your tongue. You make out for several seconds before she backs away."
#         the_person "God, I don't think my legs work anymore! I'd better get down on my knees I guess..."
#         menu:
#             "Stop her":
#                 mc.name "What are you doing? This is supposed to be a one way thing. I'll cum in your sister later."
#                 the_person "You're serious? Why not do both?"
#                 mc.name "I promised her I wouldn't go too far. You got your satisfaction, I'll get mine later."
#                 the_person "Geez, okay. I was about to offer to drink your cum as thanks, but I guess you'd better save that load then champ."
#                 "[the_person.possessive_title!c] pulls a couple wipes from her clutch and wipes herself clean."
#             "Let her continue":
#                 $ the_person.draw_person(position = "blowjob")
#                 "As she gets down on her knees, she quickly undoes your zipper and pulls your cock out."
#                 "She gives it a couple strokes, then looks up at you and smiles."
#                 the_person "You'd probably better cum in my mouth... don't want to get it all over my clothes before we go back and see [stephanie.fname]."
#                 $ mc.change_locked_clarity(30)
#                 $ date_outcome = "blowjob"
#                 "You put your hand on the back of her head."
#                 mc.name "You say that like you have a choice."
#                 "She smirks for a second, but quickly opens her mouth as you pull her head down. Her velvet lips wrap around you and start to eagerly suck you off."
#                 call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = blowjob, skip_intro = True, ignore_taboo = True, allow_continue = False) from _call_get_fucked_ashley_second_date_blowjob_01
#                 $ the_report = _return
#                 if the_report.get("guy orgasms", 0) > 0:
#                     if the_person.has_face_cum:
#                         if the_person.outfit.has_dress:
#                             "[the_person.possessive_title!c]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
#                         else:
#                             "[the_person.possessive_title!c]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
#                     elif the_person.has_mouth_cum:
#                         "[the_person.possessive_title!c] has a bit of cum on her chin, but is able to quickly clean it up."
#     else:
#         $ the_person.draw_person(position = "standing_doggy")
#         "When you finish, [the_person.possessive_title]'s legs wobble, then start to give out. She catches herself up against the wall but has trouble standing up."
#         $ the_person.change_stats(happiness = 10, obedience = 5, love = 5, slut = 2)
#         the_person "Fuck that was good... where the hell have you been all my life?"
#         "She tries to stand up for a second, but quickly leans against the wall again."
#         the_person "My legs... they don't work... I'm going to have to pay you back for this another time. Don't worry, I swear I'm good for it."
#         menu:
#             "Take her against the wall" if the_person.is_willing(facing_wall):
#                 mc.name "I'm not sure I believe you. I think I'll take my reward like this."
#                 the_person "I'm sorry... you what?"
#                 $ the_person.draw_person(position = "back_peek")
#                 "You pull your cock out, then push her roughly against the wall, pinning her to it."
#                 the_person "Oh fuck! You'd better wrap that thing up, or my sister will figure out what we did!"
#                 menu:
#                     "Take her raw":
#                         $ date_outcome = "raw sex"
#                         $ mc.condom = False
#                         "You growl at [the_person.possessive_title]."
#                         mc.name "You let me worry about [stephanie.fname]."
#                         "Without waiting for further response, you line yourself up and push your cock into [the_person.title]'s drenched pussy."
#                     "Put on a condom":
#                         $ date_outcome = "protected sex"
#                         $ mc.condom = True
#                         mc.name "Good idea."
#                         "You quickly pull a condom out of your wallet and put it on."
#                         "You line yourself up and push your cock into [the_person.title]'s drenched pussy."
#                 "You slide in easily after her multiple orgasms."
#                 call fuck_person(the_person, start_position = facing_wall, skip_intro = True, position_locked = True, private = True, skip_condom = True) from _call_sex_description_ashley_second_date_fuck_01
#                 $ the_report = _return
#                 if the_report.get("guy orgasms", 0) == 0:
#                     "You decide to pull out before you finish. You want to give your load to [stephanie.possessive_title] later..."
#                 elif the_person.has_creampie_cum:
#                     "When you look down, you can see some cum running down the inside of [the_person.possessive_title]'s legs, but it doesn't seem like any got on her clothes."
#                 elif the_person.has_ass_cum:
#                     if the_person.outfit.has_dress:
#                         "[the_person.possessive_title!c]'s ass looks amazing covered in your cum. But you slowly realise... it's all over her dress."
#                         $ cum_clue = True
#                     else:
#                         "[the_person.possessive_title!c]'s ass looks amazing covered in your cum. Thankfully her dress came off at some point, so no cum got on it."
#                 elif the_person.has_face_cum:
#                     if the_person.outfit.has_dress:
#                         "[the_person.possessive_title!c]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
#                     else:
#                         "[the_person.possessive_title!c]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
#             "Help her recover":
#                 mc.name "I understand. Here, let me help you."
#                 "You grab her arm and help her stand. It takes her several minutes, but she finally gets her legs back."
#                 $ the_person.draw_person()
#     if date_outcome:
#         if cum_clue:
#             the_person "Oh fuck... it's all over my dress!"
#             "[the_person.possessive_title!c] gets some wipes from her clutch, but despite wiping it down as best she can, it is still obvious she's been sprayed down."
#             the_person "Well... maybe my sister won't notice?"
#             mc.name "Yeah. Maybe."
#             "There's no way [stephanie.possessive_title] doesn't notice. But you have to get her home..."
#         else:
#             the_person "Damn that was hot... let me just clean up real quick..."
#             $ the_person.apply_outfit(the_person.planned_outfit)
#             $ the_person.draw_person()
#             "[the_person.possessive_title!c] gets some wipes from her clutch and straightens her clothes out."
#     "You take a couple wipes for yourself, cleaning your face and hands of her juices."
#     the_person "Alright, ready to escort me home like a gentleman?"
#     $ mc.change_location(the_person.home)
#     $ scene_manager = Scene()
#     $ scene_manager.add_actor(ashley)
#     $ scene_manager.add_actor(stephanie, display_transform = character_center_flipped)
#     "You walk into [the_person.title] and [stephanie.possessive_title]'s apartment. Of course, she is right there waiting for you."
#     stephanie "You're here! I was starting to get worried."
#     if cum_clue:
#         "[the_person.title] quickly starts walking toward the hall. [stephanie.title] raises an eyebrow."
#         the_person "Hey sis, sorry I gotta pee really bad!"
#         $ scene_manager.update_actor(ashley, position = "walking_away")
#         "As she walks by [stephanie.possessive_title]..."
#         stephanie "Hey, you got something on your dress..."
#         $ stephanie.change_stats(happiness = -10, love = -5)
#         $ scene_manager.remove_actor(the_person)
#         "[the_person.title] disappears into the restroom, leaving you with [stephanie.title]. You can tell she is suspicious, but for now, she decides not to say anything about it."
#     else:
#         the_person "Hey sis! We had a great time, and don't worry, your boyfriend was a gentleman."
#         stephanie "Ah, that's good."
#         the_person "I'm worn out. I think I'm going to go have a shower. You two try to keep it down so I can get some sleep tonight, okay?"
#         stephanie "No promises."
#         $ scene_manager.remove_actor(the_person)
#         "[the_person.title] disappears into the restroom, leaving you with [stephanie.title]."
#     $ scene_manager.update_actor(stephanie, position = "kissing")
#     "She gives you a hug and whispers in your ear."
#     stephanie "I'm so glad to finally have you for myself. Let's go to my room!"
#     $ scene_manager.clear_scene()
#
#     $ stephanie.change_to_bedroom()
#     $ stephanie.draw_person(position = "walking_away")
#     "You follow [stephanie.possessive_title] to her bedroom. She closes the door, then pushes you back onto her bed."
#     "She strips down in front of you."
#     $ stephanie.strip_outfit(position = "stand4")
#     "She climbs up on top of you and starts to undo your pants. Soon, your cock springs free."
#     $ stephanie.draw_person(position = "cowgirl")
#     stephanie "Mmm, I've been thinking about riding on this all night. Let's get you nice and hard."
#     "[stephanie.title] leans forward and licks all around the top of the shaft, then starts to suck on the tip."
#     $ mc.change_locked_clarity(30)
#     if (date_outcome == "handjob" and not cum_clue) or date_outcome is None:
#         "Her tongue swirls all around you, licking up your pre-cum. Soon you are hard as a rock."
#     elif date_outcome == "handjob" and cum_clue:
#         "She pulls off for a bit, giving you a few strokes with her hand."
#         stephanie "I need to be honest... it looked like Ash had a little something on her dress... you two didn't get naughty again did you?"
#         menu:
#             "Of course not (Lie)":
#                 mc.name "I would never do that to you."
#                 stephanie "Hmm... okay... I think I believe you..."
#                 "She starts to suck on your cock again. Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
#     elif date_outcome == "blowjob" and not cum_clue:
#         "She pulls off for a bit, giving you a few strokes with her hand."
#         stephanie "You taste kind of funny... you and Ash didn't do anything naughty, did you?"
#         menu:
#             "Make up an excuse (Lie)":
#                 mc.name "No, but I have to be honest about something."
#                 stephanie "Oh? About what?"
#                 mc.name "I was a little worried I might get tempted... so I masturbated beforehand."
#                 stephanie "Oh! I guess that makes sense..."
#                 "She starts to suck on your cock again. You think she bought your excuse."
#                 "Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
#     elif date_outcome == "blowjob" and cum_clue:
#         "She pulls off you."
#         $ stephanie.draw_person(position = "cowgirl", emotion = "angry")
#         stephanie "You taste funny... and Ash... that was cum on her dress, wasn't it!?!"
#         menu:
#             "Make up an excuse (Lie)" if mc.charisma > 3:
#                 mc.name "What? Cum? A bird tagged her as we were walking back to the apartment."
#                 stephanie "But... why do you taste like this? This isn't how you normally taste..."
#                 mc.name "I was worried that I might get tempted, so before I left my house I masturbated to help me keep a clear head."
#                 $ stephanie.change_happiness(-2)
#                 $ stephanie.draw_person(position = "cowgirl")
#                 "[stephanie.possessive_title!c] seems just on the verge of calling your excuse bullshit... but then calms down."
#                 stephanie "You promise me, [stephanie.mc_title]?"
#                 mc.name "I promise."
#                 "Whew! She bought it. She leans forward and starts to suck on your cock again."
#                 "Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
#             "Make up an excuse (Lie)\n{menu_red}Not enough Charisma{/menu_red} (disabled)" if mc.charisma <= 3:
#                 pass
#             "Confess":
#                 $ caught_ashley_cheating = True
#                 "Unfortunately, you can't think of a way out of this."
#                 mc.name "Umm, yeah... it was..."
#                 $ stephanie.draw_person(position = "cowgirl", emotion = "angry")
#     elif date_outcome == "protected sex" and not cum_clue:
#         "Her tongue swirls all around you, licking up your pre-cum. It takes a little longer than usual to get it up, having fucked [the_person.title] earlier..."
#     elif date_outcome == "protected sex" and cum_clue:
#         "She pulls off for a bit, giving you a few strokes with her hand."
#         stephanie "I need to be honest... it looked like Ash had something on her dress... you two didn't get naughty again did you?"
#         menu:
#             "Of course not (Lie)":
#                 mc.name "I would never do that to you."
#                 stephanie "Hmm... okay... I think I believe you..."
#                 "She starts to suck on your cock again. Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
#     elif date_outcome == "raw sex":
#         "She pulls off you suddenly."
#         $ stephanie.draw_person(position = "cowgirl", emotion = "angry")
#         stephanie "What the fuck? You taste like pussy!"
#         if stephanie.sex_record.get("Last Sex Day", 0) == day:
#             mc.name "Chill out, we had sex earlier today, remember?"
#             stephanie "That's... right..."
#             stephanie "Wow! I am so sorry, I must seem completely paranoid..."
#             "Whew... you also fucked her sister, but at least she seems to have bought it for now..."
#             "She starts to suck on your cock again. Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
#         elif cum_clue:
#             stephanie "I knew that was cum all over her dress in the hall! Just admit it! You fucked her!"
#             "It seems there is no way of talking your way out of this one. You are totally busted."
#             $ caught_ashley_cheating = True
#         else:
#             stephanie "I knew she couldn't keep her hands off you. You fucked her, didn't you?"
#             "It seems there is no way of talking your way out of this one. You are totally busted."
#             $ caught_ashley_cheating = True
#
#
#     if caught_ashley_cheating:
#         stephanie "I can't believe it... you promised!!!"
#         $ the_person.change_love(-50)
#         mc.name "I..."
#         stephanie "You should go."
#         "There is probably no way for you to patch things up right now... You decide to do as she asks."
#         "You gather your stuff and leave."
#         $ mc.business.add_mandatory_crisis(ashley_steph_second_date_confrontation)
#         $ ashley.event_triggers_dict["caught_cheating"] = True
#         #TODO make a mandatory event to trigger in a day or two where you and stephanie make up.
#     else:
#         stephanie "Mmm, you taste good... but that's not the only thing I want from you tonight..."
#         "[stephanie.title] slowly moves up your body until her hips are on yours. She grinds her cunt a few times along your length, enjoying the pressure against her groin."
#         $ stephanie.change_arousal(10)
#         $ mc.change_locked_clarity(30)
#         if stephanie.has_cum_fetish or stephanie.wants_creampie:
#             "She reaches down and takes your cock in her hand and lines it up with her raw cunt."
#             stephanie "I want to feel you cum inside me tonight. I'm gonna give you the ride of your life and then finish you off deep..."
#             "[stephanie.possessive_title!c] lowers her hips, sheathing your erection. She sighs in satisfaction when she bottoms out."
#             call get_fucked(stephanie, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_ashley_second_date_creampie_steph_01
#         elif stephanie.is_willing(cowgirl):
#             "She reaches over to her nightstand and pulls out a pack of condoms. She grabs one and quickly rolls it onto you with her hand."
#             stephanie "I know you don't like this, but I don't trust myself to pull off in time..."
#             if date_outcome == "protected sex":
#                 "Fine with you. This isn't the first time tonight you've had a condom on."
#             $ mc.condom = True
#             "She reaches down and takes your cock in her hand and lines it up with her cunt."
#             "[stephanie.possessive_title!c] lowers her hips, sheathing your erection. She sighs in satisfaction when she bottoms out."
#             call get_fucked(stephanie, the_goal = "get mc off", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_ashley_second_date_fuck_steph_01
#         else:
#             call get_fucked(stephanie, the_goal = "get mc off", start_position = drysex_cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_ashley_second_date_drysex_steph_01
#         $ stephanie.draw_person(position = "back_peek")
#         "[stephanie.possessive_title!c] turns her back to you. You cuddle up with her, wrapping your arm around her."
#         mc.name "Goodnight..."
#         stephanie "Night..."
#
#         $ stephanie.next_day_outfit = stephanie.outfit # stay in current outfit next day
#         call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_ashley_date_2_01
#
#         $ picked_event = get_random_girlfriend_morning_action(stephanie)
#         if picked_event:
#             call expression picked_event.effect pass (*picked_event.args) from _call_picked_event_stephanie_after_ashley_concert
#             $ del picked_event
#         else:
#             "You wake up, but [stephanie.possessive_title] isn't there. She must have gotten up early and left."
#             $ stephanie.planned_outfit = stephanie.decide_on_outfit() # choose a new outfit for the day
#             $ stephanie.apply_planned_outfit()
#
#     python:
#         mc.business.event_triggers_dict["girlfriend_person"] = None
#         mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = False  #Reset these so we can have another girlfriend sleepover.
#         mc.business.add_mandatory_crisis(ashley_sneaks_over)
#         del cum_clue
#         del caught_ashley_cheating
#         del date_outcome
#     return
#
# label ashley_steph_second_date_confrontation_label():
#     $ the_person = stephanie
#     "Your phone is ringing. It's [the_person.possessive_title]..."
#     mc.name "Hello?"
#     the_person "Hey. I'm going to keep this brief."
#     the_person "I'm okay with work. I'm okay with working for you. I'm okay with even having a booty call now and then."
#     the_person "But as a romantic partner, I'm not okay with you sleeping around, ESPECIALLY with my sister!"
#     the_person "I'm sorry, but I'm breaking up with you."
#     mc.name "Okay, I understand."
#     the_person "I'll see you on Monday."
#     $ the_person.remove_role(girlfriend_role)
#     "[the_person.title] hangs up. Well, that could have gone better. Maybe you can still patch things up somehow?"
#     return
#
# label ashley_sneaks_over_label():   #Requires 60 love and 60 sluttiness events complete.
#     python:
#         mc.change_location(bedroom)
#         the_person = ashley
#         the_person.event_triggers_dict["sneaks_over_complete"] = True
#         ashley.set_event_day("story_event")
#
#     "After a long day, you sit down at your computer to work on a couple things before bedtime."
#     "After getting through some emails, your phone vibrates."
#     $ mc.start_text_convo(the_person)
#     the_person "Hey, are you busy?"
#     mc.name "Not really. What's up?"
#     the_person "Good. I'm outside, can I come in?"
#     $ mc.end_text_convo()
#     "She's what? How does she even know where you live?"
#     $ hall.show_background()
#     $ the_person.draw_person()
#     "You get up and walk to the front door. When you open it, sure enough, there stands [the_person.possessive_title]."
#     mc.name "[the_person.title]... what?"
#     the_person "I know I don't usually do stuff like this, but I wanted to see you... can I come in?"
#     mc.name "Umm, of course..."
#     $ mc.location.show_background()
#     "You quickly take [the_person.possessive_title] back to your room and close the door."
#     if ashley_caught_cheating_on_sister():
#         the_person "I just wanted to... apologise."
#         the_person "Steph and I have always had a bit of sibling rivalry, but she's never been into anyone the way she was into you."
#         the_person "I know it was both of us messing around, but I started a lot of it, so..."
#         the_person "I'm sorry."
#         $ the_person.change_obedience(20)
#         mc.name "It's okay. I'm not sure what is going to happen with [stephanie.fname], but I'm hopeful I can patch things up somehow."
#         "[the_person.possessive_title!c] nods in understanding."
#         the_person "So you really like her too..."
#         mc.name "Yes."
#         the_person "I understand that, I really do. But tonight... I'm here. Maybe for one night, we could just like, pretend?"
#         the_person "I know I'm just a booty call to you, but can I spend the night tonight? And would you treat me the way you treated her?"
#     else:
#         the_person "So, ever since our date the other night, I can't stop thinking about how hot it was."
#         the_person "I'm so tired of the subterfuge... I swiped [stephanie.fname]'s phone and saw you didn't have any plans with her tonight..."
#         mc.name "[the_person.title]..."
#         the_person "I get it, that you and Steph are like, banging each other's brains out every chance you get."
#         the_person "I understand that, I really do. But tonight... I'm here. Maybe for one night, we could just like, pretend?"
#         the_person "I know I'm just a booty call to you, but can I spend the night tonight? And can you treat me the way you treat her?"
#     "Obviously [the_person.possessive_title] has been having jealousy issues for a while, but you assumed they were mostly physical needs."
#     "Now, she's exposing her real feelings, and it seems she's caught feelings for you that run deeper than just sex."
#     $ mc.energy = mc.max_energy
#     $ mc.change_locked_clarity(20)
#     "Seeing her expose herself in this way gives you a burst of energy. She wants the girlfriend treatment? You can give it to her."
#     mc.name "Of course you can stay the night. Don't get mad at me though if [stephanie.fname] gets suspicious when you have trouble walking tomorrow."
#     $ the_person.change_stats(happiness = 10, love = 3)
#     the_person "Me? You'll be lucky if you can get out of bed at all tomorrow!"
#     $ the_person.draw_person(position = "against_wall")
#     "[the_person.title] jumps on to you."
#     "You stumble backwards, falling onto your bed. [the_person.possessive_title!c] lands on top of you."
#     $ the_person.draw_person(position = "cowgirl")
#     "[the_person.title] is so eager, she starts pulling her clothes out of the way."
#     $ the_person.strip_to_vagina(prefer_half_off = True, position = "cowgirl")
#     the_person "What are you waiting for? Get your cock out, yeesh!"
#     "[the_person.possessive_title!c] licks her lips as you quickly pull your pants and underwear down. She grabs your erection and gives it a couple strokes."
#     the_person "Oh god, this thing is mine ALL NIGHT. It's about fucking time..."
#     $ the_person.change_arousal(10)
#     $ mc.change_locked_clarity(30)
#     $ ashley_sex_goal = None
#     if stephanie.has_broken_taboo("condomless_sex") and the_person.has_taboo("condomless_sex"):
#         the_person "Steph told me you guys go at it raw sometimes. I'm not usually into that, but hearing her talk about it makes it sound amazing."
#         the_person "I think it's about time we went for it too."
#         "[the_person.title] points your cock toward her slit, then starts to rub against it. Her arousal glistens at the tip as she moves her hips back and forth."
#         $ the_person.change_arousal(20)
#         $ mc.change_locked_clarity(30)
#         mc.name "Wouldn't it be a bit risky? What if you got knocked up?"
#         if the_person.wants_creampie:
#             the_person "What of it? Isn't that part of the thrill? The risk of pregnancy?"
#             the_person "Wouldn't it be hot to knock up your girlfriend's sister?"
#             $ mc.change_arousal(15)
#             mc.name "I'm not sure how she would like it..."
#             the_person "She doesn't have to know. I could just tell her I had a one night stand and got a little crazy. She'd totally believe it..."
#             $ ashley_sex_goal = "vaginal creampie"
#             mc.name "Then do it."
#         else:
#             the_person "That is part of the challenge. Get as close as you can to going over the edge, then pull off at the last second."
#             mc.name "Still sounds risky, but if you think you can do it, go ahead and try."
#             $ ashley_sex_goal = "body shot"
#         "[the_person.possessive_title!c] stops rolling her hips. With one smooth movement she slides you raw deep into her tight cunt."
#         $ the_person.break_taboo("condomless_sex")
#     elif the_person.has_taboo("condomless_sex") and the_person.effective_sluttiness() >= the_person.get_no_condom_threshold():  #She would normally be willing to go bare
#         the_person "I was talking to Steph about you the other day, and something she told me surprised me."
#         mc.name "Oh?"
#         the_person "She said every time you guys have, you know, she always makes you wrap it up."
#         "[the_person.title] points your bare cock toward her slit, then starts to rub against it. Her arousal glistens at the tip as she moves her hips back and forth."
#         $ the_person.change_arousal(20)
#         $ mc.change_locked_clarity(30)
#         the_person "Wanna feel the real thing? Something my sister never gives you?"
#         mc.name "Wouldn't it be a bit risky? What if you got knocked up?"
#         if the_person.wants_creampie:
#             the_person "What of it? Isn't that part of the thrill? The risk of pregnancy?"
#             the_person "Wouldn't it be hot to knock up your girlfriend's sister?"
#             $ mc.change_arousal(15)
#             mc.name "I'm not sure how she would like it..."
#             the_person "She doesn't have to know. I could just tell her I had a one night stand and got a little crazy. She'd totally believe it..."
#             $ ashley_sex_goal = "vaginal creampie"
#             mc.name "Then do it."
#         else:
#             the_person "That is part of the challenge. Get as close as you can to going over the edge, then pull off at the last second."
#             mc.name "Still sounds risky, but if you think you can do it, go ahead and try."
#             $ ashley_sex_goal = "body shot"
#         "[the_person.possessive_title!c] stops rolling her hips. With one smooth movement she slides you deep into her tight cunt."
#         $ the_person.break_taboo("condomless_sex")
#
#     elif the_person.effective_sluttiness() >= the_person.get_no_condom_threshold():
#         the_person "Mmm, it feels so hot. I just wanna slip it in..."
#         "[the_person.title] points your cock toward her slit, then starts to rub against it. Her arousal glistens at the tip as she moves her hips back and forth."
#         $ the_person.change_arousal(20)
#         $ mc.change_locked_clarity(30)
#         the_person "What would you do if I just sat on it right now? Not even a condom between us?"
#         mc.name "Sounds hot. Do it."
#         if the_person.wants_creampie:
#             the_person "What if I can't stop and pull off in time? What if I just ride you until you shoot your load right up inside me?"
#             mc.name "Are you on birth control?"
#             the_person "Does it matter? Birth control isn't perfect. You could knock me up either way. Do you want to knock up your girlfriend's sister?"
#             $ mc.change_arousal(15)
#             mc.name "I'm not sure how she would like it..."
#             the_person "She doesn't have to know. I could just tell her I had a one night stand and got a little crazy. She'd totally believe it..."
#             $ ashley_sex_goal = "vaginal creampie"
#             mc.name "Then do it."
#         else:
#             the_person "Mmm, god I hope I can pull off in time..."
#             $ ashley_sex_goal = "body shot"
#         "[the_person.possessive_title!c] stops rolling her hips. With one smooth movement she slides your raw cock deep into her tight cunt."
#     else:
#         the_person "Where do you keep your condoms at? I hope you have enough, you're going to need them!"
#         "You point to the nightstand. She quickly grabs the box and throws them on the bed after grabbing one."
#         $ ashley_sex_goal = "get mc off"
#         "[the_person.possessive_title!c] rolls it onto you, then points you at her entrance."
#         $ mc.condom = True
#         "[the_person.title] points your cock toward her slit, then starts to rub against it. Her arousal glistens at the tip of the condom as she moves her hips back and forth."
#         the_person "Here we go. Round one!"
#         "[the_person.possessive_title!c] stops rolling her hips. With one smooth movement she slides you deep into her tight cunt."
#     call get_fucked(the_person, start_position = cowgirl, the_goal = ashley_sex_goal, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_ashley_comes_over_cowgirl_01
#     $ the_person.draw_person(position = "missionary")
#
#     $ the_report = _return
#
#     $ done = False
#     $ girl_came = the_report.get("girl orgasms", 0)
#     $ energy_gain_amount = 50 #Drops each round, representing your flagging endurance.
#     if perk_system.has_ability_perk("Lustful Youth"):
#         $ energy_gain_amount += 70
#     while done == False:
#
#         if mc.energy < 40 and energy_gain_amount <= 20: #Forced to end the fuck date, so we set done to True.
#             "The spirit is willing, but the flesh is spent. Try as she might [the_person.title] can't coax your erection back to life."
#             if girl_came > 0:
#                 the_person "Mmm, I wore you out! That was fun."
#                 "She kisses you and runs her hand over your back."
#             else:
#                 $ the_person.change_stats(slut = -1, love = -3)
#                 the_person "Well I guess we're done then... Maybe next time you can get me off as well."
#             $ done = True
#
#         else:
#             "After a short rest you've recovered some of your energy and [the_person.possessive_title]'s eager to get back to work."
#             $ mc.change_energy(energy_gain_amount)
#             $ the_person.change_energy(energy_gain_amount) #She gains some back too
#             if energy_gain_amount >= 10:
#                 $ energy_gain_amount += -10 #Gain less and less energy back each time until eventually you're exhausted and gain nothing back.
#             menu:
#                 "Fuck her again":
#                     "With your cock hard again, you pull [the_person.title] towards you."
#                     $ mc.change_locked_clarity(30)
#                     call fuck_person(the_person, private = True) from _call_fuck_ashley_sleepover_gf_04
#                     $ the_report = _return
#                     $ girl_came += the_report.get("girl orgasms", 0)
#                     if the_person.energy + energy_gain_amount < 30:
#                         "[the_person.title] is panting. She is completely out of breath."
#                         the_person "That's enough... oh my god, I can't move a muscle..."
#                         the_person "I'm sorry honey, you wore me out! I need to be done for the night..."
#                         $ done = True
#                 "Call it a night":
#                     mc.name "Sorry, I need to get some sleep. I need to be done for tonight."
#                     if girl_came:
#                         the_person "Mmm, okay! That was nice."
#                         "She kisses you and runs her hand over your back."
#                     else:
#                         $ the_person.change_stats(slut = -1, love = -3)
#                         the_person "Well... Maybe next time you can get me off as well?"
#                     $ done = True
#     $ the_person.draw_person(position = "back_peek")
#     "[the_person.possessive_title!c] turns her back to you. You cuddle up with her, wrapping your arm around her."
#     mc.name "Goodnight..."
#     the_person "Night..."
#     $ del ashley_sex_goal
#
#     $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
#     call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_ashley_sleepover_01
#
#     $ the_person.draw_person(position = "walking_away")
#     "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
#     $ mc.change_locked_clarity(50)
#     "She stirs at the same time as you. She gives a big yawn."
#     the_person "... [the_person.mc_title]?"
#     mc.name "Good morning."
#     $ the_person.change_love(5)
#     the_person "Mmm... so this is what it's like? To wake up next to someone you fucked all night sober?"
#     "Her ass wiggles a bit back against you."
#     the_person "It's nice... I could get used to this..."
#     $ the_person.change_happiness(5)
#     "[the_person.title]'s ass wiggling against you soon has you getting hard. She wiggles more when she feels it."
#     the_person "One more for the road? No telling if we'll have this chance again..."
#     mc.name "Sounds good to me..."
#     $ mc.change_locked_clarity(50)
#     "You reach down and run your fingers between her legs. She is already getting wet."
#     "You wipe her juices on your dick, then do your best to point it between her closed legs. You push between her closed thighs, searching for her cunt."
#     if the_person.has_taboo("condomless_sex") and the_person.wants_creampie:
#         the_person "Mmmm... oh my god. I'm way too tired, fuck getting a condom."
#         "She reaches down and parts her legs slightly. She guides your cock towards her slick entrance."
#         "You push yourself partway inside her, but due to the angle it is hard to get deep penetration. However, [the_person.title] seems to enjoy the angle."
#         $ the_person.change_arousal(20)
#         the_person "Ahhh, that feels amazing."
#         "She sighs."
#         the_person "Look... Do what you want when you finish... okay? Just make sure you know what could happen if you cum inside me."
#         mc.name "Mmmm, okay."
#     elif the_person.has_taboo("condomless_sex"):
#         the_person "Mmm, god. I'm way too tired... you can pull out... right?"
#         "She reaches down and parts her legs slightly. She guides your cock towards her slick entrance."
#         "You push yourself partway inside her, but due to the angle it is hard to get deep penetration. However, [the_person.title] seems to enjoy the angle."
#         $ the_person.change_arousal(20)
#         the_person "Ahhh, that feels amazing."
#     else:
#         "She reaches down and parts her legs slightly. She guides your cock towards her slick entrance."
#         "You push yourself partway inside her, but due to the angle it is hard to get deep penetration. However, [the_person.title] seems to enjoy the angle."
#         $ the_person.change_arousal(20)
#         the_person "Ahhh, that feels amazing."
#     "You give her a few tentative strokes, and soon you are established in a nice, easy rhythm."
#     call fuck_person(the_person, private=True, start_position = spooning_sex, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_ashley_sleepover_wakeup_sex_01
#     $ the_person.reset_arousal()
#     $ mc.reset_arousal()
#     "You lay in bed together for a little longer, but soon it is time to start the day."
#     $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
#     $ the_person.apply_planned_outfit()
#     $ the_person.draw_person(position = "stand4")
#     "You both get ready for the day."
#     the_person "Alright, well, hopefully this doesn't make things at work awkward. I'm going to head out. Why don't you wait for a bit before you go anywhere?"
#     mc.name "Okay, have a good day [the_person.title]."
#     $ the_person.draw_person(position = "walking_away")
#     "[the_person.possessive_title!c] turns and walks out your door. You can't help but notice a slight change to her gait."
#     $ clear_scene()
#
#     "Things between [stephanie.title] and her sister are starting to get out of hand. You need to put a stop to their jealousy."
#     "You start to concoct a plan. What if you got them together, the three of you for some drinks, and you dosed them with some serums?"
#     "Maybe you could finally break through and get them to mess around with you, together, so you can stop keeping all this stuff secret."
#     "You should develop some serums that can increase love, and then talk to [the_person.title]."
#     $ the_person.add_unique_on_talk_event(ashley_steph_drinks_out)
#     return  #60
#
# label ashley_steph_drinks_out_label():  #80 Love and sneaks over event complete.
#     "This scene not yet written."
#     "In this scene, you convince the two sisters to share you."
#     $ ashley.event_triggers_dict["is_jealous"] = False
#     $ stephanie.event_triggers_dict["is_jealous"] = False
#     return
#
# label ashley_obedience_struggle():  #Use this label to describe an internal struggle MC has with obeying ashley.
#     $ the_person = ashley
#     "[the_person.title] looks at you, waiting for you to comply."
#     #First, determine if outright willpower failure is possible. Must have performed sub sex scene with ashley and given in.
#     if ashley_dom_fuck_avail() and persistent.mc_noncon_pref == 2:
#         if ashley_mc_submission_score() > 200 and ashley.obedience < 180:
#             "You look back at her. You just don't have the will to resist her demands."
#             return False
#     if persistent.mc_noncon_pref == 2:
#         if ashley_mc_submission_score() > 100:
#             "You look back at her. You just don't have the will to resist her demands."
#             return False
#         if ashley_mc_submission_score() > 0:
#             "You look back at her. You could summon your energy and resist her demands, but it won't be easy."
#             menu:
#                 "Refuse" if mc.energy >= 20:
#                     return True
#                 "Refuse\n{menu_red}Not enough Energy{/menu_red} (disabled)" if mc_energy < 20:
#                     pass
#                 "Give in":
#                     "You just don't have the energy to resist her demands."
#                     return False
#         else:
#             "You look back at her. You could let her have her fun, as crazy as it might get, or you could take things in a different direction."
#             menu:
#                 "Refuse":
#                     return True
#                 "Give in":
#                     "You decide to play along and see how things go, for now."
#                     return False
#     if persistent.mc_noncon_pref == 1:
#         "You look back at her. You could let her have her fun, as crazy as it might get, or you could take things in a different direction."
#         menu:
#             "Refuse":
#                 return True
#             "Give in":
#                 "You decide to play along and see how things go, for now."
#                 return False
#     if persistent.mc_noncon_pref == 0:
#         "You look back at her. Yeah right! Like you would let her take control like that."
#         return False
#
#     return True

# label ashley_room_excitement_overhear_label(the_person):
#     $ the_person = ashley # on_room_enter_event so the_person isn't defined
#     $ the_person.draw_person(position = "standing_doggy")
#     "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
#     the_person "I know! I can't wait to go. All of my friends say it's so much fun..."
#     "But as you enter the room, she notices, and immediately stops talking."
#     $ the_person.draw_person()
#     the_person "..."
#     "Clearly she has no issue talking to her coworkers... why is she so quiet with you? Maybe you should ask her sister about it."
#     $ stephanie.add_unique_on_talk_event(ashley_ask_sister_about_attitude)
#     $ ashley.event_triggers_dict["excitement_overhear"] = True
#     return
#
# label ashley_ask_sister_about_attitude_label(the_person):
#     "You approach [the_person.title], intending to ask her about her sister."
#     mc.name "Hello [the_person.title]. Do you have a moment?"
#     the_person "Of course sir. What can I do for you?"
#     "You lower your voice. You don't necessarily need anyone overhearing you."
#     mc.name "Well... I'm not sure how to say this but, I'm a little concerned about [ashley.fname]."
#     "A grimace forms on her face, but she waits for you to continue."
#     mc.name "Earlier, I was walking by and I could hear her carrying on with her coworkers. But as soon as I entered the room, she went completely silent."
#     "[the_person.title] nods her head as you keep going."
#     mc.name "She barely says a word anytime I talk to her. I feel like I've gotten off to a bad start with her. Do you have any advice?"
#     "[the_person.title] clears her throat."
#     the_person "Well... [ashley.fname] is a bit complicated. She has trouble talking to, and being around men in general..."
#     mc.name "Oh? Oh! I see, I mean I guess that makes sense, not everyone is heterosexual..."
#     the_person "Noooo, no. It isn't that. She's had boyfriends in the past. But something happened between her and her last boyfriend in college."
#     the_person "They broke up all of a sudden, and she's never been the same way around men since then."
#     mc.name "Hmm, that sounds like something bad might have happened."
#     the_person "Yeah... honestly, I can't really talk about it."
#     "[the_person.title] shakes her head, lost in thought."
#     mc.name "Thank you for the insight. I appreciate it."
#     the_person "Of course."
#     $ ashley.add_unique_on_room_enter_event(ashley_room_warming_up)
#     $ ashley.event_triggers_dict["attitude_discussed"] = True
#     return
#
# label ashley_room_warming_up_label(the_person):
#     $ the_person = ashley # on_room_enter_event so the_person isn't defined
#     $ the_person.draw_person(position = "standing_doggy")
#     "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
#     the_person "I know, I just need to find someone to go with!"
#     "As you enter the room, she looks up and stops talking."
#     $ the_person.draw_person()
#     the_person "Ahh... hello sir. Having a good day?"
#     "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
#     mc.name "It's been great so far. And you?"
#     the_person "Oh... it's been good I guess..."
#     mc.name "Glad to hear it."
#
#     $ ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
#     return
#
#
# label ashley_mandatory_ask_about_porn_label():
#     "You've had some time to think about [ashley.possessive_title], since you went on your date and discovered she was in a porn video unwittingly."
#     "She seems to have warmed up to you enough; you decide that maybe it is the right time to talk to her about it."
#     $ ashley.event_triggers_dict["porn_convo_avail"] = True
#     return
#
# label ashley_clothes_shopping_label(the_person):
#     $ ashley.set_override_schedule(None, day_slots = [6], time_slots = [2])
#     "You decide to swing by the clothing store, where [the_person.title] said she would be at. After a few awkward minutes poking around the women's clothing, you spot her."
#     $ the_person.draw_person()
#     "She seems preoccupied and doesn't notice you until you walk up."
#     mc.name "Hey [the_person.title]. I thought I might find you here."
#     the_person "Ah... Hello..."
#     if ashley_is_fwb_path():
#         mc.name "I remembered at the coffee shop this morning you said you were gonna come here. I was in the area and thought I could swing by. I thought you might appreciate a male perspective on your outfits?"
#         the_person "Oh, I suppose that would be okay..."
#         "Without the security of her sister nearby, [the_person.possessive_title]'s shy demeanour is really showing."
#     elif ashley_is_secret_path():
#         mc.name "You said you were gonna try on a couple things. I thought maybe you would appreciate the opinion of a secret admirer..."
#         the_person "Ah, that sounds good..."
#     elif ashley_is_normal_path():
#         mc.name "When you said you were gonna swing by here later, I knew I wanted to come out and see some of these outfits for myself."
#         "She smiles and replies shyly."
#         the_person "Ah, that's good. Let's see what we can find."
#
#     "[the_person.title] looks around at a few different clothing racks and puts an outfit together. It looks very similar to the outfit you saw earlier today. You follow her over to the changing rooms."
#     if ashley.is_girlfriend:
#         the_person "Here... Come on in with me. You're my boyfriend I'm sure no one will mind."
#         "You quickly slip into the dressing room with [the_person.title]."
#     elif the_person.sluttiness > 30:
#         "She looks around and sees that there isn't anyone around."
#         the_person "Here... Come in with me, before anyone notices..."
#         "You quietly slip into the dressing room with [the_person.title]."
#     "You sit down at the bench and watch as [the_person.possessive_title] starts to strip down."
#     $ the_person.strip_outfit(exclude_upper = False)
#     $ mc.change_locked_clarity(30)
#     if the_person.sluttiness > 50:
#         "Although she doesn't say a word, [the_person.title] doesn't make any move to cover herself either. Her body is on display as she reaches for her outfit..."
#     else:
#         "[the_person.title] absentmindedly covers her mound with one hand as she reaches for her outfit."
#     $ the_person.apply_outfit(the_person.personalize_outfit(ashley_get_observed_outfit(), coloured_underwear = True))
#     $ the_person.draw_person()
#     "When she finishes putting on her new outfit, she steps back so you can get a good look."
#     the_person "Okay... What do you think?"
#     $ the_person.draw_person(position = "back_peek")
#     "She gives a quick twirl, letting you check her out from all angles. You make sure to take in all the details."
#     $ the_person.draw_person()
#     menu:
#         "Keep it":
#             mc.name "I like it. You should get it."
#             the_person "I think so too. Thanks!"
#             $ the_person.wardrobe.add_outfit(the_person.outfit)
#         "Not for you":
#             mc.name "Sorry, it's an interesting outfit, but I don't think it's right for you."
#             the_person "Yeah... I was thinking the same thing..."
#     if the_person.is_girlfriend:
#         # the_person "So, I know that like... Clothes shopping can be pretty boring for guys... So I was wandering..."
#         # "Her voice trails off. You can tell she is trying to suggest something fun, but she's to shy to say it out loud."
#         # mc.name "You want to make this more interesting?"
#         # the_person "Err, kind of... I was thinking, maybe while I change, you could go pick something out for me? As a reward for helping me... I'll try on anything you want me to..."
#         # "That does sound like a fun proposition!"
#         # the_person "If it's too crazy though, maybe it's an outfit we could save for the bedroom..."
#         # mc.name "Sounds good! I'm sure I can find something..."
#         # "You step out of the dressing and browse the clothes racks, looking for a nice outfit for your girlfriend."
#         # [Outfit screen]
#         # [If not outfit]
#         # For some reason, you can't seem to put together a good look for Ashley. You head back to the dressing room and apologize through the door.
#         # "Hey, sorry Ashley, for some reason I couldn't come up with anything..."
#         # "Oh! That's okay... Sorry to put you on the spot like that..."
#         # [Have outfit]
#         # You put something together and take it back to the dressing room. Making sure no one is around, you quietly slip into the room.
#         # [Draw naked ashley]
#         # You hand her the outfit. When she finishes putting it on, she checks herself in the mirror.
#         # [Draw outfit backpeek]
#         # [If normal outfit]
#         # "Hmm... Interesting..."
#         # [Draw standing]
#         # "I could wear this... For you anyway..."
#         # Ashley gives you a shy smile.
#         # "I'll get it for you. Now go out and wait for me! I'll be right out..."
#         # [If slutty]
#         # "Oh... Oh my..."
#         # [Draw standing]
#         # "Would this excite you? If you came over and when I answered the door I was wearing this..?"
#         # "Definitely..."
#         # "Mmm... Okay... I'll get it... But I'm only gonna wear it for you!"
#         # "Now go out and wait for me..."
#         # [Clear ashley]
#         $ clear_scene()
#         $ the_person.apply_outfit(the_person.planned_outfit)
#         "She shoos you out of the changing room. In a few minutes, she emerges from the changing room."
#         $ the_person.draw_person()
#         the_person "Thanks for waiting..."
#         the_person "Say, do you wanna come over tonight? You could, you know, stay over..."
#         $ mc.change_locked_clarity(20)
#         menu:
#             "Come over later" if schedule_sleepover_available():
#                 mc.name "I wouldn't mind a sleepover."
#                 the_person "I'll see you tonight then..."
#                 $ schedule_sleepover_in_story(the_person)
#             "Come over later (disabled)" if not schedule_sleepover_available():
#                 pass
#             "Not tonight":
#                 mc.name "I can't tonight, maybe another night..."
#
#         "You say goodbye to [the_person.title] for now."
#     elif the_person.jealous_score > 0:
#         "Before she starts to change back, [the_person.title] starts to tease you."
#         the_person "So... I can't help but notice that [stephanie.fname] has been getting a lot of attention lately..."
#         $ the_person.strip_outfit(exclude_lower = True)
#         $ desc_tuple = the_person.jealous_sister_get_revenge_tuple()
#         the_person "[desc_tuple[0]]"
#         $ the_person.strip_outfit()
#         the_person "I can't help but feel like it should be my turn to get off..."
#         "She walks over to you. Sitting on the bench, her cunt is now just {height_system} away."
#         $ mc.change_locked_clarity(20)
#         $ the_position = cowgirl
#         if desc_tuple[1] == 1: #Foreplay
#             $ the_position = drysex_cowgirl
#         elif desc_tuple[1] == 2:
#             $ the_position = standing_cunnilingus
#         elif desc_tuple[1] >= 4:    #If 4 let the system make a position for her.
#             $ the_position = None
#         call get_fucked(the_person, the_goal = "get off", private= True, start_position = the_position, allow_continue = True) from _ashley_jealous_clothes_tryout_01
#         if _return.get("girl orgasms", 0):
#             the_person "Ahhh, that was nice. Good to know my sister isn't getting ALL your attention!"
#             $ the_person.reset_all_jealousy()
#             $ the_person.change_stats(slut = 1, love = 3)
#         else:
#             the_person "Wow, really? You can't give me the same treatment that [stephanie.fname] gave you? She got you all worn out?"
#             "She looks pissed."
#             $ the_person.change_stats(slut = -1, love = -3)
#             $ the_person.jealous_change_score(3) #Add points to jealous score so Ashley gets more desperate.
#         $ the_person.draw_person(position = "stand2")
#         "You get yourself put back together."
#         mc.name "I'm going to slip out."
#         the_person "Okay, I'll see you around [the_person.mc_title]."
#         $ clear_scene()
#         "You quietly exit the changing room."
#     else:
#         the_person "Thanks for the opinion. I'm going to go ahead and change back..."
#         mc.name "I'm going to slip out."
#         the_person "Okay, I'll see you around [the_person.mc_title]."
#         $ clear_scene()
#         "You quietly exit the changing room."
#
#     # make sure she changes back into her normal outfit
#     $ the_person.apply_planned_outfit()
#     return
#
# label ashley_test_outfit_scene():
#     $ scene_manager = Scene()
#     $ the_person = ashley
#     $ preferences = WardrobePreference(the_person)
#     $ bystander = get_random_from_list(known_people_in_the_game(excluded_people = [ashley, stephanie]))
#
#     if not bystander:
#         return  # exit loop if we have no bystander
#
#     "Enjoying your coffee, you zone out for a minute while the two sisters are chatting, when suddenly the talking stops. You look up and see them both looking out the restaurant window."
#     "Outside is a woman who has stopped and is checking her phone for something. The girls are checking her out."
#
#     $ scene_manager.add_actor(bystander, display_transform = character_right_flipped, position = "stand3")
#     "She takes a moment to look at something on her phone."
#     "Then she walks away."
#     $ scene_manager.add_actor(bystander, display_transform = character_right_flipped, position = "walking_away")
#     "The girls watch as she walks away."
#     $ scene_manager.remove_actor(bystander)
#     the_person "Wow, did you see that?"
#
#     $ new_outfit = the_person.personalize_outfit(bystander.outfit, opinion_color = "the colour green", coloured_underwear = True)
#
#     $ ashley.apply_outfit(new_outfit)
#     $ stephanie.apply_outfit(new_outfit)
#     $ scene_manager.add_actor(ashley)
#     "[ashley.fname] models her new outfits for you."
#
#     python:
#         del bystander
#         del preferences
#     $ scene_manager.clear_scene()
#     return
#
#
# label ashley_unit_test():
#     python:
#         the_person = ashley
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person._sluttiness = 0
#         the_person._obedience = 100
#         the_person.happiness = 100
#         the_person.love = 0
#     "Unit Test Ashley hiring scene."
#     call ashley_intro_label from _unit_test_ashley_01
#     if ashley.is_employee:
#         "You hired Ashley"
#     else:
#         "You did not hire Ashley."
#         call ashley_hire_directed_label from _unit_test_ashley_02
#         "You still have not hired Ashley. Aborting unit test."
#
#     "Unit test Ashley Intro."
#     call ashley_first_talk_label(the_person) from _unit_test_ashley_03
#
#     "A few days later"
#     call ashley_first_talk_label(the_person) from _unit_test_ashley_04
#
#
#     call ashley_room_excitement_overhear_label(the_person) from _unit_test_ashley_05
#     call ashley_ask_sister_about_attitude_label(stephanie)from _unit_test_ashley_06
#     call ashley_room_warming_up_label(the_person) from _unit_test_ashley_07
#     call ashley_room_overhear_classical_label(the_person) from _unit_test_ashley_08
#     call ashley_ask_date_classic_concert_label(the_person) from _unit_test_ashley_09
#     call ashley_ask_date_classic_concert_label(the_person) from _unit_test_ashley_10
#     call ashley_classical_concert_date_label() from _unit_test_ashley_11
#     call ashley_porn_video_discover_label() from _unit_test_ashley_12
#     call ashley_ask_sister_about_porn_video_label(stephanie) from _unit_test_ashley_13
#     python:
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person._sluttiness = 20
#         the_person._obedience = 100
#         the_person.happiness = 100
#         the_person.love = 0
#
#     call ashley_mandatory_ask_about_porn_label() from _unit_test_ashley_14
#     call ashley_ask_about_porn_label(the_person) from _unit_test_ashley_15
#     return
#
# label ashley_unit_test2():
#     python:
#         the_person = ashley
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person._sluttiness = 40
#         the_person._obedience = 100
#         the_person.happiness = 100
#         the_person.love = 0
#         stephanie.love = 100
#         stephanie._sluttiness = 40
#         stephanie.energy = stephanie.max_energy
#         mc.max_energy = 200
#         mc.energy = mc.max_energy
#     call ashley_post_handjob_convo_label(the_person) from _unit_test_ashley_16
#     call ashley_stephanie_arrange_relationship_label(stephanie) from _unit_test_ashley_17
#     call ashley_stephanie_saturday_coffee_intro_label(the_person) from _unit_test_ashley_18
#     python:
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person._sluttiness = 40
#         the_person._obedience = 100
#         the_person.happiness = 100
#         the_person.love = 0
#         stephanie.love = 100
#         stephanie._sluttiness = 40
#         stephanie.energy = stephanie.max_energy
#     "Coffee recurring. She should be ready for second date to proc from this."
#     call ashley_stephanie_saturday_coffee_recur_label(the_person) from _unit_test_ashley_19
#     #ashley_second_concert_intro_label(the_person)
#     call ashley_second_concert_date_label() from _unit_test_ashley_20
#     "Test stephanie's breakup dialogue"
#     call ashley_steph_second_date_confrontation_label from unit_test_ashley_21
#     python:
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person._sluttiness = 60
#         the_person._obedience = 100
#         the_person.happiness = 100
#         the_person.love = 40
#         stephanie.love = 100
#         stephanie._sluttiness = 40
#         stephanie.energy = stephanie.max_energy
#         mc.max_energy = 200
#         mc.energy = mc.max_energy
#     "Blowjob test"
#     call ashley_blows_during_meeting_label from unit_test_ashley_22
#
#
#     return
#
# init 2 python: #Coffee time requirements function. #TODO should I pull out coffee times stuff to its own file? this file might get too big.
#     def coffee_time_innocent_chat_requirement():
#         return True
#
#     def coffee_time_woman_walks_by_requirement():
#         return True
#
#     def coffee_time_sexy_chat_requirement():
#         if stephanie.sluttiness > 40 and ashley.sluttiness > 40:
#             return True
#         return False
#
#     def coffee_time_steph_gets_handsy_requirement():
#         if stephanie.sluttiness > 40:
#             if ashley_get_coffee_partner() == stephanie:
#                 return True
#         return False
#
# init 3 python:
#     ashley_coffee_time_action_list = []
#     steph_coffee_time_action_list = []
#
#     coffee_time_innocent_chat = Action("Sister Talk", coffee_time_innocent_chat_requirement, "coffee_time_innocent_chat_label")
#     coffee_time_sexy_chat = Action("Sister Sexy Talk", coffee_time_sexy_chat_requirement, "coffee_time_sexy_chat_label")
#     coffee_time_steph_gets_handsy = Action("Stephanie gets handsy", coffee_time_steph_gets_handsy_requirement, "coffee_time_steph_gets_handsy_label")
#     coffee_time_woman_walks_by_label = Action("Woman walks by", coffee_time_woman_walks_by_requirement, "coffee_time_woman_walks_by_label")
#
#     ashley_coffee_time_action_list.append(coffee_time_innocent_chat)
#     ashley_coffee_time_action_list.append(coffee_time_sexy_chat)
#     ashley_coffee_time_action_list.append(coffee_time_woman_walks_by_label)
#     steph_coffee_time_action_list.append(coffee_time_innocent_chat)
#     steph_coffee_time_action_list.append(coffee_time_sexy_chat)
#     steph_coffee_time_action_list.append(coffee_time_steph_gets_handsy)
#
#     def ashley_coffee_time_get_random_action():
#         possible_action_list = []
#         for ashley_scene in ashley_coffee_time_action_list:
#             if ashley_scene.is_action_enabled(): #Get the first element of the weighted tuple, the action.
#                 possible_action_list.append(ashley_scene) #Build a list of valid crises from ones that pass their requirement.
#         return get_random_from_list(possible_action_list)
#
#     def steph_coffee_time_get_random_action():
#         possible_action_list = []
#         for steph_scene in steph_coffee_time_action_list:
#             if steph_scene.is_action_enabled(): #Get the first element of the weighted tuple, the action.
#                 possible_action_list.append(steph_scene) #Build a list of valid crises from ones that pass their requirement.
#         return get_random_from_list(possible_action_list)
#

#End coffee time code
