# the owner can be the screen name or a tag name used by multiple screens,
# If given, this function only returns the tooltip if the focused displayable is part of the screen.
screen default_tooltip(owner = None):
    zorder 1000

    $ tooltip = GetTooltip(screen = owner)
    if tooltip:
        nearrect:
            focus "tooltip"
            preferred_side "top"

            frame:
                xsize 450
                padding (10, 10)
                pos (0.6, 0.0)
                anchor (0.0, 0.0)
                text "[tooltip]":
                    style "serum_text_style"

screen button_tooltip(owner = None):
    zorder 1000

    $ tooltip = GetTooltip(screen = owner)
    if tooltip:
        nearrect:
            focus "tooltip"

            frame:
                background None
                padding (5, 5)
                pos (0.8, 0.0)
                anchor (0.0, 0.0)
                text "[tooltip]":
                    style "serum_text_style"
