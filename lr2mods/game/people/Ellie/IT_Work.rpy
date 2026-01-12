init 6 python:
    def IT_work_requirement():
        if not mc.business.current_IT_project:
            return "No active project!"
        return True

    IT_work_action = Action("Work on IT development", IT_work_requirement, "IT_work_label")

label IT_work_label():
    "You spend some time working on the current IT Project."
    $ mc.business.IT_increase_project_progress(25, add_to_log = True)
    return
