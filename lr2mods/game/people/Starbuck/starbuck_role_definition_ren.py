from __future__ import annotations
import builtins
import renpy
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.game_logic.Room_ren import sex_store
from game.major_game_classes.character_related.Person_ren import Person, perk_system, mc, starbuck, aunt
from game.major_game_classes.clothing_related.Outfit_ren import Outfit
from game.major_game_classes.serum_related.SerumDesign_ren import SerumDesign

TIER_2_TIME_DELAY = 7
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def starbuck_vaginal_skillup_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 2 or person.progress.lust_step < 3:
        return False
    if perk_system.has_stat_perk("Vibrating Cock Ring"):
        return "Already Active"
    if not mc.business.has_funds(500):
        return "Requires: $500"
    return mc.is_at(sex_store)

def starbuck_anal_skillup_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 2 or person.progress.lust_step < 4:
        return False
    if perk_system.has_stat_perk("Perfect Anal Lube"):
        return "Already Active"
    if not mc.business.has_funds(800):
        return "Requires: $800"
    return mc.is_at(sex_store)

def starbuck_foreplay_skillup_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 1 or person.progress.lust_step < 1:
        return False
    if perk_system.has_stat_perk("Small Finger Vibrator"):
        return "Already Active"
    if not mc.business.has_funds(100):
        return "Requires: $100"
    return mc.is_at(sex_store)

def starbuck_oral_skillup_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 1 or person.progress.lust_step < 2:
        return False
    if perk_system.has_stat_perk("Stimulating Lip Balm"):
        return "Already Active"
    if not mc.business.has_funds(250):
        return "Requires: $250"
    return mc.is_at(sex_store)

def starbuck_sex_store_investment_one_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() != 0:
        return False
    if not mc.business.has_funds(1000):
        return "Requires: $1000"
    return True

def starbuck_sex_store_investment_two_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() != 1:
        return False
    if person.days_since_event("shop_stage_one_day") > 7:
        if not mc.business.has_funds(5000):
            return "Requires: $5000"
        return True
    return "Wait for her stock to balance out"

def starbuck_sex_store_investment_three_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() != 2:
        return False
    if person.days_since_event("shop_stage_two_day") > 7:
        if not mc.business.has_funds(15000):
            return "Requires: $15000"
        return True
    return "Wait for her stock to balance out"

def starbuck_sex_store_promo_one_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() == 0:
        return False
    if get_shop_promo_stage() != 1.0:
        return False
    if person.progress.love_step < 2 and person.progress.lust_step < 1 and person.progress.obedience_step < 2:
        return "Requires story progression"
    return True

def starbuck_sex_store_promo_two_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() == 0:
        return False
    if get_shop_promo_stage() != 2.0:
        return False
    if person.progress.love_step < 3 and person.progress.lust_step < 2 and person.progress.obedience_step < 3:
        return "Requires story progression"
    return get_shop_promo_stage() == 2.0 and person.days_since_event("promo_event") > TIER_2_TIME_DELAY

def starbuck_sex_store_promo_three_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 2:
        return False
    if get_shop_promo_stage() != 3.0 or not person.days_since_event("promo_event") > TIER_2_TIME_DELAY:
        return False
    if person.progress.love_step < 4 and person.progress.lust_step < 3 and person.progress.obedience_step < 4:
        return "Requires story progression"
    # if person.sluttiness < 60:
    #     return "Requires: 60+ sluttiness"
    # if person.love < 50:
    #     return "Requires: 50+ Love"
    return True

def starbuck_sex_store_promo_four_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 2:
        return False
    if get_shop_promo_stage() != 4.0 or not person.days_since_event("promo_event") > TIER_2_TIME_DELAY:
        return False
    if person.progress.love_step < 5 and person.progress.lust_step < 3 and person.progress.obedience_step < 5:
        return "Requires story progression"
    # if person.sluttiness < 70:
    #     return "Requires: 70+ sluttiness"
    # if person.love < 60:
    #     return "Requires: 60+ Love"
    return True

