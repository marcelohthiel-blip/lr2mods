from __future__ import annotations
import builtins
import renpy
from game.major_game_classes.character_related.ActiveJob_ren import ActiveJob
from game.major_game_classes.business_related.Policy_ren import Policy
from game.major_game_classes.character_related.Person_ren import Person, mc
from game.major_game_classes.game_logic.Action_ren import Action, Limited_Time_Action
from renpy.exports import write_log

uniform_policies_list: list[Policy] = []
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
#### UNIFORM POLICY SECTION ####
def uniform_disobedience_on_move(uniform_disobedience_priority): #This is an on_move function called by the business on_move phase. It is only run once, by the uniform policy with the highest priority
    highest_active_priority = -1
    for policy in (x for x in mc.business.active_policy_list if "uniform_disobedience_priority" in x.extra_arguments):
        if policy.extra_arguments.get("uniform_disobedience_priority", -1) > highest_active_priority:
            highest_active_priority = policy.extra_arguments.get("uniform_disobedience_priority", -1) #Check all policies and make sure we are only running this function once (with the highest priority, just in case)

    if highest_active_priority != uniform_disobedience_priority: #ie. only run this function if we have the highest priority, otherwise some other policy is responsible for it.
        return

    # print(f"Running uniform disobedience priority {highest_active_priority}")

    for person in (x for x in mc.business.employees_at_office if x.should_wear_uniform and x.is_wearing_uniform and not x.is_wearing_forced_uniform and x.has_event_delay("uniform_disobedience", 3)):
        disobedience_chance = 0
        if not person.judge_outfit(person.current_planned_outfit):
            #Girls who find the outfit too slutty might disobey, scaled by their obedience
            disobedience_chance = (person.current_planned_outfit.outfit_slut_score - person.effective_sluttiness()) / ((person.obedience / 200.0) or .01)
            disobedience_chance += -2 * (person.opinion.skimpy_uniforms)
        else:
            #Disobedient girls sometimes don't wear uniforms, just because they don't like following orders. Less likely than when outfits are too slutty.
            disobedience_chance = (200 - person.obedience) / 10
            disobedience_chance += -2 * person.opinion.work_uniforms

        # print(f"{person.name} {person.last_name} disobedience chance {disobedience_chance}%")

        if renpy.random.randint(5, 100) < builtins.max(disobedience_chance, 0): # when chance is less than 5% event will not occur
            write_log(f"{person.name} {person.last_name} is violating uniform policy ({disobedience_chance}%)")
            uniform_disobedience_action = Action("Uniform Disobedience LTE", uniform_disobedience_requirement, "uniform_disobedience_event",
                                                 event_duration = 3, requirement_args = person.current_job, args = person.current_planned_outfit.get_copy()) #Needs to be created here so we can reference what we disliked about the uniform.
            person.add_unique_on_talk_event(Limited_Time_Action(uniform_disobedience_action))
            person.current_planned_outfit = person.planned_outfit # set uniform to her normal planned outfit
            person.wear_uniform()
            person.set_event_day("uniform_disobedience")    # Set flag that she's not wearing uniform, she will not do so for another 3 days (prevent event spamming, even when not addressed by player)

    return

def uniform_disobedience_requirement(person: Person, job: ActiveJob):
    return (person.current_job == job
        and person.should_wear_uniform
        and not person.is_wearing_uniform)

#Called by all uniform policies to clear newly inappropriate planned uniforms.
def reset_invalid_uniforms(uniform_disobedience_priority):
    slut_limit, _, _ = mc.business.get_uniform_limits()
    for employee in (x for x in mc.business.employee_list if x.should_wear_uniform and x.current_planned_outfit.outfit_slut_score > slut_limit and x.current_planned_outfit.outfit_slut_score > x.effective_sluttiness()):
        employee.current_job.current_uniform = None
        employee.apply_planned_outfit()

