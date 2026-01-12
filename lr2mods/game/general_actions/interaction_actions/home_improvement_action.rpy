#
# Home Improvement  MOD:
# Plan:
# MC realises his bedroom is pretty shabby and gets an option to renovate when he gets enough cash on hand to do so. (Action button in Bedroom)
# Mom later comment that he shouldn't stop there, the house could use additional improvements
# Renovate Sis bedroom
# Renovate Mom's bedroom
# Build Dungeon - Dungeon makes more sense in the context of multiple renovations on the house. Can even work in Mom's permission to do whatever he likes.
# Depends on dungeon code in: dungeon_room_actions.rpy
# Possible future improvements:
# Renovate Living room
# Renovate Exterior
# Jacuzzi baths for bedrooms (still leaves main shower for encounters)
# Guest rooms/servants quarters?
init 3 python:
    mc_bedroom_renovation_cost = 3000 # Currently used for all bedrooms, this could be varied.

    def is_home_improvement_in_progress():
        finish_day = mc.business.get_event_day("home_improvement_day")
        return day <= finish_day + 1

    def format_home_improvement_completion_message():
        days_left = mc.business.get_event_day("home_improvement_day") - day + 1
        if days_left > 0:
            return f"Wait for current project completion\n({days_left} {('days' if days_left > 1 else 'day')})"
        return "Wait for day after completion call (event)"

    def mc_bedroom_renovate_requirement():
        if bedroom.background_name == "Generic_Bedroom3_Background":
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(mc_bedroom_renovation_cost):
            return True
        return False

    def home_improvement_unlocked_requirement(trigger_day): # Currently ignoring trigger_day
        return bedroom.background_name == "Generic_Bedroom3_Background"

    def lily_bedroom_renovate_requirement():
        if lily_bedroom.background_name == "Lily_Bedroom_Background":
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(mc_bedroom_renovation_cost):
            return True
        return f"Requires: ${mc_bedroom_renovation_cost:,.0f}"

    def mom_bedroom_renovate_requirement():
        if mom_bedroom.background_name == "Generic_Bedroom1_Background":
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(mc_bedroom_renovation_cost):
            return True
        return f"Requires: ${mc_bedroom_renovation_cost:,.0f}"

    def home_shower_renovate_requirement():
        if home_shower.background_name == "Home_Shower_Background":
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(mc_bedroom_renovation_cost):
            return True
        return f"Requires: ${mc_bedroom_renovation_cost:,.0f}"

    def dungeon_build_action_requirement():
        if mc.has_dungeon:
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(10000):
            return True
        return "Requires: $10,000"

    def harem_mansion_build_action_requirement():
        if mc.has_harem_mansion:
            return False
        if is_home_improvement_in_progress():
            return format_home_improvement_completion_message()
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if mc.business.has_funds(200000):
            return True
        return "Requires: $200,000"

    # ModAction initialization. Kicks off initial entry into code.
    add_mc_bedroom_renovate_action = ActionMod("Home Improvement", mc_bedroom_renovate_requirement, "mc_bedroom_renovate_option_label",
        menu_tooltip = "Enables a series of renovations to make your home more impressive (with some bonuses), including building a home dungeon.", category = "Home", is_crisis = True)

    # extend the default build phone menu function with renovations
    def build_phone_menu_home_improvement_extended(org_func):
        def phone_menu_wrapper():
            # run original function
            phone_menu = org_func()
            # run extension code
            if mc.business.event_triggers_dict.get("home_improvement_unlocked", False):
                if mc.business.event_triggers_dict.get("home_improvement_bedroom_renovated", False):
                    lily_bedroom_renovate_action = Action("Renovate Lily's bedroom", lily_bedroom_renovate_requirement, "lily_bedroom_renovate_label", menu_tooltip = f"Renovates Lily's bedroom into a more impressive state and increases her love for you. Cost ${mc_bedroom_renovation_cost:,.0f}.", priority = 10)
                    mom_bedroom_renovate_action = Action("Renovate Mom's bedroom", mom_bedroom_renovate_requirement, "mom_bedroom_renovate_label", menu_tooltip = f"Renovates Mom's bedroom into a more impressive state and increases her love for you. Cost ${mc_bedroom_renovation_cost:,.0f}.", priority = 10)
                    home_shower_renovate_action = Action("Renovate bathroom", home_shower_renovate_requirement, "home_shower_renovate_label", menu_tooltip = f"Renovates the shower in your house and increases your daily energy. Cost ${mc_bedroom_renovation_cost:,.0f}.", priority = 10)
                    dungeon_build_action = Action("Build a dungeon", dungeon_build_action_requirement, "dungeon_build_label", menu_tooltip = "Clear the cellar and build a Sex Dungeon, complete with \"Guest Accommodations\". Cost $10,000.", priority = 10)

                    phone_menu[2].insert(1, dungeon_build_action)
                    phone_menu[2].insert(1, home_shower_renovate_action)
                    phone_menu[2].insert(1, mom_bedroom_renovate_action)
                    phone_menu[2].insert(1, lily_bedroom_renovate_action)
                else:
                    bedroom_renovate_action = Action("Renovate room", mc_bedroom_renovate_requirement, "mc_bedroom_renovate_label", menu_tooltip = f"Renovates your bedroom into a more impressive state (unlocks other home improvements). Cost ${mc_bedroom_renovation_cost:,.0f}.")
                    phone_menu[2].insert(1, bedroom_renovate_action)

            if mc.event_triggers_dict.get("harem_mansion_unlocked", False):
                if not mc.has_harem_mansion:
                    harem_mansion_build_action = Action("Build Harem Mansion", harem_mansion_build_action_requirement, "harem_build_label", menu_tooltip = "Build a mansion for your harem. Cost $200,000.")
                    phone_menu[2].insert(1, harem_mansion_build_action)

            return phone_menu

        return phone_menu_wrapper

    build_phone_menu = build_phone_menu_home_improvement_extended(build_phone_menu)

    def home_renovation_completion_requirement(completion_day):
        if day > completion_day and mc.business.is_open_for_business:
            return True
        return False

    def add_mc_bedroom_renovate_completed_action():
        finish_day = (day + TIER_1_TIME_DELAY + renpy.random.randint(0,3))
        mc.business.set_event_day("home_improvement_day", finish_day)
        mc_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "mc_bedroom_renovate_completed_label", requirement_args = finish_day)
        mc.business.add_mandatory_crisis(mc_bedroom_renovate_completed_action)

    def add_lily_bedroom_renovate_completed_action():
        finish_day = (day + TIER_1_TIME_DELAY + renpy.random.randint(0,3))
        mc.business.set_event_day("home_improvement_day", finish_day)
        lily_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "lily_bedroom_renovate_completed_label", requirement_args = finish_day)
        mc.business.add_mandatory_crisis(lily_bedroom_renovate_completed_action)

    def add_mom_bedroom_renovate_completed_action():
        finish_day = (day + TIER_1_TIME_DELAY + renpy.random.randint(0,3))
        mc.business.set_event_day("home_improvement_day", finish_day)
        mom_bedroom_renovate_completed_action = Action("Bedroom Renovation Completed", home_renovation_completion_requirement, "mom_bedroom_renovate_completed_label", requirement_args = finish_day)
        mc.business.add_mandatory_crisis(mom_bedroom_renovate_completed_action)

    def add_home_shower_renovate_completed_action():
        finish_day = (day + TIER_2_TIME_DELAY + renpy.random.randint(0,3))
        mc.business.set_event_day("home_improvement_day", finish_day)
        home_shower_renovate_completed_action = Action("Shower Renovation Completed", home_renovation_completion_requirement, "home_shower_renovate_completed_label", requirement_args = finish_day)
        mc.business.add_mandatory_crisis(home_shower_renovate_completed_action)

    def add_dungeon_build_completed_action():
        finish_day = day + TIER_2_TIME_DELAY + renpy.random.randint(0,3)
        mc.business.set_event_day("home_improvement_day", finish_day)
        dungeon_completed_action = Action("Dungeon Completed", home_renovation_completion_requirement, "dungeon_completed_label", requirement_args = finish_day)
        mc.business.add_mandatory_crisis(dungeon_completed_action)

    def add_harem_build_completed_action():
        finish_day = day + TIER_3_TIME_DELAY + renpy.random.randint(2, 7)
        mc.business.set_event_day("home_improvement_day", finish_day)
        harem_mansion_completed_action = Action("Harem Mansion Completed", home_renovation_completion_requirement, "harem_completed_label", requirement_args = finish_day)
        mc.business.add_mandatory_crisis(harem_mansion_completed_action)

