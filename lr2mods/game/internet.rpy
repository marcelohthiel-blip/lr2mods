# Contains all of the events for the egirl role. Most of these are events triggered from the PC's room and take place entirely online

init -2 python:
    global list_of_additional_phone_dates
    list_of_additional_phone_dates = []
    def check_insta_requirement():
        return True

    def check_dikdok_requirement():
        return True

    def check_onlyfans_requirement():
        return True

    def show_story_progress_requirement():
        return True

    def show_mc_schedule_requirement():
        return True

    def ask_location_requirement(person):
        return True

    def text_chat_requirement(person):
        if person.event_triggers_dict.get("chatted", 0) <= 0:
            return "Enough chatting"
        if mc.energy < 15:
            return "Not enough energy"
        return True

    def text_flirt_requirement(person):
        if person.event_triggers_dict.get("flirted", 0) <= 0:
            return "Enough flirting"
        if mc.energy < 15:
            return "Not enough energy"
        return True

    def get_date_text_plan_actions(person):
        lunch_date_action = Action("Ask her out to lunch", lunch_date_requirement, "lunch_date_text_plan_label",
            menu_tooltip = "Take her out on casual date out to lunch. Gives you the opportunity to impress her and further improve your relationship.")
        movie_date_action = Action("Ask her out to the movies", movie_date_requirement, "movie_date_text_plan_label",
            menu_tooltip = "Plan a more serious date to the movies. Another step to improving your relationship, and who knows what you might get up to in the dark!")
        dinner_date_action = Action("Ask her out to a romantic dinner", dinner_date_requirement, "dinner_date_text_plan_label",
            menu_tooltip = "Plan a romantic, expensive dinner with her. Impress her and you might find yourself in a more intimate setting.")
        bar_date_action = Action("Ask her out to the local bar for drinks", bar_date_requirement, "bar_date_text_plan_label",
            menu_tooltip = "Plan a casual date at the local bar. Intoxicating beverages mean anything could happen")
    
    #IF you add new dates, make sure to update phone requests in game/internet.rpy!!! <3

        date_list = [[lunch_date_action, person], [movie_date_action, person], [dinner_date_action, person], [bar_date_action, person]]
        for extra_date in list_of_additional_phone_dates:
            date_list.append((extra_date, person))

        date_list.insert(0, "Select Date")
        date_list.append(("Never mind", None))
        return date_list

    # def text_date_requirement(person):
    #     if time_of_day in [0, 1, 4]:
    #         return "No dates at this time"
    #     if time_of_day == 2:
    #         return lunch_date_requirement(person)
    #     if time_of_day == 3:
    #         return bar_date_requirement(person) #Use bar date requirement since it has the lowest love requirement
    #     return False



init -1 python:
    texting_actions = ActionList() #List of actions that are displayed when you select a person to text
    ask_location_action = Action("Ask where she is", ask_location_requirement, "ask_location_label")
    text_chat_action = Action("Chat with her\n{menu_red}Costs: {energy=15}{/menu_red}", text_chat_requirement, "text_chat_label")
    text_flirt_action = Action("Flirt with her\n{menu_red}Costs: {energy=15}{/menu_red}", text_flirt_requirement, "text_flirt_label")
    text_ask_on_date_action = Action("Ask her on a date{image=gui/heart/Time_Advance.png}", date_option_requirement, "text_date_label")

    texting_actions.append(ask_location_action)
    texting_actions.append(text_chat_action)
    texting_actions.append(text_flirt_action)
    texting_actions.append(text_ask_on_date_action)


    def build_phone_menu():
        text_actions = ["Text Someone"]
        internet_actions = ["Check the Internet"]
        other_actions = ["Other Actions"]

        for a_person in mc.phone.get_person_list():
            text_actions.append(a_person)

        check_insta_action = Action("Check InstaPic", check_insta_requirement, "check_insta")
        check_dikdok_action = Action("Check Dikdok", check_dikdok_requirement, "check_dikdok")
        check_onlyfans_action = Action("Check OnlyFanatics", check_onlyfans_requirement, "check_onlyfans")

        internet_actions.append(check_insta_action)
        internet_actions.append(check_dikdok_action)
        internet_actions.append(check_onlyfans_action)

        show_story_progress_action = Action("Show Story Progress", show_story_progress_requirement, "show_story_progress_label")
        show_mc_schedule_action = Action("View Schedule", show_mc_schedule_requirement, "show_mc_schedule_label")
        other_actions.append(show_story_progress_action)
        other_actions.append(show_mc_schedule_action)
        other_actions.append("Back")

        return [text_actions, internet_actions, other_actions]

    def build_text_menu(person):
        text_actions = []
        for act in texting_actions:
            text_actions.append((act, person))

        for act in person.current_job_internet_actions:
            text_actions.append((act, person))

        for act in person.current_duty_internet_actions:
            if keep_talking or act.is_fast:
                text_actions_display_list.append((act, person))

        text_actions.sort(key = sort_display_list, reverse = True)
        text_actions.insert(0, f"Text {person.title}")

        other_actions = ["Other Actions"]
        other_actions.append("Back")

        return [text_actions, other_actions]