def mandatory_toys_policy_on_turn():
    if not mc.business.is_open_for_business:
        return

    modifier_percent = 0
    if mandatory_vibe_policy.is_active:
        modifier_percent += 0.15
    if mandatory_bullet_policy.is_active:
        modifier_percent += 0.2
    if mandatory_plug_policy.is_active:
        modifier_percent += 0.25

    for person in (x for x in mc.business.employees_at_office if x.arousal < (x.max_arousal * modifier_percent)):
        person.arousal = int(modifier_percent * person.max_arousal)
    return

def mandatory_toys_policy_on_day():
    def change_toy_based_stats(person: Person, happiness: int, effectiveness: int):
        #print("Toy change: {} -> {} {}".format(person.name, happiness, effectiveness))
        person.change_happiness(happiness, max_amount = 200, add_to_log = False)
        mc.business.change_team_effectiveness(effectiveness, instant = True)
        return effectiveness

    efficiency_change = 0
    for person in mc.business.employees_at_office:
        if mandatory_plug_policy.is_active and not person.has_anal_fetish:
            if person.sluttiness < 30:
                efficiency_change += change_toy_based_stats(person, -10, -3)
            elif person.sluttiness < 50:
                efficiency_change += change_toy_based_stats(person, -5, -2)
            elif person.sluttiness < 70:
                efficiency_change += change_toy_based_stats(person, -2, -1)
            elif person.sluttiness >= 70:
                efficiency_change += change_toy_based_stats(person, 2, 1)
        if mandatory_bullet_policy.is_active and not person.has_breeding_fetish:
            if person.sluttiness < 30:
                efficiency_change += change_toy_based_stats(person, -5, -2)
            elif person.sluttiness < 50:
                efficiency_change += change_toy_based_stats(person, -2, -1)
            elif person.sluttiness >= 50:
                efficiency_change += change_toy_based_stats(person, 2, 1)
        if mandatory_vibe_policy.is_active:
            if person.sluttiness < 30:
                efficiency_change += change_toy_based_stats(person, -2, -1)
            elif person.sluttiness >= 30:
                efficiency_change += change_toy_based_stats(person, 2, 1)

    if efficiency_change < 0:
        mc.business.add_normal_message(f"Your employees are generally getting annoyed and Team Efficiency is down by {abs(efficiency_change):.0f}% due to Toy policies.")
    if efficiency_change > 0:
        mc.business.add_normal_message(f"Your employees are generally happy and Team Efficiency is up by {abs(efficiency_change):.0f}% due to Toy policies.")
    return

