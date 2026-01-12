init -1 python:
    def new_footage_requirement(the_day):
        if mc.business.event_triggers_dict.get("home_cameras", []):
            if day > the_day + TIER_1_TIME_DELAY:
                if len(get_new_footage()) > renpy.random.randint(0, 2):
                    return True
        return False

    def clothing_plural(the_item):
        x = len(the_item.display_name) - 1
        if the_item.display_name[x] == "s":
            x -= 1
            if the_item.display_name[x] != "s":
                return True
        return False

    def clothing_colour_name(colour):
        if isinstance(colour, Clothing):
            colour = colour.colour
        r = str(colour[0]*100)
        g = str(colour[1]*100)
        b = str(colour[2]*100)
        rgb = rgb_percent_to_rgb((r, g, b))
        temp_name = get_colour_name(rgb)
        if temp_name in ['darkred', 'firebrick', 'indianred', 'rosybrown']:
            return "red"
        elif temp_name in ['darkorange', 'papayawhip', 'peachpuff', 'orangered']:
            return "orange"
        elif temp_name in ['darkgoldenrod', 'lemonchiffon', 'lightgoldenrodyellow', 'lightyellow', 'palegoldenrod', 'yellowgreen']:
            return "yellow"
        elif temp_name in ['darkgreen', 'darkolivegreen', 'darkseagreen', 'darkturquoise', 'forestgreen', 'lawngreen', 'lightgreen', 'lightseagreen', 'limegreen', 'mediumseagreen', 'mediumspringgreen', 'mediumturquoise', 'mintcream', 'olivedrab', 'palegreen', 'paleturquoise', 'springgreen', 'greenyellow']:
            return "green"
        elif temp_name in ['aliceblue', 'cadetblue', 'cornflowerblue', 'darkslateblue', 'deepskyblue', 'dodgerblue', 'lightblue', 'lightskyblue', 'lightsteelblue', 'mediumblue', 'darkblue', 'darkcyan', 'lightcyan', 'mediumslateblue', 'midnightblue', 'powderblue', 'royalblue', 'skyblue', 'slateblue', 'steelblue', 'mediumaquamarine']:
            return "blue"
        elif temp_name in ['blueviolet', 'darkorchid', 'darkviolet', 'lavenderblush', 'mediumvioletred', 'palevioletred', 'mediumorchid', 'mediumpurple']:
            return "violet"
        elif temp_name in ['darkkhaki', 'saddlebrown', 'sandybrown']:
            return "brown"
        elif temp_name in ['antiquewhite', 'blanchedalmond', 'floralwhite', 'ghostwhite', 'navajowhite', 'oldlace', 'whitesmoke']:
            return "white"
        elif temp_name in ['darkgray', 'darkgrey', 'darkslategray', 'darkslategrey', 'dimgray', 'dimgrey', 'lightgray', 'lightgrey', 'lightslategray', 'lightslategrey', 'slategray', 'slategrey']:
            return "grey"
        elif temp_name in ['darksalmon', 'deeppink', 'hotpink', 'lightpink', 'lightsalmon', 'darkmagenta', 'lightcoral', 'mistyrose']:
            return "pink"
        return temp_name

init 3 python:
    def electronic_intro_requirement(the_person):
        if mc.business.funds >= 5000:
            if the_person.location == electronics_store:
                return True
        return False

    def electronic_shopping_requirement():
        if electronic_employee.location == electronics_store:
            return True
        return "Wait for business to open"

    def review_footage_requirement():
        if mc.business.event_triggers_dict.get("home_cameras", []):
            return True
        return False

    def get_camera_targets():
        temp_list = []
        for x in known_people_in_the_game():
            if x.home in mc.known_home_locations:
                if not x in mc.business.event_triggers_dict.get("home_cameras", []):
                    temp_list.append(x)
        return temp_list

    def get_new_footage(): #daily run to check for new content
        temp_list = []
        for x in mc.business.event_triggers_dict.get("home_cameras", []):
            if x.sluttiness >= x.event_triggers_dict.get("camera_level", 90) + 20:
                temp_list.append(x)
        return temp_list

    def build_footage_menu(person):
        temp_list = []
        for slut in ["90", "80", "60", "40", "20", "0"]: #morning
            if person.event_triggers_dict.get("camera_level", 0) >= int(slut):
                name = "Morning " + slut
                label = "morning_" + slut
                temp_list.append([name, label])
        for slut in ["90", "80", "60", "50", "40", "20", "0"]: #shower
            if person.event_triggers_dict.get("camera_level", 0) >= int(slut):
                name = "Shower " + slut
                label = "shower_" + slut
                temp_list.append([name, label])
        if person in []: #lily, mom, others?
            for slut in ["80", "60", "40", "20", "0"]: #living room
                if person.event_triggers_dict.get("camera_level", 0) >= int(slut):
                    if any(x for x in get_existing_friends(town_relationships, person) if x.sluttiness >= int(slut)):
                        name = "Living Room " + slut
                        label = "living_room_" + slut
                        temp_list.append([name, label])
#        for slut in [60, 80]: #shower
#            if person.event_triggers_dict.get("camera_level", 0) >= slut:
#                name - "Shower " + str(slut)
#                label = "shower_" + str(slut)
#                temp_list.append([name, label])
#        for slut in [40]: #bedtime
#            if person.event_triggers_dict.get("camera_level", 0) >= slut:
#                name - "Bedtime " + str(slut)
#                label = "bedtime_" + str(slut)
#                temp_list.append([name, label])
#                if person.is_student and slut == 40:
#                    temp_list.append(["Student Bedtime 40", "student_bedtime_40"])
        return temp_list

    def electronic_employee_mod_initialization():
        global electronic_employee
        electronic_employee = make_person(age = 22, personality = introvert_personality, \
            stat_array = [2,8,2], skill_array = [5,1,1,1,1], sex_skill_array = [3,3,3,3], \
            sluttiness = 20, obedience_range = [130, 150], happiness = 150, love = 0, start_home = None, \
            mc_title = mc.name, relationship = "Single", kids = 0, \
            forced_opinions = [["flirting", 2, False], ["skirts", 2, False], ["the colour blue", 2, False]], \
            forced_sexy_opinions = [["skimpy outfits", 2, False], ["drinking cum", 2, False], ["giving blowjobs", 2, False], ["public sex", 2, False]])
        electronic_employee.generate_home()
        electronic_employee.set_title(electronic_employee.name)
        electronic_employee.set_possessive_title(electronic_employee.name)
        electronic_employee.set_mc_title("Watcher")
        electronic_employee.set_event_day("day_met")
        electronic_employee.change_job(electronics_support_job)
        electronic_employee.set_override_schedule(strip_club, time_slots = [3])
        electronics_store.add_person(electronic_employee)
        electronic_intro_action = Action("Look around", electronic_intro_requirement, "electronic_intro_label", menu_tooltip = "See what is in stock.")
        electronic_employee.add_unique_on_room_enter_event(electronic_intro_action)
        review_footage_action = Action("Look at recordings", review_footage_requirement, "review_footage_label")
        bedroom.add_action(review_footage_action)
        return

init 16 python:
    add_label_hijack("normal_start", "activate_electronic_employee_mod_core")
    add_label_hijack("after_load", "update_electronic_employee_mod_core")

label activate_electronic_employee_mod_core(stack):
    python:
        electronic_employee_mod_initialization()
        execute_hijack_call(stack)
    return

label update_electronic_employee_mod_core(stack):
    python:
        if "electronic_employee" not in globals():
            electronic_employee_mod_initialization()
        execute_hijack_call(stack)
    return

