# Alter wardrobe functions original by Kaden

label modify_wardrobe_label(the_person):
    call screen main_choice_display(build_menu_items(build_modify_wardrobe_menu()))
    $ strip_choice = _return
    $ alterations = 0
    if strip_choice == "back":
        return
    elif strip_choice == 'base':
        mc.name "Let's take a look at the accessories you are always wearing."
        the_person "Alright, it shouldn't be too hard to update my jewellery collection."
        call screen outfit_creator(the_person.base_outfit, outfit_type = "full", slut_limit = None, start_mannequin = the_person)
        if isinstance(_return, Outfit):
            $ the_person.change_obedience(1)
            $ the_person.base_outfit = _return
        $ clear_scene()
    elif strip_choice == "no_pants":
        mc.name "I want you to stop wearing pants."
        if the_person.opinion.skirts < the_person.opinion.pants:
            the_person "I'm not really a fan of skirts."
            if the_person.sluttiness > 40 or the_person.obedience > 140 or the_person.love > 40:
                mc.name "Don't worry [the_person.title] I am, and isn't that what really matters?"
                the_person "I guess you're right. I'll make the switch as soon as I can."
                $ alterations += no_pants(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.opinion.skirts > the_person.opinion.pants:
            the_person "Ok."
            $ alterations += no_pants(the_person)
        else:
            the_person "Oh, that sounds exciting. Free and open access for people like you to take advantage of me."
            $ alterations += no_pants(the_person)
        $ the_person.discover_opinion("pants")
        $ the_person.discover_opinion("skirts")
    elif strip_choice == "no_dresses":
        mc.name "I want you to stop wearing dresses."
        if the_person.opinion.skirts < the_person.opinion.dresses:
            the_person "I really prefer them to skirts."
            if the_person.sluttiness > 40 or the_person.obedience > 140 or the_person.love > 40:
                mc.name "Don't worry [the_person.title] I prefer skirts, and isn't that what really matters?"
                the_person "I guess you're right. I'll make the switch as soon as I can."
                $ alterations += no_dresses(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.opinion.skirts > the_person.opinion.dresses:
            the_person "Ok."
            $ alterations += no_dresses(the_person)
        else:
            the_person "Oh, that sounds exciting. It will give me a chance to show off more of my body from time to time."
            $ alterations += no_dresses(the_person)
        $ the_person.discover_opinion("dresses")
        $ the_person.discover_opinion("skirts")
    elif strip_choice == "lingerie_removal":
        mc.name "I want you to stop wearing lingerie."
        if the_person.opinion.not_wearing_underwear < 0:
            the_person "I'm not sure I'm comfortable with not wearing underwear."
            mc.name "Sorry, that isn't what I meant, just don't wear the full body lingerie. You can still wear bras and panties."
            the_person "Ok, I'll see if there is anything I need to change."
        elif the_person.opinion.not_wearing_underwear >= 1:
            the_person "Oh, that sounds exciting. I'll stop wearing underwear altogether."
            mc.name "Oh, actually..."
            menu:
                "Just no full body lingerie":
                    mc.name "Sorry, that isn't what I meant, just don't wear the full body lingerie. You can still wear bras and panties."
                "No bras":
                    mc.name "Actually, just get rid of bras, you can keep wearing panties."
                    $ alterations += bra_removal(the_person)
                "No panties":
                    mc.name "Actually, just get rid of panties, you can keep wearing bras."
                    $ alterations += panty_removal(the_person)
                "No underwear":
                    mc.name "That sounds even better, thanks, [the_person.title]."
                    $ alterations += bra_removal(the_person)
                    $ alterations += panty_removal(the_person)
        else:
            the_person "Ok."
        $ alterations += lingerie_removal(the_person)
        $ the_person.discover_opinion("lingerie")
    elif strip_choice == "no_bras":
        mc.name "I want you to stop wearing bras."
        if the_person.opinion.not_wearing_underwear < 0:
            the_person "I'm not sure I'm comfortable with that."
            if the_person.sluttiness > 50 or the_person.obedience > 150 or the_person.love > 50:
                mc.name "Don't worry [the_person.title] I'm comfortable with it, and isn't that what really matters?"
                the_person "I guess you're right. I'll remove them from my wardrobe as soon as I can."
                $ alterations += bra_removal(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.opinion.not_wearing_underwear == 0:
            the_person "Ok."
            $ alterations += bra_removal(the_person)
        else:
            if the_person.has_large_tits:
                the_person "Oh, that sounds exciting, but my tits are so big."
                mc.name "That's exactly why you should do it. Just imagine them swinging around all day for everyone to see."
                the_person "That does sound pretty hot. But these girls need some support, I will figure it out."
            elif the_person.tits in ("A", "AA"):
                the_person "That shouldn't be a problem. I've never had much to hold in them anyway."
                mc.name "Exactly, and this way I'll be able to grab a little handful whenever I want."
                the_person "I like the thought of that. I'll do it as soon as I can."
            else:
                the_person "Ok."
            $ alterations += bra_removal(the_person)
        if not mc.business.topless_is_legal:
            the_person "But I won't walk around town flashing my tits to everyone."
        $ the_person.discover_opinion("not wearing underwear")
    elif strip_choice == "no_panties":
        mc.name "I want you to stop wearing panties."
        if the_person.opinion.not_wearing_underwear < 0:
            the_person "I'm not sure I'm comfortable with that."
            if the_person.sluttiness > 60 or the_person.obedience > 160 or the_person.love > 60:
                mc.name "Don't worry [the_person.title] I'm comfortable with it, and isn't that what really matters?"
                the_person "I guess you're right. I'll remove them from my wardrobe as soon as I can."
                $ alterations += panty_removal(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.opinion.not_wearing_underwear == 0:
            the_person "Ok."
            $ alterations += panty_removal(the_person)
        else:
            the_person "Oh, that sounds exciting."
            $ alterations += panty_removal(the_person)
        if not mc.business.nudity_is_legal:
            the_person "But I don't want to walk around with my cooch visible to anyone."
        $ the_person.discover_opinion("not wearing underwear")
    elif strip_choice == "shorter_skirts":
        mc.name "I want you to wear shorter skirts."
        if the_person.opinion.skimpy_outfits > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.opinion.skimpy_outfits == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += shorter_skirts(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "shorter_pants":
        mc.name "I want you to wear shorter pants."
        if the_person.opinion.skimpy_outfits > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.opinion.skimpy_outfits == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += shorter_pants(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "sexier_dresses":
        mc.name "I want you to wear sexier dresses."
        if the_person.opinion.skimpy_outfits > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.opinion.skimpy_outfits == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += smaller_dresses(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "sexier_shirts":
        mc.name "I want you to wear sexier shirts."
        if the_person.opinion.skimpy_outfits > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.opinion.skimpy_outfits == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += smaller_shirts(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "sexier_bras":
        mc.name "I want you to wear sexier bras."
        if the_person.opinion.not_wearing_underwear == 2:
            the_person "That is something I could probably do, but why don't I just stop wearing them altogether?"
            $ the_person.discover_opinion("not wearing underwear")
            menu:
                "Yes":
                    mc.name "That would be even better. Go ahead and remove them from your wardrobe entirely."
                    the_person "Yes, [the_person.mc_title]."
                    $ alterations += sexier_bras(the_person)
                "No":
                    mc.name "No, I like you wearing them, I just want them to be skimpy and sexy."
                    the_person "I'll take a look and see what I can do for you."
        else:
            if the_person.opinion.lingerie > 0:
                the_person "Well I do like having something sexy to show off when I take off my clothes."
            elif the_person.opinion.lingerie == 0:
                the_person "Ok."
            else:
                the_person "Underwear is underwear, does it really matter what it looks like?"
                mc.name "It does for me, I love seeing your body highlighted by sexy clothes."
                the_person "Alright, I'll take a look through my wardrobe."
        $ the_person.discover_opinion("lingerie")
        $ alterations += sexier_bras(the_person)
    elif strip_choice == "sexier_panties":
        mc.name "I want you to wear sexier panties."
        if the_person.opinion.not_wearing_underwear >= 2:
            the_person "That is something I could probably do, but why don't I just stop wearing them altogether?"
            $ the_person.discover_opinion("not wearing underwear")
            menu:
                "Yes":
                    mc.name "That would be even better. Go ahead and remove them from your wardrobe entirely."
                    the_person "Yes, [the_person.mc_title]."
                    $ alterations += sexier_panties(the_person)
                "No":
                    mc.name "No, I like you wearing them, I just want them to be skimpy and sexy."
                    the_person "I'll take a look and see what I can do for you."
        else:
            if the_person.opinion.lingerie > 0:
                the_person "Well I do like having something sexy to show off when I take off my clothes."
            elif the_person.opinion.lingerie == 0:
                the_person "Ok."
            else:
                the_person "Underwear is underwear, does it really matter what it looks like?"
                mc.name "It does for me, I love seeing your body highlighted by sexy clothes."
                the_person "Alright, I'll take a look through my wardrobe."
        $ the_person.discover_opinion("lingerie")
        $ alterations += sexier_panties(the_person)
    elif strip_choice == "sexier_socks":
        mc.name "I want you to wear sexier socks."
        if the_person.opinion.lingerie > 0:
            the_person "Oh, that sounds fun. I'm always looking for more ways to attract attention."
            mc.name "Exactly, and if you do you'll get more attention from me."
            the_person "I'll take a look and see what I can change for you."
        elif the_person.opinion.lingerie == 0:
            the_person "What do you mean sexier socks? How are socks sexy?"
            mc.name "You know, things like thigh highs. Socks that you wear for people to see."
            the_person "Oh, I've never really gotten the appeal, but I guess I can give it a try."
        else:
            the_person "I'm not really a fan of advertising my sexuality."
            mc.name "Don't think of it as that, it is about highlighting your best features. Don't you think you are beautiful enough to show off?"
            the_person "I suppose I can take a look at my wardrobe for you."
        $ alterations += sexier_socks(the_person)
        $ the_person.discover_opinion("lingerie")
    elif strip_choice == "sexier_shoes":
        mc.name "I want you to wear sexier shoes."
        if the_person.opinion.high_heels > 0:
            the_person "Oh, that sounds fun. I'm always looking for more ways to attract attention."
            mc.name "Exactly, and if you do you'll get more attention from me."
            the_person "I'll take a look and see what I can change for you."
        elif the_person.opinion.high_heels == 0:
            the_person "What do you mean sexier shoes? How are shoes sexy?"
            mc.name "You know, things like high heels. Shoes that you wear for people to see."
            the_person "Oh, I've never really gotten the appeal, but I guess I can give it a try."
        else:
            the_person "I'm not really a fan of advertising my sexuality."
            mc.name "Don't think of it as that, it is about highlighting your best features. Don't you think you are beautiful enough to show off?"
            the_person "I suppose I can take a look at my wardrobe for you."
        $ alterations += sexier_shoes(the_person)
        $ the_person.discover_opinion("high heels")
    elif strip_choice == "translucent":
        mc.name "I like the clothes you are wearing, I just wish they didn't obstruct so much of my view of you."
        the_person "That's sweet, but it isn't like I can just make my clothes more see-through for you."
        mc.name "Sure you can, I have this compound that does just that." #whole quest chain in development: chemical spill > research > work laundry policies > serum trait > home laundry tampering
        the_person "Well in that case..."
        the_person "What parts of my clothes do you want me to change?"
        $ fade_over = False
        $ fade_under = False
        $ fade_number = .98
        menu:
            "Just overwear":
                $ fade_over = True
                mc.name "I think just the top layers of your clothes. I like being able to see your underwear showing through."
                if the_person.opinion.skimpy_outfits > 0:
                    the_person "I do like showing off."
            "Just underwear" if not the_person.has_taboo("underwear_nudity"):
                $ fade_under = True
                mc.name "I think just your underwear. I really like the look of sheer lingerie once I get your clothes off."
                if the_person.opinion.showing_her_tits > 0 or the_person.opinion.showing_her_ass > 0:
                    the_person "Fortunately I like showing off my assets."
            "Everything" if not the_person.has_taboo("underwear_nudity"):
                $ fade_over = True
                $ fade_under = True
                mc.name "I think everything you wear should be see-through."
                if the_person.opinion.showing_her_tits > 0 or the_person.opinion.showing_her_ass > 0:
                    the_person "I like the way you think, no wonder we get along so well."
        the_person "Now I just need to know how far I should take this."
        menu:
            "95":
                $ fade_number = 0.95
                mc.name "Let's start small."
            "90" if the_person.sluttiness > 20:
                $ fade_number = 0.90
                mc.name "Fade them a bit, but not too much."
            "80" if the_person.sluttiness > 40:
                $ fade_number = 0.80
                mc.name "I want to be able to see through them."
            "75" if the_person.sluttiness > 60:
                $ fade_number = 0.75
                mc.name "Take it down a quarter."
            "66" if the_person.sluttiness > 70:
                $ fade_number = 0.66
                mc.name "Go pretty far, I want to know what is under everything."
            "50" if the_person.sluttiness > 80:
                $ fade_number = 0.50
                mc.name "Go extreme, let me see everything under them."
            "33" if the_person.sluttiness > 90:
                $ fade_number = 0.33
                mc.name "I should barely be able to tell you are wearing anything."
        the_person "Alright, I should be able to do that."
        $ alterations += translucent(the_person, fade_number, fade_over, fade_under)
    elif strip_choice == "add_makeup":
        menu:
            "Respect opinion":
                $ make_up_score_boost = 0
            "Ignore opinion":
                $ make_up_score_boost = 4
        $ alterations += add_makeup(the_person, make_up_score_boost = make_up_score_boost)
        $ del make_up_score_boost
    elif strip_choice == "sexier_clothes":
        mc.name "I want you to wear sexier clothes."
        the_person "What do you mean?"
        mc.name "Show some skin, shorter skirts and pants, smaller shirts and dresses, sexier underwear. Just go crazy."
        the_person "I guess I can take a look at what I would be comfortable changing about my wardrobe."
        $ alterations += lingerie_removal(the_person)
        $ alterations += shorter_skirts(the_person)
        $ alterations += shorter_pants(the_person)
        $ alterations += smaller_shirts(the_person)
        $ alterations += smaller_dresses(the_person)
        $ alterations += sexier_panties(the_person)
        $ alterations += sexier_bras(the_person)
        $ alterations += sexier_socks(the_person)
        $ the_person.discover_opinion("skimpy outfits")
        $ the_person.discover_opinion("lingerie")

    $ test_outfit = the_person.planned_outfit
    if the_person.wardrobe.has_outfit_with_name(test_outfit.name):
        $ the_person.apply_outfit(the_person.wardrobe.get_outfit_with_name(test_outfit.name))
    $ test_outfit = None

    if alterations > 10:
        the_person "Wow, I had to make [alterations] changes to my wardrobe for you."
        mc.name "That is a lot. I really appreciate it, [the_person.title]."
        if the_person.opinion.not_wearing_anything == 2:
            the_person "At this rate I'll be not wearing anything at all before too long. Won't that be exciting?"
            mc.name "You know, we could see about trying that out now if you want."
            the_person "What did you have in mind?"
            call demand_strip_label(the_person) from call_demand_strip_label_wardrobe
    elif alterations > 5:
        the_person "That wasn't too bad, I only had to make [alterations] changes to my wardrobe."
        mc.name "Thank you [the_person.title]."
    elif alterations > 1:
        the_person "That was easy, I only had to change [alterations] parts of my wardrobe."
        mc.name "Thanks."
    elif alterations == 1:
        the_person "That was easy, I only had to change [alterations] part of my wardrobe."
        mc.name "Thanks."
    else:
        the_person "I'm sorry [the_person.mc_title], I couldn't find any parts of my wardrobe I was comfortable changing."
        if the_person.sluttiness > 90:
            mc.name "I guess we have probably taken things as far as they can go."
        else:
            mc.name "I guess I have some more work to do before you're ready for this."
    return
