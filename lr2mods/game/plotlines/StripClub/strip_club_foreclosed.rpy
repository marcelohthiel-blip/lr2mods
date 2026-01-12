## Stripclub storyline Mod by Corrado
#  You find the stripclub foreclosed.
#   foreclosed_stage = 1 Talk with Starbuck
#   foreclosed_stage = 2 Think about buying
#   foreclosed_stage = 3 Buy the club
#   foreclosed_stage = 4 Stripclub: bought - select old strippers
#   foreclosed_stage = 5 Stripclub: foreclosed finished
#   foreclosed_stage = -1 Stripclub new other owner

init 2 python:
    def init_strip_club_mod(action_mod):
        return

    def get_strip_club_foreclosed_last_action_day():
        return mc.business.event_triggers_dict.get("foreclosed_last_action_day", 0)

    def strip_club_foreclosed_event_requirement():
        if time_of_day >= 3:
            return False # Don't trigger foreclosed event while strip club is open
        if get_strip_club_foreclosed_stage() != 0:
            return False
        if mc.business.event_triggers_dict.get("strip_club_foreclosed_countdown", False):
            return False
        if sarah_epic_tits_progress() == 1: # don't start while Sarah epic tits event in progress
            return False
        if cousin.event_triggers_dict.get("blackmail_level", -1) == 1:
            return False
        if not cousin.has_job(stripper_job):
            return False
        if mc.business.has_funds(60000):
            return cousin.event_triggers_dict.get("seen_cousin_stripping", False)
        return False

    def cousin_talk_about_strip_club_requirement(person):
        return not person.is_home

    def starbuck_talk_about_strip_club_requirement(person):
        if get_strip_club_foreclosed_stage() == 1:
            if day > get_strip_club_foreclosed_last_action_day() + 2:
                if starbuck in sex_store.people:
                    return True
        return False

    def strip_club_foreclosed_countdown_requirement(start_day):
        if time_of_day >= 3:
            return False # Don't trigger foreclosed event while strip club is open
        if sarah_epic_tits_progress() == 1: # don't start while Sarah epic tits event in progress
            return False
        if cousin.event_triggers_dict.get("blackmail_level", -1) == 1:
            return False
        if day > start_day:
            return True
        return False

    def strip_club_foreclosed_change_stripper_schedules():
        for person in [x for x in mc.business.stripclub_strippers]:
            person.set_override_schedule(person.home, day_slots = [0, 1, 2, 3, 4, 5, 6], time_slots = [3, 4])
        return

    def add_cousin_talk_about_strip_club_action():
        cousin_talk_about_strip_club_action = Action("Cousin talk about strip club", cousin_talk_about_strip_club_requirement, "cousin_talk_about_strip_club_label")
        cousin.add_unique_on_room_enter_event(cousin_talk_about_strip_club_action)
        return

    def add_starbuck_talk_about_strip_club_action():
        starbuck_talk_about_strip_club_action = Action("Starbuck talk about strip club", starbuck_talk_about_strip_club_requirement, "starbuck_talk_about_strip_club_label")
        starbuck.add_unique_on_room_enter_event(starbuck_talk_about_strip_club_action)
        return

    def add_start_strip_club_foreclosed_countdown_action():
        strip_club_closes_down_action = Action("Strip Club closes down", strip_club_foreclosed_countdown_requirement, "strip_club_closes_down_label", requirement_args = day + renpy.random.randint(10, 16))
        mc.business.add_mandatory_crisis(strip_club_closes_down_action)
        return

    strip_club_foreclosed_mod_action = ActionMod("Strip Club Story Line", strip_club_foreclosed_event_requirement, "club_foreclosed_event_label",
        menu_tooltip = "At a certain point the strip club is closed and you get the chance to buy it.", category = "Misc",
        initialization = init_strip_club_mod, is_mandatory_crisis = True)

label club_foreclosed_event_label():
    # delay the actual shutdown for 10 to 16 days after initial requirements are met.
    $ add_start_strip_club_foreclosed_countdown_action()
    $ mc.business.event_triggers_dict["strip_club_foreclosed_countdown"] = True
    return

