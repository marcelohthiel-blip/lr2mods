"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -10 python:
"""

def init_list_of_hairs() -> list[tuple[str, list[float]]]:
    return [
        # Natural Colours
        # Blonde
        ("ash blonde", [0.871, 0.737, 0.6, 0.95]),
        ("barbie blonde", [1, 0.867, 0.624, 0.95]),
        ("bleach blonde", [0.862, 0.815, 0.729, 0.95]),
        ("dirty blonde", [0.663, 0.549, 0.373, 0.95]),
        ("golden blonde", [0.898, 0.784, 0.659, 0.95]),
        ("honey blonde", [0.745, 0.592, 0.471, 0.95]),
        ("light blonde", [0.902, 0.808, 0.659, 0.95]),
        ("platinum blonde", [0.792, 0.749, 0.694, 0.95]),
        ("toasted wheat", [0.848, 0.75, 0.469, 0.95]),
        ("white blonde", [1, 0.961, 0.882, 0.95]),
        # Brown
        ("ash brown", [0.592, 0.475, 0.38, 0.95]),
        ("brown", [0.416, 0.306, 0.259, 0.95]),
        ("chestnut", [0.584, 0.271, 0.208, 0.95]),
        ("chestnut brown", [0.314, 0.157, 0.027, 0.95]),
        ("chocolate brown", [0.21, 0.118, 0.039, 0.95]),
        ("dark brown", [0.231, 0.188, 0.141, 0.95]),
        ("golden brown", [0.333, 0.282, 0.22, 0.95]),
        ("light brown", [0.655, 0.522, 0.416, 0.95]),
        ("medium brown", [0.31, 0.262, 0.247, 0.95]),
        # Neutral
        ("black", [0.035, 0.031, 0.024, 0.95]),
        ("dark grey", [0.443, 0.388, 0.352, 0.95]),
        ("light grey", [0.839, 0.769, 0.761, 0.95]),
        ("medium grey", [0.718, 0.651, 0.62, 0.95]),
        ("off black", [0.173, 0.133, 0.169, 0.95]),
        ("white", [0.95, 0.95, 0.95, 0.95]),
        # Red
        ("crimson", [0.565, 0.062, 0.039, 0.95]),
        ("dark auburn", [0.363, 0.047, 0.039, 0.95]),
        ("ginger red", [0.72, 0.4, 0, 0.95]),
        ("light auburn", [0.459, 0.145, 0.039, 0.95]),
        ("light red", [0.71, 0.322, 0.224, 0.95]),
        ("red", [0.792, 0.208, 0.157, 0.95]),
        ("knight red", [0.745, 0.117, 0.235, 0.95]),
        ("strawberry blonde", [0.647, 0.42, 0.275, 0.95]),

        # Artificial Colours
        ("blue", [0.082, 0.573, 0.792, 0.95]),
        ("sapphire", [0.031, 0.145, 0.404, 0.95]),
        ("sky blue", [0.529, 0.808, 0.922, 0.95]),
        ("turquoise", [0.251, 0.878, 0.816, 0.95]),
        ("dark emerald", [0, 0.278, 0.129, 0.95]),
        ("emerald", [0.314, 0.784, 0.471, 0.95]),
        ("forest green", [0.133, 0.545, 0.133, 0.95]),
        ("hot pink", [1, 0.5, 0.8, 0.95]),
        ("icy pink", [1, 0.733, 0.851, 0.95]),
        ("pastel pink", [0.886, 0.576, 0.576, 0.95]),
        ("fuchsia", [0.408, 0.09, 0.361, 0.95]),
        ("lavender", [0.698, 0.647, 0.804, 0.95]),
        ("purple", [0.329, 0.337, 0.51, 0.95]),
        ("violet", [0.207, 0.051, 0.278, 0.95]),
        ("orange", [1, 0.255, 0.071, 0.95]),
        ("neon red", [1, 0.192, 0.192, 0.95]),
        ("saturated", [0.905, 0.898, 0.513, 0.95]),
        # TODO: Add more hair colours
    ]


def init_list_of_faces():
    return [
        "Face_1",
        "Face_2",
        "Face_3",
        "Face_4",
        "Face_5",
        "Face_6",
        "Face_7",
        "Face_8",
        "Face_9",  # Used to be Mobile Exclusion
        # "Face_10", #Bad render
        "Face_11",  # Used to be Mobile Exclusion
        "Face_12",  # Used to be Mobile Exclusion
        "Face_13",  # Used to be Mobile Exclusion
        "Face_14",  # Used to be Mobile Exclusion
    ]


def init_list_of_eyes() -> list[tuple[str, list[float]]]:
    return [
        ("dark blue", [0.32, 0.60, 0.82, 0.9]),
        ("light blue", [0.60, 0.75, 0.98, 0.9]),
        ("green", [0.35, 0.68, 0.40, 0.9]),
        ("brown", [0.62, 0.42, 0.29, 0.9]),
        ("grey", [0.82, 0.86, 0.86, 0.9]),
        ("emerald", [0.305, 0.643, 0.607, 0.9]),
        ("steel blue", [0.2745, 0.5098, 0.7059, 0.9]),
        ("dark brown", [0.4039, 0.2667, 0.2314, 0.9]),
    ]
