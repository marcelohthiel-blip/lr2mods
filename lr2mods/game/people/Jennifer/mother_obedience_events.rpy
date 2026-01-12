# In Jennifer's obedience arc, we slowly make MC the man of the house, by making Jennifer into a subservient housewife.
# In the intro event, we have Jennifer serve MC breakfast in bed, kickstarting the notion of her maid like services
# In the second event, we introduce the idea of "House Rules". Most of these are from Vren's outline, but new ideas are welcome.
# Things like daily breakfast, nude breakfast, breakfast with a service, on demand bed warmer, Arm Candy.

label mom_obedience_man_of_the_house_intro_label():    #intro action
    $ the_person = mom
    "You get up. It is Saturday of the first weekend as a small business owner."
    "As you get up, you use the restroom, then start to walk toward the kitchen."
    "As you pass by [the_person.possessive_title]'s room, you can hear her talking on the phone."
    the_person "Yes, I know. I've always been good for it in the past, but I've had a change of circumstances..."
    the_person "Of course, I just forgot to budget it in."
    "You decide to see what is going on. You peak around the door that was left cracked."
    $ the_person.draw_person(position = "sitting")
    $ mc.change_location(mom_bedroom)
    "She is sitting at her desk, talking on the phone. She doesn't notice you walk in the door."
    the_person "Look, I get paid every two weeks, I'll have it next weekend, it was just an oversight."
    the_person "I'm calling because we received a letter threatening to turn the water off. I've been on time with payments for over three years..."
    "Oh no! It sounds like she forgot to pay the water bill."
    the_person "Yes! It is just a week. Just please add a note that we talked and to hold off turning it off until then..."
    the_person "Thank you! Yes next Friday... Yes I understand..."
    "She hangs up the phone and audibly groans."
    the_person "Ugh what a pain..."
    mc.name "Hey [the_person.title]... everything okay?"
    the_person "Oh!?! Oh hello honey... yes everything is fine."
    the_person "I just... I forgot to budget in the water bill and didn't pay it on time. They sent me this big official angry letter threatening to turn it off."
    the_person "Don't worry about it, I just talked to them and next time I get paid I'll take care of it."
    mc.name "How much is the bill?"
    the_person "It is just fifty dollars. Really though honey, don't worry about it."
    "You consider the issue. You are only one week into your business, and you aren't really turning much profit yet..."
    if mc.business.has_funds(51):
        "However, you still have some of the initial investment money. At only $50, maybe you should help out..."
        menu:
            "Pay the water bill\n{menu_red}Costs: $50{/menu_red}":
                mc.name "I still have a chunk of the initial investment money. Why don't you just take $50 of it?"
                mc.name "It is only $50, and that should reduce the stress level around here some."
                the_person "[the_person.mc_title], I gave you that money for your business. You don't need to try and give it back."
                mc.name "It's okay though, really. Go ahead and take it, I'll move the money over now."
                "You pull out your phone and quickly transfer the money to [the_person.possessive_title]'s account."
                $ mc.business.change_funds(-50, stat = "Family Support")
                "[the_person.title] sighs, but looks up at you and smiles."
                the_person "Thank you honey... that would certainly reduce my stress a little, being completely caught up on bills."
                $ the_person.change_obedience(3)
                the_person "I appreciate you doing that. I'll try to find a way to make it up to you later this week."
                the_person "How's your laundry? I could run a load for you?"
                mc.name "Oh... that would be great. Thanks!"
                $ the_person.draw_person(position = "stand3")
                "[the_person.possessive_title!c] stands up."
                the_person "I'll go start it now, I'm pretty sure the washer is free..."
                $ the_person.draw_person(position = "walking_away")
                "She gets up and leaves the room. You think carefully about your interaction."
                $ clear_scene()
                "She really seemed to appreciate you helping out, and you can't remember the last time she did your laundry..."
                $ mc.business.event_triggers_dict["Mom_Payment_Level"] = 1
            "Move on":
                "You decide that for now, you should keep your initial investment money."
                "However, in the future, you might be able to help out in the future, once you are able to turn a profit."
                "[the_person.possessive_title!c] would certainly appreciate it if you were able to start contributing to household expenses."
                "You turn and step out of her room."
    else:
        "Unfortunately, you've burned through all your initial investment money."
        "However, in the future, you might be able to help out in the future, once you are able to turn a profit."
        "[the_person.possessive_title!c] would certainly appreciate it if you were able to start contributing to household expenses."
        "You turn and step out of her room."
    $ clear_scene()
    "Maybe if you can prove to her that you can be the man of the house and help out with the bills, she'd be willing to do you a favour now and then."
    "With your newly founded serum business, she would make the perfect test subject to see how far you can push personal boundaries."
    "If nothing else, it is always smart to be on mom's good side... right?"
    $ mom.progress.obedience_step = 1
    $ add_mom_obedience_breakfast_intro_action()
    $ add_mom_obedience_weekly_bills_action()
    $ mc.new_repeat_event(f"Budget with {mom.fname}", 5, 0)
    return

# label mom_obedience_breakfast_intro_label():   #120
#     $ the_person = mom
#     "A light knock on your bedroom door wakes you up. A moment later is another knock, a bit louder this time."
#     mc.name "Ahhh... umm... who is it?"
#     the_person "It's me."
#     mc.name "What... what is it?"
#     the_person "I... I thought you might like some breakfast. I brought you some."
#     mc.name "Ummm... sure!... Come in!"
#     $ the_person.draw_person()
#     "You groggily sit up in bed as [the_person.possessive_title] opens the door and turns on the lights."
#     the_person "I know it is early... I normally hear your alarm going off by now."
#     "She steps over to your bed and is carrying a tray of food. You see bacon, eggs, potatoes, and a big mug of coffee."
#     mc.name "Wow... this looks great!"
#     the_person "Yeah I... I woke up this morning a little early and was just thinking about how nice it has been, with you stepping up around the house lately."
#     the_person "I just wanted to make sure you know that I appreciate you helping with the bills and everything else."
#     mc.name "Of course... wow..."
#     "You grab the tray of food and start to dig in. Once in a while [the_person.possessive_title] will make a little extra breakfast for you, but this is way beyond what she normally does."
#     if the_person.is_employee:
#         the_person "So, I know that I work there now, but I don't really dig into the financials."
#         the_person "I was wondering, how are things going at your business?"
#     else:
#         the_person "So... while you are eating, I was wondering... how are things going at your business?"
#     mc.name "They are going pretty well. Sometimes research is a little bit slow, but we are making steady progress."
#     the_person "I see, is there anything I could do? To help?"
#     mc.name "Well... we could always use more test participants. It is helpful to have test subjects when we have proposed final version of drugs ready."
#     the_person "Oh... you need me to be a... a lab rat?"
#     mc.name "I guess you could call it that. Mostly we are looking for subtle things, like rare or hard to measure side effects."
#     mc.name "The drugs themselves are perfectly safe, but it would be useful to be able to try them in a home like setting, in a position where we could measure the effects in a real world environment."
#     the_person "I see... hmmm..."
#     "She thinks about it for a minute."
#     the_person "I would be okay with that... with being your lab rat once in a while."
#     the_person "But only after I get off work. I don't want them to effect my job performance!"
#     mc.name "Most of them wear off after a good night's sleep anyway."
#     the_person "Okay. Come find me in my room after dinner. If I'm not too tired, I'll help you test your serums."
#     mc.name "Wow, thanks mom!"
#     "You return to eating your breakfast in bed."
#     $ mc.change_energy(50)
#     "When you finish, [the_person.title] takes the tray."
#     mc.name "That was amazing. Feel free to do that anytime!"
#     the_person "Don't expect it every day, but I'll keep that in mind!. I'll take this to the kitchen. I hope you have a great day!"
#     mc.name "Thanks!"
#     $ clear_scene()
#     "[the_person.possessive_title!c] leaves your room. You look at your phone and see the alarm coming up in three minutes. You turn it off."
#     "It is interesting that she felt the need to make you breakfast in bed. You certainly don't mind it."
#     "You've noticed in general that she has been getting a little bit submissive to you since you started helping with the house and bills."
#     "You wonder if you could manage to convince her to do other things for you too..."
#     "You briefly imagine [the_person.title], walking around the house in just an apron, greeting you at the door when you get off work, and slowly getting on her knees..."
#     $ mc.change_locked_clarity(30)
#     "Step by step, you think to yourself. You don't want to rush anything."
#     "Being able to reliably get her to test your serums will really help though. You can now visit her at night in her room and ask her to help you test a serum."
#     $ mom.progress.obedience_step = 2
#     return

label mom_obedience_home_uniform_label():    #140
    $ the_person = mom
    $ add_mom_outfit_coloured_apron(the_person)
    $ the_person.draw_person()
    if mom.is_at(kitchen):
        "You step into the kitchen, you notice [the_person.possessive_title] working hard, doing some cleaning."
    else:
        "You step into the room. You notice [the_person.possessive_title] working hard, doing some cleaning."
    mc.name "Hey [the_person.title], how are you doing?"
    the_person "Oh? Oh hi [the_person.mc_title]. Just working up a sweat, getting some cleaning done."
    mc.name "Yeah? Your outfit looks very hot. Why don't you take the apron off?"
    the_person "It's so hot in here, but I don't want to get my shirt dirty."
    mc.name "Hmmm... I see."
    "The solution seems obvious... but you aren't sure if she would be willing to go along with it."
    mc.name "Why don't you take your shirt off then?"
    the_person "Pardon?"
    mc.name "You could still wear the apron, your shirt would stay clean, and you would be a lot cooler."
    "She seems to think about your proposal."
    if the_person.event_triggers_dict.get("housework_apron", False):
        the_person "I suppose I did almost the same thing other day and it was okay..."
    the_person "You wouldn't be upset if I just had the apron on instead of a shirt?"
    mc.name "No, in fact I would really appreciate it. Your body is fantastic, and it would give me the chance to appreciate it a bit more."
    if the_person.effective_sluttiness() > 30:
        "She chuckles, nodding."
        the_person "Yeah, I'm sure you would!"
    else:
        "She blushes a bit, but nods."
        the_person "Yeah... I guess that would be okay."
    the_person "Alright... one second."
    "She quickly takes off her shirt, leaving her apron in place."
    $ mom_outfit_01 = the_person.outfit
    $ mom_outfit_01.remove_shirt()
    $ the_person.apply_outfit(mom_outfit_01)
    $ the_person.draw_person()
    the_person "There... you're right, this is better!"
    mc.name "Yes... definitely... you should wear outfits like this around the house all the time."
    "You are half joking when you say it, but her response surprises you."
    the_person "Ahhh, I guess if it would mean that much to you."
    the_person "Maybe you could help me pick out a few other outfits that you like that I could wear around the house later?"
    mc.name "Oh? Yeah... definitely."
    the_person "Great!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title!c] turns and starts cleaning again, wearing the outfit without her shirt."
    "You can now give her new outfits to wear around the house. For now though, they need to be regular outfits with the shirt removed and an apron..."
    $ mom_home_wardrobe.wardrobe.add_outfit(mom_outfit_01)
    $ mom.progress.obedience_step = 3
    $ del mom_outfit_01
    return

