#Counter KS01
init -10:
    define KiNA_MOD = True

#tweaked start
init -1 python:
    #add mod var check here
    mod_checks = [
        ("KiNA Mod",   kina_enabled),
        ("VT Mod",   vt_enabled),
        ("Kaden Mod",  kaden_enabled),
        ("Grow Up Mod",    gum_enabled),
        ("ZenPack", zenpak_enabled),
        ("RealPorn Mod", realporn_enabled),
        ("Moresome Mod", moresomes_enabled)
    ]

    def get_enabled_mods() -> list[str]:
        """
        Returns the list of mod‑names whose check function returns True.
        """
        # call each check exactly once
        return [ name for name, check in mod_checks if check() ]

    def format_mod_list(names: list[str]) -> str:
        """
        Turn ["A","B","C"] into "A, B and C",
        ["A","B"]    into "A and B",
        ["A"]        into "A".
        """
        if not names:
            return "KiNA Mod"
        if len(names) == 1:
            return names[0]
        # Oxford‑comma style:
        return ", ".join(names[:-1]) + " and " + names[-1]

    def kina_update_game_speed(speed):
        global GAME_SPEED, TIER_1_TIME_DELAY, TIER_2_TIME_DELAY, TIER_3_TIME_DELAY

        GAME_SPEED = speed
        if speed == 0:
            #TIER_0_TIME_DELAY = -1
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 5
        elif speed == 1:
            #TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 3
            TIER_2_TIME_DELAY = 7
            TIER_3_TIME_DELAY = 10
        elif speed == 2:
            #TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 5
            TIER_2_TIME_DELAY = 11
            TIER_3_TIME_DELAY = 15
        elif speed ==3:
            #TIER_0_TIME_DELAY = 2
            TIER_1_TIME_DELAY = 7
            TIER_2_TIME_DELAY = 15
            TIER_3_TIME_DELAY = 20
        else:
            GAME_SPEED = 3
            #TIER_0_TIME_DELAY = -1
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 5

        return

init 10 python:
#making it a habit to init hijack label lower priority... STOP STEALING MY START ELK!!!
 
    #if vt_enabled():
    #    config.label_overrides["VT_start"] = "kina_start"
    #else:
    config.label_overrides["start"] = "kina_start"        
        

