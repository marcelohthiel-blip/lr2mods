# Use this for banging your secretary
# Assume MC is sitting in his chair OR banging her on his office desk.

init -1 python:
    def condition_secretary_sex_reward_req(condition, the_person, report_log): 
        if report_log.get("guy orgasms", 0) > 0:   #Guy Orgasmed
            return True
        return False


    def make_condition_secretary_sex():
        secretary_sex_whitelist = [anal_standing, standing_doggy, spanking]      #Note: Use whitelist OR blacklist, not both!
        secretary_sex_condition = Condition_Type("Personal Secretary Sex",
            pre_label = "condition_secretary_sex_pre_label", #This label triggers before each sex round
            reward_cond = condition_secretary_sex_reward_req,    #A function to determine if a reward condition has been met.
            reward_label = "condition_secretary_sex_reward_label",   #The reward received if the condition is met
            fail_label = "condition_secretary_sex_fail_label")       #If the reward condition is failed, shows this.
        secretary_sex_condition.condition_vars.append("chair")

        return secretary_sex_condition


label condition_secretary_sex_pre_label(the_person, the_position, the_object, report_log, the_condition):
    $ the_condition.condition_vars[0] = the_object.name
    $ rand_choice = renpy.random.randint(0,5) #Randomize dialogue for a little more variation. Don't ALWAYS return dialogue to keep from getting repetitive.
    
    if the_condition.condition_vars[0] == "chair":
        if rand_choice == 0:
            "[the_person.title] is bouncing on your lap so eagerly, for a moment your chair starts to tip. She stop suddenly until the chair settles, then resumes."
        elif rand_choice == 1:
            "You reach up for a moment and grab your secretary's tits as she bounces up and down on your cock."
        elif rand_choice == 2:
            "Your office chair is squeaking with every eager bounce as your secretary rides you."
    elif the_condition.condition_vars[0] == "desk":
        if rand_choice == 0:
            "Your desk shakes with each thrust inside of [the_person.title]. You hear something fall off the desk, but you don't really care what it was."
        elif rand_choice == 1:
            "You give your secretary's ass looks amazing bent over the side of your desk, so you give it a playful spank."
        elif rand_choice == 2:
            "Your secretary's ass bounces pleasingly with every thrust. You love bending her submissively over your desk once in a while."
    return

label condition_secretary_sex_reward_label(the_person, report_log, the_condition):
    if the_condition.condition_vars[0] == "chair":
        "Your secretary gives you a big smile. She seems really happy she was able to help you out with your sexual tension."
    elif the_condition.condition_vars[0] == "desk":
        "Your secretary looks back at you with a big smile. She seems really happy she was able to help you with your sexual tension."
    $ the_person.change_stats(happiness = 5, obedience = 1, max_obedience = 160)
    return

label condition_secretary_sex_fail_label(the_person, report_log, the_condition):
    if the_condition.condition_vars[0] == "chair":
        "Your secretary seems disappointed she wasn't able to finish you off."
    elif the_condition.condition_vars[0] == "desk":
        "Your secretary frowns, disappointed that you weren't able to finish while fucking her."
    $ the_person.change_stats(happiness = -3, obedience = 1, max_obedience = 160)
    return
