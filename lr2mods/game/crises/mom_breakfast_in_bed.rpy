## Morning crisis
## This file is just a wrapper for the breakfast in bed progression scene to easily add it to the crisis list once unlocked.
init 10 python:
    def mom_breakfast_prog_scene_morning_crisis_req():  #The random morning crisis
        if mom.days_since_event("breakfast_in_bed") >= (max(1, 10 - int((mom.obedience - 100)/10))):
            if mom.progress.obedience_step >= 2:
                return True
            return False
        return False

    mom_breakfast_prog_scene_crisis_action = ActionMod("Breakfast in Bed", mom_breakfast_prog_scene_morning_crisis_req,"mom_breakfast_prog_scene_action_label",
        menu_tooltip = "Mom serves you breakfast in bed.", category="Home", is_crisis = True, is_morning_crisis = True)