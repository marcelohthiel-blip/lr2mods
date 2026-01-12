#Production assistant helps MC create serum batches for personal consumption.
#Serum modifiers are unlocked after specific serum traits are researched and master to a specific mastery level to minimize the odds of side effects.
#This role starts initially being filled by Ashley, but if it becomes vacant via the storyline or other means, it can be filled by another girl.

label production_assistant_alt_intro_label():   #Use this to create the production assistant if we refused to hire Ashley or fired her before getting serums
    #Condition: Must have head researcher.
    $ the_person = mc.business.head_researcher
    if not mc.is_at(mc.business.r_div):
        "Your phone buzzes, alerting you to a work email."
        the_person "Could you please come down? I have a proposal for you."
        "You finish up what you were working on and head over to meet [the_person.title]."
        $ mc.change_location(mc.business.r_div)
        $ the_person.draw_person()
        mc.name "Hello [the_person.title], what's on your mind?"

    else:
        $ mc.business.r_div.show_background()
        the_person "Excuse me, [the_person.mc_title]?"
        $ the_person.draw_person()
        the_person "I have something I've been thinking about."
        mc.name "Sure, what's on your mind?"
    the_person "We have made some excellent strides in serum development here lately, getting side effects for several of them almost completely removed."
    the_person "I know that most of what we make here has... novel... use cases."
    the_person "Going over some of the files though, I think you should consider making another set of serums, for your personal use."
    mc.name "For me? I'm not sure..."
    the_person "I'm not talking about our suggestibility serums of course, but looking through the files, it wouldn't be that much of a stretch to modify something like the caffeine infusion trait."
    the_person "It would be a bit of work to adapt it to your male biome, but I believe it would be fairly easy to accomplish."
    the_person "Something like that would give you more energy for your work around the office, or other pursuits..."
    "She makes a valid point. You HAVE been developing many serums with broadly beneficial effects."
    the_person "I could help develop the methods, but you would want someone in production to oversee the actual synthesis."
    mc.name "Like a person production assistant?"
    the_person "Yeah... something like that..."
    mc.name "Yeah... that could work. Thank you [the_person.title], I'll consider it."
    the_person "Of course [the_person.mc_title]. I'm going to get back to work."
    $ clear_scene()
    "She turns and leaves you alone. Having serums for your own personal use could be very beneficial."
    "You'll have to setup an official policy for it, then promote someone from production to oversee it."
    "A new policy has been unlocked. Once you active, you can hire a production assistant from the CEO Office."
    $ mc.business.event_triggers_dict["production_assistant_policy_avail"] = True
    return