label strip_club_closes_down_label():
    python:
        strip_club.old_owner = strip_club.owner
        strip_club.old_name = strip_club.formal_name
        mc.business.event_triggers_dict["foreclosed_day"] = day
        strip_club.owner = "Foreclosed"
        strip_club.formal_name = "Foreclosed"
        strip_club.background_name = "Club_Outside_Background"
        strip_club_foreclosed_change_stripper_schedules()
        add_cousin_talk_about_strip_club_action()
        mc.business.remove_mandatory_crisis("club_foreclosed_event_label")
        update_party_schedules()
        strip_club.visible = True   # make sure the strip club is on the map

    "While reading a newspaper you find out that your favourite Strip Club is no longer in business."
    "Perhaps you should talk to your cousin [cousin.fname] about it, when your aunt cannot overhear your conversation."
    return

label cousin_talk_about_strip_club_label(the_person):
    $ the_person.draw_person(emotion = "sad")
    the_person "Oh, [mc.name]... Just the last person I wanted to see right now!"
    mc.name "Hello, [the_person.title]... What's with the long face?"
    the_person "I think I just lost my job, the Club has been foreclosed and nobody knows if and when it would be open again..."
    mc.name "Any idea about what happened?"
    the_person "I don't know for sure, but I heard some rumours about a lot of unpaid taxes..."
    mc.name "The business was in that much trouble?"
    the_person "Actually the business was running very well, but looks like [strip_club.old_owner], the boss there, just disappeared a few days ago with all the Club's money..."
    the_person "That fucking asshole didn't even pay me nor the other girls for our last week."
    "She looks at you and suddenly shifts her demeanour."
    $ the_person.draw_person(emotion = "happy", position = "stand2")
    the_person "Oh, speaking about money, can you lend me 300 bucks?"
    the_person "I could do a special performance just for you, you know..."
    menu:
        "Accept":
            mc.name "Ok, follow me..."
            "You and [the_person.title] walks to the nearest hotel."
            $ amount = 300
            $ the_person.change_stats(happiness = 10, obedience = -3, love = 2)
            call club_foreclosed_strip_label(the_person) from _call_cousin_talk_about_strip_club_label_1
        "Refuse":
            mc.name "Actually I wanted to relax and have some fun tonight, but spending time with you and your poisoned tongue isn't exactly my idea of 'fun'..."
            mc.name "Bye, [the_person.title]... See you next time !"
            $ the_person.change_stats(happiness = -5, obedience = 2, love = -2)
            $ the_person.draw_person(position = "walking_away")
            "Hit and sunk by your behaviour, [the_person.title] leaves you alone."
        "Mock":
            mc.name "Can you explain {i}why{/i} I need to spend $300 on you stripping when there's plenty of other girls around willing to do far more for less money?"
            the_person "So you are a pervert, and stingy too ? Ok [mc.name], just for you I'll do it for $200..."
            $ the_person.change_stats(happiness = -3, obedience = 1, love = -1)
            menu:
                "Accept":
                    mc.name "Perhaps I should say no..."
                    the_person "Come on, take me to a nice hotel and I'll show you a good time."
                    mc.name "Alright, let's go."
                    "You and [the_person.title] walks to the nearest hotel."
                    $ amount = 200
                    $ the_person.change_stats(happiness = 5, obedience = -1, love = 1)
                    call club_foreclosed_strip_label(the_person) from _call_cousin_talk_about_strip_club_label_2
                "Refuse":
                    mc.name "Actually I wanted to relax and have some fun tonight, but spending time with you and your poisoned tongue isn't exactly my idea of 'fun'..."
                    mc.name "Bye, [the_person.title]... See you next time !"
                    $ the_person.change_stats(happiness = -5, obedience = 2, love = -2)
                    $ the_person.draw_person(position = "walking_away")
                    "Taken aback by your behaviour, [the_person.title] turns around and sulks away, leaving you alone."

    $ set_strip_club_foreclosed_stage(1)
    $ add_starbuck_talk_about_strip_club_action()
    $ clear_scene()
    return

