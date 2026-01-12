label stranger_hire_result(the_person): #Check to see if you want to hire someone.
    call hire_select_process([the_person, 1]) from _call_hire_select_process_stranger_hire_result
    if isinstance(_return, Person):
        call hire_someone(the_person) from _call_hire_someone_process_stranger_hire_result
        $ the_person.draw_person()
        return True
    else:
        $ the_person.draw_person()
        return False

    return False
