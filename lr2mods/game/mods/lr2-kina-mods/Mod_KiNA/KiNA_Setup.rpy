#Counter = KS01

#Shamelessly adapted from zenupstart's mod. And thanks sir.us for help solving the mystery


default beautify_enabled = False
default static_opinion_enabled = False
default child_support_enabled = False
default cs_amount = 50
default auto_skill_enabled = False
default skill_check_delay = 14

init 100 python:

    def makeup_changed(is_enabled = False):
        global beautify_enabled
        beautify_enabled = is_enabled

        if (is_enabled):
            #Mom
            if hasattr(mom, 'base_outfit'):
                mom.base_outfit.add_accessory(lipstick.get_copy(), [.78, .03, .08, 0.4])
                mom.base_outfit.add_accessory(light_eye_shadow.get_copy(), [.38, .12, .15, 0.75])
                mom.base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.48, .09, .07, .5])
                mom.base_outfit.add_accessory(blush.get_copy(), [.89, .26, .20, .33])
            else:
                mom_base = Outfit("Jennifer's accessories")
                mom_base.add_accessory(lipstick.get_copy(), [.78, .03, .08, 0.4])
                mom_base.add_accessory(light_eye_shadow.get_copy(), [.38, .12, .15, 0.75])
                mom_base.add_accessory(heavy_eye_shadow.get_copy(), [.48, .09, .07, .5])
                mom_base.add_accessory(blush.get_copy(), [.89, .26, .20, .33])
            mom.apply_planned_outfit()                   

            # KiNA's preferences
            if day == 0: mom.age = 41                    # Fixed age... as youngest as the her age range allowed 
            mom.tan_style = None            #[no_tan, normal_tan, sexy_tan, one_piece_tan, slutty_tan]
            mom.pubes_style = default_pubes # shaved_pubes, landing_strip_pubes, diamond_pubes, trimmed_pubes, or default_pubes
            mom.pubes_style.colour = mom.hair_style.colour

            #Lily
            if hasattr(lily, 'base_outfit'):
                lily.base_outfit.add_accessory(lipstick.get_copy(), [.96, .29, .54, 0.4])
                lily.base_outfit.add_accessory(light_eye_shadow.get_copy(), [0, .26, .36, 0.5])
                lily.base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.29, .33, .12, .33])
                lily.base_outfit.add_accessory(blush.get_copy(), [.89, .26, .2, .5])
            else:
                lily_base = Outfit("Lily's accessories")
                lily_base.add_accessory(lipstick.get_copy(), [.96, .29, .54, 0.4])
                lily_base.add_accessory(light_eye_shadow.get_copy(), [0, .26, .36, 0.5])
                lily_base.add_accessory(heavy_eye_shadow.get_copy(), [.29, .33, .12, .33])
                lily_base.add_accessory(blush.get_copy(), [.89, .26, .2, .5])
            lily.apply_planned_outfit()

            # KiNA's preferences
            lily.tan_style = None
            lily.pubes_style = shaved_pubes
            lily.pubes_style.colour = lily.hair_style.colour

            #Set MC to her 1st everything as a nod to LR1
            if vt_enabled() and day == 0:
                if not lily.oral_virgin == 0:
                    lily.oral_first = mc.name
                if not lily.vaginal_virgin == 0:
                    lily.vaginal_first = mc.name
                if not lily.anal_virgin == 0:
                    lily.anal_first = mc.name

            #Aunt
            if hasattr(aunt, 'base_outfit'):
                aunt.base_outfit.add_accessory(lipstick.get_copy(), [.96, .29, .54, 0.4])
                aunt.base_outfit.add_accessory(light_eye_shadow.get_copy(), [.38, .12, .15, 0.75])
                aunt.base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.48, .09, .07, .5])
                aunt.base_outfit.add_accessory(blush.get_copy(), [.89, .26, .20, .33])
            else:
                aunt_base = Outfit("Rebecca's accessories")
                aunt_base.add_accessory(lipstick.get_copy(), [.96, .29, .54, 0.4])
                aunt_base.add_accessory(light_eye_shadow.get_copy(), [.38, .12, .15, 0.75])
                aunt_base.add_accessory(heavy_eye_shadow.get_copy(), [.48, .09, .07, .5])
                aunt_base.add_accessory(blush.get_copy(), [.89, .26, .20, .33])
            aunt.apply_planned_outfit()

            # KiNA's preferences
            if day == 0:
                aunt.tan_style = sexy_tan
                aunt.pubes_style = diamond_pubes
                aunt.pubes_style.colour = aunt.hair_style.colour
                #They picked the weirdest names
                aunt.last_name = renpy.random.choice(["Smiths", "Weasley", "Jackson", "Clinton", "Adams", "Brown", "Cassidy", "Daniels", "Grant", "Lloyds", "Hamilton", "Peters", "Parkers", "Roberts", "White", "Harris", "Lee", "Black", "Rice", "Winstone"])
                cousin.last_name = aunt.last_name
                aunt.home.name = str(aunt.name + " " + aunt.last_name)
                aunt.home.formal_name = str(aunt.name + " " + aunt.last_name)

            #Steph
            if hasattr(stephanie, 'base_outfit'):
                stephanie.base_outfit.add_accessory(lipstick.get_copy(), [.38, .12, .15, .4])
                stephanie.base_outfit.add_accessory(light_eye_shadow.get_copy(), [.15, .15, .15, .8])
                stephanie.base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.38, .12, .15, .95])
                stephanie.base_outfit.add_accessory(blush.get_copy(), [.80, .06, .24, .5])
            else:
                steph_base = Outfit("Stephanie's accessories")
                steph_base.add_accessory(lipstick.get_copy(), [.38, .12, .15, .4])
                steph_base.add_accessory(light_eye_shadow.get_copy(), [.15, .15, .15, .8])
                steph_base.add_accessory(heavy_eye_shadow.get_copy(), [.38, .12, .15, .95])
                steph_base.add_accessory(blush.get_copy(), [.80, .06, .24, .5])
            stephanie.apply_planned_outfit()

            # KiNA's preferences
            # stephanie.love = 10 #Seems to not needed after all
            if day == 0:
                stephanie.tan_style = slutty_tan
                stephanie.pubes_style = default_pubes            
                stephanie.pubes_style.colour = stephanie.hair_style.colour
                stephanie.last_name = renpy.random.choice(["Harris", "Johnson", "King", "Lee", "Martin", "Newman", "Quinn", "Sanders", "Simmons", "Summers", "Thomas", "Williams", "Gonzalez", "Martinez", "Cruz", "Paqueta", "Hernandez", "Rodriguez", "Cummins"])
                ashley.last_name = stephanie.last_name
                stephanie.home.name = str(stephanie.name + " " + stephanie.last_name)
                stephanie.home.formal_name = str(stephanie.name + " " + stephanie.last_name)

            #Sarah
            if hasattr(sarah, 'base_outfit'):
                sarah.base_outfit.add_accessory(lipstick.get_copy(), [.78, .03, .08, 0.5])
                sarah.base_outfit.add_accessory(light_eye_shadow.get_copy(), [.15, .15, .15, .8])
                sarah.base_outfit.add_accessory(heavy_eye_shadow.get_copy(), [.38, .12, .15, .95])
                sarah.base_outfit.add_accessory(blush.get_copy(), [.80, .06, .24, .5])
            else:
                sarah_base = Outfit("Sarah's accessories")
                sarah_base.add_accessory(lipstick.get_copy(), [.78, .03, .08, 0.5])
                sarah_base.add_accessory(light_eye_shadow.get_copy(), [.15, .15, .15, .8])
                sarah_base.add_accessory(heavy_eye_shadow.get_copy(), [.38, .12, .15, .95])
                sarah_base.add_accessory(blush.get_copy(), [.80, .06, .24, .5])
            sarah.apply_planned_outfit()
        return

    def makeup_requirement():
        return True

