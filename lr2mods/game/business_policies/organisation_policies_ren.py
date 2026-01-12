from __future__ import annotations
from game.game_roles.business_roles._duty_definitions_ren import extra_paperwork_duty
from game.main_character.MainCharacter_ren import mc
from game.major_game_classes.business_related.Policy_ren import Policy

organisation_policies_list = list[Policy] = []
unmapped_policies_list = list[Policy] = []

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init 2 python:
"""
## Organisation Policies ##
def increase_max_employee_size(amount):
    mc.business.max_employee_count += amount

def business_contract_increase(change_amount = 1):
    mc.business.max_active_contracts += change_amount

def business_contract_offered_increase(change_amount = 1):
    mc.business.max_offered_contracts += change_amount

def business_contract_increase_1_on_turn():
    mc.business.change_team_effectiveness(-len(mc.business.active_contracts))

def unlock_expensive_camera():
    mc.business.event_triggers_dict["has_expensive_camera"] = True

def strict_enforcement_on_apply():
    mc.business.standard_efficiency_drop += 1

def strict_enforcement_on_remove():
    mc.business.standard_efficiency_drop += -1

def draconian_enforcement_on_day():
    for employee in mc.business.employees_at_office:
        employee.change_happiness(-5)

def office_conduct_guidelines_on_day():
    if not mc.business.is_work_day:
        return

    for employee in (x for x in mc.business.employees_at_office if x.sluttiness < 20):
        employee.change_slut(1, 20, add_to_log = False)
        if not employee.has_duty(extra_paperwork_duty):
            mc.business.change_team_effectiveness(-1)
    return

def mandatory_staff_reading_on_day():
    if not mc.business.is_work_day:
        return

    for employee in (x for x in mc.business.employees_at_office if x.sluttiness < 40):
        if employee.sluttiness <= 20:
            employee.change_happiness(-5, add_to_log = False)

        employee.change_slut(1, 40, add_to_log = False)
        if not employee.has_duty(extra_paperwork_duty):
            mc.business.change_team_effectiveness(-1)
    return

def superliminal_office_messaging_on_day():
    if not mc.business.is_work_day:
        return

    for an_employee in (x for x in mc.business.employee_list if x.sluttiness < 60):
        if an_employee.sluttiness <= 20:
            an_employee.change_happiness(-10)
            if not an_employee.has_duty(extra_paperwork_duty):
                mc.business.change_team_effectiveness(-3)
        else:
            if not an_employee.has_duty(extra_paperwork_duty):
                mc.business.change_team_effectiveness(-1)
            an_employee.change_slut(1, 60, add_to_log = False)
    return

def max_attention_increase(amount = 100):
    mc.business.max_attention += amount

def attention_bleed_increase(amount = 10):
    mc.business.attention_bleed += amount

def init_organisation_policies():
    global business_size_1_policy
    business_size_1_policy = Policy(name = "Employee Count Improvement One",
        desc = "Some basic employee management and tracking software will let you hire more employees.\nIncreases max employee count by 2.",
        cost = 500,
        toggleable = False,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 2})

    global business_size_2_policy
    business_size_2_policy = Policy(name = "Employee Count Improvement Two",
        desc = "Improved employee management software yet again increases the number of employees you can comfortably keep around.\nIncreases max employee count by 3.",
        cost = 2000,
        toggleable = False,
        own_requirement = business_size_1_policy,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 5})

    global business_size_3_policy
    business_size_3_policy = Policy(name = "Employee Count Improvement Three",
        desc = "Distributed management roles lets you nearly double the employee count of your business.\nIncreases max employee count by 8.",
        cost = 5000,
        toggleable = False,
        own_requirement = business_size_2_policy,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 10})

    global business_size_4_policy
    business_size_4_policy = Policy(name = "Employee Count Improvement Four",
        desc = "Fully automated payroll calculations, benefit management, and productivity tracking allows for a final, massive jump in maximum business size.\nIncreases max employee count by 20.",
        cost = 10000,
        toggleable = False,
        own_requirement = business_size_3_policy,
        on_buy_function = increase_max_employee_size,
        extra_arguments = {"amount": 15})

    global business_contract_increase_1_policy
    business_contract_increase_1_policy = Policy(name = "Streamlined Contract Processing.",
        desc = "Managing multiple contracts at once is difficult, but the extra payout offered makes the trouble worth it.\nAllows you to have one additional active contract at a time, but reduces business efficiency by 1 per turn per active contract.",
        cost = 500,
        toggleable = False,
        on_buy_function = business_contract_increase,
        on_turn_function = business_contract_increase_1_on_turn)

    global business_contract_offer_increase_1_policy
    business_contract_offer_increase_1_policy = Policy(name = "Favoured Business Partnerships",
        desc = "Forging strong relationships with repeat customers makes it more likely they'll turn to you when they have special requests.\nIncreases the number of contracts offered every Monday by 1.",
        cost = 1000,
        toggleable = False,
        own_requirement = business_contract_increase_1_policy,
        on_buy_function = business_contract_offered_increase)

    global business_contract_increase_2_policy
    business_contract_increase_2_policy = Policy(name = "Multi-Contract Business Strategy.",
        desc = "Focus your business on managing multiple contract at once.\nIncreases the maximum number of active contracts by 1, but reduces business efficiency by 1 per turn per active contract.",
        cost = 3000,
        toggleable = False,
        own_requirement = business_contract_offer_increase_1_policy,
        on_buy_function = business_contract_increase,
        on_turn_function = business_contract_increase_1_on_turn)

    global business_contract_offer_increase_2_policy
    business_contract_offer_increase_2_policy = Policy(name = "Public Relationship Management",
        desc = "Further reinforce your relationship with common business partners, encouraging them to present you with contracts first and often.\nIncreases the number of contracts offered every Monday by 1.",
        cost = 5000,
        toggleable = False,
        own_requirement = business_contract_offer_increase_1_policy,
        on_buy_function = business_contract_offered_increase)

    global public_advertising_license_policy
    public_advertising_license_policy = Policy(name = "Public Advertising License",
        desc = "After filling out the proper paperwork and familiarizing yourself with publishing regulations you will be ready to advertise your product in print publications.\nAllows you to pick a girl as your company model and launch ad campaigns.",
        cost = 2500,
        on_buy_function = unlock_expensive_camera,
        toggleable = False)

    global office_punishment
    office_punishment = Policy(name = "Office Punishment",
        desc = "Establish a formal set of punishments for business policy violations. Allows you to punish employees for infractions they have committed. More severe infractions enable more severe punishments.\nUnlocks new duty for HR employees to find infractions for you.",
        cost = 700,
        toggleable = False)

    global corporal_punishment
    corporal_punishment = Policy(name = "Corporal Punishment",
        desc = "Updates to the company punishment guidelines allow for punishments involving physical contact.\nResearch into the topic has shown sexual punishment to be extremely effective in cases of severe disobedience.",
        cost = 2000,
        toggleable = False,
        own_requirement = office_punishment)

    global strict_enforcement
    strict_enforcement = Policy(name = "Strict Enforcement",
        desc = "By strictly applying the letter, rather than spirit, of the company punishment guidelines you are able to treat infractions as more severe than they initially seem.\nAll infraction severities are increased by one while this policy is active, but the increased administrative work lowers business efficiency by one per employee every day.",
        cost = 2500,
        toggleable = True,
        own_requirement = office_punishment,
        on_apply_function = strict_enforcement_on_apply,
        on_remove_function = strict_enforcement_on_remove)

    global draconian_enforcement
    draconian_enforcement = Policy(name = "Draconian Enforcement",
        desc = "Each policy infraction is to be punished to the utmost tolerable.\nAll infraction severities are increased by one, but the restrictive office environment affects company morale, lowering all employee happiness by -5 per day.",
        cost = 5000,
        toggleable = True,
        own_requirement = strict_enforcement,
        on_day_function = draconian_enforcement_on_day,
        dependant_policies = strict_enforcement)

    global bureaucratic_nightmare
    bureaucratic_nightmare = Policy(name = "Bureaucratic Nightmare",
        desc = "Trap employees within a web of intentionally vague and misleading rules and regulations.\nUnlocks a new duty that allows for the creation of minor infractions at will at the cost of business efficiency.",
        cost = 2500,
        toggleable = False,
        own_requirement = office_punishment)

    global theoretical_research
    theoretical_research = Policy(name = "Theoretical Research",
        desc = "Unlocks Theoretical Research duty for R&D staff.\nWhen assigned the employee will create 1 point of Clarity for every 5 Research Points they produce.",
        cost = 300,
        toggleable = False)

    global research_journal_subscription
    research_journal_subscription = Policy(name = "Study Outside Research",
        desc = "Unlocks Journal Studies duty for R&D staff.\nWhen assigned the employee will create 1 point of Clarity for every 5 Research Points they produce.\nJournal subscriptions will cost an additional $10 per person per work day.",
        cost = 1000,
        toggleable = False,
        own_requirement = theoretical_research)

    global practical_experimentation
    practical_experimentation = Policy(name = "Practical Experimentation",
        desc = "Unlocks Practical Experimentation Duty. Provide additional supplies to your R&D staff and encourage them to pursue promising areas of research.\nRequires 5 units of Serum Supply per researcher and produces 1 point of Clarity for every 5 Research Points they produce.",
        cost = 500,
        toggleable = True,
        own_requirement = theoretical_research)

    global office_conduct_guidelines
    office_conduct_guidelines = Policy(name = "Office Conduct Guidelines",
        desc = 'Set and distribute guidelines for staff behaviour. Daily emails will remind them to be "pleasant, open, and receptive to all things.".\nIncreases all staff Sluttiness by 1 per day, to a maximum of 20.\nReduces business efficiency by 1 per employee affected.',
        cost = 700,
        toggleable = True,
        on_day_function = office_conduct_guidelines_on_day)

    global mandatory_staff_reading
    mandatory_staff_reading = Policy(name = "Mandatory Staff Reading",
        desc = "Distribute copies of {i}Your Place in the Work Place{/i}—a guidebook for women, written in the 60's by a womanising executive.\nIncreases all staff Sluttiness by an additional 1 per day, to a maximum of 40.\nReduces business efficiency by 1 per employee affected, and reduces happiness of women with Sluttiness 20 or lower by 5 per day.",
        cost = 1500,
        toggleable = True,
        active_requirement = office_conduct_guidelines,
        on_day_function = mandatory_staff_reading_on_day,
        dependant_policies = office_conduct_guidelines)

    global superliminal_office_messaging
    superliminal_office_messaging = Policy(name = "Supraliminal Messaging",
        desc = "Fill the office with overtly sexual content. Distribute pin-up girl calendars, provide access to a company porn account, hang nude posters.\nIncreases staff Sluttiness by 1 per day, to a maximum of 60. Reduces business efficiency by 1 per employee affected, or by 3 if her Sluttiness is 20 or lower.\nReduces happiness of women with Sluttiness 20 or lower by 10 per day.",
        cost = 7500,
        toggleable = True,
        active_requirement = mandatory_staff_reading,
        on_day_function = superliminal_office_messaging_on_day,
        dependant_policies = mandatory_staff_reading)

    global max_attention_increase_1_policy
    max_attention_increase_1_policy = Policy(name = "National Sales",
        desc = "Begin working with clients all over the country.\nThe local authorities are less likely to take an interest in you if your product doesn't always end up in their backyard.\nIncrease the attention threshold by 100.",
        cost = 2000,
        toggleable = False,
        on_buy_function = max_attention_increase)

    global attention_bleed_increase_1_policy
    attention_bleed_increase_1_policy = Policy(name = "Public Charity Work",
        desc = "Sponsor a few local charities to improve the public perception of your business.\nReduces pressure for authorities to take action against you, lowering Attention by an additional 10 per day.",
        cost = 2000,
        toggleable = False,
        on_buy_function = attention_bleed_increase)

    global attention_floor_increase_1_policy
    attention_floor_increase_1_policy = Policy(name = "Establish Cover Story",
        desc = "Establish a cover story for your business.\nThis will reduce the amount of attention generated when selling a dose of serum by 1.",
        cost = 2000,
        toggleable = True)

    global organisation_policies_list
    organisation_policies_list.extend((
        business_size_1_policy,
        business_size_2_policy,
        business_size_3_policy,
        business_size_4_policy,
        business_contract_increase_1_policy,
        business_contract_offer_increase_1_policy,
        business_contract_increase_2_policy,
        business_contract_offer_increase_2_policy,
        public_advertising_license_policy,
        office_punishment,
        corporal_punishment,
        strict_enforcement,
        draconian_enforcement,
        bureaucratic_nightmare,
        theoretical_research,
        research_journal_subscription,
        practical_experimentation,
        office_conduct_guidelines,
        mandatory_staff_reading,
        superliminal_office_messaging,
        max_attention_increase_1_policy,
        attention_bleed_increase_1_policy,
        attention_floor_increase_1_policy,
    ))

    # these policies are unlocked by story and not by buying them
    global attention_bleed_increase_2_policy
    attention_bleed_increase_2_policy = Policy(name = "City Hall Internal Sabotage",
        desc = "Reports go missing, meetings are miss-scheduled, and evidence is misfiled. An inside agent down at city hall is making sure it's particularly hard to pin anything on your business.\nLowers Attention by an additional 10 per day.",
        cost = 0,
        toggleable = False,
        on_buy_function = attention_bleed_increase) #Only accessible by corrupting the city rep.

    global attention_floor_increase_2_policy
    attention_floor_increase_2_policy = Policy(name = "Business License",
        desc = "Having the proper licenses and paperwork makes it much easier to sell product without attracting undo attention.\nReduces the amount of attention generated when selling a dose of serum by another 1.",
        cost = 2500,
        toggleable = False) #Only accessible by corrupting the city rep

    global unmapped_policies_list
    unmapped_policies_list.extend((
        attention_bleed_increase_2_policy,
        attention_floor_increase_2_policy,
    ))
