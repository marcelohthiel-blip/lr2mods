# Camila's Notes:
# A faithful wife, whose husband, the bartender, has requested she adopt the hotwife lifestyle.
# Camila is also the lifestyle coach at the mall during the day, who helps MC set and prioritize goals.
# In her love story, she is introduced to Alexia as a means of taking lewd photos for company advertisements.
# In Nora's love story, Nora is introduced to Camila to help her come up with life goals as she flounders with meaning and purpose in her job
#
# Camila's current major flaws:
# There isn't a good way to increase her stats. Her only chance of getting serums is at the bar, with no useful time slot after.
# Come up with a new method for either being able to increase her stats during that scene, or give an alternate dosing method.

label camila_intro_label(the_person):
    "You decide to wander aimlessly around the mall for a bit. You do a bit of people watching and generally enjoy the time to yourself."
    "As you walk around, you spot a kiosk that catches your attention."
    "Lifestyle Coaches: We help you set and achieve long term and short term goals!"
    "You walk around the kiosk a bit, there are all kinds of testimonials and adverts up for the service."
    the_person "Hello there! I'm [the_person.title]."   # use title, since fname will return ??? until no longer stranger
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    $ the_person.set_mc_title(mc.name)
    $ the_person.set_event_day("day_met")
    mc.name "I'm [mc.name]."
    $ the_person.primary_job.job_known = True
    the_person "Nice to meet you! I'm a lifestyle coach, here to help people achieve their dreams!"
    "The sales pitch is a little... optimistic? But to be honest, she is pretty good-looking, so you decide to let her continue."
    the_person "I've personally helped all kinds of people achieve all kinds of things, from giving up drugs, to losing a few {weight_system}!"
    the_person "Our first consultation is free. Would you be interested?"
    "What the hell. It couldn't hurt anything, right?"
    mc.name "I suppose."
    "You sit down with [the_person.title]. She asks you some generic questions about your personal and work life."
    "You explain that you are a small business owner, working with pharmaceuticals, leaving out some of the details."
    "You share some of your basic short term, and a few long term goals, both for your business and for yourself, personally."
    the_person "I see. Those sound like interesting goals! Might I offer a few alternatives also?"
    mc.name "Sure."
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    the_person "I hope that was helpful! Come back again and see me if you want to adjust your goals again in the future!"
    mc.name "I think it was. I'll be sure to check back with you again if I need to. Thanks!"
    $ the_person.event_triggers_dict["met"] = 1
    $ scene_manager.clear_scene()
    $ add_camila_spot_at_bar_action()
    return

label camila_spot_at_bar_label(the_person):
    "As you walk into the bar, you take a look around."
    $ the_person.draw_person(position = "sitting")
    "Sitting at the bar by herself, you notice [the_person.title], the lifestyle coach from the mall."
    "You are surprised a woman as pretty as her is sitting by herself at the bar, so you decide to go say hi."
    "She notices you as you walk up to her."
    mc.name "Hello [the_person.title]. Out for a drink this evening?"
    the_person "Hello... [the_person.mc_title] was it?"
    mc.name "Excellent memory. Yes I worked with you some at the mall the other day."
    the_person "Yes, I remember. The small business owner."
    mc.name "I noticed you at the bar by yourself. Mind if I sit with you for a while?"
    the_person "That's fine."
    "You sit down in a bar stool next to [the_person.possessive_title]."
    mc.name "So how long have you been working as a lifestyle coach?"
    the_person "Honestly, not too long. I mainly just do it as an extra source of income to supplement what my hubby brings in."
    "Ah, so she is married. You should probably keep things low-key for now."
    mc.name "That's admirable. How long have you been married?"
    the_person "Almost 15 years now."
    mc.name "Wow, you don't look like someone who has been married 15 years!"
    the_person "Ah, we got married young."
    mc.name "Kids?"
    "[the_person.title] hesitates. You might have hit a sore subject with her..."
    the_person "No, no niños..."
    mc.name "I'm sorry... I'm probably getting a little personal."
    "You make a mental note that she doesn't have any kids."
    the_person "It's okay, that's a perfectly normal question to ask."
    "You feel bad. You notice that her glass is almost empty. You wave down the bartender. When he walks over, he smiles wide at [the_person.title]."
    "???" "Something I can get for you?"
    mc.name "Can I get a beer and another for my friend?"
    "???" "Sure. A beer and another paloma for the lovely Miss [the_person.last_name]."
    "The bartender walks off. He seems to know [the_person.title]. She must be a regular here?"
    mc.name "Ah, you come here often then?"
    the_person "I do. I'm here most evenings. I like to have a drink before I head home each night. My husband works late."
    mc.name "I see. I'm here somewhat often as well. Maybe we could have a drink together once in a while?"
    the_person "I... I suppose that would be alright."
    "You sit back in the chair and chat with [the_person.possessive_title] for a while. You both enjoy the time together, getting to know one another as friends."
    $ the_person.change_love(3)
    $ mc.business.change_funds(-20, stat = "Food and Drinks")
    "Eventually you settle up with the bartender. You notice him gesture at [the_person.title] when she isn't looking, and gives you a little wink."
    "You aren't sure... is he trying to say she's... available? Maybe since her husband works late she picks up guys at the bar..."
    "You file it away in your brain. Maybe you could come back and have drinks with her again. A bar would be an ideal place to dose her with a few serums too..."
    "You get up and say goodbye to [the_person.possessive_title]."
    mc.name "Thank you for the conversation. I'll see you around [the_person.title]."
    the_person "Take care [the_person.mc_title]."
    "You can now have drinks with [the_person.title] at the bar in the evenings."
    $ init_camila_story_line()
    call advance_time() from _call_advance_camila_meet_at_bar_first_time_01
    return
