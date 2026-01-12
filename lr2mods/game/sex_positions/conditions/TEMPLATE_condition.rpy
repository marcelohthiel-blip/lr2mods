# This template to be used for copy pasting future conditions

init -1 python:
    def condition_TEMPLATE_reward_req(condition, the_person, report_log):   #If the condition has a goal, what is that goal?
        if report_log.get("girl orgasms", 0) > 0:   #She orgasmed
            return True
        return False


    def make_condition_TEMPLATE():
        TEMPLATE_whitelist = [anal_standing, standing_doggy, spanking]      #Note: Use whitelist OR blacklist, not both!
        TEMPLATE_condition = Condition_Type("TEMPLATE",
            pre_label = "condition_TEMPLATE_pre_label", #This label triggers before each sex round
            post_label = "condition_TEMPLATE_post_label",   #This label triggers after each sex round
            position_whitelist = TEMPLATE_whitelist,        #List of positions this condition can be used with.
            position_blacklist = None,                      #List of positions this condition CANNOT be used with
            reward_cond = condition_TEMPLATE_reward_req,    #A function to determine if a reward condition has been met.
            reward_label = "condition_TEMPLATE_reward_label",   #The reward received if the condition is met
            fail_label = "condition_TEMPLATE_fail_label")       #If the reward condition is failed, shows this.

        TEMPLATE_condition.condition_vars.append(1)   #Conditions vars can be used for any custom variables we want to track inside the condition itself.
        return TEMPLATE_condition


label condition_TEMPLATE_pre_label(the_person, the_position, the_object, report_log, the_condition):
    "Before sex round dialogue"
    return

label condition_TEMPLATE_post_label(the_person, the_position, the_object, report_log, the_condition):
    "After sex round dialogue"
    return

label condition_TEMPLATE_reward_label(the_person, report_log, the_condition):
    "Use this label to give MC a reward for meeting the condition. Triggers after sex."
    return

label condition_TEMPLATE_fail_label(the_person, report_log, the_condition):
    "Use this label if you want a failure condition. Triggers after sex."
    return
