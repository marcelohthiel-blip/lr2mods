# ****HR Director role****
# Early game: She adds her charisma and HR skill to max efficiency. Lets events scale this factor up
# Mid game: She can help shape employee work interests. She will automatically work with employees in different departments increasing their relevant likes and dislikes.
#   Once per week, you can target an individual girl and a specific work interest.
# As she gets corrupted, the opinions she can train evolve. EG: showing tits, skimpy uniforms
# Late game: Unlocks threesome scenes with employees.
#
# Required Labels
# Initial Hiring
# First Monday review
# Subsequent Monday meetings
# HR Stage One event: Beginning once a week, can have personal interview with one employee.
# HR stage two event: Can create new training videos to be looped in break rooms, emphasizing "company values"
# HR stage three event: Company sponsored sexual training.
#
#####HR Director ACTION LABELS#####

label HR_director_initial_hire_label(the_person):
    "You get an alert on your phone 'Go meet [the_person.fname]'."
    if mc.is_at_office:
        "So you finish up and walk down to the lobby."
    else:
        "You quickly go over to the office to meet her."

    $ mc.change_location(lobby)
    $ the_person.draw_person()
    if the_person == sarah:
        "As you walk in, you see [the_person.title] is already there waiting for you."
        "Since she is new to the company in general, you give [the_person.title] a tour of the company first."
        the_person "So... what kind of pharmaceuticals are being researched, exactly?"
        "You decide to just be honest. If she is going to be working here at the company, she is going to figure it out sooner or later anyway."
        mc.name "Well, most of our research right now is targeted toward making people's lives better."
        mc.name "We came across a formula not long ago with almost no known side effects, that with tweaks to the final formula can be used for a number of different things, from increasing happiness to increasing charisma, to making sex better."
        the_person "Wow, that sounds very versatile!"
        "After the tour you head back to your office."

    else:
        "As you walk in, you see her already waiting for you, you say hello and head over to your office with her."

    $ mc.change_location(ceo_office)
    the_person "Well, I am excited to have this opportunity. To be honest I'm not really even sure where to begin!"
    mc.name "I'll tell you what, for the rest of this week, why don't you just get to know the other employees and see how they perform. I'll send over to you my personal dossiers on all the employees, and as you have time you can look over them."
    the_person "Okay, I can do that. I'll look over them over the weekend as well. Do you want to plan on having a meeting sometime next week?"
    mc.name "That sounds good. How about we do lunch on Monday? Since you are going to be heading up the department, having a meeting every week might be a good idea."
    $ the_person.draw_person(emotion = "happy")
    the_person "Great! I'll look forward to it. I'll try to have a plan ready for the meeting on Monday on what we can accomplish."
    if day % 7 == 4:
        mc.name "Good, then I will see you on Monday for your first work day."
    else:
        mc.name "Good, then I will see you tomorrow for your first work day."
    $ the_person.draw_person(position = "walking_away")
    "You shake hands with [the_person.possessive_title] and watch her while she walks out of your office."

    python:
        mc.business.add_employee_hr(the_person)
        # assign special HR director role
        mc.business.hire_HR_director(the_person)
        # add staff loyalty duty
        the_person.primary_job.add_duty(encourage_loyalty_duty)

        add_hr_director_first_monday_action(the_person)
    return

label HR_director_first_monday_label(the_person):
    if not mc.business.hr_director:
        "Since you have no HR director, there are no Monday morning meetings, appoint a new HR director, to resume meetings."
        return
    $ mc.new_repeat_event("HR Meeting", 0, 1)
    $ the_person.set_event_day("hr_weekly_meeting")
    "It's lunchtime, so you prepare to have your first meeting with your new HR Director, [the_person.title]."
    "You grab your lunch from the break room, head to your office, and sit down."
    $ scene_manager = Scene()
    $ mc.change_location(ceo_office)
    $ scene_manager.add_actor(the_person)
    "Soon, [the_person.title] appears in your door."
    the_person "Knock knock!"
    "She walks into your office and sits down across from you."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You both sit quietly for a minute, eating your lunches together. Eventually you break the silence."
    mc.name "So, did you have a chance to go over those dossiers?"
    the_person "I did! Actually. There's a surprising amount of detail in them..."
    the_person "I'm not sure I want to know how you gave a numerical rating to girls and their... sexual performance, but it is definitely useful info."
    "[the_person.possessive_title!c] pulls out a notebook and looks at some notes she has taken."
    the_person "So far, aside from personnel, I've noted a few different areas where I think I can improve the efficiency of the business."
    the_person "With your approval, I can go ahead and get those started. Are you okay with that?"
    mc.name "Yes, definitely. Efficiency is always a concern at a small business like this."
    the_person "Right, aside from that, I have an idea for a new program. Basically, I noted in the dossiers that there are several employees here who either don't enjoy what they are doing, or are unhappy for some other, unknown reason..."
    the_person "My proposal is to start a program where, every weekend I'll go through all the latest employee info and compile a list of girls most at risk at quitting."
    the_person "We can call one in, and see if we can have a productive discussion on their reservations. Maybe over time we can even change their opinions on work tasks they don't currently enjoy."
    mc.name "That sounds like a good idea, but why limit it to one girl a week?"
    the_person "Well, we don't want to come across as micromanaging. People are more productive if they feel they have some degree of autonomy in their work."
    the_person "Besides that, it takes time! And if we did it all the time, I think it would lose some of the effectiveness."
    mc.name "Okay. That all sounds like good ideas. Should we make this Monday lunch a permanent arrangement? We can talk about the developments of the past week, discuss who we want to meet with, and make a plan for the upcoming week."
    $ scene_manager.update_actor(the_person, emotion = "happy")

    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, 0)
    if builtins.len(HR_employee_list) == 0:
        the_person "That sounds great! Alright, I currently have no employees that would benefit from a meeting, perhaps next week."
    else:
        the_person "That sounds great! Alright, I actually have a set of possibilities arranged for a meeting today if you would like. Do you want to go over my list of girls?"
        menu:
            "Let's start next week":
                pass
            "Let's start today":
                mc.name "If you think meeting with some of these girls would be helpful, I think we should start immediately."
                the_person "OK! Let me see who I have on my list here..."
                call HR_director_personnel_interview_label(the_person, max_opinion = HR_tier_talk) from HR_DIR_INTERVIEW_CALL_1

    mc.name "Alright, I think that is all for today. Unless something comes up, same time next week?"
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Sounds great! I'll see you then!"
    $ add_hr_director_monday_meeting_action(the_person)
    # HR tiers based on progression. 1 = hired someone. 2 = training videos. 3 = company sponsored sexual training.
    $ set_HR_director_tag('business_HR_tier', 1)

    if the_person is sarah:
        $ add_sarah_third_wheel_action()
    $ scene_manager.clear_scene()
    return

label HR_director_monday_meeting_label(the_person):
    if not mc.business.hr_director:
        "Since you have no HR director, there are no Monday morning meetings, appoint a new HR director, to resume meetings."
        return

    $ scene_manager = Scene()
    $ the_person.set_event_day("hr_weekly_meeting")
    if not mc.is_at(ceo_office):
        "You hurry to your office for your weekly meeting with your HR director [the_person.title]."
        $ mc.change_location(ceo_office)
        the_person "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        mc.name "Hi [the_person.title], come in and take a seat."
    else:
        $ mc.location.show_background()
        the_person "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        "Your HR Director appears in the doorway to your office. It is time for your weekly HR meeting."
        "She sits down across from you and starts to eat her lunch."

    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 40 and not get_HR_director_tag("business_HR_sexy_meeting", False):
        $ set_HR_director_tag("business_HR_sexy_meeting", True)
        $ hr_director_prog_scene.call_scene([the_person])
    elif get_HR_director_tag("business_HR_sexy_meeting", False):
        $ hr_director_prog_scene.call_scene([the_person])
    the_person "Here are my plans for the week. I think I have a few tweaks to efficiency I can make, but overall I wouldn't expect to see a big change company-wide."

    "She hands you a few documents. You check them over."
    mc.name "Looks good. Go ahead and continue with those plans."
    #$ scene_manager.clear_scene()

    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, get_HR_director_tag("business_HR_coffee_tier", 0))
    if builtins.len(HR_employee_list) == 0:
        the_person "Can do! I currently have no girls on my counselling list, perhaps next week."
    else:
        the_person "Can do! Did you want to call in a girl for a counselling session this week?"
        menu:
            "Call one in":
                mc.name "Yes, I want to do that."
                the_person "OK! Let me see who I have on my list here..."
                call HR_director_personnel_interview_label(the_person, max_opinion = get_HR_director_tag("business_HR_coffee_tier", 0)) from HR_DIR_INTERVIEW_CALL_2
                if _return:
                    $ set_HR_director_tag("business_HR_meeting_last_day", day)
                $ scene_manager.update_actor(the_person, position = "sitting")
            "Let's not this week":
                pass

    the_person "Hmm, let's see, what's next..."
    call HR_director_manage_gym_membership(the_person) from HR_Gym_manage_1

    if not get_HR_director_tag("business_HR_headhunter_initial", False) and recruitment_batch_two_policy.is_owned:  #Unlock the new headhunter rewards
        the_person "Our new recruiting software is useful for widening the pool of applicants to hire from, but when you cast a wider net, sometimes you get less than desirable results."
        the_person "After this meeting, I'll see if I can rework some of the software to better find applicants for specific departments."
        the_person "If you want to find an employee for a specific job, let me know, I might be able to get more fitting results!"
        $ set_HR_director_tag("business_HR_headhunter_initial", True)
    elif get_HR_director_tag("business_HR_headhunter_initial", False):
        call HR_director_monday_headhunt_update_label(the_person) from HR_headhunter_monday_update_1

    the_person "Ok, next up, I wanted to review progress made on serums and policy changes from the past week to see if anything might be useful."
    call HR_director_review_discoveries_label(the_person) from HR_DIR_INTERVIEW_CALL_3
    mc.name "Alright, I think that is all for today. Unless something comes up, same time next week?"
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Sounds great! I'll see you then!"
    if not the_person.is_wearing_planned_outfit:
        "[the_person.possessive_title!c] quickly rearranges her clothes."
        $ the_person.apply_planned_outfit(show_dress_sequence = True, scene_manager = scene_manager)
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She turns around and leaves your office."

    $ add_hr_director_monday_meeting_action(the_person)
    $ scene_manager.clear_scene()
    return

