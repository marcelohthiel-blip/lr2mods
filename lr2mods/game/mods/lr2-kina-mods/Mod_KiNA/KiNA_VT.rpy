#Counter = KVT01

init -2 python:

    def kina_enabled():
        try:
            return KiNA_MOD
        except NameError:
            return False
            
    def vt_enabled():
        try:
            return VT_MOD
        except NameError:
            return False

    def kaden_enabled():
        try:
            return kaden_mod
        except NameError:
            return False

    def gum_enabled():
        for lbl in renpy.get_all_labels():
            if lbl.startswith("gum_"):
                return True
        return False
        
    def zenpak_enabled():
        try:
            return noncest_version
        except NameError:
            return False

    def moresomes_enabled():
        try:
            return renpy.has_label("bedroom_orgy_label")
        except NameError:
            return False

    def realporn_enabled():
        try:
            return renpy.has_label("describe_girl_climax_RP")
        except NameError:
            return False
#---    

label vt_detected_label():
    $ vt_mod_exists = vt_enabled()
    
    if vt_mod_exists:
        "VT_MOD installed."
    else:
        "VT_MOD NOT installed."
    return