# Use this screen any time you want to display a phone based text log. the "newest" parameters can be used to force something to the bottom with the History log might not have been updated (Used in the say statement).
label browse_internet(is_phone = True): #TODO: Maybe make this a generic function you can use at any time to call people, make it a "use phone" type of thing.
    # The phone thing should be a location based default option, kind of like "Go somewhere else". It makes it easier to gate events (ie. no triggering events inside events) and tell where the player is.
    # We may want some static options that can be brought up at any time.
    # TODO: We absolutely want the player to be able to save pictures to their phone and set them as a background. That sounds great.
    #TODO: Provide a bunch of internet browsing options. Later on this leads to "OnlyFanatics" and "InstaPic", but it might start out with just some porn (or a comment about how "normal porn just seems boring now")
label .continue_browsing():
    call screen main_choice_display(build_menu_items(build_phone_menu(), draw_hearts_for_people = False, show_location = mc.business.event_triggers_dict.get("gps_tracker_enabled", False), draw_person_previews = False))

    $ clear_scene()
    if _return == "Back":
        return
    elif isinstance(_return, Action):
        $ the_action = _return
        $ the_action.call_action()
        if _return == "Skip Phone":
            return
        else:
            jump browse_internet.continue_browsing

    elif isinstance(_return, Person):
        $ the_person = _return

        call phone_texting(the_person) from _call_phone_texting_browse_internet

        if _return:
            jump browse_internet.continue_browsing
    else:
        pass #It was an action, we've taken care of it already.
    return

label phone_texting(the_person):
    $ return_to_phone = True

label .continue_texting():
    call screen main_choice_display(build_menu_items(build_text_menu(the_person)))

    if _return == "Back":
        return True

    elif isinstance(_return, Action):
        $ the_action = _return
        $ the_action.call_action(the_person)
        $ return_to_phone = _return

    if not return_to_phone:
        return False
    jump phone_texting.continue_texting

label ask_location_label(the_person):
    $ mc.start_text_convo(the_person)

    mc.name "Hey, where are you right now?"

    if the_person.has_event_day("location_ask_day") and the_person.get_event_day("location_ask_day") == day:
        if the_person.love < 0:
            the_person "Fuck off !!"

        if the_person.event_triggers_dict.get("location_ask_time") == time_of_day:
            the_person "Seriously? I just told you..."
        else:
            the_person "Are you stalking me? I'm not letting you track me all day long."

        $ the_person.set_event_day("location_ask_day")
        $ the_person.event_triggers_dict["location_ask_time"] = time_of_day

        $ mc.end_text_convo()
        return True

    if the_person.love < 0:
        the_person "Why would I tell you that?"

        $ the_person.set_event_day("location_ask_day")
        $ the_person.event_triggers_dict["location_ask_time"] = time_of_day
        $ mc.end_text_convo()
        return True

    if the_person.is_at(mc.location): #She's in the same location as you.
        $ mc.end_text_convo()
        $ the_person.draw_person()
        "[the_person.possessive_title!c] glances at her phone when it buzzes. She looks up at you and shakes her head."
        $ mc.end_text_convo()

        the_person "I'm right here, silly. What's up?"
        call talk_person(the_person) from _call_talk_person_26
        return False

    if the_person.is_home:
        the_person "I'm at home right now."
    else:
        the_person "You can find me at [the_person.location.formal_name!i] right now."

    $ the_person.set_event_day("location_ask_day")
    $ the_person.event_triggers_dict["location_ask_time"] = time_of_day

    $ mc.end_text_convo()
    return True