def starbuck_sex_store_promo_five_requirement(person: Person):
    if not person.is_at_work or sex_shop_stage() < 3:
        return False
    if get_shop_promo_stage() != 5.0 or not person.days_since_event("promo_event") > TIER_2_TIME_DELAY:
        return False
    if person.progress.love_step < 6 and person.progress.lust_step < 4 and person.progress.obedience_step < 6:
        return "Requires story progression"
    # if person.sluttiness < 90:
    #     return "Requires: 90+ sluttiness"
    # if person.love < 70:
    #     return "Requires: 70+ Love"
    return True

def starbuck_spend_the_night_requirement(person: Person):
    if get_shop_promo_stage() != 6.0 or not person.is_home:
        return False
    if time_of_day != 4:
        return "Only at night"
    return True

def starbuck_close_up_requirement(person: Person):
    if sex_shop_stage() == 0 or not person.is_at_work:
        return False
    if time_of_day != 3:
        return "She closes in the evening"
    return True

def starbuck_anal_fetish_swing_demo_requirement(person: Person):
    return person.is_at_work and person.has_anal_fetish

def sex_shop_cashier_wardrobe_requirement(person: Person):
    return person.progress.obedience_step >= 3

def get_starbuck_role_actions():
    starbuck_vaginal_skillup = Action("Ask about temporarily improving vaginal skill", starbuck_vaginal_skillup_requirement, "starbuck_vaginal_skillup_label")
    starbuck_anal_skillup = Action("Ask about temporarily improving anal skill", starbuck_anal_skillup_requirement, "starbuck_anal_skillup_label")
    starbuck_oral_skillup = Action("Ask about temporarily improving oral skill", starbuck_oral_skillup_requirement, "starbuck_oral_skillup_label")
    starbuck_foreplay_skillup = Action("Ask about temporarily improving foreplay", starbuck_foreplay_skillup_requirement, "starbuck_foreplay_skillup_label")
    starbuck_sex_store_investment_one = Action("Ask about investing in her store", starbuck_sex_store_investment_one_requirement, "starbuck_sex_store_investment_one_label")
    starbuck_sex_store_investment_two = Action("Ask about stock levels", starbuck_sex_store_investment_two_requirement, "starbuck_sex_store_investment_two_label")
    starbuck_sex_store_investment_three = Action("Ask about further investment", starbuck_sex_store_investment_three_requirement, "starbuck_sex_store_investment_three_label")
    starbuck_sex_store_promo_one = Action("Ask how business is going", starbuck_sex_store_promo_one_requirement, "starbuck_sex_store_promo_one_label")
    starbuck_sex_store_promo_two = Action("Ask if advertising is working", starbuck_sex_store_promo_two_requirement, "starbuck_sex_store_promo_two_label")
    starbuck_sex_store_promo_three = Action("Ask if women are coming in", starbuck_sex_store_promo_three_requirement, "starbuck_sex_store_promo_three_label")
    starbuck_sex_store_promo_four = Action("Ask if couples are coming in", starbuck_sex_store_promo_four_requirement, "starbuck_sex_store_promo_four_label")
    starbuck_sex_store_promo_five = Action("Ask if couples are coming in", starbuck_sex_store_promo_five_requirement, "starbuck_sex_store_promo_five_label")
    starbuck_spend_the_night = Action("Spend the night with her", starbuck_spend_the_night_requirement, "starbuck_spend_the_night_label")
    starbuck_close_up = Action("Help close the store {image=time_advance}", starbuck_close_up_requirement, "starbuck_close_up_label")
    starbuck_anal_fetish_swing_demo = Action("Anal Sex Swing Demo", starbuck_anal_fetish_swing_demo_requirement, "starbuck_anal_fetish_swing_demo_label")
    sex_shop_cashier_wardrobe_change = Action("Modify Sex Shop Wardrobe", sex_shop_cashier_wardrobe_requirement, "sex_shop_cashier_wardrobe_label")
    return [starbuck_vaginal_skillup, starbuck_anal_skillup, starbuck_oral_skillup, starbuck_foreplay_skillup, starbuck_sex_store_investment_one,
        starbuck_sex_store_investment_two, starbuck_sex_store_investment_three, starbuck_sex_store_promo_one, starbuck_sex_store_promo_two, starbuck_sex_store_promo_three, starbuck_sex_store_promo_four,
        starbuck_sex_store_promo_five, starbuck_spend_the_night, starbuck_close_up, starbuck_anal_fetish_swing_demo, sex_shop_cashier_wardrobe_change]

