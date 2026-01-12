label iris_schedule_backup_label():
    #Use this label in an event that triggers if we haven't met Iris but have progressed through both story options.
    if not mc.phone.has_number(iris):
        $ iris_init_schedule()
    return