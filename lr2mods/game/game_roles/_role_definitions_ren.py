# GENERIC LIST OF ROLES AND ACTIONS ASSOCIATED WITH THAT ROLE
from __future__ import annotations
import renpy
from renpy import persistent
from game.random_lists_ren import get_random_from_weighted_list
from game.major_game_classes.character_related.Person_ren import Person, mc, cousin, lily, aunt, ashley, alexia, ellie, sarah, candace, nora, kaya, city_rep
from game.people.Rebecca.aunt_definition_ren import aunt_unemployed_job
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import dungeon

instapic_role: Role
mother_role: Role
sister_role: Role
aunt_role: Role
cousin_role: Role
erica_role: Role
alexia_role: Role
caged_role: Role
maid_role: Role
affair_role: Role
harem_role: Role
girlfriend_role: Role
harem_role: Role
affair_role: Role
pregnant_role: Role
employee_role: Role
employee_busywork_role: Role
employee_humiliating_work_role: Role
employee_freeuse_role: Role
head_researcher: Role
company_model_role: Role
college_intern_role: Role
IT_director_role: Role
prod_assistant_role: Role
clone_role: Role
caged_role: Role

day = 0
time_of_day = 0
TIER_1_TIME_DELAY = 0
THREESOME_BASE_SLUT_REQ = 80
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""
def always_true(person: Person):
    return True

