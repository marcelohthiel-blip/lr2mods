init 0 python:
    def get_candidate_count_costs():
        interview_cost = mc.business.recruitment_cost
        count = 3 #Num of people to generate, by default is 3. Changed with some policies
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                count += recruitment_policy.extra_data.get("recruitment_batch_adjust",0)
                interview_cost +=  recruitment_policy.extra_data.get("interview_cost_adjust",0)

        return count, interview_cost

    def interview_build_candidates_list(count):
        start_time = time.time()
        candidates = []
        for x in builtins.range(0, count): #NOTE: count is given +1 because the screen tries to pre-calculate the result of button presses. This leads to index out-of-bounds, unless we pad it with an extra character (who will not be reached).
            candidates.append(make_person(allow_premade = True, **(mc.business.generate_candidate_requirements())))

        reveal_count = 0
        reveal_sex = False

        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_count += recruitment_policy.extra_data.get("reveal_count_adjust",0)
                reveal_sex = reveal_sex or recruitment_policy.extra_data.get("reveal_sex_opinion",False)

        for a_candidate in candidates:
            for x in builtins.range(0,reveal_count): #Reveal all of their opinions based on our policies.
                a_candidate.discover_opinion(a_candidate.get_random_opinion(include_known = False, include_sexy = reveal_sex),add_to_log = False) #Get a random opinion and reveal it.

            # new candidate could be pregnant
            if persistent.pregnancy_pref > 0:
                if a_candidate.age > 21 and renpy.random.randint(0,100) < (58 - a_candidate.age) // 5: # chance she is already pregnant decreases with age
                    #Can hire her up to 10 days from due date. Probably not hiring anyone a week from due!
                    become_pregnant(a_candidate, mc_father = False, progress_days = renpy.random.randint(5,80))
                    #renpy.say("Pregnant", "Candidate: " + a_candidate.name + " " + a_candidate.last_name + " is pregnant.")

        add_to_debug_log(f"Candidates ({count}): {{total_time:.3f}}", start_time)
        return candidates


label sleep_action_description():
    if mc.business.is_weekend:
        "You go to bed after a nice day."
    else:
        "You go to bed after a hard day's work."
    call advance_time() from _call_advance_time
    return

label hr_work_action_description():
    $ mc.business.player_hr()
    call advance_time() from _call_advance_time_1
    return

label research_work_action_description():
    $ mc.business.player_research()
    call advance_time() from _call_advance_time_2
    return

label supplies_work_action_description():
    $ mc.business.player_buy_supplies()
    call advance_time() from _call_advance_time_3
    return

label market_work_action_description():
    $ mc.business.player_market()
    call advance_time() from _call_advance_time_4
    return

label production_work_action_description():
    $ mc.business.player_production()
    call advance_time() from _call_advance_time_5
    return

label manage_contracts_action_description():
    $ hide_ui()
    $ renpy.block_rollback()
    call screen manage_contracts_ui()
    $ renpy.block_rollback()
    $ show_ui()
    return

label interview_action_description():
    $ count, interview_cost = get_candidate_count_costs()

    "Bringing in [count] people for an interview will cost $[interview_cost]. Do you want to spend time interviewing potential employees?"
    menu:
        "Yes, I'll pay the cost\n{menu_red}Costs: $[interview_cost]{/menu_red}" if mc.business.has_funds(interview_cost):
            $ mc.business.change_funds(-interview_cost, stat = "Investments")
            $ clear_scene()

            $ candidates = interview_build_candidates_list(count)

            # pad with one extra element, to make sure we can see all candidates
            call hire_select_process(candidates + [1]) from _call_hire_select_process_interview_action_enhanced

            if isinstance(_return, Person):
                $ new_person = _return
                $ new_person.generate_home().add_person(new_person) #Generate them a home location so they have somewhere to go at night.
                $ candidates.remove(new_person)

                call hire_someone(new_person) from _call_hire_someone_interview_action_enhanced

                $ hire_day = "tomorrow"
                if day%7 == 4 or day%7 == 5: #If it's Friday or Saturday, don't start tomorrow
                    $ hire_day = "Monday"

                "With all arrangements made, [new_person.fname] will start [hire_day]."
                $ new_person.set_title()
                $ new_person.set_possessive_title()
                $ new_person.set_mc_title()
                $ new_person.set_event_day("day_met")
                $ del new_person
            else:
                "You decide against hiring anyone new for now."

            # cleanup not used candidates
            python:
                if persistent.keep_patreon_characters:
                    for person in candidates:
                        if person.type == "unique": # preserve Patreon unique characters.
                            person.generate_home()
                            person.home.add_person(person)
                        else:
                            person.remove_person_from_game()

                candidates.clear() #Prevent it from using up extra memory
                person = None
                candidates = None

            call advance_time() from _call_advance_time_interview_action_enhanced
        "Yes, I'll pay the cost\n{menu_red}Costs: $[interview_cost]{/menu_red} (disabled)" if not mc.business.has_funds(interview_cost):
            pass
        "Never mind":
            pass
    return

