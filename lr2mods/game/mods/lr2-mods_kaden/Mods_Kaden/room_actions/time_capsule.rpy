init -1:
    default persistent.time_capsule = []
    default persistent.lactation_serum = []

init 3 python:
    def hidden_trait_list():
        hidden_trait_list = []
        for trait in [x for x in SerumTraitMod._instances]:
            hidden_trait_list.append(trait)
        if "nora_reward_instant_trance" in globals():
            hidden_trait_list.append(nora_reward_instant_trance)
        if "nora_reward_hucow_trait" in globals():
            hidden_trait_list.append(nora_reward_hucow_trait)
        if "nora_reward_genius_trait" in globals():
            hidden_trait_list.append(nora_reward_genius_trait)
        if "nora_reward_high_slut_trait" in globals():
            hidden_trait_list.append(nora_reward_high_slut_trait)
        if "nora_reward_high_obedience_trait" in globals():
            hidden_trait_list.append(nora_reward_high_obedience_trait)
        if "nora_reward_low_love_trait" in globals():
            hidden_trait_list.append(nora_reward_low_love_trait)
        if "nora_reward_high_love_trait" in globals():
            hidden_trait_list.append(nora_reward_high_love_trait)
        if "nora_reward_nora_trait" in globals():
            hidden_trait_list.append(nora_reward_nora_trait)
        if "nora_reward_aunt_trait" in globals():
            hidden_trait_list.append(nora_reward_aunt_trait)
        if "nora_reward_cousin_trait" in globals():
            hidden_trait_list.append(nora_reward_cousin_trait)
        if "nora_reward_sister_trait" in globals():
            hidden_trait_list.append(nora_reward_sister_trait)
        if "nora_reward_mother_trait" in globals():
            hidden_trait_list.append(nora_reward_mother_trait)
        if "arousal_serum_trait" in globals():
            hidden_trait_list.append(arousal_serum_trait)
        if "body_monitor_serum_trait" in globals():
            hidden_trait_list.append(body_monitor_serum_trait)
        if "anti_bimbo_serum_trait" in globals():
            hidden_trait_list.append(anti_bimbo_serum_trait)
        if "energy_drink_serum_trait" in globals():
            hidden_trait_list.append(energy_drink_serum_trait)
        if "essential_oil_trait" in globals():
            hidden_trait_list.append(essential_oil_trait)
        if "fetish_basic_serum" in globals():
            hidden_trait_list.append(fetish_basic_serum)
        if "fetish_exhibition_serum" in globals():
            hidden_trait_list.append(fetish_exhibition_serum)
        if "fetish_anal_serum" in globals():
            hidden_trait_list.append(fetish_anal_serum)
        if "fetish_cum_serum" in globals():
            hidden_trait_list.append(fetish_cum_serum)
        if "fetish_breeding_serum" in globals():
            hidden_trait_list.append(fetish_breeding_serum)
        if "massive_pregnancy_decelerator_serum_trait" in globals():
            hidden_trait_list.append(massive_pregnancy_decelerator_serum_trait)
        if "nocturnal_emission_actuator_serum_trait" in globals():
            hidden_trait_list.append(nocturnal_emission_actuator_serum_trait)
        return hidden_trait_list

    def find_hidden_trait(name):
        for trait in [x for x in hidden_trait_list()]:
            if trait.name == name:
                return trait
        return False

    def create_time_serum(serum):
        time_capsule = []
        lactation_serum = []
        for trait in serum.traits:
            time_capsule.append(trait.name)
            if isinstance(trait.on_apply, functools.partial):
                if isinstance(trait.on_apply.args[0], SerumDesign):
                    lactation_serum = create_time_serum(trait.on_apply.args[0])[0]
        return [time_capsule, lactation_serum]

    def get_time_serum():
        temp_list = []
        list2 = []
        list2 = hidden_trait_list()
        temp_list = persistent.time_capsule
        time_serum = SerumDesign()
        time_serum.name = "Time Serum"
        if temp_list:
            for y in temp_list:
                for x in list_of_traits:
                    if x.name == y:
                        time_serum.add_trait(x)
        if temp_list and list2:
            for y in temp_list:
                for x in list2:
                    if x.name == y:
                        time_serum.add_trait(x)
        if persistent.lactation_serum:
            lactation_serum = get_lactation_serum()
            new_trait = SerumTrait(*breast_milk_serum_production.given_args, **breast_milk_serum_production.given_kwargs)
            time_serum.add_trait(new_trait)
            time_serum.traits[len(time_serum.traits)-1].on_apply = partial(breast_milk_serum_production_on_apply, lactation_serum)
            time_serum.traits[len(time_serum.traits)-1].on_remove = partial(breast_milk_serum_production_on_remove, lactation_serum)
        time_serum.attention_modifier = -4
        return time_serum

    def get_lactation_serum():
        temp_list = []
        list2 = []
        list2 = hidden_trait_list()
        temp_list = persistent.lactation_serum
        lactation_serum = SerumDesign()
        lactation_serum.name = "Lactation Serum"
        if temp_list:
            for y in temp_list:
                for x in list_of_traits:
                    if x.name == y:
                        lactation_serum.add_trait(x)
        if temp_list and list2:
            for y in temp_list:
                for x in list2:
                    if x.name == y:
                        lactation_serum.add_trait(x)
        return lactation_serum

