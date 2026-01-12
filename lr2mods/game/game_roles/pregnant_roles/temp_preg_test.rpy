# This file should not be in the final release.
# Us this label to test pregnancy role assignments as needed.

label test_basic_preg_roles():
    "Running pregnancy test on Lily and Jennifer"
    $ mom.change_baby_desire(100)
    $ lily.change_baby_desire(-100)
    $ mom.change_slut(100, 100)
    $ mom.change_love(100)
    $ lily.change_slut (-100, 5)
    $ lily.change_love(-100)
    $ become_pregnant(mom, mc_father = True, progress_days = 5)
    $ become_pregnant(lily, mc_father = True, progress_days = 5)
    "Test code complete"
    return

label test_kaya_preg_roles():
    "Running pregnancy test on Kaya"
    $ kaya.change_love(100)
    $ kaya.change_slut (100, 100)
    $ become_pregnant(kaya, mc_father = True, progress_days = 5)
    $ initialise_kaya_roaming()
    $ kaya_begin_class_schedule()
    $ kaya_begin_work_program_schedule()
    $ university.visible = True
    "Test code complete"
    "Note: this test breaks all of Kaya's other story content."
    return