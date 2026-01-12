#Counter = KEA01

#Non event content stuff

init 5 python:
    config.label_overrides["aunt_sex_accept"] = "aunt_sex_accept_revamp"

label aunt_sex_accept_revamp(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            $ random_reply = get_random_from_list(["This is our little secret, okay?", "No one can know, especially Jennifer, okay?", "I can't believe I'm doing this!"])
            the_person "[random_reply]"  
        else:
            if the_position.skill_tag == "Foreplay":
                if "giving tit fucks" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Aunty's titty fuck? You're such a pervert.", "I called these 'Hope n Dreams'", "Oh my, these juggers?", "Aunt Hooters, coming up!"])
                elif "kissing" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Kissing your own aunt, " + the_person.mc_title + ", you're such a pervert.", "Come kiss your aunty!", "I'm yours.", "Lemme teach you how to french kiss."])
                else:
                    $ random_reply = get_random_from_list(["Touch me... everywhere...", "Such a gentleman.", "Ohh..", "Hmmmm..."])
                the_person "[random_reply]"
            elif the_position.skill_tag == "Oral":
                if "getting head" in the_position.opinion_tags:
                    $ random_reply = get_random_from_list(["Oh yes, come here and take care of " + the_person.possessive_title + ".", "Oh YES!!!.", "Oh my, such a gentleman.", "Perfect gentleman."])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["Come here, let aunty take care of your big boy.", "Stay still, lemme take care of this big boy.", "What a naughty dick you have, I need to discipline it!"])
                    the_person "[random_reply]"
            else:
                $ random_reply = get_random_from_list(["Oh yes baby, fuck your aunty's brains out.", "What a naughty dick you have, lemme tame it!", "Go to town on your aunt!", "Hmmmm... YES!", "Pound me HARD!!", "Aunt gonna squeeze you dry~ {i}ufufu~{/i}"])
                the_person "[random_reply]"
    else:
        if the_person.love < 40:
            the_person "Okay, lets try it. Just don't tell Jennifer."
        else:
            if the_position.skill_tag == "Foreplay":
                $ random_reply = get_random_from_list(["Okay, lets play a little with each other.", "Mmmm, kiss me baby.", "Fooling around with aunty? I'm game.", "Oh yes, come here and kiss me!", "I'm yours."])
                the_person "[random_reply]"
            elif the_position.skill_tag == "Oral":
                $ random_reply = get_random_from_list(["Going down on each other? Sign me up.", "Come play with " + the_person.title + ".", "Oh yes, lets pleasure each other.", "I'm yours."])
                the_person "[random_reply]"
            else:
                if the_person.has_taboo(["vaginal_sex", "anal_sex"]):
                    $ random_reply = get_random_from_list(["Oh my, I don't know why I let you talk me into this.", "Promise me. Just this once, okay?"])
                    the_person "[random_reply]"
                else:
                    $ random_reply = get_random_from_list(["I don't mind giving it another try.", "Oh my, I don't know why I let you talk me into this.", "Okay, lets try it. Just don't tell Jennifer."])
                    the_person "[random_reply]"
    return