#----------------------------

    def static_changed(is_enabled = False):
        global static_opinion_enabled
        static_opinion_enabled = is_enabled

        #Mom
        #At least 1 must be love
        
        options = ["dresses", "skirts", "pants"]
        preferred = options[renpy.random.randint(0,2)]
        hate = options[renpy.random.randint(0,2)]
        mom.set_opinion(preferred, 2, False)
        if not preferred == hate:
            mom.set_opinion(hate, -2, False)
            
                
        #Ensure these not negative opinions
        for opinion in [
            "yoga",
            "sports",
            "giving blowjobs",
            "getting head",
            "anal sex",
            "doggy style sex",
            "sex standing up"]:
            if (mom.get_opinion_score(opinion) < 0):
                mom.set_opinion(opinion, renpy.random.randint(0, 2), False)

        #Always love
        for opinion in [ 
            "makeup",
            "small talks",
            "kissing",
            "giving tit fucks",
            "being fingered",
            "vaginal sex",
            "missionary style sex",
            "conservative outfits", 
            "jazz",
            "high heels"]:
            mom.set_opinion(opinion, 2, False)
            #mom.max_opinion_score(opinion, add_to_log = False)  #Works, but then set it to know

        #Always hate
        for opinion in [
            "boots",
            "heavy metal music",
            "punk music",
            "skimpy uniforms", 
            "skimpy outfits", 
            "the colour orange", 
            "incest",
            "anal creampies",
            "threesomes",
            "cheating on men"]:
            mom.set_opinion(opinion, -2, False)


        # Set normal opinion as known, we've been living together for a long time
        opinion = mom.get_normal_opinions_list()
        for topic in opinion:
            if not mom.opinion(topic) == 0:
                mom.set_opinion(topic, mom.get_opinion_score(topic), True)
                mc.stats.change_tracked_stat("Girl", "Opinion Discovered", 1)

        #Sis
        
        for opinion in [
            "makeup", 
            "small talks", 
            "skirts",
            "pants",
            "the colour brown",
            "pop music",
            "kissing",
            "giving blowjobs",
            "vaginal sex",
            "anal sex",
            "missionary style sex", 
            "sex standing up"]:
            if (lily.get_opinion_score(opinion) < 0):
                lily.set_opinion(opinion, renpy.random.randint(0, 2), False)

        for opinion in [
            "skimpy outfits",
            "lingerie", 
            "flirting",
            "masturbating",
            "getting head",
            "being fingered",
            "doggy style sex",           
            "being submissive"]:
            lily.set_opinion(opinion, 2, False)
            #lily.max_opinion_score(opinion)

        for opinion in [
            "conservative outfits",
            "taking control", 
            "the colour orange",
            "cheating on men",
            "incest",
            "threesomes"]:
            lily.set_opinion(opinion, -2, False)

        # Set normal opinion as known, we've been living together for a long time
        opinion = lily.get_normal_opinions_list()
        for topic in opinion:
            if not lily.opinion(topic) == 0:
                lily.set_opinion(topic, lily.get_opinion_score(topic), True)
                mc.stats.change_tracked_stat("Girl", "Opinion Discovered", 1)

        #Steph
        # 50% chance to know her normal preferences
        opinion = stephanie.get_normal_opinions_list()
        for topic in opinion:
            if renpy.random.randint(0, 1) == 1:                     
                if not stephanie.opinion(topic) == 0:
                    stephanie.set_opinion(topic, stephanie.get_opinion_score(topic), True)
                    mc.stats.change_tracked_stat("Girl", "Opinion Discovered", 1)
            
        mc.log_event("Mom and Sis opinions have been tweaked.", "float_text_grey")

        return

    def static_requirement():
        return True

