# The hint system is designed, so it does not need to be stored in a save game.
# Because it is not stored, we can update the list (or fix an issue) without breaking existing save games.
# A hint has a start condition and a completion condition.
# Only when the start condition evaluates to True and the completion condition evaluates to False it will be shown to the user.

init -1 python:
    game_hints = []

    # Hints for Sarah
    # game_hints.append(Hint("Meet Sarah", "You should stay home for a day and see who knocks on your door.", "day >= TIER_1_TIME_DELAY", "sarah.has_event_day('day_met') or sarah.is_employee or sarah.event_triggers_dict.get('rejected', False)"))
    game_hints.append(Hint("Join Sarah and Friends", "While working on Saturday, Sarah might ask you to join her for drinks with friends.", "mc.business.has_queued_crisis('Sarah_third_wheel_label') and sarah.sluttiness >= 20 and sarah.love >= 20", "not mc.business.has_queued_crisis('Sarah_third_wheel_label')"))
    game_hints.append(Hint("Date with Sarah", "While working on Saturday, Sarah might ask you on a date.", "bool(mc.business.has_queued_crisis('Sarah_get_drinks_label')) and sarah_epic_tits_progress() != 1 and sarah.sluttiness > 40 and sarah.love > 40", "not mc.business.has_queued_crisis('Sarah_get_drinks_label')"))
    game_hints.append(Hint("Catch Sarah stealing", "While working in the office on Friday evening, you might catch Sarah sneaking around the R&D department.", "mc.business.has_queued_crisis('Sarah_catch_stealing_label') and not strip_club_is_closed()", "not mc.business.has_queued_crisis('Sarah_catch_stealing_label')"))
    game_hints.append(Hint("Another date with Sarah", "Sarah might take you on another date on Saturday, when you work in the office.", "mc.business.has_queued_crisis('Sarah_stripclub_story_label') and (sarah_epic_tits_progress() >= 2 or sarah_epic_tits_progress() == -1) and not strip_club_is_closed() and sarah.sluttiness > 50 and sarah.love >= 60", "not mc.business.has_queued_crisis('Sarah_stripclub_story_label')"))

    # Hints for Kaya (Disabled for now until the character is more complete)
    # game_hints.append(Hint("Ask Kaya Out", "Go to the coffee shop and increase Kaya's love to greater than 20 and in the evening ask Kaya on a date.", "kaya_has_finished_intro()", "not kaya_has_had_drink_date() or kaya_has_started_internship() or kaya_has_moved()"))

    # Hints for HR Director Role
    game_hints.append(Hint("HR Director", "Purchase the business policy for the HR Director at your CEO office under Organisation Policies.", "sarah.has_event_day('day_met') and not HR_director_creation_policy.is_owned", "HR_director_creation_policy.is_owned"))

    # Hints for Cousin
    game_hints.append(Hint("Cousin at your house", "You should go home in the afternoon, why is your cousin in your house?", "cousin.has_queued_event('cousin_house_phase_two_label') and cousin.get_destination(time_slot = 2) == hall", "mc.business.has_queued_crisis('cousin_house_phase_three_label') or cousin.has_queued_event('cousin_blackmail_intro_label') or cousin.event_triggers_dict.get('blackmail_level', 0) > 0"))
    game_hints.append(Hint("Catch Cousin", "You should check your sister's bedroom in the afternoon, something is happening there.", "cousin.has_queued_event('cousin_blackmail_intro_label') and cousin.get_destination(time_slot = 2) == lily_bedroom", "cousin.event_triggers_dict.get('blackmail_level',99) < 1 and not cousin.has_queued_event('cousin_blackmail_intro_label')"))

    # Hints for Alexia
    game_hints.append(Hint("Meet Alexia", "You should go downtown and see if you run into someone you know.", "alexia in downtown.people and alexia.has_queued_event('alexia_intro_phase_one_label')", "not alexia.has_queued_event('alexia_intro_phase_one_label')"))
    game_hints.append(Hint("Hire Alexia", "You should head to the coffee shop and get to know her a little better so you can hire her as employee in your company.", "alexia.has_action('alexia_hire_label')", "not alexia.has_action('alexia_hire_label')"))
    game_hints.append(Hint("Alexia business cards", "The camera for shooting business cards has arrived, talk to Alexia to shoot the business card photos.", "mc.business.event_triggers_dict.get('has_expensive_camera',False)", "public_advertising_license_policy.is_owned"))

    # Hints for Nora
    game_hints.append(Hint("Nora's Research", "Don't try to research the Nora serum, just create a serum with the Nora trait and give it to a person, then interact and observe them until you have increased your mastery level sufficiently.", "university.has_action('nora_research_up_label') and mc.business.research_tier == 1 and builtins.round(mc.business.event_triggers_dict.get('nora_trait_researched').mastery_level, 1) < 2", "university.has_action('nora_research_up_label') and mc.business.research_tier == 2"))
    game_hints.append(Hint("Nora's Research Finished", "Go to the university during business hours to hand in the trait you researched for Nora.", "university.has_action('nora_research_up_label') and mc.business.research_tier == 1 and builtins.round(mc.business.event_triggers_dict.get('nora_trait_researched').mastery_level, 1) >= 2", "university.has_action('nora_research_up_label') and mc.business.research_tier == 2"))

    # Hints for Nora Serums (only visible when talking to Nora and unlocked)
    game_hints.append(Hint("Nora's Research Motherly Devotion", "Interview your Mom when her sluttiness > 75 and love > 75. Permanently increases the recipient's Love by 1 per turn for every 10 points that their Sluttiness is higher than Love.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_mother_trait in list_of_traits", "nora_reward_mother_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Sisterly Obedience", "Interview your Sister when her sluttiness > 75 and obedience > 150. Permanently increases the recipient's Sluttiness by 1 per day for every 10 points that their Obedience is above 100.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_sister_trait in list_of_traits", "nora_reward_sister_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Cousinly Hate", "Interview your Cousin when her sluttiness > 75 and love < -25. Permanently increases the recipient's Sluttiness by 1 per day for every 5 Love that they are below 0.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_cousin_trait in list_of_traits", "nora_reward_cousin_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Aunty Potential", "Interview your Aunt when her sluttiness > 75. Increases the number of traits a serum design may contain by 2.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_aunt_trait in list_of_traits", "nora_reward_aunt_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Meritocratic Attraction", "Interview Nora when her sluttiness > 75. Increases the recipient's Obedience and Sluttiness for the duration by 5 for every point of Intelligence you have.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_nora_trait in list_of_traits", "nora_reward_nora_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Lovers Attraction", "Interview anyone with her love > 85. Each turn permanently converts one point of Sluttiness into Love until they are equal.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_high_love_trait in list_of_traits", "nora_reward_high_love_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Distilled Disgust", "Interview anyone with her love < -50. Gives a massive penalty to love (-50) for the duration of the serum.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_low_love_trait in list_of_traits", "nora_reward_low_love_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Pleasurable Obedience", "Interview anyone with obedience > 180. Increases happiness by 1 for every 5 points of Obedience over 100 per turn.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_high_obedience_trait in list_of_traits", "nora_reward_high_obedience_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Rapid Corruption", "Interview anyone with her sluttiness > 95. Instantly and permanently increase Sluttiness by 5 when applied.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_high_slut_trait in list_of_traits", "nora_reward_high_slut_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Research Natural Talent", "Interview anyone with intelligence, charisma and focus >= 7. Instantly and permanently sets the serum recipient's Intelligence, Charisma, and Focus to 7.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_genius_trait in list_of_traits", "nora_reward_genius_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Human Breeding Hormones", "Interview anyone who is pregnant with sluttiness > 75 and the pregnancy is visible. Decreases birth control effectiveness and increases fertility, lactation and breast size for duration.", "persistent.pregnancy_pref != 0 and university.has_action('nora_special_research') and the_person == nora and not nora_reward_hucow_trait in list_of_traits", "nora_reward_hucow_trait in list_of_traits"))
    game_hints.append(Hint("Nora's Trance Inducer", "Interview anyone who is in a very heavy trance role and make sure to give the report to Nora while she's still in trance. Instantly puts someone in a trance, does not deepen trance.", "university.has_action('nora_special_research') and the_person == nora and not nora_reward_instant_trance in list_of_traits", "nora_reward_instant_trance in list_of_traits"))

    # Hints for Research
    game_hints.append(Hint("Research Idle", "Your research department is not working on anything at the moment, buy and enable the Theoretical Research business policy for generating Clarity.", "mc.business.active_research_design is None and not theoretical_research.is_active", "not mc.business.active_research_design is None"))
    game_hints.append(Hint("Research Mastered", "Your development effort is directed at a well-researched component, your efforts might be better spent on something else.", "mc.business.active_research_design and isinstance(mc.business.active_research_design, SerumTrait) and mc.business.active_research_design.researched and mc.business.active_research_design.mastery_level >= 2 and mc.business.active_research_design.side_effect_chance < 5", "mc.business.active_research_design and isinstance(mc.business.active_research_design, SerumTrait) and mc.business.active_research_design.side_effect_chance > 5"))
    game_hints.append(Hint("Advance Research", "You have researched all traits for your current research level, talk to your head researcher about advancing your research to the next level.", "mc.business.research_tier < 3 and researched_all_at_level()", "not researched_all_at_level()"))

    # Hints for Strip Club
    game_hints.append(Hint("The Strip Club is closed", "Wait a few days and have a chat with the sex shop owner.", "get_strip_club_foreclosed_stage() == 1", "get_strip_club_foreclosed_stage() == 3"))
    game_hints.append(Hint("Buy the strip club or not?", "When you have at least $60.000 and had a chat with the sex shop owner.", "get_strip_club_foreclosed_stage() == 3", "get_strip_club_foreclosed_stage() == 4"))
    game_hints.append(Hint("Talk with cousin", "You've bought the strip club, meet up with your cousin to get your strip club up and running.", "get_strip_club_foreclosed_stage() == 4", "get_strip_club_foreclosed_stage() == 5"))

    # Hints for Marketing
    game_hints.append(Hint("Hire Marketing", "Your market reach is too low, when you want to sell your serums with a profit you need to hire some people in Marketing to increase your market reach.", "day > 6 and len(mc.business.market_team) == 0", "len(mc.business.market_team) > 0"))
    game_hints.append(Hint("Low Aspect Profit", "Your aspect sale value is dropping, make sure to change the serums you sell or hire more people in Marketing to increase your Market Reach.", "any(p for p in [mc.business.get_aspect_percent(x) for x in ('mental', 'physical', 'sexual', 'medical')] if p < 0.6)", "all([p for p in [mc.business.get_aspect_percent(x) for x in ('mental', 'physical', 'sexual', 'medical')] if p >= 0.6])"))

    # Hints for Ellie
    game_hints.append(Hint("Meet Ellie after weekend", "Be at the office early Monday morning to find out how she's progressing with the Nano technology.", "mc.business.head_researcher and mc.business.it_director and body_monitor_progress_count() == 1", "body_monitor_progress_count() > 1"))

    # DEBUG HINTS (for fitting an positioning)
    # game_hints.append(Hint("Always Visible Hint", "This hint is always visible in the hint list.", "True", "False"))
    # hints with long text
    # game_hints.append(Hint("Nora's Research", "Don't try to research the Nora serum, just create a serum with the Nora trait and give it a person, then interact with them until you have increased your mastery level sufficiently.", "True", "False"))
    # game_hints.append(Hint("Hire Alexia", "You should head downtown and get to know her a little better so you can hire her as employee in your company.", "True", "False"))

    def number_of_hints():
        return builtins.len(active_hints())

    def active_hints():
        return [x for x in game_hints if x.is_active and not x.is_complete]

    def researched_all_at_level():
        return not any(x for x in list_of_traits if not x.researched and x.tier == mc.business.research_tier)

init 2:
    screen game_hints_tooltip():
        $ count = number_of_hints()
        $ hint_height = 90
        $ window_height = count * hint_height

        zorder 100
        frame:
            background "#1a45a1aa"
            xpos 420
            ypos 1080 - window_height
            xsize 630
            ysize window_height - ((count-1) * 5)

            vbox:
                spacing 5
                for hint in active_hints():
                    frame:
                        background "#33333388"
                        xsize 620
                        ysize hint_height - 10
                        padding (0,0)
                        vbox:
                            spacing 0
                            text "{size=18}[hint.title]{/size}" style "serum_text_style_header" xalign 0 text_align 0 xpos 2
                            $ opinion = hint.description
                            text "{size=14}[opinion]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
