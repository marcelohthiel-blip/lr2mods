init 1 python: 
    def auto_research_requirement():
        if mc.business.is_open_for_business:
            if mc.business.head_researcher:
                if mc.business.head_researcher.is_at_office:
                    if day > 5:
                        if mc.business.active_research_design is None or (isinstance(mc.business.active_research_design, SerumTrait) and mc.business.active_research_design.researched and mc.business.active_research_design.side_effect_chance < 5):
                            if not mc.business.event_triggers_dict.get("auto_research_intro", False) or mc.business.event_triggers_dict.get("auto_research_active", False):
                                if auto_research_trait_research() or auto_research_trait_unlock() or auto_research_trait_mastery():
                                    return True
        return False

    def auto_research_discuss_requirement(person):
        if person != mc.business.head_researcher:
            return False
        if not mc.business.event_triggers_dict.get("auto_research_intro", False):
            return False
        if not mc.is_at_work or not mc.business.is_open_for_business:
            return "Talk at work"
        return True

    def auto_research_trait_research():
        temp_list = []
        temp_number = 99999
        for trait in list_of_traits:
            if trait.unlocked and not trait.researched:
                if not isinstance(trait, SerumTraitBlueprint):
                    if isinstance(trait, SerumTrait):
                        temp_list.append(trait)
        if temp_list:
            for trait in temp_list:
                if (trait.research_needed-trait.current_research) < temp_number:
                    temp_number = (trait.research_needed-trait.current_research)
                    temp_trait = trait
            return temp_trait
        return False

    def auto_research_trait_unlock():
        temp_list = []
        temp_number = 99999
        for trait in list_of_traits:
            if not trait.unlocked and not trait.researched and trait.tier <= mc.business.research_tier:
                if not isinstance(trait, SerumTraitBlueprint):
                    if isinstance(trait, SerumTrait):
                        temp_list.append(trait)
        if temp_list:
            for trait in temp_list:
                if trait.clarity_cost < temp_number:
                    if "Production" in trait.exclude_tags or "Suggest" in trait.exclude_tags:
                        return trait
                    temp_number = trait.clarity_cost
                    temp_trait = trait
            return temp_trait
        return False

    def auto_research_trait_mastery():
        temp_list = []
        temp_number = 99999
        for trait in list_of_traits:
            if trait.unlocked and trait.researched and trait.side_effect_chance > 0:
                if not isinstance(trait, SerumTraitBlueprint):
                    if isinstance(trait, SerumTrait):
                        temp_list.append(trait)
        if temp_list:
            temp_number = 0
            for trait in temp_list:
                if trait.side_effect_chance > temp_number:
                    temp_number = trait.side_effect_chance
                    temp_trait = trait
            if mc.business.active_research_design is None or mc.business.active_research_design.name != temp_trait.name:
                return temp_trait
        return False

init 16 python:
    add_label_hijack("normal_start", "activate_auto_research_mod_core")
    add_label_hijack("after_load", "update_auto_research_mod_core")

    def auto_research_mod_initialization():
        auto_research = Action("Auto Research", auto_research_requirement, "auto_research_label")
        auto_research_discuss = Action("Discuss Automatic Research", auto_research_discuss_requirement, "auto_research_discuss_label", menu_tooltip = "Discuss your Head Researcher picking research topics.", priority = 2)
        if auto_research_discuss not in head_researcher.actions:
            mc.business.mandatory_crises_list.append(auto_research)
            head_researcher.add_action(auto_research_discuss)
        return

label activate_auto_research_mod_core(stack):
    python:
        auto_research_mod_initialization()
        execute_hijack_call(stack)
    return

label update_auto_research_mod_core(stack):
    python:
        auto_research_mod_initialization()
        execute_hijack_call(stack)
    return

