# This label is called the first time in game that MC's non consent preferene is used.
# This gives a quick rundown of the options and what they do to help players make their choice.
# Optionally, skip this if players already have a preference in place.

label non_consent_tutorial_label():
    if not mc.business.event_triggers_dict.get("Tutorial_Section", False):  #Only if we did the tutorial
        return
    if mc.business.event_triggers_dict.get("non_consent_tutorial_seen", False):
        return
    "Starbuck" "Hey everyone, Starbuck here. This next scene involves elements of players being on the receiving end of forceful or non consensual sexual acts."
    "Starbuck" "Because of the nature of this content, please select your preference for how you want this content to be handled."
    "Starbuck" "If Non Consent is set to Disabled, players will automatically force their way out of these situations, sometimes even turning the tables in the sexual encounter."
    "Starbuck" "If Non Consent is set to Roleplay, girls may ask permission first, or players may be given options to get out of these situations. However, the player will go along with the encounter and enjoy it."
    "Starbuck" "If Non Consent is set to Enabled, girls can force players into sexual encounters and actions against their will, however these scenes will always be written as if the Player Character enjoys it."
    "Starbuck" "There is no sexual horror or against their will rape in Lab Rats 2."
    "Starbuck" "Note: scenes may be different by how they play out, but this preference does not change overarching game stories, only the details of individual scenes!"
    "Starbuck" "If you change your mind later, you can always change this option in preferences!"
    $ mc.business.event_triggers_dict["non_consent_tutorial_seen"] = True
    "What do you want for your non consent setting?"
    menu:
        "Disabled":
            $ persistent.mc_noncon_pref = 0
        "Roleplay":
            $ persistent.mc_noncon_pref = 1
        "Enabled":
            $ persistent.mc_noncon_pref = 2
    return