label HR_director_personnel_interview_label(the_person, max_opinion = 0):
    $ (HR_employee_list, HR_tier_talk) = build_HR_review_list(the_person, max_opinion)
    if builtins.len(HR_employee_list) == 0: #No one qualifies!
        the_person "Actually, things are running really smoothly right now, I didn't come across any dossiers this past weekend that drew my attention!"
        #TODO add another option here? Offer to bring in any girl?
        return
    if HR_tier_talk == 0:
        the_person "Alright, here's my list. Who do you want me to call in?"
    elif HR_tier_talk == 1:
        the_person "Things are running pretty good right now, but they could always be better. Here's my list, who do you want me to call in?"
    elif HR_tier_talk == 2:
        the_person "Honestly? All the girls here like all the policies I've looked at, but it's possible with a bit of persuasion we could make them love them."
        the_person "Here's my list. Who do you want me to call in?"

    # use new menu layout for selecting people
    call screen main_choice_display(build_menu_items([["Call in"] + HR_employee_list + ["Changed my mind"]], draw_hearts_for_people = False))
    $ person_choice = _return

    if person_choice == "Changed my mind":
        return False

    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Alright, let me go get her."
    $ scene_manager.hide_actor(the_person)
    "[person_choice.title] steps in to the office after a few minutes, followed by [the_person.title]."
    person_choice "Hello [person_choice.mc_title]."

    $ scene_manager.add_actor(person_choice, position = "stand3", display_transform = character_left_flipped)
    mc.name "Hello [person_choice.title], come in and take a seat."

    $ scene_manager.update_actor(person_choice, position = "sitting")
    $ scene_manager.show_actor(the_person)

    if the_person.sluttiness > 80:
        "You notice that [the_person.title] locks the door as she enters your office."

    if the_person.outfit.cum_covered:
        "[person_choice.title] sits down across from you, but is clearly distracted by [the_person.title]. She clearly notices your cum still on her."
        $ mc.change_locked_clarity(20)
        if willing_to_threesome(person_choice, the_person):
            person_choice "Wow, not sure why you called me in here, but I hope it's for the same thing you have her in here for..."
        else:
            person_choice "Is that... I'm sorry, what is it that you needed, [person_choice.mc_title]?"
        $ person_choice.change_slut(2) # give her a temp slut boost to maybe have a threesome later...
    elif the_person.vagina_visible:
        $ mc.change_locked_clarity(20)
        "[person_choice.title] sits down across from you, but is clearly distracted by [the_person.title] showing off her pussy."
        $ person_choice.change_slut(2)
        if willing_to_threesome(person_choice, the_person):
            person_choice "I really like you the outfit you are wearing [the_person.fname]."
        else:
            person_choice "Uh... right, what can I do for you, [person_choice.mc_title]?"
    elif the_person.tits_visible:
        $ mc.change_locked_clarity(20)
        "[person_choice.title] sits down across from you, but is clearly distracted by [the_person.title]'s exposed tits."
        $ person_choice.change_slut(1)
        if willing_to_threesome(person_choice, the_person):
            person_choice "That outfit really shows off your assets [the_person.fname], I love it."
        else:
            person_choice "Oh... what can I do for you, [person_choice.mc_title]?"
    else:
        "[person_choice.title] sits down across from you at your desk."
        person_choice "Yes [person_choice.mc_title], is something wrong?"

    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        the_person "Some coffee, while we talk?"
        person_choice "Sure. [person_choice.coffee_style!c], please."
        "[the_person.title] pours a cup of coffee while talking."
        the_person "Thanks for coming. [mc.name] just wanted to have a quick chat. Here, have a cup of coffee."
        $ scene_manager.update_actor(the_person, position = "sitting")
        "[person_choice.title] takes the coffee and nods. She takes a few sips as you begin."
    else:
        "[the_person.title] starts talking while she sits down."
        $ scene_manager.update_actor(the_person, position = "sitting")
        the_person "Thanks for coming. [mc.name] just wanted to have a quick chat."

    mc.name "That's right. As you know, we run a small business here, and I like to make sure all my employees enjoy their work here."
    mc.name "Recently, I've become concerned you may not like the work environment."

    call screen main_choice_display(build_menu_items([build_HR_interview_discussion_topic_menu(person_choice, max_opinion)]))
    $ opinion_chat = _return

    if opinion_chat == "working":
        mc.name "I know that a job is just a job, but I think if you take the time to get to know your fellow employees and come in each day with a good attitude, you could learn to like coming to work every day."
    elif opinion_chat == "HR work":
        mc.name "I know that working with people all day long can be exhausting, but think about how much you can impact your fellow employees if you greet them with a smile every day."
    elif opinion_chat == "production work":
        mc.name "I know that production work is boring and tedious, but it is your hard work down in the production lab that keeps this business moving forward."
    elif opinion_chat == "research work":
        mc.name "I know that sometimes research work feels thankless, but I want you to know right now, I am so thankful for all the hard work you put into the department."
    elif opinion_chat == "marketing work":
        mc.name "I know that marketing work is difficult. For every sale there's dozens of rejections. But I want you to know that without your hard work, it doesn't matter how good our product is if no one knows it's being made."
    elif opinion_chat == "supply work":
        mc.name "I know that sourcing chemicals and trying to keep costs down is thankless work, but I want you to know, as the owner of the company, I appreciate your hard work and dedication to doing what needs to be done."
    elif opinion_chat == "work uniforms":
        mc.name "I know that it feels like we are taking some of your creativity away when we assign uniforms. I understand that, but it is also important that we keep a professional atmosphere here."
    elif opinion_chat == "skimpy uniforms":
        mc.name "I know that it feels weird, being asked to come in to work wearing clothes that show a little skin, but in the market we are in, dressing to impress can be a key business advantage."
    elif opinion_chat == "sports":
        mc.name "I know that it might be unconventional, but we feel that an employees physical health will benefit the company as much as their labour skills."
    else:
        mc.name "I know the policy in place feels weird, but I want you to rethink your opinion on [opinion_chat]. It would be helpful if you would."
    the_person "All of our employees are valued here, not just as employees, but as people."
    if person_choice.obedience > 120: #She is obedient
        person_choice "I'm not sure I really thought about being here as more than just another job... but I want this place to succeed. I want you to succeed, [person_choice.mc_title]."
    else:
        person_choice "I guess I never really thought about [opinion_chat] like that. I mean, if I have to have a job... I guess I might as well try to be more positive about it, right?"

    $ scene_manager.update_actor(person_choice, emotion = "happy")
    "[person_choice.title] thinks for a moment, then smiles at both of you."

    # when HR Director is Sarah, also wait for threesome unlock event
    if willing_to_threesome(person_choice, the_person) and (not the_person is sarah or sarah_threesomes_unlocked()):

        person_choice "Thanks for calling me in. Is that all? Or was there maybe someone... I mean some{i}THING{/i} else on the to-do list?"
        menu:
            "Attempt a threesome with [the_person.title]":
                mc.name "I have one more thing for you before you go..."
                person_choice "Yes sir?"
                mc.name "Having this meeting has been great, but, I think you could use a little more... hands-on training."
                person_choice "Mmm, that sounds nice, is [the_person.fname] going to join us?"
                $ mc.change_locked_clarity(20)
                if the_person.outfit.cum_covered:
                    "With [the_person.title] still wearing your cum from her service earlier, you get a burst of energy and arousal."
                    $ mc.change_stats(arousal = builtins.min(30, mc.max_arousal - mc.arousal), energy = builtins.min(80, mc.max_energy - mc.energy))
                mc.name "Of course. Let's get started."
                if not (the_person.vagina_visible and person_choice.vagina_visible):
                    $ scene_manager.strip_to_vagina()
                call start_threesome(person_choice, the_person) from threesome_HR_meeting_happy_ending
                person_choice "Oh my... that was fun. Thanks for calling me in! I guess I'd better go get back to work..."
                $ scene_manager.update_actor(person_choice, position = "default", display_transform = character_left_flipped)
                "You both watch as [person_choice.fname] gets dressed."
                $ scene_manager.apply_outfit(person_choice)
                if the_person is sarah:
                    $ the_person.change_happiness(10)
            "That's all":
                person_choice "Thanks for calling me in... I guess I'd better go get back to work!"
    else:
        person_choice "Thanks for calling me in... I guess I'd better go get back to work!"

    if person_choice.opinion(opinion_chat) < max_opinion:
        $ person_choice.update_opinion_with_score(opinion_chat, max_opinion)
    $ mc.listener_system.fire_event("HR_opinion_improvement", the_person = person_choice)
    $ scene_manager.update_actor(person_choice, position = "walking_away", display_transform = character_left_flipped)
    $ scene_manager.update_actor(the_person, position = "stand2", display_transform = character_right)
    "[the_person.title] gets up and walks [person_choice.title] to the door."
    "They exchange a few pleasantries before [person_choice.title] leaves the room."
    $ scene_manager.remove_actor(person_choice)
    # remove actor first (without reset), so she continues the meeting as she was dressed before
    "[the_person.title] comes back to the desk and sits down."
    $ scene_manager.update_actor(the_person, position = "sitting")

    python:
        del person_choice
        del opinion_chat
    return True