label text_chat_label(the_person):
    $ mc.start_text_convo(the_person)
    if mc.is_at(the_person.location): #She's in the same location as you.
        mc.name "Hey, how's it going [the_person.title]?"
        $ mc.end_text_convo()
        $ the_person.draw_person()
        "[the_person.possessive_title!c] glances at her phone when it buzzes. She looks up at you and shakes her head."
        $ mc.end_text_convo()

        the_person "I'm right here [the_person.mc_title]. We can just chat if you'd like."
        call small_talk_person(the_person) from _call_small_talk_person_1
        return False

    call small_talk_person(the_person, is_phone = True) from _call_small_talk_person_2
    $ mc.end_text_convo()
    return True

label text_flirt_label(the_person, apply_energy_cost = True, skip_intro = True):
    $ mc.start_text_convo(the_person)
    if mc.is_at(the_person.location) and not skip_intro: #She's in the same location as you.
        mc.name "Hey, [the_person.title]. What are you up to right now?"
        $ mc.end_text_convo()
        $ the_person.draw_person()
        "[the_person.possessive_title!c] glances at her phone when it buzzes. She looks up at you and shakes her head."
        $ mc.end_text_convo()

        the_person "I'm right here [the_person.mc_title], let's just talk."
        call flirt_person(the_person) from _call_flirt_person
        return False

    if (apply_energy_cost):
        $ mc.change_energy(-15)

    $ the_person.event_triggers_dict["flirted"] = the_person.event_triggers_dict.get("flirted", 0) - 1
    $ the_person.call_dialogue("flirt_response_text")
    menu:
        "Be romantic":
            "You text back and forth with [the_person.title], being kind and romantic."
            the_person "I've got to run, but this was nice [the_person.mc_title]. Talk to you later!"
            $ the_person.change_stats(happiness = 2, love = 1, max_love = 25)
            #$ the_person.call_dialogue("text_flirt_romantic") #TODO: Write personality specific dialogue for this

        "Be dirty":
            "You text back and forth with [the_person.title], being as flirty as you think you can get away with."
            if the_person.effective_sluttiness() < 20:
                "She doesn't seem very interested, unfortunately."
                the_person "I've got to go, sorry. Talk some other time, okay?"
            else:
                $ the_person.change_slut(1, 30)
                the_person "Hahah, you're so funny [the_person.mc_title]."
                the_person "I've got to run. Talk to you later, okay?"
            mc.name "Alright, talk to you later."
            #$ the_person.call_dialogue("text_flirt_dirty") #TODO: Write personality specific stuff

        "Ask for nudes":
            mc.name "Hey, I'm feeling bored and lonely. Send me something to cheer me up."
            if the_person.is_affair:
                "There's a pause, then she texts you back."
                the_person "For you, anything."
                python:
                    the_person.outfit.strip_to_underwear()
                    the_person.outfit.strip_to_tits()
                    the_person.draw_person(position = "kneeling1", emotion = "happy")
                $ mc.change_locked_clarity(15)
                "Another pause, then she sends you a picture."
                the_person "Wish you were here so we could really have some fun."
                mc.name "We'll have some fun soon, I promise."

                $ the_person.draw_person(position = "back_peek")
                "She sends you another pic."
                $ the_person.change_slut(1, 60)
                the_person "Don't make me wait too long!"
            elif the_person.is_girlfriend:
                if the_person.effective_sluttiness() >= 30:
                    the_person "You're so bad for me! One second..."
                    python:
                        the_person.outfit.strip_to_underwear()
                        the_person.outfit.strip_to_tits()
                        the_person.draw_person(position = "kneeling1", emotion = "happy")
                    $ mc.change_locked_clarity(15)
                    "Another pause, then she sends you a picture."
                    the_person "Come and see me so we can have some real fun!"
                    $ the_person.change_slut(1, 60)
                    mc.name "I'll see you soon, I promise."

                else:
                    the_person "Feeling a little frisky? Well, let's see what I can do..."
                    "There's a pause, then she sends you a picture."
                    python:
                        the_person.outfit.strip_to_underwear()
                        the_person.draw_person(emotion = "happy")
                    $ mc.change_locked_clarity(10)
                    $ the_person.change_slut(1, 40)
                    the_person "You'll have to convince me in person to show you any more. Hope that cures your \"boredom\"."
            elif the_person.is_family:
                if the_person.effective_sluttiness() >= 60:
                    the_person "I really shouldn't do this, but..."
                    "There's a pause, then she sends you a picture."
                    python:
                        the_person.outfit.strip_to_underwear()
                        the_person.outfit.strip_to_tits()
                        the_person.draw_person(position = "kneeling1", emotion = "happy")
                    $ mc.change_locked_clarity(15)
                    the_person "How's that?"
                    $ the_person.change_slut(1, 65)
                    mc.name "You're looking great [the_person.title], that's just what I wanted."

                elif the_person.effective_sluttiness() >= 40:
                    the_person "I really shouldn't do this, but I know you'll like it..."
                    "There's a pause, then she sends you a picture."
                    python:
                        the_person.outfit.strip_to_underwear()
                        the_person.draw_person(emotion = "happy")

                    $ mc.change_locked_clarity(10)
                    $ the_person.change_slut(1, 55)
                    the_person "There, I hope that helps. Don't show it to anyone else!"

                else:
                    the_person "What do you want me to send?"
                    mc.name "You know, a picture of yourself. Show me something fun."
                    "There's a long pause."
                    the_person "Come on [the_person.mc_title], don't be silly. Talk to you later!"

            else:
                if the_person.effective_sluttiness() >= 50:
                    the_person "I really shouldn't do this, but..."
                    python:
                        the_person.outfit.strip_to_underwear()
                        the_person.outfit.strip_to_tits()
                        the_person.draw_person(position = "kneeling1", emotion = "happy")
                    $ mc.change_locked_clarity(15)
                    "There's a pause, then she sends you a picture."
                    $ the_person.change_slut(1, 55)
                    the_person "It's kind of fun doing this! Enjoy ;)"

                elif the_person.effective_sluttiness() >= 30:
                    the_person "I shouldn't, but I guess a little fun wouldn't hurt."
                    the_person "One sec, I need to find some good light."
                    python:
                        the_person.outfit.strip_to_underwear()
                        the_person.draw_person(emotion = "happy")
                    $ mc.change_locked_clarity(10)
                    "There's a pause, then she sends you a picture."
                    $ the_person.change_slut(1, 35)
                    the_person "I'm so embarrassed! I hope you like it!"

                else:
                    "There's a long pause before [the_person.possessive_title] responds."
                    the_person "I'm not sure what you mean [the_person.mc_title]. I need to go, we can talk later okay?"

            $ the_person.apply_planned_outfit()    # restore her outfit
            # $ the_person.call_dialogue("text_flirt_nudes") #TODO: Personality specific responses
            $ clear_scene()

            # "Send a dick pic.": #TODO: Implement this, girls might respond by sending you nudes.
            #     if mc.location.person_count > 0:
            #         "You find a quiet spot where nobody will spot you taking a picture of your dick."
            #     "You rub your cock until it begins to swell and harden. When you're standing hard and impressive you snap a picture with your phone."
            #     mc.name "Take a look at this. Like what you see?"
            #     "You text her the picture."
            #     $ the_person.call_dialogue("text_flirt_dick_pic")
    $ mc.end_text_convo()
    return True

