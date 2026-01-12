init 3 python:
    def coffee_shop_get_coffee_requirement(): # Leave this in
        if time_of_day == mc.business.event_triggers_dict.get("coffee_shop_buy_coffee_day", time_of_day):
            return "Already bought coffee"
        if not mc.business.has_funds(5):
            return "Requires: $5"
        return True

    # actions available from entry point action
    coffee_shop_get_coffee_action = Action("Order a coffee", coffee_shop_get_coffee_requirement, "coffee_shop_get_coffee_label", menu_tooltip = "Restore some energy with a hot coffee")

label coffee_shop_get_coffee_label():
    $ mc.business.event_triggers_dict["coffee_shop_buy_coffee_day"] = time_of_day
    if kaya.is_at_job("Barista"):
        call kaya_get_coffee_label(kaya) from _kaya_barista_coffee_time_01

    else:
        "You step up to the coffee shop counter. You order yourself a coffee."
        "You sit down at a table and enjoy the fresh brew. The flavour and caffeine perks you up a bit."
        $ mc.change_energy(30)
        $ mc.business.change_funds(-5, stat = "Food and Drinks")
    return