init 16 python: # hijack
    def attic_search_event_requirement():
        if mc.is_home:
            if not mc.business.event_triggers_dict.get("time_capsule_discovered", False):
                return True
        return False

    attic_search_event_action = ActionMod("Search the attic", attic_search_event_requirement, "activate_attic_search",
        menu_tooltip = "Discover something weird in your attic.", category = "Home", is_crisis = True, is_morning_crisis = True, priority = 100)

    def attic_search_requirement():
        return mc.business.event_triggers_dict.get("time_capsule_discovered", False)

    add_label_hijack("mom_found_serums", "activate_attic_mod_core")

init 12 python:
    def super_serum():
        time_serum = []
        time_serum.append(futuristic_serum_prod.name)
        time_serum.append(mind_control_agent.name)
        mpa = next((x for x in list_of_traits if x == massive_pregnancy_accelerator), None)
        if mpa:
            time_serum.append(mpa.name)
        sgs = next((x for x in list_of_traits if x == self_generating_serum), None)
        if sgs:
            time_serum.append(sgs.name)
        time_serum.append(low_volatility_reagents.name)
        time_serum.append(rolling_orgasm.name)
        time_serum.append(slutty_caffeine_trait.name)
        time_serum.append(happiness_tick.name)
        time_serum.append(improved_duration_trait.name)
        time_serum.append(focus_enhancement.name)
        time_serum.append(int_enhancement.name)
        time_serum.append(cha_enhancement.name)
        time_serum.append("Behaviour Adjustment")
        time_serum.append(nora_reward_aunt_trait.name)
        time_serum.append(nora_reward_genius_trait.name)
        time_serum.append(nora_reward_instant_trance.name)
        time_serum.append("Dopamine Therapy")
        time_serum.append("Body Monitoring Nanobots")
        time_serum.append("Sexual Proclivity Nanobots")
        time_serum.append("Social Sexual Proclivity Nanobots")
        time_serum.append("Energy Drink")
        time_serum.append("Skin Sensitivity")
        time_serum.append("Teasing Nightfall")
        if "arousal_serum_trait" in globals():
            time_serum.append(arousal_serum_trait.name)
        setattr(persistent, "time_capsule", time_serum)
        mc.business.event_triggers_dict["time_capsule"] = 100
        mc.business.event_triggers_dict["time_capsule_locked"] = False
        return

label activate_attic_mod_core(stack):
    $ mc.business.add_mandatory_morning_crisis(attic_search_event_action)
    python:
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label activate_attic_search():
    python:
        attic_search_action = Action("Search the attic", attic_search_requirement, "attic_search_label", menu_tooltip = "Look for more serums in the attic")
        bedroom.add_action(attic_search_action)
        mc.business.event_triggers_dict["time_capsule_discovered"] = True
    "Suddenly you are struck by a thought."
    "[mom.possessive_title!c] already found a box of serums you hid in the attic last year, but maybe she missed some."
    "With that thought to drive you, you go up the stairs to the attic and see that it is full of boxes."
    "After some searching you find a weird metal case labelled TIME CAPSULE, but oddly the date emblazoned on the side is today."
    "It also seems to be bolted to the floor, a bit like a safe."
    if not persistent.time_capsule:
        "Does that mean that it has been up here for years and is meant to be opened? It feels empty."
    else:
        $ mc.business.event_triggers_dict["time_capsule"] = 100
        "Does that mean that it has been up here for years and is meant to be opened? It feels heavy."
    "Before you are able to investigate further, you hear your alarm going off downstairs."
    "You better get the day started, but if you want to check this out again, you should be able to do so from your bedroom."
    return