label electronic_intro_label(the_person):
    $ scene_manager = Scene()
    $ mc.business.event_triggers_dict["home_cameras"] = []
    $ electronics_store.show_background()
    "You enter the electronic's store. The smell of plastic and cleaning products gives it an oddly fresh scent."
    "Browsing through row upon row of devices, you take your time examining various models of the many products they have on display."
    $ scene_manager.add_actor(the_person)
    "As you are strolling down the home security aisle you are approached by a young girl wearing a name tag, [the_person.name!u]."
    # TODO assign variables to describe her
    "She carries herself confidently walking up and clearing her throat softly, she addresses you politely."
    the_person "Hi there! Is there anything I can assist you with today?"
    "You were mostly just browsing, but a quick look at the shelf gives you a topic to engage with."
    mc.name "Just checking these cameras actually. Thinking about getting some for home security purposes."
    "Her eyes widen briefly and a grin lights up her face. Is she working on commission?"
    the_person "Of course! Let me show you what we have available then."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She leads you deeper into the store towards rows of sleek high definition monitors displaying grainy footage captured both indoors and outdoors - all designed specifically for keeping tabs on potential threats day or night."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "As she rambles about camera angles, resolution quality and price range, you find yourself becoming increasingly distracted by thoughts not related to security anymore..."
    mc.name "And how about something smaller? Something less conspicuous perhaps?"
    $ scene_manager.update_actor(the_person, position = "stand2")
    "The girl bites her lower lip cutely before nodding knowingly and glancing around nervously."
    $ mc.change_arousal(5)
    the_person "We do carry some covert models which aren't immediately recognisable as cameras, some people enjoy using them for... different reasons."
    the_person "What kind of environment will it be used in primarily?"
    mc.name "Probably inside."
    the_person "There are different types depending on light conditions, noise levels... even whether there'll be any liquids involved during recording sessions."
    "She seems very knowledgeable, mentioning how certain colours blend better against fabric backgrounds or emphasizing waterproof capabilities when discussing bathroom/shower settings."
    "Her eagerness is palpable, revealing more about her character than she probably intended."
    mc.name "What if something were to happen unexpectedly late at night when everyone else is asleep? Do you have something that would capture everything clearly regardless?"
    the_person "Y-yes definitely! We offer several infrared models perfect for low-light situations like that."
    mc.name "That sounds great, do they record sound too?"
    $ mc.change_arousal(5)
    "Her cheeks turn bright red now and she stammers slightly before recovering gracefully."
    the_person "Yes, most modern ones do, some even come equipped with microphones capable of picking up whispers from across the room."
    mc.name "Anything else I should know?"
    the_person "You could also look into motion sensors. They send alerts directly to your phone whenever movement is detected, allowing you complete peace of mind even when you're not physically present."
    mc.name "Wow, that sounds incredible, I didn't realise there were so many options."
    "Her eyes flicker down and back up quickly, betraying her excitement."
    the_person "Of course! To truly maximize your investment though, you may want a DVR recorder for storage capacity and continuous recording capability."
    mc.name "These devices really are impressive, how much would this setup cost?"
    the_person "It can vary quite a bit depending on brand and model. But..."
    $ mc.change_arousal(5)
    "She leans close, continuing suggestively."
    the_person "If money isn't an issue... we could put together a custom package tailored exactly to your desires."
    menu:
        "Make it happen \n{color=#ff0000}{size=18}Costs: $1000{/size}{/color}" if mc.business.funds >= 1000:
            "[the_person.title] selects four miniature marvels designed specifically for close range monitoring and one water resistant unit ideal for bathroom usage."
            "She also grabs a portable DVR unit capable of storing days worth of footage."
            "There is no question that this is a worthwhile investment so you quickly hand over your business credit card to make the purchase."
            $ mc.business.change_funds(-1000)
            $ mc.business.event_triggers_dict["home_cameras"].append(lily)
            $ lily.event_triggers_dict["camera_level"] = 0
            $ mc.business.event_triggers_dict["home_cameras"].append(mom)
            $ mom.event_triggers_dict["camera_level"] = 0
            $ new_footage_mandatory = Action("New Footage", new_footage_requirement, "new_footage_label", requirement_args=day)
            $ mc.business.add_mandatory_crisis(new_footage_mandatory)
            "She efficiently bags everything up and tucks the receipt in the bag before returning your card."
            "She also hands you a business card adorned with contact info including her name and social media handles, and a site dedicated to promoting these products online."
            the_person "Enjoy watching and remember, if you ever need assistance setting anything up or have questions later on... well, my door is always open."
            $ mc.change_arousal(5)
            "She winks saucily before turning away leaving you feeling thrilled by what you just did."
        "Make it happen{color=#ff0000}{size=18}Costs: $1000{/size}{/color} (disabled)" if mc.business.funds < 1000:
            pass
        "Not now":
            mc.name "Unfortunately, right now might not be the best time... financially speaking, I've got some other stuff going on."
            the_person "I understand. I'll be here if you change your mind."
            "She hands you a business card adorned with contact info including her name and social media handles, and a site dedicated to promoting these products online."
            the_person "Don't forget us when making future decisions regarding privacy matters!"
    $ the_person.event_triggers_dict["insta_known"] = True
    $ the_person.event_triggers_dict["dikdok_known"] = True
    $ the_person.add_role(instapic_role)
    $ the_person.add_role(dikdok_role)
    $ mc.phone.register_number(the_person)
    python:
        # phone_shopping_action = Action("Look at phones", electronic_shopping_requirement, "phone_shopping_label")
        # electronics_store.add_action(phone_shopping_action)
        # gaming_shopping_action = Action("Look at gaming devices", electronic_shopping_requirement, "gaming_shopping_label")
        # electronics_store.add_action(gaming_shopping_action)
        camera_shopping_action = Action("Look at cameras \n{color=#ff0000}{size=18}Costs: $1000{/size}{/color}", electronic_shopping_requirement, "camera_shopping_label")
        electronics_store.add_action(camera_shopping_action)
    $ scene_manager.clear_scene()
    return

label phone_shopping_label():
    "You've already got a phone that meets all of your needs, but as you look at them you consider how having unfettered access to another person's phone could be advantageous."
    "For example, you could install some spyware to forward messages, giving you insight into what a girl really believes. If she is in a relationship you might even be able to probe for weaknesses to exploit."
    "It also might be possible to link the photos to a cloud you can access, allowing you to see what she is doing and who she is spending time with."
    while True:
        menu:
            "Buy a phone":
                $ mc.business.change_funds(-1200)
            "Leave":
                pass
    return

label gaming_shopping_label():
    "Buy a gift for Maya or someone else"
    while True:
        menu:
            "Leave":
                pass
    return

