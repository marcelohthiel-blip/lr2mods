init -1 python:
    def traits_by_attention(attention = 0, flaws = 0, serum = []):
        temp_list = []
        exclude_tags = build_exclude_tags(serum)
        for trait in list_of_traits:
            if trait.unlocked and trait.researched and trait.attention <= attention:
                if trait.flaws_aspect <= flaws:
                    if not trait.exclude_tags in exclude_tags:
                        if not trait in serum:
                            if not isinstance(trait, SerumTraitBlueprint):
                                if isinstance(trait, SerumTrait):
                                    temp_list.append(trait)
        return temp_list

    def unlocked_traits():
        temp_list = []
        for trait in list_of_traits:
            if trait.unlocked:
                if not trait.researched:
                    temp_list.append(trait)
        return temp_list

    def max_mental(temp_list):
        aspect = 0
        mental_list = []
        for trait in temp_list:
            if trait.mental_aspect > aspect:
                aspect = trait.mental_aspect
                mental_list = [trait]
            elif trait.mental_aspect == aspect:
                mental_list.append(trait)
        if mental_list:
            return mental_list
        return None

    def max_physical(temp_list):
        aspect = 0
        physical_list = []
        for trait in temp_list:
            if trait.physical_aspect > aspect:
                aspect = trait.physical_aspect
                physical_list = [trait]
            elif trait.physical_aspect == aspect:
                physical_list.append(trait)
        if physical_list:
            return physical_list
        return None

    def max_sexual(temp_list):
        aspect = 0
        sexual_list = []
        for trait in temp_list:
            if trait.sexual_aspect > aspect:
                aspect = trait.sexual_aspect
                sexual_list = [trait]
            elif trait.sexual_aspect == aspect:
                sexual_list.append(trait)
        if sexual_list:
            return sexual_list
        return None

    def max_medical(temp_list):
        aspect = 0
        medical_list = []
        for trait in temp_list:
            if trait.medical_aspect > aspect:
                aspect = trait.medical_aspect
                medical_list = [trait]
            elif trait.medical_aspect == aspect:
                medical_list.append(trait)
        if medical_list:
            return medical_list
        return None

    def suf_mental(temp_list, aspect):
        mental_list = []
        for trait in temp_list:
            if trait.mental_aspect >= aspect:
                mental_list.append(trait)
        if mental_list:
            return mental_list
        return max_mental(temp_list)

    def suf_physical(temp_list, aspect):
        physical_list = []
        for trait in temp_list:
            if trait.physical_aspect >= aspect:
                physical_list.append(trait)
        if physical_list:
            return physical_list
        return max_physical(temp_list)

    def suf_sexual(temp_list, aspect):
        sexual_list = []
        for trait in temp_list:
            if trait.sexual_aspect >= aspect:
                sexual_list.append(trait)
        if sexual_list:
            return sexual_list
        return max_sexual(temp_list)

    def suf_medical(temp_list, aspect):
        medical_list = []
        for trait in temp_list:
            if trait.medical_aspect >= aspect:
                medical_list.append(trait)
        if medical_list:
            return medical_list
        return max_medical(temp_list)

    def max_total_aspect(temp_list):
        max_total = 0
        max_list = []
        for trait in temp_list:
            x = trait.mental_aspect + trait.physical_aspect + trait.sexual_aspect + trait.medical_aspect
            if x > max_total:
                max_total = x
                max_list = [trait]
            else:
                max_list.append(trait)
        return max_list

    #new function to check max price at current market if max_list is > 1

    def build_exclude_tags(temp_list):
        exclude_tags = []
        for trait in temp_list:
            if trait.exclude_tags:
                exclude_tags.append(trait.exclude_tags)
        return exclude_tags
        
    def total_flaws(temp_list):
        x = 0
        for trait in temp_list:
            x += trait.flaws_aspect
        return x

    def serum_for_contract(contract, max_path = True, suf_path = True):
        max_complete = False
        suf_complete = False
        effective_attention = contract.attention
        if attention_floor_increase_1_policy.is_active:
            effective_attention += 1
        if attention_floor_increase_2_policy.is_active:
            effective_attention += 1
        max_serum = []
        suf_serum = []
        while max_path or suf_path:
            aspect_list = [[contract.mental_aspect, "mental"], [contract.physical_aspect, "physical"], [contract.sexual_aspect, "sexual"], [contract.medical_aspect, "medical"]]
            max_sorted_list = sorted(aspect_list.copy())
            suf_sorted_list = sorted(aspect_list.copy())
            flaw_allowance = contract.flaws_aspect
            if effective_attention >= 2 and futuristic_serum_prod.researched:
                slots = 7
                max_serum.append(futuristic_serum_prod)
                suf_serum.append(futuristic_serum_prod)
            elif effective_attention >= 1 and advanced_serum_prod.researched:
                slots = 5
                max_serum.append(advanced_serum_prod)
                suf_serum.append(advanced_serum_prod)
            elif improved_serum_prod.researched:
                slots = 3
                max_serum.append(improved_serum_prod)
                suf_serum.append(improved_serum_prod)
            else:
                slots = 2
                max_serum.append(primitive_serum_prod)
                suf_serum.append(primitive_serum_prod)
            temp_flaw = 0
            trait = max_serum[0]
            # renpy.say(None, trait.name)
            aspect_list[0][0] -= trait.mental_aspect
            aspect_list[1][0] -= trait.physical_aspect
            aspect_list[2][0] -= trait.sexual_aspect
            aspect_list[3][0] -= trait.medical_aspect
            if max_path:
                max_path = False
                while slots > 0:
                    temp_flaw = 0
                    while temp_flaw <= flaw_allowance and slots > 0:
                        pruned_traits = traits_by_attention(attention = effective_attention, flaws = flaw_allowance, serum = max_serum)
                        if len(pruned_traits) < slots:
                            slots = len(pruned_traits) -1
                        aspect = max_sorted_list[0][1]
                        if aspect == "mental":
                            traits = max_mental(pruned_traits)
                        elif aspect == "physical":
                            traits = max_physical(pruned_traits)
                        elif aspect == "sexual":
                            traits = max_sexual(pruned_traits)
                        elif aspect == "medical":
                            traits = max_medical(pruned_traits)
                        if traits:
                            trait = get_random_from_list(max_total_aspect(traits))
                            if trait.name == "High Capacity Design":
                                slots += 2
                            # renpy.say(None, "max " + trait.name)
                            max_serum.append(trait)
                            aspect_list[0][0] -= trait.mental_aspect
                            aspect_list[1][0] -= trait.physical_aspect
                            aspect_list[2][0] -= trait.sexual_aspect
                            aspect_list[3][0] -= trait.medical_aspect
                            flaw_allowance -= trait.flaws_aspect
                            temp_flaw = 0
                            slots -= 1
                        else:
                            temp_flaw += 1
                        max_sorted_list = sorted(aspect_list.copy())
                        x = 3
                        while x > -1:
                            if max_sorted_list[x][0] < 1:
                                max_sorted_list.pop(x)
                            x -=1
                        if not max_sorted_list:
                            max_complete = True
                            max_sorted_list = [[1, "mental"], [1, "physical"], [1, "sexual"], [1, "medical"]]
            elif suf_path:
                suf_path = False
                while slots > 0:
                    temp_flaw = 0
                    while temp_flaw <= flaw_allowance and slots > 0:
                        pruned_traits = traits_by_attention(attention = effective_attention, flaws = flaw_allowance, serum = suf_serum)
                        if len(pruned_traits) < slots:
                            # renpy.say(None, "short pruned list")
                            slots = len(pruned_traits) -1
                        aspect = suf_sorted_list[0][1]
                        target = suf_sorted_list[0][0]
                        if aspect == "mental":
                            traits = suf_mental(pruned_traits, target)
                        elif aspect == "physical":
                            traits = suf_physical(pruned_traits, target)
                        elif aspect == "sexual":
                            traits = suf_sexual(pruned_traits, target)
                        elif aspect == "medical":
                            traits = suf_medical(pruned_traits, target)
                        if traits:
                            trait = get_random_from_list(max_total_aspect(traits))
                            if trait.name == "High Capacity Design":
                                slots += 2
                            # renpy.say(None, "suf " + trait.name)
                            suf_serum.append(trait)
                            aspect_list[0][0] -= trait.mental_aspect
                            aspect_list[1][0] -= trait.physical_aspect
                            aspect_list[2][0] -= trait.sexual_aspect
                            aspect_list[3][0] -= trait.medical_aspect
                            flaw_allowance -= trait.flaws_aspect
                            temp_flaw = 0
                            slots -= 1
                        else:
                            # renpy.say(None, "suf flaw +1")
                            temp_flaw += 1
                        suf_sorted_list = sorted(aspect_list.copy())
                        x = 3
                        while x > -1:
                            # renpy.say(None, "popping suf " + str(x))
                            if suf_sorted_list[x][0] < 1:
                                suf_sorted_list.pop(x)
                            x -=1
                        if not suf_sorted_list:
                            suf_complete = True
                            suf_sorted_list = [[1, "mental"], [1, "physical"], [1, "sexual"], [1, "medical"]]
        if max_complete or suf_complete:
            if max_complete:
                if suf_complete:
                    if len(suf_serum) > len(max_serum):
                        serum = suf_serum
                    else:
                        serum = max_serum
                else:
                    serum = max_serum
            else:
                serum = suf_serum
            return serum, None
        elif len(max_serum) >= len(suf_serum):
            return max_serum, max_sorted_list
        return suf_serum, suf_sorted_list