label mom_weekly_bills_label():
    $ the_person = mom
    $ add_mom_obedience_weekly_bills_action()
    $ current_bill_level = mc.business.event_triggers_dict.get("Mom_Payment_Level", 0)
    "As you get up, you use the restroom, then start to walk toward the kitchen."
    "As you pass by [the_person.possessive_title]'s room, you hear her call out to you."
    the_person "[the_person.mc_title]? Is that you? Can you come in for a moment?"

    $ mc.change_location(mom_bedroom)
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] is sitting at her desk, with her computer on and several bills in front of her."
    the_person "Hey, I'm glad I caught you. I was just working on bills, and I was just wondering..."
    the_person "Do you think you would be able to contribute this week?"

    if lily.event_triggers_dict.get("sister_instathot_special_pictures_recent", False) and not lily.event_triggers_dict.get("sister_instathot_mom_knows", False): #She sold special pictures this week and Mom doesn't know about them yet.
        call mom_weekly_pay_lily_question(the_person) from _call_mom_weekly_bill_lily_question
        $ lily.event_triggers_dict["sister_instathot_special_pictures_recent"] = False

    if current_bill_level == 0:
        the_person "I know things have been really tight... but I'm not sure I'm going to be able to pay the water bill again this week..."
    elif current_bill_level == 1:
        the_person "I can probably swing it, but if you would be willing to help with the water bill again, I could afford to get coffee on the way to work once in a while..."
    elif current_bill_level == 2:
        the_person "It was so nice when you helped out with the groceries, I could get better quality food for the whole family if you helped out again..."
    elif current_bill_level == 3:
        the_person "When you paid for the electric bill, I had enough extra cash to get lunch out a couple times during the week, and I really appreciate that..."
    elif current_bill_level == 4:
        the_person "When you pay for the mortgage, I feel I actually have disposable income again! But if you can't this week I understand..."
    "You consider what bill you could take care of for her."
    menu:
        "Pay the water bill\n{menu_red}Costs: $50{/menu_red}":
            mc.name "I can cover the water bill this week."
            $ the_person.change_stats(love = 1, max_love = 20, obedience = 1, max_obedience = 120, happiness = 1)  #Leave this here since it is the base compliance level
            if current_bill_level == 0:
                $ mc.business.event_triggers_dict["Mom_Payment_Level"] = 1
                the_person "Oh my god... what a relief! I was really worried about that."
            elif current_bill_level > 1:
                the_person "I see. Boy things have just been really tight this past week, haven't they?"
                the_person "I appreciate you being able to help."
            else:
                the_person "Oh good. I wasn't sure if you would be able to do that gain or not. I really appreciate the help!"
            $ the_person.add_situational_obedience("payment", 5, "He helped with bills this week.")
            "You pull out your phone and transfer the cash to [the_person.possessive_title]'s account."
            $ mc.business.change_funds(-50, stat = "Family Support")

        "Pay for groceries\n{menu_red}Costs: $100{/menu_red}" if current_bill_level > 0:
            if current_bill_level == 1:
                $ mc.business.event_triggers_dict["Mom_Payment_Level"] = 2
                $ the_person.change_stats(love = 2, max_love = 30, obedience = 5, max_obedience = 140, happiness = 5)  #Big chunk of obedience the first time
                the_person "Wow... groceries? That would be amazing! Are you sure?"
                mc.name "I'm sure. Maybe use the extra money to get better quality stuff too. Maybe a couple steaks this week?"
                the_person "Oh [the_person.mc_title], thank you! I appreciate you sacrificing for the family like this!"
            elif current_bill_level > 2:    #We've set the expectations higher...
                the_person "Thank you. I appreciate you being willing to do that for us."
                $ the_person.change_stats(love = 1, max_love = 30, obedience = 1, max_obedience = 140, happiness = 1)
            else:
                the_person "Oh good. Thank you honey, it means so much that you are able to help this way!"
                $ the_person.change_stats(love = 1, max_love = 30, obedience = 2, max_obedience = 140, happiness = 2)
            "You pull out your phone and transfer the cash to [the_person.possessive_title]'s account."
            $ the_person.add_situational_obedience("payment", 10, "He helped with bills this week.")
            $ mc.business.change_funds(-100, stat = "Family Support")


        "Pay the electric bill\n{menu_red}Costs: $200{/menu_red}"if current_bill_level > 1:
            if current_bill_level == 2:
                $ mc.business.event_triggers_dict["Mom_Payment_Level"] = 3
                $ the_person.change_stats(love = 3, max_love = 40, obedience = 5, max_obedience = 160, happiness = 5)  #Big chunk of obedience the first time
                the_person "You... you don't have to do that! Your sister and I run the bill up with the hot water and..."
                mc.name "I'm sure. I'm just glad I'm able to be the man that is able to take care of you two."
                the_person "Oh [the_person.mc_title], thank you! This gives me a little of discretionary spending for the first time in a long time!"
            elif current_bill_level > 3:    #We've set the expectations higher...
                the_person "Thank you. I appreciate you being willing to do that for us."
                $ the_person.change_stats(love = 1, max_love = 40, obedience = 1, max_obedience = 160, happiness = 1)
            else:
                the_person "Wow, you are paying the electric again? Thank you honey, it means so much that you are able to help this way!"
                $ the_person.change_stats(love = 1, max_love = 40, obedience = 2, max_obedience = 160, happiness = 2)
            $ the_person.add_situational_obedience("payment", 15, "He helped with bills this week.")
            "You pull out your phone and transfer the cash to [the_person.possessive_title]'s account."
            $ mc.business.change_funds(-200, stat = "Family Support")


        "Pay the mortgage\n{menu_red}Costs: $500{/menu_red}"if current_bill_level > 2:
            if current_bill_level == 3:
                $ mc.business.event_triggers_dict["Mom_Payment_Level"] = 4
                $ the_person.change_stats(love = 3, max_love = 50, obedience = 7, max_obedience = 180, happiness = 5)  #Big chunk of obedience the first time
                the_person "[the_person.mc_title]... I didn't mean to leave that bill laying out, just pretend you didn't see it..."
                mc.name "[the_person.title]. I want to. I want to do my part and give back to the family. Let me pay the mortgage this week."
                the_person "Oh [the_person.mc_title], thank you! It has been amazing to watch you grow into being the man of the house this way! I'm so proud of you!"
            elif current_bill_level > 4:    #We've set the expectations higher... Not possible in the current build
                the_person "Thank you. I appreciate you being willing to do that for us."
                $ the_person.change_stats(love = 1, max_love = 50, obedience = 1, max_obedience = 180, happiness = 1)
            else:
                the_person "Wow, Sometimes I still can't believe you are doing this."
                the_person "Thank you [the_person.mc_title]! It means so much to me that you are doing this for our family."
                $ the_person.change_stats(love = 1, max_love = 50, obedience = 2, max_obedience = 180, happiness = 2)
            $ the_person.add_situational_obedience("payment", 20, "He helped with bills this week.")
            "You pull out your phone and transfer the cash to [the_person.possessive_title]'s account."
            $ mc.business.change_funds(-500, stat = "Family Support")

        "Do not contribute":
            mc.name "Sorry [the_person.title], I can't contribute this week."
            the_person "I see..."
            $ the_person.change_obedience(-2)
            "She sighs, then looks up at you and forces a smile."
            the_person "Well, I'll get these bills paid somehow. You better let me get to work."
            $ clear_scene()
            "You back out of her room and leave her to financial planning."
            return

        #TODO option to just pay off the entire mortgage in one go.

    #Reward dialogue
    if the_person.obedience < 120:
        the_person "You know, I am really proud of you for helping out like this. It means a lot to me."
        mc.name "Of course. If I'm to be a part of this family, I need to also do my part."
        the_person "Maybe there is something I could do repay the favour?"
    elif the_person.obedience < 140:
        the_person "I'm so happy that you are willing to step up and help out again like this."
        "She glances over at the door, as if to make sure it is closed..."
        the_person "Is there anything I could do? To repay the favour?"
    elif the_person.obedience < 160:
        the_person "It has been so nice to have a man around the house again. This means so much to me."
        "She gives you a wide smile."
        the_person "Is there anything I could help you with, [the_person.mc_title]?"
    elif the_person.obedience < 180:
        the_person "You keep amazing me, taking care of your family like this. You've really become the man of the house, haven't you?"
        "She looks up at you from her bills and smiles."
        the_person "Is there *anything* I can do to repay you, [the_person.mc_title]?"
    elif the_person.obedience < 200:
        the_person "Wow, you're so amazing! [the_person.mc_title], what can I do for you this week?"
        the_person "I want to repay you for this somehow!"
    else:
        the_person "Is there anything I can do to serve the man of house? I'll make it up to, any way you want, just say the word!"
    "You think about it for a moment."
    call screen main_choice_display(build_menu_items([build_mom_weekly_bills_menu()]))
    if isinstance(_return, Action):
        $ _return.call_action()
    $ the_person.clear_situational_obedience("payment")
    mc.name "I'm going to go get some breakfast now."
    the_person "Okay, I'm going to finish up with bills."
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    "You leave [the_person.possessive_title]'s room and continue to the kitchen."
    $ mc.change_location(kitchen)
    return

label mom_home_change_wardrobe_label(the_person):
    mc.name "I'd like to talk to you about what you wear around the house."
    the_person "Oh?"
    "You take a look at [the_person.title]'s home wardrobe."
    if mom.sluttiness < 70:
        "Right now, she is willing to wear normal outfits, but with an apron instead of a top."
        "They need to have a bra, panties, an apron, and either a skirt or pants."
    elif mom.event_triggers_dict.get("vaginal_revisit_complete", False):
        "She will wear any kind of outfit as long as it has an apron."
    elif mom.event_triggers_dict.get("anal_revisit_complete", False):
        "She will wear any kind of outfit as long as it has an apron and panties."
    elif mom.event_triggers_dict.get("oral_revisit_complete", False):
        "She will only wear outfits as long as it has her vagina is not visible, it has pants or a skirt and an apron."

    call outfit_master_manager(wardrobe = mom_home_wardrobe.wardrobe, start_mannequin = the_person, show_overwear = False, show_underwear = False, outfit_validator = mom_home_outfit_check) from _call_outfit_master_manager_mom_home_chance_wardrobe
    return

