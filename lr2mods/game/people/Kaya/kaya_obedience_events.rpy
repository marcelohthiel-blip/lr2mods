#Kaya's obedience route centres on corrupting her as she works with Nora and at the coffee shop.
#At first, we begin to pilfer some of the research that Nora is working on.
#Then, if we are working on Nora's research, we convince her to let us concoct a serum for study and to test it on her during her residency days.
#After that, we convince her to help come up with a new flavoured serum to be sold at the coffee shop
#At 180, if we haven't already convinced her to be MC's breeding stock, we unlock this ability.
#Obedience is Kaya's unfavoured arc, so each step should have some sort of limit break mechanic.
#However, if we have cured Sakari, we have the option to completely bypass all limit breaks for her.

#120 Obedience
label kaya_nora_research_pilfer_intro_label(the_person):

    $ kaya.progress.obedience_step = 1
    pass
    return

label kaya_nora_research_pilfer_recap_label(the_person):
    pass


    $ kaya.progress.obedience_step = 2
    return

label kaya_nora_research_pilfer_retry_label(the_person):

    pass
    return


#140 Obedience
label kaya_nora_serum_test_intro_label(the_person):



    $ kaya.progress.obedience_step = 3
    pass
    return

label kaya_nora_serum_test_recap_label(the_person):
    pass


    $ kaya.progress.obedience_step = 4
    return

label kaya_nora_serum_test_retry_label(the_person):

    pass
    return

# 160 obedience
label kaya_coffeeshop_flavor_shortage_label(the_person):

    pass


    $ kaya.progress.obedience_step = 5
    return

label kaya_coffeeshop_flavor_proposal_label(the_person):
    pass
    return

label kaya_coffeeshop_flavor_development_intro_label(the_person):
    pass
    return

label kaya_coffeeshop_flavor_development_final_label(the_person):
    pass
    return

label kaya_coffeeshop_flavor_final_label(the_person):
    pass


    $ kaya.progress.obedience_step = 6
    return


# 180 obedience
label kaya_trade_sexual_favors_intro(the_person):
    pass


    $ kaya.progress.obedience_step = 7
    return

label kaya_trade_sexual_favors_recap(the_person):
    pass


    $ kaya.progress.obedience_step = 8
    return

label kaya_trade_sexual_favors_retry(the_person):
    pass
    return