def init_clothing_policies():
    global strict_uniform_policy
    global b_name
    strict_uniform_policy = Policy(name = "Strict Corporate Uniforms",
        desc = f"{b_name} Strict Corporate Uniforms: Upholding a Professional Image\n\nAt {b_name}, we take pride in our professional image and reputation. That's why we're introducing our strict corporate uniforms, designed to ensure that all employees present a polished and respectful image to our clients and colleagues.\n\nOur new uniforms are all about maintaining a high level of professionalism and sophistication. With a focus on classic, timeless attire, you'll be able to project confidence and expertise in your field.\n\nTo ensure that our workplace remains respectful and professional, we've established the following guidelines:\n\n*** Overwear sets with a sluttiness rating of 10 or less are permitted as part of your business uniform ***\n\nWe believe that our strict corporate uniforms will help to foster a culture of respect, discipline, and excellence within our organization. By dressing professionally, we demonstrate our commitment to our values and our dedication to delivering exceptional results. We're confident that our new uniforms will help us to achieve even greater success in the future.",
        cost = 500,
        toggleable = True,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        extra_arguments = {"uniform_disobedience_priority": 0}) #Uniform disobedience is only run once, regardless of how many policies are running. The highest priority uniform function is run.

    global relaxed_uniform_policy
    relaxed_uniform_policy = Policy(name = "Relaxed Corporate Uniforms",
        desc = f"{b_name} Relaxed Corporate Uniforms: Where Style Meets Comfort\n\nAt {b_name}, we believe that your work attire should be an extension of your personality, not a restriction. That's why we're introducing our relaxed corporate uniforms, designed to give you the freedom to express yourself in a way that's both professional and relaxed.\n\nOur new uniforms are all about finding the perfect balance between style and comfort. With a focus on relaxed, yet still professional attire, you'll be able to feel at ease while still presenting a polished image to our clients and colleagues.\n\nTo ensure that our workplace remains respectful and professional, we've established the following guidelines:\n\n*** Overwear sets with a sluttiness rating of up to 20 are permitted as part of your business uniform ***\n\nWe're excited to see the positive impact that our relaxed corporate uniforms will have on our work environment and productivity. By giving you the freedom to dress in a way that's authentic and comfortable, we're confident that you'll be able to perform at your best and reach new heights of success.",
        cost = 1000,
        toggleable = True,
        own_requirement = strict_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = strict_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority": 1})

    global casual_uniform_policy
    casual_uniform_policy = Policy(name = "Casual Corporate Uniforms",
        desc = f"{b_name} Casual Corporate Uniforms: Where Comfort Meets Style\n\nAt {b_name}, we believe that your work attire should be comfortable, yet still reflect the professionalism and values of our company. That's why we're introducing our casual corporate uniforms, designed to give you the freedom to express yourself in a way that's both relaxed and respectful.\n\nOur new uniforms are all about finding the perfect balance between comfort and style. With a focus on casual, yet still professional attire, you'll be able to feel at ease while still presenting a polished image to our clients and colleagues.\n\nTo ensure that our workplace remains respectful and professional, we've established the following guidelines:\n\n*** Overwear sets with a sluttiness rating of up to 30 are permitted as part of your business uniform ***\n\nWe're excited to see the positive impact that our casual corporate uniforms will have on our work environment and productivity. So, get ready to dress down, yet still impress, with our casual corporate uniforms.",
        cost = 2000,
        toggleable = True,
        own_requirement = relaxed_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = relaxed_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority": 2})

    global reduced_coverage_uniform_policy
    reduced_coverage_uniform_policy = Policy(name = "Reduced Coverage Corporate Uniforms",
        desc = f"{b_name} Reduced Coverage Corporate Uniforms: Unleashing Your Inner Style\n\nAt {b_name}, we believe that your work attire should be an extension of your personality, not a restriction. That's why we're introducing our reduced coverage corporate uniforms, designed to give you the freedom to express yourself in a way that's both professional and provocative.\n\nOur new uniforms are all about striking the perfect balance between style and sophistication. With a focus on reduced coverage, you'll be able to showcase your unique sense of fashion while still maintaining a level of professionalism that's unmatched in the industry.\n\nTo ensure that our workplace remains respectful and professional, we've established the following guidelines:\n\n*** Underwear sets with a sluttiness rating of up to 15 are permitted ***\n*** Overwear sets with a sluttiness rating of up to 40 are permitted ***\n\nWe're excited to see the amazing things you'll accomplish when you're feeling confident, expressive, and unapologetically yourself. So, get ready to unleash your inner style and take your workwear to the next level with our reduced coverage corporate uniforms.",
        cost = 5000,
        toggleable = True,
        own_requirement = casual_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = casual_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority": 3})

    global minimal_coverage_uniform_policy
    minimal_coverage_uniform_policy = Policy(name = "Minimal Coverage Corporate Uniforms",
        desc = f"{b_name} Minimal Coverage Corporate Uniforms: Redefining Professional Attire\n\nAt {b_name}, we're committed to pushing the boundaries of innovation and self-expression. That's why we're introducing a new corporate uniform policy that's all about minimal coverage and maximum style.\n\nImagine a workplace where creativity and confidence thrive, where employees feel empowered to express themselves in a way that's both professional and personal. Our new policy makes that vision a reality, with uniforms that are designed to be bold, daring, and unapologetically you.\n\nWith our minimal coverage corporate uniforms, you'll be able to showcase your unique personality and style while still maintaining a level of professionalism that's unmatched in the industry. Specifically, our policy allows for:\n\n*** Underwear sets with a sluttiness rating of up to 30 ***\n*** Overwear sets with a sluttiness rating of up to 60 ***\n\nPlease note that these guidelines are in place to ensure that our workplace remains respectful and professional, while still allowing for a high degree of personal expression. We're excited to see the amazing things you'll accomplish when you're feeling confident, expressive, and unapologetically yourself.",
        cost = 10000,
        toggleable = True,
        own_requirement = reduced_coverage_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = reduced_coverage_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority": 4})

    global corporate_enforced_nudity_policy
    corporate_enforced_nudity_policy = Policy(name = "Corporate Enforced Nudity",
        desc = f"{b_name} Corporate Enforced Nudity Policy: Embracing a New Era of Transparency\n\nAs we continue to push the boundaries of innovation and progress, {b_name} is proud to introduce a bold new initiative: a corporate enforced nudity policy. By shedding the constraints of clothing, we aim to create a work environment that is more open, more honest, and more productive.\n\nImagine a workplace where creativity flows freely, unencumbered by the restrictive norms of traditional attire. A place where collaboration and teamwork thrive, fueled by the unbridled energy of the human spirit. This is the vision we aim to achieve with our new policy.\n\nBy embracing nudity, we are not only fostering a more relaxed and comfortable work environment, but also promoting a culture of trust, respect, and inclusivity. We believe that this policy will be a game-changer for our company, and we're excited to see the positive impact it will have on our employees and our business.\n\n*** Removes underwear restrictions  ***\n*** Overwear sets with a sluttiness rating of up to 80 ***\n\nSo, join us in embracing this new era of transparency and freedom. Together, let's create a workplace that is truly one-of-a-kind.",
        cost = 25000,
        toggleable = True,
        own_requirement = minimal_coverage_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = minimal_coverage_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority": 5})

    global maximal_arousal_uniform_policy
    maximal_arousal_uniform_policy = Policy(name = "Maximal Arousal Uniform Policy",
        desc = f"{b_name} Maximal Arousal Uniform Policy: Unleashing Your Inner Seductress\n\nAt {b_name}, we believe that confidence and self-expression are key to unlocking your full potential. That's why we're introducing our Maximal Arousal Uniform Policy, designed to give you the freedom to express yourself in the most alluring and seductive way possible.\n\nOur new policy is all about embracing your inner seductress and unleashing your full sensual power. With no restrictions on clothing items or accessories, you'll be able to create a look that's as bold and daring as you are.\n\nTo be clear, our uniform policy has no limits on sluttiness - the more provocative, the better. We want you to feel empowered to express yourself in the most arousing way possible, without fear of judgment or reprisal.\n\n*** Removes all uniform sluttiness limits ***\n\nSo, don't hold back - let your hair down, show some skin, and unleash your inner vixen. We can't wait to see the incredible things you'll achieve when you're feeling confident, sexy, and unstoppable.",
        cost = 50000,
        toggleable = True,
        own_requirement = corporate_enforced_nudity_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = corporate_enforced_nudity_policy,
        extra_arguments = {"uniform_disobedience_priority": 6})

    global male_focused_marketing_policy
    male_focused_marketing_policy = Policy(name = "Male Focused Modelling",
        desc = f"{b_name} Male Focused Modelling: Unlocking New Markets and Opportunities\n\n*** Increases marketing effectiveness based on outfit sluttiness ***\n\nAt {b_name}, we're always looking for ways to stay ahead of the curve and reach new heights of success. That's why we're introducing our Male Focused Modelling policy, designed to tap into the lucrative market of male-focused advertising.\n\nBy embracing a more provocative and alluring approach to marketing, we're confident that we can increase our market reach and unlock new opportunities for growth. And with our new policy, the more daring and seductive our marketing staff's outfits, the greater the reward.\n\nHere's how it works: for every point of outfit Sluttiness worn by our marketing staff, our market reach increases by an additional 1%. And with several new duties unlocked for Marketing and Supply staff, we're giving our team the tools they need to succeed in this exciting new market.\n\nSo, get ready to take our marketing efforts to the next level with Male Focused Modelling. With its unique blend of style, seduction, and savvy business sense, we're confident that this policy will be a game-changer for our company.",
        cost = 500,
        toggleable = True,
        own_requirement = strict_uniform_policy,
        dependant_policies = strict_uniform_policy)

    global creative_colored_uniform_policy
    creative_colored_uniform_policy = Policy(
        name = "Relaxed Uniform Colour Policy",
        cost = 1000,
        desc = f"{b_name} Relaxed Uniform Colour Policy: Adding a Pop of Personality to Your Workwear\n\n*** Allows employees to select their own uniform colors ***\n\nAt {b_name}, we believe that your work attire should be an extension of your personality, not a restriction. That's why we're introducing our Relaxed Uniform Colour Policy, designed to give you the freedom to express yourself through a wider range of colors and styles.\n\nSay goodbye to dull, monotonous uniforms and hello to a world of vibrant colors and bold patterns. With our new policy, you'll be able to add a pop of personality to your workwear, making you feel more confident, creative, and expressive.\n\nWhether you're looking to make a statement or simply want to add a bit of flair to your outfit, our Relaxed Uniform Colour Policy has got you covered. So, don't be afraid to get creative and show off your unique style - we can't wait to see the amazing things you'll come up with!\n\nWith this policy, we're giving you the freedom to be yourself, both in and out of the office. So, go ahead, express yourself, and make your workwear truly unforgettable.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )

    global personal_bottoms_uniform_policy
    personal_bottoms_uniform_policy = Policy(
        name = "Relaxed Uniform Bottoms Policy",
        cost = 2000,
        desc = f"{b_name} Relaxed Uniform Bottoms Policy: Giving You the Freedom to Choose\n\n*** Let's employees wear their preference between a skirt or pants ***\n\nAt {b_name}, we believe that comfort and style go hand-in-hand. That's why we're introducing our Relaxed Uniform Bottoms Policy, designed to give you the freedom to choose the bottoms that make you feel confident and expressive.\n\nSay goodbye to restrictive uniform policies and hello to a world of possibilities. With our new policy, you'll be able to choose from a wide range of bottoms, from skirts and shorts to pants and more.\n\nWhether you're looking for a more relaxed fit or want to make a fashion statement, our Relaxed Uniform Bottoms Policy has got you covered. We're giving you the freedom to choose the bottoms that make you feel like the best version of yourself, both in and out of the office.\n\nSo, go ahead and express yourself with our Relaxed Uniform Bottoms Policy. We can't wait to see the amazing things you'll come up with when you're feeling confident, comfortable, and stylish.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )

    global casual_friday_uniform_policy
    casual_friday_uniform_policy = Policy(
        name = "Casual Friday Uniform Policy",
        cost = 2000,
        desc = f"{b_name} Casual Friday Uniform Policy: Kicking Off the Weekend in Style\n\n*** No uniforms on fridays ***\n\nAt {b_name}, we believe that Fridays are a time to unwind and get ready for the weekend. That's why we're introducing our Casual Friday Uniform Policy, designed to give you the freedom to dress down and express yourself in a more relaxed way.\n\nSay goodbye to stuffy uniforms and hello to a more laid-back vibe. With our new policy, you'll be able to trade in your formal attire for something a little more casual and comfortable.\n\nWhether you're looking to show off your personal style or just want to take it easy, our Casual Friday Uniform Policy is the perfect way to kick off the weekend. So, go ahead and ditch the tie, slip on some jeans, and get ready to take on the day in a whole new way.\n\nWe're excited to see how you'll express yourself on Casual Fridays. So, don't be afraid to get creative and show us your unique style!",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )

    global creative_skimpy_uniform_policy
    creative_skimpy_uniform_policy = Policy(
        name = "Uniform Self Expression Policy",
        cost = 10000,
        desc = f"{b_name} Uniform Self Expression Policy: Embracing Your Unique Style\n\n*** Allows employees to dress sluttier than uniforms if they desire ***\n\nAt {b_name}, we believe that self-expression is a fundamental part of who we are. That's why we're introducing our Uniform Self Expression Policy, designed to give you the freedom to express yourself through your work attire.\n\nWe're throwing out the rulebook and giving you the power to create a uniform that truly reflects your personality. Whether you're into bold colours, eclectic patterns, or statement pieces, we want to see it.\n\nOur Uniform Self Expression Policy is all about embracing your unique style and showcasing your individuality. We believe that when you feel confident and expressive in what you're wearing, you'll be more productive, creative, and happy.\n\nSo, don't be afraid to take risks and try new things. We're excited to see how you'll express yourself through your uniform and can't wait to see the amazing things you'll come up with. Remember, your uniform is a reflection of you - so make it count!",
        toggleable = True,
        own_requirement = [corporate_enforced_nudity_policy, creative_colored_uniform_policy],
        dependant_policies = [corporate_enforced_nudity_policy, creative_colored_uniform_policy]
    )

    global dress_code_policy
    dress_code_policy = Policy(
        name = "Dress Code",
        cost = 500,
        desc = f"{b_name} Dress Code: Elevating Your Style and Confidence\n\nAt {b_name}, we believe that the way you dress can elevate your confidence, creativity, and overall performance. That's why we're introducing our new Dress Code policy, designed to inspire you to look and feel your best.\n\nOur Dress Code is all about embracing your personal style while maintaining a level of professionalism that reflects our company values. We encourage you to express yourself through your attire, whether that's through bold colours, statement pieces, or classic elegance.\n\nWe want you to feel confident and comfortable in what you're wearing, so we've kept our Dress Code guidelines simple and flexible. We trust your judgment and want to see your unique style shine through.\n\nRemember, your attire is an extension of your personality and a reflection of our company culture. So, take pride in your appearance, be creative, and have fun with it! We can't wait to see the amazing things you'll achieve when you're feeling confident and stylish.",
        toggleable = True,
        own_requirement = casual_uniform_policy
    )

    global easier_access_policy
    easier_access_policy = Policy(
        name = "Easier Access Policy",
        cost = 2000,
        desc = f"{b_name} Easier Access Policy: Streamlining Our Work Environment\n\nAt {b_name}, we're always looking for ways to improve our workflow and productivity. That's why we're introducing our Easier Access Policy, designed to make it easier for employees to move around the workplace and access the resources they need.\n\nAs part of this policy, we're implementing a new dress code requirement: all employees are required to wear skirts while working, unless given a specific uniform or the Relaxed Uniform Bottoms Policy is active. This will help to create a more streamlined and efficient work environment, while also promoting a sense of professionalism and respect.\n\nWe believe that this policy will have a positive impact on our workplace culture and productivity. By wearing skirts, employees will be able to move more freely and easily, without the restrictions of pants or other clothing items. We're excited to see the benefits of this policy and look forward to your cooperation and support.\n\nRemember, our goal is to create a workplace that is efficient, productive, and respectful. We're confident that our Easier Access Policy will help us achieve this goal.",
        toggleable = True,
        own_requirement = dress_code_policy,
        dependant_policies = dress_code_policy
    )

    global commando_uniform_policy
    commando_uniform_policy = Policy(
        name = "Commando Dress Code Policy",
        cost = 10000,
        desc = f"{b_name} Commando Dress Code Policy: Embracing Freedom and Comfort\n\nAt {b_name}, we're always looking for ways to promote comfort and confidence in the workplace. That's why we're introducing our Commando Dress Code Policy, designed to give employees the freedom to choose how they want to dress.\n\nThis policy is simple: employees are allowed to go commando, without wearing panties, if they choose to do so. We believe that this will help to create a more relaxed and comfortable work environment, where employees can focus on their work without distractions.\n\nPlease note that this policy is not mandatory, and employees are free to wear panties if they choose to do so. We respect each individual's personal preferences and boundaries, and we want to ensure that everyone feels comfortable and confident in their own skin.\n\nWe're excited to offer this policy as an option for our employees, and we're confident that it will have a positive impact on our workplace culture and productivity. So, feel free to go commando if you want to - we're all about embracing freedom and comfort here at {b_name}!",
        toggleable = True,
        own_requirement = [corporate_enforced_nudity_policy, dress_code_policy],
        dependant_policies = dress_code_policy
    )

    global mandatory_vibe_policy
    mandatory_vibe_policy = Policy(
        name = "Mandatory Vibrator Policy",
        cost = 30000,
        desc = f"{b_name} Mandatory Vibrator Policy: Boosting Productivity and Pleasure\n\nAt {b_name}, we're always looking for innovative ways to enhance our work environment and boost productivity. That's why we're introducing our Mandatory Vibrator Policy, designed to take your work experience to the next level.\n\nThis policy requires all employees to wear a vibrator during work hours, which will raise minimum arousal by 15%. We believe that this will not only increase job satisfaction but also improve team efficiency and overall happiness.\n\nPlease note that this policy is most effective when combined with a sluttiness level of 30 or higher. When sluttiness is less than 30, the policy may have a negative impact on person happiness and team efficiency. So, don't be shy - let your hair down and get ready to experience the ultimate in workplace pleasure and productivity.\n\nWe're excited to see the positive impact that this policy will have on our workplace culture and productivity. So, get ready to buzz with excitement and take your work to new heights with our Mandatory Vibrator Policy!",
        toggleable = True,
        own_requirement = maximal_arousal_uniform_policy,
        on_turn_function = mandatory_toys_policy_on_turn,
        on_day_function = mandatory_toys_policy_on_day
    )

    global mandatory_bullet_policy
    mandatory_bullet_policy = Policy(
        name = "Mandatory Bullet Policy",
        cost = 50000,
        desc = f"{b_name} Mandatory Bullet Policy: Taking Pleasure to the Next Level\n\nAt {b_name}, we're committed to creating a work environment that's both productive and pleasurable. That's why we're introducing our Mandatory Bullet Policy, designed to take your work experience to new heights.\n\nThis policy requires all employees to wear a bullet vibrator during work hours, which will raise minimum arousal by 20%. We believe that this will not only increase job satisfaction but also improve team efficiency and overall happiness.\n\nPlease note that this policy is most effective when combined with a sluttiness level of 50 or higher. When sluttiness is less than 50, the policy may have a negative impact on person happiness and team efficiency. So, don't hold back - let your desires shine and get ready to experience the ultimate in workplace pleasure and productivity.\n\nWe're excited to see the positive impact that this policy will have on our workplace culture and productivity. So, get ready to feel the buzz and take your work to new heights with our Mandatory Bullet Policy!",
        toggleable = True,
        own_requirement = mandatory_vibe_policy,
        on_turn_function = mandatory_toys_policy_on_turn,
        on_day_function = mandatory_toys_policy_on_day
    )

    global mandatory_plug_policy
    mandatory_plug_policy = Policy(
        name = "Mandatory Plug Policy",
        cost = 100000,
        desc = f"{b_name} Mandatory Plug Policy: Plug and Play Your Way to Success\n\nAt {b_name}, we're always looking for ways to \"amp up\" our work environment. That's why we're introducing our Mandatory Plug Policy, where \"plug and play\" takes on a whole new meaning.\n\nThis policy requires all employees to wear a plug during work hours, because let's face it, who doesn't love a good plug? And with a 25% increase in minimum arousal, you'll be buzzing with excitement in no time.\n\nJust remember, this policy is most effective when combined with a sluttiness level of 70 or higher. Anything less, and you might be left feeling a little \"disconnected\". So, don't be afraid to get a little \"plugged in\" and take your work to new heights.\n\nWe're excited to see the positive impact that this policy will have on our workplace culture and productivity. And who knows, you might just find that you're \"hooked\" on the feeling. So, go ahead and \"plug in\" - your work (and your pleasure) will thank you!",
        toggleable = True,
        own_requirement = mandatory_bullet_policy,
        on_turn_function = mandatory_toys_policy_on_turn,
        on_day_function = mandatory_toys_policy_on_day
    )

    global uniform_policies_list
    uniform_policies_list.extend((
        strict_uniform_policy,
        relaxed_uniform_policy,
        casual_uniform_policy,
        reduced_coverage_uniform_policy,
        minimal_coverage_uniform_policy,
        corporate_enforced_nudity_policy,
        maximal_arousal_uniform_policy,
        mandatory_vibe_policy,
        mandatory_bullet_policy,
        mandatory_plug_policy,

        male_focused_marketing_policy,
        creative_colored_uniform_policy,
        personal_bottoms_uniform_policy,
        casual_friday_uniform_policy,
        creative_skimpy_uniform_policy,

        dress_code_policy,
        easier_access_policy,
        commando_uniform_policy,
    ))