def sex_shop_invest_basic_requirement(person: Person):
    if sex_shop_stage() == 0 or not person.is_at_work:
        return False
    if person.event_triggers_dict.get("shop_investment_basic_total", 0) > 5000:
        return "No more investment opportunity."
    if not mc.business.has_funds(1000):
        return "Requires: $1000"
    return True

def sex_shop_invest_advanced_requirement(person: Person):
    if sex_shop_stage() < 2 or not person.is_at_work:
        return False
    if person.event_triggers_dict.get("shop_investment_advanced_total", 0) > 20000:
        return "No more investment opportunity."
    if not mc.business.has_funds(5000):
        return "Requires: $5000"
    return True

def sex_shop_invest_fetish_requirement(person: Person):
    if sex_shop_stage() < 3 or not person.is_at_work:
        return False
    if person.event_triggers_dict.get("shop_investment_fetish_total", 0) > 45000:
        return "No more investment opportunity."
    if not mc.business.has_funds(15000):
        return "Requires: $15000"
    return True

def get_sex_shop_invest_role_actions():
    sex_shop_invest_basic = Action("Invest in more basic inventory", sex_shop_invest_basic_requirement, "sex_shop_invest_basic_label")
    sex_shop_invest_advanced = Action("Invest in more advanced inventory", sex_shop_invest_advanced_requirement, "sex_shop_invest_advanced_label")
    sex_shop_invest_fetish = Action("Invest in more fetish inventory", sex_shop_invest_fetish_requirement, "sex_shop_invest_fetish_label")
    return [sex_shop_invest_basic, sex_shop_invest_advanced, sex_shop_invest_fetish]

def sex_shop_owner_on_turn(person: Person):
    return

def sex_shop_owner_on_day(person: Person): #Use this function to determine if she is going to act on jealous score. also can check for date events here.
    if sex_shop_stage() == 0:
        return
    investment_return = sex_shop_investment_return(person)
    if investment_return == 0:
        return
    mc.business.change_funds(investment_return, stat = "Return On Investments", add_to_log = False)
    mc.business.add_normal_message(f"Sex shop has returned ${investment_return:,.0f} on your investment!")

def sex_shop_introduction_requirement(person: Person):
    return person.is_at_work

def sex_shop_unlock_requirement():
    return aunt.has_event_day("moved_out") and day % 7 == 1 and time_of_day == 2    # Tuesday afternoon

def make_sex_shop_owner(person: Person):
    person.event_triggers_dict["shop_progress_stage"] = 0   #For story purposes
    person.event_triggers_dict["shop_investment_total"] = 0 #For calculation purposes
    person.event_triggers_dict["shop_investment_rate"] = 0  #For balance purposes
    person.event_triggers_dict["shop_investment_basic_total"] = 0
    person.event_triggers_dict["shop_investment_advanced_total"] = 0
    person.event_triggers_dict["shop_investment_fetish_total"] = 0
    person.event_triggers_dict["shop_promo_market_rate"] = 0  #For extra income if we've spent a lot of time on promo videos etc.
    sex_shop_invest_role = Role(role_name ="Sex Shop Invest Role", actions = get_sex_shop_invest_role_actions(), on_turn = sex_shop_owner_on_turn, on_move = None, on_day = sex_shop_owner_on_day, hidden = True)
    person.add_role(sex_shop_invest_role)
    person.set_override_schedule(person.home)   # hide her at home until we need her
    person.add_unique_on_room_enter_event(
        Action("Starbuck's Sex Shop", sex_shop_introduction_requirement, "starbuck_greetings", menu_tooltip = "Starbuck's Sex Shop", priority = 30)
    )
    mc.business.add_mandatory_crisis(
        Action("Starbuck unlock sex shop", sex_shop_unlock_requirement, "sex_shop_unlock_label", priority = 30)
    )

