

### Get to know labels ###

label stephanie_gtk_past_year_label(the_person = stephanie):
    mc.name "So, I've heard hints that it was a bit rough but, how was it at the lab after I left?"
    the_person "Ah geeze. Yeah things got tough."
    the_person "After you left, there was some drama because of some chemical inventory issues... which... really were your fault to begin with."
    the_person "We obviously didn't know that then, and [nora.fname] took the brunt of the investigation."
    mc.name "I'm sorry, I never meant for that to happen."
    the_person "I know. Anyway, after that, the Dean started breathing down our necks 24/7."
    the_person "He started having me and [nora.fname] work a bunch extra, but used some public university labor loophole to get out of paying overtime."
    the_person "The last few months especially, she was starting to act kind of weird..."
    mc.name "Weird how?"
    the_person "I don't know... I can't really describe it, but I got the feeling there was more going on between [nora.fname] and the Dean."
    the_person "I tried asking her a couple times, but was never able to find out."
    mc.name "Interesting."
    the_person "Anyway, I'm thankful that stage of my career is over. I miss working with her, but it's kind of nice to be out of that lab."
    $ the_person.change_love(1, 30)
    mc.name "And I'm glad to have you."
    return

label stephaine_gtk_tennis_label(the_person = stephanie):
    mc.name "So, how is your tennis league going?"
    the_person "Oh! It is going great."
    the_person "The league itself is fairly competitive, and even though I'm not the most athletic, I enjoy going."
    mc.name "It is good to work up a sweat once in a while."
    the_person "Definitely."
    the_person "You know, there are some people there who play mixed doubles... Maybe you could play with me sometime?"
    the_person "We'd make a great team!"
    mc.name "I'll keep that in mind."
    $ the_person.change_love(1, 30)
    return