label kina_start():
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."

    #if vt_enabled() or kaden_enabled() or gum_enabled():
    #    if vt_enabled() and kaden_enabled() and gum_enabled():
    #        "Detected mod: KiNA , Kaden , GUM and VT."
    #    elif vt_enabled() and kaden_enabled():
    #        "Detected mod: KiNA , Kaden and VT."
    #    elif vt_enabled() and gum_enabled():
    #        "Detected mod: KiNA , GUM and VT."
    #    else:
    #        "Detected mod: KiNA and Kaden."
    #else:
    #    "Detected mod: KiNA Mod."
    $ enabled = get_enabled_mods()

    $ text = "Detected mod: " + format_mod_list(enabled) + "."
    "[text]"

    "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."

    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Semi-Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

        "Realistic pregnancy content\n{size=16}Realistic cycles. Girls know their fertile times. Pulling out not 100%% effective. Girls don't want to get pregnant.{/size}":
            $ persistent.pregnancy_pref = 3

    "How quickly would you like stories from the game to play out? This will affect spacing between story events."
    menu:
        "Quick":
            $ kina_update_game_speed(0)
        "Standard":
            $ kina_update_game_speed(1)
        "Epic":
            $ kina_update_game_speed(2)
        "Marathon":
            $ kina_update_game_speed(3)
        "KiNA Mode (Quick but Reduced Interaction)":
            $ kina_update_game_speed(4)

    $ easy_mode = False
    $ kina_mode = False
    $ cherry_mode = False
    "Choose a Game Mode..."
    menu:
        "Default Game Play":
            pass
        "Higher Max Stats for MC":
            "Default gameplay but higher max ceiling for MC. And unlocked theoretical research policy at start."
            $ kina_mode = True
        "Easier Game Play":
            "All options for making the game easier will be applied after character creation."
            $ easy_mode = True
        "Super Cheat":
            "Easier Game Play + Higher Max Stats for MC. All options for making the game easier will be applied after character creation."
            $ kina_mode = True
            $ easy_mode = True
        "Easy Cherries" if vt_enabled():
            "Easy Cherries! Easy Mode + Higher Stats, everything set to just have fun"
            $ cherry_mode = True

    "Finally, the game uses random generated characters, the mod offers you the ability to control the random generation."
    "We will now open that screen for you, so you can set it to your preferences."

    call screen generic_preference_ui()

    $ starting_hires = False
    "Do you want to start the game employing just the head researcher? Or would you like to hire someone for each department?"
    menu:
        "Just Head Researcher":
            pass
        "Hire for Each Department":
            $ starting_hires = True

    if vt_enabled():
        "This next screen currently not fully implemented..."
        call screen VTMOD_setup_ui()

    "That's all, the game will now initialize, this might take a moment."

    $ renpy.block_rollback()
    if persistent.stats:
        $ name = persistent.stats['name']
        $ l_name = persistent.stats['l_name']
        $ b_name = persistent.stats['b_name']
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    $ setattr(persistent, "stats", {})
    $ [[persistent.stats["cha"],persistent.stats["int"],persistent.stats["foc"]], [persistent.stats["h_skill"],persistent.stats["m_skill"],persistent.stats["r_skill"],persistent.stats["p_skill"],persistent.stats["s_skill"]], [persistent.stats["F_skill"],persistent.stats["O_skill"],persistent.stats["V_skill"],persistent.stats["A_skill"]]] = _return
    $ [persistent.stats["name"],persistent.stats["l_name"],persistent.stats["b_name"]] = [store.name,store.l_name,store.b_name]


    python:
        renpy.show("Loading", layer = "solo", at_list = [truecenter], what = Image(get_file_handle("creating_world.png")))
        renpy.pause(0.5)
        renpy.game.interface.timeout(30)
        if easy_mode:
            for array in range(0, builtins.len(return_arrays)):
                for val in range(0, builtins.len(return_arrays[array])):
                    return_arrays[array][val] += 2

    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2]) from _call_initialize_game_state_KS01

    python:
        if easy_mode:
            # increased business stats
            mc.business.funds = 10000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 1000
            mc.business.base_effectiveness_cap = 110
            mc.business.marketability = 100
            # increased player stats
            mc.max_energy = 120
            mc.free_clarity += 500
            mc.clarity_multiplier = 3.0     # gain clarity 3 times faster
            # default unlock policies
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(theoretical_research, ignore_cost = True)
            purchase_policy(max_attention_increase_1_policy, ignore_cost = True)
        
        #KiNA Mode
        if kina_mode:
            mc.max_stats = 10
            mc.max_work_skills = 10
            mc.max_sex_skills = 10
            mc.max_energy_cap = 300
            mc.business.supply_count = 500
            mc.business.supply_goal = 1000
            purchase_policy(theoretical_research, ignore_cost = True)

        #Starting Hires
        if starting_hires:
            market_hire = create_random_person()
            hr_hire = create_random_person()
            prod_hire = create_random_person()
            supply_hire = create_random_person()

            market_hire.market_skill = 4
            market_hire.charisma = 4
            market_hire.focus = 1
            market_hire.int = 1
            market_hire.hr_skill = 1
            market_hire.research_skill = 1
            market_hire.production_skill = 1
            market_hire.supply_skill = 1
            market_hire.set_opinion("marketing work", 2, False)
            market_hire.generate_home().add_person(market_hire)

            hr_hire.market_skill = 1
            hr_hire.charisma = 4
            hr_hire.focus = 1
            hr_hire.int = 1
            hr_hire.hr_skill = 4
            hr_hire.research_skill = 1
            hr_hire.production_skill = 1
            hr_hire.supply_skill = 1
            hr_hire.set_opinion("hr work", 2, False)
            hr_hire.generate_home().add_person(hr_hire)

            prod_hire.market_skill = 1
            prod_hire.charisma = 1
            prod_hire.focus = 4
            prod_hire.int = 1
            prod_hire.hr_skill = 1
            prod_hire.research_skill = 1
            prod_hire.production_skill = 4
            prod_hire.supply_skill = 1
            prod_hire.set_opinion("production work", 2, False)
            prod_hire.generate_home().add_person(prod_hire)

            supply_hire.market_skill = 1
            supply_hire.charisma = 1
            supply_hire.focus = 4
            supply_hire.int = 1
            supply_hire.hr_skill = 1
            supply_hire.research_skill = 1
            supply_hire.production_skill = 1
            supply_hire.supply_skill = 4
            supply_hire.set_opinion("supply work", 2, False)
            supply_hire.generate_home().add_person(supply_hire)

            mc.business.add_employee_marketing(market_hire)
            mc.business.add_employee_hr(hr_hire)
            mc.business.add_employee_production(prod_hire)
            mc.business.add_employee_supply(supply_hire)


        #Cherry Mode
        if cherry_mode:
            # increased business stats
            mc.business.funds = 500000
            mc.business.funds_yesterday = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 10000
            mc.business.effectiveness_cap = 110
            mc.business.marketability = 100
            mc.business.max_employee_count = 12
            # increased player stats
            mc.charisma +=4
            mc.int +=4
            mc.focus +=4
            mc.hr_skill +=4
            mc.market_skill +=4
            mc.research_skill +=4
            mc.production_skill +=4
            mc.supply_skill +=4
            mc.sex_skills["Foreplay"] +=4
            mc.sex_skills["Oral"] +=4
            mc.sex_skills["Anal"] +=4
            mc.sex_skills["Vaginal"] +=4
            mc.max_stats = 15
            mc.max_work_skills = 15
            mc.max_sex_skills = 15
            mc.max_energy_cap = 600
            mc.business.supply_goal += 1000
            mc.energy = 500
            mc.max_energy = 500
            mc.free_clarity += 10500
            mc.clarity_multiplier = 3.0     # gain clarity 3 times faster
            # default unlock policies

            #========= Clothing Policies=============================
            purchase_policy(strict_uniform_policy, ignore_cost = True)
            purchase_policy(relaxed_uniform_policy, ignore_cost = True)
            purchase_policy(casual_uniform_policy, ignore_cost = True)
            purchase_policy(reduced_coverage_uniform_policy, ignore_cost = True)
            purchase_policy(minimal_coverage_uniform_policy, ignore_cost = True)
            purchase_policy(corporate_enforced_nudity_policy, ignore_cost = True)
            purchase_policy(maximal_arousal_uniform_policy, ignore_cost = True)
            #mandatory_vibe_policy,
            #mandatory_bullet_policy,
            #mandatory_plug_policy,
            purchase_policy(male_focused_marketing_policy, ignore_cost = True)
            #creative_colored_uniform_policy,
            #personal_bottoms_uniform_policy,
            purchase_policy(casual_friday_uniform_policy, ignore_cost = True)
            #creative_skimpy_uniform_policy,
            purchase_policy(dress_code_policy, ignore_cost = True)
            #easier_access_policy,
            purchase_policy(commando_uniform_policy, ignore_cost = True)

            #========= Organization Policies=============================
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(business_size_2_policy, ignore_cost = True)
            purchase_policy(business_size_3_policy, ignore_cost = True)
            #business_size_4_policy,
            purchase_policy(business_contract_increase_1_policy, ignore_cost = True)
            purchase_policy(business_contract_offer_increase_1_policy, ignore_cost = True)
            purchase_policy(business_contract_increase_2_policy, ignore_cost = True)
            purchase_policy(business_contract_offer_increase_2_policy, ignore_cost = True)
            purchase_policy(public_advertising_license_policy, ignore_cost = True)
            #office_punishment,
            #corporal_punishment,
            #strict_enforcement,
            #draconian_enforcement,
            #bureaucratic_nightmare,
            purchase_policy(theoretical_research, ignore_cost = True)
            purchase_policy(research_journal_subscription, ignore_cost = True)
            purchase_policy(practical_experimentation, ignore_cost = True)
            #office_conduct_guidelines,
            #mandatory_staff_reading,
            #superliminal_office_messaging,
            #max_attention_increase_1_policy,
            #attention_bleed_increase_1_policy,
            #attention_floor_increase_1_policy,

            #======== Recruitment Policies===================================
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_two_policy, ignore_cost = True)
            #recruitment_batch_three_policy,
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_two_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_three_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_four_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_minimums_policy, ignore_cost = True)
            purchase_policy(recruitment_stat_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_stat_minimums_policy, ignore_cost = True)
            purchase_policy(recruitment_suggest_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_obedience_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_slut_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_sex_improvement_policy, ignore_cost = True)
            purchase_policy(recruitment_sex_minimums_policy, ignore_cost = True)
            #recruitment_small_tits_policy,
            #recruitment_tiny_tits_policy,
            #recruitment_big_tits_policy,
            #recruitment_huge_tits_policy,
            #recruitment_short_policy,
            #recruitment_tall_policy,
            #recruitment_single_policy,
            #recruitment_married_policy,
            purchase_policy(recruitment_teen_policy, ignore_cost = True)
            #recruitment_old_policy,
            #recruitment_mothers_policy,
            #recruitment_childless_policy,

            #======= Serum/Production Policies==========================
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(mandatory_unpaid_serum_testing_policy, ignore_cost = True)
            #daily_serum_dosage_policy,
            #weekend_serum_dosage_policy,
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(serum_size_2_policy, ignore_cost = True)
            purchase_policy(serum_size_3_policy, ignore_cost = True)
            purchase_policy(serum_production_1_policy, ignore_cost = True)
            purchase_policy(serum_production_2_policy, ignore_cost = True)
            purchase_policy(serum_production_3_policy, ignore_cost = True)
            purchase_policy(production_line_addition_1_policy, ignore_cost = True)
            purchase_policy(production_line_addition_2_policy, ignore_cost = True)
            purchase_policy(breast_milking_space_policy, ignore_cost = True)
            purchase_policy(auto_pumping_stations_policy, ignore_cost = True)
            purchase_policy(high_suction_pumping_machinery_policy, ignore_cost = True)

        renpy.hide("Loading", layer = "solo")
    

    $ renpy.block_rollback()
    
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start_KS01

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start