init 3 python:
    def serum_builder_requirement():
        if mc.business.is_open_for_business:
            if mc.business.active_contracts or mc.business.offered_contracts:
                return True
            return "Wait for contracts to be offered"
        return "Wait for business to be open"

    def serum_builder_initialization(self):
        m_division.add_action(self)
        return

    def contract_menu(temp_list):
        contract_list = []
        for x in temp_list:
            contract_list.append([x.name, x])
        contract_list.append(["Back", "Back"])
        return contract_list
    
    def missing_aspect_text(sorted_list):
        x = len(sorted_list) - 1
        y = len(sorted_list) - 1
        while x >= 0:
            number = sorted_list[x][0]
            if number <= 0:
                y -= 1
            x -= 1
        text = ""
        x = len(sorted_list) - 1
        while x >= 0:
            number = sorted_list[x][0]
            if number > 0:
                number = str(sorted_list[x][0])
                label = sorted_list[x][1]
                text = text + number + " more " + label + " aspect"
                if y >= 1:
                    text = text + ", "
                if y == 1:
                    text = text + "and "
                y -= 1
            x -= 1
        return text

    serum_builder_action = ActionMod("Build a serum", serum_builder_requirement, "serum_builder_label", initialization = serum_builder_initialization,
        menu_tooltip = "Build a serum for a contract.", category = "Business Action")

