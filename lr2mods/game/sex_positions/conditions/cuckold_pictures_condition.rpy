#Use this for recording a onlyfans session.

init -1 python:
    def condition_cuckold_pictures_reward_req(self, the_person, report_log):
        if report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) > 0:   #Both partners finish
            return True
        return False


    def make_condition_cuckold_pictures():
        cuckold_pictures_blacklist = [anal_swing, missionary, breeding_missionary, doggy_anal_dildo_dp, piledriver_anal, piledriver_dp, spanking, standing_dildo, against_wall, kissing, piledriver, standing_grope]  #We should blacklist any position that would require both of MC's hands
        cuckold_pictures_condition = Condition_Type("Cuckold Pictures",
            pre_label = "condition_cuckold_pictures_pre_label",
            post_label = "condition_cuckold_pictures_post_label",
            position_blacklist = cuckold_pictures_blacklist,
            reward_cond = condition_cuckold_pictures_reward_req,
            reward_label = "condition_cuckold_pictures_reward_label")
        cuckold_pictures_condition.condition_vars.append(False) #Initialize this to false so in the first pre label we can mention getting the phone camera ready
        cuckold_pictures_condition.condition_vars.append(0)     #Female orgasms
        cuckold_pictures_condition.condition_vars.append(0)     #Male orgasms
        return cuckold_pictures_condition


label condition_cuckold_pictures_pre_label(the_person, the_position, the_object, report_log, the_condition):
    "You check the phone, trying to make sure you are keeping the action in view while you [the_position.verb] [the_person.title]."
    return

label condition_cuckold_pictures_post_label(the_person, the_position, the_object, report_log, the_condition):
    if report_log.get("girl orgasms", 0) > the_condition.condition_vars[1] and report_log.get("guy orgasms", 0) > the_condition.condition_vars[2]:  #you finished together
        "You swap to video mode for the finale, but you aren't sure if you managed to keep it in focus"
        "You're sure the sounds of [the_person.title] cumming with you were hot enough for her cuckold husband though."
        "You stop [the_position.verbing] her for a moment to make sure you capture the aftermath of your orgasms."
    elif report_log.get("girl orgasms", 0) > the_condition.condition_vars[1]: #she orgasmed
        "You make sure you are in video mode as you are [the_position.verbing] her through her orgasm."
    elif report_log.get("guy orgasms", 0) > the_condition.condition_vars[2]:
        "You stop [the_position.verbing] her for a moment to make sure you capture the aftermath of your orgasm."
    else:
        "You record some short videos and snap some pictures as you are [the_position.verbing] her."
    $ the_condition.condition_vars[1] = report_log.get("girl orgasms", 0)
    $ the_condition.condition_vars[2] = report_log.get("guy orgasms", 0)
    return

label condition_cuckold_pictures_reward_label(the_person, report_log, the_condition):
    $ the_person.change_stats(slut = 2, max_slut = 80, obedience = 3)
    "[the_person.possessive_title!c] really enjoyed your session. She takes her phone back and starts looking through the pictures."
    return