label production_assistant_general_hire_label():
    $ the_person = mc.business.prod_assistant
    "You call [the_person.title] to your office. After a minute, she appears in the door."
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "Yes. Sit down."
    $ the_person.draw_person(position = "sitting")
    if mc.business.event_triggers_dict.get("mc_serum_energy_unlocked", False) == True: #We've already unlocked some MC serums, so just bring her up to speed.
        mc.name "I have a special assignment that I want you to take over."
        the_person "Oh?"
        mc.name "You will continue your work in production, but you will also oversee special serum synthesis for my personal use."
        the_person "Oh wow!"
        mc.name "I've unlocked the details at your work station. New synthesis formulas may continue as research continues."
        mc.name "If you have any ideas yourself, you are also welcome to run them by me."
        mc.name "Most of the research will be coming from [mc.business.head_researcher.fname] in R and D."
        the_person "Sounds great! I'll look over the details. Thank you for the opportunity sir!"
        $ the_person.change_obedience(10)
        mc.name "There is a pay bump associated with the position as well."
        mc.name "For now, just look over the new formulas, I'll swing by production and let you know what to start synthesizing when I'm ready."
        # Use serum category unlocks to determine where to pickup the quest line
        if mc.business.event_triggers_dict["mc_serum_physical_unlocked"] == True:   #We've unlocked everything, this is just a face change
            mc.name "There is a ton of information, so take your time with it."
        elif mc.business.event_triggers_dict["mc_serum_cum_unlocked"] == True:
            $ add_prod_assistant_unlock_physical_action()
        elif mc.business.event_triggers_dict["mc_serum_aura_unlocked"] == True:
            $ add_prod_assistant_unlock_cum_action()
        else:
            $ add_prod_assistant_essential_oils_intro_action()
    else:
        $ mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = True
        mc.name "I have a new special assignment that I want you to lead. You'll be working with the head researcher directly."
        mc.name "She has some ideas for creation of new serums that I can have for personal use."
        mc.name "I'd like for you to work with her to carryout the actual synthesis, and to work with her to come up with new designs."
        the_person "Oh! Wow that sounds like a big assignment!"
        mc.name "It is. Obviously, as your employer, it will be important that you take this duty seriously and carry it out to the best of your abilities."
        $ the_person.change_obedience(10)
        the_person "Of course."
        mc.name "I've setup your work station to have access to the initial research. Spend some time when you have the chance looking over it."
        mc.name "I know this is an additional duty, so I've also arranged a bump in pay to compensate you for your additional duties."
        the_person "Thank you sir, I'll look over it tonight!"
        mc.name "Good. I'll swing by production and talk to you personally when I'm ready for you to begin the actual synthesis."
        $ add_prod_assistant_essential_oils_intro_action()
        $ add_prod_assistant_performance_upgrade_action()   #We know that these are the next steps.

    call initial_set_duties_label(the_person) from _call_initial_set_duties_production_assistant_hire

    the_person "Yes sir! Will that be all?"
    mc.name "For now, yeah."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] is now your production assistant. Talk to her to have her begin synthesizing serums for your personal use."
    return

label mc_serum_review_label(the_person):
    mc.name "I want to discuss my personal serums."
    the_person "Okay, let me see if I have any updated serum formulas."
    call mc_serum_review_upgrades_label(the_person) from _serum_review_upgrades_01
    the_person "We also can only give you so many serums at a time safely."
    call mc_serum_review_quantity_label(the_person) from _serum_review_quantity_01
    the_person "Alright, here are the serums that I have available."
    call screen mc_personal_serum_screen()
    mc.name "Thank you [the_person.title]. Keep up the good work."
    return

label mc_serum_review_upgrades_label(the_person):
    $ list_of_upgrades = mc_serum_list_of_upgradable_serums()
    if len(list_of_upgrades) == 0:
        the_person "Looks like we don't have any updated serum formulas right now."
    else:
        python:
            for trait in list_of_upgrades:
                trait.upgrade_with_string(the_person)
    return

label mc_serum_review_quantity_label(the_person):
    if not mc_serum_max_quantity() in (1,2,3,4):
        return
    $ the_serum = get_production_serum(mc_serum_max_quantity())
    if not the_serum:
        return
    if mc_serum_max_quantity() == 1:
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_production_1_label(the_person) from _prod_assist_increase_production_01
        else:
            the_person "Right now, we can only safely give you one serum at a time."
            the_person "If we work on researching and mastering production traits, we could probably give you more than one serum at the same time."
            the_person "Specifically, look at the Improved Serum Production trait. I think there is potential there."
    elif mc_serum_max_quantity() == 2:
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_production_2_label(the_person) from _prod_assist_increase_production_02
        else:
            the_person "Right now, we can only safely give you two serums at a time."
            the_person "If we work on researching and mastering production traits, we could probably give you more serums at the same time."
            the_person "Specifically, look at the Advanced Serum Production trait. I think there is potential there."
    elif mc_serum_max_quantity() == 3:
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_production_3_label(the_person) from _prod_assist_increase_production_03
        else:
            the_person "Right now, we can safely give you three serums at a time."
            the_person "If we work on researching and mastering production traits, we could probably give you even more serums at the same time."
            the_person "Specifically, look at the Futuristic Serum Production trait. I think there is potential there."
    else:
        the_person "Right now, we can safely give you four serums at a time."
        the_person "I think this is about the limit of how many serums you can take simultaneously."
    $ the_serum = None
    return

