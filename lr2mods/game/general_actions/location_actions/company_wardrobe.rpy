## Company Uniforms Mod by Tristimdorion, edited by Elkrose
# Adds outfits based on company name to the company uniforms
init 3 python:
    company_wardrobe_loaded = False

    def company_wardrobe_requirement():
        return not company_wardrobe_loaded

    def company_wardrobe_initialization(self):
        self.enabled = False
        ceo_office.add_action(self)
        return

    def build_company_wardrobe(pri_color, sec_color, tre_color):
        #outfit(new_clothing, re_colour: list[float] | None = None, pattern: str | None = None, colour_pattern: list[float] | None = None)
        darker_pri_color = [pri_color[0]*.5, pri_color[1]*.5, pri_color[2]*.5, .95]
        darker_sec_color = [sec_color[0]*.5, sec_color[1]*.5, sec_color[2]*.5, .95]
        darker_tre_color = [tre_color[0]*.5, tre_color[1]*.5, tre_color[2]*.5, .95]
        lips_pri_color = [pri_color[0]*.5, pri_color[1]*.5, pri_color[2]*.5, .75]
        blush_sec_color = [sec_color[0]*.5, sec_color[1]*.5, sec_color[2]*.5, .5]
        heavy_eye_pri_color = [pri_color[0]*.5, pri_color[1]*.5, pri_color[2]*.5, .75]
        light_eye_sec_color = [sec_color[0]*.5, sec_color[1]*.5, sec_color[2]*.5, .5]

        normalu = Outfit(mc.business.name + " - Normal Underwear")
        normalu.add_upper(bralette.get_copy(), sec_color)
        normalu.add_lower(cute_panties.get_copy(), sec_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Relaxed Underwear")
        normalu.add_upper(strapless_bra.get_copy(), sec_color, "Pattern_1", tre_color)
        normalu.add_lower(lace_panties.get_copy(), sec_color, "Pattern_1", tre_color)
        normalu.add_feet(high_socks.get_copy(), pri_color, "Pattern_1", tre_color)
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Sexy Underwear")
        normalu.add_upper(lace_bra.get_copy(), sec_color)
        normalu.add_lower(lace_panties.get_copy(), sec_color, "Pattern_1", tre_color)
        normalu.add_feet(thigh_highs.get_copy(), tre_color)
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Provocative Underwear")
        normalu.add_upper(thin_bra.get_copy(), sec_color)
        normalu.add_lower(thong.get_copy(), sec_color)
        normalu.add_feet(fishnets.get_copy(), sec_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalu.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Risqué Underwear")
        normalu.add_upper(corset.get_copy(), darker_pri_color, "Pattern_1", darker_sec_color)
        normalu.add_lower(tiny_g_string.get_copy(), sec_color)
        normalu.add_feet(fishnets.get_copy(), sec_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalu.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Slutty Underwear")
        normalu.add_lower(tiny_g_string.get_copy(), sec_color)
        normalu.add_feet(garter_with_fishnets.get_copy(), darker_pri_color, "Pattern_1", pri_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalu.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Commando Underwear")
        normalu.add_feet(fishnets.get_copy(), sec_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalu.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Kinky Underwear")
        normalu.add_upper(cincher.get_copy(), darker_pri_color, "Pattern_1", darker_sec_color)
        normalu.add_lower(crotchless_panties.get_copy(), sec_color)
        normalu.add_feet(thigh_highs.get_copy(), sec_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalu.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalu.add_accessory(blush.get_copy(), blush_sec_color)
        normalu.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalo = Outfit(mc.business.name + " - Normal Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalo.add_upper(dress_shirt.get_copy(), pri_color)
        normalo.add_feet(slips.get_copy(), pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Pants Overwear")
        normalo.add_upper(dress_shirt.get_copy(), pri_color)
        normalo.add_upper(vest.get_copy(), darker_pri_color)
        normalo.add_lower(suitpants.get_copy(), darker_pri_color)
        normalo.add_feet(slips.get_copy(), pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Relaxed Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalo.add_upper(lace_crop_top.get_copy(), pri_color)
        normalo.add_feet(sandal_heels.get_copy(), pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Sexy Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalo.add_upper(business_vest.get_copy(), pri_color)
        normalo.add_feet(boot_heels.get_copy(), pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Sexy Overwear Boots")
        normalo.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalo.add_upper(business_vest.get_copy(), pri_color)
        normalo.add_feet(tall_boots.get_copy(), pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Fitness Overwear")
        normalo.add_upper(sweater.get_copy(), pri_color)
        normalo.add_lower(leggings.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalo.add_feet(sneakers.get_copy(), pri_color, "Pattern_1", tre_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Provocative Overwear")
        normalo.add_lower(belted_skirt.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalo.add_upper(belted_top.get_copy(), pri_color)
        normalo.add_feet(pumps.get_copy(), pri_color, "Pattern_1", tre_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Hotpants Overwear")
        normalo.add_upper(tanktop.get_copy(), pri_color)
        normalo.add_lower(jean_hotpants.get_copy(), darker_pri_color)
        normalo.add_feet(heels.get_copy(), pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Risqué Overwear")
        normalo.add_lower(mini_skirt.get_copy(), darker_pri_color)
        normalo.add_upper(business_vest.get_copy(), pri_color)
        normalo.add_feet(high_heels.get_copy(), pri_color)
        normalo.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalo.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalo.add_accessory(blush.get_copy(), blush_sec_color)
        normalo.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Easy Access Overwear")
        normalo.add_lower(micro_skirt.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalo.add_upper(vest.get_copy(), pri_color)
        normalo.add_feet(pumps.get_copy(), pri_color, "Pattern_1", tre_color)
        normalo.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalo.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalo.add_accessory(blush.get_copy(), blush_sec_color)
        normalo.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)


        normalf = Outfit(mc.business.name + " - Normal Uniform")
        normalf.add_upper(bralette.get_copy(), sec_color)
        normalf.add_upper(dress_shirt.get_copy(), pri_color)
        normalf.add_lower(cute_panties.get_copy(), sec_color)
        normalf.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalf.add_feet(slips.get_copy(), pri_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Normal Pants Uniform")
        normalf.add_upper(bralette.get_copy(), sec_color)
        normalf.add_upper(dress_shirt.get_copy(),  modify_transparency(pri_color, 1))
        normalf.add_upper(vest.get_copy(), darker_pri_color)
        normalf.add_lower(cute_panties.get_copy(), sec_color)
        normalf.add_lower(suitpants.get_copy(), darker_pri_color)
        normalf.add_feet(slips.get_copy(), pri_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Sexy Uniform")
        normalf.add_upper(business_vest.get_copy(), pri_color)
        normalf.add_lower(lace_panties.get_copy(), sec_color, "Pattern_1", tre_color)
        normalf.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalf.add_feet(thigh_highs.get_copy(), sec_color)
        normalf.add_feet(boot_heels.get_copy(), pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Sexy Uniform Boots")
        normalf.add_upper(business_vest.get_copy(), pri_color)
        normalf.add_lower(lace_panties.get_copy(), sec_color, "Pattern_1", tre_color)
        normalf.add_lower(pencil_skirt.get_copy(), darker_pri_color)
        normalf.add_feet(thigh_highs.get_copy(), sec_color)
        normalf.add_feet(tall_boots.get_copy(), pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Fitness Uniform")
        normalf.add_upper(sweater.get_copy(), pri_color)
        normalf.add_lower(lace_panties.get_copy(), sec_color, "Pattern_1", tre_color)
        normalf.add_lower(leggings.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_feet(sneakers.get_copy(), pri_color, "Pattern_1", tre_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Hotpants Uniform")
        normalf.add_upper(tanktop.get_copy(), pri_color)
        normalf.add_lower(tiny_lace_panties.get_copy(), sec_color)
        normalf.add_lower(jean_hotpants.get_copy(), darker_pri_color)
        normalf.add_feet(heels.get_copy(), darker_pri_color)
        normalf.add_feet(thigh_highs.get_copy(), sec_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Risqué Uniform")
        normalf.add_lower(mini_skirt.get_copy(), darker_pri_color)
        normalf.add_upper(business_vest.get_copy(), pri_color)
        normalf.add_feet(garter_with_fishnets.get_copy(), darker_pri_color, "Pattern_1", pri_color)
        normalf.add_feet(pumps.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(blush.get_copy(), blush_sec_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Slutty Uniform")
        normalf.add_upper(two_part_dress.get_copy(), darker_pri_color)
        normalf.add_upper(vest.get_copy(), pri_color)
        normalf.add_feet(fishnets.get_copy(), sec_color)
        normalf.add_feet(high_heels.get_copy(), tre_color)
        normalf.add_accessory(wide_choker.get_copy(), tre_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(blush.get_copy(), blush_sec_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Easy Access Uniform")
        normalf.add_lower(micro_skirt.get_copy(), darker_pri_color, "Pattern_1", darker_sec_color)
        normalf.add_upper(cincher.get_copy(), darker_pri_color, "Pattern_1", darker_sec_color)
        normalf.add_upper(vest.get_copy(), pri_color)
        normalf.add_feet(thigh_highs.get_copy(), sec_color)
        normalf.add_feet(pumps.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_accessory(wide_choker.get_copy(), tre_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(blush.get_copy(), blush_sec_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Plug N Play Uniform")
        normalf.add_upper(business_vest.get_copy(), modify_transparency(pri_color, 0.75))
        normalf.add_upper(quarter_cup_bustier.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_upper(cincher.get_copy(), darker_pri_color, "Pattern_1", darker_sec_color)
        normalf.add_lower(belted_skirt.get_copy(),  modify_transparency(darker_pri_color, 0.75), "Pattern_1", tre_color)
        normalf.add_lower(crotchless_panties.get_copy(), darker_pri_color)
        normalf.add_feet(garter_with_fishnets.get_copy(), darker_pri_color, "Pattern_1", pri_color)
        normalf.add_feet(high_heels.get_copy(), darker_pri_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(blush.get_copy(), blush_sec_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        normalf.add_accessory(gold_chain_necklace.get_copy(), [1, 1, .4, .95])
        normalf.add_accessory(gold_earings.get_copy(), [1, 1, .4, .95])
        normalf.add_accessory(forearm_gloves.get_copy(), modify_transparency(darker_pri_color, 0.75), "Pattern_1", tre_color)
        normalf.add_accessory(cum_slut_collar.get_copy(), darker_pri_color, "Pattern_2", tre_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Netflix N Chill Uniform")
        normalf.add_upper(two_part_dress.get_copy(), pri_color)
        normalf.add_lower(crotchless_panties.get_copy(), darker_pri_color)
        normalf.add_feet(garter_with_fishnets.get_copy(), darker_pri_color, "Pattern_1", pri_color)
        normalf.add_feet(pumps.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(blush.get_copy(), blush_sec_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        normalf.add_accessory(gold_chain_necklace.get_copy(), [1, 1, .4, .95])
        normalf.add_accessory(chandelier_earings.get_copy(), [1, 1, .4, .95])
        normalf.add_accessory(forearm_gloves.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_accessory(breed_collar.get_copy(), darker_pri_color, "Pattern_3", tre_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Roll N Dole Uniform")
        normalf.add_upper(quarter_cup_bustier.get_copy(), pri_color, "Pattern_1", tre_color)
        normalf.add_upper(tshirt.get_copy(), modify_transparency(pri_color, .75), "Pattern_3", tre_color)
        normalf.add_lower(belted_skirt.get_copy(), modify_transparency(darker_pri_color, .75), "Pattern_1", tre_color)
        normalf.add_lower(crotchless_panties.get_copy(), darker_pri_color)
        normalf.add_feet(fishnets.get_copy(), darker_pri_color)
        normalf.add_feet(heels.get_copy(), tre_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), heavy_eye_pri_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), modify_transparency(light_eye_sec_color, 0.5))
        normalf.add_accessory(blush.get_copy(), blush_sec_color)
        normalf.add_accessory(lipstick.get_copy(), lips_pri_color)
        normalf.add_accessory(gold_chain_necklace.get_copy(), [1, 1, .4, .95])
        normalf.add_accessory(gold_earings.get_copy(), [1, 1, .4, .95])
        normalf.add_accessory(forearm_gloves.get_copy(), darker_pri_color, "Pattern_1", tre_color)
        normalf.add_accessory(fuck_doll_collar.get_copy(), darker_pri_color, "Pattern", tre_color)
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        return

    company_wardrobe_action = ActionMod("Add Company Wardrobe", company_wardrobe_requirement, "append_company_wardrobe", initialization = company_wardrobe_initialization,
        menu_tooltip = "Adds a collection of over- and underwear for your company to your outfit manager.", category = "Wardrobe", )

label append_company_wardrobe():
    "Choose your primary business colour"
    menu:
        #Primary_Color, Secondary_Color, Tertiary_Color
        "Primary Colour Red":
            $ build_company_wardrobe([.78, .03, .08, .95], [.58, .01, .12, .95], [.97, .97, 1, .95])
        "Primary Colour Yellow":
            $ build_company_wardrobe([1, 1, .4, .95], [1, 1, .6, .95], [.97, .97, 1, .95])
        "Primary Colour Blue":
            $ build_company_wardrobe([.17, .32, .75, .95], [.87, .69, .17, .95], [.97, .97, 1, .95])
        "Primary Colour Green":
            $ build_company_wardrobe([.49, .73, .45, .95], [.76, .95, .73, .95], [.97, .97, 1, .95])
        "Primary Colour Lavender":
            $ build_company_wardrobe([.59, .42, .62, .95], [.67, .30, .73, .95], [.97, .97, 1, .95])
        "Primary Colour Grey":
            $ build_company_wardrobe([.36, .36, .36, .95], [.97, .97, 1, .95], [.97, .97, 1, .95])
        "Primary Colour Pink":
            $ build_company_wardrobe([1, .31, .66, .95], [1, .61, .81, .95], [.97, .97, 1, .95])
        "Primary Colour White":
            $ build_company_wardrobe([1, 1, 1, .95], [.89, .89, .89, .95], [.11, .11, .11, .95])

    $ company_wardrobe_loaded = True
    "Company wardrobe complete.\nCheck your employee uniforms, some items might not be enabled due to missing clothing policies (not slutty enough)."
    return