#----------------------------

    def southern_accent_toggle(is_enabled = True):    #Ellie's accent toggle
        if (is_enabled):
            ellie.text_modifiers.remove(southern_belle)
            mc.log_event("Ellie talks normally", "float_text_grey")
        else:
            ellie.text_modifiers.append(southern_belle)
            mc.log_event("Ellie talks with heavy southern accent", "float_text_grey")

        is_enabled = not is_enabled
        return True
        
    def accent_requirement():
        return True

#----------------------------

    def narrative_bugfix(is_enabled = True): 
        if (is_enabled):
            if day == 0:
                camila.on_birth_control = False
                ellie.on_birth_control = False
                ellie.set_opinion("conservative outfits", 2, False)
                ellie.set_opinion("skimpy outfits", -2, False)
                ellie.set_opinion("skimpy uniforms", -2, False)
                mc.log_event("Setting Camila and Ellie on no BC for narrative reason.", "float_text_grey")
        else:
            if day == 0:
                mc.log_event("Deal with the consequences.", "float_text_grey")
            else:
                mc.log_event("Too late... Should done it at start of the game.", "float_text_grey")

        is_enabled = not is_enabled
        return True
        
    def bugfix_requirement():
        return True

#----------------------------

    def child_support_toggle(is_enabled = False):
        global child_support_enabled
        global cs_amount
        
        child_support_enabled = is_enabled

        if (is_enabled):
            #ceo_office.add_action(self)
            mc.log_event("Set the amount paid at your bedroom.", "float_text_grey")
        else:
            #ceo_office.remove_action(self)
            mc.log_event("No Child Support.", "float_text_grey")
        return

    def cs_requirement():
        return (persistent.pregnancy_pref == 3)

    def cs_setting_requirement():
        if not child_support_enabled:
            return "Enable in Mod Setting -> Gameplay"
        return True

    def cs_setting_initialization(self):
        bedroom.add_action(self)
        return (persistent.pregnancy_pref == 3)
        