label camera_shopping_label():
    $ scene_manager = Scene()
    $ the_person = electronic_employee
    $ scene_manager.add_actor(the_person, emotion = "happy", display_transform = character_right(xoffset = -.15))
    if not mc.business.event_triggers_dict.get("home_cameras", []):
        "As soon as you approach the camera aisle, [the_person.title] spots you from across the showroom floor and her face lights up with anticipation."
        the_person "Welcome back! Did you reconsider investing in some discreet surveillance equipment after all?"
        menu:
            "Make it happen \n{color=#ff0000}{size=18}Costs: $1000{/size}{/color}" if mc.business.funds >= 1000:
                "[the_person.title] leads you to a well-stocked corner display case filled with tiny cameras sporting various shapes and sizes."
                "Each device promises high definition video quality coupled with crisp audio recording capabilities sure to satisfy even the most discriminating voyeuristic needs."
                "After selecting three miniature marvels designed specifically for close range monitoring and one water resistant unit, she guides you towards a portable DVR unit capable of storing days worth of footage."
                "There is no question that this is a worthwhile investment so you quickly hand over your business credit card to make the purchase."
                $ mc.business.change_funds(-1000)
                $ mc.business.event_triggers_dict["home_cameras"].append(lily)
                $ lily.event_triggers_dict["camera_level"] = 0
                $ mc.business.event_triggers_dict["home_cameras"].append(mom)
                $ mom.event_triggers_dict["camera_level"] = 0
                $ new_footage_mandatory = Action("New Footage", new_footage_requirement, "new_footage_label", requirement_args=day)
                $ mc.business.add_mandatory_crisis(new_footage_mandatory)
                the_person "Enjoy watching and remember, if you ever need assistance setting anything up or have questions later on... well, my door is always open."
                $ mc.change_arousal(5)
                "She winks saucily before turning away leaving you feeling thrilled by what you just did."
            "Make it happen{color=#ff0000}{size=18}Costs: $1000{/size}{/color} (disabled)" if mc.business.funds < 1000:
                pass
            "Not now":
                mc.name "Unfortunately, right now might not be the best time financially speaking, I've got some other stuff going on."
                the_person "I understand. I'll be here if you change your mind."
                the_person "Don't forget us when making future decisions regarding privacy matters!"
    else:
        "As soon as you enter the camera aisle, [the_person.title] spots you from across the showroom floor and her face lights."
        if mc.business.event_triggers_dict.get("camera_system_count", 0) < 1:
            the_person "Back so soon? Didn't think you'd be needing more equipment quite this fast."
        else:
            the_person "[the_person.mc_title], what brings you here today?"
        $ potential_people_list = get_camera_targets()
        menu:
            "It is for a friend's house \n{color=#ff0000}{size=18}Learn more home locations{/size}{/color} (disabled)" if len(potential_people_list) < 1:
                pass
            "It is for a friend's house \n{color=#ff0000}{size=18}Costs: $1250{/size}{/color}" if len(potential_people_list) > 0:
                mc.name "Well, I have a... friend who mentioned wanting to do something similar for their house."
                "She arches an eyebrow skeptically, but plays along anyway."
                the_person "Oh? Well, let's make sure they get the best setup possible then."
                "She shows you the latest upgraded selection of cameras and accessories the store has."
                the_person "By the way, how are things going with your cameras? Any issues or complaints?"
                mc.name "No, nothing like that. I'm still fine tuning the positioning, but they are everything you promised."
                the_person "Glad to hear it. So this looks like everything you will need for your friend's house. The internet portal makes it $1250."
                menu:
                    "I'll take it \n{color=#ff0000}{size=18}Costs: $1250{/size}{/color}" if mc.business.funds >= 1250:
                        call screen main_choice_display(build_menu_items([get_sorted_people_list(potential_people_list, "Potential people", "Back")]))
                        $ person_choice = _return
                        if isinstance(person_choice, Person):
                            $ mc.business.change_funds(-1250)
                            $ temp_list = home_residents(person_choice.home)
                            while len(temp_list) > 0:
                                $ temp_person = temp_list[0]
                                $ temp_list.remove(temp_person)
                                if not temp_person in mc.business.event_triggers_dict["home_cameras"]:
                                    if not temp_person in known_people_in_the_game():
                                        $ temp_person.set_mc_title(mc.name)
                                        $ temp_person.set_title(temp_person.name)
                                    $ mc.business.event_triggers_dict["home_cameras"].append(temp_person)
                                    $ temp_person.event_triggers_dict["camera_level"] = 0
                        else:
                            "You change your mind and don't buy the camera."
                    "I'll take it \n{color=#ff0000}{size=18}Costs: $1250{/size}{/color} (disabled)" if mc.business.funds < 1250:
                        pass
                    "Not now":
                        mc.name "Unfortunately, right now might not be the best time... financially speaking, I've got some other stuff going on."
                        the_person "I understand. I'll be here if you change your mind."
                        the_person "Don't forget us when making future decisions regarding privacy matters!"
            "It is for my business \n NO CONTENT Written \n{color=#ff0000}{size=18}Costs: $2000{/size}{/color} (disabled)":
                mc.name "I'm running a business and wanted to pick up some security measures for the lab. Lots of expensive chemicals and things."
                the_person "Absolutely, we recently got these microscopic cameras that can blend seamlessly into ceiling panels or light fixtures, virtually undetectable unless someone knows precisely where to look.."
                mc.name "That sounds perfect, how about storage capacity? There are a lot of rooms."
                the_person "Our latest DVR models can hold terabytes upon terabytes of data."
                mc.name "That's impressive. How much will it set me back?"
                the_person "With the extra rooms and the new upgrades it will be $2000."
                menu:
                    "I'll take it \n{color=#ff0000}{size=18}Costs: $2000{/size}{/color}" if mc.business.funds >= 2000:
                        $ mc.business.change_funds(-2000)
                    "I'll take it \n{color=#ff0000}{size=18}Costs: $2000{/size}{/color} (disabled)" if mc.business.funds < 2000:
                        pass
                    "Not now":
                        mc.name "Unfortunately, right now might not be the best time... financially speaking, I've got some other stuff going on."
                        the_person "I understand. I'll be here if you change your mind."
                        the_person "Don't forget us when making future decisions regarding privacy matters!"
            "Something is wrong with my system \n not written (disabled)" if the_person.sluttiness > 40:
                mc.name "Actually, there might be something wrong with my system. I would love some expert assistance if you don't mind coming over tonight?"
                if the_person.love < 30:
                    "[the_person.title] hesitates only momentarily before nodding enthusiastically."
                the_person "Alright, [the_person.mc_title]. Give me your address, and I'll be there shortly after closing hours."
                "SET LOCATION"
                "ON ENTER EVENT"
            "Just browsing":
                mc.name "Just looking. Now that I have a security system I figured I would try to stay up to date on the newest tech."
                the_person "That's a great idea, so many of our customers just expect stuff to work and end up spending a ton of extra money when they can't figure it out."
                mc.name "I'll let you know if I need any help."
                the_person "Kay, I'll be around."
    $ scene_manager.clear_scene()
    return

label camera_repair_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "Arriving punctual at 9 PM sharp, dressed in form fitting jeans and a fitted top revealing generous amounts of cleavage herself, she steps inside as though she belongs there instantly."
    "Her eyes roam appreciatively around your living room before homing in on you, perched nervously on the edge of the sofa."
    "Let's see what we can do, she says, taking a seat beside you and inspecting the faulty DVR unit carefully."
    "After fiddling with wires and buttons for several minutes, [the_person.title] finally announces triumphantly, I think I got it!"
    "Sure enough, the screen comes alive with previously frozen images, and you lean forward anxiously to watch the previously elusive video."
    "The scene unfolds slowly, depicting [the_person.title] preparing dinner naked except for a loose apron tied around her waist."
    "As she moves gracefully across the kitchen, her pert ass and firm breasts sway enticing, setting off waves of heat within you."
    "This camera must be superb quality, [the_person.title] whispers admiringly, her breath brushing against your ear causing goosebumps to rise on your neck."
    "Yeah, uhm, well, it was expensive, you mutter, trying desperately to focus on the screen rather than the sensations [the_person.title] evokes."
    "But it becomes increasingly difficult as the video progresses, showing [the_person.title] accidentally dropping ingredients onto the floor, giving you excuses to zoom in on her exposed pussy dripping with juices."
    "You know, Mr. Smithsonian, [the_person.title] purred, her fingers tracing circles on your thigh beneath the table, you seem very... focused on this particular feed."
    "A knowing smirk played at her lips as her index finger teasingly skims up your leg, stopping just shy of touching the bulge growing noticeably in your pants."
    "Is there more going on between you two than meets the eye?"
    "Shifting uneasily, you try to deflect attention away from the obvious."
    "My sister likes to cook naked sometimes, that's all."
    "It sounded feeble even to your own ears, but [the_person.title] merely chuckled softly, her voice husky with desire."
    "Oh, really? And how often does she 'accidentally' drop things?"
    "She continued to stroke your thigh provocatively, drawing circles nearer to your aching cock until finally, her delicate fingertip grazes the fabric of your pants, sending electric shockwaves coursing through your body."
    "Every damn day, you growl out, unable to resist the temptation any longer."
    "The video cuts to [the_person.title] sitting on the couch, sipping wine and absentmindedly rubbing lotion onto her feet."
    "Unbeknownst to her, the camera captures everything—her slender arches spread wide open exposing plump, bare soles and supple toes begging to be worshiped; the way her hips undulate rhythmically in time with unheard music."
    "You groan audibly, unable to tear your gaze away from the mesmerizing sight."
    "Noticing your evident discomfort, [the_person.title] stands up seductively, straddling your lap face-to-face with the TV."
    "Leaning closer still, their breath mingling, she murmurs into your ear, Maybe I could help relieve some of that pent-up frustration?"
    "Before you can respond, deft hands reach underneath your shorts and boxers, freeing your throbbing member from its confines."
    "Ohhh, she hums approvingly, gently stroking the length of your hardened cock. It seems like someone needs release."
    "With practiced ease, she begins massaging your sensitive head, applying light pressure up and down your shaft, matching her movements perfectly to those onscreen."
    "Meanwhile, on the screen, [the_person.title]'s foot rub escalates into an erotic massage as her toes curl and flex in response to the sensations."
    "In real life, [the_person.title] increases the intensity of her strokes, using both hands now, working faster and harder until you are squirming in pleasure."
    "Your breath catches raggedly as [the_person.title] lifts one leg, resting her heel on the coffee table, offering easy access to her wet folds."
    "In sync, [the_person.title] wraps her warm palm around your balls, squeezing them affectionately, while her other hand continues to jack you mercilessly."
    "As [the_person.title] moans softly in ecstasy, her body trembling with approaching climax, so do you, close behind her."
    "Climaxing together, you cry out in bliss as cum explodes all over [the_person.title]'s tight tank top, staining it with your seed."
    "Breathless, you collapse back into the couch, feeling completely spent yet utterly satisfied."
    "Looking at [the_person.title], who's grinning broadly, you manage a weak apology. I'm sorry, I didn't mean—"
    "She silences you with a kiss, her tongue probing deeply into your mouth, leaving no doubt about her true intentions."
    "Don't apologise, she whispers hoarsely, threading her fingers through yours. We both enjoyed ourselves immensely."
    "Now let's make sure nothing else goes wrong today, [the_person.title] says breathlessly, breaking the intense kiss."
    "With nimble fingers, she reconnects the remaining devices, linking her own network to yours seamlessly."
    "There we go! Now you can enjoy the show, and maybe return the favor when I need a little relief?"
    "Her eyes sparkle mischievously as she presses play on another tab, revealing herself lying naked on her bed, legs spread invitingly."
    "As [the_person.title] makes her way towards the door, she turns back once more, giving you a wink."
    "Have fun watching, loverboy, she giggles before disappearing down the hallway, leaving only the sounds of her high heels clicking against the floor echoing through the house."
    "Feeling slightly dazed but incredibly turned on by the whole experience, you sink deeper into the cushions, focusing intently on the image playing out on the screen - [the_person.title] pleasuring herself expertly, her slim fingers plunging deep inside her wet core as she gasps for air."
    "Slowly building momentum, [the_person.title] slips a finger inside her dripping pussy, circling her clit with gentle pressure before thrusting two digits deep within her wetness."
    "Her breath quickens as she works herself into a frenzy, hips bucking wildly off the mattress in search of satisfaction."
    "Her free hand travels southward, cupping her perky breasts through the thin material of her bra, pinching nipples made rigid by excitement."
    "Grunting loudly, she picks up speed, sliding her middle finger in and out rapidly while her thumb furiously circles her swollen bud."
    "Desperate now, [the_person.title] reaches below for something hidden under her pillow – a smooth glass dildo which she lubricates generously before positioning it at her entrance."
    "Eyes closed tightly, she guides it slowly inside herself, taking care not to push too far too soon."
    "Moaning in delight, she starts rocking back and forth along the length of the phallus, gradually increasing pace until she hits a steady rhythm that sends jolts of pleasure shooting through her entire being."
    "Closer and closer she comes, each movement more urgent than the last until finally..."
    "...[the_person.title]'s entire body convulses violently as waves upon waves of ecstatic pleasure wash over her."
    "A sharp cry escapes her lips followed by a torrent of curses and moans mixed together."
    "She collapses backwards onto the bed, limp but satisfied, her chest rising and falling rapidly beneath the thin fabric covering it."
    $ scene_manager.clear_scene()
    return

