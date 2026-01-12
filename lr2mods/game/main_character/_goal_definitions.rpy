label instantiate_goals():
    python:
        stat_goals = []
        work_goals = []
        sex_goals = []

        init_goal_lists()
        # set initial goals for MC
        mc.generate_goals()

    return