label prod_assistant_essential_oils_intro_label(the_person):
    "As you walk into the production area, a very strange mixture of smells enter your nostrils."
    "You are having trouble placing the smell... Is there a chemical leak somewhere!?!"
    "You quickly scan the room. You notice [the_person.title] at a desk... with a strange chemical diffuser sitting next to her?"
    $ the_person.draw_person(position = "sitting")
    "You walk over. The smell is definitely coming from the diffuser."
    mc.name "[the_person.title]... can I ask what you are diffusing into the room?"
    the_person "Oh! Hello [the_person.mc_title]! Yeah I was having some trouble concentrating, so I got out my essential oil diffuser."
    "She can't be serious..."
    if the_person == ashley:
        the_person "It's my own personal mix of peppermint, rosemary, and lemon oils! Really helps me... Ahhhh ha ha ha ha I'm just kidding."
        the_person "Can you believe that people actually buy this stuff?"
        "You take another whiff... the smell is very confusing. And personally you find it a bit distracting."
        mc.name "Well, I don't think it is a good idea to be diffusing that around here. We have a lot of chemicals we store in the building, and for a minute I thought we had a leak or spill."
        the_person "Oh, yes sir! Don't worry, this batch is almost out anyway. This stuff is so expensive. Actually, you would be surprised how much money people spend on this garbage!"
        "Hmmm... expensive?"
        mc.name "So, this is something people pay a lot of money for? These, essential oils?"
        the_person "Yeah, the whole thing is nuts. I had a shop owner at the mall pawn these off on me as a free sample the other day, but they are crazy expensive."
        the_person "Some people diffuse them, rub them on their skin, even take them orally."
        mc.name "That's interesting. So you can take them orally? And they are perfectly safe?"
        the_person "Yeah, from what I've seen, they don't do a thing if taken orally. Good or bad."
        "You consider this for a moment. Maybe this is something you could use?"
        the_person "You know what you could do? Take some to [mc.business.head_researcher.fname]. I bet she could figure out how to make a serum trait out of them."
        the_person "You could probably use them to help turn a significant profit."
        mc.name "That's a good idea."
        the_person "Here, take these. I was just trying to annoy the other girls with them anyway, but it doesn't seem to be having much of an effect on them."
        "You take the essential oils from [the_person.title]. You should take them to your head researcher."
    else:
        the_person "It's my own personal mix! It has peppermint, rosemary, and lemon oils! It really helps me concentrate!"
        "You do your best not to roll your eyes. You can't believe people actually buy this stuff."
        mc.name "Well, I don't think it is a good idea to be diffusing that around here. We have a lot of chemicals we store in the building, and for a minute I thought we had a leak or spill."
        the_person "Yeah... I was getting some dirty looks from some of the other employees anyway. Sorry sir, I won't do it again."
        the_person "They are too expensive for me to waste at work, anyway..."
        "Expensive? You consider this for a moment. Maybe this is something you could use?"
        mc.name "So, this is something people pay a lot of money for? These, essential oils?"
        the_person "Yeah! Only the purest of extracts are used, I pay top dollar for the best!"
        "You consider it. You should head over and talk to [mc.business.head_researcher.title] about it. Maybe you could use them or something similar to increase serum profits."
    $ add_quest_essential_oils_research_start_action()
    return

label quest_essential_oils_research_start_label(the_person):
    $ the_person.draw_person()
    "You greet your head researcher."
    mc.name "Hello, I have a quick question for you. Have you ever heard of essential oils?"
    the_person "Oh god, don't start with that bullshit..."
    mc.name "Right, well, I was talking to another employee, and apparently there are people out there who will pay big money for them."
    the_person "There's a sucker born every minute, or so I've heard."
    mc.name "So... would it be possible to create a serum trait using essential oils? Not to do anything meaningful, but as a way of driving up the price."
    "[the_person.title] stops and considers what you are saying for a moment."
    the_person "I... think so? I don't know if there's any major negative side effects associated with them. I could look into it the next couple of days and get back to you."
    mc.name "Perfect. Let me know what you find out."
    the_person "Okay. Is there anything else I can do for you?"
    $ add_quest_essential_oils_research_end_action()
    return