label new_footage_label():
    $ new_footage_mandatory = Action("New Footage", new_footage_requirement, "new_footage_label", requirement_args=day)
    $ mc.business.add_mandatory_crisis(new_footage_mandatory)
    $ scene_manager = Scene()
    $ temp_list = get_new_footage()
    if not temp_list:
        "EVENT FAILED"
        return
    $ the_person = get_random_from_list(temp_list)
    if not isinstance(the_person, Person):
        "EVENT FAILED"
        return
    if len(mc.business.event_triggers_dict.get("home_cameras", [])) < 3:
        "You get an alert on your phone from the camera system you have set up in your house."
    else:
        "You get an alert on your phone from one of the camera systems you have set up in [the_person.possessive_title]'s house."
    $ scene_manager.add_actor(the_person)
    "It looks like you have some new recordings from the camera that is monitoring [the_person.title]."
    $ the_person.event_triggers_dict["camera_level"] += 20
    "If you want to see what is new you'll have to go to your bedroom and check."
    menu:
        "Go now":
            $ scene_manager.clear_scene()
            $ mc.change_location(bedroom)
            call review_footage_label() from _call_review_footage_label_new
        "Check later":
            pass
    $ del temp_list
    $ scene_manager.clear_scene()
    return

label review_footage_label():
    $ done_watching = False
    "Sitting at your computer you pull up the user interface for your camera systems."
    if mc.business.event_triggers_dict.get("study_recordings", []):
        menu:
            "Normal recordings":
                pass
            "Study buddy recordings":
                call study_recordings_menu_label() from _call_study_recordings_menu_label_ea
                return
    $ camera_list = mc.business.event_triggers_dict.get("home_cameras", [])
    call screen main_choice_display(build_menu_items([get_sorted_people_list(camera_list, "Footage review", "Back")]))
    $ the_person = _return
    while not the_person == "Back":
        while not done_watching:
            $ footage_list = build_footage_menu(the_person)
            call screen main_choice_display(build_menu_items([["Select Footage"] + footage_list + ["Back"]]))
            $ label_choice = _return
            if label_choice == "Back":
                $ done_watching = True
            elif label_choice == "morning_0":
                call morning_0(the_person) from _call_morning_0_review
            elif label_choice == "morning_20":
                call morning_20(the_person) from _call_morning_20_review
            elif label_choice == "morning_40":
                call morning_40(the_person) from _call_morning_40_review
            elif label_choice == "morning_60":
                call morning_60(the_person) from _call_morning_60_review
            elif label_choice == "morning_80":
                call morning_80(the_person) from _call_morning_80_review
            elif label_choice == "morning_90":
                call morning_90(the_person) from _call_morning_90_review
            elif label_choice == "shower_0":
                call shower_0(the_person) from _call_shower_0_review
            elif label_choice == "shower_20":
                call shower_20(the_person) from _call_shower_20_review
            elif label_choice == "shower_40":
                call shower_40(the_person) from _call_shower_40_review
            elif label_choice == "shower_50":
                call shower_50(the_person) from _call_shower_50_review
            elif label_choice == "shower_60":
                call shower_60(the_person) from _call_shower_60_review
            elif label_choice == "shower_80":
                call shower_80(the_person) from _call_shower_80_review
            elif label_choice == "shower_90":
                call shower_90(the_person) from _call_shower_90_review
            elif label_choice == "living_room_0":
                call living_room_0(the_person) from _call_living_room_0_review
            elif label_choice == "living_room_20":
                call living_room_20(the_person) from _call_living_room_20_review
            elif label_choice == "living_room_40":
                call living_room_40(the_person) from _call_living_room_40_review
            elif label_choice == "living_room_60":
                call living_room_60(the_person) from _call_living_room_60_review
            elif label_choice == "living_room_80":
                call living_room_80(the_person) from _call_living_room_80_review
            elif label_choice == "living_room_90":
                call living_room_90(the_person) from _call_living_room_90_review
        call screen main_choice_display(build_menu_items([get_sorted_people_list(camera_list, "Footage review", "Back")]))
        $ the_person = _return
        $ done_watching = False
    if mc.arousal > 50:
        "Watching the videos has resulted in you becoming aroused. Do you want to do something about it now?"
        menu:
            "Masturbate {image=gui/heart/Time_Advance.png}":
                call bedroom_masturbation_enhanced() from _call_bedroom_masturbation_enhanced_recordings
            "Get serviced (not written)\n Requires obedient girls (disabled)" if True:
                pass
            "Get serviced {image=gui/heart/Time_Advance.png}" if False:
                "build list of people in hub and see if they are obedient enough"
            "Visit someone (not written)\n Requires girls who are home (disabled)" if True:
                pass
            "Visit someone {image=gui/heart/Time_Advance.png}" if False:
                "check recording list to see who is home, allow failure"
            "Leave":
                pass
    $ del done_watching
    $ del camera_list
    return

label living_room_0(the_person):
    $ scene_manager = Scene()
    $ temp_list = get_existing_friends(town_relationships, person)
    $ the_other_person = get_random_from_list([x for x in temp_list if x.sluttiness >= 0])
    if not the_other_person:
        "RECORDING FAILED"
        return
    "The footage begins with the camera providing a wide-angle view of your living room."
    "Soft natural light fills the space, creating a warm and inviting atmosphere."
    "The camera captures the carefully arranged furniture, including the comfortable couch, a coffee table adorned with a stack of books, and a cozy armchair positioned near a window."
    "In the background, the television stands against the wall, displaying a captivating nature documentary."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_other_person, position = "sitting")
    "You see [the_person.possessive_title] and [the_other_person.title] engaged in a deep conversation, sitting on the couch."
    "Both of them are fully absorbed in the discussion, leaning forward and occasionally gesturing to emphasize points."
    "The camera's audio capture enables you to hear snippets of the conversation, revealing the exchange of ideas and the genuine enthusiasm in their voices."
    "It's evident that the conversation is meaningful and engrossing, filled with thoughtful insights and shared experiences."
    "As time progresses, the camera records the shifting light patterns as the sun sets outside the window."
    "Soft golden hues give way to the warm glow of lamps, casting a cozy ambiance throughout the living room."
    "Shadows dance on the walls, adding a touch of tranquility to the scene."
    "The camera focuses on the changing facial expressions and hand movements as [the_person.title] and [the_other_person.possessive_title] continue the conversation."
    "The genuine smiles, nods of agreement, and occasional laughter reveal the deep connection and comfort shared between them."
    "As the conversation gradually winds down, the camera records a sense of contentment and relaxation settling in."
    "They both lean back on the couch, briefly glancing at the television screen, appreciating the beauty of the documentary's visuals."
    $ scene_manager.clear_scene()
    return

