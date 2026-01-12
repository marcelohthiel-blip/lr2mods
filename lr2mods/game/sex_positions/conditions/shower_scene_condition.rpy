init -1 python:
    def condition_shower_scene_reward_req(self, the_person, report_log):
        if report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) > 0:   #You both finished
            return True
        return False


    def make_condition_shower_scene():
        shower_scene_condition = Condition_Type("Shower Scene",
            pre_label = "condition_shower_scene_pre_label",
            post_label = "condition_shower_scene_post_label",
            reward_cond = condition_shower_scene_reward_req,
            reward_label = "condition_shower_scene_reward_label")
        return shower_scene_condition

    shower_scene_flavor_text_generic_list = [
        "The hot water streaming from the shower leaves your bodies shining as you mess around.",
        "Messing around in the shower enhances the experience for both of you."
    ]

    shower_scene_flavor_text_vaginal_list = [
        "The hot water streaming from the shower enhances your sensations as you fuck her.",
        "Your bodies are making obscene slapping noises from the shower water as you fuck her."
    ]

    shower_scene_flavor_text_anal_list = [
        "The hot water streaming from the shower enhances your sensations as you fuck her ass.",
        "Your bodies are making obscene slapping noises from the shower water as you fuck her ass."

    ]


label condition_shower_scene_pre_label(the_person, the_position, the_object, report_log, the_condition):
    $ flavor_text = ""
    if the_position.skill_tag == "Vaginal":
        $ flavor_text = get_random_from_list(shower_scene_flavor_text_vaginal_list)
    elif the_position.skill_tag == "Anal":
        $ flavor_text = get_random_from_list(shower_scene_flavor_text_anal_list)
    else:
        $ flavor_text = get_random_from_list(shower_scene_flavor_text_generic_list)
    "[flavor_text]"
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(3)
    return

label condition_shower_scene_post_label(the_person, the_position, the_object, report_log, the_condition):
    pass
    return

label condition_shower_scene_reward_label(the_person, report_log, the_condition):
    $ the_person.change_stats(slut = 2, max_slut = 80, obedience = 3)
    "[the_person.possessive_title!c] really enjoyed fooling around in the shower."
    return