def unlock_sex_shop_and_starbuck():
    sex_store.visible = True
    starbuck.set_override_schedule(None)

def sex_shop_investment_return(person: Person):
    if day % 7 == 6:    # not open on sundays
        return 0
    investment_return = 30
    investment_return += int(person.event_triggers_dict.get("shop_investment_basic_total", 0) * get_shop_investment_rate() * 0.01)
    investment_return += int(person.event_triggers_dict.get("shop_investment_advanced_total", 0) * get_shop_investment_rate() * 0.004)
    investment_return += int(person.event_triggers_dict.get("shop_investment_fetish_total", 0) * get_shop_investment_rate() * 0.004)

    #This function returns a variation of 50% to 150%... is this really what we want?
    return builtins.int(investment_return * (renpy.random.random() + .5))    # make it variable rounded to whole dollars

def sex_shop_investment_average_return():
    investment_return = 30
    investment_return += int(starbuck.event_triggers_dict.get("shop_investment_basic_total", 0) * get_shop_investment_rate() * 0.01)
    investment_return += int(starbuck.event_triggers_dict.get("shop_investment_advanced_total", 0) * get_shop_investment_rate() * 0.004)
    investment_return += int(starbuck.event_triggers_dict.get("shop_investment_fetish_total", 0) * get_shop_investment_rate() * 0.004)
    return investment_return


def starbuck_is_business_partner():
    return sex_shop_stage() >= 1

def sex_shop_stage():
    return starbuck.event_triggers_dict.get("shop_progress_stage", 0)

def get_shop_promo_stage():
    return starbuck.event_triggers_dict.get("shop_investment_rate", 1)

def get_shop_investment_rate():
    return starbuck.event_triggers_dict.get("shop_investment_rate", 1) + starbuck.event_triggers_dict.get("shop_promo_market_rate", 0)

#Use this function to check and make sure an outfit is legal to be added to starbuck's uniform wardrobe.
def sex_shop_owner_outfit_check(outfit: Outfit, outfit_type = "full"):
    if not isinstance(outfit, Outfit):
        return False
    if not outfit.is_legal_in_public:
        return False
    if outfit.vagina_visible or outfit.tits_visible:
        return False
    if starbuck.progress.obedience_step < 3:
        if outfit_type == "full":
            return outfit.outfit_slut_score > 30 and outfit.outfit_slut_score <= 50
        elif outfit_type == "over":
            return outfit.overwear_slut_score > 10 and outfit.overwear_slut_score <= 30
        else:
            return outfit.underwear_slut_score > 10 and outfit.underwear_slut_score <= 30
    else:
        if outfit_type == "full":
            return outfit.outfit_slut_score > 30 and outfit.outfit_slut_score <= max(starbuck.sluttiness, 50)
        elif outfit_type == "over":
            return outfit.overwear_slut_score > 10 and outfit.overwear_slut_score <= max(int(starbuck.sluttiness * .6), 30)
        else:
            return outfit.underwear_slut_score > 10 and outfit.underwear_slut_score <= max(int(starbuck.sluttiness * .6), 30)
    return True

def starbuck_serum_is_acceptable_lubricant(serum: SerumDesign):   #Make a lubricant trait and assign it to this.
    return False    #Disabled for now
    #return serum.attention <= 3 and serum.has_trait(energy_drink_serum_trait)