label living_room_20(the_person):
    $ scene_manager = Scene()
    $ temp_list = get_existing_friends(town_relationships, person)
    $ the_other_person = get_random_from_list([x for x in temp_list if x.sluttiness >= 20])
    if not the_other_person:
        "RECORDING FAILED"
        return
    "The footage begins with the camera providing a wide-angle view of your living room, bathed in soft, natural light."
    "The room exudes a cozy and welcoming ambiance, with comfortable seating arrangements and tastefully decorated surroundings."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_other_person, position = "sitting")
    "[the_person.possessive_title!c] and her friend [the_other_person.title] sit on the couch, positioned opposite each other."
    "The camera captures their animated expressions and the excitement evident in their gestures."
    "They lean in, engrossed in a lively conversation, their faces illuminated by the warm glow of the room."
    "Their conversation flows effortlessly, with laughter interspersed throughout."
    "The camera's audio capture allows you to hear snippets of their discussion, filled with shared memories, inside jokes, and occasional exclamations of surprise or amusement."
    "Their voices carry a tone of familiarity and deep connection, reflecting the bond between friends."
    "As they engage in conversation, a tray of snacks rests on the coffee table between them."
    "They occasionally reach for a handful of chips or grab a refreshing drink from the glasses placed nearby."
    "The camera captures these subtle moments of enjoyment and relaxation, adding to the overall atmosphere of comfort and camaraderie."
    "The camera's focus alternates between [the_person.title] and [the_other_person.possessive_title], capturing their expressive faces and the genuine joy they derive from each other's company."
    "They lean forward, their eyes sparkling with enthusiasm, and occasionally lean back, relaxing into the cushions, allowing for moments of contemplation."
    "In the background, soft music plays from a speaker, creating a pleasant backdrop for their conversation."
    "The melody complements their interaction, infusing the room with a soothing and uplifting aura."
    "As time passes, the camera records the changing light patterns in the room, indicating the progression of the day."
    "Soft shadows cast by the setting sun dance on the walls, heightening the intimate and tranquil atmosphere."
    $ scene_manager.clear_scene()
    return

label living_room_40(the_person):
    $ scene_manager = Scene()
    $ temp_list = get_existing_friends(town_relationships, person)
    $ the_other_person = get_random_from_list([x for x in temp_list if x.sluttiness >= 40])
    if not the_other_person:
        "RECORDING FAILED"
        return
    "The footage begins with the camera providing a wide-angle view of your living room, bathed in soft, warm light that creates an intimate and inviting atmosphere."
    "The room reflects a comfortable and personal space, adorned with tasteful decorations and cozy seating arrangements."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_other_person, position = "sitting")
    "[the_person.possessive_title!c] and [the_other_person.title] sit close to each other on the couch, their hands gently intertwined."
    "The camera captures the genuine affection and tenderness they share, evident in the way they exchange soft glances and affectionate smiles."
    "Engrossed in a heartfelt conversation, their voices carry a blend of sincerity and emotional depth."
    "The camera's audio capture allows you to hear the soft timbre of their voices as they discuss their thoughts, dreams, and experiences."
    "They speak with a sense of trust and openness, creating an atmosphere of deep connection and understanding."
    "As they talk, their expressions fluctuate between moments of shared laughter and quiet reflection."
    "The camera focuses on their faces, revealing the subtle nuances of their emotions, such as the twinkle in their eyes or the warmth of their smiles."
    "In the background, a mellow playlist plays softly, setting the mood for their intimate conversation."
    "The gentle melodies provide a soothing backdrop, further enhancing the atmosphere of comfort and intimacy within the room."
    "Occasionally, they pause their conversation to share a tender embrace or a gentle touch, their affectionate gestures accentuating the depth of their bond."
    "The camera captures these moments of physical closeness, preserving the genuine love and connection they share."
    "As time passes, the camera records the changing lighting conditions in the room, as the sun sets outside."
    "Soft, warm hues filter through the windows, casting a romantic glow upon the space, amplifying the sense of intimacy."
    $ scene_manager.clear_scene()
    return

label living_room_60(the_person):
    $ scene_manager = Scene()
    $ temp_list = get_existing_friends(town_relationships, person)
    $ the_other_person = get_random_from_list([x for x in temp_list if x.sluttiness >= 60])
    if not the_other_person:
        "RECORDING FAILED"
        return
    "The footage begins with the camera providing a wide-angle view of your living room, suffused with warm, natural light."
    "The room exudes an intimate and inviting ambiance, adorned with comfortable seating arrangements and personal touches."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(the_other_person)
    "[the_person.possessive_title!c] and [the_other_person.title] enter the living room, deeply engrossed in each other's presence."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_other_person, position = "sitting")
    "As they settle onto the couch, their attention remains fixated on one another, oblivious to the camera recording their every move."
    "Their conversation gradually evolves into playful banter, accompanied by contagious laughter and animated gestures."
    "The camera's audio capture picks up their joyful exchanges, amplifying the sense of fun and affection that fills the room."
    "As their connection intensifies, their physicality becomes more pronounced."
    "They playfully nudge each other's shoulders, engage in gentle teasing, and occasionally steal quick, tender kisses."
    "Their body language reveals their comfort and trust, as they lean closer, intertwining their fingers or resting hands on each other's thighs."
    $ the_person.change_arousal(10)
    $ the_other_person.change_arousal(10)
    "The atmosphere is charged with an undercurrent of desire and excitement."
    "They lean into each other, their eyes locked with a mixture of affection and passion."
    "Their smiles radiate an undeniable attraction, and the air around them brims with an electric energy."
    "The camera expertly captures these intimate moments of physical connection."
    "Their hands explore each other's bodies with gentle caresses and affectionate touches."
    "Their movements become more fluid and spontaneous, completely lost in the pleasure of each other's company."
    $ the_person.change_arousal(10)
    $ the_other_person.change_arousal(10)
    $ mc.change_locked_clarity(5)
    "As time passes, the camera continues to record the scene."
    "The shifting light patterns indicate the progression of the day, casting subtle shadows that dance across their entwined forms."
    "Their connection remains unbroken, as their bodies subtly shift and adjust to find the perfect closeness."
    $ scene_manager.clear_scene()
    return

label living_room_80(the_person):
    $ scene_manager = Scene()
    $ temp_list = get_existing_friends(town_relationships, person)
    $ the_other_person = get_random_from_list([x for x in temp_list if x.sluttiness >= 80])
    if not the_other_person:
        "RECORDING FAILED"
        return
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_other_person, position = "sitting")
    "SEX SCENE WIP"
    $ scene_manager.clear_scene()
    return

