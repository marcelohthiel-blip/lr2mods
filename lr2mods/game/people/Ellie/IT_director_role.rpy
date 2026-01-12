label it_director_alt_intro_label():
    "In your mind, you consider the events of the previous night and your run in with the blackmailer."
    "Your IT systems are aged... maybe it is time to consider hiring someone to lead your IT department?"
    "It would take a significant investment in policy and software, but considering the nature of your business, you think it would be doable."
    "You have unlocked a new policy to hire an IT Director."
    "Once the policy is active, you can select an IT Director from the CEO Office."
    "The IT Director will be a promotion from the research department, and can help you streamline your IT while contributing to RnD."
    $ mc.business.event_triggers_dict["it_director_policy_avail"] = True
    return

label it_director_general_hire_label():
    $ the_person = mc.business.it_director
    "You call [the_person.title] to your office. After a minute, she appears in the door."
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "Yes. Sit down."
    $ the_person.draw_person(position = "sitting")
    if mc.business.event_triggers_dict.get("previous_it", False) == True: #We've already had an IT Director, so just bring her up to speed.
        mc.name "I have a special assignment that I want you to take over."
        the_person "Oh?"
        mc.name "The business is in need of a new IT Director. I'd like for you to take the role."
        mc.name "You'll be running it from the research department as an additional duty, extra compensation accordingly."
        mc.name "Our small business doesn't need a full time director, but you'll be working on IT projects at my direction."
        the_person "Oh wow. Okay, as long as it doesn't interfere with my research too much."
        mc.name "Research will always be your first priority, but I think you have what it takes to help with this also."
    else:
        $ mc.business.event_triggers_dict["previous_it"] = True
        mc.name "I have a new special assignment that I want you to lead. You'll be working with the head researcher directly."
        the_person "Oh?"
        mc.name "The company's IT systems are ageing poorly. I need someone to lead work on new IT Projects to help us modernize."
        mc.name "I don't have the payroll to make it a dedicated position, so it is in addition to your duties in research, but it includes a bump in pay."
        mc.name "Your first priority will always be research, but in your down time I'll give you new IT project to work on."
        the_person "Oh wow. Okay, as long as it doesn't interfere with my research too much."
        mc.name "It shouldn't."

    call initial_set_duties_label(the_person) from _call_initial_set_duties_head_it_director_hire

    the_person "Yes sir! Will that be all?"
    mc.name "For now, yeah."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] is now your IT Director. Talk to her to begin work on new IT Projects!"
    return

label update_IT_projects_label(the_person):
    mc.name "I'd like to review the IT projects."
    the_person "Ok. Here's what we have going on right now, [the_person.mc_title]."
    call screen it_project_screen()
    the_person "Got it. Is there anything else I can do for you, [the_person.mc_title]?"
    return

label IT_project_complete_label(the_project):
    $ the_person = mc.business.it_director
    if the_person is None:
        return
    $ the_person.draw_person()
    "[the_person.possessive_title!c] tracks you down while you are working."
    the_person "Hey [the_person.mc_title], just wanted to let you know I finished up with the [the_project.name] you had me working on."
    "You take a moment to review your completed projects and decide if you want her to start something different."
    call screen it_project_screen()
    "When you finish reviewing her projects, [the_person.title] gets back to work."
    return

label IT_director_nanobot_intro_label(the_person):
    "You approach [the_person.possessive_title] to talk to her about your nanobot program."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]."
    the_person "Hey [the_person.mc_title]. Need something?"
    mc.name "I do. Our research department has hit a bit of a dead end with the nanobot development project, and I was wondering if you could lend your expertise."
    the_person "I suppose. Didn't we already discuss the projects I could work on to improve your nanobots?"
    mc.name "Yes, but I have ideas for completely new programs I would like to have designed."
    the_person "Ah, I see."
    mc.name "Can we go to my office?"
    the_person "Sure."
    $ ceo_office.show_background()
    $ the_person.draw_person(position = "sitting")
    "You walk with [the_person.possessive_title] to your office. She sits down across from you."
    if fetish_serum_unlock_count() == 1:
        mc.name "Right, well as you know, we have a basic nanobot program, designed to increase a female's propensity for sexual activities."
        the_person "errmm... right..."
        mc.name "I have some ideas for programs that are a bit more... specific..."
        "You explain to [the_person.possessive_title] your ideas for four new nanobot programs."
        $ the_person.change_slut(1, 40)
    elif fetish_serum_unlock_count() < 4:
        mc.name "Right. As you know, we have a few basic programs for our nanobots, but I have ideas for more."
        "You explain to [the_person.possessive_title] your ideas for new nanobot programs."
        $ the_person.change_slut(1, 40)
    elif fetish_serum_unlock_count() == 4:
        mc.name "Right. As you know, we have a few programs for our nanobots, but I have an idea for one more."
        "You explain to [the_person.possessive_title] your idea for a new nanobot program."
        $ the_person.change_slut(1, 40)
    else:
        mc.name "Right. As you know, we have several programs for our nanobots, but we still know so little about how they actually affect people."
    if fetish_serum_unlock_count() < 5:
        "When you finish, her cheeks are flushed from embarrassment."
        the_person "I... I don't know... you're talking about..."
        mc.name "I know. This is a little outside of your comfort zone, but as my only IT employee, I need you to step up and help out with it."
        "She seems unconvinced for now, but relents."
        the_person "I suppose I could do that."
        $ the_person.change_obedience(3)
        mc.name "Thank you. In addition, we know so little about how they actually affect people."
    mc.name "I was hoping you would be willing to work with Research so we can learn more about them."
    mc.name "Nothing crazy, just help monitor their effects as we run tests with them."
    the_person "I'm not sure this is a good idea..."
    "It seems like [the_person.title] might need some convincing..."
    menu:
        "Do it for me\n{menu_red}Increases love{/menu_red}":
            mc.name "I know this seems odd, but I need you to trust me, okay?"
            mc.name "Don't worry, I have a plan, and I need someone like you to get this done."
            $ the_person.change_love(3)
        "It'll be fun\n{menu_red}Increases sluttiness{/menu_red}":
            mc.name "Don't worry. We'll be able to use it to have all kinds of fun."
            $ the_person.change_slut(3, 60)
        "I'm the boss\n{menu_red}Increases obedience{/menu_red}":
            mc.name "I know it seems odd, but remember who makes out your paychecks, okay?"
            $ the_person.change_obedience(3)
    the_person "I suppose..."
    mc.name "Great!"
    $ the_person.draw_person()
    "You both stand up."
    the_person "I'll add those programs to the list of projects I can work on then... just let me know when you want me to work on them."
    mc.name "Certainly."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and walks out of your office."
    $ clear_scene()
    "From now on, you can work with her towards perfecting your nanobot programs."
    "In addition, you can talk to her about the programs as you begin to master them."
    if the_person == ellie:
        $ add_IT_director_teamup_start_action()
    $ mc.location.show_background()
    return

label IT_director_teamup_start_label():
    call ellie_stephanie_teamup_progression_scene_action_label(ellie) from _it_director_teamup_intro_prog_scene_intro_01
    return
