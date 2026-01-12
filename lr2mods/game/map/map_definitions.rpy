label instantiate_map_locations():
    python:
        # storage variables for last map location
        last_hub = None
        last_page = None

        ##PC's Home##
        hall = Room("home_hall", "Living Room", "Home_Background", [make_floor(), make_wall(), make_front_door()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting)
        bedroom = Room("mc_bedroom", "Your Bedroom", "Bedroom_Background", bedroom_objects,
            actions = mc_bedroom_actions(),
            map_pos = [1,0], lighting_conditions = standard_indoor_lighting)
        lily_bedroom = Room("lily_bedroom", "Lily's Bedroom", "Bedroom_Background", bedroom_objects,
            map_pos = [0,1], lighting_conditions = standard_indoor_lighting)
        mom_bedroom = Room("mom_bedroom", "Mom's Bedroom", "Bedroom_Background", bedroom_objects,
            actions = mom_bedroom_actions(),
            map_pos = [0,2], lighting_conditions = standard_indoor_lighting)
        kitchen = Room("kitchen", "Kitchen", "Kitchen_Background", [make_wall, make_floor(), make_chair(), make_table()],
            map_pos = [1,2], lighting_conditions = standard_indoor_lighting)
        home_bathroom = Room("bathroom", "Bathroom", "Home_Bathroom_Background", home_shower_objects,
            visible = False, darken = False)
        home_shower = Room("home_shower", "Home Shower", "Home_Shower_Background_Old", home_shower_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        her_hallway = Room("her_hallway", "Front hall", "her_hallway_background", [make_floor(), make_wall(), make_front_door(), make_hall_carpet(), make_stairs()],
            visible = False, lighting_conditions = standard_indoor_lighting)
        laundry_room = Room("laundry_room", "Laundry Room", "Laundry_Room_Background", laundry_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        dungeon = Room("dungeon", "Dungeon", "Dungeon_Background", dungeon_objects, [dungeon_room_appoint_slave_action],
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        harem_mansion = Room("harem_mansion", "Harem Mansion", "harem_mansion", harem_objects,
            map_pos =[1, 1], visible = False, lighting_conditions = standard_indoor_lighting)

        ##PC's Work##
        ceo_office = Room("ceo_office", "CEO Office", "CEO_Office_Background", ceo_office_objects,
            actions = ceo_office_actions(),
            map_pos = [1,0], tutorial_label = "ceo_tutorial_intro", lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, allow_walk_in = True)
        lobby = Room("lobby", "Lobby", "Office_Lobby_Background", [make_floor(), make_wall(), make_reception(), make_chair(), make_front_door(), make_window()],
            map_pos = [1,1], tutorial_label = "lobby_tutorial_intro", lighting_conditions = standard_indoor_lighting,
            privacy_level = 2)
        office = Room("main_office", "Main Offices", "Main_Office_Background", [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = main_office_actions(),
            map_pos = [0,1], tutorial_label = "office_tutorial_intro", lighting_conditions = standard_indoor_lighting,
            privacy_level = 2)
        m_division = Room("market_div", "Marketing Division", "Marketing_Background", [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = market_division_actions(),
            map_pos = [2,1], tutorial_label = "marketing_tutorial_intro", lighting_conditions = standard_indoor_lighting,
            privacy_level = 2)
        rd_division = Room("rd_div", "R&D Division", "RandD_Background", [make_floor(), make_desk(), make_window(), make_chair(), make_wall(), make_examtable()],
            actions = research_division_actions(),
            map_pos = [2,2], tutorial_label = "research_tutorial_intro", lighting_conditions = standard_indoor_lighting,
            privacy_level = 2)
        p_division = Room("prod_div", "Production Division", "Production_Background", [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = production_division_actions(),
            map_pos = [0,2], tutorial_label = "production_tutorial_intro", lighting_conditions = standard_indoor_lighting,
            privacy_level = 2)
        clone_facility = Room("clone_facility", "Cloning Facility", "Cloning_Facility_Background", [make_floor(), make_desk(), make_chair(), make_wall()],
            map_pos = [1,2], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False)
        work_bathroom = Room("work_bathroom", "Work Bathroom", "Bathroom_Background", [make_wall(), make_floor(), make_toilet(), make_sink()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False, allow_walk_in = True)
        testing_room = Room("testing_room", "Test Room", "Testing_Room_Background", [make_floor(), make_wall(), make_medical_table(), make_mirror()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False)
        storage_room = Room("storage_room", "Storage Room", "Storage_Room_Background", [make_floor(), make_wall(), make_door()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False, allow_walk_in = True)
        break_room = Room("break_room", "Break Room", "Break_Room_Background", [make_floor(), make_wall(), make_table(), make_chair(), make_bench(), make_window()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False)

        ## Downtown ##
        downtown = Room("downtown", "Downtown Streets", "Outside_Background", [make_floor(), make_bench(), make_alley()],
            actions = downtown_actions(),
            map_pos = [1,1], lighting_conditions = standard_outdoor_lighting,
            privacy_level = 3)
        downtown_bar = Room("bar", "The Downtown Distillery", "Bar_Background", downtown_bar_objects, [downtown_bar_drink_action],
            map_pos = [2,1], visible = True, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = downtown_bar_is_open, darken = False)
        downtown_bar_bathroom = Room("bar_bathroom", "Bar Bathroom", "Bar_Bathroom_Background", [make_wall(), make_floor(), make_toilet(), make_sink()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = downtown_bar_is_open, darken = False, allow_walk_in = True)
        downtown_hotel = Room("hotel_lobby", "The Hotel", "Hotel_Lobby_Background", downtown_hotel_lobby_objects,
            map_pos = [0,1], visible = True, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, darken = False)
        downtown_hotel_room = Room("hotel_room", "The Hotel Room", "Hotel_Room_Background", downtown_hotel_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False)
        fancy_restaurant = Room("fancy_restaurant", "Restaurant", "Fancy_Restaurant_Background", [make_floor(), make_chair(), make_table()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, darken = False)
        coffee_shop = Room("coffee_shop", "Coffee Shop", "Coffee_Shop_Background", coffee_shop_objects, [coffee_shop_get_coffee_action],
            map_pos = [1,0], visible = True, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = coffee_shop_is_open)
        mom_office_lobby = Room("mom_office_lobby", "Vandenberg\u00A0Ltd. Lobby", "Office_Lobby_Background", [make_wall(), make_floor(), make_chair(), make_reception(), make_window()],
            actions = mom_office_actions(),
            map_pos = [0,2], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = mom_office_is_open)
        mom_offices = Room("mom_office", "Vandenberg\u00A0Ltd. Offices", "Marketing_Background", [make_wall(), make_floor(), make_chair(), make_desk(), make_window()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = mom_office_is_open)
        office_photocopy_room = Room("office_photocopy", "Office Copy Room", "Office_PhotoCopy_Background", [make_wall(), make_floor(), make_chair(), make_desk(), make_window()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = mom_office_is_open, darken = False, allow_walk_in = True)
        hospital = Room("hospital", "Atrium Hospital", "Hospital_Background", hospital_objects,
            map_pos = [2,2], lighting_conditions = standard_outdoor_lighting,
            privacy_level = 3)
        hospital_room = Room("hospital_room", "Hospital Room", "Hospital_Room_Background", hospital_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False, allow_walk_in = True)

        ## MALL ##
        mall = Room("mall", "Atrium", "Mall_Background", [make_wall(), make_floor(), make_bench()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = mall_is_open)
        home_store = Room("home_store", "Home Improvement Store", "Home_Improvement_Store_Background", generic_store_objects,
            map_pos = [1,0], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = mall_is_open)
        clothing_store = Room("clothing_store", "Sak's Clothing Store", "Clothing_Store_Background", clothing_store_objects,
            map_pos = [2,2], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = mall_is_open)
        office_store = Room("supply_store", "Office Supply Store", "Office_Store_Background", generic_store_objects,
            map_pos = [2,1], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = mall_is_open)
        electronics_store = Room("electronics_store", "Electronics Store", "Electronics_Store_Background", generic_store_objects,
            map_pos = [0,1], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = mall_is_open)
        mall_salon = Room("salon", "Hair Salon", "Salon_Background", hair_salon_objects,
            map_pos = [0,2], visible = True, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = hair_salon_is_open)
        gaming_cafe = Room("gaming_cafe", "Gaming Café", "Internet_Cafe_Background", gaming_cafe_objects,
            actions = [gaming_cafe_grind_character_action, gaming_cafe_buy_max_level_token_action, gaming_cafe_adult_swim],
            map_pos = [1,2], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = gaming_cafe_is_open)
        gaming_cafe_store_room = Room("gaming_cafe_store_room", "Gaming Café", "Internet_Cafe_Store_Room_Background", [make_floor(), make_wall(), make_door(), make_chair(), make_table()],
            map_pos = [0,0], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False)
        mall_bathroom = Room("mall_bathroom", "Mall Bathroom", "Mall_Bathroom_Background", [make_wall(), make_floor(), make_toilet(), make_sink()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False, allow_walk_in = True)


        gym = Room("gym", "Gym", "Gym_Background", [make_wall(), make_floor(), make_bench(), make_mirror()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, accessible_func = gym_is_open, darken = False)
        gym_shower = Room("gym_shower", "Gym Shower", "Gym_Shower_Background", gym_shower_objects,
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 1, accessible_func = gym_is_open, allow_walk_in = True)

        sex_store = Room("sex_store", "Sex Store", "Sex_Shop_Background", generic_store_objects,
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 1, accessible_func = sex_shop_is_open)
        sex_store_storage = Room("sex_store_storage", "Sex Store Storage", "Sex_Shop_Backroom_Background", [make_wall(), make_floor(), make_mirror(), make_bench()],
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = sex_shop_is_open)

        ## Mall supporting locations
        changing_room = Room("changing_room", "Changing Room", "Changing_Room_Background", changing_room_objects,
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 1, accessible_func = mall_is_open, allow_walk_in = True)

        ##Other Locations##
        aunt_apartment = Room("aunt_apartment", "Living Room", "Home_Background", [make_floor(), make_wall(), make_couch(), make_table(), make_chair(), make_window()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting)
        aunt_bedroom = Room("aunt_bedroom", "Rebecca's Bedroom", "Generic_Bedroom4_Background", bedroom_objects,
            map_pos = [2,1],visible = False, lighting_conditions = standard_indoor_lighting)
        cousin_bedroom = Room("cousin_bedroom", "Gabrielle's Bedroom", "Cousin_Bedroom_Background", bedroom_objects,
            map_pos = [2,2], visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        university = Room("campus", "University Campus", "Campus_Background", [make_grass(), make_bench()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_outdoor_lighting,
            privacy_level = 1, accessible_func = university_is_open)
        university_library = Room("uni_library", "Library", "University_Library_Background", [make_floor(), make_wall(), make_table(), make_chair(), make_couch()],
            map_pos = [0,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 1, accessible_func = university_is_open, allow_walk_in = True)
        university_study_room = Room("study_room", "Study Room", "Study_Room_Background", [make_floor(), make_wall(), make_chair(), make_table(), make_window()],
            map_pos = [2,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 1, accessible_func = university_is_open, allow_walk_in = True)
        university_bathroom = Room("university_bathroom", "University Bathroom", "University_Bathroom_Background", [make_wall(), make_floor(), make_toilet(), make_sink()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = university_is_open, darken = False, allow_walk_in = True)
        university_lab = Room("university_lab", "Nora's Laboratory", "University_Lab_Background", [make_wall(), make_floor(), make_door(), make_window(), make_table(), make_chair()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = university_is_open, darken = False, allow_walk_in = True)

        strip_club = Room("strip_club", "Gentlemen's Club", "Club_Background", [make_wall(), make_floor(), make_table(), make_chair(), make_stage(), make_pole()],
            actions = strip_club_actions(),
            map_pos = [1,1], visible = False, lighting_conditions = standard_club_lighting,
            privacy_level = 1, accessible_func = strip_club_is_open, darken = False)
        bdsm_room = Room("bdsm_room", "BDSM\u00a0room", "BDSM_Room_Background", bdsm_room_objects, [dungeon_room_appoint_slave_action],
            map_pos = [0,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 1, accessible_func = strip_club_is_open, darken = False)
        strip_club_dressing_room = Room("club_dressing_room", "Dressing Room", "Club_Dressing_Room_Background", [make_wall(), make_floor(), make_chair(), make_mirror(), make_door()],
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, accessible_func = strip_club_is_open, darken = False, allow_walk_in = True)

        police_station = Room("police_station", "Police Station", "Police_Station_Background", ceo_office_objects,
            map_pos = [0,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3, darken = False)
        police_jail = Room("police_jail", "Police Jail", "Police_Jail_Background", police_jail_objects,
            visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 2, darken = False)

        city_hall = Room("city_hall", "City Hall", "Outside_Background", [make_wall(), make_floor(), make_chair(), make_reception(), make_window()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting,
            privacy_level = 3)

        # NOTE: People will not auto-leave purgatory -> to get her back in the game you need to change her location
        purgatory = Room("purgatory", "Hospital", "Hospital_Background", purgatory_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)

        prostitute_bedroom = Room("Prostitute Bedroom", "Prostitute Bedroom", "Prostitute_Bedroom_Background", bedroom_objects + [make_love_rug],
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_1 = Room("Generic Bedroom 1", "Bedroom", "Generic_Bedroom1_Background", bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_2 = Room("Generic Bedroom 2", "Bedroom", "Generic_Bedroom2_Background", bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_3 = Room("Generic Bedroom 3", "Bedroom", "Generic_Bedroom3_Background", bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_4 = Room("Generic Bedroom 4", "Bedroom", "Generic_Bedroom4_Background", bedroom_objects,
            visible = False, lighting_conditions = standard_indoor_lighting)


        ##Keep a list of all the places##
        list_of_places = [
            bedroom,
            lily_bedroom,
            mom_bedroom,
            kitchen,
            hall,
            her_hallway,
            laundry_room,
            home_bathroom,
            home_shower,
            dungeon,
            harem_mansion,

            ceo_office,
            lobby,
            office,
            rd_division,
            testing_room,
            storage_room,
            break_room,
            p_division,
            m_division,
            work_bathroom,
            clone_facility,

            downtown,
            downtown_bar,
            downtown_bar_bathroom,
            downtown_hotel,
            downtown_hotel_room,
            fancy_restaurant,
            hospital,
            hospital_room,

            mall,
            office_store,
            clothing_store,
            changing_room,
            sex_store,
            sex_store_storage,
            home_store,
            gym,
            gym_shower,
            electronics_store,
            mall_salon,
            coffee_shop,
            gaming_cafe,
            gaming_cafe_store_room,
            mall_bathroom,

            aunt_apartment,
            aunt_bedroom,
            cousin_bedroom,

            university,
            university_library,
            university_study_room,
            university_bathroom,
            university_lab,

            strip_club,
            bdsm_room,
            strip_club_dressing_room,

            mom_office_lobby,
            mom_offices,
            office_photocopy_room,

            city_hall,
            police_station,
            police_jail,
            purgatory,

            prostitute_bedroom,
            generic_bedroom_1,
            generic_bedroom_2,
            generic_bedroom_3,
            generic_bedroom_4,
        ]

    return


label instantiate_map_hubs():
    python:
        # Map Hubs for grouped map locations
        home_hub = MapHub("home", "Home", icon = "POI_House", position = Point(250, 475), locations = [hall, bedroom, lily_bedroom, mom_bedroom, kitchen, home_bathroom, dungeon, home_shower])
        aunt_home_hub = MapHub("aunt_home", "Rebecca's Apartment", icon = "POI_House", position = Point(150, 255), locations = [aunt_apartment,aunt_bedroom, cousin_bedroom])
        office_hub = MapHub("office", business_name, icon = "POI_Business", position = Point(1295, 365), locations = [lobby, m_division, p_division, rd_division, office, ceo_office, clone_facility, testing_room, work_bathroom, storage_room])
        mall_hub = MapHub("mall", "Shopping Mall", icon = "POI_Mall", position = Point(640, 360), locations = [mall, home_store, clothing_store, electronics_store, office_store, mall_salon, gaming_cafe, gaming_cafe_store_room, mall_bathroom], accessible_func = mall_is_open)
        sex_shop_hub = MapHub("sex_shop", "Starbuck's Sex\u00A0Shop", icon = "POI_Sexshop", position = Point(770, 120), locations = [sex_store, sex_store_storage], accessible_func = sex_shop_is_open)
        downtown_hub = MapHub("downtown", "Downtown", icon = "POI_Downtown", position = Point(560, 800), locations = [mom_office_lobby, mom_offices, downtown_bar, coffee_shop, downtown, downtown_hotel, downtown_hotel_room, fancy_restaurant, hospital, hospital_room, downtown_bar_bathroom, office_photocopy_room])
        plaza_hub = MapHub("plaza", "City Plaza", icon = "POI_Police", position = Point(500, 550), locations = [city_hall, police_station, police_jail])
        gym_hub = MapHub("gym", "Gym", icon = "POI_Gym", position = Point(890, 615), locations = [gym, gym_shower], accessible_func = gym_is_open)
        university_hub = MapHub("university", "University", icon = "POI_Uni", position = Point(1165, 770), locations = [university, university_library, university_study_room, university_bathroom, university_lab], accessible_func = university_is_open)
        harem_hub = MapHub("mansion", "Harem Mansion", icon = "POI_Brothel", position = Point(120, 660), locations = [harem_mansion])
        strip_club_hub = MapHub("stripclub", "Strip\u00A0Club", icon = "POI_Club", position = Point(800, 800), locations = [strip_club, bdsm_room, strip_club_dressing_room], accessible_func = strip_club_is_open)

        residential_home_hub = HomeHub("residential", "Residential District", icon = "District_Residential", position = Point(380, 190),
            people = [camila, salon_manager, starbuck, emily, sakari, kaya, naomi],
            jobs = [doctor_job, lawyer_job, architect_job, interior_decorator_job, fashion_designer_job, prostitute_job,
                pro_gamer_job, stripper_job, secretary_job, nurse_job, night_nurse_job])

        industrial_home_hub = HomeHub("industrial", "Bay\u00A0Area Condos", icon = "District_Industrial", position = Point(1050, 210),
            people = [ellie, stephanie, ashley, sarah, alexia, candace],
            jobs = [hr_job, market_job, rd_job, supply_job, production_job, head_researcher_job, IT_director_job, production_assistant_job, personal_secretary_job, office_worker_job,
                home_improvement_support_job, electronics_support_job,
                stripclub_stripper_job, stripclub_waitress_job, stripclub_bdsm_performer_job, stripclub_manager_job, stripclub_mistress_job])

        downtown_home_hub = HomeHub("downtown_home", "Downtown Apartments", icon = "District_Downtown", position = Point(300, 765),
            people = [city_rep, myra, police_chief],
            jobs = [unemployed_job, barista_job, bartender_job, waitress_job, hotel_receptionist_job, hotel_maid_job,
                hotel_maid_job2, hotel_chef_job, clothing_cashier_job, sex_cashier_job, electronics_cashier_job, supply_cashier_job,
                home_improvement_cashier_job, salon_hairdresser_job, store_assistant_job, store_clerk_job,
                gym_instructor_job, yoga_teacher_job, unemployed_job])

        university_home_hub = HomeHub("uni_home", "University Housing", icon = "District_ResidentialB", position = Point(1440, 820),
            people = [nora, erica],
            jobs = [university_professor_job, student_job, student_intern_market_job, student_intern_hr_job,
                student_intern_production_job, student_intern_rd_job, student_intern_supply_job])

        list_of_hubs = [home_hub, aunt_home_hub, office_hub, mall_hub, sex_shop_hub, downtown_hub, plaza_hub, strip_club_hub,
            gym_hub, university_hub, harem_hub, residential_home_hub, industrial_home_hub, downtown_home_hub, university_home_hub]

    return