label HR_director_review_discoveries_label(the_person):
    # shorten the dialogue when all research is reviewed
    if not (get_HR_director_tag("business_HR_serum_tier", 0) >= 3
        and (not the_person is sarah or get_HR_director_tag("business_HR_serum_breast", False))):

        "[the_person.title] pulls out a report on all the latest achievements of the research department."
        if get_HR_director_tag("business_HR_serum_tier", 0) == 0:
            if mc.business.is_trait_researched(off_label_drugs): #Researched!
                $ set_HR_director_tag("business_HR_serum_tier", 1)
                the_person "Hmmm... interesting."
                "[the_person.title] looks closely at one of the serums that has been researched."
                the_person "I see here that you've managed to create a serum that has the ability to increase a person's... suggestibility?"
                mc.name "Right. Basically it sets up the brain to make new connections it might not have previously made, opening up a person to suggestions they may not normally consider."
                the_person "That would actually be useful... We could use some, in the coffee we make when we bring them in for meetings?"
                mc.name "A version of the serum with a short useful life would be useful for giving the meetings more impact."
                "[the_person.title] looks into more details of the serum."
                the_person "Looks like the serum is fairly easy to produce. I'd say for about $500 we could probably set up something long term for the Monday meetings..."
                mc.name "Noted. I'll consider it and get back to you if I decide to do this."
                the_person "Sounds good [the_person.mc_title]!"

        if get_HR_director_tag("business_HR_serum_tier", 0) == 1:
            if mc.business.is_trait_researched(blood_brain_pen): #Researched!
                $ set_HR_director_tag("business_HR_serum_tier", 2)
                the_person "Hmmm... interesting."
                "[the_person.title] looks closely at one of the serums that has been researched."
                the_person "I see here that you've managed to improve on an earlier design to increase a person's suggestibility!"
                mc.name "Right. It bypasses connections that would normally trigger a rejection response and causes the person to consider actions that would normally be rejected."
                if get_HR_director_tag("business_HR_coffee_tier", 0) == 0:
                    the_person "I know I brought this up last time we researched a similar serum, but having a serum like that to give employees when they come in for reviews would be very useful."
                    the_person "You should definitely consider it. I think it would give our meetings more impact with employees."
                    the_person "This version of the serum... I think we could get something set up for about $1500. It's a little difficult to synthesize."
                    mc.name "Noted. I'll consider it and get back to you if I decide to do this."
                    the_person "Sounds good [the_person.mc_title]!"
                else:
                    the_person "We already have the equipment set up from the previously researched serum. We should be able to modify it to take advantage of this advancement."
                    "[the_person.title] checks her notes on the synthesis process."
                    the_person "I think for about $1500 we could probably set something similar up for this one. It would give our meetings considerably more impact."
                    mc.name "Noted. I'll consider it and get back to you if I decide to do this."
                    the_person "Sounds good [the_person.mc_title]!"

        if get_HR_director_tag("business_HR_serum_tier", 0) == 2:
            if mc.business.is_trait_researched(mind_control_agent): #Researched
                $ set_HR_director_tag("business_HR_serum_tier", 3)
                the_person "Wow... this is crazy."
                "[the_person.title] looks closely at one of the serums that has been researched."
                the_person "It says here, you have researched a serum that allows for temporary mind control!?!"
                mc.name "Right. It bypasses all inhibitions and allows direct implantation of suggestions."
                the_person "So... obviously the ethics of this are dubious but... You could do incredible things with it, from an HR standpoint."
                mc.name "Well, we've had to dilute it quite a bit. High concentrations can have pretty bad side effects."
                the_person "So... maybe we could consider creating a concentrated, single use version? With something like that, we could change a girl's work opinions all at once!"
                the_person "Looks like for about $5000 we could stock a single use version like that. It would be pretty challenging to synthesize."
                mc.name "Noted. I'll consider it and get back to you if I decide to do this."
                the_person "Sounds good [the_person.mc_title]!"


        if the_person is sarah:
            if get_HR_director_tag("business_HR_serum_breast", False)  == False:
                if mc.business.is_trait_researched(breast_enhancement): #Researched!
                    $ set_HR_director_tag("business_HR_serum_breast", True)
                    "Suddenly, [the_person.title] sits straight up in her chair as she reads the report."
                    the_person "Wait wait... you managed to synthesize a serum that can increase breast size?"
                    mc.name "Right. It works with the pancreas to deliver local growth of fatty tissue to the breasts."
                    the_person "That's amazing! And it says here it won't leave behind stretch marks?"
                    mc.name "Correct. We were able to combine the enhancement of fatty tissue with a temporary increase in skin elasticity."
                    the_person "That incredible... but I can't afford..."
                    "She furrows her brow when she sees the initial estimate for the cost of synthesis."
                    the_person "I mean uh, it'll be interesting to see how this progresses..."
                    "You notice [the_person.title] writing herself a note to visit the research department later."
                    $ add_sarah_catch_stealing_action()

        "You spend a few minutes with [the_person.title] going over the progress in the research department over the last week or so."

    # shorten the dialogue when all policies are reviewed
    if not (get_HR_director_tag("business_HR_uniform", False)
        and get_HR_director_tag("business_HR_skimpy_uniform", False)
        and get_HR_director_tag("business_HR_relative_recruitment", 0) != 0
        and get_HR_director_tag("business_HR_meeting_on_demand", False)
        and get_HR_director_tag("business_HR_gym_tier", 0) >= 2):

        the_person "Now let's take a look at policy changes from the last week."
        if not get_HR_director_tag("business_HR_uniform", False):
            if relaxed_uniform_policy.is_owned:
                the_person "Hmmm, I see here that we have recently opened up company policy to allow for uniform guidelines."
                the_person "This is something that could potentially alienate some of our employees. It might be a good idea if we include opinions on work uniforms when meeting one–on–one with them."
                "You hadn't considered how your employees would react when you instituted the uniform policy. You decide [the_person.possessive_title] is right."
                mc.name "That's a good idea. Go ahead and implement that going forward."
                the_person "Sure thing [the_person.mc_title]!"
                $ set_HR_director_tag("business_HR_uniform", True)
        elif not get_HR_director_tag("business_HR_skimpy_uniform", False):
            if corporate_enforced_nudity_policy.is_owned:
                if the_person.sluttiness > 40:  #She only volunteers to start doing this if she is slutty enough.
                    the_person "I see here that the uniform policy has recently been loosened further."
                    the_person "Personally, I think it is great that I can come to work and show off lots of skin, but with the latest change in uniform policy, it might be intimidating to employees who don't like skimpy uniforms."
                    the_person "It might be a good idea to include opinions on skimpy uniforms when meeting one–on–one with employees."
                    "You realise the swing in the uniform policy might be a bit much for some girls, so this is probably a good thing to start counselling for."
                    mc.name "That's a good idea. Go ahead and implement that going forward."
                    the_person "Sure thing [the_person.mc_title]!"
                    $ set_HR_director_tag("business_HR_skimpy_uniform", True)
                    if the_person is sarah:
                        the_person "Mmm, I can't wait to see what outfits some of the other girls will wear around the office..."
                        $ the_person.change_slut(2)
        if get_HR_director_tag("business_HR_relative_recruitment", 0) == 0:
            if (mc.business.max_employee_count - mc.business.employee_count) > 4:
                the_person "I see here that changes within the company have produced several vacancies."
                the_person "If you like, I could post something in the break room that we are looking for more employees."
                the_person "Several of the women who work here have children or relatives who could use the work. They might be more likely to come to you asking for employment if they know we need the help."
                "You consider what she is saying. It might be good for company morale to have mothers and their daughters both employed by you. Who knows, it could lead to other situations too."
                "You weigh the option. Do you want to post something?"
                menu:
                    "Approve":
                        mc.name "That's a good idea. Go ahead and implement that going forward."
                        $ set_HR_director_tag("business_HR_relative_recruitment", 2)
                    "Deny":
                        mc.name "I think for now I'd like to stick with more traditional recruiting methods."
                        $ set_HR_director_tag("business_HR_relative_recruitment", 1)

                the_person "Sure thing, [the_person.mc_title]. If you change your mind in the future, just let me know. I can always put the sign up or down based on what we need at the time."

        if not get_HR_director_tag("business_HR_meeting_on_demand", False):
            if mc.business.employee_count > 10:
                the_person "I see the business has grown. We now have a double-digit number of employees!"
                the_person "I was thinking, with the number of employees we have now, we could probably do our one–on–one meetings more often without losing their effectiveness."
                the_person "We still don't want to do it too often, but I was thinking we could have meetings as often as once a day?"
                "With your growing number of employees, it makes sense that you would be able to have meetings more often."
                mc.name "I'll keep that in mind going forward. If I want to have a meeting with an employee, I'll make sure to come find you first."
                the_person "Great! I think that will work out nicely."
                $ set_HR_director_tag("business_HR_meeting_on_demand", True)

        if HR_director_gym_membership_tier_1_requirement(the_person) and get_HR_director_tag("business_HR_gym_msg_tier", 0) == 0:
            $ set_HR_director_tag("business_HR_gym_msg_tier", 1)
            the_person "With our small, but growing employee group, I thought it might be worth looking into a company sponsored gym fitness program."
            the_person "I did some research, and it turns out there is a local one with a nice facility with great pricing for companies."
            mc.name "How much would it cost?"
            the_person "For the company I found, the pricing is $5 per person, per week."
            mc.name "That seems pretty reasonable actually. What benefits would it provide?"
            the_person "Well, having something like that available to employees would certainly help employees get more fit."
            the_person "It might take a while to see changes, but I would say girls would have more energy over all."
            mc.name "Okay, I'll consider it and get back to you on that."

        if HR_director_gym_membership_tier_2_requirement(the_person) and get_HR_director_tag("business_HR_gym_msg_tier", 0) == 1:
            $ set_HR_director_tag("business_HR_gym_msg_tier", 2)
            the_person "The company is getting bigger, and I was thinking about possible benefits to the company for increasing good health habits of the employees."
            the_person "There is a company that specialises in information campaigns on healthy eating habits, exercise, and good mental health."
            the_person "Combined with the company gym membership, I think we would see a sizeable benefit to the company as a whole."
            mc.name "How much would it cost?"
            the_person "For the company I found, the pricing is $10 per person, per week. This would be on top of the $5 per person for the company gym membership."
            mc.name "What would be the benefits we would see if we invest in this?"
            the_person "Well, generally it would increase the energy of employees as they develop healthier eating patterns."
            the_person "Additionally, I think employees with interests in sports and hiking would really appreciate the change. In fact, we could even encourage them to like sports during our one–on–one meetings."
            mc.name "Okay, I'll consider it and get back to you on that."

        "You finish up discussing the company policies."
    return