label mom_test_serum_night_label(the_person):
    mc.name "Hey [the_person.title], I have something for you to test out for me."
    the_person "Sure, whatever you need [the_person.mc_title]."
    call give_serum(the_person) from _call_give_mom_serum_77
    if _return:
        "You give [the_person.possessive_title] the serum. She quietly drinks it then hands back the empty vial."
        $ the_person.change_obedience(1)
        the_person "Okay, is there anything you need to do to test and see if it does what you wanted?"
        $ mc.business.event_triggers_dict["mom_serum_test_count"] = mc.business.event_triggers_dict.get("mom_serum_test_count", 0) + 1  #We save this number for Lily... might as well track it for Jen?

    else:
        mc.name "Sorry [the_person.title], I forgot to bring the serum home with me."
        the_person "That's okay [the_person.mc_title], maybe tomorrow night?"
        mc.name "Maybe..."
        return
    menu:
        "Run basic diagnostic test":
            mc.name "I have a pretty basic survey that we can run. Let me see here..."
            "You pull up your basic serum survey on your phone."
            "After several minutes, you have a serviceable set of results."
            $ the_person.apply_serum_study()
        "Run masturbation test" if the_person.opinion.masturbating > -2 and the_person.effective_sluttiness() >= 20:
            mc.name "Alright, to get the best data, we've discovered at the lab that sometimes having a subject orgasm can trigger additional effects."
            mc.name "I'm going to run a basic survey now, and then I'll have you masturbate, and then run another survey after."
            if the_person.effective_sluttiness() < 30:
                the_person "Wait... you need me to what?"
                mc.name "Masturbate. Don't worry, I'll leave the room and you can just let me know when you finish."
                "She mutters for a moment."
                the_person "That... are... you really do that at your lab?"
                mc.name "Yes, and I need to be able to study the effects here as well."
                the_person "I guess..."
            else:
                the_person "Hmmm, okay."
            "You pull up your basic serum survey on your phone."
            "After a few minutes, you have a serviceable set of results."
            $ the_person.apply_serum_study()
            mc.name "Alright, now it is time for you to masturbate."
            if the_person.effective_sluttiness("bare_pussy") < 25 or not the_person.event_triggers_dict.get("kissing_revisit_complete", False):  #She requires privacy
                the_person "Okay, just give me a few minutes and all I'll call you back in, okay?"
                mc.name "Alright."
                $ clear_scene()
                "You step outside of [the_person.possessive_title]'s bedroom, waiting at the door."
                "After a few moments, you hear the faintest of moans and gasps coming from inside."
                the_person "Mmmm.... ahhh..."
                $ mc.change_locked_clarity(30)
                "You imagine the view of what is going inside that room right now. It would be so hot to be able to watch her as she masturbates..."
                the_person "Ahhh!!!! Mmmmm..."
                $ the_person.have_orgasm(force_trance = False, sluttiness_increase_limit = 40)
                "After several minutes, you hear a brief crescendo, then silence."
                "You wait several more moments."
                the_person "Ah... okay honey... you can come back in..."
                $ the_person.draw_person(position = "sitting")
                "When you walk back in, she is sitting on the side of her bed."
            else:
                if the_person.effective_sluttiness("bare_pussy") < 50:    #She hesitates for a moment but starts anyway
                    the_person "Okay... this is a little weird but if that is what you need..."

                else:
                    the_person "Okay!"
                $ the_person.draw_person(position = "back_peek")
                if the_person.vagina_available and the_person.vagina_visible:
                    "[the_person.title] turns and starts to walk to her bed."
                else:
                    "[the_person.title] turns to strips off her bottoms, then steps over towards her bed.."
                    $ the_person.strip_to_vagina(prefer_half_off = False, position = "back_peek")
                the_person "Is it okay if I lay on my bed?"
                mc.name "Yeah sure, wherever is comfortable for you."
                $ the_person.draw_person(position = "missionary")
                "[the_person.title] lays down on her back and spreads her legs, giving you a view as she starts to touch herself."
                $ mc.change_locked_clarity(40)
                $ the_person.change_arousal(15)
                $ eyes_closed = False
                if the_person.effective_sluttiness("bare_pussy") < 30:  #A little shy, so she closes her eyes and goes at it. We slowly amp things up from here.
                    "[the_person.possessive_title!c] fingers go right to work, going in circles around her clit as she closes her eyes."
                    "It is pretty hot, getting to watch your mother masturbate. You assume she is imagining getting fucked by some hot stud."
                    $ mc.change_locked_clarity(30)
                    $ eyes_closed = True
                else:   #She asks for some eye candy to help.
                    "[the_person.possessive_title!c] fingers go right to work, going in circles around her clit as she looks over at you."
                    "It is pretty hot, getting to watch your mother masturbate. It is even hotter the way she is looking right at you as she does it."
                    $ mc.change_locked_clarity(40)
                    $ mc.change_arousal(10)
                $ the_person.change_arousal(25) #40
                "She stops the circles for a moment, running her ring and middle finger up and down her slit a few times, and then slowly pushes them into her pussy."
                "The angle is tough, and she can only get them in up to the second knuckle, but she starts to finger herself."
                if eyes_closed:
                    "[the_person.title]'s pleasure is just beginning, as she starts to lose herself to the feelings."
                    $ mc.change_locked_clarity(30)

                elif the_person.effective_sluttiness("bare_pussy") < 35:
                    "With her pleasure just beginning, [the_person.title] closes her eyes and begins to let herself give in to the feelings."
                    $ eyes_closed = True
                    $ mc.change_locked_clarity(30)
                else:
                    "[the_person.title]'s eyes glaze over a bit now and then, but she continues to look right at you as she masturbates. Is she fantasizing about... you?"
                    $ mc.change_locked_clarity(40)
                    $ mc.change_arousal(10)
                $ the_person.change_arousal(25) #65
                "With two fingers stroking her insides, she must be imagining getting fucked..."
                if eyes_closed:
                    "A hint of feminine arousal hits your nostrils. You wonder how long it will be until it is you between her legs, making her cum for these serum tests..."
                    $ mc.change_locked_clarity(30)
                elif the_person.effective_sluttiness("bare_pussy") < 40:
                    "[the_person.title] closes her eyes as a wave of intense pleasure washes over her."
                    $ eyes_closed = True
                    $ mc.change_locked_clarity(30)
                else:
                    "You are so entranced watching her masturbate, it startles you when she suddenly speaks up."
                    the_person "Can you take your pants off? I want to look at you while I do this..."
                    mc.name "Yeah, yeah of course."
                    "You step around the side of the bed next to [the_person.title], then drop your pants and underwear. Your painfully erect cock springs free."
                    the_person "Oh wow... Thank you [the_person.mc_title], this will just take mommy a bit longer..."
                    $ mc.change_locked_clarity(40)
                    $ mc.change_arousal(10)
                $ the_person.change_arousal(30) #95
                if the_person.opinion.incest > 0:
                    the_person "Oh my god, seeing your amazing cock always gets me so worked up! Mmmm..."
                "[the_person.possessive_title!c] is arching her back a bit now as she continues to finger fuck herself in an incredibly arousing display."
                the_person "Mmmmm... yessssss..."
                if eyes_closed:
                    $ the_person.change_arousal(30)
                    "[the_person.title] moans are starting to get urgent. You watch in awe as her hips and stomach start to twitch erratically."
                    $ the_person.have_orgasm(force_trance = False, sluttiness_increase_limit = 45)
                    $ mc.change_locked_clarity(40)
                    the_person "Ahhh! Oh god..."
                    "She cries out in a brief crescendo, has a couple more spasms, then her arched back falls back onto the bed."
                    "She slowly opens her eyes and looks over at you."
                    the_person "There... is... is that good?"
                    mc.name "Umm yeah... amazing actually."
                    "She blushes for a moment at your compliment."
                else:
                    "[the_person.title]'s eyes are fixed on your manhood as she pushes herself close to the edge."
                    if the_person.opinion.being_covered_in_cum >= 0 and the_person.effective_sluttiness("bare_pussy") >= 50:
                        the_person "Oh my god honey, that looks so painful... Why don't you masturbate too? Here!"
                        $ the_person.strip_to_tits(position = "missionary", prefer_half_off = True)
                        "Before you can respond, [the_person.possessive_title] pulls out her tits."
                        $ mc.change_locked_clarity(50)
                        $ mc.change_arousal(10)
                        the_person "You can cum on mommy's tits. Please cum on my tits!"
                        "Damn. With words like that, you can't help but oblige. You reach down and start to stroke yourself too."
                        "[the_person.title]'s eyes go back and forth, looking at your erection, and then up at your eyes."
                        the_person "Oh god, [the_person.mc_title], I'm gonna cum... are you gonna cum too?"
                        mc.name "Yeah, I'm almost there but not yet..."
                        the_person "Ohhhh fuck I'm not gonna last any longer... oh!"
                        $ the_person.change_arousal(30)
                        $ mc.change_arousal(20)
                        "[the_person.title] moans out her last words, then you watch in awe as her hips and stomach start to twitch erratically."
                        $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 55)
                        $ mc.change_locked_clarity(40)
                        the_person "Ahhh! Oh god..."
                        "Watching her finish drives you over the edge."
                        $ mc.change_arousal(40)
                        mc.name "Oh fuck, [the_person.title] I'm gonna cum too!"
                        "It takes her a moment in her orgasm addled brain to realise what you are saying, but then she quickly reaches up with both hands and presents her tits to you."
                        the_person "That's it, cover my tits with your virile seed!"
                        "You give yourself the last couple of strokes and then point the tip down at [the_person.possessive_title]'s chest as you begin to orgasm."
                        $ ClimaxController.manual_clarity_release(climax_type = "tits", person = the_person)
                        $ the_person.cum_on_tits()
                        $ the_person.draw_person(position = "missionary")
                        "Wave after wave of your cum erupts from the tip and straight onto [the_person.possessive_title]'s tits. She gasps with each hot, sticky impact."
                        "As the last couple of waves finish, a final few drops of cum land on her chest, making her entire body quiver."
                        the_person "Oh wow... is that... is that good enough... for your test?"
                        mc.name "Yeah... that was amazing... an amazing test, I mean."
                        "She chuckles, causing her cum coated upper body to shake slightly."
                    else:
                        $ the_person.change_arousal(30)
                        "[the_person.title] moans are starting to get urgent. You watch in awe as her hips and stomach start to twitch erratically."
                        $ the_person.have_orgasm(force_trance = False, sluttiness_increase_limit = 50)
                        $ mc.change_locked_clarity(40)
                        the_person "Ahhh! Oh god..."
                        "She cries out in a brief crescendo, has a couple more spasms, then her arched back falls back onto the bed."
                        "Her eyes slowly move from your cock to your eyes."
                        the_person "There... is... is that good?"
                        mc.name "Umm yeah... amazing actually."
                        "She blushes for a moment at your compliment."
                mc.name "Alright no rush, but if you want to just sit on the edge of the bed I can give you the second study."
                the_person "Right... of course..."
                $ the_person.draw_person(position = "sitting")
                "She slowly gets up and sits on the side of her bed."

            "You run through the basic survey again, making sure to highlight differences and changes in the results."
            $ the_person.apply_serum_study()
            "You are able to get some excellent data."


    mc.name "Thanks [the_person.title], I really appreciate it."
    the_person "Happy to help, but I think I need to get to bed now."
    if the_person.is_in_trance:
        "The way she is talking, it is clear that [the_person.title] is in a trance. Before you go, maybe you could take advantage of that..."
        mc.name "Sorry [the_person.title], I have just one more thing to go over."
        the_person "Oh? Okay honey, whatever you say..."
        call do_training(the_person) from _call_do_training_mom_lab_rat_01
        "Once finished, you get up."
    mc.name "Goodnight [the_person.title]."
    $ clear_scene()
    "You head to your room and get to bed as well."
    $ mc.change_location(bedroom)
    call advance_time() from _call_advance_time_mom_survey_01
    return

