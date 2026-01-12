init 4 python:
    def recolor_company_wardrobe_requirement():
        return company_wardrobe_loaded

    def recolor_company_wardrobe_initialization(self):
        ceo_office.add_action(self)
        return

    recolor_company_wardrobe_action = ActionMod("Rebuild Company Wardrobe", recolor_company_wardrobe_requirement, "recolor_company_wardrobe", initialization = recolor_company_wardrobe_initialization,
        menu_tooltip = "Adds a collection of over- and underwear for your company to your outfit manager.", category = "Wardrobe")

label recolor_company_wardrobe():
    "This will create a new set of company uniforms with the colour of your choice."
    "If you still have your original set this will make the list long and slightly unresponsive."
    "Would you like to delete all existing business uniforms first?"
    menu:
        "Yes":
            "WARNING: This is not reversible, all existing uniforms will be cleared from the business."
            menu:
                "Proceed":
                    $ mc.business.business_uniforms = []
                "Nevermind":
                    pass
        "No":
            pass
    call append_company_wardrobe() from _call_append_company_wardrobe
    return