label HR_director_manage_gym_membership(the_person):
    if get_HR_director_tag("business_HR_gym_tier", 0) == 0:
        return

    the_person "Just to let you know, I wrote out the check this morning for this week's employee health program."
    if get_HR_director_tag("business_HR_gym_tier", 0) == 1:
        python:
            for x in mc.business.employee_list:
                if x.max_energy < 140:
                    x.change_max_energy(2 + x.opinion.sports, add_to_log = False)
                x.change_happiness(1 + x.opinion.sports + x.opinion.hiking, add_to_log = False)
            mc.business.change_funds(-(mc.business.employee_count * 5), stat = "Investments")
    elif get_HR_director_tag("business_HR_gym_tier", 0) == 2:
        python:
            for x in mc.business.employee_list:
                if x.max_energy < 180:
                    x.change_max_energy(2 + x.opinion.sports, add_to_log = False)
                x.change_happiness(1 + x.opinion.sports + x.opinion.hiking, add_to_log = False)
            mc.business.change_funds(-(mc.business.employee_count * 15), stat = "Investments")

    if erica.event_triggers_dict.get("yoga_sessions_started", False):
        the_person "I'm also going to write the check for the yoga class [erica.fname] is teaching tomorrow."
        $ mc.business.change_funds(-100, stat = "Salaries")
    return

label HR_director_coffee_tier_1_label(the_person):
    $ mc.business.change_funds(-500, stat = "Investments")
    mc.name "I've been thinking about your proposal to add serums to the coffee we serve to employees when we meet with them. I'm giving you approval to set it up."
    the_person "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person "I'll keep it in a locked cabinet and from now on I'll only use it when we give an employee coffee during our Monday meetings."
    mc.name "Sounds good."
    the_person "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_coffee_tier", 1)
    return

label HR_director_coffee_tier_2_label(the_person):
    $ mc.business.change_funds(-1500, stat = "Investments")
    mc.name "I've been thinking about your proposal to add the stronger serum to the coffee we serve to employees when we meet with them. I'm giving you approval to set it up."
    the_person "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person "I'll keep it in a locked cabinet and from now on I'll only use it when we give an employee coffee during our Monday meetings."
    mc.name "Sounds good."
    the_person "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_coffee_tier", 2)
    return

label HR_director_gym_membership_tier_1_label(the_person):
    mc.name "I've been thinking about your proposal to sponsor a company gym membership. I'm giving you approval to set it up."
    the_person "Sounds good sir! I'll have that set up and ready to begin next week."
    mc.name "Sounds good."
    the_person "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_gym_tier", 1)
    return

label HR_director_gym_membership_tier_2_label(the_person):
    mc.name "I've been thinking about your proposal to sponsor a company-wide health program. I'm giving you approval to set it up."
    the_person "Sounds good sir! I'll have that set up and ready to begin next week."
    mc.name "Sounds good."
    the_person "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_gym_tier", 2)
    return

label HR_director_change_relative_recruitment_label(the_person):
    if get_HR_director_tag("business_HR_relative_recruitment") == 2:
        the_person "I see, are you sure you want me to take down the sign in the break room that we are looking for more employees?"
        menu:
            "Take the Sign Down":
                the_person "OK, I'll take it down as soon as we are finished here. Is there anything else I can do for you?"
                $ set_HR_director_tag("business_HR_relative_recruitment", 1)
            "Leave the Sign Up":
                the_person "Oh... sorry I thought you said you wanted to change it. Is there anything else I can do for you?"
        return
    else:
        the_person "I see, are you sure you want me to put up the sign in the break room that we are looking for more employees?"
        menu:
            "Put the Sign Up":
                the_person "OK, I'll put it up as soon as we are finished here. Is there anything else I can do for you?"
                $ set_HR_director_tag("business_HR_relative_recruitment", 2)
            "Leave the Sign Down":
                the_person "Oh... sorry I thought you said you wanted to change it. Is there anything else I can do for you?"
        return

label HR_director_meeting_on_demand_label(the_person):
    $ scene_manager = Scene() # make sure we have an empty scene manager for on-demand meetings
    the_person "Okay, I think I have time for that! Let me grab my dossiers from Monday and I'll meet you in your office."
    $ mc.change_location(ceo_office)
    "You head to your office and [the_person.possessive_title] quickly arrives with her papers."
    $ scene_manager.add_actor(the_person, position = "sitting")
    the_person "Ok! Let me see who I have on my list here..."
    call HR_director_personnel_interview_label(the_person, max_opinion = get_HR_director_tag("business_HR_coffee_tier", 0)) from HR_DIR_INTERVIEW_CALL_4
    if _return:
        $ set_HR_director_tag("business_HR_meeting_last_day", day)
        the_person "I'd say that went pretty well! I'm going to head back to work, if that is okay with you, [the_person.mc_title]?"
    else:
        the_person "No problem, we can pick this up another time."

    "You thank her for her help and excuse her. She gets up and leaves you to get back to work."
    $ scene_manager.clear_scene()
    call advance_time() from hr_advance_time_one
    return

