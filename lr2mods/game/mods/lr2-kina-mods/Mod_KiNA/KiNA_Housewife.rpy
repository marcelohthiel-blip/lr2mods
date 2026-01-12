# Counter KHW01

# This allow Mom to leave work early if she works for you, allowing evening kitchen event like before
# Code highly adapted from Kaden's study buddy

init python:
    def housewife_mod_initialization():
        global kitchen_role
        kitchen_role = Role("Housewife", actions = [], hidden = False) #in actions you could anything you want to be able to do with the chef
        global kitchen_job
        kitchen_job = JobDefinition("Housewife", kitchen_role, job_location = kitchen, day_slots = [0,1,2,3,4], time_slots = [3], wardrobe = mom_home_wardrobe) #you could create a specific uniform that is distinct from what she wears in her room
        global mom_housewife_action
        mom_housewife_action = Action("Give Mom special work privilege", mom_special_privilege_requirement, "mom_housewife_label", menu_tooltip = "Let Mom leave early from office")
        if mom_our_secretary():
            mom.get_role_reference("Personal Secretary").add_action(mom_housewife_action)
        #mom.set_side_job(kitchen_job)

    def mom_special_privilege_requirement(person: Person):
        return (mom_our_secretary())

init 16 python: # hijack
    add_label_hijack("normal_start", "activate_housewife_mod_core")
    add_label_hijack("after_load", "update_housewife_mod_core")

label activate_housewife_mod_core(stack):
    python:
        housewife_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_housewife_mod_core(stack):
    python:
        if "kitchen_job" not in globals():
            housewife_mod_initialization()
        execute_hijack_call(stack)
    return

label mom_housewife_label(the_person):
    if the_person.has_job(kitchen_job):
        mc.name "[the_person.title], I'm sorry to tell you this, but you need to do overtime for a while."
        "She gazed into your eyes with affection."
        if the_person.known_opinion.working > 0:
            the_person "Why would you be sorry, [the_person.mc_title]. I'm part of your team, and I'll gladly help out if the company needs me."
            the_person "Besides, our company, remember?"
        else:
            the_person "If it'll help, [the_person.mc_title]. I'll do everything for our company."
        $ the_person.quit_job(kitchen_job)
    else:
        mc.name "[the_person.title], I'd like you to cancel all my evening commitments that involve you, effective immediately and until further notice."
        $ the_person.draw_person(position = "stand2", emotion = "sad")
        "[the_person.possessive_title!c] visibly shaken."
        the_person "Did I do something wrong? Tell me so I can fix it."
        "You quickly hug to assure her."
        mc.name "No, no, no. I'm sorry, you did nothing wrong. I just wanted to let you leave office early. I want you to be able to rest at home, [the_person.title]."
        mc.name "You know that I love you. In fact, if you tell me that you wanted to quit and just be a stay at home wife, I would gladly let you."
        "She lifted her head and gazed into your eyes with affection."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        if the_person.known_opinion.working > 0:
            the_person "I enjoy working, Sweetheart. And helping you in your own company is the least I could do."
            mc.name "Our company."
            the_person "Our company than, even though I don't really understand what we actually making here."
            the_person "Are you sure you want me to leave early? Won't others talk and get jealous?"
        else:
            the_person "I just want to help you, Darling. And we could stay close while working."
            "She gave a sultry smile. You gave her ass a tight squeeze which earns you a sexy moan."
            mc.name "And that's why I was eager to bring you on board from the beginning."
            mc.name "Still, I'm aware that for you, work is more of an obligation than a source of joy."
            mc.name "Rather than pushing you to your breaking point, I've decided it's best to allow you to leave work early."
            the_person "I would love that, but are you sure you want me to leave early? Won't others talk and get jealous?"
            mc.name "Perk of being the boss."
        mc.name "I'll inform them that you'll be working remotely."
        $ the_person.draw_person(position = "stand2")
        the_person "Very well. I'll be able to cook dinner again for us then."
        the_person "Thanks, [the_person.mc_title]."
        $ the_person.set_side_job(kitchen_job)
    return