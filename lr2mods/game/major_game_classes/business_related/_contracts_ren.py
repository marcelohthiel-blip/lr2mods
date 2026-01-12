from __future__ import annotations
import renpy
from game.random_lists_ren import get_random_from_weighted_list
from game.major_game_classes.business_related.Contract_ren import Contract
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign
from game.major_game_classes.serum_related.SerumTrait_ren import SerumTrait, list_of_traits
from game.major_game_classes.game_logic.Room_ren import strip_club
from game.major_game_classes.serum_related.serums._serum_traits_T0_ren import mc, primitive_serum_prod, suggestion_drugs_trait, caffeine_trait, birth_control_suppression
from game.major_game_classes.serum_related.serums._serum_traits_T1_ren import volatile_reaction
from game.people.Nora.nora_definition_ren import get_nora_contract
from game.people.Jennifer.jennifer_definition_ren import get_vandalay_contract

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -2 python:
"""

def generate_contract(contract_tier = 0, research_tier = None) -> Contract:
    '''
    Generates a new contract based on the current research tier and contract tier.
    The contract will have a primary and secondary aspect based on the traits of the serum design.
    param contract_tier: The tier of the contract, which affects the amount desired and the length of the contract.
    param research_tier: The tier of the research, which affects the traits that can be added to the serum design.
    '''

    def get_random_trait_from_tag(tag, research_tier) -> SerumTrait | None:
        return get_random_from_weighted_list([[t, (t.tier + 1) * 2] for t in (x for x in list_of_traits if x.researched and x.tier <= research_tier and x.has_tag(tag))])

    if research_tier is None:
        research_tier = mc.business.research_tier

    serum = SerumDesign()
    serum.add_trait(get_random_trait_from_tag("Production", research_tier) or primitive_serum_prod)

    base_tag = ""
    if serum.slots >= 2:  # key part of serums is suggestion / energy / pregnancy
        ran_num = renpy.random.randint(0, 2)
        if ran_num == 0:
            base_tag = "Suggest"
            serum.add_trait(get_random_trait_from_tag(base_tag, research_tier) or suggestion_drugs_trait)
        elif ran_num == 1:
            base_tag = "Energy"
            serum.add_trait(get_random_trait_from_tag(base_tag, research_tier) or caffeine_trait)
        else:
            base_tag = "Pregnancy"
            serum.add_trait(get_random_trait_from_tag(base_tag, research_tier) or birth_control_suppression)

    count = 0
    while serum.slots_used < serum.slots and count < 10: # try to add traits in a loop for a max of 10 tries
        trait: SerumTrait = get_random_from_weighted_list(
            [[t, (t.tier + 1) * 2] for t in
                (x for x in list_of_traits if x.researched
                    and x.tier <= research_tier
                    and x not in (volatile_reaction, )
                    and not x.has_tag((base_tag, "Production"))
                    and x not in serum.traits)]
        )
        if trait and serum.can_add_trait(trait):
            serum.add_trait(trait)
        count += 1

    serum.generate_side_effects(add_to_log = False)

    aspect_list = ["mental", "physical", "sexual", "medical"]
    aspect_value_list = [serum.mental_aspect, serum.physical_aspect, serum.sexual_aspect, serum.medical_aspect]

    sorted_aspect_list = sorted(((value, index) for index, value in enumerate(aspect_value_list)), reverse=True)

    # pick primary and secondary aspect
    primary_aspect = aspect_list[sorted_aspect_list[0][1]]
    secondary_aspect = aspect_list[sorted_aspect_list[1][1]]

    contract_name, contract_description = get_contract_description(primary_aspect, secondary_aspect, contract_tier)

    contract_length = 3 + (renpy.random.randint(1, 3 + contract_tier) + (renpy.random.randint(0, contract_tier) * 3))

    amount_desired = 5 * (contract_tier + renpy.random.randint(1, 3)) * (contract_tier + renpy.random.randint(1, 2))

    # print("{} - duration: {} doses: {} {} {}".format(contract_name, contract_length, amount_desired, primary_aspect, secondary_aspect))

    new_contract = Contract(contract_name, contract_description, contract_length,
        mental_requirement = serum.mental_aspect, physical_requirement = serum.physical_aspect,
        sexual_requirement = serum.sexual_aspect, medical_requirement = serum.medical_aspect,
        flaw_tolerance = serum.flaws_aspect, attention_tolerance = serum.attention, amount_desired = amount_desired)

    # reset side effects
    serum.side_effects.clear()
    serum.flaws_aspect = 0

    new_contract.reference_design = serum

    return new_contract

def get_contract_description(primary_aspect: str, secondary_aspect: str, contract_tier):
    contract_name = ""
    contract_description = ""
    if primary_aspect == "mental":
        if secondary_aspect == "physical":
            contract_name = "Eltaro Co. Employee Boosters"
            contract_description = "Eltaro Co. is looking for a way to improve the general productivity of their employees by sharpening both body and mind."

        elif secondary_aspect == "sexual":
            contract_name = "Iris Cosmetics Makeup Additive"
            contract_description = "Having a beautiful mind is just as important as clear skin or perfect makeup. Iris Cosmetics is looking for something to promote that feeling in their customers, and a little sex appeal always helps sell products."

        elif secondary_aspect == "medical":
            contract_name = "Tresmon Pharmaceuticals Neurotropics"
            contract_description = "Tresmon Pharmaceuticals has a number of clients interested in thought-boosting drugs, and they're willing to pay top dollar for you to fill those orders for them."

    elif primary_aspect == "physical":
        if secondary_aspect == "mental":
            contract_name = "University Athletics Council Request"
            contract_description = "The university athletics council is looking for a way to improve the performance of their key athletes, on and off the field."

        elif secondary_aspect == "sexual":
            contract_name = "University Cheerleader Council Request"
            contract_description = "Attendance at recent sporting events has been down, and many are blaming the new \"respectful\" cheerleading uniforms. Cheer leadership is looking for a new workout enhancer, ideally one that will reduce resistance to a return to the old uniform."

        elif secondary_aspect == "medical":
            contract_name = "Gary's Power Lifting Additive"
            contract_description = "Gary runs a local gym, and he's always on the look out for another performance enhancing drug to peddle to those looking for a quick path to fitness."

    elif primary_aspect == "sexual":
        if secondary_aspect == "mental":
            contract_name = "Personal Business Supplies"
            contract_description = "A C-suite executive of a nearby business has a secretary they want to turn into a, quote, \"Cock drunk bimbo-slut\", and they're willing to pay good money for a large stock of serum to make it happen."

        elif secondary_aspect == "physical":
            if mc.business.event_triggers_dict.get("foreclosed_stage", 0) != 0:
                contract_name = "Luxury Escorts"
                contract_description = "A local escort service is interested in anything that will give their girls more sex appeal and endurance. Bigger tits, toned bodies, whatever you think they need to boost profits."
            else:
                contract_name = strip_club.formal_name
                contract_description = strip_club.owner + " is interested in anything that will give his girls more sex appeal while they're stripping on stage. Bigger tits, toned bodies, whatever you think they need to get more twenties on the stage."

        elif secondary_aspect == "medical":
            contract_name = "A Questionable Contact"
            contract_description = "An individual using an obviously fake name has requested \"Anything that gets 'em horny, wet, and ready to suck dick.\". Their name might be fake, but their cash definitely isn't."

    elif primary_aspect == "medical":
        if secondary_aspect == "mental":
            contract_name = "Tresmon Pharmaceuticals Research Materials"
            contract_description = "Tresmon Pharmaceuticals is intensely interested in our work on mind–altering substances. They want a stock of their own to perform advanced R&D with."

        elif secondary_aspect == "physical":
            contract_name = "Military Research Study"
            contract_description = "The military is interested in potential \"super soldier\" applications, and they're willing to work with civilian sources to obtain research material."

        elif secondary_aspect == "sexual":
            contract_name = "Female Libido Enhancements"
            contract_description = "Low libido is a side effect for many different medications. Tresmon Pharmaceuticals is interested in an additive that might lessen or eliminate that problem from their existing drugs."

    return contract_name, contract_description

def get_designs_that_satisfy_contract(contract: Contract) -> list[SerumDesign]:
    return [design for design in mc.business.serum_designs if design.researched and contract.check_serum(design)]

def get_design_names_that_satisfy_contract(contract: Contract) -> str:
    usable_designs = get_designs_that_satisfy_contract(contract)
    if usable_designs:
        return ", ".join([x.name for x in usable_designs])
    return "None"

#Use this function to add any story specific contracts.
def generate_story_contracts() -> list[Contract]:
    story_contracts = []
    nora_contract = get_nora_contract()
    if nora_contract:
        story_contracts.append(nora_contract)
    vandalay_contract = get_vandalay_contract()
    if vandalay_contract:
        story_contracts.append(vandalay_contract)
    return story_contracts