label HR_director_sexy_meeting_start_label(the_person):
    #Phases of this label.
    #   First we determine if we have any new acts of service our girl is willing to perform.
    #   If not, give the player the option to choice an unlocked act of service
    #   Next, perform the act
    #   Then, clean up, with higher sluttiness giving the player the option to have her not clean up.


    if not get_HR_director_unlock("blowjob"):  #This is the first time this function has been run
        the_person "So... I have no idea the best way to do this..."
        mc.name "Why don't you just come over here and give me a blowjob?"
        the_person "Okay! That should be fun!"
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "[the_person.possessive_title!c] comes around to your side of the desk and gets down on her knees. She pulls down your zipper and pulls your cock out."
        the_person "Mmm, it smells so good. Let's get this taken care of!"
        $ mc.change_locked_clarity(30)
        "She runs her tongue up and down your length a few times, then parts her lips and begins to suck you off."
        $ mc.change_arousal(40)
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_start_one
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            mc.name "Mmm, this is a great way to start Monday. This was a great idea [the_person.title]."
            $ scene_manager.update_actor(the_person, emotion = "happy")
            "[the_person.possessive_title!c] stops licking the cum off her lips for a second and smiles."
            the_person "Thank you sir! I am willing to do this next week again if you decide to."
        else:
            mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "Of course sir, I am willing to do this anytime you want me to."
        $ set_HR_director_unlock("blowjob", True)
        $ scene_manager.update_actor(the_person, position = "stand3")
        "She cleans herself up and makes herself presentable again."
        $ scene_manager.apply_outfit(the_person)
        return

    if not get_HR_director_unlock("titfuck"):
        if the_person is sarah and sarah_epic_tits_progress() > 1:
            the_person "So... I was thinking this week maybe I could do that thing again. You know, where I put your cock between my tits?"
            the_person "It felt soooo good last time. I've been thinking about it a lot."
            mc.name "That sounds great, I'll admit it, seeing my cock between your tits is hot."
            if the_person.tits_available:
                "With her tits already out and ready to be used, she just gives you a big smile."
            else:
                if the_person.outfit.can_half_off_to_tits():
                    "[the_person.possessive_title!c] moves her top out of the way."
                    $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
                else:
                    "[the_person.possessive_title!c] begins to take off her top."
                    $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_tit_strip_list(), half_off_instead = False)
                "With her tits out and ready to be used, she gives you a big smile."
            $ mc.change_arousal(20)
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
            $ mc.change_locked_clarity(30)
            "She gets on her knees and gives you a couple strokes with her hand."
            $ mc.change_arousal(20)
            the_person "Mmmm, I love the feeling of a cock buried between my big tits... this is gonna be great!"
            "With her hands on each side of her chest, she wraps her sizeable boobs around you and begins to bounce them up and down."
            call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_start_two
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0:
                "After you finish, [the_person.possessive_title] runs her hands along her tits, rubbing your cum into her skin."
                the_person "Mmm, god that was hot. Let me just enjoy this a minute before we move on with the meeting..."
                if the_person.is_bald:
                    "You run your hands over her shiny scalp for a bit while she enjoys the warmth of your cum on her skin."
                else:
                    "You run your hands through her hair for a bit while she enjoys the warmth of your cum on her skin."
            else:
                mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
                $ scene_manager.update_actor(the_person, emotion = "sad")
                the_person "Of course sir, I am willing to do this anytime you want me to."
            $ set_HR_director_unlock("titfuck", True)
            $ scene_manager.update_actor(the_person, position = "stand3")
            "Eventually she cleans herself up and makes herself presentable again."
            $ scene_manager.apply_outfit(the_person)
            return

    if Sarah_unlock_special_tit_fuck_requirement() and the_person == sarah:
        call Sarah_unlock_special_tit_fuck(the_person) from _new_sarah_titfuck_position
        return

    if not get_HR_director_unlock("missionary on desk"):
        if (the_person.sluttiness + the_person.opinion.vaginal_sex * 5) >= 60 and (the_person != sarah or sarah_get_sex_unlocked()):
            the_person "Hey... you know what would be really hot?"
            "You feel yourself raise your eyebrow in response. This should be good!"
            the_person "What if I just lay down on your desk and you have your way with me, right here in your office?"
            the_person "Having my boss pin me to his desk and ravage me..."
            $ mc.change_arousal(20)
            mc.name "I think that's a good idea. Why don't you get your ass over here and we'll find out for sure!"
            the_person "Oh! Yes sir!"
            "[the_person.possessive_title!c] gets on your desk and lies on her back."
            $ scene_manager.update_actor(the_person, position = "missionary", emotion = "happy")
            if the_person.vagina_visible:
                "She spreads her legs, her pussy on display in front of you."
            else:
                if the_person.outfit.can_half_off_to_vagina():
                    "You move [the_person.possessive_title]'s clothes out of the way."
                    $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
                else:
                    "You start to strip [the_person.possessive_title] down."
                    $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
                "Soon her pussy is on full display in front of you, on your desk."
            $ mc.change_locked_clarity(50)
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            "You have your cock out in a flash. You position it at her slick entrance."
            "You push yourself inside her nice and slow, since she hasn't had much time to warm up yet."
            the_person "Mmmm, [the_person.mc_title]. Use me boss! I'm here to serve you!"
            "You start to piston your cock in and out of her."
            call fuck_person(the_person, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_start_three
            "[the_person.possessive_title!c] lies on your desk, recovering."
            mc.name "You were right, [the_person.title]. It IS really hot to fuck you on my desk!"
            the_person "Ah, yes, I suspected it would be, sir!"
            "Eventually she cleans herself up and makes herself presentable again."
            $ scene_manager.update_actor(the_person, position = "stand3")
            $ scene_manager.apply_outfit(the_person)
            $ set_HR_director_unlock("missionary on desk", True)
            return

    if not get_HR_director_unlock("bent over desk"):
        if (the_person.sluttiness + the_person.opinion.doggy_style * 5) >= 70 and (the_person != sarah or sarah_get_sex_unlocked()):
            if the_person.obedience > 180:
                mc.name "Come here, I'm going to use you the way I see fit today."
                if the_person.is_submissive:
                    the_person "Oh! Yes sir!"
                    $ the_person.change_obedience(3)
                else:
                    the_person "Ok..."
                "You stand up as she walks around to your side of the desk. You roughly turn her around and bend her over your desk."
                $ scene_manager.update_actor(the_person, position="standing_doggy")
                $ mc.change_arousal(20)
                the_person "Oh my!"
                $ set_HR_director_unlock("bent over desk", True)

                if the_person.vagina_visible:
                    "She wiggles her hips back at you a bit. Her pussy lips glisten with a bit of moisture."
                else:
                    if the_person.outfit.can_half_off_to_vagina():
                        "You move [the_person.possessive_title]'s clothes out of the way."
                        $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
                    else:
                        "You start to strip [the_person.possessive_title] down."
                        $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
                    "Soon her ass is on full display in front of you, bent over your desk."
                $ mc.change_locked_clarity(50)
                $ the_person.break_taboo("condomless_sex")
                $ the_person.break_taboo("vaginal_sex")
                "You push yourself inside her nice and slow, since she hasn't had much time to warm up yet."
                the_person "Oh God! It's going so deep."
                "You give her ass a solid spank, then begin to fuck her roughly."
                call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_start_four
                $ the_report = _return
                if the_report.get("girl_orgasms",0)>0:
                    "[the_person.possessive_title!c] is still bent over your desk, recovering from her orgasm."
                    the_person "That's... yeah you can do that to me any time."
                else:
                    "[the_person.possessive_title!c] slowly recovers from using her body for your pleasure."
                    the_person "Mmm, happy to be of service, sir. We can do that again next time... if you want!"
                "Eventually she cleans herself up and makes herself presentable again."
                $ scene_manager.update_actor(the_person, position = "stand3")
                $ scene_manager.apply_outfit(the_person)
                return

    if not get_HR_director_unlock("anal lapdance"):
        if the_person is sarah and sarah.love >= 80 and sarah.sluttiness >= 60 and sarah.event_triggers_dict.get("stripclub_progress", 0) >= 1: #This is Sarah's 80 love event.
            if the_person.is_girlfriend:
                the_person "[the_person.mc_title]... you know I love you, right?"
                "Oh god, that is a very serious line to just throw out there."
                mc.name "Of course."
                the_person "Good."
            else:
                the_person "[the_person.mc_title]... you know I care about you, right?"
                mc.name "Of course."
                the_person "Good"
            $ the_person.draw_person(position = "stand3")
            "[the_person.possessive_title!c] stands up."
            mc.name "Is there something wrong?"
            the_person "No. You know, I love these Monday meetings. Do you know why?"
            $ scene_manager.strip_to_tits(person = the_person)
            $ mc.change_locked_clarity(30)
            "[the_person.title] starts taking some of her clothes off."
            mc.name "No, why?"
            the_person "It just feels like we are starting the week off right."
            "[the_person.title] bends over and keeps stripping."
            $ scene_manager.update_actor(the_person, position = "standing_doggy")
            $ scene_manager.strip_to_vagina(the_person)
            $ mc.change_locked_clarity(50)
            the_person "Especially when it starts with us messing around in your office!"
            "[the_person.possessive_title!c] gives her ass a little shake before standing back up."
            $ scene_manager.update_actor(the_person, position = "stand3")
            if the_person.has_taboo("anal_sex"):
                the_person "I kind of want to try something... we've never really done before..."
                mc.name "Oh?"
                if the_person.is_girlfriend:
                    the_person "I want to be a good girlfriend, who meets all your needs, no matter what they are."
                    the_person "So far you've claimed my mouth... and my pussy..."
                    the_person "I want you to claim me in one more hole... I think you know what I mean!"
                else:
                    the_person "I just want you to feel good, and I think I might like it as well, if you let me sit on your lap."
                    the_person "I wouldn't normally do this, but your cock is so amazing... I just have to know what it would feel like in my ass!"
                the_person "Don't worry, I want to do it for you. Just sit back in your chair and let me!"
            else:
                the_person "This morning, I just want to make you feel good, and judging by last time, I think it will make me feel good too."
                mc.name "Oh yeah? What do you have in mind?"
                the_person "Why don't you just sit back in your chair and find out?"
            mc.name "Sounds good, do your thing."
            $ scene_manager.update_actor(the_person, position = "back_peek")
            "[the_person.possessive_title!c] turns away from you, her ass now right at eye level. She pulls her cheeks apart slightly, giving you an amazing view of her puckered hole."
            $ mc.change_locked_clarity(50)
            "She brings up one hand to her mouth and spits in it, then runs it back along her crack, giving you a show as she lubes up her ass a bit. You pull your cock out and give it a couple strokes."
            $ scene_manager.update_actor(the_person, position = "standing_doggy")
            "[the_person.title] bends over your desk, reaching for her purse she left on the far side. She wiggles her hips a bit as she pulls some lube out of her purse."
            the_person "Would you mind?"
            "[the_person.possessive_title!c] hands you the lube. You squirt a generous amount onto your fingers and work them around her sphincter and then slowly push a finger inside her."
            $ the_person.change_arousal (20)
            the_person "Ahhhhh..."
            $ mc.change_locked_clarity(50)
            "Her hips push back against you a bit as you work your finger in and out of her a bit, getting her good and lubed up. She moans at the penetration."
            the_person "Ok, let's do this."
            $ scene_manager.update_actor(the_person, position = "sitting")
            "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
            "[the_person.possessive_title!c] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
            $ the_person.break_taboo("anal_sex")
            the_person "Oh god! It's in!"
            call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = anal_on_lap, skip_intro = True, allow_continue = False) from _call_get_fucked_sarah_gives_anal_lapdance_monday_01
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0:
                "[the_person.possessive_title!c] stands up. Some of your cum has managed to escape, running down her leg."
            else:
                mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
                the_person "Of course..."
                "[the_person.possessive_title!c] stands up."
            $ scene_manager.update_actor(the_person, position = "stand3")
            $ scene_manager.apply_outfit(the_person)
            $ set_HR_director_unlock("anal lapdance", True)
            "You make a mental note that from now on you can ask your HR director for some anal on Mondays."
            return

    if not get_HR_director_unlock("breeding fetish session"):
        if the_person.has_breeding_fetish and the_person.is_highly_fertile:
            the_person "So, I know this is usually about you, and making sure your needs are met before the start of the week..."
            mc.name "... but?"
            the_person "But... I swear to god I feel like I'm in heat right now. It is all I can do to keep myself from jumping you every time I see you in the hall!"
            the_person "I know this is out of line... but would you mind? It's a good time for it too..."
            mc.name "Hmmm, I don't know..."
            the_person "Please? I'm not sure I can concentrate on my work until you give me a big virile load!"
            mc.name "Okay. Get over here and bend over."
            the_person "Yes!"
            $ scene_manager.update_actor(the_person, position = "standing_doggy")
            $ mc.change_locked_clarity(50)
            "[the_person.title] turns around. You quickly get her ready to fuck."
            $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
            call fuck_person(the_person, start_position = bent_over_breeding, private = True) from _call_hr_breeding_01
            if the_person.has_creampie_cum:
                the_person "Oh fuck... every time you finish inside me is just so good..."
                "She rubs her belly and sighs."
            "When you finish, [the_person.possessive_title] cleans herself up a bit."
            $ scene_manager.update_actor(the_person, position = "stand3")
            $ scene_manager.apply_outfit(the_person)
            the_person "Mmm, that was nice..."
            $ set_HR_director_unlock("breeding fetish session", True)
            return


    if not get_HR_director_unlock("anal fetish session"):
        #TODO: Write anal fetish session for HR director
        if the_person.has_anal_fetish:
            pass

    if not get_HR_director_unlock("cum fetish session"):
        #TODO: Write cum fetish session for HR director
        if the_person.has_cum_fetish:
            pass

    the_person "Okay! How do you want me to take care of you this week, [the_person.mc_title]?"

    $ the_position = HR_director_choose_position()
    if the_position == "any":
        the_person "Mmmm, I can do that!"
        $ mc.change_arousal(20)
        $ the_person.change_stats(happiness = 5, obedience = 3)
        $ the_position = get_HR_director_random_unlock_key()

    if the_position == "blowjob":
        the_person "Get your cock out, I want to taste it!"
        "[the_person.possessive_title!c] stands up and starts to walk around the desk while you pull out your erection."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "She gets down on her knees in front of you and takes a moment to admire your hardness."
        $ mc.change_locked_clarity(30)
        "She opens her mouth and runs her tongue along it a few times, and then parts her lips and begins to suck you off."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_mid_one

    elif the_position == "titfuck":
        if not the_person.tits_available:
            if the_person.outfit.can_half_off_to_tits():
                "[the_person.possessive_title!c] moves her top out of the way."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
            else:
                "[the_person.possessive_title!c] begins to take off her top."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_tit_strip_list(), half_off_instead = False)
            "With her tits out and ready to be used, she gives you a big smile."
        the_person "Get your cock out, I want to feel it slide between my boobs!"
        $ mc.change_locked_clarity(30)
        "You pull your cock out as she gets up and walks around your desk. She drops down on her knees in front of you."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "[the_person.possessive_title!c] smiles at you as she uses her hands to wrap her tits around your cock, and then starts to move them up and down."
        if the_person == sarah and sarah_get_special_titfuck_unlocked():
            call fuck_person(the_person, start_position = sarah_tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_special_titfuck_1
        else:
            call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_mid_two

    elif the_position == "missionary on desk":
        if not the_person.vagina_visible:
            if the_person.outfit.can_half_off_to_vagina():
                "[the_person.possessive_title!c] moves her clothes out of the way."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
            else:
                "[the_person.possessive_title!c] begins to take off her clothes."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
            "When she finishes getting naked, she gives you a big smile."
        the_person "Oh my, fucking me on your desk? You are so naughty, [the_person.mc_title]!"
        $ scene_manager.update_actor(the_person, position = "missionary")
        mc.name "Oh, I'm the naughty one? I seem to remember this was your idea in the first place..."
        "You pull your cock out and line it up with [the_person.title]'s pussy. You ease yourself inside her with one slow, smooth push."
        $ mc.change_locked_clarity(50)
        $ the_person.break_taboo("condomless_sex")
        $ the_person.break_taboo("vaginal_sex")
        the_person "I never said I wasn't naughty too... Oh god, [the_person.mc_title], that feels good. Have your way with me!"
        call fuck_person(the_person, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_mid_three

    elif the_position == "bent over desk":
        mc.name "Get over here, I'm going to bend you over my desk again."
        if the_person.is_submissive:
            the_person "Oh! Yes sir!"
            $ the_person.change_obedience(2)
        else:
            the_person "OK."
        "You stand up as she walks around to your side of the desk. You roughly pull her closer and give her ass a tight squeeze."
        $ scene_manager.update_actor(the_person, position="stand3")
        the_person "Oh my!"

        if the_person.vagina_visible:
            "You give her pussy a little rub and show her your fingers glistening with a bit of moisture. You quickly turn her around and bend her over your desk."
        else:
            if the_person.outfit.can_half_off_to_vagina():
                "You move [the_person.possessive_title]'s clothes out of the way."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
            else:
                "You start to strip [the_person.possessive_title] down."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
            "As soon as her pussy is on full display in front of you, you bend her over your desk, exposing her round ass."
        $ scene_manager.update_actor(the_person, position="standing_doggy")

        "You don't waste any time. You pull your cock out and point it at her slit. You pull her hips back as you push inside her with one smooth push."
        the_person "Mmm, fuck me good [the_person.mc_title]!"
        $ mc.change_locked_clarity(50)
        $ the_person.break_taboo("condomless_sex")
        $ the_person.break_taboo("vaginal_sex")
        "You eagerly begin to pump your hips and fuck your HR director over your desk."
        call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_meeting_mid_four

    elif the_position == "anal lapdance":
        the_person "Oh god, you want your HR director's ass, do you? What a naughty CEO!"
        $ the_person.change_arousal(20)
        if not the_person.vagina_visible:
            if the_person.outfit.can_half_off_to_vagina():
                "[the_person.possessive_title!c] moves her clothes out of the way."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
            else:
                "[the_person.possessive_title!c] begins to take off her clothes."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
            "When she finishes getting naked, she gives you a big smile."
        $ scene_manager.update_actor(the_person, position = "back_peek")
        the_person "In here was it? Where you wanted to stick that incredible dick you've got?"
        "[the_person.possessive_title!c] spreads her cheeks, revealing her puckered hole."
        $ mc.change_locked_clarity(50)
        mc.name "You know it."
        the_person "Hmm... I'm not sure it'll go in easily..."
        $ scene_manager.update_actor(the_person, position = "standing_doggy")
        "She bends over your desk and grabs her purse, looking through it."
        "Her ass is on full display for you, so you make sure to give it a couple of spanks and a firm grope."
        "[the_person.title] hands back to you a bottle of lube she pulled from her bag."
        the_person "Here, can you lube me up?"
        mc.name "With pleasure."
        "You squirt a generous amount onto [the_person.title]'s ass. You work it all along her crack and then push a finger inside."
        $ the_person.change_arousal (20)
        the_person "Ahhhhh..."
        $ mc.change_locked_clarity(50)
        "It isn't long until you've got two fingers working her backdoor good."
        the_person "Ok, let's do this."
        $ scene_manager.update_actor(the_person, position = "sitting")
        "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
        "[the_person.possessive_title!c] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
        $ the_person.break_taboo("anal_sex")
        the_person "Oh god! It's in!"
        call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = anal_on_lap, skip_intro = True, allow_continue = False) from _call_get_fucked_sarah_gives_anal_lapdance_monday_02
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "[the_person.possessive_title!c] stands up. Some of your cum has managed to escape, running down her leg."
        else:
            mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
            the_person "Of course..."
            "[the_person.possessive_title!c] stands up."
        $ scene_manager.update_actor(the_person, position = "stand3")

    elif the_position == "breeding fetish session":
        mc.name "Get over here, I'm going to bend you over my desk and creampie you."
        the_person "Fuck I love Mondays. Let's do it!"
        $ scene_manager.update_actor(the_person, position = "standing_doggy")
        $ mc.change_locked_clarity(50)
        "[the_person.title] turns around. You quickly get her ready to fuck."
        $ the_person.strip_to_vagina(prefer_half_off = True, position = "standing_doggy")
        call fuck_person(the_person, start_position = bent_over_breeding, private = True) from _call_hr_breeding_02
        if the_person.has_creampie_cum:
            the_person "Oh fuck... every time you finish inside me is just so good..."
            "She rubs her belly and sighs."
        the_person "Mmm, that was nice..."
        $ scene_manager.update_actor(the_person, position = "stand3")

    elif the_position == "anal fetish session":
        pass

    elif the_position == "cum fetish session":
        pass


    if the_person.has_cum_fetish or the_person.has_exhibition_fetish:
        the_person "Alright, I'm ready to continue the meeting."
        "[the_person.title] doesn't appear to be concerned with her appearance whatsoever."
    elif ((the_person.obedience - 100) + the_person.sluttiness) > 100: #If she is either very obedient, slutty, or a mixture
        menu:
            "Tell her to stay like that for the meeting":
                mc.name "I'm very busy, let's just continue the meeting. Don't bother to clean up."
                "[the_person.title] opens her mouth for a second, ready to protest, but quickly reconsiders."
                the_person "Of course, [the_person.mc_title]. Let's see what is next."
                $ mc.change_locked_clarity(20)
            "Let her clean herself up":
                "[the_person.possessive_title!c] quickly cleans herself up, ready to continue the meeting."
                $ scene_manager.apply_outfit(the_person)
    else:
        "She quickly starts to get dressed to continue your meeting."
        $ scene_manager.apply_outfit(the_person)

    $ scene_manager.update_actor(the_person, position = "sitting")
    return

label HR_director_mind_control_label(the_person):
    $ mc.business.change_funds(-5000, stat = "Investments")
    mc.name "I've been thinking about your proposal to create a specialised serum for mind control attempts. I would like to move forward with it."
    the_person "Sounds good sir! I'll head over to research and have them synthesize me some."
    the_person "I'll make sure it stays locked away, and only you and I will have a key to get some out."
    mc.name "Sounds good."
    the_person "Did you need anything else, [the_person.mc_title]?"
    $ set_HR_director_tag("business_HR_serum_tier", 4)
    return

label HR_director_mind_control_attempt_label(the_person):
    $ scene_manager = Scene()
    $ HR_employee_list = build_HR_mc_list(the_person)
    if builtins.len(HR_employee_list) == 0: #No one qualifies!
        the_person "Actually, things are running really smoothly right now, I'm not sure that would be beneficial."
        return

    the_person "Okay... remember this act has a chance of backfiring, having all kinds of unknown side effects. Are you sure you want to continue?"
    "Note: The chance of the session backfiring is directly related to your mastery level of the Mind Control serum effect!"
    $ ran_num = calculate_backfire_odds()
    "Current odds of backfiring are: [ran_num]%%. Successful mind control will increase all current trainable opinions by 1 tier. Are you sure you want to attempt?"
    menu:
        "Yes":
            pass
        "No":
            return
    the_person "Okay. Who do you want me to make the attempt on?"

    call screen main_choice_display(build_menu_items([["Call in"] + HR_employee_list], draw_hearts_for_people = False))
    if isinstance(_return, Person):
        the_person "Okay. I'll go get her and we can meet up in your office."
        $ clear_scene()
        $ mc.change_location(ceo_office)
        call HR_mind_control_attempt(_return, the_person) from HR_mind_control_attempt_call_1

        $ scene_manager.clear_scene()
        $ set_HR_director_tag("business_HR_meeting_last_day", day)
    call advance_time() from hr_advance_time_two
    return True

label HR_mind_control_attempt(the_person, the_HR_dir):
    "[the_HR_dir.title] returns with [the_person.title]."
    $ scene_manager.add_actor(the_HR_dir)
    $ scene_manager.add_actor(the_person, display_transform = character_left_flipped)
    the_person "You wanted to see me sir?"
    mc.name "Ah, yes, thank you for coming. [the_person.title], we are trying a new experimental counselling method, that we are combining with one of our recent serum developments."
    mc.name "I've asked you to come, because I would like you to help us test it. [the_HR_dir.title] here is going to administer the session."
    "She looks a bit concerned when you tell her what you want her to do."
    if the_person.obedience > 180:
        "When she looks into your eyes though, you can see her hesitation vanish. Her obedience to you melts away her objections."
    else:
        the_person "I don't know sir... are you sure this is safe?"
        menu:
            "(Lie) It is perfectly safe" if mc.charisma > 4:
                pass
            "There are risks involved":
                the_person "I'm not sure I want to do that. Why should I agree to something like this?"
                menu:
                    "I'll reward you sexually" if the_person.sluttiness > 60:
                        "Her face lights up at the prospect of having some alone time with you."
                        #TODO code it so it happens
                    "It would mean a lot to me" if the_person.love > 60:
                        "Her face softens when you appeal to her emotionally."
                    "I'll reward you financially ($1000)":
                        the_person "Oh... well I suppose I could really use the extra pay."
                        $ mc.business.change_funds(-1000, stat = "Investments")
                    "I'll fire you if you don't":
                        $ scene_manager.update_actor(the_person, emotion = "angry")
                        the_person "What!?! You're kidding me? I can't afford to lose this job right now!"
                        if the_person.happiness > 90:
                            $the_person.change_happiness(70 - the_person.happiness)
                        else:
                            $the_person.change_happiness(-35)

    the_person "Okay... I'll do it. Let's get this over with!"
    the_HR_dir "Alright. Come with me, and we will get the process started."
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.remove_actor(the_HR_dir)
    "The two girls get up and leave to go to a quiet room where [the_HR_dir.title] makes the mind control attempt."
    "You return to your work while the attempt is made."
    "..."
    "......"
    $ is_backfire = False
    if calculate_backfire_odds() > renpy.random.randint(0,100): #FAIL
        $ backfire_string = mind_control_backfire(the_person)
        "The mind control event has backfired!"
        #TODO add backfire string to event log
        $ is_backfire = True
    else:
        $ hr_director_mind_control_update_opinions(the_person)

    $ scene_manager.add_actor(the_HR_dir)
    "[the_HR_dir.title] eventually returns."
    mc.name "Welcome back. How did it go?"
    if is_backfire:
        the_HR_dir "Unfortunately, the attempt backfired. I'm not sure yet what the effects were, but they certainly weren't the desired ones."
        mc.name "That is... unfortunate."
        the_HR_dir "She is resting for now. It would probably be best to leave her to rest, but if you want you can go and see her."
    else:
        the_HR_dir "I believe the attempt was successful. I have no indication that she experienced any side effects."
        mc.name "Excellent. Good work [the_HR_dir.title]."
        the_HR_dir "She is resting for now, but before I left she asked to see you. It's up to you if you want to go see her."
    mc.name "Thank you. I'll consider it. That'll be all for now."
    $ scene_manager.remove_actor(the_HR_dir)
    "[the_HR_dir.title] leaves."
    #TODO the rest of this encounter. Go see her, pay her with sexual favours, etc.
    return

label HR_director_appointment_action_label():
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list([x for x in mc.business.hr_team if x.available], "Appoint", "Back")]
        ))
    $ person_choice = _return

    if person_choice != "Back":
        call HR_director_initial_hire_label(person_choice) from _call_HR_director_initial_hire_label_appointment
        $ del person_choice
    return