init 4 python:
    def market_demand_requirement():
        if mc.business.is_open_for_business:
            if mc.business.market_team:
                if mc.is_at_office:
                    if lowest_demand():
                        return True
        return False

    def lowest_demand():
        temp_serum = None
        x = 1.00
        for line in mc.business.production_lines:
            if line.selected_design and line.selected_design.market_demand < x:
                x = line.selected_design.market_demand
                temp_serum = line.selected_design
        if x < 0.50:
            return temp_serum
        return None

    def clear_production_line(the_serum):
        for line in mc.business.production_lines:
            if line.selected_design == the_serum:
                line.clear_product()
        return

    market_demand_action = ActionMod("Market Demand", market_demand_requirement, "market_demand_label",
        menu_tooltip = "Get informed that market demand for serums in production is too low.",
        category = "Business Crisis", is_crisis = True, priority = 10)

label serum_builder_label():
    $ active = len(mc.business.active_contracts)
    $ offered = len(mc.business.offered_contracts)
    "You currently have [active] active contracts and [offered] offered contracts."
    menu:
        "Active" if active > 0:
            $ contract_list = contract_menu(mc.business.active_contracts)
        "Offered" if offered > 0:
            $ contract_list = contract_menu(mc.business.offered_contracts)
        "Back":
            return
    $ contract = menu(contract_list)
    if not contract == "Back":
        $ serum_design, sorted_list = serum_for_contract(contract)
        if sorted_list:
            "A serum could not be built for this contract. The closest design will still display."
            $ temp_text = missing_aspect_text(sorted_list)
            "To fulfil this contract you need traits with [temp_text]."
            if sorted_list[0][1] == "mental":
                $ traits = max_mental(unlocked_traits())
            elif sorted_list[0][1] == "physical":
                $ traits = max_physical(unlocked_traits())
            elif sorted_list[0][1] == "sexual":
                $ traits = max_sexual(unlocked_traits())
            elif sorted_list[0][1] == "medical":
                $ traits = max_medical(unlocked_traits())
            if traits:
                $ trait = get_random_from_list(max_total_aspect(traits))
                "You might want to start by researching [trait.name]."
            else:
                "You might need to advance to your next research tier to find one."
        if serum_design:
            call serum_design_action_description(SerumDesign.clone_serum(contract.name, serum_design)) from _call_serum_design_description_builder
        else:
            "Unable to build a serum for this contract."
    return