label quest_essential_oils_research_end_label(the_person):
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. Just the man I was hoping to see. I did some research on those essential oils you were asking about."
    mc.name "And?"
    the_person "Well, they are mostly related to placebo effect. People think they work, so they imagine they feel better or whatever else after they use them."
    the_person "Most of them also have some sort of negative side effect, but they are all mostly benign. It wouldn't be too hard to make a serum trait like you were asking."
    mc.name "That's great, that is exactly what I was hoping to hear."
    the_person "Just to give you a heads-up though. Some of those oils are hard to extract, and for our company we would need to buy them in pretty bulk sizes..."
    mc.name "Hmm, so I may need to find a supplier."
    the_person "Yup! Sorry, I don't know where you could source this stuff. Here's a list of which ones would be appropriate for us to use."
    mc.name "Thanks, that's exactly what I needed."
    "It was [mc.business.prod_assistant.possessive_title] that suggested it in the beginning. Maybe she can tell you where to get more from?"
    $ add_quest_essential_oils_discover_supplier_action()
    return

label quest_essential_oils_discover_supplier_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello, I have a quick question for you."
    the_person "Yeah [the_person.mc_title]?"
    mc.name "Those oils you had the other day in here. Where did you get them from?"
    the_person "Well, I get mine from over at the mall. I like to hang out there on the weekend sometimes. The one I got is from the weird lifestyle coach lady..."
    mc.name "Do you remember her name?"
    "She thinks about it for a minute."
    the_person "Yes, I'm pretty sure her name is [camila.fname]. She has a small kiosk setup in the mall itself."
    mc.name "Thank you."
    the_person "Yup! Anything else I can do for you?"
    $ add_quest_essential_oils_decision_action()
    return

label quest_essential_oils_decision_label(the_person):
    mc.name "I have an employee who told me she got some essential oils from you. Would you happen to be able to procure a bulk order?"
    the_person "Oh? How big are we talking?"
    mc.name "Well, I am interested in using them in a small run of pharmaceuticals I am developing."
    the_person "Ah, I could set you up with a gallon size for now? A little bit of these things go a long way!"
    mc.name "That sounds good. Here is a list of the ones I need."
    "You hand her the list from your researcher."
    the_person "Okay, I'll need $500 to cover the cost. Do you want to do that up front? Or should I invoice it?"
    mc.name "I'll pay it all now. I have the cash on me."
    the_person "Ok, great!"
    "[the_person.title] takes your information and money."
    $ mc.business.change_funds(-500, stat = "Investments")
    the_person "I'll make sure it gets delivered out to your business right away!"

    $ clear_scene()
    $ add_prod_assistant_unlock_auras_action()
    if mc.business.head_researcher is None:
        "You now have access to the Essential Oils serum trait. It has a high value, but no positive effects and high chance of a negative side effect."
        # we fired the head researcher, so we don't bother checking in with them.
        return
    "You step away from the kiosk. You give your head researcher a call."
    mc.business.head_researcher "Hello?"
    mc.name "Hey, I've procured an order of essential oils. They should be delivered sometime today."
    mc.business.head_researcher "Okay. If you want to research a new serum that uses them, let me know, we should be able to start developing one ASAP."
    "You hang up the phone. You now have access to the Essential Oils serum trait. It has a high value, but no positive effects and high chance of a negative side effect."
    return