label generic_masturbation(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "[the_person.title] kicks off her heels, casting them carelessly aside, and loosens her restrictive uniform, revealing her lacy black bra and matching thong."
    "Gingerly, she runs her fingers along her sensitive inner thighs, feeling the residue left by earlier friction."
    "Unable to resist any longer, she scoots closer to her bed, lying prone on the cool sheets. She spreads her legs wide apart, exposing her juicy cunt begging for attention."
    "Restless, she plays with her nipples, pinching and twisting them till they harden, leaking droplets of sweet nectar."
    "Her hand travels lower, finding warmth and wetness waiting patiently for her touch. Teasingly, she traces the edge of her swollen lips, driving herself crazy with anticipation."
    "Then, with a swift motion, she dives right in, relishing the feel of her own fingers probing her tight hole."
    "The sounds of her heavy breathing fill the quiet room as [the_person.possessive_title] increases the intensity of her ministrations."
    "Her hips rise and fall in sync with each thrust, creating an erotic dance only meant for her ears, her eyes closed tightly in blissful abandonment."
    "So lost in her world of pleasure, [the_person.title] groans loudly, unable to contain her mounting ecstasy."
    "Just when release seems imminent, a sudden surge of electricity courses through her core, setting off a chain reaction. [the_person.title]'s entire body convulses violently, her voice cracking as she screams out her name twice before succumbing completely to the waves of euphoria washing over her - courtesy of her remote-controlled vibrator."
    "Panting heavily, sweaty and spent, [the_person.title] lies still for a moment trying to catch her breath. But already, that insatiable hunger is building once again beneath her skin; a constant reminder that there will be no rest for the wanton slut that she has become."
    
    "As the sun sets on yet another busy day at work, [the_person.title] retires to her sanctuary – her bedroom. The dim light casts a sultry ambiance over the space, inviting her to unwind and let go of the day's stressors. Eager to find relief, she sheds her clothes with practiced ease, baring her curvaceous frame adorned in nothing but a flimsy negligee."
    "Kneeling on her bed, she props herself against a pillow, allowing her hands free rein to explore her body. Starting with her full breasts, she fondles them lovingly, tweaking her nipples into hardened peaks. A low growl escapes her lips as she feels her arousal growing, demanding attention."
    "With purpose, [the_person.title] parts her legs, giving you a clear view of her dripping snatch. Without hesitation, she plunges two fingers into her depths, curling them to reach that special spot that always sends her over the edge. Her other hand joins in the fun, rubbing her engorged clit in slow, deliberate circles."
    "Moans escape her parted lips as [the_person.title] picks up the pace, her fingers working in tandem to bring her closer to bliss. Her hips grind against her palm, seeking even more stimulation, her breath coming in ragged gasps. The sound of flesh meeting flesh fills the room, echoing her desire for more."
    "Suddenly, the distinct hum of a vibrator breaks the silence, shocking [the_person.title] out of her reverie. Realising it's Robert who controls her pleasure, she tries to fight the intense sensations but fails miserably. Writhing under the powerful vibrations, [the_person.title]'s back arches, pushing her chest forward as if offering herself to him."
    "Her climax crashes down upon her like a tidal wave, pulling her under its irresistible pull. Trembling from head to toe, [the_person.title]'s walls grip tight around the intruder inside her, milking every last drop of satisfaction from it. Sweat drenches her brow as she rides out this epic orgasm, moaning out her love for me between ragged breaths."
    $ scene_manager.clear_scene()
    return

label generic_strip(the_person):
    $ scene_manager = Scene()
    $ the_person.home.show_background()
    $ scene_manager.add_actor(the_person)
    "[the_person.title] walks into their bedroom, unaware that you have set up a hidden camera to record their every move."
    "They begin to undress, slowly removing each piece of clothing as if they are performing a seductive dance just for you."
    "As they strip down, you can't help but notice how beautiful they look without any clothes on."
    "Their body is perfect, and you find yourself growing increasingly aroused by the sight of them."
    $ scene_manager.clear_scene()
    return

label bedtime(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "In the dim light of her bedroom, [the_person.title] undresses gracefully, seemingly unaware of being watched. First, she slips her blazer off her shoulders, letting it fall to the floor, followed by her fitted vest, revealing a delicate camisole that clings lovingly to her petite frame. Next, she unfastens her belt and pulls down her trousers, showing off her smooth, toned legs and perfectly trimmed bush."
    "[the_person.title] stands momentarily, gazing at herself in the mirror, appreciating her lean physique highlighted by the soft glow of the moonlight filtering through the curtains. Finally, she reaches up to unclip her bra, freeing her modest but firm breasts, which bounce enticingly as they meet freedom."
    "She steps out of her shoes and socks, allowing her soles to luxuriate in the cold wood flooring. [the_person.title] then delicately lifts one leg, hooking it around the bedpost, and slowly slithers out of her pantyhose-clad legs, revealing her shapely calves and sexy little feet. Standing completely nude except for her briefs, she hesitates for a fleeting moment, savouring this rare moment of vulnerability."
    "With a sultry smile, [the_person.title] slips on a set of adorably oversized PJ bottoms made of soft cotton, granting her even more freedom of movement. A matching tank top follows suit, emphasizing her slim torso and small but perky chest."
    "Crawling into bed, [the_person.title] burrows under the blankets, her body heat radiating like a furnace, sending waves of temptation across the room."
    $ scene_manager.clear_scene()
    return

label student_bedtime_40(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "Once alone in her spacious bedroom, she kicks shut the door behind her and immediately sets about shedding her restrictive school uniform."
    "First, the white button-up blouse comes off, exposing her lacy black bra which struggles to contain her perky breasts."
    "Next goes the plaid skirt, pooling at her feet revealing matching black panties and a hint of sheer black stockings peeking out from beneath."
    "Next comes the corseted waist cincher, loosening her already hourglass figure ever so slightly; then finally, those tight, knee-length socks are tossed carelessly aside."
    "Slipping on a short, silk pink nightgown embroidered with cherry blossoms, [the_person.title] moves towards her dresser where a box containing a pair of red satin sleepwear pants and matching top awaits her."
    "Sliding the pants up her toned thighs and over her smooth, bare ass, she savours the softness of the fabric against her sensitive flesh."
    "Then, she slips the cropped tank top over her head, baring her flat abdominal musculature and plush cleavage."
    "Stepping closer to the vanity mirror, she admires how her pert nipples press against the semi-transparent material."
    "Feeling even more liberated now, [the_person.title] crawls underneath the covers of her queen size bed, snuggling into the soft sheets."
    $ scene_manager.clear_scene()
    return

label lily_room_cheat(the_sister, the_person):
    $ lily_bedroom.show_background()
    $ scene_manager = Scene()
    $ the_buddy = get_lab_partner()
    $ scene_manager.add_actor(the_person)
    "Alone in your room, you settle down on your bed with your laptop, eager to see the latest footage of [the_sister.title] and [the_buddy.title]'s escapades."
    "As you click play, however, you're greeted by a surprise – instead of seeing [the_sister.title] and [the_buddy.title] together, you see [the_sister.title] and [the_person.title] engaged in passionate sex."
    "Your cock twitches as you watch them, their moans and gasps filling the silence of your room."
    "[the_person.title]'s fingers dance over [the_sister.title]'s sensitive flesh, driving her wild with pleasure."
    "Meanwhile, [the_sister.title] returns the favor, her tongue tracing circles around [the_person.title]'s clit until she cries out in ecstasy."
    "You close your eyes, letting out a soft moan as you stroke your throbbing member. The soundtrack of their lustful cries fills your ears, heightening your arousal."
    "You imagine being there with them, feeling their warmth and affection as they lose themselves in each other's bodies."
    "Suddenly, you hear a loud gasp from the video. Opening your eyes, you see [the_sister.title] climax violently, her body shuddering under [the_person.title]'s touch."
    "A moment later, [the_person.title] follows suit, crying out her own release."
    "As the video ends, you let out a long, drawn-out sigh, your mind filled with images of the two girls writhing in pleasure."
    "You lean back on the bed, still stroking yourself, savouring every memory of the scene you just witnessed."
    $ scene_manager.clear_scene()
    return

#two girls together
#As soon as they enter the room, [the_person.title] closes the door behind them and turns to face Ellie. Her eyes sparkle with desire and anticipation as she takes Ellie's hands in hers, drawing her closer.*
#""I've been wanting to do this all week,""
#she confesses before leaning in for a passionate kiss. Ellie responds eagerly, her lips parting slightly to allow [the_person.title]'s tongue to dance with hers sensuously.
#[the_person.title] breaks the kiss, her hands trailing down Ellie's body to reach for the hem of her shirt. She lifts it up slowly, revealing Ellie's toned stomach and bra-clad breasts.*
#""You're so beautiful,""
#[the_person.title] murmurs as she begins to unbutton Ellie's jeans, carefully sliding them down her legs along with her panties until she is left standing in only her bra. [the_person.title] then removes her own clothes, leaving both women naked and exposed before each other.*
#Ellie can feel her cheeks flushing crimson as [the_person.title]'s eyes roam over her body, taking in every curve and crevice with a mixture of hunger and admiration. [the_person.title] grins playfully before guiding Ellie to lie down on the bed, her fingers gently tracing patterns on Ellie's skin as she does so.*
#Once Ellie is comfortable, [the_person.title] leans in close again, her lips caressing Ellie's neck tenderly.*
#""Relax,""
#she whispers softly, her breath hot against Ellie's ear. "
#I'm going to take care of you."
#With that, [the_person.title] begins to kiss her way down Ellie's body, stopping at every sensitive spot along the way: nipples hardening beneath her lips, belly fluttering with each gentle touch, and finally reaching their destination - Ellie's wet pussy.
#As [the_person.title]'s tongue delves into Ellie's folds for the first time, she lets out a soft moan, arching her back off the bed in response. The sensation is unlike anything she has ever experienced before; intense yet somehow also soothing.*
#""Oh god,""
#she whispers as [the_person.title] continues to lick and suck on her clit, driving her further towards pleasure. Her hips begin to move rhythmically against [the_person.title]'s mouth, seeking more contact as she feels herself growing closer to climax.*
#Finally, after what seems like an eternity but can only have been minutes, Ellie reaches her peak. With a loud cry, she bucks her hips upwards into [the_person.title]'s face, her orgasm washing over her like waves crashing onto shore.
#[the_person.title] doesn't stop until every last shudder has subsided, gently kissing Ellie's inner thighs before crawling up next to her.*
#""How was that?"" she asks softly. ""Did you like it?""*
#Ellie nods weakly, still trying to catch her breath from the intensity of the experience. She leans in for another passionate kiss with [the_person.title] before pulling away slightly and smiling at her newfound lover.*
#""It felt… amazing,"" she admits breathlessly.

#shower threesome
#They both turn towards him with shocked expressions on their faces as they realise he has walked in on them showering together. But instead of covering themselves up or trying to hide, they simply smile shyly at each other before turning back around.*
#""Morning,"" Ellie says softly over the sound of falling water. ""We didn't think you were awake yet.""*
#[the_person.mc_title] smiles back at her and takes a step closer, his eyes roaming appreciatively over their naked forms. ""I couldn't sleep anymore… so I decided to join you girls for some fun today too!""*
#He strips off his clothes quickly and steps into the shower behind [the_person.title], wrapping one arm around her waist while reaching down between her legs from behind. His fingers find her wet folds easily enough; it seems like she was enjoying herself even without him there! Meanwhile, Ellie stands facing away from them both, giving [the_person.mc_title] an unobstructed view of her ass as she lathers up her body soap.*
#As his fingers begin to explore inside [the_person.title]'s pussy, she lets out a moan that echoes throughout the bathroom walls.
#Ellie glances over her shoulder at them with a mischievous grin before turning back around to continue washing herself.*
#""You know,"" she says teasingly, ""I've always wondered what it would be like if we all… you know…"" Her voice trails off suggestively as [the_person.mc_title]'s fingers slip deeper inside [the_person.title], making her gasp once more.*
#[the_person.mc_title] smiles broadly; it seems that Ellie has been thinking about this too! He leans forward and whispers into [the_person.title]'s ear: ""Why don't we let her join us?""*
#[the_person.title] nods eagerly in agreement just as Ellie turns around again - this time facing them both fully. Her cheeks are flushed pink from both the heat of the shower and embarrassment at being caught watching them by [the_person.mc_title] earlier on.*
#""W-what did you have in mind?"" She stammers out nervously but there is excitement dancing behind her eyes nonetheless.*
#[the_person.mc_title] takes Ellie's hand gently in his own before guiding it down towards [the_person.title]'s pussy where he has been touching her just moments ago.*
#""Why don't you take over for me?"" He suggests playfully. ""I think she likes it when someone else touches her too…""*
#Ellie hesitates for a moment, unsure if she should really go through with this - but then again, why not? They had already shared so much last night… what harm could there be in exploring things further now that they were all together once more? With a shaky breath, she nods her consent and allows [the_person.mc_title] to guide her fingers into [the_person.title]'s wet folds.*
#[the_person.title] moans loudly as Ellie begins to tentatively explore her pussy, slowly gaining confidence in her movements as she discovers how sensitive [the_person.title] is to even the lightest touch. [the_person.mc_title] steps back slightly to give them both space, watching intently from behind as their hands intertwine and their bodies move in sync beneath the streaming water.*
#[the_person.mc_title] grins as he watches the two girls pleasure each other, his own arousal growing by the second. He reaches for a bottle of shampoo on a nearby shelf and squirts some onto [the_person.title]'s ass before spreading it around with his fingers - lubricating her for what comes next.*
#As Ellie continues to finger [the_person.title]'s pussy at an increasingly faster pace, [the_person.mc_title] positions himself behind [the_person.title], pressing against her wet entrance. With one swift thrust, he enters her tight hole, causing both women to cry out in unison from the sudden intrusion. The water cascading down around them only adds to their heightened sensations, making everything feel more slippery and intense than ever before.
#[the_person.title] arches her back against him while Ellie maintains focus on her clit, working it expertly between her fingers as they all rock together underneath the shower spray.*
#""Oh god,"" [the_person.title] moans loudly, ""this feels so good!""
#""Tell me about it,"" [the_person.mc_title] groans in response, his hips pumping faster inside of her. ""You're so tight!""
#Ellie glances over at them briefly before returning to what she was doing - but not without giving each one a quick wink first.*
#Their passionate lovemaking continues for several more minutes until finally [the_person.title] cries out once again as she reaches orgasm, clenching around [the_person.mc_title]'s cock and causing him to release deep inside her as well. They all collapse against the wall together, catching their breath underneath the warm water streaming down upon them from above.
#As they slowly come back down from their high, Ellie pulls away from [the_person.title]'s now slick folds with a satisfied smirk on her face before turning off the shower and stepping out onto the bathmat beside them both.*
#""Well that was… interesting,"" She says teasingly while wrapping herself up in a large towel provided by [the_person.mc_title] earlier. ""I think I might need another round though…"" Her eyes twinkle mischievously as she looks between them both suggestively.

#[the_person.mc_title] grins as he watches the two girls pleasure each other, his own arousal growing by the second. He reaches for a bottle of shampoo on a nearby shelf and squirts some onto [the_person.title]'s ass before spreading it around with his fingers - lubricating her for what comes next.
#As Ellie continues to finger [the_person.title]'s pussy at an increasingly faster pace, [the_person.mc_title] positions himself behind [the_person.title], pressing against her tight hole. With one swift thrust, he enters her wet entrance, causing both women to cry out in unison from the sudden intrusion. The water cascading down around them only adds to their heightened sensations, making everything feel more slippery and intense than ever before.
#[the_person.title] arches her back against him while Ellie maintains focus on her clit, working it expertly between her fingers as they all rock together underneath the shower spray.*
#""Oh god,"" [the_person.title] moans loudly, ""this feels so good!""
#""Tell me about it,"" [the_person.mc_title] groans in response, his hips pumping faster inside of her. "
#[the_person.mc_title] groans in response, his hips pumping faster inside of her. ""And don't forget who taught you how to love anal like this.""
#He grabs hold of Ellie's hand, pulling her closer so that she too can feel the girth of his member sliding in and out of [the_person.title]'s ass. ""Feel that? That's pure bliss right there.""
#Ellie gasps as she feels the thickness of his shaft rubbing against her palm, unable to resist the urge any longer. She moves her hand lower, starting to stroke herself off as she watches them fuck. ""I want a turn,"" She whispers seductively into [the_person.mc_title]'s ear before leaning forward to capture [the_person.title]'s lips in a passionate kiss.*
#Their passionate lovemaking continues for several more minutes until finally [the_person.title] cries out once again as she reaches orgasm, clenching around [the_person.mc_title]'s cock and causing him to release deep inside her as well. They all collapse against the wall together, catching their breath underneath the warm water streaming down upon them from above.
#[the_person.title] and Ellie share a long, lingering kiss before turning to face [the_person.mc_title] with matching grins on their faces. ""That was… incredible,"" [the_person.title] says breathlessly.*
#""I know,"" He agrees, chuckling softly as he wraps his arms around both of them. ""And it's only just begun…""

#girl recruiting
#""I can't believe you haven't tried it yet,"" [the_person.title] says teasingly, taking a bite of her salad. ""It feels amazing."" She licks her lips suggestively as she watches Ellie carefully from across the dinner table.
#Ellie blushes slightly at this comment but doesn't respond right away - focusing instead on cutting up her steak into smaller pieces.*
#""Come on,"" [the_person.title] continues after swallowing another mouthful. ""You know you want to. I promise you won't regret it."" Her eyes sparkle mischievously as they lock onto Ellie's once more.
#Finally putting down her fork, Ellie takes a deep breath before speaking again. ""Maybe… maybe later tonight?""
#[the_person.title]'s grin widens even further at this admission, knowing she has successfully tempted her friend into trying something new. ""I knew you'd come around eventually!"" She exclaims gleefully before turning towards [the_person.mc_title] who stands by the stove, cooking up another one of his masterful creations.*
#""Looks like we have a new fan in the making,"" [the_person.title] says with a wink in Ellie's direction.
#[the_person.mc_title] chuckles softly as he plates their meals, placing them on the table with care. ""Well, I guess it's time to see if my skills are really up to par."" He gives both girls an alluring smile before sitting down between them. ""But for now, let's enjoy our dinner - we can save the real fun for dessert.""
#Ellie blushes again but can't help smiling back at him shyly. She picks up her fork and begins eating, glancing occasionally at [the_person.title] who seems more than happy to continue their conversation about [the_person.mc_title]'s prowess between bites of food.*
#The atmosphere around the table is filled with sexual tension as they eat - each bite reminding them of what lies ahead once dinner has concluded. And although Ellie remains hesitant, there's an undeniable excitement building within her at the thought of finally experiencing firsthand just how good it feels to be intimate with both [the_person.title] and [the_person.mc_title] together under one roof.
#As they finish up their meals, Ellie clears away the plates while [the_person.mc_title] and [the_person.title] help themselves to some delicious looking dessert. The moment she returns from the kitchen though, things take a more serious turn when [the_person.mc_title] looks her straight in the eye with that same alluring grin he wore earlier. ""Are you ready for your special surprise?"" He asks softly before standing up from his chair.*
#Ellie swallows hard but nods nonetheless - unable or unwilling to resist any longer as curiosity gets the better of her. Without another word, [the_person.mc_title] leads them both into the living room where an assortment of pillows have been strategically placed on the floor forming a makeshift bed big enough for three people. He helps each girl lie down comfortably before climbing onto the bed himself, positioning himself between them so that his hard cock presses against both their stomachs teasingly.
#""Now,"" He says softly as he runs his hands over their bodies, making sure they are both comfortable before moving lower towards their waists. ""It's time for us to become one.""
#With that, he slides his hands underneath them and gently guides their hips closer together until they are practically grinding against each other. As Ellie feels [the_person.title]'s soft pussy rubbing against her own clit through the thin fabric of their panties, she can't help but moan softly in anticipation of what's about to happen next.*
#""Now,"" [the_person.mc_title] continues as he leans forward so that his mouth is mere centimeters away from Ellie's ear. ""I want you both to focus on how good this feels - on all the pleasure we're going to share together."" He then begins kissing along her neck, his lips leaving a trail of fire behind them as he works towards finding her sensitive spots.*
#Meanwhile, [the_person.title] takes advantage of this moment by leaning forward herself, capturing Ellie's lips in a passionate kiss while one hand explores further southward, teasing at the hem of her shirt before finally making its way inside to touch her bare skin for the first time tonight.
#Ellie gasps into the kiss as she feels [the_person.title]'s fingers grazing against her nipples through her bra - sending shivers down her spine that only intensify when [the_person.mc_title] adds his own touch to the mix. His hands roam freely over both their bodies, leaving no inch untouched by his skilled caresses.*
#Finally breaking away from each other's lips with a gasp for air, Ellie looks at [the_person.title] who smiles reassuringly back before turning towards [the_person.mc_title] once more. ""I want this,"" She whispers breathlessly. ""I want you both."" And without further hesitation, he positions himself between them so that his cock is pressed directly against Ellie's entrance while still maintaining contact with [the_person.title] on either side of him.
#""Are you sure?"" He asks softly one last time before slowly pushing inside of her, filling her completely as he does so. Both girls moan loudly upon feeling him enter them simultaneously - their hips bucking involuntarily due to the sudden influx of pleasure coursing through their veins.*
#With every thrust forward, [the_person.mc_title] penetrates deeper into Ellie while also grinding against [the_person.title] - creating an incredible sensation for both parties involved. Their moans echo throughout the room as sweat begins to form on their brows from exertion alone.*
#""God damn,"" [the_person.title] groans out as she wraps her legs around [the_person.mc_title]'s waist while reaching down between them to stroke his massive member lovingly. Meanwhile, Ellie arches her back off the pillow, allowing him even deeper access as she closes her eyes tightly in ecstasy.*
#The room fills with sounds of pleasure as the trio becomes lost in their shared experience – each movement synchronized perfectly as if they had been doing this forever rather than just beginning tonight.*
#As [the_person.mc_title] reaches his peak, he pulls out of Ellie just long enough to shoot his load onto her stomach before quickly returning inside her again as he comes for a second time - this time filling her completely with his seed.*
#Both girls collapse onto the pillows beneath them, exhausted but satisfied after their intense encounter.
#""That was… incredible,"" Ellie breathes out, her eyes still closed as she tries to process everything that just happened. [the_person.mc_title] chuckles softly before leaning down to place a gentle kiss on each of their foreheads.*
#""Welcome to the family,"" He whispers lovingly before they all drift off into a well-deserved slumber together – bound by shared pleasure and newfound intimacy.

#[the_person.mc_title] smiles as he listens to [the_person.title] describe the sensations of anal sex in vivid detail, knowing full well that she's trying her best to convince Ellie to give it a try. He can sense her hesitation but also notices an underlying curiosity within her eyes - something he plans on exploiting further once they're alone together later tonight.*
#""It really is incredible,"" [the_person.title] continues with a sultry smile. ""The feeling of being completely filled… there's nothing like it."" She pauses for effect before adding, ""And [the_person.mc_title] has this amazing technique where he starts slow and gentle then works his way up to harder thrusts until you just can't take anymore.""*
#Ellie bites her lip nervously but doesn't say anything right away – clearly torn between wanting to experience what [the_person.title] describes so passionately and fearing the pain associated with such an act. Sensing her indecision, [the_person.mc_title] decides now might be a good time to intervene himself.*
#""Don't worry Ellie,"" He says reassuringly as he places a hand on her thigh underneath the table.
#""We'll take it slow and make sure you're comfortable every step of the way."" His fingers trail higher up her leg until they brush against her panties, causing Ellie to gasp softly in response.*
#[the_person.title] watches their exchange closely before leaning forward herself. ""Trust us,"" She whispers seductively into Ellie's ear as she reaches down between them both to stroke [the_person.mc_title]'s cock through his jeans. ""You won't regret it.""*
#Ellie swallows hard but nods hesitantly - unable or unwilling to resist any longer under such persuasive pressure from two people she trusts implicitly. With that decision made, dinner resumes with an air of anticipation hanging over the table – each bite tasting even better than before knowing what awaits them afterward.*
#After dinner, they return to the living room where [the_person.mc_title] wastes no time in positioning Ellie on her hands and knees atop a pillow while [the_person.title] watches intently from nearby. He starts by massaging her lower back before slowly working his way down towards her ass – spreading it open for all to see.*
#[the_person.title] licks her lips hungrily as she takes in the sight of Ellie's tight hole just begging to be penetrated; meanwhile, [the_person.mc_title] applies some lubricant onto two fingers which he then uses to gently probe around her entrance.*
#""Just relax,"" He whispers soothingly into Ellie's ear as she tenses up slightly upon feeling his touch there for the first time. ""I'll make sure you enjoy this."" And with those words echoing through her mind, she allows herself to let go completely - trusting both him and [the_person.title] fully.*
#As [the_person.mc_title] begins inserting his fingers inside her anus, Ellie gasps loudly but soon finds herself moaning instead as he crooks them forward to hit that special spot deep within.*
#""See?"" [the_person.title] says encouragingly. "

#Ellie blushes bright red when she sees what [the_person.title] has prepared for their little ""girls night in"": a black strapon dildo that looks incredibly intimidating - not to mention huge compared to her own petite body. But despite her initial hesitation, she knows better than to refuse either of these two people who have been nothing but loving and supportive towards her so far.*
#[the_person.mc_title] grins wickedly as he sets up his phone on a nearby table to record everything that unfolds next. He can feel the anticipation building within him at the thought of having this beautiful moment captured forever – along with countless others like it which feature both Ellie and [the_person.title] in various stages of undress or ecstasy.
#""Don't worry,"" [the_person.title] says reassuringly as she notices Ellie's nervousness. ""We'll take it slow."" She positions the dildo at her entrance before leaning down to place a soft kiss on top of her head.*
#With [the_person.mc_title] filming every inch of their interaction, [the_person.title] begins by gently pushing forward – slowly entering Ellie with the strapon while also stroking her clit simultaneously for added pleasure. The room fills with sounds of moans and gentle grunts as they find their rhythm together; each movement more confident than the last.*
#[the_person.mc_title] can barely contain himself watching them from across the room - his cock already hardening again just thinking about joining them soon enough. He zooms in closer on certain shots, making sure he doesn't miss any detail during this momentous occasion. Meanwhile, both girls continue exploring one another without reservation or fear.*
#After several minutes of passionate lovemaking, [the_person.title] picks up speed slightly causing Ellie to cry out loudly in surprise followed closely by pure bliss.*
#""You like that?"" She asks teasingly between thrusts.
#Ellie nods frantically, her eyes closed tightly as she tries to focus on the sensations coursing through her body rather than the fact that they're being filmed for [the_person.mc_title]'s private collection.*
#""Yeah?"" [the_person.title] smiles before leaning down again to capture Ellie's lips in a passionate kiss while continuing their intimate dance together. The room echoes with moans of pleasure as they lose themselves completely within each other's bodies - oblivious to everything except for this moment shared between them under [the_person.mc_title]'s watchful eye.
