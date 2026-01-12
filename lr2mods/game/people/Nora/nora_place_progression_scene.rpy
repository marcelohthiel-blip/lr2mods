

label nora_place_prog_scene_intro_scene(the_group):
    $ the_person = the_group[0]

    return

# Intro Scene
label nora_place_prog_scene_intro_0(the_group):
    $ the_person = the_group[0]
    mc.name "Hey, I was thinking about having some fun tonight. You interested?"
    the_person "[the_person.mc_title], lately, I'm ALWAYS interested."
    return

# Choice Scene
label nora_place_prog_scene_choice_label(the_group):
    $ the_person = the_group[0]
    $ nora_choice = 0
    if persistent.mc_noncon_pref == 2:  #Full sub themes. Nora decides on the action, not MC
        $ nora_choice = nora_place_prog_scene_choose_action()
        the_person "I know just what to do."
        the_person "Tell you what, why don't you make me some coffee while I slip into something more... exciting."
    else:
        the_person "Anything in particular you are in the mood for?"
        menu:
            "Oral Service" if 0 in nora_place_prog_scene.scene_unlock_list:
                $ nora_choice = 0
                mc.name "Why don't you sit on my face for a bit tonight?"
                the_person "Ah, can't get enough of my ass, can you? Alright."
            "Endurance Test" if (1 in nora_place_prog_scene.scene_unlock_list) and (nora.sex_record.get("Last Sex Day", 0) >= day - 7):
                mc.name "I want to test my endurance tonight."
                $ nora_choice = 1
                the_person "Hmm, I suppose you HAVE been doing well at keeping me satisfied lately..."
                the_person "Alright, let's see if you have what it takes to make the night last."
            "Endurance Test\n{menu_red}Too long since last sex session{/menu_red}(disabled)" if (1 in nora_place_prog_scene.scene_unlock_list) and (nora.sex_record.get("Last Sex Day", 0) < day - 7):
                pass
            "Cowgirl" if 2 in nora_place_prog_scene.scene_unlock_list:
                mc.name "Come here and put that talented mouth of yours to work."
                $ nora_choice = 2
            "Breeding Fetish Session" if 3 in nora_place_prog_scene.scene_unlock_list:
                mc.name "Come here and show me your horse riding skills."
                $ nora_choice = 3
            "Anal Fetish Session" if 4 in nora_place_prog_scene.scene_unlock_list:
                mc.name "I think I'll just take you here, on my desk."
                $ nora_choice = 4
            "Cum Fetish Session" if 5 in nora_place_prog_scene.scene_unlock_list:
                $ nora_choice = 5
            "Exhibitionist Session" if 6 in nora_place_prog_scene.scene_unlock_list:
                $ nora_choice = 6
        the_person "Alright. Why don't you make me some coffee while I slip into something more... exiciting."
    mc.name "Of course, [the_person.title]."
    $ clear_scene()
    "You head to her kitchen and put on a pot of coffee."
    "When it is done, you pour two cups. You look at [the_person.title]'s cup for a moment..."
    call give_serum(the_person) from _call_give_nora_her_prog_01
    "You mix the serum into [the_person.title]'s coffee and take it to the bedroom."
    "You sit down on the side of the bed and wait for her."
    if the_person.wardrobe.get_outfit_with_name("Nora Lingerie"):
        $ the_person.apply_outfit(the_person.wardrobe.get_outfit_with_name("Nora Lingerie"))
    else:
        $ the_person.apply_outfit(lingerie_wardrobe.pick_random_outfit(), update_taboo = True)
    "A minute later, she appears in her bedroom door."
    $ the_person.draw_person()
    the_person "Alright, ready to get started?"
    mc.name "Absolutely."
    "She walks up to you and takes her coffe from your hand and takes a sip."
    "She sets the coffe down and get's ready to begin."

    return nora_choice

#Exit scene. Nora might even get mad since he brought it up?
label nora_place_prog_scene_exit_scene(the_group):
    pass
    return

#######################
#  Transition Scenes  #
#######################

label nora_place_prog_trans_scene_0(the_group):
    pass
    "This scene should never show. If you are seeing this, something went wrong."
    return

label nora_place_prog_trans_scene_1(the_group):
    $ the_person = the_group[0]
    "In this scene, [the_person.possessive_title] decides to reward MC for taking care of her needs."

    return

label nora_place_prog_trans_scene_2(the_group):
    $ the_person = the_group[0]
    "In this scene, [the_person.possessive_title] mostly skips foreplay in favor of riding him cowgirl."
    return

label nora_place_prog_trans_scene_3(the_group):
    $ the_person = the_group[0]
    "In this scene, [the_person.possessive_title] rides MC to a creampie to fulfill her breeding fetish."
    return

label nora_place_prog_trans_scene_4(the_group):
    $ the_person = the_group[0]
    "In this scene, [the_person.possessive_title] rides MC anally to fulfill her anal fetish."
    return

label nora_place_prog_trans_scene_5(the_group):
    $ the_person = the_group[0]
    "In this scene, [the_person.possessive_title] tries to make MC cum multiple times to fulfill her cum fetish."
    return

label nora_place_prog_trans_scene_6(the_group):
    $ the_person = the_group[0]
    "In this scene, [the_person.possessive_title] ties up MC and livestreams a sex session for her exhibitionism fetish?."
    return


######################
#     End Scenes     #
######################


label nora_place_prog_scene_scene_0(the_group, scene_transition = False):
    pass
    return

label nora_place_prog_scene_scene_1(the_group, scene_transition = False):
    pass
    return

label nora_place_prog_scene_scene_2(the_group, scene_transition = False):
    pass
    return

label nora_place_prog_scene_scene_3(the_group, scene_transition = False):
    pass
    return

label nora_place_prog_scene_scene_4(the_group, scene_transition = False):
    pass
    return

label nora_place_prog_scene_scene_5(the_group, scene_transition = False):
    pass
    return

label nora_place_prog_scene_scene_6(the_group, scene_transition = False):
    pass
    return