label HR_director_headhunt_initiate_label(the_person):
    mc.name "I'd like to initiate a search for a specific job opening."
    the_person "Ah! Okay, just fill out this form with your requirements."

    $ reset_headhunter_criteria()
    $ hide_ui()
    call screen HR_director_recruitment_screen(the_person)
    $ show_ui()
    if _return:
        python:
            days_to_find = 1
            if get_HR_director_tag("recruit_obedience", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_focused", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_marital", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_slut", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_kids", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_height", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_body", None) is not None:
                days_to_find += 1
            if get_HR_director_tag("recruit_bust", None) is not None:
                days_to_find += 1

        $ days_to_find = min(days_to_find, 7)   #Cap days to find to 7

        the_person "Okay, I'll go ahead and start the search."
        if days_to_find <= 2:
            the_person "This shouldn't take me long. Hopefully just a day or two!"
        elif days_to_find <= 5:
            the_person "Alright, this is fairly specific, so give me a few days to see what I can find and I'll get back to you."
        else:
            the_person "This is... pretty specific. It'll probably take me at least a week to find someone who meets all these criteria!"
        mc.name "Thank you. Let me know when you have found someone and we'll do the interview."

        $ set_HR_director_tag("recruit_day", day + days_to_find)
        $ set_HR_director_tag("business_HR_headhunter_progress", 1)

        $ add_hr_director_headhunt_interview_action(the_person)
        the_person "Is there anything else you need?"
    else:
        mc.name "I've changed my mind."
        the_person "No problem, just let me know if you want me to start recruiting someone."
    return