label mc_bedroom_renovate_option_label():
    "It occurs to you that your bedroom still looks like that of a poor college student rather than someone who owns a business. Perhaps you should consider spending some time and money renovating?"
    "After a bit of online shopping you figure about $[mc_bedroom_renovation_cost] ought to cover it. Perhaps you should give someone a call on your phone."
    $ mc.business.event_triggers_dict["home_improvement_unlocked"] = True
    return

label mc_bedroom_renovate_label():
    "You decide to renovate your bedroom and call a contractor recommended by a college friend: Turner Construction, renowned for their efficiency and discretion."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your bedroom from a college student's decor to something more befitting the head of a successful company."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_mc_bedroom_renovate_completed_action()
    return

label mc_bedroom_renovate_completed_label():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "Your bedroom renovation is complete."
    python:
        bedroom.background_name = "Generic_Bedroom3_Background"
        mc.business.add_mandatory_crisis(Action("Open up additional home improvement", home_improvement_unlocked_requirement, "home_improvement_unlocked_label", requirement_args = day + 1))
    return

label home_improvement_unlocked_label():
    $ the_person = mom
    $ mc.start_text_convo(the_person)
    mom "Wow [mom.mc_title], you did a great job on renovating your bedroom. You know if you feel like it, keep going! The house sure could use some upgrades. Just give us a heads-up on what you want to do."
    mc.name "Okay, I'll think about it. And see when we have budget free."
    mom "No pressure, I know money's tight. But wow, if you could, that would be fantastic! Love you!"
    $ mc.end_text_convo()
    $ mc.business.event_triggers_dict["home_improvement_bedroom_renovated"] = True
    return