label hire_select_process(candidates):
    $ hide_ui()
    $ show_candidate(candidates[0]) #Show the first candidate, updates are taken care of by actions within the screen.
    show bg paper_menu_background #Show a paper background for this scene.
    $ count = builtins.len(candidates)-1
    call screen interview_ui(candidates,count)
    $ renpy.scene()
    $ show_ui()
    $ clear_scene()
    $ mc.location.show_background()

    return _return

label hire_someone(new_person, research_allowed = True, production_allowed = True, supply_allowed = True, marketing_allowed = True, hr_allowed = True, start_day = -1): # Breaks out some of the functionality of hiring someone into an independent label.
    "You complete the necessary paperwork and hire [new_person.name]. What division do you assign them to?"
    menu:
        "Research and Development" if research_allowed:
            $ mc.business.add_employee_research(new_person, start_day)

        "Production" if production_allowed:
            $ mc.business.add_employee_production(new_person, start_day)

        "Supply Procurement" if supply_allowed:
            $ mc.business.add_employee_supply(new_person, start_day)

        "Marketing" if marketing_allowed:
            $ mc.business.add_employee_marketing(new_person, start_day)

        "Human Resources" if hr_allowed:
            $ mc.business.add_employee_hr(new_person, start_day)

    call set_duties_controller(new_person, new_person.primary_job) from _call_set_duties_controller_hire_someone
    if _return:
        $ new_person.set_event_day("work_duties_last_set")

    $ generate_random_characters()    # make sure world locations don't bleed dry
    return

label serum_design_action_description(the_serum = None):
    $ hide_ui()
    if not the_serum:
        $ the_serum = SerumDesign()

    call screen serum_design_ui(the_serum) #This will return the final serum design, or None if the player backs out.
    $ the_serum = _return

    $ show_ui()
    if isinstance(the_serum, SerumDesign):
        label .set_serum_name():
            python:
                the_serum.name = renpy.input("Please give this serum design a name.", the_serum.name, exclude="[]{}")
                if any(x for x in mc.business.serum_designs if x.name == the_serum.name):
                    renpy.say(None, "You already have a serum with that name, please choose another name.", exclude="[]{}")
                    renpy.jump("serum_design_action_description.set_serum_name")

                mc.business.add_serum_design(the_serum)
                mc.business.listener_system.fire_event("new_serum", the_serum = the_serum)
                mc.business.listener_system.fire_event("general_work")
                the_serum = None
        call advance_time() from _call_advance_time_7
    else:
        "You decide not to spend any time designing a new serum type."
    return

label research_select_action_description():
    $ hide_ui()
    call screen research_select_ui()
    $ show_ui()
    return

label production_select_action_description():
    $ hide_ui()
    call screen serum_production_select_ui()
    $ show_ui()
    return

label trade_serum_action_description():
    "You step into the stock room to check what you currently have produced."
    $ hide_ui()
    $ renpy.block_rollback()
    call screen serum_trade_ui(mc.inventory,mc.business.inventory)
    $ renpy.block_rollback()
    $ show_ui()
    return

label sell_serum_action_description():
    $ hide_ui()
    $ renpy.block_rollback()
    call screen serum_sell_ui()
    $ renpy.block_rollback()
    $ show_ui()
    return

label review_designs_action_description():
    $ hide_ui()
    $ renpy.block_rollback() #Block rollback to prevent any strange issues with references being lost.
    call screen review_designs_screen()
    $ renpy.block_rollback()
    $ show_ui()
    return

