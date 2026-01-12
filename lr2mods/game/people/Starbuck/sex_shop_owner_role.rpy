#This role is a replacement for Starbuck's Sex Shop Owner inherited class file.
#All functions associated with running the sex shop can now be done via Roles, so lets simplify the code and do it that way.

label sex_shop_invest_basic_label(the_person):
    mc.name "I'd like to invest more in your shop, [the_person.title]."
    the_person "Oh?"
    mc.name "I'd like for you to expand more of your basic inventory."
    the_person "Those do tend to be high margin, profitable items. I supposed I could look around and see if I can expand my inventory some."
    mc.name "Sounds great. Here's a check for $1000."
    $ the_person.change_stats(obedience = 2, love = 1, max_love = 30)
    $ mc.business.change_funds(-1000, stat = "Investments")
    $ the_person.event_triggers_dict["shop_investment_basic_total"] += 1000
    $ the_person.event_triggers_dict["shop_investment_total"] += 1000
    the_person "Wow! I really appreciate this. Is there anything else you need [the_person.mc_title]?"
    the_person "Maybe you could swing by sometime in the evening and help me put up stock?"
    return

label sex_shop_invest_advanced_label(the_person):
    mc.name "I'd like to invest more in your shop, [the_person.title]."
    the_person "Oh?"
    mc.name "I'd like for you to expand more of your advanced inventory."
    the_person "Yeah, having intricate toys and the like can be great for driving foot traffic, even if they don't sell very fast."
    mc.name "Sounds great. Here's a check for $5000."
    $ the_person.change_stats(obedience = 3, love = 2, max_love = 50)
    $ mc.business.change_funds(-5000, stat = "Investments")
    $ the_person.event_triggers_dict["shop_investment_advanced_total"] += 5000
    $ the_person.event_triggers_dict["shop_investment_total"] += 5000
    the_person "Wow! I can't believe you are investing even more! This is really incredible. Is there anything else you need while you're here, [the_person.mc_title]?"
    return

label sex_shop_invest_fetish_label(the_person):
    mc.name "I'd like to invest more in your shop, [the_person.title]."
    the_person "Oh? You've already done so much."
    mc.name "I'd like for you to expand more of your fetish inventory."
    the_person "Fetish inventory moves slowly, but it definitely drives interest and foot traffic."
    mc.name "Sounds great. Here's a check for $15000."
    $ the_person.change_stats(obedience = 5, love = 3, max_love = 70)
    $ mc.business.change_funds(-15000, stat = "Investments")
    $ the_person.event_triggers_dict["shop_investment_fetish_total"] += 15000
    $ the_person.event_triggers_dict["shop_investment_total"] += 15000
    the_person "Holy fuck! You're amazing [the_person.mc_title]! Anything else you need while you are here?"
    return

label sex_shop_cashier_wardrobe_label(the_person):
    mc.name "I'd like to talk to you about your uniforms."
    the_person "Oh?"
    call outfit_master_manager(wardrobe = sex_shop_wardrobe.wardrobe, show_overwear = False, show_underwear = False, start_mannequin = the_person, outfit_validator = sex_shop_owner_outfit_check) from _call_outfit_master_manager_sex_shop_cashier_wardrobe
    return