label lily_bedroom_renovate_label():
    "You decide to renovate [lily.title]'s bedroom. After discussing with [lily.possessive_title] what she wants, you call your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve her bedroom from a poor college student's decor to something more befitting your family's growing wealth."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_lily_bedroom_renovate_completed_action()
    return

label lily_bedroom_renovate_completed_label():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "[lily.possessive_title!c]'s bedroom renovation is complete."
    python:
        lily_bedroom.background_name = "Lily_Bedroom_Background"
        lily.change_stats(love = 3 + mc.charisma, obedience = 1 + mc.charisma)
    return

label mom_bedroom_renovate_label():
    "You decide to renovate [mom.title]'s bedroom. After discussing with [mom.possessive_title] what she wants, you call your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve [mom.possessive_title]'s bedroom."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_mom_bedroom_renovate_completed_action()
    return

label mom_bedroom_renovate_completed_label():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The bedroom renovation is complete."
    python:
        mom_bedroom.background_name = "Generic_Bedroom1_Background"
        mom.change_stats(love = 3 + mc.charisma, obedience = 1 + mc.charisma)
    return

label home_shower_renovate_label():
    "You decide to renovate the home shower, a little more luxury in the morning can go a long way. After talking it over with [mom.title] and [lily.title], you call your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details to vastly improve your home shower."
    python:
        mc.business.change_funds(-mc_bedroom_renovation_cost, stat = "Renovations")
        add_home_shower_renovate_completed_action()
    return

label home_shower_renovate_completed_label():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The new shower is complete and ready for inspection."
    python:
        home_shower.background_name = "Home_Shower_Background"
        mc.change_max_energy(10)
        lily.change_max_energy(10)
        mom.change_max_energy(10)
    return

label dungeon_build_label():
    "You decide to build a dungeon at your house that would allow you to turn obedient girls into slaves who fulfil your deepest desires, telling [mom.possessive_title] that it will be a \"Home Workshop\" of sorts."
    "You pick up the phone and make a call."
    mc.name "Good afternoon, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details with the constructor and agree on a price of $10,000 for converting your existing cellar into a dungeon, fully soundproofed of course."
    $ mc.business.change_funds(-10000, stat = "Renovations")
    $ add_dungeon_build_completed_action()
    return

label dungeon_completed_label():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The dungeon at your house is now ready for use."
    $ mc.event_triggers_dict["dungeon_owned"] = True
    $ dungeon.visible = True
    return

label harem_build_label():
    "Now that you have a harem, it is time to build a living space for them."
    "You pick up the phone and make a call."
    mc.name "Good afternoon, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work near my house."
    "You go over the details with the constructor and agree on a price of $200,000 for building a mansion for your harem."
    "This will take some time to complete, so be patient."
    $ mc.business.change_funds(-200000, stat = "Real Estate")
    $ add_harem_build_completed_action()
    return

label harem_completed_label():
    $ man_name = Person.get_random_male_name()
    $ play_ring_sound()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The harem mansion near your house is now ready for use."
    $ mc.event_triggers_dict["harem_mansion_build"] = True
    $ harem_mansion.visible = True
    return
