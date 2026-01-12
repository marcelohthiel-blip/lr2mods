#Named events are for unique character specific overrides to generic labels.

label nora_bc_talk_label():
    $ the_person = nora
    if the_person.event_triggers_dict.get("had_bc_talk", False):
        the_person "I told you. I'm not doing birth control, and I'm not doing an IUD."
        mc.name "I see."
    else:
        $ the_person.event_triggers_dict["had_bc_talk"] = True
        the_person "Ah yes, birth control. I'm not on any."
        the_person "And before you ask, NO. I'm not going on it."
        the_person "The hormones don't work for me. They make me gain a bunch of weight and made me extremely moody."
        mc.name "Ah... what about something like an IUD?"
        "She sighs."
        the_person "I'm not doing that either. IT is a completely medically unnecessary."
        mc.name "But what about getting pregnant?"
        the_person "Condoms are something like 99%% reliable if used correctly. And I make sure they are used correctly."
        mc.name "But wouldn't you like to feel it bare sometimes?"
        the_person "No? It makes no difference to me. And besides, things tend to get so... messy."
        the_person "No. If a man wants to have sex with me, he'll wrap it up. It isn't fair to shift the burden of birth control on to me."
        mc.name "And if he doesn't?"
        the_person "Then he doesn't get to have sex with me."
        mc.name "I see..."
    $ the_person.update_birth_control_knowledge()
    return