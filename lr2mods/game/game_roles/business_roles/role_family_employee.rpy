#Use this role for a family member that works for MC as a method for splitting up work and home lives
#Mostly, we use this role to detect when and how taboos are broken, as well as separating home and work titles.

label add_role_family_employee_and_set_titles(the_person):
    mc.name "Why don't you call me something different while we are at work?"
    the_person "Oh? You want me to call you something different while we are working together?"
    mc.name "Yeah, it will give us a more professional working relation."
    the_person "Oh, okay... what did you have in mind?"
    menu:
        "Boss":
            $ add_family_employee_role(the_person, the_person.name, "Boss")
        "Sir":
            $ add_family_employee_role(the_person, the_person.name, "Sir")
        "Mr. [mc.last_name]":
            $ add_family_employee_role(the_person, the_person.name, f"Mr. {mc.last_name}")

    the_person "If you say so, [the_person.mc_title]."
    $ the_person.change_obedience(3)
    mc.name "And while we are at work, I'll just call you by name, [the_person.name]."
    the_person "Hmmm, I don't know..."
    mc.name "It's just for the office."
    the_person "Okay, I guess that works..."
    return
