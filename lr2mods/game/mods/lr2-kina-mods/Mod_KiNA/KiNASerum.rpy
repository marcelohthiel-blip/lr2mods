#Serum contained things related to *drumrolls*.. serum. Prolly gonna make this novelty serum the only thing
#Credits to afterd4rk over at LR2 discord with his inputs. Me dumb.

init -1 python:
    def novelty_on_day(the_person, the_serum, add_to_log):
        if the_person.love < 0:
            amount = builtins.int(builtins.round(the_person.obedience/30))
        else:
            amount = builtins.int(builtins.round(the_person.love/10))

        if the_person.novelty + amount > 100:
            amount = 100 - the_person.novelty
        the_person.change_novelty(amount)   #Scuplting the pussy
        display_name = the_person.create_formatted_title("???")
        if the_person.title:
            display_name = the_person.title
        mc.log_event(display_name + " adapts her body to better serve you...", "float_text_grey")
        return

    def better_novelty_on_turn(the_person, the_serum, add_to_log):
        if the_person.love < 0:
            amount = builtins.int(builtins.round(the_person.obedience/30))
        else:
            amount = builtins.int(builtins.round(the_person.love/10))
            
        if the_person.novelty + amount > 100:
            amount = 100 - the_person.novelty
        the_person.change_novelty(amount)   #Scuplting the pussy
        display_name = the_person.create_formatted_title("???")
        if the_person.title:
            display_name = the_person.title
        mc.log_event(display_name + " adapts her body to better serve you...", "float_text_grey")
        return

    def sex_learning_on_day(the_person, the_serum, add_to_log):
        amount = builtins.int((100 - the_person.novelty)/2)
        if amount > 45:
            #you really pound her everyday, she practically have less then 10 novelty left 
            the_person.increase_sex_skill("Foreplay", max_value = 8)
            the_person.increase_sex_skill("Oral", max_value = 8)
            the_person.increase_sex_skill("Vaginal", max_value = 8)
            the_person.increase_sex_skill("Anal", max_value = 8)
            display_name = the_person.create_formatted_title("???")
            if the_person.title:
                display_name = the_person.title
            mc.log_event(display_name + " sex skills increased...", "float_text_red")
        elif not amount == 0 and amount <= 45:
            if renpy.random.randint(0,100) < amount:
                position = renpy.random.randint(1,4)
                if position == 1:
                    the_person.increase_sex_skill("Foreplay", max_value = 8)
                    display_name = the_person.create_formatted_title("???")
                    if the_person.title:
                        display_name = the_person.title
                    mc.log_event(display_name + " foreplay skill increased...", "float_text_red")
                elif position == 2:
                    the_person.increase_sex_skill("Oral", max_value = 8)
                    display_name = the_person.create_formatted_title("???")
                    if the_person.title:
                        display_name = the_person.title
                    mc.log_event(display_name + " oral skill increased...", "float_text_red")
                elif position == 3:
                    the_person.increase_sex_skill("Vaginal", max_value = 8)
                    display_name = the_person.create_formatted_title("???")
                    if the_person.title:
                        display_name = the_person.title
                    mc.log_event(display_name + " vaginal skill increased...", "float_text_red")
                elif position == 4:
                    the_person.increase_sex_skill("Anal", max_value = 8)
                    display_name = the_person.create_formatted_title("???")
                    if the_person.title:
                        display_name = the_person.title
                    mc.log_event(display_name + " anal skill increased...", "float_text_red")
                else:
                    display_name = the_person.create_formatted_title("???")
                    if the_person.title:
                        display_name = the_person.title
                    mc.log_event(display_name + " doesn't learn anything tonight...", "float_text_grey")    
        else:
            display_name = the_person.create_formatted_title("???")
            if the_person.title:
                display_name = the_person.title
            mc.log_event(display_name + " doesn't learn anything tonight...", "float_text_grey")    
        return

    def babywant_on_turn(the_person, the_serum, add_to_log):
        if the_person == erica and erica_get_progress() < 4:
            mc.log_event("Erica's body is rejecting the serum...", "float_text_red")
            return

        amount = builtins.int(builtins.round(the_person.love/50))

        if the_person.baby_desire < 40:
            the_person.change_baby_desire(amount)   #want a baby
        if the_person.fertility_percent < 40:   #more realistic?
            the_person.fertility_percent += (amount/2)

        percent = builtins.int(builtins.round(the_person.baby_desire))
        display_name = the_person.create_formatted_title("???")
        if the_person.title:
            display_name = the_person.title               
            mc.log_event(display_name + " is nurturing her motherly instinct..." + str(percent) + "%", "float_text_grey")
        return

    #Side Effects
    def sexytocin_side_effect_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
        person.change_slut(1, 40, add_to_log = False)
        return
        
    def weight_gain_side_effect_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
        if (person._weight < 90 * person.height):
            person.change_weight(amount = 0.0113, chance = 50)
        return
            
    def weight_loss_side_effect_on_turn(person: Person, serum: SerumDesign, add_to_log: bool):
        if (person._weight < 50 * person.height):
            person.change_weight(amount = -0.0113, chance = 50)
        return
    
    def kina_sluttiness_side_effect():
        sexytocin_side_effect = SideEffectTraitMod(name = "Sexytocin Increment",
            desc = "An unintended interaction produces a noticeable spike in the recipient's promiscuity, but only when they are not too promiscuous already.",
            positive_slug = "Permanent +1 Sluttiness/Turn when Sluttiness < 40",
            negative_slug = "",
            on_turn = sexytocin_side_effect_on_turn,
            is_side_effect = True,
            mental_aspect = 3, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
        
    def kina_weight_gain_side_effect():
        food_addict_side_effect = SideEffectTraitMod(name = "Food Binge",
            desc = "An unintended interaction results in recipient indulging themselves with food.",
            positive_slug = "Increases body weight.",
            negative_slug = "",
            on_turn = weight_gain_side_effect_on_turn,
            exclude_tags = ["Weight Modification"],
            is_side_effect = True,
            mental_aspect = 3, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
        
    def kina_weight_loss_side_effect():
        diet_side_effect = SideEffectTraitMod(name = "Lost Appetite",
            desc = "An unintended interaction results in recipient losing her appetite.",
            positive_slug = "Loses body weight.",
            negative_slug = "",
            on_turn = weight_loss_side_effect_on_turn,
            exclude_tags = ["Weight Modification"],
            is_side_effect = True,
            mental_aspect = 3, physical_aspect = 0, sexual_aspect = 2, medical_aspect = 0, flaws_aspect = 0, attention = 1)
        
        
    def add_novelty_serum():
        novelty_serum_trait = SerumTraitMod(name = "Body Adaption",     # The name of the serum
            desc = "Girl adapts her body to fit your dick the more they love you. Use at night only.", # Make up something about how it works.
            positive_slug = "+ 1 novelty for every 10 love/day or every 30 obedience/day if they hate you",                            # The green section in the serum design screen
            negative_slug = "",                                         # The red section in the serum design screen
            research_added = 250,                                       # Extra research required to develop the protoype
            base_side_effect_chance = 30,
            on_day = novelty_on_day,                                    # Function to run every turn this trait is active
            requires = None,                                            # If it requires another serum to be researched first
            tier = 1,                                                   # Use 0-3
            start_researched = False,                                   # If trait is already researched
            research_needed = 350,                                      # Research required to unlock trait
            is_side_effect = False,                                     # IF this trait is actually a side effect and not researchable
            clarity_cost = 400,                                        # Cost in clarity to begin researching this trait
            mental_aspect = 3, 
            physical_aspect = 3, 
            sexual_aspect = 3, 
            medical_aspect = 6, 
            flaws_aspect = 0, 
            attention = 2,
            start_enabled = True)                                       # MOD function. if False, players MUST enable the serum in the mod options menu from MC bedroom.

    def add_better_novelty_serum():
        better_novelty_serum_trait = SerumTraitMod(name = "Enhanced Body Adaption",     # The name of the serum
            desc = "Girl adapting her body to fit your dick the more they love you. Faster.", # Make up something about how it works.
            positive_slug = "+ 1 novelty for every 10 love/turn or every 30 obedience/turn if they hate you",       # The green section in the serum design screen
            negative_slug = "",                                         # The red section in the serum design screen
            research_added = 350,                                       # Extra research required to develop the protoype
            base_side_effect_chance = 50,
            on_turn = better_novelty_on_turn,                           # Function to run every turn this trait is active
            tier = 2,                                                   # Use 0-3
            start_researched = False,                                   # If trait is already researched
            requires = [find_serum_trait_by_name("Body Adaption")],       # If it requires another serum to be researched first
            research_needed = 500,                                     # Research required to unlock trait
            is_side_effect = False,                                     # IF this trait is actually a side effect and not researchable
            clarity_cost = 600,                                        # Cost in clarity to begin researching this trait
            mental_aspect = 5, 
            physical_aspect = 5, 
            sexual_aspect = 5, 
            medical_aspect = 8, 
            flaws_aspect = 0, 
            attention = 3,
            start_enabled = True)                                       # MOD function. if False, players MUST enable the serum in the mod options menu from MC bedroom.

    def add_sex_learning_serum():
        sex_learning_serum_trait = SerumTraitMod(name = "Learning by Experience",     # The name of the serum
            desc = "As they familiarize themselves with you, they quickly learn how to pleasure you more. Use at night only.", # Make up something about how it works.
            positive_slug = "Chances to level random sex skills the lower her novelty is ",                            # The green section in the serum design screen
            negative_slug = "",                                         # The red section in the serum design screen
            research_added = 250,                                       # Extra research required to develop the protoype
            base_side_effect_chance = 50,
            on_day = sex_learning_on_day,                                    # Function to run every turn this trait is active
            requires = None,                                            # If it requires another serum to be researched first
            tier = 1,                                                   # Use 0-3
            start_researched = False,                                   # If trait is already researched
            research_needed = 300,                                      # Research required to unlock trait
            is_side_effect = False,                                     # IF this trait is actually a side effect and not researchable
            clarity_cost = 400,                                        # Cost in clarity to begin researching this trait
            mental_aspect = 3, 
            physical_aspect = 3, 
            sexual_aspect = 3, 
            medical_aspect = 6, 
            flaws_aspect = 0, 
            attention = 2,
            start_enabled = True)                                       # MOD function. if False, players MUST enable the serum in the mod options menu from MC bedroom.

    def add_improved_capacity_design_serum():
        improved_capacity_design = SerumTraitMod(name = "Improved Capacity Design",
            desc = "Based on previous designs, we managed to improve the capacity allowing our serum more traits to be added to the design. It is still almost certain to introduce unpleasant side effects.",
            positive_slug = "+3 Trait Slot",
            negative_slug = "",
            research_added = 100,
            slots_added = 4,
            base_side_effect_chance = 100,
            requires = [high_capacity_design], #find_serum_trait_by_name(" High Capacity Design"),
            tier = 1,
            start_researched = False,
            research_needed = 200,
            clarity_cost = 50,
            mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 0,
            start_enabled = True)  
        #return

    def add_advanced_capacity_design_serum():
        advanced_capacity_design = SerumTraitMod(name = "Advanced Capacity Design",
            desc = "Further research on our serum design allow us to improve the capacity, adding more traits to the serum. Unpleasant side effects are still a major concern.",
            positive_slug = "+4 Trait Slot",
            negative_slug = "",
            research_added = 200,
            slots_added = 5,
            base_side_effect_chance = 50,
            requires = [find_serum_trait_by_name("Improved Capacity Design")],
            tier = 2,
            start_researched = False,
            research_needed = 250,
            clarity_cost = 100,
            mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 0,
            start_enabled = True)
        #return

    def add_superior_capacity_design_serum():
        superior_capacity_design = SerumTraitMod(name = "Superior Capacity Design",
            desc = "Ongoing research on our serum design allow us to improve the capacity and reducing side effects to the serum.",
            positive_slug = "+5 Trait Slot",
            negative_slug = "",
            research_added = 300,
            slots_added = 6,
            base_side_effect_chance = 20,
            requires = [find_serum_trait_by_name("Advanced Capacity Design")],
            tier = 3,
            start_researched = False,
            research_needed = 300,
            clarity_cost = 200,
            mental_aspect = 0, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 6, flaws_aspect = 0, attention = 0,
            start_enabled = True)
        #return

    def add_baby_serum():
        novelty_serum_trait = SerumTraitMod(name = "Breeding Fascination",                                                          # The name of the serum
            desc = "Trigger the maternal instint to have babies the more they love you.",                                           # Make up something about how it works.
            positive_slug = "Increased their desire and fertility to have baby the more they love you.",                            # The green section in the serum design screen
            negative_slug = "",                                                                                                     # The red section in the serum design screen
            research_added = 250,                                                                                                   # Extra research required to develop the protoype
            base_side_effect_chance = 30,
            on_turn = babywant_on_turn,                                                                                             # Function to run every turn this trait is active
            requires = [find_serum_trait_by_name("Immediate Ovulation")],                                                           # If it requires another serum to be researched first
            hidden_tag = "Reproduction",                                                         
            tier = 3,                                                                                                               # Use 0-3
            start_researched = False,                                                                                               # If trait is already researched
            research_needed = 250,                                                                                                  # Research required to unlock trait
            is_side_effect = False,                                                                                                 # IF this trait is actually a side effect and not researchable
            clarity_cost = 200,                                                                                                    # Cost in clarity to begin researching this trait
            mental_aspect = 3, 
            physical_aspect = 3, 
            sexual_aspect = 3, 
            medical_aspect = 6, 
            flaws_aspect = 0, 
            attention = 2,
            start_enabled = True)                                                                                                   # MOD function. if False, players MUST enable the serum in the mod options menu from MC bedroom.

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_novelty_serum_trait(stack):
    python:
        add_novelty_serum()
        add_better_novelty_serum()
        add_sex_learning_serum()
        add_improved_capacity_design_serum()
        add_advanced_capacity_design_serum()
        add_superior_capacity_design_serum()
        if persistent.pregnancy_pref > 0: #in case peoples turned off preggo system
            add_baby_serum()
        execute_hijack_call(stack)
    return

#KiNA's side effect
label side_effect_mod_trait(stack):
    python:
        kina_sluttiness_side_effect()
        kina_weight_gain_side_effect()
        kina_weight_loss_side_effect()
        execute_hijack_call(stack)
    return
    

#pregnancy_accelerator_trait = SerumTrait(name = "Pregnancy Acceleration Hormones",
#    desc = "Encourages and supports the ongoing development of a fetus, increasing the effective speed at which a pregnancy develops.",
#    positive_slug = "+1 Pregnancy Progress/Day",
#    negative_slug = "",
#    research_added = 250,
#    base_side_effect_chance = 60,
#    on_day = pregnancy_accelerator_on_day,
#    requires = [fertility_enhancement_trait],
#    tier = 2,
#    research_needed = 800,
#    mental_aspect = 0, physical_aspect = 3, sexual_aspect = 0, medical_aspect = 6, flaws_aspect = 0, attention = 3,
#    exclude_tags = "Pregnancy",
#    clarity_cost = 1200)

#massive_pregnancy_accelerator = SerumTrait(name = "Extreme Pregnancy Hormones",
#    desc = "Overloads the body with natural pregnancy hormones alongside nutrient supplements. Massively increases the pace at which a pregnancy will progress.",
#    positive_slug = "+1 Pregnancy Progress/Turn",
#    negative_slug = "",
#    research_added = 300,
#    base_side_effect_chance = 80,
#    on_turn = massive_pregnancy_accelerator_on_turn,
#    requires = [pregnancy_accelerator_trait],
#    tier = 3,
#    research_needed = 1400,
#    mental_aspect = 0, physical_aspect = 9, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 4,
#    exclude_tags = "Pregnancy",
#    clarity_cost = 1800)