label prod_assistant_unlock_auras_label(the_person):
    "You walk into the production room. When you do, [the_person.possessive_title] notices you and waves you over to her desk."
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. I heard about the essential oils. I'm sure they will help out with business profitability!"
    if the_person == ashley:
        the_person "Dealing with them made me get curious a bit. Would it be possible to replicate the supposed results of essential oils?"
        the_person "Essential oils are obviously umm... shall we say... bogus... but do you know what aren't? Pheromones."
    else:
        the_person "I was thinking about them, and I started thinking about how people's bodies produce oils themselves on the skin, especially men."
        the_person "So I talked to [mc.business.head_researcher.fname] about trying to recreate their effects using the body's natural oils."
        the_person "We had a long conversation about... what were they called... pheromones?"
    mc.name "Right, the natural chemicals a person puts out that can act as signal markers to people around them."
    if the_person == ashley:
        the_person "Exactly. Science has done some studies on their effects on various mammals, but effects on humans are notoriously hard to conduct studies on..."
        the_person "Anyway, with some of the research we've been doing on various pheromones, I think it is possible to make a serum for you that would modify your personal pheromone signature."
    else:
        the_person "Yeah! She said that science has done some studies on their effects on various mammals, but effects on humans are notoriously hard to conduct studies on."
        the_person "Anyway, she came back a few hours later with a synthesis process that she said would modify your personal pheromone signature."
    if mc_serum_aura_obedience.is_unlocked:
        if the_person == ashley:
            the_person "I have a prototype for one that I think might make women near you... how do you say... more obedient."
            mc.name "That does sound useful."
            the_person "Let me know if you want to give it a try."
            "You have unlocked Personal Aura serums! These serums effect girls around you with every passage of time."
        else:
            the_person "I'm not sure of the specifics, but she says this prototype would make women around you listen to you more?"
            mc.name "That does sound useful."
            the_person "Let me know if you want to give it a try."
            "You have unlocked Personal Aura serums! These serums effect girls around you with every passage of time."
    else:
        the_person "I haven't come up with a prototype yet, but I think with some more research into other traits it might be something worth pursuing."
        mc.name "That does sound useful. Let me know if you come up with something."
        "You have unlocked Personal Aura serums! These serums effect girls around you with every passage of time."
        "Check the serum review screen for information on what to research to enable them!"
    $ add_prod_assistant_unlock_cum_action()
    $ add_prod_assistant_aura_upgrade_action()
    return

label prod_assistant_unlock_cum_label(the_person):
    $ the_person.draw_person()
    "When you walk into the production room, [the_person.possessive_title] sees you and waves you over."
    mc.name "Hello [the_person.title]."
    the_person "Good day [the_person.mc_title]. I have a question for you."
    mc.name "Go ahead?"
    the_person "Did you know, there was a study done once, that women who regularly get creampied by their partners are less depressed and are less likely to attempt suicide?"
    mc.name "I umm... isn't that an urban myth?"
    the_person "Nope! It was an actual study. The researchers hypothesize that semen contains hormones and chemicals that, when absorbed by women vaginally... or anally or orally really..."
    the_person "Will increase serotonin and other hormone levels."
    mc.name "I see... feeling depressed?"
    the_person "Ah, not particularly! Although I wouldn't be against a preventative dose sometime..."
    $ mc.change_locked_clarity(20)
    the_person "Anyway, I got to looking at the pathways for hormones in men that involve how semen itself is produced."
    the_person "I think I have a viable method for altering these hormones in semen, allowing for a customization of the hormonal properties."
    the_person "It could be used to enhance the anti-depressant effects, or possibly introduce other effects."
    mc.name "That sounds very useful."
    the_person "I've added some info for prototypes to the database. Let me know if you want to try one of the new formulas!"
    "You have unlocked a new category of personal serum traits! This new category changes the effect of your semen on women exposed to it."
    $ add_prod_assistant_unlock_physical_action()
    $ add_prod_assistant_cum_upgrade_action()
    return

label prod_assistant_unlock_physical_label(the_person):
    "Production assistant comments that some of your serums are now altering many girls physical properties."
    "Asks if MC would be interested in trying some of the beneficial ones."
    "Unlocks physical MC serums."
    $ add_prod_assistant_physical_upgrade_action()
    return

label prod_assistant_performance_upgrade_label(the_person):
    $ the_person.draw_person()
    "When you walk into the production room, [the_person.possessive_title] sees you and waves you over."
    mc.name "Hello [the_person.title]."
    the_person "[the_person.mc_title], I have some good news."
    mc.name "Oh?"
    the_person "A recent production equipment upgrade has allowed me to increase the potency of your performance related serums."
    the_person "The equipment that allows us to produce more complicated serums will also allow me to improve the entire category of effects."
    mc.name "Excellent."
    "All performance related personal serums have increased in tier by 1!"
    $ mc.business.event_triggers_dict["mc_serum_energy_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance")
    return