#----------------------------

    def meditation_requirement():
        if (mc.free_stat_points > 0) or (mc.free_work_points > 0) or (mc.free_sex_points > 0):
            return True
        return "Complete more goals"

    def meditation_initialization(self):
        bedroom.add_action(self)
        return
        
#----------------------------

    def auto_skill_toggle(is_enabled = False):
        global auto_skill_enabled
        global skill_check_delay
        
        auto_skill_enabled = is_enabled

        if (is_enabled):
            mc.log_event("Auto skill ENABLED", "float_text_grey")
        else:
            #ceo_office.remove_action(self)
            mc.log_event("Auto skill DISABLED", "float_text_grey")
        return

    def autoskill_setting_requirement():
        if not auto_skill_enabled:
            return "Enable in Mod Setting -> Gameplay"
        return True

    def autoskill_setting_initialization(self):
        bedroom.add_action(self)
        return (True)

#----------------------------
        
    # Register for modsettings
    cs_mod = ActionMod("Child Support ", cs_requirement, "cs_toggle_label",
        menu_tooltip = "Be a responsible father", # [Only $" + str(cs_amount) + "/Child weekly]", 
        category = "Gameplay", 
        initialization = init_action_mod_disabled,
        on_enabled_changed = child_support_toggle,
        is_crisis = False )

    # Register for modsettings
    cs_support_action = ActionMod("Child Support - Option", cs_setting_requirement, "cs_option_label",
        menu_tooltip = "Set the weekly amount for child support",
        category="Gameplay",
        initialization = cs_setting_initialization,
        is_crisis = False )  
        
    # Register for modsettings
    accent_mod = ActionMod("Ellie's use normal accent [toggle]", accent_requirement, "accent_toggle_label",
        menu_tooltip = "No cowgirl talking accent (toggleable)", 
        category = "Gameplay", 
        initialization = init_action_mod_disabled,
        on_enabled_changed = southern_accent_toggle,
        is_crisis = False )

    # Register for modsettings
    static_mod = ActionMod("KiNA Mod - Family static opinions.", static_requirement, "opinion_label",
        menu_tooltip = "Tweaked opinions for Mom and Sis. Soft conflict with Zenupstart's mod.", 
        category = "Home", 
        initialization = init_action_mod_disabled,
        on_enabled_changed = static_changed,
        is_crisis = False )

    # Register for modsettings
    makeup_mod = ActionMod("KiNA Mod - Pretty start.", makeup_requirement, "makeup_label",
        menu_tooltip = "Applying some makeups on few girls.", 
        category = "Home", 
        initialization = init_action_mod_disabled,
        on_enabled_changed = makeup_changed,
        is_crisis = False )

    # Register for modsettings
    meditate_action = ActionMod("Meditation", meditation_requirement, "meditation_label",
        menu_tooltip = "Convert your unused points",
        category="Gameplay",
        initialization = meditation_initialization,
        is_crisis = False ) 
        
    # Register for modsettings
    accent_mod = ActionMod("Narrative story fix", bugfix_requirement, "bugfix_label",
        menu_tooltip = "Set Camila and Ellie on no BC", 
        category = "Gameplay", 
        initialization = init_action_mod_disabled,
        on_enabled_changed = narrative_bugfix,
        is_crisis = False ) 
            
    # Register for modsettings
    level_mod = ActionMod("Employees auto gain skill", True, "autoskill_toggle_label",
        menu_tooltip = "Your employee can gain skill/stats automatically", 
        category = "Gameplay", 
        initialization = init_action_mod_disabled,
        on_enabled_changed = auto_skill_toggle,
        is_crisis = False )  

    # Register for modsettings
    autoskill_action = ActionMod("Autoskill Setup", autoskill_setting_requirement, "autoskill_option_label",
        menu_tooltip = "Autoskill Setup",
        category="Gameplay",
        initialization = autoskill_setting_initialization,
        is_crisis = False )    