label attic_search_label():
    "You go up the stairs to the attic and quickly make your way to the odd time capsule."
    $ count = mc.business.event_triggers_dict.get("time_capsule", 0)
    if mc.business.event_triggers_dict.get("time_capsule_locked", False):
        "You mess with the outside of the case for a bit but as easy as it was to open before you can't seem to find a way to open it now."
    menu:
        "Open the case" if not mc.business.event_triggers_dict.get("time_capsule_locked", False):
            if not mc.business.event_triggers_dict.get("time_capsule_opened", False):
                $ mc.business.event_triggers_dict["time_capsule_opened"] = True
                if count < 1:
                    "You were right, the case is empty. However, as you look at it you notice something about the way it is designed."
                    "Trusting your instincts you reach into your pocket you pull out a serum vial."
                    "Sure enough it is a perfect fit. The entire case is lined with slots that would securely hold the exact vials that your serums get produced to fill."
                else:
                    "You were right, the case is packed full. To your great surprise the contents are incredibly familiar."
                    "Trusting your instincts you reach into your pocket you pull out a serum vial."
                    "Sure enough it is identical. The entire case is stocked with the exact vials that your serums get produced to fill."
                    "Oddly the colour is a bit different than any of the serums you currently produce."
            else:
                if count < 1:
                    "The case is still empty, you don't really know what else you expected."
                else:
                    "The case is still full, you don't really know what else you expected."
            menu:
                "Fill the case" if mc.inventory.total_serum_count > 0 and count < 1:
                    call screen serum_inventory_select_ui(mc.inventory)
                    if isinstance(_return, SerumDesign):
                        $ serum = _return
                        "You select a vial of [serum.name] and snap it into place in the case."
                        "Suddenly it makes a hissing noise and starts to close slowly."
                        "You certainly won't be able to fill the case but you could probably retrieve the one you put in if you want."
                        menu:
                            "Retrieve the vial":
                                "You stick your hand in and pull the vial out, as soon as you do it stops closing."
                                "It seems like there is more than meets the eye to this case, but before messing with it more you decide to wait a bit."
                            "Let it close":
                                $ mc.inventory.change_serum(serum,-1)
                                $ [time_serum, lactation_serum] = create_time_serum(serum)
                                $ mc.business.event_triggers_dict["time_capsule_locked"] = True
                                $ mc.business.event_triggers_dict["time_capsule"] = 100
                                python:
                                    setattr(persistent, "time_capsule", time_serum)
                                    setattr(persistent, "lactation_serum", lactation_serum)
                                "You watch as the case closes the rest of the way and then listen as what sounds like a dozen locks spin into place. The case is surely secure for now."
                                "You wonder how you ever got it open in the first place..."
                    else:
                        "You change your mind for now."
                "Empty the case" if count > 0:
                    $ mc.inventory.change_serum(get_time_serum(), 99)
                    "You spend some time pulling vials from the case but as you are setting the second to last vial in your bag the case starts to make a hissing noise and begins closing."
                    menu:
                        "Grab the last one":
                            $ mc.inventory.change_serum(get_time_serum(), 1)
                            $ mc.business.event_triggers_dict["time_capsule"] = 0
                            "You quickly grab at the last vial, but as soon as you pick it up the case stops moving."
                            "It sits there almost like it is waiting for you to put something inside."
                        "Let it close":
                            $ mc.business.event_triggers_dict["time_capsule_locked"] = True
                            "You watch as the case closes the rest of the way and then listen as what sounds like a dozen locks spin into place. The case is surely secure for now."
                            "You wonder how you ever got it open in the first place..."
                "Leave it alone":
                    pass
        "Leave it alone":
            pass
    "You head back down the stairs and return to your room."
    return