label mom_breakfast_in_bed_crisis_label():  #Once we've unlocked it, once in a while Jennifer gives MC breakfast in bed.
    $ the_person = mom
    #This should be an old label, this has moved to the progression event.
    "In this label, [the_person.possessive_title] delivers MC breakfast in bed."
    return

label mom_weekly_pay_lily_question(the_person):
    if the_person.event_triggers_dict.get("mom_instathot_questioned", False):
        the_person "Before we talk about that, do can I ask you a question?"
        mc.name "Sure, what do you want to know?"
        the_person "Well, it's your sister again. She had more money to help with the bills, but she still won't tell me where it's from."
        the_person "I know I said I wouldn't pry, but the only times she leaves the house is to go to class."
        the_person "I just really want to be sure she's not in some sort of trouble."
    else:
        the_person "Oh, before we talk about that I'm hoping you can answer something for me."
        mc.name "Okay, what do you need to know?"
        the_person "Your sister was very strange just now. She actually offered to help with the bills."
        the_person "She wouldn't tell me where she's getting this money though."
        the_person "I respect her privacy, but I want to make sure she isn't getting into any trouble."
        $ the_person.event_triggers_dict["mom_instathot_questioned"] = True

    menu:
        "Cover for [lily.fname]":
            if the_person.event_triggers_dict.get("mom_instathot_questioned", False):
                mc.name "She's working on campus, so I guess she's working between classes."
                the_person "I just wish she would trust me."
                mc.name "I'm sure she'll tell you eventually, but you don't need to worry about her."
                the_person "I hope she does. Thank you [the_person.mc_title]."

            else:
                mc.name "Uh... No, she isn't getting into any trouble. I think she's just got a job on campus."
                the_person "Really? Why wouldn't she tell me about that, I'm so proud of her!"
                mc.name "I don't know, maybe she didn't want you to think she's doing it just because we need money."
                the_person "Well, I'll let her tell me when she's ready. I'm just happy to know it's nothing to worry about."

        "Tell her about InstaPic":
            mc.name "Well, I think she's picked up a part-time job."
            the_person "Oh, why haven't I heard about this?"
            mc.name "It's not exactly a traditional job. She's been putting pictures up on InstaPic."
            the_person "InstaPic? Isn't that an internet thing? I don't understand."
            mc.name "[lily.fname] puts up pictures showing off clothing, and InstaPic pays her for the ad traffic she generates."
            the_person "So it's like modelling, but she can do it from home?"
            mc.name "I guess so, yeah. She's just worried that you wouldn't approve."
            the_person "Why wouldn't I? Models can be very successful. And there are no photographers or agents to take advantage of her."
            the_person "I'm going to tell her how proud I am of her. Maybe she'll even let her Mom take a few photos with her."
            "She laughs and shrugs."
            the_person "Never mind, nobody's interested in looking at someone old like me."
            mc.name "You should absolutely ask [lily.fname] to take some pictures with you. I think you'd be surprised."
            the_person "Aww, you're too sweet."
            $ lily.event_triggers_dict["sister_instathot_mom_knows"] = True
            $ add_sister_instapic_discover_crisis()
    return


#########################
# Jennifer weekly bills #
#########################

#These labels are used for the weekly bill paying event.

label mom_weekly_kiss_label():
    $ the_person = mom
    mc.name "How about a kiss?"
    if the_person.has_taboo("kissing"):
        the_person "A kiss?"
        mc.name "For being such a good son."
        the_person "Oh, well that's easy then."
        "[the_person.possessive_title!c] stands up and leans in to give you a kiss on the cheek."
        mc.name "On the lips, [the_person.title]. Please?"
        the_person "You've always been so affectionate. Not like other boys at all, you know. Fine."
        $ kissing.call_taboo_break(the_person, None, None) #We can reuse the kissing taboo break scene for improved dialogue and description.
        $ mc.change_locked_clarity(10)
        "After a moment she pulls back and looks away from you, blushing."
    else:
        the_person "Okay, come here."
        if the_person.effective_sluttiness("kissing") > 30 and the_person.is_willing(kissing):
            "Before you can lean down, she stands up and turns to you."
            $ the_person.draw_person(position = "kissing")
            "She puts her arms around your neck and you get close to her."
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "You lean forward and press your lips against hers. [the_person.possessive_title!c] responds, leaning her body against yours."
            $ the_person.change_arousal(10 + mc.foreplay_sex_skill)
            the_person "Mmm... mmmm..."
            $ mc.change_locked_clarity(20)
            if the_person.opinion.incest > 0:
                the_person "You make me so happy [the_person.mc_title]..."
            "A couple moans vibrate against your lips as your tongues dance against each other. You let your hands roam up and down her sides."
            # Do we want to make an option here to kiss her *other* lips is she is slutty enough?
            # Not really an obedient theme...
            "Her body melts into yours, clearly ready for an extended makeout session if that is what you want."
            menu:
                "Makeout session":
                    "Fuck it. It's a Saturday, may as well start your weekend with a makeout session with [the_person.possessive_title]."
                    call fuck_person(the_person, start_position = kissing, private = True, skip_intro = True) from _call_makeout_weekly_jennifer_01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()
                "Pull back":
                    "You slowly pull away from [the_person.possessive_title]. She is in a bit of a daze."
                    $ the_person.draw_person()
                    the_person "Thank you [the_person.mc_title]. That was wonderful"

        elif the_person.effective_sluttiness("kissing") > 15:
            "You lean down to kiss her as she's sitting. [the_person.possessive_title!c] puts a hand on the back of your head and pulls you against her as your lips meet."
            "Her mouth opens slightly, letting your tongues meet as she makes out with you."
            $ the_person.change_arousal(5 + mc.foreplay_sex_skill)
            "It might be your imagination, but you think you might even hear her moan."
            $ mc.change_locked_clarity(10)
            "When you finally break the kiss she fixes her hair and smiles proudly at you."
        else:
            "You lean down to kiss her. She lets you press your lips against hers, and even returns the gentle kiss after a moment of hesitation."
            $ mc.change_locked_clarity(10)
            "When you finally break the kiss she looks away from you, blushing with embarrassment."

    $ the_person.break_taboo("kissing")
    $ the_person.change_slut(2, 30)
    return

label mom_weekly_please_label():
    $ the_person = mom
    mc.name "Honestly, I just want to hear you say the magic words."
    the_person "Abracadabra?"
    mc.name "No, the words we say when we want help?"
    the_person "Oooh, I see what you're getting at. I've drilled it into you and now I'm getting a taste of my own medicine."
    "She smiles and rolls her eyes playfully."
    $ mc.change_locked_clarity(5)
    the_person "May I {i}please{/i} have some help with the bills?"
    mc.name "I'm not sure if you mean it..."
    the_person "Pretty please, [the_person.mc_title]?"
    $ the_person.change_obedience(2, max_amount = 160)
    mc.name "Perfect! I'm happy to help, [the_person.title]."
    return

