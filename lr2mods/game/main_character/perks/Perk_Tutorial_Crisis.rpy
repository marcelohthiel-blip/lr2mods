init -1 python:
    def Perk_Tutorial_Crisis_requirement():
        if mc.is_in_bed and day >= 4: # The first friday night
            return True
        return False

    def time_of_need_func():
        mc.change_energy(mc.max_energy * 0.3)
        return

label Perk_Tutorial_Crisis_label():
    $ the_person = mom
    $ outfit = Outfit("Lingerie Set Blue Nightgown")
    $ outfit.add_upper(nightgown_dress.get_copy(), colour_sky_blue)
    $ outfit.add_lower(cute_panties.get_copy(), colour_sky_blue)
    $ the_person.apply_outfit(outfit)
    $ mc.change_location(bedroom)
    $ mc.business.event_triggers_dict["perk_tutorial"] = 1
    $ mc.energy = 5
    "You are worn out after a long hard day. You collapse into your bed and are rapidly falling asleep when a knock on your door awakens you."
    mc.name "Wha? Come in?"
    $ the_person.apply_outfit(outfit)
    $ the_person.draw_person()
    the_person "Hey honey... I'm sorry to bug you, but I was wondering if you could come help with something really quick!"
    mc.name "Seriously? Right now?"
    the_person "I'm sorry, I know you're tired, but it'll just be a moment I promise!"
    $ the_person.draw_person(position = "walking_away")
    "You aren't sure you can get up. You try to dig deep so you can help [the_person.title] in her time of need."
    "However, something about the way she is asking you stirs you up. Is she wearing a sheer nightgown?"
    "You have this weird feeling that things may take a sexual turn."
    $ perk_system.add_ability_perk(Ability_Perk(description = "You dig deep and summon reserves of energy to meet the needs of others. Recovers 30% energy, usable once per week. Used automatically sometimes.", active = False, usable = True, usable_func = time_of_need_func, usable_cd = 7), "Time of Need")
    "You have gained the Perk: Time of Need!"
    while mc.energy < 20:
        "Open the 'Perk Sheet' screen (top left UI) and click on the 'Time of Need' perk to continue."
    $ mc.change_location(mom_bedroom)
    $ the_person.draw_person()
    "You get up and follow [the_person.possessive_title] down the hall and into her room."
    the_person "Thank you! I just had this overwhelming urge to move some furniture around. You know how it is, once you get the urge it's hard to put it off..."
    "You start to help [the_person.possessive_title] move her furniture around."
    $ the_person.draw_person(position = "standing_doggy")
    "You just finished moving a night stand, when you see her setting down something on the floor."
    "You take a candid moment to enjoy the way her backside looks in her outfit..."
    $ mc.change_locked_clarity(15)
    $ the_person.outfit.remove_clothing(nightgown_dress)
    $ the_person.draw_person(position = "doggy")
    "Suddenly, she slips on something and lands on all fours."
    the_person "Wha... Ow!"
    "Her nightgown somehow flips up in the back, giving you a clear view of her panties!"
    $ mc.change_locked_clarity(30)
    "You make sure to take a picture in your brain of the glorious sight."
    $ the_person.apply_outfit(outfit)
    $ the_person.draw_person()
    "She quickly stands up and smooths out her clothes. You look away, pretending not to notice."
    $ the_person.change_slut(1, 30)
    "You aren't sure if she bought it or not... but you continue to move furniture around anyway."
    "Soon you have the room setup just the way she wants it."
    $ the_person.draw_person(emotion = "happy")
    $ the_person.change_stats(happiness = 5, love = 3)
    the_person "Thank you! This means a lot to me!"
    $ mc.change_location(bedroom)
    $ clear_scene()
    "You say goodnight and then head back to bed."
    "As you lay in bed, you think about the encounter you just had."
    "That burst of energy was certainly useful. You wonder if you are starting to get a sense of when special encounters are occurring."
    return

label perk_time_of_need_story_label():
    if mc.energy < 80:
        "Something about the situation has your senses tingling. Somehow, you can tell it is going to take an interesting sexual twist."
        $ time_of_need_func()
        "You get a burst of energy from your Time of Need perk!"
    return