def init_generic_roles():
    global instapic_role
    instapic_role = Role("On InstaPic", [], hidden = True, on_turn = insta_on_turn, on_day = insta_on_day)
    global dikdok_role
    dikdok_role = Role("On Dikdok", [], hidden = True, on_turn = dikdok_on_turn, on_day = dikdok_on_day)
    global onlyfans_role
    onlyfans_role = Role("On OnlyFanatics", [], hidden = True, on_turn = onlyfans_on_turn, on_day = onlyfans_on_day)

    global trance_role
    trance_role = Role("In a Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day)
    global heavy_trance_role
    heavy_trance_role = Role("In a Deep Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day, looks_like = trance_role)
    global very_heavy_trance_role
    very_heavy_trance_role = Role("In a Very Deep Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day, looks_like = heavy_trance_role)

    global drunk_role
    drunk_role = Role("Tipsy", actions = get_drunk_role_actions(), hidden = True, on_turn = drunk_on_turn, on_day = drunk_on_day)

    global hypno_orgasm_role
    hypno_orgasm_role = Role("Hypno Orgasm", actions = get_hypno_orgasm_role_orgasm_actions(), hidden = True, on_turn = hypno_orgasm_on_turn, internet_actions = get_hypno_orgasm_role_online_actions())

    global lactating_serum_role
    lactating_serum_role = Role("Lactating Serum", get_lactating_serum_role_actions(), hidden = True, on_turn = lactating_serum_on_turn, on_day = lactating_serum_on_day)

    global anal_fetish_role
    anal_fetish_role = Role(role_name ="Anal Fetish", actions = get_anal_fetish_role_actions())
    global breeding_fetish_role
    breeding_fetish_role = Role(role_name = "Breeding Fetish", actions = get_breeding_fetish_role_actions(), on_day = breeding_fetish_role_on_day)
    global cum_fetish_role
    cum_fetish_role = Role(role_name = "Cum Fetish", actions = get_cum_fetish_role_actions())
    global exhibition_fetish_role
    exhibition_fetish_role = Role(role_name = "Exhibitionist", actions = [])

    global slave_role
    slave_role = Role("Slave", get_slave_role_actions(), on_turn = slave_role_on_turn, hidden = False)

    global jealous_sister_role
    jealous_sister_role = Role("Jealous sister", [], hidden = True, on_turn = jealous_sister_on_turn, on_move = None, on_day = jealous_sister_on_day)

    global unemployed_role
    unemployed_role = Role("Unemployed", get_unemployed_role_actions(), hidden = True)
    global unimportant_job_role
    unimportant_job_role = Role("Unimportant Job", get_unimportant_job_role_actions(), hidden = True) # Used for roles where it is relatively simple to get the character to quit their job.
    global critical_job_role
    critical_job_role = Role("Critical Job", [], hidden = True) # Used for role where it is impossible to get the character to quit their job, but they don't have anything else going on.
    global prostitute_role
    prostitute_role = Role("Prostitute", get_prostitute_role_actions(), hidden = True)
    global generic_student_role
    generic_student_role = Role("Student", [], hidden = True)


################
#INTERNET ROLES#
################
#These roles are given to any girl who has an account on the particular site, even if you don't know about it.
def insta_on_turn(the_person: Person):
    return

def insta_on_day(person: Person):
    if renpy.random.randint(0, 100) < 20 + 5 * person.opinion.skimpy_outfits + 5 * person.opinion.showing_her_tits + 5 * person.opinion.showing_her_ass:
        person.event_triggers_dict["insta_generate_pic"] = True # Generates a new post when you view her profile.

def dikdok_on_turn(person: Person):
    return

def dikdok_on_day(person: Person):
    if renpy.random.randint(0, 100) < 20 + 5 * person.opinion.skimpy_outfits + 5 * person.opinion.showing_her_tits + 5 * person.opinion.showing_her_ass:
        person.event_triggers_dict["dikdok_generate_video"] = True

def onlyfans_on_turn(the_person: Person):
    return

def onlyfans_on_day(person: Person):
    underwear_weight = 25 + (10 * person.opinion.lingerie)
    nudes_weight = 25 + (10 * person.opinion(("showing her tits", "showing her ass")))
    dildo_weight = 25 + (10 * person.opinion(("public sex", "masturbating")))

    content_types = [["underwear", underwear_weight], ["nudes", nudes_weight], ["dildo", dildo_weight]] #Decide on what new content she has on her site for the day.
    if person.event_triggers_dict.get("onlyfans_new_boobs_brag", False):
        person.event_triggers_dict["onlyfans_content_type"] = "new_boobs"
        person.event_triggers_dict["onlyfans_new_boobs_brag"] = False
    else:
        person.event_triggers_dict["onlyfans_content_type"] = get_random_from_weighted_list(content_types)
    person.event_triggers_dict["onlyfans_visited_today"] = False

    person.event_triggers_dict["onlyfans_help_today"] = False # Used as a flag for any event that lts you help them make Onlyfans content.

###################
### TRANCE ROLE ###
###################
def trance_on_turn(person: Person):
    person.event_triggers_dict["trance_training_available"] = True
    if renpy.random.randint(0, 100) >= person.suggestibility:
        if person.has_exact_role(very_heavy_trance_role):
            person.remove_role(very_heavy_trance_role)
            person.add_role(heavy_trance_role)
        elif person.has_exact_role(heavy_trance_role):
            person.remove_role(heavy_trance_role)
            person.add_role(trance_role)
        else:
            person.remove_role(trance_role)

def trance_on_day(person: Person):
    # Run 2 extra instances of the on turn to match the standard decay rate of serums.
    trance_on_turn(person)
    trance_on_turn(person)

def trance_train_requirement(person: Person):
    if person == city_rep and person.is_at_work:
        return False # during her visits she can only be trained after seduction
    if not person.trance_training_available:
        return "Trained too recently"
    return True

def get_trance_role_actions():
    trance_training_action = Action("Take advantage of her trance", trance_train_requirement, "trance_train_label",
        menu_tooltip = "Take advantage of her orgasm-induced trance and make some changes while she is highly suggestible.")
    return [trance_training_action]



###################
### DRUNK ROLE ###
###################


def get_drunk_role_actions():
    pass
    return []

def drunk_on_turn(person: Person):
    person.drink_level -= 2
    if person.drink_level <= 0:
        person.drink_level = 0
        person.remove_role(drunk_role)
        person.reset_drunk_level()
    else:
        person.update_drink_level()
    return

def drunk_on_day(person: Person):
    person.drink_level = 0
    person.remove_role(drunk_role)
    person.reset_drunk_level()
    return

#######################
### TRAINABLE ROLES ###
#######################

def hypno_orgasm_on_turn(person: Person):
    person.event_triggers_dict["hypno_orgasmed_recently"] = False

def hypno_trigger_orgasm_requirement(person: Person):
    if person.event_triggers_dict.get("hypno_orgasmed_recently", False):
        return "She needs a break."
    return True

def get_hypno_orgasm_role_orgasm_actions():
    hypno_trigger_orgasm_action = Action("Trigger an orgasm", hypno_trigger_orgasm_requirement, "hypno_trigger_orgasm", menu_tooltip = "You've implanted a trigger word. You can make her cum whenever you want.")
    return [hypno_trigger_orgasm_action]

def get_hypno_orgasm_role_online_actions():
    hypno_trigger_online_action = Action("Trigger an orgasm", hypno_trigger_orgasm_requirement, "hypno_trigger_online", menu_tooltip = "You've implanted a trigger word, it should work over a text message.")
    return [hypno_trigger_online_action]

######################
### Lactating Role ###
######################
def lactating_serum_on_turn(person: Person):
    person.event_triggers_dict["recently_milked"] = False

def lactating_serum_on_day(person: Person):
    lactating_serum_on_turn(person)
    lactating_serum_on_turn(person)

def milk_for_serum_requirement(person: Person):
    if person.lactation_sources <= 0:
        return "She's not lactating"
    if person.event_triggers_dict.get("recently_milked", False):
        return "She's already been milked"
    if mc.energy < 15:
        return "Not enough energy"
    return True

def get_lactating_serum_role_actions():
    milk_for_serum_action = Action("Milk her for serum\n{menu_red}Costs: {energy=15}{/menu_red}", milk_for_serum_requirement, "milk_for_serum_label",
        menu_tooltip = "Those tits contain company property!")
    return [milk_for_serum_action]

################
# Fetish Roles #
################
def fetish_anal_staylate_requirement(person: Person):
    if mc.is_at_office and mc.business.is_open_for_business and person.is_employee:
        return True
    return False

def get_anal_fetish_role_actions():
    fetish_anal_staylate = Action("See me after work", fetish_anal_staylate_requirement, "fetish_anal_staylate_label",
        menu_tooltip = "Ask her to stay late after work day is over.", priority = 10)

    return [fetish_anal_staylate]

def breeding_fetish_role_on_day(person: Person):
    if person.knows_pregnant or person.is_lactating:
        person.change_happiness(2, add_to_log = False)
    elif person.is_highly_fertile and person.arousal_perc < 50: #Always aroused when fertile.
        person.arousal = person.max_arousal * .5

def breeding_fetish_bend_her_over_requirement(person: Person):
    if person.energy < 50:
        return "She's too tired"
    if mc.energy < 50:
        return "You're too tired"
    return True

def breeding_fetish_fuck_requirement(person: Person):
    if persistent.pregnancy_pref == 0:
        return False
    if person.knows_pregnant:
        return False
    return True

def get_breeding_fetish_role_actions():
    breeding_fetish_fuck_action = Action("Offer to knock her up", breeding_fetish_fuck_requirement, "breeding_fetish_fuck",
        menu_tooltip = "She wants to get pregnant, you could help with that.", priority = 10)
    breeding_fetish_bend_her_over_action = Action("Bend her over", breeding_fetish_bend_her_over_requirement, "breeding_fetish_bend_her_over_label",
        menu_tooltip = "Bend her over right here and give your breeding stock a creampie", priority = 10)

    return [breeding_fetish_fuck_action, breeding_fetish_bend_her_over_action]

def cum_fetish_get_dosage_requirement(person: Person):
    if mc.energy < 40 or time_of_day >= 4:
        return "You're too tired"
    return True

def get_cum_fetish_role_actions():
    cum_fetish_get_dosage = Action("Give her a cum dosage", cum_fetish_get_dosage_requirement, "cum_fetish_get_dosage_label",
        menu_tooltip = "Give her cum, right here, right now.", priority = 10)

    return [cum_fetish_get_dosage]

##############
# Slave Role #
##############
def stay_wet_requirement(person: Person):
    return not person.stay_wet

def calm_down_requirement(person: Person):
    return person.stay_wet

def collar_slave_requirement(person: Person):
    return not person.slave_collar

def slave_trim_pubes_requirement(person: Person):
    return not person.has_relation_with_mc

def slave_shave_head_requirement(person: Person):
    return (
        not person.is_affair            # she still has a SO who would notice
        and person.is_at(dungeon)       # only allow in dungeon
        and not person.is_bald          # she is already bald
    )

def uncollar_slave_requirement(person: Person):
    return person.slave_collar

def wakeup_duty_requirement(person: Person):
    if day % 7 == 4:    # not on saturday mornings, so disable button on Fridays
        return "Not available tomorrow"
    if not mc.business.has_queued_crisis("wakeup_duty_label"):
        return True
    return "Alarm duty already set."

def get_slave_role_actions():
    stay_wet_action = Action("Stay wet", stay_wet_requirement, "stay_wet_label",
        menu_tooltip = "Order your slave to stay aroused at all times.", priority = 20)
    calm_down_action = Action("Calm down", calm_down_requirement, "calm_down_label",
        menu_tooltip = "Let your slave calm down.", priority = 20)
    slave_trim_pubes_action = Action("Trim pubes", slave_trim_pubes_requirement, "slave_trim_pubes_label",
        menu_tooltip = "Order her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.", priority = 20)
    slave_shave_head_action = Action("Shave her head", slave_shave_head_requirement, "slave_shave_head_label",
        menu_tooltip = "Make her submission complete by shaving her head.", priority = 20)

    collar_slave_action = Action("Place collar on [the_person.title]", collar_slave_requirement, "slave_collar_person_label",
        menu_tooltip = "Put a collar of ownership on the target, ensure that their obedience stays high.", priority = 20)
    uncollar_slave_action = Action("Remove collar from [the_person.title]", uncollar_slave_requirement, "slave_collar_person_label",
        menu_tooltip = "Remove the collar, declaring them a free spirit.", priority = 20)

    wakeup_duty_action = Action("Wake me up in the morning", wakeup_duty_requirement, "wakeup_duty_label", menu_tooltip = "Have your slave wake you up in the morning", priority = 20)

    return [stay_wet_action, calm_down_action, collar_slave_action, uncollar_slave_action, slave_trim_pubes_action, slave_shave_head_action, wakeup_duty_action]

def slave_role_on_turn(person: Person):
    if person.stay_wet and person.arousal_perc < 50:
        person.arousal = person.max_arousal * .5
    if person.slave_collar and person._obedience < 150:
        person._obedience = 150

#######################
# Jealous Sister Role #
#######################
def jealous_act_get_score(the_act):
    if the_act == "foreplay":
        return 1
    if the_act == "oral":
        return 2
    if the_act == "anal":
        return 4
    return 3    #Use vaginal as the default. Jealous sister assumes you are fucking if she doesn't know the act

def jealous_sister_on_turn(person: Person):
    if len(person.jealous_witness_publix_sex_list()) > 0:
        the_score = 1
        for act in person.jealous_witness_publix_sex_list():
            if jealous_act_get_score(act) > the_score:
                the_score = jealous_act_get_score(act)
        jealous_string = f"You were fooling around in front of everybody at {person.location.formal_name}!"
        person.add_jealous_event(jealous_string, the_score)
        person.event_triggers_dict["jealous_public_act"] = []

def jealous_sister_on_day(person: Person):
    #Use this function to determine if she is going to act on jealous score. also can check for date events here.
    return

###################
### OTHER ROLES ###
###################
def offer_to_hire_requirement(person: Person):
    if person.is_employee:
        return False
    if person == cousin:
        return False    # only allow hire by blackmail
    if person == lily and person.has_role(generic_student_role):
        return False    # lily has her own offer to hire her when she's a student
    if person == aunt and person.has_job(aunt_unemployed_job):
        return False    # aunt has her own offer to hire her when she's unemployed
    if person in (ashley, alexia, ellie, sarah, candace, nora, kaya, city_rep):
        return False    # these have their own employment stories
    if person.int < 3 and person.charisma < 3 and person.focus < 3:
        return "You think she's not qualified enough"
    if mc.business.at_employee_limit:
        return "At employee limit"
    return True

def get_unemployed_role_actions():
    unemployed_hire_action = Action("Offer to hire her at [mc.business.name]", offer_to_hire_requirement, "unemployed_offer_hire")
    return [unemployed_hire_action]

def get_unimportant_job_role_actions():
    unimportant_hire_action = Action("Offer to hire her at [mc.business.name]", offer_to_hire_requirement, "unimportant_job_offer_hire")
    return [unimportant_hire_action]

def prostitute_requirement(person: Person):
    if not mc.business.has_funds(200):
        "Not enough cash"
    elif person.sexed_count >= 1:
        "She's worn out. Maybe later."
    return True

def get_prostitute_role_actions():
    prostitute_action = Action("Pay her for sex\n{menu_red}Costs: $200{/menu_red}", prostitute_requirement, "prostitute_label",
        menu_tooltip = "You know she's a prostitute, pay her to have sex with you.", priority = 10)
    prostitute_hire_action = Action("Offer to hire her at [mc.business.name]", offer_to_hire_requirement, "prostitute_hire_offer", priority = 10)
    return [prostitute_action, prostitute_hire_action]
