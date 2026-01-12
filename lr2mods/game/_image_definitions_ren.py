from __future__ import annotations
import renpy
from renpy.defaultstore import At
from renpy.display.im import Image

small_icon = None
phone_background = None
other_icons = None
"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -100 python:
"""
def get_file_handle(file_name: str) -> str | None:
    return next((x for x in renpy.exports.list_files() if file_name in x), None)

mod_image = Image(get_file_handle("LR2Mod_idle.png"))
mod_hover_image = Image(get_file_handle("LR2Mod_hover.png"))

info_frame_image = Image(get_file_handle("Info_Frame_1.png"))
goal_frame_image = Image(get_file_handle("Goal_Frame_1.png"))

phone_background = At(Image(get_file_handle("LR2_Phone_Text_Dark.png")), phone_background)
text_bubble_blue = Image(get_file_handle("LR2_Text_Bubble_Blue.png"))
text_bubble_gray = Image(get_file_handle("LR2_Text_Bubble_Gray.png"))
text_bubble_yellow = Image(get_file_handle("LR2_Text_Bubble_Yellow.png"))

portrait_mask_image = Image(get_file_handle("portrait_mask.png"))
empty_image = Image(get_file_handle("empty_holder.png"))

paper_background_image = Image(get_file_handle("Paper_Background.png"))
science_menu_background_image = Image(get_file_handle("Science_Menu_Background.png"))
map_background_image = Image(get_file_handle("map_background_sketch.png"))
IT_background_image = Image(get_file_handle("IT_Background.png"))

serum_slot_full_image = Image(get_file_handle("Serum_Slot_Full.png"))
serum_slot_empty_image = Image(get_file_handle("Serum_Slot_Empty.png"))
serum_slot_incorrect_image = Image(get_file_handle("Serum_Slot_Incorrect.png"))

#Harem/girlfriend/affair
empty_token_small_image = At(Image(get_file_handle("empty_token.png")), small_icon)
renpy.image("empty_token_small", empty_token_small_image)

gf_token_small_image = At(Image(get_file_handle("girlfriend.png")), small_icon)
renpy.image("gf_token_small", gf_token_small_image)

paramour_token_small_image = At(Image(get_file_handle("paramour.png")), small_icon)
renpy.image("paramour_token_small", paramour_token_small_image)

full_star_token_small_image = At(Image(get_file_handle("favourite_star_filled.png")), small_icon)
renpy.image("full_star_token_small", full_star_token_small_image)

empty_star_token_small_image = At(Image(get_file_handle("favourite_star_empty.png")), small_icon)
renpy.image("empty_star_token_small", empty_star_token_small_image)

harem_token_small_image = At(Image(get_file_handle("harem.png")), small_icon)
renpy.image("harem_token_small", harem_token_small_image)

# scaled images
taboo_break_image = At(Image(get_file_handle("taboo_lock_alt.png")), other_icons)
renpy.image("taboo_break", taboo_break_image)
thumbs_up_image = At(Image(get_file_handle("thumbs_up_small.png")), other_icons)
renpy.image("thumbs_up", thumbs_up_image)
thumbs_down_image = At(Image(get_file_handle("thumbs_down_small.png")), other_icons)
renpy.image("thumbs_down", thumbs_down_image)

energy_token_small_image = At(Image(get_file_handle("energy_token.png")), small_icon)
renpy.image("energy_token_small", energy_token_small_image)

arousal_token_small_image = At(Image(get_file_handle("arousal_token.png")), small_icon)
renpy.image("arousal_token_small", arousal_token_small_image)

red_heart_token_small_image = At(Image(get_file_handle("heart/red_heart.png")), small_icon)
renpy.image("red_heart_token_small", red_heart_token_small_image)

gold_heart_token_small_image = At(Image(get_file_handle("heart/gold_heart.png")), small_icon)
renpy.image("gold_heart_token_small", gold_heart_token_small_image)

lust_eye_token_small_image = At(Image(get_file_handle("lust_eye.png")), small_icon)
renpy.image("lust_eye_token_small", lust_eye_token_small_image)

feeding_bottle_token_small_image = At(Image(get_file_handle("feeding_bottle.png")), small_icon)
renpy.image("feeding_bottle_token_small", feeding_bottle_token_small_image)

fertile_token_small_image = At(Image(get_file_handle("fertile_token.png")), small_icon)
renpy.image("fertile_token_small", fertile_token_small_image)

hadsex_token_small_image = At(Image(get_file_handle("hadsex_token.png")), small_icon)
renpy.image("hadsex_token_small", hadsex_token_small_image)

happy_small_image = At(Image(get_file_handle("happy.png")), small_icon)
renpy.image("happy_token_small", happy_small_image)

sad_small_image = At(Image(get_file_handle("sad.png")), small_icon)
renpy.image("sad_token_small", sad_small_image)

underwear_small_image = At(Image(get_file_handle("underwear_token.png")), small_icon)
renpy.image("underwear_token_small", underwear_small_image)

padlock_small_image = At(Image(get_file_handle("padlock.png")), small_icon)
renpy.image("padlock_token_small", padlock_small_image)

triskelion_small_image = At(Image(get_file_handle("triskelion.png")), small_icon)
renpy.image("triskelion_token_small", triskelion_small_image)

question_mark_small_image = At(Image(get_file_handle("question.png")), small_icon)
renpy.image("question_mark_small", question_mark_small_image)

information_small_image = At(Image(get_file_handle("information.png")), small_icon)
renpy.image("information_token_small", information_small_image)

infraction_token_small_image = At(Image(get_file_handle("infraction_token.png")), small_icon)
renpy.image("infraction_token_small", infraction_token_small_image)

speech_bubble_small_image = At(Image(get_file_handle("speech_bubble.png")), small_icon)
renpy.image("speech_bubble_token_small", speech_bubble_small_image)

speech_bubble_exclamation_small_image = At(Image(get_file_handle("speech_bubble_exclamation.png")), small_icon)
renpy.image("speech_bubble_exclamation_token_small", speech_bubble_exclamation_small_image)

phone_token_small_image = At(Image(get_file_handle("phone_token.png")), small_icon)
renpy.image("phone_token_small", phone_token_small_image)

vial_token_small_image = At(Image(get_file_handle("vial.png")), small_icon)
renpy.image("vial_token_small", vial_token_small_image)

vial2_token_small_image = At(Image(get_file_handle("vial2.png")), small_icon)
renpy.image("vial2_token_small", vial2_token_small_image)

vial3_token_small_image = At(Image(get_file_handle("vial3.png")), small_icon)
renpy.image("vial3_token_small", vial3_token_small_image)

dna_token_small_image = At(Image(get_file_handle("dna.png")), small_icon)
renpy.image("dna_token_small", dna_token_small_image)

progress_token_small_image = At(Image(get_file_handle("Progress32.png")), small_icon)
renpy.image("progress_token_small", progress_token_small_image)

stocking_token_small_image = At(Image(get_file_handle("stocking_token.png")), small_icon)
renpy.image("stocking_token_small", stocking_token_small_image)

doggy_style_token_small_image = At(Image(get_file_handle("doggy_style_token.png")), small_icon)
renpy.image("doggy_style_token_small", doggy_style_token_small_image)

drop_down_token_image = Image(get_file_handle("drop_down_token.png")) # size 24 x 24
renpy.image("dropdown_token", drop_down_token_image)

time_advance_token_image = At(Image(get_file_handle("Time_Advance.png")), small_icon)
renpy.image("time_advance", time_advance_token_image)

vial_image = Image(get_file_handle("vial.png"))
vial2_image = Image(get_file_handle("vial2.png"))
vial3_image = Image(get_file_handle("vial3.png"))
dna_image = Image(get_file_handle("dna.png"))
home_image = Image(get_file_handle("home_marker.png"))
feeding_bottle_image = Image(get_file_handle("feeding_bottle.png"))
fertile_image = Image(get_file_handle("fertile_token.png"))
stocking_image = Image(get_file_handle("stocking_token.png"))
doggy_style_image = Image(get_file_handle("doggy_style_token.png"))