label mom_weekly_see_tits_label():
    $ the_person = mom
    mc.name "You could show me your tits? That would certainly be a nice way to repay a favour."
    if the_person.has_taboo("bare_tits") or not mom.event_triggers_dict.get("kissing_revisit_complete", False):
        if the_person.effective_sluttiness() > 30:  #She has no problem with it
            the_person "Oh! [the_person.mc_title], I had no idea you were even interested."
            if the_person.tits_visible:
                if the_person.outfit.has_apron:
                    the_person "Of course. Let me take off the apron so you have a better view."
                    $ the_person.outfit.remove_overcoat()
                    $ the_person.draw_person(position = "sitting")
                    the_person "Well, how do they look?"
                else:
                    the_person "Look all you want! Here..."

            else:
                "Without any further persuasion, she takes off her top."
                $ the_person.strip_to_tits(position = "sitting")
                "When she finishes, you get a good look at [the_person.possessive_title]'s impressive chest."
                the_person "Here, let me give you a better look..."
            $ the_person.draw_person(position = "sitting", display_transform = character_right_flipped(zoom = 1.2))

            "She turns in her chair to face you more directly, giving you a better view of her rack."
            $ mc.change_locked_clarity(20)
            $ the_person.change_arousal(10)
            "She blushes a bit as you stare in awe at her amazing bust. You feel yourself starting to get an erection."
        else:
            if the_person.tits_visible:
                the_person "Normally I would chastise you for asking something like that but..."
                "She looks down. You follow her gaze downward to her already exposed chest."
                the_person "I... I shouldn't let you... but I guess it you want to spend some time just looking..."
                mc.name "Thanks [the_person.title]."
                "You don't bother trying to hide your lecherous gaze now. You gratefully admire her body's amazing curves."
                mc.name "Damn mom, you are absolutely stacked."
                the_person "[the_person.mc_title]! Don't say things like that..."
                $ the_person.change_slut(2, 40)
                $ mc.change_locked_clarity(20)
                $ the_person.change_arousal(10)
                mc.name "I'm glad you feel comfortable enough around the house to let the girls out once in a while. You should do that more often."
            else:
                the_person "[the_person.mc_title]! You really shouldn't be asking something like that of your mother..."
                mc.name "Why not? It seems to me that if I'm going to be the man of the house, I should get SOME of the benefits that the head of household usually gets."
                the_person "Yes but... really? You want to me to take off my... top?"
                "You eagerly urge her."
                mc.name "Absolutely. Besides, it will help motivate me while I'm at work, thinking about what a beautiful woman I have back home to work for."
                the_person "Oh... I suppose a little peek wouldn't hurt anything..."
                $ the_person.strip_to_tits(position = "sitting")
                "When she finishes, you get a good look at [the_person.possessive_title]'s impressive chest."
                mc.name "Damn mom, you are absolutely stacked."
                the_person "[the_person.mc_title]! Don't say things like that..."
                $ the_person.change_slut(2, 40)
                $ mc.change_locked_clarity(20)
                $ the_person.change_arousal(10)
        $ the_person.break_taboo("bare_tits")
        mc.name "Thanks [the_person.title], I really appreciate that."
        $ the_person.draw_person(position = "sitting")
        return
    #If she doesn't have the taboo, check and see if she does it eagerly. If so, have a chance to grope her also.
    if the_person.effective_sluttiness("bare_tits") >= 20 or the_person.is_willing(standing_grope):
        if the_person.tits_visible:
            if the_person.outfit.has_apron:
                the_person "Of course. Let me take off the apron so you have a better view."
                $ the_person.outfit.remove_overcoat()
                $ the_person.draw_person(position = "sitting")
                the_person "Well, how do they look?"
            else:
                the_person "Of course. I like to let the girls out while I'm in my room, go ahead and look all you want."
        else:
            the_person "Of course I'll do that for you. One second..."
            "[the_person.possessive_title!c] takes her top off."
            $ the_person.strip_to_tits(position = "sitting")
        $ mc.change_locked_clarity(20)
        "You get a good look at [the_person.possessive_title]'s impressive chest."
        mc.name "Damn mom, you are absolutely stacked."
        "She chuckles."
        $ the_person.change_arousal(5)
        the_person "Thank you honey. I'm always happy to help brighten up your day a little."
        "Her tits look amazing. You wonder if you could get away with a little touching..."
        menu:
            "Ask to touch her":
                pass
            "Just enjoy the view":
                "You spend several moments enjoying the view of [the_person.possessive_title]'s fun bags."
                $ mc.change_locked_clarity(30)
                $ the_person.change_arousal(10)
                "She blushes a bit as you stare in awe at her amazing bust. You feel yourself starting to get an erection."
                mc.name "Thanks [the_person.title], I really appreciate that."
                return
        mc.name "They look amazing. Can I touch?"
        #If we are here, we already know she's willing. Question is how willing.
        # If she is very willing, she is happy to comply and we have the chance to advance to a tit fuck.
        if the_person.is_willing(tit_fuck) and the_person.obedience > 140:
            the_person "Of course! Here..."
            "She turns in her chair and moves closer to you."
            $ the_person.draw_person(position = "sitting", display_transform = character_right_flipped(zoom = 1.2))
            "She takes your hand in hers and moves it to her soft breast."
            "You eagerly start to grope her heavy tits."
            if the_person.opinion.incest > 0:
                the_person "Mmm, I love the feeling of my son's strong hands on my body..."
            else:
                the_person "Mmm, I love the feeling of a man's strong hands on my body..."
            $ mc.change_locked_clarity(40)
            $ the_person.change_arousal(20)
            "She moans softly as you feel her up. Her nipple hardens and she catches her breath when you give it a little pinch."
            the_person "Oh my... what have we here..."
            "When you look down, you realise [the_person.possessive_title] is face to face with your erection, straining painfully against your pants."
            the_person "You know, for a favour, you could let me take care of that for you?"
            "She uses her hands to cup both her breasts and lifts them up for a moment."
            the_person "Just pull it out, you could put it between these. I'm already warmed up, and I wouldn't mind one bit..."
            "Mmm, do you want to fuck [the_person.possessive_title]'s tits?"
            menu:
                "Fuck her tits":
                    pass
                "You need to be going":
                    mc.name "Sorry [the_person.title], I don't have time, I have somewhere to be this morning."
                    the_person "Ah, okay. I see."
                    $ the_person.change_obedience(1)
                    $ the_person.change_happiness(-2)
                    "She seems to be disappointed, but quietly obeys, turning back to her desk."
                    $ the_person.draw_person(position = "sitting")
                    return
            mc.name "Oh fuck that sounds amazing..."
            "You start to pull down your pants. [the_person.possessive_title] gropes her own tits as she waits for you."
            the_person "Mmm, let's see what we have here..."
            "Your cock springs free, and [the_person.title] smiles delightedly, getting down on her knees."
            $ the_person.draw_person(position = "blowjob")
            "You step closer and slowly slide your cock between [the_person.title]'s fantastic tits. She holds them together as you start to move your hips."
            call fuck_person(the_person, private = True, start_position =tit_fuck, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_tit_fuck_weekly_bills_01
            $ the_report = _return
            $ the_person.draw_person(position = "kneeling1")
            if the_report.get("cum on tits", 0) > 0:    #Finished on her chest
                "[the_person.possessive_title!c] looks up at you from her knees, her tits coated in your cum."
            elif the_report.get("facials", 0) > 0:    #Finished on her face
                "[the_person.possessive_title!c] looks up at you from her knees, her face covered in your cum."
            elif the_report.get("mouth_cum", 0) > 0:    #Finished in her mouth?
                "[the_person.possessive_title!c] licks her lips and looks up at you from her knees."
            the_person "I think that makes us even for this week."
            mc.name "Yes I think so."

        else:
            "She hesitates for a moment. She submits, but you can tell she doesn't like it."
            the_person "If you really want to, but just for a little bit..."
            "You step around behind [the_person.title] and put your hands on her shoulders."
            mc.name "Just close your eyes and enjoy the feelings. You can even pretend I'm someone else."
            the_person "That doesn't make this any more right..."
            "You let your hands travel down from her shoulders, across her collarbone, and down to her magnificent mammaries."
            $ mc.change_locked_clarity(30)
            if the_person.has_large_tits:
                "You take hold of their soft, fleshy mass with both hands. Their girth and heft are incredibly pleasing as you start to rub them."
            else:
                "You take hold of her perky tits with both hands. They fill your hands without being so large as to be unwieldy."
            $ the_person.change_arousal(15 + mc.sex_skills.get("Foreplay", 0))
            the_person "Mmmm.... ahhh..."
            "She moans softly as you start to work up her arousal with your hands."
            if the_person.opinion.incest > 0:
                the_person "Mmm... that feels so good [the_person.mc_title]! Play with mommy's tits!..."
                $ the_person.discover_opinion("incest")
                "Despite her initial protest, she seems to be getting really into it. She has her eyes closed as she gets lost in the sensations you are giving her."
                $ the_person.change_arousal(25 + mc.sex_skills.get("Foreplay", 0))
            else:
                the_person "Mmm, that feels so good..."
                $ the_person.discover_opinion("incest")
                "She has her eyes closed, probably imaging you are someone else, but she is getting into it regardless."
                $ the_person.change_arousal(10 + mc.sex_skills.get("Foreplay", 0))
            the_person "Mmm... that... AH!"
            $ mc.change_locked_clarity(30)
            "You give each nipple a pinch, working them between your thumb and index fingers."
            "Her eyes suddenly snap open."
            $ the_person.change_arousal(15 + mc.sex_skills.get("Foreplay", 0))
            the_person "That feels so good... but you need to stop..."
            menu:
                "Not a chance" if the_person.obedience >= 130:
                    pass
                "Not a chance{menu_red}Requires 130 Obedience{/menu_red} (disabled)" if the_person.obedience < 130:
                    pass
                "Stop":
                    "You slowly let your hands drop away from [the_person.possessive_title]'s chest."
                    the_person "Thank you. We don't want to get carried away right now..."
                    $ the_person.change_stats(love = 2, max_love = 40, happiness = 2, obedience = 1)
                    "You aren't sure if you could push her any further right now, but decide it isn't the right time to push things."
                    "You step back around her desk as she catches her breath."
                    return
            "[the_person.title], don't try to pretend like you aren't enjoying this. You're almost there."
            "Instead of letting go, you increase the intensity of your groping."
            $ the_person.change_arousal(20 + mc.sex_skills.get("Foreplay", 0))
            $ mc.change_locked_clarity(30)
            the_person "Ohhhh, oh my!..."
            "She moans and one of her hands goes to yours. Instead of taking your hand away though, she just places it on top of your hand as you grope her."
            "[the_person.possessive_title!c] looks up at you and you can see her eyes are glazing over a bit."
            "Damn! She's really getting off on having her tits played with! You make one last push to try and get her over the edge."
            $ the_person.change_arousal(15 + mc.sex_skills.get("Foreplay", 0))
            $ mc.change_locked_clarity(30)
            if the_person.arousal >= the_person.max_arousal:    # Orgasm
                "Suddenly, [the_person.title]'s whole body tenses up."
                $ the_person.call_dialogue("climax_responses_foreplay")
                $ the_person.have_orgasm()
                $ the_person.change_stats(obedience = 5, happiness = 2)
                "Her body is twitching and she moans loudly as she cums. You knew that it was possible for some women to orgasm just from nipple and breast play, but this is amazing."
                "When she finishes, you quietly let go."
                "You step back around her desk as she catches her breath."
            else:
                "She is nearly there... but you just can't quite push her past her limit. Her crescendo begins to wane without hitting orgasm."
                the_person "Ahhh, that's enough... you're starting to hurt mommy!"
                $ the_person.change_arousal(-10)
                "You quickly stop. She looks up at you, completely out of breath."
                the_person "That... I was so close, but I need more than just my tits played with to cum [the_person.mc_title]."
                mc.name "Alright, here, let me..."
                the_person "NO! No that's enough for now."
                $ the_person.change_stats(love = 2, max_love = 40, happiness = 2, obedience = 1)
                "You aren't sure if you could push her any further right now, but decide it isn't the right time to push things."
                "You step back around her desk as she catches her breath."

    else:
        the_person "I know I said we could do things like that once in a while... but it still doesn't feel right..."
        mc.name "It seems to me that if I'm going to be the man of the house, I should get SOME of the benefits that the head of household usually gets."
        "She shakes her head, but relents."
        the_person "I still don't understand why you want me to, but who am I to stop your fun."
        "She quietly takes her top off for you."
        $ the_person.strip_to_tits(position = "sitting")
        "When she finishes, you get a good look at [the_person.possessive_title]'s impressive chest."
        mc.name "Damn mom, you are absolutely stacked."
        the_person "[the_person.mc_title]! Don't say things like that..."
        $ the_person.change_slut(2, 40)
        $ mc.change_locked_clarity(20)
        $ the_person.change_arousal(10)
    return

label mom_weekly_touch_me_label():
    $ the_person = mom
    mc.name "I had a really stressful week. It would be REALLY nice if you would help me with some tension."
    mc.name "Any chance I could talk you into a quick handjob?"
    if the_person.is_willing(blowjob) or the_person.sluttiness >= 50:
        the_person "Just a handjob? Certainly honey, that is the least I could do for your help with the budget!"
    elif the_person.is_willing(handjob) and not mom.event_triggers_dict.get("kissing_revisit_complete", False):
        the_person "Certainly honey, I could do that for you."
    else:
        the_person "Oh my... I don't know..."
        mc.name "I mean, you said it yourself that it is nice having a man step up around here."
        mc.name "It would really mean a lot to me."
        if mom.event_triggers_dict.get("kissing_revisit_complete", False):
            the_person "I knew being casual about being naked around each other would lead to something like this..."
            "She sighs."
            the_person "But you're right. If you're going to be the man of the house, it is only fair that I take care of you once in a while..."
        else:
            if the_person.event_triggers_dict.get("kissing_revisit_count", 0) == 0:
                the_person "That's... crazy! A mom shouldn't be jacking off her own son!"
                mc.name "Don't think of it like that. You are just meeting the needs of the man of the house."
                "She thinks about it for a moment, then sighs."
                the_person "You should be looking for a girlfriend."
                mc.name "I will, but between things here and my new business, I'm just really busy."
                the_person "Hmmm... okay... just this once!"
            else:
                the_person "[the_person.mc_title]... we've talked about this."
                the_person "Don't you have a girlfriend or something? Have you tried looking for one?"
                mc.name "I've just been really busy, between the new business and things here."
                "She thinks about it for a moment, then sighs."
                the_person "Okay... just once!"
    "You reach down and unzip your pants, pulling your cock out, while [the_person.possessive_title] slides out of her chair onto her knees."
    $ the_person.draw_person(position = "kneeling1")
    if the_person.event_triggers_dict.get("kissing_revisit_complete", False) and not the_person.tits_visible:
        "Without prompting, she starts taking her top off."
        $ the_person.strip_to_tits(prefer_half_off = False, position = "kneeling1")
        $ mc.change_locked_clarity(50)
        mc.name "Wow. Nice."
        the_person "Yeah I thought that might help you finish a little faster."
        "She gives you a wink."
    "[the_person.title] reaches out and takes your cock in both hands. She gives it a couple soft strokes."
    $ the_person.break_taboo("touching_penis")
    the_person "God, you really are a man... you're so big honey."
    $ the_person.change_arousal(10)
    "After a few more soft strokes, she brings one hand to her mouth and spits into it. She rubs it onto your erection, trying to lubricate it."
    "She has to do this several more times before she has your dick fully lubricated."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title!c] looks up at you and starts to stroke you with her hands."
    #First, check and see if she is going to do the handjob eagerly or conservatively.
    if the_person.effective_sluttiness() >= 35 and the_person.event_triggers_dict.get("kissing_revisit_complete", False):
        #We know for sure that her tits are out#
        #First, she eagerly strokes MC, then we have the chance for her to advance to blowjob
        $ masturbating_mommy = False
        if the_person.opinion.masturbating >= 0:
            $ masturbating_mommy = True
        the_person "Does that feel good? I like it when I make you feel good."
        mc.name "Yeah that feels great. Keep going."
        "She takes one hand off your cock and starts to squeeze one of her tits. She is really getting into it."
        $ mc.change_arousal(15)
        $ mc.change_locked_clarity(40)
        $ the_person.change_arousal(15)
        "[the_person.title] keeps stroking you with her other hand, but it starting to get a little dry."
        "She brings her hand to her mouth, but her hair starts to get in the way."
        mc.name "Here, let me..."
        "You pull her hair behind the back of her head, keeping it away from her face."
        the_person "Thank you! What a gentleman..."
        "She chuckles, then spits another wad of saliva in her hand and starts to stroke you again."
        if masturbating_mommy:
            the_person "God this is getting me worked up too... honey do you mind if I... you know... touch myself a little?"
            mc.name "Of course."
            if the_person.vagina_visible:
                "Her free hand goes from her chest down between her legs."
                "You watch as she starts to play with her self as she strokes you."
            elif the_person.outfit.are_panties_visible:
                "Her free hand goes from her chest down into her panties."
                "You can see her hand start to move circles in her panties while she strokes you with the other."
            else:
                "Her free hand goes down and disappears beneath her clothes below her waist."
                "You can see movement as she starts to play with herself while she strokes you with her other hand."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(30)
        "It feels amazing to have [the_person.possessive_title]'s soft hands stroking your cock."
        $ mc.change_arousal(15)
        "She keeps stroking you for a while, and soon you need another round of saliva."
        $ the_person.draw_person(position = "blowjob")
        "This time, she leans forward a little bit, until your cock is just below her mouth."
        "You can feel her hot breath on your erection as she lets another round of saliva drip down from her mouth onto you."
        "Her mouth is just a couple inches from your cock, and your hand is in her hair... you wonder what she would do if you pulled her face a little closer..."
        menu:
            "Pull her closer":
                pass
            "Let her finish you":
                "You decide to just let her finish you with her hand. You can feel yourself getting close to orgasm anyway."
                $ mc.change_locked_clarity(30)
                $ mc.change_arousal(25)
                "With another round of saliva applied, she starts stroking you again."
                if masturbating_mommy:
                    "She looks at your cock and moans as she touches herself."
                    $ the_person.change_arousal(25)
                mc.name "Mmm that feels so good. If you can keep it up I'm going to cum soon."
                the_person "Yeah? You want to cum on your mommy's tits [the_person.mc_title]?"
                the_person "There's a reason I got them out for you..."
                mc.name "Oh fuck, I want to cover those big tits with my cum!"
                "[the_person.possessive_title!c] starts to stroke you faster, anticipating your orgasm."
                if masturbating_mommy:
                    "You can see her other hand pick up the pace too. She moans as she looks up at you, pleasuring herself at the same time."
                    $ the_person.change_arousal(25)
                $ mc.change_locked_clarity(30)
                $ mc.change_arousal(25)
                "You feel yourself getting ready to finish. You moan and call out to her."
                mc.name "Oh fuck [the_person.title] I'm gonna cum!"
                $ the_person.draw_person(position = "kneeling1")
                the_person "So do it! All over my tits [the_person.mc_title]!"
                "Just hearing her say that would have pushed you over the edge, but her soft, wet hand working your cock doesn't hurt either."
                $ climax_controller = ClimaxController(["Cum on her tits", "tits"])
                $ the_choice = climax_controller.show_climax_menu()
                $ the_person.cum_on_tits()
                $ the_person.draw_person(position = "kneeling1")
                "She aims your cock and strokes you to completion. You fire your load in thick ropes onto her large and ready tits."
                $ climax_controller.do_clarity_release(the_person)
                the_person "Oh my god, there's so much!"
                if masturbating_mommy:
                    "She looks up at you and you recognize the look in her face. She is getting ready to cum also."
                    $ the_person.change_arousal(25)
                    the_person "[the_person.mc_title]... I... Oh!!!"
                    $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 50, half_arousal = False, reset_arousal = False)
                    "You watch in awe as she start to orgasm. Her big tits wobble as her whole body shudders. Some of your cum drips off and onto the floor."
                    "She masturbates for several more seconds as her orgasm washes over her, and then finally subsides."
                "You look down at your cum covered mother."
                $ mc.change_locked_clarity(50)
                the_person "I think that makes us even for this week."
                mc.name "Yes I think so."
                $ masturbating_mommy = None
                return
        # Pull her closer. First check if she eagerly opens up and switches to blowjob mode.
        if the_person.is_willing(blowjob) and the_person.event_triggers_dict.get("oral_revisit_complete", False):
            "Feelin the pressure on the back of her head, she looks up at you, smiles, then opens her mouth."

        elif the_person.event_triggers_dict.get("oral_revisit_complete", False) and the_person.opinion.giving_blowjobs == -2:
            #She tries to refuse because she hates giving blowjobs
            "When she feels the pressure on the back of her head, [the_person.possessive_title] suddenly tenses up."
            the_person "Hey! That's not funny, I hate giving blowjobs."
            $ the_person.discover_opinion("giving blowjobs")
            mc.name "Really? When's that last time you gave one?"
            the_person "That hardly seems like information you need to know."
            mc.name "Sure, but what if you've changed since then? A lot of people change what they like or don't like over time."
            the_person "Honey... I know we agreed to this kind of thing, but I don't want to suck your cock..."
            mc.name "You didn't seem to mind much last time I ate you out. It only seems fair that you repay the favour once in a while?"
            "She sighs, but realises you aren't going to relent."
            if masturbating_mommy:
                "You see her bring her hand up from between her legs. Looks she isn't the mood to touch herself anymore..."
                $ masturbating_mommy = False
            $ the_person.change_arousal(-10)
            "She looks up at you, then opens her mouth. You gently start to pull her head closer to you again."
        elif the_person.event_triggers_dict.get("oral_revisit_complete", False): #She would normally refuse for some other reason.
            "When she feels the pressure on the back of her head, [the_person.possessive_title] stops and tenses up."
            the_person "Oh... I know we talked about doing that but... I don't think it would be right for me to do that..."
            mc.name "To do what?"
            the_person "You were... you know... in my mouth..."
            mc.name "[the_person.title], your drool is already all over my cock."
            mc.name "It would feel amazing if you just sucked on it a little. It's right there... don't you want a taste?"
            "She looks at your cock for a few moments, then looks up at you and nods."
            the_person "Okay... for the man of the house."
            "She looks up at you with a faint smile, then opens her mouth. You gently start to pull her head closer to you again."
        else:   #You haven't done the oral revisit yet.
            if the_person.event_triggers_dict.get("oral_revisit_count", 0) == 0:    #She's never sucked your cock before
                "When she feels the pressure on the back of her head, [the_person.possessive_title] suddenly tenses up."
                the_person "Hey! What are you doing?"
                mc.name "Your mouth is close [the_person.title]. I just want know what it would be like to have your lips on me..."
                "She stares at you in disbelief for a moment."
                the_person "You can't be serious... a mother can't suck on her own son's dick!"
                mc.name "A woman can choose to suck a man's dick if she wants to. Don't you want to know what it tastes like?"
                the_person "It isn't about what I want, it..."
                mc.name "But you do, don't you? And I want it too."
                mc.name "So let's stop worrying about what we should or shouldn't do. It's all bullshit anyways."
                "[the_person.possessive_title!c] looks up at you as she listens to you."
                mc.name "Let's just do what we want, and be the happiest mother and son on the whole planet."
                the_person "This... Really makes you happy?"
                mc.name "It does, more than I could ever explain."
                "She looks down at your erection and licks her lips, then looks back at up at you."
                the_person "It's been a long time, but I think I still remember how to suck my man off."
                "She obediently opens her mouth. You gently start to pull her head closer to you again."
            else:
                "When she feels the pressure on the back of her head, [the_person.possessive_title] stops and tenses up."
                the_person "Hey... we talked about this..."
                mc.name "I know, but everytime we start to fool around, I can't stop thinking about how good it is when we got a little further."
                mc.name "Please [the_person.title], I really need you to take care of me right now."
                "She shakes her head, in disbelief rather than refusal."
                the_person "Why am I even considering this? What kind of mother am I?"
                mc.name "The kind that really loves her son. It would make me so happy [the_person.title]."
                "You watch her resolve break down. Her eyes soften and she nods."
                the_person "I can't say no to you, that's the problem."
                mc.name "It isn't a problem, it is just a sign of how much we mean to each other."
                "She looks at your erection and licks her lips. Then she looks up at you, smiles, then opens her mouth. You gently start to pull her head closer to you again."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "[the_person.title] holds the base of your dick with her hand, and allows the gentle pressure on the back of her head to bring her mouth to the tip."
        "She runs a couple of cirles around the tip, tasting your pre-cum."
        "Then she takes it between her soft lips and starts to go down on you, taking about a third of your length into her warm, wet mouth."
        $ the_person.break_taboo("sucking_cock")
        mc.name "Oohhhh fuck that is nice..."
        if masturbating_mommy:
            "Although she paused earlier, she starts to masturbate again. She gives a deep moan that pleasingly vibrates all along your shaft."
            $ the_person.change_arousal(20)
        $ mc.change_arousal(15)
        $ mc.change_locked_clarity(50)
        "Still holding her hair, you moan as [the_person.title] starts to service you with her mouth, bobbing her head up and down."
        "You can feel her tongue run a circle around the tip once in a while when she backs off and then slide back down your underside when she goes down on it again."
        "Having already received considerable attention from her hand earlier, you know you won't last long in [the_person.possessive_title]'s wet mouth."
        if masturbating_mommy:
            "Especially with every muffled gasp and moan she gives around your shaft as she masturbates."
            $ the_person.change_arousal(20)
        $ mc.change_arousal(15)
        $ mc.change_locked_clarity(50)
        "The soft friction of her tongue running along the underside of your cock with each stroke is starting to feel a little TOO good."
        "You find yourself using your hand on the back of her head to speed her up a little bit. You moan when you feel her mouth bringing you to the edge of your orgasm."
        mc.name "Oh fuck, [the_person.title] I'm gonna cum!"
        if the_person.opinion.drinking_cum == -2:   #She panics.
            "Suddenly realizing you don't intend to let her off, [the_person.possessive_title]'s eyes go wide and she looks up at you."
            if masturbating_mommy:
                "In panic, she pulls her hand from between her legs and puts both hands on your hips, trying to push back away from you."
                $ masturbating_mommy = False
            else:
                "In panic, she uses her hands to try and push back away from you."
            "But you hold her head in place, the tip inside her lips as you begin to cum."
        elif the_person.opinion.drinking_cum >= 1:
            "[the_person.possessive_title!c] moans and eagerly slurps your cock a few more times."
            "She leaves the tip just inside her lips and strokes you with her hand as you begin to cum, ready to receive your load."
        else:
            "She leaves the tip just inside her lips and strokes you with her hand as you begin to cum, ready to receive your load."
        $ the_person.discover_opinion("drinking cum")
        $ climax_controller = ClimaxController(["Cum in her mouth","mouth"])
        $ the_choice = climax_controller.show_climax_menu()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", person = the_person)
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "blowjob")
        "You unload pulse after pulse of cum into [the_person.possessive_title]'s mouth. She does her best but some of it trickles down the sides of her mouth."
        "It feels amazing to unload into [the_person.title]'s mouth, but eventually your ejaculation ends. You let go of the back of her head."
        "Once you've finished she slides off and looks up at you."
        mc.name "That's it. Now be a good girl and swallow it all for me."
        $ play_swallow_sound()
        if the_person.opinion.drinking_cum <= -1:
            "[the_person.possessive_title!c] grimaces, but at this point she's committed. After a couple gulps, your load goes down her throat and into her stomach."
        elif the_person.opinion.drinking_cum == 2:
            "[the_person.possessive_title!c] happily slurps and gulps your cum down, loving the unique taste and texture of your semen."
        else:
            "[the_person.possessive_title!c] obediently gulps your cum down. She is committed to repaying you for your help with finances."
        if the_person.opinion.drinking_cum == -2 and the_person.opinion.giving_blowjobs == -2:  #She hated everything about that.
            the_person "Ugh... I can't believe I just did that. I HATE blowjobs... and especially swallowing cum!"
            mc.name "You did such a great job though, you're a natural."
            mc.name "Was it REALLY that bad? It felt so good for me."
            the_person "Well... I mean... I guess it wasn't horrible..."
            the_person "You taste better than the last man I gave a blowjob to, and I guess it is kind of nice to make you feel good."
            mc.name "I bet if you practice a bit you'd learn to like it."
            "She looks up at you and scowls."
            the_person "Look, I still don't LIKE it. But I guess if it makes you feel good it isn't that bad..."
            $ the_person.increase_opinion_score("giving blowjobs")
            $ the_person.increase_opinion_score("drinking cum")
        elif the_person.opinion.giving_blowjobs == -2:  #She hates blowjobs
            the_person "Ugh... I'm glad that's over..."
            mc.name "Wow. Was it really that bad?"
            "She looks up at you and opens her mouth to say something, but then stops. She seems to actually think about it."
            the_person "It... it was unpleasant."
            mc.name "Sure, you might find it a little distasteful, but it was kind of nice too, right?"
            the_person "I... It was kind of fun to hear you moan and to please you like that... in a weird kind of way."
            mc.name "I bet if you practice a bit you'd learn to like it."
            "She rolls her eyes and looks up at you."
            the_person "Look, I still don't LIKE it, but I guess it isn't as bad as I remembered, giving blowjobs like that."
            $ the_person.increase_opinion_score("giving blowjobs")
        elif the_person.opinion.drinking_cum == -2:     #She hates swallowing
            the_person "UGH. It feels weird, cum is so gross..."
            mc.name "It feels amazing when I finish in your mouth though. Is the taste and texture REALLY that bad?"
            "She looks up at you and opens her mouth to say something, but then stops. She seems to actually think about it."
            the_person "You know... I kind of panicked when I realised you were going to do that but... once it happened..."
            the_person "It was unpleasant, but swallowing your cum wasn't as bad as I remember."
            mc.name "I've heard it is a bit of an acquired taste. I bet if you practice, you might even learn to enjoy it."
            "She rolls her eyes and looks up at you."
            the_person "Look, I still don't LIKE it, but I guess it isn't as bad as I remembered, drinking cum like that."
            $ the_person.increase_opinion_score("drinking cum")
        elif masturbating_mommy:
            "When she finishes swallowing, she looks up at you with her eyes starting to glaze over."
            "You realise she is still masturbating and is getting ready to finish."
            $ the_person.change_arousal(30)
            mc.name "That's it. Cum for me [the_person.title]."
            the_person "Oh fuck... honey I... I'm...!!!"
            $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 50, half_arousal = False, reset_arousal = False)
            "You watch in awe as she start to orgasm. Her big tits wobble as her whole body shudders."
            "She masturbates for several more seconds as her orgasm washes over her, and then finally subsides."
        "[the_person.title] slowly gets off her knees and back into her chair."
        $ the_person.draw_person(position = "sitting")
        "You look down at your mother, some of your cum still dribbling down the sides of her mouth."
        $ mc.change_locked_clarity(50)
        the_person "I think that makes us even for this week."
        mc.name "Yes I think so."
        $ masturbating_mommy = None
    else:
        call fuck_person(the_person, start_position = handjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_jen_sat_morning_hj
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "You sigh, enjoying your post orgasm glow."
        the_person "I think that makes us even for this week."
        mc.name "Yes I think so."
    return

label mom_weekly_see_ass_label():
    $ the_person = mom
    mc.name "You could show me your ass? That would certainly be a nice way to repay a favour."
    # First, check and see if she has the taboo or we haven't finished the initial kissing taboo quest.
    if the_person.has_taboo("bare_pussy") or not mom.event_triggers_dict.get("kissing_revisit_complete", False) or the_person.effective_sluttiness("bare_pussy") < 30:
        if the_person.effective_sluttiness() > 30:  #She has no problem with it
            the_person "Oh! [the_person.mc_title], I had no idea you were even interested."
            the_person "Do you want me to just bend over my desk here?"
            mc.name "Umm yeah that would be great!"
            if the_person.vagina_visible and the_person.vagina_available:
                the_person "Okay! Look all you want! Here..."
                $ the_person.draw_person(position = "standing_doggy")

            else:
                "Without any further persuasion, she stands up and leans over her desk while pulling her bottoms down."
                $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = False)
                "When she finishes, you get a good look at [the_person.possessive_title]'s shapely ass."
            "You step around to the other side of the desk, getting closer for a good look."
            $ the_person.draw_person(position = "standing_doggy", display_transform = character_right_flipped(zoom = 1.2))

            "She turns head to look at you. She blushes a bit as you look lecherously at her backside."
            $ mc.change_locked_clarity(30)
            $ the_person.change_arousal(10)
            "She gives her ass a little wiggle, her feminine curves really turn you on. You feel yourself starting to get an erection."
        else:
            the_person "[the_person.mc_title]! You really shouldn't be asking something like that of your mother..."
            mc.name "Why not? It seems to me that if I'm going to be the man of the house, I should get SOME of the benefits that the head of household usually gets."
            the_person "Yes but... really? You want to me to flash my ass?"
            "You eagerly urge her."
            mc.name "Absolutely. Besides, it will help motivate me while I'm at work, thinking about what a beautiful woman I have back home to work for."
            the_person "Well... I suppose a little peek wouldn't hurt anything..."
            the_person "Just a peek though, okay?"
            mc.name "Of course. Just lean over your desk and let me have a good look."
            "She rolls her eyes, but obediently gets out of her chair and bends over her desk."
            $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = False)
            "When she finishes, you get a good look at [the_person.possessive_title]'s shapely ass."
            mc.name "Damn mom, your ass perfect. It looks soft and big and has curves in all the right places..."
            the_person "[the_person.mc_title]! Don't say things like that..."
            $ the_person.change_slut(2, 40)
            $ mc.change_locked_clarity(20)
            $ the_person.change_arousal(10)
        $ the_person.break_taboo("bare_pussy")
        mc.name "Thanks [the_person.title], I really appreciate that."
        $ the_person.draw_person(position = "sitting")
        "She sits back down at her desk."
        the_person "Alright that makes us even. Now get out of here so I can keep working!"
        return
    #If she doesn't have the taboo, check and see if she does it eagerly. If so, have a chance to spank/grope/finger her.
    else:
        the_person "Oh! Of course I'll do that for you. You've been so helpful lately."
        "Without any further persuasion, she stands up and leans over her desk."
        $ the_person.strip_to_vagina(position = "standing_doggy", prefer_half_off = False)
        "When she finishes, you get a good look at [the_person.possessive_title]'s shapely ass."
        mc.name "Damn mom, your ass perfect. It looks soft and big and has curves in all the right places..."
        the_person "Oh? You don't think I'm too old to show it off once in a while?"
        mc.name "Old? You're in your prime. Any man would be privileged to tap an ass like that."
        $ the_person.change_happiness(2)
        the_person "Ah thank you honey..."
        "You step around to the other side of the desk, eager to get closer for a good look."
        $ the_person.draw_person(position = "standing_doggy", display_transform = character_right_flipped(zoom = 1.2))
        "She turns head to look at you. She blushes a bit as you look lecherously at her backside."
        $ mc.change_locked_clarity(30)
        $ the_person.change_arousal(10)
        "She gives her ass a little wiggle, her feminine curves really turn you on. You feel yourself starting to get an erection."
        menu:
            "Spank her" if the_person.obedience >= 140:
                "You can't help it. Her ass is so close, you reach out give her ass cheek a solid spank."
                $ the_person.slap_ass()
                $ the_person.discover_opinion("being submissive")
                if the_person.opinion.being_submissive > 0:
                    $ play_moan_sound()
                    if the_person.can_be_spanked:
                        "[the_person.possessive_title!c] moans. Her ass wobbles pleasingly in waves, radiating out from your hand."
                        "You leave your hand on her ass and she pushes back against you a bit."
                        the_person "MMmm... I've been a bad girl this week [the_person.mc_title]."

                    else:
                        "[the_person.possessive_title!c] lets out a moan. Did she just enjoy that?"
                        "You leave your hand on her ass and feel her push back against you a bit."
                        the_person "[the_person.mc_title]... you can spank me again... if you want to..."
                        mc.name "Oh? Do you NEED to be spanked? Have you been a bad girl this week?"
                        "Suddenly realizing you are offering to roleplay, she responds enthusiastically."
                        the_person "Oh! Yes I've been bad. I've been a bad girl this week!"
                        $ the_person.unlock_spanking()
                    mc.name "Have you? I guess we should rectify that."
                    call fuck_person(the_person, start_position = spanking, position_locked = True) from _jen_sat_spanking_session_01
                    $ the_person.draw_person(position = "standing_doggy")
                    "[the_person.possessive_title!c] is left breathing hard, bent over her desk."
                    mc.name "Well, hopefully next week you can behave yourself. For now I'll consider us even."
                    the_person "Yes... I'll try to behave!.."
                    $ the_person.change_obedience(5)
                    return
                else: #She reacts obediently.
                    the_person "Ow! Hey... that hurt..."
                    mc.name "I'm sure it did, but a naughty girl like you needs to get a good spanking once in a while to keep her in line."
                    the_person "Hey, I'm not naughty, I'm..."
                    $ the_person.slap_ass()
                    "[the_person.possessive_title!c] goes silent in the middle of her protest."
                    mc.name "There we go. Are you ready for your spanking now?"
                    if the_person.opinion.being_submissive < 0:
                        the_person "NO. That hurts!"
                        "She clearly doesn't enjoy being submissive like this. Maybe you should work on training her to enjoy it."
                        "If you do, maybe she would be a little more open to submissive play in the future..."
                    the_person "A little bit is okay, but can you be a little softer?"
                    mc.name "Sure, in fact, I have a bit of an idea. Why don't we make you feel good too..."
                    "You slide your hand down her ass and in between her legs. She gasps when she feels a finger slide up and down her slit."
                    if the_person.opinion.being_fingered == -2: #She hates this too.
                        "She suddenly stands up."
                        $ the_person.draw_person(position = "back_peek")
                        the_person "Ah! No... No honey, I'm sorry."
                        $ the_person.draw_person(position = the_person.idle_pose)
                        the_person "I showed you my ass but this other stuff is just... not for me... okay?"
                        $ the_person.discover_opinion("being fingered")
                        the_person "I think that's enough for this week."
                        $ the_person.change_love(-3)
                        "You back away from [the_person.title]."
                        "Sounds like she just isn't submissive enough and refuses to let you finger her. Maybe you should traing her sexual attitudes a bit more before trying this again."
                        mc.name "Alright, I wasn't trying to make you uncomfortable."
                        # the_person "Thank you honey. I'm going to get back to the budget."
                        # mc.name "Sure thing mom."
                        # "You turn and leave her bedroom."
                        return
                    the_person "Ahhh... okay... I'm willing to see where this goes for now..."
                    $ the_person.change_arousal(10)
                    "You push your middle finger into [the_person.possessive_title]'s pussy and begin to finger her."
                    mc.name "There. That feels good, doesn't it?"
                    the_person "Yeah... I'm not sure how this is me repaying you for your budget contributions though..."
                    mc.name "Don't worry, I'm definitely enjoying it. Your ass is amazing [the_person.title]."
                    the_person "Mmm, thank you honey..."
                    $ the_person.change_arousal(20)
                    "You push your index finger inside of her also, and she is really enjoying it."
                    mc.name "Alright, I'm going to start easy okay? Just a tiny bit of pain to make the pleasure a little spicier."
                    the_person "Ah... okay..."
                    $ the_person.slap_ass(update_stats = False)
                    $ the_person.change_arousal(10)
                    "You give her ass a spank, just firm enough to sting a little, but not enough to cause any serious pain or skin markings."
                    the_person "AGH! Ahh..."
                    "You keep fingering her, and her body twitches a couple times in response."
                    mc.name "See? If you find the right balance, it can make the pleasure even better."
                    "With your free hand, you grope her ass cheeks a bit, then raise your hand up..."
                    $ the_person.slap_ass(update_stats = False)
                    $ the_person.change_arousal(15)
                    the_person "Oh! Aahhhhh...."
                    "You give [the_person.possessive_title]'s ass another light spank. She responds with a moan, and pushes her back against your hand as you start to grope her again."
                    the_person "Yes... that feels really good..."
                    $ the_person.slap_ass(update_stats = False)
                    $ the_person.change_arousal(15)
                    $ mc.change_locked_clarity(50)
                    $ play_moan_sound()
                    the_person "Oh! Oh [the_person.mc_title]..."
                    "Hearing her moan your name makes your cock twitch."
                    mc.name "Alright... let's try one more thing..."
                    "You pull your fingers out. Your index and middle fingers are coated in her arousal."
                    mc.name "Okay [the_person.title], try to relax as much as possible..."
                    the_person "Honey? What... Oh my god..."
                    "You put your index finger against her sphincter and your middle and ring fingers against her pussy and begin to push."
                    the_person "Ah! Okay I'm relaxing... AHH."
                    "With some persistent pressure, your fingers push inside of her, penetrating both her slutty holes."
                    $ the_person.change_arousal(15)
                    $ mc.change_locked_clarity(50)
                    if the_person.opinion.anal_sex < 0:
                        the_person "Ahhh I don't usually let anything in that hole... it's so dirty!"
                        mc.name "Non-sense. The anus is full of nerve endings, and with a careful partner it can be as pleasurable as vaginal penetration."
                        the_person "I... ahh... okay... just be careful, okay?"
                    elif the_person.opinion.anal_sex > 0:
                        the_person "Ooh! Yeah that feels amazing..."
                        "Hmmm, she seems to enjoy the feeling of your finger sliding into her ass..."
                    $ the_person.discover_opinion("anal sex")
                    "You give her several moments to get used to having fingers in both holes."
                    "When she seems to relax, you start to move your hand in and out of her."
                    $ the_person.change_arousal(15)
                    $ mc.change_locked_clarity(50)
                    "You grope her ass again with your free hand for several seconds, then slowly raise it up and..."
                    $ the_person.slap_ass(update_stats = False)
                    $ the_person.change_arousal(15)
                    $ mc.change_locked_clarity(50)
                    $ play_moan_sound()
                    the_person "OHMYGOD... Honey that... you're gonna make me cum!"
                    "[the_person.title] is pushing her ass back against your hand as you finger her. You put your free hand to good use."
                    $ the_person.slap_ass(update_stats = False)
                    $ the_person.slap_ass(update_stats = False)
                    $ the_person.slap_ass(update_stats = False)
                    $ play_moan_sound()
                    $ the_person.change_arousal(35)
                    $ mc.change_locked_clarity(50)
                    the_person "Ah! OHHH!"
                    $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 60, half_arousal = False, reset_arousal = False)
                    "[the_person.possessive_title!c]'s entire body quakes as she begins to orgasm."
                    "You pound her holes with your fingers and give her ass a several spanks as she cums."
                    "After several seconds, her orgasm begins to subside, and you stop pounding her with your fingers."
                    "You leave them inside of her for now though, and gently caress her ass with your free hand."
                    mc.name "See? Sometimes you just have to trust your partner with your body."
                    the_person "Yeah... yeah I see..."
                    $ the_person.increase_opinion_score(get_random_from_list(["anal sex", "being submissive"]), max_value = 2)
                    "You feel like you made your point. You slowly pull your fingers out of [the_person.title]..."
                    the_person "Ahh!... mmm..."
                    "You give her some space, and after a few moments, she sits back down into her office chair."
                    $ the_person.draw_person(position = "sitting")

            "Spank her {menu_red}Requires 140 Obedience{/menu_red} (disabled)" if the_person.obedience < 140:
                pass

            # "Grope her":
            #     "You reach down and run your hand along the soft curves of her backside."
            #     the_person "Mmm... you said you just wanted to see it?"

            "Compliment her":
                mc.name "Wow, your ass is amazing. I'm getting a hard on just looking at it."
                "She chuckles."
                the_person "Aww, thank you [the_person.mc_title]."
                "You spend a few more moments admiring her ass, then she sits back down into her office chair."
                $ the_person.draw_person(position = "sitting")

        the_person "Alright that's enough. Now get out of here so I can keep working!"
    return

label mom_weekly_blowjob_label():
    pass
    #FUTURECONTENT
    "If we are far along enough, we can skip the pre-tenses and go straight to a blowjob."
    return

label mom_weekly_sex_label():
    pass
    #FUTURECONTENT
    "If we are far along enough, we can skip the pre-tenses and go straight to having sex."
    return

label mom_weekly_glad_to_help_label():
    $ the_person = mom
    mc.name "Honestly, it's okay [the_person.title], I'm glad to help out."
    the_person "You are just the best [the_person.mc_title]."
    return