label text_date_label(the_person):
    $ mc.start_text_convo(the_person)
    if mc.is_at(the_person.location): #She's in the same location as you.
        mc.name "Hey, [the_person.title]. Want to go out sometime?"
        $ mc.end_text_convo()
        $ the_person.draw_person()
        "[the_person.possessive_title!c] glances at her phone when it buzzes. She looks up at you and shakes her head."
        $ mc.end_text_convo()

        the_person "I'm right here [the_person.mc_title], let's just talk."
        call date_person(the_person) from _call_date_person_from_text_01
        return False
    mc.name "Hey, [the_person.title]. Want to go out sometime?"
    the_person "Maybe, what did you have in mind?"

    call screen main_choice_display(build_menu_items([get_date_text_plan_actions(the_person)]))
    if isinstance(_return, Action):
        $ _return.call_action(the_person) #This is where you're asked to plan out the date, or whatever.
    else:
        mc.name "Sorry, I forgot I had something else going on."
        the_person "Okay..."
   
    $ mc.end_text_convo()
    return True


label lunch_date_text_plan_label(the_person):
    if get_named_label("lunch_date_text_plan_label", the_person):
        $ run_named_label("lunch_date_text_plan_label", the_person)
        return
    if the_person == kaya and day%7 in [5, 6]:
        mc.name "I was thinking about getting some lunch. Do you have a lunch break?"
        the_person "Sorry, I work a short shift, so I don't get a lunch break."
        mc.name "Okay, I'll try to swing by later."
        return

    # Take her out to lunch, raises love to a max of 50 if you pick the correct chat options
    if the_person.has_role(sister_role):
        mc.name "I was thinking about getting some lunch, do you want to come with me and hang out?"
        the_person "Hey, that sounds nice! You're always out of the house, I wish we got to spend more time together like we did when we were younger."

    elif the_person.has_role(mother_role):
        mc.name "I'm going to go out for lunch. You've been busy lately, would you like to take a break and join me?"
        the_person "Aww, it's so sweet that you still want to spend time with your mother. I'd love to!"

    elif the_person.has_role(aunt_role):
        mc.name "Would you like to come and have lunch with me? I haven't seen you much since I was a kid, I'm sure we have a lot to catch up on."
        the_person "It has been a long time, hasn't it. Lunch sounds wonderful!"

    elif the_person.has_role(cousin_role):
        mc.name "I'm going to get some lunch, would you like to come along with me?"
        the_person "You want me to be seen in public with you? You're really pushing it [the_person.mc_title], but sure."

    elif the_person.is_affair:
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me?"
        the_person "That sounds nice, [the_person.mc_title]."
        "After a minute, she texts you again."
        the_person "Are you sure my husband won't find out?"
        if the_person == christina:
            mc.name "You could always say you had to go over something, with [emily.fname]'s tutor."
            the_person "You are right. Let's do it!"
        else:
            mc.name "Can't you go and grab lunch with an acquaintance?"
            the_person "Of course I can, let's do it!"

    elif the_person.has_significant_other and the_person.opinion.cheating_on_men < 0: #IF she likes cheating she doesn't even mention she's in a relationship
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me? Maybe just grab a coffee and hang out for a while?"
        the_person "That sounds nice, [the_person.mc_title]."
        the_person "Just so we're on the same page, this is just as friends, right? I have a [the_person.so_title], I don't want to get anything confused here."
        mc.name "Of course! I just want to hang out and talk, that's all."
        the_person "Okay, let's do it!"

    else:
        mc.name "Would you like to go get a coffee, maybe a little lunch, and just chat for a while? I feel like I want to get to know you better."
        the_person "That sounds nice, I think I'd like to get to know you better too."
        # the_person "If you're ready to go right now I suppose I am too. Let's go!"
    call date_schedule_selection(the_person, 2) from _date_schedule_afternoon_lunch_on_phone_01
    if _return:
        $ create_lunch_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label movie_date_text_plan_label(the_person):
    if get_named_label("movie_date_text_plan_label", the_person):
        $ run_named_label("movie_date_text_plan_label", the_person)
        return
    if the_person.has_role(sister_role):
        mc.name "Hey, I was wondering if you'd like to see a movie with me sometime? You know, spend a little more time together as brother-sister."
        the_person "Sure thing [the_person.mc_title], a movie sounds fun!"

    elif the_person.has_role(mother_role):
        mc.name "Hey [the_person.title], would you like to come to the movies with me? I want to spend some more time together, mother and son."
        the_person "Aww, of course [the_person.mc_title]. I would love to go to the movies with you."
        the_person "Remember how you and I used to watch movies together every weekend? I felt like our relationship was so close because of that."

    elif the_person.has_role(aunt_role):
        mc.name "[the_person.title], would you like to come see a movie with me? I think it would just be nice to spend some more time together."
        the_person "You know, I haven't been out much since I left my ex, so a movie sounds like a real good time."

    elif the_person.has_role(cousin_role):
        mc.name "Hey, do you want to come see a movie with me and spend some time together?"
        the_person "Fine, but no telling people we're related, okay? I don't want anyone to think I might be a dweeb like you. ;)"

    elif the_person.has_significant_other:
        mc.name "So [the_person.title], I was thinking about going to see a movie sometime."
        mc.name "It would give us a chance to spend time together."
        if the_person.opinion.cheating_on_men > 0:
            the_person "I can do that, just don't tell my [the_person.so_title], okay? He might not like me hanging around with a hot guy like you."
            mc.name "My lips are sealed."
            if the_person.effective_sluttiness() >= 60:
                the_person "Treat me right and mine might not be. He's been working late so much lately, how does that sound?"
            else:
                the_person "He's been working late so much lately, I can go anytime really."

        else:
            the_person "Oh, a movie sounds fun! But..."
            mc.name "Is there something wrong?"
            the_person "I just don't know what my [the_person.so_title] would think. He might be a little jealous of you, you know?"
            mc.name "You don't have to tell him that I'll be there, if you don't want to. There's no reason you couldn't go out by yourself if you wanted to."
            the_person "You're right, of course. He's been working late so much lately. Let's do it!"

    else:
        mc.name "So [the_person.title], I was wondering if you'd like to come see a movie with me some time this week."
        mc.name "It would give us a chance to spend some time together and get to know each other better."
        the_person "Oh, a movie sounds fun! Let's do it!"

    call date_schedule_selection(the_person, 3) from _date_schedule_evening_movie_on_phone_01
    if _return:
        $ create_movie_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label dinner_date_text_plan_label(the_person):
    if get_named_label("dinner_date_text_plan_label", the_person):
        $ run_named_label("dinner_date_text_plan_label", the_person)
        return
    if the_person.has_role(sister_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together. Some brother sister bonding time."
        the_person "That sounds great [the_person.mc_title]. Let's do it."

    elif the_person.has_role(mother_role):
        mc.name "Mom, I was wondering if I could take you out to dinner, just the two of us. I'd enjoy some mother son bonding time."
        the_person "Aww, that's so sweet. I'm always happy to be taken out by you."

    elif the_person.has_role(aunt_role):
        mc.name "[the_person.title], would you like to go out on a dinner date with me? I think it would be a nice treat for you."
        the_person "That sounds like it would be amazing. It's been tough, just me and [cousin.fname]. I don't get out much any more."

    elif the_person.has_role(cousin_role):
        mc.name "Hey, I want to take you out to dinner."
        the_person "Is this you buying me dinner first? What happens after?"
        the_person "Just kidding. Okay, but no telling anyone we're related."

    elif the_person.has_significant_other:
        mc.name "[the_person.title], I'd love to spend some time together, just the two of us. Would you let me take you out for dinner?"
        the_person "[the_person.mc_title], you know I've got a [the_person.so_title], right? Well..."
        if the_person.opinion.cheating_on_men > 0:
            the_person "He won't know about it, right? What he doesn't know can't hurt him."
        else:
            "There is a long pause in the conversation."
            the_person "Just this once, and we have to make sure my [the_person.so_title] never finds out."

    else:
        mc.name "[the_person.title], I'd love to get to know you better. Would you let me take you out for dinner?"
        the_person "That sounds delightful [the_person.mc_title]."

    call date_schedule_selection(the_person, 3) from _date_schedule_evening_dinner_on_phone_01
    if _return:
        $ create_dinner_date_action(the_person, _return)
        the_person "Sounds good, I'll see you then!"
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
    return

label bar_date_text_plan_label(the_person):
    if get_named_label("bar_date_text_plan_label", the_person):
        $ run_named_label("bar_date_text_plan_label", the_person)
        return
    mc.name "Hey, I was thinking about hitting up the bar and getting a few drinks tonight. You want to join me?"
    the_person "Oh, I suppose I would be up for that. Where at?"
    call date_schedule_selection(the_person, 4) from _date_schedule_night_bar_on_phone_01
    if _return:
        "You give her the location of the bar downtown, and you agree to meet there at the specified time."
        the_person "Sounds great!"
        "You give her the location of the bar downtown, and you agree to meet there at the specified time."
        $ create_bar_date_action(the_person, _return)
    else:
        mc.name "I'll have to get back to you, my schedule is actually kind of full."
        the_person "Alright, just let me know!"
        return
    
    return

label show_story_progress_label():
    show screen story_progress(lily)
    return

label show_mc_schedule_label():
    show screen mc_appointment_schedule()
    return

label view_twatch(the_person): #TODO: Implement this as a role at some point
    # TODO: Watch a girl stream, different outcomes based on different games.
    # TODO: Much more likely to spawn on introverts, basically inverted from Insta or DikDok.
    # TODO In all cases if she's slutty she's doing things like teasing the camera.
    # TODO: She'll pimp her justfanatics if she has one
    # TODO: Otherwise you'll just end up throwing a bunch of money at her without any results.
    return