label HR_director_headhunt_interview_label(the_person):
    $ prospect = generate_HR_recruit()
    $ scene_manager = Scene()
    $ set_HR_director_tag("business_HR_headhunter_progress", 2)
    if not mc.is_at(ceo_office):
        "You are hard at work when you get a message from your HR supervisor."
        the_person "Hey, I got a hit on criteria you had for a prospective employee. Want me to send you the info?"
        if mc.business.at_employee_limit:  #We accidentally filled all available slots
            mc.name "Actually, I accidentally filled that position already. Sorry, I must have forgotten to tell you."
            "A few minutes later, she responds to you."
            the_person "Ah... OK, well try to let me know next time, okay?"
            "You promise to do so."
            return
        mc.name "Sure, meet me in my office."
        $ mc.change_location(ceo_office)
        the_person "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        mc.name "Hi [the_person.title], come in and take a seat."
    else:
        $ mc.location.show_background()
        the_person "Hello [the_person.mc_title]!"
        $ scene_manager.add_actor(the_person)
        "Your HR Director appears in the doorway to your office."
        the_person "Hey, I got a hit on criteria you had for a prospective employee. I think you are going to like this."
        if mc.business.at_employee_limit:  #We accidentally filled all available slots
            mc.name "Actually, I accidentally filled that position already. Sorry, I must have forgotten to tell you."
            the_person "You... ahh, okay. Try to remember to let me know next okay?"
            "You promise to do so."
            return
    $ scene_manager.update_actor(the_person, position = "sitting")

    the_person "Take a look at this file, she would be perfect for us."

    call hire_select_process([prospect, 1]) from _call_hire_prospect_process_1  #Copying how Vren calls this... hopefully this is right...

    $ scene_manager.draw_scene()
    if _return == prospect: #MC chooses to hire her
        mc.name "Alright [the_person.title], this looks promising. Good work finding her."
        $ the_person.change_stats(happiness = 5, obedience = 3)
        the_person "Alright! I'll give her the news."
        $ prospect.generate_home().add_person(prospect) # create home and add her to the game
        call hire_someone(prospect) from _call_hire_HR_prospect_1

        $ hire_day = "tomorrow"
        if day%7 == 4 or day%7 == 5: #If it's Friday or Saturday, don't start tomorrow
            $ hire_day = "Monday"

        "With all arrangements made, [prospect.fname] will start [hire_day]."
        $ prospect.set_title()
        $ prospect.set_possessive_title()
        $ prospect.set_mc_title()
        the_person "Give me the rest of the week to catch up on my normal HR work. If you want me to start the process again, talk to me on Monday."
    else:
        mc.name "I'm sorry, this wasn't exactly what I had in mind."
        the_person "Ah, okay. Well give me the rest of the week to catch up on my normal HR work. If you want me to start the process again, talk to me on Monday."
        $ prospect.remove_person_from_game()

    $ del prospect
    return