label pick_supply_goal_action_description():
    $ amount = renpy.input("How many units of serum supply would you like your supply procurement team to keep stocked?", allow = "0123456789")
    $ amount = builtins.int(amount.strip())
    $ mc.business.supply_goal = amount
    if mc.business.is_open_for_business:
        if amount <= 0:
            "You tell your team to keep [amount] units of serum supply stocked. They question your sanity, but otherwise continue with their work."
        else:
            "You tell your team to keep [amount] units of serum supply stocked."
    else:
        "You leave a note for the team to keep [amount] units of serum supply in stock."
    return

label policy_purchase_description():
    call screen policy_selection_screen()
    return

label head_researcher_select_description():
    call screen employee_overview(white_list = [x for x in mc.business.research_team if x.is_at_office], black_list = [mc.business.it_director], person_select = True, allow_none = True)
    if isinstance(_return, Person):
        $ mc.business.hire_head_researcher(_return)
        call head_researcher_general_hire_label() from _head_researcher_hire_01
    else:
        "You decide not to hire a head researcher."
    return

label personal_secretary_select_description():
    call screen employee_overview(white_list = [x for x in mc.business.hr_team if x.is_at_office], black_list = [mc.business.hr_director], person_select = True, allow_none = True)
    if isinstance(_return, Person):
        $ mc.business.hire_personal_secretary(_return)
        call personal_secretary_general_hire_label() from _personal_secretary_hire_01
    else:
        "You decide not to hire a personal secretary."
    return

label production_assistant_select_description():
    call screen employee_overview(white_list = [x for x in mc.business.production_team if x.is_at_office], person_select = True, allow_none = True)
    if isinstance(_return, Person):
        $ mc.business.hire_production_assistant(_return)
        call production_assistant_general_hire_label() from _production_assistant_hire_01
    else:
        "You decide not to hire a production assistant."
    return

label it_director_select_description():
    call screen employee_overview(white_list = [x for x in mc.business.research_team if x.is_at_office], black_list = [mc.business.head_researcher], person_select = True, allow_none = True)
    if isinstance(_return, Person):
        $ mc.business.hire_IT_director(_return)
        call it_director_general_hire_label() from _it_director_hire_01
    else:
        "You decide not to hire an IT director."
    return

label pick_company_model_description():
    call screen employee_overview(person_select = True, white_list = mc.business.employees_at_office, black_list = [mc.business.head_researcher, mc.business.it_director, mc.business.hr_director, mc.business.prod_assistant], allow_none = True)
    if isinstance(_return, Person):
        $ mc.business.hire_company_model(_return)
        call company_model_general_hire_label() from _company_model_hire_01
    else:
        "You decide not to hire a company model."
    return

label uniform_manager_loop():
    call screen uniform_manager()
    if _return == "Add":
        call outfit_master_manager() from _call_outfit_master_manager_uniform_manager_loop #TODO: Decide if we need to pass this the uniform parameters, of if we do that purely in what's selectable.
        if isinstance(_return, Outfit):
            $ mc.business.business_uniforms.append(UniformOutfit(_return))
            $ mc.business.listener_system.fire_event("add_uniform", the_outfit = _return)
        jump uniform_manager_loop
    return

label set_serum_description():
    call screen assign_division_serum()
    return

label mc_research_breakthrough(new_level, clarity_cost):
    "You feel an idea in the back of your head. You realise it's been there this whole time, but you've been too distracted to see it."
    "You snatch up the nearest notebook and get to work right away."
    "Within minutes your thoughts are flowing fast and clear. Everything makes sense, and your path forward is made crystal clear."
    $ mc.spend_clarity(clarity_cost)
    $ mc.business.research_tier = new_level
    if new_level == 1:
        $ add_suggest_testing_room()
        $ mc.log_event("Tier 1 Research Unlocked", "float_text_grey")
    elif new_level == 2:
        $ mc.log_event("Tier 2 Research Unlocked", "float_text_grey")
    else:
        $ mc.log_event("Max Research Tier Unlocked", "float_text_grey")
    "You throw your pen down when you're finished. Your new theory is awash in possibilities!"
    "Now you just need to research them in the lab!"
    return