label market_demand_label():
    $ scene_manager = Scene()
    if mc.business.company_model:
        $ the_person = mc.business.company_model
    else:
        $ the_person = get_random_from_list(mc.business.market_team)
    $ contract = None
    $ the_serum = lowest_demand()
    if not the_serum or not the_person:
        "MARKET DEMAND FAILED"
        return
    if mc.location == m_division:
        "As you work [the_person.possessive_title] approaches you, it looks like she has something to tell you."
    else:
        "As you work you get a text from [the_person.possessive_title] in marketing. It looks like she wants you to come see her."
        $ mc.change_location(m_division)
        "When you get there you quickly move over to [the_person.title]."
    $ scene_manager.add_actor(the_person, emotion = "sad")
    mc.name "Yes? How can I help you?"
    the_person "I've noticed a bit of a problem. Our customers just don't seem to be interested in buying [the_serum.name] anymore."
    $ temp_number = round(the_serum.market_demand * 100)
    the_person "Its market demand is down to [temp_number]%% and production just keeps sending us more."
    $ x = len(mc.business.active_contracts)-1
    while x > -1 and not contract:
        if mc.business.active_contracts[x]:
            $ test_contract = mc.business.active_contracts[x]
            if lowest_demand() in get_designs_that_satisfy_contract(test_contract):
                $ contract = mc.business.active_contracts[x]
        $ x-=1
    $ x = len(mc.business.offered_contracts)-1
    while x > -1 and not contract:
        if mc.business.offered_contracts[x]:
            $ test_contract = mc.business.offered_contracts[x]
            if lowest_demand() in get_designs_that_satisfy_contract(test_contract):
                $ contract = mc.business.offered_contracts[x]
        $ x-=1
    if contract:
        the_person "I suppose we could keep making them for contracts like the [contract.name] one, but our general customers don't want it."
    menu:
        "Thank her":
            mc.name "I understand. I'll talk to production about refocusing on something that will be easier to sell."
            $ scene_manager.update_actor(the_person, emotion = "happy")
        "Get upset":
            mc.name "Are you questioning me?"
            the_person "What?"
            mc.name "This is my business, and if I want the production department to make a serum they will make it."
            the_person "I know.. But..."
            if office_punishment.is_active:
                menu:
                    "Spank her now" if corporal_punishment.is_active:
                        mc.name "No buts... Well actually..."
                        mc.name "Get over here, there is one butt that seems like it needs some attention."
                        if not strict_enforcement.is_active:
                            call punishment_spank(the_person, Infraction.bureaucratic_mistake_factory()) from _call_punishment_spank_serum
                        else:
                            call punishment_strip_and_spank(the_person, Infraction.bureaucratic_mistake_factory()) from _call_punishment_spank_serum2
                    "Punish her for insubordination later":
                        mc.name "No buts, I'm in charge you just work here. I think I'm going to have to write you up for insubordination."
                        the_person "But..."
                        "Seeing your glare [the_person.possessive_title] trails off."
                        the_person "Yes [the_person.mc_title]. Whatever you need to do."
                        if the_person.obedience < 150:
                            $ the_person.change_stats(obedience = 3, happiness = -5, love = -1)
                        else:
                            $ the_person.change_stats(obedience = 2)
                        $ the_person.add_infraction(Infraction.bureaucratic_mistake_factory())
                    "Let it go":
                        mc.name "But nothing. Get back to work."
            else:
                mc.name "But nothing. Get back to work."
    $ clear_scene
    "Would you like to visit the production department now?"
    menu:
        "Go now":
            $ clear_production_line(the_serum)
            $ mc.change_location(p_division)
            if mc.business.production_team:
                $ the_person = get_random_from_list(mc.business.production_team)
                # $ scene_manager.add_actor(the_person, emotion = "happy")
                # talk to someone
            call production_select_action_description() from _call_production_select_action_description_market
        "Deal with it later":
            "You decide to just get back to work, but make a note to investigate more later."
    $ clear_scene
    return