label prod_assistant_aura_upgrade_label(the_person):
    $ the_person.draw_person()
    "When you walk into the production room, [the_person.possessive_title] sees you and waves you over."
    mc.name "Hello [the_person.title]."
    the_person "[the_person.mc_title], I have some good news."
    mc.name "Oh?"
    the_person "A recent production equipment upgrade has allowed me to increase the potency of your aura related serums."
    the_person "The equipment that allows us to produce more complicated serums will also allow me to improve the entire category of effects."
    mc.name "Excellent."
    "All aura related personal serums increase in tier by 1!"
    $ mc.business.event_triggers_dict["mc_serum_aura_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance")
    return

label prod_assistant_cum_upgrade_label(the_person):
    $ the_person.draw_person()
    "When you walk into the production room, [the_person.possessive_title] sees you and walks over."
    the_person "Hey, I could really use your help with something. Can we go to your office?"
    mc.name "Certainly."
    "You walk with [the_person.title] from the production area to your office."
    $ mc.change_location(ceo_office)
    "You step inside, and [the_person.possessive_title] steps in after you and locks your door. You like where this is going."
    the_person "Take your pants and underwear off and lie down on your desk. I'll take care of the rest."
    mc.name "Damn, not even dinner first? You think I'm some kind of slut?"
    the_person "Very funny. I need a semen sample, and I'd prefer to get it the fun way, but if you are feeling shy I can get you a porn mag, a cup, and some private time?"
    mc.name "Oh... a sample? I guess..."
    "You decide to go ahead and take off your pants and underwear, then sit down on your desk."
    "[the_person.title] walks over to you, then gets down on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    if mc.arousal_perc > 30:
        "Your cock is already rock hard. [the_person.possessive_title!c] runs her tongue along the side a few times, giving you shivers."
    else:
        "[the_person.possessive_title!c] leans forward and sucks in the tip of your rapidly hardening cock."
        "She strokes is softly with her hand as her tongue goes in circles around the tip."
        $ mc.change_arousal(20)
        "She gives you several seconds of attention until you are fully erect."
    $ mc.change_locked_clarity(30)
    "[the_person.title] pulls out a condom and opens the package, then skilfully rolls it down your penis."
    $ mc.condom = True  # set mc condom flag
    mc.name "A condom? Really?"
    if the_person.opinion.creampies > 0:
        the_person "Believe me, I'd love to ride this thing to a satisfying conclusion... but I really do need an uncontaminated sample."
    elif the_person.opinion.bareback_sex > 0:
        the_person "Believe me, I'd love to hop on this thing raw and go for a ride, but I really do need an uncontaminated sample."
    else:
        the_person "Sorry, I need an uncontaminated sample."
    $ the_person.draw_person()
    "She stands up and starts to push you back onto the desk."
    the_person "Lay back. No reason we can't both have a good time doing this."
    if the_person.vagina_available:
        "You lay back on the desk, and [the_person.possessive_title] climbs up on top of you."
    else:
        "You lay back on the desk, and [the_person.possessive_title] strips off her bottoms."
        $ the_person.strip_to_vagina()
        "She climbs up on top of you."
    $ the_person.draw_person(position = "cowgirl")
    $ mc.change_locked_clarity(30)
    "[the_person.title] gives you a few strokes with her hand, checking the condom for any issues, then points it up at her pussy and slowly lets herself down on it."
    $ the_person.change_arousal(15)
    $ mc.change_arousal(15)
    the_person "Oh fuck..."
    mc.name "So... what do you need a sample for... anyway?"
    "[the_person.title] starts to roll her hips a bit before she answers."
    the_person "I ah, found some research involving diet and cum potency. I think that if I analyse your semen, I can better formulate your semen related personal serums."
    mc.name "You mean like, make them more effective?"
    the_person "Exactly... Mmmm it's so big..."
    $ the_person.change_arousal(35)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "This whole scenario feels oddly clinical... but it is still hot to have [the_person.possessive_title] riding you like this... for science."
    the_person "Mmm... oh yeah... I'm glad we did this... the fun way..."
    $ the_person.change_arousal(35)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "[the_person.title] stops rocking her hips and starts bouncing on your cock instead. She is {i}really{/i} enjoying herself."
    the_person "Fuck your cock is so good... I think I'm gonna cum!"
    $ the_person.change_arousal(55)
    $ mc.change_arousal(35)
    $ mc.change_locked_clarity(50)
    "Her moans crescendo as her body starts to twitch in pleasure. You give in to the pleasure as well."
    mc.name "Me too. I'm cumming!"
    $ climax_controller = ClimaxController(["Cum inside her", "pussy"])
    $ climax_controller.show_climax_menu()
    the_person "Yes! Ah!"
    "[the_person.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
    "Her breath catches in her throat when you pulse out your hot load of cum into the condom."
    $ the_person.have_orgasm()
    $ climax_controller.do_clarity_release(the_person)
    $ mc.reset_arousal()
    "[the_person.possessive_title!c] holds herself in place until you are completely spent."
    the_person "Alright... let me do this..."
    "She carefully climbs off you, then produces a small sterile sample cup."
    "She pulls your condom off, being cautious not to spill any, and transfers it over to the cup."
    $ mc.condom = False  # remove condom flag
    $ the_person.draw_person()
    the_person "Ah ha! That should do it."
    mc.name "So... you think this will increase the potency of my serums?"
    the_person "Yeah, give me a bit to get it analysed, but I think it should increase the potency of the cum related person serums across the board."
    mc.name "That sounds great. I'm just going to take a minute..."
    the_person "I'll leave you to recover then."
    if not the_person.is_wearing_planned_outfit:
        "[the_person.possessive_title!c] quickly gets dressed."
        $ the_person.apply_planned_outfit(show_dress_sequence = True)
    $ the_person.draw_person(position = "walking_away")
    "Smiling she walks out of your office with her sample."
    $ clear_scene()
    "All cum related personal serums have increased in tier by 1!"
    $ mc.business.event_triggers_dict["mc_serum_cum_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance")
    return