#----------------------------  

label opinion_label():
    return

label makeup_label():
    return

label accent_toggle_label():
    return

label cs_toggle_label():                    
    return

label bugfix_label():
    return

label cs_option_label():
    $ amount = mc.offspring_count * cs_amount
    $ mama = sum(1 for person in all_people_in_the_game() if person.has_child_with_mc)   #shout out to Elkrose and Kaden
    if mc.offspring_count > 0:
        "Currently paying (weekly): $[cs_amount] / child "
        "Summary (weekly) : $[amount] paid to [mama] person(s) for [mc.offspring_count] kid(s)."
    else:
        "You don't have any kids yet. Current : $[cs_amount] per kid."
    menu:
        "$[cs_amount] -> $50" if (cs_amount != 50):
            $ cs_amount = 50   
        "$[cs_amount] -> $100" if (cs_amount != 100):
            $ cs_amount = 100   
        "$[cs_amount] -> $150" if (cs_amount != 150):
            $ cs_amount = 150   
        "$[cs_amount] -> $200" if (cs_amount != 200):
            $ cs_amount = 200   
        "$[cs_amount] -> $250" if (cs_amount != 250):
            $ cs_amount = 250
        "Don't change.":
            pass
    if mc.offspring_count > 0:
        "You've chosen to pay $[cs_amount] per child starting next Saturday. "
        $ amount = mc.offspring_count * cs_amount
        "Next payment : $[amount] for [mc.offspring_count] kid(s) to [mama] person(s)."
    else:        
        "You've planned to pay $[cs_amount] per kid."                           
    return

label meditation_label(): 
    "You have achieved quite a few goals in life.\n These insights are worth pondering upon."
    call main_menu_label from _call_meditation_KS
    "You've end your meditation."
    return

label stat_menu_label():
    menu:
        "Available Stat Point : [mc.free_stat_points]\n-> Work Point" if (mc.free_stat_points >= 2):
            $ mc.free_stat_points -= 2
            $ mc.free_work_points += 1
            "You lost 2 stat points.\nYou gained 1 work point."
        "Available Stat Point : [mc.free_stat_points]\n-> Sex Point" if (mc.free_stat_points >= 2):
            $ mc.free_stat_points -= 2
            $ mc.free_sex_points += 1
            "You lost 2 stat points.\nYou gained 1 sex point."  
        "{menu_red}-> Work/Sex Point (disabled)\nDon't have enough points!{/menu_red}" if (mc.free_stat_points < 2):
            pass
        "Available Stat Point : [mc.free_stat_points]\n-> Clarity" if (mc.free_stat_points >= 1):
            $ mc.free_stat_points -= 1
            $ mc.free_clarity += 100
            "You lost 1 stat point.\nYou gained 100 clarity."
        "Back":
            return #call main_menu_label from _call_meditation_KS_1

    #If still have points, call itself    
    if (mc.free_stat_points >= 1):
        call stat_menu_label from _call_meditation_KS06                 
    return

label work_menu_label():
    menu:
        "Available Work Point : [mc.free_work_points]\n-> Stat Point" if (mc.free_work_points >= 2):
            $ mc.free_work_points -= 2
            $ mc.free_stat_points += 1
            "You lost 2 work points.\nYou gained 1 stat point."
        "Available Work Point : [mc.free_work_points]\n-> Sex Point" if (mc.free_work_points >= 2):
            $ mc.free_work_points -= 2
            $ mc.free_sex_points += 1
            "You lost 2 work points.\nYou gained 1 sex point."
        "{menu_red}-> Stat/Sex Point (disabled)\nDon't have enough points!{/menu_red}" if (mc.free_work_points < 2):
            pass
        "Available Work Point : [mc.free_work_points]\n-> Clarity" if (mc.free_work_points >= 1):
            $ mc.free_work_points -= 1
            $ mc.free_clarity += 100
            "You lost 1 work point.\nYou gained 100 clarity."
        "Back":
            return #call main_menu_label from _call_meditation_KS_2

    #If still have points, call itself                
    if (mc.free_work_points >= 1):
        call work_menu_label from _call_meditation_KS09 
    return

