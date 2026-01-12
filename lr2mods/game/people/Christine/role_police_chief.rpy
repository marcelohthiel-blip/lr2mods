
label mc_arrested_penalties():
    if mc_times_arrested() == 0:
        $ mc.business.change_funds(-100, stat = "City Fines")
        "Since this is your first offence, you get off with a light fine."
        $ police_chief.event_triggers_dict["times_arrested"] = 0
    elif mc_times_arrested() == 1:
        $ mc.business.change_funds(-500, stat = "City Fines")
        "Since this is your second offence, you get fined."
        police_chief "Seriously, don't do that again. You can't be doing that stuff in public!"
    elif mc_times_arrested() == 2:
        $ mc.business.change_funds(-5000, stat = "City Fines")
        "Since this is your third offence, you receive a heavy fine."
        police_chief "I guess you still haven't learned your lesson. I'm fining you the maximum amount under the law."
        police_chief "If this happens again, I'll have to let the city know you got problems with authority. Catch my drift?"
    elif mc_times_arrested() == 3:
        $ mc.business.change_funds(-5000, stat = "City Fines")
        "You once again receive a heavy fine."
        police_chief "Damn, you just can't keep your hands to yourself, can you?"
        police_chief "Guess I'll have to call this in to the city. Where did you say you work again?"
        $ mc.business.attention += 20
    elif mc_times_arrested() == 3:
        $ mc.business.change_funds(-5000, stat = "City Fines")
        "You once again receive a heavy fine."
        police_chief "Still screwing around with whores in public are you?"
        police_chief "Guess last time I didn't word my request with the city strongly enough."
        $ mc.business.attention += 50
    else:
        $ mc.business.change_funds(-5000, stat = "City Fines")
        "You once again receive a heavy fine."
        police_chief "Again. You're here AGAIN."
        police_chief "Enough is enough. Get out of here, I'm sure the city will be checking out your business now soon enough."
        $ mc.business.attention += 100
    $ police_chief.event_triggers_dict["times_arrested"] += 1
    return
