# SB will ask MC for some help after she developed an anal fetish
init 2 python:
    def SB_fetish_phone_requirement():
        return (time_of_day in (1,2,3)
            and starbuck.has_anal_fetish
            and starbuck.is_available
            and starbuck.has_event_delay("last_phone_message", 7)
            and starbuck not in mc.location.people)

    SB_fetish_phone_crisis = ActionMod("Starbuck Phone Message", SB_fetish_phone_requirement ,"SB_fetish_phone_crisis_label",
        menu_tooltip = "Starbuck has developed an anal fetish and requests your help from time to time.", category = "Fetish", is_crisis = True)

label SB_fetish_phone_crisis_label():
    python:
        current_action = "None"
        if renpy.random.randint(0, 100) <= 25:
            current_action = "masturbate"
        starbuck.set_event_day("last_phone_message")

    if current_action == "masturbate":
        call starbuck_anal_fetish_masturbate() from _call_starbuck_anal_fetish_masturbate_phone_crisis
    elif starbuck.arousal_perc > 60:
        call starbuck_anal_fetish_request() from _call_starbuck_anal_fetish_request_phone_crisis
    else:
        call starbuck_anal_fetish_checkup() from _call_starbuck_anal_fetish_checkup_phone_crisis

    return
