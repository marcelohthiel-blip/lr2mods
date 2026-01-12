# This set of labels replaces the normal pregnancy route.


label kaya_pregnant_announce(the_person):
    if the_person.has_child_with_mc:
        call pregnant_announce(the_person) from _call_pregnant_announce_kaya_pregnant_announce
        return

    $ the_person.draw_person()
    the_person "Hey! I need to talk to you. It can't wait."
    mc.name "Oh? What can I do for you?"
    the_person "More like what did you do TO me. I'm pregnant."
    $ mc.change_locked_clarity(100)
    "This isn't really much of a surprise. It is no secret that [the_person.title] was fine with the risks."
    the_person "Isn't that amazing??? I can't believe it!"
    mc.name "That is great. I'm so excited for you."
    the_person "I know! Mom says there is no way I can feel anything yet, but I swear I can feel it moving around!"
    the_person "Anyway, that's all. I just wanted you to know, daddy."
    return

label kaya_pregnant_tits_announce(start_day, the_person):
    if the_person.has_child_with_mc:
        call pregnant_tits_announce(start_day, the_person) from _call_pregnant_tits_announce_kaya_pregnant_tits_announce
        return

    $ the_person.draw_person()
    $ the_person.lactation_sources += 1 #She is milky goddess
    the_person "Hey! I have something I want to tell you. Have a minute?"
    mc.name "Of course."
    "She lowers her voice a bit."
    the_person "I'm not sure if you can tell or not... But my milk is starting to come in already!"
    the_person "I can barely even get my bras on now! I think I might have gone up a size or two."
    $ mc.change_locked_clarity(30)
    mc.name "That's great. I wouldn't mind a closer inspection, but they do appear to be a little bigger."
    the_person "Mmm, I wouldn't mind a closer inspection either..."
    if kaya.is_at(university_hub):
        the_person "Maybe I should get a study room later..."
    if kaya.is_at_office:
        the_person "Maybe I should stick around after normal business hours tonight..."
    else:
        the_person "Maybe you could swing by after the coffee shop closes down..."
    mc.name "I might do that."
    the_person "Anyway, it feels amazing to watch my body changing like this, getting ready to be a mommy!"
    the_person "Have a good day, I'll talk to you soon, daddy."
    mc.name "I'll catch you later."
    return

label kaya_pregnant_transform_announce(start_day, the_person):
    if the_person.has_child_with_mc:
        call pregnant_transform(the_person) from _call_pregnant_transform_kaya_pregnant_transform
        return

    $ the_person.draw_person()
    $ the_person.event_triggers_dict["milk_coffee"] = True
    $ the_person.lactation_sources += 1 #She is milky goddess
    the_person "Hey daddy. How are you?"
    mc.name "I'm doing well. And how are you and the baby doing?"
    the_person "Great, although I did have a surprise this past week."
    mc.name "Oh?"
    the_person "As you can see, I'm really starting to show, feels like I'm in the final stretch now."
    the_person "My milk has also come in... Like... A LOT"
    the_person "I showed my mom, and she got scared. She said it wasn't normal for me to be lactating so much before the baby comes."
    the_person "We made a quick trip to my gynaecologist, and she said some women are just blessed with ample milk production."
    "You look down at her chest. They definitely seem to have gotten bigger since last time you saw her."
    $ mc.change_locked_clarity(50)
    mc.name "Yeah, I would definitely have to say that you are blessed in the chest."
    "She chuckles."
    the_person "Why thank you daddy. The problem is, they seem to leak constantly now unless I relieve them often. And when I get aroused..."
    mc.name "Hmm... Maybe I should swing by the coffee shop this weekend, and order a coffee with a little extra cream."
    "She looks at you surprised for a moment but then smiles."
    the_person "I umm... I hadn't really thought about doing something like that, but for you?"
    the_person "I mean... You ARE the one who did this to me in the first place!"
    mc.name "That does sound nice. I'll try to swing by if I can."
    "You've heard of health benefits associated with consumption of breast milk. Plus, the thought of milking [the_person.possessive_title]'s generous udders is an arousing idea..."
    "You can now ask [the_person.title] for *extra cream* when you order coffee from her on the weekends, as long as her body is lactating enough to meet demand."
    return
