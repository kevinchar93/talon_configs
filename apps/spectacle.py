from talon.voice import Context, Key

context = Context("spectacle")

# Requires: https://www.spectacleapp.com/

keymap = {
    "spec center": Key("alt-cmd-c"),
    "spec full": Key("alt-cmd-f"),
    "spec left": Key("alt-cmd-left"),
    "spec right": Key("alt-cmd-right"),
    "spec top": Key("alt-cmd-up"),
    "spec bottom": Key("alt-cmd-down"),
    # "spec up left": Key("ctrl-cmd-left"),
    # "spec low left": Key("ctrl-shift-cmd-left"),
    # "spec up right": Key("ctrl-cmd-right"),
    # "spec low right": Key("ctrl-shift-cmd-right"),
    "spec next": Key("ctrl-alt-cmd-right"),
    "spec previous": Key("ctrl-alt-cmd-left"),
    # "spec next slice": Key("ctrl-alt-right"),
    # "spec (previous | last) slice": Key("ctrl-alt-left"),
    # "spec grow": Key("ctrl-alt-shift-right"),
    # "spec shrink": Key("ctrl-alt-shift-left"),
    "spec undo": Key("alt-cmd-z"),
    "spec redo": Key("alt-shift-cmd-z"),
    "diffie up": Key("alt-cmd-ctrl-up"),
    "diffie down": Key("alt-cmd-ctrl-down"),
    "diffie left": Key("alt-cmd-ctrl-shift-left"),
    "diffie right": Key("alt-cmd-ctrl-shift-right"),
    "diffie (full | fullscreen)": Key("alt-cmd-ctrl-shift-up"),
    "diffie present": [Key("alt-cmd-ctrl-shift-up"), Key("alt-cmd-ctrl-shift-up")],
    "diffie center": Key("alt-cmd-ctrl-shift-down"),
}

context.keymap(keymap)
