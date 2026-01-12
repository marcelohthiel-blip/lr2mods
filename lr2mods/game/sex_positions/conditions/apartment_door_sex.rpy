# This condition tracks MC having sex with girl up against her apartment door.
# If she loves public sex or is an exhibitionist, she is purposefully noisy so her neighbors hear.
# If she is introverted or doesn't like public sex, she tries her best to stay quiet.

init -1 python:
    def condition_apartment_door_sex_reward_req(condition, the_person, report_log):  
        if report_log.get("girl orgasms", 0) >= (3 - the_person.opinion.public_sex):   #orgasms based on public sex opinion
            return True
        return False


    def make_condition_apartment_door_sex():
        apartment_door_sex_whitelist = [against_wall, facing_wall, standing_cunnilingus]      #These are currently the only "lean" positions.
        apartment_door_sex_condition = Condition_Type("apartment_door_sex",
            pre_label = "condition_apartment_door_sex_pre_label",     #How noisy is she being?
            post_label = "condition_apartment_door_sex_post_label",   #Check for orgasms
            position_whitelist = apartment_door_sex_whitelist,        
            reward_cond = condition_apartment_door_sex_reward_req,    #A function to determine if a reward condition has been met.
            reward_label = "condition_apartment_door_sex_reward_label",   #The reward received if the condition is met
            fail_label = "condition_apartment_door_sex_fail_label")       #If the reward condition is failed, shows this.

        apartment_door_sex_condition.condition_vars.append(0)   #Female orgasms
        apartment_door_sex_condition.condition_vars.append(0)   #Override with required orgasms for reward in the pre label.
        return apartment_door_sex_condition


label condition_apartment_door_sex_pre_label(the_person, the_position, the_object, report_log, the_condition):
    $ the_condition.condition_vars[1] = (3 - the_person.opinion.public_sex)     #Orgasms until she gives up being quiet
    $ rand_choice = renpy.random.randint(0,2)
    if rand_choice < 2: #To avoid excessive messages, only run on average 33% of the time
        return
    #First, determine if she is even trying to be quiet or not.
    #Then, determine is she is actually quiet or if she she's given up and is moaning loudly, disturbing neighbors
    if the_person.opinion.public_sex < 0:   #Yes, she wants to be quiet
        if the_condition.condition_vars[0] >= the_condition.condition_vars[1]:  #She's given up
            $ play_moan_sound()
            "[the_person.title] has given up trying to be quiet, her orgasm addled brain making her moan loudly, reverberating down the hall and presumably outside her front door."
        elif the_condition.condition_vars[1] > 0:
            "[the_person.title] is making soft moans. She grimaces, trying desperately to stay quiet to avoid disturbing her neighbors."
        else:
            "[the_person.title] keeps her moans and voice quiet, trying to keep herself from alerting her neighbors."

    if the_person.opinion.public_sex < 2:   #She only somewhat cares about staying quiet.
        if the_condition.condition_vars[0] >= the_condition.condition_vars[1]:  #She's given up
            $ play_moan_sound()
            "[the_person.title] has given up the pretense of staying quiet, moaning loudly for any neighbors to hear her."
        elif the_condition.condition_vars[1] > 0:
            "[the_person.title] is making soft moans, trying to stay quiet to avoid disturbing her neighbors."
        else:
            "[the_person.title] keeps her moans and voice quiet, trying to keep herself from alerting her neighbors."
    
    else:
        $ play_moan_sound()
        if the_condition.condition_vars[0] >= the_condition.condition_vars[1]:
            "[the_person.title] is moaning and talking dirty to you loudly. The idea that a neighbor could overhear you seems to turn her on even more."
            $ the_person.change_arousal(3)
        else:
            "[the_person.title] moans, seemingly excited at the prospect of her neighbors overhearing you."
    return

label condition_apartment_door_sex_post_label(the_person, the_position, the_object, report_log, the_condition):
    if report_log.get("girl orgasms", 0) > the_condition.condition_vars[0]:
        if report_log.get("girl orgasms", 0) == the_condition.condition_vars[1]:    #Her orgasm pushed her into being noisy
            if the_person.opinion.public_sex < 2:
                "With her orgasm, [the_person.title] has given up trying to be quiet."
                "Her moans and cries of pleasure echo through the apartment entryway and out into the hall where any neighbors walking by could hear."
            else:
                "[the_person.title] moans loudly, not even trying to stifle her cries of pleasure."
                "Her noises echo down the hall and through the apartment hall for any neighbors to hear, and she seems to love it."
        elif report_log.get("girl orgasms", 0) > the_condition.condition_vars[1]:
            "With another orgasm, [the_person.title]'s moans and cries seem to somehow grow even louder than before."
        else:
            "After her orgasm, [the_person.title] tries to stifle further noises, trying to keep from alerting her neighbors."
    $ the_condition.condition_vars[0] = report_log.get("girl orgasms", 0)
    return

label condition_apartment_door_sex_reward_label(the_person, report_log, the_condition):
    if the_person.opinion.public_sex < 0:
        "As she begins to recover, [the_person.possessive_title] suddenly realizes what just happened. She seems a bit panicked."
        the_person "Ha... you don't think anyone heard us... do you?"
        "You are pretty sure anyone who happened to walk by her door, as well as both her adjacent neighbors probably heard what just happened, but try to reassure her."
        mc.name "Ummm, no, I'm sure no one heard."
        the_person "Yeah... you're right..."
        $ the_person.change_slut(2, 80)
        $ the_person.change_obedience(2, 180)
    elif the_person.opinion.public_sex < 2:
        "As she begins to recover, [the_person.possessive_title] smiles at you."
        the_person "Wow, that was hot... do you umm... think my neighbors heard us?"
        mc.name "You were moaning pretty loud. I mean, not for certain, but that definitely seems like a possibility..."
        the_person "Yeah... I'll probably catch hell for it tomorrow, but that was so hot, I don't think I care!"
        $ the_person.change_slut(2, 80)
        $ the_person.change_obedience(2, 180)
    else:
        "As she begins to recover, [the_person.possessive_title] smiles at you."
        the_person "Holy shit that was amazing. Do you think all my neighbors heard us fucking?"
        "She seems more excited than scared at the idea."
        mc.name "You were moaning before I even stuck it in. I'm pretty sure if your neighbors are home they know what just happened."
        the_person "Mmm, yeah I bet they do!"
        $ the_person.change_slut(2, 80)
        $ the_person.change_obedience(2, 180)
    return

label condition_apartment_door_sex_fail_label(the_person, report_log, the_condition):
    if the_person.opinion.public_sex < 0:
        "As she begins to recover, [the_person.possessive_title] seems a bit relieved."
        the_person "That was good... I don't think anyone overheard us!"
    else:
        "As she begins to recover, [the_person.possessive_title] doesn't say much. She stayed quiet enough, you don't think anyone would have overheard you."
    return