label sex_menu_label():
    menu:
        "Available Sex Point : [mc.free_sex_points]\n-> Stat Point" if (mc.free_sex_points >= 2):
            $ mc.free_sex_points -= 2
            $ mc.free_stat_points += 1
            "You lost 2 sex points.\nYou gained 1 stat point."
            if (mc.free_sex_points >= 1):
                call sex_menu_label from _call_meditation_KS10
            else:
                call main_menu_label from _call_meditation_KS_10
        "Available Sex Point : [mc.free_sex_points]\n-> Work Point" if (mc.free_sex_points >= 2):
            $ mc.free_sex_points -= 2
            $ mc.free_work_points += 1
            "You lost 2 sex points.\nYou gained 1 work point."
            if (mc.free_sex_points >= 1):
                call sex_menu_label from _call_meditation_KS11
            else:
                call main_menu_label from _call_meditation_KS_11
        "{menu_red}-> Work/Stat Point (disabled)\nDon't have enough points!{/menu_red}" if (mc.free_sex_points < 2):
            pass
        "Available Sex Point : [mc.free_sex_points]\n-> Clarity" if (mc.free_sex_points >= 1):
            $ mc.free_sex_points -= 1
            $ mc.free_clarity += 100
            "You lost 1 sex point.\nYou gained 100 clarity."
        "Back":
            return #call main_menu_label from _call_meditation_KS_3

    #If still have points, call itself                            
    if (mc.free_sex_points >= 1):
        call sex_menu_label from _call_meditation_KS12
    return

label main_menu_label():
    menu:
        "Available Point : [mc.free_stat_points]\nConvert Stat Points" if (mc.free_stat_points >= 1):
            "The conversion rate is 2:1 to other blocks.\nClarity conversion is at 1:100"
            call stat_menu_label from _call_meditation_KS01
        "{menu_red}Convert Stat Points (disabled)\nDon't have enough points!{/menu_red}" if (mc.free_stat_points < 1):
            pass     
        "Available Point : [mc.free_work_points]\nConvert Work Points" if (mc.free_work_points >= 1):
            "The conversion rate is 2:1 to other blocks.\nClarity conversion is at 1:100"
            call work_menu_label from _call_meditation_KS02
        "{menu_red}Convert Work Points (disabled)\nDon't have enough points!{/menu_red}" if (mc.free_work_points < 1):
            pass
        "Available Point : [mc.free_sex_points]\nConvert Sex Points" if (mc.free_sex_points >= 1):
            "The conversion rate is 2:1 to other blocks.\nClarity conversion is at 1:100"
            call sex_menu_label from _call_meditation_KS03
        "{menu_red}Convert Sex Points (disabled)\nDon't have enough points!{/menu_red}" if (mc.free_sex_points < 1):
            pass
        "End meditation":
            return
    return

label autoskill_toggle_label():
    return

label autoskill_option_label(): 
    if auto_skill_enabled:               
        "Decide when skill should levelled up."
        "NOTE: If skills levelled too fast, employee might demand higher wages frequently."
        "NOTE: Skills/Stats capped at 8. However, once skill is 8, relevant stats will stop levelling up too, even if they aren't maxxed."
        "NOTE: Skill might not levelled up. Stats is twice as hard. Bimbo WILL NOT level up her Intelligent. Other stats will work."
        
        menu:
            "Daily (Run everyday)":
                $ skill_check_delay = 1 
            "Weekly (Run every 7 days)":
                $ skill_check_delay = 7 
            "Fortnightly (Run every 14 day)":
                $ skill_check_delay = 14 
            "Monthly (Run every month)":
                $ skill_check_delay = 30
            "Don't change : Running every [skill_check_delay] day":
                pass    
    else:
        "Enable Autoskill."
    return
#-------------------------

