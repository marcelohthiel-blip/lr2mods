"""renpy
init python early:
"""
from renpy.vc_version import version

def versiontuple(v):
    return tuple(map(int, (v.split("."))))

current_version = versiontuple(version)
opt_out_version = versiontuple("8.1.3.0")
print(f"Current version: {version}")
print(f"Opt out version: {opt_out_version}")

FLAG_OPT_IN_ANNOTATIONS = current_version[0] >= opt_out_version[1] and current_version[1] > opt_out_version[1]

print(f"OPT IN ANNOTATIONS: {FLAG_OPT_IN_ANNOTATIONS}")