label auto_research_label():
    $ temp_trait = None
    $ the_person = mc.business.head_researcher
    "You receive a text from your head researcher [the_person.title]. It reads:"
    if not mc.business.event_triggers_dict.get("auto_research_intro", False):
        $ mc.business.event_triggers_dict["auto_research_intro"] = True
        $ mc.start_text_convo(the_person)
        the_person "[the_person.mc_title], I appreciate all the free time you're giving me in the lab, but I think my talents would be better used if you put me to work."
        the_person "I've got some promising leads, would you like me to pick one to pursue?"
        "How would you like to reply?"
        menu:
            "Let her pick research":
                mc.name "Yeah, that's fine. Go ahead."
                the_person "Really? That's great. You won't regret this."
                $ mc.business.event_triggers_dict["auto_research_active"] = True
                the_person "If you ever decide you want to take over again just let me know. I'll look the traits over and let you know what I pick to do next."
                $ mc.end_text_convo()
                "A short time later you get another text from [the_person.title] which reads:"
            "Pick your own research":
                mc.name "No, I've got an idea already, just wait for me to decide."
                the_person "Okay."
                $ mc.end_text_convo()
                return
            "Not now":
                mc.name "I don't have time for this right now. I'll get back to you."
                the_person "Okay."
                $ mc.end_text_convo()
                return
    $ mc.start_text_convo(the_person)
    if auto_research_trait_research():
        $ temp_trait = auto_research_trait_research()
        the_person "The research department has refocused to take a look at [temp_trait.name]."
    elif auto_research_trait_unlock():
        $ temp_trait = auto_research_trait_unlock()
        $ temp_number = temp_trait.clarity_cost - mc.free_clarity
        if temp_trait.clarity_cost <= mc.free_clarity:
            $ temp_trait.unlock_trait()
            the_person "The research department used [temp_trait.clarity_cost] clarity to unlock [temp_trait.name] and started researching it."
        else:
            while isinstance(temp_trait, SerumTrait) and temp_trait.clarity_cost > mc.free_clarity:
                the_person "The research department needs [temp_number] more clarity to unlock [temp_trait.name]."
                menu:
                    "Release some clarity /n requires [temp_number] Lust (disabled)" if mc.locked_clarity*2 < temp_number:
                        pass
                    "Release some clarity /n costs [temp_number] Lust" if mc.locked_clarity*2 >= temp_number:
                        mc.name "Give me a few minutes and I can solve that problem."
                        $ mc.end_text_convo()
                        call lust_blowjob_office_label() from _call_lust_blowjob_office_label_auto
                        $ mc.start_text_convo(the_person)
                    "Increase another trait's mastery":
                        mc.name "I can't help you with that right now. Pick a trait to study and increase it's mastery."
                        $ temp_trait = False
                    "Do nothing":
                        mc.name "I'll work on that, for now just do nothing."
                        $ temp_trait = True
    if not temp_trait:
        if auto_research_trait_mastery():
            $ temp_trait = auto_research_trait_mastery()
            the_person "The research department is taking another look at [temp_trait.name] to increase it's Mastery Level." 
    if isinstance(temp_trait, SerumTrait):
        if not temp_trait.unlocked:
            $ temp_trait.unlock_trait()
        $ mc.business.set_serum_research(temp_trait)
    $ mc.end_text_convo()
    python:
        auto_research = Action("Auto Research", auto_research_requirement, "auto_research_label")
        mc.business.mandatory_crises_list.append(auto_research)
    $ del temp_trait
    return

label auto_research_discuss_label(the_person):
    if mc.business.event_triggers_dict.get("auto_research_active", False):
        the_person "I'm currently unlocking and researching traits without input from you. Would you like me to continue?"
        menu:
            "Continue researching":
                mc.name "Yes, this has been great."
            "Stop researching":
                mc.name "No, I want to assign research projects myself."
                $ mc.business.event_triggers_dict["auto_research_active"] = False
                while auto_research in mc.business.mandatory_crises_list:
                    python:
                        mc.business.mandatory_crises_list.remove(auto_research)
    else:
        the_person "I'm not researching anything unless you tell me too. Would you like me start?"
        menu:
            "Start researching":
                mc.name "Yes, I don't have time so you should take care of that."
                $ mc.business.event_triggers_dict["auto_research_active"] = True
                python:
                    auto_research = Action("Auto Research", auto_research_requirement, "auto_research_label")
                    mc.business.mandatory_crises_list.append(auto_research)
            "Not now":
                mc.name "No, I'll continue to assign research projects myself."
    return