label prod_assistant_physical_upgrade_label(the_person):
    "Use this label to start to process of upgrading physical serums."
    "In this label, the production assistant discusses recent progression with physical related serums."
    "All physical related serums increase in tier by 1 after this label."
    $ mc.business.event_triggers_dict["mc_serum_physical_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance")
    return

label prod_assistant_increase_duration_1_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, the serums she gives MC now last an additional 2 days, total of 5 days."
    $ mc.business.event_triggers_dict["mc_serum_duration"] = 5
    return

label prod_assistant_increase_duration_2_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, the serums she gives MC now last an additional 2 days, total of 7 days."
    $ mc.business.event_triggers_dict["mc_serum_duration"] = 7
    return

label prod_assistant_increase_production_1_label(the_person):
    the_person "I have some good news. As we have gained mastery of Improved Serum Production, the risks of side effects from combining serum traits has reduced drastically!"
    the_person "I believe we are at a point where we can combine two of your personal serums now with minimal risk of side effects."
    mc.name "That's great."
    the_person "However, we should be careful not to mix two serums that use similar bio mechanisms. I've broken them down by category to avoid this."
    mc.name "Sounds smart, I'll take a look."
    $ mc.business.event_triggers_dict["mc_serum_max_quant"] = 2
    return

label prod_assistant_increase_production_2_label(the_person):
    the_person "As our mastery of Advanced Serum Production has increased, as a company, we have gotten better at combining several serum effects at once."
    the_person "While my previous advice on not combining serum traits that have the same bio mechanisms holds, I think we can safely combine up to three serums now."
    mc.name "Excellent. I'll review the available serum list shortly."
    $ mc.business.event_triggers_dict["mc_serum_max_quant"] = 3
    return

label prod_assistant_increase_production_3_label(the_person):
    the_person "Our mastery of Futuristic Serum Production has allowed us to create previously thought to be impossible serum combinations."
    the_person "I can safely create one serum from all four categories now for you to use simultaneously."
    mc.name "Thank you [the_person.title], I'll take a look at the available list in a moment."
    $ mc.business.event_triggers_dict["mc_serum_max_quant"] = 4
    return