#Headhunter unlocks and requirements:
#Initial unlock: recruitment_batch_two_policy.is_owned  second screening pool size increase ###
#obedience unlock: recruitment_obedience_improvement_policy.is_owned ###
#slutty unlock: recruitment_slut_improvement_policy.is_owned ###
#Married / unmarried unlock: recruitment_knowledge_two_policy.is_owned  ###
#Has kids unlock: recruitment_knowledge_three_policy.is_owned
#focused production unlock: recruitment_batch_three_policy.is_owned ###
#Big / small tits unlock: recruitment_knowledge_four_policy.is_owned

label HR_director_monday_headhunt_update_label(the_person):
    if get_HR_director_tag("business_HR_headhunter_progress", 0) == 0:
        the_person "Looks like I'm not currently running any target searches. Let me know if you want me to initiate one."
    elif get_HR_director_tag("business_HR_headhunter_progress", 0) == 1:
        the_person "I'm still working on the current search. Give me a few more days to finish it up."
    else:
        the_person "I should have the time now to initiate another search. If you want me to start another talent search let me know!"
        $ set_HR_director_tag("business_HR_headhunter_progress", 0)

    # all updates researched (quick exit)
    if get_HR_director_tag("headhunter_kids", False) and get_HR_director_tag("headhunter_slut", False) and get_HR_director_tag("headhunter_focused", False) and get_HR_director_tag("headhunter_obedience", False):
        return

    the_person "Let's see if any recent recruiting policy updates will change how we look for employees."
    $ hr_recruit_updates = 0
    if not get_HR_director_tag("headhunter_obedience", False) and recruitment_obedience_improvement_policy.is_owned:
        the_person "I can now target a new employee based on their free will! I can either scout for an obedient, or free spirited prospect."
        $ set_HR_director_tag("headhunter_obedience", True)
        $ hr_recruit_updates += 1
    if not get_HR_director_tag("headhunter_focused", False) and recruitment_batch_three_policy.is_owned:
        the_person "I can now target highly specialised prospects. They will be more skilled in an area, but may not be well-rounded individuals."
        $ set_HR_director_tag("headhunter_focused", True)
        $ hr_recruit_updates += 1
    if not get_HR_director_tag("headhunter_physical", False) and recruitment_knowledge_one_policy.is_owned:
        the_person "With the new software update, I can now search by a variety of physical preferences. Busty? Short? Thick? I can make it happen!"
        $ set_HR_director_tag("headhunter_physical", True)
        $ hr_recruit_updates += 1
    if not get_HR_director_tag("headhunter_marital", False) and recruitment_knowledge_two_policy.is_owned:
        the_person "I can now target married or single individuals. It might be illegal in most states, but not here!"
        $ set_HR_director_tag("headhunter_marital", True)
        $ hr_recruit_updates += 1
    if not get_HR_director_tag("headhunter_slut", False) and recruitment_slut_improvement_policy.is_owned:
        the_person "I can now narrow down prospects based on general promiscuity. Want a prude or a slut? I can do that."
        $ set_HR_director_tag("headhunter_slut", True)
        $ hr_recruit_updates += 1
    if not get_HR_director_tag("headhunter_kids", False) and recruitment_knowledge_three_policy.is_owned:
        the_person "I can now pick prospects based on whether or not they have kids. More MILFs around here? I could handle that!"
        $ set_HR_director_tag("headhunter_kids", True)
        $ hr_recruit_updates += 1
    if hr_recruit_updates == 0:
        "Looks like I don't have any additions to the prospecting system this week."
    return

label HR_start_internship_program_label(the_person):
    "You decide to visit your HR director to talk to her about starting up the internship program."
    $ the_person.draw_person()
    mc.name "Hey, can we talk in my office real quick?"
    the_person "Sure, no problem."
    $ mc.change_location(ceo_office)
    $ the_person.draw_person(position = "sitting")
    mc.name "I've decided to partner up with the local university. I'm starting a STEM internship program for women to help get them work experience and a scholarship toward their studies."
    the_person "That's... wow! Okay. How can I help?"
    mc.name "I've partnered with a former professor of mine at the university, who will help me decide who to award the internships to."
    the_person "Okay..."
    mc.name "For now, I'm only hiring for Production and Research, since it is a STEM focused scholarship."
    the_person "So... what do you need from me?"
    mc.name "Mainly just introduce them to our employees, handle the NDA, explain some of the company policies, stuff like that."
    the_person "That's not a problem, I can do that."
    the_person "Just remember that serum testing requirements, office duties, etc. None of those will apply to them."
    the_person "Although they need to comply with the company dress code, since this might include protective gear."
    mc.name "That's fine."
    the_person "They also generally won't quit, but their productivity will probably hinge on how much they enjoy working here."
    the_person "In addition, if things go badly, or if you can't behave yourself, I'm sure they'll make my life hell with HR paperwork and complaints..."
    mc.name "I'll be on my best behaviour."
    the_person "Okay... can we start small at least?"
    mc.name "I haven't made any selections yet, but as soon as we find a suitable candidate, I'll let you know."
    the_person "Let's keep it to three people per department. If things go as expected, we can expand it more."
    mc.name "That's a good idea."
    the_person "Alright. I'll make up a basic intern onboarding paperwork packet that you can give them."
    the_person "I hope I don't regret this..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] gets up and says goodbye, leaving your office."
    $ clear_scene()
    $ unlock_recruit_new_college_interns()
    "You can now hire college interns! Talk to [nora.title] at the university to hire more. They cost $15,000 and will work on weekends and some weekdays for their final semester."
    # TODO: add efficiency penalty and work completion
    # "If the intern is happy working here, they can be hired on full time after graduation."
    # "Unhappy interns will hurt company efficiency while working. They will also refuse an employment offer after graduating."
    return
