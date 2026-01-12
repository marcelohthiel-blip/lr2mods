from __future__ import annotations
from game.major_game_classes.game_logic.Room_ren import mall, ceo_office
from game.clothing_lists_ren import strappy_bra, belted_top, strappy_panties, belted_skirt, garter_with_fishnets, high_heels, lipstick, heavy_eye_shadow, thin_dress, corset, thong, pumps
from game.major_game_classes.character_related.Person_ren import Person, mc, candace, salon_manager
from game.major_game_classes.game_logic.Action_ren import Action
from game.major_game_classes.game_logic.Role_ren import Role
from game.major_game_classes.clothing_related.Outfit_ren import Outfit

TIER_1_TIME_DELAY = 3
TIER_2_TIME_DELAY = 7
TIER_3_TIME_DELAY = 14
day = 0
time_of_day = 0
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -1 python:
"""

def ophelia_takes_over_hair_salon_requirement():
    return mc.business.has_event_day("T1_unlock_day") and day > mc.business.get_event_day("T1_unlock_day") + TIER_2_TIME_DELAY

def salon_introduction_action_requirement(person: Person):
    return person.is_at_work

def add_ophelia_takes_over_hair_salon():
    mc.business.add_mandatory_morning_crisis(
        Action("Ophelia takes over the hair salon", ophelia_takes_over_hair_salon_requirement, "ophelia_takes_over_hair_salon_label")
    )
    salon_manager.add_unique_on_room_enter_event(
        Action("Ophelia's Hair Salon", salon_introduction_action_requirement, "salon_manager_greetings", priority = 30)
    )

def cut_hair_requirement(person: Person):
    if not person.is_at_work:
        return False
    if person.love < 20:
        return "Requires: 20 Love"
    return True

def ophelia_ex_bf_plan_pics_requirement(person: Person):
    # prevent conflict with planned dates
    if ((mc.business.is_weekend and not mc.has_open_time_slot(3, day_restriction = (0,)))
            or not mc.has_open_time_slot(3, day_restriction = (day % 7,))):
        return False
    if person.is_at_work and ophelia_get_ex_pics_planned() < 2 and ophelia_get_phone_convo_heard() > 0:
        return True
    return False

def ophelia_talk_about_candace_requirement(person: Person):
    if ophelia_is_over_her_ex_day() > TIER_2_TIME_DELAY and ophelia_get_can_talk_about_candace():
        return not ophelia_get_will_help_candace()
    return False

def get_salon_manager_role_actions():
    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label", menu_tooltip = "Customize hair style and colour")
    ophelia_ex_bf_plan_pics = Action("Ask about Ex", ophelia_ex_bf_plan_pics_requirement, "ophelia_ex_bf_plan_pics_label", menu_tooltip = "See if you can help")
    ophelia_talk_about_candace = Action("Talk about [candace.fname]", ophelia_talk_about_candace_requirement, "ophelia_talk_about_candace_label", menu_tooltip = "Tread carefully, this will be a sore subject")

    return [cut_hair_action, ophelia_ex_bf_plan_pics, ophelia_talk_about_candace]

def create_ophelia_date_night_outfit(person: Person):
    outfit = Outfit("Sexy Plum Shirt And Khaki Skirt")
    outfit.add_upper(strappy_bra.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_upper(belted_top.get_copy(), [.41, .16, .38, 0.95])
    outfit.add_lower(strappy_panties.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_lower(belted_skirt.get_copy(), [.77, .7, .56, 0.95], "Pattern_1", [.41, .16, .38, 0.95])
    outfit.add_feet(garter_with_fishnets.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_feet(high_heels.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_accessory(lipstick.get_copy(), [.41, .16, .38, 0.4])
    outfit.add_accessory(heavy_eye_shadow.get_copy(), [.41, .16, .38, 0.5])
    person.apply_outfit(outfit)
    person.wardrobe.add_outfit(outfit)

def create_candace_date_night_outfit(person: Person):
    outfit = Outfit("Candi Sexy Date Night")
    outfit.add_upper(thin_dress.get_copy(), [1.0, 0.73, 0.85, 0.95])
    outfit.add_upper(corset.get_copy(), [1.0, 0.73, 0.85, 0.95])
    outfit.add_lower(thong.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_feet(garter_with_fishnets.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_feet(pumps.get_copy(), [.15, .15, .15, 0.95])
    outfit.add_accessory(lipstick.get_copy(), [.45, .31, .59, 0.4])
    outfit.add_accessory(heavy_eye_shadow.get_copy(), [.45, .31, .59, .5])
    person.apply_outfit(outfit)

def ophelia_gets_dumped_requirement(person: Person):
    return person.days_since_event("day_met") > TIER_2_TIME_DELAY and person.is_at_work

def add_ophelia_gets_dumped_action():
    salon_manager.set_event_day("day_met")
    salon_manager.add_unique_on_room_enter_event(
        Action("Ophelia gets dumped", ophelia_gets_dumped_requirement, "ophelia_gets_dumped_label", priority = 30,
               menu_tooltip = "Ophelia is back on the market")
    )

def ophelia_coworker_conversation_overhear_requirement(person: Person):
    return person.days_since_event("dump_day") > TIER_2_TIME_DELAY and person.is_at_work

def add_ophelia_coworker_conversation_overhear_action():
    salon_manager.change_happiness(-50)
    salon_manager.set_event_day("dump_day")
    salon_manager.add_unique_on_room_enter_event(
        Action("Ophelia talks with a coworker", ophelia_coworker_conversation_overhear_requirement, "ophelia_coworker_conversation_overhear_label", priority = 30,
               menu_tooltip = "Ophelia vents to a coworker")
    )

def ophelia_learn_chocolate_love_requirement():
    return salon_manager.known_opinion("dark chocolate") == 2

def ophelia_ex_bf_phone_overhear_requirement(person: Person):
    return person.sluttiness >= 20 and person.days_since_event("dump_day") > TIER_3_TIME_DELAY and person.is_at_work

def add_ophelia_learn_chocolate_love_action():
    salon_manager.event_triggers_dict["coworker_overhear"] = 1
    mc.business.add_mandatory_crisis(
        Action("Learn Ophelia loves chocolate", ophelia_learn_chocolate_love_requirement, "ophelia_learn_chocolate_love_label")
    )
    salon_manager.add_unique_on_room_enter_event(
        Action("Overhear a phone conversation", ophelia_ex_bf_phone_overhear_requirement, "ophelia_ex_bf_phone_overhear_label", priority = 30)
    )

def ophelia_give_chocolate_requirement():
    if not ophelia_get_chocolate_gift_unlock():
        return False

    if time_of_day < 1:
        return "Wait for shops to open"
    if time_of_day > 3 or day % 7 == 6:
        return "Shops are closed"
    if not mc.business.has_funds(50):
        return "Not enough money"
    if ophelia_get_day_of_last_gift() == day:
        return "Already gifted today"
    return True

def add_ophelia_give_chocolate_action():
    salon_manager.event_triggers_dict["chocolate_gift_unlocked"] = 1
    mall.add_action(
        Action("Buy Ophelia Dark Chocolates", ophelia_give_chocolate_requirement, "ophelia_give_chocolate_label",
               menu_tooltip = "Buy Ophelia some chocolates. Can use to apply serum")
    )

# TODO: Remove this for release (save compatibility)
def ophelia_make_blowjob_pics_requirement():
    return time_of_day == 3 and salon_manager.is_at_work

def add_ophelia_make_blowjob_pics_action():
    salon_manager.event_triggers_dict["pics_to_ex_plan_made"] = 2
    day_slot = 0 if mc.business.is_weekend else day % 7
    mc.create_date("ophelia_make_blowjob_pics_label", f"Meet {salon_manager.fname} at the salon", time_slot=(day_slot, 3), person = salon_manager)

def ophelia_blowjob_pics_review_requirement(person: Person):
    return time_of_day < 4 and person.is_at_work

def add_ophelia_blowjob_pics_review_action():
    salon_manager.event_triggers_dict["pics_to_ex_plan_made"] = 3
    salon_manager.event_triggers_dict["pics_to_ex_sent"] = 1
    salon_manager.add_unique_on_room_enter_event(
        Action("Review blowjob pictures", ophelia_blowjob_pics_review_requirement, "ophelia_blowjob_pics_review_label", priority = 30)
    )

def ophelia_revenge_date_plan_requirement(person: Person):
    return person.sluttiness >= 40 and \
        person.days_since_event("pic_review_day") > TIER_1_TIME_DELAY and \
        person.is_at_work

def add_ophelia_revenge_date_plan_action():
    salon_manager.event_triggers_dict["pics_to_ex_sent"] = 2
    salon_manager.event_triggers_dict["special_bj_unlock"] = 1
    salon_manager.set_event_day("pic_review_day")
    salon_manager.add_unique_on_room_enter_event(
        Action("Ophelia asks you on a date", ophelia_revenge_date_plan_requirement, "ophelia_revenge_date_plan_label", priority = 30)
    )

def ophelia_revenge_date_requirement():
    return time_of_day == 3 and day % 7 == 6

def add_ophelia_revenge_date_action():
    salon_manager.event_triggers_dict["first_date_planned"] = 1
    mc.business.add_mandatory_crisis(
        Action("Date with Ophelia", ophelia_revenge_date_requirement, "ophelia_revenge_date_label")
    )

def ophelia_is_over_her_ex_requirement(person: Person):
    return candace.days_since_event("day_met") > TIER_2_TIME_DELAY and person.is_at_work

def ophelia_revenge_aftermath_requirement(person: Person):
    return day % 7 != 6 and person.is_at_work

def add_ophelia_revenge_aftermath_action():
    salon_manager.add_unique_on_room_enter_event(
        Action("Ophelia finally moves on", ophelia_is_over_her_ex_requirement, "ophelia_is_over_her_ex_label", priority = 30)
    )
    salon_manager.add_unique_on_talk_event(
        Action("Talk about what happened", ophelia_revenge_aftermath_requirement, "ophelia_revenge_aftermath_label", priority = 30)
    )


def ophelia_increased_service_begin_requirement(person: Person):
    return ophelia_is_over_her_ex_day() > TIER_1_TIME_DELAY and person.sluttiness_tier >= 3 and person.is_at_work

def add_ophelia_increased_service_begin_action():
    salon_style_cost = 30
    salon_dye_cost = 15
    global salon_total_cost
    salon_total_cost = salon_style_cost + salon_dye_cost

    salon_manager.set_event_day("over_her_ex")
    salon_manager.add_unique_on_talk_event(
        Action("Ophelia increases services", ophelia_increased_service_begin_requirement, "ophelia_increased_service_begin_label", priority = 30)
    )

def ophelia_choose_service_test_requirement():
    if mc.business.is_open_for_business:
        if ophelia_get_pubic_style_state() == 1:
            return True
        return "Only during business hours"
    return False

def add_ophelia_choose_service_test_action():
    salon_manager.event_triggers_dict["full_style_state"] = 1
    ceo_office.add_action(
        Action("Pick employee for salon visit", ophelia_choose_service_test_requirement, "ophelia_choose_service_test_label",
            menu_tooltip = "Select a girl you want to have her hair and pubic hair cut and styled", priority = 40)
    )

def ophelia_add_service_full_body_massage_requirement(person: Person):
    return False

def add_ophelia_add_service_full_body_massage_action():
    salon_manager.event_triggers_dict["full_style_state"] = 2
    ceo_office.remove_action("ophelia_choose_service_test_label")
    #TODO: Write story and hookup action
    #ophelia_add_service_full_body_massage = Action ("Ophelia wants to do massages", ophelia_add_service_full_body_massage_requirement, "ophelia_add_service_full_body_massage_label")

def ophelia_get_coworker_overheard():
    return salon_manager.event_triggers_dict.get("coworker_overhear", 0)

def ophelia_get_num_chocolates_received():
    return salon_manager.event_triggers_dict.get("chocolates_received", 0)

def ophelia_get_chocolate_gift_unlock():
    return salon_manager.event_triggers_dict.get("chocolate_gift_unlocked", 0)

def ophelia_get_day_of_last_gift():
    return salon_manager.event_triggers_dict.get("day_of_last_chocolate", 0)

def ophelia_get_knows_secret_admirer():
    return salon_manager.event_triggers_dict.get("secret_admirer_known", 0)

def ophelia_get_phone_convo_heard():
    return salon_manager.event_triggers_dict.get("ex_phone_overhear", 0)

def ophelia_get_ex_pics_planned():
    return salon_manager.event_triggers_dict.get("pics_to_ex_plan_made", 0)

def ophelia_get_ex_pics_sent():
    return salon_manager.event_triggers_dict.get("pics_to_ex_sent", 0)

def ophelia_get_first_date_planned():
    return salon_manager.event_triggers_dict.get("first_date_planned", 0)

def ophelia_get_first_date_finished():
    return salon_manager.event_triggers_dict.get("first_date_finished", 0)

def ophelia_get_ex_name():
    return salon_manager.event_triggers_dict.get("ex_name", "Gary")

def ophelia_get_salon_and_spa_planned():
    return salon_manager.event_triggers_dict.get("salon_and_spa_planned", 0)

def ophelia_get_salon_and_spa_finished():
    return salon_manager.event_triggers_dict.get("salon_and_spa_finished", 0)

def ophelia_get_special_bj_unlocked():
    return salon_manager.event_triggers_dict.get("special_bj_unlock", 0)

def ophelia_is_over_her_ex_day():
    return salon_manager.days_since_event("over_her_ex")

def ophelia_get_can_talk_about_candace():
    return salon_manager.event_triggers_dict.get("talk_about_candace", 0)

def ophelia_get_will_help_candace():
    return salon_manager.event_triggers_dict.get("help_candace", 0)

def ophelia_get_pubic_style_state():
    return salon_manager.event_triggers_dict.get("full_style_state", 0)

def ophelia_get_will_change_pubic_hair(): #Testing
    return salon_manager.event_triggers_dict.get("offers_full_style", False)

def ophelia_person_wants_pubic_hair_included(person: Person):  #Check for each individual person if they are willing to have their pubic hair styled.
    if person.sluttiness >= 50 or person.obedience >= 150:
        return ophelia_get_will_change_pubic_hair()
    return False
