init 10 python:
    def sex_stat_dictionary():
        result = {}
        for x in StatTracker.sex_stats:
            result[x] = mc.stats.sex_stat(x)
        return result

    def cum_stat_dictionary():
        result = {}
        for x in StatTracker.cum_stats:
            result[x] = mc.stats.cum_stat(x)
        return result

    def girl_stat_dictionary():
        result = mc.stats.tracked_stats("Girl")
        for x in StatTracker.info_stats:
            result[x] = mc.stats.info_stat(x)
        result["Pregnant"] = mc.stats.pregnancies
        result["In Trance"] = mc.stats.in_trance
        if is_cum_fetish_unlocked():
            result["Cum Fetish"] = mc.stats.cum_fetish
        if is_anal_fetish_unlocked():
            result["Anal Fetish"] = mc.stats.anal_fetish
        if is_breeding_fetish_unlocked():
            result["Breeding Fetish"] = mc.stats.breeding_fetish
        return result

    def employee_stat_dictionary():
        result = {}
        result["Employees"] = mc.business.employee_count
        return result | mc.stats.tracked_stats("Employee")

screen global_stat_ui():
    add paper_background_image
    modal True
    zorder 100

    default people_count = len(list_of_people)
    default corruption = sum(x.sluttiness for x in list_of_people) / people_count * 1.0

    vbox:
        spacing 25
        xalign 0.5
        xanchor 0.5
        yalign 0.05
        frame:
            xsize 1750
            ysize 80
            padding (0, 10)
            align (.5, .5)
            background "#1a45a1aa"
            text "Global Statistics" style "menu_text_header_style" size 36 xalign 0.5 yalign 0.5 yanchor 0.5

        hbox:
            xsize 1750
            spacing 30

            use global_stat_grid(f"Income - ${sum(mc.stats.income.values()):,}",
                sorted(mc.stats.income.items(), key = lambda item: item[1], reverse = True),
                (415, 570),
                "${:,}")

            use global_stat_grid(f"Expenses - ${sum(mc.stats.expenses.values()):,}",
                sorted(mc.stats.expenses.items(), key = lambda item: item[1], reverse = True),
                (415, 570),
                "${:,}")

            use global_stat_grid("Business",
                sorted(mc.stats.tracked_stats("Business").items()),
                (415, 570),
                "{:,.0f}")

            use global_stat_grid("Girl Stats",
                sorted(girl_stat_dictionary().items()),
                (415, 570),
                "{:,}")

        hbox:
            xsize 1750
            spacing 30

            use global_stat_grid("Sex Stats",
                sex_stat_dictionary().items(),
                (325, 350),
                "{:,}")

            use global_stat_grid("Cum Stats",
                cum_stat_dictionary().items(),
                (325, 200),
                "{:,}")

            use global_stat_grid("Employee Stats",
                employee_stat_dictionary().items(),
                (325, 200),
                "{:,}")

            $ relations_dict = {
                "Girlfriends": mc.stats.girlfriends,
                "Harem": mc.stats.harem,
                "Paramours": mc.stats.paramours,
                "Slaves": mc.stats.slaves
            }

            use global_stat_grid("Relations",
                relations_dict.items(),
                (325, 200),
                "{}")

            $ corruption_dict = mc.stats.tracked_stats("Corruption") | { "Active Serums": mc.stats.active_serums, "City Corruption": f"{corruption:.1f}%"}
            use global_stat_grid("Corruption",
                sorted(corruption_dict.items()),
                (325, 350),
                "{}")

    frame:
        background None
        align (0.5, 0.98)
        xysize (300, 150)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action Hide("global_stat_ui")
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

screen global_stat_grid(title, items, size = (300, 200), formatter = "${:,}", value_size = 100):
    default height = len(items)
    default width = size[0] - value_size - 32

    frame:
        background "#1a45a1aa"
        xysize size
        vbox xfill True:
            text "[title]" style "serum_text_style_header"
            viewport:
                scrollbars "vertical"
                draggable False
                mousewheel True
                vbox:
                    xfill True
                    for k, v in items:
                        hbox:
                            text "[k]:" min_width width style "menu_text_style"
                            text formatter.format(v) style "menu_text_style" min_width value_size textalign 1.0