label club_foreclosed_strip_label(the_person):
    $ mc.change_location(downtown_hotel)
    "You walk up to the reception and hire a hotel room for one night. You and [the_person.title] go up to your room."
    $ mc.business.change_funds(-80)
    $ mc.change_location(downtown_hotel_room)
    mc.name "Ok, here's your money, now let's get this show started."
    $ mc.business.change_funds(-amount, stat = "Strippers")
    "[the_person.possessive_title!c] quickly disappears into the bathroom to change her clothes."
    $ the_person.apply_outfit(mc.business.stripper_wardrobe.pick_random_outfit())
    $ the_person.draw_person(emotion = "default", position = "stand4")
    the_person "You're in luck I really need the money, otherwise I would never do this for you."
    menu:
        "Give up":
            "On second though, you decide to stop her."
            mc.name "Enough! I know how desperate for money you are, [the_person.title]."
            $ the_person.draw_person(emotion = "sad", position = "stand4")
            "She thinks she just lost her opportunity to gain some cash and looks disheartened..."
            mc.name "Despite your usual attitude, I'll let you keep the money I gave you and I'll add $100 more... because, believe it or not, family matters to me."
            $ mc.business.change_funds(-100, stat = "Strippers")
            "When you give her another $100, you can see the puzzled look on her face, she can't believe what's happening..."
            $ the_person.draw_person(emotion = "happy", position = "stand4")
            the_person "Really? I never got cash this easily!"
            the_person "Ok, you're a pervert, but I admit you're a generous pervert!"
            $ the_person.change_stats(happiness = 5, obedience = -1, love = 2)
            $ clear_scene()
            "It looks like [the_person.title] is her usual obnoxious self again... a moment later she's back in the bathroom changing her clothes."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(emotion = "happy", position = "stand4")
            "When she's back, she moves right up to you."
            $ the_person.draw_person(emotion = "happy", position = "kissing")
            the_person "I still don't like you, but I think you deserve at least a kiss!"
            "She leans forward and gives you a soft kiss on your lips."
            if the_person.has_taboo("kiss"):
                $ the_person.break_taboo("kiss")
                $ the_person.change_arousal(15)
            else:
                $ the_person.change_arousal(10)
            $ the_person.draw_person(position = "walking_away")
            "Happily [the_person.title] turns around leaving the room, closing the door behind her."
            $ clear_scene()

        "Let's start":
            mc.name "Enough chit-chat, [the_person.title]—less talking and more stripping!"
            $ the_person.draw_person(position = "back_peek")
            "[the_person.title] turns on some sexy music on her phone and looks at you unsure about how far she should let the show go."
            if the_person.effective_sluttiness() < 30:
                "[the_person.title] stop moving and start to look at the floor."
                the_person "Do you really want me to strip for you ?"
                $ the_person.draw_person(emotion = "sad", position = "stand4")
                the_person "I need the money and I would do it for anybody else, but you're my cousin, we're related..."
                the_person "I'm sorry [the_person.mc_title], I can't do it..."
                mc.name "What if I give you $100 more than what we agreed?"
                $ the_person.draw_person(emotion = "default", position = "stand4")
                $ mc.business.change_funds(-100, stat = "Strippers")
                $ the_person.add_situational_slut("desperate", 10, "She is desperate for cash.")

            "You hand over the cash and [the_person.title] stares at you for a moment, sighs and slowly start to dance for you."

            call strip_tease(the_person, for_pay = True, skip_intro = True) from _call_strip_tease_cousin_club_foreclosed_strip

            $ the_person.clear_situational_slut("desperate")
            $ the_person.review_outfit()
            "When she's done, you leave the room into the hotel lobby."

    $ mc.change_location(downtown_hotel) # restore hotel background
    $ the_item = None
    $ clear_scene()
    return
